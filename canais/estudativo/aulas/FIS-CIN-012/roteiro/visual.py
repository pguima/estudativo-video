"""Visual — Estudativo · FIS-CIN-012: gráfico velocidade por tempo, inclinação e área.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001/roteiro/visual.py (peças em _ferramentas/fisica.py, F).
Nesta aula: a linha do gráfico v × t é velocidade (F.VEL, petróleo); a do a × t é aceleração (F.ACEL, violeta); a área que
se calcula vem na cor da matéria (laranja); área negativa em azul (F.NEG). Os catetos da inclinação são tracejados.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-012_grafico_velocidade_tempo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ler", "area", "aceleracao", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 20 / 10 == 2 and 10 * 20 / 2 == 100 and 10 * 5 == 50
assert (30 + 10) * 4 / 2 == 80 and 10 * 4 + 5 * 4 ** 2 / 2 == 80 and (30 - 10) / 4 == 5
assert 2 * 5 == 10 and 12 / 6 == 2 and 6 * 12 / 2 == 36 and 10 * 12 == 120 and 36 + 120 == 156 and (16 + 10) * 12 / 2 == 156


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
GX, GY, GW, GH = 900, 210, 820, 560  # caixa padrão do gráfico, à direita


def gvt(c, t, t0, tmax=12, vmax=25, passo=2, passo_y=5, eixo_y="v (m/s)", caixa=(GX, GY, GW, GH), vmin=0, marcas_x=None, marcas_y=None):
    x, y, w, h = caixa
    return F.grafico(c, t, t0, x, y, w, h, 0, tmax, vmin, vmax, "t (s)", eixo_y, passo, passo_y, marcas_x=marcas_x, marcas_y=marcas_y)


def reta(v0, v1, t1):
    return lambda x: v0 + (v1 - v0) * x / t1


def catetos(c, t, t0, P, A, B, rot_v, rot_t, t1=None, cor=None):
    """os catetos da inclinação de A a B (valores): primeiro o que anda para o lado, depois o que sobe"""
    cor = cor or E.COR
    t1 = t1 if t1 is not None else t0 + 0.8
    (xa, ya), (xb, yb) = P(*A), P(*B)
    if t >= t0:
        M.line(c, xa, ya, xb, ya, cor, 1.0, 6, dash=E.TRACO, progress=ease_io(prog(t, t0, 0.5)))
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: F.medida(c, *rot_t.split(" "), (xa + xb) / 2 + 40, ya - 22, 48, COR, a, "center"))
    if t >= t1:
        M.line(c, xb, ya, xb, yb, cor, 1.0, 6, dash=E.TRACO, progress=ease_io(prog(t, t1, 0.5)))
        E.foco(c, t, t1 + 0.3, 0.4, lambda a: F.medida(c, *rot_v.split(" "), xb + 30, (ya + yb) / 2 + 18, 48, COR, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        P = gvt(c, t, C["s01.a"])
        f = reta(0, 20, 10)
        E.curva(c, t, C["s01.b"], P, f, 0, 10, d=1.2, cor=F.VEL, largura=8)
        E.ponto(c, t, C["s01.b"] + 1.2, P, 10, 20, None, guias=True, cor=F.VEL)
        E.frase(c, t, C["s01.a"], ps("parte do", "i", 76) + [("repouso", "g", 76)], XE, 300, passo=0.12)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: F.medida(c, 20, "m/s", XE, 450, 110, F.VEL, a))
        E.frase(c, t, C["s01.b"] + 0.7, ps("em", "i", 80) + [("10 s", "g", 80)], XE, 570, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("quantos", "i", 84) + [("metros?", "g", 84, COR)], XE, 740, passo=0.12)
        if t >= C["s01.e"]:
            F.area_graf(c, t, C["s01.e"], P, f, 0, 10, "? m")
        E.frase(c, t, C["s01.d"], ps("sem fórmula:", "i", 60, TINTA2) + [("área", "g", 60, COR)], XE, 880, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "a aceleração"), ("s02.c", "o deslocamento"), ("s02.d", "a mudança de v")))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def acel(a, x, y):
        E.formula(c, "a = f{Δv}{Δt}", x - 70, y + 20, 64, "g", F.ACEL, a, "center")

    def tri(a, x, y):
        p = skia.Path()
        p.moveTo(x - 110, y + 60); p.lineTo(x + 60, y + 60); p.lineTo(x + 60, y - 60); p.close()
        c.drawPath(p, M.paint(E.COR, 0.3 * a))
        c.drawPath(p, M.paint(TINTA, a, stroke=4))
    lembrete(c, t, C, "s03", (("s03.b", "aceleração:", "quanto v muda ÷ tempo", acel),
                              ("s03.c", "área do triângulo:", "base × altura ÷ 2", tri)))


# ---------------- ler o gráfico ----------------
def b_ler(c, t, C, b):
    def s04():
        P = gvt(c, t, C["s04"], 10, 20, 2, 5)
        if t >= C["s04.a"]:  # destaca o eixo do tempo
            q = ep(t, C["s04.a"], 0.4) * (1 - ep(t, C["s04.b"], 0.4))
            M.line(c, GX, P.oy, GX + GW + 30, P.oy, E.COR, q, 12)
        if t >= C["s04.b"]:
            q = ep(t, C["s04.b"], 0.4) * (1 - ep(t, C["s04.c"], 0.4))
            M.line(c, P.ox, GY + GH, P.ox, GY - 30, E.COR, q, 12)
        E.curva(c, t, C["s04.c"] - 0.6, P, reta(4, 16, 10), 0, 10, d=1.0, cor=F.VEL)
        E.ponto(c, t, C["s04.c"] + 0.4, P, 5, 10, None, guias=True, cor=F.VEL)
        E.frase(c, t, C["s04.a"], [("deitado:", "i", 70), ("tempo", "g", 70)], XE, 340)
        E.foco(c, t, C["s04.a"] + 0.5, 0.4, lambda a: E.formula(c, "(s)", XE, 420, 54, "b", F.UNID, a))
        E.frase(c, t, C["s04.b"], [("de pé:", "i", 70), ("velocidade", "g", 70, F.VEL)], XE, 540)
        E.foco(c, t, C["s04.b"] + 0.5, 0.4, lambda a: E.formula(c, "(m/s)", XE, 620, 54, "b", F.UNID, a))
        E.frase(c, t, C["s04.c"], ps("cada ponto:", "i", 60) + [("a", "i", 60), ("velocidade", "g", 60, COR)], XE, 760, passo=0.12)
        E.frase(c, t, C["s04.c"] + 0.8, ps("naquele instante", "g", 60, COR), XE, 840, passo=0.12)
        E.foco(c, t, C["s04.c"] + 1.0, 0.4, lambda a: E.pilula(c, "5 s → 10 m/s", P.x(5) + 30, P.y(10) - 80, 40, "b", fundo=F.VEL, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], ps("três jeitos da linha", "i", 76), W / 2, 200, "center", 0.12)
    casos = (("s05.a", reta(10, 10, 4), "uniforme", "v constante"), ("s05.b", reta(2, 18, 4), "acelera", "v aumenta"),
             ("s05.c", reta(18, 2, 4), "freia", "v diminui"))
    for i, (k, f, nome, sub) in enumerate(casos):
        x = 200 + i * 580
        P = gvt(c, t, C[k], 5, 20, 1, 5, "v", (x, 380, 420, 320), marcas_x=[], marcas_y=[])
        E.curva(c, t, C[k] + 0.4, P, f, 0, 4.6, d=0.8, cor=F.VEL, largura=8)
        E.frase(c, t, C[k] + 0.6, [(nome, "g", 64, COR)], x + 210, 900, "center")
        E.frase(c, t, C[k] + 0.9, [(sub, "i", 50, TINTA2)], x + 210, 975, "center")


# ---------------- inclinação ----------------
def b_inclinacao(c, t, C, b):
    P = gvt(c, t, C["s06"])
    f = reta(0, 20, 10)
    E.curva(c, t, C["s06"] + 0.3, P, f, 0, 10, d=1.0, cor=F.VEL, largura=8)
    E.frase(c, t, C["s06"], ps("no gráfico de posição:", "i", 50, TINTA2), XE, 230, passo=0.1)
    E.frase(c, t, C["s06"] + 1.6, [("inclinação", "g", 50, TINTA2), ("=", "g", 50, TINTA2), ("velocidade", "i", 54, TINTA2)], XE, 300, passo=0.1)
    E.frase(c, t, C["s06.a"], [("aqui:", "i", 72)], XE, 430)
    E.frase(c, t, C["s06.a"] + 0.4, [("inclinação", "g", 72), ("=", "g", 72, TINTA2)], XE, 520, passo=0.12)
    E.frase(c, t, C["s06.a"] + 0.9, [("aceleração", "g", 72, F.ACEL)], XE, 610)
    catetos(c, t, C["s06.c"], P, (0, 0), (10, 20), "20 m/s", "10 s", t1=C["s06.b"])
    def sobe():
        E.frase(c, t, C["s06.b"], [("quanto", "i", 54), ("sobe", "g", 54, COR)], XE, 750, passo=0.1)
        E.frase(c, t, C["s06.c"], [("÷", "g", 54), ("quanto", "i", 54), ("anda", "g", 54, COR)], XE, 830, passo=0.1)
    if t >= C["s06.b"] - 0.2:  # sobe ÷ anda
        E.saida(c, t, C["s07.c"] - 0.1, sobe)
    if t < C["s07"]:
        return
    # s07: a conta
    y = 820
    E.foco(c, t, C["s07.c"], 0.5, lambda a: E.formula(c, "a = f{20}{10} =", XE, y, 76, "g", TINTA, a))
    bola_txt(c, t, C["s07.d"], "2 m/s^2", XE + 560, y - 26, 110, 54, F.ACEL)
    E.frase(c, t, lerp(C["s07.d"], C["s07.end"], 0.45), ps("a cada segundo,", "i", 50, TINTA2) + [("+2 m/s", "g", 50, F.ACEL)], 1040, 960, "left", 0.1)


# ---------------- área ----------------
def b_area(c, t, C, b):
    def s08():
        P = gvt(c, t, C["s08"], 6, 15, 1, 5)
        f = lambda x: 10
        E.curva(c, t, C["s08.a"], P, f, 0, 5, d=0.8, cor=F.VEL, largura=8)
        if t >= C["s08.d"]:
            F.area_graf(c, t, C["s08.d"], P, f, 0, 5, "50 m")
        E.frase(c, t, C["s08.a"], [("v", "g", 76, F.VEL), ("=", "g", 76, TINTA2)], XE, 330, passo=0.1)
        E.foco(c, t, C["s08.a"] + 0.4, 0.5, lambda a: F.medida(c, 10, "m/s", XE + 160, 330, 76, TINTA, a))
        E.frase(c, t, C["s08.a"] + 1.2, [("durante", "i", 70), ("5 s", "g", 70)], XE, 440, passo=0.12)
        E.foco(c, t, C["s08.b"], 0.5, lambda a: E.formula(c, "d = v · t", XE, 590, 84, "g", TINTA, a))
        E.foco(c, t, C["s08.c"], 0.5, lambda a: (E.formula(c, "10 · 5 =", XE, 720, 84, "g", TINTA, a),
                                                 F.medida(c, 50, "m", XE + 30 + E.formula(None, "10 · 5 =", 0, 0, 84, a=0), 720, 84, COR, a)))
        E.frase(c, t, C["s08.d"], [("=", "g", 66, TINTA2), ("área", "g", 66, COR), ("do", "i", 70), ("retângulo", "i", 70)], XE, 860, passo=0.12)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if C["s09"] <= t < C["s10"]:
        def s09():
            P = gvt(c, t, C["s09"])
            f = reta(0, 20, 10)
            E.curva(c, t, C["s09"] + 0.2, P, f, 0, 10, d=0.8, cor=F.VEL, largura=8)
            E.frase(c, t, C["s09.a"], [("área", "g", 84, COR), ("=", "g", 84, TINTA2)], XE, 300, passo=0.12)
            E.frase(c, t, C["s09.a"] + 0.5, [("deslocamento", "g", 76)], XE, 400)
            if t >= C["s09.b"]:
                F.area_graf(c, t, C["s09.b"], P, f, 0, 10, None)
                E.foco(c, t, C["s09.b"] + 0.4, 0.4, lambda a: F.medida(c, "base", "10 s", P.x(5), P.oy + 120, 44, TINTA2, a, "center", cor_u=COR))
                E.foco(c, t, C["s09.b"] + 0.9, 0.4, lambda a: F.medida(c, "altura", "20 m/s", P.x(10) - 24, P.y(6), 44, TINTA2, a, "right", cor_u=COR))
            E.foco(c, t, C["s09.c"], 0.5, lambda a: E.formula(c, "f{10 · 20}{2} =", XE, 640, 84, "g", TINTA, a))
            bola_txt(c, t, C["s09.d"], "100 m", XE + 520, 620, 120, 62)
        E.saida(c, t, C["s10"] - 0.1, s09)
    if C["s10"] <= t < C["s11"]:
        def s10():
            P = gvt(c, t, C["s10"], 5, 35, 1, 10)
            f = reta(10, 30, 4)
            E.curva(c, t, C["s10.b"], P, f, 0, 4, d=0.8, cor=F.VEL, largura=8)
            if t >= C["s10.a"] + 0.3:
                F.area_graf(c, t, C["s10.a"] + 0.3, P, f, 0, 4, None)
            E.frase(c, t, C["s10.a"], [("trapézio", "g", 84, COR)], XE, 280)
            E.foco(c, t, C["s10.b"], 0.4, lambda a: E.pilula(c, "10 m/s", P.x(0.9), P.y(5), 38, "b", fundo=F.VEL, a=a))
            E.foco(c, t, C["s10.b"] + 0.8, 0.4, lambda a: E.pilula(c, "30 m/s", P.x(4) - 90, P.y(30) - 50, 38, "b", fundo=F.VEL, a=a))
            E.foco(c, t, C["s10.c"], 0.4, lambda a: F.medida(c, 4, "s", P.x(2), P.oy + 120, 50, COR, a, "center"))
            E.foco(c, t, C["s10.d"], 0.5, lambda a: E.formula(c, "f{(B + b) · h}{2}", XE, 470, 76, "g", TINTA, a))
            E.frase(c, t, lerp(C["s10.d"], C["s10.e"], 0.55), ps("bases = velocidades", "i", 46, TINTA2), XE, 590, passo=0.08)
            E.frase(c, t, lerp(C["s10.d"], C["s10.e"], 0.8), ps("altura = tempo", "i", 46, TINTA2), XE, 650, passo=0.08)
            E.foco(c, t, C["s10.e"], 0.5, lambda a: E.formula(c, "f{(30 + 10) · 4}{2} =", XE, 820, 72, "g", TINTA, a))
            bola_txt(c, t, C["s10.f"], "80 m", XE + 560, 800, 95, 56)
        E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    P = gvt(c, t, C["s11"], 6, 15, 1, 5, vmin=-15)
    f = reta(10, -10, 4)
    E.curva(c, t, C["s11"] + 0.2, P, f, 0, 4, d=0.8, cor=F.VEL, largura=8)
    if t >= C["s11.a"]:
        F.area_graf(c, t, C["s11.a"], P, f, 0, 2, None)
    if t >= C["s11.c"]:
        F.area_graf(c, t, C["s11.c"], P, f, 2, 4, None, cor=F.NEG)
        E.foco(c, t, C["s11.c"] + 0.6, 0.4, lambda a: (centro(c, "+", P.x(0.6), P.y(3) + 20, 80, "g", COR, a),
                                                       centro(c, "−", P.x(3.4), P.y(-5) + 20, 80, "g", F.NEG, a)))
    E.frase(c, t, C["s11.a"], ps("abaixo do eixo:", "i", 70), XE, 330, passo=0.12)
    E.frase(c, t, C["s11.a"] + 0.9, [("v", "g", 76, F.VEL), ("negativa", "g", 76)], XE, 440, passo=0.12)
    E.frase(c, t, C["s11.b"], [("está", "i", 76), ("voltando", "g", 76, F.NEG)], XE, 600, passo=0.12)
    E.frase(c, t, C["s11.c"], ps("a área conta com", "i", 60) + [("−", "g", 70, F.NEG)], XE, 760, passo=0.1)


# ---------------- gráfico a × t ----------------
def b_aceleracao(c, t, C, b):
    P = gvt(c, t, C["s12.a"], 6, 3, 1, 1, "a (m/s^2)")
    f = lambda x: 2
    E.curva(c, t, C["s12.b"], P, f, 0, 5, d=0.8, cor=F.ACEL, largura=8)
    if t >= C["s12.c"]:
        F.area_graf(c, t, C["s12.c"], P, f, 0, 5, None)
        E.foco(c, t, C["s12.d"], 0.4, lambda a: F.medida(c, 10, "m/s", P.x(2.5), P.y(1) + 20, 60, TINTA, a, "center"))
    E.frase(c, t, C["s12.a"], [("gráfico", "i", 80), ("a × t", "g", 80, F.ACEL)], XE, 280, passo=0.12)
    E.foco(c, t, C["s12.b"] + 0.3, 0.5, lambda a: F.medida(c, 2, "m/s^2", XE, 420, 76, F.ACEL, a))
    E.frase(c, t, C["s12.b"] + 1.0, [("durante", "i", 66), ("5 s", "g", 66)], XE, 520, passo=0.12)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "2 · 5 =", XE, 670, 84, "g", TINTA, a))
    E.foco(c, t, C["s12.d"], 0.5, lambda a: F.medida(c, 10, "m/s", XE + 300, 670, 84, COR, a))
    E.frase(c, t, C["s12.e"] - 1.2, [("não", "i", 60), ("é", "i", 60), ("distância", "g", 56, ERRADO)], XE, 800, passo=0.12)
    E.foco(c, t, C["s12.e"], 0.5, lambda a: E.pilula(c, "quanto v mudou", XE + 250, 900, 52, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    P = gvt(c, t, C["s13"])
    f = reta(0, 20, 10)
    E.curva(c, t, C["s13"] + 0.3, P, f, 0, 10, d=0.8, cor=F.VEL, largura=8)
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 230)
    E.frase(c, t, C["s13.a"], ps("ler velocidade", "i", 60) + [("como", "i", 60)], XE, 340, passo=0.1)
    E.frase(c, t, C["s13.a"] + 0.8, [("posição", "g", 60, ERRADO)], XE, 420)
    E.ponto(c, t, C["s13.b"], P, 10, 20, None, guias=True, cor=F.VEL)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.escreve(c, "a 20 m?", XE, 580, 100, "g", ERRADO, a))
    if t >= C["s13.d"]:
        E.risco(c, XE - 10, 600, XE + 380, 500, t, C["s13.d"], largura=12)
    E.foco(c, t, C["s13.d"] + 0.6, 0.5, lambda a: F.medida(c, 20, "m/s", XE, 700, 72, F.VEL, a))
    E.foco(c, t, C["s13.d"] + 0.8, 0.4, lambda a: E.escreve(c, "é a velocidade", XE + 300, 700, 48, "i", TINTA2, a))
    if t >= C["s13.e"]:
        F.area_graf(c, t, C["s13.e"], P, f, 0, 10, "100 m")
    E.frase(c, t, C["s13.e"] + 0.2, [("caminho", "i", 66), ("=", "g", 66, TINTA2), ("área", "g", 66, CERTO)], XE, 840, passo=0.12)
    if t >= C["s13.f"]:  # o nome do eixo de pé
        q = ep(t, C["s13.f"], 0.4)
        c.drawCircle(P.ox + 110, GY - 40, 100 + 6 * math.sin(t * 5), M.paint(E.COR, q, stroke=6))
        E.frase(c, t, C["s13.f"], ps("leia o eixo de pé", "g", 56, COR), XE, 960, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("o atalho:", "i", 76, CLARO) + [("a escada", "g", 76, BR)], W / 2, 160, "center", 0.12)
        degraus = (("s14.a", "s", "posição"), ("s14.b", "v", "velocidade"), ("s14.c", "a", "aceleração"))
        for i, (k, l, nome) in enumerate(degraus):
            x, y = 640 + i * 230, 330 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, x=x, y=y, l=l, nome=nome, i=i: (
                M.rrect(c, x, y, 560, 150, 18, E.mix(E.COR, "#07070F", 0.25 + 0.2 * i), a),
                E.escreve(c, l, x + 40, y + 108, 96, "g", BR, a),
                E.escreve(c, nome, x + 150, y + 98, 56, "i", BR, a)))
        if t >= C["s14.d"]:
            F.seta(c, 480, 420, 680, 780, CLARO, ep(t, C["s14.d"], 0.3), 12, p=ease_io(prog(t, C["s14.d"], 0.7)))
            E.foco(c, t, C["s14.d"] + 0.3, 0.4, lambda a: (E.escreve(c, "inclinação", 170, 640, 60, "g", BR, a),
                                                           E.escreve(c, "desce", 230, 710, 54, "i", CLARO, a)))
        if t >= C["s14.e"]:
            F.seta(c, 1500, 820, 1680, 450, E.COR, ep(t, C["s14.e"], 0.3), 12, p=ease_io(prog(t, C["s14.e"], 0.7)))
            E.foco(c, t, C["s14.e"] + 0.3, 0.4, lambda a: (E.escreve(c, "área", 1560, 360, 64, "g", BR, a),
                                                           E.escreve(c, "sobe", 1580, 290, 54, "i", CLARO, a)))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"], ps("por causa das", "i", 76, CLARO) + [("unidades", "g", 76, BR)], W / 2, 190, "center", 0.12)
    E.frase(c, t, C["s15.a"], [("inclinação:", "g", 64, BR)], 300, 400)
    E.formula_em(c, t, C["s15.a"] + 0.8, "f{m/s}{s} = m/s^2", 900, 400, 84, "g", CLARO)
    E.frase(c, t, C["s15.b"], [("área:", "g", 64, BR)], 300, 620)
    E.formula_em(c, t, C["s15.b"] + 0.8, "m/s · s = m", 900, 620, 84, "g", CLARO)
    E.frase(c, t, C["s15.c"], [("não", "g", 56, ERRADO), ("compensa:", "i", 60, CLARO)] + ps("linha abaixo do eixo, área com", "i", 60, CLARO) + [("−", "g", 66, BR)],
            W / 2, 880, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], [("ônibus:", "i", 72), ("parte", "i", 72), ("do", "i", 72), ("repouso", "g", 72)], XE, 330, passo=0.12)
    E.frase(c, t, C["s16.b"], [("0 →", "g", 66), ("12 m/s", "g", 66, F.VEL), ("em", "i", 70), ("6 s", "g", 66)], XE, 440, passo=0.14)
    E.frase(c, t, C["s16.c"], [("+ 10 s", "g", 66), ("a", "i", 70), ("12 m/s", "g", 66, F.VEL)], XE, 550, passo=0.14)
    E.frase(c, t, C["s16.d"], [("aceleração", "g", 64), ("no", "i", 66), ("começo?", "g", 64, COR)], XE, 720, passo=0.12)
    E.frase(c, t, C["s16.e"], [("distância", "g", 64), ("total?", "g", 64, COR)], XE, 830, passo=0.12)
    if t < C["s17"]:
        P = gvt(c, t, C["s16.a"], 18, 15, 2, 3, caixa=(1050, 250, 720, 480))
        f = lambda x: 2 * x if x <= 6 else 12
        E.curva(c, t, C["s16.b"], P, f, 0, 6, d=0.7, cor=F.VEL, largura=8)
        E.curva(c, t, C["s16.c"], P, f, 6, 16, d=0.7, cor=F.VEL, largura=8)
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    P = gvt(c, t, C["s18"], 18, 15, 2, 3, caixa=(860, 250, 900, 520))
    f = lambda x: 2 * x if x <= 6 else 12
    E.curva(c, t, C["s18"] + 0.2, P, f, 0, 16, d=0.9, cor=F.VEL, largura=8)

    def s18():
        catetos(c, t, C["s18.a"], P, (0, 0), (6, 12), "12 m/s", "6 s", t1=C["s18.a"] + 0.6)
        E.frase(c, t, C["s18.a"], [("inclinação", "g", 72)], XE, 330)
        E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "a = f{12}{6} =", XE, 520, 84, "g", TINTA, a))
        bola_txt(c, t, C["s18.c"], "2 m/s^2", XE + 300, 760, 120, 56, F.ACEL)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("a", "i", 72), ("área", "g", 72, COR)], XE, 260, passo=0.12)
    if t >= C["s19.a"]:
        F.area_graf(c, t, C["s19.a"], P, f, 0, 6, "36 m", size=44)
    E.foco(c, t, C["s19.a"], 0.5, lambda a: (E.formula(c, "f{6 · 12}{2} =", XE, 420, 64, "g", TINTA, a), F.medida(c, 36, "m", XE + 25 + E.formula(None, "f{6 · 12}{2} =", 0, 0, 64, a=0), 420, 64, COR, a)))
    if t >= C["s19.b"]:
        F.area_graf(c, t, C["s19.b"], P, f, 6, 16, "120 m", cor=F.VEL, size=52)
    E.foco(c, t, C["s19.b"], 0.5, lambda a: (E.formula(c, "10 · 12 =", XE, 560, 64, "g", TINTA, a), F.medida(c, 120, "m", XE + 25 + E.formula(None, "10 · 12 =", 0, 0, 64, a=0), 560, 64, F.VEL, a)))
    bola_txt(c, t, C["s19.c"], "156 m", XE + 230, 750, 120, 60)
    E.foco(c, t, C["s19.d"], 0.5, lambda a: E.formula(c, "trapézio: f{(16 + 10) · 12}{2} = 156", W / 2 + 120, 960, 60, "g", TINTA2, a, "center"))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = (("s20.a", [("inclinação", "g", 66), ("de", "i", 70), ("v × t", "g", 66, F.VEL), ("=", "g", 66, TINTA2), ("aceleração", "g", 66, F.ACEL)]),
             ("s20.b", [("área", "g", 66), ("de", "i", 70), ("v × t", "g", 66, F.VEL), ("=", "g", 66, TINTA2), ("deslocamento", "g", 66, COR)]),
             ("s20.c", [("área", "g", 66), ("de", "i", 70), ("a × t", "g", 66, F.ACEL), ("=", "g", 66, TINTA2), ("mudança de v", "g", 66, COR)]))

    def desenho():  # bola que cai, ganhando 10 m/s a cada segundo
        for k in range(1, 4):
            tk = C["s21.b"] + 0.35 * k
            y = 520 + 40 * k * k
            E.foco(c, t, tk, 0.3, lambda a, y=y, k=k: (E.bola(c, 420, y, 34, a=a * (1.0 if k == 3 else 0.35)),
                                                      F.medida(c, 10 * k, "m/s", 500, y + 16, 40, F.VEL, a)))
    fim(c, t, C, "s20", itens, "s21", [("s21.a", [("Queda", "g", 120, COR), ("livre", "g", 120, COR)])], desenho, "s21.c", "s21.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ler=b_ler, inclinacao=b_inclinacao, area=b_area, aceleracao=b_aceleracao,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
