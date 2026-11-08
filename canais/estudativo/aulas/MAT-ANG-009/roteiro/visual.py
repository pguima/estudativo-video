"""Visual — Estudativo · MAT-ANG-009: praticando ângulos e triângulos (cinco questões).
Aula de prática no molde da MAT-EQU-012: selo de progresso "questão n de 5", figura à esquerda, pergunta embaixo à direita e
relógio de pausa; na resposta, a mesma figura ganha as medidas e a conta aparece na coluna da direita.
Linguagem da geometria plana (MAT-ANG-001 a 020): lados em tinta; ângulos iguais com a mesma cor (famílias COR, TINTA2, AMBAR);
lados iguais com tracinhos; ângulo reto = quadradinho; prolongamento tracejado; voa() leva um ângulo até onde ele é copiado.
Erro em vermelho; certo em verde; medidas na grotesca; resposta na esfera.
Peças locais (as da MAT-ANG-004/007/008/020): tri(), canto(), metades(), triang(), rotulo(), cunha_m(), voa(), vareta(), txt_lado(),
grosso(), notavel(), mediana_2_1(); e ainda marca() (progresso), pergunta() (linhas da pergunta + relógio) e paralelas_rs().
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-009_praticando_angulos_e_triangulos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "atalho", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
PAPEL = "#F4F3EE"
assert 55 - 15 == 40 and 40 // 2 == 20 and 2 * 20 + 15 == 55 and 55 + 65 == 120 and 180 - 120 == 60 and 180 - 55 - 65 == 60
assert 180 - 115 == 65 and 65 + 65 == 130 and 180 - 130 == 50 and 50 + 65 == 115
assert 5 + 5 == 10 < 11 and 11 + 5 == 16 > 11 and 11 + 11 + 5 == 27 and 5 + 5 + 11 == 21
assert 16 // 2 == 8 and 180 // 2 == 90
assert 3 * 4 - 2 == 10 and 4 + 1 == 5 and 10 == 2 * 5 and 10 + 5 == 15


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


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)


def pt(V, L, g):
    return V[0] + L * math.cos(math.radians(g)), V[1] - L * math.sin(math.radians(g))


def meio(P, Q):
    return (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2


def rotulo(c, V, g, r, s, cor, size, a):
    if a <= 0 or not s:
        return
    w = E.formula(None, s, 0, 0, size, "b", a=0)
    ux, uy = math.cos(math.radians(g)), -math.sin(math.radians(g))
    k = r + 16 + abs(ux) * w / 2 + abs(uy) * size * 0.4
    E.formula(c, s, V[0] + ux * k, V[1] + uy * k + size * 0.36, size, "b", cor, a, "center")


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


def voa(c, t, t0, d, V0, g1, g2, r, cor=None, V1=None, giro=0.0, fica=0.8):
    """o ângulo se move (ver MAT-ANG-002): a cunha sai de V0, gira e viaja até V1, deixando o contorno tracejado na origem"""
    if t < t0 or t > t0 + d + fica + 0.4:
        return
    cor = cor or E.COR
    V1 = V1 or V0
    p = ease_io(prog(t, t0, d))
    a = 1 - ep(t, t0 + d + fica, 0.4)
    ret = skia.Rect.MakeXYWH(V0[0] - r, V0[1] - r, 2 * r, 2 * r)
    tr = M.paint(cor, 0.8 * a, stroke=3)
    tr.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
    path = skia.Path(); path.moveTo(*V0); path.arcTo(ret, -g1, -(g2 - g1), False); path.close()
    c.drawPath(path, tr)
    lift = 1 + 0.08 * math.sin(math.pi * p)
    c.save()
    c.translate(lerp(V0[0], V1[0], p), lerp(V0[1], V1[1], p))
    c.rotate(-giro * p)
    c.scale(lift, lift)
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.25 * a * math.sin(math.pi * p)))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
    path2 = skia.Path(); path2.moveTo(0, 0); path2.arcTo(skia.Rect.MakeXYWH(-r, -r, 2 * r, 2 * r), -g1, -(g2 - g1), False); path2.close()
    c.save(); c.translate(6, 12); c.drawPath(path2, s); c.restore()
    cunha_m(c, (0, 0), g1, g2, r, cor, a, alfa=0.55)
    c.restore()


def dirg(V, P):
    return math.degrees(math.atan2(-(P[1] - V[1]), P[0] - V[0])) % 360


def faixa_v(V, P, Q):
    a1, a2 = dirg(V, P), dirg(V, Q)
    d = (a2 - a1) % 360
    return (a1, a1 + d) if d <= 180 else (a2, a2 + (360 - d))


def canto(c, t, t0, V, P, Q, rot=None, cor=None, r=80, tr=None, size=52, alfa=0.25, a=1.0, rl=None):
    """ângulo PVQ com arco e cunha da cor da família, e a medida por fora do arco"""
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    g1, g2 = faixa_v(V, P, Q)
    q = ease_io(prog(t, t0, 0.5))
    cunha_m(c, V, g1, g1 + (g2 - g1) * q, r, cor, a, alfa=alfa, borda=5)
    if rot:
        s = rot(t) if callable(rot) else rot
        E.foco(c, t, tr if tr is not None else t0 + 0.3, 0.4, lambda k: rotulo(c, V, (g1 + g2) / 2, rl or r, s, COR if cor == E.COR else cor, size, k * a))


def metades(c, t, t0, V, P, Q, cor=None, r=90, a=1.0):
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    g1, g2 = faixa_v(V, P, Q)
    gm = (g1 + g2) / 2
    q = ease_io(prog(t, t0, 0.5))
    cunha_m(c, V, g1, g1 + (gm - g1) * q, r, cor, a, alfa=0.3, borda=5)
    cunha_m(c, V, gm, gm + (g2 - gm) * q, r * 0.86, cor, a, alfa=0.3, borda=5)


def triang(c, t, t0, A, B, C, nomes="ABC", tinta=TINTA, preenche=0.06, d=0.9, a=1.0):
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


def txt_lado(c, P, Q, s, G, size=50, cor=None, a=1.0, gap=18):
    if a <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = meio(P, Q)
    if (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 < (mx - G[0]) ** 2 + (my - G[1]) ** 2:
        nx, ny = -nx, -ny
    E._cola(c, s, mx, my, nx, ny, gap, size, "b", cor or COR, a)


def txt_seg(c, P, Q, s, lado, size=54, cor=None, a=1.0, gap=34):
    if a <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    E._cola(c, s, *meio(P, Q), uy * lado, -ux * lado, gap, size, "b", cor or COR, a)


def grosso(c, P, Q, cor, a, larg=12):
    if a > 0:
        M.line(c, *P, *Q, cor, a, larg)


def vareta(c, P, Q, cor=TINTA, a=1.0):
    if a <= 0:
        return
    M.line(c, *P, *Q, cor, a, 14)
    for V in (P, Q):
        c.drawCircle(*V, 12, M.paint(cor, a))


def marca(c, t, t0, n):
    """questão n de 5, com cinco pontos de progresso (como na MAT-EQU-012)"""
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


def pergunta(c, t, linhas, rel, X=1500, y0=860):
    """linhas da pergunta embaixo à direita: [(t0, partes), ...]; relógio de pausa em rel"""
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, y0 + i * 100, "center", 0.12)
    E.relogio(c, t, rel, X, 430, 180)


def seta_par(c, x, y, a=1.0, cor=TINTA):
    """a setinha que marca retas paralelas"""
    if a > 0:
        M.line(c, x - 14, y - 16, x + 6, y, cor, a, 5)
        M.line(c, x - 14, y + 16, x + 6, y, cor, a, 5)


# ---------------- figuras das questões ----------------
# Q1: r em cima, s embaixo; A em r; B e C em s; B = 55°, C = 65°, A = 60°
Q1A = (560, 300)
Q1B = (Q1A[0] - 520 / math.tan(math.radians(55)), 820)
Q1C = (Q1A[0] + 520 / math.tan(math.radians(65)), 820)
X0R, X1R = 80, 1100


def paralelas_rs(c, t, t0, tinta=TINTA, a=1.0, inclina=0.0):
    """as retas r (em cima, que pode inclinar) e s (embaixo), com as setinhas de paralelas"""
    if t < t0 or a <= 0:
        return
    q = ease_io(prog(t, t0, 0.7))
    dy = math.tan(math.radians(inclina)) * (X1R - Q1A[0])
    dy0 = math.tan(math.radians(inclina)) * (X0R - Q1A[0])
    M.line(c, X0R, Q1A[1] - dy0, lerp(X0R, X1R, q), lerp(Q1A[1] - dy0, Q1A[1] - dy, q), tinta, a, 6)
    M.line(c, X0R, Q1B[1], lerp(X0R, X1R, q), Q1B[1], tinta, a, 6)
    k = ep(t, t0 + 0.6, 0.4) * a
    E.foco(c, t, t0 + 0.5, 0.4, lambda f: (centro(c, "r", X1R + 40, Q1A[1] - dy + 20, 60, "i", tinta, f * a),
                                           centro(c, "s", X1R + 40, Q1B[1] + 20, 60, "i", tinta, f * a)))
    if inclina == 0:
        for y in (Q1A[1], Q1B[1]):
            seta_par(c, 960, y, k, tinta)


def q1_fig(c, t, t0, tinta=TINTA):
    paralelas_rs(c, t, t0, tinta)
    triang(c, t, t0 + 0.5, Q1A, Q1B, Q1C, tinta=tinta, preenche=0.06)


R_ESQ = (X0R, Q1A[1])
R_DIR = (X1R, Q1A[1])


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]
    E.frase(c, t, a_ + 0.1, ps("5", "g", 240, COR) + ps("questões", "g", 170, COR), XE, 350, passo=0.25)
    E.frase(c, t, a_ + 1.0, ps("de ângulos e triângulos", "i", 80), XE, 480, passo=0.12)
    E.frase(c, t, a_ + 2.2, ps("criadas para esta aula", "i", 70, TINTA2), XE, 580, passo=0.12)
    for i, (s, cx, ti) in enumerate((("pause", 440, b_), ("resolva", 960, b_ + 0.9), ("confira", 1480, b_ + 2.0))):
        E.foco(c, t, ti, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 800, 56, 64, p),
                                                           E.escreve(c, s, cx - 110, 825, 92, "g", TINTA, p)))
    E.frase(c, t, lerp(b_, C["s01.end"], 0.6), ps("errar aqui", "i", 62) + [("ensina", "g", 66, COR)], W / 2, 980, "center", 0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.1, ps("você vai usar", "i", 84, COR), XE, 200, passo=0.12)
    itens = (("a", "ângulos nas paralelas"), ("b", "soma = 180°"), ("c", "o isósceles"),
             ("d", "o teste dos lados"), ("e", "a congruência"), ("f", "o baricentro"))
    for i, (k, s) in enumerate(itens):
        x = XE + 40 + (i // 3) * 860
        y = 380 + (i % 3) * 190
        ti = C[f"s02.{k}"]
        E.foco(c, t, ti, 0.5, lambda p, i=i, x=x, y=y: num_bola(c, str(i + 1), x, y - 28, 46, 54, p))
        E.frase(c, t, ti + 0.1, [(s, "g", 66)], x + 80, y)
    E.frase(c, t, C["s02.end"] - 2.6, ps("travou? procure a aula no canal", "i", 60), XE, 980, passo=0.1)


# ---------------- questão 1 ----------------
def b_questao1(c, t, C, b):
    a3, b3, c3 = C["s03.a"], C["s03.b"], C["s03.c"]
    a4, b4, c4, d4, e4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"], C["s04.e"]
    A, B, Cc = Q1A, Q1B, Q1C
    marca(c, t, a3, 1)
    paralelas_rs(c, t, b3)
    triang(c, t, c3, A, B, Cc)
    canto(c, t, a4, A, R_ESQ, B, "2x + 15", E.COR, 120, size=48, rl=110)
    canto(c, t, b4, A, Cc, R_DIR, "65°", AMBAR, 120, size=48, rl=110)
    canto(c, t, c4, B, A, Cc, "55°", TINTA2, 90, size=48)
    canto(c, t, e4, A, B, Cc, "?", ERRADO, 80, size=52, rl=110, alfa=0.15)
    X = 1500

    def txt():
        E.frase(c, t, b3, [("r // s", "g", 80, COR)], X, 300, "center")
        E.frase(c, t, b3 + 0.6, ps("(paralelas)", "i", 54, TINTA2), X, 380, "center", 0.1)
        E.frase(c, t, c3, ps("A em", "i", 58) + [("r,", "g", 60)] + ps("BC em", "i", 58) + [("s", "g", 60)], X, 520, "center", 0.12)
    E.saida(c, t, C["s05.a"] - 0.1, txt)
    pergunta(c, t, [(d4, [("x = ?", "g", 72, COR)]), (e4, ps("e o ângulo", "i", 60) + [("Â = ?", "g", 66, ERRADO)])], C["s05.a"])


# ---------------- resposta 1 ----------------
def b_resposta1(c, t, C, b):
    a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
    a7, b7 = C["s07.a"], C["s07.b"]
    A, B, Cc = Q1A, Q1B, Q1C
    X = 1500
    t0 = C["s06"] - 1.2
    q1_fig(c, t, t0)
    canto(c, t, t0, A, R_ESQ, B, (lambda tt: "55°" if tt >= e6 + 0.5 else "2x + 15"), E.COR, 120, size=48, rl=110)
    canto(c, t, t0, A, Cc, R_DIR, "65°", AMBAR, 120, size=48, rl=110)
    canto(c, t, t0, B, A, Cc, "55°", E.COR if t >= b6 else TINTA2, 90, size=48)
    canto(c, t, a7, Cc, A, B, "65°", AMBAR, 90, size=48)
    canto(c, t, b7, A, B, Cc, "60°", CERTO, 80, size=52, rl=110)
    # o Z dos alternos internos
    if t >= a6:
        k = ep(t, a6, 0.4) * (1 - ep(t, c6 + 0.5, 0.4))
        for P, Q in ((A, (A[0] - 300, A[1])), (A, B), (B, (B[0] + 300, B[1]))):
            grosso(c, P, Q, E.COR, k * 0.7, 10)

    def um():
        E.frase(c, t, a6, [("alternos internos", "g", 62, COR)], X, 260, "center")
        E.frase(c, t, a6 + 0.8, ps("os do Z:", "i", 56) + [("iguais", "g", 60, COR)], X, 350, "center", 0.12)
        fcen(c, t, c6, "2x + 15 = 55", X, 500, 80)
        fcen(c, t, d6, "2x = 40", X, 640, 80)
        bola_txt(c, t, e6, "x = 20", X, 830, 120, 64)
    E.saida(c, t, C["s07"] - 0.1, um)
    if t >= C["s07"]:
        E.frase(c, t, a7, ps("C alterno do 65:", "i", 56), X, 260, "center", 0.12)
        fcen(c, t, a7 + 0.6, "C = 65°", X, 360, 76, AMBAR)
        fcen(c, t, lerp(a7, b7, 0.4), "55 + 65 = 120", X, 520, 76)
        fcen(c, t, b7, "180 − 120 = 60", X, 660, 76)
        bola_txt(c, t, b7 + 0.8, "Â = 60°", X, 850, 120, 60, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a8, b8, c8, a9, b9, c9 = C["s08.a"], C["s08.b"], C["s08.c"], C["s09.a"], C["s09.b"], C["s09.c"]
    A, B, Cc = Q1A, Q1B, Q1C
    X = 1500
    inc = 8 * ease_io(prog(t, b9, 0.8))
    paralelas_rs(c, t, C["s08"], BR, inclina=inc)
    if inc > 0:
        M.line(c, X0R, A[1] - math.tan(math.radians(inc)) * (X0R - A[0]), X1R, A[1] - math.tan(math.radians(inc)) * (X1R - A[0]), ERRADO, ep(t, b9, 0.4), 6)
    triang(c, t, C["s08"], A, B, Cc, tinta=BR, preenche=0.1, a=1 - 0.5 * ep(t, a8, 0.4) * (1 - ep(t, a9, 0.4)))
    if t >= a8:  # o ponto A
        k = 0.5 + 0.5 * math.sin(2 * math.pi * (t - a8) / 1.0)
        c.drawCircle(*A, 20 + 8 * k, M.paint(CLARO, 0.5 * (1 - ep(t, b8, 0.4))))
    sem = 1 - ep(t, b9, 0.3)
    canto(c, t, b8, A, R_ESQ, B, "55°", CLARO, 120, size=50, rl=110, a=sem)
    canto(c, t, b8 + 0.4, A, B, Cc, "?", BR, 80, size=50, rl=110, a=sem)
    canto(c, t, b8 + 0.8, A, Cc, R_DIR, "65°", AMBAR, 120, size=50, rl=110, a=sem)
    if t >= b8 + 1.2:
        E.arco(c, A[0], A[1], 270, 0, 180 * ease_io(prog(t, b8 + 1.2, 0.7)), BR, 5, sem)
        E.foco(c, t, b8 + 1.6, 0.4, lambda a: centro(c, "180°", A[0] + 270, A[1] + 230, 56, "g", BR, a * sem))
    # os ângulos da base sobem e copiam os de cima
    g_b = faixa_v(B, A, Cc)
    g_c = faixa_v(Cc, A, B)
    voa(c, t, a9 + 0.3, 1.4, B, *g_b, 90, CLARO, V1=A, giro=180, fica=0.6)
    voa(c, t, a9 + 1.2, 1.4, Cc, *g_c, 90, AMBAR, V1=A, giro=180, fica=0.6)
    canto(c, t, C["s09"], B, A, Cc, None, CLARO, 70, a=sem)
    canto(c, t, C["s09"], Cc, A, B, None, AMBAR, 70, a=sem)

    def um():
        E.frase(c, t, a8, ps("olhe só para o", "i", 60, CLARO) + [("A", "g", 72, BR)], X, 260, "center", 0.12)
        E.frase(c, t, b8, ps("3 ângulos na reta r:", "i", 58, CLARO), X, 380, "center", 0.12)
        E.frase(c, t, b8 + 1.2, [("raso = 180°", "g", 70, BR)], X, 470, "center")
        fcen(c, t, c8, "180 − 55 − 65", X, 640, 76, CLARO)
        fcen(c, t, c8 + 0.8, "= 60°", X, 760, 90, BR)
        E.frase(c, t, c8 + 1.6, ps("sem passar pela base", "i", 54, CLARO), X, 880, "center", 0.1)
    E.saida(c, t, C["s09"] - 0.1, um)
    if t >= C["s09"]:
        E.frase(c, t, a9, ps("os de cima", "i", 60, CLARO) + [("copiam", "g", 66, BR)], X, 260, "center", 0.12)
        E.frase(c, t, a9 + 0.8, ps("os da base", "i", 60, CLARO), X, 350, "center", 0.12)
        E.frase(c, t, lerp(a9, b9, 0.55), ps("a mesma ideia do", "i", 54, CLARO) + [("180°", "g", 58, BR)], X, 480, "center", 0.12)
        E.frase(c, t, b9, ps("retas", "i", 60, CLARO) + [("não paralelas?", "g", 62, ERRADO)], X, 680, "center", 0.12)
        E.foco(c, t, c9, 0.5, lambda a: E.pilula(c, "não se copiam", X, 820, 66, "g", fundo=ERRADO, a=a))


# ---------------- questão 2 ----------------
I2B, I2C = (310, 860), (810, 860)
I2A = (560, 860 - 250 * math.tan(math.radians(65)))
I2D = (1080, 860)


def q2_fig(c, t, t0, ext="115°", t_ext=None):
    A, B, Cc, D = I2A, I2B, I2C, I2D
    triang(c, t, t0, A, B, Cc)
    q = ep(t, t0 + 0.7, 0.4)
    E.marcas_iguais(c, A, B, 1, TINTA, q)
    E.marcas_iguais(c, A, Cc, 1, TINTA, q)
    t_ext = t_ext if t_ext is not None else t0 + 1.0
    if t >= t_ext:
        M.line(c, *Cc, *D, TINTA, 1.0, 6, dash=E.TRACO, progress=ease_io(prog(t, t_ext, 0.6)))
        ret = skia.Rect.MakeXYWH(Cc[0] - 120, Cc[1] - 120, 240, 240)
        c.drawArc(ret, 0, -115 * ease_io(prog(t, t_ext + 0.4, 0.6)), False, M.paint(TINTA, 1.0, stroke=6, cap_round=True))
        E.foco(c, t, t_ext + 0.8, 0.4, lambda a: rotulo(c, Cc, 57, 120, ext, TINTA, 52, a))


def b_questao2(c, t, C, b):
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    A, B, Cc = I2A, I2B, I2C
    X = 1500
    marca(c, t, a10, 2)
    q2_fig(c, t, a10 + 0.4, t_ext=c10)
    for V, P, Q in ((A, B, Cc), (B, A, Cc), (Cc, A, B)):
        canto(c, t, d10, V, P, Q, "?", ERRADO, 60, size=50, alfa=0.12)

    def txt():
        E.frase(c, t, a10 + 0.4, [("isósceles", "g", 76, COR)], X, 260, "center")
        E.frase(c, t, b10, [("AB = AC", "g", 70)], X, 380, "center")
        E.frase(c, t, c10, ps("externo em C:", "i", 58) + [("115°", "g", 66)], X, 520, "center", 0.12)
    E.saida(c, t, C["s11.a"] - 0.1, txt)
    pergunta(c, t, [(d10, ps("quanto mede", "i", 60) + [("cada ângulo?", "g", 66, COR)])], C["s11.a"])


def b_resposta2(c, t, C, b):
    a12, b12, c12, a13, b13 = C["s12.a"], C["s12.b"], C["s12.c"], C["s13.a"], C["s13.b"]
    A, B, Cc = I2A, I2B, I2C
    X = 1500
    q2_fig(c, t, C["s12"] - 1.2)
    canto(c, t, a12, Cc, A, B, "65°", E.COR, 70, size=50)
    canto(c, t, b12, B, A, Cc, "65°", E.COR, 70, size=50)
    canto(c, t, c12, A, B, Cc, "50°", AMBAR, 70, size=50, rl=80)
    if t >= a13:  # os de longe enchem o externo
        k = ep(t, a13, 0.4)
        for V in (A, B):
            c.drawCircle(*V, 26, M.paint(CERTO, 0.35 * k))
        ret = skia.Rect.MakeXYWH(Cc[0] - 120, Cc[1] - 120, 240, 240)
        c.drawArc(ret, 0, -115, False, M.paint(CERTO, k, stroke=10, cap_round=True))

    def um():
        fcen(c, t, a12, "180 − 115 = 65", X, 260, 76)
        E.frase(c, t, b12, ps("base iguais:", "i", 58) + [("B = 65°", "g", 64, COR)], X, 400, "center", 0.12)
        fcen(c, t, lerp(b12, c12, 0.5), "65 + 65 = 130", X, 540, 76)
        fcen(c, t, c12, "180 − 130 = 50", X, 680, 76, AMBAR)
        E.frase(c, t, c12 + 0.8, [("50°, 65° e 65°", "g", 64, CERTO)], X, 830, "center")
    E.saida(c, t, C["s13"] - 0.1, um)
    if t >= C["s13"]:
        E.frase(c, t, C["s13"], ps("conferindo:", "i", 60, COR), X, 260, "center", 0.12)
        E.frase(c, t, a13, ps("externo =", "i", 58) + [("soma dos de longe", "g", 58)], X, 400, "center", 0.12)
        fcen(c, t, b13, "50 + 65 = 115", X, 560, 84, CERTO)
        E.foco(c, t, b13 + 1.0, 0.4, lambda a: E.selo(c, X, 720, 56, True, a))


# ---------------- questão 3 ----------------
U3 = 50


def b_questao3(c, t, C, b):
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    X = 1500
    marca(c, t, a14, 3)
    k = ep(t, b14, 0.4)
    P5, P11 = ((200, 420), (200 + 5 * U3, 420)), ((200, 600), (200 + 11 * U3, 600))
    vareta(c, *P5, TINTA, k)
    vareta(c, *P11, TINTA, ep(t, b14 + 0.6, 0.4))
    E.foco(c, t, b14 + 0.2, 0.4, lambda a: centro(c, "5 m", meio(*P5)[0], 380, 56, "b", COR, a))
    E.foco(c, t, b14 + 0.8, 0.4, lambda a: centro(c, "11 m", meio(*P11)[0], 560, 56, "b", COR, a))
    E.foco(c, t, c14, 0.4, lambda a: (centro(c, "?", 200 + 5.5 * U3, 800, 90, "g", ERRADO, a), M.line(c, 200, 740, 200 + 11 * U3, 740, CINZA, a, 6, dash=[14, 12])))

    def txt():
        E.frase(c, t, a14 + 0.4, ps("terreno", "i", 62) + [("isósceles", "g", 70, COR)], X, 260, "center", 0.12)
        E.frase(c, t, b14, ps("dois lados:", "i", 58) + [("5 m e 11 m", "g", 64)], X, 400, "center", 0.12)
    E.saida(c, t, C["s15.a"] - 0.1, txt)
    pergunta(c, t, [(c14, ps("o", "i", 60) + [("terceiro lado?", "g", 64, COR)]), (d14, ps("e o", "i", 60) + [("perímetro?", "g", 64, COR)])], C["s15.a"])


def b_resposta3(c, t, C, b):
    a16, b16, c16, a17, b17, c17, d17 = C["s16.a"], C["s16.b"], C["s16.c"], C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    E.frase(c, t, C["s16"], ps("o terceiro repete um:", "i", 60), W / 2, 150, "center", 0.12)
    E.frase(c, t, a16, [("5", "g", 70, ERRADO if t >= c16 else COR)] + ps("ou", "i", 60) + [("11", "g", 70, CERTO if t >= b17 else COR)], W / 2, 240, "center", 0.12)
    # 5, 5 e 11: não fecha
    L, R = (140, 720), (140 + 11 * U3, 720)
    if t >= b16 - 0.8:
        k = ep(t, b16 - 0.8, 0.4)
        vareta(c, L, R, TINTA, k)
        Pa, Pb = pt(L, 5 * U3, 32), pt(R, 5 * U3, 148)
        vareta(c, L, Pa, ERRADO, k)
        vareta(c, R, Pb, ERRADO, k)
        M.line(c, *Pa, *Pb, ERRADO, k, 5, dash=[12, 10])
        E.foco(c, t, b16 - 0.4, 0.4, lambda a: (centro(c, "11", meio(L, R)[0], 800, 54, "b", COR, a),
                                                centro(c, "5", meio(L, Pa)[0] - 40, meio(L, Pa)[1] - 30, 54, "b", ERRADO, a),
                                                centro(c, "5", meio(R, Pb)[0] + 40, meio(R, Pb)[1] - 30, 54, "b", ERRADO, a)))
        fcen(c, t, b16, "5 + 5 = 10 < 11", meio(L, R)[0], 920, 66, ERRADO)
        E.foco(c, t, c16, 0.4, lambda a: (E.selo(c, meio(L, R)[0] - 200, 1010, 34, False, a),
                                          centro(c, "não fecha", meio(L, R)[0] + 30, 1028, 54, "g", ERRADO, a)))
    # 11, 11 e 5: fecha
    B2, C2 = (1240, 860), (1240 + 5 * U3, 860)
    A2 = (meio(B2, C2)[0], 860 - math.sqrt((11 * U3) ** 2 - (2.5 * U3) ** 2))
    if t >= a17 - 0.6:
        k = ep(t, a17 - 0.6, 0.4)
        triang(c, t, a17 - 0.6, A2, B2, C2, nomes=None)
        E.marcas_iguais(c, A2, B2, 1, TINTA, k)
        E.marcas_iguais(c, A2, C2, 1, TINTA, k)
        E.foco(c, t, a17 - 0.2, 0.4, lambda a: (centro(c, "5", meio(B2, C2)[0], 940, 54, "b", COR, a),
                                                centro(c, "11", A2[0] - 150, 600, 54, "b", COR, a),
                                                centro(c, "11", A2[0] + 150, 600, 54, "b", COR, a)))
        fcen(c, t, a17, "11 + 5 = 16 > 11", 1365, 1020, 60, CERTO)
    E.foco(c, t, b17, 0.4, lambda a: E.pilula(c, "terceiro lado: 11 m", 900, 380, 54, "g", fundo=CERTO, a=a))
    fcen(c, t, c17, "11 + 11 + 5 = 27", 900, 520, 64)
    bola_txt(c, t, c17 + 0.8, "27 m", 900, 680, 90, 56, CERTO)
    E.foco(c, t, d17, 0.4, lambda a: (centro(c, "21 m?", 900, 860, 60, "g", ERRADO, a)))
    if t >= d17 + 0.4:
        E.risco(c, 830, 860, 970, 820, t, d17 + 0.4, largura=10)
    E.frase(c, t, d17 + 0.6, ps("não testou", "i", 50, ERRADO), 900, 940, "center", 0.1)


# ---------------- questão 4 ----------------
I4A, I4B, I4C = (600, 230), (240, 860), (960, 860)
I4D = meio(I4B, I4C)


def q4_fig(c, t, t0, tb=None, td=None):
    A, B, Cc, D = I4A, I4B, I4C, I4D
    triang(c, t, t0, A, B, Cc)
    q = ep(t, tb if tb is not None else t0 + 0.6, 0.4)
    E.marcas_iguais(c, A, B, 1, TINTA, q)
    E.marcas_iguais(c, A, Cc, 1, TINTA, q)
    td = td if td is not None else t0 + 1.0
    if t >= td:
        M.line(c, *A, *D, E.COR, 1.0, 6, dash=[14, 10], progress=ease_io(prog(t, td, 0.6)))
        k = ease_back(prog(t, td + 0.5, 0.35))
        if k > 0:
            c.drawCircle(*D, 11 * k, M.paint(E.COR))
        E.foco(c, t, td + 0.5, 0.4, lambda a: centro(c, "D", D[0], D[1] + 80, 58, "g", COR, a))


def b_questao4(c, t, C, b):
    a18, b18, c18, d18, e18, f18 = (C[f"s18.{k}"] for k in "abcdef")
    A, B, Cc, D = I4A, I4B, I4C, I4D
    X = 1500
    marca(c, t, a18, 4)
    q4_fig(c, t, a18 + 0.3, tb=b18, td=d18)
    E.foco(c, t, c18, 0.4, lambda a: centro(c, "16 cm", D[0], D[1] + 150, 56, "b", COR, a * (1 - ep(t, d18, 0.3))))
    if t >= c18:
        E.chave(c, B[0], Cc[0], B[1] + 40, TINTA2, ep(t, c18, 0.4) * (1 - ep(t, d18, 0.3)), 18)
    metades(c, t, d18 + 0.3, A, B, Cc, E.COR, 100)
    E.foco(c, t, e18, 0.4, lambda a: centro(c, "?", (B[0] + D[0]) / 2, D[1] + 80, 64, "g", ERRADO, a))
    canto(c, t, f18, D, A, Cc, "?", ERRADO, 50, size=52, alfa=0.12)

    def txt():
        E.frase(c, t, b18, [("AB = AC", "g", 70)], X, 260, "center")
        E.frase(c, t, c18, [("BC = 16 cm", "g", 70)], X, 380, "center")
        E.frase(c, t, d18, ps("bissetriz de A até", "i", 56) + [("D", "g", 62, COR)], X, 500, "center", 0.12)
    E.saida(c, t, C["s19.a"] - 0.1, txt)
    pergunta(c, t, [(e18, [("BD = ?", "g", 66, COR)]), (f18, ps("ângulo com a base?", "i", 58) + [("?", "g", 66, ERRADO)])], C["s19.a"])


def b_resposta4(c, t, C, b):
    a20, b20, c20, d20, e20 = (C[f"s20.{k}"] for k in "abcde")
    a21, b21, c21 = C["s21.a"], C["s21.b"], C["s21.c"]
    A, B, Cc, D = I4A, I4B, I4C, I4D
    X = 1500
    if t >= a20:
        for pts, cor, t0 in (([A, B, D], E.COR, a20), ([A, Cc, D], AMBAR, a20 + 0.4)):
            path = skia.Path(); path.addPoly(pts, True)
            c.drawPath(path, M.paint(cor, 0.16 * ep(t, t0, 0.4)))
    q4_fig(c, t, C["s20"] - 1.2, td=C["s20"] - 1.0)
    k = ep(t, b20, 0.3) * (1 - ep(t, c20, 0.3))
    grosso(c, A, B, E.COR, k)
    grosso(c, A, Cc, AMBAR, k)
    metades(c, t, c20, A, B, Cc, E.COR, 100)
    grosso(c, A, D, TINTA2, ep(t, d20, 0.3) * (1 - ep(t, e20, 0.3)), 14)
    if t >= a21:
        E.foco(c, t, a21, 0.4, lambda a: (centro(c, "8", (B[0] + D[0]) / 2, D[1] + 80, 64, "b", CERTO, a),
                                          centro(c, "8", (D[0] + Cc[0]) / 2, D[1] + 80, 64, "b", CERTO, a)))
        q = ep(t, a21, 0.4)
        E.marcas_iguais(c, B, D, 2, CERTO, q)
        E.marcas_iguais(c, D, Cc, 2, CERTO, q)
    if t >= b21:
        E.angulo(c, t, b21, D, A, Cc, None, r=64, cor=CERTO, reto=True, preenche=0.2)
        E.angulo(c, t, b21 + 0.2, D, A, B, None, r=64, cor=CERTO, reto=True, preenche=0.2)

    def um():
        E.frase(c, t, a20, [("ABD", "g", 64, COR)] + ps("e", "i", 58) + [("ACD", "g", 64, AMBAR)], X, 240, "center", 0.12)
        E.frase(c, t, b20, [("L", "g", 66, COR)] + ps("AB = AC", "g", 58), X, 370, "center", 0.12)
        E.frase(c, t, c20, [("A", "g", 66, COR)] + ps("ângulo ao meio", "i", 56), X, 470, "center", 0.12)
        E.frase(c, t, d20, [("L", "g", 66, COR)] + ps("AD em comum", "i", 56), X, 570, "center", 0.12)
        E.foco(c, t, e20, 0.5, lambda a: E.pilula(c, "LAL: congruentes", X, 730, 64, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s21"] - 0.1, um)
    if t >= C["s21"]:
        fcen(c, t, a21, "16 ÷ 2 = 8", X, 280, 84, CERTO)
        E.frase(c, t, a21 + 0.8, [("BD = 8 cm", "g", 64, CERTO)], X, 390, "center")
        fcen(c, t, b21, "180 ÷ 2 = 90", X, 560, 76)
        E.frase(c, t, b21 + 0.8, [("90° cada", "g", 64, CERTO)], X, 660, "center")
        E.frase(c, t, c21, ps("a linha do topo:", "i", 54), X, 800, "center", 0.12)
        E.frase(c, t, c21 + 0.8, [("bissetriz, mediana e altura", "g", 50, COR)], X, 880, "center")


# ---------------- questão 5 ----------------
Q5A, Q5B, Q5C = (190, 580), (1060, 200), (1060, 960)
Q5M = meio(Q5B, Q5C)
Q5G = (Q5A[0] + 2 / 3 * (Q5M[0] - Q5A[0]), Q5A[1] + 2 / 3 * (Q5M[1] - Q5A[1]))


def q5_fig(c, t, t0, rot_v, rot_l, tv, tl, total=None, ttot=None):
    A, B, Cc, Mm, G = Q5A, Q5B, Q5C, Q5M, Q5G
    triang(c, t, t0, A, B, Cc, nomes="A  ")
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: centro(c, "M", Mm[0] + 55, Mm[1] + 22, 58, "g", TINTA, a))
    M.line(c, *A, *Mm, TINTA, ep(t, t0 + 0.4, 0.4), 6)
    grosso(c, A, G, E.COR, ep(t, tv, 0.4))
    grosso(c, G, Mm, TINTA2, ep(t, tl, 0.4))
    s_v = rot_v(t) if callable(rot_v) else rot_v
    s_l = rot_l(t) if callable(rot_l) else rot_l
    E.foco(c, t, tv + 0.2, 0.4, lambda a: txt_seg(c, A, G, s_v, 1, 56, COR, a))
    E.foco(c, t, tl + 0.2, 0.4, lambda a: txt_seg(c, G, Mm, s_l, 1, 56, TINTA2, a))
    if total:
        E.foco(c, t, ttot, 0.4, lambda a: txt_seg(c, A, Mm, total, -1, 64, CERTO if total != "?" else ERRADO, a, gap=40))
    if t >= t0 + 0.6:
        k = ease_back(prog(t, t0 + 0.6, 0.35))
        c.drawCircle(*G, 18 * k, M.paint(E.COR))
        c.drawCircle(*G, 7 * k, M.paint("#FFFFFF"))
        E.foco(c, t, t0 + 0.8, 0.4, lambda a: (c.drawCircle(G[0], G[1] + 66, 36, M.paint(PAPEL, 0.92 * a)),
                                               centro(c, "G", G[0], G[1] + 86, 56, "g", COR, a)))


def b_questao5(c, t, C, b):
    a22, b22, c22, d22, e22 = (C[f"s22.{k}"] for k in "abcde")
    X = 1500
    marca(c, t, a22, 5)
    q5_fig(c, t, a22 + 0.3, "3x − 2", "x + 1", c22, d22, "?", e22)

    def txt():
        E.frase(c, t, a22 + 0.4, [("mediana AM", "g", 66)], X, 260, "center")
        E.frase(c, t, b22, ps("baricentro", "i", 58) + [("G", "g", 66, COR)], X, 360, "center", 0.12)
        fcen(c, t, c22, "AG = 3x − 2", X, 500, 66, COR)
        fcen(c, t, d22, "GM = x + 1", X, 610, 66, TINTA2)
    E.saida(c, t, C["s23.a"] - 0.1, txt)
    pergunta(c, t, [(e22, ps("a mediana", "i", 60) + [("AM = ?", "g", 70, COR)])], C["s23.a"])


def b_resposta5(c, t, C, b):
    a24, b24, c24 = C["s24.a"], C["s24.b"], C["s24.c"]
    a25, b25, c25, d25 = C["s25.a"], C["s25.b"], C["s25.c"], C["s25.d"]
    a26, b26 = C["s26.a"], C["s26.b"]
    X = 1500
    t0 = C["s24"] - 1.2
    q5_fig(c, t, t0, (lambda tt: "10" if tt >= b25 else "3x − 2"), (lambda tt: "5" if tt >= c25 else "x + 1"), t0, t0,
           (lambda: "15" if t >= d25 else "?")(), t0)

    def um():
        E.frase(c, t, a24, ps("vértice =", "i", 58) + [("2 ×", "g", 64, COR)] + ps("lado", "i", 58), X, 240, "center", 0.12)
        fcen(c, t, b24, "3x − 2 = 2(x + 1)", X, 400, 72)
        fcen(c, t, c24, "3x − 2 = 2x + 2", X, 540, 72)
    E.saida(c, t, C["s25"] - 0.1, um)
    if C["s25"] <= t < C["s26"] + 0.4:
        def dois():
            bola_txt(c, t, a25, "x = 4", X, 280, 100, 56)
            fcen(c, t, b25, "AG = 3 · 4 − 2 = 10", X, 480, 64, COR)
            fcen(c, t, c25, "GM = 4 + 1 = 5", X, 600, 64, TINTA2)
            E.frase(c, t, c25 + 1.2, ps("10 é o dobro de 5:", "i", 54) + [("confere", "g", 56, CERTO)], X, 710, "center", 0.12)
            bola_txt(c, t, d25, "AM = 15", X, 880, 120, 54, CERTO)
        E.saida(c, t, C["s26"] - 0.1, dois)
    if t >= C["s26"]:
        E.frase(c, t, C["s26"], [("cuidado", "g", 76, ERRADO)] + ps("com a armadilha", "i", 60), X, 260, "center", 0.12)
        E.foco(c, t, a26, 0.4, lambda a: centro(c, "4", X, 480, 140, "g", ERRADO, a))
        if t >= a26 + 0.5:
            E.risco(c, X - 70, 470, X + 70, 400, t, a26 + 0.5, largura=12)
        E.frase(c, t, a26 + 0.5, ps("é o x, não a resposta", "i", 54, ERRADO), X, 580, "center", 0.1)
        E.frase(c, t, b26, ps("a mediana inteira:", "i", 58), X, 740, "center", 0.12)
        bola_txt(c, t, b26 + 0.6, "15", X, 890, 90, 72, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s27"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s27.a", "desenhe a figura"), ("s27.b", "marque o que é igual"), ("s27.c", "confira se faz sentido"))
        for i, (k, s) in enumerate(itens):
            y = 420 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 480, y - 30, 56, 64, a))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 580, y)
    E.saida(c, t, C["s28"] - 0.1, resumo)
    if t < C["s28"]:
        return
    E.frase(c, t, C["s28"] + 0.2, ps("próxima aula: uma parte nova", "i", 76), XE, 260, passo=0.1)
    E.frase(c, t, C["s28.a"], [("Teorema de Tales", "g", 110, COR)], XE, 420)
    E.frase(c, t, C["s28.b"], ps("3 e 6 numa reta,", "i", 64) + [("4 e x", "g", 68, COR)] + ps("na outra", "i", 64), XE, 560, passo=0.1)
    # três paralelas e duas transversais
    if t >= C["s28.a"]:
        q = ep(t, C["s28.a"] + 0.3, 0.5)
        for y in (640, 740, 940):
            M.line(c, 200, y, 980, y, TINTA, q, 5)
        M.line(c, 300, 600, 420, 980, TINTA2, q, 5)
        M.line(c, 700, 600, 940, 980, TINTA2, q, 5)
        E.foco(c, t, C["s28.b"] + 0.4, 0.4, lambda a: (centro(c, "3", 275, 710, 56, "b", COR, a), centro(c, "6", 320, 860, 56, "b", COR, a),
                                                       centro(c, "4", 835, 710, 56, "b", COR, a), centro(c, "x", 935, 860, 56, "b", COR, a)))
    E.foco(c, t, C["s28.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s28.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1630, p), lerp(720, 425, p), ep(t, C["s28.c"] + 0.2, 0.4))
    E.frase(c, t, C["s28.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], 1450, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, atalho=b_atalho,
              questao2=b_questao2, resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3,
              questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
