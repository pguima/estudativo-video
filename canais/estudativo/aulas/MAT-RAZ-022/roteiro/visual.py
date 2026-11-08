"""Visual — Estudativo · MAT-RAZ-022: escala ao quadrado, escala ao cubo.
Peças locais: sala() é o retângulo da planta com a grade de centímetros quadrados (cada quadradinho vira 1 m² na escala 1:100);
lago() é a forma torta de área dada; o cubo da maquete usa E.cubo. Todo instante vem de C[...]."""
import math
from decimal import Decimal as D

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-022_escala_ao_quadrado_escala_ao_cubo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("area", "volume", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 20 * 100 == 2000 and D(2000) / 10000 == D("0.2") and 5 * 4 == 20
assert 100 * 100 == 10000 and 20 * 10000 == 200000 and 200000 // 10000 == 20
assert 2 ** 3 == 8 and 2 * 50 == 100 and 50 ** 3 == 125000 and 8 * 125000 == 1000000 and 50 ** 2 == 2500
assert 8 * 50 == 400 and D(400) / 1000 == D("0.4")
assert 1000 * 1000 == 1000000 and 6 * 1000000 == 6000000 and 6000000 // 10000 == 600 and 1000 // 100 == 10 and 10 * 10 == 100 and 6 * 100 == 600


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


def sala(c, x, y, cols, lins, u, a=1.0, grade=1.0, pinta=0.0, cor=None):
    """retângulo da planta: cols × lins quadradinhos de u px; grade = linhas internas 0..1; pinta = quantos quadradinhos acesos (0..1)"""
    if a <= 0:
        return
    cor = cor or E.COR
    w, h = cols * u, lins * u
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint("#FFFFFF", a * 0.9))
    n = cols * lins
    for k in range(int(n * pinta + 0.999)):
        i, j = k % cols, k // cols
        q = min(1.0, n * pinta - k)
        c.drawRect(skia.Rect.MakeXYWH(x + i * u + 3, y + j * u + 3, u - 6, u - 6), M.paint(cor, a * 0.85 * q))
    if grade > 0:
        for i in range(1, cols):
            M.line(c, x + i * u, y, x + i * u, y + h * grade, FIO, a, 3)
        for j in range(1, lins):
            M.line(c, x, y + j * u, x + w * grade, y + j * u, FIO, a, 3)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, a, stroke=6))


def lago(c, cx, cy, r, a=1.0, cor=None, escuro=False):
    """forma torta (de área conhecida, mas sem lados para medir)"""
    if a <= 0:
        return
    p = skia.Path()
    pts = []
    for k in range(9):
        ang = k / 9 * 2 * math.pi
        rr = r * (1 + 0.22 * math.sin(3 * ang + 0.7) + 0.12 * math.cos(5 * ang))
        pts.append((cx + rr * math.cos(ang), cy + rr * 0.72 * math.sin(ang)))
    p.moveTo(*pts[0])
    for k in range(9):
        x0, y0 = pts[k]; x1, y1 = pts[(k + 1) % 9]
        p.quadTo(x0 + (x1 - x0) * 0.5 + (y1 - y0) * 0.15, y0 + (y1 - y0) * 0.5 - (x1 - x0) * 0.15, x1, y1)
    p.close()
    c.drawPath(p, M.paint(cor or E.COR, a * 0.35))
    c.drawPath(p, M.paint(BR if escuro else TINTA, a, stroke=5))


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
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")
    a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]

    def um():
        E.foco(c, t, a1, 0.5, lambda a: E.pilula(c, "planta 1 : 100", 420, 200, 60, "g", a=a, cor=E.SOBRE))
        E.foco(c, t, b1, 0.6, lambda a: sala(c, 220, 320, 5, 4, 80, a, pinta=ep(t, b1 + 0.3, 1.2)))
        E.foco(c, t, b1 + 0.6, 0.4, lambda a: centro(c, "20 cm²", 420, 720, 80, "g", COR, a))
        fesq(c, t, c1, "20 × 100 = 2.000 cm²", 860, 400, 84, ERRADO)
        fesq(c, t, d1, "= 0,2 m²?", 860, 560, 110, ERRADO)
        E.frase(c, t, lerp(d1, C["s01.end"], 0.4), ps("menor que o tampo", "i", 64, ERRADO) + [("de uma mesa!", "g", 64, ERRADO)], 860, 690, "left", 0.1)
        if t >= a2 - 0.4:
            E.risco(c, 840, 590, 1500, 330, t, a2 - 0.4, largura=14)
            fesq(c, t, a2, "sala de verdade: 20 m²", 860, 880, 84, CERTO)
    E.saida(c, t, b2 - 0.1, um)
    if t >= b2 - 0.1:
        E.foco(c, t, c2 - 0.2, 0.7, lambda a: E.bola(c, 1450, 540, 280 * ease_back(prog(t, c2 - 0.2, 0.7))), blur=0)
        E.frase(c, t, b2, ps("até o fim da aula", "i", 92), XE, 330, passo=0.14)
        E.frase(c, t, b2 + 0.8, [("área", "g", 120, COR), ("e", "i", 110), ("volume", "g", 120, COR)], XE, 490, passo=0.14)
        E.frase(c, t, lerp(b2, c2, 0.5), ps("reais, sem cair", "i", 90), XE, 630, passo=0.12)
        E.frase(c, t, lerp(b2, c2, 0.7), ps("nessa armadilha", "i", 90, COR), XE, 750, passo=0.12)
        E.foco(c, t, c2 + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1450, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1450, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "ler", "uma escala"), ("s03.c", "dobrar o lado do quadrado", "quadruplica a área"),
                              ("s03.d", "converter", "m² e m³")))


# ---------------- área ----------------
def b_area(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8 = C["s08.a"], C["s08.b"]
    u, x0, y0 = 80, 200, 300
    E.foco(c, t, C["s04"] + 0.2, 0.5, lambda a: E.pilula(c, "planta 1 : 100", 400, 170, 54, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, a4, 0.6, lambda a: sala(c, x0, y0, 5, 4, u, a, grade=ep(t, a4 + 0.4, 0.8), pinta=ep(t, a8, 1.5)))
    real = ep(t, b5, 0.4)
    E.foco(c, t, a4 + 0.3, 0.4, lambda a: (centro(c, "5 cm", x0 + 2.5 * u, y0 + 4 * u + 70, 60, "g", TINTA, a * (1 - real)),
                                            E.escreve(c, "4 cm", x0 - 150, y0 + 2 * u + 20, 60, "g", TINTA, a * (1 - ep(t, c5, 0.4)))))
    E.foco(c, t, b5, 0.4, lambda a: centro(c, "5 m", x0 + 2.5 * u, y0 + 4 * u + 70, 60, "g", E.COR, a))
    E.foco(c, t, c5, 0.4, lambda a: E.escreve(c, "4 m", x0 - 130, y0 + 2 * u + 20, 60, "g", E.COR, a))
    xr = 820

    def papel():
        fesq(c, t, b4, "área = lado × lado", xr, 360, 72, TINTA2)
        fesq(c, t, c4, "5 × 4 = 20 cm²", xr, 480, 90)
        pil(c, t, a5, "lados para o real primeiro", xr + 420, 620, 52)
        fesq(c, t, lerp(a5, b5, 0.5), "1 : 100 → 1 cm vale 1 m", xr, 750, 64, TINTA2)
        fesq(c, t, d5, "5 × 4 = 20 m²", xr, 900, 100, CERTO)
    E.saida(c, t, C["s06"] - 0.1, papel)
    if C["s06"] - 0.1 <= t < C["s08"] - 0.1:
        def porque():
            E.frase(c, t, C["s06"] + 0.2, ps("por que × 100", "i", 64) + [("deu errado?", "g", 64, ERRADO)], xr, 270, "left", 0.1)
            fesq(c, t, a6, "cada lado: × 100", xr, 400, 76)
            fesq(c, t, b6, "área: × 100 × 100", xr, 520, 76)
            fesq(c, t, c6, "= × 10.000", xr + 220, 640, 90, COR)
            E.frase(c, t, lerp(c6, C["s06.end"], 0.3), ps("como no quadrado:", "i", 54, TINTA2) + [("lado × 2, área × 4", "g", 54, TINTA2)], xr, 760, "left", 0.08)
        E.saida(c, t, C["s07"] - 0.1, porque)
        if t >= C["s07"] - 0.1:
            fesq(c, t, a7, "20 × 10.000 = 200.000 cm²", xr, 400, 72)
            fesq(c, t, lerp(a7, b7, 0.55), "1 m² = 10.000 cm²", xr, 520, 64, TINTA2)
            fesq(c, t, b7, "= 20 m²", xr, 650, 96, CERTO)
            pil(c, t, c7, "área: escala ao quadrado", xr + 400, 820, 60)
    if t >= C["s08"] - 0.1:
        E.frase(c, t, C["s08"] + 0.2, ps("na escala", "i", 70) + [("1 : 100", "g", 74, COR)], xr, 360, "left", 0.1)
        fesq(c, t, a8, "1 cm² no papel = 1 m² real", xr, 520, 64)
        fesq(c, t, b8, "20 cm² → 20 m²", xr, 690, 100, COR)


# ---------------- volume ----------------
def b_volume(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a10, b10, c10, d10 = (C[f"s10.{k}"] for k in "abcd")
    a11, b11, c11, d11, e11 = (C[f"s11.{k}"] for k in "abcde")
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    E.foco(c, t, a9, 0.5, lambda a: E.pilula(c, "maquete 1 : 50", 400, 170, 54, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s12"] - 0.1, lambda: E.cubo(c, t, b9, 230, 700, 300, "2 cm", todas=True, tm=b9 + 0.8))
    xr = 820

    def maquete():
        fesq(c, t, c9, "V = comprimento × largura × altura", xr, 330, 54, TINTA2)
        fesq(c, t, d9, "2 × 2 × 2 = 8 cm³", xr, 450, 90)
        pil(c, t, a10, "os lados primeiro", xr + 300, 580, 52)
        fesq(c, t, b10, "2 cm × 50 = 100 cm = 1 m", xr, 710, 70)
        fesq(c, t, c10, "1 m³", xr, 860, 100, CERTO)
        fesq(c, t, d10, "= 1.000 L", xr + 260, 860, 100, CERTO)
    E.saida(c, t, C["s11"] - 0.1, maquete)
    if C["s11"] - 0.1 <= t:
        def cubo3():
            fesq(c, t, a11, "50 × 50 × 50", xr, 330, 84)
            fesq(c, t, b11, "= 50³ = 125.000", xr, 460, 84, COR)
            fesq(c, t, c11, "8 × 125.000 = 1.000.000 cm³", xr, 610, 70)
            fesq(c, t, d11, "= 1 m³", xr, 740, 96, CERTO)
            pil(c, t, e11, "volume: escala ao cubo", xr + 380, 900, 60)
        E.saida(c, t, C["s12"] - 0.1, cubo3)
    if t >= C["s12"] - 0.1:
        E.frase(c, t, C["s12"] + 0.2, ps("na mesma maquete, fica menor:", "i", 70), W / 2, 320, "center", 0.1)
        linhas = ((a12, "altura", "50 vezes", "50"), (b12, "área", "2.500 vezes", "50²"), (c12, "volume", "125.000 vezes", "50³"))
        for i, (ti, l1, l2, l3) in enumerate(linhas):
            y = 500 + i * 170
            E.foco(c, t, ti, 0.5, lambda a, l1=l1, l2=l2, l3=l3, y=y: (E.escreve(c, l1, 400, y, 76, "i", TINTA, a),
                                                                       E.escreve(c, l2, 720, y, 84, "g", E.COR, a),
                                                                       E.pilula(c, l3, 1560, y - 26, 56, "g", fundo=TINTA, a=a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, C["s13"] + 0.2, [("cuidado:", "g", 84, ERRADO)] + ps("o mesmo erro no volume", "i", 80), W / 2, 190, "center", 0.12)

    def errado():
        fcen(c, t, a13, "8 × 50", 560, 420, 110, ERRADO)
        fcen(c, t, b13, "= 400 cm³", 1100, 420, 110, ERRADO)
        fcen(c, t, c13, "= 0,4 L", W / 2, 600, 110, ERRADO)
        E.frase(c, t, c13 + 0.6, ps("uma caixa-d'água", "i", 66, ERRADO) + [("num copo grande?", "g", 66, ERRADO)], W / 2, 740, "center", 0.1)
        tr = lerp(c13, C["s13.end"], 0.7)
        if t >= tr:
            E.risco(c, 420, 450, 1500, 330, t, tr, largura=14)
    E.saida(c, t, a14 - 0.1, errado)
    if t < a14 - 0.1:
        return
    itens = ((a14, "comprimento", "escala direta", "× 50"), (b14, "área", "ao quadrado", "× 50²"), (c14, "volume", "ao cubo", "× 50³"))
    for i, (ti, l1, l2, l3) in enumerate(itens):
        y = 420 + i * 190
        E.foco(c, t, ti, 0.5, lambda a, l1=l1, l2=l2, l3=l3, y=y, i=i: (E.bola(c, 330, y - 30, 52, a=a), centro(c, str(i + 1), 330, y - 8, 60, "g", E.SOBRE, a),
                                                                         E.escreve(c, l1, 420, y, 80, "i", TINTA, a),
                                                                         E.escreve(c, l2, 900, y, 84, "g", E.COR, a),
                                                                         E.pilula(c, l3, 1560, y - 26, 54, "g", fundo=TINTA, a=a)))
    E.foco(c, t, a14 + 0.6, 0.4, lambda a: E.escreve(c, "lado, altura, distância", 420, 480, 46, "i", TINTA2, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a15, b15 = C["s15.a"], C["s15.b"]
    a16, b16, c16 = C["s16.a"], C["s16.b"], C["s16.c"]

    def regra():
        E.frase(c, t, C["s15"] + 0.3, ps("o atalho", "i", 70, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a15, ps("converta os", "i", 100, CLARO) + [("lados,", "g", 110, BR)], W / 2, 340, "center", 0.12)
        E.frase(c, t, a15 + 1.0, ps("não a", "i", 100, CLARO) + [("área", "g", 110, BR)], W / 2, 470, "center", 0.12)
        fcen(c, t, lerp(a15, b15, 0.45), "desenho → real → multiplique", W / 2, 670, 84, CLARO)
        E.frase(c, t, b15, ps("sem quadrado nem cubo", "i", 80, CLARO) + [("para esquecer", "g", 84, BR)], W / 2, 860, "center", 0.12)
    E.saida(c, t, C["s16"] - 0.1, regra)
    if t < C["s16"]:
        return
    E.frase(c, t, a16, ps("lado é comprimento:", "i", 76, CLARO) + [("escala direta", "g", 80, BR)], W / 2, 220, "center", 0.12)
    E.foco(c, t, b16, 0.5, lambda a: E.selo(c, 260, 450, 46, False, a))
    E.frase(c, t, b16 + 0.1, ps("só a área do desenho,", "i", 66, CLARO) + [("forma torta", "g", 70, BR)], 340, 475, "left", 0.1)
    E.foco(c, t, b16 + 0.4, 0.6, lambda a: lago(c, 1500, 620, 200, a, escuro=True))
    E.frase(c, t, c16, ps("aí,", "i", 84, CLARO) + [("× escala²", "g", 96, BR)], W / 2 - 300, 800, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s17.a"] - 0.8, ps("planta", "i", 84), XE, 380, passo=0.1)
    E.foco(c, t, C["s17.a"], 0.5, lambda a: E.escreve(c, "1 : 1.000", XE + 280, 385, 100, "g", COR, a))
    E.frase(c, t, C["s17.b"] - 1.0, ps("terreno irregular:", "i", 84), XE, 540, passo=0.1)
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.escreve(c, "6 cm²", XE + 680, 545, 100, "g", TINTA, a))
    E.foco(c, t, C["s17.b"] - 0.8, 0.6, lambda a: lago(c, 1150, 760, 120, a))
    E.frase(c, t, C["s17.c"], ps("área real", "i", 92) + [("em m²?", "g", 96, COR)], XE, 820, passo=0.12)
    E.relogio(c, t, C["s18.a"], 1570, 440, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    a20, b20, c20 = C["s20.a"], C["s20.b"], C["s20.c"]
    E.frase(c, t, C["s19"] + 0.2, ps("só temos a área:", "i", 70) + [("escala ao quadrado", "g", 74, COR)], W / 2, 170, "center", 0.1)
    fesq(c, t, a19, "1.000 × 1.000 = 1.000.000", XE, 330, 76)
    fesq(c, t, b19, "6 × 1.000.000 = 6.000.000 cm²", XE, 460, 76)
    fesq(c, t, c19 - 0.6, "÷ 10.000", XE, 590, 76, TINTA2)
    bola_res(c, t, c19, "600 m²", 1560, 450, 150, 66, CERTO)
    E.foco(c, t, C["s20"] + 0.1, 0.5, lambda a: M.line(c, XE, 680, W - XE, 680, FIO, a, 3))
    E.frase(c, t, C["s20"] + 0.3, ps("outro caminho:", "i", 64, TINTA2), XE, 770, "left", 0.1)
    fesq(c, t, a20, "1 cm = 10 m", XE + 460, 775, 72)
    fesq(c, t, b20, "1 cm² = 10 × 10 = 100 m²", XE, 900, 72)
    fesq(c, t, c20, "6 × 100 = 600 m²", 1100, 900, 72, CERTO)
    E.foco(c, t, c20 + 0.6, 0.5, lambda a: E.selo(c, 1730, 875, 44, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s21.a", "comprimento:", "escala direta"), ("s21.b", "área:", "escala ao quadrado"),
                 ("s21.c", "volume:", "escala ao cubo"), ("s21.d", "se der,", "converta os lados primeiro"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 330 + i * 175
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 52, a=a), centro(c, str(i + 1), 230, y - 8, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 72) + [(l2, "g", 72, COR)], 320, y, "left", 0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a0, b0 = C["s22.a"], C["s22.b"]
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, a0, [("praticando", "g", 130, COR)], XE, 400)
    E.frase(c, t, b0, ps("distâncias, áreas e volumes", "b", 64), XE, 520, passo=0.1)
    E.frase(c, t, b0 + 1.0, ps("em plantas, mapas e maquetes", "i", 64), XE, 610, passo=0.1)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(970, 785, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, area=b_area, volume=b_volume, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
