"""Visual — Estudativo · QUI-CAL-010: pressão, volume e temperatura: a escala Kelvin. Primeira aula do módulo Estudo dos gases.

Segue a linguagem da Química (cabeçalho da QUI-MIS-001) e a da trilha (QUI-CAL-001). Acrescenta a LINGUAGEM DOS GASES
(vale de QUI-CAL-010 a 016 e na 015):
- GÁS = partículas voando dentro do recipiente (Q.particulas, estado "gas"), em turquesa quando não importa qual é o gás e nas
  cores CPK quando importa. O recipiente padrão é o CILINDRO COM ÊMBOLO (cilindro): o êmbolo cinza marca o volume.
- TEMPERATURA = velocidade das bolinhas. A velocidade muda sem pulo com fase(t, [(instante, velocidade)]). Quente = laranja
  QUENTE, frio = azul FRIO (o mesmo azul do elétron), sempre também com o termômetro (termometro) e o número em kelvin.
- PRESSÃO = choques na parede: setas curtas saindo das paredes (setas_parede) e o mostrador (manometro) com o ponteiro turquesa.
- VOLUME em litros, ao lado do recipiente. As letras P, V, T e n vão na grotesca; a variável que muda fica na cor da matéria
  e a que fica parada leva a pílula cinza "fixo". Frações com índice (P₁V₁/T₁) com frac_q.
- KELVIN: as duas réguas lado a lado (reguas_escalas), Celsius à esquerda e Kelvin à direita, com a seta "+ 273".
Peças candidatas ao kit quimica.py: cilindro(), termometro(), manometro(), fase(), frac_q(), balao(), setas_parede(),
reguas_escalas() e torricelli()."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-010_pressao_volume_temperatura_kelvin.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pressao", "temperatura", "kelvin", "unidades", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 27 + 273 == 300 and 0 + 273 == 273 and 20 + 273 == 293 and 40 + 273 == 313 and 313 < 2 * 293
assert 380 / 760 == 0.5 and -23 + 273 == 250 and 1520 / 760 == 2 and (40 + 273) - (20 + 273) == 20


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


def setas_parede(c, t, t0, cx, cy, rx, ry, n=10, a=1.0, cor=None):
    """setas curtas saindo da parede: os empurrões das partículas viram força"""
    q = ep(t, t0, 0.4) * a
    if q <= 0:
        return
    for k in range(n):
        ang = k / n * math.tau + 0.3
        pul = 0.5 + 0.5 * math.sin(t * 6 + k * 1.7)
        x0, y0 = cx + rx * math.cos(ang), cy + ry * math.sin(ang)
        L = 34 + 26 * pul
        M.arrow(c, x0, y0, x0 + L * math.cos(ang), y0 + L * math.sin(ang), cor or E.COR, q, 5, 14)


def reguas_escalas(c, t, t0, x, y0, y1, marcas, a=1.0):
    """duas réguas: Celsius à esquerda, Kelvin à direita; marcas = [(°C, instante)]; a altura é proporcional à temperatura"""
    q = ep(t, t0, 0.4) * a
    if q <= 0:
        return lambda v: 0
    vmin, vmax = -273, 120
    Y = lambda v: lerp(y1, y0, (v - vmin) / (vmax - vmin))
    for xx, nome in ((x, "°C"), (x + 420, "K")):
        M.line(c, xx, y0 - 20, xx, y1 + 10, TINTA, q, 6)
        centro(c, nome, xx, y0 - 50, 56, "g", COR, q)
    for v, ti in marcas:
        p = ep(t, ti, 0.4) * a
        if p <= 0:
            continue
        yy = Y(v)
        M.line(c, x - 22, yy, x + 22, yy, TINTA, p, 5)
        M.line(c, x + 420 - 22, yy, x + 420 + 22, yy, TINTA, p, 5)
        E.formula(c, f"{v}".replace("-", "−"), x - 40, yy + 20, 54, "g", TINTA, p, "right")
        E.formula(c, f"{v + 273}", x + 420 + 40, yy + 20, 54, "g", COR, p)
        M.line(c, x + 40, yy, x + 380, yy, FIO, p, 3, dash=[10, 10])
    return Y


def torricelli(c, t, t0, cx, yb, a=1.0):
    """o tubo de Torricelli: bacia de mercúrio, tubo virado e a coluna de 76 cm"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    HG = "#A9B0B8"
    M.rrect(c, cx - 230, yb - 90, 460, 90, 20, HG, q)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 240, yb - 130, 480, 140), 24, 24), M.paint(Q.VIDRO, q, stroke=5))
    hcol = 460 * ease_out(prog(t, t0 + 0.5, 1.2))
    M.rrect(c, cx - 30, yb - 90 - hcol, 60, hcol + 40, 10, HG, q)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 36, yb - 640, 72, 600), 30, 30), M.paint(Q.VIDRO, q, stroke=5))
    for dx in (-170, 170):
        M.arrow(c, cx + dx, yb - 300, cx + dx, yb - 150, E.COR, q, 6, 18)
    centro(c, "ar", cx - 170, yb - 320, 44, "i", TINTA2, q)
    centro(c, "ar", cx + 170, yb - 320, 44, "i", TINTA2, q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        tb = C["s01.b"]
        enc = ease_io(prog(t, tb, 2.0))
        tt = fase(t, [(tb, 1.0), (tb + 2.0, 0.35)])
        # o congelador
        E.foco(c, t, tb - 0.4, 0.5, lambda a: (M.rrect(c, 1080, 220, 640, 640, 30, "#D8ECF7", a),
                                              c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1080, 220, 640, 640), 30, 30), M.paint("#8FB8D0", a, stroke=6)),
                                              centro(c, "congelador", 1400, 920, 50, "i", TINTA2, a)))
        xb = lerp(600, 1400, ease_io(prog(t, tb - 0.6, 0.8)))
        E.foco(c, t, C["s01.a"], 0.5, lambda a: balao(c, t, tt, xb, 480, lerp(220, 175, enc), lerp(260, 205, enc), 34, a=a))
        E.frase(c, t, C["s01.a"], ps("encha um balão", "i", 70), XE, 200, passo=0.1)
        E.frase(c, t, C["s01.c"], [("nenhum ar saiu", "g", 64, COR)], XE, 860)
        E.frase(c, t, C["s01.d"], ps("mudou a", "i", 66) + [("temperatura", "g", 62)] + ps("e o", "i", 66) + [("volume", "g", 62, COR)], XE, 980, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("pressão", "g", 70, COR), ("pelas", "i", 74), ("partículas", "g", 70)]),
                 (C["s02.c"], [("°C", "g", 70), ("→", "g", 70, TINTA2), ("kelvin", "g", 70, COR)]),
                 (C["s02.d"], [("mmHg", "g", 70), ("→", "g", 70, TINTA2), ("atm", "g", 70, COR)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03.a"] - 0.6, ps("você precisa de", "i", 80) + [("três coisas", "g", 76, COR)], XE, 200, passo=0.12)
    y = [400, 640, 880]
    for i, k in enumerate(("s03.b", "s03.c", "s03.d")):
        E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, XE + 40, y[i] - 30, 44, a=a), centro(c, str(i + 1), XE + 40, y[i] - 8, 54, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, ps("gás: partículas soltas, rápidas no quente", "i", 62), XE + 110, y[0], passo=0.08)
    E.foco(c, t, C["s03.b"] + 0.4, 0.4, lambda a: cilindro(c, t, 1440, 470, 300, 230, 18, embolo=False, a=a))
    E.frase(c, t, C["s03.c"] + 0.1, ps("pressão =", "i", 66), XE + 110, y[1])
    E.formula_em(c, t, C["s03.c"] + 0.6, "p = f{F}{A}", XE + 420, y[1] + 8, 80, "g", COR)
    E.frase(c, t, C["s03.d"] + 0.1, [("1 L", "g", 66, COR), ("=", "g", 66, TINTA2), ("1 dm³", "g", 66)], XE + 110, y[2], passo=0.12)


# ---------------- pressão ----------------
def b_pressao(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("bilhões de trilhões de partículas", "i", 64), XE, 200, passo=0.1)
        balao(c, t, t * 1.2, 1300, 560, 300, 330, 46)
        E.frase(c, t, C["s04.b"], ps("batem na parede e voltam", "i", 64, TINTA2), XE, 360, passo=0.1)
        E.frase(c, t, C["s04.c"], [("cada batida", "g", 62)] + ps("é um empurrão", "i", 66), XE, 560, passo=0.1)
        setas_parede(c, t, C["s04.d"], 1300, 560, 300, 330, 14)
        E.frase(c, t, C["s04.d"], [("somados:", "i", 66), ("força", "g", 66, COR)] + ps("na parede", "i", 66), XE, 760, passo=0.1)
        return
    E.frase(c, t, C["s05.a"], [("pressão", "g", 80, COR), ("=", "g", 80, TINTA2)], XE, 230, passo=0.12)
    E.formula_em(c, t, C["s05.a"] + 0.6, "f{força}{área}", XE + 480, 230, 70, "g", TINTA)
    E.frase(c, t, C["s05.b"], ps("mais batidas ou batidas mais fortes:", "i", 60, TINTA2), XE, 420, passo=0.1)
    E.frase(c, t, C["s05.c"], [("mais pressão", "g", 62, COR)], XE + 1000, 420)
    for k, (n, rot, tk) in enumerate(((8, "pneu vazio", "s05.d"), (34, "pneu cheio", "s05.e"))):
        x = 420 + 680 * k
        E.foco(c, t, C[tk], 0.5, lambda a, n=n, x=x, rot=rot: (cilindro(c, t, x, 900, 380, 300, n, embolo=False, a=a, rotulo=rot)))
        E.foco(c, t, C[tk] + 0.4, 0.4, lambda a, x=x, k=k: manometro(c, x + 540, 700, 110, 0.6 + 2.4 * k, 4, a))


# ---------------- volume ----------------
def b_volume(c, t, C, b):
    E.frase(c, t, C["s06.a"], [("volume", "g", 80, COR), ("=", "g", 80, TINTA2)] + ps("o espaço que o gás ocupa", "i", 72), XE, 220, passo=0.12)
    E.frase(c, t, C["s06.b"], ps("o gás não tem volume próprio:", "i", 60, TINTA2), XE, 340, passo=0.1)
    E.frase(c, t, C["s06.c"], ps("ocupa o recipiente inteiro", "i", 60) , XE + 880, 340, passo=0.1)
    E.foco(c, t, C["s06.b"] + 0.4, 0.5, lambda a: cilindro(c, t, XE + 40, 800, 260, 340, 22, embolo=False, a=a))
    E.foco(c, t, C["s06.c"] + 0.3, 0.5, lambda a: cilindro(c, t + 3, XE + 400, 800, 520, 170, 22, embolo=False, a=a, semente=9))
    E.frase(c, t, C["s06.d"], ps("nas contas, em", "i", 64) + [("litros", "g", 62, COR)], 1180, 520, passo=0.1)
    E.frase(c, t, C["s06.e"], [("1 m³", "g", 72), ("=", "g", 72, TINTA2), ("1.000 L", "g", 72, COR)], 1180, 680, passo=0.12)
    E.foco(c, t, C["s06.e"] + 0.8, 0.4, lambda a: E.escreve(c, "1 L = 1 dm³", 1180, 790, 56, "g", TINTA2, a))


# ---------------- temperatura ----------------
def b_temperatura(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], [("temperatura", "g", 80, COR), ("=", "g", 80, TINTA2), ("agitação", "i", 84)], XE, 210, passo=0.12)
        for k, (vel, cor, rot, tk, fr) in enumerate(((2.2, QUENTE, "quente: rápidas", "s07.b", 0.85), (0.35, FRIO, "frio: lentas", "s07.c", 0.2))):
            x = 220 + 740 * k
            E.foco(c, t, C[tk], 0.5, lambda a, x=x, vel=vel, cor=cor, rot=rot: cilindro(c, t, x, 760, 420, 380, 24, tt=t * vel, a=a, embolo=False,
                                                                                         tipos=[(cor, 1.0)], rotulo=rot))
            E.foco(c, t, C[tk] + 0.3, 0.4, lambda a, x=x, fr=fr: termometro(c, x + 520, 420, 300, fr, a))
        E.frase(c, t, C["s07.d"], ps("no congelador: lentas, batem com menos força", "i", 56, TINTA2), XE, 940, passo=0.08)
        E.frase(c, t, C["s07.e"], ps("e o ar de fora", "i", 56, TINTA2) + [("aperta o balão", "g", 54, COR)], XE, 1020, passo=0.08)
        return
    td = C["s08.a"]
    fr = lerp(0.6, 0.0, ease_io(prog(t, td, 2.6)))
    tt = fase(t, [(td, 1.2), (td + 2.6, 0.02)])
    E.frase(c, t, C["s08.a"], ps("esfrie cada vez mais", "i", 76), XE, 220, passo=0.12)
    cilindro(c, t, 1100, 860, 420, 420, 24, tt=tt, embolo=False, tipos=[(M.mix(QUENTE, FRIO, 1 - fr / 0.6 * 0.6), 1.0)])
    termometro(c, 1700, 400, 380, fr)
    E.formula_em(c, t, C["s08.b"], "−273 °C", XE, 520, 150, "g", FRIO)
    E.foco(c, t, C["s08.b"] + 0.6, 0.4, lambda a: E.escreve(c, "a agitação chegaria ao mínimo", XE, 620, 54, "i", TINTA2, a))
    E.frase(c, t, C["s08.c"], ps("mais frio que isso, não dá", "i", 64), XE, 790, passo=0.1)
    E.frase(c, t, C["s08.d"], [("zero", "g", 100, COR), ("absoluto", "g", 100, COR)], XE, 950, passo=0.15)


# ---------------- kelvin ----------------
def b_kelvin(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], ps("a escala", "i", 80) + [("Kelvin", "g", 76, COR)] + ps("começa ali", "i", 80), XE, 200, passo=0.12)
        reguas_escalas(c, t, C["s09.a"] + 0.6, 1100, 300, 980, [(-273, C["s09.b"]), (0, C["s09.c"]), (100, C["s09.c"] + 0.6)])
        E.frase(c, t, C["s09.b"], [("0 K", "g", 80, COR), ("=", "g", 80, TINTA2)] + ps("zero absoluto", "i", 80), XE, 420, passo=0.12)
        E.frase(c, t, C["s09.c"], ps("o grau tem o", "i", 66) + [("mesmo tamanho", "g", 62)], XE, 600, passo=0.1)
        E.foco(c, t, C["s09.d"], 0.5, lambda a: E.pilula(c, "+ 273", XE + 260, 800, 90, "g", fundo=E.COR, a=a))
        E.formula_em(c, t, C["s09.d"] + 0.6, "K = °C + 273", XE, 970, 80, "g", TINTA)
        return
    E.formula_em(c, t, C["s10.a"], "27 °C + 273 =", XE, 380, 110, "g", TINTA)
    bola_txt(c, t, C["s10.a"] + 1.6, "300 K", XE + 1080, 345, 110, 60)
    E.formula_em(c, t, C["s10.b"], "0 °C =", XE, 620, 110, "g", TINTA)
    bola_txt(c, t, C["s10.b"] + 0.8, "273 K", XE + 640, 585, 110, 60)
    pilula_em(c, t, C["s10.c"], "nas contas de gás: sempre kelvin", W / 2, 860, 60, TINTA)


# ---------------- unidades de pressão ----------------
def b_unidades(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], ps("a pressão em", "i", 76) + [("três unidades", "g", 72, COR)], XE, 200, passo=0.12)
        for k, (u, d, tk) in enumerate((("atm", "o ar ao nível do mar", "s11.b"), ("Pa", "newton por metro quadrado", "s11.c"), ("mmHg", "milímetro de mercúrio", "s11.e"))):
            y = 380 + 190 * k
            pilula_em(c, t, C[tk], u, XE + 160, y - 20, 70, E.COR)
            E.frase(c, t, C[tk] + 0.3, ps(d, "i", 60, TINTA2), XE + 380, y, passo=0.08)
        E.formula_em(c, t, C["s11.d"], "1 atm ≈ 10^{5} Pa", 1240, 590, 76, "g", COR)
        return
    torricelli(c, t, C["s12.a"], 1400, 960)
    E.foco(c, t, C["s12.a"] + 1.8, 0.4, lambda a: (M.line(c, 1500, 870, 1500, 410, TINTA, a, 4), E.escreve(c, "76 cm", 1520, 650, 54, "g", TINTA, a)))
    E.frase(c, t, C["s12.a"], ps("Torricelli:", "i", 70) + [("o ar segura", "g", 64)], XE, 220, passo=0.12)
    E.frase(c, t, C["s12.a"] + 1.6, ps("uma coluna de mercúrio", "i", 64, TINTA2), XE, 320, passo=0.1)
    E.formula_em(c, t, C["s12.b"], "760 mmHg", XE, 500, 110, "g", TINTA)
    E.formula_em(c, t, C["s12.c"], "1 atm = 760 mmHg", XE, 700, 96, "g", COR)
    E.formula_em(c, t, C["s12.d"], "mmHg ÷ 760 = atm", XE, 900, 80, "g", TINTA2)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], ps("a agitação acompanha o", "i", 64, TINTA2) + [("kelvin", "g", 60, COR)], XE, 170, passo=0.1)
    E.frase(c, t, C["s13.a"] - 0.4, [("cuidado", "g", 90, ERRADO)], XE, 290)
    E.frase(c, t, C["s13.a"], ps("dobrar o °C dobra a agitação?", "i", 66), XE + 420, 290, passo=0.1)
    E.formula_em(c, t, C["s13.b"], "20 °C → 40 °C", XE, 470, 96, "g", ERRADO)
    E.foco(c, t, C["s13.b"] + 1.0, 0.4, lambda a: E.escreve(c, "o dobro?", XE + 760, 465, 70, "g", ERRADO, a))
    if t >= C["s13.d"]:
        E.risco(c, XE + 740, 485, XE + 1060, 420, t, C["s13.d"], largura=10)
    E.formula_em(c, t, C["s13.c"], "293 K → 313 K", XE, 650, 96, "g", COR)
    for k, (v, tk) in enumerate(((293, "s13.c"), (313, "s13.c"))):
        p = ease_out(prog(t, C[tk] + 0.6 + 0.4 * k, 0.7))
        if p > 0:
            M.rrect(c, XE, 720 + k * 90, 2.6 * v * p, 64, 14, E.COR if k else "#7FD8CB", 1.0)
            if p >= 1:
                E.formula(c, f"{v} K", XE + 2.6 * v + 20, 768 + k * 90, 50, "g", TINTA, 1.0)
    pilula_em(c, t, C["s13.d"] + 0.3, "bem menos que o dobro", 1500, 650, 46, TINTA)
    E.frase(c, t, C["s13.e"], ps("para comparar, só vale o", "i", 60) + [("kelvin", "g", 56, COR)], XE, 1000, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s14.a"], ps("o atalho: a", "i", 70, CLARO) + [("variação", "g", 66, BR)] + ps("é a mesma nas duas", "i", 70, CLARO), W / 2, 180, "center", 0.12)
    E.formula_em(c, t, C["s14.b"], "20 °C → 40 °C", 620, 400, 90, "g", BR, "center")
    pilula_em(c, t, C["s14.b"] + 0.6, "+ 20 °C", 620, 500, 54, E.COR)
    E.formula_em(c, t, C["s14.c"], "293 K → 313 K", 1300, 400, 90, "g", BR, "center")
    pilula_em(c, t, C["s14.c"] + 0.4, "+ 20 K", 1300, 500, 54, E.COR)
    E.formula_em(c, t, C["s14.d"], "(40 + 273) − (20 + 273) = 20", W / 2, 700, 80, "g", BR, "center")
    if t >= C["s14.e"]:
        q = ep(t, C["s14.e"], 0.4)
        for x0 in (W / 2 - 300, W / 2 + 60):
            M.line(c, x0, 690, x0 + 170, 650, E.CLARO, q, 6)
        E.foco(c, t, C["s14.e"] + 0.3, 0.4, lambda a: centro(c, "o 273 some na subtração", W / 2, 790, 54, "i", CLARO, a))
    E.frase(c, t, C["s14.f"], [("não", "g", 58, ERRADO), ("compensa:", "i", 62, CLARO)] + ps("pediu a temperatura? some 273", "i", 62, CLARO), W / 2, 960, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"], 0.6, lambda a: (c.drawPath(_monte(), M.paint("#B9C2BF", a)), c.drawPath(_neve(), M.paint("#FFFFFF", a))))
        E.foco(c, t, C["s15.a"] + 0.4, 0.4, lambda a: centro(c, "5.500 m", 1500, 300, 50, "g", TINTA2, a))
    E.frase(c, t, C["s15.b"], ps("pressão do ar:", "i", 66), XE, 380, passo=0.1)
    E.formula_em(c, t, C["s15.b"] + 0.6, "380 mmHg", XE + 460, 385, 90, "g", COR)
    E.frase(c, t, C["s15.c"], ps("temperatura:", "i", 66), XE, 520, passo=0.1)
    E.formula_em(c, t, C["s15.c"] + 0.6, "−23 °C", XE + 420, 525, 90, "g", FRIO)
    E.frase(c, t, C["s15.d"], [("1", "g", 56, COR)] + ps("quanto é em atmosfera?", "i", 64), XE, 720, passo=0.1)
    E.frase(c, t, C["s15.e"], [("2", "g", 56, COR)] + ps("e em kelvin?", "i", 64), XE, 840, passo=0.1)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=520, r=170)


def _monte():
    p = skia.Path(); p.moveTo(1120, 700); p.lineTo(1500, 330); p.lineTo(1880, 700); p.close()
    return p


def _neve():
    p = skia.Path(); p.moveTo(1500, 330); p.lineTo(1420, 410); p.lineTo(1470, 395); p.lineTo(1500, 430); p.lineTo(1535, 395); p.lineTo(1580, 410); p.close()
    return p


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s17.a"], "380 = 760 ÷ 2", XE, 380, 100, "g", TINTA)
    bola_txt(c, t, C["s17.b"], "0,5 atm", XE + 1100, 345, 120, 54, CERTO)
    E.formula_em(c, t, C["s17.c"], "−23 + 273 =", XE, 720, 100, "g", TINTA)
    bola_txt(c, t, C["s17.d"], "250 K", XE + 1000, 685, 120, 60, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s18.a", [("pressão", "g", 66, COR), ("=", "g", 66, TINTA2)] + ps("batidas das partículas", "i", 70)),
                 ("s18.b", [("K", "g", 66), ("=", "g", 66, TINTA2), ("°C + 273", "g", 66, COR)]),
                 ("s18.c", [("1 atm", "g", 66), ("=", "g", 66, TINTA2), ("760 mmHg", "g", 66, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("apertar,", "g", 76), ("aquecer", "g", 76), ("ou", "i", 80), ("travar", "g", 76, COR)], XE, 420, passo=0.12)
    frac_q_em(c, t, C["s19.b"], "P1V1", "T1", XE + 180, 600, 80)
    E.formula_em(c, t, C["s19.b"] + 0.3, "=", XE + 380, 650, 80, "g", TINTA2)
    frac_q_em(c, t, C["s19.b"] + 0.5, "P2V2", "T2", XE + 580, 600, 80)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 780, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 805, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 960)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pressao=b_pressao, volume=b_volume, temperatura=b_temperatura, kelvin=b_kelvin,
              unidades=b_unidades, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
