"""Visual — Estudativo · FIS-ELE-005: condutores, poder das pontas e gaiola de Faraday.

Segue a linguagem visual da Física (FIS-CIN-001) e a da trilha Eletricidade (docstring do visual.py da FIS-ELE-001):
metal = cinza com volume; carga em excesso = bolinhas + laranja na superfície; campo em tinta e linhas em cinza-tinta;
raio e faísca em amarelo com contorno; terra = três traços. Aula conceitual: sem contas. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-005_condutores_pontas_gaiola_de_faraday.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("superficie", "pontas", "gaiola", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
METAL = "#A3AAB4"
AMAR = "#FFC400"

# aula conceitual: a única conta é U = E·d com E = 0
assert 0 * 5 == 0


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha Eletricidade (cópia das da FIS-ELE-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def q(c, x, y, r, s, a=1.0):
    """carga pequena: + laranja, − azul, com o sinal em branco"""
    if a <= 0:
        return
    cor = E.COR if s == "+" else NEG
    c.drawCircle(x + r * 0.08, y + r * 0.16, r, M.paint("#000000", 0.16 * a))
    c.drawCircle(x, y, r, M.paint(cor, a))
    k, lw = r * 0.52, max(3, r * 0.24)
    M.line(c, x - k, y, x + k, y, BR, a, lw)
    if s == "+":
        M.line(c, x, y - k, x, y + k, BR, a, lw)


def esfera_metal(c, cx, cy, R, a=1.0):
    E.bola(c, cx, cy, R, METAL, a)


def pilula_f(c, s, cx, cy, size, fundo=None, cor=BR, a=1.0):
    """pílula com fórmula (aceita potência de dez)"""
    if a <= 0:
        return
    w, h = E.formula(None, s, 0, 0, size, "g", a=0) + size * 1.2, size * 1.9
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(fundo or E.COR, a))
    E.formula(c, s, cx, cy + size * 0.36, size, "g", cor, a, "center")


def _linha(c, partes, x, y, a, align="center"):
    """linha de tipografia mista parada (para a troca)"""
    w, xs = E._arranjo(partes, x, align)
    for p, xx in zip(partes, xs):
        E.escreve(c, p[0], xx, y, p[2], p[1], p[3] if len(p) > 3 else TINTA, a)


def terra(c, x, y, a=1.0, cor=TINTA):
    """símbolo de terra: três traços, o de cima em y"""
    for i, w in enumerate((90, 60, 30)):
        M.line(c, x - w / 2, y + i * 18, x + w / 2, y + i * 18, cor, a, 6)


def promessa(c, t, C, cena, itens, sz=74):
    """tela "até o fim da aula": órbita à direita e itens numerados. itens = [(cue, texto, atraso)]"""
    tb = C[itens[0][0]] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(i + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", sz, COR if i == 0 else TINTA)], XE + 110, y)


def lembrete(c, t, C, cena, itens, desenhos):
    """o que precisa saber: itens = [(cue, linha fina, linha forte)]; desenhos[i](a, cx, cy) desenha à direita da caixa"""
    if len(itens) == 2:
        E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
        E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
        E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    else:
        E.frase(c, t, C[cena] + 0.2, ps("você precisa", "i", 84), XE, 470, passo=0.14)
        E.frase(c, t, C[cena] + 0.6, ps("de uma coisa", "i", 84), XE, 580, passo=0.14)
    x, w = 820, 1000
    y0 = 230 if len(itens) == 2 else 340
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 190, y + 115))
    if len(itens) == 2:
        q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
        E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    else:
        E.cursor(c, x + w - 30, 560, ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def resumo(c, t, C, cena, itens, dy=190):
    """tela "resumindo": itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 380 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)


def cta(c, t, C, cena):
    """inscreva-se (cue c) e bons estudos (cue d), à direita"""
    E.foco(c, t, C[cena + ".c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[cena + ".c"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C[cena + ".c"] + 0.2, 0.4))
    E.frase(c, t, C[cena + ".d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1580, 990, "center")


def questao_relogio(c, t, C, cena_pausa, desenho):
    """lado direito da questão: o desenho até a pausa, depois o relógio"""
    if t < C[cena_pausa]:
        desenho()
    else:
        E.relogio(c, t, C[cena_pausa + ".a"], cx=1460, cy=440, r=200)



def raio(c, pts, a=1.0, largura=14):
    """raio em zigue-zague amarelo com contorno"""
    if a <= 0:
        return
    for cor, lw in ((TINTA, largura + 8), (AMAR, largura)):
        p = M.paint(cor, a, stroke=lw)
        p.setStrokeJoin(skia.Paint.kRound_Join)
        path = skia.Path()
        path.moveTo(*pts[0])
        for P in pts[1:]:
            path.lineTo(*P)
        c.drawPath(path, p)


def zigue(x0, y0, x1, y1, n=6, amp=40):
    return [(lerp(x0, x1, i / n) + (amp if i % 2 else -amp) * (0 < i < n), lerp(y0, y1, i / n)) for i in range(n + 1)]


def gota(cx, cy, R, ponta=1.0, n=120):
    """contorno de um condutor com ponta à direita"""
    pts = []
    for i in range(n):
        g = 2 * math.pi * i / n
        r = R * (1 + 0.85 * ponta * max(0.0, math.cos(g)) ** 10)
        pts.append((cx + r * math.cos(g), cy - r * math.sin(g)))
    return pts


def corpo_gota(c, pts, a=1.0):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(*pts[0])
    for P in pts[1:]:
        p.lineTo(*P)
    p.close()
    g = skia.Paint(AntiAlias=True)
    xs = [P[0] for P in pts]; ys = [P[1] for P in pts]
    g.setShader(skia.GradientShader.MakeLinear([skia.Point(min(xs), min(ys)), skia.Point(max(xs), max(ys))],
                                               [M.hexc("#C9CED6", a), M.hexc("#7F8794", a)]))
    c.drawPath(p, g)


def cargas_borda(c, pts, idx, r, a):
    for i in idx:
        x, y = pts[i % len(pts)]
        q(c, x, y, r, "+", a)


def predio(c, x, y, w, h, a=1.0):
    """prédio com janelas; (x, y) = canto de baixo à esquerda"""
    if a <= 0:
        return
    M.rrect(c, x, y - h, w, h, 6, "#D9D9D4", a)
    c.drawRect(skia.Rect.MakeXYWH(x, y - h, w, h), M.paint(TINTA, a, stroke=4))
    for i in range(3):
        for j in range(5):
            M.rrect(c, x + 30 + i * (w - 60) / 3 + 10, y - h + 40 + j * (h - 80) / 5, (w - 60) / 3 - 30, (h - 80) / 5 - 30, 4, "#8FB4CC", a)


def nuvem(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    for dx, dy, r in ((-0.8, 0.1, 0.55), (-0.25, -0.25, 0.7), (0.4, -0.1, 0.65), (0.9, 0.15, 0.5), (0.0, 0.25, 0.6)):
        c.drawCircle(cx + dx * s, cy + dy * s, r * s, M.paint("#6B6F78", a))


def carro(c, x, y, w, a=1.0, cargas=0.0):
    """carro de lado com a lataria; cargas = quanto já apareceram as cargas na lataria"""
    F.carrinho(c, x, y, w, a=a)
    if cargas > 0:
        for i in range(9):
            u = i / 8
            q(c, x - w * 0.42 + u * w * 0.84, y - w * 0.27 - 0.13 * w * math.sin(u * math.pi) * (0.3 < u < 0.75), 16, "+", cargas)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        cx, cy, w = 1280, 860, 620
        E.foco(c, t, C["s01.a"], 0.5, lambda a: carro(c, cx, cy, w, a))
        p = ep(t, C["s01.a"] + 0.4, 0.2) * (0.6 + 0.4 * abs(math.sin(t * 18)) if t < C["s01.a"] + 1.2 else 1)
        raio(c, zigue(1180, 0, 1240, cy - w * 0.38, 7, 36), p)
        E.frase(c, t, C["s01.a"], ps("um raio cai no carro", "i", 80), XE, 230, passo=0.12)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.pilula(c, "quem está dentro: sem arranhão", 560, 400, 48, "g", fundo=CERTO, a=a))
        if t >= C["s01.c"]:
            for dx in (-0.29, 0.29):
                c.drawCircle(cx + dx * w, cy - w * 0.06, 70, M.paint(ERRADO, ep(t, C["s01.c"], 0.3), stroke=7))
        E.frase(c, t, C["s01.c"], [("não", "g", 80, ERRADO), ("são", "i", 84), ("os", "i", 84), ("pneus", "g", 80)], XE, 600, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "onde a carga fica", 1.4), ("s02.b", "o para-raios", 0), ("s02.c", "o carro e o raio", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def rep(a, x, y):
        q(c, x - 70, y, 28, "+", a); q(c, x + 10, y, 28, "+", a)
        F.seta(c, x - 110, y, x - 170, y, E.COR, a, 6, 18); F.seta(c, x + 50, y, x + 110, y, E.COR, a, 6, 18)
    lembrete(c, t, C, "s03", (("s03.b", "metal: elétrons andam;", "mesmo sinal repele"), ("s03.c", "tensão no campo uniforme:", "campo × distância")),
             (rep, lambda a, x, y: E.formula(c, "U = E · d", x - 30, y + 20, 56, "g", TINTA, a, "center")))


# ---------------- onde a carga fica ----------------
def b_superficie(c, t, C, b):
    cx, cy, R = 1340, 580, 270
    n = 12

    def esfera_cargas(a_sep, al=1.0, rr=24):
        for i in range(n):
            g = 2 * math.pi * i / n
            r0 = 60 + 40 * (i % 3)
            r = lerp(r0, R - 34, a_sep)
            q(c, cx + r * math.cos(g + 0.3 * i), cy + r * math.sin(g + 0.3 * i), rr, "+", al) if a_sep < 1 else q(c, cx + (R - 34) * math.cos(g), cy + (R - 34) * math.sin(g), rr, "+", al)

    def s04():
        E.foco(c, t, C["s04"] + 0.2, 0.5, lambda a: E.bola(c, cx, cy, R, METAL, a))
        sep = ease_io(prog(t, C["s04.b"] + 0.3, 1.6))
        if t >= C["s04.a"]:
            for i in range(n):
                g = 2 * math.pi * i / n
                r0 = 40 + 30 * (i % 3)
                ang0 = g + 0.7 * (i % 4)
                x0, y0 = cx + r0 * math.cos(ang0), cy + r0 * math.sin(ang0)
                x1, y1 = cx + (R - 34) * math.cos(g), cy + (R - 34) * math.sin(g)
                q(c, lerp(x0, x1, sep), lerp(y0, y1, sep), 24, "+", ep(t, C["s04.a"] + 0.05 * i, 0.3))
        E.frase(c, t, C["s04.a"], [("carga", "i", 80), ("a", "i", 80), ("mais", "g", 76, COR)], XE, 300, passo=0.12)
        E.frase(c, t, C["s04.b"], [("se", "i", 80), ("repelem", "g", 76, COR)], XE, 430, passo=0.12)
        E.frase(c, t, C["s04.c"], ps("vão para a", "i", 76) + [("superfície", "g", 72, COR)], XE, 600, passo=0.12)
        E.frase(c, t, C["s04.c"] + 0.8, [("de", "i", 76), ("fora", "g", 72, COR)], XE, 700, passo=0.12)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return

    def esfera_eq(a=1.0):
        E.bola(c, cx, cy, R, METAL, a)
        for i in range(n):
            g = 2 * math.pi * i / n
            q(c, cx + (R - 34) * math.cos(g), cy + (R - 34) * math.sin(g), 24, "+", a)

    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("em", "i", 84), ("equilíbrio:", "g", 80, COR)], XE, 230, passo=0.12)
        itens = (("s05.b", [("carga:", "g", 60), ("na", "i", 64), ("superfície", "i", 64), ("de", "i", 64), ("fora", "i", 64)]),
                 ("s05.c", [("campo", "g", 60), ("dentro:", "g", 60), ("zero", "g", 60, COR)]),
                 ("s05.d", [("potencial:", "g", 60), ("igual", "i", 64), ("em", "i", 64), ("todo", "i", 64), ("ponto", "i", 64)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 24, 40, a=a), centro(c, str(i + 1), XE + 40, y - 2, 48, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 110, y, passo=0.1)
        E.foco(c, t, C["s05"], 0.5, esfera_eq)
        E.foco(c, t, C["s05.c"] + 0.3, 0.4, lambda a: E.formula(c, "E = 0", cx, cy + 25, 90, "g", TINTA, a, "center"))
        E.foco(c, t, C["s05.d"] + 0.3, 0.4, lambda a: E.pilula(c, "V igual em todo o metal", cx, cy + R + 80, 44, "b", fundo=TINTA, a=a))
        return
    # s06: por que o campo dentro é zero
    E.frase(c, t, C["s06"], ps("por que", "i", 80) + [("E = 0", "g", 80, COR)] + ps("dentro?", "i", 80), XE, 220, passo=0.12)
    esfera_eq()
    for i, (dx, dy) in enumerate(((-120, -60), (-40, 70), (60, -80), (120, 50))):
        mx = 60 * ease_io(prog(t, C["s06.a"] + 0.3, 0.8)) * (1 - ease_io(prog(t, C["s06.b"], 0.5)))
        q(c, cx + dx + mx, cy + dy, 22, "−", ep(t, C["s06.a"], 0.4))
    if C["s06.a"] <= t < C["s06.b"]:
        p_ = ep(t, C["s06.a"] + 0.2, 0.3)
        M.line(c, cx - 200, cy + 170, cx + 150, cy + 170, TINTA2, p_, 5, dash=E.TRACO)
        F._cabeca(c, cx + 160, cy + 170, 1, 0, 24, TINTA2, p_)
    E.frase(c, t, C["s06.a"], ps("se houvesse campo,", "i", 64) + [("andariam", "g", 60)], XE, 380, passo=0.1)
    E.frase(c, t, C["s06.b"], ps("mas estão", "i", 64) + [("parados", "g", 60, COR)], XE, 500, passo=0.1)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: pilula_f(c, "E = 0 dentro", XE + 280, 650, 70, a=a))
    E.formula_em(c, t, C["s06.d"], "U = E · d = 0 · d = 0", XE, 860, 76, "g", TINTA)
    E.foco(c, t, C["s06.d"] + 1.6, 0.4, lambda a: E.escreve(c, "o potencial não muda", XE, 950, 54, "i", TINTA2, a))


# ---------------- pontas ----------------
def b_pontas(c, t, C, b):
    cx, cy, R = 980, 600, 190
    pts = gota(cx, cy, R)
    idx_ponta = [0, 3, 117, 6, 114]
    idx_resto = [10, 20, 30, 45, 60, 75, 90, 100, 110]

    def s07_08():
        E.frase(c, t, C["s07.a"], [("um", "i", 84), ("condutor", "i", 84), ("com", "i", 84), ("ponta", "g", 80, COR)], XE, 220, passo=0.12)
        E.foco(c, t, C["s07.a"], 0.5, lambda a: corpo_gota(c, pts, a))
        cargas_borda(c, pts, idx_resto, 18, ep(t, C["s07.b"], 0.4))
        cargas_borda(c, pts, idx_ponta, 18, ep(t, C["s07.b"] + 0.4, 0.4))
        if t >= C["s07.c"]:
            for i in idx_resto + idx_ponta:
                x, y = pts[i % len(pts)]
                ux, uy = E._uni(cx, cy, x, y)
                k = 230 if i in idx_ponta else 90
                F.seta(c, x + ux * 26, y + uy * 26, x + ux * (26 + k), y + uy * (26 + k), TINTA, ep(t, C["s07.c"], 0.3), 5, 18, ease_out(prog(t, C["s07.c"], 0.6)))
        E.foco(c, t, C["s07.c"] + 0.6, 0.4, lambda a: E.pilula(c, "campo mais forte na ponta", 1560, 380, 44, "b", fundo=E.COR, a=a))
        E.foco(c, t, C["s07.d"], 0.5, lambda a: E.pilula(c, "PODER DAS PONTAS", 960, 960, 64, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s08"] - 0.1, s07_08)
    if C["s08"] <= t < C["s09"]:
        E.foco(c, t, C["s08"], 0.4, lambda a: corpo_gota(c, pts, a))
        cargas_borda(c, pts, idx_resto + idx_ponta, 18, ep(t, C["s08"], 0.4))
        E.frase(c, t, C["s08"], [("o", "i", 80), ("ar", "i", 80), ("é", "i", 80), ("isolante", "g", 76)], XE, 220, passo=0.12)
        E.frase(c, t, C["s08.a"], ps("campo muito forte:", "i", 70) + [("conduz", "g", 66, COR)], XE, 340, passo=0.12)
        x0 = pts[0][0]
        if t >= C["s08.b"]:
            fl = 0.5 + 0.5 * abs(math.sin(t * 22))
            raio(c, zigue(x0 + 10, cy, x0 + 420, cy - 60, 6, 26), ep(t, C["s08.b"], 0.2) * fl, 9)
        E.foco(c, t, C["s08.b"] + 0.3, 0.4, lambda a: E.pilula(c, "faísca", x0 + 230, cy + 120, 50, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s08.c"], ps("as faíscas saltam das", "i", 66) + [("pontas", "g", 62, COR)], XE, 960, passo=0.12)
    if t < C["s09"]:
        return
    # para-raios
    px, py, pw, ph = 1060, 960, 340, 360
    E.foco(c, t, C["s09.b"] - 0.4, 0.5, lambda a: predio(c, px, py, pw, ph, a))
    hx = px + pw / 2
    topo = py - ph
    E.foco(c, t, C["s09.b"], 0.4, lambda a: (M.line(c, hx, topo, hx, topo - 160, TINTA, a, 9), c.drawCircle(hx, topo - 166, 9, M.paint(TINTA, a))))
    if t >= C["s09.c"]:
        F.fio(c, t, C["s09.c"], [(hx, topo - 20), (px + pw + 50, topo), (px + pw + 50, py)], cor=TINTA)
        E.foco(c, t, C["s09.c"] + 0.6, 0.4, lambda a: (terra(c, px + pw + 50, py + 10, a), E.escreve(c, "terra", px + pw + 110, py + 40, 46, "i", TINTA2, a)))
    E.foco(c, t, C["s09.d"] - 0.5, 0.5, lambda a: nuvem(c, hx + 60, 130, 120, a))
    if t >= C["s09.d"] + 0.4:
        fl = 0.6 + 0.4 * abs(math.sin(t * 16))
        raio(c, zigue(hx + 40, 200, hx, topo - 170, 5, 30), ep(t, C["s09.d"] + 0.4, 0.2) * fl, 12)
    if t >= C["s09.e"]:
        u = ease_io(prog(t, C["s09.e"] + 0.3, 1.4))
        trilha = [(hx, topo - 170), (hx, topo - 20), (px + pw + 50, topo), (px + pw + 50, py)]
        L = [math.dist(trilha[i], trilha[i + 1]) for i in range(3)]
        alvo = sum(L) * u
        for (x0, y0), (x1, y1), l_ in zip(trilha, trilha[1:], L):
            if alvo <= l_:
                f = alvo / l_
                bx, by = lerp(x0, x1, f), lerp(y0, y1, f)
                break
            alvo -= l_
        else:
            bx, by = trilha[-1]
        c.drawCircle(bx, by, 22, M.paint(AMAR, 1.0))
        c.drawCircle(bx, by, 22, M.paint(TINTA, 1.0, stroke=4))
    E.frase(c, t, C["s09.a"], [("o", "i", 84), ("para-raios", "g", 80, COR)], XE, 260, passo=0.12)
    E.frase(c, t, C["s09.b"], ps("haste pontuda no alto", "i", 60), XE, 400, passo=0.1)
    E.frase(c, t, C["s09.c"], ps("cabo grosso até a terra", "i", 60), XE, 510, passo=0.1)
    E.frase(c, t, C["s09.d"], ps("a ponta oferece o caminho", "i", 60), XE, 620, passo=0.1)
    E.frase(c, t, C["s09.e"], [("a", "i", 60), ("descarga", "g", 58, COR), ("desce", "i", 60), ("pelo", "i", 60), ("cabo", "i", 60)], XE, 760, passo=0.1)
    E.foco(c, t, C["s09.e"] + 1.0, 0.4, lambda a: E.escreve(c, "a carga do raio passando de uma vez", XE, 850, 44, "i", TINTA2, a))


# ---------------- gaiola de Faraday ----------------
def b_gaiola(c, t, C, b):
    def s10():
        cx, cy, w = 1220, 880, 640
        E.frase(c, t, C["s10.a"], [("gaiola", "g", 92, COR), ("de", "i", 92), ("Faraday", "g", 92, COR)], XE, 230, passo=0.12)
        E.foco(c, t, C["s10"], 0.5, lambda a: carro(c, cx, cy, w, a, ep(t, C["s10.b"], 0.5)))
        E.foco(c, t, C["s10.b"] + 0.2, 0.4, lambda a: E.escreve(c, "carga na lataria", 300, 430, 56, "i", TINTA, a))
        E.foco(c, t, C["s10.c"], 0.5, lambda a: E.pilula(c, "E ≈ 0 dentro", cx - 40, cy - w * 0.17, 46, "g", fundo=CERTO, a=a))
        if t >= C["s10.d"] - 0.6:
            fl = 0.6 + 0.4 * abs(math.sin(t * 16))
            raio(c, zigue(cx - 100, 0, cx - 60, cy - w * 0.4, 6, 30), ep(t, C["s10.d"] - 0.6, 0.2) * fl, 12)
        if t >= C["s10.d"]:
            u = ease_io(prog(t, C["s10.d"], 1.4))
            trilha = [(cx - 60, cy - w * 0.4), (cx + w * 0.3, cy - w * 0.27), (cx + w * 0.47, cy - w * 0.12), (cx + w * 0.5, cy + 20)]
            L = [math.dist(trilha[i], trilha[i + 1]) for i in range(3)]
            alvo = sum(L) * u
            bx, by = trilha[-1]
            for (x0, y0), (x1, y1), l_ in zip(trilha, trilha[1:], L):
                if alvo <= l_:
                    f = alvo / l_
                    bx, by = lerp(x0, x1, f), lerp(y0, y1, f)
                    break
                alvo -= l_
            c.drawCircle(bx, by, 20, M.paint(AMAR, 1.0))
            c.drawCircle(bx, by, 20, M.paint(TINTA, 1.0, stroke=4))
        E.frase(c, t, C["s10.d"], ps("a descarga corre pela", "i", 60) + [("lataria", "g", 58, COR)], XE, 560, passo=0.1)
        E.foco(c, t, C["s10.e"], 0.5, lambda a: E.pilula(c, "quem está dentro: protegido", 560, 700, 48, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11"], ps("a mesma blindagem", "i", 80), W / 2, 210, "center", 0.12)

    def elevador(a):
        M.rrect(c, 360, 330, 460, 560, 14, METAL, a)
        M.line(c, 590, 360, 590, 860, TINTA2, a, 4)
        M.rrect(c, 640, 560, 100, 170, 16, TINTA, a)
        M.rrect(c, 652, 578, 76, 120, 8, "#3A3A44", a)
        E.escreve(c, "sem sinal", 610, 790, 40, "b", ERRADO, a)

    def micro(a):
        M.rrect(c, 1100, 400, 560, 380, 20, "#E1E1DC", a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1100, 400, 560, 380), 20, 20), M.paint(TINTA, a, stroke=4))
        M.rrect(c, 1140, 440, 380, 300, 10, "#2C2C34", a)
        for i in range(12):
            M.line(c, 1140 + i * 32, 440, 1140 + i * 32, 740, METAL, 0.8 * a, 2)
        for j in range(10):
            M.line(c, 1140, 440 + j * 30, 1520, 440 + j * 30, METAL, 0.8 * a, 2)
        c.drawCircle(1600, 500, 22, M.paint(TINTA2, a))
    E.foco(c, t, C["s11.a"], 0.5, elevador)
    E.foco(c, t, C["s11.a"] + 0.3, 0.4, lambda a: centro(c, "elevador de metal", 590, 960, 50, "i", TINTA, a))
    E.foco(c, t, C["s11.b"], 0.5, micro)
    E.foco(c, t, C["s11.b"] + 0.3, 0.4, lambda a: centro(c, "tela de metal na porta", 1380, 860, 50, "i", TINTA, a))
    E.foco(c, t, C["s11.b"] + 1.8, 0.4, lambda a: E.pilula(c, "ondas: outra aula", 1380, 960, 40, "b", fundo=TINTA2, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    cx, cy, w = 1300, 900, 560
    E.foco(c, t, C["s12.a"], 0.5, lambda a: carro(c, cx, cy, w, a))
    E.frase(c, t, C["s12.a"], ps("os pneus isolam?", "i", 80), XE + 480, 200, passo=0.12)
    if t >= C["s12.a"] + 0.4:
        for dx in (-0.29, 0.29):
            c.drawCircle(cx + dx * w, cy - w * 0.06, 64, M.paint(ERRADO, ep(t, C["s12.a"] + 0.4, 0.3), stroke=7))
    E.frase(c, t, C["s12.b"], ps("o raio atravessa", "i", 64) + [("centenas", "g", 60), ("de", "i", 64), ("metros", "g", 60)], XE, 400, passo=0.1)
    E.frase(c, t, C["s12.b"] + 1.2, ps("de ar isolante", "i", 64), XE, 490, passo=0.1)
    E.frase(c, t, C["s12.c"], ps("borracha:", "i", 64) + [("centímetros", "g", 60, ERRADO)], XE, 620, passo=0.1)
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.pilula(c, "quem protege: a lataria", 560, 790, 54, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], ps("condutor em equilíbrio:", "i", 70, CLARO) + [("3", "g", 70, BR), ("respostas", "g", 70, BR)], W / 2, 280, "center", 0.12)
        for i, (k, p_, r_) in enumerate((("s13.b", "carga?", "superfície de fora"), ("s13.c", "campo dentro?", "zero"), ("s13.d", "potencial?", "igual em todo ponto"))):
            y = 450 + i * 140
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 360, y - 24, 44, a=a), centro(c, str(i + 1), 360, y - 2, 52, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(p_, "i", 70, CLARO)], 450, y)
            E.frase(c, t, C[k] + 0.6, [(r_, "g", 66, BR)], 980, y)
        E.frase(c, t, C["s13.e"], [("ponta", "g", 66, BR), ("→", "g", 66, CLARO), ("campo", "i", 70, CLARO), ("mais", "i", 70, CLARO), ("forte", "g", 66, BR)], W / 2, 920, "center", 0.12)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("uma ideia só:", "i", 76, CLARO), W / 2, 300, "center", 0.12)
    E.frase(c, t, C["s14.a"] + 1.0, ps("as cargas se repelem até parar", "g", 64, BR), W / 2, 420, "center", 0.12)
    E.frase(c, t, C["s14.b"], [("não", "g", 66, ERRADO), ("vale", "g", 66, ERRADO), ("para", "i", 70, CLARO), ("isolantes:", "g", 66, BR)], W / 2, 640, "center", 0.12)
    E.frase(c, t, C["s14.b"] + 1.2, ps("a carga fica onde foi posta", "i", 66, CLARO), W / 2, 760, "center", 0.12)


# ---------------- questão ----------------
def esfera_oca(c, cx, cy, R, a=1.0, cargas=0.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy, R, M.paint(METAL, a, stroke=36))
    c.drawCircle(cx, cy, R - 18, M.paint("#7F8794", a, stroke=3))
    if cargas > 0:
        for i in range(12):
            g = 2 * math.pi * i / 12
            q(c, cx + (R + 34) * math.cos(g), cy + (R + 34) * math.sin(g), 18, "+", cargas)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], ps("esfera oca de metal,", "i", 70) + [("carga", "g", 66), ("+", "g", 66, COR)], XE, 330, passo=0.1)
    E.frase(c, t, C["s15.b"], [("onde", "i", 76), ("fica", "i", 76), ("a", "i", 76), ("carga?", "g", 72, COR)], XE, 490, passo=0.15)
    E.frase(c, t, C["s15.c"], [("campo", "i", 76), ("no", "i", 76), ("centro?", "g", 72, COR)], XE, 620, passo=0.15)
    E.frase(c, t, C["s15.d"], [("com", "i", 76), ("ponta:", "i", 76), ("onde", "i", 76), ("é", "i", 76), ("mais", "i", 76), ("forte?", "g", 72, COR)], XE, 750, passo=0.15)
    questao_relogio(c, t, C, "s16", lambda: E.foco(c, t, C["s15.a"], 0.5, lambda a: esfera_oca(c, 1480, 540, 220, a)))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.foco(c, t, C["s17"], 0.5, lambda a: esfera_oca(c, 620, 540, 220, a, ep(t, C["s17.a"], 0.5)))
    E.foco(c, t, C["s17.a"] + 0.3, 0.4, lambda a: centro(c, "na superfície de fora", 620, 880, 54, "g", COR, a))
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.formula(c, "E = 0", 620, 570, 96, "g", CERTO, a, "center"))
    pts = gota(1380, 540, 170)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: corpo_gota(c, pts, a))
    cargas_borda(c, pts, [10, 30, 50, 70, 90, 110], 16, ep(t, C["s17.c"] + 0.2, 0.4))
    cargas_borda(c, pts, [0, 3, 117, 6, 114], 16, ep(t, C["s17.d"], 0.4))
    E.foco(c, t, C["s17.c"] + 0.6, 0.4, lambda a: E.pilula(c, "mais forte na ponta", 1440, 820, 46, "b", fundo=E.COR, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela():
        resumo(c, t, C, "s18", (("s18.a", [("carga", "i", 70), ("na", "i", 70), ("superfície", "g", 66), ("de", "i", 70), ("fora", "g", 66)]),
                                ("s18.b", [("campo", "i", 70), ("dentro:", "i", 70), ("zero", "g", 66, COR)]),
                                ("s18.c", [("pontas", "g", 66), ("concentram", "i", 70), ("a", "i", 70), ("carga", "i", 70)])))
    E.saida(c, t, C["s19"] - 0.1, tela)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("capacitor", "g", 120, COR)], XE, 410)
    q_ = ep(t, C["s19.a"] + 0.3, 0.5)
    if q_ > 0:
        M.rrect(c, 400, 560, 36, 320, 8, E.COR, q_)
        M.rrect(c, 640, 560, 36, 320, 8, NEG, q_)
        for i in range(4):
            q(c, 418, 610 + i * 75, 16, "+", q_)
            q(c, 658, 610 + i * 75, 16, "−", q_)
    E.foco(c, t, C["s19.b"], 0.5, lambda a: (c.drawCircle(900, 720, 70, M.paint(AMAR, a)), c.drawCircle(900, 720, 70, M.paint(TINTA, a, stroke=5)),
                                            E.escreve(c, "flash", 1000, 740, 60, "g", TINTA, a)))
    cta(c, t, C, "s19")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, superficie=b_superficie, pontas=b_pontas, gaiola=b_gaiola, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
