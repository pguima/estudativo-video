"""Visual — Estudativo · MAT-POR-011: voltar ao valor original.

Linguagem da trilha Porcentagem (MAT-POR-006 e MAT-POR-010): cartao() = valor de antes (contorno escuro) ou de depois
(cor da matéria); maquina() = o fator; fluxo() e cadeia() = valores ligados por máquinas; volta() = a conta de volta por baixo;
funde() = duas máquinas que viram uma só (0,8 × 1,25 = 1). Todo instante vem de C[...]."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia
from fractions import Fraction as Fr

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-011_voltar_ao_valor_original.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("cem", "fator", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 100 * 0.8 == 80 and 80 * 0.2 == 16 and 80 + 16 == 96 and 20 / 80 == 0.25 and 1 / 0.8 == 1.25 and 80 * 1.25 == 100
assert 1 / 0.5 == 2 and 1 / 1.25 == 0.8 and round(0.8 * 1.2, 6) == 0.96 and Fr(1, 5) / Fr(4, 5) == Fr(1, 4)
assert Fr(1, 4) / Fr(3, 4) == Fr(1, 3) and Fr(1, 10) / Fr(9, 10) == Fr(1, 9) and round(100 / 9) == 11
assert 40000 * 0.75 == 30000 and 40000 - 30000 == 10000 and 30000 / 10000 == 3 and 1 / 0.25 == 4 and 10000 * 4 == 40000
assert 10000 * 1.75 == 17500


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, ka - 0.6, ps("um", "i", 80) + [("salário", "g", 80, COR)], W / 2, 170, "center", 0.14)
        maquina(c, t, ka, 560, 420, "− 20%", 96)
        E.foco(c, t, ka + 0.3, 0.4, lambda a: centro(c, "corte", 560, 290, 58, "i", TINTA2, a))
        maquina(c, t, kb, 1360, 420, [(kb, "+ 20%"), (kc + 1.2, "+ 25%")], 96)
        E.foco(c, t, kb + 0.3, 0.4, lambda a: centro(c, "aumento", 1360, 290, 58, "i", TINTA2, a))
        p = ep(t, kb + 0.3, 0.5)
        if p > 0:
            M.arrow(c, 740, 420, 1170, 420, TINTA2, p, 6, 20, p)
        E.saida(c, t, kc, lambda: E.frase(c, t, lerp(kb, kc, 0.55), ps("voltou ao que", "i", 84) + [("era?", "g", 84, COR)], W / 2, 740, "center", 0.14))
        E.frase(c, t, kc, [("não.", "g", 84, ERRADO)] + ps("para voltar, precisava ser", "i", 76) + [("25%", "g", 84, CERTO)], W / 2, 740, "center", 0.14)
        selo_em(c, t, kc + 1.6, 1600, 330, 44)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.2), ps("quanto", "i", 96) + [("subir", "g", 110, COR)], XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.45), ps("para", "i", 96) + [("se recuperar", "g", 104, COR)], XE, 610, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.7), ps("de uma queda", "i", 90), XE, 750, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "variação percentual:", "diferença ÷ antes"), ("s03.c", "variações seguidas:", "multiplique os fatores"),
             ("s03.d", "dividir por decimal:", "sem vírgula no divisor"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 150 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    alvo = [C[k] for k, _, _ in itens]
    q1, q2 = ease_io(prog(t, alvo[1] - 0.35, 0.5)), ease_io(prog(t, alvo[2] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(320, 560, q1), 800, q2), ep(t, alvo[0], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1010, "left", 0.12)


# ---------------- com cem reais ----------------
XS5 = [240, 600, 960, 1320, 1680]


def b_cem(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    a5, b5, c5, d5, e5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]

    def quatro():
        E.frase(c, t, C["s04"] + 0.1, ps("comece com", "i", 76) + [("R$ 100", "g", 76, COR)], W / 2, 150, "center", 0.14)
        cadeia(c, t, 420, ["R$ 100", "R$ 80", "R$ 96"], ["− 20%", "+ 20%"], [a4, b4, c4], [lerp(a4, b4, 0.5), lerp(b4, c4, 0.4)], XS5,
               ("antes", "cai", "sobe"), cores=[None, None, ERRADO])
        E.frase(c, t, lerp(b4, c4, 0.5), [("20% de 80", "g", 76), ("=", "g", 76, TINTA2), ("16", "g", 80, COR)], W / 2, 690, "center", 0.25)
        E.frase(c, t, d4, ps("não chegou a", "i", 84) + [("R$ 100", "g", 84, ERRADO)], W / 2, 880, "center", 0.14)
    E.saida(c, t, C["s05"] - 0.1, quatro)
    if C["s05"] - 0.1 <= t < C["s06"] - 0.1:
        def cinco():
            E.frase(c, t, C["s05"] + 0.1, ps("para voltar a", "i", 76) + [("R$ 100", "g", 76, COR)], W / 2, 150, "center", 0.14)
            fluxo(c, t, 400, "R$ 80", [(a5, "+ R$ 20"), (d5, "+ 25%")], "R$ 100", b5, a5, C["s05"] + 0.3, rot=("agora", "de volta"))
            E.frase(c, t, c5, [("20 ÷ 80", "g", 96), ("=", "g", 96, TINTA2), ("0,25", "g", 96, COR)], W / 2, 700, "center", 0.25)
            E.frase(c, t, e5, ps("a variação percentual", "i", 70) + [("de 80 para 100", "g", 70, COR)], W / 2, 900, "center", 0.12)
        E.saida(c, t, C["s06"] - 0.1, cinco)
    if t < C["s06"] - 0.1:
        return
    E.frase(c, t, C["s06"] + 0.1, ps("o", "i", 80) + [("motivo", "g", 80, COR)], W / 2, 170, "center", 0.14)
    for y, ti, nome, conta, sobre in ((400, a6, "a queda", "20% de 100 = 20", "sobre um valor maior"), (640, b6, "a subida", "25% de 80 = 20", "sobre um valor menor")):
        E.foco(c, t, ti, 0.45, lambda a, y=y, nome=nome: E.pilula(c, nome, 380, y - 25, 58, "g", fundo=TINTA if "queda" in nome else E.COR, a=a))
        E.frase(c, t, ti + 0.3, [(conta, "g", 76)], 620, y, "left")
        E.frase(c, t, ti + 0.8, ps(sobre, "i", 60, TINTA2), 620, y + 80, "left", 0.08)
    E.frase(c, t, c6, ps("os mesmos R$ 20 pedem", "i", 76) + [("uma % maior", "g", 76, COR)], W / 2, 900, "center", 0.12)


# ---------------- com fatores ----------------
def b_fator(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    a9, b9, c9, d9, e9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]

    def sete_oito():
        E.frase(c, t, C["s07"] + 0.1, ps("com", "i", 80) + [("fatores", "g", 80, COR)], W / 2, 150, "center", 0.14)
        E.foco(c, t, a7, 0.4, lambda a: centro(c, "cai 20%", 640, 270, 56, "g", TINTA2, a))
        E.foco(c, t, b7, 0.4, lambda a: centro(c, "volta", 1280, 270, 56, "g", TINTA2, a))
        funde(c, t, a7, c8, 640, 1280, 410, "× 0,8", [(b7, "× ?"), (b8, "× 1,25")], "× 1", 84)
        E.saida(c, t, a8 - 0.1, lambda: (E.frase(c, t, b7, [("0,8 × ?", "g", 90), ("=", "g", 90, TINTA2), ("1", "g", 96, COR)], W / 2, 660, "center", 0.3),
                                          E.frase(c, t, c7, [("? = 1 ÷ 0,8", "g", 96, COR)], W / 2, 830, "center")))
        if t >= a8 - 0.1:
            E.frase(c, t, a8, [("1 ÷ 0,8", "g", 84), ("=", "g", 84, TINTA2), ("10 ÷ 8", "g", 84), ("=", "g", 84, TINTA2), ("1,25", "g", 90, COR)],
                    W / 2, 620, "center", 0.25)
            E.frase(c, t, b8, ps("fator 1,25:", "i", 72) + [("subir 25%", "g", 76, COR)], 560, 760, "center", 0.12)
            E.frase(c, t, c8, [("80 × 1,25 = 100", "g", 72, CERTO)], 1380, 760, "center")
            E.foco(c, t, d8, 0.5, lambda a: E.pilula(c, "para voltar: 1 ÷ fator", W / 2, 920, 72, "g", a=a))
    E.saida(c, t, C["s09"] - 0.1, sete_oito)
    if t < C["s09"] - 0.1:
        return
    E.frase(c, t, C["s09"] + 0.1, ps("vale para", "i", 80) + [("qualquer queda", "g", 80, COR)], W / 2, 170, "center", 0.14)
    for y, t1, t2, t3, q, conta, res in ((400, a9, b9, c9, "caiu 50%?", "1 ÷ 0,5 = 2", "dobrar: subir 100%"),
                                         (700, d9, e9, e9 + 1.6, "subiu 25%?", "1 ÷ 1,25 = 0,8", "cair 20% desfaz")):
        E.frase(c, t, t1, [(q, "g", 76, TINTA)], XE, y, "left")
        E.frase(c, t, t2, [(conta, "g", 76, COR)], 680, y, "left")
        E.frase(c, t, t3, ps(res.split(":")[0] + (":" if ":" in res else ""), "i", 64, TINTA2) +
                ([(res.split(": ")[1], "g", 64, COR)] if ": " in res else []), 680, y + 100, "left", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    E.frase(c, t, C["s10"] + 0.1, [("o erro", "g", 96, ERRADO)] + ps("comum", "i", 96), W / 2, 170, "center", 0.14)
    E.frase(c, t, a10, ps("subir a mesma % que", "i", 80) + [("caiu", "g", 80, ERRADO)], W / 2, 330, "center", 0.14)
    funde(c, t, a10 + 0.6, b10 + 0.6, 640, 1280, 540, "× 0,8", "× 1,2", "× 0,96", 84)
    E.frase(c, t, b10, [("0,8 × 1,2", "g", 84), ("=", "g", 84, TINTA2), ("0,96", "g", 90, ERRADO)], W / 2, 780, "center", 0.25)
    E.frase(c, t, c10, ps("ainda", "i", 80) + [("faltam 4%", "g", 80, ERRADO)] + ps("do valor original", "i", 80), W / 2, 930, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
PX, PY, PW, PH = 360, 500, 1200, 150


def partes(c, t, n, cores, a=1.0, nums=None, ta=None, vis=None):
    """barra de n partes no palco: cores[i] = cor cheia ou None (só o contorno)"""
    if a <= 0:
        return
    w = PW / n
    for i in range(n):
        ai = a * (vis[i] if vis else 1.0)
        if ai <= 0:
            continue
        x = PX + i * w
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 6, PY, w - 12, PH), 18, 18)
        if cores[i]:
            c.drawRRect(r, M.paint(cores[i], ai))
        c.drawRRect(r, M.paint(CLARO, ai, stroke=4))


def b_atalho(c, t, C, b):
    palco(c, t)
    a11, b11, c11, d11, e11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"]
    a12, b12, c12, d12, e12, f12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"], C["s12.f"]

    def barra():
        E.frase(c, t, C["s11"] + 0.1, [("o atalho", "g", 64, BR), ("com frações", "i", 68, CLARO)], W / 2, 110, "center", 0.2)
        E.frase(c, t, a11, [("20%", "g", 100, BR), ("=", "g", 90, CLARO)], 900, 270, "right", 0.3)
        E.foco(c, t, a11 + 0.6, 0.45, lambda a: E.fracao(c, 1, 5, 1000, 235, 80, CLARO, a))
        perdeu = ep(t, lerp(b11, c11, 0.6), 0.5)
        cores = [CLARO] * 4 + [None]
        partes(c, t, 5, cores, ep(t, b11, 0.5), vis=[1, 1, 1, 1, 1 - 0.75 * perdeu])
        E.foco(c, t, lerp(b11, c11, 0.6), 0.4, lambda a: centro(c, "perdeu 1", PX + PW * 0.9, PY + PH + 70, 54, "i", CLARO, a))
        E.foco(c, t, c11, 0.4, lambda a: centro(c, "ficaram 4", PX + PW * 0.4, PY + PH + 70, 54, "g", BR, a))
        # a parte que volta, por cima das 4 que ficaram
        E.chave(c, PX + 6, PX + PW * 0.8 - 6, PY - 18, CLARO, ep(t, d11, 0.4), -24, 6)
        E.foco(c, t, d11 + 0.3, 0.4, lambda a: centro(c, "ganhar 1 sobre 4", PX + PW * 0.4, PY - 60, 56, "g", BR, a))
        E.frase(c, t, e11, [("1/4", "g", 110, BR), ("=", "g", 100, CLARO), ("25%", "g", 120, CLARO)], W / 2, 920, "center", 0.3)
    E.saida(c, t, C["s12"] - 0.1, barra)
    if t < C["s12"] - 0.1:
        return
    E.frase(c, t, C["s12"] + 0.1, [("perdeu", "i", 70, CLARO)], 560, 170, "center")
    E.frase(c, t, C["s12"] + 0.1, [("ganha", "i", 70, CLARO)], 1200, 170, "center")
    for i, (ti, n1, d1, n2, d2, pct) in enumerate(((a12, 1, 5, 1, 4, "25%"), (b12, 1, 4, 1, 3, "≈ 33%"), (c12, 1, 10, 1, 9, "≈ 11%"))):
        y = 280 + i * 190
        E.foco(c, t, ti, 0.45, lambda a, y=y, n1=n1, d1=d1: E.fracao(c, n1, d1, 560, y, 80, BR, a))
        p = ep(t, ti + 0.3, 0.4)
        if p > 0:
            M.arrow(c, 680, y + 10, 1060, y + 10, CLARO, p, 5, 18, p)
        E.foco(c, t, ti + 0.5, 0.45, lambda a, y=y, n2=n2, d2=d2: E.fracao(c, n2, d2, 1200, y, 80, CLARO, a))
        cen(c, t, ti + 0.8, pct, 1480, y + 40, 72, BR)
    E.frase(c, t, d12, ps("o que falta é o mesmo, mas vai", "i", 64, CLARO) + [("sobre o que ficou", "g", 64, BR)], W / 2, 860, "center", 0.1)
    E.frase(c, t, e12, [("17%?", "g", 84, BR)], 720, 990, "center")
    if t >= e12 + 1.0:
        E.risco(c, 620, 1005, 830, 935, t, e12 + 1.0, largura=10)
    E.foco(c, t, f12, 0.5, lambda a: E.pilula(c, "1 ÷ fator", 1150, 965, 64, "g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s13"] + 0.6, [("sorveteria", "g", 72)], XE + 470, 170)
    sobe = ease_io(prog(t, C["s14"] - 0.2, 0.8))
    k = lerp(1.0, 0.8, sobe)
    grupo(c, W / 2, 470, k, lambda: (c.translate(0, -sobe * 100 / k),
                                     fluxo(c, t, 470, "R$ 40.000", "− 75%", "?", a13, b13, b13 + 0.5, rot=("verão, por mês", "inverno"))))
    E.saida(c, t, C["s14"] - 0.2, lambda: (E.frase(c, t, c13, ps("quantos % precisam", "i", 80) + [("subir", "g", 80, COR)], W / 2, 750, "center", 0.12),
                                          E.frase(c, t, c13 + 1.4, ps("para voltar ao que eram?", "i", 80), W / 2, 870, "center", 0.12)))
    E.relogio(c, t, C["s14.a"], 960, 780, 120)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a15, b15, c15, d15, e15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]
    a16, b16, c16, d16, e16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"]

    def cima():
        fluxo(c, t, 470, "R$ 40.000", [(C["s15"], "− 75%"), (a16, "× 0,25")], [(C["s15"], "?"), (b15, "R$ 10.000")], C["s15"], C["s15"], C["s15"],
              rot=("verão", "inverno"))
        volta(c, t, c15, XA, XD, 570, [(c15 + 0.4, "+ R$ 30.000"), (e15, "+ 300%")], alto=110)
    topo(c, t, cima, yf=230)

    def quinze():
        E.frase(c, t, a15, [("75% de 40.000", "g", 76), ("=", "g", 76, TINTA2), ("30.000", "g", 80)], W / 2, 560, "center", 0.25)
        E.frase(c, t, c15, ps("ganhar 30.000", "i", 72) + [("sobre 10.000", "g", 72, COR)], W / 2, 690, "center", 0.12)
        E.frase(c, t, d15, [("30.000 ÷ 10.000", "g", 84), ("=", "g", 84, TINTA2), ("3", "g", 90, COR)], W / 2, 830, "center", 0.25)
        E.foco(c, t, e15, 0.5, lambda a: num_bola(c, "300%", 1600, 800, 110, 64, a))
    E.saida(c, t, C["s16"] - 0.1, quinze)
    if t < C["s16"] - 0.1:
        return
    E.frase(c, t, a16, ps("pelo fator:", "i", 72) + [("caiu 75%", "g", 72), ("→", "g", 72, TINTA2), ("0,25", "g", 76, COR)], W / 2, 520, "center", 0.15)
    E.frase(c, t, b16, [("1 ÷ 0,25", "g", 80), ("=", "g", 80, TINTA2), ("4", "g", 90, COR)], 560, 650, "center", 0.25)
    E.frase(c, t, c16, ps("o inteiro + 3 vezes ele:", "i", 62) + [("+300%", "g", 66, COR)], 1360, 650, "center", 0.1)
    E.frase(c, t, d16, [("10.000 × 4", "g", 76), ("=", "g", 76, TINTA2), ("40.000", "g", 80, CERTO)], W / 2, 800, "center", 0.25)
    selo_em(c, t, d16 + 1.2, 1500, 775, 42)
    E.frase(c, t, e16, ps("quem respondeu 75% parou em", "i", 64, TINTA2) + [("17.500", "g", 70, ERRADO)], W / 2, 950, "center", 0.1)
    selo_em(c, t, e16 + 1.6, 1560, 925, 38, False)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]

    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.frase(c, t, a17, ps("para voltar:", "i", 84) + [("1 ÷ fator", "g", 96, COR)], W / 2, 400, "center", 0.15)
        E.frase(c, t, b17, ps("ou:", "i", 76) + [("o que falta", "g", 80)] + ps("sobre", "i", 76) + [("o que ficou", "g", 80)], W / 2, 580, "center", 0.15)
        E.frase(c, t, c17, ps("a volta sempre pede", "i", 76) + [("uma % maior", "g", 80, COR)], W / 2, 800, "center", 0.12)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    a18, b18, c18, d18, e18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"], C["s18.e"]
    E.frase(c, t, C["s18"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s18"] + 0.6, [("Ponto percentual", "g", 116, COR)], XE, 450)
    E.frase(c, t, a18, [("de 8% para 10%:", "i", 76)], XE, 600)
    E.frase(c, t, b18, [("+2 pontos", "g", 76, COR)], XE, 720)
    E.frase(c, t, c18, ps("e também", "i", 76) + [("+25%", "g", 76, COR)], XE + 420, 720, "left", 0.12)
    E.foco(c, t, d18, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=a))
    p = ease_io(prog(t, d18 + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, d18 + 0.2, 0.4))
    E.frase(c, t, e18, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, cem=b_cem, fator=b_fator, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
