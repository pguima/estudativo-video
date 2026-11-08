"""Visual — Estudativo · MAT-POT-007: raiz quadrada exata e aproximada.
Peças da aula: piso de lajotas (a raiz é o lado do quadrado) e a coluna de fatoração do kit, com as duplas de primos marcadas.
Todo instante vem de C[...]: fala sem cue usa um ponto entre dois cues (lerp), para continuar certo com a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, linha, montar, tabela
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-007_raiz_quadrada_exata_aproximada.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "fatorar", "estimar", "atalho", "questao", "fim"))
BR = "#FFFFFF"

T1764 = montar((1764,), (2, 2, 3, 3, 7, 7))
T1764_TELA = dict(T1764, linhas=[("1.764",)] + T1764["linhas"][1:])  # a tabela escreve str(v): assim sai com o ponto
T784 = montar((784,), (2, 2, 2, 2, 7, 7))
G = dict(xs=(380,), xb=540, xp=640, y0=205, dy=118, s=92)  # coluna de 7 linhas
assert 2 * 3 * 7 == 42 and 42 * 40 == 1680 and 42 * 2 == 84 and 1680 + 84 == 1764 == 42 ** 2
assert 2 * 2 * 5 == 20 and 4 ** 2 == 16 and 5 ** 2 == 25 and 45 * 45 == 2025 and 44 * 44 == 1936
assert 8 * 8 == 64 and 40 ** 2 == 1600 and 50 ** 2 == 2500 and 2 * 2 * 7 == 28 and 28 ** 2 == 784


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


def troca(c, t, itens, fim, x, y, size, cor=None, est="b"):
    """texto da vez: itens = [(instante, texto)], cada um some quando o seguinte chega"""
    for i, (ti, s) in enumerate(itens):
        t1 = itens[i + 1][0] - 0.15 if i + 1 < len(itens) else fim
        if ti - 0.1 <= t < t1 + 0.3:
            E.saida(c, t, t1, lambda: E.foco(c, t, ti, 0.4, lambda a: E.escreve(c, s, x, y, size, est, cor or TINTA, a)), d=0.2)


def piso(c, t, x, y, cel, ti, n=5, dt=0.03):
    """piso quadrado de n × n lajotas que se assentam uma a uma, com as bordas alternadas"""
    gap = 6
    for i in range(n * n):
        q = ease_back(prog(t, ti + i * dt, 0.35))
        if q <= 0:
            continue
        cx, cy, r = x + (i % n) * (cel + gap), y + (i // n) * (cel + gap), cel * min(q, 1.08)
        cor = E.COR if (i % n + i // n) % 2 == 0 else M.mix(E.COR, BR, 0.32)
        M.rrect(c, cx + (cel - r) / 2, cy + (cel - r) / 2, r, r, 9, cor)


def dupla(c, t, ti, i, cor=None, g=G):
    """caixa em volta de dois primos seguidos da coluna: i = linha do primeiro"""
    q = ep(t, ti, 0.45)
    s, y = g["s"], g["y0"] + i * g["dy"]
    E.caixa_pontilhada(c, g["xp"] - s * 0.6, y - s * 0.88, s * 1.2, g["dy"] + s * 1.02, q, cor or COR, prog_=q)


def direita(c, s, x, y, size, cor=None, a=1.0):
    """texto pesado alinhado pela direita"""
    E.escreve(c, s, x - E.larg(s, "g", size), y, size, "g", cor or TINTA, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]

    def calc():
        form(c, t, a_, "r{1.764}", 690, 480, 240, COR, "center")
        E.sinal(c, t, b_ - 0.15, "=", 1190, 400, 170)
        E.foco(c, t, b_, 0.5, lambda p: num_bola(c, "42", 1450, 395, 170, 170, p))
        E.frase(c, t, lerp(a_, b_, 0.3), ps("parece conta de", "i", 96) + ps("calculadora", "g", 88), W / 2, 740, "center", 0.16)
        E.frase(c, t, lerp(a_, b_, 0.68), ps("só com", "i", 96) + ps("divisões simples", "g", 88, COR), W / 2, 880, "center", 0.16)
    E.saida(c, t, C["s02"] - 0.1, calc)

    if t >= C["s02"]:
        a2, b2 = C["s02.a"], C["s02.b"]
        form(c, t, a2, "r{20}", W / 2, 590, 270, COR, "center")
        E.frase(c, t, C["s02"] + 0.1, ps("e quando não é exata?", "i", 96), W / 2, 200, "center", 0.14)
        E.frase(c, t, b2, ps("um valor", "i", 120) + ps("bem próximo", "g", 112, COR), W / 2, 860, "center", 0.2)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    itens = (("s03.b", "elevar", "ao quadrado"), ("s03.c", "fatorar", "em primos"), ("s03.d", "multiplicar", "decimais"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 150 + i * 230
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    alvo = [150 + i * 230 + 170 for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.55), ps("faltou algo? procure no canal", "i", 64), XE, 880, passo=0.12)


# ---------------- o que é ----------------
def b_ideia(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    xp, yp, cel = 200, 280, 106
    lado = 5 * cel + 24
    piso(c, t, xp, yp, cel, a4)
    E.frase(c, t, a4, ps("um piso", "i", 92) + ps("quadrado", "g", 84, COR), XE, 190)
    x = 880

    def conta():
        E.frase(c, t, lerp(a4, b4, 0.15), ps("25", "g", 130, COR) + ps("lajotas", "i", 120), x, 400, passo=0.16)
        E.frase(c, t, lerp(a4, b4, 0.55), ps("quantas tem", "i", 90), x, 560, passo=0.16)
        E.frase(c, t, lerp(a4, b4, 0.72), ps("cada lado?", "g", 86, COR), x, 670, passo=0.16)
        form(c, t, b4 + 0.2, "5 × 5 = 25", x, 860, 110)
    E.saida(c, t, C["s05"] - 0.1, conta)

    E.foco(c, t, b4, 0.45, lambda p: (E.chave(c, xp, xp + lado, yp + lado + 14, COR, p, 18, 5, abre=False),
                                       centro(c, "5", xp + lado / 2, yp + lado + 120, 90, "g", COR, p)))
    if t >= C["s05"]:
        a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
        E.frase(c, t, a5, ps("raiz quadrada", "g", 116, COR), x, 330)
        E.frase(c, t, b5, ps("que número,", "i", 84), x, 480, passo=0.16)
        E.frase(c, t, lerp(b5, c5, 0.16), ps("vezes ele mesmo,", "i", 84), x, 580, passo=0.14)
        E.frase(c, t, lerp(b5, c5, 0.34), ps("dá este aqui?", "g", 76, COR), x, 680, passo=0.14)
        ty = lerp(b5, c5, 0.58)
        form(c, t, ty, "5^2 = 25", x, 860, 100)
        p = ep(t, ty + 0.4, 0.5)
        M.arrow(c, 1200, 830, 1290, 830, COR, p, 5, 18, p)
        form(c, t, c5, "r{25} = 5", 1310, 860, 104, COR)


# ---------------- só o positivo ----------------
def b_sinal(c, t, C, b):
    a_, b_, c_, d_ = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    E.frase(c, t, C["s06"] + 0.1, ps("um detalhe", "i", 96, COR), W / 2, 190, "center")
    form(c, t, a_, "3^2 = 9", 530, 440, 130, None, "center")
    form(c, t, b_, "(−3)^2 = 9", 1340, 440, 130, None, "center")
    E.frase(c, t, c_, ps("o símbolo da raiz escolhe", "i", 84) + ps("o positivo", "g", 80, COR), W / 2, 650, "center", 0.14)
    form(c, t, c_ + 0.2, "r{9}", 880, 880, 150, COR, "center")
    E.sinal(c, t, d_, "=", 1040, 825, 120)
    E.foco(c, t, d_, 0.5, lambda p: num_bola(c, "3", 1215, 825, 96, 110, p))


# ---------------- fatorar ----------------
def linhas_1764(C):
    d = [C["s07.a"], C["s07.b"], C["s07.c"], C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]]
    return [(x,) for x in d], d[1:], d[:6]


def b_fatorar(c, t, C, b):
    tn, tp, tb = linhas_1764(C)
    tabela(c, t, T1764_TELA, tn, tp, tb, G, cor_fim=CERTO if t >= tn[-1][0] + 0.5 else None)
    x = 930
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    fim = C["s08.end"] + 0.2

    def titulo():
        E.frase(c, t, C["s07"] + 0.1, ps("número grande?", "i", 110), x, 290, passo=0.16)
        E.frase(c, t, lerp(C["s07"], a7, 0.6), ps("fatore", "g", 150, COR), x, 470)
    E.saida(c, t, a8 - 0.1, titulo)
    y = 780
    troca(c, t, [(a7, "1.764 é par"), (b7, "1.764 ÷ 2 = 882"), (c7, "882 ÷ 2 = 441"), (lerp(C["s08"], a8, 0.05), "441 é ímpar"),
                 (lerp(C["s08"], a8, 0.45), "4 + 4 + 1 = 9"), (a8, "441 ÷ 3 = 147"), (b8, "147 ÷ 3 = 49"), (c8, "49 ÷ 7 = 7"), (d8, "7 ÷ 7 = 1")], fim, x, y, 88)


# ---------------- duplas ----------------
def b_duplas(c, t, C, b):
    x = 840
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")

    def coluna():
        tabela(c, t, T1764_TELA, [(-1.0,)] * 7, [-1.0] * 6, [-1.0] * 6, G, cor_fim=CERTO)
        if t < b9:
            q = ep(t, a9, 0.4) * (1 - ep(t, b9 - 0.2, 0.2))
            E.caixa_pontilhada(c, G["xp"] - 62, 118, 124, 6 * G["dy"] + 8, q, COR, prog_=q)
        dupla(c, t, c9, 0)
        dupla(c, t, d9, 2)
        dupla(c, t, e9, 4)
    E.saida(c, t, C["s11"] - 0.1, coluna)

    def texto():
        E.frase(c, t, a9, ps("a coluna dos", "i", 96) + ps("divisores", "g", 88, COR), x, 280, passo=0.16)
        E.frase(c, t, b9, ps("cada primo veio", "i", 92) + ps("em dupla", "g", 84, COR), x, 420, passo=0.16)
        for i, (ti, s) in enumerate(((c9, "dupla de 2"), (d9, "dupla de 3"), (e9, "dupla de 7"))):
            E.foco(c, t, ti + 0.1, 0.4, lambda p: E.escreve(c, s, x, 580 + i * 110, 80, "b", TINTA, p))
    E.saida(c, t, C["s10"] - 0.1, texto)

    if C["s10"] <= t:
        def grupos():
            E.frase(c, t, a0, ps("dois grupos", "g", 88, COR) + ps("iguais", "i", 96), x, 240, passo=0.16)
            for i, gx in enumerate((x, x + 450)):
                q = ep(t, a0 + 0.3 + i * 0.2, 0.45)
                E.caixa_pontilhada(c, gx, 310, 400, 220, q, prog_=q)
                E.foco(c, t, a0 + 0.4 + i * 0.2, 0.4, lambda p: centro(c, f"grupo {i + 1}", gx + 200, 380, 52, "i", TINTA2, p))
                for j, n in enumerate("237"):
                    E.foco(c, t, b0 + 0.1 + j * 0.25, 0.4, lambda p: centro(c, n, gx + 90 + j * 110, 490, 90, "g", COR, p))
            E.frase(c, t, b0 + 0.5, ps("um primo de cada dupla", "i", 72), x, 640, passo=0.12)
            form(c, t, c0, "2 × 3 × 7 =", x, 860, 104)
            E.foco(c, t, d0, 0.5, lambda p: num_bola(c, "42", 1610, 825, 118, 120, p))
        E.saida(c, t, C["s11"] - 0.1, grupos)

    if t >= C["s11"]:
        a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
        E.frase(c, t, C["s11"] + 0.1, ps("sempre confira", "i", 104, COR), W / 2, 200, "center")
        form(c, t, a1, "42^2", 470, 640, 230, None, "center")
        x1, xi, xr = 880, 1240, 1740
        for y, ti, s, v in ((430, b1, "42 × 40", "1.680"), (570, c1, "42 × 2", "84")):
            E.foco(c, t, ti, 0.45, lambda p: (E.escreve(c, s, x1, y, 92, "b", TINTA, p), E.escreve(c, "=", xi, y, 92, "b", TINTA, p), direita(c, v, xr, y, 104, COR, p)))
        if t >= d1 - 0.1:
            p = ep(t, d1 - 0.1, 0.4)
            M.line(c, 1340, 610, xr + 8, 610, TINTA, 1.0, 6, progress=p)
            E.foco(c, t, d1 - 0.1, 0.4, lambda q: E.escreve(c, "+", 1350, 570, 90, "g", TINTA2, q))
        E.foco(c, t, d1, 0.5, lambda p: direita(c, "1.764", xr, 730, 124, CERTO, p))
        ti = lerp(d1, C["s11.end"], 0.72)
        E.foco(c, t, ti, 0.45, lambda p: E.selo(c, 900, 720, 62, True, p))
        E.frase(c, t, ti, ps("bateu", "g", 96, CERTO), 990, 752)


# ---------------- estimar ----------------
def b_estimar(c, t, C, b):
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]

    def fator():
        form(c, t, a2, "r{20}", XE + 40, 380, 170, COR)
        s = 130
        xf = 700
        E.sinal(c, t, b2 - 0.1, "=", 640, 325, 120)
        w = E.formula(c, "2 × 2 × ", 0, 0, s, a=0)
        form(c, t, b2, "2 × 2 × ", xf, 380, s)
        form(c, t, b2 + 0.3, "5", xf + w, 380, s, ERRADO if t >= c2 else None)
        q = ep(t, c2, 0.45)
        E.caixa_pontilhada(c, xf + w - 18, 262, 112, 148, q, ERRADO, prog_=q)
        E.frase(c, t, c2 + 0.1, ps("ficou sem dupla", "g", 84, ERRADO), xf + w + 56, 512, "center")
        E.frase(c, t, lerp(c2, C["s12.end"], 0.35), ps("a raiz", "i", 96) + ps("não é exata", "g", 88), W / 2, 700, "center", 0.16)
        E.frase(c, t, lerp(c2, C["s12.end"], 0.82), ps("vamos", "i", 120) + ps("cercar", "g", 116, COR), W / 2, 880, "center")
    E.saida(c, t, C["s13"] - 0.1, fator)

    if C["s13"] <= t < C["s14"] + 0.4:
        a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]

        def cerca():
            form(c, t, a3, "4^2 = 16", 240, 310, 130)
            form(c, t, b3, "5^2 = 25", 240, 500, 130)
            form(c, t, lerp(b3, c3, 0.45), "16 < 20 < 25", 1000, 400, 120)
            E.frase(c, t, c3, ps("a raiz de 20 fica entre 4 e 5", "i", 76), W / 2, 680, "center", 0.12)
            form(c, t, c3 + 0.4, "4 < r{20} < 5", W / 2, 900, 150, COR, "center")
        E.saida(c, t, C["s14"] - 0.1, cerca)

    if t >= C["s14"]:
        a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
        a5, b5 = C["s15.a"], C["s15.b"]
        s0 = C["s14"]
        x0, x1, y = 340, 1580, 300
        t1, t2 = lerp(s0, a4, 0.1), lerp(s0, a4, 0.55)
        vx = E.reta(c, t, s0, x0, x1, y, 16, 25, [16, 20, 25], size=64, tm=[t1, t1 + 0.4, t2 + 0.4])
        E.salto(c, t, t1 + 0.1, vx(16), vx(20), y - 14, 96, rotulo="4", size=64)
        E.salto(c, t, t2, vx(20), vx(25), y - 14, 96, rotulo="5", size=64)

        def teste1():
            E.frase(c, t, a4, ps("20 fica", "i", 92) + ps("quase no meio", "g", 86, COR), W / 2, 500, "center", 0.16)
            E.frase(c, t, lerp(a4, b4, 0.4), ps("o meio entre 4 e 5:", "i", 92), 420, 650, passo=0.12)
            form(c, t, b4, "4,5", 1190, 650, 120, COR)
            form(c, t, c4, "4,5 × 4,5 = 20,25", W / 2, 830, 124, None, "center")
            E.frase(c, t, lerp(c4, C["s14.end"], 0.72), ps("passou um", "i", 84) + ps("pouquinho", "g", 78, ERRADO), W / 2, 960, "center", 0.16)
        E.saida(c, t, C["s15"] - 0.1, teste1)

        if t >= C["s15"]:
            E.foco(c, t, C["s15"], 0.4, lambda p: E.formula(c, "4,5^2 = 20,25", 240, 560, 96, cor=TINTA, a=p))
            E.foco(c, t, a5, 0.45, lambda p: E.formula(c, "4,4^2 = 19,36", 240, 700, 96, cor=TINTA, a=p))
            E.frase(c, t, lerp(a5, b5, 0.62), ps("mais longe de 20", "i", 78, ERRADO), 1000, 700, passo=0.12)
            form(c, t, b5, "r{20} ≈ 4,5", 240, 910, 130, COR)
            E.frase(c, t, lerp(b5, C["s15.end"], 0.5), ps("valor", "i", 96) + ps("aproximado", "g", 88, COR), 1000, 900, passo=0.16)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_ = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    fim = C["s16.end"]
    E.frase(c, t, C["s16"] + 0.1, ps("o erro mais comum:", "i", 92), W / 2 - 310, 170, "center", 0.14)
    E.frase(c, t, a_, ps("dividir por 2", "g", 88, ERRADO), W / 2 + 370, 170, "center", 0.14)
    form(c, t, b_, "r{16} = 8", 530, 410, 130, ERRADO, "center")
    if t >= c_:
        E.risco(c, 330, 440, 760, 290, t, c_ + 0.3, largura=12)
    form(c, t, c_, "8 × 8 = 64", 1330, 410, 130, None, "center")
    form(c, t, d_, "r{16} = 4", 530, 620, 130, CERTO, "center")
    E.foco(c, t, d_ + 0.2, 0.45, lambda p: E.selo(c, 860, 575, 60, True, p))
    E.frase(c, t, lerp(d_, fim, 0.25), ps("raiz quadrada", "i", 96) + ps("não é metade", "g", 92, ERRADO), W / 2, 800, "center", 0.16)
    tq = lerp(d_, fim, 0.62)
    form(c, t, tq, "r{4} = 2", 330, 960, 96)
    E.frase(c, t, tq + 0.2, ps("a metade só acerta aqui, por coincidência", "i", 62), 720, 950, passo=0.1)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def cerco():
        a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]
        E.frase(c, t, C["s17"] + 0.1, ps("agora, o atalho", "i", 88, CLARO), W / 2, 170, "center")
        E.frase(c, t, a7, ps("cerque com", "i", 110, BR) + ps("dezenas", "g", 104, BR), W / 2, 330, "center", 0.2)
        form(c, t, b7, "40^2 = 1.600", 530, 570, 110, BR, "center")
        form(c, t, c7, "50^2 = 2.500", 1390, 570, 110, BR, "center")
        form(c, t, lerp(c7, C["s17.end"], 0.45), "40 < r{1.764} < 50", W / 2, 840, 140, CLARO, "center")
    E.saida(c, t, C["s18"] - 0.1, cerco)

    if C["s18"] <= t:
        def final():
            a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
            E.frase(c, t, a8, ps("olhe o", "i", 104, CLARO) + ps("final", "g", 100, BR), XE + 40, 210, passo=0.2)
            s = 230
            xn = XE + 40
            E.foco(c, t, a8 + 0.1, 0.45, lambda p: E.formula(c, "1.76", xn, 480, s, cor=BR, a=p))
            w = E.formula(c, "1.76", 0, 0, s, a=0)
            E.foco(c, t, a8 + 0.5, 0.45, lambda p: E.formula(c, "4", xn + w, 480, s, cor=CLARO, a=p))
            form(c, t, b8, "2^2 = 4", 1030, 330, 110, BR)
            form(c, t, b8 + 0.5, "8^2 = 64", 1030, 480, 110, BR)
            E.frase(c, t, b8 + 0.8, ps("termina em 2 ou em 8", "i", 84, CLARO), 960, 620, passo=0.13)
            form(c, t, lerp(b8, c8, 0.6), "42 ou 48?", XE + 40, 800, 130, BR)
            E.frase(c, t, c8, ps("mais perto de 1.600", "i", 84, CLARO), XE + 40, 940, passo=0.13)
            E.foco(c, t, c8 + 0.2, 0.5, lambda p: num_bola(c, "42", 1400, 810, 140, 140, p, E.COR, BR))
        E.saida(c, t, C["s19"] - 0.1, final)

    if t >= C["s19"]:
        a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]
        E.frase(c, t, a9, ps("o último algarismo do produto", "i", 92, CLARO), W / 2, 260, "center", 0.13)
        E.frase(c, t, a9 + 1.0, ps("depende só dos", "i", 92, CLARO) + ps("últimos algarismos", "g", 84, BR), W / 2, 380, "center", 0.13)
        E.frase(c, t, b9, ps("só serve se a", "i", 104, CLARO) + ps("raiz for exata", "g", 96, BR), W / 2, 620, "center", 0.17)
        linha(c, t, [("sem essa certeza:", "i", 110, CLARO, lerp(b9, c9, 0.45)), ("fatore", "g", 130, BR, c9 - 0.1)], W / 2, 860, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_ = C["s20.a"], C["s20.b"]
    E.frase(c, t, C["s20"] + 0.1, ps("hora de testar", "i", 84, COR), XE, 220)
    form(c, t, a_, "r{784} = ?", XE, 520, 190, None)
    E.frase(c, t, lerp(a_, b_, 0.8), ps("fatore", "g", 100, COR), XE, 780)
    E.frase(c, t, b_, ps("e confira no fim", "i", 100), XE, 900, passo=0.16)
    E.relogio(c, t, C["s21.a"], 1490, 460, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    s0 = C["s22"]
    d = [lerp(s0, C["s22.a"], 0.4)] + [C[f"s22.{k}"] for k in "abcdef"]
    tn = [(x,) for x in d]
    tabela(c, t, T784, tn, d[1:], d[:6], G, cor_fim=CERTO if t >= d[-1] + 0.5 else None)
    a3, b3, c3, d3, e3 = (C[f"s23.{k}"] for k in "abcde")
    x = 900
    conta = [(d[1], "784 ÷ 2 = 392"), (d[2], "392 ÷ 2 = 196"), (d[3], "196 ÷ 2 = 98"), (d[4], "98 ÷ 2 = 49"), (d[5], "49 ÷ 7 = 7"), (d[6], "7 ÷ 7 = 1")]
    troca(c, t, conta, C["s23"] - 0.1, x, 540, 100)
    dupla(c, t, a3, 0)
    dupla(c, t, a3 + 0.4, 2)
    dupla(c, t, b3, 4)
    E.foco(c, t, a3, 0.45, lambda p: E.escreve(c, "duas duplas de 2", x, 270, 80, "b", TINTA, p))
    E.foco(c, t, b3, 0.45, lambda p: E.escreve(c, "uma dupla de 7", x, 390, 80, "b", TINTA, p))
    form(c, t, c3, "2 × 2 × 7 =", x, 620, 104)
    E.foco(c, t, d3, 0.5, lambda p: num_bola(c, "28", 1610, 585, 112, 116, p))
    form(c, t, e3, "28^2 = 784", x, 860, 130, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"] + 0.1, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        itens = ((470, "s24.a", ps("raiz exata:", "g", 92, COR) + ps("duplas de primos", "i", 100)),
                 (720, "s24.b", ps("não exata:", "g", 92, COR) + ps("cerca e confere", "i", 100)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda p: num_bola(c, str(i + 1), 330, y - 30, 58, 66, p))
            E.frase(c, t, C[k] + 0.1, partes, 430, y, passo=0.16)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    a_, b_, c_, d_, e_ = (C[f"s25.{k}"] for k in "abcde")
    E.frase(c, t, C["s25"] + 0.2, ps("próxima aula", "i", 84), XE, 240)
    E.frase(c, t, a_, ps("fração", "g", 96, COR) + ps("e", "i", 96) + ps("decimal", "g", 96, COR), XE, 390, passo=0.15)
    E.frase(c, t, b_, ps("raiz cúbica", "g", 96, COR), XE, 520, passo=0.15)
    E.frase(c, t, c_, ps("número negativo", "g", 96, COR), XE, 650, passo=0.15)
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1460, 340, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, d_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1610, p), lerp(650, 385, p), ep(t, d_ + 0.2, 0.4), TINTA)
    E.frase(c, t, e_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, sinal=b_sinal, fatorar=b_fatorar, duplas=b_duplas, estimar=b_estimar,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
