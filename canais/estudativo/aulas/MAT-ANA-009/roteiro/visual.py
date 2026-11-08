"""Visual — Estudativo · MAT-ANA-009: equação geral da circunferência, completar quadrados.

Segue a linguagem da Geometria Analítica (MAT-ANA-001) e a da equação reduzida (MAT-ANA-008, leia o cabeçalho de lá):
- tudo o que é do x (x², −4x, o +4 que completa, (x − 2)²) em petróleo (DX); tudo o que é do y em âmbar (DY); o lado direito,
  r² e o raio em índigo (DIST); a circunferência em índigo, o centro como ponto preto "C";
- o número que completa o quadrado entra numa caixa pontilhada ("a peça que falta") e, no passo 3, aparece também na direita,
  na cor do seu grupo, para mostrar que o que entra de um lado entra do outro (a balança de E.balanca no erro);
- os três passos do método numeram-se com esferas; erro em vermelho, certo em verde, atalho no palco escuro.
Peças desta aula (além das de MAT-ANA-008): passo_n() (esfera com o número do passo e o título), falta() (caixa da peça que falta).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Analítica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANA-009_equacao_geral_completar_quadrados.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("origem", "metodo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ENT, SAI = COR, TINTA                       # x / y, como em Funções
DX, DY, DIST = "#0E9AA7", "#D98A00", E.COR  # o que é do x, o que é do y, o lado direito / raio
DX_ESC, DY_ESC = "#3CC7D3", "#FFB833"
# as contas do roteiro
_f = lambda x, y: x * x + y * y - 4 * x + 2 * y - 4
assert all(abs(_f(x, y) - ((x - 2) ** 2 + (y + 1) ** 2 - 9)) < 1e-9 for x, y in ((0, 0), (3, -2), (5, 7)))
assert 4 + 1 - 9 == -4 and -4 / 2 == -2 and (-2) ** 2 == 4 and 2 / 2 == 1 and 1 ** 2 == 1 and 4 + 4 + 1 == 9 and math.isqrt(9) == 3
assert math.isqrt(4) == 2 and 2 ** 2 + (-1) ** 2 == 5 and 5 - (-4) == 9
_g = lambda x, y: x * x + y * y + 8 * x - 6 * y
assert 8 / 2 == 4 and 4 ** 2 == 16 and -6 / 2 == -3 and (-3) ** 2 == 9 and 16 + 9 - 0 == 25 and math.isqrt(25) == 5
assert all(abs(_g(x, y) - ((x + 4) ** 2 + (y - 3) ** 2 - 25)) < 1e-9 for x, y in ((0, 0), (1, 2)))


def plano_igual(xmin, xmax, ymin, ymax, lado=740, cx=1430, cy=545):
    """Plano com a mesma escala nos dois eixos (a circunferência sai redonda), centrado em (cx, cy)"""
    u = lado / max(xmax - xmin, ymax - ymin)
    w, h = (xmax - xmin) * u, (ymax - ymin) * u
    return E.Plano(cx - w / 2, cy - h / 2, w, h, xmin, xmax, ymin, ymax)


PC = plano_igual(-2, 6, -5, 3, lado=600, cx=1500, cy=560)    # centro (2, −1), raio 3
PQ = plano_igual(-10, 2, -3, 9, lado=640, cx=1480, cy=560)   # questão: centro (−4, 3), raio 5


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


def passo_n(c, t, t0, n, txt, x=XE, y=200, size=64):
    """esfera com o número do passo e o título ao lado"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, x + 44, y - 22, 46 * ease_back(prog(t, t0, 0.5)), a=a),
                                     centro(c, str(n), x + 44, y - 2, 54, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, ps(txt, "i", size), x + 120, y, passo=0.1)


def falta(c, t, t0, x, y, w, h, cor=None, t1=None):
    """caixa pontilhada da peça que falta (some em t1)"""
    if t < t0 or (t1 is not None and t >= t1):
        return
    p = ep(t, t0, 0.5)
    E.caixa_pontilhada(c, x, y, w, h, p, cor or COR, prog_=p)


def larg(partes, size):
    return conta(None, partes, 0, 0, size, 0)


EQ_ABERTA = [("x^2", DX), (" + ", TINTA), ("y^2", DY), (" − 4x", DX), (" + 2y", DY), (" − 4 = 0", TINTA)]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def s01():
        cores = C["s01.c"] + 0.3
        neutro = [(s, TINTA) for s, _ in EQ_ABERTA]
        w = larg(EQ_ABERTA, 92)
        E.foco(c, t, C["s01.a"], 0.5, lambda a: conta(c, neutro, W / 2, 420, 92, a * (1 - ep(t, cores, 0.5)), "center"))
        if t >= cores:
            conta(c, EQ_ABERTA, W / 2, 420, 92, ep(t, cores, 0.5), "center")
        E.frase(c, t, C["s01.a"] + 5.0, [("é", "i", 70), ("uma", "i", 70), ("circunferência", "g", 70, COR)], W / 2, 580, "center")
        E.frase(c, t, C["s01.b"], [("onde", "i", 84), ("está", "i", 84), ("o", "i", 84), ("centro?", "g", 84, COR)], W / 2, 750, "center")
        E.frase(c, t, C["s01.c"], [("os", "i", 70), ("quadrados", "g", 70, COR), ("estão", "i", 70), ("desmontados", "g", 70)], W / 2, 900, "center")
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    E.foco(c, t, C["s02.a"] + 1.0, 0.7, lambda a: E.bola(c, 1480, 540, 270 * ease_back(prog(t, C["s02.a"] + 1.0, 0.7))), blur=0)
    E.foco(c, t, C["s02.a"] + 1.4, 0.5, lambda a: E.formula(c, "(  )^2", 1480, 600, 170, "g", BR, a, "center"))
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 300)
    E.frase(c, t, C["s02.a"] + 1.0, [("montar", "i", 96), ("os", "i", 96), ("quadrados", "g", 104, COR)], XE, 450)
    E.frase(c, t, C["s02.b"], [("achar", "i", 90), ("centro", "g", 96), ("e", "i", 90), ("raio", "g", 96, COR)], XE, 600)
    E.frase(c, t, C["s02.c"], [("+", "g", 84, COR), ("atalho", "g", 84), ("de", "i", 84), ("prova", "i", 84)], XE, 750)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("vai", "i", 84, TINTA, C["s03"] + 0.2), ("usar", "i", 84, TINTA, C["s03"] + 0.4),
                   ("duas", "g", 80, COR, C["s03.a"]), ("coisas", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 200, "center")
    x, w = 230, 1460
    for k, y in (("s03.b", 270), ("s03.c", 580)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 270, p, prog_=p)
    k = C["s03.b"]
    E.frase(c, t, k, [("a", "i", 56, TINTA2), ("equação", "i", 56, TINTA2), ("reduzida", "g", 56, TINTA2)], x + 60, 340)
    conta_em(c, t, k + 0.6, red("(x − a)^2", "(y − b)^2", "r^2"), x + 60, 450, 80)
    E.foco(c, t, k + 5.5, 0.4, lambda a: E.pilula(c, "centro (a, b)", x + 1120, 360, 42, "g", fundo=TINTA, a=a))
    E.foco(c, t, k + 6.5, 0.4, lambda a: E.pilula(c, "raio r", x + 1120, 460, 42, "g", fundo=DIST, a=a))
    k = C["s03.c"]
    E.frase(c, t, k, [("o", "i", 56, TINTA2), ("quadrado", "i", 56, TINTA2), ("da", "i", 56, TINTA2), ("diferença", "g", 56, TINTA2)], x + 60, 650)
    conta_em(c, t, k + 0.6, [("(p − q)^2 = p^2 ", TINTA), ("− 2pq", COR), (" + q^2", TINTA)], x + 60, 760, 76)
    E.frase(c, t, k + 6.0, [("na", "i", 50, TINTA2), ("soma:", "i", 50, TINTA2)], x + 60, 830)
    conta_em(c, t, k + 6.6, [("(p + q)^2 = p^2 ", TINTA), ("+ 2pq", COR), (" + q^2", TINTA)], x + 280, 830, 54)
    E.frase(c, t, C["s04"] - 2.6, ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 960, "center", passo=0.1)


# ---------------- de onde vem ----------------
def b_origem(c, t, C, b):
    E.frase(c, t, C["s04"], ps("de onde vem uma equação dessas?", "i", 60, TINTA2), XE, 170, passo=0.1)
    conta_em(c, t, C["s04.a"], [("(x − 2)^2", DX)], XE, 300, 72)
    conta_em(c, t, C["s04.b"], [(" = x^2 − 4x + 4", DX)], XE + larg([("(x − 2)^2", 0)], 72), 300, 72)
    conta_em(c, t, C["s04.c"], [("(y + 1)^2", DY)], XE, 420, 72)
    conta_em(c, t, C["s04.d"], [(" = y^2 + 2y + 1", DY)], XE + larg([("(y + 1)^2", 0)], 72), 420, 72)
    if t < C["s05"]:
        return
    conta_em(c, t, C["s05.a"] - 1.2, [("x^2 − 4x + 4", DX), (" + ", TINTA), ("y^2 + 2y + 1", DY), (" = ", TINTA), ("9", DIST)], XE, 570, 66)
    E.frase(c, t, C["s05.b"] - 1.0, ps("− 9 nos dois lados", "i", 46, TINTA2), XE + 40, 650, passo=0.08)
    conta_em(c, t, C["s05.b"], [("4", DX), (" + ", TINTA), ("1", DY), (" − ", TINTA), ("9", DIST), (" = −4", TINTA)], XE + 620, 650, 60)
    eqn(c, t, C["s05.c"], EQ_ABERTA, XE, 800, 80, caixa=C["s05.c"] + 0.8)
    E.frase(c, t, C["s05.c"] + 1.4, ps("a do começo", "i", 50, TINTA2), XE + larg(EQ_ABERTA, 80) + 70, 800, passo=0.1)
    E.frase(c, t, C["s05.d"], [("a", "i", 58), ("da", "i", 58), ("aula", "i", 58), ("anterior,", "i", 58), ("com", "i", 58), ("os", "i", 58),
                               ("parênteses", "g", 58, COR), ("abertos", "g", 58, COR)], XE, 950, passo=0.1)


# ---------------- o método ----------------
def b_metodo(c, t, C, b):
    def s06():
        E.frase(c, t, C["s06.a"], [("o", "i", 80), ("caminho", "i", 80), ("contrário", "g", 80, COR)], W / 2, 300, "center")
        E.foco(c, t, C["s06.a"] + 0.6, 0.5, lambda a: conta(c, [("x^2 − 4x + 4", DX), ("   →   ", TINTA2), ("(x − 2)^2", DX)], W / 2, 450, 72, a, "center"))
        E.frase(c, t, C["s06.b"], [("completar", "g", 110, COR), ("quadrados", "g", 110, COR)], W / 2, 650, "center")
        for i in range(3):
            cx = W / 2 + (i - 1) * 220
            t0 = C["s06.c"] + i * 0.25
            E.foco(c, t, t0, 0.5, lambda a, cx=cx, i=i, t0=t0: (E.bola(c, cx, 840, 74 * ease_back(prog(t, t0, 0.5)), a=a),
                                                               centro(c, str(i + 1), cx, 868, 80, "g", BR, a)), blur=0)
    E.saida(c, t, C["s07"] - 0.1, s06)

    def s07():
        passo_n(c, t, C["s07.a"], 1, "junte e leve o número solto")
        conta_em(c, t, C["s07.a"] + 0.6, EQ_ABERTA, XE, 380, 72)
        E.foco(c, t, C["s07.a"] + 2.2, 0.5, lambda a: conta(c, [("x^2 − 4x", DX), (" + ", TINTA), ("y^2 + 2y", DY), (" − 4 = 0", TINTA)], XE, 520, 72, a))
        E.frase(c, t, C["s07.b"], ps("+ 4 nos dois lados", "i", 48, TINTA2), XE + 40, 610, passo=0.08)
        eqn(c, t, C["s07.c"], [("x^2 − 4x", DX), (" + ", TINTA), ("y^2 + 2y", DY), (" = ", TINTA), ("4", DIST)], XE, 760, 90, caixa=C["s07.c"] + 1.2)
    E.saida(c, t, C["s08"] - 0.1, s07)

    xw = larg([("x^2 − 4x ", 0)], 90)
    def s08():
        passo_n(c, t, C["s08.a"], 2, "complete cada quadrado")
        conta_em(c, t, C["s08.a"] + 0.4, [("x^2 − 4x", DX)], XE, 380, 90)
        falta(c, t, C["s08.b"], XE + xw, 300, 150, 110, DX)
        E.foco(c, t, C["s08.b"] + 0.4, 0.4, lambda a: centro(c, "?", XE + xw + 75, 382, 80, "g", DX, a * (1 - ep(t, C["s08.f"], 0.3))))
        if t >= C["s08.c"]:
            q = pulso(t, C["s08.c"], 2.0)
            c.drawCircle(XE + larg([("x^2 − ", 0)], 90) + 30, 350, 54, M.paint(COR, q, stroke=5))
        conta_em(c, t, C["s08.c"] + 0.2, [("o número do x: ", TINTA2), ("−4", DX)], XE, 540, 60)
        conta_em(c, t, C["s08.d"], [("metade: ", TINTA2), ("−4 ÷ 2 = −2", DX)], XE, 650, 60)
        conta_em(c, t, C["s08.e"], [("ao quadrado: ", TINTA2), ("(−2)^2 = 4", DX)], XE, 760, 60)
        E.foco(c, t, C["s08.f"], 0.4, lambda a: E.formula(c, "+ 4", XE + xw + 10, 382, 90, "g", DX, a))
        eqn(c, t, C["s08.f"] + 0.4, [("x^2 − 4x + 4", DX), (" = ", DX), ("(x − 2)^2", DX)], XE, 920, 80, caixa=C["s08.f"] + 1.4)
    E.saida(c, t, C["s09"] - 0.1, s08)

    def s09():
        E.frase(c, t, C["s09"], [("por", "i", 72), ("que", "i", 72), ("a", "i", 72), ("metade?", "g", 72, COR)], XE, 220)
        conta_em(c, t, C["s09"] + 0.8, [("(x − 2)^2 = x^2 ", DX), ("− 2 · x · 2", COR), (" + 4", DX)], XE, 400, 84)
        E.frase(c, t, C["s09.a"], ps("o termo do meio: 2 · x · o número de dentro", "i", 52, TINTA2), XE, 500, passo=0.08)
        conta_em(c, t, C["s09.b"], [("4x", COR), (" = 2 · ", TINTA), ("2", DX), ("x", TINTA)], XE, 660, 84)
        E.frase(c, t, C["s09.b"] + 1.2, [("o", "i", 56, TINTA2), ("4", "g", 56), ("é", "i", 56, TINTA2), ("o", "i", 56, TINTA2), ("dobro", "g", 56, COR)], XE + 560, 660)
        conta_em(c, t, C["s09.c"], [("4 ÷ 2 = ", TINTA), ("2", DX)], XE, 820, 84)
        E.frase(c, t, C["s09.c"] + 1.2, ps("o número de dentro do parêntese", "i", 52, TINTA2), XE + 430, 820, passo=0.08)
    E.saida(c, t, C["s10"] - 0.1, s09)

    yw = larg([("y^2 + 2y ", 0)], 90)
    def s10():
        E.frase(c, t, C["s10"], [("no", "i", 72), ("y", "g", 72, DY), ("é", "i", 72), ("igual", "i", 72)], XE, 220)
        conta_em(c, t, C["s10"] + 0.5, [("y^2 + 2y", DY)], XE, 380, 90)
        falta(c, t, C["s10"] + 1.0, XE + yw, 300, 150, 110, DY)
        E.foco(c, t, C["s10"] + 1.4, 0.4, lambda a: centro(c, "?", XE + yw + 75, 382, 80, "g", DY, a * (1 - ep(t, C["s10.c"], 0.3))))
        conta_em(c, t, C["s10.a"], [("metade: ", TINTA2), ("2 ÷ 2 = 1", DY)], XE, 560, 64)
        conta_em(c, t, C["s10.b"], [("ao quadrado: ", TINTA2), ("1^2 = 1", DY)], XE, 680, 64)
        E.foco(c, t, C["s10.c"], 0.4, lambda a: E.formula(c, "+ 1", XE + yw + 10, 382, 90, "g", DY, a))
        eqn(c, t, C["s10.c"] + 0.4, [("y^2 + 2y + 1", DY), (" = ", DY), ("(y + 1)^2", DY)], XE, 860, 80, caixa=C["s10.c"] + 1.4)
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return

    passo_n(c, t, C["s11.a"], 3, "some na direita também", size=60)
    ESQ = [("x^2 − 4x ", DX), ("+ 4", DX), (" + ", TINTA), ("y^2 + 2y ", DY), ("+ 1", DY), (" = ", TINTA)]
    we = larg(ESQ, 62)
    y1 = 360

    def linha_esq():
        conta_em(c, t, C["s11.a"] + 0.5, ESQ, XE, y1, 62)
        conta_em(c, t, C["s11.a"] + 0.5, [("4", DIST)], XE + we, y1, 62)
        wq = larg([("4", 0)], 62)
        conta_em(c, t, C["s11.b"], [(" + 4", DX)], XE + we + wq, y1, 62)
        conta_em(c, t, C["s11.b"] + 0.5, [(" + 1", DY)], XE + we + wq + larg([(" + 4", 0)], 62), y1, 62)
        conta_em(c, t, C["s11.c"], [("4 + 4 + 1 = ", TINTA), ("9", DIST)], XE, y1 + 120, 62)
    linha_esq()
    eqn(c, t, C["s11.d"], red("(x − 2)^2", "(y + 1)^2", "9"), XE, 650, 70, caixa=C["s11.d"] + 1.0)
    E.frase(c, t, C["s11.e"], [("centro", "i", 58)], XE, 800)
    par_em(c, t, C["s11.e"] + 0.4, "2", "−1", XE + 220, 800, 58)
    E.frase(c, t, C["s11.f"], [("raio", "i", 58), ("3", "g", 58, DIST)], XE + 560, 800)
    if t >= C["s11.e"] - 0.4:
        eixos(c, t, C["s11.e"] - 0.4, PC, [-2, 2, 4, 6], [-4, -2, 2], size=30)
        centro_c(c, t, C["s11.e"] + 0.3, PC, 2, -1)
        circ(c, t, C["s11.f"], PC, 2, -1, 3)
        if t >= C["s11.f"] + 0.6:
            seg(c, t, C["s11.f"] + 0.6, PC, (2, -1), (2, 2), DIST, 0.6, 7)
            lado_txt(c, t, C["s11.f"] + 1.0, PC, (2, -1), (2, 2), "3", (3, 0), DIST, 46)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 84, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], [("completar", "i", 58), ("só", "g", 58, ERRADO), ("do", "i", 58), ("lado", "i", 58), ("esquerdo", "i", 58)], XE + 380, 200)
    # a balança: esquerda completa, direita só com o 4
    certo = ep(t, C["s12.e"], 0.8)
    inc = 0.0
    if t >= C["s12.d"]:
        inc = -0.8 * ep(t, C["s12.d"], 0.7) * (1 - certo)
    dir_ = "4 + 4 + 1" if t >= C["s12.e"] else "4"
    E.foco(c, t, C["s12.a"] + 0.6, 0.6, lambda a: E.balanca(c, 960, 560, "(x − 2)^2 + (y + 1)^2", dir_, inc, a, size=50, larg_braco=900))
    def baixo():
        E.frase(c, t, C["s12.b"], [("deixa", "i", 54), ("só", "i", 54), ("o", "i", 54), ("4", "g", 54, ERRADO), ("na", "i", 54), ("direita", "i", 54)], XE, 950)
        E.saida(c, t, C["s12.d"], lambda: conta_em(c, t, C["s12.c"], [("raio = r{4} = 2", ERRADO)], 1180, 950, 60))
        E.frase(c, t, C["s12.d"], [("muda", "g", 60, ERRADO), ("a", "i", 60), ("equação", "i", 60)], 1180, 950)
    E.saida(c, t, C["s12.e"], baixo)
    if t >= C["s12.e"]:
        E.frase(c, t, C["s12.e"] + 0.2, [("o", "i", 62), ("que", "i", 62), ("entra", "g", 62, CERTO), ("de", "i", 62), ("um", "i", 62), ("lado", "i", 62),
                                         ("entra", "g", 62, CERTO), ("do", "i", 62), ("outro", "i", 62)], W / 2, 960, "center", passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    eq_esc = [("x^2", DX_ESC), (" + ", BR), ("y^2", DY_ESC), (" − 4x", DX_ESC), (" + 2y", DY_ESC), (" − 4 = 0", BR)]

    def s13():
        E.frase(c, t, C["s13"], ps("o atalho", "i", 66, CLARO), W / 2, 160, "center")
        E.foco(c, t, C["s13.a"], 0.5, lambda a: conta(c, eq_esc, W / 2, 300, 84, a, "center"))
        E.frase(c, t, C["s13.b"], [("centro:", "g", 60, BR), ("a", "i", 60, CLARO), ("metade", "g", 60, BR), ("do", "i", 60, CLARO), ("número", "i", 60, CLARO),
                                   ("da", "i", 60, CLARO), ("letra,", "i", 60, CLARO)], W / 2, 460, "center", passo=0.1)
        E.frase(c, t, C["s13.b"] + 2.6, [("com", "i", 60, CLARO), ("o", "i", 60, CLARO), ("sinal", "i", 60, CLARO), ("trocado", "g", 60, BR)], W / 2, 550, "center")
        E.foco(c, t, C["s13.c"], 0.5, lambda a: conta(c, [("−4x  →  ", CLARO), ("x = 2", DX_ESC)], 640, 720, 80, a, "center"))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: conta(c, [("+2y  →  ", CLARO), ("y = −1", DY_ESC)], 1280, 720, 80, a, "center"))
        E.foco(c, t, C["s13.d"] + 1.2, 0.5, lambda a: E.pilula(c, "centro (2, −1)", W / 2, 880, 60, "g", fundo=COR, a=a))
    E.saida(c, t, C["s14"] - 0.1, s13)

    def s14():
        E.frase(c, t, C["s14"], [("e", "i", 66, CLARO), ("o", "i", 66, CLARO), ("raio", "g", 66, BR)], W / 2, 160, "center")
        E.foco(c, t, C["s14.a"], 0.5, lambda a: E.formula(c, "r^2 = 2^2 + (−1)^2 − (−4)", W / 2, 320, 84, "g", BR, a, "center"))
        E.frase(c, t, C["s14.a"] + 1.4, ps("quadrados do centro, menos o número solto", "i", 50, CLARO), W / 2, 410, "center", passo=0.08)
        E.foco(c, t, C["s14.b"], 0.5, lambda a: conta(c, [("2^2 = 4", DX_ESC), ("     ", BR), ("(−1)^2 = 1", DY_ESC)], W / 2, 540, 70, a, "center"))
        E.foco(c, t, C["s14.c"], 0.5, lambda a: conta(c, [("4 + 1 = 5", BR)], W / 2, 650, 70, a, "center"))
        E.foco(c, t, C["s14.d"], 0.5, lambda a: conta(c, [("5 − (−4) = 5 + 4 = 9", BR)], W / 2, 760, 70, a, "center"))
        E.foco(c, t, C["s14.e"], 0.5, lambda a: (E.bola(c, W / 2, 900, 100 * ease_back(prog(t, C["s14.e"], 0.5)), a=a),
                                                E.formula(c, "r = 3", W / 2, 922, 62, "g", BR, a, "center")))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"], [("por", "i", 66, CLARO), ("que", "i", 66, CLARO), ("funciona", "g", 66, BR)], W / 2, 170, "center")
    E.frase(c, t, C["s15.a"], [("os", "i", 60, CLARO), ("mesmos", "i", 60, CLARO), ("3", "g", 60, BR), ("passos,", "i", 60, CLARO), ("de", "i", 60, CLARO),
                               ("uma", "i", 60, CLARO), ("vez", "g", 60, BR)], W / 2, 300, "center")
    E.frase(c, t, C["s15.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 62, CLARO), ("número", "i", 62, CLARO), ("na", "i", 62, CLARO), ("frente", "i", 62, CLARO),
                               ("do", "i", 62, CLARO), ("x²", "g", 62, BR)], W / 2, 480, "center", passo=0.1)
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.formula(c, "2x^2 + 2y^2 + …", W / 2, 640, 84, "g", CLARO, a, "center"))
    E.foco(c, t, C["s15.d"], 0.5, lambda a: (E.caixa_pontilhada(c, W / 2 - 400, 740, 800, 150, a, BR),
                                            E.formula(c, "÷ 2 antes", W / 2, 845, 84, "g", BR, a, "center")))


# ---------------- questão ----------------
EQ_Q = [("x^2", DX), (" + ", TINTA), ("y^2", DY), (" + 8x", DX), (" − 6y", DY), (" = 0", TINTA)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 220)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: conta(c, [(s, TINTA) for s, _ in EQ_Q], W / 2, 450, 100, a, "center"))
    E.frase(c, t, C["s16.b"], [("centro?", "g", 80, COR), ("raio?", "g", 80, COR)], W / 2, 620, "center")
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=W / 2, cy=830, r=62)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    conta_em(c, t, C["s18"] - 3, EQ_Q, XE, 200, 66)

    def s18():
        E.frase(c, t, C["s18.a"], [("sem", "i", 56), ("número", "i", 56), ("solto:", "i", 56), ("a", "i", 56), ("direita", "i", 56), ("é", "i", 56)], XE, 330)
        conta_em(c, t, C["s18.a"] + 1.4, [("0", DIST)], XE + 640, 330, 64)
        E.frase(c, t, C["s18.b"], [("no", "i", 56), ("x:", "g", 56, DX)], XE, 470)
        conta_em(c, t, C["s18.b"] + 0.4, [("8 ÷ 2 = 4", DX), ("     ", TINTA), ("4^2 = 16", DX)], XE + 160, 470, 64)
        E.frase(c, t, C["s18.c"], [("no", "i", 56), ("y:", "g", 56, DY)], XE, 600)
        conta_em(c, t, C["s18.c"] + 0.4, [("−6 ÷ 2 = −3", DY), ("     ", TINTA), ("(−3)^2 = 9", DY)], XE + 160, 600, 64)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], ps("+ 16 e + 9 nos dois lados", "i", 48, TINTA2), XE, 300, passo=0.08)
    eqn(c, t, C["s19.a"], red("(x + 4)^2", "(y − 3)^2", "25"), XE, 430, 70, caixa=C["s19.a"] + 1.0)
    E.frase(c, t, C["s19.b"], [("centro", "i", 58)], XE, 580)
    par_em(c, t, C["s19.b"] + 0.4, "−4", "3", XE + 220, 580, 58)
    E.frase(c, t, C["s19.c"], [("raio", "i", 58), ("5", "g", 58, DIST)], XE + 560, 580)
    E.frase(c, t, C["s19.d"], [("atalho:", "i", 54, TINTA2)], XE, 730)
    conta_em(c, t, C["s19.d"] + 0.4, [("16", DX), (" + ", TINTA), ("9", DY), (" − 0 = ", TINTA), ("25", DIST)], XE + 210, 730, 64)
    ok(c, t, C["s19.d"] + 1.8, XE + 720, 708)
    eixos(c, t, C["s19.a"], PQ, [-6, -4, -2, 2], [3, 9], size=30)
    centro_c(c, t, C["s19.b"] + 0.3, PQ, -4, 3, lado=(-1, 1))
    circ(c, t, C["s19.c"], PQ, -4, 3, 5)
    if t >= C["s19.c"] + 0.6:
        seg(c, t, C["s19.c"] + 0.6, PQ, (-4, 3), (-4, 8), DIST, 0.6, 7)
        lado_txt(c, t, C["s19.c"] + 1.0, PQ, (-4, 3), (-4, 8), "5", (-2, 5), DIST, 46)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s20.a", [("metade", "g", 78, COR), ("do", "i", 78), ("número", "i", 78), ("da", "i", 78), ("letra,", "i", 78), ("ao", "i", 78),
                            ("quadrado", "g", 78)]),
                 ("s20.b", [("o", "i", 78), ("que", "i", 78), ("entra", "g", 78, COR), ("de", "i", 78), ("um", "i", 78), ("lado", "i", 78), ("entra", "g", 78, COR),
                            ("do", "i", 78), ("outro", "i", 78)]))
        for i, (k, partes) in enumerate(itens):
            y = 460 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 250)
    E.frase(c, t, C["s21.a"], [("ponto:", "g", 70, COR), ("dentro,", "i", 70), ("fora", "i", 70), ("ou", "i", 70), ("em", "i", 70), ("cima?", "i", 70)], XE, 420)
    E.frase(c, t, C["s21.b"], [("reta:", "g", 70, COR), ("corta,", "i", 70), ("encosta", "i", 70), ("ou", "i", 70), ("passa", "i", 70), ("longe?", "i", 70)], XE, 560)
    E.frase(c, t, C["s21.c"], [("a", "i", 80), ("conta", "i", 80), ("do", "i", 80), ("delta", "g", 90, COR)], XE, 720)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 250, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(560, 275, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, origem=b_origem, metodo=b_metodo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
