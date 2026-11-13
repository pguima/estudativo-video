"""Visual — Estudativo · QUI-CAL-007: pureza dos reagentes.

Segue a linguagem da estequiometria (cabeçalho da QUI-CAL-004), a da trilha (QUI-CAL-001) e a da Química (QUI-MIS-001).
A AMOSTRA (amostra) é uma barra cortada em parte pura (cor da matéria, com o nome da substância) e impureza (cinza
pontilhado): só a parte turquesa segue para a equação. O calcário é a pedra cinza (pedra) com pintas de impureza.
No atalho, os dois caminhos (pureza no começo × pureza no fim) correm lado a lado e chegam no mesmo número.
Peças candidatas ao kit quimica.py: amostra() (parte pura × impureza) e pedra()."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-007_pureza_dos_reagentes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pureza", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
EQ = "CaCO3 -> CaO + CO2"
IMP = "#B7B2A8"

# todas as contas da aula
assert Q.lados(EQ)[0] == Q.lados(EQ)[1] and 40 + 12 + 48 == 100 and 40 + 16 == 56 and 12 + 32 == 44
assert 0.8 * 200 == 160 and abs(160 * 56 / 100 - 89.6) < 1e-9 and 200 * 56 / 100 == 112 and abs(0.8 * 112 - 89.6) < 1e-9
assert 0.8 * 250 == 200 and 200 * 44 / 100 == 88 and 250 * 44 / 100 == 110


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


def pedra(c, cx, cy, r, a=1.0, semente=3):
    """pedra de calcário: polígono cinza irregular com pintas de impureza"""
    if a <= 0:
        return
    rnd = random.Random(semente)
    p = skia.Path()
    n = 11
    for k in range(n):
        ang = k / n * math.tau
        rr = r * (0.82 + 0.25 * rnd.random())
        x, y = cx + rr * math.cos(ang), cy + rr * 0.75 * math.sin(ang)
        p.moveTo(x, y) if k == 0 else p.lineTo(x, y)
    p.close()
    c.drawPath(p, M.paint("#CFCBC2", a))
    c.drawPath(p, M.paint("#8E8A82", a, stroke=4))
    for k in range(18):
        ang, d = rnd.random() * math.tau, rnd.random() * r * 0.7
        c.drawCircle(cx + d * math.cos(ang), cy + d * 0.7 * math.sin(ang), 5 + 7 * rnd.random(), M.paint("#8A6E4B" if k % 2 else "#9E9A92", a))


def amostra(c, t, t0, x, y, w, h, pura, rot_p, rot_i, d=1.0, escuro=False):
    """barra da amostra: parte pura (fração pura) na cor da matéria e impureza em cinza"""
    p = ease_out(prog(t, t0, d))
    if p <= 0:
        return
    wp = w * pura
    M.rrect(c, x, y, wp * min(1, p * 1.25), h, 18, E.COR, 1.0)
    if p > 0.8:
        q = (p - 0.8) / 0.2
        M.rrect(c, x + wp + 6, y, (w - wp - 6) * q, h, 18, IMP, 1.0)
    if p >= 1:
        centro(c, rot_p, x + wp / 2, y + h / 2 + 22, 56, "g", BR, 1.0)
        centro(c, rot_i, x + wp + (w - wp) / 2, y + h / 2 + 18, 42, "g", TINTA if not escuro else BR, 1.0)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: pedra(c, 380, 360, 190, a))
        E.foco(c, t, C["s01.a"] + 0.5, 0.4, lambda a: centro(c, "calcário", 380, 560, 56, "i", TINTA2, a))
        p = ep(t, C["s01.a"] + 1.0, 0.6)
        if p > 0:
            M.arrow(c, 640, 360, lerp(640, 920, ease_io(p)), 360, E.COR, 1.0, 8, 26)
            centro(c, "forno", 780, 320, 46, "i", TINTA2, p)
        E.foco(c, t, C["s01.a"] + 1.5, 0.5, lambda a: (c.drawOval(skia.Rect.MakeXYWH(990, 330, 300, 120), M.paint("#FFFFFF", a)),
                                                      c.drawOval(skia.Rect.MakeXYWH(990, 330, 300, 120), M.paint("#C9C9C4", a, stroke=3)),
                                                      centro(c, "cal", 1140, 560, 56, "i", TINTA2, a)))
        E.frase(c, t, C["s01.b"], ps("a conta:", "i", 64, TINTA2) + [("200 g", "g", 64), ("→", "g", 64, TINTA2), ("112 g", "g", 64)] + ps("de cal", "i", 64), XE, 740, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("na fábrica:", "i", 64, TINTA2) + [("menos de 90 g", "g", 64, ERRADO)], XE, 860, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("o que a conta", "i", 72) + [("esqueceu?", "g", 68, COR)], XE, 990, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("descontar", "i", 74), ("a impureza", "g", 70, COR)]),
                 (C["s02.c"], [("quanto", "i", 74), ("produto", "g", 70), ("sai", "i", 74)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 80) + [("duas coisas", "g", 76, COR)], XE, 200, passo=0.12)
    y = [430, 760]
    for i, k in enumerate(("s03.b", "s03.c")):
        E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, XE + 40, y[i] - 30, 44, a=a), centro(c, str(i + 1), XE + 40, y[i] - 8, 54, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, ps("massa para massa numa equação", "i", 66), XE + 110, y[0])
    E.frase(c, t, C["s03.c"] + 0.1, ps("porcentagem pelo decimal", "i", 66), XE + 110, y[1])
    E.formula_em(c, t, C["s03.c"] + 1.4, "37% de 240 = 0,37 × 240", XE + 110, y[1] + 130, 80, "g", TINTA)


# ---------------- pureza ----------------
def b_pureza(c, t, C, b):
    if t < C["s05"]:
        E.foco(c, t, C["s04.a"], 0.5, lambda a: pedra(c, 1420, 470, 300, a))
        E.frase(c, t, C["s04.a"], ps("o calcário é uma", "i", 76) + [("rocha", "g", 70)], XE, 220, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("o que interessa:", "i", 64, TINTA2), XE, 360, passo=0.1)
        Q.formula_em(c, t, C["s04.b"] + 0.6, "CaCO3", XE, 500, 130, cores={"indice": E.COR})
        E.foco(c, t, C["s04.b"] + 1.0, 0.4, lambda a: E.escreve(c, "carbonato de cálcio", XE, 580, 54, "i", TINTA2, a))
        E.frase(c, t, C["s04.c"], ps("o resto:", "i", 64, TINTA2) + [("areia, argila...", "g", 58)], XE, 720, passo=0.1)
        E.frase(c, t, C["s04.d"], [("pureza", "g", 76, COR), ("=", "g", 76, TINTA2)] + ps("% que reage", "i", 80), XE, 900, passo=0.12)
        return
    E.frase(c, t, C["s05.a"], [("80%", "g", 120, COR)] + ps("de pureza", "i", 90), XE, 300, passo=0.12)
    amostra(c, t, C["s05.b"], XE, 470, 1580, 160, 0.8, "80 g de carbonato", "20 g", d=1.2)
    E.foco(c, t, C["s05.b"] + 0.5, 0.4, lambda a: E.escreve(c, "em cada 100 g", XE, 720, 56, "i", TINTA2, a))
    E.foco(c, t, C["s05.c"], 0.4, lambda a: (centro(c, "não reagem", XE + 1580 * 0.9, 720, 50, "g", TINTA2, a)))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    Q.equacao(c, t, C["s06.a"], EQ, W / 2, 250, 110, tl=[C["s06.a"] + 0.3 * k for k in range(5)])
    E.foco(c, t, C["s06.a"] + 1.2, 0.4, lambda a: centro(c, "no forno", W / 2 - 60, 170, 44, "i", TINTA2, a))
    Q.sob_termos(c, t, EQ, W / 2, 250, 110, [["100 g", "56 g", ""]], tl=[[C["s06.c"], C["s06.d"], 0]], size_l=70)
    cs = Q.centros(EQ, W / 2, 250, 110)
    E.foco(c, t, C["s06.d"] + 0.4, 0.4, lambda a: centro(c, "a cal", cs[1], 480, 44, "i", TINTA2, a))
    if t < C["s07"]:
        return
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], [("1", "g", 60, COR)] + ps("tire a impureza", "i", 66), XE, 600, passo=0.12)
        amostra(c, t, C["s07.a"] + 0.4, XE, 650, 1580, 120, 0.8, "160 g puro", "40 g")
        E.formula_em(c, t, C["s07.b"], "80% = 0,8", XE, 900, 76, "g", TINTA2)
        E.formula_em(c, t, C["s07.c"], "0,8 × 200 = 160 g", XE + 600, 900, 84, "g", TINTA)
        return
    E.frase(c, t, C["s08.a"], [("2", "g", 60, COR)] + ps("regra de três só com a parte pura", "i", 66), XE, 590, passo=0.1)
    Q.regra_tres(c, t, C["s08.b"] - 0.3, ("carbonato", "cal"), [("100 g", "56 g"), ("160 g", "x")], 520, 680, 70,
                 tl=[C["s08.b"], C["s08.c"]], dx=420)
    E.formula_em(c, t, C["s08.d"], "x = f{160 × 56}{100}", 1080, 860, 74, "g", TINTA)
    bola_txt(c, t, C["s08.e"], "89,6 g", 1690, 840, 110, 60)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s09"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s09.a"], ps("esquecer a pureza", "i", 72), XE + 450, 190, passo=0.12)
    E.foco(c, t, C["s09.a"] + 0.4, 0.5, lambda a: pedra(c, 1500, 330, 180, a))
    E.formula_em(c, t, C["s09.a"] + 0.8, "200 g inteiros", XE, 400, 84, "g", TINTA)
    E.formula_em(c, t, C["s09.b"], "200 × f{56}{100} = 112 g", XE, 600, 90, "g", ERRADO)
    if t >= C["s09.c"]:
        E.risco(c, XE - 10, 640, XE + 1000, 540, t, C["s09.c"], largura=12)
        pilula_em(c, t, C["s09.c"] + 0.3, "mais cal do que a pedra dá", 1450, 600, 46, ERRADO)
    E.frase(c, t, C["s09.d"], ps("a impureza", "i", 76) + [("pesa", "g", 70)] + ps("mas", "i", 76) + [("não reage", "g", 70, COR)], XE, 860, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("o atalho: a pureza entra", "i", 70, CLARO) + [("no começo ou no fim", "g", 66, BR)], W / 2, 180, "center", 0.1)
        # caminho de cima: pureza no começo
        E.foco(c, t, C["s10.a"] + 1.0, 0.4, lambda a: E.escreve(c, "no começo", XE, 380, 54, "i", CLARO, a))
        E.formula_em(c, t, C["s10.a"] + 1.4, "200 g  → × 0,8 →  160 g  →  89,6 g", 560, 380, 70, "g", BR)
        # caminho de baixo: pureza no fim
        E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "no fim", XE, 600, 54, "i", CLARO, a))
        E.formula_em(c, t, C["s10.b"] + 0.3, "200 g  →  112 g", 560, 600, 70, "g", BR)
        E.formula_em(c, t, C["s10.c"], "→ × 0,8 →", 1130, 600, 70, "g", E.CLARO)
        E.formula_em(c, t, C["s10.d"], "89,6 g", 1530, 600, 70, "g", BR)
        if t >= C["s10.d"] + 0.5:
            q = ep(t, C["s10.d"] + 0.5, 0.4)
            for yy in (380, 600):
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1500, yy - 70, 290, 100), 30, 30), M.paint(E.CLARO, q, stroke=5))
            centro(c, "o mesmo resultado", W / 2, 800, 60, "g", E.CLARO, q)
        return
    E.frase(c, t, C["s11.a"], ps("tudo é", "i", 72, CLARO) + [("proporcional", "g", 68, BR)], W / 2, 260, "center", 0.12)
    E.frase(c, t, C["s11.a"] + 1.4, ps("−20% no reagente = −20% no produto", "i", 60, CLARO), W / 2, 360, "center", 0.1)
    E.frase(c, t, C["s11.b"], ps("escolha a conta", "i", 66, CLARO) + [("mais redonda", "g", 62, BR)], W / 2, 520, "center", 0.12)
    E.frase(c, t, C["s11.c"], [("não", "g", 60, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("tem limitante? tire a impureza primeiro", "i", 64, CLARO), W / 2, 720, "center", 0.1)
    pilula_em(c, t, C["s11.c"] + 2.6, "nunca aplique a pureza duas vezes", W / 2, 880, 50, ERRADO)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s12"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s12.a"], [("250 g", "g", 66)] + ps("de calcário com", "i", 70) + [("80%", "g", 66, COR)] + ps("de pureza", "i", 70), XE, 330, passo=0.1)
    Q.formula_em(c, t, C["s12.b"], EQ, XE, 520, 96)
    cs = Q.centros(EQ, XE, 520, 96, "left")
    E.foco(c, t, C["s12.b"] + 0.6, 0.4, lambda a: (E.formula(c, "100 g", cs[0], 620, 60, "b", TINTA, a, "center"), E.formula(c, "44 g", cs[2], 620, 60, "b", COR, a, "center")))
    E.frase(c, t, C["s12.c"], ps("quantos gramas de", "i", 66) + [("gás carbônico?", "g", 62, COR)], XE, 800, passo=0.1)
    if t < C["s13"]:
        E.foco(c, t, C["s12.a"] + 0.5, 0.5, lambda a: pedra(c, 1560, 330, 170, a))
    else:
        E.relogio(c, t, C["s13.a"], cx=1560, cy=470, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s14.a"], [("1", "g", 60, COR)] + ps("a parte pura", "i", 66), XE, 220, passo=0.12)
    amostra(c, t, C["s14.a"] + 0.3, XE, 270, 1000, 110, 0.8, "200 g", "50 g")
    E.formula_em(c, t, C["s14.a"] + 1.4, "0,8 × 250 = 200 g", 1240, 350, 58, "g", TINTA)
    E.frase(c, t, C["s14.b"], [("2", "g", 60, COR), ("100 g", "g", 64)] + ps("dão", "i", 68) + [("44 g", "g", 64)], XE, 540, passo=0.12)
    E.frase(c, t, C["s14.c"], [("200 g", "g", 64, COR)] + ps("é o dobro", "i", 68), XE, 660, passo=0.12)
    bola_txt(c, t, C["s14.d"], "88 g", 1300, 610, 100, 64, CERTO)
    E.foco(c, t, C["s14.d"] + 0.4, 0.4, lambda a: E.escreve(c, "de gás carbônico", 1430, 625, 50, "i", TINTA2, a))

    def erro():
        E.foco(c, t, C["s14.e"], 0.5, lambda a: (E.formula(c, "250 × f{44}{100} = 110 g", XE, 900, 66, "g", ERRADO, a),
                                                 E.escreve(c, "sem a pureza", XE + 880, 895, 52, "i", ERRADO, a)))
        if t >= C["s14.e"] + 0.7:
            E.risco(c, XE - 10, 930, XE + 800, 850, t, C["s14.e"] + 0.7, largura=9)
    if t >= C["s14.e"]:
        erro()


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s15"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s15.a", [("só a parte pura", "g", 66, COR)] + ps("reage", "i", 70)),
                 ("s15.b", [("amostra", "g", 66), ("×", "g", 66, TINTA2), ("pureza", "g", 66)] + ps("em decimal", "i", 70)),
                 ("s15.c", ps("estequiometria com a", "i", 70) + [("parte pura", "g", 66)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s16"] - 0.1, resumo)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s16.a"], [("rendimento", "g", 100, COR)], XE, 430)
    E.frase(c, t, C["s16.b"], ps("reações em", "i", 80) + [("etapas", "g", 76)] + ps("numa conta só", "i", 80), XE, 600, passo=0.12)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 780, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s16.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 805, p), ep(t, C["s16.c"] + 0.2, 0.4))
    E.frase(c, t, C["s16.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pureza=b_pureza, exemplo=b_exemplo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
