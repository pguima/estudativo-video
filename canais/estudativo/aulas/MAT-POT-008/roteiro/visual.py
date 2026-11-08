"""Visual — Estudativo · MAT-POT-008: expoente fracionário.
Peça da aula: a planta em que a linha da terra é o traço da fração, com a raiz embaixo. O resto é fórmula de verdade (E.formula).
Todo instante vem de C[...]: fala sem cue usa um ponto entre dois cues (lerp), para continuar certo com a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, linha
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-008_expoente_fracionario.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("origem", "dois_tercos", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert (2 ** 3) ** 4 == 2 ** 12 and 3 * 4 == 12 and 2 ** 3 == 8 and 8 ** 2 == 64 and 4 ** 3 == 64 and 3 ** 3 == 27
assert 45 * 45 == 2025 and 8 ** 3 == 512 and 22 ** 2 == 484 and 23 ** 2 == 529 and 5 ** 3 == 125 and 5 ** 2 == 25


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


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    """número dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def form(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def fase(c, t, t0, t1, fn):
    """uma tela do bloco: de t0 até sumir em t1"""
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def par(c, t, ta, tb, esq, dir_, x, y, s, cor=None, cor_d=None):
    """fórmula em ta e a continuação em tb, logo depois dela"""
    w = E.formula(c, esq, 0, 0, s, a=0)
    form(c, t, ta, esq, x, y, s, cor)
    form(c, t, tb, dir_, x + w + s * 0.2, y, s, cor_d or cor)


def traco(c, pts, p, cor, w):
    """linha quebrada que cresce do início ao fim (p = 0..1)"""
    n = len(pts) - 1
    k = p * n
    for i in range(n):
        q = M.clamp(k - i)
        if q > 0:
            M.line(c, pts[i][0], pts[i][1], lerp(pts[i][0], pts[i + 1][0], q), lerp(pts[i][1], pts[i + 1][1], q), cor, 1.0, w)


def folha(c, x, y, l, lado, p):
    """folha que brota do caule"""
    if p <= 0:
        return
    l *= p
    k = skia.Path()
    k.moveTo(x, y)
    k.quadTo(x + lado * l * 0.5, y - l * 0.62, x + lado * l, y - l * 0.3)
    k.quadTo(x + lado * l * 0.5, y + l * 0.1, x, y)
    c.drawPath(k, M.paint(E.COR))


def planta(c, t, ta, cx, y0, w=980, fundo=300):
    """a planta: a linha da terra é o traço da fração, a raiz cresce embaixo. cx = centro; y0 = linha da terra"""
    q = ep(t, ta - 0.6, 0.5)
    terra = M.mix(TINTA, E.COR, 0.2)
    if q <= 0:
        return
    M.rrect(c, cx - w / 2, y0, w, fundo, 18, terra, q)
    px = cx + 180
    cresce = ep(t, ta - 0.4, 0.9)
    M.line(c, px, y0, px, y0 - 300 * cresce, E.COR, 1.0, 14)
    folha(c, px, y0 - 130, 170, 1, ep(t, ta, 0.5))
    folha(c, px, y0 - 200, 170, -1, ep(t, ta + 0.15, 0.5))
    folha(c, px, y0 - 280, 130, 1, ep(t, ta + 0.3, 0.5))
    r = ep(t, ta, 1.0)
    for pts in (((px, y0), (px - 6, y0 + 90), (px + 12, y0 + 170), (px - 4, y0 + 260)),
                ((px - 6, y0 + 80), (px - 80, y0 + 130), (px - 110, y0 + 210)),
                ((px + 4, y0 + 60), (px + 90, y0 + 110), (px + 140, y0 + 190)),
                ((px + 10, y0 + 160), (px + 70, y0 + 210), (px + 80, y0 + 270))):
        traco(c, pts, r, CLARO, 9)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        form(c, t, a_, "9^{1/2}", 240, 520, 270, COR)
        E.frase(c, t, b_, ps("4,5?", "g", 130, ERRADO), 880, 340)
        E.frase(c, t, b_ + 0.4, ps("a metade de 9", "i", 84), 880, 460, passo=0.14)
        if t >= c_:
            E.risco(c, 860, 360, 1190, 240, t, c_, largura=12)
        E.sinal(c, t, c_, "=", 1040, 640, 130)
        E.foco(c, t, c_ + 0.1, 0.5, lambda p: num_bola(c, "3", 1290, 650, 150, 180, p))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        a2 = C["s02.a"]
        form(c, t, C["s02"] + 0.1, "9^{1/2}", W / 2, 470, 200, COR, "center")
        E.frase(c, t, lerp(C["s02"], a2, 0.4), ps("não é", "i", 100) + ps("invenção", "g", 92), W / 2, 650, "center", 0.17)
        E.frase(c, t, a2, ps("sai de uma regra", "i", 110) + ps("que você já conhece", "g", 88, COR), W / 2, 830, "center", 0.14)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 225, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "potência", "de potência"), ("s03.c", "raiz quadrada", "e raiz cúbica"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "g", 76, COR)], x + 44, y + 96)
        E.frase(c, t, C[k] + 0.3, [(l2, "i", 72)], x + 44, y + 176)
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.7), ps("faltou algo? procure no canal", "i", 62), XE, 880, passo=0.12)


# ---------------- de onde vem ----------------
def b_origem(c, t, C, b):
    def s04():
        a, b_, c_ = C["s04.a"], C["s04.b"], C["s04.c"]
        E.frase(c, t, C["s04"] + 0.1, ps("olhe a regra", "i", 96, COR), XE, 210)
        par(c, t, a, b_, "(2^3)^4", "= 2^{12}", 420, 530, 190)
        E.frase(c, t, c_, ps("os expoentes", "i", 100) + ps("se multiplicam", "g", 92, COR), W / 2, 740, "center", 0.17)
        form(c, t, c_ + 0.5, "3 × 4 = 12", W / 2, 900, 110, COR, "center")

    def s05():
        a, b_, c_, d = (C[f"s05.{k}"] for k in "abcd")
        form(c, t, a, "9^{1/2}", XE + 20, 340, 170, COR)
        E.frase(c, t, lerp(a, b_, 0.12), ps("não dá para contar", "i", 76), 720, 240, passo=0.11)
        E.frase(c, t, lerp(a, b_, 0.3), ps("meia vez", "g", 72, ERRADO), 720, 330, passo=0.11)
        E.frase(c, t, lerp(a, b_, 0.62), ps("o valor é escolhido para a", "i", 66), 720, 420, passo=0.1)
        E.frase(c, t, lerp(a, b_, 0.76), ps("regra continuar valendo", "g", 62, COR), 720, 500, passo=0.1)
        form(c, t, b_, "(9^{1/2})^2", XE + 20, 720, 150)
        form(c, t, c_, "f{1}{2} × 2 = 1", 820, 700, 120)
        form(c, t, d, "9^1 = 9", W / 2, 950, 130, CERTO, "center")

    def s06():
        a, b_, c_, d = (C[f"s06.{k}"] for k in "abcd")
        form(c, t, C["s06"] + 0.1, "9^{1/2}", XE + 20, 340, 170, COR)
        E.frase(c, t, a, ps("um número que,", "i", 88), XE + 20, 490, passo=0.13)
        E.frase(c, t, a + 0.6, ps("ao quadrado, dá 9", "g", 80, COR), XE + 20, 590, passo=0.13)
        form(c, t, b_, "= r{9}", 640, 340, 170)
        E.sinal(c, t, c_, "=", 1290, 280, 140)
        E.foco(c, t, c_, 0.5, lambda p: num_bola(c, "3", 1490, 280, 130, 150, p))
        E.frase(c, t, d - 0.5, ps("4,5 não serve:", "i", 88), XE + 20, 830, passo=0.13)
        form(c, t, d, "4,5^2 = 20,25", XE + 20, 950, 104, ERRADO)
        E.foco(c, t, d + 0.3, 0.45, lambda p: E.selo(c, 1000, 910, 60, False, p))

    def s07():
        a, b_, c_ = C["s07.a"], C["s07.b"], C["s07.c"]
        E.frase(c, t, C["s07"] + 0.2, ps("mesma base:", "i", 88) + ps("os expoentes se somam", "g", 80, COR), W / 2, 200, "center", 0.13)
        form(c, t, a, "9^{1/2} × 9^{1/2}", W / 2, 480, 170, None, "center")
        form(c, t, b_, "f{1}{2} + f{1}{2} = 1", 300, 710, 120)
        E.frase(c, t, b_ + 0.3, ps("duas metades,", "i", 80) + ps("um inteiro", "g", 76, COR), 880, 710, passo=0.14)
        form(c, t, c_, "9^1 = 9", W / 2, 940, 130, CERTO, "center")

    def s08():
        a, b_, c_, d, e = (C[f"s08.{k}"] for k in "abcde")
        E.frase(c, t, C["s08"] + 0.1, ps("com um terço, a mesma ideia", "i", 88, COR), XE, 190, passo=0.12)
        form(c, t, a, "(8^{1/3})^3", XE + 20, 400, 150)
        form(c, t, b_, "f{1}{3} × 3 = 1", 780, 385, 120)
        form(c, t, c_, "= 8", 1420, 400, 130, CERTO)
        E.frase(c, t, lerp(c_, d, 0.3), ps("o número que,", "i", 84) + ps("ao cubo, dá 8", "g", 76, COR), XE + 20, 590, passo=0.13)
        par(c, t, d, e, "8^{1/3} = r3{8}", "= 2", XE + 20, 850, 170, None, CERTO)

    def s09():
        a, b_, c_, d = (C[f"s09.{k}"] for k in "abcd")
        E.frase(c, t, a, ps("o de baixo da fração é", "i", 92) + ps("o índice da raiz", "g", 84, COR), W / 2, 210, "center", 0.13)
        for ti, n, nome, raiz, cx in ((b_, 2, "raiz quadrada", "r{  }", 450), (c_, 3, "raiz cúbica", "r3{  }", 960), (d, 4, "raiz quarta", "r4{  }", 1470)):
            E.foco(c, t, ti, 0.5, lambda p, n=n, cx=cx: (E.fracao(c, 1, n, cx, 440, 170, TINTA, p), E.caixa_pontilhada(c, cx - 78, 462, 156, 150, p, COR)))
            E.frase(c, t, ti + 0.2, [(nome, "i", 76)], cx, 730, "center")
            form(c, t, ti + 0.3, raiz, cx, 900, 130, COR, "center")

    s4, s5, s6, s7, s8, s9 = (C[f"s0{i}"] for i in range(4, 10))
    fase(c, t, s4, s5 - 0.1, s04)
    fase(c, t, s5, s6 - 0.1, s05)
    fase(c, t, s6, s7 - 0.1, s06)
    fase(c, t, s7, s8 - 0.1, s07)
    fase(c, t, s8, s9 - 0.1, s08)
    fase(c, t, s9, 1e9, s09)


# ---------------- dois terços ----------------
def b_dois_tercos(c, t, C, b):
    def s10():
        a, b_, c_, d = (C[f"s10.{k}"] for k in "abcd")
        E.frase(c, t, C["s10"] + 0.1, ps("e quando o de cima não é 1?", "i", 88, COR), XE, 190, passo=0.12)
        form(c, t, a, "8^{2/3}", XE + 20, 450, 200)
        form(c, t, b_, "f{2}{3} = f{1}{3} × 2", 800, 420, 130)
        form(c, t, c_, "8^{1/3}", 340, 800, 150)
        q = ep(t, d - 0.2, 0.5)
        M.arrow(c, 700, 750, 860, 750, COR, q, 6, 20, q)
        form(c, t, d, "(8^{1/3})^2", 900, 800, 150, COR)

    def s11():
        a, b_, c_, d, e = (C[f"s11.{k}"] for k in "abcde")
        form(c, t, a, "r3{8} = 2", XE + 40, 300, 130)
        form(c, t, b_, "2^2 = 4", XE + 40, 500, 130)
        form(c, t, c_, "8^{2/3} =", XE + 40, 780, 130)
        E.foco(c, t, c_ + 0.1, 0.5, lambda p: num_bola(c, "4", 760, 735, 110, 130, p))
        cx, cy, s = 1300, 450, 280
        E.foco(c, t, C["s11"] + 0.2, 0.5, lambda p: E.fracao(c, 2, 3, cx, cy, s, TINTA, p))
        E.foco(c, t, e, 0.45, lambda p: E.pilula(c, "potência", cx + 330, cy - 130, 66, estilo="g", a=p))
        E.foco(c, t, d, 0.45, lambda p: E.pilula(c, "raiz", cx + 270, cy + 160, 66, estilo="g", fundo=TINTA, a=p))

    def s12():
        a, b_, c_ = C["s12.a"], C["s12.b"], C["s12.c"]
        E.frase(c, t, C["s12"] + 0.1, ps("a ordem", "i", 100) + ps("não muda", "g", 92, COR) + ps("o resultado", "i", 100), W / 2, 220, "center", 0.17)
        form(c, t, a, "8^2 = 64", 270, 520, 130)
        form(c, t, b_, "r3{64} = 4", 960, 520, 130)
        E.frase(c, t, c_, ps("raiz primeiro:", "g", 100, COR) + ps("números menores", "i", 104), W / 2, 790, "center", 0.17)

    def s13():
        a, b_, c_ = C["s13.a"], C["s13.b"], C["s13.c"]
        E.frase(c, t, C["s13"] + 0.1, ps("mais um", "i", 96, COR), XE, 220)
        form(c, t, a, "27^{2/3}", XE + 20, 560, 210)
        form(c, t, b_, "r3{27} = 3", 960, 460, 130)
        form(c, t, c_, "3^2 = 9", 960, 690, 130, CERTO)

    a_, b_, c_, d_ = (C[f"s{i}"] for i in (10, 11, 12, 13))
    fase(c, t, a_, b_ - 0.1, s10)
    fase(c, t, b_, c_ - 0.1, s11)
    fase(c, t, c_, d_ - 0.1, s12)
    fase(c, t, d_, 1e9, s13)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    def s14():
        a, b_, c_ = C["s14.a"], C["s14.b"], C["s14.c"]
        E.frase(c, t, C["s14"] + 0.1, ps("o erro mais comum:", "i", 92), 620, 190, "center", 0.13)
        E.frase(c, t, a, ps("trocar os papéis", "g", 88, ERRADO), 1320, 190, "center", 0.13)
        form(c, t, a + 0.3, "8^{2/3}", XE + 20, 480, 170)
        E.frase(c, t, lerp(a, b_, 0.3), ps("o de cima como raiz,", "i", 76), 840, 380, passo=0.11)
        E.frase(c, t, lerp(a, b_, 0.6), ps("o de baixo como potência", "i", 76), 840, 480, passo=0.11)
        par(c, t, b_, lerp(b_, c_, 0.5), "r{8^3}", "= r{512}", XE + 20, 760, 170, ERRADO)
        xc = XE + 20 + E.formula(c, "r{8^3}", 0, 0, 170, a=0) + E.formula(c, "= r{512}", 0, 0, 170, a=0) + 170 * 0.55
        form(c, t, c_, "> 22", xc, 760, 170, ERRADO)
        E.frase(c, t, lerp(c_, C["s14.end"], 0.6), ps("bem longe de", "i", 92), W / 2 - 60, 950, "center", 0.14)
        E.foco(c, t, lerp(c_, C["s14.end"], 0.72), 0.45, lambda p: E.escreve(c, "4", W / 2 + 190, 950, 104, "g", CERTO, p))

    def s15():
        a, b_ = C["s15.a"], C["s15.b"]
        cx, y0 = 640, 620
        E.frase(c, t, C["s15"] + 0.1, ps("pense em uma planta", "i", 92, COR), XE, 180, passo=0.14)
        planta(c, t, a, cx, y0)
        xf = cx - 220
        E.foco(c, t, a - 0.3, 0.45, lambda p: centro(c, "2", xf, y0 - 60, 240, "g", COR, p))
        E.foco(c, t, a, 0.45, lambda p: centro(c, "3", xf, y0 + 240, 240, "g", BR, p))
        E.frase(c, t, a + 0.3, ps("a raiz fica", "i", 92), 1190, 420, passo=0.14)
        E.frase(c, t, a + 0.8, ps("embaixo da terra", "g", 76, COR), 1190, 530, passo=0.12)
        E.frase(c, t, b_, ps("o de baixo", "i", 100), 1190, 730, passo=0.14)
        E.frase(c, t, b_ + 0.4, ps("é a raiz", "g", 110, COR), 1190, 850, passo=0.14)

    fase(c, t, C["s14"], C["s15"] - 0.1, s14)
    fase(c, t, C["s15"], 1e9, s15)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s16():
        a, b_, c_, d, e = (C[f"s16.{k}"] for k in "abcde")
        E.frase(c, t, C["s16"] + 0.1, ps("agora, o atalho", "i", 84, CLARO), W / 2, 170, "center")
        E.frase(c, t, a, ps("escreva a", "i", 100, BR) + ps("base como potência", "g", 92, BR), W / 2, 310, "center", 0.15)
        form(c, t, b_, "8 = 2^3", 290, 560, 130, BR)
        form(c, t, c_, "(2^3)^{2/3}", 1000, 560, 130, BR)
        form(c, t, d, "3 × f{2}{3} = 2", 290, 840, 130, BR)
        form(c, t, e, "2^2 = 4", 1000, 860, 150, CLARO)

    def s17():
        a, b_, c_, d = (C[f"s17.{k}"] for k in "abcd")
        E.frase(c, t, a, ps("potência de potência", "g", 96, BR), W / 2, 200, "center", 0.15)
        tc = lerp(a, b_, 0.45)
        x, y, s = 300, 430, 130
        w = E.formula(c, "3 × ", 0, 0, s, a=0)
        wf = E.formula(c, "f{2}{3}", 0, 0, s, a=0)
        E.foco(c, t, tc - 0.3, 0.45, lambda p: E.formula(c, "3 × f{2}{3}", x, y, s, cor=BR, a=p))
        for cx, cy in ((x + s * 0.27, y - s * 0.36), (x + w + (wf - s * 0.1) / 2, y + s * 0.17)):
            if t >= tc:
                E.corta(c, t, tc, cx, cy, s * 0.8)
        E.frase(c, t, tc + 0.4, ps("o 3 cancela o 3 de baixo", "i", 84, CLARO), 800, 420, passo=0.11)
        E.frase(c, t, b_, ps("sem cancelamento,", "i", 92, CLARO) + ps("não compensa", "g", 84, BR), W / 2, 630, "center", 0.14)
        form(c, t, c_, "10^{1/2} = r{10}", 270, 820, 120, BR)
        E.frase(c, t, lerp(c_, d, 0.3), ps("10 não é quadrado de inteiro", "i", 68, CLARO), 960, 800, passo=0.1)
        E.frase(c, t, d, ps("deixe como raiz", "g", 80, BR) + ps("ou estime", "i", 88, CLARO), W / 2, 960, "center", 0.14)

    fase(c, t, C["s16"], C["s17"] - 0.1, s16)
    fase(c, t, C["s17"], 1e9, s17)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"] + 0.1, ps("hora de testar", "i", 84, COR), XE, 240)
    form(c, t, C["s18.a"], "25^{3/2} = ?", XE, 600, 190)
    E.relogio(c, t, C["s19.a"], 1490, 440, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s20():
        a, b_, c_, d = (C[f"s20.{k}"] for k in "abcd")
        form(c, t, C["s20"] + 0.1, "25^{3/2}", XE, 560, 190)
        x = 880
        E.foco(c, t, a, 0.45, lambda p: E.pilula(c, "de baixo: 2", x + 190, 220, 66, estilo="g", fundo=TINTA, a=p))
        E.frase(c, t, a + 0.3, ps("raiz quadrada", "i", 76), x + 420, 245)
        form(c, t, b_, "r{25} = 5", x, 420, 120)
        E.foco(c, t, c_, 0.45, lambda p: E.pilula(c, "de cima: 3", x + 180, 590, 66, estilo="g", a=p))
        E.frase(c, t, c_ + 0.3, ps("ao cubo", "i", 76), x + 400, 615)
        form(c, t, d, "5^3 =", x, 860, 130)
        E.foco(c, t, d + 0.1, 0.5, lambda p: num_bola(c, "125", 1420, 810, 130, 110, p, CERTO, BR))

    def s21():
        a, b_, c_ = C["s21.a"], C["s21.b"], C["s21.c"]
        E.frase(c, t, C["s21"] + 0.1, ps("pelo atalho", "i", 96, COR), W / 2, 200, "center")
        form(c, t, a, "25 = 5^2", 280, 480, 130)
        form(c, t, b_, "2 × f{3}{2} = 3", 950, 470, 130)
        form(c, t, c_, "5^3 = 125", W / 2, 800, 170, CERTO, "center")

    fase(c, t, C["s20"], C["s21"] - 0.1, s20)
    fase(c, t, C["s21"], 1e9, s21)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.1, ps("resumindo", "i", 96, COR), W / 2, 200, "center")
        itens = ((410, "s22.a", ps("expoente em fração é", "i", 92) + ps("raiz disfarçada", "g", 84, COR)),
                 (610, "s22.b", ps("o de baixo é", "i", 92) + ps("a raiz", "g", 84, COR)),
                 (810, "s22.c", ps("o de cima é", "i", 92) + ps("a potência", "g", 84, COR)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda p: num_bola(c, str(i + 1), 280, y - 30, 58, 66, p))
            E.frase(c, t, C[k] + 0.1, partes, 380, y, passo=0.14)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a_, b_, c_, d_, e_ = (C[f"s23.{k}"] for k in "abcde")
    E.frase(c, t, C["s23"] + 0.2, ps("próxima aula", "i", 84), XE, 230)
    E.frase(c, t, a_, ps("multiplicar raízes", "g", 96, COR), XE, 380, passo=0.15)
    E.frase(c, t, b_, ps("simplificar", "g", 96, COR), XE, 520)
    form(c, t, b_ + 0.3, "r{72}", 760, 520, 96, COR)
    E.frase(c, t, c_, ps("quando dá para", "i", 96) + ps("somar raízes", "g", 96, COR), XE, 660, passo=0.15)
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1460, 400, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, d_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1610, p), lerp(250, 445, p), ep(t, d_ + 0.2, 0.4), TINTA)
    E.frase(c, t, e_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, origem=b_origem, dois_tercos=b_dois_tercos, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
