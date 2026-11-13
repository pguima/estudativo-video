"""Visual — Estudativo · QUI-SOL-007: praticando concentração e diluição (aula de prática, cinco questões).

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a da trilha Soluções (cabeçalho de
QUI-SOL-001/roteiro/visual.py). Cada questão: número na esfera, enunciado à esquerda, desenho à direita; na pausa, o relógio
toma o lugar do desenho. Resolução: contas em linhas, resultado na esfera verde, erro comum em vermelho com risco.
Todo instante vem de C[...]."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Soluções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-SOL-007_praticando_concentracao_diluicao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"
ROSA = "#F06292"
BASE = "#DCEFF7"
KNO3 = [(0, 13), (10, 21), (20, 32), (30, 46), (40, 64), (50, 85), (60, 110), (70, 138), (80, 169)]

# as contas da aula
assert dict(KNO3)[60] / 2 == 55 and 60 - 55 == 5
assert 4 * 10 == 40 and round(40 * 0.75, 9) == 30 and round(0.015 * 1000, 9) == 15 and 15 / 5 == 3
assert 4 / 40 == 0.1 and round(0.1 / 0.25, 9) == 0.4 and round(0.4 / 4, 9) == 0.1
assert round(0.5 * 0.2, 9) == 0.1 and round(0.1 * 0.3, 9) == 0.03 and round((0.1 + 0.03) / 0.5, 9) == 0.26 and (0.5 + 0.1) / 2 == 0.3
assert round(0.2 * 15, 9) == 3 and round(3 / (2 * 10), 9) == 0.15 and round(3 / 10, 9) == 0.3


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def rotulo(c, t, t0, s, cx, y, size=48, cor=TINTA2, est="i"):
    E.foco(c, t, t0, 0.4, lambda a: centro(c, s, cx, y, size, est, cor, a))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def cabecalho(c, t, t0, n, tema):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 150, 56, a=a), centro(c, str(n), XE + 50, 176, 70, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, [("questão", "i", 70, TINTA2), (tema, "g", 64, COR)], XE + 130, 175, passo=0.12)


def figura_ou_relogio(c, t, C, cena_pausa, fn):
    """o desenho da questão até a pausa; na pausa, o relógio no lugar"""
    if t < C[cena_pausa]:
        fn()
    else:
        E.relogio(c, t, C[cena_pausa + ".a"], cx=1470, cy=540, r=220)


def bureta(c, x, ytop, h, nivel, cor=BASE, a=1.0):
    """bureta graduada com torneira (a mesma da QUI-SOL-006)"""
    if a <= 0:
        return
    w, vidro, yb = 56, Q.VIDRO, ytop + h
    M.rrect(c, x - w / 2, ytop, w, h, 10, "#FFFFFF", 0.5 * a)
    hl = (h - 20) * nivel
    M.rrect(c, x - w / 2 + 6, yb - 10 - hl, w - 12, hl, 6, cor, 0.95 * a)
    for k in range(1, 10):
        M.line(c, x - w / 2 + 6, ytop + h * k / 10, x - w / 2 + (24 if k % 2 else 32), ytop + h * k / 10, vidro, 0.7 * a, 2.5)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w / 2, ytop, w, h), 10, 10), M.paint(vidro, a, stroke=4))
    M.rrect(c, x - 10, yb, 20, 40, 4, vidro, a)
    M.rrect(c, x - 9, yb - 24, 18, 92, 9, E.COR, a)
    p = skia.Path(); p.moveTo(x - 8, yb + 40); p.lineTo(x - 3, yb + 90); p.lineTo(x + 3, yb + 90); p.lineTo(x + 8, yb + 40); p.close()
    c.drawPath(p, M.paint(vidro, a))


def garrafa(c, cx, yb, w, h, rot, cor="#E8D9B0", a=1.0):
    """garrafa de vinagre com o rótulo"""
    if a <= 0:
        return
    pth = skia.Path()
    pth.moveTo(cx - w * 0.16, yb - h); pth.lineTo(cx - w * 0.16, yb - h * 0.72); pth.quadTo(cx - w / 2, yb - h * 0.62, cx - w / 2, yb - h * 0.45)
    pth.lineTo(cx - w / 2, yb - 20); pth.quadTo(cx - w / 2, yb, cx - w / 2 + 20, yb); pth.lineTo(cx + w / 2 - 20, yb); pth.quadTo(cx + w / 2, yb, cx + w / 2, yb - 20)
    pth.lineTo(cx + w / 2, yb - h * 0.45); pth.quadTo(cx + w / 2, yb - h * 0.62, cx + w * 0.16, yb - h * 0.72); pth.lineTo(cx + w * 0.16, yb - h); pth.close()
    c.drawPath(pth, M.paint(cor, 0.9 * a))
    c.drawPath(pth, M.paint(Q.VIDRO, a, stroke=4))
    M.rrect(c, cx - w * 0.18, yb - h - 30, w * 0.36, 34, 8, E.COR, a)
    M.rrect(c, cx - w * 0.42, yb - h * 0.42, w * 0.84, h * 0.28, 12, BR, a)
    centro(c, rot, cx, yb - h * 0.24, h * 0.09, "g", COR, a)


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 150, COR), ("questões", "i", 120)], XE, 330, passo=0.15)
    for k, (ti, s) in enumerate(((C["s01.b"], "curva"), (C["s01.b"] + 0.6, "rótulo e laudo"), (C["s01.c"], "diluição"),
                                 (C["s01.c"] + 0.7, "mistura"), (C["s01.c"] + 1.3, "titulação"))):
        E.foco(c, t, ti, 0.4, lambda a, k=k: (E.bola(c, XE + 40, 474 + 100 * k, 34, a=a), centro(c, str(k + 1), XE + 40, 492 + 100 * k, 44, "g", BR, a)))
        E.frase(c, t, ti + 0.1, [(s, "g", 60)], XE + 100, 500 + 100 * k)
    E.foco(c, t, C["s01.d"], 0.8, lambda a: E.simbolo(c, 1500, 600, 260 * a, giro=8 * math.sin(t * 0.4)), blur=0)
    pilula_em(c, t, C["s01.d"] + 0.4, "pause, tente, confira", 1500, 950, 50, E.COR)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("a caixa de ferramentas", "i", 70, TINTA2), XE, 160, passo=0.12)
    itens = ((C["s02.a"], "C = f{m}{V}", "g/L, V em litros"), (C["s02.b"], "% × 10 = g/L", "rótulo"),
             (C["s02.c"], "ppm = mg/L", "na água"), (C["s02.d"], "f{g/L}{massa molar} = mol/L", "mol por litro"),
             (C["s03.a"], "C₁V₁ = C₂V₂", "diluição"), (C["s03.b"], "some os mols", "mistura"),
             (C["s03.c"], "H · M · V = OH · M · V", "titulação"))
    for k, (ti, f, sub) in enumerate(itens):
        col, lin = k // 4, k % 4
        x, y = XE + col * 880, 320 + lin * 200
        E.formula_em(c, t, ti, f, x, y, 66, "g", TINTA)
        rotulo(c, t, ti + 0.3, sub, x + 220, y + (100 if "f{" in f else 62), 40, COR, "b")


# ---------------- questão 1: curva ----------------
def b_q1(c, t, C, b):
    cabecalho(c, t, C["s04"], 1, "curva")
    E.frase(c, t, C["s04.a"], ps("a", "i", 60) + [("60 °C,", "g", 56)] + ps("100 g de água dissolvem até", "i", 60), XE, 320, passo=0.08)
    E.frase(c, t, C["s04.a"] + 1.8, [("110 g", "g", 58, COR)] + ps("de nitrato de potássio", "i", 60), XE, 400, passo=0.08)
    E.frase(c, t, C["s04.b"], ps("você põe", "i", 60) + [("60 g", "g", 58, COR)] + ps("em", "i", 60) + [("50 g", "g", 58, COR)] + ps("de água", "i", 60), XE, 540, passo=0.08)
    E.frase(c, t, C["s04.c"], ps("saturada?", "i", 62), XE, 680, passo=0.1)
    E.frase(c, t, C["s04.d"], ps("sobra sal no fundo? quanto?", "i", 62), XE, 780, passo=0.1)

    def fig():
        P = Q.solubilidade(c, t, C["s04.a"] - 0.2, 1220, 300, 560, 520, [dict(nome="KNO3", pts=KNO3)], tmax=80, smax=180, d=0.8, passo=20, passo_y=40, size=30)
        if t >= C["s04.a"] + 1.0:
            q = ease_io(prog(t, C["s04.a"] + 1.0, 0.6))
            M.line(c, P.x(60), P.y(0), P.x(60), lerp(P.y(0), P.y(110), q), E.COR, 1, 4, dash=[12, 10])
            M.line(c, P.x(60), P.y(110), lerp(P.x(60), P.x(0), ease_io(prog(t, C["s04.a"] + 1.6, 0.6))), P.y(110), E.COR, 1, 4, dash=[12, 10])
    figura_ou_relogio(c, t, C, "s05", fig)


def b_r1(c, t, C, b):
    cabecalho(c, t, C["s06"] - 0.3, 1, "resolvendo")
    E.formula_em(c, t, C["s06.a"], "50 g de água = metade de 100 g", XE, 330, 64, "g", TINTA2)
    E.formula_em(c, t, C["s06.b"], "110 ÷ 2 = 55 g", XE, 460, 86, "g", TINTA)
    E.formula_em(c, t, C["s06.c"], "60 > 55", XE, 590, 86, "g", COR)
    E.frase(c, t, C["s06.d"], ps("saturada com", "i", 60) + [("corpo de fundo", "g", 56, COR)], XE, 700, passo=0.1)
    E.formula_em(c, t, C["s06.e"], "60 − 55 =", XE, 850, 86, "g", TINTA2)
    bola_txt(c, t, C["s06.e"] + 1.4, "5 g", XE + 560, 822, 85, 60, CERTO)
    E.foco(c, t, C["s07.a"], 0.5, lambda a: (E.formula(c, "60 < 110: insaturada", 1180, 520, 62, "g", ERRADO, a),
                                             E.escreve(c, "a curva vale para 100 g de água", 1180, 610, 44, "b", ERRADO, a)))
    if t >= C["s07.b"] + 0.3:
        E.risco(c, 1160, 545, 1820, 470, t, C["s07.b"] + 0.3, largura=10)


# ---------------- questão 2: rótulo e laudo ----------------
def b_q2(c, t, C, b):
    cabecalho(c, t, C["s08"], 2, "rótulo e laudo")
    E.frase(c, t, C["s08.a"], ps("rótulo do vinagre:", "i", 60, TINTA2), XE, 310, passo=0.1)
    E.frase(c, t, C["s08.b"], [("acidez 4%", "g", 62, COR), ("(m/v)", "b", 48, TINTA2)], XE, 400, passo=0.12)
    E.frase(c, t, C["s08.c"], [("A", "g", 56, COR)] + ps("gramas de ácido em", "i", 60) + [("750 mL?", "g", 56, COR)], XE, 500, passo=0.1)
    E.frase(c, t, C["s08.d"], ps("laudo da água de rio:", "i", 60, TINTA2), XE, 660, passo=0.1)
    E.frase(c, t, C["s08.e"], [("0,015 g", "g", 58, COR)] + ps("de chumbo em", "i", 60) + [("5 L", "g", 58, COR)], XE, 750, passo=0.1)
    E.frase(c, t, C["s08.f"], [("B", "g", 56, COR)] + ps("quantos", "i", 60) + [("ppm?", "g", 56, COR)], XE, 850, passo=0.1)

    def fig():
        E.foco(c, t, C["s08.a"], 0.5, lambda a: garrafa(c, 1350, 900, 260, 560, "4%", a=a))
        Q.bequer(c, t, C["s08.d"], 1680, 900, 240, 280, 0.7, "#C9D9C0", graduacao=False)
        rotulo(c, t, C["s08.d"] + 0.3, "5 L de água de rio", 1680, 970, 40, TINTA, "b")
    figura_ou_relogio(c, t, C, "s09", fig)


def b_r2(c, t, C, b):
    cabecalho(c, t, C["s10"] - 0.3, 2, "resolvendo")
    E.formula_em(c, t, C["s10.a"], "A   4% × 10 = 40 g/L", XE, 330, 72, "g", TINTA)
    E.formula_em(c, t, C["s10.b"], "750 mL = 0,75 L", XE + 80, 440, 66, "g", TINTA2)
    E.formula_em(c, t, C["s10.c"], "40 × 0,75 =", XE + 80, 560, 72, "g", TINTA2)
    bola_txt(c, t, C["s10.c"] + 1.4, "30 g", XE + 640, 535, 85, 54, CERTO)
    E.formula_em(c, t, C["s11.a"], "B   ppm pede mg", XE, 720, 72, "g", TINTA)
    E.formula_em(c, t, C["s11.b"], "0,015 g × 1000 = 15 mg", XE + 80, 820, 66, "g", TINTA2)
    E.formula_em(c, t, C["s11.c"], "15 ÷ 5 = 3 mg/L", XE + 80, 930, 66, "g", TINTA2)
    bola_txt(c, t, C["s11.d"], "3 ppm", 1500, 880, 100, 54, CERTO)


# ---------------- questão 3: mol/L e diluição ----------------
def b_q3(c, t, C, b):
    cabecalho(c, t, C["s12"], 3, "mol/L e diluição")
    E.frase(c, t, C["s12.a"], [("4 g", "g", 58, COR)] + ps("de soda cáustica em", "i", 60) + [("250 mL", "g", 58, COR)], XE, 320, passo=0.1)
    E.foco(c, t, C["s12.a"] + 1.4, 0.4, lambda a: Q.formula(c, "NaOH", XE, 410, 60, TINTA2, a))
    E.frase(c, t, C["s12.b"], ps("massa molar:", "i", 60) + [("40 g/mol", "g", 58)], XE, 510, passo=0.1)
    E.frase(c, t, C["s12.c"], [("A", "g", 56, COR)] + ps("concentração em", "i", 60) + [("mol/L?", "g", 56, COR)], XE, 630, passo=0.1)
    E.frase(c, t, C["s12.d"], ps("diluída até", "i", 60) + [("1 L", "g", 58, COR)], XE, 760, passo=0.1)
    E.frase(c, t, C["s12.e"], [("B", "g", 56, COR)] + ps("nova concentração?", "i", 60), XE, 860, passo=0.1)

    def fig():
        Q.bequer(c, t, C["s12.a"], 1300, 860, 260, 360, 0.3, Q.AGUA, graduacao=False, particulas=dict(n=14, estado="gas", tipos=[(E.COR, 1.0)], r=8))
        rotulo(c, t, C["s12.a"] + 0.3, "250 mL", 1300, 930, 44, TINTA, "b")
        Q.bequer(c, t, C["s12.d"], 1650, 860, 300, 460, 0.85, Q.AGUA, graduacao=False, particulas=dict(n=14, estado="gas", tipos=[(E.COR, 1.0)], r=8))
        rotulo(c, t, C["s12.d"] + 0.3, "1 L", 1650, 930, 44, TINTA, "b")
    figura_ou_relogio(c, t, C, "s13", fig)


def b_r3(c, t, C, b):
    cabecalho(c, t, C["s14"] - 0.3, 3, "resolvendo")
    E.formula_em(c, t, C["s14.a"], "A   4 ÷ 40 = 0,1 mol", XE, 330, 72, "g", TINTA)
    E.formula_em(c, t, C["s14.b"], "250 mL = 0,25 L", XE + 80, 440, 66, "g", TINTA2)
    E.formula_em(c, t, C["s14.c"], "f{0,1}{0,25} =", XE + 80, 580, 72, "g", TINTA2)
    bola_txt(c, t, C["s14.c"] + 1.8, "0,4 mol/L", XE + 560, 555, 105, 40, CERTO)
    E.formula_em(c, t, C["s15.a"], "B   250 mL → 1 L: × 4", XE, 760, 72, "g", TINTA)
    E.formula_em(c, t, C["s15.b"], "0,4 ÷ 4 =", XE + 80, 890, 72, "g", TINTA2)
    bola_txt(c, t, C["s15.b"] + 1.4, "0,1 mol/L", XE + 560, 865, 105, 40, CERTO)


# ---------------- questão 4: mistura ----------------
def b_q4(c, t, C, b):
    cabecalho(c, t, C["s16"], 4, "mistura")
    E.frase(c, t, C["s16.a"], [("200 mL", "g", 58, COR)] + ps("de soda com", "i", 60) + [("0,5 mol/L", "g", 58, COR)], XE, 340, passo=0.1)
    E.frase(c, t, C["s16.b"], [("+ 300 mL", "g", 58, COR)] + ps("de soda com", "i", 60) + [("0,1 mol/L", "g", 58, COR)], XE, 450, passo=0.1)
    E.frase(c, t, C["s16.c"], ps("concentração final?", "i", 64), XE, 620, passo=0.1)

    def fig():
        Q.bequer(c, t, C["s16.a"], 1250, 800, 240, 300, 0.5, Q.AGUA, graduacao=False, particulas=dict(n=20, estado="gas", tipos=[(E.COR, 1.0)], r=8, semente=2))
        rotulo(c, t, C["s16.a"] + 0.3, "0,5 mol/L", 1250, 870, 44, TINTA, "b")
        E.foco(c, t, C["s16.b"] - 0.2, 0.4, lambda a: centro(c, "+", 1450, 700, 100, "g", TINTA2, a))
        Q.bequer(c, t, C["s16.b"], 1660, 800, 260, 340, 0.7, Q.AGUA, graduacao=False, particulas=dict(n=6, estado="gas", tipos=[(E.COR, 1.0)], r=8, semente=3))
        rotulo(c, t, C["s16.b"] + 0.3, "0,1 mol/L", 1660, 870, 44, TINTA, "b")
    figura_ou_relogio(c, t, C, "s17", fig)


def b_r4(c, t, C, b):
    cabecalho(c, t, C["s18"] - 0.3, 4, "resolvendo")
    E.frase(c, t, C["s18"], ps("some os", "i", 60) + [("mols", "g", 58, COR)], XE, 300, passo=0.1)
    E.formula_em(c, t, C["s18.a"], "0,5 × 0,2 = 0,1 mol", XE, 420, 68, "g", TINTA)
    E.formula_em(c, t, C["s18.b"], "0,1 × 0,3 = 0,03 mol", XE, 520, 68, "g", TINTA)
    E.formula_em(c, t, C["s18.c"], "0,13 mol em 0,5 L", XE, 640, 68, "g", COR)
    E.formula_em(c, t, C["s18.d"], "f{0,13}{0,5} =", XE, 800, 72, "g", TINTA2)
    bola_txt(c, t, C["s18.d"] + 1.8, "0,26 mol/L", XE + 520, 775, 110, 38, CERTO)
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, "média: f{0,5 + 0,1}{2} = 0,3", 1150, 470, 60, "g", ERRADO, a))
    if t >= C["s19.a"] + 1.0:
        E.risco(c, 1130, 500, 1830, 400, t, C["s19.a"] + 1.0, largura=10)
    rotulo(c, t, C["s19.b"], "há mais volume da fraca:", 1480, 640, 44, TINTA, "b")
    rotulo(c, t, C["s19.c"], "o resultado fica perto de 0,1", 1480, 710, 44, COR, "b")


# ---------------- questão 5: titulação ----------------
def b_q5(c, t, C, b):
    cabecalho(c, t, C["s20"], 5, "titulação")
    E.frase(c, t, C["s20.a"], [("10 mL", "g", 58, COR)] + ps("de ácido sulfúrico", "i", 60), XE, 340, passo=0.1)
    E.foco(c, t, C["s20.a"] + 1.0, 0.4, lambda a: Q.formula(c, "H2SO4", XE + 640, 340, 64, TINTA, a))
    E.frase(c, t, C["s20.b"], ps("gastaram", "i", 60) + [("15 mL", "g", 58, COR)] + ps("de soda com", "i", 60) + [("0,2 mol/L", "g", 58, COR)], XE, 450, passo=0.1)
    E.frase(c, t, C["s20.c"], ps("até ficar", "i", 60) + [("rosa", "g", 58, ROSA)], XE, 560, passo=0.1)
    E.frase(c, t, C["s20.d"], ps("concentração do ácido?", "i", 64), XE, 720, passo=0.1)

    def fig():
        E.foco(c, t, C["s20.a"], 0.5, lambda a: bureta(c, 1500, 140, 400, 0.6, BASE, a))
        Q.erlenmeyer(c, t, C["s20.a"] + 0.2, 1500, 950, 300, 300, 0.4, Q.muda_cor(t, C["s20.c"], Q.AGUA, ROSA, 0.6))
    figura_ou_relogio(c, t, C, "s21", fig)


def b_r5(c, t, C, b):
    cabecalho(c, t, C["s22"] - 0.3, 5, "resolvendo")
    E.frase(c, t, C["s22.a"], ps("ácido:", "i", 60) + [("2 H", "g", 58, COR)] + ps("· soda:", "i", 60) + [("1 OH", "g", 58, COR)], XE, 310, passo=0.1)
    E.formula_em(c, t, C["s22.b"], "2 · M · 10", XE, 450, 80, "g", COR)
    E.formula_em(c, t, C["s22.c"], "= 1 · 0,2 · 15 = 3", XE + 430, 450, 80, "g", TINTA)
    rotulo(c, t, C["s22.c"] + 1.6, "mL dos dois lados", XE + 470, 540, 42, TINTA2, "b")
    E.formula_em(c, t, C["s22.d"], "20 · M = 3 → M =", XE, 700, 80, "g", TINTA2)
    bola_txt(c, t, C["s22.e"], "0,15 mol/L", XE + 880, 675, 115, 38, CERTO)
    E.foco(c, t, C["s23.a"], 0.5, lambda a: E.formula(c, "sem o 2: f{3}{10} = 0,3", 1150, 900, 60, "g", ERRADO, a))
    if t >= C["s23.b"] + 0.6:
        E.risco(c, 1130, 920, 1720, 840, t, C["s23.b"] + 0.6, largura=10)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s24.a", [("volume", "g", 66), ("em", "i", 70), ("litros", "g", 66, COR)]),
                 ("s24.b", [("a", "i", 70), ("curva", "g", 66), ("para", "i", 70), ("a", "i", 70), ("água", "i", 70), ("da", "i", 70), ("questão", "g", 66, COR)]),
                 ("s24.c", [("some", "i", 70), ("mols,", "g", 66, COR), ("não", "i", 70), ("concentrações", "i", 70)]),
                 ("s24.d", [("conte", "i", 70), ("os", "i", 70), ("H", "g", 66, COR), ("do", "i", 70), ("ácido", "i", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25"], [("próxima", "i", 80), ("aula:", "i", 80), ("assunto", "i", 80), ("novo", "g", 76, COR)], XE, 250, passo=0.12)
    E.frase(c, t, C["s25.a"], ps("montanha:", "i", 70) + [("ferve abaixo de 100 °C", "g", 62, COR)], XE, 420, passo=0.12)
    E.frase(c, t, C["s25.b"], ps("panela de pressão:", "i", 70) + [("acima", "g", 62, COR)], XE, 540, passo=0.12)
    E.foco(c, t, C["s25.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 760, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s25.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 785, p), ep(t, C["s25.c"] + 0.2, 0.4))
    E.frase(c, t, C["s25.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4,
              q5=b_q5, r5=b_r5, fim=b_fim)
