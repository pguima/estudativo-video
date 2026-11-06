"""Visual — Estudativo · MAT-FRA-009: multiplicar frações.
A alma da aula é a grade (E.grade): colunas pintadas, faixas por cima, e o cruzamento vira a fração nova. O atalho é o corte
em cruz (E.corta), no palco escuro. Todo instante vem de C[...]: o que cai entre dois cues usa lerp(C[a], C[b], f)."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, palco, frac_q, centro, ponte
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-009_multiplicar_fracoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("de", "grade", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NY, DY = -0.565, 0.535  # centro do número de cima e do de baixo, em relação ao centro de uma fração de tamanho s

assert 30 // 5 == 6 and 6 * 2 == 12 and 2 * 30 == 60 and 60 // 5 == 12
assert 3 * 7 == 21 and 2 * 5 == 10 and 2 * 4 == 8
assert 3 * 2 == 6 and 4 * 5 == 20 and 6 // 2 == 3 and 20 // 2 == 10 and 7 * 7 == 49
assert 4 * 3 == 12 and 9 * 8 == 72 and 72 // 12 == 6 and 3 * 2 == 6
assert 2 * 5 * 4 == 5 * 8  # 2/5 de 5/8 = 1/4


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


def corte(c, t, t0, cx, cy, s, novo, tn, baixo=False, risco=None, tinta=None):
    """corte em cruz no número centrado em (cx, cy): embaixo da fração, o valor novo desce para não bater no traço"""
    E.corta(c, t, t0, cx, cy, s, None, risco or COR)
    yb = cy + s * 0.8 if baixo else cy - s * 0.5
    E.foco(c, t, tn, 0.4, lambda a: E.escreve(c, str(novo), cx + s * 0.38, yb, s * 0.56, "g", tinta or COR, a), sobe=8)


def pizza(c, cx, cy, r, a, p2, p3, p10):
    """a pizza: 5 fatias, 2 sobraram (p2); as 2 em 4 partes, 3 comidas (p3); e a pizza toda em 10 fatias (p10)"""
    if a <= 0:
        return
    ret = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.14 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 12))
    c.drawCircle(cx + 5, cy + 10, r, s)
    c.drawCircle(cx, cy, r, M.paint(E.VAZIO, a))
    if p2 > 0:
        c.drawArc(ret, -90, 144 * p2, True, M.paint(CLARO, a))
    if p3 > 0:
        c.drawArc(ret, -90, 108 * p3, True, M.paint(E.COR, a))
    raio = lambda g, q, cor: M.line(c, cx, cy, cx + r * M.math.cos(M.math.radians(g - 90)), cy + r * M.math.sin(M.math.radians(g - 90)), cor, a, 4, progress=q)
    for g in (0, 72, 144, 216, 288):
        raio(g, 1.0, BR if g <= 144 else FIO)
    if p3 > 0:
        for g in (36, 108):
            raio(g, p3, BR)
    if p10 > 0:
        for g in (180, 252, 324):
            raio(g, p10, FIO)
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=3))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def cena1():
        E.frase(c, t, C["s01"] + 0.1, ps("multiplicar sempre", "i", 92) + ps("aumenta?", "g", 84, COR), W / 2, 170, "center", 0.26)
        y, s = 370, 170
        fr(c, t, a1, 1, 2, 470, y, s, COR)
        sinal(c, t, lerp(a1, b1, 0.22), "×", 660, y - 15, 130)
        fr(c, t, lerp(a1, b1, 0.33), 1, 4, 850, y, s)
        sinal(c, t, b1 - 0.2, "=", 1050, y - 15, 130)
        E.resultado(c, t, b1, 1, 8, 1270, y, 130, 150)
        x, w, h = 620, 900, 90
        for yb, n, ti, cor in ((600, 2, c1 + 0.1, CLARO), (720, 4, lerp(c1, C["s01.end"], 0.55), CLARO), (840, 8, c1, E.COR)):
            E.foco(c, t, ti, 0.5, lambda a, yb=yb, n=n, cor=cor: (E.fracao(c, 1, n, 510, yb + 38, 56, COR, a), E.barra_fatias(c, x, yb, w, h, n, 1, cor, a)))
    E.saida(c, t, C["s02"] - 0.1, cena1)

    if C["s02"] <= t < C["s03"] + 0.3:
        a2, b2 = C["s02.a"], C["s02.b"]

        def cena2():
            E.frase(c, t, C["s02"] + 0.1, ps("não é", "i", 110) + ps("erro", "g", 100, COR), XE, 240)
            E.frase(c, t, a2, ps("vezes", "g", 130, COR) + ps("quer dizer", "i", 110), XE, 440)
            E.frase(c, t, lerp(a2, b2, 0.25), ps("pegar uma parte", "g", 120), XE, 590)
            E.frase(c, t, lerp(a2, b2, 0.5), ps("e ele se esconde em uma palavrinha", "i", 68), XE, 760, passo=0.26)
            r = 250 * ease_back(prog(t, b2, 0.7))
            if r > 0:
                E.bola(c, 1460, 640, r)
                centro(c, "de", 1460, 640 + 88, 250, "g", E.SOBRE, ep(t, b2 + 0.1, 0.4))
        E.saida(c, t, C["s03"] - 0.1, cena2)

    if t >= C["s03"]:
        a3, b3 = C["s03.a"], C["s03.b"]
        E.foco(c, t, b3 - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, b3 - 0.2, 0.7))), blur=0)
        E.frase(c, t, a3, ps("até o fim da aula", "i", 96), XE, 380)
        E.frase(c, t, lerp(a3, b3, 0.4), ps("multiplicar", "g", 132), XE, 530)
        E.frase(c, t, lerp(a3, b3, 0.55), ps("quaisquer", "i", 110) + ps("frações", "g", 118, COR), XE, 680)
        E.foco(c, t, b3 + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", E.SOBRE, a), E.escreve(c, "de prova", 1310, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, f_ = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.end"]
    E.frase(c, t, lerp(C["s04"], a_, 0.4), ps("você precisa de", "i", 84), XE, 410)
    E.foco(c, t, a_, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, a_ + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 225, 700, 120, "i", TINTA, a))
    x, w = 900, 830
    p = ep(t, b_, 0.5)
    E.caixa_pontilhada(c, x, 170, w, 230, p, prog_=p)
    E.frase(c, t, b_ + 0.1, ps("calcular a fração", "i", 70), x + 44, 265)
    E.frase(c, t, b_ + 0.4, ps("de uma quantidade", "g", 66, COR), x + 44, 350)
    p = ep(t, c_, 0.5)
    E.caixa_pontilhada(c, x, 450, w, 310, p, prog_=p)
    E.frase(c, t, c_ + 0.1, ps("simplificar", "g", 82, COR), x + 44, 555)
    E.frase(c, t, lerp(c_, f_, 0.12), ps("dividir em cima e embaixo", "i", 62), x + 44, 640, passo=0.26)
    E.frase(c, t, lerp(c_, f_, 0.5), ps("pelo mesmo número", "i", 62), x + 44, 715, passo=0.26)
    E.frase(c, t, lerp(c_, f_, 0.7), ps("faltou?", "g", 60, COR) + ps("procure a aula no canal", "i", 66), W / 2, 900, "center", 0.26)


# ---------------- de vira vezes ----------------
def b_de(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    x, y, w, h = XE, 590, 1580, 190

    def parte1():
        cy = 290
        fr(c, t, a5, 2, 5, 290, cy, 170, COR)
        E.foco(c, t, a5 + 0.3, 0.45, lambda a: E.escreve(c, "de", 410, cy + 40, 130, "i", TINTA, a))
        E.foco(c, t, a5 + 0.6, 0.45, lambda a: E.escreve(c, "30", 570, cy + 60, 170, "g", TINTA, a))
        E.frase(c, t, lerp(a5, b5, 0.5), ps("divide pelo de baixo:", "i", 60), 1000, 170, passo=0.26)
        conta(c, t, b5, "30 ÷ 5 = 6", 1000, 262, 84)
        E.frase(c, t, lerp(b5, c5, 0.25), ps("multiplica pelo de cima:", "i", 60), 1000, 370, passo=0.26)
        conta(c, t, c5, "6 × 2 = 12", 1000, 462, 84, COR)
        ped = [(i, E.COR, ep(t, c5 + i * 0.12, 0.3)) for i in range(2)]
        E.foco(c, t, a5 + 0.2, 0.5, lambda a: E.chocolate(c, x, y, w, h, 5, ped, a, ep(t, b5 - 0.5, 0.6)))
        for i in range(5):
            cx = x + w * (i + 0.5) / 5
            cor = E.SOBRE if i < 2 and t >= c5 else TINTA
            E.foco(c, t, b5 + i * 0.08, 0.35, lambda a, cx=cx, cor=cor: centro(c, "6", cx, y + h / 2 + 34, 96, "g", cor, a), sobe=8)
        q = ep(t, c5, 0.4)
        E.chave(c, x, x + w * 2 / 5, y + h + 14, COR, q, 18, 5)
        conta_c(c, t, c5 + 0.1, "12", x + w / 5, y + h + 118, 84, COR, "g")
    E.saida(c, t, C["s06"] - 0.1, parte1)

    if t >= C["s06"]:
        a6, b6, c6, d6, e6, f6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"], C["s06.end"]
        E.frase(c, t, C["s06"] + 0.1, ps("você pegou", "i", 80) + ps("uma parte", "g", 74, COR) + ps("de 30", "i", 80), W / 2, 170, "center", 0.26)
        E.foco(c, t, a6, 0.45, lambda a: centro(c, "de", 790, 350, 150, "g", COR, a))
        if t >= b6:
            p = ep(t, b6, 0.5)
            M.arrow(c, 910, 310, 1020, 310, TINTA, p, 6, 20, p)
        E.foco(c, t, b6, 0.5, lambda a: num_bola(c, "×", 1120, 305, 88, 130, a))
        cy, s = 590, 112
        fr(c, t, c6, 2, 5, 250, cy, s, COR)
        E.foco(c, t, c6 + 0.2, 0.45, lambda a: E.escreve(c, "de", 325, cy + 30, 90, "i", TINTA, a))
        E.foco(c, t, c6 + 0.4, 0.45, lambda a: E.escreve(c, "30", 430, cy + 36, 112, "g", TINTA, a))
        cm = lerp(c6, d6, 0.15)
        sinal(c, t, cm, "=", 625, cy - 15, 84)
        fr(c, t, cm + 0.2, 2, 5, 745, cy, s, COR)
        sinal(c, t, cm + 0.5, "×", 840, cy - 15, 84)
        E.foco(c, t, cm + 0.7, 0.45, lambda a: E.escreve(c, "30", 890, cy + 36, 112, "g", TINTA, a))
        sinal(c, t, d6 - 0.2, "=", 1085, cy - 15, 84)
        fr(c, t, d6, 60, 5, 1215, cy, s)
        sinal(c, t, e6 + 0.5, "=", 1355, cy - 15, 84)
        E.foco(c, t, lerp(e6, f6, 0.22), 0.5, lambda a: num_bola(c, "12", 1510, cy - 2, 108, 100, a, CERTO, BR))
        E.frase(c, t, lerp(c6, d6, 0.55), ps("o inteiro multiplica", "i", 58) + ps("só o de cima", "g", 54, COR), XE, 790, passo=0.26)
        conta(c, t, d6, "2 × 30 = 60", 1050, 790, 58)
        conta(c, t, e6, "60 ÷ 5 = 12", 1410, 790, 58)
        E.frase(c, t, lerp(e6, f6, 0.34), ps("o mesmo", "i", 74) + ps("resultado", "g", 68, CERTO), W / 2, 890, "center")
        E.frase(c, t, lerp(e6, f6, 0.57), ps("e se a quantidade for", "i", 74) + ps("outra fração?", "g", 68, COR), W / 2, 985, "center", 0.26)


# ---------------- grade ----------------
GX, GY, GW, GH = 900, 225, 810, 570


def b_grade(c, t, C, b):
    a7, b7, c7, f7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.end"]
    a8, b8 = C["s08.a"], C["s08.b"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    tb = lerp(a7, b7, 0.49)  # "uma barra de chocolate"
    # título: a conta que a grade vai fazer
    fr(c, t, a7, 2, 3, 250, 230, 130, COR)
    E.foco(c, t, a7 + 0.3, 0.45, lambda a: E.escreve(c, "de", 345, 262, 100, "i", TINTA, a))
    fr(c, t, a7 + 0.6, 5, 7, 530, 230, 130)
    # a barra: colunas, pintura e faixas descem no tempo da fala
    ap, ec, el = ep(t, tb, 0.5), ep(t, c7, 0.9), ep(t, b8, 0.9)
    pronto = t >= a8 + 1.2
    E.grade(c, GX, GY, GW, GH, 7 if pronto else 1, 3 if pronto else 1, 5 if pronto else 5 / 7, 2 if pronto else 2 / 3, ap, ec, el)
    if not pronto:
        for i in range(1, 7):
            q = ep(t, b7 + (i - 1) * 0.11, 0.3)
            if q > 0:
                M.line(c, GX + GW * i / 7, GY, GX + GW * i / 7, GY + GH * q, FIO, ap, 3, cap_round=False)
        for j in range(1, 3):
            q = ep(t, a8 + (j - 1) * 0.2, 0.4)
            if q > 0:
                M.line(c, GX, GY + GH * j / 3, GX + GW * q, GY + GH * j / 3, FIO, ap, 3, cap_round=False)
    q = ep(t, b7, 0.5)
    E.chave(c, GX, GX + GW, GY - 14, TINTA2, q, -16, 4)
    conta_c(c, t, b7, "7 colunas", GX + GW / 2, GY - 48, 54, TINTA2)
    # coluna da esquerda
    E.frase(c, t, c7, ps("pinte", "i", 70) + ps("5:", "g", 66, COR), XE, 460)
    E.frase(c, t, lerp(c7, f7, 0.55), ps("5/7", "g", 66, COR) + ps("da barra", "i", 70), 420, 460)
    E.frase(c, t, C["s08"] + 0.3, ps("2/3", "g", 62, COR) + ps("dessa parte:", "i", 70), XE, 560)
    E.frase(c, t, a8, ps("3 faixas,", "g", 62), XE, 650)
    E.frase(c, t, b8, ps("marque", "i", 70) + ps("2", "g", 66, COR), 480, 650)
    conta(c, t, a9, "3 × 7 = 21", XE, 760, 76)
    conta(c, t, a9 + 0.5, "quadradinhos", 540, 760, 54, TINTA2, "i")
    conta(c, t, b9, "2 × 5 = 10", XE, 860, 76, COR)
    conta(c, t, b9 + 0.5, "pintados e marcados", 540, 860, 44, TINTA2, "i")
    # os quadradinhos que contam
    n = 0
    for lin in range(2):
        for col in range(5):
            E.foco(c, t, b9 + n * 0.07, 0.3, lambda a, n=n, lin=lin, col=col: centro(c, str(n + 1), GX + GW * (col + 0.5) / 7, GY + GH * (lin + 0.5) / 3 + 24, 66, "g", E.SOBRE, a), sobe=6)
            n += 1
    p = ep(t, a9, 0.5) * (1 - ep(t, b9, 0.3))
    E.caixa_pontilhada(c, GX - 12, GY - 12, GW + 24, GH + 24, p, E.COR_TEXTO, prog_=p)
    E.resultado(c, t, c9, 10, 21, 1180, 925, 92, 112)
    E.frase(c, t, c9 + 0.3, ps("da barra", "i", 84), 1320, 950)


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    a0, b0, c0, d0 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]

    def regra():
        cy, s = 390, 180
        fr(c, t, C["s10"], 2, 3, 460, cy, s)
        sinal(c, t, C["s10"] + 0.1, "×", 655, cy - 15, 130)
        fr(c, t, C["s10"] + 0.2, 5, 7, 850, cy, s)
        sinal(c, t, C["s10"] + 0.3, "=", 1060, cy - 15, 130)
        fr(c, t, C["s10"] + 0.4, 10, 21, 1320, cy, s, COR)
        q = ep(t, a0, 0.5)
        E.caixa_pontilhada(c, 360, cy - 190, 1120, 165, q, E.COR_TEXTO, prog_=q)
        q = ep(t, b0, 0.5)
        E.caixa_pontilhada(c, 360, cy + 25, 1120, 165, q, TINTA, prog_=q)
        conta(c, t, a0, "2 × 5", 1540, cy - 80, 76, COR)
        conta(c, t, b0, "3 × 7", 1540, cy + 130, 76)
        E.frase(c, t, lerp(b0, c0, 0.08), ps("parte de uma parte", "i", 74) + ps("é multiplicação", "g", 68, COR), W / 2, 700, "center", 0.26)
        E.frase(c, t, c0, ps("multiplica", "g", 96, COR) + ps("os de cima", "i", 104), W / 2, 850, "center")
        E.frase(c, t, d0, ps("multiplica", "g", 96, COR) + ps("os de baixo", "i", 104), W / 2, 980, "center")
    E.saida(c, t, C["s11"] - 0.1, regra)

    if C["s11"] <= t < C["s12"] + 0.3:
        a1, b1 = C["s11.a"], C["s11.b"]

        def novo():
            E.frase(c, t, C["s11"] + 0.1, ps("sem", "g", 88, COR) + ps("igualar os denominadores", "i", 96), W / 2, 240, "center", 0.26)
            E.frase(c, t, lerp(C["s11"], a1, 0.55), ps("isso é da soma,", "i", 70) + ps("assunto de outra aula", "i", 70, TINTA2), W / 2, 350, "center", 0.26)
            E.frase(c, t, a1, ps("a própria conta cria", "i", 96) + ps("o pedaço novo", "g", 88, COR), W / 2, 520, "center", 0.26)
            E.foco(c, t, b1, 0.5, lambda a: E.grade(c, 960, 620, 560, 300, 7, 3, 1, 1, a))
            E.frase(c, t, b1 + 0.1, ps("21", "g", 150, COR) + ps("avos", "i", 130), XE + 200, 820)
        E.saida(c, t, C["s12"] - 0.1, novo)

    if t >= C["s12"]:
        a2, b2, c2, d2, f2 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.end"]
        cy, s = 260, 140
        E.frase(c, t, C["s12"] + 0.1, ps("e aquele", "i", 84), XE, 280)
        fr(c, t, C["s12"] + 0.6, 1, 2, 660, cy, s, COR)
        sinal(c, t, C["s12"] + 0.8, "×", 800, cy - 15, 100)
        fr(c, t, C["s12"] + 1.0, 1, 4, 940, cy, s)
        sinal(c, t, a2 - 0.2, "=", 1095, cy - 15, 100)
        if t < d2:
            frac_q(c, t, a2, 1, 8, a2 + 0.2, b2 + 0.5, 1280, cy, s)
        else:
            E.resultado(c, t, d2 - 0.4, 1, 8, 1290, cy, 110, 130)
        x, y, w, h = 300, 490, 1320, 130
        # um quarto da barra, e a metade dele
        E.foco(c, t, c2, 0.5, lambda a: (E.fracao(c, 1, 4, 205, y + 50, 60, TINTA, a), E.barra_fatias(c, x, y, w, h, 4, 1, CLARO, a)))
        q = ep(t, c2 + 0.4, 0.6)
        if q > 0:
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14)
            c.save(); c.clipRRect(r, True)
            c.drawRect(skia.Rect.MakeXYWH(x, y, w / 8, h * q), M.paint(E.COR))
            c.restore()
            E.chave(c, x, x + w / 8, y + h + 12, COR, q, 16, 4)
            conta(c, t, c2 + 0.5, "a metade de 1/4", x, y + h + 100, 62, COR)
        E.frase(c, t, lerp(c2, d2, 0.3), ps("só uma parte de um pedaço", "i", 72) + ps("dá menos que o pedaço", "g", 64, COR), W / 2, 850, "center", 0.26)
        E.frase(c, t, lerp(d2 - 0.2, d2, 0.0), ps("por isso", "i", 92) + ps("diminuiu", "g", 96, COR), W / 2, 980, "center")


# ---------------- treino ----------------
def b_treino(c, t, C, b):
    a_, b_, c_, d_, e_, f_, g_ = (C[f"s13.{k}"] for k in "abcdefg")
    cx, cy, r = 1530, 345, 245
    # o problema
    E.frase(c, t, C["s13"] + 0.1, ps("vamos treinar", "i", 72, COR), XE, 150)
    E.frase(c, t, lerp(C["s13"], a_, 0.8), ps("sobraram", "i", 84), XE, 300)
    fr(c, t, a_, 2, 5, 590, 270, 96, COR)
    E.frase(c, t, a_ + 0.5, ps("da pizza", "g", 72), 670, 300)
    E.frase(c, t, b_ - 0.5, ps("comeu", "i", 84), XE, 450)
    fr(c, t, b_, 3, 4, 500, 420, 96, COR)
    E.frase(c, t, b_ + 0.5, ps("disso", "g", 72), 580, 450)
    pizza(c, cx, cy, r, ep(t, a_, 0.5), ep(t, a_ + 0.2, 0.7), ep(t, b_ + 0.2, 0.7), ep(t, g_, 0.6))
    # a conta
    ti = lerp(b_, c_, 0.5)
    y, s = 680, 120
    fr(c, t, ti, 3, 4, 250, y, s, COR)
    sinal(c, t, ti + 0.2, "×", 385, y - 15, 90)
    fr(c, t, ti + 0.4, 2, 5, 520, y, s)
    sinal(c, t, e_ - 0.2, "=", 655, y - 15, 90)
    frac_q(c, t, c_ - 0.2, 6, 20, c_ + 0.2, d_ + 0.3, 800, y, s)
    conta(c, t, c_, "3 × 2 = 6", XE, 900, 64)
    conta(c, t, d_, "4 × 5 = 20", 520, 900, 64)
    if t >= f_:
        E.pontes(c, t, 880, 1060, y, s, "÷ 2", f_, f_, size=44)
    E.resultado(c, t, g_, 3, 10, 1190, y, 104, 124, CERTO)
    E.frase(c, t, g_ + 0.3, ps("da pizza", "g", 72, CERTO), 1340, 730)
    conta(c, t, f_ + 0.2, "6 e 20 são pares", 960, 900, 56, TINTA2, "i")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    a5, b5, c5, f5 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.end"]
    E.frase(c, t, C["s14"] + 0.1, ps("cuidado", "g", 92, ERRADO) + ps("com um erro comum", "i", 96), XE, 170)
    E.frase(c, t, a4, ps("repetir", "g", 88, ERRADO) + ps("o de baixo", "i", 96), XE, 290)
    y, s = 470, 140
    fr(c, t, b4, 2, 7, 260, y, s)
    sinal(c, t, b4 + 0.3, "×", 400, y - 15, 104)
    fr(c, t, b4 + 0.6, 3, 7, 540, y, s, COR)
    sinal(c, t, c4 - 0.2, "=", 695, y - 15, 104)
    fr(c, t, c4, 6, 7, 850, y, s, ERRADO)
    if t >= b5:
        E.risco(c, 770, y + 120, 930, y - 130, t, b5 - 0.1, largura=14)
    # as barras mostram que não pode dar seis sétimos
    x, w, h = 400, 860, 86
    y1, y2 = 690, 830
    E.foco(c, t, lerp(C["s15"], a5, 0.6), 0.5, lambda a: (E.fracao(c, 3, 7, 300, y1 + 34, 56, COR, a), E.barra_fatias(c, x, y1, w, h, 7, 3, E.COR, a)))
    ti = lerp(a5, b5, 0.28)
    E.foco(c, t, ti, 0.5, lambda a: (E.fracao(c, 6, 7, 300, y2 + 34, 56, ERRADO, a), E.barra_fatias(c, x, y2, w, h, 7, 6, ERRADO, a)))
    conta(c, t, a5, "tem que dar menos", 1300, y1 + 62, 50, COR)
    conta(c, t, lerp(a5, b5, 0.5), "é o dobro", 1300, y2 + 62, 58, ERRADO)
    conta(c, t, b5, "7 × 7 = 49", 1090, y - 16, 64, TINTA)
    sinal(c, t, c5 - 0.2, "=", 1475, y - 15, 104)
    E.resultado(c, t, c5, 6, 49, 1640, y, 100, 128, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def apresenta():
        a6, b6, c6, f6 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.end"]
        E.frase(c, t, C["s16"] + 0.1, ps("agora, o atalho", "i", 84, CLARO), W / 2, 200, "center")
        E.frase(c, t, a6, ps("cortar", "g", 170, BR) + ps("em cruz", "i", 180, BR), W / 2, 390, "center")
        y, s = 680, 150
        fr(c, t, b6, 4, 9, 440, y, s, BR)
        sinal(c, t, b6 + 0.3, "×", 610, y - 15, 110, BR)
        fr(c, t, b6 + 0.6, 3, 8, 780, y, s, BR)
        sinal(c, t, c6 - 0.2, "=", 960, y - 15, 110, BR)
        fr(c, t, c6, 12, 72, 1160, y, s, CLARO)
        E.frase(c, t, lerp(c6, f6, 0.45), ps("e ainda falta", "i", 76, CLARO) + ps("simplificar", "g", 72, BR), W / 2, 960, "center", 0.26)
    E.saida(c, t, C["s17"] - 0.1, apresenta)

    if C["s17"] <= t < C["s18"] + 0.3:
        a7, b7, c7, d7, e7, f7, g7 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"], C["s17.e"], C["s17.f"], C["s17.end"]

        def cruz():
            E.frase(c, t, C["s17"] + 0.1, ps("antes de multiplicar,", "i", 78, CLARO) + ps("olhe na diagonal", "g", 72, BR), W / 2, 160, "center", 0.26)
            s, xa, xb, y = 200, 330, 780, 500
            fr(c, t, C["s17"], 4, 9, xa, y, s, BR)
            fr(c, t, C["s17"] + 0.2, 3, 8, xb, y, s, BR)
            ny, dy = y + s * NY, y + s * DY
            if t >= a7:
                M.line(c, xa + 80, ny + 10, xb - 80, dy - 10, CLARO, 1.0, 7, progress=ep(t, a7, 0.6))
            if t >= c7:
                M.line(c, xb - 80, ny + 10, xa + 80, dy - 10, CLARO, 1.0, 7, progress=ep(t, c7, 0.6))
            c.drawCircle((xa + xb) / 2, y, 60, M.paint("#0F0B38"))
            sinal(c, t, C["s17"] + 0.3, "×", (xa + xb) / 2, y - 6, 120, BR)
            corte(c, t, lerp(a7, b7, 0.6), xa, ny, s, 1, b7, False, CLARO, CLARO)
            corte(c, t, lerp(a7, b7, 0.6), xb, dy, s, 2, b7, True, CLARO, CLARO)
            corte(c, t, lerp(c7, d7, 0.6), xb, ny, s, 1, d7, False, CLARO, CLARO)
            corte(c, t, lerp(c7, d7, 0.6), xa, dy, s, 3, d7, True, CLARO, CLARO)
            tc, tb = lerp(d7, e7, 0.25), lerp(d7, e7, 0.6)
            sinal(c, t, tc, "=", 1040, y - 15, 110, BR)
            E.foco(c, t, tc, 0.45, lambda a: centro(c, "1 × 1", 1270, y - 44, 100, "g", BR, a))
            E.foco(c, t, tc, 0.4, lambda a: c.drawRect(skia.Rect.MakeXYWH(1120, y - 3, 300, 7), M.paint(BR, a)))
            E.foco(c, t, tb, 0.45, lambda a: centro(c, "3 × 2", 1270, y + 106, 100, "g", BR, a))
            sinal(c, t, e7 - 0.2, "=", 1480, y - 15, 110, BR)
            E.foco(c, t, e7, 0.5, lambda a: E.fracao(c, 1, 6, 1620, y, 170, CLARO, a))
            E.frase(c, t, f7 - 0.5, ps("o mesmo valor de", "i", 72, CLARO) + ps("12/72,", "g", 66, BR) + ps("com muito menos trabalho", "i", 72, CLARO), W / 2, 950, "center", 0.26)
        E.saida(c, t, C["s18"] - 0.1, cruz)

    if t >= C["s18"]:
        a8, b8, c8, f8 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.end"]

        def porque():
            E.frase(c, t, a8, ps("é", "i", 96, CLARO) + ps("simplificar", "g", 92, BR) + ps("antes da conta", "i", 96, CLARO), W / 2, 190, "center")
            y, s = 500, 120
            q1, q2 = lerp(a8, b8, 0.14), lerp(a8, b8, 0.26)
            foc = lambda ti, txt, yy: E.foco(c, t, ti, 0.45, lambda a: centro(c, txt, 520, yy, s, "g", BR, a))
            foc(q1, "4 × 3", y - 34)
            E.foco(c, t, q1, 0.4, lambda a: c.drawRect(skia.Rect.MakeXYWH(300, y - 4, 440, 8), M.paint(BR, a)))
            foc(q2, "9 × 8", y + 128)
            conta(c, t, q1, "os de cima em uma linha", 860, y - 44, 66, CLARO)
            conta(c, t, q2, "os de baixo em outra", 860, y + 112, 66, CLARO)
            E.frase(c, t, lerp(a8, b8, 0.5), ps("tanto faz de qual fração vem cada número", "i", 70, CLARO), W / 2, 800, "center", 0.26)
            E.frase(c, t, lerp(a8, b8, 0.7), ps("divida um de cima e um de baixo", "g", 62, BR), W / 2, 920, "center", 0.26)
        E.saida(c, t, b8 - 1.2, porque)

        if t >= b8 - 1.0:
            E.frase(c, t, b8 - 1.0, ps("não compensa quando", "i", 92, CLARO), W / 2, 220, "center")
            E.frase(c, t, b8, ps("a diagonal não tem", "i", 84, BR) + ps("divisor comum", "g", 80, BR), W / 2, 350, "center", 0.26)
            y, s = 580, 150
            tx = lerp(b8, c8, 0.5)
            fr(c, t, tx, 2, 3, 760, y, s, BR)
            sinal(c, t, tx + 0.2, "×", 960, y - 15, 110, BR)
            fr(c, t, tx + 0.4, 5, 7, 1160, y, s, BR)
            E.frase(c, t, c8, ps("só vale na", "i", 120, CLARO) + ps("multiplicação", "g", 110, BR), W / 2, 930, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_, c_ = C["s19.a"], C["s19.b"], C["s19.c"]
    E.frase(c, t, C["s19"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180)
    fr(c, t, a_, 5, 8, 240, 325, 104, COR)
    E.frase(c, t, a_ + 0.4, ps("do terreno", "g", 76) + ps("plantados", "i", 84), 330, 357)
    fr(c, t, b_, 2, 5, 240, 570, 104, COR)
    E.frase(c, t, b_ + 0.4, ps("da parte plantada", "g", 70), 330, 570)
    E.frase(c, t, b_ + 1.0, ps("são de milho", "i", 84), 330, 660)
    E.frase(c, t, c_, ps("que fração do", "i", 96) + ps("terreno inteiro", "g", 88, COR), XE, 850, passo=0.26)
    E.frase(c, t, c_ + 1.0, ps("tem milho?", "i", 96), XE, 960)
    E.relogio(c, t, C["s20.a"], 1530, 350, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s21.{k}"] for k in "abcde")
    s, xa, xb, y = 200, 330, 800, 520
    E.frase(c, t, C["s21"] + 0.1, ps("vamos lá", "i", 72, COR), XE, 170)
    fr(c, t, a_ - 0.5, 2, 5, xa, y, s)
    fr(c, t, a_ + 0.2, 5, 8, xb, y, s)
    xm = (xa + xb) / 2
    E.saida(c, t, b_, lambda: E.foco(c, t, a_, 0.4, lambda a: centro(c, "de", xm, y + 34, 130, "i", TINTA, a)))
    sinal(c, t, b_, "×", xm, y - 15, 130, COR)
    ny, dy = y + s * NY, y + s * DY
    corte(c, t, c_, xa, dy, s, 1, c_ + 0.4, True)
    corte(c, t, c_ + 0.2, xb, ny, s, 1, c_ + 0.6, False)
    corte(c, t, lerp(d_, e_, 0.2), xa, ny, s, 1, lerp(d_, e_, 0.32), False)
    corte(c, t, lerp(d_, e_, 0.2), xb, dy, s, 4, lerp(d_, e_, 0.32), True)
    conta(c, t, c_, "5 e 5", 1090, 300, 64, TINTA2)
    conta(c, t, d_, "2 e 8: ÷ 2", 1090, 390, 64, TINTA2)
    sinal(c, t, e_ - 0.3, "=", 1120, y + 80, 120)
    E.resultado(c, t, e_, 1, 4, 1340, y + 90, 130, 158, CERTO)
    E.frase(c, t, e_ + 0.3, ps("do terreno", "g", 76, CERTO) + ps("tem milho", "i", 84), W / 2 + 150, 880, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.1, ps("resumindo", "i", 92, COR), W / 2, 180, "center")
        itens = ((340, "s22.a", ps("a palavra", "i", 88) + ps("de", "g", 84, COR) + ps("vira", "i", 88) + ps("vezes", "g", 84, COR)),
                 (510, "s22.b", ps("multiplica", "g", 84, COR) + ps("em cima", "i", 88)),
                 (680, "s22.c", ps("multiplica", "g", 84, COR) + ps("embaixo", "i", 88)),
                 (850, "s22.d", ps("corta em cruz", "g", 84, COR) + ps("antes, se der", "i", 88)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 340, y - 28, 56, 64, a))
            E.frase(c, t, C[k] + 0.1, partes, 430, y, passo=0.26)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a_, b_, c_, d_ = C["s23.a"], C["s23.b"], C["s23.c"], C["s23.d"]
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 84), XE, 280)
    E.frase(c, t, a_, ps("gastar", "g", 104) + ps("1/3", "g", 104, COR) + ps("do dinheiro", "g", 104), XE, 430, passo=0.25)
    E.frase(c, t, b_, ps("e depois", "i", 96) + ps("1/4", "g", 104, COR) + ps("do que sobrou", "g", 96), XE, 580, passo=0.2)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 270, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1640, p), lerp(650, 315, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, de=b_de, grade=b_grade, regra=b_regra, treino=b_treino, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
