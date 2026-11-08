"""Visual — Estudativo · MAT-POR-007: lucro sobre o custo e sobre a venda.

Mesma linguagem da trilha Porcentagem (MAT-POR-006): cartao() = valor de antes (custo, contorno escuro) ou de depois (venda,
cor da matéria); maquina() = a mudança ou o fator numa caixa cheia da cor; fluxo() = antes → [máquina] → depois; volta() = conta
inversa por baixo. Aqui o custo ocupa o lugar do "antes" e a venda o do "depois". Todo instante vem de C[...]."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-007_lucro_sobre_custo_e_sobre_venda.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("sobre", "margem", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 100 - 80 == 20 and 20 / 80 == 0.25 and 20 / 100 == 0.2 and 80 - 60 == 20
assert round(70 * 1.3, 6) == 91 and round(70 / 0.7, 6) == 100 and 700 / 7 == 100 and 100 - 70 == 30 and 30 / 100 == 0.3
assert 91 - 70 == 21 and round(21 / 91, 2) == 0.23
assert round(120 / 0.6, 6) == 200 and 1200 / 6 == 200 and 200 - 120 == 80 and 0.4 * 200 == 80 and round(120 * 1.4, 6) == 168


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
    ka, kb, kc, kd, ke = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"], C["s01.e"]

    def um():
        fluxo(c, t, 380, "R$ 80", "+ R$ 20", "R$ 100", ka, kc, kb, rot=("comprou", "vendeu"))
        E.frase(c, t, lerp(kc, kd, 0.45), ps("lucro de quantos", "i", 80) + [("por cento?", "g", 80, COR)], W / 2, 150, "center", 0.12)
        for x, s, ti in ((660, "25%", kd), (1260, "20%", ke)):
            E.foco(c, t, ti, 0.5, lambda a, x=x, s=s: num_bola(c, s, x, 760, 130, 96, a))
            E.foco(c, t, lerp(ke, C["s01.end"], 0.45) + (0 if x < 900 else 0.25), 0.45, lambda a, x=x: E.selo(c, x + 115, 660, 46, True, a))
        E.frase(c, t, lerp(ke, C["s01.end"], 0.45), ps("e ninguém", "i", 76) + [("errou", "g", 76, CERTO)], W / 2, 990, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.15), ps("de onde sai", "i", 90) + [("cada número", "g", 96, COR)], XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), [("o preço", "g", 96, COR)] + ps("que dá", "i", 90), XE, 620, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.65), ps("o lucro que você quer", "i", 90), XE, 760, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "quantos por cento:", "parte ÷ total"), ("s03.c", "o preço de antes:", "agora ÷ fator"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 260 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 210, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 88)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 70, COR)], x + 44, y + 176)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(440, 730, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- três nomes ----------------
def b_nomes(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    E.frase(c, t, C["s04"] + 0.1, ps("primeiro,", "i", 80) + [("três nomes", "g", 80, COR)], W / 2, 170, "center", 0.14)
    fluxo(c, t, 450, "R$ 80", [(c4, "lucro"), (d4 + 0.6, "+ R$ 20")], "R$ 100", a4, c4, b4, rot=("custo", "venda"))
    E.frase(c, t, a4 + 0.4, ps("você pagou", "i", 54, TINTA2), XA, 590, "center", 0.1)
    E.frase(c, t, b4 + 0.4, ps("você recebeu", "i", 54, TINTA2), XD, 590, "center", 0.1)
    E.frase(c, t, c4 + 0.3, [("lucro", "g", 90, COR), ("=", "g", 90, TINTA2), ("venda", "g", 90), ("−", "g", 90, TINTA2), ("custo", "g", 90)],
            W / 2, 790, "center", 0.25)
    E.frase(c, t, d4, [("100 − 80", "g", 84), ("=", "g", 84, TINTA2), ("R$ 20", "g", 84, COR)], W / 2, 940, "center", 0.3)


# ---------------- sobre o custo e sobre a venda ----------------
XL, XR = 520, 1400


def coluna(c, t, cx, nome, td, n, d, dec, pct, th, tc, tp, cor_pct=None):
    """uma coluna: o total da vez, a fração lucro/total, o decimal e a porcentagem"""
    E.foco(c, t, th, 0.45, lambda a: E.pilula(c, nome, cx, 320, 58, "g", fundo=TINTA if "custo" in nome else E.COR, a=a))
    E.foco(c, t, td, 0.5, lambda a: E.fracao(c, n, d, cx - 170, 500, 104, TINTA, a))
    cen(c, t, tc, "= " + dec, cx + 130, 540, 90, TINTA2)
    E.foco(c, t, tp, 0.5, lambda a: num_bola(c, pct, cx, 760, 120, 96, a))


def b_sobre(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]

    def colunas():
        E.frase(c, t, C["s05"] + 0.1, [("lucro", "g", 80, COR), ("÷", "g", 80, TINTA2), ("total", "g", 80)], 1040, 170, "right", 0.25)
        E.frase(c, t, a5, [("qual total?", "i", 76, TINTA2)], 1110, 170)
        coluna(c, t, XL, "sobre o custo", b5, 20, 80, "0,25", "25%", lerp(a5, b5, 0.5), b5 + 1.2, c5)
        coluna(c, t, XR, "sobre a venda", a6, 20, 100, "0,20", "20%", a6 - 0.6, a6 + 1.2, b6)
        if t >= c6:
            for cx in (XL, XR):
                q = ep(t, c6 + 0.3, 0.5)
                E.caixa_pontilhada(c, cx - 275, 520, 210, 110, q, COR, prog_=q)
        E.saida(c, t, a7 - 0.1, lambda: E.frase(c, t, c6, ps("a palavra depois de", "i", 66) + [("sobre", "g", 66, COR)] + ps("vai embaixo", "i", 66),
                                               W / 2, 970, "center", 0.12))
        E.frase(c, t, a7, [("sobre o custo dá mais:", "i", 66)] + [("o custo é menor", "g", 66, COR)], W / 2, 970, "center", 0.16)
    E.saida(c, t, b7 - 0.1, colunas)
    if t < b7 - 0.1:
        return
    fluxo(c, t, 450, "R$ 80", "− R$ 20", "R$ 60", b7, b7 + 1.0, b7 + 0.5, rot=("comprou", "vendeu"))
    E.frase(c, t, b7, ps("venda", "i", 80) + [("abaixo do custo", "g", 80)], W / 2, 170, "center", 0.14)
    E.foco(c, t, c7, 0.5, lambda a: E.pilula(c, "prejuízo", W / 2, 690, 72, "g", fundo=TINTA, a=a))
    E.frase(c, t, d7 + 1.5, [("20 ÷ 80", "g", 80), ("=", "g", 80, TINTA2), ("25%", "g", 80, COR)] + ps("sobre o custo", "i", 76),
            W / 2, 900, "center", 0.25)


# ---------------- preço com margem ----------------
def b_margem(c, t, C, b):
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    a11, b11, c11, d11, e11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"]

    def pergunta():
        E.frase(c, t, C["s08"] + 0.1, ps("e o caminho", "i", 80) + [("inverso?", "g", 80, COR)], W / 2, 170, "center", 0.14)
        fluxo(c, t, 450, "R$ 70", "30%", "?", a8, b8, d8, rot=("custo", "venda"))
        E.foco(c, t, b8, 0.45, lambda a: centro(c, "margem de lucro", XM, 330, 58, "i", COR, a))
        E.frase(c, t, c8, [("margem de lucro", "g", 70, COR), ("=", "g", 70, TINTA2)] + ps("o lucro em por cento", "i", 70), W / 2, 760, "center", 0.12)
        E.frase(c, t, d8 + 0.3, ps("por quanto", "i", 84) + [("vender?", "g", 84, COR)], W / 2, 920, "center", 0.14)
    E.saida(c, t, a9 - 0.1, pergunta)
    if t < a9 - 0.1:
        return

    def contas():
        # sobre o custo: aumento de 30% no custo
        E.foco(c, t, a9, 0.45, lambda a: E.pilula(c, "sobre o custo", XL, 200, 58, "g", fundo=TINTA, a=a))
        E.frase(c, t, a9 + 0.6, ps("aumento de 30% no custo", "i", 54, TINTA2), XL, 320, "center", 0.08)
        maquina(c, t, b9, XL, 450, "× 1,3", 80)
        E.frase(c, t, c9, [("70 × 1,3", "g", 80), ("=", "g", 80, TINTA2), ("91", "g", 80, COR)], XL, 650, "center", 0.25)
        # sobre a venda: o custo é 70% da venda
        E.foco(c, t, a10, 0.45, lambda a: E.pilula(c, "sobre a venda", XR, 200, 58, "g", a=a))
        E.frase(c, t, a10 + 0.6, ps("lucro = 30% da venda", "i", 54, TINTA2), XR, 320, "center", 0.08)
        E.frase(c, t, b10, [("custo", "g", 72), ("=", "g", 72, TINTA2), ("70%", "g", 72, COR)] + ps("da venda", "i", 66), XR, 450, "center", 0.2)
        E.frase(c, t, c10, [("70 ÷ 0,7", "g", 80)], XR, 565, "center")
        E.frase(c, t, d10, [("700 ÷ 7", "g", 80), ("=", "g", 80, TINTA2), ("100", "g", 80, COR)], XR, 670, "center", 0.25)
    E.saida(c, t, a11 - 0.1, contas)
    E.saida(c, t, d11 - 0.1, lambda: (cartao(c, t, c9 + 1.2, XL, 860, "R$ 91", "venda", True, 84),
                                      cartao(c, t, d10 + 1.2, XR, 860, "R$ 100", "venda", True, 84)))
    if t < a11 - 0.1:
        return

    def confere():
        E.frase(c, t, a11, [("lucro:", "i", 70), ("100 − 70 = 30", "g", 72)], XR, 330, "center", 0.2)
        E.frase(c, t, b11, [("30 ÷ 100", "g", 68), ("=", "g", 68, TINTA2), ("30%", "g", 68, CERTO)], XR - 40, 480, "center", 0.25)
        E.foco(c, t, b11 + 1.6, 0.45, lambda a: E.selo(c, XR + 300, 457, 42, True, a))
        E.frase(c, t, c11, ps("a mesma", "i", 76) + [("margem de 30%", "g", 76, COR)], XL, 400, "center", 0.12)
        E.frase(c, t, c11 + 0.8, ps("deu 91", "i", 76) + [("ou", "i", 76)] + ps("100", "i", 76), XL, 510, "center", 0.12)
        for x in (XL, XR):
            q = ep(t, c11 + 1.2, 0.5)
            E.caixa_pontilhada(c, x - 220, 740, 440, 210, q, COR, prog_=q)
    E.saida(c, t, d11 - 0.1, confere)
    if t < d11 - 0.1:
        return
    E.frase(c, t, d11, ps("na prova, procure:", "i", 80), W / 2, 180, "center", 0.14)
    E.frase(c, t, d11 + 0.6, [("sobre o custo", "g", 76), ("ou", "i", 80), ("sobre a venda?", "g", 76, COR)], W / 2, 330, "center", 0.25)
    E.frase(c, t, e11, ps("não disse?", "i", 66, TINTA2) + ps("o mais comum é", "i", 66) + [("sobre o custo", "g", 62)], W / 2, 520, "center", 0.12)
    E.frase(c, t, lerp(e11, C["s11.end"], 0.55), [("não é regra:", "g", 60, ERRADO)] + ps("leia o enunciado inteiro", "i", 64), W / 2, 640, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    E.frase(c, t, C["s12"] + 0.1, [("o erro", "g", 96, ERRADO)] + ps("comum", "i", 96), W / 2, 170, "center", 0.14)
    E.frase(c, t, a12, ps("fator de aumento", "i", 66) + [("quando pede sobre a venda", "g", 62, ERRADO)], W / 2, 300, "center", 0.12)
    fluxo(c, t, 520, "R$ 70", "× 1,3", "R$ 91", b12 - 0.6, b12 - 0.3, b12, rot=("custo", "venda"), size=84, cor_d=ERRADO)
    E.frase(c, t, c12, [("lucro 21:", "i", 70), ("21 ÷ 91", "g", 76), ("≈", "g", 76, TINTA2), ("23%", "g", 76, ERRADO)], W / 2, 790, "center", 0.25)
    E.frase(c, t, d12, ps("não chega aos", "i", 80) + [("30%", "g", 80, ERRADO)], W / 2, 940, "center", 0.14)
    E.foco(c, t, d12 + 0.8, 0.45, lambda a: E.selo(c, 1440, 910, 48, False, a))


# ---------------- atalho (palco escuro) ----------------
PX, PY, PW, PH = 360, 480, 1200, 150


def partes(c, t, n, cores, a=1.0, nums=None, ta=None, vis=None):
    """barra de n partes no palco: cores[i] = cor cheia ou None (só o contorno); nums = texto dentro, que entra em ta.
    vis[i] = opacidade de cada parte (para uma parte entrar depois)"""
    if a <= 0:
        return
    w = PW / n
    a0 = a
    for i in range(n):
        a = a0 * (vis[i] if vis else 1.0)
        if a <= 0:
            continue
        x = PX + i * w
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 6, PY, w - 12, PH), 18, 18)
        if cores[i]:
            c.drawRRect(r, M.paint(cores[i], a))
        c.drawRRect(r, M.paint(CLARO, a, stroke=4))
        if nums and ta is not None:
            E.foco(c, t, ta + 0.08 * i, 0.4, lambda q, x=x, i=i: centro(c, nums, x + w / 2, PY + PH / 2 + 28, 78, "g", "#07070F" if cores[i] in (CLARO, BR) else BR, q * a))


def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13, d13, e13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
    a14, b14, c14, d14, e14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"]

    def barra():
        E.frase(c, t, C["s13"] + 0.1, [("o atalho:", "g", 64, BR)] + ps("pense em partes", "i", 68, CLARO), W / 2, 110, "center", 0.15)
        E.frase(c, t, b13, [("20", "g", 100, BR), ("=", "g", 90, CLARO)], 820, 300, "right", 0.25)
        E.foco(c, t, b13 + 0.5, 0.45, lambda a: E.fracao(c, 1, 4, 920, 262, 88, CLARO, a))
        E.frase(c, t, b13 + 0.8, ps("do custo de 80", "i", 76, CLARO), 1000, 300, "left", 0.12)
        cores = [CLARO] * 4 + [BR if t >= d13 else None]
        partes(c, t, 5, cores, ep(t, c13, 0.5), "20", c13 + 0.4, vis=[1, 1, 1, 1, ep(t, d13, 0.5)])
        E.chave(c, PX + 6, PX + PW * 0.8 - 6, PY + PH + 22, CLARO, ep(t, c13 + 0.3, 0.4), 24, 6)
        E.foco(c, t, c13 + 0.4, 0.4, lambda a: centro(c, "custo: 4 partes", PX + PW * 0.4, PY + PH + 100, 54, "i", CLARO, a))
        E.foco(c, t, d13 + 0.2, 0.4, lambda a: centro(c, "lucro: 1", PX + PW * 0.9, PY + PH + 100, 54, "i", BR, a))
        E.chave(c, PX + 6, PX + PW - 6, PY - 22, BR, ep(t, e13, 0.4), -24, 6)
        E.foco(c, t, e13 + 0.2, 0.4, lambda a: centro(c, "venda: 5 partes", PX + PW / 2, PY - 70, 54, "g", BR, a))
        E.frase(c, t, a14, [("sobre o custo:", "i", 70, CLARO), ("1 de 4", "g", 76, BR), ("=", "g", 76, CLARO), ("25%", "g", 80, CLARO)], W / 2, 870, "center", 0.25)
        E.frase(c, t, b14, [("sobre a venda:", "i", 70, CLARO), ("1 de 5", "g", 76, BR), ("=", "g", 76, CLARO), ("20%", "g", 80, CLARO)], W / 2, 990, "center", 0.25)
    E.saida(c, t, c14 - 0.1, barra)
    if t < c14 - 0.1:
        return
    E.frase(c, t, c14, ps("o lucro é", "i", 84, CLARO) + [("o mesmo,", "g", 84, BR)], W / 2, 300, "center", 0.15)
    E.frase(c, t, c14 + 1.0, ps("só muda", "i", 84, CLARO) + [("o total", "g", 84, BR)], W / 2, 420, "center", 0.15)
    E.frase(c, t, d14, [("23%?", "g", 120, BR)], 700, 760, "center")
    if t >= d14 + 1.2:
        E.risco(c, 560, 780, 840, 680, t, d14 + 1.2, largura=12)
    E.foco(c, t, e14, 0.5, lambda a: E.pilula(c, "aí, divida", 1220, 725, 80, "g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s15"] + 0.6, [("tênis", "g", 72)], XE + 470, 170)
    sobe = ease_io(prog(t, C["s16"] - 0.2, 0.8))
    yy, k = lerp(500, 380, sobe), lerp(1.0, 0.78, sobe)

    def linha():
        fluxo(c, t, 500, "R$ 120", "lucro 40%", "?", a15, b15, c15, rot=("custo", "venda"))
        E.foco(c, t, b15 + 0.9, 0.45, lambda a: E.pilula(c, "sobre a venda", XM, 650, 50, "g", fundo=TINTA, a=a))
    grupo(c, W / 2, 500, k, lambda: (c.translate(0, (yy - 500) / k), linha()))
    E.saida(c, t, C["s16"] - 0.2, lambda: E.frase(c, t, c15 + 0.2, ps("por quanto deve", "i", 84) + [("vender?", "g", 84, COR)], W / 2, 880, "center", 0.14))
    E.relogio(c, t, C["s16.a"], 960, 720, 130)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, C["s17"] + 0.2, ps("lucro = 40% da venda, então", "i", 70), W / 2, 150, "center", 0.1)
    E.frase(c, t, a17, [("custo", "g", 84), ("=", "g", 84, TINTA2), ("60%", "g", 84, COR)] + ps("da venda", "i", 80), W / 2, 270, "center", 0.2)
    s, y = 120, 480
    cl = E.casa(s)
    xa = 330
    xd = xa + 4 * cl + 60
    xb = xd + 20
    E.foco(c, t, b17, 0.45, lambda q: E.anda(c, t, "120", 3, [(c17 + 0.2, 4)], xa, y, s, tv=c17 - 0.2, some=True))
    cen(c, t, b17 + 0.5, "÷", xd, y, 100, TINTA2)
    E.foco(c, t, b17 + 0.9, 0.45, lambda q: E.anda(c, t, "6", 0, [(c17 + 0.2, 1)], xb + cl, y, s, some=True))
    E.foco(c, t, b17 + 0.9, 0.45, lambda q: zero_some(c, t, xb + cl, y, s, c17 + 0.4))
    cen(c, t, c17 + 1.4, "=", xb + 2 * cl + 70, y, 100, TINTA2)
    E.foco(c, t, c17 + 1.8, 0.5, lambda a: num_bola(c, "R$ 200", 1530, y - 40, 140, 80, a))
    E.frase(c, t, a18, [("lucro:", "i", 70), ("200 − 120", "g", 72), ("=", "g", 72, TINTA2), ("80", "g", 72, COR)], XE, 700, "left", 0.2)
    E.frase(c, t, b18, [("40% de 200", "g", 72), ("=", "g", 72, TINTA2), ("80", "g", 72, CERTO)], XE, 820, "left", 0.25)
    E.foco(c, t, b18 + 1.4, 0.45, lambda a: E.selo(c, 900, 795, 44, True, a))
    E.frase(c, t, c18, [("com fator:", "i", 66, TINTA2), ("120 × 1,4", "g", 70), ("=", "g", 70, TINTA2), ("168", "g", 70, ERRADO)], XE, 960, "left", 0.2)
    E.foco(c, t, c18 + 2.0, 0.45, lambda a: E.selo(c, 1020, 935, 44, False, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a19, b19 = C["s19.a"], C["s19.b"]

    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.frase(c, t, a19, [("lucro", "g", 100, COR), ("=", "g", 100, TINTA2), ("venda − custo", "g", 100)], W / 2, 390, "center", 0.25)
        E.foco(c, t, b19, 0.5, lambda a: E.fracao(c, "lucro", "custo ou venda?", W / 2, 640, 96, TINTA, a))
        E.frase(c, t, b19 + 1.6, ps("depende de quem", "i", 70) + [("vai embaixo", "g", 70, COR)], W / 2, 960, "center", 0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    E.frase(c, t, C["s20"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, a20 - 0.6, [("Promoções:", "g", 120, COR)], XE, 450)
    E.frase(c, t, a20, [("leve 3, pague 2", "g", 120, COR)], XE, 590)
    E.frase(c, t, b20, ps("e não é", "i", 80) + [("50%", "g", 80, ERRADO)], XE, 750, "left", 0.15)
    E.foco(c, t, c20, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=a))
    p = ease_io(prog(t, c20 + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, c20 + 0.2, 0.4))
    E.frase(c, t, d20, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nomes=b_nomes, sobre=b_sobre, margem=b_margem, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
