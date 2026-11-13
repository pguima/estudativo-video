"""Visual — Estudativo · QUI-CAL-012: equação de Clapeyron, PV = nRT.

Segue a linguagem dos gases (cabeçalho da QUI-CAL-010), a da trilha (QUI-CAL-001) e a da Química (QUI-MIS-001).
A equação PV = nRT fica grande, com cada letra acendendo na fala e a legenda ao lado (letra, nome e unidade). O TANQUE (tanque)
é a cápsula de gás com válvula, com as partículas dentro. A constante R aparece sempre com a unidade inteira. No atalho, o
"24,6" (R vezes T a 300 K) vai numa pílula clara e a escolha da equação vira uma bifurcação de duas setas.
Peças candidatas ao kit quimica.py: tanque() e legenda_letras()."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-012_clapeyron_pv_nrt.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("origem", "letras", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 6 * 41 == 246 and abs(0.082 * 300 - 24.6) < 1e-9 and abs(246 / 24.6 - 10) < 1e-9 and 10 * 32 == 320
assert abs(6 * 41000 / 24.6 - 10000) < 1e-6 and 10 * 12.3 == 123 and abs(123 / 24.6 - 5) < 1e-9 and 5 * 44 == 220 and 27 + 273 == 300


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


def tanque(c, t, cx, cy, w, h, n=30, a=1.0, cor_gas=None, rot=None):
    """cilindro de gás (cápsula) com válvula e as partículas dentro"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), w / 2, w / 2)
    c.drawRRect(r, M.paint("#E3E6EA", a))
    c.save(); c.clipRRect(r, doAntiAlias=True)
    Q.particulas(c, t, cx - w / 2 + 10, cy - h / 2 + 30, w - 20, h - 60, n, "gas", tipos=[(cor_gas or "O", 1.0)], r=12, semente=4, a=a)
    c.restore()
    c.drawRRect(r, M.paint("#6B7078", a, stroke=7))
    M.rrect(c, cx - 30, cy - h / 2 - 60, 60, 64, 10, "#6B7078", a)
    M.rrect(c, cx - 70, cy - h / 2 - 80, 140, 28, 10, E.COR, a)
    if rot:
        centro(c, rot, cx, cy + h / 2 + 70, 50, "g", TINTA, a)


def legenda_letras(c, t, x, y, itens, size=56):
    """itens = [(letra, texto, instante)]: a letra na grotesca turquesa e a explicação em itálico"""
    for k, (l, txt, ti) in enumerate(itens):
        yy = y + k * size * 1.75
        E.foco(c, t, ti, 0.4, lambda a, l=l, txt=txt, yy=yy: (E.escreve(c, l, x, yy, size * 1.25, "g", COR, a),
                                                             E.escreve(c, txt, x + size * 1.3, yy, size, "i", TINTA, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: tanque(c, t, 1450, 600, 300, 620, 34, a, "O", "41 L"))
        E.frase(c, t, C["s01.a"], ps("um tanque de", "i", 70) + [("41 litros", "g", 66)] + ps("de oxigênio", "i", 70), XE, 220, passo=0.1)
        E.frase(c, t, C["s01.b"], [("6 atm", "g", 76, COR), ("e", "i", 80), ("27 °C", "g", 76, COR)], XE, 380, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("quantos gramas lá dentro?", "i", 76), XE, 560, passo=0.12)
        E.frase(c, t, C["s01.c"] + 2.0, ps("sem abrir para pesar", "i", 60, TINTA2), XE, 660, passo=0.1)
        E.foco(c, t, C["s01.d"], 0.5, lambda a: E.formula(c, "PV = nRT", XE, 880, 170, "g", COR, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("cada", "i", 74), ("letra", "g", 70), ("de", "i", 74), ("PV = nRT", "g", 70, COR)]),
                 (C["s02.c"], [("mols", "g", 70), ("e", "i", 74), ("massa", "g", 70), ("de", "i", 74), ("um", "i", 74), ("gás", "g", 70)]),
                 (C["s02.d"], [("quando", "i", 74), ("R = 0,082", "g", 70, COR)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03.a"] - 0.6, ps("você precisa de", "i", 80) + [("três coisas", "g", 76, COR)], XE, 200, passo=0.12)
    y = [400, 640, 880]
    for i, k in enumerate(("s03.b", "s03.c", "s03.d")):
        E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, XE + 40, y[i] - 30, 44, a=a), centro(c, str(i + 1), XE + 40, y[i] - 8, 54, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, ps("equação geral, em kelvin", "i", 66), XE + 110, y[0], passo=0.1)
    frac_q_em(c, t, C["s03.b"] + 0.8, "P1V1", "T1", 1100, y[0] - 30, 64)
    E.formula_em(c, t, C["s03.b"] + 0.9, "=", 1230, y[0] + 10, 64, "g", TINTA2)
    frac_q_em(c, t, C["s03.b"] + 1.0, "P2V2", "T2", 1360, y[0] - 30, 64)
    E.frase(c, t, C["s03.c"] + 0.1, [("o", "i", 66), ("mol", "g", 62, COR)], XE + 110, y[1], passo=0.1)
    E.formula_em(c, t, C["s03.c"] + 0.4, "1 mol = 6 × 10^{23}", 1000, y[1] + 4, 64, "g", TINTA2)
    E.frase(c, t, C["s03.d"] + 0.1, [("a", "i", 66), ("massa molar", "g", 62, COR)], XE + 110, y[2], passo=0.1)
    Q.formula_em(c, t, C["s03.d"] + 0.4, "O2", 1000, y[2] + 4, 70)
    E.formula_em(c, t, C["s03.d"] + 0.6, "= 32 g/mol", 1140, y[2] + 4, 64, "g", TINTA2)


# ---------------- de onde vem ----------------
def b_origem(c, t, C, b):
    if t < C["s05"]:
        frac_q_em(c, t, C["s04.a"], "PV", "T", 420, 330, 110)
        E.formula_em(c, t, C["s04.a"] + 0.5, "não muda", 560, 400, 70, "i", TINTA2)
        E.frase(c, t, C["s04.b"], ps("mas depende de", "i", 66) + [("quanto gás", "g", 62, COR)], XE, 640, passo=0.1)
        E.foco(c, t, C["s04.c"], 0.5, lambda a: (cilindro(c, t, 1080, 760, 260, 300, 12, a=a, embolo=False, rotulo="n mols"),
                                                 cilindro(c, t, 1440, 760, 260, 300, 24, a=a, embolo=False, rotulo="2n mols", semente=8)))
        E.foco(c, t, C["s04.c"] + 0.6, 0.4, lambda a: E.pilula(c, "o valor dobra", 1440, 360, 46, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s04.d"], ps("então", "i", 70), XE, 880, passo=0.1)
        frac_q_em(c, t, C["s04.d"] + 0.4, "PV", "T", XE + 360, 840, 84)
        E.formula_em(c, t, C["s04.d"] + 0.8, "= n × constante", XE + 470, 890, 76, "g", COR)
        return
    E.frase(c, t, C["s05.a"], ps("passe o T para o outro lado:", "i", 70), W / 2, 300, "center", 0.12)
    E.frase(c, t, C["s05.a"] + 1.2, ps("a equação de", "i", 70, TINTA2) + [("Clapeyron", "g", 66)], W / 2, 400, "center", 0.12)
    E.foco(c, t, C["s05.b"], 0.6, lambda a: E.formula(c, "PV = nRT", W / 2, 720, 240, "g", COR, a, "center"))


# ---------------- as letras ----------------
def b_letras(c, t, C, b):
    if t < C["s07"]:
        E.formula_em(c, t, C["s06"], "PV = nRT", XE, 330, 160, "g", TINTA)
        legenda_letras(c, t, XE + 40, 500, [("P", "pressão, em atmosferas", C["s06.a"]), ("V", "volume, em litros", C["s06.b"]),
                                            ("n", "número de mols", C["s06.c"]), ("T", "temperatura, sempre em kelvin", C["s06.d"]),
                                            ("R", "constante dos gases: a mesma para todos", C["s06.e"])], 52)
        E.foco(c, t, C["s06"] + 0.4, 0.5, lambda a: tanque(c, t, 1560, 600, 260, 520, 26, a, "O"))
        return
    E.frase(c, t, C["s07.a"], ps("com", "i", 70) + [("atm", "g", 66, COR)] + ps("e", "i", 70) + [("litro:", "g", 66, COR)], XE, 260, passo=0.12)
    E.foco(c, t, C["s07.b"], 0.5, lambda a: E.formula(c, "R = 0,082", XE, 470, 150, "g", COR, a))
    E.foco(c, t, C["s07.b"] + 0.8, 0.4, lambda a: E.formula(c, "f{atm · L}{mol · K}", XE + 860, 440, 72, "g", TINTA, a))
    E.frase(c, t, C["s07.c"], ps("pressão em mmHg ou Pa?", "i", 64) + [("o R muda", "g", 60, COR)], XE, 680, passo=0.1)
    E.foco(c, t, C["s07.d"], 0.4, lambda a: (E.pilula(c, "62,3 mmHg · L/(mol · K)", XE + 380, 780, 42, "b", fundo="#5A5F66", a=a),
                                             E.pilula(c, "8,31 J/(mol · K)", XE + 1000, 780, 42, "b", fundo="#5A5F66", a=a)))
    E.foco(c, t, C["s07.d"] + 0.6, 0.4, lambda a: E.escreve(c, "a prova costuma dar o valor", XE + 1260, 795, 46, "i", TINTA2, a))
    pilula_em(c, t, C["s07.e"], "unidades do R = unidades do problema", W / 2, 940, 54, TINTA)


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    linhas = (("P = 6 atm", "s08.a"), ("V = 41 L", "s08.b"), ("T = 27 + 273 = 300 K", "s08.c"), ("n = ?", "s08.d"))
    for k, (s, tk) in enumerate(linhas):
        E.formula_em(c, t, C[tk], s, XE, 230 + k * 95, 64, "g", COR if "?" in s else TINTA)
    E.foco(c, t, C["s08"], 0.5, lambda a: tanque(c, t, 1680, 360, 180, 360, 18, a, "O"))
    if t < C["s09"]:
        return
    E.foco(c, t, C["s09.a"], 0.4, lambda a: E.escreve(c, "n =", XE, 720, 90, "g", TINTA, a))
    frac_q_em(c, t, C["s09.a"] + 0.3, "PV", "RT", XE + 260, 680, 84)
    if t < C["s10"]:
        E.formula_em(c, t, C["s09.b"], "6 × 41 = 246", 760, 650, 70, "g", TINTA)
        E.formula_em(c, t, C["s09.c"], "0,082 × 300 = 24,6", 760, 780, 70, "g", TINTA)
        E.formula_em(c, t, C["s09.d"], "246 ÷ 24,6 =", 760, 940, 76, "g", TINTA2)
        bola_txt(c, t, C["s09.d"] + 1.2, "10 mol", 1420, 910, 100, 54)
        return
    E.formula_em(c, t, C["s10"], "n = 10 mol", 760, 650, 76, "g", COR)
    E.foco(c, t, C["s10.b"], 0.4, lambda a: (Q.formula(c, "O2", 760, 790, 70, TINTA, a), E.formula(c, "= 32 g/mol", 880, 790, 60, "g", TINTA2, a)))
    E.formula_em(c, t, C["s10.c"], "10 × 32 =", 760, 940, 76, "g", TINTA2)
    bola_txt(c, t, C["s10.c"] + 1.2, "320 g", 1300, 910, 100, 56)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("misturar as unidades", "i", 72), XE + 450, 190, passo=0.12)
    E.formula_em(c, t, C["s11.b"], "V em mL:", XE, 400, 76, "g", TINTA2)
    E.formula_em(c, t, C["s11.c"], "41 L = 41.000 mL", XE + 420, 400, 76, "g", TINTA)
    E.formula_em(c, t, C["s11.d"], "n = f{6 × 41.000}{24,6} = 10.000 mol", XE, 600, 84, "g", ERRADO)
    if t >= C["s11.d"] + 1.6:
        E.risco(c, XE - 10, 640, XE + 1300, 540, t, C["s11.d"] + 1.6, largura=12)
        pilula_em(c, t, C["s11.d"] + 1.8, "mil vezes mais gás", 1640, 590, 44, ERRADO)
    E.frase(c, t, C["s11.e"], [("R = 0,082", "g", 66, COR), ("→", "g", 66, TINTA2), ("litros", "g", 66)] + ps("e", "i", 70) + [("atmosferas", "g", 66)], XE, 860, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"], ps("o atalho: a 27 °C,", "i", 70, CLARO) + [("R × T", "g", 66, BR)], W / 2, 190, "center", 0.12)
        E.formula_em(c, t, C["s12.a"] + 1.2, "0,082 × 300 =", W / 2 - 60, 370, 96, "g", BR, "right")
        bola_txt(c, t, C["s12.a"] + 1.8, "24,6", W / 2 + 140, 340, 96, 72)
        E.foco(c, t, C["s12.b"], 0.4, lambda a: centro(c, "aparece em muitas provas", W / 2, 500, 54, "i", CLARO, a))
        E.foco(c, t, C["s12.c"], 0.4, lambda a: E.escreve(c, "n =", 560, 690, 90, "g", BR, a))
        frac_q_em(c, t, C["s12.c"] + 0.3, "PV", "24,6", 840, 650, 84, escuro=True)
        E.formula_em(c, t, C["s12.d"], "246 = 10 × 24,6", 1040, 700, 80, "g", BR)
        pilula_em(c, t, C["s12.e"] + 0.4, "10 mol, de cabeça", W / 2, 900, 56, E.COR)
        return
    E.frase(c, t, C["s13.a"], ps("qual equação usar?", "i", 72, CLARO), W / 2, 200, "center", 0.12)
    for k, (tk, tl, rot, eq) in enumerate((("s13.b", "s13.c", "antes e depois, gás preso", "equação geral"), ("s13.d", "s13.e", "pede mols ou massa", "PV = nRT"))):
        x = 560 + 800 * k
        p = ep(t, C[tk], 0.5)
        if p > 0:
            M.arrow(c, W / 2, 260, lerp(W / 2, x, ease_io(p)), lerp(260, 420, ease_io(p)), E.CLARO, 1.0, 6, 22)
        E.foco(c, t, C[tk] + 0.2, 0.4, lambda a, x=x, rot=rot: centro(c, rot, x, 500, 52, "i", BR, a))
        E.foco(c, t, C[tl], 0.4, lambda a, x=x, eq=eq: E.pilula(c, eq, x, 620, 64, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s13.f"], [("não", "g", 58, ERRADO), ("compensa:", "i", 62, CLARO)] + ps("o 24,6 só vale a 300 K; fora disso,", "i", 62, CLARO) + [("R × T", "g", 58, BR)], W / 2, 860, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s14.a"], ps("um cilindro de", "i", 70) + [("12,3 L", "g", 66)] + ps("de gás carbônico", "i", 70), XE, 330, passo=0.1)
    E.frase(c, t, C["s14.b"], [("10 atm", "g", 72, COR), ("e", "i", 76), ("27 °C", "g", 72, COR)], XE, 470, passo=0.12)
    Q.formula_em(c, t, C["s14.c"], "CO2", XE, 620, 90)
    E.formula_em(c, t, C["s14.c"] + 0.4, "M = 44 g/mol", XE + 240, 620, 70, "g", TINTA2)
    E.frase(c, t, C["s14.d"], ps("quantos gramas de gás?", "i", 70), XE, 800, passo=0.1)
    if t < C["s15"]:
        E.foco(c, t, C["s14.a"] + 0.4, 0.5, lambda a: tanque(c, t, 1520, 560, 240, 440, 22, a, E.COR))
    else:
        E.relogio(c, t, C["s15.a"], cx=1520, cy=480, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s16.a"], "27 °C = 300 K → RT = 24,6", XE, 260, 76, "g", TINTA2)
    E.formula_em(c, t, C["s16.b"], "PV = 10 × 12,3 = 123", XE, 440, 84, "g", TINTA)
    E.formula_em(c, t, C["s16.c"], "n = 123 ÷ 24,6 = 5 mol", XE, 620, 84, "g", TINTA)
    E.formula_em(c, t, C["s16.d"], "5 × 44 =", XE, 820, 96, "g", TINTA2)
    bola_txt(c, t, C["s16.d"] + 1.2, "220 g", XE + 620, 790, 110, 62, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s17.a", [("PV = nRT", "g", 66, COR)] + ps("liga P, V e T aos mols", "i", 70)),
                 ("s17.b", [("atm", "g", 66), ("e", "i", 70), ("litro:", "g", 66), ("R = 0,082", "g", 66, COR)]),
                 ("s17.c", ps("temperatura sempre em", "i", 70) + [("kelvin", "g", 66, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s18.a"], [("1 mol", "g", 76, COR)] + ps("de qualquer gás", "i", 80), XE, 420, passo=0.12)
    E.frase(c, t, C["s18.b"], [("22,4 L", "g", 90, COR)] + ps("a 0 °C e 1 atm", "i", 76), XE, 600, passo=0.12)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 780, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 805, p), ep(t, C["s18.c"] + 0.2, 0.4))
    E.frase(c, t, C["s18.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, origem=b_origem, letras=b_letras, exemplo=b_exemplo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
