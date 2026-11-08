"""Visual — Estudativo · MAT-FUN-006: gráfico de uma função e o teste da reta vertical.

Linguagem visual da trilha Funções (MAT-FUN-001 a 005): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita com eixos(), texto à esquerda; par (x, y) com o x índigo e o y preto (par()).
Nesta aula: o gráfico (E.curva) e os pontos (E.ponto) em índigo; a régua do teste é uma reta tracejada preta (regua()); cada toque
da régua na curva vira um anel: verde quando toca uma vez, vermelho quando toca duas. Mini-gráficos (mini()) para comparar desenhos.
Peças locais: eixos(), par(), regua(), toque(), mini(), linha_tab()."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FUN-006_grafico_de_uma_funcao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "pontos", "teste", "atalho", "questao", "fim"))
BR = "#FFFFFF"
f = lambda x: x * x - 1
g = lambda x: 3 - x * x
assert [f(x) for x in (-2, -1, 0, 1, 2)] == [3, 0, -1, 0, 3] and math.isclose(f(0.5), -0.75)
assert [g(x) for x in (-2, -1, 0, 1, 2)] == [-1, 2, 3, 2, -1] and 2 * 2 + 2 == 6 and (-2) ** 2 - 2 == 2
P = E.Plano(1080, 170, 720, 720, -3, 3, -2, 4)
CIMA = lambda x: 1 + math.sqrt(4 - x * x)
BAIXO = lambda x: 1 - math.sqrt(4 - x * x)


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


def eixos(c, t, P, tx, ty=None, tg=None, size=38):
    """plano em etapas (o mesmo da MAT-FUN-001): grade em tg, eixo x (índigo) em tx, eixo y (preto) em ty"""
    ty = tx if ty is None else ty
    x, y, w, h = P.caixa
    if tg is not None and t >= tg:
        q = ep(t, tg, 0.8)
        for v in range(int(P.xmin), int(P.xmax) + 1):
            M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
        for v in range(int(P.ymin), int(P.ymax) + 1):
            M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    if t >= tx:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 24, ep(t, tx, 0.7))
        E.foco(c, t, tx + 0.5, 0.4, lambda a: E.escreve(c, "x", x + w + 20, P.oy + 66, 62, "i", ENT, a))
        for i, v in enumerate(range(int(P.xmin), int(P.xmax) + 1)):
            if v == 0:
                continue
            X = P.x(v)
            E.foco(c, t, tx + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
                M.line(c, X, P.oy - 10, X, P.oy + 10, ENT, a, 4),
                centro(c, E._num(v), X, P.oy + 14 + size, size, "b", TINTA2, a)), sobe=6)
    if t >= ty:
        M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, SAI, 1.0, 6, 24, ep(t, ty, 0.7))
        E.foco(c, t, ty + 0.5, 0.4, lambda a: E.escreve(c, "y", P.ox + 22, y - 18, 62, "i", SAI, a))
        for i, v in enumerate(range(int(P.ymin), int(P.ymax) + 1)):
            if v == 0:
                continue
            Y = P.y(v)
            E.foco(c, t, ty + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
                M.line(c, P.ox - 10, Y, P.ox + 10, Y, SAI, a, 4),
                E.escreve(c, E._num(v), P.ox - 20 - E.larg(E._num(v), "b", size), Y + size * 0.36, size, "b", TINTA2, a)), sobe=6)


def plano(c, t, t0):
    eixos(c, t, P, t0, t0, t0)


def par(c, xv, yv, x, y, size, a=1.0, align="left", cores=None, est="g"):
    """par ordenado (x, y): x em índigo, y em preto"""
    cx_, cy_ = cores or (ENT, SAI)
    partes = (("(", TINTA), (xv, cx_), (", ", TINTA), (yv, cy_), (")", TINTA))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def regua(c, P, xv, a=1.0, cor=TINTA, largura=6):
    """a régua do teste: reta vertical tracejada de borda a borda do plano"""
    if a <= 0:
        return
    x, y, w, h = P.caixa
    X = P.x(xv)
    M.line(c, X, y - 10, X, y + h + 10, cor, a, largura, dash=[18, 12])


def regua_deitada(c, P, yv, a=1.0, cor=ERRADO):
    if a <= 0:
        return
    x, y, w, h = P.caixa
    Y = P.y(yv)
    M.line(c, x - 10, Y, x + w + 10, Y, cor, a, 6, dash=[18, 12])


def toque(c, P, xv, yv, cor, a=1.0, r=22):
    """anel no ponto em que a régua toca a curva"""
    if a <= 0:
        return
    X, Y = P(xv, yv)
    c.drawCircle(X, Y, r, M.paint(cor, 0.25 * a))
    c.drawCircle(X, Y, r, M.paint(cor, a, stroke=5))
    c.drawCircle(X, Y, 8, M.paint(cor, a))


def desliza(t, t0, d=4.0, x0=-2.8, x1=2.8):
    return lerp(x0, x1, ease_io(prog(t, t0, d)))


def mini(c, t, t0, x, y, w, h, curvas, rotulo=None, d=0.9, escuro=False):
    """mini-gráfico com eixos simples (E.plano sem grade nem números) e as curvas [(f, a, b)] desenhadas por E.curva; devolve o Plano"""
    Q = E.plano(c, t, t0, x, y, w, h, -3, 3, -3, 3, grade=False, rotulos=False, size=30, d=0.5, escuro=escuro)
    for i, (fn, a_, b_) in enumerate(curvas):
        E.curva(c, t, t0 + 0.3, Q, fn, a_, b_, d=d, largura=7)
    if rotulo:
        E.foco(c, t, t0 + 0.3, 0.4, lambda q: centro(c, rotulo, x + w / 2, y + h + 70, 46, "i", TINTA2, q))
    return Q


def anel_txt(c, t, t0, X, Y, r=46, cor=ERRADO, largura=6):
    q = ease_out(prog(t, t0, 0.5))
    if q > 0:
        E.arco(c, X, Y, r, -90, 360 * q, cor, largura)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        Q1 = mini(c, t, C["s01.a"], 260, 250, 600, 560, [(f, -2.0, 2.0)])
        Q2 = mini(c, t, C["s01.b"], 1060, 250, 600, 560, [(CIMA, -2, 2), (BAIXO, -2, 2)], d=0.9)
        for k, Q in (("s01.a", Q1), ("s01.b", Q2)):
            E.foco(c, t, C[k] + 0.6, 0.4, lambda a, Q=Q: centro(c, "é função?", Q.caixa[0] + Q.caixa[2] / 2, 140, 60, "g", COR, a))
        if t >= C["s01.c"]:
            a = ep(t, C["s01.c"], 0.4)
            xv = desliza(t, C["s01.c"] + 0.3, 2.0, -1.6, 1.0)
            for Q, dois in ((Q1, False), (Q2, True)):
                regua(c, Q, xv, a, TINTA2, 5)
                if dois:
                    toque(c, Q, xv, CIMA(xv), ERRADO, a, 16)
                    toque(c, Q, xv, BAIXO(xv), ERRADO, a, 16)
                else:
                    toque(c, Q, xv, f(xv), CERTO, a, 16)
            E.frase(c, t, C["s01.c"], [("só", "i", 70), ("uma", "i", 70), ("régua", "g", 66, COR), ("em", "i", 70), ("pé", "g", 66, COR)], W / 2, 1000, "center")
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.4, [("tabela", "g", 110), ("→", "g", 110, TINTA2), ("gráfico", "g", 110, COR)], XE, 460)
        E.frase(c, t, C["s02.b"], [("o", "i", 90), ("teste", "i", 90), ("da", "i", 90)], XE, 620)
        E.frase(c, t, C["s02.b"] + 0.6, [("reta", "g", 110, COR), ("vertical", "g", 110, COR)], XE, 760)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "marcar pontos no plano:", lambda a, y: par(c, "−2", "3", x + 44, y, 66, a)),
             ("s03.c", "calcular f(x):", lambda a, y: E.formula(c, "f(2) = 2^2 − 1 = 3", x + 44, y, 62, "g", COR, a)))
    for i, (k, l1, fn) in enumerate(itens):
        y = 250 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 64)], x + 44, y + 96)
        E.foco(c, t, C[k] + 0.4, 0.5, lambda a, fn=fn, y=y: fn(a, y + 196))
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(460, 760, q), ep(t, C["s03.b"], 0.4))


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    eixos(c, t, P, C["s04"], C["s04"], C["s04"])
    x, y, w, h = P.caixa
    q = ep(t, C["s04.a"], 0.3) * (1 - ep(t, C["s04.a"] + 1.8, 0.5))
    if q > 0:
        M.line(c, x - 10, P.oy, x + w + 20, P.oy, ENT, 0.25 * q, 26)
    q = ep(t, C["s04.b"], 0.3) * (1 - ep(t, C["s04.b"] + 1.8, 0.5))
    if q > 0:
        M.line(c, P.ox, y + h + 10, P.ox, y - 20, SAI, 0.2 * q, 26)
    E.frase(c, t, C["s04.a"], [("entrada", "g", 80, ENT), ("→", "g", 80, TINTA2), ("eixo", "i", 80), ("x", "g", 90, ENT)], XE, 330)
    E.frase(c, t, C["s04.b"], [("saída", "g", 80), ("→", "g", 80, TINTA2), ("eixo", "i", 80), ("y", "g", 90)], XE, 470)
    E.ponto(c, t, C["s04.c"], P, 2, 3, guias=True, cor=COR, r=16)
    E.foco(c, t, C["s04.c"] + 0.3, 0.4, lambda a: par(c, "2", "3", *P(2.15, 3.35), 46, a))
    E.foco(c, t, C["s04.c"], 0.5, lambda a: (par(c, "entrada", "saída", XE, 640, 64, a),))
    E.frase(c, t, C["s04.c"] + 0.6, [("=", "g", 64), ("um", "i", 68), ("ponto", "g", 64, COR)], XE + 570, 640)
    n = 33
    for i in range(n):
        xv = -2.0 + 4.0 * i / (n - 1)
        k = ease_back(prog(t, C["s04.d"] + 0.04 * i, 0.3))
        if k > 0:
            c.drawCircle(*P(xv, f(xv)), 9 * k, M.paint(COR))
    E.frase(c, t, C["s04.d"], [("gráfico:", "g", 76, COR), ("todos", "i", 76), ("os", "i", 76), ("pontos", "i", 76)], XE, 820)


# ---------------- tabela ----------------
XS = (-2, -1, 0, 1, 2)
TX, TY, TW, TH = 330, 330, 210, 92


def linha_tab(c, t, xs, ys, tx_, ty_, tc, tf, size=62, wc=TW, hl=TH, cab=("x", "f(x)"), destaque=None, escuro=False):
    """tabela x | f(x) em pé: tx_ = instante de cada x, tf = instante de cada f(x) (None = não aparece)"""
    tinta = BR if escuro else TINTA
    ca = CLARO if escuro else ENT
    a = ep(t, tc, 0.5)
    if a > 0:
        centro(c, cab[0], tx_ + wc / 2, ty_ - 24, 54, "i", ca, a)
        E.formula(c, cab[1], tx_ + wc * 1.5, ty_ - 24, 50, "b", tinta, a, "center")
        M.line(c, tx_, ty_, tx_ + 2 * wc, ty_, tinta, a, 4)
        M.line(c, tx_ + wc, ty_, tx_ + wc, ty_ + hl * len(xs) + 10, tinta, a, 4)
    for i, (xv, yv) in enumerate(zip(xs, ys)):
        ry = ty_ + 10 + hl * i
        if destaque is not None:
            q = destaque(i)
            if q > 0:
                M.rrect(c, tx_ - 8, ry + 4, 2 * wc + 16, hl - 8, 14, COR, 0.14 * q)
        E.foco(c, t, tc + 0.3 + 0.12 * i, 0.4, lambda q, xv=xv, ry=ry: centro(c, E._num(xv), tx_ + wc / 2, ry + hl / 2 + size * 0.36, size, "g", ca, q), sobe=6)
        if tf[i] is not None:
            E.foco(c, t, tf[i], 0.4, lambda q, yv=yv, ry=ry: centro(c, E._num(yv), tx_ + wc * 1.5, ry + hl / 2 + size * 0.36, size, "g", tinta, q), sobe=6)


def b_tabela(c, t, C, b):
    fml(c, t, C["s05.a"], "f(x) = x^2 − 1", W / 2, 190, 100, align="center")
    tf = [C["s05.e"], C["s06.a"] + 1.4, C["s06.b"] + 1.4, C["s06.c"] + 0.6, C["s06.d"] + 0.6]
    linha_tab(c, t, XS, [f(x) for x in XS], TX, TY, C["s05.b"], tf if True else None)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "de −2 até 2", TX + TW, TY + TH * 5 + 90, 44, "g", fundo=ENT, a=a))
    # as contas, uma por vez, à direita
    contas = (("s05.d", "s06.a", "f(−2) = (−2)^2 − 1", "= 4 − 1 = 3", "s05.e"),
              ("s06.a", "s06.b", "f(−1) = (−1)^2 − 1", "= 1 − 1 = 0", None),
              ("s06.b", "s06.c", "f(0) = 0^2 − 1", "= 0 − 1 = −1", None),
              ("s06.c", "s06.d", "f(1) = 1^2 − 1", "= 0", None),
              ("s06.d", None, "f(2) = 2^2 − 1", "= 3", None))
    for k0, k1, l1, l2, k2 in contas:
        def d(k0=k0, l1=l1, l2=l2, k2=k2):
            fml(c, t, C[k0], l1, 900, 470, 84)
            fml(c, t, C[k2] if k2 else C[k0] + 0.9, l2, 960, 600, 84, COR)
        if t >= C[k0]:
            if k1:
                E.saida(c, t, C[k1] - 0.1, d)
            else:
                d()


# ---------------- pontos ----------------
PTS = [(-2, 3), (-1, 0), (0, -1), (1, 0), (2, 3)]


def tab_pequena(c, t, t0, destaque=None):
    linha_tab(c, t, XS, [f(x) for x in XS], XE, 300, t0, [t0] * 5, size=52, wc=170, hl=78, destaque=destaque)


def b_pontos(c, t, C, b):
    plano(c, t, C["s07"] - 3)
    ks = ("s07.a", "s07.b", "s07.c", "s07.d", "s07.e")
    E.foco(c, t, C["s07"] - 3, 0.1, lambda a: fml(c, t, C["s07"] - 3, "f(x) = x^2 − 1", XE, 190, 70))

    def destaque(i):
        k = C[ks[i]]
        nxt = C[ks[i + 1]] if i < 4 else C["s08"]
        return ep(t, k, 0.3) * (1 - ep(t, nxt - 0.2, 0.3))

    def tab():
        tab_pequena(c, t, C["s07"] - 3, destaque)
    E.saida(c, t, C["s08.b"] - 0.1, tab)
    for k, (xv, yv) in zip(ks, PTS):
        E.ponto(c, t, C[k], P, xv, yv, guias=True, cor=COR, r=16)
    E.curva(c, t, C["s08.a"], P, f, -2.25, 2.25, d=1.6)
    E.saida(c, t, C["s08.b"] - 0.1, lambda: (
        E.frase(c, t, C["s08.a"] + 0.4, [("curva", "g", 64, CERTO), ("suave", "g", 64, CERTO)], 590, 430),
        E.frase(c, t, C["s08.a"] + 1.4, [("não", "i", 54, ERRADO), ("tracinhos", "i", 54, ERRADO), ("retos", "i", 54, ERRADO)], 590, 520)))
    if t >= C["s08.b"]:
        fml(c, t, C["s08.b"], "f(0,5) = 0,25 − 1", XE, 520, 72)
        fml(c, t, C["s08.c"], "= −0,75", XE + 120, 630, 80, COR)
        # o ponto cai do alto até a curva
        p = ease_out(prog(t, C["s08.d"] - 0.6, 0.8))
        if p > 0:
            yv = lerp(2.5, -0.75, p)
            c.drawCircle(*P(0.5, yv), 15, M.paint(ERRADO if p < 1 else CERTO))
        if t >= C["s08.d"] + 0.2:
            toque(c, P, 0.5, -0.75, CERTO, ep(t, C["s08.d"] + 0.2, 0.3))
            E.foco(c, t, C["s08.d"] + 0.2, 0.4, lambda a: par(c, "0,5", "−0,75", *P(0.7, -1.25), 40, a))
    E.frase(c, t, C["s08.e"], [("um", "i", 80), ("U", "g", 96, COR)], XE, 820)
    E.foco(c, t, C["s08.e"] + 1.0, 0.4, lambda a: E.pilula(c, "parábola: outra aula", XE + 470, 790, 40, "b", fundo=TINTA2, a=a))


# ---------------- teste da reta vertical ----------------
def b_teste(c, t, C, b):
    plano(c, t, C["s09"] - 3)
    circ = ep(t, C["s11.b"], 0.4)

    def parab():
        E.curva(c, t, C["s09"] - 3, P, f, -2.25, 2.25, d=0.1)
    E.saida(c, t, C["s11.b"], parab)

    def s09():
        E.frase(c, t, C["s09.a"], [("função:", "g", 66, COR), ("cada", "i", 68), ("entrada,", "i", 68, ENT), ("uma", "g", 66), ("saída", "i", 68)], XE, 300)
        E.frase(c, t, C["s09.b"], [("reta", "g", 66), ("em", "i", 68), ("pé", "g", 66), ("na", "i", 68), ("entrada", "i", 68, ENT)], XE, 440)
        E.frase(c, t, C["s09.c"], [("toca", "i", 68), ("todas", "g", 66), ("as", "i", 68), ("saídas", "i", 68)], XE, 540)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if C["s09.b"] <= t < C["s10.a"]:
        a = ep(t, C["s09.b"], 0.4)
        regua(c, P, 1.5, a)
        toque(c, P, 1.5, f(1.5), CERTO, ep(t, C["s09.c"], 0.3))
    if C["s10.a"] <= t < C["s11.b"]:
        xv = desliza(t, C["s10.a"] + 0.2, 4.5, -2.2, 1.5) if t < C["s11.a"] else lerp(1.5, -1.0, ease_io(prog(t, C["s11.a"], 1.2)))
        a = ep(t, C["s10.a"], 0.3) * (1 - ep(t, C["s11.b"] - 0.3, 0.3))
        regua(c, P, xv, a)
        toque(c, P, xv, f(xv), CERTO, a)
    if t >= C["s10"]:
        def s10():
            E.frase(c, t, C["s10.a"], [("deslize", "i", 72), ("a", "i", 72), ("régua", "g", 68, COR)], XE, 300)
            E.frase(c, t, C["s10.b"], [("toca", "i", 66), ("1", "g", 72, CERTO), ("vez:", "i", 66), ("função", "g", 64, CERTO)], XE, 450)
            E.frase(c, t, C["s10.c"], [("toca", "i", 66), ("2", "g", 72, ERRADO), ("vezes:", "i", 66), ("não", "g", 64, ERRADO), ("é", "g", 64, ERRADO)], XE, 560)
            E.frase(c, t, C["s10.d"], [("uma", "i", 60, TINTA2), ("entrada,", "i", 60, ENT), ("duas", "g", 58, ERRADO), ("saídas", "i", 60, TINTA2)], XE, 650)
        E.saida(c, t, C["s11"] - 0.1, s10)
    if t >= C["s11"]:
        E.frase(c, t, C["s11.a"], [("x²", "g", 66, COR), ("−", "g", 66, COR), ("1:", "g", 66, COR), ("toca", "i", 66), ("1", "g", 70, CERTO), ("vez", "i", 66)], XE, 320)
        E.foco(c, t, C["s11.a"] + 0.8, 0.4, lambda a: E.pilula(c, "é função", XE + 200, 420, 52, "g", fundo=CERTO, a=a))
        E.frase(c, t, C["s11.b"], [("o", "i", 70), ("círculo", "g", 66), ("falha", "g", 66, ERRADO)], XE, 600)
        E.foco(c, t, C["s11.d"], 0.5, lambda a: E.pilula(c, "não é função", XE + 240, 720, 52, "g", fundo=ERRADO, a=a))
    if circ > 0:
        E.curva(c, t, C["s11.b"], P, CIMA, -2, 2, d=0.8)
        E.curva(c, t, C["s11.b"] + 0.2, P, BAIXO, -2, 2, d=0.8)
    if t >= C["s11.c"]:
        a = ep(t, C["s11.c"], 0.4)
        regua(c, P, 0.8, a)
        toque(c, P, 0.8, CIMA(0.8), ERRADO, ep(t, C["s11.c"] + 0.4, 0.3))
        toque(c, P, 0.8, BAIXO(0.8), ERRADO, ep(t, C["s11.c"] + 0.8, 0.3))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano(c, t, C["s12"] - 3)
    E.curva(c, t, C["s12"] - 3, P, f, -2.25, 2.25, d=0.1)
    E.frase(c, t, C["s12.a"], [("régua", "g", 72, ERRADO), ("deitada?", "g", 72, ERRADO)], XE, 280)

    def deitada():
        regua_deitada(c, P, 3, ep(t, C["s12.b"], 0.4))
        toque(c, P, -2, 3, ERRADO, ep(t, C["s12.b"] + 0.5, 0.3))
        toque(c, P, 2, 3, ERRADO, ep(t, C["s12.b"] + 0.8, 0.3))
        E.foco(c, t, C["s12.b"] + 1.0, 0.4, lambda a: (par(c, "−2", "3", *P(-2.9, 3.45), 38, a), par(c, "2", "3", *P(1.05, 3.45), 38, a)))
    E.saida(c, t, C["s12.f"], deitada)
    E.frase(c, t, C["s12.c"], [("2", "g", 66, ENT), ("entradas,", "i", 64, ENT), ("mesma", "i", 64), ("saída", "g", 62)], XE, 430)
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.pilula(c, "isso pode", XE + 150, 520, 48, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s12.e"], [("1", "g", 66, ENT), ("entrada,", "i", 64, ENT), ("2", "g", 66, ERRADO), ("saídas:", "i", 64), ("não", "g", 62, ERRADO)], XE, 680)
    E.frase(c, t, C["s12.f"], [("a", "i", 76), ("régua", "g", 76, COR), ("fica", "i", 76), ("em", "i", 76), ("pé", "g", 76, COR)], XE, 850)
    if t >= C["s12.f"]:
        a = ep(t, C["s12.f"], 0.4)
        regua(c, P, 2, a)
        toque(c, P, 2, 3, CERTO, a)


# ---------------- atalho (palco escuro) ----------------
def ponte_copia(c, xa, xb, y, fundo, p, cor=CERTO):
    """curva rasa que leva o resultado de xa (positivo) até xb (negativo), com ponta de seta"""
    pts = []
    for i in range(41):
        u = p * i / 40
        x = lerp(xa, xb, u)
        pts.append((x, y + fundo * 4 * u * (1 - u)))
    pa = skia.Path()
    pa.moveTo(*pts[0])
    for q in pts[1:]:
        pa.lineTo(*q)
    c.drawPath(pa, M.paint(cor, 1.0, stroke=5, cap_round=True))
    if p > 0.98:
        (x1, y1), (x0, y0) = pts[-1], pts[-3]
        M.arrow(c, x0, y0, x1, y1 - 6, cor, 1.0, 5, 20)


def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 72, CLARO), W / 2, 150, "center")
        E.frase(c, t, C["s13.a"], [("entradas", "g", 80, BR), ("opostas,", "i", 80, CLARO), ("mesma", "i", 80, CLARO), ("saída", "g", 80, BR)], W / 2, 280, "center")
        # tabela deitada: x em cima, f(x) embaixo
        xs = [W / 2 + (i - 2) * 230 for i in range(5)]
        y1, y2 = 470, 620
        a = ep(t, C["s13.a"] + 0.6, 0.5)
        if a > 0:
            E.escreve(c, "x", 200, y1 + 20, 64, "i", CLARO, a)
            E.formula(c, "f(x)", 170, y2 + 20, 56, "b", BR, a)
            M.line(c, 340, (y1 + y2) / 2 - 20, 1660, (y1 + y2) / 2 - 20, BR, a * 0.5, 3)
            for X, xv in zip(xs, XS):
                centro(c, E._num(xv), X, y1 + 20, 72, "g", CLARO, a)
        quando = {2: C["s13.b"], -2: C["s13.b"] + 0.5, 0: C["s13.c"], 1: C["s13.c"] + 0.3, -1: C["s13.d"] + 0.5}
        for X, xv in zip(xs, XS):
            ti = quando[xv]
            E.foco(c, t, ti, 0.4, lambda q, X=X, xv=xv: centro(c, E._num(f(xv)), X, y2 + 20, 72, "g", BR if xv >= 0 else CERTO, q))
        # setas de cópia: dos positivos para os negativos
        for k, (xa, xb) in enumerate(((xs[3], xs[1]), (xs[4], xs[0]))):
            p = ease_io(prog(t, C["s13.d"] + 0.4 * k, 0.7))
            if p > 0:
                ponte_copia(c, xa, xb, y2 + 50, 60 + 40 * k, p)
        E.frase(c, t, C["s13.c"], [("calcule", "i", 60, CLARO), ("só", "i", 60, CLARO), ("0,", "g", 60, BR), ("1", "g", 60, BR), ("e", "i", 60, CLARO), ("2", "g", 60, BR)],
                W / 2, 880, "center")
        E.frase(c, t, C["s13.d"], [("e", "i", 60, CLARO), ("copie", "g", 60, CERTO), ("para", "i", 60, CLARO), ("os", "i", 60, CLARO), ("negativos", "g", 60, BR)],
                W / 2, 970, "center")
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], [("expoente", "i", 80, CLARO), ("par", "g", 80, BR), ("apaga", "i", 80, CLARO), ("o", "i", 80, CLARO), ("sinal", "g", 80, BR)], W / 2, 220, "center")
    E.foco(c, t, C["s14.a"] + 1.2, 0.5, lambda a: E.formula(c, "(−2)^2 = 2^2 = 4", W / 2, 360, 96, "g", CLARO, a, "center"))
    E.frase(c, t, C["s14.b"], [("não", "g", 66, ERRADO), ("compensa:", "i", 66, CLARO), ("x", "g", 70, BR), ("também", "i", 66, CLARO), ("sem", "i", 66, CLARO),
                               ("expoente", "i", 66, CLARO)], W / 2, 530, "center")
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "f(x) = x^2 + x", W / 2, 670, 96, "g", BR, a, "center"))
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.formula(c, "f(2) = 4 + 2 = 6", 320, 860, 76, "g", BR, a))
    E.foco(c, t, C["s14.e"], 0.5, lambda a: E.formula(c, "f(−2) = 4 − 2 = 2", 1040, 860, 76, "g", ERRADO, a))


# ---------------- questão ----------------
RETA = lambda x: 0.8 * x + 0.4
ONDA = lambda x: 1.3 * math.sin(1.7 * x)
UD_C = lambda x: math.sqrt(x) if x >= 0 else None
UD_B = lambda x: -math.sqrt(x) if x >= 0 else None
MINIS = ((190, "reta inclinada", [(RETA, -3, 3)]), (750, "onda deitada", [(ONDA, -3, 3)]), (1310, "U deitado", [(UD_C, 0, 3), (UD_B, 0, 3)]))


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 64, COR), XE, 150)
    fml(c, t, C["s15.a"], "f(x) = 3 − x^2", XE, 280, 90)
    E.frase(c, t, C["s15.b"], [("tabela:", "i", 60), ("x", "g", 64, ENT), ("de", "i", 60), ("−2", "g", 64, ENT), ("até", "i", 60), ("2", "g", 64, ENT)], XE, 390)
    for (x, nome, curvas), k in zip(MINIS, ("s15.d", "s15.e", "s15.f")):
        mini(c, t, C[k], x, 520, 420, 360, curvas, nome)
    E.frase(c, t, C["s15.g"], [("quais", "i", 66), ("são", "i", 66), ("função?", "g", 66, COR)], 1250, 390)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1000, cy=190, r=70)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        plano(c, t, C["s17"] - 3)
        fml(c, t, C["s17"] - 3, "f(x) = 3 − x^2", XE, 190, 70)
        tf = [C["s17.d"] + 0.6, C["s17.d"], C["s17.a"], C["s17.b"], C["s17.c"]]
        linha_tab(c, t, XS, [g(x) for x in XS], XE, 300, C["s17"] - 3, tf, size=52, wc=170, hl=78)
        E.foco(c, t, C["s17.b"] + 0.4, 0.4, lambda a: E.formula(c, "3 − 1 = 2", 730, 560, 56, "g", TINTA2, a))
        E.foco(c, t, C["s17.c"] + 0.4, 0.4, lambda a: E.formula(c, "3 − 4 = −1", 730, 640, 56, "g", TINTA2, a))
        if t >= C["s17.d"]:
            p = ep(t, C["s17.d"], 0.6)
            for k, (ya, yb) in enumerate(((300 + 10 + 78 * 3 + 39, 300 + 10 + 78 * 1 + 39), (300 + 10 + 78 * 4 + 39, 300 + 10 + 78 * 0 + 39))):
                q = ep(t, C["s17.d"] + 0.6 * k, 0.6)
                if q > 0:
                    E.arco(c, XE + 340 + 20, (ya + yb) / 2, (ya - yb) / 2, -90, 180 * q, CERTO, 5)
        for i, xv in enumerate(XS):
            ti = (C["s17.d"] + 0.6, C["s17.d"], C["s17.a"], C["s17.b"], C["s17.c"])[i]
            E.ponto(c, t, ti + 0.2, P, xv, g(xv), cor=COR, r=15)
        E.curva(c, t, C["s17.e"], P, g, -2.3, 2.3, d=1.4)
        E.foco(c, t, C["s17.e"] + 1.2, 0.4, lambda a: E.pilula(c, "U de cabeça para baixo", XE + 300, 880, 44, "g", fundo=COR, a=a))
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("régua", "g", 70, COR), ("em", "i", 72), ("pé", "g", 70, COR), ("nos", "i", 72), ("três", "i", 72)], W / 2, 220, "center")
    for (x, nome, curvas), k, ok in zip(MINIS, ("s18.a", "s18.b", "s18.c"), (True, True, False)):
        Q = mini(c, t, C["s18"] - 2, x, 380, 420, 360, curvas, nome)
        if t >= C[k]:
            a = ep(t, C[k], 0.3)
            xv = 1.3 if ok else 1.6
            regua(c, Q, xv, a, TINTA, 5)
            if ok:
                toque(c, Q, xv, curvas[0][0](xv), CERTO, a, 16)
            else:
                toque(c, Q, xv, UD_C(xv), ERRADO, a, 16)
                toque(c, Q, xv, UD_B(xv), ERRADO, a, 16)
            E.foco(c, t, C[k] + 0.5, 0.4, lambda q, x=x, ok=ok: E.pilula(c, "função" if ok else "não é função", x + 210, 920, 48, "g",
                                                                         fundo=CERTO if ok else ERRADO, a=q))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", [("tabela,", "g", 84), ("pontos", "g", 84, COR), ("e", "i", 84), ("curva", "g", 84), ("suave", "i", 84)]),
                 ("s19.b", [("régua", "g", 84, COR), ("em", "i", 84), ("pé", "i", 84), ("toca", "i", 84), ("2", "g", 90, ERRADO), ("vezes:", "i", 84),
                            ("não", "g", 84, ERRADO), ("é", "g", 84, ERRADO)]))
        for i, (k, partes) in enumerate(itens):
            y = 450 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s20.a"], [("ler", "g", 130, COR), ("um", "i", 120), ("gráfico", "g", 130, COR)], XE, 470)
    E.frase(c, t, C["s20.b"], ps("a temperatura ao longo do dia", "i", 64, TINTA2), XE, 590, passo=0.1)
    E.frase(c, t, C["s20.c"], [("máxima,", "g", 66), ("zero,", "g", 66), ("sobe", "i", 70), ("e", "i", 70), ("desce", "i", 70)], XE, 700)
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s20.d"] + 0.2, 0.4))
    E.frase(c, t, C["s20.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, tabela=b_tabela, pontos=b_pontos, teste=b_teste, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
