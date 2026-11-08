"""Visual — Estudativo · MAT-TRA-002: lei dos cossenos (lados 3 e 5 com 120° → x² = 34 + 15 = 49 → 7; erro com cos 120° = +1/2 → √19;
atalho 60° → −bc e 120° → +bc; questão 5 e 8 com 60° → 49 → 7).
Linguagem da Trigonometria Avançada (MAT-TRA-001): o PAR (lado + ângulo de frente) numa cor só. Aqui o par da incógnita é o
ângulo dado e o lado que se quer, em âmbar (PAR2); os dois lados conhecidos, que formam o ângulo, em índigo (PAR1).
A dobradiça (bloco "ajuste"): os lados 3 e 5 ficam fixos e o ângulo entre eles abre e fecha; o terceiro lado é medido de verdade,
x = √(34 − 30 cos θ), com a régua do Pitágoras (√34) tracejada para comparar. A figura não mente: os triângulos 3-5-7 (120°) e
5-8-7 (60°) estão em escala.
Peças locais: as de MAT-TRA-001 (tri(), rot(), fra(), lei(), resp(), lista()) e dobradica().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria Avançada")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRA-002_lei_dos_cossenos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("regra", "ajuste", "conta", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
PAR1, PAR2, PAR3 = E.COR, AMBAR, "#C0187C"
S = lambda g: math.sin(math.radians(g))
Cs = lambda g: math.cos(math.radians(g))
lado3 = lambda b, c, g: math.sqrt(b * b + c * c - 2 * b * c * Cs(g))
assert abs(lado3(3, 5, 120) - 7) < 1e-9 and 9 + 25 == 34 and 2 * 3 * 5 == 30 and 34 + 15 == 49 and 34 - 15 == 19
assert abs(lado3(5, 8, 60) - 7) < 1e-9 and 25 + 64 - 40 == 49 and math.sqrt(89) > 9 and 5.8 < math.sqrt(34) < 5.9 and 4 < math.sqrt(19) < 4.5


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
    A = (x0, y0)
    B = (x0 + base, y0)
    Cc = (x0 + lat * Cs(g), y0 - lat * S(g))
    return A, B, Cc


def tri_lal(c, t, t0, A, B, Cc, ab, ca, bc, g, tl=None, tg=None, tx=None, size=60, r_ang=70, dados=True):
    """triângulo LAL: AB e CA conhecidos (índigo), ângulo em A e o lado BC de frente para ele (âmbar)"""
    tl = tl if tl is not None else t0 + 0.8
    tg = tg if tg is not None else t0 + 0.8
    tx = tx if tx is not None else t0 + 0.8
    tri(c, t, t0, A, B, Cc, (g, None, None), (ab, bc, ca), ta={"A": tg}, tl={"C": tl, "A": tx, "B": tl},
        cores={"A": (tx, PAR2)}, size=size, r_ang=r_ang)
    if dados:
        q = ep(t, tl, 0.5)
        if q > 0:
            M.line(c, *A, *B, PAR1, 1.0, 10, progress=q)
            M.line(c, *A, *Cc, PAR1, 1.0, 10, progress=q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        A, B, Cc = por_lados(760, 760, 5 * 110, 3 * 110, 120)
        tri_lal(c, t, a1, A, B, Cc, "5", "3", "?", "120°", tl=a1 + 0.6, tg=b1, tx=c1, size=72, r_ang=80)
        E.frase(c, t, d1, ps("lei dos senos?", "i", 60, TINTA2) + [("nenhum par completo", "g", 64, ERRADO)], W / 2, 960, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, ta + 1.2, [("lei dos", "g", 130), ("cossenos", "g", 130, COR)], XE, 500, "left", 0.14)
        E.frase(c, t, ta + 2.0, ps("para o terceiro lado", "i", 84), XE, 650, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 545, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 630, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + E.larg("3", "g", 340) + 30, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "o teorema de", "Pitágoras"),
             ("s03.c", "o cosseno:", "adjacente ÷ hipotenusa"),
             ("s03.d", "acima de 90°, negativo:", "cos 120° = −f{1}{2}"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, l2=l2, y=y: E.formula(c, l2, x + 44, y + 166, 62, "g", COR, a))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 900, 1000, "left", 0.12)


# ---------------- a regra ----------------
FORMULA = [("a^2", PAR2), (" = ", TINTA), ("b^2 + c^2", PAR1), (" − 2bc · ", TINTA), ("cos A", PAR2)]


def b_regra(c, t, C, b):
    a4, b4, c4 = (C[f"s04.{k}"] for k in "abc")
    a5, b5, c5 = (C[f"s05.{k}"] for k in "abc")
    E.frase(c, t, a4, [("Pitágoras", "g", 90, COR)] + ps("com um", "i", 84) + [("ajuste", "g", 90)], W / 2, 220, "center", 0.12)

    def palavras():
        E.frase(c, t, a4 + 1.6, ps("lado de frente ao ângulo, ao quadrado =", "i", 56), W / 2, 380, "center", 0.08)
        E.frase(c, t, b4, ps("soma dos quadrados dos outros dois", "g", 58, PAR1), W / 2, 480, "center", 0.08)
        E.frase(c, t, c4, ps("− 2 × os dois lados × cos do ângulo entre eles", "g", 54), W / 2, 580, "center", 0.08)
    E.saida(c, t, a5 - 0.1, palavras)
    if t >= a5 - 0.1:
        cf_em(c, t, a5, FORMULA, W / 2, 470, 110, "center")
    A, B, Cc = por_lados(560, 930, 520, 300, 70)
    if t >= b5 - 0.4:
        tri(c, t, b5 - 0.4, A, B, Cc, ("A", None, None), ("c", "a", "b"), ta={"A": b5}, tl={"A": b5, "B": c5, "C": c5},
            cores={"A": (b5, PAR2)}, size=60, r_ang=64)
        q = ep(t, c5, 0.5)
        if q > 0:
            M.line(c, *A, *B, PAR1, 1.0, 10, progress=q)
            M.line(c, *A, *Cc, PAR1, 1.0, 10, progress=q)
    E.frase(c, t, b5, [("a:", "g", 60, PAR2)] + ps("de frente para o ângulo A", "i", 56), 1180, 760, "left", 0.1)
    E.frase(c, t, c5, [("b e c:", "g", 60, PAR1)] + ps("formam o ângulo", "i", 56), 1180, 870, "left", 0.1)


# ---------------- o ajuste: a dobradiça ----------------
def dobradica(c, g, x0, y0, k, a=1.0):
    A, B, Cc = por_lados(x0, y0, 5 * k, 3 * k, g)
    path = skia.Path(); path.addPoly([A, B, Cc], True)
    c.drawPath(path, M.paint(E.COR, 0.06 * a))
    M.line(c, *B, *Cc, PAR2, a, 12)
    M.line(c, *A, *B, PAR1, a, 10)
    M.line(c, *A, *Cc, PAR1, a, 10)
    for P in (A, B, Cc):
        c.drawCircle(*P, 10, M.paint(TINTA, a))
    E.angulo(c, 1e9, 0, A, B, Cc, f"{round(g)}°", r=70, cor=PAR2, size=54)
    x = lado3(5, 3, g)
    rot(c, B, Cc, f"{x:.1f}".replace(".", ","), ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3), 64, PAR2, a, 24)
    rot(c, A, B, "5", ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3), 56, PAR1, a, 20)
    rot(c, A, Cc, "3", ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3), 56, PAR1, a, 20)
    return A, B, Cc


def b_ajuste(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    # o ângulo: 90 no começo, fecha até 60 em c6, abre até 120 em d6
    g = 90
    g = lerp(g, 60, ease_io(prog(t, c6, 1.6)))
    g = lerp(g, 120, ease_io(prog(t, d6, 2.2)))
    x0, y0, k = 760, 860, 105
    E.foco(c, t, C["s06"], 0.5, lambda a: dobradica(c, g, x0, y0, k, a))
    # régua do Pitágoras: √34 tracejado ao lado
    q = ep(t, b6, 0.5)
    if q > 0:
        kr = 80
        L = math.sqrt(34) * kr
        xr = 1560
        M.line(c, xr, y0, xr, y0 - L, TINTA2, q, 6, dash=E.TRACO)
        M.line(c, xr - 20, y0 - L, xr + 20, y0 - L, TINTA2, q, 6)
        E.escreve(c, "Pitágoras", xr + 40, y0 - L + 30, 46, "i", TINTA2, q)
        E.formula(c, "r{34} ≈ 5,8", xr + 40, y0 - L + 90, 50, "g", TINTA2, q)
        xa = lado3(5, 3, g) * kr
        M.line(c, xr - 50, y0, xr - 50, y0 - xa, PAR2, q, 12)
        E.escreve(c, "x", xr - 120, y0 - xa + 10, 54, "g", PAR2, q)
    E.frase(c, t, C["s06"] + 0.1, ps("por que um", "i", 66) + [("ajuste?", "g", 72, COR)], XE, 170, "left", 0.1)
    E.foco(c, t, a6, 0.5, lambda a: E.formula(c, "90°: cos = 0", XE, 300, 64, "g", TINTA, a * (1 - ep(t, c6, 0.4))))
    E.foco(c, t, b6, 0.5, lambda a: E.formula(c, "sobra o próprio Pitágoras", XE, 390, 56, "g", TINTA2, a * (1 - ep(t, c6, 0.4))))
    E.foco(c, t, c6, 0.5, lambda a: E.formula(c, "fechou: cos +, o lado encolhe", XE, 300, 58, "g", CERTO, a * (1 - ep(t, d6, 0.4))))
    E.foco(c, t, d6, 0.5, lambda a: E.formula(c, "abriu: cos −, o lado cresce", XE, 300, 58, "g", ERRADO, a))


# ---------------- a conta ----------------
def b_conta(c, t, C, b):
    a7, b7, c7 = (C[f"s07.{k}"] for k in "abc")
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    a9, b9 = (C[f"s09.{k}"] for k in "ab")
    A, B, Cc = por_lados(1420, 560, 5 * 80, 3 * 80, 120)
    tri_lal(c, t, C["s07"] - 0.3, A, B, Cc, "5", "3", "7" if t >= e8 else "x", "120°", tl=C["s07"], tg=C["s07"], tx=C["s07"], size=58, r_ang=66)
    cf_em(c, t, a7, [("x^2", PAR2), (" = 3^2 + 5^2 − 2 · 3 · 5 · ", TINTA), ("cos 120°", PAR2)], XE, 220, 72)
    cf_em(c, t, b7, [("9 + 25 = 34", TINTA2)], XE, 350, 64)
    cf_em(c, t, c7, [("2 · 3 · 5 = 30", TINTA2)], XE + 560, 350, 64)
    cf_em(c, t, a8, [("cos 120° = −f{1}{2}", PAR2)], XE, 490, 64)
    cf_em(c, t, b8, [("30 · (−f{1}{2}) = −15", TINTA2)], XE + 560, 490, 64)
    cf_em(c, t, c8, [("x^2", PAR2), (" = 34 − (−15)", TINTA)], XE, 660, 84)
    cf_em(c, t, d8, [("= 34 + 15 = 49", TINTA)], XE + 160, 790, 84)
    resp(c, t, e8, [("x = r{49} = 7", BR)], 1500, 760, 76, cor=PAR2)
    E.foco(c, t, a9, 0.5, lambda a: E.formula(c, "Pitágoras: r{34} ≈ 5,8", XE, 960, 60, "g", TINTA2, a))
    E.foco(c, t, b9, 0.5, lambda a: (E.formula(c, "7 > 5,8: o ângulo aberto esticou", 960, 960, 56, "g", CERTO, a),
                                      E.selo(c, 1840, 940, 34, True, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    E.frase(c, t, a0, ps("o erro:", "i", 62) + [("perder o sinal do cosseno", "g", 66, ERRADO)], W / 2, 190, "center", 0.1)
    cf_em(c, t, b0, [("cos 120° = +f{1}{2}", ERRADO)], W / 2, 380, 96, "center")
    if t >= b0 + 1.0:
        E.risco(c, W / 2 - 330, 410, W / 2 + 330, 310, t, b0 + 1.0, largura=10)
    cf_em(c, t, c0, [("34 − 15 = 19", ERRADO)], W / 2, 560, 96, "center")
    cf_em(c, t, d0, [("r{19} ≈ 4,4  <  r{34} ≈ 5,8", ERRADO)], W / 2, 730, 84, "center")
    E.frase(c, t, d0 + 1.4, ps("ângulo aberto e lado", "i", 60) + [("menor que o Pitágoras?", "g", 64, ERRADO)], W / 2, 860, "center", 0.1)
    E.foco(c, t, e0, 0.5, lambda a: E.selo(c, W / 2, 970, 50, False, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2 = (C[f"s12.{k}"] for k in "abc")
    CL2 = "#F2B33D"

    def onze():
        E.frase(c, t, C["s11"] + 0.1, ps("agora o atalho", "i", 62, CLARO), W / 2, 170, "center", 0.1)
        E.foco(c, t, a1, 0.5, lambda a: E.formula(c, "60°:  2 · f{1}{2} = 1", 300, 340, 80, "g", CLARO, a))
        E.foco(c, t, b1, 0.5, lambda a: cf(c, [("a^2 = b^2 + c^2 ", BR), ("− bc", CL2)], 300, 480, 100, a))
        E.foco(c, t, c1, 0.5, lambda a: E.formula(c, "120°:  2 · (−f{1}{2}) = −1", 300, 680, 80, "g", CLARO, a))
        E.foco(c, t, d1, 0.5, lambda a: cf(c, [("a^2 = b^2 + c^2 ", BR), ("+ bc", CL2)], 300, 820, 100, a))
    E.saida(c, t, C["s12"] - 0.1, onze)
    if t < C["s12"] - 0.1:
        return
    E.frase(c, t, C["s12"], ps("no exemplo", "i", 62, CLARO), W / 2, 200, "center", 0.1)
    cf_em(c, t, a2, [("9 + 25 ", BR), ("+ 3 · 5", CL2), (" = 49", BR)], W / 2, 380, 110, "center")
    E.frase(c, t, a2 + 1.8, ps("sem fração nenhuma", "i", 60, CLARO), W / 2, 490, "center", 0.1)
    E.foco(c, t, b2, 0.5, lambda a: cf(c, [("o 2 da fórmula cancela o ", CLARO), ("f{1}{2}", BR), (" do cosseno", CLARO)], W / 2, 680, 64, a, "center"))
    E.foco(c, t, c2, 0.5, lambda a: E.pilula(c, "45° e outros: a fórmula inteira", W / 2, 880, 58, "g", fundo=E.COR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a3, b3, c3 = (C[f"s13.{k}"] for k in "abc")
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 170)
    A, B, Cc = por_lados(200, 820, 8 * 80, 5 * 80, 60)
    tri_lal(c, t, a3 - 0.3, A, B, Cc, "8", "5", "?", "60°", tl=a3, tg=b3, tx=c3, size=64, r_ang=70)
    E.frase(c, t, a3, ps("lados", "i", 64) + [("5 e 8", "g", 70, PAR1)], 1080, 330, "left", 0.1)
    E.frase(c, t, b3, [("60°", "g", 70, PAR2)] + ps("entre eles", "i", 64), 1080, 450, "left", 0.1)
    E.frase(c, t, c3, ps("terceiro lado?", "i", 64), 1080, 570, "left", 0.1)
    E.relogio(c, t, C["s14.a"], 1560, 760, 130)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    a6, b6 = (C[f"s16.{k}"] for k in "ab")
    A, B, Cc = por_lados(1180, 520, 8 * 55, 5 * 55, 60)
    tri_lal(c, t, C["s15"] - 0.3, A, B, Cc, "8", "5", "7" if t >= e5 else "?", "60°", tl=C["s15"], tg=C["s15"], tx=C["s15"], size=54, r_ang=56)
    E.frase(c, t, C["s15"] + 0.1, ps("vamos lá", "i", 62, COR), XE, 170, "left", 0.1)
    E.frase(c, t, a5, [("60°:", "g", 66, PAR2), ("− bc", "g", 70, AMBAR)], XE, 320, "left", 0.1)
    cf_em(c, t, b5, [("25 + 64 = 89", TINTA)], XE, 470, 80)
    cf_em(c, t, c5, [("89 − 5 · 8 = 89 − 40", TINTA)], XE, 610, 80)
    cf_em(c, t, d5, [("= 49", TINTA)], XE + 300, 740, 80)
    resp(c, t, e5, [("x = r{49} = 7", BR)], 1400, 760, 76, cor=PAR2)
    E.foco(c, t, a6, 0.5, lambda a: E.formula(c, "Pitágoras: r{89} > 9", XE, 940, 60, "g", TINTA2, a))
    E.foco(c, t, b6, 0.5, lambda a: (E.formula(c, "7 < 9: o ângulo fechado encolheu", 960, 940, 54, "g", CERTO, a),
                                      E.selo(c, 1840, 920, 34, True, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"] + 0.1, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        cf_em(c, t, C["s17.a"], FORMULA, W / 2, 420, 100, "center")
        lista(c, t, [(C["s17.a"] + 0.6, [("Pitágoras", "g", 64, COR)] + ps("com um ajuste", "i", 60)),
                     (C["s17.b"], ps("o ajuste:", "i", 60) + [("− 2bc · cos", "g", 64)]),
                     (C["s17.c"], ps("o", "i", 60) + [("sinal do cosseno", "g", 64, COR)] + ps("decide se cresce ou encolhe", "i", 60))], 200, 620, 150, 60)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"] - 0.1:
        return
    a8, b8, c8, d8, e8 = (C[f"s18.{k}"] for k in "abcde")
    E.frase(c, t, C["s18"], ps("na próxima aula", "i", 72), XE, 210, "left", 0.1)
    E.frase(c, t, a8, [("qual lei usar?", "g", 110, COR)], XE, 380, "left", 0.1)
    E.frase(c, t, b8, ps("a distância", "i", 62) + [("do outro lado do lago", "g", 64)], XE, 540, "left", 0.1)
    E.frase(c, t, c8, ps("só pelos lados:", "i", 62) + [("tem ângulo obtuso?", "g", 64)], XE, 670, "left", 0.1)
    E.foco(c, t, d8, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 370, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d8 + 0.3, 0.8))
    E.cursor(c, lerp(1850, 1650, p), lerp(610, 395, p), ep(t, d8 + 0.2, 0.4))
    E.frase(c, t, e8, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, regra=b_regra, ajuste=b_ajuste, conta=b_conta, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
