"""Visual — Estudativo · MAT-POT-002: potência de negativo, fração ou decimal.
Identidade em _ferramentas/editorial.py. Peças desta aula: camiseta que desbota a cada lavagem (a cor é a própria potência),
escada da ordem das operações e os pares de menos do atalho. Expoente sempre com E.formula."""
from fractions import Fraction as Fr

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, sinal, palco, centro
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-002_potencia_de_negativo_fracao_decimal.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("negativo", "fracao", "ordem", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert (-3) ** 2 == 9 and -3 ** 2 == -9 and (-2) ** 3 == -8 and (-1) ** 25 == -1 and Fr(2, 3) ** 3 == Fr(8, 27)
assert Fr(3, 10) ** 2 == Fr(9, 100) and 2 + 3 * 2 ** 2 == 14 and (2 + 3) * 2 ** 2 == 20 and 2 + (3 * 2) ** 2 == 38
assert 10 - 2 * (-3) ** 2 == -8 and (10 - 2) * (-3) ** 2 == 72


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


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    """número dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def fm(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, cor=cor, align=align)


def fl(c, t, partes, x, y, size, align="left", gap=None):
    """linha de fórmulas em que cada parte entra no seu instante: partes = [(escrita, cor, t0), ...]; devolve o x e a largura de cada uma"""
    gap = size * 0.2 if gap is None else gap
    ws = [E.formula(None, p[0], 0, 0, size, a=0) for p in partes]
    tot = sum(ws) + gap * (len(ws) - 1)
    xx = x - tot / 2 if align == "center" else x
    xs = []
    for p, w in zip(partes, ws):
        fm(c, t, p[2], p[0], xx, y, size, p[1])
        xs.append(xx)
        xx += w + gap
    return xs, ws


def camiseta(c, cx, cy, s, cor, a=1.0):
    """camiseta vista de frente, centrada em (cx, cy), com contorno fixo: só a cor muda"""
    if a <= 0:
        return
    p = skia.Path()
    k = s / 100
    pts = ((-34, -92), (-14, -80), (14, -80), (34, -92), (100, -48), (76, -6), (50, -24), (50, 92), (-50, 92), (-50, -24), (-76, -6), (-100, -48))
    p.moveTo(cx + pts[0][0] * k, cy + pts[0][1] * k)
    for x, y in pts[1:]:
        p.lineTo(cx + x * k, cy + y * k)
    p.close()
    c.drawPath(p, M.paint(cor, a))
    tinta = M.paint(TINTA, a, stroke=4)
    tinta.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, tinta)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s01.{k}"] for k in "abcd")

    def conta():
        s = 220
        fm(c, t, a_, "(−3)^2", 300, 390, s)
        sinal(c, t, b_ - 0.1, "=", 1010, 310, 170)
        E.foco(c, t, b_, 0.5, lambda q: num_bola(c, "9", 1330, 305, 150, 170, q))
        fm(c, t, c_, "−3^2", 400, 740, s)
        sinal(c, t, d_ - 0.1, "=", 1010, 660, 170)
        E.foco(c, t, d_, 0.5, lambda q: num_bola(c, "−9", 1330, 655, 150, 150, q, ERRADO, BR))
        E.frase(c, t, lerp(d_, C["s01.end"], 0.3), ps("um par de parênteses", "i", 80) + ps("troca o sinal", "g", 74, COR), W / 2, 960, "center", 0.16)
    E.saida(c, t, C["s02"] - 0.1, conta)

    if t >= C["s02"]:
        a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]
        E.frase(c, t, a2, ps("até o fim desta aula", "i", 92), XE, 240)
        fl(c, t, [("(−2)^3", COR, lerp(a2, b2, 0.35)), ("(f{2}{3})^3", COR, lerp(a2, b2, 0.55)), ("0,3^2", COR, lerp(a2, b2, 0.75))], XE, 480, 140, gap=100)
        E.frase(c, t, b2, ps("a potência", "i", 96) + ps("na ordem", "g", 96, COR) + ps("das operações", "i", 96), XE, 730)
        E.foco(c, t, c2 - 0.1, 0.6, lambda a: E.bola(c, 1530, 300, 200 * ease_back(prog(t, c2 - 0.1, 0.6))), blur=0)
        E.foco(c, t, c2 + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1530, 295, 76, "g", E.SOBRE, a), centro(c, "de prova", 1530, 375, 76, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_ = C["s03.a"]
    E.frase(c, t, C["s03"] + 0.1, ps("lembre de", "i", 96), XE, 410)
    E.foco(c, t, a_, 0.5, lambda p: E.escreve(c, "4", XE - 8, 720, 340, "g", COR, p))
    E.foco(c, t, a_ + 0.15, 0.5, lambda p: E.escreve(c, "coisas", XE + 235, 700, 120, "i", TINTA, p))
    x, w = 880, 860
    for i, (k, s) in enumerate((("s03.b", "o que é potência"), ("s03.c", "a regra de sinais"), ("s03.d", "multiplicar frações"), ("s03.e", "multiplicar decimais"))):
        y = 180 + i * 165
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 134, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(s, "g", 62, COR)], x + 44, y + 90)
    E.frase(c, t, lerp(C["s03.e"], C["s03.end"], 0.6), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), XE, 880, passo=0.15)


# ---------------- base negativa ----------------
def b_negativo(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    E.frase(c, t, a4, ps("o expoente diz", "i", 84) + ps("quantas vezes a base aparece", "g", 62, COR), XE, 170, passo=0.15)
    y = 420
    fm(c, t, b4, "(−2)^3", XE, y, 190)
    E.frase(c, t, b4 + 0.5, ps("base negativa", "i", 64, COR), XE, 500, passo=0.15)
    sinal(c, t, c4 - 0.1, "=", 800, y - 55, 110)
    fl(c, t, [("(−2)", None, c4), ("×", None, c4 + 0.6), ("(−2)", None, c4 + 0.7), ("×", None, c4 + 1.3), ("(−2)", None, c4 + 1.4)], 880, y - 10, 104)
    y1, y2 = 700, 890
    fm(c, t, a5, "(−2) × (−2)", XE, y1, 110)
    E.foco(c, t, a5 + 0.5, 0.45, lambda p: E.pilula(c, "sinais iguais", 980, y1 - 40, 54, estilo="b", a=p, cor=E.SOBRE))
    fm(c, t, a5 + 1.5, "= +4", 1250, y1, 120, COR)
    fm(c, t, b5, "+4 × (−2)", XE, y2, 110)
    E.foco(c, t, b5 + 0.4, 0.45, lambda p: E.pilula(c, "sinais diferentes", 980, y2 - 40, 54, estilo="b", fundo=TINTA, a=p, cor=BR))
    fm(c, t, c5 - 0.1, "=", 1250, y2, 120)
    E.foco(c, t, c5, 0.5, lambda q: num_bola(c, "−8", 1490, y2 - 42, 110, 104, q, CERTO, BR))


# ---------------- com e sem parênteses ----------------
def b_parenteses(c, t, C, b):
    def colunas():
        a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
        a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
        xa, xb = 190, 1040
        y = 330
        fm(c, t, a6, "(−3)^2", xa, y, 190)
        E.frase(c, t, lerp(a6, b6, 0.6), ps("a base é o", "i", 72) + ps("−3 inteiro", "g", 68, COR), xa, 470, passo=0.14)
        fm(c, t, b6, "(−3) × (−3)", xa, 640, 104)
        E.frase(c, t, lerp(b6, c6, 0.5), ps("sinais iguais", "i", 72), xa, 760, passo=0.14)
        E.foco(c, t, c6, 0.5, lambda q: num_bola(c, "+9", xa + 170, 880, 100, 100, q, CERTO, BR))
        M.line(c, 960, 170, 960, 980, FIO, ep(t, a7, 0.5), 3)
        E.foco(c, t, a7, 0.5, lambda q: E.formula(c, "−", xb, y, 190, cor=ERRADO if t >= lerp(b7, c7, 0.3) else TINTA, a=q))
        wm = E.formula(None, "−", 0, 0, 190, a=0)
        E.foco(c, t, a7, 0.5, lambda q: E.formula(c, "3^2", xb + wm, y, 190, cor=COR if t >= b7 else TINTA, a=q))
        q = ep(t, b7, 0.45)
        E.caixa_pontilhada(c, xb + wm - 14, y - 180, 250, 210, q, COR, prog_=q)
        E.frase(c, t, lerp(b7, c7, 0.3), ps("o menos", "g", 68, ERRADO) + ps("fica de fora", "i", 72), xb, 470, passo=0.14)
        fm(c, t, c7, "3 × 3 = 9", xb, 640, 104)
        E.frase(c, t, lerp(c7, d7, 0.5), ps("depois, entra o menos", "i", 72), xb, 760, passo=0.14)
        E.foco(c, t, d7, 0.5, lambda q: num_bola(c, "−9", xb + 170, 880, 100, 100, q, ERRADO, BR))
    E.saida(c, t, C["s08"] - 0.1, colunas)

    if t >= C["s08"]:
        a, b_ = C["s08.a"], C["s08.b"]
        E.frase(c, t, C["s08"] + 0.1, ps("o menos do começo", "i", 84), XE, 210)
        E.frase(c, t, lerp(C["s08"], a, 0.5), ps("é um", "i", 84) + ps("sinal colado", "g", 80, COR), XE, 320)
        E.frase(c, t, a, ps("mas a", "i", 92) + ps("potência", "g", 88, COR) + ps("vem antes dele", "i", 92), XE, 560)
        fm(c, t, a + 0.5, "−3^2", 1320, 340, 150)
        E.frase(c, t, lerp(a, b_, 0.65), ps("para o menos entrar na potência:", "i", 72), XE, 720, passo=0.14)
        E.frase(c, t, b_, ps("só com", "i", 92) + ps("parênteses", "g", 88, COR), XE, 850)
        fm(c, t, b_ + 0.4, "(−3)^2", 1180, 860, 150, COR)


# ---------------- fração ----------------
def b_fracao(c, t, C, b):
    def s09():
        a, b_, c_ = C["s09.a"], C["s09.b"], C["s09.c"]
        E.frase(c, t, C["s09"] + 0.1, ps("e com fração?", "i", 80, COR), XE, 130)
        xs, y, s = (290, 720, 1150, 1580), 340, 150
        tons = [Fr(2, 3) ** i for i in range(4)]
        ts = [a - 0.3, a + 0.5, lerp(b_, c_, 0.25), lerp(b_, c_, 0.5)]
        for i, (x, ton, ti) in enumerate(zip(xs, tons, ts)):
            E.foco(c, t, ti, 0.45, lambda q, x=x, ton=ton: camiseta(c, x, y, s, M.mix(BR, E.COR, float(ton)), q))
            if i:
                q = ep(t, ti, 0.4)
                if q > 0:
                    M.arrow(c, xs[i - 1] + 170, y, x - 170, y, TINTA, q, 4, 16, q)
                E.foco(c, t, ti, 0.45, lambda q, i=i, x=x: centro(c, f"{i}ª lavagem", x, y + 215, 46, "m", TINTA2, q))
        yr = 800
        fl(c, t, [("f{2}{3}", COR, a + 0.5), ("de", TINTA2, ts[2] - 0.05), ("f{2}{3}", COR, ts[2]), ("de", TINTA2, ts[3] - 0.05), ("f{2}{3}", COR, ts[3])], XE, yr, 120, gap=36)
        E.frase(c, t, lerp(ts[3], c_, 0.55), ps("de", "g", 66, COR) + ps("significa vezes", "i", 72), XE, 1000, passo=0.14)
        fm(c, t, c_, "= (f{2}{3})^3", 1050, yr, 170)
    E.saida(c, t, C["s10"] - 0.1, s09)

    if t >= C["s10"]:
        a, b_, c_, d, e = (C[f"s10.{k}"] for k in "abcde")
        y = 280
        fm(c, t, C["s10"] + 0.1, "(f{2}{3})^3", XE, y, 150)
        fl(c, t, [("=", None, a), ("f{2}{3}", None, a + 0.1), ("×", None, a + 0.3), ("f{2}{3}", None, a + 0.4), ("×", None, a + 0.6), ("f{2}{3}", None, a + 0.7)], 520, y, 130)
        E.frase(c, t, a + 0.9, ps("a fração", "i", 64) + ps("inteira", "g", 60, COR), 1270, y - 60, passo=0.13)
        E.frase(c, t, a + 1.2, ps("se repete", "i", 64), 1270, y + 20, passo=0.13)
        fl(c, t, [("2 × 2 × 2", None, b_), ("=", None, b_ + 0.9), ("8", COR, b_ + 1.0)], XE, 570, 120)
        fl(c, t, [("3 × 3 × 3", None, c_), ("=", None, c_ + 0.9), ("27", COR, c_ + 1.0)], XE, 730, 120)
        E.frase(c, t, b_ + 0.3, ps("os de cima", "i", 60, TINTA2), 940, 555, passo=0.12)
        E.frase(c, t, c_ + 0.3, ps("os de baixo", "i", 60, TINTA2), 940, 715, passo=0.12)
        E.resultado(c, t, d, 8, 27, 1500, 610, 120, 170, CERTO)
        E.frase(c, t, e, ps("o expoente vale para", "i", 76) + ps("o de cima", "g", 70, COR) + ps("e para", "i", 76) + ps("o de baixo", "g", 70, COR), W / 2, 930, "center", 0.15)


# ---------------- decimal ----------------
def b_decimal(c, t, C, b):
    a, b_, c_, d, e = (C[f"s11.{k}"] for k in "abcde")
    E.frase(c, t, C["s11"] + 0.1, ps("e com decimal?", "i", 80, COR), XE, 150)
    y = 340
    fm(c, t, a, "0,3^2", XE, y, 180)
    fl(c, t, [("=", None, b_ - 0.1), ("0,3 × 0,3", None, b_)], 700, y - 15, 130)
    E.frase(c, t, c_ - 0.8, ps("ignore as vírgulas:", "i", 76), XE, 560, passo=0.14)
    fm(c, t, c_, "3 × 3 = 9", 870, 570, 120)
    E.frase(c, t, d - 0.6, ps("conte as casas:", "i", 76), XE, 730, passo=0.14)
    fm(c, t, d, "1 + 1 = 2", 870, 740, 120)
    E.foco(c, t, d + 0.6, 0.45, lambda p: E.escreve(c, "casas", 1400, 740, 76, "i", TINTA2, p))
    E.frase(c, t, e - 0.3, ps("9 com 2 casas:", "i", 76), XE, 930, passo=0.14)
    E.foco(c, t, e, 0.5, lambda q: num_bola(c, "0,09", 1100, 900, 120, 76, q, CERTO, BR))


# ---------------- ordem ----------------
def b_ordem(c, t, C, b):
    a2, b2 = C["s12.a"], C["s12.b"]

    def s12():
        E.frase(c, t, C["s12"] + 0.1, ps("onde entra a potência?", "i", 88, COR), W / 2, 180, "center", 0.15)
        y1, y2 = 470, 730
        fm(c, t, a2, "2 + 2 + 2", 340, y1, 130)
        E.ponte(c, t, a2 + 0.4, 960, 1190, y1 - 45, "pacote", size=40)
        fm(c, t, a2 + 0.8, "3 × 2", 1260, y1, 130, COR)
        fm(c, t, b2, "2 × 2 × 2", 340, y2, 130)
        E.ponte(c, t, b2 + 0.4, 960, 1190, y2 - 45, "pacote", size=40)
        fm(c, t, b2 + 0.8, "2^3", 1260, y2, 130, COR)
        E.frase(c, t, lerp(b2, C["s12.end"], 0.45), ps("primeiro, os", "i", 76) + ps("pacotes", "g", 72, COR), W / 2, 930, "center", 0.15)
    E.saida(c, t, C["s13"] - 0.1, s12)

    if C["s13"] <= t < C["s14"] + 0.4:
        a, b_, c_, d, e = (C[f"s13.{k}"] for k in "abcde")

        def s13():
            E.frase(c, t, C["s13"] + 0.1, ps("a ordem", "g", 96, COR), XE, 170)
            itens = ((a, "parênteses", TINTA), (b_, "potência", COR), (c_, "vezes e dividido", TINTA), (d, "mais e menos", TINTA))
            for i, (k, s, cor) in enumerate(itens):
                x, y = XE + 40 + i * 150, 320 + i * 185
                E.foco(c, t, k, 0.45, lambda q, i=i, x=x, y=y: num_bola(c, str(i + 1), x, y, 58, 66, q))
                E.frase(c, t, k + 0.1, [(s, "g", 92, cor)], x + 86, y + 32)
            q = ep(t, e, 0.5)
            E.caixa_pontilhada(c, XE + 124, 424, 560, 146, q, COR, prog_=q)
            E.frase(c, t, e, ps("antes do", "i", 80) + ps("vezes", "g", 76, COR), 1040, 505)
        E.saida(c, t, C["s14"] - 0.1, s13)

    if C["s14"] <= t < C["s15"] + 0.4:
        a, b_, c_, d, e = (C[f"s14.{k}"] for k in "abcde")

        def s14():
            X, s = XE, 124
            E.foco(c, t, a, 0.5, lambda q: E.formula(c, "2 + 3 × ", X, 240, s, a=q))
            wp = E.formula(None, "2 + 3 × ", 0, 0, s, a=0)
            E.foco(c, t, a, 0.5, lambda q: E.formula(c, "2^2", X + wp, 240, s, cor=COR if t >= b_ else TINTA, a=q))
            fm(c, t, lerp(b_, c_, 0.55), "2 + 3 × 4", X, 450, s)
            fm(c, t, lerp(c_, d, 0.55), "2 + 12", X, 660, s)
            fl(c, t, [("=", None, e - 0.1)], X, 870, s)
            E.foco(c, t, e, 0.5, lambda q: num_bola(c, "14", X + 240, 830, 115, 112, q, CERTO, BR))
            R = 1000
            E.frase(c, t, b_, ps("primeiro a", "i", 72) + ps("potência", "g", 68, COR), R, 200, passo=0.14)
            fm(c, t, b_ + 0.5, "2^2 = 4", R, 320, 104, COR)
            E.frase(c, t, c_, ps("depois o", "i", 72) + ps("vezes", "g", 68, COR), R, 480, passo=0.14)
            fm(c, t, c_ + 0.4, "3 × 4 = 12", R, 600, 104, COR)
            E.frase(c, t, d, ps("por último", "i", 72), R, 760, passo=0.14)
            fm(c, t, d + 0.4, "2 + 12", R, 880, 104, COR)
        E.saida(c, t, C["s15"] - 0.1, s14)

    if t >= C["s15"]:
        a, b_, c_ = C["s15.a"], C["s15.b"], C["s15.c"]
        fm(c, t, C["s15"] + 0.1, "(2 + 3) × 2^2 = 5 × 4 =", XE, 300, 100)
        E.frase(c, t, C["s15"] + 0.1, ps("quem soma primeiro", "i", 76), XE, 170, passo=0.14)
        E.foco(c, t, a, 0.5, lambda q: num_bola(c, "20", 1500, 262, 100, 92, q, ERRADO, BR))
        E.frase(c, t, b_, ps("quem faz", "i", 76) + ps("3 × 2", "g", 70) + ps("antes do expoente", "i", 76), XE, 520, passo=0.14)
        fm(c, t, b_ + 1.0, "2 + (3 × 2)^2 = 2 + 36 =", XE, 650, 100)
        E.foco(c, t, c_, 0.5, lambda q: num_bola(c, "38", 1500, 612, 100, 92, q, ERRADO, BR))
        E.frase(c, t, lerp(c_, C["s15.end"], 0.4), ps("saiu da ordem,", "i", 92) + ps("saiu da resposta", "g", 86, ERRADO), W / 2, 900, "center", 0.17)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_, d, e = (C[f"s16.{k}"] for k in "abcde")
    y0 = 240
    fm(c, t, a, "0,3^2 = 0,9", XE, y0, 130, ERRADO)
    if t >= lerp(a, b_, 0.7):
        E.risco(c, XE - 16, y0 + 14, XE + 690, y0 - 90, t, lerp(a, b_, 0.7), largura=12)
    E.frase(c, t, b_, ps("3 × 3 dá 9, mas", "i", 72) + ps("conta uma casa só", "g", 66, ERRADO), XE, 350, passo=0.13)
    x0, x1, yr = 300, 1620, 660
    tr = lerp(b_, c_, 0.75)
    vx = E.reta(c, t, tr, x0, x1, yr, 0, 1, [0, 0.09, 0.3, 0.9, 1], lambda v: {0: "0", 1: "1"}.get(v, f"{v}".replace(".", ",")), tm=[tr, d, tr, tr, tr], size=54)
    E.frase(c, t, c_, ps("o resultado fica", "i", 76) + ps("menor que 0,3", "g", 70, COR), XE, 460, passo=0.15)
    E.foco(c, t, c_ + 0.3, 0.45, lambda q: E.pilula(c, "aqui, não", vx(0.9), yr - 90, 48, estilo="b", fundo=ERRADO, cor=BR, a=q))
    E.foco(c, t, d, 0.45, lambda q: E.pilula(c, "aqui, sim", vx(0.09) + 60, yr - 90, 48, estilo="b", fundo=CERTO, cor=BR, a=q))
    E.frase(c, t, e, ps("base entre", "i", 80) + ps("0 e 1:", "g", 74, COR) + ps("o número", "i", 80) + ps("diminui", "g", 74, COR), W / 2, 880, "center", 0.15)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s17():
        a, b_, c_ = C["s17.a"], C["s17.b"], C["s17.c"]
        E.frase(c, t, C["s17"] + 0.1, ps("agora, o atalho", "i", 80, CLARO), W / 2, 200, "center")
        E.frase(c, t, a, ps("olhe o expoente", "g", 110, BR), W / 2, 350, "center")
        E.frase(c, t, a + 0.8, ps("antes de fazer conta", "i", 92, CLARO), W / 2, 460, "center", 0.15)
        E.foco(c, t, b_ - 0.4, 0.45, lambda q: centro(c, "base negativa", W / 2, 590, 60, "i", CLARO, q))
        E.frase(c, t, b_, ps("expoente par", "i", 92, CLARO), XE + 10, 730)
        E.frase(c, t, b_ + 0.5, ps("positivo", "g", 116, BR), XE + 10, 870)
        E.frase(c, t, c_, ps("expoente ímpar", "i", 92, CLARO), 1010, 730)
        E.frase(c, t, c_ + 0.5, ps("negativo", "g", 116, BR), 1010, 870)
    E.saida(c, t, C["s18"] - 0.1, s17)

    if C["s18"] <= t < C["s19"] + 0.4:
        a, b_, c_ = C["s18.a"], C["s18.b"], C["s18.c"]

        def s18():
            fm(c, t, a, "(−1)^{25}", 330, 520, 240, BR)
            E.frase(c, t, b_, ps("25", "g", 100, CLARO) + ps("é ímpar", "i", 100, CLARO), 1060, 390)
            E.foco(c, t, c_, 0.5, lambda q: num_bola(c, "−1", 1300, 610, 150, 130, q, CERTO, BR))
            E.frase(c, t, lerp(c_, C["s18.end"], 0.45), ps("nenhuma conta", "g", 100, BR), W / 2, 900, "center")
        E.saida(c, t, C["s19"] - 0.1, s18)

    if t >= C["s19"]:
        a, b_, c_ = C["s19.a"], C["s19.b"], C["s19.c"]
        E.frase(c, t, C["s19"] + 0.1, ps("por que funciona?", "i", 80, CLARO), W / 2, 150, "center")
        y, x0, dx, r = 360, 420, 270, 80
        for i in range(5):
            x = x0 + i * dx
            cor = ERRADO if i == 4 and t >= b_ else E.COR
            E.foco(c, t, a + i * 0.12, 0.4, lambda q, x=x, cor=cor: num_bola(c, "−", x, y, r, 96, q, cor, BR))
        for i, ti in ((0, a + 0.6), (2, a + 1.1)):
            q = ep(t, ti, 0.4)
            E.chave(c, x0 + i * dx - r, x0 + (i + 1) * dx + r, y + r + 16, CLARO, q, 26, 6, abre=False)
            E.foco(c, t, ti + 0.1, 0.4, lambda p, i=i: centro(c, "+", x0 + (i + 0.5) * dx, y + r + 120, 96, "g", BR, p))
        E.foco(c, t, b_, 0.45, lambda p: centro(c, "sobra um", x0 + 4 * dx, y + r + 112, 66, "g", BR, p))
        E.frase(c, t, c_, ps("só vale com o menos", "i", 84, CLARO) + ps("dentro do parêntese", "g", 76, BR), W / 2, 760, "center", 0.15)
        E.frase(c, t, lerp(c_, C["s19.end"], 0.55), ps("base positiva:", "i", 84, CLARO) + ps("não compensa", "g", 76, ERRADO), W / 2, 900, "center", 0.15)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_ = C["s20.a"], C["s20.b"]
    E.frase(c, t, C["s20"] + 0.1, ps("hora de testar", "i", 76, COR), XE, 240)
    fl(c, t, [("10 − 2 ×", None, a), ("(−3)^2", COR, b_)], XE, 560, 150)
    E.relogio(c, t, C["s21.a"], 1510, 440, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_, d = (C[f"s22.{k}"] for k in "abcd")
    X, s = XE, 124
    wp = E.formula(None, "10 − 2 × ", 0, 0, s, a=0)
    E.foco(c, t, C["s22"] + 0.1, 0.5, lambda q: E.formula(c, "10 − 2 × ", X, 240, s, a=q))
    E.foco(c, t, C["s22"] + 0.1, 0.5, lambda q: E.formula(c, "(−3)^2", X + wp, 240, s, cor=COR if t >= lerp(C["s22"], a, 0.4) else TINTA, a=q))
    fm(c, t, a + 0.3, "= 10 − 2 × 9", X, 420, s)
    fm(c, t, b_ + 0.5, "= 10 − 18", X, 600, s)
    fl(c, t, [("=", None, d - 0.1)], X, 780, s)
    E.foco(c, t, d, 0.5, lambda q: num_bola(c, "−8", X + 240, 740, 115, 100, q, CERTO, BR))
    R = 1080
    E.frase(c, t, a - 0.6, ps("a potência primeiro:", "i", 66), R, 200, passo=0.13)
    fm(c, t, a, "(−3)^2 = +9", R, 310, 100, COR)
    E.frase(c, t, b_ - 0.5, ps("depois o vezes:", "i", 66), R, 460, passo=0.13)
    fm(c, t, b_, "2 × 9 = 18", R, 570, 100, COR)
    E.frase(c, t, c_, ps("por último:", "i", 66), R, 720, passo=0.13)
    fm(c, t, c_ + 0.4, "10 − 18", R, 830, 100, COR)
    tq = lerp(d, C["s22.end"], 0.45)
    E.frase(c, t, tq, ps("começou por", "i", 72, ERRADO), XE, 980, passo=0.13)
    fm(c, t, tq + 0.4, "10 − 2 = 8", 620, 985, 78, ERRADO)
    fm(c, t, tq + 0.9, "8 × 9 = 72", 1100, 985, 78, ERRADO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a, b_ = C["s23.a"], C["s23.b"]

    def resumo():
        E.frase(c, t, C["s23"] + 0.1, ps("resumindo", "i", 92, COR), W / 2, 190, "center")
        E.foco(c, t, a, 0.5, lambda p: num_bola(c, "1", 220, 372, 56, 64, p))
        E.frase(c, t, a + 0.1, ps("o parêntese decide", "i", 84) + ps("quem é a base", "g", 78, COR), 310, 400, passo=0.15)
        fl(c, t, [("(−3)^2", None, a + 0.8), ("−3^2", None, a + 1.0)], 310, 570, 110, gap=140)
        E.foco(c, t, b_, 0.5, lambda p: num_bola(c, "2", 220, 732, 56, 64, p))
        E.frase(c, t, b_ + 0.1, ps("a potência vem", "i", 84) + ps("antes do vezes", "g", 78, COR), 310, 760, passo=0.15)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    a2, b2, c2, d2 = (C[f"s24.{k}"] for k in "abcd")
    E.frase(c, t, C["s24"] + 0.2, ps("próxima aula", "i", 84), XE, 200)
    E.frase(c, t, a2, ps("mesma base", "g", 110, COR), XE, 340)
    fm(c, t, a2 + 0.8, "2^3 · 2^4", XE, 490, 120, COR)
    E.frase(c, t, b2, ps("por que", "i", 92), XE, 650)
    fm(c, t, b2 + 0.3, "7^0 = 1", 470, 660, 120, COR)
    E.foco(c, t, c2, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1450, 360, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c2 + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1590, p), lerp(650, 400, p), ep(t, c2 + 0.2, 0.4), TINTA)
    E.frase(c, t, d2, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 890, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, negativo=b_negativo, parenteses=b_parenteses, fracao=b_fracao, decimal=b_decimal,
              ordem=b_ordem, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
