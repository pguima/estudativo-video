"""Visual — Estudativo · MAT-POR-009: praticando porcentagem, aumentos e lucro (aula de prática).

Cinco situações, cada uma com selo de progresso, relógio de pausa e resposta passo a passo, na linguagem da trilha
Porcentagem (MAT-POR-006): cartao() = valor de antes (contorno escuro) ou de depois (cor da matéria); maquina() = o fator
ou a mudança; fluxo() = antes → [máquina] → depois; volta() = a conta inversa por baixo. Todo instante vem de C[...]."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia
from fractions import Fraction as Fr

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-009_praticando_porcentagem_aumentos_lucro.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "atalho", "questao3", "questao5", "fim"))
BR = "#FFFFFF"
assert round(2400 * 0.85, 6) == 2040 and 240 + 120 == 360 and 2400 - 360 == 2040
assert 1400 - 1250 == 150 and Fr(150, 1250) == Fr(3, 25) == Fr(12, 100)
assert round(117 / 0.65, 6) == 180 and 11700 / 65 == 180 and 117 - 65 == 52 and 520 / 65 == 8 and round(117 * 1.35, 2) == 157.95
assert 4 - 2.5 == 1.5 and Fr(15, 25) == Fr(3, 5) and 1.5 / 4 == 0.375
assert Fr(2, 5) == Fr(40, 100) and round(200 / 3) == 67


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


# ---------------- peças da prática ----------------
def marca(c, t, t0, n, escuro=False):
    """situação n de 5, com cinco pontos de progresso"""
    s = f"situação {n} de 5"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", a=a)
        for i in range(5):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def selo_em(c, t, t0, cx, cy, r=50, ok=True):
    E.foco(c, t, t0, 0.45, lambda p: E.selo(c, cx, cy, r, ok, p))


def topo(c, t, fn, y=470, yf=270, k=0.62):
    """o fluxo da questão, pequeno no alto durante a resposta"""
    grupo(c, W / 2, y, k, lambda: (c.translate(0, (yf - y) / k), fn()))


def questao(c, t, C, cena, pausa, fn, pergunta):
    """fluxo grande; na pausa, o fluxo sobe e o relógio aparece embaixo"""
    sobe = ease_io(prog(t, C[pausa] - 0.2, 0.8))
    k = lerp(1.0, 0.8, sobe)
    grupo(c, W / 2, 470, k, lambda: (c.translate(0, -sobe * 90 / k), fn()))
    E.saida(c, t, C[pausa] - 0.2, pergunta)
    E.relogio(c, t, C[pausa + ".a"], 960, 780, 120)


def pacote(c, cx, cy, s, a=1.0, gratis=0.0, preco=None):
    """um pacote com fita; gratis 0..1: vira contorno tracejado com "grátis" (saiu de graça)"""
    if a <= 0:
        return
    w, h = s, s * 1.1
    x, y = cx - w / 2, cy - h / 2
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 16, 16)
    cheio = a * (1 - gratis)
    if cheio > 0:
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeLinear([skia.Point(x, y), skia.Point(x + w, y + h)],
                                                   [M.hexc(E.mix(E.COR, BR, 0.18), cheio), M.hexc(E.mix(E.COR, "#000000", 0.2), cheio)]))
        c.drawRRect(rr, p)
        c.drawRect(skia.Rect.MakeXYWH(cx - w * 0.09, y, w * 0.18, h), M.paint(BR, 0.35 * cheio))
        M.line(c, x + 10, y + h * 0.22, x + w - 10, y + h * 0.22, BR, 0.3 * cheio, 3)
    if gratis > 0:
        pt = M.paint(COR, a * gratis, stroke=4)
        pt.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
        path = skia.Path(); path.addRRect(rr)
        c.drawPath(path, pt)
        centro(c, "grátis", cx, cy + s * 0.08, s * 0.22, "g", COR, a * gratis)


def fila(c, t, t0, n, cx, cy, s, gap=40, tg=None, ng=1, passo_=0.15):
    """n pacotes lado a lado; os ng últimos saem de graça em tg"""
    x0 = cx - (n * s + (n - 1) * gap) / 2 + s / 2
    for i in range(n):
        g = ep(t, tg, 0.5) if (tg is not None and i >= n - ng) else 0.0
        E.foco(c, t, t0 + i * passo_, 0.45, lambda a, i=i, g=g: pacote(c, x0 + i * (s + gap), cy, s, a, g))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]
    E.frase(c, t, a_ + 0.1, ps("5", "g", 240, COR) + ps("situações", "g", 170, COR), XE, 350, passo=0.25)
    E.frase(c, t, a_ + 0.8, ps("de compra e venda, criadas para esta aula", "i", 76), XE, 480, passo=0.1)
    for i, (s, cx) in enumerate((("pause", 440), ("resolva", 960), ("confira", 1480))):
        E.foco(c, t, b_ + i * 0.5, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 700, 56, 64, p), E.escreve(c, s, cx - 110, 725, 92, "g", TINTA, p)))
    E.frase(c, t, lerp(b_, C["s01.end"], 0.55), ps("errar aqui não custa nada, e ensina", "i", 70, TINTA2), W / 2, 920, "center", 0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.3, ps("quatro", "g", 84, COR) + ps("ferramentas", "i", 90), XE, 170)
    itens = (("fatores de aumento e desconto", "× 1,15   × 0,8"), ("a parte dividida pelo total", "parte ÷ total"),
             ("o preço de antes", "agora ÷ fator"), ("lucro sobre o custo ou a venda", "lucro ÷ total"))
    for i, ((txt_, ex), k) in enumerate(zip(itens, "abcd")):
        y = 330 + i * 165
        tk = C[f"s02.{k}"]
        E.foco(c, t, tk, 0.45, lambda p, i=i, y=y: num_bola(c, str(i + 1), XE + 40, y - 25, 40, 50, p))
        E.frase(c, t, tk, ps(txt_, "i", 66), XE + 110, y, passo=0.08)
        E.foco(c, t, tk + 0.4, 0.45, lambda a, ex=ex, y=y: E.escreve(c, ex, 1220, y, 64, "g", COR, a))
    E.frase(c, t, C["s02.end"] - 2.6, ps("travou? procure a aula no canal", "i", 54, TINTA2), 1250, 170, passo=0.08)


# ---------------- situação 1: desconto ----------------
def b_questao1(c, t, C, b):
    a3, b3, c3, d3 = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.d"]
    marca(c, t, a3, 1)
    questao(c, t, C, "s03", "s04",
            lambda: fluxo(c, t, 470, "R$ 2.400", "− 15%", "?", b3, c3, d3, rot=("geladeira", "à vista")),
            lambda: E.frase(c, t, d3 + 0.2, ps("quanto você paga", "i", 84) + [("à vista?", "g", 84, COR)], W / 2, 820, "center", 0.14))


def b_resposta1(c, t, C, b):
    marca(c, t, C["s05"] - 0.5, 1)
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    topo(c, t, lambda: fluxo(c, t, 470, "R$ 2.400", [(C["s05"], "− 15%"), (a5, "× 0,85")], [(C["s05"], "?"), (c5 + 0.6, "R$ 2.040")],
                              C["s05"], C["s05"], C["s05"], rot=("geladeira", "à vista")))
    E.frase(c, t, C["s05"] + 0.3, ps("tirar 15% é ficar com", "i", 76) + [("85%", "g", 80, COR)], W / 2, 500, "center", 0.12)
    E.frase(c, t, a5, ps("fator", "i", 80) + [("0,85", "g", 90, COR)], W / 2, 620, "center", 0.15)
    E.frase(c, t, b5, [("2.400 × 0,85", "g", 100), ("=", "g", 100, TINTA2)], 1080, 840, "right", 0.25)
    E.foco(c, t, c5, 0.5, lambda a: num_bola(c, "R$ 2.040", 1350, 810, 170, 72, a))
    selo_em(c, t, c5 + 0.8, 1560, 690, 44)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]

    def seis():
        E.frase(c, t, C["s06"] + 0.1, [("o atalho:", "g", 70, BR)] + ps("de cabeça", "i", 74, CLARO), W / 2, 150, "center", 0.15)
        E.frase(c, t, a6, [("15%", "g", 110, BR), ("=", "g", 100, CLARO), ("10%", "g", 110, CLARO), ("+", "g", 100, CLARO), ("5%", "g", 110, CLARO)],
                W / 2, 330, "center", 0.25)
        E.frase(c, t, b6, [("10% de 2.400", "g", 80, BR), ("=", "g", 80, CLARO), ("240", "g", 84, CLARO)], XE + 60, 520, "left", 0.25)
        E.frase(c, t, c6, [("5% é a metade", "g", 80, BR), ("=", "g", 80, CLARO), ("120", "g", 84, CLARO)], XE + 60, 640, "left", 0.25)
        E.frase(c, t, d6, [("desconto:", "i", 76, CLARO), ("240 + 120 = 360", "g", 80, BR)], XE + 60, 790, "left", 0.25)
        E.frase(c, t, e6, [("2.400 − 360", "g", 84, BR), ("=", "g", 84, CLARO), ("2.040", "g", 90, CLARO)], XE + 60, 940, "left", 0.25)
    E.saida(c, t, C["s07"] - 0.1, seis)
    if t < C["s07"] - 0.1:
        return
    E.frase(c, t, a7, [("10%", "g", 100, BR)] + ps("é andar a vírgula", "i", 84, CLARO) + [("1 casa", "g", 90, BR)], W / 2, 270, "center", 0.15)
    E.frase(c, t, a7 + 1.4, [("2.400", "g", 90, CLARO), ("→", "g", 90, CLARO), ("240,0", "g", 90, BR)], W / 2, 420, "center", 0.3)
    E.frase(c, t, lerp(a7, b7, 0.6), [("5%", "g", 90, BR)] + ps("é a metade disso", "i", 84, CLARO), W / 2, 560, "center", 0.15)
    E.frase(c, t, b7, [("37%?", "g", 120, BR)], 700, 820, "center")
    if t >= b7 + 1.2:
        E.risco(c, 560, 840, 840, 740, t, b7 + 1.2, largura=12)
    E.foco(c, t, c7, 0.5, lambda a: E.pilula(c, "use o fator", 1230, 785, 80, "g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- situação 2: variação ----------------
def b_questao2(c, t, C, b):
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    marca(c, t, a8, 2)
    questao(c, t, C, "s08", "s09", lambda: fluxo(c, t, 470, "R$ 1.250", "+ ?%", "R$ 1.400", b8, d8, c8, rot=("aluguel antes", "agora")),
            lambda: E.frase(c, t, d8 + 0.2, ps("de quantos por cento", "i", 84) + [("foi o aumento?", "g", 84, COR)], W / 2, 820, "center", 0.14))


def b_resposta2(c, t, C, b):
    marca(c, t, C["s10"] - 0.5, 2)
    a10, b10, c10, d10, e10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s10.e"]
    a11, b11 = C["s11.a"], C["s11.b"]
    topo(c, t, lambda: fluxo(c, t, 470, "R$ 1.250", [(C["s10"], "+ ?%"), (e10 + 0.5, "+ 12%")], "R$ 1.400", C["s10"], C["s10"], C["s10"],
                              rot=("antes", "agora")))

    def conta():
        E.frase(c, t, a10, [("aumento:", "i", 76), ("1.400 − 1.250", "g", 80), ("=", "g", 80, TINTA2), ("150", "g", 84, COR)], W / 2, 450, "center", 0.2)
        y = 770
        E.foco(c, t, b10, 0.5, lambda a: E.fracao(c, 150, "1.250", 420, y, 100, TINTA, a))
        E.foco(c, t, b10 + 1.2, 0.45, lambda a: centro(c, "antes, embaixo", 420, y + 180, 50, "i", COR, a))
        cen(c, t, c10 - 0.3, "=", 640, y + 36, 90, TINTA2)
        E.foco(c, t, c10, 0.5, lambda a: E.fracao(c, 3, 25, 800, y, 100, TINTA, a))
        E.foco(c, t, c10 + 0.2, 0.4, lambda a: E.pilula(c, "÷ 50", 800, y - 170, 44, "g", fundo=TINTA, a=a))
        cen(c, t, d10 - 0.3, "=", 970, y + 36, 90, TINTA2)
        E.foco(c, t, d10, 0.5, lambda a: E.fracao(c, 12, 100, 1140, y, 100, TINTA, a))
        E.foco(c, t, d10 + 0.2, 0.4, lambda a: E.pilula(c, "× 4", 1140, y - 170, 44, "g", fundo=TINTA, a=a))
        cen(c, t, e10 - 0.3, "=", 1320, y + 36, 90, TINTA2)
        E.foco(c, t, e10, 0.5, lambda a: num_bola(c, "12%", 1520, y + 10, 120, 84, a))
    E.saida(c, t, a11 - 0.1, conta)
    if t < a11 - 0.1:
        return
    E.frase(c, t, a11 - 0.6, [("150 ÷ 1.400?", "g", 90)], 760, 520, "center")
    if t >= a11 + 0.6:
        E.risco(c, 470, 540, 1050, 450, t, a11 + 0.6, largura=12)
    E.frase(c, t, a11 + 0.3, ps("usou o", "i", 72) + [("valor novo", "g", 72, ERRADO)], 1440, 520, "center", 0.12)
    E.frase(c, t, lerp(a11, b11, 0.4), ps("o valor de antes é sempre", "i", 76) + [("o 100%", "g", 80, COR)], W / 2, 720, "center", 0.12)
    E.frase(c, t, b11, ps("erro relativo:", "i", 72, TINTA2) + [("erro ÷ medida", "g", 76)], W / 2, 900, "center", 0.15)


# ---------------- situação 3: preço de antes ----------------
def b_questao3(c, t, C, b):
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    marca(c, t, a12, 3)
    questao(c, t, C, "s12", "s13", lambda: fluxo(c, t, 470, "?", "− 35%", "R$ 117", d12, b12, c12, rot=("sem desconto", "saiu por")),
            lambda: E.frase(c, t, d12 + 0.2, ps("qual era o preço", "i", 84) + [("sem desconto?", "g", 84, COR)], W / 2, 820, "center", 0.14))


def b_resposta3(c, t, C, b):
    marca(c, t, C["s14"] - 0.5, 3)
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    a15, b15, c15, d15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]

    def cima():
        fluxo(c, t, 470, [(C["s14"], "?"), (c15 + 0.6, "R$ 180")], [(C["s14"], "− 35%"), (a14, "× 0,65")], "R$ 117", C["s14"], C["s14"], C["s14"],
              rot=("sem desconto", "saiu por"))
        volta(c, t, b14 - 0.3, XA, XD, 570, "÷ 0,65", alto=110)
    topo(c, t, cima, yf=250)

    def expr():
        s, y = 112, 600
        cl = E.casa(s)
        xa = 420
        xd = xa + 5 * cl + 60
        xb = xd + 20
        E.foco(c, t, b14, 0.45, lambda q: E.anda(c, t, "117", 3, [(c14 + 0.3, 5)], xa, y, s, tv=c14, some=True))
        cen(c, t, b14 + 0.4, "÷", xd, y, 100, TINTA2)
        E.foco(c, t, b14 + 0.7, 0.45, lambda q: E.anda(c, t, "65", 0, [(c14 + 0.3, 2)], xb + cl, y, s, some=True))
        E.foco(c, t, b14 + 0.7, 0.45, lambda q: zero_some(c, t, xb + cl, y, s, c14 + 0.5))
    E.saida(c, t, a15 - 0.1, expr)

    def conta():
        D = E.dividir("11700", 65)
        E.conta_div(c, t, D, [a15 + 1.6, lerp(b15, c15, 0.55), c15 + 0.2], [b15 + 0.3, c15, c15 + 0.4], a15, 520, 520, 100,
                    ts=[a15 + 2.6, lerp(b15, c15, 0.8)])
        E.foco(c, t, c15 + 0.6, 0.5, lambda a: num_bola(c, "R$ 180", 1580, 760, 150, 84, a))
    if t >= a15 - 0.1:
        conta()
    E.frase(c, t, d15, [("117 + 35%", "g", 64), ("=", "g", 64, TINTA2), ("R$ 157,95", "g", 64, ERRADO)], XE, 1000, "left", 0.25)
    selo_em(c, t, lerp(d15, C["s15.end"], 0.7), 1020, 975, 40, False)


# ---------------- situação 4: lucro ----------------
def b_questao4(c, t, C, b):
    a16, b16, c16, d16, e16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"]
    marca(c, t, a16, 4)

    def perguntas():
        E.foco(c, t, d16, 0.45, lambda a: E.pilula(c, "margem sobre o custo?", 560, 790, 56, "g", fundo=TINTA, a=a))
        E.foco(c, t, e16, 0.45, lambda a: E.pilula(c, "e sobre a venda?", 1360, 790, 56, "g", a=a))
    questao(c, t, C, "s16", "s17", lambda: fluxo(c, t, 470, "R$ 2,50", "lucro", "R$ 4", b16, c16 + 0.3, c16, rot=("custo do bolo", "venda")), perguntas)


def b_resposta4(c, t, C, b):
    marca(c, t, C["s18"] - 0.5, 4)
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    a19, b19, c19, d19 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    topo(c, t, lambda: fluxo(c, t, 470, "R$ 2,50", [(C["s18"], "lucro"), (a18 + 1.5, "+ R$ 1,50")], "R$ 4", C["s18"], C["s18"], C["s18"],
                              rot=("custo", "venda")))
    E.saida(c, t, d19 - 0.1, lambda: E.frase(c, t, a18, [("lucro:", "i", 70), ("4 − 2,50", "g", 76), ("=", "g", 76, TINTA2), ("1,50", "g", 80, COR)],
                                            W / 2, 470, "center", 0.2))
    E.frase(c, t, d19, ps("mesmo lucro,", "i", 76) + [("totais diferentes", "g", 76, COR)], W / 2, 470, "center", 0.14)
    XL, XR = 520, 1400
    E.foco(c, t, b18 - 0.6, 0.45, lambda a: E.pilula(c, "sobre o custo", XL, 580, 54, "g", fundo=TINTA, a=a))
    E.frase(c, t, b18, [("1,5 ÷ 2,5", "g", 80)], XL, 710, "center")
    E.frase(c, t, c18, [("=", "g", 72, TINTA2), ("15/25", "g", 72), ("=", "g", 72, TINTA2), ("3/5", "g", 72, COR)], XL, 820, "center", 0.25)
    E.foco(c, t, d18, 0.5, lambda a: num_bola(c, "60%", XL, 940, 90, 64, a))
    E.foco(c, t, C["s19"] + 0.2, 0.45, lambda a: E.pilula(c, "sobre a venda", XR, 580, 54, "g", a=a))
    E.frase(c, t, a19, [("1,5 ÷ 4", "g", 80)], XR, 710, "center")
    E.frase(c, t, b19, [("=", "g", 72, TINTA2), ("0,375", "g", 72, COR)], XR, 820, "center", 0.25)
    E.foco(c, t, c19, 0.5, lambda a: num_bola(c, "37,5%", XR, 940, 90, 52, a))


# ---------------- situação 5: promoção ----------------
def b_questao5(c, t, C, b):
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    marca(c, t, a20, 5)
    E.frase(c, t, a20 + 0.8, ps("você precisa de", "i", 70) + [("5 latas de tinta", "g", 70, COR)], W / 2, 240, "center", 0.12)

    def lojas():
        E.foco(c, t, b20, 0.45, lambda a: E.pilula(c, "leve 5, pague 3", 560, 380, 60, "g", a=a))
        fila(c, t, b20 + 0.3, 5, 560, 560, 110, 24, b20 + 1.4, ng=2)
        E.foco(c, t, c20, 0.45, lambda a: E.pilula(c, "45% de desconto", 1400, 380, 60, "g", fundo=TINTA, a=a))
        E.foco(c, t, c20 + 0.4, 0.5, lambda a: num_bola(c, "− 45%", 1400, 570, 130, 76, a, TINTA))
    questao(c, t, C, "s20", "s21", lojas,
            lambda: E.frase(c, t, d20, ps("qual", "i", 84) + [("compensa mais?", "g", 84, COR)], W / 2, 860, "center", 0.14))


def b_resposta5(c, t, C, b):
    marca(c, t, C["s22"] - 0.5, 5)
    a22, b22, c22, d22, e22 = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"], C["s22.e"]
    fila(c, t, C["s22"] + 0.2, 5, W / 2, 300, 120, 30, a22, ng=2)
    E.frase(c, t, a22 + 0.3, ps("2 de graça em 5", "i", 76), W / 2, 480, "center", 0.12)
    E.frase(c, t, b22, [("2/5", "g", 90, COR), ("=", "g", 90, TINTA2), ("40%", "g", 90, COR)], W / 2, 610, "center", 0.25)
    E.frase(c, t, c22, [("40%", "g", 90), ("<", "g", 90, TINTA2), ("45%", "g", 90, CERTO)], 560, 760, "center", 0.25)
    E.frase(c, t, d22, ps("o desconto de", "i", 66) + [("45% compensa mais", "g", 66, CERTO)], 1340, 760, "center", 0.12)
    E.frase(c, t, e22, [("dividir pelas 3 pagas:", "i", 64, TINTA2), ("2/3", "g", 66), ("≈", "g", 66, TINTA2), ("67%", "g", 66, ERRADO)], W / 2, 940, "center", 0.2)
    selo_em(c, t, lerp(e22, C["s22.end"], 0.6), 1500, 915, 40, False)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s23.a", "o total certo antes de dividir"), ("s23.b", "o fator para ir e voltar"), ("s23.c", "a resposta faz sentido?"))):
            y = 400 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 330, y - 30, 56, 64, a))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 80)], 430, y)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    a24, b24, c24, d24 = C["s24.a"], C["s24.b"], C["s24.c"], C["s24.d"]
    E.frase(c, t, C["s24"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, a24 - 0.4, [("Aumentos e descontos", "g", 104, COR)], XE, 450)
    E.frase(c, t, a24, [("sucessivos", "g", 104, COR)], XE, 580)
    E.frase(c, t, b24, [("10% e depois 20%", "g", 76)] + ps("não dão", "i", 80) + [("30%", "g", 76, ERRADO)], XE, 740, "left", 0.15)
    E.foco(c, t, c24, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=a))
    p = ease_io(prog(t, c24 + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, c24 + 0.2, 0.4))
    E.frase(c, t, d24, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, atalho=b_atalho,
              questao2=b_questao2, resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3,
              questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
