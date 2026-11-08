"""Visual — Estudativo · MAT-ANA-011: praticando a circunferência no plano (fecha a Geometria Analítica e a Matemática do núcleo).

Segue a linguagem da Geometria Analítica (MAT-ANA-001) e a da circunferência (MAT-ANA-008 a 010, leia os cabeçalhos de lá):
- a circunferência e o raio em índigo (DIST), o centro como ponto preto "C"; do centro até um ponto, o cateto deitado em petróleo
  (DX) e o em pé em âmbar (DY), e a distância tracejada em índigo; na equação, (x − a)² petróleo, (y − b)² âmbar, r² índigo;
- as retas testadas em preto; o ponto de encontro é achado (índigo, com anel); a posição numa pílula preta;
- cada situação com título, plano à direita e relógio de pausa; erro em vermelho, certo em verde, atalho no palco escuro.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Analítica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANA-011_praticando_circunferencia_no_plano.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "atalho", "questao3", "questao4", "fim"))
BR = "#FFFFFF"
ENT, SAI = COR, TINTA                       # x / y, como em Funções
DX, DY, DIST = "#0E9AA7", "#D98A00", E.COR  # cateto deitado, cateto em pé, raio / circunferência
DX_ESC, DY_ESC = "#3CC7D3", "#FFB833"
# as contas do roteiro
assert math.isqrt(49) == 7 and (0 - 4) ** 2 + (0 + 3) ** 2 == 16 + 9 == 25 < 49
assert 5 - 2 == 3 and 5 - 1 == 4 and 3 ** 2 + 4 ** 2 == 25 and math.isqrt(25) == 5
assert all(x * x + y * y - 2 * x - 6 * y + 6 == (x - 1) ** 2 + (y - 3) ** 2 - 4 for x, y in ((0, 0), (2, 5))) and -6 + 1 + 9 == 4
assert (1 - 3) ** 2 == 4 and 3 - 1 == 2
assert all(2 * x * x + 8 * x + 11 == x * x + (x + 4) ** 2 - 5 for x in (0, 1)) and 8 ** 2 == 64 and 4 * 2 * 11 == 88 and 64 - 88 == -24


def plano_igual(xmin, xmax, ymin, ymax, lado=740, cx=1430, cy=545):
    """Plano com a mesma escala nos dois eixos (a circunferência sai redonda), centrado em (cx, cy)"""
    u = lado / max(xmax - xmin, ymax - ymin)
    w, h = (xmax - xmin) * u, (ymax - ymin) * u
    return E.Plano(cx - w / 2, cy - h / 2, w, h, xmin, xmax, ymin, ymax)


P1 = plano_igual(-4, 12, -11, 5)    # (x − 4)² + (y + 3)² = 49 e a origem
P2 = plano_igual(-4, 8, -5, 7)      # centro (2, 1) passando por (5, 5)
P3 = plano_igual(-3, 5, -1, 7)      # centro (1, 3), raio 2, reta y = 1
P4 = plano_igual(-6, 3, -3, 6)      # x² + y² = 5 e y = x + 4


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("4", "g", 220, COR)], XE, 420)
    E.frase(c, t, C["s01.a"] + 0.3, [("situações", "i", 110)], XE + 170, 400)
    E.frase(c, t, C["s01.a"] + 0.9, [("circunferência", "g", 86, COR)], XE, 550)
    E.frase(c, t, C["s01.a"] + 1.4, [("no", "i", 80), ("plano", "g", 80)], XE, 650)
    for i in range(4):
        cx, cy = 1260 + (i % 2) * 300, 300 + (i // 2) * 300
        t0 = C["s01.a"] + 0.4 + i * 0.25
        E.foco(c, t, t0, 0.5, lambda a, cx=cx, cy=cy, i=i, t0=t0: (
            c.drawCircle(cx, cy, 110 * ease_back(prog(t, t0, 0.5)), M.paint(DIST, a, stroke=10)),
            centro(c, str(i + 1), cx, cy + 44, 120, "g", DIST, a)), blur=0)
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
    E.frase(c, t, C["s02.b"] + 0.1, [("centro:", "g", 56), ("o", "i", 56), ("que", "i", 56), ("zera", "g", 56, COR), ("os", "i", 56), ("parênteses;", "i", 56),
                                     ("raio:", "g", 56, DIST), ("a", "i", 56), ("raiz", "g", 56)], x + 170, yb(0), passo=0.1)
    E.frase(c, t, C["s02.c"] + 0.1, [("completar", "g", 60, COR), ("quadrados", "g", 60, COR)], x + 170, yb(1))
    E.frase(c, t, C["s02.d"] + 0.1, [("ponto:", "g", 60), ("compare", "i", 60), ("com", "i", 60), ("r²", "g", 60, DIST)], x + 170, yb(2))
    E.frase(c, t, C["s02.e"] + 0.1, [("reta:", "g", 60), ("substitua", "i", 60), ("e", "i", 60), ("olhe", "i", 60), ("o", "i", 60), ("Δ", "g", 60, COR)],
            x + 170, yb(3))
    E.frase(c, t, C["s03"] - 2.6, ps("travou? procure a aula no canal", "i", 48, TINTA2), W / 2, 1000, "center", passo=0.1)


# ---------------- situação 1 ----------------
def base1(c, t, t0, tc):
    eixos(c, t, t0, P1, [-3, 4, 8], [-10, -3, 4], size=30)
    circ(c, t, tc, P1, 4, -3, 7)
    centro_c(c, t, tc, P1, 4, -3, lado=(1, 1))


def b_questao1(c, t, C, b):
    eixos(c, t, C["s03"] + 0.2, P1, [-3, 4, 8], [-10, -3, 4], size=30)
    E.ponto(c, t, C["s03.d"] + 0.3, P1, 0, 0, None, cor=TINTA, r=14)
    E.foco(c, t, C["s03.d"] + 0.6, 0.4, lambda a: E.pilula(c, "?", P1.x(0) - 60, P1.y(0) - 50, 44, "g", fundo=TINTA, a=a))
    titulo(c, t, C["s03.a"], 1)
    conta_em(c, t, C["s03.b"], red("(x − 4)^2", "(y + 3)^2", "49", TINTA, TINTA, TINTA), XE, 360, 72)
    E.frase(c, t, C["s03.c"], [("centro?", "g", 66, COR), ("raio?", "g", 66, COR)], XE, 500)
    E.frase(c, t, C["s03.d"], [("a", "i", 62), ("origem:", "g", 62)], XE, 640)
    E.frase(c, t, C["s03.d"] + 0.8, [("dentro,", "g", 56, COR), ("fora", "g", 56, COR), ("ou", "i", 56), ("em", "i", 56), ("cima?", "g", 56, COR)], XE, 730)
    pausa(c, t, C["s04.a"], cx=560, cy=860, r=62)


def b_resposta1(c, t, C, b):
    eixos(c, t, C["s05"] - 3, P1, [-3, 4, 8], [-10, -3, 4], size=30)
    E.ponto(c, t, C["s05"] - 3, P1, 0, 0, None, cor=TINTA, r=14)
    centro_c(c, t, C["s05.c"], P1, 4, -3, lado=(1, 1))
    circ(c, t, C["s05.d"] + 0.4, P1, 4, -3, 7)
    if t >= C["s05.d"] + 1.0:
        seg(c, t, C["s05.d"] + 1.0, P1, (4, -3), (11, -3), DIST, 0.6, 7)
        lado_txt(c, t, C["s05.d"] + 1.4, P1, (4, -3), (11, -3), "7", (7, -5), DIST, 46)
    if t >= C["s06.b"]:
        ate_centro(c, t, C["s06.b"], P1, (4, -3), (0, 0), "4", "3")
    if t >= C["s06.e"]:
        anel(c, t, C["s06.e"] + 0.4, *P1(0, 0), CERTO)
        anel(c, t, C["s06.e"] + 0.9, *P1(0, 0), CERTO)
        E.foco(c, t, C["s06.e"] + 0.6, 0.4, lambda a: E._cola(c, "dentro", *P1(0, 0), 1, -1, 22, 40, "g", TINTA, a))

    def s05():
        eqn(c, t, C["s05"], red("(x − 4)^2", "(y + 3)^2", "49"), XE, 220, 64)
        conta_em(c, t, C["s05.a"], [("x − 4", DX), (" zera com ", TINTA2), ("4", ENT)], XE, 370, 60)
        conta_em(c, t, C["s05.b"], [("y + 3", DY), (" zera com ", TINTA2), ("−3", SAI)], XE, 480, 60)
        E.frase(c, t, C["s05.c"], [("centro", "i", 60)], XE, 620)
        par_em(c, t, C["s05.c"] + 0.4, "4", "−3", XE + 230, 620, 62)
        conta_em(c, t, C["s05.d"], [("r = r{49} = ", TINTA), ("7", DIST)], XE, 760, 68)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], [("centro", "i", 52, TINTA2)], XE, 210)
    E.foco(c, t, C["s06"], 0.5, lambda a: par(c, "4", "−3", XE + 200, 210, 52, a))
    E.frase(c, t, C["s06"] + 0.4, [("raio", "i", 52, TINTA2), ("7", "g", 52, DIST)], XE + 470, 210)
    E.frase(c, t, C["s06.a"], [("a", "i", 58), ("origem", "i", 58)], XE, 330)
    par_em(c, t, C["s06.a"] + 0.4, "0", "0", XE + 270, 330, 58)
    conta_em(c, t, C["s06.b"], [("(0 − 4)^2 = (−4)^2 = ", TINTA), ("16", DX)], XE, 460, 58)
    conta_em(c, t, C["s06.c"], [("(0 + 3)^2 = 3^2 = ", TINTA), ("9", DY)], XE, 570, 58)
    conta_em(c, t, C["s06.d"], [("16", DX), (" + ", TINTA), ("9", DY), (" = 25", TINTA)], XE, 700, 66)
    conta_em(c, t, C["s06.e"], [("25 < 49", CERTO)], XE, 840, 72)
    posicao(c, t, C["s06.e"] + 0.8, "dentro", XE + 480, 815, 54)


# ---------------- situação 2 ----------------
def b_questao2(c, t, C, b):
    eixos(c, t, C["s07"] + 0.2, P2, [-2, 2, 5], [-4, 1, 5], size=30)
    centro_c(c, t, C["s07.b"] + 0.3, P2, 2, 1)
    nome(c, t, C["s07.c"] + 0.3, P2, 5, 5, "P", lado=(1, -1))
    titulo(c, t, C["s07.a"], 2)
    E.frase(c, t, C["s07.b"], [("centro", "i", 62)], XE, 360)
    par_em(c, t, C["s07.b"] + 0.4, "2", "1", XE + 240, 360, 62)
    E.frase(c, t, C["s07.c"], [("passa", "i", 62), ("por", "i", 62), ("P", "g", 62)], XE, 480)
    par_em(c, t, C["s07.c"] + 0.6, "5", "5", XE + 340, 480, 62)
    E.frase(c, t, C["s07.d"], [("a", "i", 62), ("equação", "g", 62, COR), ("reduzida?", "g", 62, COR)], XE, 630)
    pausa(c, t, C["s08.a"], cx=560, cy=840, r=62)


def b_resposta2(c, t, C, b):
    t0 = C["s09"] - 3
    eixos(c, t, t0, P2, [-2, 2, 5], [-4, 1, 5], size=30)
    centro_c(c, t, t0, P2, 2, 1)
    nome(c, t, t0, P2, 5, 5, "P", lado=(1, -1))
    cateto(c, t, C["s09.b"], P2, (2, 1), (5, 1), DX, 0.5, 9)
    lado_txt(c, t, C["s09.b"] + 0.4, P2, (2, 1), (5, 1), "3", (4, 2.3), DX, 46)
    cateto(c, t, C["s09.c"], P2, (5, 1), (5, 5), DY, 0.5, 9)
    lado_txt(c, t, C["s09.c"] + 0.4, P2, (5, 1), (5, 5), "4", (4, 2.3), DY, 46)
    cateto(c, t, C["s09.e"], P2, (2, 1), (5, 5), DIST, 0.6, 8)
    circ(c, t, C["s10.a"] + 0.4, P2, 2, 1, 5)
    lado_txt(c, t, C["s10.b"], P2, (2, 1), (5, 5), "5", (4, 2.3), DIST, 50)

    def s09():
        E.frase(c, t, C["s09.a"], [("raio", "g", 60, DIST), ("=", "i", 60), ("distância", "i", 60), ("do", "i", 60), ("centro", "i", 60), ("até", "i", 60),
                                   ("P", "g", 60)], XE, 240, passo=0.1)
        conta_em(c, t, C["s09.b"], [("x:  5 − 2 = ", TINTA), ("3", DX)], XE, 380, 62)
        conta_em(c, t, C["s09.c"], [("y:  5 − 1 = ", TINTA), ("4", DY)], XE, 490, 62)
        conta_em(c, t, C["s09.d"], [("3", DX), ("^2 + ", TINTA), ("4", DY), ("^2 = ", TINTA), ("25", DIST)], XE, 640, 72)
        E.frase(c, t, C["s09.e"], [("=", "i", 64), ("r²", "g", 64, DIST)], XE + 470, 640)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    eqn(c, t, C["s10.a"], red("(x − 2)^2", "(y − 1)^2", "25"), XE, 300, 70, caixa=C["s10.a"] + 1.2)
    E.frase(c, t, C["s10.b"], [("raio", "i", 60), ("5,", "g", 60, DIST), ("mas", "i", 60), ("nem", "i", 60), ("precisava", "i", 60)], XE, 480)
    E.frase(c, t, C["s10.c"], [("a", "i", 60), ("equação", "i", 60), ("pede", "i", 60), ("r²", "g", 60, DIST), ("=", "i", 60), ("25", "g", 60, DIST)], XE, 600)
    E.frase(c, t, C["s10.c"] + 1.6, ps("já estava pronto", "i", 54, TINTA2), XE, 700, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s11"], [("atalho", "g", 66, BR), ("de", "i", 66, CLARO), ("prova", "i", 66, CLARO)], W / 2, 170, "center")
    E.frase(c, t, C["s11.a"], [("raio", "i", 62, CLARO), ("por", "i", 62, CLARO), ("uma", "i", 62, CLARO), ("distância:", "i", 62, CLARO), ("pare", "g", 62, BR),
                               ("antes", "g", 62, BR), ("da", "i", 62, CLARO), ("raiz", "g", 62, BR)], W / 2, 300, "center", passo=0.1)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: conta(c, [("3^2", DX_ESC), (" + ", BR), ("4^2", DY_ESC), (" = 25", BR)], W / 2, 450, 84, a, "center"))
    E.frase(c, t, C["s11.b"] + 1.4, ps("Pitágoras dá a distância ao quadrado", "i", 52, CLARO), W / 2, 540, "center", passo=0.08)
    E.foco(c, t, C["s11.b"] + 3.4, 0.5, lambda a: (E.caixa_pontilhada(c, W / 2 - 420, 580, 840, 120, a, BR),
                                                  E.formula(c, "… = 25", W / 2, 668, 72, "g", BR, a, "center")))
    E.frase(c, t, C["s11.c"], [("não", "g", 58, ERRADO), ("compensa:", "i", 58, CLARO), ("pergunta", "i", 58, CLARO), ("o", "i", 58, CLARO), ("raio", "g", 58, BR),
                               ("ou", "i", 58, CLARO), ("a", "i", 58, CLARO), ("volta", "g", 58, BR)], W / 2, 820, "center", passo=0.1)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.pilula(c, "tire a raiz: r = 5", W / 2, 930, 56, "g", fundo=COR, a=a))


# ---------------- situação 3 ----------------
EQ3 = [("x^2 + y^2 − 2x − 6y + 6 = 0", TINTA)]


def b_questao3(c, t, C, b):
    titulo(c, t, C["s12.a"], 3)
    conta_em(c, t, C["s12.b"], EQ3, XE, 360, 76)
    E.frase(c, t, C["s12.c"], [("centro?", "g", 66, COR), ("raio?", "g", 66, COR)], XE, 500)
    E.frase(c, t, C["s12.d"], [("a", "i", 62), ("reta", "i", 62), ("y = 1:", "g", 62)], XE, 640)
    E.frase(c, t, C["s12.d"] + 1.2, [("secante,", "g", 56, COR), ("tangente", "g", 56, COR), ("ou", "i", 56), ("externa?", "g", 56, COR)], XE, 730)
    pausa(c, t, C["s13.a"], cx=1450, cy=600, r=80)


def b_resposta3(c, t, C, b):
    def s14():
        conta_em(c, t, C["s14"], EQ3, XE, 210, 60)
        conta_em(c, t, C["s14.a"], [("x^2 − 2x", DX), (" + ", TINTA), ("y^2 − 6y", DY), (" = ", TINTA), ("−6", DIST)], XE, 330, 64)
        conta_em(c, t, C["s14.b"], [("x:  ", TINTA2), ("−2 ÷ 2 = −1", DX), ("     ", TINTA), ("(−1)^2 = 1", DX)], XE, 460, 58)
        conta_em(c, t, C["s14.c"], [("y:  ", TINTA2), ("−6 ÷ 2 = −3", DY), ("     ", TINTA), ("(−3)^2 = 9", DY)], XE, 570, 58)
        conta_em(c, t, C["s14.d"], [("−6", DIST), (" + ", TINTA), ("1", DX), (" + ", TINTA), ("9", DY), (" = ", TINTA), ("4", DIST)], XE, 720, 72)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    eixos(c, t, C["s15"], P3, [-2, 1, 3], [1, 3, 5], size=30)
    centro_c(c, t, C["s15.b"] + 0.3, P3, 1, 3, lado=(-1, -1))
    circ(c, t, C["s15.c"] + 0.3, P3, 1, 3, 2)

    def s15():
        eqn(c, t, C["s15.a"], red("(x − 1)^2", "(y − 3)^2", "4"), XE, 230, 66, caixa=C["s15.a"] + 1.0)
        E.frase(c, t, C["s15.b"], [("centro", "i", 58)], XE, 360)
        par_em(c, t, C["s15.b"] + 0.4, "1", "3", XE + 220, 360, 58)
        E.frase(c, t, C["s15.c"], [("raio", "i", 58), ("2", "g", 58, DIST)], XE + 500, 360)
        E.frase(c, t, C["s15.d"], [("esqueceu", "i", 56), ("a", "i", 56), ("direita:", "i", 56)], XE, 520)
        conta_em(c, t, C["s15.d"] + 0.8, [("r^2 = −6", ERRADO)], XE + 500, 520, 62)
        E.frase(c, t, C["s15.e"], [("impossível:", "g", 56, ERRADO), ("a", "i", 56), ("conta", "i", 56), ("escorregou", "i", 56)], XE, 640)
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    reta_y(c, t, C["s16.a"], P3, 0, 1)
    E.foco(c, t, C["s16.a"] + 0.6, 0.4, lambda a: E.pilula(c, "y = 1", *P3(4.0, 0.4), 38, "g", fundo=TINTA, a=a))
    anda(c, t, C["s16.b"] + 0.3, P3, (1, 3), (1, 1), DY, 0.7, 8)
    E.foco(c, t, C["s16.b"] + 1.0, 0.4, lambda a: E._cola(c, "2", *P3(1, 2), -1, 0, 18, 50, "g", DY, a))
    achado(c, t, C["s16.f"] + 0.6, P3, 1, 1, "(1, 1)", lado=(1, 1), size=40)
    eqn(c, t, C["s16"], red("(x − 1)^2", "(y − 3)^2", "4"), XE, 220, 58)
    E.frase(c, t, C["s16.a"], [("reta", "i", 58), ("deitada:", "g", 58), ("y = 1", "g", 58)], XE, 330)
    conta_em(c, t, C["s16.b"], [("3 − 1 = ", TINTA), ("2", DY)], XE, 440, 62)
    E.frase(c, t, C["s16.b"] + 1.2, ps("passos", "i", 54, TINTA2), XE + 330, 440)
    conta_em(c, t, C["s16.c"], [("2 = raio", DIST)], XE, 550, 62)
    posicao(c, t, C["s16.c"] + 0.6, "tangente", XE + 520, 525, 50)
    conta_em(c, t, C["s16.d"], [("(1 − 3)^2 = 4", TINTA)], XE, 690, 60)
    conta_em(c, t, C["s16.e"], [("(x − 1)^2 = 0", TINTA)], XE, 800, 66)
    E.frase(c, t, C["s16.f"], [("só", "i", 56), ("o", "i", 56), ("1:", "g", 56), ("uma", "i", 56), ("raiz", "i", 56)], XE, 920)
    E.foco(c, t, C["s16.f"] + 1.4, 0.5, lambda a: par(c, "1", "1", XE + 480, 920, 56, a))


# ---------------- situação 4 ----------------
def base4(c, t, t0, tc, tr):
    eixos(c, t, t0, P4, [-4, -2, 2], [-2, 2, 4], size=30)
    circ(c, t, tc, P4, 0, 0, math.sqrt(5))
    centro_c(c, t, tc, P4, 0, 0, lado=(1, 1))
    reta_y(c, t, tr, P4, 1, 4)
    E.foco(c, t, tr + 0.6, 0.4, lambda a: E.pilula(c, "y = x + 4", *P4(-4.4, 1.0), 38, "g", fundo=TINTA, a=a))


def b_questao4(c, t, C, b):
    base4(c, t, C["s17"] + 0.2, C["s17.b"] + 0.3, C["s17.c"] + 0.3)
    E.frase(c, t, C["s17.a"], [("última", "i", 74), ("situação", "g", 74, COR)], XE, 200)
    conta_em(c, t, C["s17.b"], [("x^2 + y^2 = 5", TINTA)], XE, 360, 76)
    E.frase(c, t, C["s17.c"], [("reta", "i", 62), ("y = x + 4", "g", 62)], XE, 490)
    E.frase(c, t, C["s17.d"], [("secante,", "g", 56, COR), ("tangente", "g", 56, COR), ("ou", "i", 56), ("externa?", "g", 56, COR)], XE, 620)
    pausa(c, t, C["s18.a"], cx=560, cy=840, r=62)


def b_resposta4(c, t, C, b):
    t0 = C["s19"] - 3
    base4(c, t, t0, t0, t0)

    def s19():
        E.frase(c, t, C["s19.a"], [("inclinada:", "g", 60), ("substituição", "i", 60), ("e", "i", 60), ("Δ", "g", 60, COR)], XE, 230)
        conta_em(c, t, C["s19.b"], [("x^2 + ", TINTA), ("(x + 4)^2", COR), (" = 5", TINTA)], XE, 380, 70)
        conta_em(c, t, C["s19.c"], [("(x + 4)^2", COR), (" = x^2 + 8x + 16", TINTA)], XE + 40, 500, 56)
        E.frase(c, t, C["s19.d"] - 1.6, ps("junte e − 5", "i", 46, TINTA2), XE + 40, 600, passo=0.08)
        eqn(c, t, C["s19.d"], [("2x^2 + 8x + 11 = 0", TINTA)], XE, 740, 78, caixa=C["s19.d"] + 1.0)
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    conta_em(c, t, C["s20"], [("2x^2 + 8x + 11 = 0", TINTA)], XE, 220, 62)
    conta_em(c, t, C["s20.a"], [("b^2 = 8^2 = 64", TINTA)], XE, 350, 62)
    conta_em(c, t, C["s20.b"], [("4 · 2 · 11 = 88", TINTA)], XE, 460, 62)
    conta_em(c, t, C["s20.c"], [("Δ = 64 − 88 = ", TINTA), ("−24", COR)], XE, 590, 70)
    E.frase(c, t, C["s20.d"], [("Δ", "g", 60, COR), ("<", "g", 60), ("0:", "g", 60), ("nenhum", "i", 60), ("ponto", "i", 60)], XE, 720)
    posicao(c, t, C["s20.e"], "externa", XE + 160, 840, 60)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s21.a", [("monte", "i", 80), ("a", "i", 80), ("equação", "g", 80), ("reduzida", "g", 80, COR)]),
                 ("s21.b", [("leia", "i", 80), ("o", "i", 80), ("centro", "g", 80), ("e", "i", 80), ("o", "i", 80), ("raio", "g", 80, DIST)]),
                 ("s21.c", [("ponto:", "g", 70), ("r²;", "g", 70, DIST), ("reta:", "g", 70), ("o", "i", 70), ("delta", "g", 70, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22.a"], [("você", "i", 70), ("fecha", "i", 70), ("a", "i", 70), ("Matemática", "g", 76, COR), ("do", "i", 70), ("curso", "i", 70)], XE, 260)
    # a trilha: dos algarismos à circunferência
    q = ease_io(prog(t, C["s22.b"], 1.4))
    if q > 0:
        M.line(c, 300, 470, lerp(300, 1620, q), 470, COR, 1.0, 10)
    E.foco(c, t, C["s22.b"], 0.5, lambda a: (E.formula(c, "0, 1, 2, …, 9", 300, 420, 64, "g", TINTA, a),
                                            E.escreve(c, "algarismos", 300, 540, 52, "i", TINTA2, a)))
    E.foco(c, t, C["s22.b"] + 1.4, 0.5, lambda a: (c.drawCircle(1620, 470, 64, M.paint(DIST, a, stroke=10)), c.drawCircle(1620, 470, 10, M.paint(TINTA, a)),
                                                  E.escreve(c, "circunferência", 1400, 600, 52, "i", TINTA2, a)))
    E.frase(c, t, C["s22.c"], ps("travou? procure a aula e refaça", "i", 56, TINTA2), XE, 720, passo=0.1)
    E.foco(c, t, C["s22.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 820, 70, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(1020, 845, p), ep(t, C["s22.d"] + 0.2, 0.4))
    E.frase(c, t, C["s22.e"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], XE, 950)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              atalho=b_atalho, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
