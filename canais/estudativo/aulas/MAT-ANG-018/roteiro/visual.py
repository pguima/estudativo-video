"""Visual — Estudativo · MAT-ANG-018: relações métricas no triângulo retângulo (a · h = b · c e h² = m · n; no 3-4-5, h = 2,4).
Linguagem da geometria plana (MAT-ANG-001 a 020): lados em tinta; ângulo reto = quadradinho; ângulos iguais com a mesma cor
(o ângulo de baixo à esquerda em COR, índigo; o de baixo à direita em TINTA2); medidas na grotesca; erro em vermelho,
certo em verde; resposta na esfera; atalho no palco escuro.
Figura: o ângulo reto em cima (A), a hipotenusa deitada embaixo (B à esquerda, C à direita), a altura h de A até H.
Os pedaços: m (sob o cateto c, em TINTA2) e n (sob o cateto b, em AMBAR). As medidas são as de verdade (3-4-5: m = 1,8,
n = 3,2, h = 2,4; 4 e 9: h = 6; 9-12-15 e 2-8): a figura não mente.
Os triângulos pequenos saem do grande e "voam" (os vértices deslizam até a nova posição, como o voa() da MAT-ANG-002)
para ficar na mesma posição do grande: o reto em cima, o lado de frente para ele embaixo. Assim os lados correspondentes
ficam no mesmo lugar, e cada par ganha uma cor (o primeiro par em AMBAR, o segundo em COR).
Peças locais: geo() (vértices a partir de m, n, h), fig() (triângulo com altura e rótulos), tri() (triângulo solto, com
contorno e rótulos nos lados), copia() (o pequeno que voa até a posição do grande), txt_lado(), grosso(), pergunta().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-018_relacoes_metricas_no_triangulo_retangulo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("nomes", "relacao1", "relacao2", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
assert abs(3 * 3 / 5 - 1.8) < 1e-9 and abs(4 * 4 / 5 - 3.2) < 1e-9 and abs(3 * 4 / 5 - 2.4) < 1e-9
assert abs(1.8 * 3.2 - 5.76) < 1e-9 and abs(2.4 ** 2 - 5.76) < 1e-9 and 4 * 9 == 36 == 6 ** 2 and 2.5 * 2.5 == 6.25
assert abs(2 * 2.4 - 4.8) < 1e-9 and abs(10 * 2.4 - 24) < 1e-9 and abs(3 * 2.4 - 7.2) < 1e-9
assert 9 * 12 == 108 and 9 ** 2 + 12 ** 2 == 15 ** 2 and abs(108 / 15 - 7.2) < 1e-9 and 108 // 3 == 36 and 15 // 3 == 5
assert 2 * 8 == 16 == 4 ** 2 and 7.2 < 9 and 7.2 < 12


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


def geo(B, u, m, n, h):
    """vértices do triângulo com a hipotenusa deitada: B (esq.), C (dir.), H (pé da altura), A (o reto, em cima)"""
    Cc = (B[0] + (m + n) * u, B[1])
    Hh = (B[0] + m * u, B[1])
    A = (Hh[0], B[1] - h * u)
    return dict(B=B, C=Cc, H=Hh, A=A, G=((B[0] + Cc[0] + A[0]) / 3, (B[1] + Cc[1] + A[1]) / 3))


def tri(c, pts, a=1.0, fundo=None, alfa=0.14, larg=6, tinta=TINTA, p=1.0):
    if a <= 0:
        return
    if fundo:
        path = skia.Path(); path.addPoly(list(pts), True)
        c.drawPath(path, M.paint(fundo, alfa * a))
    E._contorno(c, list(pts), p, tinta, larg) if a >= 1 else None
    if a < 1:
        c.saveLayerAlpha(None, int(255 * a))
        E._contorno(c, list(pts), p, tinta, larg)
        c.restore()


def fig(c, t, t0, g, rot=None, th=None, altura=True, retos=True, d=0.9, size=58, tl=None):
    """triângulo com a hipotenusa embaixo e, a partir de th, a altura AH com o quadradinho em H.
    rot = dict com os rótulos {'a', 'b', 'c', 'h'} (texto, cor) e tl = instante de cada rótulo"""
    B, Cc, Hh, A, G = g["B"], g["C"], g["H"], g["A"], g["G"]
    E.triangulo(c, t, t0, B, Cc, A, vertices=None, retos=(2,) if retos else (), preenche=0.05, d=d)
    if altura and th is not None and t >= th:
        M.line(c, *A, *Hh, TINTA, 1.0, 5, progress=ease_io(prog(t, th, 0.6)))
        E.angulo(c, t, th + 0.5, Hh, Cc, A, r=36)
    rot = rot or {}
    tl = tl or {}
    lados = dict(a=(B, Cc), b=(A, Cc), c=(B, A), h=(A, Hh))
    for k, (s, cor) in rot.items():
        P, Q = lados[k]
        ti = tl.get(k, t0 + d)
        if k == "h":
            E.foco(c, t, ti, 0.4, lambda a, s=s, cor=cor: E.formula(c, s, Hh[0] + 18, (A[1] + Hh[1]) / 2 + size * 0.36, size, "b", cor, a, "left"))
        else:
            E.foco(c, t, ti, 0.4, lambda a, P=P, Q=Q, s=s, cor=cor: txt_lado(c, P, Q, s, G, size, cor, a))


def pedacos(c, t, t0, g, sm, sn, cm=TINTA2, cn=AMBAR, size=54, y_off=60, a=1.0):
    """m e n embaixo da hipotenusa, com a linha de cota de cada pedaço"""
    B, Cc, Hh = g["B"], g["C"], g["H"]
    k = ep(t, t0, 0.5) * a
    if k <= 0:
        return
    y = B[1] + 26
    for P, Q, s, cor in ((B, Hh, sm, cm), (Hh, Cc, sn, cn)):
        M.line(c, P[0] + 6, y, Q[0] - 6, y, cor, k, 5)
        for X in (P[0] + 6, Q[0] - 6):
            M.line(c, X, y - 10, X, y + 10, cor, k, 4)
        E.formula(c, s, (P[0] + Q[0]) / 2, y + y_off, size, "b", cor, k, "center")


def copia(c, t, t0, d, orig, alvo, a=1.0, fundo=None):
    """o pequeno que voa: cada vértice desliza de orig[i] até alvo[i]. Devolve os pontos do instante"""
    p = ease_io(prog(t, t0, d))
    lift = 30 * math.sin(math.pi * p)
    pts = [(lerp(o[0], v[0], p), lerp(o[1], v[1], p) - lift) for o, v in zip(orig, alvo)]
    if t >= t0:
        tri(c, pts, a, fundo, 0.2)
    return pts


def pergunta(c, t, linhas, rel, X=1500, y0=780):
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, y0 + i * 95, "center", 0.12)
    E.relogio(c, t, rel, X, 380, 170)


# ---------------- figuras ----------------
G1 = geo((150, 820), 150, 1.8, 3.2, 2.4)        # o 3-4-5 grande (gancho, nomes, semelhança, erro)
G7 = geo((110, 870), 130, 1.8, 3.2, 2.4)        # o 3-4-5 da relação 1
K1 = geo((900, 870), 130 * 3 / 5, 1.8, 3.2, 2.4)     # alvo do pequeno da esquerda (hipotenusa c = 3)
G10 = geo((90, 540), 100, 1.8, 3.2, 2.4)        # o 3-4-5 da relação 2 (em cima à esquerda)
K10a = geo((700, 560), 110 * 3 / 5, 1.8, 3.2, 2.4)   # pequeno da esquerda
K10b = geo((1120, 560), 110 * 4 / 5, 1.8, 3.2, 2.4)  # pequeno da direita (hipotenusa b = 4)
G11 = geo((130, 860), 50, 4, 9, 6)              # pedaços 4 e 9
GQ1 = geo((120, 640), 33, 5.4, 9.6, 7.2)        # questão 1: catetos 9 e 12
GQ2 = geo((700, 640), 45, 2, 8, 4)              # questão 2: pedaços 2 e 8
GR1 = geo((110, 860), 46, 5.4, 9.6, 7.2)
GR2 = geo((160, 860), 70, 2, 8, 4)
assert abs(math.dist(G1["B"], G1["A"]) - 3 * 150) < 1e-6 and abs(math.dist(G1["A"], G1["C"]) - 4 * 150) < 1e-6
assert abs(math.dist(GQ1["B"], GQ1["A"]) / 33 - 9) < 1e-6 and abs(math.dist(GQ1["A"], GQ1["C"]) / 33 - 12) < 1e-6


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    g = G1
    X = 1440

    def um():
        fig(c, t, a1, g, dict(c=("3", TINTA), b=("4", TINTA), a=("5", TINTA)), th=b1, tl=dict(c=a1 + 0.6, b=a1 + 0.7, a=a1 + 0.9))
        E.saida(c, t, d1, lambda: E.foco(c, t, b1 + 0.6, 0.4, lambda a: E.formula(c, "h = ?", g["H"][0] + 18, (g["A"][1] + g["H"][1]) / 2 + 20, 60, "b", COR, a, "left")))
        E.foco(c, t, d1, 0.4, lambda a: E.formula(c, "2,4", g["H"][0] + 18, (g["A"][1] + g["H"][1]) / 2 + 20, 64, "b", CERTO, a, "left"))
        # o chute: a altura no meio
        if c1 <= t < d1 + 0.6:
            k = ep(t, c1, 0.4) * (1 - ep(t, d1, 0.5))
            mx = (g["B"][0] + g["C"][0]) / 2
            M.line(c, mx, g["B"][1], mx, g["B"][1] - 2.5 * 150, ERRADO, k, 5, dash=E.TRACO)
        E.frase(c, t, a1 + 0.3, ps("catetos", "i", 66) + [("3", "g", 76), ("e", "i", 66), ("4", "g", 76)], X, 230, "center", 0.12)
        E.frase(c, t, b1, ps("a altura do reto até a", "i", 60) + [("hipotenusa", "g", 64, COR)], X, 350, "center", 0.1)
        fcen(c, t, c1, "2,5?", X, 560, 120, ERRADO)
        E.risco(c, X - 150, 530, X + 150, 515, t, d1 - 0.2, ERRADO, 12)
        bola_txt(c, t, d1, "2,4", X, 780, 120, 96)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.15), [("2 relações", "g", 110, COR)], XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("métricas", "g", 110, COR)], XE, 600, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), ps("contas rápidas entre as medidas", "i", 66, TINTA2), XE, 730, passo=0.1)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.2, ps("você precisa de", "i", 80, COR), XE, 190, passo=0.12)
    xg = XE + E.larg("você precisa de", "i", 80) + 30
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3 coisas", xg, 190, 84, "g", COR, a))
    itens = (("b", "teorema de Pitágoras", "a^2 = b^2 + c^2", None),
             ("c", "2 ângulos iguais:", None, "semelhantes, lados proporcionais"),
             ("d", "a cruz", "f{x}{y} = f{z}{w}  →  x · w = y · z", None))
    for i, (k, tit, form, sub) in enumerate(itens):
        y = 380 + i * 210
        ti = C[f"s03.{k}"]
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 50, y - 28, 50, a=a), centro(c, str(i + 1), XE + 50, y - 6, 60, "g", BR, a)))
        E.frase(c, t, ti + 0.1, [(tit, "g", 70)], XE + 140, y)
        if form:
            w = E.larg(tit, "g", 70)
            E.formula_em(c, t, ti + 0.8, form, XE + 140 + w + 60, y, 66, "g", COR)
        else:
            E.frase(c, t, ti + 0.8, ps(sub, "i", 60, TINTA2), XE + 140, y + 76, passo=0.08)
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), XE, 1000, "left", 0.12)


# ---------------- nomes ----------------
def b_nomes(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    g = G1
    X = 1440
    fig(c, t, C["s04"], g, dict(a=("a", COR), b=("b", TINTA), c=("c", TINTA), h=("h", AMBAR)), th=c4,
        tl=dict(a=a4, b=b4, c=b4 + 0.2, h=c4 + 0.5))
    grosso(c, g["B"], g["C"], COR, ep(t, a4, 0.4) * (1 - 0.6 * ep(t, a5, 0.4)), 10)
    grosso(c, g["A"], g["H"], AMBAR, ep(t, c4 + 0.3, 0.4), 8)
    pedacos(c, t, b5, g, "m", "n")
    if t >= c5:  # a sombra: cada cateto com a cor do seu pedaço
        k = ep(t, c5, 0.5)
        grosso(c, g["B"], g["A"], TINTA2, k, 12)
        grosso(c, g["A"], g["C"], AMBAR, k, 12)
        for P, Q, cor in ((g["B"], g["H"], TINTA2), (g["H"], g["C"], AMBAR)):
            path = skia.Path(); path.addPoly([P, Q, g["A"]], True)
            c.drawPath(path, M.paint(cor, 0.12 * k))

    def quatro():
        E.frase(c, t, a4, [("a", "g", 70, COR)] + ps("= hipotenusa", "i", 62), X, 260, "center", 0.12)
        E.frase(c, t, b4, [("b, c", "g", 70)] + ps("= catetos", "i", 62), X, 380, "center", 0.12)
        E.frase(c, t, c4, [("h", "g", 70, AMBAR)] + ps("= altura relativa", "i", 62), X, 500, "center", 0.12)
        E.frase(c, t, c4 + 0.8, ps("à hipotenusa", "i", 62), X, 580, "center", 0.12)
    E.saida(c, t, C["s05"] - 0.1, quatro)
    if t >= C["s05"] - 0.1:
        E.frase(c, t, a5, ps("a altura parte a hipotenusa", "i", 60), X, 260, "center", 0.1)
        E.frase(c, t, a5 + 0.4, ps("em", "i", 60) + [("2 pedaços", "g", 66)], X, 340, "center", 0.12)
        E.frase(c, t, b5, [("m", "g", 80, TINTA2), ("e", "i", 70), ("n", "g", 80, AMBAR)], X, 480, "center", 0.2)
        E.frase(c, t, c5, ps("projeções:", "i", 60) + [("a sombra", "g", 66)], X, 620, "center", 0.12)
        E.frase(c, t, c5 + 0.8, ps("de cada cateto", "i", 60), X, 700, "center", 0.12)


# ---------------- semelhança ----------------
def b_semelhanca(c, t, C, b):
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    g = G1
    B, Cc, Hh, A = g["B"], g["C"], g["H"], g["A"]
    X = 1440
    fig(c, t, C["s06"] - 1.0, g, th=C["s06"] - 1.0, d=0.01)
    k = ep(t, a6, 0.5)
    for pts, cor in (([B, Hh, A], TINTA2), ([Hh, Cc, A], AMBAR)):
        path = skia.Path(); path.addPoly(pts, True)
        c.drawPath(path, M.paint(cor, 0.16 * k))
    if t >= b6:  # os retos dos três
        E.angulo(c, t, b6, Hh, B, A, r=36)
    # os agudos: o de B em COR, o de C em TINTA2, e as cópias deles no topo
    E.angulo(c, t, c6, B, Cc, A, r=90, cor=COR)
    E.angulo(c, t, c6 + 0.6, A, B, Hh, r=70, cor=TINTA2)
    E.angulo(c, t, c6 + 0.3, Cc, B, A, r=90, cor=TINTA2)
    E.angulo(c, t, c6 + 0.9, A, Hh, Cc, r=56, cor=COR)
    E.frase(c, t, a6, [("2", "g", 76, COR)] + ps("triângulos pequenos", "i", 62), X, 260, "center", 0.12)
    E.frase(c, t, a6 + 0.8, ps("dentro do grande", "i", 62), X, 340, "center", 0.12)
    E.frase(c, t, b6, ps("cada um:", "i", 60) + [("1 ângulo reto", "g", 64)], X, 480, "center", 0.12)
    E.frase(c, t, c6, [("+ 1 agudo", "g", 64, COR)] + ps("em comum", "i", 60), X, 580, "center", 0.12)
    E.foco(c, t, d6, 0.5, lambda a: E.pilula(c, "os 3 são semelhantes", X, 760, 64, "g", a=a, cor=E.SOBRE))


# ---------------- relação 1: a · h = b · c ----------------
def b_relacao1(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8 = C["s08.a"], C["s08.b"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    g, k = G7, K1
    B, Cc, Hh, A = g["B"], g["C"], g["H"], g["A"]
    X = 1380
    fig(c, t, C["s07"] - 1.0, g, dict(a=("a", TINTA), b=("b", TINTA), c=("c", TINTA), h=("h", TINTA)), th=C["s07"] - 1.0, d=0.01,
        tl=dict(a=C["s07"] - 1, b=C["s07"] - 1, c=C["s07"] - 1, h=C["s07"] - 1), size=52)
    # o pequeno da esquerda (B, H, A) voa até ficar como o grande: B → B', H → A', A → C'
    tv = C["s07"] + 0.8
    pts = copia(c, t, tv, 1.6, [B, Hh, A], [k["B"], k["A"], k["C"]], fundo=TINTA2)
    if t >= tv + 1.6:
        Bp, Ap, Cp = k["B"], k["A"], k["C"]
        E.angulo(c, t, tv + 1.6, Ap, Bp, Cp, r=30)
        E.foco(c, t, tv + 1.8, 0.4, lambda a: (txt_lado(c, Bp, Ap, "m", k["G"], 50, TINTA, a), txt_lado(c, Ap, Cp, "h", k["G"], 50, TINTA, a),
                                               txt_lado(c, Bp, Cp, "c", k["G"], 50, TINTA, a)))
        E.angulo(c, t, tv + 2.0, Bp, Cp, Ap, r=56, cor=COR)
    E.angulo(c, t, C["s07"], B, Cc, A, r=80, cor=COR)
    # par 1: h (pequeno) e b (grande), de frente para o ângulo de B
    p1 = ep(t, a7, 0.4)
    grosso(c, k["A"], k["C"], AMBAR, p1, 10)
    grosso(c, A, Cc, AMBAR, ep(t, lerp(a7, b7, 0.5), 0.4), 10)
    # par 2: c (pequeno) e a (grande), de frente para o reto
    grosso(c, k["B"], k["C"], COR, ep(t, b7, 0.4), 10)
    grosso(c, B, Cc, COR, ep(t, b7 + 0.4, 0.4), 10)

    def intro():
        E.frase(c, t, C["s07"] + 0.3, ps("lado correspondente:", "i", 62), X, 210, "center", 0.12)
        E.frase(c, t, C["s07"] + 1.6, [("de frente", "g", 66)] + ps("para o mesmo ângulo", "i", 62), X, 300, "center", 0.12)
        E.frase(c, t, a7, [("h", "g", 70, AMBAR)] + ps("↔", "g", 60) + [("b", "g", 70, AMBAR)], X - 170, 450, "center", 0.15)
        E.frase(c, t, b7, [("c", "g", 70, COR)] + ps("↔", "g", 60) + [("a", "g", 70, COR)], X + 170, 450, "center", 0.15)
    E.saida(c, t, c7 - 0.1, intro)
    fcen(c, t, c7, "f{h}{b} = f{c}{a}", X, 300, 100)

    def oito():
        E.foco(c, t, a8 - 0.1, 0.5, lambda a: E.caixa_pontilhada(c, X - 270, 400, 540, 130, a, COR, prog_=ep(t, a8 - 0.1, 0.6)))
        fcen(c, t, a8, "a · h = b · c", X, 495, 90, COR)
        E.frase(c, t, b8, ps("hipotenusa × altura = cateto × cateto", "i", 50, TINTA2), X, 600, "center", 0.08)
    E.saida(c, t, C["s09"] - 0.1, oito)
    if t >= C["s09"] - 0.1:
        fcen(c, t, C["s09"], "a · h = b · c", X, 460, 76, COR)
        fcen(c, t, a9, "5 · h = 3 · 4 = 12", X, 590, 76)
        E.foco(c, t, b9, 0.4, lambda a: E.pilula(c, "÷ 5 dos dois lados", X - 60, 680, 44, "g", fundo=TINTA, a=a))
        bola_txt(c, t, c9, "h = f{12}{5} = 2,4", 1540, 860, 150, 56)


# ---------------- relação 2: h² = m · n ----------------
def b_relacao2(c, t, C, b):
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    X = W / 2

    def dez():
        g = G10
        B, Cc, Hh, A = g["B"], g["C"], g["H"], g["A"]
        fig(c, t, C["s10"] - 1.0, g, dict(h=("h", TINTA)), th=C["s10"] - 1.0, d=0.01, tl=dict(h=C["s10"] - 1), size=46)
        pedacos(c, t, C["s10"] - 1.0, g, "m", "n", TINTA2, TINTA2, 44, 50)
        # os dois pequenos voam: esquerda (B, H, A) → K10a; direita (A, H, C) → K10b
        copia(c, t, a10, 1.4, [B, Hh, A], [K10a["B"], K10a["A"], K10a["C"]], fundo=TINTA2)
        copia(c, t, a10 + 0.6, 1.4, [A, Hh, Cc], [K10b["B"], K10b["A"], K10b["C"]], fundo=AMBAR)
        for kk, (lb, lr, lh), t0 in ((K10a, ("m", "h", "c"), a10 + 1.4), (K10b, ("h", "n", "b"), a10 + 2.0)):
            if t >= t0:
                Bp, Ap, Cp = kk["B"], kk["A"], kk["C"]
                E.angulo(c, t, t0, Ap, Bp, Cp, r=26)
                E.angulo(c, t, t0 + 0.3, Bp, Cp, Ap, r=46, cor=COR)
                E.foco(c, t, t0 + 0.2, 0.4, lambda a, Bp=Bp, Ap=Ap, Cp=Cp, kk=kk, lb=lb, lr=lr: (txt_lado(c, Bp, Ap, lb, kk["G"], 48, TINTA, a),
                                                                                              txt_lado(c, Ap, Cp, lr, kk["G"], 48, TINTA, a)))
        # pares: h (esq.) com n (dir.), de frente para o ângulo em COR; m (esq.) com h (dir.)
        tp1, tp2 = lerp(a10, b10, 0.45), lerp(a10, b10, 0.75)
        grosso(c, K10a["A"], K10a["C"], AMBAR, ep(t, tp1, 0.4), 10)
        grosso(c, K10b["A"], K10b["C"], AMBAR, ep(t, tp1 + 0.3, 0.4), 10)
        grosso(c, K10a["B"], K10a["A"], COR, ep(t, tp2, 0.4), 10)
        grosso(c, K10b["B"], K10b["A"], COR, ep(t, tp2 + 0.3, 0.4), 10)
        E.frase(c, t, tp1, [("h", "g", 64, AMBAR)] + ps("↔", "g", 54) + [("n", "g", 64, AMBAR)], 1700, 300, "center", 0.15)
        E.frase(c, t, tp2, [("m", "g", 64, COR)] + ps("↔", "g", 54) + [("h", "g", 64, COR)], 1700, 420, "center", 0.15)
        fcen(c, t, b10, "f{h}{n} = f{m}{h}", 560, 840, 96)
        E.foco(c, t, c10 - 0.1, 0.5, lambda a: E.caixa_pontilhada(c, 980, 730, 520, 150, a, COR, prog_=ep(t, c10 - 0.1, 0.6)))
        fcen(c, t, c10, "h^2 = m · n", 1240, 840, 100, COR)
        E.frase(c, t, d10, ps("a altura ao quadrado é o", "i", 56) + [("produto dos pedaços", "g", 60)], X, 990, "center", 0.1)
    E.saida(c, t, C["s11"] - 0.1, dez)
    if C["s11"] - 0.1 <= t < C["s12"]:
        def onze():
            g = G11
            fig(c, t, C["s11"], g, dict(h=("h", AMBAR)), th=C["s11"] + 0.3, tl=dict(h=c11), size=56)
            pedacos(c, t, a11, g, "4", "9", TINTA2, TINTA2, 56, 66)
            Xr = 1400
            fcen(c, t, C["s11"], "h^2 = m · n", Xr, 260, 90, COR)
            fcen(c, t, b11, "h^2 = 4 · 9 = 36", Xr, 440, 90)
            bola_txt(c, t, c11, "h = 6", Xr, 680, 120, 84)
        E.saida(c, t, C["s12"] - 0.1, onze)
    if t >= C["s12"] - 0.1:
        g = G7
        fig(c, t, C["s12"], g, dict(h=("2,4", AMBAR)), th=C["s12"] + 0.3, tl=dict(h=c12), size=56)
        pedacos(c, t, a12, g, "1,8", "3,2", TINTA2, TINTA2, 56, 66)
        Xr = 1400
        fcen(c, t, C["s12"], "h^2 = m · n", Xr, 260, 90, COR)
        fcen(c, t, b12, "1,8 · 3,2 = 5,76", Xr, 430, 90)
        fcen(c, t, c12, "2,4^2 = 5,76", Xr, 590, 90, CERTO)
        E.frase(c, t, c12 + 1.4, ps("as duas relações", "i", 60) + [("concordam", "g", 64, CERTO)], Xr, 760, "center", 0.12)
        E.foco(c, t, c12 + 2.2, 0.4, lambda a: E.selo(c, Xr, 900, 56 * ease_back(prog(t, c12 + 2.2, 0.4)), True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a13, b13, c13, d13, e13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
    g = G1
    B, Cc, Hh, A = g["B"], g["C"], g["H"], g["A"]
    X = 1440
    fig(c, t, C["s13"], g, dict(c=("3", TINTA), b=("4", TINTA)), th=None, altura=False, tl=dict(c=C["s13"] + 0.5, b=C["s13"] + 0.5))
    mx = (B[0] + Cc[0]) / 2

    def chute():
        if t >= a13:
            M.line(c, mx, B[1], mx, B[1] - 2.5 * 150, ERRADO, 1.0, 6, dash=E.TRACO, progress=ease_io(prog(t, a13, 0.6)))
        pedacos(c, t, b13, g | dict(H=(mx, B[1])), "2,5", "2,5", ERRADO, ERRADO, 54, 64)
    E.saida(c, t, d13, chute)
    if t >= d13:
        M.line(c, *A, *Hh, CERTO, 1.0, 7, progress=ease_io(prog(t, d13, 0.6)))
        E.angulo(c, t, d13 + 0.4, Hh, Cc, A, r=36, cor=CERTO)
        pedacos(c, t, d13 + 0.4, g, "1,8", "3,2", CERTO, CERTO, 54, 64)
    E.frase(c, t, C["s13"], ps("o erro do começo", "i", 70, ERRADO), X, 200, "center", 0.12)
    E.frase(c, t, a13, ps("a altura", "i", 60) + [("no meio?", "g", 66, ERRADO)], X, 320, "center", 0.12)
    fcen(c, t, c13, "2,5 · 2,5 = 6,25", X, 450, 76, ERRADO)
    E.foco(c, t, c13 + 1.4, 0.4, lambda a: E.formula(c, "→  h = 2,5", X, 550, 70, "g", ERRADO, a, "center"))
    E.frase(c, t, d13, ps("os pedaços:", "i", 60) + [("1,8 e 3,2", "g", 70, CERTO)], X, 690, "center", 0.12)
    # só cai no meio com catetos iguais
    S1, S2, ST = (1300, 1010), (1580, 1010), (1440, 870)
    E.frase(c, t, e13, ps("no meio só com", "i", 52) + [("catetos iguais", "g", 56)], X, 830, "center", 0.1)
    if t >= e13 + 0.5:
        E.triangulo(c, t, e13 + 0.5, S1, S2, ST, vertices=None, iguais=(0, 1, 1), retos=(2,), preenche=0.06, d=0.6, r_ang=24)
        M.line(c, *ST, 1440, 1010, AMBAR, 1.0, 5, progress=ease_io(prog(t, e13 + 1.1, 0.5)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    a15, b15, c15, d15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    X = W / 2

    def um():
        E.frase(c, t, C["s14"] + 0.2, [("atalho", "g", 90, CLARO)] + ps("prometido", "i", 80, BR), X, 160, "center", 0.12)
        fcen(c, t, a14, "3, 4, 5   →   h = 2,4", X, 330, 96, BR)
        E.frase(c, t, b14, ps("nos múltiplos,", "i", 60, CLARO) + [("multiplique a altura também", "g", 62, BR)], X, 460, "center", 0.1)
        fcen(c, t, c14, "6, 8, 10   →   h = 4,8", X, 620, 90, BR)
        E.foco(c, t, c14 + 0.6, 0.4, lambda a: E.formula(c, "(× 2)", X + 440, 620, 60, "g", AMBAR, a, "left"))
        fcen(c, t, d14, "30, 40, 50   →   h = 24", X, 780, 90, BR)
        E.foco(c, t, d14 + 0.6, 0.4, lambda a: E.formula(c, "(× 10)", X + 500, 780, 60, "g", AMBAR, a, "left"))
    E.saida(c, t, C["s15"] - 0.1, um)
    if t >= C["s15"] - 0.1:
        E.frase(c, t, a15, ps("ampliado =", "i", 70, CLARO) + [("semelhante", "g", 76, BR)], X, 250, "center", 0.12)
        E.frase(c, t, b15, ps("todas as medidas", "i", 62, CLARO) + [("× a mesma razão", "g", 66, BR)], X, 380, "center", 0.12)
        E.frase(c, t, b15 + 1.6, ps("inclusive a", "i", 62, CLARO) + [("altura", "g", 66, AMBAR)], X, 470, "center", 0.12)
        E.foco(c, t, c15, 0.5, lambda a: E.pilula(c, "fora dos ternos, não compensa", X, 640, 60, "g", fundo=ERRADO, a=a))
        fcen(c, t, d15, "a · h = b · c", X, 820, 110, BR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a16, b16 = C["s16.a"], C["s16.b"]
    E.frase(c, t, C["s16"], ps("hora de testar:", "i", 72, COR) + [("2 perguntas", "g", 76, COR)], XE, 140, passo=0.12)
    for g, t0, rot, ped, num in ((GQ1, a16, dict(c=("9", TINTA), b=("12", TINTA), h=("h = ?", AMBAR)), None, "1"),
                                 (GQ2, b16, dict(h=("h = ?", AMBAR)), ("2", "8"), "2")):
        E.foco(c, t, t0, 0.4, lambda a, g=g, num=num: (E.bola(c, g["B"][0] + 10, 300, 36, a=a), centro(c, num, g["B"][0] + 10, 318, 46, "g", BR, a)))
        fig(c, t, t0, g, rot, th=t0 + 0.4, tl={k: t0 + 0.9 for k in rot}, size=48)
        if ped:
            pedacos(c, t, t0 + 0.9, g, ped[0], ped[1], TINTA2, TINTA2, 48, 58)
    pergunta(c, t, [(a16, [("1.", "g", 60, COR)] + ps("catetos 9 e 12:", "i", 58) + [("h?", "g", 64, AMBAR)]),
                    (b16, [("2.", "g", 60, COR)] + ps("pedaços 2 e 8:", "i", 58) + [("h?", "g", 64, AMBAR)])], C["s17.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    a19, b19 = C["s19.a"], C["s19.b"]
    a20, b20 = C["s20.a"], C["s20.b"]
    X = 1400

    def um():
        g = GR1
        fig(c, t, C["s18"] - 0.8, g, dict(c=("9", TINTA), b=("12", TINTA), a=((lambda: "15" if t >= b18 else "")(), COR),
                                         h=((lambda: "7,2" if t >= d18 else "h")(), CERTO if t >= d18 else AMBAR)),
            th=C["s18"] - 0.8, tl=dict(c=C["s18"] - 0.8, b=C["s18"] - 0.8, a=b18, h=C["s18"] - 0.4), size=54)
        fcen(c, t, a18, "9, 12 = 3, 4 (× 3)", X, 220, 70, TINTA2)
        fcen(c, t, b18, "a = 5 × 3 = 15", X, 340, 76)
        fcen(c, t, c18, "15 · h = 9 · 12 = 108", X, 470, 76)
        fcen(c, t, d18, "h = f{108}{15} = f{36}{5} = 7,2", X, 630, 74, CERTO)

        def dez9():
            E.frase(c, t, a19, ps("pelo atalho:", "i", 58, COR), X - 160, 820, "center", 0.12)
            E.formula_em(c, t, a19 + 0.5, "2,4 × 3 = 7,2", X + 60, 820, 64, "g", COR, "left")
            E.frase(c, t, b19, ps("7,2 é menor que", "i", 56) + [("9 e 12", "g", 60)], X - 60, 940, "center", 0.1)
            E.foco(c, t, b19 + 1.0, 0.4, lambda a: E.selo(c, X + 330, 925, 46 * ease_back(prog(t, b19 + 1.0, 0.4)), True, a))
        dez9()
    E.saida(c, t, C["s20"] - 0.1, um)
    if t >= C["s20"] - 0.1:
        g = GR2
        fig(c, t, C["s20"], g, dict(h=((lambda: "4" if t >= b20 else "h")(), CERTO if t >= b20 else AMBAR)), th=C["s20"] + 0.2,
            tl=dict(h=C["s20"] + 0.6), size=60)
        pedacos(c, t, C["s20"] + 0.4, g, "2", "8", TINTA2, TINTA2, 56, 66)
        fcen(c, t, C["s20"] + 0.2, "h^2 = m · n", X, 280, 84, COR)
        fcen(c, t, a20, "h^2 = 2 · 8 = 16", X, 450, 90)
        bola_txt(c, t, b20, "h = 4", X, 680, 120, 84, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s21.a", "a · h = b · c", "hipotenusa × altura = cateto × cateto"), ("s21.b", "h^2 = m · n", "altura ao quadrado = produto dos pedaços"))
        for i, (k, form, sub) in enumerate(itens):
            y = 430 + i * 270
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", BR, a)))
            E.formula_em(c, t, C[k] + 0.1, form, 400, y, 100, "g", COR)
            E.frase(c, t, C[k] + 0.8, ps(sub, "i", 56, TINTA2), 400, y + 90, passo=0.08)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.2, ps("próxima aula", "i", 84), XE, 280)
    E.frase(c, t, C["s22.a"], [("Praticando", "g", 130, COR)], XE, 430)
    E.frase(c, t, C["s22.a"] + 1.0, ps("Pitágoras, atalhos e relações", "i", 66), XE, 560, passo=0.1)
    E.frase(c, t, C["s22.b"], ps("em", "i", 70) + [("situações reais", "g", 80)], XE, 690, passo=0.12)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 360, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1630, p), lerp(680, 385, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nomes=b_nomes, semelhanca=b_semelhanca, relacao1=b_relacao1,
              relacao2=b_relacao2, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
