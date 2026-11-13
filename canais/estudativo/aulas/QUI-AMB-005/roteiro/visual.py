"""Visual — Estudativo · QUI-AMB-005: esgoto, DBO e oxigênio dissolvido.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a LINGUAGEM VISUAL DA QUÍMICA AMBIENTAL
(cabeçalho de QUI-AMB-001/roteiro/visual.py). Nesta aula:
- RIO = faixa de água (rio) com peixes (peixe) e moléculas de O₂ pequenas: o oxigênio dissolvido é o número de O₂ à vista.
  Peixe sem ar fica cinza e de barriga para cima. Esgoto = marrom-oliva (ESGOTO) saindo de um cano.
- BACTÉRIA = bastonete oliva (bacteria): as aeróbias "comem" a matéria orgânica e apagam O₂; as que vivem sem oxigênio
  soltam H₂S e CH₄ (moléculas + linhas de cheiro).
- OD em mg/L numa régua vertical (regua_od): verde-claro acima de 4, âmbar entre 4 e 1, vermelho perto de zero (com texto,
  não só cor).
- DBO = o que as bactérias PEDEM: frasco fechado no escuro; o O₂ que some é a DBO.
Peças candidatas ao kit: peixe, rio, bacteria, regua_od, cano, ete (estação de esgoto em etapas).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Química", "Química e Ambiente")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-AMB-005_esgoto_dbo_oxigenio.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("od", "esgoto", "dbo", "quente", "ete", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ESGOTO = "#7A6A3A"
OD0, OD5 = 9, 3            # a questão: começou com 9 mg/L e, depois de 5 dias, tinha 3
DBO_Q = OD0 - OD5
assert DBO_Q == 6 and DBO_Q == 2 * 3  # o dobro do limite de rio limpo
H2S = dict(atomos=[("S", 0, 0), ("H", -0.8, 0.6), ("H", 0.8, 0.6)], ligacoes=[(0, 1, 1), (0, 2, 1)])


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


def lista(c, t, itens, x, y0, dy, r=44):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, r, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def riscado(c, t, t0, s, x, y, size=56, est="i"):
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, est, ERRADO, a))
    if t >= t0 + 0.8:
        E.risco(c, x - 10, y + 14, x + E.larg(s, est, size) + 10, y - size * 0.6, t, t0 + 0.8, largura=8)


def peixe(c, cx, cy, s, a=1.0, vivo=1.0, t=0.0, cor="#F28C28"):
    """peixe de lado; vivo 0..1: com 0 fica cinza e vira de barriga para cima"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy + 4 * math.sin(t * 3) * vivo); c.rotate(180 * (1 - vivo))
    corpo = M.mix(cor, "#9AA0A8", 1 - vivo)
    c.drawOval(skia.Rect.MakeXYWH(-s, -s * 0.5, 2 * s, s), M.paint(corpo, a))
    p = skia.Path(); p.moveTo(-s * 0.85, 0); p.lineTo(-s * 1.5, -s * 0.5); p.lineTo(-s * 1.5, s * 0.5); p.close()
    c.drawPath(p, M.paint(corpo, a))
    c.drawCircle(s * 0.5, -s * 0.12, s * 0.14, M.paint(BR, a)); c.drawCircle(s * 0.53, -s * 0.12, s * 0.07, M.paint(TINTA, a))
    c.restore()


def rio(c, x, y, w, h, sujo=0.0, a=1.0):
    p = skia.Paint(AntiAlias=True)
    cor = M.mix("#8FC9E0", ESGOTO, sujo)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, y), skia.Point(0, y + h)], [M.hexc(M.mix(cor, BR, 0.2), a), M.hexc(M.mix(cor, "#000000", 0.15), a)]))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 24, 24), p)


def o2s(c, t, x, y, w, h, n, a=1.0, semente=2, r=26):
    rnd = random.Random(semente)
    for k in range(int(n)):
        Q.molecula_desenho(c, "O2", x + rnd.random() * w + 6 * math.sin(t + k), y + rnd.random() * h + 5 * math.cos(t * 1.3 + k), r, a, giro=rnd.random() * 180)


def bacteria(c, cx, cy, s, a=1.0, giro=0.0):
    c.save(); c.translate(cx, cy); c.rotate(giro)
    M.rrect(c, -s, -s * 0.38, 2 * s, s * 0.76, s * 0.38, "#7E8C3A", a)
    c.drawCircle(-s * 0.3, 0, s * 0.12, M.paint("#5C6828", a)); c.drawCircle(s * 0.3, 0, s * 0.12, M.paint("#5C6828", a))
    c.restore()


def cano(c, t, x, y, a=1.0, fluxo=1.0):
    M.rrect(c, x - 220, y - 30, 240, 60, 10, "#6E747C", a)
    if fluxo > 0:
        for k in range(8):
            u = (t * 0.8 + k / 8) % 1
            E.bola(c, x + 20 + u * 140, y + u * u * 200, 12, ESGOTO, a * fluxo * (1 - u * 0.5))


def regua_od(c, t, t0, x, y, h, valor=None, tv=None, a=1.0):
    """régua de oxigênio dissolvido de 0 a 10 mg/L, com as faixas dos peixes"""
    if t < t0:
        return
    q = ep(t, t0, 0.5) * a
    Y = lambda v: y + h - h * v / 10
    for v0, v1, cor in ((4, 10, "#BFE8CF"), (1, 4, "#F8D9A8"), (0, 1, "#F5B7B7")):
        c.drawRect(skia.Rect.MakeLTRB(x, Y(v1), x + 70, Y(v0)), M.paint(cor, q))
    c.drawRect(skia.Rect.MakeXYWH(x, y, 70, h), M.paint(Q.VIDRO, q, stroke=4))
    for v in (0, 4, 8, 10):
        E.escreve(c, str(v), x - 20 - E.larg(str(v), "b", 38), Y(v) + 14, 38, "b", TINTA2, q)
    E.escreve(c, "mg/L", x - 10, y - 20, 36, "b", TINTA2, q)
    for v, s in ((7, "peixes bem"), (2.5, "peixes sofrem"), (0.4, "morrem")):
        E.escreve(c, s, x + 90, Y(v) + 14, 38, "b", TINTA, q)
    if valor is not None:
        vv = valor(t) if callable(valor) else valor
        M.arrow(c, x - 70, Y(vv), x - 6, Y(vv), E.COR, q, 7, 22)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        sujo = ep(t, C["s01.c"], 2.0)
        rio(c, 140, 380, 1640, 460, 0.5 * sujo, ep(t, C["s01"], 0.5))
        rnd = random.Random(3)
        for k in range(30):
            E.foco(c, t, C["s01.a"], 0.4, lambda a, k=k: E.bola(c, 200 + rnd.random() * 1500, 420 + rnd.random() * 380, 6, ESGOTO, a))
        vivo = 1 - ep(t, C["s01.b"] + 0.6, 1.5)
        for k, (x, y) in enumerate(((500, 560), (900, 700), (1300, 520), (1550, 680))):
            E.foco(c, t, C["s01"], 0.4, lambda a, x=x, y=y, k=k: peixe(c, x + 20 * math.sin(t + k) * vivo, lerp(y, 420, 1 - vivo), 60, a, vivo, t))
        E.foco(c, t, C["s01.c"], 0.4, lambda a: cano(c, t, 360, 330, a))
        E.frase(c, t, C["s01.a"], ps("um rio cheio de comida", "i", 70), XE, 200, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("e os peixes morrem sem ar", "i", 70, ERRADO), XE, 300, passo=0.12)
        E.foco(c, t, C["s01.d"], 0.5, lambda a: (E.escreve(c, "DBO", 1350, 1010, 150, "g", COR, a)))
        E.frase(c, t, C["s01.c"] + 0.4, ps("o culpado: o esgoto", "i", 64), XE, 960, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("o", "i", 66), ("que", "i", 66), ("é", "i", 66), ("DBO", "g", 62, COR)]),
                 (C["s02.c"], [("esgoto", "g", 62), ("e", "i", 66), ("água", "i", 66), ("quente", "g", 62, ERRADO), ("asfixiam", "i", 66)]),
                 (C["s02.d"], [("como", "i", 66), ("se", "i", 66), ("trata", "i", 66), ("o", "i", 66), ("esgoto", "g", 62, COR)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("dois lembretes", "i", 80, TINTA2), XE, 220, passo=0.12)
    E.frase(c, t, C["s03.a"], [("gás", "g", 70), ("dissolve", "i", 70), ("menos", "g", 70, COR), ("na", "i", 70), ("água", "i", 70), ("quente", "g", 70, ERRADO)], XE, 420, passo=0.12)
    E.foco(c, t, C["s03.a"] + 1.0, 0.4, lambda a: E.escreve(c, "o refrigerante quente perde gás", XE, 510, 50, "i", TINTA2, a))
    E.formula_em(c, t, C["s03.b"], "1 ppm = 1 mg/L", XE, 720, 110, "g", COR)
    E.foco(c, t, C["s03.b"] + 0.6, 0.4, lambda a: E.escreve(c, "uma parte por milhão = um miligrama por litro", XE, 810, 46, "i", TINTA2, a))


# ---------------- oxigênio dissolvido ----------------
def b_od(c, t, C, b):
    rio(c, 120, 300, 1180, 600, 0, ep(t, C["s04"], 0.5))
    for k, (x, y) in enumerate(((400, 500), (800, 720), (1050, 480))):
        E.foco(c, t, C["s04"], 0.4, lambda a, x=x, y=y, k=k: peixe(c, x + 20 * math.sin(t + k), y, 56, a, 1, t))
    o2s(c, t, 160, 340, 1100, 520, 9 * ep(t, C["s04.a"], 1.5) if t < C["s05"] else 9, 1)
    E.frase(c, t, C["s04"], ps("o peixe respira o gás oxigênio dissolvido", "i", 54), 120, 220, passo=0.06)
    E.frase(c, t, C["s04.b"], [("e", "i", 60), ("é", "i", 60), ("pouco:", "g", 60, ERRADO)], 1360, 360, passo=0.12)
    E.frase(c, t, C["s04.c"], [("8", "g", 70, COR), ("a", "i", 64), ("9", "g", 70, COR), ("mg", "g", 60)], 1360, 470, passo=0.12)
    E.frase(c, t, C["s04.c"] + 1.0, ps("de oxigênio em 1 litro, a 20 °C", "i", 40, TINTA2), 1340, 540, passo=0.06)
    pilula_em(c, t, C["s04.d"], "oxigênio dissolvido: OD", 1600, 640, 46, E.COR)
    if t >= C["s05"]:
        regua_od(c, t, C["s05"], 1500, 740, 300, lambda tt: lerp(8.5, 0.5, ep(tt, C["s05.a"], 3.0)))


# ---------------- esgoto ----------------
def b_esgoto(c, t, C, b):
    if t < C["s07"]:
        sujo = ep(t, C["s06.a"], 2.0)
        rio(c, 120, 300, 1680, 600, 0.45 * sujo, ep(t, C["s06"], 0.5))
        E.foco(c, t, C["s06.a"], 0.4, lambda a: cano(c, t, 360, 250, a))
        E.frase(c, t, C["s06.a"], [("matéria", "g", 60, ESGOTO), ("orgânica:", "g", 60, ESGOTO)], 480, 200, passo=0.1)
        E.foco(c, t, C["s06.b"], 0.4, lambda a: E.escreve(c, "restos de comida, fezes, tudo o que já foi vivo", 480, 260, 42, "i", TINTA2, a))
        n_bact = int(14 * ep(t, C["s06.c"], 2.0))
        rnd = random.Random(5)
        for k in range(n_bact):
            bacteria(c, 220 + rnd.random() * 1500 + 8 * math.sin(t * 2 + k), 360 + rnd.random() * 500, 22, 1, rnd.random() * 180)
        o2s(c, t, 160, 340, 1600, 520, 12 * (1 - ep(t, C["s06.d"], 2.5)), 1, semente=7)
        vivo = 1 - ep(t, C["s06.e"] + 0.5, 1.5)
        for k, (x, y) in enumerate(((700, 600), (1200, 760))):
            peixe(c, x, lerp(y, 360, 1 - vivo), 56, 1, vivo, t)
        E.foco(c, t, C["s06.c"], 0.4, lambda a: E.escreve(c, "bactérias se alimentam", 1300, 960, 46, "b", "#5C6828", a))
        E.foco(c, t, C["s06.d"], 0.4, lambda a: E.escreve(c, "e gastam o O₂", 1300, 1020, 46, "b", ERRADO, a))
        return
    if t < C["s08"]:
        passos = ((C["s07.a"], "mais esgoto", ESGOTO), (C["s07.a"] + 0.8, "mais comida para as bactérias", "#5C6828"),
                  (C["s07.b"], "mais oxigênio gasto", ERRADO), (C["s07.c"], "menos oxigênio para os peixes", ERRADO))
        for k, (ti, s, cor) in enumerate(passos):
            y = 260 + 190 * k
            E.foco(c, t, ti, 0.4, lambda a, y=y, s=s, cor=cor, k=k: (M.rrect(c, 300, y - 70, 1320, 110, 30, BR, a, stroke=3, stroke_color=FIO),
                                                                    E.escreve(c, s, 360, y + 4, 60, "g", cor, a)))
            if k:
                M.arrow(c, 960, y - 120, 960, y - 76, TINTA2, ep(t, ti, 0.4), 6, 20)
        return
    rio(c, 120, 300, 1680, 600, 0.8, ep(t, C["s08"], 0.5))
    E.frase(c, t, C["s08.a"], ps("sem oxigênio, entram bactérias que vivem sem ele", "i", 52), 120, 220, passo=0.06)
    rnd = random.Random(9)
    for k in range(10):
        E.foco(c, t, C["s08.a"] + 0.1 * k, 0.4, lambda a, k=k: bacteria(c, 220 + 150 * k, 760 + 40 * math.sin(k), 22, a, 30 * k))
    for k in range(4):
        E.foco(c, t, C["s08.b"] + 0.2 * k, 0.4, lambda a, k=k: Q.molecula_desenho(c, H2S, 330 + 260 * k, 520 + 30 * math.sin(t + k), 50, a))
        E.foco(c, t, C["s08.c"] + 0.2 * k, 0.4, lambda a, k=k: Q.molecula_desenho(c, "CH4", 1180 + 160 * k, 520 + 30 * math.cos(t + k), 46, a))
    E.foco(c, t, C["s08.b"] + 0.4, 0.4, lambda a: E.escreve(c, "gás sulfídrico: cheiro de ovo podre", 300, 420, 46, "b", BR, a))
    E.foco(c, t, C["s08.c"] + 0.4, 0.4, lambda a: E.escreve(c, "metano", 1200, 420, 46, "b", BR, a))
    pilula_em(c, t, C["s08.d"], "o cheiro dos rios mortos das cidades", W / 2, 1000, 46, ESGOTO)


# ---------------- DBO ----------------
def b_dbo(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], [("DBO:", "g", 80, COR), ("demanda", "g", 70), ("bioquímica", "g", 70), ("de", "i", 70), ("oxigênio", "g", 70)], XE, 230, passo=0.12)
        E.frase(c, t, C["s09.b"], ps("quanto oxigênio as bactérias consomem", "i", 56), XE, 360, passo=0.08)
        E.frase(c, t, C["s09.b"] + 1.6, ps("para decompor a matéria orgânica de 1 litro", "i", 56), XE, 440, passo=0.08)
        Q.erlenmeyer(c, t, C["s09.c"], 1450, 930, 330, 380, 0.6, M.mix(Q.AGUA, ESGOTO, 0.3), graduacao=False)
        E.foco(c, t, C["s09.c"], 0.4, lambda a: M.rrect(c, 1410, 520, 80, 50, 10, "#2A2B31", a))
        E.foco(c, t, C["s09.c"] + 0.4, 0.4, lambda a: E.escreve(c, "5 dias, fechada, no escuro", XE, 640, 54, "b", TINTA, a))
        o2s(c, t, 1340, 760, 220, 140, 6 * (1 - ep(t, C["s09.d"], 2.5)), 1, semente=4, r=22)
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.escreve(c, "mede-se quanto oxigênio sumiu", XE, 760, 54, "g", COR, a))
        return
    E.frase(c, t, C["s10.a"], ps("em miligramas por litro, ou ppm", "i", 60, TINTA2), XE, 220, passo=0.08)
    for k, (rot, v, ti, cor, txt) in enumerate((("rio limpo", 3, C["s10.b"], CERTO, "até ~3"), ("esgoto de casa", 300, C["s10.c"], ESGOTO, "~300"))):
        y = 360 + 180 * k
        if t >= ti:
            q = ep(t, ti, 0.4)
            E.escreve(c, rot, 640 - E.larg(rot, "b", 54), y + 60, 54, "b", TINTA, q)
            ww = (40 if v == 3 else 950) * ease_io(prog(t, ti, 1.0))
            M.rrect(c, 680, y, ww, 80, 40, cor, q)
            E.foco(c, t, ti + 0.8, 0.4, lambda a, y=y, txt=txt, ww=ww: E.escreve(c, txt, 700 + ww, y + 58, 56, "g", TINTA, a))
    pilula_em(c, t, C["s10.d"], "quanto maior a DBO, mais poluída a água", W / 2, 860, 52, E.COR)


# ---------------- água quente ----------------
def b_quente(c, t, C, b):
    E.frase(c, t, C["s11"], ps("e a água quente?", "i", 66, TINTA2), XE, 200, passo=0.12)
    E.foco(c, t, C["s11.a"], 0.5, lambda a: (M.rrect(c, 160, 300, 420, 320, 20, "#9AA0A8", a), M.rrect(c, 420, 220, 90, 120, 8, "#7A818B", a),
                                            E.escreve(c, "usina", 260, 480, 60, "g", BR, a)))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: (M.rrect(c, 580, 520, 300, 50, 10, "#6E747C", a)))
    calor = ep(t, C["s11.b"], 2.0)
    rio(c, 900, 360, 900, 560, 0, ep(t, C["s11.a"], 0.5))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(900, 360, 900, 560), 24, 24), M.paint("#F28C28", 0.25 * calor))
    E.foco(c, t, C["s11.b"] + 0.4, 0.4, lambda a: E.escreve(c, "limpa, porém mais quente", 900, 330, 46, "b", "#B85C00", a))
    o2s(c, t, 940, 400, 820, 480, 10 * (1 - 0.6 * ep(t, C["s11.d"], 2.0)), 1, semente=11)
    peixe(c, 1350, 640, 60, 1, 1 - 0.5 * ep(t, C["s11.e"], 1.5), t)
    E.frase(c, t, C["s11.c"], ps("água quente dissolve menos gás:", "i", 52), XE, 720, passo=0.06)
    E.frase(c, t, C["s11.d"], [("cabe", "i", 56), ("menos", "g", 56, ERRADO), ("oxigênio", "g", 56)], XE, 800, passo=0.1)
    E.frase(c, t, C["s11.e"], ps("e o peixe precisa de mais", "i", 52), XE, 880, passo=0.08)
    pilula_em(c, t, C["s11.e"] + 1.5, "poluição térmica", 470, 990, 54, ERRADO)


# ---------------- estação de esgoto ----------------
def b_ete(c, t, C, b):
    E.frase(c, t, C["s12"], ps("como se trata o esgoto", "i", 66, TINTA2), XE, 180, passo=0.12)
    etapas = ((C["s12.a"], "grades e areia", "lixo grosso e areia"), (C["s12.b"], "decantação", "o lodo desce"),
              (C["s13.a"], "tanque com ar", "bactérias comem a matéria"), (C["s13.d"], "volta ao rio", "DBO baixa"))
    for k, (ti, nome, sub) in enumerate(etapas):
        x = 120 + 450 * k
        if t < ti:
            continue
        q = ep(t, ti, 0.5)
        M.rrect(c, x, 360, 380, 300, 24, M.mix(Q.AGUA, ESGOTO, 0.6 - 0.18 * k), q)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, 360, 380, 300), 24, 24), M.paint(Q.VIDRO, q, stroke=5))
        if k == 0:
            for j in range(6):
                M.line(c, x + 40 + 55 * j, 380, x + 40 + 55 * j, 640, "#4A5568", q, 8)
        elif k == 1:
            c.drawRect(skia.Rect.MakeXYWH(x + 10, 600, 360, 50), M.paint(ESGOTO, q))
        elif k == 2:
            for j in range(14):
                u = (t * 0.7 + j / 14) % 1
                c.drawCircle(x + 30 + 25 * j, 640 - u * 260, 8 + 4 * u, M.paint(BR, q * (1 - u), stroke=3))
            for j in range(5):
                bacteria(c, x + 60 + 65 * j, 500 + 30 * math.sin(t * 2 + j), 20, q, 40 * j)
        else:
            for j in range(2):
                peixe(c, x + 120 + 150 * j, 500 + 30 * j, 44, q, 1, t)
        E.foco(c, t, ti + 0.2, 0.4, lambda a, x=x, nome=nome: E.escreve(c, nome, x, 740, 44, "g", COR, a))
        E.foco(c, t, ti + 0.5, 0.4, lambda a, x=x, sub=sub: E.escreve(c, sub, x, 800, 40, "i", TINTA2, a))
        if k:
            M.arrow(c, x - 64, 510, x - 8, 510, TINTA2, q, 6, 20)
    E.frase(c, t, C["s13.b"], ps("bactérias com oxigênio de sobra", "i", 52), XE, 920, passo=0.08)
    pilula_em(c, t, C["s13.c"], "gastar o oxigênio aqui, e não no rio", 1300, 1000, 46, E.COR)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14.a"], ps("o atalho:", "i", 66, CLARO) + [("DBO", "g", 70, E.CLARO), ("alta,", "i", 70, CLARO), ("OD", "g", 70, BR), ("baixo", "i", 70, CLARO)], XE, 180, passo=0.12)
        p = ease_io(prog(t, C["s14.a"] + 0.8, 1.5))
        for k, (rot, v, cor) in enumerate((("DBO", lerp(0.2, 0.9, p), E.CLARO), ("OD", lerp(0.9, 0.15, p), BR))):
            x = 660 + 400 * k
            M.rrect(c, x, 300, 140, 560, 30, "#1F2030", 1)
            M.rrect(c, x, 300 + 560 * (1 - v), 140, 560 * v, 30, cor, 1)
            centro(c, rot, x + 70, 930, 64, "g", BR, 1)
        E.frase(c, t, C["s14.b"], ps("a DBO mede o oxigênio que vai ser gasto", "i", 54, CLARO), W / 2, 1010, "center", 0.08)
        return
    E.frase(c, t, C["s15.a"], [("o", "i", 66, CLARO), ("atalho", "i", 66, CLARO), ("falha", "g", 66, ERRADO), ("com", "i", 66, CLARO), ("água", "g", 66, BR), ("quente", "g", 66, "#F5A04A")], W / 2, 360, "center", 0.12)
    E.frase(c, t, C["s15.b"], ps("o OD cai mesmo com a DBO baixa", "i", 62, BR), W / 2, 520, "center", 0.1)
    pilula_em(c, t, C["s15.c"], "o problema é a temperatura, não o esgoto", W / 2, 700, 50, E.COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s16"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    riscado(c, t, C["s16.a"], "DBO alta: muito oxigênio na água", XE, 340, 64)
    E.frase(c, t, C["s16.b"], [("é", "i", 80), ("o", "i", 80), ("contrário", "g", 80, COR)], XE, 500, passo=0.12)
    E.frase(c, t, C["s16.c"], [("demanda", "g", 66, COR), ("=", "g", 66, TINTA2)] + ps("o que as bactérias pedem, não o que a água tem", "i", 56), XE, 660, passo=0.08)
    pilula_em(c, t, C["s16.d"], "DBO alta: muito esgoto e pouco oxigênio", 900, 840, 52, ESGOTO)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s17.a"], [("início:", "i", 60), (f"{OD0} mg/L", "g", 60, COR), ("de", "i", 60), ("oxigênio", "i", 60)], XE, 330, passo=0.1)
    E.frase(c, t, C["s17.b"], [("5", "g", 60), ("dias", "i", 60), ("depois:", "i", 60), (f"{OD5} mg/L", "g", 60, COR)], XE, 440, passo=0.1)
    E.frase(c, t, C["s17.c"], [("1", "g", 60, COR)] + ps("qual é a DBO?", "i", 64), XE, 600, passo=0.1)
    E.frase(c, t, C["s17.d"], [("2", "g", 60, COR)] + ps("o rio está limpo? (limpo: DBO até 3)", "i", 60), XE, 720, passo=0.08)
    if t < C["s18"]:
        Q.erlenmeyer(c, t, C["s17.a"], 1500, 900, 320, 380, 0.6, M.mix(Q.AGUA, ESGOTO, 0.25), graduacao=False)
    else:
        E.relogio(c, t, C["s18.a"], cx=1520, cy=560, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s19.a"], ps("a DBO é o oxigênio que as bactérias gastaram", "i", 58), XE, 240, passo=0.08)
    E.formula_em(c, t, C["s19.b"], f"{OD0} − {OD5} =", 760, 440, 110, "g", TINTA, "right")
    bola_txt(c, t, C["s19.b"] + 0.5, f"{DBO_Q}", 880, 405, 80, 100, ESGOTO)
    E.foco(c, t, C["s19.b"] + 0.8, 0.4, lambda a: E.escreve(c, "mg/L", 990, 440, 70, "g", TINTA, a))
    E.foco(c, t, C["s19.c"], 0.4, lambda a: E.escreve(c, f"= {DBO_Q} ppm", 1200, 440, 70, "g", TINTA2, a))
    E.frase(c, t, C["s20.a"], [(f"{DBO_Q}", "g", 70, ESGOTO), ("é", "i", 66), ("o", "i", 66), ("dobro", "g", 66, ERRADO), ("de", "i", 66), ("3", "g", 70, CERTO)], XE, 640, passo=0.12)
    pilula_em(c, t, C["s20.b"], "o rio está recebendo esgoto", 1300, 620, 50, ESGOTO)
    riscado(c, t, C["s20.c"], f"respondeu {OD5}: mediu o OD do fim, não a DBO", XE, 820, 54)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s21.a", [("peixe", "g", 62), ("depende", "i", 66), ("do", "i", 66), ("OD", "g", 62, COR)]),
                 ("s21.b", [("esgoto", "g", 62, ESGOTO), ("alimenta", "i", 66), ("bactérias", "g", 62), ("que", "i", 66), ("gastam", "i", 66), ("O₂", "g", 62)]),
                 ("s21.c", [("DBO", "g", 62, COR), ("mede", "i", 66), ("esse", "i", 66), ("gasto", "g", 62)]),
                 ("s21.d", [("água", "g", 62), ("quente", "g", 62, ERRADO), ("segura", "i", 66), ("menos", "i", 66), ("oxigênio", "i", 66)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.a"], [("Química", "g", 100, COR), ("verde", "g", 100, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s22.a"] + 0.6, ps("e economia atômica", "i", 80), XE, 520, passo=0.12)
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s22.b"] + 0.2, 0.4))
    E.frase(c, t, C["s22.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, od=b_od, esgoto=b_esgoto, dbo=b_dbo, quente=b_quente, ete=b_ete,
              atalho=b_atalho, erro=b_erro, questao=b_questao, resposta=b_resposta, fim=b_fim)
