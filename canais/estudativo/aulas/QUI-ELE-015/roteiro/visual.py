"""Visual — Estudativo · QUI-ELE-015: balancear por oxirredução.
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha Eletroquímica (cabeçalho da QUI-ELE-001). Oxidação em âmbar,
redução em azul; elétrons por fórmula embaixo da espécie; o cruzamento é um X de setas turquesa que leva cada número de
elétrons para o coeficiente do outro (peça local cruza(), candidata ao kit). Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-015_balancear_por_oxirreducao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("regra", "metodo", "forno", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OXI, RED = "#E08A00", Q.ELETRON

EQ0 = "Al + Cu^2+ -> Al^3+ + Cu"
EQ1 = "2 Al + 3 Cu^2+ -> 2 Al^3+ + 3 Cu"
F0 = "Fe2O3 + CO -> Fe + CO2"
F1 = "Fe2O3 + 3 CO -> 2 Fe + 3 CO2"
FE = "2 Fe2O3 + 3 CO -> 4 Fe + 3 CO2"
Q0 = "Fe + O2 -> Fe2O3"
Q1 = "4 Fe + 3 O2 -> 2 Fe2O3"
# contas da aula
assert Q.lados(EQ1)[0] == Q.lados(EQ1)[1] and 2 * 3 == 3 * 2 == 6 and 3 * 2 == 2 * 3   # 6 e⁻; carga +6 = +6
assert Q.lados(F1)[0] == Q.lados(F1)[1] and 3 * 2 == 6 and 3 + 3 == 3 * 2              # O: 6 = 6
assert Q.lados(FE)[0]["O"] == 9 and Q.lados(FE)[1]["O"] == 6                           # o erro não fecha
assert Q.lados(Q1)[0] == Q.lados(Q1)[1] and 4 * 3 == 3 * 2 * 2 == 12                   # 12 e⁻


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """palavras de uma frase; sinais (=, −, +, ×, →) vão na grotesca, porque a serifada itálica não tem esses glifos"""
    return [((w, "g", size * 0.9, cor) if w in ("=", "−", "+", "×", "→", "≠") else (w, "b", size * 0.9, cor) if ("-" in w and est == "i") else (w, est, size, cor)) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def tag(c, t, t0, g, nox, size, fundo=TINTA, dy=0):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, nox, g["cx"], g["topo"] - size * 1.0 + dy, size, "g", fundo=fundo, a=a))


def eletron(c, x, y, r=14, a=1.0):
    E.bola(c, x, y, r, Q.ELETRON, a)
    M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, a, max(2.5, r * 0.16))


def eletrons_fila(c, t, t0, x, y, n, r=15, dx=40, passo=0.12):
    for k in range(n):
        E.foco(c, t, t0 + passo * k, 0.3, lambda a, k=k: eletron(c, x + dx * k, y, r, a))


def cruza(c, t, t0, A, B, C_, D, cor=None, d=0.6):
    """X de setas: A → B e C_ → D (o número de elétrons de um vira o coeficiente do outro)"""
    cor = cor or E.COR
    for k, (P0, P1) in enumerate(((A, B), (C_, D))):
        p = ease_io(prog(t, t0 + 0.3 * k, d))
        if p > 0:
            M.arrow(c, P0[0], P0[1], P1[0], P1[1], cor, 1, 7, 26, p)


def lista(c, t, itens, x, y0, dy, size=66, r=40):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + r, y - size * 0.38, r, a=a), centro(c, str(i + 1), x + r, y - size * 0.38 + r * 0.42, r * 1.2, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + r * 2 + 40, y, passo=0.1)


def troca(c, t, t1, s0, s1, x, y, size, align="center", cores=None, escuro=False, t0=None):
    """a equação s0 vira s1 em t1 (sai desfocando e a nova entra)"""
    if t < t1:
        Q.formula_em(c, t, t0 if t0 is not None else -10, s0, x, y, size, align=align, escuro=escuro)
    else:
        Q.formula_em(c, t, t1, s1, x, y, size, align=align, cores=cores, escuro=escuro)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    y, s = 440, 130
    G = Q.grupos(EQ0, W / 2, y, s, "center")
    Q.formula_em(c, t, C["s01.a"], EQ0, W / 2, y, s, align="center")
    if t < C["s02"]:
        def s01():
            for k, (i, j) in enumerate(((0, 2), (1, 3))):
                tk = C["s01.b"] + 0.6 * k
                for g in (G[i], G[j]):
                    E.foco(c, t, tk, 0.4, lambda a, g=g: E.pilula(c, "1", g["cx"], g["base"] + 70, 46, "g", fundo=TINTA2, a=a))
            E.frase(c, t, C["s01.b"] + 1.4, ps("parece balanceada", "i", 64, TINTA2), W / 2, 720, "center", 0.1)
            E.foco(c, t, C["s01.c"], 0.4, lambda a: E.pilula(c, "mas está errada", W / 2, 860, 64, "g", fundo=ERRADO, a=a))
        E.saida(c, t, C["s02"] - 0.1, s01)
        return
    if t < C["s02.d"]:
        def s02a():
            E.foco(c, t, C["s02.a"], 0.4, lambda a: E.pilula(c, "perde 3 e⁻", G[0]["cx"], G[0]["base"] + 70, 46, "g", fundo=OXI, a=a))
            eletrons_fila(c, t, C["s02.a"] + 0.3, G[0]["cx"] - 40, G[0]["base"] + 160, 3)
            E.foco(c, t, C["s02.b"], 0.4, lambda a: E.pilula(c, "ganha 2 e⁻", G[1]["cx"], G[1]["base"] + 70, 46, "g", fundo=RED, a=a))
            eletrons_fila(c, t, C["s02.b"] + 0.3, G[1]["cx"] - 20, G[1]["base"] + 160, 2)
            if t >= C["s02.c"]:
                q = ep(t, C["s02.c"], 0.4)
                ex, ey = G[0]["cx"] + 40, G[0]["base"] + 160
                c.drawCircle(ex, ey, 32 + 4 * math.sin(t * 6), M.paint(ERRADO, q, stroke=6))
                E.foco(c, t, C["s02.c"] + 0.2, 0.4, lambda a: E.pilula(c, "sobra elétron", ex + 240, ey + 100, 54, "g", fundo=ERRADO, a=a))
        E.saida(c, t, C["s02.d"] - 0.1, s02a)
        return
    E.frase(c, t, C["s02.d"], ps("até o fim da aula:", "i", 70), XE, 720, passo=0.12)
    E.frase(c, t, C["s02.d"] + 1.0, [("elétrons perdidos", "g", 64, OXI), ("=", "g", 64, TINTA2), ("elétrons ganhos", "g", 64, RED)], XE, 830, passo=0.15)
    pilula_em(c, t, C["s02.e"], "+ atalho para conferir", 1500, 960, 50, E.COR)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 76, TINTA2) + [("duas", "g", 70, COR), ("coisas", "i", 76, TINTA2)], XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("se oxida", "g", 72, OXI)] + ps("perde elétrons, Nox sobe", "i", 72), XE, 380, passo=0.1)
    E.frase(c, t, C["s03.b"], [("se reduz", "g", 72, RED)] + ps("ganha elétrons, Nox desce", "i", 72), XE, 500, passo=0.1)
    E.frase(c, t, C["s03.c"], ps("e", "i", 72) + [("balancear por tentativas", "g", 66, COR)], XE, 700, passo=0.1)
    E.foco(c, t, C["s03.c"] + 1.0, 0.4, lambda a: Q.formula(c, "2 H2 + O2 -> 2 H2O", XE + 120, 880, 100, TINTA, a, cores={"coef": E.COR}))


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04"], ps("a regra é uma só", "i", 70, TINTA2), W / 2, 200, "center", 0.12)
            E.frase(c, t, C["s04.a"], ps("elétrons não somem nem aparecem", "i", 70), W / 2, 310, "center", 0.1)
            E.frase(c, t, C["s04.b"], ps("o que um perde, o outro ganha", "i", 70), W / 2, 410, "center", 0.1)
            E.foco(c, t, C["s04.c"], 0.6, lambda a: E.balanca(c, W / 2, 800, "perdidos", "ganhos", 0, a, 80))
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    y, s = 300, 120
    G = Q.grupos(EQ0, W / 2, y, s, "center")
    if t < C["s07"]:
        EQX = "2 Al + 3 Cu^2+ -> Al^3+ + Cu"
        if t < C["s06.a"]:
            Q.formula_em(c, t, C["s05"], EQ0, W / 2, y, s, align="center")
            tag(c, t, C["s05.a"], G[0], "perde 3", 40, OXI)
            tag(c, t, C["s05.b"], G[1], "ganha 2", 40, RED)
        else:
            G2 = Q.grupos(EQX, W / 2, y, s, "center")
            Q.formula_em(c, t, C["s06.a"], EQX, W / 2, y, s, align="center", cores={"coef": E.COR})

        E.frase(c, t, C["s05"] + 0.8, ps("quantos de cada, para empatar?", "i", 58, TINTA2), W / 2, 450, "center", 0.1)
        # 2 alumínios = 6 elétrons; 3 cobres = 6 elétrons
        for k in range(2):
            Q.atomo_em(c, t, C["s05.c"] + 0.2 * k, 330, 590 + 130 * k, 50, "Al")
            eletrons_fila(c, t, C["s05.c"] + 0.4 + 0.2 * k, 420, 590 + 130 * k, 3, 15, 42, 0.08)
        E.foco(c, t, C["s05.c"] + 1.0, 0.4, lambda a: E.formula(c, "2 × 3 = 6", 330, 900, 66, "g", OXI, a))
        for k in range(3):
            Q.atomo_em(c, t, C["s05.d"] + 0.2 * k, 1200, 570 + 110 * k, 46, "Cu")
            eletrons_fila(c, t, C["s05.d"] + 0.4 + 0.2 * k, 1290, 570 + 110 * k, 2, 15, 42, 0.08)
        E.foco(c, t, C["s05.d"] + 1.0, 0.4, lambda a: E.formula(c, "3 × 2 = 6", 1200, 940, 66, "g", RED, a))
        E.foco(c, t, C["s05.e"], 0.4, lambda a: E.selo(c, W / 2, 760, 56, True, a))
        if t >= C["s06"]:
            # cruzamento: o 3 do alumínio vai para o cobre, o 2 do cobre vai para o alumínio
            G2 = Q.grupos(EQX, W / 2, y, s, "center")
            E.foco(c, t, C["s06.a"], 0.3, lambda a: (E.pilula(c, "3", G2[1]["cx"], G2[1]["topo"] - 60, 44, "g", fundo=OXI, a=a), E.pilula(c, "2", G2[3]["cx"], G2[3]["topo"] - 60, 44, "g", fundo=RED, a=a)))
            cruza(c, t, C["s06.a"] + 0.3, (G2[1]["cx"] + 20, G2[1]["topo"] - 40), (G2[2]["cx"], G2[2]["topo"] + 10), (G2[3]["cx"] - 20, G2[3]["topo"] - 40), (G2[0]["cx"], G2[0]["topo"] + 10), E.COR)
            E.foco(c, t, C["s06.c"], 0.4, lambda a: E.pilula(c, "cruzar", W / 2, 1010, 60, "g", fundo=E.COR, a=a))
        return
    Q.formula_em(c, t, C["s07"], EQ1, W / 2, 470, 108, align="center", cores={"coef": E.COR})
    E.foco(c, t, C["s07.a"] + 1.4, 0.4, lambda a: E.pilula(c, "6 e⁻ saem, 6 e⁻ entram", W / 2, 700, 56, "g", fundo=TINTA, a=a))


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    E.frase(c, t, C["s08"], ps("o método:", "i", 72, TINTA2) + [("quatro passos", "g", 66, COR)], XE, 200, passo=0.12)
    lista(c, t, [(C["s08.a"], ps("Nox: quem", "i", 62) + [("sobe", "g", 58, OXI)] + ps("e quem", "i", 62) + [("desce", "g", 58, RED)]),
                 (C["s08.b"], ps("elétrons por fórmula, nos reagentes:", "i", 62)),
                 (C["s08.c"], [("cruze", "g", 62, COR)] + ps("os números", "i", 62)),
                 (C["s08.d"], ps("feche o resto por", "i", 62) + [("tentativas", "g", 58)])], XE, 380, 150, 62, 42)
    E.foco(c, t, C["s08.b"] + 2.0, 0.4, lambda a: E.pilula(c, "variação do Nox × átomos do elemento", 1180, 600, 44, "g", fundo=TINTA, a=a))


# ---------------- alto-forno ----------------
def b_forno(c, t, C, b):
    y, s = 400, 120
    G = Q.grupos(F0, W / 2, y, s, "center")
    if t < C["s11"]:
        def topo():
            if t < C["s10.b"]:
                Q.formula_em(c, t, C["s09.a"], F0, W / 2, y, s, align="center")
                GG = G
            elif t < C["s10.e"]:
                Q.formula_em(c, t, C["s10.b"], "2 Fe2O3 + 6 CO -> Fe + CO2", W / 2, y, s, align="center", cores={"coef": E.COR})
                GG = Q.grupos("2 Fe2O3 + 6 CO -> Fe + CO2", W / 2, y, s, "center")
            else:
                Q.formula_em(c, t, C["s10.e"], "Fe2O3 + 3 CO -> Fe + CO2", W / 2, y, s, align="center", cores={"coef": E.COR})
            gfe, gc = (G[0], G[2])
            tag(c, t, C["s09.b"], gfe, "+3 → 0", 40, RED, dy=-20)
            E.foco(c, t, C["s09.b"] + 0.4, 0.4, lambda a: E.escreve(c, "3 por átomo", 300, 570, 50, "i", TINTA2, a))
            E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "dois ferros", 300, 640, 50, "i", TINTA2, a))
            E.foco(c, t, C["s09.d"], 0.4, lambda a: E.formula(c, "3 × 2 = 6 e⁻", 300, 750, 70, "g", RED, a))
            tag(c, t, C["s10.a"], gc, "+2 → +4", 40, OXI, dy=-20)
            E.foco(c, t, C["s10.a"] + 0.4, 0.4, lambda a: E.formula(c, "2 × 1 = 2 e⁻", 1040, 750, 70, "g", OXI, a))
            if C["s10.b"] <= t < C["s10.e"]:
                GG = Q.grupos("2 Fe2O3 + 6 CO -> Fe + CO2", W / 2, y, s, "center")
                cruza(c, t, C["s10.b"], (1200, 690), (GG[0]["cx"] + 10, GG[0]["base"] + 20), (480, 690), (GG[3]["cx"], GG[3]["base"] + 20), E.COR)
            E.foco(c, t, C["s10.d"], 0.4, lambda a: E.formula(c, "2 e 6 ÷ 2 → 1 e 3", W / 2, 940, 70, "g", TINTA, a, "center"))
        E.saida(c, t, C["s11"] - 0.1, topo)
        return
    # s11: feche por tentativas
    E.frase(c, t, C["s11"], ps("feche por tentativas", "i", 66, TINTA2), W / 2, 240, "center", 0.1)
    if t < C["s11.b"]:
        Q.formula_em(c, t, C["s11"], "Fe2O3 + 3 CO -> Fe + CO2", W / 2, 500, 108, align="center", cores={"coef": E.COR})
    elif t < C["s11.c"]:
        Q.formula_em(c, t, C["s11.b"], "Fe2O3 + 3 CO -> 2 Fe + CO2", W / 2, 500, 108, align="center", cores={"coef": E.COR})
    else:
        Q.formula_em(c, t, C["s11.c"], F1, W / 2, 500, 108, align="center", cores={"coef": E.COR})
    E.foco(c, t, C["s11.b"], 0.4, lambda a: E.escreve(c, "2 ferros de cada lado", 300, 680, 50, "i", TINTA2, a))
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.escreve(c, "3 carbonos de cada lado", 1100, 680, 50, "i", TINTA2, a))
    if t >= C["s11.d"]:
        E.foco(c, t, C["s11.d"], 0.4, lambda a: E.formula(c, "O: 3 + 3 = 6", 560, 880, 70, "g", TINTA, a, "center"))
        E.foco(c, t, C["s11.d"] + 1.0, 0.4, lambda a: E.formula(c, "3 × 2 = 6", 1360, 880, 70, "g", TINTA, a, "center"))
        E.foco(c, t, C["s11.d"] + 1.6, 0.4, lambda a: E.selo(c, W / 2, 860, 50, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("esquecer quantos átomos a fórmula tem", "i", 60), XE + 450, 190, passo=0.1)
    Q.formula_em(c, t, C["s12.a"] + 0.4, "Fe2O3", 560, 420, 150, align="center")
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.formula(c, "3 e⁻", 560, 560, 70, "g", ERRADO, a, "center"))
    E.foco(c, t, C["s12.b"] + 1.0, 0.4, lambda a: E.escreve(c, "em vez de 6", 470, 640, 50, "i", ERRADO, a))
    if t >= C["s12.c"]:
        Q.formula_em(c, t, C["s12.c"], FE, W / 2, 790, 100, align="center", cores={"coef": ERRADO})
    if t >= C["s13"]:
        E.foco(c, t, C["s13.b"], 0.4, lambda a: E.formula(c, "O: 6 + 3 = 9", 1280, 410, 66, "g", ERRADO, a, "center"))
        E.foco(c, t, C["s13.b"] + 0.6, 0.4, lambda a: E.formula(c, "3 × 2 = 6", 1280, 500, 66, "g", ERRADO, a, "center"))
        E.foco(c, t, C["s13.b"] + 1.0, 0.4, lambda a: E.selo(c, 1580, 450, 44, False, a))
    E.frase(c, t, C["s13.c"], ps("a variação vale", "i", 60) + [("por átomo:", "g", 56, COR)], W / 2, 940, "center", 0.1)
    E.frase(c, t, C["s13.d"], [("multiplique", "g", 56, COR)] + ps("pelo índice do elemento", "i", 60), W / 2, 1030, "center", 0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("o atalho para conferir", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        E.frase(c, t, C["s14.a"], ps("com íons:", "i", 64, CLARO) + [("some as cargas", "g", 60, BR)] + ps("de cada lado", "i", 64, CLARO), W / 2, 290, "center", 0.1)
        y, s = 520, 120
        Q.formula_em(c, t, C["s14.a"] + 0.6, EQ1, W / 2, y, s, align="center", escuro=True, cores={"carga": E.CLARO})
        E.foco(c, t, C["s14.b"], 0.4, lambda a: E.formula(c, "3 × (+2) = +6", 560, 700, 70, "g", BR, a, "center"))
        E.foco(c, t, C["s14.c"], 0.4, lambda a: E.formula(c, "2 × (+3) = +6", 1360, 700, 70, "g", BR, a, "center"))
        E.foco(c, t, C["s14.d"], 0.4, lambda a: E.formula(c, "=", W / 2, 700, 90, "g", CLARO, a, "center"))
        E.foco(c, t, C["s14.d"] + 0.3, 0.4, lambda a: E.selo(c, W / 2, 860, 54, True, a))
        return
    E.frase(c, t, C["s15.a"], ps("a carga vem dos elétrons,", "i", 64, CLARO) + [("e eles não somem", "g", 60, BR)], W / 2, 220, "center", 0.1)
    Q.formula_em(c, t, C["s15.b"], EQ0, W / 2, 470, 110, align="center", escuro=True)
    E.foco(c, t, C["s15.b"] + 0.6, 0.4, lambda a: E.formula(c, "+2 ≠ +3", W / 2, 620, 80, "g", ERRADO, a, "center"))
    E.frase(c, t, C["s15.c"], [("não", "g", 60, ERRADO), ("compensa", "i", 62, CLARO)] + ps("sem íons, como no alto-forno:", "i", 62, CLARO), W / 2, 820, "center", 0.1)
    pilula_em(c, t, C["s15.c"] + 2.2, "aí, confira pelos átomos", W / 2, 940, 48, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s16"] + 1.0, ps("o ferro e o gás oxigênio formam o óxido da ferrugem", "i", 54, TINTA2), XE, 290, passo=0.06)
    Q.formula_em(c, t, C["s16.a"], Q0, XE, 520, 150)
    E.frase(c, t, C["s16.b"], ps("balanceie pela", "i", 64) + [("oxirredução", "g", 60, COR)], XE, 720, passo=0.1)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1500, cy=700, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    y, s = 380, 130
    G = Q.grupos(Q0, W / 2, y, s, "center")
    if t < C["s19.a"]:
        Q.formula_em(c, t, C["s18"], Q0, W / 2, y, s, align="center")
    elif t < C["s19.b"]:
        Q.formula_em(c, t, C["s19.a"], "4 Fe + 3 O2 -> Fe2O3", W / 2, y, s, align="center", cores={"coef": E.COR})
    if t < C["s19.b"]:
        tag(c, t, C["s18.a"], G[0], "0 → +3", 40, OXI)
        E.foco(c, t, C["s18.a"] + 0.5, 0.4, lambda a: E.formula(c, "perde 3", G[0]["cx"], 560, 60, "g", OXI, a, "center"))
        tag(c, t, C["s18.b"], G[1], "0 → −2", 40, RED)
        E.foco(c, t, C["s18.c"], 0.4, lambda a: E.formula(c, "2 × 2 = 4", G[1]["cx"], 560, 60, "g", RED, a, "center"))
        if t >= C["s19.a"]:
            E.foco(c, t, C["s19.a"], 0.4, lambda a: E.pilula(c, "cruzou: 4 e 3", W / 2, 700, 50, "g", fundo=E.COR, a=a))
        return
    if t >= C["s19.b"]:
        Q.formula_em(c, t, C["s19.b"], Q1, W / 2, 600, 130, align="center", cores={"coef": E.COR})
    E.foco(c, t, C["s19.c"], 0.4, lambda a: E.formula(c, "O: 3 × 2 = 6", 600, 800, 66, "g", TINTA, a, "center"))
    E.foco(c, t, C["s19.c"] + 1.0, 0.4, lambda a: E.formula(c, "2 × 3 = 6", 1320, 800, 66, "g", TINTA, a, "center"))
    E.foco(c, t, C["s19.d"], 0.4, lambda a: E.pilula(c, "12 e⁻ perdidos = 12 e⁻ ganhos", W / 2, 960, 52, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s19.d"] + 0.8, 0.4, lambda a: E.selo(c, W / 2 + 470, 960, 44, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s20.a"], ps("elétrons por fórmula,", "i", 66) + [("vezes o índice", "g", 62)]),
                     (C["s20.b"], [("cruze", "g", 62, COR)] + ps("os números", "i", 66)),
                     (C["s20.c"], ps("feche o resto por", "i", 66) + [("tentativas", "g", 62)])], 300, 390, 190, 66, 46)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("pilha", "g", 110, COR)], XE, 420)
    E.frase(c, t, C["s21.a"] + 0.4, [("de", "i", 110), ("Daniell", "g", 110, COR)], XE, 560)
    if t >= C["s21.a"] + 0.5:
        M.line(c, XE + 20, 780, XE + 700, 780, TINTA, ep(t, C["s21.a"] + 0.5, 0.4), 6)
        Q.eletrons(c, t, C["s21.a"] + 0.6, [(XE + 20, 780), (XE + 700, 780)], 160, 130, 18)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.b"] + 0.2, 0.4))
    E.frase(c, t, C["s21.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, regra=b_regra, metodo=b_metodo, forno=b_forno, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
