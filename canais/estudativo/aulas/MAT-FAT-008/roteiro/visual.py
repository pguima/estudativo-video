"""Visual — Estudativo · MAT-FAT-008: fórmula de Bhaskara.
x² − 5x + 6 = 0 sem isolar e sem fator comum; as duas etapas: Δ = b² − 4ac e x = (−b ± √Δ)/2a, com as letras nas cores
dos coeficientes; o exemplo com Δ = 1 e raízes 3 e 2, conferidas; −x² + 2x + 3 = 0 com a = −1 e Δ = 16; o erro de usar o a
sem o sinal (Δ = −8); no palco, o atalho de multiplicar por −1 para deixar o a positivo.

Convenções da trilha (as de MAT-FAT-004 a 007: fra, corta_f, evid, coeficientes coloridos, nos_dois, regra_zero, raizes).
Novas, para as próximas aulas da trilha:
- FÓRMULAS: Δ = b² − 4ac e x = (−b ± √Δ)/2a com cada letra na cor do seu coeficiente (delta_f, bhaskara_f);
- SUBSTITUIR: cada número entra na cor da letra que ele substitui, entre parênteses quando é negativo (subst);
- DELTA: o valor numa pílula escura "Δ = 1" (delta_pilula);
- MAIS OU MENOS: a conta se divide em duas linhas, com as pílulas "com +" e "com −" (pm).
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math
from fractions import Fraction as Fr

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-008_formula_de_bhaskara.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("formula", "exemplo1", "exemplo2", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"


def _bhaskara(a, b, c):
    d = b * b - 4 * a * c
    r = math.isqrt(d)
    assert r * r == d
    return d, Fr(-b + r, 2 * a), Fr(-b - r, 2 * a)


# as contas da aula
assert _bhaskara(1, -5, 6) == (1, 3, 2) and (-5) ** 2 == 25 and 4 * 1 * 6 == 24
assert 9 - 15 + 6 == 0 and 4 - 10 + 6 == 0
assert _bhaskara(-1, 2, 3) == (16, -1, 3) and 4 * (-1) * 3 == -12 and 4 - (-12) == 16 and Fr(2, -2) == -1 and Fr(-6, -2) == 3
assert 2 ** 2 - 4 * 1 * 3 == -8
assert _bhaskara(1, -2, -3) == (16, 3, -1) and (2 + 4) / 2 == 3 and (2 - 4) / 2 == -1
assert _bhaskara(2, -3, -2) == (25, 2, Fr(-1, 2)) and 4 * 2 * (-2) == -16 and 9 - (-16) == 25 and Fr(-2, 4) == Fr(-1, 2)


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


T_ = TINTA


def resolve(c, t, t0, cima, baixo, notas, simp, mais, menos, y=430, size=110):
    """a fórmula com os números (subst), as notas à direita, a fração simplificada e as duas contas do ±.
    notas = [(t, fórmula)], simp = (t, fórmula), mais/menos = (t, conta, t_final, final)"""
    subst(c, t, t0, cima, baixo, XE, y, size)
    for k, (tk, s) in enumerate(notas):
        form(c, t, tk, s, 1080, y - 90 + k * 120, 70, TINTA2)
    if simp:
        form(c, t, simp[0], simp[1], 1080, y + 230, 90)
    for (tk, conta, tf, final), sinal, yy in ((mais, "+", 790), (menos, "−", 960)):
        pm(c, t, tk, sinal, conta, XE, yy, 92, t1=tf, final=final)


def coefs(c, t, t0, vals, cx, cy, size=46, gap=260, dt=0.0):
    """as três pílulas a, b, c em fila, centradas em cx"""
    for k, (letra, v) in enumerate(zip("abc", vals)):
        coef(c, t, t0 + k * dt, letra, v, cx + (k - 1) * gap, cy, size)


# ---------------- gancho ----------------
Q1 = "x^2 − 5x + 6 = 0"


def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def conta():
        form(c, t, a_, Q1, W / 2, 380, 150, align="center")
        tz = entre(a_, b_, 0.55)
        selo_em(c, t, tz, XE + 40, 560, 36, False)
        E.frase(c, t, tz, ps("isolar o x ao quadrado?", "i", 64) + ps("não dá", "g", 64, ERRADO), XE + 110, 582, passo=0.08)
        selo_em(c, t, b_, XE + 40, 690, 36, False)
        E.frase(c, t, b_, ps("fator comum?", "i", 64) + ps("não tem", "g", 64, ERRADO), XE + 110, 712, passo=0.08)
        E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "uma fórmula para qualquer equação do 2º grau", W / 2, 890, 58, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2 = C["s02.a"], C["s02.b"]
    E.frase(c, t, a2, ps("até o fim desta aula, você usa", "i", 84), XE, 300, passo=0.12)
    E.frase(c, t, a2 + 1.2, ps("a fórmula de", "i", 110) + ps("Bhaskara", "g", 120, COR), XE, 470, passo=0.13)
    E.frase(c, t, b2, ps("sem tropeçar no", "i", 84) + ps("sinal de menos", "g", 84, ERRADO), XE, 660, passo=0.12)
    form(c, t, b2 + 0.8, "(−5)^2 = 25", XE + 60, 850, 110, TINTA2)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_ = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, a_, ps("duas", "g", 84, COR) + ps("ferramentas", "i", 90), XE, 180)
    xr = XE + 110
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "1", XE + 40, 330, 40, 50, p))
    E.frase(c, t, b_, ps("aponte", "i", 64) + [("a,", "g", 64, CA), ("b", "g", 64, CB)] + ps("e", "i", 64) + [("c,", "g", 64, CC)]
            + ps("com o sinal junto", "i", 64), xr, 352, passo=0.08)
    form(c, t, b_ + 1.0, "2x^2 − 3x + 1 = 0", xr + 20, 480, 84)
    coefs(c, t, b_ + 1.5, ("2", "−3", "1"), 1400, 455, 40, 190)
    E.foco(c, t, c_, 0.45, lambda p: num_bola(c, "2", XE + 40, 630, 40, 50, p))
    E.frase(c, t, c_, ps("troque a letra por um", "i", 64) + ps("número entre parênteses", "g", 64, COR), xr, 652, passo=0.08)
    E.frase(c, t, c_ + 1.4, ps("com b = −5:", "i", 58, TINTA2), xr + 20, 790, passo=0.08)
    monta(c, t, [pf("b", c_ + 1.6, CB), pf("^2", c_ + 1.6), pf("  →  (", c_ + 2.0), pf("−5", c_ + 2.0, CB), pf(")^2 = 25", c_ + 2.0)], xr + 350, 795, 84)
    E.frase(c, t, C["s04"] - 2.2, ps("faltou alguma? procure no canal", "i", 52, TINTA2), 1150, 1010, passo=0.08)


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")

    def s0405():
        E.frase(c, t, a4, ps("a fórmula tem", "i", 76) + ps("duas etapas", "g", 76, COR), XE, 170, passo=0.1)
        E.foco(c, t, b4, 0.5, lambda p: (E.bola(c, 1560, 300, 120, a=p), centro(c, "Δ", 1560, 345, 130, "g", BR, p)))
        E.foco(c, t, b4 + 0.4, 0.45, lambda p: centro(c, "delta", 1560, 490, 60, "i", COR, p))
        E.foco(c, t, c4, 0.45, lambda p: num_bola(c, "1", XE + 40, 355, 42, 52, p))
        delta_f(c, t, c4, XE + 130, 390, 120)
        E.foco(c, t, a5, 0.45, lambda p: num_bola(c, "2", XE + 40, 655, 42, 52, p))
        bhaskara_f(c, t, a5, XE + 130, 690, 120, t1=b5)
        cima, baixo = [("−", T_), ("b", CB), (" ± r{Δ}", T_)], [("2", T_), ("a", CA)]
        xf = XE + 130 + fw("x = ", 120) + fra_p_w(cima, baixo, 102) / 2
        xc = xf - sum(fw(q, 102) for q, _ in cima) / 2 + fw("−", 102) + fw("b", 102)
        realce(c, t, c5, " ± ", "±", xc, 690 - 120 * 0.32 - 102 * 0.32, 102)
        E.frase(c, t, c5 + 0.3, ps("faça a conta duas vezes:", "i", 58), 1000, 640, passo=0.08)
        E.frase(c, t, c5 + 1.5, ps("com", "i", 58) + [("+", "g", 58, COR)] + ps("e com", "i", 58) + [("−", "g", 58, COR)], 1000, 720, passo=0.1)
        E.foco(c, t, d5, 0.5, lambda p: E.pilula(c, "as duas raízes", W / 2, 940, 60, estilo="g", fundo=CERTO, cor=BR, a=p))
    fase(c, t, C["s04"], C["s06"] - 0.1, s0405)

    a6, b6 = C["s06.a"], C["s06.b"]

    def s06():
        E.frase(c, t, C["s06"] + 0.2, ps("de onde ela vem?", "i", 84), XE, 200, passo=0.1)
        E.frase(c, t, a6, ps("da equação transformada num", "i", 66) + ps("trinômio quadrado perfeito", "g", 66, COR), XE, 380, passo=0.08)
        form(c, t, a6 + 1.6, "x^2 + 6x + 9 = (x + 3)^2", XE + 60, 560, 100, TINTA2)
        E.foco(c, t, a6 + 2.2, 0.45, lambda p: E.escreve(c, "como os que você fatorou", XE + 60, 660, 54, "i", TINTA2, p))
        E.foco(c, t, b6, 0.5, lambda p: E.pilula(c, "na prova: saber usar a fórmula", W / 2, 880, 64, estilo="g", fundo=CERTO, cor=BR, a=p))
    fase(c, t, C["s06"], 1e9, s06)


# ---------------- exemplo 1 ----------------
def b_exemplo1(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")

    def s07():
        form(c, t, C["s07"] + 0.1, Q1, W / 2, 200, 110, align="center")
        coefs(c, t, a7, ("1", "−5", "6"), W / 2, 320, 48, 280, dt=0.6)
        monta(c, t, [pf("Δ = ", b7), pf("(", b7), pf("−5", b7, CB), pf(")^2", b7), pf(" − 4 · ", c7), pf("1", c7, CA), pf(" · ", c7),
                     pf("6", c7, CC)], XE, 540, 100)
        monta(c, t, [pf("Δ = 25", b7 + 1.4), pf(" − 24", c7 + 1.4)], XE, 700, 100)
        form(c, t, d7, "= 1", XE + fw("Δ = 25 − 24 ", 100), 700, 100)
        delta_pilula(c, t, d7 + 0.8, "1", 1400, 640, 70)
    fase(c, t, C["s07"], C["s08"] - 0.1, s07)

    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")

    def s08():
        delta_pilula(c, t, C["s08"] + 0.05, "1", 1620, 150, 50)
        form(c, t, C["s08"] + 0.3, "r{1} = 1", 1160, 165, 70, TINTA2)
        resolve(c, t, C["s08"] + 0.1, [("−(", T_), ("−5", CB), (") ± r{1}", T_)], [("2 · ", T_), ("1", CA)],
                [(a8, "−b = 5"), (b8, "2 · 1 = 2")], (b8 + 1.0, "x = f{5 ± 1}{2}"),
                (c8, "f{5 + 1}{2} = f{6}{2}", entre(c8, d8, 0.75), "= 3"), (d8, "f{5 − 1}{2} = f{4}{2}", d8 + 3.4, "= 2"))
    fase(c, t, C["s08"], C["s09"] - 0.1, s08)

    a9, b9 = C["s09.a"], C["s09.b"]

    def s09():
        nota(c, t, C["s09"] + 0.2, "conferindo na equação", XE, 200, 60)
        monta(c, t, [pf("3^2 − 5 · 3 + 6", a9), pf(" = 9 − 15 + 6 = 0", a9 + 1.0)], XE, 400, 96)
        selo_em(c, t, a9 + 2.0, 1650, 370, 42)
        monta(c, t, [pf("2^2 − 5 · 2 + 6", b9), pf(" = 4 − 10 + 6 = 0", b9 + 1.0)], XE, 580, 96)
        selo_em(c, t, b9 + 2.0, 1650, 550, 42)
        raizes(c, t, b9 + 1.5, ("3", "2"), W / 2, 830, 130, align="center", t1=b9 + 2.0)
    fase(c, t, C["s09"], 1e9, s09)


# ---------------- exemplo 2 ----------------
Q2 = "−x^2 + 2x + 3 = 0"


def b_exemplo2(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]

    def s10():
        E.frase(c, t, a0, ps("agora com", "i", 76) + ps("a negativo", "g", 76, CA), XE, 190, passo=0.1)
        form(c, t, a0 + 0.8, Q2, W / 2, 440, 140, align="center")
        tz = entre(a0, b0, 0.55)
        realce(c, t, tz, Q2, "−x^2", W / 2, 440, 140, CA, "center")
        E.foco(c, t, tz + 0.3, 0.45, lambda p: E.formula(c, "nenhum número escrito na frente do x^2", W / 2, 580, 56, "i", TINTA2, p, "center"))
        form(c, t, b0 - 0.6, "−x^2 = −1 · x^2", W / 2, 720, 100, TINTA2, align="center")
        coefs(c, t, b0, ("−1", "2", "3"), W / 2, 880, 54, 300, dt=0.0)
    fase(c, t, C["s10"], C["s11"] - 0.1, s10)

    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")

    def s11():
        coefs(c, t, C["s11"] + 0.05, ("−1", "2", "3"), W / 2, 170, 40, 220)
        monta(c, t, [pf("Δ = ", a1), pf("2", a1, CB), pf("^2", a1), pf(" − 4 · (", b1), pf("−1", b1, CA), pf(") · ", b1), pf("3", b1, CC)],
              XE, 380, 100)
        monta(c, t, [pf("= 4", a1 + 0.8), pf(" − (−12)", c1)], XE, 560, 100)
        form(c, t, b1 + 1.4, "4 · (−1) · 3 = −12", 1080, 555, 70, TINTA2)
        form(c, t, d1, "= 4 + 12", XE, 740, 100)
        E.frase(c, t, entre(c1, d1, 0.4), ps("tirar uma dívida é", "i", 58) + ps("ganhar", "g", 58, CERTO), 1080, 735, passo=0.08)
        delta_pilula(c, t, d1 + 0.9, "16", XE + 250, 900, 66)
    fase(c, t, C["s11"], C["s12"] - 0.1, s11)

    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")

    def s12():
        delta_pilula(c, t, C["s12"] + 0.05, "16", 1620, 150, 50)
        form(c, t, C["s12"] + 0.3, "r{16} = 4", 1160, 165, 70, TINTA2)
        resolve(c, t, C["s12"] + 0.1, [("−", T_), ("2", CB), (" ± r{16}", T_)], [("2 · (", T_), ("−1", CA), (")", T_)],
                [(a2, "−b = −2"), (b2, "2 · (−1) = −2")], (b2 + 1.2, "x = f{−2 ± 4}{−2}"),
                (c2, "f{−2 + 4}{−2} = f{2}{−2}", entre(c2, d2, 0.8), "= −1"), (d2, "f{−2 − 4}{−2} = f{−6}{−2}", d2 + 4.6, "= 3"))
    fase(c, t, C["s12"], 1e9, s12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s13.{k}"] for k in "abcde")
    E.frase(c, t, C["s13"] + 0.3, ps("o erro mais comum:", "g", 80, ERRADO) + ps("o a sem o sinal", "i", 80), XE, 170, passo=0.1)
    form(c, t, C["s13"] + 1.4, Q2, 1150, 290, 80, TINTA2)
    monta(c, t, [pf("Δ = 2^2 − 4 · ", a_), pf("1", a_, ERRADO), pf(" · 3", a_)], XE, 430, 100)
    realce(c, t, a_ + 0.4, "Δ = 2^2 − 4 · 1 · 3", "1", XE, 430, 100, ERRADO)
    nota(c, t, a_ + 0.8, "cadê o menos do −1?", 1150, 425, 56, ERRADO)
    form(c, t, b_, "4 · 1 · 3 = 12", XE, 590, 90, TINTA2)
    form(c, t, c_, "Δ = 4 − 12 = −8", XE, 750, 100, ERRADO)
    form(c, t, d_, "r{−8} = ?", 1150, 750, 100, ERRADO)
    nota(c, t, d_ + 0.6, "nenhum número vezes ele mesmo dá −8", 1150, 840, 46, ERRADO)
    E.foco(c, t, e_, 0.5, lambda p: E.pilula(c, "cada coeficiente entre parênteses: 4 · (−1) · 3", W / 2, 970, 56, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")

    def s14():
        E.frase(c, t, C["s14"] + 0.2, ps("o atalho:", "i", 72, CLARO) + ps("deixe o a positivo", "g", 70, BR), XE, 170, passo=0.1)
        form(c, t, a4, Q2, XE, 340, 100, BR)
        tz = entre(a4, b4, 0.45)
        E.foco(c, t, tz, 0.45, lambda p: E.pilula(c, "× (−1) dos dois lados", 1350, 310, 52, estilo="g", fundo=AM, cor="#07070F", a=p), sobe=8)
        form(c, t, b4, "x^2 − 2x − 3 = 0", XE, 500, 100, AM)
        form(c, t, c4, "Δ = 4 + 12 = 16", XE, 660, 90, BR)
        form(c, t, d4, "f{2 + 4}{2} = 3", XE, 840, 100, AM)
        form(c, t, e4, "f{2 − 4}{2} = −1", 900, 840, 100, AM)
        E.foco(c, t, e4 + 2.6, 0.45, lambda p: E.pilula(c, "as mesmas raízes", W / 2, 980, 56, estilo="g", fundo=CERTO, cor=BR, a=p))
    fase(c, t, C["s14"], C["s15"] - 0.1, s14)

    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]

    def s15():
        E.frase(c, t, C["s15"] + 0.2, ps("funciona porque é a", "i", 76, CLARO) + ps("balança", "g", 76, BR), XE, 180, passo=0.1)
        form(c, t, a5, "0 · (−1) = 0", XE, 370, 110, AM)
        E.frase(c, t, a5 + 1.2, ps("a equação muda de cara,", "i", 60, CLARO) + ps("não de raízes", "g", 60, BR), XE, 490, passo=0.08)
        selo_em(c, t, b5, XE + 40, 650, 38, True)
        E.frase(c, t, b5, ps("embaixo, um número positivo:", "i", 60, CLARO) + ps("sem divisão por negativo", "g", 60, BR), XE + 110, 672, passo=0.08)
        selo_em(c, t, c5, XE + 40, 820, 38, False)
        E.frase(c, t, c5, ps("a já positivo?", "g", 60, BR) + ps("vá direto para o delta", "i", 60, CLARO), XE + 110, 842, passo=0.08)
    fase(c, t, C["s15"], 1e9, s15)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_ = C["s16.a"], C["s16.b"]
    E.frase(c, t, C["s16"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, a_ - 0.4, ps("resolva", "i", 90), XE, 380, passo=0.1)
    form(c, t, a_, "2x^2 − 3x − 2 = 0", XE + 40, 590, 120, COR)
    E.foco(c, t, b_, 0.45, lambda p: E.pilula(c, "calcule o Δ primeiro", XE + 340, 780, 60, estilo="g", fundo=TINTA, cor=BR, a=p))
    E.relogio(c, t, C["s17.a"], 1560, 480, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")

    def s18():
        form(c, t, C["s18"] + 0.1, "2x^2 − 3x − 2 = 0", W / 2, 190, 100, align="center")
        coefs(c, t, a8, ("2", "−3", "−2"), W / 2, 300, 46, 280, dt=0.6)
        monta(c, t, [pf("Δ = ", b8), pf("(", b8), pf("−3", b8, CB), pf(")^2", b8), pf(" − 4 · ", c8), pf("2", c8, CA), pf(" · (", c8),
                     pf("−2", c8, CC), pf(")", c8)], XE, 500, 100)
        monta(c, t, [pf("= 9", b8 + 1.4), pf(" − (−16)", d8)], XE, 670, 100)
        form(c, t, c8 + 1.4, "4 · 2 · (−2) = −16", 1100, 665, 70, TINTA2)
        form(c, t, d8 + 1.4, "= 9 + 16", XE, 840, 100)
        delta_pilula(c, t, d8 + 3.0, "25", 1100, 810, 66)
    fase(c, t, C["s18"], C["s19"] - 0.1, s18)

    a9, b9, c9, d9, e9 = (C[f"s19.{k}"] for k in "abcde")

    def s19():
        delta_pilula(c, t, C["s19"] + 0.05, "25", 1620, 150, 50)
        form(c, t, C["s19"] + 0.3, "r{25} = 5", 1160, 165, 70, TINTA2)
        resolve(c, t, C["s19"] + 0.1, [("−(", T_), ("−3", CB), (") ± r{25}", T_)], [("2 · ", T_), ("2", CA)],
                [(a9, "−b = 3"), (b9, "2 · 2 = 4")], (b9 + 1.0, "x = f{3 ± 5}{4}"),
                (c9, "f{3 + 5}{4} = f{8}{4}", c9 + 1.6, "= 2"), (d9, "f{3 − 5}{4} = f{−2}{4}", e9, "= −f{1}{2}"))
    fase(c, t, C["s19"], 1e9, s19)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s20.a"], ps("aponte", "i", 72) + [("a,", "g", 72, CA), ("b", "g", 72, CB)] + ps("e", "i", 72) + [("c", "g", 72, CC)]
              + ps("com o sinal", "i", 72)),
             (C["s20.b"], ps("calcule o", "i", 72) + [("Δ", "g", 72, COR)] + ps("primeiro, com parênteses", "i", 72)),
             (C["s20.c"], ps("faça a conta com", "i", 72) + [("+", "g", 72, COR)] + ps("e com", "i", 72) + [("−", "g", 72, COR)]))

    def extra():
        E.frase(c, t, C["s21.b"], ps("só olhando o sinal do", "i", 70) + [("Δ", "g", 74, COR)], XE, 580, passo=0.1)
        for k, s in enumerate(("Δ > 0", "Δ = 0", "Δ < 0")):
            E.foco(c, t, C["s21.b"] + 0.8 + k * 0.25, 0.45, lambda p, s=s, k=k: E.pilula(c, s, XE + 150 + k * 300, 740, 54, estilo="g", fundo=TINTA, cor=BR, a=p), sobe=8)
    fim_padrao(c, t, C, "s20", "s21", itens, "próxima aula: sem resolver", "quantas raízes?", extra=extra, k_ins="c", k_bons="d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, formula=b_formula, exemplo1=b_exemplo1, exemplo2=b_exemplo2, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
