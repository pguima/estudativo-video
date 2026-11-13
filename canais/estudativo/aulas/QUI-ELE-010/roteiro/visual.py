"""Visual — Estudativo · QUI-ELE-010: leis de Faraday.
Linguagem visual: a da Química (QUI-MIS-001), a da trilha Eletroquímica (QUI-ELE-001) e a da Eletrólise (QUI-ELE-008). A conta
anda numa TRILHA DE QUATRO PASSOS no alto (carga → mol de e⁻ → mol de metal → massa; peça local trilha(), candidata ao kit),
com o passo da vez em turquesa. Fórmula nova com F.formula_legenda, como na Física; regra de três com Q.regra_tres. Elétron e
mol de elétrons em azul. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-010_leis_de_faraday.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("carga", "faraday", "massa", "erro", "atalho", "questao", "fim"))
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



import fisica as F

AZUL_CU = "#6FA8DC"
assert 10 * 1930 == 19300 and 19300 * 5 == 96500 and 19300 / 96500 == 0.2
assert round(0.2 / 2 * 63.5, 2) == 6.35 and round(19300 * 63.5 / (2 * 96500), 2) == 6.35 and round(0.2 * 63.5, 2) == 12.7
assert 10 * 965 == 9650 and 9650 * 10 == 96500 and round(0.1 / 2 * 65, 2) == 3.25 and round(0.1 * 65, 1) == 6.5
assert round(6.02e23 * 1.602e-19) == 96440 or True   # ≈ 96.485 C com os valores exatos; a prova usa 96.500


def conta(c, t, t0, s, x, y, size, cor=TINTA, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


PASSOS = ("carga", "mol de e⁻", "mol de metal", "massa")


def trilha(c, t, atual, tl, y=120):
    """os quatro passos em fila no alto; o da vez em turquesa, os feitos em cinza"""
    for k, nome in enumerate(PASSOS):
        x = 330 + k * 420
        q = ep(t, tl[k], 0.4) if tl[k] is not None else 0
        if q <= 0:
            continue
        cor = E.COR if k == atual else ("#B9BCC2" if k < atual else "#DADCE0")
        E.bola(c, x, y, 38, cor, q)
        centro(c, str(k + 1), x, y + 16, 46, "g", BR, q)
        E.escreve(c, nome, x + 56, y + 16, 42, "g" if k == atual else "b", TINTA if k == atual else TINTA2, q)
        if k < 3:
            M.arrow(c, x + 56 + E.larg(nome, "b", 42) + 14, y, x + 380, y, "#C8CAD2", q, 4, 14, 1)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def s01():
            K = Cuba(1300, 900, 760, 330)
            cuba(c, t, C["s01.a"], K, cor=AZUL_CU, te=C["s01.a"] + 0.5, polos=False)
            dep = ease_io(prog(t, C["s01.a"] + 0.6, 4.0))
            if dep > 0:
                M.rrect(c, K.xc - 34, K.yt + 40, 68, K.h * 0.62 * dep + 4, 10, "#C87533", 1)
            E.foco(c, t, C["s01.a"], 0.4, lambda a: (E.pilula(c, "10 A", 300, 300, 70, "g", fundo=RED, a=a)))
            E.foco(c, t, C["s01.a"] + 0.8, 0.4, lambda a: (E.pilula(c, "1.930 s", 300, 440, 70, "g", fundo=TINTA, a=a)))
            E.frase(c, t, C["s01.b"], ps("sem pesar nada:", "i", 64, TINTA2), XE, 640, passo=0.1)
            bola_txt(c, t, C["s01.c"], "6,35 g", 380, 800, 130, 74, "#B5532A")
            E.frase(c, t, C["s01.d"], [("como?", "g", 70, COR)], 640, 820)
        E.saida(c, t, C["s02"] - 0.1, s01)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1660, 280, 160 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    E.frase(c, t, C["s02.b"], ps("a", "i", 70) + [("massa de metal", "g", 66, COR)] + ps("que a corrente deposita", "i", 70), XE, 420, passo=0.1)
    trilha(c, t, -1, [C["s02.b"] + 0.8 + 0.3 * k for k in range(4)], 600)
    E.frase(c, t, C["s02.c"], [("atalho", "g", 64, COR), ("de", "i", 70), ("prova", "i", 70)], XE, 820, passo=0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 76, TINTA2) + [("três", "g", 70, COR), ("coisas", "i", 76, TINTA2)], XE, 200, passo=0.12)
    lista(c, t, [(C["s03.a"], [("corrente", "g", 62, RED)] + ps("= carga dividida pelo tempo", "i", 64)),
                 (C["s03.b"], ps("1 mol de cobre =", "i", 64) + [("63,5 g", "g", 62, COR)]),
                 (C["s03.c"], ps("a", "i", 64) + [("regra de três", "g", 62)])], XE, 400, 190, 64, 42)


# ---------------- passo 1: carga ----------------
def b_carga(c, t, C, b):
    trilha(c, t, 0, [C["s04.a"], C["s04.a"] + 0.15, C["s04.a"] + 0.3, C["s04.a"] + 0.45])
    E.frase(c, t, C["s04.b"], ps("carga = corrente vezes tempo", "i", 64, TINTA2), XE, 290, passo=0.1)
    F.formula_legenda(c, t, C["s04.c"], "Q = i · t", [("Q", "carga", "C"), ("i", "corrente", "A"), ("t", "tempo", "s")], W / 2, 520, 150,
                      tl=[C["s04.d"], C["s04.e"], C["s04.f"]])
    if t >= C["s05"]:
        conta(c, t, C["s05.a"], "Q = 10 · 1.930", W / 2 - 40, 900, 84, TINTA2, "right")
        E.foco(c, t, C["s05.b"], 0.4, lambda a: E.formula(c, "= 19.300 C", W / 2, 900, 84, "g", COR, a))


# ---------------- passo 2: Faraday ----------------
def b_faraday(c, t, C, b):
    trilha(c, t, 1, [-10] * 4)
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], ps("quantos mols de elétrons?", "i", 64, TINTA2), XE, 280, passo=0.1)
        E.foco(c, t, C["s06.b"], 0.4, lambda a: (E.escreve(c, "1 mol de elétrons =", XE, 440, 66, "i", TINTA, a), E.formula(c, "6 · 10^{23}", XE + 640, 440, 80, "g", RED, a), E.escreve(c, "elétrons", XE + 960, 440, 66, "i", TINTA, a)))
        for k in range(14):
            E.foco(c, t, C["s06.b"] + 0.3 + 0.04 * k, 0.3, lambda a, k=k: (E.bola(c, 260 + 100 * k, 560, 18, Q.ELETRON, a)))
        E.foco(c, t, C["s06.c"], 0.4, lambda a: E.formula(c, "× 1,6 · 10^{−19} C cada", XE, 700, 66, "g", TINTA2, a))
        E.foco(c, t, C["s06.d"], 0.4, lambda a: E.formula(c, "≈ 96.500 C", XE, 840, 110, "g", COR, a))
        E.foco(c, t, C["s06.e"], 0.4, lambda a: E.pilula(c, "a constante de Faraday", 1350, 805, 56, "g", fundo=E.COR, a=a))
        return
    conta(c, t, C["s07.a"], "19.300 ÷ 96.500", W / 2, 380, 90, TINTA, "center")
    conta(c, t, C["s07.b"], "19.300 × 5 = 96.500", W / 2, 560, 80, TINTA2, "center")
    E.foco(c, t, C["s07.c"], 0.4, lambda a: E.formula(c, "um quinto de mol", W / 2, 720, 74, "g", TINTA, a, "center"))
    pilula_em(c, t, C["s07.d"], "0,2 mol de e⁻", W / 2, 880, 70, RED)


# ---------------- passo 3: semirreação ----------------
def b_semi(c, t, C, b):
    trilha(c, t, 2, [-10] * 4)
    E.frase(c, t, C["s08.a"], ps("a semirreação do cátodo", "i", 64, TINTA2), XE, 280, passo=0.1)
    Q.formula_em(c, t, C["s08.b"], "Cu^2+ + 2 e^- -> Cu", W / 2, 470, 140, align="center", cores={"coef": RED})
    E.foco(c, t, C["s08.c"], 0.5, lambda a: (Q.atomo(c, 700, 640, 50, "Cu", a), E.bola(c, 800, 640, 18, Q.ELETRON, a), E.bola(c, 850, 640, 18, Q.ELETRON, a)))
    E.foco(c, t, C["s08.d"], 0.4, lambda a: E.formula(c, "2 mol de e⁻ → 1 mol de Cu", W / 2 + 60, 660, 66, "g", TINTA, a))
    conta(c, t, C["s08.e"], "0,2 mol de e⁻ ÷ 2", W / 2, 840, 80, TINTA2, "center")
    pilula_em(c, t, C["s08.f"], "0,1 mol de Cu", W / 2, 980, 60, "#B5532A")


# ---------------- passo 4: massa ----------------
def b_massa(c, t, C, b):
    trilha(c, t, 3, [-10] * 4)
    if t < C["s10"]:
        E.foco(c, t, C["s09.b"], 0.4, lambda a: E.formula(c, "1 mol de Cu = 63,5 g", W / 2, 420, 80, "g", TINTA2, a, "center"))
        conta(c, t, C["s09.c"], "0,1 · 63,5", W / 2 - 40, 620, 100, TINTA, "right")
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.formula(c, "= 6,35 g", W / 2, 620, 100, "g", COR, a))
        E.foco(c, t, C["s09.e"], 0.4, lambda a: E.pilula(c, "o número do começo", W / 2, 800, 54, "g", fundo="#B5532A", a=a))
        return
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("tudo numa", "i", 64, TINTA2) + [("regra de três", "g", 60)], XE, 280, passo=0.1)
        Q.regra_tres(c, t, C["s10.b"], ("carga", "massa de Cu"), [("193000 C", "63,5 g"), ("19300 C", "x")], 420, 470, 80,
                     tl=[C["s10.b"], C["s10.c"]], tcruz=C["s10.c"] + 0.8, tx=C["s10.d"] - 0.6, conta="x = 19300 · 63,5 / 193000", res="6,35 g")
        E.foco(c, t, C["s10.b"] + 0.4, 0.4, lambda a: E.escreve(c, "2 mols de elétrons", 1300, 560, 46, "i", TINTA2, a))
        return
    E.frase(c, t, C["s11.a"], ps("a ideia de", "i", 70) + [("Faraday", "g", 66, COR)], XE, 300, passo=0.12)
    E.frase(c, t, C["s11.b"], ps("massa depositada", "i", 64) + [("proporcional à carga", "g", 60)], XE, 440, passo=0.1)
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.formula(c, "2 × corrente  ou  2 × tempo", XE, 640, 70, "g", TINTA, a))
    E.foco(c, t, C["s11.d"], 0.4, lambda a: E.formula(c, "→ 2 × cobre", XE, 780, 90, "g", "#B5532A", a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("esquecer a carga do íon", "i", 64), XE + 450, 190, passo=0.1)

    def errado():
        conta(c, t, C["s12.b"], "0,2 mol de e⁻ → 0,2 mol de Cu", W / 2, 400, 70, ERRADO, "center")
        conta(c, t, C["s12.c"], "= 12,7 g", W / 2, 520, 90, ERRADO, "center")
        E.foco(c, t, C["s12.c"] + 0.6, 0.4, lambda a: E.pilula(c, "o dobro", W / 2 + 330, 490, 46, "g", fundo=ERRADO, a=a))
        if t >= C["s12.c"] + 1.2:
            E.risco(c, W / 2 - 460, 540, W / 2 + 460, 350, t, C["s12.c"] + 1.2, largura=10)
    E.saida(c, t, C["s13.b"] - 0.1, errado)
    Q.formula_em(c, t, C["s13.a"], "Cu^2+ + 2 e^-", W / 2, 470, 120, align="center", cores={"carga": RED, "coef": RED})
    E.frase(c, t, C["s13.b"], ps("divida os mols de elétrons pela", "i", 60) + [("carga do íon", "g", 56, COR)], W / 2, 680, "center", 0.1)
    for k, (s, n) in enumerate((("Cu^2+", "÷ 2"), ("Ag^+", "÷ 1"), ("Al^3+", "÷ 3"))):
        E.foco(c, t, C["s13.c"] + 0.5 * k, 0.4, lambda a, s=s, n=n, k=k: (Q.formula(c, s, 460 + 500 * k, 880, 90, TINTA, a, "center"), E.formula(c, n, 460 + 500 * k, 980, 64, "g", COR, a, "center")))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        E.frase(c, t, C["s14.a"], ps("a carga quase sempre é uma", "i", 60, CLARO) + [("fração redonda de 96.500", "g", 56, BR)], W / 2, 300, "center", 0.08)
        for k, (tk, v, fr_) in enumerate(((C["s14.b"], "9.650", "1/10"), (C["s14.c"], "19.300", "1/5"), (C["s14.d"], "48.250", "1/2"))):
            y = 470 + 150 * k
            E.foco(c, t, tk, 0.4, lambda a, v=v, y=y: E.formula(c, v + " C", 860, y, 90, "g", BR, a, "right"))
            E.foco(c, t, tk + 0.4, 0.4, lambda a, fr_=fr_, y=y: (E.formula(c, "=", 950, y, 90, "g", CLARO, a), E.formula(c, fr_, 1050, y, 90, "g", E.CLARO, a), E.escreve(c, "mol de elétrons", 1300, y, 56, "i", CLARO, a)))
        pilula_em(c, t, C["s14.e"], "achou a fração, achou os mols", W / 2, 960, 50, E.COR)
        return
    E.frase(c, t, C["s15.a"], ps("funciona porque quem faz a prova", "i", 60, CLARO) + [("escolhe o tempo", "g", 56, BR)], W / 2, 300, "center", 0.08)
    E.frase(c, t, C["s15.b"], [("atenção:", "g", 60, OXI)] + ps("tempo em minutos?", "i", 62, CLARO), W / 2, 480, "center", 0.1)
    E.foco(c, t, C["s15.c"], 0.4, lambda a: E.formula(c, "minutos × 60 = segundos", W / 2, 620, 80, "g", BR, a, "center"))
    E.foco(c, t, C["s15.c"] + 2.2, 0.4, lambda a: E.pilula(c, "não é fração redonda? divida", W / 2, 800, 50, "g", fundo="#3A3B46", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s16.a"], ps("cobrir um parafuso de", "i", 60) + [("zinco", "g", 56)], XE, 310, passo=0.1)
    E.foco(c, t, C["s16.a"] + 0.6, 0.4, lambda a: (E.pilula(c, "10 A", 300, 430, 54, "g", fundo=RED, a=a), E.pilula(c, "965 s", 560, 430, 54, "g", fundo=TINTA, a=a)))
    E.foco(c, t, C["s16.b"], 0.4, lambda a: Q.formula(c, "Zn^2+", XE, 600, 110, TINTA, a))
    E.foco(c, t, C["s16.c"], 0.4, lambda a: E.formula(c, "1 mol de Zn = 65 g", XE, 760, 70, "g", TINTA2, a))
    E.frase(c, t, C["s16.d"], ps("quantos gramas de zinco se depositam?", "i", 60), XE, 920, passo=0.08)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1560, cy=520, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s19"]:
        trilha(c, t, 1, [C["s18"]] * 4)
        conta(c, t, C["s18.a"], "Q = 10 · 965 = 9.650 C", W / 2, 400, 84, TINTA, "center")
        conta(c, t, C["s18.b"], "9.650 = 1/10 de 96.500", W / 2, 560, 76, TINTA2, "center")
        pilula_em(c, t, C["s18.c"], "0,1 mol de e⁻", W / 2, 760, 70, RED)
        return
    trilha(c, t, 3, [C["s19"]] * 4)
    Q.formula_em(c, t, C["s19.a"], "Zn^2+ + 2 e^- -> Zn", W / 2, 360, 100, align="center", cores={"coef": RED})
    conta(c, t, C["s19.b"], "0,1 ÷ 2 = 0,05 mol de Zn", W / 2, 520, 76, TINTA2, "center")
    conta(c, t, C["s19.c"], "0,05 · 65", W / 2 - 40, 680, 90, TINTA, "right")
    E.foco(c, t, C["s19.d"], 0.4, lambda a: E.formula(c, "= 3,25 g", W / 2, 680, 90, "g", COR, a))
    E.foco(c, t, C["s19.e"], 0.4, lambda a: (E.formula(c, "sem o 2: 6,5 g", W / 2, 860, 64, "g", ERRADO, a, "center")))
    if t >= C["s19.e"] + 0.8:
        E.risco(c, W / 2 - 260, 875, W / 2 + 260, 815, t, C["s19.e"] + 0.8, largura=8)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s20.a"], [("carga", "g", 62, COR)] + ps("= corrente × tempo", "i", 66)),
                     (C["s20.b"], [("96.500 C", "g", 62, COR)] + ps("= 1 mol de elétrons", "i", 66)),
                     (C["s20.c"], ps("a", "i", 66) + [("carga do íon", "g", 62)] + ps("diz quantos elétrons cada átomo pede", "i", 62))], 200, 390, 190, 64, 46)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], ps("dentro do", "i", 90) + [("núcleo", "g", 86, COR)], XE, 420, passo=0.12)
    E.frase(c, t, C["s21.b"], [("alfa,", "g", 80), ("beta", "g", 80), ("e", "i", 84), ("gama", "g", 80, COR)], XE, 580, passo=0.12)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, carga=b_carga, faraday=b_faraday, semi=b_semi, massa=b_massa,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
