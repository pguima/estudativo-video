"""Visual — Estudativo · MAT-ANA-007: praticando pontos e retas (distância, equação da reta, paralelas, perpendicular e encontro).

Segue a linguagem da Geometria Analítica definida em MAT-ANA-001 (leia o cabeçalho de lá):
- plano à direita, texto à esquerda; eixo x e valores de x em índigo, y em preto; par() com x índigo e y preto;
- triângulo entre dois pontos: corredor Δx em petróleo (DX), elevador Δy em âmbar (DY), a distância/a reta em índigo (DIST);
- pontos dados em tinta preta (nome()); o ponto ACHADO (o encontro das retas) em índigo, maior, com anel (achado());
- duas retas no mesmo plano: a primeira (a dada) em índigo, a segunda (a nova) em tinta preta; o m em índigo e o n em preto
  (pílula no eixo y, como em MAT-ANA-004); na situação 3, cada corte no eixo y leva a cor da sua reta;
- erro em vermelho, certo em verde, atalho no palco escuro, resposta na esfera; relógio de pausa em cada situação.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Analítica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANA-007_praticando_pontos_e_retas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "fim"))
BR = "#FFFFFF"
ENT, SAI = COR, TINTA                       # x / y, como em Funções
DX, DY, DIST = "#0E9AA7", "#D98A00", E.COR  # Δx (corredor), Δy (elevador), distância / reta
DX_ESC, DY_ESC = "#3CC7D3", "#FFB833"
# as contas do roteiro
assert 6 - (-2) == 8 and 3 - (-3) == 6 and 8 ** 2 == 64 and 6 ** 2 == 36 and 64 + 36 == 100 and math.isqrt(100) == 10 and 8 + 6 == 14
assert 7 - 1 == 6 and 3 - 1 == 2 and 6 / 2 == 3 and 1 == 3 * 1 - 2 and 3 * 3 - 2 == 7
assert all(6 * x - 2 * (3 * x + 2.5) + 5 == 0 for x in (0, 1, 2)) and -6 / -2 == 3
assert 2 * (-0.5) == -1 and -0.5 * -6 == 3 and all(abs((-0.5 * (x - 6) + 2) - (-0.5 * x + 5)) < 1e-9 for x in (0, 4))
assert 2 * 2 == -0.5 * 2 + 5 == 4 and 4 * 2 == -2 + 10

P1 = E.Plano(1070, 250, 700, 560, -3, 7, -4, 4)    # posto (−2, 3), oficina (6, −3)
P2 = E.Plano(1250, 140, 504, 792, -1, 6, -3, 8)    # (1, 1), (3, 7); y = 3x − 2 e y = 3x + 2,5
P4 = E.Plano(1090, 180, 720, 720, -1, 7, -1, 7)    # y = 2x, (6, 2), encontro (2, 4)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da geometria analítica (as mesmas de MAT-ANA-001 a 003) ----------------
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


def par(c, xv, yv, x, y, size, a=1.0, align="left", est="g"):
    """par ordenado (x, y): x em índigo, y em preto"""
    partes = (("(", TINTA), (xv, ENT), (", ", TINTA), (yv, SAI), (")", TINTA))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def par_em(c, t, t0, xv, yv, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: par(c, xv, yv, x, y, size, a, align))


def anda(c, t, t0, P, A, B, cor, d=0.8, largura=10, a=1.0):
    """seta que anda no plano de A até B (em valores) e fica"""
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        (x0, y0), (x1, y1) = P(*A), P(*B)
        M.line(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), cor, 0.22 * a, largura * 3.2)
        M.arrow(c, x0, y0, x1, y1, cor, a, largura, 30, p)


def cateto(c, t, t0, P, A, B, cor, d=0.7, largura=11, a=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P(*A), *P(*B), cor, a, largura, progress=p)


def lado_txt(c, t, t0, P, A, B, s, G, cor, size=56, gap=22, em=0.5):
    """medida ao lado do segmento AB (valores), do lado de fora do triângulo de centro G (valores)"""
    (ax, ay), (bx, by), (gx, gy) = P(*A), P(*B), P(*G)
    ux, uy = E._uni(ax, ay, bx, by)
    nx, ny = uy, -ux
    mx, my = lerp(ax, bx, em), lerp(ay, by, em)
    if (mx + nx - gx) ** 2 + (my + ny - gy) ** 2 < (mx - gx) ** 2 + (my - gy) ** 2:
        nx, ny = -nx, -ny
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, s, mx, my, nx, ny, gap, size, "g", cor, a))


def nome(c, t, t0, P, x, y, s, lado=(1, -1), size=46, r=15, cor=TINTA):
    E.ponto(c, t, t0, P, x, y, None, cor=cor, r=r)
    if s:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E._cola(c, s, *P(x, y), lado[0], lado[1], r + 8, size, "b", TINTA, a))


def tiques(c, t, t0, P, xs=(), ys=()):
    for i, v in enumerate(xs):
        E.foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, v=v: M.line(c, P.x(v), P.oy - 10, P.x(v), P.oy + 10, TINTA, a, 4), sobe=6)
    for i, v in enumerate(ys):
        E.foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, v=v: M.line(c, P.ox - 10, P.y(v), P.ox + 10, P.y(v), TINTA, a, 4), sobe=6)


def canto(c, t, t0, P, V, A, B, cor=TINTA):
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
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")))


def anel(c, t, t0, X, Y, cor=None):
    p = prog(t, t0, 0.9)
    if 0 < p < 1:
        c.drawCircle(X, Y, 14 + 60 * ease_out(p), M.paint(cor or COR, 1 - p, stroke=6))


def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))


def seg(c, t, t0, P, A, B, cor=None, d=0.8, largura=7, tracejado=False, a=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P(*A), *P(*B), cor or DIST, a, largura, dash=E.TRACO if tracejado else None, progress=p)


def _w(s, size, est="g"):
    return E.formula(None, s, 0, 0, size, est, a=0)


def fra(c, cima, baixo, x, y, size, a=1.0, cc=TINTA, cb=TINTA, barra=TINTA):
    """fração empilhada com cima e baixo em cores próprias; y = linha de base da conta. Devolve a largura"""
    s_ = size * 0.78
    wc, wb = _w(cima, s_), _w(baixo, s_)
    w = max(wc, wb) + size * 0.16
    if a > 0 and c is not None:
        E.formula(c, cima, x + (w - wc) / 2, y - size * 0.46, s_, "g", cc, a)
        E.formula(c, baixo, x + (w - wb) / 2, y + size * 0.46, s_, "g", cb, a)
        b = max(4, size * 0.07)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - size * 0.3 - b / 2, w, b), b / 2, b / 2), M.paint(barra, a))
    return w


def mfr(c, t, t0, cima, baixo, x, y, size, pre="m = ", pos="", cc=DY, cb=DX, cp=None, tpos=None, tinta=TINTA, cpre=None):
    """m = Δy/Δx com o de cima em âmbar e o de baixo em petróleo; pos (o resultado) entra em tpos"""
    wp = _w(pre, size) if pre else 0
    wf = fra(None, cima, baixo, 0, 0, size)
    gap = size * 0.12
    E.foco(c, t, t0, 0.5, lambda a: (pre and E.formula(c, pre, x, y, size, "g", cpre or tinta, a), fra(c, cima, baixo, x + wp, y, size, a, cc, cb, tinta)))
    if pos:
        E.foco(c, t, tpos if tpos is not None else t0 + 0.8, 0.5, lambda a: E.formula(c, pos, x + wp + wf + gap, y, size, "g", cp or tinta, a))
    return wp + wf + gap + (_w(pos, size) if pos else 0)


def degrau(c, t, P, A, B, tx, ty, lx=None, ly=None, tlx=None, tly=None, larg=10, a=1.0, sombra=None, canto_t=None, setas=False, size=52):
    """o triângulo da subida de A até B: Δx deitado (petróleo), Δy em pé (âmbar)"""
    R = (B[0], A[1])
    if sombra is not None:
        sombra_tri(c, t, sombra, P, A, R, B, a)
    if setas:
        anda(c, t, tx, P, A, R, DX, 0.6, larg * 0.8, a)
        anda(c, t, ty, P, R, B, DY, 0.6, larg * 0.8, a)
    else:
        cateto(c, t, tx, P, A, R, DX, 0.6, larg, a)
        cateto(c, t, ty, P, R, B, DY, 0.6, larg, a)
    if canto_t is not None and t >= canto_t:
        canto(c, t, canto_t, P, R, A, B)
    G = ((A[0] + R[0] + B[0]) / 3, (A[1] + R[1] + B[1]) / 3)
    if lx:
        lado_txt(c, t, tlx if tlx is not None else tx + 0.4, P, A, R, lx, G, DX, size)
    if ly:
        lado_txt(c, t, tly if tly is not None else ty + 0.4, P, R, B, ly, G, DY, size)


def achado(c, t, t0, P, x, y, s=None, lado=(1, -1), cor=None, size=50):
    """o ponto que a aula acha: índigo, maior, com anel"""
    cor = cor or DIST
    X, Y = P(x, y)
    if t >= t0:
        anel(c, t, t0, X, Y, cor)
        anel(c, t, t0 + 0.5, X, Y, cor)
    E.ponto(c, t, t0, P, x, y, None, cor=cor, r=19)
    if s:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E._cola(c, s, X, Y, lado[0], lado[1], 28, size, "g", cor, a))


def reta(c, t, t0, P, A, B, cor=None, largura=7, d=0.8):
    if t >= t0:
        E.reta_pontos(c, t, t0, P, A, B, cor=cor or DIST, pontos=False, largura=largura, d=d)


def titulo(c, t, t0, n, y=200):
    E.frase(c, t, t0, [("situação", "i", 74), (str(n), "g", 74, COR)], XE, y)


def pausa(c, t, t0, cx=560, cy=840, r=80):
    if t >= t0:
        E.relogio(c, t, t0, cx=cx, cy=cy, r=r)


def ok(c, t, t0, x, y, r=34):
    E.foco(c, t, t0, 0.4, lambda a: E.selo(c, x, y, r * ease_back(prog(t, t0, 0.5)), True, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("4", "g", 220, COR)], XE, 420)
    E.frase(c, t, C["s01.a"] + 0.3, [("situações", "i", 110)], XE + 170, 400)
    E.frase(c, t, C["s01.a"] + 0.9, [("pontos", "g", 92), ("e", "i", 92), ("retas", "g", 92, COR)], XE, 560)
    E.frase(c, t, C["s01.a"] + 1.8, ps("criadas para esta aula", "i", 58, TINTA2), XE, 650, passo=0.12)
    # as quatro situações, numeradas
    for i in range(4):
        cx, cy = 1260 + (i % 2) * 300, 300 + (i // 2) * 300
        t0 = C["s01.a"] + 0.4 + i * 0.25
        E.foco(c, t, t0, 0.5, lambda a, cx=cx, cy=cy, i=i, t0=t0: (
            E.bola(c, cx, cy, 110 * ease_back(prog(t, t0, 0.5)), a=a),
            centro(c, str(i + 1), cx, cy + 44, 120, "g", BR, a)), blur=0)
    E.frase(c, t, C["s01.b"], [("pause", "g", 80, COR), ("e", "i", 80), ("resolva", "g", 80)], XE, 820)
    E.frase(c, t, C["s01.b"] + 3.4, ps("errar aqui ensina", "i", 62, TINTA2), XE, 930, passo=0.12)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 80, TINTA, C["s02"]), ("vai", "i", 80, TINTA, C["s02"] + 0.2), ("usar", "i", 80, TINTA, C["s02"] + 0.4),
                   ("4", "g", 80, COR, C["s02.a"]), ("ferramentas", "i", 80, TINTA, C["s02.a"] + 0.2)], W / 2, 170, "center")
    x, w, h = 230, 1460, 160
    for i, k in enumerate(("s02.b", "s02.c", "s02.d", "s02.e")):
        y = 230 + i * 180
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, x + 80, y + h / 2, 46, a=a),
                                                     centro(c, str(i + 1), x + 80, y + h / 2 + 20, 54, "g", BR, a)))
    yb = lambda i: 230 + i * 180 + 104
    # 1: distância
    k = C["s02.b"]
    E.frase(c, t, k + 0.1, [("distância", "g", 64, DIST), ("=", "i", 64), ("hipotenusa", "i", 64)], x + 170, yb(0))
    A_, R_, B_ = (1300, 380), (1560, 380), (1560, 250)
    cat = ep(t, k + 0.8, 0.5)
    if cat > 0:
        M.line(c, *A_, *R_, DX, cat, 10)
        M.line(c, *R_, *B_, DY, cat, 10)
    hip = ep(t, k + 1.4, 0.5)
    if hip > 0:
        M.line(c, *A_, *B_, DIST, 1.0, 10, progress=hip)
    # 2: o m
    mfr(c, t, C["s02.c"] + 0.1, "Δy", "Δx", x + 170, yb(1), 66)
    # 3: reduzida e geral
    E.foco(c, t, C["s02.d"] + 0.1, 0.5, lambda a: E.formula(c, "y = mx + n", x + 170, yb(2), 66, "g", COR, a))
    E.foco(c, t, C["s02.d"] + 0.9, 0.5, lambda a: E.formula(c, "ax + by + c = 0", x + 720, yb(2), 66, "g", TINTA, a))
    # 4: paralelas e perpendiculares
    E.foco(c, t, C["s02.e"] + 0.1, 0.5, lambda a: E.formula(c, "paralelas: m = m", x + 170, yb(3), 56, "g", TINTA, a))
    E.foco(c, t, C["s02.e"] + 0.9, 0.5, lambda a: E.formula(c, "perpendiculares: m · m' = −1", x + 640, yb(3), 56, "g", TINTA, a))
    E.frase(c, t, C["s03"] - 2.6, ps("travou? procure a aula no canal", "i", 48, TINTA2), W / 2, 1000, "center", passo=0.1)


# ---------------- situação 1: distância ----------------
POS, OFI, R1 = (-2, 3), (6, -3), (6, 3)
G1 = ((POS[0] + OFI[0] + R1[0]) / 3, (POS[1] + OFI[1] + R1[1]) / 3)


def mapa1(c, t, t0, ta, tb):
    plano(c, t, t0, P1, marcas_x=[-2, 2, 4, 6], marcas_y=[-3, -2, 2, 3], size=34)
    tiques(c, t, t0, P1, (-3, -1, 1, 3, 5, 7), (-4, -1, 1, 4))
    nome(c, t, ta, P1, *POS, "posto", lado=(-1, -1), size=42)
    nome(c, t, tb, P1, *OFI, "oficina", lado=(-1, 1), size=42)


def b_questao1(c, t, C, b):
    mapa1(c, t, C["s03"] + 0.2, C["s03.b"] + 0.3, C["s03.c"] + 0.3)
    seg(c, t, C["s03.d"], P1, POS, OFI, DIST, 0.8, 6, tracejado=True)
    E.foco(c, t, C["s03.d"] + 0.6, 0.4, lambda a: E.pilula(c, "?", *P1(2.6, 0.9), 48, "g", fundo=DIST, a=a))
    titulo(c, t, C["s03.a"], 1)
    E.frase(c, t, C["s03.a"] + 1.0, ps("mapa em km", "i", 50, TINTA2), XE, 280)
    E.frase(c, t, C["s03.b"], [("posto", "g", 66)], XE, 400)
    par_em(c, t, C["s03.b"] + 0.4, "−2", "3", XE + 260, 400, 66)
    E.frase(c, t, C["s03.c"], [("oficina", "g", 66)], XE, 510)
    par_em(c, t, C["s03.c"] + 0.4, "6", "−3", XE + 300, 510, 66)
    E.frase(c, t, C["s03.d"], [("distância", "i", 66), ("em", "i", 66), ("linha", "g", 66, DIST), ("reta?", "g", 66, DIST)], XE, 650)
    pausa(c, t, C["s04.a"])


def b_resposta1(c, t, C, b):
    t0 = C["s05"] - 3
    mapa1(c, t, t0, t0, t0)
    sombra_tri(c, t, C["s05.b"] + 0.8, P1, POS, R1, OFI)
    anda(c, t, C["s05.a"] + 0.3, P1, POS, R1, DX, 0.8, 9)
    anda(c, t, C["s05.b"] + 0.3, P1, R1, OFI, DY, 0.7, 9)
    if t >= C["s05.b"] + 1.1:
        canto(c, t, C["s05.b"] + 1.1, P1, R1, POS, OFI)
    lado_txt(c, t, C["s05.a"] + 2.6, P1, POS, R1, "8", G1, DX, 54)
    lado_txt(c, t, C["s05.b"] + 2.0, P1, R1, OFI, "6", G1, DY, 54, em=0.25)
    cateto(c, t, C["s05.e"], P1, POS, OFI, DIST, 0.7, 10)
    lado_txt(c, t, C["s05.e"] + 1.6, P1, POS, OFI, "10", G1, DIST, 58, em=0.72)
    # o caminho pelas ruas pisca
    q = pulso(t, C["s06.b"], 2.4)
    if q > 0:
        M.line(c, *P1(*POS), *P1(*R1), DX, 0.3 * q, 34)
        M.line(c, *P1(*R1), *P1(*OFI), DY, 0.3 * q, 34)

    def s05ab():
        E.frase(c, t, C["s05.a"], [("x:", "g", 62, ENT), ("de", "i", 62), ("−2", "g", 62, ENT), ("até", "i", 62), ("6", "g", 62, ENT)], XE, 260)
        E.frase(c, t, C["s05.a"] + 1.4, ps("sinais diferentes", "i", 50, TINTA2), XE, 340)
        conta_em(c, t, C["s05.a"] + 2.4, [("2 + 6 = ", TINTA), ("8", DX)], XE + 40, 450, 92)
        E.frase(c, t, C["s05.b"], [("y:", "g", 62, SAI), ("de", "i", 62), ("3", "g", 62), ("até", "i", 62), ("−3", "g", 62)], XE, 620)
        conta_em(c, t, C["s05.b"] + 1.6, [("3 + 3 = ", TINTA), ("6", DY)], XE + 40, 740, 92)
    E.saida(c, t, C["s05.c"] - 0.1, s05ab)
    if t < C["s05.c"]:
        return
    conta_em(c, t, C["s05.c"], [("8", DX), ("^2 = 64", TINTA)], XE, 260, 80)
    conta_em(c, t, C["s05.d"], [("6", DY), ("^2 = 36", TINTA)], XE, 370, 80)
    conta_em(c, t, C["s05.e"], [("64 + 36 = 100", TINTA)], XE, 480, 80)
    conta_em(c, t, C["s05.e"] + 1.4, [("r{100} = ", TINTA), ("10", DIST)], XE, 610, 80)
    bola_txt(c, t, C["s05.e"] + 2.6, "10 km", 880, 580, 105, 60)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06.a"] - 0.8, [("somar", "i", 60), ("os", "i", 60), ("catetos:", "i", 60)], XE, 790)
    conta_em(c, t, C["s06.a"], [("8 + 6 = 14", ERRADO)], XE + 430, 790, 70)
    E.frase(c, t, C["s06.b"], ps("é o caminho pelas ruas", "i", 50, TINTA2), XE + 40, 860, passo=0.1)
    E.frase(c, t, C["s06.c"], [("10", "g", 66, CERTO), ("<", "g", 66), ("14:", "g", 66), ("faz", "i", 66), ("sentido", "g", 66, CERTO)], XE, 970)


# ---------------- situação 2: equação da reta ----------------
A2, B2 = (1, 1), (3, 7)


def plano2(c, t, t0):
    plano(c, t, t0, P2, marcas_x=[1, 2, 3, 4, 5], marcas_y=[4, 6, 8], size=34)
    tiques(c, t, t0, P2, (), (-3, -2, -1, 1, 2, 3, 5, 7))


def pontos2(c, t, ta, tb):
    nome(c, t, ta, P2, *A2, "A", lado=(-1, -1))
    nome(c, t, tb, P2, *B2, "B", lado=(1, 0.4))


def b_questao2(c, t, C, b):
    plano2(c, t, C["s07"] + 0.2)
    pontos2(c, t, C["s07.b"] + 0.3, C["s07.c"] + 0.3)
    titulo(c, t, C["s07.a"], 2)
    E.frase(c, t, C["s07.b"], [("A", "g", 66)], XE, 360)
    par_em(c, t, C["s07.b"] + 0.3, "1", "1", XE + 70, 360, 66)
    E.frase(c, t, C["s07.c"], [("B", "g", 66)], XE + 360, 360)
    par_em(c, t, C["s07.c"] + 0.3, "3", "7", XE + 430, 360, 66)
    E.frase(c, t, C["s07.d"], ps("a equação", "i", 66), XE, 520)
    E.frase(c, t, C["s07.d"] + 0.8, [("reduzida", "g", 66, COR), ("e", "i", 66), ("a", "i", 66), ("geral", "g", 66, COR)], XE, 620)
    pausa(c, t, C["s08.a"])


def b_resposta2(c, t, C, b):
    t0 = C["s09"] - 3
    plano2(c, t, t0)
    pontos2(c, t, t0, t0)
    degrau(c, t, P2, A2, B2, C["s09.b"], C["s09.a"], "2", "6", sombra=C["s09.b"] + 0.4, canto_t=C["s09.b"] + 0.5, size=48)
    if t >= C["s09.e"] + 1.2:  # o n é onde a reta corta o eixo y
        reta(c, t, C["s09.e"] + 1.2, P2, A2, B2, DIST, 6, 0.8)
        E.ponto(c, t, C["s09.e"] + 1.6, P2, 0, -2, None, cor=TINTA, r=14)
        E.foco(c, t, C["s09.e"] + 1.8, 0.4, lambda a: E.pilula(c, "n = −2", P2.x(0) - 120, P2.y(-2), 38, "g", fundo=SAI, a=a))
    if t >= C["s10.c"]:
        anel(c, t, C["s10.c"] + 1.6, *P2(*B2), CERTO)
        anel(c, t, C["s10.c"] + 2.1, *P2(*B2), CERTO)

    def s09():
        conta_em(c, t, C["s09.a"], [("Δy", DY), (" = 7 − 1 = ", TINTA), ("6", DY)], XE, 240, 70)
        conta_em(c, t, C["s09.b"], [("Δx", DX), (" = 3 − 1 = ", TINTA), ("2", DX)], XE, 350, 70)
        mfr(c, t, C["s09.c"], "6", "2", XE, 510, 90, pos="= 3", cp=COR, tpos=C["s09.c"] + 1.4, cpre=COR)
        conta_em(c, t, C["s09.d"], [("y = ", TINTA), ("3", COR), ("x + n", TINTA)], XE, 680, 76)
        E.frase(c, t, C["s09.e"] - 1.4, [("troque", "i", 52, TINTA2), ("o", "i", 52, TINTA2), ("A", "g", 52, TINTA2)], XE + 560, 680)
        conta_em(c, t, C["s09.e"], [("1", SAI), (" = 3 · ", TINTA), ("1", ENT), (" + n", TINTA)], XE, 800, 76)
        conta_em(c, t, C["s09.e"] + 1.4, [("n = −2", SAI)], XE, 920, 76)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("reduzida", "i", 60, TINTA2)], XE, 250)
    E.foco(c, t, C["s10.a"] + 0.3, 0.5, lambda a: (E.caixa_pontilhada(c, XE - 30, 290, 720, 150, a, COR),
                                                   E.formula(c, "y = 3x − 2", XE + 10, 400, 100, "g", COR, a)))
    E.frase(c, t, C["s10.b"], [("geral", "i", 60, TINTA2)], XE, 540)
    E.formula_em(c, t, C["s10.b"] + 0.4, "3x − y − 2 = 0", XE, 650, 84, "g", TINTA)
    E.frase(c, t, C["s10.c"], [("confira", "i", 60, TINTA2), ("com", "i", 60, TINTA2), ("o", "i", 60, TINTA2), ("B", "g", 60)], XE, 790)
    conta_em(c, t, C["s10.c"] + 0.6, [("3 · ", TINTA), ("3", ENT), (" − 2 = ", TINTA), ("7", SAI)], XE, 910, 80)
    ok(c, t, C["s10.c"] + 2.4, XE + 520, 885)


# ---------------- situação 3: paralelas? ----------------
def b_questao3(c, t, C, b):
    plano2(c, t, C["s11"] + 0.2)
    reta(c, t, C["s11"] + 0.5, P2, A2, B2, DIST, 6)
    E.foco(c, t, C["s11"] + 1.1, 0.4, lambda a: E.pilula(c, "y = 3x − 2", *P2(2.9, -1.4), 38, "g", fundo=DIST, a=a))
    E.foco(c, t, C["s11.b"] + 1.5, 0.4, lambda a: E.pilula(c, "?", *P2(1.2, 5.8), 48, "g", fundo=TINTA, a=a))
    titulo(c, t, C["s11.a"], 3)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "6x − 2y + 5 = 0", XE, 380, 90, "g", TINTA, a))
    E.frase(c, t, C["s11.b"] + 2.6, [("cruza", "g", 62), ("a", "i", 62), ("reta", "i", 62), ("da", "i", 62), ("situação", "i", 62),
                                     ("2?", "g", 62, COR)], XE, 520)
    E.frase(c, t, C["s11.c"], [("em", "i", 62), ("ângulo", "i", 62), ("reto?", "g", 62, COR)], XE, 630)
    pausa(c, t, C["s12.a"])


def b_resposta3(c, t, C, b):
    t0 = C["s13"] - 3
    plano2(c, t, t0)
    reta(c, t, t0, P2, A2, B2, DIST, 6)
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, "y = 3x − 2", *P2(2.9, -1.4), 38, "g", fundo=DIST, a=a))
    E.ponto(c, t, C["s14.b"], P2, 0, -2, None, cor=DIST, r=14)
    if t >= C["s14.c"]:
        reta(c, t, C["s14.c"], P2, (0, 2.5), (1, 5.5), TINTA, 6)
        E.foco(c, t, C["s14.c"] + 0.7, 0.4, lambda a: E.pilula(c, "y = 3x + 2,5", *P2(-0.5, 6.9), 38, "g", fundo=TINTA, a=a))
    E.ponto(c, t, C["s14.b"] + 0.4, P2, 0, 2.5, None, cor=TINTA, r=14)
    E.foco(c, t, C["s14.b"] + 0.2, 0.4, lambda a: E.pilula(c, "−2", P2.x(0) - 70, P2.y(-2), 34, "g", fundo=DIST, a=a))
    E.foco(c, t, C["s14.b"] + 0.6, 0.4, lambda a: E.pilula(c, "2,5", P2.x(0) - 76, P2.y(2.5), 34, "g", fundo=TINTA, a=a))

    def esq():
        E.frase(c, t, C["s13.a"], [("isole", "g", 66, COR), ("o", "i", 66), ("y", "g", 66, SAI)], XE, 230)
        E.formula_em(c, t, C["s13"] + 0.3, "6x − 2y + 5 = 0", XE, 350, 70, "g", TINTA)
        E.frase(c, t, C["s13.b"] - 1.0, ps("+ 2y nos dois lados", "i", 46, TINTA2), XE + 40, 430, passo=0.08)
        E.formula_em(c, t, C["s13.b"], "2y = 6x + 5", XE, 520, 70, "g", TINTA)
        E.frase(c, t, C["s13.c"] - 1.0, ps("÷ 2 em tudo", "i", 46, TINTA2), XE + 40, 600, passo=0.08)
        E.formula_em(c, t, C["s13.c"], "y = 3x + 2,5", XE, 700, 84, "g", TINTA)
        if t >= C["s14"]:
            conta_em(c, t, C["s14.a"], [("m = 3", COR), ("  nas duas", TINTA)], XE, 830, 64)
            conta_em(c, t, C["s14.b"], [("n:  ", TINTA), ("2,5", TINTA), ("  ≠  ", ERRADO), ("−2", DIST)], XE, 930, 64)
    E.saida(c, t, C["s14.c"] - 0.1, esq)
    if t < C["s14.c"]:
        return

    def conclusao():
        E.frase(c, t, C["s14.c"], [("mesmo", "i", 70), ("m,", "g", 70, COR), ("outro", "i", 70), ("n", "g", 70)], XE, 300)
        E.foco(c, t, C["s14.c"] + 1.2, 0.5, lambda a: E.pilula(c, "paralelas", XE + 230, 450, 72, "g", fundo=CERTO, a=a))
        E.frase(c, t, C["s14.c"] + 2.0, ps("nunca se cruzam", "i", 66), XE, 620, passo=0.12)
    E.saida(c, t, C["s14.d"] - 0.1, conclusao)
    if t < C["s14.d"]:
        return
    E.frase(c, t, C["s14.d"], [("cuidado", "g", 84, ERRADO)], XE, 280)
    E.foco(c, t, C["s14.d"] + 0.4, 0.5, lambda a: E.formula(c, "6x − 2y + 5 = 0", XE, 440, 76, "g", TINTA, a))
    if t >= C["s14.d"] + 1.0:
        anel(c, t, C["s14.d"] + 1.0, XE + 26, 412, ERRADO)
        E.foco(c, t, C["s14.d"] + 1.0, 0.4, lambda a: c.drawCircle(XE + 24, 414, 40, M.paint(ERRADO, a, stroke=6)))
    conta_em(c, t, C["s14.d"] + 1.6, [("m = 6", ERRADO)], XE, 600, 84)
    if t >= C["s14.d"] + 2.6:
        E.risco(c, XE - 10, 630, XE + 280, 540, t, C["s14.d"] + 2.6, largura=10)
    E.frase(c, t, C["s14.d"] + 2.8, ps("o 6 não é o m", "i", 62), XE, 760, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15"], ps("isolar o y sempre funciona", "i", 60, CLARO), W / 2, 170, "center", passo=0.12)
        E.frase(c, t, C["s15"] + 3.0, [("o", "i", 70, CLARO), ("atalho", "g", 70, BR), ("de", "i", 70, CLARO), ("prova", "i", 70, CLARO)],
                W / 2, 280, "center")
        E.foco(c, t, C["s15.a"], 0.5, lambda a: conta(c, [("a", DX_ESC), ("x + ", BR), ("b", DY_ESC), ("y + c = 0", BR)], W / 2, 440, 90, a, "center"))
        x0 = W / 2 - (_w("m = −", 110) + fra(None, "a", "b", 0, 0, 110)) / 2
        E.foco(c, t, C["s15.a"] + 2.0, 0.5, lambda a: (E.formula(c, "m = −", x0, 640, 110, "g", BR, a),
                                                      fra(c, "a", "b", x0 + _w("m = −", 110), 640, 110, a, DX_ESC, DY_ESC, BR)))
        E.frase(c, t, C["s15.a"] + 4.0, ps("cada um com o seu sinal", "i", 54, CLARO), W / 2, 780, "center", passo=0.1)
        E.foco(c, t, C["s15.b"] - 2.0, 0.5, lambda a: conta(c, [("6", DX_ESC), ("x ", BR), ("− 2", DY_ESC), ("y + 5 = 0", BR)], W / 2, 900, 70, a, "center"))
    E.saida(c, t, C["s15.b"] - 0.1, s15, d=0.3)

    def s15b():
        E.foco(c, t, C["s15.b"] - 0.1, 0.5, lambda a: conta(c, [("6", DX_ESC), ("x ", BR), ("− 2", DY_ESC), ("y + 5 = 0", BR)], W / 2, 260, 90, a, "center"))
        wm, wf = _w("m = −", 120), fra(None, "6", "−2", 0, 0, 120)
        x0 = W / 2 - (wm + wf + 20 + _w("= 3", 120)) / 2
        E.foco(c, t, C["s15.b"], 0.5, lambda a: (E.formula(c, "m = −", x0, 520, 120, "g", BR, a),
                                                fra(c, "6", "−2", x0 + wm, 520, 120, a, DX_ESC, DY_ESC, BR)))
        E.foco(c, t, C["s15.b"] + 1.4, 0.5, lambda a: E.formula(c, "= 3", x0 + wm + wf + 20, 520, 120, "g", BR, a))
        E.frase(c, t, C["s15.b"] + 2.6, [("sem", "i", 70, CLARO), ("isolar", "i", 70, CLARO), ("nada", "g", 70, BR)], W / 2, 800, "center")
    if t >= C["s15.b"] - 0.1:
        E.saida(c, t, C["s16"] - 0.1, s15b)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], [("por", "i", 64, CLARO), ("que", "i", 64, CLARO), ("funciona", "g", 64, BR)], XE, 200)
    E.foco(c, t, C["s16"] + 0.6, 0.5, lambda a: conta(c, [("a", DX_ESC), ("x + ", BR), ("b", DY_ESC), ("y + c = 0", BR)], XE, 360, 76, a))
    E.foco(c, t, C["s16.a"] + 0.4, 0.5, lambda a: conta(c, [("b", DY_ESC), ("y = −", BR), ("a", DX_ESC), ("x − c", BR)], XE, 510, 76, a))
    wy = _w("y = −", 76)
    wf = fra(None, "a", "b", 0, 0, 76)
    E.foco(c, t, C["s16.b"], 0.5, lambda a: (E.formula(c, "y = −", XE, 680, 76, "g", BR, a),
                                            fra(c, "a", "b", XE + wy, 680, 76, a, DX_ESC, DY_ESC, BR),
                                            E.formula(c, "x − …", XE + wy + wf + 10, 680, 76, "g", BR, a)))
    E.foco(c, t, C["s16.b"] + 1.4, 0.5, lambda a: E.pilula(c, "m", XE + wy + wf / 2 - 12, 790, 46, "g", fundo=COR, a=a))
    wn = E.frase(c, t, C["s16.b"] + 3.0, ps("na situação:", "i", 56, CLARO), XE, 900)
    E.foco(c, t, C["s16.b"] + 3.4, 0.5, lambda a: (fra(c, "6", "2", XE + wn + 24, 900, 76, a, DX_ESC, DY_ESC, BR),
                                                  E.formula(c, "= 3", XE + wn + 24 + fra(None, "6", "2", 0, 0, 76) + 14, 900, 76, "g", BR, a)))
    # quando não compensa
    X2 = 1060
    E.frase(c, t, C["s16.c"], [("precisa", "i", 62, CLARO), ("do", "i", 62, CLARO), ("n?", "g", 62, BR)], X2, 260)
    E.frase(c, t, C["s16.c"] + 1.6, ps("onde corta o eixo y", "i", 50, CLARO), X2, 350, passo=0.1)
    E.foco(c, t, C["s16.d"], 0.5, lambda a: (E.caixa_pontilhada(c, X2 - 30, 400, 700, 140, a, BR),
                                            E.formula(c, "isole o y de vez", X2 + 10, 495, 64, "g", BR, a)))
    ws = E.frase(c, t, C["s16.d"] + 2.4, [("sem", "i", 62, CLARO), ("y:", "g", 62, BR)], X2, 700)
    E.foco(c, t, C["s16.d"] + 3.2, 0.5, lambda a: E.formula(c, "x − 3 = 0", X2 + ws + 30, 700, 66, "g", BR, a))
    E.frase(c, t, C["s16.d"] + 5.0, [("reta", "i", 56, CLARO), ("em", "i", 56, CLARO), ("pé,", "i", 56, CLARO), ("sem", "i", 56, CLARO),
                                     ("m", "g", 56, BR)], X2, 820)
    q = ease_io(prog(t, C["s16.d"] + 4.0, 0.6))
    if q > 0:
        M.line(c, 1680, 960, 1680, lerp(960, 600, q), DX_ESC, 1.0, 8)


# ---------------- situação 4: perpendicular e encontro ----------------
Q4, E4 = (6, 2), (2, 4)


def plano4(c, t, t0):
    plano(c, t, t0, P4, marcas_x=[2, 4, 6], marcas_y=[2, 4, 6], size=36)
    tiques(c, t, t0, P4, (1, 3, 5, 7), (1, 3, 5, 7))


def dada(c, t, t0, rot=True):
    reta(c, t, t0, P4, (0, 0), (1, 2), DIST, 6)
    if rot:
        E.foco(c, t, t0 + 0.7, 0.4, lambda a: E.pilula(c, "y = 2x", *P4(4.2, 6.4), 38, "g", fundo=DIST, a=a))


def b_questao4(c, t, C, b):
    plano4(c, t, C["s17"] + 0.2)
    nome(c, t, C["s17.b"] + 0.3, P4, *Q4, "P", lado=(0.3, -1))
    dada(c, t, C["s17.c"] + 0.4)
    E.foco(c, t, C["s17.d"] + 0.5, 0.4, lambda a: E.pilula(c, "?", *P4(4.2, 3.1), 48, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s17.a"], [("última", "i", 74), ("situação", "g", 74, COR)], XE, 200)
    E.frase(c, t, C["s17.b"], [("passa", "i", 62), ("por", "i", 62), ("P", "g", 62)], XE, 340)
    par_em(c, t, C["s17.b"] + 0.6, "6", "2", XE + 330, 340, 62)
    wp = E.frase(c, t, C["s17.c"], [("perpendicular", "g", 62, COR), ("a", "i", 62)], XE, 460)
    E.formula_em(c, t, C["s17.c"] + 0.8, "y = 2x", XE + wp + 22, 460, 62, "g", DIST)
    E.frase(c, t, C["s17.d"], [("onde", "i", 62), ("as", "i", 62), ("duas", "i", 62), ("se", "i", 62), ("cruzam?", "g", 62)], XE, 600)
    pausa(c, t, C["s18.a"])


def b_resposta4(c, t, C, b):
    t0 = C["s19"] - 3
    plano4(c, t, t0)
    nome(c, t, t0, P4, *Q4, "P", lado=(0.3, -1))
    dada(c, t, t0)
    if t >= C["s20.d"] + 0.8:
        reta(c, t, C["s20.d"] + 0.8, P4, Q4, (4, 3), TINTA, 6)
        E.foco(c, t, C["s20.d"] + 1.5, 0.4, lambda a: E.pilula(c, "y = −½x + 5", *P4(5.0, 0.9), 38, "g", fundo=TINTA, a=a))
    if t >= C["s22.b"]:
        E.angulo(c, t, C["s22.b"] + 0.4, P4(*E4), P4(3, 6), P4(4, 3), r=52, cor=TINTA, preenche=0.12)
        achado(c, t, C["s22.b"], P4, *E4, None)

    def s19():
        E.frase(c, t, C["s19"], [("a", "i", 62), ("dada", "i", 62)], XE, 240)
        conta_em(c, t, C["s19.a"], [("m = 2", DIST)], XE + 230, 240, 72)
        E.frase(c, t, C["s19.b"], [("inverta", "g", 62, COR), ("e", "i", 62), ("troque", "g", 62, COR), ("o", "i", 62), ("sinal", "i", 62)], XE, 400)
        E.foco(c, t, C["s19.b"] + 1.4, 0.5, lambda a: E.formula(c, "2  →  f{1}{2}  →  −f{1}{2}", XE, 560, 80, "g", TINTA, a))
        conta_em(c, t, C["s19.b"] + 3.0, [("m' = −f{1}{2}", TINTA)], XE, 720, 80)
        conta_em(c, t, C["s19.c"], [("2 · (−f{1}{2}) = −1", TINTA)], XE, 900, 76)
        ok(c, t, C["s19.c"] + 1.6, XE + 640, 870)
    E.saida(c, t, C["s20"] - 0.1, s19)

    def s20():
        E.frase(c, t, C["s20"], ps("ponto e inclinação", "i", 60, TINTA2), XE, 220)
        conta_em(c, t, C["s20.a"], [("y − ", TINTA), ("2", SAI), (" = −f{1}{2}(x − ", TINTA), ("6", ENT), (")", TINTA)], XE, 360, 72)
        conta_em(c, t, C["s20.b"], [("−f{1}{2} · (−6) = 3", TINTA2)], XE + 60, 500, 58)
        conta_em(c, t, C["s20.c"], [("y − 2 = −f{1}{2}x + 3", TINTA)], XE, 650, 72)
        E.frase(c, t, C["s20.d"] - 1.0, ps("+ 2 nos dois lados", "i", 46, TINTA2), XE + 60, 740, passo=0.08)
        E.foco(c, t, C["s20.d"], 0.5, lambda a: (E.caixa_pontilhada(c, XE - 30, 790, 640, 150, a, COR),
                                                E.formula(c, "y = −f{1}{2}x + 5", XE + 10, 895, 80, "g", TINTA, a)))
    if t >= C["s20"]:
        E.saida(c, t, C["s21"] - 0.1, s20)

    def s21():
        E.frase(c, t, C["s21"], [("o", "i", 60), ("encontro", "g", 60, COR)], XE, 220)
        E.frase(c, t, C["s21.a"], [("o", "i", 56), ("y", "g", 56, SAI), ("é", "i", 56), ("o", "i", 56), ("mesmo", "g", 56), ("nas", "i", 56),
                                   ("duas", "i", 56)], XE, 320)
        conta_em(c, t, C["s21.b"], [("2x", DIST), (" = ", TINTA), ("−f{1}{2}x + 5", TINTA)], XE, 470, 76)
        E.frase(c, t, C["s21.c"] - 1.6, ps("× 2 em tudo", "i", 46, TINTA2), XE + 60, 560, passo=0.08)
        conta_em(c, t, C["s21.c"], [("4x = −x + 10", TINTA)], XE, 660, 76)
        conta_em(c, t, C["s21.d"], [("5x = 10", TINTA)], XE, 800, 76)
        conta_em(c, t, C["s21.d"] + 1.6, [("x = 2", ENT)], XE + 400, 800, 76)
    if t >= C["s21"]:
        E.saida(c, t, C["s22"] - 0.1, s21)
    if t < C["s22"]:
        return
    conta_em(c, t, C["s22.a"], [("x = 2", ENT)], XE, 240, 66)
    conta_em(c, t, C["s22.a"] + 0.6, [("y = 2 · 2 = ", TINTA), ("4", SAI)], XE + 280, 240, 66)
    E.frase(c, t, C["s22.b"], [("encontro", "i", 60), ("em", "i", 60)], XE, 400)
    E.foco(c, t, C["s22.b"] + 0.4, 0.5, lambda a: (E.bola(c, XE + 560, 380, 92 * ease_back(prog(t, C["s22.b"] + 0.4, 0.5)), a=a),
                                                  E.formula(c, "(2, 4)", XE + 560, 402, 58, "g", BR, a, "center")))
    E.frase(c, t, C["s22.b"] + 1.4, ps("em ângulo reto", "i", 54, TINTA2), XE, 520, passo=0.1)
    E.frase(c, t, C["s22.c"], [("confira", "i", 56, TINTA2), ("na", "i", 56, TINTA2), ("outra:", "i", 56, TINTA2)], XE, 680)
    conta_em(c, t, C["s22.c"] + 0.6, [("−f{1}{2} · 2 + 5 = ", TINTA), ("4", SAI)], XE, 820, 72)
    ok(c, t, C["s22.c"] + 2.6, XE + 610, 795)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s23.a", [("distância", "g", 80, DIST), ("=", "i", 80), ("hipotenusa", "i", 80)]),
                 ("s23.b", [("o", "i", 80), ("m", "g", 80, COR), ("diz", "i", 80), ("paralela", "g", 80), ("ou", "i", 80), ("perpendicular", "g", 80)]),
                 ("s23.c", [("encontro", "g", 80, COR), ("=", "i", 80), ("sistema", "i", 80)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s24.a"], [("Equação", "g", 130, COR), ("da", "i", 110)], XE, 460)
    E.frase(c, t, C["s24.a"] + 0.4, [("circunferência", "g", 130, COR)], XE, 610)
    E.frase(c, t, C["s24.b"], [("centro", "g", 70), ("e", "i", 70), ("raio", "g", 70), ("de", "i", 70), ("olho", "i", 70)], XE, 740)
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4,
              resposta4=b_resposta4, fim=b_fim)
