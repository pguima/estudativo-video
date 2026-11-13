"""Visual — Estudativo · QUI-CAL-015: praticando o estudo dos gases (aula de prática, cinco questões).

Segue a linguagem dos gases (cabeçalho da QUI-CAL-010), a da trilha (QUI-CAL-001) e a da Química (QUI-MIS-001), e o formato da
prática da QUI-CAL-009: cabeça da questão (pílula "questão N" + a ferramenta), enunciado curto com o desenho à direita,
relógio na pausa e resolução com as peças das aulas (fatores da 011, 24,6 da 012, 22,4 L da 013, barra de pressões da 014,
raiz de Graham da 016). Resposta final na esfera verde."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-015_praticando_gases.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"
CO, CHE = Q.cor_el("O"), Q.cor_el("He")

# todas as contas da aula
assert abs(3 * 330 / 300 - 3.3) < 1e-9 and abs(3 * 1.1 - 3.3) < 1e-9 and 57 + 273 == 330
assert -63 + 273 == 210 and 210 / 300 == 0.7 and abs(10 * 4 * 0.7 - 28) < 1e-9 and abs(10 * (1 / 0.25) * (210 / 300) - 28) < 1e-9
assert abs(150 * 8.2 - 1230) < 1e-9 and abs(1230 / 24.6 - 50) < 1e-9 and 50 * 32 == 1600
assert 88 / 44 == 2 and abs(2 * 22.4 - 44.8) < 1e-9
assert 1 / 5 * 5 == 1 and 32 / 4 == 8 and abs(math.sqrt(8) - 2.83) < 0.01


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


def cabeca(c, t, t0, n, tema):
    E.foco(c, t, t0, 0.4, lambda a: (E.pilula(c, f"questão {n}", XE + 150, 170, 52, "g", fundo=E.COR, a=a),
                                     E.pilula(c, tema, XE + 520, 170, 44, "b", fundo="#5A5F66", a=a)))


def pneu(c, cx, cy, r, a=1.0):
    c.drawCircle(cx, cy, r, M.paint("#2A2B31", a))
    c.drawCircle(cx, cy, r * 0.55, M.paint("#9AA0A8", a))
    c.drawCircle(cx, cy, r * 0.2, M.paint("#2A2B31", a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    for k, s in enumerate(("pneu na estrada", "balão que sobe", "cilindro de hospital")):
        pilula_em(c, t, C["s01.a"] + 0.4 * k, s, XE + 260 + k * 560, 270, 52, "#5A5F66")
    E.frase(c, t, C["s01.b"], ps("a prova adora", "i", 80) + [("gás no dia a dia", "g", 76, COR)], XE, 480, passo=0.12)
    E.frase(c, t, C["s01.c"], [("5", "g", 140, COR)] + ps("questões", "i", 110), XE, 720, passo=0.15)
    E.frase(c, t, C["s01.d"], ps("com todas as ferramentas do módulo", "i", 64, TINTA2), XE, 860, passo=0.1)
    E.foco(c, t, C["s01.a"] + 0.4, 0.8, lambda a: E.simbolo(c, 1640, 720, 170 * ease_back(prog(t, C["s01.a"] + 0.4, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02.a"], [("as", "i", 84), ("ferramentas", "g", 80, COR)], XE, 170, passo=0.12)
    itens = (("s02.b", [("temperatura:", "i", 58), ("kelvin", "g", 56, COR)]),
             ("s02.c", [("antes e depois:", "i", 58), ("equação geral", "g", 56)]),
             ("s02.d", [("mols ou massa:", "i", 58), ("PV = nRT", "g", 56, COR)]),
             ("s02.e", [("CNTP:", "i", 58), ("22,4 L por mol", "g", 56)]),
             ("s02.f", [("mistura:", "i", 58), ("fração em mols × total", "g", 56, COR)]),
             ("s02.g", [("difusão:", "i", 58), ("o mais leve ganha", "g", 56)]))
    for i, (k, partes) in enumerate(itens):
        y = 310 + i * 115
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 36, y - 22, 36, a=a), centro(c, str(i + 1), XE + 36, y - 4, 44, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, XE + 100, y, passo=0.1)
    E.frase(c, t, C["s02.g"] + 2.0, ps("pause e tente antes de cada resposta", "i", 54, TINTA2), XE, 1020, passo=0.1)


# ---------------- questão 1: pneu ----------------
def b_q1(c, t, C, b):
    cabeca(c, t, C["s03.a"], 1, "isocórica")
    E.frase(c, t, C["s03.b"], ps("o ar do pneu:", "i", 66) + [("3 atm", "g", 64, COR), ("e", "i", 66), ("27 °C", "g", 64, COR)], XE, 360, passo=0.1)
    E.frase(c, t, C["s03.c"], ps("depois da viagem:", "i", 66) + [("57 °C", "g", 64, QUENTE)], XE, 490, passo=0.1)
    E.frase(c, t, C["s03.d"], ps("o volume quase não muda", "i", 60, TINTA2), XE, 610, passo=0.1)
    E.frase(c, t, C["s03.e"], ps("qual é a", "i", 70) + [("nova pressão?", "g", 66, COR)], XE, 780, passo=0.1)
    if t < C["s04"]:
        E.foco(c, t, C["s03.b"], 0.5, lambda a: pneu(c, 1500, 520, 220, a))
    else:
        E.relogio(c, t, C["s04.a"], cx=1500, cy=480, r=180)


def b_q1r(c, t, C, b):
    cabeca(c, t, C["s05"], 1, "isocórica")
    pilula_em(c, t, C["s05.a"], "V fixo", XE + 140, 330, 52, "#8A8F96")
    E.formula_em(c, t, C["s05.b"], "f{P}{T} = constante", XE + 420, 345, 72, "g", COR)
    E.formula_em(c, t, C["s05.c"], "300 K → 330 K", XE, 560, 90, "g", TINTA)
    pilula_em(c, t, C["s05.d"], "um décimo a mais", XE + 900, 530, 48, E.COR)
    E.formula_em(c, t, C["s05.f"], "3 × 1,1 =", XE, 800, 96, "g", TINTA2)
    bola_txt(c, t, C["s05.f"] + 1.0, "3,3 atm", XE + 700, 770, 110, 54, CERTO)


# ---------------- questão 2: balão ----------------
def b_q2(c, t, C, b):
    cabeca(c, t, C["s06.a"], 2, "equação geral")
    E.frase(c, t, C["s06.b"], ps("balão meteorológico:", "i", 64) + [("10 L", "g", 62, COR)], XE, 330, passo=0.1)
    E.frase(c, t, C["s06.c"], [("1 atm", "g", 62), ("e", "i", 64), ("27 °C", "g", 62)], XE, 440, passo=0.1)
    E.frase(c, t, C["s06.d"], ps("lá no alto:", "i", 64) + [("¼ atm", "g", 62, COR)], XE, 580, passo=0.1)
    E.frase(c, t, C["s06.e"], ps("e", "i", 64) + [("−63 °C", "g", 62, FRIO)], XE + 560, 580, passo=0.1)
    E.frase(c, t, C["s06.f"], ps("qual é o", "i", 70) + [("volume lá em cima?", "g", 66, COR)], XE, 760, passo=0.1)
    if t < C["s07"]:
        k = ease_io(prog(t, C["s06.d"], 2.0))
        E.foco(c, t, C["s06.b"], 0.5, lambda a: balao(c, t, t, 1500, lerp(640, 420, k), lerp(110, 190, k), lerp(130, 220, k), 20, a=a))
    else:
        E.relogio(c, t, C["s07.a"], cx=1500, cy=480, r=180)


def b_q2r(c, t, C, b):
    cabeca(c, t, C["s08"], 2, "equação geral")
    E.frase(c, t, C["s08.a"], ps("pelos", "i", 70) + [("fatores", "g", 66, COR)], XE, 320, passo=0.1)
    E.frase(c, t, C["s08.b"], [("P ÷ 4", "g", 66), ("→", "g", 66, TINTA2), ("V × 4", "g", 66, COR)], XE, 460, passo=0.12)
    E.frase(c, t, C["s08.c"], [("300 K → 210 K", "g", 66)], XE, 590, passo=0.12)
    E.formula_em(c, t, C["s08.d"], "f{210}{300} = 0,7", XE + 700, 600, 70, "g", COR)
    E.formula_em(c, t, C["s08.e"], "10 × 4 × 0,7 =", XE, 830, 96, "g", TINTA2)
    bola_txt(c, t, C["s08.e"] + 1.4, "28 L", XE + 920, 800, 100, 70, CERTO)


# ---------------- questão 3: cilindro ----------------
def b_q3(c, t, C, b):
    cabeca(c, t, C["s09.a"], 3, "PV = nRT")
    E.frase(c, t, C["s09.b"], ps("cilindro de hospital:", "i", 64) + [("8,2 L", "g", 62, COR)], XE, 330, passo=0.1)
    E.frase(c, t, C["s09.c"], [("150 atm", "g", 62, COR), ("e", "i", 64), ("27 °C", "g", 62, COR)], XE, 450, passo=0.1)
    E.frase(c, t, C["s09.d"], [("R = 0,082", "g", 62)], XE, 580)
    E.frase(c, t, C["s09.e"], ps("quantos", "i", 70) + [("quilos", "g", 66, COR)] + ps("de oxigênio?", "i", 70), XE, 760, passo=0.1)
    if t < C["s10"]:
        E.foco(c, t, C["s09.b"], 0.5, lambda a: _tanque(c, t, 1500, 560, 220, 520, a))
    else:
        E.relogio(c, t, C["s10.a"], cx=1500, cy=480, r=180)


def _tanque(c, t, cx, cy, w, h, a):
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), w / 2, w / 2)
    c.drawRRect(r, M.paint("#E3E6EA", a))
    c.save(); c.clipRRect(r, doAntiAlias=True)
    Q.particulas(c, t, cx - w / 2 + 10, cy - h / 2 + 30, w - 20, h - 60, 40, "gas", tipos=[("O", 1.0)], r=11, semente=4, a=a)
    c.restore()
    c.drawRRect(r, M.paint("#6B7078", a, stroke=7))
    M.rrect(c, cx - 30, cy - h / 2 - 60, 60, 64, 10, "#6B7078", a)
    M.rrect(c, cx - 70, cy - h / 2 - 80, 140, 28, 10, E.COR, a)


def b_q3r(c, t, C, b):
    cabeca(c, t, C["s11"], 3, "PV = nRT")
    E.formula_em(c, t, C["s11.a"], "300 K: RT = 24,6", XE, 320, 76, "g", TINTA2)
    E.formula_em(c, t, C["s11.b"], "PV = 150 × 8,2 = 1.230", XE, 470, 80, "g", TINTA)
    E.formula_em(c, t, C["s11.c"], "n = 1.230 ÷ 24,6 = 50 mol", XE, 620, 80, "g", TINTA)
    E.formula_em(c, t, C["s11.d"], "50 × 32 = 1.600 g", XE, 800, 90, "g", TINTA2)
    bola_txt(c, t, C["s11.e"], "1,6 kg", XE + 1240, 770, 110, 60, CERTO)


# ---------------- questão 4: CNTP ----------------
def b_q4(c, t, C, b):
    cabeca(c, t, C["s12.a"], 4, "volume molar")
    E.frase(c, t, C["s12.b"], ps("um extintor libera", "i", 66) + [("88 g", "g", 64, COR)] + ps("de gás carbônico", "i", 66), XE, 360, passo=0.1)
    E.foco(c, t, C["s12.b"] + 1.6, 0.4, lambda a: (Q.formula(c, "CO2", XE, 490, 80, TINTA, a), E.formula(c, "M = 44 g/mol", XE + 220, 490, 64, "g", TINTA2, a)))
    E.frase(c, t, C["s12.c"], ps("que volume ocupa nas", "i", 70) + [("CNTP?", "g", 66, COR)], XE, 680, passo=0.1)
    if t < C["s13"]:
        Q.molecula(c, t, C["s12.b"] + 0.4, "CO2", 1500, 480, 150, passo=0.15)
    else:
        E.relogio(c, t, C["s13.a"], cx=1500, cy=480, r=180)


def b_q4r(c, t, C, b):
    cabeca(c, t, C["s14"], 4, "volume molar")
    E.formula_em(c, t, C["s14.a"], "88 ÷ 44 = 2 mol", XE, 400, 96, "g", TINTA)
    E.formula_em(c, t, C["s14.b"], "2 × 22,4 =", XE, 640, 96, "g", TINTA2)
    bola_txt(c, t, C["s14.c"], "44,8 L", XE + 760, 610, 110, 60, CERTO)
    pilula_em(c, t, C["s14.c"] + 0.6, "CNTP: 0 °C e 1 atm", XE + 300, 860, 50, TINTA)


# ---------------- questão 5: mistura e difusão ----------------
def b_q5(c, t, C, b):
    cabeca(c, t, C["s15.a"], 5, "mistura e difusão")
    E.frase(c, t, C["s15.b"], ps("mergulho:", "i", 64) + [("1 mol", "g", 62, CO)] + ps("de oxigênio para", "i", 64) + [("4 mol", "g", 62, CHE)] + ps("de hélio", "i", 64), XE, 360, passo=0.08)
    E.frase(c, t, C["s15.c"], ps("a", "i", 66) + [("5 atm", "g", 64, COR)], XE, 480, passo=0.1)
    E.frase(c, t, C["s15.d"], [("1", "g", 56, COR)] + ps("pressão parcial do oxigênio?", "i", 62), XE, 640, passo=0.1)
    E.frase(c, t, C["s15.e"], [("2", "g", 56, COR)] + ps("num vazamento, quem escapa mais rápido?", "i", 62), XE, 760, passo=0.08)
    if t < C["s16"]:
        E.foco(c, t, C["s15.b"] + 0.4, 0.5, lambda a: cilindro(c, t, 1440, 860, 320, 380, 25, embolo=False, tipos=[("O", 0.2), ("He", 0.8)], r=12, a=a))
    else:
        E.relogio(c, t, C["s16.a"], cx=1640, cy=560, r=140)


def b_q5r(c, t, C, b):
    cabeca(c, t, C["s17"], 5, "mistura e difusão")
    E.formula_em(c, t, C["s17.a"], "oxigênio: 1 de 5 mols", XE, 330, 76, "g", TINTA2)
    E.formula_em(c, t, C["s17.b"], "f{1}{5} × 5 =", XE, 480, 90, "g", TINTA)
    bola_txt(c, t, C["s17.b"] + 0.8, "1 atm", XE + 640, 450, 90, 54, CERTO)
    E.frase(c, t, C["s17.c"], ps("no vazamento, ganha o", "i", 64) + [("mais leve", "g", 60, COR)], XE, 680, passo=0.1)
    E.frase(c, t, C["s17.d"], [("hélio", "g", 62, CHE), ("M = 4", "g", 58)] + ps("contra", "i", 62) + [("oxigênio", "g", 62, CO), ("M = 32", "g", 58)], XE, 790, passo=0.1)
    E.formula_em(c, t, C["s17.e"], "r{f{32}{4}} = r{8} ≈ 2,8", XE, 960, 84, "g", TINTA)
    E.foco(c, t, C["s17.e"] + 2.0, 0.4, lambda a: E.pilula(c, "quase 3 vezes mais rápido", 1480, 930, 46, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s19"]:
        E.frase(c, t, C["s18.a"], ps("cinco problemas,", "i", 84) + [("uma lista de conferência", "g", 74, COR)], W / 2, 200, "center", 0.1)
        for i, (k, s) in enumerate((("s18.b", "kelvin"), ("s18.c", "as unidades do R"), ("s18.d", "o que fica parado"))):
            y = 400 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: E.selo(c, 340, y - 26, 44, True, a))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 66)], 420, y)
        E.frase(c, t, C["s18.e"], ps("fim do estudo dos gases e da trilha de", "i", 56, TINTA2) + [("mol, estequiometria e gases", "g", 52, COR)], W / 2, 1000, "center", 0.08)
        return
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.pilula(c, "Inscreva-se", W / 2, 460, 90, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.a"] + 0.3, 0.8))
    E.cursor(c, lerp(1300, 1140, p), lerp(760, 490, p), ep(t, C["s19.a"] + 0.2, 0.4))
    E.frase(c, t, C["s19.b"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], W / 2, 800, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, q1r=b_q1r, q2=b_q2, q2r=b_q2r, q3=b_q3, q3r=b_q3r, q4=b_q4, q4r=b_q4r,
              q5=b_q5, q5r=b_q5r, fim=b_fim)
