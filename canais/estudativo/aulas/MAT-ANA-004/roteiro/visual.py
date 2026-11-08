"""Visual — Estudativo · MAT-ANA-004: equação da reta reduzida (y = mx + n), geral (ax + by + c = 0) e segmentária (x/p + y/q = 1).

Segue a linguagem da Geometria Analítica definida em MAT-ANA-001 e MAT-ANA-003 (leia os cabeçalhos de lá):
- plano à direita, texto à esquerda; x em índigo, y em preto; a reta em índigo; o triângulo da subida com Δx petróleo e Δy âmbar;
- nas equações, o m (inclinação) vem em índigo e o n (corte no eixo y) em preto dentro de uma pílula no eixo y, como o valor inicial
  da função afim (MAT-FUN-010); na segmentária, o número embaixo do x é índigo (corte no eixo x, pílula índigo) e o embaixo do y é preto;
- a forma que fica no fim de cada conta ganha caixa pontilhada; erro em vermelho, certo em verde; atalho no palco escuro.
Peças desta aula: eqn() (equação com partes coloridas, que entra no cue), corte_x()/corte_y() (pílulas dos cortes nos eixos) e
reta_eq() (reta pela equação reduzida, recortada na caixa do plano).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Analítica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANA-004_equacao_da_reta_reduzida_geral_segmentaria.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("reduzida", "geral", "segmentaria", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ENT, SAI = COR, TINTA
DX, DY, DIST = "#0E9AA7", "#D98A00", E.COR
DX_ESC, DY_ESC = "#3CC7D3", "#FFB833"
assert 2 * 1 + 1 == 3 and 3 - 2 == 1                      # y = 2x + 1 passa por (1, 3)
assert all(2 * x - (2 * x + 1) + 1 == 0 for x in range(-3, 4))  # 2x − y + 1 = 0 é a mesma reta
assert 3 / 3 + 0 / 2 == 1 and 0 / 3 + 2 / 2 == 1          # x/3 + y/2 = 1 corta em (3, 0) e (0, 2)
assert all(abs(2 * x + 3 * (-2 / 3 * x + 2) - 6) < 1e-9 for x in range(-3, 4))  # 2x + 3y − 6 = 0 ⇔ y = −2/3 x + 2
assert 3 * 1 + 2 == 5 and 4 / 4 + 0 == 1 and 0 + 5 / 5 == 1

P = E.Plano(1160, 170, 560, 720, -2, 5, -2, 7)        # y = 2x + 1 e (1, 3); x − 3 = 0
PS = E.Plano(1130, 220, 630, 630, -2, 5, -2, 5)       # x/3 + y/2 = 1
PQ = E.Plano(1180, 200, 540, 630, -1, 5, -1, 6)       # questão: y = 3x + 2 e x/4 + y/5 = 1


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




def _w(s, size, est="g"):
    return E.formula(None, s, 0, 0, size, est, a=0)


def eqn(c, t, t0, partes, x, y, size, align="left", caixa=None):
    """equação com partes coloridas que entra no cue; caixa = instante da caixa pontilhada em volta"""
    conta_em(c, t, t0, partes, x, y, size, align)
    if caixa is not None and t >= caixa:
        w = conta(None, partes, 0, 0, size, 0)
        x0 = x - w / 2 if align == "center" else x
        p = ep(t, caixa, 0.5)
        E.caixa_pontilhada(c, x0 - 30, y - size * 1.05, w + 60, size * 1.45, p, COR, prog_=p)


def pilula_em(c, t, t0, s, x, y, size=40, fundo=None):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, x, y, size, "g", fundo=fundo or COR, a=a))


def reta_eq(c, t, t0, P, A, B, cor=None, largura=7, d=0.8, tracejado=False, a=1.0):
    """reta por A e B (valores), de borda a borda da caixa do plano"""
    if t < t0 or a <= 0:
        return
    (ax, ay), (bx, by) = P(*A), P(*B)
    dx, dy = bx - ax, by - ay
    k = 1e4 / (math.hypot(dx, dy) or 1)
    x, y, w, h = P.caixa
    s = E._corta_caixa(ax - dx * k, ay - dy * k, ax + dx * k, ay + dy * k, x, y, w, h)
    if s:
        M.line(c, *s, cor or DIST, a, largura, dash=E.TRACO if tracejado else None, progress=ease_io(prog(t, t0, d)))


def corte_x(c, t, t0, P, v, s=None):
    E.ponto(c, t, t0, P, v, 0, None, cor=TINTA, r=14)
    pilula_em(c, t, t0 + 0.2, s or E._num(v), P.x(v), P.oy + 48, 38, ENT)


def corte_y(c, t, t0, P, v, s=None):
    E.ponto(c, t, t0, P, 0, v, None, cor=TINTA, r=14)
    pilula_em(c, t, t0 + 0.2, s or E._num(v), P.ox - 48, P.y(v), 38, SAI)


def plano_p(c, t, t0):
    plano(c, t, t0, P, marcas_x=[-2, 2, 4], marcas_y=[2, 4, 6], size=36)
    tiques(c, t, t0, P, (-1, 1, 3, 5), (-2, -1, 1, 3, 5, 7))


def plano_s(c, t, t0):
    plano(c, t, t0, PS, marcas_x=[-2, 2, 4], marcas_y=[-2, 2, 4], size=36)
    tiques(c, t, t0, PS, (-1, 1, 3, 5), (-1, 1, 3, 5))


def plano_q(c, t, t0):
    plano(c, t, t0, PQ, marcas_x=[2, 4], marcas_y=[2, 4, 6], size=36)
    tiques(c, t, t0, PQ, (-1, 1, 3, 5), (-1, 1, 3, 5))


RED = [("y = ", TINTA), ("2", COR), ("x + ", TINTA), ("1", TINTA)]          # y = 2x + 1
GER = [("2x − y + 1 = 0", TINTA)]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        plano_p(c, t, C["s01"] + 0.3)
        reta_eq(c, t, C["s01.c"], P, (0, 1), (1, 3))
        eqn(c, t, C["s01.a"], RED, XE, 330, 100)
        eqn(c, t, C["s01.b"], GER, XE, 490, 100)
        if t >= C["s01.c"]:  # as duas apontam para a mesma reta
            p = ep(t, C["s01.c"] + 0.3, 0.6)
            M.arrow(c, 760, 300, P.x(1.55) - 28, P.y(4.1), TINTA2, p, 4, 16, p)
            M.arrow(c, 1000, 460, P.x(0.85) - 28, P.y(2.7), TINTA2, p, 4, 16, p)
        E.frase(c, t, C["s01.c"], [("a", "i", 80), ("mesma", "g", 80, COR), ("reta", "g", 80, COR)], XE, 680)
        E.frase(c, t, C["s01.c"] + 0.8, ps("escrita de dois jeitos", "i", 64, TINTA2), XE, 780)
        E.frase(c, t, C["s01.d"], ps("a prova usa qualquer um", "i", 64), XE, 930, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, cena1)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("a", "i", 110), ("equação", "g", 120)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.6, [("da", "i", 110), ("reta", "g", 120, COR)], XE, 590)
        E.frase(c, t, C["s02.a"] + 3.0, ps("de um jeito para o outro", "i", 72, TINTA2), XE, 730, passo=0.12)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("três", "g", 80, COR, C["s03.a"]), ("coisas", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 190, "center")
    x, w, h = 230, 1460, 190
    itens = (("s03.b", "coeficiente angular", None), ("s03.c", "a lei por um ponto", "troque o ponto na fórmula"),
             ("s03.d", "isolar uma letra", "o mesmo de cada lado"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 260 + i * 225
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 320, y + h / 2, 46, a=a),
                                                     centro(c, str(i + 1), 320, y + h / 2 + 20, 56, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(l1, "g", 64, COR)], 420, y + 85)
        if l2:
            E.frase(c, t, C[k] + 0.6, [(l2, "i", 58)], 420, y + 160)
    mfr(c, t, C["s03.b"] + 1.4, "Δy", "Δx", 1100, 260 + 110, 64, pre="m = ")
    E.frase(c, t, C["s04"] - 2.6, ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 1000, "center", passo=0.1)


# ---------------- reduzida ----------------
def b_reduzida(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("equação", "i", 84), ("reduzida", "g", 84, COR)], W / 2, 230, "center")
        sz, y = 170, 500
        partes = [("y = ", TINTA), ("m", COR), ("x + ", TINTA), ("n", TINTA)]
        conta_em(c, t, C["s04.b"], partes, W / 2, y, sz, "center")
        wt = conta(None, partes, 0, 0, sz, 0)
        x0 = W / 2 - wt / 2
        xm = x0 + _w("y = ", sz) + _w("m", sz) / 2
        xn = x0 + _w("y = mx + ", sz) + _w("n", sz) / 2
        for k, xx, l1, cor in (("s04.c", xm, "inclinação", COR), ("s04.d", xn, "corte no eixo y", TINTA)):
            p = ep(t, C[k], 0.5)
            if p > 0:
                M.arrow(c, xx, y + 40, xx, y + 150, cor, p, 5, 18, p)
            E.foco(c, t, C[k] + 0.2, 0.4, lambda a, xx=xx, l1=l1, cor=cor: centro(c, l1, xx, y + 230, 62, "g", cor, a))
        E.frase(c, t, C["s04.d"] + 2.4, ps("o b da função afim: o valor inicial", "i", 56, TINTA2), W / 2, 900, "center", passo=0.1)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    plano_p(c, t, C["s05"])
    nome(c, t, C["s05.b"] + 0.3, P, 1, 3, None)
    E.foco(c, t, C["s05.b"] + 0.5, 0.4, lambda a: par(c, "1", "3", *P(2.3, 3.0), 42, a, "center"))
    reta_eq(c, t, C["s06.c"], P, (0, 1), (1, 3))
    corte_y(c, t, C["s06.c"] + 0.6, P, 1)
    anda(c, t, C["s06.d"], P, (0, 1), (1, 1), DX, 0.5, 7)
    anda(c, t, C["s06.d"] + 0.6, P, (1, 1), (1, 3), DY, 0.5, 7)
    E.foco(c, t, C["s06.d"] + 0.4, 0.4, lambda a: centro(c, "1", *P(0.5, 0.45), 44, "g", DX, a))
    E.foco(c, t, C["s06.d"] + 1.0, 0.4, lambda a: centro(c, "2", *P(1.35, 1.85), 44, "g", DY, a))

    E.frase(c, t, C["s05.a"], [("m", "g", 70, COR), ("=", "g", 70, COR), ("2", "g", 70, COR)], XE, 250)
    E.frase(c, t, C["s05.b"], [("passa", "i", 64), ("por", "i", 64)], XE + 300, 250)
    par_em(c, t, C["s05.b"] + 0.3, "1", "3", XE + 560, 250, 68)
    eqn(c, t, C["s05.c"], [("y = ", TINTA), ("2", COR), ("x + n", TINTA)], XE, 400, 76)
    eqn(c, t, C["s05.d"], [("3", SAI), (" = 2 · ", TINTA), ("1", ENT), (" + n", TINTA)], XE, 520, 76)
    eqn(c, t, C["s06.a"], [("3 = 2 + n", TINTA)], XE, 640, 76)
    eqn(c, t, C["s06.b"], [("n = 1", TINTA)], XE, 760, 76)
    pilula_em(c, t, C["s06.b"] + 0.3, "− 2 de cada lado", XE + 520, 735, 36, TINTA2)
    eqn(c, t, C["s06.c"], RED, XE, 920, 92, caixa=C["s06.c"] + 0.5)


# ---------------- geral ----------------
def b_geral(c, t, C, b):
    plano_p(c, t, C["s07"])
    reta_eq(c, t, C["s07"] + 0.3, P, (0, 1), (1, 3), a=1 - 0.6 * ep(t, C["s08.b"], 0.5))
    nome(c, t, C["s07"] + 0.5, P, 1, 3, None)
    if t >= C["s08.b"]:  # a reta em pé
        x, y, w, h = P.caixa
        M.line(c, P.x(3), y + h, P.x(3), y, COR, 1.0, 8, progress=ease_io(prog(t, C["s08.b"], 0.8)))
        corte_x(c, t, C["s08.b"] + 0.5, P, 3)
        E.foco(c, t, C["s08.b"] + 0.8, 0.4, lambda a: E.pilula(c, "x − 3 = 0", P.x(3) + 130, P.y(6.2), 38, "g", fundo=COR, a=a))
        if t >= C["s08.c"]:  # Δx = 0 entre dois pontos dela
            E.ponto(c, t, C["s08.c"], P, 3, 2, None, cor=TINTA, r=12)
            E.ponto(c, t, C["s08.c"] + 0.1, P, 3, 5, None, cor=TINTA, r=12)
            E.foco(c, t, C["s08.c"] + 0.3, 0.4, lambda a: E.pilula(c, "Δx = 0", P.x(3) + 110, P.y(3.5), 36, "g", fundo=DX, a=a))

    def s07():
        E.frase(c, t, C["s07.a"], [("equação", "i", 80), ("geral", "g", 80, COR)], XE, 240)
        E.frase(c, t, C["s07.b"], [("tudo", "g", 62), ("de", "i", 62), ("um", "i", 62), ("lado,", "i", 62), ("zero", "g", 62), ("do", "i", 62), ("outro", "i", 62)], XE, 350, passo=0.12)
        eqn(c, t, C["s07.c"], RED, XE, 500, 80)
        pilula_em(c, t, C["s07.c"] + 0.5, "− y de cada lado", XE + 620, 475, 36, TINTA2)
        eqn(c, t, C["s07.d"], [("0 = 2x − y + 1", TINTA)], XE, 650, 80)
        eqn(c, t, C["s07.e"], GER, XE, 830, 92, caixa=C["s07.e"] + 0.5)
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08"], [("para", "i", 76), ("que", "i", 76), ("outro", "i", 76), ("jeito?", "g", 76, COR)], XE, 240)
    E.frase(c, t, C["s08.a"], [("qualquer", "g", 64), ("reta,", "i", 66), ("até", "i", 66), ("a", "i", 66), ("reta", "i", 66), ("em", "i", 66), ("pé", "g", 64, COR)], XE, 360, passo=0.12)
    eqn(c, t, C["s08.b"], [("x − 3 = 0", COR)], XE, 520, 90)
    E.frase(c, t, C["s08.b"] + 1.0, ps("a reta vertical do x = 3", "i", 54, TINTA2), XE, 610, passo=0.1)
    eqn(c, t, C["s08.c"], [("Δx", DX), (" = 0", TINTA), ("  →  ", TINTA2), ("÷ 0", ERRADO)], XE, 760, 76)
    E.frase(c, t, C["s08.d"], [("sem", "i", 68), ("m", "g", 68, COR), ("e", "i", 68), ("sem", "i", 68), ("reduzida", "g", 68)], XE, 900)


# ---------------- segmentária ----------------
SEG = [("f{x}{3}", ENT), (" + ", TINTA), ("f{y}{2}", SAI), (" = 1", TINTA)]


def b_segmentaria(c, t, C, b):
    plano_s(c, t, C["s09"])
    reta_eq(c, t, C["s09.c"], PS, (3, 0), (0, 2))
    corte_x(c, t, C["s10.b"], PS, 3)
    E.foco(c, t, C["s10.b"] + 0.3, 0.4, lambda a: par(c, "3", "0", PS.x(3.3), PS.oy - 30, 42, a))
    corte_y(c, t, C["s10.d"], PS, 2)
    E.foco(c, t, C["s10.d"] + 0.3, 0.4, lambda a: par(c, "0", "2", PS.ox + 30, PS.y(2.35), 42, a))
    E.frase(c, t, C["s09.a"], [("equação", "i", 80), ("segmentária", "g", 80, COR)], XE, 240)
    sz, y = 110, 450
    eqn(c, t, C["s09.b"], SEG, XE, y, sz)
    w3 = _w("f{x}{3}", sz)
    wy = _w("f{x}{3} + ", sz)
    for k, xx, ww, cor in (("s10.a", XE, w3, ENT), ("s10.c", XE + wy, _w("f{y}{2}", sz), SAI)):
        p = ep(t, C[k], 0.4)
        if p > 0:
            E.caixa_pontilhada(c, xx - 12, y + 10, ww + 24, sz * 0.62, p, cor, prog_=p)
    E.frase(c, t, C["s09.c"], ps("os cortes nos eixos, sem conta", "i", 58, TINTA2), XE, 600, passo=0.1)

    def s10():
        E.frase(c, t, C["s10.a"], [("embaixo", "i", 62), ("do", "i", 62), ("x:", "g", 62, ENT), ("corte", "i", 62), ("em", "i", 62), ("x", "g", 62, ENT)], XE, 690, passo=0.12)
        par_em(c, t, C["s10.b"], "3", "0", XE + 700, 690, 62)
        E.frase(c, t, C["s10.c"], [("embaixo", "i", 62), ("do", "i", 62), ("y:", "g", 62), ("corte", "i", 62), ("em", "i", 62), ("y", "g", 62)], XE, 790, passo=0.12)
        par_em(c, t, C["s10.d"], "0", "2", XE + 700, 790, 62)
    E.saida(c, t, C["s10.e"] - 0.3, s10)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.e"] - 2.6, [("no", "i", 62), ("eixo", "i", 62), ("x,", "g", 62, ENT), ("o", "i", 62), ("y", "g", 62), ("vale", "i", 62), ("0", "g", 62)], XE, 720, passo=0.12)
    seq(c, t, [("f{x}{3}", ENT, C["s10.e"]), (" = 1", TINTA, C["s10.e"]), ("   →   ", TINTA2, C["s10.e"] + 1.6), ("x = 3", ENT, C["s10.e"] + 1.6)], XE, 880, 90)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano_s(c, t, C["s11"])
    reta_eq(c, t, C["s11"] + 0.3, PS, (3, 0), (0, 2))
    reta_eq(c, t, C["s11.c"] + 0.4, PS, (0, 2), (1, 4), ERRADO, 5, tracejado=True, a=1 - ep(t, C["s12.b"], 0.5))
    E.foco(c, t, C["s11.c"] + 1.0, 0.4, lambda a: E.pilula(c, "m = 2? sobe?", *PS(2.6, 4.4), 36, "g", fundo=ERRADO, a=a * (1 - ep(t, C["s12.b"], 0.5))))
    nome(c, t, C["s12.a"], PS, 0, 2, None)
    nome(c, t, C["s12.a"] + 0.3, PS, 3, 0, None)
    if t >= C["s12.b"]:
        anda(c, t, C["s12.b"], PS, (0.4, 2.9), (2.6, 1.4), CERTO, 0.8, 7)
        E.foco(c, t, C["s12.b"] + 0.6, 0.4, lambda a: E.pilula(c, "desce", *PS(2.4, 2.6), 38, "g", fundo=CERTO, a=a))

    def s11():
        E.frase(c, t, C["s11"], [("cuidado", "g", 90, ERRADO)], XE, 240)
        E.frase(c, t, C["s11.a"], [("ler", "i", 66), ("o", "i", 66), ("m", "g", 66, COR), ("direto", "g", 66, ERRADO), ("na", "i", 66), ("geral", "i", 66)], XE, 360)
        eqn(c, t, C["s11.a"] + 3.0, SEG, XE, 520, 76)
        pilula_em(c, t, C["s11.a"] + 4.2, "× 6", XE + 470, 500, 40, TINTA2)
        eqn(c, t, C["s11.b"], [("2", ERRADO), ("x + 3y − 6 = 0", TINTA)], XE, 690, 84)
        eqn(c, t, C["s11.c"], [("m = 2?", ERRADO)], XE, 850, 84)
        E.frase(c, t, C["s11.c"] + 0.8, [("sobe?", "g", 72, ERRADO)], XE + 360, 850)
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    eqn(c, t, C["s12"], [("2x + 3y − 6 = 0", TINTA2)], XE, 230, 60)
    E.frase(c, t, C["s12.a"], [("de", "i", 60)], XE, 350)
    par_em(c, t, C["s12.a"] + 0.2, "0", "2", XE + 80, 350, 60)
    E.frase(c, t, C["s12.a"] + 0.6, [("até", "i", 60)], XE + 290, 350)
    par_em(c, t, C["s12.a"] + 0.8, "3", "0", XE + 400, 350, 60)
    E.frase(c, t, C["s12.b"], [("desce", "g", 64, CERTO)], XE + 640, 350)
    eqn(c, t, C["s12.c"], [("3y = −2x + 6", TINTA)], XE, 500, 80)
    pilula_em(c, t, C["s12.d"] - 0.6, "÷ 3", XE + 600, 480, 40, TINTA2)
    eqn(c, t, C["s12.d"], [("y = ", TINTA), ("−f{2}{3}", COR), ("x + 2", TINTA)], XE, 690, 90, caixa=C["s12.d"] + 0.6)
    E.frase(c, t, C["s12.e"], [("na", "i", 64), ("geral,", "i", 64), ("isole", "g", 64, CERTO), ("o", "i", 64), ("y", "g", 64, CERTO), ("primeiro", "i", 64)], XE, 900)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    PT = [("y − y₀ = ", BR), ("m", CLARO), ("(x − x₀)", BR)]

    def s13_14():
        E.frase(c, t, C["s13"], ps("agora, o atalho: ponto e inclinação", "i", 64, CLARO), W / 2, 170, "center", passo=0.12)
        eqn(c, t, C["s13.a"], PT, W / 2, 340, 110, "center")
        E.frase(c, t, C["s13.a"] + 2.0, [("(x₀, y₀)", "b", 50, BR)] + ps("= o ponto dado", "i", 54, CLARO), W / 2, 430, "center", passo=0.1)
        eqn(c, t, C["s13.b"], [("y − 3 = ", BR), ("2", CLARO), ("(x − 1)", BR)], W / 2, 590, 96, "center")
        eqn(c, t, C["s14.a"], [("y − 3 = ", BR), ("2", CLARO), ("x − 2", BR)], W / 2, 730, 96, "center")
        eqn(c, t, C["s14.b"], [("y = ", BR), ("2", CLARO), ("x + 1", BR)], W / 2, 880, 110, "center")
        if t >= C["s14.b"] + 0.4:
            w = conta(None, [("y = 2x + 1", BR)], 0, 0, 110, 0)
            p = ep(t, C["s14.b"] + 0.4, 0.5)
            E.caixa_pontilhada(c, W / 2 - w / 2 - 30, 880 - 116, w + 60, 160, p, CLARO, prog_=p)
        pilula_em(c, t, C["s14.b"] + 0.3, "+ 3 de cada lado", 1500, 860, 36, COR)
        E.frase(c, t, C["s14.c"], ps("a mesma reta, numa linha só", "i", 54, CLARO), W / 2, 1000, "center", passo=0.1)
    E.saida(c, t, C["s15"] - 0.1, s13_14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"], [("por", "i", 70, CLARO), ("que", "i", 70, CLARO), ("funciona", "g", 70, BR)], W / 2, 170, "center")
    E.frase(c, t, C["s15.a"], ps("do ponto dado até qualquer outro ponto da reta", "i", 56, CLARO), W / 2, 290, "center", passo=0.1)
    seq(c, t, [("f{y − y₀}{x − x₀}", BR, C["s15.b"] - 1.0), (" = ", BR, C["s15.b"]), ("m", CLARO, C["s15.b"])], W / 2, 440, 90, "center")
    eqn(c, t, C["s15.b"] + 2.0, PT, W / 2, 610, 90, "center")
    pilula_em(c, t, C["s15.b"] + 1.6, "× (x − x₀)", 1560, 590, 36, COR)
    E.frase(c, t, C["s15.c"], [("não", "g", 64, ERRADO), ("compensa", "i", 68, CLARO), ("com", "i", 68, CLARO), ("o", "i", 68, CLARO), ("ponto", "i", 68, CLARO),
                               ("no", "i", 68, CLARO), ("eixo", "i", 68, CLARO), ("y", "g", 68, BR)], W / 2, 790, "center")
    E.foco(c, t, C["s15.c"] + 2.2, 0.5, lambda a: (par(c, "0", "5", 760, 920, 84, a, "center", (CLARO, BR)),
                                                  E.formula(c, "→   n = 5", 900, 920, 84, "g", BR, a)))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    plano_q(c, t, C["s16"])
    nome(c, t, C["s16.b"] + 0.3, PQ, 1, 5, None)
    E.foco(c, t, C["s16.b"] + 0.5, 0.4, lambda a: par(c, "1", "5", *PQ(2.3, 5.0), 42, a, "center"))
    E.foco(c, t, C["s16.a"] + 1.0, 0.4, lambda a: E.pilula(c, "m = 3", *PQ(3.6, 2.4), 40, "g", fundo=COR, a=a))
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], [("1)", "g", 64, COR), ("reduzida", "g", 64), ("e", "i", 64), ("geral", "g", 64)], XE, 330)
    E.frase(c, t, C["s16.a"] + 1.2, [("m", "g", 60, COR), ("=", "g", 60, COR), ("3,", "g", 60, COR), ("passa", "i", 60), ("por", "i", 60)], XE + 60, 430)
    par_em(c, t, C["s16.b"], "1", "5", XE + 500, 430, 60)
    E.frase(c, t, C["s16.c"], [("2)", "g", 64, COR), ("cortes", "g", 64), ("nos", "i", 64), ("eixos", "i", 64), ("de", "i", 64)], XE, 580)
    eqn(c, t, C["s16.c"] + 1.4, [("f{x}{4}", ENT), (" + ", TINTA), ("f{y}{5}", SAI), (" = 1", TINTA)], XE + 60, 720, 76)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1000, cy=800, r=70)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    plano_q(c, t, C["s18"] - 3)

    def r1():
        nome(c, t, C["s18"] - 3, PQ, 1, 5, None)
        reta_eq(c, t, C["s18.c"], PQ, (0, 2), (1, 5))
        corte_y(c, t, C["s18.c"] + 0.5, PQ, 2)
        E.foco(c, t, C["s18"] - 3, 0.4, lambda a: par(c, "1", "5", *PQ(2.3, 5.0), 42, a, "center"))
        eqn(c, t, C["s18.a"], [("y = ", TINTA), ("3", COR), ("x + n", TINTA)], XE, 250, 76)
        eqn(c, t, C["s18.b"], [("5", SAI), (" = 3 + n", TINTA)], XE, 380, 76)
        seq(c, t, [("n = 2", TINTA, C["s18.b"] + 2.0)], XE + 480, 380, 76)
        eqn(c, t, C["s18.c"], [("y = ", TINTA), ("3", COR), ("x + 2", TINTA)], XE, 560, 90, caixa=C["s18.c"] + 0.5)
        pilula_em(c, t, C["s18.d"] - 0.4, "− y de cada lado", XE + 280, 660, 34, TINTA2)
        eqn(c, t, C["s18.d"], [("3x − y + 2 = 0", TINTA)], XE, 790, 90, caixa=C["s18.d"] + 0.5)
    E.saida(c, t, C["s19"] - 0.1, r1)
    if t < C["s19"]:
        return
    reta_eq(c, t, C["s19"] + 0.2, PQ, (4, 0), (0, 5))
    corte_x(c, t, C["s19.a"] + 0.4, PQ, 4)
    corte_y(c, t, C["s19.b"] + 0.4, PQ, 5)
    eqn(c, t, C["s19"], [("f{x}{4}", ENT), (" + ", TINTA), ("f{y}{5}", SAI), (" = 1", TINTA)], XE, 330, 96)
    E.frase(c, t, C["s19.a"], [("corte", "i", 66), ("em", "i", 66), ("x:", "g", 66, ENT)], XE, 560)
    par_em(c, t, C["s19.a"] + 0.4, "4", "0", XE + 380, 560, 84)
    E.frase(c, t, C["s19.b"], [("corte", "i", 66), ("em", "i", 66), ("y:", "g", 66)], XE, 720)
    par_em(c, t, C["s19.b"] + 0.4, "0", "5", XE + 380, 720, 84)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", [("reduzida:", "g", 72, COR), ("inclinação", "i", 72), ("e", "i", 72), ("corte", "i", 72), ("no", "i", 72), ("y", "g", 72)]),
                 ("s20.b", [("geral:", "g", 72, COR), ("qualquer", "i", 72), ("reta", "i", 72)]),
                 ("s20.c", [("segmentária:", "g", 72, COR), ("os", "i", 72), ("cortes", "i", 72), ("nos", "i", 72), ("eixos", "i", 72)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s21.a"], [("Paralelas", "g", 130, COR)], XE, 450)
    E.frase(c, t, C["s21.b"], [("e", "i", 110), ("perpendiculares", "g", 110, COR)], XE, 600)
    E.frase(c, t, C["s21.b"] + 1.4, ps("só olhando o m", "i", 60, TINTA2), XE, 700)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, reduzida=b_reduzida, geral=b_geral, segmentaria=b_segmentaria, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
