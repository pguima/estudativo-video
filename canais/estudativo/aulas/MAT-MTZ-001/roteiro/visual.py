"""Visual — Estudativo · MAT-MTZ-001: o que é matriz, transposta, soma e número vezes matriz. Primeira aula de Matrizes.

LINGUAGEM VISUAL DE MATRIZES E SISTEMAS (as próximas aulas da trilha copiam daqui):
- A matriz é a peça E.matriz (colchetes; barras=True para determinante), sempre grande (110 a 150) e com muito ar em volta.
- LINHA (deitada) em índigo, a cor da matéria; COLUNA (em pé) em âmbar #D98A00. As faixas de E.matriz_marca seguem isso.
- Endereço aᵢⱼ escrito com os índices pequenos (a₂₁): o índice da linha em índigo quando importa, o da coluna em âmbar.
- Resultado na cor de certo (verde) ou na esfera; erro em vermelho com risco; atalho no palco escuro.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matrizes e Sistemas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-MTZ-001_o_que_e_matriz.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("tabela", "lei", "somar", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
LIN, COL = COR, "#D98A00"

BOLETIM = [[7, 5, 8], [6, 9, 4]]
A = [[2, 3], [3, 4]]
B = [[1, -1], [0, 5]]
SOMA = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
assert SOMA == [[3, 2], [3, 9]]
assert [[3 * v for v in l] for l in A] == [[6, 9], [9, 12]]
assert [[i + j for j in (1, 2)] for i in (1, 2)] == A
Q = [[2 * i - j for j in (1, 2)] for i in (1, 2)]
QT = [list(r) for r in zip(*Q)]
assert Q == [[1, 0], [3, 2]] and QT == [[1, 3], [0, 2]]
assert [[Q[i][j] + QT[i][j] for j in range(2)] for i in range(2)] == A


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


# ---------------- gancho ----------------
GANCHO = [[1, 5], [3, 2]]


def b_gancho(c, t, C, b):
    def tabela():
        G = E.matriz(c, t, C["s01.a"], GANCHO, 640, 560, 170)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.formula(c, "a₂₁ = ?", 1150, 590, 150, "g", TINTA, a))
        if t >= C["s01.c"]:
            ruim = t < C["s01.d"]
            E.matriz_marca(c, G, 0, 1, ERRADO, ep(t, C["s01.c"], 0.3) * (1 - ep(t, C["s01.d"], 0.3)), ep(t, C["s01.c"], 0.4))
            if ruim:
                E.foco(c, t, C["s01.c"], 0.4, lambda a: E.escreve(c, "5 ?", 1180, 800, 120, "g", ERRADO, a))
        if t >= C["s01.d"]:
            E.matriz_marca(c, G, 1, 0, CERTO, 1, ep(t, C["s01.d"], 0.4))
            E.foco(c, t, C["s01.d"], 0.5, lambda a: (E.bola(c, 1260, 780, 110, CERTO, a), E.centro(c, "3", 1260, 820, 120, "g", BR, a)))
    E.saida(c, t, C["s02"] - 0.1, tabela)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        for i, w in enumerate(("montar", "transpor", "somar", "multiplicar")):
            E.frase(c, t, C["s02.a"] + 0.8 + 0.5 * i, [(w, "g", 104, COR if i % 2 else TINTA)], XE, 470 + i * 130)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só precisa de", "i", 84), XE, 300)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE, 560, 300, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 190, 540, 120, "i", TINTA, a))
    x, w = 900, 860
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, 200, w, 200, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("trocar a letra", "i", 64)], x + 44, 285)
    E.frase(c, t, C["s03.b"] + 0.4, [("por um número", "g", 64, COR)], x + 44, 365)
    E.foco(c, t, C["s03.c"], 0.5, lambda a: E.formula(c, "2x − 3,  x = 5", x + 40, 560, 88, "g", TINTA, a))
    E.foco(c, t, C["s03.d"], 0.5, lambda a: E.formula(c, "10 − 3 = 7", x + 40, 720, 88, "g", COR, a))
    E.cursor(c, x + w - 30, 370, ep(t, C["s03.b"] + 0.3, 0.4))


# ---------------- o que é matriz ----------------
def b_tabela(c, t, C, b):
    cx, cy, s = 1150, 560, 128
    G = E.matriz_geo(BOLETIM, cx, cy, s)
    # cabeçalhos e nomes somem quando entram os colchetes
    def rotulos():
        for j in range(3):
            E.foco(c, t, C["s04.a"] + 0.2 * j, 0.5, lambda a, j=j: E.centro(c, f"{j + 1}ª prova", G.x[j], G.y0 - 40, 44, "i", TINTA2, a))
        E.frase(c, t, C["s04.b"], [("Ana", "g", 84)], 360, G.y[0] + 30)
        E.frase(c, t, C["s04.c"], [("Bruno", "g", 84)], 360, G.y[1] + 30)
    E.saida(c, t, C["s05.a"], rotulos)
    E.frase(c, t, C["s04.a"], ps("o boletim", "i", 80), XE, 190)
    E.matriz(c, t, C["s04.b"], BOLETIM, cx, cy, s, tl=[C["s04.b"], C["s04.c"]], tm=C["s05.a"])
    E.foco(c, t, C["s05.b"], 0.5, lambda a: E.escreve(c, "matriz", XE + 390, 190, 110, "g", COR, a))
    if C["s05.c"] <= t < C["s06"]:
        E.matriz_marca(c, G, linha=0, cor=LIN, p=ep(t, C["s05.c"], 0.6))
        E.foco(c, t, C["s05.c"], 0.5, lambda a: E.escreve(c, "linha", 260, G.y[0] + 30, 84, "g", LIN, a))
    if C["s05.d"] <= t < C["s06"]:
        E.matriz_marca(c, G, coluna=0, cor=COL, p=ep(t, C["s05.d"], 0.6))
        E.foco(c, t, C["s05.d"], 0.5, lambda a: E.centro(c, "coluna", G.x[0], G.y1 + 110, 84, "g", COL, a))
    if t >= C["s06"]:
        for i in range(2):
            E.foco(c, t, C["s06.a"] + 0.3 * i, 0.4, lambda a, i=i: E.escreve(c, str(i + 1), G.x0 - 110, G.y[i] + 40, 100, "g", LIN, a))
        for j in range(3):
            E.foco(c, t, C["s06.a"] + 0.8 + 0.3 * j, 0.4, lambda a, j=j: E.centro(c, str(j + 1), G.x[j], G.y0 - 40, 80, "g", COL, a))
        E.foco(c, t, C["s06.b"], 0.5, lambda a: (E.escreve(c, "2", XE, 640, 220, "g", LIN, a), E.escreve(c, "×", XE + 165, 620, 150, "g", TINTA, a),
                                                  E.escreve(c, "3", XE + 300, 640, 220, "g", COL, a)))
        E.frase(c, t, C["s06.c"], [("linhas", "g", 76, LIN), ("primeiro,", "i", 80), ("depois", "i", 80), ("colunas", "g", 76, COL)], W / 2, 980, "center")


# ---------------- endereço ----------------
def b_endereco(c, t, C, b):
    G = E.matriz(c, t, C["s07"], BOLETIM, 560, 560, 120)
    E.frase(c, t, C["s07"], [("cada", "i", 76), ("número", "i", 76), ("é", "i", 76), ("um", "i", 76), ("elemento", "g", 70, COR)], XE, 200)
    if C["s07.b"] <= t:
        E.matriz_marca(c, G, 0, 2, COR, 1, ep(t, C["s07.b"], 0.5))
    x = 1080
    E.foco(c, t, C["s07.b"], 0.5, lambda a: (E.escreve(c, "a", x, 520, 190, "g", TINTA, a), E.escreve(c, "1", x + 110, 560, 110, "g", LIN, a),
                                              E.escreve(c, "3", x + 180, 560, 110, "g", COL, a)))
    E.foco(c, t, C["s07.c"], 0.5, lambda a: E.escreve(c, "= 8", x + 300, 520, 170, "g", COR, a))
    E.foco(c, t, C["s08.a"], 0.5, lambda a: (E.escreve(c, "linha", x + 30, 680, 60, "b", LIN, a), E.escreve(c, "coluna", x + 210, 680, 60, "b", COL, a)))
    if t >= C["s08.b"]:
        y = 890
        E.foco(c, t, C["s08.b"], 0.5, lambda a: E.escreve(c, "i = linha", x, y - 70, 64, "b", LIN, a))
        E.foco(c, t, C["s08.c"], 0.5, lambda a: E.escreve(c, "j = coluna", x + 380, y - 70, 64, "b", COL, a))
        E.foco(c, t, C["s08.d"], 0.5, lambda a: (E.escreve(c, "a", x, y + 90, 150, "g", TINTA, a), E.escreve(c, "i", x + 90, y + 120, 90, "g", LIN, a),
                                                  E.escreve(c, "j", x + 130, y + 120, 90, "g", COL, a)))


# ---------------- lei de formação ----------------
def b_lei(c, t, C, b):
    E.frase(c, t, C["s09.a"], ps("uma regra para montar", "i", 80), XE, 200)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.formula(c, "aᵢⱼ = i + j", XE, 400, 150, "g", TINTA, a))
    E.foco(c, t, C["s09.b"] + 0.3, 0.5, lambda a: E.pilula(c, "2 × 2", XE + 850, 350, 56, estilo="g", a=a))
    ks = ("s10.a", "s10.b", "s10.c", "s10.d")
    tc = {(i, j): C[ks[2 * i + j]] for i in range(2) for j in range(2)}
    G = E.matriz(c, t, C["s10"], A, 520, 720, 130, tc=tc, nome="A")
    for i in range(2):
        for j in range(2):
            k = ks[2 * i + j]
            if t < C[k]:
                E.foco(c, t, C["s10"], 0.4, lambda a, i=i, j=j: E.centro(c, "?", G.x[j], G.y[i] + 47, 130, "g", CINZA, a))
    x = 1000
    for n, k in enumerate(ks):
        i, j = divmod(n, 2)
        E.foco(c, t, C[k], 0.4, lambda a, i=i, j=j, n=n: (
            E.escreve(c, f"a{'₁₂'[i]}{'₁₂'[j]}", x, 560 + n * 110, 70, "g", TINTA, a),
            E.escreve(c, f"= {i + 1} + {j + 1} = {i + j + 2}", x + 140, 560 + n * 110, 70, "b", COR, a)))
    for n, k in enumerate(ks):
        i, j = divmod(n, 2)
        if C[k] <= t < (C[ks[n + 1]] if n < 3 else C["s10"] + 99):
            E.matriz_marca(c, G, i, j, COR, 1, ep(t, C[k], 0.3))


# ---------------- transposta ----------------
def b_transposta(c, t, C, b):
    E.frase(c, t, C["s11"], [("a", "i", 84), ("transposta", "g", 76, COR)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("troca linhas por colunas", "i", 64, TINTA2), XE, 280)
    s = 112
    G = E.matriz(c, t, C["s11"], BOLETIM, 560, 620, s, nome="A")
    T = [list(r) for r in zip(*BOLETIM)]
    GT = E.matriz_geo(T, 1460, 620, s)
    E.matriz(c, t, C["s11.b"], T, 1460, 620, s, tc={(j, i): C["s11.b"] + 0.4 if i == 0 else C["s11.c"] + 0.4 for i in range(2) for j in range(3)},
             cores={("c", 0): LIN, ("c", 1): COL})
    E.foco(c, t, C["s11.d"], 0.5, lambda a: (E.escreve(c, "A", GT.x0 - 230, 660, s, "g", TINTA, a),
                                              E.escreve(c, "t", GT.x0 - 155, 600, 80, "g", COR, a), E.escreve(c, "=", GT.x0 - 110, 660, s, "g", TINTA, a)))
    if C["s11.b"] <= t < C["s12"]:
        E.matriz_marca(c, G, linha=0, cor=LIN, p=ep(t, C["s11.b"], 0.5))
        E.matriz_marca(c, GT, coluna=0, cor=LIN, p=ep(t, C["s11.b"] + 0.4, 0.5))
    if C["s11.c"] <= t < C["s12"]:
        E.matriz_marca(c, G, linha=1, cor=COL, p=ep(t, C["s11.c"], 0.5))
        E.matriz_marca(c, GT, coluna=1, cor=COL, p=ep(t, C["s11.c"] + 0.4, 0.5))
    if t >= C["s11.b"]:
        p = ep(t, C["s11.b"], 0.6)
        M.arrow(c, G.x1 + 40, 620, GT.x0 - 260, 620, TINTA2, p, 5, 18, p)
    if t >= C["s12"]:
        E.frase(c, t, C["s12.a"], ps("cada aluno vira uma coluna", "i", 60, TINTA2), 1000, 280)
        E.foco(c, t, C["s12.b"], 0.5, lambda a: E.centro(c, "2 × 3", 560, 960, 100, "g", TINTA, a))
        E.foco(c, t, C["s12.b"] + 0.4, 0.5, lambda a: E.centro(c, "3 × 2", 1460, 1000, 100, "g", COR, a))


# ---------------- somar ----------------
def b_somar(c, t, C, b):
    E.frase(c, t, C["s13.a"], [("somar", "g", 90, COR), ("matrizes", "i", 96)], XE, 200)
    E.frase(c, t, C["s13.b"], ps("lugar com lugar", "i", 70, TINTA2), XE + 720, 200)
    y, s = 560, 112
    ks = ("s13.c", "s13.d", "s13.e", "s13.f")
    GA = E.matriz(c, t, C["s13.a"], A, 400, y, s)
    E.sinal(c, t, C["s13.a"] + 0.3, "+", 650, y - 10, 100)
    GB = E.matriz(c, t, C["s13.a"] + 0.5, B, 920, y, s)
    E.sinal(c, t, C["s13.c"] - 0.3, "=", 1190, y - 10, 100)
    tc = {(n // 2, n % 2): C[k] for n, k in enumerate(ks)}
    GS = E.matriz(c, t, C["s13.c"], SOMA, 1480, y, s, tc=tc, tm=C["s13.c"] - 0.2, cores={(i, j): CERTO for i in range(2) for j in range(2)})
    for n, k in enumerate(ks):
        i, j = divmod(n, 2)
        fim = C[ks[n + 1]] if n < 3 else C["s14"]
        if C[k] <= t < fim:
            for G in (GA, GB, GS):
                E.matriz_marca(c, G, i, j, COR, 1, ep(t, C[k], 0.3))

    def tamanhos():
        E.foco(c, t, C["s14.a"], 0.5, lambda a: E.escreve(c, "só com o mesmo tamanho", XE, 900, 70, "i", TINTA, a))
    E.saida(c, t, C["s14.b"], tamanhos)
    if t >= C["s14.b"]:
        E.foco(c, t, C["s14.b"], 0.5, lambda a: (E.escreve(c, "2 × 2  +  2 × 3", XE, 920, 80, "g", TINTA, a),
                                                  E.escreve(c, "não existe", XE + 760, 920, 80, "g", ERRADO, a)))
        E.risco(c, XE - 10, 940, XE + 640, 870, t, C["s14.b"] + 0.4, largura=12)


# ---------------- número vezes matriz ----------------
def b_numero(c, t, C, b):
    E.frase(c, t, C["s15.a"], [("3", "g", 110, COR), ("vezes", "i", 100), ("uma", "i", 100), ("matriz", "i", 100)], XE, 220)
    y, s = 600, 130
    E.foco(c, t, C["s15.a"] + 0.3, 0.5, lambda a: E.escreve(c, "3 ·", 280, y + 45, 150, "g", COR, a))
    G = E.matriz(c, t, C["s15.a"] + 0.3, A, 720, y, s, gap=s * 1.0)
    if t >= C["s15.b"]:
        for i in range(2):
            for j in range(2):
                E.foco(c, t, C["s15.b"] + 0.15 * (2 * i + j), 0.4,
                       lambda a, i=i, j=j: E.centro(c, "×3", G.x[j], G.y[i] - 62, 44, "b", COR, a), sobe=8)
    E.sinal(c, t, C["s15.c"] - 0.3, "=", 1050, y - 10, 110)
    E.matriz(c, t, C["s15.c"], [[3 * v for v in l] for l in A], 1430, y, s, cores={(i, j): CERTO for i in range(2) for j in range(2)})
    E.frase(c, t, C["s15.b"], ps("multiplica cada elemento", "i", 64, TINTA2), XE, 950)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s16"], [("cuidado", "g", 104, ERRADO), ("com", "i", 96), ("isto", "i", 96)], XE, 200)
    G = E.matriz(c, t, C["s16"], GANCHO, 600, 600, 160)
    x = 1100
    E.foco(c, t, C["s16.a"], 0.5, lambda a: E.escreve(c, "ler ao contrário", x, 400, 76, "i", ERRADO, a))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: (E.escreve(c, "a", x, 600, 150, "g", TINTA, a), E.escreve(c, "2", x + 88, 630, 90, "g", LIN, a),
                                              E.escreve(c, "1", x + 140, 630, 90, "g", COL, a)))
    if t >= C["s16.b"]:
        E.matriz_marca(c, G, linha=1, cor=LIN, p=ep(t, C["s16.b"], 0.5), cheia=0.08)
        E.matriz_marca(c, G, coluna=0, cor=COL, p=ep(t, C["s16.b"] + 0.7, 0.5), cheia=0.08)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: (E.bola(c, x + 360, 560, 90, CERTO, a), E.centro(c, "3", x + 360, 595, 100, "g", BR, a)))
    if t >= C["s16.d"]:
        E.matriz_marca(c, G, 0, 1, ERRADO, 1, ep(t, C["s16.d"], 0.4), cheia=0.15)
        E.foco(c, t, C["s16.d"], 0.5, lambda a: E.escreve(c, "5 = a₁₂", x, 800, 100, "g", ERRADO, a))
    E.frase(c, t, C["s16.e"], [("linha", "g", 100, LIN), ("primeiro", "i", 104)], x, 960)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def parte1():
        E.frase(c, t, C["s17"], [("o", "i", 84, CLARO), ("atalho", "i", 84, CLARO)], XE, 190)
        E.frase(c, t, C["s17.a"], [("trocou", "i", 76, BR), ("i", "g", 70, BR), ("por", "i", 76, BR), ("j", "g", 70, BR), ("e", "i", 76, BR),
                                   ("nada", "i", 76, BR), ("mudou?", "g", 70, CLARO)], XE, 330, passo=0.15)
        E.foco(c, t, C["s17.b"], 0.5, lambda a: E.formula(c, "A^t = A", XE, 500, 150, "g", BR, a))
        E.foco(c, t, C["s17.c"], 0.5, lambda a: E.formula(c, "i + j = j + i", XE, 760, 110, "g", CLARO, a))
        G = E.matriz(c, t, C["s17.d"], A, 1450, 560, 150, escuro=True)
        if t >= C["s17.d"]:
            p = ep(t, C["s17.d"] + 0.5, 0.6)
            M.line(c, G.x[0] - 70, G.y[0] - 70, lerp(G.x[0] - 70, G.x[1] + 70, p), lerp(G.y[0] - 70, G.y[1] + 70, p), CLARO, 0.8, 5, dash=[14, 10])
            E.foco(c, t, C["s17.d"] + 0.6, 0.5, lambda a: E.centro(c, "espelho", 1450, G.y1 + 110, 64, "i", CLARO, a))
    E.saida(c, t, C["s18"] - 0.1, parte1)
    if t >= C["s18"]:
        E.foco(c, t, C["s18.a"], 0.5, lambda a: E.formula(c, "aᵢⱼ  ↔  aⱼᵢ", XE, 320, 140, "g", BR, a))
        E.frase(c, t, C["s18.b"], [("não", "g", 90, ERRADO), ("vale", "i", 96, BR), ("para", "i", 96, BR), ("i − j", "g", 90, BR)], XE, 560)
        E.foco(c, t, C["s18.c"], 0.5, lambda a: (E.escreve(c, "a₁₂ = 1 − 2 = −1", XE, 760, 90, "g", BR, a)))
        E.foco(c, t, C["s18.d"], 0.5, lambda a: (E.escreve(c, "a₂₁ = 2 − 1 = 1", XE, 900, 90, "g", CLARO, a)))
        E.foco(c, t, C["s18.d"] + 0.5, 0.5, lambda a: E.escreve(c, "≠", 1050, 840, 140, "g", ERRADO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s19"] + 0.8, 0.5, lambda a: E.pilula(c, "A é 2 × 2", XE + 200, 340, 54, estilo="g", a=a))
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, "aᵢⱼ = 2i − j", XE, 560, 150, "g", TINTA, a))
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.formula(c, "A + A^t = ?", XE, 820, 140, "g", COR, a))
    E.relogio(c, t, C["s20.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    s = 120
    E.frase(c, t, C["s21"], [("2i", "g", 70, COR), ("=", "g", 70), ("duas", "i", 74), ("vezes", "i", 74), ("a", "i", 74), ("linha", "g", 70, LIN)], XE, 180)

    def contas():
        E.foco(c, t, C["s21.a"], 0.5, lambda a: E.escreve(c, "linha 1:  2 − 1 = 1   2 − 2 = 0", 900, 470, 58, "b", TINTA, a))
        E.foco(c, t, C["s21.b"], 0.5, lambda a: E.escreve(c, "linha 2:  4 − 1 = 3   4 − 2 = 2", 900, 610, 58, "b", TINTA, a))
    E.saida(c, t, C["s22"] - 0.1, contas)
    xa = 470 if t < C["s22"] else lerp(470, 330, ep(t, C["s22"], 0.6))
    E.matriz(c, t, C["s21.a"], Q, xa, 540, s, tl=[C["s21.a"], C["s21.b"]], nome="A" if t < C["s22"] else None)
    if t >= C["s22"]:
        E.sinal(c, t, C["s22.a"] - 0.2, "+", 580, 530, 100)
        E.matriz(c, t, C["s22.a"], QT, 830, 540, s, cores={("c", 0): LIN, ("c", 1): COL})
        E.foco(c, t, C["s22.a"], 0.5, lambda a: E.formula(c, "A^t", 830, 380, 70, "g", COR, a, "center"))
        E.sinal(c, t, C["s22.b"] - 0.2, "=", 1080, 530, 100)
        E.matriz(c, t, C["s22.b"], A, 1340, 540, s, cores={(i, j): CERTO for i in range(2) for j in range(2)})
        E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "a matriz do i + j", 1340, 820, 52, estilo="b", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s23.a", "linha antes da coluna"), ("s23.b", "soma: lugar com lugar"), ("s23.c", "número: multiplica todos"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 400, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 400, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 92)], 500, y)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], ps("próxima aula", "i", 84), XE, 330)
    E.frase(c, t, C["s24.a"], [("Multiplicar", "g", 150, COR)], XE, 490)
    E.frase(c, t, C["s24.a"] + 0.3, [("matrizes", "g", 150, COR)], XE, 640)
    E.foco(c, t, C["s24.b"], 0.5, lambda a: E.escreve(c, "AB ≠ BA", XE, 790, 90, "g", TINTA, a))
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, tabela=b_tabela, endereco=b_endereco, lei=b_lei, transposta=b_transposta,
              somar=b_somar, numero=b_numero, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
