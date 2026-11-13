"""Visual — Estudativo · QUI-CAL-002: mol, massa molar e Avogadro.

Segue a linguagem visual da trilha (cabeçalho da QUI-CAL-001) e a da Química (cabeçalho da QUI-MIS-001).
Aqui nasce a PONTE DO MOL (ponte_mol): gramas à esquerda, o mol na esfera turquesa no meio, moléculas à direita; cada vão
tem a operação numa pílula (÷ massa molar, × 6 × 10²³). A dúzia de ovos (caixa_ovos) é o modelo de "pacote".
Peças candidatas ao kit quimica.py: ponte_mol() e pacotes() (barra cortada em pacotes iguais: quantas vezes cabe)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-002_mol_massa_molar_avogadro.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("mol", "massa", "ponte", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NA = 6e23

# todas as contas da aula
assert 36 / 18 == 2 and 2 * NA == 1.2e24 and 2 * 6 == 12
assert abs(36 * NA - 2.16e25) < 1e10 and round(36 * NA / (2 * NA)) == 18
assert 132 / 44 == 3 and abs(3 * NA - 1.8e24) < 1e10 and 3 * 6 == 18
assert abs(50 / 18 - 2.78) < 0.01


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


def caixa_ovos(c, t, t0, x, y, k=1.0):
    """caixa com uma dúzia de ovos (2 × 6) que entram um a um"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    M.rrect(c, x, y, 640 * k, 230 * k, 26 * k, "#C9B79C", q, shadow=True)
    for i in range(12):
        cx, cy = x + (60 + (i % 6) * 104) * k, y + (62 + (i // 6) * 106) * k
        e = ease_back(prog(t, t0 + 0.2 + 0.06 * i, 0.35))
        if e > 0:
            r = skia.Rect.MakeXYWH(cx - 38 * k * e, cy - 46 * k * e, 76 * k * e, 92 * k * e)
            c.drawOval(r, M.paint("#FFF6E6", 1.0))
            c.drawOval(r, M.paint("#D9C3A0", 1.0, stroke=3))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        caixa_ovos(c, t, C["s01.a"], XE, 250, 0.8)
        E.frase(c, t, C["s01.a"] + 0.8, [("1 dúzia", "g", 70, COR), ("=", "g", 70, TINTA2), ("12", "g", 70)], XE, 520, passo=0.12)
        E.frase(c, t, C["s01.b"], [("1 mol", "g", 70, COR)] + ps("de água =", "i", 74), XE, 720, passo=0.12)
        E.formula_em(c, t, C["s01.b"] + 0.9, "6 × 10^{23}", XE + 640, 724, 92, "g", TINTA)
        E.foco(c, t, C["s01.b"] + 1.6, 0.4, lambda a: E.escreve(c, "moléculas: 600 sextilhões", XE, 810, 54, "i", TINTA2, a))
        Q.bequer(c, t, C["s01.c"], 1480, 880, 300, 340, 0.45, Q.AGUA, te=C["s01.c"] + 0.3, d=1.0, graduacao=False)
        E.foco(c, t, C["s01.c"] + 0.8, 0.4, lambda a: centro(c, "36 g de água", 1480, 960, 60, "g", TINTA, a))
        E.foco(c, t, C["s01.d"], 0.5, lambda a: (centro(c, "o dobro:", 1480, 280, 56, "i", TINTA2, a),
                                                 E.formula(c, "1,2 × 10^{24}", 1480, 380, 84, "g", COR, a, "center")))
        E.frase(c, t, C["s01.e"], ps("sem contar uma por uma", "i", 66, TINTA2), XE, 960, "left", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("o", "i", 74), ("mol", "g", 70, COR)]),
                 (C["s02.c"], [("gramas", "g", 70), ("→", "g", 70, TINTA2), ("mol", "g", 70, COR), ("→", "g", 70, TINTA2), ("moléculas", "g", 70)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 80) + [("três coisas", "g", 76, COR)], XE, 200, passo=0.12)
    y = [400, 640, 880]
    for i, k in enumerate(("s03.b", "s03.c", "s03.d")):
        E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, XE + 40, y[i] - 30, 44, a=a), centro(c, str(i + 1), XE + 40, y[i] - 8, 54, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, ps("massa molecular", "i", 70), XE + 110, y[0])
    Q.formula_em(c, t, C["s03.b"] + 0.5, "H2O", XE + 640, y[0] + 6, 110)
    E.formula_em(c, t, C["s03.b"] + 0.9, "= 18 u", XE + 860, y[0] + 6, 90, "g", COR)
    E.frase(c, t, C["s03.c"] + 0.1, ps("regra de três", "i", 70), XE + 110, y[1])
    E.formula_em(c, t, C["s03.c"] + 0.6, "f{3}{7} = f{18}{x}", XE + 640, y[1] + 10, 70, "g", TINTA)
    E.frase(c, t, C["s03.d"] + 0.1, ps("notação científica", "i", 70), XE + 110, y[2])
    E.formula_em(c, t, C["s03.d"] + 0.7, "2 × 6 × 10^{23} = 12 × 10^{23}", XE + 700, y[2] + 6, 70, "g", TINTA)


# ---------------- o mol ----------------
def b_mol(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("pequenos demais para contar", "i", 76), XE, 200, passo=0.12)
        E.frase(c, t, C["s04.a"] + 1.4, ps("de um em um", "i", 76, TINTA2), XE, 300, passo=0.12)
        E.foco(c, t, C["s04.a"] + 0.5, 0.6, lambda a: (Q.particulas(c, t, 1130, 160, 620, 300, 46, "gas", tipos=[("O", 0.34), ("H", 0.66)], r=13, semente=3, a=a)))
        caixa_ovos(c, t, C["s04.b"], XE, 470, 0.8)
        E.foco(c, t, C["s04.b"] + 0.8, 0.4, lambda a: E.escreve(c, "a feira conta em dúzias", XE, 730, 54, "i", TINTA2, a))
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.escreve(c, "a Química conta em", 1000, 650, 60, "i", TINTA, a))
        E.foco(c, t, C["s04.c"] + 0.6, 0.5, lambda a: E.escreve(c, "mol", 1000, 880, 240, "g", COR, a))
        return
    E.frase(c, t, C["s05.a"], [("1 mol", "g", 110, COR), ("=", "g", 110, TINTA2)], XE, 330, passo=0.12)
    E.formula_em(c, t, C["s05.a"] + 0.8, "6 × 10^{23}", XE + 540, 330, 130, "g", TINTA)
    E.foco(c, t, C["s05.a"] + 1.6, 0.4, lambda a: E.escreve(c, "unidades de qualquer coisa", XE, 440, 56, "i", TINTA2, a))
    pilula_em(c, t, C["s05.b"], "constante de Avogadro", XE + 470, 540, 52, E.COR)
    Q.molecula(c, t, C["s05.c"], "H2O", 1460, 640, 130, passo=0.12)
    E.foco(c, t, C["s05.c"] + 0.6, 0.4, lambda a: (E.formula(c, "× 6 × 10^{23}", 1460, 830, 70, "g", COR, a, "center"),
                                                  centro(c, "moléculas de água", 1460, 910, 50, "i", TINTA2, a)))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: (E.formula(c, "6,02 × 10^{23}", XE, 780, 80, "g", TINTA2, a),
                                             E.escreve(c, "mais preciso", XE, 860, 50, "i", TINTA2, a)))
    E.foco(c, t, C["s05.d"] + 1.6, 0.5, lambda a: (E.escreve(c, "a prova usa", XE, 960, 56, "i", TINTA, a), E.escreve(c, "6", XE + 330, 965, 80, "g", COR, a)))


# ---------------- massa molar ----------------
def b_massa(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], [("o", "i", 80), ("truque", "g", 76, COR)], XE, 200, passo=0.12)
        E.frase(c, t, C["s06.b"], ps("1 mol tem, em gramas,", "i", 70), XE, 320, passo=0.1)
        E.frase(c, t, C["s06.b"] + 1.4, ps("o número da massa molecular", "i", 70), XE, 410, passo=0.1)
        Q.molecula(c, t, C["s06.c"], "H2O", 520, 640, 130, passo=0.1)
        E.foco(c, t, C["s06.c"] + 0.5, 0.4, lambda a: (centro(c, "1 molécula", 520, 820, 52, "i", TINTA2, a), centro(c, "18 u", 520, 940, 110, "g", TINTA, a)))
        p = ep(t, C["s06.d"], 0.5)
        if p > 0:
            M.arrow(c, 800, 680, lerp(800, 1080, ease_io(p)), 680, E.COR, 1.0, 7, 24)
        Q.bequer(c, t, C["s06.d"], 1360, 820, 280, 300, 0.3, Q.AGUA, te=C["s06.d"] + 0.2, d=0.8, graduacao=False,
                 particulas=dict(n=26, estado="liquido", tipos=[("O", 0.34), ("H", 0.66)], r=9, semente=2))
        E.foco(c, t, C["s06.d"] + 0.6, 0.4, lambda a: (centro(c, "1 mol", 1360, 880, 52, "i", TINTA2, a), centro(c, "18 g", 1360, 1000, 110, "g", COR, a)))
        return
    E.frase(c, t, C["s07.a"], [("massa", "g", 120, COR), ("molar", "g", 120, COR)], XE, 300, passo=0.15)
    E.foco(c, t, C["s07.a"] + 1.0, 0.4, lambda a: E.escreve(c, "a massa de 1 mol", XE, 400, 60, "i", TINTA2, a))
    pilula_em(c, t, C["s07.b"], "g/mol", XE + 920, 268, 66, TINTA)
    Q.formula_em(c, t, C["s07.c"], "CO2", XE, 640, 150)
    E.formula_em(c, t, C["s07.c"] + 0.6, "44 u", XE + 400, 640, 110, "g", TINTA)
    E.formula_em(c, t, C["s07.c"] + 1.2, "→  44 g/mol", XE + 700, 640, 110, "g", COR)
    E.frase(c, t, C["s07.d"], ps("a mesma conta: troque", "i", 64) + [("u", "g", 60), ("por", "i", 64), ("g/mol", "g", 60, COR)], XE, 860, passo=0.1)


# ---------------- a ponte do mol ----------------
def b_ponte(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08"], ps("o mol é uma", "i", 80) + [("ponte", "g", 76, COR)], W / 2, 220, "center", 0.12)
        ponte_mol(c, t, C["s08.a"], 560, ("gramas", C["s08.b"]), ("mol", C["s08.d"]), ("moléculas", C["s08.c"]),
                  te=C["s08.d"] + 0.3, td=C["s08.d"] + 0.6, size=70)
        E.frase(c, t, C["s08.d"] + 0.8, ps("sempre se passa pelo mol", "i", 64, TINTA2), W / 2, 860, "center", 0.1)
        return
    # s09 e s10: a ponte no alto, a conta embaixo
    ponte_mol(c, t, C["s09"], 250, ("36 g", C["s09.a"]), ("2 mol", C["s09.e"]) if t >= C["s09.e"] else ("?", C["s09"] + 0.3),
              ("1,2 × 10^{24}", C["s10.c"]), rot_e="÷ 18", rot_d="× 6 × 10²³", te=C["s09.b"], td=C["s10.a"], size=62)

    def s09():
        Q.regra_tres(c, t, C["s09.c"] - 0.4, ("massa", "mol"), [("18 g", "1 mol"), ("36 g", "x")], 760, 560, 80,
                     tl=[C["s09.c"], C["s09.d"]], tcruz=C["s09.e"] - 0.6, res="2 mol", tres=C["s09.e"], dx=440)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("1 mol", "g", 64, COR), ("=", "g", 64, TINTA2)], XE, 540, passo=0.1)
    E.formula_em(c, t, C["s10.a"] + 0.6, "6 × 10^{23} moléculas", XE + 300, 540, 64, "g", TINTA)
    E.formula_em(c, t, C["s10.b"], "2 × 6 × 10^{23} = 12 × 10^{23}", XE, 720, 84, "g", TINTA)
    E.formula_em(c, t, C["s10.c"], "= 1,2 × 10^{24}", XE + 780, 880, 96, "g", COR)
    E.foco(c, t, C["s10.c"] + 0.8, 0.4, lambda a: E.escreve(c, "moléculas", XE + 1440, 880, 60, "i", TINTA2, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("pular o mol", "i", 76), XE + 450, 190, passo=0.12)
    ponte_mol(c, t, C["s11"], 400, "36 g", ("mol", C["s11"] + 0.2), "moléculas", size=58)
    p = ease_io(prog(t, C["s11.a"] + 0.5, 0.8))
    if p > 0:
        pth = skia.Path(); pth.moveTo(420, 330); pth.quadTo(960, 120, 1500, 330)
        m = skia.PathMeasure(pth, False); seg = skia.Path(); m.getSegment(0, m.getLength() * p, seg, True)
        c.drawPath(seg, M.paint(ERRADO, 1.0, stroke=7))
    E.formula_em(c, t, C["s11.b"], "36 × 6 × 10^{23} = 2,16 × 10^{25}", XE, 650, 84, "g", ERRADO)
    if t >= C["s11.c"]:
        E.risco(c, XE - 10, 670, XE + 1330, 590, t, C["s11.c"], largura=12)
        pilula_em(c, t, C["s11.c"] + 0.3, "18 vezes o certo", 1600, 560, 46, ERRADO)
    E.frase(c, t, C["s11.d"], ps("o Avogadro conta por", "i", 68) + [("mol", "g", 64, COR)] + ps("não por grama", "i", 68), XE, 820, passo=0.1)
    E.frase(c, t, C["s11.e"], ps("primeiro,", "i", 68) + [("÷ massa molar", "g", 64, COR)], XE, 940, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        E.frase(c, t, C["s12"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        E.frase(c, t, C["s12.a"], ps("quantas vezes a massa molar", "i", 70, BR) + [("cabe?", "g", 66, E.CLARO)], W / 2, 290, "center", 0.12)
        E.formula_em(c, t, C["s12.b"], "36 g", XE, 520, 90, "g", BR)
        pacotes(c, t, C["s12.b"] + 0.5, 2, XE + 300, 430, 1000, 130, "18 g")
        E.foco(c, t, C["s12.b"] + 1.4, 0.4, lambda a: E.escreve(c, "= 2 mol", XE + 1350, 520, 90, "g", E.CLARO, a))
        E.formula_em(c, t, C["s12.c"], "2 × 6 × 10^{23} moléculas", W / 2, 800, 84, "g", BR, "center")
        E.foco(c, t, C["s12.c"] + 0.8, 0.4, lambda a: centro(c, "dois Avogadros", W / 2, 900, 56, "i", E.CLARO, a))
        return
    E.frase(c, t, C["s13.a"], ps("contar pacotes é", "i", 72, CLARO) + [("dividir", "g", 66, BR)], W / 2, 230, "center", 0.12)
    E.frase(c, t, C["s13.b"], [("não", "g", 64, ERRADO), ("compensa:", "i", 68, CLARO)] + ps("o pacote não cabe inteiro", "i", 68, CLARO), W / 2, 380, "center", 0.12)
    E.formula_em(c, t, C["s13.b"] + 1.0, "50 g", XE, 600, 84, "g", BR)
    pacotes(c, t, C["s13.b"] + 1.3, 2, XE + 300, 520, 720, 120, "18 g")
    q = ep(t, C["s13.b"] + 2.2, 0.4)
    if q > 0:
        M.rrect(c, XE + 1024, 520, 280 * ease_out(q), 120, 14, "#3A4A55", q)
        centro(c, "14 g", XE + 1164, 600, 56, "g", BR, q)
    E.formula_em(c, t, C["s13.c"], "50 ÷ 18 ≈ 2,8 mol", W / 2, 860, 90, "g", E.CLARO, "center")
    E.foco(c, t, C["s13.c"] + 0.6, 0.4, lambda a: centro(c, "arme a divisão com vírgula", W / 2, 960, 52, "i", CLARO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s14.a"], [("132 g", "g", 70)] + ps("de gás carbônico", "i", 72), XE, 330, passo=0.12)
    Q.formula_em(c, t, C["s14.a"] + 1.0, "CO2", XE + 780, 340, 110)
    E.frase(c, t, C["s14.b"], [("M", "g", 60, TINTA2), ("=", "g", 60, TINTA2), ("44 g/mol", "g", 60, COR)], XE, 450, passo=0.12)
    E.frase(c, t, C["s14.c"], [("1", "g", 56, COR)] + ps("quantos mols?", "i", 64), XE, 640, passo=0.1)
    E.frase(c, t, C["s14.d"], [("2", "g", 56, COR)] + ps("quantas moléculas?", "i", 64), XE, 760, passo=0.1)
    if t < C["s15"]:
        Q.molecula(c, t, C["s14.a"] + 0.6, "CO2", 1460, 520, 150, passo=0.15)
    else:
        E.relogio(c, t, C["s15.a"], cx=1470, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ponte_mol(c, t, C["s16"], 230, "132 g", ("3 mol", C["s16.b"]) if t >= C["s16.b"] else ("?", C["s16"]), ("1,8 × 10^{24}", C["s16.d"]),
              rot_e="÷ 44", rot_d="× 6 × 10²³", te=C["s16.a"], td=C["s16.c"], size=60)
    E.frase(c, t, C["s16.a"], ps("quantas vezes 44 cabe em 132?", "i", 64), XE, 480, passo=0.1)
    pacotes(c, t, C["s16.a"] + 1.0, 3, XE, 540, 1200, 120, "44 g")
    bola_txt(c, t, C["s16.b"], "3 mol", XE + 1480, 600, 85, 56)
    E.formula_em(c, t, C["s16.c"], "3 × 6 × 10^{23} = 18 × 10^{23}", XE, 860, 80, "g", TINTA)
    bola_txt(c, t, C["s16.d"], "1,8 × 10^{24}", 1580, 900, 130, 48, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s17.a", [("1 mol", "g", 66), ("=", "g", 66, TINTA2), ("6 × 10²³", "g", 66), ("unidades", "i", 70)]),
                 ("s17.b", [("massa molar", "g", 66), ("=", "g", 66, TINTA2)] + ps("massa molecular em gramas", "i", 70)),
                 ("s17.c", [("massa", "g", 66), ("→", "g", 66, TINTA2), ("mol", "g", 66, COR), ("→", "g", 66, TINTA2), ("moléculas", "g", 66)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s18.a"], [("quanto", "i", 76), ("%", "g", 84, COR), ("de", "i", 76), ("cada", "i", 76), ("elemento", "g", 76)], XE, 420, passo=0.12)
    Q.formula_em(c, t, C["s18.a"] + 1.0, "NH4NO3", XE, 590, 110)
    E.frase(c, t, C["s18.b"], [("fórmula", "g", 90, COR), ("mínima", "g", 90, COR)], XE, 790, passo=0.12)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s18.c"] + 0.2, 0.4))
    E.frase(c, t, C["s18.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, mol=b_mol, massa=b_massa, ponte=b_ponte, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
