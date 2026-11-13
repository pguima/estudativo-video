"""Visual — Estudativo · QUI-AMB-001: combustíveis fósseis e biocombustíveis. Primeira aula da trilha Química e Ambiente.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py). LINGUAGEM VISUAL DA QUÍMICA AMBIENTAL
(todas as aulas QUI-AMB-* copiam daqui):
- FÓSSIL em tinta escura (gota de petróleo FOSSIL, quase preta); BIO na cor da matéria (cana, soja, folha em turquesa).
  Nunca verde puro para "bio": verde é acerto.
- CO₂ sempre como molécula de bola-vareta (Q.molecula "CO2"), cinza-escuro e vermelho; "CO₂ novo" no ar = moléculas que se
  acumulam; o ciclo do carbono = setas curvas na cor da matéria fechando um círculo.
- COMPARAÇÃO de combustíveis = barras deitadas (barra), uma por fala, com o número na ponta; fóssil em tinta, bio em turquesa.
- ATMOSFERA = faixas suaves de azul (ceu) com o chão embaixo; Sol amarelo; luz que chega = setas amarelas retas; calor que
  sai do chão (infravermelho) = setas âmbar onduladas; camada de ozônio = faixa turquesa no alto; poluente = nuvem cinza.
- ÁGUA = Q.AGUA; esgoto = marrom-oliva (ESGOTO); oxigênio dissolvido = bolinhas de O₂ (Q.molecula "O2", pequenas).
- Contas de prova (energia, massa, economia atômica) = E.formula na grotesca, resultado na esfera (bola_txt).
Peças desta aula candidatas ao kit: barra (barra deitada com valor), gota, cana, motor (pistão), esqueleto (fórmula de
linha com ramificações), ciclo_setas.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Química", "Química e Ambiente")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-AMB-001_combustiveis_fosseis_biocombustiveis.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("origem", "energia", "co2", "ciclo", "octanagem", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FOSSIL = "#23242B"

# contas e dados da aula, conferidos aqui
KJ_G = {"octano": round(5471 / 114, 1), "etanol": round(1368 / 46, 1), "biodiesel": 40}
assert KJ_G["octano"] == 48.0 and abs(KJ_G["etanol"] - 29.7) < 0.05
assert Q.lados("C2H6O + 3 O2 -> 2 CO2 + 3 H2O")[0] == Q.lados("C2H6O + 3 O2 -> 2 CO2 + 3 H2O")[1]
assert Q.lados("2 C8H18 + 25 O2 -> 16 CO2 + 18 H2O")[0] == Q.lados("2 C8H18 + 25 O2 -> 16 CO2 + 18 H2O")[1]
assert 8 * 44 == 352 and 2 * 44 == 88 and round(352 / 114, 1) == 3.1 and round(88 / 46, 1) == 1.9
assert round(352 / 5.471) == round(88 / 1.368) == 64          # mesmo CO₂ para a mesma energia
assert 1200 / 48 == 25 and 1200 / 30 == 40 and 40 - 25 == 15  # a questão
assert round(16 / 46 * 100) == 35 and round(32 / 296 * 100) == 11  # fração de O na massa: etanol e oleato de metila


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


def barra(c, t, t0, rot, valor, vmax, x, y, w, h=70, cor=None, txt=None, size=50, d=0.8):
    """barra deitada que cresce: rótulo à esquerda (alinhado à direita em x), valor na ponta"""
    if t < t0:
        return
    q = ep(t, t0, 0.4)
    p = ease_io(prog(t, t0, d))
    E.escreve(c, rot, x - 24 - E.larg(rot, "b", size), y + h / 2 + size * 0.36, size, "b", TINTA, q)
    M.rrect(c, x, y, max(2, w * valor / vmax * p), h, h / 2, cor or E.COR, q)
    E.foco(c, t, t0 + d * 0.8, 0.4, lambda a: E.escreve(c, txt or E._num(valor), x + w * valor / vmax + 24, y + h / 2 + size * 0.36, size, "g", TINTA, a))


def gota(c, cx, cy, s, cor, a=1.0):
    p = skia.Path(); p.moveTo(cx, cy - s)
    p.cubicTo(cx + s * 0.8, cy - s * 0.1, cx + s * 0.7, cy + s * 0.75, cx, cy + s * 0.75)
    p.cubicTo(cx - s * 0.7, cy + s * 0.75, cx - s * 0.8, cy - s * 0.1, cx, cy - s)
    c.drawPath(p, M.paint(cor, a))
    c.drawOval(skia.Rect.MakeXYWH(cx - s * 0.35, cy - s * 0.1, s * 0.22, s * 0.4), M.paint(BR, 0.35 * a))


def cana(c, cx, yb, h, a=1.0, n=3, cor=None):
    cor = cor or E.COR
    for k in range(n):
        x = cx + (k - (n - 1) / 2) * 60
        hh = h * (0.85 + 0.15 * (k % 2))
        for j in range(6):
            y0, y1 = yb - hh * j / 6, yb - hh * (j + 1) / 6
            M.line(c, x, y0, x, y1 + 6, cor, a, 22)
            M.line(c, x - 14, y1 + 6, x + 14, y1 + 6, M.mix(cor, "#000000", 0.3), a, 5)
        for s in (-1, 1):
            p = skia.Path(); p.moveTo(x, yb - hh); p.quadTo(x + s * 80, yb - hh - 60, x + s * 140, yb - hh + 20)
            c.drawPath(p, M.paint(M.mix(cor, BR, 0.2), a, stroke=10))


def esqueleto(c, pts, arestas, cx, cy, s, a=1.0, cor=TINTA, pontos=True):
    """fórmula de linha: pts em unidades, arestas = pares de índices; cada vértice é um carbono"""
    P = [(cx + x * s, cy - y * s) for x, y in pts]
    for i, j in arestas:
        M.line(c, P[i][0], P[i][1], P[j][0], P[j][1], cor, a, 8)
    if pontos:
        for x, y in P:
            E.bola(c, x, y, 11, "#3A3B40", a)
    return P


HEPTANO = ([(k * 0.87, 0.25 if k % 2 else -0.25) for k in range(7)], [(k, k + 1) for k in range(6)])
# 2,2,4-trimetilpentano: cadeia de 5 (0..4), duas metilas no carbono 2 (índice 1) e uma no carbono 4 (índice 3)
ISO = ([(0, -0.25), (0.87, 0.25), (1.74, -0.25), (2.61, 0.25), (3.48, -0.25), (0.87, 1.25), (0.2, 0.9), (2.61, 1.25)],
       [(0, 1), (1, 2), (2, 3), (3, 4), (1, 5), (1, 6), (3, 7)])
assert len(HEPTANO[0]) == 7 and len(ISO[0]) == 8  # C₇H₁₆ e C₈H₁₈


def motor(c, t, cx, cy, comp, a=1.0, faisca=0.0, bate=0.0):
    """cilindro com pistão: comp 0..1 espreme a mistura; faisca = brilho da vela; bate = explosão fora de hora"""
    w, h = 300, 420
    M.rrect(c, cx - w / 2 - 16, cy - h / 2, w + 32, h, 20, "#B9BFC7", a)
    M.rrect(c, cx - w / 2, cy - h / 2 + 30, w, h - 30, 10, "#EEF1F4", a)
    yp = cy + h / 2 - 60 - comp * 220
    mix = M.mix("#FFE7A8", "#F5B400", comp)
    c.drawRect(skia.Rect.MakeLTRB(cx - w / 2, cy - h / 2 + 30, cx + w / 2, yp), M.paint(mix, 0.7 * a))
    M.rrect(c, cx - w / 2 + 6, yp, w - 12, 60, 8, "#6E747C", a)
    M.line(c, cx, yp + 60, cx, cy + h / 2 + 120, "#6E747C", a, 22)
    M.rrect(c, cx - 20, cy - h / 2 - 50, 40, 70, 8, "#2A2B31", a)
    if faisca > 0:
        for k in range(6):
            ang = k * math.tau / 6
            M.line(c, cx, cy - h / 2 + 40, cx + 30 * math.cos(ang), cy - h / 2 + 40 + 30 * math.sin(ang), "#F5B400", faisca * a, 5)
    if bate > 0:
        c.drawCircle(cx, (cy - h / 2 + yp) / 2, 40 + 80 * bate, M.paint(ERRADO, 0.5 * a * (1 - bate * 0.6)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        frases = ((C["s01.a"], "com 1 litro, o etanol rende menos"), (C["s01.b"], "o etanol também solta CO₂"), (C["s01.c"], "e ele é chamado de renovável"))
        for k, (ti, s) in enumerate(frases):
            y = 330 + 190 * k
            E.foco(c, t, ti, 0.5, lambda a, y=y, s=s: (M.rrect(c, XE, y - 70, 1180, 120, 30, BR, a, stroke=3, stroke_color=FIO),
                                                      E.escreve(c, s, XE + 40, y + 12, 60, "b", TINTA, a)))
            E.foco(c, t, C["s01.d"] + 0.3 * k, 0.4, lambda a, y=y: E.selo(c, XE + 1250, y - 10, 46, True, a))
        E.frase(c, t, C["s01.d"], [("as", "i", 80), ("três", "g", 80, COR), ("são", "i", 80), ("verdade", "g", 80)], XE, 960, passo=0.12)
        E.foco(c, t, C["s01.a"], 0.5, lambda a: gota(c, 1680, 400, 120, FOSSIL, a))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: cana(c, 1690, 900, 300, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("gasolina,", "g", 62), ("etanol,", "g", 62), ("biodiesel", "g", 62, COR)]),
                 (C["s02.c"], [("o", "i", 66), ("que", "i", 66), ("é", "i", 66), ("octanagem", "g", 62, COR)]),
                 (C["s02.d"], [("de", "i", 66), ("onde", "i", 66), ("vem", "i", 66), ("o", "i", 66), ("renovável", "g", 62, COR)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("três lembretes", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("gasolina", "g", 64)] + ps("sai do petróleo, na destilação fracionada", "i", 60), XE, 360, passo=0.08)
    E.frase(c, t, C["s03.b"], [("queima", "g", 64)] + ps("é exotérmica:", "i", 60), XE, 520, passo=0.1)
    E.formula_em(c, t, C["s03.b"] + 1.2, "ΔH < 0", XE + 640, 520, 70, "g", COR)
    Q.equacao(c, t, C["s03.c"], "C2H6O + 3 O2 -> 2 CO2 + 3 H2O", W / 2, 760, 90, tl=[C["s03.c"] + 0.3 * k for k in range(8)])
    Q.sob_termos(c, t, "C2H6O + 3 O2 -> 2 CO2 + 3 H2O", W / 2, 760, 90, [["46 g", "", "88 g", ""]], tl=[C["s03.c"] + 2.4])


# ---------------- fóssil × bio ----------------
def b_origem(c, t, C, b):
    E.foco(c, t, C["s04.a"], 0.5, lambda a: gota(c, 500, 480, 170, FOSSIL, a))
    E.frase(c, t, C["s04.a"], [("fóssil", "g", 90, FOSSIL)], 500, 240, "center")
    E.frase(c, t, C["s04.a"] + 0.8, ps("restos enterrados há milhões de anos", "i", 46, TINTA2), 500, 760, "center", 0.06)
    for k, s in enumerate(("petróleo", "gás natural", "carvão")):
        pilula_em(c, t, C["s04.b"] + 0.3 * k, s, 230 + 270 * k, 880, 42, FOSSIL)
    E.foco(c, t, C["s04.c"], 0.5, lambda a: cana(c, 1420, 650, 330, a))
    E.frase(c, t, C["s04.c"], [("bio", "g", 90, COR)], 1420, 240, "center")
    E.frase(c, t, C["s04.c"] + 0.8, ps("plantas e gorduras de hoje", "i", 46, TINTA2), 1420, 760, "center", 0.06)
    pilula_em(c, t, C["s04.d"], "etanol da cana", 1290, 880, 42, E.COR)
    pilula_em(c, t, C["s04.e"], "biodiesel: soja, sebo", 1560, 960, 42, E.COR)
    M.line(c, W / 2, 200, W / 2, 1000, FIO, ep(t, C["s04.c"], 0.5), 3)


# ---------------- energia ----------------
def b_energia(c, t, C, b):
    if t < C["s06"]:
        E.frase(c, t, C["s05"], ps("energia de cada grama queimado", "i", 64, TINTA2), XE, 220, passo=0.1)
        barra(c, t, C["s05.a"], "octano (gasolina)", 48, 50, 700, 360, 1000, cor=FOSSIL, txt="48 kJ/g")
        barra(c, t, C["s05.b"], "biodiesel", 40, 50, 700, 540, 1000, txt="40 kJ/g")
        barra(c, t, C["s05.c"], "etanol", 30, 50, 700, 720, 1000, txt="30 kJ/g")
        E.foco(c, t, C["s05.c"] + 1.0, 0.4, lambda a: E.escreve(c, "kJ: quilojoule, uma unidade de energia", XE, 920, 44, "i", TINTA2, a))
        return
    if t < C["s07"]:
        E.frase(c, t, C["s06"], ps("por que o etanol perde?", "i", 64, TINTA2), XE, 200, passo=0.1)
        Q.formula_em(c, t, C["s06.a"], "C8H18", XE, 400, 130)
        E.foco(c, t, C["s06.b"], 0.5, lambda a: esqueleto(c, *HEPTANO[:0] or ([(k * 0.87, 0.25 if k % 2 else -0.25) for k in range(8)], [(k, k + 1) for k in range(7)]), 1050, 370, 90, a))
        E.frase(c, t, C["s06.b"], ps("só carbono e hidrogênio", "i", 54, TINTA2), XE, 500, passo=0.08)
        Q.formula_em(c, t, C["s06.a"] + 0.4, "C2H6O", XE, 720, 130, cores={"O": E.COR} if t >= C["s06.c"] else None)
        Q.molecula(c, t, C["s06.c"] - 0.3, "C2H6O", 1180, 700, 110, passo=0.08)
        E.frase(c, t, C["s06.c"], ps("já tem um oxigênio", "i", 54, TINTA2), XE, 820, passo=0.08)
        pilula_em(c, t, C["s06.d"], "chega ao motor meio queimado", 1500, 880, 46, E.COR)
        E.foco(c, t, C["s06.e"], 0.4, lambda a: E.escreve(c, "biodiesel: pouco oxigênio numa molécula comprida", XE, 1000, 46, "i", TINTA2, a))
        return
    E.frase(c, t, C["s07.a"], [("1", "g", 90, COR), ("litro", "i", 80)], XE, 330, passo=0.12)
    E.frase(c, t, C["s07.a"] + 0.6, ps("de etanol: menos quilômetros", "i", 64), XE + 330, 330, passo=0.1)
    barra(c, t, C["s07.a"] + 1.2, "gasolina", 100, 100, 600, 450, 900, cor=FOSSIL, txt="mais km")
    barra(c, t, C["s07.a"] + 1.6, "etanol", 70, 100, 600, 590, 900, txt="menos km")
    E.frase(c, t, C["s07.b"], ps("a regra do posto:", "i", 64, TINTA2), XE, 820, passo=0.1)
    E.frase(c, t, C["s07.c"], [("etanol", "g", 66), ("até", "i", 66), ("70%", "g", 66, COR)] + ps("do preço da gasolina", "i", 66), XE, 940, passo=0.1)


# ---------------- CO₂ ----------------
def b_co2(c, t, C, b):
    if t < C["s09"]:
        Q.equacao(c, t, C["s08.a"], "C2H6O + 3 O2 -> 2 CO2 + 3 H2O", W / 2, 300, 84, tl=[C["s08.a"] + 0.25 * k for k in range(8)])
        Q.sob_termos(c, t, "C2H6O + 3 O2 -> 2 CO2 + 3 H2O", W / 2, 300, 84, [["46 g", "", "88 g", ""]], tl=[C["s08.a"] + 1.4])
        pilula_em(c, t, C["s08.b"], "quase 2 g de CO₂ por grama", 960, 520, 46, E.COR)
        Q.formula_em(c, t, C["s08.c"], "C8H18 -> 8 CO2", W / 2, 720, 96, align="center")
        E.foco(c, t, C["s08.c"] + 0.8, 0.4, lambda a: (centro(c, "114 g", W / 2 - 300, 820, 50, "b", TINTA2, a)))
        E.foco(c, t, C["s08.d"], 0.4, lambda a: centro(c, "352 g", W / 2 + 230, 820, 50, "b", TINTA2, a))
        pilula_em(c, t, C["s08.d"] + 1.0, "mais de 3 g de CO₂ por grama", 960, 950, 46, FOSSIL)
        return
    E.frase(c, t, C["s09.a"], ps("por grama queimado:", "i", 60, TINTA2), XE, 210, passo=0.1)
    barra(c, t, C["s09.a"], "gasolina", 3.1, 3.5, 600, 280, 900, h=60, cor=FOSSIL, txt="3,1 g de CO₂")
    barra(c, t, C["s09.a"] + 0.4, "etanol", 1.9, 3.5, 600, 380, 900, h=60, txt="1,9 g de CO₂")
    E.frase(c, t, C["s09.b"], ps("mas a gasolina também dá mais energia", "i", 56), XE, 560, passo=0.08)
    E.frase(c, t, C["s09.c"], ps("para a mesma energia:", "i", 60, TINTA2), XE, 680, passo=0.1)
    barra(c, t, C["s09.c"] + 0.6, "gasolina", 64, 80, 600, 740, 900, h=60, cor=FOSSIL, txt="quase o mesmo CO₂")
    barra(c, t, C["s09.c"] + 1.0, "etanol", 64, 80, 600, 840, 900, h=60, txt="quase o mesmo CO₂")
    E.frase(c, t, C["s09.d"], ps("a diferença não está no escapamento:", "i", 50, TINTA2), XE, 1000, passo=0.06)
    E.frase(c, t, C["s09.e"], [("está", "i", 54), ("na", "i", 54), ("origem", "g", 54, COR), ("do", "i", 54), ("carbono", "g", 54, COR)], 1060, 1000, passo=0.1)


# ---------------- ciclo do carbono ----------------
def seta_curva(c, t, t0, cx, cy, r, a0, a1, cor=None, d=0.8, largura=8):
    if t < t0:
        return
    p = ease_io(prog(t, t0, d))
    am = a0 + (a1 - a0) * p
    E.arco(c, cx, cy, r, a0, am - a0, cor or E.COR, largura, 1.0)
    ang = math.radians(am)
    x, y = cx + r * math.cos(ang), cy + r * math.sin(ang)
    sg = 1 if a1 > a0 else -1
    tx, ty = -math.sin(ang) * sg, math.cos(ang) * sg
    pth = skia.Path(); pth.moveTo(x + tx * 22, y + ty * 22)
    pth.lineTo(x - tx * 6 + math.cos(ang) * 16, y - ty * 6 + math.sin(ang) * 16); pth.lineTo(x - tx * 6 - math.cos(ang) * 16, y - ty * 6 - math.sin(ang) * 16); pth.close()
    c.drawPath(pth, M.paint(cor or E.COR, 1))


def b_ciclo(c, t, C, b):
    if t < C["s11"]:
        cx, cy, r = 960, 600, 330
        Q.molecula(c, t, C["s10.a"], "CO2", cx, cy - r - 10, 90, passo=0.15)
        E.foco(c, t, C["s10.a"], 0.4, lambda a: E.escreve(c, "CO₂ do ar", cx + 160, cy - r + 10, 50, "b", TINTA, a))
        E.foco(c, t, C["s10.a"], 0.5, lambda a: cana(c, cx - r - 20, cy + 260, 260, a))
        seta_curva(c, t, C["s10.a"] + 0.4, cx, cy, r, -100, -200)
        pilula_em(c, t, C["s10.b"], "fotossíntese: outra aula, na Biologia", cx - 340, cy - 60, 40, TINTA2, "b")
        E.foco(c, t, C["s10.c"], 0.4, lambda a: (gota(c, cx + r + 10, cy + 160, 90, E.COR, a), E.escreve(c, "etanol queimando", cx + r - 120, cy + 320, 46, "b", TINTA, a)))
        seta_curva(c, t, C["s10.c"] + 0.3, cx, cy, r, 20, -80)
        seta_curva(c, t, C["s10.d"], cx, cy, r, 160, 60)
        E.foco(c, t, C["s10.d"] + 0.3, 0.4, lambda a: E.escreve(c, "próxima safra", cx - 150, cy + r + 80, 46, "i", TINTA2, a))
        return
    if t < C["s12"]:
        c.drawRect(skia.Rect.MakeLTRB(0, 760, W, H), M.paint("#B8A88F", ep(t, C["s11"], 0.5)))
        E.foco(c, t, C["s11.a"], 0.5, lambda a: gota(c, 600, 900, 110, FOSSIL, a))
        E.frase(c, t, C["s11.a"], ps("o carbono do petróleo: milhões de anos debaixo da terra", "i", 52, TINTA2), XE, 200, passo=0.06)
        if t >= C["s11.b"]:
            q = ease_io(prog(t, C["s11.b"], 1.0))
            M.arrow(c, 600, 800, 600, lerp(800, 470, q), FOSSIL, 1, 10, 30)
            for k in range(int(1 + 8 * ep(t, C["s11.b"] + 0.5, 3.0))):
                Q.molecula_desenho(c, "CO2", 900 + 160 * (k % 5), 380 + 120 * (k // 5) + 6 * math.sin(t + k), 60, 1, giro=20 * k)
            E.foco(c, t, C["s11.b"] + 0.6, 0.4, lambda a: E.escreve(c, "CO₂ novo, que se soma", 900, 640, 54, "g", FOSSIL, a))
        pilula_em(c, t, C["s11.c"], "renovável: o bio fecha o ciclo do carbono", W / 2, 1010, 46, E.COR)
        return
    E.frase(c, t, C["s12.a"], [("só", "i", 90), ("em", "i", 90), ("parte", "g", 90, COR)], XE, 300, passo=0.12)
    for k, s in enumerate(("plantar", "adubar", "colher", "transportar", "destilar")):
        pilula_em(c, t, C["s12.b"] + 0.3 * k, s, XE + 130 + 300 * k, 500, 46, TINTA)
        E.foco(c, t, C["s12.b"] + 0.3 * k + 0.4, 0.4, lambda a, k=k: Q.molecula_desenho(c, "CO2", XE + 130 + 300 * k, 610, 50, a))
    E.frase(c, t, C["s12.b"] + 1.8, ps("gastam energia, quase sempre fóssil", "i", 56, TINTA2), XE, 760, passo=0.08)
    pilula_em(c, t, C["s12.c"], "renovável não quer dizer emissão zero", W / 2, 920, 56, E.COR)


# ---------------- octanagem ----------------
def b_octanagem(c, t, C, b):
    if t < C["s14"]:
        comp = 0.5 + 0.5 * math.sin(t * 2.4) if t >= C["s13.a"] else 0
        bate = ep(t, C["s13.b"], 0.3) * (1 - ep(t, C["s13.b"] + 1.2, 0.4))
        E.foco(c, t, C["s13"], 0.5, lambda a: motor(c, t, 1450, 500, comp, a, 0, bate))
        E.frase(c, t, C["s13"], [("octanagem", "g", 96, COR)], XE, 220)
        E.frase(c, t, C["s13.a"], ps("o pistão espreme a mistura", "i", 58), XE, 380, passo=0.08)
        E.frase(c, t, C["s13.b"], ps("explodiu antes da faísca:", "i", 58), XE, 500, passo=0.08)
        E.frase(c, t, C["s13.b"] + 1.0, [("o", "i", 62), ("motor", "i", 62), ("bate", "g", 62, ERRADO)], XE, 600, passo=0.1)
        E.frase(c, t, C["s13.c"], ps("octanagem: quanto aguenta ser espremido", "i", 54), XE, 780, passo=0.06)
        E.frase(c, t, C["s13.c"] + 1.6, ps("sem explodir antes da hora", "i", 54), XE, 860, passo=0.06)
        return
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("a escala tem dois padrões", "i", 60, TINTA2), XE, 200, passo=0.1)
        E.foco(c, t, C["s14.a"], 0.5, lambda a: esqueleto(c, *HEPTANO, 300, 480, 90, a))
        E.frase(c, t, C["s14.a"], [("heptano", "g", 64)], 560, 640, "center")
        E.foco(c, t, C["s14.a"] + 0.6, 0.4, lambda a: E.escreve(c, "cadeia reta: explode fácil", 330, 720, 44, "i", TINTA2, a))
        bola_txt(c, t, C["s14.a"] + 1.0, "0", 560, 860, 70, 80, ERRADO)
        E.foco(c, t, C["s14.b"], 0.5, lambda a: esqueleto(c, *ISO, 1230, 500, 100, a))
        E.frase(c, t, C["s14.b"], [("isoctano", "g", 64)], 1420, 640, "center")
        E.foco(c, t, C["s14.b"] + 0.6, 0.4, lambda a: E.escreve(c, "2,2,4-trimetilpentano: ramificado", 1150, 720, 44, "i", TINTA2, a))
        bola_txt(c, t, C["s14.b"] + 1.2, "100", 1420, 860, 70, 64, CERTO)
        pilula_em(c, t, C["s14.c"], "ramificação resiste; cadeia reta detona", W / 2, 1010, 46, E.COR)
        return
    E.frase(c, t, C["s15.a"], [("etanol:", "g", 80), ("octanagem", "g", 80, COR), ("alta", "g", 80, COR)], XE, 360, passo=0.12)
    E.frase(c, t, C["s15.b"], ps("um dos motivos para a gasolina do Brasil levar etanol", "i", 52), XE, 520, passo=0.06)
    E.foco(c, t, C["s15.c"], 0.5, lambda a: (E.bola(c, 960, 780, 140, a=a), centro(c, "~30%", 960, 805, 80, "g", E.SOBRE, a)))
    E.foco(c, t, C["s15.c"] + 0.4, 0.4, lambda a: E.escreve(c, "de etanol na gasolina, desde 2025", 1130, 800, 48, "b", TINTA2, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s16"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    riscado(c, t, C["s16.a"], "octanagem mede energia", XE, 340, 64)
    E.frase(c, t, C["s16.b"], [("não", "g", 80, ERRADO), ("mede", "i", 80)], XE, 480, passo=0.12)
    E.frase(c, t, C["s16.c"], ps("octanagem:", "i", 54, TINTA2), XE, 620, passo=0.1)
    barra(c, t, C["s16.c"] + 0.3, "gasolina", 85, 110, 640, 650, 800, h=56, cor=FOSSIL, txt="menor", size=46)
    barra(c, t, C["s16.c"] + 0.6, "etanol", 105, 110, 640, 730, 800, h=56, txt="maior", size=46)
    E.frase(c, t, C["s16.c"] + 1.4, ps("energia por grama:", "i", 54, TINTA2), XE, 870, passo=0.1)
    barra(c, t, C["s16.c"] + 1.8, "gasolina", 48, 60, 640, 890, 800, h=56, cor=FOSSIL, txt="48", size=46)
    barra(c, t, C["s16.c"] + 2.1, "etanol", 30, 60, 640, 970, 800, h=56, txt="30", size=46)
    pilula_em(c, t, C["s16.d"], "resistência, não força", 1550, 480, 50, E.COR)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s18"]:
        E.frase(c, t, C["s17"], ps("o atalho:", "i", 66, CLARO) + [("quanto", "i", 66, CLARO), ("da", "i", 66, CLARO), ("massa", "g", 62, BR), ("é", "i", 66, CLARO), ("oxigênio?", "g", 62, E.CLARO)], XE, 160, passo=0.1)
        E.frase(c, t, C["s17.b"], [("mais", "g", 62, BR), ("oxigênio,", "i", 66, CLARO), ("menos", "g", 62, BR), ("energia", "i", 66, CLARO), ("por", "i", 66, CLARO), ("grama", "i", 66, CLARO)], XE, 280, passo=0.1)
        linhas = (("etanol", 35, "30 kJ/g"), ("biodiesel", 11, "40 kJ/g"), ("octano", 0, "48 kJ/g"))
        for k, (nome, pct, en) in enumerate(linhas):
            y = 430 + 150 * k
            ti = C["s17.c"] + 0.6 * k
            E.foco(c, t, ti, 0.4, lambda a, y=y, nome=nome: E.escreve(c, nome, XE, y + 50, 56, "g", BR, a))
            if t >= ti:
                p = ease_io(prog(t, ti, 0.6))
                M.rrect(c, 560, y, 700, 64, 32, "#1F2030", 1)
                if pct:
                    M.rrect(c, 560, y, 700 * pct / 40 * p, 64, 32, E.CLARO, 1)
                E.foco(c, t, ti + 0.4, 0.4, lambda a, y=y, pct=pct, en=en: (E.escreve(c, f"{pct}% oxigênio", 1290, y + 48, 48, "b", E.CLARO, a),
                                                                           E.escreve(c, en, 1660, y + 48, 48, "g", BR, a)))
        E.frase(c, t, C["s17.d"], ps("funciona porque essa parte já está queimada", "i", 54, CLARO), XE, 950, passo=0.08)
        return
    E.frase(c, t, C["s18.a"], [("não", "g", 66, ERRADO), ("compensa:", "i", 70, CLARO)] + ps("comparar por mol ou por litro", "i", 70, CLARO), W / 2, 420, "center", 0.1)
    E.frase(c, t, C["s18.b"], ps("a ordem pode mudar: use os números da questão", "i", 62, BR), W / 2, 600, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s19.a"], [("gasolina:", "g", 60), ("48 kJ/g", "g", 60, COR), ("etanol:", "g", 60), ("30 kJ/g", "g", 60, COR)], XE, 340, passo=0.12)
    E.frase(c, t, C["s19.b"], [("quantos", "i", 66), ("gramas", "i", 66), ("de", "i", 66), ("cada", "i", 66), ("dão", "i", 66), ("1.200 kJ?", "g", 66, COR)], XE, 520, passo=0.1)
    E.frase(c, t, C["s19.c"], ps("o que explica a diferença?", "i", 64), XE, 660, passo=0.1)
    if t >= C["s20"]:
        E.relogio(c, t, C["s20.a"], cx=1470, cy=640, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s21.a"], "gasolina: 1200 ÷ 48 =", 1100, 330, 80, "g", TINTA, "right")
    bola_txt(c, t, C["s21.b"], "25 g", 1290, 300, 90, 64, FOSSIL)
    E.formula_em(c, t, C["s21.c"], "etanol: 1200 ÷ 30 =", 1100, 560, 80, "g", TINTA, "right")
    bola_txt(c, t, C["s21.d"], "40 g", 1290, 530, 90, 64)
    E.frase(c, t, C["s22.a"], ps("para a mesma energia: 15 g a mais de etanol", "i", 56), XE, 760, passo=0.08)
    pilula_em(c, t, C["s22.b"], "o oxigênio que ele já traz", 620, 870, 50, E.COR)
    riscado(c, t, C["s22.c"], "1200 × 48: número enorme, sem sentido", XE, 1010, 50)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s23.a", [("gasolina:", "g", 62), ("mais", "i", 66), ("energia", "g", 62, COR), ("por", "i", 66), ("grama", "i", 66)]),
                 ("s23.b", [("todos", "i", 66), ("soltam", "i", 66), ("CO₂", "g", 62, COR)]),
                 ("s23.c", [("bio:", "g", 62), ("a", "i", 66), ("planta", "g", 62, COR), ("retira", "i", 66), ("o", "i", 66), ("carbono", "i", 66), ("do", "i", 66), ("ar", "i", 66)]),
                 ("s23.d", [("octanagem", "g", 62), ("=", "g", 62, TINTA2), ("resistência,", "i", 66), ("não", "i", 66), ("energia", "i", 66)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s24.a"], [("Poluentes", "g", 100, COR), ("do", "i", 100), ("ar", "g", 100, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s24.a"] + 0.6, ps("e chuva ácida", "i", 80), XE, 520, passo=0.12)
    for k in range(5):
        E.foco(c, t, C["s24.a"] + 0.8 + 0.1 * k, 0.5, lambda a, k=k: E.bola(c, 300 + 90 * k, 720 - 20 * (k % 2), 60 - 4 * k, "#8A8D94", a))
    E.foco(c, t, C["s24.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s24.b"] + 0.2, 0.4))
    E.frase(c, t, C["s24.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, origem=b_origem, energia=b_energia, co2=b_co2, ciclo=b_ciclo,
              octanagem=b_octanagem, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
