"""Visual — Estudativo · MAT-POR-006: achar o preço antes do aumento ou desconto.

Linguagem da trilha Porcentagem (as peças abaixo de "linguagem da trilha" servem a todas as aulas MAT-POR):
- cartao(): o valor num cartão branco. ANTES = contorno escuro e rótulo cinza; DEPOIS = contorno e número na cor da matéria.
- maquina(): o fator (× 0,8, × 1,15) ou a mudança (− 20%) numa caixa cheia da cor da matéria: é a "máquina" que transforma.
- fluxo(): antes → [máquina] → depois, numa linha. Valor que ainda não se sabe é "?" em cinza e troca na fala.
- volta(): seta curva por baixo, do depois para o antes, com a conta inversa (÷ 0,8) numa pílula escura.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-006_preco_antes_do_aumento_ou_desconto.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("maquina", "aumento", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 96 / 0.8 == 120 and 960 / 8 == 120 and 120 * 0.2 == 24 and 120 - 24 == 96
assert round(230 / 1.15, 6) == 200 and 115 * 2 == 230 and 115 * 200 == 23000 and 23000 / 115 == 200
assert round(96 * 0.2, 2) == 19.2 and round(96 + 19.2, 2) == 115.2 and round(115.2 * 0.8, 2) == 92.16
assert 96 / 4 == 24 and 5 * 24 == 120
assert round(168 / 1.12, 6) == 150 and 16800 / 112 == 150 and 168 - 112 == 56 and 560 / 112 == 5
assert round(150 * 0.12, 6) == 18 and 150 + 18 == 168


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        fluxo(c, t, 400, "?", "− 20%", "R$ 96", lerp(kb, kc, 0.4), kb, ka, rot=("antes", "você pagou"))
        E.frase(c, t, lerp(kb, kc, 0.4), ps("quanto custava", "i", 80) + [("antes?", "g", 80, COR)], W / 2, 170, "center", 0.12)
        E.frase(c, t, kc, [("R$ 96", "g", 96), ("+", "g", 96, TINTA2), ("20%", "g", 96)], 640, 770, "center", 0.25)
        E.frase(c, t, kc + 1.6, [("=", "g", 96, TINTA2), ("R$ 115,20", "g", 96, ERRADO)], 1280, 770, "center", 0.2)
        if t >= kc + 3.2:
            E.risco(c, 300, 800, 1600, 690, t, kc + 3.2, largura=14)
        E.frase(c, t, kc + 3.5, ps("errou por quase", "i", 76) + [("R$ 5", "g", 76, ERRADO)], W / 2, 950, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.25), ps("achar o", "i", 100) + [("preço", "g", 110, COR)], XE, 490, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.4), [("de antes", "g", 110, COR)], XE, 620, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("de qualquer aumento", "i", 80), XE, 750, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.8), ps("ou desconto", "i", 80), XE, 850, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    kb, kc = C["s03.b"], C["s03.c"]
    p = ep(t, kb, 0.5)
    E.caixa_pontilhada(c, x, 200, w, 300, p, prog_=p)
    E.frase(c, t, kb + 0.1, [("os fatores", "i", 62)], x + 44, 285)
    E.frase(c, t, lerp(kb, kc, 0.2), [("−20%", "g", 64, TINTA2), ("=", "g", 64, TINTA2), ("× 0,8", "g", 64, COR)], x + 44, 375, "left", 0.25)
    E.frase(c, t, lerp(kb, kc, 0.6), [("+15%", "g", 64, TINTA2), ("=", "g", 64, TINTA2), ("× 1,15", "g", 64, COR)], x + 44, 465, "left", 0.25)
    p = ep(t, kc, 0.5)
    E.caixa_pontilhada(c, x, 570, w, 210, p, prog_=p)
    E.frase(c, t, kc + 0.1, [("dividir por decimal:", "i", 62)], x + 44, 658)
    E.frase(c, t, kc + 0.3, [("sem vírgula no divisor", "g", 64, COR)], x + 44, 742)
    q = ease_io(prog(t, kc - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(470, 750, q), ep(t, kb, 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- a máquina ----------------
def b_maquina(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    y = 470
    E.saida(c, t, b5 - 0.1, lambda: E.frase(c, t, a4, ps("o desconto é", "i", 84) + [("uma máquina", "g", 84, COR)], W / 2, 180, "center", 0.14))
    E.frase(c, t, b5, ps("rode a máquina", "i", 84) + [("ao contrário", "g", 84, COR)], W / 2, 180, "center", 0.14)
    antes = [(lerp(a4, b4, 0.4), "R$ ..."), (a5 + 0.4, "?")]
    depois = [(c4, "R$ ..."), (a5, "R$ 96")]
    fluxo(c, t, y, antes, [(a4, ""), (b4, "× 0,8")], depois, lerp(a4, b4, 0.4), a4, c4, rot=("preço antigo", "com desconto"))
    volta(c, t, b5 + 0.3, XA, XD, y + 100, [(b5 + 0.7, "ao contrário"), (c5, "÷ 0,8")], alto=150)
    E.frase(c, t, c5 + 0.5, ps("o contrário de multiplicar é", "i", 70) + [("dividir", "g", 72, COR)], W / 2, 980, "center", 0.12)


# ---------------- a conta ----------------
def b_conta(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    s, y = 140, 330
    cl = E.casa(s)
    xa, xb = 300, 900
    pulo = lerp(b6, c6, 0.45)
    E.foco(c, t, a6, 0.45, lambda q: E.anda(c, t, "96", 2, [(pulo, 3)], xa, y, s, tv=pulo - 0.3, some=True))
    cen(c, t, a6 + 0.6, "÷", 760, y, 120, TINTA2)
    E.foco(c, t, a6 + 1.0, 0.45, lambda q: E.anda(c, t, "8", 0, [(pulo, 1)], xb, y, s, some=True))
    E.foco(c, t, a6 + 1.0, 0.45, lambda q: zero_some(c, t, xb, y, s, pulo + 0.2))
    if t < c6 + 0.3:
        E.saida(c, t, c6, lambda: (E.chave(c, xb - 4, xb + cl + 4, y + 40, COR, ep(t, b6, 0.4), 24, 6),
                                   cen(c, t, b6 + 0.1, "1 casa", xb + cl / 2, y + 140, 60, COR)))
    E.saida(c, t, a7, lambda: E.frase(c, t, lerp(b6, c6, 0.3), ps("ande", "i", 76) + [("1 casa", "g", 76, COR)] + ps("nos dois números", "i", 76),
                                      W / 2, 560, "center", 0.14))
    cen(c, t, a7, "=", 1180, y, 120, TINTA2)
    E.foco(c, t, a7 + 0.6, 0.5, lambda a: num_bola(c, "120", 1420, y - 46, 130, 120, a))
    # o preço e a conferência
    E.foco(c, t, b7, 0.5, lambda a: (E.escreve(c, "custava", XE, 610, 80, "i", TINTA, a),
                                     E.escreve(c, "R$ 120", XE + 300, 610, 96, "g", COR, a)))
    E.frase(c, t, c7, [("20% de 120", "g", 80), ("=", "g", 80, TINTA2), ("24", "g", 80, COR)], XE, 780, "left", 0.3)
    E.frase(c, t, d7, [("120 − 24", "g", 80), ("=", "g", 80, TINTA2), ("96", "g", 80, CERTO)], XE, 920, "left", 0.3)
    E.foco(c, t, d7 + 1.4, 0.45, lambda a: E.selo(c, 900, 895, 56, True, a))
    E.foco(c, t, c7 - 0.4, 0.45, lambda a: E.escreve(c, "confira:", 1180, 780, 64, "i", TINTA2, a))


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    E.frase(c, t, C["s08"] + 0.2, ps("vale para", "i", 76) + [("qualquer caso", "g", 76, COR)], W / 2, 170, "center", 0.14)
    E.frase(c, t, a8, [("antes", "g", 130), ("=", "g", 110, TINTA2), ("agora", "g", 130), ("÷", "g", 110, TINTA2), ("fator", "g", 130, COR)],
            W / 2, 400, "center", 0.35)
    for x, ti, nome, sinal_, ex, fundo in ((540, b8, "desconto", "fator < 1", "× 0,8", TINTA), (1380, c8, "aumento", "fator > 1", "× 1,15", E.COR)):
        E.foco(c, t, ti, 0.45, lambda a, x=x, nome=nome, fundo=fundo: E.pilula(c, nome, x, 600, 64, "g", fundo=fundo, a=a))
        cen(c, t, ti + 0.5, sinal_, x, 780, 110, COR)
        cen(c, t, ti + 1.0, ex, x, 910, 84, TINTA2, "b")


# ---------------- aumento ----------------
def b_aumento(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    sobe = ease_io(prog(t, a10 + 0.6, 0.8))
    yf, k = lerp(470, 215, sobe), lerp(1.0, 0.6, sobe)

    def topo():
        fluxo(c, t, 470, [(c9, "?"), (c11, "R$ 200")], [(a9, "+ 15%"), (a10, "× 1,15")], "R$ 230", c9, a9, b9,
              rot=("antes", "depois"))
        volta(c, t, a10 + 0.2, XA, XD, 570, "÷ 1,15", alto=110)
    grupo(c, W / 2, 470, k, lambda: (c.translate(0, (yf - 470) / k), topo()))
    E.saida(c, t, a10 + 0.5, lambda: E.frase(c, t, C["s09"] + 0.2, ps("agora com", "i", 76) + [("aumento", "g", 76, COR)], W / 2, 170, "center", 0.14))
    if t < a10 + 0.6:
        return
    s, y = 120, 600
    cl = E.casa(s)
    xa = 400
    xd = xa + 5 * cl + 70
    xb = xd + 80
    E.foco(c, t, a10 + 0.8, 0.45, lambda q: E.anda(c, t, "230", 3, [(b10 + 0.2, 5)], xa, y, s, tv=b10, some=True))
    cen(c, t, a10 + 1.0, "÷", xd, y, 100, TINTA2)
    E.foco(c, t, a10 + 1.2, 0.45, lambda q: E.anda(c, t, "115", 1, [(c10 + 0.2, 3)], xb, y, s, some=True))
    if t < b10 + 0.3:
        E.saida(c, t, b10, lambda: (E.chave(c, xb + cl - 4, xb + 3 * cl + 4, y + 40, COR, ep(t, a10 + 1.6, 0.4), 24, 6),
                                    cen(c, t, a10 + 1.7, "2 casas", xb + 2 * cl, y + 140, 60, COR)))
    E.frase(c, t, a11, [("115 × 2", "g", 68), ("=", "g", 68, TINTA2), ("230", "g", 68)], XE + 120, 770, "left", 0.25)
    E.frase(c, t, lerp(a11, b11, 0.5), [("115 × 200", "g", 68), ("=", "g", 68, TINTA2), ("23000", "g", 68)], XE + 120, 875, "left", 0.25)
    E.frase(c, t, b11, [("23000 ÷ 115", "g", 68), ("=", "g", 68, TINTA2), ("200", "g", 68, COR)], XE + 120, 980, "left", 0.25)
    E.foco(c, t, c11, 0.5, lambda a: E.pilula(c, "era R$ 200", 1450, 875, 72, "g", a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    E.frase(c, t, C["s12"] + 0.2, [("o erro", "g", 100, ERRADO)] + ps("do começo", "i", 96), W / 2, 170, "center", 0.14)

    def errado():
        E.frase(c, t, a12, ps("a porcentagem", "i", 70) + [("sobre o preço de agora", "g", 66, ERRADO)], W / 2, 320, "center", 0.12)
        E.frase(c, t, b12, [("20% de 96", "g", 84), ("=", "g", 84, TINTA2), ("19,20", "g", 84)], W / 2, 520, "center", 0.3)
        E.frase(c, t, c12, [("96 + 19,20", "g", 84), ("=", "g", 84, TINTA2), ("115,20", "g", 84, ERRADO)], W / 2, 680, "center", 0.3)
    E.saida(c, t, b13 - 0.2, errado)
    if t < a13:
        return
    E.frase(c, t, a13, ps("o desconto é sobre", "i", 74) + [("o preço antigo,", "g", 72, COR)] + ps("que é maior", "i", 74), W / 2, 320, "center", 0.12)
    if t < b13 - 0.2:
        return
    fluxo(c, t, 600, "R$ 115,20", "× 0,8", "R$ 92,16", b13, b13 + 0.6, c13, rot=("teste", "sobra"), size=80, cor_d=ERRADO)
    E.foco(c, t, d13, 0.45, lambda a: E.selo(c, 1520, 770, 50, False, a))
    E.frase(c, t, d13, [("não dá", "i", 84), ("R$ 96", "g", 84, ERRADO)], W / 2, 920, "center", 0.2)


# ---------------- atalho (palco escuro) ----------------
PX, PY, PW, PH = 360, 470, 1200, 150


def partes(c, t, n, cores, a=1.0, nums=None, ta=None):
    """barra de n partes no palco: cores[i] = cor cheia ou None (só o contorno); nums = texto dentro, que entra em ta"""
    if a <= 0:
        return
    w = PW / n
    for i in range(n):
        x = PX + i * w
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 6, PY, w - 12, PH), 18, 18)
        if cores[i]:
            c.drawRRect(r, M.paint(cores[i], a))
        c.drawRRect(r, M.paint(CLARO, a, stroke=4))
        if nums and ta is not None:
            E.foco(c, t, ta + 0.08 * i, 0.4, lambda q, x=x, i=i: centro(c, nums, x + w / 2, PY + PH / 2 + 28, 78, "g", "#07070F" if cores[i] == CLARO else BR, q * a))


def b_atalho(c, t, C, b):
    palco(c, t)
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    a15, b15, c15, d15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    a16, b16, c16, d16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]

    def barra():
        E.frase(c, t, C["s14"] + 0.1, [("o atalho", "g", 64, BR), ("com frações", "i", 68, CLARO)], W / 2, 110, "center", 0.2)
        E.frase(c, t, a14, [("20%", "g", 110, BR), ("=", "g", 100, CLARO)], 900, 330, "right", 0.3)
        E.foco(c, t, a14 + 0.6, 0.45, lambda a: E.fracao(c, 1, 5, 1010, 290, 96, CLARO, a))
        pinta = ep(t, d14, 0.5)
        cores = [CLARO if pinta > 0.5 else None] * 4 + ["#3A3A4A" if t >= c14 else None]
        E.foco(c, t, b14, 0.5, lambda a: partes(c, t, 5, cores, a, "24", a15 + 1.2))
        E.foco(c, t, c14 + 0.2, 0.4, lambda a: centro(c, "desconto", PX + PW * 0.9, PY + PH + 70, 54, "i", CLARO, a))
        E.foco(c, t, d14 + 0.2, 0.4, lambda a: centro(c, "você pagou", PX + PW * 0.4, PY + PH + 70, 54, "i", CLARO, a))
        # 4 partes = 96
        E.chave(c, PX + 6, PX + PW * 0.8 - 6, PY - 18, CLARO, ep(t, C["s15"] + 0.2, 0.4), -24, 6)
        E.foco(c, t, C["s15"] + 0.4, 0.4, lambda a: centro(c, "R$ 96", PX + PW * 0.4, PY - 60, 64, "g", BR, a))
        E.frase(c, t, a15, [("1 parte:", "i", 70, CLARO)], 770, 830, "right")
        E.frase(c, t, a15 + 0.3, [("96 ÷ 4 = 24", "g", 76, BR)], 800, 830, "left")
        q = ep(t, b15, 0.5)
        E.caixa_pontilhada(c, PX - 16, PY - 16, PW + 32, PH + 32, q, CLARO, prog_=q)
        E.frase(c, t, b15 + 0.3, [("5 partes:", "i", 70, CLARO)], 770, 960, "right")
        E.frase(c, t, c15, [("5 × 24 =", "g", 76, BR), ("120", "g", 90, CLARO)], 800, 960, "left", 0.3)
    E.saida(c, t, d15 - 0.1, barra)

    if d15 <= t:
        def regra():
            E.foco(c, t, d15, 0.5, lambda a: E.fracao(c, 4, 5, 560, 470, 200, BR, a))
            E.foco(c, t, d15 + 0.3, 0.45, lambda a: E.pilula(c, "÷ 4", 840, 380, 64, "g", fundo=CLARO, cor="#07070F", a=a))
            E.foco(c, t, d15 + 1.2, 0.45, lambda a: E.pilula(c, "× 5", 840, 610, 64, "g", fundo=CLARO, cor="#07070F", a=a))
            E.frase(c, t, d15 + 0.3, ps("divide pelo", "i", 76, CLARO) + [("de cima", "g", 76, BR)], 1000, 400, "left", 0.15)
            E.frase(c, t, d15 + 1.2, ps("multiplica pelo", "i", 76, CLARO) + [("de baixo", "g", 76, BR)], 1000, 630, "left", 0.15)
            E.frase(c, t, d15 + 2.0, [("96 ÷ 4 × 5 = 120", "g", 84, BR)], W / 2, 870, "center")
        E.saida(c, t, C["s16"] - 0.1, regra)

    if C["s16"] <= t:
        E.frase(c, t, a16, ps("funciona quando a % vira", "i", 76, CLARO) + [("fração simples", "g", 76, BR)], W / 2, 190, "center", 0.12)
        for i, (p, n, d) in enumerate((("25%", 1, 4), ("50%", 1, 2), ("75%", 3, 4))):
            x = 480 + i * 480
            ti = b16 + i * 0.5
            cen(c, t, ti, p + " =", x - 60, 470, 96, BR)
            E.foco(c, t, ti + 0.2, 0.45, lambda a, x=x, n=n, d=d: E.fracao(c, n, d, x + 150, 430, 90, CLARO, a))
        E.frase(c, t, c16, [("17%?", "g", 110, BR)], 640, 800, "center")
        if t >= c16 + 0.9:
            E.risco(c, 520, 820, 760, 720, t, c16 + 0.9, largura=12)
        E.foco(c, t, d16, 0.5, lambda a: E.pilula(c, "÷ 0,83", 1180, 770, 84, "g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    t0 = C["s18.a"]
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s17"] + 0.6, [("conta de luz", "g", 72)], XE + 470, 170)
    sobe = ease_io(prog(t, C["s18"] - 0.2, 0.8))
    yy, k = lerp(520, 400, sobe), lerp(1.0, 0.78, sobe)
    grupo(c, W / 2, 520, k, lambda: (c.translate(0, (yy - 520) / k),
                                     fluxo(c, t, 520, "?", "+ 12%", "R$ 168", c17, a17, b17, rot=("antes", "veio"))))
    E.saida(c, t, C["s18"] - 0.2, lambda: E.frase(c, t, c17 + 0.2, ps("quanto era", "i", 84) + [("antes do aumento?", "g", 80, COR)], W / 2, 850, "center", 0.14))
    E.relogio(c, t, t0, 960, 720, 130)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    a21, b21 = C["s21.a"], C["s21.b"]
    k, yf = 0.6, 210

    def topo():
        fluxo(c, t, 470, [(C["s19"], "?"), (d20, "R$ 150")], [(C["s19"], "+ 12%"), (a19, "× 1,12")], "R$ 168", C["s19"], C["s19"], C["s19"],
              rot=("antes", "veio"))
        volta(c, t, b19 - 0.3, XA, XD, 570, "÷ 1,12", alto=110)
    grupo(c, W / 2, 470, k, lambda: (c.translate(0, (yf - 470) / k), topo()))

    def expr():
        s, y = 112, 560
        cl = E.casa(s)
        xa = 400
        xd = xa + 5 * cl + 60
        xb = xd + 70
        E.foco(c, t, b19, 0.45, lambda q: E.anda(c, t, "168", 3, [(c19 + 0.3, 5)], xa, y, s, tv=c19, some=True))
        cen(c, t, b19 + 0.4, "÷", xd, y, 100, TINTA2)
        E.foco(c, t, b19 + 0.7, 0.45, lambda q: E.anda(c, t, "112", 1, [(c19 + 0.3, 3)], xb, y, s, some=True))
        if t < c19 + 0.3:
            E.saida(c, t, c19 + 0.1, lambda: (E.chave(c, xb + cl - 4, xb + 3 * cl + 4, y + 40, COR, ep(t, c19 - 0.4, 0.4), 24, 6),
                                              cen(c, t, c19 - 0.3, "2 casas", xb + 2 * cl, y + 140, 56, COR)))
    E.saida(c, t, a20 - 0.1, expr)

    def conta():
        D = E.dividir("16800", 112)
        E.conta_div(c, t, D, [a20 + 1.6, lerp(b20, c20, 0.6), c20 + 1.5], [b20 + 0.4, c20 + 0.4, c20 + 1.7], a20, 520, 520, 100,
                    ts=[a20 + 2.6, lerp(b20, c20, 0.8)])
        E.foco(c, t, d20, 0.5, lambda a: num_bola(c, "R$ 150", 1580, 800, 150, 84, a))
    E.saida(c, t, C["s21"] - 0.1, conta)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.1, ps("confira", "i", 80, COR), W / 2, 450, "center")
    E.frase(c, t, a21, [("12% de 150", "g", 90), ("=", "g", 90, TINTA2), ("18", "g", 90, COR)], W / 2, 620, "center", 0.3)
    E.frase(c, t, b21, [("150 + 18", "g", 90), ("=", "g", 90, TINTA2), ("168", "g", 90, CERTO)], W / 2, 790, "center", 0.3)
    E.foco(c, t, b21 + 1.3, 0.45, lambda a: E.selo(c, 1420, 760, 60, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a22, b22, c22 = C["s22.a"], C["s22.b"], C["s22.c"]

    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        E.frase(c, t, a22, [("agora", "g", 130), ("÷", "g", 110, TINTA2), ("fator", "g", 130, COR)], 1020, 470, "right", 0.3)
        E.frase(c, t, b22, [("=", "g", 110, TINTA2), ("antes", "g", 130)], 1080, 470, "left", 0.3)
        E.frase(c, t, c22, [("nunca", "g", 84, ERRADO)] + ps("faça a % sobre", "i", 84), W / 2, 700, "center", 0.14)
        E.frase(c, t, c22 + 1.0, [("o preço de agora", "g", 84, ERRADO)], W / 2, 820, "center", 0.14)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a23, b23, c23, d23, e23 = C["s23.a"], C["s23.b"], C["s23.c"], C["s23.d"], C["s23.e"]
    E.frase(c, t, C["s23"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, a23 - 0.6, [("Lucro sobre o custo", "g", 112, COR)], XE, 450)
    E.frase(c, t, a23 - 0.3, [("e sobre a venda", "g", 112, COR)], XE, 580)
    E.frase(c, t, b23, [("R$ 20 de lucro:", "i", 76), ("25%", "g", 76, COR), ("ou", "i", 76), ("20%?", "g", 76, COR)], XE, 740, "left", 0.2)
    E.foco(c, t, d23, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=a))
    p = ease_io(prog(t, d23 + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, d23 + 0.2, 0.4))
    E.frase(c, t, e23, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, maquina=b_maquina, conta=b_conta, regra=b_regra, aumento=b_aumento,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
