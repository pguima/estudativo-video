"""Visual — Estudativo · MAT-ANA-008: equação reduzida da circunferência, (x − a)² + (y − b)² = r².

Segue a linguagem da Geometria Analítica definida em MAT-ANA-001 (leia o cabeçalho de lá) e a das cores da Trigonometria:
- plano à direita, texto à esquerda; eixo x e valores de x em índigo, y em preto; par() com x índigo e y preto;
- A CIRCUNFERÊNCIA É PITÁGORAS: do centro até um ponto dela, o cateto deitado (x − a) é petróleo (DX), o cateto em pé (y − b)
  é âmbar (DY) e o raio, que é a hipotenusa, é índigo (DIST), como a distância em MAT-ANA-001. A circunferência também é índigo.
- na equação, as mesmas cores: (x − a)² em petróleo, (y − b)² em âmbar, r² e o raio em índigo. O centro é um ponto preto "C".
- erro em vermelho, certo em verde, atalho no palco escuro, resposta na esfera; a forma final ganha caixa pontilhada.
Peças novas desta aula: plano_igual() (plano com a mesma escala nos dois eixos, centrado na metade direita), circ() (a
circunferência no plano, que se fecha a partir da direita), centro_c() (o centro com o nome C), eqc() (a equação reduzida colorida).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Analítica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANA-008_equacao_reduzida_da_circunferencia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("origem", "centro", "regra", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ENT, SAI = COR, TINTA                       # x / y, como em Funções
DX, DY, DIST = "#0E9AA7", "#D98A00", E.COR  # cateto deitado, cateto em pé, raio (hipotenusa)
DX_ESC, DY_ESC = "#3CC7D3", "#FFB833"
# as contas do roteiro
assert 3 ** 2 + 4 ** 2 == 25 == 5 ** 2 and (-3) ** 2 == 9
assert (5 - 2) ** 2 + (-1 + 1) ** 2 == 9 == 3 ** 2 and math.isqrt(9) == 3
assert 5 ** 2 == 25 and (11 - 2) ** 2 == 81 != 9
assert math.isqrt(16) == 4 and 6 ** 2 == 36
assert all(abs((x - 2) ** 2 + (y + 1) ** 2 - 9 - (x * x + y * y - 4 * x + 2 * y - 4)) < 1e-9 for x, y in ((0, 0), (1, 3), (-2, 5)))


def plano_igual(xmin, xmax, ymin, ymax, lado=740, cx=1430, cy=545):
    """Plano com a mesma escala nos dois eixos (a circunferência sai redonda), centrado em (cx, cy)"""
    u = lado / max(xmax - xmin, ymax - ymin)
    w, h = (xmax - xmin) * u, (ymax - ymin) * u
    return E.Plano(cx - w / 2, cy - h / 2, w, h, xmin, xmax, ymin, ymax)


PO = plano_igual(-6, 6, -6, 6)      # centro na origem, raio 5
PC = plano_igual(-2, 6, -5, 3)      # centro (2, −1), raio 3
PW = plano_igual(-9, 3, -2, 10)     # centro (−3, 4), raio 5
P12 = plano_igual(-3, 5, -4, 4)     # (x − 1)² + y² = 7
PE = plano_igual(-8, 12, -11, 9)    # o erro: raio 9 passaria por (11, −1)
PQ1 = plano_igual(-6, 4, -1, 10, lado=720)   # (x + 1)² + (y − 5)² = 16
PQ2 = plano_igual(-3, 11, -7, 7)    # centro (4, 0), raio 6


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def s01():
        eqn(c, t, C["s01.a"], red("(x − 2)^2", "(y + 1)^2", "9", TINTA, TINTA, TINTA), XE, 330, 78)
        E.frase(c, t, C["s01.a"] + 4.0, ps("parece só uma conta", "i", 62, TINTA2), XE, 470, passo=0.12)
        E.frase(c, t, C["s01.b"], [("é", "i", 84), ("um", "i", 84), ("desenho", "g", 84, COR)], XE, 620)
        eixos(c, t, C["s01.b"], PC, [-2, 2, 4, 6], [-4, -2, 2])
        circ(c, t, C["s01.b"] + 0.4, PC, 2, -1, 3, d=1.2)
        centro_c(c, t, C["s01.c"], PC, 2, -1)
        if t >= C["s01.c"] + 0.6:
            seg(c, t, C["s01.c"] + 0.6, PC, (2, -1), (5, -1), DIST, 0.6, 7)
        pil(c, t, C["s01.c"] + 0.4, "centro (2, −1)", XE + 170, 770, 46, TINTA)
        pil(c, t, C["s01.c"] + 1.0, "raio 3", XE + 500, 770, 46, DIST)
        E.frase(c, t, C["s01.c"] + 1.8, [("em", "i", 62), ("5", "g", 62, COR), ("segundos", "i", 62)], XE, 900)
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    E.foco(c, t, C["s02.a"] + 1.0, 0.7, lambda a: E.bola(c, 1480, 540, 270 * ease_back(prog(t, C["s02.a"] + 1.0, 0.7))), blur=0)
    E.foco(c, t, C["s02.a"] + 1.3, 0.5, lambda a: c.drawCircle(1480, 540, 150, M.paint(BR, a, stroke=16)))
    E.foco(c, t, C["s02.a"] + 1.5, 0.5, lambda a: (c.drawCircle(1480, 540, 16, M.paint(BR, a)), M.line(c, 1480, 540, 1630, 540, BR, a, 10)))
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 300)
    E.frase(c, t, C["s02.a"] + 1.0, [("ler", "i", 96), ("centro", "g", 104), ("e", "i", 96), ("raio", "g", 104, COR)], XE, 450)
    E.frase(c, t, C["s02.b"], [("escrever", "i", 90), ("a", "i", 90), ("equação", "g", 96, COR)], XE, 600)
    E.frase(c, t, C["s02.c"], [("+", "g", 84, COR), ("atalho", "g", 84), ("de", "i", 84), ("prova", "i", 84)], XE, 750)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("duas", "g", 80, COR, C["s03.a"]), ("coisas", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 200, "center")
    x, w = 230, 1460
    for k, y in (("s03.b", 290), ("s03.c", 590)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 250, p, prog_=p)
    # 1: todos à mesma distância do centro
    k = C["s03.b"]
    cx, cy, r = 430, 415, 95
    E.foco(c, t, k + 0.3, 0.5, lambda a: (c.drawCircle(cx, cy, r, M.paint(DIST, a, stroke=7)), c.drawCircle(cx, cy, 10, M.paint(TINTA, a))))
    for i, ang in enumerate((20, 140, 250)):
        q = ep(t, k + 1.0 + i * 0.4, 0.4)
        if q > 0:
            ex, ey = cx + r * math.cos(math.radians(ang)), cy - r * math.sin(math.radians(ang))
            M.line(c, cx, cy, lerp(cx, ex, q), lerp(cy, ey, q), DIST, 1.0, 6)
    E.frase(c, t, k, [("todos", "i", 64), ("à", "i", 64), ("mesma", "g", 64), ("distância", "i", 64), ("do", "i", 64), ("centro", "g", 64)], 620, 400)
    E.frase(c, t, k + 2.6, [("essa", "i", 64), ("distância", "i", 64), ("é", "i", 64), ("o", "i", 64), ("raio", "g", 64, DIST)], 620, 490)
    # 2: distância com Pitágoras
    k = C["s03.c"]
    A_, R_, T_ = (330, 800), (560, 800), (560, 650)
    q = ep(t, k + 0.6, 0.5)
    if q > 0:
        M.line(c, *A_, *R_, DX, q, 10)
        M.line(c, *R_, *T_, DY, q, 10)
    q2 = ep(t, k + 1.2, 0.5)
    if q2 > 0:
        M.line(c, *A_, *T_, DIST, 1.0, 10, progress=q2)
    E.frase(c, t, k, [("distância", "g", 64, DIST), ("entre", "i", 64), ("dois", "i", 64), ("pontos", "i", 64)], 680, 700)
    E.frase(c, t, k + 1.6, [("triângulo", "i", 64), ("retângulo:", "i", 64), ("Pitágoras", "g", 64, COR)], 680, 790)
    E.frase(c, t, C["s04"] - 2.6, ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 960, "center", passo=0.1)


# ---------------- centro na origem ----------------
P34 = (3, 4)


def b_origem(c, t, C, b):
    eixos(c, t, C["s04"] + 0.2, PO, [-3, 3], [-4, 4])
    circ(c, t, C["s04.a"] + 0.4, PO, 0, 0, 5, d=1.2)
    centro_c(c, t, C["s04.a"] + 0.2, PO, 0, 0, lado=(-1, 1))

    if t >= C["s04.b"]:
        E.saida(c, t, C["s05"] - 0.1, lambda: (nome(c, t, C["s04.b"] + 0.3, PO, *P34, None),
                                                degrau(c, t, PO, (0, 0), P34, C["s04.c"], C["s04.c"] + 0.6, "3", "4", sombra=C["s04.c"] + 0.8, size=50),
                                                cateto(c, t, C["s04.e"], PO, (0, 0), P34, DIST, 0.6, 9),
                                                lado_txt(c, t, C["s04.e"] + 0.5, PO, (0, 0), P34, "5", (2, 1.33), DIST, 54),
                                                E.foco(c, t, C["s04.b"] + 0.5, 0.4, lambda a: E._cola(c, "(3, 4)", *PO(*P34), 1, -1, 26, 44, "b", TINTA, a))))
    if t >= C["s05"]:
        nome(c, t, C["s05"], PO, *PG, None)
        E.foco(c, t, C["s05"] + 0.3, 0.4, lambda a: E._cola(c, "(x, y)", *PO(*PG), 1, -1, 26, 44, "b", TINTA, a))
        degrau(c, t, PO, (0, 0), PG, C["s05.a"], C["s05.a"] + 0.5, "x", "y", sombra=C["s05.a"] + 0.7, size=50)
        cateto(c, t, C["s05.b"], PO, (0, 0), PG, DIST, 0.6, 9)
        lado_txt(c, t, C["s05.b"] + 0.5, PO, (0, 0), PG, "5", (2.7, 0.9), DIST, 54)
        if t >= C["s05.c"]:
            nome(c, t, C["s05.c"], PO, -3, 4, None)
            degrau(c, t, PO, (0, 0), (-3, 4), C["s05.c"] + 0.3, C["s05.c"] + 0.7, "−3", "4", size=46)
            cateto(c, t, C["s05.c"] + 1.1, PO, (0, 0), (-3, 4), DIST, 0.6, 9)

    def s04():
        E.frase(c, t, C["s04.a"], [("centro", "i", 64), ("na", "i", 64), ("origem,", "g", 64), ("raio", "i", 64), ("5", "g", 64, DIST)], XE, 230)
        E.frase(c, t, C["s04.b"], [("o", "i", 60), ("ponto", "i", 60)], XE, 350)
        par_em(c, t, C["s04.b"] + 0.4, "3", "4", XE + 230, 350, 60)
        E.frase(c, t, C["s04.c"], [("catetos", "i", 60), ("3", "g", 60, DX), ("e", "i", 60), ("4", "g", 60, DY)], XE, 470)
        conta_em(c, t, C["s04.d"], [("3", DX), ("^2 + ", TINTA), ("4", DY), ("^2 = 25", TINTA)], XE, 620, 80)
        conta_em(c, t, C["s04.e"], [("25 = ", TINTA), ("5", DIST), ("^2", TINTA)], XE, 750, 80)
        E.frase(c, t, C["s04.e"] + 1.6, [("a", "i", 58), ("5", "g", 58, DIST), ("do", "i", 58), ("centro:", "i", 58), ("na", "i", 58),
                                         ("circunferência", "g", 58, COR)], XE, 880, passo=0.12)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], [("qualquer", "i", 62), ("ponto", "i", 62)], XE, 230)
    par_em(c, t, C["s05"] + 0.6, "x", "y", XE + 470, 230, 62)
    E.frase(c, t, C["s05.a"], [("catetos:", "i", 58), ("o", "i", 58), ("x", "g", 58, DX), ("e", "i", 58), ("o", "i", 58), ("y", "g", 58, DY)], XE, 340)
    E.frase(c, t, C["s05.b"], [("hipotenusa:", "i", 58), ("o", "i", 58), ("raio", "g", 58, DIST)], XE, 440)
    conta_em(c, t, C["s05.c"], [("(−3)^2 = 9", TINTA)], XE, 560, 64)
    E.frase(c, t, C["s05.c"] + 1.2, ps("o quadrado apaga o sinal", "i", 50, TINTA2), XE + 360, 560, passo=0.1)
    eqn(c, t, C["s05.d"], [("x", DX), ("^2 + ", TINTA), ("y", DY), ("^2 = ", TINTA), ("25", DIST)], XE, 750, 100, caixa=C["s05.e"])
    E.frase(c, t, C["s05.e"], [("a", "i", 56), ("equação", "g", 56, COR), ("da", "i", 56), ("circunferência", "g", 56, COR)], XE, 900, passo=0.12)


PG = (5 * math.cos(math.radians(35)), 5 * math.sin(math.radians(35)))  # um ponto (x, y) qualquer


# ---------------- centro fora da origem ----------------
PX = (2 + 3 * math.cos(math.radians(50)), -1 + 3 * math.sin(math.radians(50)))  # ponto (x, y) na circunferência


def base_c(c, t, t0, tc=None):
    eixos(c, t, t0, PC, [-2, 2, 4, 6], [-4, -2, 2])
    circ(c, t, t0 if tc is None else tc, PC, 2, -1, 3)
    centro_c(c, t, t0 if tc is None else tc, PC, 2, -1)


def b_centro(c, t, C, b):
    base_c(c, t, C["s06"] + 0.2, C["s06.a"] + 0.3)
    R = (PX[0], -1)

    def tri():
        nome(c, t, C["s06.b"] - 0.4, PC, *PX, None)
        E.foco(c, t, C["s06.b"] - 0.2, 0.4, lambda a: E._cola(c, "(x, y)", *PC(*PX), 1, -1, 26, 44, "b", TINTA, a))
        sombra_tri(c, t, C["s06.b"] + 0.6, PC, (2, -1), R, PX)
        cateto(c, t, C["s06.b"], PC, (2, -1), R, DX, 0.6, 10)
        cateto(c, t, C["s06.c"], PC, R, PX, DY, 0.6, 10)
        cateto(c, t, C["s07.a"], PC, (2, -1), PX, DIST, 0.6, 9)
        if t >= C["s06.c"] + 0.6:
            canto(c, t, C["s06.c"] + 0.6, PC, R, (2, -1), PX)
        G = ((2 + R[0] + PX[0]) / 3, (-1 - 1 + PX[1]) / 3)
        lado_txt(c, t, C["s06.b"] + 0.5, PC, (2, -1), R, "x − 2", G, DX, 44)
        E.saida(c, t, C["s06.d"], lambda: lado_txt(c, t, C["s06.c"] + 0.5, PC, R, PX, "y − (−1)", G, DY, 44, em=0.8))
        if t >= C["s06.d"]:
            lado_txt(c, t, C["s06.d"] + 0.2, PC, R, PX, "y + 1", G, DY, 44, em=0.8)
        lado_txt(c, t, C["s07.a"] + 0.5, PC, (2, -1), PX, "3", G, DIST, 50)
    E.saida(c, t, C["s08"] - 0.1, tri)
    if t >= C["s08.a"]:  # o ponto (5, −1)
        nome(c, t, C["s08.a"] + 0.3, PC, 5, -1, None)
        E.foco(c, t, C["s08.a"] + 0.5, 0.4, lambda a: E._cola(c, "(5, −1)", *PC(5, -1), 0.2, 1, 24, 42, "b", TINTA, a))
        anda(c, t, C["s08.a"] + 0.6, PC, (2, -1), (5, -1), DX, 0.6, 8)
        if t >= C["s08.d"] + 0.8:
            anel(c, t, C["s08.d"] + 0.8, *PC(5, -1), CERTO)
            anel(c, t, C["s08.d"] + 1.3, *PC(5, -1), CERTO)

    def s06():
        E.frase(c, t, C["s06.a"], [("centro", "i", 60)], XE, 230)
        par_em(c, t, C["s06.a"] + 0.4, "2", "−1", XE + 230, 230, 60)
        E.frase(c, t, C["s06.a"] + 1.0, [("raio", "i", 60), ("3", "g", 60, DIST)], XE + 560, 230)
        E.frase(c, t, C["s06.b"], [("deitado:", "i", 58)], XE, 380)
        conta_em(c, t, C["s06.b"] + 0.5, [("x − 2", DX)], XE + 280, 380, 70)
        E.frase(c, t, C["s06.c"], [("em", "i", 58), ("pé:", "i", 58)], XE, 500)
        E.saida(c, t, C["s06.d"], lambda: conta_em(c, t, C["s06.c"] + 0.5, [("y − (−1)", DY)], XE + 280, 500, 70))
        conta_em(c, t, C["s06.d"], [("y + 1", DY)], XE + 280, 500, 70)
        if t >= C["s07"]:
            E.frase(c, t, C["s07"], [("Pitágoras", "g", 58, COR)], XE, 650)
            conta_em(c, t, C["s07.a"], red("(x − 2)^2", "(y + 1)^2", "3^2"), XE, 780, 68)
            E.saida(c, t, C["s07.b"], lambda: None)
            eqn(c, t, C["s07.b"], red("(x − 2)^2", "(y + 1)^2", "9"), XE, 910, 68, caixa=C["s07.b"] + 0.8)
            E.frase(c, t, C["s07.b"] + 1.4, ps("é a equação do começo", "i", 46, TINTA2), XE, 1010, passo=0.1)
    E.saida(c, t, C["s08"] - 0.1, s06)
    if t < C["s08"]:
        return
    eqn(c, t, C["s08"], red("(x − 2)^2", "(y + 1)^2", "9"), XE, 220, 64)
    E.frase(c, t, C["s08.a"], [("confira", "i", 58, TINTA2), ("com", "i", 58, TINTA2)], XE, 340)
    par_em(c, t, C["s08.a"] + 0.5, "5", "−1", XE + 330, 340, 58)
    conta_em(c, t, C["s08.b"], [("(5 − 2)^2 = 3^2 = ", TINTA), ("9", DX)], XE, 480, 66)
    conta_em(c, t, C["s08.c"], [("(−1 + 1)^2 = 0^2 = ", TINTA), ("0", DY)], XE, 610, 66)
    conta_em(c, t, C["s08.d"], [("9", DX), (" + ", TINTA), ("0", DY), (" = ", TINTA), ("9", DIST)], XE, 760, 76)
    ok(c, t, C["s08.d"] + 0.8, XE + 440, 735)
    E.frase(c, t, C["s08.d"] + 1.4, ps("está na circunferência", "i", 54, TINTA2), XE, 880, passo=0.1)


# ---------------- a regra geral ----------------
def b_regra(c, t, C, b):
    y0 = 470
    partes = red("(x − a)^2", "(y − b)^2", "r^2")
    w = conta(None, partes, 0, 0, 120, 0)
    x0 = W / 2 - w / 2
    eqn(c, t, C["s09.a"], partes, W / 2, y0, 120, "center")
    E.frase(c, t, C["s09"], [("a", "i", 72), ("regra", "g", 72, COR), ("geral", "i", 72)], W / 2, 220, "center")
    wa = conta(None, [("(x − ", 0)], 0, 0, 120, 0)
    wxa = conta(None, [("(x − a)^2 + ", 0)], 0, 0, 120, 0)
    wyb = conta(None, [("(y − ", 0)], 0, 0, 120, 0)
    xa = x0 + wa + 30
    xb = x0 + wxa + wyb + 30
    xr = x0 + w - 50
    for xx, tt in ((xa, C["s09.b"]), (xb, C["s09.b"] + 0.4)):
        q = ep(t, tt, 0.4)
        if q > 0:
            M.arrow(c, xx, y0 + 150, xx, y0 + 50, TINTA, q, 6, 20, q)
    E.foco(c, t, C["s09.b"] + 0.6, 0.5, lambda a: (E.pilula(c, "centro (a, b)", (xa + xb) / 2, y0 + 210, 52, "g", fundo=TINTA, a=a)))
    q = ep(t, C["s09.c"], 0.4)
    if q > 0:
        M.arrow(c, xr, y0 + 150, xr, y0 + 50, DIST, q, 6, 20, q)
    pil(c, t, C["s09.c"] + 0.2, "r = raio", xr, y0 + 210, 52, DIST)
    E.foco(c, t, C["s09.d"], 0.5, lambda a: E.caixa_pontilhada(c, x0 - 40, y0 - 140, w + 80, 190, a, COR))
    E.frase(c, t, C["s09.d"] + 0.3, [("equação", "g", 84, COR), ("reduzida", "g", 84, COR)], W / 2, 900, "center")


# ---------------- ler o centro e o raio ----------------
def b_ler(c, t, C, b):
    base_c(c, t, C["s10"] + 0.2)
    eqn(c, t, C["s10"] + 0.1, red("(x − 2)^2", "(y + 1)^2", "9"), XE, 220, 70)
    w1 = conta(None, [("(x − 2)^2 + ", 0)], 0, 0, 70, 0)
    # o sinal dentro de cada parêntese
    q = pulso(t, C["s10.a"], 2.4)
    if q > 0:
        for xx in (XE + 120, XE + w1 + 120):
            c.drawCircle(xx, 196, 40, M.paint(COR, q, stroke=5))
    E.frase(c, t, C["s10.a"], ps("olhe o sinal", "i", 56, TINTA2), XE, 320, passo=0.1)
    conta_em(c, t, C["s10.b"], [("x − 2", DX), ("  →  x do centro: ", TINTA2), ("2", ENT)], XE, 450, 58)
    conta_em(c, t, C["s10.c"], [("y + 1 = y − (−1)", DY)], XE, 570, 58)
    conta_em(c, t, C["s10.c"] + 3.0, [("→  y do centro: ", TINTA2), ("−1", SAI)], XE + 40, 660, 58)
    E.frase(c, t, C["s10.d"], [("sinal", "g", 66, COR), ("contrário", "g", 66, COR), ("ao", "i", 66), ("que", "i", 66), ("aparece", "i", 66)], XE, 800)
    if t >= C["s10.d"]:
        anel(c, t, C["s10.d"], *PC(2, -1), COR)
        anel(c, t, C["s10.d"] + 0.5, *PC(2, -1), COR)
        pil(c, t, C["s10.d"] + 0.3, "(2, −1)", PC.x(2) + 110, PC.y(-1) + 56, 40, TINTA)
    conta_em(c, t, C["s10.e"], [("r = r{9} = ", TINTA), ("3", DIST)], XE, 940, 70)
    if t >= C["s10.e"] + 0.4:
        seg(c, t, C["s10.e"] + 0.4, PC, (2, -1), (2, 2), DIST, 0.6, 8)
        lado_txt(c, t, C["s10.e"] + 0.9, PC, (2, -1), (2, 2), "3", (3, 0), DIST, 50)


# ---------------- escrever a equação ----------------
def b_escrever(c, t, C, b):
    def s11():
        eixos(c, t, C["s11"] + 0.2, PW, [-8, -6, -3, 2], [2, 4, 6, 8])
        centro_c(c, t, C["s11.a"] + 0.3, PW, -3, 4, lado=(1, 1))
        circ(c, t, C["s11.a"] + 0.8, PW, -3, 4, 5)
        if t >= C["s11.a"] + 1.4:
            seg(c, t, C["s11.a"] + 1.4, PW, (-3, 4), (-3, 9), DIST, 0.6, 8)
            lado_txt(c, t, C["s11.a"] + 1.9, PW, (-3, 4), (-3, 9), "5", (-1, 6), DIST, 50)
        E.frase(c, t, C["s11"], [("o", "i", 60), ("caminho", "i", 60), ("de", "i", 60), ("volta", "g", 60, COR)], XE, 220)
        E.frase(c, t, C["s11.a"], [("centro", "i", 58)], XE, 330)
        par_em(c, t, C["s11.a"] + 0.4, "−3", "4", XE + 220, 330, 58)
        E.frase(c, t, C["s11.a"] + 1.2, [("raio", "i", 58), ("5", "g", 58, DIST)], XE + 560, 330)
        conta_em(c, t, C["s11.b"], [("x − (−3)", TINTA), ("  →  ", TINTA2), ("x + 3", DX)], XE, 460, 62)
        conta_em(c, t, C["s11.c"], [("y − 4", DY)], XE, 570, 62)
        conta_em(c, t, C["s11.d"], [("5^2 = ", TINTA), ("25", DIST)], XE, 680, 62)
        eqn(c, t, C["s11.e"], red("(x + 3)^2", "(y − 4)^2", "25"), XE, 860, 70, caixa=C["s11.e"] + 1.2)
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"], ps("e se não for um quadrado perfeito?", "i", 54, TINTA2), XE, 220, passo=0.1)
    eixos(c, t, C["s12.a"], P12, [-2, 2, 4], [-3, -2, 2, 3])
    eqn(c, t, C["s12.a"], red("(x − 1)^2", "y^2", "7"), XE, 360, 76)
    conta_em(c, t, C["s12.b"], [("r = ", TINTA), ("r{7}", DIST)], XE, 500, 72)
    conta_em(c, t, C["s12.c"], [("y", DY), ("^2", DY), (" = ", TINTA), ("(y − 0)^2", DY)], XE, 650, 64)
    E.frase(c, t, C["s12.d"], [("centro", "i", 60)], XE, 800)
    par_em(c, t, C["s12.d"] + 0.4, "1", "0", XE + 230, 800, 60)
    centro_c(c, t, C["s12.d"] + 0.3, P12, 1, 0, lado=(-1, -1))
    circ(c, t, C["s12.b"] + 0.4, P12, 1, 0, math.sqrt(7))
    if t >= C["s12.b"] + 1.0:
        seg(c, t, C["s12.b"] + 1.0, P12, (1, 0), (1 + math.sqrt(7) * math.cos(math.radians(60)), math.sqrt(7) * math.sin(math.radians(60))), DIST, 0.6, 8)
        E.foco(c, t, C["s12.b"] + 1.5, 0.4, lambda a: E._cola(c, "√7", *P12(1.9, 1.2), 1, 0, 14, 48, "g", DIST, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    eixos(c, t, C["s13"] + 0.2, PE, [-6, 2, 6, 11], [-8, -4, 4, 8], size=32)
    circ(c, t, C["s13"] + 0.4, PE, 2, -1, 3)
    centro_c(c, t, C["s13"] + 0.4, PE, 2, -1, lado=(-1, 1))
    circ(c, t, C["s13.c"], PE, 2, -1, 9, ERRADO, 1.2, 6, tracejado=True)
    if t >= C["s13.c"] + 0.8:
        nome(c, t, C["s13.c"] + 0.8, PE, 11, -1, None, cor=ERRADO)
        E.foco(c, t, C["s13.c"] + 1.0, 0.4, lambda a: E._cola(c, "(11, −1)", *PE(11, -1), -0.3, 1, 24, 40, "b", ERRADO, a))
    E.frase(c, t, C["s13"], [("cuidado", "g", 84, ERRADO)], XE, 230)
    eqn(c, t, C["s13"] + 0.4, red("(x − 2)^2", "(y + 1)^2", "9"), XE, 350, 62)
    conta_em(c, t, C["s13.a"], [("r = 9", ERRADO)], XE, 480, 72)
    if t >= C["s13.b"] + 0.6:
        E.risco(c, XE - 10, 500, XE + 230, 420, t, C["s13.b"] + 0.6, largura=9)
    E.frase(c, t, C["s13.b"], [("9", "g", 60, DIST), ("é", "i", 60), ("o", "i", 60), ("raio", "i", 60), ("ao", "i", 60), ("quadrado", "g", 60)], XE + 290, 480)
    conta_em(c, t, C["s13.d"], [("(11 − 2)^2 = 9^2 = 81", TINTA)], XE, 640, 62)
    conta_em(c, t, C["s13.e"], [("81 ≠ 9", ERRADO)], XE, 760, 72)
    E.frase(c, t, C["s13.e"] + 0.8, ps("não cumpre a equação", "i", 50, TINTA2), XE + 300, 760, passo=0.1)
    conta_em(c, t, C["s13.f"], [("r = r{9} = 3", CERTO)], XE, 900, 80)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    eq = red("(x − 2)^2", "(y + 1)^2", "9", DX_ESC, DY_ESC, BR, BR)

    def s14():
        E.frase(c, t, C["s14"], ps("o atalho para o centro", "i", 60, CLARO), W / 2, 170, "center", passo=0.12)
        y0 = 400
        w = conta(None, eq, 0, 0, 110, 0)
        x0 = W / 2 - w / 2
        E.foco(c, t, C["s14"] + 0.4, 0.5, lambda a: conta(c, eq, W / 2, y0, 110, a, "center"))
        E.frase(c, t, C["s14.a"], [("que", "i", 64, CLARO), ("número", "i", 64, CLARO), ("zera", "g", 64, BR), ("cada", "i", 64, CLARO),
                                   ("parêntese?", "i", 64, CLARO)], W / 2, 260, "center")
        w1 = conta(None, [("(x − 2)^2", 0)], 0, 0, 110, 0)
        w2 = conta(None, [("(x − 2)^2 + ", 0)], 0, 0, 110, 0)
        w3 = conta(None, [("(y + 1)^2", 0)], 0, 0, 110, 0)
        c1, c2 = x0 + w1 / 2 - 20, x0 + w2 + w3 / 2 - 20
        E.foco(c, t, C["s14.b"], 0.5, lambda a: conta(c, [("x = ", BR), ("2", DX_ESC)], c1, y0 + 160, 76, a, "center"))
        E.foco(c, t, C["s14.b"] + 0.6, 0.5, lambda a: conta(c, [("2 − 2 = 0", CLARO)], c1, y0 + 260, 56, a, "center"))
        E.foco(c, t, C["s14.c"], 0.5, lambda a: conta(c, [("y = ", BR), ("−1", DY_ESC)], c2, y0 + 160, 76, a, "center"))
        E.foco(c, t, C["s14.c"] + 0.6, 0.5, lambda a: conta(c, [("−1 + 1 = 0", CLARO)], c2, y0 + 260, 56, a, "center"))
        E.foco(c, t, C["s14.d"], 0.5, lambda a: (E.bola(c, W / 2, 870, 120 * ease_back(prog(t, C["s14.d"], 0.5)), a=a),
                                                E.formula(c, "(2, −1)", W / 2, 892, 64, "g", BR, a, "center")))
        E.frase(c, t, C["s14.d"] + 1.6, ps("sem trocar sinal", "i", 52, CLARO), 1300, 880, passo=0.1)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"], [("por", "i", 66, CLARO), ("que", "i", 66, CLARO), ("funciona", "g", 66, BR)], W / 2, 180, "center")
    E.frase(c, t, C["s15.a"], [("o", "i", 60, CLARO), ("centro", "g", 60, BR), ("está", "i", 60, CLARO), ("a", "i", 60, CLARO), ("distância", "i", 60, CLARO),
                               ("0", "g", 60, BR), ("dele", "i", 60, CLARO), ("mesmo", "i", 60, CLARO)], W / 2, 320, "center", passo=0.1)
    E.foco(c, t, C["s15.a"] + 2.4, 0.5, lambda a: conta(c, [("(2 − 2)^2", DX_ESC), (" + ", BR), ("(−1 + 1)^2", DY_ESC), (" = 0", BR)], W / 2, 460, 72, a, "center"))
    E.frase(c, t, C["s15.b"], [("não", "g", 62, ERRADO), ("compensa", "i", 62, CLARO), ("com", "i", 62, CLARO), ("os", "i", 62, CLARO),
                               ("parênteses", "i", 62, CLARO), ("abertos", "g", 62, BR)], W / 2, 650, "center", passo=0.12)
    E.foco(c, t, C["s15.b"] + 2.0, 0.5, lambda a: E.formula(c, "x^2 + y^2 − 4x + 2y − 4 = 0", W / 2, 780, 66, "g", CLARO, a, "center"))
    E.frase(c, t, C["s15.c"], [("fica", "i", 60, CLARO), ("para", "i", 60, CLARO), ("a", "i", 60, CLARO), ("próxima", "g", 60, BR), ("aula", "i", 60, CLARO)],
            W / 2, 930, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    x, w = 230, 1460
    for k, y in (("s16.a", 250), ("s16.c", 500)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.foco(c, t, C[k], 0.5, lambda a, y=y, i=(1 if k == "s16.a" else 2): (E.bola(c, x + 80, y + 110, 46, a=a),
                                                                               centro(c, str(i), x + 80, y + 130, 54, "g", BR, a)))
    eqn(c, t, C["s16.a"] + 0.2, red("(x + 1)^2", "(y − 5)^2", "16", TINTA, TINTA, TINTA), x + 170, 345, 72)
    E.frase(c, t, C["s16.b"], [("centro?", "g", 62, COR), ("raio?", "g", 62, COR)], x + 170, 440)
    E.frase(c, t, C["s16.c"], [("centro", "i", 62)], x + 170, 595)
    par_em(c, t, C["s16.c"] + 0.4, "4", "0", x + 400, 595, 62)
    E.frase(c, t, C["s16.c"] + 1.0, [("raio", "i", 62), ("6", "g", 62, DIST)], x + 680, 595)
    E.frase(c, t, C["s16.c"] - 1.0, [("escreva", "g", 62, COR), ("a", "i", 62), ("equação", "i", 62)], x + 170, 690)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1450, cy=850, r=62)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s18():
        eixos(c, t, C["s18"] + 0.2, PQ1, [-5, -1, 3], [1, 5])
        eqn(c, t, C["s18"] + 0.2, red("(x + 1)^2", "(y − 5)^2", "16"), XE, 220, 64)
        conta_em(c, t, C["s18.a"], [("x + 1", DX), (" zera com ", TINTA2), ("−1", ENT)], XE, 370, 62)
        conta_em(c, t, C["s18.b"], [("y − 5", DY), (" zera com ", TINTA2), ("5", SAI)], XE, 490, 62)
        E.frase(c, t, C["s18.c"], [("centro", "i", 62)], XE, 640)
        E.foco(c, t, C["s18.c"] + 0.3, 0.5, lambda a: par(c, "−1", "5", XE + 230, 640, 66, a))
        centro_c(c, t, C["s18.c"] + 0.3, PQ1, -1, 5, lado=(-1, 1))
        conta_em(c, t, C["s18.d"], [("r = r{16} = ", TINTA), ("4", DIST)], XE, 790, 70)
        circ(c, t, C["s18.d"] + 0.5, PQ1, -1, 5, 4)
        if t >= C["s18.d"] + 1.0:
            seg(c, t, C["s18.d"] + 1.0, PQ1, (-1, 5), (3, 5), DIST, 0.6, 8)
            lado_txt(c, t, C["s18.d"] + 1.5, PQ1, (-1, 5), (3, 5), "4", (1, 7), DIST, 50)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    eixos(c, t, C["s19"], PQ2, [2, 4, 6, 8], [-6, 6])
    centro_c(c, t, C["s19"] + 0.3, PQ2, 4, 0, lado=(-1, -1))
    E.frase(c, t, C["s19"], [("centro", "i", 58)], XE, 220)
    par_em(c, t, C["s19"] + 0.4, "4", "0", XE + 220, 220, 58)
    E.frase(c, t, C["s19"] + 1.0, [("raio", "i", 58), ("6", "g", 58, DIST)], XE + 500, 220)
    conta_em(c, t, C["s19.a"], [("(x − 4)^2", DX)], XE, 370, 66)
    conta_em(c, t, C["s19.b"], [("(y − 0)^2 = ", TINTA), ("y^2", DY)], XE, 500, 66)
    conta_em(c, t, C["s19.c"], [("6^2 = ", TINTA), ("36", DIST)], XE, 630, 66)
    circ(c, t, C["s19.c"] + 0.4, PQ2, 4, 0, 6)
    if t >= C["s19.c"] + 1.0:
        seg(c, t, C["s19.c"] + 1.0, PQ2, (4, 0), (4, 6), DIST, 0.6, 8)
        lado_txt(c, t, C["s19.c"] + 1.5, PQ2, (4, 0), (4, 6), "6", (5, 3), DIST, 50)
    eqn(c, t, C["s19.d"], red("(x − 4)^2", "y^2", "36"), XE, 820, 76, caixa=C["s19.d"] + 1.4)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s20.a", [("centro", "g", 80), ("=", "i", 80), ("o", "i", 80), ("que", "i", 80), ("zera", "g", 80, COR), ("os", "i", 80),
                            ("parênteses", "i", 80)]),
                 ("s20.b", [("raio", "g", 80, DIST), ("=", "i", 80), ("raiz", "g", 80), ("do", "i", 80), ("número", "i", 80), ("da", "i", 80),
                            ("direita", "i", 80)]))
        for i, (k, partes) in enumerate(itens):
            y = 460 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s21.a"], [("parênteses", "g", 110, COR), ("abertos", "i", 110)], XE, 420)
    E.formula_em(c, t, C["s21.b"], "x^2 + y^2 − 4x + 2y − 4 = 0", XE, 560, 70, "g", TINTA)
    E.frase(c, t, C["s21.c"], [("completar", "g", 100, COR), ("quadrados", "g", 100, COR)], XE, 720)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 300, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(620, 325, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, origem=b_origem, centro=b_centro, regra=b_regra, ler=b_ler, escrever=b_escrever,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
