"""Visual — Estudativo · MAT-FAT-012: problemas de equação do 2º grau.
O livro aberto com duas páginas seguidas (produto 156), montado pelos quatro passos, com a pílula "passo n" no alto (como
em MAT-EQU-013); as raízes 12 e −13 passam pelo filtro do problema; a bola chutada, com o gráfico de h = 20t − 5t² no plano
e as raízes t = 0 e t = 4 no chão; o erro de responder com a primeira raiz; no palco, o atalho dos quadrados vizinhos;
o terreno retangular de área 150.

Convenções da trilha (as de MAT-FAT-004 a 011: coeficientes coloridos, delta_pilula, pm, raizes, evid, regra_zero).
Nova: FILTRO DO PROBLEMA = cada raiz numa pílula; a que o problema descarta fica vermelha, riscada, com o motivo ao lado;
a que serve fica verde (filtro).
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-012_problemas_equacao_2grau.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("paginas", "bola", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"

# as contas da aula
assert 1 * 1 - 4 * 1 * (-156) == 625 == 25 ** 2 and (-1 + 25) // 2 == 12 and (-1 - 25) // 2 == -13
assert 12 * 13 == 156 == (-13) * (-12) and 12 * 12 + 12 == 156
h = lambda t: 20 * t - 5 * t * t
assert h(0) == 0 == h(4) and 20 * 4 == 80 == 5 * 16 and max(h(k / 10) for k in range(41)) == 20
assert 12 * 12 == 144 < 156 < 169 == 13 * 13
assert 5 * 5 - 4 * 1 * (-150) == 625 and (-5 + 25) // 2 == 10 and (-5 - 25) // 2 == -15 and 10 * 15 == 150 and 10 * (10 + 5) == 150
del h


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


def coefs(c, t, t0, vals, cx, cy, size=46, gap=260, dt=0.0):
    for k, (letra, v) in enumerate(zip("abc", vals)):
        coef(c, t, t0 + k * dt, letra, v, cx + (k - 1) * gap, cy, size)


def etiqueta(c, t, t0, t1, n):
    """pílula "passo n" no alto (como em MAT-EQU-013)"""
    fase(c, t, t0, t1, lambda: E.foco(c, t, t0, 0.4, lambda q: E.pilula(c, f"passo {n}", 1650, 110, 46, estilo="b", a=q), sobe=6))


def filtro(c, t, t0, s, x, y, size, ok, motivo=None, t1=None, align="left"):
    """filtro do problema (convenção da trilha): a raiz numa pílula; ok = verde; descartada = vermelha, riscada, motivo ao lado"""
    t1 = t1 if t1 is not None else t0 + 0.6
    w = E.larg(s, "g", size) + size * 1.1
    cx = x + w / 2 if align == "left" else x
    fundo = CERTO if ok else (TINTA2 if t < t1 else ERRADO)
    E.foco(c, t, t0, 0.45, lambda p: E.pilula(c, s, cx, y, size, estilo="g", fundo=fundo, cor=BR, a=p), sobe=8)
    if not ok and t >= t1:
        E.risco(c, cx - w / 2 - 10, y + size * 0.6, cx + w / 2 + 10, y - size * 0.6, t, t1, ERRADO, max(5, size * 0.08))
    if motivo:
        E.frase(c, t, t1 + 0.2, ps(motivo, "i", 56, CERTO if ok else ERRADO), cx + w / 2 + 40, y + 18, passo=0.07)


def livro(c, cx, cy, e, d, a=1.0, cor_e=None, cor_d=None, w=230, h=290):
    """livro aberto: duas páginas com os números e e d"""
    if a <= 0:
        return
    for k, (s, cr) in enumerate(((e, cor_e), (d, cor_d))):
        x = cx - w if k == 0 else cx
        M.rrect(c, x + 6, cy - h / 2 + 8, w, h, 16, "#000000", 0.08 * a)
        M.rrect(c, x, cy - h / 2, w, h, 16, BR, a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, cy - h / 2, w, h), 16, 16), M.paint(TINTA, a, stroke=4))
        for i in range(4):
            yy = cy - h / 2 + 50 + i * 34
            M.line(c, x + 30, yy, x + w - 30, yy, FIO, a, 4)
        E.formula(c, s, x + w / 2, cy + h / 2 - 34, 64, cor=cr or COR, a=a, align="center")
    M.line(c, cx, cy - h / 2, cx, cy + h / 2, TINTA, a, 5)


def livro_em(c, t, t0, cx, cy, e, d, cor_e=None, cor_d=None, w=230, h=290):
    E.foco(c, t, t0, 0.5, lambda p: livro(c, cx, cy, e, d, p, cor_e, cor_d, w, h))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s01.{k}"] for k in "abcd")

    def conta():
        livro_em(c, t, a_, W / 2, 360, "?", "?")
        E.frase(c, t, a_ + 0.6, ps("duas páginas seguidas", "i", 64, TINTA2), W / 2, 600, "center", passo=0.08)
        form(c, t, b_, "? · ? = 156", W / 2, 760, 130, COR, align="center")
        E.frase(c, t, c_, ps("que páginas são?", "g", 76), W / 2, 900, "center", passo=0.1)
        E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "duas respostas: uma não serve", W / 2, 1010, 50, estilo="g", fundo=ERRADO, cor=BR, a=p))
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2 = C["s02.a"], C["s02.b"]
    E.frase(c, t, a2, ps("até o fim desta aula, você monta", "i", 80), XE, 300, passo=0.12)
    E.frase(c, t, a2 + 1.2, ps("equações do 2º grau", "g", 100, COR), XE, 440, passo=0.13)
    E.frase(c, t, a2 + 2.0, ps("a partir de problemas", "i", 80), XE, 560, passo=0.12)
    E.frase(c, t, b2, ps("e sabe qual raiz", "i", 80) + ps("jogar fora", "g", 80, ERRADO), XE, 760, passo=0.12)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_ = C["s03.a"], C["s03.b"]
    E.frase(c, t, a_, ps("os quatro passos", "g", 70, COR) + ps("para montar uma equação", "i", 70), XE, 180, passo=0.1)
    passos_ = ("o que você não sabe vira x", "cada informação vira conta", "ache o que é igual a quê", "resolva e responda")
    for k, txt in enumerate(passos_):
        tk = entre(a_, b_, 0.18 + 0.2 * k)
        yy = 320 + k * 115
        E.foco(c, t, tk, 0.45, lambda p, k=k, yy=yy: num_bola(c, str(k + 1), XE + 40, yy - 22, 36, 46, p))
        E.frase(c, t, tk, ps(txt, "i", 60), XE + 110, yy, passo=0.07)
    E.frase(c, t, b_, ps("e a", "i", 66) + ps("fórmula de Bhaskara", "g", 66, COR), XE, 830, passo=0.1)
    bhaskara_f(c, t, b_ + 1.0, 1150, 850, 84)
    E.frase(c, t, C["s04"] - 2.2, ps("faltou alguma? procure no canal", "i", 52, TINTA2), 1150, 1010, passo=0.08)


# ---------------- as páginas ----------------
def b_paginas(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")

    def s04():
        etiqueta(c, t, a4, b4 - 0.1, 1)
        etiqueta(c, t, b4, c4 - 0.1, 2)
        etiqueta(c, t, c4, 1e9, 3)
        livro(c, 560, 420, "x" if t >= a4 else "?", "x + 1" if t >= b4 else "?", ep(t, C["s04"] + 0.1, 0.5), w=260, h=320)
        E.frase(c, t, a4 + 0.3, ps("a primeira:", "i", 60) + ps("x", "g", 64, COR), 1000, 330, passo=0.08)
        E.frase(c, t, b4 + 0.3, ps("a seguinte:", "i", 60) + ps("x + 1", "g", 64, COR), 1000, 450, passo=0.08)
        E.frase(c, t, c4 + 0.3, ps("o produto das duas:", "i", 60) + ps("156", "g", 64, COR), 1000, 570, passo=0.08)
        form(c, t, d4, "x(x + 1) = 156", W / 2, 860, 140, align="center")
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)

    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]

    def s05():
        etiqueta(c, t, C["s05"], 1e9, 3)
        form(c, t, C["s05"] + 0.1, "x(x + 1) = 156", XE, 240, 96, TINTA2)
        form(c, t, entre(C["s05"], a5, 0.6), "x^2 + x = 156", XE, 400, 100)
        nota(c, t, entre(C["s05"], a5, 0.6) + 0.3, "distributiva", 1000, 390, 54, COR)
        nos_dois(c, t, a5 - 0.4, "x^2 + x = 156", "− 156", XE, 400, 100)
        form(c, t, a5, "x^2 + x − 156 = 0", XE, 620, 120, COR)
        E.foco(c, t, b5, 0.45, lambda p: E.pilula(c, "x²: do 2º grau", 1450, 585, 54, estilo="g", fundo=TINTA, cor=BR, a=p), sobe=8)
        coefs(c, t, c5, ("1", "1", "−156"), W / 2, 850, 52, 320, dt=0.6)
    fase(c, t, C["s05"], C["s06"] - 0.1, s05)

    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")

    def s06():
        form(c, t, C["s06"] + 0.05, "x^2 + x − 156 = 0", XE, 190, 84, TINTA2)
        form(c, t, a6, "Δ = 1 + 624 = 625", XE, 360, 100)
        delta_pilula(c, t, a6 + 1.5, "625", 1450, 330, 56)
        form(c, t, b6, "r{625} = 25", XE, 530, 100)
        pm(c, t, c6, "+", "f{−1 + 25}{2} = f{24}{2}", XE, 730, 96, t1=entre(c6, d6, 0.75), final="= 12")
        pm(c, t, d6, "−", "f{−1 − 25}{2} = f{−26}{2}", XE, 920, 96, t1=d6 + 4.5, final="= −13")
    fase(c, t, C["s06"], C["s07"] - 0.1, s06)

    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")

    def s07():
        etiqueta(c, t, C["s07"], 1e9, 4)
        E.frase(c, t, a7, ps("responda o que foi", "i", 70) + ps("pedido", "g", 70, COR), XE, 190, passo=0.1)
        filtro(c, t, a7 + 0.6, "x = −13", XE, 360, 64, False, "página −13 não existe", t1=b7)
        filtro(c, t, c7, "x = 12", XE, 520, 64, True, "páginas 12 e 13")
        livro_em(c, t, c7 + 0.6, 1450, 760, "12", "13", CERTO, CERTO, 200, 250)
        monta(c, t, [pf("12 · 13", d7), pf(" = 156", d7 + 0.8, CERTO)], XE, 800, 110)
        selo_em(c, t, d7 + 1.6, XE + 700, 765, 44)
    fase(c, t, C["s07"], C["s08"] - 0.1, s07)

    a8, b8 = C["s08.a"], C["s08.b"]

    def s08():
        nota(c, t, C["s08"] + 0.2, "repare", XE, 200, 64)
        form(c, t, a8, "(−13) · (−12) = 156", W / 2, 450, 130, align="center")
        nota(c, t, a8 + 2.0, "para a conta, a raiz serve", W / 2, 580, 60, align="center")
        E.foco(c, t, b8, 0.5, lambda p: E.pilula(c, "quem descarta é o problema, não a conta", W / 2, 800, 64, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    fase(c, t, C["s08"], 1e9, s08)


# ---------------- a bola ----------------
def b_bola(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    t0 = C["s09"]
    P = E.plano(c, t, t0 + 0.4, 1040, 250, 760, 560, 0, 4.6, 0, 22, passo=1, passo_y=5, nomes=("t", "h"), size=38)
    hf = lambda x: 20 * x - 5 * x * x
    E.curva(c, t, a9 + 0.3, P, hf, 0, 4, d=1.6)
    fim1 = C["s10"] - 0.1
    if t < fim1 + 0.4:
        def s09():
            E.frase(c, t, t0 + 0.2, ps("2º problema:", "g", 66, COR) + ps("a bola chutada", "i", 66), XE, 190, passo=0.1)
            form(c, t, a9, "h = 20t − 5t^2", XE, 380, 110)
            nota(c, t, a9 + 0.6, "h: altura, em metros", XE, 480, 52)
            nota(c, t, b9, "t: tempo em segundos, desde o chute", XE, 560, 52)
            E.frase(c, t, c9, ps("quando ela volta ao", "i", 66) + ps("chão?", "g", 66, COR), XE, 760, passo=0.1)
        E.saida(c, t, fim1, s09)
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    fim2 = C["s11"] - 0.1
    if C["s10"] - 0.01 <= t < fim2 + 0.4:
        def s10():
            form(c, t, a0, "no chão: h = 0", XE, 220, 84, COR)
            form(c, t, b0, "20t − 5t^2 = 0", XE, 400, 110)
            E.foco(c, t, c0, 0.45, lambda p: E.pilula(c, "incompleta: sem número sozinho", XE + 380, 520, 46, estilo="g", fundo=TINTA, cor=BR, a=p), sobe=8)
            realce(c, t, d0, "20t − 5t^2 = 0", "20t", XE, 400, 110)
            realce(c, t, d0, "20t − 5t^2 = 0", "5t^2", XE, 400, 110)
            nota(c, t, d0 + 0.3, "5t em evidência", XE, 640, 52, COR)
            evid(c, t, e0, "5t", "4 − t", XE, 800, 120, t1=e0 + 0.6)
            form(c, t, e0 + 1.0, " = 0", XE + fw("5t(4 − t)", 120), 800, 120)
        E.saida(c, t, fim2, s10)
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    if t >= C["s11"]:
        form(c, t, C["s11"] + 0.05, "5t(4 − t) = 0", XE, 220, 84, TINTA2)
        raizes(c, t, a1, ("0", "4"), XE, 350, 96, var="t", t1=a1 + 0.8)
        E.ponto(c, t, a1 + 0.2, P, 0, 0, None, cor=ERRADO if t >= b1 else TINTA2, r=16)
        E.ponto(c, t, a1 + 1.0, P, 4, 0, None, cor=CERTO, r=16)
        filtro(c, t, b1, "t = 0", XE, 470, 50, False, "a bola está saindo do pé", t1=b1 + 1.0)
        filtro(c, t, c1, "t = 4", XE, 580, 50, True, "4 segundos")
        form(c, t, d1, "20 · 4 = 80", XE, 740, 84)
        form(c, t, e1, "5 · 16 = 80", XE, 850, 84)
        form(c, t, e1 + 1.6, "80 − 80 = 0", XE, 960, 84, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s12.{k}"] for k in "abcd")
    E.frase(c, t, C["s12"] + 0.3, ps("o erro mais comum:", "g", 76, ERRADO) + ps("a primeira raiz, sem voltar ao texto", "i", 70), XE, 170, passo=0.1)
    filtro(c, t, b_, "t = 0", XE, 340, 56, False, "a bola nem saiu do chão", t1=b_ + 0.8)
    filtro(c, t, c_, "x = −13", XE, 480, 56, False, "a página nem existe", t1=c_ + 0.6)
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "toda raiz passa pelo filtro do problema", W / 2, 660, 66, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    E.frase(c, t, d_ + 2.0, ps("página, medida e quantidade:", "i", 60) + ps("não são negativas", "g", 60, COR), XE, 820, passo=0.08)
    E.frase(c, t, d_ + 4.6, ps("o instante zero é a", "i", 60) + ps("partida", "g", 60, COR), XE, 930, passo=0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")

    def s13():
        E.frase(c, t, C["s13"] + 0.2, ps("o atalho dos", "i", 72, CLARO) + ps("números seguidos", "g", 72, BR), XE, 170, passo=0.1)
        E.frase(c, t, a3, ps("procure perto da raiz do produto", "i", 66, CLARO), XE, 300, passo=0.08)
        form(c, t, b3, "12 · 12 = 144", XE, 470, 100, CLARO)
        form(c, t, c3, "13 · 13 = 169", XE, 640, 100, CLARO)
        form(c, t, entre(c3, d3, 0.5), "144 < 156 < 169", 1050, 555, 90, AM)
        form(c, t, d3, "12 · 13 = 156", XE, 860, 120, AM)
        selo_em(c, t, d3 + 1.2, XE + 900, 820, 44)
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)

    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]

    def s14():
        E.frase(c, t, C["s14"] + 0.2, ps("funciona porque", "i", 76, CLARO), XE, 180, passo=0.1)
        E.frase(c, t, a4, ps("números seguidos são", "i", 66, CLARO) + ps("quase iguais", "g", 66, BR), XE, 330, passo=0.08)
        E.frase(c, t, a4 + 1.6, ps("o produto fica entre os quadrados de cada um", "i", 60, CLARO), XE, 430, passo=0.07)
        selo_em(c, t, b4, XE + 40, 600, 38, False)
        E.frase(c, t, b4, ps("resposta", "i", 64, CLARO) + ps("não inteira", "g", 64, BR), XE + 110, 622, passo=0.08)
        selo_em(c, t, c4, XE + 40, 740, 38, False)
        E.frase(c, t, c4, ps("números", "i", 64, CLARO) + ps("não vizinhos", "g", 64, BR), XE + 110, 762, passo=0.08)
        E.foco(c, t, c4 + 1.4, 0.5, lambda p: E.pilula(c, "aí, monte a equação", W / 2, 920, 60, estilo="g", fundo=AM, cor="#07070F", a=p))
    fase(c, t, C["s14"], 1e9, s14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s15.{k}"] for k in "abcd")
    E.frase(c, t, C["s15"] + 0.3, ps("hora de testar:", "i", 72, COR) + ps("o terreno", "g", 72), XE, 170, passo=0.1)
    E.retangulo(c, t, a_, XE + 60, 330, 640, 360, base="x + 5", altura="x", tl=[a_ + 0.6] * 4)
    E.frase(c, t, a_ + 0.4, ps("comprimento = largura + 5", "i", 54, TINTA2), XE + 60, 290, passo=0.07)
    E.foco(c, t, b_, 0.45, lambda p: E.formula(c, "área = 150 m^2", XE + 380, 530, 64, cor=COR, a=p, align="center"))
    form(c, t, c_, "área = comprimento · largura", XE, 870, 76, TINTA2)
    E.frase(c, t, d_, ps("quais são as", "i", 80) + ps("medidas?", "g", 80, COR), XE, 990, passo=0.1)
    E.relogio(c, t, C["s16.a"], 1560, 330, 140)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]

    def s17():
        E.frase(c, t, a7, ps("largura", "i", 64) + ps("x,", "g", 64, COR) + ps("comprimento", "i", 64) + ps("x + 5", "g", 64, COR), XE, 220, passo=0.08)
        form(c, t, b7, "x(x + 5) = 150", XE, 430, 120)
        form(c, t, c7, "x^2 + 5x − 150 = 0", XE, 680, 130, COR)
        coefs(c, t, c7 + 1.5, ("1", "5", "−150"), W / 2, 880, 48, 320)
    fase(c, t, C["s17"], C["s18"] - 0.1, s17)

    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]

    def s18():
        form(c, t, C["s18"] + 0.05, "x^2 + 5x − 150 = 0", XE, 190, 84, TINTA2)
        form(c, t, a8, "Δ = 25 + 600 = 625", XE, 370, 100)
        form(c, t, a8 + 3.0, "r{625} = 25", 1150, 370, 90, TINTA2)
        pm(c, t, b8, "+", "f{−5 + 25}{2} = f{20}{2}", XE, 600, 96, t1=b8 + 3.5, final="= 10")
        pm(c, t, c8, "−", "f{−5 − 25}{2} = f{−30}{2}", XE, 800, 96, t1=c8 + 4.2, final="= −15")
    fase(c, t, C["s18"], C["s19"] - 0.1, s18)

    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")

    def s19():
        filtro(c, t, C["s19"] + 0.1, "x = −15", XE, 220, 56, False, "largura negativa não existe", t1=a9 + 0.3)
        filtro(c, t, b9 - 0.2, "x = 10", XE, 350, 56, True)
        E.retangulo(c, t, b9, XE + 60, 470, 560, 315, base="15 m", altura="10 m", cor=CERTO, tl=[b9 + 0.4] * 4)
        E.frase(c, t, b9 + 0.6, ps("largura", "i", 64) + ps("10 m,", "g", 64, CERTO), 920, 560, passo=0.08)
        E.frase(c, t, b9 + 1.2, ps("comprimento", "i", 64) + ps("15 m", "g", 64, CERTO), 920, 660, passo=0.08)
        monta(c, t, [pf("10 · 15", c9), pf(" = 150", c9 + 0.8, CERTO)], 920, 800, 96)
        selo_em(c, t, c9 + 1.5, 1650, 770, 40)
        E.foco(c, t, d9, 0.5, lambda p: E.pilula(c, "só 10? faltou o comprimento", 1300, 960, 52, estilo="g", fundo=ERRADO, cor=BR, a=p))
    fase(c, t, C["s19"], 1e9, s19)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s20.a"], ps("monte com os", "i", 72) + ps("quatro passos", "g", 72, COR)),
             (C["s20.b"], ps("resolva", "g", 72, COR)),
             (C["s20.c"], ps("passe cada raiz pelo", "i", 72) + ps("filtro do problema", "g", 72, COR)))
    fim_padrao(c, t, C, "s20", "s21", itens, "próxima aula: equações que", "não parecem do 2º grau",
               extra=lambda: (form(c, t, C["s21.b"], "x^4 − 13x^2 + 36 = 0", XE, 590, 100),
                              E.frase(c, t, C["s21.c"], ps("uma", "i", 76) + ps("troca de letra", "g", 80, COR) + ps("resolve tudo", "i", 76), XE, 760, passo=0.12)))


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, paginas=b_paginas, bola=b_bola, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
