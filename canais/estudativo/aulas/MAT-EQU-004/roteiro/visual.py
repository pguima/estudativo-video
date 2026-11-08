"""Visual — Estudativo · MAT-EQU-004: distributiva e sinal de menos antes do parêntese.
Três combos (lanche de x reais e suco de 4) mostram por que o número de fora multiplica cada termo de dentro; os arcos
saem do número de fora e alcançam cada termo. Depois, −2(x − 5), o menos sozinho que tira o parêntese inteiro,
o erro de multiplicar só o primeiro termo e, no palco, o atalho de trocar todos os sinais.
Instantes: os cues de C[...] e, para cada palavra, pal(cena, palavra), lido da voz gravada em audio/tempos.json."""
import json
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-004_distributiva_e_sinal_de_menos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("combo", "menos", "atalho", "questao", "fim"))
BR = "#FFFFFF"

x = 10
assert 3 * (x + 4) == 3 * x + 12 == 42 and (10 + 4) * 3 == 42 and 30 + 12 == 42
assert -2 * (x - 5) == -2 * x + 10 == -10 and -20 + 10 == -10 and -2 * x - 5 == -25
assert 5 - (x - 3) == 8 - x == -2 and 5 - x - 3 == -8
assert 3 * (x + 2) - (x - 4) == 2 * x + 10 == 30 and 36 - 6 == 30
del x

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
    return E.formula(None, s, 0, 0, size, a=0) if s else 0.0


def trecho_x(s, trecho, x, size, align="left", n=0):
    """(x inicial, largura) de um trecho da fórmula s"""
    xi = x - fw(s, size) / 2 if align == "center" else x
    i0 = -1
    for _ in range(n + 1):
        i0 = s.find(trecho, i0 + 1)
    return xi + fw(s[:i0], size), fw(trecho, size) - size * 0.02


def realce(c, t, t0, s, trecho, x, y, size, cor=None, align="left", n=0, t1=None):
    a = ep(t, t0, 0.35) * (1 - ep(t, t1, 0.3) if t1 else 1)
    if a <= 0:
        return
    x0, w = trecho_x(s, trecho, x, size, align, n)
    pad = min(size * 0.14, 16)
    M.rrect(c, x0 - pad, y - size * 0.95, w + pad * 2, size * 1.25, size * 0.2, cor or COR, 0.16 * a)


def monta(c, t, pecas, x, y, size, align="left", cor=None):
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




def arco(c, t, t0, s, de, ate_, x, y, size, alto, cor=None, align="left", n=0, rotulo=None):
    """arco com seta do número de fora até um termo de dentro"""
    x0, w0 = trecho_x(s, de, x, size, align)
    x1, w1 = trecho_x(s, ate_, x, size, align, n)
    E.salto(c, t, t0, x0 + w0 / 2, x1 + w1 / 2, y - size * 0.95, alto, cor or COR, rotulo, size=46)


def combo(c, t, cx, cy, ta, tl, ts, lanche="x"):
    """um combo: cartão com o lanche (x reais) e o suco (4 reais)"""
    E.foco(c, t, ta, 0.5, lambda p: (M.rrect(c, cx - 170, cy - 130, 340, 260, 22, BR, p),
                                     c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 170, cy - 130, 340, 260), 22, 22), M.paint(E.COR, p, stroke=4))))
    pao = M.mix(E.COR, BR, 0.45)

    def lanche_(p):
        M.rrect(c, cx - 140, cy - 92, 110, 40, 20, pao, p)
        M.rrect(c, cx - 146, cy - 48, 122, 18, 9, TINTA2, p)
        M.rrect(c, cx - 140, cy - 26, 110, 24, 10, pao, p)
        E.escreve(c, lanche, cx - 5, cy - 18, 72, "g", COR, p)

    def suco(p):
        path = skia.Path()
        path.moveTo(cx - 130, cy + 22); path.lineTo(cx - 40, cy + 22); path.lineTo(cx - 52, cy + 112); path.lineTo(cx - 118, cy + 112); path.close()
        c.drawPath(path, M.paint(M.mix(E.COR, BR, 0.7), p))
        c.drawPath(path, M.paint(E.COR, p, stroke=3))
        M.line(c, cx - 75, cy + 22, cx - 55, cy - 8, TINTA2, p, 5)
        E.escreve(c, "4", cx - 5, cy + 95, 72, "g", COR, p)
    E.foco(c, t, tl, 0.45, lanche_)
    E.foco(c, t, ts, 0.45, suco)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def conta():
        monta(c, t, [("5 − ", a_), ("(", pal("s01", "abre"), COR), ("x − 3", pal("s01", "xis")), (")", pal("s01", "fecha"), COR)], W / 2, 330, 190, "center")
        L = "5 − x − 3"
        realce(c, t, pal("s01", "errou"), L, "− 3", XE, 640, 140, ERRADO)
        form(c, t, b_, L, XE, 640, 140, ERRADO)
        if t >= pal("s01", "errou"):
            E.risco(c, XE - 10, 680, XE + 720, 520, t, pal("s01", "errou"), largura=14)
        E.frase(c, t, pal("s01", "errou"), ps("errou um sinal", "i", 70, ERRADO), XE, 790, passo=0.12)
        form(c, t, c_, "8 − x", 1180, 640, 160, CERTO)
        E.foco(c, t, c_ + 0.3, 0.45, lambda p: E.selo(c, 1660, 590, 60, True, p))
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2 = C["s02.a"], C["s02.b"]
    E.frase(c, t, a2, ps("até o fim desta aula, você", "i", 84), XE, 280, passo=0.12)
    E.frase(c, t, pal("s02", "abre"), ps("abre parênteses", "g", 110, COR), XE, 450, passo=0.15)
    E.frase(c, t, pal("s02", "sem"), ps("sem errar o", "i", 104) + ps("sinal", "g", 100, COR), XE, 600, passo=0.12)
    E.foco(c, t, b2 - 0.2, 0.7, lambda p: E.bola(c, 1600, 840, 190 * ease_back(prog(t, b2 - 0.2, 0.7))), blur=0)
    E.foco(c, t, b2 + 0.2, 0.5, lambda p: (centro(c, "+ atalho", 1600, 830, 64, "g", BR, p), centro(c, "de prova", 1600, 900, 64, "i", BR, p)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_ = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, C["s03"] + 0.4, ps("lembre de", "i", 92), XE, 400)
    E.foco(c, t, a_, 0.5, lambda p: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, p))
    E.foco(c, t, a_ + 0.15, 0.5, lambda p: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, p))
    x, w = 880, 900
    p1 = ep(t, b_, 0.5)
    E.caixa_pontilhada(c, x, 170, w, 360, p1, prog_=p1)
    E.frase(c, t, b_ + 0.1, ps("regra de sinais", "g", 66, COR) + ps("(multiplicando)", "i", 64), x + 44, 260, passo=0.1)
    E.frase(c, t, pal("s03", "iguais"), ps("sinais iguais:", "i", 66), x + 44, 370, passo=0.1)
    form(c, t, pal("s03", "mais"), "+", x + 470, 375, 80, CERTO)
    E.frase(c, t, pal("s03", "diferentes"), ps("sinais diferentes:", "i", 66), x + 44, 470, passo=0.1)
    form(c, t, pal("s03", "menos"), "−", x + 560, 475, 80, ERRADO)
    p2 = ep(t, c_, 0.5)
    E.caixa_pontilhada(c, x, 580, w, 260, p2, prog_=p2)
    E.frase(c, t, c_ + 0.1, ps("juntar termos semelhantes", "g", 64, COR), x + 44, 670, passo=0.1)
    E.frase(c, t, pal("s03", "xis"), ps("x com x, número com número", "i", 66), x + 44, 770, passo=0.1)
    E.frase(c, t, pal("s03", "procure"), ps("faltou alguma? procure no canal", "i", 58, TINTA2), x + 44, 940, passo=0.1)


# ---------------- distributiva: o combo ----------------
F, YF, SF = "3(x + 4)", 640, 150


def b_combo(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s04.{k}"] for k in "abcde")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    dez = t >= a6
    for i in range(3):
        combo(c, t, 470 + i * 420, 250, a4 + i * 0.2, b4 + i * 0.12, c4 + i * 0.12, "10" if dez else "x")
    E.foco(c, t, a6, 0.4, lambda p: E.escreve(c, "lanche de R$ 10", 1500, 470, 52, "i", TINTA2, p))
    monta(c, t, [("3", d4), ("(", pal("s04", "abre"), COR), ("x + 4", pal("s04", "xis", 1)), (")", pal("s04", "fecha"), COR)], XE, YF, SF)
    E.saida(c, t, a5, lambda: E.foco(c, t, e4, 0.45, lambda p: E.pilula(c, "3 × (x + 4)", XE + 900, YF - 50, 56, estilo="b", fundo=TINTA, a=p)))
    arco(c, t, a5, F, "3", "x", XE, YF, SF, 70)
    arco(c, t, pal("s05", "três", 2), F, "3", "4", XE, YF, SF, 120)
    form(c, t, b5, "= 3x + 12", XE + fw(F + " ", SF), YF, SF, COR)

    def regra():
        E.frase(c, t, c5, ps("o número de fora multiplica", "i", 80) + ps("cada termo de dentro", "g", 74, COR), XE, 820, passo=0.11)
        E.foco(c, t, d5, 0.5, lambda p: E.pilula(c, "propriedade distributiva", W / 2, 950, 60, estilo="b", a=p))
    fase(c, t, c5, a6 - 0.1, regra)

    def teste():
        E.frase(c, t, b6 - 0.6, ps("pelo parêntese:", "i", 72, TINTA2), XE, 830, passo=0.1)
        form(c, t, b6, "10 + 4 = 14", XE + 500, 835, 100)
        form(c, t, c6, "14 × 3 = 42", XE + 1080, 835, 100)
        E.frase(c, t, d6 - 0.6, ps("aberto:", "i", 72, TINTA2), XE, 970, passo=0.1)
        form(c, t, d6, "30 + 12 = 42", XE + 500, 975, 100)
        E.foco(c, t, e6, 0.45, lambda p: E.selo(c, 1420, 940, 54, True, p))
        E.frase(c, t, e6, ps("bateu", "g", 90, CERTO), 1500, 970)
    fase(c, t, a6, 1e9, teste)


# ---------------- com sinal de menos ----------------
G = "−2(x − 5)"


def b_negativo(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")

    def s07():
        E.frase(c, t, C["s07"] + 0.3, ps("com sinal de menos:", "i", 80) + ps("regra de sinais em cada termo", "g", 70, COR), W / 2, 170, "center", 0.11)
        monta(c, t, [("−2", a7), ("(", pal("s07", "abre"), COR), ("x − 5", pal("s07", "xis")), (")", pal("s07", "fecha"), COR)], W / 2, 470, 160, "center")
        arco(c, t, b7, G, "−2", "x", W / 2, 470, 160, 55, align="center")
        arco(c, t, c7, G, "−2", "5", W / 2, 470, 160, 95, align="center")
        form(c, t, b7 + 0.3, "(−2) × x = −2x", XE + 200, 620, 100)
        form(c, t, c7 + 0.3, "(−2) × (−5) = +10", XE + 200, 770, 100)
        E.frase(c, t, pal("s07", "sinais", 1), ps("sinais iguais", "i", 66, CERTO), XE + 1180, 760, passo=0.1)
        E.frase(c, t, d7 - 0.6, ps("resultado:", "i", 80), XE + 200, 930, passo=0.1)
        form(c, t, d7, "−2x + 10", XE + 600, 940, 130, CERTO)
    fase(c, t, C["s07"], C["s08"] - 0.1, s07)

    def s08():
        form(c, t, C["s08"] + 0.2, "−2(x − 5) = −2x + 10", XE, 260, 100, COR)
        E.frase(c, t, C["s08"] + 0.4, ps("confira com x = 10", "i", 70, TINTA2), 1250, 250, passo=0.1)
        E.frase(c, t, a8 - 0.3, ps("pelo parêntese:", "i", 72, TINTA2), XE, 450, passo=0.1)
        form(c, t, a8, "10 − 5 = 5", XE + 500, 455, 100)
        form(c, t, pal("s08", "menos", 1), "−2 × 5 =", XE + 500, 600, 100)
        form(c, t, b8, "−10", XE + 500 + fw("−2 × 5 = ", 100), 600, 100, CERTO)
        E.frase(c, t, c8 - 0.6, ps("aberto:", "i", 72, TINTA2), XE, 760, passo=0.1)
        form(c, t, c8, "−20 + 10 =", XE + 500, 765, 100)
        form(c, t, pal("s08", "também"), "−10", XE + 500 + fw("−20 + 10 = ", 100), 765, 100, CERTO)
        E.foco(c, t, pal("s08", "também") + 0.4, 0.45, lambda p: E.selo(c, 1420, 730, 50, True, p))
        arco(c, t, d8, "−2(x − 5)", "−2", "x", XE, 260, 100, 50)
        arco(c, t, pal("s08", "também", 1), "−2(x − 5)", "−2", "5", XE, 260, 100, 85)
        E.frase(c, t, d8, ps("o −2 de fora alcança o x", "i", 72) + ps("e também o 5", "g", 66, COR), W / 2, 940, "center", 0.1)
    fase(c, t, C["s08"], 1e9, s08)


# ---------------- menos sozinho ----------------
P = "5 − (x − 3)"
YP, SP = 400, 160


def b_menos(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]

    def s09_10():
        E.frase(c, t, C["s09"] + 0.3, ps("e o", "i", 88) + ps("menos sozinho", "g", 82, COR) + ps("na frente?", "i", 88), W / 2, 190, "center", 0.12)
        x0, w = trecho_x(P, "(x − 3)", W / 2, SP, "center")
        q = ep(t, b9, 0.45)
        E.caixa_pontilhada(c, x0 - 16, YP - 170, w + 32, 220, q, COR, prog_=q)
        realce(c, t, pal("s09", "tira", 1), P, "x", W / 2, YP, SP, align="center")
        realce(c, t, c9, P, "− 3", W / 2, YP, SP, align="center", n=0)
        monta(c, t, [("5 − ", a9), ("(", pal("s09", "abre"), COR), ("x − 3", pal("s09", "xis")), (")", pal("s09", "fecha"), COR)], W / 2, YP, SP, "center")

        E.saida(c, t, pal("s09", "aqui") - 0.1, lambda: E.frase(c, t, pal("s09", "só"), ps("só com números: a conta de dentro primeiro", "i", 64, TINTA2), W / 2, 570, "center", 0.08))
        if t >= pal("s09", "aqui") - 0.1:
            E.saida(c, t, b9 - 0.1, lambda: E.frase(c, t, pal("s09", "aqui"), ps("aqui não dá: o x é desconhecido", "i", 64, TINTA2), W / 2, 570, "center", 0.08))
        E.frase(c, t, b9, ps("tira o parêntese", "i", 70) + ps("inteiro", "g", 66, COR), W / 2, 570, "center", 0.1)
    fase(c, t, C["s09"], C["s11"] - 0.1, s09_10)

    def s10():
        E.frase(c, t, C["s10"], ps("tira o x:", "i", 72), XE, 720, passo=0.1)
        form(c, t, a0, "−x", XE + 300, 725, 110, COR)
        E.frase(c, t, pal("s10", "tirar", 1), ps("tira o −3:", "i", 72), 900, 720, passo=0.1)
        form(c, t, b0, "+3", 1220, 725, 110, CERTO)
        E.foco(c, t, pal("s10", "tirar", 2), 0.45, lambda p: E.pilula(c, "tirar uma dívida é como ganhar", 1240, 820, 46, estilo="b", a=p))
        form(c, t, c0, "= 5 − x + 3", XE, 960, 120)
        form(c, t, d0, "= 8 − x", XE + fw("= 5 − x + 3 ", 120), 960, 120, CERTO)
    fase(c, t, C["s10"], C["s11"] - 0.1, s10)

    def s11():
        L = "5 − x − 3"
        realce(c, t, a1, L, "− 3", XE, 300, 140, ERRADO)
        form(c, t, C["s11"] + 0.2, L, XE, 300, 140, ERRADO)
        E.frase(c, t, a1, ps("deixou o 3 de fora", "i", 72, ERRADO), XE + 820, 250, passo=0.1)
        E.frase(c, t, pal("s11", "o", 1), ps("o menos tirou só o x", "i", 72, ERRADO), XE + 820, 340, passo=0.1)
        E.frase(c, t, pal("s11", "com"), ps("com x = 10:", "i", 72, TINTA2), XE, 520, passo=0.1)
        E.frase(c, t, pal("s11", "certo"), ps("certo:", "g", 66, CERTO), XE, 680)
        form(c, t, pal("s11", "certo"), "8 − 10 =", XE + 260, 685, 110)
        form(c, t, b1, "−2", XE + 260 + fw("8 − 10 = ", 110), 685, 110, CERTO)
        E.frase(c, t, pal("s11", "versão"), ps("errado:", "g", 66, ERRADO), XE, 860)
        form(c, t, pal("s11", "versão"), "5 − 10 − 3 =", XE + 260, 865, 110)
        form(c, t, c1, "−8", XE + 260 + fw("5 − 10 − 3 = ", 110), 865, 110, ERRADO)
    fase(c, t, C["s11"], 1e9, s11)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s12.{k}"] for k in "abcde")
    E.frase(c, t, C["s12"] + 0.3, ps("outro erro:", "i", 84) + ps("multiplicar só o primeiro termo", "g", 74, ERRADO), XE, 190, passo=0.11)
    form(c, t, pal("s12", "em"), G, XE, 400, 140)
    L = "−2x − 5"
    xL = XE + fw(G + "   ", 140) + 90
    E.foco(c, t, b_, 0.4, lambda p: E.escreve(c, "→", xL - 110, 390, 100, "g", ERRADO, p))
    form(c, t, b_, L, xL, 400, 140, ERRADO)
    x0, w = trecho_x(L, "− 5", xL, 140)
    q = ep(t, c_, 0.45)
    E.caixa_pontilhada(c, x0 - 16, 250, w + 32, 190, q, ERRADO, prog_=q)
    E.foco(c, t, c_, 0.45, lambda p: centro(c, "sem ser multiplicado", x0 + w / 2, 520, 54, "i", ERRADO, p))
    E.frase(c, t, pal("s12", "com"), ps("com x = 10:", "i", 72, TINTA2), XE, 680, passo=0.1)
    form(c, t, d_ - 0.4, "−2x − 5 →", XE, 850, 110, ERRADO)
    form(c, t, d_, "−25", XE + fw("−2x − 5 → ", 110), 850, 110, ERRADO)
    E.frase(c, t, e_ - 0.5, ps("certo:", "g", 66, CERTO), 1060, 845)
    form(c, t, e_, "−10", 1300, 850, 110, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    AM = "#FFD500"

    def s13():
        E.frase(c, t, C["s13"] + 0.3, ps("agora, o atalho", "i", 80, CLARO), W / 2, 170, "center")
        E.frase(c, t, a3, ps("menos sozinho na frente do parêntese", "i", 84, CLARO), W / 2, 290, "center", 0.1)
        E.frase(c, t, pal("s13", "troca"), ps("troca todos os sinais de dentro", "g", 80, BR), W / 2, 400, "center", 0.11)
        y, s = 640, 160
        form(c, t, a3 + 0.5, "−(x − 3)", 340, y, s, BR)
        xe = 340 + fw("−(x − 3) ", s)
        form(c, t, b3 - 0.2, "=", xe, y, s, BR)
        form(c, t, b3, "−x", xe + fw("= ", s), y, s, AM)
        form(c, t, c3, "+ 3", xe + fw("= −x ", s), y, s, AM)
        E.foco(c, t, b3 + 0.2, 0.4, lambda p: centro(c, "x vira −x", xe + fw("= ", s) + 80, y + 110, 54, "b", CLARO, p))
        E.foco(c, t, c3 + 0.2, 0.4, lambda p: centro(c, "−3 vira +3", xe + fw("= −x ", s) + 120, y + 180, 54, "b", CLARO, p))
        E.frase(c, t, d3, ps("e o parêntese", "i", 90, CLARO) + ps("some", "g", 86, BR), W / 2, 960, "center", 0.12)
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)

    a4, b4, c4, d4, e4, f4 = (C[f"s14.{k}"] for k in "abcdef")

    def porque():
        E.frase(c, t, C["s14"] + 0.2, ps("funciona porque", "i", 84, CLARO), W / 2, 220, "center")
        form(c, t, a4, "−(x − 3) = −1 × (x − 3)", W / 2, 450, 120, BR, "center")
        E.frase(c, t, b4, ps("multiplicar por −1", "i", 90, CLARO) + ps("só troca o sinal", "g", 84, BR), W / 2, 680, "center", 0.12)
    fase(c, t, C["s14"], c4 - 0.1, porque)

    def casos():
        E.frase(c, t, c4, ps("número na frente:", "g", 66, BR) + ps("não basta trocar, multiplique", "i", 70, CLARO), XE, 220, passo=0.1)
        form(c, t, pal("s14", "tem"), "−2(x − 5) = −2x + 10", XE, 340, 100, CLARO)
        E.frase(c, t, d4, ps("mais na frente:", "g", 66, BR) + ps("nada muda, só apague", "i", 70, CLARO), XE, 520, passo=0.1)
        form(c, t, pal("s14", "é", 1), "+(x − 3) = x − 3", XE, 640, 100, CLARO)
        E.frase(c, t, e4, ps("menos sozinho:", "g", 66, BR) + ps("troca tudo, direto", "i", 70, CLARO), XE, 820, passo=0.1)
        form(c, t, e4 + 0.3, "−(x − 3)", XE, 940, 100, CLARO)
        form(c, t, f4, "= −x + 3", XE + fw("−(x − 3) ", 100), 940, 100, AM)
    fase(c, t, c4, 1e9, casos)


# ---------------- questão ----------------
Q = "3(x + 2) − (x − 4)"


def b_questao(c, t, C, b):
    a_, b_ = C["s15.a"], C["s15.b"]
    E.frase(c, t, C["s15"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, pal("s15", "simplifique"), ps("simplifique", "i", 110), XE, 420)
    monta(c, t, [("3", a_), ("(", pal("s15", "abre"), COR), ("x + 2", pal("s15", "xis")), (")", pal("s15", "fecha"), COR),
                 (" − ", b_), ("(", pal("s15", "abre", 1), COR), ("x − 4", pal("s15", "xis", 1)), (")", pal("s15", "fecha", 1), COR)], XE, 680, 120)
    E.relogio(c, t, C["s16.a"], 1560, 400, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    form(c, t, C["s17"] + 0.2, Q, XE, 220, 110)

    def s17():
        x1, w1 = trecho_x(Q, "3(x + 2)", XE, 110)
        x2, w2 = trecho_x(Q, "− (x − 4)", XE, 110)
        form(c, t, a7, "3x + 6", x1 + w1 / 2, 400, 100, None, "center")
        E.foco(c, t, pal("s17", "segundo"), 0.4, lambda p: centro(c, "atalho: troca os sinais", x2 + w2 / 2, 320, 46, "i", COR, p))
        form(c, t, b7, "−x + 4", x2 + w2 / 2, 400, 100, COR, "center")
        form(c, t, c7, "3x − x = 2x", XE, 600, 100)
        form(c, t, d7, "6 + 4 = 10", 1000, 600, 100)
        E.frase(c, t, e7 - 0.6, ps("resposta:", "i", 84), XE, 830, passo=0.1)
        form(c, t, e7, "2x + 10", XE + 380, 840, 150, CERTO)
    fase(c, t, C["s17"], C["s18"] - 0.1, s17)

    def s18():
        form(c, t, C["s18"], "= 2x + 10", XE + fw(Q + " ", 110), 220, 110, CERTO)
        E.frase(c, t, C["s18"] + 0.3, ps("confira com 10:", "i", 72, TINTA2), XE, 420, passo=0.1)
        form(c, t, a8, "36 − 6 = 30", XE, 570, 110)
        form(c, t, b8, "2 × 10 + 10 = 30", XE, 720, 110)
        E.foco(c, t, b8 + 0.6, 0.45, lambda p: E.selo(c, 1220, 680, 56, True, p))
        E.frase(c, t, pal("s18", "quem"), ps("esqueceu de trocar o sinal do 4:", "i", 70, ERRADO), XE, 910, passo=0.1)
        form(c, t, c8, "2x + 2", XE + 1000, 915, 110, ERRADO)
    fase(c, t, C["s18"], 1e9, s18)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a1, b1 = C["s19.a"], C["s19.b"]

    def resumo():
        E.frase(c, t, C["s19"] + 0.3, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        E.foco(c, t, a1, 0.5, lambda p: num_bola(c, "1", 230, 430, 58, 66, p))
        E.frase(c, t, a1 + 0.1, ps("o número de fora multiplica", "i", 72) + ps("cada termo de dentro", "g", 64, COR), 320, 460, passo=0.11)
        E.foco(c, t, b1, 0.5, lambda p: num_bola(c, "2", 230, 650, 58, 66, p))
        E.frase(c, t, b1 + 0.1, ps("menos sozinho troca", "i", 84) + ps("todos os sinais", "g", 76, COR), 320, 680, passo=0.12)
        form(c, t, b1 + 0.8, "−(x − 3) = −x + 3", 320, 860, 100, COR)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a_, b_, c_, d_, e_ = (C[f"s20.{k}"] for k in "abcde")
    E.frase(c, t, C["s20"] + 0.2, ps("próxima aula", "i", 84), XE, 230)
    E.frase(c, t, a_, ps("letra por letra", "g", 120, COR), XE, 390)
    form(c, t, b_, "3x × 2x", XE, 560, 120)
    E.frase(c, t, c_, ps("e", "i", 84) + ps("dois parênteses", "g", 78, COR) + ps("multiplicados", "i", 84), XE, 720, passo=0.12)
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, d_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(620, 375, p), ep(t, d_ + 0.2, 0.4), TINTA)
    E.frase(c, t, e_, ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), 1450, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, combo=b_combo, negativo=b_negativo, menos=b_menos, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
