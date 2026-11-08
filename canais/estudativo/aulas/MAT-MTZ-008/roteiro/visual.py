"""Visual — Estudativo · MAT-MTZ-008: sistema como matriz (AX = B) e regra de Cramer. Junta as linguagens de MAT-MTZ-001 a 006:
E.matriz com colchetes (barras = determinante); a coluna B dos números depois do igual em âmbar; quando ela entra no lugar
da coluna de uma letra (Dx, Dy), a coluna nova chega em âmbar. Diagonais do determinante como em MAT-MTZ-003
(principal em índigo, secundária em âmbar); resultado em verde."""
from fractions import Fraction as Fr
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matrizes e Sistemas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-MTZ-008_regra_de_cramer.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("forma", "cramer", "inversa", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMB = "#D98A00"
PRI, SEC = COR, AMB


def det(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def troca(m, j, b):
    return [[b[i] if k == j else m[i][k] for k in range(2)] for i in range(2)]


A, B = [[2, 1], [1, 1]], [5, 3]
D, DX, DY = det(A), det(troca(A, 0, B)), det(troca(A, 1, B))
assert (D, DX, DY) == (1, 2, 1) and troca(A, 0, B) == [[5, 1], [3, 1]] and troca(A, 1, B) == [[2, 5], [1, 3]]
assert 2 * 2 + 1 == 5 and 2 + 1 == 3
AI = [[1, -1], [-1, 2]]
assert [sum(AI[i][k] * B[k] for k in range(2)) for i in range(2)] == [2, 1]
assert det(troca(A, 1, B)) == 1 and 2 * 1 + 2 == 4  # o erro: coluna trocada dá x = 1, y = 2 e 2 + 2 = 4
QA, QB = [[3, 2], [1, -1]], [12, -1]
QD, QDX, QDY = det(QA), det(troca(QA, 0, QB)), det(troca(QA, 1, QB))
assert (QD, QDX, QDY) == (-5, -10, -15) and Fr(QDX, QD) == 2 and Fr(QDY, QD) == 3 and 3 * 2 + 2 * 3 == 12


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


def faixa(c, x0, y0, x1, y1, cor, p, s):
    if p <= 0:
        return
    xe, ye = lerp(x0, x1, p), lerp(y0, y1, p)
    M.line(c, x0, y0, xe, ye, cor, 0.16, s * 0.78)
    M.line(c, x0, y0, xe, ye, cor, 0.9, 5)


def diag2(c, t, G, t_p, t_s):
    k = G.size * 0.55
    faixa(c, G.x[0] - k, G.y[0] - k, G.x[1] + k, G.y[1] + k, PRI, ep(t, t_p, 0.6), G.size)
    faixa(c, G.x[0] - k, G.y[1] + k, G.x[1] + k, G.y[0] - k, SEC, ep(t, t_s, 0.6), G.size)


def sistema2(c, t, t0, linhas, x, y, size, tl=None):
    E.sistema(c, t, t0, linhas, x, y, size, tl=tl)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        sistema2(c, t, C["s01.a"], ["2x + y = 5", "x + y = 3"], 330, 400, 110, tl=[C["s01.a"], C["s01.a"] + 1.4])
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.pilula(c, "só determinantes", 1350, 330, 64, estilo="g", a=a))
        E.foco(c, t, C["s01.b"] + 0.6, 0.5, lambda a: E.formula(c, "x = f{Dx}{D}", 1180, 640, 120, "g", TINTA, a))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.formula(c, "x = 2,  y = 1", XE, 900, 120, "g", CERTO, a))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 1.0, [("A · X = B", "g", 120, COR)], XE, 490)
        E.frase(c, t, C["s02.a"] + 2.6, [("regra", "i", 110), ("de", "i", 110), ("Cramer", "g", 110, COR)], XE, 650)
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


# ---------------- forma de matriz ----------------
def b_forma(c, t, C, b):
    # o sistema no alto, com as três partes coloridas
    s = 90
    E.foco(c, t, C["s04"], 0.5, lambda a: (E.escreve(c, "2", 380, 230, s, "g", COR if t >= C["s04.a"] else TINTA, a),
                                            E.escreve(c, "x +", 440, 230, s, "g", TINTA, a),
                                            E.escreve(c, "1", 640, 230, s, "g", COR if t >= C["s04.a"] else CINZA, a),
                                            E.escreve(c, "y =", 700, 230, s, "g", TINTA, a),
                                            E.escreve(c, "5", 900, 230, s, "g", AMB if t >= C["s04.c"] else TINTA, a),
                                            E.escreve(c, "1", 380, 360, s, "g", COR if t >= C["s04.a"] else CINZA, a),
                                            E.escreve(c, "x +", 440, 360, s, "g", TINTA, a),
                                            E.escreve(c, "1", 640, 360, s, "g", COR if t >= C["s04.a"] else CINZA, a),
                                            E.escreve(c, "y =", 700, 360, s, "g", TINTA, a),
                                            E.escreve(c, "3", 900, 360, s, "g", AMB if t >= C["s04.c"] else TINTA, a)))
    y, sz = 720, 110
    GA = E.matriz(c, t, C["s04.a"], A, 420, y, sz, cores={(i, j): COR for i in range(2) for j in range(2)})
    rot(c, t, C["s04.a"], GA, "A", COR)
    E.sinal(c, t, C["s04.b"], "·", 640, y - 10, 100)
    GX = E.matriz(c, t, C["s04.b"], [["x"], ["y"]], 800, y, sz)
    rot(c, t, C["s04.b"], GX, "X")
    E.sinal(c, t, C["s04.c"], "=", 980, y - 10, 100)
    GB = E.matriz(c, t, C["s04.c"], [[5], [3]], 1150, y, sz, cores={("c", 0): AMB})
    rot(c, t, C["s04.c"], GB, "B", AMB)
    for i, k in enumerate(("s05.b", "s05.c")):
        fim = C["s05.c"] if i == 0 else C["s05.d"]
        if C[k] <= t < fim:
            E.matriz_marca(c, GA, linha=i, cor=COR, p=ep(t, C[k], 0.4))
            E.matriz_marca(c, GX, coluna=0, cor=AMB, p=ep(t, C[k] + 0.2, 0.4))
    x = 1380
    E.foco(c, t, C["s05.b"], 0.5, lambda a: E.formula(c, "2·x + 1·y", x, 680, 66, "b", TINTA, a))
    E.foco(c, t, C["s05.c"], 0.5, lambda a: E.formula(c, "1·x + 1·y", x, 800, 66, "b", TINTA, a))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: E.pilula(c, "o sistema de volta", 1580, 500, 48, estilo="b", fundo=CERTO, a=a))
    E.foco(c, t, C["s05.e"], 0.5, lambda a: E.formula(c, "A · X = B", W / 2, 1000, 110, "g", COR, a, "center"))


# ---------------- Cramer ----------------
def b_cramer(c, t, C, b):
    E.frase(c, t, C["s06"], [("regra", "i", 84), ("de", "i", 84), ("Cramer", "g", 78, COR)], XE, 160)
    s, y = 96, 430
    cols = (400, 960, 1520)
    # D
    GD = E.matriz(c, t, C["s06.b"], A, cols[0], y, s, barras=True)
    rot(c, t, C["s06.b"], GD, "D", TINTA, 72)
    diag2(c, t, GD, C["s06.b"] + 0.6, C["s06.b"] + 1.1)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: E.centro(c, "2·1 − 1·1 = 1", cols[0], 680, 56, "b", TINTA, a))
    # Dx: a coluna do x vira a coluna B
    GX = E.matriz(c, t, C["s07.b"], troca(A, 0, B), cols[1], y, s, barras=True, cores={("c", 0): AMB})
    rot(c, t, C["s07.a"], GX, "Dx", TINTA, 72)
    E.foco(c, t, C["s07.a"], 0.5, lambda a: E.centro(c, "coluna do x ← B", cols[1], 600, 44, "b", AMB, a))
    if t >= C["s07.c"]:
        diag2(c, t, GX, C["s07.c"], C["s07.c"] + 0.5)
    E.foco(c, t, C["s07.c"], 0.5, lambda a: E.centro(c, "5·1 − 1·3 = 2", cols[1], 680, 56, "b", TINTA, a))
    # Dy
    GY = E.matriz(c, t, C["s08.b"], troca(A, 1, B), cols[2], y, s, barras=True, cores={("c", 1): AMB})
    rot(c, t, C["s08.a"], GY, "Dy", TINTA, 72)
    E.foco(c, t, C["s08.a"], 0.5, lambda a: E.centro(c, "coluna do y ← B", cols[2], 600, 44, "b", AMB, a))
    if t >= C["s08.c"]:
        diag2(c, t, GY, C["s08.c"], C["s08.c"] + 0.5)
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.centro(c, "2·3 − 5·1 = 1", cols[2], 680, 56, "b", TINTA, a))
    # as divisões
    E.foco(c, t, C["s09.a"], 0.5, lambda a: E.formula(c, "x = f{Dx}{D} = f{2}{1} = 2", 260, 880, 90, "g", CERTO, a))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.formula(c, "y = f{Dy}{D} = f{1}{1} = 1", 1060, 880, 90, "g", CERTO, a))
    E.foco(c, t, C["s09.c"], 0.5, lambda a: E.pilula(c, "2·2 + 1 = 5 ✓", W / 2, 1010, 44, estilo="b", fundo=CERTO, a=a))


# ---------------- pela inversa ----------------
def b_inversa(c, t, C, b):
    def parte1():
        E.frase(c, t, C["s10"], ps("outro caminho: a inversa", "i", 84), XE, 190)
        y, s = 560, 110
        GI = E.matriz(c, t, C["s10.b"], AI, 420, y, s, cores={(i, j): CERTO for i in range(2) for j in range(2)})
        rot(c, t, C["s10.b"], GI, "A^{−1}", CERTO, 70)
        E.foco(c, t, C["s10.a"], 0.5, lambda a: E.escreve(c, "a mesma A da aula de inversa", XE, 320, 56, "i", TINTA2, a))
        E.sinal(c, t, C["s10.c"], "·", 650, y - 10, 100)
        GB = E.matriz(c, t, C["s10.c"], [[5], [3]], 800, y, s, cores={("c", 0): AMB})
        rot(c, t, C["s10.c"], GB, "B", AMB, 70)
        E.sinal(c, t, C["s10.c"] + 0.2, "=", 980, y - 10, 100)
        GX = E.matriz(c, t, C["s10.c"] + 0.3, [[2], [1]], 1150, y, s, tc={(0, 0): C["s10.d"] + 0.4, (1, 0): C["s10.e"] + 0.4},
                      cores={("c", 0): CERTO})
        rot(c, t, C["s10.c"] + 0.3, GX, "X", TINTA, 70)
        for i, k in enumerate(("s10.d", "s10.e")):
            fim = C["s10.e"] if i == 0 else C["s11"]
            if C[k] <= t < fim:
                E.matriz_marca(c, GI, linha=i, cor=COR, p=ep(t, C[k], 0.4))
                E.matriz_marca(c, GB, coluna=0, cor=AMB, p=ep(t, C[k] + 0.2, 0.4))
        E.foco(c, t, C["s10.d"], 0.5, lambda a: E.formula(c, "1·5 + (−1)·3 = 2", 1300, 500, 56, "b", TINTA, a))
        E.foco(c, t, C["s10.e"], 0.5, lambda a: E.formula(c, "(−1)·5 + 2·3 = 1", 1300, 640, 56, "b", TINTA, a))
        E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "X = A^{−1} · B", XE, 930, 90, "g", COR, a))
    E.saida(c, t, C["s11"] - 0.1, parte1)
    if t >= C["s11"]:
        E.foco(c, t, C["s11.a"], 0.5, lambda a: E.formula(c, "D = 0 ?", XE, 420, 160, "g", ERRADO, a))
        E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "x = f{Dx}{0}", 1000, 420, 130, "g", ERRADO, a))
        if t >= C["s11.b"] + 0.6:
            E.risco(c, 980, 470, 1400, 300, t, C["s11.b"] + 0.6, largura=14)
        E.frase(c, t, C["s11.b"] + 0.4, ps("não dá para dividir por zero", "i", 70, ERRADO), XE, 640)
        E.foco(c, t, C["s11.c"], 0.5, lambda a: E.pilula(c, "infinitas ou nenhuma: outra aula", W / 2, 860, 54, estilo="b", fundo=TINTA2, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 104, ERRADO), ("com", "i", 96), ("isto", "i", 96)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("trocar a coluna errada", "i", 76, ERRADO), XE, 300)
    y, s = 560, 110
    G = E.matriz(c, t, C["s12.a"] + 0.3, troca(A, 1, B), 480, y, s, barras=True, cores={("c", 1): ERRADO})
    rot(c, t, C["s12.a"] + 0.3, G, "Dx ?", ERRADO, 70)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "x = f{1}{1} = 1", 900, y + 30, 90, "g", ERRADO, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "x = 1, y = 2:  2 + 2 = 4 ≠ 5", XE, 860, 80, "g", ERRADO, a))
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.formula(c, "1ª coluna: x   ·   2ª coluna: y", XE, 1000, 70, "g", COR, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], [("o", "i", 84, CLARO), ("atalho", "i", 84, CLARO)], XE, 190)
    E.frase(c, t, C["s13.a"], [("só", "i", 84, BR), ("uma", "i", 84, BR), ("letra?", "g", 78, CLARO)], XE, 340)
    E.foco(c, t, C["s13.a"] + 1.0, 0.5, lambda a: E.formula(c, "D  e  Dx", XE, 520, 130, "g", "#FFB833", a))
    E.foco(c, t, C["s13.a"] + 1.6, 0.5, lambda a: E.escreve(c, "e pronto", XE + 680, 510, 80, "i", BR, a))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "x = f{Dx}{D}     y = f{Dy}{D}", XE, 760, 100, "g", BR, a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.escreve(c, "3 × 3: quatro Sarrus → melhor escalonar", XE, 960, 60, "b", E.ERRADO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s14"] + 1.0, 0.5, lambda a: E.pilula(c, "pela regra de Cramer", XE + 300, 330, 54, estilo="g", a=a))
    sistema2(c, t, C["s14.a"], ["3x + 2y = 12", "x − y = −1"], 330, 560, 110, tl=[C["s14.a"], C["s14.b"]])
    E.relogio(c, t, C["s15.a"], cx=1500, cy=560, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    s, y = 92, 330
    cols = (400, 960, 1520)
    itens = ((QA, "D", None, "s16.a", "3·(−1) − 2·1 = −5"), (troca(QA, 0, QB), "Dx", 0, "s16.b", "12·(−1) − 2·(−1) = −10"),
             (troca(QA, 1, QB), "Dy", 1, "s16.c", "3·(−1) − 12·1 = −15"))
    for (m, nome, col, k, txt), cx in zip(itens, cols):
        G = E.matriz(c, t, C[k], m, cx, y, s, barras=True, cores={("c", col): AMB} if col is not None else None)
        rot(c, t, C[k], G, nome, TINTA, 70)
        if t >= C[k] + 0.4:
            diag2(c, t, G, C[k] + 0.4, C[k] + 1.6)
        E.foco(c, t, C[k] + 1.8, 0.5, lambda a, txt=txt, cx=cx: E.centro(c, txt, cx, 580, 46, "b", TINTA, a))
    E.foco(c, t, C["s17.a"], 0.5, lambda a: E.formula(c, "x = f{−10}{−5} = 2", 260, 780, 90, "g", CERTO, a))
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.formula(c, "y = f{−15}{−5} = 3", 1060, 780, 90, "g", CERTO, a))
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "3·2 + 2·3 = 12 ✓", W / 2, 990, 48, estilo="b", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s18.a", "A · X = B"), ("s18.b", "x = Dx / D,  y = Dy / D"), ("s18.c", "D = 0: Cramer não serve"))
        for i, (k, s) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), E.centro(c, str(i + 1), 330, y - 7, 64, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.formula(c, s, 430, y, 92, "g", TINTA, a))
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s19.a"], [("Praticando", "g", 150, COR)], XE, 470)
    E.frase(c, t, C["s19.b"], [("sistemas", "g", 120), ("lineares", "g", 120)], XE, 630)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(1000, 845, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, forma=b_forma, cramer=b_cramer, inversa=b_inversa, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
