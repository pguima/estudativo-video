"""Visual — Estudativo · QUI-LIG-005: praticando tipos de ligação (prática, quatro questões inéditas).

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001) e a da trilha (QUI-LIG-001): íon = bolinha do elemento com a fórmula do
íon; cruzar cargas = setas em X da carga ao índice; Lewis com pontos azuis que viram traço; metal = íons + em fileiras com
elétrons azuis; teste de condutividade = lâmpada (QUI-LIG-004). Cada questão: enunciado à esquerda, desenho à direita,
relógio no lugar do desenho na pausa. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ligações Químicas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-LIG-005_praticando_tipos_de_ligacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "atalho", "questao2", "questao3", "questao4", "fim"))
BR = "#FFFFFF"
AMARELO = "#FFD23F"

assert Q.contar("K2S") == {"K": 2, "S": 1} and 2 * 1 + (-2) == 0
assert 2 * 2 + 2 * 2 == 8          # O₂: dupla (4 e) + 2 pares livres (4 e)
assert [18 - f for f in (15, 16, 17)] == [3, 2, 1]
assert Q.contar("MgO") == {"Mg": 1, "O": 1}


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


def ion(c, cx, cy, r, el, s, a=1.0, escuro=False):
    if a <= 0:
        return
    Q.atomo(c, cx, cy, r, el, a, rotulo=False, escuro=escuro)
    Q.formula(c, s, cx, cy + r * 0.3, r * 0.82, TINTA if el in ("S", "H") else BR, a, "center")


def reticulo(c, t, t0, x, y, cols, rows, passo, r1, r2, e1="Mg", s1="Mg^{2+}", e2="O", s2="O^{2-}", onda=0.05, a=1.0):
    for i in range(rows):
        for j in range(cols):
            q = ease_back(prog(t, t0 + (i + j) * onda, 0.35))
            if q > 0:
                um = (i + j) % 2 == 0
                ion(c, x + j * passo, y + i * passo, (r1 if um else r2) * q, e1 if um else e2, s1 if um else s2, a)


def _h(k, s=1.0):
    v = math.sin(k * 12.9898 + s * 78.233) * 43758.5453
    return v - math.floor(v)


def metal(c, t, t0, x, y, cols, rows, p=90, r=30, el="Al", fluxo=None, desliza=0.0, a=1.0):
    if t < t0:
        return
    meio = rows // 2
    for i in range(rows):
        for j in range(cols):
            q = ease_back(prog(t, t0 + (i + j) * 0.04, 0.35))
            if q > 0:
                cx = x + j * p + (desliza if i < meio else 0)
                Q.atomo(c, cx, y + i * p, r * q, el, a, rotulo=False)
                centro(c, "+", cx, y + i * p + r * 0.36 * q, r * q, "g", TINTA, a)
    qe = ep(t, t0 + 0.6, 0.5) * a
    w, h = cols * p, rows * p
    for k in range(int(cols * rows * 0.9)):
        bx, by = x - p / 2 + _h(k, 1) * w, y - p / 2 + _h(k, 2) * h
        if fluxo is not None and t > fluxo:
            ex = x - p / 2 + ((bx - (x - p / 2) + (t - fluxo) * 140) % w)
        else:
            ex = bx + 20 * math.sin(t * (1.1 + _h(k, 3)) + 6 * _h(k, 4))
        if desliza and by < y + (meio - 0.5) * p:
            ex += desliza
        E.bola(c, ex, by + 16 * math.sin(t * 1.3 + 6 * _h(k, 6)), 8, Q.ELETRON, qe)


def lampada(c, cx, cy, luz=0.0, a=1.0):
    if a <= 0:
        return
    if luz > 0:
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), 170, [M.hexc(AMARELO, 0.55 * luz * a), M.hexc(AMARELO, 0)], [0, 1]))
        c.drawCircle(cx, cy, 170, g)
    c.drawCircle(cx, cy, 54, M.paint(M.mix("#E8ECEF", AMARELO, luz), a))
    c.drawCircle(cx, cy, 54, M.paint("#8A9099", a, stroke=4))
    M.rrect(c, cx - 26, cy + 46, 52, 42, 8, "#9AA0A8", a)


def cruz(c, t, t0, sa, sb, xa, xb, ya, yb, fs1, s_final, fs2, xf, cores=None):
    """as cargas de cima viram os índices de baixo, por setas em X"""
    E.foco(c, t, t0, 0.4, lambda a: (Q.formula(c, sa, xa, ya, fs1, None, a, "center", cores={"carga": E.COR}),
                                     Q.formula(c, sb, xb, ya, fs1, None, a, "center", cores={"carga": E.COR})))
    for k, (dt, x0, x1) in enumerate(((0.5, xa + fs1 * 0.6, xb + fs1 * 0.45), (1.2, xb + fs1 * 0.5, xa + fs1 * 0.3))):
        p = ease_io(prog(t, t0 + dt, 0.7))
        if p > 0:
            M.arrow(c, x0, ya - fs1 * 0.75, x1, yb - fs2 * 0.45, E.COR, 1.0, 5, 18, p)


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.foco(c, t, C["s01.a"], 0.6, lambda a: (E.bola(c, 470, 470, 200 * ease_back(prog(t, C["s01.a"], 0.6)), a=a),
                                            centro(c, "4", 470, 560, 260, "g", E.SOBRE, a)))
    E.frase(c, t, C["s01.a"] + 0.4, [("questões", "g", 100)], 760, 430)
    E.frase(c, t, C["s01.a"] + 0.8, ps("criadas para esta aula", "i", 62, TINTA2), 760, 520, passo=0.1)
    for k, s_ in enumerate(("iônica", "covalente", "metálica")):
        pilula_em(c, t, C["s01.b"] + 0.3 * k, s_, 870 + k * 300, 650, 54, E.COR)
    E.frase(c, t, C["s01.c"], ps("pause e resolva antes da resposta", "i", 62), W / 2, 900, "center", 0.1)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 70, TINTA2), XE, 200, passo=0.12)
    itens = ((C["s02.a"], [("a carga", "g", 64), ("pela família", "i", 68)]),
             (C["s02.b"], [("o cruzamento", "g", 64), ("das cargas", "i", 68)]),
             (C["s02.c"], [("ligações", "g", 64), ("que faltam para 8", "i", 68)]),
             (C["s02.d"], [("conduzir", "g", 64), ("e", "i", 68), ("derreter", "g", 64)]))
    for i, (ti, partes) in enumerate(itens):
        y = 360 + i * 160
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, XE + 110, y, passo=0.12)
    E.foco(c, t, C["s02.a"] + 0.6, 0.6, lambda a: E.simbolo(c, 1560, 560, 200, a, giro=8 * math.sin(t * 0.4)), blur=0)


def titulo_q(c, t, t0, n):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 170, 50, a=a), centro(c, str(n), XE + 50, 194, 64, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.2, [("questão", "i", 76, COR)], XE + 130, 196)


# ---------------- questão 1 ----------------
def b_questao1(c, t, C, b):
    titulo_q(c, t, C["s03.a"], 1)
    E.foco(c, t, C["s03.b"], 0.5, lambda a: (Q.atomo(c, XE + 50, 330, 44, "K", a), E.escreve(c, "potássio: família 1", XE + 120, 352, 64, "b", TINTA, a)))
    E.foco(c, t, C["s03.c"], 0.5, lambda a: (Q.atomo(c, XE + 50, 460, 44, "S", a), E.escreve(c, "enxofre: família 16", XE + 120, 482, 64, "b", TINTA, a)))
    E.frase(c, t, C["s03.d"], ps("qual é a fórmula do composto?", "i", 64), XE, 680, passo=0.08)
    if t < C["s04"]:
        Q.tabela(c, t, C["s03.b"] - 0.3, 1060, 300, 40, numeros=False, destaque=("K", "S"), d=1.0)
    else:
        E.relogio(c, t, C["s04.a"], cx=1480, cy=470, r=200)


def b_resposta1(c, t, C, b):
    E.frase(c, t, C["s05"], ps("vamos lá", "i", 66, TINTA2), XE, 170)
    E.foco(c, t, C["s05.a"], 0.4, lambda a: E.formula(c, "família 1: 1 elétron, perde", XE, 300, 56, "b", TINTA, a))
    Q.formula_em(c, t, C["s05.a"] + 1.0, "K^+", XE + 900, 310, 100, cores={"carga": E.COR})
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.formula(c, "família 16: 6 elétrons, ganha 2", XE, 440, 56, "b", TINTA, a))
    Q.formula_em(c, t, C["s05.b"] + 1.4, "S^{2-}", XE + 900, 450, 100, cores={"carga": E.COR})
    cruz(c, t, C["s05.c"], "K^+", "S^{2-}", 620, 1000, 690, 960, 140, "K2S", 170, 800)
    Q.formula_em(c, t, C["s05.d"], "K2S", 800, 1000, 170, align="center", cores={"indice": E.COR})
    E.foco(c, t, C["s05.e"], 0.4, lambda a: E.formula(c, "2 · (+1) − 2 = 0", 1500, 900, 70, "g", TINTA, a, "center"))
    E.foco(c, t, C["s05.e"] + 1.6, 0.4, lambda a: E.selo(c, 1500, 1010, 50, True, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06"], ps("o atalho da carga", "i", 72, CLARO), W / 2, 150, "center", 0.12)
            E.frase(c, t, C["s06.a"], [("metal:", "g", 64, BR)] + ps("o último algarismo da família", "i", 64, CLARO), XE, 290, passo=0.1)
            for k, (fam, s_) in enumerate((("1", "+1"), ("2", "+2"), ("13", "+3"))):
                x = 360 + 300 * k
                E.foco(c, t, C["s06.b"] + 0.5 * k, 0.4, lambda a, x=x, fam=fam, s_=s_: (centro(c, "família " + fam, x, 400, 46, "i", CLARO, a), centro(c, s_, x, 500, 96, "g", BR, a)))
            E.frase(c, t, C["s06.c"], [("ametal:", "g", 64, BR)] + ps("o que falta para 18, negativo", "i", 64, CLARO), XE, 660, passo=0.1)
            for k, (fam, s_) in enumerate((("15", "−3"), ("16", "−2"), ("17", "−1"))):
                x = 360 + 300 * k
                E.foco(c, t, C["s06.d"] + 0.6 * k, 0.4, lambda a, x=x, fam=fam, s_=s_: (centro(c, "família " + fam, x, 770, 46, "i", CLARO, a), centro(c, s_, x, 870, 96, "g", E.CLARO, a)))
            E.foco(c, t, C["s06.d"] + 2.0, 0.4, lambda a: E.formula(c, "18 − 16 = 2", 1500, 860, 70, "g", CLARO, a, "center"))
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    E.frase(c, t, C["s07.a"], ps("a família conta os elétrons de valência", "i", 62, BR), W / 2, 280, "center", 0.1)
    E.frase(c, t, C["s07.b"], ps("e 18 é a família dos gases nobres, com 8", "i", 60, CLARO), W / 2, 380, "center", 0.1)
    E.frase(c, t, C["s07.c"], [("não", "g", 60, ERRADO), ("compensa:", "i", 62, CLARO)] + ps("metais do meio da tabela", "i", 62, CLARO), W / 2, 600, "center", 0.1)
    for k, f in enumerate(("Fe^{2+}", "Fe^{3+}")):
        Q.formula_em(c, t, C["s07.d"] + 0.4 * k, f, 760 + 400 * k, 800, 130, align="center", escuro=True, cores={"carga": E.CLARO})
    E.frase(c, t, C["s07.d"] + 1.2, ps("a questão precisa dizer qual", "i", 56, CLARO), W / 2, 950, "center", 0.1)


# ---------------- questão 2 ----------------
def b_questao2(c, t, C, b):
    titulo_q(c, t, C["s08.a"], 2)
    E.frase(c, t, C["s08.b"], ps("o gás oxigênio que você respira", "i", 62), XE, 320, passo=0.08)
    Q.formula_em(c, t, C["s08.b"] + 0.8, "O2", XE, 480, 150)
    E.frase(c, t, C["s08.c"], [("1", "g", 56, COR)] + ps("simples, dupla ou tripla?", "i", 62), XE, 660, passo=0.08)
    E.frase(c, t, C["s08.d"], [("2", "g", 56, COR)] + ps("quantos pares livres em cada O?", "i", 62), XE, 770, passo=0.08)
    if t < C["s09"]:
        for k in range(2):
            E.foco(c, t, C["s08.b"] + 0.6 + 0.3 * k, 0.5, lambda a, k=k: Q.simbolo_lewis(c, "O", 1330 + 300 * k, 480, 130, 6, a))
    else:
        E.relogio(c, t, C["s09.a"], cx=1480, cy=470, r=200)


def b_resposta2(c, t, C, b):
    E.frase(c, t, C["s10"], ps("vamos lá", "i", 66, TINTA2), XE, 170)
    E.frase(c, t, C["s10.a"], [("O:", "g", 60), ("6", "g", 60, COR)] + ps("de valência, faltam 2: faz 2 ligações", "i", 60), XE, 290, passo=0.08)
    trac = t >= C["s10.e"] + 1.0
    Q.lewis(c, t, C["s10.b"], [("O", -0.6, 0, [90, 270]), ("O", 0.6, 0, [90, 270])], [(0, 1, 2)], W / 2, 560, 230, 150,
            pontos=not trac, tl=[C["s10.b"]] * 2, tp=C["s10.d"])
    E.frase(c, t, C["s10.b"] + 0.6, [("2 pares", "g", 58), ("=", "g", 58, TINTA2), ("dupla", "g", 58, COR)], W / 2, 790, "center", 0.12)
    E.frase(c, t, C["s10.c"], ps("cada O: 4 na dupla, precisa de mais 4", "i", 56, TINTA2), W / 2, 880, "center", 0.08)
    E.foco(c, t, C["s10.d"], 0.4, lambda a: E.pilula(c, "2 pares livres em cada", W / 2 - 300, 990, 50, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s10.e"], 0.4, lambda a: E.formula(c, "4 + 4 = 8", W / 2 + 330, 1005, 70, "g", TINTA, a, "center"))


# ---------------- questão 3 ----------------
def panela(c, cx, cy, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - 130, cy - 60, 260, 130, 30, "#B9BFC7", a, shadow=True)
    M.rrect(c, cx - 150, cy - 74, 300, 30, 14, "#D3D8DE", a)
    M.rrect(c, cx + 140, cy - 70, 160, 26, 13, "#2A2B31", a)
    for k in range(3):
        fx = cx - 60 + 60 * k
        pth = skia.Path(); pth.moveTo(fx - 22, cy + 150); pth.quadTo(fx, cy + 80, fx + 4, cy + 100); pth.quadTo(fx + 26, cy + 120, fx + 22, cy + 150); pth.close()
        c.drawPath(pth, M.paint("#FF7A1A", a))


def b_questao3(c, t, C, b):
    titulo_q(c, t, C["s11.a"], 3)
    E.frase(c, t, C["s11.b"], ps("panela de alumínio: esquenta rápido", "i", 60), XE, 330, passo=0.08)
    E.frase(c, t, C["s11.c"], ps("papel-alumínio: dobra sem rasgar", "i", 60), XE, 440, passo=0.08)
    E.frase(c, t, C["s11.d"], ps("qual é a explicação das duas?", "i", 64), XE, 640, passo=0.08)
    if t < C["s12"]:
        E.foco(c, t, C["s11.b"] + 0.3, 0.5, lambda a: panela(c, 1430, 440, a))
    else:
        E.relogio(c, t, C["s12.a"], cx=1480, cy=470, r=200)


def b_resposta3(c, t, C, b):
    E.frase(c, t, C["s13"], ps("vamos lá", "i", 66, TINTA2), XE, 170)
    E.frase(c, t, C["s13.a"], [("alumínio:", "g", 62), ("metal", "g", 62, COR), ("→", "g", 62, TINTA2), ("ligação metálica", "i", 66)], XE, 280, passo=0.1)
    d = 90 * ease_io(prog(t, C["s13.c"] + 0.3, 1.2)) if t >= C["s13.c"] else 0
    metal(c, t, C["s13.a"] + 0.3, 760, 440, 8, 4, 100, 32, "Al", fluxo=C["s13.b"] if t < C["s13.c"] else None, desliza=d)
    if C["s13.b"] <= t < C["s13.c"]:
        g = skia.Paint(AntiAlias=True)
        w = 900 * ep(t, C["s13.b"], 2.0)
        g.setShader(skia.GradientShader.MakeLinear([skia.Point(700, 0), skia.Point(700 + w + 1, 0)], [M.hexc("#FF7A1A", 0.35), M.hexc("#FF7A1A", 0)], [0, 1]))
        c.drawRect(skia.Rect.MakeXYWH(700, 380, w, 420), g)
    E.foco(c, t, C["s13.b"], 0.4, lambda a: E.escreve(c, "elétrons livres levam o calor", 700, 880, 54, "b", TINTA, a))
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.escreve(c, "as fileiras escorregam; o mar segura tudo", 700, 960, 50, "i", TINTA2, a))
    pilula_em(c, t, C["s13.e"], "uma explicação só: elétrons livres", W / 2, 1040, 44, E.COR)


# ---------------- questão 4 ----------------
def b_questao4(c, t, C, b):
    titulo_q(c, t, C["s14.a"], 4)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (Q.atomo(c, XE + 50, 330, 44, "Mg", a), E.escreve(c, "magnésio: família 2", XE + 120, 352, 60, "b", TINTA, a)))
    E.foco(c, t, C["s14.b"] + 0.8, 0.5, lambda a: (Q.atomo(c, XE + 50, 450, 44, "O", a), E.escreve(c, "oxigênio", XE + 120, 472, 60, "b", TINTA, a)))
    E.frase(c, t, C["s14.b"] + 1.6, ps("um sólido branco que reveste fornos", "i", 56, TINTA2), XE, 570, passo=0.08)
    E.frase(c, t, C["s14.c"], [("1", "g", 56, COR)] + ps("qual é a fórmula?", "i", 62), XE, 720, passo=0.08)
    E.frase(c, t, C["s14.d"], [("2", "g", 56, COR)] + ps("conduz sólido? e derretido?", "i", 62), XE, 830, passo=0.08)
    if t < C["s15"]:
        reticulo(c, t, C["s14.b"] + 0.4, 1260, 320, 5, 4, 90, 26, 36)
    else:
        E.relogio(c, t, C["s15.a"], cx=1480, cy=470, r=200)


def b_resposta4(c, t, C, b):
    if t < C["s17"]:
        def s16():
            E.frase(c, t, C["s16"], ps("vamos lá", "i", 66, TINTA2), XE, 170)
            Q.formula_em(c, t, C["s16.a"], "Mg^{2+}", 560, 420, 160, align="center", cores={"carga": E.COR})
            Q.formula_em(c, t, C["s16.b"], "O^{2-}", 1000, 420, 160, align="center", cores={"carga": E.COR})
            E.frase(c, t, C["s16.c"], ps("cargas do mesmo tamanho: 1 para 1", "i", 60), W / 2, 590, "center", 0.1)
            Q.formula_em(c, t, C["s16.d"], "MgO", 780, 820, 190, align="center", cores={"Mg": E.COR, "O": E.COR})
            E.foco(c, t, C["s16.d"] + 0.5, 0.4, lambda a: E.selo(c, 1080, 760, 50, True, a))
            E.foco(c, t, C["s16.e"], 0.4, lambda a: Q.formula(c, "Mg2O2", 1500, 820, 120, ERRADO, a, "center"))
            if t >= C["s16.e"] + 0.6:
                E.risco(c, 1330, 840, 1670, 740, t, C["s16.e"] + 0.6, largura=10)
            E.frase(c, t, C["s16.e"] + 1.0, ps("reduza para a menor proporção", "i", 50, TINTA2), 1500, 940, "center", 0.08)
        E.saida(c, t, C["s17"] - 0.1, s16)
        return
    E.frase(c, t, C["s17.a"], [("metal + ametal:", "g", 62), ("iônica", "g", 62, COR)], XE, 190, passo=0.12)
    for k, (cue, nome, luz) in enumerate((("s17.b", "sólido", 0.0), ("s17.c", "derretido", 1.0))):
        cx = 520 + 560 * k
        def cena(a, cx=cx, luz=luz, k=k):
            lampada(c, cx, 360, luz * ep(t, C["s17.c"] + 0.5, 0.4) if k else 0, a)
            for s_ in (-1, 1):
                M.line(c, cx + s_ * 26, 440, cx + s_ * 100, 500, TINTA, a, 6)
                M.line(c, cx + s_ * 100, 500, cx + s_ * 100, 640, TINTA, a, 6)
            if k == 0:
                reticulo(c, 99, 0, cx - 120, 680, 4, 2, 80, 24, 32, a=a)
            else:
                for j in range(8):
                    xx = cx - 140 + 280 * _h(j, 7) + 20 * math.sin(t * 1.5 + j)
                    yy = 690 + 90 * _h(j, 8) + 14 * math.cos(t * 1.7 + j)
                    ion(c, xx, yy, 24 if j % 2 == 0 else 32, "Mg" if j % 2 == 0 else "O", "Mg^{2+}" if j % 2 == 0 else "O^{2-}", a)
            centro(c, nome, cx, 900, 60, "g", TINTA, a)
            centro(c, "não conduz" if k == 0 else "conduz", cx, 970, 52, "b", ERRADO if k == 0 else CERTO, a)
        E.foco(c, t, C[cue], 0.5, cena)
    E.frase(c, t, C["s17.d"], ps("e o forno? ponto de fusão alto", "i", 54), 1470, 420, "center", 0.08)
    E.foco(c, t, C["s17.e"], 0.5, lambda a: (E.escreve(c, "≈ 2850 °C", 1360, 600, 96, "g", COR, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s18.a", [("a família", "g", 64)] + ps("dá a carga", "i", 66)),
                 ("s18.b", [("o cruzamento", "g", 64)] + ps("dá a fórmula", "i", 66)),
                 ("s18.c", [("o que falta para 8", "g", 64)] + ps("dá as ligações", "i", 66)),
                 ("s18.d", [("o tipo de ligação", "g", 64)] + ps("dá as propriedades", "i", 66)))
        for i, (k, partes) in enumerate(itens):
            y = 340 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 50, a=a), centro(c, str(i + 1), 260, y - 2, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 350, y, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 240)
    E.frase(c, t, C["s19.a"], [("geometria", "g", 110, COR)], XE, 390)
    E.frase(c, t, C["s19.a"] + 0.4, [("molecular", "g", 110, COR)], XE, 510)
    E.frase(c, t, C["s19.b"], ps("água dobrada, gás carbônico reto", "i", 60), XE, 640, passo=0.1)
    Q.molecula(c, t, C["s19.b"] + 0.4, "H2O", 480, 840, 110)
    Q.molecula(c, t, C["s19.b"] + 0.8, "CO2", 960, 850, 110)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, atalho=b_atalho,
              questao2=b_questao2, resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3,
              questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
