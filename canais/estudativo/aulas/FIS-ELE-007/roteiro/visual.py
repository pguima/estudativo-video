"""Visual — Estudativo · FIS-ELE-007: praticando eletrostática (5 questões inéditas).

Segue a linguagem visual da Física (FIS-CIN-001) e a da trilha Eletricidade (docstring do visual.py da FIS-ELE-001).
Cada questão: enunciado à esquerda, desenho à direita, relógio de pausa no lugar do desenho; a resolução ocupa a tela
com as contas em sequência e a resposta numa pílula (verde). Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-007_praticando_eletrostatica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
METAL = "#A3AAB4"

# todas as contas da aula
assert abs((4.8 - 1.6) / 2 - 1.6) < 1e-12 and abs(1.6 - (-1.6) - 3.2) < 1e-12 and abs(3.2e-6 / 1.6e-19 - 2e13) / 2e13 < 1e-9 and -6 + 19 == 13
assert 80 / 2 == 40 and 40 * 4 == 160 and 80 * (1 / 2) / (1 / 2) ** 2 == 160
assert abs(1.6e-19 * 5e4 - 8e-15) < 1e-27 and 1.6 * 5 == 8 and -19 + 4 == -15
assert abs(5e4 * 0.02 - 1000) < 1e-9 and abs(1.6e-19 * 1000 - 1.6e-16) < 1e-28
assert abs(10e-6 * 200 - 2e-3) < 1e-12 and abs(2e-3 * 200 / 2 - 0.2) < 1e-12 and abs(10e-6 * 100 ** 2 / 2 - 0.05) < 1e-12 and abs(0.2 / 4 - 0.05) < 1e-12


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha Eletricidade (cópia das da FIS-ELE-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def q(c, x, y, r, s, a=1.0):
    """carga pequena: + laranja, − azul, com o sinal em branco"""
    if a <= 0:
        return
    cor = E.COR if s == "+" else NEG
    c.drawCircle(x + r * 0.08, y + r * 0.16, r, M.paint("#000000", 0.16 * a))
    c.drawCircle(x, y, r, M.paint(cor, a))
    k, lw = r * 0.52, max(3, r * 0.24)
    M.line(c, x - k, y, x + k, y, BR, a, lw)
    if s == "+":
        M.line(c, x, y - k, x, y + k, BR, a, lw)


def esfera_metal(c, cx, cy, R, a=1.0):
    E.bola(c, cx, cy, R, METAL, a)


def pilula_f(c, s, cx, cy, size, fundo=None, cor=BR, a=1.0):
    """pílula com fórmula (aceita potência de dez)"""
    if a <= 0:
        return
    w, h = E.formula(None, s, 0, 0, size, "g", a=0) + size * 1.2, size * 1.9
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(fundo or E.COR, a))
    E.formula(c, s, cx, cy + size * 0.36, size, "g", cor, a, "center")


def _linha(c, partes, x, y, a, align="center"):
    """linha de tipografia mista parada (para a troca)"""
    w, xs = E._arranjo(partes, x, align)
    for p, xx in zip(partes, xs):
        E.escreve(c, p[0], xx, y, p[2], p[1], p[3] if len(p) > 3 else TINTA, a)


def terra(c, x, y, a=1.0, cor=TINTA):
    """símbolo de terra: três traços, o de cima em y"""
    for i, w in enumerate((90, 60, 30)):
        M.line(c, x - w / 2, y + i * 18, x + w / 2, y + i * 18, cor, a, 6)


def promessa(c, t, C, cena, itens, sz=74):
    """tela "até o fim da aula": órbita à direita e itens numerados. itens = [(cue, texto, atraso)]"""
    tb = C[itens[0][0]] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(i + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", sz, COR if i == 0 else TINTA)], XE + 110, y)


def lembrete(c, t, C, cena, itens, desenhos):
    """o que precisa saber: itens = [(cue, linha fina, linha forte)]; desenhos[i](a, cx, cy) desenha à direita da caixa"""
    if len(itens) == 2:
        E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
        E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
        E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    else:
        E.frase(c, t, C[cena] + 0.2, ps("você precisa", "i", 84), XE, 470, passo=0.14)
        E.frase(c, t, C[cena] + 0.6, ps("de uma coisa", "i", 84), XE, 580, passo=0.14)
    x, w = 820, 1000
    y0 = 230 if len(itens) == 2 else 340
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 190, y + 115))
    if len(itens) == 2:
        q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
        E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    else:
        E.cursor(c, x + w - 30, 560, ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def resumo(c, t, C, cena, itens, dy=190):
    """tela "resumindo": itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 380 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)


def cta(c, t, C, cena):
    """inscreva-se (cue c) e bons estudos (cue d), à direita"""
    E.foco(c, t, C[cena + ".c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[cena + ".c"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C[cena + ".c"] + 0.2, 0.4))
    E.frase(c, t, C[cena + ".d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1580, 990, "center")


def questao_relogio(c, t, C, cena_pausa, desenho):
    """lado direito da questão: o desenho até a pausa, depois o relógio"""
    if t < C[cena_pausa]:
        desenho()
    else:
        E.relogio(c, t, C[cena_pausa + ".a"], cx=1460, cy=440, r=200)



def titulo_q(c, t, t0, n):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 46, 176, 46, a=a), centro(c, str(n), XE + 46, 198, 56, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, [("questão", "i", 72, TINTA2)], XE + 120, 200)


def placas(c, t, t0, x1, x2, y0, y1, a=1.0, linhas=True):
    q_ = ep(t, t0, 0.5) * a
    if q_ <= 0:
        return
    M.rrect(c, x1 - 22, y0 - 30, 44, y1 - y0 + 60, 10, E.COR, q_)
    M.rrect(c, x2 - 22, y0 - 30, 44, y1 - y0 + 60, 10, NEG, q_)
    for i in range(5):
        yy = lerp(y0, y1, (i + 0.5) / 5)
        M.line(c, x1 - 10, yy, x1 + 10, yy, BR, q_, 5)
        M.line(c, x1, yy - 10, x1, yy + 10, BR, q_, 5)
        M.line(c, x2 - 10, yy, x2 + 10, yy, BR, q_, 5)
    if linhas:
        for i in range(4):
            yy = lerp(y0 + 30, y1 - 30, i / 3)
            M.line(c, x1 + 30, yy, x2 - 30, yy, TINTA2, q_, 4)
            F._cabeca(c, (x1 + x2) / 2 + 11, yy, 1, 0, 20, TINTA2, q_)


def capacitor(c, x1, x2, y0, y1, a=1.0):
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeLTRB(x1 + 18, y0, x2 - 18, y1), M.paint("#FFE9A8", 0.7 * a))
    M.rrect(c, x1 - 18, y0, 36, y1 - y0, 8, METAL, a)
    M.rrect(c, x2 - 18, y0, 36, y1 - y0, 8, METAL, a)
    for i in range(4):
        yy = lerp(y0 + 40, y1 - 40, i / 3)
        q(c, x1 + 2, yy, 20, "+", a)
        q(c, x2 - 2, yy, 20, "−", a)


def pausa_ou(c, t, tp, desenho):
    """desenho à direita até o pause; depois o relógio"""
    if t < tp:
        desenho()
    else:
        E.relogio(c, t, tp, cx=1460, cy=440, r=200)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    fs = (("Q = n · e", 300, 420), ("F = k · f{Q₁ · Q₂}{d^2}", 1000, 330), ("E = f{F}{q}", 1550, 520), ("U = E · d", 620, 700),
          ("τ = q · U", 1250, 760), ("C = f{Q}{U}", 1650, 900))
    for i, (s, x, y) in enumerate(fs):
        u = ep(t, C["s01.a"] + 0.15 * i, 0.5) * (1 - ep(t, C["s01.b"] - 0.3, 0.4))
        if u > 0:
            E.formula(c, s, x, y, 76, "g", TINTA2, u, "center")
    E.frase(c, t, C["s01.a"], ps("muitas fórmulas parecidas", "i", 80), W / 2, 200, "center", 0.12)
    E.frase(c, t, C["s01.b"], [("5", "g", 200, COR), ("questões", "g", 110)], W / 2, 560, "center", 0.2)
    E.frase(c, t, C["s01.c"], ps("qual fórmula usar?", "i", 76), W / 2, 800, "center", 0.12)
    E.foco(c, t, C["s01.c"] + 1.4, 0.5, lambda a: E.pilula(c, "olhe o que a questão pede", W / 2, 930, 50, "g", fundo=E.COR, a=a))


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    def s02():
        E.frase(c, t, C["s02"] + 0.3, ps("as aulas do módulo", "i", 70, TINTA2), XE, 220, passo=0.12)
        E.frase(c, t, C["s02"] + 1.4, [("faltou", "i", 56, COR), ("alguma?", "i", 56, COR), ("procure", "i", 56), ("no", "i", 56), ("canal", "i", 56)], XE, 310, passo=0.1)
        E.foco(c, t, C["s02.a"], 0.5, lambda a: (E.bola(c, XE + 46, 494, 46, a=a), centro(c, "1", XE + 46, 516, 56, "g", BR, a)))
        E.frase(c, t, C["s02.a"] + 0.1, ps("o que a questão", "i", 80) + [("pede?", "g", 76, COR)], XE + 130, 520, passo=0.12)
        E.foco(c, t, C["s02.b"], 0.5, lambda a: (E.bola(c, XE + 46, 714, 46, a=a), centro(c, "2", XE + 46, 736, 56, "g", BR, a)))
        E.frase(c, t, C["s02.b"] + 0.1, ps("a fórmula com isso", "i", 80) + [("e", "i", 80), ("os", "i", 80), ("dados", "g", 76, COR)], XE + 130, 740, passo=0.12)
    E.saida(c, t, C["s03"] - 0.1, s02)
    if t < C["s03"]:
        return
    E.frase(c, t, C["s03"], [("a", "i", 80), ("caixa", "i", 80), ("de", "i", 80), ("ferramentas", "g", 76, COR)], W / 2, 180, "center", 0.12)
    itens = (("s03.a", "carga", "Q = n · e"), ("s03.b", "força", "F = k · f{Q₁ · Q₂}{d^2}"), ("s03.c", "campo", "E = f{F}{q}"),
             ("s03.d", "tensão", "U = E · d"), ("s03.e", "trabalho", "τ = q · U"), ("s03.f", "capacitor", "C = f{Q}{U}"))
    for i, (k, nome, f_) in enumerate(itens):
        col, lin = i // 3, i % 3
        x, y = 200 + col * 860, 380 + lin * 230
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y - 90, 760, 190, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(nome, "i", 60, TINTA2)], x + 36, y + 20)
        E.formula_em(c, t, C[k] + 0.3, f_, x + 330, y + 30, 70, "g", TINTA)


# ---------------- questão 1: contato e Q = n·e ----------------
def b_q1(c, t, C, b):
    if t < C["s05"]:
        titulo_q(c, t, C["s04"], 1)
        E.frase(c, t, C["s04.a"] - 0.8, ps("esferas de metal iguais", "i", 66), XE, 330, passo=0.1)
        E.foco(c, t, C["s04.a"], 0.5, lambda a: (E.escreve(c, "1:", XE, 450, 76, "g", TINTA, a), F.medida(c, "+4,8", "µC", XE + 110, 450, 76, COR, a)))
        E.foco(c, t, C["s04.b"], 0.5, lambda a: (E.escreve(c, "2:", XE, 560, 76, "g", TINTA, a), F.medida(c, "−1,6", "µC", XE + 110, 560, 76, NEG, a)))
        E.frase(c, t, C["s04.c"], ps("encostam e separam:", "i", 62) + [("carga", "g", 60), ("de", "i", 62), ("cada?", "g", 60, COR)], XE, 720, passo=0.1)
        E.frase(c, t, C["s04.d"], [("quantos", "i", 66), ("elétrons", "g", 62, COR), ("passaram?", "i", 66)], XE, 840, passo=0.12)

        def desenho():
            E.foco(c, t, C["s04.a"], 0.5, lambda a: (E.bola(c, 1300, 480, 140, METAL, a), centro(c, "1", 1300, 505, 70, "g", BR, a)))
            E.foco(c, t, C["s04.b"], 0.5, lambda a: (E.bola(c, 1640, 480, 140, METAL, a), centro(c, "2", 1640, 505, 70, "g", BR, a)))
        pausa_ou(c, t, C["s04.e"], desenho)
        return
    E.formula_em(c, t, C["s05.a"], "(+4,8) + (−1,6) = +3,2", XE, 230, 80, "g", TINTA)
    E.foco(c, t, C["s05.b"], 0.5, lambda a: pilula_f(c, "÷ 2 → +1,6 µC em cada", 1460, 205, 56, fundo=CERTO, a=a))
    E.formula_em(c, t, C["s05.c"], "esfera 2:  −1,6  →  +1,6", XE, 410, 76, "g", TINTA)
    E.foco(c, t, C["s05.c"] + 1.4, 0.4, lambda a: E.escreve(c, "mudou 3,2 µC", XE + 1050, 410, 60, "b", TINTA2, a))
    E.formula_em(c, t, C["s05.d"], "n = f{Q}{e} = f{3,2 × 10^{−6}}{1,6 × 10^{−19}}", XE, 620, 80, "g", TINTA)
    E.foco(c, t, C["s05.d"] + 1.6, 0.4, lambda a: E.escreve(c, "3,2 ÷ 1,6 = 2;  −6 + 19 = 13", XE + 1080, 610, 50, "b", TINTA2, a))
    E.foco(c, t, C["s05.e"], 0.5, lambda a: pilula_f(c, "n = 2 × 10^{13} elétrons", 640, 860, 70, fundo=CERTO, a=a))
    E.foco(c, t, C["s05.f"], 0.5, lambda a: (E.bola(c, 1330, 860, 80, METAL, a), E.bola(c, 1730, 860, 80, METAL, a),
                                            centro(c, "1", 1330, 885, 56, "g", BR, a), centro(c, "2", 1730, 885, 56, "g", BR, a)))
    if t >= C["s05.f"] + 0.4:
        for i in range(3):
            u = ((t - C["s05.f"] - 0.4) * 0.8 + i / 3) % 1
            q(c, lerp(1660, 1400, u), 860 - 60 * math.sin(u * math.pi), 18, "−", ep(t, C["s05.f"] + 0.4, 0.3))


# ---------------- questão 2: Coulomb por proporção ----------------
def b_q2(c, t, C, b):
    if t < C["s07"]:
        titulo_q(c, t, C["s06"], 2)
        E.frase(c, t, C["s06.a"] - 0.6, [("se", "i", 76), ("atraem", "i", 76), ("com", "i", 76)], XE, 340, passo=0.12)
        E.foco(c, t, C["s06.a"], 0.5, lambda a: F.medida(c, 80, "N", XE + 450, 340, 90, COR, a))
        E.frase(c, t, C["s06.b"], [("uma", "i", 76), ("carga", "i", 76), ("÷", "g", 76, COR), ("2", "g", 76, COR)], XE, 490, passo=0.15)
        E.frase(c, t, C["s06.c"], [("distância", "i", 76), ("÷", "g", 76, COR), ("2", "g", 76, COR)], XE, 620, passo=0.15)
        E.frase(c, t, C["s06.d"], [("nova", "i", 80), ("força?", "g", 80, COR)], XE, 790, passo=0.15)

        def desenho():
            y = 480
            u = ease_io(prog(t, C["s06.c"], 0.8))
            x2 = lerp(1760, 1500, u)
            F.carga(c, t, C["s06.a"], 1240, y, 56, "+")
            F.carga(c, t, C["s06.a"] + 0.2, x2, y, 56, "−")
            if t >= C["s06.a"] + 0.4:
                a = ep(t, C["s06.a"] + 0.4, 0.3)
                F.seta(c, 1310, y, 1390, y, E.COR, a, 9)
                F.seta(c, x2 - 70, y, x2 - 150, y, E.COR, a, 9)
        pausa_ou(c, t, C["s06.e"], desenho)
        return
    E.frase(c, t, C["s07"], [("use", "i", 80), ("a", "i", 80), ("proporção", "g", 76, COR)], XE, 220, passo=0.12)
    E.formula_em(c, t, C["s07.a"], "carga ÷ 2  →  F ÷ 2", XE, 400, 84, "g", TINTA)
    E.formula_em(c, t, C["s07.b"], "distância ÷ 2  →  F × 4", XE, 560, 84, "g", TINTA)
    E.formula_em(c, t, C["s07.c"], "80 ÷ 2 = 40", XE, 760, 90, "g", TINTA2)
    E.foco(c, t, C["s07.d"], 0.5, lambda a: (E.formula(c, "40 × 4 =", XE + 700, 760, 90, "g", TINTA2, a), pilula_f(c, "160 N", 1560, 730, 90, fundo=CERTO, a=a)))
    E.frase(c, t, C["s07.e"], [("a", "i", 76), ("força", "i", 76), ("dobrou", "g", 72, COR)], XE, 940, passo=0.12)


# ---------------- questão 3: força no elétron ----------------
def b_q3(c, t, C, b):
    x1, x2, y0, y1 = 1140, 1740, 320, 760
    if t < C["s09"]:
        titulo_q(c, t, C["s08"], 3)
        E.frase(c, t, C["s08.a"] - 0.8, ps("campo uniforme:", "i", 66), XE, 330, passo=0.1)
        E.formula_em(c, t, C["s08.a"], "E = 5 × 10^4 N/C", XE, 440, 76, "g", COR)
        E.frase(c, t, C["s08.b"], [("um", "i", 70), ("elétron", "g", 66, NEG)], XE, 570, passo=0.12)
        E.frase(c, t, C["s08.c"], [("força:", "i", 70), ("valor", "g", 66), ("e", "i", 70), ("sentido?", "g", 66, COR)], XE, 680, passo=0.12)
        E.frase(c, t, C["s08.f"], ps("e dentro de um metal", "i", 60), XE, 800, passo=0.1)
        E.frase(c, t, C["s08.f"] + 1.0, ps("carregado, em equilíbrio?", "i", 60), XE, 880, passo=0.1)

        def desenho():
            placas(c, t, C["s08.a"], x1, x2, y0, y1)
            E.foco(c, t, C["s08.b"], 0.4, lambda a: q(c, (x1 + x2) / 2, 600, 26, "−", a))
        pausa_ou(c, t, C["s08.e"], desenho)
        return
    E.formula_em(c, t, C["s09.a"], "F = e · E", XE, 260, 90, "g", TINTA)
    E.formula_em(c, t, C["s09.a"] + 1.4, "= 1,6 × 10^{−19} · 5 × 10^4", XE + 420, 260, 76, "g", TINTA2)
    E.formula_em(c, t, C["s09.b"], "1,6 · 5 = 8", XE, 440, 76, "g", COR)
    E.formula_em(c, t, C["s09.c"], "−19 + 4 = −15", XE + 520, 440, 76, "g", COR)
    E.foco(c, t, C["s09.d"], 0.5, lambda a: pilula_f(c, "F = 8 × 10^{−15} N", 640, 620, 72, fundo=CERTO, a=a))
    placas(c, t, C["s09.e"] - 0.3, 1220, 1740, 380, 660, linhas=False)
    E.foco(c, t, C["s09.e"] - 0.1, 0.4, lambda a: (F.seta(c, 1360, 440, 1600, 440, TINTA, a, 7), E.escreve(c, "E", 1470, 415, 48, "g", TINTA, a)))
    E.foco(c, t, C["s09.e"], 0.4, lambda a: q(c, 1480, 580, 26, "−", a))
    if t >= C["s09.f"]:
        F.seta(c, 1440, 580, 1280, 580, E.COR, ep(t, C["s09.f"], 0.3), 9, None, ease_out(prog(t, C["s09.f"], 0.5)))
    E.frase(c, t, C["s09.f"], ps("contrária ao campo", "i", 56, TINTA2), 1480, 760, "center", 0.1)
    E.foco(c, t, C["s09.g"], 0.5, lambda a: (E.bola(c, 1480, 930, 90, METAL, a), E.formula(c, "E = 0", 1480, 950, 50, "g", TINTA, a, "center")))
    E.foco(c, t, C["s09.g"] + 0.6, 0.5, lambda a: pilula_f(c, "dentro do metal: F = 0", 640, 880, 66, fundo=CERTO, a=a))


# ---------------- questão 4: tensão e trabalho ----------------
def b_q4(c, t, C, b):
    x1, x2, y0, y1 = 1140, 1740, 320, 760
    if t < C["s11"]:
        titulo_q(c, t, C["s10"], 4)
        E.frase(c, t, C["s10"] + 0.6, ps("as mesmas placas:", "i", 64, TINTA2), XE, 330, passo=0.1)
        E.formula_em(c, t, C["s10"] + 1.0, "E = 5 × 10^4 N/C", XE, 430, 70, "g", TINTA2)
        E.foco(c, t, C["s10.a"], 0.5, lambda a: (E.escreve(c, "d =", XE, 550, 76, "g", TINTA, a), F.medida(c, 2, "cm", XE + 160, 550, 76, COR, a)))
        E.frase(c, t, C["s10.b"], [("tensão", "g", 70), ("entre", "i", 72), ("as", "i", 72), ("placas?", "g", 70, COR)], XE, 690, passo=0.12)
        E.frase(c, t, C["s10.c"], [("trabalho", "g", 66), ("num", "i", 70), ("próton,", "g", 66, COR)], XE, 810, passo=0.12)
        E.frase(c, t, C["s10.c"] + 1.2, ps("da placa + até a −", "i", 60, TINTA2), XE, 900, passo=0.1)

        def desenho():
            placas(c, t, C["s10"] + 0.3, x1, x2, y0, y1)
            if t >= C["s10.a"]:
                a = ep(t, C["s10.a"], 0.4)
                M.line(c, x1, 860, x2, 860, TINTA2, a, 4, dash=E.TRACO)
                F.medida(c, 2, "cm", (x1 + x2) / 2, 930, 60, TINTA, a, "center")
            E.foco(c, t, C["s10.c"], 0.4, lambda a: q(c, x1 + 70, 540, 26, "+", a))
        pausa_ou(c, t, C["s10.d"], desenho)
        return
    E.formula_em(c, t, C["s11.a"], "2 cm = 0,02 m", XE, 230, 76, "g", TINTA2)
    E.formula_em(c, t, C["s11.b"], "U = E · d = 5 × 10^4 · 0,02", XE, 400, 80, "g", TINTA)
    E.foco(c, t, C["s11.c"], 0.5, lambda a: pilula_f(c, "U = 1.000 V", 1560, 375, 76, a=a))
    E.formula_em(c, t, C["s11.d"], "τ = q · U = 1,6 × 10^{−19} · 1.000", XE, 620, 80, "g", TINTA)
    E.foco(c, t, C["s11.e"], 0.5, lambda a: pilula_f(c, "τ = 1,6 × 10^{−16} J", W / 2, 820, 80, fundo=CERTO, a=a))
    E.frase(c, t, C["s11.f"], [("positivo:", "g", 58, CERTO)] + ps("do potencial maior para o menor", "i", 60), W / 2, 980, "center", 0.1)


# ---------------- questão 5: capacitor ----------------
def b_q5(c, t, C, b):
    if t < C["s13"]:
        titulo_q(c, t, C["s12"], 5)
        E.foco(c, t, C["s12.a"], 0.5, lambda a: (E.escreve(c, "C =", XE, 360, 80, "g", TINTA, a), F.medida(c, 10, "µF", XE + 160, 360, 80, COR, a)))
        E.foco(c, t, C["s12.b"], 0.5, lambda a: (E.escreve(c, "U =", XE, 490, 80, "g", TINTA, a), F.medida(c, 200, "V", XE + 160, 490, 80, COR, a)))
        E.frase(c, t, C["s12.c"], [("energia", "i", 76), ("guardada?", "g", 72, COR)], XE, 660, passo=0.12)
        E.frase(c, t, C["s12.d"], [("e", "i", 76), ("com", "i", 76), ("U", "g", 72), ("÷", "g", 72, COR), ("2?", "g", 72, COR)], XE, 790, passo=0.12)
        pausa_ou(c, t, C["s12.e"], lambda: E.foco(c, t, C["s12.a"], 0.5, lambda a: capacitor(c, 1320, 1600, 300, 760, a)))
        return
    E.formula_em(c, t, C["s13.a"], "Q = C · U = 10 × 10^{−6} · 200", XE, 240, 80, "g", TINTA)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: pilula_f(c, "Q = 2 × 10^{−3} C", 1500, 395, 66, a=a))
    E.formula_em(c, t, C["s13.c"], "energia = f{Q · U}{2} = f{2 × 10^{−3} · 200}{2}", XE, 560, 76, "g", TINTA)
    E.foco(c, t, C["s13.d"], 0.5, lambda a: pilula_f(c, "0,2 J", 1640, 540, 76, fundo=CERTO, a=a))
    E.formula_em(c, t, C["s13.e"], "U ÷ 2  →  energia ÷ 4", XE, 800, 80, "g", TINTA)
    E.foco(c, t, C["s13.e"] + 1.4, 0.4, lambda a: E.escreve(c, "a energia tem U²", XE, 880, 52, "b", TINTA2, a))
    E.foco(c, t, C["s13.f"], 0.5, lambda a: pilula_f(c, "0,05 J", 1500, 775, 76, fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela():
        resumo(c, t, C, "s14", (("s14.a", [("o", "i", 70), ("que", "i", 70), ("a", "i", 70), ("questão", "i", 70), ("pede?", "g", 66, COR)]),
                                ("s14.b", [("a", "i", 70), ("fórmula", "g", 66), ("com", "i", 70), ("isso", "i", 70), ("e", "i", 70), ("os", "i", 70), ("dados", "g", 66)]),
                                ("s14.c", [("proporção", "g", 66, COR), ("sempre", "i", 70), ("que", "i", 70), ("der", "i", 70)])))
    E.saida(c, t, C["s14.d"] - 0.6, tela)
    if t < C["s14.d"] - 0.6:
        return
    E.frase(c, t, C["s14.d"] - 0.5, [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s14.d"], [("corrente", "g", 120, COR), ("elétrica", "g", 120, COR)], XE, 410)
    y = 760
    F.fio(c, t, C["s14.d"] + 0.3, [(300, y), (1000, y)])
    F.corrente(c, t, C["s14.d"] + 0.8, [(300, y), (1000, y)], fecha=False)
    for i in range(4):
        x = 360 + ((t - C["s14.d"]) * 120 * -1 + i * 170) % 640
        q(c, x, y + 50, 18, "−", ep(t, C["s14.d"] + 0.8, 0.4))
    E.foco(c, t, C["s14.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s14.e"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s14.e"] + 0.2, 0.4))
    E.frase(c, t, C["s14.f"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1580, 990, "center")


BLOCKS = dict(gancho=b_gancho, metodo=b_metodo, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5, fim=b_fim)
