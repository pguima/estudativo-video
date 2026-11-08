"""Visual — Estudativo · MAT-ANG-015: Teorema de Pitágoras (catetos 6 e 8: hipotenusa 10; hipotenusa 13 e cateto 5: cateto 12).
Linguagem da geometria plana (MAT-ANG-001 a 020): lados em tinta; o lado da vez em cor forte por cima (a hipotenusa em COR,
índigo; os catetos em TINTA2); ângulo reto = quadradinho; medidas na grotesca; lados iguais com tracinhos; erro em vermelho,
certo em verde; resposta na esfera; atalho no palco escuro.
Pitágoras com lajotas: em cada lado do triângulo 3-4-5 nasce um quadrado quadriculado (grade de verdade, 3x3, 4x4 e 5x5).
As 9 lajotas índigo e as 16 âmbar voam para o quadrado da hipotenusa e o enchem: o 3x3 num canto e o 16 em L em volta.
As figuras respeitam as medidas (6 e 8, 5 e 12, 8 e 15): a figura não mente.
Peças locais: quadro() (quadrado sobre um lado, para fora do triângulo), grade_q() (contorno e grade), ladrilho() (uma lajota
em qualquer ângulo), voo() (lajota que viaja girando), txt_lado(), grosso(), eq() (igualdade com os dois lados separados,
para o "tire 25 de cada lado"), pergunta() (linhas da questão + relógio), poste().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-015_teorema_de_pitagoras.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("lajotas", "hipotenusa", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
assert 6 + 8 == 14 and 6 ** 2 + 8 ** 2 == 100 == 10 ** 2
assert 3 * 3 == 9 and 4 * 4 == 16 and 5 * 5 == 25 and 9 + 16 == 25 and 25 + 25 == 50 != 25
assert 13 ** 2 == 169 and 5 ** 2 == 25 and 169 - 25 == 144 == 12 ** 2 and 25 + 144 == 169
assert 169 + 25 == 194 and 14 ** 2 == 196 and 13 ** 2 < 194 < 14 ** 2
assert 13 + 5 == 18 and 13 - 5 == 8 and 18 * 8 == 144
assert 25 + 24 == 49 and 25 - 24 == 1 and 49 * 1 == 49 == 7 ** 2 and 25 ** 2 - 24 ** 2 == 49
assert 17 ** 2 == 289 and 8 ** 2 == 64 and 289 - 64 == 225 == 15 ** 2 and 17 + 8 == 25 and 17 - 8 == 9 and 25 * 9 == 225


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")))


def meio(P, Q):
    return (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2


def txt_lado(c, P, Q, s, G, size=54, cor=None, a=1.0, gap=20, dentro=False):
    """medida encostada no meio do lado PQ, por fora do triângulo de centro G (ou por dentro)"""
    if a <= 0 or not s:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = meio(P, Q)
    fora = (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 > (mx - G[0]) ** 2 + (my - G[1]) ** 2
    if fora == dentro:
        nx, ny = -nx, -ny
    E._cola(c, s, mx, my, nx, ny, gap, size, "b", cor or COR, a)


def grosso(c, P, Q, cor, a, larg=12, p=1.0):
    if a > 0 and p > 0:
        M.line(c, *P, *Q, cor, a, larg, progress=p)


def quadro(P, Q, G, k):
    """quadrado sobre o lado PQ, para fora do triângulo de centro G, dividido em k x k lajotas"""
    L = math.dist(P, Q)
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = meio(P, Q)
    if nx * (mx - G[0]) + ny * (my - G[1]) < 0:
        nx, ny = -nx, -ny
    s = L / k
    cantos = [P, Q, (Q[0] + nx * L, Q[1] + ny * L), (P[0] + nx * L, P[1] + ny * L)]

    def cel(i, j):
        return P[0] + ux * (i + 0.5) * s + nx * (j + 0.5) * s, P[1] + uy * (i + 0.5) * s + ny * (j + 0.5) * s
    centro_q = (mx + nx * L / 2, my + ny * L / 2)
    return dict(P=P, Q=Q, u=(ux, uy), n=(nx, ny), s=s, k=k, L=L, cantos=cantos, cel=cel, ang=math.degrees(math.atan2(uy, ux)), centro=centro_q)


def grade_q(c, q, p=1.0, ag=1.0, fundo=1.0):
    """contorno do quadrado (desenhado em volta, p = 0..1) e as linhas da grade (ag)"""
    if p <= 0:
        return
    P, (ux, uy), (nx, ny), s, k, L = q["P"], q["u"], q["n"], q["s"], q["k"], q["L"]
    if fundo > 0:
        path = skia.Path(); path.addPoly(q["cantos"], True)
        c.drawPath(path, M.paint("#FFFFFF", 0.85 * fundo * ep(p, 0.5, 0.5) if p < 1 else 0.85 * fundo))
    if ag > 0:
        for i in range(1, k):
            x0, y0 = P[0] + ux * i * s, P[1] + uy * i * s
            M.line(c, x0, y0, x0 + nx * L, y0 + ny * L, TINTA2, ag * 0.55, 2.5)
            x1, y1 = P[0] + nx * i * s, P[1] + ny * i * s
            M.line(c, x1, y1, x1 + ux * L, y1 + uy * L, TINTA2, ag * 0.55, 2.5)
    E._contorno(c, q["cantos"], p, TINTA, 5)


def ladrilho(c, x, y, s, ang, cor, a=1.0, k=1.0, alfa=0.88):
    """uma lajota quadrada de lado s, centro (x, y), girada ang graus; k = escala de entrada"""
    if a <= 0 or k <= 0:
        return
    h = s * 0.43 * k
    ux, uy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    nx, ny = -uy, ux
    pts = [(x + ux * h * sx + nx * h * sy, y + uy * h * sx + ny * h * sy) for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
    path = skia.Path(); path.addPoly(pts, True)
    c.drawPath(path, M.paint(cor, alfa * a))
    c.drawPath(path, M.paint(E.mix(cor, "#000000", 0.25), 0.5 * a, stroke=2))


def enche(c, t, t0, q, cor, dt=0.07, a=1.0, alfa=0.88, menos=()):
    """as lajotas do quadrado entram uma a uma, fileira por fileira a partir do lado do triângulo"""
    m = 0
    for j in range(q["k"]):
        for i in range(q["k"]):
            if (i, j) not in menos:
                k = ease_back(prog(t, t0 + m * dt, 0.3))
                ladrilho(c, *q["cel"](i, j), q["s"], q["ang"], cor, a, k, alfa)
            m += 1


def voo(c, t, t0, d, de, para, cor):
    """lajota que sai do quadrado `de` e assenta no `para`; de/para = (q, i, j). Deixa o contorno tracejado na origem"""
    (q0, i0, j0), (q1, i1, j1) = de, para
    x0, y0 = q0["cel"](i0, j0)
    x1, y1 = q1["cel"](i1, j1)
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        ladrilho(c, x0, y0, q0["s"], q0["ang"], cor)
        return
    ladrilho(c, x0, y0, q0["s"], q0["ang"], cor, 1.0, 1.0, 0.16)
    g0, g1 = q0["ang"], q1["ang"]
    dg = ((g1 - g0 + 45) % 90) - 45
    s = lerp(q0["s"], q1["s"], p)
    lift = 1 + 0.15 * math.sin(math.pi * p)
    ladrilho(c, lerp(x0, x1, p), lerp(y0, y1, p) - 40 * math.sin(math.pi * p), s * lift, g0 + dg * p, cor)


def eq(c, t, t0, esq, dir_, X, y, size, cor=None, gap=40):
    """igualdade com o sinal em X: esq termina antes dele, dir_ começa depois. Devolve (centro da esquerda, centro da direita)"""
    we = E.formula(None, esq, 0, 0, size, "g", a=0)
    wd = E.formula(None, dir_, 0, 0, size, "g", a=0)
    E.foco(c, t, t0, 0.5, lambda a: (E.formula(c, esq, X - gap, y, size, "g", cor, a, "right"),
                                     E.formula(c, "=", X, y, size, "g", cor, a, "center"),
                                     E.formula(c, dir_, X + gap, y, size, "g", cor, a, "left")))
    return X - gap - we / 2, X + gap + wd / 2


def pergunta(c, t, linhas, rel, X=1500, y0=780):
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, y0 + i * 95, "center", 0.12)
    E.relogio(c, t, rel, X, 380, 170)


# ---------------- gancho ----------------
GS, GK, GE = (230, 930), (230 + 6 * 82, 930), (230 + 6 * 82, 930 - 8 * 82)


def b_gancho(c, t, C, b):
    a1, b1, c1, d1, e1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"], C["s01.e"]
    X = 1420

    def um():
        # a caminhada: 6 para a direita, vira, 8 para cima
        p1 = ease_io(prog(t, a1 + 0.2, 1.6))
        p2 = ease_io(prog(t, b1 + 0.3, 1.8))
        E.foco(c, t, a1, 0.4, lambda a: c.drawCircle(*GS, 14, M.paint(TINTA, a)))
        E.foco(c, t, a1, 0.4, lambda a: centro(c, "partida", GS[0], GS[1] + 80, 50, "i", TINTA, a))
        if p1 > 0:
            M.line(c, *GS, *GK, TINTA, 1.0, 8, progress=p1)
        if p2 > 0:
            M.line(c, *GK, *GE, TINTA, 1.0, 8, progress=p2)
        E.foco(c, t, a1 + 1.0, 0.4, lambda a: txt_lado(c, GS, GK, "6 m", (GK[0], GS[1] - 400), 64, TINTA, a))
        E.foco(c, t, b1 + 1.6, 0.4, lambda a: txt_lado(c, GK, GE, "8 m", (GK[0] - 400, 600), 64, TINTA, a))
        E.angulo(c, t, b1, GK, GS, GE, r=80)
        if t >= a1:  # a pessoa andando
            if t < b1 + 0.3:
                pos = (lerp(GS[0], GK[0], p1), GS[1])
            else:
                pos = (GK[0], lerp(GK[1], GE[1], p2))
            c.drawCircle(pos[0], pos[1], 20, M.paint(COR))
        # o caminho reto de volta
        if t >= c1:
            M.line(c, *GE, *GS, COR, ep(t, c1, 0.3), 7, dash=E.TRACO, progress=ease_io(prog(t, c1, 0.8)))
        G = (GK[0], GK[1])
        E.saida(c, t, e1, lambda: E.foco(c, t, c1 + 0.6, 0.4, lambda a: txt_lado(c, GE, GS, "?", G, 110, COR, a)))
        E.foco(c, t, e1, 0.4, lambda a: txt_lado(c, GE, GS, "10 m", G, 72, COR, a))
        # texto da direita
        E.frase(c, t, c1, ps("que distância", "i", 76), X, 260, "center", 0.12)
        E.frase(c, t, c1 + 0.6, ps("da", "i", 76) + [("partida?", "g", 84, COR)], X, 360, "center", 0.12)
        fcen(c, t, d1, "6 + 8 = 14", X, 560, 100, ERRADO)
        E.risco(c, X - 260, 530, X + 260, 520, t, d1 + 0.5, ERRADO, 12)
        bola_txt(c, t, e1, "10 m", X, 790, 130, 90)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        tc = lerp(ta, tb, 0.7)
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.25), [("qualquer lado", "g", 104, COR)], XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.45), ps("do triângulo", "i", 96), XE, 590, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), [("retângulo", "g", 104)], XE, 720, passo=0.14)
        E.frase(c, t, tc, ps("conhecendo os outros", "i", 70, TINTA2), XE, 850, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.2, ps("você precisa de", "i", 80, COR), XE, 190, passo=0.12)
    xg = XE + E.larg("você precisa de", "i", 80) + 30
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3 coisas", xg, 190, 84, "g", COR, a))
    itens = (("b", None, "triângulo retângulo:", "tem um ângulo de 90°"),
             ("c", None, "raiz quadrada:", "vezes ela mesma dá o de dentro"),
             ("d", "x^2 = 100", None, "x = 10 ou x = −10"))
    for i, (k, form, tit, sub) in enumerate(itens):
        y = 380 + i * 220
        ti = C[f"s03.{k}"]
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 50, y - 28, 50, a=a),
                                                   centro(c, str(i + 1), XE + 50, y - 6, 60, "g", BR, a)))
        if form:
            E.formula_em(c, t, ti + 0.1, form, XE + 140, y, 80, "g", TINTA)
            E.formula_em(c, t, ti + 1.2, "→  " + sub, XE + 540, y, 70, "g", COR)
        else:
            E.frase(c, t, ti + 0.1, [(tit, "g", 70)], XE + 140, y)
            E.frase(c, t, ti + 0.7, ps(sub, "i", 64, TINTA2), XE + 140, y + 80, passo=0.1)
    # o triângulo do item 1, à direita
    R, P, Q = (1500, 470), (1760, 470), (1500, 290)
    E.foco(c, t, C["s03.b"] + 0.4, 0.5, lambda a: E.triangulo(c, 99, 0, P, R, Q, vertices=None, retos=(1,), preenche=0.12, d=0.01))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), XE, 990, "left", 0.12)


# ---------------- os nomes ----------------
NR, NB, NA = (300, 870), (300 + 4 * 150, 870), (300, 870 - 3 * 150)
NG = ((NR[0] + NB[0] + NA[0]) / 3, (NR[1] + NB[1] + NA[1]) / 3)


def b_nomes(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    X = 1420
    E.frase(c, t, C["s04"], ps("primeiro,", "i", 84) + [("os nomes", "g", 90, COR)], X, 200, "center", 0.14)
    E.triangulo(c, t, C["s04"] + 0.2, NA, NR, NB, vertices=None, retos=(1,), preenche=0.06)
    # catetos: os dois lados do ângulo reto
    q = ease_io(prog(t, a4, 0.6))
    grosso(c, NR, NA, TINTA2, 1.0, 14, q)
    grosso(c, NR, NB, TINTA2, 1.0, 14, q)
    E.foco(c, t, a4 + 0.3, 0.4, lambda a: (txt_lado(c, NR, NA, "cateto", NG, 54, TINTA2, a),
                                           txt_lado(c, NR, NB, "cateto", NG, 54, TINTA2, a)))
    # hipotenusa: de frente para o reto
    grosso(c, NA, NB, COR, 1.0, 14, ease_io(prog(t, b4, 0.6)))
    E.foco(c, t, b4 + 0.3, 0.4, lambda a: txt_lado(c, NA, NB, "hipotenusa", NG, 62, COR, a))
    if t >= b4:  # a seta do reto até a hipotenusa: "de frente"
        k = ep(t, b4, 0.5) * (1 - ep(t, c4, 0.4))
        M.arrow(c, NR[0] + 70, NR[1] - 70, NG[0] + 60, NG[1] - 40, COR, k, 5, 18, k)
    E.frase(c, t, a4, [("catetos:", "g", 76, TINTA2)], X, 400, "center")
    E.frase(c, t, a4 + 0.5, ps("formam o ângulo reto", "i", 62), X, 480, "center", 0.1)
    E.frase(c, t, b4, [("hipotenusa:", "g", 76, COR)], X, 620, "center")
    E.frase(c, t, b4 + 0.5, ps("de frente para o reto", "i", 62), X, 700, "center", 0.1)
    E.foco(c, t, c4, 0.5, lambda a: E.pilula(c, "o lado mais comprido", X, 880, 60, "g", a=a, cor=E.SOBRE))


# ---------------- lajotas ----------------
U = 76
LR = (190 + 3 * U, 130 + 7 * U)          # o reto
LA = (LR[0], LR[1] - 3 * U)              # cateto 3, para cima
LB = (LR[0] + 4 * U, LR[1])              # cateto 4, para a direita
LG = ((LR[0] + LA[0] + LB[0]) / 3, (LR[1] + LA[1] + LB[1]) / 3)
Q3 = quadro(LR, LA, LG, 3)
Q4 = quadro(LR, LB, LG, 4)
Q5 = quadro(LA, LB, LG, 5)
# 3x3 no canto do quadrado da hipotenusa e o 16 em L em volta
DESTINO3 = [(i, j) for j in range(3) for i in range(3)]
DESTINO4 = [(i, j) for j in range(5) for i in range(5) if not (i < 3 and j < 3)]
assert len(DESTINO4) == 16


def b_lajotas(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    X = 1440
    # quadrados com a grade
    for q, ti in ((Q3, c5), (Q4, c5 + 0.4), (Q5, c5 + 0.8)):
        grade_q(c, q, ease_io(prog(t, ti, 0.8)), ep(t, ti + 0.6, 0.5))
    E.triangulo(c, t, C["s05"], LA, LR, LB, vertices=None, retos=(1,), preenche=0.1)
    E.foco(c, t, a5, 0.4, lambda a: (txt_lado(c, LR, LA, "3", LG, 60, TINTA, a, dentro=True),
                                     txt_lado(c, LR, LB, "4", LG, 60, TINTA, a, dentro=True)))
    # o 5 nasce encostado na hipotenusa e sai junto com o quadrado dela, até a borda de fora
    sq = ease_io(prog(t, c5 + 0.8, 0.8))
    m5 = (Q5["centro"][0] + Q5["n"][0] * Q5["L"] * (sq - 0.5), Q5["centro"][1] + Q5["n"][1] * Q5["L"] * (sq - 0.5))
    E.foco(c, t, b5, 0.4, lambda a: E._cola(c, "5", *m5, *Q5["n"], 22, 64, "b", COR, a))
    # lajotas: 9, 16 e as 25 casas da hipotenusa
    if t >= c6:
        m = 0
        for j in range(5):
            for i in range(5):
                k = ep(t, c6 + 0.04 * m, 0.25)
                ladrilho(c, *Q5["cel"](i, j), Q5["s"], Q5["ang"], CINZA, k, 1.0, 0.5)
                m += 1
    if t < d6:
        enche(c, t, a6 + 0.3, Q3, COR, 0.09)
        enche(c, t, b6 + 0.3, Q4, AMBAR, 0.06)
    else:
        n3 = [(i, j) for j in range(3) for i in range(3)]
        n4 = [(i, j) for j in range(4) for i in range(4)]
        for m, (de, para) in enumerate(zip(n3, DESTINO3)):
            voo(c, t, d6 + 0.2 + 0.05 * m, 0.7, (Q3, *de), (Q5, *para), COR)
        for m, (de, para) in enumerate(zip(n4, DESTINO4)):
            voo(c, t, d6 + 0.8 + 0.04 * m, 0.7, (Q4, *de), (Q5, *para), AMBAR)
    # o total no meio de cada quadrado
    for q, ti, s, sai in ((Q3, a6 + 1.2, "9", d6 + 0.2), (Q4, b6 + 1.2, "16", d6 + 0.8)):
        E.saida(c, t, sai, lambda q=q, ti=ti, s=s: E.foco(c, t, ti, 0.4, lambda a: centro(c, s, q["centro"][0], q["centro"][1] + 30, 84, "g", BR, a)))
    E.foco(c, t, c6 + 1.1, 0.4, lambda a: centro(c, "25", Q5["centro"][0], Q5["centro"][1] + 34, 96, "g", TINTA, a * (1 - ep(t, d6, 0.3))))
    E.foco(c, t, d6 + 2.2, 0.4, lambda a: E.pilula(c, "9 + 16 = 25", *Q5["centro"], 50, "g", fundo=TINTA, a=a))
    # as contas, à direita
    E.frase(c, t, c5, ps("um", "i", 76) + [("piso quadrado", "g", 76, COR)], X, 200, "center", 0.12)
    E.frase(c, t, c5 + 0.7, ps("em cada lado", "i", 76), X, 300, "center", 0.12)
    fcen(c, t, a6, "3 × 3 = 9", X, 470, 90, COR)
    fcen(c, t, b6, "4 × 4 = 16", X, 600, 90, AMBAR)
    fcen(c, t, c6, "5 × 5 = 25", X, 730, 90)
    E.foco(c, t, d6, 0.5, lambda a: E.caixa_pontilhada(c, X - 330, 830, 660, 150, a, COR, prog_=ep(t, d6, 0.6)))
    fcen(c, t, d6 + 0.1, "9 + 16 = 25", X, 940, 96, COR)


# ---------------- a regra ----------------
RR, RB, RA = (300, 880), (300 + 4 * 140, 880), (300, 880 - 3 * 140)
RG = ((RR[0] + RB[0] + RA[0]) / 3, (RR[1] + RB[1] + RA[1]) / 3)


def tri_abc(c, t, t0, ta, tb, a=1.0, hip_cor=True):
    """o triângulo da regra: hipotenusa a (em COR), catetos b e c"""
    def fig(k):
        E.triangulo(c, 99, 0, RA, RR, RB, vertices=None, retos=(1,), preenche=0.06, d=0.01)
    E.foco(c, t, t0, 0.6, fig)
    if hip_cor:
        grosso(c, RA, RB, COR, a, 12, ease_io(prog(t, ta, 0.5)))
    E.foco(c, t, ta + 0.2, 0.4, lambda k: txt_lado(c, RA, RB, "a", RG, 90, COR, k * a))
    E.foco(c, t, tb, 0.4, lambda k: (txt_lado(c, RR, RA, "b", RG, 90, TINTA, k * a), txt_lado(c, RR, RB, "c", RG, 90, TINTA, k * a)))


def b_regra(c, t, C, b):
    a7, b7, c7, d7, e7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    X = 1400

    def regra():
        tri_abc(c, t, C["s07"], d7, e7)
        E.frase(c, t, a7, ps("teorema de", "i", 84), X, 200, "center", 0.14)
        E.frase(c, t, a7 + 0.5, [("Pitágoras", "g", 120, COR)], X, 330, "center")
        E.formula_em(c, t, b7, "hipotenusa^2 =", X, 470, 64, "g", COR, "center")
        E.formula_em(c, t, b7 + 1.2, "cateto^2 + cateto^2", X, 560, 64, "g", TINTA, "center")
        E.foco(c, t, c7, 0.5, lambda a: E.caixa_pontilhada(c, X - 380, 650, 760, 190, a, COR, prog_=ep(t, c7, 0.6)))
        fcen(c, t, c7 + 0.1, "a^2 = b^2 + c^2", X, 790, 120, COR)
        E.frase(c, t, d7 + 0.3, [("a", "g", 56, COR)] + ps("= hipotenusa", "i", 56), X, 940, "center", 0.1)
        E.frase(c, t, e7 + 0.3, [("b, c", "g", 56)] + ps("= catetos", "i", 56), X, 1020, "center", 0.1)
    E.saida(c, t, C["s08"], regra)
    if t < C["s08"]:
        return
    # só vale com ângulo reto: o equilátero de lado 5
    T1, T2 = (300, 880), (820, 880)
    T3 = (560, 880 - 520 * math.sqrt(3) / 2)
    E.frase(c, t, C["s08"] + 0.2, ps("só vale com", "i", 76) + [("ângulo reto", "g", 80, COR)], W / 2, 150, "center", 0.12)

    def equi():
        E.triangulo(c, t, a8, T1, T2, T3, vertices=None, lados=("5", "5", "5"), iguais=(1, 1, 1), preenche=0.06,
                    tl=(a8 + 0.6, a8 + 0.7, a8 + 0.8))
        fcen(c, t, b8, "5^2 + 5^2", 1420, 400, 96)
        fcen(c, t, b8 + 0.8, "= 25 + 25 = 50", 1420, 530, 96)
        fcen(c, t, b8 + 2.2, "5^2 = 25", 1420, 700, 96, ERRADO)
        E.foco(c, t, b8 + 2.6, 0.4, lambda a: E.pilula(c, "não dá 50", 1420, 820, 56, "g", fundo=ERRADO, a=a))
    E.saida(c, t, c8 - 0.2, equi)
    if t >= c8 - 0.2:
        tri_abc(c, t, c8 - 0.2, c8, c8 + 0.2)
        fcen(c, t, c8 + 0.2, "a^2 = b^2 + c^2", 1420, 400, 96)
        E.frase(c, t, c8 + 0.9, ps("a soma de dois quadrados", "i", 60), 1420, 500, "center", 0.1)
        E.frase(c, t, c8 + 1.8, ps("passa de cada um", "i", 60), 1420, 580, "center", 0.1)
        fcen(c, t, c8 + 2.6, "a > b   e   a > c", 1420, 730, 90, COR)
        E.foco(c, t, c8 + 3.4, 0.5, lambda a: E.pilula(c, "sempre o maior lado", 1420, 870, 60, "g", a=a, cor=E.SOBRE))


# ---------------- achar a hipotenusa ----------------
HS, HR, HE = (200, 900), (200 + 6 * 70, 900), (200 + 6 * 70, 900 - 8 * 70)
HG = ((HS[0] + HR[0] + HE[0]) / 3, (HS[1] + HR[1] + HE[1]) / 3)


def b_hipotenusa(c, t, C, b):
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    X = 1300
    E.triangulo(c, t, C["s09"], HS, HR, HE, vertices=None, retos=(1,), preenche=0.06)
    E.foco(c, t, a9, 0.4, lambda a: (txt_lado(c, HS, HR, "6", HG, 70, TINTA, a), txt_lado(c, HR, HE, "8", HG, 70, TINTA, a)))
    grosso(c, HE, HS, COR, 1.0, 12, ease_io(prog(t, a9, 0.6)))
    E.saida(c, t, c10, lambda: E.foco(c, t, a9 + 0.4, 0.4, lambda a: txt_lado(c, HE, HS, "a = ?", HG, 70, COR, a)))
    E.foco(c, t, c10, 0.4, lambda a: txt_lado(c, HE, HS, "10", HG, 84, CERTO, a))
    # o caminho da volta, na comparação do fim
    if t >= d10:
        k = ep(t, d10, 0.4)
        grosso(c, HS, HR, AMBAR, k, 12)
        grosso(c, HR, HE, AMBAR, k, 12)

    def soma():
        fcen(c, t, a9 + 0.2, "a^2 = 6^2 + 8^2", X + 150, 230, 96)
        fcen(c, t, b9, "6^2 = 6 × 6 = 36", X + 150, 400, 80, TINTA2)
        fcen(c, t, c9, "8^2 = 8 × 8 = 64", X + 150, 530, 80, TINTA2)
        fcen(c, t, d9, "a^2 = 36 + 64 = 100", X + 150, 720, 84, COR)
    E.saida(c, t, a10 - 0.1, soma)
    if t >= a10 - 0.1:
        fcen(c, t, a10, "a^2 = 100", X + 150, 230, 110)
        fcen(c, t, lerp(a10, b10, 0.5), "a = 10   ou   a = −10", X + 150, 390, 80, TINTA2)
        if t >= b10:
            wt = E.formula(None, "a = 10   ou   a = −10", 0, 0, 80, "g", a=0); wn = E.formula(None, "−10", 0, 0, 80, "g", a=0)
            E.risco(c, X + 150 + wt / 2 - wn - 14, 372, X + 150 + wt / 2 + 14, 362, t, b10, ERRADO, 10)
        E.frase(c, t, b10 + 0.3, ps("medida não é", "i", 60) + [("negativa", "g", 62, ERRADO)], X + 150, 480, "center", 0.1)
        bola_txt(c, t, c10, "a = 10", X + 150, 680, 120, 76)
        fcen(c, t, d10, "10 < 6 + 8 = 14", X + 150, 900, 80, AMBAR)
        E.frase(c, t, d10 + 0.6, ps("o caminho reto é mais curto", "i", 52, TINTA2), X + 150, 980, "center", 0.1)


# ---------------- achar um cateto ----------------
KP, KR, KT = (520 - 5 * 50, 900), (520, 900), (520, 900 - 12 * 50)
KG = ((KP[0] + KR[0] + KT[0]) / 3, (KP[1] + KR[1] + KT[1]) / 3)


def tri_cateto(c, t, t0, tb, tc, x_txt=lambda tt: "x", hip=True):
    """hipotenusa 13, cateto 5 embaixo e o cateto x de pé"""
    E.triangulo(c, t, t0, KP, KR, KT, vertices=None, retos=(1,), preenche=0.06)
    if hip:
        grosso(c, KT, KP, COR, 1.0, 12, ease_io(prog(t, tb, 0.5)))
    E.foco(c, t, tb, 0.4, lambda a: txt_lado(c, KT, KP, "13", KG, 76, COR, a))
    E.foco(c, t, tc, 0.4, lambda a: txt_lado(c, KP, KR, "5", KG, 76, TINTA, a))
    grosso(c, KR, KT, AMBAR, ep(t, t0 + 0.6, 0.4), 12)
    E.foco(c, t, t0 + 0.6, 0.4, lambda a: txt_lado(c, KR, KT, x_txt(t), KG, 76, AMBAR, a))


def b_cateto(c, t, C, b):
    a11, b11, c11, d11, e11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"]
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    X = 1340

    def conta():
        tri_cateto(c, t, a11, b11, c11, lambda tt: "12" if tt >= c12 else "x")
        E.frase(c, t, a11, ps("falta", "i", 76) + [("um cateto", "g", 80, AMBAR)], X, 150, "center", 0.12)
        el, dr = eq(c, t, d11, "13^2", "5^2 + x^2", X, 300, 90)
        eq(c, t, e11, "169", "25 + x^2", X, 440, 90)
        if t >= a12:
            for cx in (X - 40 - E.formula(None, "169", 0, 0, 90, "g", a=0) / 2, X + 40 + E.formula(None, "25", 0, 0, 90, "g", a=0) / 2):
                E.foco(c, t, a12 + 0.2, 0.4, lambda a, cx=cx: E.pilula(c, "− 25", cx, 530, 44, "g", fundo=ERRADO, a=a))
        eq(c, t, b12, "x^2", "169 − 25 = 144", X - 200, 680, 84)
        bola_txt(c, t, c12, "x = 12", X - 200, 860, 110, 70, AMBAR)
        E.foco(c, t, d12, 0.5, lambda a: E.formula(c, "25 + 144 = 169", X + 260, 850, 58, "g", CERTO, a, "center"))
        E.foco(c, t, d12 + 1.2, 0.4, lambda a: E.selo(c, X + 260, 950, 42 * ease_back(prog(t, d12 + 1.2, 0.4)), True, a))
    E.saida(c, t, C["s13"] - 0.1, conta)
    if t < C["s13"] - 0.1:
        return
    # os dois casos lado a lado
    for i, (ti, tit, verbo, form, cor) in enumerate(((a13, "hipotenusa", "some", "a^2 = b^2 + c^2", COR),
                                                    (b13, "cateto", "subtraia", "b^2 = a^2 − c^2", AMBAR))):
        cx = 520 + i * 880
        E.foco(c, t, ti, 0.5, lambda a, cx=cx: E.caixa_pontilhada(c, cx - 380, 200, 760, 470, a, cor, prog_=ep(t, ti, 0.6)))
        E.frase(c, t, ti, ps("para achar a", "i", 60), cx, 300, "center", 0.1)
        E.frase(c, t, ti + 0.4, [(tit, "g", 84, cor)], cx, 410, "center")
        E.frase(c, t, ti + 0.9, [(verbo, "g", 96)], cx, 540, "center")
        fcen(c, t, ti + 1.4, form, cx, 630, 66, TINTA2)
    E.frase(c, t, c13, ps("nos dois:", "i", 76, TINTA2), 640, 880, "center", 0.12)
    E.frase(c, t, c13 + 0.4, ps("tire a", "i", 84) + [("raiz", "g", 100, COR)] + ps("no fim", "i", 84), 1180, 880, "center", 0.14)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    X = W / 2

    def soma():
        E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)] + ps("com este erro", "i", 90), X, 150, "center", 0.14)
        E.frase(c, t, a14, ps("falta um cateto e a pessoa", "i", 64) + [("soma", "g", 70, ERRADO)], X, 280, "center", 0.1)
        fcen(c, t, b14, "169 + 25 = 194", X, 430, 110, ERRADO)
        for i, (s, ti) in enumerate((("13^2 = 169", c14), ("14^2 = 196", c14 + 1.6))):
            fcen(c, t, ti, s, X - 360 + i * 720, 600, 90)
        vx = E.reta(c, t, d14 - 0.3, 560, 1360, 800, 13, 14, (13, 14), size=60)
        v = 13 + (194 - 169) / (196 - 169)
        if t >= d14:
            k = ease_back(prog(t, d14 + 0.3, 0.4))
            c.drawCircle(vx(v), 800, 18 * k, M.paint(ERRADO))
            E.foco(c, t, d14 + 0.4, 0.4, lambda a: E.formula(c, "r{194}", vx(v), 740, 66, "g", ERRADO, a, "center"))
        E.frase(c, t, d14 + 1.0, ps("entre 13 e 14:", "i", 60) + [("maior que 13", "g", 62, ERRADO)], X, 990, "center", 0.1)
    E.saida(c, t, C["s15"] - 0.1, soma)
    if t < C["s15"] - 0.1:
        return
    tri_cateto(c, t, C["s15"] - 0.1, C["s15"] - 0.1, C["s15"] - 0.1, lambda tt: "x")
    X2 = 1340
    E.frase(c, t, a15, ps("um cateto", "i", 72) + [("maior", "g", 78, ERRADO)], X2, 200, "center", 0.12)
    E.frase(c, t, a15 + 0.6, ps("que a hipotenusa?", "i", 72), X2, 300, "center", 0.12)
    E.foco(c, t, a15 + 1.4, 0.4, lambda a: E.pilula(c, "impossível", X2, 420, 64, "g", fundo=ERRADO, a=a))
    E.frase(c, t, b15, [("hipotenusa", "g", 70, COR)] + ps("= o maior lado", "i", 66), X2, 620, "center", 0.12)
    E.frase(c, t, c15, [("cateto", "g", 70, AMBAR)] + ps("menor que ela", "i", 66), X2, 760, "center", 0.12)
    fcen(c, t, c15 + 0.8, "x < 13", X2 - 80, 920, 90, CERTO)
    E.foco(c, t, c15 + 1.2, 0.4, lambda a: E.selo(c, X2 + 170, 890, 56 * ease_back(prog(t, c15 + 1.2, 0.4)), True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a16, b16, c16, d16, e16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"]
    a17, b17, c17, d17, e17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"], C["s17.e"]
    X = W / 2

    def um():
        E.frase(c, t, C["s16"] + 0.2, [("atalho", "g", 90, CLARO)] + ps("para achar cateto", "i", 80, BR), X, 160, "center", 0.12)
        E.frase(c, t, a16, ps("em vez de dois quadrados:", "i", 64, CLARO), X, 280, "center", 0.1)
        E.frase(c, t, a16 + 1.2, [("soma", "g", 80, BR)] + ps("vezes", "i", 72, CLARO) + [("diferença", "g", 80, BR)], X, 380, "center", 0.12)
        fcen(c, t, b16, "13 + 5 = 18", 560, 560, 100, BR)
        fcen(c, t, c16, "13 − 5 = 8", 1360, 560, 100, BR)
        fcen(c, t, d16, "18 × 8 = 144", X, 740, 110, CLARO)
        E.formula_em(c, t, e16, "r{144} =", X - 40, 950, 90, "g", BR, "right")
        bola_txt(c, t, e16 + 0.3, "12", X + 90, 920, 90, 90)
    E.saida(c, t, C["s17"] - 0.1, um)
    if t < C["s17"] - 0.1:
        return

    def dois():
        E.frase(c, t, C["s17"], ps("por que funciona?", "i", 70, CLARO), X, 150, "center", 0.12)
        fcen(c, t, a17, "13^2 − 5^2", 560, 320, 100, BR)
        E.frase(c, t, a17 + 0.6, ps("diferença de dois quadrados", "i", 54, CLARO), 560, 420, "center", 0.1)
        fcen(c, t, b17, "= (13 + 5) · (13 − 5)", 1300, 320, 90, CLARO)
        E.frase(c, t, b17 + 0.6, ps("soma vezes diferença", "i", 54, CLARO), 1300, 420, "center", 0.1)
    E.saida(c, t, c17 - 1.5, dois)
    if t >= c17 - 1.5:
        E.frase(c, t, c17 - 1.4, ps("números grandes e próximos:", "i", 64, CLARO), X, 170, "center", 0.1)
        E.formula_em(c, t, c17 - 1.4, "hipotenusa 25,  cateto 24", X, 290, 76, "g", BR, "center")
        fcen(c, t, c17, "25 + 24 = 49     25 − 24 = 1", X, 450, 80, CLARO)
        fcen(c, t, c17 + 1.0, "49 × 1 = 49", X, 590, 100, BR)
        E.formula_em(c, t, d17, "r{49} =", X - 40, 780, 90, "g", BR, "right")
        bola_txt(c, t, d17 + 0.2, "7", X + 90, 750, 90, 90)
        E.foco(c, t, e17, 0.5, lambda a: E.pilula(c, "não serve para a hipotenusa", X, 930, 60, "g", fundo=ERRADO, a=a))
        E.frase(c, t, e17 + 1.2, ps("lá, os quadrados se", "i", 54, CLARO) + [("somam", "g", 58, BR)], X, 1030, "center", 0.1)


# ---------------- questão ----------------
PP = (760, 930)                 # pé do poste
PT = (760, 930 - 15 * 48)       # alto do poste (15 m: a figura não mente)
PC = (760 - 8 * 48, 930)        # onde o cabo se prende
PG = ((PP[0] + PT[0] + PC[0]) / 3, (PP[1] + PT[1] + PC[1]) / 3)


def poste(c, t, t0, tr, tc, tm, th, h_txt=lambda tt: "h = ?", h_cor=lambda tt: COR):
    """chão, poste, cabo e as medidas: tr = ângulo reto, tc = cabo, tm = 8 m, th = altura"""
    if t < t0:
        return
    q = ease_io(prog(t, t0, 0.6))
    M.line(c, 120, 930, lerp(120, 1040, q), 930, TINTA, 1.0, 6)
    for i in range(14):
        x = 140 + i * 66
        M.line(c, x, 940, x - 22, 970, TINTA2, q * 0.6, 3)
    alt = ease_io(prog(t, t0 + 0.3, 0.7))
    if alt > 0:
        M.rrect(c, PP[0] - 13, lerp(PP[1], PT[1], alt), 26, (PP[1] - PT[1]) * alt, 6, "#5A5A66", 1.0)
        if alt >= 1:
            c.drawCircle(PT[0], PT[1], 14, M.paint(TINTA))
    E.angulo(c, t, tr, PP, PC, (PP[0], PP[1] - 100), r=70)
    if t >= tc:
        M.line(c, *PT, *PC, TINTA, 1.0, 6, progress=ease_io(prog(t, tc, 0.6)))
        E.foco(c, t, tc + 0.4, 0.4, lambda a: txt_lado(c, PT, PC, "17 m", PG, 70, TINTA, a))
    E.foco(c, t, tm, 0.4, lambda a: (M.line(c, PC[0], 1000, PP[0], 1000, TINTA2, a, 3),
                                     centro(c, "8 m", (PC[0] + PP[0]) / 2, 1060, 64, "b", TINTA, a)))
    E.foco(c, t, th, 0.4, lambda a: E.escreve(c, h_txt(t), PP[0] + 50, (PP[1] + PT[1]) / 2 + 24, 72, "g", h_cor(t), a))


def b_questao(c, t, C, b):
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    X = 1500
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 140, passo=0.12)
    poste(c, t, a18 - 0.3, a18 + 0.4, b18 - 0.4, c18, d18)
    E.saida(c, t, C["s19.a"] - 0.1, lambda: E.frase(c, t, a18 + 0.5, ps("poste em pé:", "i", 64) + [("90°", "g", 70, COR)], X, 360, "center", 0.12))
    pergunta(c, t, [(b18, ps("cabo de", "i", 64) + [("17 m", "g", 70)]),
                    (c18, ps("preso a", "i", 64) + [("8 m", "g", 70)] + ps("do pé", "i", 64)),
                    (d18, ps("altura", "i", 64) + [("h = ?", "g", 72, COR)])], C["s19.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a20, b20 = C["s20.a"], C["s20.b"]
    a21, b21, c21, d21, e21 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"], C["s21.e"]
    a22, b22, c22, d22 = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"]
    X = 1440
    t0 = C["s20"] - 1.2
    poste(c, t, t0, t0, t0, t0, t0, lambda tt: "15 m" if tt >= e21 else "h", lambda tt: CERTO if tt >= e21 else AMBAR)
    grosso(c, PT, PC, COR, 1.0, 12, ease_io(prog(t, a20, 0.6)))
    grosso(c, PP, PT, AMBAR, ep(t, b20, 0.4), 10)

    def um():
        E.frase(c, t, a20, ps("cabo =", "i", 70) + [("hipotenusa", "g", 76, COR)], X, 380, "center", 0.12)
        E.frase(c, t, b20, ps("altura =", "i", 70) + [("cateto", "g", 76, AMBAR)], X, 540, "center", 0.12)
        E.foco(c, t, b20 + 1.2, 0.5, lambda a: E.pilula(c, "subtração", X, 700, 64, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, a21 - 0.1, um)

    def dois():
        fcen(c, t, a21, "17^2 = 289", X, 200, 84)
        fcen(c, t, b21, "8^2 = 64", X, 330, 84)
        fcen(c, t, c21, "289 − 64 = 225", X, 480, 90, AMBAR)
        fcen(c, t, d21, "h = r{225} = 15", X, 640, 90)
        bola_txt(c, t, e21, "15 m", X, 850, 120, 84, CERTO)
    E.saida(c, t, C["s22"] - 0.1, dois)
    if t >= C["s22"] - 0.1:
        E.frase(c, t, C["s22"], ps("pelo atalho", "i", 70, COR), X, 170, "center", 0.12)
        fcen(c, t, a22, "17 + 8 = 25", X, 320, 84)
        fcen(c, t, b22, "17 − 8 = 9", X, 450, 84)
        fcen(c, t, c22, "25 × 9 = 225", X, 600, 90, AMBAR)
        fcen(c, t, d22, "15 < 17", X - 90, 820, 100, CERTO)
        E.foco(c, t, d22 + 0.8, 0.4, lambda a: E.selo(c, X + 190, 790, 62 * ease_back(prog(t, d22 + 0.8, 0.4)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s23.a", None, "a^2 = b^2 + c^2", COR), ("s23.b", "hipotenusa:", "some", COR), ("s23.c", "cateto:", "subtraia", AMBAR))
        for i, (k, tit, s, cor) in enumerate(itens):
            y = 400 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 420, y - 30, 56, a=a),
                                                         centro(c, str(i + 1), 420, y - 7, 64, "g", BR, a)))
            if tit:
                E.frase(c, t, C[k] + 0.1, [(tit, "i", 84), (s, "g", 90, cor)], 520, y, passo=0.3)
            else:
                E.formula_em(c, t, C[k] + 0.1, s, 520, y, 96, "g", cor)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"] + 0.2, ps("próxima aula", "i", 84), XE, 260)
    E.frase(c, t, C["s24.a"], [("Ternos", "g", 130, COR)], XE, 400)
    E.frase(c, t, C["s24.a"] + 0.3, [("pitagóricos", "g", 130, COR)], XE, 530)
    E.frase(c, t, C["s24.b"], [("3, 4 e 5", "g", 84)] + ps("sem conta", "i", 76), XE, 670, passo=0.15)
    E.frase(c, t, C["s24.c"], ps("e a", "i", 76) + [("escada", "g", 80)] + ps("na parede", "i", 76), XE, 790, passo=0.12)
    E.foco(c, t, C["s24.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1630, p), lerp(720, 425, p), ep(t, C["s24.d"] + 0.2, 0.4))
    E.frase(c, t, C["s24.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nomes=b_nomes, lajotas=b_lajotas, regra=b_regra, hipotenusa=b_hipotenusa,
              cateto=b_cateto, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
