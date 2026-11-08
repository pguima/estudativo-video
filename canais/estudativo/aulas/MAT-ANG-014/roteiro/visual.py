"""Visual — Estudativo · MAT-ANG-014: praticando Tales e semelhança (cinco questões).
Aula de prática no molde da MAT-ANG-009: selo de progresso "questão n de 5", figura à esquerda, pergunta embaixo à direita e
relógio de pausa; na resposta, a mesma figura ganha as medidas e a conta aparece na coluna da direita.
Linguagem da geometria plana (MAT-ANG-001 a 020) e das aulas de Tales e semelhança (MAT-ANG-010 a 013): retas e lados em tinta;
pedaços e lados que se correspondem com a mesma cor (o de cima / a altura em COR, índigo; o de baixo / a sombra em AMBAR);
ângulos iguais com a mesma marca (um arco em COR, dois arcos em AMBAR, ângulo comum ou oposto pelo vértice em TINTA2);
setinhas de paralela; raio de sol tracejado; medidas na grotesca; erro em vermelho, certo em verde; resposta na esfera.
Figuras em escala: Q1 com as paralelas a distâncias 2 : 3 (4 e 6, 6 e 9); Q2 com o triângulo 10, 15, 20 e D a 8 de B;
Q3 com AM = 6, MB = 3, MN = 8, BC = 12; Q4 com a gravata AM = 4, MC = 6, AB = 6, CD = 9; Q5 com vara e torre no mesmo formato.
Peças locais (as da MAT-ANG-009/010/011/012/013): progresso() e pergunta() (da MAT-ANG-009, onde se chamava marca()), num_bola(),
marca() (ângulo com um ou dois arcos), reto(), metades(), txt_lado(), lab(), triang(), brilho(), frac2(), prop(), cruz(),
pedaco(), rot(), rot_troca(), seta_par(), sol(), raio(), sombra(), torre().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-014_praticando_tales_e_semelhanca.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "atalho", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
AMB_C = "#FFB238"
XT = 1500
assert 4 * (6 + 3) == 6 * 6 and 4 * 6 + 12 == 6 * 6 and 12 // 2 == 6 and 6 + 3 == 9 and 4 * 3 == 6 * 2 and 6 * 3 == 9 * 2
assert 10 // 5 == 2 and 15 // 5 == 3 and 20 // 5 == 4 and 2 * 4 == 8 and 3 * 4 == 12 and 8 * 15 == 12 * 10
assert 8 * 9 == 6 * 12 == 72 and 72 // 8 == 9 and 9 - 6 == 3
assert 6 * 6 == 4 * 9 == 36 and 36 // 6 == 6
assert 2 * 15 == 1.5 * 20 == 30 and 30 // 2 == 15 and 20 == 10 * 2 and 10 * 1.5 == 15


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



def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)


def progresso(c, t, t0, n):
    """questão n de 5, com cinco pontos de progresso (como na MAT-ANG-009)"""
    s = f"questão {n} de 5"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", a=a)
        for i in range(5):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def pergunta(c, t, linhas, rel, X=XT, y0=860):
    """linhas da pergunta embaixo à direita: [(t0, partes), ...]; relógio de pausa em rel"""
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, y0 + i * 100, "center", 0.12)
    E.relogio(c, t, rel, X, 430, 180)


def metades(c, t, t0, V, P, Q, cor=TINTA2, r=90, a=1.0):
    if t < t0 or a <= 0:
        return
    g1, g2 = faixa_v(V, P, Q)
    gm = (g1 + g2) / 2
    q = ease_io(prog(t, t0, 0.5))
    cunha_m(c, V, g1, g1 + (gm - g1) * q, r, cor, a, alfa=0.22, borda=5)
    cunha_m(c, V, gm, gm + (g2 - gm) * q, r * 0.86, cor, a, alfa=0.22, borda=5)


def pedaco(c, t, t0, P, Q, cor=None, a=1.0, larg=14, d=0.5):
    if a <= 0 or t < t0:
        return
    M.line(c, *P, *Q, cor or E.COR, a, larg, progress=ease_io(prog(t, t0, d)))


def rot(c, t, t0, P, Q, s, lado, cor=None, size=58, gap=30, onde=0.5):
    """medida do pedaço PQ, por fora da reta (lado = 1 ou −1)"""
    if t < t0:
        return
    ux, uy = E._uni(*P, *Q)
    M_ = (lerp(P[0], Q[0], onde), lerp(P[1], Q[1], onde))
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, s, *M_, uy * lado, -ux * lado, gap, size, "g", cor or COR, a))


def rot_troca(c, t, t0, t1, P, Q, s0, s1, lado, cor0, cor1, size=58, gap=30, onde=0.5):
    E.saida(c, t, t1, lambda: rot(c, t, t0, P, Q, s0, lado, cor0, size, gap, onde))
    rot(c, t, t1, P, Q, s1, lado, cor1, size, gap, onde)


def seta_par(c, P, Q, k=0.5, a=1.0, cor=TINTA):
    """setinha de paralela no ponto k da reta PQ"""
    if a <= 0:
        return
    x, y = lerp(P[0], Q[0], k), lerp(P[1], Q[1], k)
    ux, uy = E._uni(*P, *Q)
    for s in (1, -1):
        M.line(c, x - ux * 20 + uy * 16 * s, y - uy * 20 - ux * 16 * s, x, y, cor, a, 5)


def linha(c, t, t0, P, Q, cor=TINTA, larg=6, d=0.6, a=1.0, dash=None):
    if t >= t0 and a > 0:
        M.line(c, *P, *Q, cor, a, larg, dash=dash, progress=ease_io(prog(t, t0, d)))


def ponto(c, t, t0, P, nome, dx=0, dy=60, cor=TINTA, size=56, a=1.0):
    if t < t0 or a <= 0:
        return
    k = ease_back(prog(t, t0, 0.4))
    c.drawCircle(*P, 11 * k, M.paint(cor, a))
    if nome:
        E.foco(c, t, t0 + 0.1, 0.4, lambda f: centro(c, nome, P[0] + dx, P[1] + dy, size, "g", cor, f * a))


# ---------------- Q1: feixe (4 e 6; x e x + 3) ----------------
Q1Y = (240, 420, 690)                     # distâncias 2 : 3
Q1KL = -0.2
Q1KR = math.sqrt(1.5 ** 2 * (1 + Q1KL ** 2) - 1)   # cada pedaço da direita é 1,5 vez o da esquerda (4 → 6)


def q1l(y):
    return 450 + (y - Q1Y[0]) * Q1KL, y


def q1r(y):
    return 560 + (y - Q1Y[0]) * Q1KR, y


Q1L = [q1l(y) for y in Q1Y]
Q1R = [q1r(y) for y in Q1Y]
assert abs(math.dist(Q1R[0], Q1R[1]) / math.dist(Q1L[0], Q1L[1]) - 1.5) < 1e-9


def fig_q1(c, t, t0, tl=None, tr=None, labs=True, a=1.0):
    """o feixe; tl = instante dos pedaços 4 e 6, tr = instante de x e x + 3; labs = (troca, novo1, novo2)"""
    if t < t0:
        return
    for i, y in enumerate(Q1Y):
        M.line(c, 120, y, 1150, y, TINTA, a, 6, progress=ease_io(prog(t, t0 + 0.12 * i, 0.7)))
        seta_par(c, (120, y), (1150, y), 0.12, ep(t, t0 + 0.7, 0.4) * a)
    for f, dt in ((q1l, 0.4), (q1r, 0.6)):
        linha(c, t, t0 + dt, f(Q1Y[0] - 60), f(Q1Y[-1] + 70), TINTA, 6, 0.7, a)
    tl = t0 + 1.0 if tl is None else tl
    tr = t0 + 1.0 if tr is None else tr
    pedaco(c, t, tl, Q1L[0], Q1L[1], COR, a); pedaco(c, t, tl + 0.3, Q1L[1], Q1L[2], AMBAR, a)
    rot(c, t, tl + 0.2, Q1L[0], Q1L[1], "4", -1, COR)
    rot(c, t, tl + 0.5, Q1L[1], Q1L[2], "6", -1, AMBAR)
    pedaco(c, t, tr, Q1R[0], Q1R[1], COR, a); pedaco(c, t, tr + 0.3, Q1R[1], Q1R[2], AMBAR, a)
    if labs is True:
        rot(c, t, tr + 0.2, Q1R[0], Q1R[1], "x", 1, COR)
        rot(c, t, tr + 0.5, Q1R[1], Q1R[2], "x + 3", 1, AMBAR)
    else:
        t1 = labs
        rot_troca(c, t, tr + 0.2, t1, Q1R[0], Q1R[1], "x", "6", 1, COR, CERTO)
        rot_troca(c, t, tr + 0.5, t1 + 0.3, Q1R[1], Q1R[2], "x + 3", "9", 1, AMBAR, CERTO)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]
    E.frase(c, t, a_ + 0.1, ps("5", "g", 240, COR) + ps("questões", "g", 170, COR), XE, 350, passo=0.25)
    E.frase(c, t, a_ + 1.0, ps("de Tales e semelhança", "i", 80), XE, 480, passo=0.12)
    E.frase(c, t, a_ + 2.2, ps("criadas para esta aula", "i", 70, TINTA2), XE, 580, passo=0.12)
    for i, (s, cx, ti) in enumerate((("pause", 440, b_), ("resolva", 960, b_ + 0.9), ("confira", 1480, b_ + 2.0))):
        E.foco(c, t, ti, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 800, 56, 64, p),
                                                           E.escreve(c, s, cx - 110, 825, 92, "g", TINTA, p)))
    E.frase(c, t, lerp(b_, C["s01.end"], 0.6), ps("errar aqui", "i", 62) + [("ensina", "g", 66, COR)], W / 2, 980, "center", 0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.1, ps("você vai usar", "i", 84, COR), XE, 200, passo=0.12)
    itens = (("a", "Tales", "frações na mesma ordem"), ("b", "a bissetriz", "pedaços na razão dos lados"),
             ("c", "semelhança", "dois ângulos iguais"), ("d", "encaixados", "use o lado inteiro"))
    for i, (k, l1, l2) in enumerate(itens):
        x = XE + 40 + (i % 2) * 860
        y = 400 + (i // 2) * 260
        ti = C[f"s02.{k}"]
        E.foco(c, t, ti, 0.5, lambda p, i=i, x=x, y=y: num_bola(c, str(i + 1), x, y - 28, 46, 54, p))
        E.frase(c, t, ti + 0.1, [(l1, "g", 70)], x + 80, y)
        E.frase(c, t, ti + 0.4, [(l2, "i", 56, TINTA2)], x + 80, y + 80)
    E.frase(c, t, C["s02.end"] - 2.6, ps("travou? procure a aula no canal", "i", 60), XE, 980, passo=0.1)


# ---------------- questão 1 ----------------
def b_questao1(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s03.{k}"] for k in "abcd")
    rel = C["s04.a"]
    progresso(c, t, a3, 1)
    fig_q1(c, t, a3 + 0.6, b3, c3)

    def txt():
        E.frase(c, t, a3 + 0.8, [("3", "g", 80, COR)] + ps("paralelas", "i", 64), XT, 330, "center", 0.12)
        E.frase(c, t, a3 + 1.8, [("2", "g", 80, COR)] + ps("transversais", "i", 64), XT, 430, "center", 0.12)
    E.saida(c, t, rel - 0.5, txt)
    pergunta(c, t, [(b3, [("4 e 6", "g", 62)] + ps("numa,", "i", 56) + [("x e x + 3", "g", 62, COR)]),
                    (d3, [("x = ?", "g", 72, ERRADO)])], rel)


def b_resposta1(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    t0 = C["s05"] - 1.0
    fig_q1(c, t, t0, t0, t0, labs=c6)

    def cinco():
        E.frase(c, t, C["s05"] + 0.2, ps("mesma ordem", "i", 60, TINTA2), XT, 180, "center", 0.12)
        prop(c, t, a5, "4", "6", "x", "x + 3", XT, 330, 96, cores=(COR, AMBAR, COR, AMBAR), t1=a5 + 1.6, dx=190)
        if t >= b5:
            cruz(c, t, b5, b5 + 0.5, XT, 330, 96, dx=190, wa=50, wb=110)
        fcen(c, t, b5, "4 · (x + 3) = 6x", XT, 610, 72)
        fcen(c, t, c5, "4x + 12 = 6x", XT, 760, 76)
    E.saida(c, t, C["s06"] - 0.1, cinco)
    if t < C["s06"]:
        return
    fcen(c, t, a6, "12 = 6x − 4x = 2x", XT, 230, 66)
    fcen(c, t, b6, "x = 12 ÷ 2", XT - 120, 390, 70)
    bola_txt(c, t, b6 + 0.6, "6", XT + 180, 365, 72, 90, CERTO)
    E.frase(c, t, c6, ps("pedaços:", "i", 58) + [("6", "g", 70, COR), ("e", "i", 58), ("9", "g", 70, AMBAR)], XT, 540, "center", 0.12)
    fcen(c, t, d6, "f{4}{6} = f{2}{3}", XT - 180, 730, 80)
    fcen(c, t, d6 + 1.2, "f{6}{9} = f{2}{3}", XT + 180, 730, 80)
    E.foco(c, t, d6 + 2.2, 0.5, lambda a: E.selo(c, XT, 920, 64 * ease_back(prog(t, d6 + 2.2, 0.5)), True, a))


# ---------------- Q2: bissetriz (10, 15, 20) ----------------
def tri_lados(ab, ac, bc, B, u):
    x = (ab ** 2 - ac ** 2 + bc ** 2) / (2 * bc)
    h = math.sqrt(ab ** 2 - x ** 2)
    return (B[0] + x * u, B[1] - h * u), B, (B[0] + bc * u, B[1])


Q2A, Q2B, Q2C = tri_lados(10, 15, 20, (130, 860), 45)
Q2D = (Q2B[0] + 8 * 45, Q2B[1])
Q2G = centroide((Q2A, Q2B, Q2C))


def fig_q2(c, t, t0, tl=None, tbc=None, tbis=None, a=1.0):
    triang(c, t, t0, (Q2A, Q2B, Q2C), "ABC", a=a)
    tl = t0 + 0.6 if tl is None else tl
    lab(c, t, tl, Q2A, Q2B, "10", Q2G, COR, 60)
    lab(c, t, tl + 0.6, Q2A, Q2C, "15", Q2G, AMBAR, 60)
    if tbc is not None:
        E.foco(c, t, tbc, 0.4, lambda f: centro(c, "BC = 20", (Q2B[0] + Q2C[0]) / 2, Q2B[1] + 150, 54, "g", TINTA2, f * a))
    tbis = t0 + 0.6 if tbis is None else tbis
    if t >= tbis:
        metades(c, t, tbis + 0.4, Q2A, Q2B, Q2C, TINTA2, 90, a)
        linha(c, t, tbis, Q2A, Q2D, TINTA, 6, 0.7, a)
        ponto(c, t, tbis + 0.6, Q2D, "D", 0, 64, a=a)


def b_questao2(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    rel = C["s08.a"]
    progresso(c, t, a7, 2)
    fig_q2(c, t, a7 + 0.4, b7, c7, c7)
    E.foco(c, t, d7, 0.4, lambda f: (centro(c, "?", (Q2B[0] + Q2D[0]) / 2, Q2B[1] + 70, 64, "g", COR, f),
                                     centro(c, "?", (Q2D[0] + Q2C[0]) / 2, Q2B[1] + 70, 64, "g", AMBAR, f)))

    def txt():
        E.frase(c, t, b7, [("lados", "i", 60), ("10", "g", 72, COR), ("e", "i", 60), ("15", "g", 72, AMBAR)], XT, 330, "center", 0.12)
        E.frase(c, t, c7, [("bissetriz", "g", 66)] + ps("até o lado de", "i", 56) + [("20", "g", 66)], XT, 440, "center", 0.12)
    E.saida(c, t, rel - 0.5, txt)
    pergunta(c, t, [(d7, ps("quanto mede", "i", 60) + [("cada pedaço?", "g", 64, COR)])], rel)


def b_resposta2(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    t0 = C["s09"] - 1.0
    fig_q2(c, t, t0, t0, t0, t0)
    if t >= b9:
        for i in range(1, 5):
            P = (lerp(Q2B[0], Q2C[0], i / 5), Q2B[1])
            M.line(c, P[0], P[1] - 16, P[0], P[1] + 16, TINTA2, ep(t, b9 + 0.1 * i, 0.3), 5)
    pedaco(c, t, c9, Q2B, Q2D, COR, 1, 16)
    pedaco(c, t, d9, Q2D, Q2C, AMBAR, 1, 16)
    E.foco(c, t, c9 + 0.6, 0.4, lambda f: centro(c, "8 cm", (Q2B[0] + Q2D[0]) / 2, Q2B[1] + 75, 58, "g", CERTO, f))
    E.foco(c, t, d9 + 0.6, 0.4, lambda f: centro(c, "12 cm", (Q2D[0] + Q2C[0]) / 2, Q2B[1] + 75, 58, "g", CERTO, f))
    # o erro do "10 e 10": a marca do meio
    if a10 <= t < c10 + 0.6:
        k = ep(t, a10, 0.4) * (1 - ep(t, b10, 0.4))
        Mm = ((Q2B[0] + Q2C[0]) / 2, Q2B[1])
        M.line(c, Mm[0], Mm[1] - 30, Mm[0], Mm[1] + 30, ERRADO, k, 7)
        centro(c, "meio", Mm[0], Mm[1] - 50, 46, "i", ERRADO, k)
    if t >= c10:
        brilho(c, Q2A, Q2C, AMBAR, ep(t, c10, 0.4))
        brilho(c, Q2D, Q2C, AMBAR, ep(t, c10, 0.4))

    def nove():
        E.frase(c, t, C["s09"] + 0.2, [("atalho das partes", "g", 60, COR)], XT, 180, "center")
        E.frase(c, t, a9, [("10", "g", 64, COR), ("e", "i", 56), ("15", "g", 64, AMBAR), ("÷ 5", "b", 54, TINTA2)], XT, 300, "center", 0.12)
        E.frase(c, t, a9 + 1.4, [("2", "g", 84, COR), ("para", "i", 60), ("3", "g", 84, AMBAR)], XT, 410, "center", 0.12)
        fcen(c, t, b9, "20 ÷ 5 = 4", XT, 550, 72)
        fcen(c, t, c9, "BD = 2 · 4 = 8", XT, 690, 66, COR)
        fcen(c, t, d9, "DC = 3 · 4 = 12", XT, 820, 66, AMBAR)
    E.saida(c, t, C["s10"] - 0.1, nove)
    if t < C["s10"]:
        return
    E.frase(c, t, a10, [("10 e 10?", "g", 70, ERRADO)], XT - 120, 260, "center")
    E.foco(c, t, a10 + 0.4, 0.4, lambda a: E.selo(c, XT + 160, 238, 46, False, a))
    E.frase(c, t, a10 + 1.2, ps("divide o", "i", 56) + [("ângulo,", "g", 60)] + ps("não o lado", "i", 56), XT, 360, "center", 0.12)
    E.frase(c, t, b10, [("12 junto do 10?", "g", 64, ERRADO)], XT - 70, 520, "center")
    E.foco(c, t, b10 + 0.4, 0.4, lambda a: E.selo(c, XT + 260, 498, 46, False, a))
    E.foco(c, t, c10, 0.5, lambda a: E.pilula(c, "pedaço maior junto do lado maior", XT, 700, 40, "g", fundo=CERTO, a=a))


# ---------------- Q3: encaixados (AM 6, MB 3, MN 8, BC 12) ----------------
Q3B, Q3C = (120, 880), (840, 880)
Q3A = (360, 880 - math.sqrt(540 ** 2 - 240 ** 2))     # AB = 9 a 60 px por unidade
Q3M = (lerp(Q3A[0], Q3B[0], 2 / 3), lerp(Q3A[1], Q3B[1], 2 / 3))
Q3N = (lerp(Q3A[0], Q3C[0], 2 / 3), lerp(Q3A[1], Q3C[1], 2 / 3))
Q3G = centroide((Q3A, Q3B, Q3C))
assert abs(math.dist(Q3M, Q3N) - 480) < 1e-6 and abs(math.dist(Q3A, Q3M) - 360) < 1e-6


def fig_q3(c, t, t0, tmn=None, tl=None, tq=None, ab=None, a=1.0):
    """ABC com MN paralelo a BC; tl = medidas 6, 8, 12; tq = ? em MB; ab = (troca do ? por 3)"""
    triang(c, t, t0, (Q3A, Q3B, Q3C), "ABC", a=a)
    tmn = t0 + 0.6 if tmn is None else tmn
    if t >= tmn:
        M.line(c, *Q3M, lerp(Q3M[0], Q3N[0], ease_io(prog(t, tmn, 0.6))), Q3M[1], TINTA, a, 6)
        k = ep(t, tmn + 0.4, 0.3) * a
        for P_, s, dx in ((Q3M, "M", -52), (Q3N, "N", 52)):
            c.drawCircle(*P_, 10 * k, M.paint(TINTA, k))
            centro(c, s, P_[0] + dx, P_[1] + 20, 54, "g", TINTA, k)
        seta_par(c, Q3M, Q3N, 0.55, k); seta_par(c, Q3B, Q3C, 0.55, k)
    if tl is not None:
        lab(c, t, tl, Q3A, Q3M, "6", Q3G, COR, 56, 18)
        E.foco(c, t, tl + 0.8, 0.4, lambda f: centro(c, "8", (Q3M[0] + Q3N[0]) / 2, Q3M[1] - 18, 54, "g", AMBAR, f * a))
        lab(c, t, tl + 1.6, Q3B, Q3C, "12", Q3G, AMBAR, 58, 20)
    if tq is not None:
        if ab is None:
            lab(c, t, tq, Q3M, Q3B, "?", Q3G, ERRADO, 64, 18)
        else:
            E.saida(c, t, ab, lambda: lab(c, t, tq, Q3M, Q3B, "?", Q3G, ERRADO, 64, 18))
            lab(c, t, ab, Q3M, Q3B, "3", Q3G, CERTO, 64, 18)


def b_questao3(c, t, C, b):
    a11, b11, c11, d11 = (C[f"s11.{k}"] for k in "abcd")
    rel = C["s12.a"]
    progresso(c, t, a11, 3)
    fig_q3(c, t, a11 + 0.4, b11, c11, d11)

    def txt():
        E.frase(c, t, b11, [("MN", "g", 66, AMBAR)] + ps("paralelo a", "i", 58) + [("BC", "g", 66, AMBAR)], XT, 300, "center", 0.12)
        E.frase(c, t, c11, [("AM = 6", "g", 60, COR), ("MN = 8", "g", 60, AMBAR)], XT, 420, "center", 0.3)
        E.frase(c, t, c11 + 1.8, [("BC = 12", "g", 60, AMBAR)], XT, 510, "center")
    E.saida(c, t, rel - 0.5, txt)
    pergunta(c, t, [(d11, [("MB = ?", "g", 72, ERRADO)])], rel)


DESL3 = (560, -200)


def b_resposta3(c, t, C, b):
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14, d14, e14 = (C[f"s14.{k}"] for k in "abcde")
    t0 = C["s13"] - 1.0
    fig_q3(c, t, t0, t0, t0, t0, ab=d14)
    # o pequeno, AMN, sai do grande
    if t >= a13:
        q = ease_io(prog(t, a13, 1.0))
        d = (DESL3[0] * q, DESL3[1] * q)
        A2, M2, N2 = [(P[0] + d[0], P[1] + d[1]) for P in (Q3A, Q3M, Q3N)]
        path = skia.Path(); path.addPoly([A2, M2, N2], True)
        c.drawPath(path, M.paint(E.COR, 0.12))
        for P_, Q_ in ((A2, M2), (M2, N2), (N2, A2)):
            M.line(c, *P_, *Q_, TINTA, 1, 6)
        G2 = centroide((A2, M2, N2))
        for P_, s in ((A2, "A"), (M2, "M"), (N2, "N")):
            ux, uy = E._uni(*G2, *P_)
            centro(c, s, P_[0] + ux * 46, P_[1] + uy * 46 + 20, 50, "g", TINTA, ep(t, a13 + 0.8, 0.3))
        E.foco(c, t, a13 + 0.8, 0.4, lambda f: (txt_lado(c, A2, M2, "6", G2, 54, COR, f, 16),
                                                centro(c, "8", (M2[0] + N2[0]) / 2, M2[1] + 66, 54, "g", AMBAR, f)))
        if t >= b13:
            marca(c, t, b13, A2, M2, N2, 0, TINTA2, 50, alfa=0.3)
            marca(c, t, b13 + 0.8, M2, A2, N2, 1, COR, 44)
    if t >= b13:
        marca(c, t, b13, Q3A, Q3B, Q3C, 0, TINTA2, 60, alfa=0.3)
        marca(c, t, b13 + 0.8, Q3B, Q3A, Q3C, 1, COR, 60)
        marca(c, t, b13 + 0.8, Q3M, Q3A, Q3N, 1, COR, 44)
    brilho(c, Q3A, Q3B, COR, ep(t, c13, 0.4) * (1 - ep(t, c14, 0.4)))
    brilho(c, Q3M, Q3B, CERTO, ep(t, c14, 0.4))
    X = 1600

    def treze():
        E.frase(c, t, a13, [("separe", "g", 70, COR)] + ps("os triângulos", "i", 56), 1500, 700, "center", 0.12)
        E.frase(c, t, b13, ps("ângulo A comum,", "i", 52) + [("M e B iguais", "g", 56, COR)], 1500, 800, "center", 0.12)
        E.frase(c, t, b13 + 1.6, [("semelhantes", "g", 60, COR)], 1500, 890, "center")
    E.saida(c, t, c13 - 0.1, treze)
    if t >= c13:
        prop(c, t, c13, "6", "AB", "8", "12", X, 220, 84, cores=(COR, COR, AMBAR, AMBAR), t1=c13 + 1.4, dx=160)
        if t >= a14:
            cruz(c, t, a14, a14 + 0.5, X, 220, 84, dx=160, wa=50, wb=55)
        fcen(c, t, a14, "8 · AB = 6 · 12 = 72", 1490, 690, 56)
        fcen(c, t, b14, "AB = 72 ÷ 8 = 9", 1490, 790, 58, COR)
        fcen(c, t, d14, "MB = 9 − 6 = 3", 1400, 900, 62, CERTO)
        bola_txt(c, t, d14 + 0.6, "3 cm", 1750, 880, 66, 46, CERTO)
        E.frase(c, t, e14, ps("o 9 é o", "i", 50) + [("lado inteiro", "g", 54, ERRADO)], 1490, 1010, "center", 0.12)


# ---------------- Q4: gravata (AB 6, CD 9, AM 4, MC 6) ----------------
U4 = 60
Q4A, Q4B = (380, 300), (380 + 6 * U4, 300)
_g4 = math.radians(62)
Q4M = (Q4A[0] + 4 * U4 * math.cos(_g4), Q4A[1] + 4 * U4 * math.sin(_g4))
Q4C = (Q4M[0] + 1.5 * (Q4M[0] - Q4A[0]), Q4M[1] + 1.5 * (Q4M[1] - Q4A[1]))
Q4D = (Q4M[0] + 1.5 * (Q4M[0] - Q4B[0]), Q4M[1] + 1.5 * (Q4M[1] - Q4B[1]))
assert abs(math.dist(Q4C, Q4D) - 9 * U4) < 1e-6 and abs(math.dist(Q4M, Q4C) - 6 * U4) < 1e-6


def fig_q4(c, t, t0, tab=None, tl=None, tq=None, troca=None, a=1.0):
    """AC e BD se cruzam em M (t0); AB e CD paralelos (tab); medidas (tl); ? em MC (tq), que vira 6 em troca"""
    linha(c, t, t0, Q4A, Q4C, TINTA, 6, 0.8, a)
    linha(c, t, t0 + 0.3, Q4B, Q4D, TINTA, 6, 0.8, a)
    tab = t0 + 0.6 if tab is None else tab
    linha(c, t, tab, Q4A, Q4B, TINTA, 6, 0.6, a)
    linha(c, t, tab + 0.3, Q4D, Q4C, TINTA, 6, 0.6, a)
    k = ep(t, tab + 0.6, 0.3) * a
    seta_par(c, Q4A, Q4B, 0.55, k); seta_par(c, Q4D, Q4C, 0.55, k)
    for P, s, dx, dy in ((Q4A, "A", -50, 0), (Q4B, "B", 50, 0), (Q4C, "C", 50, 40), (Q4D, "D", -50, 40), (Q4M, "M", 64, 20)):
        E.foco(c, t, t0 + 0.6, 0.4, lambda f, P=P, s=s, dx=dx, dy=dy: centro(c, s, P[0] + dx, P[1] + dy + 4, 54, "g", TINTA, f * a))
    if tl is not None:
        E.foco(c, t, tl, 0.4, lambda f: centro(c, "6", (Q4A[0] + Q4B[0]) / 2, Q4A[1] - 26, 56, "g", COR, f * a))
        E.foco(c, t, tl + 0.5, 0.4, lambda f: centro(c, "9", (Q4C[0] + Q4D[0]) / 2, Q4C[1] + 70, 56, "g", COR, f * a))
        rot(c, t, tl + 1.0, Q4A, Q4M, "4", 1, AMBAR, 56, 22)
    if tq is not None:
        if troca is None:
            rot(c, t, tq, Q4M, Q4C, "?", 1, ERRADO, 64, 22)
        else:
            rot_troca(c, t, tq, troca, Q4M, Q4C, "x", "6", 1, AMBAR, CERTO, 60, 22)


def b_questao4(c, t, C, b):
    a15, b15, c15, d15, e15 = (C[f"s15.{k}"] for k in "abcde")
    rel = C["s16.a"]
    progresso(c, t, a15, 4)
    fig_q4(c, t, b15, c15, d15, e15)

    def txt():
        E.frase(c, t, b15, [("AC", "g", 64), ("e", "i", 56), ("BD", "g", 64)] + ps("se cruzam em", "i", 56) + [("M", "g", 64)], XT, 300, "center", 0.12)
        E.frase(c, t, c15, [("AB", "g", 64, COR)] + ps("paralelo a", "i", 56) + [("CD", "g", 64, COR)], XT, 400, "center", 0.12)
        E.frase(c, t, d15, [("AB = 6", "g", 56, COR), ("CD = 9", "g", 56, COR), ("AM = 4", "g", 56, AMBAR)], XT, 520, "center", 0.4)
    E.saida(c, t, rel - 0.5, txt)
    pergunta(c, t, [(e15, [("MC = ?", "g", 72, ERRADO)])], rel)


def b_resposta4(c, t, C, b):
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    a18, b18, c18, d18, e18 = (C[f"s18.{k}"] for k in "abcde")
    a19, b19 = C["s19.a"], C["s19.b"]
    t0 = C["s17"] - 1.0
    if t >= a17:
        k = ep(t, a17, 0.4)
        for T, cor, al in (((Q4A, Q4M, Q4B), E.COR, 0.16), ((Q4C, Q4M, Q4D), AMBAR, 0.16 + 0.12 * ep(t, a19, 0.4))):
            path = skia.Path(); path.addPoly(list(T), True)
            c.drawPath(path, M.paint(cor, al * k))
    fig_q4(c, t, t0, t0, t0, t0, troca=e18)
    marca(c, t, a17 + 0.6, Q4M, Q4A, Q4B, 0, TINTA2, 50, alfa=0.35)
    marca(c, t, a17 + 0.9, Q4M, Q4C, Q4D, 0, TINTA2, 50, alfa=0.35)
    marca(c, t, b17, Q4A, Q4B, Q4C, 1, COR, 60)
    marca(c, t, b17 + 0.6, Q4C, Q4D, Q4A, 1, COR, 60)
    # pares que se correspondem
    k1 = ep(t, b18, 0.4) * (1 - ep(t, d18, 0.4))
    brilho(c, Q4A, Q4M, AMBAR, k1); brilho(c, Q4C, Q4M, AMBAR, k1)
    brilho(c, Q4A, Q4B, COR, k1); brilho(c, Q4C, Q4D, COR, k1)
    X = XT

    def dezessete():
        E.frase(c, t, a17, [("AMB", "g", 62, COR), ("e", "i", 56), ("CMD", "g", 62, AMBAR)], X, 240, "center", 0.12)
        E.frase(c, t, a17 + 1.0, ps("opostos pelo vértice", "i", 54) + [("em M", "g", 58, TINTA2)], X, 330, "center", 0.12)
        E.frase(c, t, b17, ps("alternos internos:", "i", 54) + [("A e C", "g", 58, COR)], X, 460, "center", 0.12)
        E.foco(c, t, c17, 0.5, lambda a: E.pilula(c, "semelhantes", X, 600, 62, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, c17 + 0.8, ps("um de cabeça para baixo", "i", 52, TINTA2), X, 700, "center", 0.1)
    E.saida(c, t, C["s18"] - 0.1, dezessete)
    if C["s18"] - 0.1 <= t < C["s19"]:
        def dezoito():
            E.frase(c, t, a18, [("A ↔ C", "g", 58, COR), ("B ↔ D", "g", 58, AMBAR)], X, 190, "center", 0.4)
            E.frase(c, t, b18, [("AM ↔ CM", "g", 54, AMBAR), ("AB ↔ CD", "g", 54, COR)], X, 280, "center", 0.4)
            prop(c, t, c18, "4", "x", "6", "9", X, 450, 90, cores=(AMBAR, AMBAR, COR, COR), t1=c18 + 1.3, dx=150)
            if t >= d18:
                cruz(c, t, d18, d18 + 0.5, X, 450, 90, dx=150, wa=50, wb=50)
            fcen(c, t, d18, "6x = 4 · 9 = 36", X, 720, 66)
            fcen(c, t, e18, "x = 36 ÷ 6", X - 110, 860, 66)
            bola_txt(c, t, e18 + 0.6, "6", X + 180, 835, 70, 86, CERTO)
        E.saida(c, t, C["s19"] - 0.1, dezoito)
    if t >= C["s19"]:
        E.frase(c, t, a19, ps("faz sentido:", "i", 58), X, 300, "center", 0.12)
        E.frase(c, t, a19 + 0.8, ps("o de baixo é o", "i", 56) + [("maior", "g", 62, AMBAR)], X, 400, "center", 0.12)
        E.frase(c, t, b19, [("MC = 6", "g", 64, CERTO), ("> AM = 4", "g", 64, AMBAR)], X, 560, "center", 0.3)
        E.foco(c, t, b19 + 1.0, 0.5, lambda a: E.selo(c, X, 720, 60, True, a))


# ---------------- Q5: sombra (vara 1,5 e 2; torre x e 20) ----------------
GY5 = 860
V0, VT, VS = (200, GY5), (200, GY5 - 1.5 * 100), (200 + 2 * 100, GY5)
T0_, TT, TS = (640, GY5), (640, GY5 - 15 * 24), (640 + 20 * 24, GY5)
assert abs((VT[1] - GY5) / (VS[0] - V0[0]) - (TT[1] - GY5) / (TS[0] - T0_[0])) < 1e-9


def sol(c, x, y, r=40, a=1.0):
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(x, y), r * 2.4, [M.hexc(AMB_C, 0.45 * a), M.hexc(AMB_C, 0.0)], [0, 1]))
    c.drawCircle(x, y, r * 2.4, p)
    c.drawCircle(x, y, r, M.paint(AMB_C, a))
    for i in range(8):
        g = math.radians(i * 45)
        M.line(c, x + math.cos(g) * r * 1.3, y + math.sin(g) * r * 1.3, x + math.cos(g) * r * 1.7, y + math.sin(g) * r * 1.7, AMB_C, a, 5)


def raio(c, t, t0, topo, ponta, extra=200, a=1.0, cor=AMBAR, larg=5):
    if t < t0 or a <= 0:
        return
    ux, uy = E._uni(*ponta, *topo)
    O = (topo[0] + ux * extra, topo[1] + uy * extra)
    q = ease_io(prog(t, t0, 0.7))
    M.line(c, *O, lerp(O[0], ponta[0], q), lerp(O[1], ponta[1], q), cor, a, larg, dash=[16, 10])


def sombra(c, t, t0, base, ponta, a=1.0, cor=TINTA, alfa=0.32):
    if t < t0 or a <= 0:
        return
    M.line(c, *base, lerp(base[0], ponta[0], ease_io(prog(t, t0, 0.6))), base[1], cor, alfa * a, 20)


def torre(c, t, t0, base, topo, a=1.0, cor=TINTA, escuro=False):
    """torre de treliça: duas pernas que se afinam e travessas"""
    if t < t0 or a <= 0:
        return
    q = ease_io(prog(t, t0, 0.6))
    h = (base[1] - topo[1]) * q
    yt = base[1] - h
    wb, wt = 46, 10
    L0, R0 = (base[0] - wb, base[1]), (base[0] + wb * 0.0, base[1])
    M.line(c, base[0] - wb, base[1], base[0] - wt, yt, cor, a, 6)
    M.line(c, base[0], base[1], base[0], yt, cor, a, 8)
    n = int(h // 50)
    for i in range(1, n + 1):
        y = base[1] - i * 50
        f = (base[1] - y) / max(1, base[1] - topo[1])
        M.line(c, base[0] - lerp(wb, wt, f), y, base[0], y, cor, a * 0.7, 3)


def cena5(c, t, tv, tt, tl=None, tx=None, a=1.0, escuro=False):
    tinta = BR if escuro else TINTA
    M.line(c, 80, GY5, 1240, GY5, "#5A5878" if escuro else TINTA2, ep(t, tv - 0.3, 0.4) * a, 4)
    E.foco(c, t, tv - 0.3, 0.5, lambda f: sol(c, 120, 200, 36, f * a))
    linha(c, t, tv, V0, VT, tinta, 12, 0.5, a)
    sombra(c, t, tv + 0.3, V0, VS, a, "#8C8AA8" if escuro else TINTA, 0.8 if escuro else 0.32)
    raio(c, t, tv + 0.5, VT, VS, 160, a, AMB_C if escuro else AMBAR)
    if t >= tt:
        torre(c, t, tt, T0_, TT, a, tinta)
        sombra(c, t, tt + 0.4, T0_, TS, a, "#8C8AA8" if escuro else TINTA, 0.8 if escuro else 0.32)
        raio(c, t, tt + 0.7, TT, TS, 160, a, AMB_C if escuro else AMBAR)


def labs5(c, t, tv, tt, tq=None, troca=None, escuro=False, cor_h=None, cor_s=None):
    cor_h = cor_h or (CLARO if escuro else COR)
    cor_s = cor_s or (AMB_C if escuro else AMBAR)
    E.foco(c, t, tv, 0.4, lambda f: E.escreve(c, "1,5 m", V0[0] - 170, (V0[1] + VT[1]) / 2 + 20, 54, "g", cor_h, f))
    E.foco(c, t, tv + 0.6, 0.4, lambda f: centro(c, "2 m", (V0[0] + VS[0]) / 2, GY5 + 70, 54, "g", cor_s, f))
    E.foco(c, t, tt, 0.4, lambda f: centro(c, "20 m", (T0_[0] + TS[0]) / 2, GY5 + 70, 54, "g", cor_s, f))
    if tq is not None:
        def h(s, cor, f):
            E.escreve(c, s, T0_[0] - 70 - E.larg(s, "g", 64), (T0_[1] + TT[1]) / 2 + 22, 64, "g", cor, f)
        if troca is None:
            E.foco(c, t, tq, 0.4, lambda f: h("?", ERRADO, f))
        else:
            E.saida(c, t, troca, lambda: E.foco(c, t, tq, 0.4, lambda f: h("x", cor_h, f)))
            E.foco(c, t, troca, 0.4, lambda f: h("15 m", "#7EE2A0" if escuro else CERTO, f))


def b_questao5(c, t, C, b):
    a20, b20, c20, d20 = (C[f"s20.{k}"] for k in "abcd")
    rel = C["s21.a"]
    progresso(c, t, a20, 5)
    cena5(c, t, b20, c20)
    labs5(c, t, b20 + 0.6, c20 + 0.8, d20)

    def txt():
        E.frase(c, t, b20, [("vara", "g", 64)] + ps("de", "i", 56) + [("1,5 m", "g", 64, COR)], XT, 300, "center", 0.12)
        E.frase(c, t, b20 + 1.4, ps("sombra de", "i", 56) + [("2 m", "g", 64, AMBAR)], XT, 390, "center", 0.12)
        E.frase(c, t, c20, [("torre:", "g", 64)] + ps("sombra de", "i", 56) + [("20 m", "g", 64, AMBAR)], XT, 520, "center", 0.12)
    E.saida(c, t, rel - 0.5, txt)
    pergunta(c, t, [(d20, ps("altura da", "i", 60) + [("torre?", "g", 66, COR)])], rel)


def b_resposta5(c, t, C, b):
    a22, b22, c22 = C["s22.a"], C["s22.b"], C["s22.c"]
    t0 = C["s22"] - 1.0
    cena5(c, t, t0, t0)
    labs5(c, t, t0, t0, t0, troca=c22 + 0.6)
    k = ep(t, a22, 0.3) * (1 - ep(t, b22, 0.4))
    brilho(c, V0, VT, COR, k); brilho(c, T0_, TT, COR, k)
    brilho(c, V0, VS, AMBAR, k); brilho(c, T0_, TS, AMBAR, k)
    E.frase(c, t, C["s22"] + 0.2, [("altura", "g", 64, COR)] + ps("sobre", "i", 56) + [("sombra", "g", 64, AMBAR)], XT, 200, "center", 0.12)
    prop(c, t, a22, "1,5", "2", "x", "20", XT, 370, 96, cores=(COR, AMBAR, COR, AMBAR), t1=a22 + 1.6, dx=180)
    if t >= b22:
        cruz(c, t, b22, b22 + 0.5, XT, 370, 96, dx=180, wa=80, wb=55)
    fcen(c, t, b22, "2x = 1,5 · 20 = 30", XT, 640, 66)
    fcen(c, t, c22, "x = 30 ÷ 2", XT - 120, 790, 66)
    bola_txt(c, t, c22 + 0.6, "15 m", XT + 170, 765, 80, 56, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a23, b23, c23, d23 = (C[f"s23.{k}"] for k in "abcd")
    t0 = C["s23"]
    cena5(c, t, t0, t0 + 0.3, escuro=True)
    labs5(c, t, t0 + 0.4, t0 + 0.6, t0 + 0.6, troca=b23 + 0.6, escuro=True)
    LIL = CLARO
    E.frase(c, t, t0 + 0.2, ps("pelo", "i", 66, CLARO) + [("fator", "g", 80, BR)], XT, 200, "center", 0.12)
    E.frase(c, t, a23, [("20 = 10 · 2", "g", 70, AMB_C)], XT, 330, "center")
    E.frase(c, t, b23, [("10 · 1,5 = 15 m", "g", 70, "#7EE2A0")], XT, 450, "center")
    E.frase(c, t, c23, ps("semelhança: todos os lados", "i", 50, CLARO), XT, 590, "center", 0.1)
    E.frase(c, t, c23 + 1.4, [("× o mesmo número", "g", 60, BR)], XT, 670, "center")
    E.frase(c, t, d23, ps("não é múltiplo?", "i", 58, CLARO), XT, 830, "center", 0.12)
    E.foco(c, t, lerp(d23, C["s23.end"], 0.6), 0.5, lambda a: E.pilula(c, "vá de cruz", XT, 950, 62, "g", a=a, cor=E.SOBRE))
    # ×10 entre as sombras
    if t >= a23:
        k = ep(t, a23, 0.4)
        M.arrow(c, VS[0] - 40, GY5 + 130, TS[0] - 140, GY5 + 130, AMB_C, k, 5, 20, ease_io(prog(t, a23, 0.7)))
        E.foco(c, t, a23 + 0.5, 0.4, lambda f: centro(c, "× 10", (VS[0] + TS[0]) / 2 - 40, GY5 + 115, 52, "g", AMB_C, f))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s24.a", "frações sempre na mesma ordem"), ("s24.b", "siga os ângulos"), ("s24.c", "separe e use o lado inteiro"))
        for i, (k, s) in enumerate(itens):
            y = 420 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 380, y - 30, 56, 64, a))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 76)], 480, y)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25"] + 0.2, ps("próxima aula: uma parte nova", "i", 76), XE, 260, passo=0.1)
    E.frase(c, t, C["s25.a"], [("Teorema de", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s25.a"] + 0.3, [("Pitágoras", "g", 110, COR)], XE, 520)
    E.frase(c, t, C["s25.b"], [("6 e 8", "g", 66), ("→", "g", 60, TINTA2)] + ps("o lado maior", "i", 62), XE, 650, passo=0.12)
    E.frase(c, t, C["s25.c"], [("13 e 5", "g", 66), ("→", "g", 60, TINTA2)] + ps("um lado menor", "i", 62), XE, 750, passo=0.12)
    E.foco(c, t, C["s25.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s25.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1630, p), lerp(720, 425, p), ep(t, C["s25.d"] + 0.2, 0.4))
    E.frase(c, t, C["s25.e"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], 1300, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, atalho=b_atalho, fim=b_fim)
