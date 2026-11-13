"""Visual — Estudativo · QUI-ELE-007: praticando pilhas e corrosão (aula de prática, 4 questões).
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha Eletroquímica (cabeçalho da QUI-ELE-001): Nox em pílula sobre o
símbolo, Nox × índice embaixo; oxidação âmbar, redução azul; escada de potenciais como na QUI-ELE-004; pilha = Q.pilha_daniell.
Cada questão: enunciado à esquerda e relógio à direita na pausa; a resposta na tela seguinte. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-007_praticando_pilhas_e_corrosao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "fim"))
BR = "#FFFFFF"
OXI, RED = "#E08A00", Q.ELETRON
LARANJA, VERDE_CR = "#E8731A", "#3E8E41"

POT = {"Ag": 0.80, "Cu": 0.34, "Sn": -0.14, "Fe": -0.44, "Zn": -0.76}
PAR = {"Ag": "Ag^+/Ag", "Cu": "Cu^2+/Cu", "Sn": "Sn^2+/Sn", "Fe": "Fe^2+/Fe", "Zn": "Zn^2+/Zn"}
assert Q.contar("K2Cr2O7") == {"K": 2, "Cr": 2, "O": 7} and 2 * 1 + 2 * 6 + 7 * (-2) == 0
assert Q.lados("Cu + 2 Ag^+ -> Cu^2+ + 2 Ag")[0] == Q.lados("Cu + 2 Ag^+ -> Cu^2+ + 2 Ag")[1] and 2 * 1 == 2
assert round(POT["Ag"] - POT["Cu"], 2) == 0.46 and round(2 * POT["Ag"] - POT["Cu"], 2) == 1.26
assert round(POT["Cu"] - POT["Fe"], 2) == 0.78 and POT["Zn"] < POT["Fe"] < POT["Sn"]


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


def nox_tags(c, t, s, x, y, size, tags, align="left"):
    """tags = {i: (nox, t_nox, parte, t_parte, destaque)}: Nox em cima, Nox × índice embaixo"""
    G = Q.grupos(s, x, y, size, align)
    for i, (nox, tn, parte, tp, dest) in tags.items():
        g = G[i]
        fundo = E.COR if dest else TINTA
        if tn is not None:
            E.foco(c, t, tn, 0.4, lambda a, g=g, nox=nox, fundo=fundo: E.pilula(c, nox, g["cx"], g["topo"] - size * 0.32, size * 0.24, "g", fundo=fundo, a=a))
        if parte and tp is not None:
            E.foco(c, t, tp, 0.4, lambda a, g=g, parte=parte, dest=dest: E.formula(c, parte, g["cx"], g["base"] + size * 0.42, size * 0.26, "g", COR if dest else TINTA2, a, "center"))
    return G


def tag(c, t, t0, g, nox, size, fundo=TINTA, dy=0):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, nox, g["cx"], g["topo"] - size * 1.0 + dy, size, "g", fundo=fundo, a=a))


def conta(c, t, t0, s, x, y, size, cor=TINTA, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


class Escada:
    def __init__(self, x, y0, y1, vmin, vmax):
        self.x, self.y0, self.y1, self.vmin, self.vmax = x, y0, y1, vmin, vmax

    def y(self, v):
        return lerp(self.y1, self.y0, (v - self.vmin) / (self.vmax - self.vmin))


def v_br(v):
    return ("+" if v > 0 else "−" if v < 0 else "") + f"{abs(v):.2f}".replace(".", ",")


def escada(c, t, t0, S, els, destaque=(), riscar=(), size=52):
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    M.arrow(c, S.x, S.y1 + 30, S.x, lerp(S.y1 + 30, S.y0 - 40, p), TINTA2, 1, 5, 22, p)
    for k, el in enumerate(els):
        tk = t0 + 0.3 + 0.2 * k
        v, y = POT[el], S.y(POT[el])
        cor = E.COR if el in destaque else ("#A0522D" if el == "Fe" else TINTA)

        def deg(a, y=y, el=el, v=v, cor=cor):
            M.line(c, S.x - 36, y, S.x + 36, y, cor, a, 7 if el in destaque else 5)
            Q.formula(c, PAR[el], S.x - 64, y + size * 0.34, size, cor, a, "right")
            E.escreve(c, v_br(v), S.x + 64, y + size * 0.34, size, "g", cor, a)
        E.foco(c, t, tk, 0.4, deg)
        if el in riscar and t >= tk + 0.5:
            E.risco(c, S.x - 300, y + 20, S.x + 240, y - 20, t, tk + 0.5, largura=8)


def numero(c, t, t0, n, titulo):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 40, 150, 44, a=a), centro(c, str(n), XE + 40, 169, 54, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.2, [(titulo, "g", 60, COR)], XE + 120, 172)


def lista(c, t, itens, x, y0, dy, size=66, r=40):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + r, y - size * 0.38, r, a=a), centro(c, str(i + 1), x + r, y - size * 0.38 + r * 0.42, r * 1.2, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + r * 2 + 40, y, passo=0.1)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("quatro", "g", 110, COR)] + ps("questões", "i", 110), XE, 280, passo=0.14)
    for k, (tk, s, cor) in enumerate(((C["s01.b"], "Nox", TINTA), (C["s01.c"], "balanceamento", OXI), (C["s01.d"], "pilha", RED), (C["s01.e"], "corrosão", "#A0522D"))):
        x = XE + 60 + k * 410
        E.foco(c, t, tk, 0.4, lambda a, x=x, s=s, cor=cor, k=k: (E.bola(c, x + 150, 560, 120, cor, a), centro(c, str(k + 1), x + 150, 600, 120, "g", BR, a), centro(c, s, x + 150, 770, 56, "g", TINTA, a)))
    E.frase(c, t, C["s01.e"] + 1.0, ps("resolva comigo", "i", 70, TINTA2), W / 2, 960, "center", 0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("as ferramentas", "i", 76, TINTA2), XE, 170, passo=0.12)
    lista(c, t, [(C["s02.a"], ps("soma dos Nox:", "i", 58) + [("zero", "g", 54, COR)] + ps("ou a carga", "i", 58)),
                 (C["s02.b"], [("Nox sobe", "g", 54, OXI)] + ps("= se oxidou = redutor", "i", 58)),
                 (C["s02.c"], [("elétrons perdidos = ganhos", "g", 54)]),
                 (C["s02.d"], [("ddp", "g", 54, COR)] + ps("= maior − menor", "i", 58)),
                 (C["s02.e"], [("sacrifício:", "g", 54, COR)] + ps("abaixo do ferro", "i", 58))], XE, 300, 150, 58, 38)


# ---------------- questão 1 ----------------
def b_q1(c, t, C, b):
    numero(c, t, C["s03"], 1, "Nox")
    Q.formula_em(c, t, C["s03.a"], "K2Cr2O7", XE, 400, 150, cores={"Cr": E.COR})
    E.foco(c, t, C["s03.a"] + 0.6, 0.4, lambda a: E.escreve(c, "dicromato de potássio, laranja", XE, 480, 46, "i", TINTA2, a))
    E.foco(c, t, C["s03.b"], 0.4, lambda a: E.pilula(c, "Cr = cromo", XE + 750, 360, 46, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s03.c"], [("a", "g", 54, COR)] + ps("qual é o Nox do cromo?", "i", 58), XE, 640, passo=0.08)
    E.foco(c, t, C["s03.d"], 0.4, lambda a: (Q.formula(c, "Cr^3+", XE + 60, 770, 80, VERDE_CR, a), E.escreve(c, "no bafômetro antigo", XE + 300, 765, 48, "i", TINTA2, a)))
    E.frase(c, t, C["s03.e"], [("b", "g", 54, COR)] + ps("o cromo se oxida ou se reduz?", "i", 58), XE, 900, passo=0.08)
    cor = lambda tt: Q.muda_cor(tt, C["s03.d"], LARANJA, VERDE_CR, 1.5)
    if t < C["s04"]:
        Q.bequer(c, t, C["s03.a"] + 0.3, 1500, 860, 340, 380, 0.65, cor, graduacao=False)
    else:
        E.relogio(c, t, C["s04.a"], cx=1500, cy=520, r=180)


def b_r1(c, t, C, b):
    fx, fy, fs = W / 2, 400, 200
    Q.formula_em(c, t, C["s05"], "K2Cr2O7", fx, fy, fs, align="center", cores={"Cr": E.COR})
    nox_tags(c, t, "K2Cr2O7", fx, fy, fs, {0: ("+1", C["s05.a"], "+2", C["s05.a"] + 0.4, False),
                                          2: ("−2", C["s05.b"], "−14", C["s05.b"] + 0.4, False),
                                          1: ("x", C["s05.c"], "2x", C["s05.c"] + 0.3, True)}, "center")
    if t < C["s06"]:
        conta(c, t, C["s05.c"], "+2 + 2x − 14 = 0", W / 2, 720, 74, TINTA, "center")
        conta(c, t, C["s05.d"], "2x = 12", 700, 860, 70, TINTA2, "center")
        conta(c, t, C["s05.e"], "x =", 1150, 860, 70, TINTA, "right")
        bola_txt(c, t, C["s05.e"] + 0.3, "+6", 1250, 836, 60, 64)
        return
    E.foco(c, t, C["s06.a"], 0.4, lambda a: (Q.formula(c, "Cr: +6 -> +3", 360, 760, 90, TINTA, a)))
    E.foco(c, t, C["s06.b"], 0.4, lambda a: E.pilula(c, "desceu: se reduz", 1350, 735, 56, "g", fundo=RED, a=a))
    E.foco(c, t, C["s06.c"], 0.4, lambda a: E.pilula(c, "o dicromato é o agente oxidante", 1350, 850, 46, "g", fundo=None, cor=RED, a=a, contorno=True))
    E.foco(c, t, C["s06.c"], 0.4, lambda a: centro(c, "o dicromato é o agente oxidante", 1350, 866, 46, "g", RED, a))
    E.foco(c, t, C["s06.d"], 0.4, lambda a: (E.formula(c, "x = 12", 360, 990, 60, "g", ERRADO, a), E.escreve(c, "parou no 12: o índice 2 vale para o cromo", 600, 985, 44, "i", ERRADO, a)))
    if t >= C["s06.e"]:
        E.risco(c, 340, 1005, 560, 950, t, C["s06.e"], largura=8)


# ---------------- questão 2 ----------------
EQ2 = "Cu + Ag^+ -> Cu^2+ + Ag"


def b_q2(c, t, C, b):
    numero(c, t, C["s07"], 2, "balanceamento")
    E.frase(c, t, C["s07.a"], ps("fio de cobre no", "i", 58) + [("nitrato de prata", "g", 54)] + ps("se cobre de prata", "i", 58), XE, 300, passo=0.08)
    Q.formula_em(c, t, C["s07.b"], EQ2, XE, 500, 120)
    E.frase(c, t, C["s07.c"], ps("balanceie pela", "i", 62) + [("oxirredução", "g", 58, COR)], XE, 700, passo=0.1)
    if t >= C["s08"]:
        E.relogio(c, t, C["s08.a"], cx=1560, cy=760, r=150)


def b_r2(c, t, C, b):
    y, s = 400, 130
    G = Q.grupos(EQ2, W / 2, y, s, "center")
    if t < C["s09.c"]:
        Q.formula_em(c, t, C["s09"], EQ2, W / 2, y, s, align="center")
        tag(c, t, C["s09.a"], G[0], "0 → +2: perde 2", 40, OXI)
        tag(c, t, C["s09.b"], G[1], "+1 → 0: ganha 1", 40, RED, dy=-60)
    else:
        Q.formula_em(c, t, C["s09.c"], "Cu + 2 Ag^+ -> Cu^2+ + 2 Ag", W / 2, y, s, align="center", cores={"coef": E.COR})
    E.foco(c, t, C["s09.c"] + 0.2, 0.4, lambda a: E.pilula(c, "cruzou: 1 cobre, 2 íons prata", W / 2, 580, 50, "g", fundo=E.COR, a=a))
    if t >= C["s10"]:
        E.foco(c, t, C["s10.b"], 0.4, lambda a: E.formula(c, "2 × (+1) = +2", 600, 800, 74, "g", TINTA, a, "center"))
        E.foco(c, t, C["s10.c"], 0.4, lambda a: E.formula(c, "1 × (+2) = +2", 1320, 800, 74, "g", TINTA, a, "center"))
        E.foco(c, t, C["s10.d"], 0.4, lambda a: E.selo(c, W / 2, 780, 50, True, a))
        E.foco(c, t, C["s10.a"], 0.4, lambda a: E.escreve(c, "confira pela carga", XE, 700, 52, "i", TINTA2, a))


# ---------------- questão 3 ----------------
S3 = Escada(1500, 300, 760, -0.2, 1.0)


def b_q3(c, t, C, b):
    numero(c, t, C["s11"], 3, "pilha")
    Q.pilha_daniell(c, t, C["s11.a"], 640, 560, ("Cu", "Ag"), ("Cu^2+", "Ag^+"), ddp="?", polos=False, w=900, cores_sol=("#6FA8DC", "#E4E4EA"))
    E.foco(c, t, C["s11.b"], 0.4, lambda a: (Q.formula(c, "Cu^2+/Cu", 1250, 360, 64, TINTA, a), E.escreve(c, "+0,34 V", 1560, 360, 64, "g", TINTA, a)))
    E.foco(c, t, C["s11.c"], 0.4, lambda a: (Q.formula(c, "Ag^+/Ag", 1250, 460, 64, TINTA, a), E.escreve(c, "+0,80 V", 1560, 460, 64, "g", TINTA, a)))
    if t < C["s12"]:
        for k, (tk, s) in enumerate(((C["s11.d"], "qual é a ddp?"), (C["s11.e"], "quem é o polo negativo?"), (C["s11.f"], "qual placa perde massa?"))):
            E.frase(c, t, tk, [("abc"[k], "g", 52, COR)] + ps(s, "i", 56), 1250, 620 + 100 * k, passo=0.08)
    else:
        E.relogio(c, t, C["s12.a"], cx=1560, cy=720, r=150)


def b_r3(c, t, C, b):
    S = Escada(1450, 300, 800, 0.0, 1.0)
    escada(c, t, C["s13"], S, ("Ag", "Cu"), destaque=("Ag", "Cu"))
    E.foco(c, t, C["s13.a"], 0.4, lambda a: E.pilula(c, "prata: se reduz, cátodo, polo +", 560, 330, 46, "g", fundo=RED, a=a))
    E.foco(c, t, C["s13.b"], 0.4, lambda a: E.pilula(c, "cobre: se oxida, ânodo, polo −", 560, 430, 46, "g", fundo=OXI, a=a))
    conta(c, t, C["s13.c"], "0,80 − 0,34", XE, 580, 74, TINTA2)
    conta(c, t, C["s13.d"], "= 0,46 V", XE, 700, 84, COR)
    if t < C["s14.c"]:
        E.foco(c, t, C["s14.a"], 0.4, lambda a: E.pilula(c, "perde massa: a placa de cobre", 600, 860, 46, "g", fundo=ERRADO, a=a))
        E.foco(c, t, C["s14.b"], 0.4, lambda a: E.escreve(c, "elétrons: do cobre para a prata", XE, 980, 50, "i", RED, a))
        return
    conta(c, t, C["s14.e"], "2 × 0,80 − 0,34 = 1,26", XE, 900, 66, ERRADO)
    E.foco(c, t, C["s14.d"], 0.4, lambda a: E.pilula(c, "o 2 do balanceamento não multiplica o potencial", W / 2, 1010, 44, "g", fundo=TINTA, a=a))
    if t >= C["s14.e"] + 1.2:
        E.risco(c, XE - 10, 915, XE + 760, 855, t, C["s14.e"] + 1.2, largura=8)


# ---------------- questão 4 ----------------
def tanque(c, cx, yb, w, h, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, yb - h, w, h, 30, "#7A7F88", a)
    M.rrect(c, cx - w / 2 + 16, yb - h * 0.75, w - 32, h * 0.7, 20, "#6FA8DC", a)
    centro(c, "ferro", cx, yb - h - 20, 44, "g", TINTA, a)
    Q.formula(c, "CuSO4", cx, yb - h * 0.35, 60, BR, a, "center")


def b_q4(c, t, C, b):
    numero(c, t, C["s15"], 4, "corrosão")
    E.frase(c, t, C["s15.a"], ps("guardar", "i", 60) + [("sulfato de cobre", "g", 56)] + ps("num tanque de ferro", "i", 60), XE, 300, passo=0.08)
    E.frase(c, t, C["s15.b"], [("a", "g", 54, COR)] + ps("pode?", "i", 60), XE, 410, passo=0.1)
    E.frase(c, t, C["s15.c"], [("b", "g", 54, COR)] + ps("para proteger um cano de ferro enterrado:", "i", 56), XE, 540, passo=0.08)
    E.foco(c, t, C["s15.d"], 0.4, lambda a: (Q.formula(c, "Zn^2+/Zn", XE + 60, 670, 64, TINTA, a), E.escreve(c, "−0,76", XE + 400, 670, 64, "g", TINTA, a)))
    E.foco(c, t, C["s15.e"], 0.4, lambda a: (E.escreve(c, "ou", XE + 60, 770, 56, "i", TINTA2, a), Q.formula(c, "Sn^2+/Sn", XE + 160, 770, 64, TINTA, a), E.escreve(c, "−0,14", XE + 500, 770, 64, "g", TINTA, a)))
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"] + 0.4, 0.5, lambda a: tanque(c, 1500, 900, 420, 460, a))
    else:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=540, r=180)


def b_r4(c, t, C, b):
    S = Escada(1450, 260, 900, -0.9, 0.5)
    escada(c, t, C["s17"], S, ("Cu", "Sn", "Fe", "Zn"), destaque=("Cu", "Fe") if t < C["s18"] else ("Zn",), riscar=() if t < C["s18"] else ("Sn",))
    if t < C["s18"]:
        E.foco(c, t, C["s17.a"], 0.4, lambda a: E.escreve(c, "íon cobre acima do ferro", XE, 300, 56, "i", TINTA, a))
        E.foco(c, t, C["s17.b"], 0.4, lambda a: E.pilula(c, "íon de cima reage com metal de baixo", 560, 420, 44, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s17.c"], 0.4, lambda a: E.escreve(c, "o ferro do tanque vai sendo corroído", XE, 560, 52, "i", TINTA2, a))
        E.foco(c, t, C["s17.d"], 0.4, lambda a: E.pilula(c, "não pode", 400, 700, 64, "g", fundo=ERRADO, a=a))
        return
    E.foco(c, t, C["s18.a"], 0.4, lambda a: E.escreve(c, "sacrifício: abaixo do ferro", XE, 300, 56, "i", TINTA, a))
    E.foco(c, t, C["s18.b"], 0.4, lambda a: E.pilula(c, "zinco: protege", 420, 440, 60, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s18.c"], 0.4, lambda a: E.pilula(c, "estanho: acima, não", 450, 570, 60, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s18.d"], 0.4, lambda a: E.escreve(c, "faria o ferro virar ânodo", XE, 700, 52, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo o módulo", "i", 84, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s19.a"], ps("o", "i", 62) + [("Nox", "g", 58, COR)] + ps("mostra quem perde e quem ganha", "i", 62)),
                     (C["s19.a"] + 2.0, [("perdidos = ganhos", "g", 58)]),
                     (C["s19.b"], ps("a", "i", 62) + [("escada", "g", 58, COR)] + ps("dá a ddp e quem se sacrifica", "i", 62))], 200, 380, 180, 62, 44)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], ps("a corrente", "i", 90) + [("força", "g", 86, COR)] + ps("a reação", "i", 90), XE, 420, passo=0.12)
    E.frase(c, t, C["s20.b"], [("eletrólise", "g", 100, COR)], XE, 580)
    E.foco(c, t, C["s20.b"] + 0.6, 0.4, lambda a: Q.atomo(c, XE + 650, 545, 60, "Al", a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4, fim=b_fim)
