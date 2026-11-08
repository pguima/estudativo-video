"""Visual — Estudativo · MAT-POR-008: promoções, leve 3, pague 2.

Mesma linguagem da trilha Porcentagem (MAT-POR-006): cartao() = valor de antes (preço cheio, contorno escuro) ou de depois
(o que você paga, cor da matéria); maquina() = a mudança; fluxo() = antes → [máquina] → depois. Peça desta aula: pacote(),
que sai de graça virando contorno tracejado. Todo instante vem de C[...]."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia
from fractions import Fraction as Fr

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-008_leve_3_pague_2.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("preco", "regra", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 3 * 6 == 18 and 2 * 6 == 12 and Fr(6, 18) == Fr(1, 3) and Fr(1, 4) == Fr(25, 100) and Fr(1, 5) == Fr(20, 100)
assert Fr(1, 2) / 2 == Fr(1, 4) and 18 // 2 == 9 and Fr(4, 24) == Fr(1, 6) and round(100 / 6) == 17 and 10 + 10 + 4 == 24
assert 4 * 5 == 20 and 3 * 5 == 15 and 20 * 30 // 100 == 6 and 20 - 6 == 14


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def cen(c, t, ti, s, x, y, size=64, cor=None, est="g"):
    E.foco(c, t, ti, 0.45, lambda a: centro(c, s, x, y, size, est, cor or TINTA, a))


def txt(c, t, ti, s, x, y, size=64, cor=None, est="g"):
    E.foco(c, t, ti, 0.45, lambda a: E.escreve(c, s, x, y, size, est, cor or TINTA, a))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE if cor is None else M.on(cor), a)


def zero_some(c, t, x, y, size, t1, cor=None):
    """o 0 à esquerda de 0,8: some quando a vírgula sai dele. x = borda esquerda do primeiro algarismo depois da vírgula"""
    E.saida(c, t, t1, lambda: centro(c, "0", x - E.casa(size) * 0.5, y, size, "g", cor or TINTA))


def grupo(c, cx, cy, k, fn):
    """desenha fn() escalado por k em torno de (cx, cy)"""
    c.save(); c.translate(cx, cy); c.scale(k, k); c.translate(-cx, -cy)
    fn()
    c.restore()


def vez(itens, t):
    """itens = texto fixo ou [(t0, texto), ...]; devolve [(t0, t_fim, texto)]"""
    if isinstance(itens, str):
        return [(None, 1e9, itens)]
    return [(t0, itens[i + 1][0] if i + 1 < len(itens) else 1e9, s) for i, (t0, s) in enumerate(itens)]


# ---------------- linguagem da trilha Porcentagem ----------------
def larg_cartao(valores, size):
    return max(max(E.larg(s, "g", size) for s in valores) + size * 1.0, size * 2.9)


def cartao(c, t, t0, cx, cy, valor, rotulo=None, depois=False, size=92, w=None, cor=None):
    """valor num cartão: entra em t0. valor = texto ou [(t0, texto), ...] ("?" sai cinza). depois=True: cor da matéria"""
    itens = vez(valor, t)
    w = w or larg_cartao([s for _, _, s in itens], size)
    h = size * 1.75
    tinta = cor or (COR if depois else TINTA)

    def caixa(a):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 30, 30)
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
        c.save(); c.translate(6, 12); c.drawRRect(r, s); c.restore()
        c.drawRRect(r, M.paint(BR, a))
        c.drawRRect(r, M.paint(tinta, a, stroke=6))
        if rotulo:
            centro(c, rotulo, cx, cy - h / 2 - 28, 58, "i", (cor or COR) if depois else TINTA2, a)
    E.foco(c, t, t0, 0.5, caixa)
    for ti, tf, s in itens:
        ti = t0 if ti is None else ti
        cor_s = CINZA if s == "?" else tinta
        E.saida(c, t, tf - 0.05, lambda s=s, ti=ti, cor_s=cor_s: E.foco(c, t, ti, 0.45, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", cor_s, a)), d=0.25)
    return w


def maquina(c, t, t0, cx, cy, fator, size=84):
    """a máquina: o fator numa caixa cheia da cor da matéria. fator = texto ou [(t0, texto), ...]"""
    itens = vez(fator, t)
    w = max(max(E.larg(s, "g", size) for _, _, s in itens) + size * 1.2, size * 2.8)
    h = size * 1.9

    def caixa(a):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 22, 22)
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.22 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 16))
        c.save(); c.translate(8, 14); c.drawRRect(r, s); c.restore()
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeLinear([skia.Point(cx, cy - h / 2), skia.Point(cx, cy + h / 2)],
                                                   [M.hexc(E.mix(E.COR, BR, 0.18), a), M.hexc(E.mix(E.COR, "#000000", 0.25), a)]))
        c.drawRRect(r, p)
        for dx in (-1, 1):  # parafusos: é uma máquina
            c.drawCircle(cx + dx * (w / 2 - 22), cy - h / 2 + 22, 7, M.paint(E.mix(E.COR, BR, 0.45), a))
            c.drawCircle(cx + dx * (w / 2 - 22), cy + h / 2 - 22, 7, M.paint(E.mix(E.COR, BR, 0.45), a))
    E.foco(c, t, t0, 0.5, caixa)
    for ti, tf, s in itens:
        ti = t0 if ti is None else ti
        E.saida(c, t, tf - 0.05, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)), d=0.25)
    return w


XA, XM, XD = 400, 960, 1520  # antes, máquina, depois


def fluxo(c, t, y, antes, fator, depois, ta, tf, td, rot=("antes", "depois"), size=92, x=(XA, XM, XD), cor_d=None):
    """antes → [fator] → depois. ta, tf, td = instantes de cada parte (None = não desenha)"""
    xa, xm, xd = x
    wa = wd = 0
    if ta is not None:
        wa = cartao(c, t, ta, xa, y, antes, rot[0], False, size)
    if td is not None:
        wd = cartao(c, t, td, xd, y, depois, rot[1], True, size, cor=cor_d)
    if tf is not None:
        wm = maquina(c, t, tf, xm, y, fator, size * 0.9)
        p = ep(t, tf - 0.1, 0.5)
        if p > 0:
            M.arrow(c, xa + max(wa, size * 2.9) / 2 + 22, y, xm - wm / 2 - 22, y, TINTA2, p, 6, 20, p)
            M.arrow(c, xm + wm / 2 + 22, y, xd - max(wd, size * 2.9) / 2 - 22, y, TINTA2, p, 6, 20, p)


def volta(c, t, t0, x0, x1, y, rotulo, alto=170, size=62, escuro=False):
    """seta curva por baixo, de x1 (depois) a x0 (antes), com a conta inversa numa pílula. rotulo = texto ou [(t0, texto)]"""
    p = ease_io(prog(t, t0, 0.8))
    if p <= 0:
        return
    cor = "#FFFFFF" if escuro else TINTA
    mx, my = (x0 + x1) / 2, y + 2 * alto
    pts = []
    n = 60
    for i in range(int(n * p) + 1):
        u = i / n
        pts.append(((1 - u) ** 2 * x1 + 2 * u * (1 - u) * mx + u * u * x0, (1 - u) ** 2 * y + 2 * u * (1 - u) * my + u * u * y))
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        M.line(c, ax, ay, bx, by, cor, 1.0, 6)
    if len(pts) >= 2 and p > 0.15:
        (ax, ay), (bx, by) = pts[-2], pts[-1]
        M.arrow(c, ax, ay, bx, by, cor, 1.0, 6, 22)
    for ti, tf, s in vez(rotulo, t):
        ti = t0 + 0.4 if ti is None else ti
        E.saida(c, t, tf - 0.05, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: E.pilula(c, s, mx, y + alto, size, "g", fundo=cor,
                                                                                                  cor=TINTA if escuro else BR, a=a)), d=0.25)


# ---------------- peça desta aula: o pacote ----------------
def pacote(c, cx, cy, s, a=1.0, gratis=0.0, preco=None, metade=False, escuro=False):
    """um pacote com fita. gratis 0..1: o pacote vira contorno tracejado com "grátis" (saiu de graça).
    metade=True: só a metade de baixo continua paga (a segunda unidade pela metade do preço)"""
    if a <= 0:
        return
    w, h = s, s * 1.1
    x, y = cx - w / 2, cy - h / 2
    cor = CLARO if escuro else E.COR
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 16, 16)
    cheio = a * (1 - gratis)
    if metade:
        cheio = a
        c.save(); c.clipRect(skia.Rect.MakeXYWH(x - 4, cy, w + 8, h))
    if cheio > 0:
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeLinear([skia.Point(x, y), skia.Point(x + w, y + h)],
                                                   [M.hexc(E.mix(cor, BR, 0.18), cheio), M.hexc(E.mix(cor, "#000000", 0.2), cheio)]))
        c.drawRRect(rr, p)
        c.drawRect(skia.Rect.MakeXYWH(cx - w * 0.09, y, w * 0.18, h), M.paint(BR, 0.35 * cheio))
        M.line(c, x + 10, y + h * 0.22, x + w - 10, y + h * 0.22, BR, 0.3 * cheio, 3)
    if metade:
        c.restore()
    vazio = a * (1.0 if metade else gratis)
    if vazio > 0:
        tinta = CLARO if escuro else COR
        pt = M.paint(tinta, vazio, stroke=4)
        pt.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
        path = skia.Path(); path.addRRect(rr)
        c.drawPath(path, pt)
        txt_ = "metade" if metade else "grátis"
        centro(c, txt_, cx, (y + cy) / 2 + s * 0.08 if metade else cy + s * 0.08, s * 0.22, "g", tinta, vazio)
    if preco:
        centro(c, preco, cx, y + h + 64, 56, "g", BR if escuro else TINTA, a)


def fila(c, t, t0, n, cx, cy, s, gap=40, tg=None, precos=None, metade=None, escuro=False, passo_=0.15):
    """n pacotes lado a lado, centrados em cx. tg = instante em que o último sai de graça; metade = índice pela metade"""
    x0 = cx - (n * s + (n - 1) * gap) / 2 + s / 2
    for i in range(n):
        g = ep(t, tg, 0.5) if (tg is not None and i == n - 1 and metade is None) else 0.0
        E.foco(c, t, t0 + i * passo_, 0.45, lambda a, i=i, g=g: pacote(c, x0 + i * (s + gap), cy, s, a, g, precos[i] if precos else None,
                                                                    metade == i and tg is not None and t >= tg, escuro))
    return x0


def lojas(c, t, ta, tb, n_leva, n_paga, pct, t_t=None, titulo=None):
    """as duas lojas da pergunta: leve n, pague m (à esquerda) e x% de desconto (à direita)"""
    E.foco(c, t, ta, 0.45, lambda a: E.pilula(c, f"leve {n_leva}, pague {n_paga}", 560, 300, 64, "g", a=a))
    fila(c, t, ta + 0.3, n_leva, 560, 560, 150 if n_leva == 3 else 120, 30, ta + 1.4)
    E.foco(c, t, tb, 0.45, lambda a: E.pilula(c, f"{pct}% de desconto", 1400, 300, 64, "g", fundo=TINTA, a=a))
    E.foco(c, t, tb + 0.4, 0.5, lambda a: num_bola(c, f"− {pct}%", 1400, 560, 150, 84, a, TINTA))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        lojas(c, t, ka, kb, 3, 2, 30)
        E.frase(c, t, lerp(kb, kc, 0.55), ps("você precisa de", "i", 70) + [("3 pacotes", "g", 70, COR)], W / 2, 840, "center", 0.12)
        E.frase(c, t, kc, ps("qual sai", "i", 84) + [("mais barato?", "g", 84, COR)], W / 2, 970, "center", 0.14)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.2), [("leve e pague", "g", 110, COR)], XE, 470, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), ps("vira", "i", 96) + [("porcentagem", "g", 96, COR)], XE, 620, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.7), ps("de desconto", "i", 96), XE, 760, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "quantos por cento:", "parte ÷ total"), ("s03.c", "dízima:", "0,333... sem fim"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 260 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 210, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 88)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 70, COR)], x + 44, y + 176)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(440, 730, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- com preço ----------------
def b_preco(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]

    def pacotes():
        E.frase(c, t, C["s04"] + 0.1, ps("vamos com", "i", 76) + [("preço", "g", 76, COR)], W / 2, 140, "center", 0.14)
        fila(c, t, a4, 3, W / 2, 330, 140, 60, c4, precos=["R$ 6"] * 3)
    E.saida(c, t, b5 - 0.2, pacotes)

    def conta():
        sobe = ease_io(prog(t, b5 - 0.2, 0.8))
        yf = lerp(720, 300, sobe)
        fluxo(c, t, yf, "R$ 18", "− R$ 6", "R$ 12", b4, a5, c4, rot=("preço cheio", "você pagou"))
        if t >= b5:
            q = ep(t, b5 + 0.3, 0.5)
            wa = larg_cartao(["R$ 18"], 92)
            E.caixa_pontilhada(c, XA - wa / 2 - 20, yf - 100, wa + 40, 200, q, COR, prog_=q)
            E.foco(c, t, b5 + 0.4, 0.45, lambda a: centro(c, "o total", XA, yf + 160, 60, "g", COR, a))
            E.foco(c, t, b5 - 0.6, 0.45, lambda a: centro(c, "a parte", XM, yf + 160, 60, "g", TINTA2, a))
        E.frase(c, t, c5, [("6 ÷ 18", "g", 110), ("=", "g", 100, TINTA2)], 1000, 680, "right", 0.25)
        E.foco(c, t, c5 + 1.0, 0.5, lambda a: E.fracao(c, 1, 3, 1120, 640, 110, COR, a))
        E.frase(c, t, d5, ps("a economia vai sobre o", "i", 70) + [("preço cheio", "g", 70, COR)], W / 2, 940, "center", 0.12)
    E.saida(c, t, C["s06"] - 0.1, conta)
    if t < C["s06"]:
        return
    E.frase(c, t, a6, [("1 ÷ 3", "g", 120), ("=", "g", 110, TINTA2)], 860, 330, "right", 0.25)
    E.foco(c, t, a6 + 1.2, 0.45, lambda a: E.escreve(c, "0,333...", 920, 330, 120, "g", COR, a))
    q = ep(t, b6, 0.5)
    E.caixa_pontilhada(c, 1040, 220, 300, 140, q, COR, prog_=q)
    E.foco(c, t, b6 + 0.2, 0.45, lambda a: E.pilula(c, "dízima: o 3 se repete", 1180, 450, 52, "g", a=a))
    E.frase(c, t, c6, [("em %:", "i", 90), ("33,333...%", "g", 110)], W / 2, 660, "center", 0.25)
    E.foco(c, t, d6, 0.5, lambda a: num_bola(c, "≈ 33%", 840, 860, 150, 84, a))
    E.frase(c, t, d6 + 0.6, ps("de desconto", "i", 76), 1030, 885, "left")


# ---------------- a regra, sem preço ----------------
def b_regra(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]

    def sete():
        E.frase(c, t, a7, ps("o preço", "i", 84) + [("não importou", "g", 84, COR)], W / 2, 180, "center", 0.14)
        fila(c, t, a7 + 0.3, 3, W / 2, 470, 160, 60, b7 + 0.8)
        E.frase(c, t, b7, ps("de cada 3,", "i", 76) + [("1 saiu de graça", "g", 76, COR)], W / 2, 740, "center", 0.12)
        E.frase(c, t, c7, [("1 de 3", "g", 90), ("=", "g", 90, TINTA2), ("1/3", "g", 90, COR), ("≈", "g", 90, TINTA2), ("33%", "g", 90, COR)],
                W / 2, 910, "center", 0.25)
    E.saida(c, t, a8 - 0.1, sete)
    if a8 - 0.1 <= t < a9 - 0.1:
        def oito():
            E.frase(c, t, a8, ps("a regra:", "i", 76), XE, 200)
            E.foco(c, t, a8 + 0.5, 0.5, lambda a: E.fracao(c, "o que sai de graça", "o que você leva", 1100, 190, 70, COR, a))
            E.frase(c, t, b8, [("leve 4, pague 3", "g", 80)], W / 2, 430, "center")
            fila(c, t, b8 + 0.3, 4, W / 2, 620, 130, 40, b8 + 1.6)
            E.frase(c, t, lerp(b8, c8, 0.4), [("1 de 4", "g", 90), ("=", "g", 90, TINTA2), ("1/4", "g", 90, COR), ("=", "g", 90, TINTA2)], 1080, 920, "right", 0.2)
            E.foco(c, t, c8, 0.5, lambda a: num_bola(c, "25%", 1240, 890, 110, 80, a))
        E.saida(c, t, a9 - 0.1, oito)
    if a9 - 0.1 <= t < a10 - 0.1:
        def nove():
            E.frase(c, t, a9, ps("a 2ª unidade pela", "i", 80) + [("metade do preço?", "g", 80, COR)], W / 2, 180, "center", 0.12)
            fila(c, t, a9 + 0.4, 2, W / 2, 450, 170, 80, b9, metade=1)
            E.frase(c, t, b9, ps("leva 2, sai de graça", "i", 76) + [("meia unidade", "g", 76, COR)], W / 2, 700, "center", 0.12)
            E.frase(c, t, c9, [("0,5 ÷ 2", "g", 84), ("=", "g", 84, TINTA2), ("0,25", "g", 84), ("=", "g", 84, TINTA2), ("25%", "g", 84, COR)],
                    W / 2, 850, "center", 0.25)
            E.frase(c, t, d9, ps("empata com o", "i", 70) + [("leve 4, pague 3", "g", 70, COR)], W / 2, 980, "center", 0.12)
        E.saida(c, t, a10 - 0.1, nove)
    if t < a10 - 0.1:
        return
    E.frase(c, t, C["s10"] + 0.1, ps("voltando ao", "i", 80) + [("começo", "g", 80, COR)], W / 2, 180, "center", 0.14)
    E.foco(c, t, a10, 0.45, lambda a: E.pilula(c, "leve 3, pague 2", 600, 340, 60, "g", a=a))
    E.foco(c, t, a10 + 0.3, 0.5, lambda a: num_bola(c, "≈ 33%", 600, 590, 150, 92, a))
    E.foco(c, t, b10, 0.45, lambda a: E.pilula(c, "30% de desconto", 1320, 340, 60, "g", fundo=TINTA, a=a))
    E.foco(c, t, b10 + 0.3, 0.5, lambda a: num_bola(c, "30%", 1320, 590, 150, 92, a, TINTA))
    cen(c, t, b10 + 0.6, ">", W / 2, 625, 110, TINTA2)
    E.foco(c, t, c10 + 0.6, 0.45, lambda a: E.selo(c, 720, 470, 48, True, a))
    E.frase(c, t, c10, ps("para 3 pacotes,", "i", 70) + [("o leve 3, pague 2 ganha,", "g", 70, COR)] + ps("por pouco", "i", 70), W / 2, 900, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    E.frase(c, t, C["s11"] + 0.1, [("o erro", "g", 96, ERRADO)] + ps("comum", "i", 96), W / 2, 170, "center", 0.14)
    E.frase(c, t, a11, ps("dividir pelo que você", "i", 76) + [("paga", "g", 76, ERRADO)], W / 2, 320, "center", 0.12)
    E.frase(c, t, b11, [("1 grátis ÷ 2 pagos", "g", 84), ("=", "g", 84, TINTA2), ("1/2", "g", 84, ERRADO), ("=", "g", 84, TINTA2), ("50%", "g", 84, ERRADO)],
            W / 2, 480, "center", 0.25)
    if t >= c11 + 2.5:
        E.risco(c, 340, 500, 1580, 420, t, c11 + 2.5, largura=12)
    E.frase(c, t, c11, ps("50% de desconto: pagar", "i", 70) + [("R$ 9", "g", 76, ERRADO)], 560, 680, "center", 0.12)
    E.frase(c, t, lerp(c11, d11, 0.6), ps("você pagou", "i", 70) + [("R$ 12", "g", 76, COR)], 1440, 680, "center", 0.12)
    E.frase(c, t, d11, ps("o total é sempre", "i", 80) + [("tudo o que você leva", "g", 80, COR)], W / 2, 900, "center", 0.14)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a12, b12, c12, d12, e12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]

    def tres():
        E.frase(c, t, C["s12"] + 0.1, [("o atalho:", "g", 70, BR)] + ps("guarde três frações", "i", 74, CLARO), W / 2, 170, "center", 0.15)
        for i, (n, d, pct, ti) in enumerate(((1, 3, "≈ 33%", b12), (1, 4, "25%", c12), (1, 5, "20%", d12))):
            x = 480 + i * 480
            E.foco(c, t, ti, 0.5, lambda a, x=x, n=n, d=d: E.fracao(c, n, d, x, 420, 150, BR, a))
            cen(c, t, ti + 0.4, pct, x, 680, 100, CLARO)
        q = ep(t, e12, 0.5)
        E.caixa_pontilhada(c, 1440 - 160, 270, 320, 470, q, BR, prog_=q)
        E.frase(c, t, e12, [("leve 5, pague 4:", "i", 72, CLARO), ("1 em 5", "g", 74, BR), ("=", "g", 74, CLARO), ("20%", "g", 76, BR)],
                W / 2, 900, "center", 0.2)
    E.saida(c, t, C["s13"] - 0.1, tres)
    if C["s13"] - 0.1 <= t < C["s14"] - 0.1:
        def treze():
            E.frase(c, t, a13, ps("a fração que sai de graça", "i", 80, CLARO), W / 2, 260, "center", 0.12)
            E.frase(c, t, a13 + 1.4, [("já é o desconto", "g", 90, BR)], W / 2, 400, "center")
            E.frase(c, t, b13, ps("não compensa com", "i", 76, CLARO) + [("preços diferentes", "g", 76, BR)], W / 2, 640, "center", 0.12)
            E.frase(c, t, c13, ps("aí:", "i", 76, CLARO) + [("economia ÷ preço cheio", "g", 80, BR)], W / 2, 820, "center", 0.15)
        E.saida(c, t, C["s14"] - 0.1, treze)
    if t < C["s14"] - 0.1:
        return
    E.frase(c, t, C["s14"] + 0.1, ps("leve 3, pague 2 com preços", "i", 72, CLARO) + [("diferentes", "g", 72, BR)], W / 2, 170, "center", 0.12)
    fila(c, t, a14, 3, W / 2, 400, 150, 70, lerp(a14, b14, 0.65), precos=["R$ 10", "R$ 10", "R$ 4"], escuro=True)
    E.frase(c, t, b14, [("preço cheio:", "i", 72, CLARO), ("R$ 24", "g", 76, BR)], W / 2, 700, "center", 0.2)
    E.frase(c, t, c14, [("4 ÷ 24", "g", 84, BR), ("=", "g", 84, CLARO), ("1/6", "g", 84, BR), ("≈", "g", 84, CLARO), ("17%", "g", 90, CLARO)],
            W / 2, 850, "center", 0.3)
    E.frase(c, t, lerp(d14, C["s14.end"], 0.5), ps("bem longe dos", "i", 66, CLARO) + [("33%", "g", 66, BR)], W / 2, 980, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a15, b15, c15, d15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 150)
    E.frase(c, t, a15, [("4 caixas de leite", "g", 72)], XE + 470, 150)
    sobe = ease_io(prog(t, C["s16"] - 0.2, 0.8))
    k = lerp(1.0, 0.62, sobe)

    def duas():
        lojas(c, t, b15, c15, 4, 3, 30)
    grupo(c, W / 2, 430, k, lambda: (c.translate(0, -sobe * 120 / k), duas()))
    E.saida(c, t, C["s16"] - 0.2, lambda: E.frase(c, t, d15, ps("qual você", "i", 84) + [("escolhe?", "g", 84, COR)], W / 2, 900, "center", 0.14))
    E.relogio(c, t, C["s16.a"], 960, 720, 130)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]

    def regra():
        E.frase(c, t, C["s17"] + 0.2, [("leve 4, pague 3", "g", 80, COR)], W / 2, 180, "center")
        fila(c, t, C["s17"] + 0.4, 4, W / 2, 380, 120, 40, a17)
        E.frase(c, t, a17 + 0.4, [("1 em 4", "g", 90), ("=", "g", 90, TINTA2), ("1/4", "g", 90, COR), ("=", "g", 90, TINTA2), ("25%", "g", 90, COR)],
                W / 2, 640, "center", 0.25)
        E.frase(c, t, b17, [("25%", "g", 100), ("<", "g", 100, TINTA2), ("30%", "g", 100, CERTO)], W / 2, 830, "center", 0.3)
        E.frase(c, t, c17, ps("desta vez,", "i", 70) + [("os 30% de desconto ganham", "g", 70, CERTO)], W / 2, 980, "center", 0.12)
    E.saida(c, t, C["s18"] - 0.1, regra)
    if t < C["s18"]:
        return
    E.frase(c, t, a18, ps("caixa de", "i", 76) + [("R$ 5:", "g", 76, COR)] + ps("4 caixas,", "i", 76), W / 2, 180, "center", 0.12)
    E.frase(c, t, b18, [("R$ 20", "g", 80)], 1330, 180)
    lado = ((560, "leve 4, pague 3", E.COR, (lerp(b18, c18, 0.4), lerp(b18, c18, 0.75), c18), "paga 3 × 5", "R$ 15", False),
            (1360, "30% de desconto", TINTA, (lerp(c18, d18, 0.35), lerp(c18, d18, 0.75), d18), "20 − 6", "R$ 14", True))
    for x, nome, fundo, (tp, tl, tc), linha_, val, ok in lado:
        E.foco(c, t, tp, 0.45, lambda a, x=x, nome=nome, fundo=fundo: E.pilula(c, nome, x, 380, 58, "g", fundo=fundo, a=a))
        cen(c, t, tl, linha_, x, 560, 80, TINTA2)
        cartao(c, t, tc, x, 760, val, "você paga", True, 96, cor=CERTO if ok else None)
    E.foco(c, t, d18 + 0.4, 0.45, lambda a: E.selo(c, 1620, 700, 48, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a19, b19 = C["s19.a"], C["s19.b"]

    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.frase(c, t, a19 - 0.2, [("desconto", "g", 90), ("=", "g", 90, TINTA2)], 820, 460, "right", 0.2)
        E.foco(c, t, a19, 0.5, lambda a: E.fracao(c, "o que sai de graça", "o que você leva", 1250, 420, 70, COR, a))
        E.frase(c, t, b19, [("leve 3, pague 2", "g", 84), ("≈", "g", 84, TINTA2), ("33%", "g", 90, COR)], W / 2, 800, "center", 0.25)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    E.frase(c, t, C["s20"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, a20, [("Praticando", "g", 120, COR)], XE, 450)
    E.frase(c, t, a20 + 0.4, [("porcentagem", "g", 120, COR)], XE, 590)
    E.frase(c, t, b20, ps("descontos, aumentos, preço de antes e lucro", "i", 62), XE, 740, "left", 0.08)
    E.foco(c, t, c20, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=a))
    p = ease_io(prog(t, c20 + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, c20 + 0.2, 0.4))
    E.frase(c, t, d20, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, preco=b_preco, regra=b_regra, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
