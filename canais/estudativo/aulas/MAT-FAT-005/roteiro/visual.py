"""Visual — Estudativo · MAT-FAT-005: racionalizar denominadores, pela raiz e pelo conjugado.
1/√2 ≈ 1/1,4 vira √2/2 ≈ 0,7; a fração "que vale 1" (√2/√2) multiplicando em cima e embaixo; 6/√3 = 2√3; o conjugado de
√3 − 1, com o sinal do meio trocado, e a soma vezes diferença apagando o meio embaixo; a conferência; o erro de multiplicar
só embaixo; no palco, o de baixo final antes da conta.

Convenções da trilha (continuam as de MAT-FAT-004: fra, andar, corta_f, proibido):
- MULTIPLICAR EM CIMA E EMBAIXO: a fração "que vale 1" entra na cor da matéria, com "× " antes e "= 1" embaixo (vezes_um);
- CONJUGADO: os mesmos termos, um embaixo do outro; o sinal do meio trocado ganha realce da cor da matéria e a pílula
  "conjugado"; o produto dos dois mostra a soma vezes diferença apagando o meio.
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-005_racionalizar_denominadores.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("nome", "raiz", "conjugado", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"

r2, r3, r5 = math.sqrt(2), math.sqrt(3), math.sqrt(5)
assert abs(1 / r2 - r2 / 2) < 1e-12 and round(r2, 1) == 1.4 and round(r2 / 2, 1) == 0.7
assert abs(6 / r3 - 2 * r3) < 1e-12 and abs((r3 - 1) * r3 - (3 - r3)) < 1e-12
assert abs((r3 - 1) * (r3 + 1) - 2) < 1e-12 and abs(2 / (r3 - 1) - (r3 + 1)) < 1e-12
assert abs(1 / r5 - r5 / 5) < 1e-12 and abs((r5 + r2) * (r5 - r2) - 3) < 1e-12
assert abs(4 / (r5 + 1) - (r5 - 1)) < 1e-12 and abs((r5 + 1) * r5 - (5 + r5)) < 1e-12
del r2, r3, r5


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


def vezes_um(c, t, t0, s, x, y, size, um=True, cor=None):
    """multiplicar em cima e embaixo (convenção da trilha): "× " e a fração s/s na cor da matéria, com "= 1" embaixo.
    x = borda esquerda do "×"; devolve a largura total"""
    wx = fw("× ", size)
    w = fra_w(s, s, size)
    form(c, t, t0, "×", x, y + size * 0.3, size, cor or COR)
    fra_em(c, t, t0, s, s, x + wx + w / 2, y, size, cor or COR)
    if um:
        E.foco(c, t, t0 + 0.5, 0.4, lambda p: centro(c, "= 1", x + wx + w / 2, y + size * 1.75, size * 0.45, "i", cor or COR, p))
    return wx + w


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s01.{k}"] for k in "abcd")

    def conta():
        fra_em(c, t, a_, "1", "r{2}", 420, 440, 190)
        form(c, t, b_, "r{2} ≈ 1,4", XE, 860, 90, TINTA2)
        E.frase(c, t, entre(b_, c_, 0.45), ps("dividir por 1,4 à mão dá trabalho", "i", 58, TINTA2), XE, 960, passo=0.08)
        form(c, t, c_ - 0.2, "=", 620, 500, 170)
        fra_em(c, t, c_, "r{2}", "2", 900, 440, 190, CERTO)
        form(c, t, d_, "≈ 0,7", 1130, 500, 150, CERTO)
        E.foco(c, t, d_ + 0.4, 0.45, lambda p: E.escreve(c, "a metade de 1,4", 1140, 640, 58, "i", COR, p))
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2 = C["s02.a"], C["s02.b"]
    E.frase(c, t, a2, ps("até o fim desta aula, você", "i", 84), XE, 260, passo=0.12)
    E.frase(c, t, a2 + 1.0, ps("tira a raiz de baixo da fração", "g", 88, COR), XE, 410, passo=0.13)
    E.frase(c, t, b2, ps("até com soma ou subtração", "i", 80), XE, 580, passo=0.12)
    fra_em(c, t, b2 + 0.6, "2", "r{3} − 1", 1500, 760, 130, COR)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s03.{k}"] for k in "abcd")
    E.frase(c, t, a_, ps("três", "g", 84, COR) + ps("ferramentas", "i", 90), XE, 180)
    xr = XE + 110
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "1", XE + 40, 330, 40, 50, p))
    E.frase(c, t, b_, ps("× em cima e embaixo pelo mesmo número: a fração não muda", "i", 54), xr, 352, passo=0.07)
    form(c, t, b_ + 1.0, "f{1}{2} = f{1 · 3}{2 · 3} = f{3}{6}", xr + 20, 490, 76)
    E.foco(c, t, c_, 0.45, lambda p: num_bola(c, "2", XE + 40, 640, 40, 50, p))
    form(c, t, c_ + 0.1, "r{2} · r{2} = 2", xr, 670, 90)
    E.foco(c, t, d_, 0.45, lambda p: num_bola(c, "3", XE + 40, 820, 40, 50, p))
    form(c, t, d_ + 0.1, "(a + b)(a − b) = a^2 − b^2", xr, 850, 90)
    E.frase(c, t, C["s04"] - 2.2, ps("faltou alguma? procure no canal", "i", 54, TINTA2), 1150, 1000, passo=0.08)


# ---------------- o nome ----------------
def b_nome(c, t, C, b):
    a_, b_, c_ = C["s04.a"], C["s04.b"], C["s04.c"]
    E.frase(c, t, a_, ps("racionalizar", "g", 120, COR), XE, 260)
    E.frase(c, t, b_, ps("número racional:", "g", 64) + ps("fração de números inteiros", "i", 64), XE, 430, passo=0.1)
    form(c, t, b_ + 1.0, "f{3}{4}", XE + 60, 600, 100, CERTO)
    form(c, t, b_ + 1.3, "5 = f{5}{1}", XE + 300, 600, 100, CERTO)
    form(c, t, entre(b_, c_, 0.7), "r{2}", XE + 820, 600, 100, ERRADO)
    E.foco(c, t, entre(b_, c_, 0.7) + 0.3, 0.45, lambda p: E.escreve(c, "não pode", XE + 1010, 590, 60, "i", ERRADO, p))
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "o de baixo sem raiz, sem mudar o valor", W / 2, 880, 70, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))


# ---------------- raiz sozinha ----------------
def b_raiz(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    s, y = 130, 470

    def s0506():
        E.frase(c, t, a5, ps("1º caso:", "g", 70, COR) + ps("raiz sozinha embaixo", "i", 70), XE, 170, passo=0.1)
        fra_em(c, t, b5, "1", "r{2}", 330, y, s)
        vezes_um(c, t, c5, "r{2}", 460, y, s)
        E.foco(c, t, d5, 0.45, lambda p: E.escreve(c, "× 1 não muda o valor", XE, 770, 60, "i", COR, p))
        form(c, t, a6 - 0.2, "=", 900, y + 45, s)
        cx = 1130
        barra_f(c, t, a6, cx, y, fra_w("r{2}", "2", s), s)
        andar(c, t, a6, "r{2}", cx, y, s, True)
        andar(c, t, b6, "2", cx, y, s, False, CERTO)
        form(c, t, a6 + 0.3, "em cima: 1 · r{2} = r{2}", XE, 900, 64, TINTA2)
        form(c, t, b6 + 0.3, "embaixo: r{2} · r{2} = 2", XE + 820, 900, 64, TINTA2)
        realce_f(c, t, c6, "2", "2", cx, y, s, False, CERTO)
        E.foco(c, t, c6 + 0.3, 0.45, lambda p: E.pilula(c, "sem raiz embaixo", 1530, 470, 60, estilo="g", fundo=CERTO, cor=BR, a=p))
    fase(c, t, C["s05"], C["s07"] - 0.1, s0506)

    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")

    def s07():
        E.frase(c, t, C["s07"] + 0.2, ps("outro", "i", 76, TINTA2), XE, 170, passo=0.1)
        fra_em(c, t, a7, "6", "r{3}", 330, y, s)
        vezes_um(c, t, b7, "r{3}", 460, y, s, um=False)
        form(c, t, c7 - 0.2, "=", 900, y + 45, s)
        fra_em(c, t, c7, "6r{3}", "3", 1150, y, s)
        realce_f(c, t, d7, "6r{3}", "6", 1150, y, s, True)
        realce_f(c, t, d7, "3", "3", 1150, y, s, False)
        form(c, t, d7 + 0.3, "6 ÷ 3 = 2", 1400, 380, 70, TINTA2)
        form(c, t, e7, "= 2r{3}", 1400, y + 45, s, CERTO)
    fase(c, t, C["s07"], 1e9, s07)


# ---------------- conjugado ----------------
D3 = "r{3} − 1"
K3 = "r{3} + 1"


def b_conjugado(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    s, y = 120, 460

    def s08():
        E.frase(c, t, a8, ps("2º caso:", "g", 70, COR) + ps("soma ou subtração embaixo", "i", 70), XE, 170, passo=0.1)
        fra_em(c, t, b8, "2", D3, 400, y, s)
        tm = entre(b8, c8, 0.4)
        vezes_um(c, t, tm, "r{3}", 640, y, s, um=False, cor=ERRADO)
        E.frase(c, t, c8 - 0.4, ps("embaixo ficaria", "i", 62, TINTA2), XE, 860, passo=0.1)
        form(c, t, c8, "(r{3} − 1) · r{3} = 3 − r{3}", XE + 480, 870, 96, ERRADO)
        E.foco(c, t, c8 + 0.8, 0.45, lambda p: E.pilula(c, "ainda com raiz", 1500, 720, 60, estilo="g", fundo=ERRADO, cor=BR, a=p))
    fase(c, t, C["s08"], C["s09"] - 0.1, s08)

    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")

    def s09():
        E.frase(c, t, a9, ps("conjugado:", "g", 72, COR) + ps("os mesmos termos, sinal do meio trocado", "i", 66), XE, 170, passo=0.1)
        form(c, t, a9 + 0.4, D3, XE + 60, 380, 120)
        form(c, t, b9, K3, XE + 60, 560, 120, COR)
        realce(c, t, b9 + 0.3, K3, "+", XE + 60, 560, 120)
        realce(c, t, b9 + 0.3, D3, "−", XE + 60, 380, 120, TINTA2)
        E.foco(c, t, b9 + 0.5, 0.45, lambda p: E.pilula(c, "conjugado", XE + 650, 520, 56, estilo="g", a=p))
        E.frase(c, t, c9, ps("soma × diferença:", "i", 62, TINTA2), 1000, 330, passo=0.1)
        form(c, t, c9 + 0.5, "(r{3} − 1)(r{3} + 1)", 1000, 470, 90)
        form(c, t, d9, "= (r{3})^2 − 1^2", 1000, 620, 90)
        form(c, t, e9, "= 3 − 1 = 2", 1000, 770, 110, CERTO)
        E.foco(c, t, e9 + 0.6, 0.45, lambda p: E.escreve(c, "o meio sumiu: sem raiz", 1000, 890, 56, "i", CERTO, p))
    fase(c, t, C["s09"], C["s10"] - 0.1, s09)

    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]

    def s10():
        s2, y2 = 100, 450
        fra(c, "2", D3, 290, y2, s2, ep(t, C["s10"] + 0.1, 0.4))
        vezes_um(c, t, C["s10"] + 0.1, K3, 490, y2, s2, um=False)
        form(c, t, a0 - 0.2, "=", 950, y2 + 40, s2)
        TOP = "2(r{3} + 1)"
        cx = 1330
        barra_f(c, t, a0, cx, y2, fra_w(TOP, "2", s2), s2)
        andar(c, t, a0, TOP, cx, y2, s2, True)
        andar(c, t, a0 + 0.8, "2", cx, y2, s2, False)
        corta_f(c, t, b0, TOP, "2", cx, y2, s2, True)
        corta_f(c, t, b0 + 0.2, "2", "2", cx, y2, s2, False)
        E.frase(c, t, b0 + 0.3, ps("÷ 2 em cima e embaixo", "i", 56, TINTA2), 1080, 760, passo=0.08)
        E.frase(c, t, c0 - 0.4, ps("resposta:", "i", 72), XE, 900, passo=0.1)
        form(c, t, c0, "r{3} + 1", XE + 380, 910, 140, CERTO)
    fase(c, t, C["s10"], C["s11"] - 0.1, s10)

    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]

    def s11():
        E.frase(c, t, a1, ps("confira: resposta × de baixo original = de cima", "i", 66, TINTA2), XE, 200, passo=0.08)
        form(c, t, b1, "(r{3} + 1)(r{3} − 1)", XE, 480, 120)
        form(c, t, c1, "= 3 − 1 = 2", XE + fw("(r{3} + 1)(r{3} − 1) ", 120), 480, 120, CERTO)
        E.foco(c, t, c1 + 0.8, 0.45, lambda p: E.selo(c, 1700, 440, 56, True, p))
        E.foco(c, t, c1 + 0.8, 0.45, lambda p: E.escreve(c, "o 2 de cima", XE + fw("(r{3} + 1)(r{3} − 1) = 3 − 1 = ", 120) - 120, 620, 56, "i", CERTO, p))
    fase(c, t, C["s11"], 1e9, s11)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s12.{k}"] for k in "abcde")
    s, y = 130, 470
    E.frase(c, t, C["s12"] + 0.3, ps("o erro mais comum:", "g", 80, ERRADO) + ps("multiplicar só embaixo", "i", 80), XE, 170, passo=0.1)
    fra_em(c, t, a_ + 0.3, "1", "r{2}", 330, y, s)
    form(c, t, b_ - 0.2, "→", 470, y + 45, s, ERRADO)
    fra_em(c, t, b_, "1", "2", 700, y, s, ERRADO)
    if t >= b_ + 0.8:
        E.risco(c, 620, y + s * 1.2, 780, y - s * 0.9, t, b_ + 0.8, largura=11)
    form(c, t, c_, "f{1}{2} = 0,5", 1050, 400, 96, ERRADO)
    form(c, t, d_, "f{1}{r{2}} ≈ 0,7", 1050, 640, 96, CERTO)
    E.foco(c, t, e_, 0.5, lambda p: E.pilula(c, "o de baixo multiplicou? o de cima acompanha", W / 2, 920, 64, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")

    def s13():
        E.frase(c, t, C["s13"] + 0.2, ps("o atalho:", "i", 72, CLARO) + ps("o de baixo final, antes da conta", "g", 66, BR), XE, 170, passo=0.1)
        E.foco(c, t, b3, 0.45, lambda p: num_bola(c, "1", XE + 40, 330, 36, 46, p, AM, "#07070F"))
        E.frase(c, t, b3, ps("raiz sozinha: fica o número de dentro", "i", 62, CLARO), XE + 100, 352, passo=0.08)
        fra(c, "1", "r{5}", 400, 520, 100, ep(t, c3, 0.4), BR)
        form(c, t, c3 + 0.3, "→", 530, 560, 100, AM)
        fra(c, "r{5}", "5", 760, 520, 100, ep(t, c3 + 0.5, 0.4), AM)
        E.foco(c, t, d3, 0.45, lambda p: num_bola(c, "2", XE + 40, 740, 36, 46, p, AM, "#07070F"))
        E.frase(c, t, d3, ps("conjugado: quadrado do 1º − quadrado do 2º", "i", 62, CLARO), XE + 100, 762, passo=0.08)
        form(c, t, e3 - 0.3, "r{5} + r{2}", XE + 100, 920, 100, BR)
        form(c, t, e3, "→ 5 − 2 = 3", XE + 100 + fw("r{5} + r{2} ", 100), 920, 100, AM)
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)

    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]

    def s14():
        E.frase(c, t, C["s14"] + 0.2, ps("funciona porque", "i", 76, CLARO), XE, 180, passo=0.1)
        form(c, t, a4, "r{a} · r{a} = a", XE, 360, 100, BR)
        E.frase(c, t, a4 + 0.5, ps("devolve o número de dentro", "i", 58, CLARO), XE + 720, 350, passo=0.08)
        form(c, t, b4, "(a + b)(a − b) = a^2 − b^2", XE, 540, 100, BR)
        E.frase(c, t, b4 + 0.5, ps("apaga o meio", "i", 58, CLARO), XE + 1300, 530, passo=0.08)
        E.foco(c, t, c4, 0.45, lambda p: E.selo(c, XE + 40, 750, 40, False, p))
        E.frase(c, t, c4, ps("alternativas com raiz embaixo?", "g", 62, BR), XE + 110, 770, passo=0.08)
        E.frase(c, t, c4 + 1.0, ps("compare do jeito que está", "i", 62, AM), XE + 110, 870, passo=0.08)
    fase(c, t, C["s14"], 1e9, s14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_ = C["s15.a"]
    E.frase(c, t, C["s15"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 220)
    E.frase(c, t, a_ - 0.4, ps("racionalize", "i", 100), XE, 430)
    fra_em(c, t, a_, "4", "r{5} + 1", 480, 640, 140, COR)
    E.relogio(c, t, C["s16.a"], 1520, 450, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    s, y = 100, 460

    def s17():
        fra(c, "4", "r{5} + 1", 290, y, s, ep(t, C["s17"] + 0.1, 0.4))
        vezes_um(c, t, a7, "r{5} − 1", 490, y, s, um=False)
        realce_f(c, t, a7 + 0.3, "r{5} − 1", "−", 490 + fw("× ", s) + fra_w("r{5} − 1", "r{5} − 1", s) / 2, y, s, False)
        E.foco(c, t, a7 + 0.4, 0.45, lambda p: E.pilula(c, "conjugado", 670, 230, 52, estilo="g", a=p))
        form(c, t, b7 - 0.2, "=", 950, y + 40, s)
        TOP = "4(r{5} − 1)"
        cx = 1330
        barra_f(c, t, b7, cx, y, fra_w(TOP, "4", s), s)
        andar(c, t, b7, "4", cx, y, s, False)
        E.foco(c, t, b7 + 0.3, 0.45, lambda p: E.escreve(c, "5 − 1 = 4", 1530, y + 100, 56, "i", TINTA2, p))
        andar(c, t, c7, TOP, cx, y, s, True)
        corta_f(c, t, d7, TOP, "4", cx, y, s, True)
        corta_f(c, t, d7 + 0.2, "4", "4", cx, y, s, False)
        E.frase(c, t, e7 - 0.4, ps("resposta:", "i", 72), XE, 900, passo=0.1)
        form(c, t, e7, "r{5} − 1", XE + 380, 910, 140, CERTO)
    fase(c, t, C["s17"], C["s18"] - 0.1, s17)

    a8, b8 = C["s18.a"], C["s18.b"]

    def s18():
        E.frase(c, t, C["s18"] + 0.2, ps("quem multiplicou só por", "i", 66, TINTA2), XE, 220, passo=0.1)
        form(c, t, C["s18"] + 0.6, "r{5}", XE + 720, 225, 80, TINTA2)
        F = "(r{5} + 1) · r{5} = 5 + r{5}"
        form(c, t, a8, F, XE, 520, 120, ERRADO)
        realce(c, t, b8, F, "r{5}", XE + fw("(r{5} + 1) · r{5} = 5 + ", 120), 520, 120, ERRADO)
        E.foco(c, t, b8 + 0.2, 0.45, lambda p: E.escreve(c, "a raiz continuou lá", XE + 900, 700, 66, "b", ERRADO, p))
    fase(c, t, C["s18"], 1e9, s18)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]

    def resumo():
        E.frase(c, t, C["s19"] + 0.2, ps("resumindo", "i", 96, COR), W / 2, 200, "center")
        E.foco(c, t, a9, 0.5, lambda p: num_bola(c, "1", 230, 380, 58, 66, p))
        E.frase(c, t, a9 + 0.1, ps("raiz sozinha:", "i", 74) + ps("× a própria raiz", "g", 72, COR), 320, 410, passo=0.12)
        E.foco(c, t, b9, 0.5, lambda p: num_bola(c, "2", 230, 580, 58, 66, p))
        E.frase(c, t, b9 + 0.1, ps("soma ou subtração:", "i", 74) + ps("× o conjugado", "g", 72, COR), 320, 610, passo=0.12)
        E.foco(c, t, c9, 0.5, lambda p: num_bola(c, "3", 230, 780, 58, 66, p))
        E.frase(c, t, c9 + 0.1, ps("sempre", "i", 74) + ps("em cima e embaixo", "g", 72, COR), 320, 810, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a_, b_, c_, d_, e_, f_, g_ = (C[f"s20.{k}"] for k in "abcdefg")
    E.frase(c, t, C["s20"] + 0.2, ps("próxima aula", "i", 84), XE, 200)
    E.frase(c, t, a_, ps("praticar tudo desta parte", "g", 84, COR), XE, 330, passo=0.12)
    for k, (txt, tk) in enumerate((("abrir produtos notáveis", b_), ("fatorar", c_), ("simplificar frações com letra", d_), ("racionalizar", e_))):
        yy = 480 + k * 110
        E.foco(c, t, tk, 0.45, lambda p, k=k, yy=yy: num_bola(c, str(k + 1), XE + 30, yy - 20, 30, 40, p))
        E.frase(c, t, tk, ps(txt, "i", 64), XE + 90, yy, passo=0.1)
    E.foco(c, t, f_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 600, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, f_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(890, 645, p), ep(t, f_ + 0.2, 0.4), TINTA)
    E.frase(c, t, g_, ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), 1450, 950, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nome=b_nome, raiz=b_raiz, conjugado=b_conjugado, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
