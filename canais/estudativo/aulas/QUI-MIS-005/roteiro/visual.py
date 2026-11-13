"""Visual — Estudativo · QUI-MIS-005: praticando substâncias, misturas e estados físicos (aula de prática).

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e as convenções da trilha (QUI-MIS-002:
lente, copo em camadas; QUI-MIS-003: âmbar absorve, azul libera; QUI-MIS-004: curva trecho a trecho). Cada questão é um
bloco: enunciado à esquerda, desenho à direita; na pausa, o relógio ocupa o lugar do desenho; na resolução, o desenho
volta e ganha as marcas. A pegadinha de cada questão aparece em vermelho, riscada.
Peças repetidas das aulas anteriores (candidatas ao kit): copo_camadas, Graf + curva_aq. Nova: quadro_moleculas, espelho.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Química", "Matéria e Misturas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-MIS-005_praticando_substancias_misturas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "fim"))
BR = "#FFFFFF"
OLEO = "#E8B23A"
FRIO = "#1F6FEB"

QUADROS = {"A": ["O2"] * 6, "B": ["H2O"] * 6, "C": ["H2O"] * 3 + ["O2"] * 3, "D": ["O2"] * 3 + ["O3"] * 3}
assert [k for k, v in QUADROS.items() if len(set(v)) == 1 and len(Q.contar(v[0])) > 1] == ["B"]  # a composta
assert [k for k, v in QUADROS.items() if len(set(v)) > 1] == ["C", "D"]                           # as misturas
SOLDA = [(0, 150), (2, 217), (4, 217), (6, 270), (8, 310), (10, 340)]
assert SOLDA[1][1] == SOLDA[2][1] == 217 and SOLDA[3][1] != SOLDA[4][1]  # só o patamar da fusão: eutética


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def num(c, t, t0, n, cx, cy, r=34, cor=TINTA):
    E.foco(c, t, t0, 0.3, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, str(n), cx, cy + r * 0.45, r * 1.25, "g", BR, a)))


def riscado(c, t, t0, s, x, y, size=56):
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, "i", ERRADO, a))
    if t >= t0 + 0.8:
        E.risco(c, x - 10, y + 14, x + E.larg(s, "i", size) + 10, y - size * 0.6, t, t0 + 0.8, largura=8)


def titulo_q(c, t, t0, n):
    E.frase(c, t, t0, [("questão", "i", 70, TINTA2), (str(n), "g", 80, COR)], XE, 170, passo=0.12)


def copo_camadas(c, t, t0, cx, yb, w, h, camadas, a=1.0):
    """copo com fases empilhadas de baixo para cima: camadas = [(cor ou "areia", fração, instante)]. Devolve as faixas."""
    if t < t0 or a <= 0:
        return []
    q = ep(t, t0, 0.5) * a
    contorno, dentro, (yt, yb_) = Q._copo_path("bequer", cx, yb, w, h)
    c.drawPath(dentro, M.paint(BR, 0.45 * q))
    c.save()
    c.clipPath(dentro, skia.ClipOp.kIntersect, True)
    y, faixas = yb_, []
    for k, (tipo, f, ti) in enumerate(camadas):
        hh = (yb_ - yt) * f * (ease_io(prog(t, ti, 0.9)) if ti is not None else 1.0)
        r = skia.Rect.MakeLTRB(cx - w, y - hh, cx + w, y + 1)
        pt = skia.Paint(AntiAlias=True)
        pt.setShader(skia.GradientShader.MakeLinear([skia.Point(0, y - hh), skia.Point(0, y)],
                                                    [M.hexc(M.mix(tipo, BR, 0.15), 0.92 * q), M.hexc(M.mix(tipo, "#000000", 0.1), 0.95 * q)]))
        c.drawRect(r, pt)
        M.line(c, cx - w, y - hh, cx + w, y - hh, M.mix(tipo, BR, 0.5), q, 4)
        faixas.append((y - hh, y))
        y -= hh
    c.restore()
    pv = M.paint(Q.VIDRO, q, stroke=5)
    pv.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(contorno, pv)
    M.line(c, cx - w * 0.36, yt + h * 0.18, cx - w * 0.36, yt + h * 0.55, BR, 0.7 * q, max(4, w * 0.03))
    return faixas


def gelo(c, cx, cy, s, giro, a=1.0):
    c.save(); c.translate(cx, cy); c.rotate(giro)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-s / 2, -s / 2, s, s), s * 0.18, s * 0.18)
    c.drawRRect(r, M.paint("#EAF6FB", 0.95 * a)); c.drawRRect(r, M.paint("#8FC3DA", a, stroke=4))
    M.line(c, -s * 0.25, -s * 0.3, s * 0.1, -s * 0.3, BR, a, 5)
    c.restore()


def quadro_moleculas(c, t, t0, x, y, w, h, mols, letra, semente=1, s=50):
    """um quadro com as moléculas de um sistema, como nos desenhos de prova"""
    if t < t0:
        return
    q = ep(t, t0, 0.5)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 20, 20), M.paint(BR, 0.7 * q))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 20, 20), M.paint(Q.VIDRO, q, stroke=4))
    rnd = random.Random(semente)
    cols = 3
    for i, m in enumerate(mols):
        cx = x + w * (0.2 + 0.3 * (i % cols)) + rnd.uniform(-14, 14)
        cy = y + h * (0.3 + 0.42 * (i // cols)) + rnd.uniform(-12, 12)
        Q.molecula_desenho(c, m, cx + 4 * math.sin(t * 1.4 + i), cy + 4 * math.cos(t * 1.2 + i), s, q, giro=rnd.uniform(0, 360) + 8 * math.sin(t * 0.6 + i), rotulos=False)
    E.foco(c, t, t0, 0.4, lambda a: (E.bola(c, x + 6, y + 6, 34, TINTA, a), centro(c, letra, x + 6, y + 22, 44, "g", BR, a)))


class Graf:
    def __init__(self, x, y, w, h, tmin, tmax):
        self.x, self.y, self.w, self.h = x, y, w, h
        span = tmax - tmin
        self.lo, self.hi = tmin - span * 0.08, tmax + span * 0.06

    def X(self, m):
        return self.x + self.w * 0.04 + self.w * 0.9 * m / 10

    def Y(self, T):
        return self.y + self.h - self.h * (T - self.lo) / (self.hi - self.lo)


def eixos(c, t, t0, G, size=40):
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    M.arrow(c, G.x, G.y + G.h, G.x, G.y - 20, TINTA, p, 4, 18, ease_io(prog(t, t0, 0.6)))
    M.arrow(c, G.x, G.y + G.h, G.x + G.w + 20, G.y + G.h, TINTA, p, 4, 18, ease_io(prog(t, t0, 0.6)))
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: (E.escreve(c, "temperatura (°C)", G.x + 18, G.y - 10, size, "b", TINTA, a),
                                          E.escreve(c, "tempo", G.x + G.w - E.larg("tempo", "b", size), G.y + G.h + size * 1.4, size, "b", TINTA, a)))


def curva_aq(c, t, G, nos, tl, dur, valores=(), tv=(), largura=8):
    for k in range(5):
        if tl[k] is None or t < tl[k]:
            continue
        p = ease_io(prog(t, tl[k], dur[k]))
        (m0, T0), (m1, T1) = nos[k], nos[k + 1]
        M.line(c, G.X(m0), G.Y(T0), lerp(G.X(m0), G.X(m1), p), lerp(G.Y(T0), G.Y(T1), p), E.COR, 1, largura)
    for T, ti in zip(valores, tv):
        q = ep(t, ti, 0.4)
        if q <= 0:
            continue
        m = next(mm for mm, TT in nos if TT == T)
        M.line(c, G.x, G.Y(T), G.X(m), G.Y(T), TINTA2, 0.8 * q, 3, dash=[10, 8])
        s = E._num(T)
        E.foco(c, t, ti, 0.4, lambda a, s=s, T=T: E.escreve(c, s, G.x - 16 - E.larg(s, "b", 44), G.Y(T) + 16, 44, "b", TINTA, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("4", "g", 220, COR)], XE, 420)
        E.frase(c, t, C["s01.a"] + 0.4, [("questões", "g", 130)], XE + 200, 420)
        E.frase(c, t, C["s01.b"], ps("cada uma com uma", "i", 76) + [("pegadinha", "g", 76, ERRADO)], XE, 580, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("papel e caneta: você tenta primeiro", "i", 64, TINTA2), XE, 760, passo=0.1)
        E.foco(c, t, C["s01.c"] + 0.5, 0.8, lambda a: E.simbolo(c, 1580, 640, 220 * a, giro=8 * math.sin(t * 0.4)), blur=0)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02"], ps("você vai precisar de", "i", 80, TINTA2), XE, 240, passo=0.12)
    for k, (key, s) in enumerate((("s02.a", "substância e mistura"), ("s02.b", "fases"), ("s02.c", "mudanças de estado"), ("s02.d", "curva de aquecimento"))):
        y = 400 + 140 * k
        E.foco(c, t, C[key], 0.4, lambda a, y=y: E.bola(c, XE + 30, y - 24, 22, a=a))
        E.frase(c, t, C[key] + 0.1, [(s, "g", 70)], XE + 90, y)
    pilula_em(c, t, C["s02.d"] + 1.2, "faltou alguma? procure no canal", 1400, 980, 44, TINTA)


# ---------------- Q1 ----------------
def b_q1(c, t, C, b):
    titulo_q(c, t, C["s03.a"], 1)
    pos = {"A": (180, 300), "B": (620, 300), "C": (180, 640), "D": (620, 640)}
    if t < C["s04"]:
        for k, key in zip("ABCD", ("s03.b", "s03.c", "s03.d", "s03.e")):
            quadro_moleculas(c, t, C[key], 1000 + (pos[k][0] - 180) * 1.0, pos[k][1] - 40, 400, 300, QUADROS[k], k, semente=3 + ord(k))
        E.frase(c, t, C["s03.f"], ps("qual é", "i", 62) + [("composta?", "g", 62, COR)], XE, 420, passo=0.12)
        E.frase(c, t, C["s03.f"] + 1.4, ps("quais são", "i", 62) + [("misturas?", "g", 62, COR)], XE, 540, passo=0.12)
        return
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("qual é composta? quais são misturas?", "i", 56, TINTA2), XE, 290, passo=0.08)
        E.relogio(c, t, C["s04.a"], cx=W / 2, cy=600, r=200)
        return
    E.frase(c, t, C["s05.a"], ps("conte os tipos de molécula", "i", 56, TINTA2), XE + 400, 170, passo=0.08)
    resp = {"A": ("s05.b", "simples", TINTA), "B": ("s05.c", "composta", TINTA), "C": ("s06.a", "mistura", E.COR), "D": ("s06.d", "mistura", E.COR)}
    for k in "ABCD":
        x, y = 200 + (pos[k][0] - 180) * 2.0, pos[k][1] - 40
        quadro_moleculas(c, t, C["s05"], x, y, 440, 300, QUADROS[k], k, semente=3 + ord(k), s=52)
        key, s, cor = resp[k]
        tipos = len(set(QUADROS[k]))
        E.foco(c, t, C[key], 0.4, lambda a, x=x, y=y, tipos=tipos: E.escreve(c, f"{tipos} tipo{'s' if tipos > 1 else ''}", x + 470, y + 110, 46, "i", TINTA2, a))
        pilula_em(c, t, C[key] + 0.3, s, x + 590, y + 190, 46, cor)
    if t >= C["s06.b"]:
        q = ep(t, C["s06.b"], 0.4)
        x, y = 200 + (pos["D"][0] - 180) * 2.0, pos["D"][1] - 40
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 12, y - 12, 464, 324), 26, 26), M.paint(ERRADO, q, stroke=6))
        E.foco(c, t, C["s06.c"], 0.4, lambda a: E.escreve(c, "mesmo elemento, 2 substâncias", 260, 1030, 50, "b", ERRADO, a))
        pilula_em(c, t, C["s06.d"] + 0.6, "mistura de alótropos", 1500, 1010, 48, E.COR)


# ---------------- Q2 ----------------
CX2, YB2, W2, H2 = 1450, 960, 440, 600


def copo_q2(c, t, t0, t_oleo, t_gelo):
    fx = copo_camadas(c, t, t0, CX2, YB2, W2, H2, [(Q.AGUA, 0.52, None), (OLEO, 0.18, t_oleo)])
    if fx and t >= t_gelo:
        yd = fx[0][0]
        for k, (dx, g) in enumerate(((-90, 10), (60, -14))):
            q = ep(t, t_gelo + 0.3 * k, 0.4)
            gelo(c, CX2 + dx, yd + 10 + 3 * math.sin(t * 2 + k), 90, g, q)
    return fx


def b_q2(c, t, C, b):
    titulo_q(c, t, C["s07.a"], 2)
    if t < C["s08"]:
        E.frase(c, t, C["s07.b"], ps("água com sal dissolvido", "i", 62), XE, 360, passo=0.1)
        E.frase(c, t, C["s07.c"], ps("duas pedras de gelo", "i", 62), XE, 470, passo=0.1)
        E.frase(c, t, C["s07.d"], ps("uma camada de óleo", "i", 62), XE, 580, passo=0.1)
        E.frase(c, t, C["s07.e"], [("quantas", "i", 66), ("fases", "g", 66, COR), ("e", "i", 66), ("componentes?", "g", 66, COR)], XE, 760, passo=0.12)
        copo_q2(c, t, C["s07.b"], C["s07.d"], C["s07.c"])
        return
    if t < C["s09"]:
        E.frase(c, t, C["s08"], ps("quantas fases e componentes?", "i", 56, TINTA2), XE, 290, passo=0.08)
        E.relogio(c, t, C["s08.a"], cx=W / 2, cy=600, r=200)
        return
    fx = copo_q2(c, t, C["s09"], None, C["s09"])
    if fx:
        yw = (fx[0][0] + fx[0][1]) / 2 + 60
        yo = (fx[1][0] + fx[1][1]) / 2
        for key, n, y, nome in (("s09.a", 1, yw, "água com sal"), ("s09.b", 2, yo, "óleo"), ("s09.c", 3, fx[0][0] + 10, "gelo")):
            num(c, t, C[key], n, CX2 - W2 / 2 - 60, y)
            E.foco(c, t, C[key] + 0.2, 0.4, lambda a, y=y, nome=nome: E.escreve(c, nome, CX2 - W2 / 2 - 110 - E.larg(nome, "b", 46), y + 16, 46, "b", TINTA, a))
    E.foco(c, t, C["s09.d"], 0.4, lambda a: E.escreve(c, "duas pedras: a mesma fase", XE, 300, 50, "i", TINTA2, a))
    bola_txt(c, t, C["s09.e"], "3", XE + 60, 430, 56, 74, CERTO)
    E.frase(c, t, C["s09.e"] + 0.2, [("fases", "i", 70)], XE + 140, 455)
    for k, s in enumerate(("água", "sal", "óleo")):
        pilula_em(c, t, C["s10.a"] + 0.3 * k, s, XE + 70 + 170 * k, 600, 46, TINTA)
    E.foco(c, t, C["s10.c"], 0.4, lambda a: E.escreve(c, "gelo = água sólida", XE, 720, 54, "b", COR, a))
    bola_txt(c, t, C["s10.d"], "3", XE + 60, 840, 56, 74, CERTO)
    E.frase(c, t, C["s10.d"] + 0.2, [("componentes", "i", 70)], XE + 140, 865)
    riscado(c, t, C["s10.e"], "4: contou o gelo", XE, 1000, 52)


# ---------------- Q3 ----------------
def espelho(c, cx, cy, w, h, emb, a=1.0, t=0.0):
    """espelho de banheiro: moldura, reflexo e o embaçado (emb 0..1) com gotinhas"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2 - 16, cy - h / 2 - 16, w + 32, h + 32, 28, "#9AA0A8", a)
    pt = skia.Paint(AntiAlias=True)
    pt.setShader(skia.GradientShader.MakeLinear([skia.Point(cx - w / 2, cy - h / 2), skia.Point(cx + w / 2, cy + h / 2)],
                                                [M.hexc("#CFE6EF", a), M.hexc("#8FB8C9", a)]))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 18, 18), pt)
    for k in range(3):
        M.line(c, cx - w * 0.3 + 60 * k, cy - h * 0.35, cx - w * 0.1 + 60 * k, cy - h * 0.1, BR, 0.5 * a, 10)
    if emb > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 18, 18), M.paint("#F2F5F7", 0.8 * emb * a))
        rnd = random.Random(5)
        for _ in range(int(60 * emb)):
            gx, gy = cx + (rnd.random() - 0.5) * (w - 30), cy + (rnd.random() - 0.5) * (h - 30)
            r = 3 + 6 * rnd.random()
            c.drawCircle(gx, gy, r, M.paint("#BFD6E0", a * emb))
            c.drawCircle(gx - r * 0.3, gy - r * 0.3, r * 0.35, M.paint(BR, a * emb))


def vapor(c, t, x0, y0, a, n=6):
    for k in range(n):
        u = (t * 0.35 + k / n) % 1
        x = x0 + 40 * math.sin(k * 1.7 + t) + u * 160
        y = y0 - u * 220
        p = skia.Path(); p.moveTo(x, y); p.cubicTo(x + 20, y - 20, x - 20, y - 40, x, y - 60)
        c.drawPath(p, M.paint(CINZA, a * (1 - u) * min(1, 4 * u), stroke=4))


def b_q3(c, t, C, b):
    titulo_q(c, t, C["s11.a"], 3)
    if t < C["s12"]:
        E.frase(c, t, C["s11.b"], ps("depois do banho quente,", "i", 60), XE, 360, passo=0.1)
        E.frase(c, t, C["s11.b"] + 1.0, ps("o espelho embaça", "i", 60), XE, 450, passo=0.1)
        E.frase(c, t, C["s11.c"], [("qual", "i", 66), ("mudança?", "g", 66, COR)], XE, 640, passo=0.12)
        E.frase(c, t, C["s11.d"], [("absorve", "g", 62), ("ou", "i", 66), ("libera", "g", 62), ("calor?", "i", 66)], XE, 760, passo=0.12)
        E.foco(c, t, C["s11.b"], 0.5, lambda a: espelho(c, 1400, 560, 560, 640, ep(t, C["s11.b"] + 0.8, 2.0), a, t))
        return
    if t < C["s13"]:
        E.frase(c, t, C["s12"], ps("qual mudança? absorve ou libera?", "i", 56, TINTA2), XE, 290, passo=0.08)
        E.relogio(c, t, C["s12.a"], cx=W / 2, cy=600, r=200)
        return
    espelho(c, 1400, 560, 560, 640, 1.0, 1, t)
    E.foco(c, t, C["s13.a"], 0.4, lambda a: vapor(c, t, 900, 900, a))
    E.frase(c, t, C["s13.a"], ps("vapor invisível + espelho frio", "i", 56, TINTA2), XE, 330, passo=0.08)
    E.frase(c, t, C["s13.b"], [("gotinhas", "g", 62, COR), ("de", "i", 60), ("líquido", "g", 62)], XE, 440, passo=0.12)
    E.frase(c, t, C["s13.c"], [("gás", "g", 66), ("→", "g", 66, TINTA2), ("líquido", "g", 66)], XE, 590, passo=0.12)
    pilula_em(c, t, C["s13.d"], "condensação", XE + 220, 700, 60, E.COR)
    E.foco(c, t, C["s14.a"], 0.4, lambda a: (M.arrow(c, XE + 30, 790, XE + 30, 860, FRIO, a, 9, 26), E.escreve(c, "desce:", XE + 80, 850, 60, "i", TINTA, a)))
    E.foco(c, t, C["s14.b"], 0.4, lambda a: E.escreve(c, "libera calor", XE + 270, 850, 64, "g", FRIO, a))
    E.foco(c, t, C["s14.c"], 0.4, lambda a: E.escreve(c, "o espelho até esquenta", 1180, 950, 48, "i", TINTA2, a))
    riscado(c, t, C["s14.d"], "evaporação: foi no chuveiro", XE, 1010, 50)


# ---------------- Q4 ----------------
def b_q4(c, t, C, b):
    titulo_q(c, t, C["s15.a"], 4)
    G = Graf(1020, 230, 760, 640, 150, 340)
    if t < C["s16"]:
        E.frase(c, t, C["s15.a"] + 0.6, ps("aquecimento de uma solda sem chumbo", "i", 50, TINTA2), XE, 290, passo=0.08)
        E.frase(c, t, C["s15.b"], ps("deita nos 217 °C", "i", 60), XE, 420, passo=0.1)
        E.frase(c, t, C["s15.c"], ps("a fervura vai subindo", "i", 60), XE, 520, passo=0.1)
        E.frase(c, t, C["s15.d"], [("1", "g", 60, COR)] + ps("ponto de fusão?", "i", 64), XE, 680, passo=0.1)
        E.frase(c, t, C["s15.e"], [("2", "g", 60, COR)] + ps("pura ou mistura?", "i", 64), XE, 800, passo=0.1)
        eixos(c, t, C["s15.a"] + 0.4, G)
        tl = [C["s15.a"] + 0.8, C["s15.b"], C["s15.b"] + 0.8, C["s15.c"], C["s15.c"] + 0.6]
        curva_aq(c, t, G, SOLDA, tl, [0.6, 0.8, 0.6, 0.6, 0.6], (217,), (C["s15.b"],))
        return
    if t < C["s17"]:
        E.frase(c, t, C["s16"], ps("ponto de fusão? pura ou mistura?", "i", 56, TINTA2), XE, 290, passo=0.08)
        E.relogio(c, t, C["s16.a"], cx=W / 2, cy=600, r=200)
        return
    G = Graf(260, 230, 900, 640, 150, 340)
    eixos(c, t, C["s17"], G)
    curva_aq(c, t, G, SOLDA, [C["s17"] + 0.15 * k for k in range(5)], [0.3] * 5, (217,), (C["s17"],))
    if t >= C["s17.a"]:
        q = ep(t, C["s17.a"], 0.4)
        c.drawCircle((G.X(2) + G.X(4)) / 2, G.Y(217), 70 + 4 * math.sin(t * 5), M.paint(E.COR, q, stroke=6))
    E.foco(c, t, C["s17.b"], 0.4, lambda a: E.escreve(c, "PF = 217 °C", 1300, 360, 76, "g", COR, a))
    if t >= C["s17.c"]:
        E.chave(c, G.X(6), G.X(8), G.Y(310) - 40, TINTA2, ep(t, C["s17.c"], 0.5), -24)
        E.foco(c, t, C["s17.c"] + 0.3, 0.4, lambda a: E.escreve(c, "sem patamar", G.X(5.6), G.Y(310) - 90, 44, "b", TINTA2, a))
    E.frase(c, t, C["s18.a"], ps("só o patamar da fusão", "i", 58), 1300, 500, passo=0.1)
    pilula_em(c, t, C["s18.b"], "mistura eutética", 1560, 620, 60, E.COR)
    riscado(c, t, C["s18.c"], "substância pura", 1300, 790, 56)
    E.foco(c, t, C["s18.d"], 0.4, lambda a: E.escreve(c, "pura teria 2 patamares", 1300, 900, 52, "b", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("as", "i", 80, TINTA2), ("quatro", "i", 80, TINTA2), ("pegadinhas", "g", 80, COR)], W / 2, 180, "center", 0.12)
        itens = (("s19.a", [("mesmo", "i", 66), ("elemento", "g", 62), ("≠", "g", 62, ERRADO), ("substância", "i", 66), ("pura", "g", 62)]),
                 ("s19.b", [("gelo", "g", 62), ("é", "i", 66), ("água", "g", 62, COR)]),
                 ("s19.c", [("embaçado", "g", 62), ("=", "g", 62, TINTA2), ("condensação", "g", 62, COR)]),
                 ("s19.d", [("um", "i", 66), ("patamar", "g", 62), ("só", "i", 66), ("≠", "g", 62, ERRADO), ("pura", "g", 62)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("Separar", "g", 110, COR), ("sólidos", "g", 110, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s20.a"] + 0.6, ps("da peneira ao ímã", "i", 80), XE, 520, passo=0.12)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s20.b"] + 0.2, 0.4))
    E.frase(c, t, C["s20.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, fim=b_fim)
