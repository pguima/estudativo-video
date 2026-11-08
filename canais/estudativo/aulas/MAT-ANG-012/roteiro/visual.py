"""Visual — Estudativo · MAT-ANG-012: triângulos semelhantes, critérios e razão de semelhança (4, 5, 6 e 12, x: x = 15).
Linguagem da geometria plana (MAT-ANG-001 a 020): lados em tinta; ângulos iguais com a mesma marca e a mesma cor
(um arco em COR, índigo; dois arcos em AMBAR; o terceiro, quando entra, em TINTA2); ângulo reto = quadradinho; medidas na
grotesca; erro em vermelho, certo em verde; resposta na esfera; atalho no palco escuro.
Lado correspondente = lado de frente para o mesmo ângulo: o lado ganha a cor do ângulo da frente (o 4 e o 12 em COR, o 5 e o x
em AMBAR), e é essa cor que guia a montagem da proporção.
Figuras em escala: 4-5-6 e o grande 12-15-18 girado (12 embaixo, de frente para o ângulo de um arco); na questão,
30-60-90 com BC = 4, AC = 8 e PQR com QR = 6, PQ = 12.
Peças locais (as da MAT-ANG-009/010/011): cunha_m(), faixa_v(), marca() (um ou dois arcos), rotulo(), txt_lado(), triang(),
coloca() (leva o triângulo da conta para a tela), frac2(), prop(), cruz(), tesoura().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-012_triangulos_semelhantes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("semelhanca", "ordem", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
AMB_C = "#FFB238"
XT = 1520
assert 4 * 3 == 12 and 5 * 3 == 15 and 6 * 3 == 18
assert 12 * 5 == 4 * 15 == 60 and 60 // 4 == 15 and 12 // 4 == 3
assert 12 * 5 == 6 * 10 and 60 // 6 == 10
assert 180 - 30 - 90 == 60 and 180 - 30 - 60 == 90 and 6 * 8 == 4 * 12 == 48 and 48 // 4 == 12 and 8 == 2 * 4 and 12 == 2 * 6


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


def rotulo(c, V, g, r, s, cor, size, a):
    if a <= 0 or not s:
        return
    w = E.formula(None, s, 0, 0, size, "b", a=0)
    ux, uy = math.cos(math.radians(g)), -math.sin(math.radians(g))
    k = r + 16 + abs(ux) * w / 2 + abs(uy) * size * 0.4
    E.formula(c, s, V[0] + ux * k, V[1] + uy * k + size * 0.36, size, "b", cor, a, "center")


def marca(c, t, t0, V, P, Q, n=1, cor=None, r=62, rot=None, size=48, a=1.0, alfa=0.22):
    """ângulo PVQ marcado com n arcos (n = 0: só a cunha) e, se rot, a medida por fora"""
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    g1, g2 = faixa_v(V, P, Q)
    q = ease_io(prog(t, t0, 0.5))
    cunha_m(c, V, g1, g1 + (g2 - g1) * q, r, cor, a, alfa=alfa, borda=5)
    if n >= 2:
        ret = skia.Rect.MakeXYWH(V[0] - r + 14, V[1] - r + 14, 2 * r - 28, 2 * r - 28)
        c.drawArc(ret, -g1, -(g2 - g1) * q, False, M.paint(cor, a, stroke=5, cap_round=True))
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda k: rotulo(c, V, (g1 + g2) / 2, r, rot, cor, size, k * a))


def reto(c, t, t0, V, P, Q, cor=TINTA2, r=40, a=1.0):
    if t < t0 or a <= 0:
        return
    k = ep(t, t0, 0.4) * a
    ux, uy = E._uni(*V, *P)
    vx, vy = E._uni(*V, *Q)
    A_ = (V[0] + ux * r, V[1] + uy * r)
    B_ = (V[0] + vx * r, V[1] + vy * r)
    Cq = (V[0] + (ux + vx) * r, V[1] + (uy + vy) * r)
    path = skia.Path(); path.addPoly([V, A_, Cq, B_], True)
    c.drawPath(path, M.paint(cor, 0.2 * k))
    M.line(c, *A_, *Cq, cor, k, 5); M.line(c, *Cq, *B_, cor, k, 5)


def txt_lado(c, P, Q, s, G, size=56, cor=None, a=1.0, gap=22):
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


def centroide(T):
    return sum(p[0] for p in T) / 3, sum(p[1] for p in T) / 3


def triang(c, t, t0, T, nomes=None, tinta=TINTA, preenche=0.05, d=0.9, a=1.0, larg=6):
    if t < t0 or a <= 0:
        return
    if preenche:
        path = skia.Path(); path.addPoly(list(T), True)
        c.drawPath(path, M.paint(E.COR, preenche * ep(t, t0 + d * 0.6, 0.5) * a))
    p = ease_io(prog(t, t0, d))
    for i in range(3):
        P, Q = T[i], T[(i + 1) % 3]
        f = M.clamp(p * 3 - i)
        if f > 0:
            M.line(c, *P, lerp(P[0], Q[0], f), lerp(P[1], Q[1], f), tinta, a, larg)
    if nomes:
        g = centroide(T)
        for i, (V, s) in enumerate(zip(T, nomes)):
            if not s.strip():
                continue
            ux, uy = V[0] - g[0], V[1] - g[1]
            n = math.hypot(ux, uy)
            E.foco(c, t, t0 + 0.3 + 0.15 * i, 0.4, lambda k, V=V, s=s, ux=ux / n, uy=uy / n: centro(c, s, V[0] + ux * 58, V[1] + uy * 58 + 22, 56, "g", tinta, k * a))


def brilho(c, P, Q, cor, k, larg=32):
    if k > 0:
        M.line(c, *P, *Q, cor, 0.28 * k, larg)


def coloca(pts, s, ox, oy):
    """pontos da conta (y para cima) para a tela: escala s, origem (ox, oy)"""
    return tuple((ox + x * s, oy - y * s) for x, y in pts)


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


def prop(c, t, t0, n1, d1, n2, d2, cx, cy, size=100, cores=(COR, COR, AMBAR, AMBAR), t1=None, dx=170, barra=TINTA, igual=TINTA):
    t1 = t0 + 0.6 if t1 is None else t1
    E.foco(c, t, t0, 0.5, lambda a: frac2(c, n1, d1, cx - dx, cy, size, cores[0], cores[1], a, barra))
    E.foco(c, t, t1, 0.5, lambda a: (centro(c, "=", cx, cy + size * 0.36, size, "g", igual, a),
                                     frac2(c, n2, d2, cx + dx, cy, size, cores[2], cores[3], a, barra)))


def cruz(c, t, t0, t1, cx, cy, size=100, dx=170, c1=TINTA2, c2=TINTA2, wa=60, wb=60):
    xa, xb = cx - dx, cx + dx
    for tt, (P, Q), cor in ((t0, ((xa + wa, cy - size * 0.7), (xb - wb, cy + size * 0.95)), c1),
                            (t1, ((xa + wa, cy + size * 0.95), (xb - wb, cy - size * 0.7)), c2)):
        p = ease_io(prog(t, tt, 0.6))
        for u0, u1 in ((0.0, 0.36), (0.64, 1.0)):
            if p > u0:
                u = min(p, u1)
                M.line(c, lerp(P[0], Q[0], u0), lerp(P[1], Q[1], u0), lerp(P[0], Q[0], u), lerp(P[1], Q[1], u), cor, 0.85, 7)


# ---------------- figuras ----------------
# pequeno 4-5-6 (6 embaixo): L tem um arco (de frente para o 4), R tem dois arcos (de frente para o 5), T sem marca
_xt = (25 - 16 + 36) / 12
PEQ = ((0, 0), (6, 0), (_xt, math.sqrt(25 - _xt ** 2)))                     # L, R, T
# grande 12-15-18 girado (12 embaixo): T' tem um arco (de frente para o 12), L' dois arcos (de frente para o x = 15), R' sem marca
_xg = (324 - 225 + 144) / 24
GRA = ((0, 0), (12, 0), (_xg, math.sqrt(324 - _xg ** 2)))                    # L', R', T'
assert abs(math.dist(PEQ[0], PEQ[2]) - 5) < 1e-9 and abs(math.dist(PEQ[1], PEQ[2]) - 4) < 1e-9
assert abs(math.dist(GRA[0], GRA[2]) - 18) < 1e-9 and abs(math.dist(GRA[1], GRA[2]) - 15) < 1e-9
SP = coloca(PEQ, 42, 110, 880)
SG = coloca(GRA, 42, 560, 880)


def fig_par(c, t, t0, tg=None, marcas=None, labs_p=True, labs_g=True, a=1.0):
    """o pequeno (4, 5, 6) e o grande girado (12, x). marcas = instante das marcas de ângulo"""
    L, R, T = SP
    L2, R2, T2 = SG
    tg = t0 + 0.6 if tg is None else tg
    triang(c, t, t0, SP, a=a)
    triang(c, t, tg, SG, a=a)
    tm = t0 + 0.8 if marcas is None else marcas
    marca(c, t, tm, L, R, T, 1, COR, 56, a=a)
    marca(c, t, tm + 0.2, R, T, L, 2, AMBAR, 56, a=a)
    if t >= tg:
        marca(c, t, max(tm, tg + 0.6), T2, L2, R2, 1, COR, 70, a=a)
        marca(c, t, max(tm, tg + 0.6) + 0.2, L2, R2, T2, 2, AMBAR, 70, a=a)
    G1, G2 = centroide(SP), centroide(SG)
    if labs_p:
        tl = labs_p if not isinstance(labs_p, bool) else t0 + 0.5
        lab(c, t, tl, R, T, "4", G1, COR, 52, 16)
        lab(c, t, tl + 0.2, L, T, "5", G1, AMBAR, 52, 16)
        lab(c, t, tl + 0.4, L, R, "6", G1, TINTA, 52, 16)
    if labs_g:
        tl = labs_g if not isinstance(labs_g, bool) else tg + 0.5
        lab(c, t, tl, L2, R2, "12", G2, COR, 60)
        lab(c, t, tl + 0.3, R2, T2, "x", G2, AMBAR, 64)


# ---------------- gancho ----------------
def foto(c, cx, cy, w, h, a=1.0):
    """foto com borda branca e sombra; o triângulo dentro é desenhado à parte"""
    if a <= 0:
        return
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.18 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + 8, cy - h / 2 + 12, w, h), 14, 14), s)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 14, 14), M.paint("#FFFFFF", a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + 16, cy - h / 2 + 16, w - 32, h - 32), 8, 8), M.paint("#EAE8F6", a))


def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        # foto pequena e a ampliação, que cresce a partir dela
        E.foco(c, t, ka, 0.5, lambda a: foto(c, 300, 560, 300, 220, a))
        Tp = coloca(PEQ, 30, 300 - 90, 560 + 50)
        E.foco(c, t, ka + 0.3, 0.5, lambda a: triang(c, t, ka + 0.3, Tp, larg=5, a=a))
        if t >= kb:
            q = ease_io(prog(t, kb, 1.0))
            k = lerp(1.0, 2.2, q)
            cx, cy = lerp(300, 920, q), lerp(560, 560, q)
            foto(c, cx, cy, 300 * k, 220 * k)
            Tg = coloca(PEQ, 30 * k, cx - 90 * k, cy + 50 * k)
            triang(c, t, kb - 1, Tg, larg=6)
            marca(c, t, kc, Tg[0], Tg[1], Tg[2], 1, COR, 60)
            marca(c, t, kc + 0.4, Tg[1], Tg[2], Tg[0], 2, AMBAR, 60)
        marca(c, t, kc, Tp[0], Tp[1], Tp[2], 1, COR, 34)
        marca(c, t, kc + 0.4, Tp[1], Tp[2], Tp[0], 2, AMBAR, 34)
        E.frase(c, t, ka + 0.3, ps("ampliar", "i", 70) + [("a foto", "g", 76)], 1560, 300, "center", 0.12)
        E.frase(c, t, kb + 0.2, ps("maior, mas", "i", 64), 1560, 440, "center", 0.12)
        E.frase(c, t, kb + 0.8, [("nada entorta", "g", 80, COR)], 1560, 540, "center")
        E.frase(c, t, kc, ps("confira", "i", 64) + [("2 ângulos", "g", 76, COR)], 1560, 760, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("triângulos", "g", 104, COR)], XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.55), [("semelhantes", "g", 104, COR)], XE, 580, passo=0.14)
        E.frase(c, t, tb, ps("e o", "i", 84) + [("lado que falta", "g", 84)], XE, 740, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 820
    itens = (("s03.b", "congruência", "mesmo formato e tamanho"), ("s03.c", "proporção, como em Tales", "3/6 = 4/x → x = 8"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
    py = lerp(420, 700, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 920, "left", 0.12)


# ---------------- semelhança e razão ----------------
def b_semelhanca(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    t0 = C["s04"] + 0.2
    Tp = coloca(PEQ, 30, 140, 800)
    q = ease_io(prog(t, a4 + 0.6, 1.2))
    k = lerp(1, 3, q)
    Tg = coloca(PEQ, 30 * k, lerp(140, 440, q), 800)
    triang(c, t, t0, Tp, larg=5)
    if t >= a4 + 0.6:
        triang(c, t, a4 - 1, Tg)
    # ângulos iguais
    marca(c, t, b4, Tp[0], Tp[1], Tp[2], 1, COR, 34)
    marca(c, t, b4 + 0.2, Tp[1], Tp[2], Tp[0], 2, AMBAR, 34)
    marca(c, t, b4 + 0.4, Tp[2], Tp[0], Tp[1], 0, TINTA2, 30)
    marca(c, t, b4, Tg[0], Tg[1], Tg[2], 1, COR, 70)
    marca(c, t, b4 + 0.2, Tg[1], Tg[2], Tg[0], 2, AMBAR, 70)
    marca(c, t, b4 + 0.4, Tg[2], Tg[0], Tg[1], 0, TINTA2, 60)
    Gp, Gg = centroide(Tp), centroide(Tg)
    for i, (s, s3, tt, tt3) in enumerate((("4", "12", b5, c5), ("5", "15", b5 + 0.6, c5 + 0.5), ("6", "18", b5 + 1.2, c5 + 1.0))):
        P, Q = ((Tp[1], Tp[2]), (Tp[0], Tp[2]), (Tp[0], Tp[1]))[i]
        P3, Q3 = ((Tg[1], Tg[2]), (Tg[0], Tg[2]), (Tg[0], Tg[1]))[i]
        cor = (COR, AMBAR, TINTA)[i]
        lab(c, t, tt, P, Q, s, Gp, cor, 46, 12)
        lab(c, t, tt3, P3, Q3, s3, Gg, cor, 64)

    def quatro():
        E.frase(c, t, C["s04"] + 0.2, [("semelhantes", "g", 84, COR)], XT, 250, "center")
        E.frase(c, t, a4 + 0.6, ps("mesmo formato,", "i", 60), XT, 350, "center", 0.12)
        E.frase(c, t, a4 + 1.6, ps("outro tamanho", "i", 60), XT, 430, "center", 0.12)
        E.frase(c, t, b4, [("ângulos", "g", 70), ("iguais", "i", 64)], XT, 580, "center", 0.12)
        E.frase(c, t, c4, [("lados", "g", 70), ("proporcionais", "i", 64)], XT, 690, "center", 0.12)
        E.frase(c, t, c4 + 1.4, ps("todos vezes o mesmo número", "i", 50, TINTA2), XT, 780, "center", 0.1)
    E.saida(c, t, C["s05"] - 0.1, quatro)
    if t >= C["s05"]:
        E.frase(c, t, a5, ps("razão de", "i", 70), XT, 260, "center", 0.12)
        E.frase(c, t, a5 + 0.6, [("semelhança", "g", 90, COR)], XT, 370, "center")
        E.frase(c, t, b5, [("4, 5, 6", "g", 76)], XT, 530, "center")
        E.frase(c, t, lerp(b5, c5, 0.6), [("× 3", "g", 70, COR)], XT, 620, "center")
        E.frase(c, t, c5, [("12, 15, 18", "g", 76)], XT, 730, "center")
        bola_txt(c, t, d5, "3", XT, 890, 80, 100)


# ---------------- critérios ----------------
def b_criterios(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")

    def seis():
        Tp = coloca(PEQ, 30, 140, 800)
        Tg = coloca(PEQ, 90, 440, 800)
        triang(c, t, C["s06"] - 0.5, Tp, larg=5)
        triang(c, t, C["s06"] - 0.5, Tg)
        for T, r in ((Tp, 34), (Tg, 70)):
            marca(c, t, a6, T[0], T[1], T[2], 1, COR, r)
            marca(c, t, a6 + 0.6, T[1], T[2], T[0], 2, AMBAR, r)
            marca(c, t, b6, T[2], T[0], T[1], 0, TINTA2, r * 0.9, alfa=0.35)
        E.frase(c, t, a6, ps("basta conferir", "i", 64), XT, 260, "center", 0.12)
        E.frase(c, t, a6 + 0.8, [("2 ângulos", "g", 90, COR)], XT, 370, "center")
        E.frase(c, t, b6, ps("o terceiro:", "i", 60), XT, 520, "center", 0.12)
        fcen(c, t, b6 + 0.6, "180 − os outros dois", XT, 610, 58, TINTA2)
        E.foco(c, t, c6, 0.5, lambda a: E.pilula(c, "2 ângulos valem por 3", XT, 780, 58, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s07"] - 0.1, seis)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"] + 0.2, ps("também garantem", "i", 70), W / 2, 200, "center", 0.12)
    linhas = ((a7, "3 lados", "na mesma razão", TINTA), (b7, "2 lados na razão", "e o ângulo entre eles igual", TINTA),
              (d7, "2 ângulos iguais", "o que mais cai na prova", COR))
    for i, (tt, l1, l2, cor) in enumerate(linhas):
        y = 380 + i * 210
        E.foco(c, t, tt, 0.5, lambda a, i=i, y=y, cor=cor: (E.bola(c, 300, y - 30, 52, cor, a), centro(c, str(i + 1), 300, y - 8, 60, "g", BR, a)))
        E.frase(c, t, tt + 0.1, [(l1, "g", 70, cor)], 390, y - 10)
        E.frase(c, t, tt + 0.5, [(l2, "i", 56, TINTA2)], 390, y + 60)
    E.foco(c, t, c7, 0.5, lambda a: E.pilula(c, "como na congruência", 1500, 520, 52, "i", fundo=TINTA, a=a))
    E.foco(c, t, c7 + 0.8, 0.5, lambda a: centro(c, "iguais → proporcionais", 1500, 620, 50, "b", TINTA2, a))


# ---------------- a ordem ----------------
def b_ordem(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9 = (C[f"s09.{k}"] for k in "abc")
    a10, b10, c10, d10, e10 = (C[f"s10.{k}"] for k in "abcde")
    L, R, T = SP
    L2, R2, T2 = SG
    fig_par(c, t, c8, tg=d8, marcas=c8 + 0.6, labs_p=c8 + 0.5, labs_g=d8 + 0.6)
    # pares correspondentes acendem na fala
    k1 = ep(t, a9, 0.4) * (1 - ep(t, c9, 0.4))
    brilho(c, L2, R2, COR, k1)
    k1b = ep(t, b9, 0.4) * (1 - ep(t, c9, 0.4))
    brilho(c, R, T, COR, k1b, 26)
    k2 = ep(t, c9, 0.4) * (1 - ep(t, a10, 0.4))
    brilho(c, R2, T2, AMBAR, k2)
    brilho(c, L, T, AMBAR, k2, 26)
    if t >= b9:
        k = ep(t, b9 + 0.3, 0.4) * (1 - ep(t, a10, 0.4))
        if k > 0:
            M.line(c, *meio(R, T), *meio(L2, R2), COR, 0.6 * k, 4, dash=[10, 10])

    def oito():
        E.frase(c, t, a8, ps("o mais importante:", "i", 60), XT, 250, "center", 0.12)
        E.frase(c, t, a8 + 0.8, [("a ordem", "g", 96, COR)], XT, 360, "center")
        E.frase(c, t, b8, ps("lado correspondente:", "i", 56), XT, 520, "center", 0.1)
        E.frase(c, t, b8 + 1.0, [("de frente para", "g", 64)], XT, 610, "center")
        E.frase(c, t, b8 + 1.6, [("o mesmo ângulo", "g", 64, COR)], XT, 700, "center")
        E.frase(c, t, d8, [("girado", "g", 70, AMBAR)], XT, 860, "center")
    E.saida(c, t, C["s09"] - 0.1, oito)
    if C["s09"] - 0.1 <= t < C["s10"]:
        def nove():
            E.frase(c, t, a9, [("12", "g", 80, COR)] + ps("de frente para", "i", 56) + [("1 arco", "g", 60, COR)], XT, 300, "center", 0.12)
            E.frase(c, t, b9, ps("no pequeno:", "i", 56) + [("4", "g", 80, COR)], XT, 420, "center", 0.12)
            E.frase(c, t, c9, [("x", "g", 80, AMBAR)] + ps("de frente para", "i", 56) + [("2 arcos", "g", 60, AMBAR)], XT, 600, "center", 0.12)
            E.frase(c, t, c9 + 1.0, ps("no pequeno:", "i", 56) + [("5", "g", 80, AMBAR)], XT, 720, "center", 0.12)
        E.saida(c, t, C["s10"] - 0.1, nove)
    if t >= C["s10"]:
        E.frase(c, t, a10, ps("grande sobre pequeno", "i", 60), XT, 210, "center", 0.12)
        prop(c, t, b10, "12", "4", "x", "5", XT, 360, 104, t1=b10 + 1.3)
        if t >= c10:
            cruz(c, t, c10, c10 + 0.5, XT, 360, 104, wa=70, wb=60)
        fcen(c, t, c10, "4x = 12 · 5 = 60", XT, 640, 72)
        fcen(c, t, d10, "x = 60 ÷ 4", XT - 100, 780, 72)
        bola_txt(c, t, d10 + 0.6, "15", XT + 200, 755, 72, 80, CERTO)
        E.frase(c, t, e10, ps("razão:", "i", 56) + [("12 ÷ 4 = 3", "g", 64, COR)], XT, 920, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12 = C["s12.a"], C["s12.b"]
    L, R, T = SP
    L2, R2, T2 = SG
    t0 = C["s11"]
    fig_par(c, t, t0 - 0.6, tg=t0 - 0.6, marcas=t0 - 0.6, labs_p=t0 - 0.6, labs_g=t0 - 0.6)
    k = ep(t, a11 + 1.6, 0.4) * (1 - ep(t, a12, 0.4))
    brilho(c, L2, R2, ERRADO, k)
    brilho(c, L, R, ERRADO, k, 26)
    if t >= a12:
        marca(c, t, a12, T, L, R, 0, TINTA2, 46, alfa=0.45)
        brilho(c, L, R, TINTA2, ep(t, a12, 0.4), 26)
        brilho(c, L2, R2, COR, ep(t, a12 + 0.8, 0.4))
        brilho(c, R, T, COR, ep(t, a12 + 0.8, 0.4), 26)
    E.frase(c, t, t0 + 0.2, [("cuidado", "g", 84, ERRADO)], XT, 170, "center")

    def onze():
        E.frase(c, t, a11, ps("ligar pela", "i", 60) + [("posição", "g", 68, ERRADO)], XT, 280, "center", 0.12)
        E.frase(c, t, a11 + 1.6, ps("os dois de baixo:", "i", 54) + [("12 e 6", "g", 60, ERRADO)], XT, 370, "center", 0.12)
        prop(c, t, b11, "12", "6", "x", "5", XT, 520, 96, cores=(ERRADO, ERRADO, TINTA, TINTA), t1=b11 + 1.3)
        fcen(c, t, c11, "x = 10", XT - 60, 800, 84, ERRADO)
        E.foco(c, t, c11 + 0.4, 0.4, lambda a: E.selo(c, XT + 160, 772, 52, False, a))
    E.saida(c, t, C["s12"] - 0.1, onze)
    if t >= C["s12"]:
        E.frase(c, t, a12, ps("o 6 está de frente para o", "i", 54), XT, 330, "center", 0.1)
        E.frase(c, t, a12 + 1.2, [("ângulo sem marca", "g", 66, TINTA2)], XT, 420, "center")
        E.frase(c, t, b12, ps("girou ou virou:", "i", 56), XT, 600, "center", 0.12)
        E.foco(c, t, b12 + 0.8, 0.5, lambda a: E.pilula(c, "manda o ângulo da frente", XT, 720, 52, "g", a=a, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
def tesoura(c, cx, cy, ab, L=430, a=1.0, cor=BR):
    """duas lâminas presas no pino (cx, cy), abertas de ab graus para a direita; devolve as pontas"""
    pts = []
    for s in (1, -1):
        g = math.radians(s * ab / 2)
        P = (cx + L * math.cos(g), cy - L * math.sin(g))
        Q = (cx - 150 * math.cos(g), cy + 150 * math.sin(g))
        M.line(c, *Q, *P, cor, a, 12)
        c.drawCircle(Q[0] - 40 * math.cos(g), Q[1] + 40 * math.sin(g), 42, M.paint(cor, a, stroke=10))
        pts.append(P)
    c.drawCircle(cx, cy, 13, M.paint(AMB_C, a))
    return pts


def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14, d14, e14 = (C[f"s14.{k}"] for k in "abcde")
    a15, b15, c15, d15 = (C[f"s15.{k}"] for k in "abcd")
    LIL = CLARO

    def treze():
        E.frase(c, t, a13, [("maior", "g", 80, BR)] + ps("com maior,", "i", 64, CLARO), W / 2, 200, "center", 0.12)
        E.frase(c, t, a13 + 1.2, [("menor", "g", 80, BR)] + ps("com menor", "i", 64, CLARO), W / 2, 300, "center", 0.12)
        # o maior lado de frente para o maior ângulo
        T = coloca(PEQ, 70, 200, 880)
        triang(c, t, b13, T, tinta=BR, preenche=0)
        marca(c, t, b13 + 0.6, T[2], T[0], T[1], 0, AMB_C, 70, alfa=0.4)
        brilho(c, T[0], T[1], AMB_C, ep(t, b13 + 0.9, 0.4))
        E.frase(c, t, b13 + 1.2, [("maior ângulo", "g", 52, AMB_C)], 410, 470, "center")
        E.frase(c, t, b13 + 1.5, [("maior lado", "g", 52, AMB_C)], 410, 960, "center")
        # a tesoura
        if t >= c13:
            ab = lerp(14, 70, ease_io(prog(t, c13 + 0.4, 1.6)))
            k = ep(t, c13, 0.4)
            P, Q = tesoura(c, 1150, 640, ab, a=k)
            M.line(c, *P, *Q, AMB_C, k, 6, dash=[12, 10])
            E.foco(c, t, c13 + 1.2, 0.4, lambda f: E.escreve(c, "pontas longe", P[0] + 30, (P[1] + Q[1]) / 2 + 20, 52, "g", AMB_C, f))
    E.saida(c, t, C["s14"] - 0.1, treze)
    if C["s14"] - 0.1 <= t < C["s15"]:
        def quatorze():
            E.frase(c, t, a14, ps("a questão dá", "i", 64, CLARO) + [("todos os lados", "g", 72, BR)], W / 2, 200, "center", 0.12)
            xs = (700, 960, 1220)
            for i, (s, tt) in enumerate((("4", b14), ("5", b14 + 0.5), ("6", b14 + 1.0))):
                E.foco(c, t, tt, 0.4, lambda a, i=i, s=s: centro(c, s, xs[i], 400, 96, "g", (LIL, AMB_C, BR)[i], a))
            # o segundo triângulo chega fora de ordem e se arruma
            orig = {"15": 0, "18": 1, "12": 2}
            dest = {"12": 0, "15": 1, "18": 2}
            q = ease_io(prog(t, d14, 1.2))
            for s in ("15", "18", "12"):
                x = lerp(xs[orig[s]], xs[dest[s]], q)
                y = 640 + math.sin(math.pi * q) * (60 if s == "12" else -40)
                cor = (LIL, AMB_C, BR)[dest[s]] if q > 0.5 else BR
                E.foco(c, t, c14 + 0.4 * orig[s], 0.4, lambda a, s=s, x=x, y=y, cor=cor: centro(c, s, x, y, 96, "g", cor, a))
            for i in range(3):
                k = ep(t, d14 + 1.2 + 0.3 * i, 0.4)
                if k > 0:
                    M.line(c, xs[i], 440, xs[i], 560, (LIL, AMB_C, BR)[i], k, 5, dash=[10, 8])
            E.foco(c, t, e14 - 0.8, 0.4, lambda a: (centro(c, "× 3", 1420, 530, 70, "g", AMB_C, a)))
            E.foco(c, t, e14, 0.5, lambda a: E.pilula(c, "semelhantes", W / 2, 860, 70, "g", fundo=CERTO, a=a))
        E.saida(c, t, C["s15"] - 0.1, quatorze)
    if t < C["s15"]:
        return
    E.frase(c, t, a15, ps("ângulos iguais:", "i", 64, CLARO) + [("lados na mesma fila", "g", 70, BR)], W / 2, 220, "center", 0.12)
    for i, (s, cor) in enumerate((("menor", LIL), ("médio", AMB_C), ("maior", BR))):
        E.foco(c, t, a15 + 1.2 + 0.3 * i, 0.4, lambda a, i=i, s=s, cor=cor: E.pilula(c, s, 640 + 320 * i, 380, 52, "g", fundo=cor, cor="#0B0B14", a=a))
    E.frase(c, t, b15, ps("falta um lado?", "i", 64, CLARO), W / 2 - 360, 600, "center", 0.12)
    E.frase(c, t, c15, ps("lados iguais?", "i", 64, CLARO), W / 2 + 360, 600, "center", 0.12)
    E.foco(c, t, d15, 0.5, lambda a: E.pilula(c, "siga os ângulos", W / 2, 800, 72, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
S30 = math.sqrt(3)
# ABC: B reto, A = 30°, BC = 4 (de pé), AB = 4√3 (deitado), AC = 8
QA_, QB_, QC_ = coloca(((0, 0), (4 * S30, 0), (4 * S30, 4)), 48, 110, 880)
# PQR: R reto, P = 30°, Q = 60°, PQ = 12 deitado embaixo, QR = 6, PR = 6√3
QP_, QQ_ = coloca(((0, 0), (12, 0)), 44, 640, 880)
QR_ = coloca(((6 * S30 * math.cos(math.radians(30)), 6 * S30 * math.sin(math.radians(30))),), 44, 640, 880)[0]
assert abs(math.dist(QQ_, QR_) / 44 - 6) < 1e-6 and abs(math.dist(QA_, QC_) / 48 - 8) < 1e-6


def fig_q(c, t, t0, td=None, tr=None, a=1.0, tc=None):
    """os dois triângulos da questão com os dados; td = dados, tr = ângulos que faltam, tc = medida que falta"""
    td = t0 + 0.6 if td is None else td
    triang(c, t, t0, (QA_, QB_, QC_), "ABC", a=a)
    triang(c, t, t0 + 0.4, (QP_, QQ_, QR_), "PQR", a=a)
    GA, GP = centroide((QA_, QB_, QC_)), centroide((QP_, QQ_, QR_))
    marca(c, t, td, QA_, QB_, QC_, 1, COR, 70, "30°", 44, a=a)
    reto(c, t, td + 0.2, QB_, QA_, QC_, TINTA2, 36, a=a)
    lab(c, t, td + 0.4, QB_, QC_, "4", GA, TINTA, 52, 16)
    lab(c, t, td + 0.6, QA_, QC_, "8", GA, TINTA, 52, 16)
    marca(c, t, td + 1.0, QP_, QQ_, QR_, 1, COR, 80, "30°", 44, a=a)
    marca(c, t, td + 1.2, QQ_, QR_, QP_, 2, AMBAR, 56, "60°", 44, a=a)
    lab(c, t, td + 1.4, QQ_, QR_, "6", GP, TINTA, 52, 16)
    if tr is not None:
        marca(c, t, tr, QC_, QA_, QB_, 2, AMBAR, 44, "60°", 40, a=a)
        reto(c, t, tr + 1.0, QR_, QP_, QQ_, TINTA2, 34, a=a)


def b_questao(c, t, C, b):
    a16, a17, b17, c17 = C["s16.a"], C["s17.a"], C["s17.b"], C["s17.c"]
    rel = C["s18.a"]
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XT + 60, 170, "center", 0.12)
    triang(c, t, a16, (QA_, QB_, QC_), "ABC")
    GA, GP = centroide((QA_, QB_, QC_)), centroide((QP_, QQ_, QR_))
    marca(c, t, a16 + 1.0, QA_, QB_, QC_, 1, COR, 70, "30°", 44)
    reto(c, t, a16 + 2.6, QB_, QA_, QC_, TINTA2, 36)
    lab(c, t, a16 + 4.0, QB_, QC_, "4", GA, TINTA, 52, 16)
    lab(c, t, a16 + 5.4, QA_, QC_, "8", GA, TINTA, 52, 16)
    if t >= a17:
        triang(c, t, a17, (QP_, QQ_, QR_), "PQR")
        marca(c, t, a17 + 1.0, QP_, QQ_, QR_, 1, COR, 80, "30°", 44)
        marca(c, t, a17 + 2.6, QQ_, QR_, QP_, 2, AMBAR, 56, "60°", 44)
        lab(c, t, a17 + 4.4, QQ_, QR_, "6", GP, TINTA, 52, 16)
        E.foco(c, t, c17, 0.4, lambda a: txt_lado(c, QP_, QQ_, "?", GP, 64, ERRADO, a, 18))

    def lado():
        E.frase(c, t, a16, [("ABC:", "g", 58)] + ps("ângulos 30° e 90°", "i", 54), XT + 60, 360, "center", 0.12)
        E.frase(c, t, a17, [("PQR:", "g", 58)] + ps("ângulos 30° e 60°", "i", 54), XT + 60, 460, "center", 0.12)
    E.saida(c, t, rel - 0.5, lado)
    E.frase(c, t, b17, [("semelhantes?", "g", 66, COR)], XT + 60, 830, "center")
    E.frase(c, t, c17, [("PQ", "g", 66), ("= ?", "g", 66, ERRADO)], XT + 60, 940, "center", 0.12)
    E.relogio(c, t, rel, XT + 60, 420, 150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    a20, b20, c20, d20 = (C[f"s20.{k}"] for k in "abcd")
    a21, b21, c21, d21, e21 = (C[f"s21.{k}"] for k in "abcde")
    t0 = C["s19"]
    X = XT + 60
    fig_q(c, t, t0 - 0.6, t0 - 0.6)
    marca(c, t, a19 + 0.8, QC_, QA_, QB_, 2, AMBAR, 44, "60°", 40)
    reto(c, t, b19 + 0.8, QR_, QP_, QQ_, TINTA2, 34)
    GP = centroide((QP_, QQ_, QR_))
    # pares de frente para o mesmo ângulo
    brilho(c, QB_, QC_, COR, ep(t, a20, 0.4))
    brilho(c, QQ_, QR_, COR, ep(t, b20, 0.4))
    brilho(c, QA_, QC_, TINTA2, ep(t, c20, 0.4))
    brilho(c, QP_, QQ_, TINTA2, ep(t, d20, 0.4))
    E.saida(c, t, c21, lambda: E.foco(c, t, t0 - 0.4, 0.4, lambda a: txt_lado(c, QP_, QQ_, "x", GP, 64, TINTA2, a, 18)))
    E.foco(c, t, c21, 0.4, lambda a: txt_lado(c, QP_, QQ_, "12", GP, 64, CERTO, a, 18))

    def dezenove():
        E.frase(c, t, a19, [("ângulo C:", "i", 56)], X, 220, "center")
        fcen(c, t, a19 + 0.4, "180 − 30 − 90 = 60°", X, 310, 54, AMBAR)
        E.frase(c, t, b19, [("ângulo R:", "i", 56)], X, 430, "center")
        fcen(c, t, b19 + 0.4, "180 − 30 − 60 = 90°", X, 520, 54, TINTA2)
        E.foco(c, t, c19, 0.5, lambda a: E.pilula(c, "semelhantes", X, 680, 64, "g", fundo=CERTO, a=a))
        E.frase(c, t, c19 + 0.6, ps("por dois ângulos", "i", 52), X, 800, "center", 0.1)
    E.saida(c, t, C["s20"] - 0.1, dezenove)
    if C["s20"] - 0.1 <= t < C["s21"]:
        def vinte():
            E.frase(c, t, a20, [("BC = 4", "g", 62, COR)] + ps("de frente p/ 30°", "i", 52), X, 260, "center", 0.12)
            E.frase(c, t, b20, [("QR = 6", "g", 62, COR)] + ps("de frente p/ 30°", "i", 52), X, 360, "center", 0.12)
            E.frase(c, t, c20, [("AC = 8", "g", 62, TINTA2)] + ps("de frente p/ 90°", "i", 52), X, 520, "center", 0.12)
            E.frase(c, t, d20, [("PQ = x", "g", 62, TINTA2)] + ps("de frente p/ 90°", "i", 52), X, 620, "center", 0.12)
        E.saida(c, t, C["s21"] - 0.1, vinte)
    if t < C["s21"]:
        return
    prop(c, t, a21, "6", "4", "x", "8", X, 300, 96, cores=(COR, COR, TINTA2, TINTA2), t1=a21 + 1.3)
    if t >= b21:
        cruz(c, t, b21, b21 + 0.5, X, 300, 96, wa=55, wb=55)
    fcen(c, t, b21, "4x = 6 · 8 = 48", X, 560, 68)
    fcen(c, t, c21, "x = 48 ÷ 4", X - 130, 690, 66)
    bola_txt(c, t, c21 + 0.6, "12 cm", X + 160, 665, 76, 50, CERTO)
    E.frase(c, t, d21, ps("pelo fator:", "i", 54) + [("8 = 2 · 4", "g", 60, AMBAR)], X, 850, "center", 0.12)
    fcen(c, t, d21 + 2.0, "PQ = 2 · 6 = 12", X, 960, 64, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s22.a", "2 ângulos iguais garantem a semelhança"), ("s22.b", "lado correspondente: de frente para o mesmo ângulo"))
        for i, (k, s) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 30, 56, a=a),
                                                         centro(c, str(i + 1), 200, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 58)], 300, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"] + 0.2, ps("próxima aula", "i", 84), XE, 280)
    E.frase(c, t, C["s23.a"], ps("a altura do prédio", "i", 76), XE, 410, passo=0.12)
    E.frase(c, t, C["s23.a"] + 1.0, [("pela sombra", "g", 110, COR)], XE, 540)
    E.frase(c, t, C["s23.b"], ps("e triângulos", "i", 70) + [("encaixados", "g", 76)], XE, 680, passo=0.12)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1630, p), lerp(720, 425, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, semelhanca=b_semelhanca, criterios=b_criterios, ordem=b_ordem, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
