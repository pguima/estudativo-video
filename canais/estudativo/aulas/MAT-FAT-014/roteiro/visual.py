"""Visual — Estudativo · MAT-FAT-014: praticando equação do 2º grau (cinco questões inéditas; fecha a trilha).
O mapa da escolha (incompleta, soma e produto, Bhaskara); (x − 3)² = 16 pelo "algo ao quadrado"; x² − 9x + 20 = 0 pelos
pares do produto; 2x² + 4x − 4 = 0 dividida por 2 e levada por Bhaskara até −1 ± √3, separando a fração em duas; no palco,
o atalho de dividir pelo fator comum antes de tudo; k = 25 para a raiz dupla; o cercado de contorno 26 m e área 40 m².
Cada questão: etiqueta "questão n", o enunciado e o relógio de pausa (como em MAT-FAT-006).

Convenções da trilha (as de MAT-FAT-004 a 013: coeficientes coloridos, nos_dois, raizes, delta_f, delta_pilula, delta_caso,
soma e produto em pílulas e o par em esferas, separar a fração em duas, filtro do problema).
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-014_praticando_equacao_2grau.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"

# as contas da aula
r3 = math.sqrt(3)
assert [x for x in range(-20, 21) if (x - 3) ** 2 == 16] == [-1, 7] and (-1 - 3) ** 2 == 16
assert [x for x in range(-20, 21) if x * x - 9 * x + 20 == 0] == [4, 5] and 4 + 5 == 9 and 4 * 5 == 20
for x in (-1 + r3, -1 - r3):
    assert abs(2 * x * x + 4 * x - 4) < 1e-12 and abs(x * x + 2 * x - 2) < 1e-12
assert 2 * 2 - 4 * 1 * (-2) == 12 == 4 * 3 and 4 * 4 - 4 * 2 * (-4) == 48 and abs(math.sqrt(12) - 2 * r3) < 1e-12
assert 100 - 4 * 25 == 0 and 10 / 2 == 5 and all(x * x - 10 * x + 25 == (x - 5) ** 2 for x in range(-5, 6))
assert 26 / 2 == 13 and [x for x in range(0, 14) if x * (13 - x) == 40] == [5, 8] and 5 * 8 == 40 and 5 + 8 + 5 + 8 == 26
del r3, x


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


T_ = TINTA


def sp(c, t, ts, tp, S, P, cx, cy, size=56, gap=300, escuro=False):
    """soma e produto (de MAT-FAT-011): pílula da soma na cor do b e do produto na cor do c"""
    cb, cc = (CB_L, CC_L) if escuro else (CB, CC)
    tinta = "#07070F" if escuro else BR
    E.foco(c, t, ts, 0.45, lambda p: E.pilula(c, f"soma {S}", cx - gap, cy, size, estilo="g", fundo=cb, cor=tinta, a=p), sobe=8)
    E.foco(c, t, tp, 0.45, lambda p: E.pilula(c, f"produto {P}", cx + gap, cy, size, estilo="g", fundo=cc, cor=tinta, a=p), sobe=8)


def par(c, t, t0, t1, vals, cx, cy, r=70, gap=150, cor=None):
    """as raízes procuradas em esferas: "?" em t0, os números em t1 (de MAT-FAT-011)"""
    n = len(vals)
    for k, v in enumerate(vals):
        x = cx + (k - (n - 1) / 2) * gap
        q = ep(t, t0 + 0.12 * k, 0.5)
        if q <= 0:
            continue
        E.bola(c, x, cy, r * ease_back(min(1.0, q)), cor, q)
        mostra = ep(t, t1 + 0.12 * k, 0.35)
        if mostra < 1:
            centro(c, "?", x, cy + r * 0.38, r, "g", BR, q * (1 - mostra))
        if mostra > 0:
            centro(c, str(v), x, cy + r * 0.36, r * (0.95 if len(str(v)) < 3 else 0.75), "g", BR, mostra)


def separa(c, t, ta, tb, tc, cima, partes, baixo, x0, y, size, res, tinta=None, cor_res=None):
    """separar a fração em duas (de MAT-FAT-010): a fração inteira, seta, as duas frações com ± e o resultado de cada uma"""
    k = tinta or TINTA
    cr = cor_res or CERTO
    fra(c, cima, baixo, x0, y, size, ep(t, ta - 0.6, 0.4), k)
    w0 = fra_w(cima, baixo, size)
    xa = x0 + w0 / 2 + 40
    p = ep(t, ta, 0.5)
    if p > 0:
        M.arrow(c, xa, y, xa + 140, y, CLARO if k == BR else TINTA2, p, 6, 18, p)
    w1, w2 = fra_w(partes[0], baixo, size), fra_w(partes[1], baixo, size)
    x1 = xa + 200 + w1 / 2
    xs = x1 + w1 / 2 + 70
    x2 = xs + 70 + w2 / 2
    fra_em(c, t, ta + 0.3, partes[0], baixo, x1, y, size, k)
    E.foco(c, t, ta + 0.5, 0.4, lambda q: centro(c, "±", xs, y + size * 0.35, size, "g", k, q))
    fra_em(c, t, ta + 0.7, partes[1], baixo, x2, y, size, k)
    form(c, t, tb, "= " + res[0], x1, y + size * 2.1, size * 0.9, cr, "center")
    form(c, t, tc, "= " + res[1], x2, y + size * 2.1, size * 0.9, cr, "center")
    return x1, x2


def enunciado(c, t, C, sid, pid, n, rot, verbo, desenha, t_verbo=None):
    ka, kb = C[f"{sid}.a"], C[f"{sid}.b"]
    questao(c, t, ka, n, rot)
    if verbo:
        E.frase(c, t, t_verbo if t_verbo is not None else entre(ka, kb, 0.55), ps(verbo, "i", 84), XE, 380, passo=0.1)
    desenha(kb)
    E.relogio(c, t, C[f"{pid}.a"], 1560, 520, 170)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    E.frase(c, t, ka, [("5", "g", 220, COR)] + ps("questões", "i", 130), XE, 360, passo=0.15)
    E.frase(c, t, ka + 0.8, ps("criadas para esta aula", "i", 70, TINTA2), XE, 470, passo=0.1)
    for i in range(5):
        E.foco(c, t, ka + 0.6 + i * 0.15, 0.5, lambda a, i=i: num_bola(c, str(i + 1), 1130 + i * 150, 300, 58, 70, a))
    E.frase(c, t, entre(ka, kb, 0.5), ps("todas saem por Bhaskara,", "i", 60, TINTA2), 1080, 450, passo=0.08)
    E.frase(c, t, kb, ps("mas quase todas têm um", "i", 64) + ps("caminho mais curto", "g", 64, COR), XE, 620, passo=0.1)
    E.foco(c, t, kc, 0.5, lambda a: E.bola(c, XE + 70, 800, 70 * ease_back(prog(t, kc, 0.5)), a=a), blur=0)
    E.foco(c, t, kc + 0.1, 0.4, lambda a: [M.rrect(c, XE + 70 + dx - 11, 770, 22, 60, 6, BR, a) for dx in (-17, 17)])
    E.frase(c, t, kc + 0.2, [("pause", "g", 80, COR)] + ps("e procure o caminho antes da resposta", "i", 76), XE + 170, 828, passo=0.12)


# ---------------- o mapa ----------------
def b_mapa(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s02.{k}"] for k in "abcd")
    E.frase(c, t, a_, ps("o", "i", 84) + ps("mapa da escolha", "g", 84, COR), XE, 190, passo=0.1)
    linhas = ((b_, "faltou um termo?", "incompleta: isole o x² ou evidência"),
              (c_, "a = 1 e números pequenos?", "soma e produto"),
              (d_, "nada disso?", "Bhaskara, com o Δ primeiro"))
    for k, (tk, perg, resp) in enumerate(linhas):
        yy = 380 + k * 190
        w = E.larg(perg, "g", 50) + 55
        E.foco(c, t, tk, 0.45, lambda p, perg=perg, yy=yy, w=w: E.pilula(c, perg, XE + w / 2, yy, 50, estilo="g", fundo=TINTA, cor=BR, a=p), sobe=8)
        pa = ep(t, tk + 0.4, 0.4)
        if pa > 0:
            M.arrow(c, XE + w + 30, yy, XE + w + 130, yy, TINTA2, pa, 5, 16, pa)
        E.frase(c, t, tk + 0.6, ps(resp, "g", 58, COR), XE + w + 170, yy + 20, passo=0.08)
    E.frase(c, t, entre(d_, C["s02.end"], 0.6), ps("travou? procure a aula no canal", "i", 52, TINTA2), XE, 1000, passo=0.08)


# ---------------- questão 1 ----------------
Q1 = "(x − 3)^2 = 16"


def b_questao1(c, t, C, b):
    enunciado(c, t, C, "s03", "s04", 1, "o caminho mais curto", "resolva",
              lambda kb: form(c, t, kb, Q1, XE + 40, 650, 170, COR))


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")

    def s05():
        E.frase(c, t, C["s05"] + 0.2, ps("dá para abrir e usar Bhaskara. mas olhe de novo", "i", 58, TINTA2), XE, 180, passo=0.07)
        form(c, t, C["s05"] + 0.3, Q1, W / 2, 380, 150, align="center")
        realce(c, t, a5, Q1, "x − 3", W / 2, 380, 150, align="center")
        xa, wa = trecho_x(Q1, "x − 3", W / 2, 150, "center")
        nota(c, t, a5 + 0.2, "algo", xa + wa / 2, 470, 60, COR, align="center")
        E.frase(c, t, a5 + 0.8, ps("algo ao quadrado dá 16:", "i", 60), XE, 590, passo=0.08)
        raizes(c, t, b5, ("4", "−4"), 1000, 590, 84, COR, var="algo", t1=b5 + 0.6)
        monta(c, t, [pf("x − 3 = 4", c5), pf("  →  ", c5 + 0.8), pf("x = 7", c5 + 1.4, CERTO)], XE, 770, 100)
        monta(c, t, [pf("x − 3 = −4", d5), pf("  →  ", d5 + 0.8), pf("x = −1", d5 + 1.6, CERTO)], XE, 930, 100)
    fase(c, t, C["s05"], C["s06"] - 0.1, s05)

    a6, b6 = C["s06.a"], C["s06.b"]

    def s06():
        raizes(c, t, C["s06"] + 0.05, ("7", "−1"), XE, 210, 96, t1=C["s06"] + 0.05)
        monta(c, t, [pf("x = −1:  ", a6, CERTO), pf("(−1 − 3)^2 = (−4)^2", a6 + 0.4), pf(" = 16", a6 + 2.4, CERTO)], XE, 450, 100)
        selo_em(c, t, a6 + 3.4, 1650, 410, 44)
        E.foco(c, t, b6, 0.5, lambda p: E.pilula(c, "só o 4? perdeu a raiz negativa", W / 2, 700, 64, estilo="g", fundo=ERRADO, cor=BR, a=p))
        E.frase(c, t, b6 + 1.6, ps("como em", "i", 60, TINTA2), 700, 880, passo=0.08)
        form(c, t, b6 + 2.0, "x^2 = 49", 960, 885, 80, TINTA2)
    fase(c, t, C["s06"], 1e9, s06)


# ---------------- questão 2 ----------------
Q2 = "x^2 − 9x + 20 = 0"


def b_questao2(c, t, C, b):
    enunciado(c, t, C, "s07", "s08", 2, "o caminho mais curto", "resolva",
              lambda kb: form(c, t, kb, Q2, XE + 40, 650, 130, COR))


def b_resposta2(c, t, C, b):
    a_, b_, c_, d_, e_, f_ = (C[f"s09.{k}"] for k in "abcdef")
    form(c, t, C["s09"] + 0.1, Q2, XE, 190, 90, TINTA2)
    E.foco(c, t, a_, 0.45, lambda p: E.pilula(c, "a = 1: soma e produto", 1450, 160, 50, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p), sobe=8)
    sp(c, t, b_, b_ + 0.5, 9, 20, W / 2, 320, 54, 300)
    for k, (p1, p2) in enumerate(((1, 20), (2, 10), (4, 5))):
        ok = p1 == 4
        form(c, t, c_ + 0.9 * k, f"{p1} · {p2}", XE + 60 + k * 330, 500, 84, CERTO if (ok and t >= d_) else TINTA)
    form(c, t, d_, "4 + 5 = 9", 1250, 500, 84, CB)
    selo_em(c, t, d_ + 0.8, 1700, 470, 38)
    raizes(c, t, e_, ("4", "5"), W / 2, 700, 120, align="center", t1=e_ + 0.4)
    E.foco(c, t, f_ - 1.5, 0.45, lambda p: E.pilula(c, "soma −9 ?", 470, 900, 52, estilo="g", fundo=ERRADO, cor=BR, a=p), sobe=8)
    form(c, t, f_, "−4 e −5", 760, 920, 84, ERRADO)
    E.frase(c, t, f_ + 1.0, ps("não servem", "g", 60, ERRADO), 1150, 915, passo=0.08)


# ---------------- questão 3 ----------------
Q3 = "2x^2 + 4x − 4 = 0"
Q3b = "x^2 + 2x − 2 = 0"


def b_questao3(c, t, C, b):
    enunciado(c, t, C, "s10", "s11", 3, "o caminho mais curto", "resolva",
              lambda kb: form(c, t, kb, Q3, XE + 40, 650, 130, COR))


def b_resposta3(c, t, C, b):
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")

    def s12():
        form(c, t, C["s12"] + 0.1, Q3, XE, 250, 110)
        E.frase(c, t, a2, ps("tudo é par:", "g", 60, COR) + ps("divida a equação inteira por 2", "i", 60), XE, 130, passo=0.08)
        nos_dois(c, t, a2 + 0.8, Q3, "÷ 2", XE, 250, 110)
        form(c, t, b2, Q3b, XE, 480, 120, COR)
        E.frase(c, t, entre(b2, c2, 0.4), ps("os pares de −2 não somam −2", "i", 58, TINTA2), XE, 620, passo=0.08)
        E.foco(c, t, c2, 0.5, lambda p: E.pilula(c, "então, Bhaskara", 1400, 600, 54, estilo="g", fundo=TINTA, cor=BR, a=p))
        form(c, t, d2, "Δ = 4 + 8 = 12", XE, 820, 110)
        delta_pilula(c, t, d2 + 1.5, "12", 1150, 790, 56)
    fase(c, t, C["s12"], C["s13"] - 0.1, s12)

    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")

    def s13():
        form(c, t, a3, "r{12} = r{4 · 3} = 2r{3}", XE, 200, 90)
        delta_pilula(c, t, C["s13"] + 0.05, "12", 1620, 150, 50)
        form(c, t, b3, "x =", XE, 470, 110)
        separa(c, t, entre(b3, c3, 0.75), c3, c3 + 1.6, "−2 ± 2r{3}", ("−2", "2r{3}"), "2", XE + fw("x = ", 110) + fra_w("−2 ± 2r{3}", "2", 100) / 2 + 20, 430, 100, ("−1", "r{3}"))
        nota(c, t, entre(b3, c3, 0.75), "divida cada parte de cima por 2", 1000, 300, 50, COR)
        raizes(c, t, c3 + 2.4, ("−1 + r{3}", "−1 − r{3}"), W / 2, 790, 96, align="center")
        E.foco(c, t, d3, 0.45, lambda p: E.pilula(c, "dividiu só o −2?", 560, 950, 52, estilo="g", fundo=ERRADO, cor=BR, a=p), sobe=8)
        form(c, t, e3, "−1 ± 2r{3}", 960, 970, 90, ERRADO)
        if t >= e3 + 1.0:
            E.risco(c, 940, 990, 960 + fw("−1 ± 2r{3}", 90) + 20, 900, t, e3 + 1.0, largura=9)
    fase(c, t, C["s13"], 1e9, s13)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a_, b_, c_, d_ = (C[f"s14.{k}"] for k in "abcd")
    E.frase(c, t, C["s14"] + 0.2, ps("o atalho:", "i", 72, CLARO) + ps("divida pelo fator comum antes de tudo", "g", 66, BR), XE, 170, passo=0.1)
    form(c, t, a_, Q3, XE, 340, 100, BR)
    E.foco(c, t, a_ + 0.6, 0.45, lambda p: E.pilula(c, "÷ 2", 1050, 310, 54, estilo="g", fundo=AM, cor="#07070F", a=p), sobe=8)
    form(c, t, a_ + 1.0, Q3b, 1200, 340, 100, AM)
    form(c, t, b_, "0 ÷ 2 = 0", XE, 520, 90, CLARO)
    E.frase(c, t, b_ + 0.8, ps("as raízes", "i", 62, CLARO) + ps("não mudam", "g", 62, BR), 760, 515, passo=0.08)
    form(c, t, c_ - 0.6, "Δ = 16 + 32 = 48", XE, 700, 90, CLARO)
    form(c, t, c_, "→  Δ = 4 + 8 = 12", 1000, 700, 90, AM)
    E.frase(c, t, c_ + 0.8, ps("o delta", "i", 60, CLARO) + ps("encolhe", "g", 60, AM), XE, 800, passo=0.08)
    selo_em(c, t, d_, XE + 40, 935, 38, False)
    E.frase(c, t, d_, ps("a divisão cria fração?", "g", 60, BR) + ps("use a equação como veio", "i", 60, CLARO), XE + 110, 957, passo=0.08)


# ---------------- questão 4 ----------------
def b_questao4(c, t, C, b):
    ka, kb, kc = C["s15.a"], C["s15.b"], C["s15.c"]
    questao(c, t, ka, 4, "raiz dupla")
    E.frase(c, t, kb - 1.0, ps("para que valor de", "i", 76) + ps("k", "g", 80, CC), XE, 380, passo=0.1)
    monta(c, t, [pf("x^2 − 10x + ", kb, COR), pf("k", kb, CC), pf(" = 0", kb, COR)], XE + 40, 580, 120)
    E.frase(c, t, kb + 2.4, ps("tem", "i", 70) + ps("raiz dupla?", "g", 70, COR), XE + 40, 730, passo=0.1)
    E.frase(c, t, kc, ps("e qual é essa raiz?", "i", 70), XE + 40, 880, passo=0.1)
    E.relogio(c, t, C["s16.a"], 1560, 520, 170)


def b_resposta4(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s17.{k}"] for k in "abcde")
    monta(c, t, [pf("x^2 − 10x + ", C["s17"] + 0.1, TINTA2), pf("k", C["s17"] + 0.1, CC), pf(" = 0", C["s17"] + 0.1, TINTA2)], XE, 190, 84)
    delta_caso(c, t, a_, "=", 1000, 160, 46, t1=a_ + 0.4)
    form(c, t, b_, "100 − 4k = 0", XE, 370, 110)
    form(c, t, c_, "k = 25", 1000, 370, 130, CERTO)
    form(c, t, d_, "x =", XE, 600, 110)
    fra_p_em(c, t, d_ + 0.2, [("−", T_), ("b", CB)], [("2", T_), ("a", CA)], XE + fw("x = ", 110) + 70, 565, 90)
    form(c, t, d_ + 1.0, "= f{10}{2} = 5", XE + fw("x = ", 110) + 160, 600, 110, CERTO)
    form(c, t, e_, "x^2 − 10x + 25 = (x − 5)^2", W / 2, 850, 110, align="center")


# ---------------- questão 5 ----------------
def b_questao5(c, t, C, b):
    ka, kb, kc, kd = (C[f"s18.{k}"] for k in "abcd")
    questao(c, t, ka, 5, "o cercado")
    E.retangulo(c, t, kb - 0.4, XE + 60, 330, 640, 330, base="?", altura="?", tl=[kd] * 4)
    E.frase(c, t, kb, ps("contorno:", "i", 60) + ps("26 m de tela", "g", 60, COR), XE + 60, 290, passo=0.08)
    E.foco(c, t, kc, 0.45, lambda p: E.formula(c, "área = 40 m^2", XE + 380, 515, 64, cor=COR, a=p, align="center"))
    E.frase(c, t, kd, ps("quais são as", "i", 80) + ps("medidas?", "g", 80, COR), XE, 860, passo=0.1)
    E.relogio(c, t, C["s19.a"], 1560, 520, 170)


def b_resposta5(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")

    def s20():
        E.retangulo(c, t, C["s20"] + 0.1, XE + 60, 220, 560, 300, base="x" if t >= c0 else "c", altura="13 − x" if t >= c0 else "l",
                    tl=[a0] * 4)
        E.frase(c, t, a0 + 0.3, ps("contorno: 2 comprimentos + 2 larguras = 26", "i", 54), 900, 300, passo=0.07)
        form(c, t, b0, "comprimento + largura = 13", 900, 430, 70, COR)
        E.frase(c, t, c0, ps("largura", "i", 60) + ps("x,", "g", 60, COR) + ps("comprimento", "i", 60) + ps("13 − x", "g", 60, COR), XE, 700, passo=0.08)
        form(c, t, d0, "x(13 − x) = 40", XE, 900, 130)
    fase(c, t, C["s20"], C["s21"] - 0.1, s20)

    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")

    def s21():
        form(c, t, C["s21"] + 0.05, "x(13 − x) = 40", XE, 190, 84, TINTA2)
        nota(c, t, C["s21"] + 0.4, "arrumando, com o a positivo", 900, 180, 52)
        form(c, t, a1, "x^2 − 13x + 40 = 0", XE, 350, 110, COR)
        sp(c, t, b1, b1 + 0.4, 13, 40, 1450, 470, 46, 200)
        par(c, t, b1 + 0.8, b1 + 1.6, (5, 8), 1450, 600, 56, 140)
        E.foco(c, t, c1, 0.5, lambda p: E.pilula(c, "as duas servem: o mesmo cercado", 600, 520, 54, estilo="g", fundo=CERTO, cor=BR, a=p))
        E.retangulo(c, t, d1, XE + 60, 640, 420, 260, base="8 m", altura="5 m", cor=CERTO, tl=[d1 + 0.3] * 4)
        form(c, t, e1, "5 · 8 = 40", 900, 740, 90)
        form(c, t, e1 + 2.0, "5 + 8 + 5 + 8 = 26", 900, 880, 90)
        selo_em(c, t, e1 + 4.0, 1750, 850, 40)
    fase(c, t, C["s21"], C["s22"] - 0.1, s21)

    a2, b2 = C["s22.a"], C["s22.b"]

    def s22():
        E.frase(c, t, C["s22"] + 0.2, ps("repare", "i", 76), XE, 220, passo=0.1)
        E.frase(c, t, a2, ps("o problema já era", "i", 76) + ps("soma e produto", "g", 76, COR) + ps("disfarçado", "i", 76), XE, 420, passo=0.1)
        sp(c, t, b2, b2 + 0.8, 13, 40, W / 2, 620, 64, 320)
        E.frase(c, t, b2 + 0.4, ps("dois lados que somam 13 e multiplicados dão 40", "i", 60, TINTA2), W / 2, 800, "center", passo=0.07)
    fase(c, t, C["s22"], 1e9, s22)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s23.a"], ps("olhe a equação", "g", 72, COR) + ps("antes de calcular", "i", 72)),
             (C["s23.b"], ps("escolha o", "i", 72) + ps("caminho mais curto", "g", 72, COR)),
             (C["s23.c"], ps("passe cada raiz pelo", "i", 72) + ps("filtro do problema", "g", 72, COR)))
    fim_padrao(c, t, C, "s23", "s24", itens, "com isso, você fecha a trilha", "Fatoração e Equação do 2º Grau",
               extra=lambda: (E.frase(c, t, C["s24.b"], ps("a próxima trilha:", "i", 70) + ps("funções", "g", 74, COR), XE, 580, passo=0.1),
                              E.frase(c, t, C["s24.c"], ps("começa pelo", "i", 64) + ps("plano cartesiano", "g", 64, COR), XE, 720, passo=0.08),
                              E.frase(c, t, C["s24.c"] + 1.2, ps("marcar e ler pontos, como num mapa", "i", 54, TINTA2), XE, 810, passo=0.07)))


BLOCKS = dict(gancho=b_gancho, mapa=b_mapa, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
