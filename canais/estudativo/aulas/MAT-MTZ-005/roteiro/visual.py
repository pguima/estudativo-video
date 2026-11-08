"""Visual — Estudativo · MAT-MTZ-005: prática de matrizes e determinantes (4 questões). Reúne as peças de MAT-MTZ-001 a 004:
linha em índigo e coluna em âmbar; o que desce em índigo e o que sobe em âmbar (sarrus()); a inversa que se monta no lugar
(inv_passos()); resultado em verde. Cada questão tem o selo "questão N" e o relógio de pausa."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matrizes e Sistemas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-MTZ-005_praticando_matrizes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "atalho", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
LIN, COL = COR, "#D98A00"
DESCE, SOBE = COR, "#D98A00"


def mult(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]


def diags(m):
    d = [m[0][k] * m[1][(k + 1) % 3] * m[2][(k + 2) % 3] for k in range(3)]
    u = [m[2][k] * m[1][(k + 1) % 3] * m[0][(k + 2) % 3] for k in range(3)]
    return d, u


# questão 1
A1 = [[i * j for j in (1, 2)] for i in (1, 2)]
B1 = [[1, -1], [0, 2]]
T1 = [list(r) for r in zip(*A1)]
R1 = [[T1[i][j] + 3 * B1[i][j] for j in range(2)] for i in range(2)]
assert A1 == [[1, 2], [2, 4]] and T1 == A1 and R1 == [[4, -1], [2, 10]]
# questão 2
A2, B2 = [[1, 2], [3, -1]], [[2, 0], [1, 4]]
R2 = mult(A2, B2)
assert R2 == [[4, 8], [5, -4]]
# questão 3
M3 = [[1, 0, 2], [-1, 3, 1], [2, 1, 0]]
assert diags(M3) == ([0, 0, -2], [12, 1, 0]) and sum(diags(M3)[0]) - sum(diags(M3)[1]) == -15
# questão 4
A4, I4 = [[3, 1], [5, 2]], [[2, -1], [-5, 3]]
assert A4[0][0] * A4[1][1] - A4[0][1] * A4[1][0] == 1 and mult(A4, I4) == [[1, 0], [0, 1]]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def verde(n=2):
    return {(i, j): CERTO for i in range(n) for j in range(n)}


def rot(c, t, t0, G, txt, cor=TINTA, size=64):
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, txt, (G.x0 + G.x1) / 2, G.y0 - 28, size, "g", cor, a, "center"))


def selo_q(c, t, t0, n):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, f"questão {n}", XE + 150, 150, 52, estilo="g", a=a))


def conta(c, t, t0, X, Y, i, j, x, y, size=72):
    partes = []
    for k in range(len(Y)):
        if k:
            partes.append((" + ", TINTA))
        partes += [(E._num(X[i][k]), LIN), ("·", TINTA), (E._num(Y[k][j]) if Y[k][j] >= 0 else f"({E._num(Y[k][j])})", COL)]
    r = sum(X[i][k] * Y[k][j] for k in range(len(Y)))
    partes += [(" = ", TINTA), (E._num(r), CERTO)]

    def desenha(a):
        xx = x
        for s, cc in partes:
            E.escreve(c, s, xx, y, size, "g", cc, a)
            xx += E.larg(s, "g", size) + size * 0.04
    E.foco(c, t, t0, 0.5, desenha)


def faixa(c, x0, y0, x1, y1, cor, p, s, a=1.0):
    if p <= 0 or a <= 0:
        return
    xe, ye = lerp(x0, x1, p), lerp(y0, y1, p)
    M.line(c, x0, y0, xe, ye, cor, 0.16 * a, s * 0.78)
    M.line(c, x0, y0, xe, ye, cor, 0.9 * a, 5)


def sarrus(c, t, m, cx, cy, s, t0, tcopia, td, tu):
    ext = [l + l[:2] for l in m]
    G = E.matriz_geo(ext, cx, cy, s)
    k = s * 0.5
    for n in range(3):
        faixa(c, G.x[n] - k, G.y[0] - k, G.x[n + 2] + k, G.y[2] + k, DESCE, ep(t, td[n], 0.6), s)
        faixa(c, G.x[n] - k, G.y[2] + k, G.x[n + 2] + k, G.y[0] - k, SOBE, ep(t, tu[n], 0.6), s)
    q = ep(t, t0, 0.5)
    if q > 0:
        for xb in (G.x[0] - G.ws[0] / 2 - s * 0.4, G.x[2] + G.ws[2] / 2 + s * 0.4):
            M.line(c, xb, G.y0, xb, G.y1, TINTA, q, max(5, s * 0.075))
    for i in range(3):
        for j in range(5):
            ti = t0 if j < 3 else tcopia + 0.15 * (j - 3)
            cc = TINTA if j < 3 else CINZA
            E.foco(c, t, ti, 0.5, lambda a, i=i, j=j, cc=cc: E.formula(c, E._num(ext[i][j]), G.x[j], G.y[i] + s * 0.36, s, "g", cc, a, "center"))
    return G


def pf(v):
    """fator para a tela: negativo entre parênteses"""
    return f"({E._num(v)})" if v < 0 else E._num(v)


def lista(c, t, x, y0, ts, contas, cor, size=56, dy=82):
    for n, (tt, txt) in enumerate(zip(ts, contas)):
        E.foco(c, t, tt, 0.4, lambda a, n=n, txt=txt: E.escreve(c, txt, x, y0 + n * dy, size, "b", cor, a))


# ---------------- abertura ----------------
def b_gancho(c, t, C, b):
    E.foco(c, t, C["s01.a"], 0.5, lambda a: E.escreve(c, "5", XE, 620, 420, "g", COR, a))
    E.frase(c, t, C["s01.a"] + 0.3, [("questões", "g", 120)], XE + 300, 470)
    E.frase(c, t, C["s01.a"] + 0.8, ps("de matrizes e determinantes", "i", 76, TINTA2), XE + 300, 580)
    E.foco(c, t, C["s01.b"], 0.5, lambda a: E.pilula(c, "pause e resolva antes", 1300, 850, 64, estilo="g", a=a))
    E.relogio(c, t, C["s01.b"] + 0.4, cx=1600, cy=330, r=150)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("as ferramentas", "i", 84), XE, 190)
    itens = (("s02.a", "aᵢⱼ: linha antes da coluna"), ("s02.b", "produto: linha por coluna"), ("s02.c", "det: desce − sobe"), ("s02.d", "inversa: a receita"))
    for i, (k, txt) in enumerate(itens):
        y = 360 + i * 170
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 50, y - 25, 48, a=a), E.centro(c, str(i + 1), XE + 50, y - 3, 56, "g", BR, a)))
        E.foco(c, t, C[k] + 0.1, 0.5, lambda a, txt=txt, y=y: E.formula(c, txt, XE + 140, y, 80, "g", TINTA, a))


# ---------------- questão 1 ----------------
def b_questao1(c, t, C, b):
    selo_q(c, t, C["s03.a"], 1)
    E.foco(c, t, C["s03.b"], 0.5, lambda a: E.formula(c, "A: 2 × 2,  aᵢⱼ = i · j", XE, 400, 100, "g", TINTA, a))
    E.matriz(c, t, C["s03.c"], B1, 470, 680, 110, nome="B")
    E.foco(c, t, C["s03.d"], 0.5, lambda a: E.formula(c, "A^t + 3B = ?", XE, 980, 120, "g", COR, a))
    E.relogio(c, t, C["s04.a"], cx=1450, cy=560, r=200)


def b_resposta1(c, t, C, b):
    def parte1():
        E.matriz(c, t, C["s05.a"], A1, 540, 420, 120, nome="A", tl=[C["s05.a"], C["s05.a"] + 2.2])
        E.foco(c, t, C["s05.a"], 0.5, lambda a: E.escreve(c, "1·1   1·2", 900, 380, 60, "b", TINTA2, a))
        E.foco(c, t, C["s05.a"] + 2.2, 0.5, lambda a: E.escreve(c, "2·1   2·2", 900, 520, 60, "b", TINTA2, a))
        E.foco(c, t, C["s05.b"], 0.5, lambda a: E.formula(c, "i · j = j · i", XE, 780, 100, "g", COR, a))
        E.foco(c, t, C["s05.c"], 0.5, lambda a: E.formula(c, "A^t = A", XE + 760, 780, 120, "g", CERTO, a))
        E.foco(c, t, C["s05.c"] + 0.6, 0.5, lambda a: E.escreve(c, "nem precisa montar", XE, 920, 64, "i", TINTA2, a))
    E.saida(c, t, C["s06"] - 0.1, parte1)
    if t < C["s06"]:
        return
    y, s = 520, 110
    GA = E.matriz(c, t, C["s06"], T1, 300, y, s)
    rot(c, t, C["s06"], GA, "A^t")
    E.sinal(c, t, C["s06"] + 0.2, "+", 520, y - 10, 100)
    GB = E.matriz(c, t, C["s06.a"], [[3 * v for v in l] for l in B1], 760, y, s)
    rot(c, t, C["s06.a"], GB, "3B")
    E.sinal(c, t, C["s06.b"] - 0.3, "=", 1010, y - 10, 100)
    ks = ("s06.b", "s06.c", "s06.d", "s06.e")
    GR = E.matriz(c, t, C["s06.b"], R1, 1290, y, s, tc={(n // 2, n % 2): C[k] for n, k in enumerate(ks)}, cores=verde())
    for n, k in enumerate(ks):
        i, j = divmod(n, 2)
        fim = C[ks[n + 1]] if n < 3 else C["s06.e"] + 1.5
        if C[k] <= t < fim:
            for G in (GA, GB, GR):
                E.matriz_marca(c, G, i, j, COR, 1, ep(t, C[k], 0.3))
    if t >= C["s06.e"] + 0.6:
        E.foco(c, t, C["s06.e"] + 0.6, 0.5, lambda a: E.selo(c, 1620, y, 60, True, a))


# ---------------- questão 2 ----------------
def b_questao2(c, t, C, b):
    selo_q(c, t, C["s07.a"], 2)
    y = 520
    rot(c, t, C["s07.b"], E.matriz(c, t, C["s07.b"], A2, 420, y, 120), "A", size=80)
    rot(c, t, C["s07.c"], E.matriz(c, t, C["s07.c"], B2, 900, y, 120), "B", size=80)
    E.foco(c, t, C["s07.d"], 0.5, lambda a: E.formula(c, "A · B = ?", XE, 900, 130, "g", COR, a))
    E.relogio(c, t, C["s08.a"], cx=1500, cy=500, r=190)


def b_resposta2(c, t, C, b):
    y, s = 400, 104
    GA = E.matriz(c, t, C["s09"], A2, 320, y, s)
    rot(c, t, C["s09"], GA, "A")
    E.sinal(c, t, C["s09"] + 0.2, "·", 545, y - 10, 100)
    GB = E.matriz(c, t, C["s09"] + 0.3, B2, 790, y, s)
    rot(c, t, C["s09"] + 0.3, GB, "B")
    E.sinal(c, t, C["s09"] + 0.5, "=", 1040, y - 10, 100)
    ks = ("s09.a", "s09.b", "s10.a", "s10.b")
    fins = (C["s09.b"], C["s10"], C["s10.b"], C["s10.c"])
    GR = E.matriz(c, t, C["s09"] + 0.6, R2, 1380, y, s, tc={(n // 2, n % 2): C[k] + 2.4 for n, k in enumerate(ks)}, cores=verde())
    for n, k in enumerate(ks):
        i, j = divmod(n, 2)
        if t < C[k] + 2.4:
            E.foco(c, t, C["s09"] + 0.6, 0.4, lambda a, i=i, j=j: E.centro(c, "?", GR.x[j], GR.y[i] + s * 0.36, s, "g", CINZA, a))
        if C[k] <= t < fins[n]:
            E.matriz_marca(c, GA, linha=i, cor=LIN, p=ep(t, C[k], 0.4))
            E.matriz_marca(c, GB, coluna=j, cor=COL, p=ep(t, C[k] + 0.2, 0.4))
        E.saida(c, t, fins[n] - 0.05, lambda n=n, i=i, j=j, k=k: conta(c, t, C[k] + 0.5, A2, B2, i, j, 500, 800, 92))
    if t >= C["s10.c"]:
        rot(c, t, C["s10.c"], GR, "A · B", CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s11"], [("o", "i", 84, CLARO), ("atalho", "i", 84, CLARO)], XE, 190)
    E.frase(c, t, C["s11.a"], [("não", "g", 76, BR), ("calcule", "i", 84, BR), ("o", "i", 84, BR), ("produto", "i", 84, BR), ("inteiro", "g", 76, CLARO)], XE, 330)
    alts = (("a)", [[4, 8], [5, 4]]), ("b)", [[4, 8], [5, -4]]), ("c)", [[4, 8], [7, -4]]))
    for n, (l, m) in enumerate(alts):
        x = 420 + n * 540
        E.foco(c, t, C["s11.b"] + 0.2 * n, 0.5, lambda a, l=l, x=x: E.escreve(c, l, x - 250, 640, 70, "g", CLARO, a))
        G = E.matriz(c, t, C["s11.b"] + 0.2 * n, m, x, 620, 90, escuro=True,
                     cores={(1, 0): "#FFB833", (1, 1): BR} if True else None)
        if t >= C["s11.c"]:
            E.matriz_marca(c, G, 1, 0, "#FFB833", 1, ep(t, C["s11.c"], 0.4), cheia=0.0)
    E.foco(c, t, C["s11.c"] + 0.4, 0.5, lambda a: E.escreve(c, "só a linha 2 com a coluna 1: 3·2 + (−1)·1 = 5", XE, 900, 58, "b", "#FFB833", a))
    E.foco(c, t, C["s12.a"], 0.5, lambda a: E.escreve(c, "cada elemento: uma linha com uma coluna", XE, 990, 56, "i", CLARO, a))
    if t >= C["s12.b"]:
        E.foco(c, t, C["s12.b"], 0.5, lambda a: E.pilula(c, "empatou? calcule mais um", 1500, 190, 46, estilo="b", fundo="#FFB833", cor="#07070F", a=a))


# ---------------- questão 3 ----------------
def b_questao3(c, t, C, b):
    selo_q(c, t, C["s13.a"], 3)
    E.foco(c, t, C["s13.a"] + 0.6, 0.5, lambda a: E.escreve(c, "det = ?", XE, 330, 100, "g", COR, a))
    E.matriz(c, t, C["s13.b"], M3, 620, 650, 120, barras=True, tl=[C["s13.b"], C["s13.b"] + 1.8, C["s13.b"] + 3.4])
    E.relogio(c, t, C["s14.a"], cx=1450, cy=560, r=200)


def b_resposta3(c, t, C, b):
    d, u = diags(M3)
    td = [C["s15.b"], C["s15.c"], C["s15.d"]]
    tu = [C["s16.a"], C["s16.b"], C["s16.c"]]
    sarrus(c, t, M3, 560, 470, 96, C["s15"], C["s15.a"], td, tu)
    x1, x2 = 1060, 1480
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.escreve(c, "descendo +", x1, 230, 56, "g", DESCE, a))
    lista(c, t, x1, 330, td, [f"{pf(M3[0][k])}·{pf(M3[1][(k + 1) % 3])}·{pf(M3[2][(k + 2) % 3])} = {E._num(d[k])}" for k in range(3)], DESCE)
    E.foco(c, t, C["s15.e"], 0.5, lambda a: E.escreve(c, f"= {E._num(sum(d))}", x1, 600, 84, "g", DESCE, a))
    E.foco(c, t, C["s16.a"], 0.5, lambda a: E.escreve(c, "subindo −", x2, 230, 56, "g", SOBE, a))
    lista(c, t, x2, 330, tu, [f"{pf(M3[2][k])}·{pf(M3[1][(k + 1) % 3])}·{pf(M3[0][(k + 2) % 3])} = {E._num(u[k])}" for k in range(3)], SOBE)
    E.foco(c, t, C["s16.d"], 0.5, lambda a: E.escreve(c, f"= {E._num(sum(u))}", x2, 600, 84, "g", SOBE, a))
    E.foco(c, t, C["s16.e"], 0.5, lambda a: E.escreve(c, "−2 − 13 =", 620, 880, 120, "g", TINTA, a))
    E.foco(c, t, C["s16.e"] + 0.6, 0.5, lambda a: (E.bola(c, 1330, 840, 120, CERTO, a), E.centro(c, "−15", 1330, 880, 100, "g", BR, a)))


# ---------------- questão 4 ----------------
def b_questao4(c, t, C, b):
    selo_q(c, t, C["s17.a"], 4)
    E.matriz(c, t, C["s17.b"], A4, 560, 560, 150, nome="A")
    E.foco(c, t, C["s17.b"] + 0.5, 0.5, lambda a: E.formula(c, "tem inversa?", XE, 900, 100, "g", COR, a))
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.formula(c, "A^{−1} = ?", XE + 720, 900, 100, "g", COR, a))
    E.relogio(c, t, C["s18.a"], cx=1450, cy=470, r=200)


def b_resposta4(c, t, C, b):
    y = 300
    E.matriz(c, t, C["s19"], A4, 420, y, 100, nome="A", cores={(0, 0): COR, (1, 1): COR, (0, 1): COL, (1, 0): COL})
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, "det = 3·2 − 1·5 = 1", 760, y + 35, 76, "b", TINTA, a))
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.pilula(c, "≠ 0: existe", 1640, y + 10, 50, estilo="b", fundo=CERTO, a=a))
    # a inversa se monta no lugar: a principal troca, a secundária muda o sinal
    cx, cy, s = 620, 720, 120
    G = E.matriz_geo(I4, cx, cy, s, wmin=s * 0.95)
    if t < C["s20.a"]:
        sec = [[None, -1], [-5, None]] if t >= C["s19.d"] else [[None, 1], [5, None]]
        E.matriz(c, t, C["s19.c"] - 0.2, sec, cx, cy, s, cores={(0, 1): COL, (1, 0): COL}, wmin=s * 0.95)
        q = ease_io(prog(t, C["s19.c"], 0.8))
        for (v, i0, i1) in ((3, 0, 1), (2, 1, 0)):
            x, yy = lerp(G.x[i0], G.x[i1], q), lerp(G.y[i0], G.y[i1], q)
            E.foco(c, t, C["s19.c"] - 0.2, 0.5, lambda al, v=v, x=x, yy=yy: E.formula(c, str(v), x, yy + s * 0.36, s, "g", COR, al, "center"))
    else:
        E.matriz(c, t, C["s20.a"], I4, cx, cy, s, cores=verde(), wmin=s * 0.95)
        E.foco(c, t, C["s20.a"], 0.5, lambda a: E.formula(c, "A^{−1} =", G.x0 - 60, cy + 40, 90, "g", CERTO, a, "right"))
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.formula(c, "3·2 + 1·(−5) = 1", 1050, 740, 80, "g", TINTA, a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.selo(c, 1780, 715, 50, True, a))


# ---------------- questão 5 ----------------
def b_questao5(c, t, C, b):
    selo_q(c, t, C["s21.a"], 5)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: (E.formula(c, "A: 2 × 3", XE, 420, 110, "g", TINTA, a), E.formula(c, "B: 3 × 2", XE + 620, 420, 110, "g", TINTA, a)))
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.formula(c, "A · B ?", XE, 680, 110, "g", COR, a))
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.formula(c, "B · A ?", XE + 620, 680, 110, "g", COR, a))
    E.relogio(c, t, C["s22.a"], cx=1500, cy=760, r=170)


def tamanhos(c, t, t0, a_, b_, c_, d_, y, t_meio, t_fora, res):
    s, x = 130, XE
    parts = [(a_, TINTA), ("×", TINTA2), (b_, COL), ("  ·  ", TINTA2), (c_, COL), ("×", TINTA2), (d_, TINTA)]
    xs, xx = [], x
    for txt, _ in parts:
        xs.append(xx)
        xx += E.larg(txt, "g", s) + 18

    def desenha(a):
        for (txt, cc), x_ in zip(parts, xs):
            E.escreve(c, txt, x_, y, s, "g", cc, a)
    E.foco(c, t, t0, 0.5, desenha)
    if t >= t_meio:
        m1, m2 = xs[2] + E.larg(b_, "g", s) / 2, xs[4] + E.larg(c_, "g", s) / 2
        E.chave(c, m1, m2, y + 36, COL, ep(t, t_meio, 0.6), 34, 6)
        E.foco(c, t, t_meio + 0.3, 0.5, lambda a: E.centro(c, "iguais: existe", (m1 + m2) / 2, y + 120, 50, "b", COL, a))
    if t >= t_fora:
        E.foco(c, t, t_fora, 0.5, lambda a: E.escreve(c, f"→ {res}", xx + 60, y, 120, "g", CERTO, a))


def b_resposta5(c, t, C, b):
    E.frase(c, t, C["s23"], ps("os tamanhos lado a lado", "i", 80), XE, 190)
    E.foco(c, t, C["s23.a"], 0.5, lambda a: E.escreve(c, "A · B", XE, 330, 70, "g", COR, a))
    tamanhos(c, t, C["s23.a"], "2", "3", "3", "2", 470, C["s23.b"], C["s23.c"], "2 × 2")
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.escreve(c, "B · A", XE, 680, 70, "g", COR, a))
    tamanhos(c, t, C["s23.d"], "3", "2", "2", "3", 820, C["s23.e"], C["s23.e"] + 0.8, "3 × 3")
    E.foco(c, t, C["s23.f"], 0.5, lambda a: E.pilula(c, "tamanhos diferentes!", 1500, 1000, 50, estilo="g", fundo=ERRADO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s24.a", "linha antes da coluna"), ("s24.b", "produto: linha por coluna"), ("s24.c", "det: desce − sobe"), ("s24.d", "det = 0: sem inversa"))
        for i, (k, s) in enumerate(itens):
            y = 360 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 400, y - 28, 52, a=a), E.centro(c, str(i + 1), 400, y - 6, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 490, y)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25"], ps("próxima aula", "i", 84), XE, 330)
    E.frase(c, t, C["s25.a"], [("Sistemas", "g", 150, COR), ("3 × 3", "g", 150)], XE, 500)
    E.frase(c, t, C["s25.b"], ps("uma letra de cada vez", "i", 90), XE, 650)
    E.foco(c, t, C["s25.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s25.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(1000, 845, p), ep(t, C["s25.c"] + 0.2, 0.4))
    E.frase(c, t, C["s25.d"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, atalho=b_atalho, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4,
              resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
