"""Visual — Estudativo · QUI-LIG-007: polaridade da ligação e da molécula.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), a da trilha (QUI-LIG-001) e a do módulo (QUI-LIG-006): forma da
molécula em bola-vareta com lobos de par livre; δ+ e δ− em grotesca (delta()); NUVEM DA LIGAÇÃO (nuvem()) = elipse
turquesa translúcida, mais densa do lado que puxa; SETA DO DIPOLO (dipolo()) na cor da matéria, com a cruzinha no lado
positivo, apontando para o mais eletronegativo; soma das setas = seta grossa em TINTA (ou "soma = 0").
Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ligações Químicas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-LIG-007_polaridade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ligacao", "molecula", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# regra prática: par livre no central → polar; sem par livre e ligantes iguais → apolar
def regra(pares, ligantes):
    return "polar" if pares > 0 or len(set(ligantes)) > 1 else "apolar"


assert regra(0, ["O", "O"]) == "apolar" and regra(2, ["H", "H"]) == "polar" and regra(1, ["H"] * 3) == "polar"
assert regra(0, ["Cl"] * 4) == "apolar" and regra(0, ["H", "H", "H", "Cl"]) == "polar"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def lobo(c, cx, cy, ux, uy, L, a=1.0, escuro=False):
    """par livre: lobo translúcido saindo do centro na direção (ux, uy), com o par de elétrons na ponta"""
    if a <= 0:
        return
    ang = math.degrees(math.atan2(uy, ux))
    c.save()
    c.translate(cx, cy)
    c.rotate(ang)
    r = skia.Rect.MakeLTRB(L * 0.15, -L * 0.34, L * 1.05, L * 0.34)
    pf = skia.Paint(AntiAlias=True)
    pf.setShader(skia.GradientShader.MakeLinear([skia.Point(0, 0), skia.Point(L, 0)], [M.hexc(E.COR, 0.05 * a), M.hexc(E.COR, 0.32 * a)], [0, 1]))
    c.drawOval(r, pf)
    c.drawOval(r, M.paint(E.COR, 0.6 * a, stroke=3))
    for s_ in (-1, 1):
        c.drawCircle(L * 0.75, s_ * L * 0.09, L * 0.055, M.paint(Q.ELETRON, a))
    c.restore()


DIRS = {
    "linear": [(-1, 0), (1, 0)],
    "trigonal": [(0, -1), (-0.87, 0.5), (0.87, 0.5)],
    "tetra": [(0, -1), (-0.94, 0.33), (0.47, 0.6), (0.6, -0.12)],
    "angular": [(-0.78, 0.62), (0.78, 0.62)],
}


def forma(c, t, t0, central, ligantes, dirs, cx, cy, L=210, lobos=(), ordem=None, a=1.0, passo=0.2, tl=None, escuro=False, r_c=70, r_l=50):
    """molécula com geometria: central em (cx, cy); ligantes nas direções dirs (unidades); lobos = direções dos pares livres.
    ordem = ordem de ligação de cada ligante (2 = dupla). tl = instante de cada ligante. Varetas por baixo, átomos por cima"""
    if t < t0:
        return
    ordem = ordem or [1] * len(ligantes)
    for k, (ux, uy) in enumerate(lobos):
        lobo(c, cx, cy, ux, uy, L * 0.95, a * ep(t, t0 + 0.3 + 0.2 * k, 0.4), escuro)
    ts = tl or [t0 + 0.3 + passo * k for k in range(len(ligantes))]
    atras = [3] if dirs is DIRS["tetra"] and len(ligantes) == 4 else []
    pos = []
    for k in range(len(ligantes)):
        ux, uy = dirs[k]
        n = math.hypot(ux, uy)
        ux, uy = ux / n, uy / n
        q = ease_back(prog(t, ts[k], 0.45))
        pos.append((cx + ux * L, cy + uy * L, q))
        if q <= 0:
            continue
        nx, ny = -uy, ux
        offs = {1: (0,), 2: (-1, 1), 3: (-1.4, 0, 1.4)}[ordem[k]]
        for o in offs:
            M.line(c, cx + nx * o * 9, cy + ny * o * 9, cx + ux * L + nx * o * 9, cy + uy * L + ny * o * 9, Q.LIGA, a * min(1, q), 12 if ordem[k] == 1 else 8)
    for k in atras:
        x2, y2, q = pos[k]
        if q > 0:
            Q.atomo(c, x2, y2, r_l * q * 0.85, ligantes[k], a * 0.8, escuro=escuro)
    E.foco(c, t, t0, 0.4, lambda aa: Q.atomo(c, cx, cy, r_c, central, a * aa, escuro=escuro))
    for k in range(len(ligantes)):
        x2, y2, q = pos[k]
        if k not in atras and q > 0:
            Q.atomo(c, x2, y2, r_l * q, ligantes[k], a, escuro=escuro)


def angulo(c, t, t0, cx, cy, d1, d2, R, rot, a=1.0, cor=TINTA2):
    q = ep(t, t0, 0.4) * a
    if q <= 0:
        return
    a1 = math.degrees(math.atan2(d1[1], d1[0]))
    a2 = math.degrees(math.atan2(d2[1], d2[0]))
    sw = (a2 - a1) % 360
    if sw > 180:
        a1, sw = a2, 360 - sw
    c.drawArc(skia.Rect.MakeXYWH(cx - R, cy - R, 2 * R, 2 * R), a1, sw * ease_out(prog(t, t0, 0.5)), False, M.paint(cor, q, stroke=4))
    am = math.radians(a1 + sw / 2)
    E.formula(c, rot, cx + (R + 70) * math.cos(am), cy + (R + 70) * math.sin(am) + 18, 50, "g", cor, q, "center")


def _r(L):
    return dict(r_c=min(70, L * 0.34), r_l=min(50, L * 0.25))


def co2(c, t, t0, cx, cy, L=220, a=1.0, escuro=False):
    forma(c, t, t0, "C", ["O", "O"], DIRS["linear"], cx, cy, L, ordem=[2, 2], a=a, escuro=escuro, **_r(L))


def ch4(c, t, t0, cx, cy, L=200, a=1.0, escuro=False):
    forma(c, t, t0, "C", ["H"] * 4, DIRS["tetra"], cx, cy, L, a=a, escuro=escuro, **_r(L))


PIR = [(-0.92, 0.42), (0.92, 0.42), (0.2, 0.72)]


def nh3(c, t, t0, cx, cy, L=200, a=1.0, escuro=False):
    forma(c, t, t0, "N", ["H"] * 3, PIR, cx, cy, L, lobos=[(0, -1)], a=a, escuro=escuro, **_r(L))


def h2o(c, t, t0, cx, cy, L=210, a=1.0, escuro=False, lobos=True):
    forma(c, t, t0, "O", ["H", "H"], DIRS["angular"], cx, cy, L, lobos=[(-0.6, -0.8), (0.6, -0.8)] if lobos else (), a=a, escuro=escuro, **_r(L))


def delta(c, t, t0, x, y, sinal, size=56, escuro=False):
    cor = Q.ELETRON if sinal == "−" else (BR if escuro else TINTA)
    E.foco(c, t, t0, 0.4, lambda a: E.formula(c, "δ^{" + sinal + "}", x, y, size, "g", cor, a, "center"))


def nuvem(c, A, B, rA, rB, puxa=0.0, a=1.0):
    """nuvem do par da ligação de A a B; puxa 0 = no meio, 1 = toda para o lado de B"""
    if a <= 0:
        return
    ang = math.degrees(math.atan2(B[1] - A[1], B[0] - A[0]))
    L = math.dist(A, B)
    c.save(); c.translate(*A); c.rotate(ang)
    r = skia.Rect.MakeLTRB(-rA * 1.15, -max(rA, rB) * 1.1, L + rB * 1.15, max(rA, rB) * 1.1)
    pf = skia.Paint(AntiAlias=True)
    a0, a1 = lerp(0.22, 0.06, puxa), lerp(0.22, 0.48, puxa)
    pf.setShader(skia.GradientShader.MakeLinear([skia.Point(-rA, 0), skia.Point(L + rB, 0)], [M.hexc(E.COR, a0 * a), M.hexc(E.COR, a1 * a)], [0, 1]))
    c.drawOval(r, pf)
    c.drawOval(r, M.paint(E.COR, 0.5 * a, stroke=3))
    c.restore()


def dipolo(c, t, t0, A, B, cor=None, larg=7, d=0.6, a=1.0):
    """seta do dipolo de A (lado +) para B (lado −), com a cruzinha perto de A"""
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    cor = cor or E.COR
    M.arrow(c, A[0], A[1], lerp(A[0], B[0], p), lerp(A[1], B[1], p), cor, a, larg, 24)
    ux, uy = E._uni(*A, *B)
    cx, cy = A[0] + ux * 26, A[1] + uy * 26
    M.line(c, cx - uy * 18, cy + ux * 18, cx + uy * 18, cy - ux * 18, cor, a, larg)


def setas_mol(c, t, t0, cx, cy, dirs, L, passo=0.3, off=95):
    """uma seta do dipolo por ligação, do central para fora (para o ligante que puxa mais)"""
    for k, (ux, uy) in enumerate(dirs):
        n = math.hypot(ux, uy); ux, uy = ux / n, uy / n
        nx, ny = -uy, ux
        A = (cx + ux * L * 0.25 + nx * off, cy + uy * L * 0.25 + ny * off)
        B = (cx + ux * L * 0.95 + nx * off, cy + uy * L * 0.95 + ny * off)
        dipolo(c, t, t0 + passo * k, A, B)


def setas_dentro(c, t, t0, cx, cy, dirs, L, passo=0.3, off=95):
    """setas do ligante (H, menos eletronegativo) para o central"""
    for k, (ux, uy) in enumerate(dirs):
        n = math.hypot(ux, uy); ux, uy = ux / n, uy / n
        nx, ny = -uy, ux
        A = (cx + ux * L * 0.95 + nx * off, cy + uy * L * 0.95 + ny * off)
        B = (cx + ux * L * 0.25 + nx * off, cy + uy * L * 0.25 + ny * off)
        dipolo(c, t, t0 + passo * k, A, B)


def setas_lin(c, t, t0, cx, cy, L, dy=-115, passo=0.4):
    for k, s_ in enumerate((-1, 1)):
        dipolo(c, t, t0 + passo * k, (cx + s_ * 60, cy + dy), (cx + s_ * L * 0.95, cy + dy))


CCL4 = lambda c, t, t0, cx, cy, L=200, a=1.0, escuro=False: forma(c, t, t0, "C", ["Cl"] * 4, DIRS["tetra"], cx, cy, L, a=a, escuro=escuro, **_r(L))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("água", "g", 66), ("e", "i", 70), ("gás carbônico", "g", 66)], W / 2, 180, "center", 0.12)
        E.frase(c, t, C["s01.b"], ps("todas as ligações são", "i", 62) + [("polares", "g", 60, COR)], W / 2, 280, "center", 0.1)
        h2o(c, t, C["s01.a"] + 0.3, 540, 600, 190)
        co2(c, t, C["s01.a"] + 0.6, 1380, 640, 210)
        pilula_em(c, t, C["s01.c"], "polar", 540, 860, 60, E.COR)
        pilula_em(c, t, C["s01.c"] + 0.8, "apolar", 1380, 860, 60, TINTA)
        E.frase(c, t, C["s01.d"], ps("como pode?", "i", 70), W / 2, 1010, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1660, 560, 210 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("quando a", "i", 70), ("ligação", "g", 66, COR), ("é polar", "i", 70)]),
                 (C["s02.c"], [("quando a", "i", 70), ("molécula", "g", 66, COR), ("é polar", "i", 70)]),
                 (C["s02.d"], [("a", "i", 70), ("regra prática", "g", 66, COR), ("dos pares livres", "i", 70)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("duas ideias de antes", "i", 66, TINTA2), XE, 190, passo=0.12)
    E.frase(c, t, C["s03.a"], [("eletronegatividade", "g", 64, COR), ("=", "g", 64, TINTA2)], XE, 330, passo=0.12)
    E.frase(c, t, C["s03.a"] + 1.0, ps("a força com que o átomo puxa os elétrons da ligação", "i", 54), XE, 420, passo=0.06)
    E.frase(c, t, C["s03.b"], [("campeão:", "i", 60), ("flúor,", "g", 58), ("depois", "i", 60), ("oxigênio", "g", 58)], XE, 540, passo=0.1)
    E.frase(c, t, C["s03.c"], [("geometria:", "g", 60, COR)], XE, 700)
    co2(c, t, C["s03.d"], 560, 870, 150)
    h2o(c, t, C["s03.d"] + 0.6, 1300, 880, 140)
    E.foco(c, t, C["s03.d"] + 0.5, 0.4, lambda a: centro(c, "linear", 560, 1010, 50, "b", TINTA, a))
    E.foco(c, t, C["s03.d"] + 1.0, 0.4, lambda a: centro(c, "angular", 1300, 1030, 50, "b", TINTA, a))


# ---------------- ligação (s04–s06) ----------------
def b_ligacao(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04"], ps("átomos iguais", "i", 70, TINTA2), XE, 200, passo=0.12)
            Q.formula_em(c, t, C["s04.a"], "Cl2", XE, 360, 120)
            A, B = (760, 600), (1160, 600)
            E.foco(c, t, C["s04.a"] + 0.4, 0.5, lambda a: (nuvem(c, A, B, 90, 90, 0.0, a), Q.atomo(c, *A, 90, "Cl", a), Q.atomo(c, *B, 90, "Cl", a)))
            if t >= C["s04.c"]:
                Q._par(c, W / 2 - 0, 600, 90, 0, 11, Q.ELETRON, ep(t, C["s04.c"], 0.4), 2)
            E.frase(c, t, C["s04.b"], ps("puxam o par com a mesma força", "i", 58), W / 2, 800, "center", 0.08)
            E.frase(c, t, C["s04.c"], ps("o par fica no meio", "i", 58, TINTA2), W / 2, 880, "center", 0.08)
            E.foco(c, t, C["s04.d"], 0.5, lambda a: E.pilula(c, "ligação apolar: sem polos", W / 2, 990, 60, "g", fundo=TINTA, a=a))
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    E.frase(c, t, C["s05"], ps("átomos diferentes", "i", 70, TINTA2), XE, 200, passo=0.12)
    Q.formula_em(c, t, C["s05.a"], "HCl", XE, 360, 120)
    A, B = (760, 600), (1160, 600)
    puxa = ease_io(prog(t, C["s05.b"], 1.0))
    E.foco(c, t, C["s05.a"] + 0.4, 0.5, lambda a: (nuvem(c, A, B, 70, 100, puxa, a), Q.atomo(c, *A, 64, "H", a), Q.atomo(c, *B, 100, "Cl", a)))
    if t >= C["s05.a"] + 0.6:
        Q._par(c, lerp(W / 2, 1060, puxa), 600, 90, 0, 11, Q.ELETRON, 1, 2)
    E.frase(c, t, C["s05.b"], ps("o cloro puxa mais o par", "i", 58), 1300, 380, passo=0.08)
    delta(c, t, C["s05.c"], 1160, 470, "−", 70)
    delta(c, t, C["s05.d"], 760, 500, "+", 70)
    E.foco(c, t, C["s05.e"], 0.4, lambda a: E.escreve(c, "δ = delta: carga parcial", 1300, 470, 46, "b", TINTA2, a))
    if t >= C["s06"]:
        E.frase(c, t, C["s06.a"], [("dipolo:", "g", 62, COR)] + ps("um polo + e um polo −", "i", 62), XE, 820, passo=0.1)
        E.foco(c, t, C["s06.b"], 0.4, lambda a: E.pilula(c, "ligação polar", 1500, 800, 54, "g", fundo=E.COR, a=a))
        dipolo(c, t, C["s06.c"], (700, 730), (1180, 730))
        E.frase(c, t, C["s06.c"] + 0.6, ps("a seta aponta para quem puxa mais", "i", 56, TINTA2), XE, 940, passo=0.08)


# ---------------- molécula (s07–s09) ----------------
def b_molecula(c, t, C, b):
    if t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07.a"], ps("cada ligação é uma seta puxando", "i", 62), XE, 220, passo=0.1)
            E.frase(c, t, C["s07.b"], ps("o que decide é a soma:", "i", 62) + [("cabo de guerra", "g", 58, COR)], XE, 330, passo=0.1)
            # corda com nó
            M.line(c, 360, 620, 1560, 620, "#C9A36B", 1, 12)
            E.bola(c, W / 2, 620, 18, TINTA)
            for s_ in (-1, 1):
                dipolo(c, t, C["s07.b"] + 0.5, (W / 2 + s_ * 120, 540), (W / 2 + s_ * 520, 540))
            E.frase(c, t, C["s07.c"], ps("forças se cancelam:", "i", 58) + [("apolar", "g", 56, TINTA)], XE, 820, passo=0.1)
            E.frase(c, t, C["s07.d"], ps("sobra puxão para um lado:", "i", 58) + [("polar", "g", 56, COR)], XE, 920, passo=0.1)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    if t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08"], [("gás carbônico", "g", 70, COR)], XE, 200)
            co2(c, t, C["s08"] + 0.2, W / 2, 540, 260)
            setas_lin(c, t, C["s08.a"], W / 2, 540, 260)
            E.frase(c, t, C["s08.b"], ps("as ligações são polares", "i", 58), XE, 760, passo=0.08)
            E.frase(c, t, C["s08.c"], ps("mesma força, sentidos opostos", "i", 58, TINTA2), XE, 850, passo=0.08)
            E.foco(c, t, C["s08.d"], 0.5, lambda a: (E.pilula(c, "soma = 0 · apolar", 1450, 820, 60, "g", fundo=TINTA, a=a)))
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    E.frase(c, t, C["s09"], [("água", "g", 70, COR)], XE, 200)
    cx, cy, L = 960, 520, 230
    h2o(c, t, C["s09"] + 0.2, cx, cy, L)
    setas_dentro(c, t, C["s09.a"], cx, cy, DIRS["angular"], L, 0.3, 0)
    if t >= C["s09.c"]:
        p = ease_io(prog(t, C["s09.c"], 0.6))
        M.arrow(c, cx, cy + 330, cx, lerp(cy + 330, cy + 170, p), TINTA, 1, 12, 34)
    E.foco(c, t, C["s09.c"] + 0.5, 0.4, lambda a: centro(c, "a soma", cx, cy + 400, 50, "b", TINTA, a))
    delta(c, t, C["s09.d"], cx, cy - 210, "−", 64)
    delta(c, t, C["s09.d"] + 0.4, cx - L * 0.78 - 20, cy + L * 0.62 + 100, "+", 60)
    delta(c, t, C["s09.d"] + 0.5, cx + L * 0.78 + 20, cy + L * 0.62 + 100, "+", 60)
    E.frase(c, t, C["s09.b"], ps("as setas apontam para o O", "i", 56), XE, 400, passo=0.08)
    E.frase(c, t, C["s09.c"], ps("e se somam", "i", 56, TINTA2), XE, 490, passo=0.08)
    E.foco(c, t, C["s09.d"], 0.5, lambda a: E.pilula(c, "polar", XE + 120, 640, 70, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s10.a"], [("ligação polar", "g", 70), ("→", "g", 70, TINTA2), ("molécula polar?", "g", 70, ERRADO)], XE, 380, passo=0.15)
    if t >= C["s10.a"] + 1.6:
        E.risco(c, XE + 560, 400, XE + 1120, 320, t, C["s10.a"] + 1.6, largura=10)
    co2(c, t, C["s10.b"], 960, 620, 220)
    setas_lin(c, t, C["s10.b"] + 0.4, 960, 620, 220, passo=0.2)
    E.foco(c, t, C["s10.b"] + 1.2, 0.4, lambda a: centro(c, "ligações polares, molécula apolar", 960, 790, 54, "b", TINTA, a))
    E.frase(c, t, C["s10.c"], ps("quem decide:", "i", 62) + [("a geometria", "g", 60, COR)] + ps("e os átomos das pontas", "i", 62), W / 2, 950, "center", 0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s12"]:
        def s11():
            E.frase(c, t, C["s11.a"], [("regra prática", "g", 72, BR), ("dos", "i", 76, CLARO), ("pares livres", "g", 72, E.CLARO)], W / 2, 150, "center", 0.12)
            E.frase(c, t, C["s11.b"], ps("par livre no central?", "i", 62, BR) + [("→ polar", "g", 60, E.CLARO)], XE, 290, passo=0.1)
            E.frase(c, t, C["s11.c"], ps("sem par livre e ligantes iguais?", "i", 62, BR) + [("→ apolar", "g", 60, E.CLARO)], XE, 400, passo=0.1)
            co2(c, t, C["s11.d"], 560, 600, 130, escuro=True)
            E.foco(c, t, C["s11.d"] + 0.4, 0.4, lambda a: centro(c, "apolar", 560, 720, 56, "g", BR, a))
            h2o(c, t, C["s11.e"], 1360, 600, 120, escuro=True)
            E.foco(c, t, C["s11.e"] + 0.4, 0.4, lambda a: centro(c, "polar", 1360, 740, 56, "g", E.CLARO, a))
            E.frase(c, t, C["s11.f"], ps("dois átomos: iguais, apolar; diferentes, polar", "i", 56, CLARO), W / 2, 880, "center", 0.07)
            Q.molecula(c, t, C["s11.f"] + 1.4, "Cl2", 760, 990, 90, escuro=True)
            Q.molecula(c, t, C["s11.f"] + 1.8, "HCl", 1160, 990, 90, escuro=True)
        E.saida(c, t, C["s12"] - 0.1, s11)
        return
    E.frase(c, t, C["s12.a"], ps("par livre: um lado diferente do outro", "i", 60, BR), W / 2, 220, "center", 0.08)
    E.frase(c, t, C["s12.b"], ps("sem par livre e ligantes iguais: simétrica, as setas se anulam", "i", 54, CLARO), W / 2, 320, "center", 0.06)
    E.frase(c, t, C["s12.c"], [("não", "g", 60, ERRADO), ("compensa:", "i", 62, CLARO)] + ps("ligantes diferentes", "i", 62, CLARO), W / 2, 500, "center", 0.1)
    Q.formula_em(c, t, C["s12.c"] + 1.4, "CH3Cl", 600, 760, 130, align="center", escuro=True)
    forma(c, t, C["s12.c"] + 1.8, "C", ["Cl", "H", "H", "H"], DIRS["tetra"], 1300, 760, 150, escuro=True, r_c=50, r_l=38)
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.pilula(c, "sem par livre, mas polar", W / 2, 1000, 56, "g", fundo=E.COR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 180)
    Q.formula_em(c, t, C["s13.a"], "CCl4", XE, 360, 130)
    E.frase(c, t, C["s13.a"] + 0.8, ps("um carbono com quatro cloros", "i", 54, TINTA2), XE, 450, passo=0.08)
    E.frase(c, t, C["s13.b"], ps("ligações C–Cl: polares", "i", 58), XE, 550, passo=0.08)
    E.frase(c, t, C["s13.c"], [("1", "g", 56, COR)] + ps("a molécula é polar ou apolar?", "i", 60), XE, 700, passo=0.08)
    E.frase(c, t, C["s13.d"], [("2", "g", 56, COR)] + ps("e a amônia,", "i", 60), XE, 810, passo=0.08)
    Q.formula_em(c, t, C["s13.d"] + 0.8, "NH3", XE + 470, 815, 80)
    if t < C["s14"]:
        CCL4(c, t, C["s13.a"] + 0.4, 1450, 520, 200)
    else:
        E.relogio(c, t, C["s14.a"], cx=1480, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s16"]:
        def s15():
            E.frase(c, t, C["s15"], ps("vamos lá", "i", 66, TINTA2), XE, 170)
            E.frase(c, t, C["s15.a"], ps("C: 4 ligações, nenhum par livre", "i", 58), XE, 290, passo=0.08)
            E.frase(c, t, C["s15.b"], ps("4 ligantes iguais: cloros", "i", 58), XE, 390, passo=0.08)
            CCL4(c, t, C["s15"] + 0.3, 1300, 560, 230)
            setas_mol(c, t, C["s15.d"], 1300, 560, DIRS["tetra"], 230, 0.25, 0)
            E.foco(c, t, C["s15.c"], 0.5, lambda a: E.pilula(c, "apolar", XE + 140, 560, 70, "g", fundo=CERTO, a=a))
            E.frase(c, t, C["s15.d"], ps("as setas vão para os cantos e se cancelam", "i", 52, TINTA2), XE, 960, passo=0.06)
        E.saida(c, t, C["s16"] - 0.1, s15)
        return
    E.frase(c, t, C["s16.a"], ps("amônia: 3 ligações + 1 par livre", "i", 60), XE, 220, passo=0.08)
    nh3(c, t, C["s16.a"] + 0.3, 1300, 560, 230)
    setas_dentro(c, t, C["s16.c"], 1300, 560, PIR, 230, 0.25, 0)
    if t >= C["s16.c"] + 1.0:
        p = ease_io(prog(t, C["s16.c"] + 1.0, 0.6))
        M.arrow(c, 1000, 760, 1000, lerp(760, 480, p), TINTA, 1, 12, 34)
        E.foco(c, t, C["s16.c"] + 1.3, 0.4, lambda a: centro(c, "soma ≠ 0", 1000, 840, 50, "b", TINTA, a))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.pilula(c, "tem par livre: polar", XE + 300, 380, 60, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s16.c"], ps("o N puxa mais que o H", "i", 58), XE, 560, passo=0.08)
    E.frase(c, t, C["s16.c"] + 1.4, ps("as setas vão para o N, no alto", "i", 54, TINTA2), XE, 660, passo=0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s17.a", [("ligação polar:", "g", 62)] + ps("eletronegatividades diferentes", "i", 64)),
                 ("s17.b", [("molécula polar:", "g", 62)] + ps("as setas não se cancelam", "i", 64)),
                 ("s17.c", [("par livre no central", "g", 62)] + ps("= polar", "i", 64)))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 50, a=a), centro(c, str(i + 1), 260, y - 2, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 350, y, passo=0.12)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 240)
    E.frase(c, t, C["s18.a"], [("semelhante", "g", 100, COR)], XE, 390)
    E.frase(c, t, C["s18.a"] + 0.5, [("dissolve", "i", 100), ("semelhante", "g", 100, COR)], XE, 510)
    for k, s_ in enumerate(("sal", "álcool", "óleo", "iodo")):
        pilula_em(c, t, C["s18.b"] + 0.3 * k, s_, XE + 90 + 230 * k, 660, 50, TINTA)
    E.frase(c, t, C["s18.b"] + 1.4, ps("na água ou na gasolina?", "i", 60), XE, 790, passo=0.1)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s18.c"] + 0.2, 0.4))
    E.frase(c, t, C["s18.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ligacao=b_ligacao, molecula=b_molecula, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
