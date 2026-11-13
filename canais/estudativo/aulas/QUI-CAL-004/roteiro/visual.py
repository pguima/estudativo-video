"""Visual — Estudativo · QUI-CAL-004: lei de Proust e proporção em mols. Primeira aula do módulo Estequiometria.

Segue a linguagem visual da trilha (cabeçalho da QUI-CAL-001) e a da Química (cabeçalho da QUI-MIS-001). Acrescenta a
LINGUAGEM DA ESTEQUIOMETRIA (vale de QUI-CAL-004 a 009, e para as contas com gases na 013):
- A EQUAÇÃO fica no alto, centrada, com Q.equacao; embaixo de cada substância, linhas de Q.sob_termos, sempre na mesma
  ordem: moléculas → MOL (em COR) → × massa molar (cinza) → MASSA em gramas (tinta). Rótulo de cada linha à esquerda.
- Na primeira vez, as moléculas aparecem de verdade (Q.molecula) embaixo da equação: o coeficiente vira quantidade.
- A RECEITA (proporção simplificada, "1 : 8 : 9") vai numa pílula escura; o fator que dobra tudo é a pílula "× 2" na cor
  da matéria, entre as linhas da tabela (tabela_receita).
- Dado do problema em COR, em cima; xis em COR; resultado na esfera (verde na resposta da questão).
Peça candidata ao kit quimica.py: tabela_receita() (linhas da mesma receita, com o fator entre elas) e gota()."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-004_lei_de_proust_mols.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("mols", "proust", "atalho", "questao", "fim"))
BR = "#FFFFFF"
EQ = "2 H2 + O2 -> 2 H2O"
EQN = "N2 + 3 H2 -> 2 NH3"

# todas as contas da aula
assert Q.lados(EQ)[0] == Q.lados(EQ)[1] and Q.lados(EQN)[0] == Q.lados(EQN)[1]
assert 2 * 2 == 4 and 1 * 32 == 32 and 2 * 18 == 36 and 4 + 32 == 36 and 32 / 4 == 8 and 16 / 2 == 8
assert 40 / 8 == 5 and 5 * 9 == 45 and 28 + 6 == 34 and 56 / 28 == 2 and 2 * 6 == 12 and 2 * 34 == 68


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


def gota(c, cx, cy, r, a=1.0, cor=None):
    """gota de água"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx, cy - r * 1.6)
    p.cubicTo(cx + r * 0.3, cy - r * 0.9, cx + r, cy - r * 0.4, cx + r, cy + r * 0.15)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r * 0.85, 2 * r, 2 * r), 0, 180, False)
    p.cubicTo(cx - r, cy - r * 0.4, cx - r * 0.3, cy - r * 0.9, cx, cy - r * 1.6)
    c.drawPath(p, M.paint(cor or "#7CC8E8", a))
    c.drawCircle(cx - r * 0.35, cy, r * 0.18, M.paint("#FFFFFF", 0.6 * a))


def tabela_receita(c, t, cab, linhas, tl, x, y, dx=360, dy=130, size=80, fator=None):
    """linhas da mesma receita: cab = cabeçalhos; linhas = [(a, b, c)]; tl = instante de cada linha; fator = (texto, instante)
    numa pílula entre as linhas"""
    for j, h in enumerate(cab):
        E.foco(c, t, tl[0] - 0.3, 0.4, lambda a, j=j, h=h: centro(c, h, x + j * dx, y, size * 0.6, "i", TINTA2, a))
    q = ep(t, tl[0] - 0.3, 0.4)
    if q > 0:
        M.line(c, x - dx * 0.45, y + 26, x + (len(cab) - 1) * dx + dx * 0.45, y + 26, TINTA2, 0.7 * q, 3)
    for i, (lin, ti) in enumerate(zip(linhas, tl)):
        yy = y + (i + 1) * dy
        for j, v in enumerate(lin):
            E.foco(c, t, ti + 0.15 * j, 0.4, lambda a, v=v, j=j, yy=yy: E.formula(c, v, x + j * dx, yy, size, "g", TINTA, a, "center"))
        if fator and i > 0:
            pilula_em(c, t, ti, fator, x - dx * 0.75, yy - dy / 2 - size * 0.3, 40, E.COR)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for k, s in enumerate(("rio", "chuva", "geleira")):
            x = 330 + k * 300
            E.foco(c, t, C["s01.a"] + 0.4 * k, 0.5, lambda a, x=x: gota(c, x, 330, 80, a))
            E.foco(c, t, C["s01.a"] + 0.4 * k + 0.2, 0.4, lambda a, x=x, s=s: centro(c, s, x, 470, 54, "i", TINTA2, a))
        Q.molecula(c, t, C["s01.a"] + 0.5, "H2O", 1500, 340, 150, passo=0.15)
        E.frase(c, t, C["s01.b"], ps("em toda a água pura:", "i", 64, TINTA2), XE, 620, passo=0.1)
        Q.atomo_em(c, t, C["s01.b"] + 0.6, XE + 40, 735, 40, "H")
        E.formula_em(c, t, C["s01.b"] + 0.7, "1 g", XE + 110, 770, 110, "g", TINTA)
        E.formula_em(c, t, C["s01.b"] + 1.2, "para", XE + 400, 770, 70, "i", TINTA2)
        Q.atomo_em(c, t, C["s01.b"] + 1.5, XE + 630, 735, 46, "O")
        E.formula_em(c, t, C["s01.b"] + 1.6, "8 g", XE + 700, 770, 110, "g", COR)
        pilula_em(c, t, C["s01.c"], "uma receita fixa: é lei", 1450, 740, 52, TINTA)
        E.frase(c, t, C["s01.c"] + 1.2, ps("a base das contas de reação", "i", 60, TINTA2), XE, 960, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("equação", "g", 70), ("em", "i", 74), ("mols", "g", 70, COR)]),
                 (C["s02.c"], [("lei", "i", 74), ("de", "i", 74), ("Proust", "g", 70, COR)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03.a"] - 0.6, ps("você precisa de", "i", 80) + [("três coisas", "g", 76, COR)], XE, 200, passo=0.12)
    y = [400, 640, 880]
    for i, k in enumerate(("s03.b", "s03.c", "s03.d")):
        E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, XE + 40, y[i] - 30, 44, a=a), centro(c, str(i + 1), XE + 40, y[i] - 8, 54, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, ps("mol e massa molar", "i", 70), XE + 110, y[0])
    Q.formula_em(c, t, C["s03.b"] + 0.6, "H2O", XE + 720, y[0] + 6, 100)
    E.formula_em(c, t, C["s03.b"] + 0.9, "= 18 g/mol", XE + 920, y[0] + 6, 80, "g", COR)
    E.frase(c, t, C["s03.c"] + 0.1, ps("equação balanceada", "i", 70), XE + 110, y[1])
    Q.formula_em(c, t, C["s03.c"] + 0.8, EQ, XE + 720, y[1] + 8, 90, cores={"coef": E.COR})
    E.frase(c, t, C["s03.d"] + 0.1, ps("proporção", "i", 70), XE + 110, y[2])
    E.formula_em(c, t, C["s03.d"] + 0.6, "f{x}{6} = f{4}{3}", XE + 720, y[2] + 10, 76, "g", TINTA)


# ---------------- ler em mols ----------------
EX, EY, ES = W / 2, 270, 120


def b_mols(c, t, C, b):
    t4 = C["s04.a"]
    Q.equacao(c, t, t4, EQ, EX, EY, ES, tl=[t4, t4 + 0.4, t4 + 0.7, t4 + 1.0, t4 + 1.3], cores={"coef": E.COR})
    cs = Q.centros(EQ, EX, EY, ES)

    def moleculas():
        for k, dxk in enumerate((-60, 60)):
            Q.molecula(c, t, C["s04.c"] + 0.2 * k, "H2", cs[0] + dxk * 1.6, 600 + 170 * k, 120, passo=0.1)
        Q.molecula(c, t, C["s04.c"] + 0.6, "O2", cs[1], 680, 120, passo=0.1)
        for k, dxk in enumerate((-70, 70)):
            Q.molecula(c, t, C["s04.d"] + 0.3 * k, "H2O", cs[2] + dxk * 1.6, 600 + 200 * k, 110, passo=0.08)
        Q.sob_termos(c, t, EQ, EX, EY, ES, [["2 moléculas", "1 molécula", "2 moléculas"]], tl=[C["s04.b"]], dy=None, size_l=48)
    E.saida(c, t, C["s05.b"] - 0.1, moleculas)
    if t < C["s05"]:
        return
    E.foco(c, t, C["s05.a"], 0.5, lambda a: E.formula(c, "tudo × 6 × 10^{23}", EX, 900, 80, "g", TINTA2, a, "center"))
    if t >= C["s05.b"]:
        E.frase(c, t, C["s05.b"], ps("os coeficientes contam", "i", 72) + [("mols", "g", 68, COR)], EX, 720, "center", 0.12)
        Q.sob_termos(c, t, EQ, EX, EY, ES, [["2 mol", "1 mol", "2 mol"]], tl=[[C["s05.c"], C["s05.d"], C["s05.e"]]], size_l=84,
                     cores_l=[COR], dy=None)


# ---------------- em gramas ----------------
def b_massas(c, t, C, b):
    EX2 = 1100
    Q.equacao(c, t, C["s06"], EQ, EX2, EY, ES, tl=[C["s06"]] * 5, cores={"coef": E.COR})
    linhas = [["2 mol", "1 mol", "2 mol"], ["× 2 g", "× 32 g", "× 18 g"], ["4 g", "32 g", "36 g"]]
    tl = [[C["s06.a"]] * 3, [C["s06.b"], C["s06.c"], C["s06.d"]], [C["s06.b"] + 1.0, C["s06.c"] + 1.0, C["s06.d"] + 1.0]]
    Q.sob_termos(c, t, EQ, EX2, EY, ES, linhas, tl=tl, size_l=70, dy=130, cores_l=[COR, CINZA, TINTA], rotulos=["mol", "massa molar", "massa"], x_rotulo=470)
    E.formula_em(c, t, C["s07.a"], "4 + 32 = 36", 700, 900, 90, "g", TINTA2, "center")
    E.foco(c, t, C["s07.a"] + 0.6, 0.4, lambda a: E.selo(c, 1040, 870, 44, True, a))
    pilula_em(c, t, C["s07.b"], "a massa se conserva: Lavoisier", 1480, 875, 44, TINTA)


# ---------------- Proust ----------------
def b_proust(c, t, C, b):
    if t < C["s09"]:
        def s08():
            Q.atomo_em(c, t, C["s08.a"], XE + 50, 270, 42, "H")
            E.formula_em(c, t, C["s08.a"], "4 g", XE + 120, 300, 110, "g", TINTA)
            E.formula_em(c, t, C["s08.a"] + 0.5, "para", XE + 420, 300, 70, "i", TINTA2)
            Q.atomo_em(c, t, C["s08.a"] + 0.8, XE + 640, 270, 48, "O")
            E.formula_em(c, t, C["s08.a"] + 0.9, "32 g", XE + 710, 300, 110, "g", TINTA)
            pilula_em(c, t, C["s08.b"], "÷ 4", XE + 280, 400, 46, E.COR)
            pilula_em(c, t, C["s08.b"] + 0.2, "÷ 4", XE + 860, 400, 46, E.COR)
            E.foco(c, t, C["s08.c"], 0.5, lambda a: E.formula(c, "1 : 8", XE + 1250, 320, 170, "g", COR, a))
        s08()
        E.frase(c, t, C["s08.d"], ps("lei de", "i", 90) + [("Proust", "g", 90, COR)], XE, 640, passo=0.12)
        E.frase(c, t, C["s08.e"], ps("numa substância e numa reação,", "i", 62, TINTA2), XE, 760, passo=0.1)
        E.frase(c, t, C["s08.e"] + 1.6, ps("a proporção das massas é", "i", 62, TINTA2) + [("sempre a mesma", "g", 58, COR)], XE, 850, passo=0.1)
        return
    if t < C["s10"]:
        tabela_receita(c, t, ("hidrogênio", "oxigênio", "água"), [("2 g", "16 g", "18 g"), ("4 g", "?", "?")],
                       [C["s09.a"], C["s09.b"]], 760, 300, dx=380, dy=170, size=96)
        pilula_em(c, t, C["s09.c"], "× 2", 760 - 380 * 0.75, 300 + 170 * 1.5 - 30, 44, E.COR)
        if t >= C["s09.d"]:
            E.foco(c, t, C["s09.d"], 0.4, lambda a: (M.rrect(c, 1140 - 120, 640 - 90, 240, 120, 20, "#FFFFFF", a), E.formula(c, "32 g", 1140, 640 + 4, 96, "g", COR, a, "center")))
        if t >= C["s09.e"]:
            E.foco(c, t, C["s09.e"], 0.4, lambda a: (M.rrect(c, 1520 - 120, 640 - 90, 240, 120, 20, "#FFFFFF", a), E.formula(c, "36 g", 1520, 640 + 4, 96, "g", COR, a, "center")))
        E.frase(c, t, C["s09.c"] + 0.4, ps("o hidrogênio dobrou:", "i", 64, TINTA2) + [("tudo dobra", "g", 60, COR)], XE, 820, passo=0.1)
        return
    E.frase(c, t, C["s10.a"], ps("cada linha é a", "i", 72) + [("mesma receita", "g", 68, COR)], XE, 200, passo=0.12)
    tabela_receita(c, t, ("hidrogênio", "oxigênio", "água"), [("1 g", "8 g", "9 g"), ("2 g", "16 g", "18 g"), ("4 g", "32 g", "36 g")],
                   [C["s10.b"], C["s10.c"], C["s10.d"]], 760, 330, dx=380, dy=170, size=92, fator="× 2")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("ler o coeficiente como grama", "i", 70), XE + 450, 190, passo=0.12)
    Q.formula_em(c, t, C["s11.b"], EQ, EX, 420, 120, align="center", cores={"coef": E.COR})

    def errado():
        Q.sob_termos(c, t, EQ, EX, 420, 120, [["2 g", "1 g", ""]], tl=[C["s11.b"] + 1.0], size_l=80, cores_l=[ERRADO])
        if t >= C["s11.c"]:
            pilula_em(c, t, C["s11.c"], "daria 2 : 1", 640, 760, 50, ERRADO)
            E.foco(c, t, C["s11.c"] + 0.8, 0.4, lambda a: (E.escreve(c, "o certo é", 1060, 778, 60, "i", TINTA, a), E.formula(c, "1 : 8", 1360, 778, 80, "g", COR, a)))
    E.saida(c, t, C["s11.d"] + 2.0, errado)
    E.frase(c, t, C["s11.c"] + 1.8, [("coeficiente", "g", 66, COR)] + ps("conta mols", "i", 72), XE, 930, passo=0.12)
    E.frase(c, t, C["s11.d"], [("grama", "g", 66), ("=", "g", 66, TINTA2), ("mol", "g", 66, COR), ("×", "g", 66, TINTA2), ("massa molar", "g", 66)], XE + 900, 930, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"] - 0.3, ps("o atalho:", "i", 72, CLARO) + [("simplifique a receita", "g", 66, BR)], W / 2, 180, "center", 0.12)
        E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "1 : 8 : 9", W / 2, 360, 150, "g", E.CLARO, a, "center"))
        E.foco(c, t, C["s12.b"] + 0.6, 0.4, lambda a: (centro(c, "hidrogênio", W / 2 - 280, 440, 40, "i", CLARO, a), centro(c, "oxigênio", W / 2, 440, 40, "i", CLARO, a), centro(c, "água", W / 2 + 280, 440, 40, "i", CLARO, a)))
        E.frase(c, t, C["s12.c"], ps("divida pelo número dele,", "i", 62, BR) + ps("multiplique pelo do que você quer", "i", 62, CLARO), W / 2, 560, "center", 0.1)
        E.formula_em(c, t, C["s12.d"], "40 g de O", XE, 740, 84, "g", BR)
        E.formula_em(c, t, C["s12.e"], "40 ÷ 8 = 5", XE + 600, 740, 84, "g", BR)
        E.foco(c, t, C["s12.e"] + 0.8, 0.4, lambda a: E.escreve(c, "→ 5 g de H", XE + 1180, 740, 70, "g", E.CLARO, a))
        E.formula_em(c, t, C["s12.f"], "5 × 9 =", XE + 600, 900, 84, "g", BR)
        bola_txt(c, t, C["s12.f"] + 0.6, "45 g", XE + 1040, 870, 84, 56)
        E.foco(c, t, C["s12.f"] + 0.9, 0.4, lambda a: E.escreve(c, "de água", XE + 1150, 900, 60, "i", CLARO, a))
        return
    E.frase(c, t, C["s13.a"], ps("funciona: a", "i", 72, CLARO) + [("proporção", "g", 68, BR)] + ps("não muda", "i", 72, CLARO), W / 2, 300, "center", 0.12)
    E.frase(c, t, C["s13.b"], [("não", "g", 64, ERRADO), ("compensa:", "i", 70, CLARO)] + ps("um reagente sobra", "i", 70, CLARO), W / 2, 500, "center", 0.12)
    pilula_em(c, t, C["s13.c"], "reagente em excesso: outra aula", W / 2, 700, 52, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s14"] + 1.0, ps("a fabricação da amônia", "i", 62, TINTA2), XE, 290, passo=0.1)
    Q.formula_em(c, t, C["s14.a"], EQN, XE, 450, 110, cores={"coef": E.COR})
    E.frase(c, t, C["s14.b"], ps("leia em", "i", 62) + [("mols", "g", 58, COR)], XE, 590, passo=0.1)
    # mini tabela: as massas que reagem e a pergunta
    for j, f in enumerate(("N2", "H2")):
        Q.formula_em(c, t, C["s14.c"], f, XE + 160 + j * 340, 720, 80, align="center")
    E.foco(c, t, C["s14.c"] + 0.3, 0.4, lambda a: (E.formula(c, "28 g", XE + 160, 820, 76, "g", TINTA, a, "center"), E.formula(c, "6 g", XE + 500, 820, 76, "g", TINTA, a, "center"),
                                                  E.escreve(c, "reagem", XE + 720, 815, 56, "i", TINTA2, a)))
    E.foco(c, t, C["s14.d"], 0.4, lambda a: (E.formula(c, "56 g", XE + 160, 940, 76, "g", COR, a, "center"), E.formula(c, "?", XE + 500, 940, 76, "g", COR, a, "center"),
                                             E.escreve(c, "quanto hidrogênio?", XE + 720, 935, 56, "i", TINTA, a)))
    if t < C["s15"]:
        Q.molecula(c, t, C["s14.a"] + 0.5, "NH3", 1560, 560, 140, passo=0.12)
    else:
        E.relogio(c, t, C["s15.a"], cx=1540, cy=470, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    Q.equacao(c, t, C["s16"], EQN, EX, 250, 110, tl=[C["s16"]] * 5, cores={"coef": E.COR})
    Q.sob_termos(c, t, EQN, EX, 250, 110, [["1 mol", "3 mol", "2 mol"], ["28 g", "6 g", "34 g"]],
                 tl=[[C["s16.a"], C["s16.a"] + 0.5, C["s16.b"]], [C["s16.a"] + 1.0, C["s16.a"] + 1.4, C["s16.f"]]], size_l=66, dy=100, cores_l=[COR, TINTA])
    E.formula_em(c, t, C["s16.c"], "56 g = 2 × 28 g", XE, 700, 84, "g", TINTA)
    pilula_em(c, t, C["s16.d"], "× 2 em tudo", XE + 960, 675, 46, E.COR)
    E.formula_em(c, t, C["s16.d"] + 0.6, "hidrogênio: 2 × 6 =", XE, 880, 76, "g", TINTA2)
    bola_txt(c, t, C["s16.e"], "12 g", XE + 860, 852, 86, 56, CERTO)
    E.formula_em(c, t, C["s16.f"] + 0.8, "amônia: 2 × 34 = 68 g", XE + 1040, 880, 60, "g", TINTA2)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s17.a", [("coeficiente", "g", 66), ("=", "g", 66, TINTA2), ("mols", "i", 70)]),
                 ("s17.b", [("massa", "g", 66), ("=", "g", 66, TINTA2), ("coeficiente", "i", 70), ("×", "g", 66, TINTA2), ("massa molar", "i", 70)]),
                 ("s17.c", [("proporção", "g", 66)] + ps("das massas", "i", 70) + [("nunca muda", "g", 66, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s18"] + 0.8, [("massa", "g", 90, COR), ("para", "i", 90), ("massa", "g", 90, COR)], XE, 420, passo=0.12)
    Q.formula_em(c, t, C["s18.a"], "C2H6O + 3 O2 → 2 CO2 + 3 H2O", XE, 620, 70)
    E.frase(c, t, C["s18.a"] + 0.8, [("46 g", "g", 66)] + ps("de etanol", "i", 66) + [("→", "g", 66, TINTA2), ("? g", "g", 66, COR)] + ps("de gás carbônico", "i", 66), XE, 760, passo=0.1)
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s18.b"] + 0.2, 0.4))
    E.frase(c, t, C["s18.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, mols=b_mols, massas=b_massas, proust=b_proust, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
