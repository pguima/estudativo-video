"""Visual — Estudativo · FIS-CIN-016: lançamento oblíquo.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001/roteiro/visual.py (peças em _ferramentas/fisica.py, F).
Nesta aula: a velocidade de saída v₀ é a seta petróleo (F.VEL) com as duas partes (F.componentes): vx (horizontal) e vy
(vertical); a trajetória é a curva laranja; a altura máxima H e o alcance A são cotas laranja. Ângulos complementares
aparecem lado a lado, um em laranja e outro em tinta. Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-016_lancamento_obliquo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("decompor", "vertical", "erro", "angulos", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 50 * 0.8 == 40 and 50 * 0.6 == 30 and 30 / 10 == 3 and 5 * 3 ** 2 == 45 and 900 / 20 == 45 and 2 * 3 == 6 and 40 * 6 == 240
assert 2 * 40 / 10 == 8 and 30 * 8 == 240 and 40 * 30 / 5 == 240 and 40 * 30 == 1200 and 1200 / 5 == 240 and 5 * 4 ** 2 == 80
for _ang, _A in ((30, 34.64), (45, 40.0), (60, 34.64)):
    _r = math.radians(_ang)
    assert abs(2 * (20 * math.cos(_r)) * (20 * math.sin(_r)) / 10 - _A) < 0.01
assert 25 * 0.6 == 15 and 25 * 0.8 == 20 and 20 / 10 == 2 and 5 * 2 ** 2 == 20 and 2 * 2 == 4 and 15 * 4 == 60 and 15 * 20 / 5 == 60


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
def traj(c, t, t0, x0, yb, vx, vy, k, d=1.2, cor=None, largura=6, tracejada=False, a=1.0):
    """trajetória do lançamento oblíquo saindo de (x0, yb), sem ar, g = 10: x = vx·τ, y = vy·τ − 5·τ² (k px por metro).
    Devolve a função τ → ponto e o tempo de voo"""
    T = 2 * vy / 10
    P = lambda tau: (x0 + vx * tau * k, yb - (vy * tau - 5 * tau * tau) * k)
    if t >= t0:
        pts = [P(T * i / 80) for i in range(81)]
        F.poli(c, pts, ease_io(prog(t, t0, d)), cor or E.COR, a, largura, dash=E.TRACO if tracejada else None)
    return P, T


def cota_h(c, t, t0, x, y0, y1, rotulo, cor=None, lado=1):
    """cota vertical de y0 a y1 com o rótulo ao lado"""
    if t < t0:
        return
    q = ep(t, t0, 0.5)
    cor = cor or E.COR
    M.line(c, x, y0, x, lerp(y0, y1, ease_io(prog(t, t0, 0.5))), cor, q, 5)
    for y in (y0, y1):
        M.line(c, x - 14, y, x + 14, y, cor, q, 5)
    v, _, u = rotulo.partition(" ")
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: F.medida(c, v, u, x + lado * 26, (y0 + y1) / 2 + 16, 52, COR, a, "left" if lado > 0 else "right"))


def cota_a(c, t, t0, x0, x1, y, rotulo, cor=None):
    if t < t0:
        return
    E.segmento(c, t, t0, (x0, y), (x1, y), None, cor=cor or E.COR, largura=5, d=0.5)
    v, _, u = rotulo.partition(" ")
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: F.medida(c, v, u, (x0 + x1) / 2, y + 66, 52, COR, a, "center"))


def chao_em(c, t, t0, x0, x1, y):
    if t >= t0:
        F.chao(c, x0, x1, y, ep(t, t0, 0.5))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    x0, yb, k = 520, 900, 30.0
    r30, r60, r45 = math.radians(30), math.radians(60), math.radians(45)

    def um():
        chao_em(c, t, C["s01"], 420, 1860, yb)
        E.foco(c, t, C["s01"], 0.4, lambda a: E.bola(c, x0, yb - 22, 22, a=a))
        traj(c, t, C["s01.a"], x0, yb, 20 * math.cos(r30), 20 * math.sin(r30), k, cor=TINTA2)
        traj(c, t, C["s01.b"], x0, yb, 20 * math.cos(r60), 20 * math.sin(r60), k, cor=TINTA)
        E.foco(c, t, C["s01.a"] + 0.3, 0.4, lambda a: E.pilula(c, "30°", x0 + 300, yb - 120, 40, "g", fundo=TINTA2, a=a))
        E.foco(c, t, C["s01.b"] + 0.3, 0.4, lambda a: E.pilula(c, "60°", x0 + 300, yb - 420, 40, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s01.c"], ps("qual vai", "i", 76) + [("mais longe?", "g", 76, COR)], XE, 220, passo=0.12)
        if t >= C["s01.d"]:
            X = x0 + 34.64 * k
            q = ep(t, C["s01.d"], 0.4)
            c.drawCircle(X, yb, 40 + 4 * math.sin(t * 5), M.paint(CERTO, q, stroke=6))
            E.foco(c, t, C["s01.d"] + 0.3, 0.4, lambda a: E.pilula(c, "mesmo ponto", X, yb + 80, 44, "g", fundo=CERTO, a=a))
        if t >= C["s01.e"]:
            traj(c, t, C["s01.e"], x0, yb, 20 * math.cos(r45), 20 * math.sin(r45), k, cor=E.COR, largura=8)
            E.foco(c, t, C["s01.e"] + 0.9, 0.4, lambda a: E.pilula(c, "45°: o mais longe", 1640, 560, 44, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "a altura máxima"), ("s02.c", "o alcance"), ("s02.d", "os ângulos")))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "decompor:", "seno e cosseno", None), ("s03.c", "lançamento para cima:", "t = v₀ ÷ g", None),
                              ("s03.d", "lançamento horizontal:", "cada direção na sua", None)), num="3")


# ---------------- decompor ----------------
def b_decompor(c, t, C, b):
    O, k = (1060, 860), 12.0
    ang = math.atan2(0.6, 0.8)
    B = (O[0] + 50 * math.cos(ang) * k, O[1] - 50 * math.sin(ang) * k)
    chao_em(c, t, C["s04.a"], 900, 1860, O[1])
    E.foco(c, t, C["s04.a"], 0.4, lambda a: E.bola(c, O[0], O[1] - 22, 22, a=a))
    F.vetor(c, t, C["s04.a"] + 0.3, O, B, "v₀", None, F.VEL, 10, lado=-1)
    E.angulo(c, t, C["s04.a"] + 0.8, O, (O[0] + 300, O[1]), B, "θ", r=110)
    F.componentes(c, t, C["s04.c"] - 0.2, O, B, "vx", "vy", F.VEL, size=50)
    E.frase(c, t, C["s04"], ps("sai", "i", 70) + [("inclinado,", "g", 70, COR)] + ps("com um ângulo", "i", 70), XE, 230, passo=0.12)
    E.frase(c, t, C["s04.b"], [("1.", "g", 64, COR), ("decompor", "g", 64), ("v₀", "g", 64, F.VEL)], XE, 360, passo=0.12)

    def letras():
        E.formula_em(c, t, C["s04.c"], "vx = v₀ · cos θ", XE, 520, 72, "g", TINTA)
        E.formula_em(c, t, C["s04.d"], "vy = v₀ · sen θ", XE, 640, 72, "g", TINTA)
    E.saida(c, t, C["s05"] - 0.1, letras)
    if t < C["s05"]:
        return
    E.foco(c, t, C["s05.a"], 0.4, lambda a: F.medida(c, 50, "m/s", B[0] - 220, B[1] - 40, 56, F.VEL, a))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.formula(c, "cos θ = 0,8   sen θ = 0,6", XE, 520, 56, "b", TINTA2, a))
    E.formula_em(c, t, C["s05.c"], "vx = 50 · 0,8 = 40 m/s", XE, 660, 66, "g", TINTA)
    E.formula_em(c, t, C["s05.d"], "vy = 50 · 0,6 = 30 m/s", XE, 790, 66, "g", TINTA)
    E.foco(c, t, C["s05.c"] + 0.8, 0.4, lambda a: E.pilula(c, "40", (O[0] + B[0]) / 2, O[1] + 60, 40, "g", fundo=F.VEL, a=a))
    E.foco(c, t, C["s05.d"] + 0.8, 0.4, lambda a: E.pilula(c, "30", B[0] + 70, (O[1] + B[1]) / 2, 40, "g", fundo=F.VEL, a=a))


# ---------------- vertical ----------------
def b_vertical(c, t, C, b):
    x0, yb, k = 880, 900, 3.7
    chao_em(c, t, C["s06"], 800, 1860, yb)
    P, T = traj(c, t, C["s06.b"], x0, yb, 40, 30, k, d=1.4)
    xt, yt = P(3)
    cota_h(c, t, C["s06.d"], xt, yb, yt, "45 m")
    E.foco(c, t, C["s06.b"], 0.4, lambda a: (F.seta(c, x0, yb - 20, x0, yb - 20 - 30 * 5, F.VEL, a, 9), E.escreve(c, "30", x0 - 90, yb - 90, 50, "g", F.VEL, a)))
    E.frase(c, t, C["s06.a"], ps("cada parte", "i", 70) + [("na sua", "g", 70, COR)], XE, 220, passo=0.12)
    E.frase(c, t, C["s06.b"], [("vertical:", "g", 60, F.VEL)] + ps("para cima a 30 m/s", "i", 60), XE, 330, passo=0.1)
    E.formula_em(c, t, C["s06.c"], "subida: f{30}{10} = 3 s", XE, 470, 64, "g", TINTA)
    E.formula_em(c, t, C["s06.d"], "H = 5 · 3^2 = 45 m", XE, 600, 64, "g", COR)
    E.formula_em(c, t, C["s06.e"], "voo = 2 · 3 = 6 s", XE, 730, 64, "g", TINTA)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07.a"], [("horizontal:", "g", 60, F.VEL)] + ps("nada freia", "i", 60), XE, 860, passo=0.1)
    E.foco(c, t, C["s07.b"], 0.4, lambda a: (F.seta(c, x0 + 20, yb - 70, x0 + 220, yb - 70, F.VEL, a, 9), F.medida(c, 40, "m/s", x0 + 240, yb - 54, 46, F.VEL, a)))
    E.formula_em(c, t, C["s07.c"], "A = 40 · 6 =", 1200, 180, 70, "g", TINTA)
    bola_txt(c, t, C["s07.d"], "240 m", 1700, 160, 90, 52)
    cota_a(c, t, C["s07.d"], x0, x0 + 240 * k, yb + 50, "240 m")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    x0, yb, k = 900, 900, 3.6
    chao_em(c, t, C["s08"], 840, 1860, yb)
    P, T = traj(c, t, C["s08"], x0, yb, 40, 30, k, d=0.8, cor=TINTA2)
    xt, yt = P(3)
    E.foco(c, t, C["s08"] + 0.6, 0.4, lambda a: E.bola(c, xt, yt, 28, a=a))
    E.frase(c, t, C["s08"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s08.a"], ps("no alto,", "i", 66), XE, 340, passo=0.1)
    E.foco(c, t, C["s08.a"] + 0.6, 0.5, lambda a: E.escreve(c, "v = 0 ?", XE, 470, 100, "g", ERRADO, a))
    if t >= C["s08.b"]:
        E.risco(c, XE - 10, 490, XE + 360, 390, t, C["s08.b"], largura=12)
    E.frase(c, t, C["s08.b"], [("só", "i", 62), ("vy", "g", 62, F.VEL), ("zera", "g", 62)], XE, 620, passo=0.12)
    E.frase(c, t, C["s08.c"], [("vx", "g", 62, F.VEL), ("continua", "i", 62), ("40 m/s", "g", 62, F.VEL)], XE, 730, passo=0.12)
    F.vetor(c, t, C["s08.c"] + 0.4, (xt, yt), (xt + 40 * 6, yt), "vx", "40 m/s", F.VEL, 10, lado=-1)
    E.frase(c, t, C["s08.d"], ps("lá em cima: v =", "i", 58) + [("só a horizontal", "g", 58, COR)], XE, 870, passo=0.1)


# ---------------- ângulos ----------------
def b_angulos(c, t, C, b):
    x0, yb, k = 700, 960, 4.2

    def s09():
        chao_em(c, t, C["s09"], 600, 1860, yb)
        traj(c, t, C["s09"], x0, yb, 40, 30, k, d=0.6, cor=E.COR)
        if t >= C["s09.d"]:
            traj(c, t, C["s09.d"], x0, yb, 30, 40, k, d=1.2, cor=TINTA, largura=6, tracejada=True)
        E.frase(c, t, C["s09.a"], ps("ângulo", "i", 60) + [("complementar", "g", 60, COR)], XE, 210, passo=0.12)
        E.foco(c, t, C["s09.a"] + 0.7, 0.4, lambda a: E.escreve(c, "soma 90°", XE, 290, 50, "i", TINTA2, a))
        E.frase(c, t, C["s09.b"], [("sen", "g", 56), ("e", "i", 56), ("cos", "g", 56), ("trocam", "g", 56, COR)], XE, 400, passo=0.12)
        E.foco(c, t, C["s09.c"], 0.4, lambda a: (E.formula(c, "vx = 30", XE, 520, 56, "g", F.VEL, a), E.formula(c, "vy = 40", XE + 290, 520, 56, "g", F.VEL, a)))
        E.formula_em(c, t, C["s09.d"], "voo = 8 s", XE, 630, 56, "g", TINTA)
        E.formula_em(c, t, C["s09.e"], "A = 30 · 8 = 240 m", XE, 740, 56, "g", TINTA)
        E.foco(c, t, C["s09.f"], 0.5, lambda a: E.pilula(c, "o mesmo alcance!", XE + 260, 850, 50, "g", fundo=CERTO, a=a))
        if t >= C["s09.f"]:
            X = x0 + 240 * k
            c.drawCircle(X, yb, 40 + 4 * math.sin(t * 5), M.paint(CERTO, ep(t, C["s09.f"], 0.4), stroke=6))
            E.foco(c, t, C["s09.f"] + 0.8, 0.4, lambda a: (centro(c, "H = 45 m", x0 + 120 * k, yb - 45 * k + 60, 44, "b", COR, a),
                                                         centro(c, "H = 80 m", x0 + 120 * k, yb - 80 * k - 30, 44, "b", TINTA, a)))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], ps("o alcance depende de", "i", 66), XE, 230, passo=0.12)
    E.formula_em(c, t, C["s10.a"] + 1.0, "vx · vy", XE + 700, 230, 80, "g", F.VEL)
    E.formula_em(c, t, C["s10.b"], "40 · 30 = 30 · 40", XE, 360, 72, "g", TINTA)
    E.frase(c, t, C["s10.c"], [("mesma", "i", 56), ("v₀:", "g", 54)] + ps("maior produto com", "i", 56) + [("partes iguais", "g", 56, COR)], XE, 490, passo=0.1)
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "45°", XE + 90, 590, 56, "g", fundo=E.COR, a=a))
    # v0 = 20: 30°, 45° e 60°
    xb, ybb, kk = 820, 1000, 18.0
    if t >= C["s10.e"]:
        chao_em(c, t, C["s10.e"], 760, 1860, ybb)
        for j, (ang, cor) in enumerate(((30, TINTA2), (60, TINTA), (45, E.COR))):
            r = math.radians(ang)
            traj(c, t, C["s10.e"] + 0.5 * j, xb, ybb, 20 * math.cos(r), 20 * math.sin(r), kk, d=0.9, cor=cor, largura=7 if ang == 45 else 5)
        E.foco(c, t, C["s10.e"] + 1.4, 0.4, lambda a: (E.escreve(c, "35 m", xb + 34.64 * kk - 10 - E.larg("35 m", "b", 46), ybb + 60, 46, "b", TINTA, a),
                                                       E.escreve(c, "40 m", xb + 40 * kk + 10, ybb + 60, 50, "g", COR, a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s11():
        E.frase(c, t, C["s11"], ps("o atalho:", "i", 76, CLARO) + [("com g = 10", "g", 66, BR)], W / 2, 170, "center", 0.12)
        E.formula_em(c, t, C["s11.a"], "A = f{vx · vy}{5}", W / 2, 400, 130, "g", BR, "center")
        E.formula_em(c, t, C["s11.b"], "f{40 · 30}{5} = f{1200}{5}", W / 2 - 80, 640, 80, "g", CLARO, "center")
        E.foco(c, t, C["s11.c"], 0.5, lambda a: (E.bola(c, W / 2 + 420, 620, 100, a=a), F.medida(c, 240, "m", W / 2 + 420, 640, 54, BR, a, "center", cor_u=BR)))
        E.formula_em(c, t, C["s11.d"], "porque o voo = f{2 · vy}{10} = f{vy}{5}", W / 2, 890, 64, "g", CLARO, "center")
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.a"], [("não", "g", 66, ERRADO), ("compensa:", "i", 70, CLARO)] + ps("chegada em outra altura", "i", 70, CLARO), W / 2, 220, "center", 0.1)
    # morro: sai do alto e cai embaixo
    q = ep(t, C["s12.a"] + 0.8, 0.5)
    if q > 0:
        p = skia.Path()
        p.moveTo(200, 980); p.lineTo(200, 560); p.cubicTo(420, 540, 600, 560, 700, 980); p.close()
        c.drawPath(p, M.paint("#3A3A48", q))
        M.line(c, 180, 980, 1800, 980, CLARO, q, 4)
        pts = [(560 + 90 * u, 560 - (20 * u - 5 * u * u) * 12) for u in [i / 60 * 5.32 for i in range(61)]]
        F.poli(c, pts, ease_io(prog(t, C["s12.a"] + 1.0, 1.4)), E.COR, q, 6)
        E.bola(c, 560, 548, 18, a=q)
    E.frase(c, t, C["s12.a"] + 2.0, ps("nem o atalho, nem os 45°", "i", 60, CLARO), 1050, 520, "left", 0.1)
    E.frase(c, t, C["s12.b"], ps("tempo pela", "i", 60, CLARO) + [("altura", "g", 60, BR), ("da", "i", 60, CLARO), ("descida", "g", 60, BR)], 1050, 640, "left", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s13.a"], ps("bola chutada do chão", "i", 72), XE, 330, passo=0.12)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: F.medida(c, 25, "m/s", XE, 450, 96, F.VEL, a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "cos θ = 0,6   sen θ = 0,8", XE, 560, 56, "b", TINTA2, a))
    E.frase(c, t, C["s13.d"], [("altura", "g", 64), ("máxima?", "g", 64, COR), ("alcance?", "g", 64, COR)], XE, 720, passo=0.12)
    E.frase(c, t, C["s13.e"], ps("outro ângulo com o", "i", 62) + [("mesmo alcance?", "g", 60, COR)], XE, 830, passo=0.12)
    if t < C["s14"]:
        O = (1260, 900)
        ang = math.atan2(0.8, 0.6)
        chao_em(c, t, C["s13.a"], 1100, 1860, O[1])
        E.foco(c, t, C["s13.a"], 0.4, lambda a: E.bola(c, O[0], O[1] - 22, 22, a=a))
        F.vetor(c, t, C["s13.b"], O, (O[0] + 25 * 14 * math.cos(ang), O[1] - 25 * 14 * math.sin(ang)), "v₀", "25 m/s", F.VEL, 10)
        E.angulo(c, t, C["s13.c"], O, (O[0] + 300, O[1]), (O[0] + 25 * 14 * math.cos(ang), O[1] - 25 * 14 * math.sin(ang)), "θ", r=100)
    else:
        E.relogio(c, t, C["s14.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x0, yb, k = 1080, 930, 11.0
    chao_em(c, t, C["s15"], 980, 1860, yb)
    P, T = traj(c, t, C["s15.c"], x0, yb, 15, 20, k, d=1.2)
    xt, yt = P(2)
    cota_h(c, t, C["s15.d"], xt, yb, yt, "20 m")
    E.formula_em(c, t, C["s15.a"], "vx = 25 · 0,6 = 15", XE, 230, 60, "g", F.VEL)
    E.formula_em(c, t, C["s15.b"], "vy = 25 · 0,8 = 20", XE, 330, 60, "g", F.VEL)
    E.formula_em(c, t, C["s15.c"], "subida: f{20}{10} = 2 s", XE, 450, 60, "g", TINTA)
    E.formula_em(c, t, C["s15.d"], "H = 5 · 2^2 = 20 m", XE, 570, 60, "g", COR)
    E.formula_em(c, t, C["s16.a"], "voo = 4 s", XE, 690, 60, "g", TINTA)
    E.formula_em(c, t, C["s16.b"], "A = 15 · 4 = 60 m", XE, 800, 60, "g", COR)
    cota_a(c, t, C["s16.b"], x0, x0 + 60 * k, yb + 50, "60 m")
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.pilula(c, "atalho: 15 · 20 ÷ 5 = 60", 1450, 230, 48, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s16.d"], 0.5, lambda a: E.pilula(c, "complementar: sen 0,6 e cos 0,8", XE + 430, 920, 44, "g", fundo=TINTA, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = (("s17.a", [("decomponha", "g", 64), ("v₀", "g", 64, F.VEL)]),
             ("s17.b", [("vertical", "g", 64, F.VEL), ("→", "g", 64), ("tempo", "i", 66), ("e", "i", 66), ("altura", "i", 66)]),
             ("s17.c", [("horizontal", "g", 64, F.VEL), ("→", "g", 64), ("alcance", "i", 66)]),
             ("s17.d", [("mesma", "i", 66), ("altura:", "i", 66), ("45°", "g", 64, COR), ("vai", "i", 66), ("mais", "i", 66), ("longe", "g", 64)]))

    def desenho():
        for j, (lab, x) in enumerate((("gráficos", 300), ("queda", 640), ("lançamentos", 960))):
            E.foco(c, t, C["s18.b"] + 0.3 * j, 0.4, lambda a, lab=lab, x=x: E.pilula(c, lab, x + (E.larg(lab, "g", 48) + 52) / 2, 820, 48, "g", fundo=TINTA, a=a))
    fim(c, t, C, "s17", itens, "s18", [("s18.a", [("Praticando", "g", 120, COR)])], desenho, "s18.c", "s18.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, decompor=b_decompor, vertical=b_vertical, horizontal=b_vertical, erro=b_erro,
              angulos=b_angulos, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
