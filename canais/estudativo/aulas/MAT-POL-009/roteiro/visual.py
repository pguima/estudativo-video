"""Visual — Estudativo · MAT-POL-009: praticando polígonos e circunferência (cinco situações).
Aula de prática no molde da MAT-ANG-009: selo de progresso "situação n de 5", figura à esquerda, pergunta embaixo à direita e
relógio de pausa; na resposta, a mesma figura ganha as medidas e a conta aparece na coluna da direita.
Linguagem da geometria plana (MAT-ANG-001 a 020, MAT-POL-001 a 008): lados em tinta; o ângulo da vez com arco e cunha clara na
cor da matéria; ângulos iguais com a mesma cor (1ª família em COR, 2ª em TINTA2); o externo com o prolongamento tracejado
(MAT-POL-003); a volta da roda vira o rastro na cor da matéria no chão (rolar(), da MAT-POL-004); o arco da vez em destaque grosso;
lados iguais com tracinhos; medidas na grotesca; resposta na esfera; erro em vermelho, certo em verde.
As figuras respeitam as medidas: a água do cano (raio 17, fundura 9) e o arco de 60° são desenhados em escala.
Peças locais: ps(), fcen(), bola_txt(), num_bola(), marca() (progresso), pergunta() (linhas + relógio), lin(), ponto(), rot(),
vang() (ângulo interno do vértice i), roda()/rolar()/escada() (as da MAT-POL-004), deca() (pontos do decágono), agua().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polígonos e Círculo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POL-009_praticando_poligonos_e_circunferencia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
assert 180 - 65 == 115 and 2 * 65 + 2 * 115 == 360
assert 360 // 10 == 36 and 180 - 36 == 144 and (10 - 2) * 180 == 1440 and 1440 // 10 == 144
assert 10 - 3 == 7 and 10 * 7 == 70 and 70 // 2 == 35
assert 2 * 35 == 70 and 70 * 3 == 210 and 630 * 100 == 63000 and 63000 // 210 == 300 and 630 // 210 == 3 and 3 * 210 == 630
assert 2 * 30 == 60 and 2 * 3 * 12 == 72 and 72 // 6 == 12 and 72 // 12 == 6
assert 2 * 17 == 34 and 34 - 9 == 25 and 9 * 25 == 225 == 15 * 15 and 17 - 9 == 8 and 8 ** 2 + 15 ** 2 == 289 == 17 ** 2


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
                                     centro(c, s, cx, cy + size * 0.36, size, "g", BR, a)))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)


def marca(c, t, t0, n):
    """situação n de 5, com cinco pontos de progresso (como na MAT-ANG-009)"""
    s = f"situação {n} de 5"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", a=a)
        for i in range(5):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def pergunta(c, t, linhas, rel, X=1500, y0=860):
    """linhas da pergunta embaixo à direita: [(t0, partes), ...]; relógio de pausa em rel"""
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, y0 + i * 100, "center", 0.12)
    E.relogio(c, t, rel, X, 430, 180)


def lin(c, t, t0, P, Q, cor=TINTA, larg=6, d=0.6, a=1.0, dash=None):
    if t >= t0 and a > 0:
        M.line(c, *P, *Q, cor, a, larg, dash=dash, progress=ease_io(prog(t, t0, d)))


def ponto(c, t, t0, P, cor=TINTA, r=12, pulsa=False):
    k = ease_back(prog(t, t0, 0.35))
    if k <= 0:
        return
    if pulsa:
        k *= 1 + 0.45 * math.sin(math.pi * M.clamp(prog(t, t0 + 0.2, 0.8)))
    c.drawCircle(*P, r * k, M.paint(cor))


def rot(c, t, t0, s, P, Q, lado=1, cor=None, size=58, gap=16, onde=0.5):
    """rótulo ao lado do segmento PQ (lado = 1 ou −1)"""
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy * lado, -ux * lado
    mx, my = lerp(P[0], Q[0], onde), lerp(P[1], Q[1], onde)
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, s, mx, my, nx, ny, gap, size, "b", cor or COR, a))


def vang(c, t, t0, P, i, rotulo=None, cor=None, r=80, size=56, dentro=False):
    """ângulo interno do vértice i do polígono P"""
    E.angulo(c, t, t0, P[i], P[i - 1], P[(i + 1) % len(P)], rotulo, r=r, cor=cor, size=size, dentro=dentro)


def no_c(O, r, g):
    return O[0] + r * math.cos(math.radians(g)), O[1] - r * math.sin(math.radians(g))


def roda(c, cx, cy, r, giro=0.0, a=1.0, tinta=TINTA):
    """roda de bicicleta (a da MAT-POL-004): pneu grosso, 8 raios finos e o cubo; giro em graus (sentido do relógio)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint("#FFFFFF", 0.6 * a))
    for k in range(8):
        g = math.radians(giro + k * 45)
        M.line(c, cx, cy, cx + r * 0.9 * math.cos(g), cy + r * 0.9 * math.sin(g), TINTA2, a, 3)
    c.drawCircle(cx, cy, r, M.paint(tinta, a, stroke=max(8, r * 0.09)))
    c.drawCircle(cx, cy, max(8, r * 0.07), M.paint(tinta, a))
    g = math.radians(giro + 90)
    c.drawCircle(cx + r * math.cos(g), cy + r * math.sin(g), max(7, r * 0.06), M.paint(E.COR, a))


def rolar(c, t, t0, d, x0, chao, r, dist, a=1.0, rastro=E.COR):
    """a roda anda dist px em d segundos, girando sem escorregar, e deixa no chão o rastro do que percorreu (MAT-POL-004)"""
    if t < t0 or a <= 0:
        return x0
    q = ease_io(prog(t, t0, d))
    x = x0 + dist * q
    M.line(c, x0 - 40, chao, x0 + dist + r + 60, chao, TINTA, a, 4)
    if q > 0:
        M.line(c, x0, chao, x, chao, rastro, a, 12)
    roda(c, x, chao - r, r, math.degrees((x - x0) / r), a)
    return x


def escada(c, t, t0, x, y, passo_x, passo_y, a=1.0, acende=()):
    """a escada do metro (MAT-POL-004): km no alto à esquerda, mm embaixo à direita"""
    nomes = ("km", "hm", "dam", "m", "dm", "cm", "mm")
    for i, s in enumerate(nomes):
        px, py = x + i * passo_x, y + i * passo_y
        ti = t0 + 0.06 * i
        if t >= ti:
            q = ep(t, ti, 0.4) * a
            cor = E.COR if s in acende else TINTA
            M.line(c, px, py, px + passo_x, py, cor, q, 6)
            if i < len(nomes) - 1:
                M.line(c, px + passo_x, py, px + passo_x, py + passo_y, TINTA, q, 6)
            centro(c, s, px + passo_x / 2, py - 18, 46, "g", cor, q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]
    E.frase(c, t, a_ + 0.1, ps("5", "g", 240, COR) + ps("situações", "g", 170, COR), XE, 350, passo=0.25)
    E.frase(c, t, a_ + 1.0, ps("de polígonos e circunferência", "i", 80), XE, 480, passo=0.12)
    E.frase(c, t, a_ + 2.2, ps("criadas para esta aula", "i", 70, TINTA2), XE, 580, passo=0.12)
    for i, (s, cx, ti) in enumerate((("pause", 440, b_), ("resolva", 960, b_ + 0.9), ("confira", 1480, b_ + 2.0))):
        E.foco(c, t, ti, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 800, 56, 64, p),
                                                           E.escreve(c, s, cx - 110, 825, 92, "g", TINTA, p)))
    E.frase(c, t, lerp(b_, C["s01.end"], 0.6), ps("errar aqui", "i", 62) + [("ensina", "g", 66, COR)], W / 2, 980, "center", 0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.1, ps("você vai usar", "i", 84, COR), XE, 200, passo=0.12)
    itens = (("a", "o paralelogramo"), ("b", "a soma dos ângulos"), ("c", "a volta da roda"),
             ("d", "o ângulo inscrito"), ("e", "cordas que se cruzam"))
    for i, (k, s) in enumerate(itens):
        x = XE + 40 + (i // 3) * 860
        y = 380 + (i % 3) * 190
        ti = C[f"s02.{k}"]
        E.foco(c, t, ti, 0.5, lambda p, i=i, x=x, y=y: num_bola(c, str(i + 1), x, y - 28, 46, 54, p))
        E.frase(c, t, ti + 0.1, [(s, "g", 66)], x + 80, y)
    E.frase(c, t, C["s02.end"] - 2.6, ps("travou? procure a aula no canal", "i", 60), XE, 980, passo=0.1)


# ---------------- situação 1: paralelogramo ----------------
QA = (170, 800)
QP = [QA, (QA[0] + 640, QA[1]), (QA[0] + 640 + 420 * math.cos(math.radians(65)), QA[1] - 420 * math.sin(math.radians(65))),
      (QA[0] + 420 * math.cos(math.radians(65)), QA[1] - 420 * math.sin(math.radians(65)))]


def para(c, t, t0, d=0.9):
    E.poligono(c, t, t0, QP, list("ABCD"), preenche=0.06, d=d, size=58)


def b_questao1(c, t, C, b):
    a3, b3, c3, d3 = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.d"]
    marca(c, t, a3, 1)
    para(c, t, b3)
    vang(c, t, c3, QP, 0, "65°", None, 90, 60)
    for i, k in ((1, 0.0), (2, 0.25), (3, 0.5)):
        vang(c, t, d3 + k, QP, i, "?", TINTA2, 70, 60)
    pergunta(c, t, [(b3, ps("terreno:", "i", 60) + [("paralelogramo", "g", 64, COR)]),
                    (d3, ps("e os", "i", 60) + [("outros 3 ângulos?", "g", 64, COR)])], C["s04.a"])


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5, e5 = (C["s05." + k] for k in "abcde")
    X = 1450
    para(c, t, C["s05"] - 1.2, 0.01)
    vang(c, t, C["s05"] - 1.2, QP, 0, "65°", None, 90, 60)
    E.saida(c, t, b5 + 0.4, lambda: vang(c, t, C["s05"] - 1.2, QP, 1, "?", TINTA2, 70, 60))
    vang(c, t, b5 + 0.5, QP, 1, "115°", TINTA2, 70, 60)
    E.saida(c, t, c5 + 0.3, lambda: (vang(c, t, C["s05"] - 1.2, QP, 2, "?", TINTA2, 70, 60), vang(c, t, C["s05"] - 1.2, QP, 3, "?", TINTA2, 70, 60)))
    vang(c, t, c5 + 0.4, QP, 2, "65°", None, 90, 60)
    vang(c, t, c5 + 0.8, QP, 3, "115°", TINTA2, 70, 60)
    if a5 <= t < b5 + 1.0:  # A e B, vizinhos
        k = ep(t, a5, 0.3) * (1 - ep(t, b5 + 0.6, 0.4))
        M.line(c, *QP[0], *QP[1], E.COR, k, 12)
    fcen(c, t, a5, "vizinhos: 180°", X, 220, 70, TINTA2)
    fcen(c, t, b5, "180 − 65 = 115", X, 360, 80)
    E.frase(c, t, c5, ps("de frente:", "i", 62) + [("iguais", "g", 70, COR)], X, 500, "center", 0.12)
    E.frase(c, t, d5, [("65°, 115°, 65°, 115°", "g", 70, CERTO)], X, 650, "center")
    fcen(c, t, e5, "65 + 115 + 65 + 115 = 360", X, 800, 62)
    E.foco(c, t, e5 + 1.0, 0.5, lambda a: E.selo(c, X, 920, 50 * ease_back(prog(t, e5 + 1.0, 0.5)), True, a))


# ---------------- situação 2: decágono regular ----------------
DO, DR = (560, 560), 360


def deca():
    ini = 90 - 180 / 10
    return [(DO[0] + DR * math.cos(math.radians(ini + k * 36)), DO[1] + DR * math.sin(math.radians(ini + k * 36))) for k in range(10)]


DP = deca()
DV = DP[0]                          # vértice de baixo à direita: dele saem as diagonais


def b_questao2(c, t, C, b):
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    marca(c, t, a6, 2)
    E.regular(c, t, b6, 10, *DO, DR, iguais=[1] * 10, preenche=0.06, d=1.2)
    vang(c, t, c6, DP, 0, "?", None, 70, 60)
    if t >= d6:
        for k, j in enumerate(range(2, 9)):
            lin(c, t, d6 + 0.08 * k, DV, DP[j], TINTA2, 4, 0.5, dash=E.TRACO)
    pergunta(c, t, [(c6, ps("cada", "i", 60) + [("ângulo interno?", "g", 64, COR)]),
                    (d6, ps("quantas", "i", 60) + [("diagonais?", "g", 64, COR)])], C["s07.a"])


def b_resposta2(c, t, C, b):
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    X = 1450
    # os 8 triângulos do mesmo vértice, alternando tons
    if c8 <= t < a9:
        k = ep(t, c8, 0.5) * (1 - ep(t, a9 - 0.3, 0.3))
        for j in range(1, 9):
            path = skia.Path(); path.addPoly([DV, DP[j], DP[j + 1]], True)
            c.drawPath(path, M.paint(E.COR if j % 2 else TINTA2, (0.2 if j % 2 else 0.12) * k * ep(t, c8 + 0.1 * j, 0.3)))
    E.regular(c, t, C["s08"] - 1.2, 10, *DO, DR, iguais=[1] * 10, preenche=0.0, d=0.01)
    # externo: o prolongamento do lado de baixo
    ext = (DV[0] + 220, DV[1])
    E.saida(c, t, c8, lambda: (lin(c, t, a8, DV, ext, TINTA2, 4, 0.5, dash=E.TRACO),
                               E.angulo(c, t, a8 + 0.4, DV, ext, DP[9], "36°", r=110, cor=TINTA2, size=56)))
    E.saida(c, t, c8 - 0.2, lambda: vang(c, t, b8, DP, 0, "144°", None, 70, 60))
    if c8 <= t < a9:
        for k, j in enumerate(range(2, 9)):
            lin(c, t, c8 + 0.08 * k, DV, DP[j], TINTA2, 4, 0.4, a=1 - ep(t, a9 - 0.3, 0.3))
    if t >= a9:
        for k, j in enumerate(range(2, 9)):
            lin(c, t, a9 + 0.1 * k, DV, DP[j], E.COR, 6, 0.4)
        ponto(c, t, a9, DV, E.COR, 16, pulsa=True)
    if c9 <= t:  # uma diagonal tem duas pontas
        k = ep(t, c9, 0.3)
        M.line(c, *DV, *DP[5], CERTO, k, 11)
        ponto(c, t, c9 + 0.2, DV, CERTO, 18, pulsa=True)
        ponto(c, t, c9 + 0.6, DP[5], CERTO, 18, pulsa=True)

    def ang():
        E.frase(c, t, C["s08"], ps("pelo", "i", 62) + [("atalho", "g", 68, COR)], X, 200, "center", 0.12)
        fcen(c, t, a8, "externo: 360 ÷ 10 = 36", X, 330, 64, TINTA2)
        fcen(c, t, b8, "interno: 180 − 36 = 144", X, 450, 64)
        E.frase(c, t, c8 - 0.3, ps("pela soma:", "i", 58, TINTA2), X, 600, "center", 0.12)
        fcen(c, t, c8, "10 − 2 = 8 triângulos", X, 700, 62)
        fcen(c, t, c8 + 1.2, "8 × 180 = 1440", X, 800, 66)
        fcen(c, t, d8, "1440 ÷ 10 =", X - 90, 960, 66)
        bola_txt(c, t, d8 + 0.3, "144°", X + 190, 935, 86, 60, CERTO)
    E.saida(c, t, C["s09"] - 0.1, ang)
    if t >= C["s09"]:
        E.frase(c, t, C["s09"], [("diagonais", "g", 76, COR)], X, 220, "center")
        fcen(c, t, a9, "10 − 3 = 7 por vértice", X, 370, 64)
        fcen(c, t, b9, "10 × 7 = 70", X, 510, 80)
        E.frase(c, t, c9, ps("cada uma contada", "i", 58) + [("2 vezes", "g", 64, CERTO)], X, 650, "center", 0.12)
        fcen(c, t, d9, "70 ÷ 2 =", X - 70, 850, 76)
        bola_txt(c, t, d9 + 0.3, "35", X + 150, 822, 86, 80, CERTO)


# ---------------- situação 3: voltas de roda ----------------
def b_questao3(c, t, C, b):
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    marca(c, t, a10, 3)
    R0, cx, cy = 290, 560, 540
    if t >= a10 + 0.3:
        q = ep(t, a10 + 0.3, 0.5)
        M.line(c, 140, cy + R0, 980, cy + R0, TINTA, q, 5)
        E.foco(c, t, a10 + 0.3, 0.6, lambda a: roda(c, cx, cy, R0, 0, a))
    lin(c, t, b10, (cx, cy), no_c((cx, cy), R0, 40), E.COR, 8, 0.5)
    rot(c, t, b10 + 0.4, "35 cm", (cx, cy), no_c((cx, cy), R0, 40), 1, COR, 60)
    pergunta(c, t, [(c10, ps("quantas", "i", 60) + [("voltas", "g", 64, COR)] + ps("em", "i", 60) + [("630 m?", "g", 64)]),
                    (d10, ps("use", "i", 60) + [("π = 3", "g", 64, COR)])], C["s11.a"])


CH, RR, X0 = 760, 130, 140
DIST = 2 * math.pi * RR


def b_resposta3(c, t, C, b):
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    a13, b13, c13, d13, e13 = (C["s13." + k] for k in "abcde")
    X = 1500
    t0 = C["s12"]

    def fig():
        x = rolar(c, t, max(t0, a12 - 0.2), 2.2, X0, CH, RR, DIST) if t >= t0 else X0
        if t < a12 - 0.2:
            M.line(c, X0 - 40, CH, X0 + DIST + RR + 60, CH, TINTA, ep(t, t0, 0.4), 4)
            roda(c, X0, CH - RR, RR, 0, ep(t, t0, 0.4))
        E.foco(c, t, a12 + 2.0, 0.4, lambda a: centro(c, "1 volta", X0 + DIST / 2, CH + 70, 56, "b", COR, a))
        # o diâmetro, em pé, na roda parada
        xf = X0 + DIST
        lin(c, t, c12, (xf, CH - 2 * RR), (xf, CH), E.COR, 8, 0.5)
        E.saida(c, t, C["s13"], lambda: E.foco(c, t, c12 + 0.4, 0.4, lambda a: E._cola(c, "70 cm", xf + RR, CH - RR, 1, 0, 16, 54, "b", COR, a)))
        E.foco(c, t, d12 + 0.4, 0.4, lambda a: centro(c, "210 cm", X0 + DIST / 2, CH + 140, 64, "g", COR, a))
    fig()

    def um():
        E.frase(c, t, a12, ps("1 volta da roda =", "i", 60), X, 240, "center", 0.12)
        E.frase(c, t, a12 + 0.8, [("1 volta no chão", "g", 64, COR)], X, 330, "center")
        E.frase(c, t, b12, ps("com", "i", 58, TINTA2) + [("π = 3:", "g", 56, TINTA2)], X, 470, "center", 0.12)
        E.frase(c, t, b12 + 0.6, ps("volta =", "i", 62) + [("3 × diâmetro", "g", 66)], X, 560, "center", 0.12)
        fcen(c, t, c12, "diâmetro = 70 cm", X, 700, 66)
        fcen(c, t, d12, "70 × 3 = 210 cm", X, 840, 74, COR)
    E.saida(c, t, C["s13"] - 0.1, um)
    if t >= C["s13"]:
        E.frase(c, t, a13, [("mesma unidade", "g", 68, COR)], X, 200, "center")
        escada(c, t, b13 - 0.4, 1190, 320, 90, 40, acende=("m", "cm"))
        fcen(c, t, b13, "630 m = 63 000 cm", X, 640, 66)
        fcen(c, t, c13, "63 000 ÷ 210 =", X - 150, 790, 66)
        bola_txt(c, t, c13 + 0.4, "300", X + 250, 762, 86, 70, CERTO)
        E.frase(c, t, c13 + 0.9, ps("voltas", "i", 54, CERTO), X + 250, 890, "center")
        fcen(c, t, d13, "630 ÷ 210 = 3", X - 60, 990, 62, ERRADO)
        E.foco(c, t, e13, 0.5, lambda a: E.selo(c, X + 240, 968, 40 * ease_back(prog(t, e13, 0.5)), False, a))


# ---------------- situação 4: inscrito e arco ----------------
AO, AR = (560, 560), 330           # raio 12
AA, AB, AV = no_c(AO, AR, -30), no_c(AO, AR, 30), no_c(AO, AR, 180)


def arco_ab(c, t, t0, cor=None, larg=14, a=1.0):
    q = ease_io(prog(t, t0, 0.6))
    if q <= 0 or a <= 0:
        return
    ret = skia.Rect.MakeXYWH(AO[0] - AR, AO[1] - AR, 2 * AR, 2 * AR)
    c.drawArc(ret, 30, -60 * q, False, M.paint(cor or E.COR, a, stroke=larg, cap_round=True))


def fig4(c, t, t0, t_raio, t_ins, d=0.8):
    E.circulo(c, t, t0, *AO, AR, o="O", raio=(110, "12"), te={"raio": t_raio}, size=60, d=d)
    arco_ab(c, t, t_ins + 0.5)
    lin(c, t, t_ins, AV, AA, TINTA, 6, 0.6)
    lin(c, t, t_ins, AV, AB, TINTA, 6, 0.6)
    for P in (AA, AB, AV):
        ponto(c, t, t_ins + 0.5, P, TINTA, 11)
    E.angulo(c, t, t_ins + 0.6, AV, AA, AB, "30°", r=130, size=58)


def b_questao4(c, t, C, b):
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    marca(c, t, a14, 4)
    fig4(c, t, b14 - 0.3, b14 + 0.4, c14)
    E.foco(c, t, d14, 0.4, lambda a: E._cola(c, "?", *no_c(AO, AR + 10, 0), 1, 0, 16, 80, "g", COR, a))
    pergunta(c, t, [(d14, ps("comprimento", "i", 60) + [("do arco?", "g", 64, COR)]),
                    (d14 + 1.0, ps("use", "i", 60) + [("π = 3", "g", 64, COR)])], C["s15.a"])


def b_resposta4(c, t, C, b):
    a16, b16 = C["s16.a"], C["s16.b"]
    a17, b17, c17, d17, e17 = (C["s17." + k] for k in "abcde")
    X = 1500
    # a volta em 6 pedaços de 60°
    if t >= a17:
        for k in range(6):
            M.line(c, *AO, *no_c(AO, AR, -30 + 60 * k), TINTA2, ep(t, a17 + 0.08 * k, 0.4) * 0.6, 3, dash=E.TRACO)
    fig4(c, t, C["s16"] - 1.2, C["s16"] - 1.2, C["s16"] - 1.2, d=0.01)
    lin(c, t, a16, AO, AA, E.COR, 7, 0.5)
    lin(c, t, a16, AO, AB, E.COR, 7, 0.5)
    E.angulo(c, t, a16 + 0.5, AO, AA, AB, "60°", r=90, size=58, preenche=0.3)
    E.saida(c, t, b17 + 0.3, lambda: E.foco(c, t, C["s16"] - 1.2, 0.4, lambda a: E._cola(c, "?", *no_c(AO, AR + 10, 0), 1, 0, 16, 80, "g", COR, a)))
    E.foco(c, t, b17 + 0.4, 0.4, lambda a: E._cola(c, "12 cm", *no_c(AO, AR + 10, 0), 1, 0, 16, 64, "g", CERTO, a))
    if t >= b17:
        arco_ab(c, t, b17, CERTO, 16)

    def um():
        E.frase(c, t, C["s16"] + 0.2, ps("inscrito = metade do central", "i", 54, TINTA2), X, 230, "center", 0.1)
        fcen(c, t, a16, "central = 2 × 30 = 60°", X, 360, 64, COR)
        E.frase(c, t, b16, ps("a volta inteira:", "i", 58), X, 520, "center", 0.12)
        fcen(c, t, b16 + 0.6, "2 · 3 · 12 = 72 cm", X, 630, 70)
    E.saida(c, t, C["s17"] - 0.1, um)
    if t >= C["s17"]:
        fcen(c, t, a17, "60° = f{1}{6} da volta", X, 230, 66)
        fcen(c, t, b17, "72 ÷ 6 =", X - 90, 420, 74)
        bola_txt(c, t, b17 + 0.3, "12 cm", X + 160, 392, 96, 58, CERTO)
        E.frase(c, t, c17, ps("com os", "i", 58, ERRADO) + [("30° direto:", "g", 62, ERRADO)], X, 600, "center", 0.12)
        fcen(c, t, d17, "72 ÷ 12 = 6 cm", X, 710, 66, ERRADO)
        E.frase(c, t, d17 + 0.8, ps("a metade do certo", "i", 52, ERRADO), X, 790, "center", 0.1)
        E.foco(c, t, e17, 0.5, lambda a: E.pilula(c, "o arco segue o central", X, 920, 56, "g", a=a, cor=E.SOBRE))


# ---------------- situação 5: a água no cano ----------------
CO, CK = (560, 500), 18            # raio 17 → 306 px; água com 9 de fundura: superfície a 8 do centro
CR = 17 * CK
CS1, CS2 = (CO[0] - 15 * CK, CO[1] + 8 * CK), (CO[0] + 15 * CK, CO[1] + 8 * CK)
CM, CF, CT = (CO[0], CO[1] + 8 * CK), (CO[0], CO[1] + 17 * CK), (CO[0], CO[1] - 17 * CK)
assert abs(math.dist(CS1, CO) - CR) < 0.5


def agua(c, t, t0, d=0.6):
    """a água: o pedaço do círculo abaixo da superfície, que enche de baixo para cima"""
    q = ease_io(prog(t, t0, d))
    if q <= 0:
        return
    ret = skia.Rect.MakeXYWH(CO[0] - CR, CO[1] - CR, 2 * CR, 2 * CR)
    g = math.degrees(math.atan2(CS2[1] - CO[1], CS2[0] - CO[0]))
    path = skia.Path()
    path.arcTo(ret, g, 180 - 2 * g, True); path.close()
    c.save()
    c.clipRect(skia.Rect.MakeLTRB(0, lerp(CF[1], CM[1], q), W, H))
    c.drawPath(path, M.paint("#4FA3E0", 0.35))
    c.restore()
    M.line(c, *CS1, *CS2, "#2C7FC0", q, 5)


def cano(c, t, t0):
    if t < t0:
        return
    q = ep(t, t0, 0.6)
    c.drawCircle(*CO, CR + 12, M.paint("#9A9AA6", q, stroke=24))
    c.drawCircle(*CO, CR, M.paint(TINTA, q, stroke=5))


def b_questao5(c, t, C, b):
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    marca(c, t, a18, 5)
    agua(c, t, c18)
    cano(c, t, b18 - 0.2)
    ponto(c, t, b18 + 0.2, CO, TINTA, 9)
    lin(c, t, b18 + 0.3, CO, no_c(CO, CR, 135), E.COR, 7, 0.5)
    rot(c, t, b18 + 0.7, "17", CO, no_c(CO, CR, 135), 1, COR, 60)
    E.segmento(c, t, c18 + 0.5, CM, CF, "9", cor=TINTA2, tracejado=True, pontas=False, lado=-1, size=60, largura=5)
    if t >= d18:
        q = ep(t, d18, 0.4)
        M.line(c, *CS1, *CS2, E.COR, q, 9)
        E.foco(c, t, d18 + 0.3, 0.4, lambda a: E._cola(c, "?", CM[0] - 140, CM[1], 0, -1, 14, 76, "g", COR, a))
    pergunta(c, t, [(b18, ps("cano de", "i", 60) + [("raio 17 cm", "g", 64, COR)]),
                    (d18, ps("largura da", "i", 60) + [("água?", "g", 64, COR)])], C["s19.a"])


def b_resposta5(c, t, C, b):
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    a21, b21, c21, d21, e21, f21 = (C["s21." + k] for k in "abcdef")
    X = 1500
    t0 = C["s20"] - 1.2
    if t >= f21 - 0.2:
        path = skia.Path(); path.addPoly([CO, CM, CS2], True)
        c.drawPath(path, M.paint(E.COR, 0.18 * ep(t, f21 - 0.2, 0.4)))
    agua(c, t, t0, 0.01)
    cano(c, t, t0)
    ponto(c, t, t0, CO, TINTA, 9)
    M.line(c, *CS1, *CS2, E.COR, 1, 9)
    lin(c, t, a20, CT, CF, E.COR, 7, 0.7)
    ponto(c, t, a20 + 0.6, CF, E.COR, 12, pulsa=True)
    E.angulo(c, t, b20, CM, CF, CS2, r=34, reto=True)
    q = ep(t, b20 + 0.4, 0.4)
    E.marcas_iguais(c, CS1, CM, 2, TINTA, q); E.marcas_iguais(c, CM, CS2, 2, TINTA, q)
    E.foco(c, t, c20, 0.4, lambda a: E._cola(c, "34", CO[0], (CT[1] + CO[1]) / 2 - 40, -1, 0, 18, 60, "b", COR, a))
    rot(c, t, c20 + 0.6, "9", CM, CF, -1, TINTA2, 58)
    rot(c, t, d20, "25", CT, CM, -1, TINTA2, 58, onde=0.7)
    E.saida(c, t, c21, lambda: E.foco(c, t, t0, 0.4, lambda a: E._cola(c, "?", CM[0] - 140, CM[1], 0, -1, 14, 70, "g", COR, a)))
    rot(c, t, c21, "15", CS1, CM, 1, COR, 58, onde=0.3)
    rot(c, t, c21 + 0.3, "15", CM, CS2, 1, COR, 58, onde=0.6)
    if t >= d21:
        M.line(c, *CS1, *CS2, CERTO, ep(t, d21, 0.4), 11)
    rot(c, t, e21, "8", CO, CM, 1, COR, 58)
    lin(c, t, f21 - 0.2, CO, CS2, TINTA, 6, 0.5)
    rot(c, t, f21 + 0.2, "17", CO, CS2, 1, TINTA2, 56)

    def um():
        E.frase(c, t, a20, ps("trace o", "i", 62) + [("diâmetro em pé", "g", 66, COR)], X, 220, "center", 0.12)
        E.frase(c, t, b20, ps("corta a superfície", "i", 58), X, 350, "center", 0.12)
        E.frase(c, t, b20 + 0.6, [("ao meio", "g", 70, COR)], X, 440, "center")
        E.frase(c, t, lerp(b20, c20, 0.6), ps("2 cordas que se cruzam", "i", 56, TINTA2), X, 570, "center", 0.1)
        fcen(c, t, c20, "2 × 17 = 34", X, 700, 74)
        fcen(c, t, d20, "34 − 9 = 25", X, 830, 74)
    E.saida(c, t, C["s21"] - 0.1, um)
    if t >= C["s21"]:
        E.frase(c, t, C["s21"], ps("pedaço × pedaço", "i", 62, COR), X, 190, "center", 0.12)
        fcen(c, t, a21, "9 × 25 = 225", X, 300, 72)
        fcen(c, t, b21, "15 × 15 = 225", X, 410, 72, COR)
        E.frase(c, t, c21, ps("metade:", "i", 60) + [("15", "g", 70, COR)], X - 150, 560, "center", 0.12)
        bola_txt(c, t, d21, "30 cm", X + 170, 535, 96, 60, CERTO)
        fcen(c, t, e21, "17 − 9 = 8", X, 720, 66, TINTA2)
        fcen(c, t, f21, "8^2 + 15^2 = 289 = 17^2", X, 850, 62)
        E.foco(c, t, f21 + 1.6, 0.5, lambda a: E.selo(c, X, 960, 46 * ease_back(prog(t, f21 + 1.6, 0.5)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s22.a", "desenhe a figura"), ("s22.b", "mesma unidade"), ("s22.c", "confira se faz sentido"))
        for i, (k, s) in enumerate(itens):
            y = 420 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 480, y - 30, 56, 64, a))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 580, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"] + 0.2, ps("próxima aula: uma parte nova", "i", 76), XE, 260, passo=0.1)
    E.frase(c, t, C["s23"] + 1.2, [("Simetrias", "g", 130, COR)], XE, 420)
    E.frase(c, t, C["s23.a"], ps("o eixo: duas metades que se encaixam", "i", 56), XE, 540, passo=0.1)
    E.frase(c, t, C["s23.b"], ps("dobre, corte e abra", "i", 60) + [("o papel", "g", 64, COR)], XE, 640, passo=0.1)
    # uma folha com o eixo tracejado e o recorte simétrico
    if t >= C["s23.a"]:
        q = ep(t, C["s23.a"] + 0.2, 0.5)
        cx, cy = 900, 870
        pts = [(cx, cy - 150), (cx + 90, cy - 60), (cx + 200, cy - 90), (cx + 140, cy + 30), (cx + 60, cy + 130), (cx, cy + 80),
               (cx - 60, cy + 130), (cx - 140, cy + 30), (cx - 200, cy - 90), (cx - 90, cy - 60)]
        path = skia.Path(); path.addPoly(pts, True)
        c.drawPath(path, M.paint(E.COR, 0.18 * q))
        pa = M.paint(TINTA, q, stroke=5); pa.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(path, pa)
        M.line(c, cx, cy - 190, cx, cy + 170, E.COR, q, 5, dash=E.TRACO)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1630, p), lerp(720, 425, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], 1450, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
