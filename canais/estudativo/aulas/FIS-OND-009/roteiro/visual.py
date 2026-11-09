"""Visual — Estudativo · FIS-OND-009: praticando som e efeito Doppler (aula de prática, cinco questões).

Segue a linguagem visual da trilha Ondas e Som (docstring do visual.py da FIS-OND-001) e o modelo de prática da FIS-CIN-010:
cada questão tem o número no alto, o enunciado à esquerda e o desenho à direita; na pausa, o relógio entra no lugar do
desenho; na resolução, a conta em pilha (conta()) e o resultado na esfera. O MÉTODO fica no palco escuro.
Agudo em laranja, grave em azul (F.NEG). Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Ondas e Som")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OND-009_praticando_som_e_efeito_doppler.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"
GRAVE = F.NEG

# todas as contas da aula
assert 100 - 80 == 20 and 10 ** (20 // 10) == 100 and 100 / 80 == 1.25
assert 340 / 680 == 0.5
assert abs(2 * 0.6 - 1.2) < 1e-12 and abs(1.2 * 300 - 360) < 1e-9 and 3 * 300 == 900
assert 2 * 0.5 == 1 and 340 / 1 == 340 and [340 * n for n in (1, 2, 3)] == [340, 680, 1020] and 510 / 340 == 1.5 and 200 / 340 < 1
assert 340 + 34 == 374 and abs(374 / 340 - 1.1) < 1e-12 and abs(500 * 1.1 - 550) < 1e-9 and abs(500 * (340 + 34) / 340 - 550) < 1e-9


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais (copiadas da FIS-OND-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def conta(c, t, linhas, x, y0, dy, size, align="left", escuro=False):
    tinta = BR if escuro else TINTA
    for i, ln in enumerate(linhas):
        ti, s = ln[0], ln[1]
        prox = linhas[i + 1][0] if i + 1 < len(linhas) else 1e9
        cor = ln[2] if len(ln) > 2 else ((CLARO if escuro else COR) if t < prox else tinta)
        E.formula_em(c, t, ti, s, x, y0 + i * dy, size, "g", cor, align)


def pilula(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


# ---------------- peças desta aula ----------------
def cabeca(c, t, t0, n, tema):
    """número da questão no alto e o tema ao lado"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 40, 150, 46, a=a), centro(c, str(n), XE + 40, 172, 60, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, [("questão", "i", 64), (tema, "g", 60, COR)], XE + 110, 172, passo=0.15)


def desenho_ou_relogio(c, t, tp, fn):
    """o desenho da questão à direita até a pausa; na pausa, o relógio no lugar"""
    if t < tp:
        fn()
    else:
        E.relogio(c, t, tp, cx=1460, cy=470, r=190)


def alto_falante(c, x, y, s=1.0, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x - 40 * s, y - 50 * s, 50 * s, 100 * s, 8, TINTA, a)
    p = skia.Path()
    p.moveTo(x + 10 * s, y - 50 * s); p.lineTo(x + 70 * s, y - 100 * s); p.lineTo(x + 70 * s, y + 100 * s); p.lineTo(x + 10 * s, y + 50 * s); p.close()
    c.drawPath(p, M.paint(TINTA, a))


def tubo(c, x, y, w, h, a=1.0, ar=0.0, t=0.0):
    """tubo aberto nas duas pontas (paredes em tinta), com o ar vibrando em laranja se ar > 0"""
    if a <= 0:
        return
    M.line(c, x, y, x + w, y, TINTA, a, 8)
    M.line(c, x, y + h, x + w, y + h, TINTA, a, 8)
    if ar > 0:  # fundamental do tubo aberto: ventre nas pontas, nó no meio
        n = 60
        for s_ in (-1, 1):
            pts = []
            for i in range(n + 1):
                u = i / n
                amp = abs(math.cos(math.pi * u)) * h * 0.38 * math.cos(t * 6)
                pts.append((x + w * u, y + h / 2 + s_ * amp))
            F.poli(c, pts, 1.0, E.COR, a * ar, 5)


def corda(c, x0, x1, y, A, n, t, a=1.0):
    """corda presa nas pontas vibrando no harmônico n (n fusos)"""
    if a <= 0:
        return
    for k in (-1, 1):
        pts = [(x0 + (x1 - x0) * i / 120, y + k * A * math.sin(math.pi * n * i / 120) * math.cos(t * 5)) for i in range(121)]
        F.poli(c, pts, 1.0, E.COR, a * (1.0 if k == 1 else 0.35), 6)
    for xx in (x0, x1):
        c.drawCircle(xx, y, 12, M.paint(TINTA, a))


def ambulancia(c, x, y, w=240, a=1.0):
    """ambulância de lado (copiada da FIS-OND-008), rodas tocando y"""
    if a <= 0:
        return
    h = w * 0.42
    c.save(); c.translate(x, 0)
    M.rrect(c, -w / 2, y - h - w * 0.08, w * 0.72, h, 10, "#FFFFFF", a, stroke=5, stroke_color=TINTA)
    M.rrect(c, -w / 2 + w * 0.7, y - h * 0.72 - w * 0.08, w * 0.3, h * 0.72, 10, "#FFFFFF", a, stroke=5, stroke_color=TINTA)
    cx_, cy_ = -w * 0.16, y - h * 0.55 - w * 0.08
    M.line(c, cx_ - h * 0.22, cy_, cx_ + h * 0.22, cy_, ERRADO, a, h * 0.12)
    M.line(c, cx_, cy_ - h * 0.22, cx_, cy_ + h * 0.22, ERRADO, a, h * 0.12)
    M.rrect(c, -w * 0.2, y - h - w * 0.08 - h * 0.18, w * 0.12, h * 0.18, 4, E.COR, a)
    for rx in (-w * 0.3, w * 0.3):
        c.drawCircle(rx, y - w * 0.07, w * 0.08, M.paint(TINTA, a))
    c.restore()


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01"], ps("na prova, o som aparece de", "i", 70), XE, 250, passo=0.1)
    E.foco(c, t, C["s01.a"], 0.5, lambda a: E.escreve(c, "4", XE, 520, 280, "g", COR, a))
    E.foco(c, t, C["s01.a"] + 0.2, 0.5, lambda a: E.escreve(c, "jeitos", XE + 200, 510, 110, "i", TINTA, a))
    for i, (k, s) in enumerate((("s01.b", "decibéis"), ("s01.c", "instrumentos"), ("s01.d", "ressonância"), ("s01.e", "Doppler"))):
        y = 340 + i * 130
        E.foco(c, t, C[k], 0.5, lambda a, s=s, y=y, i=i: E.pilula(c, s, 1300, y, 68, "g", fundo=E.COR if i == 3 else TINTA, a=a, cor=BR))
    E.frase(c, t, C["s01.f"], ps("até o fim da aula:", "i", 64) + [("5 questões", "g", 64, COR)], XE, 920, passo=0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar as aulas do módulo", "i", 76), XE, 260, passo=0.1)
    for i, (k, s1, s2) in enumerate((("s02.a", "altura, intensidade", "e timbre"), ("s02.b", "cordas", "e tubos"), ("s02.c", "efeito", "Doppler"))):
        x = XE + i * 540
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 400, 480, 300, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(s1, "g", 54)], x + 40, 520)
        E.frase(c, t, C[k] + 0.3, [(s2, "g", 54, COR)], x + 40, 610)
    E.frase(c, t, lerp(C["s02.c"], C["s02.end"], 0.5), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), XE, 880, "left", 0.12)


# ---------------- método (palco) ----------------
def b_metodo(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s03"], ps("primeiro, o método:", "i", 70, CLARO), W / 2, 160, "center", 0.12)
    E.frase(c, t, C["s03.a"], ps("o que a questão", "i", 76, CLARO) + [("compara?", "g", 76, BR)], W / 2, 280, "center", 0.12)
    linhas = (("s03.b", "grave ou agudo", "frequência"), ("s03.c", "forte ou fraco", "intensidade (dB)"), ("s03.d", "instrumentos, mesma nota", "timbre"),
              ("s03.e", "corpo vibra forte com um som", "ressonância"), ("s03.f", "fonte ou ouvinte andando", "Doppler"))
    for i, (k, s1, s2) in enumerate(linhas):
        y = 430 + i * 125
        E.frase(c, t, C[k], ps(s1, "i", 58, CLARO), 900, y, "right", 0.06)
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, y=y: F.seta(c, 940, y - 20, 1060, y - 20, CLARO, a, 6))
        E.foco(c, t, C[k] + 0.5, 0.4, lambda a, y=y, s2=s2: E.escreve(c, s2, 1100, y, 62, "g", BR, a))


# ---------------- questão 1: decibéis ----------------
def b_q1(c, t, C, b):
    cabeca(c, t, C["s04"], 1, "decibéis")
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("fone no máximo:", "i", 64), XE, 360, passo=0.1)
        E.foco(c, t, C["s04.a"] + 0.6, 0.5, lambda a: F.medida(c, 100, "dB", XE + 500, 360, 90, ERRADO, a))
        E.frase(c, t, C["s04.b"], ps("recomendado:", "i", 64), XE, 500, passo=0.1)
        E.foco(c, t, C["s04.b"] + 0.5, 0.5, lambda a: F.medida(c, 80, "dB", XE + 500, 500, 90, CERTO, a))
        E.frase(c, t, C["s04.c"], ps("quantas vezes", "i", 70) + [("mais intenso?", "g", 70, COR)], XE, 680, passo=0.12)

        def fone():
            x, y = 1460, 480
            E.arco(c, x, y, 150, 180, 180, TINTA, 22, 1.0)
            for dx in (-150, 150):
                M.rrect(c, x + dx - 40, y - 10, 80, 140, 26, E.COR, 1.0)
        desenho_ou_relogio(c, t, C["s04.d"], lambda: E.foco(c, t, C["s04.a"], 0.6, lambda a: fone() if a > 0.99 else None))
        return
    conta(c, t, [(C["s05.a"], "100 − 80 = 20 dB"), (C["s05.b"], "2 dezenas → 10 · 10")], XE, 420, 180, 100)
    bola_txt(c, t, C["s05.c"], "100 vezes", 1450, 470, 170, 66)
    E.foco(c, t, C["s05.d"], 0.5, lambda a: E.formula(c, "100 ÷ 80 = 1,25", XE, 880, 80, "g", ERRADO, a))
    if t >= C["s05.d"] + 0.8:
        E.risco(c, XE - 10, 890, XE + 600, 820, t, C["s05.d"] + 0.8, largura=10)
    E.frase(c, t, C["s05.d"] + 1.2, ps("a escala é de", "i", 60) + [("logaritmo", "g", 58, COR)], XE + 700, 880, passo=0.1)


# ---------------- questão 2: timbre ----------------
def b_q2(c, t, C, b):
    cabeca(c, t, C["s06"], 2, "instrumentos")
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], ps("flauta e violino:", "i", 64), XE, 360, passo=0.1)
        E.frase(c, t, C["s06.a"] + 1.0, ps("mesma nota", "i", 64) + [("680", "g", 64, COR), ("Hz,", "b", 52, F.UNID)], XE, 460, passo=0.1)
        E.frase(c, t, C["s06.a"] + 2.0, ps("mesma intensidade", "i", 64), XE, 560, passo=0.1)
        E.frase(c, t, C["s06.b"], ps("o que é", "i", 64) + [("igual?", "g", 64, CERTO), ("diferente?", "g", 64, ERRADO)], XE, 700, passo=0.12)
        E.frase(c, t, C["s06.c"], [("λ", "g", 70, COR)] + ps("no ar?", "i", 64), XE, 820, passo=0.12)

        def ondas():
            for k, y in enumerate((360, 600)):
                pts = []
                for i in range(241):
                    xx = 1150 + 600 * i / 240
                    ph = 2 * math.pi * 3 * i / 240
                    yy = math.sin(ph) + (0.5 * math.sin(2 * ph) if k == 0 else 0.35 * math.sin(3 * ph + 1))
                    pts.append((xx, y - 70 * yy))
                F.poli(c, pts, 1.0, E.COR, 1.0, 6)
            E.escreve(c, "flauta", 1150, 250, 46, "i", TINTA2)
            E.escreve(c, "violino", 1150, 490, 46, "i", TINTA2)
        desenho_ou_relogio(c, t, C["s06.d"], lambda: E.foco(c, t, C["s06.a"], 0.6, lambda a: ondas() if a > 0.99 else None))
        return
    for i, (k, s1, s2, cor) in enumerate((("s07.a", "frequência", "mesma altura", CERTO), ("s07.b", "intensidade", "mesma força", CERTO),
                                         ("s07.c", "formato da onda", "timbre diferente", ERRADO))):
        y = 340 + i * 150
        E.foco(c, t, C[k], 0.5, lambda a, s1=s1, y=y: E.escreve(c, s1, XE, y, 64, "i", TINTA, a))
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, s2=s2, y=y, cor=cor: E.pilula(c, s2, XE + 780, y - 22, 54, "g", fundo=cor, a=a, cor=BR))
    E.foco(c, t, C["s07.c"] + 1.4, 0.4, lambda a: E.escreve(c, "cada um mistura harmônicos de um jeito", XE, 720, 50, "i", TINTA2, a))
    conta(c, t, [(C["s07.d"], "λ = 340 ÷ 680 = 0,5 m")], XE, 900, 0, 90)
    E.foco(c, t, C["s07.d"] + 1.2, 0.4, lambda a: E.pilula(c, "igual para os dois", 1560, 870, 50, "g", fundo=TINTA, a=a, cor=BR))


# ---------------- questão 3: corda ----------------
def b_q3(c, t, C, b):
    cabeca(c, t, C["s08"], 3, "cordas")
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("corda de", "i", 64), XE, 360, passo=0.1)
        E.foco(c, t, C["s08.a"] + 0.5, 0.5, lambda a: F.medida(c, 60, "cm", XE + 290, 360, 84, COR, a))
        E.frase(c, t, C["s08.a"] + 1.4, ps("fundamental:", "i", 64), XE, 470, passo=0.1)
        E.foco(c, t, C["s08.a"] + 1.9, 0.5, lambda a: F.medida(c, 300, "Hz", XE + 400, 470, 84, COR, a))
        E.frase(c, t, C["s08.b"], [("v", "g", 76, COR), ("?", "g", 76)], XE, 640, passo=0.1)
        E.frase(c, t, C["s08.c"], ps("3º harmônico?", "g", 70), XE, 760, passo=0.1)
        desenho_ou_relogio(c, t, C["s08.d"], lambda: E.foco(c, t, C["s08.a"], 0.6, lambda a: corda(c, 1120, 1800, 480, 80, 1, t, a)))
        return
    conta(c, t, [(C["s09.a"], "λ = 2 · 0,6 = 1,2 m"), (C["s09.b"], "v = 1,2 · 300 = 360 m/s"), (C["s09.c"], "3º harmônico: 3 · 300")], XE, 360, 190, 90)
    E.foco(c, t, C["s09.a"], 0.5, lambda a: corda(c, 1260, 1800, 300, 60, 1, t, a))
    E.foco(c, t, C["s09.c"], 0.5, lambda a: corda(c, 1260, 1800, 560, 60, 3, t, a))
    E.foco(c, t, C["s09.c"] + 0.3, 0.4, lambda a: E.escreve(c, "3 fusos", 1460, 690, 50, "i", TINTA2, a))
    bola_txt(c, t, C["s09.d"], "900 Hz", 1470, 880, 120, 60)


# ---------------- questão 4: ressonância ----------------
def b_q4(c, t, C, b):
    cabeca(c, t, C["s10"], 4, "ressonância")
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("tubo aberto de", "i", 64), XE, 360, passo=0.1)
        E.foco(c, t, C["s10.a"] + 0.6, 0.5, lambda a: F.medida(c, "0,5", "m", XE + 440, 360, 84, COR, a))
        E.foco(c, t, C["s10.b"], 0.5, lambda a: (E.escreve(c, "v =", XE, 480, 70, "g", TINTA, a), F.medida(c, 340, "m/s", XE + 150, 480, 70, TINTA, a)))
        E.frase(c, t, C["s10.c"], ps("ressoa em qual?", "i", 64), XE, 630, passo=0.1)
        for i, s in enumerate(("200", "340", "510")):
            E.foco(c, t, C["s10.c"] + 1.0 + 0.4 * i, 0.4, lambda a, s=s, i=i: E.pilula(c, s + " Hz", XE + 150 + i * 300, 770, 60, "g", fundo=TINTA, a=a, cor=BR))

        def cena():
            tubo(c, 1080, 400, 560, 140, 1.0)
            alto_falante(c, 1760, 470, 0.9)
        desenho_ou_relogio(c, t, C["s10.d"], lambda: E.foco(c, t, C["s10.a"], 0.6, lambda a: cena() if a > 0.99 else None))
        return
    conta(c, t, [(C["s11.a"], "2L = 2 · 0,5 = 1 m"), (C["s11.b"], "fundamental: 340 ÷ 1 = 340 Hz"), (C["s11.c"], "680 · 1.020 · ...")], XE, 330, 160, 84)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: tubo(c, 1260, 230, 520, 130, a, 1.0, t))
    for i, (s, ok) in enumerate((("200", False), ("340", True), ("510", False))):
        x = XE + 150 + i * 300
        E.foco(c, t, C["s11.d"] - 0.2, 0.4, lambda a, s=s, x=x, ok=ok: E.pilula(c, s + " Hz", x, 860, 60, "g", fundo=CERTO if ok else TINTA2, a=a, cor=BR))
    E.foco(c, t, C["s11.d"] + 0.5, 0.5, lambda a: E.selo(c, XE + 450, 740, 46, True, a))
    E.foco(c, t, C["s11.e"], 0.5, lambda a: E.escreve(c, "510 = 1,5 × 340: não serve", 1080, 870, 56, "b", ERRADO, a))


# ---------------- questão 5: Doppler ----------------
def b_q5(c, t, C, b):
    cabeca(c, t, C["s12"], 5, "Doppler")
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"], ps("você no carro a", "i", 64), XE, 360, passo=0.1)
        E.foco(c, t, C["s12.a"] + 0.7, 0.5, lambda a: F.medida(c, 34, "m/s", XE + 470, 360, 84, COR, a))
        E.frase(c, t, C["s12.a"] + 1.6, ps("rumo à sirene parada de", "i", 60), XE, 470, passo=0.08)
        E.foco(c, t, C["s12.a"] + 2.6, 0.5, lambda a: F.medida(c, 500, "Hz", XE, 590, 84, COR, a))
        E.frase(c, t, C["s12.b"], [("f'", "g", 80, COR), ("?", "g", 80)], XE, 750, passo=0.1)

        def cena():
            y = 640
            F.chao(c, 1080, 1840, y)
            ambulancia(c, 1700, y, 200)
            F.carrinho(c, 1240 + 120 * ((t * 0.3) % 1), y, 200)
            for k in range(4):
                r = 60 + ((t * 120 + k * 90) % 360)
                c.drawCircle(1700, y - 100, r, M.paint(E.COR, 0.8 * (1 - r / 420), stroke=5))
        desenho_ou_relogio(c, t, C["s12.c"], lambda: E.foco(c, t, C["s12.a"], 0.6, lambda a: cena() if a > 0.99 else None))
        return
    E.foco(c, t, C["s13.a"], 0.5, lambda a: E.pilula(c, "aproximou ↑: maior que 500", XE + 380, 290, 54, "g", fundo=E.COR, a=a, cor=BR))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "f' = 500 · f{340 + 34}{    }", XE, 520, 100, "g", TINTA, a) if t < C["s13.c"] else None)
    E.foco(c, t, C["s13.c"], 0.3, lambda a: E.formula(c, "f' = 500 · f{340 + 34}{340}", XE, 520, 100, "g", TINTA, a))
    E.foco(c, t, C["s13.b"] + 0.4, 0.4, lambda a: E.escreve(c, "observador: + em cima", 1150, 430, 52, "i", TINTA2, a))
    E.foco(c, t, C["s13.c"] + 0.4, 0.4, lambda a: E.escreve(c, "fonte parada: só v", 1150, 620, 52, "i", TINTA2, a))
    conta(c, t, [(C["s13.d"], "f{374}{340} = 1,1"), (C["s13.e"], "500 · 1,1")], XE, 790, 160, 90)
    bola_txt(c, t, C["s13.e"] + 0.5, "550 Hz", 1480, 840, 140, 66)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s14"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s14.a", "decibéis:", "conte as dezenas"), ("s14.b", "instrumentos:", "o timbre"),
                 ("s14.c", "cordas e tubos:", "múltiplos do fundamental"), ("s14.d", "Doppler:", "aproximou, subiu"))
        for i, (k, s1, s2) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s1, "g", 68)] + ps(s2, "i", 68), 400, y, passo=0.1)
    E.saida(c, t, C["s14.e"] - 1.5, resumo)
    if t < C["s14.e"] - 1.4:
        return
    E.frase(c, t, C["s14.e"] - 1.4, [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s14.e"], [("espectro", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s14.e"] + 0.5, [("eletromagnético", "g", 90, COR)], XE, 520)
    E.foco(c, t, C["s14.e"] + 1.0, 0.5, lambda a: E.escreve(c, "do rádio ao raio gama", XE, 640, 66, "i", TINTA, a))
    E.foco(c, t, C["s14.f"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s14.f"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s14.f"] + 0.2, 0.4))
    E.frase(c, t, C["s14.g"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5, fim=b_fim)
