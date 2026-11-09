"""Visual — Estudativo · FIS-CIN-014: lançamento vertical para cima.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001/roteiro/visual.py (peças em _ferramentas/fisica.py, F).
Nesta aula: a bola é a esfera laranja; cada foto da bola (a cada segundo) leva a seta da velocidade em petróleo (F.VEL),
com o tamanho proporcional ao módulo; a gravidade g é a seta violeta (F.ACEL), sempre para baixo. Subida e descida ficam
lado a lado (subida à esquerda) para mostrar a simetria. Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-014_lancamento_vertical.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("subida", "altura", "simetria", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
s_ = lambda v0, t: v0 * t - 5 * t * t
assert [20 - 10 * t for t in (0, 1, 2)] == [20, 10, 0] and 20 / 10 == 2 and 20 ** 2 / (2 * 10) == 20 and 5 * 2 ** 2 == 20
assert [s_(20, t) for t in (0, 1, 2, 3, 4)] == [0, 15, 20, 15, 0] and 2 * 2 == 4
assert 30 / 10 == 3 and 5 * 3 ** 2 == 45 and 900 / 20 == 45 and 2 * 3 == 6


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
def fotos_bola(c, t, x, yv, fotos, r=30, kv=9.0, lado=1):
    """fotos da bola: [(instante, altura, rótulo do tempo, velocidade com sinal ou None)]. A velocidade vira seta petróleo
    (kv px por m/s) ao lado da bola; a última foto fica forte"""
    for i, (ti, h, rot, v) in enumerate(fotos):
        q = ep(t, ti, 0.4)
        if q <= 0:
            continue
        ultima = i == len(fotos) - 1 or t < fotos[i + 1][0]
        y = yv(h)
        E.bola(c, x, y, r, None, q * (1.0 if ultima else 0.35))
        if rot:
            E.foco(c, t, ti + 0.1, 0.3, lambda a, y=y, s=rot: E.pilula(c, s, x - lado * (r + 60), y, 34, "b", fundo=TINTA, a=a))
        if v is not None:
            xs = x + lado * (r + 40)
            if v > 0:
                F.seta(c, xs, y, xs, y - v * kv, F.VEL, q * (1.0 if ultima else 0.6), 8, p=ease_io(prog(t, ti, 0.4)))
            elif v < 0:  # para baixo: a seta termina na altura da bola, para não furar o chão
                F.seta(c, xs, y + v * kv, xs, y, F.VEL, q * (1.0 if ultima else 0.6), 8, p=ease_io(prog(t, ti, 0.4)))
            E.foco(c, t, ti + 0.2, 0.3, lambda a, y=y, v=v, xs=xs: F.medida(c, abs(v), "m/s", xs + lado * 26, y + 16, 44, F.VEL, a,
                                                                       "left" if lado > 0 else "right"))


def chao_em(c, t, t0, x0, x1, y):
    if t >= t0:
        F.chao(c, x0, x1, y, ep(t, t0, 0.5))


def mao(c, x, y, s=1.0, a=1.0):
    """mão espalmada para cima, com a palma em y"""
    if a <= 0:
        return
    M.rrect(c, x - 60 * s, y, 120 * s, 46 * s, 22 * s, "#E0A87E", a)
    for i in range(4):
        M.rrect(c, x - 58 * s + i * 30 * s, y - 34 * s, 24 * s, 48 * s, 12 * s, "#E0A87E", a)
    M.rrect(c, x - 40 * s, y + 40 * s, 80 * s, 120 * s, 20 * s, "#E0A87E", a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        x, yb, k = 1450, 900, 30.0
        E.foco(c, t, C["s01"], 0.5, lambda a: mao(c, x, yb + 20, 1.0, a))
        # a bola sobe e desce num ciclo de 4 "segundos" esticados entre s01.a e s01.c
        t0, t1 = C["s01.a"] + 0.3, C["s01.c"]
        u = min(4.0, max(0.0, (t - t0) / max(0.5, t1 - t0) * 4))
        h = 20 * u - 5 * u * u
        E.foco(c, t, C["s01"] + 0.3, 0.4, lambda a: E.bola(c, x, yb - 20 - h * k, 34, a=a))
        if t >= C["s01.a"] + 0.3:
            F.seta(c, x + 90, yb - 60, x + 90, yb - 260, F.VEL, ep(t, C["s01.a"] + 0.3, 0.3) * (1 - ep(t, C["s01.c"], 0.3)), 9)
        E.frase(c, t, C["s01.a"], [("para", "i", 74), ("cima", "g", 74)], XE, 300, passo=0.12)
        E.foco(c, t, C["s01.a"] + 0.6, 0.5, lambda a: F.medida(c, 20, "m/s", XE, 430, 110, F.VEL, a))
        E.frase(c, t, C["s01.b"], ps("quanto tempo", "i", 72) + [("no ar?", "g", 72, COR)], XE, 580, passo=0.12)
        bola_txt(c, t, C["s01.c"], "4 s", XE + 150, 760, 100, 70)
        E.frase(c, t, C["s01.d"], [("no", "i", 60), ("alto:", "i", 60), ("v = 0", "g", 60, F.VEL)], XE + 320, 760, passo=0.12)
        E.frase(c, t, C["s01.e"], [("mas", "i", 60), ("g", "g", 60, F.ACEL), ("continua", "g", 60)], XE + 320, 850, passo=0.12)
        if t >= C["s01.e"]:
            F.seta(c, x - 120, yb - 600 + 30, x - 120, yb - 600 + 230, F.ACEL, ep(t, C["s01.e"], 0.3), 10, p=ease_io(prog(t, C["s01.e"], 0.5)))
            E.foco(c, t, C["s01.e"] + 0.3, 0.3, lambda a: E.escreve(c, "g", x - 190, yb - 420, 64, "g", F.ACEL, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "o tempo de subida"), ("s02.c", "a altura máxima"), ("s02.d", "o tempo no ar")))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def g(a, x, y):
        F.seta(c, x - 40, y - 70, x - 40, y + 70, F.ACEL, a, 10)
        E.escreve(c, "g", x + 0, y + 20, 64, "g", F.ACEL, a)

    def h(a, x, y):
        E.formula(c, "h = 5 · t^2", x - 60, y + 20, 56, "g", TINTA, a, "center")
    lembrete(c, t, C, "s03", (("s03.a", "a gravidade muda v em", "10 m/s a cada segundo", g),
                              ("s03.b", "a altura da queda:", "h = 5 · t²", None)), num=None, titulo=("queda", "livre"))


# ---------------- subida ----------------
def b_subida(c, t, C, b):
    x, yb, k = 1380, 900, 30.0
    yv = lambda h: yb - 20 - h * k
    chao_em(c, t, C["s04"], 1100, 1800, yb)

    fotos = [(C["s04.c"], 0, "0 s", 20), (C["s04.d"], 15, "1 s", 10), (C["s04.e"], 20, "2 s", 0)]
    fotos_bola(c, t, x, yv, fotos)
    if t >= C["s04"] + 0.4:  # a gravidade, para baixo
        F.seta(c, 1760, 200, 1760, 380, F.ACEL, ep(t, C["s04"] + 0.4, 0.4), 10)
        E.foco(c, t, C["s04"] + 0.6, 0.3, lambda a: E.escreve(c, "g", 1700, 320, 64, "g", F.ACEL, a))
    E.foco(c, t, C["s04.f"], 0.5, lambda a: E.pilula(c, "ponto mais alto", x - 260, yv(20) - 70, 42, "g", fundo=E.COR, a=a))

    def s04():
        E.frase(c, t, C["s04"], ps("na subida, a gravidade", "i", 62), XE, 260, passo=0.12)
        E.frase(c, t, C["s04.a"], [("freia", "g", 110, COR)], XE, 400)
        E.frase(c, t, C["s04.b"], [("−10 m/s", "g", 76, F.VEL)], XE, 560)
        E.frase(c, t, C["s04.b"] + 0.6, ps("a cada segundo", "i", 64), XE, 650, passo=0.12)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], ps("para cima positivo:", "i", 54, TINTA2) + [("g", "g", 54, F.ACEL), ("entra", "i", 54, TINTA2), ("com", "i", 54, TINTA2), ("−", "g", 60, F.ACEL)],
            XE, 220, passo=0.1)
    E.formula_em(c, t, C["s05.a"], "v = v₀ − g · t", XE, 360, 84, "g", TINTA)
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.pilula(c, "no alto: v = 0", XE + 210, 460, 42, "b", fundo=F.VEL, a=a))
    E.formula_em(c, t, C["s05.c"], "g · t = v₀", XE, 600, 84, "g", TINTA)
    F.formula_legenda(c, t, C["s05.d"], "t = f{v₀}{g}", [("t", "tempo de subida", "s")], XE, 790, 96, tl=[C["s05.d"] + 0.6])
    E.foco(c, t, C["s05.e"], 0.5, lambda a: E.formula(c, "f{20}{10} =", XE + 430, 790, 76, "g", TINTA2, a))
    bola_txt(c, t, C["s05.e"] + 0.6, "2 s", XE + 800, 760, 90, 60)


# ---------------- altura máxima ----------------
def b_altura(c, t, C, b):
    def s06():
        E.frase(c, t, C["s06.a"], [("Torricelli", "g", 76, COR), ("com", "i", 76), ("v = 0", "g", 76, F.VEL)], XE, 260, passo=0.12)
        E.formula_em(c, t, C["s06.b"], "0 = v₀^2 − 2 · g · H", XE, 420, 84, "g", TINTA)
        F.formula_legenda(c, t, C["s06.c"], "H = f{v₀^2}{2 · g}", [("H", "altura máxima", "m"), ("v₀", "velocidade de saída", "m/s")],
                          XE, 620, 100, tl=[C["s06.c"] + 0.8, C["s06.c"] + 1.4])
        E.foco(c, t, C["s06.d"], 0.5, lambda a: E.formula(c, "f{400}{20} =", 1150, 620, 84, "g", TINTA2, a))
        bola_txt(c, t, C["s06.e"], "20 m", 1600, 590, 110, 64)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    P = F.grafico(c, t, C["s07"], 900, 230, 820, 560, 0, 4.5, 0, 25, "t (s)", "s (m)", 1, 5)
    E.curva(c, t, C["s07.a"], P, lambda x: 20 * x - 5 * x * x, 0, 4, d=1.2, cor=E.COR, largura=8)
    E.ponto(c, t, C["s07.b"], P, 2, 20, None, guias=True)
    E.foco(c, t, C["s07.b"] + 0.5, 0.4, lambda a: E.pilula(c, "vértice: 2 s, 20 m", P.x(2), P.y(20) - 70, 40, "b", fundo=E.COR, a=a))
    E.frase(c, t, C["s07"], ps("altura em cada instante:", "i", 62), XE, 330, passo=0.1)
    E.frase(c, t, C["s07.a"], [("parábola", "g", 80, COR)], XE, 460)
    E.frase(c, t, C["s07.a"] + 0.6, ps("virada para baixo", "i", 62), XE, 550, passo=0.1)
    E.frase(c, t, C["s07.b"], [("vértice", "g", 70), ("=", "g", 70, TINTA2)], XE, 720, passo=0.12)
    E.frase(c, t, C["s07.b"] + 0.5, ps("o ponto mais alto", "i", 62), XE, 810, passo=0.1)


# ---------------- simetria ----------------
def b_simetria(c, t, C, b):
    yb, k = 930, 30.0
    yv = lambda h: yb - 30 - h * k
    xs, xd = 1150, 1560
    chao_em(c, t, C["s08"], 960, 1820, yb)
    sobe = [(C["s08"] + 0.2, 0, "0 s", 20), (C["s08"] + 0.6, 15, "1 s", 10), (C["s08"] + 1.0, 20, "2 s", 0)]
    desce = [(C["s08.b"], 20, "2 s", 0), (C["s08.b"] + 0.5, 15, "3 s", -10), (C["s08.b"] + 1.0, 0, "4 s", -20)]
    fotos_bola(c, t, xs, yv, sobe, lado=-1)
    fotos_bola(c, t, xd, yv, desce, lado=1)
    E.foco(c, t, C["s08"] + 0.2, 0.4, lambda a: centro(c, "sobe", xs, yb + 80, 50, "i", TINTA2, a))
    E.foco(c, t, C["s08.b"], 0.4, lambda a: centro(c, "desce", xd, yb + 80, 50, "i", TINTA2, a))
    E.frase(c, t, C["s08.a"], ps("a descida é uma", "i", 62) + [("queda livre", "g", 62, COR)], XE, 240, passo=0.1)
    E.frase(c, t, C["s08.c"], [("mesmo", "g", 70), ("tempo:", "g", 70)], XE, 400, passo=0.12)
    E.foco(c, t, C["s08.c"] + 0.4, 0.4, lambda a: E.escreve(c, "2 s para subir", XE, 490, 54, "i", TINTA, a))
    E.foco(c, t, C["s08.c"] + 0.8, 0.4, lambda a: E.escreve(c, "2 s para descer", XE, 560, 54, "i", TINTA, a))
    if t < C["s09"]:
        return
    E.formula_em(c, t, C["s09.a"], "voo = 2 · 2 =", XE, 720, 72, "g", TINTA)
    bola_txt(c, t, C["s09.b"], "4 s", XE + 570, 700, 80, 56)
    E.frase(c, t, C["s09.c"], [("volta", "i", 56), ("com", "i", 56), ("20 m/s", "g", 56, F.VEL)], XE, 870, passo=0.1)
    E.frase(c, t, C["s09.d"], [("para", "i", 56), ("baixo", "g", 56, F.VEL)], XE + 480, 870, passo=0.1)
    if t >= C["s09.e"]:  # mesma altura, mesma velocidade
        q = ep(t, C["s09.e"], 0.4)
        M.line(c, xs - 120, yv(15) + 40, xd + 260, yv(15) + 40, E.COR, q, 4, dash=E.TRACO)
        E.frase(c, t, C["s09.e"] + 0.3, ps("mesma altura, mesmo módulo", "g", 46, COR), XE, 970, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    x, y = 1450, 330
    E.foco(c, t, C["s10.a"], 0.5, lambda a: E.bola(c, x, y, 50, a=a))
    E.frase(c, t, C["s10.a"], ps("no ponto mais alto,", "i", 66), XE, 360, passo=0.1)
    E.foco(c, t, C["s10.a"] + 1.0, 0.5, lambda a: E.escreve(c, "a = 0 ?", XE, 500, 110, "g", ERRADO, a))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: (E.escreve(c, "v = 0", XE, 680, 90, "g", CERTO, a), E.selo(c, XE + 400, 650, 44, True, a)))
    if t >= C["s10.c"]:
        E.risco(c, XE - 10, 520, XE + 400, 420, t, C["s10.c"], largura=12)
        F.seta(c, x, y + 70, x, y + 330, F.ACEL, ep(t, C["s10.c"], 0.3), 12, p=ease_io(prog(t, C["s10.c"], 0.5)))
        E.foco(c, t, C["s10.c"] + 0.4, 0.4, lambda a: F.medida(c, 10, "m/s^2", x + 40, y + 260, 60, F.ACEL, a))
        E.foco(c, t, C["s10.c"] + 0.4, 0.4, lambda a: E.escreve(c, "para baixo", x + 40, y + 330, 48, "i", TINTA2, a))
    E.frase(c, t, C["s10.d"], ps("se fosse zero,", "i", 58) + [("ficaria", "g", 58), ("parada", "g", 58, ERRADO)], XE, 870, passo=0.1)
    E.frase(c, t, C["s10.d"] + 1.2, ps("lá em cima para sempre", "i", 58), XE, 960, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s11():
        E.frase(c, t, C["s11"], ps("o atalho:", "i", 76, CLARO), W / 2, 170, "center")
        E.frase(c, t, C["s11.a"], ps("a subida é a", "i", 70, CLARO) + [("queda", "g", 70, BR), ("ao", "i", 70, CLARO), ("contrário", "g", 70, BR)],
                W / 2, 300, "center", 0.12)
        for i, (k, nome, f_) in enumerate((("s11.b", "subida", "t = f{v₀}{10}"), ("s11.c", "altura", "H = 5 · t^2"), ("s11.d", "voo", "2 · t"))):
            y = 520 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, y=y, nome=nome, f_=f_, i=i: (E.bola(c, 520, y - 30, 50, a=a), centro(c, str(i + 1), 520, y - 6, 56, "g", BR, a),
                                                                           E.escreve(c, nome, 620, y, 66, "i", CLARO, a),
                                                                           E.formula(c, f_, 1000, y, 80, "g", BR, a)))
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"], [("v₀ = 20 m/s:", "g", 66, BR)], W / 2, 200, "center")
    for i, (k, s) in enumerate((("s12.a", "2 s"), ("s12.b", "5 · 2² = 20 m"), ("s12.c", "4 s no ar"))):
        E.foco(c, t, C[k], 0.4, lambda a, i=i, s=s: centro(c, s, 380 + i * 580, 360, 70, "g", E.CLARO, a))
    E.frase(c, t, C["s12.d"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("não volta à altura de saída", "i", 66, CLARO),
            W / 2, 560, "center", 0.1)
    # prédio: sobe e cai até a calçada
    if t >= C["s12.d"] + 0.8:
        q = ep(t, C["s12.d"] + 0.8, 0.5)
        M.rrect(c, 700, 800, 220, 250, 6, "#3A3A48", q)
        M.line(c, 500, 1050, 1500, 1050, CLARO, q, 4)
        pts = [(810 + 110 * u, 780 - 200 * u + 100 * u * u) for u in [i / 40 * 2.92 for i in range(41)]]
        F.poli(c, pts, ease_io(prog(t, C["s12.d"] + 1.0, 1.4)), E.CLARO, q, 5, dash=E.TRACO)
        E.foco(c, t, C["s12.d"] + 1.0, 0.4, lambda a: E.bola(c, 810, 780, 22, a=a))
    E.frase(c, t, C["s12.e"], [("a", "i", 60, CLARO), ("descida", "g", 60, BR), ("demora", "i", 60, CLARO), ("mais", "g", 60, BR)], 1250, 820, "left", 0.1)
    E.frase(c, t, C["s12.e"] + 1.0, [("voo", "i", 60, CLARO), ("≠", "g", 60, ERRADO), ("dobro", "g", 60, BR)], 1250, 920, "left", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s13.a"], ps("uma pedra lançada", "i", 76), XE, 340, passo=0.12)
    E.frase(c, t, C["s13.a"] + 0.9, [("para", "i", 76), ("cima", "g", 76)], XE, 440, passo=0.12)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: F.medida(c, 30, "m/s", XE, 570, 110, F.VEL, a))
    E.frase(c, t, C["s13.b"] + 0.9, ps("sem resistência do ar", "i", 52, TINTA2), XE, 650, passo=0.1)
    E.frase(c, t, C["s13.c"], [("altura", "g", 72), ("máxima?", "g", 72, COR)], XE, 800, passo=0.12)
    E.frase(c, t, C["s13.d"], [("tempo", "g", 72), ("até", "i", 76), ("voltar?", "g", 72, COR)], XE, 910, passo=0.12)
    if t < C["s14"]:
        x, yb = 1450, 900
        E.foco(c, t, C["s13.a"], 0.5, lambda a: mao(c, x, yb + 20, 1.0, a))
        E.foco(c, t, C["s13.a"] + 0.3, 0.4, lambda a: E.bola(c, x, yb - 20, 34, a=a))
        F.vetor(c, t, C["s13.b"], (x + 90, yb - 40), (x + 90, yb - 400), "v₀", "30 m/s", F.VEL, 10)
    else:
        E.relogio(c, t, C["s14.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s15.a"], [("subida:", "i", 66)], XE, 260)
    E.formula_em(c, t, C["s15.a"] + 0.4, "t = f{30}{10} =", XE + 280, 260, 80, "g", TINTA)
    bola_txt(c, t, C["s15.b"], "3 s", XE + 860, 235, 80, 56)
    E.frase(c, t, C["s15.c"], [("altura:", "i", 66)], XE, 470)
    E.formula_em(c, t, C["s15.c"] + 0.4, "H = 5 · 3^2 = 5 · 9 =", XE + 280, 470, 80, "g", TINTA)
    bola_txt(c, t, C["s15.d"], "45 m", XE + 1180, 445, 95, 56)
    E.formula_em(c, t, C["s16.a"], "Torricelli: f{900}{20} = 45", XE + 280, 640, 60, "g", CERTO)
    E.frase(c, t, C["s16.b"], [("voo:", "i", 66)], XE, 840)
    E.formula_em(c, t, C["s16.b"] + 0.4, "2 · 3 =", XE + 280, 840, 80, "g", TINTA)
    bola_txt(c, t, C["s16.c"], "6 s", XE + 680, 815, 90, 60)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = (("s17.a", [("subida:", "i", 66), ("t", "g", 66), ("=", "g", 66), ("v₀ ÷ g", "g", 66, COR)]),
             ("s17.b", [("altura:", "i", 66), ("H", "g", 66), ("=", "g", 66), ("v₀² ÷ 2g", "g", 66, COR)]),
             ("s17.c", [("descida", "i", 66), ("=", "g", 66), ("mesmo", "g", 66, COR), ("tempo", "g", 66, COR)]))

    def desenho():  # bola que sai da mesa na horizontal
        if t >= C["s18.a"]:
            q = ep(t, C["s18.a"], 0.4)
            M.rrect(c, 200, 700, 300, 30, 6, "#8B5E3C", q)
            M.rrect(c, 220, 730, 26, 250, 4, "#6E4A2F", q)
            M.line(c, 150, 980, 1100, 980, TINTA, q, 4)
            pts = [(500 + 500 * u, 670 + 300 * u * u) for u in [i / 50 for i in range(51)]]
            F.poli(c, pts, ease_io(prog(t, C["s18.b"], 1.0)), E.COR, q, 6, dash=E.TRACO)
            E.bola(c, 480, 670, 28, a=q)
    fim(c, t, C, "s17", itens, "s18", [("s18.b", [("Lançamento", "g", 110, COR)]), ("s18.b", [("horizontal", "g", 110, COR)])],
        desenho, "s18.c", "s18.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, subida=b_subida, altura=b_altura, simetria=b_simetria, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
