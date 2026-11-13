"""Visual — Estudativo · QUI-CAL-016: difusão de gases, lei de Graham.

Segue a linguagem dos gases (cabeçalho da QUI-CAL-010), a da trilha (QUI-CAL-001) e a da Química (QUI-MIS-001).
O TUBO DE GRAHAM (tubo_graham): algodões nas pontas, as nuvens de partícula de cada gás avançam (na cor CPK do átomo que as
identifica: N azul na amônia, Cl verde no HCl) e o anel branco nasce no ponto de encontro. A CORRIDA (pista) mostra dois gases
na mesma pista, com a velocidade na razão da lei de Graham. A raiz sempre aparece desenhada (E.formula com r{...}).
Peças candidatas ao kit quimica.py: tubo_graham() e pista()."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-016_lei_de_graham.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("difusao", "lei", "atalho", "questao", "fim"))
BR = "#FFFFFF"
RAZ = math.sqrt(36.5 / 17)
ENC = RAZ / (1 + RAZ)

# todas as contas da aula
assert math.sqrt(32 / 2) == 4 and 32 / 2 == 16 and math.sqrt(16 / 4) == 2 and abs(RAZ - 1.47) < 0.01 and 0.55 < ENC < 0.65
assert math.sqrt(4) == 2 and math.sqrt(9) == 3 and math.sqrt(16) == 4


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


def tubo_graham(c, t, t0, x0, x1, y, d=4.0, a=1.0):
    """tubo com amônia à esquerda e ácido clorídrico à direita; as nuvens se encontram em ENC e nasce o anel branco"""
    if a <= 0:
        return
    h = 90
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0, y - h / 2, x1, y + h / 2), h / 2, h / 2), M.paint("#FFFFFF", 0.5 * a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0, y - h / 2, x1, y + h / 2), h / 2, h / 2), M.paint(Q.VIDRO, a, stroke=5))
    for xx in (x0 + 50, x1 - 50):
        c.drawCircle(xx, y, 34, M.paint("#F2F2EE", a))
    p = ease_out(prog(t, t0, d))
    L = x1 - x0 - 100
    fe = x0 + 50 + L * ENC * p
    fd = x1 - 50 - L * (1 - ENC) * p
    rnd = random.Random(3)
    for k in range(60):
        u, v = rnd.random(), rnd.random() - 0.5
        xe = x0 + 70 + (fe - x0 - 70) * u ** 0.7
        xd = x1 - 70 - (x1 - 70 - fd) * u ** 0.7
        c.drawCircle(xe + 3 * math.sin(t * 7 + k), y + v * 60, 6, M.paint(Q.cor_el("N"), a * (0.4 + 0.6 * u)))
        c.drawCircle(xd + 3 * math.cos(t * 6 + k), y + v * 60, 6, M.paint(Q.cor_el("Cl"), a * (0.4 + 0.6 * u)))
    if p >= 1:
        q = ep(t, t0 + d, 0.5) * a
        M.rrect(c, fe - 22, y - h / 2 + 6, 44, h - 12, 12, "#FFFFFF", q, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(fe - 22, y - h / 2 + 6, 44, h - 12), 12, 12), M.paint(TINTA2, q, stroke=3))


def pista(c, t, t0, x0, x1, y, el, vel, rot, a=1.0, r=40):
    """corrida: o gás anda da esquerda para a direita com velocidade proporcional a vel (1 = chega no fim em 4 s)"""
    if a <= 0:
        return
    M.line(c, x0, y + r + 14, x1, y + r + 14, FIO, a, 4)
    p = max(0.0, min(1.0, (t - t0) * vel / 4.0))
    x = lerp(x0 + r, x1 - r, p)
    Q.atomo(c, x, y, r, el, a)
    if rot:
        Q.formula(c, rot, x0 - 90, y + 20, 60, TINTA, a, "center")


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        tubo_graham(c, t, C["s01.c"], 200, 1720, 520, d=3.0)
        E.foco(c, t, C["s01.a"], 0.4, lambda a: (Q.formula(c, "NH3", 250, 680, 80, TINTA, a, "center"), centro(c, "amônia", 250, 750, 46, "i", TINTA2, a)))
        E.foco(c, t, C["s01.b"], 0.4, lambda a: (Q.formula(c, "HCl", 1670, 680, 80, TINTA, a, "center"), centro(c, "ácido clorídrico", 1670, 750, 46, "i", TINTA2, a)))
        xm = 250 + (1670 - 250) * 0.5
        E.foco(c, t, C["s01.e"], 0.4, lambda a: (M.line(c, xm, 430, xm, 610, TINTA2, a, 3, dash=[10, 10]), centro(c, "meio", xm, 410, 44, "i", TINTA2, a)))
        E.frase(c, t, C["s01.d"], ps("onde se encontram:", "i", 64) + [("anel branco", "g", 60, COR)], XE, 240, passo=0.1)
        E.frase(c, t, C["s01.f"], ps("nasce mais perto do", "i", 70) + [("ácido.", "g", 66, COR)] + ps("por quê?", "i", 70), XE, 930, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("qual", "i", 74), ("gás", "g", 70), ("é", "i", 74), ("mais", "i", 74), ("rápido", "g", 70, COR)]),
                 (C["s02.c"], [("quantas", "i", 74), ("vezes:", "i", 74), ("Graham", "g", 70, COR)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("raiz", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03.a"] - 0.6, ps("você precisa de", "i", 80) + [("duas coisas", "g", 76, COR)], XE, 200, passo=0.12)
    y = [430, 760]
    for i, k in enumerate(("s03.b", "s03.c")):
        E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, XE + 40, y[i] - 30, 44, a=a), centro(c, str(i + 1), XE + 40, y[i] - 8, 54, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, ps("massa molar de um gás", "i", 66), XE + 110, y[0], passo=0.1)
    Q.formula_em(c, t, C["s03.b"] + 0.6, "O2", XE + 900, y[0] + 4, 80)
    E.formula_em(c, t, C["s03.b"] + 0.8, "= 32 g/mol", XE + 1040, y[0] + 4, 70, "g", TINTA2)
    E.frase(c, t, C["s03.c"] + 0.1, ps("raiz quadrada exata", "i", 66), XE + 110, y[1], passo=0.1)
    E.formula_em(c, t, C["s03.c"] + 0.8, "r{16} = 4", XE + 900, y[1] + 4, 90, "g", COR)


# ---------------- difusão ----------------
def b_difusao(c, t, C, b):
    E.frase(c, t, C["s04.a"], ps("um perfume aberto num canto da sala", "i", 64), XE, 220, passo=0.1)
    E.foco(c, t, C["s04.a"] + 0.3, 0.5, lambda a: (M.rrect(c, 300, 420, 110, 160, 20, "#E7B6D0", a), M.rrect(c, 330, 380, 50, 50, 8, "#8A8F96", a)))
    p = ease_out(prog(t, C["s04.b"], 3.0))
    rnd = random.Random(5)
    for k in range(70):
        u = rnd.random()
        ang = (rnd.random() - 0.5) * 1.4
        dist = p * (200 + 1200 * u)
        x, y = 360 + dist * math.cos(ang), 400 + dist * math.sin(ang) * 0.5
        if x < 1820:
            c.drawCircle(x + 6 * math.sin(t * 5 + k), y, 9, M.paint("#C2509A", 0.7 * min(1, p * 3)))
    E.frase(c, t, C["s04.c"], [("difusão:", "g", 70, COR)] + ps("o gás se espalha no outro", "i", 66), XE, 760, passo=0.12)
    E.frase(c, t, C["s04.d"], [("efusão:", "g", 70, COR)] + ps("escapa por um furinho", "i", 66), XE, 880, passo=0.12)
    E.foco(c, t, C["s04.e"] + 0.4, 0.4, lambda a: E.escreve(c, "a mesma regra", XE, 990, 56, "i", TINTA2, a))


# ---------------- por quê ----------------
def b_porque(c, t, C, b):
    E.frase(c, t, C["s05.a"], ps("mesma temperatura:", "i", 64, TINTA2) + [("mesma agitação", "g", 60, COR)], XE, 220, passo=0.1)
    tb = C["s05.b"] + 0.6
    pl = ease_out(prog(t, tb, 1.6))
    ph = ease_out(prog(t, tb, 3.6))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: (M.line(c, 300, 560, 1800, 560, FIO, a, 4), M.line(c, 300, 820, 1800, 820, FIO, a, 4)))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: (E.bola(c, lerp(340, 1700, pl), 520, 36, "#FFFFFF", a), E.bola(c, lerp(370, 1300, ph), 740, 76, "#2A2B31", a)))
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.escreve(c, "leve: voa", XE, 470, 56, "g", COR, a))
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.escreve(c, "pesada: devagar, mas entra uma raiz", XE, 900, 56, "g", TINTA, a))
    E.frase(c, t, C["s05.e"], ps("massa molar menor:", "i", 64) + [("mais rápido", "g", 60, COR)], XE, 1010, passo=0.1)


# ---------------- a lei ----------------
def b_lei(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], ps("lei de", "i", 80) + [("Graham", "g", 76, COR)], XE, 220, passo=0.12)
        E.frase(c, t, C["s06.b"], ps("velocidade: inversamente proporcional à", "i", 60) + [("raiz da massa molar", "g", 56, COR)], XE, 340, passo=0.08)
        E.foco(c, t, C["s06.c"], 0.4, lambda a: E.escreve(c, "aqui, v é velocidade", XE, 470, 52, "i", TINTA2, a))
        E.foco(c, t, C["s06.d"], 0.6, lambda a: E.formula(c, "f{v₁}{v₂} = r{f{M₂}{M₁}}", W / 2, 720, 140, "g", TINTA, a, "center"))
        if t >= C["s06.e"]:
            q = ep(t, C["s06.e"], 0.4)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(W / 2 + 60, 560, 300, 260), 30, 30), M.paint(E.COR, q, stroke=6))
            E.foco(c, t, C["s06.f"], 0.4, lambda a: E.pilula(c, "a massa do outro vai em cima", W / 2 + 210, 920, 46, "g", fundo=E.COR, a=a))
        return
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("hidrogênio contra oxigênio", "i", 70), XE, 200, passo=0.1)
        E.foco(c, t, C["s07.b"], 0.4, lambda a: (Q.formula(c, "H2", XE, 340, 80, TINTA, a), E.formula(c, "M = 2", XE + 160, 340, 64, "g", TINTA2, a)))
        E.foco(c, t, C["s07.c"], 0.4, lambda a: (Q.formula(c, "O2", XE + 600, 340, 80, TINTA, a), E.formula(c, "M = 32", XE + 760, 340, 64, "g", TINTA2, a)))
        E.formula_em(c, t, C["s07.d"], "r{f{32}{2}} = r{16} =", XE, 560, 110, "g", TINTA)
        bola_txt(c, t, C["s07.e"], "4", XE + 900, 520, 80, 100)
        pista(c, t, C["s07.f"], 360, 1800, 760, "H", 4.0, "H2", r=34)
        pista(c, t, C["s07.f"], 360, 1800, 920, "O", 1.0, "O2", r=44)
        E.foco(c, t, C["s07.f"] + 1.2, 0.4, lambda a: E.pilula(c, "4 vezes mais rápido", 1500, 620, 46, "g", fundo=E.COR, a=a))
        return
    tubo_graham(c, t, C["s08.a"] - 0.5, 200, 1720, 380, d=0.01)
    E.foco(c, t, C["s08.b"], 0.4, lambda a: (Q.formula(c, "NH3", 250, 560, 80, TINTA, a, "center"), centro(c, "M = 17", 250, 640, 56, "g", COR, a)))
    E.foco(c, t, C["s08.c"], 0.4, lambda a: (Q.formula(c, "HCl", 1670, 560, 80, TINTA, a, "center"), centro(c, "M = 36,5", 1670, 640, 56, "g", TINTA2, a)))
    E.frase(c, t, C["s08.d"], ps("a amônia é mais leve: anda", "i", 64) + [("mais tubo", "g", 60, COR)], XE, 820, passo=0.1)
    E.frase(c, t, C["s08.e"], ps("o anel nasce", "i", 64) + [("perto do ácido", "g", 60, COR)], XE, 940, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s09"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s09.a"], ps("esquecer a raiz", "i", 72), XE + 450, 190, passo=0.12)
    E.formula_em(c, t, C["s09.b"], "f{32}{2} = 16", XE, 440, 110, "g", ERRADO)
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "16 vezes mais rápido?", XE + 560, 440, 70, "g", ERRADO, a))
    if t >= C["s09.d"]:
        E.risco(c, XE + 540, 460, XE + 1340, 380, t, C["s09.d"], largura=11)
    E.frase(c, t, C["s09.d"], ps("massa 16 vezes menor:", "i", 64) + [("só 4 vezes mais rápido", "g", 60, COR)], XE, 700, passo=0.1)
    E.formula_em(c, t, C["s09.e"], "r{16} = 4", XE, 900, 110, "g", COR)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("o atalho: guarde as", "i", 70, CLARO) + [("raízes redondas", "g", 66, BR)], W / 2, 190, "center", 0.12)
        for k, (m, v, tk) in enumerate((("massa × 4", "velocidade ÷ 2", "s10.b"), ("massa × 9", "velocidade ÷ 3", "s10.c"), ("massa × 16", "velocidade ÷ 4", "s10.d"))):
            y = 400 + k * 190
            E.foco(c, t, C[tk], 0.4, lambda a, m=m, v=v, y=y: (E.formula(c, m, 560, y, 90, "g", BR, a, "center"), E.formula(c, "→", W / 2, y, 90, "g", CLARO, a, "center"),
                                                             E.formula(c, v, 1380, y, 90, "g", E.CLARO, a, "center")))
        return
    E.frase(c, t, C["s11.a"], ps("o tempo é o", "i", 70, CLARO) + [("contrário", "g", 66, BR)] + ps("da velocidade", "i", 70, CLARO), W / 2, 230, "center", 0.12)
    E.formula_em(c, t, C["s11.b"], "2 × mais rápido = ½ do tempo", W / 2, 400, 84, "g", E.CLARO, "center")
    E.frase(c, t, C["s11.c"], ps("é só a", "i", 66, CLARO) + [("raiz da razão", "g", 62, BR)], W / 2, 560, "center", 0.12)
    E.frase(c, t, C["s11.d"], [("não", "g", 60, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("raiz não exata, como", "i", 64, CLARO), W / 2, 740, "center", 0.1)
    E.formula_em(c, t, C["s11.d"] + 2.0, "r{f{36,5}{17}} ≈ 1,5", W / 2, 880, 84, "g", BR, "center")
    E.foco(c, t, C["s11.e"], 0.4, lambda a: centro(c, "diga quem é mais rápido, ou estime", W / 2, 1010, 50, "i", CLARO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s12"], ps("hora de testar", "i", 72, COR), XE, 180)
    for k, (f, m, tk, el) in enumerate((("He", "M = 4", "s12.a", "He"), ("CH4", "M = 16", "s12.b", "C"))):
        x = 360 + 620 * k
        E.foco(c, t, C[tk], 0.5, lambda a, x=x, el=el: balao(c, t, t, x, 470, 170, 200, 16, Q.cor_el(el) if el == "He" else "#6B7078", a, semente=3 + k))
        Q.formula_em(c, t, C[tk] + 0.3, f, x, 820, 90, align="center")
        E.foco(c, t, C[tk] + 0.5, 0.4, lambda a, x=x, m=m: centro(c, m, x, 900, 56, "g", COR, a))
    E.frase(c, t, C["s12.c"], [("1", "g", 56, COR)] + ps("qual murcha primeiro?", "i", 62), 1180, 420, passo=0.1)
    E.frase(c, t, C["s12.d"], [("2", "g", 56, COR)] + ps("quantas vezes mais rápido?", "i", 62), 1180, 540, passo=0.1)
    if t >= C["s13"]:
        E.relogio(c, t, C["s13.a"], cx=1500, cy=800, r=120)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s14.a"], [("hélio", "g", 70, COR)] + ps("é mais leve:", "i", 70), XE, 240, passo=0.12)
    E.frase(c, t, C["s14.b"], ps("o balão de hélio", "i", 70) + [("murcha primeiro", "g", 66)], XE, 360, passo=0.12)
    E.formula_em(c, t, C["s14.c"], "r{f{16}{4}} = r{4} =", XE, 620, 110, "g", TINTA)
    bola_txt(c, t, C["s14.d"], "2", XE + 820, 585, 80, 100, CERTO)
    E.frase(c, t, C["s14.e"], ps("o hélio escapa", "i", 66) + [("2 vezes mais rápido", "g", 62, COR)], XE, 860, passo=0.12)
    pista(c, t, C["s14.e"], 1240, 1820, 300, "He", 2.0, "", r=34)
    pista(c, t, C["s14.e"], 1240, 1820, 460, "C", 1.0, "", r=40)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s15"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s15.a", [("mais leve", "g", 66, COR)] + ps("se espalha mais rápido", "i", 70)),
                 ("s15.b", ps("razão das velocidades =", "i", 70) + [("raiz da razão das massas", "g", 62)]),
                 ("s15.c", ps("com as massas", "i", 70) + [("trocadas", "g", 66, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s16"] - 0.1, resumo)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], [("próxima", "i", 80), ("aula:", "i", 80), ("praticando", "g", 76, COR)], XE, 250, passo=0.12)
    E.frase(c, t, C["s16.a"], [("balões,", "g", 76), ("pneus", "g", 76), ("e", "i", 80), ("cilindros", "g", 76)], XE, 430, passo=0.12)
    E.frase(c, t, C["s16.b"], ps("todas as equações dos gases", "i", 70), XE, 590, passo=0.1)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 780, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s16.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 805, p), ep(t, C["s16.c"] + 0.2, 0.4))
    E.frase(c, t, C["s16.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, difusao=b_difusao, porque=b_porque, lei=b_lei, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
