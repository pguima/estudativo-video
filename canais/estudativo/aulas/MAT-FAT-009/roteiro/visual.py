"""Visual — Estudativo · MAT-FAT-009: discriminante, quantas raízes a equação tem.
x² + 2x + 5 = 0 sem raiz real com uma conta só; a fórmula de Bhaskara com a raiz de delta realçada; os três casos, cada um
com a pílula do sinal, a contagem com bolinhas e as raízes na reta (o centro −b/2a e os saltos de ± √Δ/2a); x² − 6x + 9 =
(x − 3)² com a raiz repetida; k = 4 para x² − 4x + k = 0; o erro de achar que Δ = 0 é nenhuma raiz; no palco, o atalho
dos sinais de a e c.

Convenções da trilha (as de MAT-FAT-004 a 008: coeficientes coloridos, delta_f, bhaskara_f, delta_pilula, raizes).
Nova: QUANTAS RAÍZES = pílula escura do sinal ("Δ > 0"), seta e a contagem com bolinhas (delta_caso); na reta, o centro
cinza e um salto para cada lado até as raízes verdes (leque).
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math
from fractions import Fraction as Fr

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-009_discriminante_quantas_raizes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "positivo", "k", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"


def _delta(a, b, c):
    return b * b - 4 * a * c


# as contas da aula
assert _delta(1, 2, 5) == 4 - 20 == -16
assert _delta(1, -5, 6) == 1 and {2, 3} == {x for x in range(-10, 10) if x * x - 5 * x + 6 == 0}
assert _delta(1, -6, 9) == 36 - 36 == 0 and 6 / 2 == 3 and all(x * x - 6 * x + 9 == (x - 3) ** 2 for x in range(-5, 6))
assert 16 - 4 * 4 == 0 and _delta(1, -4, 4) == 0 and all(x * x - 4 * x + 4 == (x - 2) ** 2 for x in range(-5, 6))
assert 9 - 18 + 9 == 0
assert _delta(2, 7, -3) == 49 + 24 > 0
assert _delta(1, -4, 5) == 16 - 20 == -4 and _delta(1, 10, 25) == 100 - 100 == 0 and -10 / 2 == -5
assert 36 - 4 * 9 == 0 and all(x * x + 6 * x + 9 == (x + 3) ** 2 for x in range(-5, 6))
assert _delta(1, -2, -1) == 8  # a próxima aula: x(x − 2) = 1 → x = 1 ± √2


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

def questao(c, t, t0, n, rot=None):
    """etiqueta da questão (convenção das práticas): pílula "questão n" e o assunto em itálico ao lado"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"questão {n}", XE + 150, 150, 52, estilo="g", a=a), sobe=8)
    if rot:
        E.frase(c, t, t0 + 0.3, ps(rot, "i", 64, TINTA2), XE + 340, 168, passo=0.08)


def selo_em(c, t, t0, cx, cy, r, ok=True):
    E.foco(c, t, t0, 0.45, lambda p: E.selo(c, cx, cy, r, ok, p))


def nota(c, t, t0, s, x, y, size=52, cor=None, est="i", align="left"):
    """texto de apoio parado que entra com foco"""
    if align == "center":
        E.foco(c, t, t0, 0.45, lambda p: centro(c, s, x, y, size, est, cor or TINTA2, p))
    else:
        E.foco(c, t, t0, 0.45, lambda p: E.escreve(c, s, x, y, size, est, cor or TINTA2, p))


def fim_padrao(c, t, C, resumo_id, prox_id, itens, prox_l1, prox_big, extra=None, k_ins="d", k_bons="e"):
    """resumo numerado (itens = [(cue, partes)]) e a ponte para a próxima aula com Inscreva-se"""
    def resumo():
        E.frase(c, t, C[resumo_id] + 0.2, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        for k, (tk, partes) in enumerate(itens):
            yy = 430 + k * 200
            E.foco(c, t, tk, 0.5, lambda p, k=k, yy=yy: num_bola(c, str(k + 1), 230, yy - 30, 58, 66, p))
            E.frase(c, t, tk + 0.1, partes, 320, yy, passo=0.12)
    E.saida(c, t, C[prox_id] - 0.1, resumo)
    if t < C[prox_id]:
        return
    E.frase(c, t, C[prox_id] + 0.2, ps(prox_l1, "i", 80), XE, 230, passo=0.1)
    E.frase(c, t, C[prox_id + ".a"], ps(prox_big, "g", 100, COR), XE, 390, passo=0.12)
    if extra:
        extra()
    ci = C[prox_id + "." + k_ins]
    E.foco(c, t, ci, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 600, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, ci + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(890, 645, p), ep(t, ci + 0.2, 0.4), TINTA)
    E.frase(c, t, C[prox_id + "." + k_bons], ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), 1450, 950, "center")


# ---------------- peças da equação do 2º grau (convenção da trilha, desde MAT-FAT-007) ----------------
# COEFICIENTES: á na cor da matéria, bê em magenta, cê em âmbar, no papel; no palco, as versões claras.
CA, CB, CC = E.COR, "#C2187A", "#B86E00"
CA_L, CB_L, CC_L = E.CLARO, "#FF8CC6", "#FFC861"


def pf(s, t0, cor=None):
    """pedaço de fórmula para monta()"""
    return (s, t0, cor) if cor else (s, t0)


def fra_p(c, cima, baixo, cx, y, size, a=1.0, cor_barra=None):
    """fração em dois andares com cada andar em pedaços coloridos: cima/baixo = [(texto, cor), ...]; y = altura da barra"""
    if a <= 0:
        return 0
    wc = sum(fw(s, size) for s, _ in cima)
    wb = sum(fw(s, size) for s, _ in baixo)
    w = max(wc, wb) + size * 0.3
    for pecas, ww, yy in ((cima, wc, y - size * 0.32), (baixo, wb, y + size * 0.98)):
        x = cx - ww / 2
        for s, cor in pecas:
            E.formula(c, s, x, yy, size, cor=cor or TINTA, a=a)
            x += fw(s, size)
    b = max(5, size * 0.07)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y - b / 2, w, b), b / 2, b / 2), M.paint(cor_barra or TINTA, a))
    return w


def fra_p_w(cima, baixo, size):
    return max(sum(fw(s, size) for s, _ in cima), sum(fw(s, size) for s, _ in baixo)) + size * 0.3


def fra_p_em(c, t, t0, cima, baixo, cx, y, size, cor_barra=None):
    E.foco(c, t, t0, 0.5, lambda p: fra_p(c, cima, baixo, cx, y, size, p, cor_barra))


def raizes(c, t, t0, vals, x, y, size, cor=CERTO, align="left", t1=None, var="x"):
    """as raízes (convenção da trilha): "x = 7  ou  x = −7", o "ou" em itálico; a segunda entra em t1"""
    partes = [f"{var} = {v}" for v in vals]
    gap = size * 0.5
    wou = E.larg("ou", "i", size * 0.8)
    total = sum(fw(p, size) for p in partes) + (len(partes) - 1) * (wou + 2 * gap)
    xx = x - total / 2 if align == "center" else x
    for i, p in enumerate(partes):
        ti = t0 if i == 0 else (t1 if t1 is not None else t0 + 0.5 * i)
        if i > 0:
            E.foco(c, t, ti, 0.4, lambda q, xx=xx: E.escreve(c, "ou", xx + gap, y, size * 0.8, "i", TINTA2, q))
            xx += wou + 2 * gap
        form(c, t, ti, p, xx, y, size, cor)
        xx += fw(p, size)
    return total


def nos_dois(c, t, t0, s, op, x, y, size, cor=None, align="left"):
    """o mesmo nos dois lados (balança): pílula com a operação embaixo de cada lado da equação s"""
    i = s.index("=")
    xi = x - fw(s, size) / 2 if align == "center" else x
    x0, we = xi, fw(s[:i].strip(), size)
    x1, wd = xi + fw(s[:i + 2], size), fw(s[i + 2:], size)
    for k, (xx, ww) in enumerate(((x0, we), (x1, wd))):
        E.foco(c, t, t0 + 0.15 * k, 0.4, lambda p, xx=xx, ww=ww: E.pilula(c, op, xx + ww / 2, y + size * 0.62, size * 0.42, estilo="g", fundo=cor or E.COR, cor=BR, a=p), sobe=8)


def ramo(c, t, t0, s, fator, x, y, size, x1, y1, cor=None, align="left", n=0):
    """seta do fator de s (produto igual a zero) até a linha do ramo em (x1, y1)"""
    xf, wf = trecho_x(s, fator, x, size, align, n)
    p = ep(t, t0, 0.5)
    M.arrow(c, xf + wf / 2, y + size * 0.3, x1, y1 - size * 0.75, cor or FIO, p, 5, 16, p)


def regra_zero(c, t, t0, cx, cy, size=50):
    """produto zero (convenção da trilha): se uma multiplicação dá zero, algum fator vale zero"""
    E.foco(c, t, t0, 0.45, lambda p: E.pilula(c, "produto = 0  →  algum fator = 0", cx, cy, size, estilo="g", fundo=TINTA, cor=BR, a=p), sobe=8)


def coef(c, t, t0, letra, valor, cx, cy, size=50, cor=None):
    """pílula do coeficiente: "a = 2" na cor da letra"""
    cor = cor or {"a": CA, "b": CB, "c": CC}[letra]
    E.foco(c, t, t0, 0.45, lambda p: E.pilula(c, f"{letra} = {valor}", cx, cy, size, estilo="g", fundo=cor, cor=BR, a=p), sobe=8)


# ---------------- delta e Bhaskara (convenção da trilha, desde MAT-FAT-008) ----------------
# FÓRMULAS: Δ = b² − 4ac e x = (−b ± √Δ)/2a com as letras nas cores dos coeficientes (delta_f, bhaskara_f).
# SUBSTITUIR: cada número entra entre parênteses na cor da letra que ele substitui (subst).
# DELTA: o valor do delta numa pílula escura "Δ = 1" (delta_pilula); com o sinal, a pílula diz quantas raízes (MAT-FAT-009).
# MAIS OU MENOS: a conta se divide em duas linhas, com as pílulas "com +" e "com −" (pm).
def delta_f(c, t, t0, x, y, size, align="left", tinta=None, cores=(CA, CB, CC), d=0.0):
    ca, cb, cc = cores
    k = tinta or TINTA
    return monta(c, t, [("Δ = ", t0, k), ("b", t0 + d, cb), ("^2 − 4", t0 + d, k), ("a", t0 + 2 * d, ca), ("c", t0 + 2 * d, cc)], x, y, size, align)


def bhaskara_f(c, t, t0, x, y, size, tinta=None, cores=(CA, CB, CC), t1=None):
    """x = (−b ± √Δ)/2a; y = linha de base do "x ="; o de baixo (2a) entra em t1"""
    ca, cb, _ = cores
    k = tinta or TINTA
    form(c, t, t0, "x =", x, y, size, k)
    cima, baixo = [("−", k), ("b", cb), (" ± r{Δ}", k)], [("2", k), ("a", ca)]
    s2 = size * 0.85
    xf = x + fw("x = ", size) + fra_p_w(cima, baixo, s2) / 2
    yb_ = y - size * 0.32
    if t1 is None:
        fra_p_em(c, t, t0 + 0.2, cima, baixo, xf, yb_, s2, k)
    else:
        w = fra_p_w(cima, baixo, s2)
        E.foco(c, t, t0 + 0.2, 0.5, lambda p: fra_p(c, cima, [], xf, yb_, s2, p, k) and None)

        def embaixo(p):
            xx = xf - sum(fw(q, s2) for q, _ in baixo) / 2
            for q, cr in baixo:
                E.formula(c, q, xx, yb_ + s2 * 0.98, s2, cor=cr, a=p)
                xx += fw(q, s2)
        E.foco(c, t, t1, 0.45, embaixo)
    return fw("x = ", size) + fra_p_w(cima, baixo, s2)


def subst(c, t, t0, cima, baixo, x, y, size, tinta=None):
    """x = fração com os números no lugar das letras; cima/baixo = [(texto, cor)]; y = linha de base do "x =" """
    k = tinta or TINTA
    form(c, t, t0, "x =", x, y, size, k)
    s2 = size * 0.85
    w = fra_p_w(cima, baixo, s2)
    fra_p_em(c, t, t0 + 0.2, cima, baixo, x + fw("x = ", size) + w / 2, y - size * 0.32, s2, k)
    return fw("x = ", size) + w


def delta_pilula(c, t, t0, valor, cx, cy, size=56, fundo=None, cor=None):
    E.foco(c, t, t0, 0.45, lambda p: E.pilula(c, f"Δ = {valor}", cx, cy, size, estilo="g", fundo=fundo or TINTA, cor=cor or BR, a=p), sobe=8)


def pm(c, t, t0, sinal, conta, x, y, size, cor=None, t1=None, final=None, cor_final=CERTO, fundo=None):
    """uma das duas contas do ±: pílula "com +" ou "com −" e a conta; final = resultado que entra em t1"""
    E.foco(c, t, t0, 0.4, lambda p: E.pilula(c, f"com {sinal}", x + 80, y - size * 0.32, size * 0.42, estilo="g", fundo=fundo or E.COR, cor=BR, a=p), sobe=8)
    form(c, t, t0 + 0.2, conta, x + 190, y, size, cor)
    if final:
        form(c, t, t1 if t1 is not None else t0 + 1.2, final, x + 190 + fw(conta + " ", size), y, size, cor_final)


# DELTA E QUANTAS RAÍZES (convenção da trilha, desde MAT-FAT-009): a pílula escura do sinal ("Δ > 0"), uma seta e a
# pílula da contagem, com bolinhas: duas, uma, ou um círculo tracejado vazio (nenhuma raiz real).
CASOS = {">": ("Δ > 0", "2 raízes reais", 2), "=": ("Δ = 0", "1 raiz (dupla)", 1), "<": ("Δ < 0", "nenhuma raiz real", 0)}


def bolinhas(c, n, x, cy, r=20, a=1.0, cor=None):
    """n raízes como bolinhas a partir de x; n = 0 é um círculo tracejado vazio. Devolve a largura"""
    if a <= 0:
        return 0
    if n == 0:
        p = M.paint(TINTA2, a, stroke=4)
        p.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
        c.drawCircle(x + r, cy, r, p)
        return 2 * r
    for i in range(n):
        E.bola(c, x + r + i * (2 * r + 14), cy, r, cor or CERTO, a)
    return n * 2 * r + (n - 1) * 14


def delta_caso(c, t, t0, sinal, x, cy, size=56, t1=None, escuro=False):
    """linha do quadro: pílula "Δ > 0" em x, seta e a contagem com bolinhas (a contagem entra em t1)"""
    txt, cont, n = CASOS[sinal]
    t1 = t1 if t1 is not None else t0 + 0.5
    w1 = E.larg(txt, "g", size) + size * 1.1
    fundo = BR if escuro else TINTA
    tinta = "#07070F" if escuro else BR
    E.foco(c, t, t0, 0.45, lambda p: E.pilula(c, txt, x + w1 / 2, cy, size, estilo="g", fundo=fundo, cor=tinta, a=p), sobe=8)
    xa = x + w1 + 30
    p = ep(t, t1 - 0.2, 0.4)
    if p > 0:
        M.arrow(c, xa, cy, xa + 90, cy, CLARO if escuro else TINTA2, p, 5, 16, p)
    w2 = E.larg(cont, "g", size) + size * 1.1
    cor_c = (TINTA2 if not escuro else "#4A4A66") if n == 0 else E.COR
    E.foco(c, t, t1, 0.45, lambda q: (E.pilula(c, cont, xa + 130 + w2 / 2, cy, size, estilo="g", fundo=cor_c, cor=BR, a=q),
                                      bolinhas(c, n, xa + 130 + w2 + 30, cy, size * 0.36, q)), sobe=8)


def coefs(c, t, t0, vals, cx, cy, size=46, gap=260, dt=0.0, letras="abc"):
    for k, (letra, v) in enumerate(zip(letras, vals)):
        coef(c, t, t0 + k * dt, letra, v, cx + (k - 1) * gap, cy, size, cor={"a": CA, "b": CB, "c": CC, "k": CC}[letra])


def leque(c, t, t0, t1, vmin, vmax, centro_, meia, x0=420, x1=1500, y=860, marcas=None):
    """as raízes na reta: o centro −b/2a em cinza (t0) e, em t1, um salto de cada lado até as raízes verdes.
    meia = 0: a raiz dupla; meia = None: nenhuma raiz real (os saltos não saem e aparece "?")"""
    vx = E.reta(c, t, t0, x0, x1, y, vmin, vmax, marcas or list(range(vmin, vmax + 1)), size=44)
    cx = vx(centro_)
    E.foco(c, t, t0 + 0.4, 0.4, lambda p: c.drawCircle(cx, y, 14, M.paint(TINTA2, p, stroke=5)))
    if meia is None:
        E.foco(c, t, t1, 0.45, lambda p: centro(c, "?", cx, y - 60, 70, "g", ERRADO, p))
        return vx
    if meia == 0:
        E.foco(c, t, t1, 0.45, lambda p: E.bola(c, cx, y, 22, CERTO, p))
        return vx
    for k, d in enumerate((meia, -meia)):
        E.salto(c, t, t1 + 0.3 * k, cx, vx(centro_ + d), y, 70, TINTA2)
        E.foco(c, t, t1 + 0.5 + 0.3 * k, 0.4, lambda p, d=d: E.bola(c, vx(centro_ + d), y, 22, CERTO, p))
    return vx


# ---------------- gancho ----------------
Q0 = "x^2 + 2x + 5 = 0"


def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def conta():
        form(c, t, a_, Q0, W / 2, 380, 150, align="center")
        for k, g in enumerate(("x = 1?", "x = −1?", "x = 2?", "x = −2?")):
            form(c, t, entre(a_, b_, 0.45 + 0.12 * k), g, XE + 60 + k * 420, 560, 70, CINZA)
        E.foco(c, t, b_, 0.5, lambda p: E.pilula(c, "uma conta de 5 segundos", W / 2, 720, 60, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
        selo_em(c, t, c_, 420, 880, 40, False)
        E.frase(c, t, c_, ps("nenhum número da reta", "g", 70, ERRADO) + ps("resolve", "i", 76), 500, 905, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2 = C["s02.a"], C["s02.b"]
    E.frase(c, t, a2, ps("até o fim desta aula, você diz", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a2 + 1.2, ps("quantas raízes", "g", 110, COR), XE, 400, passo=0.13)
    E.frase(c, t, a2 + 1.8, ps("uma equação tem,", "i", 80) + ps("sem resolver", "g", 80, COR), XE, 520, passo=0.12)
    E.frase(c, t, b2 - 1.2, ps("e acha o número que falta para", "i", 66), XE, 700, passo=0.1)
    form(c, t, b2 - 0.3, "x^2 − 4x + ? = 0", XE, 860, 110)
    E.foco(c, t, b2, 0.5, lambda p: E.pilula(c, "uma raiz só", 1450, 825, 64, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_ = C["s03.a"], C["s03.b"]
    E.frase(c, t, C["s03"] + 0.2, ps("você vai usar", "i", 84), XE, 180)
    E.foco(c, t, a_, 0.45, lambda p: num_bola(c, "1", XE + 40, 350, 40, 50, p))
    E.frase(c, t, a_, ps("o delta", "g", 66, COR), XE + 110, 372, passo=0.08)
    delta_f(c, t, a_ + 0.6, XE + 450, 380, 100)
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "2", XE + 40, 600, 40, 50, p))
    E.frase(c, t, b_, ps("raiz de número negativo", "g", 66, COR) + ps("não dá número da reta", "i", 66), XE + 110, 622, passo=0.08)
    form(c, t, b_ + 1.4, "r{−16} = ?", XE + 120, 790, 110, ERRADO)
    nota(c, t, b_ + 2.0, "nenhum número vezes ele mesmo dá negativo", XE + 650, 770, 52)
    E.frase(c, t, C["s04"] - 2.2, ps("faltou alguma? procure no canal", "i", 52, TINTA2), 1150, 1010, passo=0.08)


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    a_, b_, c_ = C["s04.a"], C["s04.b"], C["s04.c"]
    x, y, s = XE + 300, 440, 140
    bhaskara_f(c, t, a_, x, y, s)
    cima = [("−", TINTA), ("b", CB), (" ± r{Δ}", TINTA)]
    s2 = s * 0.85
    xf = x + fw("x = ", s) + fra_p_w(cima, [("2", TINTA), ("a", CA)], s2) / 2
    xr = xf - sum(fw(q, s2) for q, _ in cima) / 2 + fw("−b ± ", s2)
    yc = y - s * 0.32 - s2 * 0.32
    q = ep(t, b_, 0.4)
    if q > 0:
        M.rrect(c, xr - 12, yc - s2 * 1.0, fw("r{Δ}", s2) + 16, s2 * 1.2, 18, E.COR, 0.16 * q)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xr - 12, yc - s2 * 1.0, fw("r{Δ}", s2) + 16, s2 * 1.2), 18, 18), M.paint(E.COR, q, stroke=5))
    E.frase(c, t, b_ + 0.3, ps("tudo depende da", "i", 70) + ps("raiz do delta", "g", 70, COR), XE, 190, passo=0.1)
    E.frase(c, t, c_, ps("Δ:", "g", 90) + ps("discriminante", "g", 100, COR), XE, 790, passo=0.12)
    E.frase(c, t, c_ + 0.8, ps("ele separa os casos", "i", 66, TINTA2), XE, 900, passo=0.1)
    for k, s_ in enumerate(("Δ > 0", "Δ = 0", "Δ < 0")):
        E.foco(c, t, c_ + 1.2 + k * 0.2, 0.45, lambda p, s_=s_, k=k: E.pilula(c, s_, 1150 + k * 260, 880, 54, estilo="g", fundo=TINTA, cor=BR, a=p), sobe=8)


# ---------------- delta positivo ----------------
def b_positivo(c, t, C, b):
    a_, b_, c_ = C["s05.a"], C["s05.b"], C["s05.c"]
    delta_caso(c, t, a_, ">", XE, 190, 64, t1=b_)
    E.frase(c, t, a_ + 0.8, ps("a raiz existe e não é zero", "i", 60, TINTA2), XE, 330, passo=0.08)
    E.frase(c, t, b_ + 0.5, ps("somar e subtrair dão", "i", 60, TINTA2) + ps("resultados diferentes", "g", 60, COR), XE, 420, passo=0.08)
    form(c, t, c_, "x^2 − 5x + 6 = 0", XE, 600, 110)
    delta_pilula(c, t, c_ + 0.6, "1", 1150, 565, 60)
    raizes(c, t, c_ + 1.2, ("2", "3"), 1350, 600, 80, t1=c_ + 1.5)
    leque(c, t, c_ + 0.2, c_ + 1.2, 0, 5, Fr(5, 2), Fr(1, 2), y=850)


# ---------------- delta zero ----------------
Q2 = "x^2 − 6x + 9 = 0"


def b_zero(c, t, C, b):
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")

    def s06():
        delta_caso(c, t, a6, "=", XE, 190, 64, t1=b6)
        E.frase(c, t, a6 + 0.8, ps("a raiz de zero é zero: mais zero e menos zero dão o mesmo", "i", 56, TINTA2), XE, 320, passo=0.07)
        form(c, t, c6, Q2, XE, 500, 110)
        monta(c, t, [pf("Δ = 36 − 36", d6), pf(" = 0", d6 + 0.8, COR)], XE, 650, 96)
        monta(c, t, [pf("x = f{6}{2}", e6), pf(" = 3", e6 + 0.7, CERTO)], 1150, 650, 96)
        leque(c, t, c6 + 0.3, e6 + 0.7, 0, 6, 3, 0, y=880)
    fase(c, t, C["s06"], C["s07"] - 0.1, s06)

    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    P = "(x − 3)(x − 3) = 0"

    def s07():
        form(c, t, C["s07"] + 0.1, Q2, XE, 260, 110)
        E.frase(c, t, a7, ps("trinômio quadrado perfeito", "g", 60, COR), 1150, 250, passo=0.08)
        form(c, t, b7, "(x − 3)^2 = 0", XE, 420, 110, COR)
        form(c, t, entre(b7, c7, 0.45), P, W / 2, 600, 110, align="center")
        realce(c, t, entre(b7, c7, 0.7), P, "(x − 3)", W / 2, 600, 110, align="center")
        realce(c, t, entre(b7, c7, 0.7), P, "(x − 3)", W / 2, 600, 110, align="center", n=1)
        ramo(c, t, c7, P, "(x − 3)", W / 2, 600, 110, 620, 820, align="center")
        ramo(c, t, c7, P, "(x − 3)", W / 2, 600, 110, 1300, 820, align="center", n=1)
        form(c, t, c7 + 0.4, "x = 3", 620, 820, 96, CERTO, align="center")
        form(c, t, c7 + 0.6, "x = 3", 1300, 820, 96, CERTO, align="center")
        E.foco(c, t, c7 + 1.2, 0.45, lambda p: E.pilula(c, "a mesma raiz, repetida", W / 2, 960, 56, estilo="g", fundo=CERTO, cor=BR, a=p))
    fase(c, t, C["s07"], 1e9, s07)


# ---------------- delta negativo ----------------
def b_negativo(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s08.{k}"] for k in "abcde")
    E.foco(c, t, a_, 0.45, lambda p: E.pilula(c, "Δ < 0", XE + 110, 190, 64, estilo="g", fundo=TINTA, cor=BR, a=p), sobe=8)
    E.frase(c, t, a_ + 0.6, ps("a raiz do delta não dá número da reta", "i", 60, TINTA2), XE + 300, 210, passo=0.08)
    E.foco(c, t, b_, 0.5, lambda p: E.pilula(c, "números da reta = números reais", XE + 420, 320, 50, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    delta_caso(c, t, c_ - 0.1, "<", XE, 450, 50, t1=c_)
    form(c, t, d_ - 0.5, Q0, XE, 620, 96)
    form(c, t, d_, "Δ = 4 − 20 = −16", XE, 760, 90, ERRADO)
    leque(c, t, d_ + 0.5, d_ + 1.2, -4, 2, -1, None, y=910)
    E.foco(c, t, e_, 0.5, lambda p: E.pilula(c, "nenhuma raiz real, sem a fórmula", 1420, 730, 46, estilo="g", fundo=TINTA2, cor=BR, a=p))


# ---------------- o quadro ----------------
def b_quadro(c, t, C, b):
    E.frase(c, t, C["s09"] + 0.2, ps("em resumo", "i", 90, COR), XE, 200)
    for k, (sinal, tk) in enumerate(((">", C["s09.a"]), ("=", C["s09.b"]), ("<", C["s09.c"]))):
        delta_caso(c, t, tk, sinal, XE + 100, 400 + k * 190, 66, t1=tk + 0.4)


# ---------------- o k ----------------
QK = "x^2 − 4x + k = 0"


def b_k(c, t, C, b):
    a0, b0 = C["s10.a"], C["s10.b"]

    def s10():
        E.frase(c, t, C["s10"] + 0.3, ps("a questão que", "i", 76) + ps("inverte o jogo", "g", 76, COR), XE, 190, passo=0.1)
        E.frase(c, t, a0, ps("para que valor de", "i", 76) + ps("k", "g", 80, CC), XE, 360, passo=0.1)
        monta(c, t, [pf("x^2 − 4x + ", a0 + 1.0), pf("k", a0 + 1.0, CC), pf(" = 0", a0 + 1.0)], XE + 60, 540, 130)
        E.foco(c, t, a0 + 2.5, 0.5, lambda p: E.pilula(c, "uma raiz só?", 1450, 500, 64, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
        realce(c, t, b0, QK, "k", XE + 60, 540, 130, CC)
        E.frase(c, t, b0 + 0.3, ps("k:", "g", 64, CC) + ps("um número desconhecido, no lugar do", "i", 64) + ps("c", "g", 64, CC), XE, 760, passo=0.08)
    fase(c, t, C["s10"], C["s11"] - 0.1, s10)

    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")

    def s11():
        monta(c, t, [pf("x^2 − 4x + ", C["s11"] + 0.1), pf("k", C["s11"] + 0.1, CC), pf(" = 0", C["s11"] + 0.1)], XE, 200, 84)
        E.foco(c, t, a1, 0.45, lambda p: E.pilula(c, "uma raiz só  →  Δ = 0", 1350, 170, 54, estilo="g", fundo=TINTA, cor=BR, a=p), sobe=8)
        monta(c, t, [pf("Δ = ", b1), pf("(", b1), pf("−4", b1, CB), pf(")^2", b1), pf(" − 4 · ", c1), pf("1", c1, CA), pf(" · ", c1),
                     pf("k", c1, CC)], XE, 380, 100)
        form(c, t, b1 + 0.6, "(−4)^2 = 16", 1250, 360, 66, TINTA2)
        form(c, t, c1 + 0.6, "4 · 1 · k = 4k", 1250, 450, 66, TINTA2)
        form(c, t, d1, "16 − 4k = 0", XE, 560, 110)
        nos_dois(c, t, entre(d1, e1, 0.6), "16 − 4k = 0", "+ 4k", XE, 560, 110)
        form(c, t, e1, "4k = 16", XE, 780, 110)
        form(c, t, e1 + 1.5, "k = 4", XE + 600, 780, 130, CERTO)
        nota(c, t, e1 + 1.2, "÷ 4", XE + 470, 760, 54, COR)
    fase(c, t, C["s11"], C["s12"] - 0.1, s11)

    a2, b2 = C["s12.a"], C["s12.b"]

    def s12():
        nota(c, t, C["s12"] + 0.2, "conferindo com k = 4", XE, 200, 60)
        form(c, t, a2, "x^2 − 4x + 4 = (x − 2)^2", W / 2, 470, 120, align="center")
        raizes(c, t, b2, ("2",), W / 2 - 200, 760, 140, align="center")
        E.foco(c, t, b2 + 0.4, 0.45, lambda p: E.pilula(c, "uma raiz só", W / 2 + 330, 715, 64, estilo="g", fundo=CERTO, cor=BR, a=p))
    fase(c, t, C["s12"], 1e9, s12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s13.{k}"] for k in "abcd")
    E.frase(c, t, C["s13"] + 0.3, ps("o erro mais comum", "g", 80, ERRADO), XE, 170, passo=0.1)
    E.foco(c, t, a_, 0.45, lambda p: E.pilula(c, "Δ = 0", XE + 100, 320, 60, estilo="g", fundo=TINTA, cor=BR, a=p), sobe=8)
    form(c, t, a_ + 0.4, "→", XE + 250, 345, 80, ERRADO)
    E.foco(c, t, a_ + 0.6, 0.45, lambda p: E.pilula(c, "nenhuma raiz", XE + 560, 320, 60, estilo="g", fundo=ERRADO, cor=BR, a=p), sobe=8)
    E.frase(c, t, entre(a_, b_, 0.55), ps("zero parece nada", "i", 60, TINTA2), 1150, 340, passo=0.08)
    if t >= b_:
        E.risco(c, XE + 380, 360, XE + 740, 280, t, b_, largura=10)
    form(c, t, b_, Q2, XE, 540, 100)
    monta(c, t, [pf("x = 3:  ", b_ + 0.6, CERTO), pf("9 − 18 + 9 = 0", b_ + 1.0)], XE, 690, 96)
    selo_em(c, t, b_ + 2.0, 1500, 660, 40)
    delta_caso(c, t, c_, "=", XE, 860, 54, t1=c_ + 0.3)
    E.foco(c, t, d_, 0.45, lambda p: E.pilula(c, "nenhuma raiz: Δ < 0", 1500, 960, 52, estilo="g", fundo=TINTA2, cor=BR, a=p), sobe=8)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    QA = "2x^2 + 7x − 3 = 0"

    def s14():
        E.frase(c, t, C["s14"] + 0.2, ps("o atalho", "i", 72, CLARO), XE, 170, passo=0.1)
        E.frase(c, t, a4, [("a", "g", 70, CA_L)] + ps("e", "i", 70, CLARO) + [("c", "g", 70, CC_L)] + ps("com sinais contrários:", "i", 70, CLARO), XE, 320, passo=0.1)
        E.frase(c, t, a4 + 1.5, ps("delta positivo,", "g", 70, AM) + ps("sem conta", "i", 70, CLARO), XE, 430, passo=0.1)
        monta(c, t, [pf("2", b4, CA_L), pf("x^2 + 7x ", b4, BR), pf("− 3", b4, CC_L), pf(" = 0", b4, BR)], XE, 640, 120)
        coef(c, t, entre(b4, c4, 0.45), "a", "2 (positivo)", 1350, 560, 44, CA)
        coef(c, t, entre(b4, c4, 0.7), "c", "−3 (negativo)", 1350, 680, 44, CC)
        delta_caso(c, t, c4 - 0.3, ">", XE, 880, 60, t1=c4, escuro=True)
    fase(c, t, C["s14"], C["s15"] - 0.1, s14)

    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")

    def s15():
        E.frase(c, t, C["s15"] + 0.2, ps("funciona porque", "i", 76, CLARO), XE, 180, passo=0.1)
        monta(c, t, [pf("a", a5, CA_L), pf(" · ", a5, BR), pf("c", a5, CC_L), pf(" < 0", a5, AM)], XE, 360, 100)
        delta_f(c, t, b5, XE, 530, 100, tinta=BR, cores=(CA_L, CB_L, CC_L))
        form(c, t, b5 + 0.8, "→  b^2 + um positivo", XE + fw("Δ = b^2 − 4ac ", 100), 530, 90, AM)
        monta(c, t, [pf("b", c5, CB_L), pf("^2", c5, BR), pf(" nunca é negativo  →  Δ > 0", c5, BR)], XE, 690, 80)
        selo_em(c, t, d5, XE + 40, 870, 38, False)
        E.frase(c, t, d5, ps("sinais iguais?", "g", 62, BR) + ps("o atalho não decide: calcule o delta", "i", 62, CLARO), XE + 110, 892, passo=0.08)
    fase(c, t, C["s15"], 1e9, s15)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_, c_ = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, C["s16"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s16"] + 1.5, ps("sem resolver:", "g", 66) + ps("quantas raízes reais?", "i", 66), XE, 300, passo=0.1)
    for k, (tk, s_) in enumerate(((a_, "x^2 − 4x + 5 = 0"), (b_, "x^2 + 10x + 25 = 0"))):
        E.foco(c, t, tk, 0.45, lambda p, k=k: num_bola(c, str(k + 1), XE + 40, 440 + k * 170, 40, 50, p))
        form(c, t, tk + 0.1, s_, XE + 120, 475 + k * 170, 96, COR)
    E.foco(c, t, c_, 0.45, lambda p: num_bola(c, "3", XE + 40, 800, 40, 50, p))
    E.frase(c, t, c_, ps("k para uma raiz só:", "i", 60), XE + 120, 760, passo=0.08)
    monta(c, t, [pf("x^2 + 6x + ", c_ + 1.0, COR), pf("k", c_ + 1.0, CC), pf(" = 0", c_ + 1.0, COR)], XE + 120, 880, 96)
    E.relogio(c, t, C["s17.a"], 1560, 520, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")

    def s18():
        E.foco(c, t, C["s18"] + 0.2, 0.45, lambda p: num_bola(c, "1", XE + 40, 200, 40, 50, p))
        form(c, t, C["s18"] + 0.3, "x^2 − 4x + 5 = 0", XE + 120, 235, 84, TINTA2)
        form(c, t, a8, "Δ = 16 − 20 = −4", XE + 120, 350, 90)
        delta_caso(c, t, b8 - 0.3, "<", XE + 120, 450, 44, t1=b8)
        E.foco(c, t, c8 - 0.5, 0.45, lambda p: num_bola(c, "2", XE + 40, 560, 40, 50, p))
        form(c, t, c8 - 0.4, "x^2 + 10x + 25 = 0", XE + 120, 595, 84, TINTA2)
        form(c, t, c8, "Δ = 100 − 100 = 0", XE + 120, 710, 90)
        delta_caso(c, t, d8 - 0.3, "=", XE + 120, 810, 44, t1=d8)
        monta(c, t, [pf("x = f{−10}{2}", d8 + 1.5), pf(" = −5", d8 + 2.5, CERTO)], 1150, 960, 90)
    fase(c, t, C["s18"], C["s19"] - 0.1, s18)

    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")

    def s19():
        E.foco(c, t, C["s19"] + 0.1, 0.45, lambda p: num_bola(c, "3", XE + 40, 200, 40, 50, p))
        monta(c, t, [pf("x^2 + 6x + ", C["s19"] + 0.2, TINTA2), pf("k", C["s19"] + 0.2, CC), pf(" = 0", C["s19"] + 0.2, TINTA2)], XE + 120, 235, 84)
        E.foco(c, t, C["s19"] + 0.4, 0.45, lambda p: E.pilula(c, "uma raiz só  →  Δ = 0", 1350, 205, 50, estilo="g", fundo=TINTA, cor=BR, a=p), sobe=8)
        form(c, t, a9, "36 − 4k = 0", XE + 120, 400, 110)
        form(c, t, b9, "4k = 36", XE + 120, 570, 110)
        form(c, t, c9, "k = 9", XE + 700, 570, 130, CERTO)
        form(c, t, d9, "x^2 + 6x + 9 = (x + 3)^2", XE + 120, 800, 100)
        E.foco(c, t, d9 + 0.8, 0.45, lambda p: E.pilula(c, "raiz dupla: −3", 1500, 900, 52, estilo="g", fundo=CERTO, cor=BR, a=p))
    fase(c, t, C["s19"], 1e9, s19)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s20.a"], ps("calcule só o", "i", 76) + [("Δ", "g", 76, COR)]),
             (C["s20.b"], ps("olhe o", "i", 76) + ps("sinal", "g", 76, COR) + ps("dele", "i", 76)))
    fim_padrao(c, t, C, "s20", "s21", itens, "próxima aula: delta positivo, mas", "sem raiz exata",
               extra=lambda: (form(c, t, C["s21.b"], "x(x − 2) = 1", XE, 590, 100),
                              E.frase(c, t, C["s21.c"], ps("a resposta fica", "i", 70) + ps("com raiz:", "g", 70, COR), XE, 750, passo=0.1),
                              form(c, t, C["s21.c"] + 0.8, "x = 1 ± r{2}", XE + 70, 880, 100, COR)))


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, positivo=b_positivo, zero=b_zero, negativo=b_negativo,
              quadro=b_quadro, k=b_k, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
