"""Visual — Estudativo · QUI-AMB-003: efeito estufa e camada de ozônio.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a LINGUAGEM VISUAL DA QUÍMICA AMBIENTAL
(cabeçalho de QUI-AMB-001/roteiro/visual.py). Nesta aula:
- ATMOSFERA em corte (ceu): chão embaixo, céu em faixas de azul; Sol no canto de cima.
- LUZ QUE CHEGA do Sol = setas amarelas retas; ULTRAVIOLETA = setas violeta (UV); CALOR QUE SAI do chão (infravermelho) =
  setas âmbar onduladas (IR), que voltam para baixo quando batem num gás estufa.
- CAMADA DE OZÔNIO = faixa turquesa no alto (15 a 35 km), com moléculas de O₃; o cloro do CFC é a bolinha verde do Cl.
- Efeito estufa à esquerda/âmbar; camada de ozônio à direita/violeta, sempre nessa ordem nas comparações.
Peças candidatas ao kit: ceu (corte da atmosfera), seta_ir (onda), cfc (molécula CCl₂F₂), termometro.
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
ARQUIVO_FINAL = "estudativo_QUI-AMB-003_efeito_estufa_e_ozonio.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("estufa", "ozonio", "chao", "atalho", "questao", "fim"))
BR = "#FFFFFF"
SOL, UV, IR = "#F5B400", "#7B3FE4", "#E07B12"
CFC = dict(atomos=[("C", 0, 0), ("Cl", -1.0, -0.5), ("Cl", 1.0, -0.5), ("F", -0.55, 0.85), ("F", 0.55, 0.85)],
           ligacoes=[(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1)])
assert round(420 / 280 - 1, 2) == 0.5      # CO₂ do ar: +50% desde o começo das fábricas
assert 15 - (-18) == 33                    # o efeito estufa natural vale cerca de 33 °C
QUESTAO = {1: "estufa", 2: "ozônio", 3: "estufa", 4: "ozônio"}
assert list(QUESTAO.values()).count("estufa") == 2


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


def ceu(c, x, y, w, h, a=1.0, chao=90):
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, y), skia.Point(0, y + h)], [M.hexc("#CFE3F5", a), M.hexc("#EEF6FB", a)]))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 28, 28), p)
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 28, 28), skia.ClipOp.kIntersect, True)
    c.drawRect(skia.Rect.MakeXYWH(x, y + h - chao, w, chao), M.paint("#8FB06A", a))
    c.drawRect(skia.Rect.MakeXYWH(x, y + h - chao, w, 10), M.paint("#6E8E4E", a))
    c.restore()


def sol(c, cx, cy, r, a=1.0):
    for k in range(12):
        ang = k * math.tau / 12
        M.line(c, cx + (r + 12) * math.cos(ang), cy + (r + 12) * math.sin(ang), cx + (r + 40) * math.cos(ang), cy + (r + 40) * math.sin(ang), SOL, a, 8)
    E.bola(c, cx, cy, r, "#FFC21A", a)


def seta_reta(c, x0, y0, x1, y1, cor, p=1.0, a=1.0):
    if p > 0:
        M.arrow(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), cor, a, 7, 24)


def seta_ir(c, x0, y0, x1, y1, p=1.0, a=1.0, cor=IR, fase=0.0):
    """seta ondulada (infravermelho) de (x0, y0) até (x1, y1), crescendo até p"""
    if p <= 0:
        return
    L = math.dist((x0, y0), (x1, y1))
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    nx, ny = -uy, ux
    pth = skia.Path()
    n = 40
    for k in range(n + 1):
        s = k / n * p
        w = 16 * math.sin(s * L / 40 * math.pi + fase)
        x, y = x0 + ux * s * L + nx * w, y0 + uy * s * L + ny * w
        pth.moveTo(x, y) if k == 0 else pth.lineTo(x, y)
    c.drawPath(pth, M.paint(cor, a, stroke=7))
    xe, ye = x0 + ux * p * L, y0 + uy * p * L
    tri = skia.Path(); tri.moveTo(xe + ux * 20, ye + uy * 20); tri.lineTo(xe + nx * 14, ye + ny * 14); tri.lineTo(xe - nx * 14, ye - ny * 14); tri.close()
    c.drawPath(tri, M.paint(cor, a))


def termometro(c, cx, cy, h, nivel, cor, a=1.0, txt=None):
    M.rrect(c, cx - 22, cy - h, 44, h, 22, BR, a, stroke=4, stroke_color=Q.VIDRO)
    M.rrect(c, cx - 12, cy - h * nivel, 24, h * nivel, 12, cor, a)
    E.bola(c, cx, cy + 20, 38, cor, a)
    if txt:
        centro(c, txt, cx, cy + 120, 56, "g", TINTA, a)


def gases(c, t, t0, x, y, w, h, n=8, tipos=("CO2", "CH4"), a=1.0, semente=3):
    rnd = random.Random(semente)
    for k in range(n):
        ti = t0 + 0.15 * k
        if t < ti:
            continue
        m = tipos[k % len(tipos)]
        Q.molecula_desenho(c, m, x + rnd.random() * w + 8 * math.sin(t + k), y + rnd.random() * h + 6 * math.cos(t * 1.2 + k), 46, ep(t, ti, 0.4) * a, giro=rnd.random() * 360)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("o buraco na camada de ozônio", "i", 70), XE, 220, passo=0.1)
        E.frase(c, t, C["s01.a"] + 1.4, [("esquenta", "g", 90), ("o", "i", 90), ("planeta?", "g", 90, COR)], XE, 340, passo=0.12)
        E.foco(c, t, C["s01.b"], 0.4, lambda a: E.selo(c, 1500, 290, 80, False, a))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: (ceu(c, 140, 470, 760, 460, a), sol(c, 260, 560, 50, a)))
        E.foco(c, t, C["s01.c"] + 0.3, 0.5, lambda a: (ceu(c, 1020, 470, 760, 460, a), sol(c, 1140, 560, 50, a), M.rrect(c, 1020, 620, 760, 70, 0, E.COR, 0.7 * a)))
        if t >= C["s01.c"]:
            for k in range(3):
                seta_ir(c, 380 + 160 * k, 830, 420 + 160 * k, 560, ep(t, C["s01.c"] + 0.5 + 0.2 * k, 0.8), 1, fase=t * 4)
                seta_reta(c, 1240 + 150 * k, 520, 1240 + 150 * k, 610, UV, ep(t, C["s01.c"] + 0.8 + 0.2 * k, 0.6))
        E.frase(c, t, C["s01.c"] + 0.4, [("efeito", "g", 54), ("estufa", "g", 54, IR)], 520, 1010, "center", 0.1)
        E.frase(c, t, C["s01.c"] + 0.8, [("camada", "g", 54), ("de", "i", 54), ("ozônio", "g", 54, UV)], 1400, 1010, "center", 0.1)
        E.foco(c, t, C["s01.d"], 0.4, lambda a: centro(c, "≠", W / 2, 740, 140, "g", ERRADO, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.a"] + 0.6, [("estufa", "g", 62, IR), ("ou", "i", 66), ("ozônio?", "g", 62, UV)]),
                 (C["s02.b"], [("os", "i", 66), ("gases", "g", 62, COR), ("de", "i", 66), ("cada", "i", 66), ("um", "i", 66)]),
                 (C["s02.c"], [("onde", "i", 66), ("o", "i", 66), ("ozônio", "g", 62), ("protege", "g", 62, COR), ("e", "i", 66), ("polui", "g", 62, ERRADO)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("três lembretes", "i", 80, TINTA2), XE, 200, passo=0.12)
    Q.molecula(c, t, C["s03.a"], "O3", 300, 400, 80)
    Q.molecula(c, t, C["s03.a"] + 0.6, "O2", 560, 410, 80)
    E.frase(c, t, C["s03.a"] + 0.4, ps("ozônio: alótropo do oxigênio", "i", 58), 720, 420, passo=0.08)
    Q.molecula(c, t, C["s03.b"], "CO2", 340, 620, 80)
    E.frase(c, t, C["s03.b"] + 0.4, ps("combustível fóssil põe carbono novo no ar", "i", 58), 720, 630, passo=0.08)
    Q.molecula(c, t, C["s03.c"], CFC, 360, 860, 70)
    E.frase(c, t, C["s03.c"] + 0.4, [("CFC:", "g", 60, COR)] + ps("cloro e flúor; solta cloro na luz forte", "i", 58), 720, 860, passo=0.08)


# ---------------- efeito estufa ----------------
def b_estufa(c, t, C, b):
    if t < C["s05"]:
        ceu(c, 120, 120, 1680, 860, ep(t, C["s04"], 0.5))
        E.foco(c, t, C["s04"], 0.5, lambda a: sol(c, 280, 260, 70, a))
        for k in range(4):
            seta_reta(c, 380 + 120 * k, 320 + 30 * k, 600 + 120 * k, 860, SOL, ep(t, C["s04.a"] + 0.2 * k, 0.8))
        E.foco(c, t, C["s04.a"] + 0.4, 0.4, lambda a: E.escreve(c, "luz do Sol", 640, 330, 48, "b", "#A07400", a))
        for k in range(4):
            x0 = 1000 + 170 * k
            seta_ir(c, x0, 870, x0 + 40, 380, ep(t, C["s04.b"] + 0.2 * k, 1.0), 1, fase=t * 4)
        E.foco(c, t, C["s04.b"] + 0.6, 0.4, lambda a: E.escreve(c, "calor saindo: infravermelho", 980, 950, 46, "b", IR, a))
        gases(c, t, C["s04.c"], 980, 220, 700, 150, 8)
        if t >= C["s04.d"]:
            for k in range(3):
                x0 = 1080 + 220 * k
                seta_ir(c, x0, 300, x0 - 60, 820, ep(t, C["s04.d"] + 0.2 * k, 1.0), 1, IR, fase=t * 4)
            E.foco(c, t, C["s04.d"] + 0.6, 0.4, lambda a: E.pilula(c, "parte volta para baixo", 640, 170, 44, "b", fundo=IR, a=a))
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("isso", "i", 80), ("é", "i", 80), ("bom", "g", 90, COR)], XE, 260, passo=0.12)
        E.foco(c, t, C["s05.b"], 0.5, lambda a: termometro(c, 650, 760, 360, 0.15, "#6FA8FF", a, "−18 °C"))
        E.foco(c, t, C["s05.b"] + 0.4, 0.4, lambda a: centro(c, "sem efeito estufa", 650, 960, 44, "i", TINTA2, a))
        E.foco(c, t, C["s05.c"], 0.5, lambda a: termometro(c, 1250, 760, 360, 0.55, IR, a, "15 °C"))
        E.foco(c, t, C["s05.c"] + 0.4, 0.4, lambda a: centro(c, "com efeito estufa", 1250, 960, 44, "i", TINTA2, a))
        pilula_em(c, t, C["s05.d"], "o problema: gás demais, calor demais", 1300, 260, 46, ERRADO, "b")
        return
    E.frase(c, t, C["s06.a"], [("culpado", "g", 70), ("número", "i", 70), ("1:", "g", 70)], XE, 200, passo=0.12)
    Q.formula_em(c, t, C["s06.a"] + 0.4, "CO2", XE + 720, 205, 90, cores={"CO2": E.COR})
    E.foco(c, t, C["s06.a"] + 1.0, 0.4, lambda a: E.escreve(c, "petróleo, carvão, gás e queimadas", XE, 280, 46, "i", TINTA2, a))
    for k, (rot, v, ti) in enumerate((("antes das fábricas", 280, C["s06.b"]), ("hoje", 420, C["s06.b"] + 0.8))):
        y = 360 + 110 * k
        if t >= ti:
            q = ep(t, ti, 0.4)
            E.escreve(c, rot, 640 - E.larg(rot, "b", 46), y + 50, 46, "b", TINTA, q)
            M.rrect(c, 680, y, 2.2 * v * ease_io(prog(t, ti, 0.8)), 66, 33, CINZA if k == 0 else E.COR, q)
    E.foco(c, t, C["s06.b"] + 1.6, 0.4, lambda a: E.escreve(c, "+50%", 1640, 520, 70, "g", COR, a))
    E.frase(c, t, C["s06.c"], [("número", "i", 64), ("2:", "g", 64)], XE, 700, passo=0.12)
    Q.formula_em(c, t, C["s06.c"] + 0.4, "CH4", XE + 360, 705, 80, cores={"CH4": E.COR})
    E.foco(c, t, C["s06.c"] + 0.8, 0.4, lambda a: E.escreve(c, "metano", XE + 560, 700, 54, "i", TINTA2, a))
    for k, s in enumerate(("arroto do gado", "lixões", "arroz alagado")):
        pilula_em(c, t, C["s06.d"] + 0.4 * k, s, XE + 170 + 330 * k, 820, 44, TINTA)
    E.foco(c, t, C["s06.e"], 0.4, lambda a: E.escreve(c, "1 kg de metano segura dezenas de vezes mais calor", XE, 960, 50, "b", COR, a))


# ---------------- camada de ozônio ----------------
def b_ozonio(c, t, C, b):
    x, y, w, h = 300, 100, 1500, 880
    ceu(c, x, y, w, h, ep(t, C["s07"], 0.5))
    Y = lambda km: y + h - 90 - (h - 140) * km / 50
    if t >= C["s07"]:
        q = ep(t, C["s07"], 0.5)
        M.line(c, 220, Y(0), 220, Y(50), TINTA2, q, 4)
        for km in (0, 15, 35, 50):
            M.line(c, 205, Y(km), 235, Y(km), TINTA2, q, 4)
            E.escreve(c, f"{km} km", 60, Y(km) + 14, 38, "b", TINTA2, q)
    if t >= C["s07.a"]:
        p = ease_io(prog(t, C["s07.a"], 1.0))
        c.drawRect(skia.Rect.MakeLTRB(x, Y(35), x + w * p, Y(15)), M.paint(E.COR, 0.45))
        E.foco(c, t, C["s07.b"], 0.4, lambda a: E.escreve(c, "camada de ozônio", x + 40, Y(25) + 20, 56, "g", COR, a))
        if t >= C["s07.b"] and t < C["s08.d"] + 2:
            rnd = random.Random(5)
            for k in range(9):
                Q.molecula_desenho(c, "O3", x + 640 + rnd.random() * 780, Y(17 + rnd.random() * 16), 34, ep(t, C["s07.b"] + 0.1 * k, 0.3), giro=rnd.random() * 360)
    E.foco(c, t, C["s07.c"] - 0.4, 0.4, lambda a: sol(c, x + w - 120, y + 90, 50, a))
    if t >= C["s07.c"]:
        for k in range(4):
            xx = x + 700 + 180 * k
            seta_reta(c, xx, y + 60, xx, Y(31), UV, ep(t, C["s07.c"] + 0.15 * k, 0.6))
        E.foco(c, t, C["s07.c"] + 0.4, 0.4, lambda a: E.escreve(c, "ultravioleta", x + 340, y + 70, 46, "g", UV, a))
    if C["s07.d"] <= t < C["s08"]:
        pilula_em(c, t, C["s07.d"], "queima a pele, causa câncer de pele, danifica os olhos", W / 2 + 100, Y(5) - 10, 40, UV, "b")
    if t >= C["s08"]:
        u = ease_io(prog(t, C["s08.b"], 2.5))
        cx, cy = lerp(700, 900, u), lerp(Y(1), Y(24), u)
        if t < C["s08.c"] + 0.5:
            Q.molecula(c, t, C["s08.a"], CFC, cx, cy, 50)
        E.foco(c, t, C["s08.a"], 0.4, lambda a: E.escreve(c, "CFC: geladeiras e sprays antigos", x + 40, Y(9), 46, "b", TINTA, a))
        if t >= C["s08.c"]:
            uu = ease_io(prog(t, C["s08.c"] + 0.4, 3.0))
            clx = lerp(900, 1600, uu)
            Q.atomo(c, clx, Y(24) + 30 * math.sin(t * 6), 26, "Cl")
            E.foco(c, t, C["s08.c"] + 0.2, 0.4, lambda a: E.escreve(c, "a luz UV solta o cloro", 880, Y(38), 46, "b", TINTA, a))
        if t >= C["s08.d"]:
            n = int(lerp(0, 3000, ep(t, C["s08.d"], 3.0)))
            E.foco(c, t, C["s08.d"], 0.4, lambda a: E.escreve(c, f"O₃ destruídas: {n:,}".replace(",", "."), 1120, Y(9), 52, "g", ERRADO, a))
        pilula_em(c, t, C["s08.e"], "o cloro é catalisador: sai inteiro", 1350, Y(2.5), 44, E.COR)
    if t >= C["s09"]:
        E.foco(c, t, C["s09.a"], 0.4, lambda a: (M.rrect(c, 460, 360, 1000, 330, 30, BR, a, stroke=4, stroke_color=FIO),
                                                E.escreve(c, "1987: Protocolo de Montreal", 520, 460, 60, "g", TINTA, a)))
        E.foco(c, t, C["s09.b"], 0.4, lambda a: E.escreve(c, "todos os países aderiram; o CFC foi proibido", 520, 550, 44, "b", TINTA2, a))
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "a camada está se recuperando, devagar", 520, 630, 46, "g", CERTO, a))


# ---------------- ozônio perto do chão ----------------
def b_chao(c, t, C, b):
    ceu(c, 120, 140, 1680, 840, ep(t, C["s10"], 0.5), chao=120)
    E.foco(c, t, C["s10"], 0.4, lambda a: M.rrect(c, 120, 260, 1680, 90, 0, E.COR, 0.4 * a))
    E.foco(c, t, C["s10"], 0.4, lambda a: E.escreve(c, "no alto: protege", 160, 320, 50, "g", COR, a))
    for k in range(5):
        xx = 300 + 280 * k
        E.foco(c, t, C["s10.a"] + 0.1 * k, 0.4, lambda a, xx=xx: (M.rrect(c, xx, 820, 130, 40, 12, "#4A5568", a), c.drawCircle(xx + 30, 865, 14, M.paint("#2A2B31", a)), c.drawCircle(xx + 100, 865, 14, M.paint("#2A2B31", a))))
    if t >= C["s10.b"]:
        rnd = random.Random(8)
        for k in range(10):
            Q.molecula_desenho(c, "O3", 300 + rnd.random() * 1300, 620 + rnd.random() * 160, 40, ep(t, C["s10.b"] + 0.15 * k, 0.3), giro=rnd.random() * 360)
    E.frase(c, t, C["s10.a"], ps("o ozônio também se forma perto do chão", "i", 58), 160, 470, passo=0.08)
    E.frase(c, t, C["s10.b"], ps("gases do escapamento + luz do Sol", "i", 52, TINTA2), 160, 550, passo=0.08)
    pilula_em(c, t, C["s10.c"], "irrita os olhos e o pulmão: é poluente", 1300, 520, 44, ERRADO, "b")
    E.foco(c, t, C["s10.e"], 0.4, lambda a: E.escreve(c, "aqui embaixo: polui", 160, 940, 54, "g", ERRADO, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], ps("o atalho:", "i", 66, CLARO) + [("a", "i", 66, CLARO), ("direção", "g", 62, BR), ("da", "i", 66, CLARO), ("luz", "g", 62, E.CLARO)], XE, 160, passo=0.1)
        for k, (key, nome, cor) in enumerate((("s11.b", "efeito estufa", "#F5A04A"), ("s11.d", "camada de ozônio", "#B79CFF"))):
            x = 200 + 820 * k
            E.foco(c, t, C[key], 0.4, lambda a, x=x, nome=nome, cor=cor: (M.rrect(c, x, 260, 720, 700, 30, "#14141E", a), E.escreve(c, nome, x + 40, 350, 64, "g", cor, a)))
        E.foco(c, t, C["s11.b"] + 0.4, 0.4, lambda a: seta_ir(c, 400, 640, 400, 430, 1, a, "#F5A04A", fase=t * 4))
        E.foco(c, t, C["s11.b"] + 0.6, 0.4, lambda a: E.escreve(c, "segura o calor que sai", 480, 540, 46, "b", BR, a))
        Q.formula_em(c, t, C["s11.c"], "CO2 + CH4", 260, 760, 76, escuro=True)
        E.foco(c, t, C["s11.c"] + 0.6, 0.4, lambda a: E.escreve(c, "resultado: aquecimento", 260, 880, 50, "g", "#F5A04A", a))
        E.foco(c, t, C["s11.d"] + 0.4, 0.4, lambda a: seta_reta(c, 1220, 430, 1220, 640, "#B79CFF", 1, a))
        E.foco(c, t, C["s11.d"] + 0.6, 0.4, lambda a: E.escreve(c, "barra a luz que chega", 1300, 540, 46, "b", BR, a))
        E.foco(c, t, C["s11.e"], 0.4, lambda a: E.escreve(c, "culpado: CFC", 1080, 770, 64, "g", BR, a))
        E.foco(c, t, C["s11.e"] + 0.6, 0.4, lambda a: E.escreve(c, "resultado: mais UV na pele", 1080, 880, 50, "g", "#B79CFF", a))
        return
    E.frase(c, t, C["s12.a"], [("infravermelho", "g", 70, "#F5A04A"), ("saindo,", "i", 70, CLARO), ("ultravioleta", "g", 70, "#B79CFF"), ("entrando", "i", 70, CLARO)], W / 2, 360, "center", 0.12)
    E.frase(c, t, C["s12.b"], ps("a principal ponte entre os dois:", "i", 60, CLARO), W / 2, 560, "center", 0.1)
    E.frase(c, t, C["s12.c"], [("o", "i", 66, CLARO), ("CFC", "g", 70, BR), ("também", "i", 66, CLARO), ("é", "i", 66, CLARO), ("gás", "g", 66, E.CLARO), ("estufa", "g", 66, E.CLARO)], W / 2, 700, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    riscado(c, t, C["s13.a"], "o buraco no ozônio aumenta o aquecimento global", XE, 340, 56)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: (seta_reta(c, 520, 460, 520, 760, UV, 1, a), E.escreve(c, "mais UV:", 600, 600, 60, "g", UV, a),
                                            E.escreve(c, "queima a pele", 600, 680, 56, "i", TINTA, a)))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: (seta_ir(c, 1180, 760, 1180, 460, 1, a, fase=t * 4), E.escreve(c, "calor preso:", 1260, 600, 60, "g", IR, a),
                                            E.escreve(c, "aquece o planeta", 1260, 680, 56, "i", TINTA, a)))
    pilula_em(c, t, C["s13.c"] + 1.2, "o aquecimento vem dos gases estufa", W / 2, 920, 50, E.COR)


# ---------------- questão ----------------
FATOS = ("o gado solta metano", "mais ultravioleta chega ao chão no sul", "a queima de carvão aumenta o CO₂", "gás de geladeira antiga solta cloro no alto")


def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s14"] + 1.0, [("estufa", "g", 56, IR), ("ou", "i", 56, TINTA2), ("ozônio?", "g", 56, UV)], XE, 290, passo=0.1)
    for k, key in enumerate(("s14.a", "s14.b", "s14.c", "s14.d")):
        y = 430 + 150 * k
        E.frase(c, t, C[key], [(str(k + 1), "g", 60, COR), (FATOS[k], "b", 56)], XE, y, passo=0.12)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=1600, cy=560, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    for k, key in enumerate(("s16.a", "s16.b", "s16.c", "s16.d")):
        y = 230 + 150 * k
        E.escreve(c, f"{k + 1}  {FATOS[k]}", XE, y, 52, "b", TINTA, ep(t, C["s16"], 0.4))
        tipo = QUESTAO[k + 1]
        pilula_em(c, t, C[key], "efeito estufa" if tipo == "estufa" else "camada de ozônio", 1560, y - 18, 46, IR if tipo == "estufa" else UV)
    E.frase(c, t, C["s17.a"], ps("meio a meio: 1 e 3 estufa, 2 e 4 ozônio", "i", 58), XE, 860, passo=0.08)
    riscado(c, t, C["s17.b"], "UV no efeito estufa: trocou as luzes", XE, 980, 52)
    pilula_em(c, t, C["s17.c"], "estufa: calor que sai · ozônio: luz que entra", 1300, 1040, 40, E.COR, "b")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s18.a", [("estufa:", "g", 62, IR), ("segura", "i", 66), ("o", "i", 66), ("calor,", "i", 66), ("com", "i", 66), ("CO₂", "g", 62), ("e", "i", 66), ("metano", "g", 62)]),
                 ("s18.b", [("ozônio:", "g", 62, UV), ("barra", "i", 66), ("o", "i", 66), ("UV;", "g", 62), ("o", "i", 66), ("CFC", "g", 62), ("ataca", "i", 66)]),
                 ("s18.c", [("no", "i", 66), ("alto", "g", 62, COR), ("protege,", "i", 66), ("no", "i", 66), ("chão", "g", 62, ERRADO), ("polui", "i", 66)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("Tratamento", "g", 100, COR), ("de", "i", 100), ("água", "g", 100, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s19.a"] + 0.6, ps("do rio até a torneira", "i", 80), XE, 520, passo=0.12)
    E.foco(c, t, C["s19.a"] + 0.8, 0.5, lambda a: Q.bequer(c, t, C["s19.a"] + 0.8, 500, 960, 280, 300, 0.7, Q.AGUA, graduacao=False))
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s19.b"] + 0.2, 0.4))
    E.frase(c, t, C["s19.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, estufa=b_estufa, ozonio=b_ozonio, chao=b_chao, atalho=b_atalho,
              erro=b_erro, questao=b_questao, resposta=b_resposta, fim=b_fim)
