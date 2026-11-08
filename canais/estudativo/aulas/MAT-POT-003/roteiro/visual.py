"""Visual — Estudativo · MAT-POT-003: multiplicar e dividir potências de mesma base.
Identidade em _ferramentas/editorial.py. Peças desta aula: fila dos dias que dobram, fila de cincos que saem na divisão
e a escada do dois no palco. Expoente sempre com E.formula."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, sinal, palco, centro
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-003_multiplicar_dividir_potencias_mesma_base.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("vezes", "dividir", "zero", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 2 ** 3 * 2 ** 4 == 2 ** 7 == 128 and 5 * 5 ** 3 == 5 ** 4 and 5 ** 7 // 5 ** 4 == 5 ** 3 == 125 and 7 ** 3 // 7 ** 3 == 1 == 7 ** 0
assert 2 ** 3 * 3 ** 2 == 72 and 2 ** 3 + 2 ** 4 == 24 and 16 * 32 == 2 ** 9 == 512 and 3 ** 5 * 3 ** 2 == 3 ** 7 and 3 ** 7 // 3 ** 7 == 1


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


def dia(c, t, ti, x, y, r, cor=None):
    E.foco(c, t, ti, 0.4, lambda q: num_bola(c, "×2", x, y, r, r * 0.72, q, cor))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def conta():
        y = 620
        fm(c, t, a_, "7^0", 230, y, 330)
        sinal(c, t, b_ - 0.15, "=", 800, y - 110, 200)
        E.foco(c, t, b_, 0.5, lambda a: centro(c, "0", 1090, y, 300, "g", ERRADO, a))
        if t >= c_ - 0.2:
            E.risco(c, 980, y + 40, 1210, y - 250, t, c_ - 0.2, largura=20)
        E.foco(c, t, c_, 0.5, lambda a: num_bola(c, "1", 1500, y - 110, 190, 190, a, CERTO, BR))
        E.frase(c, t, lerp(b_, c_, 0.35), ps("em boa companhia,", "i", 84) + ps("e errou", "g", 76, ERRADO), W / 2, 880, "center", 0.15)
        E.frase(c, t, lerp(c_, C["s01.end"], 0.45), ps("não é decreto:", "i", 80) + ps("dá para provar", "g", 74, COR), W / 2, 990, "center", 0.15)
    E.saida(c, t, C["s02"] - 0.1, conta)

    if t >= C["s02"]:
        a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]
        E.frase(c, t, a2, ps("até o fim desta aula", "i", 92), XE, 250)
        E.frase(c, t, lerp(a2, b2, 0.45), ps("multiplicar", "g", 110, COR) + ps("e", "i", 110) + ps("dividir", "g", 110, COR), XE, 420)
        E.frase(c, t, b2, ps("sem calcular", "i", 104) + ps("nenhuma", "g", 96, COR), XE, 590)
        fm(c, t, lerp(b2, c2, 0.6), "7^0 = 1", XE, 790, 150, COR)
        E.foco(c, t, c2 - 0.1, 0.6, lambda a: E.bola(c, 1490, 780, 220 * ease_back(prog(t, c2 - 0.1, 0.6))), blur=0)
        E.foco(c, t, c2 + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1490, 770, 80, "g", E.SOBRE, a), centro(c, "de prova", 1490, 850, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_ = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, C["s03"] + 0.1, ps("lembre de", "i", 96), XE, 410)
    E.foco(c, t, a_, 0.5, lambda p: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, p))
    E.foco(c, t, a_ + 0.15, 0.5, lambda p: E.escreve(c, "coisas", XE + 225, 700, 120, "i", TINTA, p))
    x, w = 830, 920
    for i, (k, l1, l2) in enumerate(((b_, "o expoente diz quantas vezes", "a base aparece"), (c_, "a divisão", "desfaz a multiplicação"))):
        y = 240 + i * 290
        p = ep(t, k, 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, k + 0.1, [(l1, "i", 66)], x + 44, y + 96)
        E.frase(c, t, k + 0.3, [(l2, "g", 66, COR)], x + 44, y + 186)
    E.frase(c, t, lerp(c_, C["s03.end"], 0.6), ps("faltou alguma?", "i", 66, COR) + ps("procure no canal", "i", 66), W / 2, 960, "center", 0.15)


# ---------------- multiplicar ----------------
def b_vezes(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    xs = [330 + i * 210 for i in range(7)]

    def s04():
        E.frase(c, t, C["s04"] + 0.1, ps("um vídeo cujas visualizações", "i", 80), XE, 170, passo=0.13)
        E.frase(c, t, a4, ps("dobram", "g", 80, COR) + ps("todo dia", "i", 84), XE, 280)
        y, r = 470, 84
        for i, x in enumerate(xs):
            ti = lerp(b4, c4, 0.1 + 0.2 * i) if i < 3 else lerp(c4, d4, 0.1 + 0.15 * (i - 3))
            dia(c, t, ti, x, y, r, E.COR if i < 3 else TINTA)
        k3, k4 = ep(t, lerp(b4, c4, 0.6), 0.4), ep(t, lerp(c4, d4, 0.6), 0.4)
        E.chave(c, xs[0] - r, xs[2] + r, y + r + 18, COR, k3, 24, 5, abre=False)
        E.chave(c, xs[3] - r, xs[6] + r, y + r + 18, TINTA, k4, 24, 5, abre=False)
        fl(c, t, [("3 dias:", None, b4), ("2^3", COR, lerp(b4, c4, 0.6))], (xs[0] + xs[2]) / 2, 720, 84, "center")
        fl(c, t, [("4 dias:", None, c4), ("2^4", None, lerp(c4, d4, 0.6))], (xs[3] + xs[6]) / 2, 720, 84, "center")
        fl(c, t, [("2^3", COR, d4), ("·", None, d4 + 0.1), ("2^4", None, d4 + 0.2)], W / 2, 930, 150, "center")
    E.saida(c, t, C["s05"] - 0.1, s04)

    if C["s05"] <= t < C["s06"] + 0.4:
        a, b_, c_, d = (C[f"s05.{k}"] for k in "abcd")

        def s05():
            E.frase(c, t, C["s05"] + 0.1, ps("quantos dias?", "i", 84) + ps("sete", "g", 80, COR), XE, 180)
            fl(c, t, [("2^3", COR, C["s05"] + 0.1), ("·", None, C["s05"] + 0.1), ("2^4", None, C["s05"] + 0.1), ("=", None, a), ("2^7", COR, a)], XE, 370, 150)
            y = 640
            xs1, ws1 = fl(c, t, [("2 × 2 × 2", COR, b_)], XE, y, 130)
            xs2, ws2 = fl(c, t, [("×", None, c_), ("2 × 2 × 2 × 2", None, c_ + 0.1)], XE + ws1[0] + 26, y, 130)
            q = ep(t, d, 0.45)
            E.chave(c, XE, xs2[-1] + ws2[-1], y + 40, COR, q, 26, 6, abre=False)
            E.frase(c, t, d, ps("o 2 aparece", "i", 92) + ps("7 vezes", "g", 92, COR), W / 2, 830, "center")
        E.saida(c, t, C["s06"] - 0.1, s05)

    if t >= C["s06"]:
        a, b_, c_, d = (C[f"s06.{k}"] for k in "abcd")
        E.frase(c, t, a, ps("multiplicando potências", "i", 84) + ps("de mesma base", "g", 78, COR), XE, 200, passo=0.15)
        E.frase(c, t, b_, ps("repete a base", "g", 104, COR) + ps("e", "i", 104) + ps("soma os expoentes", "g", 92, COR), W / 2, 350, "center", 0.17)
        fm(c, t, b_ + 1.0, "2^3 · 2^4 = 2^{3 + 4} = 2^7", W / 2, 540, 130, align="center")
        M.line(c, XE, 620, W - XE, 620, FIO, ep(t, c_ - 0.5, 0.5), 3)
        E.frase(c, t, lerp(b_, c_, 0.82), ps("número sem expoente", "i", 72), XE, 730, passo=0.14)
        fm(c, t, c_, "5 = 5^1", XE, 880, 130)
        E.frase(c, t, c_ + 0.6, ps("aparece uma vez", "i", 64, TINTA2), XE, 970, passo=0.13)
        fm(c, t, d, "5 · 5^3 = 5^4", 900, 880, 150, COR)


# ---------------- dividir ----------------
def b_dividir(c, t, C, b):
    a7, b7, c7 = (C[f"s07.{k}"] for k in "abc")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")

    def tela():
        E.frase(c, t, C["s07"] + 0.1, ps("dividir é o", "i", 76) + ps("caminho de volta", "g", 70, COR), XE, 160, passo=0.14)
        fm(c, t, a7, "5^7 ÷ 5^4", XE, 350, 170)
        X = 900
        fl(c, t, [("÷ 5", COR, b7), ("desfaz", TINTA2, b7 + 0.2), ("× 5", None, b7 + 0.5)], X, 280, 72, gap=26)
        fl(c, t, [("÷ 5^4", COR, c7), ("desfaz 4 de uma vez", TINTA2, c7 + 0.4)], X, 390, 72, gap=26)
        y, r = 620, 80
        xs = [320 + i * 215 for i in range(7)]
        for i, x in enumerate(xs):
            ti = a8 + i * 0.1
            sai = ep(t, b8 + (i - 3) * 0.15, 0.5) if i >= 3 else 0
            E.foco(c, t, ti, 0.35, lambda q, x=x, i=i, sai=sai: num_bola(c, "5", x, y + 90 * sai, r, 88, q * (1 - 0.82 * sai), ERRADO if sai > 0 else None, BR))
            if i >= 3 and t >= b8 + (i - 3) * 0.15:
                E.risco(c, x - 46, y + 136, x + 46, y + 44, t, b8 + (i - 3) * 0.15 + 0.25, largura=9)
        k = ep(t, c8, 0.4)
        E.chave(c, xs[0] - r, xs[2] + r, y + r + 18, CERTO, k, 24, 5, abre=False)
        E.frase(c, t, c8, ps("sobram 3", "g", 78, CERTO), (xs[0] + xs[2]) / 2, y + r + 110, "center")
        fm(c, t, d8, "5^3 = 125", XE + 330, 980, 110, COR)
        E.frase(c, t, b8 + 0.1, ps("saem 4", "g", 78, ERRADO), xs[5], y - r - 30, "center")
    E.saida(c, t, C["s09"] - 0.1, tela)

    if t >= C["s09"]:
        a, b_ = C["s09.a"], C["s09.b"]
        E.frase(c, t, a, ps("dividindo potências", "i", 84) + ps("de mesma base", "g", 78, COR), XE, 210, passo=0.15)
        E.frase(c, t, b_, ps("repete a base", "g", 104, COR) + ps("e", "i", 104) + ps("subtrai os expoentes", "g", 88, COR), W / 2, 370, "center", 0.17)
        fm(c, t, b_ + 1.0, "5^7 ÷ 5^4 = 5^{7 − 4} = 5^3", W / 2, 570, 130, align="center")
        te = lerp(b_, C["s09.end"], 0.42)
        E.frase(c, t, te, ps("aqui, o primeiro expoente é", "i", 72) + ps("maior ou igual", "g", 66, COR) + ps("ao segundo", "i", 72), W / 2, 780, "center", 0.13)
        E.frase(c, t, lerp(b_, C["s09.end"], 0.75), ps("o outro caso é assunto de outra aula", "i", 66, TINTA2), W / 2, 890, "center", 0.12)


# ---------------- expoente zero ----------------
def b_zero(c, t, C, b):
    a0, b0 = C["s10.a"], C["s10.b"]
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")

    def prova():
        E.frase(c, t, C["s10"] + 0.1, ps("a prova", "g", 96, COR), XE, 180)
        E.frase(c, t, lerp(C["s10"], a0, 0.4), ps("todo número dividido por ele mesmo dá 1", "i", 62), 580, 170, passo=0.1)
        y1, y2 = 380, 590
        fm(c, t, a0, "7^3 ÷ 7^3", XE, y1, 130)
        fm(c, t, b0 - 0.1, "=", 900, y1, 130)
        E.foco(c, t, b0, 0.5, lambda q: num_bola(c, "1", 1120, y1 - 46, 100, 110, q, CERTO, BR))
        fm(c, t, a1, "7^3 ÷ 7^3", XE, y2, 130)
        fm(c, t, b1, "= 7^{3 − 3}", 900, y2, 130)
        fm(c, t, c1, "= 7^0", 1380, y2, 130, COR)
        E.frase(c, t, lerp(c1, d1, 0.2), ps("saíram todos os setes,", "i", 76) + ps("mas o resultado não é zero", "g", 58, ERRADO), W / 2, 740, "center", 0.13)
        E.frase(c, t, lerp(c1, d1, 0.6), ps("a mesma conta não tem duas respostas", "i", 72), W / 2, 840, "center", 0.12)
        fm(c, t, d1, "7^0", 730, 1000, 120)
        fm(c, t, d1, "=", 1000, 990, 120)
        E.foco(c, t, d1 + 0.1, 0.5, lambda q: num_bola(c, "1", 1190, 950, 90, 100, q, CERTO, BR))
    E.saida(c, t, C["s12"] - 0.1, prova)

    if t >= C["s12"]:
        a, b_, c_ = (C[f"s12.{k}"] for k in "abc")
        E.frase(c, t, a, ps("qualquer base,", "i", 88) + ps("menos a base 0", "g", 82, COR), XE, 220, passo=0.16)
        tq = lerp(a, b_, 0.45)
        fm(c, t, tq, "0 ÷ 0", XE, 400, 120, ERRADO)
        E.frase(c, t, tq + 0.4, ps("não existe divisão por zero", "i", 72, ERRADO), 620, 380, passo=0.13)
        M.line(c, XE, 480, W - XE, 480, FIO, ep(t, b_ - 0.5, 0.5), 3)
        E.frase(c, t, lerp(a, b_, 0.85), ps("e no vídeo?", "i", 80, COR), XE, 600)
        E.frase(c, t, b_, ps("zero dias dobrando", "g", 92, COR), XE, 720)
        E.frase(c, t, b_ + 1.1, ps("as visualizações ficam como estavam", "i", 72), XE, 820, passo=0.13)
        E.frase(c, t, c_, ps("é o mesmo que", "i", 84), XE, 950)
        fm(c, t, c_ + 0.4, "× 1", 760, 955, 120, COR)


# ---------------- só mesma base ----------------
def b_base(c, t, C, b):
    a, b_, c_, d, e = (C[f"s13.{k}"] for k in "abcde")

    def s13():
        E.frase(c, t, a - 0.2, ps("cuidado:", "g", 96, ERRADO), XE, 210)
        E.frase(c, t, a + 0.4, ps("só com a", "i", 96) + ps("mesma base", "g", 96, COR), 640, 210)
        fm(c, t, b_, "2^3 · 3^2", XE, 480, 170)
        E.frase(c, t, c_, ps("nada se junta", "g", 88, ERRADO), 900, 450)
        E.frase(c, t, d, ps("calcule cada potência", "i", 84), XE, 700, passo=0.15)
        fl(c, t, [("8", None, e), ("×", None, e + 0.2), ("9", None, e + 0.3), ("=", None, e + 0.5)], XE, 880, 140)
        E.foco(c, t, e + 0.7, 0.5, lambda q: num_bola(c, "72", 760, 833, 110, 104, q, CERTO, BR))
    E.saida(c, t, C["s14"] - 0.1, s13)

    if t >= C["s14"]:
        a1, b1, c1, d1 = (C[f"s14.{k}"] for k in "abcd")
        E.frase(c, t, a1 - 0.3, ps("e só com", "i", 96) + ps("vezes e dividido", "g", 96, COR), XE, 230)
        fm(c, t, b1, "2^3 + 2^4", XE, 470, 150)
        fm(c, t, lerp(b1, c1, 0.5), "= 8 + 16", 810, 465, 130)
        fm(c, t, c1 - 0.1, "=", 1340, 465, 130)
        E.foco(c, t, c1, 0.5, lambda q: num_bola(c, "24", 1590, 420, 110, 96, q, CERTO, BR))
        fm(c, t, d1 - 0.3, "2^7", XE, 760, 150, ERRADO)
        fm(c, t, d1, "daria 128", 430, 755, 110, ERRADO)
        E.foco(c, t, d1 + 0.4, 0.5, lambda q: E.selo(c, 1090, 715, 66, False, q))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_, d = (C[f"s15.{k}"] for k in "abcd")
    E.frase(c, t, a, ps("o erro comum:", "i", 88, ERRADO) + ps("multiplicar os expoentes", "g", 74, ERRADO), XE, 200, passo=0.15)
    y = 410
    fm(c, t, lerp(a, b_, 0.5), "2^3 · 2^4", XE, y, 160)
    fm(c, t, b_, "= 2^{12}", 790, y, 160, ERRADO)
    if t >= c_ - 0.4:
        E.risco(c, 860, y + 20, 1190, y - 130, t, c_ - 0.4, largura=14)
    y2, s = 640, 110
    xs1, ws1 = fl(c, t, [("2 × 2 × 2", COR, c_)], XE, y2, s)
    k1 = ep(t, c_ + 0.5, 0.4)
    E.chave(c, XE, XE + ws1[0], y2 + 34, COR, k1, 22, 5, abre=False)
    E.foco(c, t, c_ + 0.5, 0.4, lambda q: centro(c, "3 vezes", XE + ws1[0] / 2, y2 + 124, 60, "g", COR, q))
    xs2, ws2 = fl(c, t, [("×", None, c_ + 0.9), ("2 × 2 × 2 × 2", None, c_ + 1.0)], XE + ws1[0] + 24, y2, s)
    x0 = xs2[1]
    k2 = ep(t, c_ + 1.5, 0.4)
    E.chave(c, x0, x0 + ws2[1], y2 + 34, TINTA, k2, 22, 5, abre=False)
    E.foco(c, t, c_ + 1.5, 0.4, lambda q: centro(c, "4 vezes", x0 + ws2[1] / 2, y2 + 124, 60, "g", TINTA, q))
    E.frase(c, t, d, ps("7 vezes,", "g", 110, CERTO) + ps("não 12", "i", 110), W / 2, 950, "center")


# ---------------- atalho (palco escuro) ----------------
VAL = [2 ** i for i in range(1, 10)]


def escada_dois(c, t, tempos, tg, altos, x0=190, pw=172, chao=985, y0=870, dy=72):
    """degraus do 2: tempos = instante de cada um; tg = quando cada degrau mostra o expoente; altos = {i: cor} acende um degrau"""
    for i, (v, ti) in enumerate(zip(VAL, tempos)):
        yi, xi = y0 - i * dy, x0 + i * pw

        def d(a, i=i, v=v, yi=yi, xi=xi):
            cor = altos.get(i, E.COR)
            M.rrect(c, xi + 4, yi, pw - 8, chao - yi, 10, cor, a)
            centro(c, str(v), xi + pw / 2, yi + 62, 58, "g", BR, a)
            if t >= tg:
                E.formula(c, f"2^{i + 1}", xi + pw / 2, yi + 104, 40, cor=BR, a=a * ep(t, tg + i * 0.05, 0.35), align="center")
        E.foco(c, t, ti, 0.4, d, sobe=22)


def b_atalho(c, t, C, b):
    palco(c, t)
    a, b_, c_, d, e, f, g, h, i_, j = (C[f"s16.{k}"] for k in "abcdefghij")
    a7, b7, c7, d7, e7, f7 = (C[f"s17.{k}"] for k in "abcdef")
    tempos = [b_, c_, d, e, f, c7, d7, e7, f7]

    def tela():
        altos = {}
        if t >= i_:
            altos[3] = CERTO
        if t >= j:
            altos[4] = CERTO
        if t >= f7:
            altos[8] = CERTO
        E.frase(c, t, C["s16"] + 0.1, ps("agora, o atalho", "i", 76, CLARO), XE, 170)
        E.frase(c, t, a, ps("a escada do dois", "g", 92, BR), XE, 290)
        escada_dois(c, t, tempos, g, altos)
        if t >= b7:
            q = ep(t, b7, 0.4)
            xi, yi = 190 + 8 * 172, 870 - 8 * 72
            E.caixa_pontilhada(c, xi, yi - 6, 172, 985 - yi + 12, q, CLARO, prog_=q)
        y = 450
        fl(c, t, [("16", CERTO if t >= i_ else BR, h), ("×", BR, h + 0.2), ("32", CERTO if t >= j else BR, h + 0.3)], XE, y, 110)
        fl(c, t, [("4", BR, a7), ("+", CLARO, a7 + 0.2), ("5", BR, a7 + 0.3), ("=", CLARO, a7 + 0.5), ("9", BR, a7 + 0.6)], XE, y + 130, 96)
        E.foco(c, t, f7 + 0.2, 0.5, lambda q: E.formula(c, "= 512", XE + 390, y, 110, cor=CLARO, a=q))
    E.saida(c, t, C["s18"] - 0.1, tela)

    if t >= C["s18"]:
        a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
        E.frase(c, t, a8, ps("é a regra de somar expoentes,", "i", 84, CLARO) + ps("disfarçada", "g", 78, BR), W / 2, 220, "center", 0.14)
        fm(c, t, a8 + 1.2, "2^4 · 2^5 = 2^9", W / 2, 420, 130, BR, align="center")
        E.frase(c, t, b8, ps("só compensa com", "i", 84, CLARO) + ps("números da escada", "g", 78, BR), W / 2, 590, "center", 0.15)
        fm(c, t, c8, "18 × 32", XE + 90, 790, 130, BR)
        E.frase(c, t, c8 + 0.8, ps("18 não é degrau", "g", 80, ERRADO), 860, 770)
        E.frase(c, t, d8, ps("arme a conta", "g", 110, BR), W / 2, 950, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_, c_ = (C[f"s19.{k}"] for k in "abc")
    E.frase(c, t, C["s19"] + 0.1, ps("hora de testar", "i", 76, COR), XE, 200)
    E.frase(c, t, lerp(C["s19"], a, 0.6), ps("uma potência só", "i", 84), XE, 330, passo=0.14)
    fm(c, t, a, "3^5 · 3^2", XE, 510, 150, COR)
    E.frase(c, t, b_, ps("depois, divida por", "i", 84), XE, 680, passo=0.14)
    fm(c, t, b_ + 0.5, "3^7", 830, 700, 150, COR)
    E.frase(c, t, c_, ps("quanto dá", "i", 110) + ps("no fim?", "g", 104, COR), XE, 900)
    E.relogio(c, t, C["s20.a"], 1520, 400, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_, d, e = (C[f"s21.{k}"] for k in "abcde")
    E.frase(c, t, C["s21"] + 0.3, ps("multiplicando,", "i", 76) + ps("soma", "g", 70, COR), XE, 170)
    fl(c, t, [("3^5 · 3^2", None, C["s21"] + 0.1), ("=", None, b_ - 0.1), ("3^7", COR, b_)], XE, 340, 130)
    fm(c, t, a, "5 + 2 = 7", 1000, 340, 110, COR)
    E.frase(c, t, lerp(b_, c_, 0.6), ps("dividindo,", "i", 76) + ps("subtrai", "g", 70, COR), XE, 500)
    fl(c, t, [("3^7 ÷ 3^7", None, lerp(b_, c_, 0.7)), ("=", None, d - 0.1), ("3^0", COR, d)], XE, 670, 130)
    fm(c, t, c_, "7 − 7 = 0", 1000, 670, 110, COR)
    fm(c, t, e - 0.1, "3^0 =", XE, 880, 130, COR)
    E.foco(c, t, e, 0.5, lambda q: num_bola(c, "1", XE + 430, 835, 100, 110, q, CERTO, BR))
    E.frase(c, t, lerp(e, C["s21.end"], 0.3), ps("faz sentido:", "i", 76, CERTO), 760, 830)
    E.frase(c, t, lerp(e, C["s21.end"], 0.45), ps("um número dividido por ele mesmo", "i", 66), 760, 925, passo=0.11)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a, b_, c_, d = (C[f"s22.{k}"] for k in "abcd")

    def resumo():
        E.frase(c, t, C["s22"] + 0.1, ps("resumindo", "i", 92, COR), W / 2, 150, "center")
        E.frase(c, t, a, ps("na", "i", 96) + ps("mesma base", "g", 96, COR), W / 2, 300, "center")
        for k, y, s1, f1 in ((b_, 490, "vezes soma", "2^3 · 2^4 = 2^7"), (c_, 680, "dividido subtrai", "5^7 ÷ 5^4 = 5^3"), (d, 870, "expoente zero dá 1", "7^0 = 1")):
            E.frase(c, t, k, ps(s1, "g", 78, COR), XE + 40, y, passo=0.14)
            fm(c, t, k + 0.5, f1, 1040, y, 110)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a2, b2, c2, d2, e2 = (C[f"s23.{k}"] for k in "abcde")
    E.frase(c, t, C["s23"] + 0.2, ps("próxima aula", "i", 84), XE, 190)
    E.frase(c, t, a2, ps("potência de potência", "g", 84, COR), XE, 310)
    E.frase(c, t, b2, ps("potência de uma multiplicação", "g", 72, COR), XE, 430)
    E.frase(c, t, c2, ps("números grandes", "g", 84, COR) + ps("como potências", "i", 84), XE, 560)
    E.foco(c, t, d2, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1460, 700, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, d2 + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1600, p), lerp(950, 740, p), ep(t, d2 + 0.2, 0.4), TINTA)
    E.frase(c, t, e2, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), XE, 860)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, vezes=b_vezes, dividir=b_dividir, zero=b_zero, base=b_base, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
