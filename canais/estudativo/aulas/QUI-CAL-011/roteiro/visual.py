"""Visual — Estudativo · QUI-CAL-011: transformações gasosas e equação geral.

Segue a linguagem dos gases (cabeçalho da QUI-CAL-010), a da trilha (QUI-CAL-001) e a da Química (QUI-MIS-001).
Cada transformação tem o seu PAINEL P·V·T (painel_pvt): três pílulas com a letra e o que acontece com ela; a que fica parada
leva "fixo" em cinza, as que mudam vão na cor da matéria com a seta (sobe / desce). O cilindro com êmbolo mostra o volume, o
termômetro a temperatura e o mostrador a pressão. A equação geral é uma fração com índice (frac_q); o que se cancela leva
um risco na cor da matéria (não é erro). No atalho, cada mudança vira um FATOR numa pílula (× ½, × 1,2).
Peças candidatas ao kit quimica.py: painel_pvt() e lata()."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-011_transformacoes_gasosas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("isotermica", "geral", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 1 * 10 * 360 / (300 * 2) == 6 and 3600 / 600 == 6 and 10 * 0.5 * 1.2 == 6 and 360 / 300 == 1.2
assert abs(10 * 87 / (27 * 2) - 16.1) < 0.05 and 6 * 400 / 300 == 8 and 27 + 273 == 300 and 87 + 273 == 360 and 127 + 273 == 400
assert 1 * 10 == 2 * 5


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


def painel_pvt(c, t, x, y, itens, size=56):
    """itens = [(letra, texto, instante, muda)]: pílula da letra + o que acontece; muda=False = fixo (cinza)"""
    for k, (letra, txt, ti, muda) in enumerate(itens):
        yy = y + k * size * 1.9
        E.foco(c, t, ti, 0.4, lambda a, letra=letra, txt=txt, muda=muda, yy=yy: (
            E.pilula(c, letra, x + size * 0.7, yy - size * 0.35, size, "g", fundo=E.COR if muda else "#8A8F96", a=a),
            E.escreve(c, txt, x + size * 1.7, yy, size * 0.95, "g" if muda else "i", COR if muda else TINTA2, a)))


def lata(c, cx, yb, w, h, a=1.0, chama=0.0, t=0.0):
    """lata de spray (volume fixo), com a chama embaixo"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, yb - h, w, h, 20, "#C8CDD3", a)
    M.rrect(c, cx - w / 2, yb - h * 0.75, w, h * 0.35, 8, E.COR, a)
    M.rrect(c, cx - w * 0.18, yb - h - 40, w * 0.36, 44, 8, "#8A8F96", a)
    if chama > 0:
        for k in range(3):
            fx = cx + (k - 1) * w * 0.3
            hh = (70 + 20 * math.sin(t * 9 + k)) * chama
            p = skia.Path(); p.moveTo(fx - 26, yb + 110); p.quadTo(fx - 30, yb + 110 - hh * 0.6, fx, yb + 110 - hh); p.quadTo(fx + 30, yb + 110 - hh * 0.6, fx + 26, yb + 110); p.close()
            c.drawPath(p, M.paint(QUENTE, a * 0.9))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        tb, tc = C["s01.b"], C["s01.c"]
        k = ease_io(prog(t, tb, tc - tb))
        h = lerp(380, 190, k)
        E.frase(c, t, C["s01.a"], ps("tampe a seringa e empurre o", "i", 64) + [("êmbolo", "g", 60, COR)], XE, 200, passo=0.1)
        E.foco(c, t, C["s01.a"] + 0.5, 0.5, lambda a: cilindro(c, t, 1100, 900, 300, h, 26, a=a))
        if t >= tb:
            M.arrow(c, 1250, 900 - h - 260, 1250, 900 - h - 140, TINTA, 1.0, 8, 24)
        E.foco(c, t, C["s01.a"] + 0.8, 0.5, lambda a: manometro(c, 1620, 560, 130, lerp(1, 2, k), 3, a, f"{lerp(1, 2, k):.1f}".replace(".", ",") + " atm"))
        E.frase(c, t, C["s01.b"], ps("mais você aperta,", "i", 64) + [("mais difícil", "g", 60)], XE, 420, passo=0.1)
        E.frase(c, t, C["s01.c"], [("½", "g", 70, COR)] + ps("do espaço:", "i", 66) + [("2×", "g", 70, COR)] + ps("a pressão", "i", 66), XE, 600, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("uma regra, uma", "i", 66) + [("equação só", "g", 62, COR)], XE, 800, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("as", "i", 74), ("três", "g", 70), ("transformações", "g", 70, COR)]),
                 (C["s02.c"], [("a", "i", 74), ("equação", "g", 70), ("geral", "g", 70, COR)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03.a"] - 0.6, ps("você precisa de", "i", 80) + [("três coisas", "g", 76, COR)], XE, 200, passo=0.12)
    y = [400, 640, 880]
    for i, k in enumerate(("s03.b", "s03.c", "s03.d")):
        E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, XE + 40, y[i] - 30, 44, a=a), centro(c, str(i + 1), XE + 40, y[i] - 8, 54, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, ps("gás sempre em", "i", 66) + [("kelvin", "g", 62, COR)], XE + 110, y[0], passo=0.1)
    E.formula_em(c, t, C["s03.b"] + 0.8, "27 °C = 300 K", XE + 800, y[0] + 4, 70, "g", TINTA2)
    E.frase(c, t, C["s03.c"] + 0.1, [("direta", "g", 62)] + ps("e", "i", 66) + [("inversa", "g", 62)], XE + 110, y[1], passo=0.1)
    E.formula_em(c, t, C["s03.c"] + 0.8, "f{y}{x} fixo  ·  x · y fixo", XE + 800, y[1] + 4, 66, "g", TINTA2)
    E.frase(c, t, C["s03.d"] + 0.1, ps("isolar uma letra", "i", 66), XE + 110, y[2], passo=0.1)
    E.formula_em(c, t, C["s03.d"] + 0.8, "v = f{d}{t}  →  d = v · t", XE + 800, y[2] + 4, 66, "g", TINTA2)


# ---------------- isotérmica ----------------
def b_isotermica(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("um gás preso tem", "i", 76) + [("três variáveis", "g", 70, COR)], XE, 260, passo=0.12)
        for k, (l, n) in enumerate((("P", "pressão"), ("V", "volume"), ("T", "temperatura"))):
            x = XE + 200 + k * 540
            E.foco(c, t, C["s04.b"] + 0.5 * k, 0.5, lambda a, x=x, l=l, n=n: (E.bola(c, x, 520, 110, a=a), centro(c, l, x, 560, 120, "g", E.SOBRE, a),
                                                                          centro(c, n, x, 720, 56, "i", TINTA2, a)))
        E.frase(c, t, C["s04.c"], ps("numa transformação,", "i", 66) + [("uma fica parada", "g", 62, COR)], XE, 900, passo=0.12)
        return
    E.frase(c, t, C["s05.a"], [("isotérmica", "g", 90, COR)], XE, 220)
    E.frase(c, t, C["s05.b"], [("iso", "g", 60), ("=", "g", 60, TINTA2), ("igual", "i", 64), ("·", "g", 60, TINTA2), ("térmica", "g", 60), ("=", "g", 60, TINTA2), ("temperatura", "i", 64)], XE, 330, passo=0.1)
    k = ease_io(prog(t, C["s05.c"], 1.6))
    cilindro(c, t, 1080, 900, 300, lerp(380, 190, k), 24)
    manometro(c, 1600, 480, 120, lerp(1, 2, k), 3, 1.0, f"{lerp(1, 2, k):.1f}".replace(".", ",") + " atm")
    termometro(c, 1600, 680, 200, 0.45, 1.0)
    painel_pvt(c, t, XE, 470, [("T", "fixo", C["s05.a"] + 0.3, False), ("V", "cai à metade", C["s05.c"], True), ("P", "dobra", C["s05.c"] + 0.8, True)], 64)
    E.frase(c, t, C["s05.d"], ps("P e V:", "i", 62), XE, 840, passo=0.1)
    E.frase(c, t, C["s05.d"] + 0.4, [("inversamente proporcionais", "g", 56)], XE, 910, passo=0.1)
    E.formula_em(c, t, C["s05.e"], "P · V = constante", XE, 1020, 72, "g", COR)


# ---------------- isobárica ----------------
def b_isobarica(c, t, C, b):
    E.frase(c, t, C["s06.a"], [("isobárica", "g", 90, COR)], XE, 220)
    E.frase(c, t, C["s06.a"] + 1.2, ps("baro: pressão, como no barômetro", "i", 58, TINTA2), XE, 320, passo=0.1)
    tb = C["s06.b"]
    k = ease_io(prog(t, tb, 2.4))
    tt = fase(t, [(tb, 0.6), (tb + 2.4, 1.8)])
    cilindro(c, t, 1080, 900, 300, lerp(220, 440, k), 24, tt=tt, tipos=[(M.mix(FRIO, QUENTE, k), 1.0)])
    termometro(c, 1600, 430, 280, lerp(0.3, 0.9, k), 1.0, f"{round(lerp(300, 600, k))} K")
    painel_pvt(c, t, XE, 470, [("P", "fixo", C["s06.a"] + 0.4, False), ("T", "sobe", C["s06.b"], True), ("V", "sobe junto", C["s06.b"] + 0.8, True)], 64)
    E.frase(c, t, C["s06.c"], [("V", "g", 60), ("e", "i", 64), ("T", "g", 60)] + ps("em kelvin:", "i", 64), XE, 840, passo=0.1)
    E.frase(c, t, C["s06.c"] + 0.6, [("diretamente proporcionais", "g", 56)], XE, 910, passo=0.1)
    pilula_em(c, t, C["s06.d"], "300 K → 600 K: V dobra", 1230, 980, 40, TINTA)
    E.formula_em(c, t, C["s06.e"], "f{V}{T} = constante", XE, 1010, 60, "g", COR)


# ---------------- isocórica ----------------
def b_isocorica(c, t, C, b):
    E.frase(c, t, C["s07.a"], [("isocórica", "g", 90, COR)], XE, 220)
    E.frase(c, t, C["s07.a"] + 1.4, ps("ou isovolumétrica · córica: espaço", "i", 56, TINTA2), XE, 320, passo=0.1)
    k = ease_io(prog(t, C["s07.c"], 2.2))
    lata(c, 1200, 800, 220, 380, 1.0, chama=ep(t, C["s07.b"] + 0.5, 0.5), t=t)
    manometro(c, 1620, 450, 120, lerp(1, 2.6, k), 3, 1.0)
    termometro(c, 1620, 640, 200, lerp(0.35, 0.9, k), 1.0)
    painel_pvt(c, t, XE, 470, [("V", "fixo", C["s07.b"], False), ("T", "sobe", C["s07.c"], True), ("P", "sobe junto", C["s07.d"], True)], 64)
    pilula_em(c, t, C["s07.d"] + 1.0, "até a lata estourar: nunca aqueça spray", 1300, 1000, 40, ERRADO)
    E.formula_em(c, t, C["s07.e"], "f{P}{T} = constante", XE, 880, 64, "g", COR)


# ---------------- equação geral ----------------
def b_geral(c, t, C, b):
    E.frase(c, t, C["s08.a"], ps("as três regras numa", "i", 76) + [("equação só", "g", 72, COR)], W / 2, 200, "center", 0.12)
    cx1, cx2, y = 760, 1160, 420
    corte = ep(t, C["s09.e"], 0.5)
    frac_q_em(c, t, C["s08.b"], "P1V1", "T1", cx1, y, 110)
    E.formula_em(c, t, C["s08.c"], "=", 960, y + 70, 110, "g", TINTA2, "center")
    frac_q_em(c, t, C["s08.c"] + 0.2, "P2V2", "T2", cx2, y, 110)
    if t >= C["s09"]:
        E.foco(c, t, C["s09.a"], 0.4, lambda a: (centro(c, "1 = antes", cx1, 720, 54, "g", COR, a)))
        E.foco(c, t, C["s09.b"], 0.4, lambda a: (centro(c, "2 = depois", cx2, 720, 54, "g", COR, a)))
        E.foco(c, t, C["s09.c"], 0.4, lambda a: centro(c, "P pressão · V volume · T temperatura em kelvin", W / 2, 820, 50, "i", TINTA2, a))
        if corte > 0:
            for cx in (cx1, cx2):
                M.line(c, cx - 70, y + 150, cx + 70, y + 100, E.COR, corte, 8)
            E.foco(c, t, C["s09.e"] + 0.6, 0.4, lambda a: Q.formula(c, "P1V1 = P2V2", W / 2, 960, 90, COR, a, "center"))
            E.foco(c, t, C["s09.e"] + 1.0, 0.4, lambda a: E.escreve(c, "a isotérmica", W / 2 + 330, 950, 50, "i", TINTA2, a))
        else:
            E.frase(c, t, C["s09.d"], ps("variável parada: aparece igual dos dois lados e", "i", 54, TINTA2) + [("se cancela", "g", 50, COR)], W / 2, 960, "center", 0.08)


# ---------------- exemplo ----------------
def cartao(c, t, t0, x, y, titulo, linhas, tl):
    E.foco(c, t, t0, 0.5, lambda a: (M.rrect(c, x, y, 700, 330, 26, "#FFFFFF", a, shadow=True), E.escreve(c, titulo, x + 40, y + 70, 54, "i", TINTA2, a)))
    for k, (txt, ti) in enumerate(zip(linhas, tl)):
        E.foco(c, t, ti, 0.4, lambda a, txt=txt, k=k: E.formula(c, txt, x + 40, y + 160 + k * 80, 62, "g", COR if "?" in txt else TINTA, a))


def b_exemplo(c, t, C, b):
    if t < C["s11"]:
        cartao(c, t, C["s10.a"], 160, 260, "antes", ["V₁ = 10 L", "P₁ = 1 atm", "T₁ = 27 °C"], [C["s10.a"] + 0.2, C["s10.a"] + 0.8, C["s10.a"] + 1.4])
        cartao(c, t, C["s10.b"], 1060, 260, "depois", ["V₂ = ?", "P₂ = 2 atm", "T₂ = 87 °C"], [C["s10.c"], C["s10.b"] + 0.3, C["s10.b"] + 1.0])
        E.foco(c, t, C["s10.d"], 0.4, lambda a: E.pilula(c, "300 K", 160 + 590, 260 + 160 + 160 - 22, 44, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s10.e"], 0.4, lambda a: E.pilula(c, "360 K", 1060 + 590, 260 + 160 + 160 - 22, 44, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s10.d"], ps("primeiro, tudo em", "i", 66) + [("kelvin", "g", 62, COR)], XE, 760, passo=0.1)
        return
    frac_q_em(c, t, C["s11.a"], "1 · 10", "300", 620, 300, 96)
    E.formula_em(c, t, C["s11.a"] + 0.4, "=", 860, 360, 96, "g", TINTA2, "center")
    frac_q_em(c, t, C["s11.a"] + 0.8, "2 · V2", "360", 1100, 300, 96)
    E.foco(c, t, C["s11.b"], 0.4, lambda a: Q.formula(c, "V2 =", XE, 690, 96, TINTA, a))
    frac_q_em(c, t, C["s11.c"], "1 · 10 · 360", "300 · 2", 800, 640, 84)
    E.formula_em(c, t, C["s11.d"], "= f{3.600}{600} =", 1110, 690, 84, "g", TINTA2)
    bola_txt(c, t, C["s11.d"] + 1.2, "6 L", 1700, 660, 100, 76)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("temperatura em Celsius", "i", 72), XE + 450, 190, passo=0.12)
    E.formula_em(c, t, C["s12.b"], "V₂ = f{1 · 10 · 87}{27 · 2} ≈ 16 L", XE, 460, 96, "g", ERRADO)
    if t >= C["s12.c"]:
        E.risco(c, XE - 10, 520, XE + 1220, 380, t, C["s12.c"], largura=12)
    E.frase(c, t, C["s12.c"], ps("a pressão dobrou, a temperatura subiu pouco:", "i", 60, TINTA2), XE, 680, passo=0.08)
    E.frase(c, t, C["s12.c"] + 2.4, ps("o volume tinha que", "i", 64) + [("diminuir", "g", 60, COR)], XE, 780, passo=0.1)
    E.frase(c, t, C["s12.d"], ps("sem kelvin,", "i", 70) + [("a proporção quebra", "g", 66, COR)], XE, 950, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], ps("o atalho: cada mudança é um", "i", 70, CLARO) + [("fator", "g", 66, BR)], W / 2, 180, "center", 0.12)
        E.frase(c, t, C["s13.b"], [("P", "g", 64, BR)] + ps("dobrou →", "i", 66, CLARO)[:1] + [("→", "g", 64, CLARO), ("V × ½", "g", 64, E.CLARO)], XE, 380, passo=0.12)
        E.frase(c, t, C["s13.c"], [("T", "g", 64, BR), ("300 → 360 K", "g", 64, BR), ("→", "g", 64, CLARO), ("V × 1,2", "g", 64, E.CLARO)], XE, 540, passo=0.12)
        E.formula_em(c, t, C["s13.d"], "10 × ½ × 1,2 =", XE + 200, 780, 100, "g", BR)
        bola_txt(c, t, C["s13.d"] + 1.2, "6 L", XE + 1100, 750, 100, 76)
        return
    E.frase(c, t, C["s14.a"], ps("pressão é", "i", 70, CLARO) + [("inversa,", "g", 66, BR)] + ps("temperatura é", "i", 70, CLARO) + [("direta", "g", 66, BR)], W / 2, 240, "center", 0.12)
    E.frase(c, t, C["s14.b"], ps("pressão:", "i", 64, CLARO) + [("de cabeça para baixo", "g", 60, BR)], XE + 60, 440, passo=0.12)
    E.formula_em(c, t, C["s14.b"] + 1.2, "f{1}{2}", XE + 1250, 450, 90, "g", E.CLARO)
    E.frase(c, t, C["s14.c"], ps("temperatura:", "i", 64, CLARO) + [("na ordem", "g", 60, BR)], XE + 60, 620, passo=0.12)
    E.formula_em(c, t, C["s14.c"] + 1.0, "f{360}{300}", XE + 1250, 630, 90, "g", E.CLARO)
    E.frase(c, t, C["s14.d"], [("não", "g", 60, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("números que não se simplificam", "i", 64, CLARO), W / 2, 880, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s15.a"], ps("cilindro com êmbolo solto:", "i", 64, TINTA2), XE, 320, passo=0.1)
    E.formula_em(c, t, C["s15.a"] + 1.2, "6 L a 27 °C", XE, 440, 96, "g", TINTA)
    E.frase(c, t, C["s15.b"], ps("aquecido a", "i", 70) + [("127 °C,", "g", 66, QUENTE)] + ps("mesma pressão", "i", 70), XE, 580, passo=0.1)
    E.frase(c, t, C["s15.c"], [("1", "g", 56, COR)] + ps("qual é a transformação?", "i", 64), XE, 740, passo=0.1)
    E.frase(c, t, C["s15.d"], [("2", "g", 56, COR)] + ps("e o novo volume?", "i", 64), XE, 860, passo=0.1)
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"], 0.5, lambda a: cilindro(c, t, 1360, 880, 320, 300, 22, a=a))
    else:
        E.relogio(c, t, C["s16.a"], cx=1520, cy=520, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    pilula_em(c, t, C["s17.a"], "pressão parada: isobárica", XE + 340, 240, 56, E.COR)
    E.formula_em(c, t, C["s17.b"], "300 K → 400 K", XE, 440, 96, "g", TINTA)
    E.frase(c, t, C["s17.c"], ps("o volume cresce na", "i", 66) + [("mesma razão", "g", 62, COR)], XE, 580, passo=0.1)
    E.formula_em(c, t, C["s17.d"], "V₂ = f{6 × 400}{300} =", XE, 800, 90, "g", TINTA)
    bola_txt(c, t, C["s17.e"], "8 L", XE + 1060, 770, 100, 76, CERTO)
    k = ease_io(prog(t, C["s17.b"], 2.0))
    cilindro(c, t, 1440, 640, 300, lerp(240, 320, k), 20)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s18.a", [("iso-", "g", 66, COR)] + ps("diz o que fica parado", "i", 70)),
                 ("s18.b", ps("a equação geral resolve as três", "i", 70)),
                 ("s18.c", ps("temperatura sempre em", "i", 70) + [("kelvin", "g", 66, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.formula_em(c, t, C["s19.a"], "PV = nRT", XE, 470, 150, "g", COR)
    E.frase(c, t, C["s19.b"], ps("a massa de gás num", "i", 70) + [("cilindro", "g", 66)], XE, 640, passo=0.12)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 780, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 805, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, isotermica=b_isotermica, isobarica=b_isobarica, isocorica=b_isocorica, geral=b_geral,
              exemplo=b_exemplo, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
