"""Visual — Estudativo · MAT-POL-011: reflexão, rotação e translação na malha ((2, 3) refletido no eixo y vai para (−2, 3)).
Linguagem do plano (MAT-FUN-001): eixo x em índigo (corredor), eixo y em tinta preta (elevador); par ordenado com o x em índigo e o
y em preto (par()); andar no plano com setas (anda(): índigo no corredor, preta no elevador); no erro, o par inteiro em vermelho.
Linguagem da geometria plana (MAT-POL-010): o eixo que serve de espelho brilha como um espelho (espelho()); caminho do ponto ao
par cruzando o eixo em ângulo reto, com os tracinhos de distâncias iguais.
A bandeirinha: mastro em pé de (2, 1) a (2, 3) e pano índigo apontando para a direita. Cada movimento é animado de verdade:
translação desliza; reflexão vira a bandeira do avesso sobre o eixo (a largura vai a cos θ e o pano mostra o verso, mais claro);
rotação gira em volta da origem. A posição antiga fica tracejada (fantasma).
Peças locais: eixos() e par()/anda() (da MAT-FUN-001), bandeira(), espelho(), ps(), fcen(), bola_txt().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polígonos e Círculo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / corredor · y / elevador
ARQUIVO_FINAL = "estudativo_MAT-POL-011_reflexao_rotacao_translacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("movimentos", "reflexao", "rotacao", "atalho", "questao", "fim"))
BR = "#FFFFFF"
VERSO = E.mix(E.COR, "#FFFFFF", 0.55)
P = E.Plano(800, 170, 975, 675, -5, 8, -4, 5)
PQ = E.Plano(170, 200, 640, 640, -5, 5, -5, 5)          # o plano da questão, à esquerda
BAND = [(2, 1), (2, 3), (3.5, 2.5), (2, 2)]             # pé do mastro, alto do mastro, ponta do pano, pé do pano
assert (2 + 4, 3 - 2) == (6, 1) and (-2, 3) == (-2, 3) and (2, -3) == (2, -3)
assert (-3, 2) == (-3, 2) and (4, -1) == (4, -1) and (-1, 4) == (-1, 4)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     centro(c, s, cx, cy + size * 0.36, size, "g", BR, a)))


def eixos(c, t, P, t0, size=34, escuro=False):
    """plano da MAT-FUN-001: grade, eixo x índigo e eixo y preto, com os números"""
    if t < t0:
        return
    x, y, w, h = P.caixa
    q = ep(t, t0, 0.8)
    for v in range(int(P.xmin), int(P.xmax) + 1):
        M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
    for v in range(int(P.ymin), int(P.ymax) + 1):
        M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    M.arrow(c, x - 10, P.oy, x + w + 40, P.oy, ENT, 1.0, 6, 24, ep(t, t0, 0.7))
    M.arrow(c, P.ox, y + h + 10, P.ox, y - 40, SAI, 1.0, 6, 24, ep(t, t0, 0.7))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: (E.escreve(c, "x", x + w + 16, P.oy + 60, 58, "i", ENT, a),
                                           E.escreve(c, "y", P.ox + 20, y - 14, 58, "i", SAI, a)))
    for v in range(int(P.xmin), int(P.xmax) + 1):
        if v != 0:
            E.foco(c, t, t0 + 0.3, 0.4, lambda a, v=v: (M.line(c, P.x(v), P.oy - 9, P.x(v), P.oy + 9, ENT, a, 4),
                                                       centro(c, E._num(v), P.x(v), P.oy + 12 + size, size, "b", TINTA2, a)), sobe=6)
    for v in range(int(P.ymin), int(P.ymax) + 1):
        if v != 0:
            E.foco(c, t, t0 + 0.3, 0.4, lambda a, v=v: (M.line(c, P.ox - 9, P.y(v), P.ox + 9, P.y(v), SAI, a, 4),
                                                       E.escreve(c, E._num(v), P.ox - 16 - E.larg(E._num(v), "b", size), P.y(v) + size * 0.36,
                                                                 size, "b", TINTA2, a)), sobe=6)


def par(c, xv, yv, x, y, size, a=1.0, align="left", cores=None, est="g"):
    """par ordenado (x, y): x em índigo, y em preto; cores=(cx, cy) troca as duas (ERRADO no erro)"""
    cx_, cy_ = cores or (ENT, SAI)
    partes = (("(", TINTA if not cores else cx_), (xv, cx_), (", ", TINTA if not cores else cx_), (yv, cy_), (")", TINTA if not cores else cy_))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def par_em(c, t, t0, xv, yv, x, y, size, align="left", cores=None):
    E.foco(c, t, t0, 0.5, lambda a: par(c, xv, yv, x, y, size, a, align, cores))


def anda(c, t, t0, P, A, B, cor, d=0.7, largura=9, a=1.0):
    """seta que anda no plano de A até B (em valores)"""
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        (x0, y0), (x1, y1) = P(*A), P(*B)
        M.line(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), cor, 0.22 * a, largura * 3.2)
        M.arrow(c, x0, y0, x1, y1, cor, a, largura, 28, p)


def bandeira(c, P, f=lambda x, y: (x, y), a=1.0, verso=False, fantasma=False, topo=True):
    """a bandeirinha transformada por f (valores → valores)"""
    if a <= 0:
        return
    pts = [P(*f(*q)) for q in BAND]
    pano = [pts[1], pts[2], pts[3]]
    path = skia.Path(); path.addPoly(pano, True)
    if fantasma:
        pd = M.paint(TINTA2, 0.6 * a, stroke=4); pd.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
        c.drawPath(path, pd)
        M.line(c, *pts[0], *pts[1], TINTA2, 0.6 * a, 5, dash=[12, 9])
        return
    c.drawPath(path, M.paint(VERSO if verso else E.COR, a))
    pa = M.paint(E.mix(E.COR, "#000000", 0.25), a, stroke=3); pa.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pa)
    M.line(c, *pts[0], *pts[1], TINTA, a, 9)
    if topo:
        c.drawCircle(*pts[1], 11, M.paint(TINTA, a))


def espelho(c, t, t0, P, qual, t1=None, cor="#7CC4F5"):
    """o eixo vira espelho: uma faixa clara e brilhante sobre o eixo x ou y"""
    q = ep(t, t0, 0.5) * (1 - (ep(t, t1, 0.4) if t1 is not None else 0))
    if q <= 0:
        return
    x, y, w, h = P.caixa
    if qual == "y":
        ret = skia.Rect.MakeXYWH(P.ox - 10, y - 20, 20, h + 40)
        a0, a1 = skia.Point(P.ox - 10, 0), skia.Point(P.ox + 10, 0)
    else:
        ret = skia.Rect.MakeXYWH(x - 20, P.oy - 10, w + 40, 20)
        a0, a1 = skia.Point(0, P.oy - 10), skia.Point(0, P.oy + 10)
    g = skia.Paint(AntiAlias=True)
    g.setShader(skia.GradientShader.MakeLinear([a0, a1], [M.hexc(cor, 0.85 * q), M.hexc("#E8F6FF", 0.95 * q), M.hexc(cor, 0.85 * q)]))
    c.drawRect(ret, g)


def T_trans(q):
    return lambda x, y: (x + 4 * q, y - 2 * q)


def T_refl_y(q):
    k = math.cos(math.pi * q)
    return lambda x, y: (x * k, y)


def T_refl_x(q):
    k = math.cos(math.pi * q)
    return lambda x, y: (x, y * k)


def T_rot(q):
    g = math.radians(90 * q)
    cs, sn = math.cos(g), math.sin(g)
    return lambda x, y: (x * cs - y * sn, x * sn + y * cs)


def ponto(c, t, t0, P, x, y, cor=None, rotulo=None, lado=(1, -1), r=13):
    return E.ponto(c, t, t0, P, x, y, rotulo, cor=cor, lado=lado, r=r, size=44)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        eixos(c, t, P, C["s01"])
        espelho(c, t, ka + 1.0, P, "y")
        ponto(c, t, ka, P, 2, 3, E.COR)
        if t >= kb:
            ponto(c, t, kb, P, 2, -3, ERRADO)
            M.line(c, *P(2, 3), *P(2, -3), ERRADO, ep(t, kb, 0.4) * 0.7, 4, dash=[12, 9])
            if t >= kc:
                X, Y = P(2, -3)
                E.risco(c, X - 30, Y + 30, X + 30, Y - 30, t, kc - 0.4, largura=10)
        if t >= kc:
            ponto(c, t, kc, P, -2, 3, CERTO)
            M.line(c, *P(2, 3), *P(-2, 3), CERTO, ep(t, kc, 0.4), 5, dash=[12, 9])
        par_em(c, t, ka, "2", "3", XE, 300, 110)
        E.frase(c, t, ka + 0.8, ps("refletido no", "i", 62) + [("eixo y", "g", 66)], XE, 410, passo=0.12)
        E.frase(c, t, kb - 0.3, ps("muita gente:", "i", 60, TINTA2), XE, 560, passo=0.12)
        par_em(c, t, kb, "2", "−3", XE, 670, 96, cores=(ERRADO, ERRADO))
        if t >= kc - 0.4:
            E.risco(c, XE - 10, 680, XE + 300, 600, t, kc - 0.4, largura=12)
        E.frase(c, t, kc - 0.2, ps("vai para", "i", 62, CERTO), XE, 820, passo=0.12)
        E.foco(c, t, kc, 0.5, lambda a: par(c, "−2", "3", XE, 940, 110, a, cores=(CERTO, CERTO)))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc, td, te = (C["s02." + k] for k in "abcde")
        E.foco(c, t, te - 0.2, 0.7, lambda a: E.bola(c, 1530, 560, 240 * ease_back(prog(t, te - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula,", "i", 80), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.0, ps("onde a figura vai parar:", "i", 70, TINTA2), XE, 380, passo=0.12)
        for k, (ti, s) in enumerate(((tb, "espelhar"), (tc, "girar"), (td, "deslizar"))):
            E.frase(c, t, ti, [(s, "g", 100, COR)], XE, 540 + k * 140)
        E.foco(c, t, te + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1530, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1530, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "o plano cartesiano:", 150), ("s03.c", "eixo de simetria:", 500))
    for k, l1, y in itens:
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 300, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 80)
    E.frase(c, t, C["s03.b"] + 0.7, [("1º o corredor:", "i", 56), ("x", "g", 66, ENT)], x + 44, 150 + 175)
    E.frase(c, t, C["s03.b"] + 1.4, [("2º o elevador:", "i", 56), ("y", "g", 66, SAI)], x + 44, 150 + 260)
    E.frase(c, t, C["s03.c"] + 0.6, [("um espelho", "g", 66, COR)], x + 44, 500 + 200)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(150 + 270, 500 + 270, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 930, "left", 0.12)


# ---------------- os três movimentos ----------------
def b_movimentos(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    E.frase(c, t, a4, [("3", "g", 130, COR)] + ps("movimentos", "i", 84), XE, 300, passo=0.14)
    for k, s in enumerate(("translação", "reflexão", "rotação")):
        E.frase(c, t, a4 + 0.6 + 0.3 * k, [(s, "g", 62)], XE + 20, 420 + k * 80)
    E.frase(c, t, b4, ps("mesma", "i", 58) + [("forma", "g", 62, COR)] + ps("e mesmo", "i", 58) + [("tamanho", "g", 62, COR)], XE, 760, passo=0.12)
    eixos(c, t, P, c4 - 0.6)
    E.foco(c, t, c4, 0.6, lambda a: bandeira(c, P, a=a))
    ponto(c, t, d4, P, 2, 3, E.COR)
    E.foco(c, t, d4 + 0.3, 0.4, lambda a: par(c, "2", "3", P.x(2) + 30, P.y(3) - 30, 52, a))
    E.frase(c, t, d4, ps("o alto do mastro:", "i", 56, TINTA2), XE, 900, passo=0.1)


# ---------------- translação ----------------
def b_translacao(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    eixos(c, t, P, C["s05"] - 2)
    q = ease_io(prog(t, c5 + 0.2, 1.6))
    if t >= b5:
        bandeira(c, P, fantasma=True, a=ep(t, b5, 0.4))
    bandeira(c, P, T_trans(q))
    # todos os pontos andam o mesmo tanto
    if b5 <= t:
        for (x, y) in BAND[1:3]:
            anda(c, t, c5 + 0.2, P, (x, y), (x + 4, y), ENT, 1.0, 6, a=0.8)
            anda(c, t, c5 + 1.0, P, (x + 4, y), (x + 4, y - 2), SAI, 0.8, 6, a=0.8)
    ponto(c, t, c6, P, 6, 1, CERTO)
    E.foco(c, t, c6 + 0.3, 0.4, lambda a: par(c, "6", "1", P.x(6) - 200, P.y(1) - 22, 50, a))

    def txt5():
        E.frase(c, t, a5, [("translação", "g", 90, COR)], XE, 260)
        E.frase(c, t, a5 + 0.7, ps("deslizar, sem girar", "i", 62), XE, 360, passo=0.12)
        E.frase(c, t, b5, ps("todos andam", "i", 60) + [("o mesmo", "g", 64, COR)], XE, 520, passo=0.12)
        E.frase(c, t, c5, [("4", "g", 76, ENT)] + ps("para a direita", "i", 58), XE, 690, passo=0.12)
        E.frase(c, t, c5 + 0.6, [("2", "g", 76, SAI)] + ps("para baixo", "i", 58), XE, 790, passo=0.12)
    E.saida(c, t, C["s06"] - 0.1, txt5)
    if t >= C["s06"]:
        E.frase(c, t, C["s06"], ps("o alto do mastro", "i", 62), XE, 240, passo=0.12)
        fcen(c, t, a6, "2 + 4 = 6", XE + 230, 380, 84, ENT)
        fcen(c, t, b6, "3 − 2 = 1", XE + 230, 510, 84, SAI)
        E.foco(c, t, c6, 0.5, lambda a: par(c, "6", "1", XE, 680, 120, a))
        E.frase(c, t, d6, ps("mesma bandeira,", "i", 58), XE, 830, passo=0.12)
        E.frase(c, t, d6 + 0.8, ps("só mudou de", "i", 58) + [("lugar", "g", 64, COR)], XE, 920, passo=0.12)


# ---------------- reflexão ----------------
def b_reflexao(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8, e8 = (C["s08." + k] for k in "abcde")
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    eixos(c, t, P, C["s07"] - 2)
    espelho(c, t, a7, P, "y", a9)
    espelho(c, t, a9, P, "x")
    # s07: a ponta do pano e o seu par, na mesma distância
    if b7 <= t < C["s08"] + 0.4:
        k = ep(t, b7, 0.4) * (1 - ep(t, C["s08"], 0.4))
        A, B = P(3.5, 2.5), P(-3.5, 2.5)
        M.line(c, *A, *B, E.COR, k, 5, dash=[12, 9], progress=ease_io(prog(t, b7, 0.7)))
        c.drawCircle(*A, 13, M.paint(E.COR, k)); c.drawCircle(*B, 13 * ep(t, b7 + 0.6, 0.3), M.paint(E.COR, k))
        O = P(0, 2.5)
        E.marcas_iguais(c, A, O, 1, TINTA, k * ep(t, b7 + 0.7, 0.3)); E.marcas_iguais(c, O, B, 1, TINTA, k * ep(t, b7 + 0.7, 0.3))
        if t >= c7:
            E.angulo(c, t, c7, O, P(0, 3.5), A, r=34, reto=True)
    # s08: a bandeira vira sobre o eixo y; s09: sobre o eixo x
    qy = ease_io(prog(t, e8, 1.2))
    qx = ease_io(prog(t, b9, 1.2))
    bandeira(c, P, a=1.0 if t < a9 else 0.35, fantasma=t >= e8 + 1.2)
    if t >= e8:
        f = T_refl_y(qy)
        bandeira(c, P, f, verso=qy > 0.5, a=1 - ep(t, a9, 0.4) * 0.65)
    if t >= b9:
        bandeira(c, P, T_refl_x(qx), verso=qx > 0.5)
    anda(c, t, b8, P, (0, 3), (2, 3), ENT, 0.6)
    anda(c, t, c8, P, (0, 3), (-2, 3), ENT, 0.6)
    ponto(c, t, d8, P, -2, 3, CERTO)
    ponto(c, t, c9, P, 2, -3, CERTO)
    E.foco(c, t, c9 + 0.3, 0.4, lambda a: par(c, "2", "−3", P.x(2) + 30, P.y(-3) + 60, 50, a))

    def txt7():
        E.frase(c, t, a7, [("reflexão", "g", 90, COR)] + ps("= espelho", "i", 64), XE, 260, passo=0.12)
        E.frase(c, t, b7, ps("vai para o", "i", 58) + [("outro lado", "g", 62, COR)], XE, 420, passo=0.12)
        E.frase(c, t, b7 + 0.8, ps("na mesma distância", "i", 58), XE, 510, passo=0.12)
        E.frase(c, t, c7, ps("cruza o eixo em", "i", 58) + [("90°", "g", 66)], XE, 670, passo=0.12)
    E.saida(c, t, C["s08"] - 0.1, txt7)

    def txt8():
        E.frase(c, t, a8, [("eixo y:", "g", 74, SAI)] + ps("em pé", "i", 64), XE, 250, passo=0.12)
        E.frase(c, t, b8, [("2", "g", 76, ENT)] + ps("à direita", "i", 60), XE, 390, passo=0.12)
        E.frase(c, t, c8, [("2", "g", 76, ENT)] + ps("à esquerda", "i", 60), XE, 500, passo=0.12)
        E.foco(c, t, d8, 0.5, lambda a: par(c, "−2", "3", XE, 660, 110, a))
        E.frase(c, t, e8, ps("o pano vira:", "i", 58) + [("espelhado", "g", 62, COR)], XE, 820, passo=0.12)
    if C["s08"] - 0.1 <= t:
        E.saida(c, t, C["s09"] - 0.1, txt8)
    if t >= C["s09"]:
        E.frase(c, t, a9, [("eixo x:", "g", 74, ENT)] + ps("deitado", "i", 64), XE, 250, passo=0.12)
        E.frase(c, t, b9, ps("troca", "i", 60) + [("cima", "g", 64)] + ps("e", "i", 60) + [("baixo", "g", 64)], XE, 400, passo=0.12)
        E.foco(c, t, c9, 0.5, lambda a: par(c, "2", "−3", XE, 580, 110, a))


# ---------------- rotação ----------------
def b_rotacao(c, t, C, b):
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    eixos(c, t, P, C["s10"] - 2)
    O = P(0, 0)
    # o centro e o sentido do giro
    if t >= a10:
        k = ease_back(prog(t, a10, 0.4))
        c.drawCircle(*O, 16 * k, M.paint(E.COR))
        E.foco(c, t, a10 + 0.3, 0.4, lambda a: E.escreve(c, "centro", O[0] - 175, O[1] - 18, 46, "b", COR, a))
    if t >= c10:  # seta curva ao contrário do relógio
        r = 150
        ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
        p = ease_io(prog(t, c10, 0.8))
        c.drawArc(ret, -10, -80 * p, False, M.paint(TINTA2, 1, stroke=6, cap_round=True))
        if p > 0.9:
            g = math.radians(-90)
            tip = (O[0] + r * math.cos(g), O[1] + r * math.sin(g))
            M.line(c, *tip, tip[0] + 22, tip[1] - 16, TINTA2, 1, 6); M.line(c, *tip, tip[0] + 22, tip[1] + 16, TINTA2, 1, 6)
    # a bandeira e o caminho giram juntos
    q = ease_io(prog(t, c11, 1.6))
    if t >= c11:
        bandeira(c, P, fantasma=True)
    bandeira(c, P, T_rot(q))
    a_cam = 1 - ep(t, c11, 0.3)
    anda(c, t, b11, P, (0, 0), (2, 0), ENT, 0.6, a=a_cam)
    anda(c, t, b11 + 0.7, P, (2, 0), (2, 3), SAI, 0.6, a=a_cam)
    if t >= c11:
        anda(c, t, c11 + 0.4, P, (0, 0), (0, 2), ENT, 0.8)
        anda(c, t, d11, P, (0, 2), (-3, 2), SAI, 0.8)
    ponto(c, t, b12, P, -3, 2, CERTO, lado=(-1, -1))
    E.foco(c, t, b12 + 0.3, 0.4, lambda a: par(c, "−3", "2", P.x(-3) - 230, P.y(2) - 30, 50, a))

    def txt10():
        E.frase(c, t, a10, [("rotação", "g", 90, COR)], XE, 260)
        E.frase(c, t, a10 + 0.7, ps("girar em volta", "i", 60), XE, 360, passo=0.12)
        E.frase(c, t, a10 + 1.3, ps("de um", "i", 60) + [("centro", "g", 66, COR)], XE, 450, passo=0.12)
        E.frase(c, t, b10, [("90°", "g", 84)] + ps("= 1/4 de volta", "i", 60), XE, 620, passo=0.12)
        E.frase(c, t, c10, ps("ao contrário", "i", 60) + [("do relógio", "g", 64)], XE, 760, passo=0.12)
    E.saida(c, t, C["s11"] - 0.1, txt10)

    def txt11():
        E.frase(c, t, a11, ps("o caminho até o mastro:", "i", 56), XE, 250, passo=0.1)
        E.frase(c, t, b11, [("2 →", "g", 76, ENT), ("3 ↑", "g", 76, SAI)], XE, 370, passo=0.5)
        E.frase(c, t, c11, ps("gira junto:", "i", 58, TINTA2), XE, 520, passo=0.12)
        E.frase(c, t, c11 + 0.6, [("→", "g", 76, ENT)] + ps("vira", "i", 60) + [("↑", "g", 76, ENT)], XE, 630, passo=0.12)
        E.frase(c, t, d11, [("↑", "g", 76, SAI)] + ps("vira", "i", 60) + [("←", "g", 76, SAI)], XE, 750, passo=0.12)
    if t >= C["s11"] - 0.1:
        E.saida(c, t, C["s12"] - 0.1, txt11)
    if t >= C["s12"]:
        E.frase(c, t, a12, [("2 ↑", "g", 76, ENT), ("3 ←", "g", 76, SAI)], XE, 280, passo=0.5)
        E.foco(c, t, b12, 0.5, lambda a: par(c, "−3", "2", XE, 460, 110, a))
        E.frase(c, t, c12, ps("deitada, mas", "i", 58), XE, 640, passo=0.12)
        E.frase(c, t, c12 + 0.6, [("não espelhada", "g", 70, COR)], XE, 740)


# ---------------- reconhecer: girar ou virar do avesso ----------------
def cartao(c, cx, cy, w, h, sx=1.0, giro=0.0, verso=False, a=1.0, letra_cor=None):
    """um cartão com a letra F: sx = largura (cos θ), giro em graus"""
    if a <= 0:
        return
    c.save()
    c.translate(cx, cy); c.rotate(-giro); c.scale(sx if abs(sx) > 1e-3 else 1e-3, 1)
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
    ret = skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h)
    c.drawRect(ret.makeOffset(5, 9), s)
    c.drawRect(ret, M.paint(VERSO if (sx < 0) != verso else "#FFFFFF", a))
    c.drawRect(ret, M.paint(TINTA2, a, stroke=4))
    lw = E.larg("F", "g", h * 0.7)
    E.escreve(c, "F", -lw / 2, h * 0.25, h * 0.7, "g", letra_cor or E.COR, a)
    c.restore()


def b_reconhecer(c, t, C, b):
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, C["s13"], ps("reflexão ou rotação?", "i", 76), W / 2, 170, "center", 0.12)
    # girar sobre a mesa
    g = 90 * ease_io(prog(t, a13 + 0.4, 1.2))
    if t >= a13:
        cartao(c, 520, 520, 260, 320, a=0.35)
        cartao(c, 520, 520, 260, 320, giro=g, a=ep(t, a13, 0.4))
    E.frase(c, t, a13, [("rotação:", "g", 70, COR)], 520, 820, "center")
    E.frase(c, t, a13 + 0.6, ps("girar sobre a mesa", "i", 58), 520, 910, "center", 0.12)
    # virar do avesso
    k = math.cos(math.pi * ease_io(prog(t, b13 + 0.4, 1.2)))
    if t >= b13:
        cartao(c, 1400, 520, 260, 320, a=0.35)
        cartao(c, 1400, 520, 260, 320, sx=k, a=ep(t, b13, 0.4))
    E.frase(c, t, b13, [("reflexão:", "g", 70, COR)], 1400, 820, "center")
    E.frase(c, t, b13 + 0.6, ps("virar do avesso", "i", 58), 1400, 910, "center", 0.12)
    E.foco(c, t, c13, 0.5, lambda a: E.pilula(c, "só encaixa virando do avesso: reflexão", W / 2, 1010, 50, "g", a=a, cor=E.SOBRE))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a14, b14, c14, d14, e14 = (C["s14." + k] for k in "abcde")
    eixos(c, t, P, C["s14"] - 2)
    espelho(c, t, b14, P, "y")
    ponto(c, t, C["s14"], P, 2, 3, E.COR)
    if t >= a14:
        ponto(c, t, a14, P, 2, -3, ERRADO)
        M.line(c, *P(2, 3), *P(2, -3), ERRADO, ep(t, a14, 0.4) * 0.7, 4, dash=[12, 9])
        if t >= b14:
            X, Y = P(2, -3)
            E.risco(c, X - 30, Y + 30, X + 30, Y - 30, t, b14, largura=10)
    if t >= c14:  # direita e esquerda trocam
        Y = P.y(4.2)
        M.arrow(c, P.ox + 20, Y, P.x(3), Y, ENT, ep(t, c14, 0.3), 8, 26, ease_io(prog(t, c14, 0.6)))
        M.arrow(c, P.ox - 20, Y, P.x(-3), Y, ENT, ep(t, c14, 0.3), 8, 26, ease_io(prog(t, c14, 0.6)))
    if t >= e14:
        ponto(c, t, e14 + 0.3, P, -2, 3, CERTO)
        M.line(c, *P(2, 3), *P(-2, 3), CERTO, ep(t, e14 + 0.3, 0.4), 5, dash=[12, 9])
    E.frase(c, t, a14, ps("o erro:", "i", 62, ERRADO), XE, 240, passo=0.12)
    par_em(c, t, a14 + 0.4, "2", "−3", XE, 350, 96, cores=(ERRADO, ERRADO))
    E.frase(c, t, b14, [("eixo y", "g", 70, SAI)] + ps("fica em pé", "i", 60), XE, 500, passo=0.12)
    E.frase(c, t, c14, ps("troca", "i", 54) + [("direita", "g", 56)] + ps("e", "i", 54) + [("esquerda", "g", 56)], XE, 620, passo=0.12)
    E.frase(c, t, d14, ps("quem diz isso:", "i", 58) + [("o x", "g", 70, ENT)], XE, 740, passo=0.12)
    E.foco(c, t, e14, 0.5, lambda a: E.pilula(c, "eixo y: muda o sinal do x", XE + 270, 880, 50, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, e14 + 0.6, 0.5, lambda a: par(c, "−2", "3", XE + 140, 1010, 84, a, cores=(CERTO, CERTO)))


# ---------------- atalho (palco escuro) ----------------
def par_escuro(c, xv, yv, x, y, size, a=1.0, cx_=None, cy_=None, align="left"):
    return par(c, xv, yv, x, y, size, a, align, cores=(cx_ or CLARO, cy_ or BR))


def b_atalho(c, t, C, b):
    palco(c, t)
    a15, b15, c15, d15, e15, f15 = (C["s15." + k] for k in "abcdef")
    a16, b16, c16, d16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    X = W / 2

    def um():
        E.frase(c, t, a15, [("90°", "g", 80, CLARO)] + ps("ao contrário do relógio,", "i", 62, BR), X, 180, "center", 0.12)
        E.frase(c, t, a15 + 1.0, ps("centro na origem", "i", 56, CLARO), X, 260, "center", 0.12)
        E.foco(c, t, b15, 0.5, lambda a: (num_bola(c, "1", 520, 380, 40, 48, a), E.escreve(c, "troque os números de lugar", 590, 400, 60, "g", BR, a)))
        E.foco(c, t, c15, 0.5, lambda a: (num_bola(c, "2", 520, 490, 40, 48, a), E.escreve(c, "mude o sinal do da frente", 590, 510, 60, "g", BR, a)))
        E.foco(c, t, d15, 0.5, lambda a: par_escuro(c, "2", "3", 280, 760, 110, a))
        if t >= e15:
            M.arrow(c, 630, 730, 770, 730, CLARO, ep(t, e15, 0.3), 8, 26, ease_io(prog(t, e15, 0.5)))
        E.foco(c, t, e15 + 0.2, 0.5, lambda a: par_escuro(c, "3", "2", 800, 760, 110, a))
        if t >= f15:
            M.arrow(c, 1140, 730, 1260, 730, CLARO, ep(t, f15, 0.3), 8, 26, ease_io(prog(t, f15, 0.5)))
        E.foco(c, t, f15 + 0.2, 0.5, lambda a: par_escuro(c, "−3", "2", 1290, 760, 110, a, cx_="#FFD500"))
    E.saida(c, t, C["s16"] - 0.1, um)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], ps("por que funciona?", "i", 66, CLARO), X, 170, "center", 0.12)
    E.frase(c, t, a16, [("→", "g", 90, CLARO)] + ps("vira", "i", 64, BR) + [("↑", "g", 90, CLARO)], 640, 330, "center", 0.12)
    E.frase(c, t, b16, [("↑", "g", 90, BR)] + ps("vira", "i", 64, BR) + [("←", "g", 90, BR)] + ps("(negativo)", "i", 54, CLARO), 1280, 330, "center", 0.12)
    E.frase(c, t, c16, ps("no sentido do relógio:", "i", 58, CLARO), X, 520, "center", 0.12)
    E.frase(c, t, c16 + 0.8, ps("troque e mude o sinal do", "i", 58, BR) + [("de trás", "g", 62, BR)], X, 610, "center", 0.12)
    E.foco(c, t, c16 + 1.6, 0.5, lambda a: (par_escuro(c, "2", "3", 560, 740, 90, a), E.escreve(c, "→", 870, 740, 90, "g", CLARO, a),
                                            par_escuro(c, "3", "−2", 980, 740, 90, a, cy_="#FFD500")))
    E.foco(c, t, d16 - 0.8, 0.5, lambda a: E.pilula(c, "centro fora da origem: gire o caminho na malha", X, 920, 50, "g", fundo=ERRADO, a=a))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)


# ---------------- questão ----------------
def eixos_q(c, t, t0):
    eixos(c, t, PQ, t0, size=32)


def b_questao(c, t, C, b):
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 130, passo=0.12)
    eixos_q(c, t, C["s17"] + 0.2)
    ponto(c, t, a17, PQ, 4, 1, E.COR)
    E.foco(c, t, a17 + 0.3, 0.4, lambda a: par(c, "4", "1", PQ.x(4) - 70, PQ.y(1) - 34, 44, a))
    espelho(c, t, b17, PQ, "x")
    E.frase(c, t, b17, ps("refletido no", "i", 60) + [("eixo x?", "g", 64, ENT)], 1450, 900, "center", 0.12)
    E.frase(c, t, c17, ps("girado", "i", 60) + [("90°", "g", 64, COR)] + ps("ao contrário do relógio?", "i", 60), 1350, 1000, "center", 0.12)
    E.relogio(c, t, C["s18.a"], 1450, 420, 180)


def b_resposta(c, t, C, b):
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    a20, b20, c20, d20, e20 = (C["s20." + k] for k in "abcde")
    X = 1350
    t0 = C["s19"] - 1.5
    eixos_q(c, t, t0)
    ponto(c, t, t0, PQ, 4, 1, E.COR)
    espelho(c, t, t0, PQ, "x", C["s20"])
    if t >= a19:
        M.line(c, *PQ(4, 1), *PQ(4, -1), TINTA2, ep(t, a19, 0.4), 4, dash=[12, 9])
    ponto(c, t, c19, PQ, 4, -1, CERTO)
    E.foco(c, t, c19 + 0.3, 0.4, lambda a: par(c, "4", "−1", PQ.x(4) - 90, PQ.y(-1) + 66, 44, a))
    anda(c, t, d20, PQ, (0, 0), (4, 0), ENT, 0.5, 7, a=1 - ep(t, d20 + 0.8, 0.3))
    anda(c, t, d20 + 0.5, PQ, (0, 0), (0, 4), ENT, 0.6, 7)
    anda(c, t, e20, PQ, (0, 4), (-1, 4), SAI, 0.5, 7)
    ponto(c, t, c20, PQ, -1, 4, CERTO, lado=(-1, -1))
    E.foco(c, t, c20 + 0.3, 0.4, lambda a: par(c, "−1", "4", PQ.x(-1) - 230, PQ.y(4) - 30, 44, a))

    def um():
        E.frase(c, t, a19, [("eixo x", "g", 66, ENT)] + ps("deitado:", "i", 60), X, 260, "center", 0.12)
        E.frase(c, t, a19 + 0.8, ps("troca cima e baixo", "i", 58), X, 350, "center", 0.12)
        E.frase(c, t, b19, ps("muda o sinal do", "i", 60) + [("y", "g", 70, SAI)], X, 500, "center", 0.12)
        E.foco(c, t, c19, 0.5, lambda a: par(c, "4", "−1", X, 690, 120, a, "center", cores=(CERTO, CERTO)))
    E.saida(c, t, C["s20"] - 0.1, um)
    if t >= C["s20"]:
        E.frase(c, t, C["s20"], ps("no giro, pelo atalho:", "i", 58), X, 220, "center", 0.12)
        E.foco(c, t, a20, 0.5, lambda a: (par(c, "4", "1", X - 330, 360, 84, a), E.escreve(c, "→", X - 60, 360, 84, "g", TINTA2, a),
                                          par(c, "1", "4", X + 50, 360, 84, a)))
        E.frase(c, t, b20, ps("muda o sinal do 1º", "i", 58), X, 480, "center", 0.12)
        E.foco(c, t, c20, 0.5, lambda a: par(c, "−1", "4", X, 620, 110, a, "center", cores=(CERTO, CERTO)))
        E.frase(c, t, d20, [("4 →", "g", 66, ENT)] + ps("vira", "i", 58) + [("4 ↑", "g", 66, ENT)], X, 780, "center", 0.12)
        E.frase(c, t, e20, [("1 ↑", "g", 66, SAI)] + ps("vira", "i", 58) + [("1 ←", "g", 66, SAI)], X, 880, "center", 0.12)
        E.foco(c, t, e20 + 1.0, 0.5, lambda a: E.selo(c, X, 980, 44 * ease_back(prog(t, e20 + 1.0, 0.5)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s21.a", "translação", "desliza"), ("s21.b", "reflexão", "espelha"), ("s21.c", "rotação", "gira em volta de um centro"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 5, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 70, COR), (l2, "i", 72)], 390, y, "left", 0.2)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], ps("próxima aula: prática", "i", 84), XE, 300)
    E.frase(c, t, C["s22.a"], [("Qual foi o", "g", 110, COR)], XE, 440)
    E.frase(c, t, C["s22.a"] + 0.4, [("movimento?", "g", 110, COR)], XE, 560)
    E.frase(c, t, C["s22.b"], ps("malha, espelho e dobradura", "i", 64), XE, 690, passo=0.1)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(720, 425, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, movimentos=b_movimentos, translacao=b_translacao, reflexao=b_reflexao,
              rotacao=b_rotacao, reconhecer=b_reconhecer, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
