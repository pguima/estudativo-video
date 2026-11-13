"""Visual — Estudativo · QUI-LIG-011: gelo que boia e inseto sobre a água.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), a da trilha (QUI-LIG-001) e a do módulo (QUI-LIG-006/009): água em
bola-vareta, ligação de hidrogênio = tracejado turquesa grosso. Peças próprias: REDE DO GELO (rede_gelo()) = anéis de seis
moléculas, com o vão no meio marcado em turquesa claro; LÍQUIDO (liquido()) = moléculas juntas e desordenadas; COPO com
gelo boiando (copo_gelo()); PELÍCULA (pelicula()) = moléculas da superfície com setas de puxão; INSETO (inseto()) com as
patas afundando a película; TUBOS FINOS (tubos()) com a água subindo mais no mais fino. Densidade sempre em g/cm³ na grotesca.
Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ligações Químicas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-LIG-011_gelo_que_boia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("gelo", "tensao", "tubo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
GELO = "#DDF1FA"

assert abs(920 / 1000 - 0.92) < 1e-9 and 460 / 1 == 460 and abs(460 / 0.92 - 500) < 1e-9 and 500 - 460 == 40


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def agua(c, x, y, esc, giro, a=1.0):
    Q.molecula_desenho(c, "H2O", x, y, esc, a, giro=giro, rotulos=False)


def _h(k, s=1.0):
    v = math.sin(k * 12.9898 + s * 78.233) * 43758.5453
    return v - math.floor(v)


def rede_gelo(c, t, t0, cx, cy, R=120, esc=26, a=1.0, ligacoes=True, vao=True, cols=3, rows=2):
    """anéis hexagonais de moléculas de água (vista de cima): moléculas nos vértices, ligações de H nas arestas"""
    pts = {}
    dx, dy = R * math.sqrt(3), R * 1.5
    for i in range(rows):
        for j in range(cols):
            hx = cx + (j - (cols - 1) / 2) * dx + (dx / 2 if i % 2 else 0)
            hy = cy + (i - (rows - 1) / 2) * dy
            if vao:
                q = ep(t, t0 + 0.6, 0.5) * a
                if q > 0:
                    c.drawCircle(hx, hy, R * 0.55, M.paint(E.CLARO, 0.35 * q))
            for k in range(6):
                g = math.radians(90 + 60 * k)
                p = (round(hx + R * math.cos(g), 1), round(hy + R * math.sin(g), 1))
                pts[p] = True
    vs = list(pts.keys())
    if ligacoes:
        q = ep(t, t0 + 0.4, 0.5) * a
        if q > 0:
            for i, A in enumerate(vs):
                for B in vs[i + 1:]:
                    if abs(math.dist(A, B) - R) < 2:
                        M.line(c, *A, *B, E.COR, q, 5, dash=[10, 8])
    for k, P in enumerate(vs):
        qq = ease_back(prog(t, t0 + 0.02 * k, 0.4))
        if qq > 0:
            agua(c, P[0], P[1], esc * qq, 37 * k, a)
    return vs


def liquido(c, t, t0, x, y, w, h, n=26, esc=24, a=1.0):
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    for k in range(n):
        px = x + w * _h(k, 1) + 10 * math.sin(t * 1.4 + 6 * _h(k, 3))
        py = y + h * _h(k, 2) + 8 * math.cos(t * 1.2 + 6 * _h(k, 4))
        agua(c, px, py, esc, 360 * _h(k, 5) + 30 * t * (0.5 - _h(k, 6)), q)


def copo_gelo(c, cx, yb, w, h, nivel, a=1.0, cubo=True, boia=True):
    if a <= 0:
        return
    x0 = cx - w / 2
    yl = yb - h * nivel
    pp = skia.Paint(AntiAlias=True)
    pp.setShader(skia.GradientShader.MakeLinear([skia.Point(0, yl), skia.Point(0, yb)], [M.hexc(Q.AGUA, 0.9 * a), M.hexc(M.mix(Q.AGUA, "#5AA9D6", 0.35), 0.95 * a)], [0, 1]))
    c.drawRect(skia.Rect.MakeLTRB(x0 + 4, yl, x0 + w - 4, yb - 4), pp)
    if cubo:
        s = w * 0.34
        g = skia.Paint(AntiAlias=True)
        cy = (yl - s * 0.1 + s / 2) if boia else (yb - s / 2 - 8)
        g.setShader(skia.GradientShader.MakeLinear([skia.Point(cx - s / 2, cy - s / 2), skia.Point(cx + s / 2, cy + s / 2)], [M.hexc("#FFFFFF", 0.95 * a), M.hexc("#B5DDF0", 0.95 * a)], [0, 1]))
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, (yl - s * 0.1) if boia else (yb - s - 8), s, s), 14, 14)
        c.drawRRect(r, g)
        c.drawRRect(r, M.paint("#7FB8D6", a, stroke=4))
    pth = skia.Path()
    pth.moveTo(x0 - 6, yb - h - 10); pth.lineTo(x0, yb - h); pth.lineTo(x0, yb - 16); pth.quadTo(x0, yb, x0 + 16, yb)
    pth.lineTo(x0 + w - 16, yb); pth.quadTo(x0 + w, yb, x0 + w, yb - 16); pth.lineTo(x0 + w, yb - h); pth.lineTo(x0 + w + 6, yb - h - 10)
    c.drawPath(pth, M.paint(Q.VIDRO, a, stroke=5))


def inseto(c, cx, y, a=1.0, esc=1.0):
    """inseto de pernas longas apoiado na superfície (y = linha da água)"""
    if a <= 0:
        return
    for s_ in (-1, 1):
        for k, (dx, h) in enumerate(((150, 40), (210, 10), (120, -30))):
            px = cx + s_ * dx * esc
            pth = skia.Path(); pth.moveTo(cx + s_ * 20 * esc, y - 60 * esc)
            pth.quadTo(cx + s_ * dx * 0.6 * esc, y - (110 + h) * esc, px, y - 2)
            c.drawPath(pth, M.paint("#3A2E26", a, stroke=5 * esc))
            c.drawOval(skia.Rect.MakeXYWH(px - 22 * esc, y - 4, 44 * esc, 14 * esc), M.paint("#5A88A6", 0.4 * a))
    c.drawOval(skia.Rect.MakeXYWH(cx - 70 * esc, y - 90 * esc, 140 * esc, 46 * esc), M.paint("#4A3A2E", a))
    c.drawCircle(cx + 70 * esc, y - 70 * esc, 18 * esc, M.paint("#3A2E26", a))


def superficie(c, x0, x1, y, a=1.0, cova=None):
    """linha da água com covinhas nos pontos de cova [(x, prof)]"""
    pth = skia.Path(); pth.moveTo(x0, y)
    pts = sorted(cova or [])
    for (cx, pr) in pts:
        pth.lineTo(cx - 40, y); pth.quadTo(cx, y + pr * 2, cx + 40, y)
    pth.lineTo(x1, y)
    c.drawPath(pth, M.paint("#3C8DBF", a, stroke=5))


def tubos(c, t, t0, x, ybase, nivel_bacia, a=1.0, sobe=1.0):
    """bacia com três tubos de vidro de larguras diferentes; a água sobe mais no mais fino"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    M.rrect(c, x - 60, nivel_bacia, 760, ybase - nivel_bacia, 20, Q.AGUA, q)
    for k, (wk, hk) in enumerate(((90, 60), (50, 140), (24, 300))):
        tx = x + 80 + k * 230
        top = nivel_bacia - 380
        hh = hk * sobe
        c.drawRect(skia.Rect.MakeLTRB(tx - wk / 2 + 3, nivel_bacia - hh, tx + wk / 2 - 3, nivel_bacia + 80), M.paint(M.mix(Q.AGUA, "#5AA9D6", 0.3), q))
        for s_ in (-1, 1):
            M.line(c, tx + s_ * wk / 2, top, tx + s_ * wk / 2, nivel_bacia + 80, Q.VIDRO, q, 4)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("quase todo material encolhe ao congelar", "i", 58), XE, 200, passo=0.08)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (copo_gelo(c, 520, 900, 320, 420, 0.7, a, boia=False), centro(c, "parafina: o sólido afunda", 520, 980, 44, "b", TINTA, a)))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: (copo_gelo(c, 1300, 900, 320, 420, 0.7, a, boia=True), centro(c, "água: o gelo boia", 1300, 980, 44, "b", COR, a)))
        E.frase(c, t, C["s01.d"], ps("se não boiasse, os lagos congelariam de baixo para cima", "i", 46, TINTA2), W / 2, 1050, "center", 0.06)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1660, 560, 210 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 230, passo=0.14)
    lista(c, t, [(C["s02.b"], [("por que o", "i", 70), ("gelo boia", "g", 66, COR)]),
                 (C["s02.c"], [("o", "i", 70), ("inseto", "g", 66, COR), ("sobre a água", "i", 70)]),
                 (C["s02.d"], [("a água que", "i", 70), ("sobe no tubo", "g", 66, COR)])], XE, 400, 160)
    E.frase(c, t, C["s02.e"], ps("a mesma resposta:", "i", 62) + [("ligação de hidrogênio", "g", 60, COR)], XE, 920, passo=0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("duas ideias de antes", "i", 66, TINTA2), XE, 190, passo=0.12)
    E.frase(c, t, C["s03.a"], [("densidade", "g", 66, COR), ("=", "g", 66, TINTA2)], XE, 330, passo=0.1)
    E.foco(c, t, C["s03.a"] + 0.6, 0.5, lambda a: E.formula(c, "d = f{m}{V}", XE + 470, 340, 90, "g", TINTA, a))
    E.frase(c, t, C["s03.b"], ps("menor que a da água,", "i", 60) + [("1 g/cm³,", "g", 58), ("boia", "g", 58, COR)], XE, 500, passo=0.1)
    E.frase(c, t, C["s03.c"], [("ligação de hidrogênio:", "g", 58)] + ps("o H de uma gruda no O da vizinha", "i", 58), XE, 680, passo=0.08)
    esc = 70
    P1 = Q._pontos_mol(Q._mol("H2O"), 1150, 960, esc, 270, 0)
    O, Hh = P1[0], P1[2]
    ux, uy = E._uni(*O, *Hh)
    o2 = (Hh[0] + ux * esc * 1.7 + 0.413 * esc, Hh[1] + uy * esc * 1.7)
    P2 = Q._pontos_mol(Q._mol("H2O"), *o2, esc, 270, 0)
    if t >= C["s03.d"]:
        q = ep(t, C["s03.d"], 0.4)
        M.line(c, *Hh, *P2[0], E.COR, q, 8, dash=[12, 10])
    E.foco(c, t, C["s03.c"] + 0.4, 0.4, lambda a: (agua(c, 1150, 960, esc, 270, a), agua(c, *o2, esc, 270, a)))


# ---------------- gelo (s04–s06) ----------------
def b_gelo(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("água líquida:", "g", 64)] + ps("as ligações se formam e se desfazem", "i", 62), XE, 220, passo=0.08)
        E.frase(c, t, C["s04.b"], ps("as moléculas escorregam e ficam juntinhas", "i", 58, TINTA2), XE, 320, passo=0.08)
        E.foco(c, t, C["s04.a"] + 0.3, 0.4, lambda a: M.rrect(c, 560, 420, 800, 520, 30, Q.AGUA, 0.6 * a))
        liquido(c, t, C["s04.a"] + 0.3, 600, 460, 720, 440, 34, 30)
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("gelo:", "g", 64)] + ps("cada molécula prende quatro vizinhas, fixas", "i", 60), XE, 200, passo=0.08)
        E.foco(c, t, C["s05.a"] + 0.3, 0.4, lambda a: M.rrect(c, 160, 300, 1080, 680, 30, GELO, 0.7 * a))
        rede_gelo(c, t, C["s05.b"] - 0.4, 700, 640, 120, 26, vao=t >= C["s05.c"])
        E.frase(c, t, C["s05.b"], ps("anéis de seis lados", "i", 60), 1320, 450, passo=0.08)
        E.frase(c, t, C["s05.c"], [("espaços", "g", 60, COR), ("vazios", "g", 60, COR)], 1320, 560, passo=0.1)
        E.foco(c, t, C["s05.d"], 0.4, lambda a: E.pilula(c, "mesma massa, mais volume", 700, 1035, 50, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s06"], ps("a conta da densidade", "i", 62, TINTA2), XE, 180, passo=0.1)

    def conta():
        E.foco(c, t, C["s06.a"], 0.4, lambda a: E.escreve(c, "1 L de gelo = 1000 cm³ → cerca de 920 g", XE, 300, 56, "b", TINTA, a))
        E.foco(c, t, C["s06.b"], 0.5, lambda a: E.formula(c, "d = f{920}{1000} =", XE, 470, 90, "g", TINTA, a))
        E.foco(c, t, C["s06.b"] + 1.2, 0.5, lambda a: (E.bola(c, XE + 760, 440, 90, CERTO, a), centro(c, "0,92", XE + 760, 466, 70, "g", BR, a)))
        E.foco(c, t, C["s06.b"] + 1.5, 0.4, lambda a: E.escreve(c, "g/cm³", XE + 870, 470, 56, "b", TINTA, a))
        E.frase(c, t, C["s06.c"], [("menor que 1:", "i", 62), ("o gelo boia", "g", 60, COR)], XE, 640, passo=0.1)
    conta()
    E.foco(c, t, C["s06.d"], 0.5, lambda a: (M.rrect(c, 1100, 650, 700, 380, 20, M.mix(Q.AGUA, "#5AA9D6", 0.3), a),
                                            M.rrect(c, 1100, 650, 700, 70, 10, GELO, a),
                                            M.line(c, 1100, 720, 1800, 720, "#7FB8D6", a, 4)))
    E.foco(c, t, C["s06.e"], 0.4, lambda a: E.escreve(c, "gelo: uma tampa", 1140, 700, 44, "b", TINTA, a))
    for k in range(3):
        E.foco(c, t, C["s06.f"] + 0.2 * k, 0.4, lambda a, k=k: peixe(c, 1250 + k * 200 + 20 * math.sin(t + k), 850 + 50 * (k % 2), a))
    E.foco(c, t, C["s06.f"] + 0.6, 0.4, lambda a: E.escreve(c, "água líquida embaixo", 1140, 1000, 44, "b", TINTA, a))


def peixe(c, x, y, a=1.0):
    if a <= 0:
        return
    c.drawOval(skia.Rect.MakeXYWH(x - 50, y - 20, 100, 40), M.paint("#F28C28", a))
    pth = skia.Path(); pth.moveTo(x - 45, y); pth.lineTo(x - 80, y - 22); pth.lineTo(x - 80, y + 22); pth.close()
    c.drawPath(pth, M.paint("#F28C28", a))
    c.drawCircle(x + 28, y - 6, 5, M.paint(TINTA, a))


# ---------------- tensão superficial (s07–s08) ----------------
def b_tensao(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("dentro, cada molécula é puxada por todos os lados", "i", 54), XE, 200, passo=0.07)
        E.foco(c, t, C["s07"], 0.4, lambda a: (M.rrect(c, 400, 480, 1120, 520, 20, Q.AGUA, 0.7 * a), M.line(c, 400, 480, 1520, 480, "#3C8DBF", a, 5)))
        for i in range(3):
            for j in range(7):
                E.foco(c, t, C["s07"] + 0.02 * (i + j), 0.4, lambda a, i=i, j=j: E.bola(c, 480 + j * 160, 520 + i * 160, 30, "#3C8DBF", a))
        # dentro: 4 setas equilibradas
        if t >= C["s07.a"]:
            q = ep(t, C["s07.a"], 0.4)
            cx, cy = 480 + 3 * 160, 520 + 2 * 160
            for ux, uy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                M.arrow(c, cx + ux * 40, cy + uy * 40, cx + ux * 120, cy + uy * 120, E.COR, q, 6, 18)
        E.frase(c, t, C["s07.b"], ps("na superfície, não há vizinhas em cima", "i", 54), XE, 300, passo=0.07)
        if t >= C["s07.c"]:
            q = ep(t, C["s07.c"], 0.4)
            for j in (1, 3, 5):
                cx, cy = 480 + j * 160, 520
                for ux, uy in ((1, 0), (-1, 0), (0, 1)):
                    M.arrow(c, cx + ux * 40, cy + uy * 40, cx + ux * 110, cy + uy * 110, ERRADO if uy else E.COR, q, 6, 18)
        E.frase(c, t, C["s07.d"], [("a superfície fica esticada:", "i", 54), ("película", "g", 52, COR)], XE, 390, passo=0.08)
        E.foco(c, t, C["s07.e"], 0.4, lambda a: E.pilula(c, "tensão superficial: alta na água", 1500, 1040, 46, "g", fundo=E.COR, a=a))
        return
    E.foco(c, t, C["s08"], 0.4, lambda a: M.rrect(c, 160, 640, 1600, 400, 20, Q.AGUA, 0.7 * a))
    cov = [(700 + dx, 10) for dx in (-210, -150, -120, 120, 150, 210)]
    E.foco(c, t, C["s08"], 0.4, lambda a: superficie(c, 160, 1760, 640, a, cov if t >= C["s08.a"] else None))
    E.foco(c, t, C["s08.a"], 0.5, lambda a: inseto(c, 700, 640, a))
    E.frase(c, t, C["s08.a"], ps("um inseto leve não fura a película", "i", 56), XE, 220, passo=0.08)
    afunda = ease_io(prog(t, C["s08.c"] + 0.6, 1.2)) if t >= C["s08.c"] else 0

    def clipe(a):
        y = lerp(640, 960, afunda)
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1240, y - 24, 240, 40), 20, 20)
        c.drawRRect(rr, M.paint("#8A9099", a, stroke=7))
        rr2 = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1270, y - 14, 170, 22), 11, 11)
        c.drawRRect(rr2, M.paint("#8A9099", a, stroke=6))
    E.foco(c, t, C["s08.b"], 0.5, clipe)
    E.frase(c, t, C["s08.b"], [("até um clipe de aço,", "i", 54)] + ps("quase 8 vezes mais denso", "i", 54, TINTA2), XE, 320, passo=0.08)
    if t >= C["s08.c"]:
        Q.gotas(c, t, C["s08.c"], 1360, 420, 620, n=1, cor="#F2C14E")
        Q.conta_gotas(c, 1360, 420, ep(t, C["s08.c"], 0.4), cor="#F2C14E")
    E.frase(c, t, C["s08.d"], ps("o detergente enfraquece a película", "i", 54, TINTA2), XE, 420, passo=0.08)


# ---------------- tubo (s09) ----------------
def b_tubo(c, t, C, b):
    E.frase(c, t, C["s09.a"], ps("e o tubo fino?", "i", 66), XE, 200, passo=0.1)
    sobe = ease_io(prog(t, C["s09.c"], 1.6))
    tubos(c, t, C["s09.a"] + 0.3, 1060, 1000, 840, sobe=sobe)
    E.frase(c, t, C["s09.b"], ps("o vidro tem oxigênios na superfície", "i", 52), XE, 320, passo=0.07)
    E.frase(c, t, C["s09.b"] + 1.6, ps("a água faz ligações de hidrogênio com eles", "i", 52, TINTA2), XE, 400, passo=0.07)
    E.frase(c, t, C["s09.d"], ps("e puxa junto a água do meio", "i", 52), XE, 500, passo=0.07)
    E.frase(c, t, C["s09.e"], [("mais fino,", "i", 56), ("sobe mais", "g", 54, COR)], XE, 620, passo=0.1)
    E.foco(c, t, C["s09.f"], 0.4, lambda a: E.pilula(c, "capilaridade", XE + 230, 760, 60, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s09.f"] + 0.6, ps("como o papel-toalha puxando a água", "i", 50, TINTA2), XE, 880, passo=0.07)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s10.a"], ps("o gelo boia porque tem ar dentro?", "i", 62), XE + 460, 190, passo=0.1)
    if t >= C["s10.a"] + 1.6:
        E.risco(c, XE + 450, 205, XE + 1380, 160, t, C["s10.a"] + 1.6, largura=10)
    E.foco(c, t, C["s10.b"], 0.5, lambda a: copo_gelo(c, 560, 900, 360, 440, 0.7, a, boia=True))
    E.foco(c, t, C["s10.b"] + 0.3, 0.4, lambda a: centro(c, "gelo sem bolha: boia igual", 560, 990, 46, "b", TINTA, a))
    rede_gelo(c, t, C["s10.c"], 1400, 600, 95, 20, cols=2, rows=2)
    E.foco(c, t, C["s10.c"] + 0.6, 0.4, lambda a: centro(c, "os vãos são da rede de moléculas", 1400, 900, 46, "b", COR, a))
    E.foco(c, t, C["s10.d"], 0.4, lambda a: centro(c, "muito menores que qualquer bolha", 1400, 970, 44, "i", TINTA2, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s11.a"], ps("comportamento estranho da água?", "i", 66, BR), W / 2, 200, "center", 0.1)
    for k, s_ in enumerate(("gelo que boia", "película na superfície", "água subindo no tubo")):
        pilula_em(c, t, C["s11.b"] + 0.6 * k, s_, (420, 960, 1500)[k], 360, 46, "#2A2C36")
    E.frase(c, t, C["s11.c"], [("→", "g", 76, CLARO), ("ligações de hidrogênio", "g", 76, E.CLARO)], W / 2, 560, "center", 0.12)
    E.frase(c, t, C["s11.d"], ps("é a força que a água tem de sobra", "i", 58, CLARO), W / 2, 700, "center", 0.08)
    E.frase(c, t, C["s11.e"], ps("com números: mesma explicação, e mais a conta da densidade", "i", 52, BR), W / 2, 900, "center", 0.06)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s12"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s12.a"], ps("forminha com", "i", 62) + [("460 g", "g", 60, COR)] + ps("de água", "i", 62), XE, 300, passo=0.1)
    E.frase(c, t, C["s12.b"], [("1", "g", 56, COR)] + ps("que volume ocupa, líquida?", "i", 60), XE, 460, passo=0.08)
    E.frase(c, t, C["s12.c"], [("2", "g", 56, COR)] + ps("e congelada, com", "i", 60), XE, 570, passo=0.08)
    E.foco(c, t, C["s12.c"] + 1.4, 0.4, lambda a: E.escreve(c, "d = 0,92 g/cm³", XE + 620, 570, 60, "g", TINTA, a))
    E.frase(c, t, C["s12.d"], [("3", "g", 56, COR)] + ps("por que o volume mudou?", "i", 60), XE, 680, passo=0.08)
    if t >= C["s13"]:
        E.relogio(c, t, C["s13.a"], cx=1600, cy=470, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("vamos lá", "i", 66, TINTA2), XE, 170)
        E.foco(c, t, C["s14.a"], 0.4, lambda a: E.escreve(c, "água líquida: 1 g/cm³", XE, 290, 56, "b", TINTA, a))
        E.foco(c, t, C["s14.b"], 0.4, lambda a: E.escreve(c, "460 g ocupam 460 cm³", XE, 390, 64, "g", TINTA, a))
        E.frase(c, t, C["s14.c"], ps("no gelo: volume = massa dividida pela densidade", "i", 54, TINTA2), XE, 520, passo=0.07)
        E.foco(c, t, C["s14.d"], 0.5, lambda a: E.formula(c, "V = f{460}{0,92} =", XE, 690, 90, "g", TINTA, a))
        E.foco(c, t, C["s14.d"] + 1.6, 0.5, lambda a: (E.bola(c, XE + 820, 660, 90, CERTO, a), centro(c, "500", XE + 820, 686, 70, "g", BR, a)))
        E.foco(c, t, C["s14.d"] + 1.9, 0.4, lambda a: E.escreve(c, "cm³", XE + 930, 690, 60, "b", TINTA, a))
        E.foco(c, t, C["s14.e"], 0.4, lambda a: E.pilula(c, "40 cm³ a mais", XE + 300, 860, 56, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s15.a"], ps("por quê?", "i", 66, TINTA2), XE, 180)
    rede_gelo(c, t, C["s15.b"], 1250, 560, 110, 24)
    E.frase(c, t, C["s15.b"], ps("cada molécula prende quatro vizinhas", "i", 54), XE, 300, passo=0.07)
    E.frase(c, t, C["s15.c"], [("anéis com", "i", 56), ("espaços vazios", "g", 54, COR)], XE, 400, passo=0.08)
    E.frase(c, t, C["s15.d"], [("mesma massa,", "i", 58), ("mais volume", "g", 56, COR)], XE, 520, passo=0.08)
    E.foco(c, t, C["s15.e"], 0.4, lambda a: E.pilula(c, "a garrafa cheia no congelador estoura", W / 2, 1000, 50, "g", fundo=TINTA, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s16.a", [("gelo:", "g", 62)] + ps("rede com espaços, menos denso, boia", "i", 64)),
                 ("s16.b", [("superfície:", "g", 62)] + ps("uma película", "i", 64)),
                 ("s16.c", [("tubo fino:", "g", 62)] + ps("a água sobe", "i", 64)))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 50, a=a), centro(c, str(i + 1), 260, y - 2, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 350, y, passo=0.12)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 240)
    E.frase(c, t, C["s17"] + 0.8, [("praticando", "g", 110, COR)], XE, 390)
    E.frase(c, t, C["s17.a"], ps("quem se dissolve e quem ferve mais alto", "i", 58), XE, 520, passo=0.08)
    E.frase(c, t, C["s17.b"], ps("a partir da estrutura da molécula", "i", 58, TINTA2), XE, 610, passo=0.08)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s17.c"] + 0.2, 0.4))
    E.frase(c, t, C["s17.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, gelo=b_gelo, tensao=b_tensao, tubo=b_tubo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
