"""Visual — Estudativo · MAT-ANG-005: classificar triângulos por lados e por ângulos.
Linguagem da geometria plana (MAT-ANG-001 a 004): lados em tinta; lados iguais com o mesmo número de tracinhos (E.marcas_iguais);
ângulos iguais com a mesma cor — no isósceles, os da base em COR e o topo em TINTA2; no equilátero, os três em COR.
Quando o que decide é um só ângulo (o maior), ele fica em COR e os outros em cinza claro. Medidas na grotesca; resposta na esfera.
Peças locais (iguais às da MAT-ANG-004): tri(), canto(), triang(); lados() põe os tracinhos. Todo instante vem de C[...]."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-005_classificar_triangulos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("lados", "isosceles", "angulos", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEUTRO = "#B9B9C0"
assert 180 - 40 == 140 and 140 // 2 == 70 and 180 // 3 == 60 and 180 - 40 - 40 == 100 and 45 + 45 + 90 == 180
assert 180 - 36 == 144 and 144 // 2 == 72 and 36 + 72 + 72 == 180


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


def operacao(c, t, t0, op, x, y, escuro=False):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, op, x, y - 30, 54, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, t0 + 0.3, ps("nos dois lados", "i", 40, CLARO if escuro else TINTA2), x, y + 48, "center", 0.06)


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


def tri(B, BC, gb, gc):
    """triângulo com a base BC deitada: ângulo gb em B e gc em C. Devolve A, B, C"""
    ga = 180 - gb - gc
    AB = BC * math.sin(math.radians(gc)) / math.sin(math.radians(ga))
    return pt(B, AB, gb), B, (B[0] + BC, B[1])


def dirg(V, P):
    return math.degrees(math.atan2(-(P[1] - V[1]), P[0] - V[0])) % 360


def faixa_v(V, P, Q):
    """g1, g2 do ângulo PVQ (o menor), com g1 < g2 podendo passar de 360"""
    a1, a2 = dirg(V, P), dirg(V, Q)
    d = (a2 - a1) % 360
    return (a1, a1 + d) if d <= 180 else (a2, a2 + (360 - d))


def canto(c, t, t0, V, P, Q, rot=None, cor=None, r=80, tr=None, size=52, alfa=0.25, reto=None):
    """ângulo interno PVQ com arco e cunha da cor da família, e a medida dentro do triângulo"""
    if t < t0:
        return
    cor = cor or E.COR
    g1, g2 = faixa_v(V, P, Q)
    if reto or (reto is None and abs(g2 - g1 - 90) < 0.6):
        E.angulo(c, t, t0, V, P, Q, None, r=r * 0.9, cor=cor, reto=True)
    else:
        q = ease_io(prog(t, t0, 0.5))
        cunha_m(c, V, g1, g1 + (g2 - g1) * q, r, cor, 1.0, alfa=alfa, borda=5)
    if rot:
        s = rot(t) if callable(rot) else rot
        E.foco(c, t, tr if tr is not None else t0 + 0.3, 0.4, lambda a: rotulo(c, V, (g1 + g2) / 2, r, s, COR if cor == E.COR else cor, size, a))


def triang(c, t, t0, A, B, C, nomes=True, tinta=TINTA, preenche=0.06, d=0.9):
    """o contorno que se desenha em volta, com os nomes dos vértices"""
    if t < t0:
        return
    pts = [A, B, C]
    if preenche:
        path = skia.Path(); path.addPoly(pts, True)
        c.drawPath(path, M.paint(E.COR, preenche * ep(t, t0 + d * 0.6, 0.5)))
    p = ease_io(prog(t, t0, d))
    for i, (P, Q) in enumerate(((A, B), (B, C), (C, A))):
        f = M.clamp(p * 3 - i)
        if f > 0:
            M.line(c, *P, lerp(P[0], Q[0], f), lerp(P[1], Q[1], f), tinta, 1.0, 6)
    if nomes:
        g = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)
        for i, (V, s) in enumerate(zip(pts, "ABC")):
            ux, uy = V[0] - g[0], V[1] - g[1]
            n = math.hypot(ux, uy)
            E.foco(c, t, t0 + 0.3 + 0.15 * i, 0.4, lambda a, V=V, s=s, ux=ux / n, uy=uy / n: centro(c, s, V[0] + ux * 64, V[1] + uy * 64 + 22, 62, "g", tinta, a))


def lados(c, t, t0, A, B, Cc, n, cor=TINTA, d=0.4):
    """tracinhos de lados iguais: n = (AB, BC, CA)"""
    q = ep(t, t0, d)
    for (P, Q), k in zip(((A, B), (B, Cc), (Cc, A)), n):
        if k:
            E.marcas_iguais(c, P, Q, k, cor, q)


def iso(B, BC, base):
    """isósceles com a base BC deitada e os ângulos da base = base"""
    return tri(B, BC, base, base)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    A, B, Cc = iso((420, 860), 760, 40)

    def um():
        triang(c, t, ka, A, B, Cc, nomes=False)
        lados(c, t, ka + 0.8, A, B, Cc, (1, 0, 1))
        canto(c, t, kb, B, A, Cc, "40°", E.COR, 110)
        canto(c, t, kc, A, B, Cc, "70°", ERRADO, 70)
        canto(c, t, kc + 0.4, Cc, A, B, "70°", ERRADO, 110)
        E.frase(c, t, ka, ps("dois lados", "i", 76) + [("iguais", "g", 80, COR)], W / 2, 170, "center", 0.12)
        E.foco(c, t, kd, 0.5, lambda a: E.pilula(c, "errado", 1560, 560, 90, "g", fundo=ERRADO, a=a))
        E.frase(c, t, kd + 1.2, ps("o detalhe", "i", 70) + [("do desenho", "g", 70)], 1560, 760, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), [("classificar", "g", 96, COR)], XE, 440, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("por lados e por ângulos", "i", 72), XE, 550, passo=0.12)
        E.frase(c, t, tb, [("achar", "g", 96)] + ps("os ângulos", "i", 84), XE, 720, passo=0.14)
        E.frase(c, t, tb + 0.6, ps("do isósceles", "i", 84), XE, 830, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 820
    itens = (("s03.b", "no triângulo,", "A + B + C = 180°"), ("s03.c", "agudo < 90°", "obtuso > 90°"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i" if i == 0 else "g", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 160)
    py = lerp(420, 700, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 920, "left", 0.12)


# ---------------- pelos lados ----------------
def b_lados(c, t, C, b):
    a4, a5, b5, c5, d5, e5 = C["s04.a"], C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]
    E.frase(c, t, C["s04"], ps("pelos", "i", 80) + [("lados", "g", 84, COR)], W / 2, 150, "center", 0.12)

    def demo():
        for i, y in enumerate((420, 620)):
            P, Q = (700, y), (1220, y)
            if t >= a4:
                M.line(c, *P, *Q, TINTA, 1.0, 7, progress=ease_io(prog(t, a4 + 0.2 * i, 0.5)))
            E.marcas_iguais(c, P, Q, 1, COR, ep(t, a4 + 0.6, 0.4), tam=22, largura=6)
        E.frase(c, t, a4 + 0.8, ps("tracinhos iguais =", "i", 64) + [("lados iguais", "g", 64, COR)], W / 2, 820, "center", 0.12)
    E.saida(c, t, C["s05"] - 0.1, demo)
    if t < C["s05"]:
        return
    figs = ((a5, iso((150, 580), 360, 60), (1, 1, 1), "equilátero", 330),
            (b5, iso((780, 580), 360, 64), (1, 0, 1), "isósceles", 960),
            (c5, ((1500, 300), (1400, 580), (1800, 580)), (1, 2, 3), "escaleno", 1600))
    for t0, (A, B, Cc), n, nome, cx in figs:
        triang(c, t, t0, A, B, Cc, nomes=False)
        lados(c, t, t0 + 0.7, A, B, Cc, n, COR)
        E.frase(c, t, t0 + 0.5, [(nome, "g", 66, COR)], cx, 700, "center")
    E.frase(c, t, a5 + 1.4, ps("3 iguais", "i", 50, TINTA2), 330, 770, "center")
    E.frase(c, t, b5 + 0.8, ps("2 iguais", "i", 50, TINTA2), 960, 770, "center")
    E.frase(c, t, c5 + 0.8, ps("todos diferentes", "i", 50, TINTA2), 1600, 770, "center")
    # sem tracinhos: as medidas
    for t0, s, nome, y in ((d5, "5 cm, 5 cm e 8 cm", "isósceles", 890), (e5, "4 cm, 5 cm e 6 cm", "escaleno", 990)):
        E.foco(c, t, t0, 0.5, lambda a, s=s, y=y: E.escreve(c, s, 560, y, 60, "b", TINTA, a))
        E.foco(c, t, t0 + 1.0, 0.5, lambda a, nome=nome, y=y: E.pilula(c, nome, 1330, y - 20, 50, "g", a=a, cor=E.SOBRE))


# ---------------- o isósceles ----------------
def b_isosceles(c, t, C, b):
    X = 1420
    a6, b6, c6, a7, b7, c7, a8, b8 = (C["s06.a"], C["s06.b"], C["s06.c"], C["s07.a"], C["s07.b"], C["s07.c"], C["s08.a"], C["s08.b"])
    A, B, Cc = iso((420, 880), 460, 70)

    def isos():
        triang(c, t, C["s06"], A, B, Cc, nomes=False)
        lados(c, t, C["s06"] + 0.8, A, B, Cc, (1, 0, 1))
        if t >= a6:
            M.line(c, *B, *Cc, E.COR, 1.0, 12, progress=ease_io(prog(t, a6, 0.5)))
            E.foco(c, t, a6 + 0.3, 0.4, lambda a: centro(c, "base", (B[0] + Cc[0]) / 2, B[1] + 80, 60, "g", COR, a))
        canto(c, t, b6, A, B, Cc, (lambda tt: "40°" if tt >= a7 else None), TINTA2, 130)
        E.foco(c, t, b6 + 0.2, 0.4, lambda a: centro(c, "topo", A[0], A[1] - 40, 60, "g", TINTA2, a))
        canto(c, t, c6, B, A, Cc, (lambda tt: "70°" if tt >= c7 + 0.5 else None), E.COR, 90)
        canto(c, t, c6 + 0.3, Cc, A, B, (lambda tt: "70°" if tt >= c7 + 0.5 else None), E.COR, 90)
        E.frase(c, t, c6, ps("ângulos da base:", "i", 64), X, 260, "center", 0.12) if t < C["s07"] else None
        E.frase(c, t, c6 + 0.8, [("iguais", "g", 96, COR)], X, 380, "center") if t < C["s07"] else None
        if t >= C["s07"]:
            E.frase(c, t, a7, ps("topo de", "i", 70) + [("40°", "g", 76, TINTA2)], X, 240, "center", 0.12)
            fcen(c, t, b7, "180 − 40 = 140", X, 400, 90)
            E.frase(c, t, b7 + 2.0, ps("divide entre os da base", "i", 56), X, 500, "center", 0.1)
            fcen(c, t, c7, "140 ÷ 2 = 70", X, 650, 90, COR)
            bola_txt(c, t, c7 + 0.6, "70°", X, 840, 105, 76)
    E.saida(c, t, C["s08"] - 0.1, isos)
    if t >= C["s08"]:
        A2, B2, C2 = iso((330, 860), 560, 60)
        triang(c, t, C["s08"], A2, B2, C2, nomes=False)
        lados(c, t, C["s08"] + 0.8, A2, B2, C2, (1, 1, 1))
        for i, (V, P, Q) in enumerate(((A2, B2, C2), (B2, A2, C2), (C2, A2, B2))):
            canto(c, t, a8 + 0.25 * i, V, P, Q, (lambda tt: "60°" if tt >= b8 + 0.6 else None), E.COR, 80)
        E.frase(c, t, C["s08"], [("equilátero", "g", 76, COR)], X, 260, "center")
        E.frase(c, t, a8, ps("3 ângulos iguais", "i", 66), X, 380, "center", 0.12)
        fcen(c, t, b8, "180 ÷ 3 = 60", X, 560, 96)
        bola_txt(c, t, b8 + 0.6, "60°", X, 760, 105, 76)


# ---------------- pelos ângulos ----------------
def b_angulos(c, t, C, b):
    a9, b9, c9, a10, b10 = C["s09.a"], C["s09.b"], C["s09.c"], C["s10.a"], C["s10.b"]
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]

    def tres():
        E.frase(c, t, C["s09"], ps("pelos", "i", 80) + [("ângulos", "g", 84, COR)], W / 2, 150, "center", 0.12)
        figs = ((a9, tri((140, 600), 380, 65, 55), "acutângulo", "3 agudos", 330, (E.COR, E.COR, E.COR)),
                (b9, tri((800, 600), 380, 90, 40), "retângulo", "1 reto", 990, (NEUTRO, E.COR, NEUTRO)),
                (c9, tri((1440, 600), 380, 115, 30), "obtusângulo", "1 obtuso", 1630, (NEUTRO, E.COR, NEUTRO)))
        for t0, (A, B, Cc), nome, sub, cx, cores in figs:
            triang(c, t, t0, A, B, Cc, nomes=False)
            for i, (V, P, Q) in enumerate(((A, B, Cc), (B, A, Cc), (Cc, A, B))):
                canto(c, t, t0 + 0.6 + 0.15 * i, V, P, Q, None, cores[i], 60)
            E.frase(c, t, t0 + 0.4, [(nome, "g", 62, COR)], cx, 720, "center")
            E.frase(c, t, t0 + 0.8, ps(sub, "i", 52, TINTA2), cx, 800, "center", 0.1)
    E.saida(c, t, C["s10"] - 0.1, tres)
    if C["s10"] <= t < C["s11"] + 0.5:
        def dois_retos():
            B, Cc = (560, 820), (1120, 820)
            triang_aberto = ep(t, a10, 0.6)
            M.line(c, *B, *Cc, TINTA, 1.0, 6)
            for P in (B, Cc):
                M.line(c, *P, P[0], P[1] - 520 * triang_aberto, TINTA, 1.0, 6)
            canto(c, t, a10 + 0.3, B, (B[0], B[1] - 100), Cc, None, E.COR, 70)
            canto(c, t, a10 + 0.5, Cc, (Cc[0], Cc[1] - 100), B, None, E.COR, 70)
            E.frase(c, t, a10 + 1.2, ps("2 retos?", "i", 70), 840, 200, "center", 0.12)
            fcen(c, t, a10 + 3.5, "90 + 90 = 180", 1520, 420, 76)
            E.frase(c, t, a10 + 5.0, ps("não sobra nada", "i", 60, ERRADO), 1520, 520, "center", 0.12)
            E.foco(c, t, b10, 0.5, lambda a: E.pilula(c, "pelo menos 2 agudos", 1520, 720, 56, "g", a=a, cor=E.SOBRE))
        E.saida(c, t, C["s11"] - 0.1, dois_retos)
    if t >= C["s11"]:
        E.frase(c, t, a11, ps("um nome pelos", "i", 64) + [("lados", "g", 66, COR)] + ps("e outro pelos", "i", 64) + [("ângulos", "g", 66, COR)],
                W / 2, 170, "center", 0.1)
        A, B, Cc = iso((200, 720), 380, 70)
        triang(c, t, b11 - 0.6, A, B, Cc, nomes=False)
        lados(c, t, b11, A, B, Cc, (1, 0, 1))
        canto(c, t, b11, A, B, Cc, "40°", TINTA2, 110, size=46)
        canto(c, t, b11 + 0.2, B, A, Cc, "70°", E.COR, 70, size=46)
        canto(c, t, b11 + 0.4, Cc, A, B, "70°", E.COR, 70, size=46)
        E.frase(c, t, b11 + 1.0, [("isósceles", "g", 60, COR)] + ps("e", "i", 60) + [("acutângulo", "g", 60, COR)], 390, 860, "center", 0.12)
        A, B, Cc = iso((1180, 720), 480, 45)
        triang(c, t, c11, A, B, Cc, nomes=False)
        lados(c, t, c11 + 0.5, A, B, Cc, (1, 0, 1))
        canto(c, t, c11 + 0.6, A, B, Cc, "90°", TINTA2, 60, size=46)
        canto(c, t, c11 + 0.8, B, A, Cc, "45°", E.COR, 80, size=46)
        canto(c, t, c11 + 1.0, Cc, A, B, "45°", E.COR, 80, size=46)
        E.frase(c, t, d11, [("isósceles", "g", 60, COR)] + ps("e", "i", 60) + [("retângulo", "g", 60, COR)], 1420, 860, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    A, B, Cc = iso((260, 860), 760, 40)
    X = 1450
    a12, b12, c12, a13, b13, c13, d13, a14 = (C["s12.a"], C["s12.b"], C["s12.c"], C["s13.a"], C["s13.b"], C["s13.c"],
                                               C["s13.d"], C["s14.a"])
    triang(c, t, C["s12"], A, B, Cc, nomes=False)
    lados(c, t, C["s12"] + 0.8, A, B, Cc, (1, 0, 1))
    canto(c, t, C["s12"] + 1.0, B, A, Cc, "40°", E.COR, 110)
    if t >= a12:
        M.line(c, *B, *Cc, E.COR, ep(t, a12, 0.4), 12)
        E.foco(c, t, a12 + 0.3, 0.4, lambda a: centro(c, "base", (B[0] + Cc[0]) / 2, B[1] + 80, 56, "g", COR, a))
    canto(c, t, a13, Cc, A, B, "40°", E.COR, 110)
    canto(c, t, b13, A, B, Cc, "100°", TINTA2, 80)

    def errado():
        E.frase(c, t, a12, ps("os", "i", 64) + [("40°", "g", 66)] + ps("eram", "i", 64) + [("da base", "g", 66, COR)], X, 240, "center", 0.12)
        fcen(c, t, b12, "(180 − 40) ÷ 2", X, 420, 80, ERRADO)
        fcen(c, t, c12, "= 70 e 70", X, 540, 80, ERRADO)
        if t >= C["s13"]:
            E.risco(c, X - 300, 560, X + 300, 360, t, C["s13"], largura=12)
    E.saida(c, t, a13 - 0.2, errado)
    if t >= a13:
        def certo():
            E.frase(c, t, a13, ps("base:", "i", 64) + [("40°", "g", 70, COR)] + ps("e", "i", 64) + [("40°", "g", 70, COR)], X, 240, "center", 0.12)
            fcen(c, t, b13, "180 − 40 − 40 = 100", X, 400, 76, TINTA2)
            fcen(c, t, c13, "40°, 40° e 100°", X, 560, 80)
            E.foco(c, t, d13, 0.5, lambda a: E.pilula(c, "obtusângulo", X, 720, 66, "g", a=a, cor=E.SOBRE))
        E.saida(c, t, C["s14"] - 0.1, certo)
    if t >= C["s14"]:
        E.frase(c, t, a14, ps("antes de calcular:", "i", 66), X, 330, "center", 0.12)
        E.frase(c, t, a14 + 1.0, [("topo", "g", 110, TINTA2)] + ps("ou", "i", 90) + [("base?", "g", 110, COR)], X, 520, "center", 0.2)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a15, b15, c15, d15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    a16, b16, c16 = C["s16.a"], C["s16.b"], C["s16.c"]

    def regra():
        E.frase(c, t, C["s15"] + 0.5, ps("pelos ângulos:", "i", 70, CLARO), W / 2, 180, "center", 0.12)
        E.frase(c, t, a15, ps("olhe só", "i", 90, BR) + [("o maior", "g", 100, CLARO)], W / 2, 320, "center", 0.14)
        linhas = ((b15, "menor que 90°", "acutângulo", 45), (c15, "igual a 90°", "retângulo", 90), (d15, "maior que 90°", "obtusângulo", 130))
        for i, (t0, s, nome, g) in enumerate(linhas):
            y = 520 + i * 170
            V = (420, y + 30)
            if t >= t0:
                q = ease_io(prog(t, t0, 0.5))
                M.line(c, *V, V[0] + 150 * q, V[1], BR, 1.0, 6)
                M.line(c, *V, *pt(V, 150 * q, g), BR, 1.0, 6)
                E.angulo(c, t, t0, V, pt(V, 10, 0), pt(V, 10, g), None, r=55, cor=CLARO)
            E.frase(c, t, t0 + 0.2, [(s, "g", 62, CLARO)], 680, y + 20, "left")
            E.foco(c, t, t0 + 0.6, 0.5, lambda a, nome=nome, y=y: E.pilula(c, nome, 1460, y, 60, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s16"] - 0.1, regra)
    if t >= C["s16"]:
        E.frase(c, t, a16, ps("os outros:", "i", 76, CLARO) + [("sempre agudos", "g", 80, BR)], W / 2, 300, "center", 0.12)
        E.frase(c, t, b16, ps("falta um ângulo?", "i", 76, CLARO), W / 2, 500, "center", 0.12)
        E.frase(c, t, b16 + 1.2, [("calcule o terceiro antes", "g", 76, BR)], W / 2, 620, "center")
        E.frase(c, t, c16, ps("ele pode ser", "i", 76, CLARO) + [("o maior", "g", 84, ERRADO)], W / 2, 820, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    A, B, Cc = iso((1220, 900), 440, 72)
    a17, b17, c17, d17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a17, [("2 lados iguais", "g", 76)], XE, 340)
    E.frase(c, t, b17, ps("entre eles:", "i", 76) + [("36°", "g", 84, TINTA2)], XE, 470, passo=0.12)
    E.frase(c, t, c17, ps("cada ângulo", "i", 76) + [("da base?", "g", 80, COR)], XE, 630, passo=0.12)
    E.frase(c, t, d17, ps("e a", "i", 76) + [("classificação?", "g", 80, COR)], XE, 760, passo=0.12)

    def fig():
        triang(c, t, a17, A, B, Cc, nomes=False)
        lados(c, t, a17 + 0.8, A, B, Cc, (1, 0, 1))
        canto(c, t, b17, A, B, Cc, "36°", TINTA2, 150)
        canto(c, t, c17, B, A, Cc, "?", E.COR, 80)
        canto(c, t, c17 + 0.2, Cc, A, B, "?", E.COR, 80)
    E.saida(c, t, C["s18.a"] - 0.1, fig)
    E.relogio(c, t, C["s18.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    A, B, Cc = iso((360, 900), 440, 72)
    X = 1300
    a19, b19, c19, a20, b20, c20 = C["s19.a"], C["s19.b"], C["s19.c"], C["s20.a"], C["s20.b"], C["s20.c"]
    triang(c, t, C["s19"], A, B, Cc, nomes=False)
    lados(c, t, C["s19"] + 0.8, A, B, Cc, (1, 0, 1))
    canto(c, t, C["s19"] + 0.5, A, B, Cc, "36°", TINTA2, 150)
    E.foco(c, t, a19, 0.4, lambda a: centro(c, "topo", A[0], A[1] - 40, 56, "g", TINTA2, a))
    canto(c, t, C["s19"] + 0.7, B, A, Cc, (lambda tt: "72°" if tt >= c19 + 0.5 else "?"), E.COR, 80)
    canto(c, t, C["s19"] + 0.9, Cc, A, B, (lambda tt: "72°" if tt >= c19 + 0.5 else "?"), E.COR, 80)

    def contas():
        E.frase(c, t, a19, [("36°", "g", 76, TINTA2)] + ps("é o", "i", 70) + [("topo", "g", 76, TINTA2)], X, 240, "center", 0.12)
        fcen(c, t, b19, "180 − 36 = 144", X, 420, 96)
        fcen(c, t, c19, "144 ÷ 2 = 72", X, 580, 96, COR)
        bola_txt(c, t, c19 + 0.6, "72°", X, 790, 110, 80)
    E.saida(c, t, C["s20"] - 0.1, contas)
    if t >= C["s20"]:
        E.frase(c, t, a20, ps("pelos lados:", "i", 66), X, 240, "center", 0.12)
        E.foco(c, t, a20 + 0.4, 0.5, lambda a: E.pilula(c, "isósceles", X, 330, 64, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, lerp(a20, b20, 0.4), ps("maior: 72° < 90°", "b", 60, TINTA2), X, 500, "center", 0.12)
        E.foco(c, t, b20, 0.5, lambda a: E.pilula(c, "acutângulo", X, 600, 64, "g", a=a, cor=E.SOBRE))
        fcen(c, t, c20, "36 + 72 + 72 = 180", X, 790, 80)
        E.foco(c, t, c20 + 1.2, 0.4, lambda a: E.selo(c, X, 920, 52, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s21.a", "lados: conte os iguais"), ("s21.b", "ângulos: olhe o maior"), ("s21.c", "isósceles: base com ângulos iguais"))
        for i, (k, s) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 74)], 400, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22.a"] - 1.0, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s22.a"], [("Três medidas", "g", 130, COR)], XE, 450)
    E.frase(c, t, C["s22.a"] + 0.3, [("formam triângulo?", "g", 110, COR)], XE, 590)
    E.frase(c, t, C["s22.b"], ps("nem sempre:", "i", 76) + [("aprenda a testar", "g", 76)], XE, 720, passo=0.12)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 300, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(620, 325, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, lados=b_lados, isosceles=b_isosceles, angulos=b_angulos, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
