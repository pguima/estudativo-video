"""Visual — Estudativo · MAT-MTZ-004: matriz inversa. Segue a linguagem de MAT-MTZ-001 a 003: linha em índigo, coluna em âmbar,
diagonal principal em índigo e secundária em âmbar (como no determinante). A identidade I aparece em verde: é o "um" das matrizes.
inv_passos() mostra os três passos da receita da 2x2 na própria matriz: a principal troca de lugar, a secundária troca de sinal."""
from fractions import Fraction as Fr
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matrizes e Sistemas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-MTZ-004_matriz_inversa.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("identidade", "regra", "zero", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
LIN, COL = COR, "#D98A00"
PRI, SEC = COR, "#D98A00"


def mult(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]


def det(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def inv(m):
    d = det(m)
    return [[Fr(m[1][1], d), Fr(-m[0][1], d)], [Fr(-m[1][0], d), Fr(m[0][0], d)]]


I2 = [[1, 0], [0, 1]]
A = [[2, 1], [1, 1]]
AI = [[1, -1], [-1, 2]]
assert det(A) == 1 and inv(A) == AI and mult(A, AI) == I2
Z = [[2, 4], [1, 2]]
assert det(Z) == 0
assert 2 * Fr(1, 2) + 1 * 1 == 2
Q = [[2, 3], [1, 1]]
QI = [[-1, 3], [1, -2]]
assert det(Q) == -1 and inv(Q) == QI and mult(Q, QI) == I2 and 2 * -1 + 3 * 1 == 1


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def rot(c, t, t0, G, txt, cor=TINTA, size=64):
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, txt, (G.x0 + G.x1) / 2, G.y0 - 28, size, "g", cor, a, "center"))


def verde(n=2):
    return {(i, j): CERTO for i in range(n) for j in range(n)}


def inv_passos(c, t, m, cx, cy, s, t0, t_troca, t_sinal, t_div=None, div_txt=None, final=None, t_final=None):
    """a matriz que vira a inversa no lugar: t_troca = a principal troca de lugar (os números deslizam na diagonal);
    t_sinal = a secundária ganha o sinal de menos; t_final = troca para a matriz final (ex.: depois da divisão)"""
    a, b_, c_, d = m[0][0], m[0][1], m[1][0], m[1][1]
    todos = [[a, -b_], [-c_, d]] + ([list(l) for l in final] if final else [])
    wm = max(E.matriz_geo(todos, cx, cy, s).ws)
    if final is not None and t_final is not None and t >= t_final:
        E.matriz(c, t, t_final, final, cx, cy, s, cores=verde(), wmin=wm)
        return E.matriz_geo(final, cx, cy, s, wmin=wm)
    sec = [[None, -b_], [-c_, None]] if t >= t_sinal else [[None, b_], [c_, None]]
    G = E.matriz_geo([[a, -b_], [-c_, d]], cx, cy, s, wmin=wm)
    E.matriz(c, t, t0, sec, cx, cy, s, cores={(0, 1): SEC, (1, 0): SEC}, tm=t0, wmin=wm)
    q = ease_io(prog(t, t_troca, 0.8))
    for (v, i0, i1) in ((a, 0, 1), (d, 1, 0)):
        x, y = lerp(G.x[i0], G.x[i1], q), lerp(G.y[i0], G.y[i1], q)
        E.foco(c, t, t0, 0.5, lambda al, v=v, x=x, y=y: E.formula(c, E._num(v), x, y + s * 0.36, s, "g", PRI, al, "center"))
    if t >= t_sinal:
        for (i, j) in ((0, 1), (1, 0)):
            k = ep(t, t_sinal, 0.4)
            c.drawCircle(G.x[j], G.y[i], s * 0.62, M.paint(SEC, 0.12 * k))
    if t_div is not None and t >= t_div:
        E.foco(c, t, t_div, 0.5, lambda al: E.pilula(c, div_txt, cx, G.y1 + 70, 46, estilo="b", fundo=TINTA, a=al))
    return G


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        G = E.matriz(c, t, C["s01.a"], A, 560, 520, 150, nome="A")
        E.foco(c, t, C["s01.a"] + 0.3, 0.5, lambda a: E.formula(c, "A^{−1} = ?", 1000, 400, 110, "g", TINTA, a))
        if C["s01.b"] <= t < C["s01.c"]:
            E.foco(c, t, C["s01.b"], 0.5, lambda a: (E.formula(c, "f{1}{2}", 1180, 720, 100, "g", ERRADO, a), E.formula(c, "1", 1380, 720, 100, "g", ERRADO, a),
                                                      E.formula(c, "1", 1180, 880, 100, "g", ERRADO, a), E.formula(c, "1", 1380, 880, 100, "g", ERRADO, a)))
            E.risco(c, 1100, 930, 1480, 620, t, C["s01.b"] + 1.2, largura=14)
        if t >= C["s01.c"]:
            E.matriz(c, t, C["s01.c"], AI, 1300, 760, 120, cores=verde())
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 360)
        E.frase(c, t, C["s02.a"] + 1.0, [("a", "i", 120), ("inversa", "g", 120, COR)], XE, 520)
        E.frase(c, t, C["s02.a"] + 2.4, ps("e quando não existe", "i", 84), XE, 680)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 84), XE, 300)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE, 600, 320, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 210, 580, 120, "i", TINTA, a))
    x, w = 960, 800
    for i, (k, l1, l2) in enumerate((("s03.b", "multiplicar =", "linha por coluna"), ("s03.c", "determinante =", "principal − secundária"))):
        y = 280 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "b", 62)], x + 44, y + 95)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 180)


# ---------------- identidade ----------------
def b_identidade(c, t, C, b):
    def numeros():
        E.foco(c, t, C["s04.a"], 0.5, lambda a: E.formula(c, "2 · f{1}{2} = 1", XE, 360, 140, "g", TINTA, a))
        E.foco(c, t, C["s04.b"], 0.5, lambda a: E.pilula(c, "1/2 é o inverso de 2", XE + 330, 520, 52, estilo="b", a=a))
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.formula(c, "5 · 1 = 5", XE, 760, 120, "g", CERTO, a))
        E.frase(c, t, C["s04.c"] + 0.4, ps("vezes um não muda nada", "i", 70, TINTA2), XE + 620, 750)
    E.saida(c, t, C["s05"] - 0.1, numeros)
    if C["s05"] <= t:
        def ident():
            E.frase(c, t, C["s05.a"], [("matriz", "i", 90), ("identidade", "g", 84, CERTO)], XE, 210)
            G = E.matriz(c, t, C["s05.b"], I2, 520, 560, 150, cores=verde())
            E.foco(c, t, C["s05.c"], 0.5, lambda a: E.formula(c, "I =", G.x0 - 40, 560 + 54, 150, "g", CERTO, a, "right"))
            E.frase(c, t, C["s05.b"] + 0.5, ps("1 na diagonal, 0 no resto", "i", 64, TINTA2), 900, 470)
            E.foco(c, t, C["s05.d"], 0.5, lambda a: E.formula(c, "A · I = A", 900, 680, 130, "g", TINTA, a))
        E.saida(c, t, C["s06"] - 0.1, ident)
    if C["s06"] <= t:
        E.frase(c, t, C["s06.a"], [("a", "i", 90), ("inversa", "g", 84, COR)], XE, 260)
        E.foco(c, t, C["s06.b"], 0.5, lambda a: E.formula(c, "A · A^{−1} = I", W / 2, 560, 170, "g", TINTA, a, "center"))
        E.foco(c, t, C["s06.c"], 0.5, lambda a: E.pilula(c, "A elevado a menos um", W / 2, 760, 58, estilo="b", a=a))


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    passos = (("s07.b", "troque a", "principal de lugar"), ("s07.c", "troque o sinal", "da secundária"), ("s07.d", "divida tudo", "pelo determinante"))
    for n, (k, l1, l2) in enumerate(passos):
        E.passo(c, t, C[k], n + 1, l1, l2, 250 + n * 230)
    E.frase(c, t, C["s07.a"], [("3", "g", 64, COR), ("passos", "i", 70)], XE, 110)
    if t < C["s08"]:
        return
    cx, cy, s = 1400, 300, 110
    G0 = E.matriz(c, t, C["s08"], A, cx - 50, cy, s, nome="A", cores={(0, 0): PRI, (1, 1): PRI, (0, 1): SEC, (1, 0): SEC})
    E.foco(c, t, C["s08.a"], 0.5, lambda a: E.formula(c, "det = 2·1 − 1·1 = 1", 1060, 560, 64, "b", TINTA, a))
    inv_passos(c, t, A, cx, 790, s, C["s08.b"] - 0.2, C["s08.b"], C["s08.c"], C["s08.d"], "÷ 1: nada muda", AI, C["s08.e"])
    E.foco(c, t, C["s08.e"], 0.5, lambda a: E.formula(c, "A^{−1} =", cx - 230, 790 + 40, 100, "g", CERTO, a, "right"))


# ---------------- conferir ----------------
def b_confere(c, t, C, b):
    E.frase(c, t, C["s09"], ps("confira: linha por coluna", "i", 80), XE, 180)
    y, s = 460, 110
    GA = E.matriz(c, t, C["s09"], A, 330, y, s)
    rot(c, t, C["s09"], GA, "A")
    E.sinal(c, t, C["s09"] + 0.2, "·", 560, y - 10, 100)
    GB = E.matriz(c, t, C["s09"] + 0.3, AI, 820, y, s)
    rot(c, t, C["s09"] + 0.3, GB, "A^{−1}")
    E.sinal(c, t, C["s09"] + 0.5, "=", 1090, y - 10, 100)
    ks = ("s09.a", "s09.b", "s09.c", "s09.d")
    GR = E.matriz(c, t, C["s09"] + 0.5, I2, 1380, y, s, tc={(n // 2, n % 2): C[k] + 0.3 for n, k in enumerate(ks)}, cores=verde())
    for n, k in enumerate(ks):
        i, j = divmod(n, 2)
        fim = C[ks[n + 1]] if n < 3 else C["s09.e"]
        if C[k] <= t < fim:
            E.matriz_marca(c, GA, linha=i, cor=LIN, p=ep(t, C[k], 0.4))
            E.matriz_marca(c, GB, coluna=j, cor=COL, p=ep(t, C[k] + 0.2, 0.4))
            txt = f"{E._num(A[i][0])}·({E._num(AI[0][j])}) + {E._num(A[i][1])}·({E._num(AI[1][j])}) = {mult(A, AI)[i][j]}"
            E.foco(c, t, C[k], 0.4, lambda a, txt=txt: E.centro(c, txt, W / 2, 820, 80, "g", TINTA, a))
        if t < C[k] + 0.3:
            E.foco(c, t, C["s09"] + 0.5, 0.4, lambda a, i=i, j=j: E.centro(c, "?", GR.x[j], GR.y[i] + s * 0.36, s, "g", CINZA, a))
    if t >= C["s09.e"]:
        rot(c, t, C["s09.e"], GR, "I", CERTO, 80)
        E.foco(c, t, C["s09.e"], 0.5, lambda a: E.centro(c, "deu a identidade", W / 2, 840, 90, "g", CERTO, a))


# ---------------- determinante zero ----------------
def b_zero(c, t, C, b):
    def numeros():
        E.frase(c, t, C["s10"], ps("quando não existe?", "i", 90), XE, 220)
        E.foco(c, t, C["s10.a"], 0.5, lambda a: E.formula(c, "0 · ? = 1", XE, 480, 150, "g", ERRADO, a))
        E.foco(c, t, C["s10.a"] + 0.6, 0.5, lambda a: E.escreve(c, "impossível", XE + 760, 470, 90, "i", ERRADO, a))
        E.frase(c, t, C["s10.b"], [("o", "i", 84), ("aviso:", "i", 84), ("determinante", "g", 80, COR)], XE, 700)
        E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "det = 0  →  sem inversa", XE, 880, 100, "g", ERRADO, a))
    E.saida(c, t, C["s11"] - 0.1, numeros)
    if t >= C["s11"]:
        G = E.matriz(c, t, C["s11.a"], Z, 560, 540, 160, barras=True)
        E.foco(c, t, C["s11.b"], 0.5, lambda a: E.escreve(c, "2·2 − 4·1", 1000, 460, 100, "g", TINTA, a))
        E.foco(c, t, C["s11.b"] + 1.2, 0.5, lambda a: E.escreve(c, "= 4 − 4 = 0", 1000, 610, 100, "g", ERRADO, a))
        E.foco(c, t, C["s11.c"], 0.5, lambda a: (E.selo(c, 1080, 800, 70, False, a), E.escreve(c, "sem inversa", 1180, 830, 90, "g", ERRADO, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 104, ERRADO), ("com", "i", 96), ("isto", "i", 96)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("inverter cada número", "i", 76, ERRADO), XE, 300)
    y, s = 580, 110
    GA = E.matriz(c, t, C["s12.b"], A, 330, y, s)
    E.sinal(c, t, C["s12.b"] + 0.2, "·", 560, y - 10, 100)
    GB = E.matriz(c, t, C["s12.b"] + 0.3, [["f{1}{2}", 1], [1, 1]], 830, y, s, cores={(i, j): ERRADO for i in range(2) for j in range(2)}, dy=s * 1.6)
    if t >= C["s12.c"]:
        E.matriz_marca(c, GA, linha=0, cor=LIN, p=ep(t, C["s12.c"], 0.4))
        E.matriz_marca(c, GB, coluna=0, cor=COL, p=ep(t, C["s12.c"] + 0.2, 0.4))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "2 · f{1}{2} + 1 · 1 = 2", 1130, y + 30, 80, "g", TINTA, a))
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.escreve(c, "devia dar 1: não é a inversa", XE, 940, 76, "g", ERRADO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], [("o", "i", 84, CLARO), ("atalho", "i", 84, CLARO)], XE, 190)
    E.frase(c, t, C["s13.a"], [("1º:", "g", 76, BR), ("calcule", "i", 84, BR), ("o", "i", 84, BR), ("determinante", "g", 76, CLARO)], XE, 340)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: (E.escreve(c, "det = 0", XE, 540, 110, "g", "#FFB833", a),
                                              E.escreve(c, "→", XE + 470, 540, 90, "g", BR, a), E.escreve(c, "não existe", XE + 600, 540, 90, "i", BR, a)))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: (E.escreve(c, "det = 1", XE, 720, 110, "g", "#FFB833", a),
                                              E.escreve(c, "→", XE + 470, 720, 90, "g", BR, a), E.escreve(c, "de cabeça", XE + 600, 720, 90, "i", BR, a)))
    E.foco(c, t, C["s14.a"], 0.5, lambda a: E.escreve(c, "÷ 1 não muda nada", XE + 1100, 720, 60, "b", CLARO, a))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (E.escreve(c, "det = 2", XE, 900, 110, "g", "#FFB833", a),
                                              E.escreve(c, "→", XE + 470, 900, 90, "g", BR, a), E.escreve(c, "divida cada número", XE + 600, 900, 90, "i", BR, a)))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    G = E.matriz(c, t, C["s15.a"], Q, 560, 560, 150, nome="A")
    E.foco(c, t, C["s15.a"] + 0.5, 0.5, lambda a: E.formula(c, "A^{−1} = ?", XE, 900, 120, "g", COR, a))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.escreve(c, "(se existir)", XE + 620, 900, 70, "i", TINTA2, a))
    E.relogio(c, t, C["s16.a"], cx=1450, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    y = 300
    E.matriz(c, t, C["s17"], Q, 420, y, 100, nome="A", cores={(0, 0): PRI, (1, 1): PRI, (0, 1): SEC, (1, 0): SEC})
    E.foco(c, t, C["s17.a"], 0.5, lambda a: E.formula(c, "det = 2·1 − 3·1 = −1", 760, y + 35, 76, "b", TINTA, a))
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.pilula(c, "≠ 0: existe", 1640, y + 10, 50, estilo="b", fundo=CERTO, a=a))
    inv_passos(c, t, Q, 600, 720, 120, C["s17.c"] - 0.2, C["s17.c"], C["s17.d"], C["s18.a"], "÷ (−1): troca todos os sinais", QI, C["s18.c"])
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.formula(c, "A^{−1} =", 300, 720 + 40, 90, "g", CERTO, a, "right"))
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.formula(c, "2·(−1) + 3·1 = 1", 1050, 740, 80, "g", TINTA, a))
    E.foco(c, t, C["s18.d"] + 0.6, 0.5, lambda a: E.selo(c, 1780, 715, 50, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        for i, (k, s) in enumerate((("s19.a", "det = 0: sem inversa"), ("s19.b", "troca e muda o sinal"), ("s19.c", "divide pelo det"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 430, y - 30, 56, a=a), E.centro(c, str(i + 1), 430, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 96)], 530, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], ps("próxima aula", "i", 84), XE, 330)
    E.frase(c, t, C["s20.a"], [("Praticando", "g", 150, COR)], XE, 490)
    E.frase(c, t, C["s20.b"], [("matrizes", "g", 110), ("e", "i", 110), ("determinantes", "g", 110)], XE, 640)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(1000, 845, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, identidade=b_identidade, regra=b_regra, confere=b_confere, zero=b_zero,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
