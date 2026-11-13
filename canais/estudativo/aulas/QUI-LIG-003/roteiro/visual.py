"""Visual — Estudativo · QUI-LIG-003: ligação metálica e ligas.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001) e a da trilha (QUI-LIG-001). Nesta aula, a peça própria é o METAL
(metal()): íons positivos na cor do elemento, em fileiras, com "+" dentro, e o mar de elétrons = bolinhas azuis
(Q.ELETRON) passeando entre eles; com a pilha ligada, os elétrons derivam todos para o mesmo lado; ao bater, as fileiras de
cima escorregam e os elétrons vão junto; na liga, átomos de outro tamanho e outra cor tomam lugares ou ficam nos vãos.
Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ligações Químicas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-LIG-003_ligacao_metalica_ligas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("mar", "conduz", "ligas", "atalho", "questao", "fim"))
BR = "#FFFFFF"
COBRE, ESTANHO, FERRO, OURO = Q.cor_el("Cu"), Q.cor_el("Sn"), Q.cor_el("Fe"), Q.cor_el("Au")


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def _h(k, s=1.0):
    """número pseudoaleatório fixo em 0..1"""
    v = math.sin(k * 12.9898 + s * 78.233) * 43758.5453
    return v - math.floor(v)


def metal(c, t, t0, x, y, cols, rows, p=96, r=34, el="Cu", desliza=0.0, fluxo=None, eletrons=True, intrusos=None,
          vaos=(), a=1.0, onda=0.04, mais=True, escuro=False):
    """pedaço de metal: íons positivos em fileiras (x, y = centro do primeiro) e o mar de elétrons.
    desliza = px que as fileiras de cima andam; fluxo = instante em que os elétrons passam a andar para a direita;
    intrusos = {(i, j): (el, r)} troca um íon por outro átomo (liga por troca); vaos = [(i, j, el, r)] átomo pequeno no vão
    entre (i, j) e (i + 1, j + 1) (liga por vão, como o carbono no aço)"""
    if t < t0 or a <= 0:
        return
    intrusos = intrusos or {}
    meio = rows // 2
    for i in range(rows):
        for j in range(cols):
            q = ease_back(prog(t, t0 + (i + j) * onda, 0.4))
            if q <= 0:
                continue
            cx = x + j * p + (desliza if i < meio else 0)
            cy = y + i * p
            e2, r2 = intrusos.get((i, j), (el, r))
            Q.atomo(c, cx, cy, r2 * q, e2, a, rotulo=False, escuro=escuro)
            if mais:
                centro(c, "+", cx, cy + r2 * 0.36 * q, r2 * 1.0 * q, "g", BR, a)
    for (i, j, e2, r2) in vaos:
        q = ease_back(prog(t, t0 + 0.6 + (i + j) * onda, 0.4))
        if q > 0:
            cx = x + (j + 0.5) * p + (desliza if i < meio else 0)
            Q.atomo(c, cx, y + (i + 0.5) * p, r2 * q, e2, a, rotulo=True, escuro=escuro)
    if not eletrons:
        return
    w, h = cols * p, rows * p
    n = int(cols * rows * 0.9)
    qe = ep(t, t0 + 0.8, 0.6)
    if qe <= 0:
        return
    for k in range(n):
        bx = x - p / 2 + _h(k, 1) * w
        by = y - p / 2 + _h(k, 2) * h
        jx = 26 * math.sin(t * (1.1 + _h(k, 3)) + 6 * _h(k, 4))
        jy = 22 * math.sin(t * (1.3 + _h(k, 5)) + 6 * _h(k, 6))
        drift = 0.0
        if fluxo is not None and t > fluxo:
            drift = (t - fluxo) * 150 * min(1, (t - fluxo) / 0.8)
        ex = x - p / 2 + ((bx - (x - p / 2) + drift) % w)
        ey = by + jy * (0.4 if fluxo is not None and t > fluxo else 1)
        if not (fluxo is not None and t > fluxo):
            ex = bx + jx
        if desliza and ey < y + (meio - 0.5) * p:
            ex += desliza
        E.bola(c, ex, ey, 9, Q.ELETRON, a * qe)


def pilha(c, x, y, a=1.0):
    """pilha deitada com o polo + à direita"""
    if a <= 0:
        return
    M.rrect(c, x - 110, y - 50, 220, 100, 18, "#2A2B31", a)
    M.rrect(c, x + 60, y - 50, 50, 100, 12, "#C9A227", a)
    M.rrect(c, x + 110, y - 18, 16, 36, 5, "#9AA0A8", a)
    centro(c, "−", x - 60, y + 18, 56, "g", BR, a)
    centro(c, "+", x + 86, y + 18, 50, "g", TINTA, a)


def anel_joia(c, cx, cy, r, a=1.0):
    """aliança de ouro vista de frente"""
    if a <= 0:
        return
    pnt = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=r * 0.32)
    pnt.setShader(skia.GradientShader.MakeLinear([skia.Point(cx - r, cy - r), skia.Point(cx + r, cy + r)],
                                                 [M.hexc("#FFF1A8", a), M.hexc(OURO, a), M.hexc("#8A6410", a)], [0, 0.5, 1]))
    c.drawCircle(cx, cy, r, pnt)
    c.drawCircle(cx - r * 0.3, cy - r * 0.55, r * 0.08, M.paint(BR, 0.7 * a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        # fio de cobre que dobra
        p = ease_io(prog(t, C["s01.a"] + 0.4, 1.0))
        pth = skia.Path()
        pth.moveTo(200, 700)
        pth.quadTo(520, 700, 700, lerp(700, 470, p))
        E.foco(c, t, C["s01.a"], 0.5, lambda a: c.drawPath(pth, M.paint(COBRE, a, stroke=30, cap_round=True)))
        E.frase(c, t, C["s01.a"], ps("dobre um fio de cobre:", "i", 62), XE, 200, passo=0.1)
        E.frase(c, t, C["s01.b"], [("entorta,", "g", 66), ("não", "i", 70), ("quebra", "g", 66, COR)], XE, 300, passo=0.12)
        # pilha + lâmpada
        E.foco(c, t, C["s01.c"], 0.5, lambda a: pilha(c, 1400, 660, a))
        if t >= C["s01.c"] + 0.4:
            q = ep(t, C["s01.c"] + 0.4, 0.5)
            M.line(c, 1290, 660, 1150, 660, COBRE, q, 10)
            M.line(c, 1150, 660, 1150, 420, COBRE, q, 10)
            M.line(c, 1150, 420, 1650, 420, COBRE, q, 10)
            M.line(c, 1650, 420, 1650, 660, COBRE, q, 10)
            M.line(c, 1650, 660, 1526, 660, COBRE, q, 10)
            if t >= C["s01.c"] + 1.0:
                Q.eletrons(c, t, C["s01.c"] + 1.0, [(1290, 660), (1150, 660), (1150, 420), (1650, 420), (1650, 660), (1526, 660)], vel=220, espaco=110, r=12)
        E.frase(c, t, C["s01.c"], ps("ligue numa pilha:", "i", 62), 1150, 300, passo=0.1)
        E.frase(c, t, C["s01.c"] + 0.8, [("a", "i", 66), ("corrente", "g", 64, COR), ("passa", "i", 66)], 1150, 860, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("a mesma explicação: os", "i", 62) + [("elétrons", "g", 60, COR)], W / 2, 1010, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1660, 560, 220 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("o", "i", 70), ("mar", "g", 66, COR), ("de", "i", 70), ("elétrons", "g", 66, COR)]),
                 (C["s02.c"], [("bronze", "g", 66), ("e", "i", 70), ("aço:", "g", 66), ("do", "i", 70), ("que", "i", 70), ("são", "i", 70), ("feitos", "i", 70)]),
                 (C["s02.d"], [("atalho", "g", 66, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula de famílias, uma ideia só", "i", 66, TINTA2), XE, 190, passo=0.1)
    E.frase(c, t, C["s03.a"], [("metais:", "g", 70)] + ps("de 1 a 3 elétrons na última camada", "i", 70), XE, 340, passo=0.1)
    E.frase(c, t, C["s03.b"], ps("e perdem esses elétrons", "i", 70) + [("fácil", "g", 66, COR)], XE, 460, passo=0.1)
    E.frase(c, t, C["s03.c"], ps("quem perde elétrons vira", "i", 66) + [("íon positivo", "g", 64, COR)], XE, 600, passo=0.1)
    def at(a):
        Q.atomo(c, 760, 850, 80, "Cu", a)
    E.foco(c, t, C["s03.c"] + 0.3, 0.5, at)
    p = ease_io(prog(t, C["s03.c"] + 1.0, 1.0))
    if p > 0:
        E.bola(c, lerp(850, 1100, p), 850 - 40 * math.sin(math.pi * p), 14, Q.ELETRON)
        E.foco(c, t, C["s03.c"] + 1.6, 0.4, lambda a: (Q.atomo(c, 1300, 850, 70, "Cu", a, rotulo=False), Q.formula(c, "Cu^{2+}", 1300, 875, 60, BR, a, "center")))


# ---------------- mar de elétrons (s04–s05) ----------------
GX, GY, GC, GR, GP = 1040, 300, 7, 6, 112


def b_mar(c, t, C, b):
    E.frase(c, t, C["s04"], ps("um pedaço de cobre", "i", 66, TINTA2), XE, 180, passo=0.1)
    solta = t >= C["s04.c"]
    metal(c, t, C["s04"] + 0.2, GX, GY, GC, GR, GP, 36, "Cu", eletrons=solta, mais=t >= C["s04.b"])
    if not solta:
        # antes: cada átomo ainda com o elétron perto
        for i in range(GR):
            for j in range(GC):
                q = ep(t, C["s04.a"], 0.4)
                ang = t * 2 + i + j
                E.bola(c, GX + j * GP + 50 * math.cos(ang), GY + i * GP + 50 * math.sin(ang), 9, Q.ELETRON, q)
    def s04():
        E.frase(c, t, C["s04.a"], ps("cada átomo solta os elétrons", "i", 46, TINTA2), XE, 270, passo=0.06)
        E.frase(c, t, C["s04.b"], [("íons", "g", 70), ("positivos", "g", 70, COR)], XE, 420, passo=0.12)
        E.frase(c, t, C["s04.b"] + 0.6, ps("em fileiras", "i", 66), XE, 500, passo=0.1)
        E.frase(c, t, C["s04.c"], [("elétrons", "g", 66, Q.ELETRON), ("soltos,", "i", 66)], XE, 630, passo=0.1)
        E.frase(c, t, C["s04.c"] + 0.6, ps("sem dono", "i", 66), XE, 710, passo=0.1)
        E.frase(c, t, C["s04.d"], [("mar", "g", 80, COR), ("de", "i", 80), ("elétrons", "g", 80, COR)], XE, 880, passo=0.15)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t >= C["s05"]:
        E.frase(c, t, C["s05.a"], ps("íons + e mar −", "i", 70) + [("se atraem", "g", 64, COR)], XE, 380, passo=0.12)
        E.frase(c, t, C["s05.b"], [("ligação", "g", 100)], XE, 540)
        E.frase(c, t, C["s05.b"] + 0.4, [("metálica", "g", 100, COR)], XE, 660)
        pilula_em(c, t, C["s05.c"], "o mar funciona como cola", XE + 300, 820, 50, E.COR)


# ---------------- conduz (s06) ----------------
def b_conduz(c, t, C, b):
    E.frase(c, t, C["s06"], ps("por que conduz eletricidade?", "i", 70), XE, 180, passo=0.1)
    E.frase(c, t, C["s06.a"], [("corrente", "g", 60, COR), ("=", "g", 60, TINTA2)] + ps("carga andando num sentido só", "i", 62), XE, 290, passo=0.1)
    x0, y0, cols, rows, p = 520, 470, 9, 4, 104
    fl = C["s06.c"] + 0.4
    metal(c, t, C["s06"] + 0.3, x0, y0, cols, rows, p, 32, "Cu", fluxo=fl)
    E.foco(c, t, C["s06.b"], 0.4, lambda a: E.escreve(c, "os elétrons já estão soltos", x0 - 50, 900, 50, "i", TINTA2, a))
    if t >= C["s06.c"]:
        q = ep(t, C["s06.c"], 0.4)
        M.rrect(c, x0 - 120, y0 - 70, 40, 4 * p, 10, "#2A2B31", q)
        M.rrect(c, x0 + cols * p - 40, y0 - 70, 40, 4 * p, 10, "#C9A227", q)
        centro(c, "−", x0 - 100, y0 - 100, 70, "g", TINTA, q)
        centro(c, "+", x0 + cols * p - 20, y0 - 100, 70, "g", TINTA, q)
        p2 = ease_io(prog(t, fl, 0.8))
        M.arrow(c, x0 + 100, 940, x0 + 100 + 460 * p2, 940, Q.ELETRON, q, 7, 24)
        E.foco(c, t, fl + 0.4, 0.4, lambda a: E.escreve(c, "todos para o mesmo lado", x0 + 620, 955, 50, "b", Q.ELETRON, a))
    pilula_em(c, t, C["s06.d"], "e conduz calor, pelo mesmo motivo", 1440, 1030, 44, TINTA2, "b")


# ---------------- dobra (s07) ----------------
def b_dobra(c, t, C, b):
    E.frase(c, t, C["s07"], ps("por que dobra sem quebrar?", "i", 70), XE, 180, passo=0.1)
    x0, y0, p = 300, 380, 100
    d = 0.0
    if t >= C["s07.a"]:
        d = p * ease_io(prog(t, C["s07.a"] + 0.4, 1.2))
    def peca():
        metal(c, t, C["s07"] + 0.2, x0, y0, 7, 4, p, 32, "Cu", desliza=d)
        if t >= C["s07.a"]:
            q = ep(t, C["s07.a"], 0.4)
            M.arrow(c, x0 - 150, y0 + 0.5 * p, x0 - 40, y0 + 0.5 * p, TINTA, q, 9, 28)
            M.line(c, x0 - 60, y0 + 1.5 * p + 4, x0 + 7 * p + 100, y0 + 1.5 * p + 4, TINTA2, q * 0.6, 3, dash=[14, 10])
        E.frase(c, t, C["s07.a"] + 0.5, ps("as fileiras escorregam", "i", 56, TINTA2), x0 - 60, y0 + 4 * p + 30, passo=0.08)
        E.frase(c, t, C["s07.b"], ps("e o mar vai junto:", "i", 56, TINTA2) + [("continua colando", "g", 52, COR)], x0 - 60, y0 + 4 * p + 110, passo=0.08)
    E.saida(c, t, C["s07.c"] - 0.2, peca)
    if t < C["s07.c"] - 0.2:
        return
    # lâmina e fio
    def lamina(a):
        pth = skia.Path()
        pth.moveTo(260, 520)
        for k in range(9):
            pth.quadTo(300 + k * 70, 480 + (40 if k % 2 else -40), 330 + k * 70, 520)
        pth.lineTo(330 + 8 * 70, 640)
        for k in range(9):
            pth.quadTo(300 + (8 - k) * 70, 600 + (40 if k % 2 else -40), 260 + (8 - k) * 70, 640)
        pth.close()
        pp = skia.Paint(AntiAlias=True)
        pp.setShader(skia.GradientShader.MakeLinear([skia.Point(260, 480), skia.Point(900, 640)], [M.hexc("#E9ECEF", a), M.hexc("#AEB4BC", a), M.hexc("#F4F6F8", a)], [0, 0.5, 1]))
        c.drawPath(pth, pp)
        c.drawPath(pth, M.paint("#8A9099", a, stroke=3))
    E.foco(c, t, C["s07.c"], 0.5, lamina)
    E.frase(c, t, C["s07.c"] + 0.3, [("lâmina", "g", 70)], 260, 780, passo=0.1)
    E.frase(c, t, C["s07.c"] + 0.6, ps("papel-alumínio", "i", 54, TINTA2), 260, 850, passo=0.1)

    def fio(a):
        pth = skia.Path()
        for k in range(60):
            g = k / 59 * math.tau * 4
            xx, yy = 1150 + k * 9, 560 + 70 * math.sin(g)
            pth.moveTo(xx, yy) if k == 0 else pth.lineTo(xx, yy)
        c.drawPath(pth, M.paint(COBRE, a, stroke=16, cap_round=True))
    E.foco(c, t, C["s07.d"], 0.5, fio)
    E.frase(c, t, C["s07.d"] + 0.3, [("fio", "g", 70)], 1150, 780, passo=0.1)
    E.frase(c, t, C["s07.d"] + 0.6, ps("de cobre", "i", 54, TINTA2), 1150, 850, passo=0.1)
    E.frase(c, t, C["s07.e"], [("maleável", "g", 56, COR), ("=", "g", 56, TINTA2)] + ps("vira lâmina ·", "i", 58) + [("dúctil", "g", 56, COR), ("=", "g", 56, TINTA2)] + ps("vira fio", "i", 58),
            W / 2, 1000, "center", 0.1)


# ---------------- ligas (s08–s10) ----------------
BRONZE = {(0, 2): ("Sn", 44), (1, 5): ("Sn", 44), (2, 1): ("Sn", 44), (3, 4): ("Sn", 44)}


def b_ligas(c, t, C, b):
    if t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08"], ps("metal puro nem sempre é o melhor", "i", 62, TINTA2), XE, 180, passo=0.1)
            E.frase(c, t, C["s08.a"], [("liga", "g", 80, COR), ("=", "g", 80, TINTA2)] + ps("metal + outro elemento", "i", 76), XE, 310, passo=0.12)
            E.frase(c, t, C["s08.a"] + 1.4, ps("derretidos juntos, depois resfriados", "i", 54, TINTA2), XE, 390, passo=0.08)
            metal(c, t, C["s08.b"], 1050, 520, 7, 4, 100, 34, "Cu", intrusos=BRONZE)
            E.frase(c, t, C["s08.b"], [("bronze", "g", 90)], XE, 560)
            E.foco(c, t, C["s08.b"] + 0.4, 0.4, lambda a: (Q.atomo(c, XE + 30, 660, 30, "Cu", a), E.escreve(c, "cobre", XE + 80, 680, 54, "i", TINTA, a),
                                                           Q.atomo(c, XE + 300, 660, 38, "Sn", a), E.escreve(c, "estanho", XE + 360, 680, 54, "i", TINTA, a)))
            E.frase(c, t, C["s08.c"], ps("mais duro que o cobre puro", "i", 58), XE, 800, passo=0.1)
            for k, s_ in enumerate(("sinos", "estátuas", "medalhas")):
                pilula_em(c, t, C["s08.c"] + 1.2 + 0.3 * k, s_, XE + (90, 330, 600)[k], 900, 46, TINTA)
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    if t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09.a"], [("aço", "g", 110, COR)], XE, 300)
            E.frase(c, t, C["s09.a"] + 0.5, ps("ferro + uma pitada de carbono", "i", 62), XE, 400, passo=0.1)
            metal(c, t, C["s09.a"] + 0.2, 1050, 420, 7, 4, 100, 36, "Fe", vaos=[(0, 1, "C", 20), (1, 4, "C", 20), (2, 2, "C", 20)])
            E.frase(c, t, C["s09.b"], ps("bem mais resistente que o ferro puro", "i", 54, TINTA2), XE, 520, passo=0.08)
            for k, s_ in enumerate(("vigas", "pregos", "ferramentas")):
                pilula_em(c, t, C["s09.b"] + 1.0 + 0.3 * k, s_, XE + (80, 290, 560)[k], 620, 44, TINTA)
            E.frase(c, t, C["s09.c"], [("o", "i", 60), ("carbono", "g", 58), ("nem", "i", 60), ("é", "i", 60), ("metal", "g", 58, COR)], XE, 800, passo=0.1)
            E.frase(c, t, C["s09.c"] + 1.0, ps("e a liga existe do mesmo jeito", "i", 56, TINTA2), XE, 880, passo=0.08)
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    # s10: por que é mais dura
    E.frase(c, t, C["s10"], ps("por que a liga é mais dura?", "i", 66), XE, 180, passo=0.1)
    tenta = t >= C["s10.c"]
    dd = 0.0
    if tenta:
        u = prog(t, C["s10.c"], 2.0)
        dd = 22 * math.sin(u * math.pi * 3) * (1 - u)
    metal(c, t, C["s10"] + 0.2, 380, 400, 7, 4, 104, 34, "Cu", intrusos=BRONZE, desliza=dd)
    E.frase(c, t, C["s10.a"], ps("átomos de", "i", 60) + [("outro tamanho", "g", 58, COR)], 1180, 400, passo=0.1)
    E.frase(c, t, C["s10.b"], ps("como pedras num trilho", "i", 58, TINTA2), 1180, 500, passo=0.1)
    if tenta:
        q = ep(t, C["s10.c"], 0.4)
        M.arrow(c, 180, 452, 290, 452, TINTA, q, 9, 28)
        E.foco(c, t, C["s10.c"] + 0.6, 0.4, lambda a: E.selo(c, 1240, 640, 50, False, a))
        E.foco(c, t, C["s10.c"] + 0.6, 0.4, lambda a: E.escreve(c, "não escorrega", 1310, 660, 54, "b", ERRADO, a))
    E.frase(c, t, C["s10.d"], ps("escorrega menos = entorta menos", "i", 66), W / 2, 960, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("bronze é um elemento novo?", "i", 66), XE + 460, 190, passo=0.1)
    Q.tabela(c, t, C["s11.b"], 180, 300, 44, numeros=False, d=1.0)
    E.foco(c, t, C["s11.b"] + 0.8, 0.4, lambda a: E.pilula(c, "bronze?", 1500, 380, 60, "g", fundo=ERRADO, a=a))
    if t >= C["s11.b"] + 1.4:
        E.risco(c, 1380, 410, 1620, 350, t, C["s11.b"] + 1.4, largura=10)
    E.frase(c, t, C["s11.c"], [("liga", "g", 70, COR), ("=", "g", 70, TINTA2), ("mistura:", "i", 74)], XE, 760, passo=0.12)
    E.foco(c, t, C["s11.c"] + 0.8, 0.4, lambda a: (Q.atomo(c, XE + 650, 735, 40, "Cu", a), E.escreve(c, "cobre +", XE + 710, 760, 64, "b", TINTA, a),
                                                   Q.atomo(c, XE + 1010, 735, 48, "Sn", a), E.escreve(c, "estanho", XE + 1075, 760, 64, "b", TINTA, a)))
    E.frase(c, t, C["s11.d"], ps("a receita muda: mais ou menos estanho", "i", 60, TINTA2), XE, 900, passo=0.08)
    if t >= C["s11.d"] + 0.8:
        for k in range(3):
            x = XE + 200 + k * 380
            fr = (0.10, 0.15, 0.20)[k]
            q = ep(t, C["s11.d"] + 0.8 + 0.3 * k, 0.4)
            M.rrect(c, x, 960, 300, 50, 25, COBRE, q)
            M.rrect(c, x + 300 * (1 - fr * 2), 960, 300 * fr * 2, 50, 25, ESTANHO, q)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 150, "center", 0.12)
    E.frase(c, t, C["s12.a"], [("conduz", "g", 72, BR), ("ou", "i", 76, CLARO), ("dobra?", "g", 72, BR)], W / 2, 280, "center", 0.12)
    E.frase(c, t, C["s12.b"], [("→", "g", 72, CLARO), ("elétrons livres", "g", 72, E.CLARO)], W / 2, 400, "center", 0.12)
    metal(c, t, C["s12.b"] + 0.3, 760, 520, 5, 2, 100, 30, "Cu", escuro=True)
    E.frase(c, t, C["s12.c"], ps("carga que anda · cola que acompanha", "i", 58, CLARO), W / 2, 790, "center", 0.1)
    E.frase(c, t, C["s12.d"], [("não", "g", 58, ERRADO), ("compensa:", "i", 60, CLARO)] + ps("por que a liga é mais dura?", "i", 60, CLARO), W / 2, 900, "center", 0.1)
    E.frase(c, t, C["s12.e"], [("→", "g", 60, CLARO), ("átomos de outro tamanho", "g", 58, BR)], W / 2, 1000, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s13.a"], ps("ouro puro: mole, entorta e arranha", "i", 60), XE, 300, passo=0.08)
    E.frase(c, t, C["s13.b"], ps("o ouro das joias leva", "i", 60) + [("cobre", "g", 58, COR)], XE, 400, passo=0.08)
    E.frase(c, t, C["s13.c"], [("1", "g", 56, COR)] + ps("por que fica mais dura?", "i", 62), XE, 600, passo=0.08)
    E.frase(c, t, C["s13.d"], [("2", "g", 56, COR)] + ps("ainda conduz eletricidade?", "i", 62), XE, 720, passo=0.08)
    if t < C["s14"]:
        E.foco(c, t, C["s13.a"] + 0.3, 0.6, lambda a: anel_joia(c, 1470, 480, 190, a))
    else:
        E.relogio(c, t, C["s14.a"], cx=1480, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s15"], ps("vamos lá", "i", 66, TINTA2), XE, 170)
    E.frase(c, t, C["s15.a"], [("liga:", "g", 64), ("ouro", "g", 64, COR), ("+", "g", 64, TINTA2), ("cobre", "g", 64, COR)], XE, 290, passo=0.12)
    joia = {(0, 3): ("Cu", 26), (1, 1): ("Cu", 26), (2, 4): ("Cu", 26), (3, 2): ("Cu", 26)}
    u = prog(t, C["s15.c"], 2.0)
    dd = 18 * math.sin(u * math.pi * 3) * (1 - u) if t >= C["s15.c"] else 0
    metal(c, t, C["s15.a"] + 0.3, 1100, 330, 6, 4, 104, 38, "Au", intrusos=joia, desliza=dd)
    E.frase(c, t, C["s15.b"], ps("o cobre é menor", "i", 60), XE, 420, passo=0.1)
    E.frase(c, t, C["s15.c"], ps("e trava as fileiras", "i", 60), XE, 510, passo=0.1)
    E.frase(c, t, C["s15.d"], [("a joia", "i", 62), ("entorta menos", "g", 58, COR)], XE, 620, passo=0.1)
    E.foco(c, t, C["s15.d"] + 0.6, 0.4, lambda a: E.selo(c, XE + 760, 600, 44, True, a))
    E.frase(c, t, C["s15.e"], [("conduz?", "i", 62), ("sim", "g", 62, CERTO)], XE, 800, passo=0.12)
    E.frase(c, t, C["s15.f"], ps("os dois são metais: o mar de elétrons continua", "i", 52, TINTA2), XE, 890, passo=0.06)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s16.a", [("íons +", "g", 62)] + ps("em fileiras, num mar de elétrons", "i", 64)),
                 ("s16.b", [("elétrons", "g", 62)] + ps("que andam: conduz", "i", 64)),
                 ("s16.c", [("fileiras", "g", 62)] + ps("que escorregam: dobra", "i", 64)),
                 ("s16.d", [("liga:", "g", 62)] + ps("átomos de outro tamanho endurecem", "i", 64)))
        for i, (k, partes) in enumerate(itens):
            y = 330 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 50, a=a), centro(c, str(i + 1), 260, y - 2, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 350, y, passo=0.12)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 240)
    E.frase(c, t, C["s17.a"], [("iônica,", "g", 84, COR), ("covalente,", "g", 84, COR)], XE, 390, passo=0.15)
    E.frase(c, t, C["s17.a"] + 0.6, [("metálica", "g", 84, COR)], XE, 500)
    for k, f in enumerate(("NaCl", "H2O", "Fe")):
        Q.formula_em(c, t, C["s17.b"] + 0.4 * k, f, XE + 30 + 300 * k, 680, 110)
    E.frase(c, t, C["s17.c"], ps("quem conduz? quem aguenta calor?", "i", 58, TINTA2), XE, 820, passo=0.1)
    E.foco(c, t, C["s17.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s17.d"] + 0.2, 0.4))
    E.frase(c, t, C["s17.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, mar=b_mar, conduz=b_conduz, dobra=b_dobra, ligas=b_ligas,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
