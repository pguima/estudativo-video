"""Visual — Estudativo · MAT-ANG-017: diagonal do quadrado (d = ℓ√2; lado 5: 5√2 ≈ 7) e altura do equilátero (h = ℓ√3/2; lado 6: 3√3).
Linguagem da geometria plana (MAT-ANG-001 a 020, e MAT-ANG-015/016 para Pitágoras): lados em tinta; lados iguais com tracinhos;
a hipotenusa da vez em COR (índigo), o cateto conhecido em TINTA2 e o procurado em AMBAR; ângulo reto = quadradinho;
medidas e raízes na fonte pesada (√2 ≈ 1,4 e √3 ≈ 1,7, as de MAT-POT-009); erro em vermelho, certo em verde; resposta na
esfera; atalho no palco escuro.
O quadrado de lado 1 ampliado para 5 e para 10 sai do mesmo canto (três quadrados encaixados, com as diagonais na mesma
reta): é o "esse, ampliado" da fala. O equilátero de lado 2 fica ao lado do de lado 6, na mesma escala.
Peças locais: txt_lado(), grosso(), metade() (a metade do equilátero que vira triângulo retângulo), equi() (equilátero com
altura e base partida), quadrado_d() (quadrado com a diagonal), pergunta().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-017_diagonal_do_quadrado_e_altura_do_equilatero.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("diagonal", "altura", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
R2, R3 = 1.4, 1.7
assert 25 + 25 == 50 == 25 * 2 and round(5 * R2, 1) == 7.0 and 5 * math.sqrt(2) < 10 and 1 + 1 == 2
assert 36 - 9 == 27 == 9 * 3 and 4 - 1 == 3 and 6 // 2 == 3 and abs(6 * math.sqrt(3) / 2 - 3 * math.sqrt(3)) < 1e-9
assert round(6 * R3, 1) == 10.2 and 6 * math.sqrt(3) > 10 and 3 * math.sqrt(3) < 6 and round(3 * R3, 1) == 5.1
assert 16 - 4 == 12 == 4 * 3 and round(2 * R3, 1) == 3.4 < 3.5 and abs(4 * math.sqrt(2) / math.sqrt(2) - 4) < 1e-9


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


def pinta(c, pts, cor, a, alfa=0.18):
    if a > 0:
        path = skia.Path(); path.addPoly(pts, True)
        c.drawPath(path, M.paint(cor, alfa * a))


def quadrado_d(c, t, t0, x, y, l, lado=None, tl=None, d=0.9):
    """quadrado (x, y = canto de cima à esquerda), lado escrito embaixo, quatro retos e os tracinhos"""
    E.quadrado(c, t, t0, x, y, l, lado, retos=(0, 1, 2, 3), preenche=0.04, d=d, tl=None if tl is None else (tl, tl, tl, tl))


def equi(c, t, t0, B1, B2, lado="6", tl=None, d=0.9):
    """equilátero de base B1-B2 (o topo para cima), com os três tracinhos e a medida do lado esquerdo"""
    T = ((B1[0] + B2[0]) / 2, B1[1] - math.dist(B1, B2) * math.sqrt(3) / 2)
    E.triangulo(c, t, t0, B1, B2, T, vertices=None, lados=(None, None, lado), iguais=(1, 1, 1), preenche=0.05, d=d,
                tl=None if tl is None else (tl, tl, tl))
    return T


def pergunta(c, t, linhas, rel, X=1500, y0=780):
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, y0 + i * 95, "center", 0.12)
    E.relogio(c, t, rel, X, 380, 170)


# ---------------- gancho ----------------
SQ = (260, 300, 520)   # x, y, lado em px (lado 5)


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    x, y, l = SQ
    A, Bq, Cq, D = (x, y + l), (x + l, y + l), (x + l, y), (x, y)
    X = 1420

    def um():
        quadrado_d(c, t, a1, x, y, l, "5")
        if t >= b1:
            M.line(c, *A, *Cq, COR, 1.0, 8, dash=E.TRACO, progress=ease_io(prog(t, b1, 0.8)))
        E.saida(c, t, d1, lambda: E.foco(c, t, b1 + 0.6, 0.4, lambda a: txt_lado(c, A, Cq, "d = ?", ((A[0] + Bq[0] + Cq[0]) / 3, (A[1] + Bq[1] + Cq[1]) / 3), 72, COR, a)))
        E.foco(c, t, d1, 0.4, lambda a: txt_lado(c, A, Cq, "5r{2}", ((A[0] + Bq[0] + Cq[0]) / 3, (A[1] + Bq[1] + Cq[1]) / 3), 72, COR, a))
        if t >= c1:  # a volta pelos lados
            k = ep(t, c1, 0.4) * (1 - ep(t, d1, 0.4))
            grosso(c, A, Bq, AMBAR, k, 12)
            grosso(c, Bq, Cq, AMBAR, k, 12)
        E.frase(c, t, a1 + 0.3, ps("quadrado de lado", "i", 70) + [("5", "g", 80, COR)], X, 260, "center", 0.12)
        E.frase(c, t, b1, ps("a", "i", 70) + [("diagonal", "g", 80, COR)] + ps("mede?", "i", 70), X, 380, "center", 0.12)
        fcen(c, t, c1, "5 + 5 = 10", X, 560, 100, ERRADO)
        E.risco(c, X - 250, 530, X + 250, 520, t, d1 - 0.2, ERRADO, 12)
        bola_txt(c, t, d1, "5r{2}", X - 140, 790, 130, 90)
        E.foco(c, t, d1 + 1.0, 0.5, lambda a: (E.formula(c, "≈ 7", X + 60, 820, 96, "g", COR, a, "left"),
                                               E.escreve(c, "um pouco mais", X + 50, 900, 52, "i", TINTA2, a)))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb + 1.0, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb + 1.0, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("diagonal", "g", 110, COR)] + ps("do quadrado", "i", 90), XE, 460, passo=0.14)
        E.frase(c, t, tb, [("altura", "g", 110, COR)] + ps("do equilátero", "i", 90), XE, 620, passo=0.14)
        E.foco(c, t, tb + 1.4, 0.5, lambda a: (centro(c, "numa conta", 1500, 545, 76, "i", E.SOBRE, a),
                                               centro(c, "só", 1500, 640, 100, "g", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.2, ps("você precisa de", "i", 80, COR), XE, 190, passo=0.12)
    xg = XE + E.larg("você precisa de", "i", 80) + 30
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3 coisas", xg, 190, 84, "g", COR, a))
    itens = (("b", "teorema de Pitágoras", ("a^2 = b^2 + c^2", None)),
             ("c", "isósceles:", (None, "a linha do topo é altura e mediana")),
             ("d", "simplificar raiz", ("r{72} = 6r{2}", None)))
    for i, (k, tit, (form, sub)) in enumerate(itens):
        y = 380 + i * 210
        ti = C[f"s03.{k}"]
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 50, y - 28, 50, a=a), centro(c, str(i + 1), XE + 50, y - 6, 60, "g", BR, a)))
        E.frase(c, t, ti + 0.1, [(tit, "g", 70)], XE + 140, y)
        if form:
            w = E.larg(tit, "g", 70)
            E.formula_em(c, t, ti + 0.8, form, XE + 140 + w + 60, y, 70, "g", COR)
        else:
            E.frase(c, t, ti + 0.8, ps(sub, "i", 60, TINTA2), XE + 140, y + 76, passo=0.08)
    # o isósceles do item 2, à direita
    B1, B2, T = (1480, 640), (1760, 640), (1620, 380)
    if t >= C["s03.c"] + 0.3:
        E.triangulo(c, t, C["s03.c"] + 0.3, B1, B2, T, vertices=None, iguais=(0, 1, 1), preenche=0.06)
        M.line(c, *T, 1620, 640, COR, 1.0, 6, dash=E.TRACO, progress=ease_io(prog(t, C["s03.c"] + 1.2, 0.6)))
        E.angulo(c, t, C["s03.c"] + 1.8, (1620, 640), B2, T, r=30)
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), XE, 1000, "left", 0.12)


# ---------------- diagonal ----------------
DX, DY, DL = 200, 260, 520
DA, DB, DC, DD = (DX, DY + DL), (DX + DL, DY + DL), (DX + DL, DY), (DX, DY)   # embaixo esq, embaixo dir, em cima dir, em cima esq
DG = ((DA[0] + DB[0] + DC[0]) / 3, (DA[1] + DB[1] + DC[1]) / 3)
NC = (180, 920)          # canto comum dos quadrados encaixados (s07–s08)
NU = 62                  # px por unidade


def b_diagonal(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    a6, b6 = C["s06.a"], C["s06.b"]
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    a8, b8, c8, d8, e8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"], C["s08.e"]
    X = 1380

    def lado5():
        quadrado_d(c, t, C["s04"] - 0.2, DX, DY, DL)
        if t >= a4:
            M.line(c, *DA, *DC, TINTA, 1.0, 6, progress=ease_io(prog(t, a4, 0.6)))
            pinta(c, [DA, DB, DC], E.COR, ep(t, a4 + 0.4, 0.5))
        k = ep(t, b4, 0.4)
        grosso(c, DA, DB, TINTA2, k, 12)
        grosso(c, DB, DC, TINTA2, k, 12)
        E.foco(c, t, b4 + 0.2, 0.4, lambda a: (txt_lado(c, DA, DB, "5", DG, 70, TINTA2, a), txt_lado(c, DB, DC, "5", DG, 70, TINTA2, a, gap=36)))
        grosso(c, DA, DC, COR, 1.0, 12, ease_io(prog(t, c4, 0.6)))
        E.saida(c, t, d5 + 0.4, lambda: E.foco(c, t, c4 + 0.4, 0.4, lambda a: txt_lado(c, DA, DC, "d", DG, 84, COR, a)))
        E.foco(c, t, d5 + 0.4, 0.4, lambda a: txt_lado(c, DA, DC, "5r{2}", DG, 70, COR, a))
        if t >= b6:  # a volta pelos lados, para comparar
            k2 = ep(t, b6, 0.4)
            grosso(c, DA, DD, AMBAR, k2, 10)
            grosso(c, DD, DC, AMBAR, k2, 10)
        E.frase(c, t, a4, [("2", "g", 76, COR)] + ps("triângulos retângulos", "i", 66), X, 200, "center", 0.12)
        E.frase(c, t, b4, ps("catetos:", "i", 62) + [("os lados", "g", 66, TINTA2)] + ps("hipotenusa:", "i", 62) + [("d", "g", 66, COR)],
                X, 290, "center", 0.12)

        def conta():
            fcen(c, t, a5, "5^2 + 5^2 = 25 + 25 = 50", X, 440, 74)
            fcen(c, t, b5, "d^2 = 50", X, 570, 84)
            fcen(c, t, c5, "50 = 25 × 2", X, 700, 84, TINTA2)
            fcen(c, t, d5, "d = r{25 × 2} = 5r{2}", X, 860, 84, COR)
        E.saida(c, t, C["s06"] - 0.1, conta)
        if t >= C["s06"] - 0.1:
            fcen(c, t, C["s06"], "r{2} ≈ 1,4", X, 470, 90, TINTA2)
            fcen(c, t, a6, "5 × 1,4 = 7", X, 620, 96)
            E.frase(c, t, b6, ps("pouco mais de", "i", 70) + [("7", "g", 80, COR)], X, 790, "center", 0.12)
            E.frase(c, t, b6 + 1.0, ps("menor que", "i", 64) + [("5 + 5 = 10", "g", 70, AMBAR)], X, 900, "center", 0.12)
    E.saida(c, t, C["s07"] - 0.1, lado5)
    if t < C["s07"] - 0.1:
        return
    # quadrados encaixados: lado 1, depois 5 e 10 a partir do mesmo canto
    for lado_, t0, rot, tr in ((1, a7, "r{2}", c7), (5, d7, "5r{2}", a8), (10, d7 + 0.8, "10r{2}", b8)):
        s = lado_ * NU
        k = ease_io(prog(t, t0, 0.8)) if lado_ > 1 else ep(t, t0, 0.4)
        if k <= 0:
            continue
        s_ = s * k if lado_ > 1 else s
        P0, P1, P2, P3 = NC, (NC[0] + s_, NC[1]), (NC[0] + s_, NC[1] - s_), (NC[0], NC[1] - s_)
        pinta(c, [P0, P1, P2, P3], E.COR, 1.0, 0.05 if lado_ > 1 else 0.15)
        E._contorno(c, [P0, P1, P2, P3], 1.0, TINTA if lado_ == 10 or k >= 1 else TINTA2, 6 if lado_ == 1 else 5)
        M.line(c, *P0, *P2, COR, 1.0, 7 if lado_ == 1 else 5)
        if lado_ == 1:
            E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, "1", NC[0] + s / 2, NC[1] + 60, 50, "b", TINTA, a))
        else:
            E.foco(c, t, t0 + 0.6, 0.4, lambda a, s=s, lado_=lado_: centro(c, str(lado_), NC[0] + s - 20, NC[1] + 60, 50, "b", TINTA, a))
        E.foco(c, t, tr, 0.4, lambda a, s=s, rot=rot, lado_=lado_: E.formula(c, rot, NC[0] + s / 2 - 20, NC[1] - s / 2 - 40, 52 if lado_ == 1 else 60, "g", COR, a, "right"))
    fx = 1300

    def sete():
        E.frase(c, t, C["s07"] + 0.1, ps("e com", "i", 70) + [("qualquer lado?", "g", 76, COR)], fx, 200, "center", 0.12)
        fcen(c, t, a7, "lado 1", fx, 340, 80)
        fcen(c, t, b7, "d^2 = 1 + 1 = 2", fx, 470, 84)
        fcen(c, t, c7, "d = r{2}", fx, 600, 96, COR)
        E.frase(c, t, d7, ps("ampliado:", "i", 64) + [("× 5, × 10", "g", 70, AMBAR)], fx, 760, "center", 0.12)
        E.frase(c, t, d7 + 1.0, ps("Pitágoras continua valendo", "i", 58, TINTA2), fx, 850, "center", 0.1)
    E.saida(c, t, C["s08"] - 0.1, sete)
    if t >= C["s08"] - 0.1:
        fcen(c, t, a8, "lado 5  →  d = 5r{2}", fx, 220, 72)
        fcen(c, t, b8, "lado 10  →  d = 10r{2}", fx, 340, 72)
        E.foco(c, t, c8, 0.5, lambda a: E.caixa_pontilhada(c, fx - 300, 430, 600, 200, a, COR, prog_=ep(t, c8, 0.6)))
        fcen(c, t, c8 + 0.1, "d = ℓr{2}", fx, 580, 130, COR)
        E.frase(c, t, d8, [("d", "g", 64, COR)] + ps("= diagonal", "i", 60), fx, 760, "center", 0.1)
        E.frase(c, t, e8, [("ℓ", "g", 64, COR)] + ps("= lado", "i", 60), fx, 850, "center", 0.1)


# ---------------- altura do equilátero ----------------
EU = 100
EB1, EB2 = (200, 900), (200 + 6 * EU, 900)
ET = ((EB1[0] + EB2[0]) / 2, EB1[1] - 6 * EU * math.sqrt(3) / 2)
EM = ((EB1[0] + EB2[0]) / 2, EB1[1])
EG = ((ET[0] + EM[0] + EB2[0]) / 3, (ET[1] + EM[1] + EB2[1]) / 3)
PB1, PB2 = (1000, 900), (1000 + 2 * EU, 900)       # o equilátero de lado 2, na mesma escala
PT = ((PB1[0] + PB2[0]) / 2, PB1[1] - 2 * EU * math.sqrt(3) / 2)
PM = ((PB1[0] + PB2[0]) / 2, PB1[1])
PG = ((PT[0] + PM[0] + PB2[0]) / 3, (PT[1] + PM[1] + PB2[1]) / 3)


def b_altura(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12, c12, d12, e12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    X = 1400
    equi(c, t, a9 - 0.3, EB1, EB2, "6", tl=a9 + 0.3)
    # a linha do topo: altura e mediana
    if t >= b9:
        M.line(c, *ET, *EM, AMBAR, 1.0, 7, dash=None if t >= d10 else E.TRACO, progress=ease_io(prog(t, b9, 0.7)))
    E.angulo(c, t, c9, EM, EB2, ET, r=44)
    E.foco(c, t, c9 + 0.6, 0.4, lambda a: (E.marcas_iguais(c, EB1, EM, 2, TINTA, a), E.marcas_iguais(c, EM, EB2, 2, TINTA, a)))
    E.foco(c, t, a10, 0.4, lambda a: (centro(c, "3", (EB1[0] + EM[0]) / 2, 970, 64, "b", TINTA, a), centro(c, "3", (EM[0] + EB2[0]) / 2, 970, 64, "b", TINTA2, a)))
    pinta(c, [ET, EM, EB2], E.COR, ep(t, b10, 0.5), 0.2)
    grosso(c, ET, EB2, COR, 1.0, 12, ease_io(prog(t, b10, 0.5)))
    grosso(c, EM, EB2, TINTA2, ep(t, c10, 0.4), 12)
    grosso(c, ET, EM, AMBAR, ep(t, d10, 0.4), 12)
    E.foco(c, t, d10 + 0.3, 0.4, lambda a: E.formula(c, "h" if t < c11 else "3r{3}", EM[0] + 22, 740, 64, "g", AMBAR, a, "left"))

    def textos9():
        E.frase(c, t, a9, ps("equilátero:", "i", 66) + [("3 lados iguais", "g", 70, COR)], X, 220, "center", 0.12)
        E.frase(c, t, b9, ps("a linha do topo é", "i", 62), X, 340, "center", 0.1)
        E.frase(c, t, b9 + 0.8, [("altura", "g", 70, AMBAR)] + ps("e", "i", 62) + [("mediana", "g", 70)], X, 430, "center", 0.12)
        E.frase(c, t, c9, [("90°", "g", 70, COR)] + ps("e a base", "i", 62) + [("ao meio", "g", 70)], X, 560, "center", 0.12)
    E.saida(c, t, C["s10"] - 0.1, textos9)

    def textos10():
        E.frase(c, t, b10, ps("hipotenusa", "i", 64) + [("6", "g", 76, COR)], X, 300, "center", 0.12)
        E.frase(c, t, c10, ps("cateto", "i", 64) + [("3", "g", 76, TINTA2)] + ps("(metade da base)", "i", 52, TINTA2), X, 430, "center", 0.12)
        E.frase(c, t, d10, ps("cateto", "i", 64) + [("h", "g", 76, AMBAR)] + ps("(a altura)", "i", 52, TINTA2), X, 560, "center", 0.12)
    if t >= C["s10"] - 0.1:
        E.saida(c, t, C["s11"] - 0.1, textos10)

    def textos11():
        E.frase(c, t, C["s11"], ps("falta cateto:", "i", 64) + [("subtração", "g", 70, AMBAR)], X, 260, "center", 0.12)
        fcen(c, t, a11, "h^2 = 36 − 9 = 27", X, 420, 84)
        fcen(c, t, b11, "27 = 9 × 3", X, 560, 84, TINTA2)
        bola_txt(c, t, c11, "h = 3r{3}", X, 760, 130, 72, AMBAR)
    if t >= C["s11"] - 0.1:
        E.saida(c, t, C["s12"] - 0.1, textos11)
    if C["s12"] - 0.1 <= t < C["s13"]:
        def doze():
            equi(c, t, a12, PB1, PB2, "2", tl=a12 + 0.4, d=0.6)
            if t >= a12 + 0.5:
                M.line(c, *PT, *PM, AMBAR, 1.0, 6, progress=ease_io(prog(t, a12 + 0.5, 0.5)))
                E.angulo(c, t, a12 + 0.8, PM, PB2, PT, r=26)
            E.foco(c, t, a12 + 0.9, 0.4, lambda a: centro(c, "1", (PM[0] + PB2[0]) / 2, 960, 54, "b", TINTA2, a))
            E.foco(c, t, c12, 0.4, lambda a: E.formula(c, "h = r{3}", PT[0], PT[1] - 30, 54, "g", AMBAR, a, "center"))
            fx = 1560
            fcen(c, t, a12, "lado 2,  metade 1", fx, 300, 64)
            fcen(c, t, b12, "h^2 = 4 − 1 = 3", fx, 420, 74)
            fcen(c, t, c12, "h = r{3}", fx, 540, 84, AMBAR)
            E.frase(c, t, d12 - 1.6, ps("lado 6:", "i", 60) + [("3 vezes maior", "g", 62)], fx, 680, "center", 0.12)
            fcen(c, t, d12, "h = 3r{3}", fx, 790, 84, AMBAR)
            E.frase(c, t, e12, ps("metade do lado ×", "i", 58) + [("√3", "g", 62, COR)], fx, 920, "center", 0.12)
        E.saida(c, t, C["s13"] - 0.1, doze)
    if t >= C["s13"] - 0.1:
        fx = 1450
        E.foco(c, t, a13 - 0.1, 0.5, lambda a: E.caixa_pontilhada(c, fx - 300, 180, 600, 280, a, COR, prog_=ep(t, a13 - 0.1, 0.6)))
        fcen(c, t, a13, "h = f{ℓr{3}}{2}", fx, 360, 120, COR)
        E.frase(c, t, b13, [("h", "g", 64, AMBAR)] + ps("= altura", "i", 60), fx - 160, 560, "center", 0.1)
        E.frase(c, t, c13, [("ℓ", "g", 64, COR)] + ps("= lado", "i", 60), fx + 180, 560, "center", 0.1)
        fcen(c, t, d13, "f{6r{3}}{2} = 3r{3}", fx, 780, 100, AMBAR)


# ---------------- erro ----------------
FU = 60
FB1, FB2 = (320, 960), (320 + 6 * FU, 960)
FT = ((FB1[0] + FB2[0]) / 2, FB1[1] - 6 * FU * math.sqrt(3) / 2)
FM = ((FB1[0] + FB2[0]) / 2, FB1[1])
FE = (FM[0], FM[1] - 6 * FU * math.sqrt(3))          # a altura errada, 6√3


def b_erro(c, t, C, b):
    a14, b14, c14, d14, e14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"]
    X = 1300
    E.frase(c, t, C["s14"], [("cuidado", "g", 90, ERRADO)] + ps("com este erro", "i", 84), X, 140, "center", 0.14)
    equi(c, t, C["s14"] + 0.2, FB1, FB2, "6", d=0.6)
    E.frase(c, t, a14, ps("esqueceu o", "i", 66) + [("÷ 2", "g", 76, ERRADO)], X, 270, "center", 0.12)
    # a altura errada passa muito do topo
    if t >= b14:
        k = ease_io(prog(t, b14, 0.9)) * (1 - 0.7 * ep(t, e14, 0.5))
        M.line(c, *FM, FM[0], lerp(FM[1], FE[1], k), ERRADO, 1.0, 8)
        if k > 0.95:
            c.drawCircle(*FE, 10, M.paint(ERRADO))
    E.foco(c, t, b14 + 0.6, 0.4, lambda a: E.formula(c, "6r{3}", FE[0] + 30, FE[1] + 30, 60, "g", ERRADO, a * (1 - 0.7 * ep(t, e14, 0.5)), "left"))
    fcen(c, t, b14, "h = 6r{3}", X, 400, 84, ERRADO)
    fcen(c, t, c14, "6 × 1,7 = 10,2 > 10", X, 530, 74, ERRADO)
    E.frase(c, t, d14, ps("a altura é cateto: não passa de", "i", 58) + [("6", "g", 66, COR)], X, 670, "center", 0.1)
    grosso(c, FT, FB2, COR, ep(t, d14, 0.4), 10)
    # a certa
    if t >= e14:
        M.line(c, *FM, *FT, CERTO, 1.0, 9, progress=ease_io(prog(t, e14, 0.5)))
        E.angulo(c, t, e14 + 0.3, FM, FB2, FT, r=30, cor=CERTO)
    E.foco(c, t, e14 + 0.4, 0.4, lambda a: E.formula(c, "3r{3}", FM[0] + 16, 905, 48, "g", CERTO, a, "left"))
    fcen(c, t, e14, "3r{3} ≈ 3 × 1,7 = 5,1", X, 820, 78, CERTO)
    E.foco(c, t, e14 + 1.0, 0.4, lambda a: E.selo(c, X, 950, 50 * ease_back(prog(t, e14 + 1.0, 0.4)), True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    a16, b16, c16, d16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    E.frase(c, t, C["s15"] + 0.2, [("atalho", "g", 90, CLARO)] + ps("para não trocar", "i", 80, BR), W / 2, 150, "center", 0.12)
    # quadrado à esquerda, equilátero à direita
    qx, qy, ql = 330, 300, 300
    E.foco(c, t, a15, 0.5, lambda a: (c.drawRect(skia.Rect.MakeXYWH(qx, qy, ql, ql), M.paint(BR, a, stroke=6)),
                                      M.line(c, qx, qy + ql, qx + ql, qy, CLARO, a, 6)))
    fcen(c, t, a15 + 0.3, "d = ℓr{2}", 480, 720, 96, BR)
    B1, B2 = (1180, 600), (1520, 600)
    T = (1350, 600 - 340 * math.sqrt(3) / 2)
    E.foco(c, t, b15, 0.5, lambda a: (M.line(c, *B1, *B2, BR, a, 6), M.line(c, *B2, *T, BR, a, 6), M.line(c, *T, *B1, BR, a, 6),
                                      M.line(c, *T, 1350, 600, CLARO, a, 5)))
    fcen(c, t, b15 + 0.3, "h = ℓr{3}", 1310, 720, 96, BR)
    E.foco(c, t, c15, 0.5, lambda a: (E.formula(c, "÷ 2", 1560, 720, 96, "g", E.mix(E.COR, BR, 0.6), a, "left"),
                                      E.marcas_iguais(c, B1, (1350, 600), 1, AMBAR, a), E.marcas_iguais(c, (1350, 600), B2, 1, AMBAR, a)))
    fcen(c, t, a16, "1 + 1 = 2", 480, 850, 76, CLARO)
    fcen(c, t, b16, "4 − 1 = 3", 1350, 850, 76, CLARO)
    E.foco(c, t, c16, 0.5, lambda a: E.pilula(c, "retângulo comprido ou triângulo qualquer: não serve", W / 2, 960, 48, "g", fundo=ERRADO, a=a))
    E.foco(c, t, d16, 0.5, lambda a: E.pilula(c, "aí, Pitágoras completo", W / 2, 1040, 44, "g", fundo=E.COR, a=a))


# ---------------- questão ----------------
QS = (230, 400, 280)                 # quadrado: x, y, lado em px (lado 4)
QB1, QB2 = (640, 680), (920, 680)    # equilátero de mesmo lado
QT = ((QB1[0] + QB2[0]) / 2, QB1[1] - 280 * math.sqrt(3) / 2)
QM = ((QB1[0] + QB2[0]) / 2, QB1[1])


def figuras_q(c, t, t0, tl, td, th, lado=lambda tt: "ℓ", h_txt=lambda tt: "h = ?", h_cor=lambda tt: AMBAR):
    x, y, l = QS
    E.quadrado(c, t, t0, x, y, l, None, retos=(0, 1, 2, 3), preenche=0.04)
    equi(c, t, t0 + 0.3, QB1, QB2, None)
    E.foco(c, t, tl, 0.4, lambda a: (centro(c, lado(t), x + l / 2, y + l + 70, 60, "g", COR, a),
                                     centro(c, lado(t), (QB1[0] + QB2[0]) / 2, QB1[1] + 70, 60, "g", COR, a)))
    if t >= td:
        M.line(c, x, y + l, x + l, y, COR, 1.0, 7, progress=ease_io(prog(t, td, 0.6)))
    E.foco(c, t, td + 0.4, 0.4, lambda a: txt_lado(c, (x, y + l), (x + l, y), "4r{2}", (x + l * 0.7, y + l * 0.7), 50, COR, a))
    if t >= th:
        M.line(c, *QT, *QM, AMBAR, 1.0, 7, dash=E.TRACO, progress=ease_io(prog(t, th, 0.6)))
        E.angulo(c, t, th + 0.4, QM, QB2, QT, r=26)
    E.foco(c, t, th + 0.4, 0.4, lambda a: E.formula(c, h_txt(t), QM[0] + 24, QT[1] - 30, 54, "g", h_cor(t), a, "center"))


def b_questao(c, t, C, b):
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 140, passo=0.12)
    figuras_q(c, t, C["s17"] + 0.3, a17, b17, c17)
    E.saida(c, t, C["s18.a"] - 0.1, lambda: E.frase(c, t, a17, ps("o", "i", 64) + [("mesmo lado", "g", 70, COR)], 1500, 380, "center", 0.12))
    pergunta(c, t, [(a17, ps("quadrado e equilátero", "i", 58)),
                    (b17, ps("diagonal:", "i", 62) + [("4√2 cm", "g", 70)]),
                    (c17, ps("altura do triângulo:", "i", 62) + [("h = ?", "g", 70, AMBAR)])], C["s18.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a19, b19 = C["s19.a"], C["s19.b"]
    a20, b20, c20, d20, e20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"], C["s20.e"]
    X = 1440
    t0 = C["s19"] - 1.2
    figuras_q(c, t, t0, t0, t0, t0, lambda tt: "4" if tt >= b19 else "ℓ",
              lambda tt: "2r{3}" if tt >= b20 else "h", lambda tt: CERTO if tt >= b20 else AMBAR)
    E.foco(c, t, a20, 0.4, lambda a: centro(c, "2", (QM[0] + QB2[0]) / 2 + 10, QB1[1] - 16, 44, "b", TINTA2, a))
    grosso(c, QM, QB2, TINTA2, ep(t, a20, 0.4), 10)

    def um():
        fcen(c, t, a19, "d = ℓr{2}", X, 300, 96, COR)
        fcen(c, t, lerp(a19, b19, 0.6), "ℓr{2} = 4r{2}", X, 450, 84)
        bola_txt(c, t, b19, "ℓ = 4 cm", X, 660, 130, 64)
    E.saida(c, t, C["s20"] - 0.1, um)
    if t >= C["s20"] - 0.1:
        fcen(c, t, a20, "metade do lado: 2", X, 200, 70)
        bola_txt(c, t, b20, "2r{3} cm", X - 180, 380, 120, 60, CERTO)
        E.foco(c, t, c20, 0.4, lambda a: E.formula(c, "≈ 2 × 1,7 = 3,4", X + 220, 350, 52, "g", TINTA2, a, "center"))
        E.foco(c, t, c20 + 0.6, 0.4, lambda a: E.formula(c, "< 3,5", X + 220, 430, 52, "g", TINTA2, a, "center"))
        fcen(c, t, d20, "h^2 = 16 − 4 = 12", X, 620, 80)
        fcen(c, t, e20, "12 = 4 × 3  →  h = 2r{3}", X, 770, 74, CERTO)
        E.foco(c, t, e20 + 1.2, 0.4, lambda a: E.selo(c, X, 900, 52 * ease_back(prog(t, e20 + 1.2, 0.4)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s21.a", "diagonal do quadrado", "d = ℓr{2}"), ("s21.b", "altura do equilátero", "h = f{ℓr{3}}{2}"))
        for i, (k, it, form) in enumerate(itens):
            y = 440 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(it, "i", 76)], 400, y)
            E.formula_em(c, t, C[k] + 0.8, form, 1200, y, 100, "g", COR)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.2, ps("próxima aula", "i", 84), XE, 260)
    E.frase(c, t, C["s22.a"], [("a altura", "g", 110, COR)] + ps("que sai do reto", "i", 84), XE, 410, passo=0.14)
    E.frase(c, t, C["s22.b"], [("2 relações", "g", 96)] + ps("novas", "i", 84), XE, 560, passo=0.14)
    E.frase(c, t, C["s22.c"], ps("como", "i", 70) + [("2,4", "g", 80, COR)] + ps("no 3, 4, 5", "i", 70), XE, 700, passo=0.14)
    E.foco(c, t, C["s22.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1630, p), lerp(650, 355, p), ep(t, C["s22.d"] + 0.2, 0.4))
    E.frase(c, t, C["s22.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, diagonal=b_diagonal, altura=b_altura, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
