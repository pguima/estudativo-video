"""Visual — Estudativo · MAT-POL-008: cordas que se cruzam e secantes (3 · 8 = 4 · x dá x = 6; 2 · 18 = 4 · 9; tangente 6).
Linguagem da geometria plana (MAT-ANG-001 a 020, MAT-POL-001 e 007): linhas em tinta; o pedaço da vez em cor forte por cima;
os pedaços de uma corda em COR (índigo) e os da outra em TINTA2; na secante, o pedaço de fora em COR e a inteira com a linha
de cota em TINTA2; ângulos iguais com a mesma cor; medidas na grotesca; resposta na esfera; erro em vermelho, certo em verde;
atalho no palco escuro. As figuras são de verdade: as cordas cortam a circunferência nos pedaços 3, 8, 4 e 6 (raio √33 e
P a 3 do centro); nas secantes, P está a 10 do centro, o raio é 8, e a segunda secante corta em 4 e 9. A figura não mente.
"A secante gira até só encostar": a reta gira em volta de P e os dois pontos de corte correm um para o outro até virarem um.
Peças locais: ps(), fcen(), bola_txt(), lin(), ponto(), rot() (rótulo ao lado de um segmento), tri_cheio(), cortes()
(onde a reta que sai de P corta a circunferência), circ() (circunferência que também serve no palco), cota() e seta_p().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polígonos e Círculo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POL-008_cordas_que_se_cruzam_e_secantes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("cordas", "porque", "secantes", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 3 * 8 == 4 * 6 == 24 and 2 * (2 + 16) == 4 * 9 == 36 == 6 ** 2 and 9 - 4 == 5
assert 2 * 16 == 32 == 4 * 8
assert 4 * (4 + 21) == 5 * 20 == 100 == 10 ** 2 and 20 - 5 == 15 and 4 * 21 == 84 and 84 % 5 != 0


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


def lin(c, t, t0, P, Q, cor=TINTA, larg=6, d=0.6, a=1.0, dash=None):
    if t >= t0 and a > 0:
        M.line(c, *P, *Q, cor, a, larg, dash=dash, progress=ease_io(prog(t, t0, d)))


def ponto(c, t, t0, P, cor=TINTA, r=12, pulsa=False):
    k = ease_back(prog(t, t0, 0.35))
    if k <= 0:
        return
    if pulsa:
        k *= 1 + 0.45 * math.sin(math.pi * M.clamp(prog(t, t0 + 0.2, 0.8)))
    c.drawCircle(*P, r * k, M.paint(cor))


def rot(c, t, t0, s, P, Q, lado=1, cor=None, size=58, gap=16, onde=0.5):
    """rótulo ao lado do segmento PQ (lado = 1 ou −1)"""
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy * lado, -ux * lado
    mx, my = lerp(P[0], Q[0], onde), lerp(P[1], Q[1], onde)
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, s, mx, my, nx, ny, gap, size, "b", cor or COR, a))


def nome(c, t, t0, s, P, nx, ny, cor=TINTA, size=60, gap=14):
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, s, *P, nx, ny, gap, size, "g", cor, a))


def tri_cheio(c, pts, cor, a=1.0, alfa=0.2):
    if a <= 0:
        return
    path = skia.Path(); path.addPoly([tuple(p) for p in pts], True)
    c.drawPath(path, M.paint(cor, alfa * a))


def em(P, u, d):
    return P[0] + u[0] * d, P[1] + u[1] * d


def dirg(g):
    """vetor unitário no ângulo g (graus, anti-horário, como na matemática)"""
    return math.cos(math.radians(g)), -math.sin(math.radians(g))


def cortes(O, R, P, u):
    """distâncias de P, na direção u, até os dois cortes com a circunferência (None se não corta)"""
    wx, wy = O[0] - P[0], O[1] - P[1]
    b = wx * u[0] + wy * u[1]
    disc = b * b - (wx * wx + wy * wy - R * R)
    if disc < -400:
        return None
    disc = max(disc, 0.0)
    r = math.sqrt(disc)
    return b - r, b + r


def circ(c, t, t0, O, R, tinta=TINTA, d=0.8, larg=6, centro_=True):
    if t < t0:
        return
    ret = skia.Rect.MakeXYWH(O[0] - R, O[1] - R, 2 * R, 2 * R)
    c.drawArc(ret, 0, -360 * ease_io(prog(t, t0, d)), False, M.paint(tinta, 1.0, stroke=larg, cap_round=True))
    if centro_:
        ponto(c, t, t0 + d * 0.5, O, tinta, 9)


def cota(c, t, t0, P, Q, rotulo, lado=1, cor=TINTA2, off=46, size=54, rcor=None):
    """linha de cota paralela a PQ, afastada, com tracinhos nas pontas e o rótulo no meio"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy * lado, -ux * lado
    a0, b0 = (P[0] + nx * off, P[1] + ny * off), (Q[0] + nx * off, Q[1] + ny * off)
    M.line(c, *a0, *b0, cor, q, 4, progress=ease_io(prog(t, t0, 0.6)))
    for X in (a0, b0):
        M.line(c, X[0] - nx * 14, X[1] - ny * 14, X[0] + nx * 14, X[1] + ny * 14, cor, q, 4)
    if rotulo:
        E.foco(c, t, t0 + 0.4, 0.4, lambda a: E._cola(c, rotulo, (a0[0] + b0[0]) / 2, (a0[1] + b0[1]) / 2, nx, ny, 10, size, "b", rcor or cor, a))


# ---------------- figura das cordas: raio √33, P a 3 do centro ----------------
FO, FK = (560, 560), 58
FR = math.sqrt(33) * FK
_p = dirg(250)                                   # de O para P
FP = em(FO, _p, 3 * FK)
_g = math.degrees(math.atan2(-_p[1], _p[0]))
FU = dirg(_g + math.degrees(math.acos(-2.5 / 3)))  # corda AB: A = P − 3u, B = P + 8u
FV = dirg(_g - math.degrees(math.acos(-1 / 3)))    # corda CD: C = P − 4v, D = P + 6v
FA, FB = em(FP, FU, -3 * FK), em(FP, FU, 8 * FK)
FC, FD = em(FP, FV, -4 * FK), em(FP, FV, 6 * FK)
for _X in (FA, FB, FC, FD):
    assert abs(math.dist(_X, FO) - FR) < 0.5


def _fora(P):
    return P[0] - FO[0], P[1] - FO[1]


def fig_cordas(c, t, t0, t_ab, t_cd, t_nomes=None, cores=False, a_cor=1.0):
    circ(c, t, t0, FO, FR, centro_=False)
    lin(c, t, t_ab, FA, FB, TINTA, 7, 0.6)
    lin(c, t, t_cd, FC, FD, TINTA, 7, 0.6)
    if cores and t >= cores:
        q = ep(t, cores, 0.4) * a_cor
        M.line(c, *FP, *FA, E.COR, q, 11); M.line(c, *FP, *FB, E.COR, q, 11)
        M.line(c, *FP, *FC, TINTA2, q, 11); M.line(c, *FP, *FD, TINTA2, q, 11)
    for X, tt in ((FA, t_ab), (FB, t_ab + 0.5), (FC, t_cd), (FD, t_cd + 0.5)):
        ponto(c, t, tt, X, TINTA, 11)
    ponto(c, t, t_cd + 0.4, FP, TINTA, 13)
    if t_nomes is not None:
        for s, X in (("A", FA), ("B", FB), ("C", FC), ("D", FD)):
            nome(c, t, t_nomes, s, X, *_fora(X))
        nome(c, t, t_nomes, "P", FP, -1, 0.05, gap=30)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    X = 1040

    def um():
        fig_cordas(c, t, ka, ka + 0.5, ka + 1.0, cores=kb)
        rot(c, t, kb, "3", FP, FA, 1, COR, 64)
        rot(c, t, kb + 0.3, "8", FP, FB, -1, COR, 64)
        rot(c, t, kc, "4", FP, FC, -1, TINTA2, 64)
        E.saida(c, t, kd, lambda: rot(c, t, kc + 0.4, "?", FP, FD, 1, TINTA2, 72))
        rot(c, t, kd + 0.1, "6", FP, FD, 1, CERTO, 72)
        E.frase(c, t, ka, ps("duas cordas", "i", 80) + [("se cruzam", "g", 84, COR)], X, 250, passo=0.14)
        E.frase(c, t, kb, ps("uma:", "i", 70) + [("3", "g", 84, COR), ("e", "i", 70), ("8", "g", 84, COR)], X, 400, passo=0.14)
        E.frase(c, t, kc, ps("a outra:", "i", 70) + [("4", "g", 84, TINTA2), ("e", "i", 70), ("?", "g", 84, TINTA2)], X, 530, passo=0.14)
        E.frase(c, t, kd - 0.6, ps("sem régua:", "i", 70), X, 720, passo=0.14)
        bola_txt(c, t, kd, "6 cm", X + 460, 700, 110, 80, CERTO)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1530, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), ps("o pedaço", "i", 90) + [("que falta", "g", 96, COR)], XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("em", "i", 90) + [("cordas", "g", 96, COR)], XE, 590, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.75), ps("e em", "i", 90) + [("secantes", "g", 96, COR)], XE, 730, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1530, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1530, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "dois ângulos iguais:", "semelhantes", "lados proporcionais", 150),
             ("s03.c", "ângulo inscrito:", "metade do central", "do mesmo arco", 500))
    for k, l1, l2, l3, y in itens:
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 300, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 80)
        E.frase(c, t, C[k] + 0.6, [(l2, "g", 64, COR)], x + 44, y + 170)
        E.frase(c, t, C[k] + 1.4, [(l3, "i", 58)], x + 44, y + 260)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(150 + 270, 500 + 270, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 930, "left", 0.12)


# ---------------- cordas ----------------
def b_cordas(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    X = 1440
    fig_cordas(c, t, C["s04"], a4, b4, t_nomes=b4 + 0.6, cores=c4)
    ponto(c, t, b4 + 0.4, FP, E.COR, 15, pulsa=True)
    rot(c, t, c4 + 0.2, "3", FP, FA, 1, COR, 62)
    rot(c, t, c4 + 0.4, "8", FP, FB, -1, COR, 62)
    rot(c, t, c4 + 0.6, "4", FP, FC, -1, TINTA2, 62)
    E.saida(c, t, d5 + 0.2, lambda: rot(c, t, c4 + 0.8, "x", FP, FD, 1, TINTA2, 66))
    rot(c, t, d5 + 0.3, "6", FP, FD, 1, CERTO, 66)

    def txt4():
        E.frase(c, t, a4, [("corda:", "g", 80, COR)], X, 250, "center")
        E.frase(c, t, a4 + 0.5, ps("liga dois pontos", "i", 62), X, 340, "center", 0.12)
        E.frase(c, t, b4, ps("cruzam em", "i", 66) + [("P", "g", 76)], X, 480, "center", 0.12)
        E.frase(c, t, c4, ps("cada uma:", "i", 62) + [("2 pedaços", "g", 68, COR)], X, 600, "center", 0.12)
        E.frase(c, t, d4, ps("a regra", "i", 66, COR), X, 760, "center")
        fcen(c, t, d4 + 0.6, "PA · PB = PC · PD", X, 880, 76)
    E.saida(c, t, C["s05"] - 0.1, txt4)
    if t >= C["s05"]:
        E.frase(c, t, C["s05"], ps("pedaço × pedaço", "i", 70, COR), X, 220, "center", 0.12)
        fcen(c, t, a5, "3 · 8 = 4 · x", X, 380, 92)
        fcen(c, t, b5, "3 · 8 = 24", X, 520, 84, COR)
        fcen(c, t, c5, "4x = 24", X, 660, 92)
        E.foco(c, t, d5, 0.4, lambda a: E.pilula(c, "÷ 4", X + 250, 660, 44, "g", a=a, cor=E.SOBRE))
        bola_txt(c, t, d5 + 0.3, "x = 6", X, 840, 120, 66, CERTO)


# ---------------- por que funciona ----------------
def b_porque(c, t, C, b):
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    X = 1440
    t0 = C["s06"] - 3
    tri_cheio(c, [FP, FA, FC], E.COR, ep(t, a6 + 0.4, 0.5), 0.16)
    tri_cheio(c, [FP, FD, FB], TINTA2, ep(t, a6 + 0.8, 0.5), 0.14)
    # o arco CB, aberto pelos dois inscritos
    if t >= c6:
        g1 = math.degrees(math.atan2(-(FC[1] - FO[1]), FC[0] - FO[0]))
        g2 = math.degrees(math.atan2(-(FB[1] - FO[1]), FB[0] - FO[0]))
        ret = skia.Rect.MakeXYWH(FO[0] - FR, FO[1] - FR, 2 * FR, 2 * FR)
        varre = (g2 - g1) % 360
        if varre > 180:
            g1, varre = g2, 360 - varre
        c.drawArc(ret, -g1, -varre * ease_io(prog(t, c6, 0.7)), False, M.paint(CERTO, 0.9, stroke=14, cap_round=True))
    fig_cordas(c, t, t0, t0, t0, t_nomes=t0)
    lin(c, t, a6, FA, FC, TINTA, 6, 0.6)
    lin(c, t, a6 + 0.4, FD, FB, TINTA, 6, 0.6)
    E.angulo(c, t, b6, FP, FA, FC, None, r=60)
    E.angulo(c, t, b6 + 0.4, FP, FD, FB, None, r=60)
    E.angulo(c, t, c6 + 0.6, FA, FP, FC, None, r=80, cor=CERTO)
    E.angulo(c, t, c6 + 0.9, FD, FP, FB, None, r=80, cor=CERTO)

    def txt6():
        E.frase(c, t, C["s06"], ps("de onde vem?", "i", 74, COR), X, 220, "center")
        E.frase(c, t, a6, [("2", "g", 80, COR)] + ps("triângulos", "i", 70), X, 350, "center", 0.12)
        E.frase(c, t, b6, ps("em P:", "i", 62) + [("opostos pelo vértice", "g", 58, COR)], X, 490, "center", 0.12)
        E.frase(c, t, c6, ps("inscritos no", "i", 62) + [("mesmo arco", "g", 64, CERTO)], X, 640, "center", 0.12)
        E.frase(c, t, d6, ps("também", "i", 70) + [("iguais", "g", 76, CERTO)], X, 770, "center", 0.12)
    E.saida(c, t, C["s07"] - 0.1, txt6)
    if t >= C["s07"]:
        E.frase(c, t, a7, ps("2 ângulos iguais:", "i", 62), X, 220, "center", 0.12)
        E.frase(c, t, a7 + 0.6, [("semelhantes", "g", 80, COR)], X, 320, "center")
        fcen(c, t, b7 - 0.6, "f{PA}{PD} = f{PC}{PB}", X, 500, 72)
        fcen(c, t, b7 + 0.6, "PA · PB = PC · PD", X, 680, 76, COR)
        E.foco(c, t, c7, 0.5, lambda a: E.pilula(c, "na prova: só a regra", X, 850, 58, "g", a=a, cor=E.SOBRE))


# ---------------- secantes: P a 10 do centro, raio 8 ----------------
SO, SK = (650, 560), 52
SR = 8 * SK
SP = (SO[0] - 10 * SK, SO[1])
SU1 = (1.0, 0.0)                                            # a 1ª passa pelo centro: fora 2, inteira 18
SU2 = dirg(math.degrees(math.acos(6.5 / 10)))               # a 2ª corta em 4 e 9
ST_U = dirg(-math.degrees(math.asin(8 / 10)))               # a tangente, embaixo
S1a, S1b = em(SP, SU1, 2 * SK), em(SP, SU1, 18 * SK)
S2a, S2b = em(SP, SU2, 4 * SK), em(SP, SU2, 9 * SK)
STT = em(SP, ST_U, 6 * SK)
for _X in (S1a, S1b, S2a, S2b, STT):
    assert abs(math.dist(_X, SO) - SR) < 0.5


def fig_sec(c, t, t0, t1, t2, tinta=TINTA, alem=60):
    circ(c, t, t0, SO, SR, tinta, centro_=False)
    ponto(c, t, t0 + 0.3, SP, tinta, 13)
    nome(c, t, t0 + 0.3, "P", SP, -1, 0, tinta, 64)
    for u, tt, fim in ((SU1, t1, 18), (SU2, t2, 9)):
        if t >= tt:
            lin(c, t, tt, SP, em(SP, u, fim * SK + alem), tinta, 6, 0.7)


def b_secantes(c, t, C, b):
    a8, b8, c8, d8, e8 = (C["s08." + k] for k in "abcde")
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    a11, b11, c11, d11, e11 = (C["s11." + k] for k in "abcde")
    X = 1500
    fig_sec(c, t, a8, b8, c8)
    for P_, tt in ((S1a, b8 + 0.5), (S1b, b8 + 0.7), (S2a, c8 + 0.5), (S2b, c8 + 0.7)):
        ponto(c, t, tt, P_, E.COR, 12, pulsa=True)
    # os de fora e as inteiras
    if t >= d8:
        q = ep(t, d8, 0.4)
        M.line(c, *SP, *S1a, E.COR, q, 12); M.line(c, *SP, *S2a, E.COR, q, 12)
    cota(c, t, e8, SP, S1b, None, -1, off=60)
    cota(c, t, e8 + 0.3, SP, S2b, None, 1, off=84)
    E.saida(c, t, C["s10"], lambda: E.angulo(c, t, c9, SP, S1b, S2b, None, r=110, cor=TINTA2, preenche=0.3))
    if b9 <= t < c9 + 1:
        pulsa = 1 + 0.6 * math.sin(math.pi * M.clamp(prog(t, b9, 0.9)))
        c.drawCircle(*SP, 20 * pulsa, M.paint(E.COR, 0.8))
    rot(c, t, a10, "2", SP, S1a, 1, COR, 60)
    rot(c, t, b10, "16", S1a, S1b, 1, TINTA2, 60)
    rot(c, t, c10, "4", SP, S2a, 1, COR, 60)
    E.saida(c, t, e11 + 0.2, lambda: rot(c, t, d10, "x", S2a, S2b, 1, TINTA2, 66))
    rot(c, t, e11 + 0.3, "5", S2a, S2b, 1, CERTO, 66)
    rot(c, t, a11 + 0.3, "18", SP, S1b, -1, TINTA2, 54, gap=70)
    rot(c, t, d11 + 0.3, "9", SP, S2b, 1, TINTA2, 54, gap=94)

    def txt8():
        E.frase(c, t, a8, ps("e", "i", 66) + [("fora", "g", 76, COR)] + ps("da circunferência?", "i", 66), X, 220, "center", 0.12)
        E.frase(c, t, b8, [("secante:", "g", 70, COR)] + ps("corta em", "i", 62) + [("2", "g", 70)] + ps("pontos", "i", 62),
                X, 360, "center", 0.12)
        E.frase(c, t, c8, ps("de P saem", "i", 62) + [("2 secantes", "g", 68)], X, 490, "center", 0.12)
        E.frase(c, t, d8, [("o de fora:", "g", 66, COR)], X, 650, "center")
        E.frase(c, t, d8 + 0.5, ps("de P até a circunferência", "i", 50, TINTA2), X, 720, "center", 0.1)
        E.frase(c, t, e8, [("a inteira:", "g", 66, TINTA2)], X, 860, "center")
        E.frase(c, t, e8 + 0.5, ps("de P até o outro lado", "i", 50, TINTA2), X, 930, "center", 0.1)
    E.saida(c, t, C["s09"] - 0.1, txt8)

    def txt9():
        E.frase(c, t, C["s09"], ps("a regra", "i", 70, COR), X, 220, "center")
        fcen(c, t, a9, "fora · inteira", X, 350, 70, COR)
        fcen(c, t, a9 + 0.8, "= fora · inteira", X, 450, 70, COR)
        E.frase(c, t, b9, ps("sempre a partir de", "i", 60) + [("P", "g", 70, COR)], X, 610, "center", 0.12)
        E.frase(c, t, c9, ps("ângulo de P", "i", 60) + [("em comum", "g", 64, TINTA2)], X, 760, "center", 0.12)
        E.frase(c, t, c9 + 0.8, ps("triângulos semelhantes", "i", 54, TINTA2), X, 850, "center", 0.1)
    if t >= C["s09"] - 0.1:
        E.saida(c, t, C["s10"] - 0.1, txt9)

    def txt10():
        E.frase(c, t, C["s10"], ps("exemplo", "i", 72, COR), X, 220, "center")
        E.frase(c, t, a10, ps("1ª:", "i", 62) + [("2", "g", 72, COR)] + ps("fora", "i", 62), X, 380, "center", 0.12)
        E.frase(c, t, b10, ps("e", "i", 62) + [("16", "g", 72, TINTA2)] + ps("dentro", "i", 62), X, 480, "center", 0.12)
        E.frase(c, t, c10, ps("2ª:", "i", 62) + [("4", "g", 72, COR)] + ps("fora", "i", 62), X, 640, "center", 0.12)
        E.frase(c, t, d10, ps("e", "i", 62) + [("x", "g", 72, TINTA2)] + ps("dentro", "i", 62), X, 740, "center", 0.12)
    if t >= C["s10"] - 0.1:
        E.saida(c, t, C["s11"] - 0.1, txt10)
    if t >= C["s11"]:
        fcen(c, t, a11, "2 + 16 = 18", X, 220, 80, TINTA2)
        fcen(c, t, b11, "2 · 18 = 36", X, 350, 84)
        fcen(c, t, c11, "4 · inteira = 36", X, 490, 76)
        fcen(c, t, d11, "inteira = 9", X, 620, 80, TINTA2)
        fcen(c, t, e11, "9 − 4 =", X - 90, 800, 84)
        bola_txt(c, t, e11 + 0.3, "5 cm", X + 160, 772, 100, 66, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    X = 1500
    t0 = C["s12"] - 3
    fig_sec(c, t, t0, t0, t0)
    M.line(c, *SP, *S1a, E.COR, 1, 12); M.line(c, *SP, *S2a, E.COR, 1, 12)
    rot(c, t, t0, "2", SP, S1a, 1, COR, 60)
    rot(c, t, t0, "4", SP, S2a, 1, COR, 60)
    rot(c, t, t0, "x", S2a, S2b, 1, TINTA2, 66)
    if a12 <= t < a13:
        pulsa = 1 + 0.4 * math.sin(math.pi * M.clamp(prog(t, a12, 0.9)))
        M.line(c, *S1a, *S1b, ERRADO, ep(t, a12, 0.3) * (1 - ep(t, a13 - 0.4, 0.4)), 10 * pulsa)
    rot(c, t, a12, "16", S1a, S1b, 1, ERRADO if t < a13 else TINTA2, 60)
    # na secante, os dois pedaços saem de P para o mesmo lado
    if t >= b13:
        for k, (dest, off) in enumerate(((S1a, 45), (S1b, 95))):
            M.arrow(c, SP[0], SP[1] + off, dest[0], SP[1] + off, COR if k == 0 else TINTA2, ep(t, b13 + 0.3 * k, 0.3), 6, 20,
                    ease_io(prog(t, b13 + 0.3 * k, 0.7)))

    def erro():
        E.frase(c, t, a12, ps("usar o de", "i", 62) + [("dentro", "g", 70, ERRADO)], X, 220, "center", 0.12)
        E.frase(c, t, a12 + 0.8, ps("como se fosse corda", "i", 54, TINTA2), X, 300, "center", 0.1)
        fcen(c, t, b12, "2 · 16 = 32", X, 450, 84, ERRADO)
        fcen(c, t, c12, "4 · x = 32", X, 590, 84, ERRADO)
        fcen(c, t, d12, "x = 8", X - 60, 750, 96, ERRADO)
        E.foco(c, t, d12 + 0.4, 0.5, lambda a: E.selo(c, X + 150, 718, 50 * ease_back(prog(t, d12 + 0.4, 0.5)), False, a))
    E.saida(c, t, C["s13"] - 0.1, erro)
    if t >= C["s13"]:
        # mini corda: pedaços para lados opostos
        mx, my = X, 300
        E.foco(c, t, a13, 0.5, lambda a: (M.line(c, mx - 230, my, mx + 230, my, TINTA, a, 5), c.drawCircle(mx - 20, my, 11, M.paint(TINTA, a)),
                                          centro(c, "P", mx - 20, my - 30, 50, "g", TINTA, a)))
        if t >= a13 + 0.3:
            M.arrow(c, mx - 20, my + 30, mx - 230, my + 30, COR, 1, 6, 20, ease_io(prog(t, a13 + 0.3, 0.6)))
            M.arrow(c, mx - 20, my + 30, mx + 230, my + 30, TINTA2, 1, 6, 20, ease_io(prog(t, a13 + 0.3, 0.6)))
        E.frase(c, t, a13, [("corda:", "g", 62, COR)] + ps("lados opostos", "i", 58), X, 430, "center", 0.12)
        E.frase(c, t, b13, [("secante:", "g", 62, COR)] + ps("o mesmo lado", "i", 58), X, 600, "center", 0.12)
        E.foco(c, t, c13, 0.5, lambda a: E.pilula(c, "entra a secante inteira", X, 800, 56, "g", a=a, cor=E.SOBRE))
        fcen(c, t, c13 + 0.6, "2 · 18 = 4 · 9", X, 950, 76, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    a16, b16, c16, d16, e16 = (C["s16." + k] for k in "abcde")
    X = 1500
    t0 = C["s14"]
    circ(c, t, t0, SO, SR, BR, centro_=True)
    ponto(c, t, t0 + 0.3, SP, BR, 13)
    nome(c, t, t0 + 0.3, "P", SP, -1, 0, BR, 64)
    # a secante que passa pelo centro: fora 2, inteira 18
    lin(c, t, t0 + 0.3, SP, em(SP, SU1, 18 * SK + 90), BR, 5, 0.6)
    if t >= t0 + 0.6:
        M.line(c, *SP, *S1a, CLARO, ep(t, t0 + 0.6, 0.4), 11)
    E.foco(c, t, t0 + 0.8, 0.4, lambda a: E._cola(c, "2", (SP[0] + S1a[0]) / 2, SP[1], 0, -1, 14, 56, "b", CLARO, a))
    E.foco(c, t, t0 + 0.8, 0.4, lambda a: E._cola(c, "18", (SP[0] + S1b[0]) / 2 + 120, SP[1], 0, -1, 14, 56, "b", BR, a))
    # a tangente
    if t >= b14 and t < b16 - 0.3:
        lin(c, t, b14, SP, em(SP, ST_U, 6 * SK + 120), CLARO, 7, 0.7)
        ponto(c, t, b14 + 0.6, STT, CLARO, 15, pulsa=True)
        lin(c, t, b14 + 0.8, SO, STT, BR, 4, 0.5, a=0.7, dash=E.TRACO)
        E.angulo(c, t, b14 + 1.2, STT, SO, SP, r=34, reto=True, cor=CLARO)
        E.saida(c, t, c15, lambda: rot(c, t, a15 + 0.6, "?", SP, STT, -1, CLARO, 64))
        rot(c, t, c15 + 0.1, "6", SP, STT, -1, "#7CE3A0", 64)
    # a secante gira em volta de P até só encostar
    if t >= b16 - 0.3:
        g_tan = -math.degrees(math.asin(8 / 10))
        g = lerp(-20, g_tan, ease_io(prog(t, b16, 2.4)))
        if t >= d16:
            g = lerp(g_tan, -20, ease_io(prog(t, d16, 1.0)))
        u = dirg(g)
        lin(c, t, b16 - 0.3, SP, em(SP, u, 20 * SK), CLARO, 7, 0.4)
        cs = cortes(SO, SR, SP, u)
        if cs:
            P1, P2 = em(SP, u, cs[0]), em(SP, u, cs[1])
            c.drawCircle(*P1, 14, M.paint(BR)); c.drawCircle(*P2, 14, M.paint(CLARO))
    # textos
    def txt14():
        E.frase(c, t, a14, [("atalho:", "g", 80, CLARO)] + ps("a tangente", "i", 76, BR), X, 220, "center", 0.12)
        E.frase(c, t, b14, ps("só encosta:", "i", 62, CLARO) + [("1 ponto", "g", 70, BR)], X, 370, "center", 0.12)
        fcen(c, t, c14, "tangente^2", X, 540, 84, CLARO)
        fcen(c, t, c14 + 0.8, "= fora · inteira", X, 650, 76, BR)
    E.saida(c, t, C["s15"] - 0.1, txt14)

    def txt15():
        fcen(c, t, a15, "2 · 18 = 36", X, 260, 90, BR)
        fcen(c, t, b15, "tangente^2 = 36", X, 430, 80, CLARO)
        E.formula_em(c, t, c15, "r{36} =", X + 20, 640, 90, "g", BR, "right")
        bola_txt(c, t, c15 + 0.2, "6 cm", X + 170, 610, 100, 64, CERTO)
        E.frase(c, t, c15 + 1.0, ps("sem desenhar mais nada", "i", 54, CLARO), X, 820, "center", 0.1)
    if t >= C["s15"] - 0.1:
        E.saida(c, t, C["s16"] - 0.1, txt15)
    if t >= C["s16"]:
        E.frase(c, t, a16, ps("tangente =", "i", 60, CLARO) + ps("secante com", "i", 60, BR), X, 220, "center", 0.12)
        E.frase(c, t, a16 + 0.8, ps("os 2 pontos juntos", "g", 66, BR), X, 310, "center", 0.12)
        E.frase(c, t, c16, ps("fora = inteira:", "i", 60, CLARO), X, 470, "center", 0.12)
        E.frase(c, t, c16 + 0.6, [("vira quadrado", "g", 70, BR)], X, 560, "center")
        E.foco(c, t, d16, 0.5, lambda a: E.pilula(c, "corta em 2 pontos?", X, 740, 54, "g", fundo=ERRADO, a=a))
        E.frase(c, t, e16, ps("sem quadrado:", "i", 56, CLARO), X, 880, "center", 0.12)
        fcen(c, t, e16 + 0.4, "fora · inteira", X, 980, 70, BR)


# ---------------- questão: P a 14,5 do centro, raio 10,5 ----------------
QO, QK = (560, 500), 30
QR = 10.5 * QK
QP = (QO[0] - 14.5 * QK, QO[1])
QU2 = dirg(math.degrees(math.acos(12.5 / 14.5)))
Q1a, Q1b = em(QP, (1, 0), 4 * QK), em(QP, (1, 0), 25 * QK)
Q2a, Q2b = em(QP, QU2, 5 * QK), em(QP, QU2, 20 * QK)
QTU = dirg(-math.degrees(math.asin(10.5 / 14.5)))
QTT = em(QP, QTU, 10 * QK)
for _X in (Q1a, Q1b, Q2a, Q2b, QTT):
    assert abs(math.dist(_X, QO) - QR) < 0.5


def fig_q(c, t, t0, t1, t2):
    circ(c, t, t0, QO, QR, centro_=False)
    ponto(c, t, t0 + 0.3, QP, TINTA, 13)
    nome(c, t, t0 + 0.3, "P", QP, -1, 0, TINTA, 60)
    lin(c, t, t1, QP, em(QP, (1, 0), 25 * QK + 70), TINTA, 6, 0.6)
    lin(c, t, t2, QP, em(QP, QU2, 20 * QK + 70), TINTA, 6, 0.6)
    if t >= t1 + 0.4:
        M.line(c, *QP, *Q1a, E.COR, ep(t, t1 + 0.4, 0.4), 11)
    if t >= t2 + 0.4:
        M.line(c, *QP, *Q2a, E.COR, ep(t, t2 + 0.4, 0.4), 11)
    rot(c, t, t1 + 0.5, "4", QP, Q1a, -1, COR, 56, onde=0.85)
    rot(c, t, t1 + 0.8, "21", Q1a, Q1b, -1, TINTA2, 56)
    rot(c, t, t2 + 0.5, "5", QP, Q2a, 1, COR, 56)


def b_questao(c, t, C, b):
    a17, b17, c17, d17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 130, passo=0.12)
    fig_q(c, t, C["s17"] + 0.5, a17, b17)
    rot(c, t, c17, "?", Q2a, Q2b, 1, COR, 66)
    if t >= d17:
        lin(c, t, d17, QP, em(QP, QTU, 10 * QK + 80), TINTA2, 6, 0.6, dash=E.TRACO)
        rot(c, t, d17 + 0.5, "?", QP, QTT, -1, COR, 66)
    E.frase(c, t, c17, ps("quanto mede o de", "i", 60) + [("dentro", "g", 64, COR)] + ps("da 2ª?", "i", 60), 580, 920, "center", 0.12)
    E.frase(c, t, d17, ps("e a", "i", 60) + [("tangente", "g", 64, COR)] + ps("que sai de P?", "i", 60), 580, 1015, "center", 0.12)
    E.relogio(c, t, C["s18.a"])


def b_resposta(c, t, C, b):
    a19, b19, c19, d19, e19 = (C["s19." + k] for k in "abcde")
    a20, b20, c20 = C["s20.a"], C["s20.b"], C["s20.c"]
    X = 1440
    t0 = C["s19"] - 2
    fig_q(c, t, t0, t0, t0)
    E.saida(c, t, e19, lambda: rot(c, t, t0, "?", Q2a, Q2b, 1, COR, 62))
    rot(c, t, e19 + 0.3, "15", Q2a, Q2b, 1, CERTO, 62)
    lin(c, t, a20, QP, em(QP, QTU, 10 * QK + 80), TINTA, 6, 0.6)
    ponto(c, t, a20 + 0.5, QTT, TINTA, 11)
    rot(c, t, b20 + 0.2, "10", QP, QTT, -1, CERTO, 62)
    if c20 <= t:
        q = ep(t, c20, 0.3)
        M.line(c, *Q1a, *Q1b, ERRADO, q, 10)

    def conta():
        fcen(c, t, a19, "4 + 21 = 25", X, 220, 80, TINTA2)
        fcen(c, t, b19, "4 · 25 = 100", X, 350, 84)
        fcen(c, t, c19, "5 · inteira = 100", X, 490, 76)
        fcen(c, t, d19, "inteira = 20", X, 620, 80, TINTA2)
        fcen(c, t, e19, "20 − 5 =", X - 90, 800, 84)
        bola_txt(c, t, e19 + 0.3, "15 cm", X + 170, 772, 106, 62, CERTO)
    E.saida(c, t, C["s20"] - 0.1, conta)
    if t >= C["s20"]:
        fcen(c, t, a20, "tangente^2 = 100", X, 250, 80)
        E.formula_em(c, t, b20, "r{100} =", X - 10, 450, 90, "g", None, "right")
        bola_txt(c, t, b20 + 0.2, "10 cm", X + 160, 420, 106, 62, CERTO)
        E.frase(c, t, c20 - 0.4, ps("com o de dentro:", "i", 60, TINTA2), X, 640, "center", 0.12)
        fcen(c, t, c20, "4 · 21 = 84", X, 760, 84, ERRADO)
        E.frase(c, t, c20 + 1.2, ps("84 ÷ 5 não é exato", "i", 56, ERRADO), X, 870, "center", 0.12)
        E.foco(c, t, c20 + 1.6, 0.5, lambda a: E.selo(c, X + 300, 760, 46 * ease_back(prog(t, c20 + 1.6, 0.5)), False, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s21.a", "cordas:", "pedaço × pedaço"), ("s21.b", "secantes:", "fora × inteira"), ("s21.c", "tudo", "a partir de P"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 5, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 70, COR), (l2, "i", 72)], 390, y, "left", 0.2)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], ps("próxima aula: prática", "i", 84), XE, 300)
    E.frase(c, t, C["s22.a"], [("Polígonos e", "g", 120, COR)], XE, 440)
    E.frase(c, t, C["s22.a"] + 0.4, [("circunferência", "g", 120, COR)], XE, 570)
    E.frase(c, t, C["s22.b"], ps("quadriláteros, regulares,", "i", 64), XE, 690, passo=0.1)
    E.frase(c, t, C["s22.b"] + 1.0, ps("rodas e ângulos", "i", 64), XE, 780, passo=0.1)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(720, 425, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, cordas=b_cordas, porque=b_porque, secantes=b_secantes, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
