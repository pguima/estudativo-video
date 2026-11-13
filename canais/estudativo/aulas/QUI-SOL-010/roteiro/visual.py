"""Visual — Estudativo · QUI-SOL-010: osmose e pressão osmótica.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a das propriedades coligativas (cabeçalho de
QUI-SOL-008/roteiro/visual.py): água = bolinha azul-clara, soluto = bolinha turquesa maior. Peças desta aula (candidatas ao kit):
membrana (traço tracejado com furos), tubo_u (tubo em U com a membrana no meio, níveis animados, êmbolo opcional), hemacia
(célula vermelha que incha ou murcha) e setas_agua (setas azuis no sentido da osmose). Todo instante vem de C[...]."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Soluções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-SOL-010_osmose_pressao_osmotica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("membrana", "osmose", "pressao", "celulas", "reversa", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AGUA_P = "#7CC4EA"
SETA_AGUA = "#2E86AB"
HEMACIA = "#D7263D"

# a questão: a água vai do lado menos concentrado para o mais concentrado
LADO = dict(A=0.1, B=0.3)
assert max(LADO, key=LADO.get) == "B"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def rotulo(c, t, t0, s, cx, y, size=48, cor=TINTA2, est="i"):
    E.foco(c, t, t0, 0.4, lambda a: centro(c, s, cx, y, size, est, cor, a))


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def particula(c, x, y, r, cor, a=1.0):
    c.drawCircle(x, y, r, M.paint(cor, a))
    c.drawCircle(x, y, r, M.paint(M.mix(cor, "#000000", 0.35), 0.6 * a, stroke=2))


def membrana(c, x, y0, y1, a=1.0, cor=TINTA2):
    """membrana semipermeável vertical: traço grosso com furinhos"""
    if a <= 0:
        return
    n = int((y1 - y0) / 26)
    for k in range(n):
        yy = y0 + k * 26
        M.line(c, x, yy + 4, x, yy + 18, cor, a, 9)


def setas_agua(c, t, t0, x0, x1, y, n=3, a=1.0, d=0.6):
    q = ep(t, t0, 0.4) * a
    if q <= 0:
        return
    for k in range(n):
        u = ((t - t0) * 0.8 + k / n) % 1.0
        xx = lerp(x0, x1, u)
        M.arrow(c, xx - 40 * (1 if x1 > x0 else -1), y + k * 24 - 24, xx, y + k * 24 - 24, SETA_AGUA, q * (1 - abs(u - 0.5)), 5, 18)


def tubo_u(c, t, x, y, w, h, ne, nd, se, sd, a=1.0, embolo=None, semente=3, rot=("", "")):
    """tubo em U: dois braços (esquerdo e direito) ligados embaixo, membrana no meio. ne, nd = níveis 0..1 de cada braço;
    se, sd = quantas partículas de soluto em cada lado; embolo = (lado, descida 0..1) desenha o êmbolo sobre o braço"""
    if a <= 0:
        return
    bw = w * 0.32
    xl, xr = x, x + w - bw
    yb = y + h
    base_h = bw
    vidro = M.paint(Q.VIDRO, a, stroke=6)
    vidro.setStrokeJoin(skia.Paint.kRound_Join)
    # líquido
    c.save()
    for (xx, nv, lado) in ((xl, ne, 0), (xr, nd, 1)):
        top = yb - base_h - (h - base_h) * nv
        c.drawRect(skia.Rect.MakeLTRB(xx, top, xx + bw, yb), M.paint(Q.AGUA, 0.9 * a))
        M.line(c, xx, top, xx + bw, top, M.mix(Q.AGUA, "#FFFFFF", 0.5), a, 4)
    c.drawRect(skia.Rect.MakeLTRB(xl, yb - base_h, xr + bw, yb), M.paint(Q.AGUA, 0.9 * a))
    c.restore()
    # partículas
    rnd = random.Random(semente)
    for (x0, x1, n_sol, nv) in ((xl, x + w / 2 - 12, se, ne), (x + w / 2 + 12, xr + bw, sd, nd)):
        top = yb - base_h - (h - base_h) * nv
        for k in range(10):
            px, py = x0 + 14 + rnd.random() * (x1 - x0 - 28), yb - 14 - rnd.random() * (base_h - 28)
            particula(c, px + 3 * math.sin(t * 3 + k), py, 9, AGUA_P, a)
        for k in range(n_sol):
            # soluto fica no braço do seu lado
            bx = xl if x0 == xl else xr
            px = bx + 18 + rnd.random() * (bw - 36)
            py = top + 20 + rnd.random() * max(10, (yb - top - 40))
            if x0 == xl:
                px = min(px, x + w / 2 - 26)
            else:
                px = max(px, x + w / 2 + 26)
            particula(c, px + 3 * math.sin(t * 2 + k), py, 13, E.COR, a)
    # vidro
    pth = skia.Path()
    pth.moveTo(xl, y); pth.lineTo(xl, yb - 20); pth.quadTo(xl, yb, xl + 20, yb); pth.lineTo(xr + bw - 20, yb); pth.quadTo(xr + bw, yb, xr + bw, yb - 20); pth.lineTo(xr + bw, y)
    pth.moveTo(xl + bw, y); pth.lineTo(xl + bw, yb - base_h); pth.lineTo(xr, yb - base_h); pth.lineTo(xr, y)
    c.drawPath(pth, vidro)
    membrana(c, x + w / 2, yb - base_h + 4, yb - 4, a)
    for xx, r_ in ((xl + bw / 2, rot[0]), (xr + bw / 2, rot[1])):
        if r_:
            centro(c, r_, xx, yb + 64, 46, "g", TINTA, a)
    if embolo:
        lado, desce = embolo
        xx = xl if lado == 0 else xr
        nv = ne if lado == 0 else nd
        top = yb - base_h - (h - base_h) * nv
        ye = lerp(y - 40, top - 8, desce)
        M.rrect(c, xx + 6, ye - 24, bw - 12, 24, 6, TINTA, a)
        M.rrect(c, xx + bw / 2 - 8, ye - 180, 16, 160, 6, TINTA2, a)
        M.rrect(c, xx + bw / 2 - 50, ye - 196, 100, 20, 8, TINTA, a)
        M.arrow(c, xx + bw + 40, ye - 150, xx + bw + 40, ye - 40, ERRADO, a, 6, 22)


def hemacia(c, cx, cy, r, estado=0.0, a=1.0, t=0.0):
    """estado: −1 murcha, 0 normal, +1 inchada (e estourando)"""
    if a <= 0:
        return
    rr = r * (1 + 0.35 * max(0, estado)) * (1 - 0.25 * max(0, -estado))
    pth = skia.Path()
    n = 48
    for k in range(n + 1):
        ang = 2 * math.pi * k / n
        enrug = (1 - 0.18 * max(0, -estado) * (0.5 + 0.5 * math.sin(ang * 7))) if estado < 0 else 1
        px, py = cx + rr * math.cos(ang) * enrug, cy + rr * 0.62 * math.sin(ang) * enrug
        (pth.moveTo if k == 0 else pth.lineTo)(px, py)
    pth.close()
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx - rr * 0.3, cy - rr * 0.2), rr * 1.3,
                                               [M.hexc("#F2727F", a), M.hexc(HEMACIA, a), M.hexc("#8E1B28", a)], [0, 0.5, 1]))
    c.drawPath(pth, p)
    c.drawOval(skia.Rect.MakeXYWH(cx - rr * 0.45, cy - rr * 0.2, rr * 0.9, rr * 0.4), M.paint("#B71C2C", 0.5 * a))


# ---------------- gancho ----------------
def carne(c, cx, cy, w, h, a=1.0):
    """pedaço de carne-seca com cristais de sal"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 40, "#8E3B2E", a)
    M.rrect(c, cx - w / 2 + 20, cy - h / 2 + 16, w - 40, h * 0.3, 30, "#A9503F", a)
    rnd = random.Random(2)
    for k in range(30):
        x, y = cx - w / 2 + 30 + rnd.random() * (w - 60), cy - h / 2 + 20 + rnd.random() * (h - 40)
        M.rrect(c, x - 6, y - 6, 12, 12, 2, "#FFFFFF", 0.9 * a)


def micro(c, cx, cy, r, murcha=0.0, a=1.0):
    """micróbio: cápsula verde que murcha quando perde água"""
    if a <= 0:
        return
    rr = r * (1 - 0.35 * murcha)
    M.rrect(c, cx - rr * 1.4, cy - rr * 0.7, rr * 2.8, rr * 1.4, rr * 0.7, M.mix("#6FBF73", "#7A6A4F", murcha), a)
    for k in range(3):
        c.drawCircle(cx - rr * 0.6 + k * rr * 0.6, cy, rr * 0.18, M.paint("#2F6B33", a))


def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.6, lambda a: carne(c, 1400, 560, 560, 300, a))
        E.frase(c, t, C["s01.a"], [("carne-seca:", "g", 66)] + ps("meses fora da geladeira", "i", 62), XE, 250, passo=0.1)
        E.frase(c, t, C["s01.b"], ps("quem protege é o", "i", 62) + [("sal", "g", 60, COR)], XE, 400, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("mas ele", "i", 62) + [("não envenena", "g", 58, ERRADO)] + ps("os micróbios", "i", 62), XE, 520, passo=0.1)
        m = ep(t, C["s01.d"] + 0.4, 1.4)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: micro(c, 1400, 880, 90, m, a))
        setas_agua(c, t, C["s01.d"] + 0.2, 1560, 1780, 890, 2, ep(t, C["s01.d"], 0.3) * (1 - ep(t, C["s01.d"] + 2.4, 0.4)))
        E.frase(c, t, C["s01.d"], ps("ele", "i", 66) + [("tira a água", "g", 62, COR)] + ps("de dentro deles", "i", 66), XE, 720, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("para", "i", 74), ("que", "i", 74), ("lado", "g", 70, COR), ("a", "i", 74), ("água", "i", 74), ("passa", "i", 74)]),
                 (C["s02.c"], [("o", "i", 74), ("sal", "g", 70), ("que", "i", 74), ("conserva", "g", 70, COR)]),
                 (C["s02.d"], [("tirar", "i", 74), ("o", "i", 74), ("sal", "i", 74), ("do", "i", 74), ("mar", "g", 70, COR)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 76, TINTA2), XE, 170)
    E.frase(c, t, C["s03.a"], [("água", "g", 66), ("=", "g", 66, TINTA2), ("solvente", "g", 66, COR)], XE, 330, passo=0.12)
    E.frase(c, t, C["s03.a"] + 1.4, [("sal", "g", 66), ("ou", "i", 70), ("açúcar", "g", 66), ("=", "g", 66, TINTA2), ("soluto", "g", 66, COR)], XE, 450, passo=0.12)
    E.frase(c, t, C["s03.b"], ps("mais mol por litro:", "i", 62) + [("mais concentrada", "g", 58, COR)], XE, 640, passo=0.1)
    for k, n in enumerate((4, 14)):
        Q.bequer(c, t, C["s03.b"] + 0.4 + 0.3 * k, 1220 + 420 * k, 980, 260, 300, 0.75, Q.AGUA, graduacao=False,
                 particulas=dict(n=n, estado="gas", tipos=[(E.COR, 1.0)], r=9, semente=4 + k))
        rotulo(c, t, C["s03.b"] + 0.7 + 0.3 * k, ("menos", "mais")[k] + " concentrada", 1220 + 420 * k, 1050, 40, TINTA, "b")


# ---------------- membrana ----------------
def b_membrana(c, t, C, b):
    mx = 1380
    E.foco(c, t, C["s04.a"], 0.5, lambda a: membrana(c, mx, 260, 900, a))
    # água atravessa, soluto fica
    rnd = random.Random(6)
    if t >= C["s04.b"]:
        for k in range(8):
            u = ((t - C["s04.b"]) * 0.35 + k / 8) % 1.0
            y = 300 + k * 75
            particula(c, lerp(mx - 260, mx + 260, u), y, 12, AGUA_P, ep(t, C["s04.b"], 0.4))
    if t >= C["s04.c"]:
        for k in range(5):
            y = 330 + k * 120
            ph = rnd.random() * 6
            x = mx - 70 - 30 * (0.5 + 0.5 * math.sin(t * 2 + ph))
            particula(c, x, y, 22, E.COR, ep(t, C["s04.c"], 0.4))
    E.frase(c, t, C["s04.a"], ps("uma película com", "i", 62) + [("furinhos", "g", 58, COR)], XE, 250, passo=0.1)
    E.frase(c, t, C["s04.b"], [("água:", "g", 60), ("pequena,", "i", 62), ("passa", "g", 58, SETA_AGUA)], XE, 400, passo=0.12)
    E.frase(c, t, C["s04.c"], [("soluto:", "g", 60), ("maior,", "i", 62), ("fica", "g", 58, COR)], XE, 520, passo=0.12)
    E.frase(c, t, C["s04.d"], [("membrana", "g", 80, COR)], XE, 700)
    E.frase(c, t, C["s04.d"] + 0.5, [("semipermeável", "g", 80, COR)], XE, 800)
    rotulo(c, t, C["s04.e"], "deixa passar só uma parte", XE + 330, 880, 46)
    if t >= C["s05"]:
        def s05():
            c.drawRect(skia.Rect.MakeWH(W, H), M.paint("#F4F2EC", ep(t, C["s05"], 0.4)))
            E.frase(c, t, C["s05.a"], ps("a membrana das", "i", 66) + [("células", "g", 62, COR)] + ps("funciona parecido", "i", 66), XE, 300, passo=0.1)
            E.foco(c, t, C["s05.a"] + 0.6, 0.5, lambda a: hemacia(c, 700, 620, 180, 0, a))
            E.frase(c, t, C["s05.b"], ps("e também:", "i", 60, TINTA2), 1100, 540, passo=0.1)
            pilula_em(c, t, C["s05.b"] + 0.6, "papel-celofane", 1400, 650, 54, TINTA)
            pilula_em(c, t, C["s05.b"] + 1.2, "plásticos de laboratório", 1400, 760, 54, TINTA)
        s05()


# ---------------- osmose ----------------
UX, UY, UW, UH = 1060, 280, 680, 620


def b_osmose(c, t, C, b):
    sobe = ease_io(prog(t, C["s06.d"], 2.4)) if t < C["s07"] else 1.0
    ne, nd = lerp(0.55, 0.35, sobe), lerp(0.55, 0.75, sobe)
    E.foco(c, t, C["s06.a"], 0.5, lambda a: tubo_u(c, t, UX, UY, UW, UH, ne, nd, 0, 8 if t >= C["s06.c"] else 0, a,
                                                   rot=("água pura" if t >= C["s06.b"] else "", "água com sal" if t >= C["s06.c"] else "")))
    setas_agua(c, t, C["s06.d"], UX + UW / 2 - 90, UX + UW / 2 + 90, UY + UH - 60, 2)
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], ps("tubo em", "i", 66) + [("U", "g", 66, COR)], XE, 250, passo=0.1)
        E.frase(c, t, C["s06.a"] + 1.0, ps("com a membrana no meio", "i", 56, TINTA2), XE, 330, passo=0.1)
        E.frase(c, t, C["s06.b"], [("esquerda:", "i", 60), ("água pura", "g", 58)], XE, 450, passo=0.12)
        E.frase(c, t, C["s06.c"], [("direita:", "i", 60), ("água com sal", "g", 58, COR)], XE, 550, passo=0.12)
        E.frase(c, t, C["s06.d"], ps("a água passa para o lado", "i", 58) + [("salgado", "g", 56, COR)], XE, 660, passo=0.1)
        E.frase(c, t, C["s06.e"], ps("e o nível dele", "i", 62) + [("sobe", "g", 60, COR)], XE, 760, passo=0.1)
        return
    E.frase(c, t, C["s07.a"], [("osmose", "g", 130, COR)], XE, 330)
    E.frase(c, t, C["s07.a"] + 0.8, ps("a passagem da água pela membrana", "i", 50), XE, 420, passo=0.08)
    E.frase(c, t, C["s07.b"], ps("o sentido é sempre:", "i", 58, TINTA2), XE, 560, passo=0.1)
    E.frase(c, t, C["s07.c"], [("menos", "g", 58), ("concentrado", "i", 60), ("→", "g", 58, SETA_AGUA)], XE, 660, passo=0.1)
    E.frase(c, t, C["s07.c"] + 1.6, [("mais", "g", 58, COR), ("concentrado", "i", 60)], XE, 750, passo=0.1)
    rotulo(c, t, C["s07.d"], "a água vai diluir o lado concentrado", XE + 400, 880, 44, TINTA, "b")


# ---------------- pressão osmótica ----------------
def b_pressao(c, t, C, b):
    desce = ease_io(prog(t, C["s08.b"], 1.0))
    volta = ease_io(prog(t, C["s08.b"] + 0.8, 1.6))
    ne, nd = lerp(0.35, 0.55, volta), lerp(0.75, 0.55, volta)
    E.foco(c, t, C["s08"], 0.5, lambda a: tubo_u(c, t, UX, UY + 60, UW, UH - 60, ne, nd, 0, 8, a,
                                                 embolo=(1, desce) if t >= C["s08.b"] else None, rot=("água pura", "água com sal")))
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("dá para", "i", 64) + [("impedir", "g", 60, COR)], XE, 250, passo=0.12)
        E.frase(c, t, C["s08.b"], ps("empurre o lado salgado", "i", 54), XE, 360, passo=0.08)
        E.frase(c, t, C["s08.b"] + 1.2, ps("com um", "i", 54) + [("êmbolo", "g", 52)], XE, 430, passo=0.08)
        E.frase(c, t, C["s08.c"], [("pressão", "g", 58, COR), ("=", "g", 58, TINTA2), ("empurrão", "i", 56)], XE, 540, passo=0.08)
        E.frase(c, t, C["s08.c"] + 1.0, ps("espalhado na superfície", "i", 52, TINTA2), XE, 610, passo=0.08)
        E.frase(c, t, C["s08.d"], [("pressão", "g", 86, COR)], XE, 780)
        E.frase(c, t, C["s08.d"] + 0.5, [("osmótica", "g", 86, COR)], XE, 890)
        rotulo(c, t, C["s08.d"] + 1.2, "a mínima que segura a água no lugar", XE + 360, 970, 42)
        return
    E.frase(c, t, C["s09.a"], ps("mais concentrada:", "i", 64), XE, 400, passo=0.1)
    E.frase(c, t, C["s09.a"] + 1.0, [("a água quer entrar mais", "g", 54)], XE, 490, passo=0.1)
    E.frase(c, t, C["s09.b"], ps("maior a", "i", 66) + [("pressão osmótica", "g", 62, COR)], XE, 640, passo=0.12)


# ---------------- células ----------------
HX = (420, 960, 1500)


def b_celulas(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("a célula do sangue:", "i", 62) + [("hemácia", "g", 60, HEMACIA)], XE, 220, passo=0.1)
        dados = ((C["s10.b"], "água pura", "incha", +1, Q.AGUA, 0), (C["s10.c"], "água muito salgada", "murcha", -1, "#BFE3D8", 1), (C["s10.d"], "soro a 0,9%", "nada muda", 0, "#CFE9F2", 2))
        for ti, meio, efeito, est, cor, k in dados:
            cx = HX[k]
            M.rrect(c, cx - 230, 360, 460, 420, 30, cor, 0.7 * ep(t, ti, 0.4))
            e = est * ease_io(prog(t, ti + 0.6, 1.2))
            E.foco(c, t, ti, 0.4, lambda a, cx=cx, e=e: hemacia(c, cx, 570, 110, e, a))
            if est > 0:
                setas_agua(c, t, ti + 0.4, cx - 220, cx - 120, 580, 2)
            elif est < 0:
                setas_agua(c, t, ti + 0.4, cx + 120, cx + 220, 580, 2)
            rotulo(c, t, ti + 0.2, meio, cx, 840, 46, TINTA, "b")
            pilula_em(c, t, ti + 1.0, efeito, cx, 920, 48, E.COR if est == 0 else TINTA)
        rotulo(c, t, C["s10.e"], "a mesma concentração do sangue", HX[2], 1010, 40, COR, "b")
        return
    E.frase(c, t, C["s11"], ps("os nomes", "i", 66, TINTA2), XE, 200)
    nomes = ((C["s11.a"], "isotônica", "mesma concentração da célula", 0), (C["s11.b"], "hipertônica", "mais concentrada: a célula murcha", -1),
             (C["s11.c"], "hipotônica", "menos concentrada: a célula incha", 1))
    for k, (ti, nome, sub, est) in enumerate(nomes):
        y = 360 + k * 220
        E.foco(c, t, ti, 0.4, lambda a, y=y, est=est: hemacia(c, XE + 110, y - 20, 70, est, a))
        E.frase(c, t, ti + 0.2, [(nome, "g", 80, COR)], XE + 260, y)
        E.foco(c, t, ti + 0.6, 0.4, lambda a, sub=sub, y=y: E.escreve(c, sub, XE + 262, y + 66, 44, "i", TINTA2, a))


# ---------------- carne-seca ----------------
def b_carne(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("carne-seca", "g", 80, COR)], XE, 230)
    E.foco(c, t, C["s12.a"], 0.5, lambda a: carne(c, 1420, 380, 520, 260, a))
    E.frase(c, t, C["s12.b"], ps("o sal deixa o lado de fora", "i", 56), XE, 380, passo=0.1)
    E.frase(c, t, C["s12.b"] + 1.6, [("muito concentrado", "g", 56, COR)], XE, 460)
    m = ease_io(prog(t, C["s12.c"], 1.6))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: micro(c, 1420, 760, 80, m, a))
    setas_agua(c, t, C["s12.c"], 1420 + 120, 1420 + 300, 770, 2)
    E.frase(c, t, C["s12.c"], ps("a água", "i", 58) + [("sai", "g", 56, SETA_AGUA)] + ps("dos micróbios", "i", 58), XE, 600, passo=0.1)
    E.frase(c, t, C["s12.d"], ps("sem água,", "i", 58) + [("não se multiplicam", "g", 54, COR)], XE, 720, passo=0.1)
    pilula_em(c, t, C["s12.e"], "doce em calda: o mesmo, com açúcar", XE + 420, 880, 46, TINTA, "b")


# ---------------- osmose reversa ----------------
def b_reversa(c, t, C, b):
    desce = ease_io(prog(t, C["s13.a"], 1.0))
    inverte = ease_io(prog(t, C["s13.b"], 2.0))
    ne, nd = lerp(0.4, 0.7, inverte), lerp(0.7, 0.4, inverte)
    E.foco(c, t, C["s13"], 0.5, lambda a: tubo_u(c, t, UX, UY + 60, UW, UH - 60, ne, nd, 0, 10, a, embolo=(1, desce) if t >= C["s13.a"] else None,
                                               rot=("água doce", "água do mar")))
    setas_agua(c, t, C["s13.b"], UX + UW / 2 + 90, UX + UW / 2 - 90, UY + UH - 60, 2)
    E.frase(c, t, C["s13"], ps("e a água do", "i", 64) + [("mar?", "g", 60, COR)], XE, 220, passo=0.12)
    E.frase(c, t, C["s13.a"], ps("empurre com pressão", "i", 56) + [("maior", "g", 54, ERRADO)], XE, 340, passo=0.08)
    E.frase(c, t, C["s13.a"] + 1.4, ps("que a osmótica", "i", 56), XE, 410, passo=0.08)
    E.frase(c, t, C["s13.b"], ps("a água passa", "i", 58) + [("ao contrário", "g", 56, SETA_AGUA)], XE, 530, passo=0.1)
    E.frase(c, t, C["s13.c"], ps("o sal", "i", 58) + [("fica para trás", "g", 56, COR)], XE, 630, passo=0.1)
    E.frase(c, t, C["s13.d"], [("osmose", "g", 86, COR)], XE, 800)
    E.frase(c, t, C["s13.d"] + 0.4, [("reversa", "g", 86, COR)], XE, 900)
    rotulo(c, t, C["s13.e"], "dessalinização e purificadores de casa", XE + 400, 990, 42, TINTA, "b")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s14.a"], ps("é o sal que atravessa?", "i", 62), XE + 440, 190, passo=0.1)
    hx, hy = 1450, 600
    est = -ease_io(prog(t, C["s14.e"], 1.4))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (c.drawCircle(hx, hy, 330, M.paint("#BFE3D8", 0.6 * a)), hemacia(c, hx, hy, 150, est, a)))

    def errado():
        E.frase(c, t, C["s14.b"], ps("o sal entra na célula", "i", 62, ERRADO), XE, 400, passo=0.1)
        if t >= C["s14.b"] + 1.4:
            p = ep(t, C["s14.b"] + 0.6, 0.6)
            for k in range(3):
                particula(c, lerp(hx + 300, hx + 60, p), hy - 80 + 80 * k, 16, E.COR, 0.8)
            E.risco(c, XE - 10, 420, XE + 640, 340, t, C["s14.b"] + 1.8, largura=12)
    E.saida(c, t, C["s14.c"], errado)
    E.frase(c, t, C["s14.c"], ps("a membrana", "i", 62) + [("segura o soluto", "g", 58, COR)], XE, 540, passo=0.1)
    E.frase(c, t, C["s14.d"], ps("quem atravessa é a", "i", 62) + [("água", "g", 60, SETA_AGUA)], XE, 660, passo=0.1)
    E.frase(c, t, C["s14.e"], ps("ela sai para o lado mais concentrado", "i", 54), XE, 780, passo=0.08)
    setas_agua(c, t, C["s14.e"], hx + 160, hx + 300, hy + 10, 3)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s16"]:
        def s15():
            E.frase(c, t, C["s15"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 170, "center", 0.12)
            E.frase(c, t, C["s15.a"], [("a", "i", 120, BR), ("água", "g", 110, E.CLARO), ("corre", "i", 120, BR), ("atrás", "i", 120, BR)], W / 2, 400, "center", 0.12)
            E.frase(c, t, C["s15.a"] + 1.2, [("do", "i", 120, BR), ("soluto", "g", 110, E.CLARO)], W / 2, 540, "center", 0.12)
            E.frase(c, t, C["s15.b"], ps("ache o lado com mais partículas dissolvidas", "i", 56, CLARO), W / 2, 700, "center", 0.08)
            E.frase(c, t, C["s15.c"], ps("é para lá que a água vai e o nível sobe", "i", 56, CLARO), W / 2, 800, "center", 0.08)
            E.frase(c, t, C["s15.d"], ps("com pressão maior que a osmótica,", "i", 56, CLARO) + [("ela volta", "g", 54, BR)], W / 2, 920, "center", 0.08)
        E.saida(c, t, C["s16"] - 0.1, s15)
        return
    E.frase(c, t, C["s16.a"], ps("funciona porque", "i", 62, CLARO) + [("só a água passa", "g", 58, BR)], W / 2, 300, "center", 0.1)
    E.frase(c, t, C["s16.a"] + 2.0, ps("até diluir o lado concentrado", "i", 58, CLARO), W / 2, 390, "center", 0.1)
    E.frase(c, t, C["s16.b"], ps("compare em", "i", 60, CLARO) + [("mol/L,", "g", 58, BR)] + ps("não em gramas", "i", 60, CLARO), W / 2, 560, "center", 0.1)
    E.frase(c, t, C["s16.c"], [("não", "g", 56, ERRADO), ("basta:", "i", 60, CLARO)] + ps("soluto que é sal se divide em pedaços", "i", 58, CLARO), W / 2, 720, "center", 0.1)
    pilula_em(c, t, C["s16.c"] + 3.0, "contar os pedaços: outra aula", W / 2, 860, 50, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s17.a"], ps("tubo em U com membrana semipermeável", "i", 52), XE, 290, passo=0.08)
    E.frase(c, t, C["s17.b"], [("A:", "g", 58, COR)] + ps("glicose", "i", 62) + [("0,1 mol/L", "g", 58, COR)], XE, 410, passo=0.1)
    E.frase(c, t, C["s17.c"], [("B:", "g", 58, COR)] + ps("glicose", "i", 62) + [("0,3 mol/L", "g", 58, COR)], XE, 510, passo=0.1)
    E.frase(c, t, C["s17.d"], [("1", "g", 54, COR)] + ps("para que lado a água passa? qual nível sobe?", "i", 50), XE, 660, passo=0.06)
    E.frase(c, t, C["s17.e"], [("2", "g", 54, COR)] + ps("e empurrando B com mais força", "i", 50), XE, 760, passo=0.06)
    E.frase(c, t, C["s17.e"] + 2.0, ps("que a necessária para segurar a água?", "i", 50), XE + 40, 840, passo=0.06)
    if t < C["s18"]:
        E.foco(c, t, C["s17.a"], 0.5, lambda a: tubo_u(c, t, 1300, 330, 500, 520, 0.55, 0.55, 3, 9, a, rot=("A", "B")))
    else:
        E.relogio(c, t, C["s18.a"], cx=1500, cy=500, r=220)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    sobe = ease_io(prog(t, C["s19.c"], 1.6))
    inverte = ease_io(prog(t, C["s19.d"] + 0.4, 1.6))
    ne = lerp(0.55, 0.35, sobe) + lerp(0, 0.4, inverte)
    nd = lerp(0.55, 0.75, sobe) - lerp(0, 0.4, inverte)
    E.foco(c, t, C["s19"], 0.5, lambda a: tubo_u(c, t, 1150, 330, 600, 560, ne, nd, 3, 9, a, embolo=(1, ease_io(prog(t, C["s19.d"], 0.8))) if t >= C["s19.d"] else None,
                                             rot=("A", "B")))
    if t < C["s19.d"]:
        setas_agua(c, t, C["s19.b"], 1450 - 90, 1450 + 90, 840, 2)
    else:
        setas_agua(c, t, C["s19.e"], 1450 + 90, 1450 - 90, 840, 2)
    E.frase(c, t, C["s19.a"], ps("B tem", "i", 62) + [("mais soluto", "g", 58, COR)], XE, 260, passo=0.1)
    E.frase(c, t, C["s19.b"], ps("a água corre atrás dele", "i", 58), XE, 380, passo=0.1)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.formula(c, "A → B: o nível de B sobe", XE, 500, 60, "g", SETA_AGUA, a))
    E.frase(c, t, C["s19.d"], ps("empurrando B com mais força:", "i", 54), XE, 660, passo=0.08)
    E.foco(c, t, C["s19.e"], 0.5, lambda a: E.formula(c, "B → A", XE, 780, 70, "g", SETA_AGUA, a))
    pilula_em(c, t, C["s19.e"] + 1.2, "osmose reversa", XE + 520, 760, 50, E.COR)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s20.a", [("osmose:", "g", 62), ("a", "i", 66), ("água", "g", 62, SETA_AGUA), ("vai", "i", 66), ("para", "i", 66), ("o", "i", 66), ("lado", "i", 66), ("mais", "g", 62), ("concentrado", "i", 66)]),
                 ("s20.b", [("pressão", "g", 62, COR), ("osmótica", "g", 62, COR), ("=", "g", 62, TINTA2), ("o", "i", 66), ("empurrão", "i", 66), ("que", "i", 66), ("impede", "i", 66)]),
                 ("s20.c", [("mais", "i", 66), ("força:", "i", 66), ("osmose", "g", 62), ("reversa", "g", 62, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("praticando", "g", 110, COR)], XE, 400)
    for k, s in enumerate(("ferver", "congelar", "osmose")):
        pilula_em(c, t, C["s21.b"] + 0.4 * k, s, XE + 140 + 340 * k, 560, 56, TINTA)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 460, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(760, 485, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, membrana=b_membrana, osmose=b_osmose, pressao=b_pressao, celulas=b_celulas,
              carne=b_carne, reversa=b_reversa, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
