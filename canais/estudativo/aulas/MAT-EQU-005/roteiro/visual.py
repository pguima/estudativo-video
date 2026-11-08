"""Visual — Estudativo · MAT-EQU-005: multiplicar termos com letra e duas expressões.
Termo vezes termo separa números e letras; a soma e a multiplicação lado a lado; o piso retangular de lados x + 2 e
x + 3 é cortado nas emendas em quatro pedaços (x², 3x, 2x e 6); o chuveirinho refaz os mesmos pedaços com setas, e o
erro apaga as faixas do meio. No palco, o atalho de (x + a)(x + b).
Instantes: os cues de C[...] e, para cada palavra, pal(cena, palavra), lido da voz gravada em audio/tempos.json."""
import json
import math
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-005_multiplicar_termos_com_letra.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("termos", "piso", "atalho", "questao", "fim"))
BR = "#FFFFFF"

x = 10
assert 3 * x * 2 * x == 6 * x ** 2 == 600 and 30 * 20 == 600 and 2 * x ** 2 * 4 * x == 8 * x ** 3
assert x + x ** 2 == 110 and 2 * x ** 3 == 2000
assert (x + 2) * (x + 3) == x ** 2 + 5 * x + 6 == 156 == 12 * 13 and x ** 2 + 6 == 106
assert (x + 4) * (x - 1) == x ** 2 + 3 * x - 4 and 4 - 1 == 3 and 4 * -1 == -4
del x
_T = {s["id"]: s for s in json.load(open(Path(__file__).resolve().parents[1] / "audio" / "tempos.json", encoding="utf8"))["scenes"]}


def pal(sid, palavra, n=0):
    """instante em que a voz diz a palavra (n = qual ocorrência na cena)"""
    s = _T[sid]
    achou = [tk["t0"] for tk in s["tokens"] if tk["disp"].lower().strip(",.:;?!") == palavra]
    return s["start"] + achou[n]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def form(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def fw(s, size):
    return E.formula(None, s, 0, 0, size, a=0) if s else 0.0


def trecho_x(s, trecho, x, size, align="left", n=0):
    """(x inicial, largura) de um trecho da fórmula s"""
    xi = x - fw(s, size) / 2 if align == "center" else x
    i0 = -1
    for _ in range(n + 1):
        i0 = s.find(trecho, i0 + 1)
    return xi + fw(s[:i0], size), fw(trecho, size) - size * 0.02


def realce(c, t, t0, s, trecho, x, y, size, cor=None, align="left", n=0, t1=None):
    a = ep(t, t0, 0.35) * (1 - ep(t, t1, 0.3) if t1 else 1)
    if a <= 0:
        return
    x0, w = trecho_x(s, trecho, x, size, align, n)
    pad = min(size * 0.14, 16)
    M.rrect(c, x0 - pad, y - size * 0.95, w + pad * 2, size * 1.25, size * 0.2, cor or COR, 0.16 * a)


def monta(c, t, pecas, x, y, size, align="left", cor=None):
    total = fw("".join(p[0] for p in pecas), size)
    x0 = x - total / 2 if align == "center" else x
    acc = ""
    for p in pecas:
        s, t0, cp = p[0], p[1], (p[2] if len(p) > 2 else cor)
        xo = x0 + fw(acc, size)
        E.foco(c, t, t0, 0.4, lambda a, s=s, xo=xo, cp=cp: E.formula(c, s, xo, y, size, cor=cp, a=a))
        acc += s
    return x0


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def bola_em(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda p: num_bola(c, s, cx, cy, r * ease_back(prog(t, t0, 0.6)), size, p, cor, BR))




def flecha(c, t, t0, x0, y0, x1, y1, alto, cor, d=0.6, largura=6):
    """arco de (x0, y0) a (x1, y1) com ponta de seta; alto > 0 sobe, alto < 0 desce"""
    p = ep(t, t0, d)
    if p <= 0:
        return
    cx = (x0 + x1) / 2
    cy = (min(y0, y1) - alto) if alto > 0 else (max(y0, y1) - alto)
    pt = lambda u: ((1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u * u * x1, (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u * u * y1)
    n = max(2, int(30 * p))
    path = skia.Path()
    path.moveTo(*pt(0))
    for i in range(1, n + 1):
        path.lineTo(*pt(p * i / n))
    c.drawPath(path, M.paint(cor, 1.0, stroke=largura, cap_round=True))
    if p > 0.97:
        ang = math.atan2(y1 - cy, x1 - cx)
        for da in (2.6, -2.6):
            M.line(c, x1, y1, x1 + 24 * math.cos(ang + da), y1 + 24 * math.sin(ang + da), cor, 1.0, largura)


def piso(c, x0, y0, X, u, a=1.0, cortes=0.0, separa=0.0, rot=(0, 0, 0, 0), apaga=0.0, escuro=False):
    """piso de lados (x + 2) na vertical e (x + 3) na horizontal; X = medida do x, u = uma unidade.
    cortes desenha as emendas, separa afasta e pinta os 4 pedaços, rot = alfa dos rótulos (x², 3x, 2x, 6), apaga some as faixas do meio"""
    if a <= 0:
        return
    g = 16 * separa
    claro = M.mix(E.COR, BR, 0.82) if not escuro else M.mix(E.COR, "#07070F", 0.4)
    cores = (E.COR, M.mix(E.COR, BR, 0.45), M.mix(E.COR, BR, 0.45), M.mix(E.COR, BR, 0.7))
    pedacos = ((0, 0, X, X), (X + g, 0, 3 * u, X), (0, X + g, X, 2 * u), (X + g, X + g, 3 * u, 2 * u))
    nomes = ("x^2", "3x", "2x", "6")
    for i, (dx, dy, w, h) in enumerate(pedacos):
        meio = i in (1, 2)
        q = a * (1 - 0.8 * apaga if meio else 1)
        M.rrect(c, x0 + dx, y0 + dy, w, h, 8, M.mix(claro, cores[i], separa), q)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + dx, y0 + dy, w, h), 8, 8), M.paint(E.COR, q, stroke=3))
        if rot[i] > 0:
            tinta = BR if i == 0 else TINTA
            E.formula(c, nomes[i], x0 + dx + w / 2, y0 + dy + h / 2 + 26, 72 if i else 96, cor=tinta, a=rot[i] * q, align="center")
        if meio and apaga > 0:
            M.line(c, x0 + dx + 20, y0 + dy + 20, x0 + dx + w - 20, y0 + dy + h - 20, ERRADO, apaga * a, 7)
            M.line(c, x0 + dx + w - 20, y0 + dy + 20, x0 + dx + 20, y0 + dy + h - 20, ERRADO, apaga * a, 7)
    if 0 < cortes and separa < 0.3:
        for k in range(16):  # emendas tracejadas
            f0, f1 = k / 16, (k + 0.5) / 16
            if f0 < cortes:
                f1 = min(f1, cortes)
                M.line(c, x0 + X, y0 + (X + 2 * u) * f0, x0 + X, y0 + (X + 2 * u) * f1, ERRADO, a, 5)
                M.line(c, x0 + (X + 3 * u) * f0, y0 + X, x0 + (X + 3 * u) * f1, y0 + X, ERRADO, a, 5)


def lados(c, t, ta, tb, x0, y0, X, u, cor=None, size=64):
    """rótulos dos lados do piso: x + 2 à esquerda (ta), x + 3 em cima (tb)"""
    cor = cor or COR
    E.foco(c, t, ta, 0.45, lambda p: (centro(c, "x", x0 - 50, y0 + X / 2 + 22, size, "g", cor, p),
                                     centro(c, "2", x0 - 50, y0 + X + u + 22, size, "g", cor, p)))
    E.foco(c, t, tb, 0.45, lambda p: (centro(c, "x", x0 + X / 2, y0 - 30, size, "g", cor, p),
                                     centro(c, "3", x0 + X + 1.5 * u, y0 - 30, size, "g", cor, p)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s01.{k}"] for k in "abcd")

    def conta():
        form(c, t, a_, "3x × 2x = ?", W / 2, 330, 190, None, "center")
        for k, (s, tk, nota, ok) in enumerate((("5x", b_, "somou", False), ("6x", c_, "perdeu um x", False), ("6x^2", d_, "", True))):
            cx = 420 + k * 540
            form(c, t, tk, s, cx, 700, 170, CERTO if ok else ERRADO, "center")
            if nota:
                E.foco(c, t, tk + 0.8, 0.4, lambda p, nota=nota, cx=cx: centro(c, nota, cx, 830, 62, "i", ERRADO, p))
                if t >= tk + 0.8:
                    E.risco(c, cx - 150, 720, cx + 150, 560, t, tk + 0.8, largura=12)
            else:
                E.foco(c, t, tk + 0.3, 0.45, lambda p, cx=cx: E.selo(c, cx, 860, 60, True, p))
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]
    E.frase(c, t, a2, ps("até o fim desta aula, você", "i", 84), XE, 260, passo=0.12)
    E.frase(c, t, pal("s02", "multiplica"), ps("multiplica termos com letra", "g", 92, COR), XE, 410, passo=0.13)
    E.frase(c, t, b2 - 0.3, ps("e abre", "i", 96), XE, 580, passo=0.12)
    form(c, t, b2, "(x + 2)(x + 3)", XE + 300, 585, 120, COR)
    E.foco(c, t, c2 - 0.2, 0.7, lambda p: E.bola(c, 1600, 840, 190 * ease_back(prog(t, c2 - 0.2, 0.7))), blur=0)
    E.foco(c, t, c2 + 0.2, 0.5, lambda p: (centro(c, "+ atalho", 1600, 830, 64, "g", BR, p), centro(c, "de prova", 1600, 900, 64, "i", BR, p)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_ = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, C["s03"] + 0.3, ps("três", "g", 84, COR) + ps("lembretes", "i", 90), XE, 180)
    xr = XE + 110
    E.foco(c, t, a_, 0.45, lambda p: num_bola(c, "1", XE + 40, 330, 40, 50, p))
    form(c, t, a_, "x × x = x^2", xr, 360, 100)
    E.frase(c, t, pal("s03", "a"), ps("a base aparece duas vezes", "i", 64, TINTA2), xr + 640, 345, passo=0.1)
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "2", XE + 40, 560, 40, 50, p))
    E.frase(c, t, b_, ps("mesma base, multiplicando:", "i", 68), xr, 590, passo=0.1)
    E.frase(c, t, pal("s03", "repete"), ps("repete a base e", "i", 64) + ps("soma os expoentes", "g", 58, COR), xr + 640, 700, passo=0.1)
    form(c, t, pal("s03", "expoentes"), "2^3 × 2^4 = 2^7", xr, 710, 90, TINTA2)
    E.foco(c, t, c_, 0.45, lambda p: num_bola(c, "3", XE + 40, 860, 40, 50, p))
    form(c, t, c_, "3(x + 4) = 3x + 12", xr, 890, 100)
    E.frase(c, t, pal("s03", "multiplica"), ps("o de fora multiplica cada termo de dentro", "i", 58, TINTA2), xr, 990, passo=0.08)
    E.frase(c, t, pal("s03", "procure"), ps("faltou alguma? procure no canal", "i", 54, TINTA2), 1250, 180, passo=0.08)


# ---------------- termo vezes termo ----------------
def b_termos(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")

    def s04():
        form(c, t, C["s04"] + 0.3, "3x × 2x", W / 2, 260, 150, COR, "center")
        monta(c, t, [("= 3", a4), (" × x", pal("s04", "xis", 2)), (" × 2", pal("s04", "dois", 1)), (" × x", pal("s04", "xis", 3))], W / 2, 450, 130, "center")
        E.frase(c, t, b4, ps("a ordem não muda o resultado", "i", 76, TINTA2), W / 2, 590, "center", 0.11)
        L = "= 3 × 2 × x × x"
        realce(c, t, c4, L, "3 × 2", W / 2, 800, 130, align="center")
        realce(c, t, d4, L, "x × x", W / 2, 800, 130, TINTA2, "center")
        form(c, t, c4, L, W / 2, 800, 130, None, "center")
        x1, w1 = trecho_x(L, "3 × 2", W / 2, 130, "center")
        x2, w2 = trecho_x(L, "x × x", W / 2, 130, "center")
        E.foco(c, t, c4 + 0.3, 0.4, lambda p: centro(c, "números", x1 + w1 / 2, 900, 54, "i", COR, p))
        E.foco(c, t, d4 + 0.3, 0.4, lambda p: centro(c, "letras", x2 + w2 / 2, 900, 54, "i", TINTA2, p))
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)

    def s05():
        form(c, t, C["s05"], "3x × 2x = 3 × 2 × x × x", W / 2, 200, 90, TINTA2, "center")
        form(c, t, a5, "3 × 2 = 6", 300, 420, 120, COR)
        form(c, t, b5, "x × x = x^2", 1050, 420, 120)
        form(c, t, c5, "6x^2", W / 2, 680, 200, CERTO, "center")
        E.frase(c, t, pal("s05", "teste"), ps("teste com 10:", "i", 66, TINTA2), XE, 870, passo=0.1)
        form(c, t, d5, "30 × 20 = 600", 600, 875, 90)
        form(c, t, e5, "6 × 100 = 600", 600, 1000, 90)
        E.foco(c, t, e5 + 0.8, 0.45, lambda p: E.selo(c, 1300, 930, 50, True, p))
    fase(c, t, C["s05"], C["s06"] - 0.1, s05)

    def s06():
        E.frase(c, t, C["s06"] + 0.2, ps("com expoente:", "i", 80) + ps("regra da mesma base", "g", 74, COR), W / 2, 190, "center", 0.12)
        form(c, t, a6, "2x^2 × 4x", W / 2, 400, 150, None, "center")
        form(c, t, b6, "2 × 4 = 8", 300, 620, 110, COR)
        form(c, t, c6, "x^2 × x^1", 1000, 620, 110)
        E.foco(c, t, pal("s06", "que"), 0.4, lambda p: E.escreve(c, "x sozinho tem expoente 1", 1000, 690, 50, "i", TINTA2, p))
        form(c, t, pal("s06", "os"), "2 + 1 = 3", 1000, 780, 80, TINTA2)
        form(c, t, d6, "= x^3", 1000 + fw("x^2 × x^1 ", 110), 620, 110)
        form(c, t, e6, "8x^3", W / 2, 990, 150, CERTO, "center")
    fase(c, t, C["s06"], 1e9, s06)


# ---------------- soma × multiplicação ----------------
def b_contraste(c, t, C, b):
    a7, b7 = C["s07.a"], C["s07.b"]

    def s07():
        E.frase(c, t, C["s07"] + 0.3, ps("não misture com a", "i", 84) + ps("soma", "g", 78, COR), W / 2, 190, "center", 0.12)
        for i, (tit, f, nota, t0, tn) in enumerate((("somando", "3x + 2x = 5x", "termos semelhantes: a letra fica igual", a7, pal("s07", "são")),
                                                   ("multiplicando", "3x × 2x = 6x^2", "a letra ganha expoente", b7, pal("s07", "na")))):
            cx = 500 + i * 920
            q = ep(t, t0, 0.5)
            E.caixa_pontilhada(c, cx - 420, 300, 840, 560, q, COR if i else TINTA2, prog_=q)
            E.frase(c, t, t0, ps(tit, "g", 70, COR if i else TINTA2), cx, 410, "center")
            form(c, t, t0 + 0.3, f, cx, 600, 120, None, "center")
            E.foco(c, t, tn, 0.45, lambda p, nota=nota, cx=cx: centro(c, nota, cx, 760, 52, "i", TINTA, p))
    fase(c, t, C["s07"], C["s08"] - 0.1, s07)

    a8, b8, c8, d8, e8, f8, g8 = (C[f"s08.{k}"] for k in "abcdefg")

    def s08():
        form(c, t, a8, "x + x^2", XE, 300, 150)
        form(c, t, b8, "= 2x^3", XE + fw("x + x^2 ", 150), 300, 150, ERRADO)
        if t >= c8:
            E.risco(c, XE + fw("x + x^2 ", 150) - 20, 330, XE + fw("x + x^2 = 2x^3 ", 150) + 10, 170, t, c8, largura=14)
        E.frase(c, t, c8, ps("não são", "i", 80) + ps("semelhantes", "g", 74, COR), 1120, 260, passo=0.12)
        E.frase(c, t, pal("s08", "a"), ps("mesma letra, expoente diferente", "i", 60, TINTA2), 1120, 350, passo=0.1)
        E.frase(c, t, pal("s08", "teste"), ps("teste com 10:", "i", 66, TINTA2), XE, 500, passo=0.1)
        form(c, t, d8, "10 + 100 = 110", XE, 640, 110, CERTO)
        form(c, t, e8 - 0.8, "2x^3", 1000, 640, 80, ERRADO)
        E.frase(c, t, e8 - 0.6, ps("daria", "i", 70, ERRADO), 1170, 630)
        form(c, t, e8, "2.000", 1330, 640, 110, ERRADO)
        E.foco(c, t, f8, 0.5, lambda p: E.pilula(c, "na soma: mesma letra e mesmo expoente", W / 2, 800, 58, estilo="b", a=p))
        form(c, t, g8 - 0.6, "x + x^2", 620, 960, 110)
        E.frase(c, t, g8, ps("fica como está", "g", 80, CERTO), 1000, 955, passo=0.12)
    fase(c, t, C["s08"], 1e9, s08)


# ---------------- piso ----------------
PX, PY, PXX, PU = 330, 300, 380, 72
RX = 1060


def b_piso(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")

    def s09():
        E.frase(c, t, C["s09"] + 0.2, ps("e dois parênteses multiplicados?", "i", 84), W / 2, 220, "center", 0.11)
        monta(c, t, [("(", a9, COR), ("x + 2", pal("s09", "xis")), (")", pal("s09", "fecha"), COR),
                     ("(", b9, COR), ("x + 3", pal("s09", "xis", 1)), (")", pal("s09", "fecha", 1), COR)], W / 2, 520, 180, "center")
        E.frase(c, t, c9, ps("pense em um", "i", 90) + ps("piso retangular", "g", 84, COR), W / 2, 800, "center", 0.12)
    fase(c, t, C["s09"], C["s10"] - 0.1, s09)

    def s10():
        E.frase(c, t, a0 - 0.6, ps("lajotas que cobrem o piso =", "i", 76), XE, 200, passo=0.1)
        E.frase(c, t, a0, ps("área", "g", 90, COR), XE + 900, 205)
        l, x0, y0 = 130, 300, 340
        for i in range(3):
            for j in range(4):
                E.foco(c, t, b0 + (i * 4 + j) * 0.05, 0.3, lambda p, i=i, j=j: (M.rrect(c, x0 + j * l, y0 + i * l, l - 8, l - 8, 10, M.mix(E.COR, BR, 0.6), p),
                                                                                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + j * l, y0 + i * l, l - 8, l - 8), 10, 10), M.paint(E.COR, p, stroke=3))))
        E.foco(c, t, b0 + 0.3, 0.4, lambda p: (centro(c, "3 fileiras", x0 - 20 + 0, y0 + 3 * l + 70, 52, "i", TINTA2, p)))
        E.foco(c, t, b0 + 0.7, 0.4, lambda p: centro(c, "4 lajotas", x0 + 2 * l, y0 - 30, 52, "i", TINTA2, p))
        form(c, t, c0, "3 × 4 = 12", 1060, 520, 120)
        E.frase(c, t, d0 - 0.4, ps("área do retângulo:", "i", 72), 1060, 700, passo=0.1)
        E.frase(c, t, d0, ps("um lado × o outro", "g", 80, COR), 1060, 820, passo=0.12)
    fase(c, t, C["s10"], C["s11"] - 0.1, s10)

    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    if t < C["s11"]:
        return
    rot = tuple(ep(t, k, 0.4) for k in (a2, b2, c2, d2))
    E.foco(c, t, a1, 0.5, lambda p: piso(c, PX, PY, PXX, PU, p, ep(t, d1, 0.8), ep(t, e1, 0.6), rot))
    lados(c, t, a1, b1, PX, PY, PXX, PU)
    form(c, t, c1, "área = (x + 2)(x + 3)", RX, 340, 90, COR)
    form(c, t, e2, "= x^2 + 3x + 2x + 6", RX, 490, 90)
    realce(c, t, a3, "= x^2 + 3x + 2x + 6", "3x + 2x", RX, 490, 90)
    form(c, t, a3, "= x^2 + 5x + 6", RX, 640, 110, CERTO)
    E.frase(c, t, pal("s13", "teste"), ps("teste com 10:", "i", 60, TINTA2), RX, 770, passo=0.1)
    form(c, t, b3, "12 × 13 = 156", RX, 880, 80)
    form(c, t, c3, "100 + 50 + 6 = 156", RX, 1000, 80)
    E.foco(c, t, d3, 0.45, lambda p: E.selo(c, 1720, 850, 46, True, p))


# ---------------- chuveirinho ----------------
CH = "(x + 2)(x + 3)"


def chuveiro(c, t, ts, s, y, size, cor, align="center", x=W / 2, alto=90):
    """as quatro setas do chuveirinho, em ts = (x·x, x·3, 2·x, 2·3); s = fórmula com dois parênteses"""
    i2 = s.index(")(") + 1
    p1, p2 = s[1:i2 - 1], s[i2 + 1:-1]
    a1, b1 = p1.split(" ", 1)[0], p1.split(" ", 2)[2]
    a2, b2 = p2.split(" ", 1)[0], p2.split(" ", 2)[2]
    pos = lambda tr, n=0: trecho_x(s, tr, x, size, align, n)
    xa1, wa1 = pos(a1)
    xb1, wb1 = pos(b1)
    xa2, wa2 = pos(a2, 1 if a2 == a1 else 0)
    xb2, wb2 = pos(b2, 1 if b2 == b1 else 0)
    topo, base = y - size * 0.95, y + size * 0.2
    flecha(c, t, ts[0], xa1 + wa1 / 2, topo, xa2 + wa2 / 2, topo, alto * 1.4, cor)
    flecha(c, t, ts[1], xa1 + wa1 / 2, topo, xb2 + wb2 / 2, topo, alto * 2.2, cor)
    flecha(c, t, ts[2], xb1 + wb1 / 2, base, xa2 + wa2 / 2, base, -alto * 1.4, cor)
    flecha(c, t, ts[3], xb1 + wb1 / 2, base, xb2 + wb2 / 2, base, -alto * 2.2, cor)


def b_chuveirinho(c, t, C, b):
    a_, b_, c_, d_, e_, f_, g_ = (C[f"s14.{k}"] for k in "abcdefg")
    E.frase(c, t, C["s14"] + 0.3, ps("sem desenho:", "i", 80) + ps("o chuveirinho", "g", 80, COR), W / 2, 150, "center", 0.12)
    E.frase(c, t, pal("s14", "nome"), ps("de cada termo saem setas para todos os do outro parêntese", "i", 54, TINTA2), W / 2, 240, "center", 0.06)
    form(c, t, C["s14"] + 0.5, CH, W / 2, 540, 170, None, "center")
    chuveiro(c, t, (c_, d_, e_, f_), CH, 540, 170, COR)
    E.frase(c, t, b_, ps("cada termo do 1º multiplica cada termo do 2º", "b", 52, COR), W / 2, 820, "center", 0.08)
    monta(c, t, [("x^2", c_ + 0.2), (" + 3x", d_ + 0.2), (" + 2x", e_ + 0.2), (" + 6", f_ + 0.2)], W / 2, 950, 100, "center")
    E.foco(c, t, g_, 0.45, lambda p: centro(c, "os mesmos 4 pedaços do piso", W / 2, 1040, 50, "i", COR, p))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s15.{k}"] for k in "abcd")
    E.frase(c, t, C["s15"] + 0.3, ps("o erro mais comum", "g", 80, ERRADO), XE, 180)
    E.frase(c, t, a_, ps("só primeiro com primeiro e último com último", "i", 60), XE, 270, passo=0.08)
    s, y = 130, 520
    form(c, t, a_, CH, XE, y, s)
    x1, w1 = trecho_x(CH, "x", XE, s)
    x2, w2 = trecho_x(CH, "x", XE, s, n=1)
    x3, w3 = trecho_x(CH, "2", XE, s)
    x4, w4 = trecho_x(CH, "3", XE, s)
    flecha(c, t, a_ + 0.6, x1 + w1 / 2, y - s * 0.95, x2 + w2 / 2, y - s * 0.95, 110, ERRADO)
    flecha(c, t, a_ + 1.2, x3 + w3 / 2, y + s * 0.2, x4 + w4 / 2, y + s * 0.2, -110, ERRADO)
    form(c, t, b_, "= x^2 + 6", XE, 820, 130, ERRADO)
    E.foco(c, t, c_, 0.5, lambda p: piso(c, 1180, 300, 300, 56, p, 0, 1, (1, 1, 1, 1), ep(t, c_ + 0.3, 0.5)))
    E.foco(c, t, c_ + 0.5, 0.4, lambda p: centro(c, "as faixas do meio somem", 1180 + 230, 820, 54, "i", ERRADO, p))
    form(c, t, d_ - 0.6, "com 10:", XE, 980, 80, TINTA2)
    form(c, t, d_, "106", XE + 330, 985, 100, ERRADO)
    form(c, t, pal("s15", "não"), "e não 156", XE + 560, 985, 100, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    AM = "#FFD500"
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")

    def s16():
        E.frase(c, t, C["s16"] + 0.2, ps("agora, o atalho", "i", 80, CLARO), W / 2, 170, "center")
        E.frase(c, t, a6, ps("para parênteses do tipo", "i", 76, CLARO) + ps("x + um número", "g", 72, BR), W / 2, 280, "center", 0.11)
        form(c, t, a6 + 0.6, CH, W / 2, 450, 130, BR, "center")
        for k, (lab, conta, res, tk) in enumerate((("na frente", "", "x^2", b6), ("no meio", "2 + 3 = 5", "+ 5x", c6), ("no fim", "2 × 3 = 6", "+ 6", d6))):
            cx = 480 + k * 480
            E.frase(c, t, tk, ps(lab, "i", 64, CLARO), cx, 620, "center")
            if conta:
                form(c, t, tk + 0.8, conta, cx, 720, 70, CLARO, "center")
            form(c, t, (tk + 1.6) if conta else tk + 0.4, res, cx, 900, 150, AM, "center")
    fase(c, t, C["s16"], C["s17"] - 0.1, s16)

    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")

    def s17():
        E.frase(c, t, C["s17"] + 0.2, ps("funciona porque", "i", 80, CLARO), W / 2, 160, "center")
        q = ep(t, C["s17"] + 0.2, 0.5)
        piso(c, 200, 300, 300, 56, q, 0, 1, (1, 1, 1, 1))
        if t >= a7:
            for (dx, dy, w, h, k) in ((316, 0, 168, 300, 0), (0, 316, 300, 112, 0.3)):
                qq = ep(t, a7 + k, 0.4)
                E.caixa_pontilhada(c, 200 + dx - 8, 300 + dy - 8, w + 16, h + 16, qq, AM, prog_=qq)
        if t >= b7:
            qq = ep(t, b7, 0.4)
            E.caixa_pontilhada(c, 200 + 316 - 8, 300 + 316 - 8, 184, 128, qq, AM, prog_=qq)
        E.frase(c, t, a7, ps("faixas do meio:", "i", 64, CLARO) + ps("2x e 3x", "g", 64, BR), 800, 360, passo=0.1)
        E.frase(c, t, b7, ps("cantinho:", "i", 64, CLARO) + ps("2 × 3", "g", 64, BR), 800, 470, passo=0.1)
        E.frase(c, t, c7, ps("vale com menos,", "i", 66, CLARO) + ps("levando o sinal", "g", 62, BR), 800, 640, passo=0.1)
        E.frase(c, t, d7, ps("não vale com número na frente do x", "i", 64, CLARO), 800, 790, passo=0.08)
        form(c, t, pal("s17", "como"), "(2x + 1)", 800, 920, 90, BR)
        E.foco(c, t, pal("s17", "como") + 1.4, 0.45, lambda p: E.escreve(c, "→ chuveirinho", 1180, 915, 66, "b", AM, p))
    fase(c, t, C["s17"], 1e9, s17)


# ---------------- questão ----------------
Q = "(x + 4)(x − 1)"


def b_questao(c, t, C, b):
    a_, b_ = C["s18.a"], C["s18.b"]
    E.frase(c, t, C["s18"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, pal("s18", "multiplique"), ps("multiplique", "i", 110), XE, 420)
    monta(c, t, [("(", a_, COR), ("x + 4", pal("s18", "xis")), (")", pal("s18", "fecha"), COR),
                 ("(", b_, COR), ("x − 1", pal("s18", "xis", 1)), (")", pal("s18", "fecha", 1), COR)], XE, 680, 160)
    E.relogio(c, t, C["s19.a"], 1520, 440, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")
    s, y = 120, 260
    form(c, t, C["s20"] + 0.2, Q, XE, y, s)
    chuveiro(c, t, (a0, b0, c0, d0), Q, y, s, COR, "left", XE, 45)

    def s20():
        for k, (f, tk) in enumerate((("x × x = x^2", a0), ("x × (−1) = −x", b0), ("4 × x = 4x", c0), ("4 × (−1) = −4", d0))):
            form(c, t, tk + 0.3, f, XE + 60, 520 + k * 140, 90)
    fase(c, t, C["s20"], C["s21"] - 0.1, s20)

    def s21():
        E.frase(c, t, C["s21"] + 0.2, ps("juntando:", "i", 72, TINTA2), XE, 520, passo=0.1)
        form(c, t, a1, "−x + 4x = 3x", XE + 340, 525, 100)
        E.frase(c, t, b1 - 0.6, ps("resposta:", "i", 80), XE, 720, passo=0.1)
        form(c, t, b1, "x^2 + 3x − 4", XE + 380, 730, 150, CERTO)
        E.frase(c, t, pal("s21", "pelo"), ps("pelo atalho:", "i", 66, TINTA2), XE, 920, passo=0.1)
        form(c, t, c1, "4 − 1 = 3", XE + 420, 925, 90)
        form(c, t, d1, "4 × (−1) = −4", XE + 900, 925, 90)
        E.foco(c, t, e1, 0.45, lambda p: E.selo(c, 1700, 880, 56, True, p))
    fase(c, t, C["s21"], 1e9, s21)
    form(c, t, b1, "= x^2 + 3x − 4", XE + fw(Q + " ", s), y, s, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a1, b1 = C["s22.a"], C["s22.b"]

    def resumo():
        E.frase(c, t, C["s22"] + 0.3, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        E.foco(c, t, a1, 0.5, lambda p: num_bola(c, "1", 230, 430, 58, 66, p))
        E.frase(c, t, a1 + 0.1, ps("na multiplicação, a letra ganha", "i", 80) + ps("expoente", "g", 74, COR), 320, 460, passo=0.12)
        form(c, t, a1 + 0.9, "3x × 2x = 6x^2", 320, 590, 90, COR)
        E.foco(c, t, b1, 0.5, lambda p: num_bola(c, "2", 230, 730, 58, 66, p))
        E.frase(c, t, b1 + 0.1, ps("chuveirinho:", "i", 80) + ps("todo termo multiplica todo termo", "g", 70, COR), 320, 760, passo=0.12)
        form(c, t, b1 + 0.9, "(x + 2)(x + 3) = x^2 + 5x + 6", 320, 890, 90, COR)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a_, b_, c_, d_, e_ = (C[f"s23.{k}"] for k in "abcde")
    E.frase(c, t, C["s23"] + 0.2, ps("próxima aula", "i", 84), XE, 230)
    E.frase(c, t, a_, ps("praticar tudo isso", "g", 110, COR), XE, 380)
    E.frase(c, t, b_, ps("traduzir situações em expressões", "i", 80), XE, 520, passo=0.11)
    E.frase(c, t, c_, ps("e simplificar até o fim", "i", 80), XE, 630, passo=0.11)
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, d_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(620, 375, p), ep(t, d_ + 0.2, 0.4), TINTA)
    E.frase(c, t, e_, ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), 1450, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, termos=b_termos, contraste=b_contraste, piso=b_piso,
              chuveirinho=b_chuveirinho, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
