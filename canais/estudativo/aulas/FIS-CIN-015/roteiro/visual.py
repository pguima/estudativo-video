"""Visual — Estudativo · FIS-CIN-015: lançamento horizontal.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001/roteiro/visual.py (peças em _ferramentas/fisica.py, F).
Nesta aula: a trajetória é tracejada em laranja; as fotos da bola a cada segundo têm "sombras" nas duas direções — no alto,
a sombra horizontal (passos iguais, movimento uniforme, em petróleo F.VEL) e, à esquerda, a sombra vertical (passos que
crescem, queda livre, em violeta F.ACEL). Sem vetores somados: a aula não usa soma de vetores (FIS-CIN-002 ainda não veio).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-015_lancamento_horizontal.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("dois", "metodo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert math.sqrt(20 / 5) == 2 and 15 * 2 == 30 and [15 * t for t in (0, 1, 2)] == [0, 15, 30] and [5 * t * t for t in (0, 1, 2)] == [0, 5, 20]
assert 500 / 5 == 100 and math.sqrt(100) == 10 and 100 * 10 == 1000 and 30 * 2 == 60
assert 1.25 / 5 == 0.25 and math.sqrt(0.25) == 0.5 and 2 * 0.5 == 1


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
def mesa(c, x, ytop, w, h, a=1.0, cor="#8B5E3C", escuro=False):
    """mesa (ou penhasco) com o tampo em ytop, borda direita em x + w, pé até ytop + h"""
    if a <= 0:
        return
    M.rrect(c, x, ytop, w, 28, 6, cor, a)
    M.rrect(c, x + 20, ytop + 26, 26, h - 26, 4, E.mix(cor, "#000000", 0.2), a)
    M.rrect(c, x + w - 46, ytop + 26, 26, h - 26, 4, E.mix(cor, "#000000", 0.2), a)


def penhasco(c, x, ytop, ybase, a=1.0):
    """penhasco: bloco de pedra à esquerda de x, do topo ytop até o chão ybase"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x - 360, ybase); p.lineTo(x - 360, ytop); p.lineTo(x, ytop); p.lineTo(x + 20, ytop + 60); p.lineTo(x - 10, ybase); p.close()
    c.drawPath(p, M.paint("#A08A70", a))
    c.drawPath(p, M.paint("#6E5C48", a, stroke=4))


def estrobo(c, t, x0, y0, kx, ky, vx, fotos, sombras=True, r=28, rot_x=None, rot_y=None, tc=None, d_curva=1.0):
    """fotos da bola lançada na horizontal de (x0, y0): fotos = [(instante, tempo τ)]; x = vx·τ (m), queda = 5·τ² (m).
    sombras: no alto (x) e à esquerda (queda). rot_x/rot_y = rótulos dos passos; tc = instante da curva tracejada"""
    P = lambda tau: (x0 + vx * tau * kx, y0 + 5 * tau * tau * ky)
    tau_fim = fotos[-1][1]
    if tc is not None and t >= tc:
        pts = [P(tau_fim * i / 60) for i in range(61)]
        F.poli(c, pts, ease_io(prog(t, tc, d_curva)), E.COR, 1.0, 5, dash=E.TRACO)
    for i, (ti, tau) in enumerate(fotos):
        q = ep(t, ti, 0.4)
        if q <= 0:
            continue
        X, Y = P(tau)
        ultima = i == len(fotos) - 1 or t < fotos[i + 1][0]
        E.bola(c, X, Y, r, None, q * (1.0 if ultima else 0.4))
        if sombras:
            c.drawCircle(X, y0 - 90, r * 0.6, M.paint(F.VEL, 0.85 * q))
            c.drawCircle(x0 - 110, Y, r * 0.6, M.paint(F.ACEL, 0.85 * q))
            M.line(c, X, y0 - 90, X, Y, F.VEL, 0.35 * q, 3, dash=E.TRACO)
            M.line(c, x0 - 110, Y, X, Y, F.ACEL, 0.35 * q, 3, dash=E.TRACO)
            if i > 0 and rot_x:
                Xa = P(fotos[i - 1][1])[0]
                E.foco(c, t, ti + 0.2, 0.3, lambda a, Xa=Xa, X=X, s=rot_x[i - 1]: F.medida(c, *s.split(" "), (Xa + X) / 2, y0 - 130, 44, F.VEL, a, "center"))
            if i > 0 and rot_y:
                Ya = P(fotos[i - 1][1])[1]
                E.foco(c, t, ti + 0.2, 0.3, lambda a, Ya=Ya, Y=Y, s=rot_y[i - 1]: F.medida(c, *s.split(" "), x0 - 150, (Ya + Y) / 2 + 16, 44, F.ACEL, a, "right"))
    return P


def aviao(c, x, y, s=1.0, a=1.0):
    """avião de lado, voando para a direita; (x, y) = centro"""
    if a <= 0:
        return
    M.rrect(c, x - 110 * s, y - 20 * s, 220 * s, 40 * s, 20 * s, "#5B6475", a)
    p = skia.Path()
    p.moveTo(x - 10 * s, y); p.lineTo(x - 60 * s, y + 70 * s); p.lineTo(x - 30 * s, y + 70 * s); p.lineTo(x + 40 * s, y); p.close()
    c.drawPath(p, M.paint("#3E4555", a))
    p = skia.Path()
    p.moveTo(x - 100 * s, y - 10 * s); p.lineTo(x - 130 * s, y - 60 * s); p.lineTo(x - 105 * s, y - 60 * s); p.lineTo(x - 70 * s, y - 10 * s); p.close()
    c.drawPath(p, M.paint("#3E4555", a))
    for k in range(4):
        c.drawCircle(x + (10 + 22 * k) * s, y - 4 * s, 6 * s, M.paint("#BFD4E6", a))


def caixa_(c, x, y, s=36, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x - s / 2, y - s / 2, s, s, 5, "#C48A3A", a)
    M.line(c, x - s / 2, y, x + s / 2, y, "#7A5420", a, 3)


def arvore(c, x, yb, s=1.0, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x - 8 * s, yb - 60 * s, 16 * s, 60 * s, 4, "#6E4A2F", a)
    c.drawCircle(x, yb - 80 * s, 40 * s, M.paint("#3F8F4A", a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        x0, y0, ybase = 1300, 560, 940
        E.foco(c, t, C["s01"], 0.5, lambda a: mesa(c, 900, y0 + 30, 400, ybase - y0 - 30, a))
        if t >= C["s01"]:
            F.chao(c, 840, 1880, ybase, ep(t, C["s01"], 0.5))
        t0, t1 = C["s01.c"] - 0.3, C["s01.d"]
        u = max(0.0, min(1.0, (t - t0) / max(0.4, t1 - t0)))
        ky = (ybase - 30 - y0) / 1.0
        yy = y0 + u * u * ky
        E.foco(c, t, C["s01.a"], 0.4, lambda a: E.bola(c, x0 + u * 480, yy, 30, a=a))
        E.foco(c, t, C["s01.b"], 0.4, lambda a: E.bola(c, x0 + 40, yy, 30, F.ACEL, a))
        if t >= C["s01.a"] + 0.3:
            F.seta(c, x0 + 40, y0 - 70, x0 + 220, y0 - 70, F.VEL, ep(t, C["s01.a"] + 0.3, 0.3) * (1 - ep(t, t0, 0.3)), 9)
        if t >= t0:
            M.line(c, x0 - 20, yy, x0 + u * 480 + 60, yy, TINTA2, 0.6, 3, dash=E.TRACO)
        E.frase(c, t, C["s01.a"], [("empurrada", "g", 72, COR)], XE, 330)
        E.frase(c, t, C["s01.b"], [("solta", "g", 72, F.ACEL)], XE, 440)
        E.frase(c, t, C["s01.c"], ps("qual chega", "i", 72) + [("primeiro?", "g", 72)], XE, 600, passo=0.12)
        E.frase(c, t, C["s01.d"], [("juntas", "g", 100, CERTO)], XE, 760)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "o tempo no ar"), ("s02.c", "a distância")))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "queda livre:", "h = 5 · t²", None), ("s03.c", "movimento uniforme:", "d = v · t", None)))


# ---------------- dois movimentos ----------------
def b_dois(c, t, C, b):
    x0, y0 = 860, 400
    kx, ky = 22.0, 22.0
    ybase = y0 + 20 * ky + 28

    def s04():
        E.frase(c, t, C["s04"], [("lançamento", "g", 96, COR)], XE, 260)
        E.frase(c, t, C["s04"] + 0.5, [("horizontal", "g", 96, COR)], XE, 380)
        E.frase(c, t, C["s04.a"], ps("sai na horizontal, de uma altura", "i", 60), XE, 520, passo=0.1)
        E.frase(c, t, C["s04.b"], ps("dois movimentos", "g", 76), XE, 700, passo=0.12)
        E.frase(c, t, C["s04.b"] + 0.5, ps("ao mesmo tempo", "i", 76), XE, 800, passo=0.12)
        E.foco(c, t, C["s04.a"] + 0.6, 0.5, lambda a: mesa(c, 1260, 620, 300, 280, a))
        E.foco(c, t, C["s04.a"] + 0.8, 0.4, lambda a: E.bola(c, 1540, 590, 28, a=a))
        if t >= C["s04.a"] + 1.0:
            pts = [(1540 + 300 * u, 590 + 300 * u * u) for u in [i / 40 for i in range(41)]]
            F.poli(c, pts, ease_io(prog(t, C["s04.a"] + 1.0, 1.0)), E.COR, 1.0, 5, dash=E.TRACO)
            F.chao(c, 1200, 1880, 900, ep(t, C["s04.a"] + 0.6, 0.4))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("na", "i", 70), ("horizontal:", "g", 70, F.VEL)], XE, 280, passo=0.12)
            E.frase(c, t, C["s05.b"], ps("v não muda", "i", 70), XE, 380, passo=0.12)
            E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "movimento uniforme", XE + 300, 470, 46, "g", fundo=F.VEL, a=a))
            E.frase(c, t, C["s05.d"], [("para", "i", 70), ("baixo:", "g", 70, F.ACEL)], XE, 680, passo=0.12)
            E.foco(c, t, C["s05.e"], 0.4, lambda a: E.pilula(c, "queda livre", XE + 190, 780, 46, "g", fundo=F.ACEL, a=a))
            for i in range(4):
                E.foco(c, t, C["s05.a"] + 0.6 + 0.2 * i, 0.3, lambda a, i=i: (c.drawCircle(1080 + i * 170, 330, 22, M.paint(F.VEL, a)),
                                                                              F.seta(c, 1110 + i * 170, 330, 1210 + i * 170, 330, F.VEL, a, 7) if i < 3 else None))
            for i, h in enumerate((0, 5, 20, 45)):
                E.foco(c, t, C["s05.e"] + 0.2 * i, 0.3, lambda a, h=h: c.drawCircle(1350, 600 + h * 8, 22, M.paint(F.ACEL, a)))
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    if True:
        E.foco(c, t, C["s06"], 0.5, lambda a: penhasco(c, x0, y0 + 30, ybase, a))
        F.chao(c, x0 - 360, 1880, ybase, ep(t, C["s06"], 0.5))
    fotos = [(C["s06"] + 0.4, 0), (C["s06.a"], 1), (C["s06.b"], 2)]
    estrobo(c, t, x0, y0, kx, ky, 15, fotos, True, 26, ["15 m", "15 m"], ["5 m", "15 m"], tc=C["s06.c"])
    E.frase(c, t, C["s06"], ps("fotos a cada segundo,", "i", 52), XE, 990, passo=0.1)
    E.frase(c, t, C["s06"] + 1.3, [("15 m/s", "g", 52, F.VEL)], XE + 520, 990)
    E.frase(c, t, C["s06.c"], [("o", "i", 70), ("caminho:", "i", 70), ("parábola", "g", 70, COR)], 1180, 990, passo=0.12)


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    def passo_(k, n, l1, y):
        E.foco(c, t, C[k], 0.5, lambda a: (E.bola(c, XE + 40, y - 28, 40, a=a), centro(c, str(n), XE + 40, y - 6, 50, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, l1, XE + 110, y, passo=0.12)

    def s07():
        E.frase(c, t, C["s07"], ps("o método,", "i", 76) + [("em 2 passos", "g", 76, COR)], XE, 220, passo=0.12)
        passo_("s07.a", 1, [("tempo", "g", 72), ("pela", "i", 72), ("altura", "g", 72, F.ACEL)], 400)
        E.formula_em(c, t, C["s07.b"], "h = 5 · t^2", XE + 110, 510, 80, "g", TINTA)
        passo_("s07.c", 2, [("alcance", "g", 72), ("pela", "i", 72), ("horizontal", "g", 72, F.VEL)], 680)
        E.formula_em(c, t, C["s07.d"], "A = v · t", XE + 110, 790, 80, "g", TINTA)
        # alcance: cota no chão
        x0, y0, yb = 1320, 520, 900
        E.foco(c, t, C["s07.a"], 0.5, lambda a: mesa(c, x0 - 260, y0 + 28, 260, yb - y0 - 28, a))
        if t >= C["s07.a"]:
            F.chao(c, x0 - 300, 1880, yb, ep(t, C["s07.a"], 0.4))
            pts = [(x0 + 400 * u, y0 + (yb - 26 - y0) * u * u) for u in [i / 40 for i in range(41)]]
            F.poli(c, pts, ease_io(prog(t, C["s07.a"] + 0.3, 0.8)), E.COR, 1.0, 5, dash=E.TRACO)
            E.bola(c, x0, y0, 26, a=ep(t, C["s07.a"], 0.4))
        if t >= C["s07.e"]:
            E.segmento(c, t, C["s07.e"], (x0, yb + 50), (x0 + 400, yb + 50), None, cor=E.COR, largura=5, d=0.6)
            E.foco(c, t, C["s07.e"] + 0.5, 0.4, lambda a: centro(c, "alcance A", x0 + 200, yb + 120, 50, "g", COR, a))
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    x0, y0, k = 1380, 480, 16.0
    ybase = y0 + 20 * k + 28
    E.foco(c, t, C["s08.a"], 0.5, lambda a: penhasco(c, x0, y0 + 30, ybase, a))
    if t >= C["s08.a"]:
        F.chao(c, x0 - 360, 1880, ybase, ep(t, C["s08.a"], 0.5))
        E.foco(c, t, C["s08.a"] + 0.4, 0.4, lambda a: F.medida(c, 20, "m", x0 - 180, (y0 + ybase) / 2 + 20, 64, BR, a, "center", cor_u=BR))
    E.foco(c, t, C["s08.b"], 0.4, lambda a: F.seta(c, x0 + 40, y0 - 60, x0 + 240, y0 - 60, F.VEL, a, 9))
    E.foco(c, t, C["s08.b"] + 0.2, 0.4, lambda a: F.medida(c, 15, "m/s", x0 + 260, y0 - 44, 50, F.VEL, a))
    estrobo(c, t, x0, y0, k, k, 15, [(C["s08.a"] + 0.4, 0), (C["s08.e"], 2)], False, 26, tc=C["s08.e"] - 0.1)
    E.frase(c, t, C["s08.a"], [("penhasco", "i", 66), ("20 m,", "g", 66), ("15 m/s", "g", 66, F.VEL)], XE, 230, passo=0.12)
    E.formula_em(c, t, C["s08.c"], "20 = 5 · t^2", XE, 400, 76, "g", TINTA)
    E.formula_em(c, t, C["s08.c"] + 1.2, "t^2 = 4", XE, 520, 76, "g", TINTA)
    bola_txt(c, t, C["s08.d"], "2 s", XE + 470, 490, 80, 56, F.ACEL)
    E.formula_em(c, t, C["s08.e"], "A = 15 · 2 =", XE, 720, 76, "g", TINTA)
    bola_txt(c, t, C["s08.f"], "30 m", XE + 640, 695, 95, 56)
    if t >= C["s08.f"]:
        E.segmento(c, t, C["s08.f"], (x0, ybase + 50), (x0 + 30 * k, ybase + 50), None, cor=E.COR, largura=5, d=0.5)
        E.foco(c, t, C["s08.f"] + 0.4, 0.4, lambda a: F.medida(c, 30, "m", x0 + 15 * k, ybase + 115, 50, COR, a, "center"))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s09"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s09.a"], ps("soltar a carga", "i", 68) + [("em cima", "g", 68, ERRADO)] + ps("do alvo", "i", 68), XE + 480, 200, passo=0.12)
    yb, k = 960, 0.9              # chão, pixels por metro na horizontal
    xs = 520                      # onde a caixa é solta (em cima da clareira)
    if t >= C["s09.b"]:
        F.chao(c, 160, 1860, yb, ep(t, C["s09.b"], 0.5))
    # o avião anda 100 m/s; a caixa cai em 10 s. Tempo da animação: de s09.c até s10.c
    t0, t1 = C["s09.c"], C["s10.c"]
    u = max(0.0, min(1.0, (t - t0) / max(0.5, t1 - t0)))
    xa = xs - 200 + ep(t, C["s09.b"], 1.0) * 200 if t < t0 else xs + u * 1000 * k
    E.foco(c, t, C["s09.b"], 0.5, lambda a: aviao(c, xa, 330, 1.0, a))
    E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: (F.medida(c, 100, "m/s", 300, 300, 50, F.VEL, a), F.medida(c, 500, "m", 300, 380, 50, F.ACEL, a)))
    E.foco(c, t, C["s09.c"] - 0.6, 0.5, lambda a: (M.rrect(c, xs - 90, yb - 8, 180, 16, 8, "#6BBF59", a), arvore(c, xs - 140, yb, 0.8, a), arvore(c, xs + 140, yb, 0.8, a)))
    E.foco(c, t, C["s09.c"] - 0.4, 0.4, lambda a: centro(c, "clareira", xs, yb + 110, 44, "i", TINTA2, a))
    if t >= t0:
        tau = 10 * u
        cx = xs + 100 * tau * k
        cy = 360 + 5 * tau * tau * k * (yb - 380) / (500 * k)
        pts = [(xs + 100 * (10 * v) * k, 360 + 5 * (10 * v) ** 2 * (yb - 380) / 500) for v in [i / 40 * u for i in range(41)]]
        F.poli(c, pts, 1.0, E.COR, 1.0, 4, dash=E.TRACO)
        caixa_(c, cx, cy, 34)
    E.foco(c, t, C["s10.a"], 0.5, lambda a: F.cronometro(c, 1700, 560, 70, 10, a, "10 s"))
    E.formula_em(c, t, C["s10.a"] + 1.4, "500 = 5 · t^2 → t = 10 s", 300, 520, 46, "b", TINTA2)
    E.formula_em(c, t, C["s10.b"], "100 · 10 = 1000 m", 300, 600, 56, "g", F.VEL)
    if t >= C["s10.c"]:
        E.segmento(c, t, C["s10.c"], (xs, yb + 40), (xs + 1000 * k, yb + 40), None, cor=ERRADO, largura=5, d=0.5)
        E.foco(c, t, C["s10.c"] + 0.4, 0.4, lambda a: centro(c, "1 km depois", xs + 500 * k, yb + 100, 50, "g", ERRADO, a))
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "solte 1 km ANTES", 760, 760, 56, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    x0, y0, k = 420, 560, 13.0
    yb = y0 + 20 * k + 24

    def cena(s_):
        q = ep(t, C["s11"], 0.5)
        M.rrect(c, x0 - 320, y0 + 26, 320, yb - y0 - 26, 6, "#3A3A48", q)
        M.line(c, x0 - 340, yb, 1880, yb, CLARO, q, 4)
        E.bola(c, x0, y0, 24, a=q)
    cena(None)
    E.frase(c, t, C["s11"], ps("o atalho:", "i", 72, CLARO), W / 2, 150, "center")
    E.frase(c, t, C["s11.a"], ps("a altura", "i", 84, CLARO) + [("manda", "g", 84, BR), ("no", "i", 84, CLARO), ("tempo", "g", 84, BR)], W / 2, 270, "center", 0.12)
    for j, (vx, cor, ti) in enumerate(((15, E.COR, C["s11.c"]), (30, CLARO, C["s11.d"]))):
        if t >= ti:
            pts = [(x0 + vx * 2 * u * k, y0 + 20 * u * u * k) for u in [i / 50 for i in range(51)]]
            F.poli(c, pts, ease_io(prog(t, ti, 0.9)), cor, 1.0, 6, dash=E.TRACO if j == 0 else None)
            E.foco(c, t, ti + 0.8, 0.4, lambda a, vx=vx, cor=cor: (F.medida(c, vx, "m/s", x0 + vx * 2 * k, yb + 70, 48, BR, a, "center", cor_u=CLARO),
                                                                  F.medida(c, vx * 2, "m", x0 + vx * 2 * k, yb + 130, 56, cor, a, "center", cor_u=CLARO)))
    E.frase(c, t, C["s11.b"], ps("tempo da", "i", 56, CLARO) + [("queda livre", "g", 56, BR)], 1340, 420, "left", 0.1)
    E.foco(c, t, C["s11.c"] + 0.6, 0.4, lambda a: E.pilula(c, "os dois: 2 s", 1500, 510, 48, "g", a=a))
    E.frase(c, t, C["s11.d"], [("dobro", "g", 56, BR), ("da", "i", 56, CLARO), ("v", "g", 56, BR), ("→", "g", 56, CLARO)], 1340, 630, "left", 0.1)
    E.frase(c, t, C["s11.d"] + 0.5, [("dobro", "g", 56, BR), ("do", "i", 56, CLARO), ("alcance", "g", 56, BR)], 1340, 700, "left", 0.1)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.b"], [("não", "g", 46, ERRADO), ("compensa:", "i", 48, CLARO)], 1340, 820, "left", 0.1)
    E.frase(c, t, C["s12.b"] + 0.6, ps("velocidade de chegada", "g", 46, BR), 1340, 885, "left", 0.1)
    E.frase(c, t, C["s12.c"], ps("juntar as duas: outra aula", "i", 46, CLARO), 1340, 950, "left", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s13.a"], ps("bola rola sobre a mesa", "i", 70), XE, 330, passo=0.12)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: (E.escreve(c, "altura", XE, 470, 60, "i", TINTA, a), F.medida(c, "1,25", "m", XE + 200, 470, 84, F.ACEL, a)))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: (E.escreve(c, "sai a", XE, 600, 60, "i", TINTA, a), F.medida(c, 2, "m/s", XE + 200, 600, 84, F.VEL, a)))
    E.frase(c, t, C["s13.d"], [("a", "i", 72), ("que", "i", 72), ("distância", "g", 72, COR)], XE, 780, passo=0.12)
    E.frase(c, t, C["s13.d"] + 0.8, ps("toca o chão?", "g", 72, COR), XE, 880, passo=0.12)
    if t < C["s14"]:
        x0, y0, yb = 1500, 560, 900
        E.foco(c, t, C["s13.a"], 0.5, lambda a: mesa(c, x0 - 360, y0 + 28, 360, yb - y0 - 28, a))
        if t >= C["s13.a"]:
            F.chao(c, x0 - 420, 1880, yb, ep(t, C["s13.a"], 0.4))
        p = ease_io(prog(t, C["s13.a"] + 0.2, 1.2))
        E.foco(c, t, C["s13.a"] + 0.2, 0.4, lambda a: E.bola(c, lerp(x0 - 300, x0, p), y0, 26, a=a))
        if t >= C["s13.d"]:
            pts = [(x0 + 220 * u, y0 + (yb - 26 - y0) * u * u) for u in [i / 40 for i in range(41)]]
            F.poli(c, pts, ease_io(prog(t, C["s13.d"], 0.8)), E.COR, 1.0, 5, dash=E.TRACO)
            E.foco(c, t, C["s13.d"] + 0.6, 0.4, lambda a: centro(c, "?", x0 + 110, yb + 80, 70, "g", COR, a))
    else:
        E.relogio(c, t, C["s14.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s15"] + 0.6, [("1.", "g", 60, COR), ("o", "i", 64), ("tempo", "g", 64, F.ACEL)], XE, 230, passo=0.12)
    E.formula_em(c, t, C["s15.a"], "1,25 = 5 · t^2", XE, 370, 80, "g", TINTA)
    E.formula_em(c, t, C["s15.b"], "t^2 = 0,25", XE, 500, 80, "g", TINTA)
    bola_txt(c, t, C["s15.c"], "0,5 s", XE + 640, 470, 100, 56, F.ACEL)
    E.frase(c, t, C["s16.a"], [("2.", "g", 60, COR), ("o", "i", 64), ("alcance", "g", 64, F.VEL)], XE, 690, passo=0.12)
    E.formula_em(c, t, C["s16.a"] + 0.5, "A = 2 · 0,5 =", XE, 830, 80, "g", TINTA)
    bola_txt(c, t, C["s16.b"], "1 m", XE + 640, 800, 100, 60)
    x0, y0, yb = 1500, 560, 900
    E.foco(c, t, C["s15"], 0.5, lambda a: mesa(c, x0 - 360, y0 + 28, 360, yb - y0 - 28, a))
    if t >= C["s15"]:
        F.chao(c, x0 - 420, 1880, yb, ep(t, C["s15"], 0.4))
        E.bola(c, x0, y0, 26, a=ep(t, C["s15"], 0.4))
    if t >= C["s16.a"]:
        pts = [(x0 + 220 * u, y0 + (yb - 26 - y0) * u * u) for u in [i / 40 for i in range(41)]]
        F.poli(c, pts, ease_io(prog(t, C["s16.a"], 0.8)), E.COR, 1.0, 5, dash=E.TRACO)
    if t >= C["s16.b"]:
        E.segmento(c, t, C["s16.b"], (x0, yb + 40), (x0 + 220, yb + 40), None, cor=E.COR, largura=5, d=0.5)
        E.foco(c, t, C["s16.b"] + 0.4, 0.4, lambda a: F.medida(c, 1, "m", x0 + 110, yb + 110, 56, COR, a, "center"))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = (("s17.a", [("vertical:", "g", 66, F.ACEL), ("queda", "i", 70), ("livre", "i", 70), ("→", "g", 66), ("tempo", "g", 66)]),
             ("s17.b", [("horizontal:", "g", 66, F.VEL), ("v", "i", 70), ("constante", "i", 70), ("→", "g", 66), ("alcance", "g", 66)]))

    def desenho():  # um vetor e as duas partes
        O = (300, 960)
        F.vetor(c, t, C["s18.a"] + 0.3, O, (760, 660), None, None, E.COR, 10)
        F.componentes(c, t, C["s18.a"] + 1.0, O, (760, 660), "x", "y", E.COR, size=46)
        E.foco(c, t, C["s18.b"], 0.4, lambda a: E.escreve(c, "seno e cosseno", 860, 900, 60, "i", TINTA, a))
    fim(c, t, C, "s17", itens, "s18", [("s18.a", [("Decompor", "g", 110, COR)]), ("s18.a", [("um", "i", 100), ("vetor", "g", 110, COR)])],
        desenho, "s18.c", "s18.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, dois=b_dois, metodo=b_metodo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
