"""Visual — Estudativo · MAT-ARE-010: razão entre áreas de figuras semelhantes (lados × k, área × k²; +20% no lado = +44% na área).
Linguagem da trilha (MAT-ARE-001): figuras em tinta com o miolo claro da cor da matéria; a figura ORIGINAL em COR clara e a
AMPLIADA por cima, com as medidas novas em COR; a altura tracejada em TINTA2 com o quadradinho no pé. ÁREA = cópias: o triângulo
grande se divide nas nove cópias do pequeno (grade de paralelas aos lados). No quadrado que cresce, as duas faixas novas em verde
(CERTO) e o cantinho que todo mundo esquece na cor da matéria, piscando. Fatores na grotesca ("× 1,2"); k aparece como "k";
resposta na esfera; vermelho é erro; palco escuro só no atalho.
Peças locais: tri() (triângulo de base b e altura h, escala k a partir de um canto), nove() (as nove cópias), quadrado_cresce(),
faixas(), logo() (o logotipo triangular na parede), lata() (lata de tinta com o volume).
Todo instante vem de C[...] (marcadores do roteiro); entre() reparte o tempo entre dois marcadores."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Áreas e Perímetros")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ARE-010_razao_entre_areas_de_figuras_semelhantes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("triangulo", "regra", "porcento", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
assert 4 * 3 / 2 == 6 and 12 * 9 / 2 == 54 and 54 == 9 * 6 and 3 ** 2 == 9 and 4 * 3 == 12 and 3 * 3 == 9
assert 10 * 10 == 100 and 12 * 12 == 144 and 144 - 100 == 44 and abs(1.2 ** 2 - 1.44) < 1e-9
assert 10 * 2 + 10 * 2 + 2 * 2 == 44 and abs(40 * 1.2 - 48) < 1e-9 and 20 + 20 + 20 * 20 / 100 == 44
assert -20 - 20 + (-20) * (-20) / 100 == -36 and abs(0.8 ** 2 - 0.64) < 1e-9
assert 13 * 13 == 169 and abs(1.3 ** 2 - 1.69) < 1e-9 and round(200 * 1.69) == 338 and 30 + 30 + 30 * 30 / 100 == 69


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")))


def entre(C, k1, k2, f):
    return lerp(C[k1], C[k2], f)


def poli(c, pts, cor, alfa, a=1.0, borda=TINTA, larg=6):
    if a <= 0:
        return
    path = skia.Path(); path.addPoly(pts, True)
    if alfa > 0:
        c.drawPath(path, M.paint(cor, alfa * a))
    if borda:
        p = M.paint(borda, a, stroke=larg); p.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(path, p)


# o triângulo: base 4, altura 3, o topo a 1 da ponta esquerda (40 px por unidade)
U = 52


def tri(B, k):
    """vértices (B, C, A) do triângulo de base 4k e altura 3k, com B embaixo à esquerda"""
    return B, (B[0] + 4 * k * U, B[1]), (B[0] + 1 * k * U, B[1] - 3 * k * U)


def altura(c, t, t0, A, B, rot=None, cor=COR, size=54, a=1.0):
    if t < t0 or a <= 0:
        return
    pe = (A[0], B[1])
    M.line(c, *A, *pe, TINTA2, a, 5, dash=E.TRACO, progress=ease_io(prog(t, t0, 0.5)))
    E.angulo(c, t, t0 + 0.3, pe, A, (pe[0] + 40, pe[1]), r=30, reto=True, preenche=0.0)
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda f: E.formula(c, rot, pe[0] + 18, (A[1] + pe[1]) / 2 + 20, size, "g", cor, f * a, "left"))


def nove(c, B, k, p, a=1.0):
    """as nove cópias do triângulo pequeno dentro do grande (k = 3): paralelas aos três lados, nas terças partes"""
    if p <= 0 or a <= 0:
        return
    B_, C_, A_ = tri(B, k)
    for i in (1, 2):
        f = i / 3
        # paralela à base
        P, Q = (lerp(B_[0], A_[0], f), lerp(B_[1], A_[1], f)), (lerp(C_[0], A_[0], f), lerp(C_[1], A_[1], f))
        M.line(c, *P, *Q, TINTA, a, 4, progress=p)
        # paralela ao lado BA
        P, Q = (lerp(B_[0], C_[0], f), lerp(B_[1], C_[1], f)), (lerp(A_[0], C_[0], f), lerp(A_[1], C_[1], f))
        M.line(c, *P, *Q, TINTA, a, 4, progress=p)
        # paralela ao lado CA
        P, Q = (lerp(C_[0], B_[0], f), lerp(C_[1], B_[1], f)), (lerp(A_[0], B_[0], f), lerp(A_[1], B_[1], f))
        M.line(c, *P, *Q, TINTA, a, 4, progress=p)


def nove_numeros(c, t, t0, B, k, a=1.0):
    """numera as nove cópias, uma a uma"""
    B_, C_, A_ = tri(B, k)
    s = 1 / 3
    centros = []
    for j in range(3):          # faixa de baixo para cima
        for i in range(3 - j):  # em pé
            p0 = (B_[0] + (i * 4 + j * 1) * U, B_[1] - j * 3 * U)
            P = [p0, (p0[0] + 4 * U, p0[1]), (p0[0] + U, p0[1] - 3 * U)]
            centros.append(((P[0][0] + P[1][0] + P[2][0]) / 3, (P[0][1] + P[1][1] + P[2][1]) / 3))
        for i in range(2 - j):  # de cabeça para baixo
            p0 = (B_[0] + (i * 4 + j * 1 + 4) * U, B_[1] - j * 3 * U)
            P = [p0, (p0[0] - 3 * U, p0[1] - 3 * U), (p0[0] + U, p0[1] - 3 * U)]
            centros.append(((P[0][0] + P[1][0] + P[2][0]) / 3, (P[0][1] + P[1][1] + P[2][1]) / 3))
    assert len(centros) == 9
    for n, g in enumerate(centros):
        E.foco(c, t, t0 + 0.18 * n, 0.3, lambda f, g=g, n=n: centro(c, str(n + 1), g[0], g[1] + 18, 46, "g", COR, f * a))


def quadrado(c, x, yb, L, cor=E.COR, alfa=0.15, a=1.0, larg=6):
    """quadrado de lado L px com o canto de baixo à esquerda em (x, yb)"""
    poli(c, [(x, yb), (x + L, yb), (x + L, yb - L), (x, yb - L)], cor, alfa, a, TINTA, larg)


def faixas(c, t, x, yb, L, d, tdir, tcima, tcanto, pisca=None, rot=True):
    """as faixas que o quadrado de lado L ganha ao crescer d: direita (L × d), em cima (L × d) e o cantinho d × d"""
    for ti, R, s in ((tdir, (x + L, yb - L, d, L), "10 × 2"), (tcima, (x, yb - L - d, L, d), "10 × 2")):
        if ti is not None and t >= ti:
            k = ep(t, ti, 0.5)
            c.drawRect(skia.Rect.MakeXYWH(*R), M.paint(CERTO, 0.45 * k))
            c.drawRect(skia.Rect.MakeXYWH(*R), M.paint(TINTA, k, stroke=4))
            if rot:
                cx, cy = R[0] + R[2] / 2, R[1] + R[3] / 2
                if R[2] < R[3]:
                    c.save(); c.translate(cx, cy); c.rotate(-90)
                    centro(c, s, 0, 16, 44, "g", TINTA, k)
                    c.restore()
                else:
                    centro(c, s, cx, cy + 16, 44, "g", TINTA, k)
    if tcanto is not None and t >= tcanto:
        k = ep(t, tcanto, 0.4)
        bl = 1.0
        if pisca is not None and t >= pisca:
            bl = 0.55 + 0.45 * math.cos((t - pisca) * 7)
        R = (x + L, yb - L - d, d, d)
        c.drawRect(skia.Rect.MakeXYWH(*R), M.paint(E.COR, 0.85 * k * bl))
        c.drawRect(skia.Rect.MakeXYWH(*R), M.paint(TINTA, k, stroke=4))


def logo(c, cx, by, lado, a=1.0, cor=None, tracejado=False):
    """o logotipo: triângulo equilátero com um círculo dentro, base em by"""
    if a <= 0:
        return
    h = lado * math.sqrt(3) / 2
    pts = [(cx - lado / 2, by), (cx + lado / 2, by), (cx, by - h)]
    if tracejado:
        path = skia.Path(); path.addPoly(pts, True)
        p = M.paint(TINTA2, a, stroke=4); p.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
        c.drawPath(path, p)
        return
    poli(c, pts, cor or E.COR, 0.85, a, TINTA, 5)
    c.drawCircle(cx, by - h / 3, lado * 0.17, M.paint(BR, a))


def lata(c, cx, by, s, cor=None, a=1.0, k=1.0):
    """lata de tinta com o rótulo s; k = escala"""
    if a <= 0:
        return
    w, h = 170 * k, 150 * k
    x, y = cx - w / 2, by - h
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint("#E9E7E1", a))
    c.drawRect(skia.Rect.MakeXYWH(x, y + h * 0.3, w, h * 0.45), M.paint(cor or E.COR, a))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, a, stroke=4))
    c.drawOval(skia.Rect.MakeXYWH(x, y - 12 * k, w, 24 * k), M.paint("#D6D3CB", a))
    c.drawOval(skia.Rect.MakeXYWH(x, y - 12 * k, w, 24 * k), M.paint(TINTA, a, stroke=4))
    centro(c, s, cx, y + h * 0.64, 34 * k, "g", BR, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1 = C["s01.a"], C["s01.b"]
    X = 1440

    def um():
        x, yb = 300, 860
        L0 = 400
        g = ease_io(prog(t, a1 + 0.4, 1.0))
        L = L0 * lerp(1.0, 1.2, g)
        if t >= C["s01"]:
            if g > 0:
                quadrado(c, x, yb, L0, E.COR, 0.0, 0.5, 3)
            quadrado(c, x, yb, L, E.COR, 0.2, ep(t, C["s01"], 0.5))
        E.foco(c, t, a1 + 1.2, 0.4, lambda a: (E.pilula(c, "+20%", x + L / 2, yb + 60, 46, "g", a=a),
                                               E.pilula(c, "+20%", x - 100, yb - L / 2, 46, "g", a=a)))
        E.frase(c, t, a1, ps("cada lado", "i", 66) + [("+20%", "g", 76, COR)], X, 260, "center", 0.12)
        E.frase(c, t, entre(C, "s01.a", "s01.b", 0.45), ps("e a área?", "i", 70), X, 400, "center", 0.12)
        E.frase(c, t, entre(C, "s01.a", "s01.b", 0.62), [("20%?", "g", 70, TINTA2)], X - 140, 520, "center")
        E.frase(c, t, entre(C, "s01.a", "s01.b", 0.8), [("40%?", "g", 70, TINTA2)], X + 140, 520, "center")
        bola_txt(c, t, b1, "44%", X, 760, 150, 100, CERTO)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1520, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 300, passo=0.14)
        E.frase(c, t, entre(C, "s02.a", "s02.b", 0.25), [("ampliou,", "g", 100, COR), ("reduziu:", "g", 100, COR)], XE, 450, passo=0.2)
        E.frase(c, t, entre(C, "s02.a", "s02.b", 0.5), ps("a área nova", "i", 84), XE, 580, passo=0.14)
        E.frase(c, t, entre(C, "s02.a", "s02.b", 0.65), ps("sem medir tudo de novo", "i", 70, TINTA2), XE, 690, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1520, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1520, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "semelhantes: todos os lados", "× o mesmo número"), ("s03.c", "aumentar 20%:", "× 1,2"),
             ("s03.d", "dobrar o lado do quadrado:", "área × 4"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 84)
        E.formula_em(c, t, C[k] + 0.4, l2, x + 44, y + 165, 62, "g", COR)
    alvo = [(x + w - 30, 170 + i * 240 + 170) for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, alvo[0][0], lerp(lerp(alvo[0][1], alvo[1][1], q1), alvo[2][1], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 960, "left", 0.12)


# ---------------- o triângulo ampliado ----------------
B1 = (110, 900)    # o pequeno
B3 = (400, 900)    # o ampliado (× 3)


def b_triangulo(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    X = 1480
    # o pequeno
    Bp, Cp, Ap = tri(B1, 1)
    if t >= b4:
        k = ep(t, b4, 0.5)
        poli(c, [Bp, Cp, Ap], E.COR, 0.3, k)
        E.foco(c, t, b4 + 0.3, 0.4, lambda f: centro(c, "4", (Bp[0] + Cp[0]) / 2, Bp[1] + 60, 52, "g", TINTA, f))
        altura(c, t, b4 + 0.5, Ap, Bp, "3", TINTA, 48)
        E.foco(c, t, c4 + 0.6, 0.4, lambda f: E.pilula(c, "área 6", Ap[0] + 20, Ap[1] - 50, 40, "g", a=f))
    # o grande: cresce do pequeno
    if t >= a5:
        g = ease_io(prog(t, a5, 1.0))
        kk = lerp(1, 3, g)
        Bg, Cg, Ag = tri((lerp(B1[0], B3[0], g), B3[1]), kk)
        poli(c, [Bg, Cg, Ag], E.COR, 0.12, 1.0)
        E.foco(c, t, a5 + 0.6, 0.4, lambda f: E.pilula(c, "× 3", (Bg[0] + Cg[0]) / 2 + 120, Ag[1] + 40, 52, "g", fundo=AMBAR, a=f))
        Bg, Cg, Ag = tri(B3, 3)
        k9 = 1 - ep(t, a6, 0.4)  # a altura sai quando as nove cópias entram
        altura(c, t, b5, Ag, Bg, None, a=k9)
        E.foco(c, t, c5, 0.4, lambda f: centro(c, "12", (Bg[0] + Cg[0]) / 2, Bg[1] + 64, 60, "g", COR, f))
        E.foco(c, t, d5, 0.4, lambda f: E.formula(c, "9", Ag[0] + 18, (Ag[1] + Bg[1]) / 2 - 60, 60, "g", COR, f * k9, "left"))
        nove(c, B3, 3, ease_io(prog(t, a6, 1.0)))
        if t >= a6 + 0.6:
            nove_numeros(c, t, a6 + 0.6, B3, 3)

    def quatro_cinco():
        E.frase(c, t, a4, ps("vale para", "i", 62) + [("qualquer", "g", 66, COR)], X, 170, "center", 0.12)
        E.frase(c, t, a4 + 0.5, ps("figura semelhante", "i", 62), X, 250, "center", 0.12)
        E.frase(c, t, b4, ps("base", "i", 60) + [("4,", "g", 66)] + ps("altura", "i", 60) + [("3", "g", 66)], X, 330, "center", 0.12)
        fcen(c, t, c4, "f{4 · 3}{2} = 6", X, 470, 80)
        E.frase(c, t, a5, ps("razão de semelhança", "i", 58) + [("3", "g", 70, AMBAR)], X, 640, "center", 0.12)
        E.frase(c, t, b5, ps("tudo × 3,", "i", 58) + [("até a altura", "g", 62)], X, 740, "center", 0.12)
        fcen(c, t, e5, "f{12 · 9}{2} = 54", X, 900, 80, COR)
    E.saida(c, t, a6 - 0.1, quatro_cinco)
    if t >= a6 - 0.1:
        fcen(c, t, a6, "54 = 9 · 6", X, 230, 92)
        E.frase(c, t, a6 + 0.6, ps("cabem", "i", 60) + [("9", "g", 70, COR)] + ps("pequenos", "i", 60), X, 340, "center", 0.12)
        E.frase(c, t, b6, ps("lados", "i", 62) + [("× 3", "g", 70, AMBAR)], X, 480, "center", 0.12)
        E.frase(c, t, b6 + 0.6, ps("área", "i", 62) + [("× 3² = 9", "g", 70, COR)], X, 580, "center", 0.12)
        E.frase(c, t, c6, [("2 medidas:", "g", 62)] + ps("base e altura", "i", 60), X, 740, "center", 0.12)
        fcen(c, t, d6, "3 · 3 = 9", X, 880, 84, CERTO)


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    X = W / 2
    E.frase(c, t, a7, ps("razão de semelhança:", "i", 70) + [("k", "g", 90, AMBAR)], X, 220, "center", 0.12)
    E.foco(c, t, b7, 0.6, lambda a: E.formula(c, "f{área nova}{área antiga} = k^2", X, 470, 110, "g", COR, a, "center"))
    E.frase(c, t, c7, [("k", "g", 72, AMBAR)] + ps("= o número que", "i", 62) + [("multiplica cada lado", "g", 64)], X, 680, "center", 0.12)
    nomes = ("triângulo", "retângulo", "círculo", "mapa", "foto")
    t0 = entre(C, "s07.c", "s07.d", 0.45)
    ws = [E.larg(s, "g", 46) + 46 * 1.1 for s in nomes]
    x = X - (sum(ws) + 30 * (len(ws) - 1)) / 2
    for i, s in enumerate(nomes):
        E.foco(c, t, t0 + 0.3 * i, 0.4, lambda a, s=s, cx=x + ws[i] / 2: E.pilula(c, s, cx, 820, 46, "g", fundo=TINTA, a=a))
        x += ws[i] + 30
    E.frase(c, t, d7, ps("a figura", "i", 60) + [("inteira", "g", 66, COR)] + ps("na mesma proporção", "i", 60), X, 970, "center", 0.12)


# ---------------- porcentagem ----------------
QX, QYB, QU = 220, 950, 50   # quadrado de lado 10 → 500 px


def b_porcento(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    X = 1440
    L0 = 10 * QU
    g = ease_io(prog(t, b8, 0.9))
    L = L0 * lerp(1, 1.2, g)
    if t >= a8:
        if g > 0:
            quadrado(c, QX, QYB, L0, E.COR, 0.0, 0.5, 3)
        quadrado(c, QX, QYB, L, E.COR, 0.18, ep(t, a8, 0.5))
        lado = "10" if g < 0.5 else "12"
        centro(c, lado, QX + L / 2, QYB + 66, 60, "g", COR if g >= 0.5 else TINTA, ep(t, a8, 0.4))
        E.formula(c, lado, QX - 24, QYB - L / 2 + 22, 60, "g", COR if g >= 0.5 else TINTA, ep(t, a8, 0.4), "right")
        area = "100" if t < c8 else "144"
        centro(c, area, QX + L / 2, QYB - L / 2 + 30, 84, "g", TINTA if t < c8 else COR, ep(t, a8 + 0.3, 0.4))

    def oito():
        E.frase(c, t, a8, ps("lado", "i", 62) + [("10,", "g", 68)] + ps("área", "i", 62) + [("100", "g", 68)], X, 240, "center", 0.12)
        E.frase(c, t, b8, [("+20%:", "g", 66, COR)] + ps("lado", "i", 62) + [("12", "g", 70, COR)], X, 380, "center", 0.12)
        fcen(c, t, c8, "12 · 12 = 144", X, 530, 84)
        fcen(c, t, d8, "144 − 100 = 44", X, 680, 84)
        bola_txt(c, t, entre(C, "s08.d", "s08.end", 0.6), "+44%", X, 860, 125, 62, CERTO)
    E.saida(c, t, C["s09"] - 0.1, oito)
    if t >= C["s09"] - 0.1:
        E.frase(c, t, C["s09"], ps("com fatores:", "i", 66), X, 220, "center", 0.12)
        fcen(c, t, a9, "lado × 1,2", X, 360, 84)
        fcen(c, t, b9, "área × 1,2^2", X, 500, 84, COR)
        fcen(c, t, c9, "1,2 · 1,2 = 1,44", X, 650, 84)
        E.foco(c, t, d9, 0.5, lambda a: E.pilula(c, "0,44 → +44%", X, 820, 66, "g", fundo=CERTO, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a10, b10, c10, d10, e10 = (C[f"s10.{k}"] for k in "abcde")
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    X = 1440
    L0, d = 10 * QU, 2 * QU
    quadrado(c, QX, QYB, L0, E.COR, 0.18, ep(t, C["s10"], 0.5))
    centro(c, "10", QX + L0 / 2, QYB + 66, 60, "g", TINTA, ep(t, C["s10"], 0.4))
    E.formula(c, "10", QX - 24, QYB - L0 / 2 + 22, 60, "g", TINTA, ep(t, C["s10"], 0.4), "right")
    faixas(c, t, QX, QYB, L0, d, b10, c10, d10, pisca=d10 + 0.4)
    E.foco(c, t, d10 + 0.3, 0.4, lambda a: centro(c, "2 × 2", QX + L0 + d / 2, QYB - L0 - d - 24, 44, "g", COR, a))
    if t >= a11:  # o perímetro: a borda do quadrado grande, traçada
        k = ep(t, a11, 0.4) * (1 - ep(t, C["s11.end"], 0.3))
        L = L0 + d
        c.drawRect(skia.Rect.MakeXYWH(QX, QYB - L, L, L), M.paint(AMBAR, k, stroke=12))

    def dez():
        E.frase(c, t, a10, ps("erro:", "i", 64, ERRADO) + [("20% + 20% = 40%", "g", 68, ERRADO)], X, 220, "center", 0.12)
        if t >= a10 + 1.2:
            E.risco(c, X - 300, 240, X + 300, 180, t, a10 + 1.2, largura=10)
        fcen(c, t, b10, "faixa: 10 · 2 = 20", X, 380, 70, CERTO)
        fcen(c, t, c10, "faixa: 10 · 2 = 20", X, 500, 70, CERTO)
        fcen(c, t, entre(C, "s10.c", "s10.d", 0.5), "20 + 20 = 40", X, 620, 70)
        fcen(c, t, d10, "cantinho: 2 · 2 = 4", X, 750, 70, COR)
        E.foco(c, t, e10, 0.5, lambda a: E.pilula(c, "40 + 4 = 44", X, 920, 66, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s11"] - 0.1, dez)
    if t >= C["s11"] - 0.1:
        E.frase(c, t, a11, ps("perímetro:", "i", 64) + [("40 × 1,2 = 48", "g", 68, AMBAR)], X, 260, "center", 0.12)
        E.frase(c, t, a11 + 1.2, ps("os mesmos", "i", 60) + [("20%", "g", 66, AMBAR)], X, 370, "center", 0.12)
        E.frase(c, t, b11, ps("contorno acompanha o", "i", 60) + [("lado", "g", 66, AMBAR)], X, 560, "center", 0.12)
        E.frase(c, t, c11, ps("área acompanha o", "i", 60) + [("lado²", "g", 66, COR)], X, 690, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a12, b12, c12, d12 = (C[f"s12.{k}"] for k in "abcd")
    a13, b13, c13, d13, e13, f13 = (C[f"s13.{k}"] for k in "abcdef")
    X = W / 2

    def um():
        E.frase(c, t, C["s12"] + 0.2, [("atalho", "g", 90, CLARO)] + ps("dos aumentos seguidos", "i", 76, BR), X, 170, "center", 0.12)
        E.frase(c, t, a12, ps("largura", "i", 66, CLARO) + [("+20%,", "g", 74, BR)] + ps("depois altura", "i", 66, CLARO) + [("+20%", "g", 74, BR)],
                X, 330, "center", 0.12)
        fcen(c, t, b12, "20 + 20 = 40", X, 500, 96, BR)
        fcen(c, t, c12, "+ f{20 · 20}{100} = 4", X, 690, 96, AMBAR)
        E.foco(c, t, d12, 0.5, lambda a: E.pilula(c, "40 + 4 = 44%", X, 890, 76, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s13"] - 0.1, um)
    if t >= C["s13"] - 0.1:
        E.frase(c, t, a13, ps("o aumento entra", "i", 64, CLARO) + [("duas vezes", "g", 70, BR)], X, 170, "center", 0.12)
        E.frase(c, t, b13, ps("na redução:", "i", 64, CLARO) + [("sinal de menos", "g", 70, BR)], X, 290, "center", 0.12)
        fcen(c, t, c13, "−20 − 20 = −40", X, 430, 80, BR)
        fcen(c, t, d13, "f{(−20) · (−20)}{100} = +4", X, 590, 76, AMBAR)
        fcen(c, t, e13, "−40 + 4 = −36%", X, 750, 86, CLARO)
        E.foco(c, t, f13, 0.5, lambda a: E.pilula(c, "só um lado muda? não compensa", X, 900, 56, "g", fundo=ERRADO, a=a))
        E.frase(c, t, f13 + 1.6, ps("deixa de ser semelhante", "i", 56, CLARO), X, 1010, "center", 0.1)


# ---------------- questão ----------------
LX, LB = 300, 780      # o logotipo pequeno
GX = 760               # o ampliado
L1 = 260


def b_questao(c, t, C, b):
    a14, b14, c14, d14 = (C[f"s14.{k}"] for k in "abcd")
    X = 1500
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), X, 160, "center", 0.12)
    E.foco(c, t, C["s14"] + 0.4, 0.5, lambda a: logo(c, LX, LB, L1, a))
    E.foco(c, t, a14, 0.5, lambda a: lata(c, LX, 1000, "200 mL", a=a))
    if t >= b14:
        g = ease_io(prog(t, b14, 0.8))
        logo(c, lerp(LX, GX, g), LB, L1 * lerp(1, 1.3, g), 1.0, tracejado=True)
        E.foco(c, t, b14 + 0.6, 0.4, lambda a: E.pilula(c, "× 1,3", GX, LB - L1 * 1.3 * 0.87 - 50, 50, "g", fundo=AMBAR, a=a))
        E.foco(c, t, d14, 0.5, lambda a: lata(c, GX, 1000, "? mL", cor=ERRADO, a=a))
    linhas = [(a14, ps("logotipo:", "i", 58) + [("200 mL", "g", 64)]), (b14, ps("cada medida", "i", 58) + [("+30%", "g", 64, COR)]),
              (c14, ps("tinta acompanha a", "i", 58) + [("área", "g", 64, COR)]), (d14, ps("versão nova:", "i", 58) + [("? mL", "g", 64, COR)])]
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, 770 + i * 85, "center", 0.12)
    E.relogio(c, t, C["s15.a"], X, 370, 150)


def b_resposta(c, t, C, b):
    a16, b16, c16, d16 = (C[f"s16.{k}"] for k in "abcd")
    a17, b17, c17, d17 = (C[f"s17.{k}"] for k in "abcd")
    X = 1480
    logo(c, LX, LB, L1, 1.0)
    logo(c, GX, LB, L1 * 1.3, 1.0, cor=E.COR)
    E.pilula(c, "× 1,3", GX, LB - L1 * 1.3 * 0.87 - 50, 50, "g", fundo=AMBAR)
    lata(c, LX, 1000, "200 mL")
    E.foco(c, t, a17 + 0.6, 0.5, lambda a: lata(c, GX, 1000, "338 mL", cor=CERTO, a=a))

    def um():
        fcen(c, t, a16, "lado × 1,3", X, 230, 84)
        fcen(c, t, b16, "área × 1,3^2", X, 380, 84, COR)
        fcen(c, t, c16, "13 · 13 = 169", X, 540, 84)
        fcen(c, t, d16, "1,3^2 = 1,69", X, 700, 90, COR)
    E.saida(c, t, C["s17"] - 0.1, um)
    if t >= C["s17"] - 0.1:
        fcen(c, t, a17, "200 · 1,69 = 338", X, 220, 80)
        bola_txt(c, t, a17 + 0.6, "338 mL", X, 390, 110, 56, CERTO)
        E.frase(c, t, b17, ps("atalho:", "i", 60, AMBAR) + [("30 + 30 = 60", "g", 66)], X, 590, "center", 0.12)
        fcen(c, t, c17, "+ f{30 · 30}{100} = 9", X, 740, 76, AMBAR)
        fcen(c, t, d17, "60 + 9 = 69%", X - 50, 900, 80, CERTO)
        E.foco(c, t, d17 + 0.8, 0.4, lambda a: E.selo(c, X + 290, 875, 44 * ease_back(prog(t, d17 + 0.8, 0.4)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s18.a", "lados:", "× k"), ("s18.b", "área:", "× k^2"), ("s18.c", "a % do lado", "não passa igual para a área"))
        for i, (k, it, g) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(it, "i", 80)], 400, y)
            E.formula_em(c, t, C[k] + 0.5, g, 400 + E.larg(it, "i", 80) + 30, y, 76, "g", COR)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    a19, b19, c19, d19, e19 = (C[f"s19.{k}"] for k in "abcde")
    E.frase(c, t, C["s19"] + 0.1, ps("próxima aula:", "i", 72), XE, 220, passo=0.1)
    E.frase(c, t, C["s19"] + 0.8, [("triângulos de mesma altura", "g", 84, COR)], XE, 340)
    # dois triângulos com o mesmo topo: bases 2 e 3
    A, yb = (560, 440), 780
    P0, P1, P2 = (260, yb), (500, yb), (860, yb)
    if t >= a19:
        k = ep(t, a19, 0.5)
        poli(c, [P0, P1, A], E.COR, 0.35, k)
        poli(c, [P1, P2, A], AMBAR, 0.35, k)
        M.line(c, *A, A[0], yb, TINTA2, k, 5, dash=E.TRACO)
        E.foco(c, t, a19 + 0.3, 0.4, lambda f: E.formula(c, "h", A[0] + 16, (A[1] + yb) / 2, 56, "g", TINTA, f, "left"))
    E.foco(c, t, b19, 0.4, lambda f: (centro(c, "2", (P0[0] + P1[0]) / 2, yb + 64, 56, "g", COR, f),
                                      centro(c, "3", (P1[0] + P2[0]) / 2, yb + 64, 56, "g", AMBAR, f)))
    E.foco(c, t, b19 + 0.5, 0.4, lambda f: E.formula(c, "f{área 1}{área 2} = f{2}{3}", 1150, 640, 76, "g", COR, f, "left"))
    E.foco(c, t, c19, 0.5, lambda f: E.pilula(c, "a mediana corta ao meio", 1450, 800, 50, "g", fundo=TINTA, a=f))
    E.foco(c, t, d19, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1600, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, d19 + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1720, p), lerp(700, 495, p), ep(t, d19 + 0.2, 0.4))
    E.frase(c, t, e19, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 1010, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, triangulo=b_triangulo, regra=b_regra, porcento=b_porcento, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
