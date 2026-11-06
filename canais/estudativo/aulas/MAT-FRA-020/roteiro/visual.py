"""Visual — Estudativo · MAT-FRA-020: dízimas, reconhecer e prever.
O ciclo de restos (5 → 6 → 5) mostra por que a conta repete. Nas fatorações, o 2 e o 5 têm sempre a mesma cor (a da matéria);
qualquer outro primo sai em vermelho: é ele que traz a dízima.
Todo instante vem de C[...]; o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
import math
from fractions import Fraction as F

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_out, ease_back, fr, palco, centro, linha
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-020_dizimas_reconhecer_e_prever.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("repete", "porque", "exemplos", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert E.dividir("5", 11, 2)["quociente"] == "0,45" and E.dividir("5", 11, 2)["resto"] == 5
assert 2 * 5 == 10 and 2 * 2 * 5 * 5 == 100 and 2 * 2 * 2 * 5 == 40 and 2 * 2 * 2 * 5 * 5 * 5 == 1000 and 5 * 5 == 25
assert 7 * 25 == 175 and 40 * 25 == 1000 and F(7, 40) == F("0.175") and F(1, 4) == F("0.25")
assert 2 * 3 * 5 == 30 and F(9, 30) == F(3, 10) == F("0.3") and 3 * 5 * 5 == 75
assert 2 * 5 * 5 == 50 and 2 * 2 * 3 == 12 and F(6, 15) == F(2, 5) and F(7, 30) == F("0.2") + F(1, 30)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def txt(c, t, ti, s, x, y, size=64, cor=None, est="b"):
    E.foco(c, t, ti, 0.45, lambda a: E.escreve(c, s, x, y, size, est, cor or TINTA, a))


def cen(c, t, ti, s, x, y, size=64, cor=None, est="g"):
    E.foco(c, t, ti, 0.45, lambda a: centro(c, s, x, y, size, est, cor or TINTA, a))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE if cor is None else M.on(cor), a)


def sobra(c, t, t0, t1, s, x, y, size, lin, col):
    """o resto sozinho na conta, até o zero chegar: col = coluna do último algarismo do resto"""
    cl = E.casa(size)
    E.saida(c, t, t1, lambda: E.foco(c, t, t0, 0.35, lambda a: [centro(c, ch, x + (col - (len(s) - 1 - i) + 0.5) * cl, y + lin * size * 1.12, size, "g", TINTA, a) for i, ch in enumerate(s)]), d=0.01)


def fatores(c, t, t0, n, lista, x, y, size=100, dt=0.7, escuro=False, foca=None, ts=None):
    """escreve 'n = 2 × 2 × 5' a partir de x: 2 e 5 sempre na cor da matéria, outro primo em vermelho.
    ts = instante de cada fator (sem isso, um a cada dt); foca = instante em que os outros primos ganham um aro"""
    forte = CLARO if escuro else COR
    neutro = BR if escuro else TINTA
    sep = "#FFFFFF" if escuro else TINTA2
    pre = f"{n} ="
    E.foco(c, t, t0, 0.45, lambda a: E.escreve(c, pre, x, y, size, "g", neutro, a))
    xx = x + E.larg(pre, "g", size) + size * 0.5
    ts = ts or [t0 + 0.7 + i * dt for i in range(len(lista))]
    pos = []
    for i, (p, ti) in enumerate(zip(lista, ts)):
        cor = forte if p in (2, 5) else ERRADO
        if i:
            E.foco(c, t, ti - 0.05, 0.3, lambda a, xx=xx: centro(c, "×", xx - size * 0.575, y - size * 0.03, size * 0.8, "g", sep, a))
        E.foco(c, t, ti, 0.4, lambda a, p=p, xx=xx, cor=cor: centro(c, str(p), xx + size * 0.2, y, size, "g", cor, a))
        pos.append(xx + size * 0.2)
        xx += size * 1.55
    if foca is not None:
        for p, xp in zip(lista, pos):
            if p not in (2, 5) and t >= foca:
                r = size * 0.5 * ease_back(prog(t, foca, 0.45))
                c.drawCircle(xp, y - size * 0.36, max(r, 1), M.paint(ERRADO, 1.0, stroke=6))
    return pos


def lembrete(c, t, C, cena, n, nome, itens):
    """itens = [(cue, linha fina, linha forte)]"""
    E.frase(c, t, C[cena] + 0.1, ps("você precisa de", "i", 84), XE, 410, "left", 0.18)
    E.foco(c, t, C[f"{cena}.a"], 0.5, lambda a: E.escreve(c, n, XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[f"{cena}.a"] + 0.15, 0.5, lambda a: E.escreve(c, nome, XE + 245, 700, 120, "i", TINTA, a))
    x, w, y0 = 960, 780, 280
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    ks = [k for k, _, _ in itens]
    py = y0 + 170
    for i in range(1, len(ks)):
        py = lerp(py, y0 + i * 280 + 170, ease_io(prog(t, C[ks[i]] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C[ks[0]], 0.4))
    E.frase(c, t, lerp(C[ks[-1]], C[f"{cena}.end"], 0.72), ps("faltou?", "i", 60, COR) + ps("procure no canal", "i", 60), XE, 860, "left", 0.15)


def ciclo(c, t, cx, cy, ti, tv1, tv2, tgiro, gira=True):
    """o ciclo de restos: duas esferas (5 e 6) ligadas por dois arcos. Cada volta devolve o quociente 4 e depois o 5.
    ti = entra o 5; tv1 = arco 5→6 com o 4; tv2 = arco 6→5 com o 5; tgiro = um ponto começa a dar voltas"""
    dx, r = 230, 92
    x5, x6 = cx - dx, cx + dx
    E.foco(c, t, ti, 0.45, lambda a: num_bola(c, "5", x5, cy, r, 110, a))
    centro(c, "o começo", x5, cy + 212, 60, "i", TINTA, ep(t, ti, 0.4))
    # arcos: por cima de 5 para 6, por baixo de 6 para 5
    for cima, tv, q in ((True, tv1, "4"), (False, tv2, "5")):
        p = ease_out(prog(t, tv, 0.7))
        if p <= 0:
            continue
        pts = []
        n = max(2, int(44 * p))
        for i in range(n + 1):
            u = 0.2 + 0.6 * p * i / n  # não entra nas esferas
            ang = math.pi * u
            if cima:
                pts.append((cx - dx * math.cos(ang), cy - 170 * math.sin(ang)))
            else:
                pts.append((cx + dx * math.cos(ang), cy + 170 * math.sin(ang)))
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            M.line(c, x0, y0, x1, y1, TINTA, 1.0, 7)
        if p >= 0.99:
            (xa, ya), (xb, yb) = pts[-3], pts[-1]
            ang = math.atan2(yb - ya, xb - xa)
            for d in (2.55, -2.55):
                M.line(c, xb, yb, xb + 30 * math.cos(ang + d), yb + 30 * math.sin(ang + d), TINTA, 1.0, 7)
        yq = cy - 170 if cima else cy + 170
        E.foco(c, t, tv + 0.2, 0.4, lambda a, yq=yq, q=q: E.pilula(c, f"dá {q}", cx, yq, 56, estilo="g", cor=E.SOBRE, a=a))
    E.foco(c, t, tv1 + 0.5, 0.45, lambda a: num_bola(c, "6", x6, cy, r, 110, a))
    centro(c, "sobra", x6, cy + 212, 60, "i", TINTA, ep(t, tv1 + 0.5, 0.4))
    if gira and t >= tgiro:
        u = ((t - tgiro) / 2.6) % 1.0
        ang = 2 * math.pi * u
        px = cx - dx * 1.0 * math.cos(ang)
        py = cy - 170 * math.sin(ang)
        c.drawCircle(px, py, 18, M.paint(TINTA))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def conta():
        txt(c, t, a_, "5 ÷ 11", XE, 330, 170, TINTA, "g")
        cen(c, t, b_ - 0.1, "=", 880, 330, 150, TINTA2)
        xv, y, s = 620, 620, 170
        val = "0,454545"
        E.foco(c, t, b_, 0.4, lambda q: E.numero(c, "0,", xv, y, s, a=q))
        cs = E._centros(val, xv, s)
        for i in range(2, 8):
            ti = lerp(b_, c_, 0.14 + (i - 2) * 0.115)
            E.foco(c, t, ti, 0.3, lambda q, i=i: centro(c, val[i], cs[i], y, s, "g", COR, q))
        cen(c, t, lerp(b_, c_, 0.84), "...", cs[7] + 130, y, 150, COR)
        E.frase(c, t, c_, ps("não acaba", "i", 110) + [("nunca", "g", 110, ERRADO)], W / 2, 820, "center", 0.2)
        E.frase(c, t, d_, ps("dá para saber", "i", 84) + [("antes de dividir?", "g", 84, COR)], W / 2, 960, "center", 0.15)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    ta, tb = C["s02.a"], C["s02.b"]
    f = lambda q: lerp(ta, tb, q)
    E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 290 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
    E.frase(c, t, C["s02"] + 0.1, ps("dá,", "g", 100, COR) + ps("sim", "i", 100), XE, 220, "left", 0.15)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 350, "left", 0.13)
    E.frase(c, t, f(0.38), [("apontar", "g", 124)], XE, 510)
    E.frase(c, t, f(0.45), ps("o que se repete", "i", 108), XE, 630, "left", 0.15)
    E.frase(c, t, f(0.66), [("prever", "g", 124, COR)], XE, 790)
    E.frase(c, t, f(0.72), ps("se a divisão acaba", "i", 96), XE, 900, "left", 0.15)
    E.foco(c, t, tb + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1450, 505, 88, "g", E.SOBRE, a), centro(c, "de prova", 1450, 600, 92, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", "2", "coisas", (("s03.b", "transformar fração", "em decimal"), ("s03.c", "fatorar um número", "em primos")))


# ---------------- por que repete ----------------
def b_repete(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5 = C["s05.a"], C["s05.b"]
    E.frase(c, t, C["s04"] + 0.1, ps("por que a conta", "i", 80) + [("não acaba?", "g", 76, COR)], XE - 40, 130, "left", 0.15)
    x, y, s = 190, 350, 112
    Dv = E.dividir("5", 11, 2)
    # 50 = 5 + zero; 60 = 6 + zero; o último 5 é o resto final
    tq = [a4, lerp(b4, c4, 0.5), lerp(c4, C["s04.end"], 0.45)]
    tr = [b4, c4, lerp(c4, C["s04.end"], 0.72)]
    E.conta_div(c, t, Dv, tq, tr, C["s04"] + 0.4, x, y, s, tv=a4)
    sobra(c, t, lerp(b4, c4, 0.75), c4, "6", x, y, s, 2, 1)
    # quem volta: o 5 do começo e o 5 do fim, na mesma caixa
    cl = E.casa(s)
    px5 = x + 0.5 * cl
    if t >= a5:
        p = ep(t, a5, 0.4)
        E.caixa_pontilhada(c, px5 - 58, y - 100, 116, 116, p, ERRADO, prog_=p)
        col = 2
        yf = y + 3 * s * 1.12
        E.caixa_pontilhada(c, x + (col + 0.5) * cl - 58, yf - 100, 116, 116, p, ERRADO, prog_=p)
    E.frase(c, t, a5 + 0.2, [("voltou o 5", "g", 84, ERRADO)], x, 960)
    # ciclo de restos: entra à direita, no tempo de cada resto
    cx, cy = 1400, 390
    ciclo(c, t, cx, cy, a4 + 0.2, lerp(b4, c4, 0.75), lerp(c4, C["s04.end"], 0.72), b5 + 0.1)
    # o que o ciclo escreve no resultado
    val = "0,454545"
    xv, yv, sv = 1050, 860, 118
    cs = E._centros(val, xv, sv)
    E.foco(c, t, b5, 0.4, lambda q: E.numero(c, "0,", xv, yv, sv, a=q))
    for i in range(2, 8):
        ti = lerp(b5, C["s05.end"], 0.08 + (i - 2) * 0.13)
        E.foco(c, t, ti, 0.25, lambda q, i=i: centro(c, val[i], cs[i], yv, sv, "g", COR, q))
    cen(c, t, lerp(b5, C["s05.end"], 0.86), "...", cs[7] + 92, yv, 96, COR)
    E.frase(c, t, b5 + 0.1, [("repete tudo igual", "g", 62, COR)], 960, 980)


# ---------------- nomes ----------------
def b_nomes(c, t, C, b):
    a_, b_, c_, d_ = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]

    def dizima():
        E.foco(c, t, a_, 0.5, lambda q: centro(c, "dízima", W / 2, 300, 210, "g", COR, q))
        E.frase(c, t, lerp(a_, b_, 0.3), ps("um grupo de algarismos se repete sem fim", "i", 76), W / 2, 420, "center", 0.11)
        xv, y, s = 620, 680, 200
        val = "0,4545"
        cs = E._centros(val, xv, s)
        cores = {2: COR, 3: COR} if t >= c_ else None
        E.foco(c, t, lerp(a_, b_, 0.5), 0.45, lambda q: E.numero(c, val, xv, y, s, a=q, cores=cores))
        xp = cs[5] + 160
        for i in range(3):
            q = ep(t, b_ + i * 0.2, 0.3)
            pu = 1 + 0.5 * max(0.0, math.sin((t - b_ - i * 0.2) * 5)) * (1 - ep(t, b_ + 1.4, 0.3)) if t >= b_ else 1
            c.drawCircle(xp + i * 62, y - 12, 15 * pu, M.paint(ERRADO if t < b_ + 2 else TINTA, q))
        E.chave(c, cs[2] - 66, cs[3] + 66, y + 50, COR, ep(t, c_, 0.4), 34, 8)
        E.foco(c, t, c_, 0.45, lambda q: E.pilula(c, "período", (cs[2] + cs[3]) / 2, y + 170, 72, estilo="g", cor=E.SOBRE, a=q))
        E.frase(c, t, d_, [("aqui,", "i", 92), ("45", "g", 130, COR)], 1160, y + 190)
    E.saida(c, t, C["s07"] - 0.1, dizima)
    if t < C["s07"]:
        return
    a7, b7 = C["s07.a"], C["s07.b"]
    E.frase(c, t, C["s07"] + 0.1, ps("quando a conta", "i", 96) + [("acaba", "g", 96, COR)], W / 2, 260, "center", 0.16)
    y = 560
    fr(c, t, a7, 1, 4, 620, y - 30, 180, COR)
    cen(c, t, a7 + 0.5, "=", 830, y + 30, 130, TINTA2)
    E.foco(c, t, a7 + 0.7, 0.5, lambda q: E.numero(c, "0,25", 1120, y + 40, 200, a=q))
    E.frase(c, t, b7, [("decimal", "g", 140, COR), ("exato", "g", 140, COR)], W / 2, 900, "center", 0.2)


# ---------------- por que só 2 e 5 ----------------
def b_porque(c, t, C, b):
    a_, b_, c_, d_ = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]

    def base():
        E.frase(c, t, C["s08"] + 0.1, ps("como", "i", 88) + [("prever?", "g", 88, COR)], W / 2, 170, "center", 0.16)
        E.frase(c, t, a_, ps("todo decimal exato tem embaixo", "i", 80), W / 2, 290, "center", 0.12)
        E.frase(c, t, lerp(a_, b_, 0.5), [("10,", "g", 84, COR), ("100,", "g", 84, COR), ("1.000", "g", 84, COR)], W / 2, 400, "center", 0.2)
        fatores(c, t, b_, 10, (2, 5), 300, 580, 110)
        fatores(c, t, c_, 100, (2, 2, 5, 5), 300, 730, 110)
        E.frase(c, t, d_, ps("só aparecem os primos", "i", 92) + [("2", "g", 100, COR), ("e", "i", 92), ("5", "g", 100, COR)], W / 2, 920, "center", 0.15)
    E.saida(c, t, C["s09"] - 0.1, base)
    if t < C["s09"]:
        return
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    E.frase(c, t, C["s09"] + 0.1, ps("a regra,", "i", 84, COR) + ps("para a fração já simplificada", "i", 84), W / 2, 170, "center", 0.13)
    xe, xd = 510, 1400
    E.frase(c, t, a9, ps("denominador só com", "i", 76), xe, 340, "center", 0.13)
    E.frase(c, t, a9 + 0.8, [("2", "g", 150, COR), ("e", "i", 120), ("5", "g", 150, COR)], xe, 510, "center", 0.2)
    if t >= b9:
        p = ep(t, b9, 0.4)
        M.arrow(c, xe, 560, xe, 650, TINTA, p, 5, 16, p)
    E.foco(c, t, b9, 0.5, lambda q: (centro(c, "decimal", xe, 760, 110, "g", COR, q), centro(c, "exato", xe, 870, 110, "g", COR, q)))
    E.frase(c, t, lerp(a9, b9, 0.55), ps("completa até 10, 100, 1.000", "i", 58), xe, 980, "center", 0.11)
    E.frase(c, t, c9, ps("apareceu outro primo?", "i", 76), xd, 340, "center", 0.13)
    E.frase(c, t, c9 + 0.8, [("3", "g", 150, ERRADO), ("ou", "i", 120), ("7", "g", 150, ERRADO)], xd, 510, "center", 0.2)
    if t >= d9:
        p = ep(t, d9, 0.4)
        M.arrow(c, xd, 560, xd, 650, TINTA, p, 5, 16, p)
    E.frase(c, t, lerp(c9, d9, 0.45), ps("nunca chega lá", "i", 72), xd, 980, "center", 0.13)
    E.foco(c, t, d9, 0.5, lambda q: centro(c, "dízima", xd, 800, 130, "g", ERRADO, q))


# ---------------- exemplos ----------------
def b_exemplos(c, t, C, b):
    a_, b_, c_, d_, e_, f_ = (C[f"s10.{k}"] for k in "abcdef")

    def um():
        fr(c, t, a_, 7, 40, 290, 240, 120, TINTA)
        fatores(c, t, b_, 40, (2, 2, 2, 5), 520, 290, 96)
        E.foco(c, t, c_, 0.45, lambda q: E.pilula(c, "decimal exato", 1560, 262, 54, estilo="g", cor=E.SOBRE, a=q))
        pos = fatores(c, t, d_, "1.000", (2, 2, 2, 5, 5, 5), 330, 520, 96, ts=[d_ + q for q in (0.9, 1.1, 1.3, 2.1, 2.3, 2.5)])
        # os dois fatores 5 que faltam
        tm = lerp(d_, e_, 0.35)
        if t >= tm:
            p = ep(t, tm, 0.4)
            E.caixa_pontilhada(c, pos[4] - 64, 520 - 104, pos[5] - pos[4] + 128, 124, p, ERRADO, prog_=p)
        E.frase(c, t, tm + 0.3, ps("faltam dois fatores 5:", "i", 62) + [("5 × 5 = 25", "g", 62, COR)], 1020, 610, "center", 0.12)
        y, s = 810, 120
        fr(c, t, e_ - 0.2, 7, 40, 290, y, s, TINTA)
        E.pontes(c, t, 410, 740, y, s, "× 25", e_, e_ + 0.2, size=52)
        fr(c, t, f_, 175, "1.000", 920, y, s, COR)
        cen(c, t, f_ + 0.7, "=", 1170, y + 40, 110, TINTA2)
        E.foco(c, t, lerp(f_, C["s10.end"], 0.45), 0.5, lambda q: E.numero(c, "0,175", 1400, y + 50, 130, cor=COR, a=q))
    E.saida(c, t, C["s11"] - 0.1, um)
    if t < C["s11"]:
        return
    a1, b1, c1, d1, e1, f1, g1 = (C[f"s11.{k}"] for k in "abcdefg")
    fr(c, t, a1, 7, 30, 290, 240, 120, TINTA)
    fatores(c, t, b1, 30, (2, 3, 5), 520, 290, 96, foca=c1)
    E.foco(c, t, d1, 0.45, lambda q: E.pilula(c, "dízima", 1370, 262, 60, estilo="g", fundo=ERRADO, cor=BR, a=q))
    E.frase(c, t, lerp(a1, b1, 0.5), ps("não simplifica", "i", 60), XE + 330, 180, "left", 0.13)
    xv, y, s = 440, 570, 150
    val = "0,2333"
    cs = E._centros(val, xv, s)
    E.foco(c, t, e1, 0.45, lambda q: E.numero(c, val, xv, y, s, a=q, cores={3: ERRADO, 4: ERRADO, 5: ERRADO} if t >= f1 else None))
    cen(c, t, e1 + 0.8, "...", cs[5] + 130, y, 120, TINTA)
    E.chave(c, cs[3] - 52, cs[3] + 52, y + 40, ERRADO, ep(t, f1, 0.4), 28, 7)
    E.foco(c, t, f1, 0.45, lambda q: E.pilula(c, "período", cs[3], y + 140, 58, estilo="g", fundo=ERRADO, cor=BR, a=q))
    E.frase(c, t, lerp(e1, f1, 0.7), ps("o 2 aparece uma vez só", "i", 66), 1120, y - 40, "left", 0.12)
    E.frase(c, t, f1, ps("o período é", "i", 66) + [("3", "g", 80, ERRADO)], 1120, y + 60, "left", 0.13)
    E.frase(c, t, lerp(f1, g1, 0.5), ps("e o 11 do começo?", "i", 76), XE, 870, "left", 0.13)
    E.frase(c, t, g1, [("11", "g", 92, ERRADO)] + ps("é primo, e não é", "i", 76) + [("2", "g", 92, COR)] + ps("nem", "i", 76) + [("5", "g", 92, COR)], XE, 970, "left", 0.13)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_ = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]

    def pegadinha():
        E.frase(c, t, C["s12"] + 0.1, [("cuidado:", "g", 100, ERRADO)] + ps("a regra vale para a", "i", 84), W / 2, 190, "center", 0.14)
        E.frase(c, t, a_, [("fração na forma mais simples", "g", 84, COR)], W / 2, 310, "center")
        y, s = 590, 170
        fr(c, t, b_, 9, 30, 310, y, s, TINTA)
        E.frase(c, t, b_ + 1.2, ps("parece dízima", "i", 72, ERRADO), 310, 840, "center", 0.13)
        E.pontes(c, t, 440, 800, y, s, "÷ 3", c_, c_ + 0.15, size=56)
        fr(c, t, c_ + 0.3, 3, 10, 960, y, s, COR)
        cen(c, t, d_ - 0.1, "=", 1150, y + 50, 120, TINTA2)
        E.foco(c, t, d_, 0.45, lambda q: E.numero(c, "0,3", 1400, y + 60, 170, cor=COR, a=q))
        E.foco(c, t, d_ + 0.8, 0.45, lambda q: E.pilula(c, "decimal exato", 1400, 800, 58, estilo="g", cor=E.SOBRE, a=q))
    E.saida(c, t, C["s13"] - 0.1, pegadinha)
    if t < C["s13"]:
        return
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, C["s13"] + 0.1, ps("o", "i", 100) + [("3", "g", 110, ERRADO)] + ps("do denominador", "i", 100), W / 2, 230, "center", 0.15)
    E.frase(c, t, a3, [("sumiu", "g", 110, ERRADO)] + ps("na simplificação", "i", 100), W / 2, 360, "center", 0.15)
    E.foco(c, t, b3, 0.5, lambda q: num_bola(c, "1", 420, 590, 76, 100, q))
    E.frase(c, t, b3 + 0.1, [("simplifique", "g", 120, COR)], 540, 630)
    E.foco(c, t, c3, 0.5, lambda q: num_bola(c, "2", 420, 800, 76, 100, q))
    E.frase(c, t, c3 + 0.1, ps("olhe o", "i", 110) + [("denominador", "g", 110, COR)], 540, 840, "left", 0.15)


# ---------------- atalho (palco escuro) ----------------
def corta_zero(c, t, t0, n, cx, cy, s):
    """risca o último zero do denominador n de uma fração de tamanho s centrada em (cx, cy)"""
    y = cy + s * 0.9
    w = E.larg(n, "g", s)
    xz = cx + w / 2 - E.larg("0", "g", s) / 2
    if t >= t0:
        M.line(c, xz - s * 0.34, y + s * 0.08, xz + s * 0.34, y - s * 0.8, ERRADO, 1.0, 12, progress=ep(t, t0, 0.3))


def b_atalho(c, t, C, b):
    palco(c, t)
    a_, b_, c_, d_, e_, f_ = (C[f"s14.{k}"] for k in "abcdef")

    def cortes():
        E.frase(c, t, C["s14"] + 0.1, ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center")
        E.frase(c, t, a_, ps("corte os", "i", 88, BR) + [("zeros do fim", "g", 88, CLARO)] + ps("do denominador", "i", 88, BR), W / 2, 270, "center", 0.14)
        E.frase(c, t, b_, ps("cada zero é um", "i", 76, BR) + [("2", "g", 84, CLARO), ("×", "b", 64, BR), ("5", "g", 84, CLARO)], W / 2, 380, "center", 0.14)
        for y, n, tf, dn, ti, tv, lista, veredito, cor in ((580, 7, c_, 40, lerp(c_, d_, 0.2), d_, (2, 2), "exato", CLARO), (830, 7, e_, 30, lerp(e_, f_, 0.25), f_, (3,), "dízima", ERRADO)):
            E.foco(c, t, tf, 0.45, lambda q, y=y, dn=dn, ti=ti: (E.fracao(c, 7, dn, 290, y - 30, 110, BR, q), corta_zero(c, t, ti, str(dn), 290, y - 30, 110)))
            if t >= ti + 0.2:
                p = ep(t, ti + 0.2, 0.4)
                M.arrow(c, 410, y, 540, y, CLARO, p, 5, 16, p)
            sobra_ = str(dn // 10)
            if len(lista) > 1:
                fatores(c, t, ti + 0.4, sobra_, lista, 590, y + 36, 100, escuro=True)
            else:
                E.foco(c, t, ti + 0.4, 0.45, lambda q, y=y: E.escreve(c, "sobra", 590, y + 30, 84, "i", BR, q))
                E.foco(c, t, ti + 0.6, 0.45, lambda q, y=y: E.escreve(c, "3", 840, y + 36, 110, "g", ERRADO, q))
            E.foco(c, t, tv, 0.5, lambda q, y=y, veredito=veredito, cor=cor: E.escreve(c, veredito, 1260, y + 36, 110, "g", cor, q))
    E.saida(c, t, C["s15"] - 0.1, cortes)
    if t < C["s15"]:
        return
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"] + 0.1, ps("não compensa quando", "i", 88, CLARO), W / 2, 240, "center", 0.15)
    E.frase(c, t, a5, ps("o denominador", "i", 96, BR) + [("não termina em zero", "g", 92, CLARO)], W / 2, 360, "center", 0.15)
    cen(c, t, lerp(a5, b5, 0.75), "75", W / 2, 590, 180, BR)
    E.frase(c, t, b5, ps("aí,", "i", 96, CLARO) + [("fatore normalmente", "g", 96, BR)], W / 2, 750, "center", 0.15)
    fatores(c, t, c5, 75, (3, 5, 5), 520, 930, 120, escuro=True)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_, c_, d_ = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, lerp(C["s16"], a_, 0.5), ps("sem fazer a divisão,", "i", 84), XE, 310, "left", 0.14)
    E.frase(c, t, a_, [("classifique", "g", 104, COR)], XE, 440)
    E.frase(c, t, a_ + 1.2, [("decimal exato", "g", 80), ("ou", "i", 84), ("dízima?", "g", 80)], XE, 560, "left", 0.2)
    y, s = 760, 140
    for x, n, d, ti in ((300, 9, 50, b_), (620, 5, 12, c_), (940, 6, 15, d_)):
        fr(c, t, ti, n, d, x, y, s, TINTA)
    E.relogio(c, t, C["s17.a"], 1520, 400, 190)


# ---------------- resposta ----------------
def linha_resp(c, t, y, n, d, tf, s=120):
    fr(c, t, tf, n, d, 270, y - 40, s, TINTA)


def b_resposta(c, t, C, b):
    a_, b_, c_, d_ = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    a9, b9, c9, d9 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    y1, y2, y3 = 210, 510, 810
    sz, xf = 92, 480

    linha_resp(c, t, y1 + 30, 9, 50, C["s18"] + 0.1, 110)
    fatores(c, t, a_, 50, (2, 5, 5), xf, y1 + 30, sz)
    E.foco(c, t, b_, 0.45, lambda q: E.pilula(c, "decimal exato", 1450, y1, 56, estilo="g", cor=E.SOBRE, a=q))

    linha_resp(c, t, y2 + 30, 5, 12, c_ - 0.2, 110)
    fatores(c, t, c_, 12, (2, 2, 3), xf, y2 + 30, sz, foca=d_ - 1.2)
    E.foco(c, t, d_, 0.45, lambda q: E.pilula(c, "dízima", 1450, y2, 60, estilo="g", fundo=ERRADO, cor=BR, a=q))

    linha_resp(c, t, y3 + 30, 6, 15, a9, 110)
    E.saida(c, t, b9 - 0.1, lambda: E.frase(c, t, a9 + 0.6, [("a pegadinha", "g", 76, ERRADO)], 400, y3 + 30), d=0.3)
    E.pontes(c, t, 380, 620, y3 - 10, 110, "÷ 3", b9, b9 + 0.15, size=48)
    fr(c, t, c9, 2, 5, 730, y3 - 10, 110, COR)
    txt(c, t, c9 + 0.5, "embaixo, só o 5", 840, y3 + 30, 66, TINTA, "i")
    E.foco(c, t, d9, 0.45, lambda q: E.pilula(c, "decimal exato", 1450, y3, 56, estilo="g", cor=E.SOBRE, a=q))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        for i, (k, s) in enumerate((("s20.a", "simplifique"), ("s20.b", "fatore o denominador"))):
            y = 370 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 330, y - 30, 56, 64, a))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 92)], 430, y)
        cc, dd = C["s20.c"], C["s20.d"]
        E.frase(c, t, cc, ps("só", "i", 88) + [("2", "g", 100, COR), ("e", "i", 88), ("5", "g", 100, COR)], 560, 760, "center", 0.15)
        cen(c, t, cc + 0.5, "decimal exato", 560, 880, 84, COR)
        E.frase(c, t, dd, ps("outro primo", "i", 88), 1350, 760, "center", 0.15)
        cen(c, t, dd + 0.4, "dízima", 1350, 880, 84, ERRADO)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a_, b_, c_, d_ = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
    E.frase(c, t, C["s21"] + 0.1, ps("próxima aula", "i", 84), XE, 290)
    E.frase(c, t, a_, [("Praticando:", "g", 130, COR)], XE, 430)
    E.frase(c, t, a_ + 0.4, [("números decimais", "g", 130, COR)], XE, 570)
    E.frase(c, t, b_, ps("dinheiro e medida", "i", 110), XE, 700, "left", 0.2)
    E.foco(c, t, c_, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 240, 76, estilo="g", cor=E.SOBRE, a=a))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1580, p), lerp(560, 265, p), ep(t, c_ + 0.2, 0.4))
    E.frase(c, t, d_, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, repete=b_repete, nomes=b_nomes, porque=b_porque, exemplos=b_exemplos,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
