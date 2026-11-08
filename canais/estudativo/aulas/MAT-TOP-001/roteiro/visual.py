"""Visual — Estudativo · MAT-TOP-001: números binomiais e triângulo de Pascal. Primeira aula de Tópicos Avançados.

LINGUAGEM VISUAL DO MÓDULO "Binômio, distribuição binomial e casa dos pombos" (as próximas copiam daqui):
- binom(): o número binomial em pé, entre parênteses altos, sem tracinho (não é fração). Total em cima, escolhidos embaixo.
- Triângulo de Pascal: números soltos em linhas centradas (pascal()); a soma dos dois de cima aparece com dois traços
  que descem até o número novo (soma()). Linha e posição contam do zero; o rótulo "linha n" fica à esquerda.
- Cor da matéria para o que está sendo calculado agora; tinta para o resto; resposta na esfera; erro em vermelho, certo em verde.
- Pessoas como bolinhas com a inicial (as mesmas cores de MAT-CNT-008).
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
from math import comb
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-001_numeros_binomiais_triangulo_de_pascal.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("binomial", "triangulo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
GENTE = ["#E08A3C", "#8E5BD9", "#5B8DB8", "#55895A", "#C2463A", "#9C9CA3"]
assert comb(5, 2) == 10 == 5 * 4 // 2 and comb(4, 1) + comb(4, 2) == 10 and comb(5, 2) == comb(5, 3)
assert [comb(4, k) for k in range(5)] == [1, 4, 6, 4, 1] and sum(comb(4, k) for k in range(5)) == 16 == 2 ** 4
assert [comb(3, k) for k in range(4)] == [1, 3, 3, 1] and 4 * 3 // 2 == 6
assert [comb(6, k) for k in range(7)] == [1, 6, 15, 20, 15, 6, 1] and 6 * 5 // 2 == 15 and sum(comb(6, k) for k in range(7)) == 64 == 2 ** 6


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
    """texto centrado em (x, y) que entra com foco"""
    E.foco(c, t, t0, 0.45, lambda a: centro(c, str(s), x, y + size * 0.36, size, est, cor, a))


def binom(c, n, p, cx, cy, size, cor=None, a=1.0, cor_n=None, cor_p=None):
    """número binomial em pé: n em cima, p embaixo, entre parênteses altos e sem tracinho. Devolve a largura"""
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


def pessoa(c, t, t0, x, y, r, letra, cor, a=1.0):
    def f(q):
        c.drawCircle(x, y, r, M.paint(cor, q * a))
        centro(c, letra, x, y + r * 0.36, r, "g", BR, q * a)
    E.foco(c, t, t0, 0.45, f)


def pos(n, k, cx, y0, dx, dy):
    return cx + (k - n / 2) * dx, y0 + n * dy


def pascal(c, t, tl, cx, y0, dx, dy, size, cor=None, linhas=None, passo=0.07):
    """triângulo de Pascal: tl[n] = instante da linha n (None = não mostra); cor(n, k) → cor do número"""
    for n, tn in enumerate(tl):
        if tn is None:
            continue
        for k in range(n + 1):
            x, y = pos(n, k, cx, y0, dx, dy)
            num(c, t, tn + k * passo, comb(n, k), x, y, size, cor(n, k) if cor else TINTA)


def soma(c, t, t0, n, k, cx, y0, dx, dy, size, cor=None, d=0.5):
    """os dois traços que descem dos vizinhos de cima até o número (n, k)"""
    cor = cor or COR
    x, y = pos(n, k, cx, y0, dx, dy)
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    for kk in (k - 1, k):
        if 0 <= kk <= n - 1:
            x0, y1 = pos(n - 1, kk, cx, y0, dx, dy)
            ax, ay = lerp(x0, x, 0.28), y1 + size * 0.55
            bx, by = lerp(x0, x, 0.72), y - size * 0.55
            M.line(c, ax, ay, lerp(ax, bx, p), lerp(ay, by, p), cor, 1.0, 5)


def rotulos_linhas(c, t, t0, ns, x, cx, y0, dx, dy, size=40, cor=TINTA2, passo=0.12):
    for i, n in enumerate(ns):
        _, y = pos(n, 0, cx, y0, dx, dy)
        E.foco(c, t, t0 + i * passo, 0.4, lambda a, n=n, y=y: E.escreve(c, f"linha {n}", x, y + size * 0.36, size, "i", cor, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        binom_em(c, t, C["s01.a"], 5, 2, 560, 430, 190)
        if t >= C["s01.b"]:
            sinal = E.sinal
            sinal(c, t, C["s01.b"], "≠", 900, 470, 150, ERRADO)
            E.foco(c, t, C["s01.b"] + 0.2, 0.5, lambda a: E.fracao(c, 5, 2, 1160, 470, 170, ERRADO, a))
            if t >= C["s01.b"] + 1.4:
                E.risco(c, 1060, 640, 1270, 300, t, C["s01.b"] + 1.4, largura=16)
        E.frase(c, t, C["s01.c"], ps("não é fração:", "i", 80) + [("número", "g", 76, COR), ("binomial", "g", 76, COR)], W / 2, 850, "center")
        if t >= C["s01.d"]:
            E.sinal(c, t, C["s01.d"] - 0.1, "=", 1440, 470, 150, TINTA)
            bola_txt(c, t, C["s01.d"], "10", 1650, 470, 130, 130)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 560, 270 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("binomiais", "g", 120, COR)], XE, 480)
        E.frase(c, t, C["s02.b"], [("e", "i", 110), ("o", "i", 110), ("triângulo", "g", 120)], XE, 640)
        E.frase(c, t, C["s02.b"] + 0.5, [("de", "i", 110), ("Pascal", "g", 120, COR)], XE, 790)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1300, 545, 80, "g", BR, a),
                                                      E.escreve(c, "de prova", 1320, 630, 80, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 84), XE, 300)
    E.frase(c, t, C["s03.a"], [("a", "i", 120), ("combinação", "g", 120, COR)], XE, 460)
    x, y, w, h = XE, 560, 1580, 330
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, ps("arranjo dividido pelo fatorial", "i", 64) + [("de", "i", 64), ("quantos", "i", 64), ("escolhe", "g", 60, COR)],
            x + 50, y + 100)
    E.formula_em(c, t, C["s03.b"] + 1.2, "C(5, 2) = f{5 × 4}{2!}", x + 50, y + 245, 92, "g", TINTA)
    E.foco(c, t, C["s03.b"] + 1.8, 0.5, lambda a: E.escreve(c, "a ordem não importa", x + 900, y + 250, 58, "i", TINTA2, a))


# ---------------- o número binomial ----------------
AMIGOS = ("A", "B", "C", "D", "E")


def b_binomial(c, t, C, b):
    def parte1():
        cx, cy = 470, 470
        binom_em(c, t, C["s04.a"], 5, 2, cx, cy, 200, cor_n=COR if t >= C["s04.b"] else None, cor_p=COR if t >= C["s04.c"] else None)
        E.foco(c, t, C["s04.a"] + 0.3, 0.5, lambda a: E.escreve(c, "= C(5, 2)", 700, cy + 70, 96, "g", TINTA, a))
        E.foco(c, t, C["s04.b"], 0.4, lambda a: (M.arrow(c, 250, cy - 90, 380, cy - 90, COR, a, 5, 18, a),
                                                E.escreve(c, "total", 90, cy - 70, 58, "i", COR, a)))
        E.foco(c, t, C["s04.c"], 0.4, lambda a: (M.arrow(c, 250, cy + 150, 380, cy + 150, COR, a, 5, 18, a),
                                                E.escreve(c, "escolhe", 40, cy + 170, 58, "i", COR, a)))
        E.frase(c, t, C["s04.d"], ps("binomial de 5 sobre 2", "i", 66), XE, 850)
        E.frase(c, t, C["s04.d"] + 1.0, ps("escolher 2 entre 5", "g", 60, COR), XE, 950)
        # cinco amigos e dois ingressos
        for i, l in enumerate(AMIGOS):
            pessoa(c, t, C["s05.a"] + i * 0.1, 1180 + i * 130, 260, 52, l, GENTE[i])
        for i in range(2):
            E.foco(c, t, C["s05.a"] + 0.8 + i * 0.15, 0.4, lambda a, i=i: (
                M.rrect(c, 1300 + i * 220, 360, 180, 90, 14, COR, a), centro(c, "ingresso", 1390 + i * 220, 418, 34, "b", BR, a)))
        E.formula_em(c, t, C["s05.b"], "5 × 4 = 20", 1180, 600, 92, "g", TINTA)
        E.formula_em(c, t, C["s05.c"], "f{20}{2!} = 10", 1180, 790, 92, "g", TINTA)
        bola_txt(c, t, C["s05.d"], "10", 1650, 760, 110, 110)
        E.foco(c, t, C["s05.d"] + 0.3, 0.4, lambda a: centro(c, "duplas", 1650, 930, 56, "i", COR, a))
    E.saida(c, t, C["s06"] - 0.1, parte1)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], ps("três casos de cabeça", "i", 80), W / 2, 180, "center")
    casos = (("s06.a", ("n", "0"), "= 1", "ninguém vai"), ("s06.b", ("n", "n"), "= 1", "todos vão"), ("s06.c", ("n", "1"), "= n", "um de cada vez"))
    for i, (k, (n, p), r, txt) in enumerate(casos):
        x = 330 + i * 560
        binom_em(c, t, C[k], n, p, x, 360, 110)
        E.formula_em(c, t, C[k] + 0.3, r, x + 120, 410, 100, "g", COR)
        E.foco(c, t, C[k] + 0.5, 0.4, lambda a, x=x, txt=txt: centro(c, txt, x + 60, 560, 50, "i", TINTA2, a))
    y = 800
    binom_em(c, t, C["s06.d"], 5, 2, 700, y - 40, 120)
    E.foco(c, t, C["s06.d"] + 0.4, 0.4, lambda a: centro(c, "=", 960, y + 30, 110, "g", TINTA, a))
    binom_em(c, t, C["s06.d"] + 0.6, 5, 3, 1220, y - 40, 120, cor=COR)
    E.foco(c, t, C["s06.d"] + 1.0, 0.4, lambda a: (centro(c, "2 vão", 700, y + 170, 48, "i", TINTA2, a),
                                                  centro(c, "3 ficam", 1220, y + 170, 48, "i", COR, a)))


# ---------------- o triângulo ----------------
TX, TY, TDX, TDY, TS = 1300, 210, 140, 128, 66


def b_triangulo(c, t, C, b):
    # s07: a linha quatro em binomiais, que vira números
    def linha4():
        E.frase(c, t, C["s07"], ps("os binomiais em linhas", "i", 80), W / 2, 220, "center")
        for k in range(5):
            x = 400 + k * 280
            binom_em(c, t, C["s07.a"] + k * 0.25, 4, k, x, 520, 110, cor_n=COR)
            num(c, t, C["s07.a"] + 1.8 + k * 0.1, comb(4, k), x, 800, 90, COR)
        E.foco(c, t, C["s07.a"] + 1.7, 0.4, lambda a: E.escreve(c, "linha 4", XE - 60, 830, 56, "i", TINTA2, a))
    E.saida(c, t, C["s07.b"] - 0.1, linha4)
    if t < C["s07.b"]:
        return
    s09 = t >= C["s09"]

    def cor(n, k):
        if t >= C["s10.c"] and n == 4 and k == 2:
            return COR
        if s09 and t < C["s10"] and ((n == 4 and k in (1, 2)) or (n == 5 and k == 2)):
            return COR
        if t >= C["s07.e"] and t < C["s08"] and k in (0, n):
            return COR
        return TINTA
    tl = [C["s07.b"], C["s07.c"], C["s07.d"], C["s08.b"] + 0.4, C["s08.d"], C["s09.f"] if s09 else None]
    pascal(c, t, tl, TX, TY, TDX, TDY, TS, cor)
    def zero():
        E.frase(c, t, C["s07.b"], ps("linhas a partir do", "i", 64), 90, 480)
        E.frase(c, t, C["s07.b"] + 0.8, [("zero", "g", 76, COR)], 90, 580)
        E.frase(c, t, C["s07.e"], [("começa", "i", 60), ("e", "i", 60), ("termina", "i", 60)], 90, 760)
        E.frase(c, t, C["s07.e"] + 0.8, [("em", "i", 60), ("1", "g", 70, COR)], 90, 850)
    if t < C["s08"]:
        E.saida(c, t, C["s08"] - 0.1, zero)
    rotulos_linhas(c, t, C["s07.b"], [0], 760, TX, TY, TDX, TDY)
    rotulos_linhas(c, t, C["s07.c"], [1], 760, TX, TY, TDX, TDY)
    rotulos_linhas(c, t, C["s07.d"], [2], 760, TX, TY, TDX, TDY)
    rotulos_linhas(c, t, C["s08.b"] + 0.4, [3], 760, TX, TY, TDX, TDY)
    rotulos_linhas(c, t, C["s08.d"], [4], 760, TX, TY, TDX, TDY)
    if s09:
        rotulos_linhas(c, t, C["s09.f"], [5], 760, TX, TY, TDX, TDY)
    soma(c, t, C["s08.b"], 3, 1, TX, TY, TDX, TDY, TS)
    soma(c, t, C["s08.b"] + 0.4, 3, 2, TX, TY, TDX, TDY, TS)
    soma(c, t, C["s08.c"], 4, 2, TX, TY, TDX, TDY, TS)
    soma(c, t, C["s08.c"] + 0.6, 4, 1, TX, TY, TDX, TDY, TS)
    soma(c, t, C["s08.c"] + 0.6, 4, 3, TX, TY, TDX, TDY, TS)
    if s09 and t < C["s10"]:
        soma(c, t, C["s09.f"], 5, 2, TX, TY, TDX, TDY, TS)

    # texto da esquerda
    def regra():
        E.frase(c, t, C["s08.a"], ps("cada número é a", "i", 64), 90, 480)
        E.frase(c, t, C["s08.a"] + 0.8, [("soma", "g", 70, COR), ("dos", "i", 64), ("dois", "i", 64)], 90, 570)
        E.frase(c, t, C["s08.a"] + 1.3, ps("de cima", "i", 64), 90, 660)
        E.frase(c, t, C["s08.e"], [("triângulo", "g", 76), ("de", "i", 76)], 90, 880)
        E.frase(c, t, C["s08.e"] + 0.4, [("Pascal", "g", 76, COR)], 90, 970)
    if t < C["s09"]:
        E.saida(c, t, C["s09"] - 0.1, regra)

    def ana():
        pessoa(c, t, C["s09.a"], 140, 330, 50, "A", GENTE[0])
        E.frase(c, t, C["s09.a"] + 0.2, ps("separe a Ana", "i", 60), 220, 350)
        E.frase(c, t, C["s09.b"], [("Ana", "b", 54), ("vai", "g", 54, CERTO)], 90, 500)
        E.formula_em(c, t, C["s09.c"], "C(4, 1) = 4", 90, 590, 64, "g", COR)
        E.frase(c, t, C["s09.d"], [("Ana", "b", 54), ("não", "g", 54, ERRADO), ("vai", "g", 54, ERRADO)], 90, 720)
        E.formula_em(c, t, C["s09.e"], "C(4, 2) = 6", 90, 810, 64, "g", COR)
        E.formula_em(c, t, C["s09.f"], "4 + 6 = 10", 90, 960, 76, "g", TINTA)
    if s09 and t < C["s10"]:
        E.saida(c, t, C["s10"] - 0.1, ana)
    if t >= C["s10"]:
        E.frase(c, t, C["s10.a"], [("de", "i", 60), ("cima:", "i", 60), ("linha", "g", 60, COR)], 90, 420)
        E.frase(c, t, C["s10.b"], [("de", "i", 60), ("baixo:", "i", 60), ("posição", "g", 60, COR)], 90, 520)
        E.frase(c, t, C["s10.b"] + 0.8, ps("contando do zero", "i", 54, TINTA2), 90, 610)
        binom_em(c, t, C["s10.c"], 4, 2, 230, 790, 96, cor=COR)
        if t >= C["s10.c"]:
            x, y = pos(4, 2, TX, TY, TDX, TDY)
            q = ep(t, C["s10.c"] + 0.4, 0.5)
            c.drawCircle(x, y, 64, M.paint(COR, q, stroke=6))
            for k in range(5):
                xx, yy = pos(4, k, TX, TY, TDX, TDY)
                E.foco(c, t, C["s10.c"] + 0.2 + k * 0.1, 0.3, lambda a, xx=xx, yy=yy, k=k: centro(c, str(k), xx, yy + 82, 34, "b", COR, a))
        E.foco(c, t, C["s10.d"], 0.4, lambda a: E.escreve(c, "= 6", 340, 830, 96, "g", COR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], XE, 200)
    cx, y0, dx, dy = 1250, 260, 150, 150
    certo = t >= C["s11.d"]

    def cor(n, k):
        if not certo and t >= C["s11.b"] + 1.5 and n == 3:
            return ERRADO
        if t >= C["s11.e"] and n == 4 and k == 2:
            return CERTO
        return TINTA
    pascal(c, t, [C["s11"] + 0.3 + 0.15 * i for i in range(5)], cx, y0, dx, dy, 70, cor)
    if not certo:
        for i in range(4):
            E.foco(c, t, C["s11.b"] + i * 0.35, 0.3, lambda a, i=i: E.escreve(c, f"{i + 1}ª", 680, y0 + (i + 1) * dy - dy + 25, 48, "b", ERRADO, a))
    else:
        for i in range(5):
            E.foco(c, t, C["s11.d"] + i * 0.15, 0.3, lambda a, i=i: E.escreve(c, f"linha {i}", 640, y0 + i * dy + 25, 46, "i", CERTO, a))
    binom_em(c, t, C["s11.a"], 4, 2, 300, 420, 110)
    if t >= C["s11.c"]:
        E.foco(c, t, C["s11.c"], 0.4, lambda a: E.escreve(c, "= 3", 440, 470, 110, "g", ERRADO, a))
        if t >= C["s11.d"]:
            E.risco(c, 440, 500, 620, 380, t, C["s11.d"], largura=14)
    E.formula_em(c, t, C["s11.e"], "f{4 × 3}{2} = 6", XE, 820, 100, "g", CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], [("atalho:", "i", 80, CLARO), ("some", "g", 76, BR), ("a", "i", 80, CLARO), ("linha", "g", 76, BR)], W / 2, 180, "center")

    def soma_linha():
        partes = ["1", "+", "4", "+", "6", "+", "4", "+", "1"]
        for i, s in enumerate(partes):
            num(c, t, C["s12.b"] - 0.6 + i * 0.12, s, 300 + i * 105, 420, 100, BR if s != "+" else CLARO)
        E.foco(c, t, C["s12.b"] + 1.2, 0.5, lambda a: E.escreve(c, "= 16", 1250, 456, 100, "g", BR, a))
        E.formula_em(c, t, C["s12.c"], "= 2^4", 1560, 456, 100, "g", CLARO)
        E.foco(c, t, C["s12.d"], 0.5, lambda a: E.pilula(c, "linha n:  soma = 2 elevado a n", W / 2, 700, 64, "g", fundo=COR, a=a))
    E.saida(c, t, C["s13"] - 0.1, soma_linha)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], ps("grupos de qualquer tamanho", "i", 64, CLARO), W / 2, 320, "center")
    for i, l in enumerate(("A", "B", "C", "D")):
        x = 480 + i * 320
        pessoa(c, t, C["s13.b"] + i * 0.15, x, 470, 56, l, GENTE[i])
        E.foco(c, t, C["s13.b"] + 0.6 + i * 0.15, 0.4, lambda a, x=x: (centro(c, "entra", x, 580, 40, "b", CERTO, a),
                                                                       centro(c, "ou não", x, 630, 40, "b", "#FF8A8E", a)))
        if i < 3:
            E.foco(c, t, C["s13.c"] + i * 0.2, 0.4, lambda a, x=x: centro(c, "×", x + 160, 500, 70, "g", CLARO, a))
        E.foco(c, t, C["s13.c"] + i * 0.2, 0.4, lambda a, x=x: centro(c, "2", x, 740, 90, "g", BR, a))
    E.foco(c, t, C["s13.c"] + 1.0, 0.4, lambda a: E.escreve(c, "= 16", 1640, 770, 90, "g", CLARO, a))
    E.foco(c, t, C["s13.f"], 0.4, lambda a: E.pilula(c, "sem o grupo vazio: 16 − 1 = 15", W / 2, 855, 50, "g", fundo=COR, a=a))
    E.foco(c, t, C["s13.d"], 0.5, lambda a: (E.escreve(c, "quantos grupos no total?", 220, 1000, 52, "i", CLARO, a),
                                            E.escreve(c, "2^n", 860, 920, 60, "g", BR, a) if False else E.formula(c, "→ 2^n", 840, 1000, 60, "g", BR, a)))
    E.foco(c, t, C["s13.e"], 0.5, lambda a: (E.escreve(c, "um tamanho só?", 1100, 1000, 52, "i", CLARO, a),
                                            E.escreve(c, "→ C(n, p)", 1460, 1000, 56, "g", BR, a)))


# ---------------- questão ----------------
QX, QY, QDX = 1150, 0, 150


def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 170)
    y5, y6 = 330, 480
    for k in range(6):
        num(c, t, C["s14.a"] + k * 0.12, comb(5, k), 520 + k * QDX + QDX / 2, y5, 72)
    E.foco(c, t, C["s14.a"], 0.4, lambda a: E.escreve(c, "linha 5", XE, y5 + 26, 48, "i", TINTA2, a))
    for k in range(7):
        num(c, t, C["s14.b"] + k * 0.08, "?", 520 + k * QDX, y6, 72, CINZA)
    E.foco(c, t, C["s14.b"], 0.4, lambda a: E.escreve(c, "linha 6", XE, y6 + 26, 48, "g", COR, a))
    binom_em(c, t, C["s14.c"], 6, 2, 280, 700, 90)
    E.foco(c, t, C["s14.c"] + 0.3, 0.4, lambda a: E.escreve(c, "pela conta = ?", 390, 750, 60, "i", TINTA, a))
    E.foco(c, t, C["s14.d"], 0.4, lambda a: E.escreve(c, "soma da linha 6 = ?", XE, 940, 60, "i", TINTA, a))
    E.relogio(c, t, C["s15.a"], 1530, 760, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    y5, y6, dx = 260, 410, 175
    cx = W / 2
    for k in range(6):
        num(c, t, C["s16"] + k * 0.08, comb(5, k), cx + (k - 2.5) * dx, y5, 76)
    ordem = {0: "s16.a", 6: "s16.a", 1: "s16.b", 2: "s16.c", 3: "s16.d"}
    for k in range(7):
        x = cx + (k - 3) * dx
        k0 = ordem.get(k)
        t0 = C[k0] if k0 else C["s16.e"] + (k - 3) * 0.2
        if t < t0:
            num(c, t, C["s16"], "?", x, y6, 76, CINZA)
        else:
            num(c, t, t0, comb(6, k), x, y6, 80, COR if k in (1, 2, 3) or t >= C["s16.e"] else TINTA)
        if k0 in ("s16.b", "s16.c", "s16.d"):
            p = ease_io(prog(t, t0 - 0.1, 0.5))
            for kk in (k - 1, k):
                x0 = cx + (kk - 2.5) * dx
                if p > 0:
                    M.line(c, lerp(x0, x, 0.25), y5 + 45, lerp(lerp(x0, x, 0.25), lerp(x0, x, 0.75), p), lerp(y5 + 45, y6 - 45, p), COR, 1.0, 5)
    E.foco(c, t, C["s16"], 0.4, lambda a: (E.escreve(c, "linha 5", 90, y5 + 26, 44, "i", TINTA2, a), E.escreve(c, "linha 6", 90, y6 + 26, 44, "g", COR, a)))
    # s17
    binom_em(c, t, C["s17.a"], 6, 2, 300, 650, 90)
    E.formula_em(c, t, C["s17.a"] + 0.3, "= f{6 × 5}{2!} = f{30}{2}", 410, 690, 84, "g", TINTA)
    E.foco(c, t, C["s17.b"], 0.4, lambda a: E.escreve(c, "= 15", 1010, 690, 84, "g", CERTO, a))
    E.formula_em(c, t, C["s17.c"], "soma = 2^6 = 64", 300, 930, 84, "g", TINTA)
    E.formula_em(c, t, C["s17.d"], "1 + 6 + 15 + 20 + 15 + 6 + 1 = 64", 1000, 930, 54, "b", CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s18.a", "a combinação em pé"), ("s18.b", "soma dos dois de cima"))):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 420, y - 30, 56, a=a),
                                                         centro(c, str(i + 1), 420, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 96)], 520, y)
        binom_em(c, t, C["s18.a"] + 0.6, "n", "p", 1800, 340, 80, cor=COR)
        pascal(c, t, [C["s18.b"] + 0.3 + 0.1 * i for i in range(5)], 1100, 700, 100, 70, 50)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], ps("próxima aula", "i", 84), XE, 300)
    E.formula_em(c, t, C["s19.a"], "(x + 2)^4", XE, 470, 130, "g", TINTA)
    E.frase(c, t, C["s19.b"], [("Binômio", "g", 140, COR)], XE, 650)
    E.frase(c, t, C["s19.b"] + 0.3, [("de", "i", 130), ("Newton", "g", 140, COR)], XE, 800)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, binomial=b_binomial, triangulo=b_triangulo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
