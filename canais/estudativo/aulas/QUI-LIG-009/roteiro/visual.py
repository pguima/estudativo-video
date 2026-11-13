"""Visual — Estudativo · QUI-LIG-009: três forças intermoleculares.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), a da trilha (QUI-LIG-001) e a do módulo (QUI-LIG-006/007): forma em
bola-vareta, δ em grotesca, nuvem e seta do dipolo. Nesta aula: FORÇA ENTRE MOLÉCULAS = tracejado turquesa fino (dipolo
permanente), tracejado turquesa grosso (ligação de hidrogênio), tracejado cinza fino (dipolo induzido); ligação de DENTRO
da molécula = vareta cinza contínua. Ranking das forças = barras deitadas (E.colunas não, barras próprias com rótulo).
Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ligações Químicas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-LIG-009_tres_forcas_intermoleculares.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("inter", "hidrogenio", "atalho", "questao", "fim"))
BR = "#FFFFFF"

FON = {"F", "O", "N"}
def forca(h_em_fon, polar):
    return "ligação de hidrogênio" if h_em_fon else "dipolo permanente" if polar else "dipolo induzido"


assert forca(True, True) == "ligação de hidrogênio"      # HF, H₂O
assert forca(False, False) == "dipolo induzido"          # CO₂, CH₄
assert forca(False, True) == "dipolo permanente"         # H₂S, HCl


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


def traco(c, t, t0, A, B, tipo="perm", escuro=False):
    """força entre moléculas: perm = tracejado fino turquesa, h = grosso, ind = cinza fino"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    cor = {"perm": E.COR, "h": E.COR, "ind": "#9AA0A8"}[tipo]
    larg = {"perm": 4, "h": 8, "ind": 3}[tipo]
    p = ease_out(prog(t, t0, 0.5))
    M.line(c, A[0], A[1], lerp(A[0], B[0], p), lerp(A[1], B[1], p), cor, q, larg, dash=[12, 10])


def agua(c, t, t0, cx, cy, esc=60, giro=0.0, a=1.0, escuro=False):
    """água com O em cima (giro roda); devolve (O, H1, H2) na tela"""
    E.foco(c, t, t0, 0.4, lambda aa: Q.molecula_desenho(c, "H2O", cx, cy, esc, a * aa, giro=giro, escuro=escuro))
    return Q._pontos_mol(Q._mol("H2O"), cx, cy, esc, giro, 0)


def viz(P, iH, esc, d=1.7):
    """centro de uma água (giro 270, O à esquerda) cujo O fica na direção O→H, a d·esc do H"""
    O, Hh = P[0], P[iH]
    ux, uy = E._uni(*O, *Hh)
    ox, oy = Hh[0] + ux * esc * d, Hh[1] + uy * esc * d
    return ox + 0.413 * esc, oy


def hcl(c, t, t0, cx, cy, esc=70, a=1.0, escuro=False):
    E.foco(c, t, t0, 0.4, lambda aa: Q.molecula_desenho(c, "HCl", cx, cy, esc, a * aa, escuro=escuro))
    return Q._pontos_mol(Q._mol("HCl"), cx, cy, esc, 0, 0)


def ch4(c, t, t0, cx, cy, L=90, a=1.0, escuro=False):
    forma(c, t, t0, "C", ["H"] * 4, DIRS["tetra"], cx, cy, L, a=a, escuro=escuro, r_c=34, r_l=24)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("a água ferve: as bolhas são de quê?", "i", 62), XE, 200, passo=0.1)
        E.foco(c, t, C["s01.a"] + 0.3, 0.5, lambda a: Q.bequer(c, t, C["s01.a"] + 0.3, 520, 920, 360, 420, 0.7, Q.AGUA, graduacao=False))
        for k in range(5):
            u = ((t * 0.35 + k * 0.21) % 1)
            x, y = 440 + k * 40 + 12 * math.sin(t * 3 + k), lerp(880, 600, u)
            if t >= C["s01.a"] + 0.8:
                c.drawCircle(x, y, 26, M.paint(BR, 0.7, stroke=4))
                Q.molecula_desenho(c, "H2O", x, y + 2, 14, 0.9, rotulos=False)
        E.frase(c, t, C["s01.b"], ps("o vapor ainda é", "i", 62), 900, 440, passo=0.1)
        Q.formula_em(c, t, C["s01.b"] + 0.8, "H2O", 1400, 445, 90)
        E.frase(c, t, C["s01.c"], ps("o que a fervura rompe?", "i", 62), 900, 600, passo=0.1)
        P1 = agua(c, t, C["s01.d"], 1050, 800, 60, giro=200)
        P2 = agua(c, t, C["s01.d"] + 0.2, 1350, 800, 60, giro=-20)
        traco(c, t, C["s01.d"] + 0.5, P1[1], P2[0], "h")
        E.foco(c, t, C["s01.d"] + 0.8, 0.4, lambda a: centro(c, "a força entre as moléculas", 1200, 960, 50, "b", COR, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1660, 560, 210 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    E.frase(c, t, C["s02.b"], [("três forças", "g", 70, COR)] + ps("entre moléculas", "i", 72), XE, 420, passo=0.12)
    E.frase(c, t, C["s02.c"], ps("a principal no", "i", 66), XE, 560, passo=0.1)
    for k, f in enumerate(("CH4", "HCl", "H2O")):
        Q.formula_em(c, t, C["s02.c"] + 0.6 + 0.3 * k, f, XE + 470 + 230 * k, 565, 80)
    E.frase(c, t, C["s02.d"], [("+", "g", 66, COR), ("atalho", "g", 66, COR), ("de", "i", 70), ("prova", "i", 70)], XE, 700, passo=0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula de polaridade", "i", 66, TINTA2), XE, 190, passo=0.12)
    E.frase(c, t, C["s03.a"], [("polar:", "g", 62)] + ps("um lado", "i", 62), XE, 330, passo=0.1)
    E.foco(c, t, C["s03.a"] + 0.6, 0.4, lambda a: (E.formula(c, "δ^{+}", XE + 470, 330, 62, "g", TINTA, a), E.escreve(c, "e outro", XE + 560, 330, 62, "i", TINTA, a),
                                                  E.formula(c, "δ^{−}", XE + 820, 330, 62, "g", Q.ELETRON, a)))
    P = hcl(c, t, C["s03.a"] + 0.3, 1450, 320, 110)
    E.frase(c, t, C["s03.b"], [("apolar:", "g", 62)] + ps("sem polos", "i", 62), XE, 480, passo=0.1)
    ch4(c, t, C["s03.b"] + 0.3, 1450, 540, 110)
    E.frase(c, t, C["s03.c"], ps("entre os mais eletronegativos:", "i", 58), XE, 720, passo=0.08)
    for k, el in enumerate(("F", "O", "N")):
        Q.atomo_em(c, t, C["s03.c"] + 1.4 + 0.3 * k, XE + 900 + 150 * k, 700, 56, el)
    E.foco(c, t, C["s03.c"] + 2.0, 0.4, lambda a: E.escreve(c, "flúor, oxigênio, nitrogênio", XE + 830, 820, 46, "i", TINTA2, a))


# ---------------- dentro e fora (s04) ----------------
def b_inter(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("dentro:", "g", 62)] + ps("ligação covalente, forte", "i", 62), XE, 220, passo=0.1)
    E.frase(c, t, C["s04.b"], [("entre:", "g", 62, COR)] + ps("forças bem mais fracas", "i", 62), XE, 330, passo=0.1)
    E.frase(c, t, C["s04.c"], [("forças intermoleculares", "g", 60, COR)], XE, 430)
    sep = ease_io(prog(t, C["s04.d"], 1.6))
    pos = [(980, 660, 200), (1260, 760, -30), (1180, 560, 130), (1480, 640, 250)]
    pts = []
    for k, (x, y, g) in enumerate(pos):
        dx, dy = (x - 1230) * sep * 0.9, (y - 660) * sep * 0.9
        pts.append(agua(c, t, C["s04"] + 0.1 * k, x + dx, y + dy, 58, giro=g))
    if t >= C["s04.a"]:
        q = ep(t, C["s04.a"], 0.4)
        O, H1, H2 = pts[0]
        M.line(c, *O, *H1, E.COR, q * 0.9, 10)
    if sep < 0.5:
        for A, B in ((pts[0][1], pts[2][0]), (pts[2][1], pts[3][0]), (pts[1][0], pts[0][2])):
            traco(c, t, C["s04.b"] + 0.3, A, B, "h")
    E.frase(c, t, C["s04.d"], [("ferver", "g", 60)] + ps("separa as moléculas", "i", 62), XE, 760, passo=0.1)
    E.frase(c, t, C["s04.e"], ps("rompe só as forças de fora", "i", 58, TINTA2), XE, 860, passo=0.08)
    E.foco(c, t, C["s04.e"] + 1.2, 0.4, lambda a: E.pilula(c, "as ligações de dentro ficam", XE + 330, 960, 46, "g", fundo=TINTA, a=a))


# ---------------- dipolo permanente (s05) ----------------
def b_permanente(c, t, C, b):
    E.frase(c, t, C["s05"], [("1", "g", 66, COR), ("dipolo permanente", "g", 76)], XE, 210, passo=0.12)
    E.frase(c, t, C["s05.a"], ps("entre moléculas polares, como o HCl", "i", 58), XE, 310, passo=0.08)
    E.frase(c, t, C["s05.a"] + 1.6, ps("o cloro puxa mais o par: polos", "i", 54, TINTA2), XE, 390, passo=0.08)
    xs = (420, 900, 1380)
    pts = [hcl(c, t, C["s05.a"] + 0.2 * k, x, 640, 120) for k, x in enumerate(xs)]
    for k, x in enumerate(xs):
        E.foco(c, t, C["s05.a"] + 1.0 + 0.1 * k, 0.4, lambda a, k=k: (E.formula(c, "δ^{+}", pts[k][0][0], 540, 48, "g", TINTA, a, "center"),
                                                                      E.formula(c, "δ^{−}", pts[k][1][0], 540, 48, "g", Q.ELETRON, a, "center")))
    for k in range(2):
        traco(c, t, C["s05.b"] + 0.4 * k, (pts[k][1][0] + 70, 640), (pts[k + 1][0][0] - 50, 640), "perm")
    E.frase(c, t, C["s05.b"], ps("o lado + de uma atrai o lado − da vizinha", "i", 58), XE, 860, passo=0.08)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "polos sempre lá: dipolo-dipolo", 1350, 980, 48, "g", fundo=E.COR, a=a))


# ---------------- ligação de hidrogênio (s06) ----------------
def b_hidrogenio(c, t, C, b):
    E.frase(c, t, C["s06"], [("2", "g", 66, COR), ("ligação de hidrogênio", "g", 76)], XE, 210, passo=0.12)
    E.frase(c, t, C["s06.a"], ps("um caso especial, mais forte", "i", 58, TINTA2), XE, 300, passo=0.08)
    E.frase(c, t, C["s06.b"], [("H", "g", 60, COR)] + ps("ligado direto a", "i", 60), XE, 420, passo=0.1)
    for k, el in enumerate(("F", "O", "N")):
        Q.atomo_em(c, t, C["s06.b"] + 0.8 + 0.2 * k, XE + 540 + 110 * k, 400, 44, el)
    E.frase(c, t, C["s06.c"], ps("o H fica muito positivo", "i", 58), XE, 530, passo=0.08)
    E.frase(c, t, C["s06.d"], ps("e gruda no par livre da vizinha", "i", 58), XE, 630, passo=0.08)
    esc = 80
    P1 = Q._pontos_mol(Q._mol("H2O"), 1180, 640, esc, 270, 0)
    c2, c3 = viz(P1, 2, esc), viz(P1, 1, esc)
    P2 = Q._pontos_mol(Q._mol("H2O"), *c2, esc, 270, 0)
    P3 = Q._pontos_mol(Q._mol("H2O"), *c3, esc, 270, 0)
    traco(c, t, C["s06.d"] + 0.4, P1[2], P2[0], "h")
    traco(c, t, C["s06.d"] + 0.8, P1[1], P3[0], "h")
    agua(c, t, C["s06.b"], 1180, 640, esc, giro=270)
    agua(c, t, C["s06.d"] - 0.4, *c2, esc, giro=270)
    agua(c, t, C["s06.d"] - 0.2, *c3, esc, giro=270)
    if t >= C["s06.c"]:
        E.foco(c, t, C["s06.c"], 0.4, lambda a: (E.formula(c, "δ^{+}", P1[2][0] - 30, P1[2][1] - 30, 44, "g", TINTA, a, "center"),
                                                E.formula(c, "δ^{−}", P2[0][0] - 10, P2[0][1] - 50, 44, "g", Q.ELETRON, a, "center")))
    E.foco(c, t, C["s06.e"], 0.4, lambda a: E.pilula(c, "a força entre as moléculas de água", W / 2, 980, 50, "g", fundo=E.COR, a=a))


# ---------------- dipolo induzido (s07–s08) ----------------
def b_induzido(c, t, C, b):
    if t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07"], [("3", "g", 66, COR), ("dipolo induzido", "g", 76)], XE, 210, passo=0.12)
            E.frase(c, t, C["s07.a"], ps("e as apolares, como o metano?", "i", 58), XE, 310, passo=0.08)
            A, B = (640, 690), (1180, 690)
            u1 = ease_io(prog(t, C["s07.c"], 0.8))
            u2 = ease_io(prog(t, C["s07.e"], 0.8))
            for k, (P, u) in enumerate(((A, u1), (B, u2))):
                def nuv(a, P=P, u=u):
                    pp = skia.Paint(AntiAlias=True)
                    cx = P[0] + 50 * u
                    pp.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, P[1]), 200, [M.hexc(Q.ELETRON, 0.30 * a), M.hexc(Q.ELETRON, 0.04 * a)], [0, 1]))
                    c.drawCircle(P[0], P[1], 190, pp)
                    c.drawCircle(P[0], P[1], 190, M.paint(Q.ELETRON, 0.35 * a, stroke=3))
                E.foco(c, t, C["s07.a"] + 0.2 * k, 0.5, nuv)
                ch4(c, t, C["s07.a"] + 0.2 * k, *P, 100)
            E.frase(c, t, C["s07.b"], ps("os elétrons não ficam parados", "i", 54, TINTA2), XE, 390, passo=0.08)
            if t >= C["s07.d"]:
                E.foco(c, t, C["s07.d"], 0.4, lambda a: (E.formula(c, "δ^{−}", A[0] + 150, 500, 54, "g", Q.ELETRON, a, "center"), E.formula(c, "δ^{+}", A[0] - 150, 500, 54, "g", TINTA, a, "center")))
                E.foco(c, t, C["s07.d"] + 0.2, 0.4, lambda a: centro(c, "dipolo relâmpago (instantâneo)", A[0], 930, 46, "b", TINTA, a))
            if t >= C["s07.e"]:
                E.foco(c, t, C["s07.e"] + 0.4, 0.4, lambda a: (E.formula(c, "δ^{−}", B[0] + 150, 500, 54, "g", Q.ELETRON, a, "center"), E.formula(c, "δ^{+}", B[0] - 150, 500, 54, "g", TINTA, a, "center")))
                traco(c, t, C["s07.e"] + 0.8, (A[0] + 190, 690), (B[0] - 190, 690), "ind")
            E.foco(c, t, C["s07.f"], 0.4, lambda a: E.pilula(c, "dipolo induzido (força de London): a mais fraca", W / 2, 1000, 46, "g", fundo=TINTA, a=a))
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    E.frase(c, t, C["s08.a"], ps("o dipolo induzido existe entre todas", "i", 62), XE, 220, passo=0.08)
    E.frase(c, t, C["s08.b"], ps("nas apolares, é o único", "i", 60, TINTA2), XE, 320, passo=0.08)
    E.frase(c, t, C["s08.b"] + 1.4, ps("força, em moléculas de tamanho parecido:", "i", 56), XE, 460, passo=0.08)
    barras = (("s08.c", "ligação de hidrogênio", 1.0, E.COR), ("s08.d", "dipolo permanente", 0.55, M.mix(E.COR, "#FFFFFF", 0.35)), ("s08.e", "dipolo induzido", 0.25, "#B8BCC4"))
    for k, (cue, nome, v, cor) in enumerate(barras):
        y = 580 + k * 150
        p = ease_out(prog(t, C[cue], 0.7))
        if p > 0:
            M.rrect(c, XE + 560, y - 50, 900 * v * p, 90, 20, cor, 1)
        E.foco(c, t, C[cue], 0.4, lambda a, y=y, nome=nome: E.escreve(c, nome, XE, y + 14, 50, "g", TINTA, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s09"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s09.a"], ps("a ligação de hidrogênio é a O–H de dentro?", "i", 58), XE + 460, 190, passo=0.08)
    esc = 110
    P1 = Q._pontos_mol(Q._mol("H2O"), 640, 660, esc, 270, 0)
    c2 = viz(P1, 2, esc, 2.0)
    P2 = Q._pontos_mol(Q._mol("H2O"), *c2, esc, 270, 0)
    if t >= C["s09.b"]:
        q = ep(t, C["s09.b"], 0.4)
        mx, my = (P1[0][0] + P1[2][0]) / 2, (P1[0][1] + P1[2][1]) / 2
        c.drawCircle(mx, my, 95, M.paint(ERRADO, q, stroke=7))
        E.foco(c, t, C["s09.b"], 0.4, lambda a: centro(c, "covalente (dentro)", 560, 900, 50, "b", ERRADO, a))
    traco(c, t, C["s09.c"], P1[2], P2[0], "h")
    agua(c, t, C["s09.a"] + 0.4, 640, 660, esc, giro=270)
    agua(c, t, C["s09.a"] + 0.6, *c2, esc, giro=270)
    mx, my = (P1[2][0] + P2[0][0]) / 2, (P1[2][1] + P2[0][1]) / 2
    E.foco(c, t, C["s09.d"], 0.4, lambda a: E.escreve(c, "ligação de hidrogênio (entre)", mx + 130, my + 70, 50, "b", COR, a))
    E.frase(c, t, C["s09.e"], ps("o nome engana: é força", "i", 62) + [("intermolecular", "g", 60, COR)], W / 2, 980, "center", 0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10"], ps("o atalho: perguntas em sequência", "i", 66, CLARO), W / 2, 150, "center", 0.1)
            linhas = (("s10.a", "H ligado direto a F, O ou N?", "ligação de hidrogênio"), ("s10.b", "não, mas é polar?", "dipolo permanente"), ("s10.c", "é apolar?", "dipolo induzido"))
            for k, (cue, perg, resp) in enumerate(linhas):
                y = 320 + k * 170
                E.frase(c, t, C[cue], ps(perg, "i", 60, BR), XE, y, passo=0.08)
                E.foco(c, t, C[cue] + 1.2, 0.4, lambda a, y=y, resp=resp: E.pilula(c, resp, 1500, y - 20, 52, "g", fundo=E.COR, a=a))
            E.foco(c, t, C["s10.d"], 0.5, lambda a: [Q.atomo(c, 760 + 180 * k, 900, 64, el, a, escuro=True) for k, el in enumerate(("F", "O", "N"))])
            E.foco(c, t, C["s10.e"], 0.5, lambda a: E.escreve(c, "FON, como fone", 1240, 925, 70, "g", E.CLARO, a))
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    E.frase(c, t, C["s11.a"], ps("vai da força mais forte para a mais fraca", "i", 60, BR), W / 2, 240, "center", 0.08)
    E.frase(c, t, C["s11.a"] + 1.6, ps("a primeira que der sim é a principal", "i", 56, CLARO), W / 2, 330, "center", 0.08)
    E.frase(c, t, C["s11.b"], [("cuidado:", "g", 60, ERRADO)] + ps("H preso a carbono não conta", "i", 62, BR), W / 2, 520, "center", 0.1)
    ch4(c, t, C["s11.c"], W / 2, 760, 150, escuro=True)
    E.foco(c, t, C["s11.c"] + 0.8, 0.4, lambda a: centro(c, "metano: 4 H, nenhuma ligação de hidrogênio", W / 2, 990, 50, "b", CLARO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s12"], ps("hora de testar: a força principal", "i", 66, COR), XE, 180, passo=0.1)
    for k, (cue, f, nome) in enumerate((("s12.a", "HF", "fluoreto de hidrogênio"), ("s12.b", "CO2", "gás carbônico"), ("s12.c", "H2S", "cheiro de ovo podre"))):
        y = 380 + k * 200
        Q.formula_em(c, t, C[cue], f, XE, y, 120)
        E.foco(c, t, C[cue] + 0.4, 0.4, lambda a, y=y, nome=nome: E.escreve(c, nome, XE + 330, y - 10, 54, "i", TINTA2, a))
    if t >= C["s13"]:
        E.relogio(c, t, C["s13.a"], cx=1500, cy=500, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s14"], ps("com as perguntas", "i", 62, TINTA2), XE, 170, passo=0.1)
    linhas = (("s14.a", "HF", "H ligado ao F", "ligação de hidrogênio", E.COR),
              ("s14.b", "CO2", "sem H, linear e apolar", "dipolo induzido", TINTA),
              ("s14.c", "H2S", "S não é F, O nem N", None, None))
    for k, (cue, f, motivo, resp, cor) in enumerate(linhas):
        y = 360 + k * 220
        Q.formula_em(c, t, C[cue], f, XE, y, 110)
        E.foco(c, t, C[cue] + 0.3, 0.4, lambda a, y=y, motivo=motivo: E.escreve(c, motivo, XE + 330, y - 10, 52, "i", TINTA, a))
        if resp:
            E.foco(c, t, C[cue] + 1.2, 0.4, lambda a, y=y, resp=resp, cor=cor: E.pilula(c, resp, 1500, y - 30, 54, "g", fundo=cor, a=a))
    E.foco(c, t, C["s14.d"], 0.4, lambda a: E.escreve(c, "mas é angular, com pares livres: polar", XE + 330, 870, 52, "i", TINTA2, a))
    E.foco(c, t, C["s14.d"] + 1.6, 0.4, lambda a: E.pilula(c, "dipolo permanente", 1500, 770, 54, "g", fundo=M.mix(E.COR, TINTA, 0.35), a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s15"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s15.a", [("apolares:", "g", 62)] + ps("dipolo induzido", "i", 64)),
                 ("s15.b", [("polares:", "g", 62)] + ps("dipolo permanente", "i", 64)),
                 ("s15.c", [("H em F, O, N:", "g", 62)] + ps("ligação de hidrogênio, a mais forte", "i", 64)))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 50, a=a), centro(c, str(i + 1), 260, y - 2, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 350, y, passo=0.12)
    E.saida(c, t, C["s16"] - 0.1, resumo)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 240)
    E.frase(c, t, C["s16.a"], [("pontos de", "i", 100), ("ebulição", "g", 100, COR)], XE, 400, passo=0.15)
    E.frase(c, t, C["s16.b"], ps("por que a água ferve tão acima do gás de ovo podre?", "i", 54), XE, 540, passo=0.07)
    for k, (f, v) in enumerate((("H2O", "100 °C"), ("H2S", "−60 °C"))):
        E.foco(c, t, C["s16.b"] + 1.0 + 0.4 * k, 0.4, lambda a, k=k, f=f, v=v: (Q.formula(c, f, XE + 520 * k, 720, 90, None, a),
                                                                            E.escreve(c, v, XE + 520 * k, 830, 76, "g", COR if k == 0 else TINTA2, a)))
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s16.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s16.c"] + 0.2, 0.4))
    E.frase(c, t, C["s16.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, inter=b_inter, permanente=b_permanente, hidrogenio=b_hidrogenio,
              induzido=b_induzido, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
