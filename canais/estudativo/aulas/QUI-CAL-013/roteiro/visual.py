"""Visual — Estudativo · QUI-CAL-013: volume molar e estequiometria com gases.

Segue a linguagem dos gases (cabeçalho da QUI-CAL-010), a da estequiometria (QUI-CAL-004), a da trilha (QUI-CAL-001) e a da
Química (QUI-MIS-001). Os três balões de 1 mol (H₂, O₂, CO₂) têm o mesmo tamanho e as partículas na cor CPK do gás.
O volume molar vai sempre com a condição na pílula: "22,4 L · CNTP (0 °C e 1 atm)". Na equação, a linha de baixo pode
misturar gramas e litros; o que não é gás leva a pílula cinza "não é gás" e nunca recebe 22,4 L."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-013_volume_molar_gases.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("molar", "etanol", "atalho", "questao", "fim"))
BR = "#FFFFFF"
EQ = "C2H6O + 3 O2 -> 2 CO2 + 3 H2O"
EX, EY, ES = W / 2, 300, 92

# todas as contas da aula
assert Q.lados(EQ)[0] == Q.lados(EQ)[1]
assert abs(0.082 * 273 - 22.386) < 1e-9 and abs(2 * 22.4 - 44.8) < 1e-9 and abs(3 * 22.4 - 67.2) < 1e-9 and 3 * 18 == 54
assert 92 / 46 == 2 and 2 * 3 == 6 and abs(6 * 22.4 - 134.4) < 1e-9


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    tinta = E.SOBRE if cor is None else BR
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", tinta, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    """lista numerada: itens = [(instante, partes da frase)]"""
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def conta(c, t, t0, el, txt, res, x, y, size=72, tr=None, cor_res=None, escuro=False):
    """linha de massa: bolinha do elemento + "6 × 12 =" + parcial na cor da matéria (tr = instante do parcial)"""
    r = size * 0.42
    if el:
        Q.atomo_em(c, t, t0, x + r, y - size * 0.34, r, el, escuro=escuro)
        x += 2 * r + size * 0.4
    E.formula_em(c, t, t0 + 0.1, txt, x, y, size, "g", BR if escuro else TINTA)
    w = E.formula(None, txt, 0, 0, size, a=0)
    if res:
        E.formula_em(c, t, tr if tr is not None else t0 + 0.6, res, x + w + size * 0.3, y, size, "g", cor_res or (E.CLARO if escuro else COR))
    return x + w


def casa(c, cx, cy, s, el, z, m, a=1.0, cor_m=None):
    """casa do elemento na tabela periódica: Z no canto, símbolo, nome e a massa atômica embaixo"""
    if a <= 0:
        return
    w, h = s, s * 1.15
    x, y = cx - w / 2, cy - h / 2
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), s * 0.08, s * 0.08)
    c.drawRRect(rr, M.paint("#FFFFFF", a))
    c.drawRRect(rr, M.paint(E.COR, a, stroke=max(3, s * 0.025)))
    E.escreve(c, str(z), x + s * 0.09, y + s * 0.19, s * 0.14, "b", TINTA2, a)
    centro(c, el, cx, cy + s * 0.1, s * 0.42, "g", TINTA, a)
    centro(c, Q.NOMES[el], cx, cy + s * 0.28, s * 0.12, "i", TINTA2, a)
    centro(c, m, cx, cy + s * 0.5, s * 0.17, "g", cor_m or COR, a)


def casa_em(c, t, t0, cx, cy, s, el, z, m, cor_m=None):
    E.foco(c, t, t0, 0.5, lambda a: casa(c, cx, cy, s, el, z, m, a, cor_m))


def soma_vertical(c, t, tl, nums, tot, xd, y0, size, tt, cor_tot=None):
    """conta armada de somar, alinhada à direita em xd; tt = instante do traço e do total"""
    dy = size * 1.15
    for i, (n, ti) in enumerate(zip(nums, tl)):
        E.foco(c, t, ti, 0.4, lambda a, n=n, i=i: E.formula(c, n, xd, y0 + i * dy, size, "g", TINTA, a, "right"))
    E.foco(c, t, tl[1] if len(tl) > 1 else tl[0], 0.4, lambda a: E.formula(c, "+", xd - size * 2.6, y0 + dy * (len(nums) - 1), size, "g", TINTA2, a))
    p = ep(t, tt, 0.4)
    yl = y0 + (len(nums) - 1) * dy + size * 0.35
    if p > 0:
        M.line(c, xd - size * 2.8, yl, xd + size * 0.2, yl, TINTA, p, 5, progress=ease_out(prog(t, tt, 0.4)))
    return yl


def ponte_mol(c, t, t0, y, esq, meio, dir_, rot_e="", rot_d="", te=None, td=None, xs=(420, 960, 1500), size=58, escuro=False):
    """a ponte do mol: gramas ← → mol ← → moléculas. esq/meio/dir_ = texto de cada margem (ou (texto, instante));
    rot_e / rot_d = operação na pílula de cada vão; te / td = instante de cada vão"""
    tinta = BR if escuro else TINTA
    x0, xm, x1 = xs

    def txt(v):
        return v if isinstance(v, tuple) else (v, t0)
    for k, (v, x) in enumerate(((esq, x0), (dir_, x1))):
        s, ti = txt(v)
        if s:
            E.foco(c, t, ti, 0.45, lambda a, s=s, x=x: E.formula(c, s, x, y + size * 0.36, size, "g", tinta, a, "center"))
    s, ti = txt(meio)
    k = ease_back(prog(t, ti, 0.5))
    if k > 0:
        r = max(size * 1.25, E.formula(None, s, 0, 0, size * 0.8, a=0) * 0.62)
        E.bola(c, xm, y, r * k)
        E.foco(c, t, ti + 0.1, 0.4, lambda a: E.formula(c, s, xm, y + size * 0.29, size * 0.8, "g", E.SOBRE, a, "center"))
    rb = max(size * 1.25, E.formula(None, s, 0, 0, size * 0.8, a=0) * 0.62)
    we = E.formula(None, txt(esq)[0], 0, 0, size, a=0) / 2 if txt(esq)[0] else 60
    wd = E.formula(None, txt(dir_)[0], 0, 0, size, a=0) / 2 if txt(dir_)[0] else 60
    for (xa, xb, rot, tv) in ((x0 + we + 36, xm - rb - 30, rot_e, te), (xm + rb + 30, x1 - wd - 36, rot_d, td)):
        if tv is None:
            continue
        p = ease_io(prog(t, tv, 0.6))
        if p > 0:
            M.arrow(c, xa, y, lerp(xa, xb, p), y, E.CLARO if escuro else E.COR, 1.0, 7, 24, 1.0)
        if rot:
            pilula_em(c, t, tv + 0.3, rot, (xa + xb) / 2, y - 80, 42, TINTA if not escuro else "#24303A")


def pacotes(c, t, t0, n, x, y, w, h, rot, cor=None, passo=0.35, escuro=False):
    """barra cortada em n pacotes iguais que entram um a um, com o rótulo de cada um (quantas vezes cabe)"""
    wk = w / n
    for k in range(n):
        q = ease_back(prog(t, t0 + k * passo, 0.45))
        if q <= 0:
            continue
        xx = x + k * wk
        M.rrect(c, xx + 4, y + h * (1 - q) / 2, wk - 8, h * q, 14, cor or E.COR, 1.0)
        centro(c, rot, xx + wk / 2, y + h / 2 + h * 0.18, h * 0.5, "g", E.SOBRE, min(1, q))


def chip(c, s, cx, cy, size, fundo=None, a=1.0, escuro=True):
    """fórmula química dentro de uma pílula do tamanho dela"""
    if a <= 0:
        return
    w = Q.formula(None, s, 0, 0, size) + size * 0.9
    M.rrect(c, cx - w / 2, cy - size * 0.8, w, size * 1.6, size * 0.8, fundo or E.COR, a)
    Q.formula(c, s, cx, cy + size * 0.36, size, BR, a, "center", escuro=escuro)


# ---------------- peças dos gases (candidatas ao kit quimica.py) ----------------
QUENTE, FRIO = "#E8590C", "#1F6FEB"


def fase(t, pts):
    """tempo 'interno' das partículas: a velocidade muda sem pulo. pts = [(instante, velocidade), ...] em ordem;
    entre dois pontos a velocidade varia em linha reta; devolve a integral da velocidade até t"""
    if t <= pts[0][0]:
        return t * pts[0][1]
    acc = pts[0][0] * pts[0][1]
    for (t0, v0), (t1, v1) in zip(pts, pts[1:]):
        if t <= t1:
            u = t - t0
            return acc + v0 * u + (v1 - v0) * u * u / (2 * max(1e-6, t1 - t0))
        acc += (v0 + v1) / 2 * (t1 - t0)
    return acc + (t - pts[-1][0]) * pts[-1][1]


def cilindro(c, t, x, yb, w, h, n=26, tt=None, a=1.0, embolo=True, tipos=None, r=12, semente=5, rotulo=None, escuro=False):
    """recipiente com êmbolo: (x, yb) = canto de baixo à esquerda, w = largura, h = altura do gás (o êmbolo fica em yb − h).
    tt = tempo interno das partículas (use fase() para mudar a temperatura); partículas de gás voando dentro"""
    if a <= 0:
        return
    vidro = "#9AA0A8" if escuro else Q.VIDRO
    top = yb - h
    c.drawRect(skia.Rect.MakeXYWH(x, top, w, h), M.paint("#FFFFFF" if not escuro else "#16202A", 0.55 * a))
    Q.particulas(c, t if tt is None else tt, x + 6, top + (22 if embolo else 4), w - 12, h - (26 if embolo else 8), n, "gas",
                 tipos=tipos or [(E.COR, 1.0)], r=r, semente=semente, a=a, escuro=escuro)
    pa = M.paint(vidro, a, stroke=6)
    pth = skia.Path(); pth.moveTo(x, top - 120); pth.lineTo(x, yb); pth.lineTo(x + w, yb); pth.lineTo(x + w, top - 120)
    c.drawPath(pth, pa)
    if embolo:
        M.rrect(c, x + 4, top - 18, w - 8, 30, 8, "#6B7078", a)
        M.rrect(c, x + w / 2 - 14, top - 120, 28, 104, 6, "#8A8F96", a)
    if rotulo:
        centro(c, rotulo, x + w / 2, yb + 64, 48, "i", TINTA2 if not escuro else E.CLARO, a)


def termometro(c, cx, ytop, h, frac, a=1.0, rot=None, escuro=False):
    """termômetro de bulbo: frac = 0..1 da coluna; a coluna esquenta do azul ao laranja"""
    if a <= 0:
        return
    tw = 34
    cor = M.mix(FRIO, QUENTE, max(0.0, min(1.0, frac)))
    M.rrect(c, cx - tw / 2, ytop, tw, h, tw / 2, "#FFFFFF" if not escuro else "#1C2630", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - tw / 2, ytop, tw, h), tw / 2, tw / 2), M.paint(Q.VIDRO, a, stroke=4))
    hh = (h - 30) * max(0.03, min(1.0, frac))
    M.rrect(c, cx - 8, ytop + h - hh, 16, hh + 10, 8, cor, a)
    c.drawCircle(cx, ytop + h + 28, 40, M.paint(cor, a))
    c.drawCircle(cx, ytop + h + 28, 40, M.paint(Q.VIDRO, a, stroke=4))
    if rot:
        centro(c, rot, cx, ytop - 30, 48, "g", TINTA if not escuro else BR, a)


def manometro(c, cx, cy, r, val, vmax, a=1.0, rot=None, escuro=False):
    """mostrador de pressão: ponteiro de 0 a vmax (arco de 240°)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint("#FFFFFF" if not escuro else "#1C2630", a))
    c.drawCircle(cx, cy, r, M.paint(Q.VIDRO, a, stroke=6))
    for k in range(9):
        ang = math.radians(150 + 240 * k / 8)
        M.line(c, cx + r * 0.78 * math.cos(ang), cy + r * 0.78 * math.sin(ang), cx + r * 0.92 * math.cos(ang), cy + r * 0.92 * math.sin(ang),
               TINTA2 if not escuro else E.CLARO, a, 4)
    ang = math.radians(150 + 240 * max(0.0, min(1.0, val / vmax)))
    M.line(c, cx, cy, cx + r * 0.74 * math.cos(ang), cy + r * 0.74 * math.sin(ang), E.COR, a, 8)
    c.drawCircle(cx, cy, 12, M.paint(TINTA if not escuro else BR, a))
    if rot:
        centro(c, rot, cx, cy + r * 0.62, r * 0.28, "g", TINTA if not escuro else BR, a)


def frac_q(c, num, den, cx, y, size, a=1.0, cor=None, cores=None, escuro=False):
    """fração com fórmula química (índices) em cima e embaixo, centrada em cx; y = linha de base do numerador"""
    if a <= 0:
        return 0
    wn = Q.formula(None, num, 0, 0, size)
    wd = Q.formula(None, den, 0, 0, size)
    w = max(wn, wd) + size * 0.3
    Q.formula(c, num, cx, y, size, cor, a, "center", cores=cores, escuro=escuro)
    M.line(c, cx - w / 2, y + size * 0.32, cx + w / 2, y + size * 0.32, cor or (BR if escuro else TINTA), a, max(4, size * 0.06))
    Q.formula(c, den, cx, y + size * 1.15, size, cor, a, "center", cores=cores, escuro=escuro)
    return w


def frac_q_em(c, t, t0, num, den, cx, y, size, cor=None, cores=None, escuro=False):
    E.foco(c, t, t0, 0.5, lambda a: frac_q(c, num, den, cx, y, size, a, cor, cores, escuro))


def balao(c, t, tt, cx, cy, rx, ry, n=30, cor=None, a=1.0, semente=7):
    """balão de festa com o gás dentro (partículas presas na elipse)"""
    if a <= 0 or rx <= 2:
        return
    cor = cor or E.COR
    oval = skia.Rect.MakeXYWH(cx - rx, cy - ry, 2 * rx, 2 * ry)
    c.drawOval(oval, M.paint(cor, 0.22 * a))
    c.save()
    pth = skia.Path(); pth.addOval(oval)
    c.clipPath(pth, doAntiAlias=True)
    Q.particulas(c, tt, cx - rx, cy - ry, 2 * rx, 2 * ry, n, "gas", tipos=[(cor, 1.0)], r=10, semente=semente, a=a)
    c.restore()
    c.drawOval(oval, M.paint(cor, a, stroke=6))
    k = skia.Path(); k.moveTo(cx - 16, cy + ry + 22); k.lineTo(cx + 16, cy + ry + 22); k.lineTo(cx, cy + ry - 2); k.close()
    c.drawPath(k, M.paint(cor, a))
    s = skia.Path(); s.moveTo(cx, cy + ry + 22); s.cubicTo(cx + 30, cy + ry + 80, cx - 30, cy + ry + 120, cx + 10, cy + ry + 170)
    c.drawPath(s, M.paint(TINTA2, a, stroke=3))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for k, (f, el, m, tk) in enumerate((("H2", "H", "2 g", "s01.a"), ("O2", "O", "32 g", "s01.b"), ("CO2", "C", "44 g", "s01.c"))):
            x = 400 + 560 * k
            E.foco(c, t, C[tk], 0.5, lambda a, x=x, el=el: _bal(c, t, x, 470, el, a))
            Q.formula_em(c, t, C[tk] + 0.2, f, x, 840, 90, align="center")
            E.foco(c, t, C[tk] + 0.4, 0.4, lambda a, x=x, m=m: centro(c, m, x, 940, 60, "g", COR, a))
        E.frase(c, t, C["s01.d"], ps("mesma temperatura e pressão:", "i", 60, TINTA2) + [("mesmo tamanho", "g", 56, COR)], W / 2, 160, "center", 0.1)
        E.frase(c, t, C["s01.e"], [("por quê?", "i", 66)], W / 2, 1040, "center")
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("volume", "g", 70), ("molar:", "g", 70, COR), ("22,4 L", "g", 70)]),
                 (C["s02.c"], [("volume", "g", 70), ("de", "i", 74), ("gás", "g", 70), ("numa", "i", 74), ("reação", "g", 70)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("só", "i", 74), ("de", "i", 74), ("gases", "g", 70)])], XE, 460, 170)


def _bal(c, t, x, y, el, a):
    """balão de 1 mol com partículas na cor do gás"""
    oval = skia.Rect.MakeXYWH(x - 190, y - 220, 380, 440)
    c.drawOval(oval, M.paint(E.COR, 0.15 * a))
    c.save(); pth = skia.Path(); pth.addOval(oval); c.clipPath(pth, doAntiAlias=True)
    Q.particulas(c, t, x - 190, y - 220, 380, 440, 18, "gas", tipos=[(el, 1.0)], r=12, semente=3, a=a)
    c.restore()
    c.drawOval(oval, M.paint(E.COR, a, stroke=6))
    M.line(c, x, y + 220, x + 10, y + 300, TINTA2, a, 3)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03.a"] - 0.6, ps("você precisa de", "i", 80) + [("duas coisas", "g", 76, COR)], XE, 200, passo=0.12)
    y = [430, 760]
    for i, k in enumerate(("s03.b", "s03.c")):
        E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, XE + 40, y[i] - 30, 44, a=a), centro(c, str(i + 1), XE + 40, y[i] - 8, 54, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, ps("massa para massa numa equação", "i", 66), XE + 110, y[0], passo=0.1)
    E.frase(c, t, C["s03.c"] + 0.1, ps("a equação", "i", 66) + [("PV = nRT", "g", 62, COR)], XE + 110, y[1], passo=0.1)


# ---------------- volume molar ----------------
def b_molar(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("cada balão tem", "i", 76) + [("1 mol", "g", 72, COR)], XE, 220, passo=0.12)
        E.foco(c, t, C["s04.b"], 0.4, lambda a: E.escreve(c, "V =", XE, 470, 110, "g", TINTA, a))
        frac_q_em(c, t, C["s04.b"] + 0.3, "nRT", "P", XE + 360, 420, 110)
        E.frase(c, t, C["s04.c"], ps("nenhuma letra diz", "i", 66) + [("qual é o gás", "g", 62, COR)], XE, 700, passo=0.1)
        E.frase(c, t, C["s04.d"], ps("mesmos mols, T e P:", "i", 66), XE, 850, passo=0.1)
        E.frase(c, t, C["s04.e"], [("mesmo volume", "g", 66, COR)], XE + 640, 850)
        for k, el in enumerate(("H", "O", "C")):
            E.foco(c, t, C["s04.e"] + 0.2 * k, 0.4, lambda a, k=k, el=el: (cilindro(c, t, 1100 + k * 250, 620, 200, 260, 10, a=a, embolo=False, tipos=[(el, 1.0)], semente=k + 2)))
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("volume", "g", 100, COR), ("molar", "g", 100, COR)], XE, 300, passo=0.12)
        E.foco(c, t, C["s05.a"] + 1.0, 0.4, lambda a: E.escreve(c, "o volume de 1 mol de gás", XE, 400, 60, "i", TINTA2, a))
        E.frase(c, t, C["s05.b"], ps("a prova usa as", "i", 70) + [("CNTP", "g", 66, COR)], XE, 600, passo=0.12)
        E.frase(c, t, C["s05.c"], ps("condições normais de temperatura e pressão", "i", 58, TINTA2), XE, 700, passo=0.08)
        E.foco(c, t, C["s05.d"], 0.5, lambda a: (E.pilula(c, "0 °C = 273 K", XE + 260, 860, 60, "g", fundo=E.COR, a=a), E.pilula(c, "1 atm", XE + 720, 860, 60, "g", fundo=E.COR, a=a)))
        return
    E.foco(c, t, C["s06.b"] - 0.4, 0.4, lambda a: E.escreve(c, "V =", XE, 360, 100, "g", TINTA, a))
    frac_q_em(c, t, C["s06.b"], "1 · 0,082 · 273", "1", XE + 640, 320, 90)
    E.formula_em(c, t, C["s06.c"], "≈", XE + 1040, 360, 100, "g", TINTA2)
    bola_txt(c, t, C["s06.c"] + 0.4, "22,4 L", XE + 1330, 330, 120, 66)
    pilula_em(c, t, C["s06.c"] + 1.0, "1 mol de qualquer gás · CNTP", W / 2, 620, 56, TINTA)
    E.frase(c, t, C["s06.d"], ps("fora das CNTP, o valor muda:", "i", 62, TINTA2) + [("a prova avisa", "g", 58)], XE, 820, passo=0.1)
    E.frase(c, t, C["s06.d"] + 2.4, ps("ou use", "i", 62, TINTA2) + [("PV = nRT", "g", 58, COR)], XE, 920, passo=0.1)


# ---------------- etanol ----------------
def b_etanol(c, t, C, b):
    t7 = C["s07.a"]
    Q.equacao(c, t, t7, EQ, EX, EY, ES, tl=[t7 + 0.25 * k for k in range(7)], cores={"coef": E.COR})
    Q.sob_termos(c, t, EQ, EX, EY, ES, [["1 mol", "", "2 mol", ""]], tl=[[C["s07.b"], 0, C["s07.c"], 0]], size_l=66, cores_l=[COR], dy=100)
    Q.sob_termos(c, t, EQ, EX, EY + 100, ES, [["46 g", "", "2 × 22,4 L", ""]], tl=[[C["s07.b"] + 0.6, 0, C["s07.d"], 0]], size_l=60, dy=100)
    E.foco(c, t, C["s07.d"] + 0.6, 0.4, lambda a: E.pilula(c, "CNTP", Q.centros(EQ, EX, EY, ES)[2] + 250, EY + 200, 40, "g", fundo=TINTA, a=a))
    E.formula_em(c, t, C["s07.e"], "2 × 22,4 =", 560, 760, 96, "g", TINTA2)
    bola_txt(c, t, C["s07.e"] + 1.0, "44,8 L", 1180, 730, 116, 64)
    if t >= C["s08"]:
        E.frase(c, t, C["s08.a"], ps("na linha de baixo:", "i", 60, TINTA2) + [("gramas", "g", 56)] + ps("e", "i", 60) + [("litros", "g", 56, COR)] + ps("juntos", "i", 60), XE, 940, passo=0.1)
        E.frase(c, t, C["s08.c"], ps("a regra de três funciona igual", "i", 56, TINTA2), XE, 1030, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s09"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s09.a"], ps("22,4 L para o que não é gás", "i", 72), XE + 450, 190, passo=0.12)
    Q.formula_em(c, t, C["s09.a"] + 0.4, EQ, EX, 400, ES, align="center")
    cs = Q.centros(EQ, EX, 400, ES)
    pilula_em(c, t, C["s09.b"], "não é gás", cs[3], 290, 40, "#5A5F66")
    E.formula_em(c, t, C["s09.c"], "3 × 22,4 = 67,2 L", XE, 640, 90, "g", ERRADO)
    if t >= C["s09.d"]:
        E.risco(c, XE - 10, 670, XE + 860, 580, t, C["s09.d"], largura=12)
        E.foco(c, t, C["s09.d"] + 0.3, 0.4, lambda a: (E.escreve(c, "54 g de água: cerca de 54 mL", XE, 780, 60, "g", COR, a)))
    E.frase(c, t, C["s09.e"], ps("volume molar:", "i", 70) + [("só para gases", "g", 66, COR)], XE, 940, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("o atalho: entre gases, na mesma T e P,", "i", 64, CLARO), W / 2, 180, "center", 0.1)
        E.frase(c, t, C["s10.b"], [("volumes", "g", 66, BR)] + ps("seguem os", "i", 70, CLARO) + [("coeficientes", "g", 66, BR)], W / 2, 290, "center", 0.12)
        Q.formula_em(c, t, C["s10.c"], "3 O2 → 2 CO2", W / 2, 520, 150, align="center", escuro=True, cores={"coef": E.CLARO})
        cs = Q.centros("3 O2 -> 2 CO2", W / 2, 520, 150)
        E.foco(c, t, C["s10.d"], 0.4, lambda a: (E.formula(c, "3 L", cs[0], 680, 90, "g", E.CLARO, a, "center"), E.formula(c, "2 L", cs[1], 680, 90, "g", E.CLARO, a, "center")))
        pilula_em(c, t, C["s10.e"], "nem precisa do 22,4", W / 2, 880, 56, E.COR)
        return
    E.frase(c, t, C["s11.a"], ps("volume de gás é", "i", 72, CLARO) + [("proporcional aos mols", "g", 66, BR)], W / 2, 300, "center", 0.12)
    E.frase(c, t, C["s11.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("sólido ou líquido na conta", "i", 66, CLARO), W / 2, 520, "center", 0.12)
    for k, f in enumerate(("C2H6O", "H2O")):
        E.foco(c, t, C["s11.c"] + 0.3 * k, 0.4, lambda a, k=k, f=f: (Q.formula(c, f, 760 + 440 * k, 720, 110, BR, a, "center", escuro=True)))
    pilula_em(c, t, C["s11.c"] + 1.2, "aí, passe pelo mol", W / 2, 900, 52, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s12"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s12.a"], ps("quantos litros de oxigênio, nas", "i", 66) + [("CNTP,", "g", 62, COR)], XE, 330, passo=0.1)
    E.frase(c, t, C["s12.b"], ps("para queimar", "i", 66) + [("92 g", "g", 64, COR)] + ps("de etanol?", "i", 66), XE, 440, passo=0.1)
    Q.formula_em(c, t, C["s12.b"] + 1.0, EQ, XE, 640, 80, cores={"coef": E.COR})
    if t >= C["s13"]:
        E.relogio(c, t, C["s13.a"], cx=1600, cy=780, r=130)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    Q.equacao(c, t, C["s14"], EQ, EX, 260, ES, tl=[C["s14"]] * 7, cores={"coef": E.COR})
    Q.sob_termos(c, t, EQ, EX, 260, ES, [["2 mol", "6 mol", "", ""]], tl=[[C["s14.a"], C["s14.c"], 0, 0]], size_l=66, cores_l=[COR])
    E.formula_em(c, t, C["s14.a"], "92 ÷ 46 = 2 mol", XE, 560, 80, "g", TINTA)
    E.formula_em(c, t, C["s14.b"], "1 mol de etanol → 3 mol de oxigênio", XE, 690, 70, "g", TINTA2)
    E.formula_em(c, t, C["s14.d"], "6 × 22,4 =", XE, 880, 96, "g", TINTA2)
    bola_txt(c, t, C["s14.e"], "134,4 L", XE + 760, 850, 124, 58, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s15"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s15.a", [("CNTP:", "g", 66), ("1 mol", "g", 66, COR), ("de gás", "i", 70), ("=", "g", 66, TINTA2), ("22,4 L", "g", 66, COR)]),
                 ("s15.b", ps("entre gases, volumes seguem os", "i", 70) + [("coeficientes", "g", 66)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s16"] - 0.1, resumo)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s16"] + 0.6, [("misturas", "g", 90, COR)] + ps("de gases", "i", 90), XE, 420, passo=0.12)
    E.frase(c, t, C["s16.a"], ps("quanto da pressão do ar vem do", "i", 66) + [("oxigênio?", "g", 62)], XE, 600, passo=0.1)
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 780, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s16.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 805, p), ep(t, C["s16.b"] + 0.2, 0.4))
    E.frase(c, t, C["s16.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, molar=b_molar, etanol=b_etanol, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
