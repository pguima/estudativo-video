"""Visual — Estudativo · MAT-FAT-002: fator comum e agrupamento.
Os três combos de MAT-EQU-004 lidos ao contrário (3x + 12 → 3(x + 4)); o método do fator comum (MDC dos números, menor
expoente das letras, dividir cada termo); o erro do 1 que some; agrupamento em pares com o parêntese repetido numa caixa
pontilhada; no palco, o atalho de tirar o sinal de menos junto; na resposta, os quatro pedaços do piso montados de volta.

Convenção da trilha para COLOCAR EM EVIDÊNCIA (evid()): o fator comum ganha realce da cor da matéria dentro de cada termo
e depois aparece na frente, na cor da matéria, seguido do parêntese em tinta com o que sobrou de cada termo; a conferência
é a distributiva com arcos do fator até cada termo (arco_d). No agrupamento, o parêntese que se repete fica numa caixa
pontilhada da cor da matéria e vira o fator comum.
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-002_fator_comum_e_agrupamento.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "metodo", "erro", "agrupar", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"

x = 10
assert 6 * x * x + 9 * x == 3 * x * (2 * x + 3) and 3 * (x + 4) == 3 * x + 12
assert x * x + x == x * (x + 1) == 110 and x * x == 100
a_, b_, y = 2, 3, 1
assert a_ * x + a_ * y + b_ * x + b_ * y == (x + y) * (a_ + b_) == 55 == 20 + 2 + 30 + 3 == 11 * 5
assert x * x + 5 * x - 2 * x - 10 == x * (x + 5) - 2 * (x + 5) == (x + 5) * (x - 2) == 120
assert x * x + 4 * x + 3 * x + 12 == (x + 4) * (x + 3) == 182 == 100 + 40 + 30 + 12 == 14 * 13
assert x * x - 49 == (x + 7) * (x - 7)
del x, a_, b_, y


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


def combo(c, t, cx, cy, ta, s=1.0):
    """um combo de MAT-EQU-004: cartão com o lanche (x reais) e o suco (4 reais), em escala s"""
    def desenha(p):
        k = lambda v: v * s
        M.rrect(c, cx - k(170), cy - k(130), k(340), k(260), k(22), BR, p)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - k(170), cy - k(130), k(340), k(260)), k(22), k(22)), M.paint(E.COR, p, stroke=4))
        pao = M.mix(E.COR, BR, 0.45)
        M.rrect(c, cx - k(140), cy - k(92), k(110), k(40), k(20), pao, p)
        M.rrect(c, cx - k(146), cy - k(48), k(122), k(18), k(9), TINTA2, p)
        M.rrect(c, cx - k(140), cy - k(26), k(110), k(24), k(10), pao, p)
        E.escreve(c, "x", cx - k(5), cy - k(18), k(72), "g", COR, p)
        path = skia.Path()
        path.moveTo(cx - k(130), cy + k(22)); path.lineTo(cx - k(40), cy + k(22)); path.lineTo(cx - k(52), cy + k(112)); path.lineTo(cx - k(118), cy + k(112)); path.close()
        c.drawPath(path, M.paint(M.mix(E.COR, BR, 0.7), p))
        c.drawPath(path, M.paint(E.COR, p, stroke=3))
        E.escreve(c, "4", cx - k(5), cy + k(95), k(72), "g", COR, p)
    E.foco(c, t, ta, 0.5, desenha)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]

    def conta():
        form(c, t, a_, "6x^2 + 9x", W / 2, 330, 190, None, "center")
        E.frase(c, t, entre(a_, b_, 0.3), ps("até agora, você abria parênteses", "i", 70, TINTA2), W / 2, 520, "center", 0.1)
        E.frase(c, t, entre(a_, b_, 0.62), ps("hoje:", "i", 80) + ps("o caminho de volta", "g", 80, COR), W / 2, 640, "center", 0.1)
        x0 = evid(c, t, b_, "3x", "2x + 3", W / 2 + fw("= ", 170) / 2, 880, 170, "center", b_ + 0.6)
        form(c, t, b_, "=", x0 - fw("= ", 170), 880, 170)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2 = C["s02.a"], C["s02.b"]
    E.frase(c, t, a2, ps("até o fim desta aula, você", "i", 84), XE, 260, passo=0.12)
    E.frase(c, t, a2 + 1.0, ps("transforma soma em multiplicação", "g", 84, COR), XE, 410, passo=0.13)
    form(c, t, a2 + 2.2, "6x^2 + 9x → 3x(2x + 3)", XE, 560, 90, TINTA2)
    E.foco(c, t, b2 - 0.2, 0.7, lambda p: E.bola(c, 1450, 820, 200 * ease_back(prog(t, b2 - 0.2, 0.7))), blur=0)
    E.foco(c, t, b2 + 0.2, 0.5, lambda p: (centro(c, "+ atalho", 1450, 800, 64, "g", BR, p), centro(c, "do sinal de menos", 1450, 870, 50, "i", BR, p)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_ = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, a_, ps("duas", "g", 84, COR) + ps("lembranças", "i", 90), XE, 180)
    xr = XE + 110
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "1", XE + 40, 360, 40, 50, p))
    E.frase(c, t, b_, ps("MDC:", "g", 66, COR) + ps("o maior número que divide todos", "i", 64), xr, 385, passo=0.1)
    form(c, t, b_ + 1.0, "MDC(6, 9) = 3", xr, 510, 96)
    E.foco(c, t, c_, 0.45, lambda p: num_bola(c, "2", XE + 40, 660, 40, 50, p))
    E.frase(c, t, c_, ps("distributiva:", "g", 66, COR) + ps("o de fora multiplica cada termo de dentro", "i", 60), xr, 685, passo=0.1)
    D = "3(x + 4) = 3x + 12"
    form(c, t, c_ + 0.6, D, xr, 900, 100)
    arco_d(c, t, c_ + 1.2, D, "3", "x", xr, 900, 100, 70)
    arco_d(c, t, c_ + 1.5, D, "3", "4", xr, 900, 100, 100)
    E.frase(c, t, C["s04"] - 2.2, ps("faltou alguma? procure no canal", "i", 54, TINTA2), 1150, 900, passo=0.08)


# ---------------- ideia ----------------
def b_ideia(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")

    def s04():
        for i in range(3):
            combo(c, t, 520 + i * 380, 270, a4 + i * 0.15, 0.85)
        form(c, t, b4, "3(x + 4)", 520, 620, 110)
        form(c, t, c4, "= 3x + 12", 520 + fw("3(x + 4) ", 110), 620, 110)
        V = "3x + 12 = 3 · x + 3 · 4"
        form(c, t, d4, "3x + 12", XE + 350, 880, 110)
        form(c, t, d4 + 0.8, "= 3 · x + 3 · 4", XE + 350 + fw("3x + 12 ", 110), 880, 110)
        realce(c, t, d4 + 1.4, V, "3", XE + 350, 880, 110, n=1)
        realce(c, t, d4 + 1.4, V, "3", XE + 350, 880, 110, n=2)
        E.foco(c, t, d4 + 1.6, 0.45, lambda p: E.escreve(c, "o 3 se repete", XE + 350 + fw(V, 110) + 50, 870, 56, "i", COR, p))
        E.foco(c, t, entre(c4, d4, 0.55), 0.45, lambda p: E.pilula(c, "fatorar = a volta", 1620, 470, 60, estilo="g", a=p))
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)

    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")

    def s05():
        E.frase(c, t, a5, ps("fatorar", "g", 96, COR) + ps("é escrever como multiplicação", "i", 84), XE, 220, passo=0.12)
        F = "12 = 2 × 2 × 3"
        form(c, t, b5, F, W / 2, 500, 150, None, "center")
        for tr, nn, k in (("2", 1, 0), ("2", 2, 0.2), ("3", 0, 0.4)):
            xx, ww = trecho_x(F, tr, W / 2, 150, "center", nn)
            realce(c, t, c5 + k, F, tr, W / 2, 500, 150, align="center", n=nn)
            E.foco(c, t, c5 + k + 0.2, 0.4, lambda p, xx=xx, ww=ww: centro(c, "fator", xx + ww / 2, 610, 50, "i", COR, p))
        E.foco(c, t, d5, 0.5, lambda p: E.pilula(c, "fator comum: divide todos os termos", W / 2, 840, 70, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    fase(c, t, C["s05"], 1e9, s05)


# ---------------- método ----------------
P = "6x^2 + 9x"


def b_metodo(c, t, C, b):
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")

    def s06():
        E.frase(c, t, C["s06"] + 0.2, ps("vamos fatorar", "i", 76), XE, 190, passo=0.1)
        form(c, t, a6, P, XE + 520, 195, 120, COR)
        E.foco(c, t, b6, 0.45, lambda p: num_bola(c, "1", XE + 40, 370, 40, 50, p))
        E.frase(c, t, b6, ps("números:", "g", 64, COR), XE + 110, 395)
        form(c, t, b6 + 0.6, "MDC(6, 9) = 3", XE + 480, 400, 96)
        E.foco(c, t, c6, 0.45, lambda p: num_bola(c, "2", XE + 40, 580, 40, 50, p))
        E.frase(c, t, c6, ps("letras:", "g", 64, COR), XE + 110, 605)
        form(c, t, c6 + 0.6, "x^2 e x^1", XE + 480, 610, 96)
        E.foco(c, t, entre(c6, d6, 0.55), 0.45, lambda p: E.escreve(c, "menor expoente: 1", XE + 960, 600, 60, "i", TINTA2, p))
        form(c, t, d6, "→ x", XE + 1480, 610, 96, COR)
        E.frase(c, t, e6 - 0.5, ps("fator comum:", "i", 76), XE, 880, passo=0.1)
        E.foco(c, t, e6, 0.5, lambda p: E.pilula(c, "3x", XE + 640, 860, 110, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    fase(c, t, C["s06"], C["s07"] - 0.1, s06)

    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")

    def s07():
        E.frase(c, t, a7, ps("divida cada termo por", "i", 76) + ps("3x", "g", 80, COR), XE, 190, passo=0.1)
        form(c, t, b7, "6x^2 ÷ 3x", XE, 400, 110)
        tb = entre(b7, c7, 0.3)
        form(c, t, tb, "6 ÷ 3 = 2", XE + 60, 520, 66, TINTA2)
        form(c, t, entre(b7, c7, 0.6), "x^2 ÷ x = x^{2 − 1} = x", XE + 480, 520, 66, TINTA2)
        form(c, t, c7, "= 2x", XE + fw("6x^2 ÷ 3x ", 110), 400, 110, COR)
        form(c, t, d7, "9x ÷ 3x = 3", 1150, 400, 110)
        realce(c, t, d7 + 0.6, "9x ÷ 3x = 3", "3", 1150, 400, 110, n=1)
        E.frase(c, t, e7 - 0.4, ps("resultado:", "i", 70), XE, 800, passo=0.1)
        form(c, t, e7, P + " =", XE + 360, 810, 130)
        evid(c, t, e7 + 0.3, "3x", "2x + 3", XE + 360 + fw(P + " = ", 130), 810, 130, t1=e7 + 0.8, cor=CERTO)
    fase(c, t, C["s07"], C["s08"] - 0.1, s07)

    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")

    def s08():
        E.frase(c, t, a8, ps("colocar em evidência:", "g", 76, COR), XE, 190, passo=0.1)
        E.frase(c, t, a8 + 1.2, ps("o fator comum vai para a frente", "i", 66), XE, 290, passo=0.1)
        R = "3x(2x + 3)"
        evid(c, t, a8 + 0.4, "3x", "2x + 3", W / 2, 620, 150, "center")
        x0 = W / 2 - fw(R, 150) / 2
        E.frase(c, t, b8, ps("confira com a distributiva", "i", 60, TINTA2), W / 2, 740, "center", 0.1)
        arco_d(c, t, c8, R, "3x", "2x", x0, 620, 150, 70)
        arco_d(c, t, d8, R, "3x", "3", x0, 620, 150, 115, n=1)
        form(c, t, c8 + 0.4, "3x × 2x = 6x^2", 360, 870, 96)
        form(c, t, d8 + 0.4, "3x × 3 = 9x", 1080, 870, 96)
        E.foco(c, t, d8 + 1.4, 0.45, lambda p: E.selo(c, 1700, 840, 50, True, p))
    fase(c, t, C["s08"], 1e9, s08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_, f_, g_ = (C[f"s09.{k}"] for k in "abcdefg")
    E.frase(c, t, C["s09"] + 0.3, ps("cuidado com o termo que", "i", 76) + ps("sai inteiro", "g", 76, ERRADO), XE, 180, passo=0.1)
    form(c, t, b_, "x^2 + x", XE, 380, 130)
    form(c, t, entre(b_, c_, 0.5), "x^2 ÷ x = x", 900, 330, 80, TINTA2)
    form(c, t, c_, "x ÷ x = 1", 900, 450, 80, COR)
    E.foco(c, t, c_ + 0.6, 0.45, lambda p: E.pilula(c, "1, não 0", 1560, 425, 56, estilo="g", a=p))
    form(c, t, d_, "x · x", XE, 640, 110, ERRADO)
    E.foco(c, t, d_ + 0.6, 0.45, lambda p: E.escreve(c, "o 1 sumiu", XE + 330, 630, 60, "i", ERRADO, p))
    E.frase(c, t, e_ - 0.4, ps("com 10:", "i", 60, TINTA2), XE, 800, passo=0.1)
    form(c, t, e_, "100 + 10 = 110", XE + 250, 805, 90)
    form(c, t, f_, "x · x → 100", 1100, 805, 90, ERRADO)
    if t >= f_ + 0.5:
        E.risco(c, 1080, 825, 1100 + fw("x · x → 100", 90) + 20, 735, t, f_ + 0.5, largura=10)
    E.frase(c, t, g_ - 0.4, ps("o certo:", "i", 70), XE, 975, passo=0.1)
    evid(c, t, g_, "x", "x + 1", XE + 330, 980, 120, t1=g_ + 0.4, cor=CERTO)


# ---------------- agrupamento ----------------
Q4 = "ax + ay + bx + by"
G2 = "a(x + y) + b(x + y)"


def b_agrupar(c, t, C, b):
    a0, b0 = C["s10.a"], C["s10.b"]
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2 = (C[f"s12.{k}"] for k in "abc")
    s, y = 130, 330

    def s10_12():
        E.frase(c, t, C["s10"] + 0.2, ps("e quando nada se repete em", "i", 70) + ps("todos?", "g", 70, COR), XE, 150, passo=0.1)
        form(c, t, a0, Q4, W / 2, y, s, None, "center")
        x0 = W / 2 - fw(Q4, s) / 2
        t_a, t_x = entre(a0, b0, 0.4), entre(a0, b0, 0.7)
        for tr in ("bx", "by"):
            xx, ww = trecho_x(Q4, tr, x0, s)
            E.foco(c, t, t_a, 0.4, lambda p, xx=xx, ww=ww: centro(c, "sem a", xx + ww / 2, y + 80, 46, "i", ERRADO, p), sobe=6)
        xx, ww = trecho_x(Q4, "ay", x0, s)
        E.foco(c, t, t_x, 0.4, lambda p: centro(c, "sem x", xx + ww / 2, y + 80, 46, "i", ERRADO, p), sobe=6)
        # pares
        for k, (tr, tk) in enumerate((("ax + ay", b0), ("bx + by", b0 + 0.4))):
            xx, ww = trecho_x(Q4, tr, x0, s)
            E.foco(c, t, tk, 0.45, lambda p, xx=xx, ww=ww: E.chave(c, xx, xx + ww, y - s - 10, COR, p, -24))
        E.foco(c, t, b0 + 0.6, 0.45, lambda p: centro(c, "agrupar: fatorar em pares", W / 2, y + 160, 60, "b", COR, p))
        # cada par
        realce(c, t, a1, Q4, "a", x0, y, s)
        realce(c, t, a1, Q4, "a", x0, y, s, n=1)
        realce(c, t, c1, Q4, "b", x0, y, s)
        realce(c, t, c1, Q4, "b", x0, y, s, n=1)
        y2 = 640
        g0 = W / 2 - fw(G2, s) / 2
        evid(c, t, b1, "a", "x + y", g0, y2, s, t1=b1 + 0.4)
        form(c, t, d1 - 0.2, " +", g0 + fw("a(x + y)", s), y2, s)
        evid(c, t, d1, "b", "x + y", g0 + fw("a(x + y) + ", s), y2, s, t1=d1 + 0.4)
        for n, k in ((0, 0), (1, 0.3)):
            xx, ww = trecho_x(G2, "(x + y)", g0, s, n=n)
            q = ep(t, a2 + k, 0.5)
            if q > 0:
                E.caixa_pontilhada(c, xx - 14, y2 - s * 0.98, ww + 28, s * 1.28, q, COR, prog_=q)
        E.foco(c, t, a2 + 0.5, 0.45, lambda p: centro(c, "o mesmo parêntese: uma caixa fechada", W / 2, y2 + 110, 54, "i", COR, p))
        E.frase(c, t, b2, ps("caixa em evidência:", "i", 66), XE, 920, passo=0.1)
        R = "(x + y)(a + b)"
        xr = XE + 620
        form(c, t, c2, "(x + y)", xr, 930, 130, COR)
        form(c, t, c2 + 0.5, "(a + b)", xr + fw("(x + y)", 130), 930, 130, CERTO)
        q = ep(t, c2 + 0.2, 0.5)
        if q > 0:
            E.caixa_pontilhada(c, xr - 14, 930 - 128, fw("(x + y)", 130) + 28, 166, q, COR, prog_=q)
    fase(c, t, C["s10"], C["s13"] - 0.1, s10_12)

    a3, b3, c3 = (C[f"s13.{k}"] for k in "abc")

    def s13():
        E.frase(c, t, C["s13"] + 0.2, ps("teste com números", "i", 76, TINTA2), XE, 190, passo=0.1)
        form(c, t, a3, "a = 2   b = 3   x = 10   y = 1", XE, 360, 90, COR)
        form(c, t, b3 - 0.6, Q4, XE, 560, 90, TINTA2)
        form(c, t, b3, "20 + 2 + 30 + 3 = 55", 920, 560, 90)
        form(c, t, c3 - 0.6, "(x + y)(a + b)", XE, 760, 90, TINTA2)
        form(c, t, c3, "11 × 5 = 55", 920, 760, 90)
        E.foco(c, t, c3 + 1.0, 0.45, lambda p: E.selo(c, 1650, 720, 56, True, p))
    fase(c, t, C["s13"], 1e9, s13)


# ---------------- atalho (palco escuro) ----------------
A4 = "x^2 + 5x − 2x − 10"


def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    s, y = 120, 380

    def s14():
        E.frase(c, t, C["s14"] + 0.2, ps("o atalho:", "i", 70, CLARO), XE, 180, passo=0.1)
        E.frase(c, t, a4, ps("segundo par com", "i", 70, CLARO) + ps("sinal de menos", "g", 70, BR), XE + 330, 180, passo=0.1)
        form(c, t, b4, A4, W / 2, y, s, BR, "center")
        x0 = W / 2 - fw(A4, s) / 2
        xx, ww = trecho_x(A4, "x^2 + 5x", x0, s)
        E.foco(c, t, c4, 0.45, lambda p: E.chave(c, xx, xx + ww, y + 40, CLARO, p, 24))
        xm, wm = trecho_x(A4, "− 2x − 10", x0, s)
        E.foco(c, t, d4, 0.45, lambda p: E.chave(c, xm, xm + wm, y + 40, AM, p, 24))
        realce(c, t, d4 + 0.3, A4, "− 2", x0, y, s, AM)
        E.foco(c, t, d4 + 0.5, 0.45, lambda p: centro(c, "tire o −2 junto", xm + wm / 2, y + 150, 56, "i", AM, p))
        y2 = 720
        R = "x(x + 5) − 2(x + 5)"
        g0 = W / 2 - fw(R, s) / 2
        form(c, t, c4 + 0.3, "x(x + 5)", g0, y2, s, BR)
        form(c, t, e4, " − 2(x + 5)", g0 + fw("x(x + 5)", s), y2, s, AM)
        for n, k in ((0, 0), (1, 0.3)):
            xq, wq = trecho_x(R, "(x + 5)", g0, s, n=n)
            q = ep(t, e4 + 0.8 + k, 0.5)
            if q > 0:
                E.caixa_pontilhada(c, xq - 14, y2 - s * 0.98, wq + 28, s * 1.28, q, AM, prog_=q)
    fase(c, t, C["s14"], C["s15"] - 0.1, s14)

    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]

    def s15():
        E.frase(c, t, C["s15"] + 0.2, ps("o parêntese bateu", "i", 70, CLARO), XE, 180, passo=0.1)
        form(c, t, a5, "(x + 5)(x − 2)", XE + 620, 190, 110, AM)
        E.frase(c, t, b5, ps("tirando o −2, cada termo troca de sinal", "i", 64, CLARO), XE, 380, passo=0.09)
        form(c, t, b5 + 1.0, "−2x ÷ (−2) = x", XE, 520, 90, BR)
        form(c, t, b5 + 1.8, "−10 ÷ (−2) = +5", 1000, 520, 90, BR)
        E.foco(c, t, c5, 0.45, lambda p: num_bola(c, "?", XE + 40, 730, 40, 50, p, AM, "#07070F"))
        E.frase(c, t, c5, ps("não bateu?", "g", 66, BR) + ps("troque a ordem dos termos", "i", 64, CLARO), XE + 110, 755, passo=0.1)
        E.foco(c, t, entre(c5, C["s16"], 0.55), 0.45, lambda p: E.selo(c, XE + 40, 900, 40, False, p))
        E.frase(c, t, entre(c5, C["s16"], 0.55), ps("nem assim?", "g", 66, BR) + ps("não fatora por agrupamento", "i", 64, CLARO), XE + 110, 925, passo=0.1)
    fase(c, t, C["s15"], 1e9, s15)


# ---------------- questão ----------------
QQ = "x^2 + 4x + 3x + 12"


def b_questao(c, t, C, b):
    a_ = C["s16.a"]
    E.frase(c, t, C["s16"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 220)
    E.frase(c, t, a_ - 0.3, ps("fatore", "i", 110), XE, 450)
    form(c, t, a_, QQ, XE, 680, 130, COR)
    E.relogio(c, t, C["s17.a"], 1560, 400, 170)


# ---------------- resposta ----------------
PX, PY, PA, PU = 1150, 360, 330, 46


def b_resposta(c, t, C, b):
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]

    def s18():
        E.frase(c, t, C["s18"] + 0.2, ps("em pares", "i", 72, TINTA2), XE, 180, passo=0.1)
        form(c, t, C["s18"] + 0.4, QQ, W / 2, 340, 120, None, "center")
        x0 = W / 2 - fw(QQ, 120) / 2
        for k, (tr, tk) in enumerate((("x^2 + 4x", a8), ("3x + 12", b8))):
            xx, ww = trecho_x(QQ, tr, x0, 120)
            E.foco(c, t, tk, 0.45, lambda p, xx=xx, ww=ww: E.chave(c, xx, xx + ww, 380, COR, p, 24))
        R = "x(x + 4) + 3(x + 4)"
        g0 = W / 2 - fw(R, 120) / 2
        evid(c, t, a8 + 0.3, "x", "x + 4", g0, 600, 120, t1=a8 + 0.7)
        form(c, t, entre(b8, c8, 0.5), " +", g0 + fw("x(x + 4)", 120), 600, 120)
        E.foco(c, t, b8, 0.45, lambda p: E.escreve(c, "MDC(3, 12) = 3", g0 + fw("x(x + 4) + ", 120), 470, 54, "i", TINTA2, p))
        evid(c, t, entre(b8, c8, 0.5), "3", "x + 4", g0 + fw("x(x + 4) + ", 120), 600, 120)
        E.frase(c, t, c8 - 0.5, ps("resposta:", "i", 72), XE, 880, passo=0.1)
        form(c, t, c8, "(x + 4)(x + 3)", XE + 380, 890, 140, CERTO)
    fase(c, t, C["s18"], C["s19"] - 0.1, s18)

    a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]

    def s19():
        E.frase(c, t, C["s19"] + 0.2, ps("confira com 10:", "i", 72, TINTA2), XE, 200, passo=0.1)
        form(c, t, a9, "100 + 40 + 30 + 12", XE, 380, 84)
        form(c, t, a9 + 0.6, "= 182", XE, 490, 84)
        form(c, t, b9, "14 × 13 = 182", XE, 680, 84, CERTO)
        E.foco(c, t, b9 + 0.6, 0.45, lambda p: E.selo(c, XE + fw("14 × 13 = 182", 84) + 70, 650, 40, True, p))
        rot = tuple(ep(t, c9 + k, 0.4) for k in (0, 0.2, 0.4, 0.6))
        E.foco(c, t, c9, 0.5, lambda p: piso(c, PX, PY, PA, (4 * PU, 3 * PU), p, ("x^2", "4x", "3x", "12"), rot, rot, sizes=(90, 58, 58, 58)))
        lados(c, t, c9 + 0.2, PX, PY, PA, (4 * PU, 3 * PU), "x", "3", lb2="4")
        E.foco(c, t, c9 + 0.8, 0.45, lambda p: centro(c, "os 4 pedaços do piso", PX + (PA + 4 * PU) / 2, PY + PA + 3 * PU + 80, 54, "i", COR, p))
    fase(c, t, C["s19"], 1e9, s19)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a0, b0, c0 = C["s20.a"], C["s20.b"], C["s20.c"]

    def resumo():
        E.frase(c, t, C["s20"] + 0.2, ps("resumindo", "i", 96, COR), W / 2, 200, "center")
        E.foco(c, t, a0, 0.5, lambda p: num_bola(c, "1", 230, 380, 58, 66, p))
        E.frase(c, t, a0 + 0.1, ps("ache o que se repete em", "i", 76) + ps("todos", "g", 74, COR), 320, 410, passo=0.12)
        E.foco(c, t, b0, 0.5, lambda p: num_bola(c, "2", 230, 580, 58, 66, p))
        E.frase(c, t, b0 + 0.1, ps("coloque em evidência", "g", 74, COR), 320, 610, passo=0.12)
        form(c, t, b0 + 0.8, "6x^2 + 9x =", 320, 730, 90)
        evid(c, t, b0 + 1.0, "3x", "2x + 3", 320 + fw("6x^2 + 9x = ", 90), 730, 90)
        E.foco(c, t, c0, 0.5, lambda p: num_bola(c, "3", 230, 880, 58, 66, p))
        E.frase(c, t, c0 + 0.1, ps("nada em todos?", "i", 76) + ps("agrupe em pares", "g", 74, COR), 320, 910, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a_, b_, c_, d_ = (C[f"s21.{k}"] for k in "abcd")
    E.frase(c, t, C["s21"] + 0.2, ps("próxima aula", "i", 84), XE, 230)
    E.frase(c, t, C["s21"] + 0.8, ps("fatorar com produtos notáveis", "g", 80, COR), XE, 370, passo=0.12)
    form(c, t, a_, "x^2 − 49", XE, 560, 110)
    form(c, t, b_, "= (x + 7)(x − 7)", XE + fw("x^2 − 49 ", 110), 560, 110, COR)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 760, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(1000, 805, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, metodo=b_metodo, erro=b_erro, agrupar=b_agrupar,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
