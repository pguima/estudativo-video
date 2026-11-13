"""Visual — Estudativo · QUI-CAL-006: reagente limitante e excesso.

Segue a linguagem da estequiometria (cabeçalho da QUI-CAL-004), a da trilha (QUI-CAL-001) e a da Química (QUI-MIS-001).
O que se TEM fica em cima da equação (linha_cima, em COR); a massa da equação embaixo (Q.sob_termos). O MEDIDOR (medidor) mostra
quanto há de um reagente (contorno) e quanto a reação gasta (cheio): o que fica de fora é a sobra, em cinza listrado.
LIMITANTE leva a pílula turquesa; EXCESSO, a pílula cinza. Receitas contadas = pacotes (QUI-CAL-002), meia receita = meio pacote.
Peças candidatas ao kit quimica.py: medidor() (tem × gasta × sobra) e sanduiche() (a analogia do limitante)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-006_reagente_limitante.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("conceito", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
EQ = "2 H2 + O2 -> 2 H2O"
EQN = "N2 + 3 H2 -> 2 NH3"
EX, EY, ES = W / 2, 400, 120
PAO, QUEIJO = "#D9A35B", "#F6C945"

# todas as contas da aula
assert Q.lados(EQ)[0] == Q.lados(EQ)[1] and Q.lados(EQN)[0] == Q.lados(EQN)[1]
assert 64 / 32 * 4 == 8 and 10 - 8 == 2 and 64 / 32 * 36 == 72 == 8 + 64 and 10 / 4 * 36 == 90 and 10 + 64 == 74
assert 10 / 4 == 2.5 and 64 / 32 == 2 and 28 / 28 == 1 and 9 / 6 == 1.5 and 9 - 6 == 3
assert min(10 // 2, 3) == 3 and 10 - 2 * 3 == 4


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


def fatia(c, x, y, w, h, cor, a=1.0):
    M.rrect(c, x, y, w, h, h * 0.45, cor, a, shadow=True)


def sanduiche(c, cx, cy, k=1.0, a=1.0):
    """pão, queijo e pão empilhados"""
    fatia(c, cx - 70 * k, cy + 18 * k, 140 * k, 34 * k, PAO, a)
    fatia(c, cx - 76 * k, cy - 6 * k, 152 * k, 20 * k, QUEIJO, a)
    fatia(c, cx - 70 * k, cy - 40 * k, 140 * k, 34 * k, PAO, a)


def medidor(c, t, t0, x, y, w, h, tem, usa, rot_tem, rot_usa, tu=None, cor=None):
    """barra do que se tem (contorno) com o que a reação gasta (cheio); o resto é a sobra listrada"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    M.rrect(c, x, y, w, h, 18, "#E6E6E2", q)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), M.paint(TINTA2, q, stroke=3))
    centro(c, rot_tem, x + w / 2, y - 24, 46, "g", TINTA, q)
    tu = tu if tu is not None else t0 + 0.6
    p = ease_out(prog(t, tu, 0.8))
    if p > 0:
        wu = w * usa / tem * p
        M.rrect(c, x, y, wu, h, 18, cor or E.COR, 1.0)
        if p >= 1:
            centro(c, rot_usa, x + wu / 2, y + h / 2 + 20, 52, "g", BR, 1.0)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("1 sanduíche", "g", 64, COR), ("=", "g", 64, TINTA2), ("2 pães", "g", 64), ("+", "g", 64, TINTA2), ("1 queijo", "g", 64)], XE, 200, passo=0.12)
        feitos = 0 if t < C["s01.d"] else min(3, int((t - C["s01.d"]) / 0.4) + 1)
        for i in range(10):
            if i < 2 * feitos:
                continue
            E.foco(c, t, C["s01.b"] + 0.08 * i, 0.3, lambda a, i=i: fatia(c, XE + i * 140, 360, 120, 40, PAO, a))
        for j in range(3):
            if j < feitos:
                continue
            E.foco(c, t, C["s01.b"] + 1.0 + 0.1 * j, 0.3, lambda a, j=j: fatia(c, XE + j * 175, 470, 152, 24, QUEIJO, a))
        E.foco(c, t, C["s01.b"] + 0.4, 0.4, lambda a: (E.escreve(c, "10 pães", 1640, 390, 50, "g", TINTA, a), E.escreve(c, "3 queijos", 1640, 490, 50, "g", TINTA, a)))
        E.frase(c, t, C["s01.c"], ps("quantos sanduíches?", "i", 70), XE, 650, passo=0.12)
        for k in range(feitos):
            E.foco(c, t, C["s01.d"] + 0.4 * k, 0.4, lambda a, k=k: sanduiche(c, XE + 120 + k * 240, 820, 1.0, a))
        if t >= C["s01.d"]:
            bola_txt(c, t, C["s01.d"] + 1.2, "3", 960, 820, 70, 84)
        E.foco(c, t, C["s01.e"], 0.4, lambda a: (E.escreve(c, "o queijo acaba primeiro:", 1120, 800, 50, "i", TINTA2, a), E.escreve(c, "sobram 4 pães", 1120, 880, 58, "g", COR, a)))
        E.frase(c, t, C["s01.f"], ps("numa reação, é a mesma coisa", "i", 60, TINTA2), XE, 1010, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("quem", "i", 74), ("limita", "g", 70, COR)]),
                 (C["s02.c"], [("quanto", "i", 74), ("sobra", "g", 70)]),
                 (C["s02.d"], [("quanto", "i", 74), ("produto", "g", 70)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 80) + [("uma coisa", "g", 76, COR)], XE, 220, passo=0.12)
    E.frase(c, t, C["s03.b"], ps("a conta de massa para massa", "i", 70), XE, 380, passo=0.1)
    Q.formula_em(c, t, C["s03.b"] + 0.8, EQ, EX, 600, 120, align="center", cores={"coef": E.COR})
    Q.sob_termos(c, t, EQ, EX, 600, 120, [["4 g", "32 g", "36 g"]], tl=[C["s03.b"] + 1.4], size_l=80)


# ---------------- conceito ----------------
def b_conceito(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("reagente", "g", 100), ("limitante", "g", 100, COR)], XE, 300, passo=0.12)
    E.frase(c, t, C["s04.a"] + 1.2, ps("acaba primeiro e faz a reação parar", "i", 64, TINTA2), XE, 410, passo=0.1)
    E.frase(c, t, C["s04.b"], [("excesso", "g", 90, TINTA)], XE, 600)
    E.frase(c, t, C["s04.b"] + 0.8, ps("parte dele sobra, sem reagir", "i", 64, TINTA2), XE, 700, passo=0.1)
    E.frase(c, t, C["s04.c"], ps("o produto sai", "i", 70) + [("pelo limitante", "g", 66, COR)], XE, 900, passo=0.12)
    for k in range(3):
        E.foco(c, t, C["s04.a"] + 0.6 + 0.3 * k, 0.4, lambda a, k=k: sanduiche(c, 1480 + (k - 1) * 220, 340, 0.9, a))
    for k in range(2):
        E.foco(c, t, C["s04.b"] + 0.4 + 0.2 * k, 0.4, lambda a, k=k: fatia(c, 1400 + k * 180, 640, 140, 40, PAO, a))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    t5 = C["s05.b"]
    Q.equacao(c, t, t5, EQ, EX, EY, ES, tl=[t5, t5 + 0.3, t5 + 0.6, t5 + 0.9, t5 + 1.2], cores={"coef": E.COR})
    E.foco(c, t, C["s05.a"], 0.4, lambda a: E.escreve(c, "tenho:", 140, EY - 130, 50, "i", TINTA2, a))
    cs = Q.centros(EQ, EX, EY, ES)
    for cx, v, tk in ((cs[0], "10 g", C["s05.a"]), (cs[1], "64 g", C["s05.a"] + 0.8)):
        E.foco(c, t, tk, 0.4, lambda a, cx=cx, v=v: E.formula(c, v, cx, EY - 130, 80, "g", COR, a, "center"))
    Q.sob_termos(c, t, EQ, EX, EY, ES, [["4 g", "32 g", "36 g"]], tl=[[C["s05.c"], C["s05.d"], C["s05.e"]]], size_l=70)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.escreve(c, "equação:", 140, EY + 150, 50, "i", TINTA2, a))
    if t < C["s06"]:
        return
    if t < C["s08"]:
        E.frase(c, t, C["s06.a"], ps("teste o", "i", 66) + [("oxigênio", "g", 62, COR)], XE, 660, passo=0.12)
        E.foco(c, t, C["s06.b"], 0.4, lambda a: (E.formula(c, "32 g", XE, 760, 64, "g", TINTA, a), E.escreve(c, "pedem", XE + 190, 758, 56, "i", TINTA2, a), E.formula(c, "4 g", XE + 390, 760, 64, "g", TINTA, a)))
        E.foco(c, t, C["s06.c"], 0.4, lambda a: (E.formula(c, "64 g", XE, 850, 64, "g", COR, a), E.escreve(c, "pedem", XE + 190, 848, 56, "i", TINTA2, a), E.formula(c, "8 g", XE + 390, 850, 64, "g", COR, a)))
        medidor(c, t, C["s06.d"], 1000, 760, 760, 100, 10, 8, "tenho 10 g de hidrogênio", "gasta 8 g", tu=C["s06.d"] + 0.6)
        E.foco(c, t, C["s06.e"], 0.4, lambda a: centro(c, "dá e sobra", 1700, 930, 52, "i", COR, a))
        if t >= C["s07"]:
            pilula_em(c, t, C["s07.b"], "limitante", cs[1], EY - 250, 46, E.COR)
            pilula_em(c, t, C["s07.c"], "excesso", cs[0], EY - 250, 46, "#5A5F66")
            E.formula_em(c, t, C["s07.d"], "10 − 8 = 2 g", XE, 990, 76, "g", TINTA)
            E.foco(c, t, C["s07.d"] + 0.5, 0.4, lambda a: E.escreve(c, "de hidrogênio sobram", XE + 470, 986, 54, "i", TINTA2, a))
        return
    pilula_em(c, t, C["s08"], "limitante", cs[1], EY - 250, 46, E.COR)
    pilula_em(c, t, C["s08"], "excesso", cs[0], EY - 250, 46, "#5A5F66")
    E.frase(c, t, C["s08.a"], ps("a água sai", "i", 66) + [("pelo limitante", "g", 62, COR)], XE, 670, passo=0.12)
    E.foco(c, t, C["s08.b"], 0.4, lambda a: (E.formula(c, "32 g de oxigênio", XE, 790, 64, "g", TINTA, a), E.escreve(c, "dão", XE + 560, 788, 56, "i", TINTA2, a), E.formula(c, "36 g de água", XE + 700, 790, 64, "g", TINTA, a)))
    E.foco(c, t, C["s08.c"], 0.4, lambda a: (E.formula(c, "64 g", XE, 920, 64, "g", COR, a), E.escreve(c, "o dobro:", XE + 190, 918, 56, "i", TINTA2, a)))
    bola_txt(c, t, C["s08.d"], "72 g", XE + 640, 895, 84, 56)
    E.formula_em(c, t, C["s08.e"], "8 + 64 = 72", 1300, 920, 72, "g", TINTA2)
    E.foco(c, t, C["s08.e"] + 0.6, 0.4, lambda a: E.selo(c, 1760, 895, 40, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s09"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s09.a"], ps("limitante = o de menor massa?", "i", 72), XE + 450, 190, passo=0.12)
    E.foco(c, t, C["s09.b"], 0.4, lambda a: (E.formula(c, "10 g", XE + 200, 400, 110, "g", TINTA, a, "center"), E.formula(c, "64 g", XE + 760, 400, 110, "g", TINTA, a, "center")))
    Q.formula_em(c, t, C["s09.b"], "H2", XE + 200, 520, 80, align="center")
    Q.formula_em(c, t, C["s09.b"], "O2", XE + 760, 520, 80, align="center")
    E.foco(c, t, C["s09.b"] + 0.4, 0.4, lambda a: E.formula(c, "<", XE + 480, 400, 110, "g", TINTA2, a, "center"))

    def errado():
        E.foco(c, t, C["s09.c"] - 0.8, 0.4, lambda a: E.escreve(c, "água pelo hidrogênio:", 1150, 380, 52, "i", ERRADO, a))
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.formula(c, "90 g", 1150, 500, 110, "g", ERRADO, a))
        E.foco(c, t, C["s09.c"] + 0.8, 0.4, lambda a: E.escreve(c, "mais que os 74 g que entraram", 1150, 590, 46, "i", ERRADO, a))
        if t >= C["s09.c"] + 1.6:
            E.risco(c, 1130, 520, 1420, 420, t, C["s09.c"] + 1.6, largura=11)
    errado()
    E.frase(c, t, C["s09.d"], ps("quem decide é a", "i", 76) + [("proporção da equação", "g", 70, COR)], XE, 800, passo=0.12)
    E.frase(c, t, C["s09.d"] + 1.4, ps("não a massa sozinha", "i", 66, TINTA2), XE, 900, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"] - 0.3, ps("o atalho:", "i", 72, CLARO) + [("tenho ÷ equação", "g", 68, BR)], W / 2, 180, "center", 0.12)
        for k, (f, conta_, tk) in enumerate((("H2", "10 ÷ 4 = 2,5", "s10.b"), ("O2", "64 ÷ 32 = 2", "s10.c"))):
            x = 560 + 800 * k
            Q.formula_em(c, t, C[tk], f, x, 430, 130, align="center", escuro=True)
            E.formula_em(c, t, C[tk] + 0.4, conta_, x, 620, 96, "g", BR, "center")
        if t >= C["s10.d"]:
            q = ep(t, C["s10.d"], 0.4)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(1360 - 320, 300, 1360 + 320, 700), 40, 40), M.paint(E.CLARO, q, stroke=7))
            pilula_em(c, t, C["s10.d"] + 0.3, "menor = limitante", 1360, 880, 52, E.COR)
        return
    E.frase(c, t, C["s11.a"], ps("cada divisão conta quantas", "i", 66, CLARO) + [("receitas", "g", 62, BR)] + ps("cabem", "i", 66, CLARO), W / 2, 200, "center", 0.12)
    for k, (f, n, tk) in enumerate((("O2", 2.0, "s11.b"), ("H2", 2.5, "s11.b"))):
        y = 360 + 200 * k
        Q.formula_em(c, t, C[tk] + 0.8 * k, f, XE + 60, y + 70, 90, escuro=True)
        for j in range(3):
            frac = min(1.0, n - j)
            if frac <= 0:
                continue
            q = ease_back(prog(t, C[tk] + 0.8 * k + 0.3 * j, 0.4))
            if q > 0:
                M.rrect(c, XE + 300 + j * 300, y, 280 * frac, 110 * q, 18, E.COR, 1.0)
                if frac == 1:
                    centro(c, "receita", XE + 440 + j * 300, y + 70, 44, "g", BR, min(1, q))
        E.foco(c, t, C[tk] + 0.8 * k + 1.0, 0.4, lambda a, n=n, y=y: E.formula(c, str(n).replace(".", ",").replace(",0", ""), 1500, y + 80, 90, "g", E.CLARO, a))
    E.foco(c, t, C["s11.c"], 0.4, lambda a: centro(c, "a reação termina em 2", W / 2, 880, 60, "g", BR, a))
    E.frase(c, t, C["s11.d"], [("não", "g", 58, ERRADO), ("compensa:", "i", 62, CLARO)] + ps("a prova já disse quem sobra", "i", 62, CLARO), W / 2, 1000, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s12"], ps("hora de testar", "i", 72, COR), XE, 180)
    Q.equacao(c, t, C["s12.a"], EQN, EX, 400, 110, tl=[C["s12.a"]] * 5, cores={"coef": E.COR})
    Q.sob_termos(c, t, EQN, EX, 400, 110, [["28 g", "6 g", "34 g"]], tl=[C["s12.b"]], size_l=66)
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.escreve(c, "equação:", 140, 520, 46, "i", TINTA2, a))
    cs = Q.centros(EQN, EX, 400, 110)
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.escreve(c, "tenho:", 140, 290, 46, "i", TINTA2, a))
    for cx, v, k in ((cs[0], "28 g", 0), (cs[1], "9 g", 1)):
        E.foco(c, t, C["s12.c"] + 0.4 * k, 0.4, lambda a, cx=cx, v=v: E.formula(c, v, cx, 290, 72, "g", COR, a, "center"))
    E.frase(c, t, C["s12.d"], ps("quem limita?", "i", 64) + [("quanto sobra?", "g", 60)] + ps("quanta amônia?", "i", 64), XE, 760, passo=0.12)
    if t >= C["s13"]:
        E.relogio(c, t, C["s13.a"], cx=1600, cy=720, r=140)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    Q.equacao(c, t, C["s14"], EQN, EX, 330, 110, tl=[C["s14"]] * 5, cores={"coef": E.COR})
    Q.sob_termos(c, t, EQN, EX, 330, 110, [["28 g", "6 g", "34 g"]], tl=[C["s14"]], size_l=60)
    cs = Q.centros(EQN, EX, 330, 110)
    for cx, v in ((cs[0], "28 g"), (cs[1], "9 g")):
        E.foco(c, t, C["s14"] + 0.3, 0.4, lambda a, cx=cx, v=v: E.formula(c, v, cx, 220, 66, "g", COR, a, "center"))
    E.formula_em(c, t, C["s14.a"], "28 ÷ 28 = 1", 560, 640, 84, "g", TINTA, "center")
    E.formula_em(c, t, C["s14.b"], "9 ÷ 6 = 1,5", 1360, 640, 84, "g", TINTA, "center")
    pilula_em(c, t, C["s14.c"], "limitante", 560, 740, 46, E.COR)
    pilula_em(c, t, C["s14.c"] + 0.3, "excesso", 1360, 740, 46, "#5A5F66")
    E.formula_em(c, t, C["s14.e"], "9 − 6 = 3 g", 1360, 890, 76, "g", TINTA2, "center")
    E.foco(c, t, C["s14.e"] + 0.5, 0.4, lambda a: centro(c, "de hidrogênio sobram", 1360, 960, 44, "i", TINTA2, a))
    bola_txt(c, t, C["s14.f"], "34 g", 560, 900, 84, 56, CERTO)
    E.foco(c, t, C["s14.f"] + 0.4, 0.4, lambda a: centro(c, "de amônia", 560, 1030, 44, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s15"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s15.a", [("tenho", "g", 66), ("÷", "g", 66, TINTA2), ("massa da equação", "g", 66)]),
                 ("s15.b", [("o menor", "g", 66), ("=", "g", 66, TINTA2), ("limitante", "g", 66, COR)]),
                 ("s15.c", [("o produto", "i", 70)] + ps("se calcula por ele", "i", 70)))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s16"] - 0.1, resumo)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s16.a"], ps("reagente", "i", 80) + [("com impurezas", "g", 76, COR)], XE, 420, passo=0.12)
    E.frase(c, t, C["s16.b"], ps("descontar a parte que", "i", 70) + [("não reage", "g", 66)], XE, 580, passo=0.12)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 780, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s16.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 805, p), ep(t, C["s16.c"] + 0.2, 0.4))
    E.frase(c, t, C["s16.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, conceito=b_conceito, exemplo=b_exemplo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
