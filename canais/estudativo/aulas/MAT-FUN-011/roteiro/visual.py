"""Visual — Estudativo · MAT-FUN-011: zero da função afim e estudo do sinal.

Linguagem visual da trilha Funções (MAT-FUN-001 a 010): entrada / x em índigo (ENT), saída / y em preto (SAI); eixo x índigo, eixo y preto;
par (x, y) com o x índigo e o y preto; plano na metade direita e texto à esquerda; o zero (raiz) = anel preto no ponto em que a reta toca o
eixo x (MAT-FUN-007).
Nesta aula: positiva = região entre a reta e o eixo pintada de verde (E.area), negativa = de vermelho; o quadro de sinais (sinais()) é uma
reta deitada com a raiz no meio, bolinha "−" vermelha e "+" verde de cada lado e o trecho da reta na mesma cor.
Contas da equação e da inequação passo a passo à esquerda, com pílula cinza da operação (MAT-FUN-008); "vira o sinal" em vermelho.
Palco escuro só no atalho. Peças locais: mista(), eixos(), par(), marca(), anel(), sinais(), mini(), resultado(), op()."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FUN-011_zero_da_funcao_e_estudo_do_sinal.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("zero", "sinal", "desce", "atalho", "questao", "fim"))
BR = "#FFFFFF"
POS, NEG = CERTO, ERRADO

f = lambda x: 2 * x - 6
g = lambda x: -3 * x + 12
h = lambda x: -4 * x + 10
assert f(3) == 0 and (f(1), f(5), f(4)) == (-4, 4, 2)
assert g(4) == 0 and g(5) == -3 and -3 * 5 == -15 and -12 / -3 == 4
assert h(2.5) == 0 and h(0) == 10 and -10 / -4 == 2.5


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


def lei(nome, corpo):
    """'f', [('2', 'x'), ...] → partes de mista com o x em índigo"""
    partes = [(nome + "(", SAI), ("x", ENT), (") = ", SAI)]
    for p in corpo:
        partes.append((p, ENT) if p == "x" else (p, TINTA))
    return partes


LF = lei("f", ["2", "x", " − 6"])
LG = lei("g", ["−3", "x", " + 12"])
LH = lei("h", ["−4", "x", " + 10"])


def op(c, t, t0, s, x, y, cor=TINTA2, size=40):
    """pílula da operação feita nos dois lados"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, x, y, size, "g", fundo=cor, a=a))


def par(c, xv, yv, x, y, size, a=1.0, align="left", est="g"):
    partes = (("(", TINTA), (xv, ENT), (", ", TINTA), (yv, SAI), (")", TINTA))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def eixos(c, t, P, t0, mx, my, nx="x", ny="y", size=36, escuro=False, grade=True):
    """plano em etapas (MAT-FUN-001/006/007): grade, eixo x índigo, eixo y preto (claros no palco)"""
    x, y, w, h_ = P.caixa
    if t < t0:
        return
    cx_, cy_, tt = (CLARO, BR, CLARO) if escuro else (ENT, SAI, TINTA2)
    q = ep(t, t0, 0.8)
    if grade:
        for v in mx:
            M.line(c, P.x(v), y, P.x(v), y + h_, CLARO if escuro else FIO, q * (0.2 if escuro else 1), 2)
        for v in my:
            M.line(c, x, P.y(v), x + w, P.y(v), CLARO if escuro else FIO, q * (0.2 if escuro else 1), 2)
    M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, cx_, 1.0, 6, 24, ep(t, t0, 0.7))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.escreve(c, nx, x + w + 10 - E.larg(nx, "i", 46), P.oy - 22, 46, "i", cx_, a))
    for i, v in enumerate(mx):
        if v == 0:
            continue
        X = P.x(v)
        E.foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
            M.line(c, X, P.oy - 10, X, P.oy + 10, cx_, a, 4),
            centro(c, E._num(v), X, P.oy + 14 + size, size, "b", tt, a)), sobe=6)
    M.arrow(c, P.ox, y + h_ + 10, P.ox, y - 44, cy_, 1.0, 6, 24, ep(t, t0, 0.7))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.escreve(c, ny, P.ox + 22, y - 16, 46, "i", cy_, a))
    for i, v in enumerate(my):
        if v == 0:
            continue
        Y = P.y(v)
        E.foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
            M.line(c, P.ox - 10, Y, P.ox + 10, Y, cy_, a, 4),
            E.escreve(c, E._num(v), P.ox - 20 - E.larg(E._num(v), "b", size), Y + size * 0.36, size, "b", tt, a)), sobe=6)


def anel(c, t, t0, P, xv, yv, cor=SAI, r=26, largura=6):
    q = ease_out(prog(t, t0, 0.5))
    if q > 0:
        E.arco(c, *P(xv, yv), r, -90, 360 * q, cor, largura)


def raiz(c, t, t0, P, xv, rot=None, lado=1):
    """o zero: ponto preto em cima do eixo x, anel e o valor numa pílula índigo logo abaixo"""
    E.ponto(c, t, t0, P, xv, 0, cor=SAI, r=14)
    anel(c, t, t0 + 0.2, P, xv, 0, SAI, 28)
    s = rot or E._num(xv)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.pilula(c, s, P.x(xv) + lado * 6, P.oy + 112, 40, "g", fundo=ENT, a=a), sobe=0)


def sinais(c, t, t0, x0, x1, y, zero, esq, dir_, te, td, escuro=False, size=46):
    """quadro de sinais: reta deitada com a raiz no meio; esq/dir_ = "+" ou "−", que entram em te/td"""
    tinta = BR if escuro else TINTA
    a = ep(t, t0, 0.5)
    if a <= 0:
        return
    xm = (x0 + x1) / 2
    M.arrow(c, x0, y, x1 + 30, y, CLARO if escuro else ENT, a, 5, 20)
    for sgn, tt, xa, xb in ((esq, te, x0, xm), (dir_, td, xm, x1)):
        if tt is None:
            continue
        cor = POS if sgn == "+" else NEG
        p = ease_io(prog(t, tt, 0.6))
        if p > 0:
            M.line(c, xa, y, lerp(xa, xb, p) if xa == x0 else lerp(xa, xb, p), y, cor, 1.0, 12)
            k = ease_back(prog(t, tt + 0.2, 0.4))
            if k > 0:
                E.bola(c, (xa + xb) / 2, y - 70, 38 * k, cor)
                centro(c, sgn, (xa + xb) / 2, y - 70 + 22 * k, 64 * k, "g", BR, 1.0)
    c.drawCircle(xm, y, 15, M.paint(tinta, a))
    E.foco(c, t, t0 + 0.2, 0.4, lambda q: centro(c, zero, xm, y + 70, size, "g", CLARO if escuro else ENT, q))


def mini(c, t, t0, x, y, w, h_, fn, cor=None, d=0.7, escuro=False):
    Q = E.plano(c, t, t0, x, y, w, h_, -3, 3, -3, 3, grade=False, rotulos=False, size=30, d=0.5, escuro=escuro)
    E.curva(c, t, t0 + 0.3, Q, fn, -3, 3, d=d, largura=8, cor=cor)
    return Q


def resultado(c, t, t0, s, cx, cy, r=110):
    k = ease_back(prog(t, t0, 0.6))
    if k > 0:
        E.bola(c, cx, cy, r * k)
        size = r * (0.62 if len(s) <= 4 else 0.5 if len(s) <= 6 else 0.4)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", BR, a), sobe=0)


def area_sinal(c, t, t0, P, fn, a_, b_, pos, d=0.8):
    E.area(c, t, t0, P, fn, a_, b_, cor=POS if pos else NEG, alfa=0.22, d=d)


# ---------------- gancho ----------------
PB = E.Plano(1180, 260, 600, 600, -1, 7, -7, 9)


def b_gancho(c, t, C, b):
    def cena1():
        E.frase(c, t, C["s01.a"], [("gastou", "i", 70), ("R$", "g", 76, NEG), ("6", "g", 76, NEG), ("de", "i", 70), ("material", "i", 70)], XE, 260)
        E.frase(c, t, C["s01.b"], [("+", "g", 76, POS), ("R$", "g", 76, POS), ("2", "g", 76, POS), ("por", "i", 70), ("brigadeiro", "g", 70)], XE, 380)
        E.frase(c, t, C["s01.c"], [("empata", "g", 70), ("com", "i", 66), ("quantos?", "i", 66)], XE, 560)
        E.frase(c, t, C["s01.d"], [("positivo", "g", 70, POS), ("a", "i", 66), ("partir", "i", 66), ("de", "i", 66), ("quantos?", "i", 66)], XE, 680)
        if t >= C["s01.e"] - 0.6:
            E.plano(c, t, C["s01.e"] - 0.6, *PB.caixa, PB.xmin, PB.xmax, PB.ymin, PB.ymax, grade=False, rotulos=False, size=30, d=0.5)
            E.curva(c, t, C["s01.e"] - 0.3, PB, f, -1, 7, d=0.8)
            anel(c, t, C["s01.e"] + 0.4, PB, 3, 0, COR, 34)
            E.ponto(c, t, C["s01.e"] + 0.4, PB, 3, 0, cor=SAI, r=15)
        E.frase(c, t, C["s01.e"], [("um", "i", 76), ("ponto", "g", 80, COR), ("só", "i", 76)], XE, 860)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.4, [("onde", "i", 84), ("a", "i", 84), ("reta", "g", 90), ("corta", "g", 90, COR)], XE, 450)
        E.frase(c, t, C["s02.b"], [("positiva", "g", 84, POS), ("ou", "i", 80)], XE, 610)
        E.frase(c, t, C["s02.b"] + 0.6, [("negativa", "g", 84, NEG)], XE, 730)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "o a: sobe ou desce", lambda a, y: (E.escreve(c, "a > 0", x + 44, y, 66, "g", POS, a), E.escreve(c, "a < 0", x + 330, y, 66, "g", NEG, a))),
             ("s03.c", "÷ negativo vira o sinal", lambda a, y: E.formula(c, "−2x < 6 → x > −3", x + 44, y, 62, "g", COR, a)))
    for i, (k, l1, fn) in enumerate(itens):
        y = 250 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 90)
        E.foco(c, t, C[k] + 0.4, 0.5, lambda a, fn=fn, y=y: fn(a, y + 190))
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(460, 760, q), ep(t, C["s03.b"], 0.4))


# ---------------- zero ----------------
PF = E.Plano(1120, 200, 660, 680, -1.5, 7.5, -8.5, 8.5)
FX, FY = list(range(-1, 8)), list(range(-8, 9, 2))


def b_zero(c, t, C, b):
    def s04_05():
        E.foco(c, t, C["s04.a"], 0.5, lambda a: mista(c, LF, XE, 220, 110, a))
        E.frase(c, t, C["s04.a"] + 1.2, [("x", "g", 52, ENT), ("=", "g", 50), ("brigadeiros", "i", 50), ("·", "g", 50, TINTA2), ("f(x)", "g", 52), ("=", "g", 50),
                                         ("saldo", "i", 50), ("(R$)", "i", 46, TINTA2)], XE, 320)

        def s04():
            E.frase(c, t, C["s04.b"], [("empatar", "g", 70), ("=", "g", 70), ("saldo", "i", 70), ("zero", "g", 74, COR)], XE, 500)
            fml(c, t, C["s04.c"], "f(x) = 0 ?", XE, 680, 110, COR)
        E.saida(c, t, C["s05"] - 0.1, s04)
        if t >= C["s05"]:
            fml(c, t, C["s05.a"], "2x − 6 = 0", XE, 490, 96)
            fml(c, t, C["s05.b"], "2x = 6", XE + 90, 630, 96)
            op(c, t, C["s05.b"], "+6 dos dois lados", XE + 760, 600)
            fml(c, t, C["s05.c"], "x = 3", XE + 150, 770, 96, ENT)
            op(c, t, C["s05.c"], "÷ 2", XE + 640, 740)
            resultado(c, t, C["s05.d"], "3", 1450, 560, 150)
            E.foco(c, t, C["s05.d"] + 0.3, 0.4, lambda a: centro(c, "brigadeiros: empata", 1450, 790, 56, "g", COR, a))
    E.saida(c, t, C["s06"] - 0.1, s04_05)
    if t < C["s06"]:
        return
    mista(c, LF, XE, 220, 90, ep(t, C["s06"], 0.3))
    eixos(c, t, PF, C["s06"], FX, FY)
    E.curva(c, t, C["s06"] + 0.4, PF, f, -1.5, 7.5, d=1.0)
    E.frase(c, t, C["s06.a"], [("zero", "g", 90, COR), ("da", "i", 84), ("função", "i", 84)], XE, 400)
    op(c, t, C["s06.b"], "também: raiz", XE + 200, 490, COR, 44)
    raiz(c, t, C["s06.c"], PF, 3)
    E.frase(c, t, C["s06.c"], [("corta", "g", 64), ("o", "i", 62), ("eixo", "i", 62), ("x", "g", 66, ENT)], XE, 640)
    E.foco(c, t, C["s06.d"], 0.4, lambda a: par(c, "3", "0", XE, 760, 80, a))
    E.foco(c, t, C["s06.d"] + 0.3, 0.4, lambda a: par(c, "3", "0", PF.x(3) + 36, PF.y(0) - 56, 40, a))
    E.frase(c, t, C["s06.d"] + 1.2, ps("nem acima nem abaixo", "i", 52, TINTA2), XE, 860, passo=0.1)


# ---------------- sinal ----------------
def b_sinal(c, t, C, b):
    eixos(c, t, PF, C["s07"] - 3, FX, FY)
    area_sinal(c, t, C["s07.b"], PF, f, 3, 7.5, True)
    area_sinal(c, t, C["s07.d"], PF, f, -1.5, 3, False)
    E.curva(c, t, C["s07"] - 3, PF, f, -1.5, 7.5, d=0.1)
    raiz(c, t, C["s07"] - 3, PF, 3)

    def s07_08():
        E.frase(c, t, C["s07.a"], [("positiva:", "g", 66, POS), ("y", "g", 70), (">", "g", 70), ("0", "g", 70)], XE, 230)
        E.frase(c, t, C["s07.b"], [("acima", "g", 60, POS), ("do", "i", 58), ("eixo", "i", 58), ("x", "g", 62, ENT)], XE, 320)
        E.frase(c, t, C["s07.c"], [("negativa:", "g", 66, NEG), ("y", "g", 70), ("<", "g", 70), ("0", "g", 70)], XE, 450)
        E.frase(c, t, C["s07.d"], [("abaixo", "g", 60, NEG), ("do", "i", 58), ("eixo", "i", 58), ("x", "g", 62, ENT)], XE, 540)
        if t >= C["s08"]:
            fml(c, t, C["s08.a"], "2x − 6 > 0", XE, 680, 76)
            fml(c, t, C["s08.b"], "2x > 6", XE + 470, 680, 76)
            fml(c, t, C["s08.c"], "x > 3", XE, 820, 90, POS)
            op(c, t, C["s08.c"], "÷ 2, positivo: o sinal fica", XE + 580, 790)
            fml(c, t, C["s08.d"], "x < 3", XE, 950, 90, NEG)
            E.foco(c, t, C["s08.d"] + 0.3, 0.4, lambda a: E.escreve(c, "negativa", XE + 280, 940, 60, "g", NEG, a))
    E.saida(c, t, C["s09"] - 0.1, s07_08)
    if t < C["s09"]:
        return
    for k, xv, txt, cor in (("s09.a", 1, "prejuízo", NEG), ("s09.b", 5, "lucro", POS)):
        E.ponto(c, t, C[k], PF, xv, f(xv), cor=cor, r=16)
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, xv=xv, cor=cor: par(c, E._num(xv), E._num(f(xv)), PF.x(xv) + 28,
                                                                     PF.y(f(xv)) + (14 if xv == 5 else 56), 40, a))
    fml(c, t, C["s09.a"], "x = 1:  2 − 6 = −4", XE, 250, 66, NEG)
    E.foco(c, t, C["s09.a"] + 1.0, 0.4, lambda a: E.escreve(c, "prejuízo", XE + 640, 250, 52, "i", NEG, a))
    fml(c, t, C["s09.b"], "x = 5:  10 − 6 = 4", XE, 370, 66, POS)
    sinais(c, t, C["s09.c"] - 0.5, XE, 900, 600, "3", "−", "+", C["s09.c"], C["s09.d"])
    E.foco(c, t, C["s09.e"], 0.4, lambda a: E.formula(c, "4º: 8 − 6 = 2", XE, 820, 72, "g", POS, a))
    E.frase(c, t, C["s09.e"] + 0.5, ps("ninguém vende meio brigadeiro", "i", 50, TINTA2), XE, 920, passo=0.1)
    E.ponto(c, t, C["s09.e"] + 0.4, PF, 4, 2, cor=POS, r=16)
    anel(c, t, C["s09.e"] + 0.6, PF, 4, 2, POS, 30)


# ---------------- reta que desce ----------------
PG = E.Plano(1120, 200, 660, 680, -1.5, 7.5, -10, 17)
GX, GY = list(range(-1, 8)), list(range(-8, 17, 4))


def b_desce(c, t, C, b):
    eixos(c, t, PG, C["s10"] + 0.3, GX, GY)
    E.curva(c, t, C["s10.a"], PG, g, -1.5, 7.5, d=1.0)
    E.foco(c, t, C["s10.a"], 0.5, lambda a: mista(c, LG, XE, 220, 96, a))

    def s10():
        E.frase(c, t, C["s10"], [("e", "i", 66), ("se", "i", 66), ("a", "i", 66), ("reta", "g", 70), ("descer?", "g", 70, NEG)], XE, 350)
        fml(c, t, C["s10.b"], "−3x + 12 = 0", XE, 500, 84)
        fml(c, t, C["s10.c"], "−3x = −12", XE + 90, 640, 84)
        op(c, t, C["s10.c"], "−12", XE + 640, 610)
        fml(c, t, C["s10.d"], "x = 4", XE + 160, 780, 90, ENT)
        op(c, t, C["s10.d"], "÷ (−3)", XE + 620, 750)
    E.saida(c, t, C["s11"] - 0.1, s10)
    raiz(c, t, C["s10.d"] + 0.3, PG, 4)
    if t < C["s11"]:
        return
    fml(c, t, C["s11.a"], "−3x + 12 > 0", XE, 360, 78)
    fml(c, t, C["s11.b"], "−3x > −12", XE + 90, 490, 78)
    op(c, t, C["s11.b"], "−12", XE + 590, 460)
    op(c, t, C["s11.c"], "÷ negativo: vira o sinal", XE + 300, 580, NEG, 44)
    fml(c, t, C["s11.d"], "x < 4", XE + 150, 720, 96, POS)
    q = ep(t, C["s11.d"], 0.3)
    if q > 0:
        E.arco(c, XE + 150 + E.larg("x ", "g", 96) + E.larg("<", "g", 96) / 2, 690, 50, -90, 360 * ease_out(prog(t, C["s11.d"], 0.5)), NEG, 6)
    area_sinal(c, t, C["s11.e"], PG, g, -1.5, 4, True)
    E.frase(c, t, C["s11.e"], [("positiva", "g", 62, POS), ("à", "i", 60), ("esquerda", "g", 62), ("do", "i", 60), ("4", "g", 66, ENT)], XE, 860)
    if t >= C["s11.f"]:
        xv = lerp(-0.8, 6.5, ease_io(prog(t, C["s11.f"], 1.6)))
        c.drawCircle(*PG(xv, g(xv)), 16, M.paint(NEG))
    E.frase(c, t, C["s11.f"], [("começa", "i", 56), ("no", "i", 56), ("alto", "g", 58), ("e", "i", 56), ("desce", "g", 58, NEG)], XE, 960)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    eixos(c, t, PG, C["s12"] - 3, GX, GY)
    E.curva(c, t, C["s12"] - 3, PG, g, -1.5, 7.5, d=0.1)
    raiz(c, t, C["s12"] - 3, PG, 4)
    mista(c, LG, XE, 200, 84, ep(t, C["s12"] - 2, 0.3))
    E.frase(c, t, C["s12.a"], [("positiva", "g", 62, NEG), ("sempre", "g", 62, NEG), ("à", "i", 60), ("direita?", "g", 62, NEG)], XE, 320)
    errado = 1 - ep(t, C["s12.e"], 0.4)
    if t >= C["s12.b"] and errado > 0:
        x, y, w, h_ = PG.caixa
        c.save()
        c.clipRect(skia.Rect.MakeLTRB(PG.x(4), PG.oy - 120, x + w, PG.oy), True)
        c.drawRect(skia.Rect.MakeLTRB(PG.x(4), PG.oy - 120, x + w, PG.oy), M.paint(POS, 0.25 * ep(t, C["s12.b"], 0.4) * errado))
        c.restore()
    fml(c, t, C["s12.b"], "g > 0 para x > 4 ?", XE, 450, 66, NEG)
    fml(c, t, C["s12.c"], "x = 5:  −3 · 5 = −15", XE, 590, 66)
    fml(c, t, C["s12.d"], "−15 + 12 = −3", XE + 180, 700, 66)
    E.ponto(c, t, C["s12.e"], PG, 5, -3, cor=NEG, r=16)
    E.foco(c, t, C["s12.e"], 0.4, lambda a: (E.pilula(c, "negativo", XE + 420, 790, 46, "g", fundo=NEG, a=a)))
    E.foco(c, t, C["s12.e"] + 0.3, 0.4, lambda a: E.selo(c, XE + 760, 425, 34, False, a))
    area_sinal(c, t, C["s12.e"] + 0.3, PG, g, 4, 7.5, False)
    E.foco(c, t, C["s12.f"], 0.5, lambda a: E.pilula(c, "quem decide o lado: o sinal do a", XE + 420, 920, 46, "g", fundo=COR, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 66, CLARO), XE, 170)
        E.frase(c, t, C["s13.a"], [("à", "i", 66, CLARO), ("direita", "g", 70, BR), ("da", "i", 66, CLARO), ("raiz:", "i", 66, CLARO), ("o", "i", 66, CLARO),
                                   ("sinal", "g", 70, BR), ("do", "i", 66, CLARO), ("a", "g", 74, CLARO)], XE, 300)
        E.frase(c, t, C["s13.b"], [("à", "i", 66, CLARO), ("esquerda:", "g", 70, BR), ("o", "i", 66, CLARO), ("contrário", "g", 70, BR)], XE, 410)
        E.foco(c, t, C["s13.c"], 0.5, lambda a: (mista(c, [("2", BR), ("x", CLARO), (" − 6", BR)], XE, 640, 66, a),
                                                E.escreve(c, "a > 0", XE, 720, 50, "g", POS, a)))
        sinais(c, t, C["s13.c"], 760, 1700, 650, "3", "−", "+", C["s13.c"] + 1.0, C["s13.c"] + 0.4, escuro=True)
        E.foco(c, t, C["s13.d"], 0.5, lambda a: (mista(c, [("−3", BR), ("x", CLARO), (" + 12", BR)], XE, 900, 66, a),
                                                E.escreve(c, "a < 0", XE, 980, 50, "g", NEG, a)))
        sinais(c, t, C["s13.d"], 760, 1700, 910, "4", "+", "−", C["s13.d"] + 1.0, C["s13.d"] + 0.4, escuro=True)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    minis = ((C["s14.a"], 220, lambda v: 0.8 * v + 0.4, POS, "a > 0: depois, em cima"),
             (C["s14.b"], 780, lambda v: -0.9 * v - 0.3, NEG, "a < 0: depois, embaixo"),
             (C["s14.d"], 1340, lambda v: 1.4, CLARO, "f(x) = 5"))
    for t0, x, fn, cor, rot in minis:
        Q = mini(c, t, t0, x, 300, 360, 340, fn, cor, escuro=True)
        E.foco(c, t, t0 + 0.4, 0.4, lambda a, x=x, rot=rot, cor=cor: E.formula(c, rot, x + 180, 730, 44, "g", cor, a, "center"))
        if fn(0) != 1.4:
            z = -0.4 / 0.8 if cor == POS else -0.3 / 0.9
            k = ease_back(prog(t, t0 + 0.9, 0.4))
            if k > 0:
                c.drawCircle(*Q(z, 0), 12 * k, M.paint(BR))
    E.frase(c, t, C["s14"], [("funciona", "i", 64, CLARO), ("porque…", "g", 66, BR)], W / 2, 190, "center")
    E.frase(c, t, C["s14.c"], [("não", "g", 62, NEG), ("vale", "i", 60, CLARO), ("com", "i", 60, CLARO), ("a", "g", 64, BR), ("=", "g", 62, BR), ("0", "g", 64, BR)],
            1340, 830)
    E.frase(c, t, C["s14.e"], [("nunca", "g", 54, BR), ("corta", "i", 52, CLARO), ("o", "i", 52, CLARO), ("eixo", "i", 52, CLARO)], 1340, 920)
    E.frase(c, t, C["s14.e"] + 1.4, [("positiva", "g", 54, POS), ("para", "i", 52, CLARO), ("todo", "i", 52, CLARO), ("x", "g", 54, CLARO)], 1340, 1000)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 64, COR), XE, 180)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: mista(c, LH, XE, 380, 130, a))
    perguntas = (("s15.b", "1", [("onde", "i", 60), ("corta", "g", 62), ("o", "i", 60), ("eixo", "i", 60), ("x?", "g", 62, ENT)]),
                 ("s15.c", "2", [("positiva", "g", 62, POS), ("para", "i", 60), ("quais", "i", 60), ("x?", "g", 62, ENT)]),
                 ("s15.d", "3", [("negativa", "g", 62, NEG), ("para", "i", 60), ("quais", "i", 60), ("x?", "g", 62, ENT)]))
    for i, (k, n, partes) in enumerate(perguntas):
        yy = 580 + i * 130
        E.foco(c, t, C[k], 0.5, lambda a, n=n, yy=yy: (E.bola(c, XE + 34, yy - 20, 34, a=a), centro(c, n, XE + 34, yy - 4, 44, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, XE + 100, yy)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=600, r=150)


# ---------------- resposta ----------------
PH = E.Plano(1120, 200, 660, 680, -1.5, 5.5, -11, 15)
HX, HY = list(range(-1, 6)), list(range(-8, 15, 4))


def b_resposta(c, t, C, b):
    mista(c, LH, XE, 200, 84, ep(t, C["s17"] - 2, 0.3))
    eixos(c, t, PH, C["s17"] - 1.5, HX, HY)
    E.curva(c, t, C["s17"] - 1.0, PH, h, -1.5, 5.5, d=0.9)

    def s17():
        fml(c, t, C["s17.a"], "−4x + 10 = 0", XE, 380, 84)
        fml(c, t, C["s17.b"], "−4x = −10", XE + 90, 520, 84)
        op(c, t, C["s17.b"], "−10", XE + 600, 490)
        fml(c, t, C["s17.c"], "x = 2,5", XE + 160, 660, 90, ENT)
        op(c, t, C["s17.c"], "÷ (−4)", XE + 660, 630)
        E.frase(c, t, C["s17.d"], [("corta", "g", 62), ("o", "i", 60), ("eixo", "i", 60), ("x", "g", 64, ENT), ("no", "i", 60), ("2,5", "g", 66, ENT)], XE, 820)
    E.saida(c, t, C["s18"] - 0.1, s17)
    raiz(c, t, C["s17.d"], PH, 2.5, "2,5")
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18.a"], [("a", "g", 66, COR), ("=", "g", 64), ("−4:", "g", 66), ("negativo", "g", 64, NEG)], XE, 320)
    E.frase(c, t, C["s18.b"], [("à", "i", 58), ("direita", "g", 60), ("da", "i", 58), ("raiz:", "i", 58), ("−", "g", 70, NEG)], XE, 420)
    fml(c, t, C["s18.c"], "negativa: x > 2,5", XE, 550, 70, NEG)
    area_sinal(c, t, C["s18.c"], PH, h, 2.5, 5.5, False)
    fml(c, t, C["s18.d"], "positiva: x < 2,5", XE, 670, 70, POS)
    area_sinal(c, t, C["s18.d"], PH, h, -1.5, 2.5, True)
    sinais(c, t, C["s18.b"] + 0.4, XE, 900, 850, "2,5", "+", "−", C["s18.d"], C["s18.c"])
    E.ponto(c, t, C["s18.e"], PH, 0, 10, cor=POS, r=16)
    E.foco(c, t, C["s18.e"] + 0.3, 0.4, lambda a: (par(c, "0", "10", PH.x(0) + 28, PH.y(10) - 20, 40, a),
                                                  E.pilula(c, "h(0) = 10 > 0", 1460, 160, 44, "g", fundo=POS, a=a)))
    E.foco(c, t, C["s18.f"], 0.4, lambda a: E.selo(c, 1700, 160, 34, True, a))


# ---------------- fechamento ----------------
PN = E.Plano(1180, 420, 560, 440, -1, 6, -1, 6)


def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", [("zero:", "g", 78, COR), ("o", "i", 74), ("x", "g", 80, ENT), ("que", "i", 74), ("faz", "i", 74), ("y", "g", 80), ("=", "g", 78), ("0", "g", 80)]),
                 ("s19.b", [("onde", "i", 74), ("a", "i", 74), ("reta", "g", 78), ("corta", "g", 78, COR), ("o", "i", 74), ("eixo", "i", 74), ("x", "g", 80, ENT)]),
                 ("s19.c", [("sinal", "g", 78), ("do", "i", 74), ("a:", "g", 78, COR), ("lado", "i", 74), ("do", "i", 74), ("positivo", "g", 78, POS)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 28, 52, a=a),
                                                         E.escreve(c, str(i + 1), 230 - E.larg(str(i + 1), "g", 60) / 2, y - 6, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 320, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s20.a"], [("2", "g", 90, COR), ("pontos", "g", 84), ("ou", "i", 80), ("um", "i", 80), ("gráfico", "g", 84)], XE, 410)
    E.frase(c, t, C["s20.b"], [("→", "g", 76, TINTA2), ("a", "i", 76), ("lei", "g", 90, COR)], XE, 540)
    E.frase(c, t, C["s20.c"], [("prever", "g", 66), ("o", "i", 62), ("próximo", "i", 62), ("valor", "i", 62)], XE, 670)
    if t >= C["s20.a"]:
        E.plano(c, t, C["s20.a"], *PN.caixa, PN.xmin, PN.xmax, PN.ymin, PN.ymax, grade=False, rotulos=False, size=30, d=0.5)
        E.ponto(c, t, C["s20.a"] + 0.3, PN, 1, 2, cor=SAI, r=14)
        E.ponto(c, t, C["s20.a"] + 0.5, PN, 3, 3, cor=SAI, r=14)
        if t >= C["s20.b"]:
            E.reta_pontos(c, t, C["s20.b"], PN, (1, 2), (3, 3), pontos=False)
        E.foco(c, t, C["s20.c"], 0.4, lambda a: centro(c, "?", PN.x(5), PN.y(4) - 30, 70, "g", COR, a))
        k = ease_back(prog(t, C["s20.c"], 0.4))
        if k > 0:
            c.drawCircle(*PN(5, 4), 14 * k, M.paint(COR))
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 260, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(520, 285, p), ep(t, C["s20.d"] + 0.2, 0.4))
    E.frase(c, t, C["s20.e"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, zero=b_zero, sinal=b_sinal, desce=b_desce, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
