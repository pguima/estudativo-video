"""Visual — Estudativo · MAT-RAZ-019: praticando divisão proporcional, velocidade, densidade e vazão.
Aula de prática: cinco situações, cada uma com enunciado (com relógio de pausa) e resposta. Peças locais: enunciado() monta a tela
da situação; termo() e fila() vêm da aula MAT-RAZ-025 (unidades que se cortam). Todo instante vem de C[...]."""
from fractions import Fraction as Fr
from decimal import Decimal as D

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-019_praticando_proporcao_velocidade_densidade_vazao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"

assert 6000 * 4 == 24000 and 4000 * 9 == 36000 and 24000 // 12000 == 2 and 36000 // 12000 == 3 and 5000 // 5 == 1000
assert 6 // 2 == 3 and 6 // 3 == 2 and 6 // 6 == 1 and 1200 // 6 == 200 and 600 * 2 == 400 * 3 == 200 * 6 == 1200
assert D(30 + 45) / 2 == D("37.5") and 90 / 30 == 3 and 90 / 45 == 2 and 180 / 5 == 36 and 2 * 30 * 45 == 2700 and 2700 / 75 == 36
assert D(36) / D("3.6") == 10
assert Fr(600, 800) == Fr(3, 4) and D(600) / 800 == D("0.75") and Fr(800, 600) > 1
assert D(6) / 5 == D("1.2") and Fr(1, 2) + Fr(1, 3) == Fr(5, 6) and D("0.2") * 60 == 12


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None, est="g"):
    E.formula_em(c, t, t0, s, cx, y, size, est, cor, "center")


def fesq(c, t, t0, s, x, y, size, cor=None, est="g"):
    E.formula_em(c, t, t0, s, x, y, size, est, cor, "left")


def bola_res(c, t, t0, s, cx, cy, r=130, size=80, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)))


def selo_em(c, t, t0, cx, cy, ok=True, r=48):
    E.foco(c, t, t0, 0.5, lambda a: E.selo(c, cx, cy, r, ok, a))


def titulo_sit(c, t, t0, n, nome):
    """bola com o número da situação e o nome"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 170, 56, a=a), centro(c, str(n), XE + 50, 193, 64, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.15, [("situação", "i", 72, COR), (nome, "g", 72)], XE + 130, 195, "left", 0.12)


def enunciado(c, t, C, n, nome, cena, linhas, pausa):
    """linhas = [(instante, partes, y)]; pausa = instante do relógio"""
    titulo_sit(c, t, C[cena + ".a"], n, nome)
    for t0, partes, y in linhas:
        E.frase(c, t, t0, partes, XE, y, "left", 0.1)
    E.relogio(c, t, pausa, 1570, 470, 170)


def cab(c, t, t0, n, nome):
    """cabeçalho pequeno da resposta"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 30, 110, 36, a=a), centro(c, str(n), XE + 30, 125, 42, "g", E.SOBRE, a),
                                      E.escreve(c, nome, XE + 85, 126, 46, "i", TINTA2, a)))


def _partes(p, size):
    n, u = p
    wn = E.larg(n, "g", size) if n else 0
    wu = E.larg(u, "b", size * 0.8) if u else 0
    return wn, (size * 0.2 if n and u else 0), wu


def larg_termo(cima, baixo, size):
    w = sum(_partes(cima, size))
    if baixo:
        w = max(w, sum(_partes(baixo, size)))
    return w + size * 0.3


def termo(c, t, t0, cx, cy, size, cima, baixo=None, cor=None, cortes=()):
    """número com unidade, em cima e embaixo; cortes = [(onde 'c'|'b', qual 'n'|'u', instante)] riscam a parte que corta"""
    cor = cor or TINTA
    cu = E.mix(cor, "#FFFFFF", 0.25)
    linhas = {"c": (cima, cy - size * 0.2 if baixo else cy + size * 0.35)}
    if baixo:
        linhas["b"] = (baixo, cy + size * 0.9)
    caixas = {}
    for k, (p, y) in linhas.items():
        wn, gap, wu = _partes(p, size)
        x = cx - (wn + gap + wu) / 2
        caixas[(k, "n")] = (x, y, wn)
        caixas[(k, "u")] = (x + wn + gap, y, wu)

    def desenha(a):
        for k, (p, y) in linhas.items():
            if p[0]:
                E.escreve(c, p[0], caixas[(k, "n")][0], y, size, "g", cor, a)
            if p[1]:
                E.escreve(c, p[1], caixas[(k, "u")][0], y, size * 0.8, "b", cu, a)
        if baixo:
            lw = larg_termo(cima, baixo, size) - size * 0.15
            b = size * 0.075
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - lw / 2, cy - b / 2 + size * 0.03, lw, b), b / 2, b / 2), M.paint(cor, a))
    E.foco(c, t, t0, 0.5, desenha)
    for onde, qual, tc in cortes:
        p = ep(t, tc, 0.35)
        if p > 0:
            x, y, w = caixas[(onde, qual)]
            M.line(c, x - 6, y + size * 0.08, x + w + 6, y - size * 0.72, E.COR, 1.0, max(5, size * 0.08), progress=p)


def boia(c, t, t0, x, y, w, h, fundo_, a=1.0):
    """água num tanque e um bloco que boia (fundo_ = fração submersa)"""
    q = ep(t, t0, 0.6) * a
    if q <= 0:
        return
    nivel = y + h * 0.35
    c.drawRect(skia.Rect.MakeXYWH(x, nivel, w, y + h - nivel), M.paint(E.COR, 0.22 * q))
    M.line(c, x, nivel, x + w, nivel, E.COR, q, 5)
    bw, bh = w * 0.34, h * 0.34
    desce = ep(t, t0 + 0.3, 1.0)
    by = lerp(y - bh * 0.2, nivel - bh * (1 - fundo_), ease_back(desce))
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + w / 2 - bw / 2, by, bw, bh), 10, 10)
    c.drawRRect(rr, M.paint("#C89B6A", q))
    c.drawRRect(rr, M.paint(TINTA, q, stroke=4))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, q, stroke=5))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]
    E.foco(c, t, a1, 0.5, lambda a: E.escreve(c, "5", XE - 8, 470, 340, "g", COR, a))
    E.frase(c, t, a1 + 0.2, ps("situações", "i", 120), XE + 215, 450, "left")
    E.frase(c, t, lerp(a1, b1, 0.4), ps("criadas para esta aula", "i", 60, TINTA2), XE + 10, 560, "left", 0.1)
    nomes = ("sócios", "prêmio", "viagem", "objeto na água", "caixa-d'água")
    for i, s in enumerate(nomes):
        ti = lerp(b1, c1, 0.12 + i * 0.16)
        y = 190 + i * 150
        E.foco(c, t, ti, 0.5, lambda a, i=i, s=s, y=y: (E.bola(c, 1080, y, 44, a=a), centro(c, str(i + 1), 1080, y + 18, 50, "g", E.SOBRE, a),
                                                         E.escreve(c, s, 1150, y + 22, 66, "g", TINTA, a)))
    E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "pause · resolva · confira", 560, 860, 56, "g", a=a, cor=E.SOBRE))


# ---------------- ferramentas ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.2, ps("você vai usar", "i", 80), XE, 410, passo=0.14)
    E.foco(c, t, C["s02"] + 0.6, 0.5, lambda a: E.escreve(c, "4", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s02"] + 0.75, 0.5, lambda a: E.escreve(c, "ferramentas", XE + 215, 700, 100, "i", TINTA, a))
    x, w = 930, 860
    itens = (("s02.a", "o k:", "o valor de uma parte"), ("s02.b", "a palavra por:", "quer dizer ÷"),
             ("s02.c", "velocidade média:", "distância total ÷ tempo total"), ("s02.d", "as unidades:", "conferem a conta"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 90 + i * 215
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 180, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 40, y + 76)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 40, y + 148)
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.55), ps("travou?", "i", 54, COR) + ps("procure a aula no canal", "i", 54), XE, 960, "left", 0.1)


# ---------------- situação 1: sócios ----------------
def b_questao1(c, t, C, b):
    k = lambda s: C["s03." + s]
    enunciado(c, t, C, 1, "sócios", "s03", [
        (k("b"), ps("Lia:", "i", 76) + [("R$ 6.000", "g", 76, COR)] + ps("por", "i", 76) + [("4 meses", "g", 76)], 380),
        (k("c"), ps("Rui:", "i", 76) + [("R$ 4.000", "g", 76, COR)] + ps("por", "i", 76) + [("9 meses", "g", 76)], 520),
        (k("d"), ps("lucro:", "i", 76) + [("R$ 5.000", "g", 76, COR)], 660),
        (k("e"), ps("quanto", "i", 88) + [("cada um recebe?", "g", 88, COR)], 860)], C["s04.a"])


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    cab(c, t, C["s05"], 1, "sócios")
    E.foco(c, t, a5, 0.5, lambda a: E.pilula(c, "peso = capital × tempo", W / 2, 230, 64, "g", a=a, cor=E.SOBRE))

    def pesos():
        fesq(c, t, b5, "Lia:  6.000 × 4 = 24.000", 260, 420, 80)
        fesq(c, t, c5, "Rui:  4.000 × 9 = 36.000", 260, 560, 80)
        E.foco(c, t, d5, 0.5, lambda a: E.pilula(c, "÷ 12.000", 1500, 480, 56, "g", fundo=TINTA, a=a))
        E.foco(c, t, d5 + 0.4, 0.5, lambda a: (centro(c, "2", 1400, 690, 130, "g", COR, a), centro(c, "e", 1500, 680, 80, "i", TINTA, a),
                                                centro(c, "3", 1600, 690, 130, "g", COR, a)))
    E.saida(c, t, a6 - 0.1, pesos)
    if t < a6 - 0.1:
        return
    fcen(c, t, a6, "2k + 3k = 5.000", W / 2, 420, 110)
    fcen(c, t, lerp(a6, b6, 0.55), "5k = 5.000", 620, 600, 96, TINTA2)
    fcen(c, t, b6, "k = 1.000", 1300, 600, 96, COR)
    E.frase(c, t, c6, [("Lia:", "i", 76)], 300, 830, "left")
    bola_res(c, t, c6, "R$ 2.000", 620, 805, 140, 58)
    E.frase(c, t, d6, [("Rui:", "i", 76)], 980, 830, "left")
    bola_res(c, t, d6, "R$ 3.000", 1300, 805, 140, 58)
    E.frase(c, t, lerp(d6, C["s06.end"], 0.55), ps("o Rui ficou mais que", "i", 54, TINTA2) + [("o dobro do tempo", "g", 54, COR)], W / 2, 1035, "center", 0.08)


# ---------------- situação 2: prêmio ----------------
def b_questao2(c, t, C, b):
    k = lambda s: C["s07." + s]
    enunciado(c, t, C, 2, "prêmio", "s07", [
        (k("b"), [("R$ 1.200", "g", 76, COR)] + ps("para 3 pessoas", "i", 76), 380),
        (k("c"), [("inversa", "g", 76, COR)] + ps("às faltas", "i", 76), 520),
        (k("d"), ps("faltas:", "i", 76) + [("2, 3 e 6", "g", 76)], 660),
        (k("e"), ps("quanto", "i", 88) + [("cada uma recebe?", "g", 88, COR)], 860)], C["s08.a"])


def b_resposta2(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10, d10 = (C[f"s10.{k}"] for k in "abcd")
    cab(c, t, C["s09"], 2, "prêmio")
    xs = (560, 960, 1360)
    faltas, pesos, valores = (2, 3, 6), (3, 2, 1), (600, 400, 200)

    def topo():
        E.frase(c, t, C["s09"] + 0.4, ps("inversa às faltas =", "i", 60) + [("direta aos inversos", "g", 60, COR)], W / 2, 230, "center", 0.08)
        E.foco(c, t, a9, 0.5, lambda a: E.pilula(c, "peso = MMC ÷ cada número", 700, 340, 50, "g", a=a, cor=E.SOBRE))
        fcen(c, t, b9, "MMC = 6", 1380, 360, 72, COR)
    E.saida(c, t, C["s10"] - 0.1, topo)
    if t >= C["s10"]:
        E.frase(c, t, C["s10"] + 0.2, ps("soma dos pesos:", "i", 60) + [("3 + 2 + 1 = 6", "g", 60)], 560, 260, "center", 0.08)
        fcen(c, t, a10, "1.200 ÷ 6 = 200", 1360, 270, 72, COR)
    E.foco(c, t, C["s09"] + 0.2, 0.5, lambda a: E.escreve(c, "faltas", XE - 20, 518, 46, "i", TINTA2, a))
    E.foco(c, t, c9, 0.5, lambda a: E.escreve(c, "peso", XE - 20, 668, 46, "i", TINTA2, a))
    for i, x in enumerate(xs):
        fcen(c, t, C["s09"] + 0.2 + 0.15 * i, str(faltas[i]), x, 530, 88)
        E.foco(c, t, c9 + 0.25 * i, 0.5, lambda a, i=i, x=x: (centro(c, str(pesos[i]), x, 690, 100, "g", COR, a),
                                                              centro(c, f"6 ÷ {faltas[i]}", x, 590, 40, "m", TINTA2, a)))
        bola_res(c, t, b10 + 0.25 * i, f"R$ {valores[i]}", x, 830, 110, 52)
        fcen(c, t, c10 if i == 0 else lerp(c10, d10, 0.25 + 0.3 * i), f"{valores[i]} × {faltas[i]} = 1.200", x, 1010, 46, TINTA2)
    selo_em(c, t, d10, 1700, 830)


# ---------------- situação 3: viagem ----------------
def b_questao3(c, t, C, b):
    k = lambda s: C["s11." + s]
    enunciado(c, t, C, 3, "viagem", "s11", [
        (k("b"), ps("sobe", "i", 72) + [("90 km", "g", 72, COR)] + ps("a", "i", 72) + [("30 km/h", "g", 72)], 360),
        (k("c"), ps("volta a", "i", 72) + [("45 km/h", "g", 72)], 490),
        (k("d"), ps("velocidade média", "i", 76) + [("na ida e volta?", "g", 76, COR)], 680),
        (k("e"), ps("e em", "i", 76) + [("m/s?", "g", 76, COR)], 810)], C["s12.a"])


def b_resposta3(c, t, C, b):
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14, d14, e14 = (C[f"s14.{k}"] for k in "abcde")
    cab(c, t, C["s13"], 3, "viagem")

    def armadilha():
        fcen(c, t, a13, "(30 + 45) ÷ 2 = 37,5", W / 2, 300, 88, ERRADO)
        tr = lerp(a13, b13, 0.3)
        if t >= tr:
            E.risco(c, W / 2 - 430, 320, W / 2 + 430, 230, t, tr, largura=12)
            E.frase(c, t, tr + 0.3, [("armadilha", "g", 54, ERRADO)], W / 2, 400, "center")
    E.saida(c, t, b13 - 0.1, armadilha)
    if t >= b13 - 0.6:
        E.foco(c, t, lerp(a13, b13, 0.6), 0.5, lambda a: E.pilula(c, "distância total ÷ tempo total", W / 2, 260, 56, "g", a=a, cor=E.SOBRE))

    def tempos():
        fesq(c, t, b13, "subida:  90 ÷ 30 = 3 h", 260, 470, 76)
        fesq(c, t, c13, "descida:  90 ÷ 45 = 2 h", 260, 600, 76)
        fesq(c, t, a14, "total:  180 km", 1120, 470, 76)
        fesq(c, t, b14, "em  5 h", 1120, 600, 76)
    tempos()
    fcen(c, t, c14, "180 ÷ 5 = 36 km/h", W / 2, 790, 100, COR)
    E.foco(c, t, d14, 0.5, lambda a: E.formula(c, "atalho: f{2 × 30 × 45}{30 + 45} = f{2.700}{75} = 36", 640, 960, 58, "g", TINTA2, a, "center"))
    bola_res(c, t, e14, "10 m/s", 1660, 940, 105, 54, CERTO)
    E.foco(c, t, e14, 0.5, lambda a: E.escreve(c, "36 km/h =", 1190, 965, 66, "g", TINTA, a))


# ---------------- situação 4: objeto na água ----------------
def b_questao4(c, t, C, b):
    k = lambda s: C["s15." + s]
    enunciado(c, t, C, 4, "objeto na água", "s15", [
        (k("b"), ps("bloco de madeira:", "i", 76) + [("600 g", "g", 76, COR)], 380),
        (k("c"), ps("volume:", "i", 76) + [("800 cm³", "g", 76, COR)], 520),
        (k("d"), ps("qual é a", "i", 84) + [("densidade?", "g", 84, COR)], 720),
        (k("e"), [("boia", "g", 84, COR)] + ps("na água?", "i", 84), 850)], C["s16.a"])


def b_resposta4(c, t, C, b):
    a17, b17, c17, d17 = (C[f"s17.{k}"] for k in "abcd")
    a18, b18, c18, d18 = (C[f"s18.{k}"] for k in "abcd")
    cab(c, t, C["s17"], 4, "objeto na água")
    fesq(c, t, a17, "d = f{massa}{volume}", 220, 330, 84, COR)
    fesq(c, t, b17, "f{600}{800}", 220, 560, 100)
    E.foco(c, t, lerp(b17, c17, 0.5), 0.4, lambda a: E.pilula(c, "÷ 200 nos dois", 330, 700, 42, "g", fundo=TINTA, a=a))
    fesq(c, t, c17, "= f{3}{4}", 440, 560, 100)
    fesq(c, t, d17, "= 0,75 g/cm³", 650, 580, 84, COR)
    # tanque com o bloco
    fesq(c, t, a18, "água: 1 g/cm³", 1180, 330, 64, TINTA2)
    boia(c, t, b18 - 0.3, 1220, 400, 520, 360, 0.75)
    E.foco(c, t, b18, 0.5, lambda a: (E.selo(c, 1810, 520, 44, True, a)))
    E.frase(c, t, b18 + 0.2, [("0,75 < 1:", "g", 60), ("boia", "g", 60, CERTO)], 1480, 850, "center", 0.1)
    E.frase(c, t, c18, ps("atalho:", "i", 56, TINTA2) + [("600 < 800", "g", 56), ("→ boia", "g", 56, CERTO)], 1480, 950, "center", 0.08)
    if t >= d18 - 0.6:
        fesq(c, t, lerp(c18, d18, 0.7), "f{800}{600} > 1", 220, 870, 84, ERRADO)
        E.frase(c, t, d18, ps("ordem trocada:", "i", 54, ERRADO) + [("afunda?", "g", 54, ERRADO)], 220, 1010, "left", 0.08)
        tr = d18 + 0.8
        if t >= tr:
            E.risco(c, 210, 900, 640, 790, t, tr, largura=10)


# ---------------- situação 5: caixa-d'água ----------------
def b_questao5(c, t, C, b):
    k = lambda s: C["s19." + s]
    enunciado(c, t, C, 5, "caixa-d'água", "s19", [
        (k("b"), ps("uma torneira:", "i", 76) + [("2 h", "g", 76, COR)], 380),
        (k("c"), ps("outra:", "i", 76) + [("3 h", "g", 76, COR)], 520),
        (k("d"), ps("as duas juntas:", "i", 84), 720),
        (k("d") + 0.6, [("horas e minutos?", "g", 84, COR)], 850)], C["s20.a"])


def b_resposta5(c, t, C, b):
    a21, b21, c21, d21, e21 = (C[f"s21.{k}"] for k in "abcde")
    a22, b22, c22, d22 = (C[f"s22.{k}"] for k in "abcd")
    cab(c, t, C["s21"], 5, "caixa-d'água")

    def um():
        E.frase(c, t, C["s21"] + 0.4, ps("produto", "g", 70, COR) + ps("sobre", "i", 70) + [("soma", "g", 70, COR)], W / 2, 230, "center", 0.1)
        fesq(c, t, a21, "2 × 3 = 6", 260, 400, 84)
        fesq(c, t, b21, "2 + 3 = 5", 260, 530, 84)
        fesq(c, t, c21, "6 ÷ 5 = 1,2 h", 760, 470, 100, COR)
        fesq(c, t, d21, "f{1}{2} + f{1}{3} = f{5}{6} por hora", 260, 720, 76)
        fesq(c, t, lerp(d21, e21, 0.6), "f{6}{6} ÷ f{5}{6}: 6 ÷ 5 = 1,2", 1100, 720, 60, TINTA2)
        E.foco(c, t, e21, 0.5, lambda a: E.pilula(c, "sem dobro: a caixa é uma só", 700, 900, 52, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, lerp(e21, C["s21.end"], 0.35), ps("ida e volta:", "i", 52, TINTA2) + [("2 trechos → dobro", "g", 52, TINTA2)], 1180, 1000, "center", 0.08)
    E.saida(c, t, C["s22"] - 0.1, um)
    if t < C["s22"]:
        return
    E.foco(c, t, a22, 0.5, lambda a: E.formula(c, "1,2 h ≠ 1 h 20 min", W / 2, 300, 96, "g", ERRADO, a, "center"))
    tb = b22
    tc = lerp(b22, c22, 0.6)
    termo(c, t, tb, 500, 520, 96, ("0,2", "h"), cortes=[("c", "u", tc)])
    E.foco(c, t, tb + 0.2, 0.4, lambda a: centro(c, "×", 700, 560, 80, "g", TINTA2, a))
    termo(c, t, tb + 0.4, 930, 520, 96, ("60", "min"), ("1", "h"), cortes=[("b", "u", tc)])
    fesq(c, t, c22, "= 12 min", 1170, 545, 96, COR)
    fcen(c, t, lerp(c22, d22, 0.4), "cada 0,1 h = 6 min", W / 2, 715, 60, TINTA2)
    bola_res(c, t, d22, "1 h 12 min", 760, 905, 150, 50, CERTO)
    E.frase(c, t, lerp(d22, C["s22.end"], 0.3), [("< 2 h:", "g", 64), ("faz sentido", "i", 64, CERTO)], 1300, 945, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s23.a", "ache", "o peso certo antes de dividir"), ("s23.b", "some tempos e distâncias,", "não velocidades"),
                 ("s23.c", "deixe as unidades", "conferirem a conta"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 70) + [(l2, "g", 70, COR if i == 0 else TINTA)], 320, y, "left", 0.1)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    a0, b0 = C["s24.a"], C["s24.b"]
    E.frase(c, t, C["s24"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, a0, [("a escala", "g", 150, COR)], XE, 410)
    E.frase(c, t, b0, ps("ler", "i", 76) + [("1 : 100", "g", 80, COR)], XE, 540, passo=0.1)
    E.frase(c, t, lerp(b0, C["s24.c"], 0.4), [("3 cm", "g", 76)] + ps("de mapa valem quantos", "i", 76) + [("km?", "g", 76)], XE, 650, passo=0.1)
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 740, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(950, 765, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
