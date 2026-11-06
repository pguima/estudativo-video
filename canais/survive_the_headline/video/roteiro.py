"""Gera episodes/<ep>/roteiro.md (só as falas, marcadas por quem fala: [narrador], [Dan], [Bea]...)
e episodes/<ep>/roteiro_tecnico.md (cena, câmera, impactos e som de cada plano, com tempos reais).

    py video/roteiro.py ep01-ai-bubble

Lê episode.js, voz.js e trilha.json, então os tempos são os da voz real. O arquivo é gerado: para mudar o
vídeo, edite episode.js e trilha.json e rode de novo.
"""
import asyncio
import json
import re
import sys
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
ep = sys.argv[1]
base = ROOT / 'episodes' / ep

DUMP = r"""() => {
  const cena = o => { const r = {}; Object.keys(o || {}).forEach(k => { const a = o[k]; r[k] = { pose: a.pose || '', expr: a.expr || '', outfit: a.outfit || '' }; }); return r; };
  const cam = c => typeof c === 'string' ? c : Array.isArray(c) ? { a: c[0], b: c[1] } : c ? { a: c.a, b: c.b } : 'push';
  return EP.shots.map(s => ({
    i: s.i, id: s.id, start: s.start, dur: s.dur, n: s.n || '', who: s.who || '', bg: s.bg || '', mood: s.mood || '', hold: s.hold || 0,
    bars: !!s.bars, dof: !!s.dof, flicker: s.flicker || 0, prop: s.prop || '', tin: s.tin || '', tout: s.tout || '',
    clock: s.clock || null, hud: s.hud || null, card: s.card ? String(s.card) : '', gfx: s.gfx ? String(s.gfx) : '', title: s.title || '', sub: s.sub || '',
    cast: cena(s.cast), crowd: Array.isArray(s.crowd) ? s.crowd.map(e => e.role) : [], walks: (s.walks || []).map(w => w.who),
    cam: s.cuts ? null : cam(s.cam),
    cuts: (s.cuts || []).map(c => ({ at: c.at, t: Camera.when(s, c.at || 0), cam: cam(c.cam) })),
    hits: (s.hits || []).map(h => ({ at: h.at, t: Camera.when(s, h.at), stamp: h.stamp || '', flash: h.flash || '', shake: h.shake || 0, punch: h.punch || 0 }))
  }));
}"""

CEN = dict(trading_floor='Pregão da bolsa', street='Rua do bairro', house_exterior='Frente da casa dos Rivera', kitchen='Cozinha', garage='Garagem', hospital='Hospital',
           bedroom_kids='Quarto das crianças', bedroom_parents='Quarto do casal', living_room='Sala', datacenter_site='Obra do data center', datacenter_closed='Obra parada',
           school='Escola', news_desk='Telejornal simulado', supermarket='Supermercado', office='Banco', void_red='Fundo vermelho', void_night='Fundo noturno',
           void_amber='Fundo âmbar', void_green='Fundo verde')
MOOD = dict(dusk='fim de tarde', night='noite', dark='escuro', tense='tensão')
ELENCO = dict(dan='Dan', mia='Mia', leo='Leo', bea='Bea', biscuit='Biscuit')
PAPEL = dict(crew='operário', trader='operador', office='professor/funcionário', nurse='enfermeira', doctor='médico', student='aluno', kid='criança', shopper='cliente',
             cashier='atendente', neighbor='vizinho', anchor='âncora', agent='atendente do banco', boss='chefe de obra')
PLURAL = dict(crew='operários', trader='operadores', office='professores/funcionários', nurse='enfermeiras', doctor='médicos', student='alunos', kid='crianças', shopper='clientes',
              cashier='atendentes', neighbor='vizinhos', anchor='âncoras', agent='atendentes do banco', boss='chefes de obra')
POSE = dict(standing='em pé', idle='parada', explaining='explicando', pointing='apontando', hands_on_head='mãos na cabeça', arms_crossed='braços cruzados', shrugging='dando de ombros',
            running='correndo', sitting='sentado', working='trabalhando', walking='andando', hands_on_hips='mãos na cintura', thinking='pensando', worried='aflita', comforting='consolando',
            using_phone='no celular', hugging='abraçando', excited='animada', asking_question='perguntando', hands_on_cheeks='mãos no rosto', lying_down='deitado', begging='pedindo', hiding='escondido')
EXPR = dict(neutral='neutro', happy='feliz', worried='preocupado', shocked='chocado', scared='assustado', angry='com raiva', sad='triste', determined='determinado', surprised='surpreso',
            thinking='pensativo', talking='falando', skeptical='cético', reassuring='tranquilizador', confident='confiante', embarrassed='envergonhado', guilty='culpado', excited='animado')
HUD = dict(cash='dinheiro', food='comida', power='energia', stress='estresse', health='saúde')
FAIXA = dict(cordas='cordas', luz='cordas claras', baixo='baixo', metal='metais', tema='tema', alto='tema agudo', coro='coro', piano='piano', taiko='tambores', caixa='caixa', prato='pratos', tick='tique-taque')
FX = dict(sting='impacto de logo', subida='subida', sino='sino do pregão', vibra='celular vibrando', toque='telefone tocando', caixa='bipe de caixa', crash='prato', tambor='tambor',
          final='acorde sem resolução', tique='tique')


def tempo(t):
    return f'{int(t // 60):02d}:{t % 60:04.1f}'


def nome(w):
    return ELENCO.get(w, w)


def camera(c):
    if isinstance(c, str):
        p = c.split(':')
        k = p[0]
        q = dict(wide='plano aberto', push='aproximação lenta', pull='afastamento lento', hold='câmera parada', drift='deriva lenta', rack='troca de foco')
        if k in q:
            return q[k]
        if k == 'close':
            return f'close em {nome(p[1])}'
        if k == 'ecu':
            return f'superclose em {nome(p[1])}'
        if k == 'crash':
            return f'zoom rápido em {nome(p[1])}'
        if k == 'vertigo':
            return f'efeito vertigem em {nome(p[1])}'
        if k == 'dutch':
            return f'câmera inclinada em {nome(p[1])}'
        if k == 'pan':
            return f'panorâmica de {nome(p[1])} para {nome(p[2])}'
        if k == 'track':
            return f'acompanha {nome(p[1])}'
        if k == 'tilt':
            return f'sobe por {nome(p[1])}'
        return c
    a, b = c.get('a'), c.get('b')
    if a and b:
        z0, z1 = a[2], b[2]
        tipo = 'aproxima' if z1 > z0 + 0.01 else 'afasta' if z1 < z0 - 0.01 else 'desloca'
        return f'movimento livre, {tipo} (zoom {z0} → {z1})'.replace('.', ',')
    return 'movimento livre'


def impacto(h):
    p = []
    if h['stamp']:
        p.append(f"carimbo “{h['stamp']}”")
    if h['flash']:
        p.append('clarão')
    if h['shake'] >= 14:
        p.append('tremor forte')
    elif h['shake']:
        p.append('tremor')
    if h['punch']:
        p.append('soco de zoom')
    return ' + '.join(p) or 'batida'


def tela(s):
    src = s['gfx'] or s['card']
    if not src:
        return ''
    tipo = re.search(r'G\.(\w+)', src)
    tipo = tipo.group(1) if tipo else ''
    NOME = dict(headline='Manchete', ledger='Tabela de contas', chart='Gráfico', big='Número grande', loop='Diagrama do ciclo', bars='Barras', phone='Tela de celular', ripple='Ondas do impacto',
                choice='Opções A e B', verdict='Nota final', actions='Três atitudes', end='Tela final', logo='Logo do canal', day='Cartão de dia')
    txt = [re.sub(r'\\|<br>', ' ', m) for m in re.findall(r"(?:title|n|label|kicker|tag|sub|source|next):\s*(['\"])(.*?)\1", src) for m in [m[1]]]
    return NOME.get(tipo, tipo or 'Tela') + (': ' + ' · '.join(txt) if txt else '')


def marcar(s):
    """põe cada marcação logo depois da palavra em que acontece"""
    ws = s['n'].split()
    norm = [re.sub(r'[^a-z0-9$%-]', '', w.lower()) for w in ws]
    tags = {}

    def poe(at, txt):
        if not (isinstance(at, str) and at.startswith('@')):
            return
        w, _, nth = at[1:].lower().partition('#')
        ach = [k for k, x in enumerate(norm) if x.startswith(w)]
        if ach:
            tags.setdefault(ach[min(int(nth or 1) - 1, len(ach) - 1)], []).append(txt)
    for c in s['cuts']:
        poe(c['at'], 'corte')
    for h in s['hits']:
        poe(h['at'], h['stamp'] and f"carimbo: {h['stamp']}" or 'impacto')
    return ' '.join(f"**{w}** `[{' · '.join(tags[k])}]`" if k in tags else w for k, w in enumerate(ws))


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        await pg.goto((ROOT / 'video' / 'player.html').as_uri() + f'?ep={ep}')
        await pg.wait_for_function('window.playerReady', timeout=60000)
        shots = await pg.evaluate(DUMP)
        await b.close()
    cfg = json.loads((base / 'trilha.json').read_text(encoding='utf8'))
    total = shots[-1]['start'] + shots[-1]['dur']
    pal = sum(len(s['n'].split()) for s in shots)
    L = [f'# Roteiro técnico: {ep}', '',
         f'Duração: **{int(round(total) // 60)}min{int(round(total) % 60):02d}s** · **{len(shots)} planos** · {pal} palavras narradas.',
         'Arquivo gerado por `py video/roteiro.py`: as alterações são feitas em `episode.js` e `trilha.json`.', '',
         '> Rascunho. A história é uma simulação: os dados reais e o que foi inventado estão em [fontes.md](fontes.md).', '',
         '## Como ler', '',
         '- **Tempo:** início do plano no vídeo final (minutos:segundos), já com a voz real.',
         '- **Palavra em negrito com `[marcação]`:** o evento acontece nessa palavra.',
         '- **Som:** só aparece o que é específico do plano. Transições, impactos, painel e ambiente do cenário têm efeito automático.',
         '- Narração e falas ficam em inglês, como no vídeo.', '']
    L += ['## Mapa da trilha', '', '| Tempo | Início | Faixas |', '|---|---|---|']
    ini = {s['id']: s['start'] for s in shots}
    for sc in sorted(cfg['secoes'], key=lambda x: ini[x['de']] + x.get('t', 0)):
        fx = ', '.join(FAIXA.get(k, k) for k, v in sorted(sc['faixas'].items(), key=lambda kv: -kv[1])) or 'silêncio'
        L.append(f"| {tempo(ini[sc['de']] + sc.get('t', 0))} | {sc['de']} | {fx} |")
    dias = dict(re.findall(r"day\('([^']+)', '([^']+)'\)", (base / 'episode.js').read_text(encoding='utf8')))
    L += ['', '## Roteiro', '']
    for s in shots:
        if s['card'] and s['id'] != 'logo':
            sub = dias.get(s['id'])
            L += [f"### {s['id']}" + (f": {sub}" if sub else ''), '']
            L += [f"**{tempo(s['start'])}** · cartão de dia, {s['dur']:.1f} s", '']
            continue
        L.append(f"#### {tempo(s['start'])} · `{s['id']}` · {s['dur']:.1f} s")
        L.append('')
        if s['n']:
            quem = nome(s['who']).upper() if s['who'] else 'NARRADOR'
            L += [f"> **{quem}:** {marcar(s)}", '']
        else:
            L += ['> *(sem narração)*', '']
        info = []
        if s['bg']:
            c = CEN.get(s['bg'], s['bg'])
            ex = [x for x in (MOOD.get(s['mood']), 'tarjas de cinema' if s['bars'] else '', 'luz piscando' if s['flicker'] else '', 'fundo desfocado' if s['dof'] else '') if x]
            info.append(f"**Cena:** {c}" + (f" ({', '.join(ex)})" if ex else ''))
        if s['cast']:
            els = [f"{nome(k)}" + (f" ({', '.join(x for x in (POSE.get(v['pose'], v['pose']), EXPR.get(v['expr'], v['expr'])) if x)})" if v['pose'] or v['expr'] else '') for k, v in s['cast'].items()]
            info.append('**Elenco:** ' + '; '.join(els))
        if s['crowd']:
            cont = {}
            for r in s['crowd']:
                cont[r] = cont.get(r, 0) + 1
            info.append('**Figurantes:** ' + ', '.join(f'{v} {(PLURAL if v > 1 else PAPEL).get(k, k)}' for k, v in cont.items()))
        t = tela(s)
        if t:
            info.append('**Tela:** ' + t)
        if s['clock']:
            info.append('**Relógio:** ' + ' · '.join(s['clock']))
        if s['hud']:
            info.append('**Painel:** ' + ', '.join(f'{HUD.get(k, k)} {v}' for k, v in s['hud'].items()))
        if s['cuts']:
            info.append('**Câmera:** ' + ' → '.join(f"{tempo(s['start'] + c['t'])} {camera(c['cam'])}" for c in s['cuts']))
        elif s['cam']:
            info.append('**Câmera:** ' + camera(s['cam']))
        if s['hits']:
            info.append('**Impactos:** ' + '; '.join(f"{tempo(s['start'] + h['t'])} {impacto(h)}" for h in s['hits']))
        som = [f"trilha muda ({', '.join(FAIXA.get(k, k) for k in sc['faixas']) or 'silêncio'})" + (f" aos {sc['t']} s" if sc.get('t') else '') for sc in cfg['secoes'] if sc['de'] == s['id']]
        som += [FX.get(e['fx'], e['fx']) + (f" aos {e['t']} s" if e.get('t') else '') for e in cfg['eventos'] if e['plano'] == s['id']]
        if s['id'] in cfg.get('abaixa', {}):
            g = cfg['abaixa'][s['id']]
            som.append(f"trilha {'reforçada' if g > 1 else 'abaixada'} ({g:.2f}x)".replace('.', ','))
        if som:
            info.append('**Som:** ' + '; '.join(som))
        L += [f'- {x}' for x in info] + ['']
    dst = base / 'roteiro_tecnico.md'
    dst.write_text('\n'.join(L).rstrip() + '\n', encoding='utf8')
    print(dst, len(L), 'linhas')
    # só as falas
    R = [f'# Roteiro: {ep}', '']
    falas = 0
    for s in shots:
        if s['card'] and s['id'] != 'logo':
            R += [f"## {s['id']}" + (f": {dias[s['id']]}" if s['id'] in dias else ''), '']
        elif s['n']:
            R += [f"[{nome(s['who']) if s['who'] else 'narrador'}] {s['n']}", '']
            falas += 1
    dst = base / 'roteiro.md'
    dst.write_text('\n'.join(R).rstrip() + '\n', encoding='utf8')
    print(dst, falas, 'falas')


asyncio.run(main())
