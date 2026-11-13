"""Visual — Estudativo · QUI-SOL-003: concentração em g/L, porcentagem e ppm.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a da trilha Soluções (cabeçalho de
QUI-SOL-001/roteiro/visual.py): fórmula de conta na grotesca, a letra da vez em E.COR_TEXTO, unidade em cinza ao lado,
resultado na esfera. Todo instante vem de C[...]."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Soluções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-SOL-003_concentracao_gl_porcentagem_ppm.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("gl", "por", "ppm", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# as contas da aula
assert 20 / 0.5 == 40 and abs(20 / 500 - 0.04) < 1e-12
assert round(0.9 * 10, 6) == 9 and round(5 * 10, 6) == 50
assert round(9 * 0.25, 6) == 2.25 and 6 / 2 == 3


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


def rotulo(c, t, t0, s, cx, y, size=48, cor=TINTA2):
    E.foco(c, t, t0, 0.4, lambda a: centro(c, s, cx, y, size, "i", cor, a))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def frac_letras(c, x, y, esq, cima, baixo, size, cores=(TINTA, TINTA, TINTA), a=1.0, escuro=False):
    """fórmula 'esq = cima/baixo' com cor própria em cada letra; (x, y) = linha de base do sinal de igual. Candidata ao kit"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA
    E.escreve(c, esq, x, y, size, "g", cores[0], a)
    xe = x + E.larg(esq, "g", size) + size * 0.2
    E.escreve(c, "=", xe, y, size, "g", TINTA2 if not escuro else CLARO, a)
    xf = xe + E.larg("=", "g", size) + size * 0.25
    wf = max(E.larg(cima, "g", size * 0.85), E.larg(baixo, "g", size * 0.85)) + size * 0.3
    centro(c, cima, xf + wf / 2, y - size * 0.48, size * 0.85, "g", cores[1], a)
    centro(c, baixo, xf + wf / 2, y + size * 0.62, size * 0.85, "g", cores[2], a)
    bh = max(5, size * 0.07)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xf, y - size * 0.33, wf, bh), bh / 2, bh / 2), M.paint(tinta, a))


def soro(c, cx, cy, w, h, rot="0,9%", a=1.0):
    """bolsa de soro pendurada, com o rótulo da porcentagem"""
    if a <= 0:
        return
    M.rrect(c, cx - 8, cy - h / 2 - 70, 16, 70, 6, "#9AA0A8", a)
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 40, "#FFFFFF", 0.85 * a, shadow=True)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, cy - h * 0.1), skia.Point(0, cy + h / 2)], [M.hexc("#D8EEF7", a), M.hexc("#A9D6EA", a)]))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + 12, cy - h * 0.15, w - 24, h * 0.65 - 12), 30, 30), p)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 40, 40), M.paint(Q.VIDRO, a, stroke=4))
    M.rrect(c, cx - w * 0.36, cy - h * 0.36, w * 0.72, h * 0.3, 14, E.COR, a)
    centro(c, rot, cx, cy - h * 0.10, h * 0.12, "g", BR, a)
    centro(c, "NaCl", cx, cy - h * 0.27, h * 0.06, "b", BR, a)
    M.rrect(c, cx - 14, cy + h / 2, 28, 60, 8, "#9AA0A8", a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.6, lambda a: soro(c, 1440, 600, 420, 560, "0,9%", a))
        E.frase(c, t, C["s01.a"] + 0.3, ps("no soro fisiológico:", "i", 70, TINTA2), XE, 260, passo=0.12)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.escreve(c, "0,9%", XE, 470, 190, "g", COR, a))
        rotulo(c, t, C["s01.b"] + 1.4, "de cloreto de sódio, o sal de cozinha", XE + 420, 560, 46)
        E.frase(c, t, C["s01.c"], ps("quantos gramas num", "i", 66) + [("litro?", "g", 66, COR)], XE, 720, passo=0.12)
        bola_txt(c, t, C["s01.d"], "9 g", XE + 120, 880, 95, 80)
        E.frase(c, t, C["s01.d"] + 0.8, ps("em dois segundos", "i", 64, TINTA2), XE + 270, 905, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("gramas", "g", 70, COR), ("por", "i", 74), ("litro", "g", 70, COR)]),
                 (C["s02.c"], [("a", "i", 74), ("porcentagem", "g", 70), ("do", "i", 74), ("rótulo", "i", 74)]),
                 (C["s02.d"], [("ppm", "g", 70, COR), ("de", "i", 74), ("um", "i", 74), ("laudo", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 76, TINTA2), XE, 170)
    E.frase(c, t, C["s03.a"], [("soluto", "g", 66, COR), ("+", "g", 66, TINTA2), ("solvente", "g", 66, COR), ("=", "g", 66, TINTA2), ("solução", "g", 66)], XE, 300, passo=0.15)
    for k, (ti, s) in enumerate(((C["s03.b"], "1 L = 1000 mL"), (C["s03.c"], "1 g = 1000 mg"), (C["s03.d"], "5% = 5 em cada 100"))):
        E.foco(c, t, ti, 0.5, lambda a, k=k, s=s: (E.bola(c, XE + 40, 474 + 160 * k, 40, a=a),
                                                   E.formula(c, s, XE + 110, 500 + 160 * k, 90, "g", TINTA, a)))
    Q.bequer(c, t, C["s03.b"], 1520, 860, 360, 420, 0.8, Q.AGUA)
    rotulo(c, t, C["s03.b"] + 0.4, "1 litro", 1520, 940, 52)


# ---------------- concentração comum ----------------
def b_gl(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], ps("concentração:", "i", 70, TINTA2), XE, 220)
            E.frase(c, t, C["s04.a"] + 0.6, ps("quanto soluto há em cada pedaço", "i", 70), XE, 320, passo=0.12)
            E.frase(c, t, C["s04.b"], [("concentração", "g", 100, COR), ("comum", "g", 100, COR)], XE, 520, passo=0.15)
            E.foco(c, t, C["s04.b"] + 1.4, 0.5, lambda a: E.pilula(c, "g/L", XE + 1380, 490, 90, "g", fundo=TINTA, a=a))
            E.frase(c, t, C["s04.c"], ps("gramas de soluto em cada litro de solução", "i", 60), XE, 700, passo=0.1)
            Q.bequer(c, t, C["s04.c"] + 0.5, 1450, 1010, 240, 220, 0.75, Q.AGUA, graduacao=False,
                     particulas=dict(n=28, estado="liquido", tipos=[(E.COR, 1.0)], r=7))
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            cores = (COR if t >= C["s05.b"] else TINTA, COR if t >= C["s05.c"] else TINTA, COR if t >= C["s05.d"] else TINTA)
            E.foco(c, t, C["s05.a"], 0.5, lambda a: frac_letras(c, 260, 520, "C", "m", "V", 200, cores, a))
            linhas = ((C["s05.b"], "C", "concentração", "g/L"), (C["s05.c"], "m", "massa do soluto", "g"), (C["s05.d"], "V", "volume da solução", "L"))
            for k, (ti, l, nome, un) in enumerate(linhas):
                y = 330 + k * 130
                E.foco(c, t, ti, 0.5, lambda a, l=l, y=y: E.escreve(c, l, 1000, y, 80, "g", COR, a))
                E.frase(c, t, ti + 0.2, ps(nome, "i", 64), 1100, y, passo=0.1)
                pilula_em(c, t, ti + 0.7, un, 1700, y - 22, 46, TINTA)
            E.formula_em(c, t, C["s05.e"] - 1.2, "f{20 g}{1 L} =", 260, 880, 80, "g", TINTA2)
            E.foco(c, t, C["s05.e"], 0.5, lambda a: E.escreve(c, "20 g/L", 640, 880, 90, "g", COR, a))
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    if t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06.a"], [("20 g", "g", 76, COR), ("em", "i", 80), ("500 mL", "g", 76, COR)], XE, 220, passo=0.12)
            E.formula_em(c, t, C["s06.b"], "500 mL = 0,5 L", XE, 360, 76, "g", TINTA)
            rotulo(c, t, C["s06.b"] + 1.0, "meio litro", XE + 260, 440, 50)
            Q.bequer(c, t, C["s06.a"] + 0.3, 1060, 860, 260, 300, 0.5, Q.AGUA, particulas=dict(n=20, estado="liquido", tipos=[(E.COR, 1.0)], r=7))
            rotulo(c, t, C["s06.a"] + 0.5, "0,5 L · 20 g", 1060, 940, 46, TINTA)
            E.foco(c, t, C["s06.c"], 0.4, lambda a: E.pilula(c, "× 2", 1290, 720, 56, "g", fundo=E.COR, a=a))
            Q.bequer(c, t, C["s06.c"] + 0.3, 1560, 860, 320, 380, 0.8, Q.AGUA, particulas=dict(n=40, estado="liquido", tipos=[(E.COR, 1.0)], r=7))
            rotulo(c, t, C["s06.c"] + 0.5, "1 L · 40 g", 1560, 940, 46, TINTA)
            E.frase(c, t, C["s06.c"], ps("meio litro tem 20 g:", "i", 60), XE, 600, passo=0.1)
            E.frase(c, t, C["s06.c"] + 1.4, ps("um litro tem o", "i", 60) + [("dobro", "g", 58, COR)], XE, 690, passo=0.1)
            bola_txt(c, t, C["s06.d"], "40 g/L", XE + 190, 850, 110, 62)
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    E.frase(c, t, C["s07.a"], ps("o volume é o da", "i", 76) + [("solução", "g", 72, COR)], XE, 260, passo=0.12)
    E.frase(c, t, C["s07.a"] + 1.3, ps("não o da água", "i", 70, TINTA2), XE, 360, passo=0.12)
    cx, yb, w, h = 1360, 900, 380, 520
    Q.bequer(c, t, C["s07.b"], cx, yb, w, h, lerp(0.35, 0.8, ease_io(prog(t, C["s07.b"] + 1.4, 1.6))), Q.AGUA, graduacao=False,
             particulas=dict(n=36, estado="liquido", tipos=[(E.COR, 1.0)], r=7))
    if t >= C["s07.b"] + 0.4:
        q = ep(t, C["s07.b"] + 0.4, 0.4)
        ym = yb - h * 0.8
        M.line(c, cx - w / 2 - 30, ym, cx + w / 2 + 30, ym, E.COR, q, 5, dash=[14, 10])
        E.escreve(c, "marca de 1 L", cx + w / 2 + 40, ym + 14, 44, "b", COR, q)
    E.frase(c, t, C["s07.b"], ps("dissolva o sal e", "i", 62), XE, 600, passo=0.1)
    E.frase(c, t, C["s07.b"] + 1.0, [("complete", "g", 62, COR)] + ps("até a marca", "i", 62), XE, 700, passo=0.1)


# ---------------- porcentagem ----------------
def b_por(c, t, C, b):
    E.foco(c, t, C["s08"], 0.6, lambda a: soro(c, 300, 560, 300, 400, "0,9%", a))
    E.frase(c, t, C["s08.a"], ps("a porcentagem do soro", "i", 64, TINTA2), 560, 220, passo=0.1)
    E.foco(c, t, C["s08.b"], 0.5, lambda a: (E.formula(c, "0,9%", 560, 380, 110, "g", COR, a), E.formula(c, "=", 860, 380, 110, "g", TINTA2, a)))
    E.frase(c, t, C["s08.b"] + 1.2, [("0,9 g", "g", 72, COR)] + ps("em cada", "i", 72) + [("100 mL", "g", 72)], 990, 380, passo=0.12)
    # dez copinhos de 100 mL = 1 litro
    for k in range(10):
        ti = C["s08.c"] + 0.12 * k
        x = 600 + k * 120
        Q.bequer(c, t, ti, x, 720, 90, 120, 0.7, Q.AGUA, graduacao=False)
        E.foco(c, t, ti + 0.2, 0.3, lambda a, x=x: centro(c, "100 mL", x, 770, 24, "b", TINTA2, a))
    p = ep(t, C["s08.c"] + 1.3, 0.5)
    if p > 0:
        E.chave(c, 545, 1735, 800, E.COR, p, 26)
        E.foco(c, t, C["s08.c"] + 1.5, 0.4, lambda a: centro(c, "1 litro = 10 × 100 mL", 1140, 890, 50, "b", COR, a))
    E.formula_em(c, t, C["s08.d"], "10 × 0,9 =", 600, 1010, 84, "g", TINTA2)
    bola_txt(c, t, C["s08.e"], "9 g/L", 1140, 985, 90, 56)


# ---------------- ppm ----------------
def b_ppm(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("soluto muito pouco, como um poluente", "i", 60, TINTA2), XE, 220, passo=0.1)
        E.frase(c, t, C["s09.a"], [("ppm", "g", 180, COR)], XE, 470)
        E.frase(c, t, C["s09.a"] + 0.6, ps("partes por milhão", "i", 80), XE + 500, 450, passo=0.12)
        E.frase(c, t, C["s09.b"], [("1", "g", 80, COR)] + ps("parte de soluto em", "i", 70) + [("1 000 000", "g", 80, COR)], XE, 680, passo=0.12)
        rotulo(c, t, C["s09.b"] + 1.2, "de partes de solução", XE + 640, 770, 54)
        return
    E.foco(c, t, C["s10.a"], 0.5, lambda a: E.formula(c, "1 L de água ≈ 1 kg = 1 000 000 mg", XE, 260, 72, "g", TINTA, a))
    Q.bequer(c, t, C["s10.a"], 1600, 700, 300, 340, 0.8, Q.AGUA, graduacao=False)
    E.foco(c, t, C["s10.a"] + 0.4, 0.4, lambda a: centro(c, "1 L ≈ 1 kg", 1600, 780, 50, "b", TINTA, a))
    E.frase(c, t, C["s10.b"], [("1 mg", "g", 70, COR), ("em", "i", 74), ("1 L", "g", 70)] + ps("é 1 parte em 1 milhão", "i", 74), XE, 430, passo=0.12)
    E.foco(c, t, C["s10.c"], 0.5, lambda a: (E.formula(c, "1 ppm", XE, 640, 130, "g", COR, a), E.formula(c, "= 1 mg/L", XE + 400, 640, 130, "g", TINTA, a)))
    E.foco(c, t, C["s10.d"], 0.5, lambda a: (E.formula(c, "2 ppm", XE, 830, 110, "g", COR, a), E.formula(c, "= 2 mg/L", XE + 340, 830, 110, "g", TINTA, a)))
    pilula_em(c, t, C["s10.c"] + 0.8, "na água", 1600, 880, 46, E.COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("dividir pelos mililitros", "i", 64), XE + 440, 190, passo=0.1)

    def errado():
        E.formula_em(c, t, C["s11.b"], "f{20}{500} = 0,04 g/L", XE, 430, 110, "g", ERRADO)
        if t >= C["s11.c"] + 0.8:
            E.risco(c, XE - 10, 450, XE + 900, 330, t, C["s11.c"] + 0.8, largura=12)
    errado()
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.a"], ps("bom senso: meio litro tem 20 g", "i", 64), XE, 640, passo=0.1)
    E.frase(c, t, C["s12.b"], ps("e um litro teria só", "i", 64) + [("0,04 g?", "g", 62, ERRADO)], XE, 740, passo=0.1)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.selo(c, 960, 720, 60, False, a))
    E.frase(c, t, C["s12.c"] + 0.8, ps("gramas por litro pedem litros:", "i", 60, TINTA2), XE, 900, passo=0.1)
    bola_txt(c, t, C["s12.d"], "40 g/L", 1400, 880, 100, 56, CERTO)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        def s13():
            E.frase(c, t, C["s13"], ps("o atalho do rótulo", "i", 72, CLARO), W / 2, 170, "center", 0.12)
            E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "% × 10 = g/L", W / 2, 400, 170, "g", BR, a, "center"))
            E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "0,9% → 9 g/L", 560, 620, 90, "g", CLARO, a, "center"))
            E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "5% → 50 g/L", 1360, 620, 90, "g", CLARO, a, "center"))
            E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "na água: ppm = mg/L", W / 2, 860, 100, "g", BR, a, "center"))
        E.saida(c, t, C["s14"] - 0.1, s13)
        return
    E.frase(c, t, C["s14.a"], ps("funciona porque", "i", 64, CLARO) + [("% = gramas em 100 mL", "g", 62, BR)], W / 2, 260, "center", 0.12)
    E.frase(c, t, C["s14.a"] + 1.8, ps("e um litro é dez vezes isso", "i", 64, CLARO), W / 2, 360, "center", 0.1)
    E.frase(c, t, C["s14.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)], W / 2, 560, "center", 0.12)
    pilula_em(c, t, C["s14.b"] + 0.6, "% em massa: liga de metal", 540, 700, 50, E.COR)
    pilula_em(c, t, C["s14.b"] + 2.0, "% em volume: álcool da bebida", 1380, 700, 50, "#3A3B42")
    E.frase(c, t, C["s14.b"] + 3.6, ps("aí ela não conta gramas em cada 100 mL", "i", 58, CLARO), W / 2, 880, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s15.a"], [("250 mL", "g", 60, COR)] + ps("de soro a", "i", 64) + [("0,9%", "g", 60, COR)], XE, 300, passo=0.1)
    E.frase(c, t, C["s15.b"], [("1", "g", 56, COR)] + ps("concentração em g/L?", "i", 60), XE, 400, passo=0.1)
    E.frase(c, t, C["s15.c"], [("2", "g", 56, COR)] + ps("quantos gramas no frasco?", "i", 60), XE, 490, passo=0.1)
    E.frase(c, t, C["s15.d"], ps("laudo:", "i", 64, TINTA2) + [("6 mg", "g", 60, COR)] + ps("de nitrato em", "i", 64) + [("2 L", "g", 60, COR)], XE, 680, passo=0.1)
    E.frase(c, t, C["s15.e"], [("3", "g", 56, COR)] + ps("quantos ppm?", "i", 60), XE, 780, passo=0.1)
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"] + 0.3, 0.6, lambda a: soro(c, 1500, 520, 300, 400, "0,9%", a))
    else:
        E.relogio(c, t, C["s16.a"], cx=1470, cy=520, r=220)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s17"], ps("o soro", "i", 64, TINTA2), XE, 180)
    E.formula_em(c, t, C["s17.a"], "0,9% × 10 = 9 g/L", XE, 300, 80, "g", TINTA)
    E.formula_em(c, t, C["s17.b"], "250 mL = 0,25 L", XE, 420, 80, "g", TINTA)
    E.formula_em(c, t, C["s17.c"], "9 × 0,25 =", XE, 560, 90, "g", TINTA2)
    bola_txt(c, t, C["s17.c"] + 1.6, "2,25 g", XE + 620, 530, 100, 54, CERTO)
    E.frase(c, t, C["s18"], ps("o laudo", "i", 64, TINTA2), XE, 730)
    E.formula_em(c, t, C["s18.a"], "f{6 mg}{2 L} = 3 mg/L", XE, 870, 80, "g", TINTA)
    bola_txt(c, t, C["s18.c"], "3 ppm", 1500, 850, 110, 66, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = ((C["s19.a"], "C = f{m}{V}", "massa do soluto ÷ litros de solução"),
                 (C["s19.b"], "% × 10 = g/L", "o atalho do rótulo"),
                 (C["s19.c"], "ppm = mg/L", "na água"))
        for i, (ti, f, sub) in enumerate(itens):
            y = 380 + i * 220
            E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.formula_em(c, t, ti + 0.1, f, 400, y, 84, "g", TINTA)
            rotulo(c, t, ti + 0.4, sub, 1300, y, 50)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("mol", "g", 120, COR)], XE, 410)
    E.frase(c, t, C["s20.b"], [("concentração", "i", 80), ("em", "i", 80), ("mol/L", "g", 80, COR)], XE, 540, passo=0.12)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 460, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(760, 485, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, gl=b_gl, por=b_por, ppm=b_ppm, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
