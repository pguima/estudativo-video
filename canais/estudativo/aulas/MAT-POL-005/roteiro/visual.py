"""Visual — Estudativo · MAT-POL-005: comprimento de um arco (regra de três e fração da volta).
Linguagem da geometria plana (MAT-ANG-001 a 007, MAT-POL-001 a 004): a circunferência em tinta (E.circulo); o ARCO da vez é um
traço grosso na cor da matéria por cima da borda; o ângulo central é a cunha clara na cor da matéria, com os dois raios em tinta;
os pedaços seguintes alternam COR e TINTA2; a pizza tem a massa em âmbar claro. Regra de três: a tabela de duas colunas
(ângulo | arco) e a cruz, com a primeira diagonal em COR e a segunda em TINTA2. Medidas na grotesca; resposta na esfera;
vermelho é erro, verde é certo; palco escuro só no atalho.
Peças locais: arco_cor() (arco grosso de g1 a g2, graus da matemática), cunha() (ângulo central), pizza() (disco com fatias),
tabela() (regra de três com a cruz), relogio_min() (relógio com o ponteiro dos minutos), mini() (círculo com a fração pintada).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polígonos e Círculo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POL-005_comprimento_de_arco.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("arco", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
MASSA = "#F3D9A4"
assert 360 // 6 == 60 and 2 * 6 == 12 and 60 * 12 == 720 and 720 // 360 == 2 and 2 * 3 == 6
assert abs(2 * 3.14 - 6.28) < 1e-9 and 360 * 1 == 6 * 60
assert 360 // 90 == 4 and 360 // 180 == 2 and 360 // 120 == 3 and 360 // 45 == 8 and 50 * 36 == 5 * 360
assert 2 * 3 * 10 == 60 and 60 // 3 == 20 and 360 // 3 == 120 and 120 * 60 == 7200 and 7200 // 360 == 20


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


def pt(O, r, g):
    return O[0] + r * math.cos(math.radians(g)), O[1] - r * math.sin(math.radians(g))


def arco_cor(c, O, r, g1, g2, cor=None, larg=16, a=1.0, p=1.0):
    """arco grosso de g1 até g2 (graus da matemática, anti-horário), crescendo com p"""
    if a <= 0 or p <= 0:
        return
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    c.drawArc(ret, -g1, -(g2 - g1) * p, False, M.paint(cor or E.COR, a, stroke=larg, cap_round=True))


def cunha(c, O, g1, g2, r, cor=None, a=1.0, alfa=0.25, borda=5):
    if a <= 0:
        return
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    path = skia.Path(); path.moveTo(*O); path.arcTo(ret, -g1, -(g2 - g1), False); path.close()
    c.drawPath(path, M.paint(cor or E.COR, alfa * a))
    if borda:
        c.drawArc(ret, -g1, -(g2 - g1), False, M.paint(cor or E.COR, a, stroke=borda, cap_round=True))


def raios(c, O, r, gs, a=1.0, cor=TINTA, larg=5):
    for g in gs:
        M.line(c, *O, *pt(O, r, g), cor, a, larg)


def pizza(c, O, r, a=1.0, cortes=0.0, n=6, g0=0):
    """pizza vista de cima: massa, borda e os n cortes (cortes = 0..1 faz os cortes crescerem)"""
    if a <= 0:
        return
    c.drawCircle(*O, r, M.paint(MASSA, a))
    for k, (dx, dy) in enumerate(((0.35, 0.2), (-0.4, 0.3), (0.1, -0.45), (-0.2, -0.1), (0.5, -0.3), (-0.1, 0.55))):
        c.drawCircle(O[0] + dx * r, O[1] + dy * r, r * 0.09, M.paint("#C8553D", 0.75 * a))
    c.drawCircle(*O, r, M.paint(AMBAR, a, stroke=max(8, r * 0.06)))
    if cortes > 0:
        for k in range(n):
            M.line(c, *O, *pt(O, r, g0 + 360 * k / n), TINTA, a, 4, progress=cortes)


def tabela(c, t, linhas, tl, x, y, dy=130, size=84, cor_l=None, cruz=None, wcol=300, a=1.0):
    """regra de três: linhas = [(esq, dir[, cor da direita])]; tl = instante de cada linha; cruz = instante das diagonais"""
    if a <= 0:
        return
    t0 = tl[0]
    if t >= t0:
        M.line(c, x, y - size * 0.95, x, y + dy * (len(linhas) - 1) + size * 0.45, TINTA2, ep(t, t0, 0.4) * a, 4)
    for i, ln in enumerate(linhas):
        esq, dir_ = ln[0], ln[1]
        cd = ln[2] if len(ln) > 2 else None
        yy = y + dy * i
        E.foco(c, t, tl[i], 0.4, lambda f, esq=esq, yy=yy: E.formula(c, esq, x - wcol / 2, yy, size, "g", cor_l, f * a, "center"))
        E.foco(c, t, tl[i] + 0.25, 0.4, lambda f, dir_=dir_, yy=yy, cd=cd: E.formula(c, dir_, x + wcol / 2, yy, size, "g", cd, f * a, "center"))
    if cruz is not None and t >= cruz and len(linhas) >= 2:
        y1, y2 = y - size * 0.35, y + dy - size * 0.35
        x1, x2 = x - wcol / 2, x + wcol / 2
        for k, (P, Q, cor) in enumerate((((x1 + 40, y1 + 30), (x2 - 40, y2 - 40), E.COR), ((x2 - 40, y1 + 30), (x1 + 40, y2 - 40), TINTA2))):
            q = ease_io(prog(t, cruz + 0.4 * k, 0.5))
            if q > 0:
                M.line(c, *P, *Q, cor, a, 7, progress=q)


def relogio_min(c, O, r, a=1.0, ponteiro=90.0, tinta=TINTA):
    """relógio com os 12 tracinhos e o ponteiro dos minutos apontando para o ângulo `ponteiro` (graus da matemática)"""
    if a <= 0:
        return
    c.drawCircle(*O, r, M.paint("#FFFFFF", 0.7 * a))
    c.drawCircle(*O, r, M.paint(tinta, a, stroke=7))
    for k in range(12):
        g = 90 - 30 * k
        forte = k % 3 == 0
        M.line(c, *pt(O, r * (0.84 if forte else 0.9), g), *pt(O, r * 0.96, g), tinta, a, 6 if forte else 3)
    for k, s in ((0, "12"), (3, "3"), (6, "6"), (9, "9")):
        P = pt(O, r * 0.68, 90 - 30 * k)
        centro(c, s, P[0], P[1] + 18, 50, "g", tinta, a)
    M.line(c, *O, *pt(O, r * 0.8, ponteiro), E.COR, a, 10)
    c.drawCircle(*O, 12, M.paint(tinta, a))


def mini(c, O, r, frac, cor, tinta, a=1.0):
    """círculo pequeno com a fração da volta pintada a partir do alto, no sentido do relógio"""
    if a <= 0:
        return
    cunha(c, O, 90 - 360 * frac, 90, r, cor, a, 0.55, 0)
    c.drawCircle(*O, r, M.paint(tinta, a, stroke=5))
    arco_cor(c, O, r, 90 - 360 * frac, 90, cor, 12, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    O, r = (600, 580), 330
    X = 1450

    def um():
        pizza(c, O, r, ep(t, ka, 0.5), ease_io(prog(t, kb, 1.0)), 6, 0)
        if t >= ka + 0.6:
            E.foco(c, t, ka + 0.6, 0.4, lambda a: (M.line(c, *O, *pt(O, r, 210), E.COR, a, 8),
                                                   centro(c, "6 cm", *(lambda P: (P[0] - 10, P[1] - 30))(pt(O, r * 0.5, 210)), 54, "g", COR, a)))
        if t >= kc:
            arco_cor(c, O, r, 0, 60, E.COR, 22, 1.0, ease_io(prog(t, kc, 0.6)))
            E.foco(c, t, kc + 0.5, 0.4, lambda a: centro(c, "?", *(lambda P: (P[0] + 20, P[1] + 20))(pt(O, r + 60, 30)), 110, "g", COR, a))
        E.frase(c, t, ka, ps("raio", "i", 72) + [("6 cm", "g", 80, COR)], X, 260, "center", 0.12)
        E.frase(c, t, kb, [("6", "g", 80, COR)] + ps("fatias iguais", "i", 72), X, 390, "center", 0.12)
        E.frase(c, t, kc, ps("a", "i", 72) + [("borda", "g", 80, COR)] + ps("de uma fatia?", "i", 72), X, 560, "center", 0.12)
        E.foco(c, t, kd, 0.5, lambda a: E.pilula(c, "uma regra de três", X, 780, 60, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1520, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("qualquer", "g", 110, COR)], XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), [("pedaço", "g", 110, COR)], XE, 590, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.65), ps("de circunferência", "i", 84), XE, 710, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1520, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1520, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "uma volta inteira:", "360°"), ("s03.c", "a volta da circunferência:", "C = 2πr"), ("s03.d", "regra de três direta:", "tabela e cruz"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 84)
        E.formula_em(c, t, C[k] + 0.4, l2, x + 44, y + 165, 62, "g", COR)
    alvo = [(x + w - 30, 170 + i * 240 + 170) for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, alvo[0][0], lerp(lerp(alvo[0][1], alvo[1][1], q1), alvo[2][1], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 960, "left", 0.12)


# ---------------- arco e ângulo central ----------------
def b_arco(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    O, r = (600, 570), 320
    X = 1450
    # pizza clara por baixo, a partir da fala da fatia
    if t >= b4:
        pizza(c, O, r, 0.55 * ep(t, b4, 0.5), ease_io(prog(t, c5, 1.0)) if t >= c5 else 0.0)
    E.circulo(c, t, C["s04"], *O, r, o=None, d=0.6)
    # quantas fatias estão acesas
    n = 1
    if t >= a6:
        n = 2
    if t >= lerp(b6, c6, 0.35):
        n = 3
    if t >= lerp(b6, c6, 0.7):
        n = 6
    if t >= a4:
        for k in range(n):
            tk = a4 if k == 0 else (a6 if k == 1 else (lerp(b6, c6, 0.35) if k == 2 else lerp(b6, c6, 0.7) + 0.15 * (k - 3)))
            arco_cor(c, O, r, 60 * k, 60 * (k + 1), E.COR if k % 2 == 0 else TINTA2, 18, 1.0, ease_io(prog(t, tk, 0.5)))
        for g in (0, 60):
            k_ = ease_back(prog(t, a4 + 0.3, 0.35))
            if k_ > 0:
                c.drawCircle(*pt(O, r, g), 12 * k_, M.paint(TINTA))
    if t >= a5:
        g2 = 60 * n
        raios(c, O, r, (0, 60) if n == 1 else (0, g2 % 360 if g2 < 360 else 0), ep(t, a5, 0.4), TINTA, 6)
        cunha(c, O, 0, min(60 * n, 359.9), 110, E.COR, ep(t, a5, 0.4), 0.28, 5)
        rot = "60°" if t >= c5 and n == 1 else ("120°" if n == 2 else ("180°" if n == 3 else ("360°" if n == 6 else None)))
        if rot:
            P = pt(O, 160, min(60 * n, 360) / 2 if n < 6 else 30)
            centro(c, rot, P[0], P[1] + 20, 54, "g", COR)
        c.drawCircle(*O, 11, M.paint(TINTA))

    def quatro():
        E.frase(c, t, a4, [("arco:", "g", 76, COR)] + ps("um pedaço", "i", 70), X, 260, "center", 0.12)
        E.frase(c, t, a4 + 0.8, ps("da circunferência", "i", 70), X, 360, "center", 0.12)
        E.frase(c, t, b4, ps("na pizza: a", "i", 64) + [("borda", "g", 70, AMBAR)] + ps("da fatia", "i", 64), X, 540, "center", 0.12)
    E.saida(c, t, C["s05"] - 0.1, quatro)

    def cinco():
        E.frase(c, t, a5, [("ângulo central:", "g", 66, COR)], X, 260, "center")
        E.frase(c, t, a5 + 0.7, ps("o vértice no centro", "i", 60), X, 350, "center", 0.12)
        E.frase(c, t, b5, ps("que pedaço da", "i", 60) + [("volta", "g", 64, COR)], X, 500, "center", 0.12)
        fcen(c, t, c5, "360 ÷ 6 = 60°", X, 700, 90)
    if C["s05"] <= t:
        E.saida(c, t, C["s06"] - 0.1, cinco)

    if t >= C["s06"]:
        E.frase(c, t, a6, ps("dobrou o ângulo,", "i", 62) + [("dobra o arco", "g", 66, COR)], X, 260, "center", 0.12)
        E.frase(c, t, b6, [("2 fatias", "g", 62, COR)] + ps("= o dobro de borda", "i", 58), X, 380, "center", 0.12)
        E.frase(c, t, lerp(b6, c6, 0.35), [("3 fatias", "g", 62, COR)] + ps("= o triplo", "i", 58), X, 480, "center", 0.12)
        E.frase(c, t, lerp(b6, c6, 0.7), [("6 fatias", "g", 62, COR)] + ps("= a volta toda", "i", 58), X, 580, "center", 0.12)
        E.foco(c, t, c6, 0.5, lambda a: E.pilula(c, "diretamente proporcionais", X, 760, 52, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, c6 + 1.2, ps("e aí entra a", "i", 56, TINTA2) + [("regra de três", "g", 58, TINTA2)], X, 880, "center", 0.12)


# ---------------- o exemplo ----------------
def b_exemplo(c, t, C, b):
    a7, b7, c7, d7, e7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"]
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    O, r = (380, 560), 230
    X = 1260
    E.circulo(c, t, C["s07"], *O, r, o=None, d=0.6, raio=(210, "6"), te={"raio": C["s07"] + 0.3})
    if t >= C["s07"] + 0.6:
        cunha(c, O, 0, 60, 80, E.COR, ep(t, C["s07"] + 0.6, 0.4), 0.28, 4)
        raios(c, O, r, (0, 60), ep(t, C["s07"] + 0.6, 0.4))
        arco_cor(c, O, r, 0, 60, E.COR, 16, 1.0, ease_io(prog(t, C["s07"] + 0.8, 0.5)))
        E.foco(c, t, C["s07"] + 1.0, 0.4, lambda a: centro(c, "60°", *(lambda P: (P[0], P[1] + 18))(pt(O, 120, 30)), 46, "g", COR, a))
    if t >= b7:
        arco_cor(c, O, r, 60, 360, TINTA2, 8, 1.0, ease_io(prog(t, b7, 0.8)) * (1 - ep(t, C["s09"], 0.4) * 0.0))

    def tab(a=1.0):
        tabela(c, t, [("360°", "12π"), ("60°", "x", COR)], [d7, e7], X, 600, 130, 84, cruz=a8 + 0.3, a=a)

    def sete():
        E.foco(c, t, a7, 0.4, lambda a: E.pilula(c, "passo 1: a volta inteira", X, 180, 46, "g", a=a, cor=E.SOBRE))
        fcen(c, t, b7, "C = 2 × π × 6 = 12π cm", X, 320, 72)
        E.foco(c, t, c7, 0.4, lambda a: E.pilula(c, "passo 2: a tabela", X, 450, 46, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s08"] - 0.1, sete)
    if t < C["s09"]:
        E.saida(c, t, C["s09"] - 0.1, tab)

    if C["s08"] <= t < C["s09"] + 0.5:
        def oito():
            E.foco(c, t, a8, 0.4, lambda a: E.pilula(c, "passo 3: a cruz", X, 180, 46, "g", a=a, cor=E.SOBRE))
            fcen(c, t, b8, "360x = 60 × 12π = 720π", X, 860, 66)
            fcen(c, t, c8, "x = 720π ÷ 360 = 2π", X, 980, 66, COR)
            E.frase(c, t, d8 - 0.2, ps("com", "i", 56, TINTA2) + [("π = 3:", "g", 56, TINTA2)], X - 280, 340, "center", 0.1)
            fcen(c, t, d8, "2 × 3 = 6 cm", X + 120, 340, 70)
            bola_txt(c, t, d8 + 0.8, "6 cm", O[0], 920, 90, 54)
        E.saida(c, t, C["s09"] - 0.1, oito)
    if t >= C["s09"]:
        E.frase(c, t, a9, [("60°", "g", 70, COR)] + ps("é um pedaço pequeno da volta", "i", 58), X, 230, "center", 0.1)
        fcen(c, t, b9, "2π  <  12π", X, 400, 110, COR)
        E.frase(c, t, b9 + 0.8, ps("bem menor: faz sentido", "i", 54, TINTA2), X, 490, "center", 0.1)
        E.frase(c, t, c9 - 0.4, ps("com", "i", 56, TINTA2) + [("π = 3,14:", "g", 56, TINTA2)], X, 630, "center", 0.1)
        fcen(c, t, c9, "2 × 3,14 = 6,28 cm", X, 740, 72)
        E.foco(c, t, d9, 0.5, lambda a: E.pilula(c, "resposta com π: 2π", X, 900, 54, "g", a=a, cor=E.SOBRE))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    E.frase(c, t, C["s10"], [("cuidado", "g", 92, ERRADO)] + ps("com este erro", "i", 86), W / 2, 150, "center", 0.14)
    E.frase(c, t, a10, ps("pôr o", "i", 62) + [("raio", "g", 66, ERRADO)] + ps("no lugar da", "i", 62) + [("volta", "g", 66, COR)],
            W / 2, 270, "center", 0.12)
    xa, xb = 560, 1360
    tabela(c, t, [("360°", "6", ERRADO), ("60°", "x")], [b10, b10 + 0.8], xa, 520, 130, 80)
    E.foco(c, t, c10, 0.4, lambda a: E.formula(c, "x = 1", xa, 820, 84, "g", ERRADO, a, "center"))
    if t >= c10 + 0.6:
        E.risco(c, xa - 230, 640, xa + 230, 380, t, c10 + 0.6, largura=12)
    E.frase(c, t, lerp(c10, d10, 0.5), ps("o raio", "i", 56) + [("não é a borda", "g", 60, ERRADO)], xa, 950, "center", 0.12)
    if t >= d10:
        tabela(c, t, [("360°", "12π", CERTO), ("60°", "x")], [d10, d10 + 0.5], xb, 520, 130, 80)
        E.frase(c, t, d10 + 0.8, ps("ao lado de 360°:", "i", 56) + [("a volta inteira", "g", 60, CERTO)], xb, 820, "center", 0.12)
        E.foco(c, t, d10 + 1.4, 0.5, lambda a: E.selo(c, xb, 940, 50 * ease_back(prog(t, d10 + 1.4, 0.5)), True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    X = 1260

    def onze():
        E.frase(c, t, a11, ps("ângulo vira", "i", 76, CLARO) + [("fração da volta", "g", 84, BR)], W / 2, 190, "center", 0.12)
        O = (420, 600)
        if t >= a11:
            c.drawCircle(*O, 220, M.paint(BR, ep(t, a11, 0.4), stroke=6))
            for k in range(6):
                M.line(c, *O, *pt(O, 220, 30 + 60 * k), CLARO, ep(t, c11, 0.4) * 0.6, 3)
            cunha(c, O, 30, 90, 220, CLARO, ep(t, b11, 0.4), 0.5, 0)
            arco_cor(c, O, 220, 30, 90, CLARO, 14, ep(t, b11, 0.4))
        E.formula_em(c, t, b11, "f{60}{360}", X - 330, 520, 100, "g", BR, "center")
        E.formula_em(c, t, c11, "= f{1}{6}", X - 80, 520, 100, "g", CLARO, "center")
        E.formula_em(c, t, d11, "f{1}{6} × 12π = 2π", X, 800, 96, "g", BR, "center")
        E.frase(c, t, d11 + 1.4, ps("sem cruz", "i", 64, CLARO), X, 960, "center")
    E.saida(c, t, C["s12"] - 0.1, onze)

    if C["s12"] <= t < C["s13"] + 0.5:
        def doze():
            E.frase(c, t, C["s12"] + 0.2, ps("as frações que", "i", 76, CLARO) + [("mais caem", "g", 84, BR)], W / 2, 190, "center", 0.12)
            for i, (g, fr, t0) in enumerate(((90, "f{1}{4}", a12), (180, "f{1}{2}", b12), (120, "f{1}{3}", c12), (45, "f{1}{8}", d12))):
                cx = 300 + 440 * i
                mini(c, (cx, 520), 140, g / 360, CLARO, BR, ep(t, t0, 0.5))
                E.foco(c, t, t0 + 0.2, 0.4, lambda a, cx=cx, g=g: centro(c, f"{g}°", cx, 780, 80, "g", BR, a))
                E.foco(c, t, t0 + 0.4, 0.4, lambda a, cx=cx, fr=fr: E.formula(c, fr, cx, 950, 84, "g", CLARO, a, "center"))
        E.saida(c, t, C["s13"] - 0.1, doze)

    if t >= C["s13"]:
        E.frase(c, t, a13, ps("o arco é a", "i", 66, CLARO) + [("mesma fração", "g", 72, BR)] + ps("da volta", "i", 66, CLARO), W / 2, 240, "center", 0.12)
        E.frase(c, t, b13, [("50°?", "g", 90, BR)] + ps("não compensa", "i", 72, ERRADO), W / 2, 450, "center", 0.14)
        E.formula_em(c, t, c13, "f{50}{360} = f{5}{36}", W / 2, 680, 100, "g", CLARO, "center")
        E.foco(c, t, d13, 0.5, lambda a: E.pilula(c, "monte a tabela", W / 2, 900, 60, "g", fundo=E.mix(E.COR, BR, 0.25), a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    O, r = (520, 580), 280
    E.foco(c, t, C["s14"] + 0.5, 0.5, lambda a: relogio_min(c, O, r, a))
    E.foco(c, t, a14, 0.4, lambda a: E.escreve(c, "10 cm", O[0] + 24, O[1] - r * 0.45, 56, "g", COR, a))
    E.frase(c, t, a14, ps("ponteiro dos minutos:", "i", 56) + [("10 cm", "g", 60, COR)], 1000, 330, "left", 0.12)
    E.frase(c, t, b14, ps("em", "i", 60) + [("20 minutos,", "g", 64, COR)], 1000, 450, "left", 0.12)
    E.frase(c, t, b14 + 0.8, ps("quanto a ponta percorre?", "i", 58), 1000, 550, "left", 0.12)
    E.frase(c, t, c14, ps("use", "i", 56) + [("π = 3", "g", 60)], 1000, 660, "left", 0.12)
    E.relogio(c, t, C["s15.a"], 1490, 760, 120)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a16, b16, c16 = C["s16.a"], C["s16.b"], C["s16.c"]
    a17, b17, c17, d17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    O, r = (440, 580), 260
    X = 1250
    # o ponteiro anda 20 minutos: do 12 ao 4
    gira = 120 * ease_io(prog(t, c16, 1.4)) if t >= c16 else 0.0
    if t >= c16:
        cunha(c, O, 90 - gira, 90, r * 0.75, E.COR, 1.0, 0.25, 0)
    relogio_min(c, O, r, ep(t, C["s16"], 0.4), 90 - gira)
    if t >= c16:
        arco_cor(c, O, r * 0.8, 90 - gira, 90, E.COR, 14, 1.0)
        E.foco(c, t, c16 + 1.2, 0.4, lambda a: centro(c, "120°", *(lambda P: (P[0], P[1] + 18))(pt(O, r * 0.45, 30)), 50, "g", COR, a))

    def dezesseis():
        E.frase(c, t, C["s16"] + 0.3, ps("o ponteiro é o", "i", 60) + [("raio", "g", 64, COR)], X, 220, "center", 0.12)
        fcen(c, t, a16, "C = 2 × 3 × 10 = 60 cm", X, 360, 72)
        E.frase(c, t, b16, [("1 volta", "g", 66, COR)] + ps("= 60 minutos", "i", 62), X, 500, "center", 0.12)
        E.formula_em(c, t, c16, "20 min = f{1}{3} da volta", X, 670, 72, "g", None, "center")
        fcen(c, t, c16 + 1.6, "360 ÷ 3 = 120°", X, 840, 72, COR)
    E.saida(c, t, C["s17"] - 0.1, dezesseis)
    if t >= C["s17"]:
        E.formula_em(c, t, a17, "f{1}{3} × 60 = 20 cm", X - 150, 230, 80, "g", COR, "center")
        bola_txt(c, t, a17 + 0.8, "20 cm", X + 360, 200, 90, 50)
        E.frase(c, t, b17 - 0.6, ps("pela tabela:", "i", 52, TINTA2), X, 400, "center", 0.1)
        tabela(c, t, [("360°", "60"), ("120°", "x", COR)], [b17, c17], X, 540, 120, 72, cruz=d17 - 0.3, wcol=320)
        fcen(c, t, d17, "360x = 120 × 60 = 7200", X, 820, 62)
        fcen(c, t, lerp(d17, C["s17.end"], 0.45), "x = 7200 ÷ 360 = 20", X, 940, 62, CERTO)
        E.foco(c, t, lerp(d17, C["s17.end"], 0.8), 0.5, lambda a: E.selo(c, X + 380, 920, 44 * ease_back(prog(t, lerp(d17, C["s17.end"], 0.8), 0.5)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s18.a", "arco = fração da volta", "que o ângulo é"), ("s18.b", "calcule", "a volta inteira"),
                 ("s18.c", "pegue a fração", "ou a regra de três"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 28, 54, a=a), centro(c, str(i + 1), 260, y - 6, 62, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 66, COR), (l2, "i", 66)], 360, y, "left", 0.2)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s19.a"], [("Ângulo", "g", 130, COR)], XE, 440)
    E.frase(c, t, C["s19.a"] + 0.3, [("inscrito", "g", 130, COR)], XE, 570)
    E.frase(c, t, C["s19.b"], ps("vale a", "i", 76) + [("metade", "g", 80)], XE, 700, passo=0.12)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, arco=b_arco, exemplo=b_exemplo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
