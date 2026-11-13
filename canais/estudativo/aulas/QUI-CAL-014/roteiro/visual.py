"""Visual — Estudativo · QUI-CAL-014: misturas gasosas e pressão parcial.

Segue a linguagem dos gases (cabeçalho da QUI-CAL-010), a da trilha (QUI-CAL-001) e a da Química (QUI-MIS-001).
Na mistura, cada gás tem a sua cor CPK (O vermelho, N azul, He ciano) dentro do mesmo cilindro. A PRESSÃO TOTAL é uma barra
cortada nas PRESSÕES PARCIAIS (barra_pressao), cada parte na cor do gás e com o valor em atm; a soma fica na ponta.
O ar é a pizza 78 / 21 / 1. Na montanha, a barra encolhe inteira e as fatias continuam na mesma proporção.
Peça candidata ao kit quimica.py: barra_pressao() (pressão total cortada nas parciais)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-014_pressao_parcial.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("mistura", "fracao", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CN, CO, CHE = Q.cor_el("N"), Q.cor_el("O"), Q.cor_el("He")

# todas as contas da aula
assert 2 / 10 == 0.2 and 0.2 * 10 == 2 and 10 - 2 == 8 and 0.21 * 1 == 0.21
assert 32 / 32 == 1 and 4 / 4 == 1 and abs(32 / 36 - 0.89) < 0.01 and 0.1 * 5 == 0.5 and 0.2 * 5 == 1
assert 1 / 4 * 8 == 2 and 3 / 4 * 8 == 6 and 2 + 6 == 8


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


def barra_pressao(c, t, t0, x, y, w, h, partes, d=0.9, total=None, escuro=False):
    """partes = [(cor, fração, rótulo)]; w = largura que vale a pressão total"""
    p = ease_out(prog(t, t0, d))
    if p <= 0:
        return
    xx = x
    for cor, f, rot in partes:
        wk = w * f
        vis = min(wk, max(0.0, w * p - (xx - x)))
        if vis > 2:
            M.rrect(c, xx + 3, y, vis - 6, h, 14, cor, 1.0)
            if vis >= wk - 1 and rot and wk > 90:
                centro(c, rot, xx + wk / 2, y + h / 2 + 18, 48 if wk > 220 else 36, "g", BR, 1.0)
        xx += wk
    if total and p >= 1:
        E.escreve(c, total, x + w + 24, y + h / 2 + 20, 56, "g", BR if escuro else TINTA, 1.0)


def montanha(c, cx, yb, w, h, a=1.0):
    p = skia.Path(); p.moveTo(cx - w / 2, yb); p.lineTo(cx, yb - h); p.lineTo(cx + w / 2, yb); p.close()
    c.drawPath(p, M.paint("#B9C2BF", a))
    n = skia.Path(); n.moveTo(cx, yb - h); n.lineTo(cx - w * 0.1, yb - h * 0.8); n.lineTo(cx, yb - h * 0.84); n.lineTo(cx + w * 0.1, yb - h * 0.8); n.close()
    c.drawPath(n, M.paint("#FFFFFF", a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: montanha(c, 1420, 860, 760, 600, a))
        E.frase(c, t, C["s01.a"], ps("no alto do Everest:", "i", 66, TINTA2), XE, 220, passo=0.1)
        E.frase(c, t, C["s01.a"] + 1.4, [("21%", "g", 120, CO)] + ps("de oxigênio", "i", 80), XE, 380, passo=0.12)
        E.foco(c, t, C["s01.a"] + 2.4, 0.4, lambda a: E.escreve(c, "o mesmo da praia", XE, 470, 56, "i", TINTA2, a))
        E.frase(c, t, C["s01.b"], ps("e falta ar", "i", 70), XE, 630, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("não é a porcentagem:", "i", 66, TINTA2), XE, 800, passo=0.1)
        E.frase(c, t, C["s01.d"], [("é a pressão", "g", 90, COR)], XE, 930)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("pressão", "g", 70), ("parcial", "g", 70, COR)]),
                 (C["s02.c"], [("o", "i", 74), ("oxigênio", "g", 70), ("no", "i", 74), ("ar", "g", 70)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("porcentagem", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03.a"] - 0.6, ps("você precisa de", "i", 80) + [("duas coisas", "g", 76, COR)], XE, 200, passo=0.12)
    y = [430, 760]
    for i, k in enumerate(("s03.b", "s03.c")):
        E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, XE + 40, y[i] - 30, 44, a=a), centro(c, str(i + 1), XE + 40, y[i] - 8, 54, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, [("PV = nRT", "g", 66, COR)], XE + 110, y[0])
    E.frase(c, t, C["s03.c"] + 0.1, ps("porcentagem pelo decimal", "i", 66), XE + 110, y[1], passo=0.1)
    E.formula_em(c, t, C["s03.c"] + 1.0, "21% de 1 = 0,21 × 1", XE + 900, y[1] + 4, 66, "g", TINTA2)


# ---------------- mistura ----------------
def b_mistura(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("o ar é uma", "i", 80) + [("mistura", "g", 76, COR)], XE, 220, passo=0.12)
        E.pizza(c, t, C["s04.b"], [("nitrogênio", 78), ("oxigênio", 21), ("argônio", 1)], 1350, 600, 280, cores=[CN, CO, CHE], destaque=(1,), size=46)
        for k, (n, s, tk, cor) in enumerate((("78%", "nitrogênio", "s04.b", CN), ("21%", "oxigênio", "s04.c", CO), ("~1%", "quase todo argônio", "s04.d", CHE))):
            E.frase(c, t, C[tk], [(n, "g", 84, cor)] + ps(s, "i", 66), XE, 420 + k * 170, passo=0.12)
        return
    E.frase(c, t, C["s05.a"], ps("cada gás bate como se estivesse", "i", 64) + [("sozinho", "g", 60, COR)], XE, 220, passo=0.1)
    cilindro(c, t, XE + 20, 760, 420, 380, 30, embolo=False, tipos=[("O", 0.3), ("N", 0.7)], r=12)
    E.foco(c, t, C["s05.b"], 0.5, lambda a: cilindro(c, t, 760, 760, 300, 380, 9, embolo=False, tipos=[("O", 1.0)], r=12, a=a, rotulo="só o oxigênio"))
    E.frase(c, t, C["s05.b"], [("pressão parcial", "g", 62, COR)], 1180, 420)
    E.frase(c, t, C["s05.b"] + 0.8, ps("a que ele faria sozinho", "i", 58, TINTA2), 1180, 500, passo=0.1)
    E.frase(c, t, C["s05.c"], [("total", "g", 62), ("=", "g", 62, TINTA2)] + ps("soma das parciais", "i", 64), 1180, 680, passo=0.1)
    pilula_em(c, t, C["s05.d"], "lei de Dalton", 1400, 820, 52, E.COR)
    E.foco(c, t, C["s05.d"] + 0.4, 0.4, lambda a: centro(c, "o mesmo Dalton do modelo do átomo", 1400, 920, 44, "i", TINTA2, a))


# ---------------- fração em mols ----------------
def b_fracao(c, t, C, b):
    E.frase(c, t, C["s06.a"], ps("quanto da pressão é de cada gás?", "i", 72), XE, 220, passo=0.12)
    E.frase(c, t, C["s06.b"], [("PV = nRT", "g", 62)] + ps("com V e T iguais:", "i", 62, TINTA2), XE, 360, passo=0.1)
    E.frase(c, t, C["s06.c"], [("P", "g", 70, COR)] + ps("proporcional a", "i", 70) + [("n", "g", 70, COR)], XE, 480, passo=0.12)
    E.frase(c, t, C["s06.d"], ps("cada gás fica com a sua", "i", 66) + [("fração dos mols", "g", 62, COR)], XE, 620, passo=0.1)
    if t >= C["s07"]:
        E.foco(c, t, C["s07.a"], 0.5, lambda a: (E.escreve(c, "fração =", XE, 860, 80, "g", TINTA, a), E.fracao(c, "mols do gás", "mols no total", XE + 640, 830, 56, TINTA, a)))
        E.foco(c, t, C["s07.b"], 0.5, lambda a: E.formula(c, "parcial = fração × total", 1100, 860, 72, "g", COR, a))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], [("2 mol", "g", 64, CO)] + ps("de oxigênio e", "i", 66) + [("8 mol", "g", 64, CN)] + ps("de nitrogênio", "i", 66), XE, 220, passo=0.1)
        E.frase(c, t, C["s08.b"], ps("a", "i", 66) + [("10 atm", "g", 64, COR)], XE, 320, passo=0.1)
        cilindro(c, t, 1420, 640, 340, 300, 30, embolo=False, tipos=[("O", 0.2), ("N", 0.8)], r=11)
        E.formula_em(c, t, C["s08.c"], "total: 10 mol", XE, 470, 70, "g", TINTA2)
        E.formula_em(c, t, C["s08.d"], "oxigênio: f{2}{10} =", XE, 610, 70, "g", TINTA)
        E.formula_em(c, t, C["s08.e"], "0,2", XE + 640, 610, 80, "g", CO)
        E.formula_em(c, t, C["s08.f"], "0,2 × 10 = 2 atm", XE, 740, 80, "g", TINTA)
        barra_pressao(c, t, C["s08.f"] + 0.6, XE, 850, 1400, 110, [(CO, 0.2, "2 atm"), (CN, 0.8, "8 atm" if t >= C["s08.g"] else "")], total="10 atm")
        return
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], ps("no ar, a porcentagem vem em", "i", 64) + [("volume", "g", 60)], XE, 220, passo=0.1)
        E.frase(c, t, C["s09.b"], ps("volume de gás também é proporcional aos mols", "i", 58, TINTA2), XE, 320, passo=0.08)
        E.frase(c, t, C["s09.c"], [("% em volume", "g", 64), ("=", "g", 64, TINTA2), ("% em mols", "g", 64, COR)], XE, 440, passo=0.12)
        E.frase(c, t, C["s09.d"], ps("ao nível do mar:", "i", 64) + [("1 atm", "g", 62, COR)], XE, 580, passo=0.1)
        E.formula_em(c, t, C["s09.e"], "0,21 × 1 = 0,21 atm de oxigênio", XE, 710, 76, "g", TINTA)
        barra_pressao(c, t, C["s09.d"] + 0.4, XE, 820, 1400, 110, [(CO, 0.21, "0,21"), (CN, 0.78, "0,78"), (CHE, 0.01, "")], total="1 atm")
        return
    E.foco(c, t, C["s10.a"], 0.5, lambda a: montanha(c, 1620, 760, 480, 380, a))
    E.frase(c, t, C["s10.a"], ps("no Everest:", "i", 66), XE, 220, passo=0.1)
    E.formula_em(c, t, C["s10.a"] + 0.8, "total ≈ f{1}{3} atm", XE + 380, 225, 70, "g", COR)
    barra_pressao(c, t, C["s10"], XE, 380, 800, 100, [(CO, 0.21, "oxigênio"), (CN, 0.78, "nitrogênio"), (CHE, 0.01, "")], total="praia: 1 atm")
    barra_pressao(c, t, C["s10.b"], XE, 560, 267, 100, [(CO, 0.21, ""), (CN, 0.78, ""), (CHE, 0.01, "")], total="Everest: 1/3 atm")
    E.frase(c, t, C["s10.b"] + 0.6, ps("o oxigênio continua", "i", 62) + [("21%", "g", 58, CO)], XE, 760, passo=0.1)
    E.frase(c, t, C["s10.d"], ps("pressão do oxigênio:", "i", 62) + [("um terço da praia", "g", 58, COR)], XE, 860, passo=0.1)
    E.frase(c, t, C["s10.e"], ps("menos oxigênio a cada respiração", "i", 58, TINTA2), XE, 960, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("usar a fração das massas", "i", 72), XE + 450, 190, passo=0.12)
    E.frase(c, t, C["s11.b"], [("32 g", "g", 70, CO)] + ps("de oxigênio +", "i", 66) + [("4 g", "g", 70, CHE)] + ps("de hélio", "i", 66), XE, 360, passo=0.1)
    E.formula_em(c, t, C["s11.b"] + 2.0, "pela massa: f{32}{36} ≈ 89%", XE, 520, 76, "g", ERRADO)
    if t >= C["s11.c"]:
        E.risco(c, XE - 10, 545, XE + 900, 465, t, C["s11.c"], largura=11)
    E.formula_em(c, t, C["s11.c"] + 0.3, "1 mol + 1 mol", XE, 700, 84, "g", TINTA)
    barra_pressao(c, t, C["s11.d"], XE, 760, 1200, 100, [(CO, 0.5, "metade"), (CHE, 0.5, "metade")])
    E.frase(c, t, C["s11.e"], ps("antes da fração,", "i", 64) + [("massas em mols", "g", 60, COR)], XE, 980, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"], ps("o atalho: parcial =", "i", 70, CLARO) + [("% do total", "g", 66, BR)], W / 2, 200, "center", 0.12)
        E.frase(c, t, C["s12.b"], [("20%", "g", 70, E.CLARO)] + ps("de oxigênio a", "i", 70, CLARO) + [("5 atm", "g", 70, BR)], W / 2, 380, "center", 0.12)
        E.formula_em(c, t, C["s12.c"], "10% de 5 = 0,5", W / 2, 560, 96, "g", BR, "center")
        E.formula_em(c, t, C["s12.d"], "20% de 5 =", W / 2 - 80, 740, 96, "g", BR, "center")
        bola_txt(c, t, C["s12.d"] + 0.8, "1 atm", W / 2 + 380, 710, 100, 60)
        return
    E.frase(c, t, C["s13.a"], ps("a pressão se divide como os", "i", 70, CLARO) + [("mols", "g", 66, BR)], W / 2, 260, "center", 0.12)
    E.frase(c, t, C["s13.b"], ps("confira:", "i", 70, CLARO) + [("parciais somadas = total", "g", 66, E.CLARO)], W / 2, 440, "center", 0.12)
    E.frase(c, t, C["s13.c"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("porcentagem em massa", "i", 66, CLARO), W / 2, 660, "center", 0.12)
    pilula_em(c, t, C["s13.c"] + 1.8, "passe para mols primeiro", W / 2, 820, 54, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s14.a"], ps("cilindro de mergulho:", "i", 66, TINTA2), XE, 320, passo=0.1)
    E.frase(c, t, C["s14.a"] + 1.0, [("1 mol", "g", 70, CO)] + ps("de oxigênio e", "i", 70) + [("3 mol", "g", 70, CHE)] + ps("de hélio", "i", 70), XE, 440, passo=0.1)
    E.frase(c, t, C["s14.b"], ps("a", "i", 70) + [("8 atm", "g", 70, COR)], XE, 560, passo=0.1)
    E.frase(c, t, C["s14.c"], ps("qual é a pressão parcial de", "i", 66) + [("cada gás?", "g", 62, COR)], XE, 720, passo=0.1)
    if t < C["s15"]:
        E.foco(c, t, C["s14.a"] + 0.5, 0.5, lambda a: cilindro(c, t, 1440, 800, 320, 420, 24, embolo=False, tipos=[("O", 0.25), ("He", 0.75)], r=12, a=a))
    else:
        E.relogio(c, t, C["s15.a"], cx=1560, cy=480, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s16.a"], "total: 1 + 3 = 4 mol", XE, 240, 76, "g", TINTA2)
    E.formula_em(c, t, C["s16.b"], "oxigênio: f{1}{4} × 8 =", XE, 420, 80, "g", TINTA)
    bola_txt(c, t, C["s16.c"], "2 atm", XE + 980, 395, 80, 50, CERTO)
    E.formula_em(c, t, C["s16.d"], "hélio: f{3}{4} × 8 =", XE, 600, 80, "g", TINTA)
    bola_txt(c, t, C["s16.e"], "6 atm", XE + 980, 575, 80, 50, CERTO)
    barra_pressao(c, t, C["s16.f"], XE, 780, 1400, 110, [(CO, 0.25, "2 atm"), (CHE, 0.75, "6 atm")], total="8 atm")
    E.foco(c, t, C["s16.f"] + 1.0, 0.4, lambda a: E.formula(c, "2 + 6 = 8", XE, 1000, 66, "g", COR, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s17.a", ps("cada gás faz a sua", "i", 70) + [("pressão parcial", "g", 66, COR)]),
                 ("s17.b", [("parcial", "g", 66), ("=", "g", 66, TINTA2), ("fração em mols", "g", 66), ("×", "g", 66, TINTA2), ("total", "g", 66)]),
                 ("s17.c", ps("a soma das parciais dá o", "i", 70) + [("total", "g", 66, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s18.a"], ps("qual gás anda", "i", 80) + [("mais rápido?", "g", 76, COR)], XE, 420, passo=0.12)
    E.frase(c, t, C["s18.b"], ps("só pelas", "i", 70) + [("massas molares", "g", 66)], XE, 580, passo=0.12)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 780, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 805, p), ep(t, C["s18.c"] + 0.2, 0.4))
    E.frase(c, t, C["s18.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, mistura=b_mistura, fracao=b_fracao, exemplo=b_exemplo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
