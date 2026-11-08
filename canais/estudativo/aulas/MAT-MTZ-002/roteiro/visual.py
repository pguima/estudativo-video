"""Visual — Estudativo · MAT-MTZ-002: multiplicar matrizes, linha por coluna. Segue a linguagem de MAT-MTZ-001:
linha em índigo, coluna em âmbar, E.matriz e E.matriz_marca; resultado em verde ou na esfera; atalho no palco escuro.
A conta de cada elemento aparece embaixo, com o par da linha em índigo e o da coluna em âmbar."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matrizes e Sistemas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-MTZ-002_multiplicar_matrizes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("lanche", "produto", "tamanho", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
LIN, COL = COR, "#D98A00"


def mult(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]


A, B = [[1, 2], [0, 1]], [[1, 0], [3, 1]]
AB, BA = mult(A, B), mult(B, A)
assert AB == [[7, 2], [3, 1]] and BA == [[1, 2], [3, 7]]
assert [[A[i][j] * B[i][j] for j in range(2)] for i in range(2)] == [[1, 0], [0, 1]]
assert 2 * 8 + 3 * 5 == 31
QA, QB = [[2, 1], [0, 3]], [[1, 4], [2, 0]]
QR = mult(QA, QB)
assert QR == [[4, 8], [6, 0]]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def conta(c, t, t0, X, Y, i, j, x, y, size=72, cor_r=CERTO, escuro=False):
    """a conta do elemento ij: x1·y1 + x2·y2 = r, com a linha em índigo e a coluna em âmbar"""
    tinta = BR if escuro else TINTA
    lin, col = (CLARO, "#FFB833") if escuro else (LIN, COL)
    partes = []
    for k in range(len(Y)):
        if k:
            partes.append((" + ", tinta))
        partes += [(E._num(X[i][k]), lin), ("·", tinta), (E._num(Y[k][j]), col)]
    r = sum(X[i][k] * Y[k][j] for k in range(len(Y)))
    partes += [(" = ", tinta), (E._num(r), cor_r)]

    def desenha(a):
        xx = x
        for s, cc in partes:
            E.escreve(c, s, xx, y, size, "g", cc, a)
            xx += E.larg(s, "g", size) + size * 0.04
    E.foco(c, t, t0, 0.5, desenha)


def rot(c, t, t0, G, txt, cor=TINTA, size=64):
    """nome da matriz acima dela"""
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, txt, (G.x0 + G.x1) / 2, G.y0 - 28, size, "g", cor, a, "center"))


def par(c, t, GA, GB, GR, i, j, t0, t1, p_r=True):
    """faixa na linha i de A, na coluna j de B e no elemento ij do resultado, entre t0 e t1"""
    if t0 <= t < t1:
        E.matriz_marca(c, GA, linha=i, cor=LIN, p=ep(t, t0, 0.4))
        E.matriz_marca(c, GB, coluna=j, cor=COL, p=ep(t, t0 + 0.2, 0.4))
        if p_r:
            E.matriz_marca(c, GR, i, j, CERTO, 1, ep(t, t0 + 0.4, 0.4), cheia=0.0)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        y, s = 470, 120
        E.matriz(c, t, C["s01.a"], A, 380, y, s, nome="A" if False else None)
        E.sinal(c, t, C["s01.a"] + 0.3, "·", 640, y - 10, 120)
        E.matriz(c, t, C["s01.a"] + 0.4, B, 900, y, s)
        E.sinal(c, t, C["s01.b"], "=", 1160, y - 10, 110)
        errado = t < C["s01.d"]
        if errado:
            E.matriz(c, t, C["s01.b"] + 0.2, [[1, 0], [0, 1]], 1450, y, s, cores={(i, j): ERRADO for i in range(2) for j in range(2)})
            E.frase(c, t, C["s01.b"], ps("elemento com elemento?", "i", 76, ERRADO), W / 2, 820, "center")
            if t >= C["s01.c"]:
                E.risco(c, 1300, 620, 1600, 320, t, C["s01.c"], largura=16)
        else:
            E.matriz(c, t, C["s01.d"], AB, 1450, y, s, cores={(i, j): CERTO for i in range(2) for j in range(2)})
            E.frase(c, t, C["s01.d"], [("linha", "g", 96, LIN), ("por", "i", 100), ("coluna", "g", 96, COL)], W / 2, 820, "center")
            E.foco(c, t, C["s01.e"], 0.5, lambda a: E.centro(c, "AB ≠ BA", W / 2, 980, 90, "g", COR, a))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 360)
        E.frase(c, t, C["s02.a"] + 1.0, [("multiplicar", "g", 120, COR)], XE, 520)
        E.frase(c, t, C["s02.a"] + 1.4, [("matrizes", "g", 120)], XE, 660)
        E.frase(c, t, C["s02.a"] + 2.2, ps("e saber se existe", "i", 84), XE, 800)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 84), XE, 300)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE, 600, 320, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 210, 580, 120, "i", TINTA, a))
    x, w = 960, 780
    for i, (k, l1, l2) in enumerate((("s03.b", "tamanho =", "linhas × colunas"), ("s03.c", "aᵢⱼ =", "linha i, coluna j"))):
        y = 280 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.foco(c, t, C[k] + 0.1, 0.5, lambda a, l1=l1, y=y: E.formula(c, l1, x + 44, y + 95, 66, "b", TINTA, a))
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 64, COR)], x + 44, y + 180)


# ---------------- lanchonete ----------------
def b_lanche(c, t, C, b):
    E.frase(c, t, C["s04"], ps("na lanchonete", "i", 84), XE, 190)
    y = 470
    GP = E.matriz(c, t, C["s04.a"], [[2, 3]], 520, y, 130, gap=150)
    E.foco(c, t, C["s04.a"], 0.5, lambda a: (E.centro(c, "sanduíche", GP.x[0], y - 120, 44, "i", TINTA2, a),
                                              E.centro(c, "suco", GP.x[1], y - 120, 44, "i", TINTA2, a)))
    E.foco(c, t, C["s04.a"] + 0.3, 0.5, lambda a: E.centro(c, "pedido", 520, y + 160, 56, "g", LIN, a))
    GQ = E.matriz(c, t, C["s04.b"], [[8], [5]], 1150, y, 130)
    E.foco(c, t, C["s04.b"], 0.5, lambda a: (E.escreve(c, "R$", GQ.x1 + 30, GQ.y[0] + 20, 50, "i", TINTA2, a),
                                              E.escreve(c, "R$", GQ.x1 + 30, GQ.y[1] + 20, 50, "i", TINTA2, a)))
    E.foco(c, t, C["s04.b"] + 0.3, 0.5, lambda a: E.centro(c, "preço", 1150, GQ.y1 + 90, 56, "g", COL, a))
    if t >= C["s05.c"]:
        E.matriz_marca(c, GP, linha=0, cor=LIN, p=ep(t, C["s05.c"], 0.5))
    if t >= C["s05.d"]:
        E.matriz_marca(c, GQ, coluna=0, cor=COL, p=ep(t, C["s05.d"], 0.5))
    E.foco(c, t, C["s05.a"], 0.5, lambda a: E.formula(c, "2 · 8 + 3 · 5", XE, 900, 96, "g", TINTA, a))
    E.foco(c, t, C["s05.b"], 0.5, lambda a: E.formula(c, "= 16 + 15 = 31", XE + 700, 900, 96, "g", CERTO, a))
    if t >= C["s06"]:
        for k, (i, xs) in enumerate(((0, "s06.a"), (1, "s06.b"))):
            p = ep(t, C[xs], 0.6)
            if p > 0:
                M.arrow(c, GP.x[i], y + 70, lerp(GP.x[i], GQ.x0 - 10, p), lerp(y + 70, GQ.y[i], p), TINTA2, 0.8, 5, 16, p)
        E.foco(c, t, C["s06.c"], 0.5, lambda a: E.pilula(c, "linha × coluna", 1560, 330, 54, estilo="g", a=a))


# ---------------- produto ----------------
YP, SP = 420, 112
XA, XB, XR = 330, 800, 1450


def b_produto(c, t, C, b):
    GA = E.matriz(c, t, C["s07.a"], A, XA, YP, SP)
    rot(c, t, C["s07.a"], GA, "A")
    E.sinal(c, t, C["s07.b"] - 0.2, "·", 565, YP - 10, 110)
    GB = E.matriz(c, t, C["s07.b"], B, XB, YP, SP)
    rot(c, t, C["s07.b"], GB, "B")
    E.sinal(c, t, C["s07.c"], "=", 1060, YP - 10, 100)
    ks = ("s08.b", "s09.b", "s10.b", "s10.d")
    tc = {(n // 2, n % 2): C[k] for n, k in enumerate(ks)}
    GR = E.matriz(c, t, C["s07.c"], AB, XR, YP, SP, tc=tc, cores={(i, j): CERTO for i in range(2) for j in range(2)})
    for n, k in enumerate(ks):
        i, j = divmod(n, 2)
        if t < C[k]:
            E.foco(c, t, C["s07.c"], 0.4, lambda a, i=i, j=j: E.centro(c, "?", GR.x[j], GR.y[i] + SP * 0.36, SP, "g", CINZA, a))
    inicios = (C["s08.a"], C["s09.a"], C["s10.a"], C["s10.c"])
    fins = (C["s09.a"], C["s10.a"], C["s10.c"], C["s11"])
    for n in range(4):
        i, j = divmod(n, 2)
        par(c, t, GA, GB, GR, i, j, inicios[n], fins[n])
        E.saida(c, t, fins[n] - 0.05, lambda n=n, i=i, j=j: conta(c, t, inicios[n] + 0.4, A, B, i, j, 560, 820, 96))
    if t >= C["s11"]:
        E.frase(c, t, C["s11.b"], [("linha", "g", 70, LIN), ("i", "g", 70, LIN), ("de", "i", 76), ("A", "g", 70), ("com", "i", 76),
                                   ("coluna", "g", 70, COL), ("j", "g", 70, COL), ("de", "i", 76), ("B", "g", 70)], W / 2, 800, "center", passo=0.12)
        E.foco(c, t, C["s11.b"] + 1.8, 0.5, lambda a: E.formula(c, "→ elemento aᵢⱼ", W / 2, 940, 76, "g", CERTO, a, "center"))
        rot(c, t, C["s11.a"], GR, "AB", CERTO)


# ---------------- a ordem ----------------
def b_ordem(c, t, C, b):
    y, s = 430, 104
    E.frase(c, t, C["s12"], ps("troque a ordem", "i", 80), XE, 170)
    GB = E.matriz(c, t, C["s12.a"], B, 330, y, s)
    rot(c, t, C["s12.a"], GB, "B")
    E.sinal(c, t, C["s12.a"] + 0.2, "·", 560, y - 10, 100)
    GA = E.matriz(c, t, C["s12.a"] + 0.3, A, 790, y, s)
    rot(c, t, C["s12.a"] + 0.3, GA, "A")
    E.sinal(c, t, C["s12.a"] + 0.5, "=", 1040, y - 10, 100)
    GR = E.matriz(c, t, C["s12.c"], BA, 1400, y, s, tc={(0, 0): C["s12.b"] + 1.2}, tm=C["s12.b"],
                  cores={(i, j): COR for i in range(2) for j in range(2)})
    par(c, t, GB, GA, GR, 0, 0, C["s12.b"], C["s12.c"])
    E.saida(c, t, C["s12.c"], lambda: conta(c, t, C["s12.b"] + 0.4, B, A, 0, 0, 560, 760, 90, COR))
    if t >= C["s13"]:
        y2 = 820
        E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "AB =", 300, y2 + 30, 80, "g", CERTO, a, "right"))
        E.matriz(c, t, C["s13.a"], AB, 470, y2, 84, cores={(i, j): CERTO for i in range(2) for j in range(2)})
        E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "BA =", 990, y2 + 30, 80, "g", COR, a, "right"))
        E.matriz(c, t, C["s13.b"], BA, 1160, y2, 84, cores={(i, j): COR for i in range(2) for j in range(2)})
        E.foco(c, t, C["s13.c"], 0.5, lambda a: E.escreve(c, "≠", 690, y2 + 50, 140, "g", ERRADO, a))
        E.foco(c, t, C["s13.c"] + 0.4, 0.5, lambda a: E.pilula(c, "a ordem importa", 1600, y2, 50, estilo="g", fundo=ERRADO, a=a))


# ---------------- tamanho ----------------
def b_tamanho(c, t, C, b):
    E.frase(c, t, C["s14"], ps("quando o produto existe?", "i", 84), XE, 190)
    y = 460
    # uma linha de A com 3 números encontra uma coluna de B com 3 números
    GL = E.matriz(c, t, C["s14.a"], [["•", "•", "•"]], 520, y, 110, cores={("c", j): LIN for j in range(3)})
    GC = E.matriz(c, t, C["s14.a"] + 0.4, [["•"], ["•"], ["•"]], 1050, y, 90, cores={("c", 0): COL})
    E.foco(c, t, C["s14.a"] + 0.2, 0.5, lambda a: E.centro(c, "linha de A", 520, y + 130, 52, "g", LIN, a))
    E.foco(c, t, C["s14.a"] + 0.6, 0.5, lambda a: E.escreve(c, "coluna de B", GC.x1 + 40, y + 20, 52, "g", COL, a))
    if t >= C["s14.a"] + 0.8:
        for k in range(3):
            p = ep(t, C["s14.a"] + 0.8 + 0.25 * k, 0.5)
            M.line(c, GL.x[k], y, lerp(GL.x[k], GC.x[0], p), lerp(y, GC.y[k], p), TINTA2, 0.5, 3, dash=[10, 8])
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.escreve(c, "3 com 3: cada um tem par", XE, 720, 60, "i", TINTA2, a))
    E.foco(c, t, C["s15.a"], 0.5, lambda a: (E.escreve(c, "colunas de A", XE, 880, 72, "g", LIN, a),
                                              E.escreve(c, "=", XE + 540, 880, 72, "g", TINTA, a),
                                              E.escreve(c, "linhas de B", XE + 620, 880, 72, "g", COL, a)))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.escreve(c, "resultado: linhas de A × colunas de B", XE, 1000, 56, "b", CERTO, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s16"], [("cuidado", "g", 104, ERRADO), ("com", "i", 96), ("isto", "i", 96)], XE, 190)
    E.frase(c, t, C["s16.a"], ps("elemento com elemento", "i", 76, ERRADO), XE, 300)
    y, s = 580, 100
    E.matriz(c, t, C["s16.a"], A, 270, y, s)
    E.sinal(c, t, C["s16.a"] + 0.2, "·", 460, y - 10, 100)
    E.matriz(c, t, C["s16.a"] + 0.3, B, 650, y, s)
    E.sinal(c, t, C["s16.b"] - 0.2, "=", 850, y - 10, 100)
    E.matriz(c, t, C["s16.b"], [[1, 0], [0, 1]], 1070, y, s, cores={(i, j): ERRADO for i in range(2) for j in range(2)})
    if t >= C["s16.c"]:
        E.risco(c, 930, 720, 1210, 440, t, C["s16.c"], largura=14)
        E.foco(c, t, C["s16.c"] + 0.3, 0.5, lambda a: E.escreve(c, "certo:", 1300, y + 20, 56, "i", CERTO, a))
        E.matriz(c, t, C["s16.c"] + 0.3, AB, 1620, y, s, cores={(i, j): CERTO for i in range(2) for j in range(2)})
    E.frase(c, t, C["s16.d"], [("sempre", "i", 96), ("linha", "g", 90, LIN), ("com", "i", 96), ("coluna", "g", 90, COL)], W / 2, 920, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    CL, CC = CLARO, "#FFB833"
    E.frase(c, t, C["s17"], [("o", "i", 84, CLARO), ("atalho", "i", 84, CLARO), ("do", "i", 84, CLARO), ("tamanho", "g", 76, BR)], XE, 190)

    def tamanhos(t0, a_, b_, c_, d_, y, ok, t_ok, t_fora=None):
        x = 330
        s = 150
        parts = [(a_, BR), ("×", CLARO), (b_, CC), ("   ·   ", CLARO), (c_, CC), ("×", CLARO), (d_, BR)]
        xs = []
        xx = x
        for txt, _ in parts:
            xs.append(xx)
            xx += E.larg(txt, "g", s) + 20

        def desenha(a):
            for (txt, cc), x_ in zip(parts, xs):
                E.escreve(c, txt, x_, y, s, "g", cc, a)
        E.foco(c, t, t0, 0.5, desenha)
        if t >= t_ok:
            m1, m2 = xs[2] + E.larg(b_, "g", s) / 2, xs[4] + E.larg(c_, "g", s) / 2
            p = ep(t, t_ok, 0.6)
            E.chave(c, m1, m2, y + 40, CC if ok else E.ERRADO, p, 40, 6)
            E.foco(c, t, t_ok + 0.3, 0.5, lambda a: E.centro(c, "iguais: existe" if ok else "diferentes: não existe", (m1 + m2) / 2, y + 150, 60, "b",
                                                            CC if ok else E.ERRADO, a))
        if t_fora is not None and t >= t_fora:
            f1, f2 = xs[0] + E.larg(a_, "g", s) / 2, xs[6] + E.larg(d_, "g", s) / 2
            p = ep(t, t_fora, 0.6)
            E.chave(c, f1, f2, y - s * 0.85, BR, p, -40, 6)
            E.foco(c, t, t_fora + 0.3, 0.5, lambda a: E.centro(c, "resultado: 2 × 4", (f1 + f2) / 2, y - s * 0.85 - 70, 64, "g", BR, a))

    def parte1():
        tamanhos(C["s17.b"], "2", "3", "3", "4", 600, True, C["s17.c"], C["s17.d"])
    E.saida(c, t, C["s18.b"] - 0.1, parte1)
    E.foco(c, t, C["s18.a"], 0.5, lambda a: E.escreve(c, "os do meio se encontram", XE, 900, 70, "i", CLARO, a))
    if t >= C["s18.b"]:
        tamanhos(C["s18.b"] + 1.0, "3", "4", "2", "3", 600, False, C["s18.c"])


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 200)
    y, s = 520, 120
    rot(c, t, C["s19.a"], E.matriz(c, t, C["s19.a"], QA, 420, y, s), "A", size=80)
    rot(c, t, C["s19.b"], E.matriz(c, t, C["s19.b"], QB, 960, y, s), "B", size=80)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.formula(c, "A · B = ?", XE, 900, 130, "g", COR, a))
    E.relogio(c, t, C["s20.a"], cx=1560, cy=470, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    y, s = 400, 104
    GA = E.matriz(c, t, C["s21"], QA, 320, y, s)
    rot(c, t, C["s21"], GA, "A")
    E.sinal(c, t, C["s21"] + 0.2, "·", 545, y - 10, 100)
    GB = E.matriz(c, t, C["s21"] + 0.3, QB, 790, y, s)
    rot(c, t, C["s21"] + 0.3, GB, "B")
    E.sinal(c, t, C["s21"] + 0.5, "=", 1040, y - 10, 100)
    ks = ("s21.a", "s21.b", "s22.a", "s22.b")
    fins = (C["s21.b"], C["s22"], C["s22.b"], C["s22.c"])
    tc = {(n // 2, n % 2): C[k] + 2.6 for n, k in enumerate(ks)}
    GR = E.matriz(c, t, C["s21"] + 0.6, QR, 1380, y, s, tc=tc, cores={(i, j): CERTO for i in range(2) for j in range(2)})
    for n, k in enumerate(ks):
        i, j = divmod(n, 2)
        if t < C[k] + 2.6:
            E.foco(c, t, C["s21"] + 0.6, 0.4, lambda a, i=i, j=j: E.centro(c, "?", GR.x[j], GR.y[i] + s * 0.36, s, "g", CINZA, a))
        par(c, t, GA, GB, GR, i, j, C[k], fins[n])
        E.saida(c, t, fins[n] - 0.05, lambda n=n, i=i, j=j, k=k: conta(c, t, C[k] + 0.6, QA, QB, i, j, 560, 800, 96))
    if t >= C["s22.c"]:
        rot(c, t, C["s22.c"], GR, "A · B", CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s23.a", "linha com coluna"), ("s23.b", "par a par e soma"), ("s23.c", "a ordem importa"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 470, y - 30, 56, a=a), E.centro(c, str(i + 1), 470, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 100)], 570, y)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], ps("próxima aula", "i", 84), XE, 330)
    E.frase(c, t, C["s24.a"], [("Determinante", "g", 140, COR)], XE, 490)
    E.frase(c, t, C["s24.b"], [("e", "i", 120), ("Sarrus", "g", 140, COR)], XE, 640)
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, lanche=b_lanche, produto=b_produto, ordem=b_ordem, tamanho=b_tamanho,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
