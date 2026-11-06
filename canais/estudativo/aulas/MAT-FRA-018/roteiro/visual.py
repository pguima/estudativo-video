"""Visual — Estudativo · MAT-FRA-018: dividir por um número decimal.
A moeda de 25 centavos explica por que o resultado cresce e por que andar a vírgula nos dois números não muda a divisão.
Todo instante vem de C[...]; o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
from decimal import Decimal as D

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, sinal, passo, palco, centro, linha
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-018_dividir_por_um_numero_decimal.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("moedas", "regra", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert D("1.5") / D("0.25") == 6 and 6 * D("0.25") == D("1.5") and 4 * D("0.25") == 1 and 2 * D("0.25") == D("0.5")
assert D("3.75") / D("1.5") == D("2.5") and D("37.5") / 15 == D("2.5") and D("37") // 15 == 2 and 37 % 15 == 7 and 75 // 15 == 5
assert D("1.5") / 25 == D("0.06") and D("1.5") * 4 == 6
assert D("5.4") / D("0.45") == 12 and 540 // 45 == 12 and 54 // 45 == 1 and 54 % 45 == 9 and 90 // 45 == 2
assert 1 / D("0.5") == 2 and 1 / D("0.25") == 4 and 25 * 6 == 150


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


def fica(c, t, t0, t1, partes, x, y, align="left", passo_=0.2):
    """frase que entra em t0 e sai em t1"""
    E.saida(c, t, t1, lambda: E.frase(c, t, t0, partes, x, y, align, passo_))


def txt(c, t, ti, s, x, y, size=64, cor=None, est="b"):
    E.foco(c, t, ti, 0.45, lambda a: E.escreve(c, s, x, y, size, est, cor or TINTA, a))


def cen(c, t, ti, s, x, y, size=64, cor=None, est="g"):
    E.foco(c, t, ti, 0.45, lambda a: centro(c, s, x, y, size, est, cor or TINTA, a))


def troca(c, t, itens, x, y, size=66, est="b", cor=None):
    """uma linha de cada vez: itens = [(instante, texto)], cada uma sai quando a próxima chega"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        E.saida(c, t, fim, lambda s=s, ti=ti: txt(c, t, ti, s, x, y, size, cor, est), d=0.25)


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE if cor is None else M.on(cor), a)


def sobra(c, t, t0, t1, s, x, y, size, lin, col):
    """o resto sozinho na conta, até o algarismo descer: col = coluna do último algarismo (na casa do resto)"""
    cl = E.casa(size)
    E.saida(c, t, t1, lambda: E.foco(c, t, t0, 0.35, lambda a: [centro(c, ch, x + (col - (len(s) - 1 - i) + 0.5) * cl, y + lin * size * 1.12, size, "g", TINTA, a) for i, ch in enumerate(s)]), d=0.01)


def zero_some(c, t, x, y, size, t1, cor=None):
    """o 0 à esquerda de 0,25: some quando a vírgula sai dele. x = borda esquerda do primeiro algarismo depois da vírgula"""
    E.saida(c, t, t1, lambda: centro(c, "0", x - E.casa(size) * 0.5, y, size, "g", cor or TINTA))


def lembrete(c, t, C, cena, n, nome, itens):
    """itens = [(cue, linha fina, linha forte)]"""
    E.frase(c, t, C[cena] + 0.1, ps("você precisa de", "i", 84), XE, 410, "left", 0.18)
    E.foco(c, t, C[f"{cena}.a"], 0.5, lambda a: E.escreve(c, n, XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[f"{cena}.a"] + 0.15, 0.5, lambda a: E.escreve(c, nome, XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    alvo = [190 + i * 240 + 170 for i in range(len(itens))]
    ks = [k for k, _, _ in itens]
    py = alvo[0]
    for i in range(1, len(ks)):
        py = lerp(py, alvo[i], ease_io(prog(t, C[ks[i]] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C[ks[0]], 0.4))
    u = ks[-1]
    E.frase(c, t, lerp(C[u], C[f"{cena}.end"], 0.72), ps("faltou?", "i", 60, COR) + ps("procure no canal", "i", 60), XE, 860, "left", 0.15)


def promessa(c, t, ta, tb):
    E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 290 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
    f = lambda q: lerp(ta, tb, q)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 300, "left", 0.13)
    E.frase(c, t, f(0.42), [("dividir", "g", 132)], XE, 450)
    E.frase(c, t, f(0.5), [("por", "i", 120), ("qualquer", "i", 120)], XE, 580)
    E.frase(c, t, f(0.6), [("número", "i", 120), ("com", "i", 120)], XE, 700)
    E.frase(c, t, f(0.74), [("vírgula", "g", 132, COR)], XE, 830)
    E.frase(c, t, f(0.84), ps("sem medo dela", "i", 80), XE, 940, "left", 0.13)
    E.foco(c, t, tb + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1450, 505, 88, "g", E.SOBRE, a), centro(c, "de prova", 1450, 600, 92, "i", E.SOBRE, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]
    f = lambda q: lerp(b_, c_, q)

    def conta():
        y, s = 340, 180
        linha(c, t, [("1,5", "g", s, TINTA, a_), ("÷", "g", s * 0.8, TINTA2, b_), ("0,25", "g", s, COR, b_ + 0.7)], XE, y)
        cen(c, t, f(0.24), "=", 1180, y, 150, TINTA2)
        if t < c_:
            cen(c, t, f(0.24), "?", 1400, y, s, CINZA)
        E.foco(c, t, c_, 0.5, lambda a: num_bola(c, "6", 1420, y - 60, 180, 220, a))
        E.frase(c, t, f(0.24), ps("é maior ou menor que", "i", 96) + [("1,5?", "g", 92)], XE, 580, "left", 0.16)
        xs = linha(c, t, [("quase todo mundo diz", "i", 96, TINTA, f(0.58)), ("menor", "g", 104, ERRADO, f(0.7))], XE, 730)
        E.frase(c, t, f(0.74), ps("dividir parece sempre diminuir", "i", 78), XE, 860, "left", 0.12)
        if t >= c_:
            w = E.larg("menor", "g", 104)
            E.risco(c, xs[1] - 14, 700, xs[1] + w + 14, 700, t, c_ + 0.2, largura=14)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        promessa(c, t, C["s02.a"], C["s02.b"])


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", "3", "coisas", (("s03.b", "andar com a vírgula", "× 10 ou × 100"), ("s03.c", "dividir por", "dois algarismos"),
                                             ("s03.d", "continuar a conta", "depois da vírgula")))


# ---------------- moedas: por que cresce ----------------
def b_moedas(c, t, C, b):
    a_, b_, c_ = C["s04.a"], C["s04.b"], C["s04.c"]

    def pergunta():
        E.frase(c, t, C["s04"] + 0.1, ps("por que o resultado", "i", 92) + [("cresceu?", "g", 92, COR)], W / 2, 190, "center", 0.15)
        E.frase(c, t, a_, ps("quantas vezes um número", "i", 80) + [("cabe no outro?", "g", 76, COR)], W / 2, 320, "center", 0.15)
        E.frase(c, t, b_ - 0.1, ps("você tem", "i", 80), 520, 520, "center")
        cen(c, t, b_, "R$ 1,50", 520, 700, 170, TINTA)
        if t >= c_:
            p = ep(t, c_, 0.5)
            M.arrow(c, 900, 640, 1090, 640, TINTA, p, 5, 18, p)
        E.frase(c, t, c_ + 0.1, ps("moedas de", "i", 80), 1370, 450, "center")
        E.foco(c, t, c_ + 0.2, 0.5, lambda a: E.moeda(c, 1370, 680, 190 * ease_back(prog(t, c_ + 0.2, 0.5)), "25¢", a))
    E.saida(c, t, C["s05"] - 0.1, pergunta)
    if t < C["s05"]:
        return

    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    E.foco(c, t, C["s05"], 0.4, lambda a: (centro(c, "R$ 1,50", 680, 200, 90, "g", TINTA, a), centro(c, "em moedas de 25¢", 1200, 200, 76, "i", TINTA, a)))
    x0, dx, y, r = 325, 254, 410, 106
    ts = [a5 + i * 0.22 for i in range(4)] + [b5, b5 + 0.25]
    for i, ti in enumerate(ts):
        k = ease_back(prog(t, ti, 0.45))
        if k > 0:
            E.moeda(c, x0 + i * dx, y, r * k, "25¢", min(1.0, k * 1.5))
    q1 = ep(t, lerp(a5, b5, 0.55), 0.4)
    q2 = ep(t, lerp(b5, c5, 0.55), 0.4)
    E.chave(c, x0 - r, x0 + 3 * dx + r, y + r + 26, COR, q1, 26, 6)
    E.chave(c, x0 + 4 * dx - r, x0 + 5 * dx + r, y + r + 26, COR, q2, 26, 6)
    cen(c, t, lerp(a5, b5, 0.55), "R$ 1,00", x0 + 1.5 * dx, y + r + 112, 72, COR)
    cen(c, t, lerp(b5, c5, 0.55), "R$ 0,50", x0 + 4.5 * dx, y + r + 112, 72, COR)
    E.foco(c, t, c5, 0.5, lambda a: num_bola(c, "6", 330, 800, 100, 130, a))
    E.frase(c, t, c5 + 0.15, [("moedas", "g", 110)], 460, 840)
    E.frase(c, t, d5, ps("a moeda é pequena", "i", 76), 1010, 790, "left", 0.14)
    E.frase(c, t, d5 + 0.6, [("cabe", "i", 76), ("muitas vezes", "g", 72, COR)], 1010, 880, "left", 0.14)
    E.frase(c, t, lerp(d5, C["s05.end"], 0.62), ps("por isso o resultado cresceu", "i", 66), W / 2, 985, "center", 0.12)


# ---------------- por que andar a vírgula não muda ----------------
def b_porque(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]

    def centavos():
        s = 136
        for y, nome, n1, n2, ti in ((330, "em reais", "1,5", "0,25", a6), (570, "em centavos", "150", "25", b6)):
            E.frase(c, t, ti - 0.1, [(nome, "i", 86)], XE, y)
            cor = TINTA
            txt(c, t, ti, n1, 730, y, s, cor, "g")
            cen(c, t, ti + 1.0, "÷", 1060, y, 110, TINTA2)
            txt(c, t, ti + 1.6, n2, 1130, y, s, cor, "g")
            cen(c, t, c6, "=", 1490, y, 110, TINTA2)
            cen(c, t, c6 + 0.15, "6", 1610, y, s, COR)
        E.frase(c, t, lerp(b6, c6, 0.66), ps("o mesmo dinheiro,", "i", 84) + ps("a mesma moeda", "i", 84), W / 2, 770, "center", 0.14)
        E.frase(c, t, c6, ps("o resultado é", "i", 92) + [("o mesmo", "g", 96, COR)], W / 2, 920, "center", 0.16)
    E.saida(c, t, C["s07"] - 0.1, centavos)
    if t < C["s07"]:
        return

    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    xa, xb, y, s = 390, 1190, 480, 170
    E.foco(c, t, a7, 0.45, lambda q: E.pilula(c, "× 100", W / 2, 180, 84, estilo="g", cor=E.SOBRE, a=q))
    td, tm = lerp(a7, b7, 0.36), lerp(a7, b7, 0.5)
    cen(c, t, td, "o dinheiro", xa + 200, 300, 76, TINTA, "i")
    cen(c, t, tm, "a moeda", xb + 160, 300, 76, TINTA, "i")
    h1, h2 = b7 + 0.1, b7 + 1.0
    E.foco(c, t, td, 0.45, lambda q: E.anda(c, t, "15", 1, [(h1, 2), (h2, 3)], xa, y, s, some=True))
    E.foco(c, t, tm, 0.45, lambda q: E.anda(c, t, "25", 0, [(h1, 1), (h2, 2)], xb, y, s, some=True))
    E.foco(c, t, tm, 0.45, lambda q: zero_some(c, t, xb, y, s, h1 + 0.2))
    cen(c, t, tm - 0.2, "÷", 985, y, 130, TINTA2)
    E.frase(c, t, b7, ps("a vírgula anda", "i", 86) + [("2 casas", "g", 88, COR)] + ps("para a direita", "i", 86), W / 2, 680, "center", 0.15)
    E.frase(c, t, c7, [("o mesmo tanto", "g", 84, COR)] + ps("no primeiro e no segundo", "i", 84), W / 2, 820, "center", 0.15)
    E.frase(c, t, lerp(c7, C["s07.end"], 0.5), ps("não muda a divisão:", "i", 74) + ps("só troca reais por centavos", "i", 74), W / 2, 940, "center", 0.11)


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    E.frase(c, t, C["s08.a"], ps("regra de", "i", 76) + [("3 passos", "g", 76, COR)], XE, 150, "left", 0.15)
    passo(c, t, C["s08.b"], 1, "olhe o divisor,", "conte as casas", 300)
    passo(c, t, C["s09.a"], 2, "ande a vírgula", "no divisor e no outro", 560)
    passo(c, t, C["s10.a"], 3, "divida", "normalmente", 820)

    s = 124
    # passo 1: o divisor e as casas
    xv1, xv2, y = 1100, 1490, 480
    if t < C["s09.a"]:
        def um():
            E.foco(c, t, C["s08.b"], 0.45, lambda a: (E.numero(c, "1,5", xv1, y, s, a=a), centro(c, "÷", 1290, y, 104, "g", TINTA2, a)))
            E.foco(c, t, C["s08.b"], 0.45, lambda a: E.numero(c, "0,25", xv2, y, s, a=a, cores={2: COR, 3: COR} if t >= C["s08.c"] else None))
            E.foco(c, t, lerp(C["s08.b"], C["s08.c"], 0.25), 0.4, lambda a: E.pilula(c, "divisor", xv2, y - 200, 60, estilo="g", cor=E.SOBRE, a=a))
            cs = E._centros("0,25", xv2, s)
            E.chave(c, cs[2] - 46, cs[3] + 46, y + 34, COR, ep(t, C["s08.c"], 0.4), 26, 6)
            cen(c, t, C["s08.c"] + 0.1, "2 casas", (cs[2] + cs[3]) / 2, y + 150, 76, COR)
        E.saida(c, t, C["s09.a"] - 0.15, um)
        return

    # passo 2: a vírgula anda; passo 3: a conta, na mesma área
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    xa, xb, y2 = 990, 1500, 400

    def dois():
        E.foco(c, t, a9, 0.45, lambda q: E.anda(c, t, "15", 1, [(c9 + 0.1, 2), (d9 - 0.6, 3)], xa, y2, s, some=True))
        E.foco(c, t, a9, 0.45, lambda q: E.anda(c, t, "25", 0, [(b9, 1), (b9 + 0.8, 2)], xb, y2, s, some=True))
        E.foco(c, t, a9, 0.45, lambda q: zero_some(c, t, xb, y2, s, b9 + 0.2))
        cen(c, t, a9, "÷", 1385, y2, 104, TINTA2)
        E.frase(c, t, c9 + 0.6, ps("1 casa só:", "i", 70), 1000, 570, "left")
        E.frase(c, t, lerp(c9, d9, 0.5), [("complete com zero", "g", 60, COR)], 1000, 660)
    E.saida(c, t, C["s10.a"] - 0.15, dois)
    if t < C["s10.a"]:
        return
    a0, b0, c0, d0 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    Dv = E.dividir("150", 25)
    E.conta_div(c, t, Dv, [c0], [c0 + 0.2], a0, 1020, 300, 104)
    txt(c, t, b0, "25 × 6 = 150", 1010, 610, 76)
    E.frase(c, t, d0, ps("para conferir:", "i", 72), 1010, 760)
    txt(c, t, lerp(d0, C["s10.end"], 0.3), "6 × 0,25 = 1,5", 1010, 860, 76, COR)
    E.foco(c, t, lerp(d0, C["s10.end"], 0.75), 0.45, lambda a: E.selo(c, 1660, 830, 64, True, a))


# ---------------- exemplo: o outro número fica com vírgula ----------------
def b_exemplo(c, t, C, b):
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]

    def enunciado():
        E.frase(c, t, C["s11"] + 0.1, ps("só o divisor", "i", 92) + [("perde a vírgula", "g", 88, COR)], W / 2, 210, "center", 0.15)
        E.frase(c, t, lerp(C["s11"], a1, 0.5), ps("o outro número pode ficar com ela", "i", 76), W / 2, 330, "center", 0.11)
        linha(c, t, [("1,5 kg", "g", 124, TINTA, a1), ("de banana", "i", 104, TINTA, a1 + 0.6)], XE + 90, 560)
        linha(c, t, [("custou", "i", 104, TINTA, b1 - 0.3), ("R$ 3,75", "g", 124, COR, b1)], XE + 90, 720)
        E.frase(c, t, c1, ps("quanto custa", "i", 104) + [("o quilo?", "g", 100, COR)], W / 2, 920, "center", 0.16)
    E.saida(c, t, C["s12"] - 0.1, enunciado)
    if t < C["s12"]:
        return

    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    a3, b3, c3, d3, e3 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
    s, y, xa, xb = 130, 330, XE + 10, 700
    E.foco(c, t, a2, 0.45, lambda q: E.anda(c, t, "375", 1, [(c2, 2)], xa, y, s))
    cen(c, t, lerp(a2, b2, 0.36), "÷", 615, y, 104, TINTA2)
    E.foco(c, t, lerp(a2, b2, 0.5), 0.45, lambda q: E.anda(c, t, "15", 1, [(c2, 2)], xb, y, s, some=True))
    cl = E.casa(s)
    if t < c2 + 0.1:
        E.saida(c, t, c2, lambda: (E.chave(c, xb + cl + 6, xb + 2 * cl + 6, y + 34, COR, ep(t, b2, 0.4), 24, 6),
                                   cen(c, t, b2 + 0.1, "1 casa", xb + 1.5 * cl, y + 130, 66, COR)))
    if t < a3 - 0.1:
        E.frase(c, t, lerp(b2, c2, 0.4), ps("anda 1 casa", "i", 76), XE + 40, 620, "left", 0.15)
        E.frase(c, t, lerp(b2, c2, 0.7), [("em cada número", "g", 68, COR)], XE + 40, 710)
    troca(c, t, [(a3 + 0.1, "37 ÷ 15 = 2"), (lerp(a3, b3, 0.72), "sobram 7"), (b3, "vírgula no resultado"), (c3, "desce o 5: 75"), (d3 + 0.1, "75 ÷ 15 = 5")],
          XE + 40, 620, 70)
    xc, yc, sc = 1110, 300, 112
    Dv = E.dividir("37,5", 15)
    E.conta_div(c, t, Dv, [lerp(a3, b3, 0.5), lerp(d3, e3, 0.55)], [c3, lerp(d3, e3, 0.68)], a3, xc, yc, sc, tv=b3)
    sobra(c, t, lerp(a3, b3, 0.76), c3, "7", xc, yc, sc, 1, 1)
    E.foco(c, t, e3, 0.5, lambda a: num_bola(c, "R$ 2,50", 420, 840, 170, 76, a))
    E.frase(c, t, e3 + 0.3, ps("o quilo", "g", 92, COR), 630, 872)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]

    def errado():
        E.frase(c, t, C["s14"] + 0.1, [("cuidado", "g", 110, ERRADO)] + ps("com o erro mais comum", "i", 90), W / 2, 220, "center", 0.15)
        E.frase(c, t, a4, ps("andar a vírgula", "i", 96) + [("só no divisor", "g", 92, ERRADO)], W / 2, 370, "center", 0.16)
        linha(c, t, [("1,5", "g", 160, TINTA, b4), ("÷", "g", 130, TINTA2, b4 + 1.0), ("25", "g", 160, ERRADO, b4 + 1.7)], 330, 680)
        cen(c, t, c4, "=", 1040, 680, 130, TINTA2)
        txt(c, t, c4 + 0.15, "0,06", 1130, 680, 170, ERRADO, "g")
    E.saida(c, t, C["s15"] - 0.1, errado)
    if t < C["s15"]:
        return

    a5, b5 = C["s15.a"], C["s15.b"]
    E.foco(c, t, lerp(C["s15"], a5, 0.4), 0.5, lambda a: E.moeda(c, 500, 380, 170, "25¢", a))
    E.frase(c, t, lerp(C["s15"], a5, 0.3), ps("a moeda", "i", 76), 500, 630, "center")
    if t >= a5:
        p = ep(t, a5, 0.5)
        M.arrow(c, 740, 380, 1040, 380, ERRADO, p, 6, 20, p)
    E.foco(c, t, a5 + 0.2, 0.5, lambda a: E.moeda(c, 1280, 380, 170, "R$ 25", a, ERRADO))
    E.frase(c, t, lerp(a5, b5, 0.45), ps("sem mudar o dinheiro", "i", 76), 1280, 630, "center", 0.13)
    E.frase(c, t, b5 - 0.5, ps("mudou um,", "i", 96) + [("muda o outro", "g", 92, COR)], W / 2, 800, "center", 0.16)
    E.frase(c, t, lerp(b5, C["s15.end"], 0.55), ps("o mesmo tanto de casas", "i", 84), W / 2, 930, "center", 0.13)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]

    def regras():
        E.frase(c, t, C["s16"] + 0.1, ps("agora, o atalho", "i", 90, CLARO), W / 2, 180, "center")
        for y, d, m, ti, ig, fala in ((370, "÷ 0,5", "× 2", a6, lerp(a6, b6, 0.67), "é dobrar"), (590, "÷ 0,25", "× 4", b6, lerp(b6, c6, 0.65), "")):
            E.foco(c, t, ti, 0.45, lambda a, y=y, d=d: E.escreve(c, d, 240, y, 136, "g", BR, a))
            E.foco(c, t, ig, 0.45, lambda a, y=y: centro(c, "=", 800, y, 120, "g", CLARO, a))
            E.foco(c, t, ig + 0.1, 0.45, lambda a, y=y, m=m: E.escreve(c, m, 900, y, 136, "g", CLARO, a))
            if fala:
                E.foco(c, t, ig + 0.1, 0.45, lambda a, y=y: E.escreve(c, fala, 1220, y - 6, 96, "i", BR, a))
        y = 850
        E.foco(c, t, c6, 0.45, lambda a: E.escreve(c, "1,5 × 4 =", 240, y, 136, "g", BR, a))
        E.foco(c, t, lerp(c6, C["s16.end"], 0.45), 0.5, lambda a: num_bola(c, "6", 1020, y - 50, 108, 136, a, E.CLARO))
        E.frase(c, t, lerp(c6, C["s16.end"], 0.55), ps("sem armar nada", "i", 90, BR), 1220, y - 6, "left", 0.13)
    E.saida(c, t, C["s17"] - 0.1, regras)
    if t < C["s17"]:
        return

    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]
    x, w, h = 560, 840, 130
    for y, n, s_, ti, nome in ((170, 2, "0,5", a7, "2 vezes"), (400, 4, "0,25", b7, "4 vezes")):
        E.foco(c, t, ti, 0.45, lambda a, y=y, s_=s_: centro(c, s_, 350, y + 100, 120, "g", BR, a))
        E.foco(c, t, ti, 0.45, lambda a, y=y, n=n, ti=ti: E.chocolate(c, x, y, w, h, n, [(i, CLARO, prog(t, ti + 0.3 + i * 0.25, 0.35)) for i in range(n)], a, escuro=True))
        E.foco(c, t, ti + 0.3 + n * 0.25, 0.45, lambda a, y=y, nome=nome: E.escreve(c, nome, x + w + 40, y + 92, 72, "g", CLARO, a))
    cen(c, t, lerp(a7, b7, 0.45), "cabe em cada inteiro", W / 2, 625, 72, BR, "i")
    E.frase(c, t, c7 - 0.8, ps("não compensa com", "i", 92, CLARO), XE, 790, "left", 0.15)
    txt(c, t, c7, "0,7", 880, 790, 120, BR, "g")
    E.frase(c, t, lerp(c7, C["s17.end"], 0.5), ps("aí,", "i", 92, CLARO) + [("tire a vírgula", "g", 100, BR)], XE, 930, "left", 0.15)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_, c_ = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 180)
    linha(c, t, [("um rolo de", "i", 92, TINTA, a_ - 0.5), ("5,4 m", "g", 110, COR, a_), ("de fita", "i", 92, TINTA, a_ + 0.9)], XE, 370)
    linha(c, t, [("cada laço usa", "i", 92, TINTA, b_ - 0.7), ("0,45 m", "g", 110, TINTA, b_)], XE, 540)
    E.frase(c, t, c_, ps("quantos", "i", 120) + [("laços?", "g", 116, COR)], XE, 760, "left", 0.2)
    E.frase(c, t, c_ + 1.0, ps("usando a fita toda", "i", 84), XE, 880, "left", 0.14)
    E.relogio(c, t, C["s19.a"], 1520, 400, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a0, b0, c0 = C["s20.a"], C["s20.b"], C["s20.c"]
    a1, b1, c1, d1 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
    s, y, xa, xb = 130, 330, XE + 10, 760
    h1, h2 = c0 + 0.1, c0 + 1.0
    cl = E.casa(s)
    E.foco(c, t, a0, 0.45, lambda q: E.anda(c, t, "54", 1, [(h1, 2), (h2, 3)], xa, y, s, some=True))
    cen(c, t, lerp(a0, b0, 0.22), "÷", 625, y, 104, TINTA2)
    E.foco(c, t, lerp(a0, b0, 0.37), 0.45, lambda q: (E.anda(c, t, "45", 0, [(h1, 1), (h2, 2)], xb, y, s, some=True), zero_some(c, t, xb, y, s, h1 + 0.2)))
    if t < c0 + 0.1:
        E.saida(c, t, c0, lambda: (E.chave(c, xb + 6, xb + 2 * cl + 6, y + 34, COR, ep(t, b0, 0.4), 24, 6),
                                   cen(c, t, b0 + 0.1, "2 casas", xb + cl, y + 130, 66, COR)))
    if t < a1 - 0.1:
        E.frase(c, t, lerp(b0, c0, 0.4), ps("anda 2 casas", "i", 76), XE + 40, 620, "left", 0.15)
        E.frase(c, t, lerp(b0, c0, 0.7), [("em cada número", "g", 68, COR)], XE + 40, 710)
    troca(c, t, [(a1 + 0.1, "54 ÷ 45 = 1"), (lerp(a1, b1, 0.72), "sobram 9"), (b1, "desce o 0: 90"), (c1 + 0.1, "90 ÷ 45 = 2")], XE + 40, 620, 70)
    xc, yc, sc = 1110, 300, 112
    Dv = E.dividir("540", 45)
    E.conta_div(c, t, Dv, [lerp(a1, b1, 0.5), lerp(c1, d1, 0.6)], [b1, lerp(c1, d1, 0.75)], a1, xc, yc, sc)
    sobra(c, t, lerp(a1, b1, 0.76), b1, "9", xc, yc, sc, 1, 1)
    E.foco(c, t, d1, 0.5, lambda a: num_bola(c, "12", 380, 840, 130, 130, a, CERTO))
    E.frase(c, t, d1 + 0.3, [("laços", "g", 110, CERTO)], 545, 880)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s22.a", "conte as casas do divisor"), ("s22.b", "ande a vírgula igual nos dois"), ("s22.c", "divida normalmente"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 300, y - 30, 56, 64, a))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 78)], 400, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a_, b_, c_, d_ = C["s23.a"], C["s23.b"], C["s23.c"], C["s23.d"]
    E.frase(c, t, C["s23"] + 0.1, ps("próxima aula", "i", 84), XE, 290)
    E.frase(c, t, a_, ps("fração", "g", 130, COR) + ps("em decimal", "i", 120), XE, 450, "left", 0.25)
    E.frase(c, t, b_, ps("decimal", "g", 130, COR) + ps("em fração", "i", 120), XE, 610, "left", 0.25)
    E.foco(c, t, c_, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 300, 76, estilo="g", cor=E.SOBRE, a=a))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(640, 325, p), ep(t, c_ + 0.2, 0.4))
    E.frase(c, t, d_, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, moedas=b_moedas, porque=b_porque, regra=b_regra, exemplo=b_exemplo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
