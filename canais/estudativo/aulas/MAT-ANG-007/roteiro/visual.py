"""Visual — Estudativo · MAT-ANG-007: congruência de triângulos (LLL, LAL, ALA e LAAo).
Linguagem da geometria plana (MAT-ANG-001 a 006): lados em tinta; lados iguais com o mesmo número de tracinhos (E.marcas_iguais);
ângulos iguais com a mesma cor (famílias COR, TINTA2 e AMBAR). Congruência = a cópia em papel (papel()) que gira, vira e
assenta sobre o outro triângulo. Nos casos, a parte que o caso usa fica destacada em COR (lado grosso ou cunha).
Erro em vermelho; certo em verde; medidas na grotesca; resposta na esfera.
Peças locais (as da MAT-ANG-004/005): tri(), canto(), triang(), rotulo(); e ainda forma() (triângulo-modelo girado e espelhado),
papel(), vareta(), compasso(), grosso() (lado destacado) e txt_lado(). Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-007_congruencia_de_triangulos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("congruente", "lll", "gravata", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
assert 50 + 60 + 70 == 180 and 50 + 60 == 110 and 180 - 110 == 70 and 50 + 30 == 80 and 180 - 80 == 100
assert 3 ** 2 + 4 ** 2 == 5 ** 2 and 3 + 3 == 6
assert abs(9 * math.sin(math.radians(50)) / math.sin(math.radians(100)) - 7) < 0.01  # BC = 7 bate com AB = 9, 50° e 30°
assert abs((4 ** 2 + 3 ** 2 - 6 ** 2) / (2 * 4 * 3) + 11 / 24) < 1e-9  # a gravata existe: cos M = −11/24
assert 6 * math.sin(math.radians(30)) < 4  # o arco de raio 4 corta a reta de 30° em dois pontos


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


def canto(c, t, t0, V, P, Q, rot=None, cor=None, r=80, tr=None, size=52, alfa=0.25, reto=None, a=1.0, rl=None):
    """ângulo interno PVQ com arco e cunha da cor da família, e a medida por fora do arco"""
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    g1, g2 = faixa_v(V, P, Q)
    q = ease_io(prog(t, t0, 0.5))
    cunha_m(c, V, g1, g1 + (g2 - g1) * q, r, cor, a, alfa=alfa, borda=5)
    if rot:
        s = rot(t) if callable(rot) else rot
        E.foco(c, t, tr if tr is not None else t0 + 0.3, 0.4, lambda k: rotulo(c, V, (g1 + g2) / 2, rl or r, s, COR if cor == E.COR else cor, size, k * a))


def triang(c, t, t0, A, B, C, nomes="ABC", tinta=TINTA, preenche=0.06, d=0.9, cor_f=None):
    """o contorno que se desenha em volta, com os nomes dos vértices"""
    if t < t0:
        return
    pts = [A, B, C]
    if preenche:
        path = skia.Path(); path.addPoly(pts, True)
        c.drawPath(path, M.paint(cor_f or E.COR, preenche * ep(t, t0 + d * 0.6, 0.5)))
    p = ease_io(prog(t, t0, d))
    for i, (P, Q) in enumerate(((A, B), (B, C), (C, A))):
        f = M.clamp(p * 3 - i)
        if f > 0:
            M.line(c, *P, lerp(P[0], Q[0], f), lerp(P[1], Q[1], f), tinta, 1.0, 6)
    if nomes:
        g = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)
        for i, (V, s) in enumerate(zip(pts, nomes)):
            ux, uy = V[0] - g[0], V[1] - g[1]
            n = math.hypot(ux, uy)
            E.foco(c, t, t0 + 0.3 + 0.15 * i, 0.4, lambda a, V=V, s=s, ux=ux / n, uy=uy / n: centro(c, s, V[0] + ux * 58, V[1] + uy * 58 + 22, 58, "g", tinta, a))


def txt_lado(c, P, Q, s, G, size=50, cor=None, a=1.0, gap=18):
    """medida de um lado, do lado de fora (longe de G)"""
    if a <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
    if (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 < (mx - G[0]) ** 2 + (my - G[1]) ** 2:
        nx, ny = -nx, -ny
    E._cola(c, s, mx, my, nx, ny, gap, size, "b", cor or COR, a)


def grosso(c, P, Q, cor, a, larg=12):
    """lado em destaque (o lado que o caso usa)"""
    if a > 0:
        M.line(c, *P, *Q, cor, a, larg)


def forma(S, G, rot=0.0, sx=1.0, k=1.0):
    """triângulo-modelo S (em torno da origem) girado rot graus, espelhado sx e posto no centro G"""
    r = math.radians(rot)
    co, si = math.cos(r), math.sin(r)
    return [(G[0] + k * (sx * x * co - y * si), G[1] + k * (sx * x * si + y * co)) for x, y in S]


def papel(c, pts, cor, a=1.0, alfa=0.16, sombra=True, larg=6):
    """triângulo recortado em papel, com sombra e contorno na cor"""
    if a <= 0:
        return
    path = skia.Path(); path.addPoly(pts, True)
    if sombra:
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.18 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
        c.save(); c.translate(6, 12); c.drawPath(path, s); c.restore()
        c.drawPath(path, M.paint("#FFFFFF", a))
    c.drawPath(path, M.paint(cor, alfa * a))
    p = M.paint(cor, a, stroke=larg)
    p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, p)


def contorno(c, pts, cor, a=1.0, larg=6, dash=None, alfa=0.0):
    if a <= 0:
        return
    path = skia.Path(); path.addPoly(pts, True)
    if alfa:
        c.drawPath(path, M.paint(cor, alfa * a))
    p = M.paint(cor, a, stroke=larg)
    p.setStrokeJoin(skia.Paint.kRound_Join)
    if dash:
        p.setPathEffect(skia.DashPathEffect.Make(dash, 0))
    c.drawPath(path, p)


def vareta(c, P, Q, s, cor=TINTA, a=1.0, size=50, lado=1):
    """vareta de madeira: barra grossa com pontas, e a medida ao lado"""
    if a <= 0:
        return
    M.line(c, *P, *Q, cor, a, 14)
    for V in (P, Q):
        c.drawCircle(*V, 12, M.paint(cor, a))
    if s:
        ux, uy = E._uni(*P, *Q)
        E._cola(c, s, (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2, uy * lado, -ux * lado, 20, size, "b", COR, a)


# modelo de triângulo escaleno para recortes e cópias (centro na origem)
S = [(-220, 120), (260, 120), (-40, -240)]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    X = 1560
    peq = tri((120, 860), 380, 60, 70)
    gra = tri((600, 860), 560, 60, 70)

    def um():
        for (A, B, Cc), r, size, t0 in ((peq, 52, 40, ka), (gra, 80, 52, ka + 0.6)):
            triang(c, t, t0, A, B, Cc, nomes=None)
        for (A, B, Cc), r, size in ((peq, 52, 42), (gra, 80, 54)):
            canto(c, t, lerp(ka, kb, 0.28), A, B, Cc, "50°", E.COR, r, size=size)
            canto(c, t, lerp(ka, kb, 0.40), B, A, Cc, "60°", TINTA2, r, size=size)
            canto(c, t, lerp(ka, kb, 0.52), Cc, A, B, "70°", AMBAR, r, size=size)
        if t >= kc:
            p = ease_io(prog(t, kc + 0.2, 1.4))
            pts = [(lerp(P[0], Q[0], p), lerp(P[1], Q[1], p)) for P, Q in zip(peq, gra)]
            contorno(c, pts, E.COR, 1.0, 6, dash=[16, 12], alfa=0.1)
        E.frase(c, t, ka, [("mesmos", "g", 84, COR)] + ps("ângulos", "i", 84), X, 300, "center", 0.12)
        E.frase(c, t, lerp(ka, kb, 0.66), ps("são", "i", 84) + [("iguais?", "g", 90)], X, 450, "center", 0.12)
        E.frase(c, t, kb, ps("caiu na", "i", 70) + [("armadilha", "g", 74, ERRADO)], X, 600, "center", 0.12)
        E.frase(c, t, kc, [("mesmo formato", "g", 68, COR)], X, 760, "center")
        E.frase(c, t, lerp(kc, C["s01.end"], 0.55), ps("tamanho diferente", "i", 68), X, 860, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), ps("quais medidas", "i", 84) + [("bastam", "g", 96, COR)], XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.55), ps("para garantir", "i", 84), XE, 600, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.7), ps("triângulos", "i", 84) + [("iguais", "g", 96)], XE, 740, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 820
    itens = (("s03.b", "os ângulos do triângulo", "somam 180°"), ("s03.c", "mesmos tracinhos", "lados iguais"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
    # dois lados com um tracinho, no canto da 2ª caixa
    q = ep(t, C["s03.c"] + 0.6, 0.4)
    if q > 0:
        for (P, Q) in (((1520, 610), (1700, 610)), ((1520, 680), (1700, 680))):
            M.line(c, *P, *Q, TINTA, q, 6)
            E.marcas_iguais(c, P, Q, 1, COR, q)
    py = lerp(420, 700, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 920, "left", 0.12)


# ---------------- o que é congruente ----------------
def b_congruente(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    G1, G2 = (560, 680), (1300, 680)

    def um():
        E.frase(c, t, a4, [("congruentes", "g", 120, COR)], W / 2, 210, "center")
        E.frase(c, t, b4, ps("mesmo", "i", 66) + [("formato", "g", 66)] + ps("e mesmo", "i", 66) + [("tamanho", "g", 66)], W / 2, 330, "center", 0.12)
        tv = lerp(b4, c4, 0.45)
        if t >= tv:
            contorno(c, forma(S, G2), TINTA, ep(t, tv, 0.5), 6, alfa=0.05)
            # a cópia: vira (espelho) e gira até cobrir o outro
            f = ease_io(prog(t, c4, 0.7))
            g = ease_io(prog(t, c4 + 0.7, 1.3))
            G = (lerp(G1[0], G2[0], g), lerp(G1[1], G2[1], g))
            papel(c, forma(S, G, lerp(150, 0, g), lerp(-1, 1, f)), E.COR, ep(t, tv, 0.5), alfa=0.18 if g < 1 else 0.28)
        E.foco(c, t, c4 + 2.1, 0.4, lambda a: E.selo(c, G2[0] + 330, G2[1] - 220, 50, True, a))
        E.frase(c, t, c4, ps("cobre", "i", 66) + [("certinho", "g", 66, CERTO)], W / 2, 960, "center", 0.12)
        E.frase(c, t, lerp(c4, C["s04.end"], 0.45), ps("pode girar ou virar", "i", 56, TINTA2), W / 2, 1040, "center", 0.1)
    E.saida(c, t, C["s05"] - 0.1, um)

    if t < C["s05"]:
        return
    A, B, Cc = tri((200, 860), 640, 55, 65)
    X = 1460
    triang(c, t, C["s05"], A, B, Cc, nomes=None)
    for i, (P, Q) in enumerate(((A, B), (B, Cc), (Cc, A))):
        grosso(c, P, Q, E.COR, ep(t, a5 + 0.25 * i, 0.3))
    canto(c, t, lerp(a5, b5, 0.35), A, B, Cc, None, E.COR, 70)
    canto(c, t, lerp(a5, b5, 0.42), B, A, Cc, None, TINTA2, 70)
    canto(c, t, lerp(a5, b5, 0.49), Cc, A, B, None, AMBAR, 70)

    def seis():
        E.frase(c, t, a5, [("3 lados", "g", 80)], X, 300, "center")
        E.frase(c, t, lerp(a5, b5, 0.35), ps("+", "g", 80, TINTA2) + [("3 ângulos", "g", 80)], X, 420, "center", 0.12)
        E.foco(c, t, lerp(a5, b5, 0.62), 0.5, lambda a: E.pilula(c, "6 medidas", X, 560, 76, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, b5 - 0.1, seis)
    if t >= b5:
        E.frase(c, t, b5, ps("não precisa de", "i", 64) + [("todas", "g", 70, ERRADO)], X, 260, "center", 0.12)
        E.frase(c, t, lerp(b5, c5, 0.45), [("3 medidas", "g", 76, COR)], X, 390, "center")
        E.frase(c, t, lerp(b5, c5, 0.55), ps("no lugar certo", "i", 64), X, 480, "center", 0.12)
        E.frase(c, t, c5, [("4", "g", 90, COR)] + ps("casos", "i", 76), X, 640, "center", 0.12)
        for i, (s, x, y) in enumerate((("LLL", 1290, 780), ("LAL", 1630, 780), ("ALA", 1290, 910), ("LAAo", 1630, 910))):
            E.foco(c, t, c5 + 0.4 + 0.2 * i, 0.4, lambda a, s=s, x=x, y=y: E.pilula(c, s, x, y, 64, "g", a=a, cor=E.SOBRE))


# ---------------- LLL ----------------
def b_lll(c, t, C, b):
    a6, b6, c6, a7, b7 = C["s06.a"], C["s06.b"], C["s06.c"], C["s07.a"], C["s07.b"]
    X = 1450
    # triângulo 3, 4, 5 (u = 110 px por cm): B no canto reto
    B, Cc, A = (260, 860), (700, 860), (260, 530)
    alvo = ((B, A, "3 cm", 1), (B, Cc, "4 cm", -1), (A, Cc, "5 cm", 1))
    parado = (((180, 330), (510, 330)), ((180, 480), (620, 480)), ((180, 630), (730, 630)))

    def um():
        E.frase(c, t, a6, [("LLL", "g", 150, COR)], X, 320, "center")
        E.frase(c, t, a6 + 0.6, ps("lado, lado, lado", "i", 66), X, 430, "center", 0.12)
        E.frase(c, t, b6, [("3, 4 e 5 cm", "g", 76)], X, 590, "center")
        E.frase(c, t, c6, ps("sempre sai", "i", 66) + [("o mesmo", "g", 70, COR)], X, 750, "center", 0.12)
        for i, ((P1, Q1), (P2, Q2, s, lado)) in enumerate(zip(parado, alvo)):
            k = ep(t, b6 + 0.4 * i, 0.4)
            p = ease_io(prog(t, c6 + 0.3 * i, 1.0))
            P = (lerp(P1[0], P2[0], p), lerp(P1[1], P2[1], p))
            Q = (lerp(Q1[0], Q2[0], p), lerp(Q1[1], Q2[1], p))
            vareta(c, P, Q, s, TINTA, k, 50, lado if p > 0.5 else 1)
        # a cópia montada de outro jeito cai em cima: é o mesmo triângulo
        tc = c6 + 1.6
        if t >= tc:
            G = ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3)
            T = [(P[0] - G[0], P[1] - G[1]) for P in (A, B, Cc)]
            g = ease_io(prog(t, tc, 1.3))
            Gc = (lerp(G[0] + 300, G[0], g), lerp(G[1] - 250, G[1], g))
            contorno(c, forma(T, Gc, lerp(-120, 0, g), lerp(-1, 1, ease_io(prog(t, tc, 0.6)))), E.COR, ep(t, tc, 0.3), 6, dash=[16, 12], alfa=0.12)
            E.foco(c, t, tc + 1.4, 0.4, lambda a: E.selo(c, 560, 600, 44, True, a))
    E.saida(c, t, C["s07"] - 0.1, um)

    if t < C["s07"]:
        return

    def dois():
        E.frase(c, t, C["s07"], ps("telhado e portão", "i", 72), W / 2, 200, "center", 0.12)
        E.frase(c, t, a7, ps("com os lados fixos,", "i", 60), W / 2, 300, "center", 0.12)
        # quadrado de varetas entorta; triângulo não
        osc = math.sin(2 * math.pi * max(0.0, t - a7 - 0.6) / 1.6) * ep(t, a7 + 0.6, 0.6)
        dx = 150 * osc
        q = ep(t, C["s07"] + 0.3, 0.5)
        P = [(300, 880), (640, 880), (640 + dx, 540), (300 + dx, 540)]
        for i in range(4):
            vareta(c, P[i], P[(i + 1) % 4], None, TINTA, q)
        Tt = [(1200, 880), (1620, 880), (1410, 520)]
        for i in range(3):
            vareta(c, Tt[i], Tt[(i + 1) % 3], None, TINTA, q)
        E.frase(c, t, a7 + 0.8, [("entorta", "g", 66, ERRADO)], 470 + dx * 0.3, 1000, "center")
        E.frase(c, t, a7 + 1.4, [("não entorta", "g", 66, CERTO)], 1410, 1000, "center")
    E.saida(c, t, b7 - 0.1, dois)
    if t >= b7:
        T = [(-230, 130), (230, 130), (-60, -220)]
        for G, rot, t0 in (((560, 600), 0, b7), ((1360, 600), 160, b7 + 0.4)):
            pts = forma(T, G, rot)
            contorno(c, pts, TINTA, ep(t, t0, 0.5), 6, alfa=0.06)
            for i in range(3):
                E.marcas_iguais(c, pts[i], pts[(i + 1) % 3], i + 1, COR, ep(t, t0 + 0.6 + 0.2 * i, 0.3))
        E.frase(c, t, b7, ps("3 lados iguais", "i", 70) + [("→", "g", 70, TINTA2)], W / 2, 220, "center", 0.12)
        E.foco(c, t, b7 + 1.4, 0.5, lambda a: E.pilula(c, "congruentes", W / 2, 950, 80, "g", a=a, cor=E.SOBRE))


# ---------------- LAL ----------------
def compasso(c, V, L, ab, a=1.0, cor=TINTA):
    """compasso de pernas L abertas ab graus, pendurado no pino V. Devolve as pontas (esquerda, direita)"""
    h = math.radians(ab / 2)
    Pe = (V[0] - L * math.sin(h), V[1] + L * math.cos(h))
    Pd = (V[0] + L * math.sin(h), V[1] + L * math.cos(h))
    if a > 0:
        M.rrect(c, V[0] - 16, V[1] - 90, 32, 70, 10, cor, a)
        for P in (Pe, Pd):
            M.line(c, *V, *P, cor, a, 12)
        c.drawCircle(*V, 24, M.paint(cor, a))
        c.drawCircle(*V, 9, M.paint("#FFFFFF", a))
        c.drawCircle(*Pd, 9, M.paint(E.COR, a))  # grafite
    return Pe, Pd


def b_lal(c, t, C, b):
    a8, b8, c8, d8, e8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"], C["s08.e"]
    X = 1450
    V, L = (560, 230), 520
    # antes de travar, a abertura balança; no {c}, trava em 44°
    solto = 1 - ep(t, c8, 0.5)
    ab = 62 + 16 * math.sin(2 * math.pi * max(0.0, t - C["s08"]) / 2.2) * solto
    Pe, Pd = compasso(c, V, L, ab, ep(t, C["s08"] + 0.2, 0.5))
    if t >= b8:
        k = ep(t, b8, 0.4)
        for P in (Pe, Pd):
            grosso(c, V, P, E.COR, k, 14)
        E._cola(c, "lado", (V[0] + Pe[0]) / 2, (V[1] + Pe[1]) / 2, -1, 0, 30, 50, "b", COR, k)
        E._cola(c, "lado", (V[0] + Pd[0]) / 2, (V[1] + Pd[1]) / 2, 1, 0, 30, 50, "b", COR, k)
    if t >= c8:
        g1, g2 = faixa_v(V, Pe, Pd)
        q = ease_io(prog(t, c8, 0.5))
        cunha_m(c, V, g1, g1 + (g2 - g1) * q, 130, AMBAR, 1.0, alfa=0.3, borda=5)
        E.foco(c, t, c8 + 0.3, 0.4, lambda a: centro(c, "ângulo", V[0], V[1] + 200, 48, "b", AMBAR, a))
    if t >= d8:
        M.line(c, *Pe, *Pd, E.COR, 1.0, 6, dash=E.TRACO, progress=ease_io(prog(t, d8, 0.6)))
        E.foco(c, t, d8 + 0.5, 0.4, lambda a: centro(c, "fixa", V[0], Pe[1] + 80, 54, "g", COR, a))
    E.frase(c, t, a8, [("LAL", "g", 150, COR)], X, 300, "center")
    E.frase(c, t, a8 + 0.6, ps("lado, ângulo, lado", "i", 66), X, 410, "center", 0.12)
    E.frase(c, t, b8, ps("pernas:", "i", 60) + [("tamanho fixo", "g", 60)], X, 540, "center", 0.12)
    E.frase(c, t, c8, ps("abertura", "i", 60) + [("travada", "g", 60, AMBAR)], X, 640, "center", 0.12)
    E.frase(c, t, d8, ps("as pontas:", "i", 60) + [("fixas", "g", 60, COR)], X, 740, "center", 0.12)
    if t >= e8:
        E.foco(c, t, e8, 0.5, lambda a: E.pilula(c, "L  A  L", X, 880, 80, "g", a=a, cor=E.SOBRE))
        E.foco(c, t, e8 + 0.6, 0.4, lambda a: centro(c, "o ângulo no meio", X, 1000, 50, "i", AMBAR, a))


# ---------------- ALA ----------------
def b_ala(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    X = 1480
    A, B, Cc = tri((200, 860), 720, 55, 65)
    G = ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3)
    E.segmento(c, t, a9, B, Cc, None, pontas=True)
    grosso(c, B, Cc, E.COR, ep(t, a9 + 0.6, 0.4))
    E.foco(c, t, a9 + 0.8, 0.4, lambda a: txt_lado(c, B, Cc, "lado", G, 50, COR, a))
    if t >= b9:
        canto(c, t, b9, B, A, Cc, None, TINTA2, 90)
        canto(c, t, b9 + 0.4, Cc, A, B, None, AMBAR, 90)
        # as retas saem das pontas já inclinadas
        for V, P, t0 in ((B, A, b9 + 0.5), (Cc, A, b9 + 0.9)):
            L = math.dist(V, P) * 1.22
            ux, uy = E._uni(*V, *P)
            q = ease_io(prog(t, t0, 1.2))
            M.line(c, *V, V[0] + ux * L * q, V[1] + uy * L * q, TINTA2, 1.0, 5, dash=E.TRACO)
    if t >= c9:
        for V in (B, Cc):
            M.line(c, *V, *A, TINTA, 1.0, 6, progress=ease_io(prog(t, c9, 0.6)))
        k = ease_back(prog(t, c9 + 0.5, 0.4))
        if k > 0:
            c.drawCircle(*A, 16 * k, M.paint(E.COR))
        path = skia.Path(); path.addPoly([A, B, Cc], True)
        c.drawPath(path, M.paint(E.COR, 0.08 * ep(t, c9 + 0.6, 0.5)))
    E.frase(c, t, a9, [("ALA", "g", 150, COR)], X, 300, "center")
    E.frase(c, t, a9 + 0.6, ps("ângulo, lado, ângulo", "i", 64), X, 410, "center", 0.12)
    E.frase(c, t, b9, ps("os ângulos", "i", 62) + [("das pontas", "g", 62)], X, 560, "center", 0.12)
    E.frase(c, t, c9, ps("as retas se encontram", "i", 58), X, 700, "center", 0.12)
    E.frase(c, t, c9 + 0.8, [("num ponto só", "g", 66, COR)], X, 790, "center")
    E.frase(c, t, lerp(c9, C["s09.end"], 0.6), ps("triângulo", "i", 60) + [("decidido", "g", 62)], X, 930, "center", 0.12)


# ---------------- LAAo ----------------
def b_laao(c, t, C, b):
    a10, b10, c10, d10, e10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s10.e"]
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    X = 1460
    A, B, Cc = tri((200, 860), 720, 60, 50)
    G = ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3)

    def um():
        triang(c, t, C["s10"], A, B, Cc)
        grosso(c, B, Cc, E.COR, ep(t, a10 + 0.6, 0.4))
        E.foco(c, t, a10 + 0.8, 0.4, lambda a: txt_lado(c, B, Cc, "lado", G, 50, COR, a))
        canto(c, t, b10, B, A, Cc, None, TINTA2, 90)
        apaga = 1 - 0.65 * ep(t, e10, 0.5)
        canto(c, t, c10, A, B, Cc, None, E.COR, 80, a=apaga)
        if t >= c10:  # oposto: de frente para o lado
            M.line(c, *A, (B[0] + Cc[0]) / 2, B[1] - 14, E.COR, apaga * 0.8, 4, dash=[10, 10], progress=ease_io(prog(t, c10 + 0.3, 0.6)))
        canto(c, t, d10, Cc, A, B, (lambda tt: "?" if tt < d10 + 1.6 else None), AMBAR, 90, size=56)
        if t >= e10:  # vira ALA: o lado com ângulo nas duas pontas
            k = 0.5 + 0.5 * math.sin(2 * math.pi * (t - e10) / 1.0)
            for V, cor in ((B, TINTA2), (Cc, AMBAR)):
                c.drawCircle(*V, 22 + 6 * k, M.paint(cor, 0.5 * ep(t, e10, 0.4)))
        E.frase(c, t, a10, [("LAAo", "g", 140, COR)], X, 290, "center")
        E.frase(c, t, a10 + 0.6, ps("lado, ângulo e", "i", 58) + [("ângulo oposto", "g", 58)], X, 390, "center", 0.12)
        E.frase(c, t, b10, ps("um", "i", 58) + [("na ponta", "g", 58, TINTA2)], X, 520, "center", 0.12)
        E.frase(c, t, c10, ps("um", "i", 58) + [("de frente", "g", 58, COR)], X, 610, "center", 0.12)
        fcen(c, t, d10, "180 − os dois", X, 760, 70, AMBAR)
        E.frase(c, t, e10, ps("vira", "i", 64) + [("ALA", "g", 80, COR)], X, 910, "center", 0.12)
    E.saida(c, t, C["s11"] - 0.1, um)
    if t < C["s11"]:
        return
    for i, s in enumerate(("LLL", "LAL", "ALA", "LAAo")):
        E.foco(c, t, a11 + 0.25 * i, 0.5, lambda a, i=i, s=s: E.pilula(c, s, 330 + i * 420, 330, 80, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, a11 + 0.2, ps("nos livros: as iniciais", "i", 56, TINTA2), W / 2, 460, "center", 0.1)
    E.frase(c, t, lerp(a11, b11, 0.6), ps("e três ângulos?", "i", 66), W / 2, 620, "center", 0.12)
    E.foco(c, t, b11, 0.4, lambda a: centro(c, "AAA", 760, 780, 110, "g", ERRADO, a))
    if t >= b11 + 0.4:
        E.risco(c, 630, 760, 890, 720, t, b11 + 0.4, largura=12)
    E.frase(c, t, b11 + 0.3, ps("não é caso", "i", 66, ERRADO), 1240, 770, "center", 0.12)
    E.frase(c, t, c11, ps("mesmo formato, tamanho diferente:", "i", 52), W / 2, 920, "center", 0.08)
    E.frase(c, t, c11 + 0.5, [("semelhança", "g", 64, COR)] + ps("(outra aula)", "i", 52, TINTA2), W / 2, 1010, "center", 0.12)


# ---------------- exemplo: a gravata ----------------
UG = 105
MG = (700, 560)
GA, GB = pt(MG, 4 * UG, 121.35), pt(MG, 3 * UG, 238.65)
GC, GD = pt(MG, 4 * UG, 301.35), pt(MG, 3 * UG, 58.65)
assert abs(math.dist(GA, GB) - 6 * UG) < 1.5 and abs(math.dist(GC, GD) - 6 * UG) < 1.5


def b_gravata(c, t, C, b):
    A, B, Cc, D, Mm = GA, GB, GC, GD, MG
    X = 1480
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    a13, b13, c13, d13, e13, f13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"], C["s13.f"]
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    G1 = ((A[0] + B[0] + Mm[0]) / 3, (A[1] + B[1] + Mm[1]) / 3)
    G2 = ((Cc[0] + D[0] + Mm[0]) / 3, (Cc[1] + D[1] + Mm[1]) / 3)
    # os dois triângulos pintados
    if t >= c13:
        path = skia.Path(); path.addPoly([A, Mm, B], True)
        c.drawPath(path, M.paint(E.COR, 0.12 * ep(t, c13, 0.4)))
        path = skia.Path(); path.addPoly([Cc, Mm, D], True)
        c.drawPath(path, M.paint(AMBAR, 0.14 * ep(t, c13 + 0.4, 0.4)))
    E.segmento(c, t, b12, A, Cc, None, rotulos=("A", "C"), pontas=True, size=58)
    E.segmento(c, t, b12 + 0.7, B, D, None, rotulos=("B", "D"), pontas=True, size=58)
    E.foco(c, t, b12 + 1.4, 0.4, lambda a: (c.drawCircle(*Mm, 11, M.paint(TINTA, a)), centro(c, "M", Mm[0], Mm[1] + 120, 58, "g", TINTA, a)))
    # medidas e tracinhos
    q = ep(t, c12, 0.4)
    for P in (A, Cc):
        E.marcas_iguais(c, P, Mm, 1, COR, q)
        txt_lado(c, P, Mm, "4", (Mm[0], Mm[1] + 1) if P == A else (Mm[0], Mm[1] - 1), 50, COR, q, gap=30)
    q = ep(t, d12, 0.4)
    for P in (B, D):
        E.marcas_iguais(c, P, Mm, 2, TINTA2, q)
        txt_lado(c, P, Mm, "3", (Mm[0], Mm[1] - 1) if P == B else (Mm[0], Mm[1] + 1), 50, TINTA2, q, gap=32)
    # AB = 6 e CD = ?
    if t >= a13:
        M.line(c, *A, *B, TINTA, 1.0, 6, progress=ease_io(prog(t, a13, 0.5)))
        E.foco(c, t, a13 + 0.4, 0.4, lambda a: txt_lado(c, A, B, "6", G1, 54, COR, a))
    if t >= b13:
        M.line(c, *Cc, *D, TINTA, 1.0, 6, progress=ease_io(prog(t, b13, 0.5)))
        E.foco(c, t, b13 + 0.4, 0.4, lambda a: txt_lado(c, Cc, D, "?" if t < c14 + 0.3 else "6", G2, 58, ERRADO if t < c14 + 0.3 else CERTO, a))
    # os ângulos em M: opostos pelo vértice, a mesma cor
    canto(c, t, e13, Mm, A, B, None, E.COR, 70)
    canto(c, t, e13 + 0.4, Mm, Cc, D, None, E.COR, 70)
    # destaques do LAL
    grosso(c, A, Mm, E.COR, ep(t, d13, 0.3) * (1 - ep(t, e13, 0.3)))
    grosso(c, Cc, Mm, E.COR, ep(t, d13, 0.3) * (1 - ep(t, e13, 0.3)))
    grosso(c, B, Mm, TINTA2, ep(t, f13, 0.3) * (1 - ep(t, a14, 0.3)))
    grosso(c, D, Mm, TINTA2, ep(t, f13, 0.3) * (1 - ep(t, a14, 0.3)))
    if t >= b14:  # de frente para o ângulo de M
        k = ep(t, b14, 0.4)
        grosso(c, A, B, E.COR, k)
        grosso(c, Cc, D, E.COR, k)
        for P, Q in ((A, B), (Cc, D)):
            m = ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
            M.line(c, *Mm, *m, E.COR, 0.8 * k, 4, dash=[10, 10], progress=ease_io(prog(t, b14 + 0.2, 0.6)))

    def um():
        E.frase(c, t, a12, ps("descobrir", "i", 64) + [("sem medir", "g", 70, COR)], X, 220, "center", 0.12)
        E.frase(c, t, c12, [("AM = MC = 4", "g", 64, COR)], X, 400, "center")
        E.frase(c, t, d12, [("BM = MD = 3", "g", 64, TINTA2)], X, 520, "center")
    E.saida(c, t, C["s13"] - 0.1, um)
    if t >= C["s13"]:
        def dois():
            E.frase(c, t, a13, [("AB = 6", "g", 66)] + ps("e", "i", 60) + [("CD = ?", "g", 66, ERRADO)], X, 220, "center", 0.12)
            E.frase(c, t, c13, [("AMB", "g", 62, COR)] + ps("e", "i", 60) + [("CMD", "g", 62, AMBAR)], X, 340, "center", 0.12)
            E.frase(c, t, d13, [("L", "g", 66, COR)] + ps("4 e 4", "i", 62), X, 480, "center", 0.12)
            E.frase(c, t, e13, [("A", "g", 66, COR)] + ps("opostos pelo vértice", "i", 54), X, 590, "center", 0.12)
            E.frase(c, t, f13, [("L", "g", 66, COR)] + ps("3 e 3", "i", 62), X, 700, "center", 0.12)
        E.saida(c, t, C["s14"] - 0.1, dois)
    if t >= C["s14"]:
        E.foco(c, t, a14, 0.5, lambda a: E.pilula(c, "LAL", X, 260, 90, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, a14 + 0.6, [("congruentes", "g", 66, COR)], X, 400, "center")
        E.frase(c, t, b14, ps("de frente para o", "i", 58) + [("M", "g", 62, COR)], X, 540, "center", 0.12)
        E.frase(c, t, b14 + 0.8, [("AB", "g", 62)] + ps("e", "i", 58) + [("CD", "g", 62)], X, 630, "center", 0.12)
        bola_txt(c, t, c14, "CD = 6", X, 820, 130, 66)


# ---------------- erro: lado, lado e ângulo de fora ----------------
UE = 120
EA = (200, 900)
EB = (EA[0] + 6 * UE, EA[1])
_d = 6 * math.cos(math.radians(30))
_r = math.sqrt(4 ** 2 - (6 * math.sin(math.radians(30))) ** 2)
EC1, EC2 = pt(EA, (_d - _r) * UE, 30), pt(EA, (_d + _r) * UE, 30)
assert abs(math.dist(EB, EC1) - 4 * UE) < 1 and abs(math.dist(EB, EC2) - 4 * UE) < 1


def b_erro(c, t, C, b):
    A, B, C1, C2 = EA, EB, EC1, EC2
    X = 1560
    a15, b15 = C["s15.a"], C["s15.b"]
    a16, b16, c16, d16, e16, f16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"], C["s16.f"]
    E.frase(c, t, C["s15"], [("cuidado", "g", 90, ERRADO)] + ps("com este erro", "i", 84), W / 2, 150, "center", 0.12)

    def um():
        E.frase(c, t, a15, ps("o ângulo", "i", 70) + [("fora do lugar", "g", 74, ERRADO)], W / 2, 430, "center", 0.12)
        E.frase(c, t, b15, ps("2 lados e um ângulo que", "i", 62) + [("não está entre eles", "g", 62)], W / 2, 600, "center", 0.1)
        E.foco(c, t, b15 + 1.0, 0.5, lambda a: E.pilula(c, "L  L  A", W / 2, 780, 90, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s16"] - 0.1, um)
    if t < C["s16"]:
        return
    # a reta de 30° saindo de A e o lado AB
    if t >= a16:
        L = (_d + _r) * UE + 170
        q = ease_io(prog(t, a16, 0.8))
        M.line(c, *A, A[0] + L * math.cos(math.radians(30)) * q, A[1] - L * math.sin(math.radians(30)) * q, TINTA, 1.0, 6)
        cunha_m(c, A, 0, 30 * ease_io(prog(t, a16 + 0.4, 0.5)), 120, E.COR, 1.0, alfa=0.25, borda=5)
        E.foco(c, t, a16 + 0.7, 0.4, lambda a: rotulo(c, A, 15, 120, "30°", COR, 50, a))
        E.foco(c, t, a16 + 0.3, 0.4, lambda a: centro(c, "A", A[0] - 50, A[1] + 20, 58, "g", TINTA, a))
    E.segmento(c, t, b16, A, B, None, pontas=True)
    E.foco(c, t, b16 + 0.5, 0.4, lambda a: (centro(c, "6", (A[0] + B[0]) / 2, B[1] + 70, 54, "b", COR, a),
                                            centro(c, "B", B[0] + 50, B[1] + 20, 58, "g", TINTA, a)))
    # o lado de 4 preso no B: gira e encosta na reta em dois pontos
    g1, g2 = dirg(B, C1), dirg(B, C2)
    if t >= c16:
        phi = lerp(45, 175, ease_io(prog(t, d16, 2.4)))
        ver = 1 - ep(t, e16, 0.4)
        P = pt(B, 4 * UE, phi)
        M.line(c, *B, *P, TINTA2, ver * ep(t, c16, 0.3), 7)
        c.drawCircle(*P, 10, M.paint(TINTA2, ver * ep(t, c16, 0.3)))
        E.foco(c, t, c16 + 0.2, 0.4, lambda a: rotulo(c, ((B[0] + P[0]) / 2, (B[1] + P[1]) / 2), phi - 90, 0, "4", TINTA2, 50, a * ver))
        if t >= d16:
            ret = skia.Rect.MakeXYWH(B[0] - 4 * UE, B[1] - 4 * UE, 8 * UE, 8 * UE)
            tr = M.paint(TINTA2, 0.7, stroke=3)
            tr.setPathEffect(skia.DashPathEffect.Make([10, 10], 0))
            c.drawArc(ret, -45, -(phi - 45), False, tr)
        # os dois encontros
        for P_, cor, ok in ((C1, E.COR, t >= d16 and phi >= g1), (C2, AMBAR, t >= d16 and phi >= g2)):
            if ok:
                c.drawCircle(*P_, 16, M.paint(cor))
    if t >= e16:
        for (P_, cor, t0, nome) in ((C1, E.COR, e16, "C"), (C2, AMBAR, e16 + 0.5, "C'")):
            k = ep(t, t0, 0.4)
            contorno(c, [A, B, P_], cor, k, 6, alfa=0.14)
            E.foco(c, t, t0, 0.4, lambda a, P_=P_, nome=nome, cor=cor: centro(c, nome, P_[0] - 10, P_[1] - 34, 56, "g", cor, a))
            E.foco(c, t, t0 + 0.2, 0.4, lambda a, P_=P_, cor=cor: rotulo(c, ((B[0] + P_[0]) / 2, (B[1] + P_[1]) / 2), dirg(B, P_) - 90, 0, "4", cor, 48, a))
    E.frase(c, t, a16, [("30°", "g", 64, COR)] + ps("em A", "i", 60), X, 360, "center", 0.12)
    E.frase(c, t, b16, [("AB = 6", "g", 64)], X, 460, "center")
    E.frase(c, t, c16, [("BC = 4", "g", 64, TINTA2)], X, 560, "center")
    E.frase(c, t, d16, ps("encosta em", "i", 60) + [("2 pontos", "g", 64)], X, 680, "center", 0.12)
    E.frase(c, t, e16, [("2 triângulos", "g", 66, ERRADO)], X, 790, "center")
    if t >= f16:
        E.foco(c, t, f16, 0.5, lambda a: E.pilula(c, "LLA não garante", X, 930, 66, "g", fundo=ERRADO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    a18, b18, c18, d18, e18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"], C["s18.e"]
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]

    def regra():
        E.frase(c, t, a17, [("2 ângulos", "g", 120, BR)], W / 2, 330, "center")
        E.frase(c, t, a17 + 0.7, ps("valem por", "i", 84, CLARO) + [("3", "g", 110, BR)], W / 2, 480, "center", 0.12)
        fcen(c, t, b17, "3º = 180 − os dois", W / 2, 660, 80, CLARO)
        E.frase(c, t, c17, ps("sempre cai em", "i", 70, CLARO) + [("ALA", "g", 96, BR)], W / 2, 850, "center", 0.12)
    E.saida(c, t, C["s18"] - 0.1, regra)

    if C["s18"] <= t < C["s19"] + 0.4:
        def ex():
            X = 1500
            A, B, Cc = tri((200, 880), 760, 50, 70)
            triang(c, t, C["s18"], A, B, Cc, tinta=BR, preenche=0.12)
            grosso(c, B, Cc, CLARO, ep(t, a18, 0.4))
            E.foco(c, t, a18 + 0.3, 0.4, lambda a: centro(c, "8", (B[0] + Cc[0]) / 2, B[1] + 80, 64, "b", CLARO, a))
            canto(c, t, b18, B, A, Cc, "50°", CLARO, 90)
            canto(c, t, c18, A, B, Cc, "60°", AMBAR, 80)
            canto(c, t, d18, Cc, A, B, (lambda tt: "?" if tt < d18 + 1.0 else "70°"), BR, 90)
            fcen(c, t, lerp(c18, d18, 0.5), "50 + 60 = 110", X, 330, 80, CLARO)
            fcen(c, t, d18, "180 − 110 = 70", X, 470, 80, BR)
            E.frase(c, t, e18, [("8", "g", 76, BR)] + ps("entre", "i", 64, CLARO) + [("50°", "g", 66, CLARO)] + ps("e", "i", 64, CLARO) + [("70°", "g", 66, BR)], X, 640, "center", 0.12)
            E.foco(c, t, e18 + 0.9, 0.5, lambda a: E.pilula(c, "ALA", X, 800, 90, "g", a=a, cor=E.SOBRE))
        E.saida(c, t, C["s19"] - 0.1, ex)
    if t >= C["s19"]:
        E.frase(c, t, a19, ps("porque a soma é sempre", "i", 66, CLARO) + [("180°", "g", 80, BR)], W / 2, 280, "center", 0.12)
        E.frase(c, t, b19, ps("não compensa com", "i", 62, CLARO), W / 2, 470, "center", 0.12)
        E.foco(c, t, b19 + 0.3, 0.5, lambda a: E.pilula(c, "LLL", 700, 620, 84, "g", a=a, cor=E.SOBRE))
        E.foco(c, t, c19, 0.5, lambda a: E.pilula(c, "LAL", 1220, 620, 84, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, c19 + 0.5, ps("ângulo no meio", "i", 52, CLARO), 1220, 740, "center", 0.1)
        E.frase(c, t, lerp(c19, C["s19.end"], 0.6), ps("o caso", "i", 70, CLARO) + [("já está pronto", "g", 74, BR)], W / 2, 920, "center", 0.12)


# ---------------- questão ----------------
UQ = 70
QA, QB = (170, 470), (170 + 9 * UQ, 470)
QC = pt(QA, 9 * UQ * math.sin(math.radians(30)) / math.sin(math.radians(100)), 50)
QQ, QP = (170, 900), (170 + 9 * UQ, 900)
QR = pt(QQ, 9 * UQ * math.sin(math.radians(50)) / math.sin(math.radians(100)), 30)


def fig_q(c, t, t1, t2, qr="?", r_="?", tq=None):
    """os dois triângulos da questão: ABC entra em t1, PQR em t2"""
    A, B, Cc, P, Q, R = QA, QB, QC, QP, QQ, QR
    G1 = ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3)
    G2 = ((P[0] + Q[0] + R[0]) / 3, (P[1] + Q[1] + R[1]) / 3)
    triang(c, t, t1, A, B, Cc, nomes="ABC")
    E.foco(c, t, t1 + 0.5, 0.4, lambda a: txt_lado(c, A, B, "9 cm", G1, 46, COR, a))
    canto(c, t, t1 + 0.7, A, B, Cc, "50°", E.COR, 60, size=44)
    canto(c, t, t1 + 1.0, B, A, Cc, "30°", TINTA2, 80, size=44, rl=150)
    E.foco(c, t, (tq or t1) + 1.2, 0.4, lambda a: txt_lado(c, B, Cc, "7 cm", G1, 46, COR, a))
    triang(c, t, t2, P, Q, R, nomes="PQR")
    E.foco(c, t, t2 + 0.5, 0.4, lambda a: txt_lado(c, P, Q, "9 cm", G2, 46, COR, a))
    canto(c, t, t2 + 0.7, P, Q, R, "50°", E.COR, 60, size=44)
    canto(c, t, t2 + 1.0, Q, P, R, "30°", TINTA2, 80, size=44, rl=150)
    return G1, G2


def b_questao(c, t, C, b):
    a20, b20, a21, b21, c21 = C["s20.a"], C["s20.b"], C["s21.a"], C["s21.b"], C["s21.c"]
    X = 1490
    fig_q(c, t, a20, a21, tq=b20 - 1.2)
    G2 = ((QP[0] + QQ[0] + QR[0]) / 3, (QP[1] + QQ[1] + QR[1]) / 3)
    if t >= c21:
        E.foco(c, t, c21, 0.4, lambda a: txt_lado(c, QQ, QR, "?", G2, 56, ERRADO, a))
        canto(c, t, c21 + 0.3, QR, QP, QQ, "?", AMBAR, 60, size=52)

    def txt():
        E.frase(c, t, C["s20"], ps("hora de testar", "i", 72, COR), X, 200, "center", 0.12)
    E.saida(c, t, C["s22.a"] - 0.1, txt)
    E.frase(c, t, b21, ps("qual", "i", 64) + [("caso?", "g", 70, COR)], X, 900, "center", 0.12)
    E.frase(c, t, c21, [("QR = ?", "g", 64)] + ps("e", "i", 60) + [("R = ?", "g", 64)], X, 1010, "center", 0.12)
    E.relogio(c, t, C["s22.a"], cy=430, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a23, b23, a24, b24, c24 = C["s23.a"], C["s23.b"], C["s24.a"], C["s24.b"], C["s24.c"]
    X = 1450
    t0 = C["s23"]
    fig_q(c, t, t0 - 1.5, t0 - 1.5)
    G2 = ((QP[0] + QQ[0] + QR[0]) / 3, (QP[1] + QQ[1] + QR[1]) / 3)
    E.foco(c, t, t0, 0.4, lambda a: txt_lado(c, QQ, QR, "?" if t < b24 else "7 cm", G2, 50 if t >= b24 else 56, ERRADO if t < b24 else CERTO, a))
    canto(c, t, t0, QR, QP, QQ, (lambda tt: "?" if tt < c24 + 0.5 else "100°"), AMBAR, 60, size=48)
    k = ep(t, a23, 0.4) * (1 - ep(t, a24, 0.4))
    grosso(c, QA, QB, E.COR, k)
    grosso(c, QP, QQ, E.COR, k)
    if t >= a24:  # Q corresponde a B; QR a BC
        k = ep(t, a24, 0.4)
        for V in (QB, QQ):
            c.drawCircle(*V, 24, M.paint(TINTA2, 0.45 * k))
    if t >= b24:
        k = ep(t, b24, 0.4)
        grosso(c, QB, QC, CERTO, k, 10)
        grosso(c, QQ, QR, CERTO, k, 10)

    def um():
        E.frase(c, t, a23, ps("9 entre", "i", 64) + [("50°", "g", 66, COR)] + ps("e", "i", 64) + [("30°", "g", 66, TINTA2)], X, 260, "center", 0.12)
        E.foco(c, t, b23, 0.5, lambda a: E.pilula(c, "ALA", X, 430, 100, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, b23 + 0.6, ps("ângulo, lado, ângulo", "i", 56), X, 570, "center", 0.1)
    E.saida(c, t, C["s24"] - 0.1, um)
    if t >= C["s24"]:
        E.frase(c, t, a24, [("Q ↔ B", "g", 70, TINTA2)] + ps("ambos com", "i", 56) + [("30°", "g", 70, TINTA2)], X, 240, "center", 0.12)
        fcen(c, t, b24, "QR = BC = 7 cm", X, 390, 72, CERTO)
        fcen(c, t, lerp(b24, c24, 0.55), "50 + 30 = 80", X, 540, 72)
        fcen(c, t, c24, "180 − 80 = 100", X, 680, 72)
        bola_txt(c, t, c24 + 0.8, "R = 100°", X, 870, 140, 64, AMBAR)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s25"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s25.a", "3 medidas no lugar certo"), ("s25.b", "o resto, copie do outro"))
        for i, (k, s) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 380, y - 30, 56, a=a), centro(c, str(i + 1), 380, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 80)], 480, y)
        E.frase(c, t, C["s25.a"] + 0.8, ps("= triângulos congruentes", "i", 58, COR), 480, 530)
    E.saida(c, t, C["s26"] - 0.1, resumo)
    if t < C["s26"]:
        return
    E.frase(c, t, C["s26.a"] - 1.0, ps("próxima aula", "i", 84), XE, 280)
    E.frase(c, t, C["s26.a"], ps("4 linhas", "i", 96) + [("especiais", "g", 110, COR)], XE, 420, passo=0.14)
    E.frase(c, t, C["s26.b"], [("altura, mediana,", "g", 80)], XE, 570, passo=0.14)
    E.frase(c, t, C["s26.b"] + 0.6, [("bissetriz e mediatriz", "g", 80)], XE, 680, passo=0.14)
    E.foco(c, t, C["s26.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s26.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s26.c"] + 0.2, 0.4))
    E.frase(c, t, C["s26.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, congruente=b_congruente, lll=b_lll, lal=b_lal, ala=b_ala, laao=b_laao,
              gravata=b_gravata, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
