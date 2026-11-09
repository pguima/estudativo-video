"""Visual — Estudativo · FIS-MAG-005: fluxo e lei de Faraday. Linguagem visual do Magnetismo: veja o visual.py da FIS-MAG-001.
Fluxo = a área da espira pintada de laranja claro, com o campo atravessando (símbolos saindo da folha ou setas finas);
a tensão induzida aparece no ponteiro de um medidor (medidor()). Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Magnetismo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MAG-005_fluxo_e_lei_de_faraday.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("fluxo", "muda", "faraday", "barra", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
VEL = F.VEL
AREA = E.mix(E.COR, "#FFFFFF", 0.78)

# todas as contas da aula
assert math.isclose(0.2 * 0.1, 0.02) and math.isclose(0.5 * 0.02, 0.01) and math.isclose(0.01 / 0.1, 0.1)
assert math.isclose(0.5 * 0.4, 0.2) and math.isclose(0.5 * 0.4 * 5, 1.0)
assert math.isclose(0.08 - 0.02, 0.06) and math.isclose(0.06 / 0.2, 0.3) and math.isclose(10 * 0.3, 3.0)
assert math.isclose(math.cos(math.radians(90)), 0, abs_tol=1e-12)  # espira deitada ao longo das linhas: fluxo zero


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças do magnetismo ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def simbolo_campo(c, cx, cy, r, sai=True, a=1.0, cor=None, escuro=False):
    if a <= 0:
        return
    cor = cor or (BR if escuro else TINTA)
    c.drawCircle(cx, cy, r, M.paint(cor, a, stroke=max(3, r * 0.14)))
    if sai:
        c.drawCircle(cx, cy, r * 0.28, M.paint(cor, a))
    else:
        k = r * 0.62
        M.line(c, cx - k, cy - k, cx + k, cy + k, cor, a, max(3, r * 0.14))
        M.line(c, cx - k, cy + k, cx + k, cy - k, cor, a, max(3, r * 0.14))


def folha_campo(c, t, t0, x0, y0, cols, lins, passo, sai=True, r=20, cor=None, d=0.04, a=1.0):
    for i in range(lins):
        for j in range(cols):
            k = i * cols + j
            E.foco(c, t, t0 + d * k, 0.35, lambda a_, i=i, j=j: simbolo_campo(c, x0 + j * passo, y0 + i * passo, r, sai, a_ * a, cor), sobe=0)


def barra_ima(c, cx, cy, w=360, h=110, a=1.0, ang=0.0):
    """ímã em barra com o norte no sentido ang (graus da Física); letras em pé"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(-ang)
    for lado, cor in ((1, E.COR), (-1, NEG)):
        x0 = 0 if lado > 0 else -w / 2
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, -h / 2), skia.Point(0, h / 2)],
                                                   [M.hexc(E.mix(cor, BR, 0.2), a), M.hexc(E.mix(cor, "#000000", 0.2), a)]))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, -h / 2, w / 2, h), 10, 10), p)
    c.restore()
    ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
    sz = min(h, w / 2) * 0.55
    E._meio(c, "N", cx + ux * w / 4, cy + uy * w / 4, sz, "g", BR, a)
    E._meio(c, "S", cx - ux * w / 4, cy - uy * w / 4, sz, "g", BR, a)


def bobina(c, x0, cy, w, ry, n, a=1.0, cor=None, frente=True):
    """bobina de lado: n espiras entre x0 e x0 + w. frente=False desenha só a metade de trás (para o ímã passar por dentro)"""
    if a <= 0:
        return
    cor = cor or TINTA
    passo = w / n
    for k in range(n):
        x = x0 + passo * (k + 0.5)
        if not frente:
            c.drawOval(skia.Rect.MakeXYWH(x - passo * 0.32, cy - ry, passo * 0.64, 2 * ry), M.paint(cor, a * 0.4, stroke=5))
        else:
            p = skia.Path(); p.moveTo(x, cy - ry)
            p.cubicTo(x + passo * 0.55, cy - ry * 0.6, x + passo * 0.55, cy + ry * 0.6, x, cy + ry)
            c.drawPath(p, M.paint(cor, a, stroke=7))


def medidor(c, cx, cy, r, val, a=1.0, rot="corrente"):
    """medidor de ponteiro: zero no meio, val de −1 a 1"""
    if a <= 0:
        return
    M.rrect(c, cx - r, cy - r * 0.75, 2 * r, r * 1.1, 18, BR, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - r, cy - r * 0.75, 2 * r, r * 1.1), 18, 18), M.paint(TINTA, a, stroke=5))
    E.arco(c, cx, cy + r * 0.2, r * 0.75, 215, 110, TINTA2, 5, a)
    M.line(c, cx, cy - r * 0.6, cx, cy - r * 0.48, TINTA, a, 4)
    g = math.radians(90 - 50 * max(-1, min(1, val)))
    M.line(c, cx, cy + r * 0.2, cx + math.cos(g) * r * 0.72, cy + r * 0.2 - math.sin(g) * r * 0.72, E.COR, a, 7)
    c.drawCircle(cx, cy + r * 0.2, r * 0.08, M.paint(TINTA, a))
    centro(c, rot, cx, cy + r * 0.7, max(36, r * 0.24), "i", TINTA2, a)


def lembrete2(c, t, C, cena, itens, desenhos):
    """lembrete de duas coisas (o mesmo da FIS-CIN-001)"""
    E.frase(c, t, C[cena] + 0.2, ps("lembre", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def troca(c, t, itens, fn):
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def espira_lado(c, cx, cy, R, ang, a=1.0, normal=True):
    """espira vista de lado (um segmento) no ângulo ang (graus, 90 = em pé) e a reta perpendicular a ela, tracejada"""
    g = math.radians(ang)
    dx, dy = math.cos(g) * R, -math.sin(g) * R
    M.line(c, cx - dx, cy - dy, cx + dx, cy + dy, E.COR, a, 12)
    if normal:
        nx, ny = -dy / R, dx / R
        M.line(c, cx - nx * 230, cy - ny * 230, cx + nx * 230, cy + ny * 230, TINTA, a * 0.8, 4, dash=E.TRACO)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        x0, cy, w, ry = 980, 560, 560, 150
        E.foco(c, t, C["s01.a"], 0.5, lambda a: bobina(c, x0, cy, w, ry, 8, a, frente=False))
        # o ímã entra e sai até s01.c; depois fica parado dentro
        if t < C["s01.c"]:
            xm = x0 - 260 + 330 * (0.5 - 0.5 * math.cos((t - C["s01.a"]) * 2.4))
            val = math.sin((t - C["s01.a"]) * 2.4) * ep(t, C["s01.b"], 0.3)
        else:
            q = ease_io(prog(t, C["s01.c"], 0.8))
            xm = lerp(x0 + 70, x0 + 200, q)
            val = 0.7 * (1 - q)
        E.foco(c, t, C["s01.a"] + 0.2, 0.4, lambda a: barra_ima(c, xm, cy, 380, 110, a))
        E.foco(c, t, C["s01.a"], 0.5, lambda a: bobina(c, x0, cy, w, ry, 8, a))
        E.foco(c, t, C["s01.a"] + 0.4, 0.5, lambda a: medidor(c, x0 + w / 2, 900, 120, val, a))
        if t >= C["s01.a"] + 0.4:
            M.line(c, x0 + 30, cy + ry, x0 + w / 2 - 80, 860, TINTA, 1, 4)
            M.line(c, x0 + w - 30, cy + ry, x0 + w / 2 + 80, 860, TINTA, 1, 4)
        E.frase(c, t, C["s01.a"], [("1831", "g", 130)], XE, 280)
        E.frase(c, t, C["s01.a"] + 0.6, ps("Faraday: ímã e bobina", "i", 60, TINTA2), XE, 380, passo=0.1)
        E.frase(c, t, C["s01.b"], ps("corrente", "g", 70, COR) + ps("sem pilha", "i", 74), XE, 520, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("ímã parado:", "i", 64) + [("zero", "g", 64, ERRADO)], XE, 640, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("só o", "i", 74) + [("movimento", "g", 74, COR)], XE, 800, passo=0.12)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    itens = (("s02.a", "fluxo magnético", 1.4), ("s02.b", "o que muda o fluxo", 0), ("s02.c", "a tensão induzida", 0))
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def linhas(a, x, y):
        c.save(); c.translate(x - 40, y); c.scale(0.4, 0.4)
        F.linhas_campo(c, 99, 0, 0, 0, 300, 2, h=90)
        barra_ima(c, 0, 0, 300, 90, a)
        c.restore()

    def area(a, x, y):
        M.rrect(c, x - 160, y - 70, 240, 140, 6, AREA, a)
        c.drawRect(skia.Rect.MakeXYWH(x - 160, y - 70, 240, 140), M.paint(TINTA, a, stroke=4))
        centro(c, "b", x - 40, y + 110, 40, "g", TINTA, a)
        E.escreve(c, "h", x + 95, y + 14, 40, "g", TINTA, a)
    lembrete2(c, t, C, "s03", (("s03.b", "linhas de campo:", "o campo B (T)"), ("s03.c", "área do retângulo:", "base × altura")), (linhas, area))


# ---------------- fluxo ----------------
def b_fluxo(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("uma", "i", 84) + [("espira", "g", 84, COR)], XE, 220, passo=0.12)
        cx, cy, R = 1300, 600, 260
        if t >= C["s04.a"]:
            p = ease_io(prog(t, C["s04.a"], 0.7))
            c.drawArc(skia.Rect.MakeXYWH(cx - R, cy - R, 2 * R, 2 * R), -90, 360 * p, False, M.paint(TINTA, 1, stroke=10))
        E.foco(c, t, C["s04.c"], 0.5, lambda a: c.drawCircle(cx, cy, R - 6, M.paint(AREA, a)))
        for k, (dx, dy) in enumerate([(i * 130, j * 130) for i in range(-3, 4) for j in range(-3, 4)]):
            if dx * dx + dy * dy < (R + 120) ** 2:
                E.foco(c, t, C["s04.b"] + 0.03 * k, 0.3, lambda a, dx=dx, dy=dy: simbolo_campo(c, cx + dx, cy + dy, 22, True, a), sobe=0)
        E.frase(c, t, C["s04.b"], ps("campo passando por dentro", "i", 56, TINTA2), XE, 340, passo=0.1)
        E.frase(c, t, C["s04.c"], [("fluxo:", "g", 64, COR), ("quanto campo", "i", 66)], XE, 500, passo=0.12)
        E.frase(c, t, C["s04.c"] + 0.6, ps("atravessa a espira", "i", 66), XE, 590, passo=0.12)
        E.foco(c, t, C["s04.d"], 0.5, lambda a: E.formula(c, "Φ", XE + 60, 840, 200, "g", COR, a))
        E.foco(c, t, C["s04.d"] + 0.3, 0.4, lambda a: E.escreve(c, "letra grega fi", XE + 260, 820, 50, "i", TINTA2, a))
        return
    if t < C["s06"]:
        F.formula_legenda(c, t, C["s05.b"], "Φ = B · A", [("B", "campo", "T"), ("A", "área da espira", "m^2")], XE, 380, 150,
                          tl=[C["s05.c"], C["s05.d"]])
        E.frase(c, t, C["s05.a"], ps("campo atravessando", "i", 64) + [("de frente", "g", 64, COR)], XE, 200, passo=0.12)
        E.foco(c, t, C["s05.e"], 0.5, lambda a: E.pilula(c, "unidade: weber (Wb) = T · m²", XE + 330, 880, 50, "g", fundo=TINTA, a=a))
        cx, cy = 1450, 560
        E.foco(c, t, C["s05.a"], 0.5, lambda a: (M.rrect(c, cx - 220, cy - 160, 440, 320, 8, AREA, a),
                                                 c.drawRect(skia.Rect.MakeXYWH(cx - 220, cy - 160, 440, 320), M.paint(TINTA, a, stroke=9))))
        folha_campo(c, t, C["s05.a"] + 0.3, cx - 150, cy - 100, 4, 3, 100, True, 20)
        return
    E.frase(c, t, C["s06"], ps("e se a espira", "i", 70) + [("girar?", "g", 70, COR)], XE, 200, passo=0.12)
    cx, cy = 1450, 600
    for k in range(5):
        yy = cy - 260 + k * 130
        F.seta(c, cx - 360, yy, cx + 400, yy, TINTA2, 0.7, 4, 20)
    if t < C["s06.a"]:
        ang = 90
    elif t < C["s06.c"]:
        ang = lerp(90, 0, ease_io(prog(t, C["s06.a"], 1.0)))
    else:
        ang = lerp(0, 50, ease_io(prog(t, C["s06.c"], 1.0)))
    espira_lado(c, cx, cy, 230, ang)
    E.foco(c, t, C["s06.b"], 0.5, lambda a: E.pilula(c, "deitada: Φ = 0", XE + 200, 420, 56, "g", fundo=TINTA, a=a))
    if t >= C["s06.c"] + 1.0:
        E.foco(c, t, C["s06.c"] + 1.0, 0.4, lambda a: E.escreve(c, "θ", cx + 150, cy - 40, 60, "g", COR, a))
    E.foco(c, t, C["s06.c"] + 0.5, 0.5, lambda a: E.formula(c, "Φ = B · A · cos θ", XE, 640, 90, "g", TINTA, a))
    E.foco(c, t, C["s06.c"] + 1.2, 0.4, lambda a: E.escreve(c, "θ: entre B e a reta em pé", XE, 740, 50, "b", TINTA2, a))
    E.foco(c, t, C["s06.c"] + 1.4, 0.4, lambda a: E.escreve(c, "sobre a espira (tracejada)", XE, 810, 50, "b", TINTA2, a))


# ---------------- o que muda ----------------
def b_muda(c, t, C, b):
    E.frase(c, t, C["s07.a"], [("três", "g", 90, COR), ("coisas mudam o fluxo", "i", 90)], XE, 220, passo=0.12)
    xs = (380, 960, 1540)
    for i, (k, nome) in enumerate((("s07.b", "o campo"), ("s07.c", "a área"), ("s07.d", "o ângulo"))):
        x = xs[i]
        p = ep(t, C[k], 0.5)
        if p <= 0:
            continue
        E.caixa_pontilhada(c, x - 260, 330, 520, 520, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(nome, "g", 64, COR)], x, 920, "center")
        dt = t - C[k]
        if i == 0:  # o ímã se aproxima da espira
            c.drawOval(skia.Rect.MakeXYWH(x + 60, 450, 70, 280), M.paint(TINTA, p, stroke=9))
            barra_ima(c, x - 150 + 60 * math.sin(dt * 2), 590, 220, 70, p)
        elif i == 1:  # a área cresce
            s = 120 + 70 * (0.5 - 0.5 * math.cos(dt * 2))
            M.rrect(c, x - s, 590 - s, 2 * s, 2 * s, 6, AREA, p)
            c.drawRect(skia.Rect.MakeXYWH(x - s, 590 - s, 2 * s, 2 * s), M.paint(TINTA, p, stroke=8))
        else:  # a espira gira
            for yy in (450, 590, 730):
                F.seta(c, x - 220, yy, x + 220, yy, TINTA2, 0.6 * p, 4, 18)
            espira_lado(c, x, 590, 140, 90 - 40 * dt % 360, p, normal=False)


# ---------------- Faraday ----------------
def b_faraday(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08"], [("lei de", "i", 90), ("Faraday", "g", 90, COR)], XE, 220)
        E.frase(c, t, C["s08.a"], ps("fluxo mudando:", "i", 64) + [("aparece tensão", "g", 64, COR)], XE, 380, passo=0.12)
        E.frase(c, t, C["s08.a"] + 1.2, ps("o empurrão que faz a corrente andar", "i", 56, TINTA2), XE, 470, passo=0.1)
        E.foco(c, t, C["s08.b"], 0.5, lambda a: E.pilula(c, "força eletromotriz (fem)", XE + 340, 620, 56, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s08.b"] + 0.8, 0.4, lambda a: E.escreve(c, "não é força!", XE + 720, 640, 56, "i", ERRADO, a))
        E.foco(c, t, C["s08.c"], 0.5, lambda a: E.formula(c, "em volt (V)", XE, 800, 90, "g", COR, a))
        E.foco(c, t, C["s08.c"] + 0.6, 0.4, lambda a: E.escreve(c, "a unidade de tensão (outra aula)", XE + 520, 790, 46, "i", TINTA2, a))
        return
    if t < C["s10"]:
        F.formula_legenda(c, t, C["s09.a"], "ε = f{ΔΦ}{Δt}", [("ΔΦ", "quanto o fluxo mudou", "Wb"), ("Δt", "em quanto tempo", "s")],
                          XE, 330, 150, tl=[C["s09.b"], C["s09.c"]])
        E.foco(c, t, C["s09.a"] + 0.4, 0.4, lambda a: (E.formula(c, "ε:", 1050, 280, 50, "g", COR, a), E.escreve(c, "épsilon, a tensão induzida", 1130, 280, 46, "i", TINTA2, a)))
        E.foco(c, t, C["s09.d"], 0.5, lambda a: E.pilula(c, "mudança rápida: tensão grande", 1350, 600, 50, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s09.e"], 0.5, lambda a: E.formula(c, "bobina:  ε = N · f{ΔΦ}{Δt}", 1050, 820, 84, "g", TINTA, a))
        return
    E.foco(c, t, C["s10.a"], 0.5, lambda a: E.formula(c, "A = 0,2 · 0,1 = 0,02 m^2", XE, 240, 70, "g", TINTA, a))
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "B: 0,5 T → 0,   em 0,1 s", XE, 380, 70, "g", TINTA, a))
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.formula(c, "ΔΦ = 0,5 · 0,02 = 0,01 Wb", XE, 560, 80, "g", TINTA, a))
    E.foco(c, t, C["s10.e"], 0.5, lambda a: E.formula(c, "ε = f{0,01}{0,1}", XE, 790, 100, "g", TINTA, a))
    bola_txt(c, t, C["s10.e"] + 0.6, "0,1 V", 1480, 720, 170, 90)


# ---------------- barra nos trilhos ----------------
def b_barra(c, t, C, b):
    x0, x1, ya, yb = 940, 1840, 380, 780
    t0 = C["s11.d"]
    xb = 1120 + (90 * max(0.0, t - t0) if t >= t0 else 0)
    xb = min(xb, 1560)
    if t >= C["s11.c"]:
        c.drawRect(skia.Rect.MakeLTRB(x0, ya, xb, yb), M.paint(AREA, ep(t, C["s11.c"], 0.4)))
    folha_campo(c, t, C["s11.b"], x0 + 70, ya + 60, 7, 3, 130, False, 20, TINTA2)
    if t >= C["s11.a"]:
        q = ep(t, C["s11.a"], 0.4)
        M.line(c, x0, ya, x1, ya, TINTA, q, 8); M.line(c, x0, yb, x1, yb, TINTA, q, 8)
        M.line(c, x0, ya, x0, yb, TINTA, q, 8)
        M.rrect(c, xb - 14, ya - 30, 28, yb - ya + 60, 8, "#8A8A96", q)
        if t >= t0:
            F.seta(c, xb + 20, (ya + yb) / 2, xb + 180, (ya + yb) / 2, VEL, 1, 10)
            E.escreve(c, "v", xb + 120, (ya + yb) / 2 - 30, 56, "g", VEL)
        E.foco(c, t, C["s11.a"] + 0.4, 0.4, lambda a: E.escreve(c, "L", xb - 70, ya + 80, 60, "g", COR, a))
    E.frase(c, t, C["s11.a"], ps("barra nos", "i", 70) + [("trilhos", "g", 70, COR)], XE, 220, passo=0.12)
    if t < C["s12"]:
        E.frase(c, t, C["s11.d"], ps("a área", "i", 64) + [("cresce", "g", 64, COR)], XE, 480, passo=0.12)
        E.frase(c, t, C["s11.d"] + 0.6, ps("e o fluxo também", "i", 64), XE, 580, passo=0.12)
        return
    E.foco(c, t, C["s12.a"], 0.5, lambda a: E.formula(c, "por segundo: L · v", XE, 400, 70, "g", TINTA, a))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "ε = B · L · v", XE, 560, 110, "g", COR, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "0,5 · 0,4 · 5", XE, 720, 80, "g", TINTA, a))
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.formula(c, "= 0,2 · 5", XE, 840, 80, "g", TINTA, a))
    E.foco(c, t, C["s12.e"], 0.5, lambda a: E.pilula(c, "1 V", XE + 480, 820, 90, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("ímã forte", "i", 64) + [("parado", "g", 64, ERRADO)] + ps("na bobina", "i", 64), XE, 320, passo=0.12)
    x0, cy, w, ry = 1000, 560, 560, 150
    E.foco(c, t, C["s13.a"], 0.5, lambda a: (bobina(c, x0, cy, w, ry, 8, a, frente=False), barra_ima(c, x0 + w / 2, cy, 380, 110, a), bobina(c, x0, cy, w, ry, 8, a)))
    E.foco(c, t, C["s13.a"] + 0.4, 0.5, lambda a: medidor(c, x0 + w / 2, 900, 120, 0, a))
    E.frase(c, t, C["s13.b"], ps("fluxo grande, mas", "i", 60) + [("não muda", "g", 60, COR)], XE, 480, passo=0.12)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "ΔΦ = 0", XE, 640, 90, "g", TINTA, a))
    E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "ε = 0", XE + 420, 640, 90, "g", ERRADO, a))
    E.frase(c, t, C["s13.e"], ps("conta a", "i", 60) + [("mudança", "g", 60, COR)] + ps("e não o tamanho", "i", 60), XE, 800, passo=0.12)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 180, "center")
        E.foco(c, t, C["s14.a"], 0.5, lambda a: E.pilula(c, "o fluxo está mudando?", W / 2, 380, 70, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s14.b"], 0.5, lambda a: (F.seta(c, 800, 440, 560, 600, E.CLARO, a, 8), E.pilula(c, "não: ε = 0, sem conta", 520, 680, 56, "g", fundo="#3A3A48", a=a)))
        E.foco(c, t, C["s14.c"], 0.5, lambda a: (F.seta(c, 1120, 440, 1360, 600, E.CLARO, a, 8), E.pilula(c, "barra andando: B · L · v", 1420, 680, 56, "g", fundo="#3A3A48", a=a)))
        return
    E.frase(c, t, C["s15.a"], [("B · L · v", "g", 70, BR), ("é o próprio", "i", 70, CLARO), ("ΔΦ/Δt", "g", 70, BR)], W / 2, 220, "center", 0.12)
    E.formula_em(c, t, C["s15.b"], "T · m · f{m}{s}", W / 2 - 260, 500, 110, "g", BR, "center")
    E.formula_em(c, t, C["s15.c"], "= f{Wb}{s} = V", W / 2 + 260, 500, 110, "g", CLARO, "center")
    E.frase(c, t, C["s15.d"], [("campo ou ângulo mudando?", "i", 58, CLARO), ("ΔΦ/Δt", "g", 56, BR)], W / 2, 860, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    if t < C["s17"]:
        E.foco(c, t, C["s16.a"], 0.5, lambda a: E.formula(c, "N = 10 espiras", XE, 340, 72, "g", TINTA, a))
        E.foco(c, t, C["s16.b"], 0.5, lambda a: E.formula(c, "Φ: 0,02 Wb → 0,08 Wb", XE, 480, 72, "g", TINTA, a))
        E.foco(c, t, C["s16.b"] + 1.5, 0.5, lambda a: E.formula(c, "Δt = 0,2 s", XE, 600, 72, "g", TINTA, a))
        E.frase(c, t, C["s16.c"], [("ε = ?", "g", 80, COR)], XE, 760)
        E.frase(c, t, C["s16.d"], [("e com o ímã", "i", 64), ("parado?", "g", 64, COR)], XE, 880, passo=0.12)
        x0, cy, w, ry = 1150, 560, 480, 140
        E.foco(c, t, C["s16.a"], 0.5, lambda a: (bobina(c, x0, cy, w, ry, 10, a, frente=False), bobina(c, x0, cy, w, ry, 10, a)))
        xm = lerp(x0 - 250, x0 - 120, ease_io(prog(t, C["s16.b"], 2.0)))
        E.foco(c, t, C["s16.b"], 0.5, lambda a: barra_ima(c, xm, cy, 300, 90, a))
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=500, r=200)
        E.frase(c, t, C["s17"], [("N = 10,", "g", 60), ("Δt = 0,2 s", "g", 60)], XE, 400, passo=0.12)
        E.foco(c, t, C["s17"] + 0.2, 0.4, lambda a: E.formula(c, "Φ: 0,02 → 0,08 Wb", XE, 500, 60, "g", TINTA, a))
        E.frase(c, t, C["s17"] + 0.4, [("ε = ?", "g", 60, COR), ("e parado?", "g", 60)], XE, 620, passo=0.12)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s19"]:
        E.foco(c, t, C["s18.a"], 0.5, lambda a: E.formula(c, "ΔΦ = 0,08 − 0,02", XE, 280, 90, "g", TINTA, a))
        E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "= 0,06 Wb", XE + 760, 280, 90, "g", COR, a))
        E.foco(c, t, C["s18.c"], 0.5, lambda a: E.formula(c, "f{0,06}{0,2} = 0,3", XE, 520, 100, "g", TINTA, a))
        E.foco(c, t, C["s18.d"], 0.5, lambda a: E.formula(c, "× 10 espiras", XE, 760, 90, "g", TINTA, a))
        bola_txt(c, t, C["s18.e"], "3 V", 1450, 640, 170, 110)
        return
    x0, cy, w, ry = 1000, 560, 560, 150
    E.foco(c, t, C["s19.a"], 0.5, lambda a: (bobina(c, x0, cy, w, ry, 8, a, frente=False), barra_ima(c, x0 + w / 2, cy, 380, 110, a), bobina(c, x0, cy, w, ry, 8, a)))
    E.foco(c, t, C["s19.a"] + 0.3, 0.5, lambda a: medidor(c, x0 + w / 2, 900, 120, 0, a))
    E.frase(c, t, C["s19.a"], ps("ímã parado:", "i", 70) + [("Φ não muda", "g", 70)], XE, 300, passo=0.12)
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.pilula(c, "ε = 0", XE + 150, 500, 90, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s20.a", "Φ = B · A"), ("s20.b", None), ("s20.c", "ε = f{ΔΦ}{Δt}"))
        for i, (k, f) in enumerate(itens):
            y = 360 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            if f:
                E.formula_em(c, t, C[k] + 0.1, f, 400, y, 76, "g", TINTA)
            else:
                E.frase(c, t, C[k] + 0.1, [("campo, área e ângulo", "g", 70), ("mudam o fluxo", "i", 74)], 400, y, passo=0.12)
        E.frase(c, t, C["s20.d"], ps("próxima aula: o sentido da corrente,", "i", 58, TINTA2) + [("lei de Lenz", "g", 58, COR)], W / 2, 920, "center", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.foco(c, t, C["s21.a"], 0.5, lambda a: E.pilula(c, "Inscreva-se", W / 2, 460, 90, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.a"] + 0.3, 0.8))
    E.cursor(c, lerp(1300, 1080, p), lerp(800, 490, p), ep(t, C["s21.a"] + 0.2, 0.4))
    E.frase(c, t, C["s21.b"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], W / 2, 760, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, fluxo=b_fluxo, muda=b_muda, faraday=b_faraday, barra=b_barra, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
