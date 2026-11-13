"""Visual — Estudativo · QUI-ELE-008: eletrólise ígnea. Primeira aula do módulo Eletrólise.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001) e a da trilha Eletroquímica (QUI-ELE-001).
LINGUAGEM VISUAL DA ELETRÓLISE (as aulas QUI-ELE-008 a 010 e a 014 copiam daqui):
- CUBA = tanque de vidro (Q.VIDRO) com o líquido: sal derretido em laranja-quente (FUNDIDO), solução aquosa em Q.AGUA ou na cor
  do íon. Duas placas cinza; o GERADOR fica em cima, no meio do fio (peça local gerador(): caixa escura com "−" à esquerda e
  "+" à direita). Peça local cuba(), candidata ao kit.
- SINAL = COR DO POLO: placa ligada ao − do gerador = cátodo, pílula TINTA "cátodo −"; ligada ao + = ânodo, pílula turquesa
  "ânodo +" (as mesmas cores de sinal da pilha: − escuro, + turquesa). Os nomes seguem a regra das vogais da QUI-ELE-003.
- ÍONS = bolinha CPK do elemento com a carga escrita dentro ("+", "−", "3+"): cátion anda para o cátodo, ânion para o ânodo
  (peça local ion()). Elétrons azuis só nos fios, saindo do − do gerador para o cátodo e do ânodo para o + do gerador.
- PRODUTO = o que sai na placa: metal como camada cinza crescendo na placa; gás como bolhas subindo na cor do elemento
  (Cl₂ verde, H₂ branco, O₂ vermelho) (peça local bolhas()).
Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-008_eletrolise_ignea.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "cuba", "aluminio", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OXI, RED = "#E08A00", Q.ELETRON
FUNDIDO = "#F4B860"

assert Q.lados("2 NaCl -> 2 Na + Cl2")[0] == Q.lados("2 NaCl -> 2 Na + Cl2")[1]
assert Q.lados("MgCl2 -> Mg + Cl2")[0] == Q.lados("MgCl2 -> Mg + Cl2")[1]
assert Q.lados("2 Al2O3 -> 4 Al + 3 O2")[0] == Q.lados("2 Al2O3 -> 4 Al + 3 O2")[1]


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def s01():
            E.foco(c, t, C["s01.a"], 0.5, lambda a: (Q.atomo(c, 1450, 520, 170, "Al", a), centro(c, "alumínio", 1450, 760, 56, "g", TINTA, a)))
            E.frase(c, t, C["s01.a"], ps("o metal", "i", 70) + [("mais comum", "g", 66, COR)] + ps("da crosta", "i", 70), XE, 260, passo=0.12)
            E.frase(c, t, C["s01.b"], ps("no século dezenove,", "i", 64) + [("mais caro que o ouro", "g", 60, "#B8860B")], XE, 400, passo=0.1)
            E.frase(c, t, C["s01.c"], ps("ninguém o tirava do minério", "i", 60, TINTA2), XE, 540, passo=0.1)
            E.frase(c, t, C["s01.d"], ps("o que mudou:", "i", 70) + [("corrente elétrica", "g", 66, COR)], XE, 800, passo=0.12)
        E.saida(c, t, C["s02"] - 0.1, s01)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1580, 560, 230 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 230, passo=0.14)
    lista(c, t, [(C["s02.b"], [("pilha", "g", 62), ("x", "i", 66), ("eletrólise", "g", 62, COR)]),
                 (C["s02.c"], ps("o que sai em", "i", 66) + [("cada polo", "g", 62)]),
                 (C["s02.d"], ps("como se faz o", "i", 66) + [("alumínio", "g", 62)]),
                 (C["s02.e"], [("macete", "g", 62, COR), ("de", "i", 66), ("prova", "i", 66)])], XE, 390, 150, 62)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 76, TINTA2) + [("duas", "g", 70, COR), ("coisas", "i", 76, TINTA2)], XE, 200, passo=0.12)
    lista(c, t, [(C["s03.a"], [("pilha:", "g", 62)] + ps("a reação acontece sozinha", "i", 64)),
                 (C["s03.b"], [("ânodo", "g", 62, OXI)] + ps("oxidação,", "i", 64) + [("cátodo", "g", 62, RED)] + ps("redução", "i", 64)),
                 (C["s03.c"], ps("composto iônico conduz", "i", 64) + [("derretido", "g", 62, COR)])], XE, 380, 170, 64, 42)
    if t >= C["s03.c"] + 1.2:
        for k in range(6):
            el, ch = (("Na", "+"), ("Cl", "−"))[k % 2]
            f = (t * 0.3 + k / 6) % 1
            ion(c, 500 + 160 * k + 40 * math.sin(t + k), 900 + 30 * math.sin(t * 1.3 + k), el, ch, 30, ep(t, C["s03.c"] + 1.2, 0.4))
        E.foco(c, t, C["s03.c"] + 1.6, 0.4, lambda a: E.escreve(c, "íons livres", XE, 920, 50, "i", TINTA2, a))


# ---------------- pilha x eletrólise ----------------
def b_ideia(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], [("pilha", "g", 80, OXI)], 480, 250, "center")
        E.foco(c, t, C["s04"] + 0.4, 0.4, lambda a: E.pilula(c, "reação sozinha → corrente", 480, 380, 48, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s04.b"], [("eletrólise", "g", 80, COR)], 1440, 250, "center")
        E.foco(c, t, C["s04.c"], 0.4, lambda a: E.pilula(c, "corrente de fora, de um gerador", 1440, 380, 44, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s04.d"], 0.4, lambda a: E.pilula(c, "força uma reação que não iria sozinha", 1440, 470, 40, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s04.c"], 0.5, lambda a: gerador(c, 1440, 640, a))
        E.frase(c, t, C["s04.e"], ps("química vira eletricidade", "i", 60), 480, 820, "center", 0.1)
        E.frase(c, t, C["s04.f"], ps("eletricidade vira química", "i", 60), 1440, 820, "center", 0.1)
        if t >= C["s04"] + 0.2:
            M.line(c, W / 2, 200, W / 2, 900, CINZA, ep(t, C["s04"] + 0.2, 0.5), 3)
        return
    E.frase(c, t, C["s05.a"], [("ígnea", "g", 110, COR)] + ps("= com fogo", "i", 90), XE, 300, passo=0.12)
    E.frase(c, t, C["s05.a"] + 1.4, ps("a substância derretida, sem água", "i", 60, TINTA2), XE, 410, passo=0.1)
    E.foco(c, t, C["s05.b"], 0.4, lambda a: (Q.formula(c, "NaCl", XE, 600, 130, TINTA, a), E.escreve(c, "derrete a 801 °C", XE + 380, 590, 70, "g", OXI, a)))
    if t >= C["s05.c"]:
        K = Cuba(1400, 960, 760, 260)
        q = ep(t, C["s05.c"], 0.5)
        M.rrect(c, K.cx - K.w / 2, K.yb - K.h, K.w, K.h, 20, FUNDIDO, 0.85 * q)
        for k in range(8):
            el, ch = (("Na", "+"), ("Cl", "−"))[k % 2]
            ion(c, K.cx - 300 + 85 * k + 20 * math.sin(t * 1.5 + k), K.yb - 130 + 50 * math.sin(t + k * 1.7), el, ch, 28, q)
        E.foco(c, t, C["s05.c"] + 0.5, 0.4, lambda a: E.escreve(c, "íons livres para andar", XE, 800, 56, "i", TINTA, a))


# ---------------- a cuba ----------------
K1 = Cuba(W / 2, 900, 980, 430)


def b_cuba(c, t, C, b):
    cuba(c, t, C["s06.a"], K1, te=C["s06.b"], tp=C["s06.c"])
    ions_andam(c, t, C["s07.a"], K1, "Na", "+", "Cl", "−")
    if t < C["s07"]:
        E.frase(c, t, C["s06"], ps("duas placas no sal derretido, ligadas ao", "i", 56, TINTA2) + [("gerador", "g", 52)], W / 2, 110, "center", 0.08)
        E.foco(c, t, C["s06.b"], 0.4, lambda a: E.escreve(c, "empurra elétrons: negativa", K1.xc - 300, K1.yfio - 80, 46, "i", TINTA, a))
        E.foco(c, t, C["s06.c"], 0.4, lambda a: E.escreve(c, "puxa elétrons: positiva", K1.xa - 120, K1.yfio - 80, 46, "i", TINTA, a))
        return
    E.frase(c, t, C["s07.a"], [("cátion +", "g", 52, "#8E59D9")] + ps("vai à placa negativa;", "i", 56) + [("ânion −", "g", 52, "#2DB24A")] + ps("à positiva", "i", 56), W / 2, 110, "center", 0.08)
    E.foco(c, t, C["s07.c"], 0.4, lambda a: E.pilula(c, "opostos se atraem", W / 2, 1020, 46, "g", fundo=TINTA2, a=a))


# ---------------- polos ----------------
def b_polos(c, t, C, b):
    dep = ease_io(prog(t, C["s08.b"], 3.0))
    cuba(c, t, -10, K1, te=-10, tp=-10 if t < C["s08.d"] else None, polos=t < C["s08.d"], deposito=dep)
    ions_andam(c, t, -10, K1, "Na", "+", "Cl", "−")
    if t >= C["s08.d"]:
        E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "cátodo −", K1.xc - 190, K1.yt + 40, 44, "g", fundo=TINTA, a=a))
    if t >= C["s09.e"]:
        E.foco(c, t, C["s09.e"], 0.4, lambda a: E.pilula(c, "ânodo +", K1.xa + 190, K1.yt + 40, 44, "g", fundo=E.COR, a=a))
    elif t < C["s08.d"]:
        pass
    if t < C["s09"]:
        E.foco(c, t, C["s08.a"], 0.4, lambda a: Q.formula(c, "Na^+ + e^- -> Na", W / 2, 110, 70, TINTA, a, "center"))
        E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "recebeu elétron: redução", K1.xc, K1.yb + 70, 44, "g", fundo=RED, a=a))
        E.foco(c, t, C["s08.e"], 0.4, lambda a: E.escreve(c, "sódio líquido", K1.xc + 60, K1.yt + 140, 44, "g", TINTA, a))
        return
    bolhas(c, t, C["s09.c"], K1.xa, K1.yb - 60, K1.yt + 20, "#2DB24A")
    if t < C["s10"]:
        E.foco(c, t, C["s09.a"], 0.4, lambda a: Q.formula(c, "2 Cl^- -> Cl2 + 2 e^-", W / 2, 110, 70, TINTA, a, "center"))
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "gás cloro", K1.xa, K1.yb + 70, 44, "g", fundo="#2DB24A", a=a))
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.pilula(c, "perdeu elétron: oxidação", K1.xa + 150, K1.yt + 130, 40, "g", fundo=OXI, a=a))
        return
    E.foco(c, t, C["s10.b"], 0.4, lambda a: E.pilula(c, "ânodo = oxidação; cátodo = redução (como na pilha)", W / 2, 110, 42, "g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s10.c"], 0.4, lambda a: E.pilula(c, "mas os sinais trocaram", W / 2, 1030, 50, "g", fundo=ERRADO, a=a))


# ---------------- alumínio ----------------
def forno_al(c, t, t0, cx, yb, w, h, tc=None, ta=None):
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    M.rrect(c, cx - w / 2, yb - h, w, h, 18, "#4A4D55", q)
    M.rrect(c, cx - w / 2 + 24, yb - h + 60, w - 48, h - 90, 12, FUNDIDO, q)
    if tc is not None:
        M.rrect(c, cx - w / 2 + 24, yb - 30 - 70 * ep(t, tc, 1.5), w - 48, 70 * ep(t, tc, 1.5) + 6, 10, "#C8CDD6", q)
    for k in range(3):
        x = cx - w * 0.3 + k * w * 0.3
        M.rrect(c, x - 50, yb - h - 60, 100, h * 0.55, 8, "#2A2B31", q)
        if ta is not None:
            bolhas(c, t, ta + 0.2 * k, x, yb - h + h * 0.5, yb - h + 70, "#8A8D96", 4, 10)


def b_aluminio(c, t, C, b):
    if t < C["s12"]:
        def s11():
            E.frase(c, t, C["s11"], ps("o", "i", 70) + [("alumínio", "g", 66, COR)], XE, 200, passo=0.12)
            E.foco(c, t, C["s11.a"], 0.4, lambda a: (E.bola(c, 360, 420, 80, "#B5532A", a), centro(c, "bauxita", 360, 560, 46, "i", TINTA2, a)))
            if t >= C["s11.a"] + 0.6:
                M.arrow(c, 470, 420, 600, 420, TINTA2, ep(t, C["s11.a"] + 0.6, 0.4), 6, 20, ep(t, C["s11.a"] + 0.6, 0.5))
            E.foco(c, t, C["s11.a"] + 1.0, 0.4, lambda a: (Q.formula(c, "Al2O3", 640, 450, 110, TINTA, a), E.escreve(c, "alumina", 650, 540, 46, "i", TINTA2, a)))
            E.foco(c, t, C["s11.b"], 0.4, lambda a: E.pilula(c, "derrete perto de 2.000 °C", 1500, 420, 50, "g", fundo=ERRADO, a=a))
            E.frase(c, t, C["s11.c"], ps("o truque de 1886: dissolver na", "i", 58) + [("criolita derretida", "g", 54, COR)], XE, 750, passo=0.08)
            E.foco(c, t, C["s11.d"], 0.4, lambda a: E.pilula(c, "cerca de 1.000 °C", 1500, 880, 56, "g", fundo=OXI, a=a))
        E.saida(c, t, C["s12"] - 0.1, s11)
        return
    if t < C["s13"]:
        forno_al(c, t, C["s12"], 1300, 960, 900, 460, tc=C["s12.b"], ta=C["s12.d"])
        E.foco(c, t, C["s12"] + 0.3, 0.4, lambda a: Q.formula(c, "Al^3+  O^2-", XE, 200, 70, TINTA, a))
        E.foco(c, t, C["s12.a"], 0.4, lambda a: Q.formula(c, "Al^3+ + 3 e^- -> Al", XE, 330, 66, TINTA, a))
        E.foco(c, t, C["s12.b"], 0.4, lambda a: E.pilula(c, "alumínio líquido no fundo: cátodo", 1300, 1030, 44, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s12.c"], 0.4, lambda a: E.pilula(c, "ânodos de carvão", 1300, 410, 44, "g", fundo="#2A2B31", a=a))
        E.foco(c, t, C["s12.d"], 0.4, lambda a: E.escreve(c, "o oxigênio queima o carvão:", XE, 460, 48, "i", TINTA2, a))
        E.foco(c, t, C["s12.d"] + 0.4, 0.4, lambda a: Q.formula(c, "C + O2 -> CO2", XE, 540, 60, TINTA, a))
        E.foco(c, t, C["s12.e"], 0.4, lambda a: E.escreve(c, "os ânodos se gastam", XE, 640, 48, "g", OXI, a))
        return
    E.frase(c, t, C["s13.a"], ps("gasta uma", "i", 70) + [("montanha de energia", "g", 66, OXI)], XE, 280, passo=0.12)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: (M.rrect(c, 360, 440, 170, 280, 30, "#C8CDD6", a), M.rrect(c, 380, 470, 130, 60, 8, E.COR, a)))
    E.foco(c, t, C["s13.b"] + 0.4, 0.4, lambda a: (E.escreve(c, "reciclar:", 620, 560, 64, "i", TINTA, a), E.escreve(c, "cerca de 5%", 620, 660, 90, "g", COR, a), E.escreve(c, "da energia", 620, 740, 56, "i", TINTA, a)))
    E.frase(c, t, C["s13.c"], ps("no Brasil, quase toda lata volta para a fábrica", "i", 56, TINTA2), XE, 930, passo=0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s14.a"], ps("cátodo é sempre o positivo?", "i", 64), XE + 450, 190, passo=0.1)
    E.frase(c, t, C["s14.b"], ps("o sinal vem de", "i", 64) + [("quem manda os elétrons", "g", 60, COR)], XE, 360, passo=0.1)
    for k, (tk, titulo, an, ca, cor_a, cor_c) in enumerate(((C["s14.c"], "pilha", "ânodo −", "cátodo +", TINTA, E.COR), (C["s14.d"], "eletrólise", "ânodo +", "cátodo −", E.COR, TINTA))):
        x = 560 + 820 * k
        E.foco(c, t, tk, 0.4, lambda a, x=x, titulo=titulo: E.escreve(c, titulo, x - 140, 520, 70, "g", TINTA, a))
        E.foco(c, t, tk + 0.3, 0.4, lambda a, x=x, an=an, cor_a=cor_a: E.pilula(c, an, x, 640, 54, "g", fundo=cor_a, a=a))
        E.foco(c, t, tk + 0.6, 0.4, lambda a, x=x, ca=ca, cor_c=cor_c: E.pilula(c, ca, x, 760, 54, "g", fundo=cor_c, a=a))
    E.foco(c, t, C["s14.c"] + 0.9, 0.4, lambda a: E.escreve(c, "quem manda: o ânodo", 400, 880, 48, "i", TINTA2, a))
    E.foco(c, t, C["s14.d"] + 0.9, 0.4, lambda a: E.escreve(c, "quem manda: o gerador", 1200, 880, 48, "i", TINTA2, a))


# ---------------- macete (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s16"]:
        E.frase(c, t, C["s15"], ps("o macete de prova", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        for k, (tk, w1, w2, cor) in enumerate(((C["s15.a"], "Cátion", "Cátodo", "#B8A1FF"), (C["s15.b"], "Ânion", "Ânodo", "#7EE08A"))):
            y = 400 + 200 * k
            n = 3 if k == 0 else 2
            E.foco(c, t, tk, 0.4, lambda a, w1=w1, y=y, cor=cor, n=n: (E.escreve(c, w1[:n], 420, y, 130, "g", cor, a), E.escreve(c, w1[n:], 420 + E.larg(w1[:n], "g", 130) + 4, y, 130, "g", BR, a)))
            E.foco(c, t, tk + 0.4, 0.4, lambda a, y=y: E.escreve(c, "→", 900, y, 110, "g", CLARO, a))
            E.foco(c, t, tk + 0.6, 0.4, lambda a, w2=w2, y=y, cor=cor, n=n: (E.escreve(c, w2[:n], 1080, y, 130, "g", cor, a), E.escreve(c, w2[n:], 1080 + E.larg(w2[:n], "g", 130) + 4, y, 130, "g", BR, a)))
        E.frase(c, t, C["s15.c"], ps("o começo da palavra é igual", "i", 62, CLARO), W / 2, 760, "center", 0.1)
        E.frase(c, t, C["s15.e"], [("metal", "g", 60, BR)] + ps("no cátodo,", "i", 62, CLARO) + [("ametal", "g", 60, BR)] + ps("no ânodo", "i", 62, CLARO), W / 2, 900, "center", 0.1)
        return
    E.frase(c, t, C["s16.a"], ps("no sal derretido, o cátion de metal só pode", "i", 58, CLARO) + [("ganhar elétrons", "g", 54, BR)], W / 2, 300, "center", 0.08)
    E.frase(c, t, C["s16.b"], ps("o ânion só pode", "i", 58, CLARO) + [("perder", "g", 54, BR)], W / 2, 410, "center", 0.1)
    E.frase(c, t, C["s16.c"], [("não", "g", 60, ERRADO), ("compensa", "i", 62, CLARO)] + ps("com água junto:", "i", 62, CLARO), W / 2, 620, "center", 0.1)
    pilula_em(c, t, C["s16.d"], "a água disputa os polos: próxima aula", W / 2, 750, 50, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s17.a"], ps("o magnésio vem da eletrólise ígnea do", "i", 56, TINTA2) + [("cloreto de magnésio", "g", 52)], XE, 290, passo=0.06)
    E.foco(c, t, C["s17.a"] + 1.6, 0.4, lambda a: Q.formula(c, "MgCl2", XE, 450, 120, TINTA, a))
    E.foco(c, t, C["s17.b"], 0.4, lambda a: (ion(c, XE + 560, 410, "Mg", "2+", 40, a), ion(c, XE + 680, 410, "Cl", "−", 34, a), E.escreve(c, "derretidos", XE + 760, 425, 50, "i", TINTA2, a)))
    E.frase(c, t, C["s17.c"], [("1", "g", 54, COR)] + ps("o que sai no cátodo? e no ânodo?", "i", 58), XE, 640, passo=0.08)
    E.frase(c, t, C["s17.d"], [("2", "g", 54, COR)] + ps("qual polo é o negativo?", "i", 58), XE, 750, passo=0.08)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1560, cy=640, r=170)


# ---------------- resposta ----------------
K2 = Cuba(W / 2, 920, 900, 380)


def b_resposta(c, t, C, b):
    cuba(c, t, C["s19"], K2, te=C["s19"] + 0.5, tp=C["s19.e"], deposito=ease_io(prog(t, C["s19.b"], 2.5)))
    ions_andam(c, t, C["s19.a"], K2, "Mg", "2+", "Cl", "−")
    bolhas(c, t, C["s19.d"], K2.xa, K2.yb - 60, K2.yt + 20, "#2DB24A")
    E.foco(c, t, C["s19.b"], 0.4, lambda a: Q.formula(c, "Mg^2+ + 2 e^- -> Mg", 480, 110, 62, TINTA, a, "center"))
    E.foco(c, t, C["s19.d"], 0.4, lambda a: Q.formula(c, "2 Cl^- -> Cl2 + 2 e^-", 1440, 110, 62, TINTA, a, "center"))
    E.foco(c, t, C["s19.b"] + 0.6, 0.4, lambda a: E.pilula(c, "magnésio metálico", K2.xc, K2.yb + 70, 44, "g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s19.d"] + 0.6, 0.4, lambda a: E.pilula(c, "gás cloro", K2.xa, K2.yb + 70, 44, "g", fundo="#2DB24A", a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s20.a"], ps("a", "i", 66) + [("corrente de fora", "g", 62, COR)] + ps("força a reação", "i", 66)),
                     (C["s20.b"], [("cátion", "g", 62)] + ps("vai ao", "i", 66) + [("cátodo −", "g", 62)] + ps("e vira metal", "i", 66)),
                     (C["s20.c"], [("ânion", "g", 62)] + ps("vai ao", "i", 66) + [("ânodo +", "g", 62, COR)])], 240, 390, 190, 66, 46)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21"] + 0.6, [("eletrólise", "g", 100, COR), ("aquosa", "g", 100)], XE, 420)
    E.frase(c, t, C["s21.a"], ps("o sal na água", "i", 70) + [("não dá sódio", "g", 66, ERRADO)], XE, 570, passo=0.1)
    E.frase(c, t, C["s21.b"], ps("o que sai em cada polo?", "i", 66), XE, 690, passo=0.1)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, cuba=b_cuba, polos=b_polos, aluminio=b_aluminio,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
