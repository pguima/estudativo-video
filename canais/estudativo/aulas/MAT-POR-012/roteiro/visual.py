"""Visual — Estudativo · MAT-POR-012: ponto percentual e porcentagem de porcentagem.

Linguagem da trilha Porcentagem (MAT-POR-006): cartao() = valor de antes (contorno escuro) ou de depois (cor da matéria);
maquina() = a mudança (+2 p.p., +25%); fluxo() = antes → [máquina] → depois. Peça desta aula: cem(), 100 quadradinhos
para a porcentagem de porcentagem (40 de 100 na cor, 12 deles em escuro). Todo instante vem de C[...]."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-012_ponto_percentual.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pontos", "dede", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 10 - 8 == 2 and 2 / 8 == 0.25 and 1000 * 8 // 100 == 80 and 1000 * 10 // 100 == 100 and 20 / 80 == 0.25
assert 40 * 30 / 100 == 12 and round(0.3 * 0.4, 6) == 0.12 and 30 * 40 == 1200 and 80 * 2 / 100 == 1.6
assert 500 * 40 // 100 == 200 and 200 * 30 // 100 == 60 and 25 * 60 == 1500 and 60 * 25 // 100 == 15 and 18 - 15 == 3 and 3 / 15 == 0.2


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


# ---------------- peça desta aula: cem quadradinhos ----------------
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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def um():
        E.frase(c, t, C["s01"] + 0.3, ps("trabalhadores que vão de", "i", 76) + [("bicicleta", "g", 76, COR)], W / 2, 170, "center", 0.12)
        fluxo(c, t, 420, "8%", "subiu", "10%", ka, kb, kb, rot=("antes", "depois"))
        for x, txt_, ti in ((560, "subiu 2%", kc), (1360, "subiu 25%", kd)):
            E.foco(c, t, ti, 0.45, lambda a, x=x, txt_=txt_: E.pilula(c, txt_, x, 720, 66, "g", fundo=TINTA, a=a))
            E.foco(c, t, ti, 0.45, lambda a, x=x, n=("jornal 1" if x < 900 else "jornal 2"): centro(c, n, x, 630, 54, "i", TINTA2, a))
        E.frase(c, t, lerp(kd, C["s01.end"], 0.4), ps("um deles", "i", 84) + [("errou. qual?", "g", 84, ERRADO)], W / 2, 930, "center", 0.14)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.2), [("a resposta", "g", 104, COR)], XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.45), ps("e", "i", 90) + [("porcentagem", "g", 100, COR)], XE, 600, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("de porcentagem", "i", 90), XE, 730, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "porcentagem de um número:", "20% de 80 = 16"), ("s03.c", "variação percentual:", "diferença ÷ antes"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 260 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 210, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 88)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 70, COR)], x + 44, y + 176)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(440, 730, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- pontos percentuais ----------------
def b_pontos(c, t, C, b):
    a4, b4, c4, d4, e4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"], C["s04.e"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]

    def duas():
        E.frase(c, t, a4, [("duas formas", "g", 80, COR)] + ps("de medir a mudança", "i", 80), W / 2, 160, "center", 0.12)
        fluxo(c, t, 380, "8%", "?", "10%", a4 + 0.3, a4 + 0.6, a4 + 0.3, rot=("antes", "depois"), size=84)
        # 1ª forma: diferença simples
        E.foco(c, t, b4, 0.45, lambda a: E.pilula(c, "diferença simples", 560, 600, 54, "g", fundo=TINTA, a=a))
        E.frase(c, t, c4, [("10 − 8", "g", 80), ("=", "g", 80, TINTA2), ("2", "g", 84, COR)], 560, 740, "center", 0.25)
        E.frase(c, t, d4, ps("ponto percentual", "i", 64, COR), 560, 850, "center", 0.1)
        E.foco(c, t, e4, 0.5, lambda a: num_bola(c, "+2 p.p.", 560, 950, 70, 40, a))
        # 2ª forma: variação percentual
        E.foco(c, t, a5, 0.45, lambda a: E.pilula(c, "variação percentual", 1360, 600, 54, "g", a=a))
        E.frase(c, t, b5, [("2 ÷ 8", "g", 80), ("=", "g", 80, TINTA2), ("0,25", "g", 84, COR)], 1360, 740, "center", 0.25)
        E.frase(c, t, lerp(a5, b5, 0.5), ps("diferença ÷ antes", "i", 64, COR), 1360, 850, "center", 0.1)
        E.foco(c, t, c5, 0.5, lambda a: num_bola(c, "+25%", 1360, 950, 70, 44, a))
    E.saida(c, t, C["s06"] - 0.1, duas)
    if C["s06"] - 0.1 <= t < C["s07"] - 0.1:
        def seis():
            E.frase(c, t, C["s06"] + 0.2, ps("as duas", "i", 80) + [("estão certas", "g", 80, CERTO)], W / 2, 160, "center", 0.14)
            E.frase(c, t, a6, [("1000", "g", 76, COR)] + ps("trabalhadores", "i", 76), W / 2, 270, "center", 0.12)
            fluxo(c, t, 520, [(b6, "80")], "+ 20", [(c6, "100")], b6, c6 + 0.5, c6, rot=("8% de 1000", "10% de 1000"), size=88)
            E.frase(c, t, d6, [("20 ÷ 80", "g", 84), ("=", "g", 84, TINTA2), ("25%", "g", 90, COR)], W / 2, 800, "center", 0.25)
            E.frase(c, t, e6, ps("a mesma mudança:", "i", 70) + [("+2 p.p. = +25%", "g", 72, COR)], W / 2, 950, "center", 0.12)
        E.saida(c, t, C["s07"] - 0.1, seis)
    if t < C["s07"] - 0.1:
        return
    E.frase(c, t, C["s07"] + 0.2, ps("a diferença pode ser", "i", 80) + [("enorme", "g", 80, COR)], W / 2, 160, "center", 0.14)
    fluxo(c, t, 420, "1%", [(b7, "+1 p.p."), (c7, "× 2"), (d7 + 0.8, "+100%")], "2%", a7, b7, a7 + 0.8, rot=("antes", "depois"))
    E.frase(c, t, b7, ps("só", "i", 84) + [("1 ponto percentual", "g", 84)], W / 2, 710, "center", 0.14)
    E.frase(c, t, c7, ps("mas", "i", 84) + [("dobrou:", "g", 90, COR), ("+100%", "g", 96, COR)], W / 2, 880, "center", 0.2)


# ---------------- porcentagem de porcentagem ----------------
GX, GY, GL = 260, 300, 560


def b_dede(c, t, C, b):
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    a9, b9, c9, d9, e9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    E.frase(c, t, a8, [("porcentagem", "g", 80, COR)] + ps("de porcentagem", "i", 80), W / 2, 150, "center", 0.14)

    def enunciado():
        E.frase(c, t, b8, [("40%", "g", 90, COR)] + ps("vão de ônibus", "i", 80), XE + 60, 380, "left", 0.14)
        E.frase(c, t, c8, ps("desses,", "i", 80) + [("30%", "g", 90)] + ps("pegam mais de um", "i", 80), XE + 60, 540, "left", 0.14)
        E.frase(c, t, d8, ps("quantos % de", "i", 84) + [("todos os funcionários?", "g", 84, COR)], W / 2, 800, "center", 0.12)
    E.saida(c, t, a9 - 0.1, enunciado)
    if t < a9 - 0.1:
        return
    E.frase(c, t, a9, ps("os 30% são", "i", 70) + [("dos 40%", "g", 72, COR)], 1340, 300, "center", 0.12)
    cem(c, t, b9, GX, GY, GL, 40, c9, 12, d9)
    E.foco(c, t, b9 + 0.2, 0.4, lambda a: centro(c, "100 funcionários", GX + GL / 2, GY + GL + 80, 54, "i", TINTA2, a))
    E.frase(c, t, c9, [("40", "g", 80, COR)] + ps("vão de ônibus", "i", 72), 1340, 440, "center", 0.12)
    E.frase(c, t, d9, [("30% de 40", "g", 80), ("=", "g", 80, TINTA2), ("12", "g", 84)], 1340, 580, "center", 0.25)
    E.frase(c, t, e9, [("12 em 100", "g", 80), ("=", "g", 80, TINTA2), ("12%", "g", 90, COR)], 1340, 720, "center", 0.25)
    E.frase(c, t, a10, [("30% de 40%", "g", 72)], 1340, 860, "center")
    E.frase(c, t, b10, [("0,3 × 0,4", "g", 72), ("=", "g", 72, TINTA2)], 1290, 980, "right", 0.25)
    E.frase(c, t, c10, [("0,12 = 12%", "g", 72, COR)], 1320, 980, "left")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a11, b11, c11, d11, e11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"]
    E.frase(c, t, C["s11"] + 0.1, ps("voltando aos", "i", 80) + [("jornais", "g", 80, COR)], W / 2, 160, "center", 0.14)
    E.foco(c, t, a11, 0.45, lambda a: E.pilula(c, "subiu 2%", 560, 320, 66, "g", fundo=TINTA, a=a))
    selo_em(c, t, a11 + 0.8, 780, 300, 44, False)
    E.foco(c, t, a11 + 0.2, 0.45, lambda a: E.pilula(c, "subiu 25%", 1360, 320, 66, "g", a=a))
    selo_em(c, t, a11 + 1.0, 1590, 300, 44, True)
    E.frase(c, t, b11, [("2% de 80", "g", 76), ("=", "g", 76, TINTA2), ("1,6", "g", 80, ERRADO)] + ps("pessoa", "i", 70), W / 2, 500, "center", 0.2)
    E.frase(c, t, c11, ps("mas os ciclistas aumentaram", "i", 70) + [("20 pessoas", "g", 76, COR)], W / 2, 630, "center", 0.12)
    E.frase(c, t, d11, ps("diferença de porcentagens =", "i", 68) + [("pontos percentuais", "g", 72, COR)], W / 2, 790, "center", 0.12)
    E.frase(c, t, e11, [("+2 pontos percentuais", "g", 76, CERTO)] + ps("ou", "i", 76) + [("+25%", "g", 80, CERTO)], W / 2, 940, "center", 0.2)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    a13, b13, c13, d13, e13, f13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"], C["s13.f"]

    def doze():
        E.frase(c, t, C["s12"] + 0.1, [("o atalho:", "g", 70, BR)] + ps("porcentagem de porcentagem", "i", 74, CLARO), W / 2, 160, "center", 0.12)
        E.frase(c, t, a12, ps("multiplique e", "i", 84, CLARO) + [("divida por 100", "g", 90, BR)], W / 2, 360, "center", 0.15)
        E.frase(c, t, b12, [("30 × 40", "g", 110, BR), ("=", "g", 100, CLARO), ("1200", "g", 110, CLARO)], W / 2, 580, "center", 0.25)
        E.frase(c, t, c12, [("1200 ÷ 100", "g", 110, BR), ("=", "g", 100, CLARO), ("12%", "g", 120, CLARO)], W / 2, 800, "center", 0.25)
    E.saida(c, t, C["s13"] - 0.1, doze)
    if t < C["s13"] - 0.1:
        return

    def treze():
        E.frase(c, t, a13, ps("cada % é uma fração", "i", 74, CLARO) + [("com 100 embaixo", "g", 74, BR)], W / 2, 260, "center", 0.12)
        y = 520
        E.foco(c, t, a13 + 1.0, 0.45, lambda a: E.fracao(c, 30, 100, 420, y, 96, BR, a))
        cen(c, t, a13 + 1.2, "×", 590, y + 34, 90, CLARO)
        E.foco(c, t, a13 + 1.4, 0.45, lambda a: E.fracao(c, 40, 100, 760, y, 96, BR, a))
        cen(c, t, b13 - 0.2, "=", 940, y + 34, 90, CLARO)
        E.foco(c, t, b13, 0.45, lambda a: E.fracao(c, 1200, "10000", 1170, y, 96, BR, a))
        cen(c, t, c13 - 0.2, "=", 1420, y + 34, 90, CLARO)
        E.foco(c, t, c13, 0.45, lambda a: E.fracao(c, 12, 100, 1600, y, 96, CLARO, a))
    E.saida(c, t, d13 - 0.1, treze)
    if t < d13 - 0.1:
        return
    E.frase(c, t, d13, ps("o problema dá", "i", 74, CLARO) + [("pessoas", "g", 76, BR)] + ps("e pede", "i", 74, CLARO) + [("pessoas?", "g", 76, BR)],
            W / 2, 200, "center", 0.12)
    E.frase(c, t, d13 + 1.6, ps("vá em etapas", "i", 84, CLARO), W / 2, 330, "center", 0.12)
    E.frase(c, t, e13, [("40% de 500", "g", 96, BR), ("=", "g", 90, CLARO), ("200", "g", 100, CLARO)], W / 2, 560, "center", 0.25)
    E.frase(c, t, f13, [("30% de 200", "g", 96, BR), ("=", "g", 90, CLARO), ("60", "g", 100, CLARO)], W / 2, 760, "center", 0.25)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 150)
    E.frase(c, t, C["s14"] + 0.6, [("escola", "g", 72)], XE + 470, 150)

    def texto():
        E.frase(c, t, a14, [("60%", "g", 84, COR)] + ps("estudam de manhã", "i", 76), XE, 320, "left", 0.14)
        E.frase(c, t, b14, ps("desses,", "i", 76) + [("25%", "g", 84)] + ps("vão de bicicleta", "i", 76), XE, 450, "left", 0.14)
        E.frase(c, t, c14, [("1)", "g", 64, COR)] + ps("que % de todos estuda de manhã e vai de bicicleta?", "i", 60), XE, 590, "left", 0.08)
        E.frase(c, t, a15, [("2)", "g", 64, COR)] + ps("no ano seguinte:", "i", 60) + [("18%", "g", 68, COR)], XE, 700, "left", 0.1)
        E.frase(c, t, b15, ps("subiu quantos", "i", 60) + [("pontos percentuais?", "g", 62)], XE + 60, 800, "left", 0.1)
        E.frase(c, t, c15, ps("e quantos", "i", 60) + [("por cento?", "g", 62)], XE + 60, 900, "left", 0.1)
    texto()
    E.relogio(c, t, C["s16.a"], 1580, 760, 120)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a17, b17, c17, d17, e17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"], C["s17.e"]
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]

    def um():
        E.frase(c, t, C["s17"] + 0.2, [("25% de 60%", "g", 80, COR)], 1340, 200, "center")
        E.frase(c, t, a17, [("25 × 60", "g", 76), ("=", "g", 76, TINTA2), ("1500", "g", 80)], 1340, 340, "center", 0.25)
        E.frase(c, t, b17, [("÷ 100", "g", 76), ("=", "g", 76, TINTA2), ("15%", "g", 90, COR)], 1340, 470, "center", 0.25)
        cem(c, t, c17, GX, 200, GL, 60, c17 + 0.6, 15, d17)
        E.foco(c, t, c17 + 0.2, 0.4, lambda a: centro(c, "100 alunos", GX + GL / 2, 200 + GL + 70, 54, "i", TINTA2, a))
        E.frase(c, t, d17, [("25% de 60", "g", 72), ("=", "g", 72, TINTA2), ("15", "g", 76, COR)], 1340, 610, "center", 0.25)
        E.frase(c, t, e17, ps("quem somou:", "i", 64, TINTA2) + [("85%", "g", 76, ERRADO)], 1340, 760, "center", 0.12)
        E.frase(c, t, lerp(e17, C["s17.end"], 0.4), ps("mais que os 60% da manhã:", "i", 54, TINTA2) + [("impossível", "g", 58, ERRADO)], 1340, 860, "center", 0.08)
    E.saida(c, t, C["s18"] - 0.1, um)
    if t < C["s18"] - 0.1:
        return
    fluxo(c, t, 360, "15%", [(a18, "+3 p.p."), (c18, "+20%")], "18%", C["s18"] + 0.1, a18, C["s18"] + 0.3, rot=("antes", "depois"))
    E.frase(c, t, a18, [("18 − 15", "g", 84), ("=", "g", 84, TINTA2), ("3 pontos percentuais", "g", 84, COR)], W / 2, 640, "center", 0.25)
    E.frase(c, t, b18, [("3 ÷ 15", "g", 84), ("=", "g", 84, TINTA2), ("0,2", "g", 88)], W / 2, 790, "center", 0.25)
    E.foco(c, t, c18, 0.5, lambda a: E.pilula(c, "subiu 20%", W / 2, 920, 72, "g", a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]

    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        for i, (ti, l1, l2) in enumerate(((a19, "diferença de %:", "ponto percentual"), (b19, "÷ pelo valor de antes:", "variação percentual"),
                                          (c19, "% de %:", "multiplica"))):
            y = 390 + i * 190
            E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 300, y - 30, 56, 64, a))
            E.frase(c, t, ti + 0.1, [(l1, "i", 76)], 400, y)
            E.frase(c, t, ti + 0.4, [(l2, "g", 76, COR)], 1000, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20, c20, d20, e20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"], C["s20.e"]
    E.frase(c, t, C["s20"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, a20, [("Praticando", "g", 116, COR)], XE, 450)
    E.frase(c, t, a20 + 0.4, [("variações sucessivas", "g", 116, COR)], XE, 590)
    E.frase(c, t, b20, ps("aumentos e descontos seguidos, volta ao original", "i", 58), XE, 730, "left", 0.07)
    E.frase(c, t, c20, ps("e notícias cheias de porcentagem", "i", 58), XE, 810, "left", 0.07)
    E.foco(c, t, d20, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=a))
    p = ease_io(prog(t, d20 + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, d20 + 0.2, 0.4))
    E.frase(c, t, e20, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 970, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pontos=b_pontos, dede=b_dede, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
