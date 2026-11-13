"""Visual — Estudativo · QUI-LIG-012: praticando polaridade e forças intermoleculares (prática, quatro questões inéditas).

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), a da trilha (QUI-LIG-001) e a do módulo (QUI-LIG-006 a 011): forma com
lobos de par livre, seta do dipolo, tracejado das forças, termômetro de ponto de ebulição, copo de camadas. Cada questão:
enunciado à esquerda, desenho à direita, relógio no lugar do desenho na pausa. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ligações Químicas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-LIG-012_praticando_polaridade_forcas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "fim"))
BR = "#FFFFFF"
F_H, F_P, F_I = E.COR, M.mix(E.COR, "#FFFFFF", 0.4), "#A9AEB6"
OLEO, IODO = "#F2C14E", "#7A3FA0"
PE = {"etanol": 78, "eter": -24, "Br2": 59, "I2": 184}
assert PE["etanol"] > PE["eter"] and PE["I2"] > PE["Br2"]
assert Q.contar("C2H6O") == Q.contar("CH3OCH3")


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


def termometro(c, t, t0, x, y0, y1, tmin, tmax, marcas=(-200, -100, 0, 100), escuro=False):
    """régua vertical: y0 = topo (tmax), y1 = base (tmin). Devolve T → y"""
    Y = lambda T: y1 - (T - tmin) / (tmax - tmin) * (y1 - y0)
    q = ep(t, t0, 0.5)
    if q > 0:
        tinta = BR if escuro else TINTA
        M.line(c, x, y1 + 10, x, lerp(y1 + 10, y0 - 10, ease_out(prog(t, t0, 0.6))), tinta, q, 6)
        for T in marcas:
            yy = Y(T)
            M.line(c, x - 16, yy, x + 16, yy, tinta, q, 4)
            E.formula(c, f"{T} °C".replace("-", "−"), x - 30, yy + 16, 40, "b", BR if escuro else TINTA2, q, "right")
        y0c = Y(0)
        M.line(c, x + 20, y0c, x + 1100, y0c, TINTA2 if not escuro else "#8A8D99", 0.35 * q, 3, dash=[12, 10])
    return Y


def ponto(c, t, t0, Y, x, T, f, cor, dx=40, escuro=False, rot=None):
    q = ease_back(prog(t, t0, 0.45))
    if q <= 0:
        return
    yy = Y(T)
    c.drawCircle(x, yy, 22 * q, M.paint(cor))
    c.drawCircle(x, yy, 22 * q, M.paint(TINTA if not escuro else BR, 0.6, stroke=3))
    a = min(1, prog(t, t0, 0.3))
    if f:
        Q.formula(c, f, x + dx, yy + 22, 62, None, a, escuro=escuro)
    E.escreve(c, (rot or f"{T} °C").replace("-", "−"), x + dx + 260, yy + 18, 52, "g", COR if not escuro else E.CLARO, a)


def titulo_q(c, t, t0, n):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 170, 50, a=a), centro(c, str(n), XE + 50, 194, 64, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.2, [("questão", "i", 76, COR)], XE + 130, 196)


def copo(c, cx, yb, w, h, camadas, a=1.0):
    if a <= 0:
        return
    x0 = cx - w / 2
    y = yb
    for hh, cor in camadas:
        y2 = y - hh
        c.drawRect(skia.Rect.MakeLTRB(x0 + 4, y2, x0 + w - 4, y - 4 if y == yb else y), M.paint(cor, 0.92 * a))
        y = y2
    pth = skia.Path()
    pth.moveTo(x0 - 6, yb - h - 10); pth.lineTo(x0, yb - h); pth.lineTo(x0, yb - 16); pth.quadTo(x0, yb, x0 + 16, yb)
    pth.lineTo(x0 + w - 16, yb); pth.quadTo(x0 + w, yb, x0 + w, yb - 16); pth.lineTo(x0 + w, yb - h); pth.lineTo(x0 + w + 6, yb - h - 10)
    c.drawPath(pth, M.paint(Q.VIDRO, a, stroke=5))


CHCL3 = lambda c, t, t0, cx, cy, L=200, a=1.0, escuro=False: forma(c, t, t0, "C", ["H", "Cl", "Cl", "Cl"], DIRS["tetra"], cx, cy, L, a=a, escuro=escuro, **_r(L))
METANO = lambda c, t, t0, cx, cy, L=200, a=1.0, escuro=False: forma(c, t, t0, "C", ["H"] * 4, DIRS["tetra"], cx, cy, L, a=a, escuro=escuro, **_r(L))
ETANOL = [("C", -1.1, 0.3), ("C", 0, -0.3), ("O", 1.1, 0.3, [60, 300]), ("H", 2.0, -0.2)]
ETER = [("C", -1.1, 0.3), ("O", 0, -0.3, [60, 120]), ("C", 1.1, 0.3)]


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.foco(c, t, C["s01.a"], 0.6, lambda a: (E.bola(c, 470, 470, 200 * ease_back(prog(t, C["s01.a"], 0.6)), a=a), centro(c, "4", 470, 560, 260, "g", E.SOBRE, a)))
    E.frase(c, t, C["s01.a"] + 0.4, [("questões", "g", 100)], 760, 430)
    E.frase(c, t, C["s01.a"] + 0.8, ps("criadas para esta aula", "i", 62, TINTA2), 760, 520, passo=0.1)
    for k, s_ in enumerate(("forma", "polaridade", "forças")):
        pilula_em(c, t, C["s01.b"] + 0.3 * k, s_, 860 + k * 290, 650, 54, E.COR)
    E.frase(c, t, C["s01.c"], ps("pause e resolva antes da resposta", "i", 62), W / 2, 900, "center", 0.1)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("o caminho é quase sempre o mesmo", "i", 66, TINTA2), XE, 190, passo=0.1)
    passos = (("s02.a", "Lewis"), ("s02.b", "geometria"), ("s02.c", "polar?"), ("s02.d", "força"))
    for k, (cue, nome) in enumerate(passos):
        x = 300 + k * 420
        E.foco(c, t, C[cue], 0.5, lambda a, x=x, k=k, nome=nome: (E.bola(c, x, 420, 70, a=a), centro(c, str(k + 1), x, 448, 80, "g", E.SOBRE, a),
                                                                  centro(c, nome, x, 580, 60, "g", TINTA, a)))
        if k:
            p = ep(t, C[cue], 0.4)
            if p > 0:
                M.arrow(c, x - 330, 420, x - 100, 420, TINTA2, p, 6, 20)
    E.frase(c, t, C["s02.e"], [("daí:", "i", 66), ("solubilidade", "g", 62, COR), ("e", "i", 66), ("ponto de ebulição", "g", 62, COR)], W / 2, 800, "center", 0.12)


# ---------------- questão 1 ----------------
def b_questao1(c, t, C, b):
    titulo_q(c, t, C["s03.a"], 1)
    Q.formula_em(c, t, C["s03.b"], "CH4", XE, 340, 100)
    E.foco(c, t, C["s03.b"] + 0.4, 0.4, lambda a: E.escreve(c, "metano: o gás natural", XE + 280, 330, 52, "i", TINTA2, a))
    Q.formula_em(c, t, C["s03.c"], "CHCl3", XE, 480, 100)
    E.foco(c, t, C["s03.c"] + 0.4, 0.4, lambda a: E.escreve(c, "clorofórmio: já foi solvente", XE + 370, 470, 52, "i", TINTA2, a))
    E.frase(c, t, C["s03.d"], ps("qual é a geometria? quem é polar?", "i", 62), XE, 680, passo=0.08)
    if t < C["s04"]:
        METANO(c, t, C["s03.b"] + 0.3, 1450, 400, 150)
        CHCL3(c, t, C["s03.c"] + 0.3, 1450, 780, 150)
    else:
        E.relogio(c, t, C["s04.a"], cx=1480, cy=470, r=200)


def b_resposta1(c, t, C, b):
    E.frase(c, t, C["s05"], ps("vamos lá", "i", 66, TINTA2), XE, 170)
    E.frase(c, t, C["s05.a"], ps("C: 4 ligações simples, sem par livre", "i", 56), XE, 280, passo=0.08)
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.pilula(c, "as duas: tetraédricas", XE + 290, 380, 52, "g", fundo=TINTA, a=a))
    METANO(c, t, C["s05"] + 0.3, 560, 690, 180)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: (centro(c, "ligantes iguais", 560, 940, 48, "b", TINTA, a), centro(c, "apolar", 560, 1010, 60, "g", TINTA, a)))
    CHCL3(c, t, C["s05"] + 0.6, 1350, 690, 180)
    for k in (1, 2, 3):
        ux, uy = DIRS["tetra"][k]
        n = math.hypot(ux, uy); ux, uy = ux / n, uy / n
        dipolo(c, t, C["s05.e"] + 0.2 * k, (1350 + ux * 45, 690 + uy * 45), (1350 + ux * 170, 690 + uy * 170))
    E.foco(c, t, C["s05.d"], 0.4, lambda a: centro(c, "um H e três Cl", 1350, 940, 48, "b", TINTA, a))
    E.foco(c, t, C["s05.e"] + 0.8, 0.4, lambda a: centro(c, "polar", 1350, 1010, 60, "g", COR, a))


# ---------------- questão 2 ----------------
def b_questao2(c, t, C, b):
    titulo_q(c, t, C["s06.a"], 2)
    E.frase(c, t, C["s06.b"], [("vitamina C:", "g", 60)] + ps("vários grupos OH", "i", 62), XE, 320, passo=0.1)
    E.frase(c, t, C["s06.b"] + 1.2, ps("(OH: oxigênio preso a hidrogênio)", "i", 50, TINTA2), XE, 400, passo=0.07)
    E.frase(c, t, C["s06.c"], [("vitamina A:", "g", 60)] + ps("quase só C e H, um OH só", "i", 62), XE, 520, passo=0.1)
    E.frase(c, t, C["s06.d"], [("1", "g", 56, COR)] + ps("qual se perde na água do cozimento?", "i", 58), XE, 680, passo=0.08)
    E.frase(c, t, C["s06.e"], [("2", "g", 56, COR)] + ps("por que a A vai melhor com gordura?", "i", 58), XE, 790, passo=0.08)
    if t < C["s07"]:
        Q.bastao(c, t, C["s06.c"] + 0.3, Q.zigzag(9), 1450, 560, 60, rotulos={8: "OH"})
        E.foco(c, t, C["s06.c"] + 0.8, 0.4, lambda a: centro(c, "vitamina A (resumida)", 1450, 680, 40, "i", TINTA2, a))
    else:
        E.relogio(c, t, C["s07.a"], cx=1500, cy=470, r=190)


def b_resposta2(c, t, C, b):
    E.frase(c, t, C["s08"], ps("vamos lá", "i", 66, TINTA2), XE, 170)
    E.frase(c, t, C["s08.a"], [("vitamina C:", "g", 60)] + ps("muitos OH,", "i", 62) + [("polar", "g", 60, COR)], XE, 290, passo=0.1)
    E.frase(c, t, C["s08.b"], ps("se dissolve na água do cozimento e vai embora", "i", 54, TINTA2), XE, 380, passo=0.07)
    E.foco(c, t, C["s08.b"] + 0.3, 0.5, lambda a: copo(c, 1500, 470, 260, 260, [(200, Q.AGUA)], a))
    for k in range(6):
        E.foco(c, t, C["s08.b"] + 0.6 + 0.1 * k, 0.4, lambda a, k=k: E.bola(c, 1420 + (k % 3) * 70, 400 - (k // 3) * 60, 12, "#F28C28", a))
    E.frase(c, t, C["s08.c"], [("vitamina A:", "g", 60)] + ps("1 OH para 20 carbonos", "i", 62), XE, 560, passo=0.1)
    E.frase(c, t, C["s08.d"], [("a parte", "i", 62), ("apolar", "g", 60), ("vence", "i", 62)], XE, 660, passo=0.1)
    E.frase(c, t, C["s08.e"], ps("se dissolve na gordura, também apolar", "i", 58), XE, 780, passo=0.08)
    E.foco(c, t, C["s08.e"] + 0.3, 0.5, lambda a: copo(c, 1500, 900, 260, 260, [(200, OLEO)], a))
    E.foco(c, t, C["s08.e"] + 1.4, 0.4, lambda a: E.pilula(c, "semelhante dissolve semelhante", XE + 400, 920, 50, "g", fundo=E.COR, a=a))


# ---------------- questão 3 ----------------
def b_questao3(c, t, C, b):
    titulo_q(c, t, C["s09.a"], 3)
    E.frase(c, t, C["s09.b"], [("etanol", "g", 60), ("e", "i", 62), ("éter dimetílico:", "g", 60)] + ps("mesma fórmula", "i", 62), XE, 320, passo=0.1)
    Q.formula_em(c, t, C["s09.b"] + 1.4, "C2H6O", XE + 300, 450, 100)
    Q.lewis(c, t, C["s09.c"], ETANOL, [(0, 1, 1), (1, 2, 1), (2, 3, 1)], 1440, 330, 150, 90, tl=[C["s09.c"]] * 4, cores={"O": COR})
    E.foco(c, t, C["s09.c"] + 0.4, 0.4, lambda a: centro(c, "etanol: O preso a H", 1440, 490, 46, "b", TINTA, a))
    Q.lewis(c, t, C["s09.d"], ETER, [(0, 1, 1), (1, 2, 1)], 1440, 640, 150, 90, tl=[C["s09.d"]] * 3, cores={"O": COR})
    E.foco(c, t, C["s09.d"] + 0.4, 0.4, lambda a: (centro(c, "éter: O entre dois carbonos", 1440, 790, 46, "b", TINTA, a), centro(c, "(sem os H dos carbonos)", 1440, 850, 38, "i", TINTA2, a)))
    E.frase(c, t, C["s09.e"], ps("qual ferve mais alto, e por quê?", "i", 62), XE, 700, passo=0.08)
    if t >= C["s10"]:
        E.relogio(c, t, C["s10.a"], cx=900, cy=790, r=100)


def b_resposta3(c, t, C, b):
    E.frase(c, t, C["s11"], ps("força primeiro", "i", 66, TINTA2), XE, 170)
    E.frase(c, t, C["s11.a"], [("etanol:", "g", 60)] + ps("H preso a O:", "i", 62) + [("ligação de hidrogênio", "g", 58, COR)], XE, 290, passo=0.1)
    E.frase(c, t, C["s11.b"], [("éter:", "g", 60)] + ps("nenhum H no O", "i", 62), XE, 400, passo=0.1)
    E.frase(c, t, C["s11.c"], ps("mas O com pares livres, em ângulo: polar.", "i", 54, TINTA2) + [("dipolo permanente", "g", 52)], XE, 490, passo=0.07)
    E.frase(c, t, C["s11.d"], ps("mesmo tamanho, força diferente", "i", 60), XE, 620, passo=0.08)
    Y = termometro(c, t, C["s11.d"], 360, 700, 1000, -50, 100, (-50, 0, 50, 100))
    ponto(c, t, C["s11.e"], Y, 400, PE["etanol"], "", F_H, rot="etanol: 78 °C")
    ponto(c, t, C["s11.e"] + 0.4, Y, 400, PE["eter"], "", F_P, rot="éter: −24 °C")


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], ps("o atalho", "i", 70, CLARO), W / 2, 150, "center", 0.12)
    E.frase(c, t, C["s12.a"], ps("fórmula igual não decide:", "i", 62, BR), W / 2, 280, "center", 0.1)
    E.frase(c, t, C["s12.b"], ps("olhe a estrutura e procure", "i", 60, CLARO), W / 2, 380, "center", 0.1)
    for k, f in enumerate(("O–H", "N–H", "H–F")):
        E.foco(c, t, C["s12.b"] + 1.4 + 0.3 * k, 0.4, lambda a, k=k, f=f: E.formula(c, f, 620 + 340 * k, 520, 100, "g", E.CLARO, a, "center"))
    E.frase(c, t, C["s12.c"], [("achou?", "i", 62, CLARO), ("ligação de hidrogênio,", "g", 58, BR)] + ps("ferve mais alto", "i", 62, CLARO), W / 2, 680, "center", 0.1)
    E.frase(c, t, C["s12.d"], ps("com o mesmo tamanho, quem decide é a força", "i", 54, CLARO), W / 2, 800, "center", 0.07)
    E.frase(c, t, C["s12.e"], [("não", "g", 54, ERRADO), ("compensa:", "i", 56, CLARO)] + ps("tamanhos muito diferentes", "i", 56, CLARO), W / 2, 930, "center", 0.08)


# ---------------- questão 4 ----------------
def b_questao4(c, t, C, b):
    titulo_q(c, t, C["s13.a"], 4)
    E.frase(c, t, C["s13.b"], ps("iodo num copo com água e óleo por cima; agite", "i", 54), XE, 320, passo=0.07)
    Q.formula_em(c, t, C["s13.b"] + 0.6, "I2", XE, 450, 100)
    E.frase(c, t, C["s13.c"], [("1", "g", 56, COR)] + ps("em qual camada a cor do iodo fica?", "i", 58), XE, 620, passo=0.08)
    E.frase(c, t, C["s13.d"], [("2", "g", 56, COR)] + ps("quem ferve mais alto:", "i", 58), XE, 730, passo=0.08)
    E.foco(c, t, C["s13.d"] + 1.2, 0.4, lambda a: (Q.formula(c, "I2", XE + 660, 735, 70, None, a), E.escreve(c, "ou", XE + 770, 730, 58, "i", TINTA, a),
                                                  Q.formula(c, "Br2", XE + 860, 735, 70, None, a)))
    if t < C["s14"]:
        mex = math.sin(prog(t, C["s13.b"] + 1.0, 1.2) * math.pi * 5) * (1 - prog(t, C["s13.b"] + 1.0, 1.2))
        E.foco(c, t, C["s13.b"] + 0.3, 0.5, lambda a: (c.save(), c.rotate(4 * mex, 1460, 700), copo(c, 1460, 900, 300, 440, [(190, Q.AGUA), (140, OLEO)], a), c.restore()))
    else:
        E.relogio(c, t, C["s14.a"], cx=1500, cy=470, r=190)


def b_resposta4(c, t, C, b):
    E.frase(c, t, C["s15"], ps("vamos lá", "i", 66, TINTA2), XE, 170)
    E.frase(c, t, C["s15.a"], [("iodo:", "g", 60)] + ps("átomos iguais,", "i", 62) + [("apolar", "g", 60)], XE, 290, passo=0.1)
    E.frase(c, t, C["s15.b"], ps("a cor vai para o óleo, também apolar", "i", 58), XE, 390, passo=0.08)
    k = ease_io(prog(t, C["s15.b"], 1.0))
    E.foco(c, t, C["s15.a"], 0.5, lambda a: copo(c, 1500, 560, 260, 380, [(160, Q.AGUA), (130, M.mix(OLEO, IODO, 0.6 * k))], a))
    E.frase(c, t, C["s15.c"], ps("para ferver: a mesma força,", "i", 58) + [("dipolo induzido", "g", 56)], XE, 520, passo=0.08)
    E.frase(c, t, C["s15.d"], ps("empate na força, desempate no tamanho: o iodo é maior", "i", 50, TINTA2), XE, 610, passo=0.06)
    Y = termometro(c, t, C["s15.d"], 360, 700, 1000, 0, 200, (0, 100, 200))
    ponto(c, t, C["s15.e"], Y, 400, PE["I2"], "I2", F_I)
    ponto(c, t, C["s15.e"] + 0.4, Y, 400, PE["Br2"], "Br2", F_I)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s16.a", "estrutura", "forma"), ("s16.b", "forma", "polaridade"), ("s16.c", "polaridade", "solubilidade e força"), ("s16.d", "força", "ponto de ebulição"))
        for i, (k, de, para) in enumerate(itens):
            y = 340 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 50, a=a), centro(c, str(i + 1), 260, y - 2, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [("da", "i", 66), (de, "g", 62), ("sai", "i", 66), (para, "g", 62, COR)], 350, y, passo=0.12)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], ps("fim da trilha de ligações", "i", 66, TINTA2), XE, 220, passo=0.1)
    E.frase(c, t, C["s17.a"], [("próxima", "i", 80), ("aula:", "i", 80)], XE, 360)
    E.frase(c, t, C["s17.a"] + 0.6, [("as", "i", 100), ("reações", "g", 100, COR)], XE, 500)
    E.frase(c, t, C["s17.b"], ps("ler uma equação; a massa se conserva", "i", 58), XE, 630, passo=0.08)
    Q.equacao(c, t, C["s17.b"] + 0.8, "2 H2 + O2 -> 2 H2O", 640, 800, 80)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s17.c"] + 0.2, 0.4))
    E.frase(c, t, C["s17.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4,
              resposta4=b_resposta4, fim=b_fim)
