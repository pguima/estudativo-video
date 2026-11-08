"""Visual — Estudativo · MAT-EQU-006: praticando expressões algébricas.
Aula de prática: cinco situações, cada uma com selo de progresso, relógio de pausa e resposta passo a passo:
as figurinhas de Ana, Bia e Caio, o valor numérico com x = −2, os dois parênteses, a sala quadrada de lado 3x e o
terreno retangular. No palco, o teste do zero. A próxima aula aparece na balança.
Instantes: os cues de C[...] e, para cada palavra, pal(cena, palavra), lido da voz gravada em audio/tempos.json."""
import json
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-006_praticando_expressoes_algebricas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao3", "atalho", "questao5", "fim"))
BR = "#FFFFFF"

x = 10
assert x + (2 * x - 3) + (x + 5) == 4 * x + 2 == 42 and 10 + 17 + 15 == 42
x = -2
assert x ** 2 - 3 * x + 2 == 12 and 4 - 6 + 2 == 0
x = 0
assert 4 * (x - 2) - (2 * x - 5) == 2 * x - 3 == -3
x = 10
assert 3 * x * 3 * x == 9 * x ** 2 == 900 and 30 * 30 == 900
assert (x + 5) * (x + 2) == x ** 2 + 7 * x + 10 == 180 == 15 * 12 and 5 * 2 == 10
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




def marca(c, t, t0, n, escuro=False):
    """situação n de 5, com cinco pontos de progresso"""
    s = f"situação {n} de 5"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", a=a)
        for i in range(5):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def selo_em(c, t, t0, cx, cy, r=50, ok=True):
    E.foco(c, t, t0, 0.45, lambda p: E.selo(c, cx, cy, r, ok, p))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]
    E.frase(c, t, a_ + 0.1, ps("5", "g", 240, COR) + ps("situações", "g", 170, COR), XE, 350, passo=0.25)
    E.frase(c, t, a_ + 0.8, ps("com letra, criadas para esta aula", "i", 80), XE, 480, passo=0.12)
    for i, (s, cx) in enumerate((("pause", 440), ("resolva", 960), ("confira", 1480))):
        E.foco(c, t, b_ + i * 0.5, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 700, 56, 64, p), E.escreve(c, s, cx - 110, 725, 92, "g", TINTA, p)))
    E.frase(c, t, pal("s01", "errar"), ps("errar aqui não custa nada, e ensina", "i", 70, TINTA2), W / 2, 920, "center", 0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.3, ps("cinco", "g", 84, COR) + ps("ferramentas", "i", 90), XE, 170)
    itens = (("traduzir frases", "2x − 3"), ("trocar a letra entre parênteses", "x = −2 → (−2)"),
             ("juntar termos semelhantes", "3x + 5x = 8x"), ("abrir parênteses", "−(x − 3) = −x + 3"), ("multiplicar com letra", "3x × 2x = 6x^2"))
    for i, ((txt, ex), k) in enumerate(zip(itens, "abcde")):
        y = 300 + i * 150
        tk = C[f"s02.{k}"]
        E.foco(c, t, tk, 0.45, lambda p, i=i, y=y: num_bola(c, str(i + 1), XE + 40, y - 25, 40, 50, p))
        E.frase(c, t, tk, ps(txt, "i", 66), XE + 110, y, passo=0.08)
        form(c, t, tk + 0.4, ex, 1180, y, 64, COR)
    E.frase(c, t, pal("s02", "procure"), ps("travou? procure a aula no canal", "i", 54, TINTA2), 1250, 170, passo=0.08)


# ---------------- situação 1 ----------------
def b_questao1(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s03.{k}"] for k in "abcde")
    marca(c, t, a_, 1)

    def texto():
        for k, (nome, frase_, tk) in enumerate((("Ana", "tem x figurinhas", b_), ("Bia", "tem 3 a menos que o dobro de Ana", c_), ("Caio", "tem 5 a mais que Ana", d_))):
            y = 320 + k * 150
            E.frase(c, t, tk - 0.3, ps(nome, "g", 80, COR), XE, y)
            E.frase(c, t, tk, ps(frase_, "i", 76), XE + 230, y, passo=0.1)
        E.frase(c, t, e_, ps("escreva, na forma mais curta,", "i", 76), XE, 790, passo=0.1)
        E.frase(c, t, e_ + 1.2, ps("quantas eles têm", "i", 90) + ps("juntos", "g", 84, COR), XE, 910, passo=0.12)
    texto()
    E.relogio(c, t, C["s04.a"], 1560, 420, 170)


def b_resposta1(c, t, C, b):
    marca(c, t, C["s05"] - 0.5, 1)
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    J = "x + 2x − 3 + x + 5"

    def s05():
        E.frase(c, t, a5 - 0.3, ps("Ana:", "g", 76, COR), XE, 280)
        form(c, t, a5, "x", XE + 260, 285, 100)
        E.frase(c, t, b5 - 0.3, ps("Bia:", "g", 76, COR), XE, 430)
        form(c, t, pal("s05", "dois"), "2x", XE + 260, 435, 100)
        form(c, t, pal("s05", "tire"), "− 3", XE + 260 + fw("2x ", 100), 435, 100)
        E.foco(c, t, pal("s05", "quem"), 0.45, lambda p: (E.formula(c, "3 − 2x", 1100, 430, 80, cor=ERRADO, a=p),
                                                          E.escreve(c, "inverteu a ordem", 1100, 500, 50, "i", ERRADO, p)))
        if t >= pal("s05", "quem") + 0.6:
            E.risco(c, 1080, 450, 1360, 370, t, pal("s05", "quem") + 0.6, largura=10)
        E.frase(c, t, c5 - 0.2, ps("Caio:", "g", 76, COR), XE, 580)
        form(c, t, c5 + 0.6, "x + 5", XE + 260, 585, 100)
        E.frase(c, t, pal("s05", "juntos") - 0.2, ps("juntos:", "i", 80), XE, 800)
        monta(c, t, [("x", d5), (" + 2x", pal("s05", "mais", 1)), (" − 3", pal("s05", "menos", 3)), (" + x", pal("s05", "mais", 2)),
                     (" + 5", pal("s05", "mais", 3))], XE + 280, 805, 110)
    fase(c, t, C["s05"], C["s06"] - 0.1, s05)

    def s06():
        realce(c, t, a6, J, "x", XE, 260, 100)
        realce(c, t, a6 + 0.3, J, "+ 2x", XE, 260, 100)
        realce(c, t, a6 + 0.6, J, "+ x", XE, 260, 100)
        realce(c, t, b6, J, "− 3", XE, 260, 100, TINTA2)
        realce(c, t, b6 + 0.3, J, "+ 5", XE, 260, 100, TINTA2)
        form(c, t, C["s06"], J, XE, 260, 100)
        form(c, t, a6, "1 + 2 + 1 = 4  →  4x", XE, 420, 90, COR)
        form(c, t, b6, "−3 + 5 = +2", XE, 550, 90, TINTA2)
        E.frase(c, t, c6 - 0.5, ps("resposta:", "i", 76), XE, 730, passo=0.1)
        form(c, t, c6, "4x + 2", XE + 360, 740, 140, CERTO)
        E.frase(c, t, pal("s06", "se"), ps("Ana com 10:", "i", 60, TINTA2), XE, 900, passo=0.1)
        form(c, t, d6, "10 + 17 + 15 = 42", XE + 360, 905, 80)
        form(c, t, e6, "4 × 10 + 2 = 42", XE + 360, 1010, 80)
        selo_em(c, t, e6 + 0.6, 1180, 960, 46)
    fase(c, t, C["s06"], 1e9, s06)


# ---------------- situação 2 ----------------
def b_questao2(c, t, C, b):
    a_, b_, c_ = C["s07.a"], C["s07.b"], C["s07.c"]
    marca(c, t, a_, 2)
    E.frase(c, t, pal("s07", "calcule"), ps("calcule", "i", 100), XE, 380)
    form(c, t, b_, "x^2 − 3x + 2", XE, 600, 170)
    E.frase(c, t, c_ - 0.3, ps("para", "i", 100), XE, 820)
    form(c, t, c_, "x = −2", XE + 230, 825, 130, COR)
    E.relogio(c, t, C["s08.a"], 1560, 440, 180)


def b_resposta2(c, t, C, b):
    marca(c, t, C["s09"] - 0.5, 2)
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    S = 110
    L1 = "(−2)^2 − 3 × (−2) + 2"
    form(c, t, C["s09"] + 0.2, "x^2 − 3x + 2, x = −2", W - 120, 110, 56, TINTA2, "right")
    realce(c, t, b9, L1, "(−2)^2", XE, 290, S, t1=a0)
    realce(c, t, c9, L1, "3 × (−2)", XE, 290, S, t1=a0)
    monta(c, t, [("(", a9, COR), ("−2", pal("s09", "menos"), COR), (")", pal("s09", "fecha"), COR), ("^2", pal("s09", "ao"), COR),
                 (" − 3 × ", pal("s09", "menos", 1)), ("(", pal("s09", "abre", 1), COR), ("−2", pal("s09", "menos", 2), COR),
                 (")", pal("s09", "fecha", 1), COR), (" + 2", pal("s09", "mais"))], XE, 290, S)
    form(c, t, b9 + 0.3, "(−2)^2 = 4", 1350, 250, 64, COR)
    form(c, t, c9 + 0.3, "3 × (−2) = −6", 1350, 340, 64, COR)
    L2 = "= 4 − (−6) + 2"
    realce(c, t, pal("s10", "tirar"), L2, "− (−", XE, 490, S, t1=b0)
    monta(c, t, [("= 4 − ", a0), ("(", pal("s10", "abre"), COR), ("−6", pal("s10", "menos", 1), COR), (")", pal("s10", "fecha"), COR),
                 (" + 2", pal("s10", "mais"))], XE, 490, S)
    E.foco(c, t, pal("s10", "tirar"), 0.5, lambda p: E.pilula(c, "tirar uma dívida é como ganhar", 1320, 470, 48, estilo="b", a=p))
    form(c, t, b0, "= 4 + 6 + 2", XE, 690, S)
    form(c, t, c0 - 0.2, "=", XE + fw("= 4 + 6 + 2 ", S), 690, S)
    bola_em(c, t, c0, "12", XE + fw("= 4 + 6 + 2 = ", S) + 110, 650, 105, 110, CERTO)
    E.frase(c, t, pal("s10", "quem"), ps("perdeu o sinal:", "i", 70, ERRADO), XE, 920, passo=0.1)
    form(c, t, pal("s10", "quatro", 2), "4 − 6 + 2 =", XE + 480, 925, S, ERRADO)
    form(c, t, d0, "0", XE + 480 + fw("4 − 6 + 2 = ", S), 925, S, ERRADO)
    if t >= d0 + 0.5:
        E.risco(c, XE + 460, 955, XE + 480 + fw("4 − 6 + 2 = 0", S) + 20, 840, t, d0 + 0.5, largura=12)


# ---------------- situação 3 ----------------
Q3 = "4(x − 2) − (2x − 5)"


def b_questao3(c, t, C, b):
    a_, b_, c_ = C["s11.a"], C["s11.b"], C["s11.c"]
    marca(c, t, a_, 3)
    E.frase(c, t, pal("s11", "simplifique"), ps("simplifique", "i", 110), XE, 420)
    monta(c, t, [("4", b_), ("(", pal("s11", "abre"), COR), ("x − 2", pal("s11", "xis")), (")", pal("s11", "fecha"), COR),
                 (" − ", c_), ("(", pal("s11", "abre", 1), COR), ("2x − 5", pal("s11", "dois", 1)), (")", pal("s11", "fecha", 1), COR)], XE, 680, 120)
    E.relogio(c, t, C["s12.a"], 1560, 400, 170)


def b_resposta3(c, t, C, b):
    marca(c, t, C["s13"] - 0.5, 3)
    a_, b_, c_, d_, e_ = (C[f"s13.{k}"] for k in "abcde")
    form(c, t, C["s13"] + 0.2, Q3, XE, 280, 110)
    x1, w1 = trecho_x(Q3, "4(x − 2)", XE, 110)
    x2, w2 = trecho_x(Q3, "− (2x − 5)", XE, 110)
    form(c, t, a_, "4x − 8", x1 + w1 / 2, 450, 100, None, "center")
    E.foco(c, t, pal("s13", "o"), 0.4, lambda p: centro(c, "menos sozinho: troca todos os sinais", x2 + w2 / 2, 370, 44, "i", COR, p))
    form(c, t, b_, "−2x + 5", x2 + w2 / 2, 450, 100, COR, "center")
    form(c, t, c_, "4x − 2x = 2x", XE, 640, 100)
    form(c, t, d_, "−8 + 5 = −3", 1000, 640, 100)
    E.frase(c, t, e_ - 0.6, ps("resposta:", "i", 84), XE, 860, passo=0.1)
    form(c, t, e_, "2x − 3", XE + 380, 870, 150, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    AM = "#FFD500"
    a4, b4, c4, d4, e4, f4 = (C[f"s14.{k}"] for k in "abcdef")

    def s14():
        E.frase(c, t, C["s14"] + 0.3, ps("um atalho de prova:", "i", 76, CLARO) + ps("o teste do zero", "g", 76, BR), W / 2, 170, "center", 0.11)
        form(c, t, b4, Q3, W / 2, 330, 110, BR, "center")
        form(c, t, b4 + 1.2, "4(0 − 2) − (2 × 0 − 5)", W / 2, 470, 90, AM, "center")
        form(c, t, c4, "0 − 2 = −2", 330, 640, 80, CLARO)
        form(c, t, pal("s14", "quatro"), "4 × (−2) = −8", 330, 750, 80, BR)
        form(c, t, d4, "2 × 0 = 0", 1080, 640, 80, CLARO)
        form(c, t, pal("s14", "zero", 5), "0 − 5 = −5", 1080, 750, 80, CLARO)
        form(c, t, pal("s14", "abre"), "−(−5) = +5", 1080, 860, 80, BR)
        form(c, t, e4, "−8 + 5 = −3", 330, 960, 100, AM)
        E.foco(c, t, f4, 0.45, lambda p: (E.selo(c, 1110, 930, 46, True, p), E.formula(c, "o solto de 2x − 3", 1190, 950, 60, "b", CLARO, p)))
    fase(c, t, C["s14"], C["s15"] - 0.1, s14)

    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")

    def s15():
        E.frase(c, t, C["s15"] + 0.2, ps("funciona porque", "i", 84, CLARO), W / 2, 210, "center")
        form(c, t, a5, "0 × qualquer número = 0", W / 2, 380, 100, BR, "center")
        E.frase(c, t, pal("s15", "todo"), ps("todo termo com x some,", "i", 80, CLARO), W / 2, 520, "center", 0.11)
        E.frase(c, t, b5, ps("sobra só o", "i", 80, CLARO) + ps("número solto", "g", 76, BR), W / 2, 630, "center", 0.11)
        E.frase(c, t, c5, ps("mas não confere a parte com x", "i", 76, CLARO), W / 2, 790, "center", 0.1)
        E.foco(c, t, d5, 0.5, lambda p: E.pilula(c, "para isso: o teste do 10", W / 2, 920, 60, estilo="b", fundo=E.COR, cor=BR, a=p))
    fase(c, t, C["s15"], 1e9, s15)


# ---------------- situação 4 ----------------
def sala(c, x0, y0, l, a, lado="3x"):
    """sala quadrada vista de cima, com o lado marcado em cima e à esquerda"""
    M.rrect(c, x0, y0, l, l, 10, M.mix(E.COR, BR, 0.8), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y0, l, l), 10, 10), M.paint(E.COR, a, stroke=5))
    E.formula(c, lado, x0 + l / 2, y0 - 30, 70, cor=COR, a=a, align="center")
    E.formula(c, lado, x0 - 30, y0 + l / 2 + 25, 70, cor=COR, a=a, align="right")


def b_questao4(c, t, C, b):
    a_, b_, c_ = C["s16.a"], C["s16.b"], C["s16.c"]
    marca(c, t, a_, 4)
    E.frase(c, t, pal("s16", "uma"), ps("uma sala", "i", 90) + ps("quadrada", "g", 84, COR), XE, 360, passo=0.12)
    E.frase(c, t, b_ - 0.3, ps("de lado", "i", 90), XE, 500, passo=0.12)
    form(c, t, b_, "3x metros", XE + 300, 505, 100, COR)
    E.frase(c, t, c_, ps("escreva a", "i", 100) + ps("área", "g", 96, COR), XE, 760, passo=0.12)
    E.saida(c, t, C["s17"] - 0.1, lambda: E.foco(c, t, b_, 0.5, lambda p: sala(c, 1250, 330, 440, p)))
    E.relogio(c, t, C["s17.a"], 1490, 440, 200)


def b_resposta4(c, t, C, b):
    marca(c, t, C["s18"] - 0.5, 4)
    a_, b_, c_, d_, e_, f_, g_, h_ = (C[f"s18.{k}"] for k in "abcdefgh")
    E.frase(c, t, pal("s18", "área"), ps("área do quadrado = lado × lado", "i", 72, TINTA2), XE, 240, passo=0.1)
    form(c, t, a_, "3x × 3x", XE, 400, 120)
    form(c, t, b_, "3 × 3 = 9", XE, 560, 100, COR)
    form(c, t, c_, "x × x = x^2", 700, 560, 100)
    E.frase(c, t, d_ - 0.5, ps("resposta:", "i", 80), XE, 740, passo=0.1)
    form(c, t, d_, "9x^2", XE + 350, 750, 150, CERTO)
    for k, (s, tk, nota) in enumerate((("6x", e_, "somou"), ("9x", f_, "esqueceu uma letra"))):
        x = 1240 + k * 300
        form(c, t, tk, s, x, 420, 110, ERRADO)
        E.foco(c, t, tk + 0.3, 0.4, lambda p, x=x, nota=nota: E.escreve(c, nota, x, 490, 44, "i", ERRADO, p))
        if t >= tk + 0.5:
            E.risco(c, x - 10, 440, x + 160, 340, t, tk + 0.5, largura=10)
    E.frase(c, t, pal("s18", "com", 1), ps("com 10:", "i", 64, TINTA2), XE, 940, passo=0.1)
    form(c, t, g_, "30 × 30 = 900", XE + 250, 945, 90)
    form(c, t, h_, "9 × 100 = 900", 1120, 945, 90)
    selo_em(c, t, h_ + 0.6, 1800, 910, 46)


# ---------------- situação 5 ----------------
def terreno(c, x0, y0, w, h, a):
    M.rrect(c, x0, y0, w, h, 10, M.mix(E.COR, BR, 0.8), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y0, w, h), 10, 10), M.paint(E.COR, a, stroke=5))


def b_questao5(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s19.{k}"] for k in "abcd")
    marca(c, t, a_, 5)
    E.frase(c, t, a_, ps("a última junta tudo", "i", 70, COR), XE, 240, passo=0.1)
    E.frase(c, t, pal("s19", "um"), ps("um terreno", "i", 88) + ps("retangular", "g", 82, COR), XE, 370, passo=0.12)
    E.frase(c, t, b_, ps("frente:", "i", 80), XE, 510, passo=0.1)
    form(c, t, b_ + 0.4, "x + 5", XE + 280, 515, 100, COR)
    E.frase(c, t, c_, ps("fundo:", "i", 80), XE, 650, passo=0.1)
    form(c, t, c_ + 0.4, "x + 2", XE + 280, 655, 100, COR)
    E.frase(c, t, d_, ps("escreva a área", "i", 90) + ps("sem parênteses", "g", 84, COR), XE, 860, passo=0.12)

    def desenho():
        E.foco(c, t, b_, 0.5, lambda p: (terreno(c, 1150, 380, 600, 380, p), E.formula(c, "x + 5", 1450, 350, 70, cor=COR, a=p, align="center")))
        E.foco(c, t, c_, 0.5, lambda p: E.formula(c, "x + 2", 1130, 590, 70, cor=COR, a=p, align="right"))
    E.saida(c, t, C["s20"] - 0.1, desenho)
    E.relogio(c, t, C["s20.a"], 1490, 440, 200)


def b_resposta5(c, t, C, b):
    marca(c, t, C["s21"] - 0.5, 5)
    a1, b1, c1, d1 = (C[f"s21.{k}"] for k in "abcd")
    a2, b2, c2, d2 = (C[f"s22.{k}"] for k in "abcd")
    E.frase(c, t, pal("s21", "área"), ps("área do retângulo = um lado × o outro", "i", 66, TINTA2), XE, 230, passo=0.1)
    monta(c, t, [("(", a1, COR), ("x + 5", pal("s21", "xis")), (")", pal("s21", "fecha"), COR),
                 ("(", pal("s21", "abre", 1), COR), ("x + 2", pal("s21", "xis", 1)), (")", pal("s21", "fecha", 1), COR)], XE, 390, 120)
    form(c, t, a2, "= x^2 + 7x + 10", XE + fw("(x + 5)(x + 2) ", 120), 390, 120, CERTO)

    def s21():
        E.frase(c, t, pal("s21", "pelo"), ps("pelo atalho:", "i", 66, TINTA2), XE, 540, passo=0.1)
        for k, (lab, conta, res, tk) in enumerate((("na frente", "", "x^2", b1), ("no meio", "5 + 2 = 7", "+ 7x", c1), ("no fim", "5 × 2 = 10", "+ 10", d1))):
            cx = 400 + k * 520
            E.frase(c, t, tk, ps(lab, "i", 64), cx, 650, "center")
            if conta:
                form(c, t, tk + 0.7, conta, cx, 760, 70, TINTA2, "center")
            form(c, t, tk + (1.6 if conta else 0.5), res, cx, 930, 140, COR, "center")
    fase(c, t, C["s21"], C["s22"] - 0.1, s21)

    def s22():
        E.frase(c, t, pal("s22", "confira"), ps("confira com os testes", "i", 66, TINTA2), XE, 560, passo=0.1)
        E.frase(c, t, b2, ps("x = 0:", "g", 66, COR), XE, 700)
        form(c, t, b2 + 1.5, "5 × 2 = 10", XE + 250, 705, 90)
        E.foco(c, t, pal("s22", "o"), 0.4, lambda p: E.escreve(c, "o número solto bate", 900, 700, 56, "i", CERTO, p))
        E.frase(c, t, c2, ps("x = 10:", "g", 66, COR), XE, 860)
        form(c, t, c2 + 2.0, "15 × 12 = 180", XE + 250, 865, 90)
        form(c, t, d2, "100 + 70 + 10 = 180", XE + 250, 990, 90)
        selo_em(c, t, d2 + 0.8, 1300, 950, 50)
    fase(c, t, C["s22"], 1e9, s22)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a1, b1, c1 = C["s23.a"], C["s23.b"], C["s23.c"]

    def resumo():
        E.frase(c, t, C["s23"] + 0.3, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        for i, (tk, partes) in enumerate(((a1, ps("traduza", "i", 84) + ps("pedaço por pedaço", "g", 76, COR)),
                                          (b1, ps("troque a letra sempre com", "i", 84) + ps("parênteses", "g", 76, COR)),
                                          (c1, ps("confira com", "i", 84) + ps("um número", "g", 76, COR)))):
            y = 420 + i * 200
            E.foco(c, t, tk, 0.5, lambda p, i=i, y=y: num_bola(c, str(i + 1), 230, y - 30, 58, 66, p))
            E.frase(c, t, tk + 0.1, partes, 320, y, passo=0.12)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    a_, b_, c_, d_, e_ = (C[f"s24.{k}"] for k in "abcde")
    E.frase(c, t, C["s24"] + 0.2, ps("próxima aula", "i", 84), XE, 230)
    E.frase(c, t, a_, ps("o sinal de igual:", "i", 84) + ps("equação", "g", 96, COR), XE, 380, passo=0.12)
    E.frase(c, t, pal("s24", "você"), ps("teste se um número resolve", "i", 70), XE, 490, passo=0.1)
    E.foco(c, t, b_, 0.6, lambda p: E.balanca(c, 620, 800, "x + 2", "5", 0, p, 70, 520))
    E.frase(c, t, c_, ps("o mesmo", "g", 70, COR) + ps("nos dois lados", "i", 76), 1050, 690, passo=0.12)
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, d_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(620, 375, p), ep(t, d_ + 0.2, 0.4), TINTA)
    E.frase(c, t, e_, ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), 1450, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4,
              resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
