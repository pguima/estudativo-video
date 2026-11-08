"""Visual — Estudativo · MAT-ANA-010: posições relativas — ponto e circunferência (compara com r²), reta e circunferência (delta).

Segue a linguagem da Geometria Analítica (MAT-ANA-001) e a da circunferência (MAT-ANA-008, leia o cabeçalho de lá):
- a circunferência e o raio em índigo (DIST), o centro como ponto preto "C"; do centro até um ponto, o cateto deitado em petróleo
  (DX) e o em pé em âmbar (DY): a soma dos quadrados é a distância ao quadrado, que se compara com r² (índigo);
- as retas que testamos são pretas (a circunferência já é a figura índigo); os pontos de encontro são achados: índigo com anel;
- a posição vem numa pílula preta ("dentro", "em cima", "fora", "secante", "tangente", "externa"); o delta é a conta da reta;
- erro em vermelho, certo em verde, atalho no palco escuro, resposta na esfera.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Analítica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANA-010_posicoes_relativas_ponto_reta_circunferencia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ponto", "reta", "outras", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ENT, SAI = COR, TINTA                       # x / y, como em Funções
DX, DY, DIST = "#0E9AA7", "#D98A00", E.COR  # cateto deitado, cateto em pé, raio / circunferência
DX_ESC, DY_ESC = "#3CC7D3", "#FFB833"
# as contas do roteiro
_d2 = lambda x, y: (x - 2) ** 2 + (y + 1) ** 2
assert _d2(5, -1) == 9 and _d2(6, 2) == 25 > 9 and _d2(4, 1) == 8 < 9
assert all(r * r + r - 12 == 0 for r in (3, -4)) and 1 ** 2 - 4 * 1 * (-12) == 49 and 3 ** 2 + 4 ** 2 == 25 and 4 ** 2 + 3 ** 2 == 25
assert 20 ** 2 == 400 and 4 * 2 * 75 == 600 and 400 - 600 == -200 and all(2 * x * x + 20 * x + 75 == x * x + (x + 10) ** 2 - 25 for x in (0, 1, 2))
assert 9 + 4 == 13 > 10 and all(10 * x * x - 60 * x + 90 == x * x + (10 - 3 * x) ** 2 - 10 for x in (0, 1)) and 36 - 4 * 9 == 0
assert 3 ** 2 + (10 - 9) ** 2 == 10


def plano_igual(xmin, xmax, ymin, ymax, lado=740, cx=1430, cy=545):
    """Plano com a mesma escala nos dois eixos (a circunferência sai redonda), centrado em (cx, cy)"""
    u = lado / max(xmax - xmin, ymax - ymin)
    w, h = (xmax - xmin) * u, (ymax - ymin) * u
    return E.Plano(cx - w / 2, cy - h / 2, w, h, xmin, xmax, ymin, ymax)


PP = plano_igual(-2, 7, -5, 4)      # (x − 2)² + (y + 1)² = 9 e os pontos (5, −1), (6, 2), (4, 1)
PR = plano_igual(-8, 8, -8, 8)      # x² + y² = 25 e as retas y = x + 1, y = 5, y = x + 10
PQ = plano_igual(-5, 6, -5, 6)      # questão: x² + y² = 10, (3, 2) e y = 10 − 3x


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


# ---------------- peças da circunferência ----------------
def eixos(c, t, t0, P, mx, my, size=34):
    """plano com rótulos só em mx e my e tracinhos sem número nos outros inteiros"""
    plano(c, t, t0, P, marcas_x=mx, marcas_y=my, size=size)
    tiques(c, t, t0, P, [v for v in range(math.ceil(P.xmin), int(P.xmax) + 1) if v not in mx and v != 0],
           [v for v in range(math.ceil(P.ymin), int(P.ymax) + 1) if v not in my and v != 0])


def circ(c, t, t0, P, a, b, r, cor=None, d=0.9, largura=7, tracejado=False, alfa=1.0):
    """circunferência de centro (a, b) e raio r (valores) no plano P, que se fecha a partir da direita"""
    if t < t0 or alfa <= 0:
        return
    X, Y = P(a, b)
    R = P.x(a + r) - X
    p = ease_io(prog(t, t0, d))
    pt = M.paint(cor or DIST, alfa, stroke=largura, cap_round=True)
    if tracejado:
        pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    x, y, w, h = P.caixa
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x - 8, y - 8, w + 16, h + 16), True)
    c.drawArc(skia.Rect.MakeXYWH(X - R, Y - R, 2 * R, 2 * R), 0, -360 * p, False, pt)
    c.restore()


def centro_c(c, t, t0, P, a, b, lado=(-1, 1), s="C"):
    nome(c, t, t0, P, a, b, s, lado=lado, size=46)


def eqn(c, t, t0, partes, x, y, size, align="left", caixa=None):
    """equação com partes coloridas que entra no cue; caixa = instante da caixa pontilhada em volta"""
    conta_em(c, t, t0, partes, x, y, size, align)
    if caixa is not None and t >= caixa:
        w = conta(None, partes, 0, 0, size, 0)
        x0 = x - w / 2 if align == "center" else x
        p = ep(t, caixa, 0.5)
        E.caixa_pontilhada(c, x0 - 30, y - size * 1.05, w + 60, size * 1.45, p, COR, prog_=p)


def red(xp, yp, rr, cx=DX, cy=DY, cr=DIST, tinta=TINTA):
    """partes da equação reduzida: red("(x − 2)^2", "(y + 1)^2", "9")"""
    return [(xp, cx), (" + ", tinta), (yp, cy), (" = ", tinta), (rr, cr)]


def pil(c, t, t0, s, x, y, size=40, fundo=None):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, x, y, size, "g", fundo=fundo or COR, a=a))


def reta_y(c, t, t0, P, m, n, cor=TINTA, largura=6, d=0.8):
    """reta y = mx + n, de borda a borda do plano"""
    if t >= t0:
        E.reta_pontos(c, t, t0, P, (0, n), (1, m + n), cor=cor, pontos=False, largura=largura, d=d)


def ate_centro(c, t, t0, P, Cc, Pt, lx=None, ly=None, size=44, hip=True):
    """do centro até o ponto: cateto deitado (petróleo), em pé (âmbar) e a distância tracejada (índigo)"""
    R = (Pt[0], Cc[1])
    cateto(c, t, t0, P, Cc, R, DX, 0.5, 8)
    cateto(c, t, t0 + 0.4, P, R, Pt, DY, 0.5, 8)
    if hip:
        seg(c, t, t0 + 0.8, P, Cc, Pt, DIST, 0.5, 5, tracejado=True)
    G = ((Cc[0] + R[0] + Pt[0]) / 3, (Cc[1] + R[1] + Pt[1]) / 3)
    if lx:
        lado_txt(c, t, t0 + 0.3, P, Cc, R, lx, G, DX, size)
    if ly and Pt[1] != Cc[1]:
        lado_txt(c, t, t0 + 0.7, P, R, Pt, ly, G, DY, size)


def posicao(c, t, t0, s, x, y, size=46, fundo=TINTA):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, x, y, size, "g", fundo=fundo, a=a))


def circ_pp(c, t, t0, tc=None):
    eixos(c, t, t0, PP, [-2, 2, 4, 6], [-4, 2, 4])
    circ(c, t, t0 if tc is None else tc, PP, 2, -1, 3)
    centro_c(c, t, t0 if tc is None else tc, PP, 2, -1, lado=(-1, 1))


def circ_pr(c, t, t0):
    eixos(c, t, t0, PR, [-5, 5], [-5, 5], size=32)
    circ(c, t, t0 + 0.2, PR, 0, 0, 5)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def s01():
        circ_pr(c, t, C["s01.a"])
        reta_y(c, t, C["s01.a"] + 0.8, PR, 1, 1)
        achado(c, t, C["s01.a"] + 1.6, PR, 3, 4)
        achado(c, t, C["s01.a"] + 1.8, PR, -4, -3)
        reta_y(c, t, C["s01.b"], PR, 0, 5, TINTA2)
        achado(c, t, C["s01.b"] + 0.7, PR, 0, 5)
        reta_y(c, t, C["s01.c"], PR, 1, 10, TINTA2)
        E.frase(c, t, C["s01.a"], [("se", "i", 80), ("cortam?", "g", 80, COR)], XE, 330)
        E.frase(c, t, C["s01.b"], [("só", "i", 80), ("se", "i", 80), ("encostam?", "g", 80, COR)], XE, 470)
        E.frase(c, t, C["s01.c"], [("nem", "i", 80), ("se", "i", 80), ("tocam?", "g", 80, COR)], XE, 610)
        E.frase(c, t, C["s01.d"], [("uma", "i", 70), ("conta:", "i", 70), ("o", "i", 70), ("delta", "g", 76, COR)], XE, 800)
        E.foco(c, t, C["s01.d"] + 0.8, 0.5, lambda a: E.formula(c, "Δ = b^2 − 4ac", XE, 920, 70, "g", TINTA, a))
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    E.foco(c, t, C["s02.a"] + 1.0, 0.7, lambda a: E.bola(c, 1480, 540, 270 * ease_back(prog(t, C["s02.a"] + 1.0, 0.7))), blur=0)
    E.foco(c, t, C["s02.a"] + 1.4, 0.5, lambda a: centro(c, "Δ", 1480, 630, 260, "g", BR, a))
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 300)
    E.frase(c, t, C["s02.a"] + 1.0, [("onde", "i", 90), ("fica", "i", 90), ("o", "i", 90), ("ponto", "g", 96, COR)], XE, 450)
    E.frase(c, t, C["s02.b"], [("o", "i", 90), ("que", "i", 90), ("a", "i", 90), ("reta", "g", 96, COR), ("faz", "i", 90)], XE, 600)
    E.frase(c, t, C["s02.c"], [("+", "g", 84, COR), ("atalho", "g", 84), ("de", "i", 84), ("prova", "i", 84)], XE, 750)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 80, TINTA, C["s03"]), ("vai", "i", 80, TINTA, C["s03"] + 0.2), ("usar", "i", 80, TINTA, C["s03"] + 0.4),
                   ("três", "g", 76, COR, C["s03.a"]), ("coisas", "i", 80, TINTA, C["s03.a"] + 0.2)], W / 2, 180, "center")
    x, w, h = 230, 1460, 200
    for i, k in enumerate(("s03.b", "s03.c", "s03.d")):
        y = 240 + i * 230
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, x + 80, y + h / 2, 46, a=a),
                                                     centro(c, str(i + 1), x + 80, y + h / 2 + 20, 54, "g", BR, a)))
    E.frase(c, t, C["s03.b"] + 0.1, [("centro", "g", 60), ("e", "i", 60), ("raio", "g", 60, DIST)], x + 170, 315)
    conta_em(c, t, C["s03.b"] + 0.8, red("(x − a)^2", "(y − b)^2", "r^2"), x + 170, 405, 62)
    E.frase(c, t, C["s03.c"] + 0.1, [("encontro", "g", 60, COR), ("=", "i", 60), ("solução", "i", 60), ("do", "i", 60), ("sistema", "g", 60)], x + 170, 545)
    E.frase(c, t, C["s03.c"] + 1.6, ps("pela substituição", "i", 52, TINTA2), x + 170, 625, passo=0.1)
    E.foco(c, t, C["s03.d"] + 0.1, 0.5, lambda a: E.formula(c, "Δ = b^2 − 4ac", x + 170, 790, 72, "g", COR, a))
    E.frase(c, t, C["s03.d"] + 3.0, ps("conta as raízes", "i", 56, TINTA2), x + 760, 790, passo=0.1)
    E.frase(c, t, C["s04"] - 2.6, ps("faltou alguma? procure no canal", "i", 50, TINTA2), W / 2, 1000, "center", passo=0.1)


# ---------------- o ponto ----------------
def b_ponto(c, t, C, b):
    circ_pp(c, t, C["s04"] + 0.2, C["s04.a"] + 0.2)
    if t >= C["s04.b"]:
        seg(c, t, C["s04.b"] + 0.4, PP, (2, -1), (2, 2), DIST, 0.6, 7)
        lado_txt(c, t, C["s04.b"] + 0.9, PP, (2, -1), (2, 2), "3", (1, 0.5), DIST, 46)

    def s04():
        eqn(c, t, C["s04.a"], red("(x − 2)^2", "(y + 1)^2", "9"), XE, 240, 66)
        E.frase(c, t, C["s04.b"], [("centro", "i", 56)], XE, 360)
        par_em(c, t, C["s04.b"] + 0.4, "2", "−1", XE + 210, 360, 56)
        E.frase(c, t, C["s04.b"] + 1.2, [("raio", "i", 56), ("3", "g", 56, DIST)], XE + 520, 360)
        E.frase(c, t, C["s04.c"], [("esquerda", "g", 60), ("=", "i", 60), ("distância", "g", 60, DIST), ("ao", "i", 60), ("centro,", "i", 60)], XE, 520)
        E.frase(c, t, C["s04.c"] + 1.4, [("ao", "i", 60), ("quadrado", "g", 60)], XE, 610)
        E.frase(c, t, C["s04.d"], [("troque", "g", 60, COR), ("o", "i", 60), ("ponto", "i", 60), ("e", "i", 60), ("compare", "i", 60), ("com", "i", 60),
                                   ("9", "g", 60, DIST)], XE, 780)
    E.saida(c, t, C["s05"] - 0.1, s04)
    # os três pontos
    pts = ((C["s05.a"], (5, -1), "3", None, "em cima", C["s05.c"]), (C["s05.d"], (6, 2), "4", "3", "fora", C["s05.f"]),
           (C["s06.a"], (4, 1), "2", "2", "dentro", C["s06.c"]))
    fins = (C["s05.d"] - 0.1, C["s06.a"] - 0.1, C["s06.d"] - 0.1)
    for (t0, P_, lx, ly, pos, tp), t1 in zip(pts, fins):
        if t >= t0:
            nome(c, t, t0 + 0.2, PP, *P_, None)
            E.saida(c, t, t1, lambda t0=t0, P_=P_, lx=lx, ly=ly: ate_centro(c, t, t0 + 0.5, PP, (2, -1), P_, lx, ly, hip=P_[1] != -1))
            lado = (1, 1) if P_ == (5, -1) else (1, -0.4)
            E.foco(c, t, tp, 0.4, lambda a, P_=P_, pos=pos, lado=lado: E._cola(c, pos, *PP(*P_), *lado, 24, 40, "g", TINTA, a))
    if t < C["s05"]:
        return

    def linhas():
        for i, (t0, P_, _, _, pos, tp) in enumerate(pts):
            y = 260 + i * 220
            par_em(c, t, t0, str(P_[0]), "−1" if P_[1] == -1 else str(P_[1]), XE, y, 56)
        conta_em(c, t, C["s05.b"], [("3", DX), ("^2 + ", TINTA), ("0", DY), ("^2 = ", TINTA), ("9", DIST)], XE + 260, 260, 60)
        posicao(c, t, C["s05.c"], "= 9: em cima", XE + 330, 345, 40, DIST)
        conta_em(c, t, C["s05.e"], [("4", DX), ("^2 + ", TINTA), ("3", DY), ("^2 = 25", TINTA)], XE + 260, 480, 60)
        posicao(c, t, C["s05.f"], "> 9: fora", XE + 300, 565, 40)
        conta_em(c, t, C["s06.b"], [("2", DX), ("^2 + ", TINTA), ("2", DY), ("^2 = 8", TINTA)], XE + 260, 700, 60)
        posicao(c, t, C["s06.c"], "< 9: dentro", XE + 310, 785, 40)
    E.saida(c, t, C["s06.d"] - 0.1, linhas)
    if t < C["s06.d"]:
        return
    E.frase(c, t, C["s06.d"] - 0.6, [("a", "i", 70), ("regra", "g", 70, COR)], XE, 260)
    for i, (k, sinal, pos) in enumerate((("s06.d", "<", "dentro"), ("s06.e", "=", "em cima"), ("s06.f", ">", "fora"))):
        y = 420 + i * 150
        conta_em(c, t, C[k], [(sinal + " r^2", DIST)], XE, y, 76)
        posicao(c, t, C[k] + 0.3, pos, XE + 420, y - 26, 52)


# ---------------- a reta: secante ----------------
def b_reta(c, t, C, b):
    circ_pr(c, t, C["s07.a"])
    centro_c(c, t, C["s07.a"] + 0.6, PR, 0, 0, lado=(-1, 1))
    reta_y(c, t, C["s07.b"], PR, 1, 1)
    E.foco(c, t, C["s07.b"] + 0.7, 0.4, lambda a: E.pilula(c, "y = x + 1", *PR(5.3, 7.3), 38, "g", fundo=TINTA, a=a))
    achado(c, t, C["s10.d"], PR, 3, 4, "(3, 4)", lado=(1, 0.3), size=40)
    achado(c, t, C["s10.e"], PR, -4, -3, "(−4, −3)", lado=(1, 0.6), size=40)

    def s07():
        E.frase(c, t, C["s07.a"], [("centro", "i", 58)], XE, 250)
        par_em(c, t, C["s07.a"] + 0.4, "0", "0", XE + 210, 250, 58)
        E.frase(c, t, C["s07.a"] + 1.2, [("raio", "i", 58), ("5", "g", 58, DIST)], XE + 470, 250)
        E.frase(c, t, C["s07.c"], [("um", "i", 60), ("ponto", "i", 60), ("de", "i", 60), ("encontro", "g", 60, COR), ("cumpre", "i", 60), ("as", "i", 60),
                                   ("duas", "g", 60)], XE, 430, passo=0.1)
        E.sistema(c, t, C["s07.c"] + 1.4, ["x^2 + y^2 = 25", "y = x + 1"], XE + 40, 600, 80, tl=[C["s07.c"] + 1.4, C["s07.c"] + 1.8])
    E.saida(c, t, C["s08"] - 0.1, s07)

    def s08():
        E.frase(c, t, C["s08.a"], [("troque", "g", 60, COR), ("o", "i", 60), ("y", "g", 60, SAI), ("por", "i", 60), ("x + 1", "g", 60)], XE, 240)
        conta_em(c, t, C["s08.b"], [("x^2 + ", TINTA), ("(x + 1)^2", COR), (" = 25", TINTA)], XE, 380, 70)
        conta_em(c, t, C["s08.b"] + 4.0, [("(x + 1)^2", COR), (" = x^2 + 2x + 1", TINTA)], XE + 40, 490, 54)
        conta_em(c, t, C["s08.c"], [("2x^2 + 2x + 1 = 25", TINTA)], XE, 640, 70)
        E.frase(c, t, C["s08.d"] - 2.4, ps("− 25 e ÷ 2", "i", 48, TINTA2), XE + 40, 730, passo=0.08)
        eqn(c, t, C["s08.d"], [("x^2 + x − 12 = 0", TINTA)], XE, 870, 80, caixa=C["s08.d"] + 1.0)
    E.saida(c, t, C["s09"] - 0.1, s08)

    def s09():
        conta_em(c, t, C["s09"], [("x^2 + x − 12 = 0", TINTA)], XE, 220, 62)
        E.frase(c, t, C["s09.a"], [("cada", "i", 56), ("raiz", "g", 56), ("=", "i", 56), ("um", "i", 56), ("ponto", "i", 56), ("de", "i", 56),
                                   ("encontro", "g", 56, COR)], XE, 330, passo=0.1)
        E.frase(c, t, C["s09.b"], [("o", "i", 56), ("delta", "g", 56, COR), ("conta", "i", 56), ("os", "i", 56), ("pontos", "i", 56)], XE, 420)
        E.frase(c, t, C["s09.b"] + 2.6, ps("a, b e c da equação, não o centro", "i", 46, TINTA2), XE, 495, passo=0.08)
        conta_em(c, t, C["s09.c"], [("a = 1    b = 1    c = −12", TINTA)], XE, 600, 56)
        conta_em(c, t, C["s09.d"], [("b^2 = 1", TINTA)], XE, 710, 56)
        conta_em(c, t, C["s09.e"], [("4 · 1 · (−12) = −48", TINTA)], XE + 300, 710, 56)
        conta_em(c, t, C["s09.f"], [("Δ = 1 − (−48) = 1 + 48 = ", TINTA), ("49", COR)], XE, 840, 64)
        posicao(c, t, C["s09.f"] + 2.4, "Δ > 0", XE + 150, 930, 44, COR)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10"], [("Δ", "g", 70, COR), ("=", "i", 70), ("49", "g", 70), (">", "g", 70), ("0", "g", 70)], XE, 240)
    E.frase(c, t, C["s10.a"], [("2", "g", 64, COR), ("raízes:", "i", 64), ("2", "g", 64, COR), ("pontos", "i", 64)], XE, 370)
    posicao(c, t, C["s10.b"], "secante", XE + 170, 480, 60)
    conta_em(c, t, C["s10.c"], [("x = 3", ENT), ("   ou   ", TINTA2), ("x = −4", ENT)], XE, 640, 64)
    E.foco(c, t, C["s10.d"], 0.5, lambda a: par(c, "3", "4", XE, 780, 60, a))
    E.foco(c, t, C["s10.e"], 0.5, lambda a: par(c, "−4", "−3", XE + 260, 780, 60, a))


# ---------------- tangente e externa ----------------
def b_outras(c, t, C, b):
    circ_pr(c, t, C["s11"])
    E.saida(c, t, C["s11.a"], lambda: reta_y(c, t, C["s11"], PR, 1, 1, TINTA2, 4))
    reta_y(c, t, C["s11.a"], PR, 0, 5)
    E.foco(c, t, C["s11.a"] + 0.7, 0.4, lambda a: E.pilula(c, "y = 5", *PR(6.4, 4.3), 38, "g", fundo=TINTA, a=a))
    achado(c, t, C["s11.e"], PR, 0, 5, "(0, 5)", lado=(1, -1), size=40)
    reta_y(c, t, C["s12.a"], PR, 1, 10)
    E.foco(c, t, C["s12.a"] + 0.7, 0.4, lambda a: E.pilula(c, "y = x + 10", *PR(-5.6, 7.3), 38, "g", fundo=TINTA, a=a))
    if t >= C["s13"]:
        reta_y(c, t, C["s13"], PR, 1, 1, TINTA2, 4)

    def s11():
        E.frase(c, t, C["s11.a"], [("reta", "i", 60), ("y = 5", "g", 60)], XE, 240)
        conta_em(c, t, C["s11.b"], [("x^2 + ", TINTA), ("5^2", COR), (" = 25", TINTA)], XE, 380, 70)
        conta_em(c, t, C["s11.c"], [("x^2 = 0", TINTA)], XE, 510, 70)
        conta_em(c, t, C["s11.d"], [("b = 0,  c = 0:  ", TINTA2), ("Δ = 0", COR)], XE, 640, 62)
        E.frase(c, t, C["s11.d"] + 1.6, ps("um ponto só", "i", 54, TINTA2), XE, 730, passo=0.1)
        posicao(c, t, C["s11.e"], "tangente", XE + 180, 850, 60)
    E.saida(c, t, C["s12"] - 0.1, s11)

    def s12():
        E.frase(c, t, C["s12.a"], [("reta", "i", 60), ("y = x + 10", "g", 60)], XE, 220)
        conta_em(c, t, C["s12.b"], [("2x^2 + 20x + 75 = 0", TINTA)], XE, 340, 66)
        conta_em(c, t, C["s12.b"] + 3.0, [("a = 2    b = 20    c = 75", TINTA2)], XE, 430, 50)
        conta_em(c, t, C["s12.c"], [("b^2 = 400", TINTA)], XE, 540, 60)
        conta_em(c, t, C["s12.d"], [("4 · 2 · 75 = 600", TINTA)], XE + 360, 540, 60)
        conta_em(c, t, C["s12.e"], [("Δ = 400 − 600 = ", TINTA), ("−200", COR)], XE, 670, 66)
        E.frase(c, t, C["s12.f"], [("Δ", "g", 60, COR), ("<", "g", 60), ("0:", "g", 60), ("nenhum", "i", 60), ("ponto", "i", 60)], XE, 790)
        posicao(c, t, C["s12.g"], "externa", XE + 160, 900, 60)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13"], [("a", "i", 70), ("regra", "g", 70, COR), ("da", "i", 70), ("reta", "i", 70)], XE, 260)
    for i, (k, s_, pos) in enumerate((("s13.a", "Δ > 0", "secante"), ("s13.b", "Δ = 0", "tangente"), ("s13.c", "Δ < 0", "externa"))):
        y = 420 + i * 150
        conta_em(c, t, C[k], [(s_, COR)], XE, y, 76)
        posicao(c, t, C[k] + 0.2, pos, XE + 430, y - 26, 52)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    circ_pp(c, t, C["s14"] + 0.2)
    nome(c, t, C["s14"] + 0.4, PP, 4, 1, None)
    ate_centro(c, t, C["s14.b"] - 0.6, PP, (2, -1), (4, 1), "2", "2")
    if t >= C["s14.e"]:
        anel(c, t, C["s14.e"] + 0.6, *PP(4, 1), CERTO)
        anel(c, t, C["s14.e"] + 1.1, *PP(4, 1), CERTO)
    E.frase(c, t, C["s14"], [("cuidado", "g", 84, ERRADO)], XE, 220)
    E.frase(c, t, C["s14.a"], [("comparar", "i", 58), ("com", "i", 58), ("o", "i", 58), ("raio", "g", 58, ERRADO)], XE, 340)
    E.frase(c, t, C["s14.a"] + 1.4, [("e", "i", 58), ("não", "i", 58), ("com", "i", 58), ("r²", "g", 58, DIST)], XE + 470, 340)
    par_em(c, t, C["s14.b"], "4", "1", XE, 480, 56)
    conta_em(c, t, C["s14.b"] + 0.4, [("2^2 + 2^2 = 8", TINTA)], XE + 220, 480, 60)
    conta_em(c, t, C["s14.c"], [("8 > 3:  fora?", ERRADO)], XE, 620, 66)
    if t >= C["s14.d"]:
        E.risco(c, XE - 10, 645, XE + 470, 570, t, C["s14.d"], largura=9)
    E.frase(c, t, C["s14.d"], [("8", "g", 60), ("é", "i", 60), ("a", "i", 60), ("distância", "i", 60), ("ao", "i", 60), ("quadrado", "g", 60)], XE, 760)
    conta_em(c, t, C["s14.e"], [("8 < 9:  dentro", CERTO)], XE, 900, 72)


# ---------------- atalho (palco escuro) ----------------
PA = E.Plano(1180, 200, 560, 560, -7, 7, -7, 7, escuro=True)


def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15.a"], [("reta", "i", 64, CLARO), ("deitada", "g", 64, BR), ("ou", "i", 64, CLARO), ("em", "i", 64, CLARO), ("pé", "g", 64, BR)], XE, 260)
        E.frase(c, t, C["s15.b"], ps("a distância se lê no plano", "i", 58, CLARO), XE, 380, passo=0.1)
        E.plano(c, t, C["s15.b"], *PA.caixa, -7, 7, -7, 7, marcas_x=[-5, 5], marcas_y=[-5, 5], size=30, escuro=True)
        if t >= C["s15.b"] + 0.3:
            X, Y = PA(0, 0)
            R = PA.x(5) - X
            c.drawArc(skia.Rect.MakeXYWH(X - R, Y - R, 2 * R, 2 * R), 0, -360 * ease_io(prog(t, C["s15.b"] + 0.3, 0.9)), False,
                      M.paint(DX_ESC, 1, stroke=6, cap_round=True))
        if t >= C["s15.c"]:
            E.reta_pontos(c, t, C["s15.c"], PA, (0, 5), (1, 5), cor=BR, pontos=False, largura=6)
            anda(c, t, C["s15.c"] + 0.6, PA, (0, 0), (0, 5), DY_ESC, 0.8, 8)
            E.foco(c, t, C["s15.c"] + 1.2, 0.4, lambda a: E._cola(c, "5", *PA(0, 2.5), 1, 0, 18, 56, "g", DY_ESC, a))
        E.frase(c, t, C["s15.c"], [("da", "i", 58, CLARO), ("origem", "i", 58, CLARO), ("até", "i", 58, CLARO), ("y = 5:", "g", 58, BR), ("5", "g", 58, DY_ESC),
                                   ("passos", "i", 58, CLARO)], XE, 540, passo=0.1)
        E.frase(c, t, C["s15.d"], [("5", "g", 66, DY_ESC), ("=", "i", 66, CLARO), ("raio", "g", 66, BR)], XE, 700)
        E.foco(c, t, C["s15.d"] + 1.0, 0.4, lambda a: E.pilula(c, "tangente", XE + 210, 810, 60, "g", fundo=COR, a=a))
        E.frase(c, t, C["s15.d"] + 1.6, ps("sem conta nenhuma", "i", 54, CLARO), XE, 930, passo=0.1)
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], [("por", "i", 64, CLARO), ("que", "i", 64, CLARO), ("funciona", "g", 64, BR)], W / 2, 170, "center")
    E.frase(c, t, C["s16.a"], [("deitada:", "g", 56, BR), ("diferença", "i", 56, CLARO), ("dos", "i", 56, CLARO), ("y", "g", 56, DY_ESC)], W / 2, 290, "center")
    E.frase(c, t, C["s16.a"] + 3.4, [("em", "i", 56, CLARO), ("pé:", "g", 56, BR), ("diferença", "i", 56, CLARO), ("dos", "i", 56, CLARO), ("x", "g", 56, DX_ESC)],
            W / 2, 370, "center")
    for i, (s_, pos) in enumerate((("d = r", "tangente"), ("d < r", "secante"), ("d > r", "externa"))):
        x = W / 2 + (i - 1) * 470
        E.foco(c, t, C["s16.b"] + 2.0 + i * 0.8, 0.5, lambda a, x=x, s_=s_, pos=pos: (E.formula(c, s_, x, 540, 66, "g", BR, a, "center"),
                                                                                     E.pilula(c, pos, x, 610, 42, "g", fundo=COR, a=a)))
    E.frase(c, t, C["s16.c"], [("não", "g", 60, ERRADO), ("compensa:", "i", 60, CLARO), ("reta", "i", 60, CLARO), ("inclinada", "g", 60, BR)], W / 2, 780, "center")
    E.foco(c, t, C["s16.c"] + 1.4, 0.4, lambda a: E.formula(c, "y = x + 1", W / 2, 860, 54, "g", CLARO, a, "center"))
    E.frase(c, t, C["s16.d"], [("substituição", "g", 60, BR), ("e", "i", 60, CLARO), ("delta", "g", 60, BR)], W / 2, 970, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    conta_em(c, t, C["s17.a"], [("x^2 + y^2 = 10", TINTA)], XE, 340, 84)
    x, w = 230, 1460
    for i, (k, y) in enumerate((("s17.b", 430), ("s17.c", 650))):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 180, p, prog_=p)
        E.foco(c, t, C[k], 0.5, lambda a, y=y, i=i: (E.bola(c, x + 80, y + 90, 46, a=a), centro(c, str(i + 1), x + 80, y + 110, 54, "g", BR, a)))
    E.frase(c, t, C["s17.b"], [("ponto", "i", 60)], x + 170, 510)
    par_em(c, t, C["s17.b"] + 0.4, "3", "2", x + 360, 510, 60)
    E.frase(c, t, C["s17.b"] + 1.0, [("dentro,", "g", 54, COR), ("fora", "g", 54, COR), ("ou", "i", 54), ("em", "i", 54), ("cima?", "g", 54, COR)], x + 170, 585)
    E.frase(c, t, C["s17.c"], [("reta", "i", 60), ("y = 10 − 3x", "g", 60)], x + 170, 730)
    E.frase(c, t, C["s17.c"] + 1.4, [("secante,", "g", 54, COR), ("tangente", "g", 54, COR), ("ou", "i", 54), ("externa?", "g", 54, COR)], x + 170, 805)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1450, cy=210, r=50)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    eixos(c, t, C["s19"] - 3, PQ, [-4, -2, 2, 4], [-4, -2, 2, 4], size=30)
    circ(c, t, C["s19"] - 3, PQ, 0, 0, math.sqrt(10))
    centro_c(c, t, C["s19"] - 3, PQ, 0, 0, lado=(-1, 1))
    nome(c, t, C["s19.a"] - 0.4, PQ, 3, 2, None)
    E.foco(c, t, C["s19.b"] + 0.4, 0.4, lambda a: E._cola(c, "fora", *PQ(3, 2), 1, -0.6, 22, 40, "g", TINTA, a))
    reta_y(c, t, C["s19.c"], PQ, -3, 10)
    if t >= C["s21.b"]:
        achado(c, t, C["s21.b"] + 0.6, PQ, 3, 1, "(3, 1)", lado=(1, -0.2), size=40)

    def s19():
        conta_em(c, t, C["s19"], [("x^2 + y^2 = 10", TINTA)], XE, 220, 62)
        par_em(c, t, C["s19.a"] - 0.4, "3", "2", XE, 360, 58)
        conta_em(c, t, C["s19.a"], [("3^2 + 2^2 = 9 + 4 = 13", TINTA)], XE + 230, 360, 58)
        conta_em(c, t, C["s19.b"], [("13 > 10:  fora", COR)], XE, 480, 64)
        conta_em(c, t, C["s19.c"], [("x^2 + ", TINTA), ("(10 − 3x)^2", COR), (" = 10", TINTA)], XE, 660, 68)
    E.saida(c, t, C["s20"] - 0.1, s19)

    def s20():
        conta_em(c, t, C["s20"], [("x^2 + ", TINTA), ("(10 − 3x)^2", COR), (" = 10", TINTA)], XE, 240, 62)
        conta_em(c, t, C["s20.a"], [("(10 − 3x)^2", COR), (" = 100 − 60x + 9x^2", TINTA)], XE, 380, 56)
        E.frase(c, t, C["s20.b"] - 1.4, ps("junte e − 10", "i", 46, TINTA2), XE + 40, 470, passo=0.08)
        conta_em(c, t, C["s20.b"], [("10x^2 − 60x + 90 = 0", TINTA)], XE, 570, 66)
        E.frase(c, t, C["s20.c"] - 1.2, ps("÷ 10", "i", 46, TINTA2), XE + 40, 660, passo=0.08)
        eqn(c, t, C["s20.c"], [("x^2 − 6x + 9 = 0", TINTA)], XE, 780, 76, caixa=C["s20.c"] + 1.0)
    E.saida(c, t, C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    conta_em(c, t, C["s21"], [("x^2 − 6x + 9 = 0", TINTA)], XE, 220, 62)
    conta_em(c, t, C["s21.a"], [("Δ = 36 − 36 = ", TINTA), ("0", COR)], XE, 360, 70)
    posicao(c, t, C["s21.b"], "tangente", XE + 170, 470, 60)
    E.frase(c, t, C["s21.c"], [("encosta", "i", 58), ("em", "i", 58)], XE, 620)
    par_em(c, t, C["s21.c"] + 0.4, "3", "1", XE + 300, 620, 58)
    conta_em(c, t, C["s21.d"], [("3^2 + 1^2 = 9 + 1 = 10", TINTA)], XE, 760, 64)
    ok(c, t, C["s21.d"] + 1.2, XE + 700, 735)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s22.a", [("ponto:", "g", 80, COR), ("compare", "i", 80), ("com", "i", 80), ("r²", "g", 80, DIST)]),
                 ("s22.b", [("reta:", "g", 80, COR), ("substitua", "i", 80), ("e", "i", 80), ("olhe", "i", 80), ("o", "i", 80), ("sinal", "i", 80),
                            ("do", "i", 80), ("Δ", "g", 80, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 460 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.1)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s23.a"], [("Praticando", "g", 130, COR)], XE, 430)
    E.frase(c, t, C["s23.b"], [("centro", "g", 70), ("e", "i", 70), ("raio", "g", 70, DIST)], XE, 580)
    E.frase(c, t, C["s23.c"], [("pontos", "g", 70), ("e", "i", 70), ("retas", "g", 70), ("em", "i", 70), ("situações", "i", 70), ("novas", "i", 70)], XE, 700)
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 300, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(600, 325, p), ep(t, C["s23.d"] + 0.2, 0.4))
    E.frase(c, t, C["s23.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ponto=b_ponto, reta=b_reta, outras=b_outras, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
