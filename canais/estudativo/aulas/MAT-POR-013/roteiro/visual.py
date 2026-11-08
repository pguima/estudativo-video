"""Visual — Estudativo · MAT-POR-013: praticando variações sucessivas (aula de prática, fim da trilha Porcentagem).

Cinco situações, cada uma com selo de progresso, relógio de pausa e resposta passo a passo, na linguagem da trilha
(MAT-POR-006, 010, 011 e 012): cartao() = antes (contorno escuro) e depois (cor da matéria); maquina() = o fator;
funde() = fatores que se multiplicam; cadeia() = valores seguidos; volta() = conta de volta; cem() = 100 quadradinhos.
manchete() desenha as notícias inventadas da aula. Todo instante vem de C[...]."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-013_praticando_variacoes_sucessivas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "atalho", "questao3", "questao5", "fim"))
BR = "#FFFFFF"
assert round(1.05 * 1.1, 6) == 1.155 and 105 * 11 == 1155 and 5 + 10 + 5 * 10 / 100 == 15.5
assert round(0.7 * 0.8, 6) == 0.56 and 100 * 0.7 == 70 and round(70 * 0.2, 6) == 14 and 70 - 14 == 56
assert round(0.4 * 1.6, 6) == 0.64 and 4 * 16 == 64 and 40 * 0.6 == 24 and 40 + 24 == 64 and 1 / 0.4 == 2.5 and 10 / 4 == 2.5
assert 12 - 9 == 3 and 3 / 12 == 0.25 and 70 * 40 == 2800 and 70 * 40 // 100 == 28


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


def cadeia(c, t, y, valores, fatores, tv, tf, xs=None, rot=None, size=76, cores=None):
    """valor → [fator] → valor → [fator] → valor... na mesma linguagem do fluxo.
    valores/fatores = texto ou [(t0, texto)]; tv/tf = instantes (None = não desenha); rot = rótulo de cada valor.
    O primeiro valor é o de antes (contorno escuro); os outros são depois (cor da matéria)."""
    n = len(valores)
    xs = xs or [lerp(260, W - 260, i / (2 * n - 2)) for i in range(2 * n - 1)]
    ws = []
    for i, v in enumerate(valores):
        if tv[i] is None:
            ws.append(size * 2.9)
            continue
        cor = cores[i] if cores else None
        ws.append(cartao(c, t, tv[i], xs[2 * i], y, v, rot[i] if rot else None, i > 0, size, cor=cor))
    for j, f in enumerate(fatores):
        if tf[j] is None:
            continue
        xm = xs[2 * j + 1]
        wm = maquina(c, t, tf[j], xm, y, f, size * 0.9)
        p = ep(t, tf[j] - 0.1, 0.5)
        if p > 0:
            M.arrow(c, xs[2 * j] + ws[j] / 2 + 14, y, xm - wm / 2 - 14, y, TINTA2, p, 5, 18, p)
            M.arrow(c, xm + wm / 2 + 14, y, xs[2 * j + 2] - ws[j + 1] / 2 - 14, y, TINTA2, p, 5, 18, p)
    return xs


def funde(c, t, t0, t1, x1, x2, y, f1, f2, junto, size=80, sinal_x=True):
    """duas máquinas lado a lado (entram em t0) que deslizam e viram uma só em t1, com o fator multiplicado"""
    xm = (x1 + x2) / 2
    p = ease_io(prog(t, t1, 0.8))
    if p < 1:
        def duas():
            a = 1 - p
            for x, f, d in ((x1, f1, 0), (x2, f2, 0.4)):
                xx = lerp(x, xm, p)
                c.save(); c.translate(0, 0)
                if a < 1:
                    lay = skia.Paint(); lay.setAlphaf(a)
                    c.saveLayer(None, lay)
                maquina(c, t, t0 + d, xx, y, f, size)
                if a < 1:
                    c.restore()
                c.restore()
            if sinal_x and p < 0.3:
                E.foco(c, t, t0 + 0.6, 0.4, lambda q: centro(c, "×", xm, y + size * 0.35, size, "g", TINTA2, q * (1 - p / 0.3)))
        duas()
    if p > 0.5:
        maquina(c, t, t1 + 0.5, xm, y, junto, size * 1.1)


def selo_em(c, t, t0, cx, cy, r=50, ok=True):
    E.foco(c, t, t0, 0.45, lambda p: E.selo(c, cx, cy, r, ok, p))


def topo(c, t, fn, y=470, yf=270, k=0.62):
    """o fluxo da questão, pequeno no alto durante a resposta"""
    grupo(c, W / 2, y, k, lambda: (c.translate(0, (yf - y) / k), fn()))


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


def questao(c, t, C, cena, pausa, fn, pergunta):
    """fluxo grande; na pausa, o fluxo sobe e o relógio aparece embaixo"""
    sobe = ease_io(prog(t, C[pausa] - 0.2, 0.8))
    k = lerp(1.0, 0.8, sobe)
    grupo(c, W / 2, 470, k, lambda: (c.translate(0, -sobe * 90 / k), fn()))
    E.saida(c, t, C[pausa] - 0.2, pergunta)
    E.relogio(c, t, C[pausa + ".a"], 960, 780, 120)


def cem(c, t, t0, x, y, lado, n1, t1, n2=0, t2=None, cor1=None, cor2=None, escuro=False):
    """100 quadradinhos (10 × 10), preenchidos coluna a coluna: n1 na cor da matéria a partir de t1, e n2 deles,
    os primeiros, em escuro a partir de t2. (x, y) = canto de cima à esquerda; lado = tamanho do quadro inteiro"""
    a = ep(t, t0, 0.5)
    if a <= 0:
        return
    passo_ = lado / 10
    q = passo_ * 0.84
    cor1 = cor1 or E.COR
    cor2 = cor2 or ("#FFFFFF" if escuro else TINTA)
    for k in range(100):
        col, lin = divmod(k, 10)
        xx, yy = x + col * passo_, y + lin * passo_
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx, yy, q, q), 4, 4)
        cor, al = ("#3A3A4A" if escuro else FIO), a
        if t1 is not None and k < n1:
            p = ep(t, t1 + k * 0.012, 0.25)
            if p > 0:
                cor = E.mix(cor, cor1, p)
        if t2 is not None and k < n2:
            p = ep(t, t2 + k * 0.03, 0.25)
            if p > 0:
                cor = E.mix(cor1, cor2, p)
        c.drawRRect(r, M.paint(cor, al))


XS5 = [240, 600, 960, 1320, 1680]


def manchete(c, t, t0, txt_, cx, cy, size=66, risca=None):
    """manchete de jornal inventada: faixa escura com o texto; risca = instante em que leva um risco vermelho"""
    w = E.larg(txt_, "g", size) + size * 1.4
    h = size * 1.9

    def fn(a):
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, 10, BR, a, stroke=4, stroke_color=TINTA)
        c.drawRect(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, 18, h), M.paint(TINTA, a))
        centro(c, txt_, cx + 9, cy + size * 0.36, size, "g", TINTA, a)
    E.foco(c, t, t0, 0.5, fn)
    if risca is not None and t >= risca:
        E.risco(c, cx - w / 2 + 30, cy + 30, cx + w / 2 - 30, cy - 30, t, risca, largura=12)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]
    E.frase(c, t, a_ - 0.8, ps("lojas e notícias", "i", 80) + [("adoram porcentagem", "g", 80, COR)], XE, 220, passo=0.12)
    E.frase(c, t, lerp(a_, b_, 0.5), ps("e muitas vezes ela", "i", 80) + [("engana", "g", 80, ERRADO)], XE, 340, passo=0.12)
    E.frase(c, t, b_, ps("5", "g", 200, COR) + ps("situações", "g", 150, COR), XE, 580, passo=0.25)
    for i, (s, cx) in enumerate((("pause", 440), ("resolva", 960), ("confira", 1480))):
        E.foco(c, t, c_ + i * 0.5, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 800, 56, 64, p), E.escreve(c, s, cx - 110, 825, 92, "g", TINTA, p)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.3, ps("quatro", "g", 84, COR) + ps("ferramentas", "i", 90), XE, 170)
    itens = (("variações seguidas", "multiplique os fatores"), ("voltar ao original", "1 ÷ fator"),
             ("diferença de %", "ponto percentual"), ("% de %", "multiplique"))
    for i, ((txt_, ex), k) in enumerate(zip(itens, "abcd")):
        y = 330 + i * 165
        tk = C[f"s02.{k}"]
        E.foco(c, t, tk, 0.45, lambda p, i=i, y=y: num_bola(c, str(i + 1), XE + 40, y - 25, 40, 50, p))
        E.frase(c, t, tk, ps(txt_, "i", 66), XE + 110, y, passo=0.08)
        E.foco(c, t, tk + 0.4, 0.45, lambda a, ex=ex, y=y: E.escreve(c, ex, 1000, y, 64, "g", COR, a))
    E.frase(c, t, C["s02.end"] - 2.6, ps("travou? procure a aula no canal", "i", 54, TINTA2), 1250, 170, passo=0.08)


# ---------------- situação 1 ----------------
def b_questao1(c, t, C, b):
    a3, b3, c3, d3 = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.d"]
    marca(c, t, a3, 1)
    E.frase(c, t, a3 + 0.6, [("conta de água", "g", 64)], 880, 132)

    def maqs():
        maquina(c, t, b3, 640, 470, "+ 5%", 96)
        E.foco(c, t, b3 + 0.3, 0.4, lambda a: centro(c, "1º ano", 640, 340, 58, "i", TINTA2, a))
        maquina(c, t, c3, 1280, 470, "+ 10%", 96)
        E.foco(c, t, c3 + 0.3, 0.4, lambda a: centro(c, "2º ano", 1280, 340, 58, "i", TINTA2, a))
        p = ep(t, c3 + 0.2, 0.5)
        if p > 0:
            M.arrow(c, 790, 470, 1110, 470, TINTA2, p, 6, 20, p)
    questao(c, t, C, "s03", "s04", maqs,
            lambda: E.frase(c, t, d3, ps("qual foi o", "i", 84) + [("aumento total?", "g", 84, COR)], W / 2, 820, "center", 0.14))


def b_resposta1(c, t, C, b):
    marca(c, t, C["s05"] - 0.5, 1)
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    funde(c, t, C["s05"], c5 - 0.4, 640, 1280, 330, [(C["s05"], "+ 5%"), (a5, "× 1,05")], [(C["s05"] + 0.3, "+ 10%"), (a5 + 0.4, "× 1,1")], "× 1,155", 84)
    E.frase(c, t, b5, ps("sem as vírgulas:", "i", 70) + [("105 × 11 = 1155", "g", 80)], W / 2, 600, "center", 0.15)
    E.frase(c, t, c5, ps("três casas:", "i", 70) + [("1,155", "g", 84, COR)], W / 2, 740, "center", 0.15)
    E.foco(c, t, d5, 0.5, lambda a: E.pilula(c, "+ 15,5%", 800, 900, 76, "g", a=a))
    E.frase(c, t, d5 + 1.2, ps("e não", "i", 76) + [("15%", "g", 80, ERRADO)], 1250, 925, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
    E.frase(c, t, C["s06"] + 0.1, [("o atalho:", "g", 70, BR)] + ps("de cabeça", "i", 74, CLARO), W / 2, 160, "center", 0.15)
    E.frase(c, t, C["s06"] + 0.8, [("a + b + a × b ÷ 100", "g", 76, CLARO)], W / 2, 280, "center")
    E.frase(c, t, a6, [("5 + 10", "g", 96, BR), ("=", "g", 90, CLARO), ("15", "g", 96, BR)], W / 2, 440, "center", 0.25)
    E.frase(c, t, b6, [("5 × 10 ÷ 100", "g", 96, BR), ("=", "g", 90, CLARO), ("0,5", "g", 96, BR)], W / 2, 590, "center", 0.25)
    E.frase(c, t, c6, [("15,5%", "g", 130, CLARO)], W / 2, 760, "center")
    E.frase(c, t, d6, ps("o 2º aumento vale", "i", 64, CLARO) + [("sobre o 1º", "g", 64, BR)], W / 2, 880, "center", 0.1)
    E.frase(c, t, e6, ps("3 variações ou mais?", "i", 62, CLARO) + [("multiplique os fatores", "g", 62, BR)], W / 2, 990, "center", 0.1)


# ---------------- situação 2 ----------------
def b_questao2(c, t, C, b):
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    marca(c, t, a7, 2)
    E.frase(c, t, a7 + 0.6, [("liquidação", "g", 64)], 880, 132)

    def maqs():
        maquina(c, t, b7, 640, 470, "− 30%", 96)
        E.foco(c, t, b7 + 0.3, 0.4, lambda a: centro(c, "na etiqueta", 640, 340, 58, "i", TINTA2, a))
        maquina(c, t, c7, 1280, 470, "− 20%", 96)
        E.foco(c, t, c7 + 0.3, 0.4, lambda a: centro(c, "mais, no caixa", 1280, 340, 58, "i", TINTA2, a))
        p = ep(t, c7 + 0.2, 0.5)
        if p > 0:
            M.arrow(c, 800, 470, 1110, 470, TINTA2, p, 6, 20, p)
    questao(c, t, C, "s07", "s08", maqs,
            lambda: E.frase(c, t, d7, ps("qual é o", "i", 84) + [("desconto total?", "g", 84, COR)], W / 2, 820, "center", 0.14))


def b_resposta2(c, t, C, b):
    marca(c, t, C["s09"] - 0.5, 2)
    a9, b9, c9, d9, e9, f9, g9 = (C[f"s09.{k}"] for k in "abcdefg")

    def fatores():
        funde(c, t, C["s09"], c9 - 0.4, 640, 1280, 330, [(C["s09"], "− 30%"), (a9, "× 0,7")], [(C["s09"] + 0.3, "− 20%"), (a9 + 0.4, "× 0,8")], "× 0,56", 84)
        E.frase(c, t, b9, [("7 × 8 = 56", "g", 84)], W / 2, 590, "center")
        E.frase(c, t, c9, [("0,7 × 0,8", "g", 84), ("=", "g", 84, TINTA2), ("0,56", "g", 90, COR)], W / 2, 720, "center", 0.25)
        E.frase(c, t, d9, ps("paga 56%:", "i", 76) + [("desconto de 44%", "g", 80, CERTO)], W / 2, 880, "center", 0.15)
    E.saida(c, t, e9 - 0.1, fatores)
    if t < e9 - 0.1:
        return
    E.frase(c, t, e9, ps("com", "i", 76) + [("R$ 100", "g", 76, COR)], W / 2, 290, "center", 0.14)
    cadeia(c, t, 520, ["R$ 100", "R$ 70", "R$ 56"], ["− 30%", "− 20%"], [e9, e9 + 1.0, f9], [e9 + 0.5, lerp(e9, f9, 0.6)], XS5,
           ("antes", "etiqueta", "caixa"))
    E.frase(c, t, lerp(e9, f9, 0.6), [("20% de 70 = 14", "g", 68)], W / 2, 750, "center")
    E.frase(c, t, g9, ps("quem somou achou", "i", 70, TINTA2) + [("50%", "g", 76, ERRADO)], W / 2, 900, "center", 0.12)
    selo_em(c, t, g9 + 1.6, 1430, 875, 40, False)


# ---------------- situação 3 ----------------
def b_questao3(c, t, C, b):
    a10, b10, c10, d10, e10 = (C[f"s10.{k}"] for k in "abcde")
    marca(c, t, a10, 3)

    def noticia():
        manchete(c, t, b10, "vendas caem 60% e depois sobem 60%", W / 2, 330, 58)
        E.frase(c, t, c10, [("e voltam ao nível de antes", "g", 58)], W / 2, 470, "center")
    sobe = ease_io(prog(t, C["s11"] - 0.2, 0.8))
    grupo(c, W / 2, 400, lerp(1, 0.85, sobe), lambda: (c.translate(0, -sobe * 80), noticia()))
    E.saida(c, t, C["s11"] - 0.2, lambda: (E.frase(c, t, d10, ps("a notícia está", "i", 80) + [("certa?", "g", 80, COR)], W / 2, 680, "center", 0.12),
                                           E.frase(c, t, e10, ps("quanto precisariam subir para", "i", 72) + [("voltar?", "g", 76, COR)], W / 2, 820, "center", 0.12)))
    E.relogio(c, t, C["s11.a"], 960, 760, 120)


def b_resposta3(c, t, C, b):
    marca(c, t, C["s12"] - 0.5, 3)
    a12, b12, c12, d12, e12, f12 = (C[f"s12.{k}"] for k in "abcdef")
    a13, b13, c13, d13 = (C[f"s13.{k}"] for k in "abcd")

    def doze():
        funde(c, t, C["s12"], b12, 640, 1280, 330, [(C["s12"], "− 60%"), (a12, "× 0,4")], [(C["s12"] + 0.3, "+ 60%"), (a12 + 0.4, "× 1,6")], "× 0,64", 84)
        E.frase(c, t, b12, [("4 × 16 = 64", "g", 76), ("→", "g", 76, TINTA2), ("0,64", "g", 80, COR)], W / 2, 560, "center", 0.2)
        E.frase(c, t, c12, [("36% abaixo", "g", 80, COR)] + ps("do que eram", "i", 76), W / 2, 690, "center", 0.12)
        manchete(c, t, d12, "e voltam ao nível de antes", W / 2, 860, 52, risca=d12 + 0.4)
    E.saida(c, t, e12 - 0.1, doze)
    if e12 - 0.1 <= t < C["s13"] - 0.1:
        def cem_():
            E.frase(c, t, e12, ps("com", "i", 76) + [("100", "g", 76, COR)], W / 2, 250, "center", 0.14)
            cadeia(c, t, 520, ["100", "40", "64"], ["− 60%", "+ 60%"], [e12, e12 + 1.0, f12], [e12 + 0.5, lerp(e12, f12, 0.5)], XS5,
                   ("antes", "cai", "sobe"), cores=[None, None, ERRADO])
            E.frase(c, t, lerp(e12, f12, 0.5), [("60% de 40 = 24", "g", 68)], W / 2, 760, "center")
        E.saida(c, t, C["s13"] - 0.1, cem_)
    if t < C["s13"] - 0.1:
        return
    fluxo(c, t, 330, "100", "× 0,4", "40", C["s13"], C["s13"], C["s13"], rot=("antes", "depois da queda"), size=80)
    volta(c, t, a13, XA, XD, 420, [(a13 + 0.3, "÷ 0,4"), (b13, "+ 150%")], alto=100)
    E.frase(c, t, lerp(a13, b13, 0.4), [("1 ÷ 0,4", "g", 72), ("=", "g", 72, TINTA2), ("10 ÷ 4", "g", 72), ("=", "g", 72, TINTA2), ("2,5", "g", 76, COR)],
            W / 2, 720, "center", 0.2)
    E.frase(c, t, c13, ps("perdeu", "i", 66) + [("3/5,", "g", 70)] + ps("ficaram", "i", 66) + [("2", "g", 70)], 620, 880, "center", 0.12)
    E.frase(c, t, d13, ps("ganhar 3 sobre 2:", "i", 66) + [("1,5 vez", "g", 70, COR)], 1380, 880, "center", 0.12)


# ---------------- situação 4 ----------------
def b_questao4(c, t, C, b):
    a14, b14, c14, d14, e14 = (C[f"s14.{k}"] for k in "abcde")
    marca(c, t, a14, 4)
    E.frase(c, t, a14 + 0.6, ps("juros de um", "i", 66) + [("financiamento", "g", 66)], W / 2, 230, "center", 0.12)
    sobe = ease_io(prog(t, C["s15"] - 0.2, 0.8))
    grupo(c, W / 2, 440, lerp(1, 0.8, sobe), lambda: (c.translate(0, -sobe * 60),
                                                   fluxo(c, t, 440, "12%", "caiu", "9%", b14, c14, c14, rot=("antes", "depois"), size=84)))
    E.saida(c, t, C["s15"] - 0.2, lambda: (manchete(c, t, d14, "juros caem 3%", W / 2, 700, 64),
                                           E.frase(c, t, e14, ps("como", "i", 80) + [("corrigir a manchete?", "g", 80, COR)], W / 2, 900, "center", 0.12)))
    E.relogio(c, t, C["s15.a"], 960, 780, 120)


def b_resposta4(c, t, C, b):
    marca(c, t, C["s16"] - 0.5, 4)
    a16, b16, c16, d16 = (C[f"s16.{k}"] for k in "abcd")
    fluxo(c, t, 330, "12%", [(C["s16"], "caiu"), (c16, "− 3 p.p."), (d16, "− 25%")], "9%", C["s16"], C["s16"], C["s16"], rot=("antes", "depois"), size=80)
    E.frase(c, t, a16, [("12 − 9", "g", 80), ("=", "g", 80, TINTA2), ("3 pontos percentuais", "g", 80, COR)], W / 2, 580, "center", 0.25)
    E.frase(c, t, b16, [("3 ÷ 12", "g", 80), ("=", "g", 80, TINTA2), ("0,25", "g", 84, COR)], W / 2, 720, "center", 0.25)
    manchete(c, t, C["s16"] + 0.3, "juros caem 3%", 520, 900, 52, risca=lerp(d16, C["s16.end"], 0.4))
    E.foco(c, t, c16, 0.5, lambda a: E.pilula(c, "caem 3 p.p. ou 25%", 1320, 900, 60, "g", fundo=CERTO, a=a))


# ---------------- situação 5 ----------------
def b_questao5(c, t, C, b):
    a17, b17, c17, d17 = (C[f"s17.{k}"] for k in "abcd")
    marca(c, t, a17, 5)
    E.frase(c, t, a17 + 0.6, ps("casas de um", "i", 66) + [("bairro", "g", 66)], W / 2, 230, "center", 0.12)

    def texto():
        E.frase(c, t, b17, [("70%", "g", 96, COR)] + ps("têm internet", "i", 84), W / 2, 400, "center", 0.14)
        E.frase(c, t, c17, ps("dessas,", "i", 84) + [("40%", "g", 96)] + ps("têm fibra", "i", 84), W / 2, 540, "center", 0.14)
    questao(c, t, C, "s17", "s18", texto,
            lambda: E.frase(c, t, d17, ps("que % de", "i", 80) + [("todas as casas", "g", 80, COR)] + ps("tem fibra?", "i", 80), W / 2, 760, "center", 0.12))


def b_resposta5(c, t, C, b):
    marca(c, t, C["s19"] - 0.5, 5)
    a19, b19, c19, d19, e19 = (C[f"s19.{k}"] for k in "abcde")
    E.frase(c, t, a19, ps("os 40% são", "i", 66) + [("das casas com internet", "g", 66, COR)], 1340, 260, "center", 0.1)
    E.frase(c, t, b19, [("70 × 40", "g", 80), ("=", "g", 80, TINTA2), ("2800", "g", 84)], 1340, 420, "center", 0.25)
    E.frase(c, t, c19, [("÷ 100", "g", 80), ("=", "g", 80, TINTA2), ("28%", "g", 96, COR)], 1340, 560, "center", 0.25)
    cem(c, t, d19, 260, 220, 560, 70, d19 + 0.5, 28, e19)
    E.foco(c, t, d19 + 0.2, 0.4, lambda a: centro(c, "100 casas", 540, 220 + 560 + 70, 54, "i", TINTA2, a))
    E.frase(c, t, e19, [("40% de 70", "g", 76), ("=", "g", 76, TINTA2), ("28", "g", 80, CERTO)], 1340, 720, "center", 0.25)
    selo_em(c, t, e19 + 1.4, 1700, 695, 42)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a20, b20, c20, d20 = (C[f"s20.{k}"] for k in "abcd")

    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        for i, (ti, l1, l2) in enumerate(((a20, "variações seguidas:", "multiplique"), (b20, "para voltar:", "1 ÷ fator"),
                                          (c20, "diferença de %:", "ponto percentual"))):
            y = 370 + i * 170
            E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 300, y - 30, 56, 64, a))
            E.frase(c, t, ti + 0.1, [(l1, "i", 76)], 400, y)
            E.frase(c, t, ti + 0.4, [(l2, "g", 76, COR)], 1000, y)
        E.foco(c, t, d20, 0.5, lambda a: E.pilula(c, "trilha de porcentagem: completa", W / 2, 920, 64, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a21, b21, c21, d21, e21, f21 = (C[f"s21.{k}"] for k in "abcdef")
    E.frase(c, t, C["s21"] + 0.1, ps("próxima trilha:", "i", 84), XE, 280)
    E.frase(c, t, a21, [("Matemática financeira", "g", 100, COR)], XE, 420)
    E.frase(c, t, b21, ps("começa por", "i", 80) + [("juros simples", "g", 90, COR)], XE, 560, "left", 0.14)
    E.frase(c, t, c21, ps("capital, taxa, tempo e montante", "i", 60), XE, 680, "left", 0.07)
    E.frase(c, t, d21, [("R$ 1.200", "g", 64)] + ps("a 2% ao mês, em 6 meses", "i", 60), XE, 780, "left", 0.1)
    E.foco(c, t, e21, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=a))
    p = ease_io(prog(t, e21 + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, e21 + 0.2, 0.4))
    E.frase(c, t, f21, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 970, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, atalho=b_atalho,
              questao2=b_questao2, resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3,
              questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
