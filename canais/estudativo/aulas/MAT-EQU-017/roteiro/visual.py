"""Visual — Estudativo · MAT-EQU-017: praticando problemas e inequações (aula de prática, quatro situações).
Peças locais: livro() é a barra do livro em décimos (enunciado e atalho); colunas() põe cada termo numa coluna fixa, para o
resultado de cada multiplicação nascer embaixo do termo; operacao() é a pílula da conta feita nos dois lados. Todo instante vem de C[...]."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia
from fractions import Fraction as Fr

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-017_praticando_problemas_e_inequacoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "atalho", "questao2", "questao3", "questao4", "fim"))
BR = "#FFFFFF"
assert Fr(200, 2) + Fr(200, 5) + 60 == 200 and 5 * 200 + 2 * 200 + 600 == 10 * 200 and 600 / 3 == 200
assert Fr(1, 2) + Fr(1, 5) == Fr(7, 10) and 60 / 3 == 20 and 20 * 10 == 200
assert 90 + 60 * 6 == 75 * 6 == 450 and 90 + 60 * 7 == 510 and 75 * 7 == 525 and 90 / 15 == 6
assert all((1 <= 3 * x - 2 < 10) == (1 <= x < 4) for x in [0, 0.9, 1, 2.5, 3.99, 4, 5]) and 3 * 1 - 2 == 1
assert 500 - 20 * 18 == 140 and 500 - 20 * 17 == 160 > 140 and -360 / -20 == 18 and 20 * 17 == 340


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


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_res(c, t, t0, s, cx, cy, r=140, size=84, s2=None):
    def fn(a):
        E.bola(c, cx, cy, r, a=a)
        E.formula(c, s, cx, cy + size * (0.36 if not s2 else 0.1), size, "g", E.SOBRE, a, "center")
        if s2:
            centro(c, s2, cx, cy + size * 0.85, size * 0.6, "i", E.SOBRE, a)
    E.foco(c, t, t0, 0.5, fn)


def operacao(c, t, t0, op, y, x=300, escuro=False, rotulo="nos dois lados"):
    """pílula da conta feita nos dois lados, à esquerda da linha"""
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, op, x, y - 36, 60, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, t0 + 0.3, ps(rotulo, "i", 46, CLARO if escuro else TINTA2), x, y + 50, "center", 0.06)


def colunas(c, t, termos, xs, y, size):
    """termos [(fórmula, cor, t0)] centrados nas colunas xs"""
    for (s, cor, t0), x in zip(termos, xs):
        fcen(c, t, t0, s, x, y, size, cor)


def situacao(c, t, t0, n, y=170):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, f"situação {n}", XE + 150, y - 22, 54, "g", a=a, cor=E.SOBRE))


def livro(c, x, y, w, h, partes, a=1.0, escuro=False):
    """barra do livro em décimos. partes = [(de, até, cor, alfa, rótulo)] em décimos; o resto fica vazio com contorno"""
    if a <= 0:
        return
    fio = CLARO if escuro else TINTA2
    q = w / 10
    for i0, i1, cor, al, rot in partes:
        if al <= 0:
            continue
        c.drawRect(skia.Rect.MakeXYWH(x + i0 * q, y, (i1 - i0) * q, h), M.paint(cor, a * al))
        if rot:
            tom = BR if cor in (E.COR, TINTA, ERRADO, CERTO) else TINTA
            E.formula(c, rot, x + (i0 + i1) / 2 * q, y + h / 2 + 22, 60, "g", tom, a * al, "center")
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 6, 6)
    c.drawRRect(rr, M.paint(fio, a, stroke=4))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "4", XE - 8, 560, 380, "g", COR, a))
    E.frase(c, t, ka + 0.5, ps("situações", "i", 120), XE + 250, 520, "left")
    E.frase(c, t, ka + 1.3, ps("criadas para esta aula,", "i", 60, TINTA2), XE, 680, "left", 0.08)
    E.frase(c, t, ka + 2.6, ps("com valores inventados", "i", 60, TINTA2), XE, 760, "left", 0.08)
    x = 1080
    E.foco(c, t, kb, 0.5, lambda a: E.pilula(c, "pause e resolva", x + 260, 300, 70, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, kb + 0.6, ps("antes de ver a resposta", "i", 60), x + 260, 420, "center", 0.08)
    E.frase(c, t, kc, ps("responda com a", "i", 66) + [("unidade", "g", 70, COR)], x + 260, 600, "center", 0.1)
    for i, (s, k) in enumerate((("páginas", kc + 1.5), ("meses", kc + 2.2), ("horas", kc + 3.0))):
        E.foco(c, t, k, 0.4, lambda a, s=s, i=i: E.pilula(c, s, x + 30 + i * 240, 760, 56, "i", a=a, contorno=True, cor=COR))


# ---------------- ferramentas ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.3, ps("você vai usar", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s02.a"] - 0.6, 0.5, lambda a: E.escreve(c, "4", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s02.a"] - 0.45, 0.5, lambda a: E.escreve(c, "ferramentas", XE + 215, 700, 100, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s02.a", "montar a equação do problema"), ("s02.b", "achar o empate entre dois planos"),
             ("s02.c", "virar o sinal com número negativo"), ("s02.d", "resolver inequação dupla"))
    for i, (k, s) in enumerate(itens):
        y = 150 + i * 190
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 150, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(s, "g", 54, COR if i % 2 == 0 else TINTA)], x + 40, y + 95)
    ys = [150 + i * 190 + 130 for i in range(4)]
    py = ys[0]
    for i in range(1, 4):
        py = lerp(py, ys[i], ease_io(prog(t, C[itens[i][0]] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s02.a"], 0.4))
    E.frase(c, t, C["s02.end"] - 2.6, ps("se alguma travar,", "i", 56, COR) + ps("procure a aula no canal", "i", 56), x, 960, "left", 0.1)


# ---------------- situação 1: o livro ----------------
BXL, BYL, BWL, BHL = 170, 560, 1150, 130


def b_questao1(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s03.{k}"] for k in "abcde")
    situacao(c, t, ka, 1)
    E.frase(c, t, kb - 0.6, ps("leu", "i", 64) + [("metade do livro", "g", 64, COR)] + ps("no 1º mês", "i", 64), XE, 310, "left", 0.1)
    E.frase(c, t, kc - 0.4, [("um quinto do livro inteiro", "g", 64)] + ps("no 2º mês", "i", 64), XE, 420, "left", 0.1)
    E.foco(c, t, kb - 0.6, 0.5, lambda a: livro(c, BXL, BYL, BWL, BHL, [(0, 5, E.COR, ep(t, kb + 0.3, 0.5), "f{1}{2}"),
                                                                    (5, 7, TINTA, ep(t, kc + 0.6, 0.5), "f{1}{5}")], a))
    E.foco(c, t, kd, 0.5, lambda a: E.formula(c, "faltam 60", BXL + 8.5 * BWL / 10, BYL + BHL / 2 + 20, 56, "g", COR, a, "center"))
    E.frase(c, t, ke, ps("quantas páginas", "i", 84) + [("tem o livro?", "g", 84, COR)], XE, 860, "left", 0.11)
    E.relogio(c, t, C["s04.a"], 1620, 330, 150)


def b_resposta1(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s05.{k}"] for k in "abcde")
    xs = (500, 660, 820, 980, 1150, 1310, 1470)
    tm = lerp(kc, kd, 0.6)  # "O MMC de dois e cinco é dez"

    def monta():
        E.frase(c, t, ka, [("x", "g", 80, COR)] + ps("é o livro inteiro", "i", 76), W / 2, 160, "center", 0.1)
        E.frase(c, t, kb - 1.2, ps("leu + falta =", "i", 64, TINTA2) + [("o livro todo", "g", 64, TINTA2)], W / 2, 260, "center", 0.1)
        t0s = (kc, kc + 0.8, kc + 1.0, kc + 1.6, kc + 1.9, kc + 2.6, kc + 3.2)
        colunas(c, t, [(s, TINTA, k) for s, k in zip(("f{x}{2}", "+", "f{x}{5}", "+", "60", "=", "x"), t0s)], xs, 500, 104)
        E.foco(c, t, tm, 0.5, lambda a: E.pilula(c, "MMC de 2 e 5 = 10", 1660, 230, 50, "g", a=a, cor=E.SOBRE))
        for i, k in ((0, kd), (2, kd + 0.15), (4, kd + 1.8), (6, kd + 0.3)):
            E.foco(c, t, k, 0.4, lambda a, i=i: E.pilula(c, "× 10", xs[i], 360, 42, "g", a=a, cor=E.SOBRE))
        t1 = (ke, ke + 0.6, ke + 0.9, ke + 1.5, ke + 1.8, ke + 2.2, ke + 2.9)
        colunas(c, t, [(s, COR, k) for s, k in zip(("5x", "+", "2x", "+", "600", "=", "10x"), t1)], xs, 700, 104)
    E.saida(c, t, C["s06"] - 0.1, monta)
    if t < C["s06"]:
        return
    a6, b6, c6, d6, e6, f6, g6, h6 = (C[f"s06.{k}"] for k in "abcdefgh")
    cx = 820
    fcen(c, t, a6, "7x + 600 = 10x", cx, 190, 110)
    operacao(c, t, b6, "− 7x", 350)
    fcen(c, t, c6, "600 = 3x", cx + 80, 350, 110)
    operacao(c, t, lerp(c6, d6, 0.6), "÷ 3", 520)
    fcen(c, t, d6, "x = 200", cx + 80, 520, 110, COR)
    bola_res(c, t, e6, "200", 1600, 380, 160, 110, "páginas")
    E.frase(c, t, f6 - 0.9, [("conferindo", "i", 64, COR)], W / 2, 680, "center")
    fcen(c, t, f6, "f{200}{2} = 100", 560, 800, 90)
    fcen(c, t, g6, "f{200}{5} = 40", 1300, 800, 90)
    fcen(c, t, h6, "100 + 40 + 60 = 200", W / 2 - 40, 990, 96, CERTO)
    E.foco(c, t, h6 + 2.2, 0.5, lambda a: E.selo(c, W / 2 + 520, 955, 46, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    ka, kb, kc, kd, ke = (C[f"s07.{k}"] for k in "abcde")
    t5, t2 = lerp(ka, kb, 0.45), lerp(ka, kb, 0.7)  # "metade é cinco décimos" / "um quinto é dois décimos"
    x, y, w, h = 260, 420, 1400, 140

    def um():
        E.frase(c, t, C["s07"] + 0.3, ps("o atalho:", "i", 80, CLARO) + [("ache a fração que falta", "g", 80, BR)], W / 2, 170, "center", 0.11)
        fcen(c, t, t5, "f{1}{2} = f{5}{10}", 600, 300, 76, CLARO)
        fcen(c, t, t2, "f{1}{5} = f{2}{10}", 1320, 300, 76, CLARO)
        partes = [(0, 5, CLARO, ep(t, t5, 0.5), None), (5, 7, BR, ep(t, t2, 0.5), None)]
        E.foco(c, t, ka, 0.5, lambda a: livro(c, x, y, w, h, partes, a, escuro=True))
        q = w / 10
        for i in range(1, 10):
            M.line(c, x + i * q, y + 6, x + i * q, y + h - 6, "#07070F" if i < 7 else CLARO, ep(t, ka + 0.3, 0.5), 3)
        for i in range(10):
            k = kd if i >= 7 else ke
            E.foco(c, t, k, 0.4, lambda a, i=i: centro(c, "20", x + (i + 0.5) * q, y + h / 2 + 22, 56, "g", "#07070F" if i < 7 else BR, a))
        E.frase(c, t, kb, ps("leu", "i", 70, CLARO) + [("7/10", "g", 76, BR)], x + 3.5 * q, y + h + 110, "center", 0.1)
        E.frase(c, t, kc, ps("faltam", "i", 64, CLARO) + [("3/10 = 60 páginas", "g", 64, BR)], x + 8.5 * q - 150, y + h + 110, "center", 0.1)
        fcen(c, t, kd, "f{1}{10} = 60 ÷ 3 = 20", 640, 900, 84, BR)
        fcen(c, t, ke, "f{10}{10} = 10 × 20 = 200", 1380, 900, 84, CLARO)
    E.saida(c, t, C["s08"] - 0.1, um)
    if t < C["s08"]:
        return
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    E.frase(c, t, a8, ps("funciona porque", "i", 76, CLARO) + [("o que falta", "g", 80, BR)], W / 2, 260, "center", 0.12)
    E.frase(c, t, a8 + 1.2, ps("também é", "i", 76, CLARO) + [("uma fração do total", "g", 80, BR)], W / 2, 370, "center", 0.12)
    E.foco(c, t, b8, 0.5, lambda a: E.selo(c, 260, 575, 50, False, a))
    E.frase(c, t, b8 + 0.1, ps("não compensa se a 2ª fração for", "i", 66, CLARO) + [("do que sobrou", "g", 70, BR)], 340, 600, "left", 0.09)
    E.frase(c, t, b8 + 2.2, ps("e não do livro inteiro", "i", 60, CLARO), 340, 690, "left", 0.09)
    E.frase(c, t, c8, ps("aí,", "i", 84, CLARO) + [("monte a equação com calma", "g", 84, BR)], W / 2, 880, "center", 0.12)


# ---------------- situação 2: academias ----------------
def cartao(c, t, t0, letra, l1, l2, y, x=XE):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, x + 50, y - 20, 50, a=a), centro(c, letra, x + 50, y + 2, 62, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.2, [(l1, "g", 60, COR)], x + 130, y - 20)
    E.frase(c, t, t0 + 0.8, ps(l2, "i", 56), x + 130, y + 50, "left", 0.08)


def b_questao2(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s09.{k}"] for k in "abcde")
    situacao(c, t, ka, 2)
    cartao(c, t, kb - 0.6, "A", "R$ 90 de matrícula", "mais R$ 60 por mês", 340)
    cartao(c, t, kc - 1.0, "B", "sem matrícula", "R$ 75 por mês", 560)
    E.frase(c, t, kd, ps("em quantos meses o", "i", 70) + [("gasto total fica igual?", "g", 70, COR)], XE, 780, "left", 0.1)
    E.frase(c, t, ke, ps("depois disso,", "i", 70) + [("qual sai mais barata?", "g", 70, COR)], XE, 900, "left", 0.1)
    E.relogio(c, t, C["s10.a"], 1620, 360, 160)


def b_resposta2(c, t, C, b):
    ka, kb, kc, kd, ke, kf, kg = (C[f"s11.{k}"] for k in "abcdefg")
    a2, b2, c2, d2 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    cx = 820

    def resolve():
        E.frase(c, t, ka, [("x", "g", 80, COR)] + ps("são os meses", "i", 76), cx, 160, "center", 0.1)
        fcen(c, t, kb, "90 + 60x = 75x", cx, 300, 110)
        operacao(c, t, kc, "− 60x", 460)
        fcen(c, t, kd, "90 = 15x", cx + 80, 460, 110)
        operacao(c, t, lerp(kd, ke, 0.5), "÷ 15", 630)
        fcen(c, t, ke, "x = 6", cx + 80, 630, 110, COR)
        bola_res(c, t, kf, "6", 1600, 420, 160, 120, "meses")
        fcen(c, t, kg, "90 + 60 × 6 = 450", 600, 880, 76)
        fcen(c, t, kg + 0.6, "75 × 6 = 450", 1340, 880, 76)
        E.frase(c, t, kg + 1.2, ps("R$ 450 cada", "g", 60, CERTO), W / 2, 990, "center", 0.1)
    E.saida(c, t, C["s12"] - 0.1, resolve)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"] + 0.3, ps("depois de 6 meses, ganha", "i", 76) + [("a mensalidade menor", "g", 76, COR)], W / 2, 200, "center", 0.11)
    E.foco(c, t, b2, 0.5, lambda a: E.pilula(c, "academia A", W / 2, 360, 80, "g", fundo=CERTO, cor=BR, a=a))
    E.frase(c, t, c2 - 1.2, ps("no 7º mês", "i", 70, TINTA2), W / 2, 530, "center", 0.1)
    fcen(c, t, c2, "A: 90 + 60 × 7 = 510", W / 2, 690, 96, CERTO)
    fcen(c, t, d2, "B: 75 × 7 = 525", W / 2, 860, 96)


# ---------------- situação 3: inequação dupla ----------------
def b_questao3(c, t, C, b):
    ka, kb, kc = C["s13.a"], C["s13.b"], C["s13.c"]
    situacao(c, t, ka, 3)
    E.frase(c, t, kb - 0.6, ps("resolva", "i", 80), XE, 330, "left")
    E.foco(c, t, kb, 0.5, lambda a: E.formula(c, "1 ≤ 3x − 2 < 10", XE, 540, 150, "g", COR, a))
    E.frase(c, t, kc, ps("depois:", "i", 70) + [("como ficam as bolinhas", "g", 70, COR)] + ps("na reta?", "i", 70), XE, 760, "left", 0.1)
    E.relogio(c, t, C["s14.a"], 1620, 360, 160)


def b_resposta3(c, t, C, b):
    ka, kb, kc, kd = (C[f"s15.{k}"] for k in "abcd")
    a6, b6, c6, d6, e6 = (C[f"s16.{k}"] for k in "abcde")
    cx = 960
    fcen(c, t, C["s15"] + 0.2, "1 ≤ 3x − 2 < 10", cx, 170, 100)
    operacao(c, t, ka, "+ 2", 320, rotulo="nas três partes")
    fcen(c, t, kb, "3 ≤ 3x < 12", cx, 320, 100)
    operacao(c, t, kc, "÷ 3", 480, rotulo="positivo: o sinal fica")
    fcen(c, t, kd, "1 ≤ x < 4", cx, 480, 110, COR)
    y = 720
    vx = E.reta(c, t, C["s16"], 380, 1540, y, 0, 5, (0, 1, 2, 3, 4, 5), size=56)
    if t < c6:
        if t >= a6:
            c.drawCircle(vx(1), y, 17, M.paint(E.COR, ep(t, a6, 0.3)))
        if t >= b6:
            c.drawCircle(vx(4), y, 17, M.paint(E.PAPEL, ep(t, b6, 0.3)))
            c.drawCircle(vx(4), y, 17, M.paint(E.COR, ep(t, b6, 0.3), stroke=6))
    E.intervalo(c, t, c6, vx, y, 1, 4, True, False)
    E.frase(c, t, a6 + 0.2, ps("fechada:", "i", 50, TINTA2) + [("tem o igual", "g", 50, TINTA2)], vx(1), y - 60, "center", 0.07)
    E.frase(c, t, b6 + 0.2, ps("aberta", "i", 50, TINTA2), vx(4), y - 60, "center")
    fcen(c, t, d6, "3 × 1 − 2 = 1", 820, 960, 90)
    fcen(c, t, lerp(d6, e6, 0.6), "1 ≤ 1", 1280, 960, 90, CERTO)
    E.foco(c, t, e6, 0.5, lambda a: E.selo(c, 1480, 930, 44, True, a))


# ---------------- situação 4: a caixa-d'água ----------------
def b_questao4(c, t, C, b):
    ka, kb, kc, kd = (C[f"s17.{k}"] for k in "abcd")
    situacao(c, t, ka, 4)
    E.frase(c, t, ka + 0.6, ps("a última:", "i", 60, TINTA2) + [("junta tudo", "g", 60, TINTA2)], XE + 340, 150, "left", 0.1)
    E.frase(c, t, kb - 0.8, ps("caixa-d'água com", "i", 70) + [("500 litros", "g", 76, COR)], XE, 330, "left", 0.1)
    E.frase(c, t, kc - 1.0, ps("um vazamento: perde", "i", 70) + [("20 litros por hora", "g", 76, COR)], XE, 450, "left", 0.1)
    E.frase(c, t, kd, ps("por quantas", "i", 70) + [("horas inteiras,", "g", 70, COR)] + ps("no máximo,", "i", 70), XE, 640, "left", 0.1)
    E.frase(c, t, lerp(kd, C["s17.end"], 0.55), ps("ainda fica com", "i", 70) + [("mais de 140 litros?", "g", 70, COR)], XE, 750, "left", 0.1)
    E.relogio(c, t, C["s18.a"], 1620, 360, 160)


def b_resposta4(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s19.{k}"] for k in "abcde")
    a0, b0, c0, d0, e0, f0 = (C[f"s20.{k}"] for k in "abcdef")
    a1, b1, c1, d1 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
    cx = 820

    def resolve():
        E.frase(c, t, ka, [("x", "g", 80, COR)] + ps("são as horas", "i", 76), cx, 150, "center", 0.1)
        xs, ws = [], []
        partes = [("500 − 20x", TINTA, kb), (">", COR, kc), ("140", TINTA, kc + 0.4)]
        wsz = [E.formula(c, s, 0, 0, 104, a=0) for s, _, _ in partes]
        x = cx - (sum(wsz) + 2 * 30) / 2
        for (s, cor, k), w_ in zip(partes, wsz):
            E.formula_em(c, t, k, s, x, 290, 104, "g", cor)
            x += w_ + 30
        operacao(c, t, kd, "− 500", 450)
        fcen(c, t, ke, "−20x > −360", cx + 80, 450, 104)
        operacao(c, t, a0, "÷ (−20)", 620)
        E.foco(c, t, b0, 0.5, lambda a: E.pilula(c, "vira o sinal!", cx + 470, 625, 50, "g", fundo=ERRADO, cor=BR, a=a))
        fcen(c, t, c0, "x < 18", cx + 80, 660, 110, COR)
        E.frase(c, t, d0 - 0.4, ps("com 18 h: sobram", "i", 62) + [("140,", "g", 64, ERRADO)] + ps("e 140 não é mais que 140", "i", 62), W / 2, 830, "center", 0.08)
        E.frase(c, t, e0 - 2.4, ps("maior inteiro abaixo de 18:", "i", 66) + [("17", "g", 76, COR)], W / 2, 950, "center", 0.1)
        bola_res(c, t, f0, "17", 1620, 430, 160, 120, "horas")
    E.saida(c, t, C["s21"] - 0.1, resolve)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.2, [("conferindo", "i", 84, COR)] + ps("com 17 horas", "i", 84), W / 2, 200, "center", 0.12)
    fcen(c, t, a1, "20 × 17 = 340", W / 2, 400, 110)
    fcen(c, t, b1, "500 − 340 = 160", W / 2, 580, 110)
    E.frase(c, t, b1 + 1.6, ps("litros", "i", 70, TINTA2), W / 2 + 450, 580, "left")
    fcen(c, t, c1, "160 > 140", W / 2 - 40, 790, 120, CERTO)
    E.foco(c, t, d1, 0.5, lambda a: E.selo(c, W / 2 + 370, 750, 54, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s22.a", "o desconhecido vira x"), ("s22.b", "a pergunta decide: =, > ou <"), ("s22.c", "responda com a unidade certa"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 240, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 80)], 330, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a3, b3, c3 = C["s23.a"], C["s23.b"], C["s23.c"]
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 84), XE, 220, passo=0.14)
    E.frase(c, t, a3, [("duas coisas desconhecidas", "g", 84, COR)] + ps("ao mesmo tempo", "i", 80), XE, 350, passo=0.1)
    E.frase(c, t, b3, ps("duas letras e duas equações:", "i", 72), XE, 470, passo=0.1)
    E.frase(c, t, c3, ps("o", "i", 80) + [("sistema,", "g", 84, COR)] + ps("pelo método da substituição", "i", 72), XE, 590, passo=0.1)
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s23.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, C["s23.d"] + 0.2, 0.4))
    E.frase(c, t, C["s23.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, atalho=b_atalho, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
