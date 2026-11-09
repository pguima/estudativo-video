"""Visual — Estudativo · FIS-CIN-020: correias, engrenagens e eixos.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001/roteiro/visual.py e a do MOVIMENTO CIRCULAR do cabeçalho de
FIS-CIN-018/roteiro/visual.py. Nesta aula: polias e engrenagens vistas de frente, giram de verdade (a correia anda com
traços que correm; cada polia gira com ω = v/R). Correia e corrente em tinta; o que é IGUAL na ligação vem em pílula:
velocidade linear igual em petróleo (F.VEL), velocidade angular/frequência igual em violeta (F.ACEL).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-020_correias_engrenagens_eixos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("correia", "engrenagem", "eixo", "bicicleta", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FREQ = F.ACEL

# todas as contas da aula (π = 3)
assert 30 * 5 / 15 == 10 and 1800 * 5 / 15 == 600 and 10 * 60 == 600 and 30 * 60 == 1800
assert 48 / 16 == 3 and abs(2 * 3 * 0.3 * 3 - 5.4) < 1e-9
assert 40 / 10 == 4 and abs(2 * 3 * 4 * 0.3 - 7.2) < 1e-9


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
def polia(c, cx, cy, r, ang, a=1.0, cor=None, raios=3, escuro=False, marca=True):
    """polia de frente: aro na cor, raios girando (ang em graus) e uma marca laranja na borda"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA
    c.drawCircle(cx, cy, r, M.paint("#FFF7EF" if not escuro else "#1A1A24", a))
    c.drawCircle(cx, cy, r, M.paint(cor or tinta, a, stroke=max(6, r * 0.08)))
    for k in range(raios):
        g = math.radians(ang + 360 * k / raios)
        M.line(c, cx, cy, cx + math.cos(g) * r * 0.9, cy - math.sin(g) * r * 0.9, tinta, a * 0.7, 4)
    c.drawCircle(cx, cy, max(8, r * 0.08), M.paint(tinta, a))
    if marca:
        g = math.radians(ang)
        E.bola(c, cx + math.cos(g) * r, cy - math.sin(g) * r, max(12, r * 0.09), None, a)


def engrenagem(c, cx, cy, r, n, ang, a=1.0, cor=None, escuro=False):
    """engrenagem de n dentes e raio r (até a ponta dos dentes); ang em graus"""
    if a <= 0:
        return
    cor = cor or (TINTA2 if not escuro else "#5A5A66")
    p = skia.Path()
    h = r * 0.14 if n > 14 else r * 0.2
    for k in range(n * 4 + 1):
        g = math.radians(ang + 360 * k / (n * 4))
        rr = r if (k % 4) in (1, 2) else r - h
        x, y = cx + math.cos(g) * rr, cy - math.sin(g) * rr
        p.moveTo(x, y) if k == 0 else p.lineTo(x, y)
    p.close()
    c.drawPath(p, M.paint(cor, a))
    c.drawCircle(cx, cy, r * 0.55, M.paint("#FFF7EF" if not escuro else "#1A1A24", a))
    c.drawCircle(cx, cy, r * 0.12, M.paint(cor, a))
    g = math.radians(ang)
    E.bola(c, cx + math.cos(g) * (r - h * 1.5), cy - math.sin(g) * (r - h * 1.5), max(10, r * 0.08), None, a)


def tangentes(A, ra, B, rb):
    """pontos das duas tangentes externas (correia aberta) entre os círculos A e B"""
    dx, dy = B[0] - A[0], B[1] - A[1]
    d = math.hypot(dx, dy)
    th = math.atan2(dy, dx)
    phi = math.acos(max(-1.0, min(1.0, (ra - rb) / d)))
    out = []
    for s in (1, -1):
        al = th + s * phi
        out.append(((A[0] + ra * math.cos(al), A[1] + ra * math.sin(al)), (B[0] + rb * math.cos(al), B[1] + rb * math.sin(al))))
    return out


def correia(c, A, ra, B, rb, fase, a=1.0, cor=None, largura=8):
    """correia aberta em volta de A e B: dois trechos retos com traços que correm (fase em pixels)"""
    if a <= 0:
        return
    cor = cor or TINTA
    for i, (P, Q) in enumerate(tangentes(A, ra, B, rb)):
        pt = M.paint(cor, a, stroke=largura)
        pt.setPathEffect(skia.DashPathEffect.Make([34, 16], (fase if i == 0 else -fase) % 50))
        path = skia.Path(); path.moveTo(*P); path.lineTo(*Q)
        c.drawPath(path, pt)
    for X, r in ((A, ra), (B, rb)):
        c.drawCircle(X[0], X[1], r + largura / 2, M.paint(cor, a * 0.85, stroke=largura * 0.5))


def roda_bike(c, cx, cy, R, ang, a=1.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy, R, M.paint("#1B1B20", a, stroke=R * 0.07))
    for k in range(16):
        g = math.radians(ang + 22.5 * k)
        M.line(c, cx, cy, cx + math.cos(g) * R * 0.96, cy - math.sin(g) * R * 0.96, TINTA2, a * 0.6, 2)
    g = math.radians(ang)
    E.bola(c, cx + math.cos(g) * R, cy - math.sin(g) * R, 16, None, a)


def transmissao(c, t, x1, x2, y, r1, r2, n1, n2, R, giros_pedal, a=1.0, pedal=True):
    """bicicleta: coroa (x1, r1, n1 dentes) com pedal, corrente, catraca (x2, r2) no eixo da roda de raio R.
    giros_pedal = quantas voltas o pedal já deu"""
    if a <= 0:
        return
    ang1 = 90 - 360 * giros_pedal
    ang2 = 90 - 360 * giros_pedal * n1 / n2
    roda_bike(c, x2, y, R, ang2, a * 0.9)
    correia(c, (x1, y), r1, (x2, y), r2, 360 * giros_pedal * r1 * math.pi / 180, a, TINTA, 7)
    engrenagem(c, x1, y, r1, n1 // 2, ang1, a, E.COR)
    engrenagem(c, x2, y, r2, max(8, n2 // 2), ang2, a, E.COR)
    if pedal:
        g = math.radians(ang1 + 180)
        P = (x1 + math.cos(g) * r1 * 1.3, y - math.sin(g) * r1 * 1.3)
        M.line(c, x1, y, *P, TINTA, a, 12)
        M.rrect(c, P[0] - 34, P[1] - 10, 68, 20, 6, TINTA, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        u = max(0.0, min(1.0, (t - C["s01.a"]) / max(0.5, C["s01.b"] + 0.8 - C["s01.a"]))) if t >= C["s01.a"] else 0
        transmissao(c, t, 1000, 1500, 600, 150, 50, 48, 16, 300, ease_io(u), ep(t, C["s01"], 0.5))
        E.frase(c, t, C["s01.a"], [("1", "g", 120, COR), ("pedalada", "i", 80)], XE, 330, passo=0.12)
        E.frase(c, t, C["s01.b"], [("3", "g", 120, COR), ("voltas", "i", 80), ("da", "i", 80), ("roda", "i", 80)], XE, 480, passo=0.12)
        E.frase(c, t, C["s01.c"], [("como?", "g", 90)], XE, 660)
        E.foco(c, t, C["s01.d"], 0.5, lambda a: (E.pilula(c, "corrente", 1250, 880, 46, "g", fundo=TINTA, a=a),
                                                 E.pilula(c, "rodas dentadas", 1250, 960, 46, "g", fundo=E.COR, a=a)))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "polias com correia"), ("s02.c", "engrenagens"), ("s02.d", "rodas no mesmo eixo"), ("s02.e", "a bicicleta")), size=70)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "velocidade linear:", "v = ω · R", None), ("s03.c", "velocidade angular:", "ω = 2 · π · f", None)))


# ---------------- correia ----------------
def b_correia(c, t, C, b):
    A, ra, B, rb = (1080, 560), 80, (1560, 560), 240
    vbelt = 160.0  # px/s
    s = max(0.0, t - C["s04"]) * vbelt
    angA, angB = 90 - math.degrees(s / ra), 90 - math.degrees(s / rb)

    def cena():
        E.foco(c, t, C["s04"], 0.5, lambda a: (polia(c, *A, ra, angA, a), polia(c, *B, rb, angB, a)))
        if t >= C["s04.b"]:
            correia(c, A, ra, B, rb, s, ep(t, C["s04.b"], 0.4))
        if t >= C["s04.d"]:
            q = ep(t, C["s04.d"], 0.4)
            for X, r in ((A, ra), (B, rb)):
                c.drawCircle(X[0], X[1], r + 20, M.paint(F.VEL, q, stroke=5))
        E.foco(c, t, C["s04"] + 0.3, 0.4, lambda a: (centro(c, "menor", A[0], A[1] + ra + 90, 44, "i", TINTA2, a), centro(c, "maior", B[0], B[1] + rb + 80, 44, "i", TINTA2, a)))
    cena()

    def s04():
        E.frase(c, t, C["s04"], [("polia", "g", 90, COR)], XE, 260)
        E.frase(c, t, C["s04.a"], ps("roda presa a um eixo", "i", 58), XE, 350, passo=0.1)
        E.frase(c, t, C["s04.b"], [("correia", "g", 70), ("sem", "i", 70), ("escorregar", "i", 70)], XE, 500, passo=0.12)
        E.frase(c, t, C["s04.c"], ps("a borda anda com a correia", "i", 54), XE, 620, passo=0.1)
        E.foco(c, t, C["s04.d"], 0.5, lambda a: E.pilula(c, "v igual nas duas", XE + 270, 760, 56, "g", fundo=F.VEL, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.formula_em(c, t, C["s05.a"], "v = ω · R", XE, 300, 90, "g", TINTA)
            E.frase(c, t, C["s05.b"], ps("mesmo v:", "i", 60) + [("raio menor", "g", 60), ("→", "g", 60), ("gira", "i", 60), ("mais", "g", 60, COR)], XE, 440, passo=0.1)
            E.formula_em(c, t, C["s05.b"] + 2.0, "ω₁ · R₁ = ω₂ · R₂", XE, 580, 76, "g", TINTA)
            E.formula_em(c, t, lerp(C["s05.b"], C["s05.c"], 0.6), "2π · f₁ · R₁ = 2π · f₂ · R₂", XE, 720, 62, "g", TINTA2)
            if t >= C["s05.c"] - 0.6:
                for x0 in (XE, XE + E.formula(None, "2π · f₁ · R₁ = ", 0, 0, 62, "g", a=0)):
                    E.risco(c, x0 - 4, 730, x0 + E.formula(None, "2π", 0, 0, 62, "g", a=0) + 4, 680, t, C["s05.c"] - 0.6, largura=7)
            E.foco(c, t, C["s05.c"], 0.6, lambda a: (E.bola(c, XE + 330, 880, 70, F.VEL, a), centro(c, "=", XE + 330, 905, 70, "g", BR, a),
                                                     E.formula(c, "f₁ · R₁ = f₂ · R₂", XE + 430, 905, 70, "g", COR, a)))
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.foco(c, t, C["s06.a"], 0.5, lambda a: (E.escreve(c, "motor:", XE, 300, 60, "i", TINTA, a), F.medida(c, 5, "cm", XE + 200, 300, 70, TINTA, a),
                                             F.medida(c, 30, "Hz", XE + 420, 300, 70, FREQ, a)))
    E.foco(c, t, C["s06.b"], 0.5, lambda a: (E.escreve(c, "puxa:", XE, 410, 60, "i", TINTA, a), F.medida(c, 15, "cm", XE + 200, 410, 70, TINTA, a),
                                             F.medida(c, "?", "Hz", XE + 420, 410, 70, FREQ, a)))
    E.formula_em(c, t, C["s06.c"], "30 · 5 = f · 15", XE, 580, 80, "g", TINTA)
    bola_txt(c, t, C["s06.d"], "10 Hz", XE + 220, 760, 100, 54, FREQ)
    E.frase(c, t, C["s06.e"], [("3×", "g", 60, COR), ("maior", "i", 60), ("→", "g", 60), ("3×", "g", 60, COR), ("mais", "i", 60), ("devagar", "i", 60)], XE, 950, passo=0.1)


# ---------------- engrenagem ----------------
def b_engrenagem(c, t, C, b):
    A, ra, na, B, rb, nb = (1060, 560), 110, 10, (1060 + 110 + 300 - 22, 560), 300, 30
    s = max(0.0, t - C["s07"]) * 100.0
    angA = 90 - math.degrees(s / ra)
    angB = 90 + math.degrees(s / rb) + 6
    E.foco(c, t, C["s07"], 0.5, lambda a: (engrenagem(c, *A, ra, na, angA, a, E.COR), engrenagem(c, *B, rb, nb, angB, a, TINTA2)))
    if t >= C["s07.d"]:
        q = ep(t, C["s07.d"], 0.4)
        E.arco(c, A[0], A[1], ra + 50, 120, 120, E.COR, 7, q)
        E.arco(c, B[0], B[1], rb + 40, 60, -60, TINTA2, 7, q)
        E.foco(c, t, C["s07.d"] + 0.3, 0.4, lambda a: (centro(c, "horário", A[0], A[1] - ra - 80, 42, "i", COR, a), centro(c, "anti-horário", B[0], B[1] - rb - 60, 42, "i", TINTA2, a)))
    E.foco(c, t, C["s07.e"], 0.4, lambda a: (centro(c, "10 dentes", A[0], A[1] + ra + 80, 46, "g", COR, a), centro(c, "30 dentes", B[0], B[1] + rb + 70, 46, "g", TINTA, a)))
    E.frase(c, t, C["s07.a"], [("engrenagens", "g", 80, COR)], XE, 260)
    E.frase(c, t, C["s07.b"], ps("dente empurra dente", "i", 58), XE, 380, passo=0.1)
    E.frase(c, t, C["s07.c"], [("bordas", "g", 58), ("juntas:", "i", 58)], XE, 480, passo=0.1)
    E.foco(c, t, C["s07.c"] + 0.8, 0.4, lambda a: E.pilula(c, "v igual", XE + 450, 465, 46, "g", fundo=F.VEL, a=a))
    E.frase(c, t, C["s07.d"], ps("uma gira para cada lado", "g", 54), XE, 620, passo=0.1)
    E.frase(c, t, C["s07.e"], ps("raio pode vir como", "i", 54) + [("dentes", "g", 54, COR)], XE, 760, passo=0.1)


# ---------------- eixo ----------------
def b_eixo(c, t, C, b):
    cx, cy, R1, R2 = 1420, 560, 120, 320
    ang = 90 - max(0.0, t - C["s08"]) * 45
    E.foco(c, t, C["s08.a"], 0.5, lambda a: (polia(c, cx, cy, R2, ang, a, marca=False), polia(c, cx, cy, R1, ang, a, E.COR, marca=False)))
    g = math.radians(ang)
    P1, P2 = (cx + math.cos(g) * R1, cy - math.sin(g) * R1), (cx + math.cos(g) * R2, cy - math.sin(g) * R2)
    if t >= C["s08.a"]:
        q = ep(t, C["s08.a"], 0.4)
        E.bola(c, *P1, 16, TINTA, q)
        E.bola(c, *P2, 20, None, q)
    if t >= C["s08.d"]:
        tx, ty = -math.sin(g), -math.cos(g)
        q = ep(t, C["s08.d"], 0.4)
        F.seta(c, P1[0], P1[1], P1[0] + tx * 70, P1[1] + ty * 70, F.VEL, q, 8)
        F.seta(c, P2[0], P2[1], P2[0] + tx * 190, P2[1] + ty * 190, F.VEL, q, 9)
    E.frase(c, t, C["s08.a"], [("mesmo", "g", 80, COR), ("eixo", "g", 80, COR)], XE, 260, passo=0.12)
    E.frase(c, t, C["s08.a"] + 0.8, ps("uma grudada na outra", "i", 56), XE, 360, passo=0.1)
    E.frase(c, t, C["s08.b"], ps("uma volta juntas", "i", 60), XE, 500, passo=0.1)
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.pilula(c, "ω igual, f igual", XE + 270, 620, 52, "g", fundo=FREQ, a=a))
    E.frase(c, t, C["s08.d"], ps("borda maior:", "i", 58) + [("v", "g", 58, F.VEL), ("maior", "g", 58)], XE, 790, passo=0.1)
    E.frase(c, t, C["s08.d"] + 1.6, ps("como no carrossel", "i", 50, TINTA2), XE, 880, passo=0.1)


# ---------------- bicicleta ----------------
def b_bicicleta(c, t, C, b):
    x1, x2, y = 820, 1480, 560

    def giros():
        if t < C["s10.c"]:
            return 0.0
        return ease_io(prog(t, C["s10.c"], max(0.8, C["s10.g"] - C["s10.c"])))
    gp = giros()
    transmissao(c, t, x1, x2, y, 160, 54, 48, 16, 330, gp, ep(t, C["s09"], 0.5))

    def nomes():
        E.foco(c, t, C["s09.a"], 0.4, lambda a: E.pilula(c, "coroa (pedal)", x1, y + 260, 44, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s09.b"], 0.4, lambda a: E.pilula(c, "corrente", (x1 + x2) / 2, y - 210, 44, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s09.b"] + 1.2, 0.4, lambda a: E.pilula(c, "catraca", x2, y + 120, 44, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "mesmo eixo da roda", x2, y + 380, 44, "g", fundo=FREQ, a=a))
    E.saida(c, t, C["s10"] - 0.1, nomes)
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("a bicicleta junta tudo", "i", 66), XE, 180, passo=0.12)
        return

    def s10():
        E.foco(c, t, C["s10.a"], 0.4, lambda a: centro(c, "48 dentes", x1, y - 200, 50, "g", COR, a))
        E.foco(c, t, C["s10.b"], 0.4, lambda a: centro(c, "16 dentes", x2, y + 120, 44, "g", COR, a))
        E.frase(c, t, C["s10.c"], [("corrente:", "g", 56, F.VEL), ("48 ÷ 16 =", "g", 56)], XE, 180, passo=0.1)
        E.foco(c, t, C["s10.d"], 0.4, lambda a: E.escreve(c, "3 voltas da catraca", XE + 560, 180, 56, "g", COR, a))
        E.frase(c, t, C["s10.e"], [("eixo:", "g", 56, FREQ), ("f", "g", 56), ("igual", "i", 58)], XE, 280, passo=0.1)
        E.foco(c, t, C["s10.f"], 0.4, lambda a: E.escreve(c, "a roda dá 3 voltas", XE + 560, 280, 56, "g", COR, a))
        bola_txt(c, t, C["s10.g"], "1 → 3", 1780, 160, 100, 52)
        E.foco(c, t, C["s10.c"], 0.4, lambda a: centro(c, f"pedal: {min(1, int(gp + 1e-6))} volta", x1, 960, 46, "b", TINTA, a))
        E.foco(c, t, C["s10.c"], 0.4, lambda a: centro(c, f"roda: {int(3 * gp + 1e-6)} voltas", x2, 960, 46, "b", COR, a))
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11.a"], [("coroa", "i", 54), ("grande", "g", 54), ("+", "g", 54, TINTA2), ("catraca", "i", 54), ("pequena", "g", 54)], XE, 170, passo=0.1)
    E.foco(c, t, C["s11.a"] + 1.4, 0.4, lambda a: E.pilula(c, "rápida e pesada", XE + 1180, 155, 44, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s11.b"], [("coroa", "i", 54), ("pequena", "g", 54), ("+", "g", 54, TINTA2), ("catraca", "i", 54), ("grande", "g", 54)], XE, 960, passo=0.1)
    E.foco(c, t, C["s11.b"] + 1.4, 0.4, lambda a: E.pilula(c, "leve, para subir", XE + 1180, 945, 44, "g", fundo=CERTO, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    A, ra, B, rb = (1080, 600), 80, (1560, 600), 240
    s = max(0.0, t - C["s12"]) * 160.0
    polia(c, *A, ra, 90 - math.degrees(s / ra), ep(t, C["s12"], 0.4))
    polia(c, *B, rb, 90 - math.degrees(s / rb), ep(t, C["s12"], 0.4))
    correia(c, A, ra, B, rb, s, ep(t, C["s12"], 0.4))
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s12.a"], [("correia", "i", 64), ("→", "g", 64)] + [("mesma", "g", 64, ERRADO), ("frequência?", "g", 64, ERRADO)], XE, 350, passo=0.12)
    E.foco(c, t, C["s12.b"], 0.4, lambda a: (F.medida(c, 30, "Hz", A[0], A[1] - ra - 50, 56, FREQ, a, "center"), F.medida(c, "30", "Hz?", B[0], B[1] - rb - 40, 56, ERRADO, a, "center")))
    if t >= C["s12.c"]:
        E.risco(c, B[0] - 90, B[1] - rb - 30, B[0] + 90, B[1] - rb - 90, t, C["s12.c"], largura=9)
        E.foco(c, t, C["s12.c"] + 0.5, 0.4, lambda a: F.medida(c, 10, "Hz", B[0] + 140, B[1] - rb - 40, 56, CERTO, a))
    E.frase(c, t, C["s12.c"], [("na", "i", 60), ("correia:", "i", 60), ("v", "g", 60, F.VEL), ("da", "i", 60), ("borda", "i", 60), ("igual", "g", 60, CERTO)], XE, 540, passo=0.1)
    E.frase(c, t, C["s12.d"], [("f", "g", 60, FREQ), ("igual", "i", 60), ("só", "i", 60), ("no", "i", 60), ("mesmo", "g", 60), ("eixo", "g", 60)], XE, 680, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("o atalho, em", "i", 76, CLARO) + [("duas linhas", "g", 76, BR)], W / 2, 170, "center", 0.12)
        E.frase(c, t, C["s13.a"], [("correia,", "g", 66, BR), ("corrente", "g", 66, BR), ("ou", "i", 70, CLARO), ("dente:", "g", 66, BR)], 260, 360, passo=0.1)
        E.foco(c, t, C["s13.b"], 0.5, lambda a: E.pilula(c, "v igual", 420, 470, 54, "g", fundo=F.VEL, a=a))
        E.foco(c, t, C["s13.c"], 0.5, lambda a: (E.formula(c, "f · R igual", 640, 490, 70, "g", BR, a), E.escreve(c, "a menor gira mais", 1100, 490, 56, "i", CLARO, a)))
        E.frase(c, t, C["s13.d"], [("mesmo", "g", 66, BR), ("eixo:", "g", 66, BR)], 260, 700, passo=0.1)
        E.foco(c, t, C["s13.e"], 0.5, lambda a: (E.pilula(c, "ω igual", 420, 810, 54, "g", fundo=FREQ, a=a),
                                                 E.escreve(c, "a maior anda mais na borda", 640, 830, 56, "i", CLARO, a)))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("bônus: em", "i", 66, CLARO) + [("f · R", "g", 66, BR)] + ps("use", "i", 66, CLARO) + [("rpm", "g", 66, BR), ("e", "i", 66, CLARO),
                                                                                                                                  ("cm", "g", 66, BR)], W / 2, 220, "center", 0.1)
    E.frase(c, t, C["s14.b"], ps("a unidade é a mesma dos dois lados: cancela", "i", 54, CLARO), W / 2, 330, "center", 0.08)
    E.formula_em(c, t, C["s14.c"], "1800 · 5 = f · 15", W / 2, 520, 90, "g", BR, "center")
    E.foco(c, t, C["s14.c"] + 2.4, 0.5, lambda a: (E.bola(c, W / 2, 700, 110, a=a), centro(c, "600 rpm", W / 2, 718, 54, "g", BR, a)))
    E.foco(c, t, C["s14.c"] + 3.6, 0.4, lambda a: centro(c, "= 10 Hz", W / 2 + 250, 718, 54, "g", CLARO, a))
    E.frase(c, t, C["s14.d"], [("não", "g", 58, ERRADO), ("compensa:", "i", 60, CLARO)] + ps("pediu v em m/s", "i", 60, CLARO) + [("→", "g", 60, CLARO), ("Hz", "g", 60, BR), ("e", "i", 60, CLARO),
                                                                                                                                       ("metros", "g", 60, BR)], W / 2, 950, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], [("coroa", "i", 66), ("40", "g", 66, COR), ("dentes,", "i", 66)], XE, 330, passo=0.12)
    E.frase(c, t, C["s15.c"], [("catraca", "i", 66), ("10", "g", 66, COR)], XE, 430, passo=0.12)
    E.foco(c, t, C["s15.d"], 0.5, lambda a: (E.escreve(c, "roda:", XE, 530, 60, "i", TINTA, a), E.escreve(c, "R =", XE + 170, 530, 60, "g", TINTA, a), F.medida(c, "0,3", "m", XE + 300, 530, 66, COR, a)))
    E.frase(c, t, C["s15.e"], ps("1 pedalada por segundo", "g", 58), XE, 640, passo=0.1)
    E.frase(c, t, C["s15.f"], [("velocidade", "g", 70), ("da", "i", 70), ("bicicleta?", "g", 70, COR)], XE, 800, passo=0.12)
    E.frase(c, t, C["s15.f"] + 1.4, [("use", "i", 54, TINTA2), ("π = 3", "b", 50, TINTA2)], XE, 900, passo=0.1)
    if t < C["s16"]:
        transmissao(c, t, 1180, 1620, 560, 140, 36, 40, 10, 260, max(0.0, t - C["s15.e"]) if t >= C["s15.e"] else 0, ep(t, C["s15.a"], 0.5))
    else:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    transmissao(c, t, 1200, 1580, 560, 120, 32, 40, 10, 220, max(0.0, t - C["s17"]) * 0.5, ep(t, C["s17"], 0.5))
    E.frase(c, t, C["s17.a"], [("corrente:", "g", 60, F.VEL), ("40 ÷ 10 = 4", "g", 60)], XE, 260, passo=0.1)
    E.foco(c, t, C["s17.a"] + 1.4, 0.4, lambda a: E.escreve(c, "voltas da catraca", XE, 340, 50, "i", TINTA2, a))
    E.frase(c, t, C["s17.b"], [("eixo:", "g", 60, FREQ), ("roda", "i", 62), ("também", "i", 62)], XE, 460, passo=0.1)
    bola_txt(c, t, C["s17.c"], "4 Hz", XE + 760, 440, 80, 52, FREQ)
    E.formula_em(c, t, C["s18.a"], "v = 2 · π · f · R", XE, 620, 72, "g", TINTA)
    E.formula_em(c, t, C["s18.b"], "= 2 · 3 · 4 · 0,3", XE, 740, 72, "g", TINTA)
    bola_txt(c, t, C["s18.c"], "7,2 m/s", XE + 760, 710, 110, 50, F.VEL)
    E.frase(c, t, C["s18.d"], ps("borda da roda = velocidade da bicicleta", "i", 50, TINTA2), XE, 920, passo=0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = (("s19.a", [("correia:", "g", 64), ("v", "g", 64, F.VEL), ("igual", "i", 66)]),
             ("s19.b", [("eixo:", "g", 64), ("ω", "g", 64, FREQ), ("igual", "i", 66)]),
             ("s19.c", [("bicicleta:", "g", 64), ("os", "i", 66), ("dois,", "i", 66), ("um", "i", 66), ("depois", "i", 66), ("do", "i", 66), ("outro", "i", 66)]))

    def desenho():
        for j, (lab, x) in enumerate((("rotação", 300), ("polias", 610), ("bicicleta", 880))):
            E.foco(c, t, C["s20.b"] + 0.3 * j, 0.4, lambda a, lab=lab, x=x: E.pilula(c, lab, x + (E.larg(lab, "g", 48) + 52) / 2, 820, 48, "g", fundo=TINTA, a=a))
    fim(c, t, C, "s19", itens, "s20", [("s20.a", [("Praticando", "g", 110, COR)]), ("s20.a", [("movimento", "i", 90), ("circular", "g", 100, COR)])],
        desenho, "s20.c", "s20.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, correia=b_correia, engrenagem=b_engrenagem, eixo=b_eixo, bicicleta=b_bicicleta,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
