"""Alinha a voz gerada ao roteiro, plano a plano.

    py video/alinhar.py ep01-ai-bubble --corte ads

Entrada: audio/palavras.json (transcrever_palavras.py) e output/planos.json.
Saída: audio/tempos.json, com o trecho de cada parte que pertence a cada plano e o tempo de cada palavra.
Lista as diferenças entre roteiro e transcrição: é a conferência de que a voz não pulou, repetiu ou improvisou.
"""
import argparse
import difflib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser(); ap.add_argument('ep'); ap.add_argument('--corte', required=True); a = ap.parse_args()
base = ROOT / 'episodes' / a.ep
planos = json.loads((base / 'output' / 'planos.json').read_text(encoding='utf8'))
trans = json.loads((base / 'audio' / 'palavras.json').read_text(encoding='utf8'))
corte = next(s['i'] for s in planos if s['id'] == a.corte)
norm = lambda w: re.sub(r"[^a-z0-9]", '', w.lower())
cuts = {}
tot_dif = 0

for n, tr in enumerate(trans, 1):
    nar = [s for s in planos if s['n'] and not s['who'] and ((s['i'] < corte) == (n == 1))]
    rot = [(s['i'], w) for s in nar for w in s['n'].split()]
    A = [norm(w) for _, w in rot]; W = tr['words']; B = [norm(w['w']) for w in W]
    sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
    idx = [None] * len(A)
    idw = [None] * len(A)   # só para o tempo das palavras: inclui as que a transcrição grafou diferente
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1):
                idx[i1 + k] = idw[i1 + k] = j1 + k
        else:
            tot_dif += 1
            if tag == 'replace':
                for k in range(i2 - i1):
                    idw[i1 + k] = j1 + (k * (j2 - j1)) // (i2 - i1)
            print(f'parte {n} [{tag}] t={W[min(j1, len(W) - 1)]["s"]:.1f}s  roteiro: {" ".join(w for _, w in rot[i1:i2])!r}  ->  voz: {" ".join(w["w"] for w in W[j1:j2])!r}')
    print(f'parte {n}: {sm.ratio():.3f} de semelhança, {len(A)} palavras no roteiro, {len(B)} na voz')
    # primeira e última palavra reconhecida de cada plano
    for s in nar:
        pos = [k for k, (i, _) in enumerate(rot) if i == s['i']]
        ok = [idx[k] for k in pos if idx[k] is not None]
        if not ok:
            raise SystemExit(f'plano {s["id"]}: nenhuma palavra reconhecida')
        cuts[s['i']] = dict(id=s['id'], parte=n, j0=ok[0], j1=ok[-1], words=[(rot[k][1], idw[k]) for k in pos])
    # corte no meio do silêncio entre um plano e o seguinte
    for x, y in zip(nar, nar[1:]):
        cx, cy = cuts[x['i']], cuts[y['i']]
        e, s0 = W[cx['j1']]['e'], W[cy['j0']]['s']
        m = (e + s0) / 2 if s0 > e else e
        cx['b'] = round(m, 3); cy['a'] = round(m, 3)
    cuts[nar[0]['i']]['a'] = max(0.0, W[cuts[nar[0]['i']]['j0']]['s'] - 0.1)
    cuts[nar[-1]['i']]['b'] = min(tr['dur'], W[cuts[nar[-1]['i']]['j1']]['e'] + 0.4)
    for s in nar:
        c = cuts[s['i']]
        c['wt'] = [[w, round(W[j]['s'] - c['a'], 3) if j is not None else None] for w, j in c.pop('words')]
        c.pop('j0'); c.pop('j1')

curtos = [(c['id'], round(c['b'] - c['a'], 2), len(c['wt'])) for c in cuts.values() if (c['b'] - c['a']) < len(c['wt']) * 0.18]
print('planos curtos demais para o texto:', curtos)
(base / 'audio' / 'tempos.json').write_text(json.dumps(cuts, ensure_ascii=False, indent=0), encoding='utf8')

# voz.js: o que o player precisa saber. LEAD = respiro antes da fala, TAIL = depois da última palavra
LEAD, TAIL = 0.12, 0.12
voz = {}
for c in cuts.values():
    wt, n = c['wt'], len(c['wt'])
    known = [(k, t) for k, (_, t) in enumerate(wt) if t is not None]
    fill = []
    for k, (w, t) in enumerate(wt):      # palavra que a transcrição grafou diferente: interpola
        if t is None:
            a0 = max(((i, x) for i, x in known if i < k), default=(0, 0.0))
            b0 = min(((i, x) for i, x in known if i > k), default=(n, c['b'] - c['a']))
            t = a0[1] + (b0[1] - a0[1]) * (k - a0[0]) / max(b0[0] - a0[0], 1)
        fill.append([re.sub(r'[^a-z0-9$%-]', '', w.lower()), round(t + LEAD, 3)])
    voz[c['id']] = dict(d=round(LEAD + c['b'] - c['a'] + TAIL, 3), wt=fill)
for s in planos:
    if s['who']:
        import wave
        with wave.open(str(base / 'audio' / f"{s['id']}.wav")) as w:
            voz[s['id']] = dict(d=round(0.15 + w.getnframes() / w.getframerate() + 0.25, 3))
(base / 'voz.js').write_text('self.EP_VOZ = ' + json.dumps(voz, ensure_ascii=False) + ';\n', encoding='utf8')
print('diferenças:', tot_dif, '· fala total:', round(sum(v['d'] for v in voz.values()), 1), 's')
