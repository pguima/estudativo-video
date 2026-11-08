"""Visual — Estudativo · MAT-ANA-001: distância entre dois pontos. Primeira aula de Geometria Analítica.

LINGUAGEM VISUAL DA GEOMETRIA ANALÍTICA (as próximas aulas da trilha copiam daqui):
- Herda a de Funções (MAT-FUN-001): plano sempre na metade direita, texto na esquerda; eixo x em índigo, eixo y em preto;
  par ordenado "(x, y)" com o x em índigo e o y em preto (par()); andar no plano com seta: primeiro o corredor (deitado),
  depois o elevador (em pé), com anda().
- Herda as cores dos lados da Trigonometria (MAT-TRI-001) para o triângulo escondido entre dois pontos:
    DX  = petróleo #0E9AA7  o corredor: a diferença dos x (cateto deitado; no palco escuro, DX_ESC #3CC7D3)
    DY  = âmbar    #D98A00  o elevador: a diferença dos y (cateto em pé)
    DIST = índigo da matéria   a hipotenusa: a distância, o segmento entre os pontos (e, nas próximas, a própria reta)
  As mesmas cores pintam os números nas contas: "4 − 1 = 3" em petróleo, "6 − 2 = 4" em âmbar, "5" da distância em índigo.
- Pontos em tinta preta (E.ponto) com o nome ao lado; resposta final na esfera; erro em vermelho, certo em verde;
  atalho no palco escuro. A figura não mente: os pontos estão no lugar certo do plano (escala igual nos dois eixos).
Peças locais: plano() (E.plano com o eixo x em índigo), par()/par_em(), anda() (seta que anda), cateto() (lado que cresce
na cor fixa), lado_txt() (medida por fora do triângulo), canto() (ângulo reto do triângulo), conta() (conta com partes
coloridas), nome() (ponto em tinta com nome), tiques() (traços sem número quando só alguns valores têm rótulo), bola_txt() e anel().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Analítica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANA-001_distancia_entre_dois_pontos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("triangulo", "regra", "negativos", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ENT, SAI = COR, TINTA                       # x / y, como em Funções
DX, DY, DIST = "#0E9AA7", "#D98A00", E.COR  # corredor (dif. dos x), elevador (dif. dos y), distância
DX_ESC = "#3CC7D3"
assert 4 - 1 == 3 and 6 - 2 == 4 and 3 ** 2 + 4 ** 2 == 25 == 5 ** 2 and 3 + 4 == 7
assert 4 - (-2) == 6 and -7 - 1 == -8 and (-8) ** 2 == 64 and 6 ** 2 == 36 and 36 + 64 == 100 == 10 ** 2
assert 2 - (-3) == 5 and 11 - (-1) == 12 and 25 + 144 == 169 == 13 ** 2 and 5 + 12 == 17

# os três planos da aula (escala igual nos dois eixos)
P1 = E.Plano(1060, 170, 740, 740, -1, 7, -1, 7)        # casa (1, 2) e mercado (4, 6)
P2 = E.Plano(1150, 165, 600, 750, -3, 5, -8, 2)        # (−2, 1) e (4, −7)
P3 = E.Plano(1180, 140, 400, 800, -4, 3, -2, 12)       # escola (−3, −1) e hospital (2, 11)


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


# casa e mercado no P1
CASA, MERC, CANT = (1, 2), (4, 6), (4, 2)
G1 = (3, 10 / 3)


def casa_mercado(c, t, ta, tb, rotulos=True):
    nome(c, t, ta, P1, *CASA, "casa" if rotulos else None, lado=(0, 1))
    nome(c, t, tb, P1, *MERC, "mercado" if rotulos else None, lado=(1, -1))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        plano(c, t, C["s01.a"], P1)
        q = ep(t, C["s01.c"] + 1.0, 0.5)
        if q > 0:  # um quadradinho = 1 km
            c.drawRect(skia.Rect.MakeLTRB(P1.x(5), P1.y(4), P1.x(6), P1.y(3)), M.paint(COR, 0.3 * q))
            centro(c, "1 km", P1.x(5.5), P1.y(3) + 50, 36, "b", COR, q)
        casa_mercado(c, t, C["s01.b"], C["s01.c"])
        if t >= C["s01.d"]:
            (x0, y0), (x1, y1) = P1(*CASA), P1(*MERC)
            M.line(c, x0, y0, x1, y1, DIST, 1.0, 7, dash=None if t >= C["s01.f"] else E.TRACO, progress=ease_io(prog(t, C["s01.d"], 0.8)))
            mx, my = P1(2.1, 4.6)
            if t < C["s01.f"]:
                E.foco(c, t, C["s01.d"] + 0.5, 0.4, lambda a: E.pilula(c, "?", mx, my, 50, "g", fundo=DIST, a=a))
            else:
                E.foco(c, t, C["s01.f"], 0.4, lambda a: E.pilula(c, "5 km", mx - 20, my, 46, "g", fundo=DIST, a=a))
        E.frase(c, t, C["s01.b"], [("casa", "g", 72)], XE, 270)
        par_em(c, t, C["s01.b"] + 0.3, "1", "2", XE + 240, 270, 72)
        E.frase(c, t, C["s01.c"], [("mercado", "g", 72)], XE, 390)
        par_em(c, t, C["s01.c"] + 0.3, "4", "6", XE + 370, 390, 72)
        E.frase(c, t, C["s01.c"] + 1.0, ps("1 quadradinho = 1 km", "i", 52, TINTA2), XE, 490, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("a distância em", "i", 80), XE, 650)
        E.frase(c, t, C["s01.d"] + 0.6, [("linha", "g", 80, DIST), ("reta?", "g", 80, DIST)], XE, 760)
        E.frase(c, t, C["s01.e"], [("não", "i", 84), ("é", "i", 84)], XE, 910)
        E.foco(c, t, C["s01.e"] + 0.1, 0.4, lambda a: E.escreve(c, "7", XE + 200, 915, 120, "g", ERRADO, a))
        if t >= C["s01.e"] + 0.3:
            E.risco(c, XE + 180, 935, XE + 290, 815, t, C["s01.e"] + 0.3, largura=12)
        E.frase(c, t, C["s01.f"], [("é", "i", 84)], XE + 360, 910)
        bola_txt(c, t, C["s01.f"] + 0.1, "5", XE + 520, 880, 80, 110)
    E.saida(c, t, C["s02"] - 0.1, cena1)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 1.0, [("distância", "g", 130)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.6, [("entre", "i", 96), ("quaisquer", "i", 96), ("dois", "i", 96)], XE, 610)
        E.frase(c, t, C["s02.a"] + 2.2, [("pontos", "g", 110, COR)], XE, 740)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("duas", "g", 80, COR, C["s03.a"]), ("coisas", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 200, "center")
    x, w = 230, 1460
    for k, y in (("s03.b", 290), ("s03.c", 590)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 250, p, prog_=p)
    # 1: o plano, corredor e elevador
    k = C["s03.b"]
    pa, pb = ep(t, k + 0.6, 0.6), ep(t, k + 2.6, 0.6)
    if pa > 0:
        M.arrow(c, 330, 490, 520, 490, DX, pa, 10, 28, pa)
    if pb > 0:
        M.arrow(c, 520, 490, 520, 340, DY, pb, 10, 28, pb)
    E.frase(c, t, k, [("plano", "g", 70, COR), ("cartesiano", "g", 70, COR)], 620, 380)
    E.linha(c, t, [("1º", "g", 58, DX, k + 0.6), ("corredor", "i", 60, TINTA, k + 0.8), ("(x),", "g", 54, ENT, k + 1.0),
                   ("2º", "g", 58, DY, k + 2.6), ("elevador", "i", 60, TINTA, k + 2.8), ("(y)", "g", 54, SAI, k + 3.0)], 620, 480)
    # 2: Pitágoras
    k = C["s03.c"]
    A_, R_, T_ = (340, 790), (560, 790), (560, 640)
    E.triangulo(c, t, k, A_, R_, T_, vertices=None, retos=(1,), preenche=0.06, d=0.6)
    for (P_, Q_), cor, tq in (((A_, R_), DX, k + 2.6), ((R_, T_), DY, k + 2.6), ((A_, T_), DIST, k + 1.2)):
        q = ep(t, tq, 0.5)
        if q > 0:
            M.line(c, *P_, *Q_, cor, 1.0, 10, progress=q)
    E.frase(c, t, k, [("teorema", "i", 70), ("de", "i", 70), ("Pitágoras", "g", 70, COR)], 660, 680)
    E.foco(c, t, k + 1.2, 0.5, lambda a: conta(c, [("hipotenusa^2", DIST), (" = ", TINTA)], 660, 780, 58, a))
    wh = conta(None, [("hipotenusa^2", DIST), (" = ", TINTA)], 0, 0, 58, 0)
    E.foco(c, t, k + 2.6, 0.5, lambda a: conta(c, [("cateto^2", DX), (" + ", TINTA), ("cateto^2", DY)], 660 + wh, 780, 58, a))
    E.frase(c, t, C["s04"] - 2.6, ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 960, "center", passo=0.1)


# ---------------- o triângulo escondido ----------------
def b_triangulo(c, t, C, b):
    plano(c, t, C["s04"], P1)
    sombra_tri(c, t, C["s05.a"], P1, CASA, CANT, MERC)
    # a distância (hipotenusa): fina na s04, grossa na s05.d
    if t >= C["s04.b"]:
        p = ease_io(prog(t, C["s04.b"], 0.8))
        M.line(c, *P1(*CASA), *P1(*MERC), DIST, 1.0, 7, progress=p)
    cateto(c, t, C["s05.d"], P1, CASA, MERC, DIST, 0.6, 12)
    anda(c, t, C["s04.c"], P1, CASA, CANT, DX)
    anda(c, t, C["s04.d"], P1, CANT, MERC, DY)
    if t >= C["s05.b"]:
        canto(c, t, C["s05.b"], P1, CANT, CASA, MERC)
        anel(c, t, C["s05.b"], *P1(*CANT), TINTA)
    q = pulso(t, C["s05.c"], 2.0)
    if q > 0:
        M.line(c, *P1(*CASA), *P1(*CANT), DX, 0.25 * q, 34)
        M.line(c, *P1(*CANT), *P1(*MERC), DY, 0.25 * q, 34)
    q = pulso(t, C["s05.d"], 2.0)
    if q > 0:
        M.line(c, *P1(*CASA), *P1(*MERC), DIST, 0.22 * q, 34)
    casa_mercado(c, t, C["s04.a"], C["s04.a"] + 0.4)
    # medidas (s06) e a distância (s07)
    if t >= C["s06.a"]:
        q = ep(t, C["s06.a"], 0.4) * (1 - ep(t, C["s07"], 0.5))
        for v in (1, 4):
            M.line(c, P1.x(v), P1.y(2), P1.x(v), P1.oy, ENT, 0.6 * q, 4, dash=E.TRACO)
            E.pilula(c, str(v), P1.x(v), P1.oy + 50, 38, "g", fundo=ENT, a=q)
    if t >= C["s06.b"]:
        q = ep(t, C["s06.b"], 0.4) * (1 - ep(t, C["s07"], 0.5))
        for v, x0 in ((2, 1), (6, 4)):
            M.line(c, P1.x(x0), P1.y(v), P1.ox, P1.y(v), SAI, 0.6 * q, 4, dash=E.TRACO)
            E.pilula(c, str(v), P1.ox - 40, P1.y(v), 38, "g", fundo=SAI, a=q)
    lado_txt(c, t, C["s06.a"] + 1.4, P1, CASA, CANT, "3", G1, DX, 60)
    lado_txt(c, t, C["s06.b"] + 1.4, P1, CANT, MERC, "4", G1, DY, 60)
    lado_txt(c, t, C["s07.d"] + 0.4, P1, CASA, MERC, "5", G1, DIST, 64)

    def s04():
        E.frase(c, t, C["s04.a"], [("casa", "g", 66)], XE, 290)
        par_em(c, t, C["s04.a"] + 0.2, "1", "2", XE + 230, 290, 66)
        E.frase(c, t, C["s04.a"] + 0.4, [("mercado", "g", 66)], XE, 390)
        par_em(c, t, C["s04.a"] + 0.6, "4", "6", XE + 340, 390, 66)
        E.frase(c, t, C["s04.b"], [("a", "i", 80), ("distância", "g", 80, DIST)], XE, 540)
        E.frase(c, t, C["s04.b"] + 0.6, ps("que você quer", "i", 72), XE, 630)
        E.frase(c, t, C["s04.c"], [("1º", "g", 76, DX), ("corredor", "g", 76, DX), ("→", "g", 76, DX)], XE, 790)
        E.frase(c, t, C["s04.d"], [("2º", "g", 76, DY), ("elevador", "g", 76, DY), ("↑", "g", 76, DY)], XE, 900)
    E.saida(c, t, C["s05"] - 0.1, s04)

    def s05():
        E.frase(c, t, C["s05.a"], [("um", "i", 80), ("triângulo", "g", 80)], XE, 300)
        E.frase(c, t, C["s05.a"] + 0.5, [("retângulo", "g", 80, COR)], XE, 400)
        E.frase(c, t, C["s05.b"], ps("corredor e elevador:", "i", 60), XE, 520)
        E.frase(c, t, C["s05.b"] + 0.8, [("canto", "i", 66), ("reto", "g", 66)], XE, 600)
        E.frase(c, t, C["s05.c"], [("catetos:", "i", 70), ("corredor", "g", 64, DX), ("e", "i", 64), ("elevador", "g", 64, DY)], XE, 760)
        E.frase(c, t, C["s05.d"], [("hipotenusa:", "i", 70), ("a", "i", 70), ("distância", "g", 64, DIST)], XE, 880)
    E.saida(c, t, C["s06"] - 0.1, s05)

    def s06():
        E.frase(c, t, C["s06"], ps("quanto mede cada cateto?", "i", 66), XE, 270, passo=0.12)
        E.frase(c, t, C["s06.a"], [("x:", "g", 64, ENT), ("de", "i", 64), ("1", "g", 64, ENT), ("até", "i", 64), ("4", "g", 64, ENT)], XE, 420)
        conta_em(c, t, C["s06.a"] + 1.4, [("4 − 1 = ", TINTA), ("3", DX)], XE + 60, 530, 96)
        E.frase(c, t, C["s06.b"], [("y:", "g", 64, SAI), ("de", "i", 64), ("2", "g", 64), ("até", "i", 64), ("6", "g", 64)], XE, 700)
        conta_em(c, t, C["s06.b"] + 1.4, [("6 − 2 = ", TINTA), ("4", DY)], XE + 60, 810, 96)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"], [("agora", "i", 66), ("é", "i", 66), ("Pitágoras", "g", 66, COR)], XE, 250)
    conta_em(c, t, C["s07.a"], [("3", DX), ("^2 = 9", TINTA)], XE + 40, 390, 92)
    conta_em(c, t, C["s07.b"], [("4", DY), ("^2 = 16", TINTA)], XE + 40, 510, 92)
    conta_em(c, t, C["s07.c"], [("9 + 16 = 25", TINTA)], XE + 40, 630, 92)
    conta_em(c, t, C["s07.d"], [("r{25} = ", TINTA), ("5", DIST)], XE + 40, 770, 92)
    bola_txt(c, t, C["s07.e"], "5 km", 560, 900, 100, 66)
    E.frase(c, t, C["s07.e"] + 0.4, ps("em linha reta", "i", 54, TINTA2), 690, 920)


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    E.frase(c, t, C["s08"], ps("vale para quaisquer dois pontos", "i", 70, TINTA2), W / 2, 170, "center", passo=0.12)
    y1, y2, sz = 310, 420, 66
    conta_em(c, t, C["s08.a"], [("distância^2", DIST), (" = (diferença dos x)^2", DX)], 330, y1, sz)
    conta_em(c, t, C["s08.b"], [("+ (diferença dos y)^2", DY)], 330 + conta(None, [("distância^2 = ", DIST)], 0, 0, sz, 0), y2, sz)
    E.frase(c, t, C["s08.c"], [("no", "i", 66), ("fim,", "i", 66), ("tire", "i", 66), ("a", "i", 66), ("raiz", "g", 66, COR)], 330, 530)
    # a fórmula dos livros
    fy, fs = 740, 92
    partes = [("d", DIST), (" = r{(x₂ − x₁)^2 + (y₂ − y₁)^2}", TINTA)]
    wf = conta(None, partes, 0, 0, fs, 0)
    x0 = W / 2 - wf / 2
    E.foco(c, t, C["s08.c"] + 2.4, 0.6, lambda a: conta(c, partes, x0, fy, fs, a))
    if t >= C["s08.c"] + 2.4:
        p = ep(t, C["s08.c"] + 2.4, 0.5)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 - 60, fy - 150, wf + 120, 240), 30, 30), M.paint(TINTA, 0.06 * p))
    wd = E.formula(None, "d", 0, 0, fs, "g", a=0)
    E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "d = distância", x0 + wd / 2 + 60, fy + 120, 40, "g", fundo=DIST, a=a))
    if t >= C["s08.d"]:
        p = ep(t, C["s08.d"], 0.4)
        M.line(c, x0 + wd / 2, fy + 20, x0 + wd / 2, fy + 82, DIST, p, 4)
    E.foco(c, t, C["s08.e"], 0.5, lambda a: (E.formula(c, "ponto 1: (x₁, y₁)", W / 2 - 60, 960, 54, "b", TINTA2, a, "right"),
                                            E.formula(c, "ponto 2: (x₂, y₂)", W / 2 + 60, 960, 54, "b", TINTA2, a, "left")))


# ---------------- com negativos ----------------
A2, B2, R2 = (-2, 1), (4, -7), (4, 1)
G2 = (2, -5 / 3)


def b_negativos(c, t, C, b):
    plano(c, t, C["s09"], P2, marcas_x=[-2, 2], marcas_y=[-8, -6, -4, -2, 2], size=36)
    tiques(c, t, C["s09"], P2, (-3, -1, 1, 3, 4, 5), (-7, -5, -3, -1, 1))
    sombra_tri(c, t, C["s10.c"] + 0.8, P2, A2, R2, B2)
    anda(c, t, C["s10.a"] + 0.6, P2, A2, R2, DX)
    anda(c, t, C["s10.c"] + 0.4, P2, R2, B2, DY)
    if t >= C["s10.c"] + 1.2:
        canto(c, t, C["s10.c"] + 1.2, P2, R2, A2, B2)
    cateto(c, t, C["s11.c"] + 0.6, P2, A2, B2, DIST, 0.7, 10)
    E.ponto(c, t, C["s09.a"] + 0.3, P2, *A2, None, cor=TINTA, r=15)
    E.foco(c, t, C["s09.a"] + 0.5, 0.4, lambda a: par(c, "−2", "1", *P2(-2.4, 1.55), 44, a, "center"))
    E.ponto(c, t, C["s09.b"] + 0.3, P2, *B2, None, cor=TINTA, r=15)
    E.foco(c, t, C["s09.b"] + 0.5, 0.4, lambda a: par(c, "4", "−7", *P2(3.2, -7.75), 44, a, "center"))
    lado_txt(c, t, C["s10.b"] + 0.8, P2, A2, R2, "6", G2, DX, 56)
    lado_txt(c, t, C["s11.a"] + 0.6, P2, R2, B2, "8", G2, DY, 56)
    lado_txt(c, t, C["s11.d"] + 0.4, P2, A2, B2, "10", G2, DIST, 60, em=0.68)

    E.frase(c, t, C["s09"], [("e", "i", 80), ("com", "i", 80), ("negativos?", "g", 80, COR)], XE, 240)

    def s09_10():
        par_em(c, t, C["s09.a"], "−2", "1", XE, 370, 80)
        par_em(c, t, C["s09.b"], "4", "−7", XE + 380, 370, 80)
        E.frase(c, t, C["s10.a"], [("dif.", "i", 60), ("dos", "i", 60), ("x", "g", 64, ENT)], XE, 510)
        conta_em(c, t, C["s10.a"] + 0.6, [("4 − (−2)", DX)], XE, 610, 84)
        conta_em(c, t, C["s10.b"], [(" = 4 + 2 = ", TINTA), ("6", DX)], XE + conta(None, [("4 − (−2)", DX)], 0, 0, 84, 0), 610, 84)
        E.frase(c, t, C["s10.c"], [("dif.", "i", 60), ("dos", "i", 60), ("y", "g", 64, SAI)], XE, 760)
        conta_em(c, t, C["s10.c"] + 0.6, [("−7 − 1 = ", TINTA), ("−8", DY)], XE, 860, 84)
    E.saida(c, t, C["s11"] - 0.1, s09_10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11"], [("o", "i", 66), ("−8", "g", 66, DY), ("não", "i", 66), ("atrapalha", "i", 66)], XE, 370)
    conta_em(c, t, C["s11.a"], [("(−8)", DY), ("^2 = 64", TINTA)], XE, 490, 84)
    E.foco(c, t, C["s11.a"] + 0.8, 0.4, lambda a: E.pilula(c, "positivo", XE + 630, 462, 40, "g", fundo=CERTO, a=a))
    conta_em(c, t, C["s11.b"], [("6", DX), ("^2 = 36", TINTA)], XE, 600, 84)
    conta_em(c, t, C["s11.c"], [("36 + 64 = 100", TINTA)], XE, 710, 84)
    conta_em(c, t, C["s11.d"], [("r{100} = ", TINTA)], XE, 860, 84)
    bola_txt(c, t, C["s11.d"] + 0.2, "10", XE + 360, 832, 82, 80)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano(c, t, C["s12"], P1)
    sombra_tri(c, t, C["s12"] + 0.4, P1, CASA, CANT, MERC)
    cateto(c, t, C["s12"] + 0.4, P1, CASA, CANT, DX, 0.6, 9)
    cateto(c, t, C["s12"] + 0.8, P1, CANT, MERC, DY, 0.6, 9)
    canto(c, t, C["s12"] + 1.2, P1, CANT, CASA, MERC)
    casa_mercado(c, t, C["s12"] + 0.2, C["s12"] + 0.3)
    lado_txt(c, t, C["s12"] + 1.2, P1, CASA, CANT, "3", G1, DX, 60)
    lado_txt(c, t, C["s12"] + 1.2, P1, CANT, MERC, "4", G1, DY, 60)
    # o caminho pelas ruas, em vermelho
    anda(c, t, C["s12.c"], P1, CASA, CANT, ERRADO, 0.7, 9)
    anda(c, t, C["s12.c"] + 0.7, P1, CANT, MERC, ERRADO, 0.7, 9)
    E.foco(c, t, C["s12.c"] + 1.2, 0.4, lambda a: E.pilula(c, "pelas ruas: 7", P1.x(5.6), P1.y(1.2), 40, "g", fundo=ERRADO, a=a))
    cateto(c, t, C["s13.a"], P1, CASA, MERC, DIST, 0.7, 12)
    E.foco(c, t, C["s13.a"] + 0.6, 0.4, lambda a: E.pilula(c, "linha reta: 5", P1.x(1.75), P1.y(5.4), 40, "g", fundo=DIST, a=a))

    def s12():
        E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 250)
        E.frase(c, t, C["s12.a"], ps("somar os catetos", "i", 72), XE, 380)
        E.frase(c, t, C["s12.a"] + 0.8, [("sem", "i", 72), ("Pitágoras", "g", 72, ERRADO)], XE, 480)
        conta_em(c, t, C["s12.b"], [("3", DX), (" + ", TINTA), ("4", DY), (" = 7", ERRADO)], XE, 640, 100)
        E.foco(c, t, C["s12.b"] + 1.4, 0.4, lambda a: E.escreve(c, "7 km?", XE + 470, 640, 80, "g", ERRADO, a))
        if t >= C["s12.b"] + 2.0:
            E.risco(c, XE + 450, 660, XE + 690, 570, t, C["s12.b"] + 2.0, largura=11)
        E.frase(c, t, C["s12.c"], [("7", "g", 72, ERRADO), ("=", "i", 72), ("caminho", "i", 72), ("pelas", "i", 72), ("ruas", "g", 72)], XE, 800)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], [("a", "i", 72), ("linha", "i", 72), ("reta", "i", 72), ("é", "i", 72), ("a", "i", 72), ("hipotenusa", "g", 66, DIST)], XE, 300)
    E.frase(c, t, C["s13.a"] + 1.2, ps("sempre mais curta", "i", 64, TINTA2), XE, 390)
    conta_em(c, t, C["s13.b"], [("5", CERTO), (" < 7", TINTA)], XE, 560, 120)
    E.frase(c, t, C["s13.c"], [("some", "i", 66), ("os", "i", 66), ("quadrados,", "g", 66, COR)], XE, 720)
    E.frase(c, t, C["s13.c"] + 1.0, [("depois", "i", 66), ("a", "i", 66), ("raiz", "g", 66, COR)], XE, 810)
    conta_em(c, t, C["s13.c"] + 1.6, [("r{3^2 + 4^2} = ", TINTA), ("5", CERTO)], XE, 950, 76)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    RY, RX0, RX1 = 650, 330, 1590

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s14.a"], [("cada", "i", 70, CLARO), ("diferença", "g", 70, BR), ("=", "i", 70, CLARO), ("passos", "g", 70, BR),
                                   ("entre", "i", 70, CLARO), ("os", "i", 70, CLARO), ("pontos", "i", 70, CLARO)], W / 2, 280, "center", passo=0.12)
        vx = E.reta(c, t, C["s14.a"] + 1.0, RX0, RX1, RY, -3, 7, list(range(-3, 8)), E._num, escuro=True, size=44)

        def caso1():
            E.frase(c, t, C["s14.b"], [("sinais", "i", 70, CLARO), ("diferentes:", "g", 70, BR), ("some", "i", 70, CLARO)], W / 2, 420, "center")
            for v in (-2, 4):
                E.foco(c, t, C["s14.c"] - 0.4, 0.3, lambda a, v=v: E.bola(c, vx(v), RY, 18, DX_ESC, a), blur=0)
            E.salto(c, t, C["s14.c"], vx(-2), vx(0), RY, 110, DX_ESC, "2", size=54)
            E.salto(c, t, C["s14.c"] + 0.7, vx(0), vx(4), RY, 150, DX_ESC, "4", size=54)
            conta_em(c, t, C["s14.c"] + 1.4, [("2 + 4 = ", BR), ("6", DX_ESC), (" passos", CLARO)], W / 2, 900, 84, "center")
        E.saida(c, t, C["s14.d"] - 0.1, caso1)
        if t >= C["s14.d"]:
            E.frase(c, t, C["s14.d"], [("sinais", "i", 70, CLARO), ("iguais:", "g", 70, BR), ("subtraia", "i", 70, CLARO)], W / 2, 420, "center")
            for v in (2, 6):
                E.foco(c, t, C["s14.e"] - 0.4, 0.3, lambda a, v=v: E.bola(c, vx(v), RY, 18, DY, a), blur=0)
            E.salto(c, t, C["s14.e"], vx(2), vx(6), RY, 130, DY, "4", size=54)
            conta_em(c, t, C["s14.e"] + 0.8, [("6 − 2 = ", BR), ("4", DY), (" passos", CLARO)], W / 2, 900, 84, "center")
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    RY2 = 430
    E.frase(c, t, C["s15"], [("por", "i", 70, CLARO), ("que", "i", 70, CLARO), ("funciona", "g", 70, BR)], W / 2, 170, "center")
    vx = E.reta(c, t, C["s15"] + 0.2, RX0, RX1, RY2, -3, 7, list(range(-3, 8)), E._num, escuro=True, size=44)
    for v in (-2, 4):
        E.foco(c, t, C["s15"] + 0.6, 0.3, lambda a, v=v: E.bola(c, vx(v), RY2, 18, DX_ESC, a), blur=0)
    E.salto(c, t, C["s15.a"] + 0.6, vx(-2), vx(0), RY2, 100, DX_ESC, "2", size=50)
    E.salto(c, t, C["s15.a"] + 2.0, vx(0), vx(4), RY2, 140, DX_ESC, "4", size=50)
    if t >= C["s15.a"]:
        anel(c, t, C["s15.a"], vx(0), RY2, BR)
        anel(c, t, C["s15.a"] + 0.9, vx(0), RY2, BR)
    E.frase(c, t, C["s15.a"], [("o", "i", 60, CLARO), ("zero", "g", 60, BR), ("fica", "i", 60, CLARO), ("no", "i", 60, CLARO),
                               ("meio", "g", 60, BR)], W / 2, 600, "center")
    def sinal_():
        conta_em(c, t, C["s15.b"], [("(−6)^2 = 6^2 = 36", BR)], W / 2, 770, 84, "center")
        E.frase(c, t, C["s15.b"] + 0.8, [("o", "i", 54, CLARO), ("quadrado", "g", 54, BR), ("apaga", "i", 54, CLARO), ("o", "i", 54, CLARO),
                                         ("sinal", "g", 54, BR)], W / 2, 870, "center")
    E.saida(c, t, C["s15.c"] - 0.1, sinal_)
    E.frase(c, t, C["s15.c"], [("não", "g", 76, ERRADO), ("compensa", "i", 80, CLARO), ("com", "i", 80, CLARO), ("quadriculado:", "g", 70, BR)],
            W / 2, 780, "center")
    E.frase(c, t, C["s15.c"] + 1.2, ps("conte os quadradinhos", "i", 70, CLARO), W / 2, 890, "center")


# ---------------- questão ----------------
ESC, HOS, R3 = (-3, -1), (2, 11), (2, -1)
G3 = (1 / 3, 3)


def mapa3(c, t, t0, ta, tb):
    plano(c, t, t0, P3, marcas_x=[], marcas_y=[2, 4, 6, 8, 10], size=34)
    tiques(c, t, t0, P3, (-4, -3, -2, -1, 1, 2, 3), (-2, -1, 1, 3, 5, 7, 9, 11, 12))
    nome(c, t, ta, P3, *ESC, "escola", lado=(-1, 0), size=42, r=14)
    nome(c, t, tb, P3, *HOS, "hospital", lado=(1, 0), size=42, r=14)


def b_questao(c, t, C, b):
    mapa3(c, t, C["s16"], C["s16.a"] + 0.3, C["s16.b"] + 0.3)
    if t >= C["s16.c"]:
        M.line(c, *P3(*ESC), *P3(*HOS), DIST, 1.0, 6, dash=E.TRACO, progress=ease_io(prog(t, C["s16.c"], 0.8)))
        E.foco(c, t, C["s16.c"] + 0.6, 0.4, lambda a: E.pilula(c, "?", *P3(-1.4, 5.6), 48, "g", fundo=DIST, a=a))
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], [("escola", "g", 70)], XE, 330)
    par_em(c, t, C["s16.a"] + 0.3, "−3", "−1", XE + 280, 330, 70)
    E.frase(c, t, C["s16.b"], [("hospital", "g", 70)], XE, 450)
    par_em(c, t, C["s16.b"] + 0.3, "2", "11", XE + 340, 450, 70)
    E.frase(c, t, C["s16.c"], ps("distância em", "i", 70), XE, 590)
    E.frase(c, t, C["s16.c"] + 0.5, [("linha", "g", 70, DIST), ("reta?", "g", 70, DIST)], XE + 450, 590)
    E.frase(c, t, C["s16"] + 0.6, ps("mapa em km", "i", 46, TINTA2), XE, 680)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=560, cy=830, r=90)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    mapa3(c, t, C["s18"] - 3, C["s18"] - 3, C["s18"] - 3)
    sombra_tri(c, t, C["s18.b"] + 0.8, P3, ESC, R3, HOS)
    anda(c, t, C["s18.a"] + 0.4, P3, ESC, R3, DX, 0.7, 9)
    anda(c, t, C["s18.b"] + 0.4, P3, R3, HOS, DY, 0.9, 9)
    if t >= C["s18.b"] + 1.2:
        canto(c, t, C["s18.b"] + 1.2, P3, R3, ESC, HOS)
    lado_txt(c, t, C["s18.a"] + 1.4, P3, ESC, R3, "5", G3, DX, 52, em=0.3)
    E.foco(c, t, C["s18.a"] + 0.2, 0.4, lambda a: (E.pilula(c, "−3", P3.x(-3), P3.oy - 44, 34, "g", fundo=ENT, a=a),
                                                  E.pilula(c, "2", P3.x(2), P3.oy - 44, 34, "g", fundo=ENT, a=a)))
    E.foco(c, t, C["s18.b"] + 0.2, 0.4, lambda a: (E.pilula(c, "−1", P3.x(2), P3.y(-1) + 52, 34, "g", fundo=SAI, a=a),
                                                  E.pilula(c, "11", P3.ox - 50, P3.y(11), 34, "g", fundo=SAI, a=a)))
    lado_txt(c, t, C["s18.b"] + 1.6, P3, R3, HOS, "12", G3, DY, 52)
    cateto(c, t, C["s19.d"], P3, ESC, HOS, DIST, 0.7, 10)
    lado_txt(c, t, C["s19.d"] + 0.5, P3, ESC, HOS, "13", G3, DIST, 56, em=0.3)

    def s18():
        E.frase(c, t, C["s18.a"], [("x:", "g", 62, ENT), ("de", "i", 62), ("−3", "g", 62, ENT), ("até", "i", 62), ("2", "g", 62, ENT)], XE, 280)
        E.frase(c, t, C["s18.a"] + 1.0, ps("sinais diferentes", "i", 50, TINTA2), XE, 360)
        conta_em(c, t, C["s18.a"] + 1.8, [("3 + 2 = ", TINTA), ("5", DX)], XE + 40, 470, 92)
        E.frase(c, t, C["s18.b"], [("y:", "g", 62, SAI), ("de", "i", 62), ("−1", "g", 62), ("até", "i", 62), ("11", "g", 62)], XE, 650)
        conta_em(c, t, C["s18.b"] + 1.2, [("1 + 11 = ", TINTA), ("12", DY)], XE + 40, 780, 92)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    conta_em(c, t, C["s19.a"], [("5", DX), ("^2 = 25", TINTA)], XE, 250, 80)
    conta_em(c, t, C["s19.b"], [("12", DY), ("^2 = 144", TINTA)], XE, 360, 80)
    conta_em(c, t, C["s19.c"], [("25 + 144 = 169", TINTA)], XE, 470, 80)
    conta_em(c, t, C["s19.d"], [("r{169} = ", TINTA), ("13", DIST)], XE, 600, 80)
    bola_txt(c, t, C["s19.e"], "13 km", 960, 575, 110, 64)
    E.frase(c, t, C["s19.f"], [("pelas", "i", 60), ("ruas:", "i", 60)], XE, 790)
    conta_em(c, t, C["s19.f"] + 0.5, [("5 + 12 = 17", TINTA)], XE + 360, 790, 70)
    E.frase(c, t, C["s19.f"] + 2.0, [("13", "g", 66, CERTO), ("<", "g", 66), ("17:", "g", 66), ("faz", "i", 66), ("sentido", "g", 66, CERTO)], XE, 910)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", [("desenhe", "i", 84), ("o", "i", 84), ("triângulo", "g", 84)]),
                 ("s20.b", [("catetos", "g", 84), ("=", "i", 84), ("diferenças", "i", 84), ("dos", "i", 84), ("x", "g", 84, DX), ("e", "i", 84),
                            ("dos", "i", 84), ("y", "g", 84, DY)]),
                 ("s20.c", [("distância", "g", 84, DIST), ("=", "i", 84), ("hipotenusa", "i", 84)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s21.a"], [("Ponto", "g", 150, COR), ("médio", "g", 150, COR)], XE, 470)
    E.frase(c, t, C["s21.b"], [("e", "i", 110), ("baricentro", "g", 120, COR)], XE, 620)
    E.frase(c, t, C["s21.b"] + 1.4, ps("com contas de cabeça", "i", 60, TINTA2), XE, 720)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, triangulo=b_triangulo, regra=b_regra, negativos=b_negativos, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
