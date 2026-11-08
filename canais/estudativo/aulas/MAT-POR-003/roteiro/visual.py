"""Visual — Estudativo · MAT-POR-003: descobrir quantos por cento e achar o total.
Linguagem da trilha Porcentagem (cartao, maquina, fluxo, volta: as mesmas peças de MAT-POR-006). Peças desta aula: barra() é o
total como 10 (ou 20) pedaços iguais, para passar pelo 10% (ou 5%) e chegar ao 100%; tabela3() e proporcao() são a regra de três.
A voz é real: os marcadores vêm de C[...] e, onde a tela precisa da palavra exata, fala(cena, palavra) lê o tempos.json."""
import json
import math
from pathlib import Path
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, passo
import motor as M
import skia

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-003_quantos_por_cento_e_total.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("quantos", "total", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 30 / 120 == 0.25 and 120 * 25 == 3000 and 30 * 100 == 3000 and 0.4 * 100 == 40
assert 60 / 3 == 20 and 20 * 10 == 200 and 30 * 200 == 6000 and 60 * 100 == 6000 and 200 * 0.1 * 3 == 60 and 60 * 0.3 == 18
assert 17 * 2 == 34 and 50 * 2 == 100 and 25 * 4 == 100 and 200 / 2 == 100
assert 14 / 2 == 7 and 40 / 2 == 20 and 7 * 5 == 35 and 20 * 5 == 100 and 14 / 40 == 0.35
assert 45 / 3 == 15 and 15 * 20 == 300 and 300 * 0.15 == 45


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




# ---------------- peças desta aula ----------------
def barra(c, x, y, w, h, n, a=1.0, pinta=None, rot=None, size=56, cor_txt=None):
    """o total como uma barra de n pedaços iguais. pinta = {i: (cor, alfa)}; rot = {i: (texto, alfa)}"""
    if a <= 0:
        return
    rr = E._casco(c, x, y, w, h, 14, a)
    s = w / n
    c.save(); c.clipRRect(rr, True)
    for i, (cor, al) in (pinta or {}).items():
        c.drawRect(skia.Rect.MakeXYWH(x + i * s, y, s, h), M.paint(cor, a * al))
    for i in range(1, n):
        cheio = (pinta or {}).get(i - 1, (None, 0))[1] > 0.5 and (pinta or {}).get(i, (None, 0))[1] > 0.5
        M.line(c, x + i * s, y, x + i * s, y + h, BR if cheio else FIO, a, 4)
    c.restore()
    c.drawRRect(rr, M.paint(TINTA, a, stroke=4))
    for i, (txt_, al) in (rot or {}).items():
        dentro = (pinta or {}).get(i, (None, 0))[1] > 0.5
        centro(c, txt_, x + (i + 0.5) * s, y + h / 2 + size * 0.36, size, "g", BR if dentro else (cor_txt or TINTA), a * al)


def tabela3(c, t, x, y, cab, linhas, tc, wcol=260, hlin=130, size=84):
    """tabela da regra de três: cab = (col1, col2) com instantes tc; linhas = [[(valor, t0), (valor, t0)], ...]"""
    a = ep(t, tc[0], 0.5)
    if a <= 0:
        return
    xl = x + wcol
    M.line(c, xl, y - hlin * 0.75, xl, y + hlin * (len(linhas) - 0.1), TINTA, a, 5)
    M.line(c, x - 20, y + hlin * 0.25, x + 2 * wcol + 20, y + hlin * 0.25, TINTA, a, 5)
    for j, (s, ti) in enumerate(zip(cab, tc)):
        cen(c, t, ti, s, x + wcol * (j + 0.5), y, size * 0.8, COR)
    for i, lin in enumerate(linhas):
        for j, (s, ti) in enumerate(lin):
            cen(c, t, ti, s, x + wcol * (j + 0.5), y + hlin * (i + 1) + 10, size, COR if s == "x" else TINTA)


def proporcao(c, t, t0, n1, d1, n2, d2, cx, cy, s, tcruz=None, tnum=None):
    """n1/d1 = n2/d2 com o produto cruzado em X (tcruz)"""
    xa, xb = cx - s * 2.1, cx + s * 2.1
    E.foco(c, t, t0, 0.5, lambda a: E.fracao(c, n1, d1, xa, cy, s, TINTA, a))
    sinal(c, t, t0 + 0.3, "=", cx, cy - s * 0.12, s * 0.8)
    E.foco(c, t, tnum if tnum else t0 + 0.5, 0.5, lambda a: E.fracao(c, n2, d2, xb, cy, s, TINTA, a))
    if tcruz is not None:
        for x0, y0, x1, y1, d in ((xa + s * 1.0, cy - s * 0.45, xb - s * 1.0, cy + s * 0.65, 0), (xa + s * 1.0, cy + s * 0.65, xb - s * 1.0, cy - s * 0.45, 0.4)):
            p = ep(t, tcruz + d, 0.5)
            if p > 0:
                M.line(c, x0, y0, x1, y1, COR, 0.8, 6, progress=p)


def sinal(c, t, t0, s, cx, cy, size, cor=None):
    E.sinal(c, t, t0, s, cx, cy, size, cor or TINTA2)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def um():
        cartao(c, t, kb, 420, 400, "R$ 120", "compra", False, 96)
        cartao(c, t, ka, 980, 400, "R$ 30", "desconto", True, 96)
        E.frase(c, t, fala("s01", "quantos"), [("quantos %?", "g", 110, COR)], 1580, 435, "center")
        E.frase(c, t, fala("s01", "muita"), ps("muita gente chuta", "i", 76), 560, 760, "center", 0.12)
        E.foco(c, t, kc, 0.5, lambda a: centro(c, "30%", 560, 920, 150, "g", ERRADO, a))
        if t >= fala("s01", "mas"):
            E.risco(c, 420, 940, 700, 820, t, fala("s01", "mas"), largura=14)
        E.frase(c, t, fala("s01", "mas"), ps("foi", "i", 84), 1180, 900, "center")
        E.foco(c, t, kd, 0.5, lambda a: num_bola(c, "25%", 1460, 860, 140, 100, a, CERTO))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, fala("s02", "quantos"), [("quantos por cento", "g", 100, COR)], XE, 500)
        E.frase(c, t, fala("s02", "parte") - 0.2, ps("a parte é do total", "i", 80), XE, 620, passo=0.1)
        E.frase(c, t, fala("s02", "achar"), ps("e achar", "i", 90) + [("o total", "g", 100, COR)], XE, 790, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "Porcentagem de", "um valor"), ("s03.c", "Montar uma", "regra de três"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 270
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 66)], x + 44, y + 92)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 66, COR)], x + 44, y + 178)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(420, 690, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, fala("s03", "se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 900, "left", 0.12)


# ---------------- quantos por cento ----------------
def b_quantos(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    y = 520

    def quatro_cinco():
        E.frase(c, t, C["s04"] + 0.2, [("30", "g", 90, COR)] + ps("é quantos % de", "i", 90) + [("120?", "g", 90)], W / 2, 200, "center", 0.15)
        E.frac_q(c, t, a4, 30, 120, fala("s04", "parte"), fala("s04", "total"), 330, y, 140)
        E.saida(c, t, a5, lambda: (cen(c, t, fala("s04", "parte"), "parte", 560, y - 40, 60, TINTA2, "i"),
                                    cen(c, t, fala("s04", "total"), "total", 560, y + 120, 60, TINTA2, "i")))
        cen(c, t, a5, "30 ÷ 120", 330, y + 300, 60, TINTA2)
        cen(c, t, fala("s05", "zero") - 0.2, "=", 520, y + 50, 100, TINTA2)
        cen(c, t, fala("s05", "zero"), "0,25", 720, y + 60, 130, TINTA)
        cen(c, t, b5 - 0.2, "=", 930, y + 50, 100, TINTA2)
        E.foco(c, t, b5, 0.5, lambda a: E.fracao(c, 25, 100, 1110, y, 130, TINTA, a))
        cen(c, t, c5 - 0.2, "=", 1300, y + 50, 100, TINTA2)
        E.foco(c, t, c5, 0.5, lambda a: num_bola(c, "25%", 1520, y + 10, 140, 100, a))
    E.saida(c, t, C["s06"] - 0.1, quatro_cinco)

    if C["s06"] <= t < C["s07"]:
        def seis():
            E.frase(c, t, C["s06"] + 0.2, ps("a", "i", 80) + [("regra", "g", 80, COR)], XE, 170, "left", 0.12)
            passo(c, t, a6, 1, "divida", "a parte pelo total", 330)
            passo(c, t, b6, 2, "ande a vírgula", "2 casas para a direita", 560)
            E.frase(c, t, fala("s06", "multiplicar"), [("× 100", "g", 64, COR)] + ps(": por cento é em cada cem", "i", 60, TINTA2), XE + 108, 770, "left", 0.1)
            # exemplo: 0,4 vira 40%
            s, ye = 170, 500
            x0 = 1180
            E.frase(c, t, d6, ps("por exemplo", "i", 60, TINTA2), x0 + 120, 280, "center", 0.1)
            cl = E.casa(s)
            pulo = fala("s06", "vira")
            E.foco(c, t, d6, 0.45, lambda q: (zero_some(c, t, x0, ye, s, pulo), E.anda(c, t, "4", 0, [(pulo, 2)], x0, ye, s, some=True)))
            E.foco(c, t, fala("s06", "quarenta"), 0.45, lambda a: E.escreve(c, "%", x0 + 2 * cl + 10, ye, s, "g", COR, a))
            if t >= pulo:
                E.chave(c, x0 + 4, x0 + 2 * cl - 4, ye + 40, COR, ep(t, pulo, 0.4), 24, 6)
        E.saida(c, t, C["s07"] - 0.1, seis)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"] + 0.2, ps("pela", "i", 80) + [("regra de três", "g", 80, COR)], W / 2, 160, "center", 0.12)
    tabela3(c, t, 230, 380, ("R$", "%"), [[("120", fala("s07", "cento", 2)), ("100", fala("s07", "cem"))],
                                          [("30", fala("s07", "trinta")), ("x", fala("s07", "xis"))]], (a7, fala("s07", "por")))
    proporcao(c, t, b7, 120, 30, 100, "x", 1300, 400, 110, tcruz=c7, tnum=fala("s07", "cem", 2))
    E.linha(c, t, [("120 · x", "g", 84, TINTA, fala("s07", "cento", 5)), ("=", "g", 84, TINTA2, fala("s07", "igual")), ("3000", "g", 84, TINTA, fala("s07", "três", 2))],
            1300, 720, "center")
    E.foco(c, t, d7, 0.5, lambda a: E.pilula(c, "x = 25", 1300, 880, 80, "g", a=a))


# ---------------- achar o total ----------------
BX, BY, BW, BH = 360, 520, 1200, 150


def b_total(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10 = C["s10.a"], C["s10.b"]
    a11, b11 = C["s11.a"], C["s11.b"]
    s_ = BW / 10

    def barra_fase():
        E.frase(c, t, C["s08"] + 0.3, ps("o caminho de", "i", 80) + [("volta", "g", 80, COR)], W / 2, 150, "center", 0.12)
        E.linha(c, t, [("R$ 60", "g", 92, COR, a8), ("são", "i", 92, TINTA, fala("s08", "são")), ("30%", "g", 92, TINTA, fala("s08", "trinta")),
                       ("de", "i", 92, TINTA, fala("s08", "de", 2)), ("?", "g", 92, CINZA, fala("s08", "valor"))], W / 2, 300, "center")
        pinta, rot = {}, {}
        for i in range(3):
            pinta[i] = (E.COR, ep(t, b8 + 0.1 * i, 0.4))
        if t >= a9:
            q = ep(t, a9, 0.4) * (1 - ep(t, b9, 0.3))
            if q > 0:
                rot[0] = ("10%", q)
        for i in range(10):
            ti = fala("s09", "vinte") + 0.15 * i if i < 3 else c9 + 0.08 * (i - 3)
            if t >= ti:
                rot[i] = ("20", ep(t, ti, 0.4))
        E.foco(c, t, a8 + 0.4, 0.5, lambda a: barra(c, BX, BY, BW, BH, 10, a, pinta, rot, 60))
        E.chave(c, BX + 6, BX + 3 * s_ - 6, BY - 20, COR, ep(t, b8, 0.4), -26, 6)
        cen(c, t, b8 + 0.1, "R$ 60 = a parte", BX + 1.5 * s_, BY - 70, 56, COR)
        E.chave(c, BX + 6, BX + BW - 6, BY + BH + 20, TINTA, ep(t, c8, 0.5), 26, 6)
        if t < c9 + 0.8:
            E.saida(c, t, c9 + 0.6, lambda: cen(c, t, c8 + 0.1, "100% = o total", BX + BW / 2, BY + BH + 110, 60, TINTA))
        E.frase(c, t, fala("s09", "trinta"), [("30% = 3 × 10%", "g", 64)], XE, 880, "left")
        E.frase(c, t, b9, [("10% = 60 ÷ 3 = 20", "g", 64, COR)], XE, 980, "left")
        E.foco(c, t, c9 + 0.8, 0.5, lambda a: E.escreve(c, "20 × 10 =", 1080, 960, 72, "g", TINTA, a))
        E.foco(c, t, fala("s09", "duzentos"), 0.5, lambda a: num_bola(c, "R$ 200", 1640, 935, 130, 64, a))
    E.saida(c, t, C["s10"] - 0.1, barra_fase)

    if C["s10"] <= t < C["s11"]:
        def dez():
            E.frase(c, t, C["s10"] + 0.3, ps("como achar", "i", 70) + [("1 kg", "g", 70)] + ps("antes de", "i", 70) + [("7 kg", "g", 70)],
                    W / 2, 170, "center", 0.12)
            E.frase(c, t, fala("s10", "pela"), ps("pela", "i", 70) + [("regra de três", "g", 70, COR)], W / 2, 270, "center", 0.12)
            tabela3(c, t, 230, 470, ("%", "R$"), [[("30", a10), ("60", fala("s10", "sessenta"))],
                                                  [("100", fala("s10", "cem")), ("x", fala("s10", "xis"))]], (a10 - 0.3, a10 - 0.1))
            proporcao(c, t, fala("s10", "trinta", 2), 30, 100, 60, "x", 1300, 480, 110, tcruz=b10, tnum=fala("s10", "sessenta", 2))
            E.linha(c, t, [("30 · x", "g", 84, TINTA, b10), ("=", "g", 84, TINTA2, fala("s10", "igual")), ("6000", "g", 84, TINTA, fala("s10", "seis"))],
                    1300, 800, "center")
            E.foco(c, t, fala("s10", "xis", 4), 0.5, lambda a: E.pilula(c, "x = 200", 1300, 950, 80, "g", a=a))
        E.saida(c, t, C["s11"] - 0.1, dez)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11"] + 0.3, ps("confira", "i", 84, COR), W / 2, 260, "center")
    E.linha(c, t, [("10% de 200", "g", 100, TINTA, a11), ("=", "g", 100, TINTA2, fala("s11", "é")), ("20", "g", 100, COR, fala("s11", "vinte"))], W / 2, 480, "center")
    E.linha(c, t, [("20 × 3", "g", 100, TINTA, b11), ("=", "g", 100, TINTA2, fala("s11", "sessenta") - 0.2), ("60", "g", 100, CERTO, fala("s11", "sessenta"))],
            W / 2, 680, "center")
    E.foco(c, t, fala("s11", "bateu"), 0.45, lambda a: E.selo(c, 1420, 640, 60, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    E.frase(c, t, C["s12"] + 0.3, [("o erro:", "g", 92, ERRADO)] + ps("calcular a % da", "i", 92) + [("parte", "g", 92)], W / 2, 180, "center", 0.12)
    E.linha(c, t, [("30% de 60", "g", 110, TINTA, b12), ("=", "g", 110, TINTA2, fala("s12", "responde")), ("18", "g", 110, ERRADO, c12)], W / 2, 400, "center")
    if t >= d12 + 0.3:
        E.risco(c, 1180, 420, 1360, 300, t, d12 + 0.3, largura=14)
    s_ = BW / 10
    E.foco(c, t, fala("s12", "mas"), 0.5, lambda a: barra(c, BX, 600, BW, 120, 10, a, {0: (E.COR, 1), 1: (E.COR, 1), 2: (E.COR, 1)}, {}, 56))
    E.foco(c, t, fala("s12", "pedaço"), 0.4, lambda a: centro(c, "60 é um pedaço", BX + 1.5 * s_, 570, 54, "i", COR, a))
    E.foco(c, t, d12, 0.5, lambda a: E.pilula(c, "o total não pode ser menor", W / 2, 880, 66, "g", fundo=ERRADO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]

    def treze():
        E.frase(c, t, C["s13"] + 0.3, ps("o atalho:", "i", 84, CLARO) + [("total vira 100", "g", 84, BR)], W / 2, 200, "center", 0.14)
        y, s = 560, 150
        E.foco(c, t, b13, 0.5, lambda a: E.fracao(c, 17, 50, 480, y, s, BR, a))
        E.pontes(c, t, 640, 860, y, s, "× 2", fala("s13", "dobre"), fala("s13", "embaixo"), CLARO, 56)
        E.foco(c, t, c13, 0.5, lambda a: E.fracao(c, 34, 100, 1030, y, s, BR, a))
        sinal(c, t, d13 - 0.2, "=", 1240, y - 15, 120, CLARO)
        E.foco(c, t, d13, 0.5, lambda a: (E.bola(c, 1500, y + 5, 150, a=a), centro(c, "34%", 1500, y + 50, 120, "g", BR, a)))
        E.frase(c, t, fala("s13", "sem"), ps("sem dividir nada", "i", 70, CLARO), W / 2, 920, "center", 0.12)
    E.saida(c, t, C["s14"] - 0.1, treze)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"] + 0.3, ps("fração equivalente", "i", 72, CLARO) + [("não muda o valor", "g", 72, BR)], W / 2, 170, "center", 0.12)
    for i, (ti, d, op, ok) in enumerate(((b14, 25, "× 4", True), (c14, 200, "÷ 2", True), (d14, 120, "?", False))):
        y = 400 + i * 220
        E.foco(c, t, ti - 0.6, 0.5, lambda a, d=d, y=y: (centro(c, "total", 360, y + 15, 56, "i", CLARO, a), centro(c, str(d), 600, y + 30, 110, "g", BR, a)))
        if ok:
            E.ponte(c, t, ti, 760, 1060, y, op, CLARO, 56)
            E.foco(c, t, ti + 0.4, 0.5, lambda a, y=y: centro(c, "100", 1200, y + 30, 110, "g", CLARO, a))
        else:
            if t >= ti + 0.3:
                E.risco(c, 500, y + 40, 700, y - 60, t, ti + 0.3, largura=12)
            E.foco(c, t, fala("s14", "divida", 2), 0.5, lambda a, y=y: E.pilula(c, "parte ÷ total", 1150, y, 70, "g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a15, b15, c15, d15, e15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]
    E.frase(c, t, C["s15"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 170)
    E.linha(c, t, [("turma:", "i", 76, TINTA, fala("s15", "uma")), ("40 alunos", "g", 80, TINTA, a15)], XE, 330)
    E.linha(c, t, [("passaram:", "i", 76, TINTA, b15), ("14", "g", 80, COR, b15 + 0.2)], XE, 440)
    E.frase(c, t, c15, [("quantos %?", "g", 84, COR)], XE, 560)
    E.linha(c, t, [("escola:", "i", 76, TINTA, fala("s15", "na")), ("45 alunos", "g", 80, COR, d15), ("=", "g", 80, TINTA2, fala("s15", "são")),
                   ("15%", "g", 80, TINTA, fala("s15", "quinze"))], XE, 760)
    E.frase(c, t, e15, [("quantos alunos?", "g", 84, COR)], XE, 880)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], 1520, 470, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a17, b17, c17, d17, e17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"], C["s17.e"]
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]

    def turma():
        E.frase(c, t, C["s17"] + 0.3, ps("na", "i", 76) + [("turma", "g", 76, COR)], XE, 170, "left", 0.12)
        y, s = 470, 120
        E.foco(c, t, a17, 0.5, lambda a: E.fracao(c, 14, 40, 280, y, s, TINTA, a))
        E.pontes(c, t, 400, 560, y, s, "÷ 2", b17, b17 + 0.4, None, 46)
        E.foco(c, t, fala("s17", "sete"), 0.5, lambda a: E.fracao(c, 7, 20, 680, y, s, TINTA, a))
        E.frase(c, t, fala("s17", "vinte", 2), [("20 × 5 = 100", "g", 56, TINTA2)], 680, y + 240, "center")
        E.pontes(c, t, 800, 960, y, s, "× 5", c17, c17 + 0.4, None, 46)
        E.foco(c, t, d17, 0.5, lambda a: E.fracao(c, 35, 100, 1100, y, s, TINTA, a))
        sinal(c, t, e17 - 0.2, "=", 1290, y - 15, 100)
        E.foco(c, t, e17, 0.5, lambda a: num_bola(c, "35%", 1480, y + 5, 130, 96, a, CERTO))
    E.saida(c, t, C["s18"] - 0.1, turma)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"] + 0.3, ps("na", "i", 76) + [("escola", "g", 76, COR)], XE, 170, "left", 0.12)
    n, x, y, w, h = 20, 300, 450, 1320, 120
    s_ = w / n
    pinta, rot = {}, {}
    for i in range(3):
        pinta[i] = (E.COR, ep(t, a18 + 0.1 * i, 0.4))
    for i in range(n):
        ti = fala("s18", "quinze", 2) + 0.15 * i if i < 3 else fala("s18", "quinze", 3) + 0.06 * (i - 3)
        if t >= ti:
            rot[i] = ("15", ep(t, ti, 0.4))
    E.foco(c, t, C["s18"] + 0.4, 0.5, lambda a: barra(c, x, y, w, h, n, a, pinta, rot, 42))
    E.chave(c, x + 6, x + 3 * s_ - 6, y - 20, COR, ep(t, a18, 0.4), -26, 6)
    cen(c, t, a18 + 0.1, "45 = 15%", x + 1.5 * s_ + 60, y - 70, 54, COR)
    E.frase(c, t, fala("s18", "quinze"), [("15% = 3 × 5%", "g", 62)], XE, 760, "left")
    E.frase(c, t, b18, [("5% = 45 ÷ 3 = 15", "g", 62, COR)], XE, 860, "left")
    E.frase(c, t, fala("s18", "cem"), [("100% = 20 × 5%", "g", 62)], XE, 960, "left")
    E.chave(c, x + 6, x + w - 6, y + h + 20, TINTA, ep(t, fala("s18", "cem"), 0.5), 26, 6)
    E.frase(c, t, c18, [("15 × 20 =", "g", 72)], 1150, 860, "left")
    E.foco(c, t, fala("s18", "trezentos"), 0.5, lambda a: num_bola(c, "300", 1600, 840, 120, 92, a, CERTO))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s19.a", "quantos %: parte ÷ total"), ("s19.b", "o total: passe por 10% ou 5%"))):
            y = 430 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", "#FFFFFF", a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 400, y)
        E.frase(c, t, fala("s19", "chegue"), ps("e chegue ao", "i", 64, TINTA2) + [("100%", "g", 64, COR)], 400, 760, "left", 0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    E.frase(c, t, C["s20"] + 0.3, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, fala("s20", "aumentar"), [("Aumento e desconto", "g", 112, COR)], XE, 450)
    E.frase(c, t, a20, [("numa conta só", "g", 112, COR)], XE, 580)
    E.frase(c, t, b20, [("+ 15%", "g", 84)], XE, 790)
    p = ep(t, fala("s20", "multiplicando"), 0.4)
    if p > 0:
        M.arrow(c, XE + 290, 760, XE + 450, 760, TINTA2, p, 6, 20, p)
    maquina(c, t, fala("s20", "um", 2), XE + 650, 760, "× 1,15", 72)
    E.foco(c, t, c20, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=a))
    q = ease_io(prog(t, c20 + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, q), lerp(620, 325, q), ep(t, c20 + 0.2, 0.4))
    E.frase(c, t, d20, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, quantos=b_quantos, total=b_total, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
