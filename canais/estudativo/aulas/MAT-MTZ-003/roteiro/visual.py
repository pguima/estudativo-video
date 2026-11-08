"""Visual — Estudativo · MAT-MTZ-003: determinante de 2ª e 3ª ordem, com a regra de Sarrus. Segue a linguagem de MAT-MTZ-001.
Novidade da trilha: o que DESCE (diagonal principal e as paralelas a ela) em índigo, com sinal +; o que SOBE (secundária) em âmbar,
com sinal −. Determinante = matriz com barras (E.matriz(..., barras=True)). sarrus() desenha as colunas copiadas em cinza
e as faixas das diagonais; as próximas aulas copiam daqui."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matrizes e Sistemas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-MTZ-003_determinante.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("oque", "sarrus", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
DESCE, SOBE = COR, "#D98A00"


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def diags(m):
    d = [m[0][k] * m[1][(k + 1) % 3] * m[2][(k + 2) % 3] for k in range(3)]
    u = [m[2][k] * m[1][(k + 1) % 3] * m[0][(k + 2) % 3] for k in range(3)]
    return d, u


D2 = [[1, 2], [3, 4]]
assert det2(D2) == -2 and 1 * 4 == 4 and 3 * 2 == 6
S3 = [[2, 1, 3], [0, 1, 4], [1, 0, 2]]
assert diags(S3) == ([4, 4, 0], [3, 0, 0]) and sum(diags(S3)[0]) - sum(diags(S3)[1]) == 5
TR = [[2, 5, 7], [0, 3, 1], [0, 0, 4]]
assert sum(diags(TR)[0]) - sum(diags(TR)[1]) == 24 == 2 * 3 * 4
Q = [[1, 2, 0], [3, 1, 2], [0, 1, 1]]
assert diags(Q) == ([1, 0, 0], [0, 2, 6]) and sum(diags(Q)[0]) - sum(diags(Q)[1]) == -7


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def faixa(c, x0, y0, x1, y1, cor, p, s, a=1.0):
    """faixa larga e translúcida sobre uma diagonal, que cresce de (x0, y0) até (x1, y1)"""
    if p <= 0 or a <= 0:
        return
    xe, ye = lerp(x0, x1, p), lerp(y0, y1, p)
    M.line(c, x0, y0, xe, ye, cor, 0.16 * a, s * 0.78)
    M.line(c, x0, y0, xe, ye, cor, 0.9 * a, 5)


def diag2(c, t, G, t_p, t_s, a=1.0):
    k = G.size * 0.55
    faixa(c, G.x[0] - k, G.y[0] - k, G.x[1] + k, G.y[1] + k, DESCE, ep(t, t_p, 0.6), G.size, a)
    faixa(c, G.x[0] - k, G.y[1] + k, G.x[1] + k, G.y[0] - k, SOBE, ep(t, t_s, 0.6), G.size, a)


def sarrus(c, t, m, cx, cy, s, t0, tcopia, td, tu, escuro=False, apaga=None):
    """matriz 3x3 com barras + as duas primeiras colunas copiadas; td/tu = instante de cada diagonal (desce/sobe).
    apaga = instante em que as faixas somem (para a próxima etapa). Devolve G (geometria das 5 colunas)."""
    ext = [l + l[:2] for l in m]
    G = E.matriz_geo(ext, cx, cy, s)
    tinta = BR if escuro else TINTA
    k = s * 0.5
    fa = 1.0 if apaga is None else 1 - ep(t, apaga, 0.4)
    for n in range(3):
        faixa(c, G.x[n] - k, G.y[0] - k, G.x[n + 2] + k, G.y[2] + k, CLARO if escuro else DESCE, ep(t, td[n], 0.6), s, fa)
        faixa(c, G.x[n] - k, G.y[2] + k, G.x[n + 2] + k, G.y[0] - k, "#FFB833" if escuro else SOBE, ep(t, tu[n], 0.6), s, fa)
    q = ep(t, t0, 0.5)
    if q > 0:
        for xb in (G.x[0] - G.ws[0] / 2 - s * 0.4, G.x[2] + G.ws[2] / 2 + s * 0.4):
            M.line(c, xb, G.y0, xb, G.y1, tinta, q, max(5, s * 0.075))
    for i in range(3):
        for j in range(5):
            ti = t0 if j < 3 else tcopia + 0.15 * (j - 3)
            cc = tinta if j < 3 else (CLARO if escuro else CINZA)
            E.foco(c, t, ti, 0.5, lambda a, i=i, j=j, cc=cc: E.formula(c, E._num(ext[i][j]), G.x[j], G.y[i] + s * 0.36, s, "g", cc, a, "center"))
    return G


def lista(c, t, x, y0, ts, contas, cor, size=58, dy=86):
    for n, (tt, txt) in enumerate(zip(ts, contas)):
        E.foco(c, t, tt, 0.4, lambda a, n=n, txt=txt: E.escreve(c, txt, x, y0 + n * dy, size, "b", cor, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        G = E.matriz(c, t, C["s01.a"], D2, 620, 520, 170, barras=True)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.escreve(c, "2  ou  −2 ?", 1050, 560, 130, "g", TINTA, a))
        if C["s01.c"] <= t < C["s01.d"]:
            E.foco(c, t, C["s01.c"], 0.4, lambda a: E.escreve(c, "6 − 4 = 2", 1050, 800, 110, "g", ERRADO, a))
            E.risco(c, 1040, 830, 1560, 720, t, C["s01.c"] + 0.6, largura=14)
        if t >= C["s01.d"]:
            diag2(c, t, G, C["s01.d"], C["s01.d"] + 0.4)
            E.foco(c, t, C["s01.d"], 0.5, lambda a: E.escreve(c, "4 − 6 =", 1050, 820, 110, "g", TINTA, a))
            E.foco(c, t, C["s01.d"] + 0.4, 0.5, lambda a: (E.bola(c, 1570, 780, 100, CERTO, a), E.centro(c, "−2", 1570, 815, 100, "g", BR, a)))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 360)
        E.frase(c, t, C["s02.a"] + 1.0, [("determinante", "g", 116, COR)], XE, 520)
        E.frase(c, t, C["s02.a"] + 2.0, [("2 × 2", "g", 110), ("e", "i", 110), ("3 × 3", "g", 110)], XE, 680)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 84), XE, 300)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE, 600, 320, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 210, 580, 120, "i", TINTA, a))
    x, w = 960, 780
    for i, (k, l1, l2) in enumerate((("s03.b", "matriz =", "linhas e colunas"), ("s03.c", "aᵢⱼ =", "linha i, coluna j"))):
        y = 280 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.foco(c, t, C[k] + 0.1, 0.5, lambda a, l1=l1, y=y: E.formula(c, l1, x + 44, y + 95, 66, "b", TINTA, a))
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 64, COR)], x + 44, y + 180)


# ---------------- o que é ----------------
def b_oque(c, t, C, b):
    def def_():
        E.frase(c, t, C["s04.a"], [("um", "i", 90), ("número", "g", 84, COR), ("que", "i", 90), ("vem", "i", 90), ("da", "i", 90), ("matriz", "i", 90)], XE, 220)
        E.frase(c, t, C["s04.b"], [("só", "i", 84), ("na", "i", 84), ("quadrada", "g", 80, COR)], XE, 380)
        E.matriz(c, t, C["s04.c"], [[1, 2], [3, 4]], 600, 640, 100)
        E.foco(c, t, C["s04.c"] + 0.2, 0.5, lambda a: E.centro(c, "2 × 2", 600, 860, 70, "g", COR, a))
        E.matriz(c, t, C["s04.c"] + 0.8, [[2, 1, 3], [0, 1, 4], [1, 0, 2]], 1250, 640, 90)
        E.foco(c, t, C["s04.c"] + 1.0, 0.5, lambda a: E.centro(c, "3 × 3", 1250, 900, 70, "g", COR, a))
        E.foco(c, t, C["s04.d"], 0.5, lambda a: E.pilula(c, "serve para: aula de matriz inversa", W / 2, 990, 44, estilo="b", fundo=TINTA2, a=a))
    E.saida(c, t, C["s05"] - 0.1, def_)
    if t >= C["s05"]:
        E.frase(c, t, C["s05"], ps("as duas diagonais", "i", 90), XE, 220)
        G = E.matriz(c, t, C["s05"], D2, 700, 600, 170)
        diag2(c, t, G, C["s05.a"], C["s05.b"])
        E.foco(c, t, C["s05.a"], 0.5, lambda a: (E.escreve(c, "principal", 1150, 520, 90, "g", DESCE, a),
                                                  E.escreve(c, "desce", 1150, 600, 64, "i", DESCE, a)))
        E.foco(c, t, C["s05.b"], 0.5, lambda a: (E.escreve(c, "secundária", 1150, 760, 90, "g", SOBE, a),
                                                  E.escreve(c, "sobe", 1150, 840, 64, "i", SOBE, a)))


# ---------------- dois por dois ----------------
def b_dois(c, t, C, b):
    E.frase(c, t, C["s06"], [("dois", "i", 90), ("por", "i", 90), ("dois", "i", 90)], XE, 200)
    G = E.matriz(c, t, C["s06"], D2, 520, 560, 160, barras=t >= C["s07.d"])
    diag2(c, t, G, C["s06.a"], C["s06.b"])
    x = 1000
    E.foco(c, t, C["s06.a"], 0.5, lambda a: E.escreve(c, "principal", x, 360, 70, "g", DESCE, a))
    E.foco(c, t, C["s06.b"], 0.5, lambda a: E.escreve(c, "secundária", x + 380, 360, 70, "g", SOBE, a))
    E.foco(c, t, C["s06.c"], 0.5, lambda a: E.escreve(c, "−", x + 315, 360, 80, "g", TINTA, a))
    E.foco(c, t, C["s07.a"], 0.5, lambda a: E.escreve(c, "1 · 4", x + 40, 520, 100, "g", DESCE, a))
    E.foco(c, t, C["s07.b"], 0.5, lambda a: E.escreve(c, "−  3 · 2", x + 300, 520, 100, "g", SOBE, a))
    E.foco(c, t, C["s07.b"] + 0.5, 0.5, lambda a: E.escreve(c, "= 4 − 6", x + 40, 680, 100, "g", TINTA, a))
    E.foco(c, t, C["s07.c"], 0.5, lambda a: (E.escreve(c, "=", x + 40, 840, 100, "g", TINTA, a), E.bola(c, x + 250, 805, 90, CERTO, a),
                                              E.centro(c, "−2", x + 250, 840, 90, "g", BR, a)))
    if t >= C["s07.d"]:
        E.foco(c, t, C["s07.d"], 0.5, lambda a: E.pilula(c, "barras = determinante", 520, 900, 46, estilo="b", a=a))


# ---------------- com negativo ----------------
NEG = [[3, -2], [5, 1]]
assert det2(NEG) == 13 and 5 * -2 == -10 and 3 - (-10) == 13


def b_negativo(c, t, C, b):
    E.frase(c, t, C["s08"], [("com", "i", 90), ("negativo:", "i", 90), ("cuidado", "g", 84, ERRADO)], XE, 200)
    G = E.matriz(c, t, C["s08.b"], NEG, 520, 600, 160, barras=True)
    diag2(c, t, G, C["s08.c"], C["s08.d"])
    x = 1000
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.escreve(c, "3 · 1 = 3", x, 440, 100, "g", DESCE, a))
    E.foco(c, t, C["s08.d"], 0.5, lambda a: E.escreve(c, "5 · (−2) = −10", x, 590, 100, "g", SOBE, a))
    E.foco(c, t, C["s08.e"], 0.5, lambda a: E.escreve(c, "3 − (−10) = 3 + 10", x, 760, 84, "g", TINTA, a))
    E.foco(c, t, C["s08.f"], 0.5, lambda a: (E.escreve(c, "=", x, 920, 100, "g", TINTA, a), E.bola(c, x + 210, 885, 90, CERTO, a),
                                              E.centro(c, "13", x + 210, 920, 90, "g", BR, a)))


# ---------------- Sarrus ----------------
def b_sarrus(c, t, C, b):
    E.frase(c, t, C["s09.a"], [("regra", "i", 90), ("de", "i", 90), ("Sarrus", "g", 84, COR)], XE, 190)
    d, u = diags(S3)
    td = [C["s10.b"], C["s10.c"], C["s10.d"]]
    tu = [C["s11.b"], C["s11.c"], C["s11.d"]]
    sarrus(c, t, S3, 560, 560, 100, C["s09"], C["s09.b"], td, tu)
    if t >= C["s09.b"]:
        E.foco(c, t, C["s09.b"], 0.5, lambda a: E.escreve(c, "cópia", 700, 820, 52, "i", CINZA, a))
    x1, x2 = 1060, 1480
    E.foco(c, t, C["s10.a"], 0.5, lambda a: E.escreve(c, "descendo +", x1, 330, 60, "g", DESCE, a))
    lista(c, t, x1, 430, td, [f"{S3[0][k]}·{S3[1][(k + 1) % 3]}·{S3[2][(k + 2) % 3]} = {d[k]}" for k in range(3)], DESCE)
    E.foco(c, t, C["s10.e"], 0.5, lambda a: E.escreve(c, f"= {sum(d)}", x1, 720, 90, "g", DESCE, a))
    E.foco(c, t, C["s11.a"], 0.5, lambda a: E.escreve(c, "subindo −", x2, 330, 60, "g", SOBE, a))
    lista(c, t, x2, 430, tu, [f"{S3[2][k]}·{S3[1][(k + 1) % 3]}·{S3[0][(k + 2) % 3]} = {u[k]}" for k in range(3)], SOBE)
    E.foco(c, t, C["s11.e"], 0.5, lambda a: E.escreve(c, f"= {sum(u)}", x2, 720, 90, "g", SOBE, a))
    if t >= C["s12"]:
        E.foco(c, t, C["s12.a"], 0.5, lambda a: E.escreve(c, "8 − 3 =", x1, 900, 110, "g", TINTA, a))
        E.foco(c, t, C["s12.b"], 0.5, lambda a: (E.bola(c, x1 + 520, 860, 90, CERTO, a), E.centro(c, "5", x1 + 520, 895, 100, "g", BR, a)))
        E.frase(c, t, C["s12.c"], [("desce", "g", 64, DESCE), ("menos", "i", 70), ("sobe", "g", 64, SOBE)], XE, 1000)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 104, ERRADO), ("com", "i", 96), ("isto", "i", 96)], XE, 200)
    G = E.matriz(c, t, C["s13"], D2, 520, 600, 160, barras=True)
    diag2(c, t, G, C["s13.a"], C["s13.a"])
    x = 1000
    E.foco(c, t, C["s13.a"], 0.5, lambda a: E.escreve(c, "secundária − principal", x, 420, 64, "b", ERRADO, a))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.escreve(c, "6 − 4 = 2", x, 580, 110, "g", ERRADO, a))
    if t >= C["s13.b"] + 0.8:
        E.risco(c, x - 10, 610, x + 500, 500, t, C["s13.b"] + 0.8, largura=14)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.escreve(c, "4 − 6 = −2", x, 780, 110, "g", CERTO, a))
    E.frase(c, t, C["s13.c"] + 0.4, [("principal", "g", 70, DESCE), ("primeiro", "i", 76)], x, 920)


# ---------------- atalho (palco escuro) ----------------
ZL = [[4, 1, 7], [0, 0, 0], [2, 5, 3]]
assert sum(diags(ZL)[0]) - sum(diags(ZL)[1]) == 0


def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s14"], [("o", "i", 84, CLARO), ("atalho", "i", 84, CLARO)], XE, 190)

    def regra():
        E.frase(c, t, C["s14.a"], ps("zero embaixo da principal?", "i", 76, BR), XE, 330)
        E.frase(c, t, C["s14.b"], [("só", "i", 76, BR), ("a", "i", 76, BR), ("diagonal", "g", 70, CLARO)], XE, 440)
    E.saida(c, t, C["s15"] - 0.1, regra)

    def triangular():
        G = E.matriz(c, t, C["s14.b"] + 0.6, TR, 560, 720, 110, barras=True, escuro=True,
                     cores={(1, 0): "#FFB833", (2, 0): "#FFB833", (2, 1): "#FFB833", (0, 0): CLARO, (1, 1): CLARO, (2, 2): CLARO})
        if t >= C["s14.c"]:
            k = 60
            faixa(c, G.x[0] - k, G.y[0] - k, G.x[2] + k, G.y[2] + k, CLARO, ep(t, C["s14.c"], 0.6), 110)
        E.foco(c, t, C["s14.c"], 0.5, lambda a: E.escreve(c, "2 · 3 · 4 = 24", 1000, 740, 110, "g", BR, a))
        if t >= C["s15"]:
            E.frase(c, t, C["s15.a"], ps("as outras diagonais pegam um zero", "i", 64, CLARO), XE, 330)
            E.foco(c, t, C["s15.b"], 0.5, lambda a: E.escreve(c, "zero em cima também vale", 1000, 900, 54, "b", "#FFB833", a))
            E.foco(c, t, C["s15.c"], 0.5, lambda a: E.escreve(c, "zero fora do lugar: Sarrus", 1000, 990, 54, "b", E.ERRADO, a))
    E.saida(c, t, C["s15.d"] - 0.1, triangular)
    if t >= C["s15.d"]:
        E.frase(c, t, C["s15.d"], [("linha", "i", 84, BR), ("de", "i", 84, BR), ("zeros", "g", 78, "#FFB833")], XE, 360)
        G = E.matriz(c, t, C["s15.d"] + 0.2, ZL, 620, 680, 120, barras=True, escuro=True, cores={("l", 1): "#FFB833"})
        E.matriz_marca(c, G, linha=1, cor="#FFB833", p=ep(t, C["s15.d"] + 0.6, 0.5))
        E.foco(c, t, C["s15.e"], 0.5, lambda a: E.escreve(c, "det = 0", 1100, 720, 150, "g", BR, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s16"] + 0.6, 0.5, lambda a: E.escreve(c, "det = ?", XE, 340, 100, "g", COR, a))
    E.matriz(c, t, C["s16.a"], Q, 620, 640, 120, barras=True, tl=[C["s16.a"], C["s16.a"] + 1.6, C["s16.a"] + 3.0])
    E.relogio(c, t, C["s17.a"], cx=1450, cy=520, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    d, u = diags(Q)
    td = [C["s18.b"], C["s18.c"], C["s18.d"]]
    tu = [C["s19.a"], C["s19.b"], C["s19.c"]]
    sarrus(c, t, Q, 540, 470, 96, C["s18"], C["s18.a"], td, tu)
    x1, x2 = 1060, 1480
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.escreve(c, "descendo +", x1, 230, 56, "g", DESCE, a))
    lista(c, t, x1, 330, td, [f"{Q[0][k]}·{Q[1][(k + 1) % 3]}·{Q[2][(k + 2) % 3]} = {d[k]}" for k in range(3)], DESCE, 54, 80)
    E.foco(c, t, C["s18.e"], 0.5, lambda a: E.escreve(c, f"= {sum(d)}", x1, 600, 84, "g", DESCE, a))
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.escreve(c, "subindo −", x2, 230, 56, "g", SOBE, a))
    lista(c, t, x2, 330, tu, [f"{Q[2][k]}·{Q[1][(k + 1) % 3]}·{Q[0][(k + 2) % 3]} = {u[k]}" for k in range(3)], SOBE, 54, 80)
    E.foco(c, t, C["s19.d"], 0.5, lambda a: E.escreve(c, f"= {sum(u)}", x2, 600, 84, "g", SOBE, a))
    E.foco(c, t, C["s19.e"], 0.5, lambda a: E.escreve(c, "1 − 8 =", 700, 880, 120, "g", TINTA, a))
    E.foco(c, t, C["s19.e"] + 0.5, 0.5, lambda a: (E.bola(c, 1250, 840, 110, CERTO, a), E.centro(c, "−7", 1250, 880, 110, "g", BR, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, l1, l2) in enumerate((("s20.a", "2 × 2:", "principal − secundária"), ("s20.b", "3 × 3:", "desce − sobe"))):
            y = 450 + i * 250
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), E.centro(c, str(i + 1), 330, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "i", 96), (l2, "g", 92, COR)], 430, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], ps("próxima aula", "i", 84), XE, 330)
    E.frase(c, t, C["s21.a"], [("Matriz", "g", 150, COR)], XE, 490)
    E.frase(c, t, C["s21.a"] + 0.3, [("inversa", "g", 150, COR)], XE, 640)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.escreve(c, "det = 0 ?", XE, 790, 90, "g", TINTA, a))
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, oque=b_oque, dois=b_dois, negativo=b_negativo, sarrus=b_sarrus, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
