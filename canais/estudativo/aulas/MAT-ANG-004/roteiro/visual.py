"""Visual — Estudativo · MAT-ANG-004: soma dos ângulos do triângulo e ângulo externo.
Linguagem da geometria plana (MAT-ANG-001 a 003): lados em tinta; ângulos iguais com a mesma cor. Num triângulo, cada vértice tem a
sua família: A em COR (índigo), B em TINTA2 (cinza escuro), C em AMBAR (3ª família, só quando há três ângulos diferentes).
A prova se faz movendo ângulos com voa(): a cunha de B sobe até A (gira meia volta, como alterno interno) e a de C também;
no externo, as cunhas de A e B viajam até C e enchem o ângulo externo. Resposta na esfera; medidas na grotesca.
Peças locais: tri() acha o 3º vértice pelos ângulos da base; dirg() dá a direção de um lado; peca() é uma ponta de papel rasgada;
canto() desenha o ângulo interno de um vértice com arco e medida. Todo instante vem de C[...]."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-004_soma_dos_angulos_e_angulo_externo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("prova", "terceiro", "externo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
assert 50 + 60 + 70 == 180 and 180 - 110 == 70 and 90 - 25 == 65 and 180 - 70 == 110 == 50 + 60
assert 180 - 120 - 50 == 10 and 120 - 50 == 70 and 3 * 50 == 150 and 180 - 150 == 30 and 50 + 100 + 30 == 180


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


def peca(c, V, rot, g1, g2, L, cor, a=1.0):
    """ponta de papel rasgada em V, girada rot graus; o ângulo dela vai de g1 a g2"""
    if a <= 0:
        return
    P1, P2 = pt(V, L, g1 + rot), pt(V, L, g2 + rot)
    path = skia.Path(); path.moveTo(*V); path.lineTo(*P1)
    nx, ny = (P2[1] - P1[1]), -(P2[0] - P1[0])
    nn = math.hypot(nx, ny) or 1
    for i in range(1, 7):
        f = i / 7
        k = 9 if i % 2 else -9
        path.lineTo(lerp(P1[0], P2[0], f) + nx / nn * k, lerp(P1[1], P2[1], f) + ny / nn * k)
    path.lineTo(*P2); path.close()
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.2 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
    c.save(); c.translate(5, 9); c.drawPath(path, s); c.restore()
    c.drawPath(path, M.paint("#FFFFFF", a))
    c.drawPath(path, M.paint(CINZA, a, stroke=2))
    cunha_m(c, V, g1 + rot, g2 + rot, L * 0.5, cor, a, alfa=0.35, borda=5)


def arco_ext(c, t, t0, V, g, r, a=1.0, cor=TINTA):
    """o ângulo externo: arco em tinta de 0 até g graus"""
    if t >= t0 and a > 0:
        ret = skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r)
        c.drawArc(ret, 0, -g * ease_io(prog(t, t0, 0.6)), False, M.paint(cor, a, stroke=6, cap_round=True))


# triângulo das aulas: B = 60°, C = 70°, A = 50°
TA, TB, TC = tri((380, 850), 520, 60, 70)
FA, FB, FC = (240, 290), (0, 60), (110, 180)  # faixa de cada ângulo interno (graus)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd, ke = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"], C["s01.e"]
    A, B, Cc = tri((200, 720), 600, 60, 70)
    O = (1380, 760)
    Lp = 170

    def um():
        rasga = ep(t, kb, 0.5)
        if t >= ka:
            a = ep(t, ka, 0.6)
            u = lambda V, P: pt(V, Lp, dirg(V, P))
            hexa = [u(A, B), u(B, A), u(B, Cc), u(Cc, B), u(Cc, A), u(A, Cc)]
            pts = hexa if rasga > 0 else [A, B, Cc]
            s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.2 * a))
            s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 12))
            path = skia.Path(); path.addPoly(pts, True)
            c.save(); c.translate(6, 12); c.drawPath(path, s); c.restore()
            c.drawPath(path, M.paint("#FFFFFF", a))
            c.drawPath(path, M.paint(CINZA, a, stroke=2))
        # as três pontas: soltam no rasgo e voam até a linha
        for V, (g1, g2), giro, cor, i in ((B, FB, 0, TINTA2, 0), (A, FA, -180, E.COR, 1), (Cc, FC, 0, AMBAR, 2)):
            if t < kb:
                continue
            p = ease_io(prog(t, kc + 0.5 * i, 1.0))
            g = (g1 + g2) / 2
            solto = pt(V, 30 * rasga, g + 180)
            pos = (lerp(solto[0], O[0], p), lerp(solto[1], O[1], p))
            peca(c, pos, giro * p, g1, g2, Lp, cor, 1.0)
        if t >= kd:
            M.line(c, O[0] - 420, O[1], O[0] + 420, O[1], TINTA, 1.0, 7, progress=ease_io(prog(t, kd, 0.6)))
            E.arco(c, O[0], O[1], 230, 180, 180 * ease_io(prog(t, kd + 0.3, 0.6)), E.COR, 6)
            E.foco(c, t, kd + 0.6, 0.4, lambda a: centro(c, "180°", O[0], O[1] - 260, 72, "g", COR, a))
        E.frase(c, t, kd, ps("sempre dá uma", "i", 72) + [("linha reta", "g", 72, COR)], O[0], 920, "center", 0.12)
        E.frase(c, t, ke, [("sempre", "g", 96, COR)], 600, 960, "center")
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), [("entender", "g", 96, COR)] + ps("o porquê", "i", 84), XE, 450, passo=0.14)
        E.frase(c, t, tb, [("achar", "g", 96)] + ps("o ângulo", "i", 84), XE, 610, passo=0.14)
        E.frase(c, t, tb + 0.5, ps("que falta", "i", 84), XE, 720, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "do externo", 1500, 620, 72, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 820
    itens = (("s03.b", "linha reta", "raso = 180°"), ("s03.c", "com paralelas,", "alternos internos iguais"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
    py = lerp(420, 700, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 920, "left", 0.12)


# ---------------- por que 180° ----------------
def b_prova(c, t, C, b):
    A, B, Cc = TA, TB, TC
    X = 1560
    a4, b4, a5, b5 = C["s04.a"], C["s04.b"], C["s05.a"], C["s05.b"]
    a6, b6, c6, a7, b7, c7 = C["s06.a"], C["s06.b"], C["s06.c"], C["s07.a"], C["s07.b"], C["s07.c"]
    triang(c, t, a4, A, B, Cc)
    # a paralela por A
    if t >= b4:
        q = ease_io(prog(t, b4, 0.8))
        M.line(c, A[0] - 520 * q, A[1], A[0] + 520 * q, A[1], TINTA2, 1.0, 6)
        k = ep(t, b4 + 0.8, 0.4)
        for (x, y) in ((A[0] + 400, A[1]), (B[0] + 400, B[1])):
            M.line(c, x - 14, y - 16, x + 6, y, TINTA, k, 5)
            M.line(c, x - 14, y + 16, x + 6, y, TINTA, k, 5)
    # os três ângulos lá em cima: primeiro neutros, depois cada um ganha a cor do seu par
    r = 90
    if t >= a5:
        cB = E.mix(CINZA, TINTA2, ep(t, a6 + 2.4, 0.4))
        cC = E.mix(CINZA, AMBAR, ep(t, c6 + 2.0, 0.4))
        cunha_m(c, A, 180, 180 + 60 * ease_io(prog(t, a5, 0.5)), r, cB, alfa=0.25, borda=5)
        cunha_m(c, A, 290, 290 + 70 * ease_io(prog(t, a5 + 0.3, 0.5)), r, cC, alfa=0.25, borda=5)
    canto(c, t, b5, A, B, Cc, cor=E.COR, r=r)
    canto(c, t, a6, B, A, Cc, cor=TINTA2, r=r)
    canto(c, t, c6 - 0.3, Cc, A, B, cor=AMBAR, r=r)
    # o ângulo de B sobe até A girando meia volta; o de C também
    voa(c, t, a6 + 1.0, 1.4, B, *FB, r, TINTA2, V1=A, giro=180, fica=0.6)
    voa(c, t, c6 + 0.4, 1.4, Cc, *FC, r, AMBAR, V1=A, giro=180, fica=0.6)
    if t >= b7:
        E.arco(c, A[0], A[1], 150, 0, 180 * ease_io(prog(t, b7, 0.7)), E.COR, 6)
        E.foco(c, t, b7 + 0.5, 0.4, lambda a: centro(c, "180°", A[0] + 240, A[1] + 130, 64, "g", COR, a))

    def texto():
        E.frase(c, t, b4, ps("paralela ao lado", "i", 66), X, 260, "center", 0.12)
        E.frase(c, t, b4 + 0.8, [("BC", "g", 72, TINTA2)], X, 360, "center")
        E.frase(c, t, a5, ps("3 ângulos", "i", 66) + [("lado a lado", "g", 66, COR)], X, 520, "center", 0.12)
        E.frase(c, t, b5, ps("o do meio:", "i", 60) + [("A", "g", 66, COR)], X, 640, "center", 0.12)
    E.saida(c, t, C["s06"] - 0.1, texto)
    if C["s06"] <= t:
        def iguais():
            E.frase(c, t, a6, ps("alterno interno", "i", 64), X, 260, "center", 0.12)
            E.frase(c, t, b6, ps("esquerda =", "i", 64) + [("B", "g", 72, TINTA2)], X, 400, "center", 0.12)
            E.frase(c, t, c6, ps("direita =", "i", 64) + [("C", "g", 72, AMBAR)], X, 520, "center", 0.12)
        E.saida(c, t, C["s07"] - 0.1, iguais)
    if C["s07"] <= t:
        E.frase(c, t, a7, ps("os 3 ângulos", "i", 66), X, 280, "center", 0.12)
        E.frase(c, t, b7, ps("numa", "i", 66) + [("linha reta", "g", 66, COR)], X, 390, "center", 0.12)
        E.foco(c, t, c7, 0.5, lambda a: E.pilula(c, "A + B + C = 180°", X, 600, 62, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, c7 + 1.2, ps("em qualquer triângulo", "i", 60), X, 740, "center", 0.12)


# ---------------- o terceiro ângulo ----------------
def b_terceiro(c, t, C, b):
    X = 1450
    a8, a9, b9, c9 = C["s08.a"], C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]

    def um():
        A, B, Cc = TA, TB, TC
        triang(c, t, C["s08"], A, B, Cc)
        canto(c, t, a8, A, B, Cc, "50°", E.COR, 80)
        canto(c, t, a8 + 0.6, B, A, Cc, "60°", TINTA2, 80)
        canto(c, t, a8 + 1.2, Cc, A, B, (lambda tt: "70°" if tt >= b9 + 0.6 else "?"), AMBAR, 80)
        E.frase(c, t, a8 + 1.6, ps("e o terceiro?", "i", 70), X, 260, "center", 0.12)
        fcen(c, t, a9, "50 + 60 = 110", X, 420, 90)
        fcen(c, t, b9 - 0.2, "180 − 110 = 70", X, 560, 90)
        bola_txt(c, t, b9 + 0.6, "70°", X, 740, 110, 80, AMBAR)
        fcen(c, t, c9, "50 + 60 + 70 = 180", X, 950, 66, TINTA2)
        E.foco(c, t, c9 + 1.2, 0.4, lambda a: E.selo(c, X + 360, 926, 40, True, a))
    E.saida(c, t, C["s10"] - 0.1, um)
    if t >= C["s10"]:
        A, B, Cc = (260, 430), (260, 850), (1160, 850)
        triang(c, t, C["s10"], A, B, Cc)
        canto(c, t, a10, B, A, Cc, None, TINTA2, 80)
        canto(c, t, c10, Cc, A, B, "25°", AMBAR, 150)
        canto(c, t, d10, A, B, Cc, "65°", E.COR, 90)
        E.frase(c, t, a10, ps("com", "i", 70) + [("um reto", "g", 72, COR)], X, 260, "center", 0.12)
        fcen(c, t, a10 + 2.0, "180 − 90 = 90", X, 400, 84, TINTA2)
        E.frase(c, t, b10, ps("os outros:", "i", 64), X, 520, "center", 0.12)
        E.frase(c, t, b10 + 0.6, [("complementares", "g", 64, COR)], X, 610, "center")
        fcen(c, t, d10 - 0.8, "90 − 25 = 65", X, 760, 90)
        bola_txt(c, t, d10, "65°", X, 920, 95, 72)


# ---------------- ângulo externo ----------------
def b_externo(c, t, C, b):
    A, B, Cc = TA, TB, TC
    D = (Cc[0] + 330, Cc[1])
    X = 1580
    a11, b11, c11, a12, b12 = C["s11.a"], C["s11.b"], C["s11.c"], C["s12.a"], C["s12.b"]
    a13, b13, c13, a14, b14, c14 = C["s13.a"], C["s13.b"], C["s13.c"], C["s14.a"], C["s14.b"], C["s14.c"]
    triang(c, t, C["s11"], A, B, Cc)
    canto(c, t, a11, A, B, Cc, "50°", E.COR, 80)
    canto(c, t, a11 + 0.5, B, A, Cc, "60°", TINTA2, 80)
    canto(c, t, a11 + 1.0, Cc, A, B, "70°", AMBAR, 70)
    if t >= b11:
        M.line(c, *Cc, *D, TINTA, 1.0, 6, dash=E.TRACO, progress=ease_io(prog(t, b11, 0.7)))
    # o externo: arco em tinta; depois as cunhas de A e B chegam e o enchem
    re_ = 125
    arco_ext(c, t, c11, Cc, 110, re_)
    E.foco(c, t, b12, 0.4, lambda a: rotulo(c, Cc, 55, re_, "110°", TINTA, 56, a * (1 - ep(t, a13 + 0.2, 0.4))))
    if t >= a12:
        E.arco(c, Cc[0], Cc[1], 250, 180, 180, CERTO, 5, ep(t, a12, 0.5) * (1 - ep(t, C["s13"], 0.4)))
    t_v = a13 + 0.3
    voa(c, t, t_v, 1.3, B, *FB, re_, TINTA2, V1=Cc, fica=0.2)
    voa(c, t, t_v + 1.0, 1.4, A, *FA, re_, E.COR, V1=Cc, giro=180, fica=0.2)
    cunha_m(c, Cc, 0, 60, re_, TINTA2, ep(t, t_v + 1.4, 0.3), alfa=0.35, borda=5)
    cunha_m(c, Cc, 60, 110, re_, E.COR, ep(t, t_v + 2.5, 0.3), alfa=0.35, borda=5)
    E.foco(c, t, t_v + 1.6, 0.4, lambda a: rotulo(c, Cc, 30, re_, "60°", TINTA2, 48, a))
    E.foco(c, t, t_v + 2.7, 0.4, lambda a: rotulo(c, Cc, 85, re_, "50°", COR, 48, a))

    def um():
        E.frase(c, t, b11, ps("prolongue", "i", 66) + [("BC", "g", 70)], X, 260, "center", 0.12)
        E.frase(c, t, c11, [("ângulo externo", "g", 62)] + ps("em C", "i", 60), X, 380, "center", 0.12)
    E.saida(c, t, C["s12"] - 0.1, um)
    if C["s12"] <= t:
        def dois():
            E.frase(c, t, a12, ps("com o de dentro:", "i", 64), X, 260, "center", 0.12)
            E.frase(c, t, a12 + 0.8, [("linha reta", "g", 70, CERTO)], X, 360, "center")
            fcen(c, t, b12, "180 − 70 = 110°", X, 500, 76)
        E.saida(c, t, C["s13"] - 0.1, dois)
    if C["s13"] <= t:
        def tres():
            fcen(c, t, a13, "110 = 50 + 60", X, 280, 84)
            E.frase(c, t, b13, ps("os de", "i", 64) + [("A", "g", 70, COR)] + ps("e", "i", 64) + [("B", "g", 70, TINTA2)], X, 410, "center", 0.12)
            E.frase(c, t, b13 + 1.4, ps("não encostam no C", "i", 60), X, 500, "center", 0.12)
            E.foco(c, t, c13, 0.5, lambda a: E.pilula(c, "externo = A + B", X, 680, 64, "g", a=a, cor=E.SOBRE))
            E.frase(c, t, c13 + 1.0, ps("os internos não vizinhos", "i", 56, TINTA2), X, 790, "center", 0.1)
        E.saida(c, t, C["s14"] - 0.1, tres)
    if C["s14"] <= t:
        fcen(c, t, a14, "externo + C = 180", X, 300, 68)
        fcen(c, t, b14, "A + B + C = 180", X, 440, 76)
        E.foco(c, t, c14, 0.5, lambda a: E.pilula(c, "externo = A + B", X, 620, 64, "g", a=a, cor=E.SOBRE))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    A, B, Cc = tri((300, 870), 560, 70, 60)
    D = (Cc[0] + 300, Cc[1])
    X = 1480
    a15, b15, c15, a16, b16, c16, d16 = (C["s15.a"], C["s15.b"], C["s15.c"], C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"])
    E.frase(c, t, C["s15"], [("cuidado", "g", 90, ERRADO)] + ps("com este erro", "i", 84), W / 2, 150, "center", 0.12)
    E.frase(c, t, a15, ps("o externo", "i", 54) + [("não é de dentro", "g", 54, ERRADO)], X, 290, "center", 0.12)
    triang(c, t, C["s15"] + 0.5, A, B, Cc)
    if t >= b15 - 0.6:
        M.line(c, *Cc, *D, TINTA, 1.0, 6, dash=E.TRACO, progress=ease_io(prog(t, b15 - 0.6, 0.6)))
    arco_ext(c, t, b15, Cc, 120, 115)
    E.foco(c, t, b15 + 0.3, 0.4, lambda a: rotulo(c, Cc, 60, 115, "120°", TINTA, 56, a))
    canto(c, t, c15, A, B, Cc, "50°", E.COR, 80)
    canto(c, t, c15 + 0.8, B, A, Cc, (lambda tt: "70°" if tt >= d16 + 0.5 else "?"), TINTA2, 80)
    fcen(c, t, a16, "180 − 120 − 50 = 10°", X, 440, 62, ERRADO)
    if t >= c16:
        E.risco(c, X - 330, 455, X + 330, 390, t, c16, largura=12)
    E.frase(c, t, c16, ps("o certo:", "i", 56) + [("externo = A + B", "g", 54, CERTO)], X, 600, "center", 0.12)
    fcen(c, t, d16, "120 − 50 = 70°", X, 760, 84, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    A, B, Cc = TA, TB, TC
    D = (Cc[0] + 330, Cc[1])
    X = 1580
    a17, b17, a18, b18, c18 = C["s17.a"], C["s17.b"], C["s18.a"], C["s18.b"], C["s18.c"]
    triang(c, t, C["s17"], A, B, Cc, tinta=BR, preenche=0.12)
    if t >= C["s17"] + 0.6:
        M.line(c, *Cc, *D, BR, 1.0, 6, dash=E.TRACO, progress=ease_io(prog(t, C["s17"] + 0.6, 0.6)))
    canto(c, t, a17, A, B, Cc, None, CLARO, 80)
    canto(c, t, a17 + 0.3, B, A, Cc, None, CLARO, 80)
    if t >= a17:
        cunha_m(c, Cc, 0, 110 * ease_io(prog(t, a17 + 0.5, 0.6)), 125, BR, 1.0, alfa=0.3, borda=6)
    # o vizinho, que o atalho pula
    if t >= b17:
        cunha_m(c, Cc, 110, 180, 70, ERRADO, ep(t, b17, 0.4), alfa=0.35, borda=5)

    def regra():
        E.frase(c, t, a17, [("externo", "g", 90, BR)], X, 280, "center")
        E.frase(c, t, a17 + 0.6, ps("= soma dos internos", "i", 64, CLARO), X, 390, "center", 0.12)
        E.frase(c, t, a17 + 1.4, [("de longe", "g", 80, CLARO)], X, 490, "center")
        E.frase(c, t, b17, ps("pula o", "i", 64, CLARO) + [("vizinho", "g", 66, ERRADO)], X, 680, "center", 0.12)
    E.saida(c, t, C["s18"] - 0.1, regra)
    if t >= C["s18"]:
        E.frase(c, t, a18, ps("os dois completam", "i", 64, CLARO), X, 260, "center", 0.12)
        E.frase(c, t, a18 + 1.0, [("180°", "g", 90, BR)] + ps("com o vizinho", "i", 64, CLARO), X, 370, "center", 0.12)
        E.frase(c, t, b18, ps("pergunta é o", "i", 60, CLARO) + [("vizinho?", "g", 64, ERRADO)], X, 560, "center", 0.12)
        fcen(c, t, c18, "180 − externo", X, 720, 90, BR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    A, B, Cc = tri((1020, 760), 520, 100, 30)
    D = (Cc[0] + 300, Cc[1])
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a19, ps("externo em C:", "i", 70), XE, 360, passo=0.12)
    fcen(c, t, a19 + 0.6, "150°", XE + 140, 480, 100)
    E.frase(c, t, b19, ps("em A e em B:", "i", 70), XE, 620, passo=0.12)
    fcen(c, t, b19 + 0.6, "x e 2x", XE + 170, 740, 100, COR)
    E.frase(c, t, c19, ps("quanto mede", "i", 76) + [("cada um?", "g", 80, COR)], XE, 900, passo=0.14)

    def fig():
        triang(c, t, C["s19"] + 0.5, A, B, Cc)
        if t >= a19:
            M.line(c, *Cc, *D, TINTA, 1.0, 6, dash=E.TRACO, progress=ease_io(prog(t, a19, 0.6)))
        arco_ext(c, t, a19 + 0.3, Cc, 150, 110)
        E.foco(c, t, a19 + 0.6, 0.4, lambda a: rotulo(c, Cc, 30, 110, "150°", TINTA, 52, a))
        canto(c, t, b19, A, B, Cc, "x", E.COR, 70)
        canto(c, t, b19 + 0.4, B, A, Cc, "2x", TINTA2, 60)
    E.saida(c, t, C["s20.a"] - 0.1, fig)
    E.relogio(c, t, C["s20.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    A, B, Cc = tri((260, 820), 520, 100, 30)
    D = (Cc[0] + 280, Cc[1])
    X = 1450
    a21, b21, c21, d21 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
    a22, b22, c22, d22 = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"]
    triang(c, t, C["s21"], A, B, Cc)
    if t >= C["s21"]:
        M.line(c, *Cc, *D, TINTA, 1.0, 6, dash=E.TRACO)
    arco_ext(c, t, C["s21"], Cc, 150, 110)
    E.foco(c, t, C["s21"] + 0.3, 0.4, lambda a: rotulo(c, Cc, 30, 110, "150°", TINTA, 50, a))
    canto(c, t, C["s21"] + 0.4, A, B, Cc, (lambda tt: "50°" if tt >= a22 else "x"), E.COR, 70)
    canto(c, t, C["s21"] + 0.6, B, A, Cc, (lambda tt: "100°" if tt >= b22 else "2x"), TINTA2, 60)
    canto(c, t, c22, Cc, A, B, "30°", AMBAR, 100)

    def contas():
        E.frase(c, t, a21, [("externo = A + B", "g", 66, COR)], X, 220, "center")
        fcen(c, t, b21, "x + 2x = 150", X, 380, 96)
        fcen(c, t, c21, "3x = 150", X, 530, 96)
        E.foco(c, t, d21, 0.5, lambda a: E.pilula(c, "x = 50", X, 690, 90, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s22"] - 0.1, contas)
    if t >= C["s22"]:
        fcen(c, t, a22, "A = 50°", X, 240, 84, COR)
        fcen(c, t, b22, "B = 2 · 50 = 100°", X, 380, 84, TINTA2)
        fcen(c, t, c22, "C = 180 − 150 = 30°", X, 520, 72, AMBAR)
        fcen(c, t, d22, "50 + 100 + 30 = 180", X, 700, 76)
        E.foco(c, t, d22 + 1.2, 0.4, lambda a: E.selo(c, X, 840, 56, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s23.a", "A + B + C = 180°"), ("s23.b", "externo = soma dos de longe"))
        for i, (k, s) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 380, y - 30, 56, a=a), centro(c, str(i + 1), 380, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 480, y)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24.a"] - 1.0, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s24.a"], [("Classificar", "g", 140, COR)], XE, 450)
    E.frase(c, t, C["s24.a"] + 0.3, [("triângulos", "g", 140, COR)], XE, 590)
    E.frase(c, t, C["s24.b"], ps("e o de", "i", 76) + [("dois lados iguais", "g", 76)], XE, 720, passo=0.12)
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, prova=b_prova, terceiro=b_terceiro, externo=b_externo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
