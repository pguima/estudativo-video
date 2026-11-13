"""Visual — Estudativo · QUI-ELE-014: praticando eletrólise e radioatividade (aula de prática, 4 questões).
Linguagem visual: a da Química (QUI-MIS-001), a da Eletrólise (cabeçalho da QUI-ELE-008: cuba, gerador, polos por cor de sinal,
gás em bolhas na cor do elemento) e a da Radioatividade (cabeçalho da QUI-ELE-011: nuclídeo com nuc(), equação nuclear com
eq_nuc(), alfa laranja, beta azul). A cuba aqui é a versão curta cuba() desta aula. Cada questão: enunciado à esquerda e
relógio à direita na pausa; a resposta na tela seguinte. Todo instante vem de C[...]."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-014_praticando_eletrolise_e_radioatividade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "fim"))
BR = "#FFFFFF"
PROTON, GAMA, BETA = "#E07B39", "#8E44AD", Q.ELETRON

def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """palavras de uma frase; sinais (=, −, +, ×, →) vão na grotesca, porque a serifada itálica não tem esses glifos"""
    return [((w, "g", size * 0.9, cor) if w in ("=", "−", "+", "×", "→", "≠") else (w, "b", size * 0.9, cor) if ("-" in w and est == "i") else (w, est, size, cor)) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=66, r=40):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + r, y - size * 0.38, r, a=a), centro(c, str(i + 1), x + r, y - size * 0.38 + r * 0.42, r * 1.2, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + r * 2 + 40, y, passo=0.1)


def nuc(c, A, Z, s, x, y, size, cor=None, a=1.0, cor_a=None, cor_z=None):
    """nuclídeo: massa em cima e número atômico embaixo, à esquerda do símbolo. Devolve a largura."""
    cor = cor or TINTA
    sn = size * 0.5
    ta, tz = str(A), str(Z)
    wn = max(E.larg(ta, "g", sn), E.larg(tz, "g", sn))
    if c is not None and a > 0:
        E.escreve(c, ta, x + wn - E.larg(ta, "g", sn), y - size * 0.46, sn, "g", cor_a or TINTA, a)
        E.escreve(c, tz, x + wn - E.larg(tz, "g", sn), y + size * 0.2, sn, "g", cor_z or COR, a)
        E.escreve(c, s, x + wn + size * 0.06, y, size, "g", cor, a)
    return wn + size * 0.06 + E.larg(s, "g", size)


def eq_nuc(c, t, tl, itens, x, y, size, align="center"):
    """itens = [(A, Z, símbolo, cor) | "+" | "->"]; tl = instante de cada item. Devolve o centro x de cada item."""
    gap = size * 0.35
    ws = []
    for it in itens:
        if it == "+":
            ws.append(E.larg("+", "g", size * 0.8))
        elif it == "->":
            ws.append(size * 1.4)
        else:
            ws.append(nuc(None, it[0], it[1], it[2], 0, 0, size))
    tot = sum(ws) + gap * (len(ws) - 1)
    xx = x - tot / 2 if align == "center" else x
    cs = []
    for k, (it, w) in enumerate(zip(itens, ws)):
        tk = tl[k] if tl else -10
        q = ep(t, tk, 0.4)
        if q > 0:
            if it == "+":
                E.escreve(c, "+", xx, y - size * 0.05, size * 0.8, "g", TINTA2, q)
            elif it == "->":
                M.arrow(c, xx, y - size * 0.32, xx + w * ease_io(prog(t, tk, 0.5)), y - size * 0.32, E.COR, q, 6, 22, ease_io(prog(t, tk, 0.5)))
            else:
                E.foco(c, t, tk, 0.4, lambda aa, it=it, xx=xx: nuc(c, it[0], it[1], it[2], xx, y, size, it[3] if len(it) > 3 else None, aa))
        cs.append(xx + w / 2)
        xx += w + gap
    return cs


def nucleo(c, cx, cy, Zv, Nv, r=14, a=1.0, semente=2, treme=0.0, t=0.0):
    """cacho de prótons (laranja) e nêutrons (cinza); Zv e Nv = quantas bolinhas de cada"""
    if a <= 0:
        return
    rnd = random.Random(semente)
    n = Zv + Nv
    tipos = [PROTON] * Zv + [Q.NEUTRON] * Nv
    rnd.shuffle(tipos)
    pts = []
    for k in range(n):
        ang = k * 2.399963
        rr = r * 1.05 * math.sqrt(k + 0.5)
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    dx = treme * math.sin(t * 40) * 2
    for (x, y), cor in sorted(zip(pts, tipos), key=lambda p: -math.dist(p[0], (cx, cy))):
        E.bola(c, x + dx, y, r, cor, a)


def alfa(c, x, y, r=16, a=1.0, rotulo=True):
    for k, (ox, oy, cor) in enumerate(((-1, -1, PROTON), (1, -1, Q.NEUTRON), (-1, 1, Q.NEUTRON), (1, 1, PROTON))):
        E.bola(c, x + ox * r * 0.75, y + oy * r * 0.75, r, cor, a)
    if rotulo:
        E.escreve(c, "α", x + r * 2, y - r * 1.2, r * 2.4, "g", PROTON, a)


def beta(c, x, y, r=16, a=1.0, rotulo=True):
    E.bola(c, x, y, r, BETA, a)
    M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, a, max(2.5, r * 0.16))
    if rotulo:
        E.escreve(c, "β", x + r * 1.4, y - r * 1.2, r * 2.4, "g", BETA, a)


def gama_onda(c, x0, x1, y, amp=20, lam=60, a=1.0, cor=None, rotulo=True):
    if a <= 0 or x1 <= x0:
        return
    p = skia.Path()
    p.moveTo(x0, y)
    x = x0
    while x < x1:
        x += 4
        p.lineTo(x, y + amp * math.sin((x - x0) / lam * 2 * math.pi))
    c.drawPath(p, M.paint(cor or GAMA, a, stroke=6))
    if rotulo:
        E.escreve(c, "γ", x0, y - amp - 20, 60, "g", cor or GAMA, a)


def barreiras(c, t, t0, x, y, h, a=1.0):
    nomes = (("papel", "#EFEAD8", 18), ("alumínio", "#B9C0CC", 40), ("chumbo", "#3A3D45", 110))
    xs = []
    for k, (nome, cor, w) in enumerate(nomes):
        xx = x + k * 360
        q = ep(t, t0 + 0.3 * k, 0.4) * a
        if q > 0:
            M.rrect(c, xx, y - h / 2, w, h, 6, cor, q)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx, y - h / 2, w, h), 6, 6), M.paint(TINTA2, 0.5 * q, stroke=2))
            centro(c, nome, xx + w / 2, y + h / 2 + 60, 44, "g", TINTA, q)
        xs.append((xx, w))
    return xs



OXI, RED = "#E08A00", Q.ELETRON
FUNDIDO, LIMPA = "#F4B860", Q.AGUA
assert round(3.175 / 63.5, 3) == 0.05 and round(0.05 * 2, 2) == 0.1 and round(0.1 * 96500) == 9650 and 9650 / 5 == 1930 and 4825 / 5 == 965
assert (226 - 4, 88 - 2) == (222, 86) and (214, 82 + 1) == (214, 83)
assert 2077 - 1987 == 90 and 90 / 30 == 3 and 100 / 2 ** 3 == 12.5


def conta(c, t, t0, s, x, y, size, cor=TINTA, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def numero(c, t, t0, n, titulo):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 40, 150, 44, a=a), centro(c, str(n), XE + 40, 169, 54, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.2, [(titulo, "g", 60, COR)], XE + 120, 172)


def gerador(c, cx, cy, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - 100, cy - 45, 200, 90, 16, "#22232B", a)
    centro(c, "−", cx - 62, cy + 20, 56, "g", BR, a)
    centro(c, "+", cx + 62, cy + 20, 56, "g", E.CLARO, a)


def cuba(c, t, t0, cx, yb, w, h, cor, prod_c=None, prod_a=None, tc=None, ta=None, gas_c=None, gas_a=None):
    """cuba simples: líquido, duas placas, gerador; prod_c/prod_a = rótulo do que sai em cada polo (em tc/ta)"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    x0 = cx - w / 2
    M.rrect(c, x0, yb - h * 0.75, w, h * 0.75, 18, cor, 0.85 * q)
    pth = skia.Path(); pth.moveTo(x0, yb - h); pth.lineTo(x0, yb); pth.lineTo(x0 + w, yb); pth.lineTo(x0 + w, yb - h)
    c.drawPath(pth, M.paint(Q.VIDRO, q, stroke=5))
    xc, xa = cx - w * 0.3, cx + w * 0.3
    for x in (xc, xa):
        M.rrect(c, x - 20, yb - h - 30, 40, h * 0.82, 8, "#9AA0AA", q)
    yf = yb - h - 140
    for pts in (((xc, yb - h - 30), (xc, yf), (cx - 100, yf)), ((cx + 100, yf), (xa, yf), (xa, yb - h - 30))):
        p = skia.Path(); p.moveTo(*pts[0]); [p.lineTo(*pp) for pp in pts[1:]]
        c.drawPath(p, M.paint(TINTA, q, stroke=5))
    gerador(c, cx, yf, q)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: (E.pilula(c, "cátodo −", xc - 150, yb - h + 20, 38, "g", fundo=TINTA, a=a), E.pilula(c, "ânodo +", xa + 150, yb - h + 20, 38, "g", fundo=E.COR, a=a)))
    for (x, tk, rot, gas) in ((xc, tc, prod_c, gas_c), (xa, ta, prod_a, gas_a)):
        if tk is None:
            continue
        if gas:
            for k in range(5):
                f = ((t - tk) * 0.6 + k / 5) % 1.0
                c.drawCircle(x + 20 * math.sin(k * 2 + f * 4), lerp(yb - 40, yb - h + 20, f), 10, M.paint(gas, ep(t, tk, 0.4) * (1 - 0.6 * f)))
        else:
            M.rrect(c, x - 30, yb - h * 0.7, 60, h * 0.55 * ep(t, tk, 1.5) + 4, 8, "#C8CDD6", q)
        E.foco(c, t, tk, 0.4, lambda a, x=x, rot=rot: E.pilula(c, rot, x, yb + 60, 42, "g", fundo=TINTA2, a=a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("quatro", "g", 110, COR)] + ps("questões para fechar a trilha", "i", 80), XE, 280, passo=0.12)
    for k, (tk, s, cor) in enumerate(((C["s01.b"], "eletrólise", TINTA), (C["s01.c"], "Faraday", RED), (C["s01.d"], "decaimento", PROTON), (C["s01.e"], "meia-vida", E.COR))):
        x = XE + 60 + k * 410
        E.foco(c, t, tk, 0.4, lambda a, x=x, s=s, cor=cor, k=k: (E.bola(c, x + 150, 560, 120, cor, a), centro(c, str(k + 1), x + 150, 600, 120, "g", BR, a), centro(c, s, x + 150, 770, 56, "g", TINTA, a)))
    E.frase(c, t, C["s01.e"] + 1.0, ps("resolva comigo", "i", 70, TINTA2), W / 2, 960, "center", 0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("as ferramentas", "i", 76, TINTA2), XE, 170, passo=0.12)
    lista(c, t, [(C["s02.a"], [("cátion", "g", 54)] + ps("vai ao cátodo; na água, família 1, 2 e Al dão", "i", 56) + [("H₂", "g", 54)]),
                 (C["s02.b"], [("Q = i · t", "g", 54, RED)] + ps("e 96.500 C = 1 mol de elétrons", "i", 56)),
                 (C["s02.c"], [("alfa", "g", 54, PROTON)] + ps("tira 4 e 2;", "i", 56) + [("beta", "g", 54, BETA)] + ps("sobe 1 no número atômico", "i", 56)),
                 (C["s02.d"], ps("cada meia-vida corta", "i", 56) + [("metade do que sobrou", "g", 54)])], XE, 320, 170, 56, 38)


# ---------------- questão 1 ----------------
def b_q1(c, t, C, b):
    numero(c, t, C["s03"], 1, "eletrólise")
    E.frase(c, t, C["s03.a"], ps("cálcio metálico: eletrólise do", "i", 58) + [("cloreto de cálcio derretido", "g", 54)], XE, 300, passo=0.08)
    E.foco(c, t, C["s03.a"] + 1.4, 0.4, lambda a: Q.formula(c, "CaCl2", XE, 450, 110, TINTA, a))
    E.frase(c, t, C["s03.b"], [("a", "g", 54, COR)] + ps("o que sai no cátodo e no ânodo?", "i", 58), XE, 620, passo=0.08)
    E.frase(c, t, C["s03.c"], [("b", "g", 54, COR)] + ps("e se estivesse dissolvido em água?", "i", 58), XE, 730, passo=0.08)
    if t >= C["s04"]:
        E.relogio(c, t, C["s04.a"], cx=1560, cy=560, r=170)


def b_r1(c, t, C, b):
    if t < C["s06"]:
        E.frase(c, t, C["s05"], ps("derretido: sem água para disputar", "i", 58, TINTA2), XE, 180, passo=0.08)
        cuba(c, t, C["s05"], W / 2, 900, 900, 380, FUNDIDO, "cálcio metálico", "gás cloro", C["s05.b"], C["s05.c"], None, "#2DB24A")
        return
    E.frase(c, t, C["s06.a"], ps("em água: o cálcio é da", "i", 58, TINTA2) + [("família 2", "g", 54)], XE, 180, passo=0.08)
    cuba(c, t, C["s06"], W / 2, 900, 900, 380, LIMPA, "gás hidrogênio", "gás cloro", C["s06.b"], C["s06.d"], "#F7F7F5", "#2DB24A")
    E.foco(c, t, C["s06.e"], 0.4, lambda a: E.pilula(c, "só o cátodo mudou", W / 2, 1040, 50, "g", fundo=E.COR, a=a))


# ---------------- questão 2 ----------------
def b_q2(c, t, C, b):
    numero(c, t, C["s07"], 2, "Faraday")
    E.frase(c, t, C["s07.a"], ps("quanto tempo uma corrente de", "i", 58) + [("5 A", "g", 56, RED)] + ps("leva", "i", 58), XE, 300, passo=0.08)
    E.frase(c, t, C["s07.b"], ps("para depositar", "i", 58) + [("3,175 g de cobre?", "g", 56)], XE, 400, passo=0.08)
    E.foco(c, t, C["s07.c"], 0.4, lambda a: E.formula(c, "1 mol de Cu = 63,5 g", XE, 560, 66, "g", TINTA2, a))
    E.foco(c, t, C["s07.d"], 0.4, lambda a: Q.formula(c, "Cu^2+", XE, 700, 100, TINTA, a))
    if t >= C["s08"]:
        E.relogio(c, t, C["s08.a"], cx=1560, cy=560, r=170)


def b_r2(c, t, C, b):
    E.frase(c, t, C["s09"], ps("pelo caminho de volta", "i", 60, TINTA2), XE, 170, passo=0.1)
    conta(c, t, C["s09.a"], "3,175 = 1/20 de 63,5", XE, 320, 66, TINTA2)
    conta(c, t, C["s09.b"], "→ 0,05 mol de Cu", XE + 780, 320, 66, TINTA)
    conta(c, t, C["s09.c"], "× 2 elétrons", XE, 440, 66, TINTA2)
    conta(c, t, C["s09.d"], "→ 0,1 mol de e⁻", XE + 780, 440, 66, RED)
    if t >= C["s10"]:
        conta(c, t, C["s10.a"], "1/10 de 96.500", XE, 600, 66, TINTA2)
        conta(c, t, C["s10.b"], "→ 9.650 C", XE + 780, 600, 66, TINTA)
        conta(c, t, C["s10.c"], "t = Q ÷ i", XE, 760, 70, TINTA2)
        conta(c, t, C["s10.d"], "9.650 ÷ 5", XE + 500, 760, 70, TINTA)
        E.foco(c, t, C["s10.e"], 0.4, lambda a: E.formula(c, "= 1.930 s", XE + 960, 760, 80, "g", COR, a))
        E.foco(c, t, C["s10.f"], 0.4, lambda a: E.pilula(c, "sem a carga 2 do íon: 965 s, a metade", W / 2, 930, 46, "g", fundo=ERRADO, a=a))


# ---------------- questão 3 ----------------
def b_q3(c, t, C, b):
    numero(c, t, C["s11"], 3, "decaimento")
    E.foco(c, t, C["s11.a"], 0.5, lambda a: (nuc(c, 226, 88, "Ra", XE, 420, 130, TINTA, a), E.escreve(c, "→", XE + 400, 410, 100, "g", TINTA2, a), nuc(c, 4, 2, "α", XE + 560, 420, 130, PROTON, a), E.escreve(c, "+ ?", XE + 760, 410, 100, "g", TINTA, a)))
    E.frase(c, t, C["s11.b"], [("a", "g", 54, COR)] + ps("que massa e que número atômico sobram?", "i", 58), XE, 560, passo=0.08)
    E.foco(c, t, C["s11.c"], 0.5, lambda a: (nuc(c, 214, 82, "Pb", XE, 760, 130, TINTA, a), E.escreve(c, "→", XE + 400, 750, 100, "g", TINTA2, a), nuc(c, 0, -1, "β", XE + 560, 760, 130, BETA, a), E.escreve(c, "+ ?", XE + 740, 750, 100, "g", TINTA, a)))
    E.frase(c, t, C["s11.d"], [("b", "g", 54, COR)] + ps("que núcleo ele vira?", "i", 58), XE, 900, passo=0.08)
    if t >= C["s12"]:
        E.relogio(c, t, C["s12.a"], cx=1600, cy=560, r=160)


def b_r3(c, t, C, b):
    cs = eq_nuc(c, t, [C["s13"], C["s13"] + 0.3, C["s13"] + 0.6, C["s13"] + 0.9, C["s13.b"]], [(226, 88, "Ra"), "->", (4, 2, "α", PROTON), "+", (222, 86, "Rn")], W / 2, 360, 120)
    E.foco(c, t, C["s13.a"], 0.4, lambda a: E.pilula(c, "226 − 4 = 222", cs[4], 500, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.pilula(c, "88 − 2 = 86", cs[4], 590, 44, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s13.e"], 0.4, lambda a: E.escreve(c, "radônio, um gás radioativo", cs[4] - 260, 680, 46, "i", TINTA2, a))
    if t >= C["s14"]:
        cs2 = eq_nuc(c, t, [C["s14"], C["s14"] + 0.3, C["s14"] + 0.6, C["s14"] + 0.9, C["s14.a"]], [(214, 82, "Pb"), "->", (0, -1, "β", BETA), "+", (214, 83, "Bi")], W / 2, 860, 110)
        E.foco(c, t, C["s14.b"], 0.4, lambda a: E.pilula(c, "82 + 1 = 83", cs2[4], 990, 44, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s14.c"], 0.4, lambda a: E.escreve(c, "bismuto 214", cs2[0] - 100, 990, 46, "i", TINTA2, a))


# ---------------- questão 4 ----------------
def b_q4(c, t, C, b):
    numero(c, t, C["s15"], 4, "meia-vida")
    E.frase(c, t, C["s15.a"], [("césio 137,", "g", 56)] + ps("do acidente de Goiânia: meia-vida de cerca de", "i", 56) + [("30 anos", "g", 54, COR)], XE, 300, passo=0.06)
    E.foco(c, t, C["s15.b"], 0.4, lambda a: (E.formula(c, "100 g", XE, 480, 110, "g", TINTA, a), E.escreve(c, "em 1987", XE + 360, 470, 60, "i", TINTA2, a)))
    E.frase(c, t, C["s15.c"], ps("quanto restará em", "i", 62) + [("2077?", "g", 58, COR)], XE, 660, passo=0.1)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1560, cy=560, r=170)


def b_r4(c, t, C, b):
    E.foco(c, t, C["s17.a"], 0.4, lambda a: E.formula(c, "2077 − 1987", XE, 300, 80, "g", TINTA2, a))
    E.foco(c, t, C["s17.b"], 0.4, lambda a: E.formula(c, "= 90 anos", XE + 560, 300, 80, "g", TINTA, a))
    E.foco(c, t, C["s17.c"], 0.4, lambda a: E.formula(c, "90 ÷ 30", XE, 430, 80, "g", TINTA2, a))
    E.foco(c, t, C["s17.d"], 0.4, lambda a: E.pilula(c, "3 meias-vidas", XE + 620, 405, 56, "g", fundo=E.COR, a=a))
    if t >= C["s18"]:
        vals = ("100", "50", "25", "12,5 g")
        for k, v in enumerate(vals):
            tk = C["s18.a"] + 0.4 * k if k < 3 else C["s18.b"]
            E.foco(c, t, tk, 0.4, lambda a, v=v, k=k: E.escreve(c, v, XE + 360 * k, 640, 100, "g", COR if k == 3 else TINTA, a))
            if k:
                p = ep(t, tk - 0.2, 0.3)
                if p > 0:
                    M.arrow(c, XE + 360 * (k - 1) + E.larg(vals[k - 1], "g", 100) + 20, 610, XE + 360 * k - 20, 610, E.COR, p, 5, 18, p)
        E.foco(c, t, C["s18.c"], 0.4, lambda a: E.formula(c, "100 − 50 − 50 = 0", XE, 840, 70, "g", ERRADO, a))
        if t >= C["s18.d"]:
            E.risco(c, XE - 10, 860, XE + 640, 790, t, C["s18.d"], largura=9)
        E.foco(c, t, C["s18.e"], 0.4, lambda a: E.pilula(c, "metade do que sobrou", 1350, 820, 52, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo a trilha", "i", 84, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s19.a"], ps("eletrólise: a carga conta os elétrons; a", "i", 58) + [("carga do íon", "g", 54)] + ps("diz quantos", "i", 58)),
                     (C["s19.b"], ps("no núcleo,", "i", 60) + [("as somas fecham", "g", 56)]),
                     (C["s19.c"], ps("o tempo se conta em", "i", 60) + [("metades", "g", 56, COR)])], 180, 390, 180, 58, 44)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], ps("fim da trilha de", "i", 70), XE, 250, passo=0.1)
    E.frase(c, t, C["s20"] + 0.8, [("eletroquímica", "g", 90, COR)], XE, 380)
    E.frase(c, t, C["s20"] + 1.2, ps("e", "i", 90) + [("radioatividade", "g", 90, COR)], XE, 500, passo=0.12)
    E.foco(c, t, C["s20.a"], 0.4, lambda a: E.pilula(c, "revise na playlist da trilha", 560, 660, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.b"] + 0.2, 0.4))
    E.frase(c, t, C["s20.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4, fim=b_fim)
