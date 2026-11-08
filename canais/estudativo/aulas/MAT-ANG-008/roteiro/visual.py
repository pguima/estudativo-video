"""Visual — Estudativo · MAT-ANG-008: altura, mediana, bissetriz e mediatriz.
Linguagem da geometria plana (MAT-ANG-001 a 007): lados em tinta; a linha da vez em COR (índigo), grossa; metades iguais com o mesmo
número de tracinhos (E.marcas_iguais); as duas metades de um ângulo com a mesma cor; ângulo reto = quadradinho; prolongamento de lado
tracejado em TINTA2. Erro em vermelho; certo em verde; medidas na grotesca; resposta na esfera.
Peças locais (as da MAT-ANG-004/007): tri(), canto(), triang(), rotulo(), cunha_m(); e ainda meio(), pe() (pé da perpendicular),
pe_bis() (onde a bissetriz chega), linha() (a linha da vez crescendo), reto() (quadradinho), metades() (ângulo dividido em dois)
e mini() (ícone de cada linha). Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-008_altura_mediana_bissetriz_mediatriz.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("mediana", "altura", "mediatriz", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
assert 10 / 2 == 5 and 80 / 2 == 40 and 40 / 2 == 20 and 180 - 40 == 140 and 140 / 2 == 70
assert 180 - 120 - 24 == 36 and 24 / 2 == 12 and 120 > 90


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


def tri(B, BC, gb, gc):
    """triângulo com a base BC deitada: ângulo gb em B e gc em C. Devolve A, B, C"""
    ga = 180 - gb - gc
    AB = BC * math.sin(math.radians(gc)) / math.sin(math.radians(ga))
    return pt(B, AB, gb), B, (B[0] + BC, B[1])


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


def metades(c, t, t0, V, P, Q, rot, cor=None, r=90, size=48, a=1.0, rl=None):
    """o ângulo PVQ dividido ao meio: duas cunhas iguais, da mesma cor, cada uma com a sua medida"""
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    g1, g2 = faixa_v(V, P, Q)
    gm = (g1 + g2) / 2
    q = ease_io(prog(t, t0, 0.5))
    cunha_m(c, V, g1, g1 + (gm - g1) * q, r, cor, a, alfa=0.3, borda=5)
    cunha_m(c, V, gm, gm + (g2 - gm) * q, r * 0.86, cor, a, alfa=0.3, borda=5)
    if rot:
        E.foco(c, t, t0 + 0.4, 0.4, lambda k: (rotulo(c, V, (g1 + gm) / 2, rl or r, rot, COR if cor == E.COR else cor, size, k * a),
                                              rotulo(c, V, (gm + g2) / 2, rl or r, rot, COR if cor == E.COR else cor, size, k * a)))


def triang(c, t, t0, A, B, C, nomes="ABC", tinta=TINTA, preenche=0.06, d=0.9, a=1.0):
    """o contorno que se desenha em volta, com os nomes dos vértices"""
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


def meio(P, Q):
    return (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2


def pe(P, Q1, Q2):
    """pé da perpendicular de P até a reta Q1Q2"""
    dx, dy = Q2[0] - Q1[0], Q2[1] - Q1[1]
    k = ((P[0] - Q1[0]) * dx + (P[1] - Q1[1]) * dy) / (dx * dx + dy * dy)
    return Q1[0] + k * dx, Q1[1] + k * dy


def pe_bis(A, B, Cc):
    """onde a bissetriz de A chega no lado BC (divide BC na razão AB : AC)"""
    ab, ac = math.dist(A, B), math.dist(A, Cc)
    k = ab / (ab + ac)
    return lerp(B[0], Cc[0], k), lerp(B[1], Cc[1], k)


def linha(c, t, t0, P, Q, cor=None, larg=8, d=0.7, a=1.0, dash=None):
    """a linha da vez, crescendo de P até Q"""
    if t >= t0 and a > 0:
        M.line(c, *P, *Q, cor or E.COR, a, larg, dash=dash, progress=ease_io(prog(t, t0, d)))
        k = ease_back(prog(t, t0 + d * 0.9, 0.35))
        if k > 0:
            c.drawCircle(*Q, 11 * k, M.paint(cor or E.COR, a))


def reto(c, t, t0, V, P, Q, cor=None, r=64, a=1.0):
    """quadradinho do ângulo reto PVQ"""
    if t >= t0 and a > 0:
        E.angulo(c, t, t0, V, P, Q, None, r=r, cor=cor or E.COR, reto=True, preenche=0.2 * a)


def txt_lado(c, P, Q, s, G, size=50, cor=None, a=1.0, gap=18):
    """medida de um lado, do lado de fora (longe de G)"""
    if a <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = meio(P, Q)
    if (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 < (mx - G[0]) ** 2 + (my - G[1]) ** 2:
        nx, ny = -nx, -ny
    E._cola(c, s, mx, my, nx, ny, gap, size, "b", cor or COR, a)


def grosso(c, P, Q, cor, a, larg=12):
    if a > 0:
        M.line(c, *P, *Q, cor, a, larg)


def ponto(c, P, cor, a, r=11):
    if a > 0:
        c.drawCircle(*P, r, M.paint(cor, a))


def mini(c, tipo, cx, cy, k, a=1.0, tinta=TINTA, cor=None):
    """ícone de cada linha no mesmo triângulo pequeno: "mediana", "bissetriz", "altura" ou "mediatriz\""""
    if a <= 0:
        return
    cor = cor or E.COR
    B, Cc, A = (cx - 150 * k, cy + 90 * k), (cx + 150 * k, cy + 90 * k), (cx - 40 * k, cy - 130 * k)
    path = skia.Path(); path.addPoly([A, B, Cc], True)
    c.drawPath(path, M.paint(E.COR, 0.06 * a))
    p = M.paint(tinta, a, stroke=5)
    p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, p)
    Mm = meio(B, Cc)
    if tipo == "mediana":
        M.line(c, *A, *Mm, cor, a, 7)
        E.marcas_iguais(c, B, Mm, 1, cor, a, tam=12, largura=4)
        E.marcas_iguais(c, Mm, Cc, 1, cor, a, tam=12, largura=4)
    elif tipo == "bissetriz":
        D = pe_bis(A, B, Cc)
        M.line(c, *A, *D, cor, a, 7)
        g1, g2 = faixa_v(A, B, Cc)
        gm = (g1 + g2) / 2
        cunha_m(c, A, g1, gm, 52 * k, cor, a, alfa=0.3, borda=4)
        cunha_m(c, A, gm, g2, 44 * k, cor, a, alfa=0.3, borda=4)
    elif tipo == "altura":
        Hh = pe(A, B, Cc)
        M.line(c, *A, *Hh, cor, a, 7)
        s = 22 * k
        M.line(c, Hh[0] + s, Hh[1], Hh[0] + s, Hh[1] - s, cor, a, 4)
        M.line(c, Hh[0], Hh[1] - s, Hh[0] + s, Hh[1] - s, cor, a, 4)
    else:
        M.line(c, Mm[0], cy - 150 * k, Mm[0], cy + 150 * k, cor, a, 7)
        s = 22 * k
        M.line(c, Mm[0] + s, Mm[1], Mm[0] + s, Mm[1] - s, cor, a, 4)
        M.line(c, Mm[0], Mm[1] - s, Mm[0] + s, Mm[1] - s, cor, a, 4)
        E.marcas_iguais(c, B, Mm, 1, cor, a, tam=12, largura=4)
        E.marcas_iguais(c, Mm, Cc, 1, cor, a, tam=12, largura=4)


# triângulo das três primeiras linhas: Â = 80°, B̂ = 55°, Ĉ = 45°, base BC = 10
TA, TB, TC = tri((200, 880), 760, 55, 45)
TG = ((TA[0] + TB[0] + TC[0]) / 3, (TA[1] + TB[1] + TC[1]) / 3)
NOMES = ("altura", "mediana", "bissetriz", "mediatriz")


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, ka, ps("4 linhas,", "i", 80) + [("4 nomes parecidos", "g", 80, COR)], W / 2, 190, "center", 0.12)
        for i, nome in enumerate(NOMES):
            x = 280 + i * 455
            t0 = lerp(kb, kc, 0.12 + 0.18 * i)
            E.foco(c, t, t0, 0.5, lambda a, nome=nome, x=x: mini(c, nome, x, 470, 1.15, a))
            E.frase(c, t, t0 + 0.1, [(nome, "g", 62)], x, 720, "center")
        E.frase(c, t, kc, ps("trocou uma pela outra?", "i", 66), W / 2, 870, "center", 0.12)
        E.frase(c, t, kc + 1.0, [("perde a questão", "g", 74, ERRADO)], W / 2, 980, "center")
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.25), [("traçar", "g", 96, COR)] + ps("cada uma", "i", 84), XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), ps("o que ela", "i", 84) + [("divide", "g", 90)], XE, 600, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.62), ps("ou", "i", 84) + [("corta", "g", 90)], XE, 730, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 820
    itens = (("s03.b", "o ângulo reto", "90°"), ("s03.c", "o isósceles", "2 lados iguais"), ("s03.d", "os casos de congruência", "LLL, LAL, ALA, LAAo"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 150 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 186, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 80)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 152)
    py = lerp(lerp(300, 540, ease_io(prog(t, C["s03.c"] - 0.35, 0.5))), 780, ease_io(prog(t, C["s03.d"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 940, "left", 0.12)


# ---------------- mediana ----------------
def b_mediana(c, t, C, b):
    A, B, Cc = TA, TB, TC
    Mm = meio(B, Cc)
    X = 1480
    a4, b4, c4, a5, b5, c5 = C["s04.a"], C["s04.b"], C["s04.c"], C["s05.a"], C["s05.b"], C["s05.c"]
    triang(c, t, C["s04"], A, B, Cc)
    tv = lerp(a4, b4, 0.3)
    if t >= tv:  # o vértice de onde ela sai
        k = 0.5 + 0.5 * math.sin(2 * math.pi * (t - tv) / 1.0)
        ponto(c, A, E.COR, ep(t, tv, 0.3) * (1 - ep(t, b4, 0.3)), 22 + 6 * k)
    linha(c, t, b4, A, Mm)
    E.foco(c, t, b4 + 0.6, 0.4, lambda a: centro(c, "M", Mm[0], Mm[1] + 80, 58, "g", COR, a))
    q = ep(t, c4, 0.4)
    E.marcas_iguais(c, B, Mm, 1, COR, q)
    E.marcas_iguais(c, Mm, Cc, 1, COR, q)
    if t >= a5:
        E.foco(c, t, a5, 0.4, lambda a: centro(c, "10", Mm[0], Mm[1] + 170, 60, "b", TINTA, a * (1 - ep(t, b5, 0.3))))
        if t < b5 + 0.3:
            E.chave(c, B[0], Cc[0], B[1] + 100, TINTA2, ep(t, a5, 0.5) * (1 - ep(t, b5, 0.3)), 18)
    if t >= b5:
        for P, Q in ((B, Mm), (Mm, Cc)):
            E.foco(c, t, b5, 0.4, lambda a, P=P, Q=Q: centro(c, "5", (P[0] + Q[0]) / 2, B[1] + 80, 60, "b", COR, a))

    def um():
        E.frase(c, t, a4, [("mediana", "g", 110, COR)], X, 260, "center")
        E.frase(c, t, tv, ps("sai de um", "i", 62) + [("vértice", "g", 64)], X, 390, "center", 0.12)
        E.frase(c, t, tv + 0.9, ps("(um canto)", "i", 50, TINTA2), X, 460, "center", 0.12)
        E.frase(c, t, b4, ps("até o", "i", 62) + [("ponto médio", "g", 64, COR)], X, 590, "center", 0.12)
        E.frase(c, t, b4 + 0.8, ps("do lado da frente", "i", 58), X, 670, "center", 0.12)
        E.frase(c, t, c4, ps("2 metades", "i", 62) + [("iguais", "g", 66, COR)], X, 820, "center", 0.12)
    E.saida(c, t, C["s05"] - 0.1, um)
    if t >= C["s05"]:
        fcen(c, t, a5, "BC = 10", X, 300, 84)
        fcen(c, t, b5, "10 ÷ 2 = 5", X, 450, 84, COR)
        E.foco(c, t, c5, 0.5, lambda a: E.pilula(c, "corta o lado ao meio", X, 640, 60, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, c5 + 0.3, [("mediana", "g", 66, COR)], X, 770, "center")


# ---------------- bissetriz ----------------
def b_bissetriz(c, t, C, b):
    A, B, Cc = TA, TB, TC
    D = pe_bis(A, B, Cc)
    X = 1480
    a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
    triang(c, t, C["s06"] - 0.5, A, B, Cc)
    canto(c, t, c6, A, B, Cc, "80°", AMBAR, 110, size=54, a=1 - ep(t, d6, 0.4))
    metades(c, t, d6, A, B, Cc, "40°", E.COR, 110, size=52, rl=120)
    linha(c, t, a6 + 0.6, A, D)
    E.frase(c, t, a6, [("bissetriz", "g", 110, COR)], X, 260, "center")
    E.frase(c, t, a6 + 0.6, ps("também sai de um", "i", 58) + [("vértice", "g", 60)], X, 380, "center", 0.12)
    E.frase(c, t, b6, ps("divide", "i", 62) + [("o ângulo", "g", 66, COR)] + ps("ao meio", "i", 62), X, 510, "center", 0.12)
    fcen(c, t, c6, "Â = 80°", X, 650, 76, AMBAR)
    fcen(c, t, d6, "80 ÷ 2 = 40", X, 780, 76, COR)
    E.frase(c, t, e6, ps("bis =", "i", 66) + [("dois", "g", 70, COR)], X, 920, "center", 0.12)


# ---------------- altura ----------------
def pessoa(c, x, y_chao, alt, a=1.0):
    """pessoa de pé e a fita que desce reta da cabeça até o chão"""
    if a <= 0:
        return
    cab = alt * 0.12
    topo = y_chao - alt
    c.drawCircle(x, topo + cab, cab, M.paint(TINTA2, a))
    M.rrect(c, x - alt * 0.13, topo + 2.2 * cab, alt * 0.26, alt * 0.42, 30, TINTA2, a)
    for dx in (-0.06, 0.06):
        M.line(c, x + alt * dx, topo + 2.2 * cab + alt * 0.38, x + alt * dx, y_chao, TINTA2, a, 18)
    M.line(c, x - alt * 0.3, y_chao, x + alt * 0.45, y_chao, TINTA, a, 5)


def b_altura(c, t, C, b):
    A, B, Cc = TA, TB, TC
    Hh = pe(A, B, Cc)
    X = 1560
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    triang(c, t, C["s07"], A, B, Cc)
    linha(c, t, a7 + 0.6, A, Hh)
    reto(c, t, b7, Hh, A, Cc)
    # a fita da pessoa
    if t >= c7:
        k = ep(t, c7, 0.4)
        xp, yc, alt = 1150, 880, 420
        pessoa(c, xp, yc, alt, k)
        xf = xp + 100
        q = ease_io(prog(t, c7 + 0.4, 0.8))
        M.line(c, xf, yc - alt, xf, yc - alt + alt * q, AMBAR, k, 6)
        for i in range(1, 8):
            yy = yc - alt + alt * i / 8
            if yy <= yc - alt + alt * q:
                M.line(c, xf - 12, yy, xf + 12, yy, AMBAR, k, 3)
        M.line(c, xp - 30, yc - alt, xf + 20, yc - alt, AMBAR, k, 4)
    E.foco(c, t, d7, 0.4, lambda a: centro(c, "h", (A[0] + Hh[0]) / 2 + 40, (A[1] + Hh[1]) / 2 + 20, 64, "g", COR, a))

    def txt():
        E.frase(c, t, a7, [("altura", "g", 110, COR)], X, 260, "center")
        E.frase(c, t, a7 + 0.6, ps("do vértice ao lado da frente", "i", 52), X, 370, "center", 0.1)
        E.frase(c, t, b7, ps("em", "i", 62) + [("ângulo reto", "g", 66, COR)], X, 490, "center", 0.12)
    E.saida(c, t, c7 - 0.1, txt)
    if t >= c7:
        E.frase(c, t, c7, ps("a fita desce", "i", 64) + [("reta", "g", 66, AMBAR)], X + 60, 300, "center", 0.12)
        E.frase(c, t, d7, ps("a distância do vértice", "i", 54), X + 60, 500, "center", 0.1)
        E.frase(c, t, d7 + 0.8, ps("até a", "i", 54) + [("reta do lado", "g", 58, COR)], X + 60, 580, "center", 0.12)


# ---------------- altura no obtusângulo ----------------
OA, OB, OC = (299, 337), (620, 720), (1120, 720)


def b_obtuso(c, t, C, b):
    A, B, Cc = OA, OB, OC
    Hh = pe(A, B, Cc)
    X = 1560
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    G = ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3)

    def fig():
        triang(c, t, C["s08"], A, B, Cc)
        canto(c, t, a8, B, A, Cc, None, AMBAR, 80, alfa=0.3)
        if t >= b8:  # a linha em ângulo reto não encontra o lado
            k = 1 - ep(t, d8, 0.3)
            M.line(c, *A, *Hh, ERRADO, k, 5, dash=[12, 10], progress=ease_io(prog(t, b8, 0.7)))
            E.foco(c, t, b8 + 0.7, 0.4, lambda a: centro(c, "não chega", Hh[0] + 20, Hh[1] + 80, 48, "b", ERRADO, a * k))
        if t >= c8:  # prolonga CB além de B
            M.line(c, *B, Hh[0] - 90, Hh[1], TINTA2, 1.0, 5, dash=E.TRACO, progress=ease_io(prog(t, c8, 0.7)))
        linha(c, t, d8, A, Hh)
        reto(c, t, d8 + 0.6, Hh, A, B)
        if t >= a9:  # a altura de C também cai fora; a de B, dentro
            Hc = pe(Cc, A, B)
            M.line(c, *A, Hc[0] + (Hc[0] - A[0]) * 0.15, Hc[1] + (Hc[1] - A[1]) * 0.15, TINTA2, 1.0, 5, dash=E.TRACO, progress=ease_io(prog(t, a9, 0.6)))
            linha(c, t, a9 + 0.6, Cc, Hc)
            reto(c, t, a9 + 1.2, Hc, Cc, A, r=40)
        if t >= b9:
            Hb = pe(B, A, Cc)
            linha(c, t, b9, B, Hb, CERTO)
            reto(c, t, b9 + 0.6, Hb, B, Cc, cor=CERTO, r=40)
    E.saida(c, t, c9 - 0.1, fig)

    def txt():
        E.frase(c, t, C["s08"], [("obtusângulo", "g", 76, AMBAR)], X, 220, "center")
        E.frase(c, t, C["s08"] + 0.6, ps("um ângulo maior que", "i", 52) + [("90°", "g", 54)], X, 300, "center", 0.1)
        E.frase(c, t, b8, ps("de A, em ângulo reto:", "i", 56), X, 430, "center", 0.12)
        E.frase(c, t, b8 + 0.8, [("não chega em BC", "g", 58, ERRADO)], X, 510, "center")
        E.frase(c, t, c8, [("prolongue", "g", 62)] + ps("o lado", "i", 58), X, 640, "center", 0.12)
        E.frase(c, t, d8, ps("a altura", "i", 62) + [("cai fora", "g", 70, COR)], X, 790, "center", 0.12)
    E.saida(c, t, C["s09"] - 0.1, txt)
    if t >= C["s09"]:
        def txt2():
            E.frase(c, t, a9, ps("dos ângulos agudos:", "i", 58), X, 300, "center", 0.12)
            E.frase(c, t, a9 + 0.8, [("fora", "g", 76, COR)], X, 400, "center")
            E.frase(c, t, b9, ps("do ângulo obtuso:", "i", 58), X, 560, "center", 0.12)
            E.frase(c, t, b9 + 0.8, [("dentro", "g", 76, CERTO)], X, 660, "center")
        E.saida(c, t, c9 - 0.1, txt2)
    if t >= c9:  # no retângulo, os lados do ângulo reto já são alturas
        R1, R2, R3 = (360, 860), (1060, 860), (360, 360)
        triang(c, t, c9, R3, R1, R2, nomes=None)
        reto(c, t, c9 + 0.5, R1, R2, R3, r=60)
        grosso(c, R1, R2, E.COR, ep(t, c9 + 0.8, 0.4))
        grosso(c, R1, R3, E.COR, ep(t, c9 + 1.1, 0.4))
        E.frase(c, t, c9, [("retângulo", "g", 76, COR)], X, 380, "center")
        E.frase(c, t, c9 + 0.8, ps("os lados do", "i", 58) + [("reto", "g", 62)], X, 520, "center", 0.12)
        E.frase(c, t, c9 + 1.4, ps("já são", "i", 58) + [("alturas", "g", 66, COR)], X, 610, "center", 0.12)


# ---------------- mediatriz ----------------
MA, MB, MC = (300, 800), (1000, 800), (840, 330)


def b_mediatriz(c, t, C, b):
    A, B, Cc = MA, MB, MC
    Mm = meio(A, B)
    P = (Mm[0], 360)
    X = 1520
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    a11, b11, c11, d11, e11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"]
    some_c = 1 - ep(t, C["s11"], 0.5)
    if some_c > 0:  # o triângulo some e fica só o lado AB
        triang(c, t, C["s10"], A, B, Cc, nomes="AB ", a=some_c)
    if t >= C["s11"]:
        M.line(c, *A, *B, TINTA, 1.0, 6)
        for V, s in ((A, "A"), (B, "B")):
            centro(c, s, V[0] + (-60 if s == "A" else 60), V[1] + 22, 58, "g", TINTA)
    if t >= b10:  # nenhum vértice
        k = ep(t, b10, 0.3) * (1 - ep(t, c10, 0.3))
        for V in (A, B, Cc):
            c.drawCircle(*V, 26, M.paint(TINTA2, 0.35 * k))
    q = ep(t, c10, 0.4)
    ponto(c, Mm, E.COR, q)
    E.marcas_iguais(c, A, Mm, 1, COR, q)
    E.marcas_iguais(c, Mm, B, 1, COR, q)
    E.foco(c, t, c10 + 0.3, 0.4, lambda a: centro(c, "M", Mm[0] - 50, Mm[1] + 70, 56, "g", COR, a))
    if t >= d10:
        p = ease_io(prog(t, d10, 0.8))
        M.line(c, Mm[0], Mm[1] - 560 * p, Mm[0], Mm[1] + 220 * p, E.COR, 1.0, 8)
        reto(c, t, d10 + 0.5, Mm, (Mm[0], Mm[1] - 100), B)
    # o ponto P na mediatriz e as ligações
    if t >= b11:
        ponto(c, P, TINTA, ease_back(prog(t, b11, 0.35)), 14)
        E.foco(c, t, b11 + 0.2, 0.4, lambda a: centro(c, "P", P[0] - 50, P[1] + 10, 58, "g", TINTA, a))
        for Q in (A, B):
            M.line(c, *P, *Q, TINTA, 1.0, 6, progress=ease_io(prog(t, b11 + 0.4, 0.6)))
    if t >= c11:
        k = ep(t, c11, 0.4) * (1 - ep(t, e11, 0.3))
        grosso(c, P, Mm, AMBAR, k, 12)
        grosso(c, A, Mm, E.COR, k, 10)
        grosso(c, Mm, B, E.COR, k, 10)
    q = ep(t, e11, 0.4)
    E.marcas_iguais(c, P, A, 2, TINTA, q)
    E.marcas_iguais(c, P, B, 2, TINTA, q)

    def um():
        E.frase(c, t, a10, [("mediatriz", "g", 110, COR)], X, 260, "center")
        E.frase(c, t, b10, ps("não precisa", "i", 58) + [("de vértice", "g", 60)], X, 380, "center", 0.12)
        E.frase(c, t, c10, ps("passa pelo", "i", 58) + [("ponto médio", "g", 60, COR)], X, 520, "center", 0.12)
        E.frase(c, t, d10, ps("em", "i", 58) + [("ângulo reto", "g", 60, COR)], X, 620, "center", 0.12)
        E.frase(c, t, lerp(d10, C["s10.end"], 0.4), ps("corta o lado ao meio,", "i", 56), X, 760, "center", 0.1)
        E.frase(c, t, lerp(d10, C["s10.end"], 0.6), [("em pé", "g", 64, COR)], X, 850, "center")
    E.saida(c, t, C["s11"] - 0.1, um)
    if t >= C["s11"]:
        E.frase(c, t, a11, ps("qualquer ponto dela:", "i", 58), X, 230, "center", 0.12)
        E.frase(c, t, a11 + 1.0, [("mesma distância", "g", 62, COR)], X, 320, "center")
        E.frase(c, t, a11 + 1.6, ps("das pontas", "i", 58), X, 400, "center", 0.12)
        E.frase(c, t, c11, ps("metades,", "i", 54) + [("reto", "g", 56, COR)] + ps("e", "i", 54) + [("PM", "g", 56, AMBAR)], X, 540, "center", 0.12)
        E.foco(c, t, d11, 0.5, lambda a: E.pilula(c, "LAL", X, 680, 84, "g", a=a, cor=E.SOBRE))
        fcen(c, t, e11, "PA = PB", X, 860, 90, COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    B, Cc, A = (200, 780), (1000, 780), (330, 380)
    D = pe_bis(A, B, Cc)
    Mm = meio(B, Cc)
    X = 1520
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    E.frase(c, t, C["s12"], [("cuidado", "g", 90, ERRADO)] + ps("com este erro", "i", 84), W / 2, 150, "center", 0.12)
    triang(c, t, C["s12"] + 0.4, A, B, Cc)
    metades(c, t, a12, A, B, Cc, None, E.COR, 100)
    linha(c, t, a12 + 0.3, A, D)
    E.foco(c, t, a12 + 1.0, 0.4, lambda a: centro(c, "bissetriz", D[0] - 30, D[1] + 80, 46, "b", COR, a))
    if t >= b12:  # o ponto médio de verdade
        q = ep(t, b12, 0.4)
        M.line(c, *A, *Mm, TINTA2, q, 4, dash=[12, 10])
        ponto(c, Mm, TINTA2, q)
        E.marcas_iguais(c, B, Mm, 1, TINTA2, q)
        E.marcas_iguais(c, Mm, Cc, 1, TINTA2, q)
        E.foco(c, t, b12 + 0.3, 0.4, lambda a: centro(c, "meio", Mm[0] + 30, Mm[1] + 80, 46, "b", TINTA2, a))
    if t >= c12:
        E.chave(c, D[0], Mm[0], D[1] + 130, ERRADO, ep(t, c12, 0.5), 22)
        E.foco(c, t, c12 + 0.4, 0.4, lambda a: centro(c, "longe", (D[0] + Mm[0]) / 2, D[1] + 205, 50, "g", ERRADO, a))
    E.frase(c, t, a12, ps("a bissetriz cai", "i", 60), X, 330, "center", 0.12)
    E.frase(c, t, a12 + 0.8, [("no meio do lado?", "g", 62)], X, 420, "center")
    E.foco(c, t, b12, 0.5, lambda a: E.pilula(c, "em geral, não", X, 560, 66, "g", fundo=ERRADO, a=a))
    E.frase(c, t, c12, ps("lado comprido:", "i", 56) + [("vai longe", "g", 58, ERRADO)], X, 690, "center", 0.12)
    E.frase(c, t, d12, ps("ângulo ao meio", "i", 58), X, 820, "center", 0.12)
    E.frase(c, t, d12 + 0.8, [("≠ lado ao meio", "g", 64, ERRADO)], X, 910, "center")


# ---------------- atalho (palco escuro) ----------------
IB, IC = (400, 900), (920, 900)
IA = (660, 900 - 260 * math.tan(math.radians(70)))


def b_atalho(c, t, C, b):
    palco(c, t)
    A, B, Cc = IA, IB, IC
    Mm = meio(B, Cc)
    X = 1500
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    a15, b15, c15, d15, e15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]
    G = ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3)
    fig_a = 1 - ep(t, d15, 0.4) * 0.75
    triang(c, t, C["s13"], A, B, Cc, nomes="A  ", tinta=BR, preenche=0.12, a=fig_a)
    q = ep(t, C["s13"] + 0.8, 0.4) * fig_a
    E.marcas_iguais(c, A, B, 1, BR, q)
    E.marcas_iguais(c, A, Cc, 1, BR, q)
    linha(c, t, b13, A, Mm, CLARO, a=fig_a)
    if t >= c13:  # continua: mediatriz da base
        M.line(c, Mm[0], Mm[1], Mm[0], Mm[1] + 70, CLARO, fig_a, 6, dash=E.TRACO, progress=ease_io(prog(t, c13, 0.5)))
    canto(c, t, a14, A, B, Cc, "40°", AMBAR, 150, size=50, a=(1 - ep(t, b14, 0.4)) * fig_a)
    metades(c, t, b14, A, B, Cc, "20°", CLARO, 150, size=46, a=fig_a, rl=270)
    E.foco(c, t, a14 + 0.4, 0.4, lambda a: centro(c, "10", Mm[0], B[1] + 140, 56, "b", BR, a * (1 - ep(t, c14, 0.3)) * fig_a))
    if t >= c14:
        q = ep(t, c14, 0.4) * fig_a
        E.marcas_iguais(c, B, Mm, 2, CLARO, q)
        E.marcas_iguais(c, Mm, Cc, 2, CLARO, q)
        for P in (B, Cc):
            centro(c, "5", (P[0] + Mm[0]) / 2, B[1] + 80, 56, "b", CLARO, q)
    reto(c, t, d14, Mm, A, Cc, cor=CLARO, a=fig_a)
    if t >= a15:
        k = ep(t, a15, 0.4) * (1 - ep(t, c15 + 1.0, 0.4))
        grosso(c, A, B, AMBAR, k, 10)
        grosso(c, A, Cc, AMBAR, k, 10)
    if t >= b15:
        grosso(c, A, Mm, AMBAR, ep(t, b15, 0.4) * (1 - ep(t, c15 + 1.0, 0.4)), 12)
    # nos vértices da base, cada linha vai para um lugar
    if t >= d15:
        Mac = meio(A, Cc)
        Dac = pe_bis(B, A, Cc)
        Hac = pe(B, A, Cc)
        for P, cor, t0, nome in ((Hac, CERTO, d15 + 0.3, "altura"), (Dac, AMBAR, d15 + 0.8, "bissetriz"), (Mac, BR, d15 + 1.3, "mediana")):
            linha(c, t, t0, B, P, cor, larg=7)

    def um():
        E.frase(c, t, a13, ps("no", "i", 62, CLARO) + [("isósceles", "g", 72, BR)], X, 250, "center", 0.12)
        E.frase(c, t, a13 + 0.8, ps("a linha do topo", "i", 58, CLARO) + [("faz tudo", "g", 62, BR)], X, 340, "center", 0.12)
        for i, s in enumerate(("altura", "mediana", "bissetriz")):
            E.foco(c, t, b13 + 0.5 + 0.35 * i, 0.4, lambda a, s=s, i=i: E.pilula(c, s, X, 480 + i * 110, 56, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, c13, ps("+ mediatriz", "i", 58, CLARO) + [("da base", "g", 60, BR)], X, 840, "center", 0.12)
    E.saida(c, t, C["s14"] - 0.1, um)
    if C["s14"] <= t:
        def dois():
            E.frase(c, t, a14, ps("topo", "i", 60, CLARO) + [("40°", "g", 70, AMBAR)] + ps("base", "i", 60, CLARO) + [("10", "g", 70, BR)], X, 260, "center", 0.12)
            fcen(c, t, b14, "40 ÷ 2 = 20", X, 420, 76, CLARO)
            fcen(c, t, c14, "10 ÷ 2 = 5", X, 560, 76, CLARO)
            E.frase(c, t, d14, ps("na base:", "i", 60, CLARO) + [("90°", "g", 76, BR)], X, 720, "center", 0.12)
        E.saida(c, t, C["s15"] - 0.1, dois)
    if C["s15"] <= t:
        def tres():
            E.frase(c, t, C["s15"], ps("por congruência:", "i", 58, CLARO), X, 240, "center", 0.12)
            E.frase(c, t, a15, [("lados iguais", "g", 60, AMBAR)], X, 340, "center")
            E.frase(c, t, a15 + 1.6, [("metades da base", "g", 60, CLARO)], X, 430, "center")
            E.frase(c, t, b15, [("lado em comum", "g", 60, AMBAR)], X, 520, "center")
            E.foco(c, t, c15, 0.5, lambda a: E.pilula(c, "LLL", X, 670, 84, "g", a=a, cor=E.SOBRE))
            E.frase(c, t, c15 + 0.5, ps("metades iguais", "i", 56, CLARO), X, 790, "center", 0.12)
        E.saida(c, t, d15 - 0.1, tres)
    if t >= d15:
        E.frase(c, t, d15, ps("nos vértices da base:", "i", 58, CLARO), X, 260, "center", 0.12)
        for i, (s, cor) in enumerate((("altura", CERTO), ("bissetriz", AMBAR), ("mediana", BR))):
            E.frase(c, t, d15 + 0.3 + 0.5 * i, [(s, "g", 58, cor)], X, 370 + i * 80, "center")
        E.frase(c, t, e15, ps("cada uma num", "i", 58, CLARO) + [("lugar", "g", 62, BR)], X, 680, "center", 0.12)
        E.frase(c, t, lerp(e15, C["s15.end"], 0.45), ps("equilátero:", "i", 58, CLARO) + [("vale nos 3", "g", 62, BR)], X, 860, "center", 0.12)


# ---------------- questão ----------------
QC_, QB_ = (120, 900), (640, 900)
QA_ = pt(QB_, 520 * math.sin(math.radians(36)) / math.sin(math.radians(24)), 60)


def b_questao(c, t, C, b):
    A, B, Cc = QA_, QB_, QC_
    X = 1490
    a16, b16, c16, d16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    triang(c, t, C["s16"], A, B, Cc)
    canto(c, t, a16, B, A, Cc, None, TINTA2, 70)
    E.foco(c, t, a16 + 0.3, 0.4, lambda a: centro(c, "120°", B[0] + 5, B[1] - 105, 50, "b", TINTA2, a))
    canto(c, t, b16, A, B, Cc, "24°", E.COR, 110, size=50, rl=140)
    if t >= c16:
        D = pe_bis(A, B, Cc)
        M.line(c, *A, *D, E.COR, 1.0, 5, dash=[12, 10], progress=ease_io(prog(t, c16, 0.6)))
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), X, 160, "center", 0.12)
    E.frase(c, t, c16, ps("bissetriz de A:", "i", 58) + [("? e ?", "g", 64, COR)], X, 880, "center", 0.12)
    E.frase(c, t, d16, ps("altura de A:", "i", 58) + [("dentro ou fora?", "g", 60)], X, 990, "center", 0.12)
    E.relogio(c, t, C["s17.a"], cy=470, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    A, B, Cc = QA_, QB_, QC_
    Hh = pe(A, B, Cc)
    D = pe_bis(A, B, Cc)
    X = 1500
    a18, b18, a19, b19, c19 = C["s18.a"], C["s18.b"], C["s19.a"], C["s19.b"], C["s19.c"]
    triang(c, t, C["s18"] - 1.5, A, B, Cc)
    canto(c, t, C["s18"] - 1.5, B, A, Cc, None, AMBAR if t >= a19 else TINTA2, 70)
    centro(c, "120°", B[0] + 5, B[1] - 105, 50, "b", AMBAR if t >= a19 else TINTA2)
    canto(c, t, C["s18"] - 1.5, A, B, Cc, "24°", E.COR, 110, size=50, rl=140, a=1 - ep(t, b18, 0.4))
    metades(c, t, b18, A, B, Cc, None, E.COR, 160)
    linha(c, t, a18, A, D)
    if t >= c19 - 1.5:
        M.line(c, *B, Hh[0] + 90, Hh[1], TINTA2, 1.0, 5, dash=E.TRACO, progress=ease_io(prog(t, c19 - 1.5, 0.6)))
    linha(c, t, c19 - 0.6, A, Hh, CERTO)
    reto(c, t, c19, Hh, A, B, cor=CERTO)

    def um():
        fcen(c, t, a18, "24 ÷ 2 = 12", X, 300, 84)
        bola_txt(c, t, b18, "12° e 12°", X, 520, 150, 60)
    E.saida(c, t, C["s19"] - 0.1, um)
    if t >= C["s19"]:
        E.frase(c, t, a19, [("120° > 90°", "g", 70, AMBAR)], X, 260, "center")
        E.frase(c, t, a19 + 0.8, [("obtusângulo", "g", 70)], X, 360, "center")
        E.frase(c, t, b19, ps("A não é o obtuso:", "i", 58), X, 510, "center", 0.12)
        E.foco(c, t, b19 + 0.8, 0.5, lambda a: E.pilula(c, "a altura cai fora", X, 640, 64, "g", fundo=CERTO, a=a))
        E.frase(c, t, c19 - 1.5, ps("prolongue CB além do B", "i", 54), X, 790, "center", 0.1)
        E.frase(c, t, c19, ps("e desça em", "i", 56) + [("ângulo reto", "g", 60, CERTO)], X, 880, "center", 0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 160, "center")
        itens = (("s20.a", "mediana", "o lado ao meio"), ("s20.b", "bissetriz", "o ângulo ao meio"),
                 ("s20.c", "altura", "chega em ângulo reto"), ("s20.d", "mediatriz", "lado ao meio, em ângulo reto"))
        for i, (k, nome, s) in enumerate(itens):
            y = 330 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, nome=nome, y=y: mini(c, nome, 320, y - 30, 0.62, a))
            E.frase(c, t, C[k], [(nome, "g", 70, COR)], 480, y)
            E.frase(c, t, C[k] + 0.4, ps(s, "i", 62), 950, y, "left", 0.08)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.2, ps("próxima aula", "i", 84), XE, 260)
    E.frase(c, t, C["s21.a"], ps("cada linha", "i", 76) + [("3 vezes", "g", 96, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s21.b"], ps("se cruzam", "i", 76) + [("num ponto só", "g", 84)], XE, 530, passo=0.14)
    E.frase(c, t, C["s21.c"], [("baricentro", "g", 110, COR)], XE, 690)
    E.frase(c, t, C["s21.c"] + 1.2, ps("um pedaço com o", "i", 62) + [("dobro", "g", 66)] + ps("do outro", "i", 62), XE, 790, passo=0.12)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1630, p), lerp(720, 425, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 970, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, mediana=b_mediana, bissetriz=b_bissetriz, altura=b_altura, obtuso=b_obtuso,
              mediatriz=b_mediatriz, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
