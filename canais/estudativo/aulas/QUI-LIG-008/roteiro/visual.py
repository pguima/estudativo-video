"""Visual — Estudativo · QUI-LIG-008: semelhante dissolve semelhante.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), a da trilha (QUI-LIG-001) e a do módulo (QUI-LIG-006). Peças próprias:
COPO DE CAMADAS (copo()): vidro em Q.VIDRO com as camadas que não se misturam, de baixo para cima; água = Q.AGUA, óleo =
amarelo-ouro, gasolina = âmbar claro, iodo dissolvido = violeta. ÁGUA EM VOLTA DO ÍON (hidrata()): moléculas de água
viradas para o íon, o oxigênio (δ−) para o Na⁺ e os hidrogênios (δ+) para o Cl⁻. Atração entre moléculas = tracejado
turquesa. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ligações Químicas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-LIG-008_semelhante_dissolve_semelhante.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("dissolver", "regra", "exemplos", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OLEO, GASOLINA, IODO, MEL = "#F2C14E", "#F6DFA0", "#7A3FA0", "#D98E04"
assert 65 - 50 == 15 and 50 - 15 == 35


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


def copo(c, cx, yb, w, h, camadas, a=1.0, marcas=False, rotulos=True):
    """copo de vidro com camadas [(altura px, cor, rótulo)] empilhadas de baixo para cima"""
    if a <= 0:
        return
    x0 = cx - w / 2
    y = yb
    for hh, cor, rot in camadas:
        y2 = y - hh
        pp = skia.Paint(AntiAlias=True)
        pp.setShader(skia.GradientShader.MakeLinear([skia.Point(0, y2), skia.Point(0, y)], [M.hexc(M.mix(cor, "#FFFFFF", 0.15), 0.92 * a), M.hexc(cor, 0.95 * a)], [0, 1]))
        c.drawRect(skia.Rect.MakeLTRB(x0 + 4, y2, x0 + w - 4, y - 4 if y == yb else y), pp)
        if rotulos and rot:
            E.escreve(c, rot, cx + w / 2 + 24, (y + y2) / 2 + 16, 44, "b", TINTA, a)
        y = y2
    pth = skia.Path()
    pth.moveTo(x0 - 6, yb - h - 10); pth.lineTo(x0, yb - h); pth.lineTo(x0, yb - 16); pth.quadTo(x0, yb, x0 + 16, yb)
    pth.lineTo(x0 + w - 16, yb); pth.quadTo(x0 + w, yb, x0 + w, yb - 16); pth.lineTo(x0 + w, yb - h); pth.lineTo(x0 + w + 6, yb - h - 10)
    pv = M.paint(Q.VIDRO, a, stroke=5); pv.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(pth, pv)
    M.line(c, x0 + w * 0.12, yb - h * 0.85, x0 + w * 0.12, yb - h * 0.35, BR, 0.7 * a, 6)
    if marcas:
        for k in range(1, 10):
            yy = yb - h * k / 10
            M.line(c, x0 + w - 30 + (12 if k % 2 else 0), yy, x0 + w - 4, yy, Q.VIDRO, 0.7 * a, 3)


def agua_mol(c, cx, cy, esc, alvo=None, giro=0.0, a=1.0):
    """molécula de água; com alvo, o O aponta para o alvo (sinal +1) ou os H apontam (sinal −1)"""
    if alvo is not None:
        (ax, ay), sinal = alvo
        dx, dy = ax - cx, ay - cy
        n = math.hypot(dx, dy) or 1
        dx, dy = dx / n * sinal, dy / n * sinal
        giro = math.degrees(math.atan2(dx, -dy))
    Q.molecula_desenho(c, "H2O", cx, cy, esc, a, giro=giro, rotulos=False)


def ion(c, cx, cy, r, el, s, a=1.0):
    if a <= 0:
        return
    Q.atomo(c, cx, cy, r, el, a, rotulo=False)
    Q.formula(c, s, cx, cy + r * 0.3, r * 0.82, BR, a, "center")


def hidrata(c, t, t0, cx, cy, el, s, r, n=6, R=130, esc=42, sinal=1):
    q = ease_back(prog(t, t0, 0.5))
    if q > 0:
        ion(c, cx, cy, r * q, el, s)
    for k in range(n):
        g = math.tau * k / n + 0.3
        px, py = cx + R * math.cos(g), cy + R * math.sin(g)
        E.foco(c, t, t0 + 0.3 + 0.12 * k, 0.4, lambda a, px=px, py=py: agua_mol(c, px, py, esc, ((cx, cy), sinal), a=a))


def tracejado(c, A, B, a=1.0, larg=4):
    M.line(c, *A, *B, E.COR, a, larg, dash=[10, 9])


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("óleo", "g", 66), ("e", "i", 70), ("água", "g", 66)] + ps("não se misturam", "i", 70), XE, 200, passo=0.12)
        mex = 0.0
        if t >= C["s01.b"]:
            u = prog(t, C["s01.b"], 1.6)
            mex = math.sin(u * math.pi * 6) * (1 - u)
        E.foco(c, t, C["s01.a"] + 0.3, 0.5, lambda a: (c.save(), c.rotate(4 * mex, 520, 700),
                                                       copo(c, 520, 900, 300, 420, [(200, Q.AGUA, ""), (130, OLEO, "")], a), c.restore()))
        E.foco(c, t, C["s01.a"] + 0.6, 0.4, lambda a: (centro(c, "óleo", 520, 640, 46, "b", TINTA, a), centro(c, "água", 520, 820, 46, "b", TINTA, a)))
        E.frase(c, t, C["s01.b"] + 0.4, ps("chacoalhe: as camadas voltam", "i", 52, TINTA2), 280, 990, passo=0.08)
        E.frase(c, t, C["s01.c"], [("óleo", "g", 60), ("some na", "i", 62), ("gasolina", "g", 60, COR)], 1050, 420, passo=0.12)
        E.foco(c, t, C["s01.c"] + 0.4, 0.5, lambda a: copo(c, 1200, 880, 220, 280, [(220, M.mix(GASOLINA, OLEO, 0.4), "")], a))
        E.frase(c, t, C["s01.d"], [("e", "i", 62), ("sal", "g", 60), ("some na", "i", 62), ("água", "g", 60, COR)], 1050, 520, passo=0.12)
        E.foco(c, t, C["s01.d"] + 0.4, 0.5, lambda a: copo(c, 1600, 880, 220, 280, [(220, Q.AGUA, "")], a))
        E.foco(c, t, C["s01.d"], 0.4, lambda a: (centro(c, "gasolina + óleo", 1200, 940, 42, "b", TINTA, a) if t >= C["s01.c"] + 0.4 else None,
                                                centro(c, "água + sal", 1600, 940, 42, "b", TINTA, a)))
        E.frase(c, t, C["s01.e"], ps("uma regra de três palavras", "i", 62), 1050, 1040, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1660, 560, 210 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    for k, s_ in enumerate(("sal", "álcool", "óleo", "iodo")):
        pilula_em(c, t, C["s02.b"] + 0.3 * k, s_, XE + 90 + 230 * k, 420, 56, TINTA)
    E.frase(c, t, C["s02.c"], [("na", "i", 72), ("água", "g", 70, COR), ("ou", "i", 72), ("na", "i", 72), ("gasolina?", "g", 70, COR)], XE, 580, passo=0.12)
    E.frase(c, t, C["s02.d"], [("+", "g", 66, COR), ("atalho", "g", 66, COR)] + ps("pela fórmula", "i", 70), XE, 720, passo=0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 66, TINTA2), XE, 190, passo=0.12)
    E.frase(c, t, C["s03.a"], [("a polaridade", "g", 70, COR)], XE, 320)
    E.frase(c, t, C["s03.b"], [("água:", "g", 60), ("polar", "i", 64)], XE, 440, passo=0.1)
    E.foco(c, t, C["s03.b"] + 0.3, 0.5, lambda a: agua_mol(c, 1300, 420, 120, giro=0, a=a))
    E.foco(c, t, C["s03.b"] + 1.0, 0.4, lambda a: (E.formula(c, "δ^{−}", 1300, 300, 60, "g", Q.ELETRON, a, "center"),
                                                  E.formula(c, "δ^{+}", 1170, 560, 56, "g", TINTA, a, "center"), E.formula(c, "δ^{+}", 1430, 560, 56, "g", TINTA, a, "center")))
    E.frase(c, t, C["s03.c"], [("sal:", "g", 60), ("iônico,", "i", 64)] + ps("presos num cristal", "i", 64), XE, 700, passo=0.1)
    for k in range(6):
        el, s_ = ("Na", "Na^+") if k % 2 == 0 else ("Cl", "Cl^-")
        E.foco(c, t, C["s03.c"] + 0.5 + 0.08 * k, 0.4, lambda a, k=k, el=el, s_=s_: ion(c, 1150 + (k % 3) * 90, 700 + (k // 3) * 90, 28 if el == "Na" else 38, el, s_, a))


# ---------------- dissolver (s04–s05) ----------------
def b_dissolver(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], [("dissolver", "g", 80, COR)], XE, 220)
            E.frase(c, t, C["s04.a"] + 0.6, ps("espalhar as partículas no meio das outras", "i", 58), XE, 320, passo=0.08)
            E.foco(c, t, C["s04.a"] + 0.4, 0.5, lambda a: copo(c, 1600, 900, 300, 440, [(330, Q.AGUA, "")], a))
            for k in range(14):
                q = ease_io(prog(t, C["s04.a"] + 1.0, 2.0))
                x0, y0 = 1600 + (k % 4 - 1.5) * 30, 520 + (k // 4) * 30
                x1, y1 = 1480 + 240 * ((k * 0.37) % 1), 620 + 250 * ((k * 0.61) % 1)
                E.bola(c, lerp(x0, x1, q) + 6 * math.sin(t * 2 + k), lerp(y0, y1, q), 12, E.COR, ep(t, C["s04.a"] + 0.6, 0.4))
            E.frase(c, t, C["s04.b"], [("soluto", "g", 66), ("=", "g", 66, TINTA2)] + ps("quem se dissolve", "i", 66), XE, 560, passo=0.1)
            E.frase(c, t, C["s04.c"], [("solvente", "g", 66), ("=", "g", 66, TINTA2)] + ps("quem dissolve (o que tem mais)", "i", 66), XE, 680, passo=0.1)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    E.frase(c, t, C["s05.a"], [("gasolina", "g", 76, COR)], XE, 220)
    E.frase(c, t, C["s05.a"] + 0.5, ps("(sem o álcool): só carbono e hidrogênio", "i", 56), XE, 310, passo=0.08)
    Q.bastao(c, t, C["s05.a"] + 0.6, Q.zigzag(8), 1380, 330, 110, numeros=None)
    Q.formula_em(c, t, C["s05.a"] + 1.4, "C8H18", 1380, 470, 70, align="center")
    E.frase(c, t, C["s05.b"], ps("C e H: eletronegatividades parecidas", "i", 58), XE, 600, passo=0.08)
    E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "apolar", XE + 120, 700, 60, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s05.d"], [("óleo de cozinha:", "g", 60)] + ps("quase todo C e H,", "i", 62) + [("apolar", "g", 60)], XE, 860, passo=0.1)


# ---------------- regra (s06–s08) ----------------
def b_regra(c, t, C, b):
    if t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06.a"], [("semelhante", "g", 110, COR)], W / 2, 280, "center")
            E.frase(c, t, C["s06.a"] + 0.5, [("dissolve", "i", 110), ("semelhante", "g", 110, COR)], W / 2, 410, "center", 0.2)
            E.frase(c, t, C["s06.b"], [("polar", "g", 60), ("dissolve", "i", 62), ("polar", "g", 60)] + ps("e muitos iônicos", "i", 62), W / 2, 560, "center", 0.1)
            E.frase(c, t, C["s06.c"], [("apolar", "g", 60), ("dissolve", "i", 62), ("apolar", "g", 60)], W / 2, 660, "center", 0.1)
            E.foco(c, t, C["s06.d"], 0.5, lambda a: copo(c, 620, 1000, 240, 240, [(200, Q.AGUA, "")], a))
            E.foco(c, t, C["s06.e"], 0.5, lambda a: copo(c, 1300, 1000, 240, 240, [(200, M.mix(GASOLINA, OLEO, 0.4), "")], a))
            E.foco(c, t, C["s06.d"] + 0.3, 0.4, lambda a: E.escreve(c, "água + sal", 780, 900, 46, "b", TINTA, a))
            E.foco(c, t, C["s06.e"] + 0.3, 0.4, lambda a: E.escreve(c, "gasolina + óleo", 1460, 900, 46, "b", TINTA, a))
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    if t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07"], ps("por quê?", "i", 70, TINTA2), XE, 190)
            # águas que se atraem pelas pontas
            pos = [(300, 420), (480, 360), (420, 560), (620, 520)]
            for k, (x, y) in enumerate(pos):
                E.foco(c, t, C["s07.a"] + 0.1 * k, 0.4, lambda a, x=x, y=y, k=k: agua_mol(c, x, y, 50, giro=40 * k + 10, a=a))
            if t >= C["s07.a"] + 0.6:
                q = ep(t, C["s07.a"] + 0.6, 0.4)
                for A, B in (((340, 400), (450, 380)), ((420, 520), (470, 400)), ((470, 560), (580, 520))):
                    tracejado(c, A, B, q)
            E.frase(c, t, C["s07.a"] + 0.4, ps("a água se atrai pelas pontas: + com −", "i", 50, TINTA2), XE, 700, passo=0.06)
            E.frase(c, t, C["s07.b"], ps("para entrar, é preciso oferecer atração", "i", 50), XE, 790, passo=0.06)
            hidrata(c, t, C["s07.d"], 1150, 540, "Na", "Na^+", 44, 6, 130, 40, 1)
            hidrata(c, t, C["s07.e"], 1600, 540, "Cl", "Cl^-", 56, 6, 150, 40, -1)
            E.foco(c, t, C["s07.d"] + 0.8, 0.4, lambda a: centro(c, "O (δ−) para o Na⁺", 1150, 760, 42, "b", TINTA, a))
            E.foco(c, t, C["s07.e"] + 0.8, 0.4, lambda a: centro(c, "H (δ+) para o Cl⁻", 1600, 760, 42, "b", TINTA, a))
            E.frase(c, t, C["s07.e"] + 1.2, ps("os íons se soltam do cristal", "i", 56, TINTA2), 1380, 900, "center", 0.08)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    E.frase(c, t, C["s08.a"], [("óleo:", "g", 64)] + ps("não tem polos, não oferece nada", "i", 64), XE, 200, passo=0.1)
    sep = ease_io(prog(t, C["s08.c"], 1.6))
    for k in range(10):
        x, y = 380 + (k % 5) * 110, 520 + (k // 5) * 110
        E.foco(c, t, C["s08.b"] + 0.05 * k, 0.4, lambda a, x=x, y=y, k=k: agua_mol(c, x, y + 160 * sep, 40, giro=35 * k, a=a))
    for k in range(5):
        E.foco(c, t, C["s08.a"] + 0.5, 0.4, lambda a, k=k: E.bola(c, 400 + (k % 3) * 200, lerp(570, 400, sep) + (k // 3) * 70, 30, OLEO, a))
    E.frase(c, t, C["s08.b"], ps("a água continua presa a si mesma", "i", 54, TINTA2), XE, 300, passo=0.08)
    E.foco(c, t, C["s08.d"], 0.5, lambda a: E.pilula(c, "duas camadas", 600, 980, 56, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s08.e"], [("sal na gasolina?", "g", 60)], 1150, 440)
    E.frase(c, t, C["s08.e"] + 1.0, ps("fica inteiro: sem polos", "i", 56), 1150, 530, passo=0.08)
    E.frase(c, t, C["s08.e"] + 1.6, ps("para soltar os íons", "i", 56), 1150, 600, passo=0.08)
    E.foco(c, t, C["s08.e"] + 0.5, 0.5, lambda a: (copo(c, 1450, 1000, 300, 320, [(260, GASOLINA, "")], a),
                                                   [ion(c, 1400 + (k % 3) * 40 - 20, 960 - (k // 3) * 40, 16 if k % 2 == 0 else 21, "Na" if k % 2 == 0 else "Cl", "", a) for k in range(6)]))


# ---------------- exemplos (s09–s10) ----------------
def b_exemplos(c, t, C, b):
    if t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09.a"], [("iodo", "g", 76, IODO)], XE, 220)
            Q.formula_em(c, t, C["s09.a"] + 0.3, "I2", XE + 250, 222, 90)
            Q.molecula(c, t, C["s09.a"] + 0.4, dict(atomos=[("I", -0.7, 0), ("I", 0.7, 0)], ligacoes=[(0, 1, 1)]), XE + 600, 200, 90)
            E.frase(c, t, C["s09.a"] + 1.0, ps("átomos iguais: apolar", "i", 58), XE, 320, passo=0.08)
            E.foco(c, t, C["s09.b"], 0.5, lambda a: copo(c, 620, 900, 300, 380, [(300, M.mix(Q.AGUA, IODO, 0.12), "")], a))
            E.foco(c, t, C["s09.b"], 0.4, lambda a: (centro(c, "água", 620, 980, 50, "b", TINTA, a), centro(c, "quase não dissolve", 620, 1040, 44, "i", TINTA2, a)))
            E.foco(c, t, C["s09.c"], 0.5, lambda a: copo(c, 1300, 900, 300, 380, [(300, M.mix(GASOLINA, IODO, 0.6), "")], a))
            E.foco(c, t, C["s09.c"], 0.4, lambda a: (centro(c, "gasolina", 1300, 980, 50, "b", TINTA, a), centro(c, "dissolve bem", 1300, 1040, 44, "i", CERTO, a)))
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    E.frase(c, t, C["s10"], [("etanol,", "g", 76, COR)] + ps("o álcool comum", "i", 72), XE, 210, passo=0.12)
    E.frase(c, t, C["s10.a"], ps("se mistura com os dois", "i", 60), XE, 300, passo=0.08)
    pts = Q.molecula(c, t, C["s10"] + 0.3, "C2H6O", 1150, 560, 140, passo=0.08)
    if t >= C["s10.b"]:
        q = ep(t, C["s10.b"], 0.4)
        ox, oy = (pts[2][0] + pts[8][0]) / 2, (pts[2][1] + pts[8][1]) / 2
        c.drawCircle(ox, oy, 110, M.paint(E.COR, q, stroke=6))
    if t >= C["s10.c"]:
        q = ep(t, C["s10.c"], 0.4)
        ii = [0, 1, 3, 4, 5, 6, 7]
        xs, ys = [pts[i][0] for i in ii], [pts[i][1] for i in ii]
        E.caixa_pontilhada(c, min(xs) - 50, min(ys) - 50, max(xs) - min(xs) + 100, max(ys) - min(ys) + 100, q, TINTA2, prog_=q)
    E.foco(c, t, C["s10.b"] + 0.3, 0.4, lambda a: centro(c, "OH: polar", 1500, 820, 50, "g", COR, a))
    E.foco(c, t, C["s10.c"] + 0.3, 0.4, lambda a: centro(c, "C e H: apolar", 860, 880, 50, "g", TINTA, a))
    E.frase(c, t, C["s10.d"], [("OH", "g", 56, COR), ("→", "g", 56, TINTA2), ("água", "i", 60)], XE, 520, passo=0.1)
    E.frase(c, t, C["s10.e"], [("C e H", "g", 56), ("→", "g", 56, TINTA2), ("gasolina", "i", 60)], XE, 620, passo=0.1)
    pilula_em(c, t, C["s10.f"], "a gasolina do Brasil já leva etanol", W / 2, 1010, 48, E.COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("o óleo não se mistura porque é grosso?", "i", 60), XE + 460, 190, passo=0.08)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: copo(c, 560, 820, 300, 380, [(300, M.mix(Q.AGUA, MEL, 0.35), "")], a))
    E.foco(c, t, C["s11.b"] + 0.3, 0.4, lambda a: (centro(c, "mel: grosso", 560, 900, 54, "b", TINTA, a), centro(c, "dissolve na água", 560, 965, 48, "i", CERTO, a)))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: copo(c, 1350, 820, 300, 380, [(170, Q.AGUA, ""), (130, GASOLINA, "")], a))
    E.foco(c, t, C["s11.c"] + 0.3, 0.4, lambda a: (centro(c, "gasolina: fininha", 1350, 900, 54, "b", TINTA, a), centro(c, "não dissolve na água", 1350, 965, 48, "i", ERRADO, a)))
    E.frase(c, t, C["s11.d"], ps("quem decide:", "i", 62) + [("a polaridade", "g", 60, COR)], W / 2, 1050, "center", 0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], ps("o atalho pela fórmula", "i", 70, CLARO), W / 2, 150, "center", 0.12)
    E.frase(c, t, C["s12.a"], ps("só C e H, ou átomos iguais?", "i", 60, BR) + [("→ gasolina", "g", 58, E.CLARO)], XE, 290, passo=0.08)
    for k, f in enumerate(("C8H18", "I2")):
        Q.formula_em(c, t, C["s12.a"] + 1.6 + 0.3 * k, f, XE + 120 + 320 * k, 390, 70, escuro=True)
    E.frase(c, t, C["s12.b"], ps("iônico ou tem OH?", "i", 60, BR) + [("→ água", "g", 58, E.CLARO)] + ps("(em geral)", "i", 52, CLARO), XE, 520, passo=0.08)
    for k, f in enumerate(("NaCl", "C2H5OH")):
        Q.formula_em(c, t, C["s12.b"] + 1.4 + 0.3 * k, f, XE + 120 + 320 * k, 620, 70, escuro=True)
    E.frase(c, t, C["s12.c"], ps("C–H quase não tem polo; O–H é bem polar", "i", 54, CLARO), XE, 760, passo=0.06)
    E.frase(c, t, C["s13.a"], [("não", "g", 56, ERRADO), ("compensa:", "i", 58, CLARO)] + ps("muitos carbonos e um OH só", "i", 58, CLARO), XE, 890, passo=0.08)
    E.frase(c, t, C["s13.b"], ps("a parte apolar vence: quase não dissolve na água", "i", 52, BR), XE, 980, passo=0.06)
    Q.bastao(c, t, C["s13.a"] + 1.0, Q.zigzag(9), 1450, 560, 70, rotulos={8: "OH"}, escuro=True)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s14.a"], ps("proveta: tubo de vidro com marcas de volume", "i", 52, TINTA2), XE, 270, passo=0.06)
    E.frase(c, t, C["s14.b"], [("50 mL", "g", 60), ("de gasolina", "i", 62), ("+", "g", 60, TINTA2), ("50 mL", "g", 60), ("de água", "i", 62)], XE, 400, passo=0.1)
    E.frase(c, t, C["s14.c"], ps("no fim, a água tem", "i", 60) + [("65 mL", "g", 60, COR)], XE, 520, passo=0.1)
    E.frase(c, t, C["s14.d"], [("1", "g", 56, COR)] + ps("por que a água aumentou?", "i", 60), XE, 680, passo=0.08)
    E.frase(c, t, C["s14.e"], [("2", "g", 56, COR)] + ps("quantos mL de etanol havia?", "i", 60), XE, 790, passo=0.08)
    if t < C["s15"]:
        fim = t >= C["s14.c"]
        cam = [(195, Q.AGUA, "65 mL"), (105, GASOLINA, "35 mL")] if fim else [(150, Q.AGUA, "50 mL"), (150, GASOLINA, "50 mL")]
        E.foco(c, t, C["s14.b"], 0.5, lambda a: copo(c, 1450, 940, 170, 640, cam, a, marcas=True))
    else:
        E.relogio(c, t, C["s15.a"], cx=1480, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s16"], ps("vamos lá", "i", 66, TINTA2), XE, 170)
    E.frase(c, t, C["s16.a"], [("água", "g", 60), ("e", "i", 62), ("gasolina:", "g", 60)] + ps("polar e apolar, não se misturam", "i", 60), XE, 290, passo=0.08)
    E.frase(c, t, C["s16.b"], ps("o etanol se dá bem com a água", "i", 60), XE, 400, passo=0.08)
    E.frase(c, t, C["s16.c"], ps("e passa para a camada de água", "i", 60, TINTA2), XE, 490, passo=0.08)
    k = ease_io(prog(t, C["s16.c"], 1.6))
    cam = [(lerp(150, 195, k), Q.AGUA, ""), (lerp(150, 105, k), GASOLINA, "")]
    copo(c, 1450, 940, 170, 640, cam, 1.0, marcas=True)
    for j in range(8):
        x = 1420 + (j % 4) * 22
        y = lerp(720 - (j // 4) * 30, 840 - (j // 4) * 30, k)
        E.bola(c, x, y, 9, E.COR, ep(t, C["s16.b"], 0.4))
    E.foco(c, t, C["s16.d"], 0.4, lambda a: E.formula(c, "65 − 50 =", XE + 400, 700, 90, "g", TINTA2, a, "right"))
    E.foco(c, t, C["s16.e"], 0.5, lambda a: (E.bola(c, XE + 560, 670, 80, CERTO, a), centro(c, "15", XE + 560, 700, 80, "g", BR, a)))
    E.foco(c, t, C["s16.e"] + 0.3, 0.4, lambda a: E.escreve(c, "mL de etanol", XE + 660, 700, 60, "b", TINTA, a))
    E.frase(c, t, C["s16.e"] + 1.2, ps("e a gasolina encolheu para 35 mL", "i", 54, TINTA2), XE, 860, passo=0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s17.a", [("semelhante", "g", 62)] + ps("dissolve", "i", 64) + [("semelhante", "g", 62)]),
                 ("s17.b", [("polar e iônico", "g", 62)] + ps("vão com a água", "i", 64)),
                 ("s17.c", [("apolar", "g", 62)] + ps("vai com a gasolina", "i", 64)),
                 ("s17.d", [("etanol:", "g", 62)] + ps("um pedaço de cada, vai com os dois", "i", 64)))
        for i, (k, partes) in enumerate(itens):
            y = 340 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 50, a=a), centro(c, str(i + 1), 260, y - 2, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 350, y, passo=0.12)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 240)
    E.frase(c, t, C["s18.a"], [("três forças", "g", 100, COR)], XE, 390)
    E.frase(c, t, C["s18.a"] + 0.5, [("entre", "i", 90), ("moléculas", "g", 90, COR)], XE, 500)
    for k, s_ in enumerate(("dipolo induzido", "dipolo permanente", "ligação de hidrogênio")):
        pilula_em(c, t, C["s18.b"] + 0.5 * k, s_, XE + 250, 640 + k * 100, 50, TINTA if k < 2 else E.COR)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s18.c"] + 0.2, 0.4))
    E.frase(c, t, C["s18.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, dissolver=b_dissolver, regra=b_regra, exemplos=b_exemplos, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
