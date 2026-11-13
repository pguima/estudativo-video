"""Visual — Estudativo · QUI-CAL-003: composição percentual e fórmula mínima.

Segue a linguagem visual da trilha (cabeçalho da QUI-CAL-001) e a da Química (cabeçalho da QUI-MIS-001).
Composição = pizza da massa (E.pizza) com o elemento da vez destacado. Os 100 gramas viram uma BARRA DE MASSA (barra_massa):
uma faixa cortada na proporção das porcentagens, cada parte na cor CPK do elemento; embaixo, a divisão pela massa molar e a
divisão pelo menor, em colunas alinhadas a cada parte.
Peça candidata ao kit quimica.py: barra_massa() (amostra cortada pela composição, na cor de cada elemento)."""
import math
from math import gcd

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-003_composicao_formula_minima.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("percentual", "minima", "cem", "atalho", "questao", "fim"))
BR = "#FFFFFF"
MA = {"H": 1, "C": 12, "N": 14, "O": 16}


def massa(f):
    return sum(MA[el] * n for el, n in Q.contar(f).items())


# todas as contas da aula
assert Q.contar("NH4NO3") == {"N": 2, "H": 4, "O": 3} and massa("NH4NO3") == 80 == 28 + 4 + 48
assert 28 / 80 == 0.35 and 14 / 80 == 0.175
assert abs(40 / 12 - 3.33) < 0.01 and abs(53.3 / 16 - 3.33) < 0.01 and abs(6.7 / 3.33 - 2) < 0.02 and 40 + 6.7 + 53.3 == 100
assert massa("CH2O") == 30 and 180 / 30 == 6 and gcd(gcd(6, 12), 6) == 6
assert gcd(4, 10) == 2 and massa("CH4") == 16 and 12 / 16 == 0.75
PALE = {"H": "#D9DCE1"}


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    tinta = E.SOBRE if cor is None else BR
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", tinta, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    """lista numerada: itens = [(instante, partes da frase)]"""
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def conta(c, t, t0, el, txt, res, x, y, size=72, tr=None, cor_res=None, escuro=False):
    """linha de massa: bolinha do elemento + "6 × 12 =" + parcial na cor da matéria (tr = instante do parcial)"""
    r = size * 0.42
    if el:
        Q.atomo_em(c, t, t0, x + r, y - size * 0.34, r, el, escuro=escuro)
        x += 2 * r + size * 0.4
    E.formula_em(c, t, t0 + 0.1, txt, x, y, size, "g", BR if escuro else TINTA)
    w = E.formula(None, txt, 0, 0, size, a=0)
    if res:
        E.formula_em(c, t, tr if tr is not None else t0 + 0.6, res, x + w + size * 0.3, y, size, "g", cor_res or (E.CLARO if escuro else COR))
    return x + w


def casa(c, cx, cy, s, el, z, m, a=1.0, cor_m=None):
    """casa do elemento na tabela periódica: Z no canto, símbolo, nome e a massa atômica embaixo"""
    if a <= 0:
        return
    w, h = s, s * 1.15
    x, y = cx - w / 2, cy - h / 2
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), s * 0.08, s * 0.08)
    c.drawRRect(rr, M.paint("#FFFFFF", a))
    c.drawRRect(rr, M.paint(E.COR, a, stroke=max(3, s * 0.025)))
    E.escreve(c, str(z), x + s * 0.09, y + s * 0.19, s * 0.14, "b", TINTA2, a)
    centro(c, el, cx, cy + s * 0.1, s * 0.42, "g", TINTA, a)
    centro(c, Q.NOMES[el], cx, cy + s * 0.28, s * 0.12, "i", TINTA2, a)
    centro(c, m, cx, cy + s * 0.5, s * 0.17, "g", cor_m or COR, a)


def casa_em(c, t, t0, cx, cy, s, el, z, m, cor_m=None):
    E.foco(c, t, t0, 0.5, lambda a: casa(c, cx, cy, s, el, z, m, a, cor_m))


def soma_vertical(c, t, tl, nums, tot, xd, y0, size, tt, cor_tot=None):
    """conta armada de somar, alinhada à direita em xd; tt = instante do traço e do total"""
    dy = size * 1.15
    for i, (n, ti) in enumerate(zip(nums, tl)):
        E.foco(c, t, ti, 0.4, lambda a, n=n, i=i: E.formula(c, n, xd, y0 + i * dy, size, "g", TINTA, a, "right"))
    E.foco(c, t, tl[1] if len(tl) > 1 else tl[0], 0.4, lambda a: E.formula(c, "+", xd - size * 2.6, y0 + dy * (len(nums) - 1), size, "g", TINTA2, a))
    p = ep(t, tt, 0.4)
    yl = y0 + (len(nums) - 1) * dy + size * 0.35
    if p > 0:
        M.line(c, xd - size * 2.8, yl, xd + size * 0.2, yl, TINTA, p, 5, progress=ease_out(prog(t, tt, 0.4)))
    return yl


def ponte_mol(c, t, t0, y, esq, meio, dir_, rot_e="", rot_d="", te=None, td=None, xs=(420, 960, 1500), size=58, escuro=False):
    """a ponte do mol: gramas ← → mol ← → moléculas. esq/meio/dir_ = texto de cada margem (ou (texto, instante));
    rot_e / rot_d = operação na pílula de cada vão; te / td = instante de cada vão"""
    tinta = BR if escuro else TINTA
    x0, xm, x1 = xs

    def txt(v):
        return v if isinstance(v, tuple) else (v, t0)
    for k, (v, x) in enumerate(((esq, x0), (dir_, x1))):
        s, ti = txt(v)
        if s:
            E.foco(c, t, ti, 0.45, lambda a, s=s, x=x: E.formula(c, s, x, y + size * 0.36, size, "g", tinta, a, "center"))
    s, ti = txt(meio)
    k = ease_back(prog(t, ti, 0.5))
    if k > 0:
        r = max(size * 1.25, E.formula(None, s, 0, 0, size * 0.8, a=0) * 0.62)
        E.bola(c, xm, y, r * k)
        E.foco(c, t, ti + 0.1, 0.4, lambda a: E.formula(c, s, xm, y + size * 0.29, size * 0.8, "g", E.SOBRE, a, "center"))
    rb = max(size * 1.25, E.formula(None, s, 0, 0, size * 0.8, a=0) * 0.62)
    we = E.formula(None, txt(esq)[0], 0, 0, size, a=0) / 2 if txt(esq)[0] else 60
    wd = E.formula(None, txt(dir_)[0], 0, 0, size, a=0) / 2 if txt(dir_)[0] else 60
    for (xa, xb, rot, tv) in ((x0 + we + 36, xm - rb - 30, rot_e, te), (xm + rb + 30, x1 - wd - 36, rot_d, td)):
        if tv is None:
            continue
        p = ease_io(prog(t, tv, 0.6))
        if p > 0:
            M.arrow(c, xa, y, lerp(xa, xb, p), y, E.CLARO if escuro else E.COR, 1.0, 7, 24, 1.0)
        if rot:
            pilula_em(c, t, tv + 0.3, rot, (xa + xb) / 2, y - 80, 42, TINTA if not escuro else "#24303A")


def pacotes(c, t, t0, n, x, y, w, h, rot, cor=None, passo=0.35, escuro=False):
    """barra cortada em n pacotes iguais que entram um a um, com o rótulo de cada um (quantas vezes cabe)"""
    wk = w / n
    for k in range(n):
        q = ease_back(prog(t, t0 + k * passo, 0.45))
        if q <= 0:
            continue
        xx = x + k * wk
        M.rrect(c, xx + 4, y + h * (1 - q) / 2, wk - 8, h * q, 14, cor or E.COR, 1.0)
        centro(c, rot, xx + wk / 2, y + h / 2 + h * 0.18, h * 0.5, "g", E.SOBRE, min(1, q))


def chip(c, s, cx, cy, size, fundo=None, a=1.0, escuro=True):
    """fórmula química dentro de uma pílula do tamanho dela"""
    if a <= 0:
        return
    w = Q.formula(None, s, 0, 0, size) + size * 0.9
    M.rrect(c, cx - w / 2, cy - size * 0.8, w, size * 1.6, size * 0.8, fundo or E.COR, a)
    Q.formula(c, s, cx, cy + size * 0.36, size, BR, a, "center", escuro=escuro)


def pz(c, t, t0, itens, cx, cy, r, destaque=()):
    """pizza com a cor de cada elemento: itens = [(rótulo, valor, cor)]"""
    E.pizza(c, t, t0, [(a, v) for a, v, _ in itens], cx, cy, r, cores=[k for _, _, k in itens], destaque=destaque, size=48)


def cor_parte(el):
    return PALE.get(el, Q.cor_el(el))


def barra_massa(c, t, t0, partes, x, y, w, h, d=1.0):
    """amostra cortada pela composição: partes = [(elemento, porcentagem, rótulo)]; devolve o centro x de cada parte"""
    p = ease_out(prog(t, t0, d))
    xs, xx = [], x
    for el, pc, rot in partes:
        wk = w * pc / 100
        xs.append(xx + wk / 2)
        vis = min(wk, max(0.0, w * p - (xx - x)))
        if vis > 0:
            M.rrect(c, xx + 3, y, vis - 6, h, 16, cor_parte(el), 1.0)
            if vis >= wk - 1 and rot:
                tinta = TINTA if el == "H" else BR
                centro(c, rot, xx + wk / 2, y + h / 2 + 22, 60 if wk > 200 else 44, "g", tinta, 1.0)
        xx += wk
    return xs


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("no saco de adubo:", "i", 70, TINTA2), XE, 220, passo=0.1)
        E.frase(c, t, C["s01.a"] + 1.0, ps("nitrato de amônio", "i", 80), XE, 330, passo=0.12)
        Q.formula_em(c, t, C["s01.b"], "NH4NO3", XE, 560, 200, cores={"N": E.COR} if t >= C["s01.c"] else None)
        E.frase(c, t, C["s01.c"], ps("quanto é", "i", 70) + [("nitrogênio?", "g", 66, COR)], XE, 760, passo=0.12)
        pz(c, t, C["s01.d"] - 0.3, [("N", 35, Q.cor_el("N")), ("H", 5, PALE["H"]), ("O", 60, Q.cor_el("O"))], 1450, 520, 230, destaque=(0,))
        bola_txt(c, t, C["s01.d"] + 0.6, "35%", 1450, 900, 90, 70)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("%", "g", 70, COR), ("de", "i", 74), ("cada", "i", 74), ("elemento", "g", 70)]),
                 (C["s02.c"], [("fórmula", "g", 70), ("mínima", "g", 70, COR)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 80) + [("duas coisas", "g", 76, COR)], XE, 200, passo=0.12)
    y = [440, 760]
    for i, k in enumerate(("s03.b", "s03.c")):
        E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, XE + 40, y[i] - 30, 44, a=a), centro(c, str(i + 1), XE + 40, y[i] - 8, 54, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, ps("massa molar", "i", 72), XE + 110, y[0])
    Q.formula_em(c, t, C["s03.b"] + 0.5, "H2O", XE + 560, y[0] + 6, 110)
    E.formula_em(c, t, C["s03.b"] + 0.9, "= 18 g/mol", XE + 790, y[0] + 6, 84, "g", COR)
    E.frase(c, t, C["s03.c"] + 0.1, ps("quantos por cento", "i", 72), XE + 110, y[1])
    E.formula_em(c, t, C["s03.c"] + 1.4, "30 de 120 = f{30}{120} = 25%", XE + 700, y[1] + 10, 72, "g", TINTA)


# ---------------- composição percentual ----------------
def b_percentual(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("composição", "g", 90, COR), ("percentual", "g", 90, COR)], XE, 280, passo=0.15)
        E.frase(c, t, C["s04.a"] + 1.4, ps("quanto da massa vem de cada elemento", "i", 64, TINTA2), XE, 390, passo=0.1)
        E.formula_em(c, t, C["s04.b"], "% = f{massa do elemento}{massa toda}", XE, 700, 84, "g", TINTA)
        E.formula_em(c, t, C["s04.c"], "× 100", XE + 1160, 700, 84, "g", COR)
        return
    cores = {"N": E.COR} if C["s05.b"] <= t < C["s06"] else None
    Q.formula_em(c, t, C["s05"], "NH4NO3", XE, 280, 160, cores=cores)
    G = [g for g in Q.grupos("NH4NO3", XE, 280, 160) if g["s"] == "N"]
    if t < C["s06"]:
        for k, g in zip(("s05.b", "s05.c"), G):
            if t >= C[k]:
                q = ep(t, C[k], 0.4)
                E.caixa_pontilhada(c, g["x0"] - 10, g["topo"] - 10, g["x1"] - g["x0"] + 20, g["base"] - g["topo"] + 20, q, E.COR, prog_=q)
        E.frase(c, t, C["s05.a"], ps("conte com cuidado", "i", 60, TINTA2), XE + 760, 260, passo=0.1)
        Q.inventario(c, t, C["s05.d"], [("N", 2), ("H", 4), ("O", 3)], XE + 10, 480, 64, tl=[C["s05.d"], C["s05.d"] + 0.5, C["s05.d"] + 1.0])
    for k, (el, z, m) in enumerate((("N", 7, "14"), ("H", 1, "1"), ("O", 8, "16"))):
        if t < C["s07"]:
            casa_em(c, t, C["s05.e"] + 0.3 * k, 1120 + k * 240, 560, 200, el, z, m)
    if C["s06"] <= t < C["s07"]:
        ys = [450, 570, 690]
        for (k, el, txt, res), y in zip((("s06.a", "N", "2 × 14 =", "28"), ("s06.b", "H", "4 × 1 =", "4"), ("s06.c", "O", "3 × 16 =", "48")), ys):
            conta(c, t, C[k], el, txt, res, XE, y, 70, tr=C[k] + 1.0)
        p = ep(t, C["s06.d"], 0.4)
        if p > 0:
            M.line(c, XE, 740, XE + 560, 740, TINTA, p, 5, progress=ease_out(prog(t, C["s06.d"], 0.4)))
        bola_txt(c, t, C["s06.d"] + 0.3, "80 g/mol", XE + 300, 860, 110, 52)
    if t < C["s07"]:
        return
    pz(c, t, C["s07"], [("N", 35, Q.cor_el("N")), ("H", 5, PALE["H"]), ("O", 60, Q.cor_el("O"))], 1450, 560, 230, destaque=(0,))
    E.frase(c, t, C["s07.a"], [("28 g", "g", 70, COR)] + ps("de nitrogênio em", "i", 72) + [("80 g", "g", 70)], XE, 520, passo=0.12)
    E.formula_em(c, t, C["s07.b"], "28 ÷ 80 = 0,35", XE, 700, 92, "g", TINTA)
    E.formula_em(c, t, C["s07.c"], "0,35 × 100 =", XE, 880, 92, "g", TINTA2)
    bola_txt(c, t, C["s07.c"] + 0.6, "35%", XE + 820, 850, 100, 76)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s08"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s08.a"], ps("contar o nitrogênio uma vez só", "i", 70), XE + 450, 190, passo=0.12)
    Q.formula_em(c, t, C["s08"] + 0.3, "NH4NO3", XE, 420, 170)
    G = [g for g in Q.grupos("NH4NO3", XE, 420, 170) if g["s"] == "N"]

    def errado():
        g = G[0]
        q = ep(t, C["s08.a"] + 0.6, 0.4)
        if q > 0:
            E.caixa_pontilhada(c, g["x0"] - 10, g["topo"] - 10, g["x1"] - g["x0"] + 20, g["base"] - g["topo"] + 20, q, ERRADO, prog_=q)
        E.formula_em(c, t, C["s08.b"], "14 ÷ 80 = 17,5%", XE, 640, 96, "g", ERRADO)
        if t >= C["s08.c"]:
            E.risco(c, XE - 10, 660, XE + 820, 570, t, C["s08.c"], largura=12)
            pilula_em(c, t, C["s08.c"] + 0.3, "a metade do certo", XE + 1150, 610, 50, ERRADO)
    E.saida(c, t, C["s08.d"] - 0.1, errado)
    if t >= C["s08.d"]:
        for k, g in enumerate(G):
            q = ep(t, C["s08.d"] + 0.3 * k, 0.4)
            E.caixa_pontilhada(c, g["x0"] - 10, g["topo"] - 10, g["x1"] - g["x0"] + 20, g["base"] - g["topo"] + 20, q, E.COR, prog_=q)
        E.frase(c, t, C["s08.d"] + 0.4, ps("procure o mesmo símbolo", "i", 72) + [("duas vezes", "g", 68, COR)], XE, 700, passo=0.12)
        E.formula_em(c, t, C["s08.d"] + 1.6, "2 × 14 = 28", XE, 860, 84, "g", TINTA)
        E.foco(c, t, C["s08.d"] + 2.0, 0.4, lambda a: E.selo(c, XE + 620, 832, 46, True, a))


# ---------------- fórmula mínima ----------------
def b_minima(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], [("fórmula", "g", 90, COR), ("mínima", "g", 90, COR)], XE, 220, passo=0.15)
        E.frase(c, t, C["s09.b"], ps("a menor proporção inteira entre os átomos", "i", 60, TINTA2), XE, 320, passo=0.1)
        Q.formula_em(c, t, C["s09.c"], "C6H12O6", XE, 560, 190, cores={"indice": E.COR} if t >= C["s09.d"] else None)
        G = [g for g in Q.grupos("C6H12O6", XE, 560, 190) if g["tipo"] == "el"]
        for k, g in enumerate(G):
            pilula_em(c, t, C["s09.d"] + 0.3 * k, "÷ 6", g["x1"] - 28, 670, 42, E.COR)
        E.foco(c, t, C["s09.e"], 0.5, lambda a: E.formula(c, "→", XE + 920, 560, 150, "g", TINTA2, a))
        Q.formula_em(c, t, C["s09.e"] + 0.3, "CH2O", XE + 1120, 560, 190, cores={"indice": E.COR})
        E.frase(c, t, C["s09.e"] + 1.2, [("1", "g", 60, COR), ("C", "g", 60), (":", "g", 60, TINTA2), ("2", "g", 60, COR), ("H", "g", 60),
                                         (":", "g", 60, TINTA2), ("1", "g", 60, COR), ("O", "g", 60)], XE + 1120, 760, passo=0.1)
        return
    E.frase(c, t, C["s10.a"], ps("mostra a", "i", 80) + [("proporção,", "g", 76, COR)] + ps("não a molécula", "i", 80), XE, 230, passo=0.12)
    Q.formula_em(c, t, C["s10.a"] + 0.6, "C6H12O6", XE, 480, 150)
    E.formula_em(c, t, C["s10.b"], "= 6 ×", XE + 700, 480, 120, "g", COR)
    Q.formula_em(c, t, C["s10.b"] + 0.4, "CH2O", XE + 1060, 480, 150)
    for k in range(6):
        x = XE + 110 + k * 270
        E.foco(c, t, C["s10.b"] + 0.8 + 0.15 * k, 0.4, lambda a, x=x: chip(c, "CH2O", x, 720, 56, a=a))
    E.foco(c, t, C["s10.b"] + 1.8, 0.4, lambda a: centro(c, "uma molécula de glicose = seis pedaços", W / 2, 880, 54, "i", TINTA2, a))


# ---------------- das porcentagens à fórmula ----------------
PARTES = [("C", 40, "40 g"), ("H", 6.7, "6,7"), ("O", 53.3, "53,3 g")]
BX, BY, BW, BH = 170, 300, 1580, 120


def b_cem(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11"], ps("e se a prova der só as porcentagens?", "i", 70), XE, 220, passo=0.1)
        for k, (el, pc, _), tk in zip(range(3), PARTES, ("s11.a", "s11.b", "s11.c")):
            x = 380 + k * 560
            Q.atomo_em(c, t, C[tk], x, 560, 86 if el != "H" else 66, el)
            E.foco(c, t, C[tk] + 0.3, 0.4, lambda a, x=x, pc=pc: centro(c, f"{str(pc).replace('.', ',')}%", x, 790, 110, "g", COR, a))
            E.foco(c, t, C[tk] + 0.5, 0.4, lambda a, x=x, el=el: centro(c, Q.NOMES[el], x, 880, 54, "i", TINTA2, a))
        return
    if t < C["s15"]:
        def tela():
            E.frase(c, t, C["s12.a"], [("1", "g", 60, COR)] + ps("imagine", "i", 64) + [("100 g", "g", 60, COR)], XE, 200, passo=0.12)
            xs = barra_massa(c, t, C["s12.b"], PARTES, BX, BY, BW, BH, d=1.2)
            E.foco(c, t, C["s12.c"], 0.4, lambda a: centro(c, "% vira grama", 1480, 200, 56, "i", TINTA2, a))
            # passo 2: ÷ massa molar = mols
            if t >= C["s13.a"]:
                E.frase(c, t, C["s13.a"], [("2", "g", 56, COR), ("÷ massa molar", "g", 52), ("=", "g", 52, TINTA2), ("mols", "i", 58)], XE, 540, passo=0.12)
            for x, (txt, tk) in zip(xs, (("40 ÷ 12 ≈ 3,3", "s13.b"), ("6,7 ÷ 1 = 6,7", "s13.c"), ("53,3 ÷ 16 ≈ 3,3", "s13.d"))):
                E.formula_em(c, t, C[tk], txt, max(x, 330), 640, 50, "g", TINTA, "center")
            # passo 3: ÷ o menor
            if t >= C["s14.a"]:
                E.frase(c, t, C["s14.a"], [("3", "g", 56, COR), ("÷ o menor,", "g", 52), ("3,3", "g", 52, COR)], XE, 780, passo=0.12)
            for x, (txt, tk) in zip(xs, (("1", "s14.b"), ("2", "s14.c"), ("1", "s14.d"))):
                bola_txt(c, t, C[tk], txt, max(x, 330), 890, 54, 60)
            Q.formula_em(c, t, C["s14.e"], "CH2O", 1480, 820, 120, cores={"indice": E.COR})
            E.foco(c, t, C["s14.e"] + 0.4, 0.4, lambda a: centro(c, "fórmula mínima", 1600, 900, 46, "i", TINTA2, a))
        E.saida(c, t, C["s15"] - 0.1, tela)
        return
    E.frase(c, t, C["s15.a"], ps("se a prova der a massa molar:", "i", 70), XE, 240, passo=0.1)
    E.formula_em(c, t, C["s15.a"] + 1.0, "M = 180", XE, 380, 100, "g", COR)
    Q.formula_em(c, t, C["s15.b"], "CH2O", XE, 560, 110)
    E.formula_em(c, t, C["s15.b"] + 0.4, "= 12 + 2 + 16 = 30", XE + 330, 560, 84, "g", TINTA2)
    E.formula_em(c, t, C["s15.c"] - 0.4, "180 ÷ 30 =", XE, 740, 100, "g", TINTA)
    bola_txt(c, t, C["s15.c"], "6", XE + 640, 710, 70, 84)
    Q.formula_em(c, t, C["s15.d"], "CH2O × 6 → C6H12O6", XE, 920, 110, cores={"indice": E.COR})


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s16.a"], ps("o atalho:", "i", 72, CLARO) + [("base de 100 g", "g", 70, BR)], W / 2, 190, "center", 0.12)

    def parte1():
        E.formula_em(c, t, C["s16.b"], "40%  →  40 g", W / 2, 340, 100, "g", E.CLARO, "center")
        barra_massa(c, t, C["s16.c"], PARTES, 270, 450, 1380, 110, d=0.9)
        E.foco(c, t, C["s16.c"] + 0.4, 0.4, lambda a: E.escreve(c, "100 g", 120, 525, 50, "g", BR, a))
        barra_massa(c, t, C["s16.c"] + 1.0, [(el, pc, "") for el, pc, _ in PARTES], 270, 610, 690, 80, d=0.9)
        E.foco(c, t, C["s16.c"] + 1.4, 0.4, lambda a: E.escreve(c, "50 g", 120, 665, 50, "g", BR, a))
        E.foco(c, t, C["s16.c"] + 1.8, 0.4, lambda a: centro(c, "a proporção não depende de quanto você pega", W / 2, 800, 52, "i", CLARO, a))
    E.saida(c, t, C["s16.d"] - 0.1, parte1)
    if t >= C["s16.d"]:
        E.frase(c, t, C["s16.d"], [("não", "g", 64, ERRADO), ("compensa:", "i", 70, CLARO)] + ps("a prova já deu as massas", "i", 70, CLARO), W / 2, 420, "center", 0.12)
        E.formula_em(c, t, C["s16.d"] + 1.2, "2,4 g de C  ÷ 12", W / 2, 620, 90, "g", BR, "center")
        E.foco(c, t, C["s16.d"] + 1.8, 0.4, lambda a: centro(c, "divida essas massas direto", W / 2, 760, 54, "i", E.CLARO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s17.a"], ps("butano, do gás de cozinha:", "i", 64, TINTA2), XE, 300, passo=0.1)
    Q.formula_em(c, t, C["s17.a"] + 1.0, "C4H10", XE, 450, 140)
    E.frase(c, t, C["s17.b"], [("1", "g", 56, COR)] + ps("qual é a fórmula mínima?", "i", 62), XE, 570, passo=0.1)
    Q.formula_em(c, t, C["s17.c"], "CH4", XE, 760, 140)
    E.frase(c, t, C["s17.c"] + 0.5, ps("metano", "i", 62, TINTA2), XE + 330, 740)
    E.frase(c, t, C["s17.d"], [("2", "g", 56, COR)] + ps("quantos % da massa é carbono?", "i", 62), XE, 880, passo=0.1)
    E.foco(c, t, C["s17.a"] + 1.2, 0.4, lambda a: (E.pilula(c, "C = 12", 800, 410, 44, "g", fundo=TINTA, a=a), E.pilula(c, "H = 1", 1020, 410, 44, "g", fundo=TINTA, a=a)))
    if t < C["s18"]:
        Q.molecula(c, t, C["s17.c"] + 0.2, "CH4", 1560, 480, 150, passo=0.12)
    else:
        E.relogio(c, t, C["s18.a"], cx=1520, cy=450, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    Q.formula_em(c, t, C["s19"], "C4H10", XE, 300, 150, cores={"indice": E.COR} if t >= C["s19.a"] else None)
    G = [g for g in Q.grupos("C4H10", XE, 300, 150) if g["tipo"] == "el"]
    for k, g in enumerate(G):
        pilula_em(c, t, C["s19.a"] + 0.3 * k, "÷ 2", g["x1"] - 28, 400, 40, E.COR)
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.formula(c, "→", XE + 560, 300, 120, "g", TINTA2, a))
    Q.formula_em(c, t, C["s19.b"] + 0.3, "C2H5", XE + 760, 300, 150, cores={"indice": E.COR})
    E.foco(c, t, C["s19.b"] + 0.9, 0.4, lambda a: E.selo(c, XE + 1180, 250, 46, True, a))
    Q.formula_em(c, t, C["s19.c"], "CH4", XE, 620, 130)
    E.formula_em(c, t, C["s19.c"] + 0.5, "= 12 + 4 = 16 g/mol", XE + 300, 620, 80, "g", TINTA2)
    E.formula_em(c, t, C["s19.d"], "12 ÷ 16 = 0,75", XE, 860, 92, "g", TINTA)
    bola_txt(c, t, C["s19.e"], "75%", XE + 880, 830, 96, 76, CERTO)
    pz(c, t, C["s19.d"], [("C", 75, "#3A3A40"), ("H", 25, PALE["H"])], 1580, 820, 150, destaque=(0,))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s20.a", [("%", "g", 66, COR), ("=", "g", 66, TINTA2)] + ps("massa do elemento ÷ massa molar × 100", "i", 66)),
                 ("s20.b", [("fórmula mínima", "g", 66), ("=", "g", 66, TINTA2)] + ps("menor proporção inteira", "i", 70)),
                 ("s20.c", [("com %:", "g", 66)] + ps("comece por", "i", 70) + [("100 g", "g", 66, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    Q.formula_em(c, t, C["s21.a"], "2 H2 + O2 → 2 H2O", XE, 440, 100, cores={"coef": E.COR})
    E.frase(c, t, C["s21.a"] + 0.8, ps("lida em", "i", 70, TINTA2) + [("mols", "g", 66, COR)], XE, 560, passo=0.1)
    E.frase(c, t, C["s21.b"], [("a", "i", 76), ("proporção", "g", 76, COR), ("das", "i", 76), ("massas", "g", 76)], XE, 760, passo=0.12)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, percentual=b_percentual, erro=b_erro, minima=b_minima, cem=b_cem, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
