"""Visual — Estudativo · MAT-LEI-006: escolher a melhor opção.

Linguagem da trilha Leitura de Problemas (as peças abaixo de "linguagem da trilha" servem a todas as aulas MAT-LEI):
- enunciado(): o problema num cartão branco com fio da cor da matéria. Os números são escritos em grotesca; a pergunta fica numa
  linha própria. marca = marca-texto da cor da matéria (dado útil), aponta = caixa pontilhada (dado em dúvida),
  risca = traço vermelho e número cinza (dado que não entra na conta).
- garrafa() e pacote(): a garrafa com o volume no rótulo e o pacote de latas (4 ou 6), com a etiqueta de preço embaixo.
- tabela(): as opções que fecham a quantidade, uma linha por compra; a linha descartada é riscada e a melhor acende em verde.
Todo instante vem de C[...] (marcadores do roteiro) ou de pal() (a palavra na voz real)."""
import json
from pathlib import Path
import re
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Leitura de Problemas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-LEI-006_escolher_a_melhor_opcao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("litro", "latas", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula, conferidas (em centavos)
assert 700 / 2 == 350 and 540 / 1.5 == 360 and 54 / 15 == 3.6 and 360 - 350 == 10
assert 1000 / 4 == 250 and 1380 / 6 == 230 and 4 * 1000 == 4000 and (16 - 6) % 4 != 0
assert 2 * 1380 == 2760 and 2760 + 1000 == 3760 and 3 * 6 > 16 and 3 * 1380 == 4140 and 18 - 16 == 2
assert 600 / 4 == 150 and 840 / 6 == 140 and 3 * 6 + 4 == 22 and 3 * 840 == 2520 and 2520 + 600 == 3120
assert 6 + 4 * 4 == 22 and 840 + 4 * 600 == 3240 and 3240 > 3120


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- instante de uma palavra na voz ----------------
_T = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))
_TOK = {s["id"]: (s["start"], s["tokens"]) for s in _T["scenes"]}


def pal(sid, palavra, n=1):
    """instante em que a n-ésima ocorrência de `palavra` começa na cena sid"""
    st, toks = _TOK[sid]
    k = 0
    for tk in toks:
        if tk["disp"].lower().strip(".,:;!?") == palavra:
            k += 1
            if k == n:
                return st + tk["t0"]
    raise KeyError((sid, palavra, n))


# ---------------- peças gerais ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + size * 0.36, size, "g", M.on(cor or E.COR), a)))


# ---------------- linguagem da trilha Leitura de Problemas ----------------
_PEDACO = re.compile(r"\[([^|\]]+)\|(\w+)\]")


def _tokens(txt):
    """'Uma escola tem [8 turmas|tur].' -> [('Uma', None), ('escola', None), ('tem', None), ('8 turmas', 'tur'), ('.', None)]"""
    out, i = [], 0
    for m in _PEDACO.finditer(txt):
        out += [(w, None) for w in txt[i:m.start()].split()]
        out.append((m.group(1), m.group(2)))
        i = m.end()
    out += [(w, None) for w in txt[i:].split()]
    return out


def _layout(linha, x, size, pergunta):
    """x de cada pedaço da linha; pontuação cola no pedaço anterior"""
    pos, xx = [], x
    for j, (s, k) in enumerate(linha):
        est = "b" if (k or pergunta) else "i"
        sz = size * 0.9 if est == "b" else size
        if j and not s[0] in ".,:;?!":
            xx += size * 0.25
        w = E.larg(s, est, sz)
        pos.append((s, k, est, sz, xx, xx + w))
        xx += w
    return pos


def enunciado(c, t, x, y, w, linhas, size=60, dy=None, t_card=None, marca=None, risca=None, aponta=None):
    """o problema num cartão. linhas = [(t0, "texto com [número|chave]"[, True se for a pergunta])].
    marca / risca / aponta = {chave: instante}; a chave "q" marca a pergunta inteira. Devolve {chave: (x0, x1, base)}"""
    marca, risca, aponta = marca or {}, risca or {}, aponta or {}
    dy = dy or size * 1.62
    pad = size * 0.85
    h = pad * 2 + size * 1.05 + dy * (len(linhas) - 1)
    t_card = linhas[0][0] - 0.3 if t_card is None else t_card

    def cartao(a):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26)
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 18))
        c.save(); c.translate(6, 14); c.drawRRect(r, s); c.restore()
        c.drawRRect(r, M.paint(BR, a))
        c.save(); c.clipRRect(r, True)
        c.drawRect(skia.Rect.MakeXYWH(x, y, 14, h), M.paint(E.COR, a))
        c.restore()
    E.foco(c, t, t_card, 0.5, cartao, blur=8)
    onde = {}
    for i, ln in enumerate(linhas):
        t0, txt = ln[0], ln[1]
        pergunta = len(ln) > 2 and ln[2]
        base = y + pad + size * 0.78 + i * dy
        pos = _layout(_tokens(txt), x + pad + 14, size, pergunta)
        if pergunta:
            onde["q"] = (pos[0][4], pos[-1][5], base)
        for s, k, est, sz, x0, x1 in pos:
            if k:
                onde[k] = (x0, x1, base)
        if t < t0:
            continue
        # marca-texto atrás dos pedaços úteis
        for k, (x0, x1, b_) in list(onde.items()):
            if b_ != base or k not in marca or t < marca[k]:
                continue
            p = ease_io(prog(t, marca[k], 0.45))
            M.rrect(c, x0 - 12, base - size * 0.8, (x1 - x0 + 24) * p, size * 1.08, 12, E.COR, 0.16)

        def texto(a, pos=pos, pergunta=pergunta):
            for s, k, est, sz, x0, x1 in pos:
                kk = "q" if pergunta else k
                cor = TINTA
                if kk and kk in marca and t >= marca[kk]:
                    cor = COR
                if kk and kk in risca and t >= risca[kk] + 0.2:
                    cor = CINZA
                E.escreve(c, s, x0, base, sz, est, cor, a)
        E.foco(c, t, t0, 0.5, texto, sobe=10)
    for k, ta in aponta.items():
        if k in onde and t >= ta and (k not in risca or t < risca[k] + 0.4):
            x0, x1, b_ = onde[k]
            q = ep(t, ta, 0.35) * (1 - ep(t, risca.get(k, 1e9), 0.4))
            E.caixa_pontilhada(c, x0 - 14, b_ - size * 0.86, x1 - x0 + 28, size * 1.16, q, ERRADO, prog_=ep(t, ta, 0.35))
    for k, tr in risca.items():
        if k in onde and t >= tr:
            x0, x1, b_ = onde[k]
            E.risco(c, x0 - 10, b_ - size * 0.3, x1 + 10, b_ - size * 0.3, t, tr, ERRADO, 8)
    return onde


def pessoa(c, cx, base, h, cor=TINTA, a=1.0):
    """bonequinho de pé, com os pés em base"""
    if a <= 0:
        return
    c.drawCircle(cx, base - h * 0.84, h * 0.15, M.paint(cor, a))
    M.rrect(c, cx - h * 0.17, base - h * 0.64, h * 0.34, h * 0.64, h * 0.12, cor, a)


def lista(c, t, C, ini, itens, n_txt):
    """'você só precisa de N coisas' com as caixas pontilhadas"""
    E.frase(c, t, C[ini] + 0.5, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[itens[0][0]] - 0.4, 0.5, lambda a: E.escreve(c, n_txt, XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[itens[0][0]] - 0.25, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    y0, dy = (250, 280) if len(itens) == 2 else (170, 240)
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * dy
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    py = y0 + 170
    for i, (k, _, _) in enumerate(itens[1:], 1):
        py = lerp(py, y0 + i * dy + 170, ease_io(prog(t, C[k] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C[itens[0][0]], 0.4))



def tabela(c, t, x, y, larg, cab, linhas, t_cab, h=96, size=60, escuro=False, verde=None, cor_cab=None):
    """tabela de palpites. cab = títulos; linhas = [(t0, [células])], célula = texto ou (texto, cor);
    verde = (índice da linha, instante): a linha da resposta acende. Devolve (x de cada coluna, y de cada linha)"""
    tinta = BR if escuro else TINTA
    total = sum(larg)
    xs, xx = [], x
    for w in larg:
        xs.append(xx + w / 2)
        xx += w

    def topo(a):
        M.rrect(c, x, y, total, h, 18, cor_cab or E.COR, a)
        for s, cx in zip(cab, xs):
            centro(c, s, cx, y + h / 2 + size * 0.3, size * 0.8, "b", BR, a)
    E.foco(c, t, t_cab, 0.5, topo)
    ys = []
    if verde is not None and t >= verde[1]:
        q = ep(t, verde[1], 0.4)
        yy = y + h * (verde[0] + 1)
        M.rrect(c, x - 6, yy + 4, total + 12, h - 8, 16, CERTO, 0.16 * q)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 6, yy + 4, total + 12, h - 8), 16, 16), M.paint(CERTO, q, stroke=4))
    for i, (t0, cel) in enumerate(linhas):
        yy = y + h * (i + 1)
        ys.append(yy + h / 2)

        def linha_(a, yy=yy, cel=cel):
            M.line(c, x, yy + h, x + total, yy + h, CINZA if escuro else FIO, a, 2)
            for s, cx in zip(cel, xs):
                cor = tinta
                if isinstance(s, tuple):
                    s, cor = s
                centro(c, s, cx, yy + h / 2 + size * 0.36, size, "g", cor, a)
        E.foco(c, t, t0, 0.45, linha_, sobe=8)
    return xs, ys




def risca_linha(c, t, t0, x0, x1, y, cor=ERRADO):
    E.risco(c, x0, y, x1, y, t, t0, cor, 7, 0.5)


# ---------------- garrafas e pacotes ----------------
def garrafa(c, cx, base, h, rot, cor=None, a=1.0):
    """garrafa de pé, com o volume no rótulo; base = fundo"""
    if a <= 0:
        return
    cor = cor or E.COR
    w = h * 0.42
    sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + 6, base - h * 0.78 + 12, w, h * 0.78), w * 0.2, w * 0.2), sh)
    p = skia.Path()
    p.moveTo(cx - w / 2, base - h * 0.62)
    p.cubicTo(cx - w / 2, base - h * 0.8, cx - w * 0.18, base - h * 0.8, cx - w * 0.18, base - h * 0.9)
    p.lineTo(cx + w * 0.18, base - h * 0.9)
    p.cubicTo(cx + w * 0.18, base - h * 0.8, cx + w / 2, base - h * 0.8, cx + w / 2, base - h * 0.62)
    p.lineTo(cx + w / 2, base - w * 0.15)
    p.quadTo(cx + w / 2, base, cx + w / 2 - w * 0.15, base)
    p.lineTo(cx - w / 2 + w * 0.15, base)
    p.quadTo(cx - w / 2, base, cx - w / 2, base - w * 0.15)
    p.close()
    c.drawPath(p, M.paint(E.mix(cor, BR, 0.75), a))
    c.drawPath(p, M.paint(cor, a, stroke=5))
    M.rrect(c, cx - w * 0.22, base - h, w * 0.44, h * 0.1, 6, cor, a)
    M.rrect(c, cx - w / 2 + 2, base - h * 0.5, w - 4, h * 0.26, 4, cor, a)
    centro(c, rot, cx, base - h * 0.37 + h * 0.06, h * 0.12, "g", BR, a)


def lata(c, x, y, w, h, cor, a):
    M.rrect(c, x, y, w, h, w * 0.18, cor, a)
    M.rrect(c, x + w * 0.12, y + h * 0.12, w * 0.76, h * 0.1, 4, E.mix(cor, BR, 0.5), a)
    M.rrect(c, x + w * 0.12, y + h * 0.45, w * 0.76, h * 0.22, 4, BR, 0.35 * a)


def pacote(c, cx, base, n, s=1.0, cor=None, a=1.0):
    """pacote com n latas (4 = 2 × 2, 6 = 3 × 2) visto de frente; base = fundo"""
    if a <= 0:
        return
    cor = cor or E.COR
    cols = 2 if n == 4 else 3
    lw, lh, g = 70 * s, 120 * s, 12 * s
    w = cols * lw + (cols + 1) * g
    h = 2 * lh + 3 * g
    x0, y0 = cx - w / 2, base - h
    M.rrect(c, x0, y0, w, h, 18 * s, BR, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y0, w, h), 18 * s, 18 * s), M.paint(TINTA, a, stroke=3))
    for i in range(n):
        r, k = divmod(i, cols)
        lata(c, x0 + g + k * (lw + g), y0 + g + r * (lh + g), lw, lh, cor, a)


def etiqueta(c, cx, y, s, a=1.0, cor=TINTA, size=60):
    """preço numa etiqueta branca"""
    if a <= 0:
        return
    w = E.larg(s, "g", size) + size * 1.0
    M.rrect(c, cx - w / 2, y - size * 1.05, w, size * 1.5, 14, BR, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y - size * 1.05, w, size * 1.5), 14, 14), M.paint(cor, a, stroke=3))
    centro(c, s, cx, y, size, "g", cor, a)


# ---------------- gancho ----------------
GA, GB, GY = 560, 1360, 660  # garrafa de 1,5 L, garrafa de 2 L, base


def duas_garrafas(c, t, ta, tb, verde=None, tam=1.0):
    E.foco(c, t, ta, 0.5, lambda a: (garrafa(c, GA, GY, 380 * tam, "1,5 L", a=a), etiqueta(c, GA, GY + 110, "R$ 5,40", a)))
    E.foco(c, t, tb, 0.5, lambda a: (garrafa(c, GB, GY, 440 * tam, "2 L", a=a), etiqueta(c, GB, GY + 110, "R$ 7,00", a)))
    if verde is not None and t >= verde:
        q = ep(t, verde, 0.4)
        E.caixa_pontilhada(c, GB - 210, GY - 470, 420, 620, q, CERTO, prog_=q)


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def cena():
        E.frase(c, t, C["s01"], ps("qual sai mais em conta?", "i", 76), W / 2, 150, "center", 0.12)
        duas_garrafas(c, t, a1, b1, c1)
        E.frase(c, t, pal("s01", "etiqueta"), ps("a etiqueta menor", "i", 70) + [("engana", "g", 74, ERRADO)], GA, 950, "center", 0.1)
        E.frase(c, t, c1 + 0.2, [("mais em conta", "g", 74, CERTO)], GB, 950, "center")
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 86), XE, 300, passo=0.12)
        E.frase(c, t, pal("s02", "compara"), [("comparar preços", "g", 96, COR)], XE, 450, passo=0.12)
        E.frase(c, t, pal("s02", "monta"), ps("e montar a", "i", 86), XE, 590, passo=0.12)
        E.frase(c, t, pal("s02", "compra"), [("compra mais barata", "g", 90, COR)], XE, 710, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lista(c, t, C, "s03", (("s03.a", "numa taxa, por", "quer dizer dividido por"), ("s03.b", "opções se organizam", "numa tabela")), "2")
    E.frase(c, t, pal("s03", "se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1000, "left", 0.12)


# ---------------- preço por litro ----------------
def b_litro(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5 = C["s05.a"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    E.saida(c, t, a4 - 0.2, lambda: E.frase(c, t, C["s04"] + 0.3, ps("tamanhos diferentes:", "i", 70) + [("não compare a etiqueta", "g", 72, ERRADO)], W / 2, 150, "center", 0.1))
    E.saida(c, t, a7 - 0.2, lambda: E.frase(c, t, a4, ps("compare o", "i", 84) + [("preço por litro", "g", 90, COR)], W / 2, 150, "center", 0.12))
    if t >= a7 - 0.2:
        E.frase(c, t, a7, [("R$ 3,50", "g", 84, CERTO)] + ps("contra", "i", 76) + [("R$ 3,60", "g", 84, ERRADO)], W / 2, 150, "center", 0.12)
    y0 = 560  # base das garrafas, menores aqui
    E.foco(c, t, C["s04"] + 0.4, 0.5, lambda a: (garrafa(c, GA, y0, 300, "1,5 L", a=a), etiqueta(c, GA, y0 + 100, "R$ 5,40", a, size=54)))
    E.foco(c, t, C["s04"] + 0.6, 0.5, lambda a: (garrafa(c, GB, y0, 340, "2 L", a=a), etiqueta(c, GB, y0 + 100, "R$ 7,00", a, size=54)))
    E.foco(c, t, b4, 0.4, lambda a: centro(c, "quanto custa 1 litro?", W / 2, 400, 54, "i", TINTA2, a * (1 - ep(t, a5, 0.4))))

    def contas():
        fcen(c, t, a5, "7 ÷ 2 = 3,50", GB, 800, 84)
        fcen(c, t, a6, "5,4 ÷ 1,5", GA, 800, 84)
        E.foco(c, t, pal("s06", "tire"), 0.4, lambda a: E.pilula(c, "× 10 nos dois", GA, 880, 44, "g", a=a, cor=E.SOBRE))
        fcen(c, t, b6, "54 ÷ 15 = 3,60", GA, 990, 84)
    E.saida(c, t, a7 - 0.2, contas)
    if t >= a7 - 0.2:
        E.foco(c, t, a7, 0.4, lambda a: (etiqueta(c, GA, 820, "R$ 3,60 por litro", a, ERRADO, 54), etiqueta(c, GB, 820, "R$ 3,50 por litro", a, CERTO, 54)))
        q = ep(t, b7, 0.4)
        E.caixa_pontilhada(c, GB - 330, 170 + 60, 660, 680, q, CERTO, prog_=q)

        def frases():
            E.saida(c, t, pal("s07", "a", 2) - 0.2, lambda: E.frase(c, t, b7, ps("cada litro sai", "i", 66) + [("10 centavos mais barato", "g", 68, CERTO)], W / 2, 980, "center", 0.1))
            E.saida(c, t, d7 - 0.2, lambda: E.frase(c, t, pal("s07", "a", 2), ps("etiqueta: o preço da garrafa ·", "i", 62) + ps("por litro:", "i", 62) + [("o preço do suco", "g", 64, COR)],
                                                    W / 2, 980, "center", 0.08))
            E.frase(c, t, d7, ps("só compensa se você", "i", 66) + [("usar todo o suco", "g", 68, COR)], W / 2, 980, "center", 0.1)
        frases()


# ---------------- latas: a quantidade certa ----------------
PX4, PX6 = 620, 1300
TBX, TBY = 170, 300
TBL = (230, 230, 230, 300)


def b_latas(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a0 = C["s10.a"]
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")

    def pacotes():
        E.frase(c, t, C["s08"] + 0.3, ps("você precisa de", "i", 76) + [("16 latas", "g", 84, COR)], W / 2, 160, "center", 0.12)
        E.foco(c, t, b8, 0.5, lambda a: (pacote(c, PX4, 560, 4, 1.2, a=a), etiqueta(c, PX4, 680, "R$ 10,00", a)))
        E.foco(c, t, c8, 0.5, lambda a: (pacote(c, PX6, 560, 6, 1.2, a=a), etiqueta(c, PX6, 680, "R$ 13,80", a)))
        E.frase(c, t, pal("s08", "qual"), ps("qual é a", "i", 70) + [("compra mais barata?", "g", 72, COR)], W / 2, 1010, "center", 0.1)
        fcen(c, t, a9, "10 ÷ 4 = 2,50", PX4, 830, 76)
        fcen(c, t, b9, "13,80 ÷ 6 = 2,30", PX6, 830, 76)
        E.frase(c, t, a9 + 0.6, ps("por lata", "i", 54, TINTA2), PX4, 910, "center")
        E.frase(c, t, b9 + 0.6, ps("por lata", "i", 54, TINTA2), PX6, 910, "center")
        if t >= c9:
            q = ep(t, c9, 0.4)
            E.caixa_pontilhada(c, PX6 - 300, 260, 600, 680, q, CERTO, prog_=q)
    E.saida(c, t, C["s10"] - 0.1, pacotes)
    if t < C["s10"] - 0.1:
        return
    E.frase(c, t, C["s10"] + 0.3, [("16 latas", "g", 72, COR)] + ps("não fecham só com pacotes de 6", "i", 66), XE, 170, "left", 0.1)
    linhas = [(a1, ["0", "16", "4", "R$ 40,00"]), (c1, ["1", "10", ("?", ERRADO), ("—", ERRADO)]),
              (a2, ["2", "4", ("1", CERTO) if t >= b2 else ("", TINTA), ("R$ 37,60", CERTO) if t >= pal("s12", "mais") else ("", TINTA)])]
    xs, ys = tabela(c, t, TBX, TBY, TBL, ("de 6", "faltam", "de 4", "total"), linhas, a0, h=110, size=68, verde=(2, d2))
    if t >= pal("s11", "linha"):
        risca_linha(c, t, pal("s11", "linha"), TBX + 20, TBX + sum(TBL) - 20, ys[1])
    xr = 1550
    E.frase(c, t, d1, ps("10 latas não fecham", "i", 54, ERRADO), xr, ys[1] + 18, "center", 0.08)
    E.frase(c, t, pal("s11", "linha"), ps("linha descartada", "g", 46, ERRADO), xr, ys[1] + 80, "center", 0.08)
    E.saida(c, t, pal("s12", "três") - 0.2, lambda: (fcen(c, t, c2, "2 × 13,80 = 27,60", xr, ys[2] - 10, 56),
                                                     fcen(c, t, pal("s12", "mais"), "+ 10 = 37,60", xr, ys[2] + 70, 56, CERTO)))
    E.frase(c, t, pal("s12", "três"), [("3 de 6 = 18", "g", 60, ERRADO)] + ps("passa de 16", "i", 56, ERRADO), TBX, ys[2] + 160, "left", 0.1)
    E.frase(c, t, d2, ps("melhor compra:", "i", 66) + [("2 de 6 + 1 de 4", "g", 70, CERTO)], TBX, ys[2] + 270, "left", 0.1)


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, C["s13"] + 0.3, ps("o erro:", "i", 80) + [("parar no preço por lata", "g", 84, ERRADO)], W / 2, 180, "center", 0.12)
    for k in range(3):
        E.foco(c, t, pal("s13", "três") + 0.15 * k, 0.5, lambda a, k=k: pacote(c, 600 + k * 360, 660, 6, 1.0, a=a))
    E.frase(c, t, a3, ps("só pacotes de 6:", "i", 70) + [("3 pacotes", "g", 74)], W / 2, 300, "center", 0.12)
    fcen(c, t, b3, "3 × 13,80 = 41,40", W / 2, 810, 100, ERRADO)
    if t >= c3:
        q = ep(t, c3, 0.4)
        x0, y0 = 1320 - 129, 660 - 276  # o 3º pacote; as 2 latas que sobram são as duas últimas
        E.caixa_pontilhada(c, x0 + 12 + 82 - 8, y0 + 12 + 132 - 8, 2 * 70 + 12 + 16, 120 + 16, q, ERRADO, prog_=q)
    E.frase(c, t, c3, [("18 latas:", "g", 64, ERRADO)] + ps("2 sobrando", "i", 64, ERRADO), W / 2, 910, "center", 0.1)
    E.frase(c, t, pal("s13", "gastou"), ps("gastou mais que", "i", 64) + [("R$ 37,60", "g", 66, CERTO)] + ps("e levou o que não precisava", "i", 64), W / 2, 1000, "center", 0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    a5, b5 = C["s15.a"], C["s15.b"]

    def um():
        E.frase(c, t, C["s14"] + 0.3, ps("agora, o atalho", "i", 70, CLARO), W / 2, 150, "center", 0.1)
        E.frase(c, t, a4, ps("comece pelo", "i", 80, CLARO) + [("máximo", "g", 84, BR)] + ps("da embalagem", "i", 80, CLARO), W / 2, 290, "center", 0.12)
        E.frase(c, t, pal("s14", "mais"), [("mais barata por unidade", "g", 84, BR)], W / 2, 400, "center", 0.12)
        E.foco(c, t, b4, 0.5, lambda a: E.selo(c, 500, 560, 46, True, a))
        E.frase(c, t, pal("s14", "se"), ps("fechou?", "i", 72, CLARO) + [("é a resposta", "g", 76, BR)], 580, 585, "left", 0.1)
        E.foco(c, t, c4, 0.5, lambda a: E.selo(c, 500, 720, 46, False, a))
        E.frase(c, t, pal("s14", "se", 2), ps("não fechou?", "i", 72, CLARO) + [("tire um pacote", "g", 76, BR)] + ps("e teste de novo", "i", 72, CLARO), 580, 745, "left", 0.1)
        E.frase(c, t, c4 + 0.8, [("3 de 6 = 18", "g", 60, ERRADO)] + ps("→", "g", 60, CLARO) + [("2 de 6 + 1 de 4 = 16", "g", 60, CERTO)], W / 2, 920, "center", 0.12)
    E.saida(c, t, C["s15"] - 0.1, um)
    if t < C["s15"]:
        return
    E.frase(c, t, a5 - 1.0, ps("cada lata no pacote de 6", "i", 76, CLARO) + [("custa menos", "g", 80, BR)], W / 2, 240, "center", 0.12)
    E.frase(c, t, pal("s15", "quanto"), ps("mais latas nele,", "i", 76, CLARO) + [("menor a conta", "g", 80, BR)], W / 2, 370, "center", 0.12)
    tn = pal("s15", "não")
    E.foco(c, t, tn, 0.5, lambda a: E.selo(c, 330, 590, 56, False, a))
    E.frase(c, t, tn, ps("não compensa: aceita", "i", 76, CLARO) + [("sobra", "g", 80, BR)], 430, 615, "left", 0.1)
    E.frase(c, t, pal("s15", "ou"), ps("ou tem", "i", 76, CLARO) + [("promoção", "g", 80, BR)], 430, 715, "left", 0.1)
    E.frase(c, t, b5 - 0.3, ps("aí,", "i", 90, CLARO) + [("faça a tabela inteira", "g", 96, BR)], W / 2, 860, "center", 0.12)


# ---------------- questão ----------------
def linhas_q(C):
    return [(C["s16.a"] - 1.2, "Você precisa de exatamente [22 garrafas|g] de água."), (C["s16.b"], "O pacote de 4 custa [R$ 6,00|p]."),
            (C["s16.c"], "O de 6 custa [R$ 8,40|q]."), (C["s16.d"], "Qual é a compra mais barata,", True), (C["s16.d"] + 1.2, "e quanto custa?", True)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 64, COR), XE, 150, passo=0.12)
    enunciado(c, t, XE, 210, 1240, linhas_q(C), size=60)
    E.relogio(c, t, C["s17.a"], 1640, 460, 150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    fcen(c, t, a8, "6 ÷ 4 = 1,50", 560, 200, 72)
    fcen(c, t, b8, "8,40 ÷ 6 = 1,40", 1300, 200, 72, CERTO)
    E.frase(c, t, a8 + 0.6, ps("por garrafa, no pacote de 4", "i", 50, TINTA2), 560, 260, "center", 0.06)
    E.frase(c, t, b8 + 0.6, ps("por garrafa, no pacote de 6:", "i", 50, TINTA2) + [("ganha", "g", 52, CERTO)], 1300, 260, "center", 0.06)
    linhas = [(c8, ["3", ("4", TINTA) if t >= a9 - 0.3 else ("", TINTA), ("1", TINTA) if t >= pal("s19", "um") else ("", TINTA),
                    ("R$ 31,20", CERTO) if t >= c9 else ("", TINTA)]),
              (d9, ["1", "16", "4", ("R$ 32,40", ERRADO)])]
    xs, ys = tabela(c, t, TBX, 360, TBL, ("de 6", "faltam", "de 4", "total"), linhas, C["s18"] + 0.4, h=110, size=68,
                    verde=(0, pal("s19", "fechou")))
    xr = 1550
    E.frase(c, t, c8 + 0.4, ps("máximo de 6:", "i", 52, TINTA2) + [("18 garrafas", "g", 54)], xr, ys[0] - 40, "center", 0.08)
    E.saida(c, t, d9 - 0.2, lambda: (fcen(c, t, b9, "3 × 8,40 = 25,20", xr, ys[0] + 40, 54), fcen(c, t, c9, "+ 6 = 31,20", xr, ys[0] + 110, 54, CERTO)))
    E.frase(c, t, pal("s19", "confira"), ps("confira outra linha:", "i", 52, TINTA2), xr, ys[1] - 30, "center", 0.08)
    E.frase(c, t, pal("s19", "mais", 2), [("mais caro", "g", 60, ERRADO)], xr, ys[1] + 50, "center")
    E.foco(c, t, c9 + 0.4, 0.5, lambda a: E.pilula(c, "3 de 6 + 1 de 4 = R$ 31,20", W / 2, 920, 64, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.1, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", "compare", "o preço por unidade"), ("s20.b", "monte as opções", "que fecham a quantidade"), ("s20.c", "escolha", "o menor total"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 76, COR)] + ps(l2, "i", 74), 320, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, pal("s21", "pratica"), [("praticar", "g", 100, COR)] + ps("tudo da trilha", "i", 92), XE, 390, passo=0.12)
    x = XE
    for s, k in (("ler enunciados longos", a1), ("estimar o resultado", b1), ("escolher a melhor opção", c1)):
        w = E.larg(s, "b", 50) + 50 * 1.1
        E.foco(c, t, k, 0.4, lambda a, s=s, x=x, w=w: E.pilula(c, s, x + w / 2, 540, 50, "b", a=a, cor=E.SOBRE))
        x += w + 26
    E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d1 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, d1 + 0.2, 0.4))
    E.frase(c, t, e1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, litro=b_litro, latas=b_latas, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
