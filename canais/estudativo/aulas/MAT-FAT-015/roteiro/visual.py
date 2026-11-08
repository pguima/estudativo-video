"""Visual — Estudativo · MAT-FAT-015: soma vezes diferença e cubo da soma.
(x + 5)(x − 5) pelo chuveirinho, com os termos do meio se anulando; a regra (a + b)(a − b) = a² − b² e 101 × 99; o cubo
(x + 1)³ = (x + 1)²(x + 1), com as duas linhas do chuveirinho somadas em colunas de semelhantes; o erro x³ + 1; no palco,
52 × 48 pela distância ao 50 na reta.
Mesma linguagem da trilha (ver MAT-FAT-001): termo do meio com realce na cor da matéria, erro em vermelho com risco,
atalho no palco. Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-015_soma_vezes_diferenca_e_cubo_da_soma.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("soma", "cubo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"

x = 10
assert 101 * 99 == 100 ** 2 - 1 == 9999
assert (x + 5) * (x - 5) == x * x - 25 == 75 == 15 * 5
assert (x + 1) ** 3 == x ** 3 + 3 * x * x + 3 * x + 1 == 1331 == 11 ** 3 and x ** 3 + 1 == 1001
assert (x + 1) ** 2 * (x + 1) == (x ** 3 + 2 * x * x + x) + (x * x + 2 * x + 1)
assert 52 * 48 == 50 ** 2 - 2 ** 2 == 2496
assert (30 + 4) * (30 - 4) == 900 - 16 == 884 == 34 * 26
del x


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def entre(t0, t1, f):
    """instante na fração f do trecho entre dois marcadores: fala sem marcador própria"""
    return t0 + (t1 - t0) * f


def form(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def fw(s, size):
    return E.formula(None, s, 0, 0, size, a=0) if s else 0.0


def trecho_x(s, trecho, x, size, align="left", n=0):
    """(x inicial, largura) de um trecho da fórmula s"""
    xi = x - fw(s, size) / 2 if align == "center" else x
    i0 = -1
    for _ in range(n + 1):
        i0 = s.find(trecho, i0 + 1)
    return xi + fw(s[:i0], size), fw(trecho, size) - size * 0.02


def realce(c, t, t0, s, trecho, x, y, size, cor=None, align="left", n=0, t1=None):
    a = ep(t, t0, 0.35) * (1 - ep(t, t1, 0.3) if t1 else 1)
    if a <= 0:
        return
    x0, w = trecho_x(s, trecho, x, size, align, n)
    pad = min(size * 0.14, 16)
    M.rrect(c, x0 - pad, y - size * 0.95, w + pad * 2, size * 1.25, size * 0.2, cor or COR, 0.16 * a)


def monta(c, t, pecas, x, y, size, align="left", cor=None):
    total = fw("".join(p[0] for p in pecas), size)
    x0 = x - total / 2 if align == "center" else x
    acc = ""
    for p in pecas:
        s, t0, cp = p[0], p[1], (p[2] if len(p) > 2 else cor)
        xo = x0 + fw(acc, size)
        E.foco(c, t, t0, 0.4, lambda a, s=s, xo=xo, cp=cp: E.formula(c, s, xo, y, size, cor=cp, a=a))
        acc += s
    return x0


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def flecha(c, t, t0, x0, y0, x1, y1, alto, cor, d=0.6, largura=6):
    """arco de (x0, y0) a (x1, y1) com ponta de seta; alto > 0 sobe, alto < 0 desce"""
    p = ep(t, t0, d)
    if p <= 0:
        return
    cx = (x0 + x1) / 2
    cy = (min(y0, y1) - alto) if alto > 0 else (max(y0, y1) - alto)
    pt = lambda u: ((1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u * u * x1, (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u * u * y1)
    n = max(2, int(30 * p))
    path = skia.Path()
    path.moveTo(*pt(0))
    for i in range(1, n + 1):
        path.lineTo(*pt(p * i / n))
    c.drawPath(path, M.paint(cor, 1.0, stroke=largura, cap_round=True))
    if p > 0.97:
        ang = math.atan2(y1 - cy, x1 - cx)
        for da in (2.6, -2.6):
            M.line(c, x1, y1, x1 + 24 * math.cos(ang + da), y1 + 24 * math.sin(ang + da), cor, 1.0, largura)


def chuveiro(c, t, ts, s, y, size, cor, align="center", x=W / 2, alto=90):
    """as quatro setas do chuveirinho, em ts = (1º·1º, 1º·2º, 2º·1º, 2º·2º); s = fórmula com dois parênteses"""
    i2 = s.index(")(") + 1
    p1, p2 = s[1:i2 - 1], s[i2 + 1:-1]
    a1, b1 = p1.split(" ", 1)[0], p1.split(" ", 2)[2]
    a2, b2 = p2.split(" ", 1)[0], p2.split(" ", 2)[2]
    pos = lambda tr, n=0: trecho_x(s, tr, x, size, align, n)
    xa1, wa1 = pos(a1)
    xb1, wb1 = pos(b1)
    xa2, wa2 = pos(a2, 1 if a2 == a1 else 0)
    xb2, wb2 = pos(b2, 1 if b2 == b1 else 0)
    topo, base = y - size * 0.95, y + size * 0.2
    flecha(c, t, ts[0], xa1 + wa1 / 2, topo, xa2 + wa2 / 2, topo, alto * 1.4, cor)
    flecha(c, t, ts[1], xa1 + wa1 / 2, topo, xb2 + wb2 / 2, topo, alto * 2.2, cor)
    flecha(c, t, ts[2], xb1 + wb1 / 2, base, xa2 + wa2 / 2, base, -alto * 1.4, cor)
    flecha(c, t, ts[3], xb1 + wb1 / 2, base, xb2 + wb2 / 2, base, -alto * 2.2, cor)


TONS = (E.COR, M.mix(E.COR, BR, 0.45), M.mix(E.COR, BR, 0.45), M.mix(E.COR, BR, 0.72))


def piso(c, x0, y0, A, B, a=1.0, nomes=("x^2", "3x", "3x", "9"), rot=(0, 0, 0, 0), pinta=(1, 1, 1, 1), falta=(0, 0, 0, 0),
         sizes=(96, 64, 64, 64), escuro=False):
    """piso quadrado de lado A + B (em pixels): quadrado grande A×A, faixa A×B à direita, faixa B×A embaixo, quadradinho B×B.
    rot = alfa do nome de cada pedaço; pinta = quanto cada pedaço já tem a sua cor; falta = pedaço que sumiu (contorno vermelho tracejado)"""
    if a <= 0:
        return
    vazio = M.mix(E.COR, BR, 0.88) if not escuro else M.mix(E.COR, "#07070F", 0.5)
    pedacos = ((0, 0, A, A), (A, 0, B, A), (0, A, A, B), (A, A, B, B))
    for i, (dx, dy, w, h) in enumerate(pedacos):
        f = falta[i]
        q = a * (1 - 0.85 * f)
        r = skia.Rect.MakeXYWH(x0 + dx, y0 + dy, w, h)
        M.rrect(c, x0 + dx, y0 + dy, w, h, 8, M.mix(vazio, TONS[i], pinta[i]), q)
        c.drawRRect(skia.RRect.MakeRectXY(r, 8, 8), M.paint(E.COR, q, stroke=3))
        if f > 0:
            p = M.paint(ERRADO, a * f, stroke=5)
            p.setPathEffect(skia.DashPathEffect.Make([16, 12], 0))
            c.drawRRect(skia.RRect.MakeRectXY(r.makeInset(6, 6), 6, 6), p)
        if rot[i] > 0:
            tinta = BR if (i == 0 and pinta[0] > 0.5) else TINTA
            E.formula(c, nomes[i], x0 + dx + w / 2, y0 + dy + h / 2 + sizes[i] * 0.36, sizes[i], cor=tinta, a=rot[i] * q, align="center")


def lados(c, t, ta, x0, y0, A, B, la="x", lb="3", cor=None, size=64):
    """rótulos dos lados do piso quadrado: la + lb à esquerda e em cima"""
    cor = cor or COR
    E.foco(c, t, ta, 0.45, lambda p: (E.formula(c, la, x0 - 46, y0 + A / 2 + size * 0.36, size, cor=cor, a=p, align="center"),
                                     E.formula(c, lb, x0 - 46, y0 + A + B / 2 + size * 0.36, size, cor=cor, a=p, align="center"),
                                     E.formula(c, la, x0 + A / 2, y0 - 28, size, cor=cor, a=p, align="center"),
                                     E.formula(c, lb, x0 + A + B / 2, y0 - 28, size, cor=cor, a=p, align="center")))


def risca(c, t, t0, s, trecho, x, y, size, align="left", cor=ERRADO):
    """risco inclinado sobre um trecho da fórmula: termo que se anula"""
    if t < t0:
        return
    x0, w = trecho_x(s, trecho, x, size, align)
    E.risco(c, x0 - 8, y + size * 0.1, x0 + w + 8, y - size * 0.75, t, t0, cor, 9)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]

    def conta():
        form(c, t, a_, "101 × 99", W / 2, 400, 200, COR, "center")
        E.frase(c, t, entre(a_, b_, 0.35), ps("sem conta armada, sem calculadora", "i", 70, TINTA2), W / 2, 560, "center", 0.1)
        form(c, t, b_, "= 9.999", W / 2, 820, 200, CERTO, "center")
        E.foco(c, t, entre(b_, C["s02"], 0.5), 0.45, lambda p: centro(c, "em poucos segundos", W / 2, 960, 62, "i", COR, p))
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]
    E.frase(c, t, a2, ps("até o fim desta aula, você", "i", 84), XE, 230, passo=0.12)
    E.frase(c, t, a2 + 1.0, ps("faz essa conta de cabeça", "g", 92, COR), XE, 370, passo=0.13)
    E.frase(c, t, b2, ps("soma × diferença", "i", 80), XE, 560, passo=0.12)
    form(c, t, b2 + 0.4, "(a + b)(a − b)", XE + 700, 565, 100, COR)
    E.frase(c, t, b2 + 1.0, ps("sem chuveirinho", "i", 60, TINTA2), XE + 700, 650, passo=0.1)
    E.frase(c, t, c2, ps("e o cubo de uma soma", "i", 80), XE, 830, passo=0.12)
    form(c, t, c2 + 0.6, "(a + b)^3", XE + 820, 835, 100, COR)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_ = C["s03.a"], C["s03.b"]
    E.frase(c, t, C["s03"] + 0.3, ps("para", "i", 84) + ps("acompanhar", "g", 84, COR), XE, 180)
    xr = XE + 110
    E.foco(c, t, a_, 0.45, lambda p: num_bola(c, "1", XE + 40, 360, 40, 50, p))
    E.frase(c, t, a_, ps("quadrado da soma", "g", 66, COR), xr, 385, passo=0.1)
    form(c, t, a_ + 0.7, "(a + b)^2 = a^2 + 2ab + b^2", xr, 520, 100)
    realce(c, t, a_ + 1.5, "(a + b)^2 = a^2 + 2ab + b^2", "2ab", xr, 520, 100)
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "2", XE + 40, 680, 40, 50, p))
    E.frase(c, t, b_, ps("chuveirinho:", "g", 66, COR) + ps("todo termo multiplica todo termo", "i", 60), xr, 705, passo=0.1)
    s = "(x + 2)(x + 3)"
    form(c, t, b_ + 0.5, s, xr + 20, 920, 100)
    chuveiro(c, t, (b_ + 1.0, b_ + 1.3, b_ + 1.6, b_ + 1.9), s, 920, 100, COR, "left", xr + 20, 34)
    E.frase(c, t, C["s04"] - 2.2, ps("faltou alguma? procure no canal", "i", 54, TINTA2), 1150, 920, passo=0.08)


# ---------------- soma vezes diferença ----------------
SD = "(x + 5)(x − 5)"
MEIO = "x^2 − 5x + 5x − 25"


def b_soma(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]

    def s04():
        E.frase(c, t, C["s04"] + 0.2, ps("comece com", "i", 80), W / 2, 220, "center")
        monta(c, t, [("(x + 5)", a4), ("(x − 5)", b4)], W / 2, 520, 200, "center")
        x1, w1 = trecho_x(SD, "+", W / 2, 200, "center")
        x2, w2 = trecho_x(SD, "−", W / 2, 200, "center")
        realce(c, t, c4, SD, "+", W / 2, 520, 200, align="center")
        realce(c, t, c4 + 0.6, SD, "−", W / 2, 520, 200, align="center")
        E.foco(c, t, c4, 0.45, lambda p: centro(c, "com mais", x1 + w1 / 2, 680, 60, "i", COR, p))
        E.foco(c, t, c4 + 0.6, 0.45, lambda p: centro(c, "com menos", x2 + w2 / 2, 680, 60, "i", COR, p))
        E.frase(c, t, entre(b4, c4, 0.4), ps("os mesmos termos:", "i", 66, TINTA2) + ps("x e 5", "g", 66, TINTA), W / 2, 880, "center", 0.1)
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)

    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")

    def s0506():
        form(c, t, C["s05"] + 0.1, SD, W / 2, 270, 130, None, "center")
        chuveiro(c, t, (a5, b5, c5, d5), SD, 270, 130, COR, "center", W / 2, 46)
        y = 590
        monta(c, t, [("x^2", a5 + 0.2), (" − 5x", b5 + 0.2), (" + 5x", c5 + 0.2), (" − 25", d5 + 0.2)], W / 2, y, 130, "center")
        for tr, nota, tk in (("x^2", "x × x", a5), ("− 5x", "x × (−5)", b5), ("+ 5x", "5 × x", c5), ("− 25", "5 × (−5)", d5)):
            xx, ww = trecho_x(MEIO, tr, W / 2, 130, "center")
            E.foco(c, t, tk + 0.3, 0.4, lambda p, xx=xx, ww=ww, nota=nota: centro(c, nota, xx + ww / 2, y + 90, 48, "i", TINTA2, p))
        realce(c, t, a6, MEIO, "− 5x + 5x", W / 2, y, 130, align="center")
        xm, wm = trecho_x(MEIO, "− 5x + 5x", W / 2, 130, "center")
        E.foco(c, t, a6 + 0.6, 0.45, lambda p: centro(c, "= 0", xm + wm / 2, y - 150, 70, "g", COR, p))
        risca(c, t, b6, MEIO, "− 5x", W / 2, y, 130, "center")
        risca(c, t, b6 + 0.2, MEIO, "+ 5x", W / 2, y, 130, "center")
        E.foco(c, t, b6 + 0.4, 0.45, lambda p: centro(c, "se anulam", xm + wm / 2, y + 160, 56, "b", ERRADO, p))
        form(c, t, c6, "= x^2 − 25", W / 2, 900, 120, CERTO, "center")
        E.frase(c, t, d6 - 0.6, ps("com 10:", "i", 56, TINTA2), XE, 1030, passo=0.1)
        form(c, t, d6, "15 × 5 = 75", XE + 230, 1035, 72)
        form(c, t, e6, "100 − 25 = 75", 1000, 1035, 72)
        E.foco(c, t, e6 + 0.6, 0.45, lambda p: E.selo(c, 1580, 1010, 36, True, p))
    fase(c, t, C["s05"], 1e9, s0506)


# ---------------- regra ----------------
REGRA = "(a + b)(a − b) = a^2 − b^2"


def b_regra(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")

    def s07():
        E.frase(c, t, C["s07"] + 0.2, ps("produto notável:", "i", 76), XE, 180, passo=0.1)
        E.frase(c, t, a7, ps("soma × diferença", "g", 84, COR), XE + 560, 185, passo=0.12)
        s, y = 140, 470
        x0 = W / 2 - fw(REGRA, s) / 2
        monta(c, t, [("(a + b)(a − b) = ", a7 + 0.4), ("a^2", b7, COR), (" − b^2", c7, COR)], x0, y, s)
        for tr, nota, tk, dy in (("a^2", "quadrado do 1º", b7, 100), ("b^2", "quadrado do 2º", c7, 170)):
            xx, ww = trecho_x(REGRA, tr, x0, s)
            E.foco(c, t, tk + 0.3, 0.4, lambda p, xx=xx, ww=ww, nota=nota, dy=dy: centro(c, nota, xx + ww / 2, y + dy, 52, "i", COR, p))
        E.frase(c, t, d7, ps("o meio sempre some:", "i", 66), XE, 800, passo=0.1)
        form(c, t, d7 + 0.8, "+ ab − ab = 0", XE + 640, 805, 100, COR)
        E.frase(c, t, d7 + 1.6, ps("um acrescenta o que o outro tira", "i", 56, TINTA2), XE, 930, passo=0.08)
    fase(c, t, C["s07"], C["s08"] - 0.1, s07)

    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")

    def s08():
        E.frase(c, t, C["s08"] + 0.2, ps("volte ao gancho", "i", 76, TINTA2), XE, 180, passo=0.1)
        form(c, t, a8, "101 = 100 + 1", XE, 350, 110)
        form(c, t, b8, "99 = 100 − 1", 1050, 350, 110)
        form(c, t, c8, "101 × 99 = 100^2 − 1^2", XE, 580, 120, COR)
        form(c, t, d8, "= 10.000 − 1 = 9.999", XE + 120, 800, 120, CERTO)
        E.foco(c, t, d8 + 1.0, 0.45, lambda p: E.selo(c, XE + 120 + fw("= 10.000 − 1 = 9.999", 120) + 90, 760, 52, True, p))
    fase(c, t, C["s08"], 1e9, s08)


# ---------------- cubo ----------------
COLS = (560, 900, 1260, 1560)  # colunas de x³, x², x e número


def linha_cols(c, t, t0, termos, y, size, cor=None):
    for xc, s in zip(COLS, termos):
        if s:
            form(c, t, t0, s, xc, y, size, cor, "center")


def b_cubo(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]

    def s09():
        E.frase(c, t, C["s09"] + 0.2, ps("agora, o", "i", 80) + ps("cubo", "g", 80, COR), XE, 180, passo=0.1)
        form(c, t, a9, "(x + 1)^3 = (x + 1)(x + 1)(x + 1)", XE, 380, 110)
        E.foco(c, t, a9 + 1.2, 0.45, lambda p: E.escreve(c, "o parêntese três vezes", XE, 470, 56, "i", TINTA2, p))
        F = "(x + 1)^3 = (x + 1)^2 · (x + 1)"
        form(c, t, b9, F, XE, 680, 120, COR)
        E.foco(c, t, b9 + 0.6, 0.45, lambda p: E.escreve(c, "o quadrado vezes mais um parêntese", XE, 780, 56, "i", TINTA2, p))
        E.foco(c, t, c9, 0.45, lambda p: E.pilula(c, "2 + 1 = 3", 1500, 940, 70, estilo="g", a=p))
        E.frase(c, t, c9 + 0.3, ps("regra da mesma base", "i", 54, TINTA2), XE, 950, passo=0.08)
    fase(c, t, C["s09"], C["s10"] - 0.1, s09)

    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    a1, b1, c1 = (C[f"s11.{k}"] for k in "abc")

    def s1011():
        form(c, t, C["s10"] + 0.1, "(x + 1)^2", XE, 180, 84, TINTA2)
        form(c, t, a0, "= x^2 + 2x + 1", XE + fw("(x + 1)^2 ", 84), 180, 84, TINTA2)
        form(c, t, b0, "(x^2 + 2x + 1)(x + 1)", W / 2, 330, 110, COR, "center")
        E.frase(c, t, c0, ps("tudo × x", "b", 54, COR), XE, 490, passo=0.08)
        linha_cols(c, t, c0 + 0.4, ("x^3", "+ 2x^2", "+ x", ""), 500, 96)
        E.frase(c, t, d0, ps("tudo × 1", "b", 54, COR), XE, 620, passo=0.08)
        linha_cols(c, t, d0 + 0.4, ("", "+ x^2", "+ 2x", "+ 1"), 620, 96)
        q = ep(t, a1, 0.5)
        if q > 0:
            M.line(c, 460, 665, lerp(460, 1680, q), 665, TINTA, 1.0, 5)
        linha_cols(c, t, a1 + 0.2, ("x^3", "+ 3x^2", "+ 3x", "+ 1"), 780, 110, CERTO)
        for xc, k in ((COLS[1], 0), (COLS[2], 0.2)):
            E.foco(c, t, a1 + 0.2 + k, 0.4, lambda p, xc=xc: M.rrect(c, xc - 120, 440, 240, 380, 30, E.COR, 0.08 * p))
        E.frase(c, t, b1 - 0.6, ps("com 10:", "i", 56, TINTA2), XE, 925, passo=0.1)
        form(c, t, b1, "11^3 = 1.331", XE + 230, 930, 76)
        T = "1.000 + 300 + 30 + 1 = 1.331"
        form(c, t, c1, T, XE + 230, 1035, 76)
        E.foco(c, t, entre(c1, C["s12"], 0.75), 0.45, lambda p: E.selo(c, XE + 230 + fw(T, 76) + 70, 1005, 38, True, p))
    fase(c, t, C["s10"], C["s12"] - 0.1, s1011)

    a2, b2 = C["s12.a"], C["s12.b"]

    def s12():
        G = "(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3"
        E.frase(c, t, C["s12"] + 0.2, ps("com quaisquer termos", "i", 76), XE, 190, passo=0.1)
        s, y = 110, 420
        form(c, t, a2, G, W / 2, y, s, None, "center")
        notas = (("a^3", "cubo do 1º"), ("3a^2b", "3 × 1º^2 × 2º"), ("3ab^2", "3 × 1º × 2º^2"), ("b^3", "cubo do 2º"))
        for k, (tr, nota) in enumerate(notas):
            xx, ww = trecho_x(G, tr, W / 2, s, "center")
            tk = entre(a2, b2, 0.12 + 0.17 * k)
            realce(c, t, tk, G, tr, W / 2, y, s, align="center")
            E.foco(c, t, tk, 0.4, lambda p, xx=xx, ww=ww, nota=nota, k=k: E.formula(c, nota, xx + ww / 2, y + 95 + (k % 2) * 62, 48, "i", COR, p, "center"))
        E.frase(c, t, b2 - 0.8, ps("não precisa decorar:", "i", 66, TINTA2), W / 2, 760, "center", 0.1)
        E.foco(c, t, b2, 0.5, lambda p: E.pilula(c, "o quadrado × mais um parêntese", W / 2, 900, 70, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    fase(c, t, C["s12"], 1e9, s12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s13.{k}"] for k in "abcde")
    E.frase(c, t, C["s13"] + 0.3, ps("o erro mais comum", "g", 80, ERRADO), XE, 170)
    E.frase(c, t, a_, ps("elevar cada termo ao cubo", "i", 66), XE, 270, passo=0.1)
    F = "(x + 1)^3 = x^3 + 1"
    form(c, t, b_, F, XE, 450, 120, ERRADO)
    if t >= b_ + 0.9:
        E.risco(c, XE - 10, 470, XE + fw(F, 120) + 10, 350, t, b_ + 0.9, largura=11)
    E.frase(c, t, c_ - 0.4, ps("com 10:", "i", 62, TINTA2), XE, 620, passo=0.1)
    form(c, t, c_, "1.001", XE + 260, 625, 100, ERRADO)
    E.foco(c, t, d_ - 0.3, 0.4, lambda p: E.escreve(c, "e o certo é", XE + 620, 615, 60, "i", TINTA, p))
    form(c, t, d_, "1.331", XE + 1000, 625, 100, CERTO)
    R = "x^3 + 3x^2 + 3x + 1"
    form(c, t, e_ - 0.3, R, W / 2, 860, 130, None, "center")
    realce(c, t, e_, R, "3x^2 + 3x", W / 2, 860, 130, ERRADO, "center")
    xx, ww = trecho_x(R, "3x^2 + 3x", W / 2, 130, "center")
    E.foco(c, t, e_ + 0.2, 0.45, lambda p: centro(c, "os termos do meio sumiram", xx + ww / 2, 990, 56, "i", ERRADO, p))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4, e4, f4 = (C[f"s14.{k}"] for k in "abcdef")

    def s14():
        E.frase(c, t, C["s14"] + 0.2, ps("agora, o atalho", "i", 76, CLARO), XE, 160, passo=0.1)
        E.frase(c, t, a4, ps("números à mesma distância de um redondo", "i", 62, CLARO), XE, 250, passo=0.08)
        form(c, t, b4, "52 × 48", XE, 420, 130, BR)
        y = 600
        vx = E.reta(c, t, b4 + 0.4, 520, 1720, y, 46, 54, [48, 50, 52], escuro=True, size=52, tm=[b4 + 0.6, c4, b4 + 0.6])
        E.foco(c, t, c4, 0.45, lambda p: E.bola(c, vx(50), y, 22, AM, p))
        E.salto(c, t, d4, vx(50), vx(52), y - 10, 110, AM, "2")
        E.salto(c, t, d4 + 0.3, vx(50), vx(48), y - 10, 110, AM, "2")
        form(c, t, e4, "50^2 − 2^2", XE, 860, 110, BR)
        form(c, t, f4, "= 2.500 − 4 = 2.496", XE + fw("50^2 − 2^2 ", 110), 860, 110, AM)
    fase(c, t, C["s14"], C["s15"] - 0.1, s14)

    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]

    def s15():
        E.frase(c, t, C["s15"] + 0.2, ps("funciona porque é", "i", 76, CLARO) + ps("soma × diferença", "g", 72, BR), XE, 190, passo=0.1)
        form(c, t, a5, "52 × 48 = (50 + 2)(50 − 2)", XE, 400, 110, AM)
        E.foco(c, t, b5, 0.45, lambda p: E.selo(c, XE + 40, 620, 40, False, p))
        E.frase(c, t, b5, ps("não compensa:", "i", 64, CLARO) + ps("meio não redondo", "g", 64, BR), XE + 110, 640, passo=0.1)
        form(c, t, c5, "53 × 46", XE + 110, 830, 110, BR)
        E.foco(c, t, entre(c5, C["s16"], 0.55), 0.45, lambda p: E.escreve(c, "→ conta normal", XE + 600, 825, 72, "b", AM, p))
    fase(c, t, C["s15"], 1e9, s15)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_ = C["s16.a"], C["s16.b"]
    E.frase(c, t, C["s16"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, a_ - 0.3, 0.45, lambda p: num_bola(c, "1", XE + 40, 370, 40, 50, p))
    E.frase(c, t, a_ - 0.3, ps("escreva sem parênteses", "i", 66), XE + 110, 395, passo=0.1)
    form(c, t, a_, "(x + 4)(x − 4)", XE + 110, 560, 140, COR)
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "2", XE + 40, 720, 40, 50, p))
    E.frase(c, t, b_, ps("calcule de cabeça", "i", 62), XE + 110, 745, passo=0.1)
    form(c, t, b_ + 0.5, "34 × 26", XE + 110, 910, 140, COR)
    E.relogio(c, t, C["s17.a"], 1520, 470, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s18.{k}"] for k in "abcd")
    E.frase(c, t, C["s18"] + 0.2, ps("soma × diferença:", "i", 66, TINTA2), XE, 180, passo=0.1)
    form(c, t, a_ - 0.4, "(x + 4)(x − 4)", XE, 330, 110)
    form(c, t, a_, "= x^2 − 16", XE + fw("(x + 4)(x − 4) ", 110), 330, 110, CERTO)
    form(c, t, b_, "34 = 30 + 4", XE, 520, 100)
    form(c, t, c_, "26 = 30 − 4", 1000, 520, 100)
    E.foco(c, t, d_ - 0.6, 0.45, lambda p: E.pilula(c, "x = 30", XE + 150, 680, 64, estilo="g", a=p))
    form(c, t, d_, "900 − 16 = 884", XE, 880, 150, CERTO)
    E.foco(c, t, d_ + 1.0, 0.45, lambda p: E.selo(c, XE + fw("900 − 16 = 884", 150) + 110, 830, 56, True, p))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a1, b1 = C["s19.a"], C["s19.b"]

    def resumo():
        E.frase(c, t, C["s19"] + 0.2, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        E.foco(c, t, a1, 0.5, lambda p: num_bola(c, "1", 230, 430, 58, 66, p))
        E.frase(c, t, a1 + 0.1, ps("soma × diferença", "g", 74, COR), 320, 460, passo=0.12)
        form(c, t, a1 + 0.9, "(a + b)(a − b) = a^2 − b^2", 320, 590, 96)
        E.foco(c, t, b1, 0.5, lambda p: num_bola(c, "2", 230, 730, 58, 66, p))
        E.frase(c, t, b1 + 0.1, ps("cubo:", "g", 74, COR) + ps("o quadrado vezes mais um parêntese", "i", 70), 320, 760, passo=0.12)
        form(c, t, b1 + 0.9, "(a + b)^3 = (a + b)^2 · (a + b)", 320, 890, 96)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a_, b_, c_, d_ = (C[f"s20.{k}"] for k in "abcd")
    E.frase(c, t, C["s20"] + 0.2, ps("até aqui, você abriu parênteses", "i", 70, TINTA2), XE, 200, passo=0.1)
    E.frase(c, t, entre(C["s20"], a_, 0.55), ps("próxima aula: o caminho de volta", "i", 80), XE, 320, passo=0.11)
    E.frase(c, t, a_, ps("fatorar", "g", 110, COR), XE, 490)
    E.frase(c, t, a_ + 0.8, ps("colocando em evidência o que se repete", "i", 62), XE, 590, passo=0.09)
    form(c, t, b_, "6x^2 + 9x", XE, 780, 120)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(620, 375, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), 1450, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, soma=b_soma, regra=b_regra, cubo=b_cubo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
