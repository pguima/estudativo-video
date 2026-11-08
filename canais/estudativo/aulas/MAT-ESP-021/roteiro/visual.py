"""Visual — Estudativo · MAT-ESP-021: praticando sólidos compostos e razão entre volumes. Última aula da Geometria Espacial.
Mesma linguagem da trilha (MAT-ESP-001 a 020): sólidos do kit com a metade de trás tracejada, o elemento da vez na cor da
matéria, a 2ª família em cinza, resposta na esfera. Aula de prática: cada situação tem enunciado à esquerda e figura à direita,
relógio de pausa, e a resposta com a figura à esquerda e a conta à direita.
- SILO (silo()): E.cilindro com E.cone em cima, sobre a mesma base; na resposta, a parte da vez pintada (cilindro, depois cone).
- AQUÁRIO (aquario()): E.paralelepipedo com a água pintada (agua_bloco()) na altura dita; a faixa que subiu fica mais forte,
  a pedra é uma mancha cinza no fundo, a borda de 28 cm é marcada e a água que passa dela escorre pela lateral.
- LATA COM BOLAS (lata()): E.cilindro com três E.esfera empilhadas; o vazio pintado na cor da matéria por trás das bolas.
- EMBALAGENS: dois E.paralelepipedo semelhantes; a comparação dos aumentos (10% e 33,1%) com E.colunas.
- π = 3 em todas as contas.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-021_praticando_solidos_compostos_e_razao_entre_volumes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))  # a inclinação de E.cone e E.cilindro
KC, KS = 0.5 * math.cos(math.radians(38)), 0.5 * math.sin(math.radians(38))  # a profundidade de E.paralelepipedo
assert 3 * 9 == 27 and 27 * 5 == 135 and 27 * 2 == 54 and 54 // 3 == 18 and 135 + 18 == 153
assert 50 * 20 == 1000 and 26 - 23 == 3 and 1000 * 3 == 3000 and 26 + 3 == 29 and 29 > 28
assert 3 * 6 == 18 and 27 * 18 == 486 and 27 * 4 // 3 == 36 and 36 * 3 == 108 and 108 * 3 == 324 and 486 - 324 == 162 and 162 * 3 == 486
assert round(1.1 * 1.1, 4) == 1.21 and round(1.21 * 1.1, 4) == 1.331 and round(1000 * 1.331) == 1331


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com ², ³, π ou → vai na grotesca: a serifada não tem esses sinais)"""
    return [(w, "g" if any(ch in w for ch in "²³√π→") else est, size * (0.92 if any(ch in w for ch in "²³√π→") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def topo(cy, h):
    return cy - h * COS


def lateral_cil(cx, cy, r, h):
    ry, ct = r * SEN, topo(cy, h)
    p = skia.Path()
    p.moveTo(cx - r, ct); p.lineTo(cx - r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
    p.lineTo(cx + r, ct)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), 0, 180, False)
    p.close()
    return p


def lateral_cone(cx, cy, r, h):
    ry, hy = r * SEN, h * COS
    yt = -ry * ry / hy
    xt = r * math.sqrt(max(0.0, 1 - (yt / ry) ** 2))
    at = math.degrees(math.atan2(yt / ry, xt / r))
    p = skia.Path()
    p.moveTo(cx, cy - hy); p.lineTo(cx - xt, cy + yt)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180 - at, -(180 - 2 * at), False)
    p.close()
    return p


def enunciado(c, t, linhas, x=XE):
    """o enunciado à esquerda: [(t0, partes, y)]"""
    for t0, partes, y in linhas:
        E.frase(c, t, t0, partes, x, y, "left", 0.1)


# ================= peças desta aula =================
def silo(c, t, t0, cx, cy, r, h, hc, rot=(None, None, None), tm=None, size=50, pinta_cil=0.0, pinta_cone=0.0):
    """cilindro de raio r e altura h (px) com o telhado em cone de altura hc em cima, sobre a mesma base"""
    ct = topo(cy, h)
    if pinta_cil > 0:
        c.drawPath(lateral_cil(cx, cy, r, h), M.paint(E.COR, 0.45 * pinta_cil))
    if pinta_cone > 0:
        c.drawPath(lateral_cone(cx, ct, r, hc), M.paint(TINTA2, 0.45 * pinta_cone))
    E.cilindro(c, t, t0, cx, cy, r, h, rot[0], rot[1], preenche=0.3, size=size, tm=tm)
    E.cone(c, t, t0 + 0.5, cx, ct, r, hc, None, None, preenche=0.3, size=size)
    if rot[2]:
        E.foco(c, t, (tm if tm is not None else t0 + 1.2) + 0.4, 0.4,
               lambda a: E.escreve(c, rot[2], cx - r * 0.55 - 24 - E.larg(rot[2], "b", size), ct - hc * COS / 2 + 4, size, "b", COR, a))


def agua_bloco(c, x, y, a, b, hw, cor=None, alfa_=0.32, y0=0.0):
    """a água dentro do E.paralelepipedo (canto da frente embaixo em (x, y), largura a, profundidade b): de y0 a hw px de altura"""
    if hw <= y0:
        return
    dx, dy = KC * b, KS * b
    k = cor or E.COR
    corpo = skia.Path()
    corpo.addPoly([(x, y - y0), (x + a, y - y0), (x + a + dx, y - y0 - dy), (x + a + dx, y - dy - hw), (x + dx, y - dy - hw), (x, y - hw)], True)
    c.drawPath(corpo, M.paint(k, alfa_))
    sup = skia.Path(); sup.addPoly([(x, y - hw), (x + a, y - hw), (x + a + dx, y - dy - hw), (x + dx, y - dy - hw)], True)
    c.drawPath(sup, M.paint(E.mix(k, "#FFFFFF", 0.35), alfa_ * 1.3))
    M.line(c, x, y - hw, x + a, y - hw, k, 1, 4)


def pedra(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    p = skia.Path()
    pts = [(-1.0, 0.1), (-0.7, -0.6), (-0.1, -0.85), (0.6, -0.65), (1.0, -0.05), (0.75, 0.45), (-0.4, 0.5)]
    p.moveTo(cx + pts[0][0] * s, cy + pts[0][1] * s)
    for px, py in pts[1:]:
        p.lineTo(cx + px * s, cy + py * s)
    p.close()
    c.drawPath(p, M.paint("#8C8C96", a))
    c.drawPath(p, M.paint(TINTA, a, stroke=4))


def aquario(c, t, t0, x, y, s, nivel, pedras=(), medidas=True, size=46, tm=None, marca_borda=None):
    """aquário 50 x 20 x 28 cm (s px por cm), água até nivel cm; pedras = [(alfa, dx)]"""
    a, b, h = 50 * s, 20 * s, 28 * s
    for al, dxp in pedras:
        pedra(c, x + a * dxp, y - 2.2 * s, 2.6 * s, al)
    agua_bloco(c, x, y, a, b, nivel * s)
    E.paralelepipedo(c, t, t0, x, y, a, b, h, ("50", "20", "28") if medidas else (None, None, None), preenche=0.04, size=size, tm=tm)
    if marca_borda is not None:
        q = ep(t, marca_borda, 0.4)
        if q > 0:
            M.line(c, x - 30, y - h, x + a + KC * b + 30, y - h - KS * b, ERRADO, q, 5, dash=E.TRACO)
    return a, b, h


def nivel_rot(c, t, t0, x, y, s, n, cor=None, size=40, t1=None):
    """o nível n (cm) marcado à esquerda do aquário; some em t1"""
    fn = lambda: E.foco(c, t, t0, 0.4, lambda a: (M.line(c, x - 40, y - n * s, x, y - n * s, cor or E.COR, a, 5),
                                                  E.escreve(c, str(n), x - 52 - E.larg(str(n), "g", size), y - n * s + size * 0.35, size, "g", cor or COR, a)))
    if t1 is None:
        fn()
    else:
        E.saida(c, t, t1, fn)


def lata(c, t, t0, cx, cy, r, tb=None, vazio=0.0, raio=None, tr=None):
    """lata justa para três bolas de raio r (px), uma sobre a outra; a altura na tela é 6r"""
    hpx = 6 * r / COS
    if vazio > 0:
        c.drawPath(lateral_cil(cx, cy, r, hpx), M.paint(E.COR, 0.42 * vazio))
    E.cilindro(c, t, t0, cx, cy, r, hpx, preenche=0.12)
    tb = t0 + 0.6 if tb is None else tb
    for i in range(3):
        E.esfera(c, t, tb + 0.3 * i, cx, cy - r - 2 * r * i, r, preenche=0.62)
    E.cilindro(c, t, t0, cx, cy, r, hpx, preenche=0.0)
    if raio:
        ct = topo(cy, hpx)
        E.foco(c, t, tr, 0.4, lambda a: (M.line(c, cx, ct, cx + r, ct, E.COR, a, 7), c.drawCircle(cx, ct, 8 * a, M.paint(TINTA)),
                                         centro(c, raio, cx + r / 2, ct - r * SEN - 18, 52, "g", COR, a)))
    return hpx


def regua(c, t, t0, x, y0, y1, rot, cor=None, size=46, lado=1):
    p = ease_io(prog(t, t0, 0.5))
    if p <= 0:
        return
    k = cor or E.COR
    M.line(c, x, y0, x, lerp(y0, y1, p), k, 1, 5)
    for yy in (y0, y1):
        M.line(c, x - 14, yy, x + 14, yy, k, p, 5)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, rot, x + 24 if lado > 0 else x - 24 - E.larg(rot, "g", size), (y0 + y1) / 2 + size * 0.35,
                                                   size, "g", COR if cor is None else cor, a))


# ---------------- gancho ----------------
def icones(c, t, ts, y=860, k=1.0):
    """as quatro situações, pequenas, numeradas"""
    xs = (330, 760, 1190, 1600)
    if t >= ts[0]:
        silo(c, t, ts[0], xs[0], y, 70 * k, 120 * k, 60 * k)
    if t >= ts[1]:
        aquario(c, t, ts[1], xs[1] - 130 * k, y, 5 * k, 22, medidas=False)
    if t >= ts[2]:
        lata(c, t, ts[2], xs[2], y, 45 * k)
    if t >= ts[3]:
        E.paralelepipedo(c, t, ts[3], xs[3] - 140 * k, y, 110 * k, 70 * k, 140 * k, preenche=0.12)
        E.paralelepipedo(c, t, ts[3] + 0.3, xs[3] + 10 * k, y, 121 * k, 77 * k, 154 * k, preenche=0.3)
    for i, x in enumerate(xs):
        E.foco(c, t, ts[i] + 0.3, 0.4, lambda a, i=i, x=x: (E.bola(c, x, 440, 46, a=a), centro(c, str(i + 1), x, 462, 60, "g", E.SOBRE, a)))


def b_gancho(c, t, C, b):
    a1, b1 = C["s01.a"], C["s01.b"]
    E.frase(c, t, a1, [("4 situações", "g", 110, COR)] + ps("para fechar", "i", 90), W / 2, 220, "center", 0.12)
    E.frase(c, t, a1 + 1.4, ps("a geometria espacial", "i", 80), W / 2, 320, "center", 0.12)
    icones(c, t, [a1 + 0.8 + 0.5 * i for i in range(4)])
    E.foco(c, t, b1, 0.5, lambda a: E.pilula(c, "pause e resolva antes da resposta", W / 2, 1010, 54, "g", a=a, cor=E.SOBRE))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.3, ps("você vai usar", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s02.a"], 0.5, lambda a: E.escreve(c, "4", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s02.a"] + 0.15, 0.5, lambda a: E.escreve(c, "ferramentas", XE + 215, 700, 100, "i", TINTA, a))
    x, w, hh, dy, y0 = 940, 880, 160, 200, 140
    itens = (("s02.b", "separar em", "partes conhecidas"), ("s02.c", "medir o volume pela", "água que sobe"),
             ("s02.d", "achar a medida que", "liga um sólido ao outro"), ("s02.e", "multiplicar o volume por", "k³"))
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * dy
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, hh, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 52), x + 40, y + 66, "left", 0.08)
        E.frase(c, t, C[k] + 0.4, [(l2, "g", 58, COR)], x + 40, y + 134, "left", 0.08)
    alvo = [y0 + i * dy + hh - 24 for i in range(4)]
    py = alvo[0]
    for i, k in enumerate(("s02.c", "s02.d", "s02.e")):
        py = lerp(py, alvo[i + 1], ease_io(prog(t, C[k] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s02.b"], 0.4))
    E.frase(c, t, lerp(C["s02.e"], C["s02.end"], 0.75), ps("travou?", "i", 50, COR) + ps("procure a aula no canal", "i", 50), x, 1010, "left", 0.1)


# ---------------- situação 1: o silo ----------------
S1X, S1Y, S1R, S1H, S1C = 1460, 930, 180, 300, 120   # raio 3 m, altura 5 m, telhado 2 m (60 px por m)


def titulo_sit(c, t, t0, n):
    E.frase(c, t, t0, ps("situação", "i", 72, COR) + [(str(n), "g", 78, COR)], XE, 190, "left", 0.1)


def b_questao1(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s03.{k}"] for k in "abcde")
    titulo_sit(c, t, a3, 1)
    enunciado(c, t, [(b3, ps("silo:", "i", 60) + [("cilindro", "g", 64, COR)], 330),
                     (b3 + 1.0, ps("raio", "i", 60) + [("3 m,", "g", 64, COR)] + ps("altura", "i", 60) + [("5 m", "g", 64, COR)], 430),
                     (c3, ps("telhado em", "i", 60) + [("cone,", "g", 64, COR)] + ps("altura", "i", 60) + [("2 m", "g", 64, COR)], 560),
                     (c3 + 1.6, ps("sobre a mesma base", "i", 54, TINTA2), 650),
                     (d3, [("π = 3", "g", 64, COR)], 770),
                     (e3, ps("quantos", "i", 70) + [("litros", "g", 76, COR)] + ps("cabem?", "i", 70), 910)])
    E.saida(c, t, C["s04.a"] - 0.1, lambda: silo(c, t, b3, S1X, S1Y, S1R, S1H, S1C, ("3 m", "5 m", "2 m"), c3 + 0.4, 50))
    E.relogio(c, t, C["s04.a"])


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    silo(c, t, C["s05"], 420, 940, 180, 300, 120, ("3", "5", "2"), C["s05"] + 0.8, 50,
         pinta_cil=ep(t, c5, 0.5), pinta_cone=ep(t, d5, 0.5))
    X = 1300

    def contas():
        E.foco(c, t, a5, 0.5, lambda q: E.pilula(c, "cilindro + cone", X, 210, 58, "g", a=q, cor=E.SOBRE))
        fcen(c, t, b5, "fundo: 3² = 9,  3 × 9 = 27 m²", X, 390, 62)
        fcen(c, t, c5, "cilindro: 27 × 5 = 135", X, 540, 66, COR)
        fcen(c, t, d5, "cone: 27 × 2 = 54", X, 690, 66, TINTA2)
        fcen(c, t, d5 + 2.0, "54 ÷ 3 = 18", X, 810, 66, TINTA2)
    fase(c, t, C["s05"], C["s06"] - 0.1, contas)
    if t < C["s06"] - 0.1:
        return
    fcen(c, t, a6, "135 + 18 = 153 m³", X, 300, 80)
    fcen(c, t, b6, "1 m³ = 1.000 L", X, 500, 72, TINTA2)
    bola_txt(c, t, c6, "153.000 L", X, 770, 190, 60)


# ---------------- situação 2: o aquário ----------------
def b_questao2(c, t, C, b):
    a7, b7, c7, d7, e7, f7 = (C[f"s07.{k}"] for k in "abcdef")
    titulo_sit(c, t, a7, 2)
    enunciado(c, t, [(b7, ps("aquário: fundo", "i", 58) + [("50 × 20 cm", "g", 62, COR)], 320),
                     (c7, ps("altura", "i", 58) + [("28 cm,", "g", 62, COR)] + ps("água em", "i", 58) + [("23", "g", 62, COR)], 420),
                     (d7, ps("uma pedra: a água sobe para", "i", 56) + [("26", "g", 62, COR)], 540),
                     (e7, [("1)", "g", 62, COR)] + ps("volume da pedra?", "i", 62), 700),
                     (f7, [("2)", "g", 62, COR)] + ps("cabe outra pedra igual", "i", 58), 820),
                     (f7 + 1.6, ps("sem transbordar?", "i", 58), 900)])
    s, x, y = 11, 1180, 840

    def fig():
        nv = lerp(23, 26, ease_io(prog(t, d7, 1.0)))
        aquario(c, t, b7, x, y, s, nv, [(ep(t, d7, 0.5), 0.5)], tm=c7)
        nivel_rot(c, t, c7 + 1.0, x, y, s, 23, TINTA2, t1=d7 + 0.8)
        if t >= d7:
            nivel_rot(c, t, d7 + 1.0, x, y, s, 26)
    E.saida(c, t, C["s08.a"] - 0.1, fig)
    E.relogio(c, t, C["s08.a"])


def b_resposta2(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    s, x, y = 13, 300, 900
    nv = 26 + 3 * ease_io(prog(t, a0, 1.0))
    a_, b_, h_ = 50 * s, 20 * s, 28 * s
    pedras = [(1.0, 0.35), (ep(t, a0, 0.4), 0.65)]
    aquario(c, t, C["s09"], x, y, s, min(nv, 28), pedras, tm=C["s09"] + 0.6, marca_borda=c0)
    if t >= a9:
        q = ep(t, a9, 0.5)
        alfa_ = 0.35 * q
        agua_bloco(c, x, y, a_, b_, 26 * s, E.COR, alfa_, y0=23 * s)
    nivel_rot(c, t, C["s09"] + 0.6, x, y, s, 23, TINTA2)
    nivel_rot(c, t, C["s09"] + 0.9, x, y, s, 26)
    if nv > 28:   # o que passa de 28 escorre pela lateral
        q = (nv - 28) / 1.0
        cxw = x + a_ + KC * b_ + 16
        top = y - h_ - KS * b_ + 6
        path = skia.Path()
        path.addRoundRect(skia.Rect.MakeXYWH(cxw - 8, top, 22, 300 * q), 11, 11)
        c.drawPath(path, M.paint(E.COR, 0.6))
        for k in range(3):
            c.drawCircle(cxw + 3 + (k - 1) * 30, top + 300 * q + 30 + 20 * k, 10, M.paint(E.COR, 0.55))
    X = 1400

    def um():
        E.frase(c, t, a9, ps("pedra =", "i", 60) + [("água que subiu", "g", 64, COR)], X, 220, "center", 0.1)
        fcen(c, t, b9, "26 − 23 = 3 cm", X, 400, 72)
        fcen(c, t, c9, "50 × 20 = 1.000", X, 550, 72)
        fcen(c, t, d9, "1.000 × 3 = 3.000 cm³", X, 700, 72, COR)
        bola_txt(c, t, d9 + 1.6, "3 L", X, 880, 110, 72)
    fase(c, t, C["s09"], C["s10"] - 0.1, um)
    if t < C["s10"] - 0.1:
        return
    E.frase(c, t, C["s10"] + 0.2, ps("segunda pedra:", "i", 60) + [("+3 cm", "g", 64, COR)], X, 220, "center", 0.1)
    fcen(c, t, b0, "26 + 3 = 29", X, 420, 84)
    fcen(c, t, c0, "29 > 28", X, 600, 96, ERRADO)
    E.foco(c, t, d0, 0.5, lambda q: E.pilula(c, "transborda!", X, 800, 76, "g", fundo=ERRADO, a=q))


# ---------------- situação 3: as bolas na lata ----------------
def b_questao3(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    titulo_sit(c, t, a1, 3)
    enunciado(c, t, [(b1, [("3 bolas", "g", 64, COR)] + ps("de raio", "i", 60) + [("3 cm", "g", 64, COR)], 330),
                     (b1 + 1.6, ps("numa lata, uma sobre a outra", "i", 58), 430),
                     (c1, ps("encostam no fundo, na tampa", "i", 56, TINTA2), 550),
                     (c1 + 1.2, ps("e na parede", "i", 56, TINTA2), 630),
                     (d1, [("π = 3:", "g", 62, COR)] + ps("quanto fica", "i", 66) + [("vazio?", "g", 70, COR)], 800)])
    E.saida(c, t, C["s12.a"] - 0.1, lambda: lata(c, t, b1, 1500, 960, 115, b1 + 0.5))
    E.relogio(c, t, C["s12.a"])


def b_resposta3(c, t, C, b):
    a3, b3 = C["s13.a"], C["s13.b"]
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    a5, b5 = C["s15.a"], C["s15.b"]
    cx, cy, r = 330, 990, 120
    hpx = lata(c, t, C["s13"], cx, cy, r, C["s13"] + 0.4, ep(t, a5, 0.6), "3", a3)
    regua(c, t, b3, cx + r + 50, cy - 6 * r, cy, "18 = 3 × 6", None, 50)
    X = 1330

    def frases():
        E.frase(c, t, C["s13"] + 0.3, ps("as frases que ligam as medidas", "i", 58), X, 230, "center", 0.1)
        E.frase(c, t, a3, ps("raio da lata = raio da bola:", "i", 54) + [("3", "g", 62, COR)], X, 420, "center", 0.1)
        E.frase(c, t, b3, ps("altura da lata =", "i", 54) + [("3 diâmetros", "g", 60, COR)], X, 580, "center", 0.1)
        fcen(c, t, b3 + 1.4, "3 × 6 = 18", X, 720, 84, COR)
    fase(c, t, C["s13"], C["s14"] - 0.1, frases)

    def contas():
        fcen(c, t, a4, "lata: 3 × 9 = 27", X, 230, 64)
        fcen(c, t, a4 + 1.8, "27 × 18 = 486", X, 340, 64, COR)
        fcen(c, t, b4, "bola: 3³ = 27", X, 500, 64)
        fcen(c, t, b4 + 1.8, "f{4}{3} · 27 = 36,  36 × 3 = 108", X, 630, 64, TINTA2)
        fcen(c, t, c4, "3 bolas: 3 × 108 = 324", X, 810, 66, TINTA2)
    fase(c, t, C["s14"], C["s15"] - 0.1, contas)
    if t < C["s15"] - 0.1:
        return
    E.frase(c, t, C["s15"] + 0.1, ps("vazio", "i", 70, COR), X, 220, "center", 0.1)
    fcen(c, t, a5, "486 − 324", X - 210, 450, 84)
    bola_txt(c, t, a5 + 0.8, "162 cm³", X + 230, 430, 140, 54)
    fcen(c, t, b5, "162 = f{1}{3} · 486", X, 760, 92, COR)
    E.frase(c, t, b5 + 0.8, [("um terço", "g", 60, COR)] + ps("da lata", "i", 56), X, 920, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def icone_lata(c, cx, cy, r, n, a):
    """o corte da lata justa: retângulo 2r x 2nr com n círculos; o vazio na cor da matéria"""
    if a <= 0:
        return
    rect = skia.Rect.MakeXYWH(cx - r, cy - 2 * n * r, 2 * r, 2 * n * r)
    c.drawRect(rect, M.paint(E.COR, 0.85 * a))
    for i in range(n):
        c.drawCircle(cx, cy - r - 2 * r * i, r, M.paint("#0A0820", a))
        c.drawCircle(cx, cy - r - 2 * r * i, r, M.paint(BR, a, stroke=5))
    c.drawRect(rect, M.paint(BR, a, stroke=5))


def b_atalho(c, t, C, b):
    palco(c, t)
    a6, b6, c6, d6, e6 = (C[f"s16.{k}"] for k in "abcde")
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, C["s16"] + 0.2, ps("o atalho:", "i", 64, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a6, ps("bola em lata justa ocupa", "i", 64, CLARO) + [("2/3", "g", 72, BR)], W / 2, 270, "center", 0.1)
        E.foco(c, t, b6, 0.5, lambda q: icone_lata(c, 420, 820, 170, 1, q))
        E.foco(c, t, b6 + 0.4, 0.4, lambda q: E.escreve(c, "altura = 2r", 620, 660, 54, "g", CLARO, q))
        fcen(c, t, c6, "lata: πr^2 · 2r = 2πr^3", 1260, 470, 72, BR)
        fcen(c, t, d6, "bola: f{4πr^3}{3}", 1260, 650, 72, BR)
        fcen(c, t, e6, "f{2}{3} · 2 = f{4}{3}", 1260, 850, 80, CLARO)
        E.foco(c, t, e6 + 2.0, 0.5, lambda q: E.pilula(c, "a bola é 2/3 da lata", 1260, 1000, 54, "g", a=q, cor=E.SOBRE))
    fase(c, t, C["s16"], C["s17"] - 0.1, um)
    if t < C["s17"] - 0.1:
        return
    E.foco(c, t, C["s17"] + 0.1, 0.5, lambda q: icone_lata(c, 380, 960, 125, 3, q))
    E.frase(c, t, a7, ps("3 bolas: lata", "i", 62, CLARO) + [("3 vezes", "g", 66, BR)] + ps("mais alta", "i", 62, CLARO), 1180, 260, "center", 0.1)
    E.frase(c, t, a7 + 1.4, ps("e guarda", "i", 62, CLARO) + [("3 vezes", "g", 66, BR)] + ps("mais", "i", 62, CLARO), 1180, 350, "center", 0.1)
    E.frase(c, t, b7, ps("continua", "i", 70, CLARO) + [("2/3", "g", 80, BR)], 1180, 500, "center", 0.1)
    E.foco(c, t, c7, 0.5, lambda a: E.selo(c, 760, 660, 48, False, a))
    E.frase(c, t, c7 + 0.1, ps("bolas longe da parede,", "i", 56, CLARO), 840, 680, "left", 0.1)
    E.frase(c, t, c7 + 1.4, ps("numa lata mais larga", "i", 56, CLARO), 840, 760, "left", 0.1)
    E.foco(c, t, d7, 0.5, lambda a: E.pilula(c, "faça as duas contas", 1180, 920, 64, "g", a=a, cor=E.SOBRE))


# ---------------- situação 4: a embalagem ----------------
def embalagens(c, t, t0, t1, x, y, s, rot=True):
    """a embalagem de 1 L e a semelhante, com cada medida × 1,1"""
    E.paralelepipedo(c, t, t0, x, y, 10 * s, 6 * s, 14 * s, preenche=0.12)
    E.foco(c, t, t0 + 0.6, 0.4, lambda a: centro(c, "1 L", x + 5 * s, y + 70, 58, "g", TINTA2, a))
    x2 = x + 10 * s + 6 * s * KC + 70
    E.paralelepipedo(c, t, t1, x2, y, 11 * s, 6.6 * s, 15.4 * s, preenche=0.3, cor=E.COR)
    if rot:
        E.foco(c, t, t1 + 0.6, 0.4, lambda a: centro(c, "cada medida × 1,1", x2 + 5.5 * s, y + 70, 50, "g", COR, a))


def b_questao4(c, t, C, b):
    a8, b8, c8, d8, e8 = (C[f"s18.{k}"] for k in "abcde")
    titulo_sit(c, t, a8, 4)
    enunciado(c, t, [(b8, ps("embalagem de", "i", 60) + [("1 litro", "g", 64, COR)], 330),
                     (b8 + 1.2, ps("ganha uma versão", "i", 60) + [("semelhante", "g", 64, COR)], 430),
                     (c8, ps("cada medida", "i", 60) + [("10% maior", "g", 64, COR)], 550),
                     (d8, [("1)", "g", 62, COR)] + ps("quantos mL na nova?", "i", 62), 720),
                     (e8, [("2)", "g", 62, COR)] + ps("o volume aumenta quantos %?", "i", 60), 840)])
    E.saida(c, t, C["s19.a"] - 0.1, lambda: embalagens(c, t, b8, c8, 1180, 860, 22))
    E.relogio(c, t, C["s19.a"])


def b_resposta4(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    a1, b1, c1, d1 = (C[f"s21.{k}"] for k in "abcd")
    X = 1300

    def k():
        embalagens(c, t, C["s20"], C["s20"] + 0.3, 140, 900, 22, rot=False)
        E.frase(c, t, a0, [("+10%", "g", 70, COR)] + ps("=", "g", 66) + [("× 1,1", "g", 70, COR)], X, 220, "center", 0.1)
        E.frase(c, t, a0 + 1.6, ps("esse é o", "i", 58) + [("k", "g", 64, COR)], X, 310, "center", 0.1)
        fcen(c, t, b0, "volume: 1,1³", X, 470, 76)
        fcen(c, t, c0, "1,1 × 1,1 = 1,21", X, 630, 76)
        fcen(c, t, d0, "1,21 × 1,1 = 1,331", X, 790, 76, COR)
    fase(c, t, C["s20"], C["s21"] - 0.1, k)
    if t < C["s21"] - 0.1:
        return
    fcen(c, t, a1, "1.000 × 1,331 = 1.331 mL", W / 2, 220, 80, COR)
    E.frase(c, t, b1, ps("o volume aumenta", "i", 60) + [("33,1%", "g", 70, COR)], 560, 420, "center", 0.1)
    E.frase(c, t, c1, ps("bem mais que os", "i", 56) + [("10%", "g", 62)] + ps("de cada medida", "i", 56), 560, 520, "center", 0.1)
    E.colunas(c, t, c1, [("cada medida", 10, TINTA2), ("volume", 33.1)], 1150, 360, 560, 480, vmax=40,
              fmt=lambda v: E._num(v).replace("−", "") + "%", size=46)
    E.foco(c, t, d1, 0.5, lambda q: E.pilula(c, "medidas um pouco maiores, volume bem maior", W / 2, 1000, 50, "g", a=q, cor=E.SOBRE))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s22.a", ps("separe em", "i", 66) + [("partes conhecidas", "g", 70, COR)]),
                 ("s22.b", ps("escreva a", "i", 66) + [("frase que liga as medidas", "g", 70, COR)]),
                 ("s22.c", ps("semelhantes:", "i", 66) + [("volume × k³", "g", 70, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 25, 52, a=a), centro(c, str(i + 1), 240, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 330, y, "left", 0.12)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a3, b3, c3, d3, e3, f3 = (C[f"s23.{k}"] for k in "abcdef")
    E.frase(c, t, a3, ps("geometria espacial:", "i", 70) + [("fechada", "g", 76, CERTO)], XE, 230, passo=0.1)
    E.frase(c, t, b3 - 0.8, ps("na próxima aula", "i", 72), XE, 380, passo=0.12)
    E.frase(c, t, b3, [("Estatística", "g", 130, COR)], XE, 530)
    E.frase(c, t, c3, ps("pesquisa com todo mundo ou", "i", 54) + [("só uma parte", "g", 58, COR)], XE, 660, passo=0.1)
    E.frase(c, t, d3, ps("uma amostra que respeita", "i", 54) + [("cada grupo", "g", 58, COR)], XE, 760, passo=0.1)
    E.foco(c, t, e3, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, e3 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, e3 + 0.2, 0.4))
    E.frase(c, t, f3, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4,
              resposta4=b_resposta4, fim=b_fim)
