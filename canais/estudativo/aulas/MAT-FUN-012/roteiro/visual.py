"""Visual — Estudativo · MAT-FUN-012: achar a lei da função afim por dois pontos.

Linguagem visual da trilha Funções (MAT-FUN-001 a 011): entrada / x em índigo (ENT), saída / y em preto (SAI); eixo x índigo, eixo y preto;
par (x, y) com o x índigo e o y preto; plano na metade direita e texto à esquerda.
Da MAT-FUN-010: o degrau entre dois pontos (degrau()), andada Δx = seta índigo deitada, subida Δy = seta preta em pé (vermelha se desce);
o b = ponto preto em cima do eixo y, com o valor numa pílula preta (marca_y()).
Nesta aula: os dois passos do método em esferas numeradas (passo()); a conferência acende anel verde no ponto; a previsão é um ponto
verde novo; o atalho anda para trás em degraus (para_tras()) até o eixo y, no palco escuro.
Peças locais: mista(), lei(), eixos(), par(), degrau(), marca_y(), anel(), para_tras(), passo(), op(), resultado(), mini()."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FUN-012_achar_a_lei_por_dois_pontos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "grafico", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMAR = "#FFE680"

f = lambda x: 2 * x + 3
g = lambda x: -2 * x + 6
errada = lambda x: -2 * x + 7
tec = lambda x: 50 * x + 50
assert (9 - 5) / (3 - 1) == 2 and 5 - 2 * 1 == 3 and (f(1), f(3), f(4)) == (5, 9, 11)
assert (g(0), g(2)) == (6, 2) and (2 - 6) / (2 - 0) == -2
assert (9 - 5) / (1 - 3) == -2 and 5 + 2 == 7 and errada(3) == 1 and 5 - 2 == 3
assert (300 - 150) / (5 - 2) == 50 and 150 - 2 * 50 == 50 and (tec(2), tec(5), tec(6)) == (150, 300, 350)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fml(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def mista(c, partes, x, y, size, a=1.0, align="left", est="g"):
    ws = [E.larg(s, est, size) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x
    for (s, cor), w in zip(partes, ws):
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += w
    return sum(ws)


def lei(nome, corpo, cor=TINTA):
    partes = [(nome + "(", SAI), ("x", ENT), (") = ", SAI)]
    for p in corpo:
        partes.append((p, ENT) if p == "x" else (p, cor))
    return partes


def op(c, t, t0, s, x, y, cor=TINTA2, size=40):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, x, y, size, "g", fundo=cor, a=a))


def par(c, xv, yv, x, y, size, a=1.0, align="left", est="g", cores=None, tinta=TINTA):
    cx_, cy_ = cores or (ENT, SAI)
    partes = (("(", tinta), (xv, cx_), (", ", tinta), (yv, cy_), (")", tinta))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def eixos(c, t, P, t0, mx, my, nx="x", ny="y", size=36, escuro=False, grade=True):
    """plano em etapas (MAT-FUN-001/006/007): grade, eixo x índigo, eixo y preto (claros no palco)"""
    x, y, w, h = P.caixa
    if t < t0:
        return
    cx_, cy_, tt = (CLARO, BR, CLARO) if escuro else (ENT, SAI, TINTA2)
    q = ep(t, t0, 0.8)
    if grade:
        for v in mx:
            M.line(c, P.x(v), y, P.x(v), y + h, CLARO if escuro else FIO, q * (0.2 if escuro else 1), 2)
        for v in my:
            M.line(c, x, P.y(v), x + w, P.y(v), CLARO if escuro else FIO, q * (0.2 if escuro else 1), 2)
    M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, cx_, 1.0, 6, 24, ep(t, t0, 0.7))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.escreve(c, nx, x + w + 10 - E.larg(nx, "i", 46), P.oy - 22, 46, "i", cx_, a))
    for i, v in enumerate(mx):
        X = P.x(v)
        E.foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
            M.line(c, X, P.oy - 10, X, P.oy + 10, cx_, a, 4),
            centro(c, E._num(v), X + (14 if v == 0 else 0), P.oy + 14 + size, size, "b", tt, a)), sobe=6)
    M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, cy_, 1.0, 6, 24, ep(t, t0, 0.7))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.escreve(c, ny, P.ox + 22, y - 16, 46, "i", cy_, a))
    for i, v in enumerate(my):
        if v == 0:
            continue
        Y = P.y(v)
        E.foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
            M.line(c, P.ox - 10, Y, P.ox + 10, Y, cy_, a, 4),
            E.escreve(c, E._num(v), P.ox - 20 - E.larg(E._num(v), "b", size), Y + size * 0.36, size, "b", tt, a)), sobe=6)


def degrau(c, t, tx, ty, P, A, B, rx=None, ry=None, size=44, cx=ENT, cy=None, escuro=False, dy_rx=26):
    """o degrau entre A e B (MAT-FUN-010): andada Δx índigo deitada em tx, subida Δy preta em pé em ty (vermelha se desce)"""
    (ax, ay), (bx, by) = A, B
    cy = cy or (ERRADO if by < ay else (BR if escuro else SAI))
    p = ease_io(prog(t, tx, 0.7))
    if p > 0:
        M.arrow(c, *P(ax, ay), *P(bx, ay), cx, 1.0, 7, 24, p)
        if rx:
            E.foco(c, t, tx + 0.4, 0.4, lambda a: E.formula(c, rx, (P.x(ax) + P.x(bx)) / 2, P.y(ay) + (size + dy_rx if by >= ay else -dy_rx), size, "g", cx, a, "center"))
    p = ease_io(prog(t, ty, 0.7))
    if p > 0:
        M.arrow(c, *P(bx, ay), *P(bx, by), cy, 1.0, 7, 24, p)
        if ry:
            E.foco(c, t, ty + 0.4, 0.4, lambda a: E.formula(c, ry, P.x(bx) + 24, (P.y(ay) + P.y(by)) / 2 + size * 0.35, size, "g", cy, a))


def marca_y(c, t, t0, P, v, cor=SAI, size=40, txt=None):
    s = txt or E._num(v)
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, P.ox - 24 - E.larg(s, "g", size) / 2, P.y(v), size, "g", fundo=cor, a=a), sobe=0)


def anel(c, t, t0, P, xv, yv, cor=SAI, r=28, largura=6):
    q = ease_out(prog(t, t0, 0.5))
    if q > 0:
        E.arco(c, *P(xv, yv), r, -90, 360 * q, cor, largura)


def para_tras(c, t, ts, P, A, a_, cx=ENT, cy=ERRADO, d=0.6):
    """anda para trás no x, um passo por instante de ts, e o y muda a_ por passo (setas: índigo para a esquerda, vermelha/verde em pé)"""
    x0, y0 = A
    for i, ti in enumerate(ts):
        xa, ya = x0 - i, y0 - a_ * i
        xb, yb = xa - 1, ya - a_
        p = ease_io(prog(t, ti, d))
        if p > 0:
            M.arrow(c, *P(xa, ya), *P(xb, ya), cx, 1.0, 7, 24, p)
        p = ease_io(prog(t, ti + d * 0.9, d))
        if p > 0:
            M.arrow(c, *P(xb, ya), *P(xb, yb), cy if yb < ya else CERTO, 1.0, 7, 24, p)


def passo(c, t, t0, n, partes, x, y, size=72, escuro=False):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, x + 44, y - size * 0.32, 44, a=a), centro(c, str(n), x + 44, y - size * 0.32 + 20, 56, "g", BR, a)))
    E.frase(c, t, t0 + 0.1, partes, x + 120, y)


def resultado(c, t, t0, s, cx, cy, r=110):
    k = ease_back(prog(t, t0, 0.6))
    if k > 0:
        E.bola(c, cx, cy, r * k)
        size = r * (0.62 if len(s) <= 4 else 0.5 if len(s) <= 6 else 0.4)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", BR, a), sobe=0)


P1 = E.Plano(1120, 190, 660, 700, -0.6, 5.6, -0.6, 12.6)
X1, Y1 = list(range(0, 6)), list(range(0, 13, 2))
LF = lei("f", ["2", "x", " + 3"])


def plano1(c, t, t0, pontos=True, tp=None):
    eixos(c, t, P1, t0, X1, Y1)
    if pontos:
        tp = tp or (t0, t0)
        for (xv, yv), ti in zip(((1, 5), (3, 9)), tp):
            E.ponto(c, t, ti, P1, xv, yv, cor=COR, r=16)
            if xv == 1:
                E.foco(c, t, ti + 0.2, 0.4, lambda a, xv=xv, yv=yv: par(c, E._num(xv), E._num(yv), P1.x(xv) + 30, P1.y(yv) + 56, 40, a))
            else:
                E.foco(c, t, ti + 0.2, 0.4, lambda a, xv=xv, yv=yv: par(c, E._num(xv), E._num(yv), P1.x(xv) - 26, P1.y(yv) - 6, 40, a, "right"))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        plano1(c, t, C["s01.a"], True, (C["s01.b"], C["s01.c"]))
        E.frase(c, t, C["s01.a"], [("só", "i", 76), ("2", "g", 90, COR), ("pontos", "g", 80, COR)], XE, 260)
        E.foco(c, t, C["s01.b"], 0.4, lambda a: par(c, "1", "5", XE, 400, 84, a))
        E.foco(c, t, C["s01.c"], 0.4, lambda a: par(c, "3", "9", XE + 320, 400, 84, a))
        E.frase(c, t, C["s01.d"], [("a", "i", 76), ("fórmula", "g", 80), ("inteira", "i", 76)], XE, 580)
        E.foco(c, t, C["s01.d"] + 0.6, 0.4, lambda a: E.formula(c, "f(x) = ?", XE, 720, 96, "g", COR, a))
        E.frase(c, t, C["s01.e"], [("e", "i", 70), ("prever", "g", 76, CERTO), ("o", "i", 70), ("resto", "i", 70)], XE, 880)
        k = ease_back(prog(t, C["s01.e"] + 0.4, 0.4))
        if k > 0:
            c.drawCircle(*P1(4.5, 12), 15 * k, M.paint(CERTO))
            E.centro(c, "?", P1.x(4.5) + 40, P1.y(12) + 20, 56, "g", CERTO, k)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.4, [("a", "i", 90), ("lei", "g", 110, COR), ("por", "i", 90), ("2", "g", 110, COR), ("pontos", "g", 100)], XE, 460)
        E.frase(c, t, C["s02.b"], [("ou", "i", 84), ("lendo", "i", 84), ("o", "i", 84), ("gráfico", "g", 90, COR)], XE, 640)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 200, 700, 120, "i", TINTA, a))
    x, w, y = 900, 860, 230
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, y, w, 620, p, prog_=p)
    E.foco(c, t, C["s03.b"], 0.5, lambda a: mista(c, lei("f", ["a", "x", " + b"]), x + 44, y + 120, 84, a))
    E.foco(c, t, C["s03.c"], 0.5, lambda a: E.formula(c, "a = f{Δy}{Δx}", x + 44, y + 300, 80, "g", COR, a))
    E.foco(c, t, C["s03.c"] + 0.4, 0.4, lambda a: E.escreve(c, "taxa de variação", x + 420, y + 290, 46, "i", TINTA2, a))
    E.foco(c, t, C["s03.d"], 0.5, lambda a: E.escreve(c, "b = y no x = 0", x + 44, y + 500, 72, "g", COR, a))
    E.foco(c, t, C["s03.d"] + 0.4, 0.4, lambda a: E.escreve(c, "valor inicial", x + 560, y + 500, 46, "i", TINTA2, a))
    E.cursor(c, x + w - 30, y + 600, ep(t, C["s03.b"], 0.4))


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    plano1(c, t, C["s04"])

    def s04():
        E.frase(c, t, C["s04.a"], [("2", "g", 110, COR), ("passos", "g", 100)], XE, 320)
        passo(c, t, C["s04.a"] + 0.8, 1, [("o", "i", 80), ("a", "g", 96, COR)], XE, 520, 80)
        passo(c, t, C["s04.a"] + 1.8, 2, [("o", "i", 80), ("b", "g", 96, COR)], XE, 680, 80)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    degrau(c, t, C["s05.c"], C["s05.b"], P1, (1, 5), (3, 9), "Δx = 2", "Δy = 4", dy_rx=96)

    def s05():
        passo(c, t, C["s05.a"], 1, [("o", "i", 76), ("a", "g", 90, COR)], XE, 230, 76)
        fml(c, t, C["s05.b"], "Δy = 9 − 5 = 4", XE, 400, 76)
        fml(c, t, C["s05.c"], "Δx = 3 − 1 = 2", XE, 530, 76, ENT)
        fml(c, t, C["s05.d"], "a = f{4}{2} = 2", XE, 720, 96, COR)
        E.frase(c, t, C["s05.e"], [("x", "g", 60, ENT), ("anda", "i", 58), ("1", "g", 62, ENT), ("→", "g", 60, TINTA2), ("y", "g", 60), ("sobe", "i", 58),
                                   ("2", "g", 62, CERTO)], XE, 880)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    passo(c, t, C["s06.a"], 2, [("o", "i", 76), ("b", "g", 90, COR)], XE, 230, 76)

    def s06():
        E.foco(c, t, C["s06.b"], 0.5, lambda a: mista(c, lei("f", ["2", "x", " + b"]), XE, 380, 84, a))
        E.frase(c, t, C["s06.c"], [("um", "i", 60), ("ponto:", "i", 60)], XE, 500)
        E.foco(c, t, C["s06.c"] + 0.3, 0.4, lambda a: par(c, "1", "5", XE + 260, 500, 66, a))
        fml(c, t, C["s06.d"], "2 · 1 + b = 5", XE, 650, 84)
    E.saida(c, t, C["s07"] - 0.1, s06)
    anel(c, t, C["s06.c"], P1, 1, 5, COR, 30)
    if t < C["s07"]:
        return
    fml(c, t, C["s07.a"], "2 + b = 5", XE, 400, 84)
    fml(c, t, C["s07.b"], "b = 3", XE + 120, 540, 90, COR)
    op(c, t, C["s07.b"], "−2 dos dois lados", XE + 640, 510)
    E.ponto(c, t, C["s07.b"] + 0.3, P1, 0, 3, cor=SAI, r=15)
    marca_y(c, t, C["s07.b"] + 0.5, P1, 3)
    E.foco(c, t, C["s07.c"], 0.5, lambda a: mista(c, LF, XE, 760, 110, a))
    q = ep(t, C["s07.c"] + 0.2, 0.4)
    if q > 0:
        M.rrect(c, XE - 30, 650, mista(c, LF, XE, 760, 110, 0) + 60, 150, 24, COR, 0.08 * q)
    if t >= C["s07.c"]:
        E.reta_pontos(c, t, C["s07.c"], P1, (1, 5), (3, 9), pontos=False)


# ---------------- conferir e prever ----------------
def b_prever(c, t, C, b):
    plano1(c, t, C["s08"] - 3)
    E.reta_pontos(c, t, C["s08"] - 3, P1, (1, 5), (3, 9), pontos=False, d=0.1)
    mista(c, LF, XE, 210, 96, ep(t, C["s08"] - 2, 0.3))
    E.frase(c, t, C["s08.a"], [("confira", "g", 66, CERTO), ("com", "i", 64), ("o", "i", 64), ("outro", "i", 64), ("ponto", "i", 64)], XE, 350)
    anel(c, t, C["s08.a"], P1, 3, 9, CERTO, 32)
    fml(c, t, C["s08.b"], "2 · 3 + 3 = 9", XE, 480, 80)
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.selo(c, XE + 620, 452, 38, True, a))
    E.frase(c, t, C["s08.d"], [("prever:", "g", 66, CERTO), ("x", "g", 70, ENT), ("=", "g", 66), ("4", "g", 70, ENT)], XE, 660)
    fml(c, t, C["s08.e"], "2 · 4 + 3 = 11", XE, 800, 80)
    E.ponto(c, t, C["s08.e"] + 0.8, P1, 4, 11, cor=CERTO, r=17)
    anel(c, t, C["s08.e"] + 1.0, P1, 4, 11, CERTO, 32)
    E.foco(c, t, C["s08.e"] + 1.0, 0.4, lambda a: par(c, "4", "11", P1.x(4) + 40, P1.y(11) + 14, 40, a))
    resultado(c, t, C["s08.e"] + 1.2, "11", XE + 760, 780, 80)


# ---------------- gráfico ----------------
P2 = E.Plano(1120, 190, 660, 700, -1.2, 4.6, -1.2, 7.6)
X2, Y2 = list(range(-1, 5)), list(range(-1, 8))


def b_grafico(c, t, C, b):
    eixos(c, t, P2, C["s09.a"] - 0.4, X2, Y2)
    if t >= C["s09.a"]:
        E.reta_pontos(c, t, C["s09.a"], P2, (0, 6), (2, 2), pontos=False, d=0.9)
    q = ep(t, C["s09.b"], 0.4) * (1 - ep(t, C["s09.c"], 0.4))
    if q > 0:
        for xv in X2:
            for yv in Y2:
                if abs(g(xv) - yv) < 1e-9:
                    c.drawCircle(*P2(xv, yv), 22, M.paint(CERTO, 0.35 * q))
    for k, xv, yv in (("s09.c", 0, 6), ("s09.d", 2, 2)):
        E.ponto(c, t, C[k], P2, xv, yv, cor=COR, r=16)
        anel(c, t, C[k] + 0.2, P2, xv, yv, COR, 30)
        E.saida(c, t, C["s10.c"] - 0.2, lambda k=k, xv=xv, yv=yv: E.foco(c, t, C[k] + 0.3, 0.4, lambda a: par(c, E._num(xv), E._num(yv), P2.x(xv) + 34, P2.y(yv) - 20, 40, a)))

    def s09():
        E.frase(c, t, C["s09.a"], [("só", "i", 70), ("o", "i", 70), ("gráfico?", "g", 76, COR)], XE, 280)
        E.frase(c, t, C["s09.b"], [("pontos", "i", 60), ("no", "i", 60), ("cruzamento", "g", 62), ("da", "i", 60), ("grade", "g", 62)], XE, 420)
        E.foco(c, t, C["s09.c"], 0.4, lambda a: par(c, "0", "6", XE, 580, 84, a))
        E.foco(c, t, C["s09.d"], 0.4, lambda a: par(c, "2", "2", XE + 320, 580, 84, a))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("em", "i", 62), ("cima", "i", 62), ("do", "i", 62), ("eixo", "i", 62), ("y:", "g", 64), ("x", "g", 64, ENT), ("=", "g", 62), ("0", "g", 64, ENT)],
            XE, 230)
    marca_y(c, t, C["s10.b"], P2, 6)
    fml(c, t, C["s10.b"], "b = 6", XE, 360, 84, COR)
    degrau(c, t, C["s10.d"], C["s10.c"], P2, (0, 6), (2, 2), "Δx = 2", "Δy = −4")
    fml(c, t, C["s10.c"], "Δy = 2 − 6 = −4", XE, 500, 70, ERRADO)
    fml(c, t, C["s10.d"], "Δx = 2 − 0 = 2", XE, 610, 70, ENT)
    fml(c, t, C["s10.e"], "a = f{−4}{2} = −2", XE, 780, 84, COR)
    E.foco(c, t, C["s10.f"], 0.5, lambda a: mista(c, lei("f", ["−2", "x", " + 6"]), XE, 950, 96, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano1(c, t, C["s11"] - 2)

    def s11():
        E.frase(c, t, C["s11.a"], [("trocar", "g", 66, ERRADO), ("a", "i", 64), ("ordem", "g", 66), ("no", "i", 64), ("meio", "i", 64)], XE, 240)
        if t < C["s11.c"]:
            E.foco(c, t, C["s11.b"], 0.4, lambda a: E.formula(c, "f{9 − 5}{?}", XE, 460, 90, "g", TINTA, a))
        else:
            E.foco(c, t, C["s11.c"], 0.3, lambda a: E.formula(c, "f{9 − 5}{1 − 3}", XE, 460, 90, "g", ERRADO, a), sobe=0)
        fml(c, t, C["s11.d"], "= f{4}{−2} = −2", XE + 300, 460, 90, ERRADO)
        E.frase(c, t, C["s11.e"], [("a", "i", 64), ("reta", "g", 66), ("que", "i", 64), ("sobe", "g", 66, CERTO), ("viraria", "i", 64)], XE, 680)
        E.frase(c, t, C["s11.e"] + 1.0, [("uma", "i", 64), ("que", "i", 64), ("desce", "g", 66, ERRADO)], XE, 780)
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t >= C["s11.e"]:
        E.reta_pontos(c, t, C["s11.e"], P1, (1, 5), (2, 3), cor=ERRADO, pontos=False)
    if t < C["s12"]:
        return
    fml(c, t, C["s12.a"], "b = 7", XE, 250, 76, ERRADO)
    E.foco(c, t, C["s12.a"] + 0.6, 0.4, lambda a: mista(c, lei("f", ["−2", "x", " + 7"], ERRADO), XE + 300, 250, 76, a))
    fml(c, t, C["s12.b"], "x = 3:  −6 + 7 = 1", XE, 400, 72, ERRADO)
    E.foco(c, t, C["s12.b"] + 0.8, 0.4, lambda a: E.escreve(c, "o ponto pede 9", XE + 700, 400, 50, "i", TINTA2, a))
    E.ponto(c, t, C["s12.b"] + 0.4, P1, 3, 1, cor=ERRADO, r=15)
    anel(c, t, C["s12.b"] + 0.6, P1, 3, 9, ERRADO, 32)
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.formula(c, "f{9 − 5}{3 − 1}", XE, 620, 90, "g", CERTO, a))
    E.frase(c, t, C["s12.c"] + 0.8, [("quem", "i", 52), ("entra", "i", 52), ("primeiro", "g", 54), ("em", "i", 52), ("cima,", "i", 52)], XE + 320, 590)
    E.frase(c, t, C["s12.c"] + 1.6, [("entra", "i", 52), ("primeiro", "g", 54), ("embaixo", "i", 52)], XE + 320, 660)
    op(c, t, C["s12.d"], "a conferência denuncia a troca", XE + 380, 830, COR, 44)


# ---------------- atalho (palco escuro) ----------------
PA = E.Plano(1160, 220, 600, 640, -0.6, 3.6, -0.6, 10.6)
XA, YA = list(range(0, 4)), list(range(0, 11, 2))


def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho para o b", "i", 64, CLARO), XE, 170)
        E.frase(c, t, C["s13.a"], [("ande", "g", 76, BR), ("para", "i", 72, CLARO), ("trás", "g", 76, BR)], XE, 310)
        E.frase(c, t, C["s13.a"] + 0.8, [("até", "i", 72, CLARO), ("o", "i", 72, CLARO), ("x", "g", 76, CLARO), ("=", "g", 76, BR), ("0", "g", 76, BR)], XE, 410)
        E.frase(c, t, C["s13.b"], [("a", "g", 62, CLARO), ("=", "g", 60, BR), ("2:", "g", 62, BR), ("cada", "i", 58, CLARO), ("passo", "i", 58, CLARO), ("atrás,", "i", 58, CLARO),
                                   ("−2", "g", 64, ERRADO)], XE, 560)
        eixos(c, t, PA, C["s13"], XA, YA, escuro=True)
        E.curva(c, t, C["s13"] + 0.3, PA, f, -0.6, 3.6, d=0.6, cor=CLARO, largura=6)
        E.ponto(c, t, C["s13"] + 0.6, PA, 1, 5, cor=BR, r=15)
        E.ponto(c, t, C["s13"] + 0.7, PA, 3, 9, cor=BR, r=15)
        anel(c, t, C["s13.c"], PA, 1, 5, AMAR, 30)
        E.foco(c, t, C["s13.c"], 0.4, lambda a: par(c, "1", "5", XE, 700, 70, a, cores=(CLARO, BR), tinta=BR))
        para_tras(c, t, [C["s13.d"]], PA, (1, 5), 2, cx=CLARO)
        fml(c, t, C["s13.e"], "5 − 2 = 3", XE + 320, 700, 70, BR)
        E.ponto(c, t, C["s13.f"], PA, 0, 3, cor=AMAR, r=17)
        anel(c, t, C["s13.f"] + 0.2, PA, 0, 3, AMAR, 32)
        E.foco(c, t, C["s13.f"], 0.4, lambda a: E.pilula(c, "= b", XE + 200, 840, 60, "g", fundo=COR, a=a))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], [("b", "g", 70, AMAR), ("=", "g", 66, BR), ("y", "g", 70, BR), ("no", "i", 66, CLARO), ("x", "g", 70, CLARO), ("=", "g", 66, BR),
                               ("0", "g", 70, BR)], XE, 220)
    E.frase(c, t, C["s14.a"] + 1.2, [("a:", "g", 60, CLARO), ("quanto", "i", 58, CLARO), ("muda", "i", 58, CLARO), ("por", "i", 58, CLARO), ("passo", "g", 60, BR)], XE, 320)
    E.frase(c, t, C["s14.a"] + 3.2, [("a", "g", 58, CLARO), ("negativo:", "g", 58, ERRADO), ("para", "i", 56, CLARO), ("trás", "i", 56, CLARO), ("soma", "g", 58, CERTO)],
            XE, 410)
    E.frase(c, t, C["s14.b"], [("não", "g", 64, ERRADO), ("compensa:", "i", 62, CLARO), ("ponto", "i", 62, CLARO), ("longe", "g", 64, BR), ("do", "i", 62, CLARO),
                               ("zero", "g", 64, BR)], XE, 580)
    E.frase(c, t, C["s14.c"], [("x", "g", 64, CLARO), ("=", "g", 62, BR), ("100:", "g", 64, BR), ("100", "g", 64, BR), ("passos", "i", 60, CLARO), ("para", "i", 60, CLARO),
                               ("trás", "i", 60, CLARO)], XE, 690)
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.pilula(c, "troque o ponto na fórmula", XE + 420, 840, 54, "g", fundo=COR, a=a))
    # degraus para trás, muitos, ao longe
    q = ep(t, C["s14.c"], 0.4)
    if q > 0:
        x0, y0 = 1700, 520
        n = 12
        for i in range(n):
            k = ep(t, C["s14.c"] + 0.12 * i, 0.3)
            if k <= 0:
                continue
            xa, ya = x0 - i * 50, y0 + i * 30
            M.line(c, xa, ya, xa - 50, ya, CLARO, k, 5)
            M.line(c, xa - 50, ya, xa - 50, ya + 30, ERRADO, k, 5)
        E.foco(c, t, C["s14.c"] + 1.4, 0.4, lambda a: E.escreve(c, "…", 1050, 900, 90, "g", CLARO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 64, COR), XE, 170)
    E.frase(c, t, C["s15"] + 0.6, [("um", "i", 64), ("técnico", "g", 66)], XE, 280)
    E.frase(c, t, C["s15.a"], [("2", "g", 76, ENT), ("h", "g", 72, ENT), ("→", "g", 72, TINTA2), ("R$", "g", 76), ("150", "g", 76)], XE, 430)
    E.frase(c, t, C["s15.b"], [("5", "g", 76, ENT), ("h", "g", 72, ENT), ("→", "g", 72, TINTA2), ("R$", "g", 76), ("300", "g", 76)], XE, 560)
    perguntas = (("s15.c", "1", [("a", "i", 62), ("lei", "g", 64, COR), ("do", "i", 62), ("preço?", "i", 62)]),
                 ("s15.d", "2", [("6", "g", 64, ENT), ("horas", "i", 62), ("custam?", "i", 62)]))
    for i, (k, n, partes) in enumerate(perguntas):
        yy = 740 + i * 130
        E.foco(c, t, C[k], 0.5, lambda a, n=n, yy=yy: (E.bola(c, XE + 34, yy - 20, 34, a=a), centro(c, n, XE + 34, yy - 4, 44, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, XE + 100, yy)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1440, cy=520, r=150)


# ---------------- resposta ----------------
P3 = E.Plano(1120, 200, 660, 680, -0.6, 6.6, -25, 390)
X3, Y3 = list(range(0, 7)), [0, 100, 200, 300]


def b_resposta(c, t, C, b):
    eixos(c, t, P3, C["s17"] - 0.4, X3, Y3, "horas", "R$")
    for k, xv, yv in (("s17.a", 2, 150), ("s17.b", 5, 300)):
        E.ponto(c, t, C[k], P3, xv, yv, cor=COR, r=16)
        E.foco(c, t, C[k] + 0.2, 0.4, lambda a, xv=xv, yv=yv: par(c, E._num(xv), E._num(yv), P3.x(xv) - 26 if xv == 5 else P3.x(xv) + 30,
                                                                  P3.y(yv) - 10 if xv == 5 else P3.y(yv) + 60, 40, a, "right" if xv == 5 else "left"))

    def s17():
        E.foco(c, t, C["s17.a"], 0.4, lambda a: par(c, "2", "150", XE, 260, 72, a))
        E.foco(c, t, C["s17.b"], 0.4, lambda a: par(c, "5", "300", XE + 360, 260, 72, a))
        fml(c, t, C["s17.c"], "Δy = 300 − 150 = 150", XE, 430, 66)
        fml(c, t, C["s17.d"], "Δx = 5 − 2 = 3", XE, 540, 66, ENT)
        fml(c, t, C["s17.e"], "a = f{150}{3} = 50", XE, 720, 84, COR)
        E.frase(c, t, C["s17.e"] + 1.0, [("R$", "g", 56), ("50", "g", 58), ("por", "i", 54), ("hora", "g", 56, ENT)], XE, 860)
        degrau(c, t, C["s17.d"], C["s17.c"], P3, (2, 150), (5, 300), "Δx = 3", "Δy = 150")
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("o", "i", 62), ("b,", "g", 66, COR), ("pelo", "i", 62), ("atalho", "g", 66)], XE, 240)
    para_tras(c, t, [C["s18.a"], C["s18.a"] + 1.4], P3, (2, 150), 50)
    E.frase(c, t, C["s18.a"], [("2", "g", 58, ENT), ("passos", "i", 56), ("atrás:", "i", 56), ("−50", "g", 58, ERRADO), ("cada", "i", 56)], XE, 350)
    fml(c, t, C["s18.b"], "150 − 100 = 50", XE, 470, 72)
    E.ponto(c, t, C["s18.b"] + 0.3, P3, 0, 50, cor=SAI, r=15)
    marca_y(c, t, C["s18.b"] + 0.5, P3, 50)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: mista(c, lei("f", ["50", "x", " + 50"]), XE, 620, 90, a))
    if t >= C["s18.c"]:
        E.reta_pontos(c, t, C["s18.c"], P3, (2, 150), (5, 300), pontos=False)
    fml(c, t, C["s18.d"], "50 · 6 = 300", XE, 770, 70)
    fml(c, t, C["s18.e"], "300 + 50 = 350", XE, 880, 70, CERTO)
    E.ponto(c, t, C["s18.e"] + 0.4, P3, 6, 350, cor=CERTO, r=17)
    anel(c, t, C["s18.e"] + 0.6, P3, 6, 350, CERTO, 32)
    E.foco(c, t, C["s18.e"] + 0.8, 0.4, lambda a: E.pilula(c, "R$ 350", XE + 720, 850, 56, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
PN = E.Plano(1180, 420, 560, 440, -1, 6, -1, 6)


def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", [("a", "g", 84, COR), ("=", "g", 80), ("Δy", "g", 80), ("÷", "g", 80, TINTA2), ("Δx", "g", 80, ENT)]),
                 ("s19.b", [("b:", "g", 80, COR), ("um", "i", 76), ("ponto", "g", 80), ("na", "i", 76), ("fórmula", "i", 76)]),
                 ("s19.c", [("o", "i", 76), ("outro", "i", 76), ("ponto", "i", 76), ("confere", "g", 80, CERTO)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 28, 52, a=a),
                                                         E.escreve(c, str(i + 1), 230 - E.larg(str(i + 1), "g", 60) / 2, y - 6, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 320, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s20.a"], [("a", "i", 80), ("reta", "g", 86), ("pela", "i", 80), ("origem", "g", 86, COR)], XE, 410)
    E.frase(c, t, C["s20.b"], [("grandezas", "g", 64), ("proporcionais", "g", 64, COR)], XE, 540)
    E.frase(c, t, C["s20.c"], [("táxi", "g", 60), ("com", "i", 58), ("bandeirada:", "i", 58), ("não", "g", 60, ERRADO)], XE, 660)
    if t >= C["s20.a"]:
        E.plano(c, t, C["s20.a"], *PN.caixa, PN.xmin, PN.xmax, PN.ymin, PN.ymax, grade=False, rotulos=False, size=30, d=0.5)
        E.curva(c, t, C["s20.a"] + 0.3, PN, lambda v: 0.9 * v, 0, 6, d=0.8)
        E.ponto(c, t, C["s20.a"] + 0.4, PN, 0, 0, cor=SAI, r=14)
        E.curva(c, t, C["s20.c"], PN, lambda v: 0.5 * v + 2, 0, 6, d=0.8, cor=TINTA2, tracejada=True)
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 260, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(520, 285, p), ep(t, C["s20.d"] + 0.2, 0.4))
    E.frase(c, t, C["s20.e"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, prever=b_prever, grafico=b_grafico, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
