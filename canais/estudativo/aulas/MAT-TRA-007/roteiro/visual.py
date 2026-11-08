"""Visual — Estudativo · MAT-TRA-007: praticando leis, identidades e equações (6 e 10 com 120° → 14 m; 45° e 30° com 8 → 4√2 ≈ 5,6;
(sec² x − 1) · cos² x = sen² x; sen 15° = (√6 − √2)/4 ≈ 0,25; 2 sen x + √3 = 0 → 4π/3 e 5π/3).
Linguagem de cada parte, como nas aulas de origem: o PAR (lado + ângulo de frente) numa cor só, índigo o dado e âmbar o procurado
(MAT-TRA-001 a 003); seno em âmbar (OPO), cosseno em petróleo (ADJ), tangente em magenta (TG), como na MAT-TRA-004 e 005; a linha no
ciclo e os pontos onde ela corta (MAT-TRA-006). Fator que se corta leva o risco vermelho. Cada questão: título "questão n", a
pergunta e o relógio de pausa; resposta final na pílula. A figura não mente: os triângulos e os pontos do ciclo são os de verdade.
Peças locais: as de MAT-TRA-001 (tri(), rot(), fra(), lei(), resp(), lista(), pontos()) e as do ciclo da MAT-TRA-006 (ciclo(),
ponto(), linha_h()), mais por_lados(), titulo() e risco_em().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria Avançada")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRA-007_praticando_leis_identidades_e_equacoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
PAR1, PAR2, PAR3 = E.COR, AMBAR, "#C0187C"
OPO, ADJ, TG = "#D98A00", "#0E9AA7", "#C0187C"
S = lambda g: math.sin(math.radians(g))
Cs = lambda g: math.cos(math.radians(g))
assert 36 + 100 + 6 * 10 == 196 == 14 ** 2 and abs(math.sqrt(36 + 100 - 120 * Cs(120)) - 14) < 1e-9 and math.sqrt(136) < 12
assert abs(8 / S(45) - 8 * math.sqrt(2)) < 1e-9 and abs(8 / S(45) * S(30) - 4 * math.sqrt(2)) < 1e-9 and abs(4 * 1.4 - 5.6) < 1e-12
assert abs(S(15) - (math.sqrt(6) - math.sqrt(2)) / 4) < 1e-12 and abs((2.4 - 1.4) / 4 - 0.25) < 1e-12
assert abs(2 * S(240) + math.sqrt(3)) < 1e-12 and abs(2 * S(300) + math.sqrt(3)) < 1e-12 and 180 + 60 == 240 == 4 * 60 and 360 - 60 == 300 == 5 * 60


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


# ---------------- o ciclo (como na MAT-TRI-009) ----------------
def pt(cx, cy, r, ang):
    return cx + r * Cs(ang), cy - r * S(ang)


def ciclo(c, t, t0, cx, cy, r, escuro=False):
    if t < t0:
        return
    tinta = BR if escuro else TINTA
    q = ep(t, t0, 0.6)
    M.arrow(c, cx - r - 70, cy, cx + r + 90, cy, tinta, q, 4, 20, q)
    M.arrow(c, cx, cy + r + 70, cx, cy - r - 90, tinta, q, 4, 20, q)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -360 * ease_io(prog(t, t0 + 0.2, 0.9)), False, M.paint(tinta, 1.0, stroke=5))
    sec = CLARO if escuro else TINTA2
    E.foco(c, t, t0 + 0.6, 0.4, lambda a: (E.escreve(c, "cos", cx + r + 60, cy + 56, 44, "i", sec, a),
                                           E.escreve(c, "sen", cx + 22, cy - r - 66, 44, "i", sec, a)))


def ponto(c, t, t0, cx, cy, r, ang, rot=None, cor=None, escuro=False, fora=78, size=50, arco=False):
    k = ease_back(prog(t, t0, 0.4))
    if k <= 0:
        return
    cor = cor or (E.COR if not escuro else CLARO)
    if arco:
        c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -ang * ease_io(prog(t, t0, 0.7)), False, M.paint(cor, 0.85, stroke=8, cap_round=True))
    X, Y = pt(cx, cy, r, ang)
    c.drawCircle(X, Y, 16 * k, M.paint(cor))
    c.drawCircle(X, Y, 16 * k, M.paint(BR if not escuro else "#07070F", 1.0, stroke=3))
    if rot:
        Xr, Yr = pt(cx, cy, r + fora, ang)
        E.foco(c, t, t0 + 0.1, 0.4, lambda a: E.formula(c, rot, Xr, Yr + size * 0.36, size, "g", cor, a, "center"))


def linha_h(c, t, t0, cx, cy, r, v, cor=OPO, rot=None, a=1.0):
    """linha horizontal na altura v (seno = v), de borda a borda do ciclo"""
    q = ep(t, t0, 0.6) * a
    if q <= 0:
        return
    y = cy - r * v
    M.line(c, cx - r - 60, y, lerp(cx - r - 60, cx + r + 60, ease_io(prog(t, t0, 0.6))), y, cor, q, 5, dash=[20, 12])
    if rot:
        E.formula(c, rot, cx - r - 80, y + 18, 48, "g", cor, q, "right")


def linha_v(c, t, t0, cx, cy, r, v, cor=ADJ, rot=None, a=1.0):
    """linha vertical na horizontal v (cosseno = v)"""
    q = ep(t, t0, 0.6) * a
    if q <= 0:
        return
    x = cx + r * v
    M.line(c, x, cy + r + 60, x, lerp(cy + r + 60, cy - r - 60, ease_io(prog(t, t0, 0.6))), cor, q, 5, dash=[20, 12])
    if rot:
        E.formula(c, rot, x, cy + r + 110, 48, "g", cor, q, "center")


def arco_sol(c, t, t0, cx, cy, r, de, ate, cor=CERTO, a=1.0, larg=16):
    """o arco-solução, de `de` até `ate` graus, grosso por cima do ciclo"""
    q = ep(t, t0, 0.8) * a
    if q <= 0:
        return
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -de, -(ate - de) * ease_io(prog(t, t0, 0.8)), False, M.paint(cor, q, stroke=larg))


def aberta(c, cx, cy, r, ang, cor, a=1.0, cheia=False):
    X, Y = pt(cx, cy, r, ang)
    c.drawCircle(X, Y, 17, M.paint(cor if cheia else BR, a))
    c.drawCircle(X, Y, 17, M.paint(cor, a, stroke=6))


def por_lados(x0, y0, base, lat, g):
    """A = vértice do ângulo g; AB = base (deitado, para a direita); AC = lat, aberto g graus a partir de AB"""
    return (x0, y0), (x0 + base, y0), (x0 + lat * Cs(g), y0 - lat * S(g))


def titulo(c, t, t0, n, nome, x=XE, y=150):
    E.frase(c, t, t0, ps("questão", "i", 64, COR) + [(str(n), "g", 72, COR)] + ps(f"· {nome}", "i", 56, TINTA2), x, y, "left", 0.1)


def risco_em(c, t, t0, x, y, w, h=60, cor=ERRADO):
    if t >= t0:
        E.risco(c, x - w / 2, y + h * 0.35, x + w / 2, y - h * 0.65, t, t0, cor, 8)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]
    E.foco(c, t, a1, 0.5, lambda a: E.escreve(c, "5", XE - 8, 520, 340, "g", COR, a))
    E.foco(c, t, a1 + 0.15, 0.5, lambda a: E.escreve(c, "questões", XE + E.larg("5", "g", 340) + 30, 500, 110, "i", TINTA, a))
    nomes = (("lei dos senos", PAR1), ("lei dos cossenos", PAR2), ("identidades", TG), ("seno da diferença", OPO), ("equação no ciclo", ADJ))
    for i, (s, cor) in enumerate(nomes):
        x, y = 1120 + (i % 2) * 420, 230 + (i // 2) * 140
        if i == 4:
            x = 1330
        E.foco(c, t, lerp(a1 + 0.8, b1, 0.12 + 0.17 * i), 0.5, lambda a, s=s, x=x, y=y, cor=cor: E.pilula(c, s, x, y, 50, "g", fundo=cor, a=a))
    E.frase(c, t, b1, ps("em cada uma,", "i", 62) + [("pause e resolva", "g", 66, COR)], XE, 760, "left", 0.1)
    E.frase(c, t, b1 + 1.4, ps("antes de ver a resposta", "i", 62), XE, 860, "left", 0.1)
    E.frase(c, t, c1, ps("errar aqui", "i", 56, TINTA2) + [("não custa nada", "g", 58, CERTO)], XE, 990, "left", 0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    k = {x: C[f"s02.{x}"] for x in "abcde"}
    E.frase(c, t, C["s02"] + 0.1, ps("você vai usar", "i", 70, COR), XE, 180, "left", 0.1)
    lista(c, t, [(k["a"], ps("a", "i", 58) + [("lei dos senos", "g", 62, PAR1)] + ps("(par completo)", "i", 52, TINTA2)),
                 (k["b"], ps("a", "i", 58) + [("lei dos cossenos", "g", 62, PAR2)] + ps("(sem par)", "i", 52, TINTA2)),
                 (k["c"], ps("as", "i", 58) + [("identidades", "g", 62, TG)]),
                 (k["d"], ps("o", "i", 58) + [("seno da soma e da diferença", "g", 62, OPO)]),
                 (k["e"], ps("as", "i", 58) + [("equações no ciclo", "g", 62, ADJ)])], XE, 340, 135, 58)
    E.frase(c, t, C["s02.end"] - 2.4, ps("travou?", "i", 56, COR) + ps("procure a aula no canal", "i", 56), XE, 1010, "left", 0.12)


# ---------------- questão 1: lei dos cossenos ----------------
def tri_q1(c, t, t0, x0, y0, k, tl, tg, tx, txt_x="?", size=60):
    A, B, Cc = por_lados(x0, y0, 10 * k, 6 * k, 120)
    tri(c, t, t0, A, B, Cc, ("120°", None, None), ("10 m", txt_x, "6 m"), ta={"A": tg}, tl={"C": tl, "A": tx, "B": tl},
        cores={"A": (tx, PAR2)}, size=size, r_ang=64)
    q = ep(t, tl, 0.5)
    if q > 0:
        M.line(c, *A, *B, PAR1, 1.0, 10, progress=q)
        M.line(c, *A, *Cc, PAR1, 1.0, 10, progress=q)


def b_q1(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s03.{k}"] for k in "abcd")
    titulo(c, t, a3, 1, "o terreno")
    tri_q1(c, t, b3 - 0.3, 360, 780, 70, b3, c3, d3)
    E.frase(c, t, b3, ps("lados", "i", 62) + [("6 m e 10 m", "g", 68, PAR1)], 1180, 330, "left", 0.1)
    E.frase(c, t, c3, ps("entre eles,", "i", 62) + [("120°", "g", 68, PAR2)], 1180, 450, "left", 0.1)
    E.frase(c, t, d3, ps("terceiro lado?", "i", 62), 1180, 570, "left", 0.1)
    E.relogio(c, t, C["s04.a"], 1560, 780, 100)


def b_r1(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    a6, b6 = C["s06.a"], C["s06.b"]
    tri_q1(c, t, C["s05"] - 0.3, 1330, 430, 42, C["s05"], C["s05"], C["s05"], "14 m" if t >= e5 else "?", 52)
    E.frase(c, t, C["s05"] + 0.1, ps("vamos lá", "i", 62, COR), XE, 170, "left", 0.1)
    E.frase(c, t, a5, ps("sem par completo:", "i", 56) + [("cossenos", "g", 62, PAR2)], XE, 300, "left", 0.1)
    E.frase(c, t, b5, [("120°:", "g", 62, PAR2), ("+ bc", "g", 66, AMBAR)], XE, 420, "left", 0.1)
    cf_em(c, t, c5, [("x^2 = 36 + 100 + 6 · 10", TINTA)], XE, 560, 76)
    cf_em(c, t, d5, [("= 196", TINTA)], XE + 330, 680, 76)
    resp(c, t, e5, [("x = r{196} = 14 m", BR)], 1430, 760, 66, 2.0, cor=PAR2)
    E.foco(c, t, a6, 0.5, lambda a: E.formula(c, "Pitágoras: r{136} < 12", XE, 880, 60, "g", TINTA2, a))
    E.foco(c, t, b6, 0.5, lambda a: (E.formula(c, "14 > 12: o ângulo aberto esticou", XE, 990, 56, "g", CERTO, a),
                                      E.selo(c, 1060, 970, 34, True, a)))


# ---------------- questão 2: lei dos senos ----------------
def tri_q2(c, t, t0, x0, y0, base, tl, tx, txt_x="?", size=60):
    A, B, Cc = pontos(base, 45, 30, x0, y0)  # 45° em A (de frente: BC = 8), 30° em B (de frente: CA = ?)
    tri(c, t, t0, A, B, Cc, ("45°", "30°", None), (None, "8", txt_x), ta={"A": t0 + 0.5, "B": t0 + 0.8}, tl={"A": tl, "B": tx},
        cores={"A": (tl, PAR1), "B": (tx, PAR2)}, size=size, r_ang=64)


def b_q2(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    titulo(c, t, a7, 2, "dois ângulos e um lado")
    tri_q2(c, t, b7 - 0.3, 160, 800, 860, c7, d7)
    E.frase(c, t, b7, ps("ângulos", "i", 62) + [("45° e 30°", "g", 68, COR)], 1180, 330, "left", 0.1)
    E.frase(c, t, c7, ps("de frente para 45°:", "i", 58) + [("8", "g", 68, PAR1)], 1180, 450, "left", 0.1)
    E.frase(c, t, d7, ps("de frente para 30°:", "i", 58) + [("?", "g", 72, PAR2)], 1180, 570, "left", 0.1)
    E.relogio(c, t, C["s08.a"], 1560, 780, 100)


def b_r2(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a0, b0, c0 = (C[f"s10.{k}"] for k in "abc")
    tri_q2(c, t, C["s09"] - 0.3, 1130, 480, 620, C["s09"], C["s09"], "4r{2}" if t >= b0 else "?", 52)
    E.frase(c, t, a9, ps("par completo:", "i", 56) + [("senos", "g", 62, PAR1)], XE, 190, "left", 0.1)
    cf_em(c, t, b9, [("f{8}{sen 45°} = 8 ÷ f{r{2}}{2}", TINTA)], XE, 340, 72)
    cf_em(c, t, c9, [("= 8 · f{2}{r{2}} = f{16}{r{2}}", TINTA)], XE, 490, 72)
    cf_em(c, t, d9, [("= f{16r{2}}{2} = ", TINTA), ("8r{2}", PAR1)], XE, 640, 72)
    cf_em(c, t, a0, [("8r{2} · f{1}{2}", TINTA)], XE, 800, 76)
    resp(c, t, b0, [("4r{2} ≈ 4 · 1,4 = 5,6", BR)], 1430, 800, 70, 1.9, cor=PAR2)
    E.frase(c, t, c0, ps("ângulo menor,", "i", 56) + [("lado menor", "g", 60, CERTO)], 1430, 960, "center", 0.1)


# ---------------- questão 3: identidade ----------------
def b_q3(c, t, C, b):
    a1, b1, c1 = (C[f"s11.{k}"] for k in "abc")
    titulo(c, t, a1, 3, "identidade")
    E.frase(c, t, a1 + 0.6, ps("simplifique:", "i", 66), XE, 380, "left", 0.1)
    cf_em(c, t, b1, [("(sec^2 x − 1)", ADJ)], XE, 580, 110)
    cf_em(c, t, c1, [(" · cos^2 x", ADJ)], XE + cf(None, [("(sec^2 x − 1)", ADJ)], 0, 0, 110), 580, 110)
    E.relogio(c, t, C["s12.a"], 1560, 760, 100)


def b_r3(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    E.frase(c, t, C["s13"] + 0.1, ps("vamos lá", "i", 62, COR), XE, 170, "left", 0.1)
    cf_em(c, t, a3, [("sec^2 x = 1 + ", ADJ), ("tg^2 x", TG)], XE, 320, 80)
    cf_em(c, t, b3, [("sec^2 x − 1 = ", ADJ), ("tg^2 x", TG)], XE, 460, 80)
    sz, y = 100, 700
    partes = [("f{sen^2 x}{cos^2 x}", OPO), (" · cos^2 x", ADJ)]
    cf_em(c, t, c3, partes, XE, y, sz)
    if t >= d3:
        w1 = E.formula(None, "f{sen^2 x}{cos^2 x}", 0, 0, sz, "g", a=0)
        wc = E.formula(None, "cos^2 x", 0, 0, sz * 0.78, "g", a=0)
        risco_em(c, t, d3, XE + w1 / 2, y + sz * 0.46, wc + 10, 70)
        x2 = XE + w1 + E.formula(None, " · ", 0, 0, sz, "g", a=0)
        risco_em(c, t, d3 + 0.3, x2 + E.formula(None, "cos^2 x", 0, 0, sz, "g", a=0) / 2, y, E.formula(None, "cos^2 x", 0, 0, sz, "g", a=0) + 10, 80)
        E.foco(c, t, d3, 0.4, lambda a: E.escreve(c, "fator: corta", XE + 60, y + 180, 48, "g", CERTO, a))
    resp(c, t, e3, [("sen^2 x", BR)], 1450, 700, 96, 1.6, cor=OPO)


# ---------------- questão 4: seno da diferença ----------------
def b_q4(c, t, C, b):
    a4, b4, c4 = (C[f"s14.{k}"] for k in "abc")
    titulo(c, t, a4, 4, "seno da diferença")
    cf_em(c, t, b4, [("sen 15° = ?", OPO)], XE, 480, 130)
    cf_em(c, t, c4, [("use 45° e 30°", TINTA2)], XE, 700, 84)
    E.relogio(c, t, C["s15.a"], 1500, 440, 170)


def b_r4(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    a7, b7, c7 = (C[f"s17.{k}"] for k in "abc")
    cf_em(c, t, a6, [("sen 15° = sen(45° − 30°)", TINTA)], XE, 190, 80)
    cf_em(c, t, b6, [("sen 45°", OPO), (" · ", TINTA), ("cos 30°", ADJ)], XE, 340, 76)
    cf_em(c, t, c6, [(" − ", ERRADO), ("sen 30°", OPO), (" · ", TINTA), ("cos 45°", ADJ)],
          XE + cf(None, [("sen 45°", OPO), (" · ", TINTA), ("cos 30°", ADJ)], 0, 0, 76), 340, 76)
    cf_em(c, t, d6, [("= f{r{6}}{4} − f{r{2}}{4}", TINTA)], XE, 510, 84)
    resp(c, t, a7, [("sen 15° = f{r{6} − r{2}}{4}", BR)], W / 2, 700, 76, 2.3, cor=OPO)
    cf_em(c, t, b7, [("≈ f{2,4 − 1,4}{4}", TINTA2)], W / 2 - 200, 900, 72, "center")
    cf_em(c, t, c7, [("≈ 0,25", TINTA)], W / 2 + 200, 900, 84, "center")


# ---------------- questão 5: equação no ciclo ----------------
CX, CY, CR = 560, 580, 300


def b_q5(c, t, C, b):
    a8, b8, c8 = (C[f"s18.{k}"] for k in "abc")
    titulo(c, t, a8, 5, "equação no ciclo")
    cf_em(c, t, b8, [("2 ", TINTA), ("sen x", OPO), (" + r{3} = 0", TINTA)], XE, 480, 120)
    cf_em(c, t, c8, [("0 ≤ x ≤ 2π", TINTA2)], XE, 700, 90)
    E.relogio(c, t, C["s19.a"], 1500, 440, 170)


def b_r5(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")
    X = 1420
    ciclo(c, t, C["s20"] - 0.3, CX, CY, CR)
    if t >= c0:  # metade de baixo: seno negativo
        q = ep(t, c0, 0.5)
        c.save(); c.clipRect(skia.Rect.MakeLTRB(CX - CR - 10, CY, CX + CR + 10, CY + CR + 10))
        c.drawCircle(CX, CY, CR, M.paint(OPO, 0.10 * q)); c.restore()
    linha_h(c, t, d0, CX, CY, CR, -math.sqrt(3) / 2, rot="−f{r{3}}{2}")
    ponto(c, t, a1, CX, CY, CR, 240, "f{4π}{3}" if t >= b1 else "240°")
    ponto(c, t, c1, CX, CY, CR, 300, "f{5π}{3}" if t >= d1 else "300°")
    if t >= e1:
        X1, Y1 = pt(CX, CY, CR, 60)
        q = ep(t, e1, 0.4)
        c.drawCircle(X1, Y1, 16, M.paint(ERRADO, q))
        E.formula(c, "60°?", X1 + 30, Y1 - 20, 50, "g", ERRADO, q)
    cf_em(c, t, a0, [("sen x = −f{r{3}}{2}", OPO)], X, 220, 84, "center")
    cf_em(c, t, b0, [("sem o sinal: 60°", TINTA2)], X, 360, 64, "center")
    E.frase(c, t, c0, [("seno negativo:", "g", 58, ERRADO)] + ps("3º e 4º quadrantes", "i", 56), X, 470, "center", 0.1)
    cf_em(c, t, a1, [("180° + 60° = 240° → ", TINTA2), ("f{4π}{3}", COR)], X, 600, 60, "center")
    cf_em(c, t, c1, [("360° − 60° = 300° → ", TINTA2), ("f{5π}{3}", COR)], X, 730, 60, "center")
    resp(c, t, d1 + 0.6, [("S = {f{4π}{3}, f{5π}{3}}", BR)], X, 880, 64, 2.3, cor=OPO)
    E.foco(c, t, e1, 0.5, lambda a: E.formula(c, "no 1º quadrante, o seno é positivo", X, 1010, 44, "g", ERRADO, a, "center"))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.1, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s22.a"], ps("par completo,", "i", 62) + [("senos;", "g", 66, PAR1)] + ps("sem par,", "i", 62) + [("cossenos", "g", 66, PAR2)]),
                     (C["s22.b"], ps("identidade:", "i", 62) + [("tudo em seno e cosseno", "g", 66, COR)]),
                     (C["s22.c"], ps("equação:", "i", 62) + [("a linha corta o ciclo em 2 pontos", "g", 64, COR)])], 200, 400, 190, 62)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"] - 0.1:
        return
    a3, b3, c3, d3 = (C[f"s23.{k}"] for k in "abcd")
    E.frase(c, t, C["s23"], ps("trigonometria avançada:", "i", 64) + [("trilha completa", "g", 70, CERTO)], XE, 210, "left", 0.1)
    E.frase(c, t, a3 - 0.8, ps("o próximo assunto", "i", 64), XE, 360, "left", 0.1)
    E.frase(c, t, a3, [("polinômios", "g", 120, COR)], XE, 510, "left", 0.1)
    cf_em(c, t, b3, [("P(x) = 2x^3 − x + 5", TINTA)], XE, 690, 84)
    E.foco(c, t, c3, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 400, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c3 + 0.3, 0.8))
    E.cursor(c, lerp(1850, 1650, p), lerp(640, 425, p), ep(t, c3 + 0.2, 0.4))
    E.frase(c, t, d3, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4,
              q5=b_q5, r5=b_r5, fim=b_fim)
