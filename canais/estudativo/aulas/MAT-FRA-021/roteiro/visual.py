"""Visual — Estudativo · MAT-FRA-021: praticando números decimais (última aula da trilha).
Aula de prática: cinco situações, cada uma com selo de progresso, relógio de pausa e a conta na tela.
Todo instante vem de C[...]; o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
from decimal import Decimal as D
from fractions import Fraction as F

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, palco, centro, linha
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-021_praticando_numeros_decimais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao3", "atalho", "questao5", "fim"))
BR = "#FFFFFF"

assert D("3.75") + D("12.90") == D("16.65") and 20 - D("16.65") == D("3.35")
assert 14 / D("2.5") == D("5.6") and 140 // 25 == 5 and 140 % 25 == 15 and 150 // 25 == 6
assert D("8.7") / D("1.5") == D("5.8") and 87 // 15 == 5 and 87 % 15 == 12 and 120 // 15 == 8
assert F(3, 4) == F("0.75") and D("16.4") * D("0.75") == D("12.3") and 164 * 75 == 12300
assert D("16.40") / 4 == D("4.10") and D("4.10") * 3 == D("12.30") and D("17.30") / 4 == D("4.325")
assert F("16.67") * 3 == F("50.01") and F("0.85") == F(17, 20) and D("0.85") * 100 == 85


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


def zero_some(c, t, x, y, size, t1, cor=None):
    """o 0 à esquerda de 0,85: some quando a vírgula sai dele. x = borda esquerda do primeiro algarismo depois da vírgula"""
    E.saida(c, t, t1, lambda: centro(c, "0", x - E.casa(size) * 0.5, y, size, "g", cor or TINTA))


def selo(c, t, t0, n):
    """situação n de 5, com cinco pontos de progresso"""
    s = f"situação {n} de 5"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", cor=E.SOBRE, a=a)
        for i in range(5):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def pacote(c, x, y, w, h, nome, peso, cor, a=1.0):
    """pacote de arroz: caixa com a letra e o peso"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 22, cor, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 12, y + 12, w - 24, h - 24), 14, 14), M.paint(M.on(cor), 0.5 * a, stroke=3))
    centro(c, nome, x + w / 2, y + h * 0.5, 74, "g", M.on(cor), a)
    centro(c, peso, x + w / 2, y + h * 0.8, 54, "b", M.on(cor), a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]
    E.frase(c, t, a_ + 0.1, [("5", "g", 240, COR), ("situações", "g", 180, COR)], XE, 350, "left", 0.25)
    E.frase(c, t, a_ + 0.8, ps("de dinheiro e de medida", "i", 110), XE, 490, "left", 0.15)
    E.frase(c, t, lerp(a_, b_, 0.6), ps("criadas para esta aula", "i", 72), XE, 590, "left", 0.15)
    for i, (s, cx) in enumerate((("pause", 440), ("resolva", 960))):
        ti = b_ + i * 0.5
        E.foco(c, t, ti, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 730, 56, 64, p), E.escreve(c, s, cx - 110, 755, 92, "g", TINTA, p)))
    E.frase(c, t, lerp(b_, C["s01.end"], 0.68), ps("os decimais ficam", "i", 88) + [("de vez na cabeça", "g", 80, COR)], W / 2, 930, "center", 0.17)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.2, ps("você vai usar", "i", 110), XE, 340, "left", 0.18)
    E.frase(c, t, C["s02"] + 0.9, [("quatro", "g", 130, COR)], XE, 490)
    E.frase(c, t, C["s02"] + 1.1, [("ferramentas", "i", 110)], XE, 610)
    x, w = 880, 860
    for i, (k, s) in enumerate((("s02.a", "alinhar a vírgula"), ("s02.b", "multiplicar e dividir"), ("s02.c", "fração em decimal"), ("s02.d", "reconhecer dízima"))):
        y = 180 + i * 165
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 134, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(s, "g", 62, COR)], x + 44, y + 90)
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.5), ps("travou?", "i", 62, COR), XE, 730, "left", 0.13)
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.6), ps("procure a aula no canal", "i", 60), XE, 810, "left", 0.13)


# ---------------- situação 1: somar e subtrair ----------------
def b_questao1(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s03.{k}"] for k in "abcde")
    selo(c, t, a_, 1)
    E.frase(c, t, a_ + 0.3, ps("no mercado", "i", 84), XE, 250)
    linha(c, t, [("pão", "i", 100, TINTA, b_), ("R$ 3,75", "g", 110, COR, b_ + 0.4)], XE, 400)
    linha(c, t, [("carne", "i", 100, TINTA, c_), ("R$ 12,90", "g", 110, COR, c_ + 0.4)], XE, 550)
    linha(c, t, [("nota de", "i", 100, TINTA, d_), ("R$ 20", "g", 110, TINTA, d_ + 0.4)], XE, 700)
    E.frase(c, t, e_, ps("qual é o", "i", 120) + [("troco?", "g", 116, COR)], XE, 900, "left", 0.18)
    E.relogio(c, t, C["s04.a"], 1520, 400, 190)


def b_resposta1(c, t, C, b):
    selo(c, t, C["s05"] - 0.5, 1)
    a_, b_, c_, d_ = (C[f"s05.{k}"] for k in "abcd")
    E.frase(c, t, lerp(C["s05"], a_, 0.5), ps("primeiro, o total", "i", 72, COR), 240, 250, "left", 0.13)
    E.frase(c, t, a_, ps("vírgula embaixo de vírgula", "i", 58), 240, 900, "left", 0.11)
    s = 104
    E.armada(c, t, ["3,75", "12,90"], "+", "16,65", (a_, a_ + 0.5), [b_ + i * 0.15 for i in range(4)], 480, 400, s)
    ti = lerp(b_, c_, 0.55)
    E.frase(c, t, ti, ps("depois, o troco", "i", 72, COR), 1000, 250, "left", 0.13)
    E.armada(c, t, ["20", "16,65"], "−", "3,35", (c_, c_ + 0.5), [d_ + i * 0.15 for i in range(3)], 1270, 400, s, tz=lerp(c_, d_, 0.25), cz=CERTO)
    E.frase(c, t, lerp(c_, d_, 0.3), ps("20,00: as casas batem", "i", 58), 1000, 900, "left", 0.11)
    E.foco(c, t, d_ + 0.5, 0.5, lambda q: E.pilula(c, "troco: R$ 3,35", 1370, 1000, 60, estilo="g", fundo=CERTO, cor=BR, a=q))


# ---------------- situação 2: dividir por decimal e comparar ----------------
def b_questao2(c, t, C, b):
    a_, b_, c_, d_, e_, f_ = (C[f"s06.{k}"] for k in "abcdef")
    selo(c, t, a_, 2)
    E.frase(c, t, lerp(a_, b_, 0.3), ps("o mesmo arroz, em pacotes diferentes", "i", 84), XE, 270, "left", 0.13)
    y = 350
    E.foco(c, t, lerp(a_, b_, 0.72), 0.45, lambda q: pacote(c, XE, y, 230, 290, "A", "", COR, q))
    txt(c, t, b_, "2,5 kg", XE + 270, y + 130, 96, TINTA, "g")
    txt(c, t, c_, "R$ 14", XE + 270, y + 250, 96, COR, "g")
    E.foco(c, t, lerp(c_, d_, 0.55), 0.45, lambda q: pacote(c, 880, y, 230, 290, "B", "", TINTA, q))
    txt(c, t, d_, "1,5 kg", 1150, y + 130, 96, TINTA, "g")
    txt(c, t, e_, "R$ 8,70", 1150, y + 250, 96, COR, "g")
    E.frase(c, t, f_, ps("em qual o quilo sai", "i", 100) + [("mais barato?", "g", 96, COR)], W / 2, 860, "center", 0.15)
    E.relogio(c, t, C["s07.a"], 1660, 280, 110)


def b_resposta2(c, t, C, b):
    selo(c, t, C["s08"] - 0.5, 2)
    a_, b_, c_, d_ = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    f = lambda q: lerp(c_, d_, q)

    def pa():
        E.frase(c, t, a_, ps("preço do quilo =", "i", 76) + [("preço ÷ quilos", "g", 76, COR)], XE, 240, "left", 0.13)
        txt(c, t, b_ - 0.5, "pacote A:", XE, 390, 76, TINTA, "b")
        txt(c, t, b_, "14 ÷ 2,5", XE, 510, 104, TINTA, "g")
        txt(c, t, lerp(b_, c_, 0.45), "anda 1 casa em cada número", XE, 600, 56, TINTA, "i")
        txt(c, t, c_, "140 ÷ 25", XE, 730, 104, COR, "g")
        x, y, s = 900, 420, 112
        Dv = E.dividir("140", 25)
        E.conta_div(c, t, Dv, [f(0.38), f(0.88)], [f(0.72), f(0.93)], c_, x, y, s, tv=f(0.72))
        sobra(c, t, f(0.47), f(0.72), "15", x, y, s, 1, 2)
        E.foco(c, t, d_, 0.5, lambda q: E.pilula(c, "R$ 5,60 o quilo", 1340, 830, 72, estilo="g", cor=E.SOBRE, a=q))
    E.saida(c, t, C["s09"] - 0.1, pa)
    if C["s09"] - 0.1 <= t < d9 - 0.1 + 0.5:
        g = lambda q: lerp(b9, c9, q)

        def pb():
            txt(c, t, C["s09"], "pacote B:", XE, 240, 76, TINTA, "b")
            txt(c, t, a9, "8,7 ÷ 1,5", XE, 390, 104, TINTA, "g")
            txt(c, t, b9, "87 ÷ 15", XE, 560, 104, COR, "g")
            x, y, s = 900, 300, 112
            Dv = E.dividir("87", 15)
            E.conta_div(c, t, Dv, [g(0.3), g(0.84)], [g(0.68), g(0.92)], a9, x, y, s, tv=g(0.68))
            sobra(c, t, g(0.4), g(0.68), "12", x, y, s, 1, 1)
            E.foco(c, t, c9, 0.5, lambda q: E.pilula(c, "R$ 5,80 o quilo", 1340, 780, 72, estilo="g", cor=E.SOBRE, a=q))
        E.saida(c, t, d9 - 0.1, pb)
    if t >= d9:
        for x, nome, kg, pr, cor, ok in ((330, "A", "R$ 5,60", "o quilo", CERTO, True), (1080, "B", "R$ 5,80", "o quilo", TINTA, False)):
            E.foco(c, t, d9, 0.45, lambda q, x=x, nome=nome, cor=cor: pacote(c, x, 230, 230, 290, nome, "", cor, q))
            txt(c, t, d9 + 0.2, kg, x + 270, 390, 92, cor, "g")
            txt(c, t, d9 + 0.2, pr, x + 270, 480, 72, TINTA, "i")
        E.foco(c, t, d9 + 0.3, 0.45, lambda q: E.selo(c, 330, 230, 56, True, q))
        E.frase(c, t, d9 + 0.3, ps("resposta:", "i", 92) + [("pacote A", "g", 96, CERTO)], W / 2, 680, "center", 0.15)
        E.frase(c, t, lerp(d9, e9, 0.55), ps("o pacote B custa menos no caixa,", "i", 76), W / 2, 810, "center", 0.11)
        E.frase(c, t, e9, ps("mas", "i", 84) + [("o quilo dele é mais caro", "g", 80, ERRADO)], W / 2, 930, "center", 0.15)


# ---------------- situação 3: fração em decimal e multiplicar ----------------
def b_questao3(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s10.{k}"] for k in "abcd")
    selo(c, t, a_, 3)
    E.frase(c, t, a_ + 0.5, ps("uma costureira comprou", "i", 88), XE, 270, "left", 0.14)
    E.foco(c, t, b_, 0.5, lambda q: E.fracao(c, 3, 4, 270, 440, 130, COR, q))
    txt(c, t, b_ + 0.6, "de metro de tecido", 380, 490, 92, TINTA, "i")
    linha(c, t, [("o metro custa", "i", 92, TINTA, c_ - 0.5), ("R$ 16,40", "g", 110, COR, c_)], XE, 700)
    E.frase(c, t, d_, ps("quanto ela", "i", 120) + [("pagou?", "g", 116, COR)], XE, 890, "left", 0.2)
    E.relogio(c, t, C["s11.a"], 1540, 500, 170)


def b_resposta3(c, t, C, b):
    selo(c, t, C["s12"] - 0.5, 3)
    a_, b_, c_, d_, e_ = (C[f"s12.{k}"] for k in "abcde")
    E.foco(c, t, a_, 0.5, lambda q: E.fracao(c, 3, 4, 270, 270, 104, COR, q))
    txt(c, t, a_ + 0.4, "= 3 ÷ 4 = 0,75", 370, 310, 92, TINTA, "g")
    txt(c, t, b_, "16,4 × 0,75", XE, 490, 110, TINTA, "g")
    txt(c, t, c_, "164 × 75 =", XE, 650, 96, TINTA2, "g")
    x0, y, s = 690, 650, 112
    E.foco(c, t, c_ + 0.6, 0.45, lambda q: E.anda(c, t, "12300", 5, [(d_ + 0.1, 2)], x0, y, s, tv=d_))
    E.frase(c, t, d_, [("1 casa", "g", 72, COR)] + ps("+", "g", 72) + [("2 casas", "g", 72, COR)] + ps("=", "g", 72) + [("3 casas", "g", 72, COR)], XE, 800, "left", 0.15)
    E.foco(c, t, e_, 0.5, lambda q: E.pilula(c, "R$ 12,30", 1400, 900, 88, estilo="g", fundo=CERTO, cor=BR, a=q))
    E.frase(c, t, e_, ps("ela pagou", "i", 88), XE, 925, "left", 0.15)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a_, b_, c_ = (C[f"s13.{k}"] for k in "abc")

    def conta():
        E.frase(c, t, C["s13"] + 0.1, ps("aqui cabe um atalho", "i", 84, CLARO), W / 2, 180, "center", 0.14)
        E.frase(c, t, lerp(C["s13"], a_, 0.6), ps("três quartos de um preço", "i", 76, BR), W / 2, 290, "center", 0.12)
        E.frase(c, t, a_, [("÷ 4", "g", 150, CLARO), ("depois", "i", 110, BR), ("× 3", "g", 150, CLARO)], W / 2, 480, "center", 0.3)
        txt(c, t, b_, "R$ 16,40 ÷ 4 = R$ 4,10", 250, 680, 106, BR, "g")
        txt(c, t, c_, "R$ 4,10 × 3 =", 250, 850, 106, BR, "g")
        txt(c, t, c_ + 0.6, "R$ 12,30", 1110, 850, 106, CLARO, "g")
    E.saida(c, t, C["s14"] - 0.1, conta)
    if t < C["s14"]:
        return
    a4, b4, c4 = (C[f"s14.{k}"] for k in "abc")
    x, y, w, h = 400, 200, 1120, 190
    E.foco(c, t, a4, 0.45, lambda q: E.chocolate(c, x, y, w, h, 4, [(i, CLARO, prog(t, lerp(a4, b4, 0.35) + i * 0.3, 0.35)) for i in range(3)], q, escuro=True))
    E.frase(c, t, lerp(a4, b4, 0.1), ps("o quarto é uma parte de quatro iguais,", "i", 76, BR), W / 2, 500, "center", 0.11)
    E.frase(c, t, lerp(a4, b4, 0.4), ps("e você quer", "i", 76, BR) + [("três delas", "g", 76, CLARO)], W / 2, 600, "center", 0.13)
    E.frase(c, t, lerp(a4, b4, 0.8), ps("não compensa se não fecha nos centavos:", "i", 72, CLARO), W / 2, 740, "center", 0.11)
    txt(c, t, b4, "R$ 17,30 ÷ 4", 300, 870, 96, BR, "g")
    E.frase(c, t, c4, ps("aí,", "i", 84, CLARO) + [("multiplique pelo decimal", "g", 66, BR)], 1000, 868, "left", 0.13)


# ---------------- situação 4: dízima e arredondar ----------------
def b_questao4(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s15.{k}"] for k in "abcd")
    selo(c, t, a_, 4)
    linha(c, t, [("3 amigos", "g", 110, TINTA, lerp(a_, b_, 0.45)), ("dividem", "i", 100, TINTA, lerp(a_, b_, 0.65))], XE, 310)
    linha(c, t, [("uma conta de", "i", 100, TINTA, b_), ("R$ 50", "g", 110, COR, b_ + 0.7)], XE, 450)
    E.frase(c, t, c_, ps("a parte de cada um é", "i", 84), XE, 620, "left", 0.13)
    E.frase(c, t, c_ + 1.0, [("decimal exato", "g", 88, COR), ("ou", "i", 88), ("dízima?", "g", 88, COR)], XE, 730, "left", 0.2)
    E.frase(c, t, d_, ps("e quanto cada um paga,", "i", 84), XE, 870, "left", 0.13)
    E.frase(c, t, d_ + 1.0, [("no centavo?", "g", 88, COR)], XE, 975)
    E.relogio(c, t, C["s16.a"], 1560, 400, 170)


def b_resposta4(c, t, C, b):
    selo(c, t, C["s17"] - 0.5, 4)
    a_, b_, c_, d_ = (C[f"s17.{k}"] for k in "abcd")
    a8, b8, c8, d8, e8 = (C[f"s18.{k}"] for k in "abcde")
    val = "16,666"
    xv, y, s = 620, 590, 170
    cs = E._centros(val, xv, s)

    def parte():
        E.foco(c, t, a_, 0.5, lambda q: E.fracao(c, 50, 3, 300, 280, 110, COR, q))
        txt(c, t, lerp(a_, b_, 0.4), "não simplifica", 450, 260, 66, TINTA, "i")
        E.frase(c, t, b_, [("denominador 3:", "i", 80), ("dízima", "g", 88, ERRADO)], 450, 345, "left", 0.15)
    E.saida(c, t, C["s18"] - 0.1, parte)
    cores = {3: ERRADO, 4: ERRADO, 5: ERRADO} if t >= d_ and t < C["s18"] else None
    if t >= a8:
        cores = {5: COR}
    E.foco(c, t, c_, 0.5, lambda q: E.numero(c, val, xv, y, s, a=q, cores=cores))
    cen(c, t, c_ + 1.0, "...", cs[5] + 150, y, 130, TINTA)
    if t < C["s18"]:
        E.chave(c, cs[3] - 60, cs[3] + 60, y + 44, ERRADO, ep(t, d_, 0.4), 28, 7)
        E.foco(c, t, d_, 0.45, lambda q: E.pilula(c, "período: 6", cs[3], y + 150, 62, estilo="g", fundo=ERRADO, cor=BR, a=q))
    if t >= C["s18"]:
        E.frase(c, t, C["s18"] + 0.1, ps("para arredondar no centavo,", "i", 76), XE, 215, "left", 0.13)
        E.frase(c, t, a8, ps("olhe", "i", 92) + [("a terceira casa", "g", 88, COR)], XE, 315, "left", 0.15)
        E.chave(c, cs[5] - 60, cs[5] + 60, y + 44, COR, ep(t, a8, 0.4), 28, 7)
        E.foco(c, t, lerp(a8, b8, 0.5), 0.45, lambda q: E.pilula(c, "5 ou mais: sobe", cs[5] + 30, y + 150, 58, estilo="g", cor=E.SOBRE, a=q))
        E.salto(c, t, b8, cs[5], cs[4], y - 125, 40, COR, "+1", size=72)
        y2 = 845
        E.foco(c, t, c8, 0.5, lambda q: E.pilula(c, "R$ 16,67 cada um", 560, y2, 72, estilo="g", fundo=CERTO, cor=BR, a=q))
        txt(c, t, d8, "3 × R$ 16,67 = R$ 50,01", 940, y2 + 26, 76, TINTA, "g")
        E.frase(c, t, e8, ps("esse centavo a mais é", "i", 80) + [("a dízima no bolso", "g", 80, COR)], W / 2, 990, "center", 0.13)


# ---------------- situação 5: decimal em fração e andar com a vírgula ----------------
def b_questao5(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s19.{k}"] for k in "abcd")
    selo(c, t, a_, 5)
    linha(c, t, [("caminha", "i", 100, TINTA, b_ - 0.6), ("0,85 km", "g", 116, COR, b_), ("por dia", "i", 100, TINTA, b_ + 1.0)], XE, 330)
    E.frase(c, t, c_, ps("que fração do km?", "i", 92), XE, 520, "left", 0.15)
    E.frase(c, t, c_ + 1.0, [("na forma mais simples", "g", 72, COR)], XE, 620)
    E.frase(c, t, d_, ps("e em", "i", 92) + [("100 dias?", "g", 96, COR)], XE, 800, "left", 0.2)
    E.relogio(c, t, C["s20.a"], 1540, 500, 170)


def b_resposta5(c, t, C, b):
    selo(c, t, C["s21"] - 0.5, 5)
    a_, b_, c_ = (C[f"s21.{k}"] for k in "abc")

    def frac():
        y, s, x0, x1 = 540, 170, 480, 1300
        E.foco(c, t, a_ - 0.3, 0.45, lambda q: E.escreve(c, "duas casas:", XE, 260, 80, "i", TINTA, q))
        fr(c, t, a_, 85, 100, x0, y, s, COR)
        E.frase(c, t, lerp(a_, b_, 0.3), ps("85 termina em 5, 100 termina em 0", "i", 72), W / 2, 930, "center", 0.1)
        E.pontes(c, t, x0 + 180, x1 - 200, y, s, "÷ 5", b_, b_ + 0.15, size=60)
        E.foco(c, t, c_, 0.5, lambda q: (E.bola(c, x1, y + 3, 175, CERTO, q), E.fracao(c, 17, 20, x1, y, 130, BR, q)))
        E.frase(c, t, c_ + 0.5, ps("do quilômetro", "i", 76, CERTO), x1, 800, "center", 0.13)
    E.saida(c, t, C["s22"] - 0.1, frac)
    if t < C["s22"]:
        return
    a2, b2, c2 = (C[f"s22.{k}"] for k in "abc")
    E.frase(c, t, C["s22"] + 0.1, ps("em cem dias,", "i", 88), XE, 280, "left", 0.15)
    E.foco(c, t, a2, 0.45, lambda q: E.pilula(c, "× 100", 1000, 255, 84, estilo="g", cor=E.SOBRE, a=q))
    x, y, s = 640, 560, 200
    h1, h2 = b2 + 0.1, b2 + 1.0
    E.foco(c, t, C["s22"] + 0.2, 0.45, lambda q: E.anda(c, t, "85", 0, [(h1, 1), (h2, 2)], x, y, s, some=True))
    E.foco(c, t, C["s22"] + 0.2, 0.45, lambda q: zero_some(c, t, x, y, s, h1 + 0.2))
    E.frase(c, t, b2, ps("a vírgula anda", "i", 88) + [("2 casas", "g", 92, COR)] + ps("para a direita", "i", 88), W / 2, 760, "center", 0.15)
    E.foco(c, t, c2, 0.5, lambda q: E.pilula(c, "85 km", W / 2, 910, 96, estilo="g", fundo=CERTO, cor=BR, a=q))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        for i, (k, l1, l2) in enumerate((("s23.a", "vírgula alinhada", "para somar"), ("s23.b", "casas contadas", "para multiplicar"),
                                         ("s23.c", "divisor sem vírgula", "para dividir"), ("s23.d", "resposta conferida", "no final"))):
            y = 340 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 300, y - 28, 54, 62, a))
            linha(c, t, [(l1, "g", 74, TINTA, C[k] + 0.1), (l2, "i", 74, COR, C[k] + 0.3)], 400, y)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    a_, b_, c_, d_, e_ = (C[f"s24.{k}"] for k in "abcde")
    E.frase(c, t, a_, ps("a trilha de", "i", 80) + [("frações e decimais", "g", 84, COR)] + ps("terminou", "i", 80), XE, 230, "left", 0.15)
    E.frase(c, t, b_ - 0.5, ps("você saiu de", "i", 76), XE, 390, "left", 0.13)
    E.frase(c, t, b_, [("o que é uma fração", "g", 104, TINTA)], XE, 500)
    E.frase(c, t, c_ - 0.5, ps("e chegou até", "i", 76), XE, 620, "left", 0.13)
    E.frase(c, t, c_, [("prever uma dízima sem dividir", "g", 88, COR)], XE, 730)
    E.foco(c, t, d_, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 500, 76, estilo="g", cor=E.SOBRE, a=a))
    p = ease_io(prog(t, d_ + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1590, p), lerp(800, 525, p), ep(t, d_ + 0.2, 0.4))
    E.frase(c, t, e_, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
