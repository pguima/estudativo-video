"""Visual — Estudativo · MAT-FRA-019: fração em decimal e decimal em fração.
A reta numérica desmente 3/8 = 3,8. A conta na chave vem de E.dividir, então tela e conta não têm como divergir.
Todo instante vem de C[...]; o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
from decimal import Decimal as D
from fractions import Fraction as F

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, palco, centro, linha
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-019_fracao_em_decimal_e_decimal_em_fracao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("conta", "volta", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert F(3, 8) == F("0.375") and F(5, 8) == F("0.625") and F(1, 2) == F("0.5")
assert F("0.6") == F(3, 5) and F("0.35") == F(7, 20) and F("0.28") == F(7, 25) and 35 // 5 == 7 and 100 // 5 == 20 and 28 // 4 == 7 and 100 // 4 == 25
assert D(35) / 10 == D("3.5") and 20 * 5 == 100 and 7 * 5 == 35 and 8 * 125 == 1000


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


def txt(c, t, ti, s, x, y, size=64, cor=None, est="b"):
    E.foco(c, t, ti, 0.45, lambda a: E.escreve(c, s, x, y, size, est, cor or TINTA, a))


def cen(c, t, ti, s, x, y, size=64, cor=None, est="g"):
    E.foco(c, t, ti, 0.45, lambda a: centro(c, s, x, y, size, est, cor or TINTA, a))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE if cor is None else M.on(cor), a)


def troca(c, t, itens, x, y, size=66, est="b", cor=None):
    """uma linha de cada vez: itens = [(instante, texto)], cada uma sai quando a próxima chega"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        E.saida(c, t, fim, lambda s=s, ti=ti: txt(c, t, ti, s, x, y, size, cor, est), d=0.25)


def sobra(c, t, t0, t1, s, x, y, size, lin, col):
    """o resto sozinho na conta, até o zero chegar: col = coluna do último algarismo do resto"""
    cl = E.casa(size)
    E.saida(c, t, t1, lambda: E.foco(c, t, t0, 0.35, lambda a: [centro(c, ch, x + (col - (len(s) - 1 - i) + 0.5) * cl, y + lin * size * 1.12, size, "g", TINTA, a) for i, ch in enumerate(s)]), d=0.01)


def lembrete(c, t, C, cena, n, nome, itens):
    """itens = [(cue, linha fina, linha forte)]"""
    E.frase(c, t, C[cena] + 0.1, ps("você precisa de", "i", 84), XE, 410, "left", 0.18)
    E.foco(c, t, C[f"{cena}.a"], 0.5, lambda a: E.escreve(c, n, XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[f"{cena}.a"] + 0.15, 0.5, lambda a: E.escreve(c, nome, XE + 245, 700, 120, "i", TINTA, a))
    x, w, y0 = 960, 780, 280
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    ks = [k for k, _, _ in itens]
    py = y0 + 170
    for i in range(1, len(ks)):
        py = lerp(py, y0 + i * 280 + 170, ease_io(prog(t, C[ks[i]] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C[ks[0]], 0.4))
    E.frase(c, t, lerp(C[ks[-1]], C[f"{cena}.end"], 0.72), ps("faltou?", "i", 60, COR) + ps("procure no canal", "i", 60), XE, 860, "left", 0.15)


def promessa(c, t, ta, tb):
    E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 290 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
    f = lambda q: lerp(ta, tb, q)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 320, "left", 0.13)
    E.frase(c, t, f(0.45), [("fração", "g", 124, COR)], XE, 480)
    E.frase(c, t, f(0.52), ps("por decimal", "i", 116), XE, 600, "left", 0.15)
    E.frase(c, t, f(0.7), [("decimal", "g", 124, COR)], XE, 760)
    E.frase(c, t, f(0.78), ps("por fração", "i", 116), XE, 880, "left", 0.15)
    E.foco(c, t, tb + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1450, 505, 88, "g", E.SOBRE, a), centro(c, "de prova", 1450, 600, 92, "i", E.SOBRE, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def erro():
        y, s = 300, 150
        fr(c, t, a_, 3, 8, 620, y - 40, s, COR)
        cen(c, t, b_, "=", 830, y, 130, TINTA2)
        cen(c, t, b_ + 0.15, "?", 960, y - 60, 90, ERRADO)
        txt(c, t, b_ + 0.2, "3,8", 1040, y, 170, ERRADO, "g")
        x0, x1, yr = 330, 1590, 700
        vx = E.reta(c, t, c_ - 0.4, x0, x1, yr, 0, 4, [0, 1, 2, 3, 4], size=60)
        for v, lab, ti, cor, fala in ((3 / 8, "3/8", c_, COR, "menos que um inteiro"), (3.8, "3,8", d_, ERRADO, "quase quatro inteiros")):
            E.foco(c, t, ti, 0.45, lambda a, v=v, lab=lab, cor=cor: (c.drawCircle(vx(v), yr, 26, M.paint(cor, a)), centro(c, lab, vx(v), yr - 54, 76, "g", cor, a)))
        E.frase(c, t, c_ + 0.3, ps("menos que", "i", 70) + [("1 inteiro", "g", 64, COR)], 700, 900, "center", 0.15)
        E.frase(c, t, d_ + 0.3, ps("quase", "i", 70) + [("4 inteiros", "g", 64, ERRADO)], 1300, 900, "center", 0.15)
        ti = lerp(d_, C["s01.end"], 0.55)
        E.frase(c, t, ti, ps("não pode ser o mesmo número", "i", 80), W / 2, 1010, "center", 0.12)
        if t >= ti:
            E.risco(c, 1010, 270, 1320, 215, t, ti, largura=14)
    E.saida(c, t, C["s02"] - 0.1, erro)
    if t >= C["s02"]:
        promessa(c, t, C["s02.a"], C["s02.b"])


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", "2", "coisas", (("s03.b", "continuar uma divisão", "depois da vírgula"), ("s03.c", "simplificar", "uma fração")))


# ---------------- o traço é divisão ----------------
def b_traco(c, t, C, b):
    a_, b_, c_, d_ = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    E.frase(c, t, a_, ps("o traço da fração é uma", "i", 96) + [("divisão", "g", 96, COR)], W / 2, 200, "center", 0.15)
    s = 124
    y1, y2 = 370, 640
    fr(c, t, b_, 12, 4, 500, y1, s, COR)
    cen(c, t, b_ + 0.5, "=", 720, y1 + 44, 120, TINTA2)
    txt(c, t, b_ + 1.0, "12 ÷ 4", 820, y1 + 50, 136, TINTA, "g")
    fr(c, t, c_, 1, 2, 500, y2, s, COR)
    cen(c, t, c_ + 0.5, "=", 720, y2 + 44, 120, TINTA2)
    txt(c, t, c_ + 1.0, "1 ÷ 2", 820, y2 + 50, 136, TINTA, "g")
    cen(c, t, d_ - 0.1, "=", 1240, y2 + 44, 120, TINTA2)
    E.foco(c, t, d_, 0.5, lambda a: num_bola(c, "0,5", 1460, y2 - 2, 140, 110, a))
    a5 = C["s05.a"]
    E.frase(c, t, C["s05"] + 0.2, ps("para virar decimal,", "i", 76), W / 2, 870, "center", 0.14)
    E.frase(c, t, a5, ps("divida", "g", 92, COR) + ps("o de cima pelo de baixo", "i", 88), W / 2, 980, "center", 0.14)


# ---------------- três oitavos ----------------
def b_conta(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]

    Dv = E.dividir("3", 8)
    x, y, s = 260, 250, 112

    def conta():
        E.foco(c, t, a6, 0.5, lambda q: E.fracao(c, 3, 8, 1560, 215, 118, COR, q))
        E.conta_div(c, t, Dv, [b6, lerp(a7, b7, 0.45), lerp(b7, c7, 0.45), lerp(c7, d7, 0.75)], [c6 + 0.5, b7, c7, d7], a6 + 0.5, x, y, s, tv=b6)
        sobra(c, t, lerp(a7, b7, 0.8), b7, "6", x, y, s, 2, 1)
        sobra(c, t, lerp(b7, c7, 0.65), c7, "4", x, y, s, 3, 2)
        tl = [(a6 + 0.5, "3 ÷ 8"), (lerp(a6, b6, 0.55), "3 é menor que 8"), (b6, "0 e vírgula"), (c6, "ponha um zero: 30"), (a7, "30 ÷ 8 = 3"), (lerp(a7, b7, 0.75), "sobram 6"),
              (b7, "60 ÷ 8 = 7"), (lerp(b7, c7, 0.6), "sobram 4"), (c7, "40 ÷ 8 = 5"), (d7, "não sobra nada")]
        troca(c, t, tl, 1020, 600, 88)
    E.saida(c, t, a8 - 0.1, conta)
    if t >= a8:
        y2 = 400
        fr(c, t, a8, 3, 8, 470, y2 - 30, 170, COR)
        cen(c, t, a8 + 0.4, "=", 680, y2 + 30, 130, TINTA2)
        E.foco(c, t, a8 + 0.6, 0.5, lambda q: E.numero(c, "0,375", 960, y2 + 40, 200, cor=COR, a=q))
        E.frase(c, t, b8 - 0.9, ps("menos que um inteiro,", "i", 84), W / 2, 680, "center", 0.14)
        E.frase(c, t, b8, ps("como tinha que ser", "i", 84, COR), W / 2, 790, "center", 0.14)
        E.frase(c, t, c8, ps("o", "i", 92) + [("mesmo número,", "g", 92, COR)] + ps("escrito de jeitos diferentes", "i", 84), W / 2, 930, "center", 0.14)


# ---------------- decimal em fração ----------------
def b_volta(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")

    def seis():
        E.frase(c, t, C["s09"] + 0.1, ps("e o caminho de volta?", "i", 84), W / 2, 180, "center", 0.14)
        E.frase(c, t, a9, ps("leia o número", "i", 96) + [("em voz alta", "g", 92, COR)], W / 2, 310, "center", 0.15)
        y, s = 600, 170
        E.foco(c, t, b9, 0.45, lambda a: E.numero(c, "0,6", 320, y + 60, 180, a=a))
        cen(c, t, b9 + 0.5, "=", 560, y + 50, 120, TINTA2)
        E.frase(c, t, b9 + 0.8, [("seis", "i", 84)], 370, 840)
        E.frase(c, t, b9 + 1.0, [("décimos", "g", 76, COR)], 370, 930)
        fr(c, t, c9, 6, 10, 760, y, s, COR)
        E.pontes(c, t, 890, 1190, y, s, "÷ 2", d9, d9 + 0.1, size=56)
        E.foco(c, t, e9, 0.5, lambda a: (E.bola(c, 1370, y + 3, 170, CERTO, a), E.fracao(c, 3, 5, 1370, y, 130, BR, a)))
    E.saida(c, t, C["s10"] - 0.1, seis)
    if C["s10"] - 0.1 <= t < C["s11"]:
        def regra():
            a_, b_, c_, d_, e_, f_ = (C[f"s10.{k}"] for k in "abcdef")
            E.frase(c, t, a_, ps("o número sem vírgula vai", "i", 88) + [("em cima", "g", 88, COR)], W / 2, 180, "center", 0.14)
            E.frase(c, t, b_, ps("embaixo:", "i", 88) + [("1 + um zero por casa", "g", 84, COR)], W / 2, 300, "center", 0.14)
            cols = (520, 960, 1400)
            for i, (ti, ca, de, no) in enumerate(((c_, "1 casa", "10", "décimos"), (d_, "2 casas", "100", "centésimos"), (e_, "3 casas", "1.000", "milésimos"))):
                y = 470 + i * 140
                cen(c, t, ti - 0.5, ca, cols[0], y, 84, TINTA, "i")
                cen(c, t, ti, de, cols[1], y, 100, COR)
                cen(c, t, ti + 0.3, no, cols[2], y, 88, TINTA, "i")
            E.frase(c, t, f_, ps("depois,", "i", 88) + [("simplifique, se der", "g", 84, COR)], W / 2, 920, "center", 0.14)
        E.saida(c, t, C["s11"] - 0.1, regra)
    if t >= C["s11"]:
        a_, b_, c_, d_, e_, f_ = (C[f"s11.{k}"] for k in "abcdef")
        y, s, x0, x1 = 520, 170, 830, 1470
        E.foco(c, t, a_, 0.45, lambda q: E.numero(c, "0,35", 290, y + 56, 146, a=q))
        cen(c, t, b_ - 0.2, "=", 610, y + 50, 120, TINTA2)
        fr(c, t, b_, 35, 100, x0, y, s, COR)
        E.frase(c, t, b_, ps("duas casas:", "i", 80) + [("centésimos", "g", 80, COR)], W / 2, 220, "center", 0.14)
        E.frase(c, t, lerp(b_, c_, 0.26), ps("35 termina em 5,", "i", 72) + ps("100 termina em 0", "i", 72), W / 2, 830, "center", 0.11)
        E.pontes(c, t, x0 + 170, x1 - 200, y, s, "÷ 5", d_, e_, size=60)
        if t < f_:
            E.frac_q(c, t, c_, 7, 20, lerp(d_, e_, 0.6), lerp(e_, f_, 0.6), x1, y, s)
        E.foco(c, t, f_, 0.5, lambda a: (E.bola(c, x1, y + 3, 170, CERTO, a), E.fracao(c, 7, 20, x1, y, 130, BR, a)))
        E.frase(c, t, c_, ps("divida em cima e embaixo por 5", "i", 76), W / 2, 950, "center", 0.11)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s12.{k}"] for k in "abcde")
    E.frase(c, t, C["s12"] + 0.1, [("cuidado", "g", 104, ERRADO)] + ps("com um erro comum", "i", 88), W / 2, 200, "center", 0.15)
    E.frase(c, t, a_, ps("errar o", "i", 96) + [("número de zeros", "g", 92, ERRADO)], W / 2, 330, "center", 0.15)
    y, s = 600, 150
    E.foco(c, t, b_ - 0.3, 0.45, lambda q: E.numero(c, "0,35", 290, y + 50, 140, a=q))
    cen(c, t, b_ - 0.1, "=", 600, y + 45, 110, TINTA2)
    certo = t >= e_
    if not certo:
        fr(c, t, b_, 35, 10, 800, y, s, ERRADO)
    else:
        E.foco(c, t, e_, 0.45, lambda a: E.fracao(c, 35, 100, 800, y, s, CERTO, a))
    txt(c, t, c_, "35 ÷ 10 = 3,5", 1020, y - 20, 96, TINTA, "g")
    E.frase(c, t, d_, [("10 vezes maior", "g", 84, ERRADO)], 1020, y + 100)
    E.frase(c, t, e_, ps("2 casas,", "i", 100) + [("2 zeros", "g", 100, CERTO)], W / 2, 930, "center", 0.15)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]

    def cem():
        E.frase(c, t, C["s13"] + 0.1, ps("agora, o atalho", "i", 80, CLARO), W / 2, 170, "center")
        E.frase(c, t, a3, ps("faça o de baixo virar", "i", 96, BR) + [("10 ou 100", "g", 96, CLARO)], W / 2, 300, "center", 0.15)
        y, s, x0, x1 = 600, 170, 330, 860
        fr(c, t, b3 - 0.6, 7, 20, x0, y, s, BR)
        E.pontes(c, t, x0 + 130, x1 - 170, y, s, "× 5", c3, b3, CLARO, size=56)
        def dir_(a):
            E.fracao(c, 35 if t >= c3 + 0.3 else "?", 100, x1, y, s, CLARO, a)
        E.foco(c, t, b3 + 0.3, 0.45, dir_)
        cen(c, t, d3 - 0.1, "=", 1100, y + 50, 130, BR)
        E.foco(c, t, d3 + 0.5, 0.5, lambda a: E.numero(c, "0,35", 1340, y + 60, 180, cor=CLARO, a=a))
        E.frase(c, t, lerp(d3, C["s13.end"], 0.6), ps("sem armar a divisão", "i", 84, BR), W / 2, 920, "center", 0.14)
    E.saida(c, t, C["s14"] - 0.1, cem)
    if t < C["s14"]:
        return
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, a4, ps("você troca por uma", "i", 84, BR) + [("fração equivalente", "g", 84, CLARO)], W / 2, 200, "center", 0.14)
    E.frase(c, t, lerp(a4, b4, 0.4), ps("com 100 embaixo, se lê direto como decimal", "i", 76, BR), W / 2, 310, "center", 0.11)
    y, s = 620, 170
    E.frase(c, t, b4 - 0.8, ps("não compensa em", "i", 88, CLARO), XE, y + 40, "left", 0.15)
    fr(c, t, b4, 3, 8, 930, y, s, BR)
    txt(c, t, lerp(b4, c4, 0.35), "8 × 125 = 1.000", 1080, y + 30, 84, CLARO, "g")
    E.frase(c, t, c4, ps("aí,", "i", 104, CLARO) + [("divida", "g", 110, BR)], W / 2, 930, "center", 0.15)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_, c_, d_ = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    y1, y2 = 310, 670
    E.frase(c, t, a_ - 0.5, ps("tábua de", "i", 92), XE, y1 + 30, "left", 0.15)
    E.foco(c, t, a_, 0.5, lambda q: (E.fracao(c, 5, 8, 640, y1, 104, COR, q)))
    txt(c, t, a_ + 0.6, "de metro", 720, y1 + 30, 92, TINTA, "i")
    E.frase(c, t, b_, ps("quanto é", "i", 88) + [("em decimal?", "g", 84, COR)], XE, y1 + 200, "left", 0.15)
    linha(c, t, [("tábua de", "i", 92, TINTA, c_ - 0.5), ("0,28 m", "g", 110, COR, c_)], XE, y2)
    E.frase(c, t, d_, ps("que fração do metro?", "i", 88), XE, y2 + 130, "left", 0.13)
    E.frase(c, t, d_ + 1.0, [("na forma mais simples", "g", 72, COR)], XE, y2 + 240)
    E.relogio(c, t, C["s16.a"], 1520, 400, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s17.{k}"] for k in "abcde")
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    Dv = E.dividir("5", 8)
    x, y, s = 260, 250, 112

    def conta():
        E.foco(c, t, a_, 0.5, lambda q: E.fracao(c, 5, 8, 1560, 215, 118, COR, q))
        ze = lerp(a_, b_, 0.55)
        E.conta_div(c, t, Dv, [ze, lerp(b_, c_, 0.5), lerp(c_, d_, 0.5), lerp(d_, e_, 0.5)], [b_, c_, d_, lerp(d_, e_, 0.75)], a_, x, y, s, tv=ze)
        sobra(c, t, lerp(b_, c_, 0.72), c_, "2", x, y, s, 2, 1)
        sobra(c, t, lerp(c_, d_, 0.72), d_, "4", x, y, s, 3, 2)
        troca(c, t, [(a_, "5 ÷ 8"), (ze, "0 e vírgula"), (b_, "50 ÷ 8 = 6"), (lerp(b_, c_, 0.68), "sobram 2"), (c_, "20 ÷ 8 = 2"), (lerp(c_, d_, 0.68), "sobram 4"),
                  (d_, "40 ÷ 8 = 5"), (lerp(d_, e_, 0.62), "não sobra nada")], 1020, 600, 88)
        E.foco(c, t, e_, 0.5, lambda q: (E.pilula(c, "0,625 m", 1400, 860, 92, estilo="g", fundo=CERTO, cor=BR, a=q)))
    E.saida(c, t, C["s18"] - 0.1, conta)
    if t < C["s18"]:
        return
    y2, s2, x0, x1 = 540, 180, 520, 1370
    E.frase(c, t, C["s18"] + 0.1, ps("na outra tábua, duas casas", "i", 84), W / 2, 200, "center", 0.14)
    fr(c, t, a8, 28, 100, x0, y2, s2, COR)
    E.frase(c, t, a8 + 0.3, [("centésimos", "g", 76, COR)], x0, 860, "center")
    E.pontes(c, t, x0 + 180, x1 - 210, y2, s2, "÷ 4", b8, b8 + 0.15, size=60)
    E.foco(c, t, c8, 0.5, lambda a: (E.bola(c, x1, y2 + 3, 180, CERTO, a), E.fracao(c, 7, 25, x1, y2, 134, BR, a)))
    E.frase(c, t, c8 + 0.5, [("do metro", "g", 84, CERTO)], x1, 860, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        a_, b_ = C["s19.a"], C["s19.b"]
        E.frase(c, t, a_, [("fração", "g", 100, COR), ("→", "g", 90, TINTA2), ("decimal", "g", 100, COR)], W / 2, 400, "center", 0.15)
        E.frase(c, t, lerp(a_, b_, 0.45), ps("divida o de cima pelo de baixo", "i", 84), W / 2, 510, "center", 0.12)
        E.frase(c, t, b_, [("decimal", "g", 100, COR), ("→", "g", 90, TINTA2), ("fração", "g", 100, COR)], W / 2, 730, "center", 0.15)
        E.frase(c, t, b_ + 1.2, ps("conte as casas e simplifique", "i", 84), W / 2, 840, "center", 0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a_, b_, c_, d_, e_ = (C[f"s20.{k}"] for k in "abcde")
    E.frase(c, t, C["s20"] + 0.1, ps("3/8 acabou em 3 casas", "i", 72), XE, 170, "left", 0.13)
    E.frase(c, t, a_, ps("algumas divisões", "i", 90) + [("nunca acabam", "g", 90, COR)], XE, 300, "left", 0.15)
    E.frase(c, t, lerp(C["s20"], b_, 0.75), ps("próxima aula", "i", 76), XE, 450)
    E.frase(c, t, b_, [("Dízimas:", "g", 130, COR), ("reconhecer", "i", 110)], XE, 600, "left", 0.25)
    E.frase(c, t, c_, ps("e", "i", 110) + [("prever", "i", 110), ("sem dividir", "g", 104, COR)], XE, 740, "left", 0.2)
    E.foco(c, t, d_, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 460, 76, estilo="g", cor=E.SOBRE, a=a))
    p = ease_io(prog(t, d_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1580, p), lerp(760, 485, p), ep(t, d_ + 0.2, 0.4))
    E.frase(c, t, e_, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, traco=b_traco, conta=b_conta, volta=b_volta, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
