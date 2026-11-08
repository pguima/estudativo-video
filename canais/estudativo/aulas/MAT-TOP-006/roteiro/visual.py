"""Visual — Estudativo · MAT-TOP-006: praticando binômio, binomial e contagem.
Mesma linguagem do módulo (MAT-TOP-001 a 005): binom() em pé, triângulo de Pascal em números soltos, b do binômio em âmbar,
pior caso em grade de casinhas, múltiplos em grade de números (múltiplo de 2 cheio, de 3 com anel âmbar).
Situação 5: bolinhas (bolas de sorvete) na cor da matéria e barras em tinta, numa fila de 6 lugares.
Cada situação: enunciado à esquerda, relógio de pausa à direita; resposta em tela própria, com o resultado na esfera.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
from math import comb
from itertools import combinations_with_replacement
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-006_praticando_binomio_e_contagem.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
AMB = "#D98A00"
assert comb(5, 4) * 2 ** 4 == 80 and comb(5, 4) == 5
assert [comb(4, k) for k in range(5)] == [1, 4, 6, 4, 1] and 2 ** 4 == 16 and 6 * 2 == 16 * 3 // 4 and 3 / 8 == 0.375
assert 12 * 3 + 1 == 37 and 12 * 4 == 48
um = lambda n, ks: sum(1 for i in range(1, n + 1) if any(i % k == 0 for k in ks))
assert 120 // 2 == 60 and 120 // 3 == 40 and 120 // 6 == 20 and 60 + 40 - 20 == 80 == um(120, (2, 3)) and 120 - 80 == 40 == (120 // 6) * 2
assert comb(6, 2) == 15 == len(list(combinations_with_replacement(range(5), 2))) and comb(5, 2) + 5 == 15


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças do módulo ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def num(c, t, t0, s, x, y, size, cor=TINTA, est="g"):
    E.foco(c, t, t0, 0.45, lambda a: centro(c, str(s), x, y + size * 0.36, size, est, cor, a))


def binom(c, n, p, cx, cy, size, cor=None, a=1.0):
    cor = cor or TINTA
    n, p = str(n), str(p)
    w = max(E.larg(n, "g", size), E.larg(p, "g", size))
    if a <= 0:
        return
    centro(c, n, cx, cy - size * 0.1, size, "g", cor, a)
    centro(c, p, cx, cy + size * 0.82, size, "g", cor, a)
    h, k = size * 0.98, size * 0.24
    for lado in (-1, 1):
        x0 = cx + lado * (w / 2 + size * 0.22)
        path = skia.Path()
        path.moveTo(x0, cy - h)
        path.quadTo(x0 + lado * k * 1.6, cy, x0, cy + h)
        c.drawPath(path, M.paint(cor, a, stroke=max(4, size * 0.075), cap_round=True))


def binom_em(c, t, t0, n, p, cx, cy, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: binom(c, n, p, cx, cy, size, cor, a))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, str(s), cx, cy + size * 0.36, size, "g", BR, a, "center")))


def txt_em(c, t, t0, s, x, y, size, cor=TINTA, est="g", align="left"):
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, s, x, y, size, est, cor, a, align))


def enunciado(c, t, C, k, n, linhas, relogio):
    """tela da questão: 'situação n' + linhas [(cue, partes, y)] + relógio"""
    E.frase(c, t, C[k], [("situação", "i", 72, COR), (str(n), "g", 72, COR)], XE, 200)
    for cue, partes, y in linhas:
        E.frase(c, t, C[cue], partes, XE, y)
    E.relogio(c, t, C[relogio], 1500, 460, 190)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 140, COR), ("situações", "g", 130)], XE, 330)
    temas = ("binômio", "chance", "pombos", "conjuntos", "repetição")
    for i, s in enumerate(temas):
        x, y = XE + (i % 3) * 540, 520 + (i // 3) * 150
        E.foco(c, t, C["s01.b"] + i * 0.4, 0.4, lambda a, s=s, x=x, y=y, i=i: (E.bola(c, x + 40, y - 24, 40, a=a),
                                                                               centro(c, str(i + 1), x + 40, y - 6, 46, "g", BR, a),
                                                                               E.escreve(c, s, x + 100, y, 66, "g", TINTA, a)))
    E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "pause e resolva antes da resposta", W / 2, 920, 60, "g", fundo=COR, a=a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 80), XE, 170)
    E.frase(c, t, C["s02.a"], [("5", "g", 100, COR), ("ferramentas", "i", 90)], XE + 600, 170)
    itens = (("s02.b", "binômio:", "termo geral"), ("s02.c", "chance:", "binomial × uma ordem"), ("s02.d", "pombos:", "pior caso + 1"),
             ("s02.e", "conjuntos:", "some e tire o repetido"), ("s02.f", "repetição:", "bolinhas e barras"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 320 + i * 150
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 24, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 50, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 64)], XE + 120, y)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 64, COR)], XE + 520, y)


# ---------------- situação 1: binômio ----------------
def b_questao1(c, t, C, b):
    enunciado(c, t, C, "s03.a", 1, [("s03.b", [("(x", "g", 120), ("+", "g", 120), ("2)⁵", "g", 120, AMB)], 450),
                                   ("s03.c", ps("coeficiente de x?", "i", 90), 680)], "s04.a")


def b_resposta1(c, t, C, b):
    E.formula_em(c, t, C["s05"], "(x + 2)^5", XE, 190, 100, "g", TINTA)
    txt_em(c, t, C["s05.a"], "expoente do x: 5 − k", XE, 360, 76)
    txt_em(c, t, C["s05.b"], "= 1  →  k = 4", XE + 760, 360, 76, COR)
    y = 560
    binom_em(c, t, C["s05.c"], 5, 4, 250, y - 40, 90)
    E.foco(c, t, C["s05.c"] + 0.3, 0.4, lambda a: E.escreve(c, "= 5", 350, y + 30, 90, "g", COR, a))
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.formula(c, "2^4 = 16", 700, y + 30, 90, "g", AMB, a))
    txt_em(c, t, C["s05.e"], "5 · 16 = 80", XE, 780, 100)
    bola_txt(c, t, C["s05.e"] + 0.5, "80", 1450, 720, 120, 120, CERTO)
    E.foco(c, t, C["s05.f"], 0.4, lambda a: E.escreve(c, "só o 5 do triângulo? faltou o 2 elevado a 4", XE, 950, 56, "i", ERRADO, a))


# ---------------- situação 2: distribuição binomial ----------------
def b_questao2(c, t, C, b):
    enunciado(c, t, C, "s06.a", 2, [("s06.b", [("4", "g", 100, COR), ("filhos", "i", 100)], 420),
                                   ("s06.b", ps("menina: chance 1/2", "i", 70, TINTA2), 540),
                                   ("s06.c", [("exatamente", "i", 90), ("2", "g", 90, COR), ("meninas?", "g", 90, COR)], 720)], "s07.a")


def b_resposta2(c, t, C, b):
    xs = [380 + k * 260 for k in range(5)]
    for k in range(5):
        on = k == 2 and t >= C["s08.c"]
        num(c, t, C["s08.a"] + k * 0.12, comb(4, k), xs[k], 260, 100, COR if on else TINTA)
        E.foco(c, t, C["s08.b"], 0.4, lambda a, k=k: (M.line(c, xs[k] - 70, 340, xs[k] + 70, 340, TINTA, a, 5),
                                                     centro(c, "16", xs[k], 440, 76, "g", TINTA2, a)))
        E.foco(c, t, C["s08.a"] + 0.8, 0.4, lambda a, k=k: centro(c, f"{k} menina" + ("s" if k != 1 else ""), xs[k], 540, 38, "i", TINTA2, a))
    if t >= C["s08.c"]:
        q = ep(t, C["s08.c"], 0.4)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xs[2] - 100, 170, 200, 400), 26, 26), M.paint(CERTO, q, stroke=6))
    E.formula_em(c, t, C["s08.d"], "f{6}{16} = f{3}{8}", XE, 760, 100, "g", TINTA)
    bola_txt(c, t, C["s08.d"] + 0.4, "37,5%", 1100, 730, 130, 76, CERTO)
    E.foco(c, t, C["s09.a"], 0.4, lambda a: E.escreve(c, "6 é o maior da linha", XE, 950, 56, "i", TINTA, a))
    E.foco(c, t, C["s09.b"], 0.4, lambda a: E.escreve(c, "não chega à metade:", XE + 640, 950, 56, "g", ERRADO, a))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.formula(c, "as outras: f{10}{16}", XE + 1180, 960, 60, "g", TINTA, a))


# ---------------- situação 3: casa dos pombos ----------------
def b_questao3(c, t, C, b):
    enunciado(c, t, C, "s10.a", 3, [("s10.b", [("12", "g", 110, COR), ("signos", "i", 100)], 430),
                                   ("s10.c", [("garantir", "i", 86), ("4", "g", 86, COR), ("no", "i", 86), ("mesmo", "i", 86), ("signo?", "i", 86)], 680)], "s11.a")


def b_resposta3(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("12", "g", 64, COR), ("casinhas", "i", 66)], XE, 180)
    for i in range(12):
        x, y = 175 + (i % 6) * 270, 230 + (i // 6) * 190
        q = ep(t, C["s12.a"] + i * 0.04, 0.4)
        on = i == 5 and t >= C["s12.d"]
        M.rrect(c, x, y, 240, 160, 18, COR if on else BR, q * (0.14 if on else 0.9))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 240, 160), 18, 18), M.paint(COR if on else FIO, q, stroke=4))
        for k in range(3):
            s = ease_back(prog(t, C["s12.b"] + k * 0.5 + i * 0.03, 0.4))
            if s > 0:
                c.drawCircle(x + 50 + k * 50, y + 80, 18 * s, M.paint(TINTA))
        if i == 5:
            s = ease_back(prog(t, C["s12.d"], 0.4))
            if s > 0:
                c.drawCircle(x + 200, y + 80, 18 * s, M.paint(COR))
    txt_em(c, t, C["s12.c"], "12 · 3 = 36", XE, 700, 90)
    E.foco(c, t, C["s12.c"] + 0.5, 0.4, lambda a: E.escreve(c, "nenhum quarteto", XE + 560, 700, 56, "i", TINTA2, a))
    txt_em(c, t, C["s12.d"], "36 + 1 =", XE, 860, 100, COR)
    bola_txt(c, t, C["s12.d"] + 0.4, "37", 720, 830, 95, 110, CERTO)
    E.foco(c, t, C["s12.e"], 0.4, lambda a: E.escreve(c, "12 · 4 = 48 garante, mas não é o mínimo", 960, 860, 50, "i", ERRADO, a))


# ---------------- situação 4: inclusão-exclusão ----------------
def b_questao4(c, t, C, b):
    enunciado(c, t, C, "s13.a", 4, [("s13.a", [("de", "i", 90), ("1", "g", 90, COR), ("a", "i", 90), ("120", "g", 90, COR)], 430),
                                   ("s13.b", [("nem", "i", 86), ("múltiplo", "i", 86), ("de", "i", 86), ("2", "g", 86), ("nem", "i", 86),
                                              ("de", "i", 86), ("3?", "g", 86)], 650)], "s14.a")


def b_resposta4(c, t, C, b):
    txt_em(c, t, C["s15.a"], "120 ÷ 2 = 60", XE, 230, 76)
    txt_em(c, t, C["s15.b"], "120 ÷ 3 = 40", XE + 620, 230, 76, AMB)
    txt_em(c, t, C["s15.c"], "120 ÷ 6 = 20", XE + 1240, 230, 76, ERRADO)
    txt_em(c, t, C["s15.d"], "60 + 40 − 20 = 80", XE, 400, 90)
    E.foco(c, t, C["s15.d"] + 0.5, 0.4, lambda a: E.escreve(c, "múltiplos de 2 ou de 3", XE + 900, 400, 52, "i", TINTA2, a))
    E.frase(c, t, C["s16.a"], [("nenhum", "g", 70, COR), ("dos", "i", 72), ("dois:", "i", 72)], XE, 560)
    txt_em(c, t, C["s16.b"], "120 − 80 =", XE, 700, 100)
    bola_txt(c, t, C["s16.b"] + 0.4, "40", 820, 665, 95, 110, CERTO)
    for i in range(1, 7):
        x = 1080 + (i - 1) * 120
        livre = i in (1, 5)
        E.foco(c, t, C["s16.c"] + i * 0.06, 0.4, lambda a, x=x, i=i, livre=livre: (
            M.rrect(c, x, 600, 100, 100, 16, CERTO if livre else BR, a), c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, 600, 100, 100), 16, 16),
                                                                                    M.paint(FIO, a, stroke=3)),
            centro(c, str(i), x + 50, 668, 52, "g", BR if livre else TINTA, a)))
    E.foco(c, t, C["s16.d"], 0.4, lambda a: E.escreve(c, "20 blocos · 2 = 40", 1080, 840, 70, "g", CERTO, a))


# ---------------- situação 5: combinação com repetição ----------------
SABORES = ("#C2463A", "#E8A33C", "#55895A", "#8E5BD9", "#5B8DB8")


def b_questao5(c, t, C, b):
    enunciado(c, t, C, "s17.a", 5, [("s17.b", [("5", "g", 100, COR), ("sabores", "i", 100)], 400),
                                   ("s17.c", ps("2 bolas, pode repetir", "i", 76), 560),
                                   ("s17.c", ps("a ordem não importa", "i", 64, TINTA2), 660),
                                   ("s17.d", [("quantas", "i", 90), ("casquinhas?", "g", 90, COR)], 840)], "s18.a")
    for i, cor in enumerate(SABORES):
        E.foco(c, t, C["s17.b"] + 0.1 * i, 0.4, lambda a, i=i, cor=cor: c.drawCircle(860 + i * 80, 370, 30, M.paint(cor, a)))


def b_resposta5(c, t, C, b):
    E.frase(c, t, C["s19.a"], [("combinação", "g", 70, COR), ("com", "i", 72), ("repetição", "g", 70, COR)], XE, 190)
    # fila de 6 lugares: um exemplo, bolinhas no 2º e no 5º lugar (sabores 2 e 4)
    xs = [420 + i * 190 for i in range(6)]
    y = 420
    bol = (1, 4)
    for i, x in enumerate(xs):
        if i in bol:
            E.foco(c, t, C["s19.b"] + 0.3 * bol.index(i), 0.4, lambda a, x=x: c.drawCircle(x, y, 50, M.paint(COR, a)))
        else:
            E.foco(c, t, C["s19.c"] + 0.15 * i, 0.4, lambda a, x=x: M.line(c, x, y - 70, x, y + 70, TINTA, a, 12))
    E.foco(c, t, C["s19.c"] + 0.8, 0.4, lambda a: E.escreve(c, "barras dividem os 5 sabores", 420, y + 170, 48, "i", TINTA2, a))
    E.foco(c, t, C["s19.d"], 0.4, lambda a: E.escreve(c, "6 lugares, escolha 2", XE, 760, 70, "g", TINTA, a))
    binom_em(c, t, C["s19.e"], 6, 2, 1000, 720, 84, COR)
    E.foco(c, t, C["s19.e"] + 0.3, 0.4, lambda a: E.escreve(c, "= 15", 1100, 790, 90, "g", COR, a))
    E.foco(c, t, C["s20.a"], 0.4, lambda a: E.formula(c, "diferentes: 10", XE, 940, 60, "g", TINTA, a))
    E.foco(c, t, C["s20.b"], 0.4, lambda a: E.formula(c, "iguais: 5", XE + 520, 940, 60, "g", TINTA, a))
    bola_txt(c, t, C["s20.c"], "15", 1550, 760, 110, 120, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        for i, (k, s) in enumerate((("s21.a", "binomial: escolhas, binômios, chances"), ("s21.b", "pior caso: garante repetições"),
                                    ("s21.c", "tire o repetido: sem contar 2 vezes"))):
            y = 400 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a), centro(c, str(i + 1), 260, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 74)], 360, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s22.a"], [("Distância", "g", 130, COR)], XE, 470)
    E.frase(c, t, C["s22.a"] + 0.3, [("de", "i", 120), ("ponto", "g", 130), ("a", "i", 120), ("reta", "g", 130, COR)], XE, 620)
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s22.b"] + 0.2, 0.4))
    E.frase(c, t, C["s22.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5,
              resposta5=b_resposta5, fim=b_fim)
