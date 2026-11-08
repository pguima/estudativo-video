"""Visual — Estudativo · MAT-ANG-020: pontos notáveis e baricentro (2 para 1).
Linguagem da geometria plana (MAT-ANG-001 a 008): lados em tinta; as três linhas da vez em COR, crescendo uma de cada vértice;
o ponto notável numa bolinha que pulsa, com o nome na grotesca. Círculo inscrito e circunscrito com E.circulo. Na mediana, os
pedaços do baricentro: o do vértice em COR (o dobro), o do lado em TINTA2, com três tracinhos de pedaços iguais. Moedas = E.moeda.
Erro em vermelho; certo em verde; medidas na grotesca; resposta na esfera.
Peças locais (as da MAT-ANG-004/008): tri(), canto(), triang(), rotulo(), meio(), pe(), pe_bis(), linha(), reto(); e ainda
incentro(), circuncentro(), ortocentro(), baric(), notavel() (o ponto que pulsa), lapis(), papelao(), casa(), mediana_2_1()
(a mediana em três pedaços) e gangorra(). Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-020_pontos_notaveis_e_baricentro.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("encontro", "dois_um", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
PAPELAO = "#C9A46C"
PAPEL = "#F4F3EE"  # fundo atrás do nome do ponto, para não brigar com as linhas
assert 9 / 3 == 3 and 2 * 3 == 6 and 6 + 3 == 9 and 12 / 2 == 6 and 12 + 6 == 18
assert 30 / 3 == 10 and 2 * 10 == 20 and 2 * 7 == 14 and 7 + 14 == 21


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


def pt(V, L, g):
    return V[0] + L * math.cos(math.radians(g)), V[1] - L * math.sin(math.radians(g))


def tri(B, BC, gb, gc):
    """triângulo com a base BC deitada: ângulo gb em B e gc em C. Devolve A, B, C"""
    ga = 180 - gb - gc
    AB = BC * math.sin(math.radians(gc)) / math.sin(math.radians(ga))
    return pt(B, AB, gb), B, (B[0] + BC, B[1])


def triang(c, t, t0, A, B, C, nomes="ABC", tinta=TINTA, preenche=0.06, d=0.9, a=1.0, cor_f=None):
    """o contorno que se desenha em volta, com os nomes dos vértices"""
    if t < t0 or a <= 0:
        return
    pts = [A, B, C]
    if preenche:
        path = skia.Path(); path.addPoly(pts, True)
        c.drawPath(path, M.paint(cor_f or E.COR, preenche * ep(t, t0 + d * 0.6, 0.5) * a))
    p = ease_io(prog(t, t0, d))
    for i, (P, Q) in enumerate(((A, B), (B, C), (C, A))):
        f = M.clamp(p * 3 - i)
        if f > 0:
            M.line(c, *P, lerp(P[0], Q[0], f), lerp(P[1], Q[1], f), tinta, a, 6)
    if nomes:
        g = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)
        for i, (V, s) in enumerate(zip(pts, nomes)):
            if not s.strip():
                continue
            ux, uy = V[0] - g[0], V[1] - g[1]
            n = math.hypot(ux, uy)
            E.foco(c, t, t0 + 0.3 + 0.15 * i, 0.4, lambda k, V=V, s=s, ux=ux / n, uy=uy / n: centro(c, s, V[0] + ux * 58, V[1] + uy * 58 + 22, 58, "g", tinta, k * a))


def meio(P, Q):
    return (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2


def pe(P, Q1, Q2):
    """pé da perpendicular de P até a reta Q1Q2"""
    dx, dy = Q2[0] - Q1[0], Q2[1] - Q1[1]
    k = ((P[0] - Q1[0]) * dx + (P[1] - Q1[1]) * dy) / (dx * dx + dy * dy)
    return Q1[0] + k * dx, Q1[1] + k * dy


def pe_bis(A, B, Cc):
    ab, ac = math.dist(A, B), math.dist(A, Cc)
    k = ab / (ab + ac)
    return lerp(B[0], Cc[0], k), lerp(B[1], Cc[1], k)


def baric(A, B, Cc):
    return (A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3


def incentro(A, B, Cc):
    a, b, c_ = math.dist(B, Cc), math.dist(A, Cc), math.dist(A, B)
    s = a + b + c_
    I = ((a * A[0] + b * B[0] + c_ * Cc[0]) / s, (a * A[1] + b * B[1] + c_ * Cc[1]) / s)
    return I, math.dist(I, pe(I, B, Cc))


def circuncentro(A, B, Cc):
    ax, ay = A; bx, by = B; cx, cy = Cc
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    return (ux, uy), math.dist((ux, uy), A)


def ortocentro(A, B, Cc):
    O, _ = circuncentro(A, B, Cc)
    return A[0] + B[0] + Cc[0] - 2 * O[0], A[1] + B[1] + Cc[1] - 2 * O[1]


def linha(c, t, t0, P, Q, cor=None, larg=7, d=0.7, a=1.0, dash=None, ponta=True):
    """a linha da vez, crescendo de P até Q"""
    if t >= t0 and a > 0:
        M.line(c, *P, *Q, cor or E.COR, a, larg, dash=dash, progress=ease_io(prog(t, t0, d)))
        if ponta:
            k = ease_back(prog(t, t0 + d * 0.9, 0.35))
            if k > 0:
                c.drawCircle(*Q, 9 * k, M.paint(cor or E.COR, a))


def reto(c, t, t0, V, P, Q, cor=None, r=50, a=1.0):
    if t >= t0 and a > 0:
        E.angulo(c, t, t0, V, P, Q, None, r=r, cor=cor or E.COR, reto=True, preenche=0.2 * a)


def notavel(c, t, t0, P, nome, cor=None, lado=(1, -1), size=60, a=1.0, pulsa=True):
    """o ponto notável: bolinha que entra com salto e pulsa; o nome ao lado"""
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    k = ease_back(prog(t, t0, 0.4))
    if pulsa:
        f = (t - t0) % 1.4 / 1.4
        if t - t0 < 4.2:
            c.drawCircle(*P, 18 + 40 * f, M.paint(cor, 0.35 * (1 - f) * a))
    c.drawCircle(*P, 18 * k, M.paint(cor, a))
    c.drawCircle(*P, 7 * k, M.paint("#FFFFFF", a))
    if nome:
        n = math.hypot(*lado) or 1
        Lx, Ly = P[0] + lado[0] / n * (size * 0.9 + 14), P[1] + lado[1] / n * (size * 0.9 + 14)

        def rot(q):
            c.drawCircle(Lx, Ly, size * 0.62, M.paint(PAPEL, 0.92 * q * a))
            centro(c, nome, Lx, Ly + size * 0.36, size, "g", COR if cor == E.COR else cor, q * a)
        E.foco(c, t, t0 + 0.2, 0.4, rot)


def grosso(c, P, Q, cor, a, larg=12):
    if a > 0:
        M.line(c, *P, *Q, cor, a, larg)


def txt_seg(c, P, Q, s, lado, size=54, cor=None, a=1.0, gap=22):
    """rótulo ao lado do segmento PQ: lado = 1 ou −1"""
    if a <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    E._cola(c, s, *meio(P, Q), uy * lado, -ux * lado, gap, size, "b", cor or COR, a)


def lapis(c, x, y, a=1.0):
    """lápis em pé com a ponta em (x, y)"""
    if a <= 0:
        return
    path = skia.Path(); path.moveTo(x, y); path.lineTo(x - 22, y + 70); path.lineTo(x + 22, y + 70); path.close()
    c.drawPath(path, M.paint("#E8C9A0", a))
    path = skia.Path(); path.moveTo(x, y); path.lineTo(x - 7, y + 22); path.lineTo(x + 7, y + 22); path.close()
    c.drawPath(path, M.paint(TINTA, a))
    M.rrect(c, x - 22, y + 70, 44, 420, 4, AMBAR, a)
    for dx in (-8, 8):
        M.line(c, x + dx, y + 74, x + dx, y + 490, "#B87400", a, 2)


def papelao(c, pts, a=1.0, alfa=1.0):
    if a <= 0:
        return
    path = skia.Path(); path.addPoly(pts, True)
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.2 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 12))
    c.save(); c.translate(6, 14); c.drawPath(path, s); c.restore()
    c.drawPath(path, M.paint(PAPELAO, a * alfa))
    p = M.paint("#8E6A35", a, stroke=5)
    p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, p)


def gira(pts, O, g):
    r = math.radians(g)
    co, si = math.cos(r), math.sin(r)
    return [(O[0] + (x - O[0]) * co - (y - O[1]) * si, O[1] + (x - O[0]) * si + (y - O[1]) * co) for x, y in pts]


def casa(c, x, y, s=1.0, a=1.0, cor=TINTA2):
    """casinha de bairro com a base em (x, y)"""
    if a <= 0:
        return
    w, h = 70 * s, 54 * s
    M.rrect(c, x - w / 2, y - h, w, h, 4, cor, a)
    path = skia.Path(); path.moveTo(x - w / 2 - 12 * s, y - h); path.lineTo(x, y - h - 44 * s); path.lineTo(x + w / 2 + 12 * s, y - h); path.close()
    c.drawPath(path, M.paint(AMBAR, a))
    M.rrect(c, x - 10 * s, y - 30 * s, 20 * s, 30 * s, 3, "#FFFFFF", a)


def mediana_2_1(c, t, P, Mm, tv, tl, rot_v=None, rot_l=None, lado=1, tq=None, cor_v=None, cor_l=TINTA2, size=58):
    """a mediana de P (vértice) até Mm (lado) em três pedaços: dois com o vértice (cor_v), um com o lado (cor_l).
    tv / tl = instantes em que cada parte ganha cor e rótulo; tq = instante dos três tracinhos"""
    G = (P[0] + 2 / 3 * (Mm[0] - P[0]), P[1] + 2 / 3 * (Mm[1] - P[1]))
    cor_v = cor_v or E.COR
    grosso(c, P, G, cor_v, ep(t, tv, 0.4), 12)
    grosso(c, G, Mm, cor_l, ep(t, tl, 0.4), 12)
    if tq is not None:
        q = ep(t, tq, 0.4)
        for k in range(3):
            A_ = (P[0] + k / 3 * (Mm[0] - P[0]), P[1] + k / 3 * (Mm[1] - P[1]))
            B_ = (P[0] + (k + 1) / 3 * (Mm[0] - P[0]), P[1] + (k + 1) / 3 * (Mm[1] - P[1]))
            E.marcas_iguais(c, A_, B_, 1, TINTA, q)
    if rot_v:
        s = rot_v(t) if callable(rot_v) else rot_v
        E.foco(c, t, tv + 0.2, 0.4, lambda a: txt_seg(c, P, G, s, lado, size, COR if cor_v == E.COR else cor_v, a, gap=34))
    if rot_l:
        s = rot_l(t) if callable(rot_l) else rot_l
        E.foco(c, t, tl + 0.2, 0.4, lambda a: txt_seg(c, G, Mm, s, lado, size, cor_l, a, gap=34))
    return G


# triângulo dos pontos notáveis (acutângulo escaleno)
TA, TB, TC = tri((260, 880), 760, 62, 50)
NOT = (("medianas", "baricentro"), ("bissetrizes", "incentro"), ("mediatrizes", "circuncentro"), ("alturas", "ortocentro"))


def esc(P, k=0.8, O=(640, 640)):
    """o mesmo triângulo, menor (para o círculo de fora caber na tela)"""
    return O[0] + (P[0] - O[0]) * k, O[1] + (P[1] - O[1]) * k


def medianas(c, t, t0, A, B, Cc, passo=0.5, cor=None, a=1.0):
    for i, (V, P, Q) in enumerate(((A, B, Cc), (B, Cc, A), (Cc, A, B))):
        linha(c, t, t0 + passo * i, V, meio(P, Q), cor, a=a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    X = 1500
    T0 = [(640, 330), (300, 690), (1060, 690)]
    G = baric(*T0)

    def um():
        p0 = (G[0] - 150, G[1] + 40)
        # antes do {b}: o lápis fora do ponto e o papelão tomba; no {b}, o lápis vai ao baricentro e ele assenta
        q = ease_io(prog(t, kb, 1.0))
        P = (lerp(p0[0], G[0], q), lerp(p0[1], G[1], q))
        tomba = 16 * ease_io(prog(t, ka + 1.0, 1.2)) * (1 - q)
        balanco = 2.0 * math.sin(2 * math.pi * (t - kb) / 1.2) * math.exp(-max(0.0, t - kb - 1.0)) if t > kb + 1.0 else 0.0
        pts = gira(T0, P, -tomba + balanco)
        lapis(c, P[0], P[1] + 4, ep(t, ka, 0.4))
        papelao(c, pts, ep(t, ka, 0.4))
        if t >= kb + 1.0:
            notavel(c, t, kb + 1.0, gira([G], P, balanco)[0], None)
        E.frase(c, t, ka, ps("papelão na", "i", 70) + [("ponta do lápis", "g", 70)], X, 280, "center", 0.12)
        E.frase(c, t, kb, ps("só num", "i", 70) + [("ponto exato", "g", 76, COR)], X, 440, "center", 0.12)
        E.frase(c, t, kc, ps("achado com uma", "i", 64), X, 620, "center", 0.12)
        E.frase(c, t, kc + 0.6, [("conta de cabeça", "g", 76, COR)], X, 720, "center")
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.25), ps("cada", "i", 84) + [("linha", "g", 96, COR)], XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), ps("no seu", "i", 84) + [("ponto especial", "g", 90)], XE, 600, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 820
    itens = (("s03.b", "altura, mediana,", "bissetriz e mediatriz"), ("s03.c", "proporção e a cruz", "2x = 12 → x = 6"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
    py = lerp(420, 700, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 920, "left", 0.12)


# ---------------- o encontro ----------------
def b_encontro(c, t, C, b):
    A, B, Cc = TA, TB, TC
    G = baric(A, B, Cc)
    X = 1480
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    triang(c, t, C["s04"], A, B, Cc)
    medianas(c, t, a4, A, B, Cc, 0.6)
    notavel(c, t, b4, G, None)
    E.frase(c, t, a4, [("3 medianas", "g", 80, COR)], X, 260, "center")
    E.frase(c, t, a4 + 0.8, ps("uma de cada vértice", "i", 58), X, 350, "center", 0.12)
    E.frase(c, t, b4, ps("se cruzam", "i", 64) + [("num ponto só", "g", 68)], X, 490, "center", 0.12)
    for i, s in enumerate(("alturas", "bissetrizes", "mediatrizes")):
        E.frase(c, t, lerp(b4, c4, 0.35 + 0.17 * i), ps("e as", "i", 56, TINTA2) + [(s, "g", 58)], X, 610 + i * 80, "center", 0.12)
    E.foco(c, t, c4, 0.5, lambda a: E.pilula(c, "ponto notável", X, 920, 72, "g", a=a, cor=E.SOBRE))


def b_baricentro(c, t, C, b):
    A, B, Cc = TA, TB, TC
    G = baric(A, B, Cc)
    X = 1480
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    triang(c, t, C["s05"] - 1.0, A, B, Cc)
    medianas(c, t, C["s05"] - 1.0, A, B, Cc, 0.0)
    notavel(c, t, a5, G, "G", lado=(1, 0.6))
    E.frase(c, t, a5, [("baricentro", "g", 100, COR)], X, 260, "center")
    E.frase(c, t, a5 + 0.6, ps("encontro das", "i", 58) + [("medianas", "g", 60)], X, 360, "center", 0.12)
    E.frase(c, t, b5, ps("bari =", "i", 66) + [("peso", "g", 72, COR)], X, 520, "center", 0.12)
    E.frase(c, t, b5 + 0.9, ps("ponto de", "i", 58) + [("equilíbrio", "g", 60)], X, 610, "center", 0.12)
    E.frase(c, t, c5, ps("sempre", "i", 64) + [("dentro", "g", 70, CERTO)], X, 780, "center", 0.12)


def b_incentro(c, t, C, b):
    A, B, Cc = TA, TB, TC
    I, r = incentro(A, B, Cc)
    X = 1480
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    triang(c, t, C["s06"] - 0.5, A, B, Cc)
    for i, (V, P, Q) in enumerate(((A, B, Cc), (B, Cc, A), (Cc, A, B))):
        linha(c, t, a6 + 0.4 * i, V, pe_bis(V, P, Q), AMBAR)
    if t >= c6:
        E.circulo(c, t, c6, I[0], I[1], r, o=None, cor=AMBAR, preenche=0.08)
    notavel(c, t, a6 + 1.4, I, "I", AMBAR, lado=(1, 0.6))
    E.frase(c, t, a6, [("incentro", "g", 100, AMBAR)], X, 260, "center")
    E.frase(c, t, a6 + 0.6, ps("encontro das", "i", 58) + [("bissetrizes", "g", 60)], X, 360, "center", 0.12)
    E.frase(c, t, b6, ps("in =", "i", 66) + [("dentro", "g", 72, AMBAR)], X, 520, "center", 0.12)
    E.frase(c, t, c6, ps("centro do círculo", "i", 58), X, 680, "center", 0.12)
    E.frase(c, t, c6 + 0.8, [("de dentro", "g", 64, AMBAR)], X, 770, "center")
    E.frase(c, t, lerp(c6, C["s06.end"], 0.6), ps("sempre", "i", 60) + [("dentro", "g", 64, CERTO)], X, 920, "center", 0.12)


def b_circuncentro(c, t, C, b):
    A, B, Cc = (esc(P) for P in (TA, TB, TC))
    O, R = circuncentro(A, B, Cc)
    X = 1500
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    if t >= c7:
        E.circulo(c, t, c7, O[0], O[1], R, o=None, cor=TINTA2, preenche=0.05)
    triang(c, t, C["s07"] - 0.5, A, B, Cc)
    for i, (P, Q) in enumerate(((B, Cc), (Cc, A), (A, B))):
        Mm = meio(P, Q)
        ux, uy = E._uni(*P, *Q)
        nx, ny = uy, -ux
        if (O[0] - Mm[0]) * nx + (O[1] - Mm[1]) * ny < 0:
            nx, ny = -nx, -ny
        L = math.dist(Mm, O) + 90
        t0 = a7 + 0.4 * i
        linha(c, t, t0, (Mm[0] - nx * 70, Mm[1] - ny * 70), (Mm[0] + nx * L, Mm[1] + ny * L), TINTA2, larg=5, ponta=False)
        q = ep(t, t0 + 0.4, 0.3)
        E.marcas_iguais(c, P, Mm, 1, TINTA2, q, tam=14, largura=4)
        E.marcas_iguais(c, Mm, Q, 1, TINTA2, q, tam=14, largura=4)
    if t >= d7:
        for i, V in enumerate((A, B, Cc)):
            linha(c, t, d7 + 0.3 * i, O, V, E.COR, larg=6, dash=[14, 10], ponta=False)
            E.marcas_iguais(c, O, V, 2, COR, ep(t, d7 + 0.3 * i + 0.6, 0.3))
    notavel(c, t, a7 + 1.4, O, "O", TINTA2, lado=(1, -0.4))
    E.frase(c, t, a7, [("circuncentro", "g", 90, TINTA2)], X, 230, "center")
    E.frase(c, t, a7 + 0.6, ps("encontro das", "i", 56) + [("mediatrizes", "g", 58)], X, 320, "center", 0.12)
    E.frase(c, t, b7, ps("circun =", "i", 64) + [("em volta", "g", 68, TINTA2)], X, 460, "center", 0.12)
    E.frase(c, t, c7, ps("círculo pelos", "i", 58) + [("3 vértices", "g", 60)], X, 600, "center", 0.12)
    E.frase(c, t, d7, [("mesma distância", "g", 64, COR)], X, 790, "center")
    E.frase(c, t, d7 + 0.8, ps("dos três vértices", "i", 58), X, 870, "center", 0.12)


# obtusângulo do ortocentro (B obtuso)
OB_, OC_ = (560, 500), (1080, 500)
OA_ = pt(OB_, 360, 115)


def b_ortocentro(c, t, C, b):
    A, B, Cc = OA_, OB_, OC_
    Hh = ortocentro(A, B, Cc)
    O, R = circuncentro(A, B, Cc)
    X = 1560
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    triang(c, t, C["s08"], A, B, Cc)
    # as três alturas, prolongadas até se cruzarem
    tl = lerp(b8, c8, 0.45)
    for i, (V, P, Q) in enumerate(((A, B, Cc), (Cc, A, B), (B, A, Cc))):
        F = pe(V, P, Q)
        t0 = a8 + 0.5 * i
        linha(c, t, t0, V, F, ponta=False)
        reto(c, t, t0 + 0.5, F, V, Q if math.dist(F, Q) > 30 else P, r=40)
        if t >= tl:  # prolonga até o ortocentro
            far = Hh if math.dist(V, Hh) > math.dist(V, F) else F
            M.line(c, *F, *far, E.COR, 1.0, 4, dash=[12, 10], progress=ease_io(prog(t, tl + 0.2 * i, 0.8)))
    if t >= tl:  # os lados prolongados
        for P, Q in ((Cc, B), (A, B)):
            ux, uy = E._uni(*P, *Q)
            far = max(math.dist(Q, pe(V, P, Q)) for V in (A, B, Cc)) + 60
            M.line(c, *Q, Q[0] + ux * far, Q[1] + uy * far, TINTA2, 0.8, 4, dash=E.TRACO, progress=ease_io(prog(t, tl, 0.6)))
    notavel(c, t, c8, Hh, "H", lado=(1, 0.3))
    if t >= d8:
        notavel(c, t, d8, O, "O", TINTA2, lado=(1, -0.3))
    E.frase(c, t, a8, [("ortocentro", "g", 96, COR)], X, 220, "center")
    E.frase(c, t, a8 + 0.6, ps("encontro das", "i", 56) + [("alturas", "g", 58)], X, 310, "center", 0.12)
    E.frase(c, t, b8, ps("orto =", "i", 64) + [("reto", "g", 70, COR)], X, 450, "center", 0.12)
    E.frase(c, t, lerp(b8, c8, 0.3), ps("obtusângulo:", "i", 58), X, 590, "center", 0.12)
    E.frase(c, t, c8, [("H fica fora", "g", 66, COR)], X, 690, "center")
    E.frase(c, t, d8, [("O também sai", "g", 62, TINTA2)], X, 820, "center")


def b_equilatero(c, t, C, b):
    a9 = C["s09.a"]
    X = 1500
    B, Cc = (240, 900), (940, 900)
    A = (590, 900 - 700 * math.sin(math.radians(60)))
    G = baric(A, B, Cc)
    triang(c, t, C["s09"], A, B, Cc)
    q = ep(t, C["s09"] + 0.6, 0.4)
    for P, Q in ((A, B), (B, Cc), (Cc, A)):
        E.marcas_iguais(c, P, Q, 1, TINTA, q)
    medianas(c, t, lerp(C["s09"], a9, 0.45), A, B, Cc, 0.4)
    # os quatro nomes chegam ao mesmo ponto
    for i, (nome, cor) in enumerate((("baricentro", COR), ("incentro", AMBAR), ("circuncentro", TINTA2), ("ortocentro", COR))):
        p = ease_io(prog(t, a9 + 0.2 * i, 0.9))
        y0 = 300 + i * 110
        if t >= a9:
            E.foco(c, t, a9 - 1.0 + 0.2 * i, 0.4, lambda k, nome=nome, cor=cor, y0=y0: centro(c, nome, X, y0, 58, "g", cor, k))
            M.line(c, X - 200, y0 - 18, lerp(X - 200, G[0] + 30, p), lerp(y0 - 18, G[1], p), cor, 0.6 * (1 - ep(t, a9 + 2.0, 0.5)), 3, dash=[8, 8])
        else:
            E.foco(c, t, lerp(C["s09"], a9, 0.6) + 0.2 * i, 0.4, lambda k, nome=nome, cor=cor, y0=y0: centro(c, nome, X, y0, 58, "g", cor, k))
    E.frase(c, t, C["s09"], ps("e no", "i", 66) + [("equilátero?", "g", 70, COR)], X, 180, "center", 0.12)
    notavel(c, t, a9 + 0.8, G, None)
    E.frase(c, t, a9 + 1.0, [("4 pontos = 1 só", "g", 70, COR)], X, 800, "center")


# ---------------- baricentro: dois para um ----------------
DA, DB, DC = (560, 180), (120, 900), (1060, 900)
DM = meio(DB, DC)


def b_dois_um(c, t, C, b):
    A, B, Cc, Mm = DA, DB, DC, DM
    X = 1480
    a10, b10 = C["s10.a"], C["s10.b"]
    a11, b11, c11, d11, e11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"]
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    G = (A[0] + 2 / 3 * (Mm[0] - A[0]), A[1] + 2 / 3 * (Mm[1] - A[1]))
    triang(c, t, C["s10"], A, B, Cc, nomes="A  ")
    E.foco(c, t, C["s10"] + 0.4, 0.4, lambda a: centro(c, "M", Mm[0], Mm[1] + 70, 58, "g", TINTA, a))
    linha(c, t, C["s10"] + 0.4, A, Mm, TINTA, larg=6)
    # s10: só as proporções; s11: os números; s12: de trás para frente
    if t < C["s11"]:
        mediana_2_1(c, t, A, Mm, b10, b10 + 0.6, "2", "1", lado=1, size=60)
    elif t < C["s12"]:
        mediana_2_1(c, t, A, Mm, c11, d11, "6", "3", lado=1, tq=b11)
        E.foco(c, t, a11, 0.4, lambda a: txt_seg(c, A, Mm, "9", -1, 60, TINTA, a * (1 - ep(t, c11, 0.3)), gap=40))
    else:
        mediana_2_1(c, t, A, Mm, a12, b12, "12", (lambda tt: "x" if tt < c12 + 1.0 else "6"), lado=1)
        E.foco(c, t, d12, 0.4, lambda a: txt_seg(c, A, Mm, "18", -1, 64, CERTO, a, gap=40))
    notavel(c, t, a10, G, "G", lado=(-1, 0), size=54)

    def um():
        E.frase(c, t, a10, ps("o baricentro divide", "i", 58), X, 240, "center", 0.12)
        E.frase(c, t, a10 + 0.9, ps("cada mediana em", "i", 58), X, 320, "center", 0.12)
        fcen(c, t, a10 + 1.6, "2 para 1", X, 460, 110, COR)
        E.frase(c, t, b10, ps("o pedaço do vértice", "i", 56), X, 620, "center", 0.12)
        E.frase(c, t, b10 + 1.0, ps("é o", "i", 56) + [("dobro", "g", 66, COR)] + ps("do pedaço do lado", "i", 56), X, 710, "center", 0.12)
    E.saida(c, t, C["s11"] - 0.1, um)
    if C["s11"] <= t < C["s12"] + 0.4:
        def dois():
            fcen(c, t, a11, "AM = 9", X, 240, 84)
            fcen(c, t, b11, "9 ÷ 3 = 3", X, 380, 84, TINTA2)
            fcen(c, t, c11, "AG = 2 · 3 = 6", X, 520, 76, COR)
            fcen(c, t, d11, "GM = 3", X, 660, 76, TINTA2)
            E.foco(c, t, e11, 0.5, lambda a: E.pilula(c, "6 é o dobro de 3", X, 820, 64, "g", a=a, cor=E.SOBRE))
        E.saida(c, t, C["s12"] - 0.1, dois)
    if t >= C["s12"]:
        E.frase(c, t, C["s12"], ps("de trás para frente", "i", 58), X, 200, "center", 0.12)
        fcen(c, t, a12, "AG = 12", X, 320, 80, COR)
        fcen(c, t, b12, "f{12}{x} = f{2}{1}", X, 490, 80)
        fcen(c, t, c12, "2x = 12", X, 640, 76)
        fcen(c, t, c12 + 1.0, "x = 6", X, 750, 76, TINTA2)
        bola_txt(c, t, d12, "18", X, 920, 100, 80, CERTO)
        E.frase(c, t, d12 + 0.3, ps("12 + 6", "g", 56, TINTA2), X - 260, 940, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    A, B, Cc, Mm = DA, DB, DC, DM
    X = 1480
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    G = (A[0] + 2 / 3 * (Mm[0] - A[0]), A[1] + 2 / 3 * (Mm[1] - A[1]))
    Gx = (A[0] + 1 / 3 * (Mm[0] - A[0]), A[1] + 1 / 3 * (Mm[1] - A[1]))  # o lugar errado
    E.frase(c, t, C["s13"], [("cuidado", "g", 84, ERRADO)] + ps("com este erro", "i", 70), X, 150, "center", 0.12)
    if t >= c13:  # o papelão: ponta fina, lado largo
        papelao(c, [A, B, Cc], ep(t, c13, 0.5), 0.55)
    triang(c, t, C["s13"] + 0.3, A, B, Cc, nomes="A  ")
    E.foco(c, t, C["s13"] + 0.6, 0.4, lambda a: centro(c, "M", Mm[0], Mm[1] + 70, 58, "g", TINTA, a))
    linha(c, t, C["s13"] + 0.6, A, Mm, TINTA, larg=6)
    errado = ep(t, b13, 0.4) * (1 - ep(t, d13, 0.4))
    if errado > 0:
        grosso(c, A, Gx, ERRADO, errado, 12)
        grosso(c, Gx, Mm, ERRADO, errado * 0.5, 12)
        c.drawCircle(*Gx, 18, M.paint(ERRADO, errado))
        txt_seg(c, A, Gx, "3", 1, 56, ERRADO, errado)
        txt_seg(c, Gx, Mm, "6", 1, 56, ERRADO, errado)
    if t >= c13:  # onde tem mais papelão
        k = ep(t, c13 + 0.6, 0.4) * (1 - ep(t, d13 + 1.5, 0.4))
        path = skia.Path(); path.addPoly([A, (A[0] + (B[0] - A[0]) * 0.25, A[1] + (B[1] - A[1]) * 0.25), (A[0] + (Cc[0] - A[0]) * 0.25, A[1] + (Cc[1] - A[1]) * 0.25)], True)
        c.drawPath(path, M.paint(ERRADO, 0.25 * k))
        E.foco(c, t, c13 + 0.6, 0.4, lambda a: centro(c, "fina", A[0] + 140, A[1] + 110, 46, "b", ERRADO, a * k))
        E.foco(c, t, c13 + 1.6, 0.4, lambda a: centro(c, "larga", Mm[0] + 220, Mm[1] - 40, 50, "b", CERTO, a * k))
    if t >= d13:
        mediana_2_1(c, t, A, Mm, d13, d13 + 0.3, "6", "3", lado=1, cor_l=CERTO)
        notavel(c, t, d13 + 0.3, G, "G", CERTO, lado=(-1, 0), size=54)
    E.frase(c, t, a13, [("inverter", "g", 70, ERRADO)] + ps("os pedaços", "i", 64), X, 290, "center", 0.12)
    E.frase(c, t, b13, [("3", "g", 66, ERRADO)] + ps("no vértice,", "i", 56) + [("6", "g", 66, ERRADO)] + ps("no lado", "i", 56), X, 420, "center", 0.1)
    E.frase(c, t, c13, ps("ponta", "i", 58) + [("fina,", "g", 60, ERRADO)] + ps("lado", "i", 58) + [("largo", "g", 60, CERTO)], X, 590, "center", 0.12)
    E.frase(c, t, d13, ps("o equilíbrio fica", "i", 58), X, 750, "center", 0.12)
    E.frase(c, t, d13 + 0.8, [("perto do lado", "g", 66, CERTO)], X, 840, "center")


# ---------------- atalho (palco escuro) ----------------
def barra(c, t, x, y0, y1, ts, tl, tv, rots, a=1.0):
    """a mediana em pé, dividida em três: rots = (do vértice, do lado)"""
    if a <= 0:
        return
    q = ep(t, ts, 0.4) * a
    M.line(c, x, y0, x, y1, BR, q, 10)
    yg = y0 + 2 / 3 * (y1 - y0)
    for k in range(1, 3):
        yy = y0 + k / 3 * (y1 - y0)
        M.line(c, x - 24, yy, x + 24, yy, BR, ep(t, ts + 0.4, 0.3) * a, 5)
    grosso(c, (x, yg), (x, y1), CLARO, ep(t, tl, 0.4) * a, 16)
    grosso(c, (x, y0), (x, yg), AMBAR, ep(t, tv, 0.4) * a, 16)
    E.foco(c, t, tl + 0.2, 0.4, lambda k: centro(c, rots[1], x + 150, (yg + y1) / 2 + 22, 64, "g", CLARO, k * a))
    E.foco(c, t, tv + 0.2, 0.4, lambda k: centro(c, rots[0], x + 150, (y0 + yg) / 2 + 22, 64, "g", AMBAR, k * a))
    E.foco(c, t, ts, 0.4, lambda k: (centro(c, "vértice", x - 130, y0 + 18, 44, "i", CLARO, k * a), centro(c, "lado", x - 100, y1 + 18, 44, "i", CLARO, k * a)))


def gangorra(c, t, t0, cx, cy, L, a=1.0, ta=None, tb=None):
    """tábua A—M apoiada em G (2/3 do caminho): uma moeda em A, duas em M"""
    if t < t0 or a <= 0:
        return
    xa, xm = cx - 2 * L / 3, cx + L / 3
    path = skia.Path(); path.moveTo(cx, cy); path.lineTo(cx - 50, cy + 90); path.lineTo(cx + 50, cy + 90); path.close()
    c.drawPath(path, M.paint(CLARO, a))
    M.rrect(c, xa - 30, cy - 18, L + 60, 18, 8, BR, a)
    q = ep(t, ta or t0, 0.4) * a
    E.moeda(c, xa, cy - 18 - 46, 44, "1", q, AMBAR)
    E.moeda(c, xm, cy - 18 - 46, 44, "1", q, AMBAR)
    E.moeda(c, xm, cy - 18 - 46 - 70, 44, "1", q, AMBAR)
    E.foco(c, t, (ta or t0) + 0.2, 0.4, lambda k: (centro(c, "A", xa, cy + 70, 54, "g", CLARO, k * a), centro(c, "M", xm, cy + 70, 54, "g", CLARO, k * a)))
    if tb is not None:
        k = ep(t, tb, 0.4) * a
        E.chave(c, xa, cx, cy + 120, AMBAR, k, 20)
        E.chave(c, cx, xm, cy + 120, CLARO, k, 20)
        E.foco(c, t, tb + 0.3, 0.4, lambda q: (centro(c, "2", (xa + cx) / 2, cy + 220, 70, "g", AMBAR, q * a), centro(c, "1", (cx + xm) / 2, cy + 220, 70, "g", CLARO, q * a)))


def b_atalho(c, t, C, b):
    palco(c, t)
    X = 1300
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    a15, b15 = C["s15.a"], C["s15.b"]
    a16, b16, c16, d16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]

    def um():
        x, y0, y1 = 420, 220, 880
        barra(c, t, x, y0, y1, C["s14"] + 0.3, b14, c14, ((lambda: "20" if t >= d14 + 0.8 else "dobro")(), (lambda: "10" if t >= d14 else "÷ 3")()))
        E.frase(c, t, a14, ps("divida a mediana", "i", 64, CLARO) + [("por 3", "g", 76, BR)], X, 260, "center", 0.12)
        E.frase(c, t, b14, ps("= pedaço do", "i", 60, CLARO) + [("lado", "g", 66, BR)], X, 390, "center", 0.12)
        E.frase(c, t, c14, ps("o dobro = pedaço do", "i", 60, CLARO) + [("vértice", "g", 66, AMBAR)], X, 510, "center", 0.12)
        fcen(c, t, d14, "30 ÷ 3 = 10", X, 680, 84, CLARO)
        fcen(c, t, d14 + 0.8, "2 · 10 = 20", X, 800, 84, AMBAR)
        E.frase(c, t, d14 + 1.4, ps("de cabeça", "i", 60, CLARO), X, 920, "center", 0.12)
    E.saida(c, t, C["s15"] - 0.1, um)

    if C["s15"] <= t < C["s16"] + 0.4:
        def dois():
            A, B, Cc = (560, 200), (180, 880), (1000, 880)
            Mm = meio(B, Cc)
            G = baric(A, B, Cc)
            triang(c, t, C["s15"], A, B, Cc, nomes=None, tinta=BR, preenche=0.12)
            E.frase(c, t, C["s15"], ps("uma imagem,", "i", 60, CLARO) + [("não prova", "g", 60, BR)], 1480, 220, "center", 0.12)
            q = ep(t, a15, 0.4)
            p = ease_io(prog(t, b15, 1.2))
            E.moeda(c, *A, 48, "1", q, AMBAR)
            for V in (B, Cc):
                E.moeda(c, lerp(V[0], Mm[0], p), lerp(V[1], Mm[1], p) - 60 * p * (1 if V == B else 0), 48, "1", q, AMBAR)
            notavel(c, t, a15 + 0.8, G, None, CLARO)
            if t >= b15:
                linha(c, t, b15, A, Mm, CLARO, larg=5, dash=[12, 10], ponta=False)
            E.frase(c, t, a15, ps("uma moeda", "i", 60, CLARO) + [("em cada vértice", "g", 60, BR)], 1480, 380, "center", 0.12)
            E.frase(c, t, a15 + 1.6, ps("equilibram no", "i", 60, CLARO) + [("baricentro", "g", 62, BR)], 1480, 480, "center", 0.12)
            E.frase(c, t, b15, ps("B e C:", "i", 60, CLARO) + [("juntas no M", "g", 64, AMBAR)], 1480, 660, "center", 0.12)
        E.saida(c, t, C["s16"] - 0.1, dois)
    if t >= C["s16"]:
        def tres():
            gangorra(c, t, C["s16"], 1100, 600, 840, 1.0, a16, b16)
            E.frase(c, t, a16, ps("1 moeda no", "i", 60, CLARO) + [("A,", "g", 64, BR)] + ps("2 no", "i", 60, CLARO) + [("M", "g", 64, BR)], W / 2, 200, "center", 0.12)
            E.frase(c, t, lerp(a16, b16, 0.45), ps("o lado mais pesado senta", "i", 54, CLARO) + [("mais perto", "g", 56, BR)], W / 2, 300, "center", 0.1)
            E.frase(c, t, b16, ps("o braço da moeda sozinha:", "i", 56, CLARO) + [("o dobro", "g", 62, AMBAR)], W / 2, 980, "center", 0.12)
        E.saida(c, t, c16 - 0.1, tres)
        if t >= c16:
            E.frase(c, t, c16, ps("nos outros pontos notáveis?", "i", 66, CLARO), W / 2, 400, "center", 0.12)
            E.foco(c, t, c16 + 1.0, 0.5, lambda a: E.pilula(c, "não vale", W / 2, 540, 72, "g", fundo=ERRADO, a=a))
            E.frase(c, t, d16, [("2 para 1", "g", 110, BR)], W / 2, 760, "center")
            E.frase(c, t, d16 + 0.6, ps("é só do", "i", 70, CLARO) + [("baricentro", "g", 76, AMBAR)], W / 2, 890, "center", 0.12)


# ---------------- questão ----------------
Q1A, Q1B, Q1C = (420, 130), (130, 520), (800, 520)
Q1M = meio(Q1B, Q1C)
Q2 = [(180, 1010), (880, 1010), (720, 700)]


def fig1(c, t, t0, rot_v, rot_l, tv=None, tl=None, tq=None):
    A, B, Cc, Mm = Q1A, Q1B, Q1C, Q1M
    triang(c, t, t0, A, B, Cc, nomes="A  ")
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: centro(c, "M", Mm[0], Mm[1] + 66, 54, "g", TINTA, a))
    linha(c, t, t0 + 0.4, A, Mm, TINTA, larg=5)
    G = mediana_2_1(c, t, A, Mm, tv if tv is not None else t0 + 0.8, tl if tl is not None else t0 + 0.8, rot_v, rot_l, lado=1, size=50, tq=tq)
    notavel(c, t, t0 + 0.8, G, "G", lado=(-1, 0), size=50, pulsa=False)
    return G


def fig2(c, t, t0, a=1.0):
    for i, P in enumerate(Q2):
        E.foco(c, t, t0 + 0.2 * i, 0.4, lambda k, P=P: casa(c, P[0], P[1] + 30, 1.0, k * a))
    if t >= t0 + 0.6:
        path = skia.Path(); path.addPoly(Q2, True)
        p = M.paint(TINTA2, 0.7 * ep(t, t0 + 0.6, 0.4) * a, stroke=3)
        p.setPathEffect(skia.DashPathEffect.Make([10, 10], 0))
        c.drawPath(path, p)


def b_questao(c, t, C, b):
    X = 1490
    a17, b17, a18, b18, c18 = C["s17.a"], C["s17.b"], C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), X, 160, "center", 0.12)
    fig1(c, t, a17, "?", "7 cm", tv=b17, tl=a17 + 1.0)
    if t >= a18:
        fig2(c, t, a18)
        Gq = baric(*Q2)
        E.foco(c, t, b18, 0.4, lambda a: (E.bola(c, Gq[0], Gq[1] - 30, 40, a=a), centro(c, "+", Gq[0], Gq[1] - 30 + 22, 64, "g", BR, a)))
        E.foco(c, t, b18 + 0.5, 0.4, lambda a: centro(c, "?", Gq[0] + 70, Gq[1] - 10, 60, "g", ERRADO, a))
    E.frase(c, t, b17, [("1)", "g", 58, COR), ("GM = 7 cm.", "g", 58), ("AM = ?", "g", 58, COR)], X, 880, "center", 0.12)
    E.frase(c, t, c18, [("2)", "g", 58, COR)] + ps("mesma distância:", "i", 54) + [("qual ponto?", "g", 58, COR)], X, 990, "center", 0.12)
    if t < C["s19.a"]:
        def lado():
            E.frase(c, t, a18, ps("posto de saúde à", "i", 58), X, 420, "center", 0.12)
            E.frase(c, t, b18, [("mesma distância", "g", 62, COR)], X, 510, "center")
            E.frase(c, t, b18 + 0.8, ps("de três bairros", "i", 58), X, 600, "center", 0.12)
        E.saida(c, t, C["s19.a"] - 0.5, lado)
    E.relogio(c, t, C["s19.a"], cy=470, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    X = 1480
    a20, b20, c20, a21, b21, c21 = C["s20.a"], C["s20.b"], C["s20.c"], C["s21.a"], C["s21.b"], C["s21.c"]

    def um():
        A, B, Cc = (560, 190), (200, 900), (1020, 900)
        Mm = meio(B, Cc)
        triang(c, t, C["s20"] - 1.0, A, B, Cc, nomes="A  ")
        centro(c, "M", Mm[0], Mm[1] + 70, 58, "g", TINTA)
        linha(c, t, C["s20"] - 1.0, A, Mm, TINTA, larg=6, ponta=False)
        G = mediana_2_1(c, t, A, Mm, b20, a20, (lambda tt: "?" if tt < b20 else "14"), "7", lado=1)
        notavel(c, t, C["s20"] - 1.0, G, "G", lado=(-1, 0), size=54, pulsa=False)
        E.foco(c, t, c20 + 0.3, 0.4, lambda a: txt_seg(c, A, Mm, "21", -1, 64, CERTO, a, gap=40))
        E.frase(c, t, a20, [("7", "g", 70, TINTA2)] + ps("é o pedaço do lado", "i", 58), X, 280, "center", 0.12)
        fcen(c, t, b20, "2 · 7 = 14", X, 440, 84, COR)
        fcen(c, t, c20, "7 + 14 = 21", X, 600, 84)
        bola_txt(c, t, c20 + 0.6, "21 cm", X, 800, 120, 70, CERTO)
    E.saida(c, t, C["s21"] - 0.1, um)
    if t < C["s21"]:
        return
    pts = [(200, 850), (1000, 850), (260, 330)]
    O, R = circuncentro(*pts)
    G = baric(*pts)
    for i, P in enumerate(pts):
        casa(c, P[0], P[1] + 30, 1.0, ep(t, C["s21"] + 0.1 * i, 0.4))
    path = skia.Path(); path.addPoly(pts, True)
    p = M.paint(TINTA2, 0.7 * ep(t, C["s21"], 0.4), stroke=3)
    p.setPathEffect(skia.DashPathEffect.Make([10, 10], 0))
    c.drawPath(path, p)
    if t >= a21:
        E.circulo(c, t, a21, O[0], O[1], R, o=None, cor=TINTA2, preenche=0.0, largura=4)
        for i, V in enumerate(pts):
            linha(c, t, a21 + 0.5 + 0.2 * i, O, V, CERTO, larg=6, ponta=False)
            E.marcas_iguais(c, O, V, 2, CERTO, ep(t, a21 + 1.2, 0.3))
        notavel(c, t, a21 + 0.4, O, "O", CERTO, lado=(1, -0.6))
    if t >= b21:
        k = ep(t, b21, 0.4)
        for V in pts:
            M.line(c, *G, *V, ERRADO, k, 4, dash=[8, 8])
        c.drawCircle(*G, 14, M.paint(ERRADO, k))
        E.foco(c, t, b21 + 0.2, 0.4, lambda a: centro(c, "G", G[0] - 10, G[1] + 70, 54, "g", ERRADO, a))
    E.foco(c, t, a21, 0.5, lambda a: E.pilula(c, "circuncentro", X, 260, 76, "g", fundo=CERTO, a=a))
    E.frase(c, t, a21 + 0.6, ps("encontro das", "i", 56) + [("mediatrizes", "g", 58)], X, 380, "center", 0.12)
    E.frase(c, t, b21, [("baricentro?", "g", 64, ERRADO)], X, 540, "center")
    E.frase(c, t, b21 + 0.8, ps("equilíbrio", "i", 58) + [("≠ distância", "g", 60, ERRADO)], X, 630, "center", 0.12)
    E.frase(c, t, c21, ps("fora do equilátero,", "i", 56), X, 780, "center", 0.12)
    E.frase(c, t, c21 + 0.8, [("G não é equidistante", "g", 56, ERRADO)], X, 860, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 160, "center")
        itens = (("s22.a", "medianas", "baricentro", COR), ("s22.b", "bissetrizes", "incentro", AMBAR),
                 ("s22.c", "mediatrizes", "circuncentro", TINTA2), ("s22.d", "alturas", "ortocentro", COR))
        for i, (k, l, p, cor) in enumerate(itens):
            y = 320 + i * 140
            E.frase(c, t, C[k], [(l, "i", 64)], 840, y, "right")
            E.frase(c, t, C[k] + 0.2, [("→", "g", 60, TINTA2)], 900, y)
            E.frase(c, t, C[k] + 0.3, [(p, "g", 70, cor)], 990, y)
        E.foco(c, t, C["s22.e"], 0.5, lambda a: E.pilula(c, "baricentro: 2 para 1", W / 2, 940, 70, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"] + 0.2, ps("próxima aula", "i", 84), XE, 280)
    E.frase(c, t, C["s23.a"], [("praticando", "g", 120, COR)], XE, 430)
    E.frase(c, t, C["s23.b"], ps("paralelas, soma dos ângulos,", "i", 64), XE, 560, passo=0.1)
    E.frase(c, t, C["s23.b"] + 0.8, ps("isósceles e", "i", 64) + [("pontos notáveis", "g", 68)], XE, 650, passo=0.1)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1630, p), lerp(720, 425, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, encontro=b_encontro, baricentro=b_baricentro, incentro=b_incentro,
              circuncentro=b_circuncentro, ortocentro=b_ortocentro, equilatero=b_equilatero, dois_um=b_dois_um, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
