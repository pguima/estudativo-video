"""Visual — Estudativo · MAT-ANG-011: Tales no triângulo e teorema da bissetriz interna (lados 6 e 9, oposto 10: pedaços 4 e 6).
Linguagem da geometria plana (MAT-ANG-001 a 020): lados em tinta; ângulos iguais com a mesma cor (as duas metades da
bissetriz em TINTA2, cunha clara); paralela extra tracejada; medidas na grotesca; tracinhos de lados iguais; erro em
vermelho, certo em verde; resposta na esfera; atalho no palco escuro.
Famílias de cor desta aula: o que fica em cima / junto de AB vai em COR (índigo); o que fica embaixo / junto de AC vai em AMBAR.
Assim "cada pedaço acompanha o lado que encosta nele" se vê pela cor: AB e BD índigo, AC e DC âmbar.
As figuras são honestas: AM = 2, MB = 3, AN = 4, NC = 6 (AB = 5, AC = 10, BC = 9) e o triângulo 6, 9, 10 em escala, com D
calculado pelo próprio teorema (BD = 4). No "por que vale", C escorrega e D é recalculado a cada quadro.
Peças locais (as da MAT-ANG-009/010): cunha_m(), faixa_v(), metades(), triang(), txt_lado(), pedaco(), frac2(), prop(), cruz(),
ponto(), barra_partes() (o lado dividido em partes, no atalho).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-011_tales_no_triangulo_e_bissetriz_interna.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("tales", "bissetriz", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
AMB_C = "#FFB238"
XT = 1500
assert 2 * 6 == 3 * 4 and 12 // 2 == 6
assert 9 * 4 == 6 * (10 - 4) and 9 * 4 + 6 * 4 == 60 and 60 // 15 == 4 and 10 - 4 == 6
assert 6 // 3 == 2 and 9 // 3 == 3 and 2 + 3 == 5 and 10 // 5 == 2 and 2 * 2 == 4 and 3 * 2 == 6
assert 8 // 4 == 2 and 12 // 4 == 3 and 15 // 5 == 3 and 2 * 3 == 6 and 3 * 3 == 9 and 6 * 12 == 9 * 8 == 72


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


def meio(P, Q):
    return (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2


def entre(P, Q, k):
    return lerp(P[0], Q[0], k), lerp(P[1], Q[1], k)


def dist(P, Q):
    return math.hypot(Q[0] - P[0], Q[1] - P[1])


def cunha_m(c, V, g1, g2, r, cor, a=1.0, alfa=0.3, borda=6):
    if a <= 0:
        return
    ret = skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r)
    path = skia.Path()
    path.moveTo(*V); path.arcTo(ret, -g1, -(g2 - g1), False); path.close()
    c.drawPath(path, M.paint(cor, alfa * a))
    if borda:
        p = M.paint(cor, a, stroke=borda, cap_round=True)
        p.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(path, p)


def dirg(V, P):
    return math.degrees(math.atan2(-(P[1] - V[1]), P[0] - V[0])) % 360


def faixa_v(V, P, Q):
    a1, a2 = dirg(V, P), dirg(V, Q)
    d = (a2 - a1) % 360
    return (a1, a1 + d) if d <= 180 else (a2, a2 + (360 - d))


def metades(c, t, t0, V, P, Q, cor=TINTA2, r=90, a=1.0):
    """o ângulo PVQ cortado ao meio: duas cunhas iguais, da mesma cor"""
    if t < t0 or a <= 0:
        return
    g1, g2 = faixa_v(V, P, Q)
    gm = (g1 + g2) / 2
    q = ease_io(prog(t, t0, 0.5))
    cunha_m(c, V, g1, g1 + (gm - g1) * q, r, cor, a, alfa=0.22, borda=5)
    cunha_m(c, V, gm, gm + (g2 - gm) * q, r * 0.86, cor, a, alfa=0.22, borda=5)


def triang(c, t, t0, A, B, C, nomes="ABC", tinta=TINTA, preenche=0.05, d=0.9, a=1.0):
    if t < t0 or a <= 0:
        return
    pts = [A, B, C]
    if preenche:
        path = skia.Path(); path.addPoly(pts, True)
        c.drawPath(path, M.paint(E.COR, preenche * ep(t, t0 + d * 0.6, 0.5) * a))
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


def txt_lado(c, P, Q, s, G, size=56, cor=None, a=1.0, gap=22):
    """medida do lado PQ, do lado de fora (longe do ponto G)"""
    if a <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = meio(P, Q)
    if (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 < (mx - G[0]) ** 2 + (my - G[1]) ** 2:
        nx, ny = -nx, -ny
    E._cola(c, s, mx, my, nx, ny, gap, size, "g", cor or COR, a)


def lab(c, t, t0, P, Q, s, G, cor=None, size=56, gap=22):
    if t >= t0:
        E.foco(c, t, t0, 0.4, lambda a: txt_lado(c, P, Q, s, G, size, cor, a, gap))


def lab_troca(c, t, t0, t1, P, Q, s0, s1, G, cor0, cor1, size=56, gap=22):
    E.saida(c, t, t1, lambda: lab(c, t, t0, P, Q, s0, G, cor0, size, gap))
    lab(c, t, t1, P, Q, s1, G, cor1, size, gap)


def pedaco(c, t, t0, P, Q, cor=None, a=1.0, larg=14, d=0.5):
    if a <= 0 or t < t0:
        return
    M.line(c, *P, *Q, cor or E.COR, a, larg, progress=ease_io(prog(t, t0, d)))


def ponto(c, t, t0, P, nome, dx=0, dy=60, cor=TINTA, size=56, a=1.0):
    if t < t0 or a <= 0:
        return
    k = ease_back(prog(t, t0, 0.4))
    c.drawCircle(*P, 11 * k, M.paint(cor, a))
    if nome:
        E.foco(c, t, t0 + 0.1, 0.4, lambda f: centro(c, nome, P[0] + dx, P[1] + dy, size, "g", cor, f * a))


def linha(c, t, t0, P, Q, cor=TINTA, larg=6, d=0.6, a=1.0, dash=None):
    if t >= t0 and a > 0:
        M.line(c, *P, *Q, cor, a, larg, dash=dash, progress=ease_io(prog(t, t0, d)))


def frac2(c, n, d, cx, cy, size, cn=TINTA, cd=TINTA, a=1.0, barra=TINTA):
    if a <= 0:
        return
    n, d = str(n), str(d)
    wn, wd = E.formula(None, n, 0, 0, size, "g", a=0), E.formula(None, d, 0, 0, size, "g", a=0)
    lw = max(wn, wd) + size * 0.2
    E.formula(c, n, cx, cy - size * 0.2, size, "g", cn, a, "center")
    E.formula(c, d, cx, cy + size * 0.9, size, "g", cd, a, "center")
    b = size * 0.085
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - lw / 2, cy - b / 2 + size * 0.03, lw, b), b / 2, b / 2), M.paint(barra, a))


def prop(c, t, t0, n1, d1, n2, d2, cx, cy, size=100, cores=(COR, AMBAR, COR, AMBAR), t1=None, dx=170, barra=TINTA, igual=TINTA):
    t1 = t0 + 0.6 if t1 is None else t1
    E.foco(c, t, t0, 0.5, lambda a: frac2(c, n1, d1, cx - dx, cy, size, cores[0], cores[1], a, barra))
    E.foco(c, t, t1, 0.5, lambda a: (centro(c, "=", cx, cy + size * 0.36, size, "g", igual, a),
                                     frac2(c, n2, d2, cx + dx, cy, size, cores[2], cores[3], a, barra)))


def cruz(c, t, t0, t1, cx, cy, size=100, dx=170, c1=None, c2=AMBAR, wa=50, wb=60):
    """produto cruzado: as duas diagonais pulam o = do meio"""
    xa, xb = cx - dx, cx + dx
    for tt, (P, Q), cor in ((t0, ((xa + wa, cy - size * 0.7), (xb - wb, cy + size * 0.95)), c1 or E.COR),
                            (t1, ((xa + wa, cy + size * 0.95), (xb - wb, cy - size * 0.7)), c2)):
        p = ease_io(prog(t, tt, 0.6))
        for u0, u1 in ((0.0, 0.36), (0.64, 1.0)):
            if p > u0:
                u = min(p, u1)
                M.line(c, *entre(P, Q, u0), *entre(P, Q, u), cor, 0.85, 7)


def seta_par(c, P, Q, k=0.5, a=1.0, cor=TINTA):
    """setinha de paralela no ponto k da reta PQ"""
    if a <= 0:
        return
    x, y = entre(P, Q, k)
    ux, uy = E._uni(*P, *Q)
    for s in (1, -1):
        M.line(c, x - ux * 20 + uy * 16 * s, y - uy * 20 - ux * 16 * s, x, y, cor, a, 5)


# ---------------- figuras ----------------
# Tales no triângulo: AB = 5 (AM 2 + MB 3), AC = 10 (AN 4 + NC 6), BC = 9, a 100 px por unidade
U = 100
_x = (5 ** 2 - 10 ** 2 + 9 ** 2) / (2 * 9)          # pé da altura de A, medido a partir de B
TB, TC = (200, 900), (200 + 9 * U, 900)
TA = (200 + _x * U, 900 - math.sqrt(5 ** 2 - _x ** 2) * U)
TM, TN = entre(TA, TB, 0.4), entre(TA, TC, 0.4)
TG = ((TA[0] + TB[0] + TC[0]) / 3, (TA[1] + TB[1] + TC[1]) / 3)
assert abs(dist(TA, TB) - 500) < 1 and abs(dist(TA, TC) - 1000) < 1 and abs(TM[1] - TN[1]) < 0.01


def tri_lados(ab, ac, bc, B, u):
    """triângulo de lados AB = ab, AC = ac, BC = bc, com B dado, BC deitado e u pixels por unidade"""
    x = (ab ** 2 - ac ** 2 + bc ** 2) / (2 * bc)
    h = math.sqrt(ab ** 2 - x ** 2)
    return (B[0] + x * u, B[1] - h * u), B, (B[0] + bc * u, B[1])


# bissetriz: 6, 9, 10 a 90 px por unidade; D a 4 de B
BA, BB, BC_ = tri_lados(6, 9, 10, (160, 880), 90)
BD = entre(BB, BC_, 0.4)
BG = ((BA[0] + BB[0] + BC_[0]) / 3, (BA[1] + BB[1] + BC_[1]) / 3)
# questão: 8, 12, 15 a 62 px por unidade; D a 6 de B
QA, QB, QC = tri_lados(8, 12, 15, (150, 860), 62)
QD = entre(QB, QC, 0.4)
QG = ((QA[0] + QB[0] + QC[0]) / 3, (QA[1] + QB[1] + QC[1]) / 3)


def fig_bis(c, t, t0, tb, A=BA, B=BB, Cc=BC_, D=BD, G=BG, lados=None, cores=True, tp=None, nomes="ABC", a=1.0):
    """triângulo com a bissetriz de A até D. lados = (AB, AC, BC); tp = instante das cores de família"""
    triang(c, t, t0, A, B, Cc, nomes, a=a)
    if t >= tb:
        metades(c, t, tb + 0.4, A, B, Cc, TINTA2, 100, a)
        linha(c, t, tb, A, D, TINTA, 6, 0.7, a)
        ponto(c, t, tb + 0.6, D, "D", 0, 64, a=a)
    if tp is not None:
        k = ep(t, tp, 0.4) * a
        if k > 0:
            M.line(c, *A, *B, COR, 0.3 * k, 30)
            M.line(c, *B, *D, COR, 0.3 * k, 30)
            M.line(c, *A, *Cc, AMBAR, 0.3 * k, 30)
            M.line(c, *D, *Cc, AMBAR, 0.3 * k, 30)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    A, B, Cc, D = BA, BB, BC_, BD
    Mm = meio(B, Cc)

    def um():
        triang(c, t, ka, A, B, Cc)
        lab(c, t, ka + 0.6, A, B, "6", BG, COR, 64)
        lab(c, t, ka + 1.0, A, Cc, "9", BG, AMBAR, 64)
        E.saida(c, t, kd + 0.4, lambda: lab(c, t, ka + 2.0, B, Cc, "10", BG, TINTA, 64, 30))
        # a bissetriz chega primeiro ao meio (o chute), depois vai para o lugar certo
        if t >= kb:
            metades(c, t, kb + 0.4, A, B, Cc, TINTA2, 100)
            q = ease_io(prog(t, kd, 0.8))
            P = entre(Mm, D, q)
            linha(c, t, kb, A, P, TINTA, 6, 0.7)
            ponto(c, t, kb + 0.6, P, None)
        if kc <= t:
            E.saida(c, t, kd, lambda: E.foco(c, t, kc, 0.4, lambda a: (centro(c, "5", lerp(B[0], Mm[0], 0.5), B[1] + 70, 60, "g", ERRADO, a),
                                                                      centro(c, "5", lerp(Mm[0], Cc[0], 0.5), B[1] + 70, 60, "g", ERRADO, a))))
        if t >= kd + 0.6:
            pedaco(c, t, kd + 0.6, B, D, COR, 1, 14)
            pedaco(c, t, kd + 0.8, D, Cc, AMBAR, 1, 14)
            E.foco(c, t, kd + 0.8, 0.4, lambda a: (centro(c, "4", meio(B, D)[0], B[1] + 70, 64, "g", COR, a),
                                                   centro(c, "6", meio(D, Cc)[0], B[1] + 70, 64, "g", AMBAR, a)))
        E.frase(c, t, ka + 0.3, [("lados", "i", 70), ("6", "g", 84, COR), ("e", "i", 70), ("9", "g", 84, AMBAR)], XT, 260, "center", 0.12)
        E.frase(c, t, kb, [("bissetriz", "g", 80)], XT, 400, "center")
        E.frase(c, t, kb + 0.8, ps("corta o lado de 10", "i", 58), XT, 480, "center", 0.1)
        E.frase(c, t, kc, ps("o chute:", "i", 64) + [("5 e 5", "g", 76, ERRADO)], XT, 640, "center", 0.12)
        E.foco(c, t, kd, 0.4, lambda a: E.risco(c, XT + 15, 615, XT + 185, 615, t, kd, ERRADO, 9))
        E.frase(c, t, kd + 0.5, [("4", "g", 110, COR), ("e", "i", 90), ("6", "g", 110, AMBAR)], XT, 850, "center", 0.15)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.25), [("Tales", "g", 110, COR)] + ps("dentro do", "i", 84), XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), [("triângulo", "g", 110, COR)], XE, 580, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("os pedaços", "i", 84) + [("sem medir", "g", 84)], XE, 730, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 820
    itens = (("s03.b", "Teorema de Tales", "3/6 = 4/x → x = 8"), ("s03.c", "a bissetriz", "divide o ângulo ao meio"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
    py = lerp(420, 700, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 920, "left", 0.12)


# ---------------- Tales no triângulo ----------------
def b_tales(c, t, C, b):
    A, B, Cc, Mm, N = TA, TB, TC, TM, TN
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6 = C["s06.a"], C["s06.b"]
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    X0, X1 = 90, 1170
    # as três paralelas, prolongadas (na fala de "três paralelas")
    if t >= a5:
        linha(c, t, a5, (X0, A[1]), (X1, A[1]), TINTA2, 5, 0.8, dash=E.TRACO)
        E.foco(c, t, a5 + 0.4, 0.4, lambda f: E.escreve(c, "paralela pelo A", A[0] + 40, A[1] - 24, 44, "i", TINTA2, f))
    if t >= b5:
        k = ep(t, b5, 0.6)
        for P, Q in (((X0, Mm[1]), (Mm[0], Mm[1])), ((N[0], N[1]), (X1, N[1])), ((X0, B[1]), (B[0], B[1])), ((Cc[0], Cc[1]), (X1, Cc[1]))):
            M.line(c, *P, *Q, TINTA2, k, 4, dash=E.TRACO)
        for y in (A[1], Mm[1], B[1]):
            seta_par(c, (X0, y), (X1, y), 0.85, k, TINTA2)
    # as transversais
    k = ep(t, c5, 0.3) * (1 - ep(t, C["s06"], 0.4))
    if k > 0:
        M.line(c, *A, *B, TINTA, 0.22 * k, 34)
        M.line(c, *A, *Cc, TINTA, 0.22 * k, 34)
    triang(c, t, C["s04"] + 0.2 if t < a4 + 0.5 else a4, A, B, Cc)
    if t >= b4:
        linha(c, t, b4, Mm, N, TINTA, 6, 0.7)
        ponto(c, t, b4 + 0.6, Mm, "M", -56, 18)
        ponto(c, t, b4 + 1.2, N, "N", 30, -26)
        seta_par(c, Mm, N, 0.5, ep(t, b4 + 0.8, 0.3))
        seta_par(c, B, Cc, 0.5, ep(t, b4 + 0.8, 0.3))
    # os pedaços: em cima COR, embaixo AMBAR
    tp = a6
    pedaco(c, t, tp, A, Mm, COR); pedaco(c, t, tp + 0.4, Mm, B, AMBAR)
    pedaco(c, t, tp + 1.2, A, N, COR); pedaco(c, t, tp + 1.6, N, Cc, AMBAR)
    lab(c, t, a7, A, Mm, "2", TG, COR, 60)
    lab(c, t, a7 + 0.8, Mm, B, "3", TG, AMBAR, 60)
    lab(c, t, b7, A, N, "4", TG, COR, 60)
    lab_troca(c, t, b7 + 0.6, e7, N, Cc, "x", "6", TG, AMBAR, CERTO, 60)

    def quatro():
        E.frase(c, t, a4, [("triângulo", "g", 76), ("ABC", "g", 76, COR)], XT, 280, "center", 0.12)
        E.frase(c, t, b4, ps("MN", "g", 70) + ps("paralela a", "i", 64) + [("BC", "g", 70)], XT, 420, "center", 0.12)
    E.saida(c, t, a5 - 0.1, quatro)
    if a5 - 0.1 <= t < C["s06"]:
        def cinco():
            E.frase(c, t, a5, ps("onde está o", "i", 64) + [("feixe?", "g", 72, COR)], XT, 260, "center", 0.12)
            E.frase(c, t, b5, [("3", "g", 90, COR)] + ps("paralelas", "i", 76), XT, 420, "center", 0.12)
            E.frase(c, t, c5, ps("AB e AC:", "g", 64) + ps("as transversais", "i", 60), XT, 560, "center", 0.12)
        E.saida(c, t, C["s06"] - 0.1, cinco)
    if t >= C["s06"]:
        E.saida(c, t, a7 - 0.1, lambda: (E.frase(c, t, a6 - 0.6, ps("vale Tales:", "i", 64), XT, 230, "center", 0.12),
                                          E.frase(c, t, b6, ps("cima sobre baixo", "i", 56, TINTA2), XT, 640, "center", 0.12)))
        E.saida(c, t, c7 - 0.1, lambda: prop(c, t, a6, "AM", "MB", "AN", "NC", XT, 400, 90, t1=a6 + 1.6, dx=190))
    if t >= C["s07"]:
        prop(c, t, c7, "2", "3", "4", "x", XT, 330, 110, t1=c7 + 1.2)
        if t >= d7:
            cruz(c, t, d7, d7 + 0.5, XT, 330, 110)
        fcen(c, t, d7, "2x = 3 · 4 = 12", XT, 640, 80)
        fcen(c, t, e7, "x = 12 ÷ 2", XT - 90, 800, 76)
        bola_txt(c, t, e7 + 0.6, "6", XT + 210, 775, 76, 96, CERTO)


# ---------------- bissetriz ----------------
def b_bissetriz(c, t, C, b):
    A, B, Cc, D = BA, BB, BC_, BD
    Mm = meio(B, Cc)
    a8, b8 = C["s08.a"], C["s08.b"]
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a10, b10, c10 = (C[f"s10.{k}"] for k in "abc")
    a11, b11, c11 = (C[f"s11.{k}"] for k in "abc")
    a12, b12, c12 = (C[f"s12.{k}"] for k in "abc")
    t0 = C["s08"] + 0.2
    tb = a8 + 0.4 if t < a9 + 0.6 else a8 + 0.4
    fig_bis(c, t, t0, tb, tp=d9)
    # o meio do lado, para comparar (some quando o D ganha nome)
    k = ep(t, a8 + 1.2, 0.4) * (1 - ep(t, a9, 0.4))
    if k > 0:
        M.line(c, Mm[0], Mm[1] - 26, Mm[0], Mm[1] + 26, ERRADO, k, 6)
        centro(c, "meio", Mm[0], Mm[1] + 80, 48, "i", ERRADO, k)
    # medidas
    lab(c, t, a10, A, B, "6", BG, COR, 64)
    lab(c, t, a10 + 0.6, A, Cc, "9", BG, AMBAR, 64)
    lab_troca(c, t, b10, c12, B, D, "x", "4", BG, COR, CERTO, 60, 60)
    lab_troca(c, t, c10, c12 + 0.6, D, Cc, "10 − x", "6", BG, AMBAR, CERTO, 56, 60)

    def oito():
        E.frase(c, t, a8, ps("em geral,", "i", 60) + [("não", "g", 66, ERRADO)] + ps("corta ao meio", "i", 60), XT, 300, "center", 0.12)
        E.frase(c, t, b8, ps("teorema da", "i", 70), XT, 470, "center", 0.12)
        E.frase(c, t, b8 + 0.5, [("bissetriz", "g", 96, COR)], XT, 580, "center")
        E.frase(c, t, b8 + 0.9, [("interna", "g", 96, COR)], XT, 690, "center")
    E.saida(c, t, C["s09"] - 0.1, oito)
    if C["s09"] - 0.1 <= t < C["s10"]:
        def nove():
            E.frase(c, t, b9, ps("na razão dos", "i", 60) + [("lados vizinhos", "g", 64)], XT, 200, "center", 0.12)
            prop(c, t, c9, "BD", "DC", "AB", "AC", XT, 400, 100, t1=c9 + 1.6, dx=190)
            E.frase(c, t, d9, ps("cada pedaço", "i", 60), XT, 700, "center", 0.12)
            E.frase(c, t, d9 + 0.6, ps("acompanha o", "i", 60) + [("lado vizinho", "g", 64)], XT, 790, "center", 0.12)
        E.saida(c, t, C["s10"] - 0.1, nove)
    if t >= C["s10"]:
        E.saida(c, t, a12 - 0.1, lambda: (
            E.frase(c, t, a10, [("AB = 6", "g", 54, COR), ("AC = 9", "g", 54, AMBAR), ("BC = 10", "g", 54)], XT, 170, "center", 0.5),
            E.frase(c, t, b10, [("BD = x", "g", 60, COR)], XT - 180, 270, "center"),
            E.frase(c, t, c10, [("DC = 10 − x", "g", 60, AMBAR)], XT + 150, 270, "center")))
    if t >= C["s11"]:
        E.saida(c, t, a12 - 0.1, lambda: (
            prop(c, t, a11, "x", "10 − x", "6", "9", XT, 440, 90, t1=a11 + 1.6, dx=200),
            fcen(c, t, b11, "9x = 6 · (10 − x)", XT, 700, 72),
            fcen(c, t, c11, "9x = 60 − 6x", XT, 830, 76)))
    if t >= C["s12"]:
        fcen(c, t, a12 - 0.2, "9x = 60 − 6x", XT, 220, 64, TINTA2)
        fcen(c, t, a12 + 0.4, "9x + 6x = 60", XT, 360, 76)
        fcen(c, t, a12 + 1.4, "15x = 60", XT, 490, 84)
        fcen(c, t, b12, "x = 60 ÷ 15", XT - 90, 640, 76)
        bola_txt(c, t, b12 + 0.6, "4", XT + 200, 615, 70, 90, CERTO)
        E.frase(c, t, c12, [("BD = 4", "g", 70, COR)], XT, 800, "center")
        fcen(c, t, c12 + 0.6, "DC = 10 − 4 = 6", XT, 920, 70, AMBAR)


# ---------------- por que vale ----------------
def b_porque(c, t, C, b):
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    A, B = BA, BB
    # isósceles: AC = AB; depois C escorrega até o triângulo 6, 9, 10
    ab = dist(A, B)
    C0 = (A[0] + math.sqrt(ab ** 2 - (B[1] - A[1]) ** 2), B[1])
    q = ease_io(prog(t, c13, 1.6))
    Cc = entre(C0, BC_, q)
    ac = dist(A, Cc)
    D = entre(B, Cc, ab / (ab + ac))     # o próprio teorema
    G = ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3)
    E.frase(c, t, C["s13"] + 0.2, ps("por que", "i", 70) + [("faz sentido?", "g", 76, COR)], XT, 200, "center", 0.12)
    E.frase(c, t, C["s13"] + 1.6, ps("uma imagem, não uma prova", "i", 50, TINTA2), XT, 280, "center", 0.1)
    if t < a13:
        return
    triang(c, t, a13, A, B, Cc)
    metades(c, t, a13 + 0.8, A, B, Cc, TINTA2, 100)
    linha(c, t, a13 + 0.6, A, D, TINTA, 6, 0.7)
    ponto(c, t, a13 + 1.2, D, "D", 0, 64)
    k = ep(t, b13, 0.4) * (1 - ep(t, c13, 0.3))
    E.marcas_iguais(c, A, B, 1, TINTA, k)
    E.marcas_iguais(c, A, Cc, 1, TINTA, k)
    E.marcas_iguais(c, B, D, 2, COR, k)
    E.marcas_iguais(c, D, Cc, 2, COR, k)
    E.frase(c, t, a13, ps("no", "i", 64) + [("isósceles,", "g", 70)], XT, 420, "center", 0.12)
    E.frase(c, t, a13 + 1.0, ps("cai no meio da base", "i", 60), XT, 510, "center", 0.12)
    E.frase(c, t, b13, ps("lados iguais,", "i", 54) + [("pedaços iguais", "g", 58)], XT, 640, "center", 0.12)
    if t >= c13:
        pedaco(c, t, c13, A, Cc, AMBAR, 1, 14, 0.3)
        pedaco(c, t, c13, D, Cc, AMBAR, 1, 14, 0.3)
        pedaco(c, t, c13, A, B, COR, 1, 14, 0.3)
        pedaco(c, t, c13, B, D, COR, 1, 14, 0.3)
        E.frase(c, t, c13, ps("o lado", "i", 60) + [("cresce", "g", 66, AMBAR)], XT, 790, "center", 0.12)
        E.frase(c, t, c13 + 0.8, ps("o pedaço junto", "i", 60) + [("cresce", "g", 66, AMBAR)], XT, 880, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    A, B, Cc, D = BA, BB, BC_, BD
    a14, b14, c14, d14 = (C[f"s14.{k}"] for k in "abcd")
    a15, b15 = C["s15.a"], C["s15.b"]
    t0 = C["s14"]
    fig_bis(c, t, t0 - 0.6, t0 - 0.6)
    lab(c, t, t0 - 0.4, A, B, "6", BG, COR, 64)
    lab(c, t, t0 - 0.4, A, Cc, "9", BG, AMBAR, 64)
    lab_troca(c, t, c14, b15 + 0.4, B, D, "6", "4", BG, ERRADO, COR, 60, 60)
    lab_troca(c, t, c14 + 0.3, b15 + 0.4, D, Cc, "4", "6", BG, ERRADO, AMBAR, 60, 60)
    if t >= a15:
        k = ep(t, a15, 0.4)
        M.line(c, *A, *Cc, AMBAR, 0.3 * k, 30)
        M.line(c, *D, *Cc, AMBAR, 0.3 * k, 30)
    E.frase(c, t, t0 + 0.2, [("cuidado", "g", 84, ERRADO)], XT, 170, "center")

    def quatorze():
        E.frase(c, t, a14, ps("cada pedaço com o", "i", 58), XT, 270, "center", 0.12)
        E.frase(c, t, a14 + 1.0, [("lado errado", "g", 68, ERRADO)], XT, 350, "center")
        prop(c, t, b14, "BD", "DC", "9", "6", XT, 500, 96, cores=(TINTA, TINTA, ERRADO, ERRADO), t1=b14 + 1.6, dx=190)
        E.frase(c, t, c14, [("BD = 6", "g", 64, ERRADO), ("e", "i", 58), ("DC = 4", "g", 64, ERRADO)], XT, 760, "center", 0.12)
        E.frase(c, t, d14, [("trocados", "g", 76, ERRADO)], XT - 90, 900, "center")
        E.foco(c, t, d14 + 0.3, 0.4, lambda a: E.selo(c, XT + 200, 875, 50, False, a))
    E.saida(c, t, C["s15"] - 0.1, quatorze)
    if t >= C["s15"]:
        E.frase(c, t, a15, [("pedaço maior", "g", 66, AMBAR)], XT, 330, "center")
        E.frase(c, t, a15 + 0.8, ps("junto do", "i", 60) + [("lado maior", "g", 66, AMBAR)], XT, 420, "center", 0.12)
        E.frase(c, t, b15 - 1.6, [("AC = 9", "g", 70, AMBAR)] + ps("encosta em", "i", 60) + [("DC", "g", 70, AMBAR)], XT, 600, "center", 0.12)
        fcen(c, t, b15, "DC = 6", XT - 80, 790, 84, CERTO)
        E.foco(c, t, b15 + 0.5, 0.4, lambda a: E.selo(c, XT + 150, 765, 54, True, a))


# ---------------- atalho (palco escuro) ----------------
def barra_partes(c, t, t0, x0, x1, y, n, cores, a=1.0, larg=26, d=0.25):
    """segmento dividido em n partes iguais, que acendem uma a uma com a cor de cores[i]"""
    if a <= 0 or t < t0:
        return
    w = (x1 - x0) / n
    for i in range(n):
        k = ep(t, t0 + d * i, 0.3) * a
        if k > 0:
            M.rrect(c, x0 + i * w + 5, y - larg / 2, w - 10, larg, larg / 2, cores[i], k)


def b_atalho(c, t, C, b):
    palco(c, t)
    a16, b16, c16, d16, e16 = (C[f"s16.{k}"] for k in "abcde")
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    LIL = CLARO
    x0, x1, yb = 360, 1560, 560

    def dezesseis():
        E.frase(c, t, a16, [("divida", "g", 96, BR)] + ps("em partes", "i", 84, CLARO), W / 2, 200, "center", 0.12)
        E.frase(c, t, a16 + 1.5, [("6", "g", 76, LIL), ("para", "i", 64, CLARO), ("9", "g", 76, AMB_C)], W / 2 - 330, 360, "center", 0.12)
        E.foco(c, t, b16 - 0.4, 0.4, lambda a: centro(c, "÷ 3", W / 2, 360, 56, "b", CLARO, a))
        E.frase(c, t, b16, [("2", "g", 90, LIL), ("para", "i", 64, CLARO), ("3", "g", 90, AMB_C)], W / 2 + 330, 360, "center", 0.12)
        # o lado BC em cinco partes
        q = ep(t, c16 - 0.4, 0.4)
        if q > 0:
            M.line(c, x0, yb, x1, yb, BR, q * 0.35, 4)
            for xx, s in ((x0, "B"), (x1, "C"), (x0 + 2 / 5 * (x1 - x0), "D")):
                c.drawCircle(xx, yb, 12, M.paint(BR, q))
                centro(c, s, xx, yb - 40, 52, "g", BR, q)
        barra_partes(c, t, c16, x0, x1, yb, 5, (LIL, LIL, AMB_C, AMB_C, AMB_C), larg=48)
        E.foco(c, t, c16 + 1.4, 0.4, lambda a: (E.chave(c, x0 + 6, x0 + 2 / 5 * (x1 - x0) - 6, yb + 45, LIL, a, 26),
                                                E.chave(c, x0 + 2 / 5 * (x1 - x0) + 6, x1 - 6, yb + 45, AMB_C, a, 26)))
        E.foco(c, t, c16 + 1.6, 0.4, lambda a: (centro(c, "2 partes", x0 + 1 / 5 * (x1 - x0), yb + 120, 50, "i", LIL, a),
                                                centro(c, "3 partes", x0 + 7 / 10 * (x1 - x0), yb + 120, 50, "i", AMB_C, a)))
        fcen(c, t, d16, "10 ÷ 5 = 2", W / 2, 840, 84, BR)
        E.frase(c, t, e16, [("BD = 2 · 2 = 4", "g", 72, LIL)], W / 2 - 400, 990, "center")
        E.frase(c, t, e16 + 1.2, [("DC = 3 · 2 = 6", "g", 72, AMB_C)], W / 2 + 400, 990, "center")
        for i in range(5):
            E.foco(c, t, d16 + 0.6 + 0.1 * i, 0.3, lambda a, i=i: centro(c, "2", x0 + (i + 0.5) * (x1 - x0) / 5, yb + 14, 40, "g", "#0B0B14", a))
    E.saida(c, t, C["s17"] - 0.1, dezesseis)
    if t < C["s17"]:
        return
    E.frase(c, t, a17, [("2 para 3", "g", 110, BR)], W / 2, 260, "center")
    barra_partes(c, t, a17 + 0.6, 560, 1360, 430, 5, (LIL, LIL, AMB_C, AMB_C, AMB_C), d=0.15)
    E.frase(c, t, a17 + 1.4, ps("a cada", "i", 60, CLARO) + [("2", "g", 70, LIL)] + ps("em BD,", "i", 60, CLARO) + [("3", "g", 70, AMB_C)] + ps("em DC", "i", 60, CLARO), W / 2, 560, "center", 0.12)
    E.frase(c, t, b17, ps("a questão", "i", 64, CLARO) + [("já dá um pedaço?", "g", 70, AMB_C)], W / 2, 740, "center", 0.12)
    E.foco(c, t, c17, 0.5, lambda a: E.pilula(c, "proporção direta", W / 2, 880, 66, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]
    rel = C["s19.a"]
    A, B, Cc, D = QA, QB, QC, QD
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XT, 170, "center", 0.12)
    fig_bis(c, t, C["s18"] + 0.3, lerp(b18, c18, 0.5), A, B, Cc, D, QG)
    lab(c, t, a18, A, B, "8 cm", QG, COR, 56)
    lab(c, t, a18 + 1.2, A, Cc, "12 cm", QG, AMBAR, 56)
    E.foco(c, t, b18, 0.4, lambda a: centro(c, "BC = 15 cm", meio(B, Cc)[0], B[1] + 150, 54, "g", TINTA2, a))
    E.foco(c, t, c18, 0.4, lambda a: (centro(c, "?", meio(B, D)[0], B[1] + 70, 64, "g", COR, a),
                                      centro(c, "?", meio(D, Cc)[0], B[1] + 70, 64, "g", AMBAR, a)))

    def lado():
        E.frase(c, t, a18, [("AB = 8", "g", 66, COR), ("e", "i", 60), ("AC = 12", "g", 66, AMBAR)], XT, 380, "center", 0.12)
        E.frase(c, t, b18, [("BC = 15", "g", 66)], XT, 480, "center")
    E.saida(c, t, rel - 0.5, lado)
    E.frase(c, t, b18 + 0.8, ps("a bissetriz do A", "i", 56) + [("corta em D", "g", 60)], XT, 860, "center", 0.12)
    E.frase(c, t, c18, [("BD", "g", 64, COR), ("e", "i", 58), ("DC", "g", 64, AMBAR), ("?", "g", 64)], XT, 960, "center", 0.12)
    E.relogio(c, t, rel, XT, 420, 150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a20, b20, c20, d20, e20 = (C[f"s20.{k}"] for k in "abcde")
    a21, b21 = C["s21.a"], C["s21.b"]
    A, B, Cc, D = QA, QB, QC, QD
    t0 = C["s20"]
    fig_bis(c, t, t0 - 0.6, t0 - 0.6, A, B, Cc, D, QG)
    lab(c, t, t0 - 0.4, A, B, "8", QG, COR, 60)
    lab(c, t, t0 - 0.4, A, Cc, "12", QG, AMBAR, 60)
    E.foco(c, t, t0 - 0.4, 0.4, lambda a: centro(c, "15", meio(B, Cc)[0], B[1] + 160, 54, "g", TINTA2, a))
    # o lado em cinco partes, com as marcas
    if t >= b20:
        for i in range(1, 5):
            P = entre(B, Cc, i / 5)
            M.line(c, P[0], P[1] - 16, P[0], P[1] + 16, TINTA2, ep(t, b20 + 0.1 * i, 0.3), 5)
    pedaco(c, t, d20, B, D, COR, 1, 16)
    pedaco(c, t, e20, D, Cc, AMBAR, 1, 16)
    E.foco(c, t, d20 + 0.6, 0.4, lambda a: centro(c, "6 cm", meio(B, D)[0], B[1] + 80, 60, "g", CERTO, a))
    E.foco(c, t, e20 + 0.6, 0.4, lambda a: centro(c, "9 cm", meio(D, Cc)[0], B[1] + 80, 60, "g", CERTO, a))

    def vinte():
        E.frase(c, t, C["s20"] + 0.3, [("8", "g", 70, COR), ("e", "i", 60), ("12", "g", 70, AMBAR), ("÷ 4", "b", 56, TINTA2)], XT, 200, "center", 0.12)
        E.frase(c, t, a20, [("2", "g", 90, COR), ("para", "i", 64), ("3", "g", 90, AMBAR)], XT, 320, "center", 0.12)
        E.frase(c, t, b20, [("5", "g", 76), ("partes", "i", 64)], XT, 450, "center", 0.12)
        fcen(c, t, c20, "15 ÷ 5 = 3", XT, 580, 80)
        fcen(c, t, d20, "BD = 2 · 3 = 6", XT, 730, 70, COR)
        fcen(c, t, e20, "DC = 3 · 3 = 9", XT, 860, 70, AMBAR)
    E.saida(c, t, C["s21"] - 0.1, vinte)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("conferindo", "g", 72, COR)], XT, 200, "center")
    prop(c, t, a21, "6", "9", "8", "12", XT, 380, 100, t1=a21 + 1.4)
    if t >= b21:
        cruz(c, t, b21, b21 + 1.4, XT, 380, 100, c1=COR, c2=AMBAR, wa=55, wb=75)
    fcen(c, t, b21, "6 · 12 = 72", XT, 660, 72, COR)
    fcen(c, t, b21 + 1.4, "9 · 8 = 72", XT, 780, 72, AMBAR)
    E.foco(c, t, b21 + 2.6, 0.5, lambda a: E.selo(c, XT, 920, 70 * ease_back(prog(t, b21 + 2.6, 0.5)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s22.a", "paralela a um lado:", "corta os outros na mesma razão"),
                 ("s22.b", "bissetriz:", "pedaços na razão dos lados vizinhos"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 420 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 30, 56, a=a),
                                                         centro(c, str(i + 1), 240, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "i", 64)], 340, y - 20)
            E.frase(c, t, C[k] + 0.4, [(l2, "g", 64)], 340, y + 70)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    # a paralela separou um triângulo menor
    k = 0.42
    ox, oy = 1150, 120

    def P(Q):
        return ox + (Q[0] - 200) * k, oy + (Q[1] - TA[1]) * k
    if t >= C["s23"]:
        triang(c, t, C["s23"] + 0.2, P(TA), P(TB), P(TC), nomes="")
        linha(c, t, C["s23"] + 0.6, P(TM), P(TN), TINTA, 6)
        if t >= C["s23.a"]:
            path = skia.Path(); path.addPoly([P(TA), P(TM), P(TN)], True)
            c.drawPath(path, M.paint(E.COR, 0.4 * ep(t, C["s23.a"], 0.5)))
    E.frase(c, t, C["s23.a"], ps("um triângulo menor,", "i", 56), 1390, 430, "center", 0.1)
    E.frase(c, t, C["s23.a"] + 0.8, [("mesmo formato", "g", 62, COR)], 1390, 515, "center")
    E.frase(c, t, C["s23"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s23.b"], [("Triângulos", "g", 110, COR)], XE, 440)
    E.frase(c, t, C["s23.b"] + 0.3, [("semelhantes", "g", 110, COR)], XE, 570)
    E.frase(c, t, C["s23.c"], ps("e o lado que falta", "i", 70), XE, 700, passo=0.12)
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 690, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1580, p), lerp(900, 715, p), ep(t, C["s23.d"] + 0.2, 0.4))
    E.frase(c, t, C["s23.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, tales=b_tales, bissetriz=b_bissetriz, porque=b_porque, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
