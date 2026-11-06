"""Visual — Estudativo · MAT-FRA-013: praticando operações com frações.
Aula de prática: cinco situações, cada uma com selo de progresso, relógio de pausa e um desenho próprio: a parede em quinze
partes, os funcionários, o caminhão em oito blocos de 30 caixas, o tecido e a reta da dívida.
Todo instante vem de C[...]: o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, palco, centro
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-013_praticando_operacoes_com_fracoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao3", "atalho", "questao5", "fim"))
BR = "#FFFFFF"
NY, DY = -0.565, 0.535  # centro do número de cima e do de baixo, em relação ao centro de uma fração de tamanho s

F = __import__("fractions").Fraction
assert F(2, 5) + F(1, 3) == F(11, 15) and 2 * 3 + 1 * 5 == 11 and 15 - 11 == 4
assert F(3, 10) * F(5, 6) == F(1, 4) and 60 // 4 == 15 and 60 * 5 // 6 == 50 and 50 * 3 // 10 == 15
assert 240 // 8 == 30 and 30 * 3 == 90 and 240 - 90 == 150 and 150 // 5 == 30 and 150 - 30 == 120
assert 240 // 5 == 48 and 150 - 48 == 102 and F(4, 5) * F(5, 8) == F(1, 2)
assert 7 + F(1, 2) == F(15, 2) and F(15, 2) / F(3, 4) == 10 and 10 * F(3, 4) == F(30, 4) == F(15, 2) and F(2, 15) * F(3, 4) == F(1, 10)
assert F(1, 2) / F(3, 4) == F(2, 3) and F(-5, 6) + F(2, 3) == F(-1, 6) and F(2, 3) == F(4, 6)


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


def fica(c, t, t0, t1, partes, x, y, align="left", passo=0.2):
    """frase que entra em t0 e sai em t1"""
    E.saida(c, t, t1, lambda: E.frase(c, t, t0, partes, x, y, align, passo))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    """número dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def conta(c, t, ti, s, x, y, size=64, cor=None, est="b"):
    E.foco(c, t, ti, 0.45, lambda a: E.escreve(c, s, x, y, size, est, cor or TINTA, a))


def conta_c(c, t, ti, s, cx, y, size=64, cor=None, est="b"):
    E.foco(c, t, ti, 0.45, lambda a: centro(c, s, cx, y, size, est, cor or TINTA, a))


def selo(c, t, t0, n):
    """situação n de 5, com cinco pontos de progresso"""
    s = f"situação {n} de 5"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", fundo=E.COR, cor=E.SOBRE, a=a)
        for i in range(5):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


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


def misto(c, t, ti, i, n, d, cx, cy, s, cor=None):
    """número misto: o inteiro grande e a fração ao lado"""
    cor = cor or TINTA

    def fn(a):
        w = E.larg(str(i), "g", s * 1.6)
        E.escreve(c, str(i), cx - w - s * 0.2, cy + s * 0.56, s * 1.6, "g", cor, a)
        E.fracao(c, n, d, cx + s * 0.45, cy, s, cor, a)
    E.foco(c, t, ti, 0.5, fn)


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


def bloco(c, x, y, w, h, q, cor=None):
    """caixa de um bloco da conta; q = 0..1"""
    if q > 0:
        E.caixa_pontilhada(c, x, y, w, h, q, cor or COR, prog_=q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, f_ = C["s01.a"], C["s01.b"], C["s01.end"]
    E.frase(c, t, a_ + 0.1, ps("5", "g", 240, COR) + ps("situações", "g", 180, COR), XE, 330, passo=0.25)
    E.frase(c, t, a_ + 0.9, ps("criadas para esta aula", "i", 96), XE, 470, passo=0.26)
    E.frase(c, t, lerp(a_, b_, 0.55), ps("com as", "i", 80) + ps("quatro operações", "g", 74, COR) + ps("entre frações", "i", 80), XE, 590, passo=0.26)
    for i, (s, cx) in enumerate((("pause", 520), ("resolva", 1210))):
        ti = b_ + i * 0.9
        E.foco(c, t, ti, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 730, 56, 64, p), E.escreve(c, s, cx - 110, 760, 96, "g", TINTA, p)))
    E.frase(c, t, lerp(b_, f_, 0.5), ps("errar aqui", "i", 88) + ps("não custa nada", "g", 80, COR), W / 2, 900, "center", 0.18)
    E.frase(c, t, lerp(b_, f_, 0.72), ps("e ensina mais do que só assistir", "i", 68), W / 2, 1000, "center", 0.26)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    a_, f_ = C["s02.a"], C["s02.end"]
    E.frase(c, t, C["s02"] + 0.2, ps("antes de qualquer conta,", "i", 76), XE, 330, passo=0.26)
    E.frase(c, t, a_, ps("que operação", "g", 96, COR), XE, 470)
    E.frase(c, t, a_ + 0.5, ps("é essa?", "i", 110), XE, 590)
    x, w = 940, 790
    for i, (k, s) in enumerate((("s02.b", "somar com MMC"), ("s02.c", "multiplicar"), ("s02.d", "fração do restante"), ("s02.e", "dividir"), ("s02.f", "ordem das operações"))):
        y = 130 + i * 142
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 118, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(s, "g", 58, COR)], x + 40, y + 80)
    E.frase(c, t, lerp(C["s02.f"], f_, 0.4), ps("travou?", "i", 62, COR), XE, 750, passo=0.26)
    E.frase(c, t, lerp(C["s02.f"], f_, 0.55), ps("procure a aula no canal", "i", 60), XE, 830, passo=0.26)


# ---------------- situação 1: somar e quanto falta ----------------
def parede(c, t, x, y, w, h, n1, n2, q1, q2, a=1.0, cortes=1.0):
    """a parede em quinze partes: n1 de manhã, n2 à tarde"""
    ped = [(i, E.COR, ep(t, q1 + i * 0.05, 0.3)) for i in range(n1)] + [(i, CLARO, ep(t, q2 + (i - n1) * 0.05, 0.3)) for i in range(n1, n1 + n2)]
    E.chocolate(c, x, y, w, h, 15, ped, a, cortes)


def b_questao1(c, t, C, b):
    a_, b_, c_, d_ = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.d"]
    selo(c, t, a_, 1)
    E.frase(c, t, b_ - 0.4, ps("de manhã, pintou", "i", 84), XE, 300)
    fr(c, t, b_, 2, 5, 810, 270, 100, COR)
    E.frase(c, t, b_ + 0.4, ps("da parede", "g", 72), 900, 300)
    E.frase(c, t, c_ - 0.4, ps("à tarde,", "i", 84), XE, 480)
    fr(c, t, c_, 1, 3, 530, 450, 100, COR)
    E.frase(c, t, c_ + 0.4, ps("da parede", "g", 72), 620, 480)
    E.frase(c, t, d_, ps("que fração", "i", 110) + ps("falta pintar?", "g", 104, COR), XE, 800, passo=0.2)
    E.relogio(c, t, C["s04.a"], 1560, 340, 180)


def b_resposta1(c, t, C, b):
    selo(c, t, C["s05"] + 0.1, 1)
    a_, b_, c_, d_, e_, f_ = (C[f"s05.{k}"] for k in "abcdef")

    def conta_ok():
        y, s = 310, 130
        fr(c, t, a_, 2, 5, 260, y, s)
        sinal(c, t, a_ + 0.3, "+", 385, y - 15, 96)
        fr(c, t, a_ + 0.5, 1, 3, 510, y, s)
        E.foco(c, t, b_, 0.45, lambda p: E.pilula(c, "MMC = 15", 780, y, 54, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
        fr(c, t, c_, 6, 15, 1060, y, s, COR)
        sinal(c, t, c_ + 0.4, "+", 1200, y - 15, 96)
        fr(c, t, c_ + 0.7, 5, 15, 1340, y, s)
        sinal(c, t, d_ - 0.2, "=", 1485, y - 15, 96)
        fr(c, t, d_, 11, 15, 1620, y, s, CERTO)
        E.frase(c, t, lerp(d_, e_, 0.2), ps("com denominadores pequenos,", "i", 66) + ps("a borboleta", "g", 62, COR) + ps("também serve", "i", 66), W / 2, 590, "center", 0.26)
        conta_c(c, t, e_, "2 × 3 + 1 × 5 = 11", 690, 760, 84, TINTA)
        conta_c(c, t, f_, "5 × 3 = 15", 1370, 760, 84, TINTA)
        E.foco(c, t, f_ + 0.5, 0.45, lambda p: E.fracao(c, 11, 15, W / 2, 900, 80, CERTO, p))
    E.saida(c, t, C["s06"] - 0.1, conta_ok)

    if t >= C["s06"]:
        a6, b6, c6, f6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.end"]
        E.frase(c, t, lerp(C["s06"], a6, 0.2), ps("a pergunta é o que", "i", 96) + ps("falta", "g", 100, COR), W / 2, 280, "center")
        x, y, w, h = 216, 360, 1488, 170
        q = C["s06"] + 0.1
        parede(c, t, x, y, w, h, 6, 5, q, q, ep(t, q, 0.4))
        conta_c(c, t, b6, "a parede inteira", 500, 670, 70, TINTA)
        lp = w / 15
        E.chave(c, x + 11 * lp, x + 15 * lp, y + h + 12, CERTO, ep(t, c6, 0.4), 18, 5)
        conta_c(c, t, c6, "faltam 4", x + 13 * lp, 670, 70, CERTO, "g")
        yr = 810
        fr(c, t, b6, 15, 15, 500, yr, 110)
        sinal(c, t, lerp(b6, c6, 0.3), "−", 640, yr - 15, 96)
        fr(c, t, lerp(b6, c6, 0.5), 11, 15, 780, yr, 110)
        sinal(c, t, c6 - 0.2, "=", 930, yr - 15, 96)
        E.resultado(c, t, c6, 4, 15, 1090, yr, 92, 112, CERTO)
        E.frase(c, t, lerp(c6, f6, 0.3), ps("parou em", "i", 62) + ps("11/15?", "g", 58, ERRADO) + ps("respondeu outra pergunta", "i", 62), W / 2, 1000, "center", 0.26)


# ---------------- situação 2: multiplicar ----------------
def b_questao2(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s07.{k}"] for k in "abcde")
    selo(c, t, a_, 2)
    E.frase(c, t, b_, ps("60", "g", 110, COR) + ps("funcionários", "g", 92), XE, 300)
    fr(c, t, c_, 5, 6, 240, 425, 100, COR)
    E.frase(c, t, c_ + 0.4, ps("fizeram o curso", "i", 84), 330, 455)
    fr(c, t, d_, 3, 10, 240, 640, 100, COR)
    E.frase(c, t, d_ + 0.4, ps("de quem fez", "g", 74) + ps("foram promovidos", "i", 84), 340, 670, passo=0.26)
    E.frase(c, t, e_, ps("quantos", "i", 110) + ps("foram promovidos?", "g", 100, COR), XE, 900, passo=0.2)
    E.relogio(c, t, C["s08.a"], 1570, 320, 170)


def b_resposta2(c, t, C, b):
    selo(c, t, C["s09"] + 0.1, 2)
    a_, b_, c_, d_ = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]

    def cruz():
        s, xa, xb, y = 190, 340, 790, 500
        E.frase(c, t, C["s09"] + 0.2, ps("a palavra", "i", 66) + ps("de", "g", 62, COR) + ps("vira", "i", 66) + ps("vezes", "g", 62, COR), 810, 130)
        fr(c, t, a_, 3, 10, xa, y, s)
        sinal(c, t, a_ + 0.3, "×", (xa + xb) / 2, y - 15, 130, COR)
        fr(c, t, a_ + 0.5, 5, 6, xb, y, s)
        ny, dy = y + s * NY, y + s * DY
        corte(c, t, b_ + 0.3, xa, ny, s, 1, b_ + 0.7, False)
        corte(c, t, b_ + 0.3, xb, dy, s, 2, b_ + 0.7, True)
        corte(c, t, c_ + 0.3, xb, ny, s, 1, c_ + 0.7, False)
        corte(c, t, c_ + 0.3, xa, dy, s, 2, c_ + 0.7, True)
        conta(c, t, b_, "3 e 6: ÷ 3", 1070, 300, 62, TINTA2)
        conta(c, t, c_, "5 e 10: ÷ 5", 1070, 400, 62, TINTA2)
        sinal(c, t, d_ - 0.3, "=", 1130, y + 80, 110)
        E.resultado(c, t, d_, 1, 4, 1320, y + 90, 110, 134, CERTO)
        E.frase(c, t, d_ + 0.3, ps("dos funcionários", "g", 66, CERTO), 1320, 800, "center")
    E.saida(c, t, C["s10"] - 0.1, cruz)

    if t >= C["s10"]:
        a0, b0, c0, f0 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.end"]
        x, y, w, h = 216, 300, 1488, 180
        ped = [(0, CERTO, ep(t, a0 + 0.4, 0.4))]
        E.foco(c, t, a0, 0.5, lambda p: E.chocolate(c, x, y, w, h, 4, ped, p))
        for i in range(4):
            conta_c(c, t, a0 + 0.2 + i * 0.1, "15", x + w * (i + 0.5) / 4, y + h / 2 + 34, 96, BR if i == 0 and t >= a0 + 0.4 else TINTA, "g")
        conta_c(c, t, a0, "60 ÷ 4 = 15 funcionários", W / 2, 230, 84, CERTO)
        E.frase(c, t, lerp(a0, b0, 0.8), ps("confira:", "i", 80, COR), XE, 620)
        fr(c, t, b0 - 0.3, 5, 6, 560, 585, 100)
        E.foco(c, t, b0, 0.45, lambda p: E.escreve(c, "de 60 = 50", 660, 615, 84, "b", TINTA, p))
        fr(c, t, c0 - 0.3, 3, 10, 560, 800, 100)
        E.foco(c, t, c0, 0.45, lambda p: E.escreve(c, "de 50 = 15", 660, 830, 84, "b", TINTA, p))
        tb = lerp(c0, f0, 0.4)
        E.foco(c, t, tb, 0.5, lambda p: E.selo(c, 1320, 720, 76, True, p))
        E.frase(c, t, tb, ps("bateu", "g", 96, CERTO), 1430, 755)


# ---------------- situação 3: fração do restante ----------------
def b_questao3(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s11.{k}"] for k in "abcde")
    selo(c, t, a_, 3)
    E.frase(c, t, b_, ps("240", "g", 110, COR) + ps("caixas no caminhão", "i", 88), XE, 300, passo=0.26)
    E.frase(c, t, c_ - 0.5, ps("1ª parada:", "i", 84), XE, 455)
    fr(c, t, c_, 3, 8, 630, 425, 100, COR)
    E.frase(c, t, d_ - 0.4, ps("2ª parada:", "i", 84), XE, 670)
    fr(c, t, d_, 1, 5, 630, 640, 100, COR)
    E.frase(c, t, d_ + 0.4, ps("do restante", "g", 74), 720, 670)
    E.frase(c, t, e_, ps("quantas", "i", 110) + ps("continuam?", "g", 104, COR), XE, 900, passo=0.2)
    E.relogio(c, t, C["s12.a"], 1570, 320, 170)


def b_resposta3(c, t, C, b):
    selo(c, t, C["s13"] + 0.1, 3)
    a_, b_, c_, d_, e_, f_, g_, h_ = (C[f"s13.{k}"] for k in "abcdefgh")
    fim = C["s13.end"]
    x, y, w, h, cai = 216, 340, 1488, 130, 150
    lp = w / 8
    ped = []
    for i in range(8):
        if i < 3:
            q, dy, cor = ep(t, b_ + i * 0.1, 0.4), cai * ease_io(prog(t, b_ + 0.5, 0.7)), M.mix(CLARO, E.COR, ep(t, b_, 0.4))
        elif i == 3:
            q, dy, cor = 1, cai * ease_io(prog(t, e_, 0.7)), M.mix(CLARO, TINTA, ep(t, e_, 0.4))
        else:
            q, dy, cor = 1, 0, M.mix(CLARO, CERTO, ep(t, f_, 0.4))
        ped.append((i, cor, ep(t, a_ + 0.3 + i * 0.05, 0.3), dy))
    E.foco(c, t, a_, 0.5, lambda p: E.chocolate(c, x, y, w, h, 8, ped, p))
    for i in range(8):
        dy = ped[i][3]
        forte = (i < 3 and t >= b_) or (i == 3 and t >= e_) or (i > 3 and t >= f_)
        conta_c(c, t, a_ + 0.3 + i * 0.05, "30", x + (i + 0.5) * lp, y + dy + h / 2 + 24, 66, BR if forte else TINTA, "g")
    conta(c, t, a_, "240 ÷ 8 = 30", 830, 130, 66, TINTA)
    conta(c, t, b_, "× 3 = 90", 1310, 130, 66, COR)
    conta_c(c, t, b_ + 0.6, "90", x + 1.5 * lp, y + h + cai + 70, 72, COR, "g")
    E.saida(c, t, d_, lambda: (E.chave(c, x + 3 * lp, x + 8 * lp, y - 12, TINTA2, ep(t, c_, 0.4), -14, 4),
                               conta_c(c, t, c_, "ficam 150", x + 5.5 * lp, y - 42, 56, TINTA2)))
    E.saida(c, t, f_, lambda: (E.chave(c, x + 3 * lp, x + 8 * lp, y - 12, COR, ep(t, d_, 0.4), -14, 4),
                               conta_c(c, t, d_, "1/5 de 150, não de 240", x + 5.5 * lp, y - 42, 56, COR)))
    conta_c(c, t, e_, "30", x + 3.5 * lp, y + h + cai + 70, 72, TINTA, "g")
    E.chave(c, x + 4 * lp, x + 8 * lp, y - 12, CERTO, ep(t, f_, 0.4), -14, 4)
    conta_c(c, t, f_, "continuam 120", x + 6 * lp, y - 42, 60, CERTO, "g")
    # o erro
    conta(c, t, g_, "1/5 do total: 48", XE, 880, 66, ERRADO)
    conta(c, t, h_, "150 − 48 = 102", 800, 880, 66, ERRADO)
    th = lerp(h_, fim, 0.6)
    if t >= th:
        E.risco(c, 780, 895, 1320, 830, t, th, largura=10)
        conta(c, t, th, "errado", 1400, 880, 72, ERRADO, "g")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a_, b_, c_, d_, e_, f_ = (C[f"s14.{k}"] for k in "abcdef")

    def parte14():
        E.frase(c, t, C["s14"] + 0.1, ps("aqui cabe o atalho", "i", 76, CLARO), XE, 160)
        E.frase(c, t, a_, ps("multiplique", "g", 100, BR) + ps("só as sobras", "i", 110, BR), XE, 280)
        E.frase(c, t, lerp(a_, b_, 0.6), ps("saíram 3/8:", "i", 76, BR), XE, 450)
        E.foco(c, t, b_, 0.45, lambda p: E.escreve(c, "sobram", 610, 450, 76, "g", CLARO, p))
        fr(c, t, b_ + 0.1, 5, 8, 960, 420, 100, CLARO)
        E.frase(c, t, lerp(b_, c_, 0.45), ps("saiu 1/5 do restante:", "i", 76, BR), XE, 620)
        E.foco(c, t, c_, 0.45, lambda p: E.escreve(c, "sobram", 880, 620, 76, "g", CLARO, p))
        fr(c, t, c_ + 0.1, 4, 5, 1230, 590, 100, CLARO)
        s, xa, xb, y = 130, 400, 740, 855
        fr(c, t, d_, 4, 5, xa, y, s, BR)
        sinal(c, t, d_ + 0.3, "×", (xa + xb) / 2, y - 15, 110, BR)
        fr(c, t, d_ + 0.6, 5, 8, xb, y, s, BR)
        ny, dy = y + s * NY, y + s * DY
        tc = lerp(d_, e_, 0.45)
        corte(c, t, tc, xa, dy, s, 1, tc + 0.4, True, CLARO, CLARO)
        corte(c, t, tc, xb, ny, s, 1, tc + 0.4, False, CLARO, CLARO)
        tq = lerp(d_, e_, 0.75)
        corte(c, t, tq, xa, ny, s, 1, tq + 0.3, False, CLARO, CLARO)
        corte(c, t, tq, xb, dy, s, 2, tq + 0.3, True, CLARO, CLARO)
        sinal(c, t, e_ - 0.2, "=", 930, y - 15, 110, BR)
        E.foco(c, t, e_, 0.5, lambda p: E.fracao(c, 1, 2, 1060, y, s, CLARO, p))
        conta(c, t, lerp(e_, f_, 0.3), "metade de 240:", 1210, y - 30, 62, BR, "i")
        E.foco(c, t, f_, 0.5, lambda p: E.escreve(c, "120", 1210, y + 90, 130, "g", CLARO, p))
    E.saida(c, t, C["s15"] - 0.1, parte14)

    if t >= C["s15"]:
        a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
        E.frase(c, t, C["s15"] + 0.1, ps("funciona porque", "i", 84, CLARO), W / 2, 230, "center")
        E.frase(c, t, a5, ps("cada sobra é uma fração", "g", 96, BR), W / 2, 370, "center", 0.26)
        E.frase(c, t, a5 + 1.0, ps("da sobra anterior", "i", 104, BR), W / 2, 490, "center", 0.26)
        E.frase(c, t, b5 - 0.8, ps("não compensa se a pergunta for", "i", 70, CLARO), W / 2, 670, "center", 0.26)
        E.frase(c, t, b5, ps("quantas caixas saíram em uma parada", "g", 76, BR), W / 2, 780, "center", 0.26)
        E.frase(c, t, c5, ps("aí,", "i", 92, CLARO) + ps("calcule aquela parada", "g", 88, BR), W / 2, 920, "center")


# ---------------- situação 4: dividir com número misto ----------------
def b_questao4(c, t, C, b):
    a_, b_, c_, d_ = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    selo(c, t, a_, 4)
    E.frase(c, t, b_ - 0.5, ps("a costureira tem", "i", 88), XE, 320)
    misto(c, t, b_, 7, 1, 2, 920, 290, 104, COR)
    E.frase(c, t, b_ + 0.5, ps("metros", "g", 76), 1040, 320)
    E.frase(c, t, c_ - 0.4, ps("cada avental usa", "i", 88), XE, 540)
    fr(c, t, c_, 3, 4, 860, 510, 110, COR)
    E.frase(c, t, c_ + 0.4, ps("de metro", "g", 76), 960, 540)
    E.frase(c, t, d_, ps("quantos", "i", 110) + ps("aventais?", "g", 104, COR), XE, 830, passo=0.2)
    E.relogio(c, t, C["s17.a"], 1570, 320, 170)


def b_resposta4(c, t, C, b):
    selo(c, t, C["s18"] + 0.1, 4)
    a_, b_, c_, d_ = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    a9, b9, c9, d9, e9, f9, g9 = *(C[f"s19.{k}"] for k in "abcdef"), C["s19.end"]
    E.frase(c, t, lerp(C["s18"], a_, 0.4), ps("quantas vezes o avental", "i", 60) + ps("cabe no tecido?", "g", 54, COR), 810, 128, passo=0.26)

    def primeira():
        y = 270
        conta(c, t, a_, "isso é dividir", XE, 215, 62, COR)
        misto(c, t, b_ - 0.5, 7, 1, 2, 340, y + 40, 90, TINTA)
        sinal(c, t, b_, "=", 500, y + 25, 90)
        fr(c, t, b_ + 0.1, 15, 2, 630, y + 40, 110, COR)
    E.saida(c, t, C["s19"] - 0.1, primeira)
    s, xa, xb, y = 190, 400, 860, 630
    fr(c, t, c_, 15, 2, xa, y, s)
    E.saida(c, t, d_ + 0.2, lambda: sinal(c, t, c_ + 0.2, "÷", (xa + xb) / 2, y - 15, 130))
    sinal(c, t, d_ + 0.2, "×", (xa + xb) / 2, y - 15, 130, COR)
    vira(c, t, d_, 3, 4, xb, y, s, TINTA, ti=c_ + 0.4)
    ny, dy = y + s * NY, y + s * DY
    corte(c, t, a9 + 0.4, xa, ny, s, 5, a9 + 0.8, False)
    corte(c, t, a9 + 0.4, xb, dy, s, 1, a9 + 0.8, True)
    corte(c, t, b9 + 0.4, xb, ny, s, 2, b9 + 0.8, False)
    corte(c, t, b9 + 0.4, xa, dy, s, 1, b9 + 0.8, True)
    conta(c, t, a9, "15 e 3: ÷ 3", 1120, 260, 60, TINTA2)
    conta(c, t, b9, "4 e 2: ÷ 2", 1120, 345, 60, TINTA2)
    conta(c, t, c9, "5 × 2 =", 1120, 470, 84, TINTA, "g")
    E.foco(c, t, c9 + 0.2, 0.5, lambda p: num_bola(c, "10", 1490, 440, 90, 90, p, CERTO, BR))
    E.frase(c, t, c9 + 0.5, ps("aventais", "g", 56, CERTO), 1595, 465)
    conta(c, t, d9, "10 × 3/4 = 30/4", 1120, 620, 66, TINTA)
    E.foco(c, t, e9, 0.45, lambda p: E.escreve(c, "= 15/2", 1120, 710, 66, "b", CERTO, p))
    tb = lerp(e9, f9, 0.3)
    E.foco(c, t, tb, 0.45, lambda p: E.selo(c, 1420, 685, 46, True, p))
    E.frase(c, t, tb, ps("bateu", "g", 66, CERTO), 1485, 710)
    conta(c, t, f9, "virou a errada?", 1120, 850, 62, ERRADO, "i")
    conta(c, t, f9 + 0.5, "1/10 de avental", 1120, 930, 70, ERRADO)
    E.frase(c, t, lerp(f9, g9, 0.6), ps("impossível", "g", 66, ERRADO), 1120, 1010)


# ---------------- situação 5: expressão com negativa ----------------
def b_questao5(c, t, C, b):
    a_, b_, c_ = C["s20.a"], C["s20.b"], C["s20.c"]
    selo(c, t, a_ + 0.1, 5)
    E.frase(c, t, lerp(a_, b_, 0.3), ps("a última,", "i", 92) + ps("conta pura", "g", 86, COR), XE, 320)
    E.frase(c, t, b_ - 0.5, ps("resolva", "g", 130), XE, 480)
    y, s = 760, 170
    neg(c, t, b_, 5, 6, 400, y, s)
    sinal(c, t, c_, "+", 570, y - 15, 130)
    fr(c, t, c_ + 0.3, 1, 2, 750, y, s, COR)
    sinal(c, t, c_ + 0.8, "÷", 930, y - 15, 120)
    fr(c, t, c_ + 1.4, 3, 4, 1110, y, s, COR)
    E.relogio(c, t, C["s21.a"], 1570, 320, 170)


def b_resposta5(c, t, C, b):
    selo(c, t, C["s22"] + 0.1, 5)
    a_, b_, c_, d_ = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"]

    def blocos():
        E.frase(c, t, C["s22"] + 0.2, ps("em blocos", "g", 66, COR), 810, 130)
        y, s = 310, 130
        neg(c, t, C["s22"] + 0.2, 5, 6, 330, y, s)
        sinal(c, t, C["s22"] + 0.3, "+", 480, y - 15, 100)
        xa, xb = 640, 1000
        fr(c, t, C["s22"] + 0.4, 1, 2, xa, y, s, COR)
        sinal(c, t, C["s22"] + 0.5, "÷", (xa + xb) / 2, y - 15, 100)
        fr(c, t, C["s22"] + 0.6, 3, 4, xb, y, s, COR)
        bloco(c, 550, y - 140, 540, 280, ep(t, a_, 0.5), E.COR_TEXTO)
        E.frase(c, t, lerp(C["s22"], a_, 0.5), ps("o dividido vem antes do mais", "i", 58, TINTA2), 1140, 320, passo=0.26)
        yb, sb = 730, 170
        xa2, xb2 = 600, 980
        fr(c, t, b_, 1, 2, xa2, yb, sb)
        sinal(c, t, b_ + 0.2, "×", (xa2 + xb2) / 2, yb - 15, 120, COR)
        fr(c, t, b_ + 0.4, 4, 3, xb2, yb, sb)
        conta(c, t, lerp(a_, b_, 0.4), "conserva, vira, multiplica", XE, 520, 58, TINTA2, "i")
        ny, dy = yb + sb * NY, yb + sb * DY
        corte(c, t, c_, xa2, dy, sb, 1, c_ + 0.4, True)
        corte(c, t, c_, xb2, ny, sb, 2, c_ + 0.4, False)
        sinal(c, t, d_ - 0.2, "=", 1230, yb - 15, 110)
        E.resultado(c, t, d_, 2, 3, 1420, yb, 110, 134)
    E.saida(c, t, C["s23"] - 0.1, blocos)

    if t >= C["s23"]:
        a3, b3, c3, f3 = C["s23.a"], C["s23.b"], C["s23.c"], C["s23.end"]
        y, s = 300, 120
        neg(c, t, a3, 5, 6, 330, y, s)
        sinal(c, t, a3 + 0.4, "+", 460, y - 15, 90)
        fr(c, t, a3 + 0.7, 2, 3, 580, y, s)
        E.foco(c, t, lerp(a3, b3, 0.6), 0.45, lambda p: E.pilula(c, "MMC = 6", 870, y, 50, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
        neg(c, t, b3, 5, 6, 1180, y, s, COR)
        sinal(c, t, b3 + 0.4, "+", 1300, y - 15, 90)
        fr(c, t, b3 + 0.7, 4, 6, 1420, y, s, COR)
        tr = lerp(b3, c3, 0.15)
        vx = E.reta(c, t, tr, 260, 1560, 660, -5, 0, (-5, -1, 0), lambda v: f"−{abs(v)}" if v else "0", size=56)
        E.foco(c, t, tr + 0.3, 0.45, lambda p: E.bola(c, vx(-5), 660, 20, ERRADO, p))
        conta_c(c, t, tr + 0.3, "devia 5", vx(-5), 590, 56, ERRADO)
        E.salto(c, t, lerp(b3, c3, 0.5), vx(-5), vx(-1), 660, 130, CERTO, "pagou 4")
        E.foco(c, t, lerp(b3, c3, 0.85), 0.45, lambda p: E.bola(c, vx(-1), 660, 20, COR, p))
        conta_c(c, t, lerp(b3, c3, 0.85), "ainda deve 1", vx(-1) + 60, 590, 56, COR)
        E.frase(c, t, c3 - 0.1, ps("resposta:", "i", 84), 620, 900)
        neg(c, t, c3, 1, 6, 1120, 875, 124, CERTO)
        E.foco(c, t, c3 + 0.3, 0.45, lambda p: E.selo(c, 1290, 875, 60, True, p))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"] + 0.1, ps("resumindo", "i", 92, COR), W / 2, 180, "center")
        E.frase(c, t, C["s24.a"] - 0.5, ps("antes da conta,", "i", 80) + ps("descubra a operação", "g", 76, COR), W / 2, 320, "center", 0.26)
        itens = ((500, "s24.b", ps("falta", "g", 92, COR) + ps("é subtrair", "i", 96)),
                 (680, "s24.c", ps("a palavra", "i", 96) + ps("de", "g", 92, COR) + ps("é vezes", "i", 96)),
                 (860, "s24.d", ps("quantos cabem", "g", 92, COR) + ps("é dividir", "i", 96)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 460, y - 28, 56, 64, a))
            E.frase(c, t, C[k] + 0.1, partes, 550, y, passo=0.26)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    a_, b_, c_, d_, e_, f_ = (C[f"s25.{k}"] for k in "abcdef")
    E.frase(c, t, lerp(C["s25"], a_, 0.3), ps("na próxima aula", "i", 84), XE, 260)
    E.frase(c, t, a_, ps("números decimais", "g", 124, COR), XE, 410, passo=0.25)
    E.frase(c, t, b_, ps("ler", "i", 92) + ps("3,25", "g", 92, COR), XE, 570)
    E.frase(c, t, c_, ps("comparar", "i", 92), 620, 570)
    E.frase(c, t, d_, ps("arredondar", "i", 92), 1060, 570)
    E.foco(c, t, e_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 215, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, e_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1640, p), lerp(650, 260, p), ep(t, e_ + 0.2, 0.4), TINTA)
    E.frase(c, t, f_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 860, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
