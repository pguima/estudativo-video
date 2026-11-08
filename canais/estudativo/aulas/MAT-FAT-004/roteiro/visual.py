"""Visual — Estudativo · MAT-FAT-004: simplificar frações algébricas.
18/24 com o 6 cortado em cima e embaixo; fator × parcela; (x² − 9)/(x − 3) fatorada no lugar, com o fator comum realçado
e cortado; o valor proibido; (5x + 15)/(x² − 9) com dois valores proibidos; o erro de cortar parcela; no palco, o atalho
de trocar x por um número nas alternativas.

Convenções da trilha:
- fração em dois andares (fra); cada andar troca no lugar quando é fatorado (andar);
- CORTAR FATOR: realce da cor da matéria no mesmo fator em cima e embaixo, depois um traço inclinado na cor da matéria;
  corte proibido (parcela) é o mesmo traço em vermelho, seguido de risco no resultado errado;
- VALOR PROIBIDO: o de baixo da fração original ganha realce vermelho com "= 0", e a resposta leva ao lado a pílula
  vermelha "x ≠ 3" (proibido()).
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math
from fractions import Fraction as Fr

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-004_simplificar_fracoes_algebricas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("numeros", "algebrica", "proibido", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"

x = 10
assert Fr(18, 24) == Fr(6 * 3, 6 * 4) == Fr(3, 4)
assert Fr(x * x - 9, x - 3) == x + 3 == 13 and x * x - 9 == 91 and Fr(91, 7) == 13
assert Fr(5 * x + 15, x * x - 9) == Fr(5, x - 3) == Fr(65, 91) == Fr(5, 7) and 65 // 13 == 5 and 91 // 13 == 7
assert Fr(6 + 3, 3) == 3 != 6
assert Fr(x * x - 25, 2 * x + 10) == Fr(x - 5, 2) == Fr(75, 30) == Fr(5, 2) and 75 // 15 == 5 and 30 // 15 == 2
assert 2 * (-5 + 5) == 0
x = 2
assert Fr(x * x - 9, x - 3) == 5 == x + 3 and x - 3 == -1
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


def fra(c, cima, baixo, cx, y, size, a=1.0, cor=None, cor_c=None, cor_b=None, so_cima=False):
    """fração armada em dois andares, centrada em cx; y = altura da barra. Cada andar é uma fórmula (aceita x^2, r{2})"""
    if a <= 0:
        return
    w = max(fw(cima, size), fw(baixo, size)) + size * 0.3
    tinta = cor or TINTA
    E.formula(c, cima, cx, y - size * 0.32, size, cor=cor_c or tinta, a=a, align="center")
    if not so_cima:
        b = max(5, size * 0.07)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y - b / 2, w, b), b / 2, b / 2), M.paint(tinta, a))
        E.formula(c, baixo, cx, y + size * 0.98, size, cor=cor_b or tinta, a=a, align="center")


def fra_w(cima, baixo, size):
    return max(fw(cima, size), fw(baixo, size)) + size * 0.3


def fra_em(c, t, t0, cima, baixo, cx, y, size, cor=None, cor_c=None, cor_b=None):
    E.foco(c, t, t0, 0.5, lambda p: fra(c, cima, baixo, cx, y, size, p, cor, cor_c, cor_b))


def andar(c, t, t0, s, cx, y, size, cima=True, cor=None, t1=None):
    """um andar da fração que troca no lugar (fatorado entra em t0 e sai em t1)"""
    yy = y - size * 0.32 if cima else y + size * 0.98
    fn = lambda p: E.formula(c, s, cx, yy, size, cor=cor or TINTA, a=p, align="center")
    if t1 is not None:
        if t0 - 0.01 <= t < t1 + 0.4:
            E.saida(c, t, t1, lambda: E.foco(c, t, t0, 0.45, fn))
    else:
        E.foco(c, t, t0, 0.45, fn)


def barra_f(c, t, t0, cx, y, w, size, cor=None):
    b = max(5, size * 0.07)
    p = ep(t, t0, 0.4)
    if p > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 * p, y - b / 2, w * p, b), b / 2, b / 2), M.paint(cor or TINTA, 1.0))


def yb(y, size, cima):
    """linha de base de um andar"""
    return y - size * 0.32 if cima else y + size * 0.98


def realce_f(c, t, t0, s, trecho, cx, y, size, cima, cor=None, n=0, t1=None):
    realce(c, t, t0, s, trecho, cx, yb(y, size, cima), size, cor, "center", n, t1)


def corta_f(c, t, t0, s, trecho, cx, y, size, cima, cor=None, n=0):
    """corte de um fator: traço inclinado sobre o trecho (na cor da matéria: corte permitido; vermelho: proibido)"""
    if t < t0:
        return
    x0, w = trecho_x(s, trecho, cx, size, "center", n)
    yy = yb(y, size, cima)
    E.risco(c, x0 - 10, yy + size * 0.12, x0 + w + 10, yy - size * 0.8, t, t0, cor or COR, max(6, size * 0.07))


def proibido(c, t, t0, s, cx, cy, size=60):
    """valor proibido (convenção da trilha): pílula vermelha com o x que zera o de baixo da fração original"""
    E.foco(c, t, t0, 0.45, lambda p: E.pilula(c, s, cx, cy, size, estilo="g", fundo=ERRADO, cor=BR, a=p))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]

    def conta():
        fra_em(c, t, a_, "x^2 − 9", "x − 3", 700, 470, 170)
        E.frase(c, t, entre(a_, b_, 0.5), ps("parece complicado", "i", 70, TINTA2), 700, 800, "center", 0.1)
        form(c, t, b_, "= x + 3", 1000, 530, 190, CERTO)
        E.foco(c, t, b_ + 0.6, 0.45, lambda p: centro(c, "disfarçado", 1340, 700, 70, "i", COR, p))
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]
    E.frase(c, t, a2, ps("até o fim desta aula, você", "i", 84), XE, 260, passo=0.12)
    E.frase(c, t, a2 + 1.0, ps("simplifica frações com letra", "g", 88, COR), XE, 410, passo=0.13)
    E.frase(c, t, b2, ps("sem o", "i", 84) + ps("corte proibido", "g", 84, ERRADO), XE, 560, passo=0.12)
    E.foco(c, t, c2 - 0.2, 0.7, lambda p: E.bola(c, 1450, 820, 200 * ease_back(prog(t, c2 - 0.2, 0.7))), blur=0)
    E.foco(c, t, c2 + 0.2, 0.5, lambda p: (centro(c, "+ atalho", 1450, 800, 64, "g", BR, p), centro(c, "das alternativas", 1450, 870, 50, "i", BR, p)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_ = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, a_, ps("duas", "g", 84, COR) + ps("lembranças", "i", 90), XE, 180)
    xr = XE + 110
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "1", XE + 40, 340, 40, 50, p))
    E.frase(c, t, b_, ps("simplificar:", "g", 64, COR) + ps("dividir em cima e embaixo pelo mesmo número", "i", 58), xr, 365, passo=0.08)
    form(c, t, b_ + 1.2, "f{6}{8} = f{3}{4}", xr + 20, 500, 96)
    E.foco(c, t, c_, 0.45, lambda p: num_bola(c, "2", XE + 40, 640, 40, 50, p))
    E.frase(c, t, c_, ps("fatorar:", "g", 64, COR) + ps("evidência e diferença de quadrados", "i", 58), xr, 665, passo=0.08)
    form(c, t, c_ + 1.0, "5x + 15 =", xr + 20, 800, 84)
    evid(c, t, c_ + 1.3, "5", "x + 3", xr + 20 + fw("5x + 15 = ", 84), 800, 84)
    form(c, t, c_ + 1.8, "x^2 − 9 = (x + 3)(x − 3)", xr + 20, 920, 84)
    E.frase(c, t, C["s04"] - 2.2, ps("faltou alguma? procure no canal", "i", 54, TINTA2), 1150, 920, passo=0.08)


# ---------------- com números ----------------
def b_numeros(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s04.{k}"] for k in "abcde")
    s, y = 130, 520

    def s04():
        E.frase(c, t, C["s04"] + 0.2, ps("comece com números", "i", 76, TINTA2), XE, 180, passo=0.1)
        fra_em(c, t, a4, "18", "24", 420, y, s)
        form(c, t, b4, "=", 600, y + 45, s)
        cx = 950
        barra_f(c, t, b4, cx, y, fra_w("6 · 3", "6 · 4", s), s)
        andar(c, t, b4, "6 · 3", cx, y, s, True)
        andar(c, t, c4, "6 · 4", cx, y, s, False)
        tm = entre(c4, d4, 0.4)
        realce_f(c, t, tm, "6 · 3", "6", cx, y, s, True)
        realce_f(c, t, tm, "6 · 4", "6", cx, y, s, False)
        E.foco(c, t, tm + 0.2, 0.45, lambda p: E.escreve(c, "o 6 multiplica em cima e embaixo", XE, 900, 56, "i", COR, p))
        corta_f(c, t, d4, "6 · 3", "6", cx, y, s, True)
        corta_f(c, t, d4 + 0.2, "6 · 4", "6", cx, y, s, False)
        form(c, t, e4 - 0.2, "=", 1180, y + 45, s)
        fra_em(c, t, e4, "3", "4", 1400, y, s, CERTO)
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)

    a5, b5 = C["s05.a"], C["s05.b"]

    def s05():
        for k, (tit, nota, tk, ok) in enumerate((("fator", "multiplica a parte de cima inteira e a de baixo inteira", a5, True),
                                                 ("parcela", "pedaço de uma soma", b5, False))):
            cx = 500 + k * 920
            cor = CERTO if ok else ERRADO
            q = ep(t, tk, 0.5)
            E.caixa_pontilhada(c, cx - 420, 200, 840, 760, q, cor, prog_=q)
            E.frase(c, t, tk, ps(tit, "g", 80, cor), cx, 320, "center")
            for j, linha in enumerate((nota.split(" e ") if ok else [nota])):
                E.foco(c, t, tk + 0.4 + j * 0.6, 0.45, lambda p, linha=linha, j=j, cx=cx: centro(c, (linha if j == 0 else "e " + linha), cx, 410 + j * 64, 48, "i", TINTA, p))
            cima, baixo = ("6 · 3", "6 · 4") if ok else ("6 + 3", "6")
            fra_em(c, t, tk + 0.8, cima, baixo, cx, 660, 110)
            corta_f(c, t, tk + 1.4, cima, "6", cx, 660, 110, True, cor)
            corta_f(c, t, tk + 1.6, baixo, "6", cx, 660, 110, False, cor)
            E.foco(c, t, tk + 2.0, 0.45, lambda p, cx=cx, ok=ok: E.selo(c, cx, 880, 46, ok, p))
        E.foco(c, t, b5 + 2.4, 0.45, lambda p: centro(c, "não se corta", 1420, 490, 56, "b", ERRADO, p))
    fase(c, t, C["s05"], 1e9, s05)


# ---------------- fração algébrica ----------------
def b_algebrica(c, t, C, b):
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    s, y, cx = 130, 540, 760
    TOP = "(x + 3)(x − 3)"

    def s06():
        E.frase(c, t, a6, ps("fração algébrica:", "g", 76, COR) + ps("a mesma regra", "i", 76), XE, 180, passo=0.1)
        barra_f(c, t, C["s06"] + 0.3, cx, y, fra_w(TOP, "x − 3", s), s)
        andar(c, t, C["s06"] + 0.3, "x^2 − 9", cx, y, s, True, t1=b6)
        andar(c, t, b6 + 0.3, TOP, cx, y, s, True)
        andar(c, t, C["s06"] + 0.3, "x − 3", cx, y, s, False)
        E.foco(c, t, b6 + 0.3, 0.45, lambda p: E.escreve(c, "fatore em cima", cx + 520, y - 160, 54, "i", TINTA2, p))
        realce_f(c, t, c6, "x − 3", "x − 3", cx, y, s, False)
        realce_f(c, t, c6 + 0.4, TOP, "(x − 3)", cx, y, s, True)
        corta_f(c, t, d6, TOP, "(x − 3)", cx, y, s, True)
        corta_f(c, t, d6 + 0.2, "x − 3", "x − 3", cx, y, s, False)
        form(c, t, e6, "= x + 3", cx + 540, y + 45, 150, CERTO)
    fase(c, t, C["s06"], C["s07"] - 0.1, s06)

    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")

    def s07():
        E.frase(c, t, C["s07"] + 0.2, ps("teste com 10", "i", 76, TINTA2), XE, 180, passo=0.1)
        form(c, t, a7, "100 − 9 = 91", XE, 380, 96)
        form(c, t, b7, "10 − 3 = 7", XE, 540, 96)
        fra_em(c, t, c7, "91", "7", 1020, 470, 110)
        form(c, t, c7 + 0.4, "= 13", 1120, 510, 110)
        form(c, t, d7, "10 + 3 = 13", 1020, 820, 110, CERTO)
        E.foco(c, t, d7 + 0.8, 0.45, lambda p: E.selo(c, 1020 + fw("10 + 3 = 13", 110) + 90, 780, 50, True, p))
    fase(c, t, C["s07"], 1e9, s07)


# ---------------- valor proibido ----------------
def b_proibido(c, t, C, b):
    a_, b_, c_ = C["s08.a"], C["s08.b"], C["s08.c"]
    s, y, cx = 130, 480, 520
    E.frase(c, t, C["s08"] + 0.3, ps("mas tem um detalhe", "i", 76, TINTA2), XE, 180, passo=0.1)
    fra_em(c, t, C["s08"] + 0.5, "x^2 − 9", "x − 3", cx, y, s)
    realce_f(c, t, a_, "x − 3", "x − 3", cx, y, s, False, ERRADO)
    E.frase(c, t, a_, ps("com x = 3:", "i", 66), 960, 450, passo=0.1)
    form(c, t, a_ + 0.6, "3 − 3 = 0", 960, 600, 110, ERRADO)
    E.foco(c, t, b_, 0.5, lambda p: E.pilula(c, "divisão por zero não existe", 1300, 760, 60, estilo="g", fundo=ERRADO, cor=BR, a=p))
    E.frase(c, t, c_ - 0.6, ps("resposta completa:", "i", 66), XE, 960, passo=0.1)
    form(c, t, c_, "x + 3", XE + 600, 970, 130, CERTO)
    proibido(c, t, c_ + 0.6, "x ≠ 3", XE + 600 + fw("x + 3", 130) + 170, 925, 66)


# ---------------- outro exemplo ----------------
def b_exemplo(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    s, y, cx = 120, 500, 700
    TOP, BOT = "5(x + 3)", "(x + 3)(x − 3)"

    def s09():
        E.frase(c, t, C["s09"] + 0.2, ps("mais um", "i", 76, TINTA2), XE, 180, passo=0.1)
        barra_f(c, t, a9, cx, y, fra_w(BOT, "5x + 15", s), s)
        andar(c, t, a9, "5x + 15", cx, y, s, True, t1=b9)
        andar(c, t, b9 + 0.3, TOP, cx, y, s, True)
        andar(c, t, a9, "x^2 − 9", cx, y, s, False, t1=c9)
        andar(c, t, c9 + 0.3, BOT, cx, y, s, False)
        E.foco(c, t, b9 + 0.3, 0.45, lambda p: E.escreve(c, "o 5 em evidência", 1180, y - 60, 52, "i", TINTA2, p))
        E.foco(c, t, c9 + 0.3, 0.45, lambda p: E.escreve(c, "diferença de quadrados", 1180, y + 130, 52, "i", TINTA2, p))
        realce_f(c, t, d9 - 0.3, TOP, "(x + 3)", cx, y, s, True)
        realce_f(c, t, d9 - 0.3, BOT, "(x + 3)", cx, y, s, False)
        corta_f(c, t, d9, TOP, "(x + 3)", cx, y, s, True)
        corta_f(c, t, d9 + 0.2, BOT, "(x + 3)", cx, y, s, False)
        form(c, t, e9 - 0.2, "=", 1080, 900, 120)
        fra_em(c, t, e9, "5", "x − 3", 1320, 860, 110, CERTO)
    fase(c, t, C["s09"], C["s10"] - 0.1, s09)

    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")

    def s10():
        E.frase(c, t, a0, ps("dois valores proibidos", "g", 76, ERRADO), XE, 180, passo=0.1)
        fra(c, "5x + 15", "(x + 3)(x − 3)", 470, 380, 90, ep(t, C["s10"] + 0.2, 0.5), cor_b=TINTA)
        realce_f(c, t, b0, "(x + 3)(x − 3)", "(x − 3)", 470, 380, 90, False, ERRADO)
        realce_f(c, t, b0 + 0.4, "(x + 3)(x − 3)", "(x + 3)", 470, 380, 90, False, ERRADO)
        proibido(c, t, entre(b0, c0, 0.35), "x ≠ 3", 1080, 380, 62)
        proibido(c, t, entre(b0, c0, 0.65), "x ≠ −3", 1450, 380, 62)
        E.frase(c, t, c0 - 0.5, ps("com 10:", "i", 62, TINTA2), XE, 720, passo=0.1)
        fra_em(c, t, c0, "65", "91", 540, 690, 100)
        form(c, t, d0 - 0.2, "=", 655, 730, 100)
        fra_em(c, t, d0, "5", "7", 800, 690, 100)
        E.foco(c, t, d0 + 0.3, 0.45, lambda p: centro(c, "÷ 13", 683, 640, 44, "i", TINTA2, p))
        fra_em(c, t, e0, "5", "10 − 3", 1180, 690, 100)
        form(c, t, e0 + 0.4, "=", 1355, 730, 100)
        fra_em(c, t, e0 + 0.6, "5", "7", 1490, 690, 100, CERTO)
        E.foco(c, t, e0 + 1.2, 0.45, lambda p: E.selo(c, 1630, 700, 44, True, p))
    fase(c, t, C["s10"], 1e9, s10)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_, f_ = (C[f"s11.{k}"] for k in "abcdef")
    s, y, cx = 140, 470, 420
    E.frase(c, t, C["s11"] + 0.3, ps("o erro mais comum:", "g", 80, ERRADO) + ps("cortar parcela", "i", 80), XE, 170, passo=0.1)
    fra_em(c, t, b_, "x + 3", "3", cx, y, s)
    corta_f(c, t, c_ - 0.4, "x + 3", "3", cx, y, s, True, ERRADO)
    corta_f(c, t, c_ - 0.2, "3", "3", cx, y, s, False, ERRADO)
    form(c, t, c_, "= x", cx + 220, y + 50, s, ERRADO)
    if t >= c_ + 0.8:
        E.risco(c, cx + 200, y + 70, cx + 220 + fw("= x", s) + 20, y - 70, t, c_ + 0.8, largura=11)
    E.frase(c, t, d_ - 0.4, ps("com x = 6:", "i", 62, TINTA2), 1000, 330, passo=0.1)
    fra_em(c, t, d_, "6 + 3", "3", 1120, 480, 100)
    form(c, t, d_ + 0.5, "=", 1270, 515, 100)
    fra_em(c, t, d_ + 0.8, "9", "3", 1410, 480, 100)
    form(c, t, d_ + 1.2, "= 3", 1495, 515, 100, CERTO)
    E.frase(c, t, e_ - 0.4, ps("o corte daria", "i", 62), 1000, 760, passo=0.1)
    form(c, t, e_, "6", 1400, 770, 110, ERRADO)
    realce_f(c, t, f_, "x + 3", "+ 3", cx, y, s, ERRADO)
    E.foco(c, t, f_ + 0.3, 0.45, lambda p: E.escreve(c, "o 3 está somando, não multiplicando", XE, 960, 60, "b", ERRADO, p))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2 = C["s12.a"], C["s12.b"]

    def s12():
        E.frase(c, t, C["s12"] + 0.2, ps("o atalho das alternativas", "i", 76, CLARO), XE, 170, passo=0.1)
        E.foco(c, t, a2, 0.45, lambda p: num_bola(c, "1", XE + 40, 300, 36, 46, p, AM, "#07070F"))
        E.frase(c, t, a2, ps("troque o x por um número fácil:", "i", 62, CLARO), XE + 100, 322, passo=0.08)
        form(c, t, a2 + 0.8, "x = 2", XE + 1010, 325, 80, AM)
        tc = entre(a2, b2, 0.45)
        E.foco(c, t, tc, 0.45, lambda p: num_bola(c, "2", XE + 40, 440, 36, 46, p, AM, "#07070F"))
        E.frase(c, t, tc, ps("calcule a original e cada alternativa", "i", 62, CLARO), XE + 100, 462, passo=0.08)
        fra(c, "x^2 − 9", "x − 3", 420, 640, 80, ep(t, tc + 0.4, 0.5), BR)
        form(c, t, tc + 0.8, "→ 5", 600, 670, 80, AM)
        form(c, t, tc + 1.2, "A)  x − 3  → −1", 980, 620, 70, CLARO)
        form(c, t, tc + 1.6, "B)  x + 3  → 5", 980, 740, 70, BR)
        E.foco(c, t, b2, 0.45, lambda p: num_bola(c, "3", XE + 40, 880, 36, 46, p, AM, "#07070F"))
        E.frase(c, t, b2, ps("a que der o mesmo valor é a", "i", 62, CLARO) + ps("candidata", "g", 62, AM), XE + 100, 902, passo=0.08)
        E.foco(c, t, b2 + 0.4, 0.45, lambda p: E.selo(c, 1560, 715, 34, True, p))
    fase(c, t, C["s12"], C["s13"] - 0.1, s12)

    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")

    def s13():
        E.frase(c, t, C["s13"] + 0.2, ps("funciona porque", "i", 76, CLARO), XE, 170, passo=0.1)
        E.frase(c, t, a3, ps("expressões iguais dão o mesmo resultado", "g", 60, BR), XE, 290, passo=0.08)
        E.frase(c, t, a3 + 1.4, ps("para todo valor permitido do x", "i", 60, CLARO), XE, 370, passo=0.08)
        for k, (tk, ok, txt) in enumerate(((b3, False, "nunca use um valor proibido"), (c3, False, "evite 0 e 1: muita alternativa empata"),
                                           (d3, True, "empatou? teste outro número"))):
            yy = 540 + k * 150
            E.foco(c, t, tk, 0.45, lambda p, yy=yy, ok=ok: E.selo(c, XE + 40, yy - 20, 38, ok, p))
            E.frase(c, t, tk, ps(txt, "i", 62, CLARO), XE + 110, yy, passo=0.08)
    fase(c, t, C["s13"], 1e9, s13)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_ = C["s14.a"], C["s14.b"]
    E.frase(c, t, C["s14"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, a_ - 0.3, ps("simplifique", "i", 90), XE, 380, passo=0.1)
    fra_em(c, t, a_, "x^2 − 25", "2x + 10", 520, 600, 130, COR)
    E.frase(c, t, b_, ps("e diga o", "i", 70) + ps("valor proibido", "g", 70, ERRADO), XE, 960, passo=0.1)
    E.relogio(c, t, C["s15.a"], 1520, 450, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    s, y, cx = 120, 470, 640
    TOP, BOT = "(x + 5)(x − 5)", "2(x + 5)"

    def s16():
        barra_f(c, t, C["s16"] + 0.2, cx, y, fra_w(TOP, "2x + 10", s), s)
        andar(c, t, C["s16"] + 0.2, "x^2 − 25", cx, y, s, True, t1=a6)
        andar(c, t, a6 + 0.3, TOP, cx, y, s, True)
        andar(c, t, C["s16"] + 0.2, "2x + 10", cx, y, s, False, t1=b6)
        andar(c, t, b6 + 0.3, BOT, cx, y, s, False)
        E.foco(c, t, a6 + 0.3, 0.45, lambda p: E.escreve(c, "diferença de quadrados", 1150, y - 70, 52, "i", TINTA2, p))
        E.foco(c, t, b6 + 0.3, 0.45, lambda p: E.escreve(c, "o 2 em evidência", 1150, y + 120, 52, "i", TINTA2, p))
        realce_f(c, t, c6 - 0.3, TOP, "(x + 5)", cx, y, s, True)
        realce_f(c, t, c6 - 0.3, BOT, "(x + 5)", cx, y, s, False)
        corta_f(c, t, c6, TOP, "(x + 5)", cx, y, s, True)
        corta_f(c, t, c6 + 0.2, BOT, "(x + 5)", cx, y, s, False)
        E.frase(c, t, d6 - 0.5, ps("resposta:", "i", 70), XE, 900, passo=0.1)
        fra_em(c, t, d6, "x − 5", "2", 760, 860, 120, CERTO)
    fase(c, t, C["s16"], C["s17"] - 0.1, s16)

    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")

    def s17():
        E.frase(c, t, C["s17"] + 0.2, ps("o proibido zera o de baixo original", "i", 66, TINTA2), XE, 170, passo=0.1)
        form(c, t, a7, "2(x + 5) = 0", XE, 330, 100, ERRADO)
        E.foco(c, t, a7 + 0.5, 0.45, lambda p: E.escreve(c, "quando x = −5", XE + 680, 325, 70, "i", ERRADO, p))
        proibido(c, t, entre(a7, b7, 0.7), "x ≠ −5", 1600, 300, 62)
        E.frase(c, t, b7 - 0.5, ps("com 10:", "i", 62, TINTA2), XE, 560, passo=0.1)
        fra_em(c, t, b7, "75", "30", 540, 560, 100)
        form(c, t, c7 - 0.2, "=", 655, 600, 100)
        fra_em(c, t, c7, "5", "2", 800, 560, 100)
        E.foco(c, t, c7 + 0.3, 0.45, lambda p: centro(c, "÷ 15", 683, 510, 44, "i", TINTA2, p))
        fra_em(c, t, d7, "10 − 5", "2", 1180, 560, 100)
        form(c, t, d7 + 0.4, "=", 1355, 600, 100)
        fra_em(c, t, d7 + 0.6, "5", "2", 1490, 560, 100, CERTO)
        E.foco(c, t, d7 + 1.2, 0.45, lambda p: E.selo(c, 1630, 570, 44, True, p))
    fase(c, t, C["s17"], 1e9, s17)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]

    def resumo():
        E.frase(c, t, C["s18"] + 0.2, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        for k, (tk, partes) in enumerate(((a8, ps("fatore", "g", 76, COR) + ps("em cima e embaixo", "i", 76)),
                                          (b8, ps("corte só", "i", 76) + ps("fatores,", "g", 76, COR) + ps("nunca parcelas", "i", 76)),
                                          (c8, ps("anote o", "i", 76) + ps("valor proibido", "g", 76, ERRADO)))):
            yy = 430 + k * 200
            E.foco(c, t, tk, 0.5, lambda p, k=k, yy=yy: num_bola(c, str(k + 1), 230, yy - 30, 58, 66, p))
            E.frase(c, t, tk + 0.1, partes, 320, yy, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    a_, b_, c_, d_ = (C[f"s19.{k}"] for k in "abcd")
    E.frase(c, t, C["s19"] + 0.2, ps("próxima aula: a raiz sai de baixo", "i", 80), XE, 230, passo=0.1)
    E.frase(c, t, a_, ps("racionalizar", "g", 110, COR), XE, 400)
    fra_em(c, t, b_, "1", "r{2}", XE + 90, 620, 120)
    form(c, t, b_ + 0.4, "=", XE + 220, 660, 120)
    fra_em(c, t, b_ + 0.7, "r{2}", "2", XE + 410, 620, 120, COR)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 600, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(890, 645, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), 1450, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, numeros=b_numeros, algebrica=b_algebrica, proibido=b_proibido,
              exemplo=b_exemplo, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
