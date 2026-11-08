"""Visual — Estudativo · MAT-FUN-010: coeficientes da função afim, taxa de variação e valor inicial.

Linguagem visual da trilha Funções (MAT-FUN-001 a 009): entrada / x em índigo (ENT), saída / y em preto (SAI); eixo x índigo, eixo y preto;
par (x, y) com o x índigo e o y preto; plano na metade direita e texto à esquerda; o "a" e o "b" da lei ganham caixa pontilhada (MAT-FUN-009).
Nesta aula:
- valor inicial (b) = o ponto da reta em cima do eixo y, com pílula preta no valor (é um y);
- taxa de variação (a) = o degrau entre dois pontos (degrau()): a andada Δx é uma seta índigo deitada e a subida Δy uma seta preta em pé,
  as mesmas cores do x e do y; subida que desce sai em vermelho;
- sinal do a: três mini-gráficos (sobe = verde, desce = vermelho, constante = cinza);
- palco escuro só no atalho.
Peças locais: mista(), caixa_em(), eixos(), par(), degrau(), marca_y(), mini(), tabela2(), salto_tab(), resultado()."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FUN-010_coeficientes_taxa_de_variacao_e_valor_inicial.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("inicial", "delta", "sinal", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMAR = "#FFE680"

loc = lambda x: 40 + 0.5 * x
vela = lambda x: 20 - 2 * x
assert (loc(0), loc(1), loc(2), loc(3), loc(10), loc(30)) == (40, 40.5, 41, 41.5, 45, 55)
assert (55 - 45) / (30 - 10) == 0.5 and 40 * 10 + 0.5 == 400.5
assert (vela(1), vela(4)) == (18, 12) and (12 - 18) / (4 - 1) == -2


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
    cs = []
    for (s, cor), w in zip(partes, ws):
        E.escreve(c, s, xx, y, size, est, cor, a)
        cs.append((xx + w / 2, w))
        xx += w
    return cs


def mista_em(c, t, t0, partes, x, y, size, align="left", est="g"):
    E.foco(c, t, t0, 0.5, lambda a: mista(c, partes, x, y, size, a, align, est))
    return mista(c, partes, x, y, size, 0, align, est)


def caixa_em(c, t, t0, cx, w, y, size, cor=None, d=0.5):
    p = ep(t, t0, d)
    if p > 0:
        E.caixa_pontilhada(c, cx - w / 2 - 14, y - size * 0.86, w + 28, size * 1.12, p, cor, p)


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


def marca_y(c, t, t0, P, v, cor=SAI, size=40, txt=None):
    s = txt or E._num(v)
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, P.ox - 24 - E.larg(s, "g", size) / 2, P.y(v), size, "g", fundo=cor, a=a), sobe=0)


def degrau(c, t, tx, ty, P, A, B, rx=None, ry=None, size=44, cx=ENT, cy=None, escuro=False):
    """o degrau entre A e B: andada Δx (seta índigo deitada) em tx e subida Δy (seta preta em pé, vermelha se desce) em ty"""
    (ax, ay), (bx, by) = A, B
    cy = cy or (ERRADO if by < ay else (BR if escuro else SAI))
    p = ease_io(prog(t, tx, 0.7))
    if p > 0:
        M.arrow(c, *P(ax, ay), *P(bx, ay), cx, 1.0, 7, 24, p)
        if rx:
            E.foco(c, t, tx + 0.4, 0.4, lambda a: E.formula(c, rx, (P.x(ax) + P.x(bx)) / 2, P.y(ay) + (size + 26 if by >= ay else -26), size, "g", cx, a, "center"))
    p = ease_io(prog(t, ty, 0.7))
    if p > 0:
        M.arrow(c, *P(bx, ay), *P(bx, by), cy, 1.0, 7, 24, p)
        if ry:
            E.foco(c, t, ty + 0.4, 0.4, lambda a: E.formula(c, ry, P.x(bx) + 24, (P.y(ay) + P.y(by)) / 2 + size * 0.35, size, "g", cy, a))


def resultado(c, t, t0, s, cx, cy, r=110):
    k = ease_back(prog(t, t0, 0.6))
    if k > 0:
        E.bola(c, cx, cy, r * k)
        size = r * (0.62 if len(s) <= 4 else 0.5 if len(s) <= 6 else 0.4)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", BR, a), sobe=0)


def mini(c, t, t0, x, y, w, h, fn, cor=None, d=0.7):
    """mini-gráfico (MAT-FUN-006/007): eixos simples e a reta de fn"""
    Q = E.plano(c, t, t0, x, y, w, h, -3, 3, -3, 3, grade=False, rotulos=False, size=30, d=0.5)
    E.curva(c, t, t0 + 0.3, Q, fn, -3, 3, d=d, largura=8, cor=cor)
    return Q


def tabela2(c, t, t0, linhas, x, y, cab=("x (km)", "f(x) (R$)"), wc=230, hl=92, size=60, tl=None):
    a = ep(t, t0, 0.5)
    n = len(linhas)
    if a > 0:
        centro(c, cab[0], x + wc / 2, y - 24, 46, "b", ENT, a)
        centro(c, cab[1], x + wc * 1.5, y - 24, 46, "b", SAI, a)
        M.line(c, x, y, x + 2 * wc, y, TINTA, a, 4)
        M.line(c, x + wc, y, x + wc, y + hl * n + 10, TINTA, a, 4)
    for i, (e, s) in enumerate(linhas):
        ry = y + 10 + hl * i
        ti = tl[i] if tl else t0 + 0.3 + 0.15 * i
        E.foco(c, t, ti, 0.4, lambda q, e=e, s=s, ry=ry: (
            centro(c, E._num(e), x + wc / 2, ry + hl / 2 + size * 0.36, size, "g", ENT, q),
            centro(c, E._num(s), x + wc * 1.5, ry + hl / 2 + size * 0.36, size, "g", SAI, q)), sobe=6)


def salto_tab(c, t, t0, x, y0, y1, rot, cor=CERTO, d=0.5):
    q = ease_out(prog(t, t0, d))
    if q > 0:
        r = (y1 - y0) / 2
        E.arco(c, x, (y0 + y1) / 2, r, -90, 180 * q, cor, 6)
        if q > 0.95:
            M.arrow(c, x + 4, y1 - 2, x - 4, y1, cor, 1.0, 6, 18)
        E.foco(c, t, t0 + 0.3, 0.3, lambda a: E.escreve(c, rot, x + r + 14, (y0 + y1) / 2 + 18, 46, "g", cor, a))


LEI = [("f(", SAI), ("x", ENT), (") = ", SAI), ("40", TINTA), (" + ", TINTA), ("0,5", TINTA), ("x", ENT)]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        E.frase(c, t, C["s01"], [("uma", "i", 72), ("locadora", "g", 72), ("de", "i", 72), ("carros", "i", 72)], W / 2, 220, "center")
        cs = mista_em(c, t, C["s01.a"], LEI, W / 2, 500, 150, "center")
        (c40, w40), (c05, w05) = cs[3], cs[5]
        caixa_em(c, t, C["s01.b"], c40, w40, 500, 150, COR)
        E.foco(c, t, C["s01.b"] + 0.2, 0.4, lambda a: (M.arrow(c, c40, 640, c40, 560, COR, a, 6, 22),
                                                      centro(c, "antes de rodar", c40, 700, 52, "b", COR, a)))
        caixa_em(c, t, C["s01.c"], c05, w05, 500, 150, COR)
        E.foco(c, t, C["s01.c"] + 0.2, 0.4, lambda a: (M.arrow(c, c05, 640, c05, 560, COR, a, 6, 22),
                                                      centro(c, "cada km", c05, 700, 52, "b", COR, a)))
        E.frase(c, t, C["s01.d"], [("contam", "i", 76), ("a", "i", 76), ("história", "g", 76, COR), ("inteira", "i", 76)], W / 2, 900, "center")
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.4, [("ler", "i", 90), ("o", "i", 90), ("a", "g", 110, COR), ("e", "i", 90), ("o", "i", 90), ("b", "g", 110, COR)], XE, 450)
        E.frase(c, t, C["s02.b"], [("quanto", "i", 80), ("a", "i", 80), ("reta", "g", 84), ("sobe", "g", 84, COR)], XE, 610)
        E.frase(c, t, C["s02.b"] + 1.0, ps("a cada passo", "i", 72), XE, 720)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "função afim:", lambda a, y: mista(c, [("f(", SAI), ("x", ENT), (") = a", SAI), ("x", ENT), (" + b", SAI)], x + 44, y, 66, a)),
             ("s03.c", "taxa: \"por\" = dividido", lambda a, y: E.formula(c, "R$ por km = f{R$}{km}", x + 44, y + 10, 56, "g", COR, a)))
    for i, (k, l1, fn) in enumerate(itens):
        y = 250 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 90)
        E.foco(c, t, C[k] + 0.4, 0.5, lambda a, fn=fn, y=y: fn(a, y + 190))
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(460, 760, q), ep(t, C["s03.b"], 0.4))


# ---------------- valor inicial ----------------
PL = E.Plano(1120, 230, 680, 640, -4, 42, -4, 65)
LX, LY = [0, 10, 20, 30, 40], [0, 20, 40, 60]


def b_inicial(c, t, C, b):
    cs = mista_em(c, t, C["s04"], LEI, XE, 200, 96)
    E.frase(c, t, C["s04"] + 1.0, [("x", "g", 50, ENT), ("=", "g", 48), ("km", "i", 48), ("·", "g", 48, TINTA2), ("f(x)", "g", 50), ("=", "g", 48),
                                   ("preço", "i", 48), ("(R$)", "i", 46, TINTA2)], XE, 290)
    eixos(c, t, PL, C["s04"] + 0.6, LX, LY, "km", "R$")
    E.curva(c, t, C["s04"] + 1.6, PL, loc, 0, 42, d=1.0)

    def s04():
        E.frase(c, t, C["s04.a"], [("sem", "i", 66), ("rodar:", "i", 66), ("x", "g", 70, ENT), ("=", "g", 70), ("0", "g", 70, ENT)], XE, 450)
        fml(c, t, C["s04.b"], "0,5 · 0 = 0", XE, 580, 76)
        E.frase(c, t, C["s04.c"], [("sobram", "i", 70), ("R$", "g", 80), ("40", "g", 90)], XE, 730)
    E.saida(c, t, C["s05"] - 0.1, s04)
    (c40, w40) = cs[3]
    E.ponto(c, t, C["s04.c"], PL, 0, 40, cor=SAI, r=17)
    marca_y(c, t, C["s04.c"] + 0.2, PL, 40)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05.a"], [("valor", "g", 76, COR), ("inicial", "g", 76, COR)], XE, 450)
    E.frase(c, t, C["s05.a"] + 1.0, [("o", "i", 58), ("y", "g", 62), ("quando", "i", 58), ("x", "g", 62, ENT), ("=", "g", 60), ("0", "g", 62, ENT)], XE, 540)
    caixa_em(c, t, C["s05.b"], c40, w40, 200, 96, COR)
    E.frase(c, t, C["s05.b"], [("na", "i", 58), ("fórmula:", "i", 58), ("o", "i", 58), ("b", "g", 66, COR)], XE, 660)
    E.frase(c, t, C["s05.c"], [("no", "i", 58), ("gráfico:", "i", 58), ("corta", "g", 60), ("o", "i", 58), ("eixo", "i", 58), ("y", "g", 62)], XE, 760)
    q = ease_out(prog(t, C["s05.c"], 0.5))
    if q > 0:
        E.arco(c, *PL(0, 40), 26, -90, 360 * q, COR, 6)
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.pilula(c, "coeficiente linear", XE + 270, 880, 46, "g", fundo=TINTA2, a=a))


# ---------------- taxa de variação ----------------
TBX, TBY = 220, 330


def b_taxa(c, t, C, b):
    cs = mista(c, LEI, XE, 200, 96, ep(t, C["s06"] - 2, 0.3))
    (c05, w05) = cs[5]

    def s06():
        linhas = [(0, "40"), (1, "40,50"), (2, "41"), (3, "41,50")]
        tabela2(c, t, C["s06"], linhas, TBX, TBY, tl=[C["s06"] + 0.3, C["s06.a"], C["s06.b"], C["s06.c"]])
        for i in range(3):
            y0 = TBY + 10 + 92 * i + 46
            salto_tab(c, t, C["s06.d"] + 0.3 * i, TBX + 2 * 230 + 30, y0, y0 + 92, "+0,50")
        E.frase(c, t, C["s06.d"], [("sobe", "i", 66), ("R$", "g", 70, CERTO), ("0,50", "g", 70, CERTO)], 1100, 520)
        E.frase(c, t, C["s06.d"] + 0.6, [("a", "i", 66), ("cada", "i", 66), ("km", "g", 66, ENT)], 1100, 620)
        caixa_em(c, t, C["s06.d"] + 1.6, c05, w05, 200, 96, COR)
        E.foco(c, t, C["s06.d"] + 2.0, 0.4, lambda a: E.pilula(c, "é o a", 1240, 760, 56, "g", fundo=COR, a=a))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    caixa_em(c, t, C["s07"] - 2, c05, w05, 200, 96, COR)
    E.frase(c, t, C["s07.a"], [("a", "g", 76, COR), ("=", "g", 72), ("0,5", "g", 76), ("real", "i", 70), ("por", "g", 70, COR), ("km", "i", 70)], XE, 380)
    E.frase(c, t, C["s07.b"], [("quanto", "i", 62), ("o", "i", 62), ("y", "g", 66), ("muda", "g", 64), ("quando", "i", 62), ("o", "i", 62), ("x", "g", 66, ENT),
                               ("anda", "i", 62), ("1", "g", 66, ENT)], XE, 520)
    E.frase(c, t, C["s07.c"], [("taxa", "g", 100, COR), ("de", "i", 90), ("variação", "g", 100, COR)], XE, 720)
    E.foco(c, t, C["s07.d"], 0.4, lambda a: E.pilula(c, "coeficiente angular", XE + 290, 860, 46, "g", fundo=TINTA2, a=a))


# ---------------- delta ----------------
A_, B_ = (10, 45), (30, 55)


def b_delta(c, t, C, b):
    eixos(c, t, PL, C["s08"], LX, LY, "km", "R$")
    E.ponto(c, t, C["s08.b"], PL, *A_, cor=COR, r=16)
    E.foco(c, t, C["s08.b"] + 0.3, 0.4, lambda a: par(c, "10", "45", PL.x(10) - 60, PL.y(45) - 40, 40, a))
    E.ponto(c, t, C["s08.c"], PL, *B_, cor=COR, r=16)
    E.foco(c, t, C["s08.c"] + 0.3, 0.4, lambda a: par(c, "30", "55", PL.x(30) - 60, PL.y(55) - 40, 40, a))

    def s08():
        E.frase(c, t, C["s08.a"], [("só", "i", 72), ("2", "g", 80, COR), ("pontos,", "g", 72, COR), ("sem", "i", 72), ("fórmula", "i", 72)], XE, 300)
        E.frase(c, t, C["s08.b"], [("10", "g", 66, ENT), ("km:", "i", 62), ("R$", "g", 66), ("45", "g", 66)], XE, 460)
        E.frase(c, t, C["s08.c"], [("30", "g", 66, ENT), ("km:", "i", 62), ("R$", "g", 66), ("55", "g", 66)], XE, 570)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    degrau(c, t, C["s09.d"], C["s09.c"], PL, A_, B_, "Δx = 20", "Δy = 10")

    def s09():
        E.foco(c, t, C["s09.a"], 0.5, lambda a: E.escreve(c, "Δ", XE, 330, 160, "g", COR, a))
        E.frase(c, t, C["s09.a"] + 0.2, [("delta", "i", 80)], XE + 150, 310)
        E.frase(c, t, C["s09.b"], [("variação:", "g", 60), ("final", "i", 60), ("−", "g", 60), ("inicial", "i", 60)], XE, 440)
        fml(c, t, C["s09.c"], "Δy = 55 − 45 = 10", XE, 600, 76)
        fml(c, t, C["s09.d"], "Δx = 30 − 10 = 20", XE, 740, 76, ENT)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("taxa:", "g", 66), ("reais", "i", 66), ("por", "g", 66, COR), ("km", "i", 66)], XE, 300)
    fml(c, t, C["s10.b"], "a = f{Δy}{Δx}", XE, 500, 110)
    fml(c, t, C["s10.c"], "f{10}{20} = 0,5", XE + 420, 500, 100, COR)
    if t >= C["s10.d"]:
        E.reta_pontos(c, t, C["s10.d"], PL, A_, B_, pontos=False)
    E.foco(c, t, C["s10.d"], 0.4, lambda a: (mista(c, LEI, XE, 760, 76, a), E.selo(c, XE + 760, 735, 36, True, a)))
    E.frase(c, t, C["s10.d"] + 0.6, [("o", "i", 56), ("mesmo", "g", 58, CERTO), ("número", "i", 56)], XE, 860)


# ---------------- sobe, desce, constante ----------------
MINIS = ((280, lambda v: 0.6 * v + 0.5, CERTO, "sobe", "a > 0"), (800, lambda v: -0.9 * v + 0.6, ERRADO, "desce", "a < 0"),
         (1320, lambda v: 1.2, TINTA2, "horizontal", "a = 0"))


def b_sinal(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("o", "i", 70), ("sinal", "g", 74), ("do", "i", 70), ("a:", "g", 74, COR), ("para", "i", 70), ("onde", "i", 70), ("vai", "g", 74)],
            W / 2, 180, "center")
    tm = (C["s11.b"], C["s11.c"], C["s12.d"])
    for (x, fn, cor, nome, regra), t0 in zip(MINIS, tm):
        mini(c, t, t0, x, 300, 360, 340, fn, cor)
        E.foco(c, t, t0 + 0.4, 0.4, lambda a, x=x, nome=nome, cor=cor, regra=regra: (
            centro(c, regra, x + 180, 720, 62, "g", cor, a), centro(c, nome, x + 180, 790, 50, "i", TINTA, a)))
    E.foco(c, t, C["s11.b"] + 1.2, 0.4, lambda a: centro(c, "locadora", 280 + 180, 880, 44, "b", TINTA2, a))
    fml(c, t, C["s11.d"], "100 − 5x", 800 + 180, 880, 56, None, "center")
    E.foco(c, t, C["s11.e"], 0.4, lambda a: centro(c, "a = −5: −5 por hora", 800 + 180, 960, 44, "b", ERRADO, a))
    E.frase(c, t, C["s12.a"], [("a", "g", 56, COR), ("=", "g", 56), ("0?", "g", 56)], 1320 + 120, 880)
    E.foco(c, t, C["s12.b"], 0.4, lambda a: centro(c, "assinatura de R$ 30", 1320 + 180, 960, 44, "b", TINTA2, a))
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.formula(c, "f(x) = 30", 1320 + 180, 1030, 50, "g", TINTA, a, "center"))
    E.foco(c, t, C["s12.d"] + 0.8, 0.4, lambda a: E.pilula(c, "constante", 1320 + 180, 270, 40, "g", fundo=TINTA2, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13.a"], [("o", "i", 66), ("a", "g", 70, ERRADO), ("é", "i", 66), ("o", "i", 66), ("primeiro", "g", 70, ERRADO), ("número?", "g", 70, ERRADO)],
            XE, 220)
    cs = mista_em(c, t, C["s13.a"] + 0.6, [("f(", SAI), ("x", ENT), (") = ", SAI), ("40", TINTA), (" + ", TINTA), ("0,5", TINTA), ("x", ENT)], XE, 420, 110)
    (c40, w40), (c05, w05) = cs[3], cs[5]
    if t >= C["s13.b"]:
        E.risco(c, c40 - w40 / 2 - 10, 440, c40 + w40 / 2 + 10, 340, t, C["s13.b"], largura=9)
        E.foco(c, t, C["s13.b"] + 0.3, 0.4, lambda a: centro(c, "a ≠ 40", c40, 530, 56, "g", ERRADO, a))
    fml(c, t, C["s13.c"], "40 · 10 + 0,5 = 400,50", XE, 700, 72, ERRADO)
    E.frase(c, t, C["s13.c"] + 1.6, [("e", "i", 62), ("não", "i", 62), ("R$", "g", 66, CERTO), ("45", "g", 66, CERTO)], XE + 1000, 700)
    caixa_em(c, t, C["s13.d"], c05 + E.larg("x", "g", 110) / 2, w05 + E.larg("x", "g", 110), 420, 110, CERTO)
    E.foco(c, t, C["s13.d"] + 0.3, 0.4, lambda a: centro(c, "a = 0,5: colado no x", c05 + 60, 610, 56, "g", CERTO, a))
    E.frase(c, t, C["s13.d"] + 1.0, [("em", "i", 58), ("qualquer", "i", 58), ("posição:", "i", 58)], XE, 880)
    E.foco(c, t, C["s13.d"] + 1.6, 0.4, lambda a: mista(c, [("0,5", CERTO), ("x", ENT), (" + 40", TINTA)], XE + 560, 880, 72, a))


# ---------------- atalho (palco escuro) ----------------
PG = E.Plano(1120, 220, 640, 640, -0.6, 5.6, -0.6, 6.6)
GX = list(range(0, 6))


def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 66, CLARO), XE, 180)
        E.frase(c, t, C["s14.a"], [("quanto", "i", 76, CLARO), ("sobe", "g", 80, BR)], XE, 320)
        E.frase(c, t, C["s14.a"] + 0.8, [("÷", "g", 80, AMAR), ("quanto", "i", 76, CLARO), ("anda", "g", 80, CLARO)], XE, 430)
        eixos(c, t, PG, C["s14"], GX, GX, escuro=True)
        sai = 1 - ep(t, C["s14.d"] - 0.2, 0.4)
        if sai > 0:
            def subida():
                E.ponto(c, t, C["s14"] + 0.8, PG, 1, 1, cor=BR, r=15)
                E.ponto(c, t, C["s14"] + 1.0, PG, 3, 5, cor=BR, r=15)
                degrau(c, t, C["s14.b"], C["s14.c"], PG, (1, 1), (3, 5), "anda 2", "sobe 4", cx=CLARO, escuro=True)
                E.foco(c, t, C["s14.c"] + 1.2, 0.4, lambda a: E.formula(c, "a = f{4}{2} = 2", XE, 640, 84, "g", BR, a))
            E.saida(c, t, C["s14.d"] - 0.2, subida)
        if t >= C["s14.d"]:
            E.ponto(c, t, C["s14.d"], PG, 1, 5, cor=BR, r=15)
            E.ponto(c, t, C["s14.d"] + 0.2, PG, 3, 1, cor=BR, r=15)
            degrau(c, t, C["s14.d"] + 0.5, C["s14.d"] + 1.2, PG, (1, 5), (3, 1), "anda 2", "desce 4", cx=CLARO, escuro=True)
            E.foco(c, t, C["s14.d"] + 2.0, 0.4, lambda a: E.formula(c, "a = f{−4}{2} = −2", XE, 640, 84, "g", ERRADO, a))
            E.frase(c, t, C["s14.d"], [("desce:", "g", 60, ERRADO), ("subida", "i", 58, CLARO), ("negativa", "g", 60, BR)], XE, 820)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], [("subida", "i", 64, CLARO), ("=", "g", 64, BR), ("Δy", "g", 70, BR), ("·", "g", 64, CLARO), ("andada", "i", 64, CLARO), ("=", "g", 64, BR),
                               ("Δx", "g", 70, CLARO)], XE, 210)
    E.frase(c, t, C["s15.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 60, CLARO), ("escalas", "g", 62, BR), ("diferentes", "g", 62, BR)], XE, 360)
    PS = E.Plano(1120, 300, 640, 520, -4, 52, -0.4, 5.6)
    if t >= C["s15.c"] - 0.4:
        eixos(c, t, PS, C["s15.c"] - 0.4, [0, 10, 20, 30, 40, 50], [0, 1, 2, 3, 4, 5], escuro=True)
        E.foco(c, t, C["s15.c"] + 0.4, 0.4, lambda a: (E.pilula(c, "1 quadradinho = 10", PS.x(25), PS.oy + 110, 40, "g", fundo=COR, a=a),
                                                      E.pilula(c, "1 quadradinho = 1", PS.ox + 210, PS.y(5.4), 40, "g", fundo=TINTA2, a=a)))
    E.frase(c, t, C["s15.c"], [("10", "g", 60, CLARO), ("no", "i", 58, CLARO), ("x,", "g", 60, CLARO), ("1", "g", 60, BR), ("no", "i", 58, CLARO), ("y", "g", 60, BR)], XE, 470)
    E.frase(c, t, C["s15.d"], [("leia", "g", 66, AMAR), ("os", "i", 64, CLARO), ("valores", "i", 64, CLARO), ("nos", "i", 64, CLARO), ("eixos", "g", 66, BR)], XE, 640)
    E.frase(c, t, C["s15.d"] + 0.8, [("e", "i", 64, CLARO), ("faça", "i", 64, CLARO), ("a", "i", 64, CLARO), ("conta", "g", 66, BR)], XE, 740)


# ---------------- questão ----------------
LEI_V = [("f(", SAI), ("x", ENT), (") = ", SAI), ("20", TINTA), (" − ", TINTA), ("2", TINTA), ("x", ENT)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 64, COR), XE, 160)
    E.frase(c, t, C["s16"] + 0.6, [("altura", "g", 64), ("de", "i", 62), ("uma", "i", 62), ("vela", "g", 64, COR), ("(cm)", "i", 56, TINTA2)], XE, 260)
    mista_em(c, t, C["s16.a"], LEI_V, XE, 400, 100)
    E.frase(c, t, C["s16.a"] + 1.0, [("x", "g", 52, ENT), ("=", "g", 50), ("horas", "i", 50)], XE + 760, 390)
    perguntas = (("s16.b", "1", [("altura", "i", 56), ("antes", "g", 58), ("de", "i", 56), ("acender?", "i", 56)]),
                 ("s16.c", "2", [("muda", "i", 56), ("quanto", "g", 58), ("por", "i", 56), ("hora?", "i", 56)]),
                 ("s16.d", "3", [("sobe", "g", 58, CERTO), ("ou", "i", 56), ("desce?", "g", 58, ERRADO)]),
                 ("s16.e", "4", [("confira", "g", 58), ("o", "i", 56), ("a:", "g", 58, COR), ("x", "g", 58, ENT), ("=", "g", 56), ("1", "g", 58, ENT),
                                 ("e", "i", 56), ("x", "g", 58, ENT), ("=", "g", 56), ("4", "g", 58, ENT)]))
    for i, (k, n, partes) in enumerate(perguntas):
        yy = 540 + i * 110
        E.foco(c, t, C[k], 0.5, lambda a, n=n, yy=yy: (E.bola(c, XE + 34, yy - 20, 34, a=a), centro(c, n, XE + 34, yy - 4, 44, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, XE + 100, yy)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1500, cy=470, r=150)


# ---------------- resposta ----------------
PV = E.Plano(1120, 220, 660, 640, -0.6, 10.6, -1.5, 22.5)
VX, VY = [0, 2, 4, 6, 8, 10], [0, 4, 8, 12, 16, 20]


def b_resposta(c, t, C, b):
    cs = mista(c, LEI_V, XE, 190, 84, ep(t, C["s18"] - 2, 0.3))
    (c20, w20), (c2, w2) = cs[3], cs[5]
    eixos(c, t, PV, C["s18"] - 1.6, VX, VY, "horas", "cm")
    E.curva(c, t, C["s18.d"], PV, vela, 0, 10, d=1.0, cor=ERRADO)

    def s18():
        caixa_em(c, t, C["s18.a"], c20, w20, 190, 84, COR)
        E.frase(c, t, C["s18.a"], [("inicial:", "i", 60), ("b", "g", 66, COR), ("=", "g", 62), ("20", "g", 66), ("cm", "i", 58)], XE, 360)
        caixa_em(c, t, C["s18.b"], (c2 - w2 / 2 - E.larg(" − ", "g", 84) + c2 + w2 / 2 + E.larg("x", "g", 84)) / 2,
                 w2 + E.larg(" − ", "g", 84) + E.larg("x", "g", 84), 190, 84, COR)
        E.frase(c, t, C["s18.b"], [("a", "g", 66, COR), ("=", "g", 62), ("−2", "g", 66), ("(colado", "i", 56), ("no", "i", 56), ("x)", "g", 58, ENT)], XE, 480)
        E.frase(c, t, C["s18.c"], [("perde", "g", 62, ERRADO), ("2", "g", 64), ("cm", "i", 58), ("por", "i", 58), ("hora", "i", 58)], XE, 600)
        E.frase(c, t, C["s18.d"], [("a", "g", 66, COR), ("<", "g", 66), ("0:", "g", 66), ("a", "i", 62), ("reta", "i", 62), ("desce", "g", 66, ERRADO)], XE, 740)
        E.ponto(c, t, C["s18.a"], PV, 0, 20, cor=SAI, r=15)
        marca_y(c, t, C["s18.a"] + 0.2, PV, 20)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    for k, xv in (("s19.a", 1), ("s19.b", 4)):
        E.ponto(c, t, C[k], PV, xv, vela(xv), cor=COR, r=16)
        if xv == 4:
            E.foco(c, t, C[k] + 0.3, 0.4, lambda a, xv=xv: par(c, E._num(xv), E._num(vela(xv)), PV.x(xv) - 30, PV.y(vela(xv)) + 62, 40, a, "right"))

    fml(c, t, C["s19.a"], "x = 1:  20 − 2 = 18", XE, 340, 64)
    fml(c, t, C["s19.b"], "x = 4:  20 − 8 = 12", XE, 450, 64)
    degrau(c, t, C["s19.d"], C["s19.c"], PV, (1, 18), (4, 12), "Δx = 3", "Δy = −6")
    fml(c, t, C["s19.c"], "Δy = 12 − 18 = −6", XE, 600, 64, ERRADO)
    fml(c, t, C["s19.d"], "Δx = 4 − 1 = 3", XE, 710, 64, ENT)
    fml(c, t, C["s19.e"], "a = f{−6}{3} = −2", XE, 880, 84)
    E.foco(c, t, C["s19.e"] + 0.8, 0.4, lambda a: E.selo(c, XE + 640, 850, 38, True, a))


# ---------------- fechamento ----------------
PN = E.Plano(1180, 420, 560, 440, -3, 4, -3, 4)


def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", [("b:", "g", 80, COR), ("de", "i", 76), ("onde", "i", 76), ("a", "i", 76), ("reta", "i", 76), ("parte", "g", 80)]),
                 ("s20.b", [("a:", "g", 80, COR), ("quanto", "i", 76), ("sobe", "g", 80), ("a", "i", 76), ("cada", "i", 76), ("passo", "i", 76)]),
                 ("s20.c", [("sinal", "g", 80), ("do", "i", 76), ("a:", "g", 80, COR), ("sobe,", "g", 76, CERTO), ("desce", "g", 76, ERRADO), ("ou", "i", 76),
                            ("parada", "g", 76, TINTA2)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 28, 52, a=a),
                                                         E.escreve(c, str(i + 1), 230 - E.larg(str(i + 1), "g", 60) / 2, y - 6, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 320, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s21.a"], [("onde", "i", 76), ("a", "i", 76), ("reta", "g", 80), ("corta", "g", 80, COR)], XE, 410)
    E.frase(c, t, C["s21.a"] + 0.6, [("o", "i", 76), ("eixo", "i", 76), ("x", "g", 84, ENT)], XE, 510)
    E.frase(c, t, C["s21.b"], [("positiva", "g", 66, CERTO), ("ou", "i", 62), ("negativa", "g", 66, ERRADO)], XE, 660)
    if t >= C["s21.a"]:
        E.plano(c, t, C["s21.a"], *PN.caixa, PN.xmin, PN.xmax, PN.ymin, PN.ymax, grade=False, rotulos=False, size=30, d=0.5)
        g = lambda v: v - 1
        E.area(c, t, C["s21.b"], PN, g, -3, 1, cor=ERRADO, alfa=0.2)
        E.area(c, t, C["s21.b"] + 0.4, PN, g, 1, 4, cor=CERTO, alfa=0.2)
        E.curva(c, t, C["s21.a"] + 0.3, PN, g, -3, 4, d=0.8)
        E.ponto(c, t, C["s21.a"] + 1.0, PN, 1, 0, cor=SAI, r=15)
        q = ease_out(prog(t, C["s21.a"] + 1.2, 0.5))
        if q > 0:
            E.arco(c, *PN(1, 0), 30, -90, 360 * q, SAI, 6)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 260, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(520, 285, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, inicial=b_inicial, taxa=b_taxa, delta=b_delta, sinal=b_sinal, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
