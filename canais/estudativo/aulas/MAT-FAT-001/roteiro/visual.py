"""Visual — Estudativo · MAT-FAT-001: quadrado da soma e da diferença.
(x + 3)² aberto pelo chuveirinho; o piso quadrado de lado x + 3 cortado em x², duas faixas 3x e o quadradinho 9; a regra
(a + b)² = a² + 2ab + b² com o nome de cada pedaço; o menos só no meio; (2x + 1)²; o erro (3 + 4)² ≠ 9 + 16 com as faixas
que faltam; no palco, 101² e 99² de cabeça.

Linguagem visual da trilha Fatoração (vale para MAT-FAT-001 a 015):
- piso de lajotas como em MAT-EQU-005: o quadrado grande na cor da matéria com texto branco, as faixas em tom médio,
  o quadradinho em tom claro; lados rotulados por fora (à esquerda e em cima);
- o termo do meio (2ab) é o que a trilha protege: sempre com realce da cor da matéria;
- erro em vermelho com risco; acerto em verde com selo; atalho no palco escuro, resultado em amarelo.
Instantes: só os marcadores C[...] (as aulas desta trilha foram feitas antes da voz); falas sem marcador usam a
fração do trecho entre dois marcadores (entre()), para acompanhar qualquer ritmo de voz."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-001_quadrado_da_soma_e_da_diferenca.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("piso", "diferenca", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"

x = 10
assert (x + 3) ** 2 == x * x + 6 * x + 9 == 169 and x * x + 9 == 109
assert (x - 3) ** 2 == x * x - 6 * x + 9 == 49 == 100 - 60 + 9
assert (2 * x + 1) ** 2 == 4 * x * x + 4 * x + 1
assert (3 + 4) ** 2 == 49 and 9 + 16 == 25 and 2 * 3 * 4 == 24 == 49 - 25
assert 101 ** 2 == 10000 + 200 + 1 == 10201 and 99 ** 2 == 10000 - 200 + 1 == 9801
assert (x - 5) ** 2 == x * x - 10 * x + 25 and 95 ** 2 == 10000 - 1000 + 25 == 9025
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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s01.{k}"] for k in "abcd")

    def conta():
        form(c, t, a_, "(x + 3)^2", W / 2, 300, 190, COR, "center")
        form(c, t, b_, "= x^2 + 9 ?", W / 2, 560, 150, None, "center")
        E.foco(c, t, entre(b_, c_, 0.55), 0.45, lambda p: centro(c, "perdeu um pedaço", W / 2, 680, 62, "i", ERRADO, p))
        E.frase(c, t, c_ - 0.5, ps("com x = 10:", "i", 64, TINTA2), XE, 820, passo=0.1)
        form(c, t, c_, "13^2 = 169", XE, 960, 120, CERTO)
        E.foco(c, t, c_ + 0.5, 0.45, lambda p: E.selo(c, XE + fw("13^2 = 169", 120) + 80, 920, 46, True, p))
        form(c, t, d_, "100 + 9 = 109", 1080, 960, 120, ERRADO)
        if t >= d_ + 0.6:
            E.risco(c, 1060, 980, 1080 + fw("100 + 9 = 109", 120) + 20, 860, t, d_ + 0.6, largura=12)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2 = C["s02.a"], C["s02.b"]
    E.frase(c, t, a2, ps("até o fim desta aula, você", "i", 84), XE, 260, passo=0.12)
    E.frase(c, t, a2 + 1.0, ps("abre esse quadrado", "g", 96, COR), XE, 410, passo=0.13)
    E.frase(c, t, a2 + 2.0, ps("sem multiplicar tudo", "i", 90), XE, 540, passo=0.12)
    E.foco(c, t, b2 - 0.2, 0.7, lambda p: E.bola(c, 1450, 820, 200 * ease_back(prog(t, b2 - 0.2, 0.7))), blur=0)
    form(c, t, b2 + 0.2, "101^2", 1450, 830, 120, BR, "center")
    E.foco(c, t, b2 + 0.6, 0.5, lambda p: centro(c, "de cabeça", 1450, 900, 56, "i", BR, p))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_ = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, a_, ps("duas", "g", 84, COR) + ps("lembranças", "i", 90), XE, 180)
    xr = XE + 110
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "1", XE + 40, 360, 40, 50, p))
    E.frase(c, t, b_, ps("ao quadrado: o número vezes ele mesmo", "i", 66), xr, 385, passo=0.1)
    form(c, t, b_ + 0.8, "3^2 = 3 × 3 = 9", xr, 510, 100, COR)
    E.foco(c, t, c_, 0.45, lambda p: num_bola(c, "2", XE + 40, 660, 40, 50, p))
    E.frase(c, t, c_, ps("chuveirinho:", "g", 66, COR) + ps("cada termo multiplica cada termo do outro", "i", 60), xr, 685, passo=0.1)
    s = "(x + 2)(x + 3)"
    form(c, t, c_ + 0.5, s, xr + 20, 900, 100)
    chuveiro(c, t, (c_ + 1.0, c_ + 1.3, c_ + 1.6, c_ + 1.9), s, 900, 100, COR, "left", xr + 20, 34)
    E.frase(c, t, C["s04"] - 2.2, ps("faltou alguma? procure no canal", "i", 54, TINTA2), 1150, 900, passo=0.08)


# ---------------- abrir pelo chuveirinho ----------------
PROD = "(x + 3)(x + 3)"


def b_abrir(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s04.{k}"] for k in "abcde")
    s, y = 150, 400
    L = "(x + 3)^2 = "
    x0 = W / 2 - fw(L + PROD, s) / 2
    xp = x0 + fw(L, s)

    def s04():
        form(c, t, C["s04"] + 0.3, L, x0, y, s, COR)
        form(c, t, a4, PROD, xp, y, s)
        chuveiro(c, t, (b4, c4, d4, e4), PROD, y, s, COR, "left", xp, 60)
        for k, (f, tk) in enumerate((("x × x = x^2", b4), ("x × 3 = 3x", c4), ("3 × x = 3x", d4), ("3 × 3 = 9", e4))):
            form(c, t, tk + 0.3, f, 360 + (k % 2) * 700, 790 + (k // 2) * 150, 96)
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)

    a5, b5 = C["s05.a"], C["s05.b"]

    def s05():
        S1 = "x^2 + 3x + 3x + 9"
        form(c, t, C["s05"], S1, W / 2, 300, 110, TINTA2, "center")
        realce(c, t, b5, S1, "3x + 3x", W / 2, 300, 110, align="center")
        S2 = "= x^2 + 6x + 9"
        form(c, t, a5, S2, W / 2, 540, 160, CERTO, "center")
        tm = entre(a5, b5, 0.4)
        realce(c, t, tm, S2, "6x", W / 2, 540, 160, align="center")
        x6, w6 = trecho_x(S2, "6x", W / 2, 160, "center")
        E.foco(c, t, tm + 0.2, 0.45, lambda p: centro(c, "o pedaço que sumiu no gancho", x6 + w6 / 2, 680, 60, "i", COR, p))
        xa, wa = trecho_x(S1, "3x + 3x", W / 2, 110, "center")
        E.foco(c, t, b5 + 0.2, 0.45, lambda p: E.chave(c, xa, xa + wa, 170, COR, p, -22))
        E.foco(c, t, b5 + 0.3, 0.45, lambda p: centro(c, "dois termos iguais", xa + wa / 2, 130, 56, "i", COR, p))
        E.foco(c, t, b5 + 0.6, 0.5, lambda p: E.pilula(c, "3x + 3x = 6x", W / 2, 870, 70, estilo="g", a=p))
    fase(c, t, C["s05"], 1e9, s05)


# ---------------- piso ----------------
PX, PY, PA, PB = 280, 300, 420, 160
RX = 990


def b_piso(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s06.{k}"] for k in "abcd")
    E.frase(c, t, C["s06"] + 0.3, ps("no", "i", 76) + ps("piso,", "g", 76, COR) + ps("aparece na hora", "i", 76), XE, 170, passo=0.1)
    pin = (ep(t, b_, 0.5), ep(t, d_, 0.5), ep(t, d_ + 0.3, 0.5), ep(t, c_, 0.5))
    E.foco(c, t, a_, 0.5, lambda p: piso(c, PX, PY, PA, PB, p, rot=pin, pinta=pin))
    lados(c, t, a_ + 0.2, PX, PY, PA, PB)
    E.foco(c, t, a_ + 0.6, 0.45, lambda p: centro(c, "lado x + 3", PX + (PA + PB) / 2, PY + PA + PB + 80, 56, "i", TINTA2, p))
    linhas = (("x^2", "quadrado grande", b_, 380), ("9", "quadradinho 3 × 3", c_, 560), ("3x + 3x", "duas faixas iguais", d_, 740))
    for f, nota, tk, yy in linhas:
        form(c, t, tk, f, RX, yy, 110, COR if f != "x^2" else TINTA)
        E.frase(c, t, tk + 0.3, ps(nota, "i", 56, TINTA2), RX + fw(f, 110) + 40, yy - 8, passo=0.08)
    form(c, t, d_ + 1.4, "= x^2 + 6x + 9", RX, 940, 110, CERTO)


# ---------------- regra ----------------
REGRA = "(a + b)^2 = a^2 + 2ab + b^2"


def b_regra(c, t, C, b):
    a_, b_, c_, d_, e_, f_ = (C[f"s07.{k}"] for k in "abcdef")
    E.frase(c, t, C["s07"] + 0.3, ps("essa conta ganhou nome:", "i", 76), XE, 170, passo=0.1)
    E.frase(c, t, a_, ps("produto notável", "g", 84, COR), XE + 820, 175)
    E.frase(c, t, b_, ps("quadrado da soma", "i", 84), W / 2, 330, "center", 0.12)
    s, y = 140, 560
    x0 = W / 2 - fw(REGRA, s) / 2
    pecas = [("(a + b)^2 = ", b_ + 0.3, COR), ("a^2", c_), (" + 2ab", d_), (" + b^2", e_)]
    monta(c, t, pecas, x0, y, s)
    realce(c, t, d_ + 0.2, REGRA, "2ab", x0, y, s)
    for tr, nota, tk in (("a^2", "quadrado do 1º", c_), ("2ab", "2 × 1º × 2º", d_), ("b^2", "quadrado do 2º", e_)):
        xx, ww = trecho_x(REGRA, tr, x0, s)
        E.foco(c, t, tk + 0.3, 0.4, lambda p, xx=xx, ww=ww, nota=nota: centro(c, nota, xx + ww / 2, 680, 50, "i", COR, p))
    xa, wa = trecho_x(REGRA, "a", x0, s)
    xb, wb = trecho_x(REGRA, "b", x0, s)
    for xx, ww, nome, k, xr in ((xa, wa, "a = 1º termo", 0, XE), (xb, wb, "b = 2º termo", 0.5, XE + 560)):
        E.foco(c, t, f_ + k, 0.45, lambda p, xx=xx, ww=ww: E.chave(c, xx - 6, xx + ww + 6, y + 50, TINTA2, p, 20))
        E.foco(c, t, f_ + k + 0.2, 0.45, lambda p, nome=nome, xr=xr: E.escreve(c, nome, xr, 900, 64, "b", TINTA2, p))


# ---------------- diferença ----------------
def passos3(c, t, ts, linhas, x, y0, dy, size):
    """três linhas da regra: (rótulo itálico, conta) entrando nos instantes ts"""
    for k, ((rot, f), tk) in enumerate(zip(linhas, ts)):
        E.foco(c, t, tk, 0.45, lambda p, k=k: num_bola(c, str(k + 1), x + 30, y0 + k * dy - 30, 32, 40, p))
        E.frase(c, t, tk, ps(rot, "i", 58, TINTA2), x + 90, y0 + k * dy - 12, passo=0.08)
        form(c, t, tk + 0.6, f, x + 640, y0 + k * dy, 96)


def b_diferenca(c, t, C, b):
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")

    def s08():
        E.frase(c, t, C["s08"] + 0.2, ps("e com", "i", 80) + ps("menos?", "g", 80, COR), XE, 170, passo=0.12)
        form(c, t, a8, "(x − 3)^2", XE + 600, 175, 120, COR)
        passos3(c, t, (b8, c8, d8), (("quadrado do 1º", "x^2"), ("2 × 1º × 2º", "2 · x · (−3) = −6x"), ("quadrado do 2º", "(−3)^2 = +9")), XE, 380, 160, 96)
        E.foco(c, t, d8 + 1.6, 0.45, lambda p: E.escreve(c, "sinais iguais dão mais", XE + 640, 790, 50, "i", COR, p))
        E.frase(c, t, e8 - 0.5, ps("resultado:", "i", 70), XE, 960, passo=0.1)
        form(c, t, e8, "x^2 − 6x + 9", XE + 400, 970, 130, CERTO)
    fase(c, t, C["s08"], C["s09"] - 0.1, s08)

    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")

    def s09():
        R = "(a − b)^2 = a^2 − 2ab + b^2"
        E.frase(c, t, a9, ps("quadrado da diferença", "g", 84, COR), W / 2, 190, "center", 0.12)
        form(c, t, a9 + 0.5, R, W / 2, 400, 130, None, "center")
        realce(c, t, b9, R, "− 2ab", W / 2, 400, 130, align="center")
        realce(c, t, entre(b9, c9, 0.45), R, "+ b^2", W / 2, 400, 130, CERTO, "center")
        x1, w1 = trecho_x(R, "− 2ab", W / 2, 130, "center")
        x2, w2 = trecho_x(R, "+ b^2", W / 2, 130, "center")
        E.foco(c, t, b9 + 0.2, 0.45, lambda p: centro(c, "só o meio tem menos", x1 + w1 / 2, 530, 50, "i", COR, p))
        E.foco(c, t, entre(b9, c9, 0.45) + 0.2, 0.45, lambda p: centro(c, "sempre mais", x2 + w2 / 2, 600, 50, "i", CERTO, p))
        E.frase(c, t, c9 - 0.6, ps("teste com 10:", "i", 62, TINTA2), XE, 720, passo=0.1)
        form(c, t, c9, "(10 − 3)^2 = 7^2 = 49", XE + 440, 730, 92)
        form(c, t, d9, "100 − 60 + 9 = 49", XE + 440, 900, 92)
        E.foco(c, t, d9 + 1.2, 0.45, lambda p: E.selo(c, 1560, 820, 56, True, p))
    fase(c, t, C["s09"], 1e9, s09)


# ---------------- número na frente do x ----------------
def b_frente(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s10.{k}"] for k in "abcde")
    E.frase(c, t, C["s10"] + 0.3, ps("com número na frente do x", "g", 72, COR), XE, 170, passo=0.1)
    E.frase(c, t, entre(C["s10"], a_, 0.45), ps("o atalho de (x + a)(x + b) não serve; a regra serve", "i", 52, TINTA2), XE, 250, passo=0.07)
    form(c, t, a_, "(2x + 1)^2", XE + 1180, 175, 110, COR)
    passos3(c, t, (b_, c_, d_), (("quadrado do 1º", "2x · 2x = 4x^2"), ("2 × 1º × 2º", "2 · 2x · 1 = 4x"), ("quadrado do 2º", "1^2 = 1")), XE, 420, 160, 96)
    E.frase(c, t, e_ - 0.5, ps("fica:", "i", 70), XE, 960, passo=0.1)
    form(c, t, e_, "4x^2 + 4x + 1", XE + 220, 970, 130, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s11.{k}"] for k in "abcd")
    E.frase(c, t, C["s11"] + 0.3, ps("o erro mais comum", "g", 80, ERRADO), XE, 170)
    E.frase(c, t, a_, ps("elevar cada termo e somar", "i", 64), XE, 260, passo=0.1)
    form(c, t, a_ + 0.6, "(x + 3)^2 = x^2 + 9", XE, 400, 100, ERRADO)
    if t >= a_ + 1.4:
        E.risco(c, XE - 10, 420, XE + fw("(x + 3)^2 = x^2 + 9", 100) + 10, 320, t, a_ + 1.4, largura=10)
    E.frase(c, t, b_ - 0.4, ps("com números:", "i", 62, TINTA2), XE, 560, passo=0.1)
    form(c, t, b_, "(3 + 4)^2 = 7^2 = 49", XE, 690, 96, CERTO)
    form(c, t, c_, "3^2 + 4^2 = 9 + 16 = 25", XE, 830, 96, ERRADO)
    form(c, t, d_ + 0.3, "faltou 2 × 3 × 4 = 24", XE, 980, 90, COR)
    # piso 3 + 4: as faixas do meio somem no erro e voltam marcadas
    U = 62
    x0, y0 = 1260, 330
    falta = ep(t, c_ + 0.4, 0.5) * (1 - ep(t, d_, 0.5))
    pin = (1, ep(t, d_, 0.5), ep(t, d_ + 0.2, 0.5), 1)
    rot = (1, ep(t, d_ + 0.3, 0.4), ep(t, d_ + 0.5, 0.4), 1)
    E.foco(c, t, b_ + 0.4, 0.5, lambda p: piso(c, x0, y0, 3 * U, 4 * U, p, ("9", "3 × 4", "3 × 4", "16"), rot, pin, (0, falta, falta, 0), (64, 50, 50, 64)))
    lados(c, t, b_ + 0.6, x0, y0, 3 * U, 4 * U, "3", "4", size=56)
    E.foco(c, t, d_ + 0.2, 0.45, lambda p: centro(c, "as duas faixas do meio", x0 + 3.5 * U, y0 + 7 * U + 80, 52, "i", COR, p))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2, e2, f2 = (C[f"s12.{k}"] for k in "abcdef")
    XL, XR = XE, 820

    def s12():
        E.frase(c, t, C["s12"] + 0.2, ps("agora, o atalho:", "i", 76, CLARO), XL, 170, passo=0.1)
        form(c, t, a2, "101^2", XL + 620, 180, 110, BR)
        E.foco(c, t, a2 + 0.4, 0.45, lambda p: E.escreve(c, "de cabeça", XL + 950, 170, 60, "i", CLARO, p))
        form(c, t, b2, "101 = 100 + 1", XL, 360, 100, AM)
        for k, (rot, f, tk) in enumerate((("quadrado do 1º", "100^2 = 10.000", c2), ("2 × 1º × 2º", "2 × 100 × 1 = 200", d2), ("quadrado do 2º", "1^2 = 1", e2))):
            E.frase(c, t, tk, ps(rot, "i", 56, CLARO), XL, 520 + k * 130, passo=0.08)
            form(c, t, tk + 0.4, f, XR, 525 + k * 130, 90, BR)
        E.frase(c, t, f2 - 0.4, ps("total:", "i", 70, CLARO), XL, 960, passo=0.1)
        form(c, t, f2, "10.201", XR, 975, 150, AM)
    fase(c, t, C["s12"], C["s13"] - 0.1, s12)

    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]

    def s13():
        E.frase(c, t, C["s13"] + 0.2, ps("com menos, também", "i", 76, CLARO), XL, 200, passo=0.1)
        form(c, t, a3, "99^2", XL, 400, 130, BR)
        form(c, t, a3 + 0.5, "99 = 100 − 1", XL + 420, 400, 100, AM)
        form(c, t, b3, "10.000 − 200 + 1", XL, 620, 110, BR)
        form(c, t, c3, "= 9.801", XL, 840, 150, AM)
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)

    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]

    def s14():
        E.frase(c, t, C["s14"] + 0.2, ps("funciona porque", "i", 80, CLARO), XL, 180, passo=0.1)
        E.frase(c, t, a4, ps("o redondo", "g", 70, BR) + ps("é fácil de elevar ao quadrado", "i", 66, CLARO), XL, 320, passo=0.1)
        E.frase(c, t, entre(a4, b4, 0.55), ps("o resto", "g", 70, BR) + ps("é conta pequena", "i", 66, CLARO), XL, 430, passo=0.1)
        E.foco(c, t, b4, 0.45, lambda p: E.selo(c, XL + 40, 600, 40, True, p))
        E.frase(c, t, b4, ps("perto de um redondo:", "i", 62, CLARO), XL + 110, 620, passo=0.1)
        form(c, t, b4 + 1.2, "95 = 100 − 5", XL + 760, 625, 90, AM)
        E.foco(c, t, c4, 0.45, lambda p: E.selo(c, XL + 40, 800, 40, False, p))
        E.frase(c, t, c4, ps("longe dele:", "i", 62, CLARO) + ps("conta armada", "g", 66, BR), XL + 110, 820, passo=0.1)
    fase(c, t, C["s14"], 1e9, s14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_ = C["s15.a"], C["s15.b"]
    E.frase(c, t, C["s15"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, a_ - 0.3, 0.45, lambda p: num_bola(c, "1", XE + 40, 370, 40, 50, p))
    E.frase(c, t, a_ - 0.3, ps("escreva sem parênteses", "i", 66), XE + 110, 395, passo=0.1)
    form(c, t, a_, "(x − 5)^2", XE + 110, 560, 150, COR)
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "2", XE + 40, 720, 40, 50, p))
    E.frase(c, t, b_, ps("use o resultado e calcule de cabeça", "i", 62), XE + 110, 745, passo=0.1)
    form(c, t, b_ + 0.5, "95^2", XE + 110, 910, 150, COR)
    E.relogio(c, t, C["s16.a"], 1520, 470, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")

    def s17():
        form(c, t, C["s17"] + 0.2, "(x − 5)^2", XE, 200, 120, COR)
        passos3(c, t, (a7, b7, c7), (("quadrado do 1º", "x^2"), ("2 × 1º × 2º", "2 · x · (−5) = −10x"), ("quadrado do 2º", "(−5)^2 = +25")), XE, 400, 160, 96)
        E.frase(c, t, d7 - 0.5, ps("resposta:", "i", 70), XE, 960, passo=0.1)
        form(c, t, d7, "x^2 − 10x + 25", XE + 380, 970, 130, CERTO)
    fase(c, t, C["s17"], C["s18"] - 0.1, s17)

    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]

    def s18():
        form(c, t, C["s18"] + 0.2, "95^2", XE, 220, 130, COR)
        form(c, t, a8, "95 = 100 − 5", XE + 380, 220, 100)
        E.foco(c, t, a8 + 0.8, 0.45, lambda p: E.pilula(c, "x = 100", 1500, 190, 64, estilo="g", a=p))
        form(c, t, a8 + 0.9, "x^2 − 10x + 25", XE, 420, 90, TINTA2)
        form(c, t, b8, "10.000 − 1.000 + 25", XE, 600, 120)
        form(c, t, c8, "= 9.025", XE, 830, 160, CERTO)
        E.foco(c, t, c8 + 0.5, 0.45, lambda p: E.selo(c, XE + fw("= 9.025", 160) + 110, 780, 56, True, p))
    fase(c, t, C["s18"], 1e9, s18)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s19.{k}"] for k in "abcd")

    def resumo():
        E.frase(c, t, C["s19"] + 0.2, ps("resumindo", "i", 96, COR), W / 2, 210, "center")
        s, y = 130, 470
        x0 = W / 2 - fw(REGRA, s) / 2
        monta(c, t, [("(a + b)^2 = ", C["s19"] + 0.4, COR), ("a^2", a1), (" + 2ab", b1), (" + b^2", c1)], x0, y, s)
        realce(c, t, d1, REGRA, "2ab", x0, y, s)
        for tr, nota, tk, n in (("a^2", "quadrado do 1º", a1, 0), ("2ab", "2 × 1º × 2º", b1, 0), ("b^2", "quadrado do 2º", c1, 0)):
            xx, ww = trecho_x(REGRA, tr, x0, s, n=n)
            E.foco(c, t, tk + 0.2, 0.4, lambda p, xx=xx, ww=ww, nota=nota: centro(c, nota, xx + ww / 2, 590, 50, "i", COR, p))
        E.foco(c, t, d1, 0.5, lambda p: E.pilula(c, "o termo do meio nunca some", W / 2, 800, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a_, b_, c_, d_ = (C[f"s20.{k}"] for k in "abcd")
    E.frase(c, t, C["s20"] + 0.2, ps("próxima aula", "i", 84), XE, 230)
    E.frase(c, t, a_, ps("soma × diferença", "g", 96, COR), XE, 380, passo=0.12)
    form(c, t, a_ + 1.0, "(x + 5)(x − 5)", XE, 510, 96)
    E.frase(c, t, b_, ps("cubo de uma soma", "g", 96, COR), XE, 680, passo=0.12)
    form(c, t, b_ + 0.6, "(a + b)^3", XE, 810, 96)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(620, 375, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), 1450, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, abrir=b_abrir, piso=b_piso, regra=b_regra, diferenca=b_diferenca,
              frente=b_frente, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
