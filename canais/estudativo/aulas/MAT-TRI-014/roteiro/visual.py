"""Visual — Estudativo · MAT-TRI-014: mexer na onda, y = a + b · cos(cx) (em y = 1 + 2 cos(2x): máximo 3, mínimo −1, período π).
Segue MAT-TRI-011 (gráficos): eixo x (ângulo) em índigo e eixo y em preto, régua de radianos embaixo do gráfico; a onda do
cosseno em petróleo (ADJ) e a do seno em âmbar; a onda de antes fica apagada ao fundo; imagem = barra preta em pé no eixo y.
Cada letra tem uma cor e uma marca que a acompanha na tela inteira:
    á = âmbar (#D98A00): empurra a onda; a LINHA DO MEIO tracejada em âmbar (y = a)
    bê = índigo (E.COR): estica; a seta da amplitude, do meio até o topo, em índigo
    cê = magenta (#C0187C): aperta; o colchete do período em magenta
Resposta na pílula; erro em vermelho, certo em verde; atalho no palco escuro (cartões das três contas).
A figura não mente: as curvas são as funções ditas, desenhadas de verdade; as transformações animam o parâmetro (b de 1 a 2,
a de 0 a 1, c de 1 a 2), e a onda muda no lugar.
Peças locais: cf() (fórmula com cores por parte), formula_abc() (a forma geral colorida, com a posição de cada letra), eixos(),
curva_a(), barra_y(), periodo(), meio() (linha do meio), amplitude(), cartao(), resp(). Todo instante vem de C[...]."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-014_mexer_na_onda.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("forma", "be", "a", "ce", "juntando", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
ADJ, OPO, ADJ_ESC = "#0E9AA7", AMBAR, "#3CC7D3"
LA, LB, LC = AMBAR, E.COR, "#C0187C"     # as cores do á, do bê e do cê
LA_ESC, LB_ESC, LC_ESC = "#FFB020", CLARO, "#FF6FB5"
ENT, SAI = E.COR, TINTA
PI = math.pi
cos, sen = math.cos, math.sin
assert 1 + 2 == 3 and 1 - 2 == -1 and abs(2 * PI / 2 - PI) < 1e-12 and 2 + 3 == 5 and 2 - 3 == -1 and abs(2 * PI / 4 - PI / 2) < 1e-12
assert 3 + 2 == 5 and 3 - 2 == 1 and abs(cos(-2 * 1.234) - cos(2 * 1.234)) < 1e-12


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def _w(s, size, est="g"):
    return E.formula(None, s, 0, 0, size, est, a=0)


def cf(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """fórmula numa linha com partes coloridas: [(texto, cor), ...]; devolve a lista com o x do centro de cada parte"""
    ws = [_w(s, size, est) for s, _ in partes]
    w = sum(ws)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    centros = []
    for (s, cor), wi in zip(partes, ws):
        if a > 0 and c is not None:
            E.formula(c, s, xx, y, size, est, cor, a)
        centros.append(xx + wi / 2)
        xx += wi
    return centros


def cf_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: cf(c, partes, x, y, size, a, align))


def resp(c, t, t0, partes, cx, cy, size=66, alto=1.75, cor=None):
    if isinstance(partes, str):
        partes = [(partes, BR)]

    def f(a):
        w = sum(_w(s, size) for s, _ in partes) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        cf(c, partes, cx, cy + size * 0.36, size, a, "center")
    E.foco(c, t, t0, 0.5, f)


def geral(tinta=TINTA, a_="a", b_="b", c_="c", fn="cos", esc=False):
    """y = a + b · cos(cx), com as letras nas cores delas"""
    la, lb, lc = (LA_ESC, LB_ESC, LC_ESC) if esc else (LA, LB, LC)
    return [("y = ", tinta), (a_, la), (" + ", tinta), (b_, lb), (f" · {fn}(", tinta), (c_, lc), ("x)", tinta)]


MARCAS = [(0, "0"), (PI / 2, "f{π}{2}"), (PI, "π"), (3 * PI / 2, "f{3π}{2}"), (2 * PI, "2π")]


def eixos(c, t, P, tx, ty=None, tl=None, marcas=MARCAS, ys=(1, -1), escuro=False, size=50, grade=True):
    if t < tx:
        return
    ty = tx if ty is None else ty
    x, y, w, h = P.caixa
    tinta = BR if escuro else SAI
    ent = CLARO if escuro else ENT
    if grade:
        q = ep(t, tx, 0.8) * (0.25 if escuro else 1)
        for v, _ in marcas:
            M.line(c, P.x(v), y, P.x(v), y + h, CLARO if escuro else FIO, q, 2)
        for v in ys:
            M.line(c, x, P.y(v), x + w, P.y(v), CLARO if escuro else FIO, q, 2)
    M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ent, 1.0, 6, 24, ep(t, tx, 0.7))
    E.foco(c, t, tx + 0.5, 0.4, lambda b: E.escreve(c, "x", x + w + 24, P.oy + 52, 50, "i", ent, b))
    for v, _ in marcas:
        X = P.x(v)
        E.foco(c, t, tx + 0.3, 0.4, lambda b, X=X: M.line(c, X, P.oy - 10, X, P.oy + 10, ent, b, 4), sobe=4)
    if t >= ty:
        M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, tinta, 1.0, 6, 24, ep(t, ty, 0.7))
        E.foco(c, t, ty + 0.5, 0.4, lambda b: E.escreve(c, "y", P.ox + 22, y - 10, 50, "i", tinta, b))
        for v in ys:
            Y = P.y(v)
            s = E._num(v).replace("-", "−")
            E.foco(c, t, ty + 0.3, 0.4, lambda b, Y=Y, s=s: (M.line(c, P.ox - 10, Y, P.ox + 10, Y, tinta, b, 4),
                                                            E.escreve(c, s, P.ox - 22 - E.larg(s, "b", size), Y + size * 0.36, size, "b", tinta, b)))
    if tl is not None:
        for i, (v, rad) in enumerate(marcas):
            X = P.x(v)
            E.foco(c, t, tl + 0.06 * i, 0.4, lambda b, X=X, rad=rad: E.formula(c, rad, X, y + h + 62, size, "g", ent, b, "center"))


def curva_a(c, t, t0, P, f, a_, b_, d=1.2, cor=None, alfa=1.0, largura=8, tracejada=False):
    if alfa <= 0 or t < t0:
        return
    if alfa < 1:
        pt = skia.Paint(); pt.setAlphaf(alfa); c.saveLayer(None, pt)
    E.curva(c, t, t0, P, f, a_, b_, d=d, cor=cor, largura=largura, tracejada=tracejada)
    if alfa < 1:
        c.restore()


def barra_y(c, t, t0, P, a_, b_, cor=SAI, d=0.8, larg=14, r=15):
    p = ease_out(prog(t, t0, d))
    if p <= 0:
        return
    y0, y1 = P.y(a_), P.y(b_)
    m = (y0 + y1) / 2
    M.line(c, P.ox, lerp(m, y0, p), P.ox, lerp(m, y1, p), cor, 0.85, larg)
    q = ep(t, t0 + d * 0.6, 0.3)
    for Y in (y0, y1):
        c.drawCircle(P.ox, Y, r, M.paint(cor, q))


def periodo(c, t, t0, P, x0, x1, yv, rot, cor=LC, size=54, d=0.6, a=1.0):
    if t < t0 or a <= 0:
        return
    p = ease_out(prog(t, t0, d))
    Y = P.y(yv)
    if a < 1:
        pt = skia.Paint(); pt.setAlphaf(a); c.saveLayer(None, pt)
    E.chave(c, P.x(x0), P.x(x1), Y, cor, p, -26, 6)
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda b: E.formula(c, rot, (P.x(x0) + P.x(x1)) / 2, Y - 50, size, "g", cor, b, "center"))
    if a < 1:
        c.restore()


def meio(c, t, t0, P, yv, rot=None, cor=LA, size=46, a=1.0):
    """a linha do meio da onda, tracejada na cor do á"""
    if t < t0 or a <= 0:
        return
    x, y, w, h = P.caixa
    M.line(c, x, P.y(yv), x + w, P.y(yv), cor, a, 5, dash=E.TRACO, progress=ep(t, t0, 0.8))
    if rot:
        E.foco(c, t, t0 + 0.4, 0.4, lambda b: E.formula(c, rot, x + w + 30, P.y(yv) + 16, size, "g", cor, b * a))


def amplitude(c, t, t0, P, xv, y0, y1, rot=None, cor=LB, size=46, a=1.0, lado=1):
    """seta da amplitude: do meio da onda (y0) até o topo (y1), em x = xv"""
    if t < t0 or a <= 0:
        return
    q = ep(t, t0, 0.6)
    M.arrow(c, P.x(xv), P.y(y0), P.x(xv), P.y(y1), cor, a, 7, 26, q)
    if rot:
        E.foco(c, t, t0 + 0.4, 0.4, lambda b: E.formula(c, rot, P.x(xv) + lado * 24, (P.y(y0) + P.y(y1)) / 2 + 16, size, "g", cor, b * a,
                                                         "left" if lado > 0 else "right"))


def ponto(c, t, t0, P, xv, yv, rot=None, cor=TINTA, lado=(1, -1), size=46):
    E.ponto(c, t, t0, P, xv, yv, None, cor=cor, r=14)
    if rot:
        X, Y = P(xv, yv)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.formula(c, rot, X + lado[0] * 28, Y + lado[1] * 36 + 16, size, "g", cor, a,
                                                         "left" if lado[0] > 0 else "right" if lado[0] < 0 else "center"))


# ---------------- gancho ----------------
def gancho_formula(c, a, y=430, size=140):
    partes = [("y = ", TINTA), ("1", LA), (" + ", TINTA), ("2", LB), (" · cos(", TINTA), ("2", LC), ("x)", TINTA)]
    return cf(c, partes, W / 2, y, size, a, "center")


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.foco(c, t, a1, 0.6, lambda a: gancho_formula(c, a))
        xs = gancho_formula(None, 0)
        for i, (k, s, cor) in enumerate(((1, "sobe", LA), (3, "estica", LB), (5, "aperta", LC))):
            tt = b1 + 0.9 * i
            E.foco(c, t, tt, 0.4, lambda a, k=k, cor=cor: M.arrow(c, xs[k], 520, xs[k], 470, cor, a, 5, 18, 1.0))
            E.frase(c, t, tt + 0.1, [(s, "g", 62, cor)], xs[k], 600, "center")
        E.frase(c, t, b1 + 0.2, ps("cada número tem", "i", 58) + [("uma tarefa só", "g", 62)], W / 2, 220, "center", 0.1)
        E.foco(c, t, c1, 0.5, lambda a: cf(c, [("máx 3", TINTA), ("     ", TINTA), ("mín −1", TINTA), ("     ", TINTA), ("período π", LC)],
                                           W / 2, 850, 76, a, "center"))
        E.frase(c, t, c1 + 0.4, ps("em segundos", "i", 54, TINTA2), W / 2, 960, "center", 0.08)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 600, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, ta + 1.4, ps("o que", "i", 80) + [("cada número", "g", 90, COR)], XE, 450, passo=0.14)
        E.frase(c, t, ta + 2.6, ps("faz com", "i", 80) + [("a onda", "g", 90, ADJ)], XE, 600, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 585, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 670, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
PL = E.Plano(1000, 340, 740, 280, -0.3, 2 * PI + 0.4, -1.5, 1.5)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 190, 700, 120, "i", TINTA, a))
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, 880, 150, 960, 820, p, prog_=p)
    eixos(c, t, PL, C["s03.b"] + 0.2, tl=C["s03.b"] + 0.4, marcas=[(PI, "π"), (2 * PI, "2π")], size=42)
    curva_a(c, t, C["s03.b"] + 0.6, PL, cos, 0, 2 * PI + 0.3, d=1.4, cor=ADJ)
    E.frase(c, t, C["s03.b"] + 0.3, ps("o gráfico do", "i", 52) + [("cosseno:", "g", 56, ADJ)], 940, 230, "left", 0.08)
    E.frase(c, t, C["s03.b"] + 2.2, ps("começa no alto, de", "i", 50) + [("−1 a 1,", "g", 54)] + ps("repete a cada", "i", 50) + [("2π", "g", 54)],
            940, 720, "left", 0.07)
    E.frase(c, t, C["s03.c"], ps("número na frente", "i", 52) + [("estica a altura", "g", 56, COR)], 940, 840, "left", 0.08)
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), XE, 1000, "left", 0.12)


# ---------------- a forma geral ----------------
def b_forma(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    E.frase(c, t, C["s04"] + 0.2, ps("a forma geral", "i", 66, TINTA2), W / 2, 200, "center", 0.1)
    E.foco(c, t, a4, 0.6, lambda a: cf(c, geral(), W / 2, 460, 150, a, "center"))
    xs = cf(None, geral(), W / 2, 460, 150, 0, "center")
    for i, (k, s, cor) in enumerate(((1, "sobe ou", LA), (3, "estica", LB), (5, "aperta", LC))):
        tt = b4 + 0.6 + 0.6 * i
        E.foco(c, t, tt, 0.4, lambda a, k=k, cor=cor: M.arrow(c, xs[k], 560, xs[k], 500, cor, a, 5, 18, 1.0))
        E.frase(c, t, tt + 0.1, [(s, "g", 54, cor)], xs[k], 640, "center")
    E.frase(c, t, b4 + 0.7, [("desce", "g", 54, LA)], xs[1], 700, "center")
    E.frase(c, t, b4, ps("três letras,", "i", 60) + [("três tarefas", "g", 64)], W / 2, 770, "center", 0.1)
    E.frase(c, t, c4, ps("vale igual para o", "i", 54) + [("seno:", "g", 58, OPO)], 560, 940, "center", 0.1)
    E.foco(c, t, c4 + 0.9, 0.5, lambda a: cf(c, geral(fn="sen"), 1300, 940, 70, a, "center"))


# ---------------- o gráfico ----------------
GX, GY, GW, GH = 300, 330, 1380, 560
XF = 2 * PI + 0.9   # fim das curvas: começam no 0, para não cobrir os números do eixo y
PB = E.Plano(GX, GY, GW, GH, -0.4, 2 * PI + 1.3, -2.6, 3.6)


def b_be(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    eixos(c, t, PB, C["s05"] - 0.2, tl=C["s05"], ys=(3, 2, 1, -1, -2))
    k = 1 + ease_io(prog(t, c5, 1.4))  # o bê vai de 1 a 2
    curva_a(c, t, C["s05"], PB, cos, 0, XF, d=1.0, cor=ADJ, alfa=1 - 0.7 * ep(t, c5, 0.4), largura=7)
    if t >= c5:
        E.curva(c, t, c5 - 5, PB, lambda x: k * cos(x), 0, XF, d=0.01, cor=ADJ, largura=9)
    barra_y(c, t, c5 + 1.6, PB, -2, 2)
    amplitude(c, t, d5, PB, 2 * PI, 0, 2, "amplitude" if t < e5 else "amplitude = 2")

    def topo():
        E.frase(c, t, a5, [("bê:", "g", 62, LB)] + ps("o número na frente", "i", 58), XE, 150, "left", 0.1)
        E.frase(c, t, b5, ps("estica", "i", 58) + [("a altura", "g", 64, LB)], XE, 245, "left", 0.1)
        E.foco(c, t, c5, 0.5, lambda a: cf(c, [("y = ", TINTA), ("2", LB), (" · cos x", TINTA)], 1050, 150, 64, a))
        E.frase(c, t, c5 + 1.6, ps("vai de", "i", 54) + [("−2 a 2", "g", 60, SAI)], 1050, 245, "left", 0.1)
    topo()


def b_a(c, t, C, b):
    a6, b6, c6, d6, e6, f6 = (C[f"s06.{k}"] for k in "abcdef")
    eixos(c, t, PB, C["s06"] - 0.3, tl=C["s06"] - 0.3, ys=(3, 2, 1, -1, -2))
    s = ease_io(prog(t, c6, 1.6))  # o á vai de 0 a 1
    if t >= c6:
        curva_a(c, t, c6, PB, lambda x: 2 * cos(x), 0, XF, d=0.01, cor=ADJ, alfa=0.3, largura=6)
    E.curva(c, t, C["s06"] - 0.3, PB, lambda x: s + 2 * cos(x), 0, XF, d=0.01, cor=ADJ, largura=9)
    if t >= c6:  # setas de subida
        q = ep(t, c6, 0.3) * (1 - ep(t, d6, 0.4))
        for xv in (PI / 2, 3 * PI / 2):
            M.arrow(c, PB.x(xv), PB.y(0), PB.x(xv), PB.y(1), LA, q, 5, 20, s)
    ponto(c, t, d6, PB, 0, 3, None, cor=LB)
    ponto(c, t, d6 + 0.3, PB, 2 * PI, 3, "2 → 3", cor=LB, lado=(1, -1))
    ponto(c, t, e6, PB, PI, -1, "−2 → −1", cor=LB, lado=(1, 1))
    meio(c, t, f6, PB, 1, "y = 1")

    def topo():
        E.frase(c, t, a6, [("á:", "g", 62, LA)] + ps("o número somado", "i", 58), XE, 150, "left", 0.1)
        E.frase(c, t, b6, ps("empurra", "i", 56) + [("a onda inteira", "g", 62, LA)] + ps("para cima (ou para baixo)", "i", 54), XE, 245, "left", 0.08)
    E.saida(c, t, c6 - 0.2, topo)
    if t >= c6 - 0.2:
        E.foco(c, t, c6, 0.5, lambda a: cf(c, [("y = ", TINTA), ("1", LA), (" + ", TINTA), ("2", LB), (" · cos x", TINTA)], XE, 160, 70, a))
        E.frase(c, t, c6 + 0.8, ps("cada ponto", "i", 56) + [("sobe 1", "g", 60, LA)], XE + 760, 160, "left", 0.1)
        E.frase(c, t, f6, ps("o meio da onda sobe para", "i", 52) + [("a altura 1", "g", 58, LA)], XE, 260, "left", 0.08)


PC = E.Plano(GX, GY + 40, GW, GH - 80, -0.4, 2 * PI + 1.3, -1.7, 1.7)


def b_ce(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8, e8, f8 = (C[f"s08.{k}"] for k in "abcdef")
    eixos(c, t, PC, C["s07"] - 0.3, tl=C["s07"] - 0.3)
    curva_a(c, t, C["s07"] - 0.1, PC, cos, 0, XF, d=1.0, cor=ADJ, alfa=1 - 0.7 * ep(t, b7, 0.4), largura=7)
    curva_a(c, t, b7 + 0.3, PC, lambda x: cos(2 * x), 0, XF, d=2.4, cor=ADJ, largura=9)
    periodo(c, t, c8, PC, 0, 2 * PI, 1.55, "2π", cor=CINZA, size=46, a=1 - 0.6 * ep(t, d8, 0.4))
    periodo(c, t, c8 + 0.8, PC, 0, PI, 1.2, "π", cor=LC)
    if t >= d8:  # as duas ondas que cabem
        for i, (x0, x1) in enumerate(((0, PI), (PI, 2 * PI))):
            if t >= d8 + 0.4 * i:
                E.curva(c, t, d8 + 0.4 * i, PC, lambda x: cos(2 * x), x0, x1, d=0.6, cor=LC, largura=13)
                E.foco(c, t, d8 + 0.4 * i + 0.3, 0.4, lambda a, x0=x0, x1=x1, i=i: E.bola(c, PC.x((x0 + x1) / 2), PC.y(-1.35), 30, LC, a))
                E.foco(c, t, d8 + 0.4 * i + 0.4, 0.4, lambda a, x0=x0, x1=x1, i=i: centro(c, str(i + 1), PC.x((x0 + x1) / 2), PC.y(-1.35) + 15, 40, "g", BR, a))

    def sete():
        E.frase(c, t, a7, [("cê:", "g", 62, LC)] + ps("multiplica o x lá dentro", "i", 58), XE, 150, "left", 0.1)
        E.foco(c, t, b7, 0.5, lambda a: cf(c, [("cos(", TINTA), ("2", LC), ("x)", TINTA)], XE, 250, 66, a))
        E.frase(c, t, b7 + 0.8, ps("o ângulo anda", "i", 54) + [("2 vezes mais rápido", "g", 58, LC)], XE + 300, 250, "left", 0.08)
        E.frase(c, t, c7, ps("a volta fecha quando", "i", 54, TINTA2) + [("o de dentro do parêntese = 2π", "g", 58)], W / 2, 1010, "center", 0.07)
    E.saida(c, t, a8 - 0.2, sete)
    if t < a8 - 0.2:
        return

    def oito():
        E.foco(c, t, a8, 0.5, lambda a: cf(c, [("2", LC), ("x = 2π", TINTA)], XE, 160, 72, a))
        E.foco(c, t, b8, 0.5, lambda a: cf(c, [("  →  x = π", TINTA)], XE + _w("2x = 2π", 72), 160, 72, a))
        E.frase(c, t, b8 - 0.8, ps("÷ 2 dos dois lados", "i", 44, TINTA2), XE, 245, "left", 0.06)
        E.frase(c, t, c8, ps("o período cai", "i", 56) + [("pela metade", "g", 60, LC)], 1050, 160, "left", 0.1)
    E.saida(c, t, e8 - 0.2, oito)
    if t >= e8 - 0.2:
        E.foco(c, t, e8, 0.5, lambda a: (E.caixa_pontilhada(c, XE - 30, 70, 820, 130, a, LC, prog_=ep(t, e8, 0.6)),
                                         cf(c, [("período = 2π ÷ ", TINTA), ("c", LC)], XE + 10, 160, 72, a)))
        E.frase(c, t, f8, ps("aperta ou alarga,", "i", 54) + [("não mexe na altura", "g", 58, LC)], XE, 280, "left", 0.08)


PJ = E.Plano(GX, GY, GW, GH, -0.4, 2 * PI + 1.3, -1.8, 3.8)


def b_juntando(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    eixos(c, t, PJ, C["s09"] - 0.3, tl=C["s09"] - 0.3, ys=(3, 1, -1))
    f = lambda x: 1 + 2 * cos(2 * x)
    meio(c, t, a9, PJ, 1, "y = 1")
    curva_a(c, t, a9 + 0.2, PJ, f, 0, XF, d=1.6, cor=ADJ, largura=9)
    for i, xv in enumerate((0, PI, 2 * PI)):
        ponto(c, t, b9 + 0.2 * i, PJ, xv, 3, None, cor=LB)
    for i, xv in enumerate((PI / 2, 3 * PI / 2)):
        ponto(c, t, c9 + 0.2 * i, PJ, xv, -1, None, cor=LB)
    periodo(c, t, d9, PJ, 0, PI, 3.45, "π")
    barra_y(c, t, e9, PJ, -1, 3)
    E.foco(c, t, a9, 0.5, lambda a: cf(c, [("y = ", TINTA), ("1", LA), (" + ", TINTA), ("2", LB), (" · cos(", TINTA), ("2", LC), ("x)", TINTA)], XE, 150, 66, a))
    E.foco(c, t, b9, 0.5, lambda a: cf(c, [("máx = ", TINTA), ("1", LA), (" + ", TINTA), ("2", LB), (" = 3", TINTA)], XE, 255, 56, a))
    E.foco(c, t, c9, 0.5, lambda a: cf(c, [("mín = ", TINTA), ("1", LA), (" − ", TINTA), ("2", LB), (" = −1", TINTA)], XE + 470, 255, 56, a))
    E.foco(c, t, d9, 0.5, lambda a: cf(c, [("período = ", TINTA), ("π", LC)], XE + 960, 255, 56, a))
    E.frase(c, t, e9, ps("imagem:", "i", 54) + [("de −1 a 3", "g", 60, SAI)], 1200, 150, "left", 0.1)


# ---------------- erro ----------------
PE = E.Plano(1060, 360, 700, 440, -0.2, 2 * PI + 0.4, -1.6, 1.6)


def b_erro(c, t, C, b):
    a0, b0 = C["s10.a"], C["s10.b"]
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    x = XE
    E.frase(c, t, a0, ps("o erro:", "i", 60) + [("multiplicar o período pelo cê", "g", 60, ERRADO)], x, 190, "left", 0.1)
    E.foco(c, t, b0 - 2.6, 0.5, lambda a: E.formula(c, "2π · 2 = 4π", x, 370, 100, "g", ERRADO, a))
    if t >= b0 + 0.6:
        E.risco(c, x - 10, 390, x + _w("2π · 2 = 4π", 100) + 10, 300, t, b0 + 0.6, ERRADO, 10)
    eixos(c, t, PE, C["s11"] - 0.2, tl=C["s11"], marcas=[(PI, "π"), (2 * PI, "2π")], size=44)
    curva_a(c, t, C["s11"], PE, cos, -0.2, 2 * PI + 0.4, d=1.0, cor=ADJ, alfa=0.35, largura=6)
    curva_a(c, t, b1, PE, lambda v: cos(2 * v), -0.2, 2 * PI + 0.4, d=1.4, cor=ADJ, largura=9)
    periodo(c, t, e1, PE, 0, PI, 1.4, "π", cor=CERTO)
    E.frase(c, t, a1, ps("cê maior: o ângulo", "i", 56) + [("corre mais", "g", 60, LC)], x, 540, "left", 0.1)
    E.frase(c, t, b1, ps("chega a", "i", 56) + [("2π", "g", 60), ("mais cedo", "g", 60, LC)], x, 640, "left", 0.1)
    E.frase(c, t, c1, ps("repete em", "i", 56) + [("menos tempo", "g", 60, LC)], x, 740, "left", 0.1)
    E.frase(c, t, d1, ps("cê maior,", "i", 56) + [("onda mais apertada", "g", 60)], x, 840, "left", 0.1)
    resp(c, t, e1, [("período = 2π ÷ c", BR)], x + 330, 960, 60, cor=CERTO)


# ---------------- atalho (palco escuro) ----------------
def cartao(c, t, t0, x, y, w, h, partes, size=70):
    def f(a):
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26)
        c.drawRRect(rr, M.paint("#FFFFFF", 0.06 * a))
        c.drawRRect(rr, M.paint(CLARO, a, stroke=3))
        cf(c, partes, x + w / 2, y + h / 2 + size * 0.36, size, a, "center")
    E.foco(c, t, t0, 0.5, f)


PA = E.Plano(1130, 330, 640, 420, -0.2, 2 * PI + 0.3, -0.6, 5.8)


def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    a3, b3, c3, d3, e3, f3 = (C[f"s13.{k}"] for k in "abcdef")

    def doze():
        E.frase(c, t, C["s12"] + 0.1, ps("o atalho:", "i", 66, CLARO) + [("três contas", "g", 72, BR)], W / 2, 200, "center", 0.1)
        cartao(c, t, b2, 260, 330, 1400, 160, [("máximo = ", BR), ("a", LA_ESC), (" + ", BR), ("b", LB_ESC)], 84)
        cartao(c, t, c2, 260, 540, 1400, 160, [("mínimo = ", BR), ("a", LA_ESC), (" − ", BR), ("b", LB_ESC)], 84)
        cartao(c, t, d2, 260, 750, 1400, 160, [("período = 2π ÷ ", BR), ("c", LC_ESC)], 84)
    E.saida(c, t, C["s13"] - 0.1, doze)
    if t < C["s13"] - 0.1:
        return

    def treze_a():
        E.frase(c, t, C["s13"] + 0.1, ps("funciona porque o cosseno vai de", "i", 56, CLARO) + [("−1 a 1", "g", 62, BR)], W / 2, 200, "center", 0.08)
        E.foco(c, t, a3 + 2.0, 0.5, lambda a: cf(c, [("topo: ", CLARO), ("a", LA_ESC), (" + ", BR), ("b", LB_ESC), (" · 1", BR)], W / 2, 400, 80, a, "center"))
        E.foco(c, t, a3 + 4.6, 0.5, lambda a: cf(c, [("fundo: ", CLARO), ("a", LA_ESC), (" + ", BR), ("b", LB_ESC), (" · (−1)", BR)], W / 2, 580, 80, a, "center"))
    E.saida(c, t, b3 - 0.2, treze_a)
    if t < b3 - 0.2:
        return

    def treze_b():
        E.frase(c, t, b3, ps("cuidado com o", "i", 58, CLARO) + [("bê negativo", "g", 64, LB_ESC)], XE, 200, "left", 0.1)
        E.foco(c, t, c3, 0.5, lambda a: cf(c, [("y = ", BR), ("3", LA_ESC), (" − ", BR), ("2", LB_ESC), (" · cos x", BR)], XE, 340, 80, a))
        E.frase(c, t, d3, ps("use o bê", "i", 56, CLARO) + [("sem o sinal:", "g", 60, BR)], XE, 470, "left", 0.1)
        E.foco(c, t, d3 + 1.0, 0.5, lambda a: cf(c, [("máx = 3 + 2 = 5", BR)], XE, 570, 62, a))
        E.foco(c, t, d3 + 1.8, 0.5, lambda a: cf(c, [("mín = 3 − 2 = 1", BR)], XE, 660, 62, a))
        E.foco(c, t, d3 + 2.6, 0.5, lambda a: cf(c, [("amplitude = 2", LB_ESC)], XE, 750, 62, a))
        eixos(c, t, PA, c3, tl=c3, marcas=[(PI, "π"), (2 * PI, "2π")], ys=(5, 3, 1), escuro=True, size=42)
        curva_a(c, t, c3 + 0.4, PA, lambda v: 3 + 2 * cos(v), -0.2, 2 * PI + 0.3, d=1.0, cor=CLARO, alfa=0.45, largura=5, tracejada=True)
        curva_a(c, t, e3, PA, lambda v: 3 - 2 * cos(v), -0.2, 2 * PI + 0.3, d=1.4, cor=ADJ_ESC, largura=9)
        meio(c, t, c3 + 0.6, PA, 3, None, cor=LA_ESC)
        E.frase(c, t, e3 + 0.6, ps("o menos", "i", 50, CLARO) + [("vira a onda", "g", 54, BR)] + ps("de cabeça para baixo", "i", 50, CLARO),
                1450, 1010, "center", 0.08)
    E.saida(c, t, f3 - 0.2, treze_b)
    if t >= f3 - 0.2:
        E.frase(c, t, f3, ps("e com o", "i", 60, CLARO) + [("cê negativo?", "g", 66, LC_ESC)], W / 2, 220, "center", 0.1)
        E.frase(c, t, f3 + 1.2, ps("o ângulo só anda para trás, no mesmo ritmo", "i", 54, CLARO), W / 2, 340, "center", 0.07)
        E.foco(c, t, f3 + 3.6, 0.5, lambda a: cf(c, [("cos(", BR), ("−2", LC_ESC), ("x) = cos(", BR), ("2", LC_ESC), ("x)", BR)], W / 2, 530, 90, a, "center"))
        cartao(c, t, f3 + 5.2, 360, 670, 1200, 180, [("período = 2π ÷ ", BR), ("2", LC_ESC), (" = π", BR)], 80)
        E.frase(c, t, f3 + 6.4, ps("no período, use o", "i", 54, CLARO) + [("cê sem o sinal", "g", 60, LC_ESC)], W / 2, 960, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a4, b4 = C["s14.a"], C["s14.b"]
    E.frase(c, t, C["s14"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.foco(c, t, a4, 0.5, lambda a: cf(c, [("y = ", TINTA), ("2", LA), (" + ", TINTA), ("3", LB), (" · sen(", TINTA), ("4", LC), ("x)", TINTA)], XE, 420, 104, a))
    E.frase(c, t, b4, [("máximo,", "g", 70, COR), ("mínimo", "g", 70, COR)] + ps("e", "i", 64) + [("período?", "g", 70, LC)], XE, 640, "left", 0.12)
    E.relogio(c, t, C["s15.a"], 1520, 440, 170)


# ---------------- resposta ----------------
PR = E.Plano(1080, 290, 680, 560, -0.15, PI + 0.3, -1.8, 5.8)


def b_resposta(c, t, C, b):
    a6, b6, c6, d6, e6 = (C[f"s16.{k}"] for k in "abcde")
    f = lambda v: 2 + 3 * sen(4 * v)
    eixos(c, t, PR, C["s16"] + 0.2, tl=C["s16"] + 0.4, marcas=[(PI / 4, "f{π}{4}"), (PI / 2, "f{π}{2}"), (3 * PI / 4, "f{3π}{4}"), (PI, "π")],
          ys=(5, 2, -1), size=44)
    curva_a(c, t, C["s16"] + 0.8, PR, f, 0, PI + 0.3, d=1.6, cor=OPO, largura=8)
    meio(c, t, C["s16"] + 1.6, PR, 2, None)
    for i, xv in enumerate((PI / 8, PI / 8 + PI / 2)):
        ponto(c, t, a6 + 0.2 * i, PR, xv, 5, None, cor=LB)
    for i, xv in enumerate((3 * PI / 8, 3 * PI / 8 + PI / 2)):
        ponto(c, t, b6 + 0.2 * i, PR, xv, -1, None, cor=LB)
    periodo(c, t, d6, PR, PI / 8, PI / 8 + PI / 2, 5.55, "f{π}{2}", size=46)
    barra_y(c, t, e6, PR, -1, 5)
    E.frase(c, t, C["s16"] + 0.1, ps("á = 2, bê = 3, cê = 4", "i", 54, TINTA2), XE, 170, "left", 0.07)
    E.foco(c, t, a6, 0.5, lambda a: cf(c, [("máx = ", TINTA), ("2", LA), (" + ", TINTA), ("3", LB), (" = 5", TINTA)], XE, 320, 72, a))
    E.foco(c, t, b6, 0.5, lambda a: cf(c, [("mín = ", TINTA), ("2", LA), (" − ", TINTA), ("3", LB), (" = −1", TINTA)], XE, 470, 72, a))
    E.foco(c, t, c6, 0.5, lambda a: cf(c, [("período = 2π ÷ ", TINTA), ("4", LC)], XE, 620, 72, a))
    resp(c, t, d6, [("período = f{π}{2}  (90°)", BR)], XE + 380, 780, 62, 2.3, LC)
    E.frase(c, t, e6, ps("imagem:", "i", 58) + [("de −1 a 5", "g", 64, SAI)], XE, 950, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s17.a", [("o á", "g", 66, LA)] + ps("sobe ou desce a onda", "i", 62)),
                 ("s17.b", [("o bê", "g", 66, LB)] + ps("estica a altura", "i", 62)),
                 ("s17.c", [("o cê", "g", 66, LC)] + ps("aperta e", "i", 62) + [("divide o período", "g", 66, LC)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 320, y, "left", 0.1)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, C["s18"] + 0.2, ps("na próxima aula, a onda", "i", 70), XE, 200, passo=0.1)
    E.frase(c, t, a8, [("sai do papel", "g", 84, COR)], XE, 320, passo=0.1)
    E.frase(c, t, b8, ps("a altura da", "i", 62) + [("maré", "g", 70, ADJ)] + ps("num porto", "i", 62), XE, 450, passo=0.1)
    if t >= b8:  # a maré sobe e desce
        p = ease_io(prog(t, b8, 1.6))
        path = skia.Path()
        x0, y0, w, h = 1100, 430, 680, 60
        n = 120
        for i in range(int(n * p) + 1):
            xx = x0 + w * i / n
            (path.moveTo if i == 0 else path.lineTo)(xx, y0 - h * math.cos(2 * math.pi * 1.5 * i / n))
        c.drawPath(path, M.paint(ADJ, 1.0, stroke=8, cap_round=True))
    E.frase(c, t, c8, ps("maré alta, maré baixa e", "i", 56) + [("de quantas em quantas horas", "g", 60, COR)], XE, 580, passo=0.08)
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s18.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1030, 815, p), ep(t, C["s18.d"] + 0.2, 0.4))
    E.frase(c, t, C["s18.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, forma=b_forma, be=b_be, a=b_a, ce=b_ce, juntando=b_juntando, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
