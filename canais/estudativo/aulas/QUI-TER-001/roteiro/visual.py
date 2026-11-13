"""Visual — Estudativo · QUI-TER-001: exotérmica, endotérmica e ΔH. Primeira aula da trilha Termoquímica e Cinética.

Segue a LINGUAGEM VISUAL DA QUÍMICA do cabeçalho da QUI-MIS-001 (fórmula sempre com Q.formula, átomo CPK, palco só no atalho).
LINGUAGEM VISUAL DA TRILHA "Termoquímica e Cinética" (as aulas QUI-TER-* copiam daqui):
- SINAL DO ΔH tem cor fixa, a mesma do kit (Q.energia): ΔH < 0 (exotérmica) em AZUL = Q.ELETRON; ΔH > 0 (endotérmica) em
  ÂMBAR #E8A317. O número do ΔH sai na cor do sinal; o resto da equação, em tinta. Nunca use vermelho/verde para sinal.
- CALOR que passa = seta ondulada laranja-quente #E8590C (seta_calor): sai do sistema na exo, entra no sistema na endo.
  SISTEMA = círculo tracejado turquesa com as partículas dentro; VIZINHANÇA = o que fica fora dele (pílulas em tinta).
- TERMÔMETRO da vizinhança (termometro): líquido vermelho que sobe (esquenta) ou desce (esfria).
- DIAGRAMA DE ENTALPIA em patamares (niveis): eixo de pé "entalpia", patamar dos reagentes à esquerda e dos produtos à direita,
  cada um com a fórmula e o nome do lado de fora (em cima se for o mais alto, embaixo se for o mais baixo); seta do ΔH no
  meio, na cor do sinal. Valores aparecem como marcas do eixo ("na marca de 120"), nunca como entalpia absoluta.
  O caminho com morro (energia de ativação) é Q.energia, a partir da QUI-TER-006.
- Conta de apoio em TINTA2; resultado na esfera (bola_txt), na cor do sinal quando for um ΔH.
Peças desta aula candidatas ao kit (quimica.py): niveis, seta_calor, termometro, bolsa (compressa), chama, panela, gelo.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Termoquímica e Cinética")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-TER-001_exotermica_endotermica_delta_h.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("sistema", "dh", "diagrama", "bolsa", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AZUL, AMBAR, CALOR = Q.ELETRON, "#E8A317", "#E8590C"

# as contas da aula
assert Q.lados("2 H2 + O2 -> 2 H2O")[0] == Q.lados("2 H2 + O2 -> 2 H2O")[1]
assert 2 * (-286) == -572
assert 40 - 120 == -80 and 120 - 40 == 80
assert 250 * 4.184 > 1045 and 250 * 4.184 < 1047   # rótulo: 250 kcal ≈ 1046 kJ


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
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    """lista numerada: itens = [(instante, partes da frase)]"""
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def cor_dh(v):
    return AZUL if v < 0 else AMBAR


def dh_em(c, t, t0, valor, x, y, size, align="left", unidade=" kJ", escuro=False):
    """ΔH = −572 kJ: o número na cor do sinal"""
    tinta = BR if escuro else TINTA
    num = ("+" if valor > 0 else "−") + str(abs(valor)) + unidade

    def desenha(a):
        w1 = E.formula(None, "ΔH = ", 0, 0, size, a=0)
        w2 = E.formula(None, num, 0, 0, size, a=0)
        x0 = x - (w1 + w2) / 2 if align == "center" else x - w1 - w2 if align == "right" else x
        E.formula(c, "ΔH = ", x0, y, size, "g", tinta, a)
        E.formula(c, num, x0 + w1, y, size, "g", cor_dh(valor), a)
    E.foco(c, t, t0, 0.5, desenha)


def seta_calor(c, x0, y0, x1, y1, t, a=1.0, p=1.0, cor=CALOR, onda=13, largura=6):
    """calor que passa: seta ondulada que corre de (x0, y0) até (x1, y1)"""
    if a <= 0 or p <= 0:
        return
    L = math.dist((x0, y0), (x1, y1))
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    nx, ny = -uy, ux
    pth = skia.Path()
    n = 70
    for i in range(n + 1):
        s = i / n * p
        amp = onda * max(0.0, min(1.0, (0.86 - s) / 0.12)) if s > 0.74 else onda
        f = math.sin(s * L / 38 * 2 * math.pi - t * 7)
        px, py = x0 + ux * s * L + nx * amp * f, y0 + uy * s * L + ny * amp * f
        if i == 0:
            pth.moveTo(px, py)
        else:
            pth.lineTo(px, py)
    pt = M.paint(cor, a, stroke=largura, cap_round=True)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(pth, pt)
    if p > 0.8:
        ex, ey = x0 + ux * p * L, y0 + uy * p * L
        M.arrow(c, ex - ux * 34, ey - uy * 34, ex, ey, cor, a, largura, 26)


def termometro(c, cx, ytop, h, nivel, a=1.0, escuro=False):
    """termômetro de pé: nivel 0..1 é a altura do líquido vermelho"""
    if a <= 0:
        return
    vidro = "#FFFFFF" if not escuro else "#2A2B33"
    borda = TINTA2 if not escuro else "#9AA0A8"
    w = 40
    M.rrect(c, cx - w / 2, ytop, w, h, w / 2, vidro, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, ytop, w, h), w / 2, w / 2), M.paint(borda, a, stroke=4))
    yb = ytop + h + 26
    c.drawCircle(cx, yb, 40, M.paint(vidro, a))
    c.drawCircle(cx, yb, 40, M.paint(borda, a, stroke=4))
    c.drawCircle(cx, yb, 30, M.paint("#E5322D", a))
    hl = (h - 24) * max(0.05, min(1.0, nivel))
    M.rrect(c, cx - 9, ytop + h - hl, 18, hl + 20, 9, "#E5322D", a)
    for k in range(1, 6):
        yy = ytop + h * k / 6
        M.line(c, cx + w / 2 + 4, yy, cx + w / 2 + 22, yy, borda, a, 3)


def bolsa(c, cx, cy, w, h, a=1.0, frio=0.0, t=0.0, grao=0.0):
    """compressa instantânea: saco plástico com água; frio 0..1 deixa azulado e com geada; grao 0..1 mostra o pó ainda sem dissolver"""
    if a <= 0:
        return
    cor = M.mix("#E9F4FA", "#8FCFEA", frio)
    x, y = cx - w / 2, cy - h / 2
    for yy in (y - 18, y + h - 6):  # as bordas soldadas, em zigue-zague
        pth = skia.Path()
        pth.moveTo(x + 10, yy + 12)
        for k in range(int((w - 20) / 24) + 1):
            pth.lineTo(x + 10 + k * 24 + 12, yy + (0 if k % 2 == 0 else 24))
        c.drawPath(pth, M.paint("#B9C6CF", a, stroke=5))
    M.rrect(c, x, y, w, h, 46, cor, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 46, 46), M.paint("#9DB3C2", a, stroke=4))
    M.rrect(c, x + 40, y + 34, w * 0.18, h * 0.62, 20, "#FFFFFF", 0.45 * a)
    if frio > 0:
        for k in range(9):
            fx = x + w * 0.62 + (k * 131 % int(w * 0.3))
            fy = y + 40 + (k * 97 % int(h - 80))
            r = (16 + 4 * math.sin(t * 2 + k)) * min(1.0, w / 500)
            for ang in (0, 60, 120):
                dx, dy = r * math.cos(math.radians(ang)), r * math.sin(math.radians(ang))
                M.line(c, fx - dx, fy - dy, fx + dx, fy + dy, "#FFFFFF", a * frio, 3)
    fs = 40 * min(1.0, w / 500)
    E.escreve(c, "COMPRESSA", cx - E.larg("COMPRESSA", "b", fs) / 2, cy - fs * 0.25, fs, "b", "#5E7A8C", a)
    E.escreve(c, "FRIA", cx - E.larg("FRIA", "b", fs) / 2, cy + fs * 1.1, fs, "b", "#5E7A8C", a)
    if grao > 0:
        for k in range(26):
            gx = cx - w * 0.36 + (k * 37 % int(w * 0.72))
            gy = y + h - 40 - (k * 53 % 70)
            c.drawCircle(gx, gy, 7, M.paint("#FFFFFF", a * grao))
            c.drawCircle(gx, gy, 7, M.paint("#9DB3C2", a * grao, stroke=2))


def chama(c, cx, cy, s, t, a=1.0):
    """chama de fogão: base em (cx, cy)"""
    if a <= 0:
        return
    for k, (dx, esc) in enumerate(((-0.55, 0.75), (0.0, 1.0), (0.55, 0.75))):
        f = 1 + 0.07 * math.sin(t * 9 + k * 2)
        x0, hh, ww = cx + dx * s, s * esc * f, s * 0.32 * esc
        for cor, kk in (("#F59F00", 1.0), ("#FFE066", 0.62), ("#4DABF7", 0.3)):
            pth = skia.Path()
            pth.moveTo(x0, cy - hh * kk)
            pth.cubicTo(x0 + ww * kk * 1.2, cy - hh * kk * 0.45, x0 + ww * kk, cy, x0, cy)
            pth.cubicTo(x0 - ww * kk, cy, x0 - ww * kk * 1.2, cy - hh * kk * 0.45, x0, cy - hh * kk)
            c.drawPath(pth, M.paint(cor, a))


def panela(c, cx, cy, w, h, a=1.0, t=0.0, vapor=0.0):
    """panela vista de lado: (cx, cy) é o centro do fundo"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h, w, h, 18, "#4A4D55", a)
    M.rrect(c, cx - w / 2 - 16, cy - h - 10, w + 32, 22, 11, "#2E3036", a)
    M.rrect(c, cx + w / 2 + 10, cy - h + 20, 150, 26, 13, "#2E3036", a)
    if vapor > 0:
        for k in range(3):
            xx = cx - w * 0.25 + k * w * 0.25
            pth = skia.Path()
            for i in range(30):
                yy = cy - h - 30 - i * 5
                px = xx + 12 * math.sin(i * 0.4 - t * 4 + k)
                (pth.moveTo if i == 0 else pth.lineTo)(px, yy)
            c.drawPath(pth, M.paint(TINTA2, 0.6 * a * vapor, stroke=5, cap_round=True))


def gelo(c, cx, cy, s, a=1.0, derrete=0.0):
    """cubo de gelo que derrete numa poça: (cx, cy) é o chão"""
    if a <= 0:
        return
    pr = s * (0.5 + 0.7 * derrete)
    c.drawOval(skia.Rect.MakeLTRB(cx - pr, cy - 16, cx + pr, cy + 16), M.paint("#A5D8FF", 0.7 * a))
    k = s * (1 - 0.55 * derrete)
    M.rrect(c, cx - k / 2, cy - k, k, k, k * 0.18, "#D0EBFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - k / 2, cy - k, k, k), k * 0.18, k * 0.18), M.paint("#74C0FC", a, stroke=4))
    M.rrect(c, cx - k * 0.32, cy - k * 0.84, k * 0.2, k * 0.42, 8, "#FFFFFF", 0.8 * a)


def sistema(c, t, t0, cx, cy, r, sentido=0, tc=None, escuro=False, rotulo=True, alcance=150, angulos=(20, 140, 260)):
    """o sistema (círculo tracejado com partículas) e as setas de calor: sentido = +1 sai (exo), −1 entra (endo), 0 sem setas"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(E.COR, 0.12 * q))
    pt = M.paint(E.COR, q, stroke=6)
    pt.setPathEffect(skia.DashPathEffect.Make([22, 14], t * 20))
    c.drawCircle(cx, cy, r, pt)
    for k, el in enumerate(("O", "H", "C", "H", "O")):
        ang = k * 72 + t * 25
        Q.atomo(c, cx + r * 0.45 * math.cos(math.radians(ang)), cy + r * 0.45 * math.sin(math.radians(ang)), r * 0.16, el, q, rotulo=False, escuro=escuro)
    if rotulo:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, "sistema", cx, cy + r + 56, 46, "i", COR if not escuro else CLARO, a))
    if sentido and tc is not None and t >= tc:
        p = ease_out(prog(t, tc, 0.8))
        for ang in angulos:
            ux, uy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
            a0, a1 = (r + 16, r + alcance) if sentido > 0 else (r + alcance, r + 16)
            seta_calor(c, cx + ux * a0, cy + uy * a0, cx + ux * a1, cy + uy * a1, t, 1.0, p)


def niveis(c, t, te, x, y, w, h, vr, vp, vmax, tr=None, tp=None, ts=None, fr=None, rot=("reagentes", "produtos"), marcas=(),
           dh=None, escuro=False, size=46, vmin=0):
    """diagrama de entalpia em patamares na caixa (x, y, w, h). vr, vp = marcas dos reagentes e dos produtos no eixo;
    tr, tp, ts = instantes do patamar dos reagentes, dos produtos e da seta do ΔH; fr = (fórmula dos reagentes, dos produtos);
    marcas = valores escritos no eixo; dh = texto ao lado da seta (senão, "ΔH < 0" ou "ΔH > 0"). Devolve Y(valor) → pixel"""
    tinta = BR if escuro else TINTA
    tinta2 = "#9AA0A8" if escuro else TINTA2
    Y = lambda v: y + h - (v - vmin) / (vmax - vmin) * h
    q = ep(t, te, 0.4)
    if q <= 0:
        return Y
    F.seta(c, x, y + h, x, y - 40, tinta, q, 5, 24, ease_out(prog(t, te, 0.5)))
    E.foco(c, t, te + 0.3, 0.4, lambda a: E.escreve(c, "entalpia", x + 26, y - 14, size, "i", tinta, a))
    for v in marcas:
        E.foco(c, t, te + 0.4, 0.4, lambda a, v=v: (M.line(c, x - 14, Y(v), x + 14, Y(v), tinta, a, 4),
                                                    E.formula(c, str(v), x - 26, Y(v) + size * 0.36, size, "g", tinta2, a, "right")))
    barras = ((tr, vr, x + 0.08 * w, x + 0.40 * w, 0), (tp, vp, x + 0.60 * w, x + 0.92 * w, 1))
    for tb, v, x0, x1, k in barras:
        if tb is None:
            continue
        p = ease_io(prog(t, tb, 0.6))
        if p <= 0:
            continue
        cor = E.COR if k == 1 else tinta
        M.line(c, x0, Y(v), x0 + (x1 - x0) * p, Y(v), cor, 1.0, 10)
        alto = v >= (vp if k == 0 else vr)
        yt = Y(v) - 26 if alto else Y(v) + size + 30
        cx_ = (x0 + x1) / 2
        if fr:
            E.foco(c, t, tb + 0.3, 0.4, lambda a, cx_=cx_, yt=yt, k=k, alto=alto:
                   Q.formula(c, fr[k], cx_, yt - (size * 1.1 if alto else -size * 1.25 + size * 1.1), size * 1.05, tinta, a, "center"))
            yr = yt if alto else yt + size * 1.25
        else:
            yr = yt
        E.foco(c, t, tb + 0.2, 0.4, lambda a, cx_=cx_, yr=yr, k=k: centro(c, rot[k], cx_, yr, size * 0.95, "i", tinta2, a))
    if ts is not None and t >= ts:
        p = ep(t, ts, 0.4)
        xm = x + 0.5 * w
        M.line(c, x + 0.40 * w, Y(vr), xm + 14, Y(vr), tinta2, 0.7 * p, 3, dash=[10, 8])
        M.line(c, xm - 14, Y(vp), x + 0.60 * w, Y(vp), tinta2, 0.7 * p, 3, dash=[10, 8])
        d = vp - vr
        F.seta(c, xm, Y(vr), xm, Y(vp) + (6 if d < 0 else -6), cor_dh(d), p, 7, 26, ease_out(prog(t, ts, 0.6)))
        s_ = dh or ("ΔH < 0" if d < 0 else "ΔH > 0")
        E.foco(c, t, ts + 0.3, 0.4, lambda a: E.formula(c, s_, xm + 22, (Y(vr) + Y(vp)) / 2 + size * 0.36, size, "g", cor_dh(d), a))
    return Y


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def um():
        frio = ep(t, b1, 1.4)
        E.foco(c, t, a1, 0.6, lambda a: bolsa(c, 1380, 560, 600, 420, a, frio, t))
        if t >= b1:
            E.foco(c, t, b1, 0.5, lambda a: termometro(c, 1780, 330, 360, 0.75 - 0.55 * ep(t, b1 + 0.3, 1.6), a))
        E.frase(c, t, a1, ps("você aperta a bolsa", "i", 76), XE, 300, passo=0.12)
        E.frase(c, t, b1, [("gelada", "g", 170, COR)], XE, 480)
        E.frase(c, t, b1 + 0.7, ps("sem geladeira nenhuma", "i", 60, TINTA2), XE, 570, passo=0.1)
        pilula_em(c, t, c1, "libera?", XE + 150, 730, 62, TINTA)
        pilula_em(c, t, c1 + 0.5, "absorve?", XE + 490, 730, 62, TINTA)
        E.frase(c, t, d1, ps("a resposta óbvia está", "i", 66) + [("errada", "g", 62, ERRADO)], XE, 900, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("o", "i", 74), ("sinal", "g", 70), ("do", "i", 74), ("ΔH", "g", 70, COR)]),
                 (C["s02.c"], [("diagrama", "g", 70), ("de", "i", 74), ("entalpia", "g", 70, COR)]),
                 (C["s02.d"], [("a", "i", 74), ("bolsa", "g", 70), ("gelada", "g", 70, COR)])], XE, 470, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 80, TINTA2), XE, 220, passo=0.12)
    lista(c, t, [(C["s03.a"], [("calor", "g", 64, COR)] + ps("vai do quente para o frio", "i", 68)),
                 (C["s03.b"], [("derreter", "g", 64), ("e", "i", 68), ("ferver", "g", 64)] + ps("absorvem calor", "i", 68)),
                 (C["s03.c"], [("negativo", "g", 64, COR)] + ps("fica abaixo do zero", "i", 68))], XE, 420, 180)
    if t >= C["s03.c"]:
        E.reta(c, t, C["s03.c"] + 0.6, 1100, 1760, 900, -3, 3, [-3, -2, -1, 0, 1, 2, 3])
    E.foco(c, t, C["s03.a"] + 0.6, 0.6, lambda a: termometro(c, 1640, 230, 300, 0.4 + 0.3 * math.sin(t * 0.8), a))


# ---------------- sistema, exo e endo ----------------
def b_sistema(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("sistema", "g", 84, COR), ("=", "g", 84, TINTA2)] + ps("a reação", "i", 88), XE, 300, passo=0.12)
        E.frase(c, t, C["s04.b"], [("vizinhança", "g", 84), ("=", "g", 84, TINTA2)] + ps("tudo em volta", "i", 88), XE, 460, passo=0.12)
        sistema(c, t, C["s04.a"] + 0.3, 1520, 560, 190, rotulo=False)
        E.foco(c, t, C["s04.a"] + 0.6, 0.4, lambda a: centro(c, "sistema", 1520, 830, 56, "g", COR, a))
        for k, (s, x, y) in enumerate((("o ar", 1520, 260), ("o plástico", 1740, 420), ("a sua mão", 1740, 720))):
            pilula_em(c, t, C["s04.b"] + 0.5 + 0.35 * k, s, x, y, 46, TINTA, "i")
        if t >= C["s04.c"]:
            p = ease_out(prog(t, C["s04.c"], 0.8))
            seta_calor(c, 1310, 520, 1170, 520, t, 1, p)
            seta_calor(c, 1170, 620, 1310, 620, t, 1, p)
        E.frase(c, t, C["s04.c"] + 0.3, ps("a energia passa", "i", 70, TINTA2) + [("de um para o outro", "g", 60, CALOR)], XE, 700, passo=0.12)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    # em cima, as cenas; embaixo, os dois cartões
    E.foco(c, t, C["s05.a"], 0.5, lambda a: (chama(c, 420, 470, 120, t, a)))
    E.foco(c, t, C["s05.a"] + 0.3, 0.5, lambda a: panela(c, 420, 360, 360, 170, a, t, ep(t, C["s05.b"], 0.8)))
    if t >= C["s05.b"]:
        p = ease_out(prog(t, C["s05.b"], 0.8))
        seta_calor(c, 560, 440, 700, 330, t, 1, p)
    E.frase(c, t, C["s05.b"] + 0.2, [("a", "i", 56), ("panela", "g", 52), ("esquenta", "i", 56)], 690, 290, passo=0.1)

    def cartao(x, t0, titulo, sentido, sub, cor_t):
        q = ep(t, t0, 0.5)
        if q <= 0:
            return
        M.rrect(c, x, 560, 760, 440, 36, "#FFFFFF", q, shadow=True)
        sistema(c, t, t0, x + 200, 780, 88, sentido, t0 + 0.4, rotulo=False, alcance=95, angulos=(180, 245, 115))
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.escreve(c, titulo, x + 350, 760, 62, "g", cor_t, a))
        E.frase(c, t, sub[0], [(sub[1], "g", 50, TINTA), ("=", "g", 50, TINTA2), (sub[2], "i", 52, TINTA2)], x + 350, 850, passo=0.12)
    cartao(150, C["s05.d"], "exotérmica", +1, (C["s05.e"], "exo", "para fora"), AZUL)
    if t >= C["s06"]:
        E.foco(c, t, C["s06.d"], 0.5, lambda a: gelo(c, 1560, 480, 220, a, 0.45 * ep(t, C["s06.d"] + 0.4, 3.0)))
        if t >= C["s06.d"] + 0.6:
            p = ease_out(prog(t, C["s06.d"] + 0.6, 0.8))
            seta_calor(c, 1830, 300, 1700, 400, t, 1, p)
            seta_calor(c, 1300, 300, 1430, 400, t, 1, p)
        E.frase(c, t, C["s06.a"], ps("puxa calor de fora", "i", 56), 1180, 170, passo=0.1)
        E.frase(c, t, C["s06.b"], ps("o que está em volta", "i", 52, TINTA2) + [("esfria", "g", 48)], 1180, 240, passo=0.1)
        cartao(1010, C["s06.a"] + 0.4, "endotérmica", -1, (C["s06.c"], "endo", "para dentro"), AMBAR)


# ---------------- entalpia e ΔH ----------------
def b_dh(c, t, C, b):
    def s07():
        E.frase(c, t, C["s07.a"], [("entalpia", "g", 150, COR)], XE, 330)
        E.foco(c, t, C["s07.a"] + 0.6, 0.5, lambda a: E.escreve(c, "H", 1080, 340, 220, "g", TINTA, a))
        E.foco(c, t, C["s07.a"] + 1.4, 0.5, lambda a: (Q.atomo(c, 1500, 260, 70, "H", a), E.pilula(c, "não é o hidrogênio", 1500, 400, 40, "b", fundo=TINTA, a=a)))
        if t >= C["s07.a"] + 2.0:
            E.risco(c, 1420, 330, 1580, 190, t, C["s07.a"] + 2.0, largura=9)
        E.frase(c, t, C["s07.a"] + 2.4, ps("a energia guardada nas substâncias", "i", 64, TINTA2), XE, 460, passo=0.1)
        E.frase(c, t, C["s07.b"], ps("ninguém mede a entalpia sozinha", "i", 64), XE, 620, passo=0.1)
        E.foco(c, t, C["s07.c"], 0.5, lambda a: E.formula(c, "ΔH", XE, 880, 230, "g", COR, a))
        E.foco(c, t, C["s07.c"] + 0.8, 0.4, lambda a: E.pilula(c, "Δ = variação", XE + 650, 810, 60, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.foco(c, t, C["s08.a"], 0.5, lambda a: E.formula(c, "ΔH = produtos − reagentes", W / 2, 230, 96, "g", TINTA, a, "center"))
    pilula_em(c, t, C["s08.b"], "chegada − partida", W / 2, 340, 56, E.COR)
    for k, (tt, tv, x, nome, s_, v, txt) in enumerate(((C["s08.c"], C["s08.d"], 520, "exotérmica", "ΔH < 0", -1, "a energia saiu"),
                                                       (C["s08.e"], C["s08.f"], 1400, "endotérmica", "ΔH > 0", 1, "a energia entrou"))):
        E.foco(c, t, tt, 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 520, 76, "g", TINTA, a))
        E.foco(c, t, tt + 0.4, 0.4, lambda a, x=x, txt=txt: centro(c, txt, x, 600, 56, "i", TINTA2, a))
        E.foco(c, t, tv, 0.5, lambda a, x=x, s_=s_, v=v: E.formula(c, s_, x, 790, 150, "g", cor_dh(v), a, "center"))
    # o saldo de uma conta
    for k, (tt, x, s, v) in enumerate(((C["s09.b"], 520, "pagou: o saldo desce", -1), (C["s09.c"], 1400, "recebeu: o saldo sobe", 1))):
        if t >= tt:
            p = ease_out(prog(t, tt, 0.6))
            F.seta(c, x - 200, 905 + 45 * v, x - 200, 905 + 45 * v - 90 * v * p, cor_dh(v), 1, 7, 24)
        E.foco(c, t, tt, 0.4, lambda a, x=x, s=s: centro(c, s, x + 30, 925, 52, "i", TINTA, a))
    E.frase(c, t, C["s09.c"] + 1.2, ps("o que a reação perde, a vizinhança ganha", "i", 52, TINTA2), W / 2, 1030, "center", 0.08)


# ---------------- exemplo: a queima do hidrogênio ----------------
EQ = "2 H2(g) + O2(g) -> 2 H2O(l)"


def b_exemplo(c, t, C, b):
    a1 = C["s10.a"]
    cores = {"coef": E.COR} if t >= C["s11.c"] else None
    cs = Q.equacao(c, t, a1, EQ, W / 2, 300, 110, tl=[a1, a1 + 0.4, a1 + 0.7, a1 + 1.1, a1 + 1.5], cores=cores)
    # os modelos embaixo de cada espécie
    for k, (mol, n) in enumerate((("H2", 2), ("O2", 1), ("H2O", 2))):
        for j in range(n):
            dx = (j - (n - 1) / 2) * 120
            Q.molecula(c, t, a1 + 0.3 + 0.5 * k, mol, cs[k] + dx, 480, 70, passo=0.1)
    dh_em(c, t, C["s10.b"], -572, W / 2, 680, 120, "center")
    if C["s10.c"] <= t < C["s11"] + 0.4:
        def rotulo():
            M.rrect(c, 1180, 790, 600, 220, 20, "#FFFFFF", 1, shadow=True)
            E.escreve(c, "INFORMAÇÃO NUTRICIONAL", 1210, 840, 30, "b", TINTA)
            M.line(c, 1210, 860, 1750, 860, TINTA, 1, 4)
            E.escreve(c, "Valor energético", 1210, 920, 36, "b", TINTA)
            E.formula(c, "250 kcal = 1046 kJ", 1750, 980, 40, "g", TINTA, 1, "right")
            wk = E.formula(None, "1046 kJ", 0, 0, 40, a=0)
            E.caixa_pontilhada(c, 1750 - wk - 12, 938, wk + 24, 58, 1, E.COR)
        E.saida(c, t, C["s11"] + 0.3, lambda: E.foco(c, t, C["s10.c"] + 0.6, 0.5, lambda a: rotulo()))
        E.frase(c, t, C["s10.c"], [("kJ", "g", 64, COR), ("=", "g", 64, TINTA2)] + ps("quilojoule, unidade de energia", "i", 64), XE, 870, passo=0.1)
    if t >= C["s11"] + 0.3:
        if t >= C["s11.a"]:
            q = ep(t, C["s11.a"], 0.4)
            w1 = E.formula(None, "ΔH = ", 0, 0, 120, a=0)
            wt = w1 + E.formula(None, "−572 kJ", 0, 0, 120, a=0)
            wm = E.formula(None, "−", 0, 0, 120, a=0)
            xs = W / 2 - wt / 2 + w1 + wm / 2
            c.drawCircle(xs, 645, 52, M.paint(AZUL, q, stroke=6))
        pilula_em(c, t, C["s11.b"], "libera energia: exotérmica", W / 2, 840, 60, AZUL)
        if t >= C["s11.c"]:
            for g in Q.grupos(EQ, W / 2, 300, 110, "center"):
                if g["tipo"] == "coef":
                    q = ep(t, C["s11.c"], 0.4)
                    E.caixa_pontilhada(c, g["x0"] - 14, g["topo"] - 14, g["x1"] - g["x0"] + 28, g["base"] - g["topo"] + 28, q, E.COR, prog_=q)
            E.frase(c, t, C["s11.c"] + 0.3, ps("vale para as quantidades da equação", "i", 60, TINTA2), W / 2, 980, "center", 0.1)


# ---------------- diagrama de entalpia ----------------
def b_diagrama(c, t, C, b):
    E.frase(c, t, C["s12.a"], ps("diagrama de", "i", 70) + [("entalpia", "g", 66, COR)], XE, 150, passo=0.12)
    niveis(c, t, C["s12.b"], 330, 290, 960, 620, 80, 20, 100, tr=C["s12.c"], tp=C["s12.d"], ts=C["s12.e"],
           fr=("2 H2 + O2", "2 H2O"), dh="ΔH = −572 kJ" if t >= C["s13.b"] else None)

    def notas():
        E.foco(c, t, C["s12.b"] + 0.6, 0.4, lambda a: E.escreve(c, "mais alto", 1420, 360, 60, "g", TINTA, a))
        E.foco(c, t, C["s12.b"] + 0.9, 0.4, lambda a: E.escreve(c, "mais energia", 1420, 440, 60, "i", TINTA2, a))
        E.foco(c, t, C["s12.b"] + 2.4, 0.4, lambda a: E.escreve(c, "o zero é referência", 1420, 560, 50, "i", TINTA2, a))
        E.foco(c, t, C["s12.e"] + 0.4, 0.4, lambda a: E.escreve(c, "partida → chegada", 1420, 700, 54, "g", COR, a))
    E.saida(c, t, C["s13.a"] - 0.1, notas)
    if t >= C["s13.a"]:
        E.frase(c, t, C["s13.a"], ps("produtos abaixo", "i", 60), 1400, 330, passo=0.12)
        E.frase(c, t, C["s13.b"], [("seta", "i", 60), ("desce", "g", 56, AZUL)], 1400, 420, passo=0.12)
        pilula_em(c, t, C["s13.b"] + 0.6, "exotérmica", 1560, 500, 46, AZUL)
    if t >= C["s13.c"]:
        # o caso contrário, menor, à direita
        niveis(c, t, C["s13.c"], 1400, 610, 400, 330, 25, 85, 100, tr=C["s13.c"] + 0.2, tp=C["s13.c"] + 0.4, ts=C["s13.d"], size=40)
        pilula_em(c, t, C["s13.d"] + 0.5, "endotérmica", 1600, 1020, 40, AMBAR)
    pilula_em(c, t, C["s13.e"], "o morro no caminho: outra aula", 800, 1020, 40, TINTA2, "b")


# ---------------- a bolsa gelada (erro comum) ----------------
def b_bolsa(c, t, C, b):
    frio = ep(t, C["s14.c"] + 0.6, 2.0)
    grao = 1 - ep(t, C["s14.c"], 1.6)
    E.foco(c, t, C["s14"], 0.5, lambda a: bolsa(c, 1500, 470, 480, 360, a, frio, t, grao))
    if t >= C["s14.c"]:
        E.foco(c, t, C["s14.c"], 0.4, lambda a: termometro(c, 1830, 300, 300, 0.7 - 0.5 * frio, a))

    def s14():
        E.frase(c, t, C["s14.a"], ps("dentro: água e um pó", "i", 70), XE, 260, passo=0.12)
        Q.formula_em(c, t, C["s14.b"], "NH4NO3", XE, 480, 150, cores={"indice": E.COR})
        E.foco(c, t, C["s14.b"] + 0.5, 0.4, lambda a: E.escreve(c, "nitrato de amônio", XE, 570, 56, "i", TINTA2, a))
        E.frase(c, t, C["s14.c"], ps("apertou:", "i", 66) + [("o pó se dissolve", "g", 60, COR)], XE, 760, passo=0.12)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if C["s15"] <= t < C["s16"]:
        def s15():
            E.frase(c, t, C["s15.a"], [("o erro comum", "g", 70, ERRADO)], XE, 240)
            for k, s in enumerate(("ficou fria", "soltou frio", "exotérmica")):
                pilula_em(c, t, C["s15.a"] + 0.6 + 0.7 * k, s, XE + 140 + k * 320, 380, 42, ERRADO, "b")
                if k:
                    E.foco(c, t, C["s15.a"] + 0.5 + 0.7 * k, 0.3, lambda a, k=k: centro(c, "→", XE + k * 320 - 20, 396, 50, "g", ERRADO, a))
            if t >= C["s15.b"] - 0.2:
                E.risco(c, XE, 410, XE + 920, 350, t, C["s15.b"] - 0.2, largura=10)
            E.frase(c, t, C["s15.b"], ps("frio não é uma coisa que sai", "i", 70), XE, 580, passo=0.12)
            E.frase(c, t, C["s15.c"], ps("a bolsa esfria porque", "i", 70) + [("perde calor", "g", 64, CALOR)], XE, 720, passo=0.12)
        E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], ps("perde para onde?", "i", 74), XE, 240, passo=0.12)
    for k, (s, x, y) in enumerate((("o plástico", 1200, 860), ("a sua pele", 1760, 860))):
        pilula_em(c, t, C["s16.b"] + 0.3 * k, s, x, y + 90, 44, TINTA, "i")
        if t >= C["s16.b"] + 0.3 * k:
            seta_calor(c, x, y + 40, x + (220 if k == 0 else -180), y - 160, t, 1, ease_out(prog(t, C["s16.b"] + 0.3 * k, 0.8)))
    E.frase(c, t, C["s16.b"], ps("a mistura", "i", 66) + [("puxa calor", "g", 60, CALOR)], XE, 380, passo=0.12)
    E.frase(c, t, C["s16.c"], ps("a vizinhança", "i", 66) + [("esfria", "g", 60)], XE, 500, passo=0.12)
    E.foco(c, t, C["s16.d"], 0.5, lambda a: E.escreve(c, "endotérmica", XE, 700, 96, "g", AMBAR, a))
    E.foco(c, t, C["s16.d"] + 0.4, 0.5, lambda a: E.formula(c, "ΔH > 0", XE, 840, 110, "g", AMBAR, a))
    E.foco(c, t, C["s16.d"] + 0.8, 0.4, lambda a: E.selo(c, XE + 470, 800, 50, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s18"]:
        def s17():
            E.frase(c, t, C["s17"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 150, "center", 0.12)
            E.frase(c, t, C["s17.a"], ps("o sinal do", "i", 70, BR) + [("ΔH", "g", 66, CLARO)] + ps("é o contrário do termômetro de fora", "i", 70, BR),
                    W / 2, 270, "center", 0.1)
            for k, (tt, x, v, s1, s2) in enumerate(((C["s17.b"], 560, -1, "esquentou em volta", "ΔH < 0"), (C["s17.c"], 1360, 1, "esfriou em volta", "ΔH > 0"))):
                nivel = 0.35 + 0.45 * ep(t, tt + 0.2, 1.4) * (1 if v < 0 else -0.6)
                E.foco(c, t, tt, 0.4, lambda a, x=x, nivel=nivel: termometro(c, x - 230, 420, 380, nivel, a, escuro=True))
                E.foco(c, t, tt + 0.1, 0.4, lambda a, x=x, s1=s1: E.escreve(c, s1, x - 140, 560, 54, "i", BR, a))
                E.foco(c, t, tt + 0.6, 0.5, lambda a, x=x, s2=s2, v=v: E.formula(c, s2, x - 140, 740, 130, "g", cor_dh(v), a))
                E.foco(c, t, tt + 1.0, 0.4, lambda a, x=x, v=v: E.escreve(c, "soltou calor" if v < 0 else "puxou calor", x - 140, 850, 50, "i", CLARO, a))
        E.saida(c, t, C["s18"] - 0.1, s17)
        return
    E.frase(c, t, C["s18.a"], ps("o", "i", 72, CLARO) + [("ΔH", "g", 68, BR)] + ps("é contado do lado da reação", "i", 72, CLARO), W / 2, 300, "center", 0.12)
    E.frase(c, t, C["s18.b"], ps("deu o diagrama ou os números?", "i", 70, BR), W / 2, 520, "center", 0.12)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.formula(c, "ΔH = chegada − partida", W / 2, 720, 110, "g", CLARO, a, "center"))


# ---------------- questão ----------------
QX, QY, QW, QH = 300, 290, 760, 620


def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 160)
    niveis(c, t, C["s19.a"] - 0.4, QX, QY, QW, QH, 120, 40, 150, tr=C["s19.a"], tp=C["s19.b"], marcas=(40, 120))
    E.frase(c, t, C["s19.c"], [("1", "g", 56, COR)] + ps("quanto vale o", "i", 60) + [("ΔH?", "g", 56)], 1160, 700, passo=0.08)
    E.frase(c, t, C["s19.d"], [("2", "g", 56, COR)] + ps("exo ou endo?", "i", 60), 1160, 810, passo=0.08)
    E.frase(c, t, C["s19.e"], [("3", "g", 56, COR)] + ps("a vizinhança esquenta ou esfria?", "i", 56), 1160, 920, passo=0.08)
    E.relogio(c, t, C["s20.a"], cx=1500, cy=290, r=110)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    niveis(c, t, C["s21"] - 0.6, QX, QY, QW, QH, 120, 40, 150, tr=C["s21"] - 0.6, tp=C["s21"] - 0.6, marcas=(40, 120),
           ts=C["s21.e"], dh="−80 kJ")
    E.frase(c, t, C["s21.a"], ps("chegada menos partida", "i", 64, TINTA2), 1160, 220, passo=0.1)
    E.formula_em(c, t, C["s21.b"], "40 − 120 =", 1560, 380, 84, "g", TINTA2, "right")
    bola_txt(c, t, C["s21.c"], "−80", 1690, 352, 86, 70, AZUL)
    E.foco(c, t, C["s21.c"] + 0.4, 0.4, lambda a: E.escreve(c, "kJ", 1795, 380, 60, "g", TINTA, a))
    pilula_em(c, t, C["s21.d"], "negativo: exotérmica", 1450, 510, 52, AZUL)
    E.foco(c, t, C["s21.e"] + 0.4, 0.5, lambda a: termometro(c, 1200, 590, 150, 0.3 + 0.5 * ep(t, C["s21.e"] + 0.6, 1.2), a))
    E.frase(c, t, C["s21.e"] + 0.6, ps("a vizinhança", "i", 56) + [("esquenta", "g", 52, CALOR)], 1290, 700, passo=0.1)

    def erro():
        E.foco(c, t, C["s22.a"], 0.5, lambda a: E.formula(c, "120 − 40 = +80", 1480, 920, 70, "g", ERRADO, a, "center"))
        if t >= C["s22.a"] + 0.9:
            E.risco(c, 1230, 940, 1730, 870, t, C["s22.a"] + 0.9, largura=10)
    erro()
    pilula_em(c, t, C["s22.b"], "sempre produtos − reagentes", 1480, 1030, 44, E.COR)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for k, (tt, v, s1, s2, y) in enumerate(((C["s23.a"], -1, "ΔH < 0", "libera calor: a vizinhança esquenta", 420),
                                                 (C["s23.b"], 1, "ΔH > 0", "absorve calor: a vizinhança esfria", 680))):
            E.foco(c, t, tt, 0.5, lambda a, s1=s1, v=v, y=y: E.formula(c, s1, XE, y, 120, "g", cor_dh(v), a))
            E.frase(c, t, tt + 0.4, ps(s2, "i", 64), XE + 520, y - 20, passo=0.1)
        E.foco(c, t, C["s23.b"] + 1.6, 0.5, lambda a: bolsa(c, 1580, 880, 300, 200, a, 1.0, t))
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s24.a"], [("Lei", "g", 130, COR), ("de", "i", 130), ("Hess", "g", 130, COR)], XE, 420)
    E.frase(c, t, C["s24.b"], ps("somar equações, como peças", "i", 64, TINTA2), XE, 560, passo=0.1)
    for k in range(3):
        tk = C["s24.b"] + 0.6 + 0.3 * k
        E.foco(c, t, tk, 0.4, lambda a, k=k: M.rrect(c, XE + k * 230, 660 + (k % 2) * 40, 200, 140, 26, (E.COR, TINTA, E.mix(E.COR, "#FFFFFF", 0.4))[k], a, shadow=True))
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, sistema=b_sistema, dh=b_dh, exemplo=b_exemplo, diagrama=b_diagrama,
              bolsa=b_bolsa, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
