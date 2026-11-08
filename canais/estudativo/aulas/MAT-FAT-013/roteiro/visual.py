"""Visual — Estudativo · MAT-FAT-013: equações que viram do 2º grau.
x⁴ − 13x² + 36 = 0 com a troca y = x² (y² − 13y + 36 = 0, y = 4 ou 9) e a volta para o x (±2 e ±3); a biquadrada e o
cuidado com y negativo; 6/x = x − 1 com o valor proibido, multiplicada por x; o erro de parar no y; no palco, o atalho de
achar as positivas e espelhar, que não vale com expoente ímpar.

Convenções da trilha (as de MAT-FAT-004 a 012: proibido, nos_dois, raizes, coeficientes coloridos; soma e produto em
pílulas na cor do b e do c, com o par em esferas, de MAT-FAT-011). Nova: TROCA DE LETRA = pílula "y = x²" na cor da
matéria no canto, enquanto se trabalha com o y, e o y escrito na cor da matéria; a VOLTA PARA O X é uma seta de cada valor
de y até a sua linha de x (volta).
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-013_equacoes_que_viram_2grau.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("troca", "fracao", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"

# as contas da aula
f4 = lambda x: x ** 4 - 13 * x ** 2 + 36
assert [y for y in range(-40, 41) if y * y - 13 * y + 36 == 0] == [4, 9] and 4 + 9 == 13 and 4 * 9 == 36
assert [x for x in range(-10, 11) if f4(x) == 0] == [-3, -2, 2, 3] and 16 - 52 + 36 == 0
assert [x for x in range(-10, 11) if x != 0 and 6 == x * (x - 1)] == [-2, 3] and 6 / 3 == 3 - 1 and 6 / -2 == -2 - 1
assert f4(4) == 256 - 208 + 36 == 84 and 6 / -3 == -2 != -3 - 1 == -4
assert [x for x in range(-10, 11) if x ** 4 - 10 * x ** 2 + 9 == 0] == [-3, -1, 1, 3]
assert [x for x in range(-10, 11) if x != 0 and x * x + 4 == 5 * x] == [1, 4] and 4 + 4 / 4 == 5
del f4


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


def nos_dois(c, t, t0, s, op, x, y, size, cor=None, align="left", dy=None):
    """o mesmo nos dois lados (balança): pílula com a operação embaixo de cada lado da equação s"""
    i = s.index("=")
    xi = x - fw(s, size) / 2 if align == "center" else x
    x0, we = xi, fw(s[:i].strip(), size)
    x1, wd = xi + fw(s[:i + 2], size), fw(s[i + 2:], size)
    for k, (xx, ww) in enumerate(((x0, we), (x1, wd))):
        E.foco(c, t, t0 + 0.15 * k, 0.4, lambda p, xx=xx, ww=ww: E.pilula(c, op, xx + ww / 2, y + (dy if dy is not None else size * 0.62), size * 0.42, estilo="g", fundo=cor or E.COR, cor=BR, a=p), sobe=8)


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


def sp(c, t, ts, tp, S, P, cx, cy, size=56, gap=300, escuro=False):
    """soma e produto (de MAT-FAT-011): pílula da soma na cor do b e do produto na cor do c"""
    cb, cc = (CB_L, CC_L) if escuro else (CB, CC)
    tinta = "#07070F" if escuro else BR
    E.foco(c, t, ts, 0.45, lambda p: E.pilula(c, f"soma {S}", cx - gap, cy, size, estilo="g", fundo=cb, cor=tinta, a=p), sobe=8)
    E.foco(c, t, tp, 0.45, lambda p: E.pilula(c, f"produto {P}", cx + gap, cy, size, estilo="g", fundo=cc, cor=tinta, a=p), sobe=8)


def par(c, t, t0, t1, vals, cx, cy, r=70, gap=150, cor=None, t2=None):
    """as raízes procuradas em esferas: "?" em t0, os números em t1 (de MAT-FAT-011, para n valores)"""
    n = len(vals)
    for k, v in enumerate(vals):
        x = cx + (k - (n - 1) / 2) * gap
        q = ep(t, t0 + 0.12 * k, 0.5)
        if q <= 0:
            continue
        E.bola(c, x, cy, r * ease_back(min(1.0, q)), cor, q)
        mostra = ep(t, (t1 if t2 is None else (t1 if k == 0 else t2)) + 0.12 * k, 0.35)
        if mostra < 1:
            centro(c, "?", x, cy + r * 0.38, r, "g", BR, q * (1 - mostra))
        if mostra > 0:
            centro(c, str(v), x, cy + r * 0.36, r * (0.95 if len(str(v)) < 3 else 0.75), "g", BR, mostra)


def troca(c, t, t0, cx=1640, cy=120, size=50, t1=1e9):
    """troca de letra (convenção da trilha): pílula "y = x²" no canto enquanto se trabalha com o y"""
    fase(c, t, t0, t1, lambda: E.foco(c, t, t0, 0.45, lambda p: E.pilula(c, "y = x²", cx, cy, size, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p), sobe=6))


def yeq(c, t, t0, b, cc, x, y, size, align="left", tinta=None):
    """y² − b·y + c = 0 com o y na cor da matéria"""
    k = tinta or TINTA
    return monta(c, t, [pf("y", t0, COR), pf("^2 − " + b, t0, k), pf("y", t0, COR), pf(" + " + cc + " = 0", t0, k)], x, y, size, align)


def volta(c, t, t0, yv, raizes_, x, ytop, y1, y2, size=96):
    """a volta para o x (convenção da trilha): seta do valor de y (em x, ytop) até "x² = 4", e as raízes do x embaixo"""
    p = ep(t, t0, 0.5)
    if p > 0:
        M.arrow(c, x + 60, ytop + 30, x + 60, y1 - size * 1.0, FIO, p, 5, 16, p)
    form(c, t, t0 + 0.3, "x^2 = " + yv, x, y1, size)
    raizes(c, t, t0 + 1.1, raizes_, x, y2, size * 0.9, t1=t0 + 1.6)


def ys(c, t, t0, v1, v2, x1, x2, y, size, t1=None):
    """os dois valores de y, cada um em cima da sua coluna"""
    form(c, t, t0, "y = " + v1, x1, y, size, COR)
    E.foco(c, t, t0 + 0.2, 0.4, lambda q: E.escreve(c, "ou", (x1 + x2) / 2 + 40, y, size * 0.8, "i", TINTA2, q))
    form(c, t, t1 if t1 is not None else t0 + 0.4, "y = " + v2, x2, y, size, COR)


# ---------------- gancho ----------------
Q4 = "x^4 − 13x^2 + 36 = 0"


def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def conta():
        form(c, t, a_, Q4, W / 2, 380, 150, align="center")
        xe, we = trecho_x(Q4, "x^4", W / 2, 150, "center")
        tz = entre(a_, b_, 0.45)
        E.foco(c, t, tz, 0.45, lambda p: c.drawCircle(xe + we - 22, 380 - 125, 46, M.paint(COR, p, stroke=6)))
        E.frase(c, t, tz + 0.4, ps("expoente 4:", "g", 64, COR) + ps("parece outro assunto", "i", 64), W / 2, 560, "center", passo=0.08)
        E.foco(c, t, b_, 0.5, lambda p: E.pilula(c, "uma troca de letra: y = x²", W / 2, 720, 64, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
        E.frase(c, t, c_, ps("e vira do 2º grau,", "i", 70) + ps("de cabeça", "g", 70, CERTO), W / 2, 890, "center", passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2 = C["s02.a"], C["s02.b"]
    E.frase(c, t, a2, ps("até o fim desta aula, você", "i", 84), XE, 280, passo=0.12)
    E.frase(c, t, a2 + 1.0, ps("desmonta o disfarce", "g", 110, COR), XE, 430, passo=0.13)
    E.frase(c, t, b2, ps("e o de", "i", 76) + ps("x embaixo da fração", "g", 76, COR), XE, 620, passo=0.12)
    form(c, t, b2 + 1.0, "f{6}{x} = x − 1", XE + 60, 840, 130)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s03.{k}"] for k in "abcd")
    E.frase(c, t, a_, ps("três", "g", 84, COR) + ps("ferramentas", "i", 90), XE, 180)
    xr = XE + 110
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "1", XE + 40, 330, 40, 50, p))
    E.frase(c, t, b_, ps("soma e produto:", "g", 64, COR) + ps("raízes de cabeça", "i", 64), xr, 352, passo=0.08)
    form(c, t, b_ + 1.2, "x^2 − 7x + 12 = 0  →  3 e 4", xr + 20, 460, 76, TINTA2)
    E.foco(c, t, c_, 0.45, lambda p: num_bola(c, "2", XE + 40, 590, 40, 50, p))
    E.frase(c, t, c_, ps("potência de potência:", "g", 64, COR), xr, 612, passo=0.08)
    form(c, t, c_ + 1.0, "(x^2)^2 = x^4", xr + 700, 618, 90)
    E.foco(c, t, d_, 0.45, lambda p: num_bola(c, "3", XE + 40, 790, 40, 50, p))
    E.frase(c, t, d_, ps("o valor proibido", "g", 64, COR) + ps("de uma fração com letra", "i", 64), xr, 812, passo=0.08)
    form(c, t, d_ + 1.2, "f{5}{x − 3}", xr + 40, 930, 80)
    proibido(c, t, d_ + 1.6, "x ≠ 3", xr + 340, 905, 50)
    E.frase(c, t, C["s04"] - 2.2, ps("faltou alguma? procure no canal", "i", 52, TINTA2), 1150, 1010, passo=0.08)


# ---------------- a troca ----------------
def b_troca(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    troca(c, t, b4)

    def s04():
        form(c, t, C["s04"] + 0.1, Q4, XE, 200, 84, TINTA2)
        form(c, t, a4, "x^4 = (x^2)^2", XE, 400, 120)
        realce(c, t, b4, "x^4 = (x^2)^2", "x^2", XE, 400, 120)
        monta(c, t, [pf("x^4 → ", c4), pf("y", c4, COR), pf("^2", c4)], 1050, 400, 110)
        yeq(c, t, d4, "13", "36", W / 2, 720, 140, "center")
        p = ep(t, d4 - 0.5, 0.5)
        if p > 0:
            M.arrow(c, W / 2, 500, W / 2, 590, FIO, p, 6, 18, p)
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)

    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]

    def s05():
        yeq(c, t, C["s05"] + 0.05, "13", "36", XE, 200, 90)
        nota(c, t, C["s05"] + 0.4, "essa você conhece", 1100, 190, 56, COR)
        sp(c, t, a5, a5 + 0.6, 13, 36, W / 2, 360, 58, 300)
        par(c, t, a5 + 1.0, b5, (4, 9), W / 2, 560, 80, 170)
        form(c, t, b5 + 0.6, "4 + 9 = 13", XE + 60, 590, 76, CB)
        form(c, t, b5 + 0.9, "4 · 9 = 36", 1350, 590, 76, CC)
        raizes(c, t, c5, ("4", "9"), W / 2, 820, 120, COR, "center", t1=c5 + 0.8, var="y")
    fase(c, t, C["s05"], 1e9, s05)


# ---------------- a volta ----------------
def b_volta(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    troca(c, t, C["s06"], t1=C["s07"] - 0.1)

    def s06():
        E.frase(c, t, a6, ps("a pergunta é o", "i", 66) + ps("x,", "g", 66, COR) + ps("não o y", "i", 66), XE, 180, passo=0.08)
        ys(c, t, C["s06"] + 0.05, "4", "9", XE, 1000, 340, 100)
        volta(c, t, b6, "4", ("2", "−2"), XE, 340, 580, 790, 100)
        volta(c, t, c6, "9", ("3", "−3"), 1000, 340, 580, 790, 100)
    fase(c, t, C["s06"], C["s07"] - 0.1, s06)

    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]

    def s07():
        E.frase(c, t, a7, ps("quatro raízes", "g", 72, COR), XE, 200, passo=0.1)
        par(c, t, a7 + 0.3, a7 + 0.6, ("−3", "−2", "2", "3"), W / 2, 380, 72, 190, CERTO)
        monta(c, t, [pf("x = 2:  ", b7, CERTO), pf("2^4 − 13 · 2^2 + 36", b7 + 0.2), pf(" = 16 − 52 + 36 = 0", b7 + 1.2)], XE, 620, 76)
        selo_em(c, t, b7 + 2.6, 1730, 590, 38)
        E.foco(c, t, c7 - 1.5, 0.5, lambda p: E.pilula(c, "biquadrada", 560, 830, 70, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
        form(c, t, c7 - 1.0, "x^4, x^2 e número", 900, 850, 76, TINTA2)
    fase(c, t, C["s07"], C["s08"] - 0.1, s07)

    a8, b8 = C["s08.a"], C["s08.b"]

    def s08():
        E.frase(c, t, C["s08"] + 0.2, ps("um cuidado", "g", 76, ERRADO), XE, 200, passo=0.1)
        monta(c, t, [pf("y = −4", a8, ERRADO), pf("  →  x^2 = −4 ?", a8 + 0.6)], XE, 430, 110)
        E.foco(c, t, a8 + 1.4, 0.45, lambda p: E.pilula(c, "não gera x nenhum", 1450, 400, 54, estilo="g", fundo=ERRADO, cor=BR, a=p))
        E.frase(c, t, entre(a8, b8, 0.5), ps("o y é x²:", "g", 64, COR), XE, 620, passo=0.08)
        E.frase(c, t, b8, ps("número vezes ele mesmo", "i", 70) + ps("nunca dá negativo", "g", 70, COR), XE, 760, passo=0.1)
    fase(c, t, C["s08"], 1e9, s08)


# ---------------- a fração ----------------
QF = "f{6}{x} = x − 1"


def b_fracao(c, t, C, b):
    a9, b9 = C["s09.a"], C["s09.b"]

    def s09():
        E.frase(c, t, C["s09"] + 0.2, ps("outro disfarce", "i", 76), XE, 200, passo=0.1)
        form(c, t, a9, QF, W / 2, 520, 170, align="center")
        nota(c, t, a9 + 1.5, "x embaixo da fração", W / 2, 700, 58, align="center")
        proibido(c, t, b9, "x ≠ 0", W / 2, 860, 70)
    fase(c, t, C["s09"], C["s10"] - 0.1, s09)

    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")

    def s10():
        form(c, t, C["s10"] + 0.05, QF, XE, 260, 130)
        proibido(c, t, C["s10"] + 0.05, "x ≠ 0", 1600, 140, 46)
        nos_dois(c, t, a0, QF, "× x", XE, 260, 130, dy=150)
        monta(c, t, [pf("6", b0), pf(" = ", c0), pf("x(x − 1)", c0), pf(" = x^2 − x", c0 + 1.5)], XE, 580, 110)
        nota(c, t, b0 + 0.2, "o x de baixo some", XE, 680, 52, COR)
        form(c, t, d0, "x^2 − x − 6 = 0", XE, 860, 130, COR)
        nota(c, t, d0 + 0.4, "tudo para um lado", 1150, 850, 54)
    fase(c, t, C["s10"], C["s11"] - 0.1, s10)

    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")

    def s11():
        form(c, t, C["s11"] + 0.05, "x^2 − x − 6 = 0", XE, 200, 90, TINTA2)
        proibido(c, t, C["s11"] + 0.05, "x ≠ 0", 1600, 140, 46)
        sp(c, t, a1, a1 + 0.5, 1, "−6", W / 2, 360, 56, 300)
        E.frase(c, t, b1, ps("produto negativo:", "i", 60) + ps("sinais contrários", "g", 60, COR), W / 2, 500, "center", passo=0.08)
        par(c, t, b1 + 0.4, c1, (3, "−2"), W / 2, 670, 76, 200)
        E.frase(c, t, d1 - 0.6, ps("nenhuma é o 0 proibido:", "i", 60), XE, 900, passo=0.08)
        raizes(c, t, d1, ("3", "−2"), 1050, 900, 100, t1=d1 + 0.3)
    fase(c, t, C["s11"], C["s12"] - 0.1, s11)

    a2, b2 = C["s12.a"], C["s12.b"]

    def s12():
        nota(c, t, C["s12"] + 0.2, "conferindo na equação original", XE, 200, 60)
        monta(c, t, [pf("x = 3:  ", a2, CERTO), pf("f{6}{3} = 2", a2 + 0.3), pf("   e   3 − 1 = 2", a2 + 1.5)], XE, 420, 100)
        selo_em(c, t, a2 + 2.6, 1700, 385, 42)
        monta(c, t, [pf("x = −2:  ", b2, CERTO), pf("f{6}{−2} = −3", b2 + 0.3), pf("   e   −2 − 1 = −3", b2 + 2.2)], XE, 680, 100)
        selo_em(c, t, b2 + 3.2, 1700, 645, 42)
    fase(c, t, C["s12"], 1e9, s12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s13.{k}"] for k in "abcd")
    E.frase(c, t, C["s13"] + 0.3, ps("o erro mais comum:", "g", 80, ERRADO) + ps("parar no y", "i", 80), XE, 170, passo=0.1)
    yeq(c, t, a_ + 0.5, "13", "36", XE, 330, 84)
    form(c, t, a_ + 1.0, "→  y = 4 ou y = 9", XE + fw("y^2 − 13y + 36 = 0 ", 84), 330, 84, TINTA2)
    E.foco(c, t, b_, 0.45, lambda p: E.pilula(c, "resposta: 4 e 9 ?", 560, 470, 58, estilo="g", fundo=ERRADO, cor=BR, a=p), sobe=8)
    nota(c, t, c_ - 0.6, "teste o 4 no lugar do x:", XE, 610, 54)
    form(c, t, c_, "4^4 − 13 · 4^2 + 36 = 256 − 208 + 36 = 84", XE, 730, 80, ERRADO)
    E.frase(c, t, c_ + 2.4, ps("não deu zero", "g", 60, ERRADO), XE, 830, passo=0.08)
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "o y é só um apoio: sempre volte para o x", W / 2, 960, 60, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]

    def s14():
        E.frase(c, t, C["s14"] + 0.2, ps("o atalho da biquadrada:", "i", 72, CLARO), XE, 170, passo=0.1)
        E.frase(c, t, a4, ps("ache só as positivas e", "i", 76, CLARO) + ps("espelhe", "g", 80, AM), XE, 300, passo=0.1)
        vx = E.reta(c, t, a4 + 0.4, 360, 1560, 560, -4, 4, list(range(-4, 5)), escuro=True, size=44)
        for k, v in enumerate((2, 3)):
            E.foco(c, t, a4 + 1.0 + 0.3 * k, 0.4, lambda p, v=v: E.bola(c, vx(v), 560, 24, AM, p))
            E.salto(c, t, b4 + 0.3 * k, vx(v), vx(-v), 560, 110 + 50 * k, CLARO)
            E.foco(c, t, b4 + 0.6 + 0.3 * k, 0.4, lambda p, v=v: E.bola(c, vx(-v), 560, 24, AM, p))
        E.frase(c, t, b4 + 0.3, ps("se 2 serve,", "i", 64, CLARO) + ps("−2 também", "g", 64, BR), XE, 760, passo=0.08)
        E.frase(c, t, c4, ps("o x só tem expoente par:", "i", 60, CLARO), XE, 900, passo=0.08)
        form(c, t, c4 + 1.0, "(−2)^4 = 2^4 = 16", XE + 760, 905, 80, AM)
    fase(c, t, C["s14"], C["s15"] - 0.1, s14)

    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]

    def s15():
        selo_em(c, t, a5, XE + 40, 210, 38, False)
        E.frase(c, t, a5, ps("não vale com", "i", 66, CLARO) + ps("expoente ímpar", "g", 66, BR), XE + 110, 232, passo=0.08)
        form(c, t, b5, "x^3,  x", XE + 110, 360, 90, CLARO)
        form(c, t, c5 - 0.5, QF, XE, 560, 110, BR)
        monta(c, t, [pf("x = 3:  ", c5, AM), pf("f{6}{3} = 2 = 3 − 1", c5 + 0.3, BR)], XE, 760, 90)
        selo_em(c, t, c5 + 1.0, 1300, 730, 36, True)
        monta(c, t, [pf("x = −3:  ", c5 + 1.5, AM), pf("f{6}{−3} = −2", c5 + 2.0, BR), pf(",  −3 − 1 = −4", c5 + 3.5, BR)], XE, 930, 90)
        selo_em(c, t, c5 + 4.2, 1500, 900, 36, False)
    fase(c, t, C["s15"], 1e9, s15)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_ = C["s16.a"], C["s16.b"]
    E.frase(c, t, C["s16"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16"] + 1.2, ps("resolva as duas", "i", 84), XE, 340, passo=0.1)
    E.foco(c, t, a_, 0.45, lambda p: num_bola(c, "1", XE + 40, 510, 40, 50, p))
    form(c, t, a_ + 0.1, "x^4 − 10x^2 + 9 = 0", XE + 120, 545, 104, COR)
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "2", XE + 40, 730, 40, 50, p))
    form(c, t, b_ + 0.1, "x + f{4}{x} = 5", XE + 120, 765, 104, COR)
    nota(c, t, entre(b_, C["s16.end"], 0.55), "só o 4 fica em cima do x", XE + 120, 900, 54)
    E.relogio(c, t, C["s17.a"], 1560, 480, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    troca(c, t, C["s18"] + 0.3, t1=C["s19"] - 0.1)

    def s18():
        E.foco(c, t, C["s18"] + 0.1, 0.45, lambda p: num_bola(c, "1", XE + 40, 190, 40, 50, p))
        form(c, t, C["s18"] + 0.2, "x^4 − 10x^2 + 9 = 0", XE + 120, 225, 84, TINTA2)
        yeq(c, t, a8, "10", "9", XE, 390, 100)
        sp(c, t, b8, b8 + 0.4, 10, 9, 1350, 360, 46, 220)
        ys(c, t, b8 + 1.2, "1", "9", XE, 1000, 540, 84)
        volta(c, t, c8, "1", ("1", "−1"), XE, 540, 760, 940, 84)
        volta(c, t, d8, "9", ("3", "−3"), 1000, 540, 760, 940, 84)
    fase(c, t, C["s18"], C["s19"] - 0.1, s18)

    a9, b9, c9, d9, e9 = (C[f"s19.{k}"] for k in "abcde")

    def s19():
        E.foco(c, t, C["s19"] + 0.1, 0.45, lambda p: num_bola(c, "2", XE + 40, 190, 40, 50, p))
        form(c, t, C["s19"] + 0.2, "x + f{4}{x} = 5", XE + 120, 225, 84, TINTA2)
        proibido(c, t, a9, "x ≠ 0", 900, 200, 46)
        form(c, t, b9, "x^2 + 4 = 5x", XE, 410, 100)
        nota(c, t, b9 + 0.3, "× x em tudo", 900, 400, 54, COR)
        form(c, t, c9, "x^2 − 5x + 4 = 0", XE, 590, 110, COR)
        sp(c, t, d9, d9 + 0.4, 5, 4, 1350, 560, 46, 210)
        raizes(c, t, d9 + 1.2, ("1", "4"), XE, 790, 110, t1=d9 + 1.5)
        monta(c, t, [pf("x = 4:  ", e9, CERTO), pf("4 + f{4}{4} = 4 + 1 = 5", e9 + 0.3)], XE, 960, 84)
        selo_em(c, t, e9 + 1.3, 1350, 930, 38)
    fase(c, t, C["s19"], 1e9, s19)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s20.a"], ps("troque", "i", 70) + [("x²", "g", 70)] + ps("por", "i", 70) + ps("y", "g", 70, COR) + ps("e volte no fim", "i", 70)),
             (C["s20.b"], ps("x embaixo:", "g", 70, COR) + ps("anote o proibido e multiplique por x", "i", 66)))
    fim_padrao(c, t, C, "s20", "s21", itens, "próxima aula: pratique tudo de", "equação do 2º grau",
               extra=lambda: (E.frase(c, t, C["s21.b"], ps("o", "i", 64) + ps("caminho mais curto", "g", 64, COR) + ps("para cada uma", "i", 64), XE, 580, passo=0.08),
                              E.frase(c, t, C["s21.c"], ps("e", "i", 64) + ps("monta a equação", "g", 64, COR) + ps("a partir de um problema", "i", 64), XE, 720, passo=0.08)))


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, troca=b_troca, volta=b_volta, fracao=b_fracao, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
