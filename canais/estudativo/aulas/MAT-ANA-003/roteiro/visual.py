"""Visual — Estudativo · MAT-ANA-003: coeficiente angular (m = Δy/Δx = tg θ) e alinhamento de três pontos.

Segue a linguagem da Geometria Analítica definida em MAT-ANA-001 (leia o cabeçalho de lá) e a das cores da Trigonometria:
- o TRIÂNGULO DA SUBIDA entre dois pontos da reta: Δx deitado em petróleo (DX = cateto adjacente ao θ), Δy em pé em âmbar
  (DY = cateto oposto), a reta em índigo (DIST = a hipotenusa). Na fração do m, o Δy (em cima) é âmbar e o Δx (embaixo) é petróleo;
- o ângulo θ entre a reta e a horizontal é o arco índigo de E.angulo, com a horizontal de apoio tracejada;
- x em índigo, y em preto, par() com x índigo; plano à direita, texto à esquerda; erro em vermelho, certo em verde; atalho no palco.
Peças novas desta aula: fra() (fração com cima e baixo em cores próprias, como na MAT-TRI-001), mfr() (m = Δy/Δx colorido),
degrau() (o triângulo da subida entre dois pontos, com as medidas) e teta() (o ângulo com a horizontal de apoio).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Analítica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANA-003_coeficiente_angular_e_alinhamento.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("eme", "angulo", "alinhamento", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ENT, SAI = COR, TINTA                       # x / y, como em Funções
DX, DY, DIST = "#0E9AA7", "#D98A00", E.COR  # Δx (adjacente), Δy (oposto), a reta
DX_ESC, DY_ESC = "#3CC7D3", "#FFB833"
assert 5 - 1 == 4 and 3 - 1 == 2 and 10 - 5 == 5 and 5 - 3 == 2 and 4 / 2 == 2 and 5 / 2 == 2.5
assert 8 - 2 == 6 and 4 - 1 == 3 and 6 / 3 == 2 and 3 / 6 == 0.5
assert 4 * 2 == 8 and 2 * 5 == 10
assert 1 - 4 == -3 and 1 - (-1) == 2 and -3 / 2 == -1.5 and -5 - 1 == -6 and 5 - 1 == 4 and -3 * 4 == -12 == 2 * (-6)

P1 = E.Plano(1120, 110, 630, 840, -1, 8, -1, 11)     # postes (1, 1), (3, 5), (5, 10)
P2 = E.Plano(1150, 130, 560, 800, -1, 6, -1, 9)      # (1, 2) e (4, 8); (1, 1) e (4, 4)
P4 = E.Plano(1180, 150, 560, 770, -2, 6, -6, 5)      # questão: (−1, 4), (1, 1), (5, −5)


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


def seg(c, t, t0, P, A, B, cor=None, d=0.8, largura=7, tracejado=False, a=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P(*A), *P(*B), cor or DIST, a, largura, dash=E.TRACO if tracejado else None, progress=p)


def letra_par(c, t, t0, L, xv, yv, x, y, size, cor=TINTA):
    E.foco(c, t, t0, 0.5, lambda a: (E.escreve(c, L, x, y, size, "g", cor, a),
                                     par(c, xv, yv, x + E.larg(L, "g", size) + size * 0.3, y, size, a)))


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
    """m = Δy/Δx com o de cima em âmbar e o de baixo em petróleo; pos (o resultado) entra em tpos. Devolve a largura"""
    wp = _w(pre, size) if pre else 0
    wf = fra(None, cima, baixo, 0, 0, size)
    gap = size * 0.12
    E.foco(c, t, t0, 0.5, lambda a: (pre and E.formula(c, pre, x, y, size, "g", cpre or tinta, a), fra(c, cima, baixo, x + wp, y, size, a, cc, cb, tinta)))
    if pos:
        E.foco(c, t, tpos if tpos is not None else t0 + 0.8, 0.5, lambda a: E.formula(c, pos, x + wp + wf + gap, y, size, "g", cp or tinta, a))
    return wp + wf + gap + (_w(pos, size) if pos else 0)


def degrau(c, t, P, A, B, tx, ty, lx=None, ly=None, tlx=None, tly=None, larg=10, a=1.0, sombra=None, canto_t=None, setas=False, size=52, emx=0.5):
    """o triângulo da subida de A até B: Δx deitado (petróleo), Δy em pé (âmbar); lx, ly = medidas; setas = anda() em vez de lado"""
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
        lado_txt(c, t, tlx if tlx is not None else tx + 0.4, P, A, R, lx, G, DX, size, em=emx)
    if ly:
        lado_txt(c, t, tly if tly is not None else ty + 0.4, P, R, B, ly, G, DY, size)


def teta(c, t, t0, P, A, B, rot="θ", r=78, ref=1.6, cor=None):
    """o ângulo da reta AB com a horizontal, em A, com a horizontal de apoio tracejada"""
    if t < t0:
        return
    X, Y = P(*A)
    M.line(c, X, Y, P.x(A[0] + ref), Y, TINTA2, 0.8, 4, dash=E.TRACO, progress=ease_io(prog(t, t0, 0.5)))
    E.angulo(c, t, t0 + 0.2, (X, Y), (P.x(A[0] + 1), Y), P(*B), rot, r=r, cor=cor, size=50)


def num_ponto(c, t, t0, P, x, y, s, lado=(-1, -1), cor=TINTA):
    """ponto com um número ou letra ao lado"""
    nome(c, t, t0, P, x, y, s, lado=lado, size=44, r=14, cor=cor)


# ---------------- os postes ----------------
Q1, Q2, Q3 = (1, 1), (3, 5), (5, 10)


def plano1(c, t, t0):
    plano(c, t, t0, P1, marcas_x=[2, 4, 6, 8], marcas_y=[2, 4, 6, 8, 10], size=36)
    tiques(c, t, t0, P1, (1, 3, 5, 7), (1, 3, 5, 7, 9))


def postes(c, t, ta, tb, tc):
    num_ponto(c, t, ta, P1, *Q1, "1")
    num_ponto(c, t, tb, P1, *Q2, "2")
    num_ponto(c, t, tc, P1, *Q3, "3")


def postes_txt(c, t, ta, tb, tc, y0=270, dy=100, size=62):
    for i, (ti, (xv, yv)) in enumerate(((ta, Q1), (tb, Q2), (tc, Q3))):
        letra_par(c, t, ti, str(i + 1), str(xv), str(yv), XE, y0 + i * dy, size, TINTA2)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        plano1(c, t, C["s01"] + 0.2)
        postes(c, t, C["s01.a"] + 0.3, C["s01.b"] + 0.3, C["s01.c"] + 0.3)
        seg(c, t, C["s01.d"], P1, (0.5, -0.125), (5.5, 11.125), TINTA2, 0.9, 5, tracejado=True)
        if t >= C["s01.e"]:  # o 2 fica fora da reta que liga 1 e 3
            q = ep(t, C["s01.e"], 0.4)
            M.line(c, *P1(3, 5), *P1(3, 5.5), ERRADO, q, 8)
            anel(c, t, C["s01.e"], *P1(3, 5), ERRADO)
            anel(c, t, C["s01.e"] + 0.6, *P1(3, 5), ERRADO)
            E.foco(c, t, C["s01.e"] + 0.3, 0.4, lambda a: E.pilula(c, "fora!", P1.x(4.6), P1.y(4.6), 40, "g", fundo=ERRADO, a=a))
        postes_txt(c, t, C["s01.a"], C["s01.b"], C["s01.c"])
        E.frase(c, t, C["s01.d"], [("na", "i", 80), ("mesma", "i", 80), ("reta?", "g", 80, COR)], XE, 640)
        E.frase(c, t, C["s01.e"], [("não", "g", 96, ERRADO), ("estão", "g", 96, ERRADO)], XE, 800)
        E.frase(c, t, C["s01.e"] + 1.2, ps("e uma conta curta prova", "i", 60, TINTA2), XE, 900, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, cena1)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.a"] + 1.0, 0.7, lambda a: E.bola(c, 1480, 540, 270 * ease_back(prog(t, C["s02.a"] + 1.0, 0.7))), blur=0)
        E.foco(c, t, C["s02.a"] + 1.4, 0.5, lambda a: centro(c, "m", 1480, 620, 260, "g", BR, a))
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("a", "i", 110), ("inclinação", "g", 120)], XE, 450)
        E.frase(c, t, C["s02.b"], [("um", "i", 90), ("ângulo", "g", 96, COR)], XE, 600)
        E.frase(c, t, C["s02.c"], [("3", "g", 90, COR), ("pontos", "i", 90), ("alinhados?", "g", 90)], XE, 750)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("duas", "g", 80, COR, C["s03.a"]), ("coisas", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 200, "center")
    x, w = 230, 1460
    for k, y in (("s03.b", 290), ("s03.c", 590)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 250, p, prog_=p)
    # 1: taxa de variação
    k = C["s03.b"]
    pa, pb = ep(t, k + 0.6, 0.6), ep(t, k + 1.2, 0.6)
    if pa > 0:
        M.arrow(c, 330, 490, 520, 490, DX, pa, 10, 28, pa)
    if pb > 0:
        M.arrow(c, 520, 490, 520, 340, DY, pb, 10, 28, pb)
    E.frase(c, t, k, [("taxa", "g", 66, COR), ("de", "i", 70), ("variação", "g", 66, COR)], 620, 380)
    mfr(c, t, k + 2.0, "Δy", "Δx", 620, 490, 64, pre="a = ")
    # 2: tangente
    k = C["s03.c"]
    A_, R_, T_ = (330, 800), (600, 800), (600, 640)
    E.triangulo(c, t, k, A_, R_, T_, vertices=None, retos=(1,), preenche=0.06, d=0.6)
    for (P_, Q_), cor in (((A_, R_), DX), ((R_, T_), DY)):
        q = ep(t, k + 1.6, 0.5)
        if q > 0:
            M.line(c, *P_, *Q_, cor, 1.0, 10, progress=q)
    E.angulo(c, t, k + 0.8, A_, R_, T_, "θ", r=70, size=44)
    E.frase(c, t, k, [("a", "i", 70), ("tangente", "g", 70, COR)], 700, 680)
    mfr(c, t, k + 1.6, "oposto", "adjacente", 700, 790, 56, pre="tg θ = ")
    E.foco(c, t, k + 4.0, 0.5, lambda a: E.formula(c, "tg 45° = 1", 1250, 790, 56, "g", COR, a))
    E.frase(c, t, C["s04"] - 2.6, ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 960, "center", passo=0.1)


# ---------------- coeficiente angular ----------------
A1, B1 = (1, 2), (4, 8)


def plano2(c, t, t0):
    plano(c, t, t0, P2, marcas_x=[1, 2, 3, 4, 5, 6], marcas_y=[2, 4, 6, 8], size=36)
    tiques(c, t, t0, P2, (), (1, 3, 5, 7, 9))


def reta_ab(c, t, ta, tb, tr):
    num_ponto(c, t, ta, P2, *A1, "A")
    num_ponto(c, t, tb, P2, *B1, "B")
    if t >= tr:
        E.reta_pontos(c, t, tr, P2, A1, B1, pontos=False, largura=6)


def b_eme(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], ps("aquela taxa ganha um nome e uma letra", "i", 70), W / 2, 220, "center", passo=0.12)
        E.frase(c, t, C["s04.b"], [("coeficiente", "g", 120, COR)], XE, 450)
        E.frase(c, t, C["s04.b"] + 0.4, [("angular", "g", 120, COR)], XE, 590)
        E.foco(c, t, C["s04.b"] + 0.8, 0.6, lambda a: E.bola(c, 1450, 500, 190 * ease_back(prog(t, C["s04.b"] + 0.8, 0.6)), a=a), blur=0)
        E.foco(c, t, C["s04.b"] + 1.1, 0.5, lambda a: centro(c, "m", 1450, 575, 230, "g", BR, a))
        E.frase(c, t, C["s04.b"] + 2.0, ps("o mesmo a da função afim", "i", 60, TINTA2), XE, 690, passo=0.12)
        E.frase(c, t, C["s04.c"], [("quanto", "i", 70), ("a", "i", 70), ("reta", "i", 70), ("sobe", "g", 70, DY)], W / 2, 860, "center")
        E.frase(c, t, C["s04.c"] + 1.0, [("a", "i", 70), ("cada", "i", 70), ("passo", "g", 70, DX), ("para", "i", 70), ("a", "i", 70),
                                         ("direita", "g", 70, DX)], W / 2, 960, "center")
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    plano2(c, t, C["s05"])
    reta_ab(c, t, C["s05.a"] + 0.3, C["s05.b"] + 0.3, C["s05.b"] + 0.6)
    degrau(c, t, P2, A1, B1, C["s05.d"], C["s05.c"], "3", "6", sombra=C["s05.d"] + 0.5, canto_t=C["s05.d"] + 0.6)
    anda(c, t, C["s05.f"], P2, (2, 4), (3, 4), DX, 0.5, 6)
    anda(c, t, C["s05.f"] + 0.6, P2, (3, 4), (3, 6), DY, 0.5, 6)
    E.foco(c, t, C["s05.f"] + 0.4, 0.4, lambda a: centro(c, "1", *P2(2.5, 3.55), 42, "g", DX, a))
    E.foco(c, t, C["s05.f"] + 1.0, 0.4, lambda a: centro(c, "2", *P2(3.3, 5.15), 42, "g", DY, a))
    letra_par(c, t, C["s05.a"], "A", "1", "2", XE, 250, 64)
    letra_par(c, t, C["s05.b"], "B", "4", "8", XE + 400, 250, 64)
    conta_em(c, t, C["s05.c"], [("Δy", DY), (" = 8 − 2 = ", TINTA), ("6", DY)], XE, 420, 76)
    conta_em(c, t, C["s05.d"], [("Δx", DX), (" = 4 − 1 = ", TINTA), ("3", DX)], XE, 540, 76)
    mfr(c, t, C["s05.e"], "6", "3", XE, 730, 100, pos="= 2", cp=COR, tpos=C["s05.e"] + 1.4, cpre=COR)
    E.frase(c, t, C["s05.f"], [("+1", "g", 64, DX), ("para", "i", 64), ("a", "i", 64), ("direita,", "i", 64), ("sobe", "i", 64), ("2", "g", 64, DY)], XE, 920)


# ---------------- o ângulo ----------------
C1, D1 = (1, 1), (4, 4)


def b_angulo(c, t, C, b):
    plano2(c, t, C["s06"])

    def ab():
        reta_ab(c, t, C["s06"] + 0.2, C["s06"] + 0.3, C["s06"] + 0.4)
        degrau(c, t, P2, A1, B1, C["s06.b"], C["s06.c"], "Δx", "Δy", sombra=C["s06.a"], canto_t=C["s06.a"] + 0.4)
        teta(c, t, C["s06.d"], P2, A1, B1)
        # mais em pé, maior o m
        if t >= C["s07.e"]:
            p = ease_io(prog(t, C["s07.e"], 0.8))
            X, Y = P2(*A1)
            M.line(c, X, Y, *P2(2.75, 9), COR, 0.55, 5, dash=E.TRACO, progress=p)
            E.angulo(c, t, C["s07.e"] + 0.4, (X, Y), (P2.x(2), Y), P2(2.75, 9), None, r=125, cor=TINTA2, preenche=0.0, largura=4)
            E.foco(c, t, C["s07.e"] + 0.8, 0.4, lambda a: E.pilula(c, "m maior", *P2(1.6, 8.3), 36, "g", fundo=COR, a=a))
    E.saida(c, t, C["s08"] - 0.1, ab)

    def s06():
        E.frase(c, t, C["s06"], [("de", "i", 70), ("onde", "i", 70), ("vem", "i", 70), ("o", "i", 70), ("nome", "i", 70), ("angular?", "g", 70, COR)], XE, 250)
        E.frase(c, t, C["s06.a"], [("o", "i", 70), ("triângulo", "g", 70), ("da", "i", 70), ("subida", "g", 70)], XE, 390)
        E.frase(c, t, C["s06.b"], [("Δx", "g", 72, DX), ("deitado", "i", 72)], XE, 510)
        E.frase(c, t, C["s06.c"], [("Δy", "g", 72, DY), ("em", "i", 72), ("pé", "i", 72)], XE, 620)
        E.frase(c, t, C["s06.d"], [("θ", "g", 76, COR), ("=", "i", 72), ("ângulo", "i", 72), ("com", "i", 72), ("a", "i", 72), ("horizontal", "g", 70)], XE, 790)
        E.frase(c, t, C["s06.d"] + 1.6, ps("o eixo x", "i", 56, TINTA2), XE, 880)
    E.saida(c, t, C["s07"] - 0.1, s06)

    def s07():
        E.frase(c, t, C["s07.a"], [("Δy", "g", 70, DY), ("=", "i", 70), ("cateto", "i", 70), ("oposto", "g", 70, DY)], XE, 250)
        E.frase(c, t, C["s07.b"], [("Δx", "g", 70, DX), ("=", "i", 70), ("cateto", "i", 70), ("adjacente", "g", 70, DX)], XE, 360)
        mfr(c, t, C["s07.c"], "oposto", "adjacente", XE, 540, 76, pre="tg θ = ")
        E.foco(c, t, C["s07.d"], 0.5, lambda a: (E.caixa_pontilhada(c, XE - 30, 630, 560, 150, a, COR),
                                                 E.formula(c, "m = tg θ", XE + 10, 740, 110, "g", COR, a)))
        E.frase(c, t, C["s07.e"], [("mais", "i", 66), ("em", "i", 66), ("pé:", "i", 66), ("m", "g", 66, COR), ("maior", "g", 66)], XE, 900)
    if t >= C["s07"]:
        E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    # um ângulo conhecido
    num_ponto(c, t, C["s08.a"] + 0.3, P2, *C1, None)
    num_ponto(c, t, C["s08.b"] + 0.3, P2, *D1, None)
    if t >= C["s08.b"] + 0.5:
        E.reta_pontos(c, t, C["s08.b"] + 0.5, P2, C1, D1, pontos=False, largura=6)
    degrau(c, t, P2, C1, D1, C["s08.c"], C["s08.c"] + 0.5, "3", "3", sombra=C["s08.c"] + 0.8, canto_t=C["s08.c"] + 0.9)
    teta(c, t, C["s08.d"], P2, C1, D1, "45°", r=90)
    if t >= C["s08.e"]:  # 60°: m = √3
        p = ease_io(prog(t, C["s08.e"], 0.8))
        M.line(c, *P2(*C1), *P2(1 + 8 / math.sqrt(3), 9), TINTA2, 0.9, 5, dash=E.TRACO, progress=p)
        E.foco(c, t, C["s08.e"] + 0.6, 0.4, lambda a: E.pilula(c, "60°: m = √3", *P2(3.2, 8.5), 34, "g", fundo=TINTA, a=a))
    if t >= C["s08.f"]:  # reta que desce
        p = ease_io(prog(t, C["s08.f"], 0.8))
        M.line(c, *P2(0, 7), *P2(5.5, 1.5), TINTA2, 0.9, 5, dash=E.TRACO, progress=p)
        E.foco(c, t, C["s08.f"] + 0.6, 0.4, lambda a: E.pilula(c, "desce: m < 0", *P2(1.5, 7.4), 34, "g", fundo=TINTA2, a=a))
    E.frase(c, t, C["s08"], [("um", "i", 70), ("ângulo", "i", 70), ("conhecido", "g", 70, COR)], XE, 250)
    par_em(c, t, C["s08.a"], "1", "1", XE, 360, 62)
    par_em(c, t, C["s08.b"], "4", "4", XE + 260, 360, 62)
    mfr(c, t, C["s08.c"], "3", "3", XE, 540, 90, pos="= 1", cp=COR, tpos=C["s08.c"] + 1.6, cpre=COR)
    conta_em(c, t, C["s08.d"], [("tg θ = 1", TINTA), ("  →  ", TINTA2), ("θ = 45°", COR)], XE, 700, 72)
    conta_em(c, t, C["s08.e"], [("60°:  ", TINTA2), ("m = r{3}", COR)], XE, 830, 72)
    E.frase(c, t, C["s08.f"], [("desce:", "i", 62), ("m", "g", 62, COR), ("negativo", "g", 62)], XE, 950)


# ---------------- alinhamento ----------------
def b_alinhamento(c, t, C, b):
    plano1(c, t, C["s09"])
    postes(c, t, C["s09"] + 0.3, C["s09"] + 0.4, C["s09"] + 0.5)
    seg(c, t, C["s09.b"], P1, Q1, Q2, largura=6)
    seg(c, t, C["s09.c"], P1, Q2, Q3, largura=6)
    if t >= C["s09.e"]:
        seg(c, t, C["s09.e"], P1, Q2, (5, 9), TINTA2, 0.6, 5, tracejado=True)
        anel(c, t, C["s09.e"], *P1(*Q2), ERRADO)
        anel(c, t, C["s09.e"] + 0.6, *P1(*Q2), ERRADO)
    degrau(c, t, P1, Q1, Q2, C["s10.a"], C["s10.a"] + 0.6, "2", "4", larg=9)
    degrau(c, t, P1, Q2, Q3, C["s10.b"], C["s10.b"] + 0.6, "2", "5", larg=9)

    def s09():
        E.frase(c, t, C["s09"], [("teste", "i", 72), ("de", "i", 72), ("alinhamento", "g", 72, COR)], XE, 250)
        E.frase(c, t, C["s09.a"], [("mesma", "i", 64), ("reta:", "i", 64), ("o", "i", 64), ("m", "g", 64, COR), ("não", "g", 64), ("muda", "i", 64)], XE, 370)
        E.frase(c, t, C["s09.b"], [("m", "g", 64, COR), ("do", "i", 64), ("1º", "g", 64), ("ao", "i", 64), ("2º", "g", 64)], XE, 500)
        E.frase(c, t, C["s09.c"], [("m", "g", 64, COR), ("do", "i", 64), ("2º", "g", 64), ("ao", "i", 64), ("3º", "g", 64)], XE, 600)
        E.frase(c, t, C["s09.d"], [("igual:", "g", 68, CERTO), ("alinhados", "i", 68)], XE, 760)
        E.frase(c, t, C["s09.e"], [("diferente:", "g", 68, ERRADO), ("a", "i", 68), ("linha", "i", 68), ("entorta", "g", 68)], XE, 870)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10"], [("nos", "i", 72), ("postes", "g", 72)], XE, 250)
    E.frase(c, t, C["s10.a"], [("1º", "g", 60), ("→", "g", 60), ("2º:", "g", 60)], XE, 430)
    mfr(c, t, C["s10.a"] + 0.6, "4", "2", XE + 300, 430, 84, pos="= 2", cp=COR, tpos=C["s10.a"] + 2.2)
    E.frase(c, t, C["s10.b"], [("2º", "g", 60), ("→", "g", 60), ("3º:", "g", 60)], XE, 620)
    mfr(c, t, C["s10.b"] + 0.6, "5", "2", XE + 300, 620, 84, pos="= 2,5", cp=COR, tpos=C["s10.b"] + 2.4)
    conta_em(c, t, C["s10.c"], [("2 ≠ 2,5", ERRADO)], XE, 810, 90)
    E.frase(c, t, C["s10.c"] + 0.8, [("não", "g", 70, ERRADO), ("estão", "i", 70), ("alinhados", "g", 70)], XE, 920)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano2(c, t, C["s11"])
    reta_ab(c, t, C["s11"] + 0.2, C["s11"] + 0.3, C["s11"] + 0.4)
    degrau(c, t, P2, A1, B1, C["s11"] + 0.6, C["s11"] + 0.9, "3", "6", sombra=C["s11"] + 1.0, canto_t=C["s11"] + 1.2)
    if t >= C["s11.c"]:  # a reta de 45°, para comparar
        p = ease_io(prog(t, C["s11.c"], 0.8))
        M.line(c, *P2(*A1), *P2(6, 7), TINTA2, 0.9, 5, dash=E.TRACO, progress=p)
        E.foco(c, t, C["s11.c"] + 0.6, 0.4, lambda a: E.pilula(c, "45°: m = 1", *P2(5.0, 5.0), 34, "g", fundo=TINTA2, a=a))
    E.frase(c, t, C["s11"], [("cuidado", "g", 90, ERRADO)], XE, 240)
    E.frase(c, t, C["s11.a"], [("dividir", "i", 70), ("ao", "i", 70), ("contrário", "g", 70, ERRADO)], XE, 360)
    mfr(c, t, C["s11.a"] + 1.2, "Δx", "Δy", XE + 640, 360, 66, pre="", cc=DX, cb=DY)
    mfr(c, t, C["s11.b"], "3", "6", XE, 540, 90, pre="", pos="= 0,5", cc=DX, cb=DY, cp=ERRADO, tpos=C["s11.b"] + 1.4)
    if t >= C["s11.c"] + 1.0:
        E.risco(c, XE - 10, 580, XE + 380, 470, t, C["s11.c"] + 1.0, largura=10)
    E.frase(c, t, C["s11.c"], [("mais", "i", 64), ("em", "i", 64), ("pé", "i", 64), ("que", "i", 64), ("45°:", "g", 64), ("m", "g", 64, COR),
                               (">", "g", 64), ("1", "g", 64)], XE, 700)
    mfr(c, t, C["s11.d"], "sobe", "anda", XE, 880, 76, pos="= 2", cp=CERTO, tpos=C["s11.d"] + 2.0)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("agora, o atalho do alinhamento", "i", 66, CLARO), W / 2, 150, "center", passo=0.12)
        E.frase(c, t, C["s12.a"], [("multiplique", "i", 80, CLARO), ("em", "i", 80, CLARO), ("cruz", "g", 80, BR)], W / 2, 260, "center")
        x1, x2, cy, s = 620, 1060, 520, 160
        E.foco(c, t, C["s12.b"], 0.5, lambda a: E.fracao(c, 4, 2, x1, cy, s, BR, a))
        E.foco(c, t, C["s12.c"], 0.5, lambda a: E.fracao(c, 5, 2, x2, cy, s, BR, a))
        E.foco(c, t, C["s12.c"] + 0.3, 0.5, lambda a: centro(c, "?", (x1 + x2) / 2, cy + 40, 110, "g", CLARO, a))
        for k, (p0, p1), txt, ty in (("s12.d", ((x1 + 60, cy - 90), (x2 - 60, cy + 90)), "4 × 2 = 8", 470),
                                     ("s12.e", ((x1 + 60, cy + 90), (x2 - 60, cy - 90)), "2 × 5 = 10", 640)):
            p = ep(t, C[k], 0.6)
            if p > 0:
                M.line(c, *p0, *p1, CLARO, 1.0, 7, progress=p)
            E.foco(c, t, C[k] + 0.2, 0.45, lambda a, txt=txt, ty=ty: E.escreve(c, txt, 1270, ty, 80, "g", BR, a))
        conta_em(c, t, C["s12.f"], [("8 ≠ 10", ERRADO)], W / 2, 860, 100, "center")
        E.frase(c, t, C["s12.f"] + 0.8, [("não", "g", 66, ERRADO), ("estão", "i", 70, CLARO), ("alinhados", "g", 66, BR)], W / 2, 970, "center")
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13"], [("por", "i", 70, CLARO), ("que", "i", 70, CLARO), ("funciona", "g", 70, BR)], W / 2, 170, "center")
    E.frase(c, t, C["s13.a"], [("frações", "i", 70, CLARO), ("iguais", "g", 66, BR), ("=", "i", 70, CLARO), ("produtos", "i", 70, CLARO),
                               ("em", "i", 70, CLARO), ("cruz", "i", 70, CLARO), ("iguais", "g", 66, BR)], W / 2, 330, "center", passo=0.12)
    E.frase(c, t, C["s13.a"] + 2.4, [("a", "i", 60, CLARO), ("proporção", "g", 60, BR)], W / 2, 430, "center")
    E.frase(c, t, C["s13.b"], [("foge", "i", 70, CLARO), ("da", "i", 70, CLARO), ("divisão", "g", 66, BR), ("que", "i", 70, CLARO), ("não", "i", 70, CLARO),
                               ("dá", "i", 70, CLARO), ("exata", "g", 66, BR)], W / 2, 600, "center", passo=0.12)
    E.frase(c, t, C["s13.c"], [("não", "g", 66, ERRADO), ("compensa", "i", 70, CLARO), ("com", "i", 70, CLARO), ("divisão", "i", 70, CLARO),
                               ("fácil:", "g", 66, BR)], W / 2, 800, "center")
    mfr(c, t, C["s13.c"] + 1.6, "6", "3", 820, 930, 84, pos="= 2", cc=DY_ESC, cb=DX_ESC, tinta=BR)


# ---------------- questão ----------------
QA, QB, QC = (-1, 4), (1, 1), (5, -5)


def plano4(c, t, t0):
    plano(c, t, t0, P4, marcas_x=[-2, 2, 4, 6], marcas_y=[-6, -4, -2, 2], size=34)
    tiques(c, t, t0, P4, (-1, 1, 3, 5), (-5, -3, -1, 1, 3, 4, 5))


def b_questao(c, t, C, b):
    plano4(c, t, C["s14"])
    num_ponto(c, t, C["s14.a"] + 0.3, P4, *QA, "A", lado=(-1, 0))
    num_ponto(c, t, C["s14.b"] + 0.3, P4, *QB, "B", lado=(-1, 1))
    num_ponto(c, t, C["s14.c"] + 0.3, P4, *QC, "C", lado=(1, 0))
    seg(c, t, C["s14.d"], P4, QA, QB, largura=7)
    E.foco(c, t, C["s14.d"] + 0.6, 0.4, lambda a: E.pilula(c, "m?", *P4(0.9, 3.4), 38, "g", fundo=DIST, a=a))
    E.foco(c, t, C["s14.e"] + 0.3, 0.4, lambda a: E.pilula(c, "alinhados?", *P4(3.6, -1.6), 36, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    letra_par(c, t, C["s14.a"], "A", "−1", "4", XE, 320, 66)
    letra_par(c, t, C["s14.b"], "B", "1", "1", XE, 420, 66)
    letra_par(c, t, C["s14.c"], "C", "5", "−5", XE, 520, 66)
    E.frase(c, t, C["s14.d"], [("m", "g", 66, COR), ("de", "i", 66), ("A", "g", 66), ("até", "i", 66), ("B?", "g", 66)], XE, 680)
    E.frase(c, t, C["s14.e"], [("os", "i", 66), ("três", "i", 66), ("estão", "i", 66), ("alinhados?", "g", 66, COR)], XE, 790)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=1000, cy=820, r=70)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    t0 = C["s16"] - 3
    plano4(c, t, t0)
    num_ponto(c, t, t0, P4, *QA, "A", lado=(-1, 0))
    num_ponto(c, t, t0, P4, *QB, "B", lado=(-1, 1))
    num_ponto(c, t, t0, P4, *QC, "C", lado=(1, 0))
    degrau(c, t, P4, QA, QB, C["s16.b"], C["s16.a"], "2", "−3", setas=True, size=46, emx=0.75)
    if t >= C["s16.d"]:
        E.reta_pontos(c, t, C["s16.d"], P4, QA, QB, pontos=False, largura=6)
    degrau(c, t, P4, QB, QC, C["s17.b"], C["s17.a"], "4", "−6", setas=True, size=46)
    if t >= C["s17.e"]:
        E.reta_pontos(c, t, C["s17.e"], P4, QA, QC, cor=CERTO, pontos=False, largura=8)

    def s16():
        E.frase(c, t, C["s16"], [("de", "i", 72), ("A", "g", 72), ("até", "i", 72), ("B", "g", 72)], XE, 230)
        conta_em(c, t, C["s16.a"], [("Δy", DY), (" = 1 − 4 = ", TINTA), ("−3", DY)], XE, 370, 72)
        conta_em(c, t, C["s16.b"], [("Δx", DX), (" = 1 − (−1) = ", TINTA), ("2", DX)], XE, 490, 72)
        mfr(c, t, C["s16.c"], "−3", "2", XE, 680, 96, pos="= −1,5", cp=COR, tpos=C["s16.c"] + 1.8, cpre=COR)
        E.frase(c, t, C["s16.d"], [("negativo:", "i", 66), ("a", "i", 66), ("reta", "i", 66), ("desce", "g", 66, COR)], XE, 860)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("de", "i", 72), ("B", "g", 72), ("até", "i", 72), ("C", "g", 72)], XE, 220)
    conta_em(c, t, C["s17.a"], [("Δy", DY), (" = −5 − 1 = ", TINTA), ("−6", DY)], XE, 340, 66)
    conta_em(c, t, C["s17.b"], [("Δx", DX), (" = 5 − 1 = ", TINTA), ("4", DX)], XE, 440, 66)
    E.foco(c, t, C["s17.c"] - 0.4, 0.5, lambda a: (fra(c, "−3", "2", XE, 590, 84, a, DY, DX), E.formula(c, "e", XE + 150, 590, 60, "i", TINTA2, a),
                                                  fra(c, "−6", "4", XE + 210, 590, 84, a, DY, DX)))
    conta_em(c, t, C["s17.c"], [("−3 × 4 = −12", TINTA)], XE, 750, 72)
    conta_em(c, t, C["s17.d"], [("2 × (−6) = −12", TINTA)], XE, 850, 72)
    E.frase(c, t, C["s17.e"], [("iguais:", "g", 70, CERTO), ("alinhados", "g", 70)], XE, 970)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s18.a", [("m", "g", 84, COR), ("=", "i", 84), ("Δy", "g", 84, DY), ("÷", "g", 84), ("Δx", "g", 84, DX)]),
                 ("s18.b", [("m", "g", 84, COR), ("=", "i", 84), ("tg", "g", 84), ("θ", "g", 84, COR), ("(ângulo", "i", 70, TINTA2), ("com", "i", 70, TINTA2),
                            ("o", "i", 70, TINTA2), ("eixo", "i", 70, TINTA2), ("x)", "i", 70, TINTA2)]),
                 ("s18.c", [("alinhados:", "g", 84), ("o", "i", 84), ("mesmo", "i", 84), ("m", "g", 84, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s19.a"], [("Equação", "g", 140, COR)], XE, 460)
    E.frase(c, t, C["s19.a"] + 0.4, [("da", "i", 120), ("reta", "g", 140, COR)], XE, 610)
    E.frase(c, t, C["s19.b"], [("reduzida,", "i", 70), ("geral", "i", 70), ("e", "i", 70), ("segmentária", "i", 70)], XE, 740)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, eme=b_eme, angulo=b_angulo, alinhamento=b_alinhamento, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
