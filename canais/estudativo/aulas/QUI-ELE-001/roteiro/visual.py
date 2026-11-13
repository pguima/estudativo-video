"""Visual — Estudativo · QUI-ELE-001: número de oxidação. Primeira aula da trilha Eletroquímica e Radioatividade.

Segue a LINGUAGEM VISUAL DA QUÍMICA do cabeçalho do visual.py da QUI-MIS-001 (fórmula sempre com Q.formula, átomos CPK,
elétron azul Q.ELETRON, erro com risco/selo, palco só no atalho).

LINGUAGEM VISUAL DA TRILHA ELETROQUÍMICA (as aulas QUI-ELE-001 a 007 copiam daqui):
- NOX = etiqueta em cima do símbolo, na grotesca: pílula escura (TINTA) com o valor e o sinal ("+1", "−2"); o Nox que se
  procura é "x" numa pílula turquesa (E.COR) e vira o valor na esfera quando a conta fecha. Embaixo do símbolo, em cinza-tinta,
  o Nox vezes o índice ("+2", "−8"): é a parte de cada elemento na soma. Peça local nox_tags() (candidata ao kit).
- SOMA DOS NOX = E.formula em linha ("+2 + x − 8 = 0"), uma linha por passo, com o resultado na esfera turquesa.
- ELÉTRON = bolinha azul Q.ELETRON com "−"; elétron que passa de um átomo a outro anda num arco (peça local voa_eletron).
- OXIDAÇÃO e REDUÇÃO (a partir da 002): oxidação = âmbar OXI, seta do Nox para cima, "perde e⁻"; redução = azul RED (o do
  elétron), seta para baixo, "ganha e⁻". Agente = pílula com contorno na mesma cor.
- PILHA (a partir da 003): Q.pilha_daniell; elétrons azuis só no fio; íons na ponte salina em turquesa (+) e cinza (−).
  ÂNODO = TINTA "ânodo −"; CÁTODO = turquesa "cátodo +" (o kit já faz assim).
- ESCADA DE POTENCIAIS (a partir da 004): eixo vertical, maior E° em cima, hidrogênio no zero, cada degrau com o par e o valor.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-001_numero_de_oxidacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "regras", "sulfurico", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# contas da aula
assert Q.contar("H2SO4") == {"H": 2, "S": 1, "O": 4}
assert 2 * (+1) + 4 * (-2) + 6 == 0                 # S = +6
assert Q.contar("KMnO4") == {"K": 1, "Mn": 1, "O": 4}
assert 1 + 4 * (-2) + 7 == 0                        # Mn = +7
assert 4 * (-2) + 6 == -2                           # S no sulfato
assert 1 + 1 * (-2) + 1 == 0                        # erro: x = +1
assert 1 + 3 * (-2) + 5 == 0 and 3 * 1 + (-3) == 0  # HNO3: N = +5; NH3: N = −3


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """palavras de uma frase; sinais (=, −, +, ×, →) vão na grotesca, porque a serifada itálica não tem esses glifos"""
    return [((w, "g", size * 0.9, cor) if w in ("=", "−", "+", "×", "→", "≠") else (w, "b", size * 0.9, cor) if ("-" in w and est == "i") else (w, est, size, cor)) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def nox_tags(c, t, s, x, y, size, tags, align="left", escuro=False):
    """etiquetas de Nox sobre os grupos da fórmula: tags = {i: (nox, t_nox, parte, t_parte, destaque)}.
    nox na pílula em cima; parte (Nox × índice) embaixo, em cinza; destaque=True = pílula turquesa (o x procurado)."""
    G = Q.grupos(s, x, y, size, align)
    for i, (nox, tn, parte, tp, dest) in tags.items():
        g = G[i]
        cy = g["topo"] - size * 0.32
        fundo = E.COR if dest else (TINTA if not escuro else "#3A3B46")
        if tn is not None:
            E.foco(c, t, tn, 0.4, lambda a, g=g, cy=cy, nox=nox, fundo=fundo: E.pilula(c, nox, g["cx"], cy, size * 0.24, "g", fundo=fundo, a=a))
        if parte and tp is not None:
            cor = (CLARO if escuro else COR) if dest else (TINTA2 if not escuro else "#C8CAD2")
            E.foco(c, t, tp, 0.4, lambda a, g=g, parte=parte, cor=cor: E.formula(c, parte, g["cx"], g["base"] + size * 0.42, size * 0.26, "g", cor, a, "center"))
    return G


def voa_eletron(c, t, t0, A, B, d=1.0, alto=120, r=16):
    """um elétron azul que sai de A e pousa em B num arco"""
    p = ease_io(prog(t, t0, d))
    if t < t0:
        return
    mx, my = (A[0] + B[0]) / 2, min(A[1], B[1]) - alto
    x = (1 - p) ** 2 * A[0] + 2 * (1 - p) * p * mx + p ** 2 * B[0]
    y = (1 - p) ** 2 * A[1] + 2 * (1 - p) * p * my + p ** 2 * B[1]
    E.bola(c, x, y, r, Q.ELETRON, 1)
    M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, 1, 3)


def eletron(c, x, y, r=14, a=1.0):
    E.bola(c, x, y, r, Q.ELETRON, a)
    M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, a, max(2.5, r * 0.16))


def lista(c, t, itens, x, y0, dy, size=66, r=40):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + r, y - size * 0.38, r, a=a), centro(c, str(i + 1), x + r, y - size * 0.38 + r * 0.42, r * 1.2, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + r * 2 + 40, y, passo=0.1)


def conta(c, t, t0, s, x, y, size, cor=TINTA, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def s01():
        fx, fy, fs = XE + 20, 600, 300
        cores = {"indice": E.COR} if C["s01.b"] <= t < C["s01.c"] else ({"S": E.COR} if t >= C["s01.c"] else None)
        Q.formula_em(c, t, C["s01.a"], "H2SO4", fx, fy, fs, cores=cores)
        E.foco(c, t, C["s01.a"] + 0.6, 0.4, lambda a: E.escreve(c, "ácido sulfúrico", fx + 10, fy + 140, 60, "i", TINTA2, a))
        G = Q.grupos("H2SO4", fx, fy, fs)
        if t >= C["s01.c"]:
            g = G[1]
            bola_txt(c, t, C["s01.c"], "+6", g["cx"], g["topo"] - 110, 92, 96)
            E.foco(c, t, C["s01.c"] + 0.5, 0.4, lambda a: E.pilula(c, "Nox", g["cx"] + 190, g["topo"] - 110, 46, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s01.d"], ps("de onde sai esse", "i", 76) + [("seis?", "g", 70, COR)], 1760, 960, "right", 0.12)
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("calcular", "i", 72), ("o", "i", 72), ("Nox", "g", 70, COR)]),
                 (C["s02.c"], [("o", "i", 72), ("manganês", "g", 70), ("em", "i", 72)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], XE, 450, 170)
    Q.formula_em(c, t, C["s02.c"] + 0.8, "KMnO4", XE + 700, 620, 96, cores={"Mn": E.COR})


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 76, TINTA2) + [("duas", "g", 70, COR), ("coisas", "i", 76, TINTA2)], XE, 200, passo=0.12)
    # 1: o mais eletronegativo puxa os elétrons
    E.foco(c, t, C["s03.a"], 0.5, lambda a: (E.bola(c, XE + 40, 340, 40, a=a), centro(c, "1", XE + 40, 357, 48, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.a"] + 0.1, ps("o mais", "i", 64) + [("eletronegativo", "g", 60, COR)] + ps("puxa os elétrons", "i", 64), XE + 120, 362, passo=0.1)
    hx, clx, yy = 520, 760, 530
    Q.atomo_em(c, t, C["s03.a"] + 0.6, hx, yy, 58, "H")
    Q.atomo_em(c, t, C["s03.a"] + 0.8, clx, yy, 82, "Cl")
    if t >= C["s03.a"] + 1.0:
        M.line(c, hx + 58, yy, clx - 82, yy, Q.LIGA, ep(t, C["s03.a"] + 1.0, 0.3), 10)
        k = ease_io(prog(t, C["s03.a"] + 1.6, 1.2))
        px = lerp((hx + clx) / 2, clx - 110, k)
        a = ep(t, C["s03.a"] + 1.2, 0.3)
        eletron(c, px - 4, yy - 22, 13, a)
        eletron(c, px + 4, yy + 22, 13, a)
    # 2: íon tem carga
    E.foco(c, t, C["s03.b"], 0.5, lambda a: (E.bola(c, XE + 40, 740, 40, a=a), centro(c, "2", XE + 40, 757, 48, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, ps("um", "i", 64) + [("íon", "g", 60, COR)] + ps("tem carga", "i", 64), XE + 120, 762, passo=0.1)
    Q.atomo_em(c, t, C["s03.c"] - 0.3, 560, 910, 70, "Na")
    E.foco(c, t, C["s03.c"], 0.4, lambda a: Q.formula(c, "Na^+", 700, 935, 90, TINTA, a))
    E.foco(c, t, C["s03.c"] + 0.4, 0.4, lambda a: E.pilula(c, "carga +1", 1010, 905, 48, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s03.a"] + 0.3, 0.8, lambda a: E.simbolo(c, 1560, 380, 150 * a, giro=-6 * math.sin(t * 0.5)), blur=0)


# ---------------- o que é Nox ----------------
def b_ideia(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04"], ps("o sal de cozinha:", "i", 70, TINTA2), XE, 200, passo=0.12)
            E.foco(c, t, C["s04"] + 0.8, 0.4, lambda a: Q.formula(c, "NaCl", XE + 560, 202, 80, TINTA, a))
            nx, cx_, yy = 640, 1240, 560
            Q.atomo_em(c, t, C["s04"] + 0.4, nx, yy, 100, "Na")
            Q.atomo_em(c, t, C["s04"] + 0.6, cx_, yy, 120, "Cl")
            voa_eletron(c, t, C["s04.a"], (nx + 60, yy - 70), (cx_ - 60, yy - 90), 1.4, 180, 20)
            E.frase(c, t, C["s04.a"] + 0.2, ps("o sódio", "i", 60) + [("entrega", "g", 56, COR)] + ps("um elétron", "i", 60), W / 2, 330, "center", 0.1)
            bola_txt(c, t, C["s04.b"], "+1", nx, yy + 210, 64, 66)
            bola_txt(c, t, C["s04.c"], "−1", cx_, yy + 210, 64, 66, TINTA)
            E.frase(c, t, C["s04.c"] + 1.2, ps("essas cargas são o", "i", 68) + [("número de oxidação", "g", 62, COR)], W / 2, 960, "center", 0.1)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    # s05 e s06: HCl, o par puxado
    hx, clx, yy = 700, 1180, 560
    E.frase(c, t, C["s05"] + 0.2, ps("e quando ninguém entrega de vez?", "i", 68, TINTA2), XE, 200, passo=0.1)
    E.foco(c, t, C["s05.a"] - 0.4, 0.4, lambda a: Q.formula(c, "HCl", 1700, 205, 80, TINTA, a, "right"))
    Q.atomo_em(c, t, C["s05"] + 0.4, hx, yy, 76, "H")
    Q.atomo_em(c, t, C["s05"] + 0.6, clx, yy, 120, "Cl")
    if t >= C["s05.a"]:
        M.line(c, hx + 76, yy, clx - 120, yy, Q.LIGA, ep(t, C["s05.a"], 0.3), 12)
    k1 = ease_io(prog(t, C["s05.b"], 1.2)) * 0.6
    k2 = ease_io(prog(t, C["s06.a"], 1.0))
    k = k1 + 0.4 * k2
    if t >= C["s05.a"]:
        a = ep(t, C["s05.a"] + 0.2, 0.3)
        px = lerp((hx + clx) / 2 - 20, clx - 60, k)
        py = lerp(yy, yy - 150, k2)
        eletron(c, px - 5, py - 24, 15, a)
        eletron(c, px + 5, py + 24, 15, a)
    E.saida(c, t, C["s06"] - 0.1, lambda: E.frase(c, t, C["s05.a"] + 0.2, ps("dividem um", "i", 60) + [("par", "g", 56, Q.ELETRON)] + ps("de elétrons", "i", 60), W / 2, 820, "center", 0.1))
    if C["s05.b"] <= t < C["s06"]:
        E.foco(c, t, C["s05.b"], 0.4, lambda a: E.pilula(c, "mais eletronegativo: puxa", clx, yy - 190, 42, "g", fundo=E.COR, a=a))
    if t < C["s06"]:
        return
    E.foco(c, t, C["s06.a"], 0.4, lambda a: E.pilula(c, "finge que levou o par inteiro", clx, yy - 270, 42, "b", fundo=TINTA2, a=a))
    bola_txt(c, t, C["s06.b"], "+1", hx, yy + 200, 60, 62)
    bola_txt(c, t, C["s06.c"], "−1", clx, yy + 200, 60, 62, TINTA)

    def defin():
        E.frase(c, t, C["s06.d"], [("Nox", "g", 64, COR)] + ps("= a carga que o átomo teria", "i", 60), W / 2, 930, "center", 0.1)
        E.frase(c, t, C["s06.d"] + 1.3, ps("se cada ligação virasse uma", "i", 60) + [("entrega", "g", 56, COR)], W / 2, 1010, "center", 0.1)
    defin()


# ---------------- regras ----------------
def regra(c, t, t0, n, partes, y):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 40, y - 26, 42, a=a), centro(c, str(n), XE + 40, y - 7, 50, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.1, partes, XE + 120, y, passo=0.1)


def b_regras(c, t, C, b):
    if t < C["s09"]:
        def r12():
            E.frase(c, t, C["s07"], ps("quatro regras", "i", 72, TINTA2), XE, 180, passo=0.12)
            regra(c, t, C["s07.a"], 1, ps("substância simples:", "i", 66) + [("Nox zero", "g", 62, COR)], 330)
            for i, (f, x) in enumerate((("O2", 520), ("Fe", 920), ("H2", 1300))):
                Q.formula_em(c, t, C["s07.a"] + 1.2 + 0.3 * i, f, x, 560, 130, align="center")
                if t >= C["s07.b"]:
                    G = Q.grupos(f, x, 560, 130, "center")
                    bola_txt(c, t, C["s07.b"] + 0.15 * i, "0", G[0]["cx"], G[0]["topo"] - 60, 40, 50)
            E.frase(c, t, C["s07.b"] + 1.0, ps("átomos iguais não puxam elétron um do outro", "i", 52, TINTA2), XE + 120, 680, passo=0.08)
            regra(c, t, C["s08.a"], 2, ps("íon de um átomo só:", "i", 66) + [("a própria carga", "g", 62, COR)], 830)
            Q.formula_em(c, t, C["s08.b"], "Cu^2+", 1500, 840, 120)
            E.foco(c, t, C["s08.b"] + 0.5, 0.4, lambda a: E.pilula(c, "Nox +2", 1600, 940, 46, "g", fundo=TINTA, a=a))
        E.saida(c, t, C["s09"] - 0.1, r12)
        return
    if t < C["s10"]:
        def r3():
            regra(c, t, C["s09.a"], 3, ps("valores", "i", 68) + [("fixos", "g", 64, COR)], 200)
            linhas = (("s09.b", ("Na", "K"), "família 1", "+1"), ("s09.c", ("H",), "com ametal", "+1"),
                      ("s09.d", ("O",), "quase sempre", "−2"), ("s09.e", ("Cl",), "no fim da fórmula", "−1"))
            for i, (k, els, txt, v) in enumerate(linhas):
                y = 360 + i * 150
                for j, el in enumerate(els):
                    Q.atomo_em(c, t, C[k] + 0.15 * j, XE + 150 + 130 * j, y - 24, 50, el)
                E.frase(c, t, C[k] + 0.2, [(txt, "i", 60, TINTA2)], XE + 440, y)
                E.foco(c, t, C[k] + 0.4, 0.4, lambda a, v=v, y=y: E.pilula(c, v, 1300, y - 20, 56, "g", fundo=TINTA, a=a))
            pilula_em(c, t, C["s09.f"], "exceção: água oxigenada (outra aula)", 1380, 960, 42, TINTA2, "b")
        E.saida(c, t, C["s10"] - 0.1, r3)
        return
    regra(c, t, C["s10.a"], 4, ps("a mais", "i", 68) + [("importante", "g", 64, COR)], 220)
    E.frase(c, t, C["s10.b"], ps("numa substância,", "i", 76), XE, 420, passo=0.12)
    E.frase(c, t, C["s10.b"] + 0.8, ps("a soma dos Nox dá", "i", 76), XE, 520, passo=0.12)
    bola_txt(c, t, C["s10.b"] + 1.6, "0", XE + 790, 494, 62, 80)
    E.frase(c, t, C["s10.c"], ps("num íon, a soma dá", "i", 76), XE, 760, passo=0.12)
    E.frase(c, t, C["s10.c"] + 0.8, [("a carga do íon", "g", 72, COR)], XE, 860)
    Q.formula_em(c, t, C["s10.c"] + 1.2, "SO4^2-", 1450, 860, 150)


# ---------------- H2SO4 ----------------
FX, FY, FS = W / 2, 470, 230


def b_sulfurico(c, t, C, b):
    cores = {"S": E.COR}
    Q.formula_em(c, t, C["s11"], "H2SO4", FX, FY, FS, align="center", cores=cores)
    nox_tags(c, t, "H2SO4", FX, FY, FS, {
        1: ("x", C["s11.a"], "x", C["s11.b"], True),
        0: ("+1", C["s11.c"], "+2", C["s11.d"], False),
        2: ("−2", C["s11.e"], "−8", C["s11.f"], False)}, "center")
    E.foco(c, t, C["s11.d"], 0.4, lambda a: E.escreve(c, "2 × (+1)", 430, 760, 44, "b", TINTA2, a))
    E.foco(c, t, C["s11.f"], 0.4, lambda a: E.escreve(c, "4 × (−2)", 1310, 760, 44, "b", TINTA2, a))
    if t < C["s12"]:
        return
    y = 880
    conta(c, t, C["s12.a"], "+2 + x − 8 = 0", W / 2, y, 80, TINTA, "center")
    if t >= C["s12.b"]:
        def l2():
            conta(c, t, C["s12.b"], "x − 6 = 0", 640, 1010, 70, TINTA2, "center")
        l2()
    if t >= C["s12.c"]:
        conta(c, t, C["s12.c"], "x =", 1150, 1010, 70, TINTA, "right")
        bola_txt(c, t, C["s12.c"] + 0.3, "+6", 1250, 985, 62, 66)
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.pilula(c, "o seis do começo", 1560, 985, 44, "g", fundo=TINTA, a=a))


# ---------------- KMnO4 ----------------
def violeta(t):
    return "#6A1B7A"


def b_permanganato(c, t, C, b):
    fx, fy, fs = 820, 470, 220
    Q.formula_em(c, t, C["s13"], "KMnO4", fx, fy, fs, align="center", cores={"Mn": E.COR})
    E.foco(c, t, C["s13"] + 0.6, 0.4, lambda a: E.escreve(c, "permanganato de potássio", 470, 180, 56, "i", TINTA2, a))
    Q.bequer(c, t, C["s13.a"], 1620, 700, 300, 340, 0.7, violeta, te=C["s13.a"] + 0.2, d=1.0, graduacao=False)
    E.foco(c, t, C["s13.a"] + 0.6, 0.4, lambda a: centro(c, "pó roxo, desinfeta", 1620, 790, 42, "i", TINTA2, a))
    nox_tags(c, t, "KMnO4", fx, fy, fs, {
        0: ("+1", C["s13.b"], "+1", C["s13.b"] + 0.4, False),
        2: ("−2", C["s13.c"], "−8", C["s13.c"] + 0.4, False),
        1: ("x", C["s13.d"], "x", C["s13.d"] + 0.3, True)}, "center")
    if t < C["s14"]:
        return
    conta(c, t, C["s14.a"], "+1 + x − 8 = 0", fx, 870, 80, TINTA, "center")
    conta(c, t, C["s14.b"], "x − 7 = 0", 560, 1000, 66, TINTA2, "center")
    conta(c, t, C["s14.c"], "Mn:", 1000, 1000, 66, TINTA, "right")
    bola_txt(c, t, C["s14.c"] + 0.3, "+7", 1100, 976, 60, 64)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s15.a"], ps("esquecer o índice", "i", 70), XE + 450, 190, passo=0.12)
    fx, fy, fs = 560, 520, 200
    Q.formula_em(c, t, C["s15.a"] + 0.6, "H2SO4", fx, fy, fs, align="center", cores={"indice": E.COR})
    G = Q.grupos("H2SO4", fx, fy, fs, "center")

    def errado():
        conta(c, t, C["s15.b"], "+1 + x − 2 = 0", 1400, 470, 76, ERRADO, "center")
        conta(c, t, C["s15.c"], "x = +1", 1400, 600, 76, ERRADO, "center")
        if t >= C["s15.c"] + 0.8:
            E.risco(c, 1180, 620, 1620, 420, t, C["s15.c"] + 0.8, largura=10)
    E.saida(c, t, C["s16.b"] - 0.1, errado)
    if t >= C["s16.a"]:
        for k, g in enumerate((G[0], G[2])):
            pad = 12
            q = ep(t, C["s16.a"] + 0.3 * k, 0.4)
            E.caixa_pontilhada(c, g["x0"] - pad, g["topo"] - pad, g["x1"] - g["x0"] + 2 * pad, g["base"] - g["topo"] + 2 * pad, q, E.COR, prog_=q)
        E.foco(c, t, C["s16.a"] + 0.3, 0.4, lambda a: Q.atomo(c, 300, 740, 34, "H", a))
        E.foco(c, t, C["s16.a"] + 0.4, 0.4, lambda a: Q.atomo(c, 380, 740, 34, "H", a))
        for k in range(4):
            E.foco(c, t, C["s16.a"] + 0.7 + 0.12 * k, 0.4, lambda a, k=k: Q.atomo(c, 560 + 80 * k, 740, 34, "O", a))
    if t >= C["s16.b"]:
        conta(c, t, C["s16.b"], "2 × (+1) + x + 4 × (−2) = 0", 1350, 520, 60, TINTA, "center")
        conta(c, t, C["s16.b"] + 0.8, "x = +6", 1350, 640, 70, TINTA, "center")
        E.foco(c, t, C["s16.b"] + 1.0, 0.4, lambda a: E.selo(c, 1580, 618, 40, True, a))
    E.frase(c, t, C["s16.c"], [("multiplique", "g", 66, COR)] + ps("o Nox pelo índice antes de somar", "i", 66), W / 2, 960, "center", 0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s18"]:
        def s17():
            E.frase(c, t, C["s17"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 150, "center", 0.12)
            E.frase(c, t, C["s17.a"], ps("de cabeça:", "i", 66, CLARO) + [("some o que conhece", "g", 62, BR)], W / 2, 270, "center", 0.12)
            E.frase(c, t, C["s17.b"], ps("o Nox que falta leva a soma até", "i", 58, CLARO) + [("zero", "g", 56, BR)], W / 2, 360, "center", 0.1)
            Q.formula_em(c, t, C["s17.c"] - 0.4, "H2SO4", W / 2, 620, 190, align="center", escuro=True, cores={"S": E.CLARO})
            nox_tags(c, t, "H2SO4", W / 2, 620, 190, {0: ("+1", C["s17.c"], "+2", C["s17.c"] + 0.3, False),
                                                    2: ("−2", C["s17.c"] + 0.5, "−8", C["s17.c"] + 0.8, False)}, "center", escuro=True)
            conta(c, t, C["s17.d"], "+2 − 8 = −6", W / 2 - 60, 900, 84, BR, "right")
            E.foco(c, t, C["s17.e"], 0.4, lambda a: E.escreve(c, "falta", W / 2 + 10, 900, 70, "i", CLARO, a))
            bola_txt(c, t, C["s17.e"] + 0.3, "+6", W / 2 + 290, 872, 66, 70)
        E.saida(c, t, C["s18"] - 0.1, s17)
        return
    if t < C["s19"]:
        def s18():
            E.frase(c, t, C["s18.a"], ps("num íon, a soma vai até a", "i", 66, CLARO) + [("carga", "g", 62, BR)], W / 2, 190, "center", 0.12)
            Q.formula_em(c, t, C["s18.b"], "SO4^2-", W / 2, 520, 200, align="center", escuro=True, cores={"carga": E.CLARO})
            nox_tags(c, t, "SO4^2-", W / 2, 520, 200, {1: ("−2", C["s18.b"] + 0.6, "−8", C["s18.b"] + 1.0, False)}, "center", escuro=True)
            conta(c, t, C["s18.c"], "−8 → −2", W / 2 - 40, 840, 84, BR, "right")
            E.foco(c, t, C["s18.d"], 0.4, lambda a: E.escreve(c, "faltam", W / 2 + 20, 840, 70, "i", CLARO, a))
            bola_txt(c, t, C["s18.d"] + 0.3, "+6", W / 2 + 340, 812, 66, 70)
            E.foco(c, t, C["s18.d"] + 0.8, 0.4, lambda a: centro(c, "o enxofre, de novo", W / 2 + 340, 940, 46, "i", CLARO, a))
        E.saida(c, t, C["s19"] - 0.1, s18)
        return
    E.frase(c, t, C["s19.a"], ps("funciona porque a soma dos Nox", "i", 64, CLARO), W / 2, 300, "center", 0.1)
    E.frase(c, t, C["s19.a"] + 1.2, [("é a carga", "g", 66, BR)] + ps("da substância ou do íon", "i", 64, CLARO), W / 2, 400, "center", 0.1)
    E.frase(c, t, C["s19.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("dois elementos sem valor fixo", "i", 64, CLARO), W / 2, 620, "center", 0.12)
    pilula_em(c, t, C["s19.b"] + 2.0, "a questão precisa dar mais um dado", W / 2, 760, 48, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s20"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s20.a"], [("1", "g", 60, COR)] + ps("Nox do nitrogênio no ácido nítrico", "i", 60), XE, 330, passo=0.08)
    Q.formula_em(c, t, C["s20.b"], "HNO3", XE + 120, 500, 140, cores={"N": E.COR})
    E.frase(c, t, C["s20.c"], [("2", "g", 60, COR)] + ps("e na amônia", "i", 60), XE, 700, passo=0.08)
    Q.formula_em(c, t, C["s20.d"], "NH3", XE + 120, 870, 140, cores={"N": E.COR})
    if t < C["s21"]:
        Q.molecula(c, t, C["s20.d"] + 0.2, "NH3", 1450, 560, 150, passo=0.12)
    else:
        E.relogio(c, t, C["s21.a"], cx=1470, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x1, y1, s1 = 520, 360, 170
    Q.formula_em(c, t, C["s22"], "HNO3", x1, y1, s1, align="center", cores={"N": E.COR})
    nox_tags(c, t, "HNO3", x1, y1, s1, {0: ("+1", C["s22.a"], "+1", C["s22.a"] + 0.3, False),
                                        2: ("−2", C["s22.b"], "−6", C["s22.b"] + 0.3, False)}, "center")
    conta(c, t, C["s22.c"], "+1 − 6 = −5", x1, 640, 66, TINTA2, "center")
    G = Q.grupos("HNO3", x1, y1, s1, "center")
    if t >= C["s22.d"]:
        bola_txt(c, t, C["s22.d"], "+5", G[1]["cx"], 790, 62, 66)
    x2 = 1380
    Q.formula_em(c, t, C["s23"], "NH3", x2, y1, s1, align="center", cores={"N": E.COR})
    nox_tags(c, t, "NH3", x2, y1, s1, {1: ("+1", C["s23.a"], "+3", C["s23.a"] + 0.3, False)}, "center")
    G2 = Q.grupos("NH3", x2, y1, s1, "center")
    if t >= C["s23.b"]:
        bola_txt(c, t, C["s23.b"], "−3", G2[0]["cx"], 790, 62, 66, TINTA)
    E.frase(c, t, C["s23.c"], ps("o mesmo elemento, Nox diferente:", "i", 58), W / 2, 960, "center", 0.1)
    E.frase(c, t, C["s23.d"], [("é a fórmula que decide", "g", 56, COR)], W / 2, 1040, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s24.a"], ps("use os", "i", 70) + [("valores fixos", "g", 66)]),
                     (C["s24.b"], [("multiplique", "g", 66)] + ps("pelo índice", "i", 70)),
                     (C["s24.c"], ps("complete a soma até", "i", 70) + [("zero", "g", 66, COR)] + ps("ou até a carga", "i", 70))], 260, 380, 190, 66, 46)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s25.a"], [("oxidação", "g", 100, COR)], XE, 420)
    E.frase(c, t, C["s25.b"], [("e", "i", 100), ("redução", "g", 100, COR)], XE, 560)
    voa_eletron(c, t, C["s25.a"] + 0.3, (360, 800), (900, 800), 1.4, 140, 20)
    Q.atomo_em(c, t, C["s25.a"], 300, 820, 70, "Zn")
    E.foco(c, t, C["s25.b"], 0.4, lambda a: Q.formula(c, "Cu^2+", 960, 850, 90, TINTA, a))
    E.foco(c, t, C["s25.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s25.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s25.c"] + 0.2, 0.4))
    E.frase(c, t, C["s25.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, regras=b_regras, sulfurico=b_sulfurico,
              permanganato=b_permanganato, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
