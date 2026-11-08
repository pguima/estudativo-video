"""Visual — Estudativo · MAT-FAT-011: soma e produto, raízes de cabeça.
x² − 7x + 12 = 0 com o par 3 e 4; (x − 3)(x − 4) aberto pelo chuveirinho; a regra com a = 1 (soma = −b, produto = c);
os sinais pelo produto; x² + 5x + 6 = (x + 2)(x + 3) com o teste com 10; a equação de raízes 2 e 5; o erro de não trocar o
sinal da soma; no palco, o atalho de listar os pares do produto.

Convenções da trilha (as de MAT-FAT-004 a 010: coeficientes coloridos, chuveiro, regra_zero, raizes). Nova:
SOMA E PRODUTO = pílula "soma 7" na cor do b e "produto 12" na cor do c (sp), e as duas raízes procuradas como duas
esferas que começam com "?" e ganham os números na fala (par).
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-011_soma_e_produto.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("origem", "regra", "fatorar", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"


def _raizes(b, c):
    return sorted(x for x in range(-50, 51) if x * x + b * x + c == 0)


# as contas da aula
assert _raizes(-7, 12) == [3, 4] and 3 + 4 == 7 and 3 * 4 == 12
assert all((x - 3) * (x - 4) == x * x - 7 * x + 12 for x in range(-5, 6))
assert _raizes(5, 6) == [-3, -2] and all((x + 2) * (x + 3) == x * x + 5 * x + 6 for x in range(-5, 6))
assert 100 + 50 + 6 == 156 == 12 * 13
assert _raizes(-7, 10) == [2, 5] and 4 - 14 + 10 == 0 and 4 + 10 + 6 == 20
assert [p for p in range(1, 13) if 12 % p == 0 and p <= 12 // p] == [1, 2, 3] and 1 + 12 == 13 and 2 + 6 == 8
assert _raizes(-2, -1) == []
assert _raizes(2, -15) == [-5, 3] and -1 + 4 == 3 and -1 * 4 == -4 and _raizes(-3, -4) == [-1, 4]


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


def sp(c, t, ts, tp, S, P, cx, cy, size=56, gap=300, escuro=False):
    """soma e produto (convenção da trilha): pílula da soma na cor do b e do produto na cor do c"""
    cb, cc = (CB_L, CC_L) if escuro else (CB, CC)
    tinta = "#07070F" if escuro else BR
    E.foco(c, t, ts, 0.45, lambda p: E.pilula(c, f"soma {S}", cx - gap, cy, size, estilo="g", fundo=cb, cor=tinta, a=p), sobe=8)
    E.foco(c, t, tp, 0.45, lambda p: E.pilula(c, f"produto {P}", cx + gap, cy, size, estilo="g", fundo=cc, cor=tinta, a=p), sobe=8)


def par(c, t, t0, t1, v1, v2, cx, cy, r=78, gap=120, cor=None, t2=None):
    """as duas raízes procuradas: esferas com "?" (t0) que ganham os números (t1; a segunda em t2)"""
    t2 = t2 if t2 is not None else t1 + 0.3
    for k, (v, tv) in enumerate(((v1, t1), (v2, t2))):
        x = cx + (k * 2 - 1) * gap
        q = ep(t, t0 + 0.15 * k, 0.5)
        if q <= 0:
            continue
        E.bola(c, x, cy, r * ease_back(min(1.0, q)), cor, q)
        mostra = ep(t, tv, 0.35)
        if mostra < 1:
            centro(c, "?", x, cy + r * 0.38, r * 1.0, "g", BR, q * (1 - mostra))
        if mostra > 0:
            centro(c, str(v), x, cy + r * 0.36, r * (0.95 if len(str(v)) < 3 else 0.75), "g", BR, mostra)


# ---------------- gancho ----------------
Q1 = "x^2 − 7x + 12 = 0"


def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s01.{k}"] for k in "abcd")

    def conta():
        form(c, t, a_, Q1, W / 2, 300, 140, align="center")
        sp(c, t, b_, entre(b_, c_, 0.5), 7, 12, W / 2, 450, 60, 320)
        par(c, t, b_ + 0.3, c_, 3, 4, W / 2, 660, 90, 140)
        form(c, t, c_ + 0.5, "3 + 4 = 7", XE + 60, 690, 84, CB)
        form(c, t, c_ + 0.8, "3 · 4 = 12", 1300, 690, 84, CC)
        raizes(c, t, d_, ("3", "4"), W / 2, 880, 100, align="center")
        E.foco(c, t, d_ + 0.6, 0.45, lambda p: E.pilula(c, "sem delta e sem fórmula", W / 2, 990, 52, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]
    E.frase(c, t, a2, ps("até o fim desta aula, você", "i", 84), XE, 240, passo=0.12)
    for k, (tk, partes) in enumerate(((a2 + 1.0, ps("acha raízes", "i", 84) + ps("de cabeça", "g", 84, COR)),
                                      (b2, ps("fatora", "g", 84, COR) + ps("o trinômio", "i", 84)),
                                      (c2, ps("monta a equação", "g", 84, COR) + ps("a partir das raízes", "i", 84)))):
        yy = 440 + k * 190
        E.foco(c, t, tk, 0.45, lambda p, k=k, yy=yy: num_bola(c, str(k + 1), XE + 50, yy - 28, 48, 58, p))
        E.frase(c, t, tk + 0.1, partes, XE + 140, yy, passo=0.12)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_ = C["s03.a"], C["s03.b"]
    E.frase(c, t, C["s03"] + 0.2, ps("você vai usar", "i", 84), XE, 180)
    E.foco(c, t, a_, 0.45, lambda p: num_bola(c, "1", XE + 40, 330, 40, 50, p))
    E.frase(c, t, a_, ps("o chuveirinho:", "g", 64, COR) + ps("cada termo multiplica cada termo do outro", "i", 60), XE + 110, 352, passo=0.08)
    S = "(x + 1)(x + 2)"
    form(c, t, a_ + 1.5, S, XE + 120, 590, 100)
    chuveiro(c, t, (a_ + 2.0, a_ + 2.3, a_ + 2.6, a_ + 2.9), S, 590, 100, COR, "left", XE + 120, 50)
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "2", XE + 40, 780, 40, 50, p))
    E.frase(c, t, b_, ps("Bhaskara,", "g", 64, COR) + ps("para quando o macete não servir", "i", 64), XE + 110, 802, passo=0.08)
    bhaskara_f(c, t, b_ + 1.2, 1150, 600, 84)
    E.frase(c, t, C["s04"] - 2.2, ps("faltou alguma? procure no canal", "i", 52, TINTA2), 1150, 1010, passo=0.08)


# ---------------- de onde vem ----------------
def b_origem(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    S = "(x − 3)(x − 4)"

    def s04():
        nota(c, t, C["s04"] + 0.2, "de onde vem isso?", XE, 190, 64)
        form(c, t, a4, S, W / 2, 420, 130, align="center")
        chuveiro(c, t, (b4, b4 + 0.8, b4 + 1.6, b4 + 2.4), S, 420, 130, COR, "center", W / 2, 70)
        monta(c, t, [pf("= x^2", b4 + 0.2), pf(" − 4x", b4 + 1.0), pf(" − 3x", b4 + 1.8), pf(" + 12", b4 + 2.6)], W / 2, 680, 110, "center")
        form(c, t, c4, "= x^2 − 7x + 12", W / 2, 880, 120, COR, align="center")
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)

    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    F = "(x − 3)(x − 4) = x^2 − 7x + 12"

    def s05():
        form(c, t, C["s05"] + 0.05, F, W / 2, 260, 100, align="center")
        x7 = trecho_x(F, "7", W / 2, 100, "center")
        x12 = trecho_x(F, "12", W / 2, 100, "center")
        realce(c, t, a5, F, "7", W / 2, 260, 100, CB, "center")
        form(c, t, a5 + 0.3, "7 = 3 + 4", x7[0] + x7[1] / 2, 400, 80, CB, align="center")
        realce(c, t, b5, F, "12", W / 2, 260, 100, CC, "center")
        form(c, t, b5 + 0.3, "12 = 3 · 4", x12[0] + x12[1] / 2, 510, 80, CC, align="center")
        raizes(c, t, c5, ("3", "4"), W / 2, 680, 120, align="center")
        regra_zero(c, t, d5, W / 2, 860, 54)
    fase(c, t, C["s05"], 1e9, s05)


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    a_, b_, c_ = C["s06.a"], C["s06.b"], C["s06.c"]
    E.frase(c, t, C["s06"] + 0.2, ps("a regra, com", "i", 76), XE, 190, passo=0.1)
    monta(c, t, [pf("a", C["s06"] + 0.8, CA), pf(" = 1", C["s06"] + 0.8)], XE + 400, 190, 76)
    monta(c, t, [pf("soma das raízes = −", a_), pf("b", a_, CB)], XE, 380, 110)
    nota(c, t, a_ + 1.2, "o b com o sinal trocado", XE + 620, 470, 52, CB)
    monta(c, t, [pf("produto das raízes = ", b_), pf("c", b_, CC)], XE, 630, 110)
    form(c, t, entre(b_, c_, 0.4), "x^2 − 7x + 12:  soma 7, produto 12", XE, 790, 76, TINTA2)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "a diferente de 1? divida a equação inteira pelo a antes", W / 2, 950, 54, estilo="g", fundo=TINTA, cor=BR, a=p))


# ---------------- sinais ----------------
Q2 = "x^2 + 5x + 6 = 0"


def b_sinais(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")

    def s07():
        E.frase(c, t, C["s07"] + 0.2, ps("com sinais, comece", "i", 76) + ps("pelo produto", "g", 76, CC), XE, 200, passo=0.1)
        for k, (tk, rot, fundo, txt, sinais) in enumerate(((b7, "produto positivo", CC, "mesmo sinal", "+ +   ou   − −"),
                                                          (c7, "produto negativo", CC, "sinais contrários", "+ −"),
                                                          (d7, "a soma", CB, "diz qual sinal ganha", ""))):
            yy = 400 + k * 190
            E.foco(c, t, tk, 0.45, lambda p, rot=rot, fundo=fundo, yy=yy: E.pilula(c, rot, XE + 260, yy, 54, estilo="g", fundo=fundo, cor=BR, a=p), sobe=8)
            pa = ep(t, tk + 0.3, 0.4)
            if pa > 0:
                M.arrow(c, XE + 540, yy, XE + 640, yy, TINTA2, pa, 5, 16, pa)
            E.frase(c, t, tk + 0.4, ps(txt, "g", 64, TINTA), XE + 680, yy + 22, passo=0.08)
            if sinais:
                form(c, t, tk + 0.8, sinais, 1450, yy + 22, 70, TINTA2)
    fase(c, t, C["s07"], C["s08"] - 0.1, s07)

    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")

    def s08():
        form(c, t, a8, Q2, W / 2, 230, 120, align="center")
        sp(c, t, b8, b8 + 0.6, "−5", 6, W / 2, 380, 56, 300)
        E.frase(c, t, c8, ps("produto positivo e soma negativa:", "i", 60) + ps("as duas negativas", "g", 60, COR), W / 2, 520, "center", passo=0.08)
        par(c, t, c8 + 0.6, d8, "−2", "−3", W / 2, 690, 80, 130, t2=d8 + 0.4)
        form(c, t, d8 + 1.2, "−2 + (−3) = −5", XE, 890, 80, CB)
        form(c, t, d8 + 2.4, "(−2) · (−3) = 6", 1150, 890, 80, CC)
    fase(c, t, C["s08"], 1e9, s08)


# ---------------- fatorar ----------------
def b_fatorar(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]

    def s09():
        nota(c, t, C["s09"] + 0.2, "raízes −2 e −3", XE, 190, 60, COR)
        E.foco(c, t, a9, 0.5, lambda p: E.pilula(c, "cada raiz vira um parêntese: (x − raiz)", W / 2, 330, 58, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
        form(c, t, entre(a9, b9, 0.6), "x − (−2)", XE, 530, 110)
        form(c, t, b9, "= x + 2", XE + fw("x − (−2) ", 110), 530, 110, COR)
        form(c, t, b9 + 0.6, "x − (−3) = x + 3", 1050, 530, 90, TINTA2)
        form(c, t, c9, "x^2 + 5x + 6 = (x + 2)(x + 3)", W / 2, 780, 120, CERTO, align="center")
    fase(c, t, C["s09"], C["s10"] - 0.1, s09)

    a0, b0 = C["s10.a"], C["s10.b"]

    def s10():
        form(c, t, C["s10"] + 0.05, "x^2 + 5x + 6 = (x + 2)(x + 3)", W / 2, 230, 96, align="center")
        nota(c, t, C["s10"] + 0.3, "teste com 10", XE, 380, 60)
        monta(c, t, [pf("100 + 50 + 6", a0), pf(" = 156", a0 + 1.4, COR)], XE, 540, 110)
        monta(c, t, [pf("12 · 13", b0), pf(" = 156", b0 + 0.8, COR)], XE, 720, 110)
        selo_em(c, t, b0 + 1.5, 1000, 680, 46)
    fase(c, t, C["s10"], 1e9, s10)


# ---------------- montar ----------------
def b_montar(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s11.{k}"] for k in "abcd")
    E.frase(c, t, C["s11"] + 0.2, ps("o caminho de volta:", "i", 72) + ps("raízes 2 e 5", "g", 72, COR), XE, 190, passo=0.1)
    par(c, t, a_, a_ + 0.3, 2, 5, W / 2, 360, 72, 110)
    sp(c, t, b_, b_ + 0.6, 7, 10, W / 2, 530, 56, 300)
    monta(c, t, [pf("x^2 ", c_), pf("− 7", c_, CB), pf("x ", c_), pf("+ 10", c_, CC), pf(" = 0", c_)], W / 2, 720, 120, "center")
    monta(c, t, [pf("x = 2:  ", d_, CERTO), pf("4 − 14 + 10 = 0", d_ + 0.4)], XE, 920, 84)
    selo_em(c, t, d_ + 1.5, 1100, 890, 40)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s12.{k}"] for k in "abcde")
    E.frase(c, t, C["s12"] + 0.3, ps("o erro mais comum:", "g", 76, ERRADO) + ps("não trocar o sinal da soma", "i", 76), XE, 170, passo=0.1)
    form(c, t, a_ + 1.5, Q2, XE, 340, 110)
    E.foco(c, t, b_, 0.45, lambda p: E.pilula(c, "soma +5 ?", 1300, 310, 56, estilo="g", fundo=ERRADO, cor=BR, a=p), sobe=8)
    par(c, t, b_ + 0.2, c_, 2, 3, 560, 540, 70, 110, ERRADO, t2=c_ + 0.3)
    monta(c, t, [pf("x = 2:  ", d_), pf("4 + 10 + 6 = 20", d_ + 0.4, ERRADO)], XE, 750, 90)
    E.frase(c, t, entre(d_, e_, 0.6), ps("não deu zero", "g", 64, ERRADO), 1150, 745, passo=0.08)
    E.foco(c, t, e_, 0.5, lambda p: E.pilula(c, "soma = −b: aqui, −5", W / 2, 930, 64, estilo="g", fundo=CB, cor=BR, a=p))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]

    def s13():
        E.frase(c, t, C["s13"] + 0.2, ps("o atalho de prova:", "i", 72, CLARO) + ps("liste os pares do produto", "g", 70, BR), XE, 170, passo=0.1)
        form(c, t, a3 + 1.4, Q1, XE, 330, 100, BR)
        sp(c, t, a3 + 1.8, a3 + 1.8, 7, 12, 1450, 300, 46, 200, escuro=True)
        for k, (p1, p2, sm) in enumerate(((1, 12, 13), (2, 6, 8), (3, 4, 7))):
            yy = 500 + k * 150
            ti = b3 + k * 0.9
            form(c, t, ti, f"{p1} · {p2} = 12", XE + 60, yy, 96, BR)
            form(c, t, c3 + 0.2 * k, f"soma {sm}", XE + 760, yy, 96, AM if sm == 7 else CLARO)
            selo_em(c, t, c3 + 0.2 * k + 0.3, XE + 1200, yy - 34, 36, sm == 7)
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)

    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")

    def s14():
        E.frase(c, t, C["s14"] + 0.2, ps("funciona porque", "i", 76, CLARO), XE, 180, passo=0.1)
        E.frase(c, t, a4, ps("o produto tem", "i", 64, CLARO) + ps("poucos pares", "g", 64, AM) + ps("de inteiros; a soma tem", "i", 64, CLARO)
                + ps("infinitos", "g", 64, BR), XE, 320, passo=0.08)
        selo_em(c, t, b4, XE + 40, 480, 38, False)
        E.frase(c, t, b4, ps("não compensa com raízes", "i", 64, CLARO) + ps("não inteiras", "g", 64, BR), XE + 110, 502, passo=0.08)
        form(c, t, c4, "x^2 − 2x − 1 = 0", XE + 110, 660, 100, BR)
        form(c, t, c4 + 0.8, "raízes: 1 ± r{2}", XE + 1000, 660, 80, CLARO)
        E.foco(c, t, d4, 0.5, lambda p: E.pilula(c, "nenhum par em poucos segundos? vá de Bhaskara", W / 2, 880, 58, estilo="g", fundo=AM, cor="#07070F", a=p))
    fase(c, t, C["s14"], 1e9, s14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_ = C["s15.a"], C["s15.b"]
    E.frase(c, t, C["s15"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, a_ - 0.8, 0.45, lambda p: num_bola(c, "1", XE + 40, 380, 40, 50, p))
    E.frase(c, t, a_ - 0.7, ps("raízes de cabeça:", "i", 64), XE + 120, 402, passo=0.08)
    form(c, t, a_, "x^2 + 2x − 15 = 0", XE + 120, 540, 110, COR)
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "2", XE + 40, 700, 40, 50, p))
    E.frase(c, t, b_, ps("monte a equação de raízes", "i", 64), XE + 120, 722, passo=0.08)
    form(c, t, b_ + 1.2, "−1 e 4", XE + 120, 860, 110, COR)
    E.relogio(c, t, C["s16.a"], 1560, 480, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")

    def s17():
        form(c, t, C["s17"] + 0.05, "x^2 + 2x − 15 = 0", W / 2, 200, 100, align="center")
        sp(c, t, a7, a7 + 0.6, "−2", "−15", W / 2, 340, 54, 300)
        E.frase(c, t, b7, ps("produto negativo:", "i", 60) + ps("sinais contrários", "g", 60, COR), XE, 480, passo=0.08)
        form(c, t, c7, "pares de 15:  1 e 15,  3 e 5", XE, 600, 80, TINTA2)
        E.frase(c, t, entre(c7, d7, 0.5), ps("o menos vai no mais longe do zero", "i", 56, TINTA2), XE, 700, passo=0.08)
        par(c, t, d7 - 0.4, d7, 3, "−5", 1450, 640, 72, 110, t2=d7 + 0.3)
        raizes(c, t, d7 + 0.8, ("3", "−5"), W / 2, 900, 110, align="center")
    fase(c, t, C["s17"], C["s18"] - 0.1, s17)

    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]

    def s18():
        nota(c, t, C["s18"] + 0.2, "raízes −1 e 4", XE, 200, 64, COR)
        form(c, t, a8, "soma:  −1 + 4 = 3", XE, 400, 100, CB)
        form(c, t, b8, "produto:  (−1) · 4 = −4", XE, 570, 100, CC)
        monta(c, t, [pf("x^2 ", c8), pf("− 3", c8, CB), pf("x ", c8), pf("− 4", c8, CC), pf(" = 0", c8)], W / 2, 800, 130, "center")
        nota(c, t, c8 + 0.8, "b é a soma com o sinal trocado", W / 2, 920, 54, align="center")
    fase(c, t, C["s18"], 1e9, s18)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s19.a"], [("a = 1:", "g", 72, CA)] + ps("soma das raízes =", "i", 72) + [("−b", "g", 72, CB)]),
             (C["s19.b"], ps("produto =", "i", 72) + [("c", "g", 72, CC)]),
             (C["s19.c"], ps("comece pelo", "i", 72) + ps("produto", "g", 72, COR)))
    fim_padrao(c, t, C, "s19", "s20", itens, "próxima aula: a equação sai de", "problemas",
               extra=lambda: (E.frase(c, t, C["s20.b"], ps("dois números seguidos com produto", "i", 64) + ps("156", "g", 64, COR), XE, 580, passo=0.08),
                              E.frase(c, t, C["s20.c"], ps("a altura de uma bola que", "i", 64) + ps("sobe e cai", "g", 64, COR), XE, 720, passo=0.08)))


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, origem=b_origem, regra=b_regra, sinais=b_sinais, fatorar=b_fatorar,
              montar=b_montar, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
