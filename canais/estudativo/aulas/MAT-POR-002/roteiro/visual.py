"""Visual — Estudativo · MAT-POR-002: calcular porcentagem de cabeça e na conta.
Linguagem da trilha Porcentagem (cartao, maquina, fluxo, volta, funde: as mesmas peças de MAT-POR-006): aqui a máquina aparece
pela primeira vez, quando "÷ 100" e "× 37" viram uma máquina só, "× 0,37". A vírgula que anda é E.anda.
A voz é real: os marcadores vêm de C[...] e, onde a tela precisa da palavra exata, fala(cena, palavra) lê o tempos.json."""
import json
import math
from pathlib import Path
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-002_calcular_porcentagem.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("dez", "conta", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 80 // 10 == 8 and 345 / 10 == 34.5 and 8 / 2 == 4 and 8 * 2 == 16 and 8 + 4 == 12 and 80 / 100 == 0.8
assert 240 * 37 == 8880 and round(240 * 0.37, 2) == 88.8 and 240 * 40 / 100 == 96 == 4 * 24 and 88.8 < 96
assert 8 * 50 / 100 == 50 * 8 / 100 == 4
assert 140 / 10 == 14 and 14 / 2 == 7 and 14 + 7 == 21 and 140 * 15 == 2100 and round(140 * 0.15, 2) == 21


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- tempo da palavra dita ----------------
_TEMPOS = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))
_CENAS = {s["id"]: s for s in _TEMPOS["scenes"]}


def fala(sid, palavra, k=1):
    """instante em que a k-ésima `palavra` da cena começa a ser dita"""
    s = _CENAS[sid]
    n = 0
    for tk in s["tokens"]:
        if tk["disp"].lower().strip(".,:;?!") == palavra:
            n += 1
            if n == k:
                return s["start"] + tk["t0"]
    raise KeyError((sid, palavra, k))


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




# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb = C["s01.a"], C["s01.b"]

    def um():
        E.frase(c, t, ka, [("15%", "g", 220, COR), ("de", "i", 200), ("80", "g", 220)], W / 2, 450, "center", 0.4)
        E.frase(c, t, fala("s01", "de"), ps("de cabeça,", "i", 80) + ps("em poucos segundos", "i", 80), W / 2, 640, "center", 0.12)
        E.frase(c, t, fala("s01", "sem"), ps("sem decorar", "i", 80) + [("tabela", "g", 80, TINTA)], W / 2, 760, "center", 0.12)
        E.foco(c, t, kb, 0.5, lambda a: num_bola(c, "12", W / 2, 920, 100, 110, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, fala("s02", "porcentagem"), [("porcentagem", "g", 110, COR)], XE, 500)
        E.frase(c, t, fala("s02", "cabeça"), ps("de", "i", 90) + [("cabeça", "g", 100)], XE, 650, passo=0.12)
        E.frase(c, t, fala("s02", "na"), ps("e na", "i", 90) + [("conta", "g", 100)], XE, 800, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "Trocar % por", "fração ou decimal"), ("s03.c", "Fração de", "uma quantidade"), ("s03.d", "Andar com", "a vírgula"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    alvo = [x + w - 30, [170 + i * 240 + 170 for i in range(3)]]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    py = lerp(lerp(alvo[1][0], alvo[1][1], q1), alvo[1][2], q2)
    E.cursor(c, alvo[0], py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, fala("s03", "se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- dez por cento ----------------
def b_dez(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]

    def quatro():
        E.frase(c, t, C["s04"] + 0.3, ps("comece pelo", "i", 80) + [("mais útil", "g", 80, COR)], XE, 180, "left", 0.12)
        E.foco(c, t, a4, 0.5, lambda a: E.escreve(c, "10%", XE, 470, 220, "g", COR, a))
        cen(c, t, b4 - 0.3, "=", 720, 440, 140, TINTA2)
        E.foco(c, t, b4, 0.5, lambda a: E.fracao(c, 1, 10, 900, 400, 150, TINTA, a))
        E.frase(c, t, fala("s04", "fração"), ps("fração de uma quantidade:", "i", 66, TINTA2), XE, 680, "left", 0.1)
        E.frase(c, t, fala("s04", "divide"), ps("divide pelo", "i", 72) + [("de baixo", "g", 72, COR)], XE, 790, "left", 0.12)
        E.frase(c, t, fala("s04", "multiplica"), ps("multiplica pelo", "i", 72) + [("de cima", "g", 72, COR)], XE, 890, "left", 0.12)
        E.foco(c, t, c4, 0.5, lambda a: E.pilula(c, "÷ 10", 1500, 420, 120, "g", a=a))
        E.frase(c, t, c4 + 0.4, ps("com 1/10, é só", "i", 64, TINTA2), 1500, 620, "center", 0.1)
        E.frase(c, t, c4 + 0.8, [("dividir por 10", "g", 64)], 1500, 710, "center")
    E.saida(c, t, C["s05"] - 0.1, quatro)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"] + 0.3, [("÷ 10", "g", 90, COR)] + ps("é andar a vírgula", "i", 80), W / 2, 180, "center", 0.14)
    E.frase(c, t, fala("s05", "uma"), [("1 casa", "g", 80, COR)] + ps("para a esquerda", "i", 80), W / 2, 290, "center", 0.14)
    s = 150
    cl = E.casa(s)
    for y, ti, rot, dig, pos, nova, tv, tj, res in ((540, b5, "10% de 80", "80", 2, 1, fala("s05", "dá") - 0.3, fala("s05", "dá"), "= 8"),
                                                 (820, c5, "10% de 345", "345", 3, 2, fala("s05", "dá", 2) - 0.4, fala("s05", "dá", 2), None)):
        E.frase(c, t, ti, [(rot, "g", 84)], 900, y, "right")
        cen(c, t, ti + 0.3, "→", 980, y - 10, 84, TINTA2)
        E.foco(c, t, ti + 0.4, 0.45, lambda q, dig=dig, pos=pos, nova=nova, tv=tv, tj=tj, y=y: E.anda(c, t, dig, pos, [(tj, nova)], 1080, y, s, tv=tv))
        if res:
            E.foco(c, t, fala("s05", "oito", 1), 0.45, lambda a, y=y: E.escreve(c, res, 1080 + 3 * cl, y, 120, "g", CERTO, a))


# ---------------- montar as outras ----------------
def b_montar(c, t, C, b):
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    a7, b7, c7, d7, e7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"]
    X1, X2, X3 = 560, 1000, 1400

    def seis():
        E.frase(c, t, C["s06"] + 0.3, ps("com o", "i", 76) + [("10%", "g", 76, COR)] + ps("na mão, monte as outras", "i", 76), W / 2, 170, "center", 0.12)
        linhas = ((330, C["s06"] + 0.8, "10%", None, None, "8", C["s06"] + 1.2, TINTA),
                  (560, a6, "5%", "metade", "÷ 2", "4", b6, COR),
                  (790, c6, "20%", "dobro", "× 2", "16", d6, COR))
        for y, ti, pc, nome, op, res, tr, cor in linhas:
            cen(c, t, ti, pc + " de 80", X1, y, 90, TINTA)
            if op:
                E.ponte(c, t, ti + 0.6, X1 + 250, X3 - 150, y - 30, op, None, 54)
                E.frase(c, t, ti + 0.9, ps(nome, "i", 54, TINTA2), X2, y + 55, "center")
            else:
                cen(c, t, ti + 0.3, "=", X2, y, 90, TINTA2)
            E.foco(c, t, tr, 0.45, lambda a, res=res, y=y, cor=cor: num_bola(c, res, X3 + 40, y - 30, 70, 76, a) if cor == COR else
                   centro(c, res, X3 + 40, y, 100, "g", TINTA, a))
    E.saida(c, t, C["s07"] - 0.1, seis)
    if t < C["s07"]:
        return

    def sete():
        y = 330
        E.linha(c, t, [("15%", "g", 110, COR, a7), ("=", "g", 110, TINTA2, fala("s07", "é")), ("10%", "g", 110, TINTA, fala("s07", "dez")),
                       ("+", "g", 110, TINTA2, fala("s07", "mais")), ("5%", "g", 110, TINTA, fala("s07", "cinco"))], XE, y)
        E.linha(c, t, [("8", "g", 110, TINTA, b7), ("+", "g", 110, TINTA2, fala("s07", "mais", 2)), ("4", "g", 110, TINTA, fala("s07", "quatro")),
                       ("=", "g", 110, TINTA2, fala("s07", "dá"))], XE + 190, y + 190)
        E.foco(c, t, fala("s07", "doze"), 0.5, lambda a: num_bola(c, "12", XE + 820, y + 150, 90, 100, a))
        E.frase(c, t, c7, [("15% de 80", "g", 70)], 1250, y + 140, "left")
        E.frase(c, t, c7 + 0.3, ps("como no começo", "i", 66, COR), 1250, y + 230, "left", 0.12)
    E.saida(c, t, d7 - 0.2, sete)
    if t < d7 - 0.2:
        return
    E.frase(c, t, d7 - 0.1, ps("precisa de", "i", 84) + [("1%?", "g", 84, COR)], W / 2, 200, "center", 0.12)
    E.frase(c, t, d7 + 0.2, [("÷ 100", "g", 84, COR)] + ps("= vírgula", "i", 80) + [("2 casas", "g", 84, COR)], W / 2, 340, "center", 0.14)
    s, y = 170, 680
    E.frase(c, t, e7, [("1% de 80", "g", 90)], 680, y, "right")
    cen(c, t, e7 + 0.3, "→", 770, y - 10, 90, TINTA2)
    cl = E.casa(s)
    x0 = 860 + cl
    E.foco(c, t, e7 + 0.3, 0.45, lambda q: E.anda(c, t, "80", 2, [(fala("s07", "dá"), 0)], x0, y, s, tv=fala("s07", "dá") - 0.3))
    E.foco(c, t, fala("s07", "zero"), 0.45, lambda a: E.escreve(c, "= 0,8", x0 + 2.4 * cl, y, 110, "g", CERTO, a))


# ---------------- na conta ----------------
def b_conta(c, t, C, b):
    a8, b8 = C["s08.a"], C["s08.b"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]

    def oito():
        E.frase(c, t, C["s08"] + 0.3, ps("mas e", "i", 84), W / 2, 260, "center")
        E.frase(c, t, a8, [("37%", "g", 200, COR), ("de", "i", 180), ("240?", "g", 200)], W / 2, 520, "center", 0.4)
        E.frase(c, t, fala("s08", "montar"), ps("de cabeça dá", "i", 76) + [("trabalho", "g", 76, ERRADO)], W / 2, 700, "center", 0.12)
        E.foco(c, t, b8, 0.5, lambda a: E.pilula(c, "aqui entra o decimal", W / 2, 880, 70, "g", a=a))
    E.saida(c, t, C["s09"] - 0.1, oito)
    if C["s09"] <= t < C["s10"]:
        def nove():
            E.linha(c, t, [("37%", "g", 110, COR, C["s09"] + 0.3), ("=", "g", 110, TINTA2, a9 - 0.2)], 760, 300, "right")
            E.foco(c, t, a9, 0.5, lambda a: E.fracao(c, 37, 100, 900, 260, 110, TINTA, a))
            E.frase(c, t, fala("s09", "trinta", 2) + 0.4, ps("37 centésimos", "i", 60, TINTA2), 1240, 290, "left", 0.1)
            y = 680
            cartao(c, t, b9 - 0.4, 300, y, "240", "total", False, 84)
            funde(c, t, b9, c9, 760, 1160, y, "÷ 100", "× 37", "× 0,37", 76)
            p = ep(t, b9 - 0.1, 0.5)
            if p > 0:
                M.arrow(c, 300 + 130, y, 600, y, TINTA2, p, 6, 20, p)
                M.arrow(c, 1320, y, 1500, y, TINTA2, p, 6, 20, p)
            cartao(c, t, b9 - 0.2, 1640, y, "?", "37%", True, 84)
            E.frase(c, t, c9 + 0.8, ps("tudo de", "i", 66) + [("uma vez", "g", 66, COR)], W / 2, 960, "center", 0.12)
        E.saida(c, t, C["s10"] - 0.1, nove)
    if C["s10"] <= t < C["s11"]:
        def dez():
            E.frase(c, t, a10, [("240 × 0,37", "g", 110)], W / 2, 220, "center")
            E.frase(c, t, b10, ps("ignore a vírgula:", "i", 70, TINTA2), XE, 430, "left", 0.1)
            E.linha(c, t, [("240 × 37", "g", 100, TINTA, fala("s10", "duzentos", 2)), ("=", "g", 100, TINTA2, fala("s10", "dá")),
                           ("8880", "g", 100, COR, fala("s10", "oito"))], XE + 640, 430)
            E.frase(c, t, c10, ps("2 casas de volta:", "i", 70, TINTA2), XE, 720, "left", 0.1)
            s = 130
            cl = E.casa(s)
            x0 = XE + 700
            E.foco(c, t, c10 + 0.2, 0.45, lambda q: E.anda(c, t, "8880", 4, [(fala("s10", "duas") + 0.3, 2)], x0, 720, s, tv=c10 + 0.4))
            E.chave(c, x0 + 2 * cl + 4, x0 + 4 * cl - 4, 760, COR, ep(t, fala("s10", "casas"), 0.4), 24, 6)
            E.foco(c, t, fala("s10", "oitenta", 2), 0.5, lambda a: num_bola(c, "88,8", 1600, 690, 130, 92, a))
        E.saida(c, t, C["s11"] - 0.1, dez)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11"] + 0.3, ps("confira", "i", 84, COR) + ps("de cabeça", "i", 84), W / 2, 190, "center", 0.12)
    E.linha(c, t, [("37%", "g", 96, TINTA, fala("s11", "trinta")), ("<", "g", 96, TINTA2, a11), ("40%", "g", 96, COR, fala("s11", "quarenta"))], W / 2, 360, "center")
    E.linha(c, t, [("40% de 240", "g", 84, TINTA, fala("s11", "quarenta", 2)), ("=", "g", 84, TINTA2, fala("s11", "é", 2)),
                   ("4 × 24", "g", 84, TINTA, fala("s11", "quatro")), ("=", "g", 84, TINTA2, b11 - 0.2), ("96", "g", 84, COR, b11)], W / 2, 530, "center")
    # reta de 0 a 240 com 88,8 logo abaixo de 96
    x0, x1, yr = 360, 1560, 790
    px = lambda v: x0 + (x1 - x0) * v / 240
    p = ep(t, fala("s11", "oitenta"), 0.6)
    if p > 0:
        M.line(c, x0, yr, x0 + (x1 - x0) * p, yr, TINTA, 1.0, 6)
        for v in (0, 240):
            E.foco(c, t, fala("s11", "oitenta"), 0.4, lambda a, v=v: (M.line(c, px(v), yr - 18, px(v), yr + 18, TINTA, a, 6),
                                                                       centro(c, str(v), px(v), yr + 80, 52, "g", TINTA2, a)))
        E.foco(c, t, fala("s11", "oitenta") + 0.3, 0.4, lambda a: (c.drawCircle(px(96), yr, 16, M.paint(COR, a)),
                                                                   centro(c, "96", px(96) + 20, yr - 40, 56, "g", COR, a)))
        E.foco(c, t, fala("s11", "ficou"), 0.4, lambda a: (c.drawCircle(px(88.8), yr, 16, M.paint(CERTO, a)),
                                                           centro(c, "88,8", px(88.8) - 70, yr + 80, 56, "g", CERTO, a)))
    E.foco(c, t, c11, 0.45, lambda a: E.selo(c, 1700, 520, 60, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    E.frase(c, t, C["s12"] + 0.3, [("o erro:", "g", 96, ERRADO)] + ps("esquecer as", "i", 96) + [("casas", "g", 96)], W / 2, 190, "center", 0.12)
    E.linha(c, t, [("37% de 240", "g", 100, TINTA, fala("s12", "multiplica")), ("=", "g", 100, TINTA2, fala("s12", "para")),
                   ("8880?", "g", 100, ERRADO, b12)], W / 2, 400, "center")
    if t >= d12 + 0.5:
        E.risco(c, 1080, 420, 1440, 300, t, d12 + 0.5, largura=14)
    x, w, y, h = 360, 1200, 600, 130
    E.foco(c, t, c12 - 0.2, 0.5, lambda a: (E.barra_fatias(c, x, y, w, h, 100, 0, COR, a, cortes=0),
                                            centro(c, "total: 240", x + w / 2, y + h + 70, 56, "i", TINTA2, a)))
    pinta = ep(t, c12 + 0.3, 0.6)
    if pinta > 0:
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w * 0.37 * pinta, h), 14, 14)
        c.drawRRect(r, M.paint(COR))
        E.foco(c, t, c12 + 0.6, 0.4, lambda a: centro(c, "37%", x + w * 0.185, y + h / 2 + 24, 64, "g", BR, a))
    E.foco(c, t, fala("s12", "pedaço"), 0.4, lambda a: centro(c, "só um pedaço", x + w * 0.185, y - 30, 54, "i", COR, a))
    E.foco(c, t, d12, 0.5, lambda a: E.pilula(c, "resultado menor que 240", W / 2, 960, 64, "g", a=a))


# ---------------- atalho (palco escuro) ----------------
def troca(c, t, t0, cx, y, size, a=1.0):
    """'8% de 50' vira '50% de 8': o 8 e o 50 trocam de lugar por cima e por baixo"""
    p = ease_io(prog(t, t0, 0.9))

    def lay(n1, n2):
        ws = [E.larg(n1, "g", size), E.larg("%", "g", size) + size * 0.25, E.larg("de", "i", size) + size * 0.25, E.larg(n2, "g", size)]
        x = cx - sum(ws) / 2
        xs = []
        for w_ in ws:
            xs.append(x)
            x += w_
        return xs
    xa, xb = lay("8", "50"), lay("50", "8")
    arco = math.sin(p * math.pi) * size * 0.9
    E.escreve(c, "8", lerp(xa[0], xb[3], p), y - arco, size, "g", CLARO, a)
    E.escreve(c, "50", lerp(xa[3], xb[0], p), y + arco, size, "g", CLARO if p < 1 else BR, a)
    E.escreve(c, "%", lerp(xa[1], xb[1], p), y, size, "g", BR, a)
    E.escreve(c, "de", lerp(xa[2], xb[2], p), y, size, "i", BR, a)


def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]

    def treze():
        E.frase(c, t, C["s13"] + 0.3, ps("o atalho:", "i", 84, CLARO) + [("troque a ordem", "g", 84, BR)], W / 2, 200, "center", 0.14)
        E.foco(c, t, b13, 0.5, lambda a: troca(c, t, c13 - 0.3, 900, 520, 170, a))
        E.saida(c, t, c13 - 0.3, lambda: E.frase(c, t, fala("s13", "parece"), ps("parece chato", "i", 64, CLARO), 900, 680, "center", 0.12))
        E.frase(c, t, fala("s13", "metade"), ps("metade de 8", "i", 70, CLARO), 900, 700, "center", 0.12)
        E.foco(c, t, d13, 0.5, lambda a: (E.bola(c, 1560, 470, 130, a=a), centro(c, "4", 1560, 470 + 54, 150, "g", BR, a)))
        E.frase(c, t, fala("s13", "e"), ps("as duas contas dão", "i", 64, CLARO) + [("o mesmo", "g", 64, BR)], W / 2, 900, "center", 0.12)
    E.saida(c, t, C["s14"] - 0.1, treze)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"] + 0.3, ps("funciona porque a conta é", "i", 74, CLARO) + [("a mesma", "g", 74, BR)], W / 2, 180, "center", 0.12)
    E.linha(c, t, [("8 × 50 ÷ 100", "g", 96, BR, a14), ("=", "g", 96, CLARO, fala("s14", "mudar")), ("50 × 8 ÷ 100", "g", 96, BR, fala("s14", "mudar") + 0.3)],
            W / 2, 380, "center")
    E.frase(c, t, fala("s14", "não"), ps("a ordem", "i", 64, CLARO) + [("não muda", "g", 64, BR)] + ps("o resultado", "i", 64, CLARO), W / 2, 500, "center", 0.12)
    E.frase(c, t, fala("s14", "não", 2), [("não compensa:", "g", 66, CLARO)], XE, 720)
    E.frase(c, t, b14, [("37% de 240", "g", 100, BR)], XE, 860)
    E.frase(c, t, fala("s14", "fácil"), ps("nenhum lado fácil", "i", 60, CLARO), XE, 950, "left", 0.1)
    E.foco(c, t, c14, 0.5, lambda a: E.pilula(c, "vá de decimal", 1420, 840, 80, "g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, fala("s15", "conta"), ps("conta do restaurante:", "i", 76), XE, 340, "left", 0.12)
    E.frase(c, t, a15, [("R$ 140", "g", 110)], XE, 470)
    E.frase(c, t, fala("s15", "taxa"), ps("taxa de serviço:", "i", 76), XE, 620, "left", 0.12)
    E.frase(c, t, b15, [("15%", "g", 110, COR)], XE, 750)
    E.frase(c, t, c15, ps("quanto é a", "i", 92) + [("taxa?", "g", 92, COR)], XE, 920, "left", 0.15)
    E.saida(c, t, C["s16"] - 0.1, lambda: E.frase(c, t, fala("s15", "tente"), ps("tente", "i", 84) + [("de cabeça", "g", 84, COR)], 1450, 520, "center", 0.12))
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], 1420, 470, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    a18, b18 = C["s18.a"], C["s18.b"]

    def cabeca():
        E.frase(c, t, C["s17"] + 0.3, ps("de", "i", 80) + [("cabeça", "g", 80, COR)], XE, 170, "left", 0.12)
        s, y = 130, 360
        cl = E.casa(s)
        E.frase(c, t, a17, [("10% de 140", "g", 84)], 760, y, "right")
        cen(c, t, a17 + 0.3, "→", 850, y - 10, 84, TINTA2)
        E.foco(c, t, a17 + 0.4, 0.45, lambda q: E.anda(c, t, "140", 3, [(fala("s17", "anda"), 2)], 940, y, s, tv=fala("s17", "vírgula") - 0.2))
        E.foco(c, t, fala("s17", "catorze"), 0.45, lambda a: E.escreve(c, "= 14", 940 + 3.3 * cl, y, 110, "g", COR, a))
        E.linha(c, t, [("5% de 140", "g", 84, TINTA, b17), ("=", "g", 84, TINTA2, fala("s17", "metade")), ("14 ÷ 2", "g", 84, TINTA, fala("s17", "metade") + 0.2),
                       ("=", "g", 84, TINTA2, fala("s17", "sete") - 0.2), ("7", "g", 84, COR, fala("s17", "sete"))], XE, 560)
        E.linha(c, t, [("14 + 7", "g", 100, TINTA, c17), ("=", "g", 100, TINTA2, fala("s17", "dá"))], XE, 790)
        E.foco(c, t, fala("s17", "vinte"), 0.5, lambda a: num_bola(c, "R$ 21", 690, 760, 130, 80, a, CERTO))
    E.saida(c, t, C["s18"] - 0.1, cabeca)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"] + 0.3, ps("na", "i", 80) + [("conta", "g", 80, COR)] + ps("dá igual", "i", 80), XE, 170, "left", 0.12)
    E.frase(c, t, a18, [("140 × 0,15", "g", 110)], XE, 380)
    E.linha(c, t, [("140 × 15", "g", 90, TINTA, fala("s18", "cento", 2)), ("=", "g", 90, TINTA2, fala("s18", "dá")),
                   ("2100", "g", 90, COR, fala("s18", "dois"))], XE, 560)
    s = 130
    cl = E.casa(s)
    E.frase(c, t, fala("s18", "com"), ps("2 casas:", "i", 70, TINTA2), XE, 780, "left", 0.1)
    x0 = XE + 320
    E.foco(c, t, fala("s18", "com") + 0.1, 0.45, lambda q: E.anda(c, t, "2100", 4, [(fala("s18", "casas"), 2)], x0, 780, s, tv=fala("s18", "duas")))
    E.foco(c, t, b18, 0.5, lambda a: num_bola(c, "R$ 21", 1450, 740, 140, 84, a, CERTO))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s19.a", "de cabeça: parta do 10%"), ("s19.b", "na conta: × o decimal"), ("s19.c", "confira o tamanho"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 330 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", "#FFFFFF", a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 90)], 430, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    E.frase(c, t, fala("s20", "próxima"), [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, a20 - 0.3, [("Quantos por cento", "g", 112, COR)], XE, 450)
    E.frase(c, t, a20, [("e o total", "g", 112, COR)], XE, 580)
    E.frase(c, t, fala("s20", "trinta"), [("30", "g", 76)] + ps("é quantos % de", "i", 76) + [("120?", "g", 76)], XE, 740, "left", 0.15)
    E.frase(c, t, b20, ps("o total, sabendo só", "i", 76) + [("a parte", "g", 76, COR)], XE, 850, "left", 0.12)
    E.foco(c, t, c20, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=a))
    p = ease_io(prog(t, c20 + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, c20 + 0.2, 0.4))
    E.frase(c, t, d20, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, dez=b_dez, montar=b_montar, conta=b_conta, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
