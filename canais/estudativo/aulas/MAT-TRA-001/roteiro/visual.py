"""Visual — Estudativo · MAT-TRA-001: lei dos senos (30° e 45°, lado oposto a 30° = 10 → x = 10√2 ≈ 14; questão 30° e 120°,
lado oposto a 30° = 5 → 5√3 ≈ 8,5). Primeira aula de Trigonometria Avançada.

LINGUAGEM VISUAL DA TRIGONOMETRIA AVANÇADA (as próximas aulas da trilha copiam daqui; segue a da trigonometria, MAT-TRI-001):
- Triângulo qualquer em tinta preta, preenchido de leve; altura tracejada com o quadradinho no pé.
- O PAR (lado + ângulo de frente para ele) ganha uma COR só, pintada no lado e no arco do ângulo:
    PAR1 = índigo da matéria (E.COR)   o par completo, que a questão dá
    PAR2 = âmbar #D98A00               o par com a incógnita
    PAR3 = magenta #C0187C             o terceiro par, quando entra
  Nas frações da lei, o lado e o seno do seu ângulo saem na cor do par.
- sen sempre abreviado na tela; resposta final na pílula; erro em vermelho, certo em verde; atalho no palco escuro.
- A figura não mente: os ângulos são os de verdade (30°, 45°, 105°; 30°, 120°, 30°) e os lados, proporcionais.
Peças locais: tri() (triângulo por ângulos, com os pares coloridos), rot(), arco_par(), fra(), lei(), resp(), lista().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria Avançada")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRA-001_lei_dos_senos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("altura", "conta", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
PAR1, PAR2, PAR3 = E.COR, AMBAR, "#C0187C"
S = lambda g: math.sin(math.radians(g))
X = 10 * S(45) / S(30)
assert abs(X - 10 * math.sqrt(2)) < 1e-9 and abs(10 / S(30) - 20) < 1e-9 and round(10 * math.sqrt(2)) == 14
assert abs(10 * S(30) / S(45) - 5 * math.sqrt(2)) < 1e-9 and round(5 * math.sqrt(2)) == 7
assert abs(5 / S(30) - 10) < 1e-9 and abs(S(120) - S(60)) < 1e-12 and abs(10 * S(120) - 5 * math.sqrt(3)) < 1e-9 and 5 * 1.7 == 8.5


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


# triângulo do exemplo: 30° em A, 45° em B, lado BC (de frente para 30°) = 10, lado CA (de frente para 45°) = x
TA, TB, TC = pontos(966, 30, 45, 0, 0)


def tri_ex(c, t, t0, x0, y0, k=1.0, **kw):
    A = (x0 + TA[0] * k, y0 + TA[1] * k)
    B = (x0 + TB[0] * k, y0 + TB[1] * k)
    Cc = (x0 + TC[0] * k, y0 + TC[1] * k)
    tri(c, t, t0, A, B, Cc, **kw)
    return A, B, Cc


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        tri_ex(c, t, a1, 470, 760, 1.0, angs=("30°", "45°", None), lados=(None, "10", "?"),
               ta={"A": a1 + 0.6, "B": a1 + 1.0}, tl={"A": b1, "B": c1}, cores={"A": (b1, PAR1), "B": (c1, PAR2)}, size=70)
        E.frase(c, t, d1, ps("sem", "i", 66) + [("ângulo reto", "g", 70, ERRADO)], W / 2, 960, "center", 0.1)
        if t >= d1 + 0.8:
            E.foco(c, t, d1 + 0.8, 0.4, lambda a: E.formula(c, "sen, cos, tg do triângulo retângulo?", W / 2, 1040, 46, "g", TINTA2, a, "center"))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, ta + 1.2, [("lei dos", "g", 140), ("senos", "g", 140, COR)], XE, 500, "left", 0.14)
        E.frase(c, t, ta + 2.0, ps("numa linha", "i", 90), XE, 650, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 545, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 630, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 230, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "no triângulo retângulo:", [("oposto = hip × sen", "g", 64, COR)]),
             ("s03.c", "ângulo maior que 90°:", [("sen 150° = sen 30°", "g", 64, COR)]))
    for i, (k, l1, l2) in enumerate(itens):
        y = 260 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 210, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 88)
        E.frase(c, t, C[k] + 0.3, l2, x + 44, y + 172, "left", 0.08)
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 900, 920, "left", 0.12)


# ---------------- de onde vem: a altura ----------------
def b_altura(c, t, C, b):
    a4, b4, c4 = (C[f"s04.{k}"] for k in "abc")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6 = (C[f"s06.{k}"] for k in "abc")
    x0, y0 = 120, 640
    A, B, Cc = tri_ex(c, t, C["s04"] - 0.3, x0, y0, 0.86, angs=("30°", "45°", None), lados=(None, "10", "x"),
                      ta={"A": C["s04"], "B": C["s04"]}, tl={"A": C["s04"], "B": C["s04"]},
                      cores={"A": (C["s04"] - 0.3, PAR1), "B": (C["s04"] - 0.3, PAR2)}, size=60)
    altura(c, t, a4, Cc, y0)
    E.foco(c, t, c4, 0.4, lambda a: E.escreve(c, "h", Cc[0] + 14, (Cc[1] + y0) / 2 + 20, 60, "b", TINTA2, a))
    # os dois triângulos retângulos piscam
    for i, (P, Q, t_) in enumerate(((A, (Cc[0], y0), b4), ((Cc[0], y0), B, b4 + 0.4))):
        q = ep(t, t_, 0.4) * (1 - ep(t, t_ + 1.2, 0.5))
        if q > 0:
            path = skia.Path(); path.addPoly([P, Q, Cc], True)
            c.drawPath(path, M.paint(PAR2 if i == 0 else PAR1, 0.18 * q))
    X0 = 1430
    E.frase(c, t, a5, ps("na esquerda:", "i", 56, TINTA2), X0, 170, "center", 0.1)
    cf_em(c, t, b5, [("h = ", TINTA), ("x", PAR2), (" · sen 30°", TINTA)], X0, 260, 72, "center")
    E.frase(c, t, c5, ps("na direita:", "i", 56, TINTA2), X0, 380, "center", 0.1)
    cf_em(c, t, d5, [("h = ", TINTA), ("10", PAR1), (" · sen 45°", TINTA)], X0, 470, 72, "center")
    cf_em(c, t, a6, [("x", PAR2), (" · sen 30° = ", TINTA), ("10", PAR1), (" · sen 45°", TINTA)], X0, 610, 64, "center")
    E.frase(c, t, b6, ps("a", "i", 60) + [("lei dos senos", "g", 66, COR)], X0, 730, "center", 0.1)
    E.foco(c, t, b6 + 0.6, 0.5, lambda a: lei(c, [("x", "45°", PAR2), ("10", "30°", PAR1)], X0, 880, 92, a, align="center"))


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    E.frase(c, t, C["s07"] + 0.1, ps("nos livros", "i", 70, COR), W / 2, 140, "center", 0.1)
    E.foco(c, t, a7, 0.6, lambda a: lei(c, [("a", "A", PAR1), ("b", "B", PAR2), ("c", "C", PAR3)], W / 2, 375, 130, a, align="center"))
    A, B, Cc = pontos(600, 50, 70, 220, 1010)
    k_lado = ep(t, b7, 0.4)
    tri(c, t, b7 - 0.4, A, B, Cc, ("A", "B", "C"), ("c", "a", "b"), ta={k: c7 for k in "ABC"}, tl={k: b7 for k in "ABC"},
        cores={"A": (d7, PAR1), "B": (d7 + 0.3, PAR2), "C": (d7 + 0.6, PAR3)}, size=64, r_ang=70)
    E.frase(c, t, b7, [("minúscula:", "g", 60)] + ps("o lado", "i", 60), 1000, 660, "left", 0.1)
    E.frase(c, t, c7, [("maiúscula:", "g", 60)] + ps("o ângulo de frente", "i", 60), 1000, 780, "left", 0.1)
    E.frase(c, t, d7, ps("lado e ângulo de frente:", "i", 58) + [("um par", "g", 62, COR)], 1000, 900, "left", 0.1)


# ---------------- a conta ----------------
def b_conta(c, t, C, b):
    a8, b8, c8 = (C[f"s08.{k}"] for k in "abc")
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    a0, b0, c0 = (C[f"s10.{k}"] for k in "abc")
    A, B, Cc = tri_ex(c, t, C["s08"] - 0.3, 1100, 520, 0.72, angs=("30°", "45°", None), lados=(None, "10", "x"),
                      ta={"A": C["s08"], "B": C["s08"]}, tl={"A": C["s08"], "B": C["s08"]},
                      cores={"A": (C["s08"] - 0.3, PAR1), "B": (C["s08"] - 0.3, PAR2)}, size=56, r_ang=64)
    E.foco(c, t, a8, 0.5, lambda a: lei(c, [("10", "30°", PAR1), ("x", "45°", PAR2)], XE, 300, 110, a))
    E.foco(c, t, b8, 0.5, lambda a: E.formula(c, "sen 30° = f{1}{2}", XE, 480, 66, "g", TINTA2, a))
    cf_em(c, t, c8, [("10 ÷ f{1}{2} = 10 × 2 = ", TINTA), ("20", PAR1)], XE, 620, 72)
    cf_em(c, t, a9, [("x", PAR2), (" ÷ sen 45° = 20", TINTA)], XE, 760, 72)
    cf_em(c, t, b9, [("x", PAR2), (" = 20 · sen 45°", TINTA)], XE, 880, 72)
    cf_em(c, t, c9, [("= 20 · f{r{2}}{2}", TINTA)], XE + 115, 1000, 72)
    resp(c, t, d9, [("x = 10", BR), ("r{2}", BR)], 1450, 720, 80, cor=PAR2)
    E.foco(c, t, e9, 0.5, lambda a: E.formula(c, "≈ 10 · 1,4 = 14", 1450, 860, 64, "g", TINTA2, a, "center"))
    E.frase(c, t, a0, ps("maior ângulo,", "i", 52) + [("maior lado", "g", 56, CERTO)], 1450, 980, "center", 0.1)
    E.foco(c, t, c0, 0.5, lambda a: E.selo(c, 1790, 960, 36, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1 = (C[f"s11.{k}"] for k in "abc")
    a2, b2, c2 = (C[f"s12.{k}"] for k in "abc")
    errado = a2 > t >= b1
    x0, y0 = 160, 740
    A, B, Cc = tri_ex(c, t, C["s11"] - 0.3, x0, y0, 0.8, angs=("30°", "45°", None), lados=(None, "10", "x"),
                      ta={"A": C["s11"], "B": C["s11"]}, tl={"A": C["s11"], "B": C["s11"]}, size=60, r_ang=70)
    E.frase(c, t, a1, ps("o erro:", "i", 62) + [("o par errado", "g", 68, ERRADO)], W / 2, 170, "center", 0.1)
    if t >= b1:  # o 10 com os 45° que encostam nele
        q = ep(t, b1, 0.5)
        M.line(c, *B, *Cc, ERRADO, q, 12)
        E.angulo(c, t, b1 + 0.2, B, Cc, A, None, r=70, cor=ERRADO)
    E.foco(c, t, c1, 0.5, lambda a: lei(c, [("10", "45°", ERRADO), ("x", "30°", ERRADO)], 1180, 360, 92, a))
    E.foco(c, t, c1 + 0.8, 0.5, lambda a: E.formula(c, "x = 5r{2} ≈ 7", 1180, 560, 80, "g", ERRADO, a))
    E.foco(c, t, a2, 0.5, lambda a: (E.formula(c, "7 de frente para 45°", 1180, 700, 60, "g", ERRADO, a),
                                      E.formula(c, "10 de frente para 30°", 1180, 790, 60, "g", ERRADO, a)))
    E.foco(c, t, b2, 0.5, lambda a: E.selo(c, 1110, 740, 44, False, a))
    E.foco(c, t, c2, 0.5, lambda a: E.pilula(c, "cada lado conversa com o ângulo de FRENTE", W / 2, 990, 52, "g", fundo=E.COR, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    a4, b4, c4 = (C[f"s14.{k}"] for k in "abc")
    CL1, CL2 = E.mix(PAR1, BR, 0.45), "#F2B33D"

    def treze():
        E.frase(c, t, C["s13"] + 0.1, ps("agora o atalho", "i", 62, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a3, ps("ache primeiro o", "i", 72, CLARO) + [("número fixo", "g", 80, BR)], W / 2, 300, "center", 0.12)
        E.foco(c, t, b3, 0.5, lambda a: (fra(c, "lado do par", "sen do seu ângulo", 420, 500, 96, a, CL1, CL1, barra=BR)))
        cf_em(c, t, c3, [("f{10}{sen 30°} = ", BR), ("20", CL1)], 1180, 500, 96)
        E.frase(c, t, d3, ps("qualquer lado =", "i", 64, CLARO) + [("20 × sen", "g", 70, BR)] + ps("do ângulo de frente", "i", 64, CLARO),
                W / 2, 730, "center", 0.1)
        cf_em(c, t, e3, [("45°: ", CL2), ("20 · f{r{2}}{2} = 10r{2}", BR)], W / 2, 900, 88, "center")
    E.saida(c, t, C["s14"] - 0.1, treze)
    if t < C["s14"] - 0.1:
        return
    E.frase(c, t, a4, ps("funciona porque a divisão dá", "i", 64, CLARO) + [("o mesmo número", "g", 70, BR)], W / 2, 260, "center", 0.1)
    E.frase(c, t, a4 + 1.4, ps("para os", "i", 64, CLARO) + [("três lados", "g", 70, BR)], W / 2, 360, "center", 0.1)
    E.foco(c, t, b4, 0.5, lambda a: E.selo(c, 470, 575, 42, False, a))
    E.frase(c, t, b4, ps("sem", "i", 64, CLARO) + [("par completo,", "g", 70, BR)] + ps("não começa", "i", 64, CLARO), 540, 600, "left", 0.1)
    E.frase(c, t, b4 + 1.2, ps("um lado e o ângulo de frente para ele", "i", 54, CLARO), 540, 690, "left", 0.08)
    E.foco(c, t, c4, 0.5, lambda a: E.pilula(c, "sem par: lei dos cossenos", W / 2, 880, 60, "g", fundo=E.COR, a=a))


# ---------------- questão ----------------
QA, QB, QC = pontos(820, 30, 30, 0, 0)
G3 = math.degrees(math.asin(3 * S(120) / 7))   # ângulo de frente para o 3 no triângulo 3, 5, 7
G5 = 180 - 120 - G3  # 30°, 30° e 120° no topo


def b_questao(c, t, C, b):
    a5, b5, c5 = (C[f"s15.{k}"] for k in "abc")
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    x0, y0 = 160, 760
    A, B, Cc = (x0 + QA[0], y0 + QA[1]), (x0 + QB[0], y0 + QB[1]), (x0 + QC[0], y0 + QC[1])
    tri(c, t, a5 - 0.4, A, B, Cc, ("30°", None, "120°"), ("?", "5", None), ta={"A": a5, "C": a5 + 0.5}, tl={"A": b5, "C": c5},
        cores={"A": (b5, PAR1), "C": (c5, PAR2)}, size=64, r_ang=72)
    E.frase(c, t, a5, ps("ângulos", "i", 64) + [("30° e 120°", "g", 70, COR)], 1120, 360, "left", 0.1)
    E.frase(c, t, b5, ps("de frente para 30°:", "i", 60) + [("5 m", "g", 70, PAR1)], 1120, 480, "left", 0.1)
    E.frase(c, t, c5, ps("de frente para 120°:", "i", 60) + [("?", "g", 76, PAR2)], 1120, 600, "left", 0.1)
    E.relogio(c, t, C["s16.a"], 1500, 800, 140)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7 = (C[f"s17.{k}"] for k in "abc")
    a8, b8, c8 = (C[f"s18.{k}"] for k in "abc")
    x0, y0 = 1060, 520
    k = 0.8
    A, B, Cc = ((x0 + QA[0] * k, y0 + QA[1] * k), (x0 + QB[0] * k, y0 + QB[1] * k), (x0 + QC[0] * k, y0 + QC[1] * k))
    tri(c, t, C["s17"] - 0.3, A, B, Cc, ("30°", None, "120°"), ("?", "5", None), ta={"A": C["s17"], "C": C["s17"]},
        tl={"A": C["s17"], "C": C["s17"]}, cores={"A": (C["s17"] - 0.3, PAR1), "C": (C["s17"] - 0.3, PAR2)}, size=56, r_ang=60)
    E.frase(c, t, C["s17"] + 0.1, ps("vamos lá", "i", 62, COR), XE, 170, "left", 0.1)
    cf_em(c, t, a7, [("número fixo: ", TINTA2), ("5 ÷ f{1}{2} = ", TINTA), ("10", PAR1)], XE, 320, 76)
    cf_em(c, t, b7, [("sen 120° = sen 60°", TINTA)], XE, 480, 76)
    cf_em(c, t, c7, [("= f{r{3}}{2}", TINTA)], XE + 270, 610, 76)
    cf_em(c, t, a8, [("10 · f{r{3}}{2} = 5r{3}", TINTA)], XE, 780, 80)
    resp(c, t, b8, "≈ 5 · 1,7 = 8,5 m", 1450, 780, 64, cor=PAR2)
    E.frase(c, t, c8, ps("maior ângulo,", "i", 56) + [("maior lado", "g", 60, CERTO)], 1450, 950, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"] + 0.1, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        E.foco(c, t, C["s19.a"], 0.5, lambda a: lei(c, [("a", "A", PAR1), ("b", "B", PAR2), ("c", "C", PAR3)], W / 2, 420, 110, a, align="center"))
        lista(c, t, [(C["s19.b"], ps("ache o número com o", "i", 64) + [("par completo", "g", 68, COR)]),
                     (C["s19.c"], [("multiplique", "g", 68, COR)] + ps("pelo seno do ângulo que você quer", "i", 64))], 260, 700, 170, 64)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"] - 0.1:
        return
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    E.frase(c, t, C["s20"], ps("na próxima aula", "i", 72), XE, 210, "left", 0.1)
    E.frase(c, t, C["s20"] + 0.8, [("lei dos cossenos", "g", 110, COR)], XE, 360, "left", 0.1)
    E.frase(c, t, a0, ps("dois lados e o", "i", 62) + [("ângulo entre eles", "g", 66)], XE, 500, "left", 0.1)
    A, B, Cc = pontos(560, G5, G3, XE, 860)  # lados 5 e 3 com 120° entre eles (o terceiro lado é 7)
    tri(c, t, b0, A, B, Cc, (None, None, "120°"), (None, "5", "3"), ta={"C": b0 + 0.6}, tl={"A": b0 + 0.6, "B": b0 + 0.6}, size=58, r_ang=56)
    E.foco(c, t, c0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1460, 560, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c0 + 0.3, 0.8))
    E.cursor(c, lerp(1790, 1590, p), lerp(800, 585, p), ep(t, c0 + 0.2, 0.4))
    E.frase(c, t, d0, [("bons", "i", 120), ("estudos!", "i", 120, COR)], 1420, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, altura=b_altura, regra=b_regra, conta=b_conta, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
