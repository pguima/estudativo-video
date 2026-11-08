"""Visual — Estudativo · MAT-RAZ-020: o que é escala, medida real e do desenho.
Peças locais: mapa() é um recorte de mapa com duas cidades, régua e a escala no canto; escada() é a escada do metro (km → mm),
com o salto em destaque; parede() é a planta com uma parede cotada. Todo instante vem de C[...]."""
from decimal import Decimal as D

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-020_o_que_e_escala.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("escala", "real", "papel", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 3 * 50000 == 150000 and 150000 / 100 == 1500 and D(1500) / 1000 == D("1.5")
assert 400 / 50 == 8 and 8 * 50 == 400 and 4 * 100 == 400
assert 150000 > 3 * 40000
assert D(50000) / 100 == 500 and D(50000) / 100000 == D("0.5") and 3 * D("0.5") == D("1.5")
assert 7 * 200000 == 1400000 and D(1400000) / 100000 == 14 and D(200000) / 100000 == 2 and 7 * 2 == 14


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


def fesq(c, t, t0, s, x, y, size, cor=None, est="g"):
    E.formula_em(c, t, t0, s, x, y, size, est, cor, "left")


def bola_res(c, t, t0, s, cx, cy, r=130, size=80, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)))


def pil(c, t, t0, s, cx, cy, size=52, fundo=None):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, s, cx, cy, size, "g", fundo=fundo, a=a, cor=E.SOBRE if fundo is None else BR))


def mapa(c, t, t0, x, y, w, h, escala="1 : 50.000", treg=None, tesc=None, rot="3 cm"):
    """recorte de mapa: rio, curvas de nível, duas cidades; treg = régua entre as cidades; tesc = destaque na escala do canto"""
    a = ep(t, t0, 0.6)
    if a <= 0:
        return None
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 22, 22)
    c.drawRRect(rr, M.paint("#FFFFFF", a * 0.92))
    c.save(); c.clipRRect(rr, True)
    for k in range(4):  # curvas de nível
        c.drawOval(skia.Rect.MakeXYWH(x + w * 0.55 - k * 60, y + h * 0.05 - k * 40, w * 0.5 + k * 120, h * 0.45 + k * 80), M.paint(FIO, a, stroke=3))
    p = skia.Path()  # rio
    p.moveTo(x - 10, y + h * 0.8); p.cubicTo(x + w * 0.3, y + h * 0.6, x + w * 0.5, y + h * 1.0, x + w + 10, y + h * 0.7)
    c.drawPath(p, M.paint(E.mix(E.COR, "#FFFFFF", 0.7), a, stroke=18))
    c.restore()
    c.drawRRect(rr, M.paint(TINTA, a, stroke=4))
    ax, ay, bx, by = x + w * 0.22, y + h * 0.42, x + w * 0.78, y + h * 0.42
    for cx, cy, nome in ((ax, ay, "A"), (bx, by, "B")):
        c.drawCircle(cx, cy, 18, M.paint(E.COR, a))
        c.drawCircle(cx, cy, 18, M.paint(BR, a, stroke=4))
        E.escreve(c, nome, cx - 18, cy - 34, 48, "g", TINTA, a)
    if treg is not None:
        q = ep(t, treg, 0.7)
        if q > 0:
            M.line(c, ax, ay + 50, lerp(ax, bx, q), ay + 50, TINTA, 1, 6)
            for xx in (ax, lerp(ax, bx, q)):
                M.line(c, xx, ay + 36, xx, ay + 64, TINTA, 1, 6)
            E.foco(c, t, treg + 0.5, 0.4, lambda b: centro(c, rot, (ax + bx) / 2, ay + 120, 60, "g", E.COR, b))
    E.escreve(c, escala, x + w - E.larg(escala, "b", 40) - 30, y + h - 30, 40, "b", TINTA2, a)
    if tesc is not None:
        q = ep(t, tesc, 0.5)
        E.caixa_pontilhada(c, x + w - E.larg(escala, "b", 40) - 50, y + h - 80, E.larg(escala, "b", 40) + 40, 70, q, prog_=q)
    return ax, bx, ay


NOMES = ("km", "hm", "dam", "m", "dm", "cm", "mm")


def escada(c, t, t0, x, y, pw=150, ph=62, saltos=(), size=46):
    """escada do metro: km no topo à esquerda, mm embaixo à direita. saltos = [(de, para, instante, rótulo)] com arco por cima"""
    a = ep(t, t0, 0.5)
    if a <= 0:
        return
    for i, n in enumerate(NOMES):
        sx, sy = x + i * pw, y + i * ph
        M.line(c, sx, sy, sx + pw, sy, TINTA, a, 5)
        if i < len(NOMES) - 1:
            M.line(c, sx + pw, sy, sx + pw, sy + ph, TINTA, a, 5)
        centro(c, n, sx + pw / 2, sy - 14, size, "b", TINTA, a)
    for de, para, ti, rot in saltos:
        q = ep(t, ti, 0.7)
        if q <= 0:
            continue
        i0, i1 = NOMES.index(de), NOMES.index(para)
        x0, y0 = x + i0 * pw + pw / 2, y + i0 * ph - 70
        x1, y1 = x + i1 * pw + pw / 2, y + i1 * ph - 70
        alto = min(y0, y1) - 70
        pth = skia.Path(); pth.moveTo(x0, y0); pth.cubicTo(x0, alto, x1, alto, x1, y1)
        me = skia.PathMeasure(pth, False)
        seg = skia.Path(); me.getSegment(0, me.getLength() * q, seg, True)
        c.drawPath(seg, M.paint(E.COR, 1, stroke=7, cap_round=True))
        if q >= 1:
            c.drawPath(skia.Path.Polygon([(x1 - 14, y1 - 18), (x1 + 14, y1 - 18), (x1, y1 + 4)], True), M.paint(E.COR))
        E.foco(c, t, ti + 0.4, 0.4, lambda b, rot=rot, xm=(x0 + x1) / 2, al=alto: E.pilula(c, rot, xm, al - 10, 40, "g", a=b, cor=E.SOBRE))


def lembrete(c, t, C, cena, itens):
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

    def um():
        mapa(c, t, C["s01"] + 0.2, 260, 170, 1000, 640, treg=a1, tesc=c1)
        E.frase(c, t, b1, ps("no real:", "i", 76), 1360, 400, "left")
        E.foco(c, t, b1 + 0.3, 0.5, lambda a: E.escreve(c, "? km", 1360, 540, 130, "g", COR, a))
        E.frase(c, t, c1 + 0.2, ps("um número pequeno,", "i", 64) + ps("no canto do mapa", "g", 64, COR), W / 2, 960, "center", 0.1)
        p = ease_io(prog(t, c1, 0.8))
        E.cursor(c, lerp(1500, 1150, p), lerp(950, 790, p), ep(t, c1, 0.4))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return

    def nome():
        E.frase(c, t, C["s02"] + 0.1, ps("esse número é a", "i", 90), W / 2, 380, "center", 0.12)
        E.frase(c, t, C["s02.a"], [("escala", "g", 230, COR)], W / 2, 650, "center")
    E.saida(c, t, C["s02.b"] + 0.5, nome)
    if t >= C["s02.b"] + 0.5:
        tb, tc = C["s02.b"] + 0.6, C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1450, 540, 280 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, tb, ps("até o fim da aula", "i", 92), XE, 330, passo=0.14)
        E.frase(c, t, tb + 0.6, [("ler", "i", 110), ("qualquer escala", "g", 110, COR)], XE, 480, passo=0.14)
        E.frase(c, t, lerp(tb, tc, 0.45), [("papel", "g", 90), ("→", "g", 90, COR), ("real", "g", 90)], XE, 640, passo=0.14)
        E.frase(c, t, lerp(tb, tc, 0.7), [("real", "g", 90), ("→", "g", 90, COR), ("papel", "g", 90)], XE, 780, passo=0.14)
        E.foco(c, t, tc + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1450, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1450, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "razão: compara duas medidas", "na mesma unidade"), ("s03.c", "proporção:", "o produto cruzado"),
                              ("s03.d", "a escada", "do metro")))


# ---------------- o que é escala ----------------
def b_escala(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5, d5, e5, f5 = (C[f"s05.{k}"] for k in "abcdef")
    a6, b6 = C["s06.a"], C["s06.b"]

    def defin():
        fcen(c, t, a4, "escala = f{desenho}{real}", W / 2, 470, 150, COR)
        pil(c, t, b4, "as duas na mesma unidade", W / 2, 700, 64)
        E.frase(c, t, lerp(b4, C["s04.end"], 0.5), ps("desenho em cima, real embaixo", "i", 64, TINTA2), W / 2, 870, "center", 0.1)
    E.saida(c, t, C["s05"] - 0.1, defin)
    if t < C["s05"]:
        return

    def planta():
        E.foco(c, t, a5, 0.5, lambda a: centro(c, "1 : 100", W / 2, 330, 200, "g", COR, a))
        E.frase(c, t, b5, ps("um para cem", "i", 80, TINTA2), W / 2, 450, "center", 0.12)
        fcen(c, t, c5, "1 cm", 520, 650, 110)
        E.foco(c, t, c5 + 0.3, 0.4, lambda a: centro(c, "no papel", 520, 740, 54, "i", TINTA2, a))
        if t >= d5 - 0.2:
            q = ep(t, d5 - 0.2, 0.5)
            M.arrow(c, 700, 620, 700 + 360 * q, 620, E.COR, 1, 6, 18, q)
        fcen(c, t, d5, "100 cm", 1300, 650, 110)
        E.foco(c, t, d5 + 0.3, 0.4, lambda a: centro(c, "na casa", 1300, 740, 54, "i", TINTA2, a))
        fcen(c, t, e5, "= 1 m", 1650, 650, 110, COR)
        pil(c, t, f5, "1 cm no papel = 1 m na casa", W / 2, 900, 64)
    E.saida(c, t, C["s06"] - 0.1, planta)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"] + 0.2, ps("a escala", "i", 84) + [("não tem unidade", "g", 88, COR)], W / 2, 250, "center", 0.12)
    E.frase(c, t, a6, ps("vale para", "i", 70) + [("qualquer unidade,", "g", 70, COR)] + ps("a mesma em cima e embaixo", "i", 70), W / 2, 420, "center", 0.1)
    fcen(c, t, lerp(a6, b6, 0.45), "1 m no papel  →  100 m de verdade", W / 2, 580, 80, TINTA2)
    E.frase(c, t, b6, ps("na prova:", "i", 80) + [("centímetro,", "g", 84, COR)] + ps("a unidade da régua", "i", 80), W / 2, 800, "center", 0.12)


# ---------------- do papel para o real ----------------
def b_real(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    E.foco(c, t, a7, 0.5, lambda a: E.pilula(c, "1 : 50.000", 330, 170, 60, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, b7, 0.5, lambda a: E.pilula(c, "mapa: 3 cm", 760, 170, 60, "g", fundo=TINTA, a=a))

    def conta():
        fcen(c, t, c7, "f{1}{50.000} = f{3}{x}", 500, 450, 110)
        E.foco(c, t, c7 + 0.4, 0.4, lambda a: (E.escreve(c, "desenho", 800, 420, 46, "i", TINTA2, a), E.escreve(c, "real", 800, 520, 46, "i", TINTA2, a)))
        fesq(c, t, a8, "x = 3 × 50.000", 1060, 420, 90)
        fesq(c, t, b8, "x = 150.000 cm", 1060, 560, 90, COR)
        pil(c, t, c8, "papel → real: × o número de baixo", W / 2, 750, 56)
    E.saida(c, t, a9 - 0.6, conta)
    if t < a9 - 0.6:
        return
    E.foco(c, t, a9 - 0.5, 0.5, lambda a: E.escreve(c, "150.000 cm", 1180, 360, 90, "g", COR, a))
    escada(c, t, lerp(C["s09"], a9, 0.4), 180, 420, 150, 64, saltos=[("cm", "m", a9, "÷ 100"), ("m", "km", b9, "÷ 1.000")])
    fesq(c, t, a9 + 0.6, "= 1.500 m", 1180, 520, 90)
    fesq(c, t, b9 + 0.6, "= 1,5 km", 1180, 680, 90, COR)
    E.frase(c, t, c9, [("3 cm", "g", 70)] + ps("no mapa =", "i", 70) + [("1,5 km", "g", 74, COR)] + ps("em linha reta", "i", 70), W / 2, 960, "center", 0.1)


# ---------------- do real para o papel ----------------
def parede(c, t, t0, x, y, w, rot, a_rot=None):
    """planta: uma parede cotada"""
    a = ep(t, t0, 0.5)
    if a <= 0:
        return
    M.rrect(c, x, y, w, 34, 4, TINTA, a)
    M.line(c, x, y + 80, x + w, y + 80, TINTA2, a, 4)
    for xx in (x, x + w):
        M.line(c, xx, y + 62, xx, y + 98, TINTA2, a, 4)
    E.foco(c, t, a_rot if a_rot is not None else t0 + 0.3, 0.4, lambda q: centro(c, rot, x + w / 2, y + 160, 64, "g", E.COR, q))


def b_papel(c, t, C, b):
    a10, b10 = C["s10.a"], C["s10.b"]
    a11, b11, c11, d11 = (C[f"s11.{k}"] for k in "abcd")
    a12, b12 = C["s12.a"], C["s12.b"]
    E.frase(c, t, C["s10"] + 0.2, ps("o caminho", "i", 76) + [("contrário", "g", 80, COR)], XE, 170, "left", 0.12)
    parede(c, t, a10, XE, 250, 700, "4 m")
    E.foco(c, t, b10, 0.5, lambda a: E.pilula(c, "planta 1 : 50", 1300, 260, 64, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, lerp(b10, C["s10.end"], 0.4), ps("quantos", "i", 70) + [("cm no papel?", "g", 72, COR)], 1300, 400, "center", 0.1)

    def conta():
        fesq(c, t, a11, "4 m = 400 cm", XE, 600, 90)
        pil(c, t, b11, "real → papel: ÷ o número de baixo", 1300, 560, 48)
        fesq(c, t, c11, "400 ÷ 50 = 8 cm", XE, 770, 100, COR)
        fesq(c, t, d11, "8 × 50 = 400", XE, 930, 72, TINTA2)
        E.foco(c, t, d11 + 0.6, 0.5, lambda a: E.selo(c, XE + 520, 905, 44, True, a))
        parede(c, t, c11 + 0.5, 1150, 700, 8 * 40, "8 cm")
    E.saida(c, t, C["s12"] - 0.1, conta)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"] + 0.2, ps("pela proporção", "i", 76, TINTA2), W / 2, 560, "center", 0.12)
    fcen(c, t, a12, "f{1}{50} = f{x}{400}", 640, 790, 110)
    fesq(c, t, b12, "50x = 400", 1000, 740, 84)
    fesq(c, t, b12 + 0.8, "x = 8 cm", 1000, 880, 96, COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a13, b13 = C["s13.a"], C["s13.b"]
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, C["s13"] + 0.2, [("cuidado:", "g", 90, ERRADO)] + ps("esquecer a", "i", 84) + [("escada", "g", 90)], W / 2, 200, "center", 0.12)
    fcen(c, t, lerp(a13, b13, 0.35), "3 × 50.000 = 150.000", W / 2, 400, 100)

    def errado():
        fcen(c, t, b13, "150.000 km?", W / 2, 580, 130, ERRADO)
        E.frase(c, t, a14, ps("mais que", "i", 72, ERRADO) + [("3 voltas na Terra!", "g", 72, ERRADO)], W / 2, 720, "center", 0.1)
        tr = a14 + 1.2
        if t >= tr:
            E.risco(c, W / 2 - 420, 610, W / 2 + 420, 490, t, tr, largura=14)
    E.saida(c, t, b14 - 0.1, errado)
    if t < b14 - 0.1:
        return
    E.frase(c, t, b14, ps("a conta sai na unidade do desenho:", "i", 70) + [("cm", "g", 76, COR)], W / 2, 600, "center", 0.1)
    fcen(c, t, c14, "150.000 cm = 1,5 km", W / 2, 820, 110, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    a16, b16, c16 = C["s16.a"], C["s16.b"], C["s16.c"]
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]

    def regra():
        E.frase(c, t, C["s15"] + 0.3, ps("o atalho", "i", 70, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a15, ps("quanto vale", "i", 110, CLARO) + [("1 cm?", "g", 120, BR)], W / 2, 340, "center", 0.12)
        fcen(c, t, lerp(a15, b15, 0.45), "1 : n  →  1 cm vale n cm", W / 2, 520, 90, BR)
        E.frase(c, t, b15, ps("em metros:", "i", 70, CLARO) + [("vírgula 2 casas ←", "g", 74, BR)], W / 2, 720, "center", 0.1)
        E.frase(c, t, c15, ps("em quilômetros:", "i", 70, CLARO) + [("5 casas ←", "g", 74, BR)], W / 2, 860, "center", 0.1)
    E.saida(c, t, C["s16"] - 0.1, regra)
    if t < C["s16"]:
        return

    def exemplo():
        E.frase(c, t, C["s16"] + 0.2, ps("na escala", "i", 76, CLARO) + [("1 : 50.000,", "g", 80, BR)] + ps("1 cm vale", "i", 76, CLARO), W / 2, 200, "center", 0.1)
        s = 140
        x0 = 380
        E.foco(c, t, C["s16"] + 0.6, 0.5, lambda a: E.anda(c, t, "50000", 5, [(a16 - 0.6, 3), (b16 - 0.6, 0)], x0, 480, s, cor=BR, cor_v=CLARO, cor_novo=CLARO, tv=a16 - 0.8))
        xu = x0 + E.casa(s) * 5 + 40
        for i, (ti, u) in enumerate(((C["s16"] + 0.6, "cm"), (a16 - 0.1, "m"), (b16 - 0.1, "km"))):
            fim = (a16 - 0.2, b16 - 0.2, 1e9)[i]
            E.saida(c, t, fim, lambda u=u, ti=ti: E.foco(c, t, ti, 0.4, lambda a: E.escreve(c, u, xu, 480, 100, "b", CLARO, a)), d=0.2)
        fcen(c, t, a16, "1 cm = 500 m", 640, 690, 96, BR)
        fcen(c, t, b16, "= 0,5 km", 1280, 690, 96, BR)
        E.foco(c, t, c16, 0.5, lambda a: E.formula(c, "3 cm  →  3 × 0,5 = 1,5 km", W / 2, 880, 100, "g", CLARO, a, "center"))
    E.saida(c, t, C["s17"] - 0.1, exemplo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"] + 0.2, ps("funciona porque", "i", 70, CLARO), W / 2, 200, "center", 0.1)
    fcen(c, t, a17, "1 m = 100 cm", W / 2, 380, 100, BR)
    fcen(c, t, b17, "1 km = 100.000 cm", W / 2, 530, 100, BR)
    E.foco(c, t, lerp(b17, c17, 0.5), 0.5, lambda a: E.selo(c, 520, 730, 46, False, a))
    E.frase(c, t, lerp(b17, c17, 0.5) + 0.1, ps("do real para o papel:", "i", 64, CLARO), 600, 755, "left", 0.1)
    E.frase(c, t, c17, ps("passe para", "i", 72, CLARO) + [("cm", "g", 76, BR)] + ps("e", "i", 72, CLARO) + [("divida", "g", 76, BR)], W / 2, 900, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s18.a"] - 0.8, ps("escala", "i", 84), XE, 380, passo=0.1)
    E.foco(c, t, C["s18.a"], 0.5, lambda a: E.escreve(c, "1 : 200.000", XE + 280, 385, 100, "g", COR, a))
    E.frase(c, t, C["s18.b"] - 0.8, ps("no mapa:", "i", 84), XE, 540, passo=0.1)
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.escreve(c, "7 cm", XE + 340, 545, 100, "g", TINTA, a))
    E.frase(c, t, C["s18.c"], ps("distância real", "i", 92) + [("em km?", "g", 96, COR)], XE, 790, passo=0.12)
    E.relogio(c, t, C["s19.a"], 1560, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a20, b20, c20, d20 = (C[f"s20.{k}"] for k in "abcd")
    E.frase(c, t, C["s20"] + 0.2, ps("do papel para o real:", "i", 76) + [("multiplica", "g", 80, COR)], W / 2, 190, "center", 0.12)
    fcen(c, t, a20, "7 × 200.000 = 1.400.000 cm", W / 2, 380, 100)
    E.foco(c, t, b20 - 0.6, 0.4, lambda a: E.pilula(c, "vírgula 5 casas ←", 620, 560, 52, "g", fundo=TINTA, a=a))
    fesq(c, t, b20, "= 14 km", 900, 590, 110, COR)
    E.frase(c, t, c20 - 0.4, ps("pelo", "i", 72) + [("atalho:", "g", 72, COR)], 420, 790, "center", 0.1)
    fesq(c, t, c20, "1 cm = 2 km", 640, 800, 90)
    fesq(c, t, d20, "7 × 2 =", 640, 950, 90)
    bola_res(c, t, d20 + 0.5, "14 km", 1150, 920, 120, 70, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s21.a", "desenho sobre real,", "mesma unidade"), ("s21.b", "do papel para o real:", "multiplica"),
                 ("s21.c", "do real para o papel:", "divide"), ("s21.d", "converta", "no fim"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 330 + i * 175
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 52, a=a), centro(c, str(i + 1), 230, y - 8, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 72) + [(l2, "g", 72, COR)], 320, y, "left", 0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a0, b0 = C["s22.a"], C["s22.b"]
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula, o contrário", "i", 80), XE, 220, passo=0.12)
    E.frase(c, t, a0, [("4 cm", "g", 90, COR)] + ps("representam", "i", 84) + [("10 km", "g", 90, COR)], XE, 380, passo=0.12)
    E.frase(c, t, a0 + 1.4, ps("qual é a", "i", 84) + [("escala?", "g", 90)], XE, 500, passo=0.12)
    E.frase(c, t, b0, ps("e a", "i", 70) + [("escala gráfica,", "g", 72, COR)] + ps("com a régua", "i", 70), XE, 630, passo=0.1)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(970, 785, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, escala=b_escala, real=b_real, papel=b_papel, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
