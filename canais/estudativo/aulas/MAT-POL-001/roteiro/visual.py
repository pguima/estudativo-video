"""Visual — Estudativo · MAT-POL-001: quadriláteros (paralelogramo, retângulo, losango e trapézio). Primeira aula de Polígonos e Círculo.
Linguagem da geometria plana (MAT-ANG-001 a 007): lados em tinta; o ângulo da vez com arco e cunha clara na cor da matéria;
ângulos iguais com a mesma cor (1ª família em COR, 2ª em TINTA2); lados iguais com o mesmo número de tracinhos (E.marcas_iguais);
lados paralelos com as setinhas (uma seta = um par, duas setas = o outro par); medidas na grotesca; resposta na esfera;
vermelho é erro, verde é certo. "Os ângulos do Z são iguais": a cunha de A voa pela diagonal (voa(), da MAT-ANG-002) e assenta em C.
"Os triângulos são cópias": a cópia de ABC gira meia volta em torno do meio da diagonal e assenta em CDA.
Peças locais: quad() (E.poligono com as setinhas), setas(), lin(), vang() (ângulo interno do vértice i), cunha_m() e voa().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polígonos e Círculo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POL-001_quadrilateros.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("quadri", "paralelo", "especiais", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 180 - 70 == 110 and 70 + 110 == 180
assert 3 * 35 - 10 == 95 and 35 + 50 == 85 and 95 + 85 == 180
assert 4 * 35 + 40 == 180 and 180 - 40 == 140 and 140 // 4 == 35
assert 3 * 30 - 10 == 30 + 50 == 80 and 80 + 80 != 180


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


def pt(V, L, g):
    return V[0] + L * math.cos(math.radians(g)), V[1] - L * math.sin(math.radians(g))


def dirg(V, P):
    return math.degrees(math.atan2(-(P[1] - V[1]), P[0] - V[0]))


def lin(c, t, t0, P, Q, cor=TINTA, larg=6, d=0.6, a=1.0, dash=None):
    if t >= t0 and a > 0:
        M.line(c, *P, *Q, cor, a, larg, dash=dash, progress=ease_io(prog(t, t0, d)))


def setas(c, P, Q, n, a=1.0, cor=TINTA, onde=0.5):
    """n setinhas de paralela no lado PQ, apontando de P para Q"""
    if a <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = -uy, ux
    mx, my = lerp(P[0], Q[0], onde), lerp(P[1], Q[1], onde)
    for k in range(n):
        off = (k - (n - 1) / 2) * 20
        tx, ty = mx + ux * (off + 8), my + uy * (off + 8)
        for s in (-1, 1):
            M.line(c, tx - ux * 20 + nx * 16 * s, ty - uy * 20 + ny * 16 * s, tx, ty, cor, a, 5)


def quad(c, t, t0, pts, nomes="ABCD", par=(0, 0), d=0.9, tinta=TINTA, escuro=False, preenche=0.06, ts=None, a=1.0):
    """quadrilátero pelos pontos (A, B, C, D em volta). par = (setas em AB/CD, setas em BC/DA); ts = instante das setas"""
    if a <= 0 or t < t0:
        return pts
    if a < 1:
        c.saveLayerAlpha(None, int(255 * a))
    E.poligono(c, t, t0, pts, list(nomes) if nomes else None, preenche=preenche, d=d, escuro=escuro, size=56)
    q = ep(t, ts if ts is not None else t0 + d, 0.4)
    cor = BR if escuro else tinta
    if par[0]:
        setas(c, pts[0], pts[1], par[0], q, cor); setas(c, pts[3], pts[2], par[0], q, cor)
    if par[1]:
        setas(c, pts[0], pts[3], par[1], q, cor); setas(c, pts[1], pts[2], par[1], q, cor)
    if a < 1:
        c.restore()
    return pts


def vang(c, t, t0, P, i, rot=None, cor=None, r=70, size=54):
    """ângulo interno do vértice i do polígono P"""
    E.angulo(c, t, t0, P[i], P[i - 1], P[(i + 1) % len(P)], rot, r=r, cor=cor, size=size)


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


def tri_cheio(c, pts, cor, a=1.0, alfa=0.2, borda=0):
    if a <= 0:
        return
    path = skia.Path(); path.addPoly([tuple(p) for p in pts], True)
    c.drawPath(path, M.paint(cor, alfa * a))
    if borda:
        p = M.paint(cor, a, stroke=borda); p.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(path, p)


def losango(cx, cy, p, q):
    """losango de diagonais 2p (deitada) e 2q (em pé): A à esquerda, B embaixo, C à direita, D em cima"""
    return [(cx - p, cy), (cx, cy + q), (cx + p, cy), (cx, cy - q)]


def para_pts(x, y, base, lado, ang):
    """paralelogramo com A em (x, y), AB deitado para a direita e ângulo `ang` em A"""
    A = (x, y)
    B = (x + base, y)
    D = pt(A, lado, ang)
    return [A, B, (D[0] + base, D[1]), D]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    cx, cy, L = 520, 560, 400

    def um():
        g = 45 * ease_io(prog(t, kc, 1.2))
        pts = [pt((cx, cy), L / math.sqrt(2), 225 + g + 90 * k) for k in range(4)]
        E.poligono(c, t, ka, pts, None, iguais=[1, 1, 1, 1], retos=(0, 1, 2, 3), preenche=0.08, d=0.9, r_ang=56)
        X = 1000
        E.frase(c, t, ka + 0.2, ps("um", "i", 90) + [("quadrado", "g", 92, COR)], X, 300, "left", 0.14)
        E.frase(c, t, ka + 0.9, ps("é um", "i", 90) + [("retângulo?", "g", 92)], X, 420, "left", 0.14)
        mas = lerp(kb, kc, 0.55)
        E.frase(c, t, kb, ps("muita gente:", "i", 70, TINTA2) + [("não", "g", 76, ERRADO)], X, 580, "left", 0.14)
        if t >= mas:
            xn = X + E.larg("muita gente: ", "i", 70) + 20
            E.risco(c, xn - 10, 560, xn + E.larg("não", "g", 76) + 10, 548, t, mas, largura=10)
        E.frase(c, t, mas + 0.2, [("mas", "i", 84, CERTO), ("é!", "g", 88, CERTO)], X, 690, "left", 0.14)
        E.frase(c, t, kc + 0.2, ps("e também é", "i", 76) + [("losango", "g", 84, COR)], X, 830, "left", 0.14)
        E.foco(c, t, lerp(kc, C["s01.end"], 0.55), 0.5, lambda a: E.pilula(c, "o que cada nome exige", cx, 960, 50, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1520, 560, 240 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 280, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("lados,", "g", 96, COR), ("ângulos", "g", 96, COR)], XE, 420, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), ps("e", "i", 90) + [("diagonais", "g", 96, COR)], XE, 540, passo=0.14)
        E.frase(c, t, tb, ps("os ângulos do", "i", 76), XE, 700, passo=0.14)
        E.frase(c, t, tb + 0.6, [("paralelogramo", "g", 90)], XE, 810, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1520, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1520, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "paralelas e transversal:", "agudo = agudo", "agudo + obtuso = 180°", 150),
             ("s03.c", "triângulos congruentes:", "cópias um do outro", "caso ALA", 500))
    for k, l1, l2, l3, y in itens:
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 300, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 80)
        E.frase(c, t, C[k] + 0.6, [(l2, "g", 60, COR)], x + 44, y + 170)
        E.frase(c, t, lerp(C[k], C["s03.c"] if k == "s03.b" else C["s03.end"] - 3.0, 0.55), [(l3, "g", 60, COR)], x + 44, y + 260)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(150 + 270, 500 + 270, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 930, "left", 0.12)


# ---------------- quadrilátero ----------------
def b_quadri(c, t, C, b):
    a4, b4, c4, d4, e4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"], C["s04.e"]
    P = [(260, 820), (900, 870), (1000, 340), (420, 300)]

    def fig():
        if t >= a4:
            path = skia.Path(); path.addPoly(P, True)
            c.drawPath(path, M.paint(E.COR, 0.06 * ep(t, a4 + 0.5, 0.5)))
            E._contorno(c, P, ease_io(prog(t, a4, 1.0)), TINTA, 6)
        for i, (s, V) in enumerate(zip("ABCD", P)):
            k = ease_back(prog(t, b4 + 0.25 * i, 0.35))
            if k > 0:
                c.drawCircle(*V, 12 * k, M.paint(TINTA))
            G = (sum(p[0] for p in P) / 4, sum(p[1] for p in P) / 4)
            E.foco(c, t, b4 + 0.25 * i, 0.4, lambda a, s=s, V=V: E._cola(c, s, V[0], V[1], V[0] - G[0], V[1] - G[1], 16, 64, "g", TINTA, a))
        # A e C não são vizinhos
        if c4 <= t < d4 + 0.6:
            for V in (P[0], P[2]):
                pulsa = 1 + 0.5 * math.sin(math.pi * M.clamp(prog(t, c4, 0.8)))
                c.drawCircle(*V, 20 * pulsa, M.paint(E.COR, 0.9))
        lin(c, t, d4, P[0], P[2], E.COR, 7, 0.7)
        lin(c, t, e4 + 0.2, P[1], P[3], E.COR, 7, 0.7)
    E.saida(c, t, C["s05"] - 0.1, fig)

    def txt():
        X = 1500
        E.frase(c, t, a4 + 0.3, [("4", "g", 130, COR)] + ps("lados", "i", 100), X, 300, "center", 0.14)
        E.frase(c, t, b4 + 0.4, ps("cantos =", "i", 64) + [("vértices", "g", 66)], X, 430, "center", 0.12)
        E.frase(c, t, c4, ps("não vizinhos:", "i", 60, TINTA2) + [("A e C", "g", 62, COR)], X, 560, "center", 0.12)
        E.frase(c, t, d4 + 0.2, [("diagonal", "g", 84, COR)], X, 690, "center")
        E.frase(c, t, e4, [("2", "g", 96, COR)] + ps("diagonais:", "i", 70), X, 840, "center", 0.12)
        E.frase(c, t, e4 + 0.8, [("AC", "g", 70), ("e", "i", 70), ("BD", "g", 70)], X, 940, "center", 0.12)
    E.saida(c, t, C["s05"] - 0.1, txt)

    if t >= C["s05"]:
        a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
        E.frase(c, t, C["s05"] + 0.2, ps("quantos pares de lados", "i", 72) + [("paralelos?", "g", 76, COR)], W / 2, 170, "center", 0.12)
        T = [(140, 720), (860, 720), (700, 380), (330, 380)]
        quad(c, t, b5, T, None, (1, 0), ts=b5 + 0.6)
        E.frase(c, t, b5 + 0.4, [("trapézio", "g", 84, COR)], 500, 910, "center")
        E.frase(c, t, b5 + 0.8, ps("só 1 par", "i", 56, TINTA2), 500, 990, "center", 0.12)
        E.foco(c, t, c5, 0.4, lambda a: (centro(c, "base", 515, 355, 52, "b", COR, a), centro(c, "base", 500, 790, 52, "b", COR, a)))
        Pg = [(1060, 720), (1640, 720), (1800, 380), (1220, 380)]
        quad(c, t, d5, Pg, None, (1, 2), d=0.8, ts=d5 + 0.5)
        E.frase(c, t, d5 + 0.4, [("paralelogramo", "g", 84, COR)], 1430, 910, "center")
        E.frase(c, t, d5 + 0.8, ps("2 pares", "i", 56, TINTA2), 1430, 990, "center", 0.12)


# ---------------- paralelogramo: por que valem as regras ----------------
PA, PB, PC, PD = (200, 840), (840, 840), (1100, 380), (460, 380)
PP = [PA, PB, PC, PD]
POo = meio(PA, PC)


def b_paralelo(c, t, C, b):
    a6, b6 = C["s06.a"], C["s06.b"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    X = 1250
    # cópia de ABC que gira meia volta e assenta em CDA
    if a7 <= t:
        tri_cheio(c, [PA, PB, PC], E.COR, ep(t, a7, 0.4) * (1 - ep(t, a8, 0.5)), 0.14)
        g = 180 * ease_io(prog(t, a7 + 0.6, 1.6))
        if t < a8:
            rot = [(POo[0] + (P[0] - POo[0]) * math.cos(math.radians(g)) - (P[1] - POo[1]) * math.sin(math.radians(g)),
                    POo[1] + (P[0] - POo[0]) * math.sin(math.radians(g)) + (P[1] - POo[1]) * math.cos(math.radians(g))) for P in (PA, PB, PC)]
            tri_cheio(c, rot, E.COR, ep(t, a7 + 0.4, 0.3) * (1 - ep(t, b7, 0.5)), 0.22, 5)
            tri_cheio(c, [PC, PD, PA], TINTA2, ep(t, a7 + 2.2, 0.4) * (1 - ep(t, a8, 0.5)), 0.12)
    # o Z: D → C → A → B
    if b6 <= t < a7 + 0.5:
        z = 1 - ep(t, a7, 0.4)
        c.saveLayerAlpha(None, int(255 * z))
        E._contorno(c, [PD, PC, PA, PB], ease_io(prog(t, b6, 0.9)), E.mix(E.COR, BR, 0.55), 16, fecha=False)
        c.restore()
    quad(c, t, C["s06"], PP, "ABCD", (1, 2), ts=C["s06"] + 0.8, preenche=0.0)
    # a diagonal: transversal
    lin(c, t, a6, PA, PC, TINTA2 if t < c7 else E.COR, 6 if t < c7 else 10, 0.7, 1 - ep(t, d8 - 0.3, 0.3))
    gac = dirg(PA, PC)
    angs = lambda: (E.angulo(c, t, b6, PA, PB, PC, None, r=130), E.angulo(c, t, b6 + 2.2, PC, PD, PA, None, r=130),
                    E.angulo(c, t, lerp(b6, C["s06.end"], 0.55), PA, PC, PD, None, r=95, cor=TINTA2),
                    E.angulo(c, t, lerp(b6, C["s06.end"], 0.55), PC, PA, PB, None, r=95, cor=TINTA2))
    if t >= b6:
        E.saida(c, t, a8, angs)
    voa(c, t, b6 + 0.9, 1.2, PA, 0, gac, 130, V1=PC, giro=180)

    def txt6():
        E.frase(c, t, a6, [("diagonal AC", "g", 64, TINTA2)], X, 300, "left")
        E.frase(c, t, a6 + 0.6, ps("= transversal", "i", 64), X, 390, "left", 0.12)
        E.frase(c, t, b6, ps("alternos internos", "i", 60), X, 560, "left", 0.12)
        E.frase(c, t, b6 + 0.5, [("iguais", "g", 76, COR)] + ps("(o Z)", "i", 64), X, 660, "left", 0.12)
    E.saida(c, t, C["s07"] - 0.1, txt6)

    def txt7():
        E.frase(c, t, a7, [("ABC", "g", 70, COR), ("e", "i", 66), ("CDA", "g", 70, TINTA2)], X, 280, "left", 0.14)
        E.frase(c, t, a7 + 0.7, [("congruentes", "g", 66)], X, 370, "left")
        E.foco(c, t, b7, 0.5, lambda a: E.pilula(c, "ângulo, lado, ângulo", X + 290, 520, 48, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, c7, ps("lado", "i", 70) + [("comum:", "g", 70, COR)], X, 690, "left", 0.12)
        E.frase(c, t, c7 + 0.6, [("AC", "g", 90, COR)], X, 800, "left")
    if t >= C["s07"]:
        E.saida(c, t, C["s08"] - 0.1, txt7)

    if t >= C["s08"]:
        # lados opostos
        for (P, Q), n in (((PA, PB), 1), ((PD, PC), 1), ((PB, PC), 2), ((PA, PD), 2)):
            E.marcas_iguais(c, P, Q, n, TINTA, ep(t, a8 + 0.2, 0.4) * (1 - ep(t, d8 - 0.2, 0.4)))
        # ângulos internos: A e C em COR, B e D em TINTA2
        E.saida(c, t, d8 - 0.2, lambda: (vang(c, t, b8, PP, 0, None, None, 80), vang(c, t, b8 + 0.3, PP, 2, None, None, 80),
                                          vang(c, t, b8 + 0.7, PP, 1, None, TINTA2, 70), vang(c, t, b8 + 1.0, PP, 3, None, TINTA2, 70)))
        if c8 <= t < d8:
            pulsa = 1 + 0.15 * math.sin(math.pi * M.clamp(prog(t, c8, 0.8)))
            cunha_m(c, PA, 0, dirg(PA, PD), 80 * pulsa, E.COR, ep(t, c8, 0.4) * (1 - ep(t, d8 - 0.3, 0.3)), 0.5)
            cunha_m(c, PB, dirg(PB, PC), 180, 70 * pulsa, TINTA2, ep(t, c8, 0.4) * (1 - ep(t, d8 - 0.3, 0.3)), 0.5)
        # diagonais que se cortam ao meio
        if t >= d8:
            lin(c, t, d8, PA, PC, E.COR, 7, 0.6)
            lin(c, t, d8 + 0.3, PB, PD, TINTA2, 7, 0.6)
            q = ep(t, d8 + 1.0, 0.4)
            E.marcas_iguais(c, PA, POo, 1, E.COR, q); E.marcas_iguais(c, POo, PC, 1, E.COR, q)
            E.marcas_iguais(c, PB, POo, 2, TINTA2, q); E.marcas_iguais(c, POo, PD, 2, TINTA2, q)
            k = ease_back(prog(t, d8 + 0.8, 0.4))
            if k > 0:
                c.drawCircle(*POo, 14 * k, M.paint(TINTA))
        itens = ((a8, "lados opostos", "iguais"), (b8, "ângulos opostos", "iguais"), (c8, "vizinhos somam", "180°"), (d8, "diagonais", "cortam ao meio"))
        for i, (ti, l1, l2) in enumerate(itens):
            y = 250 + i * 190
            E.foco(c, t, ti, 0.4, lambda a, i=i, y=y: (E.bola(c, X + 30, y - 22, 36, a=a), centro(c, str(i + 1), X + 30, y - 5, 44, "g", BR, a)))
            E.frase(c, t, ti + 0.1, [(l1, "i", 54)], X + 90, y - 10, "left")
            E.frase(c, t, ti + 0.4, [(l2, "g", 58, COR)], X + 90, y + 62, "left")


# ---------------- o exemplo do 70° ----------------
SP = para_pts(240, 800, 640, 440, 70)


def b_setenta(c, t, C, b):
    a9, b9, c9, d9, a10 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s10.a"]
    X = 1450
    quad(c, t, C["s09"], SP, "ABCD", (1, 2), ts=C["s09"] + 0.8)
    vang(c, t, a9, SP, 0, "70°", None, 90, 60)
    vang(c, t, b9, SP, 2, "70°", None, 90, 60)
    vang(c, t, c9, SP, 1, "110°", TINTA2, 70, 60)
    vang(c, t, d9, SP, 3, "110°", TINTA2, 70, 60)

    def contas():
        E.frase(c, t, a9, ps("em A:", "i", 72) + [("70°", "g", 80, COR)], X, 260, "center", 0.12)
        E.frase(c, t, b9, ps("C, de frente:", "i", 66) + [("70°", "g", 74, COR)], X, 400, "center", 0.12)
        E.frase(c, t, c9, ps("B, vizinho de A:", "i", 60, TINTA2), X, 540, "center", 0.12)
        fcen(c, t, c9 + 0.8, "180 − 70 = 110°", X, 650, 78, TINTA2)
        E.frase(c, t, d9, ps("D, de frente:", "i", 66) + [("110°", "g", 74, TINTA2)], X, 800, "center", 0.12)
    E.saida(c, t, C["s10"] - 0.1, contas)
    if t >= C["s10"]:
        E.frase(c, t, C["s10"], ps("conferindo", "i", 84, COR), X, 300, "center")
        fcen(c, t, a10, "70 + 110 = 180", X, 520, 96)
        E.frase(c, t, a10 + 1.2, ps("em cada par de vizinhos", "i", 54, TINTA2), X, 620, "center", 0.1)
        E.foco(c, t, C["s10.end"] - 1.6, 0.5, lambda a: E.selo(c, X, 800, 90 * ease_back(prog(t, C["s10.end"] - 1.6, 0.5)), True, a))
        if t >= a10:
            pulsa = 1 + 0.12 * math.sin(math.pi * M.clamp(prog(t, a10, 0.8)))
            cunha_m(c, SP[0], 0, 70, 90 * pulsa, E.COR, ep(t, a10, 0.4), 0.45)
            cunha_m(c, SP[1], 70, 180, 70 * pulsa, TINTA2, ep(t, a10, 0.4), 0.45)


# ---------------- os especiais ----------------
def diag_par(c, t, t0, P, cor1, cor2=None, larg=6):
    lin(c, t, t0, P[0], P[2], cor1, larg, 0.6)
    lin(c, t, t0 + 0.3, P[1], P[3], cor2 or cor1, larg, 0.6)


def b_especiais(c, t, C, b):
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12 = C["s12.a"], C["s12.b"]
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    R = [(150, 590), (590, 590), (590, 330), (150, 330)]
    Lz = losango(960, 460, 230, 140)
    Q = [(1420, 600), (1700, 600), (1700, 320), (1420, 320)]

    def tudo():
        E.saida(c, t, a11, lambda: E.frase(c, t, C["s11"], ps("os paralelogramos", "i", 80) + [("especiais", "g", 84, COR)], W / 2, 170, "center", 0.12))
        E.frase(c, t, a11, ps("herdam tudo e ganham", "i", 76) + [("1 regra", "g", 84, COR)], W / 2, 170, "center", 0.12)
        # retângulo
        E.poligono(c, t, b11, R, None, retos=(0, 1, 2, 3), preenche=0.06, d=0.8, r_ang=46)
        E.frase(c, t, b11 + 0.3, [("retângulo", "g", 70, COR)], 370, 730, "center")
        E.frase(c, t, b11 + 0.7, ps("4 ângulos retos", "i", 44, TINTA2), 370, 800, "center", 0.1)
        diag_par(c, t, c11, R, E.COR, larg=7)
        E.foco(c, t, c11 + 0.6, 0.4, lambda a: E.pilula(c, "diagonais iguais", 370, 900, 42, "g", a=a, cor=E.SOBRE))
        # losango
        E.poligono(c, t, a12, Lz, None, iguais=[1, 1, 1, 1], preenche=0.06, d=0.8)
        E.frase(c, t, a12 + 0.3, [("losango", "g", 70, COR)], 960, 730, "center")
        E.frase(c, t, a12 + 0.7, ps("4 lados iguais", "i", 44, TINTA2), 960, 800, "center", 0.1)
        diag_par(c, t, b12, Lz, E.COR)
        E.angulo(c, t, b12 + 0.7, (960, 460), (1060, 460), (960, 360), None, r=56)
        E.foco(c, t, b12 + 0.6, 0.4, lambda a: E.pilula(c, "diagonais perpendiculares", 960, 900, 42, "g", a=a, cor=E.SOBRE))
        # quadrado
        E.poligono(c, t, a13, Q, None, iguais=[1, 1, 1, 1], retos=(0, 1, 2, 3), preenche=0.06, d=0.8, r_ang=46)
        E.frase(c, t, a13 + 0.3, [("quadrado", "g", 70, COR)], 1560, 730, "center")
        E.frase(c, t, a13 + 0.7, ps("lados iguais e retos", "i", 44, TINTA2), 1560, 800, "center", 0.1)
        E.foco(c, t, b13, 0.4, lambda a: E.pilula(c, "retângulo + losango", 1560, 220, 40, "b", fundo=TINTA, a=a))
        diag_par(c, t, c13, Q, E.COR, larg=7)
        E.angulo(c, t, c13 + 0.7, (1560, 460), (1660, 360), (1460, 360), None, r=50)
        E.foco(c, t, c13 + 0.6, 0.4, lambda a: E.pilula(c, "ganha tudo", 1560, 900, 42, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, d13, tudo)
    if t >= d13:
        E.frase(c, t, d13, ps("todo", "i", 92) + [("quadrado", "g", 96, COR)] + ps("é retângulo", "i", 92), W / 2 - 60, 420, "center", 0.12)
        E.foco(c, t, d13 + 1.0, 0.5, lambda a: E.selo(c, 1690, 390, 60 * ease_back(prog(t, d13 + 1.0, 0.5)), True, a))
        E.frase(c, t, lerp(d13, C["s13.end"], 0.6), ps("nem todo", "i", 80, TINTA2) + [("retângulo", "g", 84)] + ps("é quadrado", "i", 80, TINTA2),
                W / 2, 640, "center", 0.12)
        k = lerp(d13, C["s13.end"], 0.6) + 0.8
        E.foco(c, t, k, 0.5, lambda a: (E.poligono(c, t, k, [(760, 960), (1160, 960), (1160, 760), (760, 760)], None, retos=(0, 1, 2, 3), d=0.6, r_ang=40)))


# ---------------- trapézio ----------------
def b_trapezio(c, t, C, b):
    t0, a14, b14, c14, d14 = C["s14"], C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    T1 = [(140, 680), (860, 680), (700, 360), (300, 360)]
    T2 = [(1080, 680), (1760, 680), (1480, 360), (1080, 360)]
    E.frase(c, t, t0, [("trapézio:", "g", 76, COR)] + ps("1 par de paralelos", "i", 72), W / 2, 170, "center", 0.12)
    quad(c, t, t0 + 0.4, T1, None, (1, 0), ts=t0 + 1.2)
    nao = lerp(t0, a14, 0.3)
    E.saida(c, t, a14 - 0.2, lambda: E.frase(c, t, nao, [("não", "g", 72, ERRADO)] + ps("segue as regras", "i", 66) +
                                              ps("do paralelogramo", "i", 66), W / 2 + 470, 470, "center", 0.12))
    q = ep(t, lerp(t0, a14, 0.75), 0.4)
    E.marcas_iguais(c, T1[1], T1[2], 1, TINTA, q); E.marcas_iguais(c, T1[3], T1[0], 1, TINTA, q)
    E.frase(c, t, a14, [("isósceles", "g", 72, COR)], 500, 790, "center")
    E.angulo(c, t, b14, T1[0], T1[3], T1[1], None, r=80)
    E.angulo(c, t, b14 + 0.2, T1[1], T1[0], T1[2], None, r=80)
    E.angulo(c, t, b14 + 0.5, T1[2], T1[1], T1[3], None, r=60, cor=TINTA2)
    E.angulo(c, t, b14 + 0.7, T1[3], T1[2], T1[0], None, r=60, cor=TINTA2)
    E.frase(c, t, b14 + 0.3, ps("ângulos da base", "i", 50) + [("iguais", "g", 54, COR)], 500, 880, "center", 0.1)
    lin(c, t, c14, T1[0], T1[2], E.COR, 6, 0.6)
    lin(c, t, c14 + 0.3, T1[1], T1[3], E.COR, 6, 0.6)
    E.frase(c, t, c14 + 0.3, ps("diagonais", "i", 50) + [("iguais", "g", 54, COR)], 500, 960, "center", 0.1)
    if t >= d14 - 0.2:
        quad(c, t, d14 - 0.2, T2, None, (1, 0), ts=d14 + 0.5)
        E.angulo(c, t, d14 + 0.4, T2[0], T2[3], T2[1], None, r=60)
        E.angulo(c, t, d14 + 0.6, T2[3], T2[2], T2[0], None, r=60)
        E.frase(c, t, d14 + 0.3, [("retângulo", "g", 72, COR)], 1420, 790, "center")
        E.frase(c, t, d14 + 0.7, ps("um lado reto com as bases", "i", 46, TINTA2), 1420, 880, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a15, b15, c15, d15, e15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]
    cx, cy, L = 560, 560, 300
    E.frase(c, t, C["s15"], [("cuidado", "g", 92, ERRADO)] + ps("com este erro", "i", 86), W / 2, 150, "center", 0.14)
    E.saida(c, t, d15, lambda: E.frase(c, t, a15, ps("todo losango tem", "i", 64) + [("diagonais iguais?", "g", 64, ERRADO)], W / 2, 260, "center", 0.12))
    # achatar: o lado fica igual e o ângulo abre
    g = lerp(32, 15, ease_io(prog(t, b15, 1.4)))
    q = L * math.sin(math.radians(g))
    p = L * math.cos(math.radians(g))
    Lz = losango(cx, cy, p, q)
    E.poligono(c, t, a15, Lz, None, iguais=[1, 1, 1, 1], preenche=0.06, d=0.8)
    lin(c, t, a15 + 0.8, Lz[0], Lz[2], E.COR, 7, 0.5)
    lin(c, t, a15 + 1.0, Lz[1], Lz[3], TINTA2, 7, 0.5)
    E.foco(c, t, c15, 0.4, lambda a: centro(c, "comprida", cx, cy - q - 40, 54, "g", COR, a))
    E.foco(c, t, c15 + 0.6, 0.4, lambda a: centro(c, "curta", cx + 130, cy + q + 80, 54, "g", TINTA2, a))
    E.frase(c, t, b15, ps("achatou:", "i", 56, TINTA2), cx, 880, "center")
    E.frase(c, t, c15 + 1.0, [("diagonais", "i", 60), ("diferentes", "g", 60, ERRADO)], cx, 970, "center", 0.12)
    # o retângulo é que tem diagonais iguais
    R = [(1160, 660), (1720, 660), (1720, 360), (1160, 360)]
    if t >= d15:
        E.poligono(c, t, d15, R, None, retos=(0, 1, 2, 3), preenche=0.06, d=0.7, r_ang=44)
        lin(c, t, d15 + 0.6, R[0], R[2], CERTO, 7, 0.5)
        lin(c, t, d15 + 0.8, R[1], R[3], CERTO, 7, 0.5)
        E.frase(c, t, d15 + 0.3, ps("diagonais iguais:", "i", 56) + [("retângulo", "g", 60, CERTO)], 1440, 780, "center", 0.1)
    E.angulo(c, t, e15, (cx, cy), (cx + 60, cy), (cx, cy - 60), None, r=44, cor=CERTO)
    E.frase(c, t, e15 + 0.2, ps("losango:", "i", 56) + [("perpendiculares", "g", 60, CERTO)], 1440, 900, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
AP = para_pts(200, 760, 620, 400, 62)


def b_atalho(c, t, C, b):
    palco(c, t)
    a16, b16, c16, d16, e16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"]
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    X = 1400

    def um():
        quad(c, t, C["s16"], AP, None, (1, 2), escuro=True, preenche=0.0, ts=C["s16"] + 0.8)
        E.angulo(c, t, b16, AP[0], AP[1], AP[3], "α", r=86, cor=CLARO, size=64)
        E.angulo(c, t, c16, AP[1], AP[2], AP[0], "180° − α", r=70, cor=BR, size=54)
        E.angulo(c, t, d16, AP[2], AP[3], AP[1], "α", r=86, cor=CLARO, size=64)
        E.angulo(c, t, e16, AP[3], AP[0], AP[2], "180° − α", r=70, cor=BR, size=54)
        if t >= a17:
            for P, Q in ((AP[0], AP[1]), (AP[3], AP[2])):
                ux, uy = E._uni(*P, *Q)
                lin(c, t, a17, (P[0] - ux * 140, P[1]), (Q[0] + ux * 110, Q[1]), CLARO, 4, 0.7, dash=E.TRACO)
            pulsa = 1 + 0.12 * math.sin(math.pi * M.clamp(prog(t, a17 + 0.4, 0.8)))
            M.line(c, *AP[0], *AP[3], CLARO, ep(t, a17, 0.4), 12)
            cunha_m(c, AP[0], 0, 62, 86 * pulsa, CLARO, ep(t, a17 + 0.4, 0.4), 0.45)
            cunha_m(c, AP[3], 180 + 62, 360, 70 * pulsa, BR, ep(t, a17 + 0.4, 0.4), 0.3)

        def txt():
            E.frase(c, t, a16, ps("só", "i", 80, CLARO) + [("2", "g", 110, BR)] + ps("medidas", "i", 80, CLARO), X, 260, "center", 0.12)
            E.frase(c, t, b16, [("α", "g", 80, CLARO)] + ps("= a que você conhece", "i", 54, BR), X, 400, "center", 0.12)
            E.frase(c, t, c16, [("180° − α", "g", 80, BR)], X, 530, "center")
            E.frase(c, t, d16, ps("de frente:", "i", 60, CLARO) + [("iguais", "g", 66, BR)], X, 690, "center", 0.12)
            E.frase(c, t, e16, ps("lado a lado:", "i", 60, CLARO) + [("somam 180°", "g", 66, BR)], X, 810, "center", 0.12)
        E.saida(c, t, a17 - 0.1, txt)
        if t >= a17:
            E.frase(c, t, a17, ps("cada lado é uma", "i", 66, CLARO), X, 400, "center", 0.12)
            E.frase(c, t, a17 + 0.6, [("transversal", "g", 84, BR)], X, 510, "center")
            E.frase(c, t, a17 + 1.0, ps("entre paralelas", "i", 66, CLARO), X, 610, "center", 0.12)
    E.saida(c, t, b17 - 0.1, um)

    if b17 <= t:
        G = [(260, 780), (880, 820), (790, 360), (380, 440)]

        def dois():
            quad(c, t, b17, G, None, escuro=True, preenche=0.0, d=0.7)
            E.foco(c, t, b17 + 0.8, 0.5, lambda a: E.selo(c, 560, 600, 80 * ease_back(prog(t, b17 + 0.8, 0.5)), False, a))
            E.frase(c, t, b17 + 0.2, ps("sem lados paralelos:", "i", 66, CLARO), X, 450, "center", 0.12)
            E.frase(c, t, b17 + 0.8, [("não vale", "g", 96, ERRADO)], X, 590, "center")
        E.saida(c, t, c17 - 0.1, dois)
    if c17 <= t:
        T = [(180, 780), (920, 780), (760, 380), (360, 380)]
        quad(c, t, c17, T, None, (1, 0), escuro=True, preenche=0.0, d=0.7, ts=c17 + 0.6)
        E.angulo(c, t, c17 + 0.9, T[0], T[1], T[3], None, r=80, cor=CLARO)
        E.angulo(c, t, c17 + 1.2, T[3], T[0], T[2], None, r=70, cor=CLARO)
        M.line(c, *T[0], *T[3], CLARO, ep(t, c17 + 0.8, 0.4), 12)
        E.frase(c, t, c17, ps("no trapézio:", "i", 66, CLARO), X, 380, "center", 0.12)
        E.frase(c, t, c17 + 0.6, ps("os do mesmo lado", "i", 64, BR), X, 500, "center", 0.12)
        E.frase(c, t, c17 + 1.2, [("somam 180°", "g", 90, CLARO)], X, 630, "center")


# ---------------- questão ----------------
QP = para_pts(220, 720, 640, 360, 95)


def b_questao(c, t, C, b):
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    quad(c, t, C["s18"] + 0.3, QP, "ABCD", (1, 2), ts=C["s18"] + 1.0)
    vang(c, t, a18, QP, 0, "3x − 10", None, 80, 58)
    vang(c, t, b18, QP, 1, "x + 50", TINTA2, 70, 58)
    E.frase(c, t, a18 + 0.3, ps("vizinhos", "i", 70, TINTA2), 540, 850, "center")
    E.frase(c, t, c18, ps("quanto mede", "i", 76) + [("cada ângulo?", "g", 80, COR)], 560, 970, "center", 0.12)
    E.relogio(c, t, C["s19.a"])


# ---------------- resposta ----------------
RP = para_pts(1180, 780, 580, 330, 95)


def b_resposta(c, t, C, b):
    a20, b20, c20, d20, e20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"], C["s20.e"]
    a21, b21, c21, d21 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
    X = 580
    quad(c, t, C["s20"], RP, "ABCD", (1, 2), d=0.7, ts=C["s20"] + 0.7)
    E.saida(c, t, a21, lambda: (vang(c, t, C["s20"] + 0.5, RP, 0, "3x − 10", None, 80, 50),
                                vang(c, t, C["s20"] + 0.7, RP, 1, "x + 50", TINTA2, 66, 50)))
    vang(c, t, a21 + 0.2, RP, 0, "95°", None, 80, 58)
    vang(c, t, b21 + 0.2, RP, 1, "85°", TINTA2, 66, 58)
    vang(c, t, c21, RP, 2, "95°", None, 80, 58)
    vang(c, t, lerp(c21, d21, 0.3), RP, 3, "85°", TINTA2, 66, 58)

    def conta():
        E.frase(c, t, a20, ps("vizinhos", "i", 66) + [("somam 180°", "g", 70, COR)], X, 200, "center", 0.12)
        fcen(c, t, b20, "3x − 10 + x + 50 = 180", X, 340, 70)
        fcen(c, t, c20, "4x + 40 = 180", X, 480, 80)
        E.foco(c, t, d20, 0.4, lambda a: E.pilula(c, "− 40", X + 300, 620, 44, "g", a=a, cor=E.SOBRE))
        fcen(c, t, d20 + 0.2, "4x = 140", X, 620, 80)
        E.foco(c, t, e20, 0.4, lambda a: E.pilula(c, "÷ 4", X + 260, 790, 44, "g", a=a, cor=E.SOBRE))
        bola_txt(c, t, e20 + 0.3, "x = 35", X, 790, 120, 62)
    E.saida(c, t, a21 - 0.1, conta)

    def ang2():
        fcen(c, t, a21, "3 × 35 − 10 = 95°", X, 260, 76, COR)
        fcen(c, t, b21, "35 + 50 = 85°", X, 400, 76, TINTA2)
        fcen(c, t, lerp(b21, c21, 0.45), "95 + 85 = 180", X, 540, 70)
        E.foco(c, t, lerp(b21, c21, 0.75), 0.5, lambda a: E.selo(c, X + 330, 520, 44 * ease_back(prog(t, lerp(b21, c21, 0.75), 0.5)), True, a))
        E.frase(c, t, c21, ps("de frente: cópias", "i", 60, TINTA2), X, 690, "center", 0.12)
        E.frase(c, t, c21 + 0.8, [("95°, 95°, 85°, 85°", "g", 70, CERTO)], X, 800, "center")
    E.saida(c, t, d21 - 0.1, ang2)
    if t >= d21:
        E.frase(c, t, d21, ps("igualar, como se fossem opostos:", "i", 54, TINTA2), X, 260, "center", 0.1)
        fcen(c, t, d21 + 0.6, "3x − 10 = x + 50", X, 400, 76, ERRADO)
        fcen(c, t, d21 + 1.6, "x = 30  →  80°", X, 540, 76, ERRADO)
        fcen(c, t, d21 + 2.6, "80 + 80 = 160", X, 700, 76, ERRADO)
        E.foco(c, t, d21 + 3.0, 0.5, lambda a: E.selo(c, X + 330, 680, 44 * ease_back(prog(t, d21 + 3.0, 0.5)), False, a))
        E.frase(c, t, d21 + 3.2, ps("não fecha 180°", "i", 60, ERRADO), X, 840, "center", 0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s22.a", "paralelogramo:", "opostos iguais, diagonais ao meio"), ("s22.b", "retângulo:", "diagonais iguais"),
                 ("s22.c", "losango:", "diagonais perpendiculares"), ("s22.d", "quadrado:", "tudo"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 350 + i * 175
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 50, a=a), centro(c, str(i + 1), 260, y - 5, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 64, COR), (l2, "i", 64)], 350, y, "left", 0.2)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23.a"] - 1.0, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s23.a"], [("Soma dos", "g", 130, COR)], XE, 440)
    E.frase(c, t, C["s23.a"] + 0.3, [("ângulos", "g", 130, COR)], XE, 570)
    E.frase(c, t, C["s23.b"], ps("e as", "i", 84) + [("diagonais", "g", 90)], XE, 700, passo=0.12)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, quadri=b_quadri, paralelo=b_paralelo, setenta=b_setenta, especiais=b_especiais,
              trapezio=b_trapezio, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
