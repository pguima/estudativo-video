"""Visual — Estudativo · MAT-RAZ-014: dividir em partes inversamente proporcionais.
Mesma linguagem da MAT-RAZ-013: partes() é a barra do prêmio cortada em k pedaços iguais, pintada por pessoa (índigo = Edu,
preto = Fabi, lilás = Gil), com o valor de cada pedaço dentro; troca() faz a conta de cima evoluir no lugar. Peças locais:
faltas() desenha os dias de falta riscados; tira() é a barra comprida que encolhe com o dobro e o triplo.
Todo instante vem de C[...]; o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
from fractions import Fraction as Fr

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-014_divisao_inversamente_proporcional.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "conta", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
LILAS = E.mix(E.COR, "#FFFFFF", 0.42)  # a terceira pessoa
# as contas da aula, conferidas
assert [Fr(1, n) * 12 for n in (2, 3, 4)] == [6, 4, 3] and 6 + 4 + 3 == 13 and 2340 // 13 == 180
assert (6 * 180, 4 * 180, 3 * 180) == (1080, 720, 540) and 1080 + 720 + 540 == 2340 and 1080 * 2 == 720 * 3 == 540 * 4 == 2160
assert 2340 // 9 == 260 and (4 * 260, 3 * 260, 2 * 260) == (1040, 780, 520) and 1040 * 2 == 2080 and 780 * 3 == 2340
assert (12 // 3, 12 // 4, 12 // 6) == (4, 3, 2) and 1800 // 9 == 200 and (800, 600, 400) == (4 * 200, 3 * 200, 2 * 200)
assert 800 + 600 + 400 == 1800 and 800 * 3 == 600 * 4 == 400 * 6 == 2400


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


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def troca(c, t, estados, cx, y, size):
    """conta que evolui no lugar: estados = [(t0, fórmula, cor)]; cada uma sai quando a próxima entra"""
    for i, (t0, s, cor) in enumerate(estados):
        if t < t0:
            break
        t1 = estados[i + 1][0] if i + 1 < len(estados) else 1e9
        E.saida(c, t, t1 - 0.15, lambda t0=t0, s=s, cor=cor: fcen(c, t, t0, s, cx, y, size, cor), d=0.3)


def partes(c, x, y, w, h, n, grupos=(), a=1.0, rotulos=(), size=56, escuro=False):
    """barra cortada em n pedaços iguais. grupos = [(i0, i1, cor, p)]; rotulos = [(i, texto, a)] no meio do pedaço i"""
    if a <= 0:
        return
    rr = E._casco(c, x, y, w, h, 14, a, escuro)
    fat = w / n
    c.save(); c.clipRRect(rr, True)
    pint = set()
    for i0, i1, cor, p in grupos:
        if p > 0:
            c.drawRect(skia.Rect.MakeXYWH(x + fat * i0, y, fat * (i1 - i0) * M.clamp(p), h), M.paint(cor, a))
            if p >= 0.99:
                pint.update(range(i0, i1))
    for i in range(1, n):
        lx = x + fat * i
        M.line(c, lx, y, lx, y + h, BR if (i in pint or i - 1 in pint) else (CINZA if escuro else FIO), a, 4)
    c.restore()
    c.drawRRect(rr, M.paint(BR if escuro else TINTA, a, stroke=3))
    for i, s, q in rotulos:
        if q > 0:
            cor = BR if (i in pint or escuro) else TINTA
            centro(c, s, x + fat * (i + 0.5), y + h / 2 + size * 0.36, size, "g", cor, a * q)


def grupo_rot(c, t, t0, x, y, w, n, i0, i1, l1, cor, tl=None, l2=None, size=64):
    """chave embaixo dos pedaços i0..i1, o nome e (em tl) o valor"""
    fat = w / n
    x0, x1 = x + fat * i0 + 8, x + fat * i1 - 8
    E.chave(c, x0, x1, y, cor, ep(t, t0, 0.5), 22)
    E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, l1, (x0 + x1) / 2, y + 90, 54, "i", TINTA if cor == LILAS else cor, a))
    if l2 is not None and tl is not None:
        fcen(c, t, tl, l2, (x0 + x1) / 2, y + 190, size, TINTA if cor == LILAS else cor)


def faltas(c, cx, y, n, a, lado=64, gap=14, cor=TINTA):
    """n dias de falta: quadradinhos de calendário riscados, centrados em cx"""
    if a <= 0:
        return
    w = n * (lado + gap) - gap
    for i in range(n):
        x = cx - w / 2 + i * (lado + gap)
        M.rrect(c, x, y, lado, lado, 10, BR, a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, lado, lado), 10, 10), M.paint(cor, a, stroke=4))
        M.line(c, x + 16, y + 16, x + lado - 16, y + lado - 16, cor, a, 6)
        M.line(c, x + lado - 16, y + 16, x + 16, y + lado - 16, cor, a, 6)


def tira(c, x, y, w, h, cor, a, p=1.0):
    """barra cheia de comprimento w (p = 0..1 cresce)"""
    if a <= 0 or p <= 0:
        return
    M.rrect(c, x, y, w * p, h, 14, cor, a)


BX, BY, BW, BH = 260, 450, 1400, 170
PESSOAS = (("Edu", 2, COR), ("Fabi", 3, TINTA), ("Gil", 4, LILAS))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1 = C["s01.a"], C["s01.b"]
    tf = (C["s01.c"], C["s01.d"], C["s01.e"])
    a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]

    def cena():
        E.frase(c, t, a1, ps("prêmio de", "i", 80) + [("R$ 2.340", "g", 92, COR)] + ps("para 3", "i", 80), W / 2, 170, "center", 0.12)
        E.frase(c, t, lerp(a1, b1, 0.55), ps("inversamente proporcional às faltas", "i", 62, TINTA2), W / 2, 270, "center", 0.08)
        E.frase(c, t, b1, ps("quem faltou menos", "i", 76) + [("leva mais", "g", 80, COR)], W / 2, 380, "center", 0.12)
        for (nome, n, cor), k, cx in zip(PESSOAS, tf, (420, 960, 1500)):
            E.foco(c, t, k, 0.5, lambda a, nome=nome, cx=cx, cor=cor: centro(c, nome, cx, 560, 80, "i", TINTA if cor == LILAS else cor, a))
            E.foco(c, t, k + 0.2, 0.5, lambda a, n=n, cx=cx: faltas(c, cx, 610, n, a))
            E.foco(c, t, k + 0.4, 0.5, lambda a, n=n, cx=cx: centro(c, f"{n} faltas", cx, 780, 60, "g", TINTA, a))
        E.frase(c, t, a2, ps("muita gente", "i", 76) + [("troca a ordem", "g", 80, ERRADO)] + ps("e erra", "i", 76), W / 2, 950, "center", 0.12)
    E.saida(c, t, b2 - 0.1, cena)

    if t >= b2:
        E.foco(c, t, c2 - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, c2 - 0.2, 0.7))), blur=0)
        E.frase(c, t, b2, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(b2, c2, 0.2), [("repartir", "g", 120, COR)] + ps("o prêmio", "i", 100), XE, 470, passo=0.14)
        E.frase(c, t, lerp(b2, c2, 0.45), ps("do", "i", 90) + [("jeito certo", "g", 96, COR)], XE, 610, passo=0.12)
        E.foco(c, t, c2 + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "dividir em partes", "diretamente proporcionais"), ("s03.c", "grandezas inversas:", "o produto não muda"),
             ("s03.d", "somar frações", "com o MMC"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 150 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
    alvo = [C[k] for k, _, _ in itens]
    q1, q2 = ease_io(prog(t, alvo[1] - 0.35, 0.5)), ease_io(prog(t, alvo[2] - 0.35, 0.5))
    py = lerp(lerp(320, 560, q1), 800, q2)
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.55), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56, TINTA2), x, 1000, "left", 0.1)


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]

    def inversa():
        E.frase(c, t, C["s04"] + 0.2, ps("dividir em partes", "i", 76), W / 2, 170, "center", 0.12)
        E.frase(c, t, a4, [("inversamente proporcionais", "g", 96, COR)], W / 2, 290, "center")
        E.frase(c, t, b4 - 0.6, ps("maior o número,", "i", 72) + [("menor a parte", "g", 76, COR)], W / 2, 410, "center", 0.12)
        x0, wb, h = 560, 1000, 110
        for y, k, rot, ww, lab in ((520, c4 - 0.8, "2 faltas", 1.0, None), (680, c4, "4 faltas", 0.5, "a metade"), (840, d4, "6 faltas", 1 / 3, "a terça parte")):
            E.foco(c, t, k, 0.4, lambda a, y=y, rot=rot: E.escreve(c, rot, x0 - 40 - E.larg(rot, "g", 56), y + 74, 56, "g", TINTA, a))
            tira(c, x0, y, wb * ww, h, COR, ep(t, k, 0.3), ep(t, k + 0.1, 0.7))
            if lab:
                E.foco(c, t, k + 0.6, 0.5, lambda a, y=y, ww=ww, lab=lab: E.escreve(c, lab, x0 + wb * ww + 30, y + 76, 62, "i", COR, a))
        E.foco(c, t, c4 - 0.4, 0.4, lambda a: E.escreve(c, "o dobro", x0 - 40 - E.larg("o dobro", "i", 44), 798, 44, "i", TINTA2, a))
        E.foco(c, t, d4 - 0.3, 0.4, lambda a: E.escreve(c, "o triplo", x0 - 40 - E.larg("o triplo", "i", 44), 958, 44, "i", TINTA2, a))
    E.saida(c, t, C["s05"] - 0.1, inversa)

    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    if C["s05"] <= t:
        def inversos():
            E.frase(c, t, C["s05"] + 0.2, ps("os pesos", "i", 76) + [("não", "g", 76, ERRADO)] + ps("são as faltas", "i", 76), W / 2, 180, "center", 0.12)
            for i, (n, cx) in enumerate(zip((2, 3, 4), (560, 960, 1360))):
                k = a5 - 0.9 + i * 0.15
                E.foco(c, t, k, 0.4, lambda a, n=n, cx=cx: centro(c, f"{n}", cx, 360, 90, "g", TINTA2, a))
                if t >= a5:
                    M.arrow(c, cx, 385, cx, 432, COR, ep(t, a5 + i * 0.4, 0.4), 5, 16, ep(t, a5 + i * 0.4, 0.4))
                E.foco(c, t, a5 + 0.2 + i * 0.4, 0.5, lambda a, n=n, cx=cx: E.fracao(c, 1, n, cx, 560, 110, COR, a))
            E.frase(c, t, b5, ps("inverso =", "i", 80) + [("1 ÷ o número", "g", 84, COR)], W / 2, 820, "center", 0.12)
            fcen(c, t, c5, "inverso de 2 = 1 ÷ 2 = f{1}{2}", W / 2, 990, 80, TINTA)
        E.saida(c, t, C["s06"] - 0.1, inversos)

    if t < C["s06"]:
        return
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    E.frase(c, t, C["s06"] + 0.2, ps("por que o", "i", 84) + [("inverso?", "g", 88, COR)], W / 2, 200, "center", 0.12)
    fcen(c, t, a6, "parte × faltas = sempre o mesmo", W / 2, 420, 84)
    fcen(c, t, b6, "parte = mesmo número ÷ faltas", W / 2, 620, 84, TINTA2)
    if t >= c6 - 0.6:
        E.formula_em(c, t, c6 - 0.6, "÷ 2", 560, 880, 130, "g", COR, "center")
        E.frase(c, t, c6 - 0.3, ps("é o mesmo que", "i", 76), W / 2, 870, "center", 0.1)
        E.formula_em(c, t, c6, "× f{1}{2}", 1360, 880, 130, "g", COR, "center")


# ---------------- tirar as frações ----------------
XS = (560, 960, 1360)


def b_pesos(c, t, C, b):
    a7, b7 = C["s07.a"], C["s07.b"]
    tk = (C["s07.c"], C["s07.d"], C["s07.e"])
    a8, b8 = C["s08.a"], C["s08.b"]
    E.frase(c, t, C["s07"] + 0.2, ps("peso em fração", "i", 70) + [("dá trabalho", "g", 70)], W / 2, 150, "center", 0.12)
    for i, (n, cx) in enumerate(zip((2, 3, 4), XS)):
        E.foco(c, t, C["s07"] + 0.4 + i * 0.12, 0.5, lambda a, n=n, cx=cx: E.fracao(c, 1, n, cx, 330, 110, COR, a))
    E.foco(c, t, a7, 0.5, lambda a: E.pilula(c, "MMC de 2, 3 e 4" + (" = 12" if t >= b7 else ""), W / 2, 540, 56, "g", a=a))
    for i, (cx, r, k, n) in enumerate(zip(XS, (6, 4, 3), tk, (2, 3, 4))):
        if t >= lerp(b7, tk[0], 0.5):
            p = ep(t, lerp(b7, tk[0], 0.5) + i * 0.1, 0.4)
            M.arrow(c, cx, 610, cx, 680, TINTA2, p, 4, 14, p)
            E.foco(c, t, lerp(b7, tk[0], 0.5) + i * 0.1, 0.4, lambda a, cx=cx: E.pilula(c, "× 12", cx + 90, 645, 38, "g", fundo=TINTA, a=a))
        E.foco(c, t, k, 0.5, lambda a, cx=cx, r=r: (E.bola(c, cx, 790, 80, a=a), centro(c, str(r), cx, 822, 92, "g", BR, a)))
        E.saida(c, t, a8 - 0.6, lambda cx=cx, n=n, r=r, k=k: fcen(c, t, k + 0.4, f"f{{1}}{{{n}}} de 12 = {r}", cx, 960, 52, TINTA2))
    E.frase(c, t, a8 - 0.5, [("× 12", "g", 60, COR)] + ps("em todos:", "i", 60) + [("a divisão não muda", "g", 60)], W / 2, 950, "center", 0.1)
    E.frase(c, t, b8 - 0.6, ps("vira uma divisão", "i", 60, TINTA2) + [("direta", "g", 60, COR)], W / 2, 1040, "center", 0.1)


# ---------------- a conta ----------------
def b_conta(c, t, C, b):
    a9, b9 = C["s09.a"], C["s09.b"]
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    troca(c, t, [(a9, "6 + 4 + 3 = 13", TINTA), (b9, "k = 2.340 ÷ 13 = 180", COR), (a0, "6 × 180 = 1.080", COR),
                 (b0, "4 × 180 = 720", TINTA), (c0, "3 × 180 = 540", TINTA)], W / 2, 290, 96)
    g = [(0, 6, COR, 1), (6, 10, TINTA, 1), (10, 13, LILAS, 1)]
    rot = [(i, "k", 1 - ep(t, b9, 0.3)) for i in range(13)] + [(i, "180", ep(t, b9 + 0.6 + i * 0.05, 0.4)) for i in range(13)]
    E.foco(c, t, C["s09"], 0.5, lambda a: partes(c, BX, BY, BW, BH, 13, g, a, rotulos=rot, size=44))
    for (nome, _, cor), (i0, i1), k, v in zip(PESSOAS, ((0, 6), (6, 10), (10, 13)), (a0, b0, c0), ("R$ 1.080", "R$ 720", "R$ 540")):
        grupo_rot(c, t, C["s09"] + 0.3, BX, BY + BH + 20, BW, 13, i0, i1, f"{nome}: peso {i1 - i0}", cor, k + 0.4, v, 66)


# ---------------- conferir ----------------
def b_confere(c, t, C, b):
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    fcen(c, t, a1, "1.080 + 720 + 540 = 2.340", W / 2, 210, 84, CERTO)
    E.foco(c, t, a1 + 1.4, 0.5, lambda a: E.selo(c, 1580, 182, 40, True, a))
    E.frase(c, t, b1, ps("parte × faltas =", "i", 72) + [("sempre o mesmo", "g", 76, COR)], W / 2, 360, "center", 0.12)
    for (nome, n, cor), k, conta, y in zip(PESSOAS, (c1, d1, e1), ("1.080 × 2 =", "720 × 3 =", "540 × 4 ="), (520, 670, 820)):
        E.foco(c, t, k, 0.5, lambda a, nome=nome, y=y, cor=cor: E.escreve(c, nome, 330, y, 66, "i", TINTA if cor == LILAS else cor, a))
        E.formula_em(c, t, k + 0.1, conta, 1140, y, 90, "g", TINTA, "right")
        E.formula_em(c, t, k + 0.8, "2.160", 1180, y, 90, "g", COR)
    if t >= e1 + 1.2:
        p = ep(t, e1 + 1.2, 0.5)
        E.caixa_pontilhada(c, 1160, 440, 320, 420, p, COR, prog_=p)
    E.frase(c, t, lerp(e1, C["s11.end"], 0.65), ps("é inversa", "i", 76) + [("de verdade", "g", 80, CERTO)], W / 2, 1000, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2, e2 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.end"]

    def errado():
        E.frase(c, t, C["s12"] + 0.2, ps("o erro:", "i", 76) + [("trocar a ordem", "g", 80, ERRADO)], W / 2, 160, "center", 0.12)
        fcen(c, t, a2, "faltas 2, 3, 4  →  pesos 4, 3, 2", W / 2, 280, 68, TINTA2)
        troca(c, t, [(b2, "4 + 3 + 2 = 9    k = 2.340 ÷ 9 = 260", ERRADO)], W / 2, 390, 68)
        g = [(0, 4, COR, 1), (4, 7, TINTA, 1), (7, 9, LILAS, 1)]
        rot = [(i, "260", ep(t, b2 + 0.8 + i * 0.05, 0.4)) for i in range(9)]
        E.foco(c, t, a2 + 0.4, 0.5, lambda a: partes(c, BX, BY, BW, BH, 9, g, a, rotulos=rot, size=54))
        for (nome, _, cor), (i0, i1), k, v in zip(PESSOAS, ((0, 4), (4, 7), (7, 9)), (c2, lerp(c2, e2, 0.4), lerp(c2, e2, 0.75)),
                                                 ("R$ 1.040", "R$ 780", "R$ 520")):
            grupo_rot(c, t, a2 + 0.6, BX, BY + BH + 20, BW, 9, i0, i1, nome, cor, k, v, 66)
    E.saida(c, t, C["s13"] - 0.1, errado)
    if t < C["s13"]:
        return
    a3, b3, c3, d3 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    E.frase(c, t, C["s13"] + 0.2, ps("parece certo...", "i", 70, TINTA2) + ps("teste o", "i", 70) + [("produto", "g", 72, COR)], W / 2, 180, "center", 0.12)
    fcen(c, t, a3, "1.040 × 2 = 2.080", W / 2, 360, 96)
    fcen(c, t, b3, "780 × 3 = 2.340", W / 2, 510, 96)
    E.frase(c, t, c3, ps("não deu o mesmo:", "i", 72) + [("não é inversa", "g", 76, ERRADO)], W / 2, 680, "center", 0.12)
    E.foco(c, t, c3 + 0.4, 0.5, lambda a: E.selo(c, 1580, 470, 54, False, a))
    E.foco(c, t, d3, 0.5, lambda a: E.pilula(c, "inverso = 1 ÷ o número", W / 2, 860, 66, "g", a=a))
    E.frase(c, t, d3 + 0.8, ps("não é trocar a ordem", "i", 60, ERRADO), W / 2, 1000, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4, e4 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.end"]

    def um():
        E.frase(c, t, C["s14"] + 0.1, ps("agora, o atalho", "i", 70, CLARO), W / 2, 160, "center", 0.12)
        E.frase(c, t, a4, [("MMC ÷ cada número", "g", 92, BR)] + ps("= o peso", "i", 88, CLARO), W / 2, 300, "center", 0.12)
        for k, s, y in ((b4, "12 ÷ 2 = 6", 470), (c4, "12 ÷ 3 = 4", 620), (d4, "12 ÷ 4 = 3", 770)):
            fcen(c, t, k, s, W / 2, y, 100, BR)
        E.frase(c, t, lerp(d4, e4, 0.55), ps("sem escrever", "i", 70, CLARO) + [("fração nenhuma", "g", 72, BR)], W / 2, 940, "center", 0.12)
    E.saida(c, t, C["s15"] - 0.1, um)
    if t < C["s15"]:
        return
    a5, b5, c5, d5, e5 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.end"]
    fcen(c, t, a5, "f{1}{2} de 12 = 12 ÷ 2", W / 2, 230, 96, CLARO)
    E.frase(c, t, b5, ps("com", "i", 76, CLARO) + [("2 pessoas,", "g", 80, BR)] + ps("mais fácil ainda", "i", 76, CLARO), W / 2, 420, "center", 0.12)
    E.linha(c, t, [("inversa a", "i", 76, CLARO, c5 - 1.2), ("2 e 3", "g", 92, BR, c5 - 0.9), ("=", "g", 92, CLARO, c5 - 0.3),
                   ("direta a", "i", 76, CLARO, c5), ("3 e 2", "g", 92, BR, c5 + 0.3)], W / 2, 580, "center")
    E.foco(c, t, d5, 0.5, lambda a: E.selo(c, 330, 750, 50, False, a))
    E.frase(c, t, d5 + 0.1, ps("trocar a ordem:", "i", 72, CLARO) + [("só com 2 pessoas", "g", 76, BR)], 420, 775, "left", 0.1)
    E.frase(c, t, lerp(d5, e5, 0.5), ps("com 3 ou mais,", "i", 70, CLARO) + [("é o erro", "g", 74, ERRADO)], 420, 920, "left", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a6, b6, c6, d6 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a6 - 0.3, ps("a avó divide", "i", 80) + [("R$ 1.800", "g", 84, COR)], XE, 340, passo=0.12)
    E.frase(c, t, a6 + 0.6, ps("entre 3 netos", "i", 80), XE, 450, passo=0.12)
    E.frase(c, t, b6, [("inversa à idade", "g", 84)], XE, 580, passo=0.12)
    E.linha(c, t, [("idades:", "i", 80, TINTA, c6 - 0.3), ("3,", "g", 92, COR, c6), ("4", "g", 92, COR, lerp(c6, d6, 0.35)),
                   ("e 6 anos", "g", 84, COR, lerp(c6, d6, 0.65))], XE, 710)
    E.frase(c, t, d6, ps("quanto recebe", "i", 96) + [("cada neto?", "g", 100, COR)], XE, 880, passo=0.12)
    E.relogio(c, t, C["s17.a"], 1590, 430, 170)


# ---------------- resposta ----------------
NETOS = (("3 anos", 3, 4, COR), ("4 anos", 4, 3, TINTA), ("6 anos", 6, 2, LILAS))


def b_resposta(c, t, C, b):
    a8, b8, c8, d8 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]

    def pesos():
        E.foco(c, t, a8, 0.5, lambda a: E.pilula(c, "MMC de 3, 4 e 6 = 12", W / 2, 180, 60, "g", a=a))
        for i, ((nome, n, p, cor), cx) in enumerate(zip(NETOS, XS)):
            k = b8 - 0.6 + i * 0.5
            E.foco(c, t, b8 - 1.2, 0.5, lambda a, nome=nome, cx=cx, cor=cor: centro(c, nome, cx, 380, 64, "i", TINTA if cor == LILAS else cor, a))
            fcen(c, t, k, f"12 ÷ {n}", cx, 510, 84, TINTA2)
            E.foco(c, t, k + 0.4, 0.5, lambda a, cx=cx, p=p, cor=cor: (E.bola(c, cx, 640, 74, cor, a), centro(c, str(p), cx, 670, 86, "g", BR, a)))
        fcen(c, t, c8, "4 + 3 + 2 = 9", W / 2, 840, 84)
        fcen(c, t, d8, "k = 1.800 ÷ 9 = 200", W / 2, 980, 90, COR)
    E.saida(c, t, C["s19"] - 0.1, pesos)
    if t < C["s19"]:
        return
    a9, b9, c9, d9, e9 = (C[f"s19.{k}"] for k in "abcde")
    troca(c, t, [(C["s19"], "k = 200", COR), (a9, "4 × 200 = 800", COR), (d9, "800 + 600 + 400 = 1.800", CERTO)], W / 2, 290, 96)
    E.foco(c, t, d9 + 1.2, 0.5, lambda a: E.selo(c, 1620, 260, 42, True, a))
    g = [(0, 4, COR, 1), (4, 7, TINTA, 1), (7, 9, LILAS, 1)]
    rot = [(i, "200", 1) for i in range(9)]
    E.foco(c, t, C["s19"], 0.5, lambda a: partes(c, BX, BY, BW, BH, 9, g, a, rotulos=rot, size=54))
    for (nome, _, p, cor), (i0, i1), k, v in zip(NETOS, ((0, 4), (4, 7), (7, 9)), (a9, b9, c9), ("R$ 800", "R$ 600", "R$ 400")):
        grupo_rot(c, t, C["s19"] + 0.3, BX, BY + BH + 20, BW, 9, i0, i1, nome, cor, k + 0.3, v, 66)
    fcen(c, t, e9, "800 × 3 = 600 × 4 = 400 × 6 = 2.400", W / 2, 1020, 60, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s20.a", "inversa aos números", "= direta aos inversos"), ("s20.b", "MMC ÷ cada número", "= os pesos"),
                 ("s20.c", "o resto é", "o k de sempre"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 72) + [(l2, "g", 72, COR)], 320, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, a1, [("taxas", "g", 130, COR)], XE, 400, passo=0.12)
    E.frase(c, t, lerp(a1, b1, 0.3), ps("km por litro, R$ por quilo", "i", 70), XE, 510, passo=0.1)
    E.frase(c, t, b1, ps("e a", "i", 76) + [("velocidade média", "g", 80, COR)], XE, 620, passo=0.12)
    E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c1 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1020, 815, p), ep(t, c1 + 0.2, 0.4))
    E.frase(c, t, d1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, pesos=b_pesos, conta=b_conta, confere=b_confere, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
