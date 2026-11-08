"""Visual — Estudativo · MAT-EQU-002: valor numérico de uma expressão.
A troca acontece na tela: o x sai, o número entra entre parênteses e o vezes escondido volta. A conta do começo,
2x² − 3 com x = −2, é montada peça por peça no tempo da fala; o −11 e o 13 mostram onde a conta se perde.
Instantes: os cues de C[...] e, para cada palavra, pal(cena, palavra), lido da voz gravada em audio/tempos.json."""
import json
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-002_valor_numerico_de_uma_expressao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("trocar", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 3 * 5 + 4 == 19 and 5 - (-4) == 9
assert 2 * (-2) ** 2 - 3 == 5 and 2 * -(2 ** 2) - 3 == -11 and (2 * -2) ** 2 - 3 == 13
assert (-3) ** 2 == 9 and -(3 ** 2) == -9 and (-2) ** 3 == -8 and 2 ** 3 == 8
assert (-3) ** 2 - 4 * (-3) == 21 and 9 - 12 == -3

_T = {s["id"]: s for s in json.load(open(Path(__file__).resolve().parents[1] / "audio" / "tempos.json", encoding="utf8"))["scenes"]}


def pal(sid, palavra, n=0):
    """instante em que a voz diz a palavra (n = qual ocorrência na cena)"""
    s = _T[sid]
    achou = [tk["t0"] for tk in s["tokens"] if tk["disp"].lower().strip(",.:;?!") == palavra]
    return s["start"] + achou[n]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def form(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def fw(s, size):
    """largura de uma fórmula (0 se vazia)"""
    return E.formula(None, s, 0, 0, size, a=0) if s else 0.0


def realce(c, t, t0, s, trecho, x, y, size, cor=None, align="left", n=0, t1=None):
    """fundo claro atrás de um trecho da fórmula s; t1 = some"""
    a = ep(t, t0, 0.35) * (1 - ep(t, t1, 0.3) if t1 else 1)
    if a <= 0:
        return
    xi = x - fw(s, size) / 2 if align == "center" else x
    i0 = -1
    for _ in range(n + 1):
        i0 = s.find(trecho, i0 + 1)
    x0, w = xi + fw(s[:i0], size), fw(trecho, size) - size * 0.02
    pad = min(size * 0.14, 16)
    M.rrect(c, x0 - pad, y - size * 0.95, w + pad * 2, size * 1.25, size * 0.2, cor or COR, 0.16 * a)


def monta(c, t, pecas, x, y, size, align="left", cor=None):
    """fórmula que se monta peça por peça: pecas = [(texto, instante[, cor])]; devolve o x inicial"""
    total = fw("".join(p[0] for p in pecas), size)
    x0 = x - total / 2 if align == "center" else x
    acc = ""
    for p in pecas:
        s, t0, cp = p[0], p[1], (p[2] if len(p) > 2 else cor)
        xo = x0 + fw(acc, size)
        E.foco(c, t, t0, 0.4, lambda a, s=s, xo=xo, cp=cp: E.formula(c, s, xo, y, size, cor=cp, a=a))
        acc += s
    return x0


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def bola_em(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda p: num_bola(c, s, cx, cy, r * ease_back(prog(t, t0, 0.6)), size, p, cor, BR))


def seta(c, t, t0, x0, x1, y, cor=None):
    p = ep(t, t0, 0.45)
    if p > 0:
        M.arrow(c, x0, y, x1, y, cor or COR, p, 5, 16, p)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s01.{k}"] for k in "abcd")

    def conta():
        form(c, t, a_, "2x^2 − 3", W / 2, 400, 220, None, "center")
        form(c, t, b_, "x = −2", W / 2, 620, 120, COR, "center")
        E.foco(c, t, c_, 0.4, lambda p: E.escreve(c, "−11", 380, 900, 170, "g", ERRADO, p))
        if t >= pal("s01", "faltou"):
            E.risco(c, 360, 900, 720, 770, t, pal("s01", "faltou"), largura=14)
        E.frase(c, t, pal("s01", "faltou"), ps("faltou um par de", "i", 70, ERRADO) + ps("parênteses", "g", 64, ERRADO), 380, 990, passo=0.1)
        bola_em(c, t, d_, "5", 1480, 830, 150, 170, CERTO)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2 = C["s02.a"], C["s02.b"]
    E.frase(c, t, a2, ps("até o fim desta aula, você", "i", 84), XE, 280, passo=0.12)
    E.frase(c, t, pal("s02", "troca"), ps("troca a letra", "g", 110, COR), XE, 450, passo=0.15)
    E.frase(c, t, pal("s02", "qualquer"), ps("por qualquer número", "i", 104), XE, 590, passo=0.12)
    E.frase(c, t, pal("s02", "sem"), ps("sem errar o", "i", 104) + ps("sinal", "g", 100, COR), XE, 730, passo=0.12)
    E.foco(c, t, b2 - 0.2, 0.7, lambda p: E.bola(c, 1600, 840, 190 * ease_back(prog(t, b2 - 0.2, 0.7))), blur=0)
    E.foco(c, t, b2 + 0.2, 0.5, lambda p: (centro(c, "+ atalho", 1600, 830, 64, "g", BR, p), centro(c, "de prova", 1600, 900, 64, "i", BR, p)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s03.{k}"] for k in "abcd")
    E.frase(c, t, C["s03"] + 0.3, ps("três", "g", 84, COR) + ps("lembretes", "i", 90), XE, 180)
    xr = XE + 110
    E.foco(c, t, a_, 0.45, lambda p: num_bola(c, "1", XE + 40, 310, 40, 50, p))
    form(c, t, a_, "2x = 2 × x", xr, 340, 90)
    E.foco(c, t, b_, 0.45, lambda p: num_bola(c, "2", XE + 40, 500, 40, 50, p))
    y = 530
    form(c, t, pal("s03", "parênteses"), "( )", xr, y, 80)
    seta(c, t, pal("s03", "potência") - 0.3, xr + 150, xr + 240, y - 26)
    E.foco(c, t, pal("s03", "potência"), 0.4, lambda p: E.escreve(c, "potência", xr + 270, y, 72, "b", TINTA, p))
    seta(c, t, pal("s03", "vezes", 1) - 0.3, xr + 600, xr + 690, y - 26)
    form(c, t, pal("s03", "vezes", 1), "× ÷", xr + 720, y, 80)
    seta(c, t, pal("s03", "mais") - 0.3, xr + 900, xr + 990, y - 26)
    form(c, t, pal("s03", "mais"), "+ −", xr + 1020, y, 80)
    E.foco(c, t, c_, 0.45, lambda p: num_bola(c, "3", XE + 40, 700, 40, 50, p))
    form(c, t, c_, "(−3)^2", xr, 740, 120)
    form(c, t, pal("s03", "nove"), "= 9", xr + 360, 740, 120, CERTO)
    E.foco(c, t, pal("s03", "nove") + 0.3, 0.4, lambda p: E.escreve(c, "com parênteses", xr + 700, 725, 60, "i", TINTA2, p))
    form(c, t, d_, "−3^2", xr, 920, 120)
    form(c, t, pal("s03", "nove", 1), "= −9", xr + 360, 920, 120, ERRADO)
    E.foco(c, t, pal("s03", "sem"), 0.4, lambda p: E.escreve(c, "sem parênteses", xr + 700, 905, 60, "i", TINTA2, p))
    E.frase(c, t, pal("s03", "procure"), ps("faltou alguma? procure no canal", "i", 54, TINTA2), 1180, 1020, passo=0.08)


# ---------------- trocar ----------------
def b_trocar(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s04.{k}"] for k in "abcde")
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]

    def s04_05():
        E.frase(c, t, C["s04"] + 0.4, ps("troque a letra e faça a conta:", "i", 76), W / 2, 180, "center", 0.1)
        E.frase(c, t, a4, ps("valor numérico", "g", 96, COR), W / 2, 300, "center", 0.2)
        # 3x + 4: o x sai e o (5) entra no lugar
        s, y, x0 = 140, 520, XE + 40
        w3, ws = fw("3", s), fw("(5)", s)
        E.foco(c, t, b4, 0.45, lambda p: (E.formula(c, "3", x0, y, s, a=p), E.formula(c, " + 4", x0 + w3 + ws, y, s, a=p)))
        sai = ep(t, c4, 0.5)
        E.foco(c, t, b4, 0.45, lambda p: E.formula(c, "x", x0 + w3 + (ws - fw("x", s)) / 2, y, s, cor=COR, a=p * (1 - sai)))
        if t >= c4:
            q = ep(t, c4 + 0.3, 0.4) * (1 - ep(t, d4, 0.3))
            E.caixa_pontilhada(c, x0 + w3 + 4, y - 120, ws - 8, 150, q, COR, prog_=q)
        E.foco(c, t, d4, 0.45, lambda p: E.formula(c, "(5)", x0 + w3, y, s, cor=COR, a=p))
        form(c, t, pal("s04", "xis", 1), "x = 5", 1300, y, 110, COR)
        # a conta com o vezes de volta
        L = "3 × (5) + 4"
        realce(c, t, a5, L, "×", x0, 720, s)
        realce(c, t, b5, L, "3 × (5)", x0, 720, s, TINTA2)
        form(c, t, e4, L, x0, 720, s)
        E.frase(c, t, a5, ps("o vezes escondido", "i", 70) + ps("volta", "g", 64, COR), 1150, 700, passo=0.1)
        form(c, t, pal("s05", "quinze"), "= 15 + 4", x0, 910, s)
        form(c, t, pal("s05", "dezenove"), "= 19", x0 + fw("= 15 + 4 ", s), 910, s, CERTO)
    fase(c, t, C["s04"], C["s06"] - 0.1, s04_05)

    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")

    def s06a():
        E.frase(c, t, pal("s06", "com"), ps("com número positivo, o parêntese parece", "i", 80) + ps("enfeite", "g", 74), W / 2, 330, "center", 0.1)
        E.frase(c, t, a6, ps("mas ele guarda o número", "i", 92) + ps("inteiro", "g", 86, COR), W / 2, 560, "center", 0.12)
        E.frase(c, t, pal("s06", "com", 1), ps("com sinal e tudo", "g", 86, COR), W / 2, 700, "center", 0.12)
    fase(c, t, C["s06"], b6 - 0.1, s06a)

    def s06b():
        form(c, t, b6, "5 − x", XE, 220, 110)
        form(c, t, pal("s06", "xis", 1), "x = −4", XE + 400, 220, 110, COR)
        monta(c, t, [("5 − ", c6), ("(", pal("s06", "abre"), COR), ("−4", pal("s06", "menos", 3), COR), (")", pal("s06", "fecha"), COR)], W / 2, 470, 160, "center")
        E.foco(c, t, pal("s06", "tirar"), 0.5, lambda p: E.pilula(c, "tirar uma dívida é como ganhar", W / 2, 610, 54, estilo="b", a=p))
        form(c, t, d6, "5 + 4 = 9", W / 2, 790, 130, CERTO, "center")
        Lx = "5 − −4"
        realce(c, t, e6 + 0.3, Lx, "− −", 760, 975, 110, ERRADO)
        E.frase(c, t, pal("s06", "sem"), ps("sem parênteses:", "i", 70, ERRADO), XE, 970, passo=0.1)
        form(c, t, e6, Lx, 760, 975, 110, ERRADO)
        E.frase(c, t, pal("s06", "encosta"), ps("um sinal encosta no outro", "i", 60, ERRADO), 1180, 965, passo=0.1)
    fase(c, t, b6, C["s07"] - 0.1, s06b)

    a7, b7 = C["s07.a"], C["s07.b"]

    def s07():
        E.frase(c, t, pal("s07", "regra"), ps("a regra", "i", 84, COR), W / 2, 190, "center")
        E.frase(c, t, a7, ps("ao trocar a letra, ponha o número", "i", 92), W / 2, 330, "center", 0.12)
        E.frase(c, t, pal("s07", "entre"), ps("entre parênteses", "g", 110, COR), W / 2, 470, "center", 0.15)
        form(c, t, pal("s07", "positivo"), "(5)", 640, 680, 150)
        form(c, t, pal("s07", "negativo"), "(−4)", 960, 680, 150)
        E.frase(c, t, b7, ps("sempre", "g", 150, COR), W / 2, 870, "center")
        E.frase(c, t, pal("s07", "hábito"), ps("custa um segundo e evita o erro mais caro", "i", 58, TINTA2), W / 2, 980, "center", 0.07)
    fase(c, t, C["s07"], 1e9, s07)


# ---------------- a conta do começo ----------------
def b_exemplo(c, t, C, b):
    a8, b8 = C["s08.a"], C["s08.b"]
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    L1 = "2 × (−2)^2 − 3"
    S, X = 130, XE

    def s08_09():
        form(c, t, a8, "2x^2 − 3", X, 220, 110, COR)
        form(c, t, pal("s08", "xis", 1), "x = −2", X + 560, 220, 110, COR)
        realce(c, t, a9, L1, "(−2)^2", X, 440, S, t1=b9)
        realce(c, t, b9, L1, "2 ×", X, 440, S, t1=c9)
        monta(c, t, [("2 × ", b8), ("(", pal("s08", "abre"), COR), ("−2", pal("s08", "menos", 2), COR), (")", pal("s08", "fecha"), COR),
                     ("^2", pal("s08", "ao", 1), COR), (" − 3", pal("s08", "menos", 3))], X, 440, S)
        # o lado: a potência
        E.foco(c, t, pal("s09", "menos"), 0.45, lambda p: E.formula(c, "(−2) × (−2)", 1160, 430, 70, cor=TINTA2, a=p))
        E.frase(c, t, pal("s09", "sinais"), ps("sinais iguais:", "i", 64, TINTA2), 1160, 520, passo=0.1)
        form(c, t, pal("s09", "mais"), "+4", 1560, 525, 74, COR)
        L2 = "= 2 × 4 − 3"
        realce(c, t, b9, L2, "2 × 4", X, 650, S, t1=c9)
        form(c, t, pal("s09", "quatro"), L2, X, 650, S)
        L3 = "= 8 − 3"
        realce(c, t, c9, L3, "8 − 3", X, 860, S)
        form(c, t, pal("s09", "oito"), L3, X, 860, S)
        form(c, t, d9 - 0.3, "=", X + fw(L3 + " ", S), 860, S)
        bola_em(c, t, d9, "5", X + fw(L3 + " = ", S) + 140, 815, 110, 130, CERTO)
    fase(c, t, C["s08"], C["s10"] - 0.1, s08_09)

    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")

    def s10():
        E.frase(c, t, pal("s10", "e"), ps("e o", "i", 92) + ps("−11?", "g", 90, ERRADO), XE, 200, passo=0.15)
        L = "2 × −2^2 − 3"
        E.frase(c, t, pal("s10", "sem"), ps("sem parênteses:", "i", 70, ERRADO), XE, 380, passo=0.1)
        realce(c, t, a0, L, "2^2", 700, 390, 120, ERRADO)
        form(c, t, pal("s10", "sem"), L, 700, 390, 120)
        E.frase(c, t, a0 + 0.4, ps("o expoente só alcança o 2", "i", 60, ERRADO), 1180, 270, passo=0.1)
        form(c, t, b0, "= 2 × (−4) − 3", 700, 580, 120)
        form(c, t, c0, "= −8 − 3", 700, 770, 120)
        form(c, t, d0, "= −11", 700 + fw("= −8 − 3 ", 120), 770, 120, ERRADO)
        E.frase(c, t, e0, ps("a conta usou só", "i", 80) + ps("um pedaço do −2", "g", 74, ERRADO), W / 2, 960, "center", 0.12)
    fase(c, t, C["s10"], 1e9, s10)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_, f_ = (C[f"s11.{k}"] for k in "abcdef")

    def errado():
        E.frase(c, t, C["s11"] + 0.3, ps("outro erro:", "i", 84) + ps("o vezes antes da potência", "g", 74, ERRADO), XE, 190, passo=0.12)
        form(c, t, b_, "2 × (−2)", XE, 380, 110)
        form(c, t, pal("s11", "menos", 1), "= −4", XE + fw("2 × (−2) ", 110), 380, 110, ERRADO)
        form(c, t, c_, "(−4)^2 = 16", XE, 570, 110, ERRADO)
        form(c, t, d_ - 0.6, "16 − 3", XE, 760, 110, ERRADO)
        form(c, t, d_, "= 13", XE + fw("16 − 3 ", 110), 760, 110, ERRADO)
        if t >= d_ + 0.5:
            E.risco(c, XE - 20, 800, XE + 640, 300, t, d_ + 0.5, largura=14)
    errado()
    xc = 1420
    E.foco(c, t, e_, 0.5, lambda p: E.formula(c, "2x^2", xc, 640, 240, cor=TINTA, a=p, align="center"))
    w2, wx = fw("2", 240), fw("x^2", 240)
    x0 = xc - fw("2x^2", 240) / 2
    q = ep(t, e_ + 0.4, 0.5)
    E.caixa_pontilhada(c, x0 + w2 - 6, 420, wx + 10, 270, q, COR, prog_=q)
    E.frase(c, t, e_ + 0.4, ps("o expoente está colado", "i", 60) + ps("só no x", "g", 56, COR), xc, 790, "center", 0.1)
    E.foco(c, t, f_, 0.45, lambda p: (M.arrow(c, x0 + w2 / 2, 370, x0 + w2 / 2, 450, COR, p, 5, 16, p),
                                     centro(c, "multiplica depois", x0 + w2 / 2 + 60, 340, 58, "b", COR, p)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")

    def s12():
        E.frase(c, t, C["s12"] + 0.3, ps("agora, o atalho", "i", 80, CLARO), W / 2, 170, "center")
        E.frase(c, t, a2, ps("com o menos dentro do parêntese,", "i", 84, CLARO), W / 2, 300, "center", 0.11)
        E.frase(c, t, pal("s12", "expoente"), ps("expoente par", "g", 96, BR) + ps("apaga o sinal", "i", 104, CLARO), W / 2, 420, "center", 0.13)
        monta(c, t, [("(−2)", b2, BR), ("^2", pal("s12", "ao"), BR)], 480, 640, 160)
        form(c, t, c2, "= 2^2 = 4", 480 + fw("(−2)^2 ", 160), 640, 160, CLARO)
        E.frase(c, t, pal("s12", "sem"), ps("sem parênteses, o expoente", "i", 64, CLARO) + ps("nem alcança o sinal", "g", 60, BR), W / 2, 800, "center", 0.1)
        E.foco(c, t, d2, 0.5, lambda p: E.pilula(c, "x² com parênteses: conta com o número sem o sinal", W / 2, 950, 52, estilo="b", fundo=E.COR, cor=BR, a=p))
    fase(c, t, C["s12"], C["s13"] - 0.1, s12)

    a3, b3 = C["s13.a"], C["s13.b"]

    def s13():
        E.frase(c, t, C["s13"] + 0.2, ps("funciona porque", "i", 84, CLARO), W / 2, 220, "center")
        form(c, t, a3, "(−) × (−) = (+)", W / 2, 400, 130, BR, "center")
        E.frase(c, t, pal("s13", "dupla"), ps("cada dupla de menos vira mais", "i", 70, CLARO), W / 2, 510, "center", 0.1)
        E.frase(c, t, b3, ps("não vale no x", "g", 84, BR) + ps("sem expoente", "i", 90, CLARO), W / 2, 700, "center", 0.12)
        form(c, t, pal("s13", "menos", 1), "−3x", 760, 900, 130, BR)
        E.foco(c, t, pal("s13", "menos", 1) + 0.3, 0.45, lambda p: E.selo(c, 1080, 860, 56, False, p))
        E.frase(c, t, pal("s13", "sinal"), ps("o sinal muda a resposta", "i", 64, CLARO), 1170, 880, passo=0.1)
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)

    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]

    def s14():
        E.frase(c, t, a4, ps("nem com", "i", 100, CLARO) + ps("expoente ímpar", "g", 96, BR), W / 2, 230, "center", 0.13)
        form(c, t, b4, "(−2)^3", 240, 470, 140, BR)
        form(c, t, pal("s14", "menos", 1), "= −8", 240 + fw("(−2)^3 ", 140), 470, 140, CLARO)
        E.foco(c, t, c4 + 0.5, 0.45, lambda p: centro(c, "≠", 1010, 465, 130, "g", ERRADO, p))
        form(c, t, c4, "2^3 = 8", 1140, 470, 140, BR)
        E.frase(c, t, pal("s14", "com", 1), ps("expoente ímpar:", "i", 84, CLARO) + ps("o sinal fica", "g", 80, BR), W / 2, 720, "center", 0.12)
        E.frase(c, t, pal("s14", "conta"), ps("conta inteira, com sinal e tudo", "i", 76, CLARO), W / 2, 860, "center", 0.11)
    fase(c, t, C["s14"], 1e9, s14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_ = C["s15.a"], C["s15.b"]
    E.frase(c, t, C["s15"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, pal("s15", "calcule"), ps("calcule", "i", 100), XE, 400)
    form(c, t, a_, "x^2 − 4x", XE, 600, 180)
    E.frase(c, t, b_ - 0.2, ps("para", "i", 100), XE, 820)
    form(c, t, b_, "x = −3", XE + 230, 825, 130, COR)
    E.relogio(c, t, C["s16.a"], 1490, 440, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7 = C["s17.a"], C["s17.b"]
    a8, b8, c8, d8, e8 = (C[f"s18.{k}"] for k in "abcde")
    S, X = 110, XE
    L1 = "(−3)^2 − 4 × (−3)"
    form(c, t, C["s17"] + 0.2, "x^2 − 4x, x = −3", W - 120, 130, 60, TINTA2, "right")
    realce(c, t, b7, L1, "(−3)^2", X, 280, S, t1=a8)
    realce(c, t, a8, L1, "4 × (−3)", X, 280, S, t1=b8)
    monta(c, t, [("(", a7, COR), ("−3", pal("s17", "menos"), COR), (")", pal("s17", "fecha"), COR), ("^2", pal("s17", "ao"), COR),
                 (" − 4 × ", pal("s17", "menos", 1)), ("(", pal("s17", "abre", 1), COR), ("−3", pal("s17", "menos", 2), COR),
                 (")", pal("s17", "fecha", 1), COR)], X, 280, S)
    E.frase(c, t, pal("s17", "pelo"), ps("pelo atalho:", "i", 60, TINTA2), 1250, 250, passo=0.1)
    form(c, t, b7 + 0.3, "3^2 = 9", 1250, 330, 80, COR)
    E.foco(c, t, a8, 0.45, lambda p: E.formula(c, "4 × (−3) = −12", 1250, 450, 64, cor=TINTA2, a=p))
    L3 = "= 9 − (−12)"
    realce(c, t, pal("s18", "tirar"), L3, "− (−", X, 480, S, t1=c8)
    monta(c, t, [("= 9 − ", b8), ("(", pal("s18", "abre"), COR), ("−12", pal("s18", "menos", 3), COR), (")", pal("s18", "fecha"), COR)], X, 480, S)
    E.foco(c, t, pal("s18", "tirar"), 0.5, lambda p: E.pilula(c, "tirar uma dívida é ganhar", 1300, 560, 52, estilo="b", a=p))
    form(c, t, c8, "= 9 + 12", X, 680, S)
    form(c, t, d8 - 0.3, "=", X + fw("= 9 + 12 ", S), 680, S)
    bola_em(c, t, d8, "21", X + fw("= 9 + 12 = ", S) + 110, 640, 110, 110, CERTO)
    E.frase(c, t, pal("s18", "quem"), ps("perdeu o sinal:", "i", 70, ERRADO), X, 900, passo=0.1)
    form(c, t, pal("s18", "nove", 2), "9 − 12", X + 480, 905, S, ERRADO)
    form(c, t, e8, "= −3", X + 480 + fw("9 − 12 ", S), 905, S, ERRADO)
    if t >= e8 + 0.5:
        E.risco(c, X + 460, 935, X + 1150, 820, t, e8 + 0.5, largura=12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a1, b1 = C["s19.a"], C["s19.b"]

    def resumo():
        E.frase(c, t, C["s19"] + 0.3, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        E.foco(c, t, a1, 0.5, lambda p: num_bola(c, "1", 230, 410, 58, 66, p))
        E.frase(c, t, a1 + 0.1, ps("troque a letra pelo número", "i", 84) + ps("entre parênteses", "g", 76, COR), 320, 440, passo=0.12)
        form(c, t, pal("s19", "com"), "x = −2  →  (−2)", 320, 590, 90, COR)
        E.foco(c, t, b1, 0.5, lambda p: num_bola(c, "2", 230, 760, 58, 66, p))
        E.frase(c, t, b1 + 0.1, ps("siga a", "i", 84) + ps("ordem das operações", "g", 76, COR), 320, 790, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a_, b_, c_, d_, e_ = (C[f"s20.{k}"] for k in "abcde")
    E.frase(c, t, C["s20"] + 0.2, ps("próxima aula", "i", 84), XE, 230)
    E.frase(c, t, a_, ps("juntar termos", "g", 120, COR), XE, 390)
    E.frase(c, t, a_ + 0.4, ps("parecidos", "g", 120, COR), XE, 530)
    form(c, t, b_, "3x + 5x", XE, 700, 110)
    E.frase(c, t, c_, ps("expressão mais curta", "i", 80), XE, 830, passo=0.12)
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, d_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(620, 375, p), ep(t, d_ + 0.2, 0.4), TINTA)
    E.frase(c, t, e_, ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), 1450, 760, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, trocar=b_trocar, exemplo=b_exemplo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
