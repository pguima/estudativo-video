"""Visual — Estudativo · MAT-ANA-002: ponto médio e baricentro (média das coordenadas).

Segue a linguagem da Geometria Analítica definida em MAT-ANA-001 (leia o cabeçalho de lá):
- plano à direita, texto à esquerda; eixo x e valores de x em índigo, y em preto; par() com x índigo e y preto;
- andar no plano com anda(): corredor em petróleo (DX), elevador em âmbar (DY); o segmento entre os pontos em índigo (DIST);
- pontos dados em tinta preta (nome()); o ponto ACHADO na aula (ponto médio M, baricentro G) é índigo, maior, com anel (achado());
- erro em vermelho, certo em verde, atalho no palco escuro, resposta na esfera.
Peças novas desta aula: seq() (conta que cresce peça a peça, cada uma no seu instante; aceita fração "f{2 + 6}{2}"),
achado() e medianas() (as três medianas tracejadas que se cruzam no baricentro).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Analítica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANA-002_ponto_medio_e_baricentro.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("media", "medio", "baricentro", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ENT, SAI = COR, TINTA                       # x / y, como em Funções
DX, DY, DIST = "#0E9AA7", "#D98A00", E.COR  # corredor, elevador, segmento
DX_ESC = "#3CC7D3"
assert (2 + 6) / 2 == 4 and (4 + 10) / 2 == 7 and 4 - 2 == 6 - 4 == 2 and 7 - 4 == 10 - 7 == 3
assert (-3 + 5) / 2 == 1 and (2 - 6) / 2 == -2
assert (1 + 5 + 3) / 3 == 3 and (2 + 4 + 9) / 3 == 5
assert (6 - 2) / 2 == 2 and (10 - 4) / 2 == 3 and 3 < 4
assert 2 * 4 - 2 == 6 and 2 * 7 - 4 == 10
assert (-2 + 4) / 2 == 1 and (5 + 1) / 2 == 3 and (-2 + 4 + 7) / 3 == 3 and (5 + 1 + 3) / 3 == 3

P1 = E.Plano(1120, 110, 630, 840, -1, 8, -1, 11)     # amigas em (2, 4) e (6, 10)
P2 = E.Plano(1080, 170, 700, 700, -4, 6, -7, 3)      # (−3, 2) e (5, −6)
P3 = E.Plano(1180, 150, 560, 770, -1, 7, -1, 10)     # triângulo (1, 2), (5, 4), (3, 9)
P4 = E.Plano(1140, 250, 660, 480, -3, 8, -1, 7)      # questão: (−2, 5), (4, 1), (7, 3)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da geometria analítica ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def plano(c, t, t0, P, marcas_x=None, marcas_y=None, size=38, grade=True):
    """E.plano na caixa de P, com o eixo x em índigo (como em Funções)"""
    E.plano(c, t, t0, *P.caixa, P.xmin, P.xmax, P.ymin, P.ymax, marcas_x=marcas_x, marcas_y=marcas_y, size=size,
            nomes=("", "y"), grade=grade)
    if t >= t0:
        x, y, w, h = P.caixa
        p = ep(t, t0, 0.6)
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 24, p)
        E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.escreve(c, "x", x + w + 26, P.oy + 62, 58, "i", ENT, a))


def par(c, xv, yv, x, y, size, a=1.0, align="left", cores=None, est="g"):
    """par ordenado (x, y): x em índigo, y em preto; cores=(cx, cy) troca as duas"""
    cx_, cy_ = cores or (ENT, SAI)
    neutro = TINTA if not cores else cx_
    partes = (("(", neutro), (xv, cx_), (", ", neutro), (yv, cy_), (")", neutro if not cores else cy_))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def par_em(c, t, t0, xv, yv, x, y, size, align="left", cores=None):
    E.foco(c, t, t0, 0.5, lambda a: par(c, xv, yv, x, y, size, a, align, cores))


def anda(c, t, t0, P, A, B, cor, d=0.8, largura=10, a=1.0):
    """seta que anda no plano de A até B (em valores) e fica"""
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        (x0, y0), (x1, y1) = P(*A), P(*B)
        M.line(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), cor, 0.22 * a, largura * 3.2)
        M.arrow(c, x0, y0, x1, y1, cor, a, largura, 30, p)


def cateto(c, t, t0, P, A, B, cor, d=0.7, largura=11, a=1.0):
    """lado do triângulo que cresce de A até B (em valores), na cor fixa"""
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P(*A), *P(*B), cor, a, largura, progress=p)


def lado_txt(c, t, t0, P, A, B, s, G, cor, size=56, gap=22, em=0.5):
    """medida ao lado do segmento AB (valores), do lado de fora do triângulo de centro G (valores); em = onde, de A (0) a B (1)"""
    (ax, ay), (bx, by), (gx, gy) = P(*A), P(*B), P(*G)
    ux, uy = E._uni(ax, ay, bx, by)
    nx, ny = uy, -ux
    mx, my = lerp(ax, bx, em), lerp(ay, by, em)
    if (mx + nx - gx) ** 2 + (my + ny - gy) ** 2 < (mx - gx) ** 2 + (my - gy) ** 2:
        nx, ny = -nx, -ny
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, s, mx, my, nx, ny, gap, size, "g", cor, a))


def nome(c, t, t0, P, x, y, s, lado=(1, -1), size=46, r=15, cor=TINTA):
    """ponto em tinta com o nome ao lado, também em tinta (o índigo fica para o x e para a distância)"""
    E.ponto(c, t, t0, P, x, y, None, cor=cor, r=r)
    if s:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E._cola(c, s, *P(x, y), lado[0], lado[1], r + 8, size, "b", TINTA, a))


def tiques(c, t, t0, P, xs=(), ys=()):
    """tracinhos sem número nos eixos (quando só alguns valores têm rótulo)"""
    for i, v in enumerate(xs):
        E.foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, v=v: M.line(c, P.x(v), P.oy - 10, P.x(v), P.oy + 10, TINTA, a, 4), sobe=6)
    for i, v in enumerate(ys):
        E.foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, v=v: M.line(c, P.ox - 10, P.y(v), P.ox + 10, P.y(v), TINTA, a, 4), sobe=6)


def canto(c, t, t0, P, V, A, B, cor=TINTA):
    """quadradinho do ângulo reto em V (valores), entre os lados VA e VB"""
    E.angulo(c, t, t0, P(*V), P(*A), P(*B), r=58, cor=cor, preenche=0.12)


def sombra_tri(c, t, t0, P, A, R, B, a=1.0):
    q = ep(t, t0, 0.6) * a
    if q > 0:
        path = skia.Path()
        path.addPoly([P(*A), P(*R), P(*B)], True)
        c.drawPath(path, M.paint(COR, 0.08 * q))


def conta(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """conta numa linha com partes coloridas: partes = [(texto em escrita de fórmula, cor)]. Devolve a largura"""
    ws = [E.formula(None, s, 0, 0, size, est, a=0) for s, _ in partes]
    w = sum(ws)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    if a > 0:
        for (s, cor), wi in zip(partes, ws):
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += wi
    return w


def conta_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: conta(c, partes, x, y, size, a, align))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")))


def anel(c, t, t0, X, Y, cor=None):
    p = prog(t, t0, 0.9)
    if 0 < p < 1:
        c.drawCircle(X, Y, 14 + 60 * ease_out(p), M.paint(cor or COR, 1 - p, stroke=6))


def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))



def seq(c, t, pecas, x, y, size, align="left"):
    """conta que cresce: pecas = [(texto em escrita de fórmula, cor, t0)], cada peça entra no seu instante, uma ao lado da outra"""
    ws = [E.formula(None, s, 0, 0, size, "g", a=0) for s, _, _ in pecas]
    xx = x - sum(ws) / 2 if align == "center" else x
    for (s, cor, ti), w in zip(pecas, ws):
        E.foco(c, t, ti, 0.5, lambda a, s=s, cor=cor, xx=xx: E.formula(c, s, xx, y, size, "g", cor, a))
        xx += w


def eixo_txt(c, t, t0, s, x, y, cor, size=70):
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, "g", cor, a))


def achado(c, t, t0, P, x, y, s=None, lado=(1, -1), cor=None, size=50):
    """o ponto que a aula acha (ponto médio, baricentro): índigo, maior, com anel"""
    cor = cor or DIST
    X, Y = P(x, y)
    if t >= t0:
        anel(c, t, t0, X, Y, cor)
        anel(c, t, t0 + 0.5, X, Y, cor)
    E.ponto(c, t, t0, P, x, y, None, cor=cor, r=19)
    if s:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E._cola(c, s, X, Y, lado[0], lado[1], 28, size, "g", cor, a))


def seg(c, t, t0, P, A, B, cor=None, d=0.8, largura=7, tracejado=False, a=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P(*A), *P(*B), cor or DIST, a, largura, dash=E.TRACO if tracejado else None, progress=p)


def medianas(c, t, t0, P, A, B, C_, d=0.7):
    """as três medianas, tracejadas: de cada vértice até o meio do lado oposto"""
    for i, (V, Q, R) in enumerate(((A, B, C_), (B, C_, A), (C_, A, B))):
        m = ((Q[0] + R[0]) / 2, (Q[1] + R[1]) / 2)
        p = ease_io(prog(t, t0 + 0.25 * i, d))
        if p > 0:
            M.line(c, *P(*V), *P(*m), TINTA2, 0.6, 4, dash=E.TRACO, progress=p)


def par_no_plano(c, t, t0, P, xv, yv, em, size=42, cores=None):
    E.foco(c, t, t0, 0.4, lambda a: par(c, xv, yv, *P(*em), size, a, "center", cores))


def letra_par(c, t, t0, L, xv, yv, x, y, size):
    E.foco(c, t, t0, 0.5, lambda a: (E.escreve(c, L, x, y, size, "g", TINTA, a),
                                     par(c, xv, yv, x + E.larg(L, "g", size) + size * 0.3, y, size, a)))


# ---------------- os pontos do começo ----------------
A1, B1, M1 = (2, 4), (6, 10), (4, 7)


def plano1(c, t, t0):
    plano(c, t, t0, P1, marcas_x=[2, 4, 6, 8], marcas_y=[2, 4, 6, 8, 10], size=36)
    tiques(c, t, t0, P1, (1, 3, 5, 7), (1, 3, 5, 7, 9))


def pontas1(c, t, ta, tb, nomes=False):
    nome(c, t, ta, P1, *A1, "amiga 1" if nomes else None, lado=(0, 1), size=40)
    nome(c, t, tb, P1, *B1, "amiga 2" if nomes else None, lado=(1, 0), size=40)
    if not nomes:
        par_no_plano(c, t, ta + 0.2, P1, "2", "4", (0.95, 4.45))
        par_no_plano(c, t, tb + 0.2, P1, "6", "10", (6.0, 10.65))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        plano1(c, t, C["s01"] + 0.2)
        pontas1(c, t, C["s01.a"] + 0.3, C["s01.b"] + 0.3, True)
        seg(c, t, C["s01.c"], P1, A1, B1, tracejado=t < C["s01.d"])
        if t < C["s01.d"]:
            E.foco(c, t, C["s01.c"] + 0.5, 0.4, lambda a: E.pilula(c, "?", *P1(2.9, 7.6), 50, "g", fundo=DIST, a=a))
        achado(c, t, C["s01.d"], P1, *M1)
        par_no_plano(c, t, C["s01.d"] + 0.3, P1, "4", "7", (2.3, 7.2), 44)
        E.frase(c, t, C["s01.a"], [("amiga", "i", 70), ("1", "g", 70)], XE, 270)
        par_em(c, t, C["s01.a"] + 0.3, "2", "4", XE + 270, 270, 70)
        E.frase(c, t, C["s01.b"], [("amiga", "i", 70), ("2", "g", 70)], XE, 390)
        par_em(c, t, C["s01.b"] + 0.3, "6", "10", XE + 270, 390, 70)
        E.frase(c, t, C["s01.c"], ps("exatamente no", "i", 80), XE, 560)
        E.frase(c, t, C["s01.c"] + 0.6, [("meio", "g", 96, DIST)], XE, 670)
        par_em(c, t, C["s01.d"], "4", "7", XE, 850, 110)
        E.frase(c, t, C["s01.d"] + 1.2, ps("de cabeça", "i", 66, TINTA2), XE + 360, 850)
    E.saida(c, t, C["s02"] - 0.1, cena1)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 1.0, [("ponto", "g", 130), ("médio", "g", 130, COR)], XE, 480)
        E.frase(c, t, C["s02.b"], [("e", "i", 110), ("baricentro", "g", 120, COR)], XE, 640)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("duas", "g", 80, COR, C["s03.a"]), ("coisas", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 200, "center")
    x, w = 230, 1460
    for k, y in (("s03.b", 290), ("s03.c", 590)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 250, p, prog_=p)
    # 1: marcar pontos
    k = C["s03.b"]
    pa, pb = ep(t, k + 0.6, 0.6), ep(t, k + 1.6, 0.6)
    if pa > 0:
        M.arrow(c, 330, 490, 520, 490, DX, pa, 10, 28, pa)
    if pb > 0:
        M.arrow(c, 520, 490, 520, 340, DY, pb, 10, 28, pb)
    if t >= k + 2.2:
        k2 = ease_back(prog(t, k + 2.2, 0.4))
        c.drawCircle(520, 340, 16 * k2, M.paint(TINTA))
    E.frase(c, t, k, [("marcar", "g", 70, COR), ("pontos", "g", 70, COR)], 620, 380)
    E.linha(c, t, [("1º", "g", 58, TINTA, k + 0.6), ("o", "i", 60, TINTA, k + 0.8), ("x,", "g", 60, ENT, k + 1.0),
                   ("2º", "g", 58, TINTA, k + 1.6), ("o", "i", 60, TINTA, k + 1.8), ("y", "g", 60, SAI, k + 2.0)], 620, 480)
    # 2: baricentro
    k = C["s03.c"]
    A_, B_, C2 = (320, 800), (610, 790), (460, 630)
    E.triangulo(c, t, k, A_, B_, C2, vertices=None, preenche=0.06, d=0.6)
    for i, (V, Q, R) in enumerate(((A_, B_, C2), (B_, C2, A_), (C2, A_, B_))):
        m = ((Q[0] + R[0]) / 2, (Q[1] + R[1]) / 2)
        p = ease_io(prog(t, k + 2.4 + 0.25 * i, 0.6))
        if p > 0:
            M.line(c, *V, *m, TINTA2, 0.85, 4, dash=E.TRACO, progress=p)
    G_ = ((A_[0] + B_[0] + C2[0]) / 3, (A_[1] + B_[1] + C2[1]) / 3)
    if t >= k + 3.6:
        c.drawCircle(*G_, 15 * ease_back(prog(t, k + 3.6, 0.4)), M.paint(DIST))
    E.frase(c, t, k, [("o", "i", 70), ("baricentro", "g", 70, COR)], 700, 680)
    E.frase(c, t, k + 1.4, ps("o ponto de equilíbrio do triângulo", "i", 54), 700, 760, passo=0.1)
    E.frase(c, t, k + 2.6, ps("onde as 3 medianas se encontram", "i", 54, TINTA2), 700, 830, passo=0.1)
    E.frase(c, t, C["s04"] - 2.6, ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 960, "center", passo=0.1)


# ---------------- o meio de dois números ----------------
def b_media(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("uma", "i", 80), ("coordenada", "g", 80, COR), ("só", "i", 80)], W / 2, 200, "center")
    RY = 470
    vx = E.reta(c, t, C["s04.a"] + 0.4, 360, 1560, RY, 0, 8, list(range(0, 9)), E._num, size=48)
    for v in (2, 6):
        E.foco(c, t, C["s04.b"], 0.3, lambda a, v=v: E.bola(c, vx(v), RY, 22, TINTA, a), blur=0)
    E.salto(c, t, C["s04.c"], vx(2), vx(4), RY, 110, DX, "2")
    E.salto(c, t, C["s04.c"] + 0.6, vx(6), vx(4), RY, 110, DX, "2")
    E.foco(c, t, C["s04.c"] + 1.0, 0.4, lambda a: E.bola(c, vx(4), RY, 30, DIST, a), blur=0)
    if t >= C["s04.c"] + 1.0:
        anel(c, t, C["s04.c"] + 1.0, vx(4), RY)
    E.saida(c, t, C["s05"] - 0.1, lambda: E.frase(c, t, C["s04.c"] + 1.2, [("2", "g", 72, DX), ("passos", "i", 76), ("de", "i", 76), ("cada", "i", 76),
                                                                          ("lado", "g", 72)], W / 2, 690, "center"))
    E.frase(c, t, C["s05.a"], [("some", "g", 70, COR), ("e", "i", 74), ("divida", "g", 70, COR), ("por", "i", 74), ("2", "g", 70, COR)],
            W / 2, 670, "center")
    s = 84
    pecas = [("f{2 + 6}{2}", TINTA, C["s05.b"]), (" = f{8}{2}", TINTA, C["s05.c"]), (" = ", TINTA, C["s05.c"] + 0.8), ("4", DIST, C["s05.c"] + 0.8)]
    seq(c, t, pecas, W / 2, 840, s, "center")
    E.frase(c, t, C["s05.d"], [("média:", "g", 64, COR), ("a", "i", 66), ("soma", "g", 64), ("dividida", "i", 66), ("pela", "i", 66),
                               ("quantidade", "g", 64)], W / 2, 990, "center", passo=0.12)


# ---------------- ponto médio ----------------
A2, B2, M2 = (-3, 2), (5, -6), (1, -2)


def b_medio(c, t, C, b):
    def p1():
        plano1(c, t, C["s06"])
        seg(c, t, C["s06"] + 0.3, P1, A1, B1)
        pontas1(c, t, C["s06"] + 0.6, C["s06"] + 0.8)
        # leitura dos eixos (s06)
        q = ep(t, C["s06.b"], 0.4) * (1 - ep(t, C["s07"], 0.5))
        if q > 0:
            for v in (2, 6):
                M.line(c, P1.x(v), P1.y(A1[1] if v == 2 else B1[1]), P1.x(v), P1.oy, ENT, 0.5 * q, 4, dash=E.TRACO)
                E.pilula(c, str(v), P1.x(v), P1.oy + 46, 36, "g", fundo=ENT, a=q)
        q = ep(t, C["s06.c"], 0.4) * (1 - ep(t, C["s07"], 0.5))
        if q > 0:
            for v, xv in ((4, 2), (10, 6)):
                M.line(c, P1.x(xv), P1.y(v), P1.ox, P1.y(v), SAI, 0.5 * q, 4, dash=E.TRACO)
                E.pilula(c, str(v), P1.ox - 44, P1.y(v), 36, "g", fundo=SAI, a=q)
        achado(c, t, C["s06.d"], P1, *M1, "M", lado=(-1, -1))
        par_no_plano(c, t, C["s06.d"] + 0.3, P1, "4", "7", (2.3, 6.6), 42)
        # passos iguais (s07)
        anda(c, t, C["s07.a"], P1, A1, (4, 4), DX, 0.6, 8)
        anda(c, t, C["s07.a"] + 0.7, P1, (4, 4), M1, DY, 0.6, 8)
        anda(c, t, C["s07.b"], P1, M1, (6, 7), DX, 0.6, 8)
        anda(c, t, C["s07.b"] + 0.7, P1, (6, 7), B1, DY, 0.6, 8)
        for t0, s, em, cor in ((C["s07.a"] + 0.4, "2", (3, 3.45), DX), (C["s07.a"] + 1.1, "3", (4.45, 5.5), DY),
                               (C["s07.b"] + 0.4, "2", (5, 6.45), DX), (C["s07.b"] + 1.1, "3", (6.45, 8.5), DY)):
            E.foco(c, t, t0, 0.4, lambda a, s=s, em=em, cor=cor: centro(c, s, *P1(*em), 50, "g", cor, a))
    E.saida(c, t, C["s08"] - 0.1, p1)

    def s06():
        E.frase(c, t, C["s06.a"], [("x", "g", 72, ENT), ("e", "i", 76), ("y", "g", 72, SAI), ("separados", "i", 76)], XE, 260)
        eixo_txt(c, t, C["s06.b"], "x:", XE, 440, ENT)
        seq(c, t, [("f{2 + 6}{2}", TINTA, C["s06.b"]), (" = f{8}{2}", TINTA, C["s06.b"] + 1.4), (" = ", TINTA, C["s06.b"] + 2.6),
                   ("4", ENT, C["s06.b"] + 2.6)], XE + 100, 440, 76)
        eixo_txt(c, t, C["s06.c"], "y:", XE, 630, SAI)
        seq(c, t, [("f{4 + 10}{2}", TINTA, C["s06.c"]), (" = f{14}{2}", TINTA, C["s06.c"] + 1.5), (" = ", TINTA, C["s06.c"] + 2.8),
                   ("7", SAI, C["s06.c"] + 2.8)], XE + 100, 630, 76)
        E.frase(c, t, C["s06.d"], [("ponto", "i", 72), ("médio", "g", 72, DIST)], XE, 800)
        par_em(c, t, C["s06.d"] + 0.4, "4", "7", XE, 920, 100)
    E.saida(c, t, C["s07"] - 0.1, s06)

    def s07():
        E.frase(c, t, C["s07"], [("por", "i", 80), ("que", "i", 80), ("funciona?", "g", 76, COR)], XE, 260)
        for k, y, extra in (("s07.a", 420, "até M"), ("s07.b", 540, "até o fim")):
            E.frase(c, t, C[k], [("anda", "i", 70), ("2,", "g", 70, DX), ("sobe", "i", 70), ("3", "g", 70, DY)] + ps(extra, "i", 56, TINTA2), XE, y)
        E.frase(c, t, C["s07.c"], [("passos", "i", 84), ("iguais", "g", 84, COR)], XE, 730)
        E.frase(c, t, C["s07.c"] + 1.0, [("bem", "i", 72), ("no", "i", 72), ("meio", "g", 72, DIST)], XE, 840)
    if C["s07"] <= t:
        E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    # com negativos
    plano(c, t, C["s08"], P2, marcas_x=[-4, -2, 2, 4, 6], marcas_y=[-6, -4, -2, 2], size=36)
    tiques(c, t, C["s08"], P2, (-3, -1, 1, 3, 5), (-7, -5, -3, -1, 1, 3))
    nome(c, t, C["s08.a"] + 0.3, P2, *A2, None)
    par_no_plano(c, t, C["s08.a"] + 0.5, P2, "−3", "2", (-2.6, 2.55))
    nome(c, t, C["s08.b"] + 0.3, P2, *B2, None)
    par_no_plano(c, t, C["s08.b"] + 0.5, P2, "5", "−6", (4.4, -6.6))
    seg(c, t, C["s08.b"] + 0.6, P2, A2, B2)
    achado(c, t, C["s08.e"], P2, *M2, "M", lado=(-1, 1))
    par_no_plano(c, t, C["s08.e"] + 0.3, P2, "1", "−2", (2.5, -1.45))
    E.frase(c, t, C["s08"], [("com", "i", 76), ("negativos", "g", 76, COR)], XE, 250)
    par_em(c, t, C["s08.a"], "−3", "2", XE, 370, 70)
    par_em(c, t, C["s08.b"], "5", "−6", XE + 330, 370, 70)
    eixo_txt(c, t, C["s08.c"], "x:", XE, 540, ENT)
    seq(c, t, [("f{−3 + 5}{2}", TINTA, C["s08.c"]), (" = f{2}{2}", TINTA, C["s08.c"] + 1.6), (" = ", TINTA, C["s08.c"] + 2.8),
               ("1", ENT, C["s08.c"] + 2.8)], XE + 100, 540, 76)
    eixo_txt(c, t, C["s08.d"], "y:", XE, 720, SAI)
    seq(c, t, [("f{2 − 6}{2}", TINTA, C["s08.d"]), (" = f{−4}{2}", TINTA, C["s08.d"] + 1.6), (" = ", TINTA, C["s08.d"] + 3.0),
               ("−2", SAI, C["s08.d"] + 3.0)], XE + 100, 720, 76)
    par_em(c, t, C["s08.e"], "1", "−2", XE, 910, 100)


# ---------------- baricentro ----------------
TA, TB, TC, TG = (1, 2), (5, 4), (3, 9), (3, 5)


def triangulo3(c, t, ta, tb, tc, tt, tm=None):
    plano(c, t, ta - 0.6, P3, marcas_x=[2, 4, 6], marcas_y=[2, 4, 6, 8, 10], size=36)
    tiques(c, t, ta - 0.6, P3, (-1, 1, 3, 5, 7), (-1, 1, 3, 5, 7, 9))
    E.triangulo(c, t, tt, P3(*TA), P3(*TB), P3(*TC), vertices=("A", "B", "C"), tv=(ta, tb, tc), preenche=0.07, d=0.8)
    for ti, V in ((ta, TA), (tb, TB), (tc, TC)):
        E.ponto(c, t, ti, P3, *V, None, cor=TINTA, r=14)
    if tm is not None:
        medianas(c, t, tm, P3, TA, TB, TC)


def b_baricentro(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09"], [("e", "i", 90), ("o", "i", 90), ("baricentro?", "g", 90, COR)], W / 2, 240, "center")
        E.frase(c, t, C["s09.a"], [("a", "i", 76), ("mesma", "i", 76), ("ideia,", "i", 76), ("com", "i", 76), ("3", "g", 80, COR),
                                   ("pontos", "g", 76)], W / 2, 390, "center")
        for k, y, L, cor in (("s09.b", 560, "x:", ENT), ("s09.c", 690, "y:", SAI)):
            E.frase(c, t, C[k], [(L, "g", 74, cor), ("some", "i", 74), ("os", "i", 74), ("três", "i", 74), ("e", "i", 74), ("divida", "i", 74),
                                 ("por", "i", 74), ("3", "g", 74, COR)], W / 2, y, "center", passo=0.12)
        E.frase(c, t, C["s09.d"], [("média", "g", 84, DIST), ("dos", "i", 84), ("vértices", "i", 84)], W / 2, 880, "center")
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    triangulo3(c, t, C["s10.a"], C["s10.b"], C["s10.c"], C["s10.c"] + 0.4, C["s10.c"] + 1.4)
    achado(c, t, C["s10.f"], P3, *TG)
    E.foco(c, t, C["s10.f"] + 0.3, 0.4, lambda a: (E.escreve(c, "G", P3.x(4.55), P3.y(6.1), 46, "g", DIST, a),
                                                  par(c, "3", "5", P3.x(4.55) + 46, P3.y(6.1), 42, a)))
    letra_par(c, t, C["s10.a"], "A", "1", "2", XE, 250, 62)
    letra_par(c, t, C["s10.b"], "B", "5", "4", XE + 420, 250, 62)
    letra_par(c, t, C["s10.c"], "C", "3", "9", XE, 350, 62)
    eixo_txt(c, t, C["s10.d"], "x:", XE, 530, ENT)
    seq(c, t, [("f{1 + 5 + 3}{3}", TINTA, C["s10.d"]), (" = f{9}{3}", TINTA, C["s10.d"] + 1.8), (" = ", TINTA, C["s10.d"] + 3.0),
               ("3", ENT, C["s10.d"] + 3.0)], XE + 100, 530, 76)
    eixo_txt(c, t, C["s10.e"], "y:", XE, 710, SAI)
    seq(c, t, [("f{2 + 4 + 9}{3}", TINTA, C["s10.e"]), (" = f{15}{3}", TINTA, C["s10.e"] + 2.0), (" = ", TINTA, C["s10.e"] + 3.2),
               ("5", SAI, C["s10.e"] + 3.2)], XE + 100, 710, 76)
    E.frase(c, t, C["s10.f"], [("baricentro", "g", 70, DIST)], XE, 890)
    par_em(c, t, C["s10.f"] + 0.4, "3", "5", XE + 470, 890, 84)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano1(c, t, C["s11"])
    q = ep(t, C["s12.a"], 0.5)
    if q > 0:  # o meio fica entre os pontos: a faixa de y entre 4 e 10
        x, y, w, h = P1.caixa
        c.drawRect(skia.Rect.MakeLTRB(x, P1.y(10), x + w, P1.y(4)), M.paint(CERTO, 0.12 * q))
    if t >= C["s12.b"]:
        M.line(c, P1.caixa[0], P1.y(4), P1.caixa[0] + P1.caixa[2], P1.y(4), CERTO, ep(t, C["s12.b"], 0.5), 5, dash=E.TRACO)
    seg(c, t, C["s11"] + 0.3, P1, A1, B1)
    pontas1(c, t, C["s11"] + 0.5, C["s11"] + 0.7)
    # o ponto errado
    if t >= C["s11.d"]:
        X, Y = P1(2, 3)
        k = ease_back(prog(t, C["s11.d"], 0.45))
        for s_ in (1, -1):
            M.line(c, X - 18 * k, Y - 18 * k * s_, X + 18 * k, Y + 18 * k * s_, ERRADO, 1.0, 9)
        E.foco(c, t, C["s11.d"] + 0.2, 0.4, lambda a: par(c, "2", "3", X + 120, Y + 16, 42, a, "center", (ERRADO, ERRADO)))
    # metade do caminho
    anda(c, t, C["s12.c"], P1, A1, (4, 4), DX, 0.6, 8)
    anda(c, t, C["s12.c"] + 0.6, P1, (4, 4), M1, DY, 0.6, 8)
    E.foco(c, t, C["s12.c"] + 0.4, 0.4, lambda a: centro(c, "2", *P1(3, 3.45), 50, "g", DX, a))
    E.foco(c, t, C["s12.c"] + 1.0, 0.4, lambda a: centro(c, "3", *P1(4.45, 5.5), 50, "g", DY, a))
    achado(c, t, C["s12.d"], P1, *M1, "M", lado=(-1, -1), cor=CERTO)

    def s11():
        E.frase(c, t, C["s11"], [("cuidado", "g", 90, ERRADO)], XE, 240)
        E.frase(c, t, C["s11.a"], [("subtrair", "g", 72, ERRADO), ("em", "i", 76), ("vez", "i", 76), ("de", "i", 76), ("somar", "g", 72)], XE, 370)
        eixo_txt(c, t, C["s11.b"], "x:", XE, 540, ENT)
        seq(c, t, [("f{6 − 2}{2}", ERRADO, C["s11.b"]), (" = f{4}{2} = 2", ERRADO, C["s11.b"] + 1.6)], XE + 100, 540, 76)
        eixo_txt(c, t, C["s11.c"], "y:", XE, 720, SAI)
        seq(c, t, [("f{10 − 4}{2}", ERRADO, C["s11.c"]), (" = f{6}{2} = 3", ERRADO, C["s11.c"] + 1.6)], XE + 100, 720, 76)
        E.frase(c, t, C["s11.d"], [("responde", "i", 70)], XE, 900)
        par_em(c, t, C["s11.d"] + 0.3, "2", "3", XE + 330, 900, 84, cores=(ERRADO, ERRADO))
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.a"], [("o", "i", 74), ("meio", "g", 72, CERTO), ("fica", "i", 74), ("entre", "g", 72), ("os", "i", 74), ("pontos", "i", 74)], XE, 260)
    E.frase(c, t, C["s12.b"], [("o", "i", 66), ("y", "g", 66, ERRADO), ("=", "i", 66), ("3", "g", 66, ERRADO), ("nem", "i", 66), ("chega", "i", 66),
                               ("no", "i", 66), ("4", "g", 66, CERTO)], XE, 400)
    E.frase(c, t, C["s12.c"], [("subtrair", "g", 64, ERRADO), ("dá", "i", 68), ("metade", "i", 68), ("do", "i", 68), ("caminho", "g", 64)], XE, 570)
    E.frase(c, t, C["s12.c"] + 1.4, ps("e não o lugar do meio", "i", 60, TINTA2), XE, 660)
    E.frase(c, t, C["s12.d"], [("para", "i", 76), ("o", "i", 76), ("meio,", "i", 76), ("some", "g", 80, CERTO)], XE, 830)
    seq(c, t, [("f{2 + 6}{2} = 4", CERTO, C["s12.d"] + 0.6)], XE, 960, 60)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    y, xa, xm, xb = 500, 380, 960, 1540

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 70, CLARO), W / 2, 150, "center")
        E.frase(c, t, C["s13.a"], [("achar", "i", 76, CLARO), ("a", "i", 76, CLARO), ("outra", "g", 76, BR), ("ponta", "g", 76, BR)], W / 2, 250, "center")
        E.frase(c, t, C["s13.b"], [("dobre", "g", 66, BR), ("o", "i", 70, CLARO), ("ponto", "i", 70, CLARO), ("médio", "i", 70, CLARO), ("e", "i", 70, CLARO),
                                   ("tire", "g", 66, BR), ("a", "i", 70, CLARO), ("ponta", "i", 70, CLARO)], W / 2, 350, "center", passo=0.14)
        if t >= C["s13.d"]:
            M.line(c, xa, y, xm, y, BR, 1.0, 6, progress=ease_io(prog(t, C["s13.d"], 0.6)))
        if t >= C["s13.g"]:
            M.line(c, xm, y, xb, y, DX_ESC, 1.0, 6, progress=ease_io(prog(t, C["s13.g"] - 0.3, 0.6)))
        E.foco(c, t, C["s13.c"], 0.4, lambda a: E.bola(c, xm, y, 28, COR, a), blur=0)
        if t >= C["s13.c"]:
            anel(c, t, C["s13.c"], xm, y, CLARO)
        E.foco(c, t, C["s13.c"] + 0.2, 0.4, lambda a: (centro(c, "médio", xm, y - 50, 44, "i", CLARO, a),
                                                      par(c, "4", "7", xm, y + 90, 64, a, "center", (CLARO, BR))))
        E.foco(c, t, C["s13.c"] + 1.0, 0.4, lambda a: E.pilula(c, "dobro: (8, 14)", xm, y + 170, 40, "g", fundo=COR, a=a))
        E.foco(c, t, C["s13.d"], 0.4, lambda a: (E.bola(c, xa, y, 20, BR, a), centro(c, "ponta", xa, y - 46, 44, "i", CLARO, a),
                                                 par(c, "2", "4", xa, y + 90, 64, a, "center", (CLARO, BR))), blur=0)
        if t < C["s13.g"]:
            E.foco(c, t, C["s13.b"] + 0.6, 0.4, lambda a: E.pilula(c, "?", xb, y, 48, "g", fundo=COR, a=a))
        else:
            E.foco(c, t, C["s13.g"], 0.4, lambda a: (E.bola(c, xb, y, 24, DX_ESC, a), centro(c, "outra ponta", xb, y - 50, 44, "i", CLARO, a),
                                                    par(c, "6", "10", xb, y + 90, 64, a, "center", (DX_ESC, DX_ESC))), blur=0)
        seq(c, t, [("x:  ", CLARO, C["s13.e"]), ("8 − 2 = ", BR, C["s13.e"]), ("6", DX_ESC, C["s13.e"] + 0.8)], W / 2, 850, 80, "center")
        seq(c, t, [("y:  ", CLARO, C["s13.f"]), ("14 − 4 = ", BR, C["s13.f"]), ("10", DX_ESC, C["s13.f"] + 0.8)], W / 2, 960, 80, "center")
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"], [("por", "i", 70, CLARO), ("que", "i", 70, CLARO), ("funciona", "g", 70, BR)], W / 2, 170, "center")
    seq(c, t, [("médio = f{soma das pontas}{2}", BR, C["s14.a"])], W / 2, 350, 76, "center")
    seq(c, t, [("2 × médio = ", BR, C["s14.b"]), ("soma das pontas", DX_ESC, C["s14.b"] + 0.6)], W / 2, 520, 76, "center")
    E.frase(c, t, C["s14.b"] + 1.8, ps("tirando uma ponta, sobra a outra", "i", 60, CLARO), W / 2, 620, "center", passo=0.12)
    E.frase(c, t, C["s14.c"], [("não", "g", 72, ERRADO), ("compensa", "i", 76, CLARO), ("com", "i", 76, CLARO), ("as", "i", 76, CLARO), ("duas", "g", 72, BR),
                               ("pontas:", "g", 72, BR)], W / 2, 820, "center")
    E.frase(c, t, C["s14.c"] + 1.4, ps("some e divida por 2", "i", 70, CLARO), W / 2, 930, "center")


# ---------------- questão ----------------
QA, QB, QC, QM, QG = (-2, 5), (4, 1), (7, 3), (1, 3), (3, 3)


def tri4(c, t, t0, ta, tb, tc, tt):
    plano(c, t, t0, P4, marcas_x=[-2, 2, 4, 6, 8], marcas_y=[2, 4, 6], size=34)
    tiques(c, t, t0, P4, (-3, -1, 1, 3, 5, 7), (-1, 1, 3, 5, 7))
    E.triangulo(c, t, tt, P4(*QA), P4(*QB), P4(*QC), vertices=("A", "B", "C"), tv=(ta, tb, tc), preenche=0.07, d=0.8, size=46)
    for ti, V in ((ta, QA), (tb, QB), (tc, QC)):
        E.ponto(c, t, ti, P4, *V, None, cor=TINTA, r=13)


def b_questao(c, t, C, b):
    tri4(c, t, C["s15"], C["s15.a"] + 0.3, C["s15.b"] + 0.3, C["s15.c"] + 0.3, C["s15.c"] + 0.6)
    seg(c, t, C["s15.d"], P4, QA, QB, largura=9)
    E.foco(c, t, C["s15.d"] + 0.6, 0.4, lambda a: E.pilula(c, "?", *P4(1.3, 1.9), 40, "g", fundo=DIST, a=a))
    E.foco(c, t, C["s15.e"] + 0.3, 0.4, lambda a: E.pilula(c, "G?", *P4(3, 3), 40, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    letra_par(c, t, C["s15.a"], "A", "−2", "5", XE, 320, 66)
    letra_par(c, t, C["s15.b"], "B", "4", "1", XE, 420, 66)
    letra_par(c, t, C["s15.c"], "C", "7", "3", XE, 520, 66)
    E.frase(c, t, C["s15.d"], [("ponto", "i", 66), ("médio", "g", 66, DIST), ("de", "i", 66), ("AB?", "g", 66)], XE, 680)
    E.frase(c, t, C["s15.e"], [("baricentro?", "g", 66, DIST)], XE, 790)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1000, cy=800, r=70)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    t0 = C["s17"] - 3
    tri4(c, t, t0, t0, t0, t0, t0)
    seg(c, t, t0, P4, QA, QB, largura=9)
    achado(c, t, C["s17.c"], P4, *QM, "M", lado=(-0.5, 1))
    if t >= C["s18"]:
        medianas(c, t, C["s18"] + 0.3, P4, QA, QB, QC)
    achado(c, t, C["s18.c"], P4, *QG, "G", lado=(0.5, 1))

    def s17():
        E.frase(c, t, C["s17"], [("ponto", "i", 72), ("médio", "g", 72, DIST), ("de", "i", 72), ("AB", "g", 72)], XE, 230)
        eixo_txt(c, t, C["s17.a"], "x:", XE, 420, ENT)
        seq(c, t, [("f{−2 + 4}{2}", TINTA, C["s17.a"]), (" = f{2}{2}", TINTA, C["s17.a"] + 1.8), (" = ", TINTA, C["s17.a"] + 3.0),
                   ("1", ENT, C["s17.a"] + 3.0)], XE + 100, 420, 76)
        eixo_txt(c, t, C["s17.b"], "y:", XE, 600, SAI)
        seq(c, t, [("f{5 + 1}{2}", TINTA, C["s17.b"]), (" = f{6}{2}", TINTA, C["s17.b"] + 1.4), (" = ", TINTA, C["s17.b"] + 2.6),
                   ("3", SAI, C["s17.b"] + 2.6)], XE + 100, 600, 76)
        E.frase(c, t, C["s17.c"], [("M", "g", 84, DIST)], XE, 800)
        par_em(c, t, C["s17.c"] + 0.2, "1", "3", XE + 110, 800, 84)
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("baricentro", "g", 72, DIST)], XE, 230)
    eixo_txt(c, t, C["s18.a"], "x:", XE, 410, ENT)
    seq(c, t, [("f{−2 + 4 + 7}{3}", TINTA, C["s18.a"]), (" = f{9}{3}", TINTA, C["s18.a"] + 2.2), (" = ", TINTA, C["s18.a"] + 3.4),
               ("3", ENT, C["s18.a"] + 3.4)], XE + 100, 410, 72)
    eixo_txt(c, t, C["s18.b"], "y:", XE, 580, SAI)
    seq(c, t, [("f{5 + 1 + 3}{3}", TINTA, C["s18.b"]), (" = f{9}{3}", TINTA, C["s18.b"] + 2.2), (" = ", TINTA, C["s18.b"] + 3.4),
               ("3", SAI, C["s18.b"] + 3.4)], XE + 100, 580, 72)
    E.frase(c, t, C["s18.c"], [("G", "g", 84, DIST)], XE, 760)
    par_em(c, t, C["s18.c"] + 0.2, "3", "3", XE + 110, 760, 84)
    E.foco(c, t, C["s18.d"], 0.4, lambda a: E.escreve(c, "÷ 2", XE, 920, 70, "g", ERRADO, a))
    if t >= C["s18.d"] + 0.4:
        E.risco(c, XE - 10, 935, XE + 130, 870, t, C["s18.d"] + 0.4, largura=9)
    E.frase(c, t, C["s18.d"] + 0.8, [("são", "i", 66), ("três", "g", 66, COR), ("vértices", "i", 66)], XE + 190, 920)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s19.a", [("ponto", "g", 80, DIST), ("médio", "g", 80, DIST), ("=", "i", 80), ("média", "i", 80), ("de", "i", 80), ("2", "g", 80),
                            ("pontos", "i", 80)]),
                 ("s19.b", [("baricentro", "g", 80, DIST), ("=", "i", 80), ("média", "i", 80), ("de", "i", 80), ("3", "g", 80)]),
                 ("s19.c", [("cada", "i", 80), ("coordenada", "g", 80), ("separada", "i", 80)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s20.a"], [("Coeficiente", "g", 130, COR)], XE, 450)
    E.frase(c, t, C["s20.a"] + 0.4, [("angular", "g", 130, COR)], XE, 590)
    E.frase(c, t, C["s20.b"], [("e", "i", 76), ("alinhamento", "g", 76)], XE, 720)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, media=b_media, medio=b_medio, baricentro=b_baricentro, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
