"""Visual — Estudativo · MAT-TOP-010: parábola, foco e diretriz. Abre o módulo "Noções de cônicas".

LINGUAGEM VISUAL DAS CÔNICAS (as próximas aulas do módulo copiam daqui):
- Plano na metade direita, texto na esquerda; eixo x em índigo (como na Geometria Analítica, MAT-ANA-001); escala igual nos eixos.
- A curva em tinta; o foco é uma bolinha na cor da matéria com o nome "F"; a diretriz é uma reta tracejada em âmbar.
- Distância até o foco em índigo; distância até a diretriz em âmbar; quando as duas batem, o ponto acende em verde.
- Atalho no palco escuro; erro em vermelho; resposta na esfera.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-010_parabola_foco_e_diretriz.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("definicao", "equacao", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMB = "#D98A00"
dist = lambda A, B: math.hypot(A[0] - B[0], A[1] - B[1])
assert 4 ** 2 == 8 * 2 and dist((4, 2), (0, 2)) == 4 == 2 - (-2)
assert 8 ** 2 == 8 * 8 and dist((8, 8), (0, 2)) == 10 == 8 - (-2)
assert dist((8, 8), (0, 8)) == 8 and 8 - (-8) == 16                    # o foco errado não bate
assert 4 ** 2 == 8 * 2 and 2 * 4 == 8                                   # largura no foco = 4p = 8
assert 12 / 4 == 3 and 6 ** 2 == 12 * 3 == 36 and dist((6, 3), (0, 3)) == 6 == 3 - (-3)
for p_ in (1, 2, 3):  # x² = 4py ⇔ distância ao foco = distância à diretriz
    for x in (-3, 0, 2, 5):
        y = x * x / (4 * p_)
        assert abs(dist((x, y), (0, p_)) - (y + p_)) < 1e-9

PP = E.Plano(900, 200, 900, 600, -9, 9, -3, 9)    # x² = 8y
PQ = E.Plano(1000, 230, 800, 600, -8, 8, -4, 8)   # x² = 12y


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, str(s), cx, cy + size * 0.36, size, "g", BR, a, "center")))


def txt_em(c, t, t0, s, x, y, size, cor=TINTA, est="g", align="left"):
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, s, x, y, size, est, cor, a, align))


# ---------------- peças das cônicas ----------------
def plano(c, t, t0, P, size=34, escuro=False, marcas_x=None, marcas_y=None):
    E.plano(c, t, t0, *P.caixa, P.xmin, P.xmax, P.ymin, P.ymax, size=size, nomes=("", "y"), escuro=escuro, marcas_x=marcas_x, marcas_y=marcas_y)
    if t >= t0:
        x, y, w, h = P.caixa
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, COR if not escuro else CLARO, 1.0, 6, 24, ep(t, t0, 0.6))
        E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.escreve(c, "x", x + w + 26, P.oy + 62, 58, "i", COR if not escuro else CLARO, a))


def parabola(c, t, t0, P, k, cor=TINTA, d=1.2, largura=7):
    """x² = k·y, isto é, y = x²/k"""
    E.curva(c, t, t0, P, lambda x: x * x / k, P.xmin, P.xmax, d=d, cor=cor, largura=largura)


def foco_pt(c, t, t0, P, x, y, cor=None, rot="F", escuro=False):
    cor = cor or (CLARO if escuro else COR)
    X, Y = P(x, y)
    s = ease_back(prog(t, t0, 0.45))
    if s > 0:
        c.drawCircle(X, Y, 16 * s, M.paint(cor))
        if rot:
            E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.escreve(c, rot, X + 22, Y - 16, 50, "g", cor, a))


def diretriz(c, t, t0, P, y, rot=True, escuro=False):
    p = ease_io(prog(t, t0, 0.8))
    if p <= 0:
        return
    x0, x1 = P.caixa[0], P.caixa[0] + P.caixa[2]
    Y = P.y(y)
    M.line(c, x0, Y, lerp(x0, x1, p), Y, AMB, 1, 6, dash=E.TRACO)
    if rot:
        E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.escreve(c, "diretriz", x1 - 170, Y + 48, 40, "i", AMB, a))


def ponto(c, t, t0, P, x, y, cor=TINTA, rot=None, lado=(1, -1)):
    E.ponto(c, t, t0, P, x, y, rot, cor=cor, lado=lado, size=40)


def seg(c, t, t0, P, A, B, cor, largura=7, d=0.6, tracejado=False):
    p = ease_io(prog(t, t0, d))
    if p > 0:
        M.line(c, *P(*A), *P(*B), cor, 1, largura, dash=E.TRACO if tracejado else None, progress=p)


def rotulo(c, t, t0, P, x, y, s, cor, size=44):
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, P.x(x), P.y(y), size, "g", cor, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        P = PP
        parabola(c, t, C["s01.a"], P, 8, TINTA, largura=9)
        if t >= C["s01.b"]:
            for i, x in enumerate((-6, -4, -2, 2, 4, 6)):
                y = x * x / 8
                p = ease_io(prog(t, C["s01.b"] + 0.08 * i, 0.6))
                q = ease_io(prog(t, C["s01.b"] + 0.6 + 0.08 * i, 0.6))
                X, Y0, Y = P.x(x), P.y(9), P.y(y)
                M.line(c, X, Y0, X, lerp(Y0, Y, p), AMB, 0.9, 4)
                if q > 0:
                    Fx, Fy = P(0, 2)
                    M.line(c, X, Y, lerp(X, Fx, q), lerp(Y, Fy, q), AMB, 0.9, 4)
            foco_pt(c, t, C["s01.b"] + 1.0, P, 0, 2)
        E.frase(c, t, C["s01.a"], [("antena", "i", 76), ("parabólica", "g", 70, COR)], XE, 300)
        E.foco(c, t, C["s01.b"] + 1.2, 0.4, lambda a: E.escreve(c, "tudo vai para o foco", XE, 420, 56, "i", AMB, a))
        txt_em(c, t, C["s01.c"], "x^2 = 8y", XE, 620, 110)
        E.foco(c, t, C["s01.d"], 0.4, lambda a: E.escreve(c, "foco (0, 2)", XE, 790, 90, "g", COR, a))
        E.foco(c, t, C["s01.e"], 0.4, lambda a: E.pilula(c, "de olho", 360, 920, 60, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 560, 270 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("foco", "g", 120, COR), ("e", "i", 110)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.4, [("diretriz", "g", 120, AMB)], XE, 630)
        E.frase(c, t, C["s02.a"] + 2.0, [("na", "i", 110), ("equação", "g", 120)], XE, 780)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1300, 545, 80, "g", BR, a),
                                                      E.escreve(c, "de prova", 1320, 630, 80, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 84), XE, 200)
    E.frase(c, t, C["s03.a"], [("2", "g", 110, COR), ("coisas", "i", 100)], XE + 640, 200)
    for i, k in enumerate(("s03.b", "s03.c")):
        y = 290 + i * 340
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, XE, y, 1580, 290, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("distância", "g", 66, COR), ("entre", "i", 66), ("dois", "i", 66), ("pontos", "i", 66)], XE + 50, 400)
    txt_em(c, t, C["s03.b"] + 0.8, "d^2 = (diferença dos x)^2 + (diferença dos y)^2", XE + 50, 520, 60)
    E.frase(c, t, C["s03.c"] + 0.1, [("vértice:", "g", 66, COR), ("onde", "i", 66), ("a", "i", 66), ("curva", "i", 66), ("volta", "i", 66)], XE + 50, 740)
    if t >= C["s03.c"]:
        x0, y0 = 1400, 860
        pts = [(x0 + u, y0 - 0.006 * u * u * 1.0 - 0) for u in range(-200, 201, 10)]
        q = ep(t, C["s03.c"] + 0.5, 0.6)
        for p0, p1 in zip(pts, pts[1:]):
            M.line(c, p0[0], p0[1] - 0 + 0, p1[0], p1[1], TINTA, q, 6)
        c.drawCircle(x0, y0, 14 * q, M.paint(COR))


# ---------------- definição ----------------
def b_definicao(c, t, C, b):
    P = PP
    plano(c, t, C["s04"], P, marcas_x=[-8, -4, 4, 8], marcas_y=[-2, 2, 4, 6, 8])
    foco_pt(c, t, C["s04.a"], P, 0, 2)
    diretriz(c, t, C["s04.b"], P, -2)
    parabola(c, t, C["s04.c"], P, 8)

    def textos1():
        E.frase(c, t, C["s04.a"], [("foco:", "i", 66), ("um", "i", 66), ("ponto", "g", 62, COR)], XE, 300)
        E.frase(c, t, C["s04.b"], [("diretriz:", "i", 66), ("uma", "i", 66), ("reta", "g", 62, AMB)], XE, 410)
        E.frase(c, t, C["s04.c"], ps("mesma distância", "g", 60, CERTO), XE, 560)
        E.frase(c, t, C["s04.c"] + 0.6, ps("do foco e da diretriz", "i", 60), XE, 650)
        E.frase(c, t, C["s04.d"], ps("até a reta: em ângulo reto", "i", 54, TINTA2), XE, 800)
        E.foco(c, t, C["s05.a"], 0.4, lambda a: E.escreve(c, "F = (0, 2)", XE, 930, 64, "g", COR, a))
    E.saida(c, t, C["s05.b"] - 0.1, textos1)
    if C["s05.b"] <= t < C["s06"]:
        E.saida(c, t, C["s06"] - 0.1, lambda: (
            E.foco(c, t, C["s05.b"], 0.4, lambda a: E.formula(c, "diretriz: y = −2", XE, 400, 76, "g", AMB, a)),
            E.frase(c, t, C["s05.c"], ps("a reta deitada em que", "i", 58), XE, 540),
            E.frase(c, t, C["s05.c"] + 0.8, ps("todo ponto tem y = −2", "g", 56, AMB), XE, 630)))
    # (4, 2)
    if C["s06"] <= t < C["s07"]:
        def p1():
            ponto(c, t, C["s06.a"], P, 4, 2, rot="(4, 2)", lado=(1, -1))
            seg(c, t, C["s06.b"], P, (4, 2), (0, 2), COR)
            rotulo(c, t, C["s06.b"] + 0.4, P, 1.6, 2.4, "4", COR)
            seg(c, t, C["s06.c"], P, (4, 2), (4, -2), AMB)
            rotulo(c, t, C["s06.c"] + 0.4, P, 4.3, 0.2, "4", AMB)
            E.foco(c, t, C["s06.b"], 0.4, lambda a: E.escreve(c, "até o foco: 4", XE, 400, 64, "g", COR, a))
            E.foco(c, t, C["s06.c"], 0.4, lambda a: E.escreve(c, "até a diretriz: 4", XE, 520, 64, "g", AMB, a))
            E.foco(c, t, C["s06.d"], 0.4, lambda a: E.pilula(c, "iguais: está na parábola", 480, 680, 54, "g", fundo=CERTO, a=a))
        E.saida(c, t, C["s07"] - 0.1, p1)
    if t >= C["s07"]:
        ponto(c, t, C["s07.a"], P, 8, 8, rot="(8, 8)", lado=(-1, -1))
        seg(c, t, C["s07.b"], P, (8, 8), (0, 2), COR)
        seg(c, t, C["s07.b"] + 0.6, P, (0, 2), (8, 2), COR, 3, tracejado=True)
        rotulo(c, t, C["s07.b"] + 0.6, P, 3.4, 6.2, "10", COR)
        seg(c, t, C["s07.c"], P, (8, 8), (8, -2), AMB)
        rotulo(c, t, C["s07.c"] + 0.4, P, 8.2, 3.6, "10", AMB)
        E.foco(c, t, C["s07.b"], 0.4, lambda a: E.formula(c, "até o foco: r{8^2 + 6^2} = 10", XE, 400, 58, "g", COR, a))
        E.foco(c, t, C["s07.c"], 0.4, lambda a: E.escreve(c, "até a diretriz: 10", XE, 520, 58, "g", AMB, a))
        E.foco(c, t, C["s07.d"], 0.4, lambda a: E.pilula(c, "iguais de novo", 400, 650, 54, "g", fundo=CERTO, a=a))
        ponto(c, t, C["s07.e"], P, 0, 0, cor=CERTO)
        E.foco(c, t, C["s07.e"], 0.4, lambda a: E.escreve(c, "vértice: 2 de cada lado", XE, 820, 58, "g", CERTO, a))


# ---------------- equação ----------------
def b_equacao(c, t, C, b):
    def parte1():
        E.frase(c, t, C["s08.a"], [("p", "g", 80, COR), ("=", "g", 80), ("vértice", "i", 76), ("→", "g", 76), ("foco", "i", 76)], XE, 200)
        E.foco(c, t, C["s08.b"], 0.4, lambda a: E.escreve(c, "F = (0, p)", XE, 340, 72, "g", COR, a))
        E.foco(c, t, C["s08.c"], 0.4, lambda a: E.escreve(c, "diretriz: y = −p", XE + 560, 340, 72, "g", AMB, a))
        txt_em(c, t, C["s08.c"] + 1.0, "r{x^2 + (y − p)^2} = y + p", XE, 520, 76)
        txt_em(c, t, C["s08.c"] + 2.2, "x^2 + y^2 − 2py + p^2 = y^2 + 2py + p^2", XE, 680, 64, TINTA2)
        E.foco(c, t, C["s08.d"], 0.5, lambda a: E.pilula(c, "x² = 4py", 700, 870, 100, "g", fundo=COR, a=a))
    E.saida(c, t, C["s09"] - 0.1, parte1)
    if C["s09"] <= t < C["s10"]:
        def parte2():
            E.foco(c, t, C["s09.a"], 0.5, lambda a: E.formula(c, "x^2 = 4p·y", XE, 260, 100, "g", TINTA, a))
            E.foco(c, t, C["s09.a"] + 0.6, 0.4, lambda a: E.escreve(c, "o número da frente do y é 4p", XE + 620, 260, 54, "i", COR, a))
            E.foco(c, t, C["s09.b"], 0.5, lambda a: E.formula(c, "x^2 = 8y:  4p = 8,  p = 2", XE, 450, 92, "g", TINTA, a))
            E.foco(c, t, C["s09.c"], 0.5, lambda a: E.escreve(c, "foco (0, 2)", XE, 650, 96, "g", COR, a))
            E.foco(c, t, C["s09.d"], 0.5, lambda a: E.escreve(c, "diretriz y = −2", XE, 820, 96, "g", AMB, a))
        E.saida(c, t, C["s10"] - 0.1, parte2)
    if t >= C["s10"]:
        P = E.Plano(1000, 180, 800, 700, -8, 8, -9, 5)
        plano(c, t, C["s10"], P, marcas_x=[-4, 4], marcas_y=[-8, -2, 2])
        E.curva(c, t, C["s10.b"], P, lambda x: -x * x / 8, P.xmin, P.xmax, d=1.0, cor=TINTA, largura=7)
        foco_pt(c, t, C["s10.c"], P, 0, -2)
        diretriz(c, t, C["s10.d"], P, 2)
        txt_em(c, t, C["s10.a"], "x^2 = −8y", XE, 300, 100)
        E.frase(c, t, C["s10.b"], [("abre", "i", 76), ("para", "i", 76), ("baixo", "g", 72, COR)], XE, 470)
        E.foco(c, t, C["s10.c"], 0.4, lambda a: E.escreve(c, "foco (0, −2)", XE, 640, 76, "g", COR, a))
        E.foco(c, t, C["s10.d"], 0.4, lambda a: E.escreve(c, "diretriz y = 2", XE, 790, 76, "g", AMB, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], XE, 190)
    P = E.Plano(1080, 150, 720, 800, -9, 9, -9, 11)
    plano(c, t, C["s11"], P, marcas_x=[-8, 8], marcas_y=[-8, 2, 8])
    parabola(c, t, C["s11"] + 0.3, P, 8)
    txt_em(c, t, C["s11.a"], "x^2 = 8y", XE, 330, 90)
    E.foco(c, t, C["s11.b"], 0.4, lambda a: E.escreve(c, "foco (0, 8)?", XE, 480, 90, "g", ERRADO, a))
    if t < C["s11.e"]:
        foco_pt(c, t, C["s11.b"], P, 0, 8, ERRADO, "F?")
        diretriz(c, t, C["s11.b"] + 0.3, P, -8, rot=False)
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.escreve(c, "8 = 4p", XE + 560, 480, 76, "g", COR, a))
    if t >= C["s11.d"] and t < C["s11.e"]:
        ponto(c, t, C["s11.d"], P, 8, 8)
        seg(c, t, C["s11.d"], P, (8, 8), (0, 8), ERRADO)
        seg(c, t, C["s11.d"] + 0.3, P, (8, 8), (8, -8), AMB)
    E.foco(c, t, C["s11.d"], 0.4, lambda a: E.escreve(c, "8 ≠ 16: não bate", XE, 640, 76, "g", ERRADO, a))
    if t >= C["s11.e"]:
        E.risco(c, XE - 10, 500, XE + 520, 420, t, C["s11.e"] - 0.3, largura=10)
        foco_pt(c, t, C["s11.e"], P, 0, 2, CERTO)
        diretriz(c, t, C["s11.e"] + 0.3, P, -2, rot=False)
    E.foco(c, t, C["s11.e"], 0.4, lambda a: E.escreve(c, "8 ÷ 4 = 2: foco (0, 2)", XE, 820, 80, "g", CERTO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    P = E.Plano(1000, 200, 800, 650, -8, 8, -3, 10)
    plano(c, t, C["s12"], P, escuro=True, marcas_x=[-4, 4], marcas_y=[2])
    E.curva(c, t, C["s12"] + 0.3, P, lambda x: x * x / 8, P.xmin, P.xmax, d=1.0, cor=BR, largura=7)
    foco_pt(c, t, C["s12"] + 0.6, P, 0, 2, escuro=True)
    E.frase(c, t, C["s12.a"], [("na", "i", 70, CLARO), ("altura", "i", 70, CLARO), ("do", "i", 70, CLARO), ("foco:", "i", 70, CLARO)], XE, 300)
    E.frase(c, t, C["s12.a"] + 0.8, [("largura", "g", 76, BR), ("4p", "g", 76, CLARO)], XE, 410)
    if t >= C["s12.b"]:
        p = ease_io(prog(t, C["s12.b"], 0.8))
        (x0, y0), (x1, _) = P(-4, 2), P(4, 2)
        cx = (x0 + x1) / 2
        M.line(c, cx, y0, lerp(cx, x0, p), y0, AMB, 1, 8)
        M.line(c, cx, y0, lerp(cx, x1, p), y0, AMB, 1, 8)
        for X in (x0, x1):
            c.drawCircle(X, y0, 14 * p, M.paint(AMB))
        E.foco(c, t, C["s12.b"] + 0.8, 0.4, lambda a: (E.escreve(c, "−4", x0 - 70, y0 - 24, 46, "g", BR, a), E.escreve(c, "4", x1 + 20, y0 - 24, 46, "g", BR, a)))
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.escreve(c, "x² = 8y: largura 8", XE, 560, 64, "g", BR, a))
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.escreve(c, "vértice + 2 pontos", XE, 680, 64, "g", CLARO, a))
    E.foco(c, t, C["s13.a"], 0.4, lambda a: E.escreve(c, "até a diretriz: 2p", XE, 820, 56, "i", CLARO, a))
    E.foco(c, t, C["s13.b"], 0.4, lambda a: E.escreve(c, "cada lado: 2p", XE + 480, 820, 56, "g", BR, a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.pilula(c, "vértice fora da origem? ache o vértice primeiro", 900, 960, 50, "g", fundo=COR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    txt_em(c, t, C["s14.a"], "x^2 = 12y", XE, 430, 140)
    E.frase(c, t, C["s14.b"], [("foco", "g", 80, COR), ("e", "i", 84), ("diretriz?", "g", 80, AMB)], XE, 640)
    E.frase(c, t, C["s14.c"], [("confira", "i", 76), ("com", "i", 76), ("(6, 3)", "g", 76)], XE, 820)
    E.relogio(c, t, C["s15.a"], 1500, 460, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    P = PQ
    plano(c, t, C["s16"], P, marcas_x=[-6, 6], marcas_y=[-3, 3, 6])
    parabola(c, t, C["s16"] + 0.3, P, 12)
    E.foco(c, t, C["s16.a"], 0.4, lambda a: E.escreve(c, "4p = 12, p = 3", XE, 280, 76, "g", TINTA, a))
    foco_pt(c, t, C["s16.b"], P, 0, 3)
    E.foco(c, t, C["s16.b"], 0.4, lambda a: E.escreve(c, "foco (0, 3)", XE, 400, 76, "g", COR, a))
    diretriz(c, t, C["s16.c"], P, -3)
    E.foco(c, t, C["s16.c"], 0.4, lambda a: E.escreve(c, "diretriz y = −3", XE, 520, 76, "g", AMB, a))
    ponto(c, t, C["s17.a"], P, 6, 3, rot="(6, 3)", lado=(1, -1))
    E.foco(c, t, C["s17.a"], 0.4, lambda a: E.escreve(c, "6² = 36 = 12 · 3", XE, 670, 64, "g", TINTA, a))
    seg(c, t, C["s17.b"], P, (6, 3), (0, 3), COR)
    E.foco(c, t, C["s17.b"], 0.4, lambda a: E.escreve(c, "até o foco: 6", XE, 790, 64, "g", COR, a))
    seg(c, t, C["s17.c"], P, (6, 3), (6, -3), AMB)
    E.foco(c, t, C["s17.c"], 0.4, lambda a: E.escreve(c, "até a diretriz: 6", XE, 900, 64, "g", AMB, a))
    E.foco(c, t, C["s17.d"], 0.5, lambda a: E.pilula(c, "bateu", 820, 850, 70, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        for i, (k, s) in enumerate((("s18.a", "mesma distância do foco e da diretriz"), ("s18.b", "x² = 4py: foco a p do vértice"))):
            y = 450 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a), centro(c, str(i + 1), 260, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 78)], 360, y)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s19.a"], [("dois", "i", 120), ("focos", "g", 130, COR)], XE, 470)
    E.frase(c, t, C["s19.b"], [("a", "i", 120), ("elipse", "g", 130, COR)], XE, 640)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, definicao=b_definicao, equacao=b_equacao, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
