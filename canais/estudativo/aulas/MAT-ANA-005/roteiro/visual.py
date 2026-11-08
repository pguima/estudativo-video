"""Visual — Estudativo · MAT-ANA-005: retas paralelas (mesmo m) e perpendiculares (m₁ · m₂ = −1).

Segue a linguagem da Geometria Analítica definida em MAT-ANA-001, 003 e 004 (leia os cabeçalhos de lá):
- plano à direita, texto à esquerda; x em índigo, y em preto; a reta dada em índigo, a reta achada em tinta preta;
- o degrau da reta (anda 1, sobe 2): andada em petróleo (DX), subida em âmbar (DY), como o triângulo da subida;
- O DEGRAU GIRANDO (degrau_giro): o degrau de m = 2 gira um quarto de volta em volta do ponto e cada lado LEVA A SUA COR:
  a subida âmbar vira andada e a andada petróleo vira descida. Por isso, em m = −1/2, o 1 de cima é petróleo e o 2 de baixo
  é âmbar: a cor mostra o número virando de cabeça para baixo;
- ângulo reto = quadradinho (E.angulo); erro em vermelho, certo em verde; atalho no palco escuro.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Analítica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANA-005_retas_paralelas_e_perpendiculares.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("paralelas", "perpendiculares", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ENT, SAI = COR, TINTA
DX, DY, DIST = "#0E9AA7", "#D98A00", E.COR
DX_ESC, DY_ESC = "#3CC7D3", "#FFB833"
assert 2 * (-0.5) == -1 and abs((2 * 1.2 + 1) - (-1.2 / 2 + 4)) < 1e-12                     # gancho: cruzam em (1,2; 3,4)
assert 2 * 0 + 3 == 3 and -0.5 * 2 + 1 == 0 and -1 + 1 == 0                 # paralela y = 2x + 3; perpendicular y = −x/2 + 1
assert 2 * (-2) == -4 != -1 and -3 * (1 / 3) == -1 and (-1 / 4) * 4 == -1
assert -3 * 1 + 7 == 4 and abs((1 / 3) * 3 + 1 - 2) < 1e-12               # questão

PG = E.Plano(1140, 150, 630, 720, -2, 5, -1, 7)       # gancho: y = 2x + 1 e y = −x/2 + 4
PP = E.Plano(1180, 150, 560, 720, -3, 4, -2, 7)       # paralelas
PR = E.Plano(1140, 170, 630, 720, -3, 4, -2, 6)       # perpendiculares: y = 2x + 1 e y = −x/2 + 1
PQ = E.Plano(1200, 150, 525, 750, -1, 6, -2, 8)       # questão: y = −3x + 5


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




def plano_de(c, t, t0, P, mx, my):
    todos_x = [v for v in range(int(P.xmin), int(P.xmax) + 1) if v != 0 and v not in mx]
    todos_y = [v for v in range(int(P.ymin), int(P.ymax) + 1) if v != 0 and v not in my]
    plano(c, t, t0, P, marcas_x=mx, marcas_y=my, size=36)
    tiques(c, t, t0, P, todos_x, todos_y)


def reta_m(c, t, t0, P, m, n, cor=None, largura=7, tracejado=False, a=1.0, d=0.8):
    """reta y = mx + n"""
    reta_eq(c, t, t0, P, (0, n), (1, m + n), cor, largura, d, tracejado, a)


def reto(c, t, t0, P, V, A, B, cor=TINTA):
    """quadradinho do ângulo reto entre as retas VA e VB (valores)"""
    E.angulo(c, t, t0, P(*V), P(*A), P(*B), r=62, cor=cor, preenche=0.14)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        plano_de(c, t, C["s01"] + 0.2, PG, [-2, 2, 4], [2, 4, 6])
        reta_m(c, t, C["s01.a"] + 0.3, PG, 2, 1)
        reta_m(c, t, C["s01.b"] + 0.3, PG, -0.5, 4, TINTA)
        if t >= C["s01.c"]:
            reto(c, t, C["s01.c"], PG, (1.2, 3.4), (2.2, 5.4), (3.2, 2.4), COR)
            anel(c, t, C["s01.c"], *PG(1.2, 3.4))
        eqn(c, t, C["s01.a"], [("y = ", TINTA), ("2", COR), ("x + 1", TINTA)], XE, 300, 92)
        eqn(c, t, C["s01.b"], [("y = ", TINTA), ("−f{1}{2}", COR), ("x + 4", TINTA)], XE, 460, 92)
        q = ep(t, C["s01.e"], 0.4)
        if q > 0:
            E.caixa_pontilhada(c, XE + _w("y = ", 92) - 14, 300 - 90, _w("2", 92) + 28, 110, q, COR, prog_=q)
            E.caixa_pontilhada(c, XE + _w("y = ", 92) - 14, 460 - 120, _w("−f{1}{2}", 92) + 28, 170, q, COR, prog_=q)
        E.frase(c, t, C["s01.c"], [("ângulo", "g", 80, COR), ("reto", "g", 80, COR)], XE, 680)
        E.frase(c, t, C["s01.c"] + 1.0, ps("um canto de esquadro", "i", 60, TINTA2), XE, 770, passo=0.12)
        E.frase(c, t, C["s01.d"], [("sem", "i", 72), ("desenhar", "g", 72), ("nada", "i", 72)], XE, 920)
    E.saida(c, t, C["s02"] - 0.1, cena1)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 280)
        E.frase(c, t, C["s02.a"] + 1.0, [("paralelas", "g", 120)], XE, 430)
        E.frase(c, t, C["s02.a"] + 1.4, [("e", "i", 100), ("perpendiculares", "g", 100, COR)], XE, 570)
        E.frase(c, t, C["s02.a"] + 2.4, [("pelo", "i", 84), ("m", "g", 90, COR)], XE, 700)
        E.frase(c, t, C["s02.b"], ps("e a equação de cada uma", "i", 66, TINTA2), XE, 830, passo=0.12)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("uma", "g", 80, COR, C["s03.a"]), ("coisa", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 200, "center")
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, 330, 270, 1260, 600, p, prog_=p)
    E.frase(c, t, C["s03.b"], [("a", "i", 70), ("equação", "g", 70, COR), ("reduzida", "g", 70, COR)], W / 2, 370, "center")
    sz, y = 150, 590
    partes = [("y = ", TINTA), ("m", COR), ("x + ", TINTA), ("n", TINTA)]
    conta_em(c, t, C["s03.b"] + 0.8, partes, W / 2, y, sz, "center")
    x0 = W / 2 - conta(None, partes, 0, 0, sz, 0) / 2
    xm = x0 + _w("y = ", sz) + _w("m", sz) / 2
    xn = x0 + _w("y = mx + ", sz) + _w("n", sz) / 2
    for k, xx, l1, cor in (("s03.c", xm, "inclinação", COR), ("s03.d", xn, "corte no eixo y", TINTA)):
        q = ep(t, C[k], 0.5)
        if q > 0:
            M.arrow(c, xx, y + 30, xx, y + 120, cor, q, 5, 18, q)
        E.foco(c, t, C[k] + 0.2, 0.4, lambda a, xx=xx, l1=l1, cor=cor: centro(c, l1, xx, y + 200, 58, "g", cor, a))
    E.frase(c, t, C["s04"] - 2.4, ps("faltou? procure no canal", "i", 52, TINTA2), W / 2, 980, "center", passo=0.1)


# ---------------- paralelas ----------------
def b_paralelas(c, t, C, b):
    def trilhos():
        plano_de(c, t, C["s04"], PP, [-2, 2, 4], [2, 4, 6])
        reta_m(c, t, C["s04.a"], PP, 2, -2)
        reta_m(c, t, C["s04.a"] + 0.4, PP, 2, 1, TINTA)
        for i, (x0, n) in enumerate(((1, -2), (-1, 1))):
            y0 = 2 * x0 + n
            t0 = C["s04.b"] + 0.3 * i
            anda(c, t, t0, PP, (x0, y0), (x0 + 1, y0), DX, 0.5, 7)
            anda(c, t, t0 + 0.5, PP, (x0 + 1, y0), (x0 + 1, y0 + 2), DY, 0.5, 7)
        if t >= C["s04.c"]:  # uma reta que sobe mais cruza a outra
            reta_m(c, t, C["s04.c"], PP, 3.2, -4.4, ERRADO, 5, True, 1 - ep(t, C["s05"], 0.4))
            X, Y = PP(2, 2)
            k = ease_back(prog(t, C["s04.c"] + 0.7, 0.4)) * (1 - ep(t, C["s05"], 0.4))
            if k > 0:
                c.drawCircle(X, Y, 16 * k, M.paint(ERRADO))
                anel(c, t, C["s04.c"] + 0.7, X, Y, ERRADO)
        pilula_em(c, t, C["s05.a"], "m = 2", *PP(2.95, 4.6), 36, COR)
        pilula_em(c, t, C["s05.a"] + 0.2, "m = 2", *PP(-1.7, 0.2), 36, TINTA)
    E.saida(c, t, C["s06"] - 0.1, trilhos)

    def s04_05():
        E.frase(c, t, C["s04.a"], [("paralelas", "g", 84, COR)], XE, 260)
        E.frase(c, t, C["s04.a"] + 0.8, ps("nunca se encontram", "i", 66), XE, 360)
        E.frase(c, t, C["s04.a"] + 2.4, ps("como trilhos de trem", "i", 56, TINTA2), XE, 440, passo=0.12)
        E.frase(c, t, C["s04.b"], [("a", "i", 66), ("mesma", "g", 66), ("inclinação", "g", 66, COR)], XE, 570)
        E.frase(c, t, C["s04.c"], [("subiu", "i", 62), ("mais:", "i", 62), ("cruza", "g", 62, ERRADO)], XE, 680)
        E.frase(c, t, C["s05.a"], [("mesmo", "g", 70), ("m,", "g", 70, COR), ("só", "i", 70), ("o", "i", 70), ("n", "g", 70), ("muda", "i", 70)], XE, 830)
        E.frase(c, t, C["s05.b"], [("n", "g", 60), ("igual", "i", 60), ("também:", "i", 60), ("a", "i", 60), ("mesma", "g", 60), ("reta", "g", 60)], XE, 940)
    E.saida(c, t, C["s06"] - 0.1, s04_05)
    if t < C["s06"]:
        return
    plano_de(c, t, C["s06"], PP, [-2, 2, 4], [2, 4, 6])
    reta_m(c, t, C["s06.a"], PP, 2, 0)
    nome(c, t, C["s06.b"] + 0.3, PP, 0, 3, None)
    E.foco(c, t, C["s06.b"] + 0.5, 0.4, lambda a: par(c, "0", "3", PP.ox - 150, PP.y(3) + 14, 42, a, "center"))
    reta_m(c, t, C["s06.e"], PP, 2, 3, TINTA)
    if t >= C["s06.f"]:
        for x0 in (-1, 1):
            anda(c, t, C["s06.f"] + 0.3 * (x0 + 1), PP, (x0, 2 * x0), (x0, 2 * x0 + 3), TINTA2, 0.6, 5)
        E.foco(c, t, C["s06.f"] + 0.8, 0.4, lambda a: E.pilula(c, "+3", *PP(1.55, 3.2), 36, "g", fundo=TINTA, a=a))
    eqn(c, t, C["s06.a"], [("y = ", TINTA), ("2", COR), ("x", TINTA)], XE, 260, 80)
    E.frase(c, t, C["s06.b"], [("passa", "i", 62), ("por", "i", 62)], XE, 380)
    par_em(c, t, C["s06.b"] + 0.3, "0", "3", XE + 250, 380, 66)
    eqn(c, t, C["s06.c"], [("m = 2", COR)], XE, 510, 76)
    E.frase(c, t, C["s06.c"] + 0.6, ps("igual ao da reta dada", "i", 50, TINTA2), XE + 300, 505, passo=0.1)
    eqn(c, t, C["s06.d"], [("n = 3", TINTA)], XE, 630, 76)
    E.frase(c, t, C["s06.d"] + 0.6, ps("o ponto está no eixo y", "i", 50, TINTA2), XE + 300, 625, passo=0.1)
    eqn(c, t, C["s06.e"], [("y = ", TINTA), ("2", COR), ("x + 3", TINTA)], XE, 800, 96, caixa=C["s06.e"] + 0.5)
    E.frase(c, t, C["s06.f"], ps("3 unidades acima", "i", 56, TINTA2), XE, 930)


# ---------------- perpendiculares ----------------
O = (0, 1)


def _rot(v, ang):
    a = math.radians(ang)
    return (v[0] * math.cos(a) - v[1] * math.sin(a), v[0] * math.sin(a) + v[1] * math.cos(a))


def degrau_giro(c, t, C, a=1.0):
    """o degrau de m = 2 (anda 1, sobe 2) a partir de O gira um quarto de volta; cada lado leva a sua cor"""
    if t < C["s07.b"] or a <= 0:
        return
    g = ease_io(prog(t, C["s07.c"], 1.4))
    ang = -90 * g
    s1 = ease_io(prog(t, C["s08.a"], 0.8))   # a subida (âmbar) sobe e vira andada
    s2 = ease_io(prog(t, C["s08.b"], 0.8))   # a andada (petróleo) vai para a ponta e vira descida
    r1, r2 = _rot((1, 0), ang), _rot((1, 2), ang)
    A1 = (O[0] + r1[0], O[1] + r1[1])
    A2 = (O[0] + r2[0], O[1] + r2[1])
    am0, am1 = (A1[0], A1[1] + s1), (A2[0], A2[1] + s1)
    pe0, pe1 = (O[0] + 2 * s2, O[1]), (A1[0] + 2 * s2, A1[1])
    hm = ((O[0] + A2[0]) / 2, (O[1] + A2[1]) / 2)
    pa = ease_io(prog(t, C["s07.b"], 0.6))
    pb = ease_io(prog(t, C["s07.b"] + 0.7, 0.6))
    if pa > 0:
        M.line(c, *PR(*pe0), *PR(*pe1), DX, a, 10, progress=pa)
    if pb > 0:
        M.line(c, *PR(*am0), *PR(*am1), DY, a, 10, progress=pb)

    def rotulo(p0, p1, s, cor, t0):
        mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
        ux, uy = p1[0] - p0[0], p1[1] - p0[1]
        n = math.hypot(ux, uy) or 1
        nx, ny = -uy / n, ux / n
        if (mx + nx - hm[0]) ** 2 + (my + ny - hm[1]) ** 2 < (mx - hm[0]) ** 2 + (my - hm[1]) ** 2:
            nx, ny = -nx, -ny
        E.foco(c, t, t0, 0.4, lambda q: centro(c, s, *PR(mx + nx * 0.36, my + ny * 0.36 - 0.18), 52, "g", cor, q * a))
    rotulo(pe0, pe1, "1", DX, C["s07.b"] + 0.4)
    rotulo(am0, am1, "2", DY, C["s07.b"] + 1.1)
    # seta do giro
    if 0 < prog(t, C["s07.c"], 1.4) and t < C["s07.c"] + 2.4:
        q = 1 - ep(t, C["s07.c"] + 1.8, 0.5)
        X, Y = PR(*O)
        r = 2.6 * 90
        ini = math.degrees(math.atan2(-2, 1))
        E.arco(c, X, Y, r, ini, 90 * g, TINTA2, 5, q)
        if g > 0.05:
            ae = math.radians(ini + 90 * g)
            ex, ey = X + r * math.cos(ae), Y + r * math.sin(ae)
            tg = ae + math.pi / 2
            pth = skia.Path()
            pth.moveTo(ex + 22 * math.cos(tg), ey + 22 * math.sin(tg))
            pth.lineTo(ex + 14 * math.cos(tg + 2.2), ey + 14 * math.sin(tg + 2.2))
            pth.lineTo(ex + 14 * math.cos(tg - 2.2), ey + 14 * math.sin(tg - 2.2))
            pth.close()
            c.drawPath(pth, M.paint(TINTA2, q))


def b_perpendiculares(c, t, C, b):
    plano_de(c, t, C["s07"], PR, [-2, 2, 4], [2, 4, 6])
    reta_m(c, t, C["s07"] + 0.4, PR, 2, 1)
    nome(c, t, C["s07"] + 0.6, PR, *O, None)
    degrau_giro(c, t, C, 1 - 0.75 * ep(t, C["s10"], 0.5))
    reta_m(c, t, C["s08.c"], PR, -0.5, 1, TINTA)
    if t >= C["s08.c"] + 0.6:
        reto(c, t, C["s08.c"] + 0.6, PR, O, (1, 3), (-1, 1.5), COR)

    def s07():
        E.frase(c, t, C["s07.a"], [("perpendiculares", "g", 80, COR)], XE, 260)
        E.frase(c, t, C["s07.a"] + 1.2, ps("cruzam em ângulo reto", "i", 62), XE, 350)
        E.frase(c, t, C["s07.b"], [("m", "g", 66, COR), ("=", "g", 66, COR), ("2:", "g", 66, COR), ("anda", "i", 66), ("1,", "g", 66, DX),
                                   ("sobe", "i", 66), ("2", "g", 66, DY)], XE, 520)
        E.frase(c, t, C["s07.c"], [("gire", "g", 70), ("um", "i", 70), ("quarto", "i", 70), ("de", "i", 70), ("volta", "g", 70)], XE, 680)
        E.frase(c, t, C["s07.c"] + 1.6, ps("como quem vira um esquadro", "i", 54, TINTA2), XE, 770, passo=0.1)
    E.saida(c, t, C["s08"] - 0.1, s07)

    def s08():
        E.frase(c, t, C["s08.a"], [("a", "i", 64), ("subida", "g", 64, DY), ("vira", "i", 64), ("andada", "g", 64)], XE, 260)
        E.frase(c, t, C["s08.b"], [("a", "i", 64), ("andada", "g", 64, DX), ("vira", "i", 64), ("descida", "g", 64)], XE, 370)
        E.frase(c, t, C["s08.c"], [("anda", "i", 66), ("2,", "g", 66, DY), ("desce", "i", 66), ("1", "g", 66, DX)], XE, 520)
        mfr(c, t, C["s08.d"], "−1", "2", XE, 730, 110, pos="= −f{1}{2}", cc=DX, cb=DY, cp=COR, tpos=C["s08.d"] + 1.4, cpre=TINTA)
    if t >= C["s08"]:
        E.saida(c, t, C["s09"] - 0.1, s08)

    def s09():
        E.frase(c, t, C["s09"], ps("o que aconteceu com o 2?", "i", 66), XE, 240, passo=0.12)
        seq(c, t, [("f{2}{1}", TINTA, C["s09.a"]), ("  →  ", TINTA2, C["s09.a"] + 0.5), ("f{1}{2}", TINTA, C["s09.a"] + 0.5)], XE, 410, 96)
        E.frase(c, t, C["s09.a"] + 1.2, ps("de cabeça para baixo", "i", 50, TINTA2), XE + 460, 405, passo=0.1)
        seq(c, t, [("f{1}{2}", TINTA, C["s09.b"]), ("  →  ", TINTA2, C["s09.b"]), ("−f{1}{2}", COR, C["s09.b"] + 0.5)], XE, 590, 96)
        E.frase(c, t, C["s09.b"] + 1.0, ps("troca o sinal", "i", 50, TINTA2), XE + 460, 585)
        eqn(c, t, C["s09.c"], [("2 · ", TINTA), ("(−f{1}{2})", COR), (" = −1", TINTA)], XE, 760, 90)
        eqn(c, t, C["s09.d"], [("m₁ · m₂ = −1", COR)], XE, 920, 96, caixa=C["s09.d"] + 0.4)
        E.frase(c, t, C["s09.d"] + 3.0, ps("(se nenhuma das retas estiver em pé)", "i", 46, TINTA2), XE, 1015, passo=0.1)
    if t >= C["s09"]:
        E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    nome(c, t, C["s10.b"] + 0.3, PR, 2, 0, None)
    if t >= C["s10.b"] + 0.3:
        anel(c, t, C["s10.b"] + 0.3, *PR(2, 0), TINTA)
    E.foco(c, t, C["s10.b"] + 0.5, 0.4, lambda a: par(c, "2", "0", PR.x(3.2), PR.y(0.75), 42, a, "center"))
    eqn(c, t, C["s10.a"], [("y = ", TINTA), ("2", COR), ("x + 1", TINTA)], XE, 240, 70)
    E.frase(c, t, C["s10.b"], [("por", "i", 60)], XE + 470, 240)
    par_em(c, t, C["s10.b"] + 0.3, "2", "0", XE + 580, 240, 62)
    eqn(c, t, C["s10.c"], [("m = −f{1}{2}", COR)], XE, 390, 76)
    eqn(c, t, C["s10.d"], [("0", SAI), (" = −f{1}{2}", COR), (" · ", TINTA), ("2", ENT), (" + n", TINTA)], XE, 550, 76)
    eqn(c, t, C["s10.e"], [("0 = −1 + n", TINTA)], XE, 700, 76)
    seq(c, t, [("n = 1", TINTA, C["s10.e"] + 1.6)], XE + 500, 700, 76)
    eqn(c, t, C["s10.f"], [("y = ", TINTA), ("−f{1}{2}", COR), ("x + 1", TINTA)], XE, 890, 96, caixa=C["s10.f"] + 0.5)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano_de(c, t, C["s11"], PR, [-2, 2, 4], [2, 4, 6])
    reta_m(c, t, C["s11"] + 0.3, PR, 2, 1)
    nome(c, t, C["s11"] + 0.5, PR, *O, None)
    reta_m(c, t, C["s11.d"], PR, -2, 1, ERRADO, 6, True)
    if t >= C["s11.d"] + 0.6:
        X, Y = PR(*O)
        E.angulo(c, t, C["s11.d"] + 0.6, (X, Y), PR(1, 3), PR(1, -1), None, r=80, cor=ERRADO, preenche=0.15)
        E.foco(c, t, C["s11.d"] + 1.0, 0.4, lambda a: E.pilula(c, "torto", PR.x(1.6), PR.y(1.0), 36, "g", fundo=ERRADO, a=a))
    reta_m(c, t, C["s11.e"] + 0.4, PR, -0.5, 1, CERTO, 6)
    if t >= C["s11.e"] + 1.0:
        reto(c, t, C["s11.e"] + 1.0, PR, O, (1, 3), (-1, 1.5), CERTO)
    E.frase(c, t, C["s11"], [("cuidado", "g", 90, ERRADO)], XE, 240)
    E.frase(c, t, C["s11.a"], [("trocar", "i", 70), ("só", "g", 70, ERRADO), ("o", "i", 70), ("sinal", "i", 70)], XE, 360)
    eqn(c, t, C["s11.b"], [("m = 2", COR), ("  →  ", TINTA2), ("m = −2", ERRADO)], XE, 500, 76)
    eqn(c, t, C["s11.c"], [("2 · (−2) = −4", ERRADO)], XE, 640, 76)
    E.frase(c, t, C["s11.c"] + 1.6, [("não", "g", 56, ERRADO), ("dá", "i", 58), ("−1", "g", 56)], XE + 560, 635)
    E.frase(c, t, C["s11.d"], ps("sem canto reto", "i", 60, TINTA2), XE, 760)
    E.frase(c, t, C["s11.e"], [("troque", "i", 62), ("o", "i", 62), ("sinal", "g", 62, CERTO), ("e", "i", 62), ("vire", "g", 62, CERTO),
                               ("o", "i", 62), ("número", "i", 62)], XE, 880)
    eqn(c, t, C["s11.e"] + 0.8, [("m = −f{1}{2}", CERTO)], XE + 40, 990, 64)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("agora, o atalho", "i", 70, CLARO), W / 2, 170, "center")
        E.frase(c, t, C["s12.a"], [("inverte", "g", 96, BR), ("e", "i", 96, CLARO), ("troca", "g", 96, BR), ("o", "i", 96, CLARO), ("sinal", "g", 96, BR)],
                W / 2, 330, "center")
        for k, de, para, y in (("s12.b", "2", "−f{1}{2}", 520), ("s12.c", "−3", "f{1}{3}", 700), ("s12.d", "−f{1}{4}", "4", 880)):
            xd = 720
            E.foco(c, t, C[k], 0.5, lambda a, de=de, y=y: E.formula(c, de, xd, y, 100, "g", BR, a, "right"))
            E.foco(c, t, C[k] + 0.3, 0.5, lambda a, y=y: E.formula(c, "→", W / 2 - 60, y, 100, "g", CLARO, a))
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, para=para, y=y: E.formula(c, para, 1200, y, 100, "g", DY_ESC, a))
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return

    def s13ab():
        E.frase(c, t, C["s13"], [("por", "i", 70, CLARO), ("que", "i", 70, CLARO), ("funciona", "g", 70, BR)], W / 2, 170, "center")
        eqn(c, t, C["s13.a"], [("2 · f{1}{2} = 1", BR)], W / 2, 360, 96, "center")
        E.frase(c, t, C["s13.a"] + 1.4, ps("um número vezes ele de cabeça para baixo", "i", 52, CLARO), W / 2, 460, "center", passo=0.1)
        eqn(c, t, C["s13.b"], [("2 · ", BR), ("(−f{1}{2})", DY_ESC), (" = −1", BR)], W / 2, 640, 96, "center")
        E.frase(c, t, C["s13.b"] + 1.4, ps("o sinal trocado deixa o produto negativo", "i", 52, CLARO), W / 2, 740, "center", passo=0.1)
    E.saida(c, t, C["s13.c"] - 0.1, s13ab)
    if t < C["s13.c"]:
        return
    E.frase(c, t, C["s13.c"], [("não", "g", 70, ERRADO), ("funciona", "i", 76, CLARO), ("com", "i", 76, CLARO), ("m", "g", 76, BR), ("=", "g", 76, BR),
                               ("0", "g", 76, BR)], W / 2, 210, "center")
    cx, cy = W / 2 + 120, 640
    p = ep(t, C["s13.c"] + 1.0, 0.7)
    if p > 0:
        M.line(c, cx - 520, cy, cx + 520, cy, BR, 1, 7, progress=p)
        E.foco(c, t, C["s13.c"] + 1.4, 0.4, lambda a: (E.formula(c, "y = 3", cx + 300, cy - 30, 60, "g", BR, a),
                                                      E.formula(c, "m = 0", cx + 300, cy + 80, 50, "g", CLARO, a)))
    E.frase(c, t, C["s13.c"] + 2.4, ps("0 não vira de cabeça para baixo", "i", 54, CLARO), 460, 400, "center", passo=0.1)
    q = ep(t, C["s13.d"], 0.7)
    if q > 0:
        M.line(c, cx - 180, cy + 300, cx - 180, cy - 260, DY_ESC, 1, 7, progress=q)
        E.foco(c, t, C["s13.d"] + 0.5, 0.4, lambda a: (E.formula(c, "x = 2", cx - 470, cy - 160, 60, "g", DY_ESC, a),
                                                      E.formula(c, "sem m", cx - 470, cy - 80, 50, "g", CLARO, a)))
        E.angulo(c, t, C["s13.d"] + 0.6, (cx - 180, cy), (cx + 100, cy), (cx - 180, cy - 200), r=60, cor=BR, preenche=0.15)
    E.frase(c, t, C["s13.d"] + 4.0, [("aqui", "i", 60, CLARO), ("a", "i", 60, CLARO), ("regra", "i", 60, CLARO), ("não", "g", 60, ERRADO), ("vale", "g", 60, BR)],
            W / 2, 1010, "center")


# ---------------- questão ----------------
def plano_q(c, t, t0):
    plano_de(c, t, t0, PQ, [2, 4, 6], [-2, 2, 4, 6, 8])


def b_questao(c, t, C, b):
    plano_q(c, t, C["s14"])
    reta_m(c, t, C["s14.a"] + 0.4, PQ, -3, 5)
    E.foco(c, t, C["s14.a"] + 1.0, 0.4, lambda a: E.pilula(c, "r", *PQ(2.8, -1.3), 40, "g", fundo=COR, a=a))
    nome(c, t, C["s14.b"] + 0.3, PQ, 1, 4, None)
    E.foco(c, t, C["s14.b"] + 0.5, 0.4, lambda a: par(c, "1", "4", *PQ(2.3, 4.0), 40, a, "center"))
    nome(c, t, C["s14.c"] + 0.3, PQ, 3, 2, None)
    E.foco(c, t, C["s14.c"] + 0.5, 0.4, lambda a: par(c, "3", "2", *PQ(4.3, 2.0), 40, a, "center"))
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    eqn(c, t, C["s14.a"], [("r:  y = ", TINTA), ("−3", COR), ("x + 5", TINTA)], XE, 330, 76)
    E.frase(c, t, C["s14.b"], [("paralela", "g", 64), ("a", "i", 64), ("r", "g", 64, COR), ("por", "i", 64)], XE, 480)
    par_em(c, t, C["s14.b"] + 0.5, "1", "4", XE + 520, 480, 64)
    E.frase(c, t, C["s14.c"], [("perpendicular", "g", 64), ("a", "i", 64), ("r", "g", 64, COR), ("por", "i", 64)], XE, 600)
    par_em(c, t, C["s14.c"] + 0.5, "3", "2", XE + 690, 600, 64)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=780, cy=820, r=80)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    t0 = C["s16"] - 3
    plano_q(c, t, t0)
    reta_m(c, t, t0, PQ, -3, 5)
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, "r", *PQ(2.8, -1.3), 40, "g", fundo=COR, a=a))
    nome(c, t, t0, PQ, 1, 4, None)
    nome(c, t, t0, PQ, 3, 2, None)
    reta_m(c, t, C["s16.c"], PQ, -3, 7, TINTA)
    reta_m(c, t, C["s17.d"], PQ, 1 / 3, 1, TINTA)
    if t >= C["s17.e"]:
        reto(c, t, C["s17.e"], PQ, (1.2, 1.4), (2.2, 1.4 + 1 / 3), (0.7, 2.9), CERTO)

    def s16():
        E.frase(c, t, C["s16"], [("paralela", "g", 72)], XE, 230)
        eqn(c, t, C["s16.a"], [("m = −3", COR)], XE, 370, 76)
        E.frase(c, t, C["s16.a"] + 0.6, ps("o mesmo de r", "i", 52, TINTA2), XE + 330, 365)
        eqn(c, t, C["s16.b"], [("4", SAI), (" = −3 + n", TINTA)], XE, 520, 76)
        seq(c, t, [("n = 7", TINTA, C["s16.b"] + 1.8)], XE + 500, 520, 76)
        eqn(c, t, C["s16.c"], [("y = ", TINTA), ("−3", COR), ("x + 7", TINTA)], XE, 700, 96, caixa=C["s16.c"] + 0.5)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("perpendicular", "g", 72)], XE, 230)
    eqn(c, t, C["s17.a"], [("−3", TINTA), ("  →  ", TINTA2), ("f{1}{3}", COR)], XE, 370, 80)
    eqn(c, t, C["s17.b"], [("2", SAI), (" = ", TINTA), ("f{1}{3}", COR), (" · ", TINTA), ("3", ENT), (" + n", TINTA)], XE, 520, 76)
    eqn(c, t, C["s17.c"], [("2 = 1 + n", TINTA)], XE, 650, 76)
    seq(c, t, [("n = 1", TINTA, C["s17.c"] + 1.4)], XE + 450, 650, 76)
    eqn(c, t, C["s17.d"], [("y = ", TINTA), ("f{1}{3}", COR), ("x + 1", TINTA)], XE, 810, 90, caixa=C["s17.d"] + 0.5)
    eqn(c, t, C["s17.e"], [("−3 · f{1}{3} = −1", CERTO)], XE, 970, 66)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s18.a", [("paralelas:", "g", 72, COR), ("o", "i", 72), ("mesmo", "i", 72), ("m", "g", 72)]),
                 ("s18.b", [("perpendiculares:", "g", 72, COR), ("m₁ · m₂ = −1", "g", 72)]),
                 ("s18.c", [("inverta", "g", 72), ("e", "i", 72), ("troque", "g", 72), ("o", "i", 72), ("sinal", "i", 72)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s19.a"], [("Onde", "g", 130, COR), ("duas", "g", 130, COR)], XE, 450)
    E.frase(c, t, C["s19.a"] + 0.5, [("retas", "g", 130, COR), ("se", "i", 120), ("cruzam", "g", 130, COR)], XE, 600)
    E.frase(c, t, C["s19.b"], ps("com um sistema de equações", "i", 60, TINTA2), XE, 710, passo=0.12)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, paralelas=b_paralelas, perpendiculares=b_perpendiculares, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
