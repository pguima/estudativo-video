"""Visual — Estudativo · FIS-CIN-017: praticando gráficos, queda e lançamentos (aula de prática, 5 situações).

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001/roteiro/visual.py (peças em _ferramentas/fisica.py, F).
Cada situação: enunciado à esquerda e desenho à direita; na cena "pause o vídeo", o relógio toma o lugar do desenho.
Gráfico v × t com a linha em petróleo (F.VEL) e a área em laranja; corpo que cai em laranja; trajetórias tracejadas em
laranja. Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-017_praticando_graficos_queda_lancamentos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "atalho", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert -20 / 4 == -5 and 4 * 20 / 2 == 40 and 400 / (2 * 5) == 40
assert math.sqrt(125 / 5) == 5 and 10 * 5 == 50 and 50 * 3.6 == 180 and [5 * t * t for t in range(1, 6)] == [5, 20, 45, 80, 125]
assert 8 / 2 == 4 and 10 * 4 == 40 and 5 * 4 ** 2 == 80 and 1600 / 20 == 80
assert math.sqrt(5 / 5) == 1 and 3 * 1 == 3 and 6 * 1 == 6 and 30 + 60 == 90


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def promessa(c, t, C, cena, itens, size=76):
    """“até o fim da aula” + itens numerados [(cue, texto)] + a órbita da Física à direita"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    passo_y = 150 if len(itens) <= 3 else 128
    for i, (k, s) in enumerate(itens):
        y = 430 + i * passo_y
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 38, a=a), centro(c, str(i + 1), XE + 40, y - 6, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", size, COR if i == 0 else TINTA)], XE + 110, y)


def lembrete(c, t, C, cena, itens, num="2", titulo=("coisas",)):
    """você precisa de N coisas: itens = [(cue, linha fina, linha forte, desenho(a, x, y) ou None)]"""
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 80), XE, 380, passo=0.14)
    t1 = C[itens[0][0]] - 0.6 if num is None else C[cena + ".a"]
    if num:
        E.foco(c, t, t1, 0.5, lambda a: E.escreve(c, num, XE - 8, 700, 320, "g", COR, a))
        E.foco(c, t, t1 + 0.15, 0.5, lambda a: E.escreve(c, titulo[0], XE + 205, 680, 110, "i", TINTA, a))
    else:
        for j, s in enumerate(titulo):
            E.frase(c, t, t1 + 0.2 * j, [(s, "g", 110, COR)], XE, 540 + 130 * j)
    n = len(itens)
    x, w = 820, 1000
    h = 230 if n == 2 else 190
    gap = 290 if n == 2 else 225
    y0 = 230 if n == 2 else 150
    for i, (k, l1, l2, des) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 54)], x + 44, y + h * 0.4)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + h * 0.75)
        if des:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, des=des, y=y: des(a, x + w - 170, y + h / 2))
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 52, COR) + ps("procure no canal", "i", 52),
            820, y0 + n * gap + 20, "left", 0.12)


def fim(c, t, C, cr, itens, cp, linhas, desenho, k_insc, k_bons):
    """resumo numerado (cena cr, itens = [(cue, partes)]) e a ponte (cena cp): linhas = [(cue, partes)], desenho(a) à esquerda embaixo"""
    def resumo():
        E.frase(c, t, C[cr], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 175
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C[cp] - 0.1, resumo)
    if t < C[cp]:
        return
    E.frase(c, t, C[cp], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    for i, (k, partes) in enumerate(linhas):
        E.frase(c, t, C[k], partes, XE, 400 + 140 * i, passo=0.12)
    desenho()
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


# ---------------- peças desta aula ----------------
def situacao(c, t, C, cq, cp, n, linhas, desenho):
    """tela de enunciado: "situação n" + linhas [(instante, partes, y)]; desenho() à direita até a cena da pausa cp"""
    E.frase(c, t, C[cq + ".a"], [("situação", "i", 70, COR), (str(n), "g", 76, COR)], XE, 200, passo=0.12)
    for ti, partes, y in linhas:
        E.frase(c, t, ti, partes, XE, y, passo=0.12)
    if t < C[cp]:
        desenho()
    else:
        E.relogio(c, t, C[cp + ".a"], cx=1460, cy=440, r=200)


def chao_em(c, t, t0, x0, x1, y):
    if t >= t0:
        F.chao(c, x0, x1, y, ep(t, t0, 0.5))


def casa(c, x, yb, w, h, a=1.0):
    """casa com telhado plano; topo em yb − h, borda direita em x + w"""
    if a <= 0:
        return
    M.rrect(c, x, yb - h, w, h, 6, "#D9CBB4", a)
    M.rrect(c, x - 10, yb - h - 16, w + 20, 22, 6, "#8B5E3C", a)
    M.rrect(c, x + w * 0.4, yb - h * 0.45, w * 0.22, h * 0.45, 4, "#8B5E3C", a)
    M.rrect(c, x + w * 0.12, yb - h * 0.75, w * 0.2, h * 0.2, 4, "#8FA9C2", a)


def traj(c, t, t0, x0, yb, vx, vy, k, d=1.0, cor=None, largura=6, tracejada=False):
    T = 2 * vy / 10
    P = lambda tau: (x0 + vx * tau * k, yb - (vy * tau - 5 * tau * tau) * k)
    if t >= t0:
        F.poli(c, [P(T * i / 80) for i in range(81)], ease_io(prog(t, t0, d)), cor or E.COR, 1.0, largura, dash=E.TRACO if tracejada else None)
    return P


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.foco(c, t, C["s01.a"], 0.6, lambda a: E.escreve(c, "5", XE - 10, 560, 400, "g", COR, a))
    E.frase(c, t, C["s01.a"] + 0.3, [("situações", "g", 110)], XE + 300, 470)
    E.frase(c, t, C["s01.a"] + 0.9, ps("gráficos, quedas e lançamentos", "i", 64), XE + 300, 570, passo=0.1)
    E.foco(c, t, C["s01.b"], 0.5, lambda a: E.pilula(c, "pause e resolva antes", XE + 640, 780, 60, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s01.b"] + 0.4, 0.6, lambda a: E.simbolo(c, 1600, 300, 150 * a, giro=12 * math.sin(t * 0.4)), blur=0)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 84), XE, 200, passo=0.14)
    itens = (("s02.a", [("v × t:", "g", 58, F.VEL), ("inclinação = aceleração,", "i", 60), ("área = deslocamento", "i", 60)]),
             ("s02.b", [("queda:", "g", 58, COR), ("h = 5 · t²", "g", 58), ("e", "i", 60), ("v = 10 · t", "g", 58)]),
             ("s02.c", [("subida:", "g", 58, COR), ("mesmo", "i", 60), ("tempo", "i", 60), ("da", "i", 60), ("descida", "i", 60)]),
             ("s02.d", [("lançamentos:", "g", 58, COR), ("cada", "i", 60), ("direção", "i", 60), ("na", "i", 60), ("sua", "i", 60)]))
    for i, (k, partes) in enumerate(itens):
        y = 360 + i * 150
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 30, y - 22, 30, a=a), centro(c, str(i + 1), XE + 30, y - 4, 38, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, XE + 90, y, passo=0.1)
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.6), ps("travou?", "i", 52, COR) + ps("procure a aula no canal", "i", 52), XE + 90, 960, "left", 0.1)


# ---------------- situação 1: gráfico ----------------
def g1(c, t, t0, x=1000, y=260, w=760, h=520):
    return F.grafico(c, t, t0, x, y, w, h, 0, 5, 0, 25, "t (s)", "v (m/s)", 1, 5)


def b_questao1(c, t, C, b):
    def desenho():
        P = g1(c, t, C["s03.d"] - 0.6)
        E.curva(c, t, C["s03.d"], P, lambda x: 20 - 5 * x, 0, 4, d=0.8, cor=F.VEL, largura=8)
    situacao(c, t, C, "s03", "s04", 1, [
        (C["s03.b"], [("carro", "i", 70), ("a", "i", 70), ("20 m/s", "g", 70, F.VEL), ("freia", "g", 70)], 340),
        (C["s03.c"], [("para", "i", 70), ("em", "i", 70), ("4 s", "g", 70)], 450),
        (C["s03.e"], [("aceleração?", "g", 70, COR)], 640),
        (C["s03.f"], [("distância", "g", 70), ("até", "i", 70), ("parar?", "g", 70, COR)], 760)], desenho)


def b_resposta1(c, t, C, b):
    P = g1(c, t, C["s05"])
    E.curva(c, t, C["s05"] + 0.2, P, lambda x: 20 - 5 * x, 0, 4, d=0.6, cor=F.VEL, largura=8)
    if t >= C["s05.a"]:
        q = ep(t, C["s05.a"], 0.5)
        M.line(c, P.x(0), P.y(20), P.x(4), P.y(20), E.COR, q, 5, dash=E.TRACO)
        E.foco(c, t, C["s05.a"] + 0.4, 0.4, lambda a: (F.medida(c, "−20", "m/s", P.x(4) + 20, P.y(10), 46, COR, a), F.medida(c, 4, "s", P.x(2), P.y(20) - 20, 46, COR, a, "center")))
    E.formula_em(c, t, C["s05.b"], "a = f{−20}{4} =", XE, 330, 76, "g", TINTA)
    bola_txt(c, t, C["s05.c"], "−5 m/s^2", XE + 600, 305, 105, 46, F.ACEL)
    E.frase(c, t, lerp(C["s05.c"], C["s05.d"], 0.4), ps("menos: está freando", "i", 50, TINTA2), XE, 470, passo=0.1)
    if t >= C["s05.d"]:
        F.area_graf(c, t, C["s05.d"], P, lambda x: 20 - 5 * x, 0, 4, "40 m")
    E.formula_em(c, t, C["s05.d"], "d = f{4 · 20}{2} =", XE, 630, 76, "g", TINTA)
    bola_txt(c, t, C["s05.e"], "40 m", XE + 640, 605, 95, 56)
    E.formula_em(c, t, C["s05.f"], "Torricelli: 400 = 2 · 5 · d → d = 40", XE, 830, 46, "g", CERTO)


# ---------------- situação 2: queda ----------------
def regua(c, t, t0, x, ytop, k, marcas):
    yv = lambda h: ytop + h * k
    if t >= t0:
        M.line(c, x, ytop, x, lerp(ytop, yv(marcas[-1]) + 20, ease_io(prog(t, t0, 0.6))), TINTA2, 1.0, 4, dash=E.TRACO)
    for i, h in enumerate(marcas):
        E.foco(c, t, t0 + 0.2 + 0.06 * i, 0.4, lambda a, h=h: (M.line(c, x - 14, yv(h), x + 14, yv(h), TINTA2, a, 4),
                                                              F.medida(c, h, "m", x - 30, yv(h) + 16, 42, TINTA2, a, "right")))
    return yv


def penhasco(c, x, ytop, ybase, a=1.0):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x - 300, ybase); p.lineTo(x - 300, ytop); p.lineTo(x, ytop); p.lineTo(x + 20, ytop + 60); p.lineTo(x - 10, ybase); p.close()
    c.drawPath(p, M.paint("#A08A70", a))


def b_questao2(c, t, C, b):
    def desenho():
        E.foco(c, t, C["s06.b"], 0.5, lambda a: penhasco(c, 1420, 260, 960, a))
        chao_em(c, t, C["s06.b"], 1100, 1860, 960)
        E.foco(c, t, C["s06.b"] + 0.3, 0.4, lambda a: E.bola(c, 1460, 240, 26, a=a))
        if t >= C["s06.b"] + 0.4:
            M.line(c, 1520, 240, 1520, 960, TINTA2, ep(t, C["s06.b"] + 0.4, 0.4), 4, dash=E.TRACO)
            E.foco(c, t, C["s06.b"] + 0.6, 0.4, lambda a: F.medida(c, 125, "m", 1550, 620, 64, COR, a))
    situacao(c, t, C, "s06", "s07", 2, [
        (C["s06.b"], [("pedra", "i", 70), ("cai", "i", 70), ("de", "i", 70), ("125 m", "g", 70, COR)], 340),
        (C["s06.b"] + 1.4, ps("despreze o ar", "i", 54, TINTA2), 430),
        (C["s06.c"], [("quanto", "i", 70), ("tempo?", "g", 70, COR)], 620),
        (C["s06.d"], [("velocidade", "g", 70), ("de", "i", 70), ("chegada?", "g", 70, COR)], 740)], desenho)


def b_resposta2(c, t, C, b):
    E.formula_em(c, t, C["s08.a"], "125 = 5 · t^2", XE, 300, 84, "g", TINTA)
    E.formula_em(c, t, C["s08.b"], "t^2 = 25", XE, 450, 84, "g", TINTA)
    bola_txt(c, t, C["s08.c"], "5 s", XE + 560, 420, 95, 64)
    E.formula_em(c, t, C["s08.d"], "v = 10 · 5 =", XE, 680, 84, "g", TINTA)
    bola_txt(c, t, C["s08.d"] + 1.6, "50 m/s", XE + 720, 655, 120, 58, F.VEL)
    E.foco(c, t, lerp(C["s08.d"], C["s08.end"], 0.75), 0.5, lambda a: E.pilula(c, "= 180 km/h", XE + 720, 840, 50, "g", fundo=TINTA, a=a))
    yv = regua(c, t, C["s08"], 1580, 180, 6.0, [0, 5, 20, 45, 80, 125])
    for i, (h, ti) in enumerate(((0, C["s08"] + 0.3), (125, C["s08.c"]))):
        E.foco(c, t, ti, 0.4, lambda a, h=h, i=i: E.bola(c, 1680, yv(h), 24, a=a * (1.0 if i == 1 else 0.35)))


# ---------------- atalho: a tabela da queda ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s09"], ps("aqui cabe o atalho:", "i", 70, CLARO) + [("a tabela da queda", "g", 70, BR)], W / 2, 170, "center", 0.12)
    E.foco(c, t, C["s09.b"] - 0.4, 0.4, lambda a: (centro(c, "t (s)", 640, 320, 54, "b", CLARO, a), centro(c, "h (m)", 1280, 320, 54, "b", CLARO, a),
                                                   M.line(c, 470, 345, 1450, 345, CLARO, a, 3)))
    for i, (tt, h) in enumerate(((1, 5), (2, 20), (3, 45), (4, 80), (5, 125))):
        y = 440 + i * 100
        E.foco(c, t, C["s09.b"] + 0.35 * i, 0.4, lambda a, y=y, h=h: centro(c, str(h), 1280, y, 72, "g", E.CLARO, a))
        E.foco(c, t, C["s09.c"] + 0.3 * i, 0.4, lambda a, y=y, tt=tt: centro(c, str(tt), 640, y, 72, "g", BR, a))
    if t >= C["s09.d"]:
        q = ep(t, C["s09.d"], 0.4)
        M.rrect(c, 520, 840 - 70, 900, 96, 20, E.COR, 0.35 * q)
        E.foco(c, t, C["s09.d"] + 0.2, 0.4, lambda a: E.escreve(c, "sem conta!", 1480, 840, 52, "g", BR, a))
    E.frase(c, t, C["s09.e"], ps("fora da tabela:", "i", 56, CLARO) + [("÷ 5", "g", 56, BR), ("e", "i", 56, CLARO), ("raiz", "g", 56, BR)], W / 2, 1000, "center", 0.1)


# ---------------- situação 3: lançamento vertical ----------------
def mao(c, x, y, s=1.0, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x - 60 * s, y, 120 * s, 46 * s, 22 * s, "#E0A87E", a)
    for i in range(4):
        M.rrect(c, x - 58 * s + i * 30 * s, y - 34 * s, 24 * s, 48 * s, 12 * s, "#E0A87E", a)
    M.rrect(c, x - 40 * s, y + 40 * s, 80 * s, 120 * s, 20 * s, "#E0A87E", a)


def b_questao3(c, t, C, b):
    def desenho():
        x, yb = 1450, 880
        E.foco(c, t, C["s10.a"], 0.5, lambda a: mao(c, x, yb, 1.0, a))
        u = max(0.0, min(8.0, (t - C["s10.a"] - 0.3) / max(0.5, C["s10.b"] + 1.0 - C["s10.a"] - 0.3) * 8))
        h = 40 * u - 5 * u * u
        E.foco(c, t, C["s10.a"] + 0.2, 0.4, lambda a: E.bola(c, x, yb - 40 - h * 7, 30, a=a))
        E.foco(c, t, C["s10.b"], 0.5, lambda a: F.cronometro(c, 1700, 300, 80, 8, a, "8 s"))
    situacao(c, t, C, "s10", "s11", 3, [
        (C["s10.a"] + 0.4, ps("bola jogada para cima", "i", 66), 340),
        (C["s10.b"], [("volta", "i", 70), ("à", "i", 70), ("mão", "i", 70), ("em", "i", 70), ("8 s", "g", 70, COR)], 450),
        (C["s10.c"], [("velocidade", "g", 70), ("de", "i", 70), ("saída?", "g", 70, COR)], 640),
        (C["s10.d"], [("altura", "g", 70), ("máxima?", "g", 70, COR)], 760)], desenho)


def b_resposta3(c, t, C, b):
    E.frase(c, t, C["s12.a"], ps("subida = descida", "g", 66), XE, 250, passo=0.12)
    E.formula_em(c, t, C["s12.b"], "f{8}{2} = 4 s para subir", XE, 380, 72, "g", TINTA)
    E.formula_em(c, t, C["s12.c"], "v₀ = 10 · 4 =", XE, 560, 76, "g", TINTA)
    bola_txt(c, t, C["s12.c"] + 1.4, "40 m/s", XE + 650, 535, 110, 54, F.VEL)
    E.formula_em(c, t, C["s12.d"], "H = 5 · 4^2 =", XE, 740, 76, "g", TINTA)
    bola_txt(c, t, C["s12.e"], "80 m", XE + 650, 715, 100, 58)
    E.formula_em(c, t, C["s12.f"], "Torricelli: f{1600}{20} = 80", XE, 920, 56, "g", CERTO)
    # a bola: subida e descida lado a lado
    yb, k = 940, 8.0
    for j, (x, lab) in enumerate(((1450, "sobe 4 s"), (1650, "desce 4 s"))):
        E.foco(c, t, C["s12.a"] + 0.3 * j, 0.4, lambda a, x=x, lab=lab, j=j: (
            F.seta(c, x, yb - 20 - (0 if j == 0 else 80 * k), x, yb - 20 - (80 * k if j == 0 else 0), F.VEL, a, 8),
            centro(c, lab, x, yb + 50, 44, "i", TINTA2, a)))
    chao_em(c, t, C["s12.a"], 1300, 1800, yb)


# ---------------- situação 4: lançamento horizontal ----------------
def b_questao4(c, t, C, b):
    x0, y0, yb, k = 1400, 500, 900, 70.0

    def desenho():
        E.foco(c, t, C["s13.b"], 0.5, lambda a: casa(c, x0 - 300, yb, 300, yb - y0, a))
        chao_em(c, t, C["s13.b"], x0 - 360, 1880, yb)
        E.foco(c, t, C["s13.b"] + 0.4, 0.4, lambda a: F.medida(c, 5, "m", x0 + 24, (y0 + yb) / 2, 60, COR, a))
        E.foco(c, t, C["s13.c"], 0.4, lambda a: (E.bola(c, x0, y0 - 40, 24, a=a), F.seta(c, x0 + 40, y0 - 90, x0 + 200, y0 - 90, F.VEL, a, 9),
                                                 F.medida(c, 3, "m/s", x0 + 220, y0 - 74, 48, F.VEL, a)))
    situacao(c, t, C, "s13", "s14", 4, [
        (C["s13.b"], [("telhado", "i", 70), ("de", "i", 70), ("5 m", "g", 70, COR)], 340),
        (C["s13.c"], [("sai", "i", 70), ("na", "i", 70), ("horizontal", "i", 70), ("a", "i", 70), ("3 m/s", "g", 70, F.VEL)], 450),
        (C["s13.d"], [("a", "i", 66), ("que", "i", 66), ("distância", "g", 66, COR), ("cai?", "g", 66, COR)], 640),
        (C["s13.e"], [("e", "i", 66), ("com", "i", 66), ("o", "i", 66), ("dobro", "g", 66), ("da", "i", 66), ("velocidade?", "g", 66, COR)], 760)], desenho)


def b_resposta4(c, t, C, b):
    x0, y0, yb, k = 1400, 500, 900, 70.0
    E.foco(c, t, C["s15"], 0.5, lambda a: casa(c, x0 - 300, yb, 300, yb - y0, a))
    chao_em(c, t, C["s15"], x0 - 360, 1880, yb)
    E.bola(c, x0, y0 - 24, 22, a=ep(t, C["s15"], 0.4))
    for j, (vx, ti, cor, lab) in enumerate(((3, C["s15.b"], E.COR, "3 m"), (6, C["s15.d"], TINTA, "6 m"))):
        if t >= ti:
            pts = [(x0 + vx * u * k, y0 - 24 + (yb - 22 - y0 + 24) * u * u) for u in [i / 40 for i in range(41)]]
            F.poli(c, pts, ease_io(prog(t, ti, 0.8)), cor, 1.0, 6, dash=E.TRACO if j == 0 else None)
            E.foco(c, t, ti + 0.6, 0.4, lambda a, vx=vx, lab=lab, cor=cor: F.medida(c, *lab.split(" "), x0 + vx * k, yb + 70, 54, cor, a, "center"))
    E.formula_em(c, t, C["s15.a"], "5 = 5 · t^2 → t = 1 s", XE, 300, 66, "g", TINTA)
    E.formula_em(c, t, C["s15.b"], "A = 3 · 1 = 3 m", XE, 430, 66, "g", COR)
    E.frase(c, t, C["s15.c"], [("dobro", "g", 62), ("da", "i", 62), ("v:", "g", 62), ("t", "g", 62), ("continua", "i", 62), ("1 s", "g", 62, CERTO)], XE, 600, passo=0.1)
    E.frase(c, t, C["s15.c"] + 1.2, ps("a altura manda no tempo", "i", 56, TINTA2), XE, 690, passo=0.1)
    E.formula_em(c, t, C["s15.d"], "A = 6 · 1 = 6 m", XE, 850, 66, "g", TINTA)


# ---------------- situação 5: ângulos ----------------
def b_questao5(c, t, C, b):
    x0, yb, k = 1060, 880, 18.0

    def desenho():
        chao_em(c, t, C["s16.b"], 980, 1860, yb)
        E.foco(c, t, C["s16.b"], 0.4, lambda a: E.bola(c, x0, yb - 20, 20, a=a))
        for ang, ti, cor in ((30, C["s16.b"], TINTA2), (60, C["s16.c"], TINTA)):
            r = math.radians(ang)
            F.vetor(c, t, ti + 0.2, (x0, yb - 20), (x0 + 220 * math.cos(r), yb - 20 - 220 * math.sin(r)), None, None, F.VEL, 8)
            E.foco(c, t, ti + 0.5, 0.4, lambda a, ang=ang, r=r: E.pilula(c, f"{ang}°", x0 + 300 * math.cos(r) + 30, yb - 20 - 300 * math.sin(r), 40, "g", fundo=TINTA, a=a))
    situacao(c, t, C, "s16", "s17", 5, [
        (C["s16.a"] + 0.8, ps("sem conta:", "i", 62, TINTA2), 300),
        (C["s16.b"], [("chute", "i", 66), ("a", "i", 66), ("30°", "g", 66, COR)], 420),
        (C["s16.c"], [("chute", "i", 66), ("a", "i", 66), ("60°", "g", 66, COR)], 520),
        (C["s16.d"], [("qual", "i", 66), ("vai", "i", 66), ("mais", "i", 66), ("longe?", "g", 66, COR)], 680),
        (C["s16.e"], [("e", "i", 66), ("o", "i", 66), ("maior", "g", 66), ("alcance?", "g", 66, COR)], 790)], desenho)


def b_resposta5(c, t, C, b):
    x0, yb, k = 980, 900, 22.0
    chao_em(c, t, C["s18"], 900, 1880, yb)
    for j, (ang, ti, cor, larg) in enumerate(((30, C["s18.a"], TINTA2, 6), (60, C["s18.a"] + 0.5, TINTA, 6), (45, C["s18.e"], E.COR, 8))):
        r = math.radians(ang)
        traj(c, t, ti, x0, yb, 20 * math.cos(r), 20 * math.sin(r), k, d=0.9, cor=cor, largura=larg)
    if t >= C["s18.c"]:
        X = x0 + 34.64 * k
        c.drawCircle(X, yb, 40 + 4 * math.sin(t * 5), M.paint(CERTO, ep(t, C["s18.c"], 0.4), stroke=6))
    E.frase(c, t, C["s18"] + 0.4, [("30°", "g", 66), ("+", "g", 66, TINTA2), ("60°", "g", 66), ("=", "g", 66, TINTA2), ("90°", "g", 66, COR)], XE, 260, passo=0.12)
    E.foco(c, t, C["s18.a"], 0.4, lambda a: E.pilula(c, "complementares", XE + 230, 360, 48, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s18.b"], [("sen", "g", 60), ("de", "i", 62), ("um", "i", 62), ("=", "g", 60), ("cos", "g", 60), ("do", "i", 62), ("outro", "i", 62)], XE, 500, passo=0.1)
    E.frase(c, t, C["s18.c"], [("mesmo", "g", 66, CERTO), ("ponto", "g", 66, CERTO)], XE, 620, passo=0.12)
    E.frase(c, t, C["s18.d"], ps("o de 60° sobe mais e demora mais", "i", 52, TINTA2), XE, 720, passo=0.1)
    E.frase(c, t, C["s18.e"], [("maior", "i", 66), ("alcance:", "i", 66), ("45°", "g", 72, COR)], XE, 860, passo=0.12)
    E.frase(c, t, C["s18.e"] + 1.0, ps("mesma altura de saída e chegada, sem ar", "i", 46, TINTA2), XE, 940, passo=0.08)


# ---------------- fechamento ----------------
def ventilador(c, x, y, r, giro, a=1.0):
    if a <= 0:
        return
    for k in range(3):
        g = math.radians(giro + 120 * k)
        c.save(); c.translate(x, y); c.rotate(math.degrees(g))
        c.drawOval(skia.Rect.MakeXYWH(r * 0.1, -r * 0.18, r * 0.9, r * 0.36), M.paint(E.COR, a))
        c.restore()
    c.drawCircle(x, y, r * 0.16, M.paint(TINTA, a))


def b_fim(c, t, C, b):
    itens = (("s19.a", [("gráfico:", "g", 66), ("leia", "i", 70), ("o", "i", 70), ("eixo", "g", 66, COR)]),
             ("s19.b", [("queda:", "g", 66), ("a", "i", 70), ("tabela", "i", 70), ("do", "i", 70), ("5", "g", 66, COR)]),
             ("s19.c", [("lançamento:", "g", 66), ("a", "i", 70), ("altura", "g", 66, COR), ("manda", "i", 70), ("no", "i", 70), ("tempo", "i", 70)]))

    def desenho():
        E.foco(c, t, C["s20.a"], 0.5, lambda a: ventilador(c, 420, 760, 170, (t - C["s20.a"]) * 400, a))
        E.frase(c, t, C["s20.b"], ps("período, frequência e rpm", "g", 56, COR), 660, 740, passo=0.1)
    fim(c, t, C, "s19", itens, "s20", [("s20.a", [("O", "g", 110, COR), ("que", "g", 110, COR), ("gira", "g", 110, COR)])], desenho, "s20.d", "s20.e")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              atalho=b_atalho, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
