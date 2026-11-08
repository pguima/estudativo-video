"""Visual — Estudativo · MAT-POL-002: soma dos ângulos internos e número de diagonais de um polígono.
Linguagem da geometria plana (MAT-ANG-001 a 007, MAT-POL-001): lados em tinta; o vértice escolhido pulsa na cor da matéria;
diagonais na cor da matéria; os triângulos do corte pintados alternando COR e TINTA2 (claros), cada um com seu número;
os ângulos de cada triângulo são cunhas da cor dele e mostram que encaixam nos ângulos do polígono; medidas na grotesca;
resposta na esfera; vermelho é erro, verde é certo. A diagonal contada duas vezes leva uma seta em cada sentido.
Peças locais: reg() (pontos do polígono regular com A à esquerda, em volta no sentido do relógio), leque() (corte em triângulos
a partir de A), cunha_v() (ângulo pintado do vértice V entre P e Q), seta_dupla(), ps(), fcen(), bola_txt().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polígonos e Círculo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POL-002_soma_dos_angulos_e_diagonais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("poligono", "triangulos", "diagonais", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 6 * 3 == 18 and 18 // 2 == 9 and 6 * (6 - 3) // 2 == 9
assert (6 - 2) * 180 == 720 and (4 - 2) * 180 == 360 and (5 - 2) * 180 == 540 and (3 - 2) * 180 == 180
assert 4 * (4 - 3) == 4 and 4 // 2 == 2
assert (20 - 2) * 180 == 3240 and (8 - 2) * 180 == 1080 and 720 + 180 == 900 and 900 + 180 == 1080
assert 8 * (8 - 3) == 40 and 40 // 2 == 20
NOMES = {3: "triângulo", 4: "quadrilátero", 5: "pentágono", 6: "hexágono", 8: "octógono", 10: "decágono"}


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


def reg(n, cx, cy, r):
    """polígono regular de n lados com um lado deitado embaixo; A é o vértice mais à esquerda (ou o de baixo à esquerda),
    e os outros seguem em volta no sentido do relógio"""
    ini = 90 - 180 / n
    pts = [(cx + r * math.cos(math.radians(ini + k * 360 / n)), cy + r * math.sin(math.radians(ini + k * 360 / n))) for k in range(n)]
    i0 = min(range(n), key=lambda k: (round(pts[k][0], 3), -pts[k][1]))
    return pts[i0:] + pts[:i0]


def lin(c, t, t0, P, Q, cor=TINTA, larg=6, d=0.5, a=1.0, dash=None):
    if t >= t0 and a > 0:
        M.line(c, *P, *Q, cor, a, larg, dash=dash, progress=ease_io(prog(t, t0, d)))


def cunha_v(c, V, P, Q, r, cor, a=1.0, alfa=0.35, borda=4):
    """ângulo pintado do vértice V, entre os lados VP e VQ (o menor dos dois)"""
    if a <= 0:
        return
    a1 = math.degrees(math.atan2(P[1] - V[1], P[0] - V[0]))
    a2 = math.degrees(math.atan2(Q[1] - V[1], Q[0] - V[0]))
    varre = (a2 - a1 + 180) % 360 - 180
    ret = skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r)
    path = skia.Path(); path.moveTo(*V); path.arcTo(ret, a1, varre, False); path.close()
    c.drawPath(path, M.paint(cor, alfa * a))
    if borda:
        c.drawArc(ret, a1, varre, False, M.paint(cor, a, stroke=borda, cap_round=True))


def tri_cheio(c, pts, cor, a=1.0, alfa=0.2):
    if a <= 0:
        return
    path = skia.Path(); path.addPoly([tuple(p) for p in pts], True)
    c.drawPath(path, M.paint(cor, alfa * a))


def cent(pts):
    return sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)


def leque(c, t, P, td, tt, ta=None, a=1.0, escuro=False, numeros=True):
    """corta o polígono P em triângulos a partir de P[0]: td = instante das diagonais, tt = dos triângulos pintados,
    ta = das cunhas dos ângulos de cada triângulo"""
    n = len(P)
    cores = (E.COR, TINTA2) if not escuro else (CLARO, BR)
    for k in range(1, n - 1):
        tri = (P[0], P[k], P[k + 1])
        cor = cores[(k - 1) % 2]
        if tt is not None and t >= tt + 0.25 * (k - 1):
            q = ep(t, tt + 0.25 * (k - 1), 0.4) * a
            tri_cheio(c, tri, cor, q, 0.2)
            if numeros:
                G = cent(tri)
                E.foco(c, t, tt + 0.25 * (k - 1), 0.4, lambda f, G=G, k=k, cor=cor: centro(c, str(k), G[0], G[1] + 18, 52, "g", cor, f * a))
        if ta is not None and t >= ta + 0.3 * (k - 1):
            q = ep(t, ta + 0.3 * (k - 1), 0.4) * a
            for V, A_, B_ in ((tri[0], tri[1], tri[2]), (tri[1], tri[2], tri[0]), (tri[2], tri[0], tri[1])):
                cunha_v(c, V, A_, B_, 60 if V != P[0] else 110, cor, q, 0.42, 4)
    for k in range(2, n - 1):
        lin(c, t, td + 0.3 * (k - 2), P[0], P[k], CLARO if escuro else E.COR, 6, 0.5, a)


def pulsa_v(c, t, t0, V, cor=None, t1=None, r=16):
    if t < t0 or (t1 is not None and t > t1 + 0.4):
        return
    a = ep(t, t0, 0.3) * (1 - (ep(t, t1, 0.4) if t1 is not None else 0))
    k = 1 + 0.6 * math.sin(math.pi * M.clamp(prog(t, t0, 0.8)))
    c.drawCircle(*V, r * k, M.paint(cor or E.COR, a))


def seta_dupla(c, P, Q, cor, a=1.0, p=1.0):
    """diagonal com uma seta em cada ponta: contada nos dois sentidos"""
    if a <= 0:
        return
    M.line(c, *P, *Q, cor, a, 9, progress=p)
    ux, uy = E._uni(*P, *Q)
    nx, ny = -uy, ux
    for (X, Y), s in ((Q, 1), (P, -1)):
        if p < 0.98 and s == -1:
            continue
        bx, by = X - ux * s * 34, Y - uy * s * 34
        M.line(c, bx + nx * 20, by + ny * 20, X, Y, cor, a, 9)
        M.line(c, bx - nx * 20, by - ny * 20, X, Y, cor, a, 9)


def poli(c, t, t0, P, nomes=None, d=0.8, escuro=False, preenche=0.06, size=56, a=1.0):
    if a <= 0 or t < t0:
        return
    if a < 1:
        c.saveLayerAlpha(None, int(255 * a))
    E.poligono(c, t, t0, P, list(nomes) if nomes else None, preenche=preenche, d=d, escuro=escuro, size=size)
    if a < 1:
        c.restore()


# ---------------- gancho ----------------
HX = reg(6, 560, 560, 330)


def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    X = 1450

    def um():
        poli(c, t, ka, HX, "ABCDEF")
        tq = lerp(ka, kb, 0.45)
        k = 0
        for i in range(6):
            for j in range(i + 2, 6):
                if i == 0 and j == 5:
                    continue
                lin(c, t, tq + 0.12 * k, HX[i], HX[j], E.mix(E.COR, BR, 0.45), 4, 0.4, 1 - ep(t, kd, 0.4) * 0.6)
                k += 1
        if t >= kd:
            p = ease_io(prog(t, kd + 0.2, 0.8))
            seta_dupla(c, HX[0], HX[3], E.COR, ep(t, kd, 0.3), p)
        E.frase(c, t, ka + 0.2, [("6", "g", 110, COR)] + ps("lados", "i", 90), X, 260, "center", 0.14)
        E.frase(c, t, ka + 1.4, ps("quantas", "i", 76) + [("diagonais?", "g", 80, COR)], X, 380, "center", 0.14)
        E.frase(c, t, kb - 1.0, ps("muita gente:", "i", 64, TINTA2), X, 530, "center", 0.12)
        E.foco(c, t, kb, 0.5, lambda a: centro(c, "18", X, 720, 190, "g", ERRADO, a))
        if t >= kc:
            E.risco(c, X - 130, 700, X + 130, 600, t, kc, largura=14)
        E.frase(c, t, kc + 0.2, ps("o dobro do certo", "i", 64, ERRADO), X, 830, "center", 0.12)
        E.frase(c, t, kd + 0.4, ps("cada uma contada", "i", 60) + [("2 vezes", "g", 62, COR)], X, 950, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1520, 560, 240 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 280, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), [("a soma", "g", 100, COR)] + ps("dos ângulos", "i", 92), XE, 430, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.55), ps("de qualquer polígono", "i", 80), XE, 540, passo=0.14)
        E.frase(c, t, tb, [("as diagonais", "g", 96, COR)], XE, 710, passo=0.14)
        E.frase(c, t, tb + 0.7, ps("sem desenhar", "i", 80), XE, 820, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1520, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1520, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    # triângulo com as três cunhas
    T = [(1400, 400), (1700, 400), (1580, 220)]
    itens = (("s03.b", "ângulos de dentro do triângulo", "somam 180°", 150), ("s03.c", "diagonal: liga vértices", "não vizinhos", 500))
    for k, l1, l2, y in itens:
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 300, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 52)], x + 44, y + 80)
        E.frase(c, t, C[k] + 0.6, [(l2, "g", 66, COR)], x + 44, y + 180)
    tb = C["s03.b"] + 0.9
    if t >= tb:
        q = ep(t, tb, 0.5)
        E._contorno(c, T, ease_io(prog(t, tb, 0.6)), TINTA, 5)
        for i in range(3):
            cunha_v(c, T[i], T[i - 1], T[(i + 1) % 3], 46, (E.COR, TINTA2, E.COR)[i], ep(t, tb + 0.5 + 0.2 * i, 0.4), 0.4)
    tc = C["s03.c"] + 0.9
    Q = [(1400, 760), (1700, 760), (1720, 590), (1420, 590)]
    if t >= tc:
        E._contorno(c, Q, ease_io(prog(t, tc, 0.6)), TINTA, 5)
        lin(c, t, tc + 0.6, Q[0], Q[2], E.COR, 6, 0.5)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(150 + 270, 500 + 270, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 930, "left", 0.12)


# ---------------- polígono ----------------
def b_poligono(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]

    def nomes():
        E.frase(c, t, a4, [("polígono:", "g", 70, COR)] + ps("figura fechada só de segmentos", "i", 64), W / 2, 170, "center", 0.12)
        cel = ((3, 380, 430, b4), (4, 960, 430, b4 + 0.9), (5, 1540, 430, c4), (6, 380, 800, c4 + 0.9), (8, 960, 800, d4), (10, 1540, 800, d4 + 0.9))
        for n, cx, cy, t0 in cel:
            r = 125 if n > 4 else 140
            poli(c, t, t0, reg(n, cx, cy - 20, r), None, d=0.6, size=40)
            E.frase(c, t, t0 + 0.2, [(str(n), "g", 60, COR), (NOMES[n], "i", 56)], cx, cy + 190, "center", 0.12)
    E.saida(c, t, C["s05"] - 0.1, nomes)
    if t >= C["s05"]:
        a5, b5 = C["s05.a"], C["s05.b"]
        E.frase(c, t, a5, ps("nesta aula:", "i", 70) + [("convexos", "g", 80, COR)], W / 2, 180, "center", 0.12)
        P1 = reg(6, 560, 560, 250)
        poli(c, t, a5, P1, None, d=0.7)
        E.foco(c, t, a5 + 0.8, 0.5, lambda a: E.selo(c, 560, 920, 60 * ease_back(prog(t, a5 + 0.8, 0.5)), True, a))
        # côncavo: a ponta de cima virada para dentro
        Pc = reg(6, 1360, 560, 250)
        mid = ((Pc[1][0] + Pc[2][0]) / 2, 560 - 40)  # entre os dois vértices de cima, uma ponta virada para dentro
        Pc = Pc[:2] + [mid] + Pc[2:]
        if t >= b5:
            poli(c, t, b5, Pc, None, d=0.7, preenche=0.05)
            cunha_v(c, mid, Pc[1], Pc[3], 50, ERRADO, ep(t, b5 + 0.7, 0.4), 0.4)
            E.foco(c, t, b5 + 0.8, 0.5, lambda a: E.selo(c, 1360, 920, 60 * ease_back(prog(t, b5 + 0.8, 0.5)), False, a))
            E.frase(c, t, b5 + 0.4, ps("ponta para dentro", "i", 52, ERRADO), 1360, 300, "center", 0.1)


# ---------------- corte em triângulos ----------------
HB = reg(6, 560, 570, 340)


def b_triangulos(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    X = 1450
    poli(c, t, C["s06"], HB, "ABCDEF")
    pulsa_v(c, t, a6, HB[0])
    leque(c, t, HB, b6, c6, a7)
    # cada lado longe de A ganha um triângulo; os dois lados de A ficam de fora
    for k in range(1, 5):
        tk = a8 + 0.6 + 0.5 * (k - 1)
        if a8 <= t < C["s08.end"]:
            q = ep(t, tk, 0.3) * (1 - ep(t, b8, 0.3))
            M.line(c, *HB[k], *HB[k + 1], E.COR, q, 14)
    if t >= b8:
        for P in (HB[1], HB[5]):
            M.line(c, *HB[0], *P, ERRADO, ep(t, b8 + 0.3, 0.4), 14)

    def seis():
        E.frase(c, t, a6, ps("escolha", "i", 76) + [("1 vértice", "g", 80, COR)], X, 280, "center", 0.12)
        E.frase(c, t, b6, ps("todas as", "i", 70) + [("diagonais", "g", 74, COR)], X, 420, "center", 0.12)
        E.frase(c, t, c6, [("4", "g", 130, COR)] + ps("triângulos", "i", 84), X, 620, "center", 0.12)
    E.saida(c, t, C["s07"] - 0.1, seis)

    def sete():
        E.frase(c, t, a7, ps("os ângulos", "i", 70) + [("encaixam", "g", 74, COR)], X, 280, "center", 0.12)
        E.frase(c, t, a7 + 0.9, ps("nada sobra, nada falta", "i", 56, TINTA2), X, 370, "center", 0.1)
        fcen(c, t, b7, "4 × 180°", X, 560, 100)
        bola_txt(c, t, c7, "720°", X, 780, 140, 84)
    if t >= C["s07"]:
        E.saida(c, t, C["s08"] - 0.1, sete)

    if t >= C["s08"]:
        E.frase(c, t, C["s08"] + 0.2, ps("por que 4, e não", "i", 70) + [("6?", "g", 76, COR)], X, 250, "center", 0.12)
        E.frase(c, t, a8, ps("cada lado longe de A", "i", 56), X, 400, "center", 0.1)
        E.frase(c, t, a8 + 0.8, [("1 triângulo", "g", 64, COR)], X, 480, "center")
        E.frase(c, t, b8, ps("os 2 lados de A:", "i", 56), X, 640, "center", 0.1)
        E.frase(c, t, b8 + 0.6, [("ficam de fora", "g", 64, ERRADO)], X, 720, "center")
        fcen(c, t, c8, "6 − 2 = 4", X, 900, 100, COR)


# ---------------- a fórmula da soma ----------------
def b_formula(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]

    def nove():
        E.frase(c, t, C["s09"] + 0.2, ps("com qualquer polígono", "i", 80), W / 2, 220, "center", 0.12)
        E.frase(c, t, a9, [("n", "g", 120, COR)] + ps("= número de lados", "i", 76), W / 2, 420, "center", 0.12)
        E.frase(c, t, b9, [("n − 2", "g", 110, COR)] + ps("triângulos", "i", 80), W / 2, 590, "center", 0.12)
        p = ep(t, c9, 0.5)
        E.caixa_pontilhada(c, W / 2 - 560, 690, 1120, 210, p, prog_=p)
        fcen(c, t, c9, "S = (n − 2) × 180°", W / 2, 840, 110, COR)
    E.saida(c, t, C["s10"] - 0.1, nove)
    if t < C["s10"]:
        return
    fcen(c, t, C["s10"], "S = (n − 2) × 180°", W / 2, 180, 70, COR)
    Q = reg(4, 500, 470, 190)
    poli(c, t, C["s10"] + 0.2, Q, None, d=0.6)
    leque(c, t, Q, a10, a10 + 0.5, None)
    fcen(c, t, a10 + 0.4, "4 − 2 = 2", 500, 790, 76)
    fcen(c, t, b10, "2 × 180 = 360°", 500, 920, 76, COR)
    Pn = reg(5, 1420, 480, 200)
    poli(c, t, c10 - 0.4, Pn, None, d=0.6)
    leque(c, t, Pn, c10, c10 + 0.7, None)
    fcen(c, t, c10 + 0.4, "5 − 2 = 3", 1420, 790, 76)
    fcen(c, t, d10, "3 × 180 = 540°", 1420, 920, 76, COR)


# ---------------- diagonais ----------------
def b_diagonais(c, t, C, b):
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    X = 1450

    def fig():
        poli(c, t, C["s11"], HB, "ABCDEF")
        pulsa_v(c, t, C["s11"] + 0.5, HB[0], t1=a12)
        if a11 <= t < a12:
            k = 1 - ep(t, a12 - 0.3, 0.3)
            E.foco(c, t, a11, 0.4, lambda f: (c.drawCircle(*HB[0], 24, M.paint(ERRADO, f * k, stroke=6))))
            for P in (HB[1], HB[5]):
                q = ep(t, b11, 0.4) * k
                M.line(c, *HB[0], *P, ERRADO, q, 14)
                c.drawCircle(*P, 18, M.paint(ERRADO, q, stroke=6))
        if t < a12:
            for j, k in enumerate((2, 3, 4)):
                lin(c, t, c11 + 0.3 * j, HB[0], HB[k], E.COR, 7, 0.5)
        else:
            # 6 vértices × 3 diagonais: cada vértice desenha as suas
            for i in range(6):
                ti = a12 + 0.35 * i
                for k in (2, 3, 4):
                    j = (i + k) % 6
                    P, Q = HB[i], HB[j]
                    q = ease_io(prog(t, ti, 0.4))
                    if q > 0:
                        ax, ay = lerp(P[0], Q[0], 0.5 * q), lerp(P[1], Q[1], 0.5 * q)
                        M.line(c, *P, ax, ay, E.mix(E.COR, BR, 0.25), 1.0, 6)
            if t >= c12:
                q = ep(t, c12, 0.3) * (1 - ep(t, C["s12.end"], 0.4))
                seta_dupla(c, HB[0], HB[3], E.COR, q, 1.0)
    E.saida(c, t, a13 - 0.1, fig)

    def onze():
        E.frase(c, t, a11, ps("com ele mesmo:", "i", 60) + [("não", "g", 66, ERRADO)], X, 300, "center", 0.12)
        E.frase(c, t, b11, ps("com os vizinhos:", "i", 60) + [("não", "g", 66, ERRADO)], X, 420, "center", 0.12)
        E.frase(c, t, b11 + 0.7, ps("(seria um lado)", "i", 50, TINTA2), X, 500, "center", 0.1)
        fcen(c, t, c11, "6 − 3 = 3", X, 700, 110, COR)
        E.frase(c, t, c11 + 0.6, ps("diagonais por vértice", "i", 56), X, 800, "center", 0.1)
    E.saida(c, t, C["s12"] - 0.1, onze)

    def doze():
        E.frase(c, t, a12, ps("6 vértices,", "i", 64) + [("3 cada", "g", 70, COR)], X, 260, "center", 0.12)
        fcen(c, t, b12, "6 × 3 = 18", X, 420, 96)
        E.frase(c, t, c12, [("A → D", "g", 70, COR), ("=", "g", 70), ("D → A", "g", 70, COR)], X, 590, "center", 0.2)
        E.frase(c, t, c12 + 1.0, ps("a mesma, contada 2 vezes", "i", 50, TINTA2), X, 680, "center", 0.1)
        fcen(c, t, d12, "18 ÷ 2 = 9", X, 840, 96)
        bola_txt(c, t, d12 + 0.8, "9", X + 330, 810, 70, 80)
    if t >= C["s12"]:
        E.saida(c, t, a13 - 0.1, doze)

    if t >= a13:
        E.frase(c, t, a13 - 0.3, ps("em fórmula", "i", 80, COR), W / 2, 200, "center")
        E.formula_em(c, t, a13, "d = f{n(n − 3)}{2}", 760, 470, 120, "g", None, "center")
        p = ep(t, b13, 0.5)
        E.caixa_pontilhada(c, 735, 325, 295, 115, p, E.COR, prog_=p)
        E.foco(c, t, b13 + 0.2, 0.4, lambda a: E.pilula(c, "saem de cada vértice", 1460, 380, 46, "g", a=a, cor=E.SOBRE))
        if t >= b13:
            M.arrow(c, 1205, 380, 1045, 380, E.COR, ep(t, b13 + 0.2, 0.4), 5, 16, ep(t, b13 + 0.2, 0.4))
        p = ep(t, c13, 0.5)
        E.caixa_pontilhada(c, 805, 450, 95, 95, p, TINTA, prog_=p)
        E.foco(c, t, c13 + 0.2, 0.4, lambda a: E.pilula(c, "desconta a contagem dupla", 1460, 520, 46, "g", fundo=TINTA, a=a))
        if t >= c13:
            M.arrow(c, 1135, 515, 915, 500, TINTA, ep(t, c13 + 0.2, 0.4), 5, 16, ep(t, c13 + 0.2, 0.4))
        E.foco(c, t, lerp(a13, b13, 0.6), 0.4, lambda a: E.escreve(c, "n = número de vértices = número de lados", 560, 800, 54, "i", TINTA2, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    X = 1400
    Q = reg(4, 560, 580, 300)
    E.frase(c, t, C["s14"], [("cuidado", "g", 92, ERRADO)] + ps("com este erro", "i", 86), W / 2, 150, "center", 0.14)
    E.saida(c, t, C["s14.end"], lambda: E.frase(c, t, a14, ps("esqueceu de", "i", 64) + [("dividir por 2", "g", 66, ERRADO)], X, 300, "center", 0.12))
    poli(c, t, lerp(a14, b14, 0.25), Q, "ABCD", d=0.7)
    t1 = lerp(a14, b14, 0.55)
    E.frase(c, t, t1, ps("de cada vértice:", "i", 56), X, 430, "center", 0.1)
    fcen(c, t, t1 + 0.6, "4 − 3 = 1", X, 530, 80)
    # cada vértice puxa a sua: cada diagonal sai duas vezes
    if b14 <= t < c14:
        for i in range(4):
            P, R = Q[i], Q[(i + 2) % 4]
            q = ease_io(prog(t, b14 + 0.3 * i, 0.4))
            if q > 0:
                M.line(c, *P, lerp(P[0], R[0], 0.48 * q), lerp(P[1], R[1], 0.48 * q), ERRADO, 1.0, 8)
                c.drawCircle(*P, 14, M.paint(ERRADO))
    fcen(c, t, b14, "4 × 1 = 4", X, 660, 80, ERRADO)
    if t >= c14:
        lin(c, t, c14, Q[0], Q[2], E.COR, 9, 0.5)
        lin(c, t, c14 + 0.3, Q[1], Q[3], E.COR, 9, 0.5)
        E.frase(c, t, c14 + 0.3, ps("só tem", "i", 60) + [("2", "g", 70, COR)], X, 790, "center", 0.12)
    fcen(c, t, d14, "4 ÷ 2 = 2", X, 930, 90, CERTO)
    E.foco(c, t, d14 + 0.6, 0.5, lambda a: E.selo(c, X + 290, 900, 50 * ease_back(prog(t, d14 + 0.6, 0.5)), True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a15 = C["s15.a"]
    a16, b16, c16, d16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    fila = ((3, 300, "180°", C["s15.b"]), (4, 740, "360°", C["s15.c"]), (5, 1180, "540°", C["s15.d"]), (6, 1620, "720°", C["s15.e"]))

    E.saida(c, t, a15 - 0.1, lambda: E.frase(c, t, C["s15"] + 0.2, ps("o atalho da", "i", 100, CLARO) + [("soma", "g", 110, BR)], W / 2, 560, "center", 0.14))

    def um():
        E.frase(c, t, a15, ps("cada lado a mais:", "i", 76, CLARO) + [("+ 180°", "g", 96, BR)], W / 2, 200, "center", 0.12)
        for i, (n, cx, s, t0) in enumerate(fila):
            P = reg(n, cx, 560, 150)
            poli(c, t, t0, P, None, d=0.5, escuro=True, preenche=0.0, size=40)
            leque(c, t, P, t0 + 0.3, t0 + 0.4 if t >= a16 else None, None, escuro=True, numeros=False)
            E.frase(c, t, t0 + 0.2, [(s, "g", 80, CLARO)], cx, 830, "center")
            if i:
                E.foco(c, t, t0 - 0.2, 0.4, lambda a, cx=cx: E.pilula(c, "+180°", cx - 220, 830 - 28, 34, "g", fundo=E.mix(E.COR, BR, 0.25), a=a))
        E.frase(c, t, a16, [("1 lado a mais", "g", 64, BR)] + ps("= 1 triângulo a mais", "i", 64, CLARO), W / 2, 980, "center", 0.12)
    E.saida(c, t, b16 - 0.1, um)
    if t >= b16:
        E.frase(c, t, b16, ps("polígono de", "i", 76, CLARO) + [("20 lados?", "g", 84, BR)], W / 2, 280, "center", 0.12)
        E.frase(c, t, b16 + 1.0, ps("somar 180 várias vezes", "i", 60, CLARO) + [("não compensa", "g", 64, ERRADO)], W / 2, 400, "center", 0.12)
        fcen(c, t, c16, "20 − 2 = 18", W / 2, 600, 100, BR)
        fcen(c, t, d16, "18 × 180 = 3240°", W / 2, 780, 110, CLARO)


# ---------------- questão ----------------
OC = reg(8, 560, 570, 330)


def b_questao(c, t, C, b):
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    poli(c, t, a17 - 0.4, reg(8, 520, 520, 260), None, d=0.8)
    E.frase(c, t, a17, [("octógono:", "g", 64, COR)] + ps("8 lados", "i", 64), 520, 880, "center", 0.12)
    E.frase(c, t, b17, ps("soma dos", "i", 64) + [("ângulos internos?", "g", 64, COR)], 1000, 330, "left", 0.12)
    E.frase(c, t, c17, ps("quantas", "i", 64) + [("diagonais?", "g", 64, COR)], 1000, 470, "left", 0.12)
    E.relogio(c, t, C["s18.a"], 1490, 640, 160)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    a20, b20, c20 = C["s20.a"], C["s20.b"], C["s20.c"]
    X = 1440
    poli(c, t, C["s19"], OC, None, d=0.7)
    pulsa_v(c, t, C["s19"] + 0.4, OC[0], t1=C["s20.end"])
    if t < C["s20"]:
        leque(c, t, OC, a19, a19 + 0.4, None, a=1 - ep(t, C["s20"] - 0.4, 0.4))
    else:
        for j, k in enumerate(range(2, 7)):
            lin(c, t, a20 + 0.25 * j, OC[0], OC[k], E.COR, 7, 0.4)

    def dezenove():
        fcen(c, t, a19, "8 − 2 = 6", X, 250, 84)
        E.frase(c, t, a19 + 0.5, ps("triângulos", "i", 56, TINTA2), X, 330, "center")
        fcen(c, t, b19, "6 × 180 = 1080°", X, 470, 84, COR)
        bola_txt(c, t, b19 + 0.8, "1080°", X + 10, 640, 110, 62)
        tc = c19
        E.frase(c, t, tc, ps("pelo atalho:", "i", 52, TINTA2) + [("720", "g", 56)], X, 820, "center", 0.1)
        fcen(c, t, lerp(tc, C["s19.end"], 0.3), "720 + 180 = 900", X, 900, 56, TINTA2)
        fcen(c, t, lerp(tc, C["s19.end"], 0.6), "900 + 180 = 1080", X, 980, 56, TINTA2)
        E.foco(c, t, lerp(tc, C["s19.end"], 0.85), 0.5, lambda a: E.selo(c, X + 310, 960, 40 * ease_back(prog(t, lerp(tc, C["s19.end"], 0.85), 0.5)), True, a))
    E.saida(c, t, C["s20"] - 0.1, dezenove)
    if t >= C["s20"]:
        fcen(c, t, a20, "8 − 3 = 5", X, 280, 90)
        E.frase(c, t, a20 + 0.5, ps("de cada vértice", "i", 56, TINTA2), X, 370, "center", 0.1)
        fcen(c, t, b20, "8 × 5 = 40", X, 540, 90)
        fcen(c, t, c20, "40 ÷ 2 = 20", X, 700, 90, COR)
        bola_txt(c, t, c20 + 0.8, "20", X, 870, 90, 80)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s21.a", "corte em triângulos", "a partir de 1 vértice"), ("s21.b", "S = (n − 2) × 180°", ""),
                 ("s21.c", "diagonais:", "divida por 2"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 28, 54, a=a), centro(c, str(i + 1), 300, y - 6, 62, "g", BR, a)))
            if i == 1:
                E.formula_em(c, t, C[k] + 0.1, l1, 400, y, 76, "g", COR)
            else:
                E.frase(c, t, C[k] + 0.1, [(l1, "g", 70, COR), (l2, "i", 70)], 400, y, "left", 0.2)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s22.a"], [("Polígonos", "g", 130, COR)], XE, 440)
    E.frase(c, t, C["s22.a"] + 0.3, [("regulares", "g", 130, COR)], XE, 570)
    E.frase(c, t, C["s22.b"], ps("o ângulo do octógono", "i", 66), XE, 690, passo=0.12)
    E.frase(c, t, C["s22.c"], ps("e o piso de hexágonos", "i", 66), XE, 780, passo=0.12)
    E.foco(c, t, C["s22.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s22.d"] + 0.2, 0.4))
    E.frase(c, t, C["s22.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, poligono=b_poligono, triangulos=b_triangulos, formula=b_formula,
              diagonais=b_diagonais, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
