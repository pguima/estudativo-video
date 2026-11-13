"""Visual — Estudativo · QUI-AMB-002: poluentes do ar e chuva ácida.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a LINGUAGEM VISUAL DA QUÍMICA AMBIENTAL
(cabeçalho de QUI-AMB-001/roteiro/visual.py). Nesta aula:
- cada POLUENTE é um cartão (cartao): a fórmula grande (Q.formula), a origem com um ícone pequeno e o efeito embaixo;
- pH = Q.escala_ph, com a marca da chuva natural (5,6) em tinta e a faixa abaixo de 5,6 riscada de vermelho claro;
- reação da chuva = Q.equacao no tempo da fala, o ácido formado na cor da matéria;
- mármore = estátua branca-acinzentada (estatua) que perde detalhes (gasto 0..1), com bolhas de CO₂ saindo.
Peças candidatas ao kit: nuvem, chamine, cartao (cartão de poluente), estatua, gota_chuva, marca_ph.
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
ARQUIVO_FINAL = "estudativo_QUI-AMB-002_poluentes_e_chuva_acida.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("poluentes", "chuva", "sulfurico", "marmore", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FUMACA = "#8A8D94"

EQS = ["N2 + O2 -> 2 NO", "2 NO + O2 -> 2 NO2", "S + O2 -> SO2", "2 CO + 2 NO -> 2 CO2 + N2", "2 CO + O2 -> 2 CO2",
       "2 SO2 + O2 -> 2 SO3", "SO3 + H2O -> H2SO4", "CO2 + H2O -> H2CO3", "4 NO2 + O2 + 2 H2O -> 4 HNO3",
       "CaCO3 + H2SO4 -> CaSO4 + H2O + CO2"]
for e in EQS:
    r, p = Q.lados(e)
    assert r == p, e
assert {k: Q.contar("SO3").get(k, 0) + Q.contar("H2O").get(k, 0) for k in "HSO"} == Q.contar("H2SO4")  # o atalho: somar a água
assert 4.5 < 5.6 < 7


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


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


def nuvem(c, cx, cy, s, cor=FUMACA, a=1.0, t=0.0):
    for k, (dx, dy, r) in enumerate(((-0.6, 0.1, 0.45), (-0.15, -0.2, 0.6), (0.4, -0.05, 0.5), (0.8, 0.15, 0.35), (0.1, 0.2, 0.5))):
        c.drawCircle(cx + dx * s + 4 * math.sin(t + k), cy + dy * s, r * s, M.paint(cor, 0.85 * a))


def chamine(c, t, x, yb, a=1.0, cor=FUMACA):
    M.rrect(c, x, yb - 260, 70, 260, 6, "#7A4A3A", a)
    M.rrect(c, x - 160, yb - 140, 170, 140, 6, "#9A6A55", a)
    for k in range(4):
        u = (t * 0.25 + k / 4) % 1
        nuvem(c, x + 35 + u * 120, yb - 300 - u * 220, 40 + 50 * u, cor, a * (1 - u))


def cartao(c, t, t0, x, y, w, h, formula, origem, efeito, icone=None):
    if t < t0:
        return
    q = ep(t, t0, 0.5)
    M.rrect(c, x, y, w, h, 30, BR, q, stroke=3, stroke_color=FIO)
    Q.formula(c, formula, x + 40, y + 140, 120, TINTA, q)
    E.foco(c, t, t0 + 0.6, 0.4, lambda a: E.escreve(c, origem, x + 40, y + 230, 44, "b", TINTA2, a))
    E.foco(c, t, t0 + 1.4, 0.4, lambda a: E.escreve(c, efeito, x + 40, y + 300, 44, "b", COR, a))
    if icone:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: icone(c, x + w - 150, y + 110, a))


def ic_carro(c, cx, cy, a):
    M.rrect(c, cx - 100, cy - 10, 200, 60, 20, "#4A5568", a)
    M.rrect(c, cx - 60, cy - 50, 120, 50, 18, "#4A5568", a)
    for dx in (-60, 60):
        c.drawCircle(cx + dx, cy + 52, 22, M.paint("#2A2B31", a))
    nuvem(c, cx + 140, cy + 30, 30, FUMACA, a)


def ic_motor(c, cx, cy, a):
    M.rrect(c, cx - 70, cy - 70, 140, 140, 16, "#B9BFC7", a)
    for k in range(3):
        M.line(c, cx - 40 + 40 * k, cy - 50, cx - 40 + 40 * k, cy + 50, "#F28C28", a, 6)
    E.escreve(c, "ar quente", cx - 90, cy + 110, 36, "b", TINTA2, a)


def ic_carvao(c, cx, cy, a):
    rnd = random.Random(4)
    for k in range(7):
        x, y = cx + (rnd.random() - 0.5) * 140, cy + (rnd.random() - 0.5) * 70
        p = skia.Path(); p.moveTo(x - 24, y); p.lineTo(x - 8, y - 22); p.lineTo(x + 20, y - 16); p.lineTo(x + 26, y + 10); p.lineTo(x - 6, y + 22); p.close()
        c.drawPath(p, M.paint("#2A2B31", a))
    Q.atomo(c, cx + 80, cy - 60, 26, "S", a)


def ic_fuligem(c, cx, cy, a):
    rnd = random.Random(7)
    for k in range(40):
        c.drawCircle(cx + (rnd.random() - 0.5) * 180, cy + (rnd.random() - 0.5) * 120, 3 + 4 * rnd.random(), M.paint("#3A3B40", a * 0.8))


def gota_chuva(c, cx, cy, s, cor="#9FD3E6", a=1.0):
    p = skia.Path(); p.moveTo(cx, cy - s)
    p.cubicTo(cx + s * 0.8, cy - s * 0.1, cx + s * 0.7, cy + s * 0.75, cx, cy + s * 0.75)
    p.cubicTo(cx - s * 0.7, cy + s * 0.75, cx - s * 0.8, cy - s * 0.1, cx, cy - s)
    c.drawPath(p, M.paint(cor, a)); c.drawPath(p, M.paint("#5FA8C4", a, stroke=4))


def chuva(c, t, x0, x1, y0, y1, a=1.0, n=22, cor="#7FB8D6"):
    rnd = random.Random(2)
    for k in range(n):
        x = x0 + rnd.random() * (x1 - x0)
        u = (t * 0.9 + rnd.random()) % 1
        y = lerp(y0, y1, u)
        M.line(c, x, y, x - 8, y + 34, cor, a * 0.8, 4)


def escala(c, t, t0, x, y, w, marcas=(), ta=None):
    """escala de pH de 0 a 14 com marcas [(pH, texto, instante)] e a faixa ácida da chuva (ta)"""
    Q.escala_ph(c, t, t0, x, y, w, 64)
    X = lambda ph: x + w * ph / 14
    if ta is not None and t >= ta:
        q = ep(t, ta, 0.5)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x - 6, y - 14, X(5.6), y + 78), 18, 18), M.paint(ERRADO, q, stroke=6))
        E.foco(c, t, ta + 0.3, 0.4, lambda a: E.escreve(c, "chuva ácida", x, y - 30, 46, "g", ERRADO, a))
    for m in marcas:
        ph, s, ti = m[:3]
        dy = m[3] if len(m) > 3 else 0
        if t < ti:
            continue
        q = ep(t, ti, 0.4)
        M.arrow(c, X(ph), y + 170 + dy, X(ph), y + 80, TINTA, q, 6, 20)
        E.foco(c, t, ti, 0.4, lambda a, ph=ph, s=s, dy=dy: centro(c, s, X(ph), y + 220 + dy, 46, "g", TINTA, a))


def estatua(c, cx, yb, s, gasto=0.0, a=1.0):
    """busto de mármore: gasto 0..1 tira o nariz e os detalhes"""
    if a <= 0:
        return
    marm = "#E9E7E2"
    M.rrect(c, cx - s * 0.7, yb - s * 0.5, s * 1.4, s * 0.5, 10, "#CFCBC2", a)
    p = skia.Path(); p.moveTo(cx - s * 0.55, yb - s * 0.5); p.lineTo(cx - s * 0.3, yb - s * 1.25); p.lineTo(cx + s * 0.3, yb - s * 1.25); p.lineTo(cx + s * 0.55, yb - s * 0.5); p.close()
    c.drawPath(p, M.paint(marm, a)); c.drawPath(p, M.paint("#B8B3A8", a, stroke=3))
    hx, hy, hr = cx, yb - s * 1.6, s * 0.38
    c.drawCircle(hx, hy, hr, M.paint(marm, a)); c.drawCircle(hx, hy, hr, M.paint("#B8B3A8", a, stroke=3))
    nariz = 1 - gasto
    if nariz > 0:
        pn = skia.Path(); pn.moveTo(hx + hr * 0.1, hy - hr * 0.2); pn.lineTo(hx + hr * (0.1 + 0.45 * nariz), hy + hr * 0.15); pn.lineTo(hx + hr * 0.1, hy + hr * 0.2); pn.close()
        c.drawPath(pn, M.paint("#D8D4CB", a))
    for k in range(3):
        M.line(c, hx - hr * 0.7 + k * hr * 0.4, hy - hr * 0.85, hx - hr * 0.5 + k * hr * 0.4, hy - hr * 0.55, "#B8B3A8", a * (1 - gasto), 6)
    rnd = random.Random(3)
    for k in range(int(14 * gasto)):
        c.drawCircle(cx + (rnd.random() - 0.5) * s, yb - s * (0.5 + rnd.random() * 1.4), 5 + 6 * rnd.random(), M.paint("#C9C3B6", a))


def bolhas_co2(c, t, cx, cy, a=1.0):
    for k in range(5):
        u = (t * 0.5 + k / 5) % 1
        Q.molecula_desenho(c, "CO2", cx + 30 * math.sin(k + t), cy - u * 200, 30, a * (1 - u))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("toda", "i", 100), ("chuva", "g", 100, COR), ("é", "i", 100), ("ácida", "g", 100)], XE, 260, passo=0.14)
        E.frase(c, t, C["s01.b"], ps("até a chuva sem poluição nenhuma", "i", 60, TINTA2), XE, 380, passo=0.08)
        escala(c, t, C["s01.b"], 260, 560, 1400, [(5.6, "chuva limpa: 5,6", C["s01.b"] + 1.0), (7, "água pura: 7", C["s01.c"], 70)])
        E.foco(c, t, C["s01.a"] + 0.4, 0.5, lambda a: (gota_chuva(c, 1650, 280, 90, a=a)))
        E.frase(c, t, C["s01.d"], ps("então, o que é chuva ácida?", "i", 72, COR), W / 2, 1000, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("de", "i", 66), ("onde", "i", 66), ("vem", "i", 66), ("cada", "i", 66), ("poluente", "g", 62, COR)]),
                 (C["s02.c"], [("como", "i", 66), ("a", "i", 66), ("chuva", "g", 62), ("vira", "i", 66), ("ácido", "g", 62, COR)]),
                 (C["s02.d"], [("o", "i", 66), ("mármore", "g", 62, COR), ("se", "i", 66), ("desgastando", "i", 66)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("três lembretes", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("pH", "g", 76, COR), ("<", "g", 76, TINTA2), ("7", "g", 76), ("=", "g", 76, TINTA2), ("ácido", "g", 76)], XE, 380, passo=0.12)
    E.frase(c, t, C["s03.b"], [("óxido", "g", 70), ("ácido", "g", 70, COR), ("+", "g", 70, TINTA2), ("água", "g", 70), ("→", "g", 70, TINTA2), ("ácido", "g", 70, COR)], XE, 570, passo=0.12)
    E.frase(c, t, C["s03.c"], ps("combustão incompleta, com pouco oxigênio, solta", "i", 58), XE, 760, passo=0.08)
    Q.formula_em(c, t, C["s03.c"] + 2.0, "CO", XE + 1260, 770, 110, cores={"CO": E.COR})


# ---------------- poluentes ----------------
POS = [(90, 130), (990, 130), (90, 580), (990, 580)]


def b_poluentes(c, t, C, b):
    if t < C["s08"]:
        def grade():
            cartao(c, t, C["s04.a"], *POS[0], 840, 400, "CO", "queima com pouco oxigênio", "toma o lugar do O₂ no sangue", ic_carro)
            cartao(c, t, C["s05.a"], *POS[1], 840, 400, "NO + NO2", "o N₂ e o O₂ do próprio ar", "no motor quentíssimo", ic_motor)
            cartao(c, t, C["s06.a"], *POS[2], 840, 400, "SO2", "o enxofre do carvão e do diesel", "S + O₂ → SO₂", ic_carvao)
            cartao(c, t, C["s07.a"], *POS[3], 840, 400, "", "fuligem e poeira fina", "entra fundo no pulmão", ic_fuligem)
            E.foco(c, t, C["s07.a"], 0.4, lambda a: E.escreve(c, "material particulado", POS[3][0] + 40, POS[3][1] + 130, 60, "g", TINTA, a))
            if C["s04.c"] <= t < C["s05"] + 2:
                E.foco(c, t, C["s04.c"] + 0.8, 0.4, lambda a: E.escreve(c, "sem cheiro e sem cor", POS[0][0] + 40, POS[0][1] + 365, 40, "b", ERRADO, a))
            if C["s05.b"] <= t < C["s06"]:
                pilula_em(c, t, C["s05.c"], "vem do ar, não do combustível", 1410, 530, 40, ERRADO, "b")
        E.saida(c, t, C["s08"] - 0.1, grade)
        return
    E.frase(c, t, C["s08.a"], [("o", "i", 80), ("catalisador", "g", 80, COR), ("do", "i", 80), ("escapamento", "i", 80)], XE, 260, passo=0.12)
    E.foco(c, t, C["s08.a"] + 0.4, 0.5, lambda a: (M.rrect(c, 1380, 140, 380, 220, 30, "#B9BFC7", a),
                                                  [c.drawCircle(1420 + 40 * (k % 8), 180 + 40 * (k // 8), 14, M.paint("#6E747C", a)) for k in range(32)]))
    Q.equacao(c, t, C["s08.b"], "2 CO + 2 NO -> 2 CO2 + N2", W / 2, 600, 96, tl=[C["s08.b"] + 0.3 * k for k in range(6)], cores={"CO2": E.COR, "N2": E.COR})
    E.foco(c, t, C["s08.b"] + 2.4, 0.4, lambda a: centro(c, "gases bem menos perigosos para a saúde", W / 2, 760, 52, "i", TINTA2, a))


# ---------------- chuva natural ----------------
def b_chuva(c, t, C, b):
    E.foco(c, t, C["s09"], 0.4, lambda a: chuva(c, t, 1200, 1800, 120, 520, a))
    Q.molecula(c, t, C["s09.a"], "CO2", 1300, 220, 90)
    E.frase(c, t, C["s09.a"], [("o", "i", 70), ("ar", "i", 70), ("sempre", "i", 70), ("teve", "i", 70)], XE, 220, passo=0.12)
    Q.formula_em(c, t, C["s09.a"] + 0.8, "CO2", XE + 600, 220, 90)
    E.foco(c, t, C["s09.a"] + 1.2, 0.4, lambda a: E.escreve(c, "um óxido ácido", XE, 300, 50, "i", TINTA2, a))
    Q.equacao(c, t, C["s09.b"], "CO2 + H2O <=> H2CO3", 760, 470, 96, tl=[C["s09.b"], C["s09.b"] + 0.3, C["s09.b"] + 0.6, C["s09.c"] - 0.4, C["s09.c"]], cores={"H2CO3": E.COR})
    E.foco(c, t, C["s09.c"] + 0.6, 0.4, lambda a: centro(c, "ácido carbônico: fraco", 1100, 560, 44, "b", COR, a))
    escala(c, t, C["s09.d"] - 0.5, 260, 700, 1400, [(5.6, "natural: 5,6", C["s09.d"])], ta=C["s10.a"])
    E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "quem empurra para baixo:", 260, 1040, 46, "i", TINTA2, a))
    Q.formula_em(c, t, C["s10.c"], "SO2", 860, 1045, 70, cores={"SO2": ERRADO})
    E.foco(c, t, C["s10.c"] + 0.3, 0.4, lambda a: E.escreve(c, "e os NOₓ", 1060, 1040, 50, "g", ERRADO, a))


# ---------------- ácido sulfúrico ----------------
def b_sulfurico(c, t, C, b):
    E.frase(c, t, C["s11"], ps("o caminho do enxofre: dois passos", "i", 62, TINTA2), XE, 180, passo=0.1)
    Q.equacao(c, t, C["s11.a"], "2 SO2 + O2 -> 2 SO3", W / 2, 360, 96, tl=[C["s11.a"] + 0.3 * k for k in range(4)])
    Q.equacao(c, t, C["s11.b"], "SO3 + H2O -> H2SO4", W / 2, 580, 130, tl=[C["s11.b"], C["s11.c"] - 0.6, C["s11.c"] - 0.3, C["s11.c"], C["s11.c"] + 0.6], cores={"H2SO4": E.COR})
    pilula_em(c, t, C["s11.d"], "ácido sulfúrico: forte", 1380, 700, 50, E.COR)
    if t >= C["s12"]:
        E.frase(c, t, C["s12.a"], ps("com o nitrogênio, parecido:", "i", 56, TINTA2), XE, 850, passo=0.08)
        Q.formula_em(c, t, C["s12.b"], "4 NO2 + O2 + 2 H2O -> 4 HNO3", 1250, 860, 72, align="center", cores={"HNO3": E.COR})
        pilula_em(c, t, C["s12.c"], "ácido nítrico: também forte", 1250, 980, 44, E.COR)


# ---------------- mármore ----------------
def b_marmore(c, t, C, b):
    gasto = ep(t, C["s14.a"], 4.0)
    E.foco(c, t, C["s13"], 0.5, lambda a: estatua(c, 1500, 960, 300, gasto, a))
    E.foco(c, t, C["s13"], 0.4, lambda a: chuva(c, t, 1200, 1800, 80, 900, a, 18, "#E5484D"))
    E.frase(c, t, C["s13.a"], [("mármore", "g", 90, COR)], XE, 220)
    Q.formula_em(c, t, C["s13.a"] + 0.6, "CaCO3", XE, 380, 110)
    E.foco(c, t, C["s13.a"] + 1.0, 0.4, lambda a: E.escreve(c, "carbonato de cálcio", XE + 420, 370, 48, "i", TINTA2, a))
    Q.formula_em(c, t, C["s13.b"], "CaCO3 + H2SO4 -> CaSO4 + H2O + CO2", XE, 560, 56, cores={"CO2": E.COR})
    if t >= C["s13.c"]:
        bolhas_co2(c, t, 1480, 520)
        E.foco(c, t, C["s13.c"] + 0.4, 0.4, lambda a: E.escreve(c, "o CO₂ escapa como gás", XE, 650, 50, "b", COR, a))
    E.frase(c, t, C["s14.a"], ps("gota a gota, ano a ano:", "i", 58, TINTA2), XE, 800, passo=0.08)
    E.frase(c, t, C["s14.a"] + 1.2, ps("o nariz, os dedos, os detalhes", "i", 58), XE, 880, passo=0.08)
    E.foco(c, t, C["s14.b"], 0.4, lambda a: E.escreve(c, "e ainda: lagos, florestas, metal de carros e pontes", XE, 1010, 44, "b", TINTA2, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s16"]:
        E.frase(c, t, C["s15"], ps("o atalho:", "i", 66, CLARO) + [("some", "g", 62, BR), ("a", "i", 66, CLARO), ("água", "g", 62, E.CLARO), ("à", "i", 66, CLARO), ("fórmula", "i", 66, CLARO)], XE, 170, passo=0.1)
        Q.formula_em(c, t, C["s15.b"], "SO3 + H2O", 560, 430, 120, align="center", escuro=True, cores={"H2O": E.CLARO})
        E.foco(c, t, C["s15.c"], 0.4, lambda a: centro(c, "→", 960, 430, 120, "g", CLARO, a))
        Q.formula_em(c, t, C["s15.c"] + 0.4, "H2SO4", 1350, 430, 120, align="center", escuro=True, cores={"H": E.CLARO})
        E.foco(c, t, C["s15.c"] + 1.0, 0.4, lambda a: centro(c, "H: 2   S: 1   O: 3 + 1 = 4", W / 2, 560, 54, "b", BR, a))
        Q.formula_em(c, t, C["s15.d"], "CO2 + H2O -> H2CO3", W / 2, 760, 100, align="center", escuro=True, cores={"H2CO3": E.CLARO})
        return
    E.frase(c, t, C["s16.a"], ps("funciona porque os átomos não somem: só se juntam", "i", 58, CLARO), W / 2, 260, "center", 0.08)
    E.frase(c, t, C["s16.b"], [("não", "g", 58, ERRADO), ("compensa", "i", 62, CLARO), ("com", "i", 62, CLARO)], W / 2 - 160, 470, "center", 0.12)
    Q.formula_em(c, t, C["s16.b"] + 0.5, "NO2", W / 2 + 200, 480, 90, align="center", escuro=True)
    E.foco(c, t, C["s16.b"] + 1.0, 0.4, lambda a: centro(c, "a soma não dá um ácido de verdade", W / 2, 580, 50, "i", CLARO, a))
    Q.formula_em(c, t, C["s16.c"], "CO", W / 2 - 250, 800, 110, align="center", escuro=True)
    E.foco(c, t, C["s16.c"] + 0.4, 0.4, lambda a: E.escreve(c, "óxido neutro: não forma ácido", W / 2 - 120, 790, 56, "g", BR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s17"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    riscado(c, t, C["s17.a"], "a culpa da chuva ácida é do CO₂", XE, 340, 60, "b")
    escala(c, t, C["s17.b"] - 0.4, 260, 480, 1400, [(5.6, "CO₂: o natural, 5,6", C["s17.b"]), (4.3, "", C["s17.c"])], ta=C["s17.c"])
    E.frase(c, t, C["s17.c"] + 0.4, ps("para baixo disso: os ácidos fortes", "i", 56), XE, 860, passo=0.08)
    Q.formula_em(c, t, C["s17.d"], "SO2", XE + 300, 980, 80, cores={"SO2": ERRADO})
    E.foco(c, t, C["s17.d"] + 0.4, 0.4, lambda a: E.escreve(c, "e NOₓ", XE + 560, 980, 60, "g", ERRADO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s18.a"], ps("cidade com usinas a carvão; estátuas de mármore se desgastam", "i", 50, TINTA2), XE, 290, passo=0.06)
    E.frase(c, t, C["s18.b"], [("1", "g", 60, COR)] + ps("qual gás do carvão é o culpado?", "i", 60), XE, 450, passo=0.08)
    E.frase(c, t, C["s18.c"], [("2", "g", 60, COR)] + ps("a reação do", "i", 60), XE, 580, passo=0.08)
    Q.formula_em(c, t, C["s18.c"] + 0.6, "SO3", XE + 520, 585, 66)
    E.foco(c, t, C["s18.c"] + 0.8, 0.4, lambda a: E.escreve(c, "com a água", XE + 680, 580, 60, "i", TINTA, a))
    E.frase(c, t, C["s18.d"], [("3", "g", 60, COR)] + ps("cidade: pH 4,5; serra: 5,6. Qual é ácida?", "i", 60), XE, 710, passo=0.08)
    if t < C["s19"]:
        E.foco(c, t, C["s18.a"], 0.5, lambda a: chamine(c, t, 1580, 1000, a))
        E.foco(c, t, C["s18.a"] + 0.4, 0.5, lambda a: estatua(c, 1300, 1000, 160, 0.3, a))
    else:
        E.relogio(c, t, C["s19.a"], cx=1500, cy=760, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s20.a"], [("1", "g", 60, COR)], XE, 240)
    Q.formula_em(c, t, C["s20.a"] + 0.2, "SO2", XE + 80, 245, 96, cores={"SO2": E.COR})
    E.foco(c, t, C["s20.a"] + 0.6, 0.4, lambda a: E.escreve(c, "do enxofre do carvão", XE + 330, 240, 52, "i", TINTA2, a))
    E.frase(c, t, C["s20.b"], [("2", "g", 60, COR)], XE, 440)
    Q.formula_em(c, t, C["s20.b"] + 0.2, "SO3 + H2O -> H2SO4", XE + 80, 445, 96, cores={"H2SO4": E.COR})
    E.frase(c, t, C["s21.a"], [("3", "g", 60, COR)], XE, 620)
    escala(c, t, C["s21.a"], 260, 680, 1400, [(4.5, "cidade: 4,5", C["s21.a"] + 0.4), (5.6, "serra: 5,6", C["s21.b"], 70)], ta=C["s21.a"] + 0.8)
    riscado(c, t, C["s21.c"], "as duas são ácidas, abaixo de 7", XE + 820, 620, 48)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s22.a", "CO", "queima com pouco oxigênio"), ("s22.b", "NO + NO2", "ar aquecido no motor"),
                 ("s22.c", "SO2", "enxofre do combustível"), ("s22.d", None, "chuva ácida: abaixo de 5,6"))
        for i, (k, f, txt) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            x = 400
            if f:
                Q.formula_em(c, t, C[k] + 0.1, f, 400, y, 70)
                x = 400 + Q.grupos(f, 0, 0, 70)[-1]["x1"] + 40
            E.frase(c, t, C[k] + 0.3, [(txt, "i", 66)], x, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s23.a"], [("Efeito", "g", 100, COR), ("estufa", "g", 100, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s23.a"] + 0.6, ps("e camada de ozônio", "i", 80), XE, 520, passo=0.12)
    E.foco(c, t, C["s23.a"] + 0.8, 0.5, lambda a: (E.bola(c, 560, 820, 150, "#3E7FC1", a), E.arco(c, 560, 820, 200, 0, 360, E.COR, 10, a)))
    E.foco(c, t, C["s23.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s23.b"] + 0.2, 0.4))
    E.frase(c, t, C["s23.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, poluentes=b_poluentes, chuva=b_chuva, sulfurico=b_sulfurico, marmore=b_marmore,
              atalho=b_atalho, erro=b_erro, questao=b_questao, resposta=b_resposta, fim=b_fim)
