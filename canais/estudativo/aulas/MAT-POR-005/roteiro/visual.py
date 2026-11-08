"""Visual — Estudativo · MAT-POR-005: variação percentual.
Linguagem da trilha Porcentagem (cartao, maquina, fluxo: as mesmas peças de MAT-POR-006): valor de antes = cartão escuro, valor de
depois = cartão na cor da matéria; a máquina guarda a mudança ("+ 25%", "− 20%"), que chega como "?" e troca quando é dita.
Esta aula não usa fator (MAT-POR-004 fica fora da cadeia dela). marca_antes() é a caixa pontilhada do valor de antes, o 100%.
A voz é real: os marcadores vêm de C[...] e, onde a tela precisa da palavra exata, fala(cena, palavra) lê o tempos.json."""
import json
import math
from pathlib import Path
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, passo
import motor as M
import skia

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-005_variacao_percentual.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("base", "queda", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 100 - 80 == 20 and 20 / 80 == 0.25 and 20 / 100 == 0.2 and 75 - 50 == 25 and 25 / 50 == 0.5
assert 100 / 80 == 1.25 and 80 / 100 == 0.8 and 180 - 160 == 20 and 20 / 160 == 0.125
assert 1380 - 1200 == 180 and 180 / 1200 == 0.15 and 1200 * 0.1 == 120 and 120 / 2 == 60 and 120 + 60 == 180
assert 60 - 45 == 15 and 15 / 60 == 0.25 and 60 / 4 == 15


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- tempo da palavra dita ----------------
_TEMPOS = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))
_CENAS = {s["id"]: s for s in _TEMPOS["scenes"]}


def fala(sid, palavra, k=1):
    """instante em que a k-ésima `palavra` da cena começa a ser dita"""
    s = _CENAS[sid]
    n = 0
    for tk in s["tokens"]:
        if tk["disp"].lower().strip(".,:;?!") == palavra:
            n += 1
            if n == k:
                return s["start"] + tk["t0"]
    raise KeyError((sid, palavra, k))


# ---------------- peças gerais ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def cen(c, t, ti, s, x, y, size=64, cor=None, est="g"):
    E.foco(c, t, ti, 0.45, lambda a: centro(c, s, x, y, size, est, cor or TINTA, a))


def txt(c, t, ti, s, x, y, size=64, cor=None, est="g"):
    E.foco(c, t, ti, 0.45, lambda a: E.escreve(c, s, x, y, size, est, cor or TINTA, a))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE if cor is None else M.on(cor), a)


def zero_some(c, t, x, y, size, t1, cor=None):
    """o 0 à esquerda de 0,8: some quando a vírgula sai dele. x = borda esquerda do primeiro algarismo depois da vírgula"""
    E.saida(c, t, t1, lambda: centro(c, "0", x - E.casa(size) * 0.5, y, size, "g", cor or TINTA))


def grupo(c, cx, cy, k, fn):
    """desenha fn() escalado por k em torno de (cx, cy)"""
    c.save(); c.translate(cx, cy); c.scale(k, k); c.translate(-cx, -cy)
    fn()
    c.restore()


def vez(itens, t):
    """itens = texto fixo ou [(t0, texto), ...]; devolve [(t0, t_fim, texto)]"""
    if isinstance(itens, str):
        return [(None, 1e9, itens)]
    return [(t0, itens[i + 1][0] if i + 1 < len(itens) else 1e9, s) for i, (t0, s) in enumerate(itens)]


# ---------------- linguagem da trilha Porcentagem ----------------
def larg_cartao(valores, size):
    return max(max(E.larg(s, "g", size) for s in valores) + size * 1.0, size * 2.9)


def cartao(c, t, t0, cx, cy, valor, rotulo=None, depois=False, size=92, w=None, cor=None):
    """valor num cartão: entra em t0. valor = texto ou [(t0, texto), ...] ("?" sai cinza). depois=True: cor da matéria"""
    itens = vez(valor, t)
    w = w or larg_cartao([s for _, _, s in itens], size)
    h = size * 1.75
    tinta = cor or (COR if depois else TINTA)

    def caixa(a):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 30, 30)
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
        c.save(); c.translate(6, 12); c.drawRRect(r, s); c.restore()
        c.drawRRect(r, M.paint(BR, a))
        c.drawRRect(r, M.paint(tinta, a, stroke=6))
        if rotulo:
            centro(c, rotulo, cx, cy - h / 2 - 28, 58, "i", (cor or COR) if depois else TINTA2, a)
    E.foco(c, t, t0, 0.5, caixa)
    for ti, tf, s in itens:
        ti = t0 if ti is None else ti
        cor_s = CINZA if s == "?" else tinta
        E.saida(c, t, tf - 0.05, lambda s=s, ti=ti, cor_s=cor_s: E.foco(c, t, ti, 0.45, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", cor_s, a)), d=0.25)
    return w


def maquina(c, t, t0, cx, cy, fator, size=84):
    """a máquina: o fator numa caixa cheia da cor da matéria. fator = texto ou [(t0, texto), ...]"""
    itens = vez(fator, t)
    w = max(max(E.larg(s, "g", size) for _, _, s in itens) + size * 1.2, size * 2.8)
    h = size * 1.9

    def caixa(a):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 22, 22)
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.22 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 16))
        c.save(); c.translate(8, 14); c.drawRRect(r, s); c.restore()
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeLinear([skia.Point(cx, cy - h / 2), skia.Point(cx, cy + h / 2)],
                                                   [M.hexc(E.mix(E.COR, BR, 0.18), a), M.hexc(E.mix(E.COR, "#000000", 0.25), a)]))
        c.drawRRect(r, p)
        for dx in (-1, 1):  # parafusos: é uma máquina
            c.drawCircle(cx + dx * (w / 2 - 22), cy - h / 2 + 22, 7, M.paint(E.mix(E.COR, BR, 0.45), a))
            c.drawCircle(cx + dx * (w / 2 - 22), cy + h / 2 - 22, 7, M.paint(E.mix(E.COR, BR, 0.45), a))
    E.foco(c, t, t0, 0.5, caixa)
    for ti, tf, s in itens:
        ti = t0 if ti is None else ti
        E.saida(c, t, tf - 0.05, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)), d=0.25)
    return w


XA, XM, XD = 400, 960, 1520  # antes, máquina, depois


def fluxo(c, t, y, antes, fator, depois, ta, tf, td, rot=("antes", "depois"), size=92, x=(XA, XM, XD), cor_d=None):
    """antes → [fator] → depois. ta, tf, td = instantes de cada parte (None = não desenha)"""
    xa, xm, xd = x
    wa = wd = 0
    if ta is not None:
        wa = cartao(c, t, ta, xa, y, antes, rot[0], False, size)
    if td is not None:
        wd = cartao(c, t, td, xd, y, depois, rot[1], True, size, cor=cor_d)
    if tf is not None:
        wm = maquina(c, t, tf, xm, y, fator, size * 0.9)
        p = ep(t, tf - 0.1, 0.5)
        if p > 0:
            M.arrow(c, xa + max(wa, size * 2.9) / 2 + 22, y, xm - wm / 2 - 22, y, TINTA2, p, 6, 20, p)
            M.arrow(c, xm + wm / 2 + 22, y, xd - max(wd, size * 2.9) / 2 - 22, y, TINTA2, p, 6, 20, p)


def volta(c, t, t0, x0, x1, y, rotulo, alto=170, size=62, escuro=False):
    """seta curva por baixo, de x1 (depois) a x0 (antes), com a conta inversa numa pílula. rotulo = texto ou [(t0, texto)]"""
    p = ease_io(prog(t, t0, 0.8))
    if p <= 0:
        return
    cor = "#FFFFFF" if escuro else TINTA
    mx, my = (x0 + x1) / 2, y + 2 * alto
    pts = []
    n = 60
    for i in range(int(n * p) + 1):
        u = i / n
        pts.append(((1 - u) ** 2 * x1 + 2 * u * (1 - u) * mx + u * u * x0, (1 - u) ** 2 * y + 2 * u * (1 - u) * my + u * u * y))
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        M.line(c, ax, ay, bx, by, cor, 1.0, 6)
    if len(pts) >= 2 and p > 0.15:
        (ax, ay), (bx, by) = pts[-2], pts[-1]
        M.arrow(c, ax, ay, bx, by, cor, 1.0, 6, 22)
    for ti, tf, s in vez(rotulo, t):
        ti = t0 + 0.4 if ti is None else ti
        E.saida(c, t, tf - 0.05, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: E.pilula(c, s, mx, y + alto, size, "g", fundo=cor,
                                                                                                  cor=TINTA if escuro else BR, a=a)), d=0.25)




# ---------------- peças desta aula ----------------
def bolinha(c, t, t0, n, x, y, r=40):
    E.foco(c, t, t0, 0.45, lambda a: (E.bola(c, x, y, r, a=a), centro(c, str(n), x, y + r * 0.42, r * 1.15, "g", E.SOBRE, a)))


def marca_antes(c, t, t0, x, y, size=92, rot="valor de antes"):
    """caixa pontilhada em volta do cartão de antes, com o rótulo embaixo"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    w, h = size * 2.9 + 40, size * 1.75 + 40
    E.caixa_pontilhada(c, x - w / 2, y - h / 2, w, h, q, COR, prog_=q)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rot, x, y + h / 2 + 64, 54, "g", COR, a))


def dif(c, t, t0, x0, x1, y, s, cor=None):
    """a diferença numa pílula por baixo das setas do fluxo"""
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, s, (x0 + x1) / 2, y, 50, "g", fundo=cor or TINTA, a=a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        fluxo(c, t, 380, "R$ 80", [(ka, "?"), (kc, "+ 25%")], "R$ 100", ka, ka + 0.3, fala("s01", "cem"), rot=("antes", "depois"))
        dif(c, t, fala("s01", "subiu"), XA, XD, 560, "subiu R$ 20")
        E.frase(c, t, fala("s01", "muita"), ps("muita gente diz", "i", 70), 560, 760, "center", 0.12)
        E.foco(c, t, kb, 0.5, lambda a: centro(c, "20%", 560, 930, 150, "g", ERRADO, a))
        if t >= fala("s01", "errado"):
            E.risco(c, 420, 950, 700, 830, t, fala("s01", "errado"), largura=14)
        E.foco(c, t, kc, 0.5, lambda a: num_bola(c, "25%", 1360, 860, 130, 96, a, CERTO))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta + 0.2, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, fala("s02", "quantos"), [("quantos por cento", "g", 100, COR)], XE, 500)
        E.frase(c, t, fala("s02", "subiu"), ps("algo", "i", 90) + [("subiu", "g", 100)], XE, 650, passo=0.12)
        E.frase(c, t, fala("s02", "caiu"), ps("ou", "i", 90) + [("caiu", "g", 100)], XE, 800, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 200, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, 330, w, 300, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("Quantos % uma parte", "i", 66)], x + 44, 430)
    E.frase(c, t, C["s03.b"] + 0.3, [("é do total", "g", 66, COR)], x + 44, 520)
    E.frase(c, t, fala("s03", "dividindo"), [("parte ÷ total", "g", 56, TINTA2)], x + 44, 595)
    E.cursor(c, x + w - 30, 600, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, fala("s03", "se"), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 760, "left", 0.12)


# ---------------- de quê ----------------
def b_base(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    a5, b5, c5, d5, e5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]

    def quatro():
        E.frase(c, t, a4, [("variação percentual", "g", 96, COR)], W / 2, 180, "center")
        E.frase(c, t, fala("s04", "quanto"), ps("quanto um valor mudou,", "i", 70) + [("em %", "g", 70)], W / 2, 290, "center", 0.12)
        y = 560
        fluxo(c, t, y, "R$ 80", "", "R$ 100", fala("s04", "a"), None, fala("s04", "a") + 0.3, rot=("antes", "depois"))
        p = ep(t, fala("s04", "a") + 0.3, 0.5)
        if p > 0:
            M.arrow(c, XA + 195, y, XD - 215, y, TINTA2, p, 6, 20, p)
        dif(c, t, fala("s04", "vinte"), XA, XD, y, "+ R$ 20")
        E.frase(c, t, fala("s04", "vinte"), [("20", "g", 80)] + ps("são quantos % de", "i", 76), 1060, 980, "right", 0.12)
        E.frase(c, t, b4, [("quê?", "g", 90, COR)], 1090, 980)
        marca_antes(c, t, c4, XA, y)
        E.foco(c, t, d4, 0.5, lambda a: centro(c, "= 100%", XA, y + 270, 76, "g", COR, a))
    E.saida(c, t, C["s05"] - 0.1, quatro)
    if t < C["s05"]:
        return
    E.frase(c, t, a5, [("parte", "g", 90)] + [("÷", "g", 90, TINTA2)] + [("total", "g", 90)], W / 2, 200, "center", 0.2)
    y, s = 520, 150
    E.frac_q(c, t, a5, 20, 80, b5, c5, 520, y, s)
    E.foco(c, t, b5, 0.45, lambda a: E.escreve(c, "o aumento", 660, y - 60, 60, "i", TINTA2, a))
    E.foco(c, t, c5, 0.45, lambda a: E.escreve(c, "o valor antigo", 660, y + 120, 60, "i", TINTA2, a))
    if t >= d5:
        E.pontes(c, t, 1100, 1300, y, s, "÷ 20", d5 + 0.3, d5 + 0.6, None, 50)
        E.foco(c, t, fala("s05", "quarto"), 0.5, lambda a: E.fracao(c, 1, 4, 1420, y, s, COR, a))
    E.frase(c, t, d5, [("simplifica", "i", 64, TINTA2)], 1200, y - 170, "center")
    E.foco(c, t, e5, 0.5, lambda a: num_bola(c, "25%", 1420, y + 330, 120, 92, a, CERTO))


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    a7, b7, c7, d7, e7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"]

    def seis():
        E.frase(c, t, C["s06"] + 0.2, ps("a regra:", "i", 84) + [("3 passos", "g", 84, COR)], XE, 200, "left", 0.12)
        passo(c, t, b6, 1, "a diferença", "novo − antigo", 400)
        passo(c, t, c6, 2, "divida", "pelo antigo", 620)
        passo(c, t, d6, 3, "ande a vírgula", "2 casas para a direita", 840)
    E.saida(c, t, C["s07"] - 0.1, seis)
    if t < C["s07"]:
        return
    y = 300
    fluxo(c, t, y, "R$ 50", [(a7, "?"), (d7, "+ 50%")], "R$ 75", a7, a7 + 0.3, fala("s07", "setenta"), rot=("antes", "depois"), size=80)
    bolinha(c, t, b7, 1, XE + 40, 560)
    E.linha(c, t, [("75 − 50", "g", 80, TINTA, b7), ("=", "g", 80, TINTA2, fala("s07", "vinte") - 0.1), ("25", "g", 80, COR, fala("s07", "vinte"))], XE + 110, 588)
    bolinha(c, t, c7, 2, XE + 40, 710)
    E.linha(c, t, [("25 ÷ 50", "g", 80, TINTA, c7), ("=", "g", 80, TINTA2, fala("s07", "dá") - 0.1), ("0,5", "g", 80, COR, fala("s07", "zero"))], XE + 110, 738)
    bolinha(c, t, fala("s07", "andando"), 3, XE + 40, 860)
    s, x0, yv = 96, XE + 200, 888
    cl = E.casa(s)
    pulo = d7 - 0.3
    E.foco(c, t, fala("s07", "andando"), 0.45, lambda q: (zero_some(c, t, x0, yv, s, pulo), E.anda(c, t, "5", 0, [(pulo, 2)], x0, yv, s, some=True)))
    E.foco(c, t, d7, 0.45, lambda a: E.escreve(c, "%", x0 + 2 * cl + 8, yv, s, "g", COR, a))
    E.foco(c, t, e7, 0.5, lambda a: E.pilula(c, "subiu metade do que custava", 1340, 740, 56, "g", a=a))


# ---------------- queda ----------------
def b_queda(c, t, C, b):
    a8, b8, c8, d8, e8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"], C["s08.e"]
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]

    def oito():
        E.frase(c, t, C["s08"] + 0.3, ps("na", "i", 80) + [("queda,", "g", 80, COR)] + ps("é igual", "i", 80), W / 2, 150, "center", 0.12)
        y = 380
        fluxo(c, t, y, "R$ 100", [(a8, "?"), (e8, "− 20%")], "R$ 80", fala("s08", "cem"), a8, fala("s08", "oitenta"), rot=("antes", "depois"))
        marca_antes(c, t, c8, XA, y)
        E.linha(c, t, [("100 − 80", "g", 84, TINTA, b8 - 0.3), ("=", "g", 84, TINTA2, b8 - 0.1), ("20", "g", 84, COR, b8)], W / 2, 720, "center")
        E.linha(c, t, [("20 ÷ 100", "g", 84, TINTA, d8), ("=", "g", 84, TINTA2, fala("s08", "dá")), ("0,20", "g", 84, COR, fala("s08", "zero")),
                       ("→", "g", 84, TINTA2, fala("s08", "uma")), ("queda de 20%", "g", 84, COR, e8)], W / 2, 880, "center")
    E.saida(c, t, C["s09"] - 0.1, oito)
    if t < C["s09"]:
        return
    E.frase(c, t, a9, ps("a mesma diferença:", "i", 76) + [("R$ 20", "g", 76, COR)], W / 2, 150, "center", 0.12)
    xs = (380, 960, 1540)
    fluxo(c, t, 380, "R$ 80", "+ 25%", "R$ 100", fala("s09", "subindo"), b9, fala("s09", "subindo") + 0.3, rot=("antes", "depois"), size=76, x=xs)
    fluxo(c, t, 720, "R$ 100", "− 20%", "R$ 80", fala("s09", "descendo"), c9, fala("s09", "descendo") + 0.3, rot=("antes", "depois"), size=76, x=xs)
    for y in (380, 720):
        q = ep(t, d9, 0.5)
        if q > 0:
            w, h = 76 * 2.9 + 40, 76 * 1.75 + 36
            E.caixa_pontilhada(c, xs[0] - w / 2, y - h / 2, w, h, q, COR, prog_=q)
    E.foco(c, t, d9 + 0.2, 0.45, lambda a: E.pilula(c, "o que muda: o valor de antes", W / 2, 960, 60, "g", a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    E.frase(c, t, C["s10"] + 0.3, [("o erro:", "g", 92, ERRADO)] + ps("dividir pelo", "i", 92) + [("valor novo", "g", 92)], W / 2, 170, "center", 0.12)
    y = 400
    fluxo(c, t, y, "R$ 80", "", "R$ 100", fala("s10", "aumento"), None, fala("s10", "aumento") + 0.3, rot=("antes", "depois"), size=80)
    p = ep(t, fala("s10", "aumento") + 0.3, 0.5)
    if p > 0:
        M.arrow(c, XA + 170, y, XD - 185, y, TINTA2, p, 6, 20, p)
    E.linha(c, t, [("20 ÷ 100", "g", 90, ERRADO, b10), ("=", "g", 90, TINTA2, c10 - 0.2), ("20%", "g", 90, ERRADO, c10)], 560, 700, "center")
    if t >= c10 + 0.6:
        E.risco(c, 300, 720, 820, 620, t, c10 + 0.6, largura=12)
    marca_antes(c, t, d10, XA, y, 80, "o preço de antes")
    E.linha(c, t, [("20 ÷ 80", "g", 90, TINTA, fala("s10", "oitenta", 2)), ("=", "g", 90, TINTA2, fala("s10", "oitenta", 2) + 0.3), ("25%", "g", 90, CERTO, fala("s10", "oitenta", 2) + 0.5)],
            1380, 700, "center")
    E.foco(c, t, fala("s10", "oitenta", 2) + 0.8, 0.45, lambda a: E.selo(c, 1380, 850, 50, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    a13, b13 = C["s13.a"], C["s13.b"]

    def onze_doze():
        E.frase(c, t, C["s11"] + 0.3, ps("o atalho:", "i", 84, CLARO) + [("novo ÷ antigo", "g", 84, BR)], W / 2, 180, "center", 0.14)
        E.linha(c, t, [("100 ÷ 80", "g", 90, BR, b11), ("=", "g", 90, CLARO, fala("s11", "dá")), ("1,25", "g", 90, CLARO, fala("s11", "um")),
                       ("=", "g", 90, CLARO, c11 - 0.2), ("125%", "g", 90, BR, c11)], W / 2, 380, "center")
        E.frase(c, t, fala("s11", "o", 3), ps("passou de 100:", "i", 70, CLARO), 900, 500, "right", 0.1)
        E.foco(c, t, d11, 0.5, lambda a: E.pilula(c, "aumento de 25%", 1220, 480, 62, "g", fundo=CLARO, cor="#07070F", a=a))
        E.linha(c, t, [("80 ÷ 100", "g", 90, BR, a12), ("=", "g", 90, CLARO, fala("s12", "dá")), ("0,8", "g", 90, CLARO, fala("s12", "zero")),
                       ("=", "g", 90, CLARO, fala("s12", "oitenta", 2) - 0.2), ("80%", "g", 90, BR, fala("s12", "oitenta", 2))], W / 2, 690, "center")
        E.frase(c, t, b12 - 0.6, ps("faltam 20 para 100:", "i", 70, CLARO), 900, 810, "right", 0.1)
        E.foco(c, t, fala("s12", "queda", 2), 0.5, lambda a: E.pilula(c, "queda de 20%", 1200, 790, 62, "g", fundo=CLARO, cor="#07070F", a=a))
        E.frase(c, t, c12, ps("o antigo vira", "i", 70, CLARO) + [("100%", "g", 70, BR)], W / 2, 970, "center", 0.12)
    E.saida(c, t, d12 - 0.1, onze_doze)

    def bonus():
        E.frase(c, t, d12 - 0.1, [("bônus:", "g", 80, CLARO)], W / 2, 260, "center")
        E.linha(c, t, [("dobrou", "g", 110, BR, d12 + 0.1), ("=", "g", 110, CLARO, fala("s12", "duzentos") - 0.2), ("200%", "g", 110, BR, fala("s12", "duzentos"))],
                W / 2, 520, "center")
        E.foco(c, t, fala("s12", "aumentou"), 0.5, lambda a: E.pilula(c, "aumento de 100%", W / 2, 760, 80, "g", fundo=CLARO, cor="#07070F", a=a))
    if t >= d12 - 0.1:
        E.saida(c, t, C["s13"] - 0.1, bonus)
    if t < C["s13"]:
        return
    E.frase(c, t, a13 - 0.2, ps("não compensa: diferença", "i", 70, CLARO) + [("pequena e fácil", "g", 70, BR)], W / 2, 190, "center", 0.12)
    E.linha(c, t, [("160 → 180", "g", 90, BR, fala("s13", "de")), ("diferença 20", "i", 80, CLARO, fala("s13", "diferença", 2))], W / 2, 380, "center")
    y, s = 620, 120
    E.foco(c, t, b13, 0.5, lambda a: E.fracao(c, 20, 160, 560, y, s, BR, a))
    E.pontes(c, t, 700, 900, y, s, "÷ 20", fala("s13", "simplifica"), fala("s13", "simplifica") + 0.3, CLARO, 46)
    E.foco(c, t, fala("s13", "oitavo"), 0.5, lambda a: E.fracao(c, 1, 8, 1010, y, s, CLARO, a))
    E.foco(c, t, fala("s13", "doze"), 0.5, lambda a: E.escreve(c, "= 12,5%", 1110, y + 40, 110, "g", BR, a))
    E.frase(c, t, fala("s13", "dividir"), [("180 ÷ 160", "g", 76, CLARO)] + ps("dá mais trabalho", "i", 70, CLARO), W / 2, 920, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    E.frase(c, t, C["s14"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 140)
    fluxo(c, t, 330, "R$ 1200", [(a14, "?"), (b14, "+ ?%")], "R$ 1380", a14, a14 + 0.3, fala("s14", "mil", 2), rot=("aluguel antes", "depois"), size=80)
    fluxo(c, t, 610, "R$ 60", [(c14, "?"), (d14, "− ?%")], "R$ 45", fala("s14", "sessenta"), c14 + 0.3, fala("s14", "quarenta"), rot=("produto antes", "depois"), size=80)
    E.saida(c, t, C["s15"] - 0.1, lambda: E.frase(c, t, b14, ps("de", "i", 80) + [("quantos %", "g", 80, COR)] + ps("subiu e caiu?", "i", 80), W / 2, 900, "center", 0.12))
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], W / 2, 830, 95)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a16, b16, c16, d16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    a17, b17, c17, d17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    y = 280

    def aluguel():
        fluxo(c, t, y, "R$ 1200", [(C["s16"], "?"), (c16, "+ 15%")], "R$ 1380", C["s16"], C["s16"], C["s16"], rot=("aluguel antes", "depois"), size=76)
        E.linha(c, t, [("1380 − 1200", "g", 76, TINTA, a16 - 0.3), ("=", "g", 76, TINTA2, a16 - 0.1), ("180", "g", 76, COR, a16)], XE, 520)
        E.linha(c, t, [("180 ÷ 1200", "g", 76, TINTA, b16), ("=", "g", 76, TINTA2, fala("s16", "dá")), ("0,15", "g", 76, COR, fala("s16", "zero")),
                       ("=", "g", 76, TINTA2, c16 - 0.2), ("15%", "g", 76, COR, c16)], XE, 640)
        E.frase(c, t, d16 - 0.6, ps("confira:", "i", 64, COR), XE, 790)
        E.frase(c, t, d16, [("10% = 120", "g", 64)], XE, 880)
        E.frase(c, t, fala("s16", "cinco"), [("5% = 60", "g", 64)], XE + 420, 880)
        E.frase(c, t, fala("s16", "juntos"), [("120 + 60 = 180", "g", 64, CERTO)], XE + 760, 880)
        E.foco(c, t, fala("s16", "bateu"), 0.45, lambda a: E.selo(c, 1560, 860, 50, True, a))
    E.saida(c, t, C["s17"] - 0.1, aluguel)
    if t < C["s17"]:
        return
    fluxo(c, t, y, "R$ 60", [(C["s17"], "?"), (c17, "− 25%")], "R$ 45", C["s17"], C["s17"], C["s17"], rot=("produto antes", "depois"), size=76)
    E.linha(c, t, [("60 − 45", "g", 76, TINTA, a17 - 0.3), ("=", "g", 76, TINTA2, a17 - 0.1), ("15", "g", 76, COR, a17)], XE, 520)
    s, yy = 100, 700
    E.foco(c, t, b17, 0.5, lambda a: E.fracao(c, 15, 60, XE + 80, yy, s, TINTA, a))
    sinal(c, t, fala("s17", "um") - 0.2, "=", XE + 220, yy - 12, 80)
    E.foco(c, t, fala("s17", "um"), 0.5, lambda a: E.fracao(c, 1, 4, XE + 330, yy, s, COR, a))
    sinal(c, t, c17 - 0.2, "=", XE + 440, yy - 12, 80)
    E.foco(c, t, c17, 0.5, lambda a: E.escreve(c, "25%", XE + 500, yy + 30, 90, "g", COR, a))
    E.frase(c, t, fala("s17", "confira"), ps("confira:", "i", 64, COR) + [("1/4 de 60 = 15", "g", 64, CERTO)], XE, 930, "left", 0.12)
    E.frase(c, t, fala("s17", "dividir"), ps("pelo novo:", "i", 64, TINTA2) + [("15/45", "g", 64, ERRADO)], 1180, 650, "left", 0.12)
    E.foco(c, t, d17, 0.45, lambda a: E.escreve(c, "= 1/3", 1180, 760, 76, "g", ERRADO, a))
    if t >= d17 + 1.0:
        E.risco(c, 1170, 785, 1390, 690, t, d17 + 1.0, largura=12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s18.a", "diferença ÷ valor de antes"), ("s18.b", "o antigo é sempre 100%"))):
            y = 430 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 330 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", "#FFFFFF", a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 90)], 430, y)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    a19, b19, c19, d19, e19 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"], C["s19.e"]
    E.frase(c, t, C["s19"] + 0.2, ps("a mesma conta", "i", 76) + [("mede erros", "g", 76, COR)], XE, 200, "left", 0.12)
    E.frase(c, t, fala("s19", "próxima"), [("próxima", "i", 84), ("aula", "i", 84)], XE, 350)
    E.frase(c, t, fala("s19", "qual"), [("Qual erro pesa mais?", "g", 112, COR)], XE, 500)
    E.frase(c, t, b19, [("1 cm", "g", 84)] + ps("em", "i", 84) + [("2 m", "g", 84)], XE, 680, "left", 0.15)
    E.frase(c, t, c19, ps("ou", "i", 84) + [("1 mm", "g", 84)] + ps("em", "i", 84) + [("1 cm?", "g", 84)], XE, 800, "left", 0.15)
    E.foco(c, t, d19, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=a))
    p = ease_io(prog(t, d19 + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, d19 + 0.2, 0.4))
    E.frase(c, t, e19, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 980, "center")


def sinal(c, t, t0, s, cx, cy, size, cor=None):
    E.sinal(c, t, t0, s, cx, cy, size, cor or TINTA2)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, base=b_base, regra=b_regra, queda=b_queda, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
