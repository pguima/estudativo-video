"""Visual — Estudativo · MAT-FRA-011: dividir frações.
A alma da aula são os litros e as garrafas: cada litro é uma barra (E.barra) que a lâmina corta em copos, e os pedaços viram
tabletes (E.chocolate) que se contam e se juntam em garrafas. A fração que vira de cabeça para baixo é a peça local vira()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, palco, frac_q, centro, barra
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-011_dividir_fracoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("cabe", "garrafas", "regra", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NY, DY = -0.565, 0.535  # centro do número de cima e do de baixo, em relação ao centro de uma fração de tamanho s

assert 12 // 3 == 4 and 3 * 4 == 12 and 6 * 3 == 18 and 18 // 2 == 9 and 6 // 2 == 3 and 3 * 3 == 9
assert 2 * 7 == 14 and 3 * 5 == 15 and 14 * 5 * 3 == 2 * 15 * 7  # 14/15 × 5/7 = 2/3
assert 3 * 4 == 12 and 8 // 4 == 2 and 4 // 4 == 1 and 3 * 2 == 6
assert 4 // 2 == 2 and 15 // 5 == 3 and 2 * 3 == 6 and 6 * 2 == 12 and 12 * 5 == 4 * 15


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


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    """número dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def conta(c, t, ti, s, x, y, size=64, cor=None, est="b"):
    E.foco(c, t, ti, 0.45, lambda a: E.escreve(c, s, x, y, size, est, cor or TINTA, a))


def conta_c(c, t, ti, s, cx, y, size=64, cor=None, est="b"):
    E.foco(c, t, ti, 0.45, lambda a: centro(c, s, cx, y, size, est, cor or TINTA, a))


def corte(c, t, t0, cx, cy, s, novo, tn, baixo=False, risco=None, tinta=None):
    """corte em cruz no número centrado em (cx, cy): embaixo da fração, o valor novo desce para não bater no traço"""
    E.corta(c, t, t0, cx, cy, s, None, risco or COR)
    yb = cy + s * 0.8 if baixo else cy - s * 0.5
    E.foco(c, t, tn, 0.4, lambda a: E.escreve(c, str(novo), cx + s * 0.38, yb, s * 0.56, "g", tinta or COR, a), sobe=8)


def vira(c, t, t0, n, d, cx, cy, s, cor=None, ti=None):
    """a fração vira de cabeça para baixo: os dois números trocam de lugar, cada um por um lado do traço"""
    cor = cor or TINTA

    def fn(a):
        q = ease_io(prog(t, t0, 0.9))
        n_, d_ = str(n), str(d)
        lw = max(E.larg(n_, "g", s), E.larg(d_, "g", s)) + s * 0.2
        arco = math.sin(q * math.pi) * s * 0.85
        E.escreve(c, n_, cx - E.larg(n_, "g", s) / 2 + arco, lerp(cy - s * 0.2, cy + s * 0.9, q), s, "g", cor, a)
        E.escreve(c, d_, cx - E.larg(d_, "g", s) / 2 - arco, lerp(cy + s * 0.9, cy - s * 0.2, q), s, "g", cor, a)
        b = s * 0.085
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - lw / 2, cy - b / 2 + s * 0.03, lw, b), b / 2, b / 2), M.paint(cor, a))
    E.foco(c, t, ti if ti is not None else t0 - 0.5, 0.45, fn)


def litro(c, x, y, w, h, n, p, a=1.0, cor=None):
    """um litro de suco: barra cheia, com a lâmina cortando em n partes (p = 0..1)"""
    barra(c, x, y, w, h, 1.0, [(i / n, p) for i in range(1, n)], a, cor)


# ---------------- gancho ----------------
X3, W3, G3 = 170, 480, 40  # três litros em fila


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]
    a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]

    def cena():
        y, h = 350, 170
        E.frase(c, t, a1, ps("3 litros", "g", 96, COR) + ps("de suco", "i", 104), XE, 180)
        for i in range(3):
            x = X3 + i * (W3 + G3)
            E.foco(c, t, a1 + i * 0.2, 0.5, lambda p, x=x: litro(c, x, y, W3, h, 4, ep(t, b1 + 0.2, 0.7), p))
        E.frase(c, t, b1, ps("copos de", "i", 92), XE, 680)
        fr(c, t, b1 + 0.4, 1, 4, 620, 650, 110, COR)
        E.frase(c, t, b1 + 0.7, ps("de litro", "i", 92), 700, 680)
        E.frase(c, t, c1, ps("quantos copos", "g", 108, COR) + ps("você enche?", "i", 116), XE, 880)
    E.saida(c, t, C["s02"] - 0.1, cena)

    if C["s02"] <= t < C["s03"] + 0.3:
        def cena2():
            y = 330
            E.foco(c, t, a2, 0.45, lambda p: E.escreve(c, "3", 400, y + 60, 170, "g", TINTA, p))
            sinal(c, t, a2 + 0.3, "÷", 620, y - 15, 130)
            fr(c, t, a2 + 0.6, 1, 4, 800, y, 170, COR)
            sinal(c, t, b2 - 0.2, "=", 1000, y - 15, 130)
            E.foco(c, t, b2, 0.5, lambda p: num_bola(c, "12", 1230, y, 150, 150, p, CERTO, BR))
            E.frase(c, t, c2 - 0.8, ps("você dividiu,", "i", 100) + ps("e o número", "i", 100), W / 2, 650, "center")
            E.frase(c, t, c2, ps("cresceu", "g", 190, COR), W / 2, 830, "center")
            E.frase(c, t, lerp(c2, C["s02.end"], 0.45), ps("parece errado,", "i", 76) + ps("mas está certo", "g", 70, CERTO), W / 2, 960, "center")
        E.saida(c, t, C["s03"] - 0.1, cena2)

    if t >= C["s03"]:
        a3, b3 = C["s03.a"], C["s03.b"]
        E.foco(c, t, b3 - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, b3 - 0.2, 0.7))), blur=0)
        E.frase(c, t, a3, ps("até o fim da aula", "i", 96), XE, 340)
        E.frase(c, t, lerp(a3, b3, 0.25), ps("entender", "g", 120) + ps("por quê", "i", 120, COR), XE, 500)
        E.frase(c, t, lerp(a3, b3, 0.6), ps("dividir", "g", 120) + ps("quaisquer", "i", 104) , XE, 640)
        E.frase(c, t, lerp(a3, b3, 0.72), ps("frações", "g", 120, COR), XE, 770)
        E.foco(c, t, b3 + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", E.SOBRE, a), E.escreve(c, "de prova", 1310, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, f_ = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.end"]
    E.frase(c, t, lerp(C["s04"], a_, 0.4), ps("você só precisa de", "i", 84), XE, 410)
    E.foco(c, t, a_, 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, a_ + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 225, 700, 120, "i", TINTA, a))
    x, w = 860, 890
    p = ep(t, b_, 0.5)
    E.caixa_pontilhada(c, x, 180, w, 480, p, prog_=p)
    E.frase(c, t, b_ + 0.1, ps("multiplicar frações", "g", 74, COR), x + 44, 285)
    E.frase(c, t, lerp(b_, c_, 0.1), ps("numerador vezes numerador", "i", 64), x + 44, 385, passo=0.26)
    E.frase(c, t, lerp(b_, c_, 0.5), ps("denominador vezes denominador", "i", 64), x + 44, 470, passo=0.26)
    E.frase(c, t, c_, ps("cortar em cruz", "g", 66, COR) + ps("quando der", "i", 70), x + 44, 600, passo=0.26)
    E.frase(c, t, lerp(c_, f_, 0.5), ps("faltou?", "g", 60, COR) + ps("procure a aula no canal", "i", 66), W / 2, 880, "center", 0.26)


# ---------------- quantas vezes cabe ----------------
def b_cabe(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]

    def doze():
        E.frase(c, t, C["s05"] + 0.1, ps("o que dividir", "i", 88) + ps("quer dizer?", "g", 80, COR), W / 2, 170, "center")
        conta_c(c, t, a5, "12 ÷ 3", W / 2, 320, 120, TINTA, "g")
        x, y, w, h = 216, 400, 1488, 150
        lp = w / 12
        ped = [(i, E.COR if (i // 3) % 2 == 0 else CLARO, ep(t, a5 + 0.2 + i * 0.04, 0.3)) for i in range(12)]
        E.foco(c, t, a5 + 0.1, 0.5, lambda p: E.chocolate(c, x, y, w, h, 12, ped, p))
        E.frase(c, t, b5, ps("quantas vezes o", "i", 76) + ps("3", "g", 76, COR) + ps("cabe no", "i", 76) + ps("12?", "g", 76, COR), W / 2, 725, "center", 0.26)
        for k in range(4):
            ti = lerp(b5, c5, 0.5 + k * 0.12)
            E.chave(c, x + 3 * k * lp + 6, x + 3 * (k + 1) * lp - 6, y + h + 10, TINTA2, ep(t, ti, 0.3), 16, 4)
            conta_c(c, t, ti, str(k + 1), x + (3 * k + 1.5) * lp, y + h + 74, 48, TINTA2)
        E.foco(c, t, c5, 0.5, lambda p: num_bola(c, "4", W / 2 - 150, 860, 80, 100, p, CERTO, BR))
        E.frase(c, t, c5 + 0.2, ps("vezes", "i", 96), W / 2 - 40, 890)
        E.frase(c, t, lerp(c5, C["s05.end"], 0.45), ps("com fração,", "i", 66) + ps("a pergunta é a mesma", "g", 60, COR), W / 2, 1010, "center", 0.26)
    E.saida(c, t, C["s06"] - 0.1, doze)

    if t >= C["s06"]:
        a6, b6, c6, a7, b7, c7, f7 = C["s06.a"], C["s06.b"], C["s06.c"], C["s07.a"], C["s07.b"], C["s07.c"], C["s07.end"]
        y, h = 300, 170
        q = ease_io(prog(t, a7 - 0.3, 0.8))  # o litro encolhe para dar lugar aos outros dois
        x1, w1 = lerp(410, X3, q), lerp(1100, W3, q)
        tlab = C["s07"]
        E.saida(c, t, tlab - 0.2, lambda: E.frase(c, t, a6, ps("quantas vezes", "i", 76) + ps("1/4 de litro", "g", 72, COR) + ps("cabe em", "i", 76) + ps("3 litros?", "g", 72, COR), W / 2, 170, "center", 0.26))
        E.foco(c, t, b6, 0.5, lambda p: litro(c, x1, y, w1, h, 4, ep(t, c6 - 0.3, 0.7), p))
        E.saida(c, t, a7 - 0.3, lambda: conta_c(c, t, b6, "1 litro", W / 2, 560, 76, TINTA))
        E.saida(c, t, a7 - 0.3, lambda: conta_c(c, t, c6, "rende 4 copos", W / 2, 660, 84, COR, "g"))
        for i in range(1, 3):
            x = X3 + i * (W3 + G3)
            E.foco(c, t, a7 + (i - 1) * 0.2, 0.5, lambda p, x=x: litro(c, x, y, W3, h, 4, 1.0, p))
        # os copos contados
        for i in range(12):
            bar, pos = i // 4, i % 4
            lp = (w1 if bar == 0 else W3) / 4
            x0 = x1 if bar == 0 else X3 + bar * (W3 + G3)
            ti = c6 + pos * 0.12 if bar == 0 else b7 + (i - 4) * 0.05
            conta_c(c, t, ti, str(i + 1), x0 + (pos + 0.5) * lp, y + h / 2 + 22, 62, E.SOBRE, "g")
        conta_c(c, t, a7, "3 × 4", 620, 620, 110, TINTA, "g")
        sinal(c, t, b7 - 0.2, "=", 810, 585, 100)
        E.foco(c, t, b7, 0.5, lambda p: E.escreve(c, "12 copos", 880, 620, 110, "g", CERTO, p))
        y2 = 740
        E.frase(c, t, c7 - 0.5, ps("dividir por", "i", 80), 300, y2 + 26)
        fr(c, t, c7, 1, 4, 700, y2, 96, COR)
        sinal(c, t, c7 + 0.3, "=", 800, y2 - 15, 84)
        E.frase(c, t, c7 + 0.5, ps("multiplicar por", "i", 80), 860, y2 + 26)
        E.foco(c, t, c7 + 0.9, 0.45, lambda p: E.escreve(c, "4", 1345, y2 + 34, 110, "g", COR, p))
        E.frase(c, t, lerp(c7, f7, 0.5), ps("o copo é menor que um litro,", "i", 62) + ps("cabe muitas vezes", "g", 58, COR), W / 2, 890, "center", 0.26)
        E.frase(c, t, lerp(c7, f7, 0.8), ps("por isso", "i", 72) + ps("o número cresceu", "g", 68, COR), W / 2, 990, "center", 0.26)


# ---------------- garrafas ----------------
X6, W6, G6 = 150, 240, 20  # seis litros em fila
Y6, H6 = 300, 150


def b_garrafas(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9, f9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.end"]
    E.saida(c, t, C["s09"] - 0.1, lambda: E.frase(c, t, C["s08"] + 0.1, ps("e se o de cima", "i", 84) + ps("não for 1?", "g", 78, COR), W / 2, 150, "center"))
    E.frase(c, t, C["s09"] + 0.1, ps("mas", "i", 84) + ps("2/3", "g", 80, COR) + ps("é", "i", 84) + ps("o dobro", "g", 80, COR) + ps("de", "i", 84) + ps("1/3", "g", 80, COR), W / 2, 150, "center")
    tc = lerp(b8, c8, 0.6)  # "cada litro encheria três"
    separa = t >= tc + 0.7
    for i in range(6):
        x = X6 + i * (W6 + G6)
        E.foco(c, t, a8 + i * 0.1, 0.5, lambda p, x=x, i=i: litro(c, x, Y6, W6, H6, 3, ep(t, tc, 0.7), p) if not separa else None)
    conta_c(c, t, a8, "6 litros", W / 2, 262, 56, TINTA2)
    if separa:
        forma = ep(t, a9 + 0.2, 0.6)  # as garrafas: dois terços de cada vez
        for bar in range(6):
            x = X6 + bar * (W6 + G6)
            ped = []
            for j in range(3):
                k = (bar * 3 + j) // 2
                ped.append((j, M.mix(E.COR, E.COR if k % 2 == 0 else CLARO, forma), 1.0))
            E.chocolate(c, x, Y6, W6, H6, 3, ped)
        for k in range(9):
            ti = b9 + k * 0.1
            i0 = 2 * k
            xa = X6 + (i0 // 3) * (W6 + G6) + (i0 % 3) * W6 / 3
            i1 = i0 + 1
            xb = X6 + (i1 // 3) * (W6 + G6) + (i1 % 3 + 1) * W6 / 3
            E.chave(c, xa + 6, xb - 6, Y6 + H6 + 10, TINTA2, ep(t, ti, 0.3), 16, 4)
            conta_c(c, t, ti, str(k + 1), (xa + xb) / 2, Y6 + H6 + 76, 50, COR, "g")

    def primeira():
        y = 590
        E.frase(c, t, b8, ps("garrafas de", "i", 84), XE, y + 28)
        fr(c, t, b8 + 0.4, 2, 3, 650, y, 110, COR)
        E.frase(c, t, b8 + 0.7, ps("de litro", "i", 84), 730, y + 28)
        E.frase(c, t, lerp(b8, c8, 0.3), ps("se fosse de", "i", 76), XE, 812)
        fr(c, t, lerp(b8, c8, 0.42), 1, 3, 590, 787, 96, COR)
        E.frase(c, t, lerp(b8, c8, 0.5), ps("cada litro encheria 3", "g", 66), 670, 812)
        conta_c(c, t, c8, "6 × 3 = 18 garrafas", W / 2, 985, 90, COR)
    E.saida(c, t, a9, primeira)

    if t >= b9 - 0.3:
        conta_c(c, t, b9, "18 ÷ 2 = 9 garrafas", W / 2, 700, 90, CERTO)
        conta_c(c, t, lerp(a9, b9, 0.5), "cabe metade", W / 2, 600, 66, TINTA2, "i")
        E.frase(c, t, c9, ps("× 3", "g", 76, COR) + ps("o de baixo", "i", 72), XE, 835)
        E.frase(c, t, d9, ps("÷ 2", "g", 76, COR) + ps("o de cima", "i", 72), XE, 960)
        E.frase(c, t, lerp(d9, f9, 0.3), ps("quantos pedaços cabem em um inteiro", "i", 54), 730, 835, passo=0.26)
        E.frase(c, t, lerp(d9, f9, 0.65), ps("quantos pedaços formam uma garrafa", "i", 54), 730, 960, passo=0.26)


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    a0, b0, c0, d0, e0, f0, g0 = (C[f"s10.{k}"] for k in "abcdefg")
    tfim = lerp(d0, e0, 0.34)

    def parte_a():
        y = 270
        conta(c, t, C["s10"] + 0.2, "× 3 e ÷ 2", 260, y + 30, 92, TINTA, "g")
        sinal(c, t, a0 - 0.2, "=", 860, y - 15, 100)
        conta(c, t, a0, "×", 960, y + 30, 92, COR, "g")
        vira(c, t, b0, 2, 3, 1140, y, 150, COR, ti=a0)
        E.frase(c, t, b0 + 0.7, ps("de cabeça", "i", 64), 1340, y - 10)
        E.frase(c, t, b0 + 0.9, ps("para baixo", "g", 58, COR), 1340, y + 66)
        y2 = 640
        fr(c, t, c0, 3, 2, 300, y2, 130, COR)
        E.foco(c, t, c0 + 0.2, 0.45, lambda p: E.escreve(c, "de", 390, y2 + 34, 110, "i", TINTA, p))
        E.foco(c, t, c0 + 0.4, 0.45, lambda p: E.escreve(c, "6", 530, y2 + 44, 130, "g", TINTA, p))
        conta(c, t, lerp(c0, d0, 0.35), "6 ÷ 2 = 3", 760, y2 - 16, 80, TINTA)
        conta(c, t, lerp(c0, d0, 0.8), "3 × 3 =", 760, y2 + 80, 80, TINTA)
        E.foco(c, t, d0, 0.5, lambda p: num_bola(c, "9", 1200, y2 + 52, 76, 96, p, CERTO, BR))
        E.frase(c, t, d0 + 0.2, ps("garrafas", "g", 72, CERTO), 1300, y2 + 76)
        E.frase(c, t, lerp(d0, e0, 0.08), ps("de cima maior?", "i", 74) + ps("é só um passo da conta", "g", 66, COR), W / 2, 880, "center", 0.26)
    E.saida(c, t, tfim, parte_a)

    if t >= tfim:
        E.frase(c, t, tfim + 0.1, ps("só a garrafa", "g", 92, COR) + ps("decidiu a conta", "i", 100), W / 2, 200, "center")
        E.frase(c, t, lerp(d0, e0, 0.53), ps("antes do sinal de dividir,", "i", 66) + ps("inteiro ou fração:", "g", 60) + ps("o caminho é o mesmo", "i", 66), W / 2, 320, "center", 0.26)
        for i, (ti, s, y) in enumerate(((e0, "conserva a primeira", 520), (f0, "vira a segunda", 700), (g0, "multiplica", 880))):
            E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 460, y - 34, 62, 72, a))
            pal = s.split(" ", 1)
            E.frase(c, t, ti + 0.1, ps(pal[0], "g", 110, COR) + (ps(pal[1], "i", 110) if len(pal) > 1 else []), 560, y)


def b_regra2(c, t, C, b):
    a1, b1, c1, d1 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    a2, b2, c2, d2, e2, f2 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"], C["s12.end"]

    def usar():
        y, s = 300, 160
        E.frase(c, t, C["s11"] + 0.1, ps("vamos usar", "i", 72, COR), XE, 150)
        fr(c, t, a1, 2, 3, 700, y, s)
        sinal(c, t, a1 + 0.3, "÷", 890, y - 15, 120)
        fr(c, t, a1 + 0.6, 5, 7, 1080, y, s)
        y2 = 760
        conta_c(c, t, b1, "conserva", 700, y2 - 200, 58, COR)
        fr(c, t, b1, 2, 3, 700, y2, s, COR)
        conta_c(c, t, c1 - 0.5, "vira a segunda", 1120, y2 - 200, 58, COR)
        vira(c, t, c1, 5, 7, 1080, y2, s, COR, ti=c1 - 0.5)
        if t < d1:
            sinal(c, t, c1 - 0.5, "÷", 890, y2 - 15, 120, CINZA)
        sinal(c, t, d1, "×", 890, y2 - 15, 130, COR)
        conta_c(c, t, d1, "troca o sinal", 1420, y2 + 20, 58, COR)
    E.saida(c, t, C["s12"] - 0.1, usar)

    if t >= C["s12"]:
        y, s = 280, 140
        fr(c, t, C["s12"], 2, 3, 300, y, s)
        sinal(c, t, C["s12"] + 0.1, "×", 450, y - 15, 110)
        fr(c, t, C["s12"] + 0.2, 7, 5, 600, y, s)
        sinal(c, t, c2 - 0.2, "=", 770, y - 15, 110)
        fr(c, t, c2, 14, 15, 960, y, s, COR)
        conta(c, t, a2, "2 × 7 = 14", 1190, y - 30, 72, TINTA)
        conta(c, t, b2, "3 × 5 = 15", 1190, y + 74, 72, TINTA)
        E.frase(c, t, lerp(c2, d2, 0.1), ps("deu", "i", 80) + ps("menos que 1:", "g", 74, COR), XE, 540, passo=0.26)
        E.frase(c, t, lerp(c2, d2, 0.3), ps("5/7", "g", 66, COR) + ps("não chega a caber uma vez inteira em", "i", 68) + ps("2/3", "g", 66, COR), XE, 640, passo=0.26)
        E.frase(c, t, lerp(c2, d2, 0.7), ps("multiplicar desfaz a divisão", "g", 68), XE, 760, passo=0.26)
        y2, s2 = 900, 110
        fr(c, t, d2, 14, 15, 280, y2, s2, COR)
        sinal(c, t, d2 + 0.3, "×", 410, y2 - 15, 90)
        fr(c, t, d2 + 0.6, 5, 7, 530, y2, s2)
        sinal(c, t, e2 - 0.2, "=", 660, y2 - 15, 90)
        fr(c, t, e2, 2, 3, 780, y2, s2, CERTO)
        E.foco(c, t, e2 + 0.2, 0.45, lambda p: E.selo(c, 930, y2, 54, True, p))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a3, b3, c3, d3 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    a4, b4, f4 = C["s14.a"], C["s14.b"], C["s14.end"]
    E.frase(c, t, C["s13"] + 0.1, ps("o erro mais comum", "i", 88), XE, 170)
    E.frase(c, t, a3, ps("virar a fração errada", "g", 100, ERRADO), XE, 290)
    y, s = 500, 140

    def conta_errada():
        tv = lerp(a3, b3, 0.45)
        E.foco(c, t, tv, 0.45, lambda p: E.escreve(c, "3", 200, y + 52, 140, "g", TINTA, p))
        sinal(c, t, tv + 0.2, "÷", 365, y - 15, 110)
        fr(c, t, tv + 0.4, 1, 4, 490, y, s, COR)
        sinal(c, t, b3 - 0.2, "=", 625, y - 15, 110)
        fr(c, t, b3, 3, 1, 750, y, s)
        sinal(c, t, b3 + 0.3, "÷", 880, y - 15, 110)
        fr(c, t, b3 + 0.5, 1, 4, 1010, y, s, COR)
    conta_errada()
    y2 = 770
    conta(c, t, c3 - 0.1, "vira o 3:", XE, y2 + 26, 62, ERRADO)
    fr(c, t, c3, 1, 3, 540, y2, s, ERRADO)
    sinal(c, t, c3 + 0.3, "×", 670, y2 - 15, 110)
    fr(c, t, c3 + 0.5, 1, 4, 800, y2, s, COR)
    sinal(c, t, d3 - 0.2, "=", 935, y2 - 15, 110)
    fr(c, t, d3, 1, 12, 1060, y2, s, ERRADO)
    if t >= a4 + 0.6:
        E.risco(c, 960, y2 + 125, 1160, y2 - 110, t, a4 + 0.6, largura=14)
    E.frase(c, t, a4, ps("menos de um copo", "g", 62, ERRADO), 1210, 450)
    E.frase(c, t, a4 + 0.8, ps("em 3 litros?", "i", 72), 1210, 545)
    E.frase(c, t, lerp(a4, b4, 0.75), ps("não faz sentido", "i", 64), 1210, 635)
    E.frase(c, t, b4, ps("a que vira é", "i", 66) + ps("a segunda", "g", 60, CERTO), 1210, 780, passo=0.26)
    E.frase(c, t, b4 + 1.0, ps("depois do sinal", "i", 64), 1210, 870, passo=0.26)
    E.frase(c, t, b4 + 1.5, ps("de dividir", "i", 64), 1210, 950, passo=0.26)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def parte15():
        a_, b_, c_, d_ = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
        E.frase(c, t, C["s15"] + 0.1, ps("agora, o atalho", "i", 78, CLARO), W / 2, 160, "center")
        E.frase(c, t, a_, ps("fração com", "i", 110, BR) + ps("1 em cima", "g", 104, BR), W / 2, 300, "center")
        s = 84
        for i, (ti, n, d, r, extra) in enumerate(((b_, 1, 2, "× 2", "é dobrar"), (c_, 1, 3, "× 3", ""), (d_, 1, 4, "× 4", ""))):
            y = 470 + i * 178
            E.foco(c, t, ti, 0.45, lambda p, y=y: E.escreve(c, "÷", 520, y + 40, 110, "g", BR, p))
            fr(c, t, ti + 0.1, n, d, 690, y, s, BR)
            sinal(c, t, ti + 0.3, "=", 840, y - 15, 100, BR)
            E.foco(c, t, ti + 0.4, 0.45, lambda p, r=r, y=y: E.escreve(c, r, 920, y + 40, 110, "g", CLARO, p))
            if extra:
                conta(c, t, ti + 0.6, extra, 1240, y + 30, 76, BR, "i")
    E.saida(c, t, C["s16"] - 0.1, parte15)

    if C["s16"] <= t < C["s17"] + 0.3:
        a_, b_, c_, f_ = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.end"]

        def parte16():
            E.frase(c, t, C["s16"] + 0.1, ps("funciona porque", "i", 80, CLARO), W / 2, 170, "center")
            E.frase(c, t, a_, ps("um inteiro tem", "i", 92, BR) + ps("4 quartos", "g", 88, CLARO), W / 2, 300, "center")
            x, y, w, h = 410, 360, 1100, 170
            ped = [(i, CLARO, ep(t, a_ + 0.4 + i * 0.2, 0.4)) for i in range(4)]
            E.foco(c, t, a_ + 0.2, 0.5, lambda p: E.chocolate(c, x, y, w, h, 4, ped, p, 1.0, True))
            for i in range(4):
                conta_c(c, t, a_ + 0.5 + i * 0.2, str(i + 1), x + w * (i + 0.5) / 4, y + h / 2 + 30, 84, TINTA, "g")
            E.frase(c, t, lerp(a_, b_, 0.45), ps("cada unidade", "i", 76, BR) + ps("rende 4", "g", 72, CLARO), W / 2, 640, "center")
            E.frase(c, t, lerp(a_, b_, 0.75), ps("não compensa quando o de cima não é 1,", "i", 62, CLARO), W / 2, 770, "center", 0.26)
            fr(c, t, b_, 5, 7, 620, 890, 100, BR)
            E.frase(c, t, c_, ps("conserva,", "g", 66, BR) + ps("vira", "g", 66, BR) + ps("e multiplica", "g", 66, BR), 740, 915)
        E.saida(c, t, C["s17"] - 0.1, parte16)

    if t >= C["s17"]:
        a_, b_, c_, d_, e_, f_ = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"], C["s17.e"], C["s17.end"]
        E.frase(c, t, C["s17"] + 0.1, ps("veja em ação", "i", 72, CLARO), XE, 150)
        linha_y = 290
        fr(c, t, a_, 3, 4, 300, linha_y, 120, BR)
        E.frase(c, t, a_ + 0.4, ps("de litro,", "i", 76, BR), 400, linha_y + 28)
        E.frase(c, t, b_ - 0.4, ps("doses de", "i", 76, BR), 740, linha_y + 28)
        fr(c, t, b_, 1, 8, 1120, linha_y, 120, CLARO)
        E.frase(c, t, b_ + 0.4, ps("de litro", "i", 76, BR), 1220, linha_y + 28)
        x, y, w, h = 300, 440, 1320, 150
        ped = [(i, CLARO, ep(t, a_ + 0.3 + i * 0.1, 0.4)) for i in range(6)]
        E.foco(c, t, a_ + 0.2, 0.5, lambda p: E.chocolate(c, x, y, w, h, 8, ped, p, ep(t, b_, 0.8), True))
        for i in range(6):
            conta_c(c, t, e_ + i * 0.1, str(i + 1), x + w * (i + 0.5) / 8, y + h / 2 + 28, 76, TINTA, "g")
        yc, s = 815, 150
        fr(c, t, c_ - 0.4, 3, 4, 400, yc, s, BR)
        sinal(c, t, c_ - 0.2, "×", 570, yc - 15, 110, BR)
        E.foco(c, t, c_, 0.45, lambda p: E.fracao(c, 8, 1, 730, yc, s, CLARO, p))
        corte(c, t, lerp(d_, e_, 0.35), 730, yc + s * NY, s, 2, lerp(d_, e_, 0.6), False, CLARO, CLARO)
        corte(c, t, lerp(d_, e_, 0.35), 400, yc + s * DY, s, 1, lerp(d_, e_, 0.6), True, CLARO, CLARO)
        conta(c, t, d_, "8 e 4: ÷ 4", 900, yc - 30, 66, CLARO)
        conta(c, t, lerp(d_, e_, 0.9), "3 × 2 =", 900, yc + 76, 84, BR, "g")
        E.foco(c, t, e_, 0.5, lambda p: num_bola(c, "6", 1290, yc + 44, 78, 100, p, E.COR, BR))
        E.frase(c, t, e_ + 0.2, ps("doses", "g", 84, BR), 1400, yc + 74)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_, c_ = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, C["s18"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, a_ - 0.4, ps("a fita tem", "i", 92), XE, 350)
    fr(c, t, a_, 4, 5, 620, 320, 110, COR)
    E.frase(c, t, a_ + 0.4, ps("de metro", "g", 76), 710, 350)
    E.frase(c, t, b_ - 0.4, ps("cada laço usa", "i", 92), XE, 560)
    fr(c, t, b_, 2, 15, 760, 530, 110, COR)
    E.frase(c, t, b_ + 0.4, ps("de metro", "g", 76), 860, 560)
    E.frase(c, t, c_, ps("quantos laços", "g", 104, COR) + ps("dá para fazer?", "i", 110), XE, 830, passo=0.26)
    E.relogio(c, t, C["s19.a"], 1530, 350, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a0, b0, c0 = C["s20.a"], C["s20.b"], C["s20.c"]
    a1, b1, c1, d1, e1, f1, g1 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"], C["s21.e"], C["s21.f"], C["s21.end"]
    E.frase(c, t, C["s20"] + 0.1, ps("quantas vezes o laço", "i", 76) + ps("cabe na fita?", "g", 70, COR), XE, 150, passo=0.26)
    s, xa, xb, y = 180, 330, 760, 435
    conta(c, t, a0, "÷", 1270, 150, 76, COR, "g")
    conta(c, t, a0 + 0.2, "isso é dividir", 1340, 150, 66, COR)
    fr(c, t, b0, 4, 5, xa, y, s)
    E.saida(c, t, c0 - 0.1, lambda: sinal(c, t, b0 + 0.4, "÷", (xa + xb) / 2, y - 15, 130))
    vira(c, t, c0 - 0.1, 2, 15, xb, y, s, TINTA, ti=b0 + 0.5)
    sinal(c, t, c0 + 0.3, "×", (xa + xb) / 2, y - 15, 130, COR)
    ny, dy = y + s * NY, y + s * DY
    corte(c, t, a1 + 0.5, xa, ny, s, 2, lerp(a1, b1, 0.8), False)
    corte(c, t, a1 + 0.5, xb, dy, s, 1, lerp(a1, b1, 0.8), True)
    corte(c, t, b1 + 0.5, xa, dy, s, 1, lerp(b1, c1, 0.8), True)
    corte(c, t, b1 + 0.5, xb, ny, s, 3, lerp(b1, c1, 0.8), False)
    conta(c, t, a1, "4 e 2: ÷ 2", 1090, 340, 62, TINTA2)
    conta(c, t, b1, "15 e 5: ÷ 5", 1090, 440, 62, TINTA2)
    conta(c, t, c1, "2 × 3 =", 1090, 570, 84, TINTA, "g")
    E.foco(c, t, d1, 0.5, lambda p: num_bola(c, "6", 1480, 540, 88, 110, p, CERTO, BR))
    E.frase(c, t, d1 + 0.2, ps("laços", "g", 76, CERTO), 1590, 565)
    # a fita: quinze partes, doze pintadas, em seis laços
    x, yf, w, h = 216, 725, 1488, 110
    lp = w / 15
    ped = [(i, E.COR if (i // 2) % 2 == 0 else CLARO, ep(t, e1 + i * 0.05, 0.3)) for i in range(12)]
    E.foco(c, t, e1, 0.5, lambda p: E.chocolate(c, x, yf, w, h, 15, ped, p))
    conta_c(c, t, e1 + 0.5, "6 × 2/15 = 12/15", 620, 950, 70, TINTA)
    E.foco(c, t, f1, 0.5, lambda p: E.escreve(c, "= 4/5", 960, 950, 70, "b", CERTO, p))
    tb = lerp(f1, g1, 0.5)
    E.foco(c, t, tb, 0.5, lambda p: E.selo(c, 1300, 925, 58, True, p))
    E.frase(c, t, tb, ps("bateu", "g", 76, CERTO), 1380, 950)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.1, ps("resumindo", "i", 92, COR), W / 2, 200, "center")
        E.frase(c, t, C["s22.a"], ps("dividir é perguntar", "i", 100), W / 2, 400, "center")
        E.frase(c, t, C["s22.a"] + 0.9, ps("quantas vezes cabe", "g", 104, COR), W / 2, 530, "center")
        E.frase(c, t, C["s22.b"] - 0.4, ps("na conta,", "i", 84), W / 2, 700, "center")
        E.frase(c, t, C["s22.b"], ps("conserva,", "g", 92, COR) + ps("vira", "g", 92, COR) + ps("e multiplica", "g", 92, COR), W / 2, 830, "center", 0.3)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a_, b_, c_, d_, e_ = (C[f"s23.{k}"] for k in "abcde")
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 84), XE, 240)
    E.frase(c, t, a_, ps("as operações em uma conta só", "g", 84, COR), XE, 370, passo=0.26)
    E.foco(c, t, b_, 0.45, lambda p: E.fracao(c, 1, 2, 240, 490, 84, TINTA, p))
    E.foco(c, t, b_ + 0.3, 0.45, lambda p: E.escreve(c, "+", 310, 520, 80, "g", TINTA, p))
    E.foco(c, t, b_ + 0.6, 0.45, lambda p: E.fracao(c, 2, 3, 430, 490, 84, TINTA, p))
    E.foco(c, t, b_ + 0.9, 0.45, lambda p: E.escreve(c, "×", 500, 520, 80, "g", TINTA, p))
    E.foco(c, t, b_ + 1.2, 0.45, lambda p: E.fracao(c, 3, 4, 620, 490, 84, TINTA, p))
    E.frase(c, t, c_, ps("frações negativas", "g", 70, COR) + ps("e", "i", 76) + ps("número misto", "g", 70, COR), XE, 660, passo=0.26)
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 215, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, d_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1640, p), lerp(650, 260, p), ep(t, d_ + 0.2, 0.4), TINTA)
    E.frase(c, t, e_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 880, "center")


def b_regra_tudo(c, t, C, b):
    """o bloco regra tem três cenas: a regra sai de s10; a conta de s11 e s12 ocupa a tela limpa"""
    if t < C["s11"] + 0.3:
        E.saida(c, t, C["s11"] - 0.1, lambda: b_regra(c, t, C, b))
    if t >= C["s11"]:
        b_regra2(c, t, C, b)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, cabe=b_cabe, garrafas=b_garrafas, regra=b_regra_tudo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
