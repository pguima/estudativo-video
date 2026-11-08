"""Visual — Estudativo · MAT-FAT-010: Bhaskara com raiz não exata.
x(x − 2) = 1 com resposta 1 ± √2; a equação arrumada pela distributiva e pela balança; Δ = 8 e √8 = 2√2 (uma dupla sai);
a fração (2 ± 2√2)/2 com o 2 em evidência e cortado; a conferência com √2 ≈ 1,4; o erro de dividir só um termo; no palco,
o atalho de separar a fração em duas, cada parte com a sua divisão.

Convenções da trilha (as de MAT-FAT-004 a 009: fra, andar, corta_f, evid, coeficientes coloridos, nos_dois, delta_f,
delta_pilula, raizes). Nova: SEPARAR A FRAÇÃO EM DUAS = a fração inteira à esquerda, uma seta e as duas frações com o ± no
meio, cada uma com o seu resultado embaixo (separa).
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-010_bhaskara_raiz_nao_exata.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("arrumar", "formula", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"

# as contas da aula
r2, r5 = math.sqrt(2), math.sqrt(5)
for x in (1 + r2, 1 - r2):
    assert abs(x * (x - 2) - 1) < 1e-12 and abs(x * x - 2 * x - 1) < 1e-12
assert (-2) ** 2 - 4 * 1 * (-1) == 8 == 2 * 2 * 2 and abs(math.sqrt(8) - 2 * r2) < 1e-12
assert abs((2 + 2 * r2) / 2 - (1 + r2)) < 1e-12 and round(r2, 1) == 1.4
assert abs(2.4 * 0.4 - 0.96) < 1e-12 and abs((1 + 2 * 1.4) - 3.8) < 1e-12 and abs(3.8 * 1.8 - 6.84) < 1e-12
assert (10 + 6) / 2 == 10 / 2 + 6 / 2 == 5 + 3 == 8
for x in (2 + r5, 2 - r5):
    assert abs(x * x - (4 * x + 1)) < 1e-12
assert (-4) ** 2 - 4 * 1 * (-1) == 20 == 4 * 5 and abs(math.sqrt(20) - 2 * r5) < 1e-12 and abs((4 + 2 * r5) / 2 - (2 + r5)) < 1e-12
del r2, r5, x


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


def separa(c, t, ta, tb, tc, cima, partes, baixo, x0, y, size, res, tinta=None, cor_res=None):
    """separar a fração em duas (convenção da trilha): a fração inteira em x0 (centro), seta, as duas frações com ± no meio
    e o resultado de cada uma embaixo (tb, tc). partes = (cima1, cima2); res = (r1, r2)"""
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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]

    def conta():
        form(c, t, a_, "x(x − 2) = 1", W / 2, 380, 170, align="center")
        tz = entre(a_, b_, 0.55)
        selo_em(c, t, tz, 560, 520, 36, False)
        E.frase(c, t, tz, ps("nenhum número inteiro resolve", "i", 64, TINTA2), 630, 542, passo=0.08)
        raizes(c, t, b_, ("1 + r{2}", "1 − r{2}"), W / 2, 760, 120, align="center", t1=b_ + 1.5)
        E.foco(c, t, entre(b_, C["s01.end"], 0.65), 0.5, lambda p: E.pilula(c, "e não tem nada de errado com ela", W / 2, 920, 56, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2 = C["s02.a"], C["s02.b"]
    E.frase(c, t, a2, ps("até o fim desta aula, você leva", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, a2 + 1.2, ps("Bhaskara até o fim", "g", 100, COR), XE, 400, passo=0.13)
    E.frase(c, t, a2 + 2.2, ps("quando o delta", "i", 80) + ps("não tem raiz exata", "g", 80, COR), XE, 530, passo=0.12)
    E.foco(c, t, b2 - 0.2, 0.7, lambda p: E.bola(c, 1450, 820, 200 * ease_back(prog(t, b2 - 0.2, 0.7))), blur=0)
    E.foco(c, t, b2 + 0.2, 0.5, lambda p: (centro(c, "+ atalho", 1450, 800, 64, "g", BR, p), centro(c, "da divisão final", 1450, 870, 48, "i", BR, p)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_ = C["s03.a"], C["s03.b"]
    E.frase(c, t, C["s03"] + 0.2, ps("você vai usar", "i", 84), XE, 180)
    E.foco(c, t, a_, 0.45, lambda p: num_bola(c, "1", XE + 40, 330, 40, 50, p))
    E.frase(c, t, a_, ps("Bhaskara,", "g", 66, COR) + ps("com o delta primeiro", "i", 66), XE + 110, 352, passo=0.08)
    delta_f(c, t, a_ + 1.0, XE + 120, 500, 84)
    bhaskara_f(c, t, a_ + 1.6, XE + 760, 500, 84)
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "2", XE + 40, 680, 40, 50, p))
    E.frase(c, t, b_, ps("simplificar radicais:", "g", 66, COR) + ps("tire as duplas de primos", "i", 66), XE + 110, 702, passo=0.08)
    form(c, t, b_ + 1.4, "r{18} = r{3 · 3 · 2} = 3r{2}", XE + 120, 860, 90)
    E.frase(c, t, C["s04"] - 2.2, ps("faltou alguma? procure no canal", "i", 52, TINTA2), 1150, 1010, passo=0.08)


# ---------------- arrumar ----------------
def b_arrumar(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s04.{k}"] for k in "abcd")
    Q = "x(x − 2) = 1"
    E.frase(c, t, a_, ps("1º:", "g", 72, COR) + ps("arrume a equação", "i", 72), XE, 180, passo=0.1)
    E.foco(c, t, b_, 0.5, lambda p: E.pilula(c, "tudo de um lado, zero do outro", 1350, 160, 50, estilo="g", fundo=TINTA, cor=BR, a=p), sobe=8)
    form(c, t, C["s04"] + 0.4, Q, XE, 450, 120)
    arco_d(c, t, c_, Q, "x", "x", XE, 450, 120, 50, n=1)
    arco_d(c, t, c_ + 0.3, Q, "x", "2", XE, 450, 120, 85)
    nota(c, t, c_ + 0.2, "distributiva", 1100, 430, 56, COR)
    form(c, t, c_ + 1.2, "x^2 − 2x = 1", XE, 640, 120)
    nos_dois(c, t, d_, "x^2 − 2x = 1", "− 1", XE, 640, 120)
    form(c, t, d_ + 1.0, "x^2 − 2x − 1 = 0", XE, 870, 130, COR)
    coefs(c, t, C["s05.a"], ("1", "−2", "−1"), 1450, 835, 46, 200, dt=0.6)


# ---------------- delta ----------------
def b_delta(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]

    def s06():
        coefs(c, t, C["s06"] + 0.05, ("1", "−2", "−1"), W / 2, 170, 40, 220)
        monta(c, t, [pf("Δ = ", a6), pf("(", a6), pf("−2", a6, CB), pf(")^2", a6), pf(" − 4 · ", b6), pf("1", b6, CA), pf(" · (", b6),
                     pf("−1", b6, CC), pf(")", b6)], XE, 380, 100)
        monta(c, t, [pf("= 4", a6 + 1.2), pf(" − (−4)", c6)], XE, 560, 100)
        form(c, t, b6 + 1.4, "4 · 1 · (−1) = −4", 1150, 555, 66, TINTA2)
        form(c, t, c6 + 1.4, "= 4 + 4", XE, 740, 100)
        delta_pilula(c, t, c6 + 2.4, "8", XE + 250, 900, 66)
    fase(c, t, C["s06"], C["s07"] - 0.1, s06)

    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")

    def s07():
        delta_pilula(c, t, C["s07"] + 0.05, "8", 1620, 150, 50)
        form(c, t, a7 - 1.6, "r{8} = ?", XE, 330, 120)
        nota(c, t, a7 - 0.8, "8 não é quadrado de nenhum inteiro", XE + 520, 310, 54)
        E.foco(c, t, a7, 0.45, lambda p: E.pilula(c, "raiz não exata", XE + 860, 400, 50, estilo="g", fundo=TINTA2, cor=BR, a=p), sobe=8)
        E.foco(c, t, b7, 0.5, lambda p: E.pilula(c, "não é erro: a conta continua com a raiz", W / 2, 540, 56, estilo="g", fundo=CERTO, cor=BR, a=p))
        form(c, t, c7, "8 = 2 · 2 · 2", XE, 720, 100)
        S = "r{8} = r{2 · 2 · 2}"
        form(c, t, entre(c7, d7, 0.5), S, XE, 900, 110)
        realce(c, t, entre(c7, d7, 0.75), S, "2 · 2", XE, 900, 110, CERTO)
        nota(c, t, entre(c7, d7, 0.8), "uma dupla sai", 1200, 720, 54, CERTO)
        form(c, t, d7, "= 2r{2}", XE + fw(S + " ", 110), 900, 120, CERTO)
    fase(c, t, C["s07"], 1e9, s07)


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    s, y, cx = 130, 480, 640
    TOP0, TOP1 = "2 ± 2r{2}", "2(1 ± r{2})"

    def s08():
        delta_pilula(c, t, C["s08"] + 0.05, "8", 1620, 150, 50)
        form(c, t, C["s08"] + 0.2, "r{8} = 2r{2}", 1160, 165, 70, TINTA2)
        form(c, t, a8, "x =", XE, y + 45, s)
        barra_f(c, t, a8 + 0.2, cx, y, fra_w(TOP1, "2", s), s)
        andar(c, t, a8 + 0.2, TOP0, cx, y, s, True, t1=c8)
        andar(c, t, a8 + 0.2, "2", cx, y, s, False)
        realce_f(c, t, b8, TOP0, "2", cx, y, s, True, t1=c8)
        realce_f(c, t, b8 + 0.2, TOP0, "2", cx, y, s, True, n=1, t1=c8)
        nota(c, t, b8 + 0.4, "o 2 está nos dois termos de cima: evidência", XE, 250, 54, COR)
        andar(c, t, c8 + 0.3, TOP1, cx, y, s, True)
        corta_f(c, t, d8, TOP1, "2", cx, y, s, True)
        corta_f(c, t, d8 + 0.2, "2", "2", cx, y, s, False)
        form(c, t, d8 + 1.0, "= 1 ± r{2}", cx + 380, y + 45, s, CERTO)
    fase(c, t, C["s08"], C["s09"] - 0.1, s08)

    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]

    def s09():
        form(c, t, C["s09"] + 0.05, "x = 1 ± r{2}", XE, 260, 90, TINTA2)
        nota(c, t, C["s09"] + 0.3, "resposta", XE, 380, 56)
        raizes(c, t, a9, ("1 + r{2}", "1 − r{2}"), W / 2, 600, 130, align="center", t1=b9)
        E.foco(c, t, c9, 0.5, lambda p: E.pilula(c, "nas alternativas: com a raiz, sem vírgula", W / 2, 860, 60, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    fase(c, t, C["s09"], 1e9, s09)


# ---------------- faz sentido ----------------
def b_sentido(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s10.{k}"] for k in "abcd")
    E.frase(c, t, C["s10"] + 0.2, ps("faz sentido?", "i", 84), XE, 190, passo=0.1)
    form(c, t, a_, "r{2} ≈ 1,4", XE, 360, 110, COR)
    form(c, t, b_, "1 + 1,4 = 2,4", XE, 530, 90)
    form(c, t, b_ + 1.2, "1 − 1,4 = −0,4", 1000, 530, 90)
    tx = entre(b_, c_, 0.55)
    nota(c, t, tx - 0.6, "na equação original, com x = 2,4:", XE, 670, 54)
    form(c, t, tx, "x − 2 = 0,4", XE + 900, 680, 80, TINTA2)
    form(c, t, c_, "x(x − 2) = 2,4 · 0,4 = 0,96", XE, 830, 100)
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "quase 1: é o esperado com o valor aproximado", W / 2, 970, 52, estilo="g", fundo=CERTO, cor=BR, a=p))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s11.{k}"] for k in "abcde")
    s, y, cx = 110, 400, 400
    TOP = "2 ± 2r{2}"
    E.frase(c, t, C["s11"] + 0.3, ps("o erro mais comum:", "g", 76, ERRADO) + ps("dividir só um termo", "i", 76), XE, 170, passo=0.1)
    fra_em(c, t, a_, TOP, "2", cx, y, s)
    corta_f(c, t, a_ + 1.5, TOP, "2", cx, y, s, True, ERRADO)
    corta_f(c, t, a_ + 1.7, "2", "2", cx, y, s, False, ERRADO)
    form(c, t, b_, "= 1 ± 2r{2}", cx + 220, y + 40, s, ERRADO)
    realce(c, t, b_ + 0.8, "= 1 ± 2r{2}", "2r{2}", cx + 220, y + 40, s, ERRADO)
    nota(c, t, b_ + 1.0, "este 2 ficou sem a divisão", 1300, 300, 50, ERRADO)
    nota(c, t, c_ - 0.4, "teste com 1,4:", XE, 620, 54)
    form(c, t, c_, "1 + 2 · 1,4 = 3,8", XE, 730, 90)
    form(c, t, entre(c_, d_, 0.6), "3,8 − 2 = 1,8", 1080, 730, 90)
    form(c, t, d_, "3,8 · 1,8 = 6,84", XE, 870, 90, ERRADO)
    E.frase(c, t, d_ + 1.2, ps("quase 7:", "g", 60, ERRADO) + ps("longe de 1", "i", 60), 1080, 865, passo=0.08)
    E.foco(c, t, e_, 0.5, lambda p: E.pilula(c, "o ÷ 2 vale para tudo o que está em cima", W / 2, 990, 54, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")

    def s12():
        E.frase(c, t, C["s12"] + 0.2, ps("o atalho:", "i", 72, CLARO) + ps("separe a fração em duas", "g", 72, BR), XE, 170, passo=0.1)
        x1, x2 = separa(c, t, a2, b2, c2, "2 ± 2r{2}", ("2", "2r{2}"), "2", 400, 450, 110, ("1", "r{2}"), BR, AM)
        nota(c, t, b2 + 0.3, "−b ÷ 2a", x1, 300, 46, CLARO, est="b", align="center")
        nota(c, t, c2 + 0.3, "√Δ ÷ 2a", x2, 300, 46, CLARO, est="b", align="center")
        E.foco(c, t, d2, 0.5, lambda p: E.pilula(c, "x = 1 ± √2", W / 2, 920, 72, estilo="g", fundo=AM, cor="#07070F", a=p))
    fase(c, t, C["s12"], C["s13"] - 0.1, s12)

    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]

    def s13():
        E.frase(c, t, C["s13"] + 0.2, ps("funciona porque", "i", 76, CLARO), XE, 180, passo=0.1)
        E.frase(c, t, a3, ps("dividir uma soma é", "i", 70, CLARO) + ps("dividir cada parte", "g", 70, BR), XE, 320, passo=0.1)
        E.frase(c, t, entre(a3, b3, 0.5), ps("R$ 10 + R$ 6 entre duas pessoas", "i", 60, CLARO), XE, 450, passo=0.08)
        form(c, t, b3, "f{10 + 6}{2} = f{10}{2} + f{6}{2}", XE, 640, 110, BR)
        form(c, t, b3 + 1.2, "= 5 + 3 = 8", XE + fw("f{10 + 6}{2} = f{10}{2} + f{6}{2} ", 110), 640, 110, AM)
        selo_em(c, t, c3, XE + 40, 840, 38, True)
        E.frase(c, t, c3, ps("nenhum termo fica sem a sua divisão", "i", 62, CLARO), XE + 110, 862, passo=0.08)
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)

    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]

    def s14():
        selo_em(c, t, a4, XE + 40, 230, 38, False)
        E.frase(c, t, a4, ps("não compensa quando as partes", "i", 64, CLARO) + ps("não dividem certinho", "g", 64, BR), XE + 110, 252, passo=0.08)
        fra_em(c, t, b4, "3 ± r{5}", "2", 600, 520, 130, BR)
        nota(c, t, b4 + 0.8, "3 ÷ 2 não dá inteiro", 900, 540, 60, CLARO)
        E.foco(c, t, c4, 0.5, lambda p: E.pilula(c, "deixe a fração inteira, como saiu da fórmula", W / 2, 860, 60, estilo="g", fundo=AM, cor="#07070F", a=p))
    fase(c, t, C["s14"], 1e9, s14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_ = C["s15.a"], C["s15.b"]
    E.frase(c, t, C["s15"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, a_ - 0.4, ps("resolva", "i", 90), XE, 380, passo=0.1)
    form(c, t, a_, "x^2 = 4x + 1", XE + 40, 610, 150, COR)
    E.foco(c, t, b_, 0.45, lambda p: E.pilula(c, "na forma mais simples", XE + 330, 820, 60, estilo="g", fundo=TINTA, cor=BR, a=p))
    E.relogio(c, t, C["s16.a"], 1560, 480, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")

    def s17():
        form(c, t, C["s17"] + 0.1, "x^2 = 4x + 1", XE, 200, 84, TINTA2)
        form(c, t, a7, "x^2 − 4x − 1 = 0", XE, 360, 110)
        nota(c, t, a7 + 0.4, "tudo para um lado", 1100, 350, 54, COR)
        coefs(c, t, b7, ("1", "−4", "−1"), 1350, 470, 44, 200, dt=0.5)
        form(c, t, c7, "Δ = 16 + 4 = 20", XE, 620, 110)
        form(c, t, d7, "r{20} = r{4 · 5} = 2r{5}", XE, 820, 110, CERTO)
    fase(c, t, C["s17"], C["s18"] - 0.1, s17)

    a8, b8, c8, d8, e8, f8 = (C[f"s18.{k}"] for k in "abcdef")

    def s18():
        s, y, cx = 100, 380, 540
        TOP0, TOP1 = "4 ± 2r{5}", "2(2 ± r{5})"
        form(c, t, a8, "x =", XE, y + 40, s)
        barra_f(c, t, a8, cx, y, fra_w(TOP1, "2", s), s)
        andar(c, t, a8, TOP0, cx, y, s, True, t1=b8)
        andar(c, t, a8, "2", cx, y, s, False)
        andar(c, t, b8 + 0.3, TOP1, cx, y, s, True)
        corta_f(c, t, b8 + 1.2, TOP1, "2", cx, y, s, True)
        corta_f(c, t, b8 + 1.4, "2", "2", cx, y, s, False)
        raizes(c, t, c8, ("2 + r{5}", "2 − r{5}"), XE, 680, 74, t1=c8 + 1.5)
        nota(c, t, d8 - 0.6, "pelo atalho, separando:", 1000, 230, 54, COR)
        form(c, t, d8, "f{4}{2} = 2", 1000, 380, 96)
        form(c, t, e8, "f{2r{5}}{2} = r{5}", 1000, 580, 96)
        form(c, t, f8, "x = 2 ± r{5}", 1000, 770, 110, CERTO)
        selo_em(c, t, f8 + 1.0, 1700, 730, 40)
    fase(c, t, C["s18"], 1e9, s18)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s19.a"], ps("arrume", "i", 72) + ps("tudo igual a zero", "g", 72, COR)),
             (C["s19.b"], ps("simplifique a", "i", 72) + ps("raiz do delta", "g", 72, COR)),
             (C["s19.c"], ps("divida", "i", 72) + ps("todos os termos", "g", 72, COR) + ps("de cima", "i", 72)))
    fim_padrao(c, t, C, "s19", "s20", itens, "próxima aula: raízes", "de cabeça, sem fórmula",
               extra=lambda: (form(c, t, C["s20.b"], "x^2 − 7x + 12 = 0", XE, 590, 100),
                              E.frase(c, t, C["s20.c"], ps("usando a", "i", 76) + ps("soma e o produto", "g", 80, COR), XE, 760, passo=0.12)))


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, arrumar=b_arrumar, delta=b_delta, formula=b_formula, sentido=b_sentido,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
