"""Visual — Estudativo · QUI-ELE-009: eletrólise aquosa.
Linguagem visual: a da Química (QUI-MIS-001), a da trilha Eletroquímica (QUI-ELE-001) e a da Eletrólise (cabeçalho da
QUI-ELE-008: cuba, gerador, polos por cor de sinal, íons CPK com a carga, metal depositado na placa, gás em bolhas na cor do
elemento: H₂ branco, O₂ vermelho, Cl₂ verde). As peças da cuba vêm copiadas da QUI-ELE-008 (candidatas ao kit). A água que
disputa o polo aparece como a molécula H₂O. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-009_eletrolise_aquosa.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("disputa", "nacl", "aplica", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OXI, RED = "#E08A00", Q.ELETRON
FUNDIDO = "#F4B860"

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


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=66, r=40):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + r, y - size * 0.38, r, a=a), centro(c, str(i + 1), x + r, y - size * 0.38 + r * 0.42, r * 1.2, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + r * 2 + 40, y, passo=0.1)


def ion(c, x, y, el, carga, r=30, a=1.0):
    Q.atomo(c, x, y, r, el, a, rotulo=False, cor={"Mg": "#8C93A0"}.get(el))
    centro(c, carga, x, y + r * 0.36, r * 0.95, "g", TINTA if el in ("H",) else BR, a)


def gerador(c, cx, cy, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - 110, cy - 50, 220, 100, 18, "#22232B", a)
    centro(c, "−", cx - 70, cy + 22, 60, "g", BR, a)
    centro(c, "+", cx + 70, cy + 22, 60, "g", E.CLARO, a)
    centro(c, "gerador", cx, cy + 92, 34, "b", TINTA2, a)


class Cuba:
    def __init__(self, cx, yb, w=900, h=420):
        self.cx, self.yb, self.w, self.h = cx, yb, w, h
        self.xc, self.xa = cx - w * 0.3, cx + w * 0.3     # placa do cátodo (esquerda) e do ânodo (direita)
        self.yt = yb - h
        self.yfio = self.yt - 170


def cuba(c, t, t0, K, cor=FUNDIDO, te=None, polos=True, tp=None, placa_c="#9AA0AA", placa_a="#9AA0AA", nivel=0.75, deposito=0.0):
    """cuba eletrolítica com gerador; te = elétrons nos fios; tp = pílulas dos polos"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    x0, x1 = K.cx - K.w / 2, K.cx + K.w / 2
    yl = K.yb - K.h * nivel
    M.rrect(c, x0, yl, K.w, K.yb - yl, 20, cor, 0.85 * q)
    pv = M.paint(Q.VIDRO, q, stroke=6)
    pth = skia.Path(); pth.moveTo(x0, K.yt); pth.lineTo(x0, K.yb); pth.lineTo(x1, K.yb); pth.lineTo(x1, K.yt)
    c.drawPath(pth, pv)
    for x, cp in ((K.xc, placa_c), (K.xa, placa_a)):
        M.rrect(c, x - 24, K.yt - 40, 48, K.h * 0.82, 8, cp, q)
    if deposito > 0:
        M.rrect(c, K.xc - 34, K.yt + 60, 68, K.h * 0.58 * deposito + 4, 10, "#C8CDD6", q)
    # fios e gerador
    p1 = ep(t, t0 + 0.3, 0.5)
    if p1 > 0:
        for pts in (((K.xc, K.yt - 40), (K.xc, K.yfio), (K.cx - 110, K.yfio)), ((K.cx + 110, K.yfio), (K.xa, K.yfio), (K.xa, K.yt - 40))):
            pth = skia.Path(); pth.moveTo(*pts[0]); [pth.lineTo(*p) for p in pts[1:]]
            c.drawPath(pth, M.paint(TINTA, p1, stroke=6))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: gerador(c, K.cx, K.yfio, a))
    if te is not None and t >= te:
        Q.eletrons(c, t, te, [(K.cx - 110, K.yfio), (K.xc, K.yfio), (K.xc, K.yt - 40)], 140, 110, 12)
        Q.eletrons(c, t, te, [(K.xa, K.yt - 40), (K.xa, K.yfio), (K.cx + 110, K.yfio)], 140, 110, 12)
    if polos and tp is not None:
        E.foco(c, t, tp, 0.4, lambda a: E.pilula(c, "cátodo −", K.xc - 190, K.yt + 40, 44, "g", fundo=TINTA, a=a))
        E.foco(c, t, tp + 0.3, 0.4, lambda a: E.pilula(c, "ânodo +", K.xa + 190, K.yt + 40, 44, "g", fundo=E.COR, a=a))


def ions_andam(c, t, t0, K, cation, ca, anion, aa, n=4, nivel=0.75, r=30):
    """cátions andam para o cátodo (esquerda), ânions para o ânodo (direita), em vaivém"""
    if t < t0:
        return
    a = ep(t, t0, 0.4)
    yl = K.yb - K.h * nivel
    for k in range(n):
        f = ((t - t0) * 0.22 + k / n) % 1.0
        y = lerp(yl + 50, K.yb - 50, (k + 0.5) / n)
        xm = K.cx
        ion(c, lerp(xm + 40, K.xc + 60, f), y, cation, ca, r, a * (1 - 0.4 * f))
        ion(c, lerp(xm - 40, K.xa - 60, f), y + 20, anion, aa, r, a * (1 - 0.4 * f))


def bolhas(c, t, t0, x, y0, y1, cor, n=6, r=12):
    if t < t0:
        return
    a = ep(t, t0, 0.4)
    for k in range(n):
        f = ((t - t0) * 0.6 + k / n) % 1.0
        c.drawCircle(x + 26 * math.sin(k * 2.1 + f * 4), lerp(y0, y1, f), r * (0.7 + 0.5 * f), M.paint(cor, a * (1 - f * 0.6)))
        c.drawCircle(x + 26 * math.sin(k * 2.1 + f * 4), lerp(y0, y1, f), r * (0.7 + 0.5 * f), M.paint(TINTA2, a * 0.5 * (1 - f), stroke=2))



LIMPA, AZUL_CU = Q.AGUA, "#6FA8DC"
assert Q.lados("2 H2O + 2 e^- -> H2 + 2 OH^-")[0] == Q.lados("2 H2O + 2 e^- -> H2 + 2 OH^-")[1]
assert Q.lados("2 H2O -> O2 + 4 H^+ + 4 e^-")[0] == Q.lados("2 H2O -> O2 + 4 H^+ + 4 e^-")[1]


def topo(c, t, t0, partes, y=105):
    E.frase(c, t, t0, partes, W / 2, y, "center", 0.1)


def deposito_cor(c, K, f, cor, a=1.0):
    if f > 0:
        M.rrect(c, K.xc - 34, K.yt + 40, 68, K.h * 0.62 * f + 4, 10, cor, a)


def linha_ions(c, t, t0, itens, x, y, dx=150, r=40):
    for k, (el, ch) in enumerate(itens):
        E.foco(c, t, t0 + 0.15 * k, 0.4, lambda a, k=k, el=el, ch=ch: (ion(c, x + dx * k, y, el, ch, r, a), centro(c, el, x + dx * k, y + r + 50, 40, "g", TINTA, a)))


# ---------------- gancho ----------------
KA = Cuba(500, 860, 640, 300)
KB = Cuba(1420, 860, 640, 300)


def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def s01():
            cuba(c, t, C["s01.a"], KA, te=C["s01.a"] + 0.5, polos=False, deposito=ep(t, C["s01.a"] + 0.6, 2.0))
            E.foco(c, t, C["s01.a"] + 0.4, 0.4, lambda a: E.pilula(c, "sal derretido: sai sódio", KA.cx, KA.yb + 70, 44, "g", fundo=TINTA, a=a))
            cuba(c, t, C["s01.b"], KB, cor=LIMPA, te=C["s01.b"] + 0.5, polos=False)
            E.foco(c, t, C["s01.b"] + 0.4, 0.4, lambda a: E.pilula(c, "sal na água", KB.cx, KB.yb + 70, 44, "g", fundo=Q.VIDRO, a=a))
            E.foco(c, t, C["s01.c"], 0.4, lambda a: E.pilula(c, "sódio nenhum", KB.cx, KB.yb + 150, 46, "g", fundo=ERRADO, a=a))
            bolhas(c, t, C["s01.d"], KB.xc, KB.yb - 40, KB.yt + 20, "#F7F7F5")
            E.foco(c, t, C["s01.d"] + 0.3, 0.4, lambda a: Q.formula(c, "H2", KB.xc + 90, KB.yt + 120, 70, TINTA, a))
            E.frase(c, t, C["s01.e"], [("por quê?", "g", 70, COR)], W / 2, 140, "center")
        E.saida(c, t, C["s02"] - 0.1, s01)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1580, 560, 230 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 230, passo=0.14)
    lista(c, t, [(C["s02.b"], ps("o que sai em", "i", 66) + [("cada polo", "g", 62)] + ps("na água", "i", 66)),
                 (C["s02.c"], ps("como se", "i", 66) + [("cobre uma peça", "g", 62)]),
                 (C["s02.d"], ps("como se", "i", 66) + [("purifica o cobre", "g", 62)]),
                 (C["s02.e"], [("atalho", "g", 62, COR), ("de", "i", 66), ("prova", "i", 66)])], XE, 390, 150, 62)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de uma coisa", "i", 76, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("cátion", "g", 66)] + ps("vai ao", "i", 70) + [("cátodo −", "g", 66)] + ps("e ganha elétrons", "i", 70), XE, 420, passo=0.1)
    E.frase(c, t, C["s03.b"], [("ânion", "g", 66)] + ps("vai ao", "i", 70) + [("ânodo +", "g", 66, COR)] + ps("e perde", "i", 70), XE, 560, passo=0.1)


# ---------------- a disputa ----------------
K1 = Cuba(W / 2, 900, 980, 400)


def b_disputa(c, t, C, b):
    cuba(c, t, C["s04"], K1, cor=LIMPA, te=C["s04"] + 0.6, tp=C["s04"] + 0.8)
    topo(c, t, C["s04"], ps("na água, os polos têm uma concorrente:", "i", 56) + [("a própria água", "g", 52, COR)])
    E.foco(c, t, C["s04.a"], 0.4, lambda a: Q.molecula_desenho(c, "H2O", W / 2, 760, 70, a))
    E.foco(c, t, C["s04.b"], 0.4, lambda a: Q.formula(c, "2 H2O + 2 e^- -> H2 + 2 OH^-", 120, 1050, 44, TINTA, a))
    bolhas(c, t, C["s04.c"], K1.xc, K1.yb - 40, K1.yt + 20, "#F7F7F5")
    E.foco(c, t, C["s04.c"], 0.4, lambda a: E.pilula(c, "gás hidrogênio", K1.xc, K1.yb + 60, 42, "g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s04.d"], 0.4, lambda a: Q.formula(c, "2 H2O -> O2 + 4 H^+ + 4 e^-", 1150, 1050, 44, TINTA, a))
    bolhas(c, t, C["s04.e"], K1.xa, K1.yb - 40, K1.yt + 20, "#E5322D")
    E.foco(c, t, C["s04.e"], 0.4, lambda a: E.pilula(c, "gás oxigênio", K1.xa, K1.yb + 60, 42, "g", fundo="#E5322D", a=a))
    E.foco(c, t, C["s04.f"], 0.4, lambda a: E.pilula(c, "em cada polo, só um ganha", W / 2, 640, 50, "g", fundo=E.COR, a=a))


# ---------------- cátodo ----------------
def b_catodo(c, t, C, b):
    E.frase(c, t, C["s05.a"], [("no cátodo", "g", 72, TINTA)], XE, 190)
    E.frase(c, t, C["s05.b"], ps("família 1, família 2 e alumínio", "i", 60) + [("perdem para a água", "g", 56, ERRADO)], XE, 320, passo=0.08)
    linha_ions(c, t, C["s05.c"], (("Na", "+"), ("K", "+"), ("Ca", "2+"), ("Mg", "2+"), ("Al", "3+")), 260, 460)
    E.foco(c, t, C["s05.d"], 0.4, lambda a: (E.escreve(c, "→", 1050, 480, 80, "g", TINTA2, a), Q.formula(c, "sai H2", 1150, 480, 80, TINTA, a)))
    E.frase(c, t, C["s05.e"], ps("os outros", "i", 60) + [("ganham", "g", 56, CERTO)], XE, 680, passo=0.1)
    linha_ions(c, t, C["s05.e"] + 0.5, (("Cu", "2+"), ("Ag", "+"), ("Ni", "2+"), ("Zn", "2+")), 260, 820)
    E.foco(c, t, C["s05.f"], 0.4, lambda a: (E.escreve(c, "→", 900, 840, 80, "g", TINTA2, a), E.escreve(c, "o metal se deposita", 1000, 840, 60, "g", TINTA, a)))


# ---------------- ânodo ----------------
def b_anodo(c, t, C, b):
    E.frase(c, t, C["s06.a"], [("no ânodo", "g", 72, COR)], XE, 190)
    E.frase(c, t, C["s06.b"], ps("ânions sem oxigênio", "i", 60) + [("ganham da água", "g", 56, CERTO)], XE, 320, passo=0.08)
    E.foco(c, t, C["s06.b"] + 1.6, 0.4, lambda a: E.pilula(c, "menos o fluoreto", 1500, 300, 44, "g", fundo=TINTA2, a=a))
    linha_ions(c, t, C["s06.c"], (("Cl", "−"), ("Br", "−"), ("I", "−")), 260, 460)
    E.foco(c, t, C["s06.d"], 0.4, lambda a: (E.escreve(c, "→", 760, 480, 80, "g", TINTA2, a), Q.formula(c, "Cl2  Br2  I2", 860, 480, 76, TINTA, a)))
    E.frase(c, t, C["s06.e"], ps("ânions com oxigênio", "i", 60) + [("perdem para a água", "g", 56, ERRADO)], XE, 680, passo=0.08)
    E.foco(c, t, C["s06.e"] + 0.8, 0.4, lambda a: Q.formula(c, "SO4^2-   NO3^-", 260, 840, 90, TINTA, a))
    E.foco(c, t, C["s06.f"], 0.4, lambda a: (E.escreve(c, "→", 900, 840, 80, "g", TINTA2, a), Q.formula(c, "sai O2", 1000, 840, 80, "#E5322D", a)))


# ---------------- NaCl em água ----------------
def b_nacl(c, t, C, b):
    cuba(c, t, C["s07"], K1, cor=LIMPA, te=C["s07"] + 0.4, tp=C["s07"] + 0.6)
    ions_andam(c, t, C["s07"] + 0.6, K1, "Na", "+", "Cl", "−")
    bolhas(c, t, C["s07.b"], K1.xc, K1.yb - 40, K1.yt + 20, "#F7F7F5")
    bolhas(c, t, C["s07.d"], K1.xa, K1.yb - 40, K1.yt + 20, "#2DB24A")
    if t < C["s08"]:
        topo(c, t, C["s07"], ps("o sal de cozinha na água", "i", 60, TINTA2))
        E.foco(c, t, C["s07.a"], 0.4, lambda a: E.pilula(c, "sódio: perde", K1.xc, K1.yb + 70, 44, "g", fundo=ERRADO, a=a))
        E.foco(c, t, C["s07.b"], 0.4, lambda a: Q.formula(c, "H2", K1.xc + 100, K1.yt + 130, 70, TINTA, a))
        E.foco(c, t, C["s07.c"], 0.4, lambda a: E.pilula(c, "cloreto: ganha", K1.xa, K1.yb + 70, 44, "g", fundo=CERTO, a=a))
        E.foco(c, t, C["s07.d"], 0.4, lambda a: Q.formula(c, "Cl2", K1.xa - 200, K1.yt + 130, 70, "#2DB24A", a))
        return
    topo(c, t, C["s08.a"], ps("na solução, sobram", "i", 60) + [("sódio e hidróxido", "g", 56)])
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "soda cáustica: NaOH", W / 2, K1.yb + 70, 48, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "cloro, hidrogênio e soda de uma vez", W / 2, 230, 44, "g", fundo=TINTA, a=a))


# ---------------- CuSO4 em água ----------------
def b_cuso4(c, t, C, b):
    cor = lambda tt: Q.muda_cor(tt, C["s09.e"], AZUL_CU, "#CFE2EF", 3.0)
    cuba(c, t, C["s09"], K1, cor=cor(t), te=C["s09"] + 0.4, tp=C["s09"] + 0.6, placa_c="#3A3B42", placa_a="#3A3B42")
    deposito_cor(c, K1, ease_io(prog(t, C["s09.b"], 3.0)), "#C87533")
    bolhas(c, t, C["s09.d"], K1.xa, K1.yb - 40, K1.yt + 20, "#E5322D")
    topo(c, t, C["s09"], ps("sulfato de cobre, com placas de", "i", 58, TINTA2) + [("grafite", "g", 54)])
    E.foco(c, t, C["s09.a"], 0.4, lambda a: E.pilula(c, "cobre: ganha", K1.xc, K1.yb + 70, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s09.b"], 0.4, lambda a: E.pilula(c, "a placa se cobre de cobre", K1.xc + 40, K1.yt - 70, 42, "g", fundo="#B5532A", a=a))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "sulfato: perde para a água", K1.xa, K1.yb + 70, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s09.d"], 0.4, lambda a: Q.formula(c, "O2", K1.xa - 180, K1.yt + 130, 70, "#E5322D", a))
    E.foco(c, t, C["s09.e"], 0.4, lambda a: E.pilula(c, "o azul vai sumindo", W / 2, 230, 46, "g", fundo=AZUL_CU, a=a))


# ---------------- galvanoplastia e refino ----------------
def colher(c, x, y, s, cor, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x - s * 0.08, y - s, s * 0.16, s * 0.9, s * 0.08, cor, a)
    c.drawOval(skia.Rect.MakeXYWH(x - s * 0.26, y - s * 0.12, s * 0.52, s * 0.6), M.paint(cor, a))


def b_aplica(c, t, C, b):
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10.a"], [("galvanoplastia:", "g", 64, COR)] + ps("cobrir uma peça com metal", "i", 64), XE, 190, passo=0.1)
            K = Cuba(1380, 960, 760, 360)
            cuba(c, t, C["s10.b"], K, cor=AZUL_CU, te=C["s10.b"] + 0.4, tp=C["s10.b"] + 0.6, placa_c="#C9CDD4")
            cob = ease_io(prog(t, C["s10.c"], 2.0))
            colher(c, K.xc, K.yb - 80, 260, M.mix("#C9CDD4", "#C87533", cob), ep(t, C["s10.b"], 0.4))
            E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "a peça no cátodo", XE, 420, 56, "i", TINTA, a))
            E.foco(c, t, C["s10.c"], 0.4, lambda a: E.escreve(c, "camada fina e lisa", XE, 520, 56, "g", "#B5532A", a))
            E.frase(c, t, C["s10.d"], [("níquel,", "g", 54), ("cromo,", "g", 54), ("prata:", "g", 54)], XE, 680, passo=0.15)
            E.foco(c, t, C["s10.d"] + 1.0, 0.4, lambda a: E.escreve(c, "talher prateado, torneira cromada", XE, 770, 48, "i", TINTA2, a))
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    K = Cuba(1250, 960, 800, 360)
    gasto = ease_io(prog(t, C["s11.e"], 3.0))
    cuba(c, t, C["s11"], K, cor=AZUL_CU, te=C["s11"] + 0.4, tp=C["s11"] + 0.6, placa_a="#8A4A2A")
    deposito_cor(c, K, ease_io(prog(t, C["s11.e"], 3.0)), "#E07B39")
    if t >= C["s11.f"]:
        for k in range(7):
            E.bola(c, K.xa - 60 + 20 * k, K.yb - 20, 10, ("#E6B422", "#C0C0C8")[k % 2], ep(t, C["s11.f"] + 0.1 * k, 0.3))
        E.foco(c, t, C["s11.f"] + 0.5, 0.4, lambda a: E.pilula(c, "ouro e prata no fundo", K.xa, K.yb + 70, 42, "g", fundo="#B8860B", a=a))
    E.frase(c, t, C["s11"], ps("e se o ânodo também for de cobre?", "i", 58, TINTA2), XE, 190, passo=0.08)
    E.foco(c, t, C["s11.b"], 0.4, lambda a: E.escreve(c, "ele mesmo se dissolve", XE, 300, 54, "g", OXI, a))
    E.frase(c, t, C["s11.c"], [("refino", "g", 64, COR)] + ps("do cobre:", "i", 64), XE, 450, passo=0.1)
    E.foco(c, t, C["s11.d"], 0.4, lambda a: (E.escreve(c, "ânodo: cobre impuro", XE, 560, 50, "i", TINTA, a), E.escreve(c, "cátodo: cobre puro", XE, 640, 50, "i", TINTA, a)))
    E.foco(c, t, C["s11.e"], 0.4, lambda a: E.pilula(c, "o cobre passa de uma placa à outra", 520, 780, 42, "g", fundo="#B5532A", a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("sal na água dá sódio?", "i", 64), XE + 450, 190, passo=0.1)
    E.foco(c, t, C["s12.a"] + 0.6, 0.4, lambda a: (Q.formula(c, "NaCl(aq)", XE, 400, 100, TINTA, a), E.escreve(c, "→", XE + 520, 400, 90, "g", TINTA2, a), Q.formula(c, "Na", XE + 650, 400, 100, ERRADO, a)))
    if t >= C["s12.a"] + 1.4:
        E.risco(c, XE + 630, 420, XE + 820, 320, t, C["s12.a"] + 1.4, largura=10)
    E.frase(c, t, C["s12.b"], ps("na água, o sódio", "i", 62) + [("perde a disputa", "g", 58, COR)], XE, 600, passo=0.1)
    E.frase(c, t, C["s12.c"], ps("e o sódio metálico", "i", 62) + [("reagiria com a água", "g", 58, OXI)] + ps("na hora", "i", 62), XE, 740, passo=0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 160, "center", 0.12)
        E.frase(c, t, C["s13.a"], ps("cátodo:", "i", 62, CLARO) + [("família 1, 2 ou Al?", "g", 58, BR)], XE, 330, passo=0.1)
        E.foco(c, t, C["s13.b"], 0.4, lambda a: Q.formula(c, "sai H2", 1250, 330, 80, E.CLARO, a, escuro=True))
        E.frase(c, t, C["s13.c"], ps("ânodo:", "i", 62, CLARO) + [("ânion com oxigênio?", "g", 58, BR)], XE, 500, passo=0.1)
        E.foco(c, t, C["s13.d"], 0.4, lambda a: Q.formula(c, "sai O2", 1250, 500, 80, E.CLARO, a, escuro=True))
        E.frase(c, t, C["s13.e"], ps("senão, sai o", "i", 62, CLARO) + [("próprio íon", "g", 58, BR)], XE, 700, passo=0.1)
        E.foco(c, t, C["s13.e"] + 1.2, 0.4, lambda a: E.escreve(c, "o metal, ou cloro, bromo e iodo", XE, 800, 50, "i", CLARO, a))
        return
    E.frase(c, t, C["s14.a"], ps("esses metais perdem elétrons tão fácil que", "i", 56, CLARO) + [("não aceitam de volta", "g", 52, BR)], W / 2, 300, "center", 0.08)
    E.frase(c, t, C["s14.b"], ps("os ânions com oxigênio", "i", 58, CLARO) + [("seguram os seus", "g", 54, BR)], W / 2, 400, "center", 0.1)
    E.frase(c, t, C["s14.c"], [("não", "g", 58, ERRADO), ("compensa", "i", 60, CLARO)] + ps("com ânodo que se dissolve:", "i", 60, CLARO), W / 2, 620, "center", 0.1)
    pilula_em(c, t, C["s14.d"], "aí, quem se oxida é a própria placa", W / 2, 750, 48, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s15.a"], [("1", "g", 56, COR)] + ps("o que sai em cada polo?", "i", 60), XE, 330, passo=0.08)
    E.foco(c, t, C["s15.a"] + 0.6, 0.4, lambda a: (Q.formula(c, "AgNO3", XE + 80, 470, 110, TINTA, a), E.escreve(c, "nitrato de prata em água", XE + 520, 465, 50, "i", TINTA2, a)))
    E.frase(c, t, C["s15.b"], [("2", "g", 56, COR)] + ps("e na do iodeto de potássio?", "i", 60), XE, 650, passo=0.08)
    E.foco(c, t, C["s15.b"] + 0.6, 0.4, lambda a: (Q.formula(c, "KI", XE + 80, 790, 110, TINTA, a), E.escreve(c, "em água", XE + 300, 785, 50, "i", TINTA2, a)))
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1560, cy=560, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    K = Cuba(1300, 940, 820, 340)
    if t < C["s18"]:
        cuba(c, t, C["s17"], K, cor=LIMPA, te=C["s17"] + 0.4, tp=C["s17"] + 0.6, deposito=0)
        deposito_cor(c, K, ease_io(prog(t, C["s17.b"], 2.0)), "#C0C0C8")
        bolhas(c, t, C["s17.c"], K.xa, K.yb - 40, K.yt + 20, "#E5322D")
        E.foco(c, t, C["s17.a"], 0.4, lambda a: Q.formula(c, "AgNO3", XE, 260, 100, TINTA, a))
        E.foco(c, t, C["s17.b"], 0.4, lambda a: (E.escreve(c, "cátodo:", XE, 420, 56, "i", TINTA, a), E.escreve(c, "prata", XE + 220, 420, 60, "g", "#8A8D96", a)))
        E.foco(c, t, C["s17.c"], 0.4, lambda a: (E.escreve(c, "ânodo:", XE, 540, 56, "i", TINTA, a), Q.formula(c, "O2", XE + 220, 540, 66, "#E5322D", a)))
        E.foco(c, t, C["s17.c"] + 0.5, 0.4, lambda a: E.escreve(c, "nitrato tem oxigênio", XE, 640, 46, "i", TINTA2, a))
        return
    cuba(c, t, C["s18"], K, cor="#F3E7A0", te=C["s18"] + 0.4, tp=C["s18"] + 0.6)
    bolhas(c, t, C["s18.b"], K.xc, K.yb - 40, K.yt + 20, "#F7F7F5")
    E.foco(c, t, C["s18.c"], 0.6, lambda a: M.rrect(c, K.xa - 30, K.yt + 40, 60, K.h * 0.6, 8, "#6B2FA0", 0.7 * a))
    E.foco(c, t, C["s18.a"], 0.4, lambda a: Q.formula(c, "KI", XE, 260, 100, TINTA, a))
    E.foco(c, t, C["s18.b"], 0.4, lambda a: (E.escreve(c, "cátodo:", XE, 420, 56, "i", TINTA, a), Q.formula(c, "H2", XE + 220, 420, 66, TINTA, a)))
    E.foco(c, t, C["s18.b"] + 0.5, 0.4, lambda a: E.escreve(c, "potássio é da família 1", XE, 500, 46, "i", TINTA2, a))
    E.foco(c, t, C["s18.c"], 0.4, lambda a: (E.escreve(c, "ânodo:", XE, 620, 56, "i", TINTA, a), Q.formula(c, "I2", XE + 220, 620, 66, "#6B2FA0", a)))
    E.foco(c, t, C["s18.c"] + 0.5, 0.4, lambda a: E.escreve(c, "iodeto não tem oxigênio", XE, 700, 46, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s19.a"], ps("família 1, 2 e Al:", "i", 64) + [("hidrogênio no cátodo", "g", 60)]),
                     (C["s19.b"], ps("ânion com oxigênio:", "i", 64) + [("oxigênio no ânodo", "g", 60, COR)]),
                     (C["s19.c"], ps("a peça a cobrir vai no", "i", 64) + [("cátodo", "g", 60)])], 220, 390, 190, 64, 46)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], ps("quanto metal", "i", 90) + [("se deposita", "g", 86, COR)], XE, 420, passo=0.12)
    E.foco(c, t, C["s20.b"], 0.4, lambda a: E.formula(c, "10 A · 1.930 s → 6,35 g", XE, 600, 80, "g", TINTA, a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, disputa=b_disputa, catodo=b_catodo, anodo=b_anodo, nacl=b_nacl, cuso4=b_cuso4,
              aplica=b_aplica, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
