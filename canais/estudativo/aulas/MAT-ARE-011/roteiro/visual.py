"""Visual — Estudativo · MAT-ARE-011: triângulos de mesma altura (a razão das áreas é a razão das bases; a mediana corta ao meio).
Linguagem da trilha (MAT-ARE-001) e dos triângulos (MAT-ANG-001/008): lados em tinta; o triângulo ABC sempre o mesmo (B = (0, 0),
C = (10, 0), A = (3, 6), 80 px por unidade), cortado pela linha AD; o pedaço da esquerda em COR clara e o da direita em âmbar claro.
A altura é UMA linha tracejada em TINTA2, de A até a reta de BC, com o quadradinho no pé: serve aos dois pedaços. Bases medidas
com cota embaixo; mediana em COR com os tracinhos de lados iguais. Repartir = barra dividida em partes iguais (2 em COR, 3 em âmbar).
Erro em vermelho, certo em verde; resposta na esfera; atalho no palco (o vértice que anda na paralela, com a área parada).
Peças locais: P() (unidade → pixel), pedaco(), cota(), altura_tr(), barra_partes(), terreno().
Todo instante vem de C[...] (marcadores do roteiro); entre() reparte o tempo entre dois marcadores."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Áreas e Perímetros")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ARE-011_triangulos_de_mesma_altura.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("altura", "mediana", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
assert 10 * 6 / 2 == 30 and 4 * 6 / 2 == 12 and 6 * 6 / 2 == 18 and 12 / 6 == 2 and 18 / 6 == 3 and 4 / 2 == 2 and 6 / 2 == 3
assert 5 * 6 / 2 == 15 and 30 / 5 == 6 and 2 * 6 == 12 and 3 * 6 == 18 and 3 * 6 / 2 == 9 and 7 * 6 / 2 == 21 and 9 + 21 == 30
assert 600 / 5 == 120 and 2 * 120 == 240 and 3 * 120 == 360 and 240 + 360 == 600 and 20 + 30 == 50 and 20 / 10 == 2 and 30 / 10 == 3


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


def entre(C, k1, k2, f):
    return lerp(C[k1], C[k2], f)


U, OX, OY = 80, 180, 880


def P(x, y=0.0):
    """unidade → pixel (B = (0, 0) em (OX, OY))"""
    return OX + x * U, OY - y * U


TA, TB, TC = P(3, 6), P(0), P(10)


def pedaco(c, pts, cor, alfa, a=1.0):
    if a > 0:
        path = skia.Path(); path.addPoly(pts, True)
        c.drawPath(path, M.paint(cor, alfa * a))


def nomes(c, t, t0, pts, letras, a=1.0, cor=TINTA):
    g = (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))
    for i, (V, s) in enumerate(zip(pts, letras)):
        if not s:
            continue
        ux, uy = V[0] - g[0], V[1] - g[1]
        n = math.hypot(ux, uy) or 1
        E.foco(c, t, t0 + 0.1 * i, 0.4, lambda f, V=V, s=s, ux=ux / n, uy=uy / n: centro(c, s, V[0] + ux * 50, V[1] + uy * 50 + 20, 56, "g", cor, f * a))


def cota(c, x0, x1, y, s, cor=TINTA, a=1.0, size=54):
    if a <= 0:
        return
    M.line(c, x0 + 4, y, x1 - 4, y, cor, a, 4)
    for x in (x0 + 4, x1 - 4):
        M.line(c, x, y - 12, x, y + 12, cor, a, 4)
    centro(c, s, (x0 + x1) / 2, y + size + 6, size, "g", cor, a)


def altura_tr(c, t, t0, A, pe, rot=None, cor=TINTA2, a=1.0, larg=5):
    if t < t0 or a <= 0:
        return
    M.line(c, *A, *pe, cor, a, larg, dash=E.TRACO, progress=ease_io(prog(t, t0, 0.6)))
    k = ep(t, t0 + 0.4, 0.3) * a
    if k > 0:
        s = 26
        p = M.paint(cor, k, stroke=3)
        c.drawRect(skia.Rect.MakeXYWH(pe[0], pe[1] - s, s, s), p)
    if rot:
        E.foco(c, t, t0 + 0.4, 0.4, lambda f: E.formula(c, rot, A[0] - 18, (A[1] + pe[1]) / 2 + 20, 56, "g", cor, f * a, "right"))


def triangulo(c, t, t0, D=None, tD=None, tpinta=None, a=1.0):
    """ABC com o ponto D e os dois pedaços pintados"""
    if t < t0 or a <= 0:
        return
    if D is not None and tpinta is not None and t >= tpinta:
        k = ep(t, tpinta, 0.5) * a
        pedaco(c, [TA, TB, D], E.COR, 0.3, k)
        pedaco(c, [TA, D, TC], AMBAR, 0.3, k)
    elif t >= t0:
        pedaco(c, [TA, TB, TC], E.COR, 0.1 * ep(t, t0 + 0.5, 0.5), a)
    if a >= 1:
        E._contorno(c, [TB, TC, TA], ease_io(prog(t, t0, 0.8)), TINTA, 6)
    else:
        c.saveLayerAlpha(None, int(255 * a)); E._contorno(c, [TB, TC, TA], 1.0, TINTA, 6); c.restore()
    nomes(c, t, t0 + 0.4, [TA, TB, TC], "ABC", a)
    if D is not None and tD is not None and t >= tD:
        k = ease_back(prog(t, tD, 0.35))
        c.drawCircle(*D, 11 * k, M.paint(TINTA, a))
        E.foco(c, t, tD, 0.3, lambda f: centro(c, "D", D[0], D[1] + 64, 56, "g", TINTA, f * a))


def barra_partes(c, t, t0, x, y, w, h, n, cores, tp=None, rot=None, a=1.0):
    """barra dividida em n partes iguais; cores[i] = cor de cada parte; tp = instante de cada parte acender"""
    if t < t0 or a <= 0:
        return
    k = ep(t, t0, 0.5) * a
    s = w / n
    for i in range(n):
        q = ep(t, tp[i], 0.4) * a if tp else k
        if q > 0:
            c.drawRect(skia.Rect.MakeXYWH(x + i * s, y, s, h), M.paint(cores[i], 0.55 * q))
        if rot:
            E.foco(c, t, tp[i] if tp else t0, 0.4, lambda f, i=i: centro(c, rot, x + i * s + s / 2, y + h / 2 + 20, 56, "g", TINTA, f * a))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, k, stroke=5))
    for i in range(1, n):
        M.line(c, x + i * s, y, x + i * s, y + h, TINTA, k, 4)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    X = 1480
    # um triângulo obtuso: A além de C; a mediana AM deixa um pedaço fino e outro aberto
    q = lambda x, y: (150 + x * 85, 900 - y * 85)
    A, B, Cc, Mm = q(10, 7), q(0, 0), q(8, 0), q(4, 0)

    def um():
        k = ep(t, a1, 0.5)
        if t >= a1:
            E._contorno(c, [B, Cc, A], ease_io(prog(t, a1, 0.8)), TINTA, 6)
            M.line(c, *A, *Mm, E.COR, 1.0, 7, progress=ease_io(prog(t, a1 + 0.8, 0.6)))
        pedaco(c, [A, Mm, Cc], AMBAR, 0.45, ep(t, b1, 0.5))
        pedaco(c, [A, B, Mm], E.COR, 0.3, ep(t, c1, 0.5))
        E.foco(c, t, d1 + 0.3, 0.4, lambda f: (E.pilula(c, "área", (A[0] + B[0] + Mm[0]) / 3, (A[1] + B[1] + Mm[1]) / 3, 52, "g", fundo=E.COR, a=f),
                                               E.pilula(c, "área", (A[0] + Mm[0] + Cc[0]) / 3 + 20, (A[1] + Mm[1] + Cc[1]) / 3, 52, "g", fundo=AMBAR, a=f)))
        E.frase(c, t, b1, ps("um", "i", 64) + [("fino e inclinado", "g", 66, AMBAR)], X, 300, "center", 0.12)
        E.frase(c, t, c1, ps("outro", "i", 64) + [("bem mais aberto", "g", 66, COR)], X, 430, "center", 0.12)
        E.frase(c, t, d1, [("mesma área", "g", 92, CERTO)], X, 640, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1520, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 300, passo=0.14)
        E.frase(c, t, entre(C, "s02.a", "s02.b", 0.3), [("repartir", "g", 110, COR)] + ps("a área", "i", 90), XE, 450, passo=0.14)
        E.frase(c, t, entre(C, "s02.a", "s02.b", 0.55), ps("de um triângulo", "i", 84), XE, 580, passo=0.14)
        E.frase(c, t, entre(C, "s02.a", "s02.b", 0.75), ps("sem medir altura", "i", 72, TINTA2), XE, 700, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1520, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1520, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "área do triângulo:", "f{base · altura}{2}"), ("s03.c", "mediana: do vértice até o", "ponto médio do lado da frente"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 84)
        E.formula_em(c, t, C[k] + 0.4, l2, x + 44, y + (190 if "f{" not in l2 else 165), 50 if "f{" not in l2 else 66, "g", COR)
    alvo = [(x + w + 20, 250 + i * 280 + 200) for i in range(2)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, alvo[0][0], lerp(alvo[0][1], alvo[1][1], q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 900, "left", 0.12)


# ---------------- a mesma altura ----------------
D4 = P(4)
H3 = P(3)


def b_altura(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    X = 1480
    if t >= a5:  # a reta de BC, esticada
        k = ep(t, a5, 0.5)
        M.line(c, OX - 120, OY, OX + 10 * U + 120, OY, TINTA2, k, 3, dash=[10, 10])
    triangulo(c, t, a4, D4, b4, d4)
    if t >= c4:
        M.line(c, *TA, *D4, TINTA, 1.0, 6, progress=ease_io(prog(t, c4, 0.5)))
    altura_tr(c, t, b5, TA, H3, "h", TINTA2)

    E.frase(c, t, a4, ps("triângulo", "i", 66) + [("ABC", "g", 72)], X, 220, "center", 0.12)
    E.frase(c, t, b4, ps("ponto", "i", 62) + [("D", "g", 68)] + ps("no lado", "i", 62) + [("BC", "g", 68)], X, 330, "center", 0.12)
    E.frase(c, t, c4, ps("ligue", "i", 62) + [("A", "g", 68)] + ps("a", "i", 62) + [("D", "g", 68)], X, 440, "center", 0.12)
    E.frase(c, t, d4, [("ABD", "g", 70, COR)] + ps("e", "i", 62) + [("ADC", "g", 70, AMBAR)], X, 550, "center", 0.12)
    E.frase(c, t, a5, ps("bases na", "i", 60) + [("mesma reta", "g", 64)], X, 700, "center", 0.12)
    E.frase(c, t, b5, ps("a altura é", "i", 60) + [("a mesma linha", "g", 64)], X, 800, "center", 0.12)
    E.foco(c, t, c5, 0.5, lambda a: E.pilula(c, "mesma altura", X, 930, 64, "g", fundo=CERTO, a=a))


# ---------------- o exemplo: 10 e 6 ----------------
def b_exemplo(c, t, C, b):
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    X = 1480
    t0 = C["s06"]
    triangulo(c, t, t0 - 1.0, D4, t0 - 1.0, c6)
    M.line(c, *TA, *D4, TINTA, 1.0, 6)
    altura_tr(c, t, t0 - 1.0, TA, H3, None, TINTA2)
    E.foco(c, t, a6, 0.4, lambda f: E.formula(c, "6", H3[0] - 18, (TA[1] + OY) / 2 + 20, 60, "g", TINTA2, f, "right"))
    k10 = ep(t, a6, 0.4) * (1 - ep(t, c6, 0.4))
    cota(c, OX, OX + 10 * U, OY + 100, "10", TINTA, k10)
    k46 = ep(t, c6, 0.4)
    cota(c, OX, D4[0], OY + 100, "4", COR, k46)
    cota(c, D4[0], OX + 10 * U, OY + 100, "6", AMBAR, k46)
    E.foco(c, t, d6 + 0.6, 0.4, lambda f: E.pilula(c, "12", (TA[0] + TB[0] + D4[0]) / 3 - 10, (TA[1] + TB[1] + D4[1]) / 3 + 30, 52, "g", fundo=E.COR, a=f))
    E.foco(c, t, e6 + 0.6, 0.4, lambda f: E.pilula(c, "18", (TA[0] + D4[0] + TC[0]) / 3 + 20, (TA[1] + D4[1] + TC[1]) / 3 + 30, 52, "g", fundo=AMBAR, a=f))

    def seis():
        E.frase(c, t, a6, [("BC = 10,", "g", 62)] + ps("altura", "i", 58) + [("6", "g", 62)], X, 220, "center", 0.12)
        fcen(c, t, b6, "ABC: f{10 · 6}{2} = 30", X, 380, 70)
        E.frase(c, t, c6, [("BD = 4,", "g", 62, COR), ("DC = 6", "g", 62, AMBAR)], X, 540, "center", 0.12)
        fcen(c, t, d6, "ABD: f{4 · 6}{2} = 12", X, 690, 70, COR)
        fcen(c, t, e6, "ADC: f{6 · 6}{2} = 18", X, 870, 70, AMBAR)
    E.saida(c, t, C["s07"] - 0.1, seis)
    if t >= C["s07"] - 0.1:
        E.frase(c, t, a7, ps("bases", "i", 62) + [("4 : 6 = 2 : 3", "g", 70)], X, 220, "center", 0.12)
        E.frase(c, t, b7, ps("áreas", "i", 62) + [("12 : 18", "g", 70)], X, 340, "center", 0.12)
        E.frase(c, t, c7, ps("÷ 6:", "g", 58, TINTA2) + [("2 : 3", "g", 74, CERTO)], X, 460, "center", 0.12)
        E.foco(c, t, d7, 0.5, lambda a: (E.pilula(c, "mesma altura:", X, 600, 52, "g", fundo=TINTA, a=a),
                                         centro(c, "razão das áreas = razão das bases", X, 700, 44, "g", COR, a)))
        fcen(c, t, e7, "f{4 · 6 ÷ 2}{6 · 6 ÷ 2} = f{4}{6}", X, 860, 70)
        E.frase(c, t, e7 + 1.0, ps("a altura e o ÷ 2", "i", 54, TINTA2) + [("se cancelam", "g", 56)], X, 1000, "center", 0.1)


# ---------------- a mediana ----------------
M5 = P(5)


def b_mediana(c, t, C, b):
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    X = 1480
    g = ease_io(prog(t, a8, 0.8))
    D = (lerp(D4[0], M5[0], g), OY)
    t0 = C["s08"]
    triangulo(c, t, t0 - 1.0, D, t0 - 1.0, t0 - 1.0)
    M.line(c, *TA, *D, E.COR if t >= b8 else TINTA, 1.0, 8 if t >= b8 else 6)
    altura_tr(c, t, t0 - 1.0, TA, H3, None, TINTA2, a=1 - ep(t, b8, 0.4) * 0.6)
    if t >= c8:
        k = ep(t, c8, 0.4)
        cota(c, OX, M5[0], OY + 100, "5", COR, k)
        cota(c, M5[0], OX + 10 * U, OY + 100, "5", AMBAR, k)
        E.marcas_iguais(c, TB, M5, 1, TINTA, k)
        E.marcas_iguais(c, M5, TC, 1, TINTA, k)
    E.foco(c, t, d8 + 0.5, 0.4, lambda f: (E.pilula(c, "15", (TA[0] + TB[0] + M5[0]) / 3 - 10, (TA[1] + TB[1] + M5[1]) / 3 + 30, 52, "g", fundo=E.COR, a=f),
                                           E.pilula(c, "15", (TA[0] + M5[0] + TC[0]) / 3 + 20, (TA[1] + M5[1] + TC[1]) / 3 + 30, 52, "g", fundo=AMBAR, a=f)))
    E.frase(c, t, a8, [("D", "g", 68)] + ps("no", "i", 62) + [("ponto médio", "g", 68, COR)], X, 220, "center", 0.12)
    E.frase(c, t, b8, [("AD", "g", 68)] + ps("é a", "i", 62) + [("mediana", "g", 68, COR)], X, 340, "center", 0.12)
    E.frase(c, t, c8, ps("bases", "i", 62) + [("5 e 5", "g", 70)], X, 460, "center", 0.12)
    E.frase(c, t, d8, ps("áreas", "i", 62) + [("15 e 15", "g", 70, CERTO)], X, 580, "center", 0.12)
    E.foco(c, t, e8, 0.5, lambda a: E.pilula(c, "mediana: áreas iguais", X, 750, 58, "g", fundo=CERTO, a=a))
    E.frase(c, t, e8 + 1.5, ps("mesmo com formatos diferentes", "i", 54, TINTA2), X, 870, "center", 0.1)


# ---------------- repartir ----------------
def b_repartir(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    X = 1480
    x, y, w, h = 170, 520, 900, 140
    cores = [E.COR, E.COR, AMBAR, AMBAR, AMBAR]
    E.foco(c, t, a9, 0.4, lambda f: E.pilula(c, "área 30", x + w / 2, y - 90, 56, "g", fundo=TINTA, a=f))
    barra_partes(c, t, b9, x, y, w, h, 5, ["#CCCCCC"] * 5, rot=None)
    s = w / 5
    for i in range(5):
        ti = d9 + 0.15 * i if i < 2 else e9 + 0.15 * (i - 2)
        k = ep(t, ti, 0.4)
        if k > 0:
            c.drawRect(skia.Rect.MakeXYWH(x + i * s, y, s, h), M.paint(cores[i], 0.5 * k))
            M.line(c, x + i * s, y, x + i * s, y + h, TINTA, k, 4)
        E.foco(c, t, c9 + 0.1 * i, 0.4, lambda f, i=i: centro(c, "6", x + i * s + s / 2, y + h / 2 + 20, 60, "g", TINTA, f))
    if t >= b9:
        k = ep(t, b9, 0.4)
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, k, stroke=5))
        for i in range(1, 5):
            M.line(c, x + i * s, y, x + i * s, y + h, TINTA, k, 4)
    if t >= d9:
        E.chave(c, x + 6, x + 2 * s - 6, y + h + 20, E.COR, ep(t, d9, 0.4), 26)
        E.foco(c, t, d9 + 0.3, 0.4, lambda f: centro(c, "12", x + s, y + h + 120, 70, "g", COR, f))
    if t >= e9:
        E.chave(c, x + 2 * s + 6, x + w - 6, y + h + 20, AMBAR, ep(t, e9, 0.4), 26)
        E.foco(c, t, e9 + 0.3, 0.4, lambda f: centro(c, "18", x + 3.5 * s, y + h + 120, 70, "g", AMBAR, f))
    E.frase(c, t, a9, ps("repartir", "i", 66) + [("pela razão", "g", 70, COR)], X, 240, "center", 0.12)
    fcen(c, t, b9, "2 + 3 = 5 partes", X, 400, 76)
    fcen(c, t, c9, "30 ÷ 5 = 6", X, 540, 80)
    fcen(c, t, d9, "2 · 6 = 12", X, 690, 80, COR)
    fcen(c, t, e9, "3 · 6 = 18", X, 830, 80, AMBAR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a10, b10, c10, d10, e10 = (C[f"s10.{k}"] for k in "abcde")
    X = 1480
    triangulo(c, t, C["s10"], H3, None, b10)
    if t >= b10:
        M.line(c, *TA, *H3, ERRADO, 1.0, 7, progress=ease_io(prog(t, b10, 0.5)))
        E.angulo(c, t, b10 + 0.4, H3, TA, TC, r=30, reto=True, preenche=0.0, cor=ERRADO)
        k = ep(t, b10 + 0.5, 0.4)
        cota(c, OX, H3[0], OY + 100, "3", COR, k)
        cota(c, H3[0], OX + 10 * U, OY + 100, "7", AMBAR, k)
    E.foco(c, t, c10 + 0.6, 0.4, lambda f: E.pilula(c, "9", (TA[0] + TB[0] + H3[0]) / 3 - 10, (TA[1] + TB[1] + H3[1]) / 3 + 40, 52, "g", fundo=E.COR, a=f))
    E.foco(c, t, d10 + 0.6, 0.4, lambda f: E.pilula(c, "21", (TA[0] + H3[0] + TC[0]) / 3 + 20, (TA[1] + H3[1] + TC[1]) / 3 + 30, 52, "g", fundo=AMBAR, a=f))
    if t >= e10:  # a mediana, a certa
        M.line(c, *TA, *M5, CERTO, 1.0, 8, progress=ease_io(prog(t, e10, 0.6)))
        k = ep(t, e10 + 0.5, 0.4)
        E.marcas_iguais(c, TB, M5, 1, CERTO, k)
        E.marcas_iguais(c, M5, TC, 1, CERTO, k)

    E.frase(c, t, a10, ps("erro:", "i", 60, ERRADO) + [("qualquer linha", "g", 64)], X, 200, "center", 0.12)
    E.frase(c, t, a10 + 1.0, ps("do vértice corta ao meio?", "i", 60), X, 290, "center", 0.12)
    E.frase(c, t, b10, ps("a altura cai a", "i", 58) + [("3", "g", 64, COR)] + ps("do", "i", 58) + [("B", "g", 64)], X, 430, "center", 0.12)
    fcen(c, t, c10, "f{3 · 6}{2} = 9", X, 580, 72, COR)
    fcen(c, t, d10, "f{7 · 6}{2} = 21", X, 740, 72, AMBAR)
    E.frase(c, t, d10 + 1.2, [("9 ≠ 21", "g", 64, ERRADO)], X, 860, "center")
    E.foco(c, t, e10, 0.5, lambda a: E.pilula(c, "só a mediana corta ao meio", X, 970, 52, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a11, b11, c11, d11 = (C[f"s11.{k}"] for k in "abcd")
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    X = 1460
    yb, ya = 880, 420
    B, Cc = (180, yb), (820, yb)
    # o vértice: parado até c; depois anda na paralela
    ax = 380
    if t >= c11:
        ax = 380 + 330 * math.sin((t - c11) * 1.1) * ep(t, c11, 0.6)
    A = (ax, ya)
    if t < c11:
        Dm = (436, yb)
        k = ep(t, C["s11"] + 0.2, 0.5) * (1 - ep(t, c11 - 0.3, 0.3))
        pedaco(c, [A, B, Dm], E.COR, 0.6, k)
        pedaco(c, [A, Dm, Cc], AMBAR, 0.5, k)
        M.line(c, *A, *Dm, BR, k, 5)
        E.foco(c, t, b11, 0.4, lambda f: (centro(c, "2", (B[0] + Dm[0]) / 2, yb + 64, 56, "g", CLARO, f * k),
                                          centro(c, "3", (Dm[0] + Cc[0]) / 2, yb + 64, 56, "g", AMBAR, f * k)))
    else:
        pedaco(c, [A, B, Cc], E.COR, 0.6, ep(t, c11, 0.4))
        M.line(c, 100, ya, 1000, ya, CLARO, ep(t, c11, 0.4), 3, dash=[12, 10])
        E.foco(c, t, d11, 0.4, lambda f: E.pilula(c, "a área não muda", 500, 980, 56, "g", fundo=CERTO, a=f))
    path = skia.Path(); path.addPoly([B, Cc, A], True)
    p = M.paint(BR, ep(t, C["s11"], 0.4), stroke=6); p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, p)
    M.line(c, *A, A[0], yb, CLARO, ep(t, a11, 0.4), 4, dash=[10, 10])

    def onze():
        E.frase(c, t, C["s11"] + 0.2, [("atalho", "g", 90, CLARO)], X, 170, "center", 0.12)
        E.frase(c, t, a11, ps("vértice comum,", "i", 52, CLARO) + [("bases na mesma reta", "g", 52, BR)], X, 300, "center", 0.12)
        E.frase(c, t, b11, [("compare só as bases", "g", 72, AMBAR)], X, 420, "center", 0.12)
        E.frase(c, t, c11, [("mesma base,", "g", 54, BR)] + ps("vértice na", "i", 52, CLARO) + [("paralela", "g", 54, BR)], X, 600, "center", 0.12)
        E.frase(c, t, d11, ps("altura igual,", "i", 60, CLARO) + [("área igual", "g", 66, BR)], X, 720, "center", 0.12)
    E.saida(c, t, C["s12"] - 0.1, onze)
    if t >= C["s12"] - 0.1:
        E.frase(c, t, a12, ps("altura =", "i", 60, CLARO) + [("distância do vértice", "g", 62, BR)], X, 260, "center", 0.12)
        E.frase(c, t, a12 + 1.0, ps("até a reta das bases", "i", 60, CLARO), X, 350, "center", 0.12)
        E.foco(c, t, b12, 0.5, lambda a: E.pilula(c, "sem vértice comum? não compensa", X, 540, 42, "g", fundo=ERRADO, a=a))
        E.frase(c, t, b12 + 1.6, ps("ou bases fora da mesma reta", "i", 54, CLARO), X, 640, "center", 0.1)
        E.frase(c, t, c12, ps("aí,", "i", 66, CLARO) + [("cada área inteira", "g", 72, BR)], X, 800, "center", 0.12)


# ---------------- questão ----------------
QU = 16
QP, QQ = (170, 860), (170 + 50 * QU, 860)   # a frente: 50 m
QV = (420, 400)                             # o canto de onde sai a cerca
QF = (170 + 20 * QU, 860)                   # a cerca chega a 20 m de P


def terreno(c, t, t0, tcerca=None, tl=None, pinta=None, a=1.0):
    if t < t0 or a <= 0:
        return
    q = ease_io(prog(t, t0, 0.7))
    pedaco(c, [QP, QQ, QV], "#DDEFD5", 0.95 * q, a)
    if pinta is not None and t >= pinta:
        k = ep(t, pinta, 0.5) * a
        pedaco(c, [QV, QP, QF], E.COR, 0.3, k)
        pedaco(c, [QV, QF, QQ], AMBAR, 0.35, k)
    E._contorno(c, [QP, QQ, QV], q, TINTA, 6)
    if tcerca is not None and t >= tcerca:
        p = ease_io(prog(t, tcerca, 0.8))
        M.line(c, *QV, lerp(QV[0], QF[0], p), lerp(QV[1], QF[1], p), "#7A4E1E", a, 9)
        for k in range(1, 7):
            f = k / 7
            if f <= p:
                c.drawCircle(lerp(QV[0], QF[0], f), lerp(QV[1], QF[1], f), 8, M.paint("#7A4E1E", a))
    if tl is not None:
        E.foco(c, t, tl, 0.4, lambda f: (cota(c, QP[0], QF[0], QP[1] + 40, "20 m", COR, f * a, 50),
                                         cota(c, QF[0], QQ[0], QP[1] + 40, "30 m", AMBAR, f * a, 50)))


def b_questao(c, t, C, b):
    a13, b13, c13, d13 = (C[f"s13.{k}"] for k in "abcd")
    X = 1500
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), X, 160, "center", 0.12)
    terreno(c, t, a13 - 0.3, tcerca=b13, tl=c13)
    E.foco(c, t, a13 + 0.3, 0.4, lambda f: E.pilula(c, "600 m²", (QP[0] + QQ[0] + QV[0]) / 3 + 40, 740, 50, "g", fundo=TINTA, a=f * (1 - ep(t, c13, 0.3))))
    E.foco(c, t, b13 + 0.6, 0.4, lambda f: centro(c, "frente: 50 m", (QP[0] + QQ[0]) / 2, 260, 52, "g", TINTA, f * (1 - ep(t, c13, 0.3))))
    linhas = [(a13, ps("terreno de", "i", 58) + [("600 m²", "g", 64)]), (b13, ps("cerca do canto até a", "i", 56) + [("frente: 50 m", "g", 60)]),
              (c13, [("20 m", "g", 62, COR)] + ps("e", "i", 58) + [("30 m", "g", 62, AMBAR)]), (d13, ps("cada irmão fica com", "i", 56) + [("?", "g", 66, COR)])]
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, 770 + i * 85, "center", 0.12)
    E.relogio(c, t, C["s14.a"], X, 370, 150)


def b_resposta(c, t, C, b):
    a15, b15 = C["s15.a"], C["s15.b"]
    a16, b16, c16, d16, e16 = (C[f"s16.{k}"] for k in "abcde")
    X = 1480
    t0 = C["s15"] - 1.2
    terreno(c, t, t0, tcerca=t0, tl=t0, pinta=a15)
    altura_tr(c, t, a15 + 0.4, QV, (QV[0], QP[1]), "h", TINTA2)
    E.foco(c, t, c16 + 0.5, 0.4, lambda f: E.pilula(c, "240", (QV[0] + QP[0] + QF[0]) / 3 - 20, (QV[1] + QP[1] + QF[1]) / 3 + 40, 50, "g", fundo=E.COR, a=f))
    E.foco(c, t, d16 + 0.5, 0.4, lambda f: E.pilula(c, "360", (QV[0] + QF[0] + QQ[0]) / 3 + 20, (QV[1] + QF[1] + QQ[1]) / 3 + 30, 50, "g", fundo=AMBAR, a=f))

    def um():
        E.frase(c, t, a15, ps("mesmo vértice:", "i", 60) + [("mesma altura", "g", 66, CERTO)], X, 260, "center", 0.12)
        E.frase(c, t, b15, ps("áreas como as bases:", "i", 58), X, 420, "center", 0.12)
        fcen(c, t, b15 + 0.8, "20 : 30 = 2 : 3", X, 540, 84, COR)
    E.saida(c, t, C["s16"] - 0.1, um)
    if t >= C["s16"] - 0.1:
        fcen(c, t, a16, "2 + 3 = 5 partes", X, 200, 74)
        fcen(c, t, b16, "600 ÷ 5 = 120", X, 330, 78)
        fcen(c, t, c16, "2 · 120 = 240 m²", X, 470, 78, COR)
        fcen(c, t, d16, "3 · 120 = 360 m²", X, 610, 78, AMBAR)
        fcen(c, t, e16, "240 + 360 = 600", X - 40, 790, 76, CERTO)
        E.foco(c, t, e16 + 0.8, 0.4, lambda a: E.selo(c, X + 330, 765, 44 * ease_back(prog(t, e16 + 0.8, 0.4)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s17.a", "com a", "mesma altura,"), ("s17.b", "razão das áreas =", "razão das bases"), ("s17.c", "a mediana corta", "a área ao meio"))
        for i, (k, it, g) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(it, "i", 76), (g, "g", 76, COR)], 400, y, passo=0.25)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    a18, b18, c18, d18 = (C[f"s18.{k}"] for k in "abcd")
    E.frase(c, t, C["s18"] + 0.1, ps("próxima aula:", "i", 72), XE, 220, passo=0.1)
    E.frase(c, t, C["s18"] + 0.8, [("praticar", "g", 100, COR)] + ps("do círculo para cá", "i", 80), XE, 350, passo=0.14)
    if t >= a18:  # região sombreada: quadrado menos um quarto de círculo
        k = ep(t, a18, 0.5)
        x, y, L = 220, 520, 300
        path = skia.Path(); path.addRect(skia.Rect.MakeXYWH(x, y, L, L))
        q = skia.Path(); q.moveTo(x, y + L); q.arcTo(skia.Rect.MakeXYWH(x - L, y, 2 * L, 2 * L), -90, 90, False); q.close()
        path.addPath(q); path.setFillType(skia.PathFillType.kEvenOdd)
        c.drawPath(path, M.paint(E.COR, 0.4 * k))
        c.drawRect(skia.Rect.MakeXYWH(x, y, L, L), M.paint(TINTA, k, stroke=5))
        c.drawArc(skia.Rect.MakeXYWH(x - L, y, 2 * L, 2 * L), -90, 90, False, M.paint(TINTA, k, stroke=5))
        centro(c, "sombreada", x + L / 2, y + L + 70, 50, "g", TINTA, k)
    if t >= b18:
        k = ep(t, b18, 0.5)
        for (x, L, al) in ((640, 200, 0.2), (880, 300, 0.4)):
            c.drawRect(skia.Rect.MakeXYWH(x, 820 - L, L, L), M.paint(E.COR, al * k))
            c.drawRect(skia.Rect.MakeXYWH(x, 820 - L, L, L), M.paint(TINTA, k, stroke=5))
        centro(c, "ampliada", 1030, 890, 50, "g", TINTA, k)
    E.foco(c, t, c18, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 560, 76, estilo="g", a=a))
    p = ease_io(prog(t, c18 + 0.3, 0.8))
    E.cursor(c, lerp(1840, 1680, p), lerp(840, 585, p), ep(t, c18 + 0.2, 0.4))
    E.frase(c, t, d18, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 1010, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, altura=b_altura, exemplo=b_exemplo, mediana=b_mediana, repartir=b_repartir,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
