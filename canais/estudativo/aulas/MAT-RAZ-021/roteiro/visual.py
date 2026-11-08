"""Visual — Estudativo · MAT-RAZ-021: descobrir a escala e usar escala gráfica.
Peças locais: mapa() é o recorte de mapa da aula MAT-RAZ-020 (com a escala escrita ou a barrinha no canto); barra() é a escala
gráfica, com trechos alternados e a distância real embaixo; trecho() é a chave que marca um pedaço medido. U = pixels por centímetro
de mapa, para que barra, cidades e régua fiquem sempre na mesma proporção. Todo instante vem de C[...]."""
from decimal import Decimal as D

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-021_descobrir_a_escala_e_escala_grafica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("achar", "grafica", "atalho", "questao", "fim"))
BR = "#FFFFFF"
U = 120  # px por centímetro de mapa

assert 50000 * 2 == 100000
assert 10 * 1000 == 10000 and 10000 * 100 == 1000000 and 1000000 // 4 == 250000 and 250000 * 4 == 1000000
assert 6 // 2 == 3 and 3 * 5 == 15 and 5 * 100000 == 500000 and 500000 // 2 == 250000
assert D(10) / 4 == D("2.5")
assert 6 * 100000 == 600000 and 600000 // 3 == 200000 and 9 // 3 == 3 and 3 * 6 == 18 and 9 * 200000 == 1800000 and 1800000 // 100000 == 18


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


def mapa(c, a, x, y, w, h, escala="1 : 50.000", cor_esc=None):
    """recorte de mapa com rio, curvas de nível, duas cidades e a escala escrita no canto"""
    if a <= 0:
        return
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 22 * w / 1000, 22 * w / 1000)
    c.drawRRect(rr, M.paint("#FFFFFF", a * 0.92))
    c.save(); c.clipRRect(rr, True)
    k = w / 1000
    for i in range(4):
        c.drawOval(skia.Rect.MakeXYWH(x + w * 0.55 - i * 60 * k, y + h * 0.05 - i * 40 * k, w * 0.5 + i * 120 * k, h * 0.45 + i * 80 * k), M.paint(FIO, a, stroke=3))
    p = skia.Path()
    p.moveTo(x - 10, y + h * 0.8); p.cubicTo(x + w * 0.3, y + h * 0.6, x + w * 0.5, y + h * 1.0, x + w + 10, y + h * 0.7)
    c.drawPath(p, M.paint(E.mix(E.COR, "#FFFFFF", 0.7), a, stroke=18 * k))
    c.restore()
    c.drawRRect(rr, M.paint(TINTA, a, stroke=4))
    for cx in (x + w * 0.22, x + w * 0.78):
        c.drawCircle(cx, y + h * 0.42, 18 * k, M.paint(E.COR, a))
    if escala:
        s = 44 * k
        E.escreve(c, escala, x + w - E.larg(escala, "b", s) - 30 * k, y + h - 30 * k, s, "b", cor_esc or TINTA2, a)


def barra(c, x, y, n, trecho, a=1.0, rotulos=None, size=46, h=26, escuro=False):
    """escala gráfica: n trechos de `trecho` px, alternando cheio e vazio; rotulos = textos embaixo de cada divisa"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA
    for i in range(n):
        r = skia.Rect.MakeXYWH(x + i * trecho, y, trecho, h)
        c.drawRect(r, M.paint(tinta if i % 2 == 0 else ("#FFFFFF" if not escuro else "#07070F"), a))
        c.drawRect(r, M.paint(tinta, a, stroke=4))
    for i, s in enumerate(rotulos or ()):
        centro(c, s, x + i * trecho, y + h + size * 1.2, size, "b", tinta, a)


def trecho(c, t, t0, x0, x1, y, rot, cor=None, size=46, cima=True):
    """chave sobre (ou sob) um trecho, com o rótulo"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    cor = cor or E.COR
    E.chave(c, x0, x1, y, cor, q, -22 if cima else 22, 5)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rot, (x0 + x1) / 2, y + (-48 if cima else 48 + size * 0.7), size, "g", cor, a))


def regua(c, x, y, cm, a=1.0):
    """régua de `cm` centímetros, encostada embaixo de y"""
    if a <= 0:
        return
    w = cm * U + 40
    M.rrect(c, x - 20, y, w, 70, 8, "#F7E9B0", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 20, y, w, 70), 8, 8), M.paint(TINTA, a, stroke=3))
    for i in range(cm * 10 + 1):
        xx = x + i * U / 10
        alto = 30 if i % 10 == 0 else (20 if i % 5 == 0 else 12)
        M.line(c, xx, y, xx, y + alto, TINTA, a, 3 if i % 10 == 0 else 2)
        if i % 10 == 0:
            centro(c, str(i // 10), xx, y + 62, 26, "b", TINTA, a)


def lembrete2(c, t, C, cena, itens):
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 930, 860
    for i, (k, l1, l2) in enumerate(itens):
        y = 260 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 690, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.55), ps("faltou alguma?", "i", 52, COR) + ps("procure no canal", "i", 52), 930, 860, "left", 0.12)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        mapa(c, ep(t, C["s01"] + 0.2, 0.5), 120, 260, 800, 520)
        E.foco(c, t, C["s01"] + 0.4, 0.4, lambda a: centro(c, "original", 520, 860, 54, "i", TINTA2, a))
        q = ep(t, a1, 0.9)
        if q > 0:
            w = lerp(800, 400, ease_io(q))
            mapa(c, ep(t, a1, 0.3), lerp(120, 1180, ease_io(q)), lerp(260, 380, ease_io(q)), w, w * 0.65,
                 cor_esc=ERRADO if t >= c1 else (E.COR if t >= b1 else None))
            E.foco(c, t, a1 + 0.6, 0.4, lambda a: centro(c, "cópia pela metade", 1380, 720, 54, "i", TINTA2, a))
        if t >= b1:
            E.foco(c, t, b1, 0.4, lambda a: E.caixa_pontilhada(c, 1430, 580, 160, 54, a, E.COR))
            E.foco(c, t, b1 + 0.2, 0.4, lambda a: E.pilula(c, "ainda diz 1 : 50.000", 1380, 820, 46, "g", fundo=ERRADO if t >= c1 else None, a=a, cor=E.SOBRE))
        if t >= c1:
            E.frase(c, t, c1, [("a escala escrita", "i", 70), ("está errada", "g", 70, ERRADO)], W / 2, 180, "center", 0.12)
        fcen(c, t, d1, "escala de verdade: 1 : 100.000", W / 2, 990, 76, CERTO)
    E.saida(c, t, C["s02"] - 0.1, um)

    def certo():
        E.foco(c, t, C["s02"] + 0.2, 0.5, lambda a: centro(c, "um jeito de escala que", W / 2, 380, 84, "i", TINTA, a))
        E.foco(c, t, C["s02.a"], 0.5, lambda a: (centro(c, "continua certo", W / 2, 520, 120, "g", E.COR, a),
                                                  centro(c, "em qualquer cópia", W / 2, 640, 84, "i", TINTA, a)))
        E.foco(c, t, C["s02.a"] + 0.6, 0.5, lambda a: barra(c, W / 2 - 240, 760, 2, 240, a, ("0", "5", "10 km"), 46))
    if C["s02"] - 0.1 <= t:
        E.saida(c, t, C["s02.b"] - 0.1, certo)
    if t >= C["s02.b"] - 0.1:
        tb = C["s02.b"]
        tc = lerp(tb, C["s02.end"], 0.45)
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1450, 540, 280 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, tb, ps("até o fim da aula", "i", 92), XE, 330, passo=0.14)
        E.frase(c, t, tb + 0.8, [("usar", "i", 110), ("esse jeito", "g", 110, COR)], XE, 480, passo=0.14)
        E.frase(c, t, lerp(tb, tc, 0.6), ps("e achar a escala", "i", 84), XE, 640, passo=0.12)
        E.frase(c, t, lerp(tb, tc, 0.85), ps("de um mapa sem escala", "i", 84, COR), XE, 760, passo=0.12)
        E.foco(c, t, tc + 0.2, 0.5, lambda a: (centro(c, "escala", 1450, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "gráfica", 1450, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete2(c, t, C, "s03", (("s03.b", "escala = desenho sobre real,", "na mesma unidade"), ("s03.c", "subir e descer", "a escada do metro")))


# ---------------- achar a escala ----------------
def b_achar(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    E.frase(c, t, C["s04"] + 0.2, ps("mapa", "i", 70) + [("sem escala", "g", 74, COR)], XE, 170, "left", 0.12)
    E.foco(c, t, a4, 0.5, lambda a: E.pilula(c, "papel: 4 cm", 1030, 150, 56, "g", fundo=TINTA, a=a))
    E.foco(c, t, b4, 0.5, lambda a: E.pilula(c, "real: 10 km", 1460, 150, 56, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s05"] - 0.1, lambda: E.frase(c, t, lerp(b4, C["s04.end"], 0.4), ps("qual é a", "i", 90) + [("escala?", "g", 96, COR)], W / 2, 500, "center", 0.12))

    def unidade():
        pil(c, t, a5, "desenho sobre real, na mesma unidade", W / 2, 320, 54)
        fesq(c, t, b5, "10 km × 1.000 = 10.000 m", 380, 500, 84)
        fesq(c, t, c5, "10.000 m × 100 = 1.000.000 cm", 380, 640, 84, COR)
    if t >= C["s05"]:
        E.saida(c, t, a6 - 0.1, unidade)
    if t < a6 - 0.1:
        return
    fcen(c, t, a6, "f{4}{1.000.000}", 440, 470, 120)
    pil(c, t, b6, "escala: 1 em cima", 440, 290, 50)
    E.foco(c, t, lerp(b6, c6, 0.5), 0.5, lambda a: E.pilula(c, "÷ 4 nos dois", 900, 360, 46, "g", fundo=TINTA, a=a))
    fcen(c, t, c6, "= f{1}{250.000}", 1320, 470, 120, COR)
    bola_res(c, t, d6, "1 : 250.000", W / 2, 760, 200, 60)
    fcen(c, t, e6, "250.000 × 4 = 1.000.000", W / 2 - 60, 1020, 64, TINTA2)
    E.foco(c, t, e6 + 0.8, 0.5, lambda a: E.selo(c, W / 2 + 400, 1000, 40, True, a))


# ---------------- escala gráfica ----------------
def b_grafica(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10 = C["s10.a"], C["s10.b"]
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12 = C["s12.a"], C["s12.b"]
    E.frase(c, t, a7, ps("a", "i", 80) + [("escala gráfica", "g", 84, COR)], XE, 170, "left", 0.12)
    # tudo o que é desenho do mapa encolhe junto em s12
    k = lerp(1.0, 0.55, ease_io(prog(t, a12, 1.2)))
    ox, oy = XE, 300
    c.save(); c.translate(ox, oy); c.scale(k, k); c.translate(-ox, -oy)
    bx, by = XE + 20, 330
    E.foco(c, t, b7, 0.5, lambda a: barra(c, bx, by, 2, 2 * U, a, ("0", "5", "10 km") if t >= c7 else None, 46))
    if t >= a8 and t < a9 - 0.1:
        E.foco(c, t, a8, 0.5, lambda a: regua(c, bx, by + 120, 4, a))
    if t >= b8:
        trecho(c, t, b8, bx, bx + 2 * U, by - 10, "2 cm")
    # duas cidades a 6 cm
    cy = 700
    if t >= a9:
        E.foco(c, t, a9, 0.5, lambda a: (c.drawCircle(bx, cy, 20, M.paint(E.COR, a)), c.drawCircle(bx + 6 * U, cy, 20, M.paint(E.COR, a)),
                                          M.line(c, bx, cy, bx + 6 * U, cy, TINTA2, a, 4, dash=[14, 10])))
        trecho(c, t, a9 + 0.3, bx, bx + 6 * U, cy - 30, "6 cm", TINTA)
        for i in range(3):
            trecho(c, t, b9 + 0.25 * i, bx + i * 2 * U + 6, bx + (i + 1) * 2 * U - 6, cy + 30, "5 km", E.COR, 40, cima=False)
    # tira de papel com as duas marcas
    if t >= a10:
        q = ease_io(prog(t, b10, 1.0))
        tx, ty = bx, lerp(cy + 170, by + 120, q)
        E.foco(c, t, a10, 0.5, lambda a: (M.rrect(c, tx - 30, ty, 6 * U + 60, 56, 6, "#FFFFFF", a),
                                           c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(tx - 30, ty, 6 * U + 60, 56), 6, 6), M.paint(TINTA2, a, stroke=3)),
                                           M.line(c, tx, ty, tx, ty + 40, E.COR, a, 6), M.line(c, tx + 6 * U, ty, tx + 6 * U, ty + 40, E.COR, a, 6)))
    c.restore()
    # coluna da direita
    xr = 1100

    def explica():
        E.frase(c, t, b7 + 0.3, ps("barrinha no canto,", "i", 52) + [("em trechos", "g", 52, COR)], xr, 330, "left", 0.1)
        E.frase(c, t, c7, ps("distância", "i", 52) + [("real", "g", 52, COR)] + ps("embaixo", "i", 52), xr, 420, "left", 0.1)
        E.frase(c, t, a8, ps("meça um trecho", "i", 52) + [("com a régua", "g", 52)], xr, 540, "left", 0.1)
        fesq(c, t, c8, "2 cm → 5 km", xr, 650, 80, COR)
        fesq(c, t, c9, "3 × 5 = 15 km", xr, 800, 80, CERTO)
    E.saida(c, t, a10 - 0.1, explica)

    def tira():
        E.frase(c, t, a10, ps("marque as cidades", "i", 52) + [("numa tira", "g", 52)], xr, 600, "left", 0.1)
        E.frase(c, t, b10, ps("encoste na barra e", "i", 52) + [("leia", "g", 52, COR)], xr, 700, "left", 0.1)
    if a10 - 0.1 <= t:
        E.saida(c, t, C["s11"] - 0.1, tira)

    def numerica():
        E.frase(c, t, C["s11"] + 0.2, ps("e a escala", "i", 56) + [("numérica?", "g", 56, COR)], xr, 330, "left", 0.1)
        fesq(c, t, a11, "2 cm → 5 km", xr, 460, 76)
        fesq(c, t, b11, "5 km = 500.000 cm", xr, 590, 70)
        fesq(c, t, lerp(b11, c11, 0.6), "500.000 ÷ 2", xr, 710, 70, TINTA2)
        bola_res(c, t, c11, "1 : 250.000", xr + 300, 880, 165, 50)
    if C["s11"] - 0.1 <= t:
        E.saida(c, t, C["s12"] - 0.1, numerica)
    if t >= C["s12"]:
        E.frase(c, t, C["s12"] + 0.2, ps("por que resiste", "i", 56) + [("à cópia?", "g", 56, COR)], xr, 330, "left", 0.1)
        E.frase(c, t, a12, ps("o mapa encolhe,", "i", 52), xr, 460, "left", 0.1)
        E.frase(c, t, a12 + 0.6, [("a barra encolhe junto", "g", 52, COR)], xr, 550, "left", 0.1)
        E.frase(c, t, lerp(a12, b12, 0.5), ps("cidades:", "i", 52) + [("3 trechos", "g", 52)], xr, 680, "left", 0.1)
        bola_res(c, t, b12, "15 km", xr + 200, 860, 110, 60, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, C["s13"] + 0.2, [("cuidado:", "g", 84, ERRADO)] + ps("unidades", "i", 80) + [("diferentes", "g", 84)], W / 2, 190, "center", 0.12)
    E.foco(c, t, a13, 0.5, lambda a: E.pilula(c, "4 cm  para  10 km", W / 2, 330, 60, "g", fundo=TINTA, a=a))

    def errado():
        fcen(c, t, b13, "f{4}{10}", 640, 590, 130, ERRADO)
        fcen(c, t, c13, "→  1 : 2,5", 1180, 590, 120, ERRADO)
        E.frase(c, t, a14, ps("o mapa teria", "i", 64, ERRADO) + [("quase metade", "g", 64, ERRADO)] + ps("da região?!", "i", 64, ERRADO), W / 2, 780, "center", 0.1)
        tr = a14 + 1.6
        if t >= tr:
            E.risco(c, 480, 640, 1460, 470, t, tr, largura=14)
    E.saida(c, t, b14 - 0.1, errado)
    if t < b14 - 0.1:
        return
    E.frase(c, t, b14, ps("escala de mapa tem", "i", 70) + [("um número enorme", "g", 74, COR)] + ps("embaixo", "i", 70), W / 2, 560, "center", 0.1)
    E.frase(c, t, c14, ps("saiu pequeno?", "i", 70) + [("passe tudo para cm", "g", 74, CERTO)], W / 2, 760, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    a16, b16, c16 = C["s16.a"], C["s16.b"], C["s16.c"]

    def regra():
        E.frase(c, t, C["s15"] + 0.3, ps("o atalho", "i", 70, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a15, ps("divida o", "i", 96, CLARO) + [("real", "g", 104, BR)] + ps("pelo", "i", 96, CLARO) + [("desenho", "g", 104, BR)], W / 2, 360, "center", 0.12)
        E.frase(c, t, a15 + 1.2, ps("já em centímetros", "i", 70, CLARO), W / 2, 470, "center", 0.1)
        fcen(c, t, b15, "1.000.000 ÷ 4 = 250.000", W / 2, 680, 110, BR)
        E.foco(c, t, c15, 0.5, lambda a: E.pilula(c, "1 : 250.000 direto", W / 2, 870, 70, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s16"] - 0.1, regra)
    if t < C["s16"]:
        return
    E.frase(c, t, a16, ps("é a simplificação que deixa", "i", 70, CLARO) + [("o 1 em cima", "g", 74, BR)], W / 2, 230, "center", 0.1)
    E.foco(c, t, a16 + 1.0, 0.5, lambda a: E.formula(c, "f{4 ÷ 4}{1.000.000 ÷ 4} = f{1}{250.000}", W / 2, 470, 100, "g", BR, a, "center"))
    E.foco(c, t, b16, 0.5, lambda a: E.selo(c, 330, 720, 46, False, a))
    E.frase(c, t, b16 + 0.1, ps("só uma distância, e o mapa tem", "i", 62, CLARO) + [("a barra?", "g", 66, BR)], 410, 745, "left", 0.1)
    E.frase(c, t, c16, [("conte os trechos", "g", 90, BR)], W / 2, 920, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s17.a"], ps("escala gráfica:", "i", 76) + [("3 cm → 6 km", "g", 80, COR)], XE, 380, passo=0.1)
    E.foco(c, t, C["s17.a"] + 0.4, 0.5, lambda a: barra(c, XE + 10, 450, 2, 3 * 60, a, ("0", "6", "12 km"), 40))
    E.frase(c, t, C["s17.b"], ps("qual é a", "i", 80) + [("escala numérica?", "g", 80, COR)], XE, 700, passo=0.1)
    E.frase(c, t, C["s17.c"], [("9 cm", "g", 80)] + ps("no mapa valem", "i", 80) + [("quantos km?", "g", 80, COR)], XE, 840, passo=0.1)
    E.relogio(c, t, C["s18.a"], 1570, 440, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    a20, b20, c20, d20 = (C[f"s20.{k}"] for k in "abcd")
    fesq(c, t, a19, "6 km = 600.000 cm", XE, 230, 84)
    fesq(c, t, b19, "600.000 ÷ 3 = 200.000", XE, 370, 84)
    bola_res(c, t, c19, "1 : 200.000", 1500, 300, 180, 50)
    # nove centímetros: três trechos de três
    x0, y0, u = XE + 10, 560, 110
    E.foco(c, t, a20, 0.5, lambda a: barra(c, x0, y0, 3, 3 * u, a, None, 40, 22))
    for i in range(3):
        trecho(c, t, a20 + 0.3 * i, x0 + i * 3 * u + 6, x0 + (i + 1) * 3 * u - 6, y0 + 40, "6 km", E.COR, 44, cima=False)
    E.foco(c, t, a20, 0.5, lambda a: centro(c, "9 cm = 3 trechos de 3 cm", x0 + 4.5 * u, y0 - 40, 50, "b", TINTA2, a))
    fesq(c, t, b20, "3 × 6 = 18 km", 1260, 640, 84, CERTO)
    fesq(c, t, c20, "9 × 200.000 = 1.800.000 cm", XE, 900, 76)
    fesq(c, t, d20, "= 18 km", 1260, 900, 84, CERTO)
    E.foco(c, t, d20 + 0.5, 0.5, lambda a: E.selo(c, 1680, 870, 44, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s21.a", "achar a escala:", "cm, e real ÷ desenho"), ("s21.b", "escala gráfica:", "meça a barra, conte os trechos"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 440 + i * 230
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 70) + [(l2, "g", 70, COR)], 320, y, "left", 0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a0, b0 = C["s22.a"], C["s22.b"]
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula, uma", "i", 80) + [("armadilha", "g", 84, ERRADO)], XE, 240, passo=0.12)
    E.frase(c, t, a0, [("área e volume", "g", 120, COR)], XE, 400)
    E.frase(c, t, a0 + 0.8, ps("numa planta ou maquete", "i", 76), XE, 510, passo=0.1)
    E.frase(c, t, b0, ps("aplicar a escala direto", "i", 70) + [("dá errado", "g", 74, ERRADO)], XE, 640, passo=0.1)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(970, 785, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, achar=b_achar, grafica=b_grafica, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
