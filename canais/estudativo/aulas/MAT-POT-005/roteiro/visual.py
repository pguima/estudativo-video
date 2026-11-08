"""Visual — Estudativo · MAT-POT-005: expoente negativo e potências de 10.
Identidade em _ferramentas/editorial.py. Peças desta aula: fração de dois andares com os dois cortados, escada que desce de 8 a 1/8
e a vírgula que anda com E.anda. Expoente sempre com E.formula."""
from fractions import Fraction as Fr

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, sinal, palco, centro
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-005_expoente_negativo_potencias_de_10.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("divisao", "escada", "dez", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert Fr(2) ** -3 == Fr(1, 8) == Fr(2 ** 3, 2 ** 6) and Fr(3) ** -2 == Fr(1, 9) and Fr(5 ** 3, 5 ** 5) == Fr(1, 25)
assert Fr(10) ** -3 == Fr(1, 1000) and Fr(10) ** -2 == Fr(1, 100) and Fr(10) ** -6 == Fr(1, 10 ** 6) and Fr(10) ** -5 == Fr(1, 10 ** 5)
DEGRAUS = [("8", "2^3"), ("4", "2^2"), ("2", "2^1"), ("1", "2^0"), ("f{1}{2}", "2^{−1}"), ("f{1}{4}", "2^{−2}"), ("f{1}{8}", "2^{−3}")]


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
    """número ou fórmula dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    E.formula(c, s, cx, cy + size * 0.36, size, cor=tinta or E.SOBRE, a=a, align="center")


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


def corrente(c, t, ti, tf, n, cx, y, size, sai=None):
    """2 × 2 × ... centrado em cx, termo a termo de ti a tf; sai = instante em que os três primeiros são riscados"""
    partes = []
    for i in range(n):
        q = lerp(ti, tf, i / n)
        if i:
            partes.append(("×", None, q - 0.03))
        partes.append(("2", None, q))
    xs, ws = fl(c, t, partes, cx, y, size, "center", gap=size * 0.16)
    if sai is not None and t >= sai:
        for i in range(3):
            j = 2 * i
            E.risco(c, xs[j] - 6, y + 10, xs[j] + ws[j] + 6, y - size * 0.8, t, sai + i * 0.1, largura=9)
    return xs, ws


def degrau_desce(c, t, i, ti, x0=190, pw=220, y0=170, dy=100, chao=985):
    """degrau i da escada que desce: o valor em cima e a potência embaixo"""
    v, p = DEGRAUS[i]
    yi, xi = y0 + i * dy, x0 + i * pw

    def fn(a):
        M.rrect(c, xi + 4, yi, pw - 8, chao - yi, 10, E.COR if i < 4 else TINTA, a)
        E.formula(c, v, xi + pw / 2, yi + (84 if i < 4 else 92), 76 if i < 4 else 62, cor=BR, a=a, align="center")
        E.formula(c, p, xi + pw / 2, yi + (160 if i < 4 else 186), 56 if i < 4 else 50, cor=BR, a=a, align="center")
    E.foco(c, t, ti, 0.45, fn, sobe=26)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def conta():
        y = 600
        fm(c, t, a_, "2^{−3}", 200, y, 300)
        sinal(c, t, b_ - 0.15, "=", 830, y - 100, 190)
        E.foco(c, t, b_, 0.5, lambda a: E.formula(c, "−8", 1110, y, 260, cor=ERRADO, a=a, align="center"))
        if t >= lerp(b_, c_, 0.5):
            E.risco(c, 930, y + 40, 1310, y - 220, t, lerp(b_, c_, 0.5), largura=20)
        E.foco(c, t, c_, 0.5, lambda a: num_bola(c, "f{1}{8}", 1560, y - 100, 190, 150, a, CERTO, BR))
        E.frase(c, t, lerp(b_, c_, 0.55), ps("nem é", "i", 92) + ps("negativo", "g", 84, ERRADO), W / 2, 880, "center")
    E.saida(c, t, C["s02"] - 0.1, conta)

    if t >= C["s02"]:
        a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]
        E.frase(c, t, a2, ps("até o fim desta aula", "i", 92), XE, 240)
        E.frase(c, t, lerp(a2, b2, 0.4), ps("expoente negativo", "g", 84, COR) + ps("vira fração", "i", 92), XE, 370, passo=0.16)
        fm(c, t, lerp(a2, b2, 0.7), "2^{−3} = f{1}{8}", XE, 530, 110, COR)
        E.frase(c, t, b2, ps("potências de 10:", "g", 84, COR) + ps("zeros e casas", "i", 92), XE, 720, passo=0.16)
        fm(c, t, b2 + 1.0, "10^{−3} = 0,001", XE, 880, 110, COR)
        E.foco(c, t, c2 - 0.1, 0.6, lambda a: E.bola(c, 1540, 760, 200 * ease_back(prog(t, c2 - 0.1, 0.6))), blur=0)
        E.foco(c, t, c2 + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1540, 750, 76, "g", E.SOBRE, a), centro(c, "de prova", 1540, 830, 76, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_ = C["s03.a"]
    E.frase(c, t, C["s03"] + 0.1, ps("lembre de", "i", 96), XE, 410)
    E.foco(c, t, a_, 0.5, lambda p: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, p))
    E.foco(c, t, a_ + 0.15, 0.5, lambda p: E.escreve(c, "coisas", XE + 235, 700, 120, "i", TINTA, p))
    x, w = 850, 900
    itens = (("s03.b", "mesma base, dividindo:", "subtrai os expoentes"), ("s03.c", "o traço da fração", "é uma divisão"), ("s03.d", "andar com", "a vírgula"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 232
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.6), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), W / 2, 960, "center", 0.15)


# ---------------- sai da divisão ----------------
def b_divisao(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5 = (C[f"s05.{k}"] for k in "abc")

    def s04_05():
        E.frase(c, t, C["s04"] + 0.1, ps("de onde vem um expoente negativo?", "i", 84), XE, 190, passo=0.13)
        E.frase(c, t, a4, ps("da divisão", "g", 110, COR), XE, 330)
        E.frase(c, t, lerp(a4, b4, 0.35), ps("o primeiro expoente nunca era menor:", "i", 66, TINTA2), XE, 440, passo=0.11)
        fm(c, t, b4, "2^3 ÷ 2^6", XE, 660, 170)
        E.frase(c, t, a5, ps("repete a base", "g", 72, COR) + ps("e subtrai", "i", 80), 900, 560, passo=0.15)
        fl(c, t, [("3 − 6 =", None, lerp(a5, b5, 0.6)), ("−3", COR, b5)], 900, 680, 120)
        fl(c, t, [("=", None, c5 - 0.1), ("2^{−3}", COR, c5)], XE, 890, 170)
        E.frase(c, t, lerp(c5, C["s05.end"], 0.45), ps("mas o que isso quer dizer?", "i", 76), 830, 860, passo=0.13)
    E.saida(c, t, C["s06"] - 0.1, s04_05)

    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")

    def s06_07():
        E.frase(c, t, C["s06"] + 0.1, ps("o traço é divisão", "i", 76, COR), XE, 150)
        fm(c, t, a6, "f{2^3}{2^6}", XE + 20, 470, 170)
        fm(c, t, a6 + 0.2, "=", 460, 470, 110)
        cx, yn, yd, s = 910, 370, 610, 88
        sai = d6 + 0.2
        E.saida(c, t, a7, lambda: corrente(c, t, b6, lerp(b6, c6, 0.8), 3, cx, yn, s, sai), d=0.3)
        E.foco(c, t, a7, 0.45, lambda p: E.formula(c, "1", cx, yn, 110, cor=CERTO, a=p, align="center"))
        q = ep(t, b6, 0.4)
        c.drawRect(skia.Rect.MakeXYWH(cx - 340, 433, 680, 8), M.paint(TINTA, q))
        corrente(c, t, c6, lerp(c6, d6, 0.75), 6, cx, yd, s, sai)
        E.foco(c, t, d6, 0.45, lambda p: (M.rrect(c, 700, 196, 420, 90, 45, E.COR, p), E.formula(c, "÷ 2^3 nos dois", 910, 262, 58, cor=E.SOBRE, a=p, align="center")))
        fl(c, t, [("=", None, b7), ("f{1}{2^3}", None, b7), ("=", None, lerp(b7, c7, 0.45))], 1310, 470, 120)
        E.foco(c, t, lerp(b7, c7, 0.5), 0.5, lambda p: num_bola(c, "f{1}{8}", 1660, 430, 110, 96, p))
        fm(c, t, c7, "2^{−3} = f{1}{8}", XE, 830, 110, COR)
        E.frase(c, t, d7, ps("expoente negativo", "g", 58, COR) + ps("vira fração", "i", 64), 800, 790, passo=0.12)
        E.frase(c, t, d7 + 1.2, ps("1 em cima, expoente positivo embaixo", "i", 58), 800, 880, passo=0.1)
    if C["s06"] <= t < C["s08"] + 0.4:
        E.saida(c, t, C["s08"] - 0.1, s06_07)

    if t >= C["s08"]:
        a, b_, c_ = (C[f"s08.{k}"] for k in "abc")
        E.frase(c, t, C["s08"] + 0.1, ps("veja outra", "i", 96, COR), XE, 280)
        y = 620
        fm(c, t, a, "3^{−2}", XE + 60, y, 220)
        fm(c, t, b_, "= f{1}{3^2}", 770, y, 200)
        fl(c, t, [("=", None, c_ - 0.1)], 1230, y, 200)
        E.foco(c, t, c_, 0.5, lambda p: num_bola(c, "f{1}{9}", 1600, y - 70, 170, 150, p, CERTO, BR))


# ---------------- escada ----------------
def b_escada(c, t, C, b):
    a, b_, c_, d, e = (C[f"s09.{k}"] for k in "abcde")
    a0, b0, c0 = (C[f"s10.{k}"] for k in "abc")
    for i, ti in enumerate((a, b_, c_, d, a0, b0, c0)):
        degrau_desce(c, t, i, ti)
    E.frase(c, t, C["s09"] + 0.1, ps("uma escada", "i", 92, COR), 1000, 160)
    E.frase(c, t, e, ps("cada degrau", "i", 84) + ps("÷ 2", "g", 84, COR), 1000, 280)
    E.frase(c, t, lerp(c0, C["s10.end"], 0.3), ps("sem regra nova", "g", 80, CERTO), 1180, 400)


# ---------------- base dez ----------------
def b_dez(c, t, C, b):
    def s11():
        a, b_, c_, d = (C[f"s11.{k}"] for k in "abcd")
        E.frase(c, t, C["s11"] + 0.1, ps("com base 10,", "i", 84) + ps("tudo vira contagem", "g", 76, COR), XE, 170, passo=0.15)
        E.frase(c, t, a, ps("expoente positivo conta", "i", 80) + ps("zeros", "g", 80, COR), XE, 290, passo=0.14)
        for k, y, f1, s1 in ((b_, 470, "10^3 = 1.000", "três zeros"), (c_, 650, "10^6 = 1.000.000", "seis zeros"), (d, 830, "10^0 = 1", "nenhum zero")):
            fm(c, t, k, f1, XE, y, 120)
            E.frase(c, t, k + 0.5, ps(s1, "g", 66, COR), 1230, y - 16, passo=0.12)
    E.saida(c, t, C["s12"] - 0.1, s11)

    if C["s12"] <= t < C["s13"] + 0.4:
        a, b_, c_, d, e = (C[f"s12.{k}"] for k in "abcde")

        def s12():
            E.frase(c, t, a, ps("expoente negativo conta", "i", 80) + ps("casas", "g", 80, COR), XE, 170, passo=0.14)
            E.frase(c, t, a + 1.2, ps("depois da vírgula", "i", 72), XE, 260, passo=0.13)
            fl(c, t, [("10^{−3}", None, b_), ("=", None, b_ + 0.6), ("f{1}{10^3}", None, b_ + 0.7)], XE, 470, 130)
            fl(c, t, [("=", None, c_ - 0.1), ("f{1}{1.000}", COR, c_)], 830, 470, 130)
            E.frase(c, t, c_ + 0.3, ps("um milésimo", "g", 66, COR), 1320, 450)
            E.frase(c, t, lerp(c_, d, 0.6), ps("mil tem três zeros", "i", 66), XE, 640, passo=0.13)
            E.frase(c, t, d, ps("3 casas para a esquerda", "g", 62, COR), XE, 730, passo=0.12)
            sal = [(lerp(d, e, 0.1 + 0.28 * i), -i) for i in range(3)]
            E.foco(c, t, lerp(c_, d, 0.8), 0.45, lambda q: E.anda(c, t, "1", 1, sal, 1430, 900, 170, cor=CERTO if t >= e else TINTA, tv=sal[0][0] - 0.2, cor_novo=CERTO if t >= e else COR, cor_v=CERTO if t >= e else COR))
        E.saida(c, t, C["s13"] - 0.1, s12)

    if t >= C["s13"]:
        a, b_, c_ = (C[f"s13.{k}"] for k in "abc")
        xv, y, s = 620, 400, 190
        E.foco(c, t, a, 0.45, lambda q: E.numero(c, "0,001", xv, y, s, "g", TINTA, q, {4: COR}))
        cen = E._centros("0,001", xv, s)
        k = ep(t, a + 0.3, 0.45)
        E.chave(c, cen[2] - 60, cen[4] + 60, y + 44, COR, k, 24, 6, abre=False)
        E.foco(c, t, a + 0.3, 0.45, lambda q: centro(c, "3 casas", cen[3], y + 148, 72, "g", COR, q))
        E.frase(c, t, lerp(a, b_, 0.3), ps("dois zeros e o 1", "i", 76), 1120, 300, passo=0.13)
        E.frase(c, t, lerp(a, b_, 0.6), ps("contar só os zeros", "i", 76), 1120, 420, passo=0.13)
        E.frase(c, t, lerp(a, b_, 0.72), ps("é erro", "g", 76, ERRADO), 1120, 520)
        M.line(c, XE, 640, W - XE, 640, FIO, ep(t, b_ - 0.3, 0.5), 3)
        fm(c, t, b_, "10^{−2}", XE, 840, 170)
        E.frase(c, t, b_ + 0.6, ps("2 casas", "g", 84, COR), 660, 810)
        fl(c, t, [("=", None, c_ - 0.1)], 1030, 835, 150)
        E.foco(c, t, c_, 0.5, lambda p: num_bola(c, "0,01", 1320, 785, 130, 96, p, CERTO, BR))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_, d = (C[f"s14.{k}"] for k in "abcd")
    E.frase(c, t, C["s14"] + 0.1, ps("o erro do começo", "i", 76, ERRADO), XE, 160)
    y = 370
    fm(c, t, a, "2^{−3}", XE, y, 170)
    fm(c, t, lerp(a, b_, 0.3), "= −8", 640, y, 170, ERRADO)
    if t >= lerp(a, b_, 0.75):
        E.risco(c, 650, y + 24, 1100, y - 130, t, lerp(a, b_, 0.75), largura=16)
    M.line(c, XE, 480, W - XE, 480, FIO, ep(t, b_ - 0.3, 0.5), 3)
    fm(c, t, b_, "f{2^3}{2^6}", XE + 20, 680, 150)
    E.frase(c, t, b_ + 0.3, ps("positivo", "g", 80, COR) + ps("dividido por", "i", 84) + ps("positivo", "g", 80, COR), 520, 650, passo=0.15)
    E.frase(c, t, c_, ps("nunca dá negativo", "g", 84, CERTO), 520, 770)
    E.frase(c, t, lerp(c_, d, 0.5), ps("o menos do expoente não é o sinal do resultado", "i", 64), W / 2, 900, "center", 0.1)
    E.foco(c, t, d, 0.45, lambda q: E.pilula(c, "manda virar fração", W / 2, 980, 54, estilo="g", a=q, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15"] + 0.1, ps("agora, o atalho", "i", 92, CLARO), W / 2, 210, "center")
        E.frase(c, t, lerp(C["s15"], C["s15.a"], 0.5), ps("base 10, expoente negativo", "g", 80, BR), W / 2, 330, "center", 0.14)
        for i, (k, s1) in enumerate((("s15.a", "tantos zeros quanto o expoente"), ("s15.b", "vírgula depois do primeiro zero"), ("s15.c", "termine com 1"))):
            y = 520 + i * 170
            E.foco(c, t, C[k], 0.45, lambda q, i=i, y=y: num_bola(c, str(i + 1), XE + 50, y, 56, 64, q, None, BR))
            E.frase(c, t, C[k] + 0.1, [(s1, "g", 66, BR)], XE + 140, y + 24, passo=0.12)
    E.saida(c, t, C["s16"] - 0.1, s15)

    if t >= C["s16"]:
        a, b_, c_, d, e = (C[f"s16.{k}"] for k in "abcde")
        a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
        fm(c, t, a, "10^{−6}", W / 2, 240, 150, BR, "center")
        s_, xv, y, s = "0,000001", 700, 500, 170
        cor = lambda: CERTO if t >= e else BR
        E.foco(c, t, b_, 0.45, lambda q: E._so(c, s_, xv, y, s, [0, 2, 3, 4, 5, 6], cor(), q))
        E.foco(c, t, c_, 0.45, lambda q: E._so(c, s_, xv, y, s, [1], cor(), q))
        E.foco(c, t, d, 0.45, lambda q: E._so(c, s_, xv, y, s, [7], CLARO if t < e else CERTO, q))
        cen = E._centros(s_, xv, s)
        E.foco(c, t, b_ + 0.1, 0.4, lambda q: centro(c, "6 zeros", W / 2, 620, 66, "g", CLARO, q * (1 - ep(t, a7 - 0.2, 0.3))))
        k = ep(t, a7, 0.45)
        E.chave(c, cen[2] - 50, cen[7] + 50, y + 44, CLARO, k, 24, 6, abre=False)
        E.foco(c, t, a7, 0.45, lambda q: centro(c, "6 casas", (cen[2] + cen[7]) / 2, y + 140, 66, "g", CLARO, q))
        E.foco(c, t, b7, 0.45, lambda q: (E.chave(c, cen[0] - 46, cen[0] + 46, y + 44, BR, q, 24, 6, abre=False),
                                          centro(c, "+ esse zero", cen[0], y + 140, 58, "b", BR, q)))
        E.frase(c, t, c7, ps("só vale para", "i", 88, CLARO) + ps("base 10", "g", 84, BR), W / 2, 790, "center")
        fm(c, t, d7, "2^{−3}", XE + 240, 950, 110, BR)
        E.frase(c, t, d7 + 0.8, ps("não há zeros:", "i", 76, CLARO) + ps("vire fração", "g", 72, BR), 720, 930, passo=0.14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_ = C["s18.a"], C["s18.b"]
    E.frase(c, t, C["s18"] + 0.1, ps("hora de testar:", "i", 76, COR) + ps("duas partes", "g", 70, COR), XE, 200, passo=0.14)
    E.foco(c, t, a, 0.45, lambda q: num_bola(c, "1", XE + 50, 400, 50, 58, q))
    fm(c, t, a, "5^3 ÷ 5^5", XE + 130, 450, 140, COR)
    E.frase(c, t, a + 1.4, ps("escreva como fração", "i", 76), XE + 130, 570, passo=0.13)
    E.foco(c, t, b_, 0.45, lambda q: num_bola(c, "2", XE + 50, 720, 50, 58, q))
    fm(c, t, b_, "10^{−5}", XE + 130, 770, 140, COR)
    E.frase(c, t, b_ + 1.0, ps("escreva como número decimal", "i", 76), XE + 130, 890, passo=0.13)
    E.relogio(c, t, C["s19.a"], 1520, 400, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_, d = (C[f"s20.{k}"] for k in "abcd")
    a1, b1 = C["s21.a"], C["s21.b"]

    def s20():
        fm(c, t, C["s20"] + 0.1, "5^3 ÷ 5^5", XE, 280, 130)
        E.frase(c, t, lerp(C["s20"], a, 0.6), ps("repete a base e subtrai", "i", 72), 870, 200, passo=0.13)
        fm(c, t, a, "3 − 5 = −2", 870, 300, 110, COR)
        fm(c, t, b_, "= 5^{−2}", XE, 520, 150)
        E.frase(c, t, lerp(b_, c_, 0.6), ps("vira fração", "g", 72, COR), 870, 500)
        fm(c, t, c_, "= f{1}{5^2}", XE, 790, 170)
        fl(c, t, [("=", None, d - 0.1)], 650, 790, 170)
        E.foco(c, t, d, 0.5, lambda p: num_bola(c, "f{1}{25}", 950, 730, 150, 130, p, CERTO, BR))
    E.saida(c, t, C["s21"] - 0.1, s20)

    if t >= C["s21"]:
        fm(c, t, C["s21"] + 0.1, "10^{−5}", W / 2, 340, 190, None, "center")
        E.frase(c, t, a1, ps("5 casas,", "g", 100, COR) + ps("com o 1 na última", "i", 100), W / 2, 520, "center")
        E.foco(c, t, b1, 0.5, lambda p: E.numero(c, "0,00001", 760, 790, 190, "g", CERTO, p))
        cen = E._centros("0,00001", 760, 190)
        E.chave(c, cen[2] - 56, cen[6] + 56, 836, CERTO, ep(t, b1 + 0.4, 0.45), 24, 6, abre=False)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a, b_, c_ = (C[f"s22.{k}"] for k in "abc")

    def resumo():
        E.frase(c, t, C["s22"] + 0.1, ps("resumindo", "i", 92, COR), W / 2, 170, "center")
        E.frase(c, t, a, ps("expoente negativo é", "i", 84) + ps("fração", "g", 80, COR), XE, 340, passo=0.15)
        E.frase(c, t, a + 1.2, ps("não número negativo", "i", 72, ERRADO), XE, 440, passo=0.13)
        fm(c, t, a + 0.8, "2^{−3} = f{1}{8}", 1200, 400, 110, COR)
        E.frase(c, t, b_ - 0.4, ps("na base 10", "i", 76), XE, 580)
        E.frase(c, t, b_, ps("positivo conta zeros", "g", 76, COR), XE, 700, passo=0.13)
        fm(c, t, b_ + 0.6, "10^3 = 1.000", 1100, 705, 100)
        E.frase(c, t, c_, ps("negativo conta casas", "g", 76, COR), XE, 860, passo=0.13)
        fm(c, t, c_ + 0.6, "10^{−3} = 0,001", 1100, 865, 100)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a2, b2, c2, d2 = (C[f"s23.{k}"] for k in "abcd")
    E.frase(c, t, C["s23"] + 0.2, ps("próxima aula", "i", 84), XE, 240)
    E.frase(c, t, a2, ps("Praticando", "g", 150, COR), XE, 410)
    E.frase(c, t, b2, ps("expressões com", "i", 84) + ps("todas as propriedades", "g", 72, COR), XE, 560, passo=0.15)
    E.foco(c, t, c2, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1480, 340, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c2 + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1620, p), lerp(640, 380, p), ep(t, c2 + 0.2, 0.4), TINTA)
    E.frase(c, t, d2, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 860, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, divisao=b_divisao, escada=b_escada, dez=b_dez, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
