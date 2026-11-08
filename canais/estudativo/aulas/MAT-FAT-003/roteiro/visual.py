"""Visual — Estudativo · MAT-FAT-003: fatorar com produtos notáveis.
x² − 49 lido de trás para a frente: cada termo ganha embaixo o que foi elevado ao quadrado (x · x, 7 · 7) e vira
(x + 7)(x − 7); o trinômio x² + 6x + 9 com a conferência do meio e o piso quadrado de lado x + 3 (o de MAT-FAT-001);
o meio que não bate; o fator comum antes de tudo (convenção evid() da trilha); o erro (x − 7)²; no palco, 1.001² − 999².
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-003_fatorar_com_produtos_notaveis.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("diferenca", "trinomio", "primeiro", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"

x = 10
assert 1001 ** 2 - 999 ** 2 == (1001 + 999) * (1001 - 999) == 2000 * 2 == 4000
assert (x + 7) * (x - 7) == x * x - 49 == 51 and (x - 7) ** 2 == 9 == x * x - 14 * x + 49
assert 4 * x * x - 25 == (2 * x + 5) * (2 * x - 5)
assert x * x + 6 * x + 9 == (x + 3) ** 2 and x * x - 10 * x + 25 == (x - 5) ** 2 and x * x + 5 * x + 9 != (x + 3) ** 2
assert 2 * x * x - 50 == 2 * (x * x - 25) == 2 * (x + 5) * (x - 5)
assert 3 * x * x - 12 == 3 * (x * x - 4) == 3 * (x + 2) * (x - 2) == 288 == 300 - 12 == 3 * 12 * 8
assert 5 ** 2 - 3 ** 2 == 25 - 9
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
    """piso de lado A + B (em pixels; B = (Bw, Bh) faz o piso retangular A + Bw por A + Bh): quadrado grande A×A, faixa A×B à direita, faixa B×A embaixo, quadradinho B×B.
    rot = alfa do nome de cada pedaço; pinta = quanto cada pedaço já tem a sua cor; falta = pedaço que sumiu (contorno vermelho tracejado)"""
    if a <= 0:
        return
    Bw, Bh = B if isinstance(B, tuple) else (B, B)
    vazio = M.mix(E.COR, BR, 0.88) if not escuro else M.mix(E.COR, "#07070F", 0.5)
    pedacos = ((0, 0, A, A), (A, 0, Bw, A), (0, A, A, Bh), (A, A, Bw, Bh))
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


def lados(c, t, ta, x0, y0, A, B, la="x", lb="3", cor=None, size=64, lb2=None):
    """rótulos dos lados do piso: la + lb à esquerda, la + lb2 em cima (lb2 = lb no quadrado; B = (Bw, Bh) no retangular)"""
    cor = cor or COR
    Bw, Bh = B if isinstance(B, tuple) else (B, B)
    lb2 = lb2 or lb
    E.foco(c, t, ta, 0.45, lambda p: (E.formula(c, la, x0 - 46, y0 + A / 2 + size * 0.36, size, cor=cor, a=p, align="center"),
                                     E.formula(c, lb, x0 - 46, y0 + A + Bh / 2 + size * 0.36, size, cor=cor, a=p, align="center"),
                                     E.formula(c, la, x0 + A / 2, y0 - 28, size, cor=cor, a=p, align="center"),
                                     E.formula(c, lb2, x0 + A + Bw / 2, y0 - 28, size, cor=cor, a=p, align="center")))


def evid(c, t, t0, fator, dentro, x, y, size, align="left", t1=None, cor=None):
    """colocar em evidência (convenção da trilha): o fator comum na cor da matéria, na frente; o parêntese com o que
    sobrou de cada termo entra depois (t1). Devolve o x inicial"""
    s = fator + "(" + dentro + ")"
    x0 = x - fw(s, size) / 2 if align == "center" else x
    form(c, t, t0, fator, x0, y, size, COR)
    form(c, t, t1 if t1 is not None else t0 + 0.4, "(" + dentro + ")", x0 + fw(fator, size), y, size, cor)
    return x0


def arco_d(c, t, t0, s, de, ate_, x, y, size, alto, cor=None, align="left", n=0, rotulo=None):
    """arco com seta do fator de fora até um termo de dentro (distributiva, como em MAT-EQU-004)"""
    x0, w0 = trecho_x(s, de, x, size, align)
    x1, w1 = trecho_x(s, ate_, x, size, align, n)
    E.salto(c, t, t0, x0 + w0 / 2, x1 + w1 / 2, y - size * 0.95, alto, cor or COR, rotulo, size=46)


def sob(c, t, t0, s, trecho, x, y, size, nota, cor=None, align="left", n=0, dy=None, size_n=None, est="g"):
    """nota embaixo de um trecho da fórmula: o que foi elevado ao quadrado"""
    xx, ww = trecho_x(s, trecho, x, size, align, n)
    sn = size_n or size * 0.5
    E.foco(c, t, t0, 0.45, lambda p: E.formula(c, nota, xx + ww / 2, y + (dy or size * 0.75), sn, est, cor or COR, p, "center"))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def conta():
        s = "1.001^2 − 999^2"
        x0 = W / 2 - fw(s, 180) / 2
        form(c, t, a_, "1.001^2", x0, 360, 180, COR)
        form(c, t, b_, " − 999^2", x0 + fw("1.001^2", 180), 360, 180, COR)
        E.frase(c, t, entre(b_, c_, 0.35), ps("parece conta de calculadora", "i", 70, TINTA2), W / 2, 540, "center", 0.1)
        form(c, t, c_, "= 4.000", W / 2, 800, 200, CERTO, "center")
        E.foco(c, t, c_ + 0.8, 0.45, lambda p: centro(c, "de cabeça", W / 2, 940, 66, "i", COR, p))
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2 = C["s02.a"], C["s02.b"]
    E.frase(c, t, a2, ps("até o fim desta aula, você", "i", 84), XE, 260, passo=0.12)
    E.frase(c, t, a2 + 1.0, ps("fatora com os", "i", 90) + ps("produtos notáveis", "g", 90, COR), XE, 410, passo=0.13)
    E.foco(c, t, b2 - 0.2, 0.7, lambda p: E.bola(c, 1450, 800, 210 * ease_back(prog(t, b2 - 0.2, 0.7))), blur=0)
    E.foco(c, t, b2 + 0.2, 0.5, lambda p: (centro(c, "atalho", 1450, 760, 60, "i", BR, p),
                                          E.formula(c, "1.001^2 − 999^2", 1450, 850, 56, cor=BR, a=p, align="center")))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s03.{k}"] for k in "abcd")
    E.frase(c, t, a_, ps("três", "g", 84, COR) + ps("ferramentas", "i", 90), XE, 180)
    xr = XE + 110
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "1", XE + 40, 370, 40, 50, p))
    form(c, t, b_ + 0.2, "(a ± b)^2 = a^2 ± 2ab + b^2", xr, 400, 96)
    E.foco(c, t, c_, 0.45, lambda p: num_bola(c, "2", XE + 40, 590, 40, 50, p))
    form(c, t, c_ + 0.2, "(a + b)(a − b) = a^2 − b^2", xr, 620, 96)
    E.foco(c, t, d_, 0.45, lambda p: num_bola(c, "3", XE + 40, 810, 40, 50, p))
    E.frase(c, t, d_ + 0.1, ps("em evidência:", "g", 60, COR), xr, 830, passo=0.1)
    form(c, t, d_ + 0.5, "6x^2 + 9x =", xr + 440, 840, 90)
    evid(c, t, d_ + 0.8, "3x", "2x + 3", xr + 440 + fw("6x^2 + 9x = ", 90), 840, 90)
    E.frase(c, t, C["s04"] - 2.2, ps("faltou alguma? procure no canal", "i", 54, TINTA2), XE, 1000, passo=0.08)


# ---------------- diferença de dois quadrados ----------------
D49 = "x^2 − 49"


def b_diferenca(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]

    def s04():
        E.frase(c, t, C["s04"] + 0.2, ps("pela soma × diferença", "i", 76, TINTA2), XE, 200, passo=0.1)
        L = "(x + 7)(x − 7) = x^2 − 49"
        x0 = W / 2 - fw(L, 140) / 2
        form(c, t, a4, "(x + 7)(x − 7)", x0, 520, 140)
        form(c, t, b4, " = x^2 − 49", x0 + fw("(x + 7)(x − 7)", 140), 520, 140)
        xa, wa = trecho_x(L, "(x + 7)(x − 7)", x0, 140)
        xb, wb = trecho_x(L, "x^2 − 49", x0, 140)
        flecha(c, t, c4, xb + wb / 2, 580, xa + wa / 2, 580, -170, COR, 0.8, 7)
        E.foco(c, t, c4 + 0.6, 0.45, lambda p: centro(c, "fatorar: de trás para a frente", W / 2, 860, 70, "b", COR, p))
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)

    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")

    def s05():
        s, y = 170, 380
        x0 = W / 2 - fw(D49, s) / 2
        form(c, t, a5, D49, x0, y, s)
        realce(c, t, b5, D49, "x^2", x0, y, s)
        realce(c, t, b5 + 0.3, D49, "49", x0, y, s)
        realce(c, t, b5 + 0.8, D49, "−", x0, y, s, ERRADO)
        E.foco(c, t, b5 + 0.2, 0.45, lambda p: centro(c, "dois quadrados, com menos entre eles", W / 2, 160, 60, "i", COR, p))
        sob(c, t, c5, D49, "x^2", x0, y, s, "x · x", dy=140, size_n=80)
        sob(c, t, d5, D49, "49", x0, y, s, "7 · 7", dy=140, size_n=80)
        E.frase(c, t, e5 - 0.4, ps("então:", "i", 70), XE, 830, passo=0.1)
        form(c, t, e5, "x^2 − 49 = (x + 7)(x − 7)", XE + 260, 840, 120, CERTO)
    fase(c, t, C["s05"], C["s06"] - 0.1, s05)

    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")

    def s06():
        E.frase(c, t, a6, ps("diferença de dois quadrados", "g", 76, COR), XE, 180, passo=0.1)
        form(c, t, a6 + 0.6, "a^2 − b^2 = (a + b)(a − b)", XE, 300, 84)
        E.foco(c, t, b6, 0.45, lambda p: num_bola(c, "1", XE + 30, 410, 30, 40, p))
        E.frase(c, t, b6, ps("descubra o que foi elevado ao quadrado", "i", 54), XE + 80, 428, passo=0.08)
        E.foco(c, t, c6, 0.45, lambda p: num_bola(c, "2", XE + 30, 500, 30, 40, p))
        E.frase(c, t, c6, ps("escreva a soma × a diferença", "i", 54), XE + 80, 518, passo=0.08)
        s, y = 120, 740
        Q = "4x^2 − 25"
        form(c, t, d6, Q, XE, y, s)
        sob(c, t, entre(d6, e6, 0.3), Q, "4x^2", XE, y, s, "2x · 2x", dy=120, size_n=70)
        sob(c, t, entre(d6, e6, 0.65), Q, "25", XE, y, s, "5 · 5", dy=120, size_n=70)
        form(c, t, e6, "= (2x + 5)(2x − 5)", XE + fw(Q + " ", s), y, s, CERTO)
    fase(c, t, C["s06"], 1e9, s06)


# ---------------- trinômio quadrado perfeito ----------------
T9 = "x^2 + 6x + 9"
PX, PY, PA, PB = 1430, 330, 280, 110


def b_trinomio(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")

    def s07():
        s, y = 170, 330
        x0 = W / 2 - fw(T9, s) / 2
        E.frase(c, t, C["s07"] + 0.2, ps("agora, três termos", "i", 76, TINTA2), XE, 150, passo=0.1)
        form(c, t, a7, T9, x0, y, s)
        E.foco(c, t, b7, 0.45, lambda p: E.pilula(c, "3 termos = trinômio", 1600, 140, 56, estilo="g", a=p))
        sob(c, t, c7, T9, "x^2", x0, y, s, "x · x", dy=130, size_n=76)
        sob(c, t, d7, T9, "9", x0, y, s, "3 · 3", dy=130, size_n=76)
        realce(c, t, entre(d7, e7, 0.6), T9, "6x", x0, y, s)
        E.foco(c, t, entre(d7, e7, 0.6), 0.45, lambda p: E.formula(c, "?", trecho_x(T9, "6x", x0, s)[0] + trecho_x(T9, "6x", x0, s)[1] / 2, y + 130 + 30, 76, cor=COR, a=p * (1 - ep(t, e7, 0.3)), align="center"))
        E.frase(c, t, e7 - 0.4, ps("o meio:", "i", 70), XE, 760, passo=0.1)
        form(c, t, e7, "2 · x · 3 = 6x", XE + 280, 770, 120, COR)
        E.foco(c, t, e7 + 1.2, 0.45, lambda p: E.selo(c, XE + 280 + fw("2 · x · 3 = 6x", 120) + 90, 730, 52, True, p))
    fase(c, t, C["s07"], C["s08"] - 0.1, s07)

    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")

    def s08():
        E.frase(c, t, a8, ps("trinômio quadrado perfeito", "g", 76, COR), XE, 180, passo=0.1)
        E.frase(c, t, a8 + 1.0, ps("o quadrado de uma soma", "i", 64), XE, 270, passo=0.1)
        form(c, t, b8 - 0.3, T9, XE, 470, 110)
        form(c, t, b8, "= (x + 3)^2", XE + fw(T9 + " ", 110), 470, 110, CERTO)
        E.frase(c, t, c8 - 0.6, ps("com menos no meio:", "i", 60, TINTA2), XE, 640, passo=0.1)
        form(c, t, c8, "x^2 − 10x + 25", XE, 780, 110)
        form(c, t, d8, "= (x − 5)^2", XE + fw("x^2 − 10x + 25 ", 110), 780, 110, CERTO)
        q = ep(t, b8 + 0.4, 0.5)
        E.foco(c, t, b8 + 0.4, 0.5, lambda p: piso(c, PX, PY, PA, PB, p, rot=(1, 1, 1, 1)))
        lados(c, t, b8 + 0.6, PX, PY, PA, PB)
    fase(c, t, C["s08"], C["s09"] - 0.1, s08)

    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]

    def s09():
        E.frase(c, t, C["s09"] + 0.2, ps("e se o meio", "i", 76) + ps("não bater?", "g", 76, ERRADO), XE, 180, passo=0.1)
        Q = "x^2 + 5x + 9"
        s, y = 150, 400
        form(c, t, a9, Q, XE, y, s)
        form(c, t, entre(a9, b9, 0.45), "2 · x · 3 = 6x", XE, 600, 100, COR)
        realce(c, t, b9, Q, "5x", XE, y, s, ERRADO)
        form(c, t, b9 + 0.3, "6x ≠ 5x", 1000, 600, 100, ERRADO)
        E.foco(c, t, c9, 0.45, lambda p: E.selo(c, XE + 40, 790, 40, False, p))
        E.frase(c, t, c9, ps("não é quadrado perfeito", "g", 70, ERRADO), XE + 110, 815, passo=0.1)
        E.foco(c, t, entre(c9, C["s10"], 0.5), 0.5, lambda p: E.pilula(c, "confira sempre o meio", W / 2, 960, 66, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    fase(c, t, C["s09"], 1e9, s09)


# ---------------- fator comum antes ----------------
def b_primeiro(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s10.{k}"] for k in "abcd")
    E.foco(c, t, a_, 0.5, lambda p: E.pilula(c, "antes de tudo: fator comum", W / 2, 180, 72, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    Q = "2x^2 − 50"
    form(c, t, b_, Q, XE, 420, 140)
    E.foco(c, t, entre(b_, c_, 0.4), 0.45, lambda p: E.escreve(c, "50 não é quadrado de inteiro", XE + 720, 400, 56, "i", ERRADO, p))
    realce(c, t, c_, Q, "2", XE, 420, 140)
    realce(c, t, c_ + 0.2, Q, "50", XE, 420, 140)
    E.frase(c, t, c_ - 0.2, ps("o 2 é comum:", "i", 64, TINTA2), XE, 590, passo=0.1)
    evid(c, t, c_ + 0.6, "2", "x^2 − 25", XE + 440, 600, 120, t1=c_ + 1.2)
    E.frase(c, t, d_ - 0.4, ps("aí sim:", "i", 64, TINTA2), XE, 820, passo=0.1)
    form(c, t, d_, "2", XE + 260, 830, 130, COR)
    form(c, t, d_ + 0.4, "(x + 5)(x − 5)", XE + 260 + fw("2", 130), 830, 130, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s11.{k}"] for k in "abcde")
    E.frase(c, t, C["s11"] + 0.3, ps("o erro mais comum", "g", 80, ERRADO), XE, 170)
    E.frase(c, t, a_, ps("diferença de quadrados", "i", 60) + ps("≠", "g", 60, ERRADO) + ps("quadrado da diferença", "i", 60), XE, 260, passo=0.1)
    F = "x^2 − 49 = (x − 7)^2"
    form(c, t, b_, F, XE, 440, 120, ERRADO)
    if t >= b_ + 0.9:
        E.risco(c, XE - 10, 460, XE + fw(F, 120) + 10, 340, t, b_ + 0.9, largura=11)
    E.frase(c, t, c_ - 0.4, ps("com 10:", "i", 60, TINTA2), XE, 600, passo=0.1)
    form(c, t, c_, "100 − 49 = 51", XE + 250, 605, 90, CERTO)
    form(c, t, d_, "(10 − 7)^2 = 9", 1050, 605, 90, ERRADO)
    R = "(x − 7)^2 = x^2 − 14x + 49"
    form(c, t, e_, R, XE, 850, 110)
    realce(c, t, e_ + 0.5, R, "− 14x", XE, 850, 110, ERRADO)
    xx, ww = trecho_x(R, "− 14x", XE, 110)
    E.foco(c, t, e_ + 0.7, 0.45, lambda p: centro(c, "tem termo do meio", xx + ww / 2, 960, 54, "i", ERRADO, p))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2, e2, f2 = (C[f"s12.{k}"] for k in "abcdef")

    def s12():
        E.frase(c, t, C["s12"] + 0.2, ps("o atalho, que é o gancho", "i", 70, CLARO), XE, 160, passo=0.1)
        form(c, t, a2, "1.001^2 − 999^2", XE, 330, 120, BR)
        E.foco(c, t, b2, 0.45, lambda p: E.escreve(c, "diferença de dois quadrados", XE + 1000, 320, 52, "i", AM, p))
        form(c, t, c2, "= (1.001 + 999)(1.001 − 999)", XE, 500, 100, BR)
        form(c, t, d2, "1.001 + 999 = 2.000", XE, 680, 86, CLARO)
        form(c, t, e2, "1.001 − 999 = 2", 1060, 680, 86, CLARO)
        form(c, t, f2, "2.000 × 2 = 4.000", XE, 900, 140, AM)
    fase(c, t, C["s12"], C["s13"] - 0.1, s12)

    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]

    def s13():
        E.frase(c, t, C["s13"] + 0.2, ps("funciona porque", "i", 76, CLARO), XE, 180, passo=0.1)
        E.frase(c, t, a3, ps("dois quadrados enormes", "g", 64, BR), XE, 300, passo=0.08)
        E.frase(c, t, a3 + 0.8, ps("viram uma soma e uma subtração fáceis", "i", 62, CLARO), XE, 390, passo=0.08)
        E.foco(c, t, b3, 0.45, lambda p: E.selo(c, XE + 40, 560, 40, False, p))
        E.frase(c, t, b3, ps("soma de quadrados não vira:", "i", 62, CLARO), XE + 110, 580, passo=0.1)
        form(c, t, b3 + 0.8, "a^2 + b^2", XE + 960, 585, 90, BR)
        E.foco(c, t, c3, 0.45, lambda p: E.selo(c, XE + 40, 750, 40, False, p))
        E.frase(c, t, c3, ps("números pequenos:", "i", 62, CLARO), XE + 110, 770, passo=0.1)
        form(c, t, c3 + 0.6, "5^2 − 3^2 = 25 − 9", XE + 700, 775, 90, BR)
        E.foco(c, t, entre(c3, C["s14"], 0.6), 0.45, lambda p: E.escreve(c, "a conta direta já é rápida", XE + 110, 910, 62, "b", AM, p))
    fase(c, t, C["s13"], 1e9, s13)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_ = C["s14.a"]
    E.frase(c, t, C["s14"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 220)
    E.frase(c, t, a_ - 0.4, ps("fatore até o fim", "i", 100), XE, 450)
    form(c, t, a_, "3x^2 − 12", XE, 700, 160, COR)
    E.relogio(c, t, C["s15.a"], 1520, 420, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]

    def s16():
        E.frase(c, t, C["s16"] + 0.2, ps("primeiro, o fator comum", "i", 70, TINTA2), XE, 180, passo=0.1)
        form(c, t, a6 - 0.3, "3x^2 − 12 =", XE, 360, 120)
        evid(c, t, a6, "3", "x^2 − 4", XE + fw("3x^2 − 12 = ", 120), 360, 120, t1=a6 + 0.5)
        sob(c, t, b6, "3(x^2 − 4)", "4", XE + fw("3x^2 − 12 = ", 120), 360, 120, "2 · 2", dy=100, size_n=60)
        E.frase(c, t, b6 - 0.3, ps("dentro, diferença de quadrados", "i", 58, TINTA2), XE, 560, passo=0.08)
        E.frase(c, t, c6 - 0.5, ps("resposta:", "i", 72), XE, 800, passo=0.1)
        form(c, t, c6, "3", XE + 360, 810, 140, COR)
        form(c, t, c6 + 0.4, "(x + 2)(x − 2)", XE + 360 + fw("3", 140), 810, 140, CERTO)
    fase(c, t, C["s16"], C["s17"] - 0.1, s16)

    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]

    def s17():
        E.frase(c, t, C["s17"] + 0.2, ps("confira com 10:", "i", 70, TINTA2), XE, 180, passo=0.1)
        form(c, t, a7, "300 − 12 = 288", XE, 380, 110)
        form(c, t, b7, "3 × 12 × 8 = 288", XE, 560, 110, CERTO)
        E.foco(c, t, b7 + 0.8, 0.45, lambda p: E.selo(c, XE + fw("3 × 12 × 8 = 288", 110) + 90, 520, 50, True, p))
        form(c, t, c7, "3(x^2 − 4)", XE, 820, 110, TINTA2)
        E.foco(c, t, c7 + 0.3, 0.45, lambda p: E.pilula(c, "não terminou: ainda fatora", XE + 980, 790, 60, estilo="g", fundo=ERRADO, cor=BR, a=p))
    fase(c, t, C["s17"], 1e9, s17)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a8, b8 = C["s18.a"], C["s18.b"]

    def resumo():
        E.frase(c, t, C["s18"] + 0.2, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        E.foco(c, t, a8, 0.5, lambda p: num_bola(c, "1", 230, 430, 58, 66, p))
        E.frase(c, t, a8 + 0.1, ps("dois quadrados com menos:", "i", 72) + ps("soma × diferença", "g", 70, COR), 320, 460, passo=0.12)
        form(c, t, a8 + 1.0, "x^2 − 49 = (x + 7)(x − 7)", 320, 590, 90)
        E.foco(c, t, b8, 0.5, lambda p: num_bola(c, "2", 230, 730, 58, 66, p))
        E.frase(c, t, b8 + 0.1, ps("três termos, meio certo:", "i", 72) + ps("um quadrado", "g", 70, COR), 320, 760, passo=0.12)
        form(c, t, b8 + 1.0, "x^2 + 6x + 9 = (x + 3)^2", 320, 890, 90)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    a_, b_, c_, d_ = (C[f"s19.{k}"] for k in "abcd")
    E.frase(c, t, C["s19"] + 0.2, ps("próxima aula", "i", 84), XE, 230)
    E.frase(c, t, a_, ps("simplificar frações com letra", "g", 84, COR), XE, 380, passo=0.12)
    form(c, t, b_, "f{x^2 − 9}{x − 3}", XE + 40, 660, 140)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 600, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(890, 645, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), 1450, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, diferenca=b_diferenca, trinomio=b_trinomio, primeiro=b_primeiro,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
