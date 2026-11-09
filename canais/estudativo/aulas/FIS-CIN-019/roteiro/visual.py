"""Visual — Estudativo · FIS-CIN-019: velocidade angular e velocidade linear.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001/roteiro/visual.py e a do MOVIMENTO CIRCULAR do cabeçalho de
FIS-CIN-018/roteiro/visual.py (disco visto de cima, ponto laranja na borda, rastro em arco laranja).
Nesta aula: a velocidade linear é a seta petróleo (F.VEL) tangente ao círculo, com tamanho proporcional ao módulo; a
velocidade angular ω é o ângulo varrido, pintado como setor violeta (F.ACEL) a partir do raio inicial. O ponto da borda é
laranja; o ponto de perto do centro é tinta. π = 3 nas contas. Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-019_velocidade_angular_e_linear.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("linear", "angular", "ligacao", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OMEGA = F.ACEL

# todas as contas da aula (π = 3)
assert 2 * 3 * 3 == 18 and 18 / 6 == 3 and 2 * 3 * 1 / 6 == 1 and 2 * 3 / 6 == 1 and 1 * 3 == 3
assert 1 / 2 == 0.5 and 6 / 0.5 == 12 and 2 * 3 * 2 == 12 and abs(12 * 0.3 - 3.6) < 1e-9


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
def carrossel(c, cx, cy, R, ang, a=1.0, pontos=(), raios=4, escuro=False):
    """disco visto de cima girando (ang em graus, anti-horário); pontos = [(fração do raio, cor)]: ficam no mesmo raio"""
    if a <= 0:
        return []
    tinta = BR if escuro else TINTA
    c.drawCircle(cx, cy, R, M.paint("#FFF7EF" if not escuro else "#1A1A24", a))
    c.drawCircle(cx, cy, R, M.paint(tinta, a, stroke=5))
    for k in range(raios):
        g = math.radians(ang + 360 * k / raios)
        M.line(c, cx, cy, cx + math.cos(g) * R, cy - math.sin(g) * R, TINTA2 if k else tinta, a * (0.35 if k else 1.0), 3 if k else 4)
    c.drawCircle(cx, cy, 9, M.paint(tinta, a))
    g = math.radians(ang)
    pos = []
    for fr, cor in pontos:
        px, py = cx + math.cos(g) * R * fr, cy - math.sin(g) * R * fr
        E.bola(c, px, py, 22, cor, a)
        pos.append((px, py))
    return pos


def tangente(c, P, ang, L, a=1.0, cor=None, largura=9):
    """seta da velocidade linear num ponto do disco que gira no sentido anti-horário; ang = posição do ponto (graus)"""
    g = math.radians(ang)
    tx, ty = -math.sin(g), -math.cos(g)  # direção anti-horária na tela
    F.seta(c, P[0], P[1], P[0] + tx * L, P[1] + ty * L, cor or F.VEL, a, largura)


def setor(c, cx, cy, R, ini, varre, a=1.0, cor=None):
    """ângulo varrido a partir de ini (graus), anti-horário"""
    if a <= 0 or varre <= 0:
        return
    p = skia.Path()
    p.moveTo(cx, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - R, cy - R, 2 * R, 2 * R), -ini, -min(359.9, varre), False)
    p.close()
    c.drawPath(p, M.paint(cor or OMEGA, 0.22 * a))


def gira(t, t0, T):
    """ângulo (graus) de um disco que dá uma volta a cada T segundos a partir de t0, começando em 90°"""
    return 90 + 360 * max(0.0, t - t0) / T


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        cx, cy, R = 1400, 540, 330
        ang = gira(t, C["s01"], 5.0)
        E.foco(c, t, C["s01"], 0.5, lambda a: carrossel(c, cx, cy, R, ang, a, []))
        g = math.radians(ang)
        pos = [(cx + math.cos(g) * R * fr, cy - math.sin(g) * R * fr) for fr in (0.95, 0.33)]
        E.foco(c, t, C["s01.a"], 0.4, lambda a: E.bola(c, *pos[0], 24, None, a), blur=0)
        E.foco(c, t, C["s01.b"], 0.4, lambda a: E.bola(c, *pos[1], 24, TINTA, a), blur=0)
        if t >= C["s01.d"]:
            tangente(c, pos[0], ang, 220, ep(t, C["s01.d"], 0.4))
            tangente(c, pos[1], ang, 75, ep(t, C["s01.d"], 0.4))
        E.frase(c, t, C["s01.a"], [("borda", "g", 76, COR)], XE, 300)
        E.frase(c, t, C["s01.b"], ps("perto do", "i", 76) + [("centro", "g", 76)], XE, 410, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("1 volta no", "i", 66) + [("mesmo tempo", "g", 66)], XE, 580, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("a da borda é", "i", 66) + [("mais rápida", "g", 66, F.VEL)], XE, 700, passo=0.12)
        E.frase(c, t, C["s01.d"] + 1.6, [("como", "i", 90), ("pode?", "g", 90, COR)], XE, 880, passo=0.14)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "a velocidade angular"), ("s02.c", "a velocidade linear"), ("s02.d", "o mistério")))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "período:", "T = tempo de 1 volta", None), ("s03.c", "comprimento da circunferência:", "C = 2 · π · R", None),
                              ("s03.d", "1 volta inteira em radianos:", "2π rad", None)), num="3")


# ---------------- velocidade linear ----------------
def b_linear(c, t, C, b):
    cx, cy, R = 1480, 540, 300

    def s04():
        ang = gira(t, C["s04.c"], 4.0) if t >= C["s04.c"] else 90
        E.foco(c, t, C["s04"], 0.5, lambda a: carrossel(c, cx, cy, R, ang, a, [(1.0, None)]))
        if t >= C["s04.c"]:
            E.arco(c, cx, cy, R + 24, -90, min(359.9, (ang - 90) % 360 if t < C["s04.c"] + 4 else 359.9), E.COR, 8, ep(t, C["s04.c"], 0.3))
            E.foco(c, t, C["s04.c"] + 0.5, 0.4, lambda a: centro(c, "2πR", cx, cy - R - 60, 60, "g", COR, a))
        E.frase(c, t, C["s04.a"], [("velocidade", "g", 80, F.VEL), ("linear", "g", 80, F.VEL)], XE, 250, passo=0.12)
        E.formula_em(c, t, C["s04.b"], "v = f{distância}{tempo}", XE, 420, 72, "g", TINTA)
        E.frase(c, t, C["s04.c"], ps("1 volta:", "i", 60) + [("2πR", "g", 60, COR)], XE, 560, passo=0.1)
        E.frase(c, t, C["s04.d"], ps("no tempo de", "i", 60) + [("1 período, T", "g", 60)], XE, 650, passo=0.1)
        F.formula_legenda(c, t, C["s04.e"], "v = f{2 · π · R}{T}", [("v", "velocidade linear", "m/s")], XE, 830, 96, tl=[C["s04.e"] + 0.9])
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    ang = gira(t, C["s05"], 6.0)
    pos = carrossel(c, cx, cy, R, ang, ep(t, C["s05"], 0.4), [(1.0, None), (1 / 3, TINTA)])
    E.foco(c, t, C["s05.b"] + 0.4, 0.4, lambda a: tangente(c, pos[0], ang, 210, a))
    E.foco(c, t, C["s05.d"] + 0.4, 0.4, lambda a: tangente(c, pos[1], ang, 70, a))
    E.foco(c, t, C["s05.a"], 0.4, lambda a: (F.cronometro(c, 1840, 180, 50, 6, a, "T = 6 s")))
    E.frase(c, t, C["s05"], [("carrossel:", "i", 62), ("T = 6 s,", "g", 62), ("π = 3", "g", 62, TINTA2)], XE, 230, passo=0.12)
    E.frase(c, t, C["s05.b"], [("borda,", "g", 62, COR), ("R = 3 m:", "g", 62)], XE, 370, passo=0.12)
    E.formula_em(c, t, C["s05.b"] + 0.8, "f{2 · 3 · 3}{6} = f{18}{6} =", XE, 490, 70, "g", TINTA)
    bola_txt(c, t, C["s05.c"], "3 m/s", XE + 760, 465, 90, 50, F.VEL)
    E.frase(c, t, C["s05.d"], [("perto,", "g", 62), ("R = 1 m:", "g", 62)], XE, 660, passo=0.12)
    E.formula_em(c, t, C["s05.d"] + 0.8, "f{2 · 3 · 1}{6} = f{6}{6} =", XE, 780, 70, "g", TINTA)
    bola_txt(c, t, C["s05.e"], "1 m/s", XE + 760, 755, 90, 50, F.VEL)
    if t >= C["s06"]:
        E.frase(c, t, C["s06.a"], [("mesmo", "i", 60), ("tempo,", "i", 60), ("caminho", "g", 60), ("3×", "g", 60, COR), ("maior", "g", 60)], XE, 950, passo=0.12)


# ---------------- velocidade angular ----------------
def b_angular(c, t, C, b):
    cx, cy, R = 1460, 560, 300
    ang = gira(t, C["s07.a"], 6.0) if t >= C["s07.a"] else 90
    if t >= C["s07.a"]:
        setor(c, cx, cy, R * 0.98, 90, min(359.9, ang - 90), ep(t, C["s07.a"], 0.3))
    carrossel(c, cx, cy, R, ang, ep(t, C["s07"], 0.4), [(1.0, None), (1 / 3, TINTA)])
    M.line(c, cx, cy, cx, cy - R, TINTA2, 0.6 * ep(t, C["s07.a"], 0.3), 3, dash=E.TRACO) if t >= C["s07.a"] else None

    def s07():
        E.frase(c, t, C["s07"], ps("algo igual para as duas:", "i", 60), XE, 230, passo=0.1)
        E.frase(c, t, C["s07.a"], ps("o", "i", 76) + [("ângulo", "g", 76, OMEGA)] + ps("que giram", "i", 76), XE, 350, passo=0.12)
        E.frase(c, t, C["s07.b"], ps("6 s: uma volta,", "i", 56, TINTA2) + [("2π rad", "g", 56, OMEGA)], XE, 450, passo=0.1)
        E.frase(c, t, C["s07.c"], [("velocidade", "g", 70, OMEGA), ("angular", "g", 70, OMEGA)], XE, 600, passo=0.12)
        E.foco(c, t, C["s07.d"], 0.5, lambda a: E.escreve(c, "ω", XE, 830, 230, "g", OMEGA, a))
        E.formula_em(c, t, C["s07.e"], "= f{ângulo}{tempo}", XE + 210, 790, 76, "g", TINTA)
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    F.formula_legenda(c, t, C["s08.a"], "ω = f{2 · π}{T}", [("ω", "velocidade angular", "rad/s")], XE, 330, 110, tl=[C["s08.b"]])
    E.formula_em(c, t, C["s08.c"], "f{2 · 3}{6} =", XE, 670, 80, "g", TINTA)
    bola_txt(c, t, C["s08.d"], "1 rad/s", XE + 470, 645, 100, 44, OMEGA)
    E.foco(c, t, C["s08.e"], 0.5, lambda a: E.pilula(c, "igual para todos os pontos", XE + 400, 860, 50, "g", fundo=OMEGA, a=a))


# ---------------- v = ω·R ----------------
def b_ligacao(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09"], ps("junte as duas", "i", 70), XE, 220, passo=0.12)
        E.formula_em(c, t, C["s09.a"], "v = f{2 · π · R}{T}", XE, 400, 96, "g", TINTA)
        E.formula_em(c, t, C["s09.b"], "= f{2 · π}{T} · R", XE + 620, 400, 96, "g", TINTA)
        if t >= C["s09.c"]:
            q = ep(t, C["s09.c"], 0.4)
            x0 = XE + 620 + E.formula(None, "= ", 0, 0, 96, "g", a=0)
            w = E.formula(None, "f{2 · π}{T}", 0, 0, 96, "g", a=0)
            M.rrect(c, x0 - 10, 280, w + 20, 170, 16, OMEGA, 0.18 * q)
            E.foco(c, t, C["s09.c"] + 0.2, 0.4, lambda a: centro(c, "= ω", x0 + w / 2, 520, 64, "g", OMEGA, a))
        E.foco(c, t, C["s09.d"], 0.6, lambda a: (E.bola(c, W / 2, 780, 200, a=a), E.formula(c, "v = ω · R", W / 2, 810, 84, "g", BR, a, "center")))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if C["s10"] <= t < C["s11"]:
        def s10():
            E.formula_em(c, t, C["s10"], "v = ω · R", XE, 260, 120, "g", TINTA)
            for i, (k, l, nome, u, cor) in enumerate((("s10.a", "v", "velocidade linear", "m/s", F.VEL), ("s10.b", "ω", "velocidade angular", "rad/s", OMEGA),
                                                      ("s10.c", "R", "distância até o centro", "m", COR))):
                y = 400 + i * 90
                E.foco(c, t, C[k], 0.4, lambda a, y=y, l=l, nome=nome, u=u, cor=cor: (E.escreve(c, l, XE, y, 64, "g", cor, a), E.escreve(c, nome, XE + 90, y, 56, "i", TINTA, a),
                                                                                    E.formula(c, f"({u})", XE + 100 + E.larg(nome, "i", 56) + 20, y, 50, "b", F.UNID, a)))
            E.formula_em(c, t, C["s10.d"], "borda: 1 · 3 = 3 m/s", XE, 760, 72, "g", CERTO)
            E.frase(c, t, C["s10.e"], [("ω", "g", 66, OMEGA), ("igual,", "i", 66), ("R", "g", 66, COR), ("maior", "i", 66), ("→", "g", 66), ("v", "g", 66, F.VEL), ("maior", "g", 66)],
                    XE, 900, passo=0.12)
            cx, cy, R = 1520, 560, 270
            ang = gira(t, C["s10"], 6.0)
            pos = carrossel(c, cx, cy, R, ang, ep(t, C["s10"], 0.4), [(1.0, None), (1 / 3, TINTA)])
            tangente(c, pos[0], ang, 200, ep(t, C["s10.e"], 0.4))
            tangente(c, pos[1], ang, 66, ep(t, C["s10.e"], 0.4))
        E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    # s11: a direção da velocidade é tangente
    cx, cy, R = 820, 560, 280
    ang_solta = 150.0
    ang = min(ang_solta, gira(t, C["s11"], 6.0) + 0) if t < C["s11.a"] else ang_solta
    carrossel(c, cx, cy, R, ang if t < C["s11.a"] else ang_solta, 1.0, [])
    g = math.radians(ang_solta)
    P = (cx + math.cos(g) * R, cy - math.sin(g) * R)
    if t < C["s11.a"]:
        E.bola(c, cx + math.cos(math.radians(ang)) * R, cy - math.sin(math.radians(ang)) * R, 22)
    else:
        u = ease_out(prog(t, C["s11.a"], 1.6))
        tx, ty = -math.sin(g), -math.cos(g)
        M.line(c, P[0] - tx * 400, P[1] - ty * 400, P[0] + tx * 600, P[1] + ty * 600, TINTA2, 0.6 * ep(t, C["s11.b"], 0.4), 4, dash=E.TRACO) if t >= C["s11.b"] else None
        E.bola(c, P[0] + tx * 520 * u, P[1] + ty * 520 * u, 22)
        tangente(c, P, ang_solta, 200, ep(t, C["s11.a"], 0.3))
        if t >= C["s11.c"]:  # ângulo reto com o raio
            E.angulo(c, t, C["s11.c"], P, (cx, cy), (P[0] + tx * 200, P[1] + ty * 200), None, r=44, reto=True)
    E.frase(c, t, C["s11"], ps("e a direção?", "i", 70), 1300, 260, passo=0.12)
    E.frase(c, t, C["s11.a"], ps("sai pela", "i", 66) + [("tangente", "g", 66, F.VEL)], 1300, 400, passo=0.12)
    E.frase(c, t, C["s11.b"], ps("só encosta no círculo", "i", 50, TINTA2), 1300, 490, passo=0.1)
    E.frase(c, t, C["s11.c"], [("90°", "g", 56, COR)] + ps("com o raio", "i", 56), 1300, 580, passo=0.1)
    E.frase(c, t, C["s11.d"], ps("v linear: sempre assim", "g", 50, F.VEL), 1300, 700, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s12.a"], ps("a da borda", "i", 72) + [("gira", "g", 72, ERRADO)] + ps("mais rápido?", "i", 72), XE, 350, passo=0.12)
    if t >= C["s12.b"]:
        E.risco(c, XE + 330, 370, XE + 560, 290, t, C["s12.b"], largura=10)
    E.frase(c, t, C["s12.b"], ps("girar, giram", "i", 66) + [("igual", "g", 66, CERTO)], XE, 520, passo=0.12)
    E.frase(c, t, C["s12.c"], [("mesmo", "g", 66, OMEGA), ("ω", "g", 76, OMEGA)], XE, 640, passo=0.12)
    E.frase(c, t, C["s12.d"], ps("o que muda:", "i", 66) + [("v", "g", 76, F.VEL)], XE, 780, passo=0.12)
    E.frase(c, t, C["s12.d"] + 1.6, ps("leia qual das duas a questão pede", "i", 54, TINTA2), XE, 910, passo=0.1)
    cx, cy, R = 1480, 560, 280
    ang = gira(t, C["s12"], 6.0)
    pos = carrossel(c, cx, cy, R, ang, ep(t, C["s12"], 0.4), [(1.0, None), (1 / 3, TINTA)])
    if t >= C["s12.c"]:
        setor(c, cx, cy, R * 0.98, ang - 60, 60, ep(t, C["s12.c"], 0.3))
    tangente(c, pos[0], ang, 190, ep(t, C["s12.d"], 0.4))
    tangente(c, pos[1], ang, 63, ep(t, C["s12.d"], 0.4))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("o atalho:", "i", 76, CLARO), W / 2, 170, "center")
        E.frase(c, t, C["s13.a"], ps("no mesmo corpo,", "i", 64, CLARO) + [("v", "g", 70, BR)] + ps("é proporcional a", "i", 64, CLARO) + [("R", "g", 70, BR)],
                W / 2, 300, "center", 0.1)
        # barras: R = 1, 2, 3 → v = 1, 2, 3
        for i in range(3):
            ti = C["s13.b"] + 0.4 * i
            q = ease_io(prog(t, ti, 0.5))
            if q > 0:
                x, yb = 640 + i * 320, 880
                M.rrect(c, x, yb - 120 * (i + 1) * q, 180, 120 * (i + 1) * q, 14, E.COR, 0.9)
                centro(c, f"R = {i + 1}", x + 90, yb + 60, 50, "g", CLARO, q)
                centro(c, f"v = {i + 1}", x + 90, yb - 120 * (i + 1) * q - 24, 50, "g", BR, q)
        E.frase(c, t, C["s13.c"], ps("3 m anda", "i", 56, CLARO) + [("3×", "g", 56, BR)] + ps("mais que 1 m", "i", 56, CLARO), W / 2, 1010, "center", 0.1)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], [("ω", "g", 80, BR)] + ps("é o mesmo no corpo todo", "i", 70, CLARO), W / 2, 280, "center", 0.12)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: centro(c, "v = ω · R", W / 2, 450, 110, "g", BR, a))
    E.frase(c, t, C["s14.c"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("rodas diferentes", "g", 62, BR), W / 2, 650, "center", 0.1)
    for j, (x, r) in enumerate(((760, 120), (1140, 200))):
        E.foco(c, t, C["s14.c"] + 0.6 + 0.2 * j, 0.5, lambda a, x=x, r=r, j=j: carrossel(c, x, 860, r * 0.7, 90 + (t - C["s14.c"]) * (200 if j == 0 else 120), a, [], escuro=True))
    E.foco(c, t, C["s14.c"] + 1.4, 0.4, lambda a: E.escreve(c, "próxima aula", 1340, 880, 56, "i", CLARO, a))


# ---------------- questão ----------------
def roda(c, cx, cy, R, ang, a=1.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy, R, M.paint("#1B1B20", a, stroke=R * 0.09))
    for k in range(12):
        g = math.radians(ang + 30 * k)
        M.line(c, cx, cy, cx + math.cos(g) * R * 0.95, cy - math.sin(g) * R * 0.95, TINTA2, a, 2)
    c.drawCircle(cx, cy, R * 0.08, M.paint(TINTA, a))
    g = math.radians(ang)
    E.bola(c, cx + math.cos(g) * R, cy - math.sin(g) * R, 18, None, a)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], ps("roda de bicicleta", "i", 72), XE, 330, passo=0.12)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: (E.escreve(c, "R =", XE, 450, 72, "g", TINTA, a), F.medida(c, "0,3", "m", XE + 140, 450, 72, COR, a)))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: (E.escreve(c, "f =", XE + 480, 450, 72, "g", TINTA, a), F.medida(c, 2, "Hz", XE + 600, 450, 72, OMEGA, a)))
    E.frase(c, t, C["s15.d"], [("velocidade", "g", 64), ("angular", "g", 64, OMEGA), ("ω?", "g", 64, OMEGA)], XE, 640, passo=0.12)
    E.frase(c, t, C["s15.e"], [("velocidade", "g", 64), ("linear", "g", 64, F.VEL), ("na", "i", 66), ("borda?", "g", 64, F.VEL)], XE, 760, passo=0.12)
    E.frase(c, t, C["s15.e"] + 1.4, [("use", "i", 54, TINTA2), ("π = 3", "b", 50, TINTA2)], XE, 870, passo=0.1)
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"], 0.5, lambda a: roda(c, 1480, 560, 280, gira(t, C["s15.a"], 0.5), a))
    else:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s17.a"], [("2 Hz:", "g", 66, OMEGA)] + ps("2 voltas por segundo", "i", 66), XE, 240, passo=0.12)
    E.formula_em(c, t, C["s17.b"], "T = f{1}{2} = 0,5 s", XE, 380, 72, "g", COR)
    E.formula_em(c, t, C["s17.c"], "ω = f{2 · 3}{0,5} =", XE, 560, 80, "g", TINTA)
    bola_txt(c, t, C["s17.d"], "12 rad/s", XE + 680, 535, 110, 46, OMEGA)
    E.formula_em(c, t, C["s18.a"], "v = 12 · 0,3 =", XE, 760, 80, "g", TINTA)
    bola_txt(c, t, C["s18.b"], "3,6 m/s", XE + 680, 735, 110, 48, F.VEL)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "atalho: ω = 2 · π · f = 2 · 3 · 2 = 12", XE + 560, 930, 46, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s17"], 0.5, lambda a: roda(c, 1560, 540, 230, gira(t, C["s17"], 0.5), a))


# ---------------- fechamento ----------------
def polias(c, t, t0, x1, x2, y, r1, r2, a=1.0):
    """duas polias ligadas por correia (vista de frente)"""
    if a <= 0:
        return
    for x, r in ((x1, r1), (x2, r2)):
        c.drawCircle(x, y, r, M.paint("#FFF7EF", a))
        c.drawCircle(x, y, r, M.paint(TINTA, a, stroke=5))
        c.drawCircle(x, y, 8, M.paint(TINTA, a))
    M.line(c, x1, y - r1, x2, y - r2, E.COR, a, 6)
    M.line(c, x1, y + r1, x2, y + r2, E.COR, a, 6)


def b_fim(c, t, C, b):
    itens = (("s19.a", [("ω = 2π ÷ T,", "g", 64, OMEGA), ("igual", "i", 66), ("no", "i", 66), ("corpo", "i", 66), ("todo", "i", 66)]),
             ("s19.b", [("v = ω · R", "g", 64, F.VEL)]),
             ("s19.c", [("mais", "i", 66), ("longe", "i", 66), ("do", "i", 66), ("centro", "i", 66), ("→", "g", 64), ("mais", "g", 64), ("rápido", "g", 64, F.VEL)]))

    def desenho():
        E.foco(c, t, C["s20.a"], 0.5, lambda a: polias(c, t, C["s20.a"], 300, 640, 820, 70, 140, a))
        E.frase(c, t, C["s20.b"], ps("e as marchas da bicicleta", "i", 56), 840, 830, passo=0.1)
    fim(c, t, C, "s19", itens, "s20", [("s20.a", [("Correias,", "g", 100, COR)]), ("s20.a", [("engrenagens", "g", 100, COR), ("e", "i", 100), ("eixos", "g", 100, COR)])],
        desenho, "s20.c", "s20.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, linear=b_linear, angular=b_angular, ligacao=b_ligacao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
