"""Visual — Estudativo · MAT-EQU-010: equação com frações ou decimais.
Peças locais: pedacos() mostra seis metades (ou seis terços) de caixa se juntando em caixas inteiras; termo_a_termo() põe cada termo
da equação numa coluna fixa, para o resultado de cada multiplicação nascer embaixo do termo. Todo instante vem de C[...]."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia
from fractions import Fraction as Fr

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-010_equacao_com_fracoes_e_decimais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("fracoes", "decimais", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert Fr(6, 2) + Fr(6, 3) == 5 and 6 * 5 == 30 and 30 / 5 == 6
assert 5 * 3.6 + 12 == 30 and abs(0.5 * 3.6 - 1.8) < 1e-9 and abs(1.8 + 1.2 - 3) < 1e-9 and abs(1.8 * 2 - 3.6) < 1e-9
assert Fr(1, 2) + Fr(1, 3) == Fr(5, 6) and 3 * 1 + 2 * 1 == 5
assert Fr(12, 4) + 1 == Fr(12, 6) + 2 == 4 and 3 * 12 + 12 == 2 * 12 + 24


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


def eq_f(c, t, partes, cx, y, size):
    """equação em partes [(fórmula, cor, t0)], centrada; devolve os x e as larguras"""
    ws = [E.formula(c, s, 0, 0, size, a=0) for s, _, _ in partes]
    gap = size * 0.26
    x = cx - (sum(ws) + gap * (len(ws) - 1)) / 2
    xs = []
    for (s, cor, t0), w in zip(partes, ws):
        xs.append(x)
        E.formula_em(c, t, t0, s, x, y, size, "g", cor)
        x += w + gap
    return xs, ws


def bola_res(c, t, t0, s, cx, cy, r=140, size=84):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, a=a), E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def realce(c, t, t0, x, y, w, size, cor=None, alto=1.15):
    """fundo leve atrás de um trecho já escrito"""
    q = ep(t, t0, 0.3)
    if q > 0:
        M.rrect(c, x - size * 0.12, y - size * 0.9, w + size * 0.24, size * alto, size * 0.18, cor or E.COR, 0.14 * q)


def operacao(c, t, t0, op, y, x=300, escuro=False):
    """pílula da conta feita nos dois lados, à esquerda da linha"""
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, op, x, y - 36, 60, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, t0 + 0.3, ps("nos dois lados", "i", 46, CLARO if escuro else TINTA2), x, y + 50, "center", 0.06)


SP = 84  # lado da caixa inteira


def pedacos(c, x0, y, k, p, a=1.0):
    """seis pedaços de 1/k de caixa; com p = 1 eles se juntam em 6/k caixas inteiras com x. (x0, y) = canto de baixo à esquerda"""
    if a <= 0:
        return
    w = SP / k
    for i in range(6):
        g, j = divmod(i, k)
        xi = lerp(x0 + i * (w + 14), x0 + g * (SP + 24) + j * w, ease_io(p))
        c.drawRect(skia.Rect.MakeXYWH(xi, y - SP, w, SP), M.paint(E.COR, a))
        if p < 1:
            c.drawRect(skia.Rect.MakeXYWH(xi, y - SP, w, SP), M.paint(BR, a * (1 - p), stroke=3))
    if p > 0.6:
        for g in range(6 // k):
            centro(c, "x", x0 + g * (SP + 24) + SP / 2, y - 24, 60, "g", BR, a * ep(p, 0.6, 0.4))


def colunas(c, t, termos, xs, y, size):
    """termos [(fórmula, cor, t0)] centrados nas colunas xs"""
    for (s, cor, t0), x in zip(termos, xs):
        fcen(c, t, t0, s, x, y, size, cor)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb = C["s01.a"], C["s01.b"]

    def um():
        eq_f(c, t, [("f{x}{2}", TINTA, ka), ("+", TINTA, ka + 1.6), ("f{x}{3}", TINTA, ka + 2.1), ("=", TINTA, ka + 2.9), ("5", TINTA, ka + 3.5)], W / 2, 430, 190)
        E.frase(c, t, ka + 4.4, ps("fração dentro de equação", "i", 80) + [("assusta", "g", 80, ERRADO)], W / 2, 700, "center", 0.12)
        E.frase(c, t, kb, ps("as frações", "i", 84) + [("somem", "g", 90, COR)] + ps("num passo só", "i", 84), W / 2, 880, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.2), [("resolver", "g", 110, COR)] + ps("equações", "i", 100), XE, 470, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), ps("com", "i", 90) + [("frações", "g", 96, COR)], XE, 600, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.7), ps("e com", "i", 90) + [("vírgula", "g", 96, COR)], XE, 730, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "achar", "o MMC"), ("s03.c", "andar com a vírgula", "ao multiplicar por 10"), ("s03.d", "resolver equação", "com x dos dois lados"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    alvo = [C[k] for k, _, _ in itens]
    q1, q2 = ease_io(prog(t, alvo[1] - 0.35, 0.5)), ease_io(prog(t, alvo[2] - 0.35, 0.5))
    py = lerp(lerp(340, 580, q1), 820, q2)
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1000, "left", 0.12)


# ---------------- frações ----------------
def b_fracoes(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]

    def ideia():
        fcen(c, t, C["s04"] + 0.2, "f{x}{2} + f{x}{3} = 5", W / 2, 230, 120)
        fcen(c, t, a4, "f{x}{2} = x ÷ 2", W / 2, 440, 96, TINTA2)
        E.frase(c, t, b4, ps("multiplique", "i", 70) + [("cada lado", "g", 70, COR)] + ps("por um número", "i", 70), W / 2, 590, "center", 0.1)
        E.frase(c, t, lerp(b4, c4, 0.5), ps("que", "i", 70) + [("todos os denominadores", "g", 70, COR)] + ps("dividem", "i", 70), W / 2, 680, "center", 0.1)
        E.frase(c, t, c4, ps("o melhor é", "i", 80) + [("o MMC", "g", 84, COR)], W / 2, 820, "center", 0.12)
        E.foco(c, t, d4 - 1.6, 0.5, lambda a: E.pilula(c, "MMC de 2 e 3 = 6", W / 2, 950, 64, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s05"] - 0.1, ideia)

    a5, b5, c5, d5, e5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]
    if C["s05"] - 0.1 <= t:
        def balanca():
            ent = ep(t, C["s05"], 0.6)
            if t < e5:
                E.saida(c, t, e5 - 0.4, lambda: E.balanca(c, 560, 610, lambda c_, x, y: E.formula(c_, "f{x}{2} + f{x}{3}", x, y - 40, 80, "g", TINTA, ent, "center"), "5", 0, ent, size=80, larg_braco=600))
            E.foco(c, t, e5 - 0.3, 0.5, lambda a: E.balanca(c, 560, 610, "3x + 2x", "30", 0, a, size=80, larg_braco=600), blur=8)
            for x in (260, 860):
                E.foco(c, t, a5, 0.5, lambda a, x=x: E.pilula(c, "× 6", x, 830, 60, "g", a=a, cor=E.SOBRE))
            E.frase(c, t, a5 + 0.4, ps("6 cópias de cada prato", "i", 56, TINTA2), 560, 960, "center", 0.08)
            x0 = 1130
            E.frase(c, t, b5, ps("6 metades de x", "i", 56), x0, 230, "left", 0.08)
            E.foco(c, t, b5, 0.5, lambda a: pedacos(c, x0, 360, 2, ep(t, b5 + 0.9, 0.8), a))
            fcen(c, t, b5 + 1.6, "= 3x", 1640, 350, 90, COR)
            E.frase(c, t, c5, ps("6 terços de x", "i", 56), x0, 470, "left", 0.08)
            E.foco(c, t, c5, 0.5, lambda a: pedacos(c, x0, 600, 3, ep(t, c5 + 0.9, 0.8), a))
            fcen(c, t, c5 + 1.6, "= 2x", 1640, 590, 90, COR)
            fcen(c, t, d5, "6 × 5 = 30", 1430, 760, 96)
            E.frase(c, t, e5, ps("cresceram", "i", 62) + [("o mesmo tanto", "g", 62, COR)], 1430, 900, "center", 0.1)
        E.saida(c, t, C["s06"] - 0.1, balanca)

    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    if C["s06"] - 0.1 <= t:
        def frase_fr():
            E.frase(c, t, C["s06"] + 0.3, ps("sem desenhar:", "i", 70, TINTA2), W / 2, 170, "center", 0.1)
            E.frase(c, t, a6, [("divide pelo de baixo,", "g", 76, COR)] + ps("multiplica pelo de cima", "g", 76), W / 2, 290, "center", 0.12)
            for y, k, d, r, t1 in ((520, b6, 2, 3, lerp(b6, c6, 0.5)), (800, c6, 3, 2, lerp(c6, C["s06.end"], 0.5))):
                fcen(c, t, k - 0.3, f"6 × f{{x}}{{{d}}}", 380, y, 110)
                E.ponte(c, t, k, 560, 760, y - 30, f"6 ÷ {d} = {r}", None, 50)
                fcen(c, t, t1, f"{r} × x", 1110, y, 110)
                fcen(c, t, t1 + 0.8, f"= {r}x", 1450, y, 110, COR)
        E.saida(c, t, C["s07"] - 0.1, frase_fr)

    if t >= C["s07"]:
        a7, b7, c7, d7, e7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"]
        cx = 760
        fcen(c, t, a7, "3x + 2x = 30", cx, 230, 120)
        E.frase(c, t, lerp(a7, b7, 0.6), ps("sem nenhuma fração", "i", 60, CERTO), cx, 330, "center", 0.1)
        fcen(c, t, b7, "5x = 30", cx, 470, 110)
        E.frase(c, t, c7, [("÷ 5", "g", 54, TINTA2)] + ps("nos dois lados", "i", 56, TINTA2), cx, 570, "center", 0.08)
        bola_res(c, t, lerp(c7, d7, 0.4), "x = 6", 1560, 380, 150, 90)
        fcen(c, t, d7, "f{6}{2} + f{6}{3}", cx - 120, 790, 100)
        fcen(c, t, lerp(d7, e7, 0.6), "= 3 + 2", cx + 330, 790, 100)
        fcen(c, t, e7, "= 5", 1440, 790, 110, CERTO)
        E.foco(c, t, e7 + 1.7, 0.5, lambda a: E.selo(c, 1620, 760, 50, True, a))


# ---------------- decimais ----------------
def b_decimais(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]

    def dez():
        E.frase(c, t, C["s08"] + 0.3, ps("com vírgula,", "i", 76) + [("a mesma ideia", "g", 76, COR)], W / 2, 170, "center", 0.12)
        fcen(c, t, a8, "0,5x + 1,2 = 3", W / 2, 330, 130)

        def explica():
            E.foco(c, t, b8, 0.5, lambda a: E.pilula(c, "× 10 em tudo", W / 2, 500, 72, "g", a=a, cor=E.SOBRE))
            E.frase(c, t, c8, ps("no máximo", "i", 66) + [("1 casa", "g", 66, COR)] + ps("depois da vírgula", "i", 66), W / 2, 680, "center", 0.1)
            E.frase(c, t, lerp(c8, C["s08.end"], 0.4), [("2 casas:", "g", 60, TINTA2)] + ps("seria por 100", "i", 60, TINTA2), W / 2, 800, "center", 0.1)
        E.saida(c, t, C["s09"] - 0.1, explica)
        xs = (520, 960, 1400)
        for (s0, s1, k), x in zip((("0,5x", "5x", a9), ("1,2", "12", b9), ("3", "30", c9)), xs):
            if t >= C["s09"]:
                fcen(c, t, k - 0.2, s0, x, 520, 100, TINTA2)
                if t >= k:
                    M.arrow(c, x, 560, x, 660, COR, ep(t, k, 0.4), 6, 18, ep(t, k, 0.4))
                E.foco(c, t, k + 0.1, 0.4, lambda a, x=x: E.pilula(c, "× 10", x + 110, 610, 44, "g", a=a, cor=E.SOBRE))
                fcen(c, t, k + 0.5, s1, x, 760, 110, COR)
        fcen(c, t, d9, "5x + 12 = 30", W / 2, 950, 120)
    E.saida(c, t, C["s10"] - 0.1, dez)

    if t >= C["s10"]:
        a0, b0, c0, d0 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
        cx = 820
        fcen(c, t, C["s10"] + 0.1, "5x + 12 = 30", cx, 190, 110)
        operacao(c, t, a0, "− 12", 360)
        fcen(c, t, a0 + 2.2, "5x = 18", cx + 80, 360, 110)
        operacao(c, t, b0, "÷ 5", 540)
        fcen(c, t, b0 + 1.2, "x = 3,6", cx + 80, 540, 110, COR)
        bola_res(c, t, b0 + 2.0, "x = 3,6", 1590, 450, 150, 76)
        E.frase(c, t, c0 - 1.0, [("conferindo", "i", 64, COR)], W / 2, 700, "center")
        fcen(c, t, c0, "0,5 × 3,6 = 1,8", W / 2, 820, 100)
        fcen(c, t, d0, "1,8 + 1,2 = 3", W / 2 - 40, 960, 100, CERTO)
        E.foco(c, t, d0 + 2.0, 0.5, lambda a: E.selo(c, W / 2 + 330, 925, 48, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    tf = lerp(b1, c1, 0.6)  # "esquecendo de multiplicar o cinco"

    def um():
        E.frase(c, t, a1 - 0.4, ps("o erro:", "i", 80) + [("multiplicar só as frações", "g", 80, ERRADO)], W / 2, 170, "center", 0.11)
        fcen(c, t, lerp(a1, b1, 0.5), "f{x}{2} + f{x}{3} = 5", W / 2, 360, 110)
        xs, ws = eq_f(c, t, [("3x + 2x", TINTA, b1), ("=", TINTA, b1 + 0.8), ("5", ERRADO, b1 + 1.2)], W / 2, 590, 120)
        if t >= tf:
            realce(c, t, tf, xs[2], 590, ws[2], 120, ERRADO)
        E.frase(c, t, tf + 0.2, ps("o 5 ficou sem", "i", 60, ERRADO) + [("× 6", "g", 60, ERRADO)], xs[2] + ws[2] / 2, 700, "center", 0.08)
        fcen(c, t, c1, "x = 1", W / 2, 880, 140, ERRADO)
    E.saida(c, t, C["s12"] - 0.1, um)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"] + 0.2, [("conferindo", "i", 76, COR)] + ps("com x = 1", "i", 76), W / 2, 170, "center", 0.1)
    xs, ws = eq_f(c, t, [("f{1}{2} + f{1}{3}", TINTA, a2), ("=", TINTA, a2 + 1.2), ("f{5}{6}", TINTA, a2 + 1.6), ("≠ 5", ERRADO, b2)], W / 2 - 60, 360, 110)
    E.foco(c, t, b2 + 0.3, 0.5, lambda a: E.selo(c, xs[3] + ws[3] + 90, 330, 48, False, a))
    tp = lerp(b2, c2, 0.45)
    xs, ws = eq_f(c, t, [("f{x}{2}", TINTA, tp - 0.4), ("+", TINTA, tp - 0.4), ("f{x}{3}", TINTA, tp - 0.4), ("=", TINTA, tp - 0.4), ("5", TINTA, tp - 0.4)], W / 2, 680, 110)
    for i, k in ((0, tp), (2, tp + 0.2), (4, c2 + 0.6)):
        E.foco(c, t, k, 0.4, lambda a, i=i: E.pilula(c, "× 6", xs[i] + ws[i] / 2, 520, 50, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, c2, [("cada termo,", "g", 76, COR)] + ps("até o número sem fração", "i", 76), W / 2, 910, "center", 0.11)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    t_sub, t_div = lerp(a3, b3, 0.6), lerp(b3, c3, 0.5)  # "subtraia um vírgula dois" / "divida por zero vírgula cinco"

    def um():
        E.frase(c, t, C["s13"] + 0.3, ps("agora, o atalho da vírgula", "i", 70, CLARO), W / 2, 160, "center", 0.1)
        E.frase(c, t, a3, ps("dividir por", "i", 96, CLARO) + [("0,5", "g", 100, BR)] + ps("é", "i", 96, CLARO) + [("dobrar", "g", 100, BR)], W / 2, 300, "center", 0.12)
        cx = 960
        fcen(c, t, t_sub - 0.8, "0,5x + 1,2 = 3", cx, 470, 100, CLARO)
        operacao(c, t, t_sub, "− 1,2", 620, 330, escuro=True)
        fcen(c, t, b3, "0,5x = 1,8", cx, 620, 100, BR)
        operacao(c, t, t_div, "÷ 0,5", 800, 330, escuro=True)
        fcen(c, t, c3 - 0.4, "x = 1,8 × 2", cx - 60, 800, 100, BR)
        fcen(c, t, c3 + 1.0, "= 3,6", cx + 380, 800, 100, CLARO)
    E.saida(c, t, C["s14"] - 0.1, um)
    if t < C["s14"]:
        return
    E.frase(c, t, a4, [("0,5", "g", 96, BR)] + ps("cabe", "i", 90, CLARO) + [("2 vezes", "g", 96, BR)] + ps("em cada inteiro", "i", 90, CLARO), W / 2, 280, "center", 0.12)
    fcen(c, t, a4 + 1.2, "0,5 + 0,5 = 1", W / 2, 440, 100, CLARO)
    E.foco(c, t, b4, 0.5, lambda a: E.selo(c, 420, 620, 50, False, a))
    E.frase(c, t, b4 + 0.1, ps("não compensa com", "i", 76, CLARO) + [("0,3", "g", 84, BR)], 500, 645, "left", 0.1)
    E.frase(c, t, c4, ps("aí,", "i", 84, CLARO) + [("multiplique tudo por 10", "g", 84, BR)], W / 2, 860, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s15.a"] - 0.9, ps("resolva", "i", 80), XE, 340, passo=0.1)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: E.formula(c, "f{x}{4} + 1 = f{x}{6} + 2", XE, 560, 130, "g", COR, a))
    E.frase(c, t, C["s15.b"], ps("quanto vale", "i", 90) + [("x?", "g", 96, COR)], XE, 790, passo=0.12)
    E.relogio(c, t, C["s16.a"], 1560, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    a8, b8, c8, d8, e8 = (C[f"s18.{k}"] for k in "abcde")
    xs = (560, 760, 900, 1060, 1220, 1420, 1560)
    tm = lerp(a7, b7, 0.48)  # "Multiplique cada termo por doze"

    def resolve():
        E.foco(c, t, a7, 0.5, lambda a: E.pilula(c, "MMC de 4 e 6 = 12", W / 2, 140, 60, "g", a=a, cor=E.SOBRE))
        colunas(c, t, [("f{x}{4}", TINTA, C["s17"] + 0.2), ("+", TINTA, C["s17"] + 0.2), ("1", TINTA, C["s17"] + 0.2), ("=", TINTA, C["s17"] + 0.2),
                       ("f{x}{6}", TINTA, C["s17"] + 0.2), ("+", TINTA, C["s17"] + 0.2), ("2", TINTA, C["s17"] + 0.2)], xs, 410, 100)
        for i, k in ((0, b7), (2, c7), (4, d7), (6, e7)):
            E.foco(c, t, tm + i * 0.08, 0.4, lambda a, i=i: E.pilula(c, "× 12", xs[i], 260, 42, "g", a=a, cor=E.SOBRE))
            realce(c, t, k, xs[i] - 60, 410, 120, 100, alto=1.9) if i in (0, 4) else realce(c, t, k, xs[i] - 30, 410, 60, 100)
        colunas(c, t, [("3x", COR, b7 + 1.6), ("+", COR, a8), ("12", COR, c7 + 0.9), ("=", COR, a8), ("2x", COR, d7 + 1.6), ("+", COR, a8), ("24", COR, e7 + 1.1)], xs, 600, 100)
        operacao(c, t, b8, "− 2x", 760)
        fcen(c, t, lerp(b8, c8, 0.45), "x + 12 = 24", 1060, 760, 100)
        operacao(c, t, c8, "− 12", 930)
        fcen(c, t, c8 + 1.2, "x = 12", 1060, 930, 110, COR)
        bola_res(c, t, c8 + 2.0, "x = 12", 1680, 840, 120, 70)
    E.saida(c, t, d8 - 0.6, resolve)
    if t < d8 - 0.6:
        return
    E.frase(c, t, d8 - 0.5, [("conferindo", "i", 84, COR)] + ps("com x = 12", "i", 84), W / 2, 190, "center", 0.12)
    xl, xr = 540, 1380
    fcen(c, t, d8, "f{12}{4} + 1", xl, 420, 100)
    fcen(c, t, lerp(d8, e8, 0.45), "= 3 + 1", xl, 580, 100)
    fcen(c, t, lerp(d8, e8, 0.75), "= 4", xl, 730, 110, COR)
    fcen(c, t, e8, "f{12}{6} + 2", xr, 420, 100)
    fcen(c, t, lerp(e8, C["s18.end"], 0.4), "= 2 + 2", xr, 580, 100)
    fcen(c, t, lerp(e8, C["s18.end"], 0.62), "= 4", xr, 730, 110, COR)
    fcen(c, t, lerp(e8, C["s18.end"], 0.75), "4 = 4", W / 2 - 40, 930, 120, CERTO)
    E.foco(c, t, lerp(e8, C["s18.end"], 0.82), 0.5, lambda a: E.selo(c, W / 2 + 200, 890, 50, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s19.a", "com fração:", "× MMC"), ("s19.b", "com vírgula:", "× 10, ou × 100 se forem 2 casas"), ("s19.c", "tudo quer dizer:", "cada termo, nos dois lados"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 70) + [(l2, "g", 72, COR if i == 0 else TINTA)], 320, y, "left", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0 = C["s20.a"], C["s20.b"]
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, a0 - 0.6, ps("a balança numa", "i", 80) + [("fórmula com várias letras", "g", 84, COR)], XE, 390, passo=0.11)
    E.frase(c, t, b0 - 0.4, ps("como a da", "i", 76) + [("velocidade de um carro", "g", 76, COR)], XE, 520, passo=0.1)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, fracoes=b_fracoes, decimais=b_decimais, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
