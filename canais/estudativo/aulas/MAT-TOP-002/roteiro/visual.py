"""Visual — Estudativo · MAT-TOP-002: binômio de Newton.
Mesma linguagem do módulo (MAT-TOP-001): binom() em pé, triângulo de Pascal em números soltos, resposta na esfera.
Cores desta aula: coeficiente (número do triângulo) em índigo; o primeiro termo (a, x) em tinta; o segundo termo (b, 2, 3) em
âmbar B2, porque é ele que "entra elevado" e muda os coeficientes. Erro em vermelho, certo em verde, atalho no palco.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
from math import comb
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-002_binomio_de_newton.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("padrao", "exemplo", "termo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
B2 = "#D98A00"      # o segundo termo do binômio
B2_ESC = "#FFB833"
TERMOS = [comb(4, k) * 2 ** k for k in range(5)]
assert TERMOS == [1, 8, 24, 32, 16] and sum(TERMOS) == 81 == 3 ** 4
assert comb(4, 2) * 2 ** 2 == 24 and comb(3, 1) == 3
assert comb(5, 2) * 3 ** 2 == 90 and sum(comb(5, k) * 3 ** k for k in range(6)) == 1024 == 4 ** 5


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


def conta(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """conta numa linha com partes coloridas: partes = [(escrita de fórmula, cor)]. Devolve a largura"""
    ws = [E.formula(None, s, 0, 0, size, est, a=0) for s, _ in partes]
    w = sum(ws)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    if a > 0:
        for (s, cor), wi in zip(partes, ws):
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += wi
    return w


def conta_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: conta(c, partes, x, y, size, a, align))


def pascal(c, t, tl, cx, y0, dx, dy, size, cor=None, passo=0.07):
    for n, tn in enumerate(tl):
        if tn is None:
            continue
        for k in range(n + 1):
            num(c, t, tn + k * passo, comb(n, k), cx + (k - n / 2) * dx, y0 + n * dy, size, cor(n, k) if cor else TINTA)


EXPANSAO = [("x^4", TINTA), (" + ", TINTA), ("8", COR), ("x^3", TINTA), (" + ", TINTA), ("24", COR), ("x^2", TINTA), (" + ", TINTA),
            ("32", COR), ("x", TINTA), (" + ", TINTA), ("16", COR)]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        E.formula_em(c, t, C["s01.a"], "(x + 2)^4", W / 2, 330, 170, "g", TINTA, "center")
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.formula(c, "(x + 2)(x + 2)(x + 2)(x + 2)", W / 2, 520, 84, "g", TINTA2, a, "center"))
        if t >= C["s01.c"]:
            E.risco(c, 420, 545, 1500, 455, t, C["s01.c"] - 0.2, largura=12)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "1    4    6    4    1", W / 2, 690, 70, "g", fundo=COR, a=a))
        conta_em(c, t, C["s01.d"], EXPANSAO, W / 2, 900, 96, "center")
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 560, 270 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("abrir", "g", 120, COR), ("qualquer", "i", 110)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.4, [("potência", "g", 120)], XE, 630)
        E.frase(c, t, C["s02.b"], [("e", "i", 110), ("achar", "i", 110), ("um", "i", 110), ("termo", "g", 120, COR)], XE, 790)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1300, 545, 80, "g", BR, a),
                                                      E.escreve(c, "de prova", 1320, 630, 80, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 84), XE, 200)
    E.frase(c, t, C["s03.a"], [("2", "g", 110, COR), ("coisas", "i", 100)], XE + 640, 200)
    x, w = XE, 1580
    for i, (k, h) in enumerate((("s03.b", 300), ("s03.c", 250))):
        y = 290 + i * 340
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("triângulo", "g", 66), ("de", "i", 66), ("Pascal", "g", 66, COR)], x + 50, 400)
    E.frase(c, t, C["s03.b"] + 0.6, ps("cada número é a soma dos dois de cima", "i", 54, TINTA2), x + 50, 490)
    pascal(c, t, [C["s03.b"] + 0.4 + 0.12 * i for i in range(4)], 1500, 345, 100, 64, 46)
    E.frase(c, t, C["s03.c"], [("o", "i", 66), ("cubo", "g", 66, COR), ("da", "i", 66), ("soma", "g", 66, COR)], x + 50, 730)
    conta_em(c, t, C["s03.c"] + 0.8, [("(x + 1)^3 = x^3 + ", TINTA), ("3", COR), ("x^2 + ", TINTA), ("3", COR), ("x + ", TINTA), ("1", COR)],
             x + 50, 840, 84)


# ---------------- o padrão ----------------
def b_padrao(c, t, C, b):
    def parte1():
        E.frase(c, t, C["s04"], [("binômio:", "i", 80), ("soma", "g", 76, COR), ("de", "i", 80), ("dois", "i", 80), ("termos", "i", 80)], XE, 200)
        conta_em(c, t, C["s04.a"], [("a", TINTA), (" + ", TINTA), ("b", B2)], 1340, 200, 90)
        E.foco(c, t, C["s04.b"], 0.5, lambda a: E.pilula(c, "coeficiente = o número da frente", 640, 330, 50, "b", fundo=COR, a=a))
        conta_em(c, t, C["s04.c"], [("(a + ", TINTA), ("b", B2), (")^2 = ", TINTA), ("1", COR), ("a^2 + ", TINTA), ("2", COR), ("a", TINTA), ("b", B2),
                                    (" + ", TINTA), ("1", COR), ("b^2", B2)], XE, 660, 84)
        conta_em(c, t, C["s04.d"], [("(a + ", TINTA), ("b", B2), (")^3 = ", TINTA), ("1", COR), ("a^3 + ", TINTA), ("3", COR), ("a^2", TINTA), ("b", B2),
                                    (" + ", TINTA), ("3", COR), ("a", TINTA), ("b^2", B2), (" + ", TINTA), ("1", COR), ("b^3", B2)], XE, 840, 84)

        def cor(n, k):
            return COR if n in (2, 3) and t >= C["s04.e"] else TINTA
        if t >= C["s04.e"] - 0.6:
            pascal(c, t, [C["s04.e"] - 0.6 + 0.1 * i for i in range(4)], 1640, 300, 110, 80, 56, cor)
            E.foco(c, t, C["s04.e"], 0.4, lambda a: (E.escreve(c, "linha 2", 1290, 476, 44, "i", COR, a),
                                                    E.escreve(c, "linha 3", 1290, 556, 44, "i", COR, a)))
    E.saida(c, t, C["s05"] - 0.1, parte1)
    if C["s05"] <= t < C["s06"]:
        def parte2():
            E.frase(c, t, C["s05"], ps("por que o triângulo aparece?", "i", 76), W / 2, 180, "center")
            xs = (560, 960, 1360)
            for i, x in enumerate(xs):
                conta_em(c, t, C["s05.a"] + i * 0.2, [("(a + ", TINTA), ("b", B2), (")", TINTA)], x, 340, 96, "center")
            E.frase(c, t, C["s05.b"], ps("uma letra de cada parêntese", "i", 58, TINTA2), W / 2, 450, "center")
            for j in range(3):  # o b sai do parêntese j
                y = 590 + j * 110
                for i, x in enumerate(xs):
                    letra, cor = ("b", B2) if i == j else ("a", TINTA)
                    num(c, t, C["s05.c"] + j * 0.5 + i * 0.08, letra, x, y, 80, cor)
            E.foco(c, t, C["s05.d"], 0.4, lambda a: E.escreve(c, "3 jeitos", 1560, 720, 64, "g", COR, a))
            binom_em(c, t, C["s05.e"], 3, 1, 1680, 860, 70, cor=COR)
            E.foco(c, t, C["s05.e"] + 0.3, 0.4, lambda a: E.escreve(c, "= 3", 1760, 900, 70, "g", COR, a))
        E.saida(c, t, C["s06"] - 0.1, parte2)
    if t >= C["s06"]:
        conta_em(c, t, C["s06"], [("(a + ", TINTA), ("b", B2), (")^n", TINTA)], XE, 210, 100)
        itens = (("s06.a", "coeficientes:", "linha n do triângulo", COR), ("s06.b", "expoente do a:", "começa em n e desce", TINTA),
                 ("s06.c", "expoente do b:", "começa em 0 e sobe", B2), ("s06.d", "em cada termo:", "os expoentes somam n", COR))
        for i, (k, l1, l2, cor) in enumerate(itens):
            y = 380 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a),
                                                         centro(c, str(i + 1), XE + 40, y - 6, 50, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "i", 66)], XE + 120, y)
            E.frase(c, t, C[k] + 0.4, [(l2, "g", 66, cor)], XE + 580, y)


# ---------------- exemplo ----------------
XS = [330 + i * 315 for i in range(5)]


def b_exemplo(c, t, C, b):
    E.formula_em(c, t, C["s07.a"], "(x + 2)^4", XE, 190, 110, "g", TINTA)
    E.foco(c, t, C["s07.b"], 0.5, lambda a: (conta(c, [("a = x", TINTA)], 760, 190, 70, a), conta(c, [("b = 2", B2)], 1060, 190, 70, a)))
    ks = ("s08.a", "s08.b", "s08.c", "s09.a", "s09.b")
    for k in range(5):
        x = XS[k]
        tk = C[ks[k]]
        # coeficiente
        E.foco(c, t, C["s07.c"] + k * 0.15, 0.45, lambda a, x=x, k=k: (E.bola(c, x, 340, 52, a=a), centro(c, str(comb(4, k)), x, 340 + 20, 56, "g", BR, a)))
        px = "x^" + str(4 - k) if 4 - k > 1 else ("x" if k == 3 else "")
        pb = "2^" + str(k) if k > 1 else ("2" if k == 1 else "")
        cima = [(px, TINTA)] + ([(" · ", TINTA2)] if px and pb else []) + ([(pb, B2)] if pb else [])
        E.foco(c, t, tk, 0.45, lambda a, x=x, cima=cima: conta(c, cima, x, 500, 70, a, "center"))
        val = comb(4, k) * 2 ** k
        res = [] if val == 1 else [(str(val), COR)]
        res += [(px, TINTA)] if px else []
        res = res or [("1", COR)]
        E.foco(c, t, tk + 0.6, 0.45, lambda a, x=x, k=k: M.arrow(c, x, 545, x, 615, FIO, a, 4, 14, a))
        E.foco(c, t, tk + 0.8, 0.45, lambda a, x=x, res=res: conta(c, res, x, 720, 84, a, "center"))
        if k < 4:
            E.foco(c, t, tk + 0.9, 0.4, lambda a, x=x: centro(c, "+", x + 157, 715, 70, "g", TINTA2, a))
    if t >= C["s09.c"]:
        p = ep(t, C["s09.c"], 0.5)
        E.caixa_pontilhada(c, 200, 625, 1520, 140, p, CERTO, prog_=p)
        E.frase(c, t, C["s09.c"] + 0.2, [("sem", "i", 70), ("multiplicar", "i", 70), ("nenhum", "i", 70), ("parêntese", "g", 64, CERTO)], W / 2, 920, "center")


# ---------------- termo geral ----------------
def b_termo(c, t, C, b):
    def parte1():
        E.frase(c, t, C["s10.a"], ps("só o coeficiente de", "i", 76), XE, 200)
        E.formula_em(c, t, C["s10.a"] + 0.8, "x^2?", XE + 690, 200, 90, "g", COR)
        E.frase(c, t, C["s10.b"], [("termo", "g", 90), ("geral", "g", 90, COR)], XE, 380)
        y = 560
        binom_em(c, t, C["s10.c"], "n", "k", 300, y - 40, 96, cor=COR)
        conta_em(c, t, C["s10.d"], [("· a^{n − k}", TINTA)], 410, y + 30, 100)
        conta_em(c, t, C["s10.e"], [("· ", TINTA), ("b^k", B2)], 780, y + 30, 100)
        E.foco(c, t, C["s10.f"], 0.5, lambda a: E.pilula(c, "k = quantas vezes o b foi escolhido", 960, 820, 54, "b", fundo=B2, a=a))
    E.saida(c, t, C["s11"] - 0.1, parte1)
    if t < C["s11"]:
        return
    E.formula_em(c, t, C["s11"], "(x + 2)^4", XE, 190, 100, "g", TINTA)
    E.frase(c, t, C["s11"] + 0.4, ps("quero", "i", 76) + [("x²", "g", 76, COR)], 760, 190)
    conta_em(c, t, C["s11.a"], [("4 − k = 2", TINTA)], XE, 380, 96)
    conta_em(c, t, C["s11.b"], [("k = 2", COR)], 760, 380, 96)
    y = 620
    binom_em(c, t, C["s11.c"], 4, 2, 260, y - 40, 96)
    E.foco(c, t, C["s11.c"] + 0.3, 0.4, lambda a: E.escreve(c, "= 6", 360, y + 30, 96, "g", COR, a))
    conta_em(c, t, C["s11.d"], [("2^2", B2), (" = 4", TINTA)], 700, y + 30, 96)
    conta_em(c, t, C["s11.e"], [("6 · 4 = 24", TINTA)], XE, 900, 100)
    bola_txt(c, t, C["s11.e"] + 0.6, "24x^2", 1450, 760, 190, 96)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], XE, 200)
    for k in range(5):
        num(c, t, C["s12.a"] + k * 0.1, comb(4, k), 1150 + k * 130, 200, 70, ERRADO if k == 2 and t >= C["s12.b"] else TINTA)
    E.foco(c, t, C["s12.a"], 0.4, lambda a: E.escreve(c, "linha 4", 860, 225, 46, "i", TINTA2, a))
    certo = t >= C["s12.c"]
    E.foco(c, t, C["s12.b"], 0.5, lambda a: conta(c, [("6x^2", ERRADO)], 500, 520, 150, a, "center"))
    if certo:
        E.risco(c, 330, 560, 680, 400, t, C["s12.c"], largura=16)
    conta_em(c, t, C["s12.c"], [("6 · ", COR), ("2^2", B2), (" · x^2", TINTA)], 1000, 470, 96)
    conta_em(c, t, C["s12.d"], [("= 24x^2", CERTO)], 1000, 620, 120)
    E.frase(c, t, C["s12.e"], [("o", "i", 74), ("b", "g", 70, B2), ("entra", "i", 74), ("elevado", "g", 70, COR)], W / 2, 880, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def parte1():
        E.frase(c, t, C["s13"], [("atalho:", "i", 80, CLARO), ("troque", "g", 76, BR), ("x", "g", 76, BR), ("por", "i", 80, CLARO), ("1", "g", 76, BR)], W / 2, 200, "center")
        E.formula_em(c, t, C["s13.b"] - 0.6, "(1 + 2)^4 = 3^4 = 81", W / 2, 420, 110, "g", BR, "center")
        E.formula_em(c, t, C["s13.c"], "1 + 8 + 24 + 32 + 16", W / 2, 640, 100, "g", CLARO, "center")
        E.foco(c, t, C["s13.d"], 0.5, lambda a: E.pilula(c, "= 81   bateu!", W / 2, 820, 76, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s14"] - 0.1, parte1)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("x = 1: sobra a", "i", 80, CLARO) + [("soma", "g", 76, BR), ("dos", "i", 80, CLARO)], W / 2, 270, "center")
    E.frase(c, t, C["s14.a"] + 1.0, [("coeficientes", "g", 76, BR)], W / 2, 380, "center")
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (E.escreve(c, "deu diferente?", 300, 600, 70, "i", CLARO, a),
                                            E.escreve(c, "tem erro", 820, 600, 76, "g", "#FF8A8E", a)))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: (E.escreve(c, "um coeficiente só?", 300, 800, 70, "i", CLARO, a),
                                            E.escreve(c, "termo geral", 960, 800, 76, "g", BR, a)))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.formula_em(c, t, C["s15.a"], "(x + 3)^5", XE, 420, 150, "g", TINTA)
    E.frase(c, t, C["s15.b"], ps("coeficiente de", "i", 76), XE, 620)
    E.formula_em(c, t, C["s15.b"] + 0.6, "x^3 = ?", XE + 520, 620, 90, "g", COR)
    E.frase(c, t, C["s15.c"], ps("soma dos coeficientes = ?", "i", 76), XE, 800)
    E.relogio(c, t, C["s16.a"], 1500, 460, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s17"], "(x + 3)^5", XE, 190, 100, "g", TINTA)
    conta_em(c, t, C["s17.a"], [("5 − k = 3", TINTA)], XE, 370, 90)
    conta_em(c, t, C["s17.b"], [("k = 2", COR)], 700, 370, 90)
    y = 580
    binom_em(c, t, C["s17.c"], 5, 2, 250, y - 40, 90)
    E.foco(c, t, C["s17.c"] + 0.3, 0.4, lambda a: E.escreve(c, "= 10", 350, y + 30, 90, "g", COR, a))
    conta_em(c, t, C["s17.d"], [("3^2", B2), (" = 9", TINTA)], 700, y + 30, 90)
    conta_em(c, t, C["s17.e"], [("10 · 9 = 90", TINTA)], XE, 790, 90)
    bola_txt(c, t, C["s17.f"], "90x^3", 1450, 450, 180, 90, CERTO)
    E.foco(c, t, C["s18"], 0.4, lambda a: E.escreve(c, "soma:", XE, 960, 70, "i", TINTA2, a))
    conta_em(c, t, C["s18.a"], [("(1 + 3)^5 = 4^5", TINTA)], XE + 200, 960, 80)
    conta_em(c, t, C["s18.b"], [("= 1024", CERTO)], XE + 820, 960, 90)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        for i, (k, s) in enumerate((("s19.a", "coeficientes do triângulo"), ("s19.b", "expoentes de um em um"), ("s19.c", "o b entra elevado"))):
            y = 400 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 380, y - 30, 56, a=a), centro(c, str(i + 1), 380, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 92)], 480, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s20.a"], [("Distribuição", "g", 130, COR)], XE, 470)
    E.frase(c, t, C["s20.a"] + 0.3, [("binomial", "g", 130, COR)], XE, 610)
    E.frase(c, t, C["s20.b"], ps("2 caras em 5 lançamentos", "i", 70), XE, 760)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, padrao=b_padrao, exemplo=b_exemplo, termo=b_termo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
