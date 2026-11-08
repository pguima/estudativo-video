"""Visual — Estudativo · MAT-FAT-007: equação do 2º grau incompleta.
x² = 49 com o 7 e o −7; a forma ax² + bx + c = 0 com os coeficientes coloridos; 2x² − 3x + 1 = 0 com a, b e c apontados;
sem b: x² − 49 = 0 pela balança e pela fatoração, com o produto zero abrindo dois ramos; sem c: x² − 5x = 0 com o x em
evidência; o erro de dividir por x; no palco, o atalho "uma raiz é 0, a outra é −b/a".

Convenções da trilha (continuam as de MAT-FAT-004 a 006: fra, andar, corta_f, proibido, evid, vezes_um). Novas:
- COEFICIENTES: á na cor da matéria, bê em magenta, cê em âmbar (CA, CB, CC; no palco, CA_L, CB_L, CC_L), na equação e
  nas pílulas "a = 2" (coef);
- O MESMO NOS DOIS LADOS: pílula com a operação embaixo de cada lado (nos_dois);
- PRODUTO ZERO: pílula escura "produto = 0 → algum fator = 0" (regra_zero) e uma seta de cada fator até o seu ramo (ramo);
- RAÍZES: "x = 7  ou  x = −7" em verde, com o "ou" em itálico (raizes).
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-007_equacao_2grau_incompleta.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("forma", "semb", "semc", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"

# as contas da aula
for x in (7, -7):
    assert x * x == 49 and x * x - 49 == 0 and (x + 7) * (x - 7) == 0
for x in (0, 5):
    assert x * x - 5 * x == 0 == x * (x - 5)
assert 5 ** 2 - 5 * 5 == 0 and 25 - 25 == 0
for x in (0, -4):
    assert 3 * x * x + 12 * x == 0
assert -12 / 3 == -4
for x in (6, -6):
    assert 2 * x * x - 72 == 0 and x * x == 36 and 72 / 2 == 36
for x in (0, 6):
    assert x * x == 6 * x and x * (x - 6) == 0


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


def geral(c, t, t0, x, y, size, align="left", d=0.3, cores=(CA, CB, CC)):
    """ax² + bx + c = 0 com as letras coloridas; d = intervalo entre as letras"""
    ca, cb, cc = cores
    return monta(c, t, [pf("a", t0, ca), pf("x^2 + ", t0), pf("b", t0 + d, cb), pf("x + ", t0 + d), pf("c", t0 + 2 * d, cc),
                        pf(" = 0", t0 + 2 * d)], x, y, size, align)


def centro_de(s, trecho, x, size, align="left", n=0):
    x0, w = trecho_x(s, trecho, x, size, align, n)
    return x0 + w / 2


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s01.{k}"] for k in "abcd")

    def conta():
        form(c, t, a_, "x^2 = 49", XE, 420, 170)
        form(c, t, b_, "x = 7", 1150, 420, 150, CERTO)
        selo_em(c, t, b_ + 0.4, 1650, 370, 50)
        E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "falta metade da resposta", 1400, 560, 54, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
        form(c, t, d_, "(−7)^2 = 49", XE, 800, 140, COR)
        E.foco(c, t, d_ + 0.8, 0.45, lambda p: E.escreve(c, "também", XE + fw("(−7)^2 = 49", 140) + 50, 790, 80, "i", TINTA2, p))
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]
    E.frase(c, t, a2, ps("até o fim desta aula, você resolve", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a2 + 1.2, ps("equações com", "g", 88, COR), XE, 390, passo=0.13)
    form(c, t, a2 + 1.6, "x^2", XE + E.larg("equações com ", "g", 88) + 10, 390, 96, COR)
    E.frase(c, t, a2 + 2.2, ps("sem fórmula nenhuma", "i", 80), XE, 510, passo=0.12)
    E.frase(c, t, b2, ps("sem perder a", "i", 76) + ps("raiz negativa", "g", 72, COR), XE, 690, passo=0.12)
    E.frase(c, t, c2, ps("nem o", "i", 76), XE, 830, passo=0.12)
    form(c, t, c2 + 0.3, "x = 0", XE + E.larg("nem o ", "i", 76) + 10, 830, 84, COR)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s03.{k}"] for k in "abcd")
    E.frase(c, t, a_, ps("três", "g", 84, COR) + ps("ferramentas", "i", 90), XE, 180)
    xr = XE + 110
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "1", XE + 40, 330, 40, 50, p))
    E.frase(c, t, b_, ps("balança:", "g", 64, COR) + ps("o mesmo nos dois lados", "i", 64), xr, 352, passo=0.08)
    E.foco(c, t, c_, 0.45, lambda p: num_bola(c, "2", XE + 40, 530, 40, 50, p))
    E.frase(c, t, c_, ps("raiz quadrada:", "g", 64, COR), xr, 552, passo=0.08)
    form(c, t, c_ + 0.4, "r{49} = 7", xr + 520, 556, 80)
    E.foco(c, t, d_, 0.45, lambda p: num_bola(c, "3", XE + 40, 730, 40, 50, p))
    E.frase(c, t, d_, ps("fatorar:", "g", 64, COR) + ps("evidência e diferença de quadrados", "i", 58), xr, 752, passo=0.08)
    form(c, t, d_ + 1.2, "x^2 − 49 = (x + 7)(x − 7)", xr, 880, 80)
    E.frase(c, t, C["s04"] - 2.2, ps("faltou alguma? procure no canal", "i", 52, TINTA2), 1150, 1010, passo=0.08)


# ---------------- a forma ----------------
G = "ax^2 + bx + c = 0"
EX = "2x^2 − 3x + 1 = 0"


def b_forma(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]

    def s04():
        nota(c, t, C["s04"] + 0.3, "até aqui:", XE, 200, 58)
        form(c, t, C["s04"] + 0.6, "2x + 3 = 11", XE + 260, 205, 90, TINTA2)
        E.foco(c, t, C["s04"] + 1.6, 0.45, lambda p: E.escreve(c, "x sem expoente", XE + 900, 200, 56, "i", TINTA2, p))
        form(c, t, a4, "x^2", XE, 480, 170)
        E.foco(c, t, a4, 0.45, lambda p: c.drawCircle(XE + fw("x", 170) + 30, 480 - 125, 48, M.paint(COR, p, stroke=6)))
        E.frase(c, t, a4 + 0.5, ps("maior expoente do x:", "i", 70) + ps("2", "g", 70, COR), XE + 300, 440, passo=0.1)
        E.frase(c, t, b4, ps("equação do", "i", 84) + ps("2º grau", "g", 84, COR), XE + 300, 560, passo=0.12)
        nota(c, t, entre(b4, c4, 0.55), "toda equação do 2º grau pode ser arrumada assim:", XE, 760, 54)
        geral(c, t, c4, W / 2, 920, 150, "center")
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)

    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    s, y = 140, 330

    def s0506():
        geral(c, t, C["s05"] + 0.1, W / 2, y, s, "center", d=0)
        nota(c, t, a5, "coeficientes: os números que acompanham cada termo", W / 2, 180, 54, align="center")
        for k, (tk, letra, txt, cor) in enumerate(((b5, "a", "multiplica o x^2", CA), (c5, "b", "multiplica o x", CB), (d5, "c", "o número sozinho", CC))):
            cx = centro_de(G, letra, W / 2, s, "center")
            realce(c, t, tk, G, letra, W / 2, y, s, cor, "center")
            E.foco(c, t, tk + 0.2, 0.45, lambda q, txt=txt, cx=cx, cor=cor: E.formula(c, txt, cx, y + 110, 48, "i", cor, q, "center"))
        form(c, t, a6, EX, W / 2, 700, 140, align="center")
        for tk, letra, valor, trecho in ((b6, "a", "2", "2"), (c6, "b", "−3", "− 3"), (d6, "c", "1", "1")):
            cx = centro_de(EX, trecho, W / 2, 140, "center")
            realce(c, t, tk, EX, trecho, W / 2, 700, 140, {"a": CA, "b": CB, "c": CC}[letra], "center")
            coef(c, t, tk + 0.2, letra, valor, cx, 820, 46)
        E.foco(c, t, e6, 0.5, lambda p: E.pilula(c, "a nunca é 0: sem x², não é do 2º grau", W / 2, 975, 52, estilo="g", fundo=TINTA, cor=BR, a=p))
    fase(c, t, C["s05"], C["s07"] - 0.1, s0506)

    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]

    def s07():
        nota(c, t, C["s07"] + 0.2, "quando falta um termo", XE, 190, 60)
        form(c, t, a7, "x^2 − 49 = 0", XE, 380, 110)
        coef(c, t, a7 + 0.5, "b", "0", XE + fw("x^2 − 49 = 0", 110) / 2, 480, 44)
        form(c, t, a7 + 1.0, "x^2 − 5x = 0", 1050, 380, 110)
        coef(c, t, a7 + 1.5, "c", "0", 1050 + fw("x^2 − 5x = 0", 110) / 2, 480, 44)
        E.frase(c, t, b7, ps("equação", "i", 96) + ps("incompleta", "g", 96, COR), XE, 680, passo=0.12)
        E.frase(c, t, entre(b7, c7, 0.45), ps("sem fórmula", "i", 64, CERTO), 1250, 670, passo=0.1)
        E.foco(c, t, c7, 0.5, lambda p: E.pilula(c, "raízes = soluções", 560, 870, 64, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
        E.frase(c, t, entre(c7, C["s07.end"], 0.4), ps("não é raiz quadrada", "i", 60, TINTA2), 1000, 890, passo=0.1)
    fase(c, t, C["s07"], 1e9, s07)


# ---------------- sem b ----------------
def b_semb(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    Q = "x^2 − 49 = 0"

    def s08():
        E.frase(c, t, a8, ps("1º caso:", "g", 70, COR) + ps("sem o termo com x", "i", 70), XE, 180, passo=0.1)
        coef(c, t, a8 + 1.0, "b", "0", 1500, 160, 44)
        form(c, t, b8, Q, W / 2, 440, 140, align="center")
        nota(c, t, c8 - 0.3, "na balança:", XE, 630, 52)
        nos_dois(c, t, c8, Q, "+ 49", W / 2, 440, 140, align="center")
        form(c, t, d8, "x^2 = 49", W / 2, 860, 150, align="center")
    fase(c, t, C["s08"], C["s09"] - 0.1, s08)

    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")

    def s09():
        form(c, t, C["s09"] + 0.1, "x^2 = 49", XE, 200, 90, TINTA2)
        form(c, t, a9, "? · ? = 49", XE, 360, 110)
        form(c, t, b9, "7 · 7 = 49", XE, 520, 110, CERTO)
        form(c, t, c9, "(−7) · (−7) = 49", XE, 680, 110, CERTO)
        nota(c, t, c9 + 0.8, "sinais iguais dão mais", XE + fw("(−7) · (−7) = 49", 110) + 40, 670, 50)
        tr = entre(c9, d9, 0.45)
        form(c, t, tr, "r{49} = 7", 1150, 380, 100, TINTA2)
        nota(c, t, tr + 0.4, "a raiz quadrada dá só o positivo", 1150, 470, 48)
        E.frase(c, t, d9, ps("a equação pede", "i", 62) + ps("todos", "g", 62, COR), 1150, 560, passo=0.1)
        raizes(c, t, e9, ("7", "−7"), W / 2, 900, 130, align="center", t1=e9 + 1.0)
    fase(c, t, C["s09"], C["s10"] - 0.1, s09)

    a0, b0 = C["s10.a"], C["s10.b"]
    P = "(x + 7)(x − 7) = 0"

    def s10():
        nota(c, t, C["s10"] + 0.2, "fatorando: diferença de dois quadrados", XE, 190, 58)
        form(c, t, a0, P, W / 2, 400, 130, align="center")
        E.frase(c, t, b0, ps("se uma multiplicação dá", "i", 70) + ps("zero,", "g", 70, COR), W / 2, 620, "center", passo=0.1)
        E.frase(c, t, b0 + 1.2, ps("algum fator vale", "i", 70) + ps("zero", "g", 70, COR), W / 2, 720, "center", passo=0.1)
        regra_zero(c, t, b0 + 2.0, W / 2, 860, 54)
        E.frase(c, t, entre(b0, C["s10.end"], 0.6), ps("nenhum número diferente de 0, vezes outro diferente de 0, dá 0", "i", 50, TINTA2), W / 2, 990, "center", passo=0.07)
    fase(c, t, C["s10"], C["s11"] - 0.1, s10)

    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]

    def s11():
        s2, y2 = 120, 300
        form(c, t, C["s11"] + 0.05, P, W / 2, y2, s2, align="center")
        regra_zero(c, t, C["s11"] + 0.05, W / 2, 140, 44)
        realce(c, t, a1, P, "(x + 7)", W / 2, y2, s2, align="center")
        ramo(c, t, a1, P, "(x + 7)", W / 2, y2, s2, 520, 580, align="center")
        monta(c, t, [pf("x + 7 = 0", a1 + 0.3), pf("  →  ", a1 + 1.0), pf("x = −7", a1 + 1.3, CERTO)], 520, 580, 84, "center")
        realce(c, t, b1, P, "(x − 7)", W / 2, y2, s2, align="center")
        ramo(c, t, b1, P, "(x − 7)", W / 2, y2, s2, 1400, 580, align="center")
        monta(c, t, [pf("x − 7 = 0", b1 + 0.3), pf("  →  ", b1 + 1.0), pf("x = 7", b1 + 1.3, CERTO)], 1400, 580, 84, "center")
        E.foco(c, t, c1, 0.5, lambda p: E.pilula(c, "as mesmas duas raízes", W / 2, 800, 60, estilo="g", fundo=CERTO, cor=BR, a=p))
    fase(c, t, C["s11"], 1e9, s11)


# ---------------- sem c ----------------
def b_semc(c, t, C, b):
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    Q = "x^2 − 5x = 0"

    def s12():
        E.frase(c, t, a2, ps("2º caso:", "g", 70, COR) + ps("sem o número sozinho", "i", 70), XE, 180, passo=0.1)
        coef(c, t, a2 + 1.0, "c", "0", 1500, 160, 44)
        form(c, t, b2, Q, XE, 440, 140)
        realce(c, t, c2, Q, "x", XE, 440, 140)
        realce(c, t, c2 + 0.3, Q, "x", XE, 440, 140, n=1)
        nota(c, t, c2 + 0.5, "o x está nos dois termos", 1100, 420, 54, COR)
        form(c, t, d2, "=", XE, 700, 140)
        x0 = XE + fw("= ", 140)
        evid(c, t, d2, "x", "x − 5", x0, 700, 140, t1=d2 + 0.5)
        form(c, t, d2 + 1.0, " = 0", x0 + fw("x(x − 5)", 140), 700, 140)
    fase(c, t, C["s12"], C["s13"] - 0.1, s12)

    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    P = "x(x − 5) = 0"

    def s13():
        s2, y2 = 120, 280
        form(c, t, C["s13"] + 0.05, P, W / 2, y2, s2, align="center")
        regra_zero(c, t, a3, W / 2, 130, 44)
        realce(c, t, b3, P, "x", W / 2, y2, s2, align="center")
        ramo(c, t, b3, P, "x", W / 2, y2, s2, 560, 530, align="center")
        form(c, t, b3 + 0.3, "x = 0", 560, 530, 96, CERTO, align="center")
        realce(c, t, c3, P, "(x − 5)", W / 2, y2, s2, align="center")
        ramo(c, t, c3, P, "(x − 5)", W / 2, y2, s2, 1360, 530, align="center")
        monta(c, t, [pf("x − 5 = 0", c3 + 0.3), pf("  →  ", c3 + 1.2), pf("x = 5", c3 + 1.5, CERTO)], 1360, 530, 96, "center")
        nota(c, t, d3 - 0.4, "conferindo", XE, 700, 52)
        monta(c, t, [pf("5^2 − 5 · 5", d3), pf(" = 25 − 25 = 0", d3 + 1.0)], XE, 810, 84)
        selo_em(c, t, d3 + 2.0, 1300, 780, 38)
        monta(c, t, [pf("0^2 − 5 · 0", e3), pf(" = 0 − 0 = 0", e3 + 0.8)], XE, 950, 84)
        selo_em(c, t, e3 + 1.6, 1300, 920, 38)
    fase(c, t, C["s13"], 1e9, s13)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s14.{k}"] for k in "abcde")
    Q = "x^2 − 5x = 0"
    E.frase(c, t, C["s14"] + 0.3, ps("o erro mais comum:", "g", 80, ERRADO) + ps("dividir por x", "i", 80), XE, 170, passo=0.1)
    form(c, t, C["s14"] + 1.5, Q, XE, 380, 110)
    nos_dois(c, t, a_, Q, "÷ x", XE, 380, 110, ERRADO)
    form(c, t, b_, "x − 5 = 0", XE, 620, 110)
    form(c, t, b_ + 0.8, "→  x = 5", XE + fw("x − 5 = 0 ", 110), 620, 110, TINTA2)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "o zero sumiu", 1450, 590, 60, estilo="g", fundo=ERRADO, cor=BR, a=p))
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "x pode ser 0, e divisão por zero não existe", W / 2, 790, 54, estilo="g", fundo=ERRADO, cor=BR, a=p))
    E.foco(c, t, e_, 0.5, lambda p: E.pilula(c, "coloque o x em evidência; nunca divida por ele", W / 2, 940, 56, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    MB = [("−", BR), ("b", CB_L)]
    DA = [("a", CA_L)]

    def s15():
        E.frase(c, t, C["s15"] + 0.2, ps("o atalho:", "i", 72, CLARO) + ps("sem o número sozinho", "g", 66, BR), XE, 170, passo=0.1)
        E.foco(c, t, a5, 0.45, lambda p: num_bola(c, "1", XE + 40, 310, 36, 46, p, AM, "#07070F"))
        E.frase(c, t, a5, ps("uma raiz é sempre", "i", 66, CLARO), XE + 100, 332, passo=0.08)
        form(c, t, a5 + 1.0, "x = 0", XE + 720, 335, 90, AM)
        E.foco(c, t, b5, 0.45, lambda p: num_bola(c, "2", XE + 40, 480, 36, 46, p, AM, "#07070F"))
        E.frase(c, t, b5, ps("a outra:", "i", 66, CLARO), XE + 100, 502, passo=0.08)
        form(c, t, b5 + 0.3, "x =", XE + 400, 505, 90, BR)
        fra_p_em(c, t, b5 + 0.4, MB, DA, XE + 400 + fw("x = ", 90) + 60, 475, 80, BR)
        monta(c, t, [pf("3", c5, CA_L), pf("x^2 + ", c5, BR), pf("12", c5, CB_L), pf("x = 0", c5, BR)], XE, 760, 110)
        form(c, t, d5, "x = 0", XE, 940, 100, AM)
        E.foco(c, t, d5 + 0.6, 0.4, lambda q: E.escreve(c, "e", XE + fw("x = 0", 100) + 50, 935, 70, "i", CLARO, q))
        x1 = XE + fw("x = 0", 100) + 150
        form(c, t, d5 + 0.8, "x =", x1, 940, 100, AM)
        fra_p_em(c, t, d5 + 1.0, [("−", BR), ("12", CB_L)], [("3", CA_L)], x1 + fw("x = ", 100) + 75, 905, 80, BR)
        form(c, t, d5 + 2.0, "= −4", x1 + fw("x = ", 100) + 160, 940, 100, AM)
    fase(c, t, C["s15"], C["s16"] - 0.1, s15)

    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")

    def s16():
        E.frase(c, t, C["s16"] + 0.2, ps("funciona porque", "i", 76, CLARO), XE, 180, passo=0.1)
        monta(c, t, [pf("x(", a6, BR), pf("a", a6, CA_L), pf("x + ", a6, BR), pf("b", a6, CB_L), pf(") = 0", a6, BR)], XE, 360, 110)
        monta(c, t, [pf("a", b6, CA_L), pf("x + ", b6, BR), pf("b", b6, CB_L), pf(" = 0  →  x =", b6, BR)], XE, 540, 100)
        xf = XE + fw("ax + b = 0  →  x = ", 100) + 60
        fra_p_em(c, t, b6 + 0.6, MB, DA, xf, 505, 80, BR)
        selo_em(c, t, c6, XE + 40, 735, 38, True)
        E.frase(c, t, c6, ps("só vale com", "i", 62, CLARO), XE + 110, 758, passo=0.08)
        monta(c, t, [pf("c", c6 + 0.6, CC_L), pf(" = 0", c6 + 0.6, BR)], XE + 500, 760, 70)
        selo_em(c, t, d6, XE + 40, 885, 38, False)
        E.frase(c, t, d6, ps("com os três termos:", "i", 62, CLARO) + ps("completa, outro caminho", "g", 62, BR), XE + 110, 908, passo=0.08)
    fase(c, t, C["s16"], 1e9, s16)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_ = C["s17.a"], C["s17.b"]
    E.frase(c, t, C["s17"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s17"] + 1.0, ps("resolva as duas", "i", 90), XE, 360, passo=0.1)
    E.foco(c, t, a_, 0.45, lambda p: num_bola(c, "1", XE + 40, 540, 40, 50, p))
    form(c, t, a_ + 0.1, "2x^2 − 72 = 0", XE + 120, 575, 110, COR)
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "2", XE + 40, 760, 40, 50, p))
    form(c, t, b_ + 0.1, "x^2 = 6x", XE + 120, 795, 110, COR)
    E.relogio(c, t, C["s18.a"], 1520, 500, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]

    def s19():
        E.foco(c, t, C["s19"] + 0.2, 0.45, lambda p: num_bola(c, "1", XE + 40, 200, 40, 50, p))
        form(c, t, C["s19"] + 0.3, "2x^2 − 72 = 0", XE + 120, 235, 96, TINTA2)
        nos_dois(c, t, a9, "2x^2 − 72 = 0", "+ 72", XE + 120, 235, 96)
        form(c, t, a9 + 0.8, "2x^2 = 72", XE + 120, 470, 110)
        form(c, t, b9, "x^2 = 36", XE + 120, 650, 110)
        nota(c, t, b9 + 0.3, "÷ 2 nos dois lados", XE + 700, 640, 54, COR)
        raizes(c, t, c9, ("6", "−6"), W / 2, 880, 130, align="center", t1=c9 + 1.0)
    fase(c, t, C["s19"], C["s20"] - 0.1, s19)

    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")

    def s20():
        E.foco(c, t, C["s20"] + 0.1, 0.45, lambda p: num_bola(c, "2", XE + 40, 200, 40, 50, p))
        form(c, t, C["s20"] + 0.2, "x^2 = 6x", XE + 120, 235, 96, TINTA2)
        form(c, t, a0, "x^2 − 6x = 0", XE + 120, 420, 110)
        nota(c, t, a0 + 0.4, "tudo para um lado", XE + 950, 410, 54, COR)
        evid(c, t, b0, "x", "x − 6", XE + 120, 600, 110, t1=b0 + 0.5)
        form(c, t, b0 + 0.9, " = 0", XE + 120 + fw("x(x − 6)", 110), 600, 110)
        raizes(c, t, c0, ("0", "6"), W / 2, 810, 130, align="center", t1=c0 + 1.0)
        E.foco(c, t, d0, 0.5, lambda p: E.pilula(c, "dividiu por x? perdeu o 0", W / 2, 960, 56, estilo="g", fundo=ERRADO, cor=BR, a=p))
    fase(c, t, C["s20"], 1e9, s20)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s21.a"], ps("sem b:", "g", 70, CB) + ps("isole o", "i", 70) + [("x²", "g", 64)] + ps("e pegue", "i", 70) + ps("as duas raízes", "g", 70, COR)),
             (C["s21.b"], ps("sem c:", "g", 70, CC) + ps("x em evidência, e", "i", 70) + ps("uma raiz é zero", "g", 70, COR)))
    fim_padrao(c, t, C, "s21", "s22", itens, "próxima aula: a equação completa", "com os três termos",
               extra=lambda: (form(c, t, C["s22.b"], "x^2 − 5x + 6 = 0", XE, 590, 100),
                              E.frase(c, t, C["s22.c"], ps("a fórmula de", "i", 80) + ps("Bhaskara", "g", 84, COR), XE, 760, passo=0.12)))


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, forma=b_forma, semb=b_semb, semc=b_semc, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
