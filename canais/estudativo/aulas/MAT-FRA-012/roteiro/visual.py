"""Visual — Estudativo · MAT-FRA-012: expressões com frações, inclusive negativas.
Os blocos da conta aparecem como caixas: o que está grudado por vezes ou dividido fica na mesma caixa. A dívida usa a reta
(E.reta e E.salto): quem devia 8 e pagou 3 ainda deve 5. Número misto é tablete: dois inteiros e um quarto são nove pedaços."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, palco, centro
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-012_expressoes_com_fracoes_negativas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ordem", "negativas", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NY, DY = -0.565, 0.535  # centro do número de cima e do de baixo, em relação ao centro de uma fração de tamanho s

F = __import__("fractions").Fraction
assert F(1, 2) + F(2, 3) * F(3, 4) == 1 and (F(1, 2) + F(2, 3)) * F(3, 4) == F(7, 8)
assert F(-2, 3) + F(1, 4) == F(-5, 12) and F(-2, 3) == F(-8, 12) and F(1, 4) == F(3, 12)
assert F(-2, 5) * F(5, 6) == F(-1, 3) and F(-1, 2) * F(-2, 3) == F(1, 3)
assert F(9, 4) == 2 + F(1, 4) and F(9, 4) * F(2, 3) == F(3, 2) == 1 + F(1, 2)
assert -F(3, 2) + F(3, 4) == F(-3, 4) and F(-6, 4) == F(-3, 2) and -1 + F(1, 2) == F(-1, 2)
assert F(7, 8) - F(1, 4) / F(2, 3) == F(1, 2) and F(1, 4) * F(3, 2) == F(3, 8) and F(4, 8) == F(1, 2)
assert -(1 + F(1, 3)) + F(4, 5) * F(5, 8) == F(-5, 6) and F(-4, 3) == F(-8, 6) and F(1, 2) == F(3, 6)


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


def lwf(n, d, s):
    return max(E.larg(str(n), "g", s), E.larg(str(d), "g", s)) + s * 0.2


def neg(c, t, t0, n, d, cx, cy, s, cor=None):
    """fração negativa: o sinal fica antes do traço, na altura dele"""
    cor = cor or TINTA

    def fn(a):
        E.fracao(c, n, d, cx, cy, s, cor, a)
        centro(c, "−", cx - lwf(n, d, s) / 2 - s * 0.42, cy + s * 0.34, s, "g", cor, a)
    E.foco(c, t, t0, 0.5, fn)


def misto(c, t, ti, i, n, d, cx, cy, s, cor=None, menos=False):
    """número misto: o inteiro grande e a fração ao lado; menos = sinal à frente"""
    cor = cor or TINTA

    def fn(a):
        w = E.larg(str(i), "g", s * 1.6)
        x = cx - w - s * 0.2
        E.escreve(c, str(i), x, cy + s * 0.56, s * 1.6, "g", cor, a)
        E.fracao(c, n, d, cx + s * 0.45, cy, s, cor, a)
        if menos:
            centro(c, "−", x - s * 0.5, cy + s * 0.42, s * 1.2, "g", cor, a)
    E.foco(c, t, ti, 0.5, fn)


def bloco(c, x, y, w, h, q, cor=None, fundo=0.0):
    """caixa de um bloco da conta; q = 0..1"""
    if q <= 0:
        return
    if fundo:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), M.paint(cor or E.COR, fundo * q))
    E.caixa_pontilhada(c, x, y, w, h, q, cor or COR, prog_=q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def cena1():
        y, s = 300, 170
        fr(c, t, a1, 1, 2, 300, y, s, COR)
        sinal(c, t, a1 + 0.5, "+", 470, y - 15, 120)
        fr(c, t, a1 + 0.8, 2, 3, 640, y, s, COR)
        sinal(c, t, a1 + 1.3, "×", 810, y - 15, 120)
        fr(c, t, a1 + 1.6, 3, 4, 980, y, s, COR)
        sinal(c, t, b1 - 0.2, "=", 1160, y - 15, 120)
        fr(c, t, b1, 7, 8, 1340, y, s, ERRADO)
        if t >= c1:
            E.risco(c, 1250, y + 150, 1430, y - 150, t, c1, largura=16)
        E.frase(c, t, lerp(a1, b1, 0.55), ps("na ordem em que leu?", "i", 88), W / 2, 620, "center", 0.26)
        E.frase(c, t, c1, ps("errado", "g", 120, ERRADO), W / 2 - 300, 800, "center")
        E.frase(c, t, d1 - 0.5, ps("a resposta é", "i", 92), 960, 800)
        E.foco(c, t, d1, 0.5, lambda p: num_bola(c, "1", 1530, 770, 118, 150, p, CERTO, BR))
    E.saida(c, t, C["s02"] - 0.1, cena1)

    if t >= C["s02"]:
        a2, b2, c2, d2 = C["s02.a"], C["s02.b"], C["s02.c"], C["s02.d"]
        E.foco(c, t, d2 - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, d2 - 0.2, 0.7))), blur=0)
        E.frase(c, t, a2, ps("até o fim da aula", "i", 96), XE, 320)
        E.frase(c, t, lerp(a2, b2, 0.45), ps("contas com", "i", 96) + ps("várias", "g", 92) , XE, 460)
        E.frase(c, t, lerp(a2, b2, 0.7), ps("frações", "g", 120, COR), XE, 590)
        E.frase(c, t, b2, ps("negativas", "g", 92), XE, 730)
        E.frase(c, t, c2, ps("e", "i", 92) + ps("número misto", "g", 92, COR), XE, 850)
        E.foco(c, t, d2 + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", E.SOBRE, a), E.escreve(c, "de prova", 1310, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, ps("quatro lembretes", "i", 70, COR), XE, 110)
    xs, ys, w, h = (170, 985), (150, 540), 770, 360

    def caixa(i, ti):
        x, y = xs[i % 2], ys[i // 2]
        p = ep(t, ti, 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.foco(c, t, ti, 0.5, lambda a: num_bola(c, str(i + 1), x + 62, y + 66, 38, 46, a))
        return x + 118, y

    a3, a4, a5, b5, f3, f4 = C["s03.a"], C["s04.a"], C["s05.a"], C["s05.b"], C["s03.end"], C["s04.end"]
    x, y = caixa(0, a3)
    E.frase(c, t, a3 + 0.1, ps("ordem das operações", "g", 50, COR), x, y + 84, passo=0.26)
    conta(c, t, lerp(a3, f3, 0.35), "( )", xs[0] + 50, y + 210, 90, TINTA, "g")
    conta(c, t, lerp(a3, f3, 0.35), "parênteses", xs[0] + 50, y + 300, 44, TINTA2, "i")
    conta(c, t, lerp(a3, f3, 0.6), "× ÷", xs[0] + 310, y + 210, 90, TINTA, "g")
    conta(c, t, lerp(a3, f3, 0.6), "depois", xs[0] + 330, y + 300, 44, TINTA2, "i")
    conta(c, t, lerp(a3, f3, 0.85), "+ −", xs[0] + 550, y + 210, 90, TINTA, "g")
    conta(c, t, lerp(a3, f3, 0.85), "por último", xs[0] + 555, y + 300, 44, TINTA2, "i")
    x, y = caixa(1, a4)
    E.frase(c, t, a4 + 0.1, ps("regra de sinais", "g", 50, COR), x, y + 84, passo=0.26)
    conta(c, t, lerp(a4, f4, 0.25), "× e ÷", xs[1] + 50, y + 170, 50, TINTA2, "i")
    conta(c, t, lerp(a4, f4, 0.55), "sinais iguais:  +", xs[1] + 50, y + 240, 62, TINTA)
    conta(c, t, lerp(a4, f4, 0.8), "sinais diferentes:  −", xs[1] + 50, y + 320, 62, TINTA)
    x, y = caixa(2, a5)
    E.frase(c, t, a5 + 0.1, ps("misto vira fração", "g", 50, COR), x, y + 84, passo=0.26)
    conta(c, t, lerp(a5, b5, 0.4), "inteiro × o de baixo", xs[0] + 50, y + 180, 58, TINTA)
    conta(c, t, lerp(a5, b5, 0.65), "+ o de cima", xs[0] + 50, y + 250, 58, TINTA)
    conta(c, t, lerp(a5, b5, 0.85), "o de baixo se repete", xs[0] + 50, y + 320, 52, TINTA2, "i")
    x, y = caixa(3, b5)
    E.frase(c, t, b5 + 0.1, ps("denominadores diferentes", "g", 44, COR), x, y + 84, passo=0.26)
    conta(c, t, b5 + 0.4, "MMC", xs[1] + 50, y + 240, 130, TINTA, "g")
    conta(c, t, b5 + 0.7, "o menor múltiplo comum", xs[1] + 50, y + 320, 50, TINTA2, "i")
    E.frase(c, t, lerp(b5, C["s05.end"], 0.65), ps("faltou?", "g", 52, COR) + ps("procure a aula no canal", "i", 58), W / 2, 980, "center", 0.26)


# ---------------- ordem ----------------
def b_ordem(c, t, C, b):
    a6, b6, a7, b7, c7, d7, f7 = C["s06.a"], C["s06.b"], C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.end"]
    tp = lerp(c7, d7, 0.55)  # "E aqueles sete oitavos?"

    def conta_certa():
        y, s = 380, 170
        E.frase(c, t, C["s06"] + 0.1, ps("o vezes vem", "i", 76) + ps("antes do mais", "g", 70, COR), XE, 110, passo=0.26)
        fr(c, t, C["s06"], 1, 2, 280, y, s)
        sinal(c, t, C["s06"] + 0.1, "+", 435, y - 15, 110)
        xa, xb = 610, 970
        fr(c, t, C["s06"] + 0.2, 2, 3, xa, y, s)
        sinal(c, t, C["s06"] + 0.3, "×", (xa + xb) / 2, y - 15, 110)
        fr(c, t, C["s06"] + 0.4, 3, 4, xb, y, s)
        bloco(c, 520, y - 170, 560, 340, ep(t, a6, 0.5), E.COR_TEXTO)
        ny, dy = y + s * NY, y + s * DY
        corte(c, t, b6, xa, dy, s, 1, b6 + 0.3, True)
        corte(c, t, b6, xb, ny, s, 1, b6 + 0.3, False)
        corte(c, t, b6 + 0.2, xa, ny, s, 1, b6 + 0.5, False)
        corte(c, t, b6 + 0.2, xb, dy, s, 2, b6 + 0.5, True)
        sinal(c, t, b6 + 0.4, "=", 1200, y - 15, 110)
        E.resultado(c, t, b6 + 0.6, 1, 2, 1400, y, 124, 148)
        y2, s2 = 765, 130
        fr(c, t, a7, 1, 2, 600, y2, s2, COR)
        sinal(c, t, a7 + 0.3, "+", 740, y2 - 15, 110)
        fr(c, t, a7 + 0.5, 1, 2, 880, y2, s2, COR)
        sinal(c, t, b7 - 0.2, "=", 1040, y2 - 15, 110)
        E.foco(c, t, b7, 0.5, lambda p: num_bola(c, "1", 1200, y2, 96, 120, p, CERTO, BR))
        E.frase(c, t, c7, ps("quem soma antes", "i", 76) + ps("muda a conta", "g", 72, ERRADO), W / 2, 1000, "center", 0.26)
    E.saida(c, t, tp - 0.1, conta_certa)

    if t >= tp:
        E.frase(c, t, tp, ps("e aqueles", "i", 92), XE, 220)
        fr(c, t, tp + 0.5, 7, 8, 650, 190, 120, ERRADO)
        E.frase(c, t, tp + 0.7, ps("?", "g", 92, ERRADO), 740, 222)
        E.frase(c, t, d7 - 0.8, ps("são a resposta de outra conta", "i", 76), 830, 222, passo=0.26)
        y, s = 560, 170
        xe = 250
        E.foco(c, t, d7, 0.45, lambda p: centro(c, "(", xe, y + 80, 230, "m", COR, p))
        fr(c, t, d7 + 0.1, 1, 2, 350, y, s)
        sinal(c, t, d7 + 0.2, "+", 490, y - 15, 110)
        fr(c, t, d7 + 0.3, 2, 3, 640, y, s)
        E.foco(c, t, d7 + 0.4, 0.45, lambda p: centro(c, ")", 750, y + 80, 230, "m", COR, p))
        sinal(c, t, d7 + 0.6, "×", 850, y - 15, 110)
        fr(c, t, d7 + 0.8, 3, 4, 1000, y, s)
        sinal(c, t, d7 + 1.0, "=", 1170, y - 15, 110)
        fr(c, t, d7 + 1.2, 7, 8, 1320, y, s, COR)
        E.frase(c, t, lerp(d7, f7, 0.68), ps("parêntese manda fazer", "i", 84) + ps("a soma primeiro", "g", 78, COR), W / 2, 880, "center", 0.26)


# ---------------- negativas ----------------
def b_negativas(c, t, C, b):
    a8, b8 = C["s08.a"], C["s08.b"]
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]

    def soma():
        E.frase(c, t, C["s08"] + 0.1, ps("e com fração", "i", 76) + ps("negativa?", "g", 70, COR), XE, 130)
        y, s = 300, 130
        neg(c, t, a8, 2, 3, 300, y, s)
        sinal(c, t, a8 + 0.5, "+", 430, y - 15, 100)
        fr(c, t, a8 + 0.8, 1, 4, 550, y, s)
        E.foco(c, t, b8, 0.45, lambda p: E.pilula(c, "MMC = 12", 770, y, 52, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
        neg(c, t, a9, 8, 12, 1140, y, s, COR)
        sinal(c, t, b9 - 0.2, "+", 1290, y - 15, 100)
        fr(c, t, b9, 3, 12, 1430, y, s)
        conta(c, t, c9 - 0.5, "o sinal vai com o de cima", XE, 505, 62, TINTA2, "i")
        y2 = 505
        conta_c(c, t, c9, "−8 + 3", 1285, y2, 84, COR, "g")
        vmin, vmax = -8, 0
        tr = lerp(c9, d9, 0.2)
        vx = E.reta(c, t, tr, 260, 1560, 720, vmin, vmax, (-8, -5, 0), lambda v: f"−{abs(v)}" if v else "0", size=56)
        E.foco(c, t, tr + 0.3, 0.45, lambda p: E.bola(c, vx(-8), 720, 20, ERRADO, p))
        conta_c(c, t, tr + 0.3, "devia 8", vx(-8), 640, 56, ERRADO)
        ts = lerp(c9, d9, 0.5)
        E.salto(c, t, ts, vx(-8), vx(-5), 720, 110, CERTO, "pagou 3")
        E.foco(c, t, lerp(c9, d9, 0.8), 0.45, lambda p: E.bola(c, vx(-5), 720, 20, COR, p))
        conta_c(c, t, lerp(c9, d9, 0.8), "ainda deve 5", vx(-5) + 300, 640, 56, COR)
        sinal(c, t, d9 - 0.2, "=", 620, 910, 100)
        neg(c, t, d9, 5, 12, 830, 925, 110, CERTO)
    E.saida(c, t, C["s10"] - 0.1, soma)

    if t >= C["s10"]:
        a0, b0, c0, d0, e0, f0, g0 = (C[f"s10.{k}"] for k in "abcdefg")
        E.frase(c, t, C["s10"] + 0.1, ps("na multiplicação,", "i", 76), XE, 150)
        E.frase(c, t, a0, ps("decida o sinal primeiro", "g", 76, COR), 810, 150, passo=0.26)
        y, s = 360, 140
        neg(c, t, b0, 2, 5, 320, y, s)
        sinal(c, t, b0 + 0.5, "×", 450, y - 15, 100)
        fr(c, t, b0 + 0.8, 5, 6, 570, y, s)
        sinal(c, t, c0 - 0.2, "=", 710, y - 15, 100)
        E.foco(c, t, c0, 0.45, lambda p: centro(c, "−", 810, y + 34, 140, "g", ERRADO, p))
        E.foco(c, t, d0, 0.5, lambda p: E.fracao(c, 1, 3, 920, y, s, TINTA, p))
        sinal(c, t, e0 - 0.2, "=", 1060, y - 15, 100)
        neg(c, t, e0, 1, 3, 1270, y, s, COR)
        conta(c, t, lerp(b0, c0, 0.6), "sinais diferentes:", XE, 570, 62, TINTA2, "i")
        conta(c, t, c0, "dá menos", 640, 570, 66, ERRADO, "g")
        conta(c, t, d0, "depois, a conta normal", 1040, 570, 62, TINTA2, "i")
        y2 = 790
        neg(c, t, f0, 1, 2, 320, y2, s)
        sinal(c, t, f0 + 0.4, "×", 460, y2 - 15, 100)
        neg(c, t, f0 + 0.8, 2, 3, 680, y2, s)
        sinal(c, t, g0 - 0.2, "=", 820, y2 - 15, 100)
        E.foco(c, t, g0, 0.5, lambda p: (centro(c, "+", 920, y2 + 34, 130, "g", CERTO, p), E.fracao(c, 1, 3, 1030, y2, s, CERTO, p)))
        conta(c, t, lerp(f0, g0, 0.5), "sinais iguais:", 1190, y2 - 30, 62, TINTA2, "i")
        conta(c, t, g0, "dá mais", 1190, y2 + 60, 70, CERTO, "g")


# ---------------- misto ----------------
def b_misto(c, t, C, b):
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]

    def parte11():
        E.frase(c, t, a1, ps("transforme em fração", "g", 80, COR) + ps("antes de qualquer conta", "i", 84), W / 2, 170, "center", 0.26)
        y, s = 360, 130
        misto(c, t, b1, 2, 1, 4, 480, y, s)
        sinal(c, t, b1 + 0.6, "×", 690, y - 15, 100)
        fr(c, t, b1 + 0.9, 2, 3, 830, y, s)
        # 2 inteiros e 1/4: nove pedaços
        x, yb, w, h, g = 216, 570, 460, 140, 56
        ti = lerp(b1, c1, 0.42)
        for k in range(2):
            ped = [(i, E.COR, ep(t, ti + (k * 4 + i) * 0.1, 0.3)) for i in range(4)]
            E.foco(c, t, ti - 0.1, 0.45, lambda p, k=k, ped=ped: E.chocolate(c, x + k * (w + g), yb, w, h, 4, ped, p))
        ped = [(0, CERTO, ep(t, c1 - 0.4, 0.3))]
        E.foco(c, t, ti - 0.1, 0.45, lambda p: E.chocolate(c, x + 2 * (w + g), yb, w, h, 4, ped, p))
        conta(c, t, ti, "2 × 4 = 8", 300, 890, 76, TINTA)
        conta(c, t, c1 - 0.5, "+ 1", 720, 890, 76, CERTO)
        sinal(c, t, c1 - 0.2, "=", 930, 860, 100)
        E.resultado(c, t, c1, 9, 4, 1130, 860, 100, 124)
        E.frase(c, t, c1 + 0.3, ps("quartos", "i", 84), 1290, 890)
    E.saida(c, t, C["s12"] - 0.1, parte11)

    if t >= C["s12"]:
        a2, b2, c2, d2, e2 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
        s, xa, xb, y = 200, 340, 800, 480
        fr(c, t, a2, 9, 4, xa, y, s)
        fr(c, t, a2 + 0.3, 2, 3, xb, y, s)
        sinal(c, t, a2 + 0.2, "×", (xa + xb) / 2, y - 15, 130, COR)
        ny, dy = y + s * NY, y + s * DY
        corte(c, t, b2 + 0.1, xa, ny, s, 3, b2 + 0.4, False)
        corte(c, t, b2 + 0.1, xb, dy, s, 1, b2 + 0.4, True)
        corte(c, t, c2 + 0.1, xb, ny, s, 1, c2 + 0.4, False)
        corte(c, t, c2 + 0.1, xa, dy, s, 2, c2 + 0.4, True)
        conta(c, t, b2, "9 e 3: ÷ 3", XE, 150, 62, TINTA2)
        conta(c, t, c2, "2 e 4: ÷ 2", 620, 150, 62, TINTA2)
        sinal(c, t, d2 - 0.2, "=", 1090, y - 15, 120)
        fr(c, t, d2, 3, 2, 1260, y, 170, COR)
        sinal(c, t, e2 - 0.2, "=", 1420, y - 15, 120)
        misto(c, t, e2, 1, 1, 2, 1620, y, 130, CERTO)
        E.frase(c, t, e2 + 0.3, ps("um inteiro e um meio", "i", 76), W / 2 + 330, 850, "center", 0.26)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]

    def errado():
        E.frase(c, t, C["s13"] + 0.1, ps("o erro mais comum junta", "i", 76) + ps("o misto e o sinal", "g", 70, ERRADO), W / 2, 170, "center", 0.26)
        y, s = 400, 130
        misto(c, t, a3, 1, 1, 2, 600, y, s, TINTA, menos=True)
        sinal(c, t, a3 + 0.8, "+", 830, y - 15, 100)
        fr(c, t, a3 + 1.1, 3, 4, 970, y, s)
        tl = lerp(C["s13"], b3, 0.8)
        conta(c, t, tl, "muita gente lê:", XE, 680, 70, TINTA2, "i")
        conta(c, t, b3, "−1  +", 700, 690, 110, ERRADO, "g")
        E.foco(c, t, b3 + 0.4, 0.45, lambda p: E.fracao(c, 1, 2, 1040, 660, 110, ERRADO, p))
        conta(c, t, c3 - 0.4, "=", 1130, 690, 100, TINTA, "g")
        neg(c, t, c3, 1, 2, 1360, 660, 110, ERRADO)
        if t >= c3 + 1.0:
            E.risco(c, 660, 760, 1450, 590, t, c3 + 1.0, largura=12)
    E.saida(c, t, C["s14"] - 0.1, errado)

    if t >= C["s14"]:
        a4, b4, c4, d4, e4 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"]
        E.frase(c, t, C["s14"] + 0.1, ps("pense em", "i", 76) + ps("dívida", "g", 70, COR), XE, 150)
        E.foco(c, t, lerp(C["s14"], a4, 0.3), 0.45, lambda p: (E.moeda(c, 730, 125, 72, "R$1", p), E.moeda(c, 890, 125, 72, "50¢", p)))
        E.frase(c, t, lerp(C["s14"], a4, 0.45), ps("deve mais de R$ 1,", "i", 66) + ps("não R$ 0,50", "g", 60, ERRADO), 1000, 150, passo=0.26)
        E.frase(c, t, a4, ps("o sinal vale para", "i", 96) + ps("o misto todo", "g", 88, COR), W / 2, 290, "center", 0.26)
        y, s = 530, 130
        misto(c, t, a4 + 0.4, 1, 1, 2, 460, y, s, TINTA, menos=True)
        bloco(c, 170, y - 145, 460, 290, ep(t, a4 + 0.7, 0.5), E.COR_TEXTO)
        conta_c(c, t, lerp(a4, b4, 0.6), "sem o sinal:", 840, y - 135, 58, TINTA2, "i")
        fr(c, t, b4, 3, 2, 840, y, s, COR)
        conta_c(c, t, lerp(b4, c4, 0.5), "devolva o sinal:", 1260, y - 135, 58, TINTA2, "i")
        neg(c, t, c4, 3, 2, 1260, y, s, COR)
        y2 = 850
        conta(c, t, lerp(c4, d4, 0.5), "com denominador 4:", XE, y2 + 30, 62, TINTA2, "i")
        neg(c, t, d4, 6, 4, 830, y2, s, COR)
        sinal(c, t, d4 + 0.5, "+", 960, y2 - 15, 100)
        fr(c, t, d4 + 0.8, 3, 4, 1080, y2, s)
        sinal(c, t, e4 - 0.2, "=", 1220, y2 - 15, 100)
        neg(c, t, e4, 3, 4, 1440, y2, s, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def parte15():
        a_, b_, c_ = C["s15.a"], C["s15.b"], C["s15.c"]
        E.frase(c, t, C["s15"] + 0.1, ps("agora, o atalho", "i", 78, CLARO), W / 2, 180, "center")
        E.frase(c, t, a_, ps("separe a conta", "g", 120, BR), W / 2, 340, "center")
        E.frase(c, t, a_ + 0.9, ps("nos sinais de", "i", 96, CLARO) + ps("+", "g", 96, BR) + ps("e", "i", 96, CLARO) + ps("−", "g", 96, BR), W / 2, 470, "center")
        for i, (x, ti) in enumerate(((330, b_), (800, b_ + 0.3), (1270, b_ + 0.6))):
            bloco(c, x, 570, 320, 170, ep(t, ti, 0.5), CLARO, 0.25)
            conta_c(c, t, ti, f"bloco {i + 1}", x + 160, 678, 62, BR)
        conta_c(c, t, b_ + 0.2, "cada pedaço é um bloco", W / 2, 840, 76, BR)
        E.frase(c, t, c_, ps("só no fim,", "i", 80, CLARO) + ps("junte os blocos", "g", 76, BR), W / 2, 960, "center")
    E.saida(c, t, C["s16"] - 0.1, parte15)

    if C["s16"] <= t < C["s17"] + 0.3:
        a_, b_, c_, d_, e_, f_, g_ = (C[f"s16.{k}"] for k in "abcdefg")

        def parte16():
            E.frase(c, t, C["s16"] + 0.1, ps("veja", "i", 72, CLARO), XE, 150)
            y, s = 300, 150
            fr(c, t, a_, 7, 8, 500, y, s, BR)
            xm = 690
            sinal(c, t, a_ + 0.5, "−", xm, y - 15, 120, BR)
            fr(c, t, a_ + 0.8, 1, 4, 890, y, s, BR)
            sinal(c, t, a_ + 1.2, "÷", 1060, y - 15, 110, BR)
            fr(c, t, a_ + 1.5, 2, 3, 1230, y, s, BR)
            bloco(c, 400, y - 165, 200, 330, ep(t, b_ + 0.2, 0.5), CLARO, 0.2)
            bloco(c, 790, y - 165, 560, 330, ep(t, b_ + 0.4, 0.5), CLARO, 0.2)
            if t >= b_:
                M.line(c, xm, y - 200, xm, y + 200, CLARO, 1.0, 5, dash=[14, 12], progress=ep(t, b_, 0.5))
            y2, s2 = 615, 110
            fr(c, t, c_, 1, 4, 830, y2, s2, BR)
            sinal(c, t, c_ + 0.2, "×", 950, y2 - 15, 100, BR)
            fr(c, t, c_ + 0.4, 3, 2, 1070, y2, s2, CLARO)
            sinal(c, t, d_ - 0.2, "=", 1190, y2 - 15, 100, BR)
            fr(c, t, d_, 3, 8, 1320, y2, s2, CLARO)
            y3 = 870
            fr(c, t, e_, 7, 8, 470, y3, s2, BR)
            sinal(c, t, e_ + 0.3, "−", 600, y3 - 15, 100, BR)
            fr(c, t, e_ + 0.5, 3, 8, 730, y3, s2, CLARO)
            sinal(c, t, f_ - 0.2, "=", 860, y3 - 15, 100, BR)
            fr(c, t, f_, 4, 8, 990, y3, s2, BR)
            sinal(c, t, g_ - 0.2, "=", 1120, y3 - 15, 100, BR)
            E.resultado(c, t, g_, 1, 2, 1290, y3, 100, 124, CERTO)
        E.saida(c, t, C["s17"] - 0.1, parte16)

    if t >= C["s17"]:
        a_, b_, c_, d_, f_ = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"], C["s17.end"]
        E.frase(c, t, C["s17"] + 0.1, ps("funciona porque", "i", 76, CLARO), W / 2, 150, "center")
        E.frase(c, t, a_, ps("× e ÷", "g", 84, BR) + ps("ficam grudados no mesmo bloco", "i", 84, CLARO), W / 2, 260, "center", 0.26)
        E.frase(c, t, b_ - 0.5, ps("só não separe no", "i", 76, CLARO) + ps("sinal colado na fração", "g", 70, BR), W / 2, 400, "center", 0.26)
        y, s = 590, 120
        bloco(c, 380, y - 140, 680, 280, ep(t, c_ + 0.3, 0.5), CLARO, 0.2)
        neg(c, t, c_, 1, 2, 560, y, s, BR)
        sinal(c, t, c_ + 0.2, "×", 690, y - 15, 90, BR)
        neg(c, t, c_ + 0.4, 2, 3, 880, y, s, BR)
        conta(c, t, c_ + 0.5, "um bloco só", 1120, y + 24, 76, CLARO)
        E.frase(c, t, d_ - 0.4, ps("e não serve com", "i", 76, CLARO) + ps("parênteses:", "g", 70, BR), W / 2, 830, "center", 0.26)
        E.frase(c, t, lerp(d_, f_, 0.3), ps("o que está dentro deles é um bloco só", "i", 66, CLARO), W / 2, 930, "center", 0.26)
        E.frase(c, t, lerp(d_, f_, 0.82), ps("e vem primeiro", "g", 62, BR), W / 2, 1020, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_ = C["s18.a"], C["s18.b"]
    E.frase(c, t, C["s18"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, lerp(C["s18"], a_, 0.6), ps("resolva", "g", 150), XE, 380)
    y, s = 760, 150
    misto(c, t, a_, 1, 1, 3, 500, y, s, TINTA, menos=True)
    sinal(c, t, b_, "+", 760, y - 15, 120)
    fr(c, t, b_ + 0.3, 4, 5, 910, y, s, COR)
    sinal(c, t, b_ + 0.8, "×", 1090, y - 15, 120)
    fr(c, t, b_ + 1.2, 5, 8, 1260, y, s, COR)
    E.relogio(c, t, C["s19.a"], 1530, 300, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a0, b0, c0, d0 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]

    def blocos():
        E.frase(c, t, C["s20"] + 0.1, ps("vamos lá,", "i", 72, COR) + ps("em blocos", "g", 66, COR), XE, 125)
        y, s = 430, 120
        conta_c(c, t, lerp(C["s20"], a0, 0.7), "primeiro bloco", 500, 200, 62, COR)
        bloco(c, 170, 230, 660, 400, ep(t, a0, 0.5), E.COR_TEXTO)
        misto(c, t, a0, 1, 1, 3, 340, y, s, TINTA)
        sinal(c, t, a0 + 0.7, "=", 510, y - 15, 90)
        fr(c, t, a0 + 0.9, 4, 3, 640, y, s, COR)
        conta_c(c, t, lerp(a0, b0, 0.7), "1 × 3 + 1 = 4", 500, 710, 62, TINTA2)
        neg(c, t, b0, 4, 3, 500, 860, 120, COR)
        conta_c(c, t, lerp(b0, c0, 0.4), "segundo bloco", 1320, 200, 62, COR)
        bloco(c, 990, 230, 660, 400, ep(t, c0, 0.5), E.COR_TEXTO)
        xa, xb = 1190, 1470
        fr(c, t, c0, 4, 5, xa, y, s + 20)
        sinal(c, t, c0 + 0.3, "×", (xa + xb) / 2, y - 15, 90)
        fr(c, t, c0 + 0.6, 5, 8, xb, y, s + 20)
        s2 = s + 20
        ny, dy = y + s2 * NY, y + s2 * DY
        corte(c, t, lerp(c0, d0, 0.7), xa, dy, s2, 1, d0 - 0.2, True)
        corte(c, t, lerp(c0, d0, 0.7), xb, ny, s2, 1, d0 - 0.2, False)
        corte(c, t, lerp(c0, d0, 0.8), xa, ny, s2, 1, d0 - 0.1, False)
        corte(c, t, lerp(c0, d0, 0.8), xb, dy, s2, 2, d0 - 0.1, True)
        E.resultado(c, t, d0, 1, 2, 1320, 830, 100, 124)
    E.saida(c, t, C["s21"] - 0.1, blocos)

    if t >= C["s21"]:
        a_, b_, c_, f_ = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.end"]
        E.frase(c, t, C["s21"] + 0.1, ps("junte os blocos", "i", 72, COR), XE, 180)
        y, s = 380, 150
        neg(c, t, a_, 4, 3, 480, y, s)
        sinal(c, t, a_ + 0.4, "+", 640, y - 15, 110)
        fr(c, t, a_ + 0.7, 1, 2, 790, y, s)
        tm = lerp(a_, b_, 0.65)
        E.foco(c, t, tm, 0.45, lambda p: E.pilula(c, "MMC = 6", 1180, y, 62, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
        y2 = 720
        neg(c, t, b_, 8, 6, 480, y2, s, COR)
        sinal(c, t, b_ + 0.4, "+", 640, y2 - 15, 110)
        fr(c, t, b_ + 0.7, 3, 6, 790, y2, s, COR)
        sinal(c, t, c_ - 0.2, "=", 960, y2 - 15, 110)
        neg(c, t, c_, 5, 6, 1190, y2, s, CERTO)
        E.foco(c, t, c_ + 0.3, 0.45, lambda p: E.selo(c, 1400, y2, 64, True, p))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.1, ps("resumindo", "i", 92, COR), W / 2, 200, "center")
        itens = ((400, "s22.a", ps("blocos", "g", 92, COR) + ps("primeiro", "i", 96)),
                 (590, "s22.b", ps("misto", "g", 92, COR) + ps("vira fração", "i", 96)),
                 (780, "s22.c", ps("o sinal do misto", "g", 84, COR) + ps("vale para ele todo", "i", 88)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 240, y - 28, 56, 64, a))
            E.frase(c, t, C[k] + 0.1, partes, 330, y, passo=0.26)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a_, b_, c_, d_ = C["s23.a"], C["s23.b"], C["s23.c"], C["s23.d"]
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 84), XE, 260)
    E.frase(c, t, a_, ps("pratica tudo isso", "g", 124, COR), XE, 410)
    E.frase(c, t, b_, ps("5 situações", "g", 92) + ps("para pausar e resolver", "i", 92), XE, 560, passo=0.26)
    E.frase(c, t, b_ + 1.4, ps("antes de ver a resposta", "i", 80), XE, 660, passo=0.26)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 230, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1640, p), lerp(650, 275, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ordem=b_ordem, negativas=b_negativas, misto=b_misto, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
