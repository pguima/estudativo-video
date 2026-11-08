"""Visual — Estudativo · MAT-RAZ-018: vazão e torneiras juntas.
Peças locais: caixa() é a caixa-d'água que enche (com marcas de fração na parede), torneira() solta o jato na hora da fala.
Todo instante vem de C[...]; o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
from fractions import Fraction as Fr
from decimal import Decimal as D

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-018_vazao_e_torneiras_juntas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("vazao", "juntas", "tempos", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert D(1500) / D("12.5") == 120 and D(15000) / 125 == 120 and 125 * 8 == 1000 and 15 * 8 == 120 and 120 / 60 == 2
assert 30 + 20 == 50 and 1500 / 50 == 30 and 1500 / 30 == 50
assert Fr(1, 3) + Fr(1, 6) == Fr(1, 2) and Fr(2, 6) + Fr(1, 6) == Fr(3, 6)
assert D("1.5") / D("12.5") == D("0.12") and D("0.12") * 60 < 10
assert 3 * 6 == 18 and 3 + 6 == 9 and 18 / 9 == 2 and 1 * 6 + 3 * 1 == 9
assert Fr(1, 4) + Fr(1, 12) == Fr(4, 12) == Fr(1, 3) and 4 * 12 == 48 and 4 + 12 == 16 and 48 / 16 == 3


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


def fcen(c, t, t0, s, cx, y, size, cor=None, est="g"):
    E.formula_em(c, t, t0, s, cx, y, size, est, cor, "center")


def bola_res(c, t, t0, s, cx, cy, r=130, size=80, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)))


def caixa(c, x, y, w, h, nivel, a=1.0, divs=0, cor=None, escuro=False):
    """caixa-d'água: (x, y) = canto de cima à esquerda; nivel 0..1 de água; divs = marcas de fração na parede"""
    if a <= 0:
        return
    cor = cor or E.COR
    tinta = BR if escuro else TINTA
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18)
    c.drawRRect(rr, M.paint("#FFFFFF" if not escuro else "#FFFFFF", a * (0.9 if not escuro else 0.08)))
    nivel = max(0.0, min(1.0, nivel))
    if nivel > 0:
        c.save(); c.clipRRect(rr, True)
        c.drawRect(skia.Rect.MakeXYWH(x, y + h * (1 - nivel), w, h * nivel), M.paint(cor, a * 0.88))
        c.drawRect(skia.Rect.MakeXYWH(x, y + h * (1 - nivel), w, 6), M.paint(BR, a * 0.35))
        c.restore()
    for k in range(1, divs):
        yy = y + h * k / divs
        M.line(c, x + 4, yy, x + w - 4, yy, BR if (1 - k / divs) < nivel - 1e-6 else FIO, a, 3, dash=[12, 10])
    c.drawRRect(rr, M.paint(tinta, a, stroke=5))


def torneira(c, x, y, s, a=1.0, jorro=0.0, ate=None, escuro=False):
    """torneira com o bico em (x, y) apontando para baixo; jorro 0..1 desce até `ate`"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA2
    M.rrect(c, x - s * 1.6, y - s * 0.95, s * 1.75, s * 0.5, s * 0.12, tinta, a)  # cano
    M.rrect(c, x - s * 0.25, y - s * 0.95, s * 0.5, s * 0.95, s * 0.12, tinta, a)  # bico
    M.rrect(c, x - s * 0.95, y - s * 1.35, s * 0.18, s * 0.42, s * 0.06, tinta, a)  # registro
    M.rrect(c, x - s * 1.2, y - s * 1.45, s * 0.7, s * 0.16, s * 0.08, tinta, a)
    if jorro > 0 and ate is not None:
        yb = lerp(y, ate, min(1.0, jorro))
        c.drawRect(skia.Rect.MakeXYWH(x - s * 0.13, y, s * 0.26, yb - y), M.paint(E.COR, a * 0.75))


def conjunto(c, t, t0, cx, yt, w, h, nivel, jorro, divs=0, s=46, cor=None):
    """torneira sobre a caixa, centrados em cx; yt = topo da caixa"""
    a = ep(t, t0, 0.5)
    if a <= 0:
        return
    bx = cx - w / 2
    caixa(c, bx, yt, w, h, nivel, a, divs, cor)
    tx = bx + w * 0.3
    torneira(c, tx, yt - 40, s, a, jorro, yt + h * (1 - nivel) if nivel > 0 else yt + h)


def lembrete(c, t, C, cena, itens):
    """itens = [(cue, linha fina, linha forte)]"""
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 930, 860
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    q1, q2 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5)), ease_io(prog(t, C[itens[2][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(340, 580, q1), 820, q2), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[2][0]], C[cena + ".end"], 0.55), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1000, "left", 0.12)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]
    xa, xb, yt, w, h = 560, 1360, 300, 330, 330

    def um():
        # as duas enchem juntas a partir de "seis horas": a de 3 h no dobro da velocidade da de 6 h
        ta = b1 + 0.3
        enche_a, enche_b = prog(t, ta, 3.0), prog(t, ta, 6.0)
        conjunto(c, t, C["s01"] + 0.2, xa, yt, w, h, 0.95 * enche_a, ep(t, ta, 0.3) * (1 - ep(t, ta + 3.0, 0.2)), s=52)
        conjunto(c, t, a1 + 0.6, xb, yt, w, h, 0.95 * enche_b, ep(t, ta, 0.3) * (1 - ep(t, ta + 6.0, 0.2)), s=52)
        fcen(c, t, a1, "3 h", xa, 790, 120, COR)
        fcen(c, t, b1, "6 h", xb, 790, 120, TINTA)
        tq = lerp(b1, c1, 0.4)
        E.saida(c, t, c1 - 0.1, lambda: E.frase(c, t, tq, ps("as duas juntas:", "i", 84) + [("?", "g", 96, COR)], W / 2, 950, "center", 0.12))

        def chute():
            fcen(c, t, c1, "4 h 30 min?", W / 2, 960, 100, ERRADO)
            tr = lerp(c1, C["s01.end"], 0.6)
            if t >= tr:
                E.risco(c, W / 2 - 330, 985, W / 2 + 330, 890, t, tr, largura=14)
        if t >= c1:
            E.saida(c, t, C["s02.a"] - 0.1, chute)
        if t >= C["s02.a"]:
            E.frase(c, t, C["s02.a"], ps("com ajuda, enche", "i", 76) + [("mais rápido:", "g", 80, COR)], W / 2 - 260, 960, "center", 0.12)
            fcen(c, t, lerp(C["s02.a"], C["s02.b"], 0.5), "juntas < 3 h", W / 2 + 520, 965, 90, COR)
    E.saida(c, t, C["s02.b"] - 0.1, um)

    if t >= C["s02.b"] - 0.1:
        tb, tc = C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1450, 540, 280 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, tb, ps("até o fim da aula", "i", 92), XE, 360, passo=0.14)
        E.frase(c, t, tb + 0.8, [("acertar", "g", 132, COR)], XE, 520)
        E.frase(c, t, tb + 1.2, ps("o tempo das", "i", 96), XE, 660, passo=0.12)
        E.frase(c, t, tb + 1.6, ps("torneiras juntas", "i", 96, COR), XE, 780, passo=0.12)
        E.foco(c, t, tc + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1450, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1450, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "ler uma taxa,", "como km/h"), ("s03.c", "um metro cúbico guarda", "1.000 litros"),
                              ("s03.d", "somar frações com", "denominadores diferentes")))


# ---------------- vazão ----------------
def b_vazao(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]

    def ideia():
        E.frase(c, t, a4, [("vazão", "g", 150, COR)], XE, 260)
        E.frase(c, t, a4 + 0.6, ps("quanto líquido passa", "i", 76), XE, 380, passo=0.12)
        E.frase(c, t, b4, ps("a cada", "i", 76) + [("unidade de tempo", "g", 72, COR)], XE, 480, passo=0.12)
        # torneira: 12,5 L em cada minuto
        cx, yt, w, h = 1450, 500, 360, 380
        minutos = ep(t, c4 + 0.6, 3.2)
        conjunto(c, t, a4 + 0.4, cx, yt, w, h, 0.12 + 0.6 * minutos, ep(t, c4, 0.3), divs=4)
        E.foco(c, t, c4, 0.5, lambda a: E.pilula(c, "12,5 L/min", 700, 700, 84, "g", a=a, cor=E.SOBRE))
        for i in range(3):
            ti = lerp(c4, C["s04.end"], 0.25 + i * 0.22)
            E.foco(c, t, ti, 0.4, lambda a, i=i: E.escreve(c, f"{i + 1} min  →  {['12,5', '25', '37,5'][i]} L", 440, 840 + i * 80, 54, "b", TINTA2, a))
    E.saida(c, t, C["s05"] - 0.1, ideia)
    if t < C["s05"]:
        return

    def taxa():
        tv = lerp(C["s05"], C["s05.a"], 0.4)
        E.frase(c, t, C["s05"] + 0.2, ps("é uma", "i", 84) + [("taxa", "g", 90, COR)], W / 2, 190, "center", 0.12)
        fcen(c, t, tv, "velocidade = f{distância}{tempo}", W / 2, 400, 96, TINTA2)
        fcen(c, t, C["s05.a"], "vazão = f{volume}{tempo}", W / 2, 640, 110, COR)
        if t >= C["s05.b"]:
            E.foco(c, t, C["s05.b"], 0.5, lambda a: (E.pilula(c, "L/min", 760, 870, 80, "g", a=a, cor=E.SOBRE)))
            E.frase(c, t, C["s05.b"] + 0.3, [("por", "g", 80, COR)] + ps("é", "i", 80) + [("÷", "g", 90, COR)], 1180, 895, "center", 0.12)
    E.saida(c, t, C["s06"] - 0.1, taxa)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"] + 0.2, ps("a prova pergunta o", "i", 84) + [("tempo", "g", 90, COR)], W / 2, 260, "center", 0.12)
    fcen(c, t, lerp(C["s06"], C["s06.a"], 0.6), "velocidade = f{distância}{tempo}  →  tempo = f{distância}{velocidade}", W / 2, 470, 70, TINTA2)
    E.foco(c, t, C["s06.a"], 0.5, lambda a: (M.rrect(c, 420, 620, 1080, 300, 40, E.COR, a),
                                              E.formula(c, "tempo = f{volume}{vazão}", W / 2, 800, 120, "g", E.SOBRE, a, "center")))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    cx, yt, w, h = 1540, 330, 380, 420
    nivel = 0.95 * ep(t, b8, 2.0)
    conjunto(c, t, a7, cx, yt, w, h, nivel, ep(t, a7 + 1.0, 0.3))
    E.foco(c, t, a7, 0.5, lambda a: centro(c, "1.500 L", cx, yt + h + 100, 84, "g", TINTA, a))
    E.foco(c, t, lerp(a7, b7, 0.45), 0.5, lambda a: E.pilula(c, "12,5 L/min", cx - 160, yt - 150, 56, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, C["s07"] + 0.2, 0.5, lambda a: E.formula(c, "tempo = f{volume}{vazão}", XE, 210, 76, "g", TINTA2, a))

    def divisoes():
        fcen(c, t, b7, "1.500 ÷ 12,5", 650, 420, 110)
        tz = lerp(b7, c7, 0.5)
        E.foco(c, t, tz, 0.5, lambda a: E.pilula(c, "× 10 nos dois", 650, 530, 52, "g", a=a, cor=E.SOBRE))
        fcen(c, t, c7, "15.000 ÷ 125", 650, 690, 110, COR)
    E.saida(c, t, C["s08"] - 0.1, divisoes)
    if t < C["s08"]:
        return
    fcen(c, t, C["s08"] + 0.2, "15.000 ÷ 125", 650, 380, 96)
    fcen(c, t, lerp(C["s08"], a8, 0.25), "125 × 8 = 1.000", 650, 530, 76, TINTA2)
    E.frase(c, t, a8 - 0.6, ps("15.000 são", "i", 64) + [("15 × 1.000", "g", 64)], 650, 650, "center", 0.1)
    fcen(c, t, a8, "15 × 8 = 120", 650, 780, 96, COR)
    bola_res(c, t, b8, "120 min", 420, 940, 135, 56)
    fcen(c, t, c8, "÷ 60 = 2 h", 830, 965, 96, COR)


# ---------------- duas vazões ----------------
def b_juntas(c, t, C, b):
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    E.frase(c, t, C["s09"] + 0.2, ps("duas torneiras?", "i", 84) + [("some as vazões", "g", 84, COR)], W / 2, 170, "center", 0.12)
    yt, w, h = 400, 300, 300
    junta = ep(t, d9, 0.6)
    conjunto(c, t, b9, 420, yt, w, h, 0.08, ep(t, b9 + 0.3, 0.3), s=40)
    conjunto(c, t, c9, 900, yt, w, h, 0.08, ep(t, c9 + 0.3, 0.3), s=40)
    fcen(c, t, b9, "30 L/min", 420, 830, 72)
    fcen(c, t, c9, "20 L/min", 900, 830, 72)
    E.foco(c, t, b9 + 0.2, 0.5, lambda a: centro(c, "+", 660, 560, 110, "g", TINTA, a))
    fcen(c, t, d9, "= 50 L/min", 1480, 330, 96, COR)

    def conta():
        fcen(c, t, C["s10.a"], "1.500 ÷ 50", 1480, 520, 88)
        bola_res(c, t, C["s10.b"], "30 min", 1480, 700, 120, 66)
        tm = lerp(C["s10.b"], C["s10.c"], 0.3)
        fcen(c, t, tm, "só a de 30: 1.500 ÷ 30 = 50 min", W / 2, 990, 64, TINTA2)
    conta()
    if t >= C["s10.c"]:
        E.foco(c, t, C["s10.c"], 0.5, lambda a: E.selo(c, 1690, 640, 56, True, a))
        E.frase(c, t, C["s10.c"] + 0.1, [("juntas,", "i", 64), ("menos", "g", 64, CERTO)], 1480, 890, "center", 0.12)


# ---------------- só os tempos ----------------
def b_tempos(c, t, C, b):
    a11, b11 = C["s11.a"], C["s11.b"]
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    w, h, yt = 260, 360, 520
    xa, xb, xj = 330, 720, 1520
    a = ep(t, a11, 0.5)
    caixa(c, xa - w / 2, yt, w, h, Fr(1, 3) * ep(t, a12, 0.8), a, 3)
    caixa(c, xb - w / 2, yt, w, h, Fr(1, 6) * ep(t, b12, 0.8), a, 6)
    fcen(c, t, a11, "3 h", xa, yt - 40, 84, COR)
    fcen(c, t, a11 + 0.3, "6 h", xb, yt - 40, 84, TINTA)
    E.saida(c, t, b11 - 0.1, lambda: E.frase(c, t, C["s11"] + 0.3, ps("só conhecemos", "i", 84) + [("os tempos", "g", 90, COR)], W / 2, 200, "center", 0.12))
    E.frase(c, t, b11, ps("em", "i", 84) + [("1 hora,", "g", 90, COR)] + ps("quanto enche?", "i", 84), W / 2, 200, "center", 0.12)
    E.foco(c, t, a12, 0.5, lambda q: E.fracao(c, 1, 3, xa, yt + h + 80, 72, COR, q))
    E.foco(c, t, b12, 0.5, lambda q: E.fracao(c, 1, 6, xb, yt + h + 80, 72, TINTA, q))
    # conta à direita, em cima
    y = 440
    if t >= c12:
        fcen(c, t, c12, "f{1}{3} + f{1}{6}", 1300, y, 100)
    tm = lerp(C["s13"], a13, 0.3)
    E.foco(c, t, tm, 0.4, lambda q: E.pilula(c, "MMC = 6", 1300, 290, 50, "g", a=q, cor=E.SOBRE))
    fcen(c, t, a13, "= f{2}{6} + f{1}{6}", 1650, y, 100, TINTA2)
    # a terceira caixa: juntas, em 1 hora
    if t >= b13:
        fcen(c, t, b13, "= f{3}{6}", 1180, 640, 100)
        fcen(c, t, c13, "= f{1}{2}", 1400, 640, 100, COR)
        caixa(c, xj + 60, 560, 220, 300, Fr(1, 2) * ep(t, c13, 0.8), ep(t, c13, 0.5), 2)
        E.foco(c, t, c13 + 0.3, 0.4, lambda q: centro(c, "juntas, 1 h", xj + 170, 920, 46, "i", TINTA2, q))
        E.frase(c, t, lerp(c13, d13, 0.4), [("metade", "g", 70, COR)] + ps("por hora", "i", 70), 1280, 800, "center", 0.12)
        bola_res(c, t, d13, "2 h", 1280, 950, 90, 70)


# ---------------- erro de unidade ----------------
def b_erro(c, t, C, b):
    a14 = C["s14.a"]
    a15, b15, c15, d15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    E.frase(c, t, C["s14"] + 0.2, [("cuidado", "g", 100, ERRADO)] + ps("com a unidade", "i", 92), W / 2, 190, "center", 0.12)
    E.foco(c, t, a14, 0.5, lambda a: E.pilula(c, "1,5 m³", 520, 360, 84, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, lerp(a14, C["s15"], 0.6), 0.5, lambda a: E.pilula(c, "12,5 L/min", 1400, 360, 84, "g", fundo=TINTA, a=a))
    if t >= lerp(a14, C["s15"], 0.75):
        E.foco(c, t, lerp(a14, C["s15"], 0.75), 0.5, lambda a: centro(c, "m³  ≠  L", W / 2, 385, 64, "g", ERRADO, a))

    def errado():
        fcen(c, t, a15, "1,5 ÷ 12,5", 700, 620, 100, ERRADO)
        fcen(c, t, b15, "= 0,12 min", 1260, 620, 100, ERRADO)
        E.frase(c, t, lerp(b15, c15, 0.3), ps("nem", "i", 70) + [("10 segundos?!", "g", 70, ERRADO)], W / 2, 760, "center", 0.12)
        tr = lerp(b15, c15, 0.55)
        if t >= tr:
            E.risco(c, 420, 650, 1520, 560, t, tr, largura=14)
    tu = lerp(b15, c15, 0.75)
    E.saida(c, t, tu - 0.1, errado)
    if t < tu:
        return
    E.frase(c, t, tu, ps("tudo na", "i", 72) + [("mesma unidade", "g", 72, COR)], W / 2, 560, "center", 0.12)
    fcen(c, t, c15, "1,5 m³ = 1.500 L", W / 2, 720, 100, COR)
    fcen(c, t, d15, "1.500 ÷ 12,5 = 120 min", W / 2, 900, 100, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a16, b16, c16, d16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]

    def regra():
        E.frase(c, t, C["s16"] + 0.3, ps("o atalho de duas torneiras", "i", 70, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a16, [("produto", "g", 130, BR)] + ps("sobre", "i", 120, CLARO) + [("soma", "g", 130, BR)], W / 2, 340, "center", 0.15)
        fcen(c, t, b16, "3 × 6 = 18", 620, 560, 100, BR)
        fcen(c, t, c16, "3 + 6 = 9", 620, 760, 100, BR)
        E.foco(c, t, d16, 0.5, lambda a: E.formula(c, "f{18}{9} = 2 h", 1380, 700, 150, "g", CLARO, a, "center"))
    E.saida(c, t, C["s17"] - 0.1, regra)

    def porque():
        a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
        E.frase(c, t, a17, ps("é a", "i", 84, CLARO) + [("borboleta", "g", 96, BR)], W / 2, 170, "center", 0.12)
        s, xa, xb, y = 150, 380, 740, 470
        E.foco(c, t, a17 + 0.4, 0.5, lambda a: (E.fracao(c, 1, 3, xa, y, s, BR, a), E.fracao(c, 1, 6, xb, y, s, BR, a),
                                                ))
        for x0, y0, x1, y1, k in ((xa + 60, y - 80, xb - 60, y + 90, b17), (xa + 60, y + 90, xb - 60, y - 80, b17 + 0.4)):
            p = ep(t, k, 0.6)
            if p > 0:
                M.line(c, x0, y0, x1, y1, CLARO, 0.8, 6, progress=p)
        E.foco(c, t, a17 + 0.4, 0.5, lambda a: (c.drawCircle((xa + xb) / 2, y, 52, M.paint("#0A0820", a)),
                                                centro(c, "+", (xa + xb) / 2, y + 38, 100, "g", BR, a)))
        cn = 1260
        E.foco(c, t, b17, 0.5, lambda a: centro(c, "6 + 3", cn, y - 40, 96, "g", BR, a))
        td = lerp(b17, c17, 0.25)
        E.foco(c, t, td, 0.4, lambda a: c.drawRect(skia.Rect.MakeXYWH(cn - 170, y - 3, 340, 7), M.paint(BR, a)))
        E.foco(c, t, td, 0.5, lambda a: centro(c, "3 × 6", cn, y + 106, 96, "g", BR, a))
        E.foco(c, t, td + 0.5, 0.4, lambda a: E.escreve(c, "soma", cn + 200, y - 50, 54, "i", CLARO, a))
        E.foco(c, t, td + 0.5, 0.4, lambda a: E.escreve(c, "produto", cn + 200, y + 95, 54, "i", CLARO, a))
        fcen(c, t, lerp(b17, c17, 0.5), "f{9}{18} da caixa por hora", W / 2, 760, 84, CLARO)
        fcen(c, t, lerp(b17, c17, 0.75), "caixa inteira = f{18}{18}", 620, 950, 70, CLARO)
        fcen(c, t, c17, "18 ÷ 9 = 2 h", 1400, 950, 84, BR)
    if t >= C["s17"]:
        E.saida(c, t, C["s18"] - 0.1, porque)
    if t < C["s18"]:
        return
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    E.foco(c, t, a18, 0.5, lambda a: E.selo(c, 260, 220, 46, False, a))
    E.frase(c, t, a18 + 0.1, [("3 torneiras:", "g", 70, BR)] + ps("some as frações", "i", 70, CLARO), 340, 245, "left", 0.1)
    E.foco(c, t, b18, 0.5, lambda a: E.selo(c, 260, 400, 46, True, a))
    E.frase(c, t, b18 + 0.1, [("vazões dadas:", "g", 70, BR)] + ps("some as vazões", "i", 70, CLARO), 340, 425, "left", 0.1)
    tv = lerp(b18, c18, 0.55)
    E.frase(c, t, tv, ps("não confunda com a", "i", 64, CLARO) + [("ida e volta", "g", 70, BR)], W / 2, 600, "center", 0.1)
    E.foco(c, t, c18, 0.5, lambda a: E.formula(c, "ida e volta:  f{2 × produto}{soma}", 520, 820, 76, "g", CLARO, a, "center"))
    E.foco(c, t, d18, 0.5, lambda a: E.formula(c, "torneiras:  f{produto}{soma}", 1420, 820, 76, "g", BR, a, "center"))
    E.frase(c, t, d18 + 0.3, ps("sem", "i", 70, CLARO) + [("dobro", "g", 74, BR)], 1420, 990, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s19.a"] - 1.2, ps("uma enche em", "i", 84), XE, 380, passo=0.1)
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.escreve(c, "4 h", XE + 560, 385, 110, "g", COR, a))
    E.frase(c, t, C["s19.b"] - 1.0, ps("outra em", "i", 84), XE, 540, passo=0.1)
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.escreve(c, "12 h", XE + 380, 545, 110, "g", TINTA, a))
    E.frase(c, t, C["s19.c"], ps("juntas,", "i", 100) + [("quanto tempo?", "g", 100, COR)], XE, 800, passo=0.12)
    E.relogio(c, t, C["s20.a"], 1540, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_, d, e, f, g = (C[f"s21.{k}"] for k in "abcdefg")

    def frac():
        E.frase(c, t, C["s21"] + 0.2, ps("em", "i", 76) + [("1 hora", "g", 80, COR)], W / 2, 170, "center", 0.12)
        fcen(c, t, a, "f{1}{4} + f{1}{12}", 480, 400, 110)
        fcen(c, t, b_, "= f{3}{12} + f{1}{12}", 1080, 400, 110, TINTA2)
        fcen(c, t, c_, "= f{4}{12}", 620, 640, 110)
        fcen(c, t, d, "= f{1}{3}  por hora", 1080, 640, 110, COR)
        caixa(c, 1520, 520, 200, 300, Fr(1, 3) * ep(t, d, 0.8), ep(t, d, 0.5), 3)
        bola_res(c, t, e, "3 h", W / 2, 880, 110, 84, CERTO)
    E.saida(c, t, f - 0.1, frac)
    if t < f:
        return
    E.frase(c, t, f, ps("pelo", "i", 84) + [("atalho", "g", 88, COR)], W / 2, 220, "center", 0.12)
    E.foco(c, t, f + 0.3, 0.5, lambda q: E.formula(c, "f{4 × 12}{4 + 12} = f{48}{16} = 3 h", W / 2, 500, 120, "g", TINTA, q, "center"))
    fcen(c, t, g, "3 h < 4 h", W / 2 - 60, 820, 110, CERTO)
    E.foco(c, t, g + 0.2, 0.5, lambda q: E.selo(c, W / 2 + 290, 785, 56, True, q))
    E.frase(c, t, g + 0.5, ps("faz sentido", "i", 72, CERTO), W / 2, 970, "center", 0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s22.a", "tempo =", "volume ÷ vazão"), ("s22.b", "vazões juntas", "se somam"), ("s22.c", "juntas <", "a mais rápida sozinha"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 76) + [(l2, "g", 76, COR if i == 0 else TINTA)], 320, y, "left", 0.1)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a0, b0 = C["s23.a"], C["s23.b"]
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, a0, [("gota a gota", "g", 130, COR)], XE, 400)
    E.frase(c, t, lerp(a0, b0, 0.4), ps("quantos litros", "i", 76) + [("em um mês?", "g", 76)], XE, 520, passo=0.1)
    E.frase(c, t, b0, ps("só", "i", 76) + [("encaixando as unidades", "g", 76, COR)], XE, 640, passo=0.1)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 740, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(950, 765, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, vazao=b_vazao, exemplo=b_exemplo, juntas=b_juntas, tempos=b_tempos,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
