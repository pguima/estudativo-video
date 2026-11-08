"""Visual — Estudativo · MAT-TRA-003: qual lei usar (par completo → senos; LAL ou LLL → cossenos; dois ângulos → o terceiro pela
soma e senos; lago: 80 m, 50 m e 60° → 70 m; 4, 5, 7 → 49 > 41, obtusângulo; questão 6, 8, 11 → 121 > 100).
Linguagem da Trigonometria Avançada (MAT-TRA-001 e 002): o PAR (lado + ângulo de frente) numa cor só; índigo = o que a questão dá,
âmbar = o que se quer. O lago é uma mancha azul-clara entre os dois pontos; o terceiro ponto fica na margem de baixo.
A decisão é um fluxograma de duas saídas ("tem par completo?"), que volta no resumo. A figura não mente: o triângulo do lago é
80-50-70 com 60° de verdade, e o 4-5-7 tem o ângulo obtuso (≈ 101,5°) de frente para o 7.
Peças locais: as de MAT-TRA-001 (tri(), rot(), fra(), lei(), resp(), lista()), por_lados(), por_tres(), lago(), caixa_dec().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria Avançada")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRA-003_qual_lei_usar_senos_ou_cossenos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("decide", "lago", "lados", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
PAR1, PAR2, PAR3 = E.COR, AMBAR, "#C0187C"
AGUA = "#0A93E0"
S = lambda g: math.sin(math.radians(g))
Cs = lambda g: math.cos(math.radians(g))
assert 80 ** 2 + 50 ** 2 - 80 * 50 == 4900 == 70 ** 2 and abs(math.sqrt(80 ** 2 + 50 ** 2 - 2 * 80 * 50 * Cs(60)) - 70) < 1e-9
assert 16 + 25 == 41 and 49 - 41 == 8 and (16 + 25 - 49) / 40 == -0.2 and 121 > 36 + 64 == 100


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def _w(s, size, est="g"):
    return E.formula(None, s, 0, 0, size, est, a=0)


def cf(c, partes, x, y, size, a=1.0, align="left", est="g"):
    ws = [_w(s, size, est) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    if c is not None and a > 0:
        for (s, cor), wi in zip(partes, ws):
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += wi
    return sum(ws)


def cf_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: cf(c, partes, x, y, size, a, align))


def resp(c, t, t0, partes, cx, cy, size=64, alto=1.75, cor=None):
    if isinstance(partes, str):
        partes = [(partes, BR)]

    def f(a):
        w = cf(None, partes, 0, 0, size) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        cf(c, partes, cx, cy + size * 0.36, size, a, "center")
    E.foco(c, t, t0, 0.5, f)


def lista(c, t, itens, x, y0, dy=150, size=60):
    for i, (t0, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - size * 0.36, 40, a=a),
                                                   centro(c, str(i + 1), x + 40, y - size * 0.36 + 18, 50, "g", BR, a)))
        E.frase(c, t, t0 + 0.1, partes, x + 110, y, "left", 0.1)


def fra(c, cima, baixo, x, y, size, a=1.0, cc=TINTA, cb=TINTA, est="g", barra=TINTA):
    """fração empilhada com cima e baixo em cores próprias; y = linha de base da conta. Devolve a largura"""
    s_ = size * 0.78
    wc, wb = _w(cima, s_, est), _w(baixo, s_, est)
    w = max(wc, wb) + size * 0.16
    if c is not None and a > 0:
        E.formula(c, cima, x + (w - wc) / 2, y - size * 0.46, s_, est, cc, a)
        E.formula(c, baixo, x + (w - wb) / 2, y + size * 0.46, s_, est, cb, a)
        b = max(4, size * 0.07)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - size * 0.3 - b / 2, w, b), b / 2, b / 2), M.paint(barra, a))
    return w


def lei(c, pares, x, y, size, a=1.0, tinta=TINTA, align="left"):
    """lado/sen ângulo = lado/sen ângulo ...; pares = [(lado, ângulo, cor)]"""
    ws = [fra(None, l, f"sen {g}", 0, 0, size) for l, g, _ in pares]
    weq = _w(" = ", size)
    tot = sum(ws) + weq * (len(pares) - 1)
    xx = x - tot / 2 if align == "center" else x
    for i, ((l, g, cor), w) in enumerate(zip(pares, ws)):
        fra(c, l, f"sen {g}", xx, y, size, a, cor, cor, barra=tinta)
        xx += w
        if i < len(pares) - 1:
            E.formula(c, " = ", xx, y, size, "g", tinta, a)
            xx += weq
    return tot


def rot(c, P, Q, s, G, size=60, cor=None, a=1.0, gap=20, est="b"):
    """rótulo ao lado do segmento PQ, do lado de fora do triângulo de centro G"""
    if a <= 0 or not s:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
    if (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 < (mx - G[0]) ** 2 + (my - G[1]) ** 2:
        nx, ny = -nx, -ny
    E._cola(c, s, mx, my, nx, ny, gap, size, est, cor or TINTA, a)


def pontos(base, ga, gb, x0, y0):
    """vértices A (esquerda), B (direita) e C (topo) de um triângulo com base AB = base px e ângulos ga em A e gb em B"""
    gc = 180 - ga - gb
    ac = base * S(gb) / S(gc)
    A = (x0, y0)
    B = (x0 + base, y0)
    C = (x0 + ac * math.cos(math.radians(ga)), y0 - ac * S(ga))
    return A, B, C


def tri(c, t, t0, A, B, Cc, angs, lados, ta=None, tl=None, cores=None, size=60, escuro=False, r_ang=78):
    """triângulo ABC. angs = (rótulo em A, em B, em C) ou None; lados = (AB, BC, CA) ou None; ta/tl = instantes;
    cores = {"A"|"B"|"C": (instante, cor)} pinta o ângulo e o lado de frente para ele (o par)"""
    G = ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3)
    E.triangulo(c, t, t0, A, B, Cc, vertices=None, preenche=0.06, d=0.9, escuro=escuro)
    cores = cores or {}
    frente = {"A": (B, Cc), "B": (Cc, A), "C": (A, B)}
    for k, (P, Q) in frente.items():
        if k in cores and t >= cores[k][0]:
            M.line(c, *P, *Q, cores[k][1], 1.0, 12, progress=ease_io(prog(t, cores[k][0], 0.5)))
    viz = {"A": (A, B, Cc), "B": (B, Cc, A), "C": (Cc, A, B)}
    for i, k in enumerate("ABC"):
        if angs[i] is None:
            continue
        V, P, Q = viz[k]
        cor = cores[k][1] if k in cores and t >= cores[k][0] else (CLARO if escuro else TINTA2)
        ti = (ta or {}).get(k, t0 + 1.0)
        E.angulo(c, t, ti, V, P, Q, angs[i], r=r_ang, cor=cor, size=size * 0.85)
    for i, (P, Q) in enumerate(((A, B), (B, Cc), (Cc, A))):
        if lados[i] is None:
            continue
        k = "CAB"[i]
        cor = cores[k][1] if k in cores and t >= cores[k][0] else (BR if escuro else TINTA)
        ti = (tl or {}).get(k, t0 + 1.0)
        E.foco(c, t, ti, 0.4, lambda a, P=P, Q=Q, s=lados[i], cor=cor: rot(c, P, Q, s, G, size, cor, a, 24))
    return G


def altura(c, t, t0, Cc, yb, a=1.0, cor=TINTA2):
    """altura tracejada do topo até a base, com o quadradinho no pé"""
    q = ep(t, t0, 0.6)
    if q <= 0:
        return
    Hp = (Cc[0], yb)
    M.line(c, *Cc, *Hp, cor, a, 5, dash=E.TRACO, progress=q)
    if q >= 0.9:
        s = 26
        M.line(c, Hp[0] + s, Hp[1], Hp[0] + s, Hp[1] - s, cor, a, 4)
        M.line(c, Hp[0], Hp[1] - s, Hp[0] + s, Hp[1] - s, cor, a, 4)


def por_lados(x0, y0, base, lat, g):
    """A = vértice do ângulo g; AB = base (deitado, para a direita); AC = lat, aberto g graus a partir de AB"""
    return (x0, y0), (x0 + base, y0), (x0 + lat * Cs(g), y0 - lat * S(g))


def por_tres(x0, y0, ab, bc, ca, k):
    """triângulo pelos três lados: AB deitado embaixo, C em cima"""
    x = (ca * ca - bc * bc + ab * ab) / (2 * ab)
    y = math.sqrt(ca * ca - x * x)
    return (x0, y0), (x0 + ab * k, y0), (x0 + x * k, y0 - y * k)


def mini(c, cx, cy, s, tipo, a=1.0, escuro=False):
    """ícone de triângulo: "par" (um lado e o ângulo de frente), "lal" (dois lados e o ângulo entre eles), "lll" (três lados),
    "aa" (dois ângulos e o lado entre eles)"""
    tinta = BR if escuro else TINTA
    A, B, Cc = (cx - s, cy + s * 0.55), (cx + s, cy + s * 0.55), (cx - s * 0.25, cy - s * 0.75)
    path = skia.Path(); path.addPoly([A, B, Cc], True)
    c.drawPath(path, M.paint(E.COR, 0.08 * a))
    c.drawPath(path, M.paint(tinta, a, stroke=4))
    cor = "#F2B33D" if escuro else AMBAR

    def arco(V, P, Q):
        a1 = math.degrees(math.atan2(P[1] - V[1], P[0] - V[0]))
        a2 = math.degrees(math.atan2(Q[1] - V[1], Q[0] - V[0]))
        varre = (a2 - a1 + 180) % 360 - 180
        r = s * 0.32
        c.drawArc(skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r), a1, varre, False, M.paint(cor, a, stroke=7))
    if tipo == "par":
        M.line(c, *B, *Cc, cor, a, 9)
        arco(A, B, Cc)
    elif tipo == "lal":
        M.line(c, *A, *B, cor, a, 9); M.line(c, *A, *Cc, cor, a, 9)
        arco(A, B, Cc)
    elif tipo == "lll":
        for P, Q in ((A, B), (B, Cc), (Cc, A)):
            M.line(c, *P, *Q, cor, a, 9)
    elif tipo == "aa":
        M.line(c, *A, *B, cor, a, 9)
        arco(A, B, Cc); arco(B, Cc, A)


def lago(c, A, B, a=1.0):
    """a mancha de água entre A e B"""
    mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    ang = math.degrees(math.atan2(B[1] - A[1], B[0] - A[0]))
    L = math.dist(A, B)
    c.save(); c.translate(mx, my - 40); c.rotate(ang)
    p = skia.Path()
    p.addOval(skia.Rect.MakeXYWH(-L * 0.42, -110, L * 0.84, 200))
    c.drawPath(p, M.paint(AGUA, 0.22 * a))
    c.drawPath(p, M.paint(AGUA, 0.6 * a, stroke=4))
    for i in range(3):
        y = -50 + i * 45
        M.line(c, -L * 0.2 + i * 30, y, -L * 0.05 + i * 30, y, AGUA, 0.6 * a, 4)
    c.restore()


def ponto(c, P, s, a=1.0, cor=TINTA, dx=0, dy=-30):
    c.drawCircle(*P, 14, M.paint(cor, a))
    E.escreve(c, s, P[0] + dx, P[1] + dy, 60, "g", cor, a)


# lago: C embaixo, A em cima à esquerda (80), B em cima à direita (50), 60° em C
LK = 6.0


def pontos_lago(cx, cy, k=LK):
    Cc = (cx, cy)
    A = (cx + 80 * k * Cs(120), cy - 80 * k * S(120))
    B = (cx + 50 * k * Cs(60), cy - 50 * k * S(60))
    return A, B, Cc


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        A, B, Cc = pontos_lago(900, 900)
        E.foco(c, t, a1, 0.6, lambda a: (lago(c, A, B, a), ponto(c, A, "A", a, dx=-60), ponto(c, B, "B", a, dx=20)))
        if t >= b1:
            q = ep(t, b1, 0.6)
            M.line(c, *Cc, *A, PAR1, 1.0, 10, progress=q, dash=None)
            M.line(c, *Cc, *B, PAR1, 1.0, 10, progress=ep(t, b1 + 0.4, 0.6))
            E.foco(c, t, b1, 0.4, lambda a: ponto(c, Cc, "C", a, dx=-20, dy=80))
        if t >= c1:
            E.angulo(c, t, c1, Cc, A, B, None, r=70, cor=PAR2)
        q = ep(t, d1 - 0.4, 0.6)
        if q > 0:
            M.line(c, *A, *B, PAR2, q, 8, dash=[20, 14])
            E.escreve(c, "?", (A[0] + B[0]) / 2 - 10, (A[1] + B[1]) / 2 - 60, 90, "g", PAR2, q)
        E.frase(c, t, d1, [("senos", "g", 76, COR)] + ps("ou", "i", 70) + [("cossenos?", "g", 76, COR)], 1400, 520, "center", 0.1)
        E.frase(c, t, d1 + 1.4, ps("escolher a lei é", "i", 56, TINTA2) + [("metade da questão", "g", 58)], 1400, 640, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, ta + 1.2, [("a lei", "g", 130), ("certa", "g", 130, COR)], XE, 480, "left", 0.14)
        E.frase(c, t, tb, [("+ atalho:", "g", 70, COR)] + ps("tem ângulo obtuso?", "i", 70), XE, 680, "left", 0.12)
        E.frase(c, t, tb + 1.5, ps("só pelos lados", "i", 70, TINTA2), XE, 790, "left", 0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + E.larg("2", "g", 340) + 30, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, 200, w, 300, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("lei dos senos", "i", 60)], x + 44, 290)
    E.foco(c, t, C["s03.b"] + 0.4, 0.5, lambda a: lei(c, [("a", "A", PAR1), ("b", "B", PAR2), ("c", "C", PAR3)], x + 44, 420, 84, a))
    p = ep(t, C["s03.c"], 0.5)
    E.caixa_pontilhada(c, x, 560, w, 240, p, prog_=p)
    E.frase(c, t, C["s03.c"] + 0.1, [("lei dos cossenos", "i", 60)], x + 44, 650)
    E.foco(c, t, C["s03.c"] + 0.4, 0.5, lambda a: cf(c, [("a^2", PAR2), (" = b^2 + c^2 − 2bc · ", TINTA), ("cos A", PAR2)], x + 44, 750, 64, a))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 900, 960, "left", 0.12)


# ---------------- a decisão ----------------
def b_decide(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5 = (C[f"s05.{k}"] for k in "abc")
    a6, b6, c6 = (C[f"s06.{k}"] for k in "abc")
    E.foco(c, t, a4, 0.5, lambda a: E.pilula(c, "tem um par completo?", W / 2, 200, 66, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, a4 + 1.0, 0.5, lambda a: mini(c, W / 2, 350, 75, "par", a))
    E.foco(c, t, a4 + 1.0, 0.5, lambda a: E.escreve(c, "lado + ângulo de frente", W / 2 + 110, 380, 44, "i", TINTA2, a))
    xs, xc = 480, 1440
    for x, t0, txt, cor in ((xs, b4, "sim", CERTO), (xc, a5, "não", ERRADO)):
        q = ep(t, t0, 0.5)
        if q > 0:
            M.arrow(c, W / 2 + (x - W / 2) * 0.15, 440, x, 520, cor, q, 5, 18, q)
            E.escreve(c, txt, (W / 2 + x) / 2 + (-60 if x < W / 2 else 20), 470, 50, "g", cor, q)
    E.foco(c, t, b4, 0.5, lambda a: E.pilula(c, "lei dos senos", xs, 590, 64, "g", fundo=PAR1, a=a))
    E.foco(c, t, a5, 0.5, lambda a: E.pilula(c, "lei dos cossenos", xc, 590, 64, "g", fundo=PAR2, a=a))
    E.foco(c, t, b5, 0.5, lambda a: (mini(c, xc - 200, 750, 85, "lal", a), centro(c, "2 lados e o", xc - 200, 880, 46, "i", TINTA, a),
                                      centro(c, "ângulo entre eles", xc - 200, 935, 46, "g", TINTA, a)))
    E.foco(c, t, c5, 0.5, lambda a: (mini(c, xc + 200, 750, 85, "lll", a), centro(c, "os 3 lados", xc + 200, 880, 46, "g", TINTA, a)))
    E.foco(c, t, a6, 0.5, lambda a: (mini(c, xs, 750, 85, "aa", a), centro(c, "2 ângulos e 1 lado", xs, 880, 46, "i", TINTA, a)))
    E.foco(c, t, b6, 0.5, lambda a: centro(c, "o 3º ângulo: 180° − os outros", xs, 940, 46, "g", COR, a))
    E.foco(c, t, c6, 0.5, lambda a: centro(c, "apareceu o par: senos", xs, 1005, 50, "g", CERTO, a))
    if t >= c6:
        q = ep(t, c6, 0.5)
        M.arrow(c, xs + 140, 700, xs + 140, 640, CERTO, q, 5, 16, q)


# ---------------- o lago ----------------
def b_lago(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8, d8, e8, f8 = (C[f"s08.{k}"] for k in "abcdef")
    A, B, Cc = pontos_lago(560, 960, 6.6)
    E.foco(c, t, C["s07"], 0.6, lambda a: (lago(c, A, B, a), ponto(c, A, "A", a, dx=-60), ponto(c, B, "B", a, dx=20),
                                           ponto(c, Cc, "C", a, dx=-20, dy=80)))
    tri(c, t, C["s07"] + 0.2, A, B, Cc, (None, None, "60°"), ("70 m" if t >= f8 else "?", "50 m", "80 m"),
        ta={"C": c7}, tl={"C": d7, "A": b7, "B": a7}, cores={"C": (c7, PAR2)}, size=58, r_ang=64)
    for P, Q, t0 in ((Cc, A, a7), (Cc, B, b7)):
        q = ep(t, t0, 0.5)
        if q > 0:
            M.line(c, *P, *Q, PAR1, 1.0, 10, progress=q)
    X = 1440
    E.frase(c, t, d7, [("LAL:", "g", 62, COR)] + ps("nenhum par completo", "i", 56), X, 200, "center", 0.1)
    E.foco(c, t, d7 + 1.4, 0.5, lambda a: E.pilula(c, "lei dos cossenos", X, 300, 56, "g", fundo=PAR2, a=a))
    E.frase(c, t, a8, [("60°:", "g", 60, PAR2), ("− bc", "g", 64, AMBAR)], X, 430, "center", 0.1)
    cf_em(c, t, b8, [("80^2 = 6.400", TINTA2)], X, 540, 62, "center")
    cf_em(c, t, c8, [("50^2 = 2.500", TINTA2)], X, 630, 62, "center")
    cf_em(c, t, d8, [("80 · 50 = 4.000", TINTA2)], X, 720, 62, "center")
    cf_em(c, t, e8, [("6.400 + 2.500 − 4.000 = 4.900", TINTA)], X, 830, 52, "center")
    resp(c, t, f8, [("r{4.900} = 70 m", BR)], X, 960, 66, cor=PAR2)


# ---------------- três lados: tem obtuso? ----------------
def b_lados(c, t, C, b):
    a9, b9, c9 = (C[f"s09.{k}"] for k in "abc")
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    A, B, Cc = por_tres(200, 820, 7, 5, 4, 100)
    tri(c, t, a9 - 0.3, A, B, Cc, (None, None, "?" if t < d0 else "> 90°"), ("7", "5", "4"), ta={"C": b9}, tl={"A": a9, "B": a9, "C": a9},
        cores={"C": (b9, PAR2)}, size=64, r_ang=60)
    X = 1380
    E.frase(c, t, b9, ps("maior lado", "i", 56) + [("→", "b", 56), ("maior ângulo", "g", 60, PAR2)], X, 220, "center", 0.1)
    cf_em(c, t, c9, [("7^2", PAR2), (" = 4^2 + 5^2 − ajuste", TINTA)], X, 360, 70, "center")
    cf_em(c, t, a0, [("49 = 41 − ajuste", TINTA)], X, 500, 70, "center")
    E.frase(c, t, b0, ps("o ajuste", "i", 58) + [("soma 8", "g", 64, COR)], X, 630, "center", 0.1)
    E.frase(c, t, c0, [("cos < 0", "g", 64, ERRADO)], X, 750, "center", 0.1)
    E.frase(c, t, d0, [("→ ângulo > 90°", "g", 64, PAR2)], X, 850, "center", 0.1)
    resp(c, t, e0, "obtusângulo", X, 970, 64, cor=PAR2)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    A, B, Cc = pontos_lago(560, 960, 6.6)
    E.foco(c, t, C["s11"], 0.6, lambda a: (lago(c, A, B, a), ponto(c, A, "A", a, dx=-60), ponto(c, B, "B", a, dx=20),
                                           ponto(c, Cc, "C", a, dx=-20, dy=80)))
    tri(c, t, C["s11"] + 0.2, A, B, Cc, ("?", "?", "60°"), ("?", "50 m", "80 m"), ta={"A": b1 + 0.6, "B": b1 + 0.6, "C": C["s11"] + 0.2},
        size=58, r_ang=60)
    E.frase(c, t, a1, ps("o erro:", "i", 60) + [("senos sem par completo", "g", 62, ERRADO)], W / 2, 170, "center", 0.1)
    E.foco(c, t, b1, 0.5, lambda a: cf(c, [("f{80}{sen ?}", ERRADO), (" = ", TINTA), ("f{50}{sen ?}", ERRADO)], 1440, 450, 100, a, "center"))
    E.frase(c, t, c1, ps("que ângulo?", "i", 62) + [("ninguém sabe", "g", 66, ERRADO)], 1440, 640, "center", 0.1)
    E.foco(c, t, c1 + 0.8, 0.5, lambda a: E.selo(c, 1440, 760, 46, False, a))
    E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "sem par completo: cossenos", 1440, 900, 54, "g", fundo=PAR2, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    a3, b3 = C["s13.a"], C["s13.b"]
    CL2 = "#F2B33D"

    def doze():
        E.frase(c, t, C["s12"] + 0.1, ps("agora o atalho", "i", 62, CLARO), W / 2, 160, "center", 0.1)
        E.foco(c, t, a2, 0.5, lambda a: cf(c, [("(maior lado)^2", CL2), ("  vs  ", CLARO), ("soma dos quadrados dos outros", BR)], W / 2, 300, 64, a, "center"))
        linhas = ((b2, ">", "obtusângulo", "7² = 49 > 41"), (c2, "=", "retângulo", "5² = 25 = 9 + 16"), (d2, "<", "acutângulo", "6² = 36 < 25 + 25"))
        for i, (t0, sg, nome, ex) in enumerate(linhas):
            y = 480 + i * 160
            E.foco(c, t, t0, 0.5, lambda a, sg=sg, nome=nome, ex=ex, y=y: (
                E.bola(c, 420, y - 24, 56, a=a), centro(c, sg, 420, y + 4, 70, "g", BR, a),
                E.escreve(c, nome, 520, y, 72, "g", BR, a), E.escreve(c, ex, 1180, y, 54, "b", CLARO, a)))
    E.saida(c, t, C["s13"] - 0.1, doze)
    if t < C["s13"] - 0.1:
        return
    E.frase(c, t, a3, ps("a diferença é o", "i", 66, CLARO) + [("ajuste", "g", 72, BR)], W / 2, 300, "center", 0.1)
    E.frase(c, t, a3 + 1.6, ps("o sinal dela é o", "i", 66, CLARO) + [("sinal do cosseno", "g", 72, BR)], W / 2, 410, "center", 0.1)
    E.foco(c, t, b3, 0.5, lambda a: E.pilula(c, "só com o MAIOR lado", W / 2, 620, 64, "g", fundo=E.COR, a=a))
    E.frase(c, t, b3 + 1.4, ps("com um lado menor, o teste sempre dá agudo", "i", 56, CLARO), W / 2, 780, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 170)

    def um():
        A, B, Cc = por_tres(200, 760, 11, 8, 6, 58)
        tri(c, t, a4 - 0.3, A, B, Cc, (None, None, "?"), ("11", "8", "6"), ta={"C": b4}, tl={"A": a4, "B": a4, "C": a4}, size=60, r_ang=56)
    um()
    E.frase(c, t, a4, ps("lados", "i", 62) + [("6, 8 e 11 m", "g", 68, COR)], 1000, 300, "left", 0.1)
    E.frase(c, t, b4, ps("tem ângulo", "i", 62) + [("obtuso?", "g", 68, PAR2)], 1000, 410, "left", 0.1)
    E.foco(c, t, c4, 0.5, lambda a: mini(c, 1060, 530, 50, "aa", a))
    E.frase(c, t, c4, ps("2 ângulos e o lado entre eles:", "i", 52), 1140, 550, "left", 0.08)
    E.frase(c, t, d4, ps("que", "i", 62) + [("lei?", "g", 68, COR)], 1140, 640, "left", 0.1)
    E.relogio(c, t, C["s15.a"], 1600, 820, 100)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    a7, b7, c7 = (C[f"s17.{k}"] for k in "abc")
    A, B, Cc = por_tres(200, 700, 11, 8, 6, 52)
    tri(c, t, C["s16"] - 0.3, A, B, Cc, (None, None, "> 90°" if t >= d6 else "?"), ("11", "8", "6"), ta={"C": C["s16"]},
        tl={"A": C["s16"], "B": C["s16"], "C": C["s16"]}, cores={"C": (a6, PAR2)}, size=56, r_ang=52)
    E.frase(c, t, C["s16"] + 0.1, ps("vamos lá", "i", 62, COR), XE, 170, "left", 0.1)
    X = 1380
    cf_em(c, t, a6, [("11^2 = 121", PAR2)], X, 250, 72, "center")
    cf_em(c, t, b6, [("6^2 + 8^2 = 36 + 64 = 100", TINTA)], X, 370, 64, "center")
    cf_em(c, t, c6, [("121 > 100", TINTA)], X, 490, 76, "center")
    resp(c, t, d6, "tem ângulo obtuso", X, 610, 58, cor=PAR2)
    E.foco(c, t, a7, 0.5, lambda a: mini(c, 360, 900, 60, "aa", a))
    E.frase(c, t, a7, ps("2 ângulos", "i", 56) + [("→", "b", 56), ("o 3º: 180° − os dois", "g", 58, COR)], 480, 900, "left", 0.1)
    E.frase(c, t, b7, ps("o lado ganha o ângulo de frente:", "i", 56) + [("par", "g", 60, CERTO)], 480, 990, "left", 0.1)
    resp(c, t, c7, "lei dos senos", X, 780, 58, cor=PAR1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"] + 0.1, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.foco(c, t, C["s18.a"], 0.5, lambda a: (mini(c, 360, 400, 70, "par", a), E.pilula(c, "senos", 640, 410, 64, "g", fundo=PAR1, a=a)))
        E.foco(c, t, C["s18.b"], 0.5, lambda a: (mini(c, 1060, 400, 70, "lal", a), mini(c, 1260, 400, 70, "lll", a),
                                                 E.pilula(c, "cossenos", 1560, 410, 64, "g", fundo=PAR2, a=a)))
        E.foco(c, t, C["s18.c"], 0.5, lambda a: cf(c, [("(maior lado)^2", PAR2), ("  vs  soma dos quadrados dos outros", TINTA)], W / 2, 720, 64, a, "center"))
        E.frase(c, t, C["s18.c"] + 1.0, ps("diz se tem", "i", 60) + [("ângulo obtuso", "g", 64, PAR2)], W / 2, 840, "center", 0.1)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"] - 0.1:
        return
    a9, b9, c9, d9, e9 = (C[f"s19.{k}"] for k in "abcde")
    E.frase(c, t, C["s19"], ps("na próxima aula", "i", 72), XE, 210, "left", 0.1)
    E.frase(c, t, a9, [("sec, cossec, cotg", "g", 100, COR)], XE, 380, "left", 0.1)
    E.frase(c, t, b9, ps("simplificar", "i", 64) + [("expressões", "g", 68)], XE, 530, "left", 0.1)
    E.foco(c, t, c9, 0.5, lambda a: E.formula(c, "f{1 − cos^2 x}{sen x} = sen x", XE, 720, 90, "g", TINTA, a))
    E.foco(c, t, d9, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 400, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d9 + 0.3, 0.8))
    E.cursor(c, lerp(1850, 1650, p), lerp(640, 425, p), ep(t, d9 + 0.2, 0.4))
    E.frase(c, t, e9, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, decide=b_decide, lago=b_lago, lados=b_lados, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
