"""Visual — Estudativo · FIS-CIN-013: queda livre.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001/roteiro/visual.py (peças em _ferramentas/fisica.py, F).
Nesta aula: o corpo que cai é a esfera laranja; a régua de queda (posições a cada segundo, foto estroboscópica) fica em
tinta com a altura em cinza-tinta; velocidade em petróleo (F.VEL), aceleração g em violeta (F.ACEL).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-013_queda_livre.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("conceito", "velocidade", "altura", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert [10 * t for t in (1, 2, 3)] == [10, 20, 30] and [5 * t * t for t in (1, 2, 3, 4, 5)] == [5, 20, 45, 80, 125]
assert math.sqrt(80 / 5) == 4 and 10 * 4 == 40 and math.sqrt(2 * 10 * 80) == 40 and 2 * 10 * 80 == 1600
assert 80 / 10 == 8 and abs(math.sqrt(8) - 2.83) < 0.01 and abs(math.sqrt(60 / 5) - 3.46) < 0.01
assert math.sqrt(45 / 5) == 3 and 10 * 3 == 30 and 30 * 3.6 == 108


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
def martelo(c, x, y, s, a=1.0):
    """martelo em pé: cabo de x, y (ponta de cima) até y + 1,6·s"""
    if a <= 0:
        return
    M.rrect(c, x - s * 0.08, y, s * 0.16, s * 1.6, 6, "#8B5E3C", a)
    M.rrect(c, x - s * 0.5, y - s * 0.12, s * 1.0, s * 0.34, 8, "#55555F", a)


def pena(c, x, y, s, a=1.0):
    """pena: oval clara com a haste no meio; (x, y) = ponta de cima"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x, y); p.cubicTo(x + s * 0.55, y + s * 0.3, x + s * 0.45, y + s * 1.2, x, y + s * 1.5)
    p.cubicTo(x - s * 0.45, y + s * 1.2, x - s * 0.55, y + s * 0.3, x, y); p.close()
    c.drawPath(p, M.paint("#E8E2D4", a))
    c.drawPath(p, M.paint(TINTA2, a * 0.6, stroke=3))
    M.line(c, x, y + s * 0.05, x, y + s * 1.8, TINTA2, a, 4)


def predio(c, x, yb, w, h, a=1.0, rotulo=None):
    """prédio de base em yb, canto esquerdo em x"""
    if a <= 0:
        return
    M.rrect(c, x, yb - h, w, h, 6, "#C9C4BA", a)
    nj = max(1, int(h // 80))
    for i in range(nj):
        for j in range(2):
            M.rrect(c, x + w * (0.18 + 0.42 * j), yb - h + 26 + i * (h - 40) / nj, w * 0.24, (h - 40) / nj * 0.55, 4, "#8FA9C2", a)
    F.chao(c, x - 140, x + w + 360, yb, a)


def regua(c, t, t0, x, ytop, k, marcas, cor=None):
    """régua vertical de queda: marcas = alturas caídas (m); k = pixels por metro. Devolve y(h)"""
    yv = lambda h: ytop + h * k
    if t >= t0:
        M.line(c, x, ytop, x, lerp(ytop, yv(marcas[-1]) + 20, ease_io(prog(t, t0, 0.6))), TINTA2, 1.0, 4, dash=E.TRACO)
    for i, h in enumerate(marcas):
        E.foco(c, t, t0 + 0.2 + 0.06 * i, 0.4, lambda a, h=h: (M.line(c, x - 14, yv(h), x + 14, yv(h), TINTA2, a, 4),
                                                              F.medida(c, h, "m", x - 30, yv(h) + 16, 44, TINTA2, a, "right")))
    return yv


def queda(c, t, x, yv, fotos, r=34, cor=None):
    """foto estroboscópica: fotos = [(instante, h caída, rótulo do tempo, rótulo da velocidade ou None)]; a última fica forte"""
    for i, (ti, h, rot_t, rot_v) in enumerate(fotos):
        q = ep(t, ti, 0.4)
        if q <= 0:
            continue
        ultima = i == len(fotos) - 1 or t < fotos[i + 1][0]
        E.bola(c, x, yv(h), r, cor, q * (1.0 if ultima else 0.3))
        if rot_t:
            E.foco(c, t, ti + 0.1, 0.3, lambda a, h=h, s=rot_t: E.pilula(c, s, x + r + 70, yv(h), 36, "b", fundo=TINTA, a=a))
        if rot_v:
            E.foco(c, t, ti + 0.2, 0.3, lambda a, h=h, s=rot_v: F.medida(c, *s.split(" "), x + r + 150, yv(h) + 14, 46, F.VEL, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        yc = 840
        q = ep(t, C["s01.a"] - 0.5, 0.5)
        if q > 0:
            c.drawRect(skia.Rect.MakeXYWH(900, yc, 960, 200), M.paint("#B9B6B0", q))
            for cx, cy, r in ((1100, 900, 40), (1500, 960, 26), (1740, 890, 34)):
                c.drawOval(skia.Rect.MakeXYWH(cx - r, cy - r * 0.4, 2 * r, r * 0.8), M.paint("#8D8A84", q))
        # os dois sobem até o alto e caem juntos a partir de s01.b + 0.6
        tq = C["s01.b"] + 0.6
        f = ease_io(prog(t, tq, max(0.6, C["s01.c"] - tq)))
        dy = lerp(0, 430, f * f)
        E.foco(c, t, C["s01.a"], 0.5, lambda a: martelo(c, 1180, 300 + dy, 120, a))
        E.foco(c, t, C["s01.b"], 0.5, lambda a: pena(c, 1560, 330 + dy, 110, a))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "chegaram juntos", 1380, 200, 52, "g", fundo=CERTO, a=a))
        E.frase(c, t, C["s01"], [("1971,", "g", 120, TINTA)], XE, 330)
        E.frase(c, t, C["s01"] + 0.8, ps("na", "i", 90) + [("Lua", "g", 90, COR)], XE, 460, passo=0.12)
        E.frase(c, t, C["s01.a"], [("martelo", "g", 70), ("e", "i", 74), ("pena", "g", 70)], XE, 600, passo=0.4)
        E.frase(c, t, C["s01.d"] - 1.4, ps("sem ar:", "i", 70, TINTA2), XE, 760, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("tudo cai", "g", 70, COR) + ps("do mesmo jeito", "i", 74), XE, 860, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "o tempo de queda"), ("s02.c", "a velocidade final")))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.a", "velocidade:", "v = v₀ + a · t", None),
                              ("s03.b", "posição:", "s = s₀ + v₀ · t + a · t² ÷ 2", None)), num="2", titulo=("fórmulas",))


# ---------------- o que é ----------------
def b_conceito(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], [("queda", "g", 110, COR), ("livre", "g", 110, COR)], XE, 260, passo=0.2)
        for i, (k, s) in enumerate((("s04.a", "só a gravidade"), ("s04.b", "a partir do repouso"), ("s04.c", "sem resistência do ar"))):
            y = 440 + i * 130
            E.foco(c, t, C[k], 0.5, lambda a, y=y: E.bola(c, XE + 30, y - 22, 26, a=a))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 66)], XE + 80, y)
        E.foco(c, t, C["s04"] + 0.5, 0.5, lambda a: E.bola(c, 1500, 360, 70, a=a))
        if t >= C["s04.a"]:
            F.seta(c, 1500, 470, 1500, 720, F.ACEL, ep(t, C["s04.a"], 0.3), 12, p=ease_io(prog(t, C["s04.a"], 0.6)))
            E.foco(c, t, C["s04.a"] + 0.5, 0.4, lambda a: E.escreve(c, "g", 1540, 640, 80, "g", F.ACEL, a))
        E.foco(c, t, C["s04.d"], 0.5, lambda a: E.pilula(c, "“despreze a resistência do ar”", W / 2, 920, 52, "i", fundo=TINTA, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], ps("perto do chão, todo corpo:", "i", 72), XE, 260, passo=0.12)
    E.frase(c, t, C["s05"] + 1.4, ps("a mesma aceleração", "g", 72), XE, 370, passo=0.12)
    E.foco(c, t, C["s05.a"], 0.6, lambda a: E.escreve(c, "g", XE, 700, 300, "g", F.ACEL, a))
    E.foco(c, t, C["s05.b"], 0.5, lambda a: (E.escreve(c, "≈", XE + 260, 640, 90, "g", TINTA2, a),
                                             F.medida(c, "9,8", "m/s^2", XE + 360, 640, 90, TINTA2, a)))
    E.frase(c, t, lerp(C["s05.b"], C["s05.c"], 0.5), [("na", "i", 66), ("prova:", "i", 66)], 1100, 560, passo=0.12)
    bola_txt(c, t, C["s05.c"] - 0.1, "10 m/s^2", 1500, 720, 170, 76, F.ACEL)


# ---------------- velocidade ----------------
def b_velocidade(c, t, C, b):
    x, ytop, k = 1300, 230, 15.0
    yv = regua(c, t, C["s06"], x - 90, ytop, k, [0, 5, 20, 45])
    queda(c, t, x, yv, [(C["s06"] + 0.3, 0, "0 s", "0 m/s"), (C["s06.b"], 5, "1 s", "10 m/s"),
                         (C["s06.c"], 20, "2 s", "20 m/s"), (C["s06.d"], 45, "3 s", "30 m/s")])
    E.frase(c, t, C["s06.a"], ps("a cada segundo", "i", 70), XE, 280, passo=0.12)
    E.frase(c, t, C["s06.a"] + 0.9, [("+10 m/s", "g", 84, F.VEL)], XE, 400)
    if t < C["s07"]:
        return
    E.formula_em(c, t, C["s07"] + 0.2, "v = v₀ + a · t", XE, 580, 76, "g", TINTA)
    E.foco(c, t, C["s07.a"], 0.4, lambda a: E.pilula(c, "v₀ = 0", XE + 140, 680, 44, "b", fundo=TINTA2, a=a))
    E.foco(c, t, C["s07.b"], 0.4, lambda a: E.pilula(c, "a = g", XE + 420, 680, 44, "b", fundo=F.ACEL, a=a))
    E.formula_em(c, t, C["s07.c"], "v = g · t", XE, 830, 96, "g", TINTA)
    E.foco(c, t, C["s07.d"], 0.5, lambda a: E.pilula(c, "v = 10 · t", XE + 600, 800, 64, "g", fundo=E.COR, a=a))


# ---------------- altura ----------------
def b_altura(c, t, C, b):
    def s08():
        E.formula_em(c, t, C["s08"] + 0.6, "s = s₀ + v₀ · t + f{a · t^2}{2}", XE, 300, 80, "g", TINTA2)
        if t >= C["s08.a"] + 0.6:
            E.risco(c, XE + 225, 300, XE + 470, 255, t, C["s08.a"] + 0.6, cor=TINTA2, largura=8)
        E.frase(c, t, C["s08.a"], ps("sai do repouso:", "i", 50, TINTA2) + [("v₀ = 0", "g", 48, TINTA2)], XE + 900, 300, passo=0.1)
        E.formula_em(c, t, C["s08.b"], "h = f{a · t^2}{2}", XE, 520, 90, "g", TINTA)
        E.formula_em(c, t, C["s08.c"], "f{10}{2} = 5", XE + 560, 520, 90, "g", F.ACEL)
        F.formula_legenda(c, t, C["s08.d"], "h = 5 · t^2", [("h", "altura da queda", "m"), ("t", "tempo", "s")], XE, 760, 120,
                          tl=[C["s08.e"], C["s08.e"] + 0.9])
        if t >= C["s08.d"]:
            E.foco(c, t, C["s08.d"] + 0.3, 0.4, lambda a: E.pilula(c, "o atalho da queda", 1360, 730, 50, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    x, ytop, k = 1250, 200, 9.0
    yv = regua(c, t, C["s09"], x - 90, ytop, k, [0, 5, 20, 45, 80])
    fotos = [(C["s09"] + 0.3, 0, "0 s", None), (C["s09.a"], 5, "1 s", None), (C["s09.b"], 20, "2 s", None),
             (C["s09.c"], 45, "3 s", None), (C["s09.d"], 80, "4 s", None)]
    queda(c, t, x, yv, fotos, r=28)
    E.frase(c, t, C["s09"], [("h", "g", 80, COR), ("=", "g", 80, TINTA2), ("5 · t²", "g", 80)], XE, 260, passo=0.12)
    for i, (kk, s) in enumerate((("s09.a", "1 s → 5 m"), ("s09.b", "2 s → 20 m"), ("s09.c", "3 s → 45 m"), ("s09.d", "4 s → 80 m"))):
        E.foco(c, t, C[kk], 0.4, lambda a, i=i, s=s: E.escreve(c, s, XE, 400 + i * 100, 64, "g", TINTA, a))
    # cada segundo cobre mais metros: 5, 15, 25, 35
    for i, (h0, h1) in enumerate(((0, 5), (5, 20), (20, 45), (45, 80))):
        ti = C["s09.e"] + 0.5 * i
        q = ep(t, ti, 0.4)
        if q > 0:
            xx = x + 260
            M.line(c, xx, yv(h0) + 6, xx, yv(h1) - 6, E.COR, q, 8)
            M.line(c, xx - 14, yv(h1) - 6, xx + 14, yv(h1) - 6, E.COR, q, 6)
            F.medida(c, h1 - h0, "m", xx + 30, (yv(h0) + yv(h1)) / 2 + 16, 46, COR, q)
    E.frase(c, t, C["s09.e"] + 0.2, ps("cada segundo cobre", "i", 54) + [("mais", "g", 54, COR)], XE, 880, passo=0.1)


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    yb = 900
    E.foco(c, t, C["s10"], 0.6, lambda a: predio(c, 1420, yb, 240, 560, a))
    E.foco(c, t, C["s10.a"], 0.5, lambda a: F.medida(c, 80, "m", 1380, yb - 270, 70, COR, a, "right"))
    if t >= C["s10.a"]:
        q = ep(t, C["s10.a"], 0.5)
        M.line(c, 1400, yb - 560, 1400, yb, TINTA2, q, 4, dash=E.TRACO)
    q = ease_io(prog(t, C["s11.a"], 1.0))
    E.foco(c, t, C["s10"] + 0.4, 0.4, lambda a: E.bola(c, 1540, lerp(yb - 600, yb - 40, q * q), 36, a=a))

    def s10():
        E.frase(c, t, C["s10"], ps("cai de", "i", 76) + [("80 m", "g", 76, COR)], XE, 250, passo=0.12)
        E.formula_em(c, t, C["s10.b"], "80 = 5 · t^2", XE, 420, 96, "g", TINTA)
        E.formula_em(c, t, C["s10.c"], "t^2 = 16", XE, 580, 96, "g", TINTA)
        E.foco(c, t, C["s10.c"] - 0.2, 0.4, lambda a: E.escreve(c, "÷ 5", XE + 500, 580, 60, "i", TINTA2, a))
        E.formula_em(c, t, C["s10.d"], "t = r{16} =", XE, 760, 96, "g", TINTA)
        bola_txt(c, t, C["s10.d"] + 0.6, "4 s", XE + 650, 730, 100, 66)
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11"], ps("velocidade de chegada", "i", 70), XE, 250, passo=0.12)
    E.formula_em(c, t, C["s11.a"], "v = 10 · 4 =", XE, 420, 90, "g", TINTA)
    bola_txt(c, t, C["s11.b"], "40 m/s", XE + 760, 395, 120, 60, F.VEL)
    E.frase(c, t, C["s11.c"], [("Torricelli", "g", 60, COR)] + ps("sem o tempo:", "i", 60, TINTA2), XE, 620, passo=0.12)
    E.formula_em(c, t, C["s11.c"] + 0.8, "v^2 = 2 · 10 · 80 = 1600", XE, 740, 76, "g", TINTA)
    E.formula_em(c, t, C["s11.d"], "v = r{1600} = 40", XE, 880, 76, "g", CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s12.a"], ps("esquecer o", "i", 76) + [("÷ 2", "g", 76, ERRADO)], XE + 500, 210, passo=0.12)
    E.formula_em(c, t, C["s12.b"], "80 = 10 · t^2", XE, 420, 96, "g", ERRADO)
    E.formula_em(c, t, C["s12.b"] + 1.6, "t^2 = 8", XE, 560, 96, "g", ERRADO)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.escreve(c, "t ≈ 2,8 s", XE, 720, 96, "g", ERRADO, a))
    if t >= C["s12.d"]:
        E.risco(c, XE - 10, 740, XE + 450, 640, t, C["s12.d"], largura=12)
    E.foco(c, t, C["s12.d"] + 0.4, 0.5, lambda a: E.selo(c, XE + 560, 680, 50, False, a))
    E.formula_em(c, t, C["s12.d"] + 0.6, "80 = 5 · t^2 → t = 4 s", 1000, 560, 76, "g", CERTO)
    E.frase(c, t, C["s12.e"], ps("use direto o", "i", 70) + [("5", "g", 90, COR)], 1000, 760, passo=0.12)
    E.frase(c, t, C["s12.e"] + 1.0, ps("ele já é", "i", 60, TINTA2) + [("10 ÷ 2", "g", 60, TINTA2)], 1000, 870, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("o atalho:", "i", 76, CLARO) + [("a tabela da queda", "g", 76, BR)], W / 2, 170, "center", 0.12)
        E.foco(c, t, C["s13.a"], 0.4, lambda a: (centro(c, "t (s)", 640, 320, 56, "b", CLARO, a), centro(c, "h (m)", 1280, 320, 56, "b", CLARO, a),
                                                 M.line(c, 470, 345, 1450, 345, CLARO, a, 3)))
        for i, (k, tt, h) in enumerate((("s13.b", 1, 5), ("s13.c", 2, 20), ("s13.d", 3, 45), ("s13.e", 4, 80), ("s13.f", 5, 125))):
            y = 440 + i * 105
            E.foco(c, t, C[k], 0.4, lambda a, y=y, tt=tt, h=h: (centro(c, str(tt), 640, y, 76, "g", BR, a),
                                                              centro(c, str(h), 1280, y, 76, "g", E.CLARO, a)))
            E.foco(c, t, lerp(C["s13.f"], C["s14"], 0.55) + 0.15 * i, 0.4,
                   lambda a, y=y, tt=tt: E.escreve(c, f"= 5 × {tt * tt}", 1460, y, 52, "i", CLARO, a))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], [("2×", "g", 96, BR), ("o", "i", 90, CLARO), ("tempo", "i", 90, CLARO), ("→", "g", 90, CLARO), ("4×", "g", 96, BR),
                               ("a", "i", 90, CLARO), ("altura", "i", 90, CLARO)], W / 2, 300, "center", 0.12)
    E.foco(c, t, C["s14.a"] + 1.2, 0.5, lambda a: centro(c, "2 s → 20 m      4 s → 80 m", W / 2, 420, 60, "b", CLARO, a))
    E.frase(c, t, C["s14.b"], [("não", "g", 64, ERRADO), ("compensa:", "i", 66, CLARO), ("60 m", "g", 66, BR), ("não", "i", 66, CLARO),
                               ("está", "i", 66, CLARO), ("na", "i", 66, CLARO), ("tabela", "i", 66, CLARO)], W / 2, 640, "center", 0.1)
    E.formula_em(c, t, C["s14.c"], "f{60}{5} = 12 → t = r{12} ≈ 3,5 s", W / 2, 840, 84, "g", BR, "center")


# ---------------- questão ----------------
def vaso(c, x, y, s, a=1.0):
    """vaso com planta; (x, y) = centro da boca"""
    if a <= 0:
        return
    for g in (-40, 0, 40):
        r = math.radians(-90 + g)
        c.drawOval(skia.Rect.MakeXYWH(x + math.cos(r) * s * 0.4 - s * 0.16, y + math.sin(r) * s * 0.4 - s * 0.3, s * 0.32, s * 0.6), M.paint("#3F8F4A", a))
    p = skia.Path()
    p.moveTo(x - s * 0.5, y); p.lineTo(x + s * 0.5, y); p.lineTo(x + s * 0.35, y + s * 0.7); p.lineTo(x - s * 0.35, y + s * 0.7); p.close()
    c.drawPath(p, M.paint("#B5562A", a))


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], ps("um vaso cai de", "i", 76), XE, 340, passo=0.12)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: F.medida(c, 45, "m", XE, 470, 110, COR, a))
    E.frase(c, t, C["s15.b"] + 1.0, ps("sem resistência do ar", "i", 52, TINTA2), XE, 560, passo=0.1)
    E.frase(c, t, C["s15.c"], [("tempo", "g", 76), ("de", "i", 80), ("queda?", "g", 76, COR)], XE, 720, passo=0.12)
    E.frase(c, t, C["s15.d"], [("velocidade", "g", 76), ("de", "i", 80), ("chegada?", "g", 76, COR)], XE, 840, passo=0.12)
    if t < C["s16"]:
        yb = 940
        E.foco(c, t, C["s15.a"], 0.6, lambda a: predio(c, 1400, yb, 260, 640, a))
        E.foco(c, t, C["s15.a"] + 0.3, 0.5, lambda a: vaso(c, 1530, yb - 690, 70, a))
    else:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s17.a"], "45 = 5 · t^2", XE, 300, 96, "g", TINTA)
    E.formula_em(c, t, C["s17.b"], "t^2 = 9", XE, 450, 96, "g", TINTA)
    bola_txt(c, t, C["s17.c"], "3 s", XE + 620, 400, 110, 70)
    E.frase(c, t, lerp(C["s17.c"], C["s17.end"], 0.5), [("tabela:", "i", 56, TINTA2), ("3 s → 45 m", "g", 52, TINTA2)], XE, 580, passo=0.1)
    yv = regua(c, t, C["s17"], 1560, 200, 13.0, [0, 5, 20, 45])
    queda(c, t, 1650, yv, [(C["s17"] + 0.3, 0, "0 s", None), (C["s17.a"] + 0.6, 5, "1 s", None), (C["s17.b"], 20, "2 s", None),
                          (C["s17.c"], 45, "3 s", None)], r=30)
    E.formula_em(c, t, C["s18.a"], "v = 10 · 3 =", XE, 800, 96, "g", TINTA)
    bola_txt(c, t, C["s18.b"], "30 m/s", XE + 860, 770, 130, 64, F.VEL)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "= 108 km/h", XE + 860, 960, 56, "g", fundo=TINTA, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = (("s19.a", [("sem", "i", 70), ("ar:", "i", 70), ("g = 10 m/s²", "g", 66, F.ACEL), ("para", "i", 70), ("todos", "i", 70)]),
             ("s19.b", [("v", "g", 70, F.VEL), ("=", "g", 70), ("10 · t", "g", 70)]),
             ("s19.c", [("h", "g", 70, COR), ("=", "g", 70), ("5 · t²", "g", 70)]))

    def desenho():  # bola jogada para cima
        F.vetor(c, t, C["s20.a"] + 0.3, (420, 940), (420, 640), "v", None, F.VEL, 10)
        E.foco(c, t, C["s20.a"], 0.4, lambda a: E.bola(c, 420, lerp(940, 620, ease_out(prog(t, C["s20.a"], 1.2))), 40, a=a))
        E.frase(c, t, C["s20.b"], [("altura", "i", 60), ("máxima", "g", 60, COR)], 560, 760, passo=0.12)
        E.frase(c, t, C["s20.c"], [("tempo", "i", 60), ("no", "i", 60), ("ar", "g", 60, COR)], 560, 870, passo=0.12)
    fim(c, t, C, "s19", itens, "s20", [("s20.a", [("Lançamento", "g", 110, COR)]), ("s20.a", [("para cima", "g", 110, COR)])],
        desenho, "s20.d", "s20.e")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, conceito=b_conceito, velocidade=b_velocidade, altura=b_altura, exemplo=b_exemplo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
