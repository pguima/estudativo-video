"""Visual — Estudativo · MAT-POR-010: aumentos e descontos sucessivos.

Linguagem da trilha Porcentagem (MAT-POR-006): cartao() = valor de antes (contorno escuro) ou de depois (cor da matéria);
maquina() = o fator. Peças novas desta aula, para as seguintes: cadeia() = valor → [fator] → valor → [fator] → valor;
funde() = duas máquinas que deslizam e viram uma só, com o fator multiplicado (1,1 × 1,2 = 1,32). Todo instante vem de C[...]."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-010_aumentos_e_descontos_sucessivos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("cem", "fatores", "sobedesce", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert round(100 * 1.1, 6) == 110 and round(110 * 0.2, 6) == 22 and 110 + 22 == 132 and round(1.1 * 1.2, 6) == 1.32
assert round(1.2 * 0.8, 6) == 0.96 and round(120 * 0.2, 6) == 24 and 120 - 24 == 96 and round(100 * 0.8 * 1.2, 6) == 96
assert 10 + 20 + 10 * 20 / 100 == 32 and 20 - 20 + 20 * (-20) / 100 == -4 and round(1.25 * 0.8, 6) == 1 and 125 * 8 == 1000
assert 25 - 20 + 25 * (-20) / 100 == 0


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        maquina(c, t, ka, 560, 380, "+ 10%", 96)
        E.foco(c, t, ka + 0.3, 0.4, lambda a: centro(c, "1º mês", 560, 250, 58, "i", TINTA2, a))
        maquina(c, t, kb, 1360, 380, "+ 20%", 96)
        E.foco(c, t, kb + 0.3, 0.4, lambda a: centro(c, "2º mês", 1360, 250, 58, "i", TINTA2, a))
        p = ep(t, kb + 0.3, 0.5)
        if p > 0:
            M.arrow(c, 720, 380, 1200, 380, TINTA2, p, 6, 20, p)
        ti = lerp(kb, kc, 0.55)
        E.frase(c, t, ti, ps("subiu", "i", 90) + [("30%?", "g", 110, ERRADO)], 700, 690, "center", 0.2)
        if t >= kc + 0.3:
            E.risco(c, 640, 710, 900, 610, t, kc + 0.3, largura=14)
        E.foco(c, t, kc + 0.6, 0.6, lambda a: num_bola(c, "32%", 1300, 650, 150, 100, a))
        E.frase(c, t, kc + 0.6, ps("subiu", "i", 76, COR), 1300, 860, "center")
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.2), [("juntar", "g", 110, COR)], XE, 470, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), ps("aumentos e descontos", "i", 90), XE, 610, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.6), [("seguidos", "g", 110, COR)], XE, 760, passo=0.12)
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
    E.frase(c, t, lerp(kb, kc, 0.2), [("+15%", "g", 64, TINTA2), ("=", "g", 64, TINTA2), ("× 1,15", "g", 64, COR)], x + 44, 375, "left", 0.25)
    E.frase(c, t, lerp(kb, kc, 0.6), [("−20%", "g", 64, TINTA2), ("=", "g", 64, TINTA2), ("× 0,8", "g", 64, COR)], x + 44, 465, "left", 0.25)
    p = ep(t, kc, 0.5)
    E.caixa_pontilhada(c, x, 570, w, 210, p, prog_=p)
    E.frase(c, t, kc + 0.1, [("multiplicar com vírgula:", "i", 62)], x + 44, 658)
    E.frase(c, t, kc + 0.3, [("1,1 × 1,2", "g", 64, COR)], x + 44, 742)
    q = ease_io(prog(t, kc - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(470, 750, q), ep(t, kb, 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- com cem reais ----------------
XS5 = [240, 600, 960, 1320, 1680]


def b_cem(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    E.frase(c, t, C["s04"] + 0.1, ps("veja com", "i", 76) + [("R$ 100", "g", 76, COR)], W / 2, 150, "center", 0.14)
    cadeia(c, t, 420, ["R$ 100", "R$ 110", "R$ 132"], ["+ 10%", "+ 20%"], [a4, c4, c5], [b4, a5 + 0.3], XS5, ("antes", "1º mês", "2º mês"))
    if t >= a5:
        q = ep(t, a5 + 0.2, 0.5)
        w = larg_cartao(["R$ 110"], 76)
        E.caixa_pontilhada(c, 960 - w / 2 - 18, 420 - 84, w + 36, 168, q, COR, prog_=q)
        E.foco(c, t, a5 + 0.4, 0.45, lambda a: centro(c, "sobre 110, não sobre 100", 960, 600, 54, "g", COR, a))
    E.saida(c, t, a5 - 0.1, lambda: E.frase(c, t, b4, [("10% de 100", "g", 80), ("=", "g", 80, TINTA2), ("10", "g", 84, COR)], W / 2, 760, "center", 0.25))
    E.frase(c, t, b5, [("20% de 110", "g", 80), ("=", "g", 80, TINTA2), ("22", "g", 84, COR)], W / 2, 760, "center", 0.25)
    E.frase(c, t, d5, [("32", "g", 84, COR)] + ps("a mais em cada 100:", "i", 80) + [("32%", "g", 90, COR)], W / 2, 920, "center", 0.15)


# ---------------- com os fatores ----------------
def b_fatores(c, t, C, b):
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]

    def seis():
        E.frase(c, t, C["s06"] + 0.1, ps("com os", "i", 80) + [("fatores", "g", 80, COR)], W / 2, 170, "center", 0.14)
        E.foco(c, t, a6, 0.4, lambda a: centro(c, "+10%", 640, 300, 60, "g", TINTA2, a))
        E.foco(c, t, b6, 0.4, lambda a: centro(c, "+20%", 1280, 300, 60, "g", TINTA2, a))
        funde(c, t, a6, d6, 640, 1280, 450, "× 1,1", "× 1,2", "× 1,32", 88)
        E.frase(c, t, c6, ps("cada aumento multiplica:", "i", 70) + [("multiplique os fatores", "g", 70, COR)], W / 2, 700, "center", 0.12)
        E.frase(c, t, d6, [("1,1 × 1,2", "g", 96), ("=", "g", 96, TINTA2), ("1,32", "g", 100, COR)], W / 2, 880, "center", 0.3)
    E.saida(c, t, C["s07"] - 0.1, seis)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"] + 0.1, ps("como se lê", "i", 84) + [("1,32?", "g", 90, COR)], W / 2, 200, "center", 0.14)
    s, y = 230, 560
    E.foco(c, t, C["s07"] + 0.4, 0.5, lambda a: E.escreve(c, "1", 600, y, s, "g", TINTA, a))
    E.foco(c, t, C["s07"] + 0.4, 0.5, lambda a: E.escreve(c, ",32", 600 + E.larg("1", "g", s) + 6, y, s, "g", COR, a))
    x1 = 600 + E.larg("1", "g", s) / 2
    x2 = 600 + E.larg("1", "g", s) + 6 + E.larg(",32", "g", s) / 2
    E.foco(c, t, a7, 0.45, lambda a: (centro(c, "o preço", x1 - 60, 700, 60, "i", TINTA, a), centro(c, "inteiro", x1 - 60, 770, 60, "g", TINTA, a)))
    E.foco(c, t, b7, 0.45, lambda a: (centro(c, "0,32", x2 + 40, 700, 60, "g", COR, a), centro(c, "veio a mais", x2 + 40, 770, 60, "i", COR, a)))
    E.foco(c, t, c7, 0.5, lambda a: E.pilula(c, "+ 32% de aumento", W / 2, 920, 72, "g", a=a))


# ---------------- sobe e desce ----------------
def b_sobedesce(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9, e9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]
    a10, b10 = C["s10.a"], C["s10.b"]

    def oito():
        E.frase(c, t, C["s08"] + 0.1, ps("o caso que", "i", 80) + [("mais engana", "g", 80, ERRADO)], W / 2, 160, "center", 0.14)
        E.foco(c, t, a8, 0.4, lambda a: centro(c, "sobe 20%", 640, 300, 60, "g", TINTA2, a))
        E.foco(c, t, a8 + 0.8, 0.4, lambda a: centro(c, "cai 20%", 1280, 300, 60, "g", TINTA2, a))
        funde(c, t, a8, c8, 640, 1280, 450, [(a8, "+ 20%"), (b8, "× 1,2")], [(a8 + 0.4, "− 20%"), (b8 + 0.4, "× 0,8")], "× 0,96", 88)
        E.frase(c, t, lerp(a8, b8, 0.55), ps("parece que volta ao mesmo...", "i", 70, TINTA2), W / 2, 670, "center", 0.1)
        E.frase(c, t, c8, [("1,2 × 0,8", "g", 96), ("=", "g", 96, TINTA2), ("0,96", "g", 100, COR)], W / 2, 830, "center", 0.3)
        E.frase(c, t, a9, [("fator < 1:", "i", 72, TINTA2), ("fica com 96%", "g", 72)], 620, 970, "center", 0.15)
        E.frase(c, t, b9, [("4% menor", "g", 80, COR)], 1380, 970, "center")
    E.saida(c, t, c9 - 0.1, oito)
    if t < c9 - 0.1:
        return

    def nove():
        E.frase(c, t, c9, ps("com", "i", 76) + [("R$ 100", "g", 76, COR)], W / 2, 150, "center", 0.14)
        cadeia(c, t, 400, ["R$ 100", "R$ 120", "R$ 96"], ["× 1,2", "× 0,8"], [c9, c9 + 0.6, e9], [c9 + 0.3, d9], XS5, ("antes", "sobe", "cai"))
        E.frase(c, t, d9, [("20% de 120", "g", 76), ("=", "g", 76, TINTA2), ("24", "g", 80, COR)], W / 2, 660, "center", 0.25)
        E.frase(c, t, e9 + 0.3, [("120 − 24", "g", 76), ("=", "g", 76, TINTA2), ("96", "g", 80, COR)], W / 2, 790, "center", 0.25)
    E.saida(c, t, a10 - 0.1, nove)
    if t < a10 - 0.1:
        return
    E.frase(c, t, a10, ps("e a ordem", "i", 80) + [("não importa", "g", 80, COR)], W / 2, 150, "center", 0.14)
    cadeia(c, t, 400, ["R$ 100", "R$ 80", "R$ 96"], ["× 0,8", "× 1,2"], [a10, a10 + 1.0, a10 + 1.6], [a10 + 0.5, a10 + 1.3], XS5,
           ("antes", "cai", "sobe"))
    E.frase(c, t, b10, [("0,8 × 1,2", "g", 90), ("=", "g", 90, TINTA2), ("1,2 × 0,8", "g", 90), ("=", "g", 90, TINTA2), ("0,96", "g", 96, COR)],
            W / 2, 760, "center", 0.25)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    E.frase(c, t, C["s11"] + 0.1, [("o erro", "g", 96, ERRADO)] + ps("comum", "i", 96), W / 2, 170, "center", 0.14)
    E.frase(c, t, a11, ps("somar as", "i", 80) + [("porcentagens", "g", 80, ERRADO)], W / 2, 320, "center", 0.14)
    for y, txt_, ti in ((500, ("10 + 20", "30%"), b11), (650, ("20 − 20", "0%"), c11)):
        E.frase(c, t, ti, [(txt_[0], "g", 90), ("=", "g", 90, TINTA2), (txt_[1], "g", 96, ERRADO)], W / 2, y, "center", 0.25)
        selo_em(c, t, ti + 0.9, 1360, y - 30, 44, False)
    E.frase(c, t, d11, ps("cada % vale sobre", "i", 74) + [("o preço daquele momento", "g", 74, COR)], W / 2, 870, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a12, b12, c12, d12, e12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
    a13, b13, c13, d13, e13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
    a14, b14 = C["s14.a"], C["s14.b"]

    def doze():
        E.frase(c, t, C["s12"] + 0.1, [("o atalho:", "g", 70, BR)] + ps("para duas variações", "i", 74, CLARO), W / 2, 150, "center", 0.15)
        E.frase(c, t, a12, [("a + b", "g", 110, BR)], 640, 360, "right")
        E.frase(c, t, b12, [("+", "g", 110, CLARO), ("a × b ÷ 100", "g", 110, CLARO)], 680, 360, "left", 0.3)
        E.frase(c, t, c12, [("10 + 20", "g", 84, BR), ("=", "g", 84, CLARO), ("30", "g", 84, BR)], 640, 580, "right", 0.25)
        E.frase(c, t, d12, [("+", "g", 84, CLARO), ("10 × 20 ÷ 100 = 2", "g", 84, CLARO)], 680, 580, "left", 0.25)
        E.frase(c, t, e12, [("total:", "i", 84, CLARO), ("32%", "g", 120, BR)], W / 2, 820, "center", 0.25)
    E.saida(c, t, C["s13"] - 0.1, doze)
    if C["s13"] - 0.1 <= t < C["s14"] - 0.1:
        def treze():
            E.frase(c, t, a13, ps("o 2º aumento vale", "i", 74, CLARO) + [("sobre o 1º", "g", 74, BR)], W / 2, 200, "center", 0.12)
            E.frase(c, t, b13, [("20% dos R$ 10", "g", 80, BR), ("=", "g", 80, CLARO), ("R$ 2 extras", "g", 80, CLARO)], W / 2, 360, "center", 0.25)
            E.frase(c, t, c13, ps("desconto entra com", "i", 74, CLARO) + [("sinal de menos", "g", 74, BR)], W / 2, 540, "center", 0.12)
            E.frase(c, t, lerp(c13, d13, 0.5), [("20 − 20 = 0", "g", 80, BR)], W / 2, 680, "center")
            E.frase(c, t, d13, [("+", "g", 80, CLARO), ("20 × (−20) ÷ 100 = −4", "g", 80, CLARO)], W / 2, 810, "center", 0.25)
            E.frase(c, t, e13, [("−4%:", "g", 96, BR)] + ps("4% a menos", "i", 84, CLARO), W / 2, 960, "center", 0.2)
        E.saida(c, t, C["s14"] - 0.1, treze)
    if t < C["s14"] - 0.1:
        return
    E.frase(c, t, a14, [("3 variações ou mais?", "g", 100, BR)], W / 2, 400, "center")
    E.foco(c, t, b14, 0.5, lambda a: E.pilula(c, "multiplique os fatores", W / 2, 640, 84, "g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    sobe = ease_io(prog(t, C["s16"] - 0.2, 0.8))
    k = lerp(1.0, 0.8, sobe)

    def duas():
        maquina(c, t, a15, 640, 420, "+ 25%", 96)
        E.foco(c, t, a15 + 0.3, 0.4, lambda a: centro(c, "aumento", 640, 290, 58, "i", TINTA2, a))
        maquina(c, t, b15, 1280, 420, "− 20%", 96)
        E.foco(c, t, b15 + 0.3, 0.4, lambda a: centro(c, "desconto", 1280, 290, 58, "i", TINTA2, a))
        p = ep(t, b15 + 0.2, 0.5)
        if p > 0:
            M.arrow(c, 800, 420, 1120, 420, TINTA2, p, 6, 20, p)
    grupo(c, W / 2, 420, k, lambda: (c.translate(0, -sobe * 80 / k), duas()))
    E.saida(c, t, C["s16"] - 0.2, lambda: (E.frase(c, t, c15, ps("o cliente paga", "i", 80) + [("mais, menos ou o mesmo", "g", 80, COR)], W / 2, 720, "center", 0.12),
                                          E.frase(c, t, c15 + 1.6, ps("que antes do aumento?", "i", 80), W / 2, 840, "center", 0.12)))
    E.relogio(c, t, C["s16.a"], 960, 760, 130)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a17, b17, c17, d17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]

    def dezessete():
        funde(c, t, C["s17"], d17 - 0.4, 640, 1280, 260, [(C["s17"], "+ 25%"), (a17, "× 1,25")], [(C["s17"] + 0.3, "− 20%"), (a17 + 0.4, "× 0,8")], "× 1", 80)
        E.frase(c, t, b17, ps("sem as vírgulas:", "i", 70) + [("125 × 8 = 1000", "g", 80)], W / 2, 520, "center", 0.15)
        E.frase(c, t, c17, ps("três casas:", "i", 70) + [("1,000", "g", 80), ("=", "g", 80, TINTA2), ("1", "g", 90, COR)], W / 2, 670, "center", 0.15)
        E.frase(c, t, d17, ps("fator 1 não muda nada:", "i", 70) + [("paga o mesmo", "g", 76, CERTO)], W / 2, 860, "center", 0.12)
        selo_em(c, t, d17 + 1.2, 1700, 830, 44)
    E.saida(c, t, C["s18"] - 0.1, dezessete)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"] + 0.1, ps("pelo", "i", 80) + [("atalho", "g", 80, COR)], W / 2, 180, "center", 0.14)
    E.frase(c, t, a18, [("25 − 20", "g", 84), ("=", "g", 84, TINTA2), ("5", "g", 84)], W / 2, 360, "center", 0.25)
    E.frase(c, t, b18, [("25 × (−20) ÷ 100", "g", 84), ("=", "g", 84, TINTA2), ("−5", "g", 84)], W / 2, 500, "center", 0.25)
    E.frase(c, t, c18, [("5 − 5", "g", 96), ("=", "g", 96, TINTA2), ("0", "g", 110, CERTO)], W / 2, 660, "center", 0.25)
    selo_em(c, t, c18 + 1.0, 1250, 625, 46)
    E.frase(c, t, d18, ps("quem somou:", "i", 70, TINTA2) + [("5% a mais", "g", 76, ERRADO)], W / 2, 860, "center", 0.12)
    selo_em(c, t, d18 + 1.2, 1450, 835, 40, False)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a19, b19 = C["s19.a"], C["s19.b"]

    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        E.frase(c, t, a19, ps("porcentagens seguidas", "i", 84) + [("não se somam", "g", 84, ERRADO)], W / 2, 450, "center", 0.14)
        E.frase(c, t, b19, [("multiplique os fatores", "g", 90, COR)], W / 2, 640, "center")
        E.frase(c, t, b19 + 1.0, ps("e leia o resultado", "i", 80), W / 2, 760, "center", 0.14)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    E.saida(c, t, b20 - 0.1, lambda: (E.frase(c, t, C["s20"] + 0.2, ps("no teste:", "i", 80), W / 2, 330, "center"),
                                      E.frase(c, t, a20, [("1,25 × 0,8 = 1", "g", 110, COR)], W / 2, 520, "center"),
                                      E.frase(c, t, a20 + 1.2, ps("subir 25 e cair 20", "i", 80) + [("se desfazem", "g", 80, COR)], W / 2, 690, "center", 0.12)))
    if t < b20 - 0.1:
        return
    E.frase(c, t, b20, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, b20 + 0.3, [("Voltar ao valor", "g", 120, COR)], XE, 450)
    E.frase(c, t, b20 + 0.6, [("original", "g", 120, COR)], XE, 590)
    E.frase(c, t, lerp(b20, c20, 0.5), ps("quanto subir depois de uma queda?", "i", 70), XE, 740, "left", 0.1)
    E.foco(c, t, c20, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=a))
    p = ease_io(prog(t, c20 + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, c20 + 0.2, 0.4))
    E.frase(c, t, d20, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, cem=b_cem, fatores=b_fatores, sobedesce=b_sobedesce, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
