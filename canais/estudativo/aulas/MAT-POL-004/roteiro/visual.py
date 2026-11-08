"""Visual — Estudativo · MAT-POL-004: circunferência, raio, diâmetro, pi e comprimento (C = 2πr).
Linguagem da geometria plana (MAT-ANG-001 a 007, MAT-POL-001 a 003): a circunferência em tinta, desenhada com E.circulo;
raio e diâmetro na cor da matéria (o kit já faz assim); o comprimento da volta, quando "desenrola", vira um segmento na cor da
matéria deitado no chão; cada diâmetro copiado sobre ele alterna COR e TINTA2; o que sobra (o 0,14) fica em âmbar.
Medidas na grotesca; resposta na esfera; vermelho é erro, verde é certo; palco escuro só no atalho.
Peças locais: roda() (roda de bicicleta com raios, que gira), rolar() (a roda anda e deixa o rastro do que percorreu),
desenrola() (a volta vira segmento), escada() (a escada do metro, de km a mm), ps(), fcen(), bola_txt().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polígonos e Círculo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POL-004_circunferencia_raio_diametro_comprimento.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("circ", "pi", "roda", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
assert 2 * 6 == 12 and 12 * 3 == 36
assert 2 * 3 * 30 == 180 and 180 * 100 == 18000 and 18000 // 100 == 180
assert 2 * 3 * 60 == 360 and 360 == 2 * 180 and 60 // 2 == 30
assert 2 * 30 == 60 and 60 * 3 == 180
assert 2 * 3 == 6 and 600 // 6 == 100 and 600 // 3 == 200 and 200 // 2 == 100


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     centro(c, s, cx, cy + size * 0.36, size, "g", BR, a)))


def lin(c, t, t0, P, Q, cor=TINTA, larg=6, d=0.5, a=1.0, dash=None):
    if t >= t0 and a > 0:
        M.line(c, *P, *Q, cor, a, larg, dash=dash, progress=ease_io(prog(t, t0, d)))


def roda(c, cx, cy, r, giro=0.0, a=1.0, tinta=TINTA, escuro=False):
    """roda de bicicleta: pneu grosso, 8 raios finos e o cubo; giro em graus (sentido do relógio)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint("#FFFFFF" if not escuro else "#15132E", 0.6 * a))
    for k in range(8):
        g = math.radians(giro + k * 45)
        M.line(c, cx, cy, cx + r * 0.9 * math.cos(g), cy + r * 0.9 * math.sin(g), TINTA2 if not escuro else CLARO, a, 3)
    c.drawCircle(cx, cy, r, M.paint(tinta, a, stroke=max(8, r * 0.09)))
    c.drawCircle(cx, cy, max(8, r * 0.07), M.paint(tinta, a))
    # uma marca no pneu, para ver a roda girar
    g = math.radians(giro + 90)
    c.drawCircle(cx + r * math.cos(g), cy + r * math.sin(g), max(7, r * 0.06), M.paint(E.COR if not escuro else CLARO, a))


def rolar(c, t, t0, d, x0, chao, r, dist, a=1.0, rastro=E.COR, voltas=None):
    """a roda anda dist px em d segundos, girando sem escorregar, e deixa no chão o rastro do que percorreu"""
    if t < t0 or a <= 0:
        return x0
    q = ease_io(prog(t, t0, d))
    x = x0 + dist * q
    M.line(c, x0 - 40, chao, x0 + dist + r + 60, chao, TINTA, a, 4)
    if q > 0:
        M.line(c, x0, chao, x, chao, rastro, a, 12)
    roda(c, x, chao - r, r, math.degrees((x - x0) / r), a)
    return x


def desenrola(c, t, t0, d, cx, cy, r, x0, y0, cor=None, a=1.0):
    """a volta da circunferência desenrola e vira o segmento de x0 até x0 + 2πr, na altura y0"""
    if a <= 0:
        return
    cor = cor or E.COR
    q = ease_io(prog(t, t0, d)) if t >= t0 else 0.0
    L = 2 * math.pi * r
    ret = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
    if q < 1:
        c.drawArc(ret, 90 + 360 * q, 360 * (1 - q), False, M.paint(cor, a, stroke=10, cap_round=True))
    if q > 0:
        M.line(c, x0, y0, x0 + L * q, y0, cor, a, 10)


def escada(c, t, t0, x, y, passo_x, passo_y, a=1.0, acende=(), tq=None):
    """a escada do metro: km no alto à esquerda, mm embaixo à direita"""
    nomes = ("km", "hm", "dam", "m", "dm", "cm", "mm")
    pos = []
    for i, s in enumerate(nomes):
        px, py = x + i * passo_x, y + i * passo_y
        pos.append((px, py))
        ti = t0 + 0.06 * i
        if t >= ti:
            q = ep(t, ti, 0.4) * a
            cor = E.COR if s in acende else TINTA
            M.line(c, px, py, px + passo_x, py, cor, q, 6)
            if i < len(nomes) - 1:
                M.line(c, px + passo_x, py, px + passo_x, py + passo_y, TINTA, q, 6)
            centro(c, s, px + passo_x / 2, py - 18, 48, "g", cor, q)
    return pos


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        r = 130
        x = rolar(c, t, ka, kb - ka + 0.6, 240, 760, r, 1250)
        E.frase(c, t, ka + 0.3, [("100", "g", 100, COR)] + ps("voltas", "i", 90), W / 2, 200, "center", 0.12)
        E.frase(c, t, ka + 1.6, ps("quanto a bicicleta", "i", 70) + [("andou?", "g", 76, COR)], W / 2, 320, "center", 0.12)
        if t >= kb:
            # o tamanho da roda: o raio
            cx, cy = 240 + 1250, 760 - r
            lin(c, t, kb + 0.6, (cx, cy), (cx, cy - r), E.COR, 8, 0.4)
            E.foco(c, t, kb + 0.9, 0.4, lambda a: E.escreve(c, "raio", cx - 150, cy - r / 2 + 20, 54, "g", COR, a))
            E.frase(c, t, kb, ps("só com o", "i", 60) + [("tamanho da roda", "g", 64)], W / 2, 920, "center", 0.12)
        E.foco(c, t, kc, 0.6, lambda a: E.bola(c, 640, 560, 150 * ease_back(prog(t, kc, 0.6)), a=a))
        E.foco(c, t, kc + 0.2, 0.5, lambda a: centro(c, "π", 640, 610, 180, "g", BR, a))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1520, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("a volta", "g", 110, COR)], XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), ps("de qualquer", "i", 84), XE, 580, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.65), [("circunferência", "g", 96, COR)], XE, 700, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1520, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1520, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "razão: comparar", "pela divisão"), ("s03.c", "isolar uma letra:", "o mesmo nos dois lados"), ("s03.d", "escada", "do metro"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.4, [(l2, "g", 58, COR)], x + 44, y + 160)
    alvo = [(x + w - 30, 170 + i * 240 + 170) for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, alvo[0][0], lerp(lerp(alvo[0][1], alvo[1][1], q1), alvo[2][1], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 960, "left", 0.12)


# ---------------- circunferência ----------------
def b_circ(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    O, r = (620, 560), 300
    X = 1450

    def quatro():
        # o barbante preso no centro e o lápis que gira
        g = 360 * ease_io(prog(t, b4, max(1.2, c4 - b4))) if t >= b4 else 0.0
        if t >= a4:
            k = ease_back(prog(t, a4, 0.4))
            c.drawCircle(*O, 14 * k, M.paint(TINTA))
            P = (O[0] + r * math.cos(math.radians(-g)), O[1] + r * math.sin(math.radians(-g)))
            M.line(c, *O, *P, AMBAR, ep(t, a4 + 0.3, 0.4) * (1 - ep(t, d4, 0.4)), 4)
            ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
            if g > 0:
                c.drawArc(ret, 0, -g, False, M.paint(TINTA, 1.0, stroke=7, cap_round=True))
            # lápis
            al = ep(t, a4 + 0.3, 0.4) * (1 - ep(t, c4 + 0.6, 0.4))
            if al > 0:
                ux, uy = math.cos(math.radians(-g)), math.sin(math.radians(-g))
                nx, ny = -uy, ux
                M.line(c, P[0], P[1], P[0] + nx * 70 + ux * 20, P[1] + ny * 70 + uy * 20, AMBAR, al, 16)
                c.drawCircle(*P, 8, M.paint(TINTA, al))
        if t >= d4:
            for j, gg in enumerate((20, 100, 200, 290)):
                Q = (O[0] + r * math.cos(math.radians(gg)), O[1] + r * math.sin(math.radians(gg)))
                lin(c, t, d4 + 0.15 * j, O, Q, E.COR, 5, 0.4, dash=E.TRACO)
            E.foco(c, t, d4 + 0.4, 0.4, lambda a: E.escreve(c, "centro", O[0] - 80, O[1] + 70, 50, "g", TINTA, a))
        E.frase(c, t, a4, ps("barbante + lápis", "i", 66), X, 280, "center", 0.12)
        E.frase(c, t, b4, [("gire", "g", 90, COR)], X, 420, "center")
        E.frase(c, t, c4, [("circunferência", "g", 80, COR)], X, 580, "center")
        E.frase(c, t, d4, ps("todos à", "i", 60) + [("mesma distância", "g", 62, COR)], X, 740, "center", 0.12)
        E.frase(c, t, d4 + 0.8, ps("do centro", "i", 60), X, 830, "center", 0.12)
    E.saida(c, t, C["s05"] - 0.1, quatro)

    if t >= C["s05"]:
        E.circulo(c, t, C["s05"], 560, 560, 280, o=None, d=0.5, cor=E.COR, preenche=0.22 if t >= b5 else 0.0)
        if a5 <= t < b5 + 0.5:
            c.drawCircle(560, 560, 280, M.paint(E.COR, ep(t, a5, 0.4) * (1 - ep(t, b5, 0.4)), stroke=16))
        if t >= b5:
            c.drawCircle(560, 560, 280, M.paint(E.COR, 0.3 * ep(t, b5, 0.5)))
        E.frase(c, t, a5, [("circunferência", "g", 70, COR)] + ps("= a linha", "i", 64), X, 300, "center", 0.12)
        E.frase(c, t, b5, [("círculo", "g", 70, COR)] + ps("= a região", "i", 64), X, 430, "center", 0.12)
        # pneu e roda
        E.foco(c, t, c5, 0.5, lambda a: (c.drawCircle(1260, 720, 110, M.paint(TINTA, a, stroke=26)),
                                         centro(c, "pneu", 1260, 900, 52, "i", TINTA, a)))
        E.foco(c, t, c5 + 0.5, 0.5, lambda a: (c.drawCircle(1640, 720, 120, M.paint(E.COR, 0.3 * a)), roda(c, 1640, 720, 120, 0, a),
                                               centro(c, "roda inteira", 1640, 900, 52, "i", TINTA, a)))


# ---------------- raio e diâmetro ----------------
def b_raio(c, t, C, b):
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    O, r = (600, 560), 320
    X = 1450
    E.circulo(c, t, C["s06"], *O, r, o="O", d=0.5, raio=(50, "r") if t < b6 else None, te={"raio": a6})
    if t >= b6:
        E.circulo(c, t, C["s06"], *O, r, o="O", d=0.5, diametro=(0, "d"), te={"diametro": b6})
    if t >= c6:
        # um raio para cada lado
        for j, (P, Q) in enumerate((((O[0] - r, O[1]), O), (O, (O[0] + r, O[1])))):
            q = ep(t, c6 + 0.3 * j, 0.4)
            M.line(c, P[0], P[1] + 90, Q[0], Q[1] + 90, (E.COR, TINTA2)[j], q, 5)
            for X0 in (P[0], Q[0]):
                M.line(c, X0, P[1] + 76, X0, P[1] + 104, (E.COR, TINTA2)[j], q, 5)
            E.foco(c, t, c6 + 0.3 * j, 0.4, lambda a, P=P, Q=Q, j=j: centro(c, "r", (P[0] + Q[0]) / 2, P[1] + 170, 60, "g", (COR, TINTA2)[j], a))
    E.frase(c, t, a6, [("raio:", "g", 72, COR)] + ps("do centro até a borda", "i", 54), X, 280, "center", 0.12)
    E.frase(c, t, a6 + 1.0, ps("(o barbante)", "i", 50, TINTA2), X, 360, "center", 0.12)
    E.frase(c, t, b6, [("diâmetro:", "g", 72, COR)] + ps("atravessa", "i", 54), X, 500, "center", 0.12)
    E.frase(c, t, b6 + 1.0, ps("passando pelo centro", "i", 50, TINTA2), X, 580, "center", 0.12)
    E.frase(c, t, c6, ps("um raio para cada lado", "i", 54), X, 720, "center", 0.12)
    fcen(c, t, d6, "d = 2r", X, 880, 120, COR)


# ---------------- pi ----------------
def b_pi(c, t, C, b):
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    O, r = (560, 400), 150
    x0, y0 = 300, 820
    L = 2 * math.pi * r

    def sete():
        E.frase(c, t, C["s07"] + 0.2, ps("o comprimento:", "i", 70) + [("a volta inteira", "g", 72, COR)], W / 2, 150, "center", 0.12)
        E.circulo(c, t, C["s07"] + 0.3, *O, r, o=None, d=0.5)
        if a7 <= t < b7:
            q = ease_io(prog(t, a7, 1.0))
            ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
            c.drawArc(ret, 90, 360 * q, False, M.paint(E.COR, 1.0, stroke=12, cap_round=True))
        if t >= b7:
            E.foco(c, t, b7, 0.4, lambda a: E.escreve(c, "lata (vista de cima)", O[0] + r + 40, O[1] + 10, 44, "i", TINTA2, a))
            desenrola(c, t, b7 + 0.3, 1.4, *O, r, x0, y0)
            E.foco(c, t, b7 + 1.8, 0.4, lambda a: E.escreve(c, "volta", x0 + L + 30, y0 + 16, 54, "g", COR, a))
        if t >= c7:
            # o diâmetro, e quantas vezes ele cabe na volta
            lin(c, t, c7, (O[0] - r, O[1]), (O[0] + r, O[1]), TINTA, 7, 0.4)
            E.foco(c, t, c7 + 0.3, 0.4, lambda a: centro(c, "diâmetro", O[0], O[1] - 24, 46, "g", TINTA, a))
            for k in range(3):
                tk = c7 + 0.8 + 0.6 * k
                q = ease_io(prog(t, tk, 0.4))
                if q > 0:
                    xa = x0 + 2 * r * k
                    cor = (TINTA, TINTA2, TINTA)[k]
                    M.line(c, lerp(O[0] - r, xa, q), lerp(O[1], y0 - 46, q), lerp(O[0] + r, xa + 2 * r, q), lerp(O[1], y0 - 46, q), cor, 1.0, 9)
                    E.foco(c, t, tk + 0.4, 0.3, lambda a, xa=xa, k=k: centro(c, str(k + 1), xa + r, y0 - 70, 50, "g", TINTA, a))
        if t >= d7:
            x3 = x0 + 6 * r
            M.line(c, x3, y0 - 46, x0 + L, y0 - 46, AMBAR, ep(t, d7, 0.4), 9)
            E.frase(c, t, d7, ps("cabe", "i", 60) + [("pouco mais que 3", "g", 64, COR)] + ps("vezes", "i", 60), W / 2, 980, "center", 0.12)
    E.saida(c, t, C["s08"] - 0.1, sete)

    if t >= C["s08"]:
        for k, (cx, rr, nome) in enumerate(((300, 70, "lata"), (580, 110, "prato"), (930, 170, "roda gigante"))):
            tk = C["s08"] + 0.3 * k
            E.circulo(c, t, tk, cx, 420, rr, o=None, d=0.5)
            lin(c, t, tk + 0.4, (cx - rr, 420), (cx + rr, 420), TINTA2, 5, 0.3)
            E.foco(c, t, tk + 0.4, 0.4, lambda a, cx=cx, nome=nome: centro(c, nome, cx, 660, 44, "i", TINTA2, a))
        E.formula_em(c, t, a8, "f{volta}{diâmetro} = sempre igual", 640, 840, 64, "g", None, "center")
        E.foco(c, t, b8, 0.6, lambda a: E.bola(c, 1500, 420, 190 * ease_back(prog(t, b8, 0.6)), a=a))
        E.foco(c, t, b8 + 0.2, 0.5, lambda a: centro(c, "π", 1500, 490, 220, "g", BR, a))
        E.frase(c, t, b8 + 0.6, ps("pi, letra grega", "i", 52, TINTA2), 1500, 690, "center", 0.1)
        fcen(c, t, c8, "π = 3,14159...", 1500, 800, 70, COR)
        E.foco(c, t, d8, 0.4, lambda a: E.pilula(c, "π = 3", 1360, 940, 52, "g", a=a, cor=E.SOBRE))
        E.foco(c, t, d8 + 0.4, 0.4, lambda a: E.pilula(c, "π = 3,14", 1640, 940, 52, "g", fundo=TINTA, a=a))


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    a9, b9, c9, d9, e9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]

    def nove():
        E.formula_em(c, t, C["s09"] + 0.3, "f{C}{d} = π", W / 2, 260, 90, "g", TINTA2, "center")
        fcen(c, t, a9, "C = π × d", W / 2, 440, 100)
        fcen(c, t, b9, "C = 2πr", W / 2, 680, 170, COR)
        xs = W / 2 - E.formula(None, "C = 2πr", 0, 0, 170, "g", a=0) / 2
        wC = E.formula(None, "C", 0, 0, 170, "g", a=0)
        w_ate2 = E.formula(None, "C = ", 0, 0, 170, "g", a=0)
        w2 = E.formula(None, "2", 0, 0, 170, "g", a=0)
        w_ate_r = E.formula(None, "C = 2π", 0, 0, 170, "g", a=0)
        wr = E.formula(None, "r", 0, 0, 170, "g", a=0)
        for k, (tt, xc, s) in enumerate(((c9, xs + wC / 2, "comprimento"), (d9, xs + w_ate_r + wr / 2, "raio"), (e9, xs + w_ate2 + w2 / 2, "do diâmetro"))):
            yy = (860, 860, 990)[k]
            E.foco(c, t, tt, 0.4, lambda a, xc=xc, s=s, yy=yy: (M.line(c, xc, 715, xc, yy - 60, E.COR, a, 4),
                                                                 E.pilula(c, s, xc, yy - 20, 42, "g", a=a, cor=E.SOBRE)))
    E.saida(c, t, C["s10"] - 0.1, nove)
    if t < C["s10"]:
        return
    E.circulo(c, t, C["s10"], 520, 560, 280, o=None, d=0.5, raio=(40, "6"), te={"raio": a10})
    X = 1360
    fcen(c, t, C["s10"] + 0.2, "C = 2πr", X, 230, 80, TINTA2)
    fcen(c, t, b10, "C = 2 × π × 6 = 12π", X, 420, 80, COR)
    E.foco(c, t, c10, 0.4, lambda a: E.pilula(c, "o π fica na resposta", X, 560, 48, "g", fundo=TINTA, a=a))
    E.frase(c, t, d10 - 0.3, ps("com", "i", 60, TINTA2) + [("π = 3:", "g", 58, TINTA2)], X, 720, "center", 0.12)
    fcen(c, t, d10, "12 × 3 = 36", X, 860, 96)


# ---------------- a roda ----------------
def b_roda(c, t, C, b):
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    r = 120

    def onze():
        x0 = 300
        dist = 2 * math.pi * r
        if t < c11:
            roda(c, x0, 800 - r, r, 0, ep(t, C["s11"], 0.4))
            M.line(c, x0 - 160, 800, x0 + dist + r + 60, 800, TINTA, ep(t, C["s11"], 0.4), 4)
            lin(c, t, a11, (x0, 800 - r), (x0, 800 - 2 * r), E.COR, 8, 0.4)
            E.foco(c, t, a11 + 0.3, 0.4, lambda a: E.escreve(c, "30 cm", x0 + r + 24, 800 - 1.5 * r + 18, 52, "g", COR, a))
        else:
            rolar(c, t, c11, 2.4, x0, 800, r, dist)
            E.foco(c, t, c11 + 2.4, 0.4, lambda a: centro(c, "180 cm = 1 volta", x0 + dist / 2, 880, 56, "g", COR, a))
        E.frase(c, t, a11, ps("raio", "i", 64) + [("30 cm,", "g", 68, COR), ("π = 3", "g", 68)], 1350, 200, "center", 0.12)
        fcen(c, t, b11, "2 × 3 × 30 = 180 cm", 1350, 360, 76, COR)
        E.frase(c, t, c11, ps("a borda inteira encosta", "i", 52, TINTA2), 1350, 470, "center", 0.1)
        E.frase(c, t, c11 + 0.8, ps("no chão uma vez", "i", 52, TINTA2), 1350, 540, "center", 0.1)
    E.saida(c, t, C["s12"] - 0.1, onze)

    if t >= C["s12"]:
        X = 560
        E.frase(c, t, C["s12"] + 0.2, ps("em", "i", 70) + [("100 voltas", "g", 76, COR)], X, 220, "center", 0.12)
        fcen(c, t, a12, "180 × 100 = 18000 cm", X, 380, 70)
        pos = escada(c, t, b12 - 0.8, 1020, 300, 120, 80, acende=("m", "cm") if t >= b12 else ())
        if t >= b12:
            # de cm para m: dois degraus para cima
            for k, (i0, i1) in enumerate(((5, 4), (4, 3))):
                q = ep(t, b12 + 0.4 * k, 0.4)
                p0 = (pos[i0][0] + 60, pos[i0][1] + 40)
                p1 = (pos[i1][0] + 60, pos[i1][1] + 40)
                M.arrow(c, p0[0], p0[1], p1[0] + 20, p1[1] + 10, E.COR, q, 5, 16, q)
            E.foco(c, t, b12 + 0.8, 0.4, lambda a: E.pilula(c, "÷ 100", 1500, 860, 54, "g", a=a, cor=E.SOBRE))
            E.frase(c, t, b12, ps("de cm para m:", "i", 60) + [("2 degraus", "g", 64, COR)], X, 540, "center", 0.12)
        fcen(c, t, c12, "18000 ÷ 100 = 180", X, 700, 76)
        bola_txt(c, t, c12 + 0.8, "180 m", X, 860, 110, 62)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a13, b13, c13, d13, e13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
    X = 1350
    O, r = (520, 600), 260
    E.frase(c, t, C["s13"], [("cuidado", "g", 92, ERRADO)] + ps("com este erro", "i", 86), W / 2, 150, "center", 0.14)
    E.frase(c, t, a13, ps("usar o", "i", 60) + [("diâmetro", "g", 64, ERRADO)] + ps("no lugar do", "i", 60) + [("raio", "g", 64, COR)],
            W / 2, 260, "center", 0.12)
    if t >= b13:
        roda(c, *O, r, 0, ep(t, b13, 0.4))
        lin(c, t, b13 + 0.3, (O[0] - r, O[1]), (O[0] + r, O[1]), ERRADO if t < e13 else TINTA2, 8, 0.5)
        E.foco(c, t, b13 + 0.6, 0.4, lambda a: centro(c, "60 cm", O[0] - r / 2 - 10, O[1] - 24, 50, "g", ERRADO if t < e13 else TINTA2, a))
    if t >= e13:
        lin(c, t, e13, O, (O[0] + r, O[1]), CERTO, 10, 0.4)
        E.foco(c, t, e13 + 0.3, 0.4, lambda a: centro(c, "30", O[0] + r / 2, O[1] + 60, 54, "g", CERTO, a))
    fcen(c, t, c13, "2 × 3 × 60 = 360 cm", X, 430, 70, ERRADO)
    if t >= d13:
        E.risco(c, X - 330, 450, X + 330, 390, t, d13, largura=10)
    E.frase(c, t, d13, ps("o", "i", 60, ERRADO) + [("dobro", "g", 64, ERRADO)] + ps("do certo", "i", 60, ERRADO), X, 540, "center", 0.12)
    fcen(c, t, e13, "r = 60 ÷ 2 = 30", X, 700, 70)
    fcen(c, t, e13 + 1.2, "2 × 3 × 30 = 180 cm", X, 840, 70, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]

    def um():
        E.frase(c, t, C["s14"] + 0.2, ps("com", "i", 80, CLARO) + [("π = 3", "g", 90, BR)], W / 2, 200, "center", 0.12)
        E.frase(c, t, a14, [("volta =", "g", 96, BR), ("3 × diâmetro", "g", 96, CLARO)], W / 2, 360, "center", 0.14)
        # o diâmetro, três vezes, ao lado da roda
        O, r = (420, 690), 120
        roda(c, *O, r, 0, ep(t, a14, 0.4), BR, escuro=True)
        if t >= a14 + 0.4:
            lin(c, t, a14 + 0.4, (O[0] - r, O[1]), (O[0] + r, O[1]), CLARO, 8, 0.4)
            for k in range(3):
                q = ease_io(prog(t, a14 + 1.0 + 0.4 * k, 0.4))
                xa = 640 + 2 * r * k
                if q > 0:
                    M.line(c, xa, 900, xa + 2 * r * q, 900, (CLARO, BR, CLARO)[k], 1.0, 10)
            E.foco(c, t, a14 + 2.4, 0.4, lambda a: E.escreve(c, "a volta", 640 + 6 * r + 30, 916, 56, "g", CLARO, a))
        fcen(c, t, b14, "d = 2 × 30 = 60", 1460, 620, 76, BR)
        fcen(c, t, c14, "60 × 3 = 180", 1460, 760, 90, CLARO)
    E.saida(c, t, C["s15"] - 0.1, um)
    if t >= C["s15"]:
        E.formula_em(c, t, a15, "2πr = π × d", W / 2, 320, 130, "g", BR, "center")
        E.frase(c, t, b15, ps("com", "i", 66, CLARO) + [("π = 3,14", "g", 72, BR)] + ps(":", "i", 66, CLARO) + [("não compensa", "g", 72, ERRADO)],
                W / 2, 560, "center", 0.12)
        E.foco(c, t, c15, 0.5, lambda a: E.pilula(c, "o triplo só serve para conferir", W / 2, 760, 56, "g", fundo=E.mix(E.COR, BR, 0.25), a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a16, b16 = C["s16.a"], C["s16.b"]
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    O, r = (560, 600), 270
    if t >= C["s16"] + 0.6:
        c.drawCircle(*O, r, M.paint(AMBAR, 0.35 * ep(t, C["s16"] + 0.6, 0.5), stroke=60))
        E.circulo(c, t, C["s16"] + 0.6, *O, r, o=None, d=0.6)
    E.foco(c, t, a16, 0.4, lambda a: centro(c, "600 m", O[0], O[1] - 40, 90, "g", COR, a))
    E.foco(c, t, a16 + 0.3, 0.4, lambda a: centro(c, "de volta", O[0], O[1] + 90, 56, "i", TINTA2, a))
    E.frase(c, t, b16, ps("com", "i", 60) + [("π = 3,", "g", 64)], 1000, 330, "left", 0.12)
    E.frase(c, t, b16 + 0.8, ps("quanto mede o", "i", 60) + [("raio?", "g", 66, COR)], 1000, 440, "left", 0.12)
    E.relogio(c, t, C["s17.a"], 1490, 720, 150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    X = 640
    O, r = (1450, 560), 250
    E.circulo(c, t, C["s18"], *O, r, o=None, d=0.6)
    E.foco(c, t, C["s18"] + 0.4, 0.4, lambda a: centro(c, "C = 600", O[0], O[1] - r - 40, 56, "g", COR, a))
    if t >= d18:
        lin(c, t, d18, O, (O[0] + r * math.cos(math.radians(-40)), O[1] + r * math.sin(math.radians(-40))), E.COR, 8, 0.4)
        E.foco(c, t, d18 + 0.4, 0.4, lambda a: centro(c, "r = 100", O[0] + 60, O[1] + 70, 54, "g", COR, a))
    if t >= b19:
        lin(c, t, b19, (O[0] - r, O[1] + 140), (O[0] + r, O[1] + 140), TINTA2, 5, 0.5, dash=E.TRACO)
        E.foco(c, t, b19 + 0.4, 0.4, lambda a: centro(c, "d = 200", O[0], O[1] + 200, 50, "g", TINTA2, a))

    def dezoito():
        E.frase(c, t, C["s18"] + 0.2, ps("a volta é dada;", "i", 60) + [("falta o raio", "g", 64, COR)], X, 220, "center", 0.12)
        fcen(c, t, a18, "600 = 2 × 3 × r", X, 400, 84)
        fcen(c, t, b18, "600 = 6r", X, 560, 84)
        E.foco(c, t, c18, 0.4, lambda a: E.pilula(c, "÷ 6 nos dois lados", X, 680, 46, "g", a=a, cor=E.SOBRE))
        bola_txt(c, t, d18, "r = 100 m", X, 850, 120, 56)
    E.saida(c, t, C["s19"] - 0.1, dezoito)
    if t >= C["s19"]:
        E.frase(c, t, C["s19"] + 0.2, ps("pelo", "i", 66) + [("atalho", "g", 70, COR)], X, 220, "center", 0.12)
        fcen(c, t, a19, "volta = 3 × d", X, 380, 80)
        fcen(c, t, b19, "d = 600 ÷ 3 = 200", X, 540, 80)
        fcen(c, t, c19, "r = 200 ÷ 2 = 100 m", X, 700, 80, CERTO)
        E.foco(c, t, c19 + 1.2, 0.5, lambda a: E.selo(c, X, 860, 60 * ease_back(prog(t, c19 + 1.2, 0.5)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", "d = 2r"), ("s20.b", "volta = π × d"), ("s20.c", "C = 2πr"))
        for i, (k, s) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 560, y - 30, 56, a=a), centro(c, str(i + 1), 560, y - 7, 64, "g", BR, a)))
            E.formula_em(c, t, C[k] + 0.1, s, 670, y, 100, "g", COR)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s21.a"], [("Arco de", "g", 130, COR)], XE, 440)
    E.frase(c, t, C["s21.a"] + 0.3, [("circunferência", "g", 130, COR)], XE, 570)
    E.frase(c, t, C["s21.b"], ps("com a regra de três", "i", 70), XE, 700, passo=0.12)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, circ=b_circ, raio=b_raio, pi=b_pi, formula=b_formula, roda=b_roda,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
