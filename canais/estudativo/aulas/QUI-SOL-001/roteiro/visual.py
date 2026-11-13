"""Visual — Estudativo · QUI-SOL-001: solução, coloide e suspensão. Primeira aula da trilha Soluções.

Segue a LINGUAGEM VISUAL DA QUÍMICA do cabeçalho de QUI-MIS-001/roteiro/visual.py (kit _ferramentas/quimica.py, como Q).

LINGUAGEM VISUAL DA TRILHA SOLUÇÕES (QUI-SOL-001 a 007 copiam daqui):
- FRASCO: Q.bequer em cinza com véu; solvente água = Q.AGUA. SOLUTO = bolinhas pequenas na cor da matéria (E.COR) dentro do
  líquido (graos(...) ou Q.particulas): mais bolinhas = mais concentrada. Sal no fundo (corpo de fundo) = grãos brancos
  empilhados no fundo do béquer. Rótulo do frasco embaixo, em itálico cinza ("água com sal", "500 mL").
- SOLUÇÃO, COLOIDE, SUSPENSÃO: o mesmo béquer com três tamanhos de partícula: pontinhos (solução), gotinhas creme (coloide),
  grãos marrons que descem até o fundo (suspensão). O FEIXE DE LUZ é vermelho-laser (LASER), saindo da caneta à esquerda; no
  coloide e na suspensão ele brilha dentro do líquido (efeito Tyndall); na solução só o ponto aparece na parede de trás.
- CONCENTRAÇÃO e FÓRMULAS DE CONTA (C = m/V, C₁V₁ = C₂V₂): E.formula na grotesca, a letra da vez em E.COR_TEXTO; unidade
  (g/L, mol/L, mL) sempre escrita ao lado em cinza-tinta; resultado final na esfera turquesa (bola_txt).
- CURVA DE SOLUBILIDADE: Q.solubilidade; leitura com as duas guias tracejadas (da temperatura até a curva e da curva até o
  eixo), o valor lido numa pílula turquesa.
- Erro e acerto como na Química: risco/selo, nunca só a cor.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Soluções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-SOL-001_solucao_coloide_suspensao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("soluto", "tipos", "tyndall", "atalho", "questao", "fim"))
BR = "#FFFFFF"
LASER = "#FF2D2D"
LEITE = "#EEE9DC"      # coloide: leite diluído, turvo
TERRA = "#C9B28C"      # suspensão: água com terra
CAFE = "#7A4A2A"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula (candidatas ao kit: caneta_laser, feixe, graos) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def rotulo(c, t, t0, s, cx, y, size=48, cor=TINTA2):
    E.foco(c, t, t0, 0.4, lambda a: centro(c, s, cx, y, size, "i", cor, a))


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def caneta_laser(c, x, y, a=1.0, ligada=True, comp=180):
    """caneta laser deitada, com a ponta em (x, y) apontando para a direita"""
    if a <= 0:
        return
    M.rrect(c, x - 10 - comp, y - 20, comp, 40, 18, "#2A2B31", a)
    M.rrect(c, x - 10 - comp * 0.78, y - 26, 34, 8, 4, "#9AA0A8", a)
    M.rrect(c, x - 14, y - 14, 16, 28, 6, "#5B6470", a)
    if ligada:
        c.drawCircle(x + 2, y, 7, M.paint(LASER, a))


def feixe(c, t, t0, x0, xv0, xv1, y, brilho, a=1.0, d=0.5):
    """feixe de laser de x0 até a parede de trás do frasco (xv1). Dentro do líquido (xv0..xv1) ele só aparece se brilho > 0
    (efeito Tyndall); na solução, só o ponto vermelho na parede de trás"""
    if t < t0 or a <= 0:
        return
    p = ease_out(prog(t, t0, d))
    xf = lerp(x0, xv1, p)
    M.line(c, x0, y, min(xf, xv0), y, LASER, 0.55 * a, 3)
    if xf > xv0 and brilho > 0:
        for lw, al in ((34, 0.10), (18, 0.22), (8, 0.55), (3.5, 1.0)):
            M.line(c, xv0, y, xf, y, LASER, al * brilho * a, lw)
    if p >= 1:
        c.drawCircle(xv1, y, 9, M.paint(LASER, a))
        c.drawCircle(xv1, y, 18, M.paint(LASER, 0.25 * a))


def graos(c, t, x, y, w, h, n, r, cor, assenta=0.0, semente=1, a=1.0, borda=None):
    """partículas espalhadas no líquido (x, y, w, h); assenta = 0..1 leva cada uma para a pilha do fundo"""
    if a <= 0:
        return
    rnd = random.Random(semente)
    por_linha = max(1, int(w / (2.1 * r)))
    for i in range(n):
        px, py = x + r + rnd.random() * (w - 2 * r), y + r + rnd.random() * (h - 2 * r)
        fx = x + r + (i % por_linha) * (w - 2 * r) / max(1, por_linha - 1)
        fy = y + h - r - (i // por_linha) * 1.7 * r
        ph = rnd.random() * 6.28
        q = ease_io(assenta)
        xx = lerp(px + 3 * math.sin(t * 1.3 + ph), fx, q)
        yy = lerp(py + 3 * math.cos(t * 1.1 + ph), fy, q)
        c.drawCircle(xx, yy, r, M.paint(cor, a))
        if borda:
            c.drawCircle(xx, yy, r, M.paint(borda, 0.5 * a, stroke=1.5))


def frasco(c, t, t0, cx, yb, w, h, liquido, tipo, assenta=0.0, nivel=0.78, semente=3, a_max=1.0):
    """béquer com um dos três tipos: 'sol' (pontinhos turquesa), 'col' (gotinhas creme), 'sus' (grãos marrons que assentam)"""
    Q.bequer(c, t, t0, cx, yb, w, h, nivel, liquido, graduacao=False)
    if t < t0:
        return
    q = ep(t, t0, 0.5) * a_max
    x0, y0 = cx - w / 2 + 16, yb - h * nivel + 16
    ww, hh = w - 32, h * nivel - 30
    if tipo == "sol":
        graos(c, t, x0, y0, ww, hh, 70, 2.6, E.COR, 0, semente, 0.8 * q)
    elif tipo == "col":
        graos(c, t, x0, y0, ww, hh, 46, 6.5, "#FFFDF5", 0, semente, 0.95 * q, borda="#C9C2B0")
    elif tipo == "sus":
        graos(c, t, x0, y0, ww, hh, 34, 11, "#8B6A44", assenta, semente, q)


# ---------------- gancho ----------------
GX = (560, 1340)
GYB, GW, GH = 840, 380, 430


def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("dois copos", "i", 80), XE, 170)
        frasco(c, t, C["s01.a"] + 0.2, GX[0], GYB, GW, GH, Q.AGUA, "sol")
        rotulo(c, t, C["s01.a"] + 0.6, "água com sal", GX[0], GYB + 80, 54)
        frasco(c, t, C["s01.b"], GX[1], GYB, GW, GH, LEITE, "col")
        rotulo(c, t, C["s01.b"] + 0.3, "água com leite", GX[1], GYB + 80, 54)
        pilula_em(c, t, lerp(C["s01.b"], C["s01.c"], 0.5), "parecem uma coisa só", W / 2, 260, 46, TINTA2, "b")
        yb = GYB - GH * 0.42
        for k, (cx, ti, br) in enumerate(((GX[0], C["s01.d"], 0.0), (GX[1], C["s01.e"], 1.0))):
            xl = cx - GW / 2 - 70
            E.foco(c, t, C["s01.c"] + 0.3 * k, 0.4, lambda a, xl=xl: caneta_laser(c, xl, yb, a))
            feixe(c, t, ti, xl + 4, cx - GW / 2, cx + GW / 2 - 6, yb, br)
        pilula_em(c, t, C["s01.d"] + 0.5, "o feixe some", GX[0], 1010, 50, TINTA)
        pilula_em(c, t, C["s01.e"] + 0.6, "o feixe aparece", GX[1], 1010, 50, E.COR)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("soluto", "g", 70, COR), ("e", "i", 74), ("solvente", "g", 70, COR)]),
                 (C["s02.c"], [("solução,", "g", 66), ("coloide,", "g", 66), ("suspensão", "g", 66)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 76, TINTA2), XE, 170)
    E.frase(c, t, C["s03.a"], [("homogênea", "g", 76, COR)], XE, 300)
    E.frase(c, t, C["s03.a"] + 0.6, ps("uma fase só", "i", 70), XE, 390, passo=0.12)
    Q.bequer(c, t, C["s03.a"] + 0.3, 1180, 560, 230, 260, 0.75, Q.AGUA, graduacao=False)
    pilula_em(c, t, C["s03.a"] + 1.0, "1 fase", 1180, 620, 42, E.COR)
    E.frase(c, t, C["s03.b"], [("heterogênea", "g", 76, COR)], XE, 520)
    E.frase(c, t, C["s03.b"] + 0.6, ps("mais de uma fase", "i", 70), XE, 610, passo=0.12)
    Q.bequer(c, t, C["s03.b"] + 0.3, 1580, 560, 230, 260, 0.75, "#F2C94C", graduacao=False)
    Q.bequer(c, t, C["s03.b"] + 0.3, 1580, 560, 230, 260, 0.45, Q.AGUA, graduacao=False)
    pilula_em(c, t, C["s03.b"] + 1.0, "2 fases", 1580, 620, 42, E.COR)
    rotulo(c, t, C["s03.b"] + 1.2, "água e óleo", 1580, 690, 44)
    E.frase(c, t, C["s03.c"], ps("semelhante dissolve semelhante", "i", 70), XE, 860, passo=0.12)
    E.frase(c, t, C["s03.c"] + 1.6, [("sal", "g", 60), ("dissolve", "i", 64), ("na", "i", 64), ("água;", "i", 64), ("óleo", "g", 60), ("não", "g", 60, ERRADO)], XE, 960, passo=0.12)


# ---------------- soluto e solvente ----------------
def b_soluto(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04"], ps("o café adoçado", "i", 76, TINTA2), XE, 190, passo=0.12)
            cx, yb = 1420, 860
            Q.bequer(c, t, C["s04"] + 0.2, cx, yb, 380, 420, 0.72, CAFE, graduacao=False)
            # açúcar caindo e sumindo no líquido
            ta = C["s04.a"]
            rnd = random.Random(7)
            for k in range(14):
                ti = ta + 0.08 * k
                u = prog(t, ti, 0.7)
                if u <= 0:
                    continue
                x = cx - 120 + rnd.random() * 240
                y = lerp(360, 640 + rnd.random() * 120, u * u)
                al = 1 - ep(t, ti + 0.9, 0.8)
                if al > 0:
                    M.rrect(c, x - 9, y - 9, 18, 18, 3, BR, al, stroke=1.5, stroke_color="#C8C2B6")
            graos(c, t, cx - 170, 600, 340, 230, 60, 2.6, "#F4E9D8", 0, 5, 0.9 * ep(t, ta + 1.2, 0.8))
            rotulo(c, t, C["s04.a"] + 0.4, "o açúcar some: foi dissolvido", cx, yb + 80, 46)
            E.frase(c, t, C["s04.b"], [("soluto", "g", 110, COR)], XE, 400)
            E.frase(c, t, C["s04.b"] + 0.5, ps("o que se dissolve", "i", 64, TINTA2), XE, 480, passo=0.1)
            E.frase(c, t, C["s04.c"], [("solvente", "g", 110, COR)], XE, 650)
            E.frase(c, t, C["s04.c"] + 0.5, ps("o que dissolve", "i", 64, TINTA2), XE, 730, passo=0.1)
            pilula_em(c, t, C["s04.d"], "soluto: açúcar", XE + 190, 870, 50, E.COR)
            pilula_em(c, t, C["s04.d"] + 0.8, "solvente: água", XE + 640, 870, 50, TINTA)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], ps("na dúvida, o solvente é o que está em", "i", 64), XE, 200, passo=0.1)
            E.frase(c, t, C["s05.a"] + 1.6, [("maior quantidade", "g", 72, COR)], XE, 300)
            E.frase(c, t, C["s05.b"], [("água:", "g", 66), ("solvente", "i", 72), ("universal", "i", 72, COR)], XE, 430, passo=0.12)
            # soluto + solvente = solução
            y = 740
            pilula_em(c, t, C["s05.c"], "soluto", 420, y, 66, E.COR)
            E.foco(c, t, C["s05.c"] + 0.3, 0.4, lambda a: centro(c, "+", 640, y + 26, 90, "g", TINTA2, a))
            pilula_em(c, t, C["s05.c"] + 0.5, "solvente", 880, y, 66, TINTA)
            E.foco(c, t, C["s05.d"] - 0.3, 0.4, lambda a: centro(c, "=", 1130, y + 26, 90, "g", TINTA2, a))
            E.frase(c, t, C["s05.d"], [("solução", "g", 110, COR)], 1230, y + 38)
            rotulo(c, t, C["s05.d"] + 0.5, "uma fase só", 1440, y + 130, 50)
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    E.frase(c, t, C["s06"], ps("solução não precisa ser líquida", "i", 70), XE, 200, passo=0.12)
    E.frase(c, t, C["s06.a"], [("o", "i", 90), ("ar", "g", 110, COR)], XE, 420)
    E.frase(c, t, C["s06.a"] + 0.5, ps("é uma solução de gases", "i", 70), XE, 520, passo=0.12)
    E.frase(c, t, C["s06.a"] + 2.0, [("nitrogênio", "g", 60), ("=", "g", 60, TINTA2), ("solvente", "i", 66, COR)], XE, 690, passo=0.12)
    E.frase(c, t, C["s06.a"] + 3.4, [("oxigênio", "g", 60), ("=", "g", 60, TINTA2), ("soluto", "i", 66, COR)], XE, 790, passo=0.12)
    E.foco(c, t, C["s06.a"], 0.6, lambda a: c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1100, 260, 640, 600), 30, 30), M.paint(FIO, a, stroke=4)))
    if t >= C["s06.a"]:
        for k, (mol, x, y) in enumerate([("N2", 1200, 360), ("N2", 1420, 330), ("O2", 1620, 400), ("N2", 1250, 560), ("N2", 1500, 520),
                                         ("O2", 1330, 760), ("N2", 1630, 640), ("N2", 1460, 760), ("N2", 1180, 760)]):
            dx, dy = 14 * math.sin(t * 0.9 + k), 12 * math.cos(t * 0.7 + 2 * k)
            Q.molecula(c, t, C["s06.a"] + 0.1 * k, mol, x + dx, y + dy, 60, passo=0.05, rotulos=True, giro=20 * k + 10 * math.sin(t * 0.5 + k))


# ---------------- os três tipos ----------------
TX = (360, 960, 1560)


def b_tipos(c, t, C, b):
    E.frase(c, t, C["s07.a"] - 0.6, ps("o que separa:", "i", 64, TINTA2) + [("o", "i", 70), ("tamanho", "g", 64, COR)] + ps("das partículas", "i", 70), XE, 160, passo=0.1)
    yb, w, h = 700, 330, 360
    # solução
    E.frase(c, t, C["s07.b"], [("solução", "g", 70, COR)], TX[0], 320, "center")
    frasco(c, t, C["s07.b"] + 0.2, TX[0], yb, w, h, Q.AGUA, "sol")
    rotulo(c, t, C["s07.b"] + 0.6, "do tamanho de uma molécula", TX[0], yb + 70, 40)
    pilula_em(c, t, C["s07.c"], "nunca assenta", TX[0], yb + 160, 44, TINTA)
    # suspensão
    E.frase(c, t, C["s08.a"], [("suspensão", "g", 70, COR)], TX[2], 320, "center")
    frasco(c, t, C["s08.a"] + 0.2, TX[2], yb, w, h, TERRA, "sus", assenta=ease_io(prog(t, C["s08.c"], 2.0)), semente=9)
    rotulo(c, t, C["s08.b"], "grãos que se veem", TX[2], yb + 70, 40)
    pilula_em(c, t, C["s08.c"] + 0.6, "assenta no fundo", TX[2], yb + 160, 44, TINTA)
    E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "agite antes de usar", TX[2], yb + 250, 40, "b", fundo=E.COR, a=a))
    # coloide
    E.frase(c, t, C["s09.a"], [("coloide", "g", 70, COR)], TX[1], 320, "center")
    frasco(c, t, C["s09.a"] + 0.2, TX[1], yb, w, h, LEITE, "col")
    rotulo(c, t, C["s09.b"], "gotinhas de gordura", TX[1], yb + 70, 40)
    pilula_em(c, t, C["s09.c"], "não assenta", TX[1], yb + 160, 44, TINTA)
    # lupa sobre o leite: as gotinhas aparecem no microscópio
    if C["s09.d"] <= t < C["s09.e"] + 0.5:
        def lupa():
            q = ep(t, C["s09.d"], 0.5)
            lx, ly, lr = TX[1] + 170, 470, 120
            c.save()
            pth = skia.Path(); pth.addCircle(lx, ly, lr * q)
            c.clipPath(pth, skia.ClipOp.kIntersect, True)
            c.drawCircle(lx, ly, lr, M.paint("#F7F3EA"))
            graos(c, t, lx - lr, ly - lr, 2 * lr, 2 * lr, 16, 17, "#FFFDF5", 0, 11, 1.0, borda="#B9B19C")
            c.restore()
            c.drawCircle(lx, ly, lr * q, M.paint(TINTA, q, stroke=8))
            M.line(c, lx + lr * 0.7, ly + lr * 0.7, lx + lr * 1.25, ly + lr * 1.25, TINTA, q, 16)
        E.saida(c, t, C["s09.e"] + 0.4, lupa)
    if t >= C["s09.e"]:
        for k, s in enumerate(("gelatina", "neblina", "maionese")):
            pilula_em(c, t, C["s09.e"] + 0.3 * k, s, TX[1] - 260 + 260 * k, yb + 250, 40, TINTA2, "b")


# ---------------- efeito Tyndall ----------------
def farol(c, x, y, a=1.0):
    """farol de carro na neblina: o cone de luz aparece"""
    if a <= 0:
        return
    for k in range(7):
        c.drawCircle(x + 40 + 70 * k, y + 30 * math.sin(k * 1.7), 120, M.paint("#C9CFD6", 0.16 * a))
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(x, y), skia.Point(x + 460, y)], [M.hexc("#FFF6C8", 0.95 * a), M.hexc("#FFF6C8", 0.0)]))
    pth = skia.Path(); pth.moveTo(x, y - 18); pth.lineTo(x + 460, y - 120); pth.lineTo(x + 460, y + 120); pth.lineTo(x, y + 18); pth.close()
    c.drawPath(pth, p)
    M.rrect(c, x - 54, y - 30, 60, 60, 14, "#3A3B42", a)
    c.drawCircle(x, y, 18, M.paint("#FFF6C8", a))


def fresta(c, x, y, a=1.0):
    """raio de sol entrando por uma fresta, com poeira"""
    if a <= 0:
        return
    M.rrect(c, x - 30, y - 150, 60, 300, 6, "#3A3B42", a)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(x, y), skia.Point(x + 440, y + 120)], [M.hexc("#FFE08A", 0.85 * a), M.hexc("#FFE08A", 0.0)]))
    pth = skia.Path(); pth.moveTo(x + 30, y - 30); pth.lineTo(x + 460, y + 30); pth.lineTo(x + 420, y + 200); pth.lineTo(x + 30, y + 30); pth.close()
    c.drawPath(pth, p)
    rnd = random.Random(2)
    for k in range(24):
        u = rnd.random()
        xx = x + 50 + u * 380
        yy = y + lerp(-10, 120, u) * rnd.random() + 10 + 5 * math.sin(k + 0.002 * xx)
        c.drawCircle(xx, yy, 2.6, M.paint("#FFF3C4", 0.9 * a))


def b_tyndall(c, t, C, b):
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10"], ps("e aí entra a luz", "i", 76, TINTA2), XE, 180, passo=0.12)
            yb, w, h = 820, 380, 420
            for k, (cx, tipo, liq, ti, br, nome) in enumerate(((560, "sol", Q.AGUA, C["s10.a"], 0.0, "solução"), (1360, "col", LEITE, C["s10.b"], 1.0, "coloide"))):
                frasco(c, t, ti - 0.3, cx, yb, w, h, liq, tipo)
                yy = yb - h * 0.42
                E.foco(c, t, ti - 0.1, 0.4, lambda a, cx=cx, yy=yy: caneta_laser(c, cx - w / 2 - 70, yy, a))
                feixe(c, t, ti + 0.3, cx - w / 2 - 66, cx - w / 2, cx + w / 2 - 6, yy, br)
                E.frase(c, t, ti, [(nome, "g", 66, COR)], cx, 330, "center")
            rotulo(c, t, C["s10.a"] + 1.4, "o feixe passa sem ser visto", 560, yb + 80, 44)
            rotulo(c, t, C["s10.c"], "o caminho do feixe aparece", 1360, yb + 80, 44, COR)
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    if t < C["s12"]:
        def s11():
            E.frase(c, t, C["s11.a"], ps("efeito", "i", 100), XE, 260)
            E.frase(c, t, C["s11.a"] + 0.4, [("Tyndall", "g", 150, COR)], XE + 330, 260)
            E.foco(c, t, C["s11.b"], 0.6, lambda a: farol(c, 300, 640, a))
            rotulo(c, t, C["s11.b"] + 0.4, "farol na neblina", 500, 880, 50)
            E.foco(c, t, C["s11.c"], 0.6, lambda a: fresta(c, 1150, 560, a))
            rotulo(c, t, C["s11.c"] + 0.4, "sol na poeira", 1400, 880, 50)
        E.saida(c, t, C["s12"] - 0.1, s11)
        return
    yb, w, h = 820, 380, 420
    cx = 1300
    E.frase(c, t, C["s12"], [("suspensão", "g", 76, COR)], XE, 260)
    E.frase(c, t, C["s12.a"], ps("também mostra o feixe", "i", 70), XE, 370, passo=0.12)
    frasco(c, t, C["s12"], cx, yb, w, h, TERRA, "sus", assenta=ease_io(prog(t, C["s12.b"], 1.8)), semente=9)
    yy = yb - h * 0.42
    E.foco(c, t, C["s12"] + 0.2, 0.4, lambda a: caneta_laser(c, cx - w / 2 - 70, yy, a))
    feixe(c, t, C["s12.a"] + 0.3, cx - w / 2 - 66, cx - w / 2, cx + w / 2 - 6, yy, 1.0 - 0.6 * ep(t, C["s12.b"] + 1.0, 1.0))
    E.frase(c, t, C["s12.b"], ps("mas, com o tempo,", "i", 70), XE, 600, passo=0.12)
    E.frase(c, t, C["s12.b"] + 0.8, [("assenta", "g", 110, COR)], XE, 740)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("parece homogêneo, então é solução?", "i", 64), XE + 440, 190, passo=0.1)
    cx, yb, w, h = 1360, 860, 400, 440
    frasco(c, t, C["s13.b"], cx, yb, w, h, LEITE, "col")
    rotulo(c, t, C["s13.b"] + 0.3, "água com leite", cx, yb + 80, 50)

    def errado():
        E.frase(c, t, C["s13.b"] + 0.6, [("solução", "g", 100, ERRADO)], XE, 520)
        if t >= C["s13.c"] + 0.4:
            E.risco(c, XE - 10, 545, XE + 470, 450, t, C["s13.c"] + 0.4, largura=12)
    E.saida(c, t, C["s13.d"] + 1.2, errado)
    yy = yb - h * 0.42
    E.foco(c, t, C["s13.c"] - 0.2, 0.4, lambda a: caneta_laser(c, cx - w / 2 - 70, yy, a))
    feixe(c, t, C["s13.c"], cx - w / 2 - 66, cx - w / 2, cx + w / 2 - 6, yy, 1.0)
    E.foco(c, t, C["s13.d"], 0.5, lambda a: (E.pilula(c, "coloide", XE + 230, 700, 80, "g", fundo=E.COR, a=a), E.selo(c, XE + 560, 690, 50, True, a)))
    E.frase(c, t, C["s13.e"], ps("o olho não basta:", "i", 64) + [("quem", "i", 64), ("decide", "i", 64), ("é", "i", 64), ("a", "i", 64), ("luz", "g", 62, COR)], XE, 930, passo=0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        def s14():
            E.frase(c, t, C["s14"], ps("duas perguntas, nesta ordem", "i", 70, CLARO), W / 2, 150, "center", 0.12)
            # pergunta 1
            E.foco(c, t, C["s14.a"], 0.5, lambda a: (E.bola(c, XE + 40, 304, 44, a=a), centro(c, "1", XE + 40, 326, 54, "g", BR, a)))
            E.frase(c, t, C["s14.a"] + 0.1, [("assenta", "g", 76, BR), ("com", "i", 80, CLARO), ("o", "i", 80, CLARO), ("tempo?", "i", 80, CLARO)], XE + 110, 330, passo=0.12)
            p = ep(t, C["s14.b"], 0.5)
            if p > 0:
                M.arrow(c, 1180, 305, 1330, 305, E.CLARO, p, 6, 22, ease_io(p))
            E.frase(c, t, C["s14.b"] - 0.2, [("sim", "g", 50, CLARO)], 1190, 280)
            pilula_em(c, t, C["s14.b"] + 0.2, "suspensão", 1560, 305, 64, E.COR)
            # pergunta 2
            E.foco(c, t, C["s14.c"], 0.5, lambda a: (E.bola(c, XE + 40, 564, 44, a=a), centro(c, "2", XE + 40, 586, 54, "g", BR, a)))
            E.frase(c, t, C["s14.c"] + 0.1, [("o", "i", 80, CLARO), ("feixe", "g", 76, BR), ("aparece?", "i", 80, CLARO)], XE + 110, 590, passo=0.12)
            E.frase(c, t, C["s14.c"] - 0.3, ps("se não assenta:", "i", 50, CLARO), XE + 110, 480, passo=0.1)
            for k, (ti, s, y, fundo) in enumerate(((C["s14.d"], "coloide", 520, E.COR), (C["s14.e"], "solução", 760, "#3A3B42"))):
                p = ep(t, ti, 0.5)
                if p > 0:
                    M.arrow(c, 1000, 565, 1330, y, E.CLARO, p, 6, 22, ease_io(p))
                E.frase(c, t, ti - 0.2, [("sim" if k == 0 else "não", "g", 50, CLARO)], 1120, y - 40 + (0 if k == 0 else 40))
                pilula_em(c, t, ti + 0.2, s, 1560, y, 64, fundo)
            pass
        E.saida(c, t, C["s15"] - 0.1, s14)
        return
    E.frase(c, t, C["s15.a"], ps("a ordem importa:", "i", 70, CLARO), W / 2, 220, "center", 0.12)
    E.frase(c, t, C["s15.a"] + 0.8, ps("a suspensão", "i", 70, CLARO) + [("também", "g", 66, BR)] + ps("mostra o feixe", "i", 70, CLARO), W / 2, 330, "center", 0.12)
    E.frase(c, t, C["s15.a"] + 2.8, ps("comece pelo fundo do copo", "i", 64, CLARO), W / 2, 440, "center", 0.1)
    E.frase(c, t, C["s15.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("mistura escura, como tinta", "i", 66, CLARO), W / 2, 640, "center", 0.12)
    Q.bequer(c, t, C["s15.b"] + 0.6, W / 2, 960, 220, 220, 0.75, "#1D1F3A", graduacao=False, escuro=True)
    E.foco(c, t, C["s15.b"] + 1.2, 0.4, lambda a: caneta_laser(c, W / 2 - 180, 900, a))
    feixe(c, t, C["s15.b"] + 1.4, W / 2 - 176, W / 2 - 110, W / 2 - 110, 900, 0.0, d=0.3)
    pilula_em(c, t, C["s15.b"] + 2.6, "a luz nem atravessa: veja se assenta", W / 2 + 470, 790, 40, E.COR, "b")


# ---------------- questão ----------------
QX = (440, 960, 1480)


def tres_copos(c, t, t0s, yb=900, w=250, h=280, resp=None):
    """os três copos da questão: 1 solução, 2 coloide, 3 suspensão (com camada no fundo)"""
    dados = ((Q.AGUA, "sol", 0.0, False), (LEITE, "col", 1.0, False), (TERRA, "sus", 1.0, True))
    for k, ((liq, tipo, br, ass), t0) in enumerate(zip(dados, t0s)):
        cx = QX[k]
        frasco(c, t, t0, cx, yb, w, h, liq, tipo, assenta=0.85 if ass and t >= t0 + 1.2 else 0.0, semente=4 + k)
        yy = yb - h * 0.45
        E.foco(c, t, t0, 0.4, lambda a, cx=cx, yy=yy: caneta_laser(c, cx - w / 2 - 40, yy, a, comp=110))
        feixe(c, t, t0 + 0.4, cx - w / 2 - 36, cx - w / 2, cx + w / 2 - 6, yy, br)
        E.foco(c, t, t0, 0.4, lambda a, cx=cx, k=k: (E.bola(c, cx, yb + 70, 36, TINTA, a), centro(c, str(k + 1), cx, yb + 89, 46, "g", BR, a)))


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 170)
    if t < C["s17"]:
        tres_copos(c, t, (C["s16.a"], C["s16.b"], C["s16.c"]), yb=600)
        for k, (ti, l1, l2) in enumerate(((C["s16.a"], "feixe não aparece", "nada assenta"), (C["s16.b"], "feixe aparece", "nada assenta"),
                                           (C["s16.c"], "feixe aparece", "camada no fundo"))):
            rotulo(c, t, ti + 0.6, l1, QX[k], 760, 42, TINTA)
            rotulo(c, t, ti + 1.2, l2, QX[k], 815, 42, TINTA)
        E.frase(c, t, C["s16.d"], [("1", "g", 56, COR)] + ps("classifique os três copos", "i", 60), XE, 930, passo=0.1)
        E.frase(c, t, C["s16.e"], [("2", "g", 56, COR)] + ps("água com açúcar: qual é o soluto?", "i", 60), XE, 1020, passo=0.1)
    else:
        E.frase(c, t, C["s17"], [("1", "g", 56, COR)] + ps("classifique os três copos", "i", 60), XE, 400, passo=0.05)
        E.frase(c, t, C["s17"], [("2", "g", 56, COR)] + ps("água com açúcar: o soluto?", "i", 60), XE, 500, passo=0.05)
        E.relogio(c, t, C["s17.a"], cx=1470, cy=520, r=220)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    t0 = C["s18"] - 0.3
    tres_copos(c, t, (t0, t0, t0), yb=640, w=240, h=270)
    for k, (ti, s) in enumerate(((C["s18.c"], "solução"), (C["s18.b"], "coloide"), (C["s18.a"], "suspensão"))):
        E.foco(c, t, ti, 0.5, lambda a, k=k, s=s: (E.pilula(c, s, QX[k], 820, 52, "g", fundo=E.COR, a=a)))
    E.frase(c, t, C["s18"], ps("assenta?", "i", 56, TINTA2), XE - 40, 200)
    E.frase(c, t, C["s18.a"] - 0.9, ps("o feixe aparece?", "i", 56, TINTA2), XE - 40, 280)
    E.frase(c, t, C["s18.d"], [("soluto:", "i", 64), ("açúcar", "g", 64, COR)], XE + 120, 990, passo=0.12)
    E.frase(c, t, C["s18.e"], [("solvente:", "i", 64), ("água", "g", 64, COR)], XE + 820, 990, passo=0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s19.a", [("soluto", "g", 66), ("se", "i", 70), ("dissolve", "i", 70), ("no", "i", 70), ("solvente", "g", 66)]),
                 ("s19.b", [("suspensão", "g", 66), ("=", "g", 66, TINTA2), ("assenta", "i", 70)]),
                 ("s19.c", [("coloide", "g", 66), ("=", "g", 66, TINTA2), ("mostra", "i", 70), ("o", "i", 70), ("feixe", "i", 70)]),
                 ("s19.d", [("solução", "g", 66), ("=", "g", 66, TINTA2), ("não", "i", 70), ("mostra", "i", 70), ("nada", "i", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("solubilidade", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s20.b"], ps("o limite muda com a temperatura", "i", 64), XE, 510, passo=0.1)
    Q.solubilidade(c, t, C["s20.b"] + 0.3, XE + 60, 610, 600, 300, [dict(nome="", pts=[(0, 13), (20, 32), (40, 64), (60, 110), (80, 169)])],
                   tmax=80, smax=180, passo=20, passo_y=60, size=30)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 460, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(760, 485, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, soluto=b_soluto, tipos=b_tipos, tyndall=b_tyndall, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
