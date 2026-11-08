"""Visual — Estudativo · MAT-TOP-003: distribuição binomial.
Mesma linguagem do módulo (MAT-TOP-001): binom() em pé, triângulo de Pascal em números soltos, resposta na esfera.
Peças desta aula: moeda() (cara = cheia na cor da matéria; coroa = branca com contorno), dado() (face do dado com o número
ou "não 6"), ordens das duas caras em grade (as 10 escolhas de 2 jogadas entre 5).
Sucesso em índigo, fracasso em tinta; erro em vermelho, certo em verde; atalho no palco escuro.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
from math import comb
from fractions import Fraction as F
from itertools import combinations
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-003_distribuicao_binomial.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ordem", "regra", "dado", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ORDENS = list(combinations(range(5), 2))
assert len(ORDENS) == 10 == comb(5, 2) and F(1, 2) ** 5 == F(1, 32) and 10 * F(1, 32) == F(5, 16)
assert round(float(F(5, 16)) * 100, 2) == 31.25 and round(float(F(1, 32)) * 100, 3) == 3.125
assert comb(3, 1) * F(1, 6) * F(5, 6) ** 2 == F(75, 216) and F(5, 6) ** 2 == F(25, 36) and 0.34 < 75 / 216 < 0.35
assert [comb(5, k) for k in range(6)] == [1, 5, 10, 10, 5, 1] and 2 ** 5 == 32
assert comb(3, 2) * F(1, 4) ** 2 * F(3, 4) == F(9, 64) and F(1, 4) ** 2 == F(1, 16) and 0.14 < 9 / 64 < 0.141


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças do módulo (iguais às da MAT-TOP-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def num(c, t, t0, s, x, y, size, cor=TINTA, est="g"):
    E.foco(c, t, t0, 0.45, lambda a: centro(c, str(s), x, y + size * 0.36, size, est, cor, a))


def binom(c, n, p, cx, cy, size, cor=None, a=1.0, cor_n=None, cor_p=None):
    cor = cor or TINTA
    n, p = str(n), str(p)
    w = max(E.larg(n, "g", size), E.larg(p, "g", size))
    if a <= 0:
        return w + size * 0.9
    centro(c, n, cx, cy - size * 0.1, size, "g", cor_n or cor, a)
    centro(c, p, cx, cy + size * 0.82, size, "g", cor_p or cor, a)
    h, k = size * 0.98, size * 0.24
    for lado in (-1, 1):
        x0 = cx + lado * (w / 2 + size * 0.22)
        path = skia.Path()
        path.moveTo(x0, cy - h)
        path.quadTo(x0 + lado * k * 1.6, cy, x0, cy + h)
        c.drawPath(path, M.paint(cor, a, stroke=max(4, size * 0.075), cap_round=True))
    return w + size * 0.9


def binom_em(c, t, t0, n, p, cx, cy, size, cor=None, **kw):
    E.foco(c, t, t0, 0.5, lambda a: binom(c, n, p, cx, cy, size, cor, a, **kw))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, str(s), cx, cy + size * 0.36, size, "g", BR, a, "center")))


# ---------------- peças desta aula ----------------
def moeda(c, x, y, r, face, a=1.0, escuro=False):
    """cara = cheia na cor da matéria; coroa = branca com contorno; '?' = cinza"""
    if a <= 0:
        return
    if face == "cara":
        c.drawCircle(x, y, r, M.paint(COR, a))
        c.drawCircle(x, y, r * 0.8, M.paint(BR, 0.35 * a, stroke=max(2, r * 0.05)))
        if r >= 40:
            centro(c, "cara", x, y + r * 0.13, r * 0.36, "b", BR, a)
    elif face == "coroa":
        c.drawCircle(x, y, r, M.paint("#2A2A33" if escuro else BR, a))
        c.drawCircle(x, y, r, M.paint(CLARO if escuro else TINTA, a, stroke=max(3, r * 0.07)))
        if r >= 40:
            centro(c, "coroa", x, y + r * 0.13, r * 0.32, "b", CLARO if escuro else TINTA, a)
    else:
        c.drawCircle(x, y, r, M.paint(CINZA, 0.35 * a))
        centro(c, "?", x, y + r * 0.3, r * 0.8, "g", BR, a)


def moeda_em(c, t, t0, x, y, r, face, escuro=False):
    E.foco(c, t, t0, 0.45, lambda a: moeda(c, x, y, r * ease_back(prog(t, t0, 0.45)), face, a, escuro))


def fileira(c, t, t0, caras, x0, y, r, gap, passo=0.12):
    for i in range(5):
        moeda_em(c, t, t0 + i * passo, x0 + i * gap, y, r, "cara" if i in caras else "coroa")


def dado(c, x, y, s, txt, cor, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x - s / 2, y - s / 2, s, s, s * 0.18, cor if txt == "6" else BR, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - s / 2, y - s / 2, s, s), s * 0.18, s * 0.18), M.paint(cor, a, stroke=5))
    centro(c, txt, x, y + s * (0.16 if txt == "6" else 0.08), s * (0.5 if txt == "6" else 0.24), "g" if txt == "6" else "b", BR if txt == "6" else cor, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        for i in range(5):
            x = 460 + i * 250
            face = "?" if t < C["s01.b"] else ("cara" if i in (0, 2) else "coroa")
            if t < C["s01.b"]:
                moeda_em(c, t, C["s01.a"] + i * 0.15, x, 330, 95, "?")
            else:
                moeda_em(c, t, C["s01.b"] + i * 0.1, x, 330, 95, face)
        E.frase(c, t, C["s01.b"], [("exatamente", "i", 84), ("2", "g", 84, COR), ("caras?", "g", 84, COR)], W / 2, 560, "center")
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.fracao(c, 2, 5, 560, 780, 130, ERRADO, a))
        if t >= C["s01.d"]:
            E.risco(c, 470, 880, 650, 680, t, C["s01.d"] - 0.2, largura=14)
        bola_txt(c, t, C["s01.d"], "f{5}{16}", 1120, 780, 135, 110)
        E.foco(c, t, C["s01.d"] + 0.8, 0.4, lambda a: E.escreve(c, "≈ 31%", 1300, 815, 100, "g", COR, a))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 560, 270 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("a", "i", 110), ("chance", "g", 120, COR), ("de", "i", 110)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.5, [("um", "i", 110), ("número", "g", 120)], XE, 630)
        E.frase(c, t, C["s02.a"] + 2.0, [("exato", "g", 120, COR), ("de", "i", 110), ("vezes", "i", 110)], XE, 780)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1300, 545, 80, "g", BR, a),
                                                      E.escreve(c, "de prova", 1320, 630, 80, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 84), XE, 200)
    E.frase(c, t, C["s03.a"], [("2", "g", 110, COR), ("coisas", "i", 100)], XE + 640, 200)
    x, w = XE, 1580
    for i, k in enumerate(("s03.b", "s03.c")):
        y = 290 + i * 340
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 290, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("independentes:", "i", 66), ("multiplique", "g", 64, COR)], x + 50, 400)
    E.formula_em(c, t, C["s03.b"] + 0.8, "f{1}{2} · f{1}{2} = f{1}{4}", x + 50, 520, 84, "g", TINTA)
    E.frase(c, t, C["s03.c"] + 0.1, [("binomial:", "i", 66), ("quantos", "g", 64, COR), ("jeitos", "g", 64, COR)], x + 50, 740)
    binom_em(c, t, C["s03.c"] + 0.8, 5, 2, x + 110, 810, 70)
    E.foco(c, t, C["s03.c"] + 1.0, 0.4, lambda a: E.escreve(c, "= 10", x + 200, 860, 84, "g", TINTA, a))
    E.foco(c, t, C["s03.c"] + 1.2, 0.4, lambda a: E.escreve(c, "escolher 2 entre 5", x + 520, 860, 56, "i", TINTA2, a))


# ---------------- uma ordem ----------------
def b_ordem(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("uma", "i", 90), ("ordem", "g", 84, COR), ("só", "i", 90)], W / 2, 200, "center")
    xs = [460 + i * 250 for i in range(5)]
    for i, x in enumerate(xs):
        moeda_em(c, t, C["s04.b"] + i * 0.3, x, 400, 90, "cara" if i < 2 else "coroa")
        E.foco(c, t, C["s04.c"] + i * 0.1, 0.4, lambda a, x=x: E.fracao(c, 1, 2, x, 600, 70, TINTA, a))
        if i < 4:
            E.foco(c, t, C["s04.d"] + i * 0.1, 0.4, lambda a, x=x: centro(c, "×", x + 125, 615, 60, "g", TINTA2, a))
    E.formula_em(c, t, C["s04.d"] + 0.4, "(f{1}{2})^5", 620, 870, 110, "g", TINTA)
    E.foco(c, t, C["s04.e"], 0.4, lambda a: E.escreve(c, "=", 920, 870, 110, "g", TINTA, a))
    bola_txt(c, t, C["s04.e"] + 0.2, "f{1}{32}", 1140, 840, 120, 96)


# ---------------- quantas ordens ----------------
def b_ordens(c, t, C, b):
    E.frase(c, t, C["s05"], ps("2 caras em qualquer par de jogadas", "i", 70), W / 2, 160, "center")
    # grade: as 10 ordens, em duas colunas de 5
    r, gap = 30, 76
    destaque = {ORDENS.index((0, 2)): "s05.b", ORDENS.index((3, 4)): "s05.c"}
    for j, caras in enumerate(ORDENS):
        col, lin = divmod(j, 5)
        x0, y = 150 + col * 470, 290 + lin * 120
        t0 = C[destaque[j]] if j in destaque else C["s05.d"] + 0.15 * j
        for i in range(5):
            moeda_em(c, t, t0 + i * 0.05, x0 + i * gap, y, r, "cara" if i in caras else "coroa")
        if j in destaque and t >= t0:
            q = ep(t, t0 + 0.3, 0.4)
            E.caixa_pontilhada(c, x0 - 50, y - 50, 4 * gap + 100, 100, q, COR, prog_=q)
    binom_em(c, t, C["s05.e"], 5, 2, 1280, 330, 90, cor=COR)
    E.foco(c, t, C["s05.e"] + 0.3, 0.4, lambda a: E.escreve(c, "= 10 ordens", 1380, 380, 80, "g", COR, a))
    E.formula_em(c, t, C["s06.a"], "10 · f{1}{32} = f{10}{32}", 1140, 650, 90, "g", TINTA)
    E.foco(c, t, C["s06.b"], 0.4, lambda a: E.escreve(c, "÷ 2", 1180, 830, 64, "i", TINTA2, a))
    bola_txt(c, t, C["s06.b"] + 0.3, "f{5}{16}", 1520, 820, 120, 96, CERTO)


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    def parte1():
        E.frase(c, t, C["s07.a"], [("distribuição", "g", 110, COR), ("binomial", "g", 110)], W / 2, 220, "center")
        itens = (("s07.b", "a mesma tentativa, várias vezes"), ("s07.c", "mesma chance, uma não muda a outra"), ("s07.d", "só sucesso ou fracasso"))
        for i, (k, s) in enumerate(itens):
            y = 440 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 46, a=a), centro(c, str(i + 1), 300, y - 6, 52, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 70)], 390, y)
    E.saida(c, t, C["s08"] - 0.1, parte1)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08.a"], ps("exatamente k sucessos em n tentativas", "i", 70), W / 2, 220, "center")
    y = 520
    binom_em(c, t, C["s08.b"], "n", "k", 520, y - 40, 110, cor=COR)
    E.formula_em(c, t, C["s08.c"], "· p^k", 650, y + 40, 120, "g", COR)
    E.formula_em(c, t, C["s08.d"], "· q^{n − k}", 940, y + 40, 120, "g", TINTA)
    E.foco(c, t, C["s08.c"] + 0.3, 0.4, lambda a: E.escreve(c, "sucesso", 690, y + 170, 52, "i", COR, a))
    E.foco(c, t, C["s08.d"] + 0.3, 0.4, lambda a: E.escreve(c, "fracasso", 990, y + 170, 52, "i", TINTA, a))
    E.foco(c, t, C["s08.e"], 0.5, lambda a: (E.pilula(c, "p = chance de sucesso", 640, 860, 54, "b", fundo=COR, a=a),
                                            E.pilula(c, "q = chance de fracasso", 1280, 860, 54, "b", fundo=TINTA, a=a)))


# ---------------- dado ----------------
def b_dado(c, t, C, b):
    E.frase(c, t, C["s09.a"], [("3", "g", 80, COR), ("jogadas", "i", 84), ("do", "i", 84), ("dado", "i", 84)], XE, 190)
    E.frase(c, t, C["s09.b"], [("exatamente", "i", 84), ("um", "i", 84), ("6", "g", 84, COR)], 1000, 190)
    E.foco(c, t, C["s09.c"], 0.4, lambda a: (dado(c, 260, 360, 120, "6", COR, a), E.escreve(c, "sucesso:", 360, 380, 60, "i", COR, a)))
    E.formula_em(c, t, C["s09.c"] + 0.3, "f{1}{6}", 640, 385, 84, "g", COR)
    E.foco(c, t, C["s09.d"], 0.4, lambda a: (dado(c, 1010, 360, 120, "não 6", TINTA, a), E.escreve(c, "fracasso:", 1110, 380, 60, "i", TINTA, a)))
    E.formula_em(c, t, C["s09.d"] + 0.6, "f{5}{6}", 1400, 385, 84, "g", TINTA)
    if t < C["s10"]:
        return
    # as três ordens
    for j in range(3):
        for i in range(3):
            x, y = 260 + i * 110, 560 + j * 120
            txt = "6" if i == j else "não 6"
            E.foco(c, t, C["s10.a"] + 0.4 * j + 0.08 * i, 0.4, lambda a, x=x, y=y, txt=txt: dado(c, x, y, 90, txt, COR if txt == "6" else TINTA, a))
    binom_em(c, t, C["s10.a"], 3, 1, 640, 640, 80, cor=COR)
    E.foco(c, t, C["s10.a"] + 0.3, 0.4, lambda a: E.escreve(c, "= 3", 720, 680, 80, "g", COR, a))
    E.formula_em(c, t, C["s10.b"], "f{1}{6}", 980, 600, 76, "g", COR)
    E.formula_em(c, t, C["s10.c"], "(f{5}{6})^2 = f{25}{36}", 1180, 600, 76, "g", TINTA)
    E.formula_em(c, t, C["s10.d"], "3 · f{1}{6} · f{25}{36} = f{75}{216}", 940, 820, 70, "g", TINTA)
    E.formula_em(c, t, C["s10.e"], "= f{25}{72}", 940, 990, 80, "g", CERTO)
    E.foco(c, t, C["s10.e"] + 1.0, 0.4, lambda a: E.escreve(c, "≈ 35%", 1250, 1010, 64, "g", CERTO, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], XE, 200)
    E.frase(c, t, C["s11.a"], ps("esquecer o binomial", "i", 72, ERRADO), 1050, 200)
    fileira(c, t, C["s11.b"], (0, 1), 300, 400, 60, 150)
    E.formula_em(c, t, C["s11.b"] + 0.8, "= f{1}{32}", 1050, 430, 90, "g", ERRADO)
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.escreve(c, "≈ 3%", 1400, 430, 90, "g", ERRADO, a))
    if t >= C["s11.d"]:
        E.risco(c, 1040, 470, 1600, 330, t, C["s11.d"] - 0.2, largura=12)
    E.formula_em(c, t, C["s11.d"], "10 ordens · f{1}{32} = f{10}{32}", XE, 720, 96, "g", CERTO)
    E.frase(c, t, C["s11.e"], [("multiplique", "i", 74), ("pelo", "i", 74), ("número", "i", 74), ("de", "i", 74), ("ordens", "g", 70, CERTO)], W / 2, 920, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def parte1():
        E.frase(c, t, C["s12"], [("atalho:", "i", 80, CLARO), ("chance", "g", 76, BR)], W / 2 - 160, 220, "center")
        E.formula_em(c, t, C["s12.a"], "f{1}{2}", W / 2 + 200, 220, 90, "g", BR, "center")
        E.formula_em(c, t, C["s12.b"], "toda ordem: (f{1}{2})^n", W / 2, 450, 90, "g", CLARO, "center")
        E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "f{linha n do triângulo}{2^n}", W / 2, 760, 96, "g", BR, a, "center"))
    E.saida(c, t, C["s13"] - 0.1, parte1)
    if t < C["s13"]:
        return
    linha = [comb(5, k) for k in range(6)]
    xs = [360 + k * 240 for k in range(6)]
    for k in range(6):
        num(c, t, C["s13.a"] + k * 0.15, linha[k], xs[k], 260, 90, BR)
        E.foco(c, t, C["s13.a"] + 1.0, 0.4, lambda a, k=k: (M.line(c, xs[k] - 70, 330, xs[k] + 70, 330, CLARO, a, 5),
                                                         centro(c, "32", xs[k], 420, 70, "g", CLARO, a)))
        E.foco(c, t, C["s13.a"] + 1.2, 0.4, lambda a, k=k: centro(c, f"{k} caras" if k != 1 else "1 cara", xs[k], 520, 42, "i", CLARO, a))
    for k, cue in ((0, "s13.b"), (2, "s13.c"), (3, "s13.d")):
        if t >= C[cue]:
            q = ep(t, C[cue], 0.4)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xs[k] - 100, 180, 200, 380), 26, 26), M.paint(CERTO, q, stroke=6))
    E.foco(c, t, C["s13.e"], 0.5, lambda a: E.formula(c, "1 + 5 + 10 + 10 + 5 + 1 = 32 = 2^5", W / 2, 720, 72, "g", BR, a, "center"))
    E.foco(c, t, C["s13.f"], 0.5, lambda a: E.pilula(c, "chance diferente de 1/2: regra completa", W / 2, 900, 60, "b", fundo=COR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s14.a"], [("3", "g", 90, COR), ("questões,", "i", 90)], XE, 380)
    E.frase(c, t, C["s14.a"] + 1.2, [("4", "g", 90, COR), ("alternativas", "i", 90), ("cada", "i", 90)], XE, 500)
    for i in range(3):
        for j, l in enumerate("ABCD"):
            E.foco(c, t, C["s14.b"] + i * 0.15 + j * 0.03, 0.4, lambda a, i=i, j=j, l=l: (
                c.drawCircle(1180 + j * 90, 300 + i * 110, 34, M.paint(TINTA, a, stroke=4)),
                centro(c, l, 1180 + j * 90, 300 + i * 110 + 13, 36, "b", TINTA, a)))
    E.frase(c, t, C["s14.b"], [("chuta", "g", 84), ("todas", "i", 90)], XE, 650)
    E.frase(c, t, C["s14.c"], [("acertar", "i", 96), ("exatamente", "i", 96), ("2?", "g", 96, COR)], XE, 860)
    E.relogio(c, t, C["s15.a"], 1560, 760, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.foco(c, t, C["s16.a"], 0.4, lambda a: E.escreve(c, "acertar:", XE, 260, 70, "i", COR, a))
    E.formula_em(c, t, C["s16.a"] + 0.4, "f{1}{4}", XE + 300, 260, 84, "g", COR)
    E.foco(c, t, C["s16.b"], 0.4, lambda a: E.escreve(c, "errar:", 800, 260, 70, "i", TINTA, a))
    E.formula_em(c, t, C["s16.b"] + 0.4, "f{3}{4}", 1030, 260, 84, "g", TINTA)
    binom_em(c, t, C["s16.c"], 3, 2, 1420, 210, 80, cor=COR)
    E.foco(c, t, C["s16.c"] + 0.3, 0.4, lambda a: E.escreve(c, "= 3", 1500, 260, 84, "g", COR, a))
    E.formula_em(c, t, C["s17.a"], "(f{1}{4})^2 = f{1}{16}", XE, 500, 90, "g", COR)
    E.formula_em(c, t, C["s17.b"], "f{3}{4}", 900, 500, 90, "g", TINTA)
    E.formula_em(c, t, C["s17.c"], "3 · f{1}{16} · f{3}{4} =", XE, 780, 96, "g", TINTA)
    bola_txt(c, t, C["s17.d"], "f{9}{64}", 1120, 750, 130, 100, CERTO)
    E.foco(c, t, C["s17.d"] + 1.0, 0.4, lambda a: E.escreve(c, "≈ 14%", 1300, 790, 96, "g", CERTO, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        for i, (k, s) in enumerate((("s18.a", "conte as ordens: binomial"), ("s18.b", "× a chance de uma ordem"))):
            y = 450 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 96)], 430, y)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s19.a"], [("Casa", "g", 140, COR), ("dos", "i", 130)], XE, 470)
    E.frase(c, t, C["s19.a"] + 0.3, [("pombos", "g", 140, COR)], XE, 620)
    E.frase(c, t, C["s19.b"], ps("13 pessoas, 12 meses", "i", 70), XE, 770)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ordem=b_ordem, ordens=b_ordens, regra=b_regra, dado=b_dado, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
