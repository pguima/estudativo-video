"""Visual — Estudativo · QUI-CAL-008: rendimento e reações em etapas.

Segue a linguagem da estequiometria (cabeçalho da QUI-CAL-004), a da trilha (QUI-CAL-001) e a da Química (QUI-MIS-001).
RENDIMENTO = barra do máximo (contorno, rendimento teórico) com a parte que sai de verdade cheia na cor da matéria (barra_rend);
a parte perdida fica vazia, nunca em vermelho (vermelho é só o erro). REAÇÕES EM ETAPAS: as equações empilhadas; o átomo que
passa por todas (o enxofre, amarelo CPK) salta de uma para a outra (salto_atomo) e ganha um anel na cor da matéria.
Peças candidatas ao kit quimica.py: barra_rend() e salto_atomo()."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-008_rendimento_e_etapas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("rendimento", "etapas", "atalho", "questao", "fim"))
BR = "#FFFFFF"
EQS = ("S + O2 -> SO2", "2 SO2 + O2 -> 2 SO3", "SO3 + H2O -> H2SO4")

# todas as contas da aula
for e in EQS:
    assert Q.lados(e)[0] == Q.lados(e)[1], e
assert 2 + 32 + 64 == 98 and 64 / 32 * 98 == 196 and 0.75 * 196 == 147 and 0.25 * 196 == 49
assert 16 / 32 * 98 == 49 and abs(0.8 * 49 - 39.2) < 1e-9


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


def barra_rend(c, t, t0, x, y, w, h, frac, rot_max, rot_real, tr=None):
    """rendimento: o máximo em contorno e a parte que sai de verdade cheia"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 20, 20), M.paint(TINTA2, q, stroke=4, ))
    centro(c, rot_max, x + w / 2, y - 26, 48, "g", TINTA2, q)
    tr = tr if tr is not None else t0 + 0.6
    p = ease_out(prog(t, tr, 0.9))
    if p > 0:
        M.rrect(c, x + 6, y + 6, (w * frac - 12) * p, h - 12, 16, E.COR, 1.0)
        if p >= 1:
            centro(c, rot_real, x + w * frac / 2, y + h / 2 + 20, 54, "g", BR, 1.0)
            centro(c, "perdido", x + w * frac + w * (1 - frac) / 2, y + h / 2 + 16, 42, "i", TINTA2, 1.0)


def salto_atomo(c, t, pts, tl, r=34):
    """o átomo amarelo salta de ponto em ponto (tl = instante de cada chegada) e deixa um anel em cada parada"""
    if t < tl[0]:
        return
    k = max(i for i, ti in enumerate(tl) if t >= ti)
    for i in range(k + 1):
        q = ep(t, tl[i], 0.3)
        c.drawCircle(pts[i][0], pts[i][1], r + 26, M.paint(E.COR, q, stroke=6))
    if k + 1 < len(pts):
        p = ease_io(prog(t, tl[k] + 0.2, max(0.3, tl[k + 1] - tl[k] - 0.4)))
        x = lerp(pts[k][0], pts[k + 1][0], p)
        y = lerp(pts[k][1], pts[k + 1][1], p) - math.sin(p * math.pi) * 90
    else:
        x, y = pts[k]
    Q.atomo(c, x, y, r, "S")


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("a fábrica faz a conta:", "i", 66, TINTA2), XE, 220, passo=0.1)
        Q.atomo_em(c, t, C["s01.b"], XE + 50, 340, 46, "S")
        E.formula_em(c, t, C["s01.b"], "64 g", XE + 130, 370, 100, "g", TINTA)
        p = ep(t, C["s01.b"] + 0.6, 0.5)
        if p > 0:
            M.arrow(c, XE + 420, 340, lerp(XE + 420, XE + 640, ease_io(p)), 340, E.COR, 1.0, 7, 24)
        Q.formula_em(c, t, C["s01.b"] + 0.9, "H2SO4", XE + 700, 370, 100)
        barra_rend(c, t, C["s01.b"] + 1.4, XE, 560, 1580, 140, 0.75, "deveriam sair 196 g", "saem 147 g", tr=C["s01.c"])
        E.frase(c, t, C["s01.d"], ps("para onde foi o resto?", "i", 70), XE, 860, passo=0.12)
        E.frase(c, t, C["s01.e"], ps("e", "i", 66, TINTA2) + [("três reações", "g", 62, COR)] + ps("numa conta só?", "i", 66, TINTA2), XE, 980, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("corrigir", "i", 74), ("pelo", "i", 74), ("rendimento", "g", 70, COR)]),
                 (C["s02.c"], [("reações", "g", 70), ("em", "i", 74), ("etapas", "g", 70, COR)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 80) + [("duas coisas", "g", 76, COR)], XE, 200, passo=0.12)
    y = [430, 760]
    for i, k in enumerate(("s03.b", "s03.c")):
        E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, XE + 40, y[i] - 30, 44, a=a), centro(c, str(i + 1), XE + 40, y[i] - 8, 54, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, ps("massa para massa numa equação", "i", 66), XE + 110, y[0])
    E.frase(c, t, C["s03.c"] + 0.1, ps("porcentagem pelo decimal", "i", 66), XE + 110, y[1])
    E.formula_em(c, t, C["s03.c"] + 1.2, "75% de 196 = 0,75 × 196", XE + 110, y[1] + 130, 80, "g", TINTA)


# ---------------- rendimento ----------------
def b_rendimento(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("nenhuma reação de fábrica dá", "i", 70) + [("tudo", "g", 66, COR)], XE, 220, passo=0.12)
        for k, (s, tk) in enumerate((("fica sem reagir", C["s04.b"]), ("vira outra coisa", C["s04.b"] + 1.0), ("se perde no caminho", C["s04.b"] + 1.9))):
            pilula_em(c, t, tk, s, XE + 230 + k * 520, 400, 46, "#5A5F66")
        E.frase(c, t, C["s04.c"], [("rendimento", "g", 100, COR)], XE, 640)
        E.frase(c, t, C["s04.c"] + 1.0, ps("a porcentagem do máximo que sai de verdade", "i", 60, TINTA2), XE, 750, passo=0.1)
        return
    E.frase(c, t, C["s05.a"], ps("a conta dá o", "i", 70) + [("máximo:", "g", 66)] + ps("o rendimento teórico", "i", 70, TINTA2), XE, 240, passo=0.12)
    barra_rend(c, t, C["s05.a"] + 0.6, XE, 440, 1580, 150, 0.75, "máximo = 100%", "75%", tr=C["s05.b"])
    E.formula_em(c, t, C["s05.c"], "real = máximo × 0,75", W / 2, 840, 92, "g", TINTA, "center")


# ---------------- etapas ----------------
YS = (300, 480, 660)


def b_etapas(c, t, C, b):
    if t < C["s08"]:
        xs = []
        for k, (e, tk) in enumerate(zip(EQS, ("s06.a", "s06.b", "s06.c"))):
            Q.formula_em(c, t, C[tk], e, 260, YS[k], 96, cores={"S": E.COR} if t >= C["s07.b"] else None)
            E.foco(c, t, C[tk], 0.4, lambda a, k=k: E.bola(c, 160, YS[k] - 34, 34, a=a))
            E.foco(c, t, C[tk], 0.4, lambda a, k=k: centro(c, str(k + 1), 160, YS[k] - 14, 44, "g", E.SOBRE, a))
        E.frase(c, t, C["s06"], ps("três etapas", "i", 60, TINTA2), XE, 170, passo=0.1)
        if t >= C["s07"]:
            E.frase(c, t, C["s07.a"], ps("três regras de três?", "i", 56, TINTA2), 1180, 170, passo=0.1)
            pts = [(1400, YS[k] - 34) for k in range(3)]
            salto_atomo(c, t, pts, [C["s07.c"], C["s07.d"], C["s07.e"]], r=32)
            E.foco(c, t, C["s07.e"] + 1.6, 0.4, lambda a: centro(c, "2 para 2 = 1 para 1", 1690, YS[1] - 20, 46, "i", TINTA2, a))
            E.frase(c, t, C["s07.f"], [("1 mol", "g", 70, COR)] + ps("de enxofre →", "i", 72)[:2] + [("→", "g", 70, TINTA2), ("1 mol", "g", 70, COR)] + ps("de ácido", "i", 72), XE, 900, passo=0.12)
        return
    if t < C["s09"]:
        Q.formula_em(c, t, C["s08"], "S → H2SO4", W / 2, 300, 130, align="center")
        E.foco(c, t, C["s08.a"], 0.4, lambda a: E.formula(c, "32 g", W / 2 - 330, 430, 84, "g", TINTA, a, "center"))
        E.foco(c, t, C["s08.b"], 0.4, lambda a: E.formula(c, "98 g", W / 2 + 200, 430, 84, "g", TINTA, a, "center"))
        E.formula_em(c, t, C["s08.b"] + 0.8, "2 + 32 + 4 × 16 = 98", W / 2 + 200, 520, 52, "g", TINTA2, "center")
        E.foco(c, t, C["s08.c"], 0.4, lambda a: E.formula(c, "64 g", W / 2 - 330, 700, 96, "g", COR, a, "center"))
        pilula_em(c, t, C["s08.c"] + 0.3, "× 2", W / 2 - 330, 545, 44, E.COR)
        bola_txt(c, t, C["s08.d"], "196 g", W / 2 + 200, 670, 104, 60)
        pilula_em(c, t, C["s08.e"], "o máximo", W / 2 + 520, 670, 50, TINTA)
        return
    E.frase(c, t, C["s09.a"], ps("falta o", "i", 76) + [("rendimento", "g", 72, COR)], XE, 240, passo=0.12)
    barra_rend(c, t, C["s09.a"] + 0.3, XE, 380, 1580, 140, 0.75, "máximo: 196 g", "147 g", tr=C["s09.c"])
    E.formula_em(c, t, C["s09.b"], "0,75 × 196 =", XE, 760, 96, "g", TINTA)
    bola_txt(c, t, C["s09.c"], "147 g", XE + 860, 730, 110, 64)
    pilula_em(c, t, C["s09.d"], "o número do começo", XE + 1300, 730, 46, TINTA)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s10.a"], ps("calcular a parte perdida", "i", 72), XE + 450, 190, passo=0.12)
    E.frase(c, t, C["s10.b"], [("75%", "g", 70, COR)] + ps("de rendimento =", "i", 70) + [("sai 75%", "g", 66, COR)], XE, 360, passo=0.12)
    E.frase(c, t, C["s10.c"], ps("não é o que se perde", "i", 66, TINTA2), XE, 460, passo=0.1)
    E.formula_em(c, t, C["s10.d"], "0,25 × 196 = 49 g", XE, 680, 96, "g", ERRADO)
    if t >= C["s10.e"]:
        E.risco(c, XE - 10, 710, XE + 900, 610, t, C["s10.e"], largura=12)
        pilula_em(c, t, C["s10.e"] + 0.3, "essa é a parte perdida", 1460, 660, 46, ERRADO)
        E.foco(c, t, C["s10.e"] + 1.2, 0.5, lambda a: (E.formula(c, "0,75 × 196 = 147 g", XE, 880, 84, "g", COR, a), E.selo(c, XE + 880, 852, 40, True, a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s12"]:
        E.frase(c, t, C["s11"], ps("o atalho:", "i", 72, CLARO) + [("siga o elemento", "g", 66, BR)], W / 2, 180, "center", 0.12)
        for k, e in enumerate(EQS):
            E.foco(c, t, C["s11.a"] + 0.2 * k, 0.4, lambda a, k=k, e=e: Q.formula(c, e, W / 2, 330 + k * 90, 62, BR, a * 0.45, "center", escuro=True, cores={"S": E.CLARO}))
        Q.formula_em(c, t, C["s11.b"], "S", 640, 760, 150, align="center", escuro=True, cores={"S": E.CLARO})
        Q.formula_em(c, t, C["s11.b"] + 0.3, "H2SO4", 1280, 760, 150, align="center", escuro=True, cores={"S": E.CLARO})
        p = ep(t, C["s11.b"] + 0.5, 0.5)
        if p > 0:
            M.arrow(c, 760, 710, lerp(760, 1020, ease_io(p)), 710, E.CLARO, 1.0, 8, 26)
        E.foco(c, t, C["s11.c"], 0.4, lambda a: centro(c, "1 S", 640, 880, 64, "g", E.CLARO, a))
        E.foco(c, t, C["s11.d"], 0.4, lambda a: centro(c, "1 S", 1280, 880, 64, "g", E.CLARO, a))
        pilula_em(c, t, C["s11.e"], "1 : 1, sem as etapas do meio", W / 2, 1000, 50, E.COR)
        return
    E.frase(c, t, C["s12.a"], ps("o átomo", "i", 72, CLARO) + [("não some", "g", 68, BR)] + ps("nem aparece", "i", 72, CLARO), W / 2, 260, "center", 0.12)
    E.frase(c, t, C["s12.b"], ps("todo enxofre que entra sai no ácido", "i", 62, CLARO), W / 2, 370, "center", 0.1)
    E.frase(c, t, C["s12.c"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("o elemento se divide entre dois produtos", "i", 66, CLARO), W / 2, 560, "center", 0.1)
    E.frase(c, t, C["s12.d"], ps("um rendimento por etapa?", "i", 66, CLARO) + [("multiplique todos", "g", 62, BR)], W / 2, 740, "center", 0.12)
    E.formula_em(c, t, C["s12.d"] + 2.0, "máximo × 0,9 × 0,8 …", W / 2, 870, 76, "g", E.CLARO, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 180)
    Q.atomo_em(c, t, C["s13.a"], XE + 50, 320, 44, "S")
    E.frase(c, t, C["s13.a"], [("16 g", "g", 76)] + ps("de enxofre", "i", 80), XE + 130, 350, passo=0.12)
    E.frase(c, t, C["s13.b"], [("80%", "g", 76, COR)] + ps("de rendimento", "i", 80), XE, 500, passo=0.12)
    E.frase(c, t, C["s13.c"], ps("quantos gramas de", "i", 66), XE, 700, passo=0.1)
    Q.formula_em(c, t, C["s13.c"] + 0.6, "H2SO4?", XE + 600, 710, 90)
    if t < C["s14"]:
        Q.molecula(c, t, C["s13.c"], "H2SO4", 1480, 480, 140, passo=0.1)
    else:
        E.relogio(c, t, C["s14.a"], cx=1480, cy=470, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    Q.formula_em(c, t, C["s15"], "S → H2SO4", W / 2, 260, 120, align="center")
    E.foco(c, t, C["s15.a"], 0.4, lambda a: (E.formula(c, "32 g", W / 2 - 300, 380, 76, "g", TINTA, a, "center"), E.formula(c, "98 g", W / 2 + 190, 380, 76, "g", TINTA, a, "center")))
    E.foco(c, t, C["s15.b"], 0.4, lambda a: (E.formula(c, "16 g", W / 2 - 300, 520, 84, "g", COR, a, "center")))
    pilula_em(c, t, C["s15.b"] + 0.3, "÷ 2", W / 2 - 520, 450, 44, E.COR)
    E.foco(c, t, C["s15.c"], 0.4, lambda a: E.formula(c, "49 g", W / 2 + 190, 520, 84, "g", TINTA, a, "center"))
    E.foco(c, t, C["s15.c"] + 0.4, 0.4, lambda a: E.escreve(c, "no máximo", W / 2 + 360, 515, 54, "i", TINTA2, a))
    E.formula_em(c, t, C["s15.d"], "0,8 × 49 =", XE + 300, 800, 96, "g", TINTA)
    bola_txt(c, t, C["s15.e"], "39,2 g", XE + 1060, 770, 116, 62, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s16.a", [("real", "g", 66), ("=", "g", 66, TINTA2), ("máximo", "g", 66), ("×", "g", 66, TINTA2), ("rendimento", "g", 66, COR)]),
                 ("s16.b", [("em etapas:", "g", 66)] + ps("siga o elemento do começo ao fim", "i", 70)))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("próxima", "i", 80), ("aula:", "i", 80), ("praticando", "g", 76, COR)], XE, 250, passo=0.12)
    E.frase(c, t, C["s17.a"], ps("fábrica e", "i", 76) + [("meio ambiente", "g", 72)], XE, 420, passo=0.12)
    E.frase(c, t, C["s17.b"], [("mol,", "g", 66), ("pureza,", "g", 66), ("rendimento,", "g", 66), ("limitante", "g", 66, COR)], XE, 580, passo=0.12)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 780, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 805, p), ep(t, C["s17.c"] + 0.2, 0.4))
    E.frase(c, t, C["s17.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, rendimento=b_rendimento, etapas=b_etapas, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
