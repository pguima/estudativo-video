"""Visual — Estudativo · QUI-CAL-009: praticando mol e estequiometria (aula de prática, quatro questões).

Segue a linguagem da estequiometria (cabeçalho da QUI-CAL-004), a da trilha (QUI-CAL-001) e a da Química (QUI-MIS-001).
Cada questão abre com a CABEÇA (cabeca): pílula "questão N" e a ferramenta da vez numa pílula cinza; o enunciado vem em
linhas curtas com a equação em Q.formula; na pausa entra o relógio à direita. A resolução reaproveita as peças das aulas:
ponte do mol (002), amostra pura × impureza (007), barra de rendimento (008) e a divisão do limitante (006).
Resposta final na esfera verde."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-009_praticando_estequiometria.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "fim"))
BR = "#FFFFFF"
EQF = "Fe2O3 + 3 CO -> 2 Fe + 3 CO2"
EQN = "N2 + 3 H2 -> 2 NH3"
EQC = "CaO + SO2 -> CaSO3"
IMP = "#B7B2A8"

# todas as contas da aula
for e in (EQF, EQN, EQC):
    assert Q.lados(e)[0] == Q.lados(e)[1], e
assert 880 / 44 == 20 and abs(20 * 6e23 - 1.2e25) < 1e12
assert 2 * 56 + 3 * 16 == 160 and 2 * 56 == 112 and 0.8 * 1000 == 800 and 800 / 160 == 5 and 5 * 112 == 560
assert 28 + 6 == 34 and 56 / 28 * 34 == 68 and 68 / 4 == 17
assert 40 + 16 == 56 and 32 + 32 == 64 and 112 / 56 == 2 and 160 / 64 == 2.5 and 2 * 64 == 128 and 160 - 128 == 32


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


def cabeca(c, t, t0, n, tema):
    E.foco(c, t, t0, 0.4, lambda a: (E.pilula(c, f"questão {n}", XE + 150, 170, 52, "g", fundo=E.COR, a=a),
                                     E.pilula(c, tema, XE + 470, 170, 44, "b", fundo="#5A5F66", a=a)))


def barra(c, t, t0, x, y, w, h, frac, rot1, rot2, cor2=IMP, d=0.9):
    """barra cortada em duas partes: frac na cor da matéria e o resto em cor2"""
    p = ease_out(prog(t, t0, d))
    if p <= 0:
        return
    w1 = w * frac
    M.rrect(c, x, y, w1 * min(1, p * 1.25), h, 18, E.COR, 1.0)
    if p > 0.8:
        M.rrect(c, x + w1 + 6, y, (w - w1 - 6) * (p - 0.8) / 0.2, h, 18, cor2, 1.0)
    if p >= 1:
        centro(c, rot1, x + w1 / 2, y + h / 2 + 20, 52, "g", BR, 1.0)
        centro(c, rot2, x + w1 + (w - w1) / 2, y + h / 2 + 16, 42, "g", TINTA, 1.0)


def relogio_dir(c, t, C, k):
    E.relogio(c, t, C[k], cx=1560, cy=520, r=170)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    for k, s in enumerate(("escapamento", "siderúrgica", "fábrica de adubo", "chaminé")):
        pilula_em(c, t, C["s01.a"] + 0.35 * k, s, XE + 180 + k * 430, 260, 50, "#5A5F66")
    E.frase(c, t, C["s01.b"], ps("a estequiometria vem", "i", 76) + [("vestida de problema real", "g", 70, COR)], XE, 470, passo=0.12)
    E.frase(c, t, C["s01.c"], [("4", "g", 140, COR)] + ps("questões", "i", 110), XE, 720, passo=0.15)
    for k, s in enumerate(("mol", "pureza", "rendimento", "limitante")):
        pilula_em(c, t, C["s01.d"] + 0.3 * k, s, XE + 160 + k * 360, 900, 54, E.COR)
    E.foco(c, t, C["s01.a"] + 0.4, 0.8, lambda a: E.simbolo(c, 1680, 720, 150 * ease_back(prog(t, C["s01.a"] + 0.4, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02.a"], [("as", "i", 84), ("ferramentas", "g", 80, COR)], XE, 180, passo=0.12)
    itens = (("s02.b", [("massa", "g", 60), ("÷", "g", 60, TINTA2), ("massa molar", "g", 60), ("=", "g", 60, TINTA2), ("mol", "g", 60, COR)]),
             ("s02.c", [("massas", "g", 60)] + ps("embaixo da equação e", "i", 64) + [("regra de três", "g", 60)]),
             ("s02.d", [("pureza", "g", 60, COR), ("e", "i", 64), ("rendimento", "g", 60, COR), ("multiplicam", "i", 64)]),
             ("s02.e", [("limitante", "g", 60, COR), ("=", "g", 60, TINTA2)] + ps("menor resultado de", "i", 64) + [("tenho ÷ equação", "g", 60)]))
    for i, (k, partes) in enumerate(itens):
        y = 360 + i * 150
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 24, 42, a=a), centro(c, str(i + 1), XE + 40, y - 4, 50, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, XE + 110, y, passo=0.1)
    E.frase(c, t, C["s02.e"] + 2.4, ps("pause e tente antes de cada resposta", "i", 56, TINTA2), XE, 990, passo=0.1)


# ---------------- questão 1: mol ----------------
def b_q1(c, t, C, b):
    cabeca(c, t, C["s03.a"], 1, "mol")
    E.frase(c, t, C["s03.b"], ps("um carro solta", "i", 70) + [("880 g", "g", 66, COR)] + ps("de gás carbônico", "i", 70), XE, 360, passo=0.1)
    Q.formula_em(c, t, C["s03.c"], "CO2", XE, 520, 110)
    E.formula_em(c, t, C["s03.c"] + 0.4, "M = 44 g/mol", XE + 280, 520, 76, "g", TINTA)
    E.frase(c, t, C["s03.d"], ps("quantos", "i", 70) + [("mols", "g", 66, COR)] + ps("e quantas", "i", 70) + [("moléculas?", "g", 66, COR)], XE, 720, passo=0.1)
    if t < C["s04"]:
        Q.molecula(c, t, C["s03.c"], "CO2", 1520, 500, 150, passo=0.15)
    else:
        relogio_dir(c, t, C, "s04.a")


def b_q1r(c, t, C, b):
    cabeca(c, t, C["s05"], 1, "mol")
    ponte_mol(c, t, C["s05"], 420, ("880 g", C["s05"] + 0.2), ("20 mol", C["s05.a"] + 1.2), ("1,2 × 10^{25}", C["s05.c"] + 0.6),
              rot_e="÷ 44", rot_d="× 6 × 10²³", te=C["s05.a"], td=C["s05.b"], size=64)
    E.formula_em(c, t, C["s05.a"], "880 ÷ 44 = 20 mol", XE, 650, 80, "g", TINTA)
    E.formula_em(c, t, C["s05.b"] + 1.4, "20 × 6 × 10^{23} = 120 × 10^{23}", XE, 800, 80, "g", TINTA)
    bola_txt(c, t, C["s05.c"] + 0.6, "1,2 × 10^{25}", 1580, 900, 150, 50, CERTO)
    E.foco(c, t, C["s05.c"] + 1.0, 0.4, lambda a: E.escreve(c, "moléculas", XE, 950, 60, "i", TINTA2, a))


# ---------------- questão 2: pureza ----------------
def b_q2(c, t, C, b):
    cabeca(c, t, C["s06.a"], 2, "pureza")
    E.frase(c, t, C["s06.b"], ps("o ferro sai da", "i", 66) + [("hematita,", "g", 62)], XE, 330, passo=0.1)
    Q.formula_em(c, t, C["s06.b"] + 1.6, "Fe2O3", XE + 700, 335, 90)
    Q.formula_em(c, t, C["s06.c"], EQF, XE, 480, 84)
    cs = Q.centros(EQF, XE, 480, 84, "left")
    E.foco(c, t, C["s06.d"], 0.4, lambda a: (E.formula(c, "160 g", cs[0], 570, 60, "b", TINTA, a, "center"), E.formula(c, "112 g", cs[2], 570, 60, "b", COR, a, "center")))
    E.frase(c, t, C["s06.e"], [("1.000 kg", "g", 66)] + ps("de minério com", "i", 70) + [("80%", "g", 66, COR)] + ps("de hematita", "i", 70), XE, 740, passo=0.1)
    E.frase(c, t, C["s06.e"] + 2.0, ps("quanto ferro sai?", "i", 70), XE, 860, passo=0.1)
    if t >= C["s07"]:
        E.relogio(c, t, C["s07.a"], cx=1640, cy=730, r=140)


def b_q2r(c, t, C, b):
    cabeca(c, t, C["s08"], 2, "pureza")
    barra(c, t, C["s08.a"], XE, 290, 1580, 120, 0.8, "800 kg de hematita", "200 kg")
    E.formula_em(c, t, C["s08.a"] + 0.6, "0,8 × 1.000 = 800 kg", XE, 520, 76, "g", TINTA)
    E.formula_em(c, t, C["s08.b"], "160 → 112", XE, 660, 76, "g", TINTA)
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.escreve(c, "em gramas ou em quilos", XE + 480, 655, 52, "i", TINTA2, a))
    E.formula_em(c, t, C["s08.d"], "800 = 5 × 160", XE, 820, 80, "g", TINTA)
    E.formula_em(c, t, C["s08.e"], "5 × 112 =", XE + 700, 820, 80, "g", TINTA2)
    bola_txt(c, t, C["s08.e"] + 1.4, "560 kg", XE + 1340, 795, 110, 58, CERTO)
    E.foco(c, t, C["s08.e"] + 1.8, 0.4, lambda a: centro(c, "de ferro", XE + 1340, 960, 50, "i", TINTA2, a))


# ---------------- questão 3: rendimento ----------------
def b_q3(c, t, C, b):
    cabeca(c, t, C["s09.a"], 3, "rendimento")
    E.frase(c, t, C["s09.b"], ps("na fábrica de adubo:", "i", 66, TINTA2), XE, 320, passo=0.1)
    Q.formula_em(c, t, C["s09.b"] + 0.6, EQN, XE, 450, 96, cores={"coef": E.COR})
    cs = Q.centros(EQN, XE, 450, 96, "left")
    E.foco(c, t, C["s09.c"], 0.4, lambda a: (E.formula(c, "28 g", cs[0], 550, 60, "b", TINTA, a, "center"), E.formula(c, "34 g", cs[2], 550, 60, "b", COR, a, "center")))
    E.frase(c, t, C["s09.d"], ps("rendimento de", "i", 70) + [("25%", "g", 66, COR)], XE, 710, passo=0.1)
    E.frase(c, t, C["s09.e"], ps("quanta amônia sai de", "i", 70) + [("56 kg", "g", 66, COR)] + ps("de nitrogênio?", "i", 70), XE, 840, passo=0.1)
    if t >= C["s10"]:
        E.relogio(c, t, C["s10.a"], cx=1600, cy=460, r=160)


def b_q3r(c, t, C, b):
    cabeca(c, t, C["s11"], 3, "rendimento")
    E.formula_em(c, t, C["s11.a"], "56 = 2 × 28", XE, 360, 80, "g", TINTA)
    E.formula_em(c, t, C["s11.b"], "máximo: 2 × 34 = 68 kg", XE + 640, 360, 80, "g", TINTA)
    barra(c, t, C["s11.c"], XE, 500, 1580, 120, 0.25, "17 kg", "não sai: 75%", cor2="#E6E6E2")
    E.foco(c, t, C["s11.c"] + 0.4, 0.4, lambda a: E.escreve(c, "25% = um quarto", XE, 720, 60, "i", TINTA2, a))
    E.formula_em(c, t, C["s11.d"], "68 ÷ 4 =", XE, 880, 90, "g", TINTA2)
    bola_txt(c, t, C["s11.d"] + 0.8, "17 kg", XE + 560, 850, 100, 60, CERTO)
    E.foco(c, t, C["s11.d"] + 1.2, 0.4, lambda a: E.escreve(c, "de amônia", XE + 700, 880, 56, "i", TINTA2, a))


# ---------------- questão 4: limitante ----------------
def b_q4(c, t, C, b):
    cabeca(c, t, C["s12.a"], 4, "limitante")
    w = E.frase(c, t, C["s12.b"], ps("segurar o", "i", 64), XE, 320, passo=0.1)
    Q.formula_em(c, t, C["s12.b"] + 0.4, "SO2", XE + w + 20, 325, 80)
    E.frase(c, t, C["s12.b"] + 0.8, ps("que causa chuva ácida", "i", 60, TINTA2), XE + 470, 320, passo=0.1)
    Q.formula_em(c, t, C["s12.c"], EQC, XE, 460, 96)
    cs = Q.centros(EQC, XE, 460, 96, "left")
    E.foco(c, t, C["s12.d"], 0.4, lambda a: (E.formula(c, "56 g", cs[0], 560, 60, "b", TINTA, a, "center"), E.formula(c, "64 g", cs[1], 560, 60, "b", TINTA, a, "center")))
    w = E.frase(c, t, C["s12.e"], ps("entram", "i", 66) + [("112 kg", "g", 62, COR)] + ps("de cal e", "i", 66) + [("160 kg", "g", 62, COR)], XE, 730, passo=0.1)
    Q.formula_em(c, t, C["s12.e"] + 2.0, "SO2", XE + w + 24, 735, 70)
    w = E.frase(c, t, C["s12.f"], ps("quanto", "i", 66), XE, 860, passo=0.1)
    w2 = Q.formula(None, "SO2", 0, 0, 70)
    Q.formula_em(c, t, C["s12.f"] + 0.3, "SO2", XE + w + 20, 865, 70)
    E.frase(c, t, C["s12.f"] + 0.6, ps("escapa?", "i", 66), XE + w + w2 + 40, 860, passo=0.1)
    if t >= C["s13"]:
        E.relogio(c, t, C["s13.a"], cx=1620, cy=500, r=160)


def b_q4r(c, t, C, b):
    cabeca(c, t, C["s14"], 4, "limitante")
    for k, (f, conta_, tk) in enumerate((("CaO", "112 ÷ 56 = 2", "s14.b"), ("SO2", "160 ÷ 64 = 2,5", "s14.c"))):
        x = 520 + 760 * k
        Q.formula_em(c, t, C[tk], f, x, 360, 96, align="center")
        E.formula_em(c, t, C[tk] + 0.4, conta_, x, 500, 80, "g", TINTA, "center")
    pilula_em(c, t, C["s14.d"], "limitante", 520, 600, 46, E.COR)
    pilula_em(c, t, C["s14.d"] + 0.3, "excesso", 1280, 600, 46, "#5A5F66")
    E.formula_em(c, t, C["s14.e"], "2 × 64 = 128 kg retidos", XE, 780, 76, "g", TINTA)
    E.formula_em(c, t, C["s14.f"], "160 − 128 =", XE, 920, 84, "g", TINTA2)
    bola_txt(c, t, C["s14.f"] + 1.4, "32 kg", XE + 720, 890, 96, 60, CERTO)
    E.foco(c, t, C["s14.f"] + 1.8, 0.4, lambda a: E.escreve(c, "escapam", XE + 850, 920, 60, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s15.a"], ps("quatro problemas,", "i", 84) + [("um caminho", "g", 80, COR)], W / 2, 200, "center", 0.12)
        itens = (("s15.b", [("fique com a", "i", 70), ("parte que reage", "g", 66)]),
                 ("s15.c", [("use as", "i", 70), ("massas da equação", "g", 66)]),
                 ("s15.d", [("corrija pelo", "i", 70), ("rendimento", "g", 66, COR), ("no fim", "i", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s16"] - 0.1, resumo)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], [("próxima", "i", 80), ("aula:", "i", 80), ("os gases", "g", 76, COR)], XE, 250, passo=0.12)
    E.frase(c, t, C["s16.a"], [("pressão", "g", 80), ("e", "i", 84), ("volume", "g", 80)], XE, 430, passo=0.12)
    E.frase(c, t, C["s16.b"], ps("temperatura em", "i", 80) + [("kelvin", "g", 76, COR)], XE, 600, passo=0.12)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 780, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s16.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 805, p), ep(t, C["s16.c"] + 0.2, 0.4))
    E.frase(c, t, C["s16.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, q1r=b_q1r, q2=b_q2, q2r=b_q2r, q3=b_q3, q3r=b_q3r, q4=b_q4, q4r=b_q4r, fim=b_fim)
