"""Visual — Estudativo · MAT-ARE-007: praticando perímetros e áreas (cinco situações de obra e reforma).
Aula de prática no molde da MAT-ANG-019: selo de progresso "situação n de 5", figura à esquerda, pergunta embaixo à direita e
relógio de pausa; na resposta, a mesma figura ganha as medidas e a conta aparece na coluna da direita.
Linguagem da geometria plana (MAT-ANG-001): lados em tinta, linha auxiliar tracejada em TINTA2; a região da área pintada clara
(terra, grama, piso) e, quando a conta é de área, na cor da matéria; o contorno do perímetro traçado grosso em COR, dando a volta.
Medidas na grotesca; erro em vermelho, certo em verde; resposta na esfera; atalho no palco escuro.
As figuras respeitam as medidas (40 x 25, paralelogramo 12/5/4, trapézio 6/4/3, hexágono de lado 4, cercado 30 de meia volta).
Peças locais: marca() (progresso), pergunta() (linhas + relógio), escada() (cm → dm → m), terreno(), canteiro(), varanda(),
quiosque(), galao(), cercado(). Todo instante vem de C[...] (marcadores do roteiro); entre() reparte o tempo entre dois
marcadores, para a fala sem marcador acompanhar a voz real."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Áreas e Perímetros")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ARE-007_praticando_perimetros_e_areas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "atalho", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
TERRA = "#EADFC8"
GRAMA = "#D5EBCB"
PISO = "#E9D8B8"
assert 2500 / 100 == 25 and 2 * (40 + 25) == 130 and 130 * 15 == 1950 == 1300 + 650 and 1300 / 2 == 650
assert 12 * 4 == 48 and 48 * 10 == 480 and 2 * (12 + 5) == 34 and 12 * 5 * 10 == 600 and 600 - 480 == 120 and 3 ** 2 + 4 ** 2 == 5 ** 2
assert (6 + 4) * 3 / 2 == 15 and 15 * 50 == 750 and (6 + 4) / 2 * 3 == 15
assert (4 / 2) ** 2 == 4 and 6 * 4 == 24 and abs(24 * 1.7 - 40.8) < 1e-9 and abs(40.8 / 20 - 2.04) < 1e-9
assert 60 / 2 == 30 and (0 + 30) / 2 == 15 and 15 * 15 == 225 and 60 / 4 == 15 and 20 * 10 == 200 and 20 + 10 == 30


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


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)


def entre(C, k1, k2, f):
    """instante a uma fração f do caminho entre dois marcadores (fala sem marcador próprio)"""
    return lerp(C[k1], C[k2], f)


def troca(t, t0, a, b):
    return b if t >= t0 else a


def marca(c, t, t0, n):
    """situação n de 5, com cinco pontos de progresso (como na MAT-ANG-019)"""
    s = f"situação {n} de 5"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", a=a)
        for i in range(5):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def pergunta(c, t, linhas, rel, X=1500, y0=800):
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, y0 + i * 95, "center", 0.12)
    E.relogio(c, t, rel, X, 400, 170)


def regiao(c, pts, cor, a):
    if a > 0:
        path = skia.Path(); path.addPoly(pts, True)
        c.drawPath(path, M.paint(cor, a))


def volta(c, t, t0, pts, cor=None, larg=14, d=1.2, a=1.0):
    """o perímetro: o contorno traçado grosso, dando a volta inteira"""
    if t >= t0 and a > 0:
        E._contorno(c, pts, ease_io(prog(t, t0, d)), cor or E.COR, larg)


def rot(c, s, x, y, size=60, cor=TINTA, a=1.0, align="center"):
    if a > 0:
        E.formula(c, s, x, y, size, "b", cor, a, align)


def rot_troca(c, t, t0, velho, novo, x, y, size=60, cor_v=TINTA, cor_n=None, align="center", tn=None):
    """um rótulo que vira outro (2.500 cm → 25 m)"""
    q = ep(t, tn if tn is not None else t0, 0.5)
    if q < 1:
        rot(c, velho, x, y, size, cor_v, 1 - q, align)
    if q > 0:
        E.foco(c, t, tn if tn is not None else t0, 0.5, lambda a: rot(c, novo, x, y, size, cor_n or COR, a, align))


def escada(c, t, t0, cx, y0, tm=None):
    """cm → dm → m: dois degraus para cima, cada um dividindo por 10 (seta subindo junto de cada degrau)"""
    nomes = ("m", "dm", "cm")
    w, dy = 190, 100
    x0 = cx - 1.5 * w
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    for i, s in enumerate(nomes):
        x, y = x0 + i * w, y0 + i * dy
        M.line(c, x, y, x + w, y, TINTA, q, 6)
        if i < 2:
            M.line(c, x + w, y, x + w, y + dy, TINTA, q, 6)
        centro(c, s, x + w / 2 + (20 if i else 0), y - 22, 58, "g", COR if i == 0 else TINTA, q)
    for k, ti in enumerate(tm or (t0 + 0.4, t0 + 0.9)):
        i = 1 - k  # o degrau de cima de cada subida: primeiro cm → dm, depois dm → m
        xr, ya, yb = x0 + (i + 1) * w + 30, y0 + (i + 1) * dy - 12, y0 + i * dy + 14
        p = ease_io(prog(t, ti, 0.5))
        if p > 0:
            M.arrow(c, xr, ya, xr, yb, AMBAR, 1.0, 6, 18, p)
            E.foco(c, t, ti + 0.2, 0.3, lambda a, xr=xr, i=i: centro(c, "÷ 10", xr - 95, y0 + i * dy + 72, 42, "b", AMBAR, a))


# ---------------- figuras ----------------
# S1: terreno 40 m x 25 m (16 px por metro)
T1 = (400, 330, 40 * 16, 25 * 16)
T1P = [(T1[0], T1[1] + T1[3]), (T1[0] + T1[2], T1[1] + T1[3]), (T1[0] + T1[2], T1[1]), (T1[0], T1[1])]


def terreno(c, t, t0, tb, tl, tconv=None, tpreco=None, cerca=None, cerca_cor=COR):
    if t < t0:
        return
    x, y, w, h = T1
    q = ease_io(prog(t, t0, 0.6))
    regiao(c, T1P, TERRA, 0.95 * q)
    E._contorno(c, T1P, q, TINTA, 6)
    for i, V in enumerate(T1P):
        E.angulo(c, t, t0 + 0.5, V, T1P[i - 1], T1P[(i + 1) % 4], r=34)
    E.foco(c, t, tb, 0.4, lambda a: rot(c, "40 m", x + w / 2, y + h + 76, 60, TINTA, a))
    if t >= tl:
        E.foco(c, t, tl, 0.4, lambda a: rot_troca(c, t, tl, "2.500 cm", "25 m", x - 30, y + h / 2 + 22, 58, TINTA, COR, "right",
                                                  tn=tconv if tconv is not None else 1e9))
    if tpreco is not None:
        E.foco(c, t, tpreco, 0.4, lambda a: E.pilula(c, "R$ 15 o metro", x + w / 2, y - 70, 50, "g", fundo=TINTA, a=a))
    if cerca is not None and t >= cerca:  # a cerca: a volta inteira, com os mourões
        p = ease_io(prog(t, cerca, 1.4))
        E._contorno(c, T1P, p, E.COR, 12)
        per = 2 * (w + h)
        for k in range(26):
            f = k / 26
            if f <= p:
                d_ = f * per
                if d_ < w:
                    P = (x + d_, y + h)
                elif d_ < w + h:
                    P = (x + w, y + h - (d_ - w))
                elif d_ < 2 * w + h:
                    P = (x + w - (d_ - w - h), y)
                else:
                    P = (x, y + (d_ - 2 * w - h))
                c.drawCircle(*P, 9, M.paint(E.COR))


# S2: canteiro em paralelogramo, base 12, lado 5, altura 4 (56 px por metro)
U2 = 56
P2X, P2Y = 200, 400
P2 = [(P2X, P2Y + 4 * U2), (P2X + 12 * U2, P2Y + 4 * U2), (P2X + 15 * U2, P2Y), (P2X + 3 * U2, P2Y)]
P2PE = (P2X + 3 * U2, P2Y + 4 * U2)
assert abs(math.dist(P2[1], P2[2]) / U2 - 5) < 1e-9


def canteiro(c, t, t0, tb, tlado, th, area=None, borda=None, h_cor=TINTA2, h_forte=None, lado_forte=None):
    if t < t0:
        return
    q = ease_io(prog(t, t0, 0.6))
    regiao(c, P2, GRAMA, 0.95 * q)
    if area is not None:
        regiao(c, P2, E.COR, 0.22 * ep(t, area, 0.6))
    E._contorno(c, P2, q, TINTA, 6)
    E.foco(c, t, tb, 0.4, lambda a: rot(c, "12 m", (P2[0][0] + P2[1][0]) / 2, P2[0][1] + 76, 60, TINTA, a))
    E.foco(c, t, tlado, 0.4, lambda a: rot(c, "5 m", (P2[1][0] + P2[2][0]) / 2 + 40, (P2[1][1] + P2[2][1]) / 2 + 22, 60, TINTA, a, "left"))
    if t >= th:
        topo = P2[3]
        forte = ep(t, h_forte, 0.4) if h_forte is not None else 0
        M.line(c, *topo, *P2PE, h_cor if forte == 0 else CERTO, 1.0, 5 + 5 * forte, dash=E.TRACO, progress=ease_io(prog(t, th, 0.6)))
        E.angulo(c, t, th + 0.4, P2PE, topo, (P2PE[0] + 50, P2PE[1]), r=36, reto=True, preenche=0.0)
        E.foco(c, t, th + 0.4, 0.4, lambda a: rot(c, "4 m", P2PE[0] + 22, (topo[1] + P2PE[1]) / 2 + 22, 60,
                                                   CERTO if forte > 0.5 else COR, a, "left"))
    if borda is not None:
        volta(c, t, borda, P2, E.COR, 12, 1.2)
    if lado_forte is not None:
        k = ep(t, lado_forte, 0.4)
        if k > 0:
            M.line(c, *P2[1], *P2[2], AMBAR, k, 16)
            M.line(c, *P2[3], *P2[0], AMBAR, k, 16)


# S3: varanda em trapézio, bases 6 e 4, altura 3 (100 px por metro)
U3 = 100
V3X, V3Y = 250, 340
V3 = [(V3X, V3Y + 3 * U3), (V3X + 6 * U3, V3Y + 3 * U3), (V3X + 5 * U3, V3Y), (V3X + U3, V3Y)]


def varanda(c, t, t0, tB, tb, th, meio=None, area=None):
    if t < t0:
        return
    q = ease_io(prog(t, t0, 0.6))
    regiao(c, V3, PISO, 0.95 * q)
    if q > 0:  # o piso: lajotas de meio metro
        c.save()
        path = skia.Path(); path.addPoly(V3, True)
        c.clipPath(path, True)
        for k in range(1, 12):
            M.line(c, V3X + k * 50, V3Y, V3X + k * 50, V3Y + 3 * U3, "#C9B48F", q, 2)
        for k in range(1, 6):
            M.line(c, V3X, V3Y + k * 50, V3X + 6 * U3, V3Y + k * 50, "#C9B48F", q, 2)
        c.restore()
    if area is not None:
        regiao(c, V3, E.COR, 0.2 * ep(t, area, 0.6))
    E._contorno(c, V3, q, TINTA, 6)
    E.foco(c, t, tB, 0.4, lambda a: rot(c, "6 m", V3X + 3 * U3, V3Y + 3 * U3 + 76, 60, TINTA, a))
    E.foco(c, t, tb, 0.4, lambda a: rot(c, "4 m", V3X + 3 * U3, V3Y - 30, 60, TINTA, a))
    if t >= th:
        topo, pe_ = V3[3], (V3X + U3, V3Y + 3 * U3)
        M.line(c, *topo, *pe_, TINTA2, 1.0, 5, dash=E.TRACO, progress=ease_io(prog(t, th, 0.6)))
        E.angulo(c, t, th + 0.4, pe_, topo, (pe_[0] + 50, pe_[1]), r=36, reto=True, preenche=0.0)
        E.foco(c, t, th + 0.4, 0.4, lambda a: rot(c, "3 m", pe_[0] + 22, V3Y + 2.3 * U3 + 22, 60, COR, a, "left"))
    if meio is not None and t >= meio:  # a base do meio e o retângulo 5 x 3
        ym = V3Y + 1.5 * U3
        x0, x1 = V3X + 0.5 * U3, V3X + 5.5 * U3
        M.line(c, x0, ym, x1, ym, E.COR, 1.0, 9, progress=ease_io(prog(t, meio, 0.6)))
        E.foco(c, t, meio + 0.5, 0.4, lambda a: E.pilula(c, "5 m", (x0 + x1) / 2 + 60, ym - 4, 46, "g", a=a))
        k = ep(t, meio + 1.2, 0.6)
        if k > 0:
            p = M.paint(CERTO, k, stroke=6)
            p.setPathEffect(skia.DashPathEffect.Make([18, 12], 0))
            c.drawRect(skia.Rect.MakeLTRB(x0, V3Y, x1, V3Y + 3 * U3), p)


# S4: quiosque em hexágono regular de lado 4 (65 px por metro)
H4C, H4R = (560, 540), 260


def hex_pts(cx=H4C[0], cy=H4C[1], r=H4R):
    return [(cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a))) for a in (0, 60, 120, 180, 240, 300)]


def quiosque(c, t, t0, tl, fatias=None, trot=None, pinta=None, falta=None):
    if t < t0:
        return
    pts = hex_pts()
    q = ease_io(prog(t, t0, 0.7))
    regiao(c, pts, PISO, 0.95 * q)
    if pinta is not None:  # dois galões cobrem 40 dos 40,8 m²: sobra a pontinha da direita
        p = ease_io(prog(t, pinta, 1.0))
        if p > 0:
            hex_area = 3 * math.sqrt(3) / 2 * H4R ** 2
            dd = math.sqrt((0.8 / 40.8) * hex_area / math.sqrt(3))  # a ponta: triângulo de 120° com lado d até o corte
            xc = H4C[0] + H4R - dd
            c.save()
            path = skia.Path(); path.addPoly(pts, True)
            c.clipPath(path, True)
            c.drawRect(skia.Rect.MakeLTRB(H4C[0] - H4R - 5, 0, lerp(H4C[0] - H4R, xc, p), H), M.paint(E.COR, 0.35))
            c.restore()
            if falta is not None:
                k = ep(t, falta, 0.5)
                if k > 0:
                    c.save(); c.clipPath(path, True)
                    c.drawRect(skia.Rect.MakeLTRB(xc, 0, W, H), M.paint(ERRADO, 0.8 * k))
                    c.restore()
                    c.drawCircle(H4C[0] + H4R - dd / 2, H4C[1], 70, M.paint(ERRADO, k, stroke=6))
    E._contorno(c, pts, q, TINTA, 6)
    E.foco(c, t, tl, 0.4, lambda a: rot(c, "4 m", (pts[4][0] + pts[5][0]) / 2, pts[4][1] + 76, 60, TINTA, a))
    if fatias is not None:
        for i, V in enumerate(pts):
            ti = fatias + 0.18 * i
            if t >= ti:
                M.line(c, *H4C, *V, TINTA, 1.0, 5, progress=ease_io(prog(t, ti, 0.4)))
            if i % 2 == 0:
                regiao(c, [H4C, V, pts[(i + 1) % 6]], E.COR, 0.16 * ep(t, ti + 0.3, 0.4))
        k = ease_back(prog(t, fatias, 0.35))
        if k > 0:
            c.drawCircle(*H4C, 9 * k, M.paint(TINTA))
    if trot is not None:
        for i in range(6):
            a1, a2 = pts[i], pts[(i + 1) % 6]
            g = ((H4C[0] + a1[0] + a2[0]) / 3, (H4C[1] + a1[1] + a2[1]) / 3)
            E.foco(c, t, trot + 0.1 * i, 0.4, lambda a, g=g: E.formula(c, "4r{3}", g[0], g[1] + 16, 42, "g", COR, a, "center"))


def galao(c, cx, by, nivel, cor, a=1.0, w=96, h=130, rotulo=None):
    """galão de tinta: base em by; nivel 0..1 de tinta dentro"""
    if a <= 0:
        return
    x, y = cx - w / 2, by - h
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14)
    if nivel > 0:
        c.save()
        c.clipRect(skia.Rect.MakeLTRB(x - 5, by - h * nivel, x + w + 5, by + 5))
        c.drawRRect(rr, M.paint(cor, a))
        c.restore()
    c.drawRRect(rr, M.paint(TINTA, a, stroke=5))
    path = skia.Path(); path.addArc(skia.Rect.MakeXYWH(cx - 30, y - 34, 60, 60), 180, 180)
    c.drawPath(path, M.paint(TINTA, a, stroke=5))
    if rotulo:
        centro(c, rotulo, cx, by + 52, 40, "b", TINTA, a)


# S5: galinheiro com 60 m de tela (cercado 20 x 10 desenhado; 24 px por metro)
G5 = (330, 360, 20 * 30, 10 * 30)
G5P = [(G5[0], G5[1] + G5[3]), (G5[0] + G5[2], G5[1] + G5[3]), (G5[0] + G5[2], G5[1]), (G5[0], G5[1])]


def cercado(c, t, t0, base="?", alt="?", tl=None, meia=None, tb=None, ta=None):
    if t < t0:
        return
    x, y, w, h = G5
    q = ease_io(prog(t, t0, 0.6))
    regiao(c, G5P, TERRA, 0.95 * q)
    E._contorno(c, G5P, q, TINTA, 6)
    if q > 0:  # a tela: mourões em volta
        for k in range(10):
            f = k / 10
            if f <= q:
                for P in ((x + w * f, y), (x + w * (1 - f), y + h)):
                    c.drawCircle(*P, 8, M.paint(TINTA))
        for k in range(1, 5):
            for X_ in (x, x + w):
                c.drawCircle(X_, y + h * k / 5, 8 * q, M.paint(TINTA))
    if meia is not None:  # a meia volta: base + altura
        k = ease_io(prog(t, meia, 0.8))
        E._contorno(c, [G5P[3], G5P[0], G5P[1]], k, E.COR, 14, fecha=False)
    E.foco(c, t, tb if tb is not None else (tl if tl is not None else t0), 0.4,
           lambda a: rot(c, base, x + w / 2, y + h + 76, 62, COR if base != "?" else TINTA, a))
    E.foco(c, t, ta if ta is not None else (tl if tl is not None else t0), 0.4,
           lambda a: rot(c, alt, x - 28, y + h / 2 + 22, 62, COR if alt != "?" else TINTA, a, "right"))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    E.frase(c, t, a_ + 0.1, ps("5", "g", 220, COR) + ps("situações", "g", 160, COR), XE, 330, passo=0.25)
    E.frase(c, t, a_ + 0.9, ps("de obra e reforma, criadas para esta aula", "i", 64, TINTA2), XE, 440, passo=0.1)
    for i, s in enumerate(("cerca", "grama", "piso", "tinta", "tela")):
        E.foco(c, t, b_ + 0.38 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, 300 + i * 330, 580, 62, "g", fundo=TINTA if i % 2 else E.COR, a=a))
    for i, (s, cx, ti) in enumerate((("pause", 560, c_), ("resolva", 1240, c_ + 0.9))):
        E.foco(c, t, ti, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 770, 56, 64, p),
                                                           E.escreve(c, s, cx - 110, 795, 92, "g", TINTA, p)))
    E.frase(c, t, d_, ps("o mais difícil:", "i", 66) + [("escolher a fórmula certa", "g", 72, COR)], W / 2, 970, "center", 0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.1, ps("o que você vai usar", "i", 84, COR), XE, 200, passo=0.12)
    itens = (("a", "perímetro:", "a volta inteira"),
             ("b", "área:", "retângulo, paralelogramo e triângulo"),
             ("c", "e também:", "trapézio e hexágono regular"),
             ("d", "o retângulo", "de maior área"))
    for i, (k, tit, sub) in enumerate(itens):
        y = 360 + i * 160
        ti = C[f"s02.{k}"]
        E.foco(c, t, ti, 0.5, lambda p, i=i, y=y: num_bola(c, str(i + 1), XE + 46, y - 26, 44, 52, p))
        E.frase(c, t, ti + 0.1, [(tit, "g", 64)], XE + 120, y)
        E.foco(c, t, ti + 0.6, 0.4, lambda a, tit=tit, sub=sub, y=y: E.escreve(c, sub, XE + 150 + E.larg(tit, "g", 64), y, 60, "i", COR, a))
    E.frase(c, t, C["s02.end"] - 2.6, ps("travou? procure a aula no canal", "i", 60), XE, 1010, passo=0.1)


# ---------------- situação 1: cerca ----------------
def b_questao1(c, t, C, b):
    a3, b3, c3, d3 = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.d"]
    marca(c, t, a3, 1)
    terreno(c, t, b3 - 0.3, b3, b3 + 1.2, tpreco=c3)
    E.saida(c, t, C["s04.a"] - 0.1, lambda: E.frase(c, t, b3, ps("terreno", "i", 64) + [("retangular", "g", 70)], 1500, 380, "center", 0.12))
    pergunta(c, t, [(b3, [("40 m × 2.500 cm", "g", 64)]),
                    (c3, ps("cerca:", "i", 60) + [("R$ 15 o metro", "g", 64)]),
                    (d3, ps("cercar tudo custa", "i", 60) + [("?", "g", 72, COR)])], C["s04.a"])


def b_resposta1(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    X = 1440
    t0 = C["s05"] - 1.2
    terreno(c, t, t0, t0, t0, tconv=c5 + 0.6, tpreco=t0, cerca=a5)
    E.foco(c, t, b6, 0.4, lambda a: E.pilula(c, "130 m", T1[0] + T1[2] / 2, T1[1] + T1[3] / 2, 64, "g", fundo=E.COR, a=a))

    def um():
        E.frase(c, t, a5, ps("cerca na borda:", "i", 62) + [("perímetro", "g", 70, COR)], X, 230, "center", 0.12)
        E.foco(c, t, b5, 0.5, lambda a: E.pilula(c, "tudo na mesma unidade", X, 370, 52, "g", fundo=TINTA, a=a))
        escada(c, t, c5 - 0.6, X, 560, (c5, c5 + 0.5))
        fcen(c, t, c5 + 1.2, "2.500 cm = 25 m", X, 900, 86, COR)
    E.saida(c, t, C["s06"] - 0.1, um)
    if t >= C["s06"] - 0.1:
        E.frase(c, t, a6, ps("retângulo:", "i", 62) + [("some e dobre", "g", 70, COR)], X, 220, "center", 0.12)
        fcen(c, t, entre(C, "s06.a", "s06.b", 0.45), "40 + 25 = 65", X, 370, 80)
        fcen(c, t, b6, "2 × 65 = 130 m", X, 500, 80, COR)
        fcen(c, t, c6, "130 × 15", X, 640, 80)
        bola_txt(c, t, c6 + 0.7, "R$ 1.950", X, 830, 150, 56, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    X = W / 2

    def um():
        E.frase(c, t, C["s07"] + 0.2, [("atalho", "g", 90, CLARO)] + ps("para o preço", "i", 76, BR), X, 170, "center", 0.12)
        E.frase(c, t, a7, [("× 15", "g", 96, BR)] + ps("é", "i", 84, CLARO) + [("× 10", "g", 96, BR)] + ps("mais a", "i", 84, CLARO)
                + [("metade", "g", 96, AMBAR)], X, 340, "center", 0.15)
        fcen(c, t, b7, "130 × 10 = 1.300", X, 500, 90, CLARO)
        fcen(c, t, c7, "1.300 ÷ 2 = 650", X, 640, 90, AMBAR)
        fcen(c, t, d7, "1.300 + 650 = 1.950", X, 790, 96, BR)
        E.foco(c, t, d7 + 0.7, 0.5, lambda a: E.pilula(c, "R$ 1.950", X, 930, 70, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s08"] - 0.1, um)
    if t >= C["s08"] - 0.1:
        E.frase(c, t, C["s08"] + 0.1, ps("por que funciona", "i", 76, CLARO), X, 170, "center", 0.12)
        fcen(c, t, a8, "15 = 10 + 5", X, 320, 92, BR)
        E.frase(c, t, entre(C, "s08.a", "s08.b", 0.5), [("5", "g", 84, AMBAR)] + ps("é a metade de", "i", 76, CLARO) + [("10", "g", 84, BR)],
                X, 440, "center", 0.12)
        E.frase(c, t, b8, [("× 5", "g", 90, BR)] + ps("é", "i", 80, CLARO) + [("× 10", "g", 90, BR)] + ps("e a", "i", 80, CLARO)
                + [("metade", "g", 90, AMBAR)], X, 590, "center", 0.15)
        E.foco(c, t, c8, 0.5, lambda a: E.pilula(c, "R$ 14,90? não compensa", X, 760, 64, "g", fundo=ERRADO, a=a))
        E.frase(c, t, d8, ps("aí,", "i", 72, CLARO) + [("faça a conta armada", "g", 80, BR)], X, 930, "center", 0.12)


# ---------------- situação 2: grama e borda ----------------
def b_questao2(c, t, C, b):
    a9, b9, c9, d9, e9, f9, g9 = (C[f"s09.{k}"] for k in "abcdefg")
    marca(c, t, a9, 2)
    canteiro(c, t, b9 - 0.3, b9, c9, d9)
    E.saida(c, t, C["s10.a"] - 0.1, lambda: E.frase(c, t, b9, ps("canteiro em", "i", 62) + [("paralelogramo", "g", 66)], 1500, 380, "center", 0.12))
    pergunta(c, t, [(e9, ps("grama:", "i", 60) + [("R$ 10 o m²", "g", 64)]),
                    (f9, ps("gramar custa", "i", 60) + [("?", "g", 72, COR)]),
                    (g9, ps("e a borda mede", "i", 60) + [("?", "g", 72, COR)])], C["s10.a"])


def b_resposta2(c, t, C, b):
    a11, b11, c11, d11 = (C[f"s11.{k}"] for k in "abcd")
    a12, b12, c12, d12, e12, f12 = (C[f"s12.{k}"] for k in "abcdef")
    X = 1440
    t0 = C["s11"] - 1.2
    canteiro(c, t, t0, t0, t0, t0, area=a11, h_forte=b11, borda=a12, lado_forte=e12)

    def um():
        E.frase(c, t, a11, ps("grama cobre:", "i", 62) + [("área", "g", 70, COR)], X, 230, "center", 0.12)
        fcen(c, t, b11, "A = base × altura", X, 380, 76, COR)
        fcen(c, t, c11, "12 × 4 = 48 m²", X, 520, 84)
        fcen(c, t, d11, "48 × 10", X, 660, 80)
        bola_txt(c, t, d11 + 0.7, "R$ 480", X, 850, 130, 66, CERTO)
    E.saida(c, t, C["s12"] - 0.1, um)

    def dois():
        E.frase(c, t, a12, ps("borda:", "i", 62) + [("o contorno", "g", 70, COR)], X, 230, "center", 0.12)
        fcen(c, t, b12, "12 + 5 = 17", X, 390, 84)
        fcen(c, t, c12, "2 × 17", X, 530, 80)
        bola_txt(c, t, c12 + 0.6, "34 m", X, 720, 120, 70, CERTO)
    if C["s12"] - 0.1 <= t:
        E.saida(c, t, d12 - 0.1, dois)
    if t >= d12 - 0.1:
        E.frase(c, t, d12, ps("na área entra a", "i", 62) + [("altura", "g", 70, CERTO)], X, 240, "center", 0.12)
        E.frase(c, t, e12, ps("no perímetro, o", "i", 62) + [("lado", "g", 70, AMBAR)], X, 360, "center", 0.12)
        fcen(c, t, f12, "12 × 5 × 10 = R$ 600", X + 40, 560, 62, ERRADO)
        if t >= f12 + 0.6:
            E.risco(c, X - 260, 575, X + 340, 510, t, f12 + 0.6, largura=10)
        E.foco(c, t, entre(C, "s12.f", "s12.end", 0.55), 0.5, lambda a: E.pilula(c, "R$ 120 a mais", X, 720, 62, "g", fundo=ERRADO, a=a))


# ---------------- situação 3: piso ----------------
def b_questao3(c, t, C, b):
    a13, b13, c13, d13, e13, f13 = (C[f"s13.{k}"] for k in "abcdef")
    marca(c, t, a13, 3)
    varanda(c, t, b13 - 0.3, c13, entre(C, "s13.c", "s13.d", 0.5), d13)
    E.saida(c, t, C["s14.a"] - 0.1, lambda: E.frase(c, t, b13, ps("varanda em", "i", 62) + [("trapézio", "g", 70)], 1500, 380, "center", 0.12))
    pergunta(c, t, [(e13, ps("piso:", "i", 60) + [("R$ 50 o m²", "g", 64)]),
                    (f13, ps("o piso custa", "i", 60) + [("?", "g", 72, COR)])], C["s14.a"], y0=850)


def b_resposta3(c, t, C, b):
    a15, b15, c15, d15, e15, f15 = (C[f"s15.{k}"] for k in "abcdef")
    X = 1440
    t0 = C["s15"] - 1.2
    varanda(c, t, t0, t0, t0, t0, meio=f15, area=a15)

    def um():
        fcen(c, t, a15, "A = f{(B + b) · h}{2}", X, 250, 84, COR)
        fcen(c, t, b15, "6 + 4 = 10", X, 430, 78)
        fcen(c, t, c15, "10 × 3 = 30", X, 540, 78)
        fcen(c, t, d15, "30 ÷ 2 = 15 m²", X, 650, 78, COR)
        fcen(c, t, e15, "15 × 50", X, 780, 74)
        bola_txt(c, t, e15 + 0.6, "R$ 750", X, 925, 105, 58, CERTO)
    E.saida(c, t, f15 - 0.1, um)
    if t >= f15 - 0.1:
        E.frase(c, t, f15, ps("pela", "i", 66) + [("base do meio", "g", 72, COR)], X, 250, "center", 0.12)
        fcen(c, t, f15 + 0.5, "f{6 + 4}{2} = 5", X, 460, 90, COR)
        fcen(c, t, entre(C, "s15.f", "s15.end", 0.6), "5 × 3 = 15 m²", X, 660, 90, CERTO)
        E.foco(c, t, entre(C, "s15.f", "s15.end", 0.75), 0.5, lambda a: E.pilula(c, "os mesmos 15", X, 820, 60, "g", fundo=CERTO, a=a))


# ---------------- situação 4: tinta no hexágono ----------------
def b_questao4(c, t, C, b):
    a16, b16, c16, d16, e16 = (C[f"s16.{k}"] for k in "abcde")
    marca(c, t, a16, 4)
    quiosque(c, t, b16 - 0.2, b16 + 0.8)
    E.saida(c, t, C["s17.a"] - 0.1, lambda: E.frase(c, t, b16, ps("hexágono", "i", 62) + [("regular", "g", 70)], 1500, 380, "center", 0.12))
    pergunta(c, t, [(c16, ps("1 galão pinta", "i", 60) + [("20 m²", "g", 64)]),
                    (d16, ps("quantos", "i", 60) + [("galões?", "g", 68, COR)]),
                    (e16, ps("use", "i", 60) + [("√3 ≈ 1,7", "g", 64)])], C["s17.a"])


def b_resposta4(c, t, C, b):
    a18, b18, c18, d18 = (C[f"s18.{k}"] for k in "abcd")
    a19, b19, c19, d19, e19 = (C[f"s19.{k}"] for k in "abcde")
    X = 1440
    t0 = C["s18"] - 1.2
    quiosque(c, t, t0, t0, fatias=a18, trot=d18, pinta=d19 - 0.2, falta=d19 + 0.8)
    E.foco(c, t, a18 + 1.2, 0.4, lambda a: E.pilula(c, "6 equiláteros", H4C[0], 200, 52, "g", fundo=E.COR, a=a))

    def um():
        E.frase(c, t, a18, ps("6 triângulos de", "i", 62) + [("lado 4", "g", 70, COR)], X, 230, "center", 0.12)
        fcen(c, t, b18, "A = f{ℓ^2 · r{3}}{4}", X, 420, 84, COR)
        E.frase(c, t, c18, ps("metade do lado:", "i", 60) + [("4 ÷ 2 = 2", "g", 70)], X, 600, "center", 0.12)
        fcen(c, t, entre(C, "s18.c", "s18.d", 0.55), "2^2 = 4", X, 720, 80)
        bola_txt(c, t, d18, "4r{3}", X, 890, 105, 66)
    E.saida(c, t, C["s19"] - 0.1, um)
    if t >= C["s19"] - 0.1:
        fcen(c, t, a19, "6 · 4r{3} = 24r{3}", X, 210, 78, COR)
        fcen(c, t, b19, "24 × 1,7 = 40,8 m²", X, 330, 76)
        fcen(c, t, c19, "40,8 ÷ 20 = 2,04", X, 450, 76)
        for i, (niv, r_) in enumerate(((1.0, "20 m²"), (1.0, "20 m²"), (0.04, "0,8 m²"))):
            E.foco(c, t, d19 + 0.25 * i, 0.4, lambda a, i=i, niv=niv, r_=r_: galao(c, X - 210 + i * 210, 690, niv, E.COR if i < 2 else ERRADO, a, rotulo=r_))
        E.frase(c, t, d19 + 0.8, ps("com 2, falta um", "i", 56) + [("pedacinho", "g", 60, ERRADO)], X, 840, "center", 0.12)
        E.foco(c, t, e19, 0.5, lambda a: E.pilula(c, "compre 3 galões", X, 960, 64, "g", fundo=CERTO, a=a))


# ---------------- situação 5: maior área com a tela ----------------
def b_questao5(c, t, C, b):
    a20, b20, c20 = C["s20.a"], C["s20.b"], C["s20.c"]
    marca(c, t, a20, 5)
    cercado(c, t, b20 - 0.3, tl=b20 + 0.6)
    E.foco(c, t, b20 + 0.3, 0.4, lambda a: E.pilula(c, "60 m de tela", G5[0] + G5[2] / 2, G5[1] - 80, 54, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s21.a"] - 0.1, lambda: E.frase(c, t, b20, ps("galinheiro", "i", 62) + [("retangular", "g", 70)], 1500, 380, "center", 0.12))
    pergunta(c, t, [(b20, [("60 m", "g", 66)] + ps("de tela", "i", 60)),
                    (c20, ps("que medidas dão a", "i", 58)),
                    (c20 + 0.8, [("maior área?", "g", 68, COR)])], C["s21.a"])


def b_resposta5(c, t, C, b):
    a22, b22, c22, d22, e22 = (C[f"s22.{k}"] for k in "abcde")
    a23, b23, c23, d23, e23, f23 = (C[f"s23.{k}"] for k in "abcdef")
    X = 1440
    t0 = C["s22"] - 1.2
    E.saida(c, t, e22 - 0.1, lambda: (cercado(c, t, t0, "x", "30 − x", meia=a22, tb=b22, ta=c22),
                                      E.foco(c, t, a22 + 0.8, 0.4, lambda a: E.pilula(c, "meia volta: 30 m", G5[0] + G5[2] / 2, G5[1] - 80, 54, "g", a=a))))
    if t >= e22 - 0.3:
        P = E.plano(c, t, e22 - 0.3, 180, 240, 860, 620, 0, 32, 0, 250, passo=5, passo_y=50, marcas_x=[0, 10, 30], marcas_y=[100],
                    nomes=("x", "A"))
        f = lambda x: x * (30 - x)
        E.area(c, t, e22 + 0.3, P, f, 0, 30, alfa=0.14)
        E.curva(c, t, e22 + 0.2, P, f, 0, 30, d=1.0)
        for xr in (0, 30):
            E.ponto(c, t, e22 + 0.9, P, xr, 0, None, cor=ERRADO)
        E.ponto(c, t, a23 + 0.6, P, 15, 225, None, guias=True, valores=True, cor=CERTO)
        E.ponto(c, t, e23, P, 20, 200, "20 × 10", guias=True, valores=True, cor=TINTA2, lado=(1, -0.4))
        E.foco(c, t, b23, 0.4, lambda a: E.pilula(c, "15 × 15", P.x(15), P.y(225) - 60, 46, "g", fundo=CERTO, a=a))

    def um():
        fcen(c, t, a22, "C + L = 60 ÷ 2 = 30", X, 230, 76, COR)
        E.frase(c, t, b22, ps("um lado:", "i", 60) + [("x", "g", 70, COR)], X - 220, 370, "center", 0.12)
        E.frase(c, t, c22, ps("o outro:", "i", 60) + [("30 − x", "g", 70, COR)], X + 200, 370, "center", 0.12)
        fcen(c, t, d22, "A(x) = x · (30 − x)", X, 530, 84)
        E.frase(c, t, e22, ps("raízes:", "i", 62) + [("0 e 30", "g", 70, ERRADO)], X, 700, "center", 0.12)
        E.frase(c, t, e22 + 1.0, ps("lado zero,", "i", 58) + [("área zero", "g", 62)], X, 810, "center", 0.12)
    E.saida(c, t, C["s23"] - 0.1, um)
    if t >= C["s23"] - 0.1:
        fcen(c, t, a23, "vértice: f{0 + 30}{2} = 15", X, 250, 76, COR)
        E.frase(c, t, b23, [("15 × 15:", "g", 70)] + ps("um", "i", 64) + [("quadrado", "g", 70, CERTO)], X, 420, "center", 0.12)
        bola_txt(c, t, c23, "225 m²", X, 580, 110, 58, CERTO)
        E.foco(c, t, d23, 0.5, lambda a: E.pilula(c, "atalho: 60 ÷ 4 = 15", X, 760, 56, "g", fundo=AMBAR, a=a))
        E.linha(c, t, [("20 × 10", "g", 64, TINTA2, e23 + 0.2), ("= 200", "g", 64, TINTA2, f23), ("< 225", "g", 64, CERTO, f23 + 0.6)], X + 50, 920, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s24.a", "borda pede", "perímetro"), ("s24.b", "cobertura pede", "área"),
                 ("s24.c", "medidas na", "mesma unidade"), ("s24.d", "no fim:", "faz sentido na compra?"))
        for i, (k, it, g) in enumerate(itens):
            y = 380 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 28, 52, a=a), centro(c, str(i + 1), 300, y - 6, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(it, "i", 72), (g, "g", 72, COR)], 400, y, passo=0.25)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25"] + 0.1, ps("próxima aula: a figura fica", "i", 72), XE, 230, passo=0.1)
    E.frase(c, t, C["s25"] + 1.0, [("redonda", "g", 110, COR)], XE, 360)
    figs = ((C["s25.a"], "círculo", 300), (C["s25.b"], "coroa", 710), (C["s25.c"], "setor", 1120))
    for i, (ti, nome, cx) in enumerate(figs):
        cy, r = 620, 125
        if t >= ti:
            if i == 0:
                E.circulo(c, t, ti, cx, cy, r, o=None, preenche=0.3, d=0.6)
            elif i == 1:
                q = ep(t, ti + 0.3, 0.5)
                path = skia.Path(); path.addCircle(cx, cy, r); path.addCircle(cx, cy, r * 0.55)
                path.setFillType(skia.PathFillType.kEvenOdd)
                c.drawPath(path, M.paint(E.COR, 0.3 * q))
                E.circulo(c, t, ti, cx, cy, r, o=None, d=0.6)
                E.circulo(c, t, ti + 0.2, cx, cy, r * 0.55, o=None, d=0.6)
            else:
                E.circulo(c, t, ti, cx, cy, r, o=None, setor=(20, 110, None), d=0.6, te={"setor": ti + 0.3})
        E.foco(c, t, ti + 0.3, 0.4, lambda a, nome=nome, cx=cx: centro(c, nome, cx, 830, 60, "g", TINTA, a))
    E.foco(c, t, C["s25.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1600, 620, 72, estilo="g", a=a))
    p = ease_io(prog(t, C["s25.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1720, p), lerp(900, 645, p), ep(t, C["s25.d"] + 0.2, 0.4))
    E.frase(c, t, C["s25.e"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, atalho=b_atalho,
              questao2=b_questao2, resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4,
              resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
