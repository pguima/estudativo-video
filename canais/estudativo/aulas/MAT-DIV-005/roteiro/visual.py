"""Visual — Estudativo · MAT-DIV-005: calcular o MMC.
A peça central é a tabela de fatoração simultânea do kit (montar + tabela + passos + produto). Cinza = número que só desceu repetido."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, linha, montar, tabela, seta_primo, passos, produto, TAB_GRANDE, TAB_PEQUENA
import motor as M

E.usar("Matemática", "Divisibilidade, MMC e MDC")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-DIV-005_calcular_mmc.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("listar", "fatorar", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    """número dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


T12 = montar((12, 18, 30), (2, 2, 3, 3, 5))  # 180
T6 = montar((6, 8, 10), (2, 2, 2, 3, 5))  # 120


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        s0 = C["s01"]
        E.frase(c, t, s0 + 0.35, [("qual", "i", 84), ("é", "i", 84), ("o", "i", 84), ("menor", "g", 76, COR), ("número", "i", 84)], W / 2, 180, "center", passo=0.15)
        E.frase(c, t, s0 + 1.9, [("múltiplo", "g", 76, COR), ("de", "i", 84)], W / 2, 290, "center", passo=0.15)
        m = ep(t, s0 + 6.6, 0.7)  # as esferas vão para a esquerda e viram rótulo das listas
        for i, (n, k) in enumerate(((12, C["s01.a"] + 0.2), (18, C["s01.b"] + 0.1), (30, C["s01.c"] + 0.6))):
            cx, cy = lerp(560 + i * 400, 240, m), lerp(600, 430 + i * 165, m)
            r = lerp(150, 70, m) * ease_back(prog(t, k, 0.55))
            if r > 1:
                num_bola(c, str(n), cx, cy, r, round(lerp(130, 62, m)))
            for j in range(10):
                ti = s0 + 7.0 + j * 0.27 + i * 0.08
                E.foco(c, t, ti, 0.3, lambda a, j=j, n=n, cy=cy: centro(c, str(n * (j + 1)), 400 + j * 138, cy + 20, 58, "b", TINTA2, a), sobe=8)
            E.foco(c, t, s0 + 9.8 + i * 0.08, 0.3, lambda a, cy=cy: E.escreve(c, "...", 1732, cy + 20, 58, "b", TINTA2, a), sobe=8)
        E.saida(c, t, s0 + 6.5, lambda: E.frase(c, t, s0 + 5.55, [("ao", "i", 84), ("mesmo", "i", 84), ("tempo?", "g", 76, COR)], W / 2, 900, "center"), d=0.3)
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        s0 = C["s02"]
        q = ease_back(prog(t, C["s02.b"] - 0.2, 0.7))
        if q > 0:
            E.bola(c, 1480, 540, 290 * q)
        E.frase(c, t, s0 + 0.35, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("da", "i", 90), ("aula", "i", 90)], XE, 370)
        E.frase(c, t, s0 + 1.9, [("você", "i", 124), ("resolve", "g", 124)], XE, 530)
        E.frase(c, t, C["s02.a"], [("em", "i", 90), ("menos", "i", 90), ("de", "i", 90)], XE, 680, passo=0.15)
        E.frase(c, t, C["s02.a"] + 0.55, [("1", "g", 130, COR), ("minuto", "g", 130, COR)], XE, 820)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1480, 525, 84, "g", E.SOBRE, a),
                                                      centro(c, "de prova", 1480, 610, 84, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.35, [("para", "i", 84), ("acompanhar,", "i", 84)], XE, 310)
    E.frase(c, t, C["s03"] + 1.6, [("lembre", "i", 84), ("de", "i", 84)], XE, 420)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 730, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 710, 120, "i", TINTA, a))
    x, w = 960, 780
    itens = (("s03.b", "O que são", "números primos"), ("s03.c", "O que é", "o MDC"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 250
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(410, 660, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03"] + 7.9, [("procure", "i", 62), ("a", "i", 62), ("aula", "i", 62), ("no", "i", 62), ("canal", "i", 62)], x, 860, passo=0.14)


# ---------------- o que quer dizer ----------------
def b_nome(c, t, C, b):
    ys = (340, 600, 860)
    tam = 150
    letras = (("M", "ínimo", 0.0), ("M", "últiplo", 0.58), ("C", "omum", 1.52))
    p = ease_io(prog(t, C["s04.a"] - 0.15, 0.6))  # o MMC gigante se desmonta nas três iniciais
    size0 = 440
    w0 = sum(E.larg(l, "g", size0) for l, _, _ in letras) + 2 * size0 * 0.02
    xi = W / 2 - w0 / 2
    for i, (l, resto, dt) in enumerate(letras):
        x = lerp(xi, XE, p)
        y = lerp(690, ys[i], p)
        s = round(lerp(size0, tam, p))
        E.foco(c, t, C["s04"] + 0.35 + i * 0.12, 0.5, lambda a, l=l, x=x, y=y, s=s: E.escreve(c, l, x, y, s, "g", COR, a))
        xi += E.larg(l, "g", size0) + size0 * 0.02
        E.foco(c, t, C["s04.a"] + dt, 0.5, lambda a, l=l, resto=resto, i=i: E.escreve(c, resto, XE + E.larg(l, "g", tam) + 2, ys[i], tam, "g", TINTA, a))

    E.saida(c, t, C["s05"] - 0.05, lambda: (E.frase(c, t, C["s04"] + 4.1, [("o", "i", 84), ("nome", "i", 84), ("já", "i", 84), ("explica", "i", 84), ("tudo", "g", 76, COR)], 1000, 470, passo=0.15),
                                            E.frase(c, t, C["s04"] + 5.6, [("parte", "i", 84), ("por", "i", 84), ("parte", "i", 84)], 1000, 590, passo=0.16)))

    X = 930
    s0 = C["s05"]
    # múltiplo
    E.frase(c, t, C["s05.a"] + 1.1, [("o", "i", 62), ("resultado", "i", 62), ("da", "i", 62), ("tabuada,", "i", 62)], X, ys[1] - 62, passo=0.3)
    E.frase(c, t, s0 + 5.4, [("sem", "g", 60), ("parar", "g", 60), ("no", "g", 60), ("10", "g", 60, COR)], X, ys[1] + 18, passo=0.14)
    # comum
    E.frase(c, t, C["s05.b"] + 0.8, [("que", "i", 62), ("aparece", "i", 62), ("na", "i", 62), ("lista", "i", 62)], X, ys[2] - 62, passo=0.2)
    E.frase(c, t, C["s05.b"] + 2.0, [("de", "g", 60), ("todos", "g", 60, COR)], X, ys[2] + 18, passo=0.14)
    # mínimo
    E.frase(c, t, C["s05.c"] + 1.1, [("o", "i", 62), ("menor", "i", 62), ("deles,", "i", 62)], X, ys[0] - 62, passo=0.15)
    E.frase(c, t, C["s05.c"] + 1.9, [("sem", "g", 60), ("contar", "g", 60), ("o", "g", 60), ("zero", "g", 60, COR)], X, ys[0] + 18, passo=0.14)
    # o cursor segue a ordem da fala: múltiplo, comum, mínimo
    q1, q2 = ease_io(prog(t, C["s05.b"] - 0.35, 0.5)), ease_io(prog(t, C["s05.c"] - 0.35, 0.5))
    E.cursor(c, 830, lerp(lerp(ys[1], ys[2], q1) - 60, ys[0] - 60, q2), ep(t, C["s05.a"], 0.4))


# ---------------- listar ----------------
def b_listar(c, t, C, b):
    X = lambda v: 200 + v * 62
    y1, y2 = 410, 670
    # instantes de cada número medidos na onda da narração (o "quatro" da lista veio errado do alinhador)
    l4 = ((4, 1.94), (8, 2.7), (12, 3.46), (16, 4.24), (20, 5.28), (24, 6.02))
    l6 = ((6, 1.94), (12, 2.74), (18, 3.5), (24, 4.38))

    def lista():
        linha(c, t, [("vamos", "i", 80, TINTA, C["s06"] + 0.35), ("ver", "i", 80, TINTA, C["s06"] + 0.5), ("com", "i", 80, TINTA, C["s06"] + 0.7),
                     ("4", "g", 86, COR, C["s06"] + 1.27), ("e", "i", 80, TINTA, C["s06"] + 1.75), ("6", "g", 86, COR, C["s06"] + 2.07)], W / 2, 170, "center")
        E.frase(c, t, C["s06.a"], [("múltiplos", "i", 72), ("de", "i", 72), ("4", "g", 72, COR)], XE, 280, passo=0.2)
        E.frase(c, t, C["s06.b"], [("múltiplos", "i", 72), ("de", "i", 72), ("6", "g", 72, COR)], XE, 540, passo=0.2)
        for y, itens, t0 in ((y1, l4, C["s06.a"]), (y2, l6, C["s06.b"])):
            for v, dt in itens:
                marca = C["s07.a"] if v == 12 else C["s07.b"] if v == 24 else None
                ativo = marca is not None and t >= marca
                if ativo:
                    r = 88 * ease_back(prog(t, marca, 0.5))
                    E.bola(c, X(v), y - 40, r)
                E.foco(c, t, t0 + dt, 0.45, lambda a, v=v, y=y, ativo=ativo: centro(c, str(v), X(v), y, 110, "g", E.SOBRE if ativo else TINTA, a))
        # a caixa pontilhada fecha a coluna do 12: o menor comum
        p = ep(t, C["s07.c"], 0.5)
        E.caixa_pontilhada(c, X(12) - 118, y1 - 150, 236, y2 - y1 + 225, p, prog_=p)
        E.cursor(c, X(12) + 100, y2 + 50, ep(t, C["s07.c"] + 0.2, 0.4))
        E.foco(c, t, C["s07.d"], 0.5, lambda a: (centro(c, "MMC de 4 e 6 = 12", W / 2, 925, 100, "g", COR, a)))
    E.saida(c, t, C["s08"] - 0.1, lista)

    if t >= C["s08"]:
        s0 = C["s08"]
        linha(c, t, [("números", "i", 88, TINTA, s0 + 0.9), ("pequenos:", "i", 88, TINTA, s0 + 1.3), ("resolve", "g", 84, CERTO, s0 + 2.3)], XE, 270)
        linha(c, t, [("números", "i", 88, TINTA, s0 + 3.2), ("grandes:", "i", 88, TINTA, s0 + 3.5), ("não", "g", 84, ERRADO, C["s08.a"] + 0.2),
                     ("acaba", "g", 84, ERRADO, C["s08.a"] + 0.5), ("mais", "g", 84, ERRADO, C["s08.a"] + 0.9)], XE, 470)
        for i in range(9):
            E.foco(c, t, C["s08.a"] + i * 0.2, 0.3, lambda a, i=i: centro(c, str(18 * (i + 1)), 240 + i * 160, 620, 72, "b", CINZA, a), sobe=8)
        E.foco(c, t, C["s08.a"] + 1.8, 0.3, lambda a: E.escreve(c, "...", 1660, 620, 72, "b", CINZA, a), sobe=8)
        E.frase(c, t, s0 + 6.2, [("e", "i", 96), ("aí", "i", 96), ("entra", "i", 96), ("o", "i", 96), ("método", "g", 110, COR), ("de", "i", 96), ("verdade", "i", 96)],
                W / 2, 860, "center", passo=0.17)


# ---------------- fatoração simultânea ----------------
def tempos_12(C):
    tp = [C["s10.a"], C["s10.c"], C["s11.a"] + 0.8, C["s11.c"], C["s11.e"] + 0.85]
    tn = [[C["s09.b"] + 1.32, C["s09.b"] + 2.14, C["s09.b"] + 3.0],
          [C["s10.b"], C["s10.b"] + 0.82, C["s10.b"] + 1.7],
          [C["s10.d"] + 0.16, C["s10.d"] + 1.2, C["s10.d"] + 1.8],
          [C["s11.b"] + 0.06, C["s11.b"] + 0.82, C["s11.b"] + 1.58],
          [C["s11.d"] + 0.04, C["s11.d"] + 0.74, C["s11.d"] + 1.28],
          [C["s11.f"] + 0.04, C["s11.f"] + 0.56, C["s11.f"] + 0.98]]
    tb = [C["s09.b"], C["s10.a"], C["s10.c"], C["s11.a"], C["s11.c"], C["s11.e"]]
    ti = [C["s10.a"], C["s10.c"], C["s11.a"], C["s11.c"], C["s11.e"]]
    return tp, tn, tb, ti


def b_fatorar(c, t, C, b):
    def titulo():
        E.frase(c, t, C["s09.a"], [("fatoração", "g", 170, COR)], W / 2, 500, "center")
        E.frase(c, t, C["s09.a"] + 0.8, [("simultânea", "i", 180)], W / 2, 680, "center")
        E.frase(c, t, C["s09"] + 3.2, [("todos", "g", 70), ("ao", "i", 76), ("mesmo", "i", 76), ("tempo", "i", 76)], W / 2, 850, "center", passo=0.22)
    E.saida(c, t, C["s09"] + 5.2, titulo)
    if t < C["s09"] + 5.4:
        return
    tp, tn, tb, ti = tempos_12(C)
    final = C["s11"] + 11.2
    tabela(c, t, T12, tn, tp, tb, cor_fim=CERTO if t >= final else None)
    for i in range(5):
        seta_primo(c, t, ti[i], ti[i + 1] if i < 4 else C["s12"], i)

    # à direita: lado a lado, a regra, as contas de cada passo
    X = 1130
    E.saida(c, t, C["s09.c"] - 0.2, lambda: E.frase(c, t, C["s09.b"], [("lado", "i", 96), ("a", "i", 96), ("lado", "i", 96)], X, 480), d=0.3)

    def regra():
        E.frase(c, t, C["s09.c"], [("sempre", "i", 80), ("o", "i", 80)], X, 250, passo=0.2)
        E.frase(c, t, C["s09.c"] + 0.75, [("menor", "g", 84, COR), ("primo", "g", 84, COR)], X, 355, passo=0.3)
        E.frase(c, t, C["s09.c"] + 1.5, [("que", "i", 80), ("divide", "i", 80)], X, 475, passo=0.2)
        E.frase(c, t, C["s09.c"] + 2.1, [("pelo", "g", 66), ("menos", "g", 66), ("um", "g", 66)], X, 565, passo=0.2)
        E.frase(c, t, C["s09"] + 16.1, [("não", "i", 80), ("divide?", "i", 80)], X, 760, passo=0.2)
        E.frase(c, t, C["s09.d"], [("desce", "g", 76, CINZA), ("repetido", "g", 76, CINZA)], X, 860, passo=0.2)
    E.saida(c, t, C["s10.a"] - 0.2, regra, d=0.3)

    passos(c, t, T12, ti, tp, tn, C["s12"] - 0.1)
    E.saida(c, t, C["s12"] - 0.1, lambda: E.frase(c, t, final, [("tudo", "i", 76), ("virou", "i", 76), ("1:", "g", 72), ("acabou", "g", 72, CERTO)], X, 760, passo=0.2))

    if t >= C["s12"]:
        p = ep(t, C["s12.a"] + 1.0, 0.5)  # a coluna dos primos
        s, y0, dy, xp = TAB_GRANDE["s"], TAB_GRANDE["y0"], TAB_GRANDE["dy"], TAB_GRANDE["xp"]
        E.caixa_pontilhada(c, xp - 70, y0 - s * 0.95, 140, dy * 4 + s * 1.2, p, COR, prog_=p)
        E.frase(c, t, C["s12.a"] + 0.1, [("a", "i", 80), ("multiplicação", "i", 80)], X, 230, passo=0.2)
        E.frase(c, t, C["s12.a"] + 0.8, [("de", "g", 66), ("todos", "g", 66), ("os", "g", 66), ("primos", "g", 66, COR)], X, 325, passo=0.22)
        v = C["s12.b"]
        produto(c, t, T12, (v, v + 0.55, v + 1.45, v + 2.35, v + 3.2), X + 40, 540)
        E.foco(c, t, C["s12.c"], 0.5, lambda a: (E.escreve(c, "MMC =", X, 790, 76, "g", TINTA, a), num_bola(c, "180", 1560, 765, 150, 116, a)))


# ---------------- diferença ----------------
def b_diferenca(c, t, C, b):
    E.saida(c, t, C["s13"] + 2.7, lambda: E.frase(c, t, C["s13"] + 0.35, [("se", "i", 100), ("você", "i", 100), ("viu", "i", 100), ("a", "i", 100), ("aula", "i", 100), ("de", "i", 100), ("MDC", "g", 96, COR)],
                                                  W / 2, 560, "center", passo=0.2), d=0.3)
    E.frase(c, t, C["s13"] + 2.9, [("repare", "i", 84), ("na", "i", 84), ("diferença", "g", 78, COR)], W / 2, 180, "center")
    M.line(c, W / 2, 270, W / 2, 900, FIO, ep(t, C["s13.a"] - 0.2, 0.4), 3)

    def lado(cx, nome, conta, nums, cheios, t0, l1, l2, t1, t2):
        E.foco(c, t, t0, 0.5, lambda a: centro(c, nome, cx, 380, 130, "g", COR if nome == "MMC" else TINTA, a))
        E.foco(c, t, t0 + 0.2, 0.5, lambda a: E.pilula(c, conta, cx, 460, 48, estilo="b", fundo=TINTA, cor=BR, a=a))
        for i, n in enumerate(nums):
            cx_i, ti = cx - 180 + i * 180, t1 + i * 0.22
            r = 76 * ease_back(prog(t, ti, 0.5))
            if r > 1:
                if n in cheios:
                    num_bola(c, str(n), cx_i, 610, r, 66, cor=COR)
                else:
                    c.drawCircle(cx_i, 610, r, M.paint(CINZA, 1.0, stroke=4))
                    centro(c, str(n), cx_i, 634, 66, "g", CINZA, ep(t, ti, 0.4))
        E.frase(c, t, t1, [(l1, "i", 66)], cx, 780, "center", passo=0.2)
        E.frase(c, t, t2, [(l2, "g", 88, COR)], cx, 880, "center")

    s0 = C["s13"]
    lado(480, "MDC", "÷ 2", (12, 18, 30), (12, 18, 30), C["s13.a"], "o primo divide", "todos", s0 + 6.1, s0 + 6.49)
    lado(1440, "MMC", "÷ 2", (6, 9, 15), (6,), C["s13.b"], "basta dividir", "um", s0 + 8.93, s0 + 9.67)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    s0 = C["s14"]
    E.frase(c, t, s0 + 0.35, [("o", "i", 84), ("erro", "g", 76, ERRADO), ("mais", "i", 84), ("comum", "i", 84)], XE, 180, passo=0.14)
    E.frase(c, t, C["s14.a"], [("é", "i", 84), ("parar", "g", 76, ERRADO), ("antes", "g", 76, ERRADO), ("da", "g", 76, ERRADO), ("hora", "g", 76, ERRADO)], 870, 180, passo=0.2)
    e = C["s14.e"]
    tn = [[s0 + 0.3] * 3, [s0 + 0.3] * 3, [s0 + 0.3] * 3, [s0 + 0.3] * 3, [C["s14.b"], C["s14.b"] + 0.7, C["s14.b"] + 1.22], [e, e + 0.2, e + 0.4]]
    tp = [s0 + 0.3] * 4 + [C["s14.c"]]
    tabela(c, t, T12, tn, tp, [s0 + 0.3] * 5 + [e - 0.1], TAB_PEQUENA, cor_fim=CERTO, cor_primo={4: ERRADO if t < e else CERTO})
    g = TAB_PEQUENA
    y = g["y0"] + 4 * g["dy"]
    p = ep(t, C["s14.b"], 0.4) * (1 - ep(t, e - 0.3, 0.3))
    E.caixa_pontilhada(c, 170, y - 88, 435, 118, p, ERRADO, prog_=p)

    X = 960
    E.frase(c, t, s0 + 5.53, [("acha", "i", 76), ("que", "i", 76), ("acabou,", "i", 76)], X, 340, passo=0.14)
    E.frase(c, t, s0 + 6.73, [("esquece", "i", 76), ("o", "i", 76), ("último", "i", 76), ("5", "g", 84, ERRADO)], X, 450, passo=0.22)
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.escreve(c, "2 × 2 × 3 × 3 = 36", X, 620, 78, "g", ERRADO, a))
    if t >= s0 + 9.95:  # o risco cai sobre o 36
        w, w36 = E.larg("2 × 2 × 3 × 3 = 36", "g", 78), E.larg("36", "g", 78)
        E.risco(c, X + w - w36 - 12, 636, X + w + 12, 556, t, s0 + 9.95, largura=10)
    E.frase(c, t, s0 + 9.95, [("36", "g", 62, ERRADO), ("nem", "i", 66), ("é", "i", 66), ("múltiplo", "i", 66), ("de", "i", 66), ("30", "g", 62)], X, 720, passo=0.2)
    E.frase(c, t, s0 + 11.93, [("só", "i", 76), ("pare", "i", 76), ("quando", "i", 76)], X, 860, passo=0.16)
    E.frase(c, t, e, [("todos", "g", 76, CERTO), ("virarem", "g", 76, CERTO), ("1", "g", 76, CERTO)], X, 950, passo=0.2)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def formula():
        s0 = C["s15"]
        E.frase(c, t, s0 + 0.35, [("agora,", "i", 90, CLARO), ("o", "i", 90, CLARO), ("atalho", "i", 90, CLARO)], W / 2, 230, "center")
        E.frase(c, t, C["s15.a"], [("para", "i", 90, BR), ("dois", "g", 84, BR), ("números", "g", 84, BR)], W / 2, 350, "center")
        v = C["s15.b"]
        linha(c, t, [("MMC", "g", 170, BR, v), ("×", "g", 130, CLARO, v + 0.68), ("MDC", "g", 170, BR, v + 1.28)], W / 2, 620, "center")
        linha(c, t, [("=", "g", 120, CLARO, v + 2.3), ("um", "i", 120, BR, v + 3.28), ("número", "i", 120, BR, v + 3.5),
                     ("×", "g", 100, CLARO, v + 3.9), ("o", "i", 120, BR, v + 4.4), ("outro", "i", 120, BR, v + 4.55)], W / 2, 840, "center")
    E.saida(c, t, C["s16"] - 0.1, formula)

    def exemplo():
        s0 = C["s16"]
        xs = linha(c, t, [("só", "i", 110, CLARO, s0 + 0.35), ("12", "g", 120, BR, s0 + 0.79), ("e", "i", 110, CLARO, s0 + 1.17),
                          ("18", "g", 120, BR, s0 + 1.35), ("30", "g", 120, CINZA, s0 + 1.89)], XE, 220)
        if t >= s0 + 2.29:
            M.line(c, xs[4] - 12, 234, xs[4] + E.larg("30", "g", 120) + 12, 142, ERRADO, 1.0, 12, progress=ep(t, s0 + 2.29, 0.35))
        E.foco(c, t, C["s16.a"], 0.5, lambda a: E.pilula(c, "MDC = 6", 1400, 180, 76, estilo="g", fundo=E.COR, cor=BR, a=a))
        E.frase(c, t, s0 + 5.45, [("para", "i", 72, CLARO), ("achar", "i", 72, CLARO), ("o", "i", 72, CLARO), ("MMC:", "g", 68, BR)], XE, 370, passo=0.15)
        E.frase(c, t, s0 + 7.43, [("multiplique", "i", 72, CLARO), ("os", "i", 72, CLARO), ("dois", "i", 72, CLARO)], 790, 370, passo=0.16)
        E.frase(c, t, s0 + 8.93, [("e", "i", 72, CLARO), ("divida", "i", 72, CLARO), ("pelo", "i", 72, CLARO), ("MDC", "g", 68, BR)], 790, 460, passo=0.16)
        v = C["s16.b"]
        y = 670
        linha(c, t, [("12", "g", 110, BR, v), ("×", "g", 86, CLARO, v + 0.38), ("18", "g", 110, BR, v + 0.6),
                     ("=", "g", 96, CLARO, v + 1.5), ("216", "g", 110, BR, v + 1.56)], XE, y)
        if t >= C["s16.c"]:
            p = ep(t, C["s16.c"], 0.5)
            M.arrow(c, 1000, y - 40, 1250, y - 40, CLARO, p, 5, 16, p)
            E.foco(c, t, C["s16.c"], 0.4, lambda a: E.pilula(c, "÷ 6", 1115, y - 110, 56, estilo="g", fundo=E.COR, cor=BR, a=a))
        E.foco(c, t, C["s16.d"], 0.5, lambda a: num_bola(c, "36", 1450, y - 45, 150, 136, a, E.COR, BR))
        E.frase(c, t, s0 + 16.49, [("esse", "i", 72, CLARO), ("é", "i", 72, CLARO), ("o", "i", 72, CLARO), ("MMC", "g", 68, BR)], 1450, 870, "center", passo=0.2)
        E.frase(c, t, s0 + 18.25, [("sem", "i", 72, CLARO), ("fatorar", "g", 68, BR), ("nada", "g", 68, BR)], 1450, 970, "center", passo=0.3)
    if t >= C["s16"]:
        E.saida(c, t, C["s17"] - 0.1, exemplo)

    if t >= C["s17"]:
        s0 = C["s17"]
        E.frase(c, t, s0 + 0.35, [("um", "i", 90, CLARO), ("caso", "i", 90, CLARO), ("ainda", "i", 90, CLARO), ("mais", "g", 84, BR), ("rápido", "g", 84, BR)], W / 2, 220, "center", passo=0.16)
        E.frase(c, t, s0 + 2.4, [("o", "i", 80, CLARO), ("maior", "g", 74, BR), ("já", "i", 80, CLARO), ("é", "i", 80, CLARO), ("múltiplo", "i", 80, CLARO),
                                 ("do", "i", 80, CLARO), ("menor?", "g", 74, BR)], W / 2, 410, "center", passo=0.28)
        E.frase(c, t, s0 + 4.8, [("ele", "i", 80, CLARO), ("mesmo", "i", 80, CLARO), ("é", "i", 80, CLARO), ("o", "i", 80, CLARO), ("MMC", "g", 74, BR)], W / 2, 530, "center", passo=0.28)
        v = C["s17.a"]
        linha(c, t, [("MMC", "g", 120, BR, v), ("de", "i", 110, CLARO, v + 0.68), ("5", "g", 120, BR, v + 0.8), ("e", "i", 110, CLARO, v + 1.2), ("20?", "g", 120, BR, v + 1.5)], 260, 810)
        E.foco(c, t, C["s17.b"], 0.5, lambda a: (centro(c, "=", 1230, 810, 110, "g", CLARO, a), num_bola(c, "20", 1440, 770, 136, 120, a, E.COR, BR)))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    s0 = C["s18"]
    E.frase(c, t, s0 + 0.3, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 200)
    E.frase(c, t, C["s18.a"], [("qual", "i", 110), ("é", "i", 110), ("o", "i", 110)], XE, 400, passo=0.15)
    linha(c, t, [("MMC", "g", 170, COR, C["s18.a"] + 0.55), ("de", "i", 130, TINTA, C["s18.a"] + 1.35)], XE, 590)
    linha(c, t, [("6,", "g", 170, TINTA, s0 + 3.72), ("8", "g", 170, TINTA, s0 + 4.5), ("e", "i", 140, TINTA, s0 + 4.8), ("10?", "g", 170, TINTA, s0 + 5.2)], XE, 810)
    # relógio de pausa: enche em 3 segundos
    t0 = C["s19.a"]
    r = 210 * ease_back(prog(t, t0, 0.6))
    if r > 0:
        cx, cy = 1490, 440
        E.bola(c, cx, cy, r)
        f = M.clamp(prog(t, t0 + 0.8, 3.0))
        if f > 0:
            E.arco(c, cx, cy, r + 34, -90, 360 * f, TINTA, 10)
        for dx in (-44, 44):
            M.rrect(c, cx + dx - 22, cy - 80, 44, 160, 12, E.SOBRE, ep(t, t0 + 0.2, 0.4))
        E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, "pause o vídeo", cx, cy + r + 120, 64, "i", TINTA, a))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a_, b_, c_, d_, e_ = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"], C["s20.e"]
    ini = C["s20"] + 0.35
    tp = [a_ + 0.4, b_ + 0.45, c_ + 0.45, d_ + 1.0, e_ + 0.45]  # o "dois", "três", "cinco" de cada "por..."
    tn = [[ini, ini + 0.12, ini + 0.24],
          [a_ + 1.12, a_ + 1.82, a_ + 2.44],
          [b_ + 1.2, b_ + 1.92, b_ + 2.64],
          [c_ + 1.2, c_ + 1.96, c_ + 2.54],
          [d_ + 1.88, d_ + 2.48, d_ + 2.98],
          [e_ + 1.14, e_ + 1.7, e_ + 2.24]]
    tb = [ini, a_, b_, c_, d_ + 0.6, e_]
    final = e_ + 2.24
    tabela(c, t, T6, tn, tp, tb, cor_fim=CERTO if t >= final else None)
    ti = [a_, b_, c_, d_ + 0.6, e_]
    for i in range(5):
        seta_primo(c, t, ti[i], ti[i + 1] if i < 4 else C["s21"], i)
    passos(c, t, T6, ti, tp, tn, C["s21"] - 0.1)

    if t >= C["s21"]:
        X = 1130
        p = ep(t, C["s21"] + 0.8, 0.5)
        s, y0, dy, xp = TAB_GRANDE["s"], TAB_GRANDE["y0"], TAB_GRANDE["dy"], TAB_GRANDE["xp"]
        E.caixa_pontilhada(c, xp - 70, y0 - s * 0.95, 140, dy * 4 + s * 1.2, p, COR, prog_=p)
        E.frase(c, t, C["s21"] + 0.35, [("agora", "i", 88), ("multiplique", "g", 76, COR)], X, 290, passo=0.3)
        v = C["s21.a"]
        produto(c, t, T6, (v, v + 0.4, v + 1.2, v + 2.0, v + 2.8), X + 40, 520)
        E.foco(c, t, C["s21.b"], 0.5, lambda a: (E.escreve(c, "MMC =", X, 770, 76, "g", TINTA, a), num_bola(c, "120", 1560, 745, 150, 116, a, CERTO, BR)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.35, [("resumindo", "i", 96, COR)], W / 2, 210, "center")
        linhas = (("s22.a", [("divida", "i", 84), ("pelo", "i", 84), ("menor", "g", 80, COR), ("primo", "g", 80, COR)]),
                  ("s22.b", [("quem", "i", 84), ("não", "i", 84), ("divide", "i", 84), ("desce", "g", 80, COR), ("repetido", "g", 80, COR)]),
                  ("s22.c", [("multiplique", "i", 84), ("a", "i", 84), ("coluna", "g", 80, COR), ("quando", "i", 84), ("tudo", "i", 84), ("virar", "i", 84), ("1", "g", 80, COR)]))
        for i, (k, partes) in enumerate(linhas):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 220, y - 28, 56, 64, a))
            E.frase(c, t, C[k] + 0.1, partes, 310, y, passo=0.16)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    s0 = C["s23"]
    E.frase(c, t, s0 + 0.6, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s23.a"], [("MDC", "g", 140, COR), ("em", "i", 130)], XE, 450)
    E.frase(c, t, C["s23.a"] + 0.9, [("problemas", "g", 140, COR)], XE, 590)
    E.frase(c, t, s0 + 4.3, [("dividir", "i", 72), ("em", "i", 72), ("partes", "i", 72), ("iguais", "i", 72)], XE, 720, passo=0.22)
    E.foco(c, t, C["s23.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1400, 400, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=a))
    p = ease_io(prog(t, C["s23.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1700, 1560, p), lerp(720, 445, p), ep(t, C["s23.b"] + 0.2, 0.4), TINTA)
    E.frase(c, t, C["s23.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nome=b_nome, listar=b_listar, fatorar=b_fatorar, diferenca=b_diferenca,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
