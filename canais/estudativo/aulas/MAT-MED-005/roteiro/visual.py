"""Visual — Estudativo · MAT-MED-005: converter volume e litros.
Mesma linguagem da trilha (peças locais Escada e num_un, iguais às de MAT-MED-001): aqui é a escada do VOLUME (m³, dm³, cm³),
em que cada degrau vale mil, então a vírgula salta TRÊS casas por degrau; embaixo do dm³ e do cm³ aparecem o litro e o mL.
Peças locais novas: cubinho() e caixa() (cubinhos que enchem a caixa fileira a fileira, camada a camada, na mesma perspectiva
cavaleira de E.paralelepipedo), garrafa() (igual à de MAT-MED-002) e seringa(). Instantes: cues C[...] e a palavra falada (PW)."""
import json
import math
import unicodedata
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Medidas e Unidades")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-MED-005_converter_volume_e_litros.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("volume", "dm3", "litro", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 3 * 2 * 1 == 6 and 3 * 2 * 2 == 12 and 10 * 10 * 10 == 1000 and 2 * 1000 == 2000 and 500 / 1000 == 0.5
assert 5 * 1000 == 5000 and abs(0.3 * 1000 - 300) < 1e-9 and 3.5 * 1000 == 3500 and 900 / 1000 == 0.9 and 2 * 100 == 200

_TEMPOS = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))


def _n(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", s.lower()) if ch.isalnum())


def PW(sid, palavra, n=1):
    """instante em que a voz diz a n-ésima `palavra` da cena sid"""
    for s in _TEMPOS["scenes"]:
        if s["id"] == sid:
            k = 0
            for tk in s["tokens"]:
                if _n(tk["disp"]) == _n(palavra):
                    k += 1
                    if k == n:
                        return s["start"] + tk["t0"]
    raise KeyError((sid, palavra, n))


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo (palavra com ² ou ³ vai na grotesca: a serifada não tem o expoente)"""
    return [(w, "g" if any(ch in w for ch in "²³") else est, size * (0.92 if any(ch in w for ch in "²³") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_res(c, t, t0, s, cx, cy, r=140, size=84, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    """desenha fn de t0 até t1 e some desfocando"""
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


# ================= a ESCADA das unidades (mesma peça em toda a trilha Medidas e Unidades) =================
UN = ("km", "hm", "dam", "m", "dm", "cm", "mm")
NOMES = ("quilômetro", "hectômetro", "decâmetro", "metro", "decímetro", "centímetro", "milímetro")


class Escada:
    """degraus descendo da esquerda para a direita. (x, y) = canto de cima do 1º degrau; sw, sh = largura e altura do degrau.
    base = onde todos os degraus apoiam. meio = índice da unidade principal (degrau cheio da cor da matéria)."""

    def __init__(s, x=110, y=300, sw=186, sh=78, base=950, un=UN, nomes=NOMES, meio=3, size=60):
        s.x, s.y, s.sw, s.sh, s.base, s.un, s.nomes, s.meio, s.size = x, y, sw, sh, base, un, nomes, meio, size
        s.n = len(un)

    def cx(s, i):
        return s.x + (i + 0.5) * s.sw

    def topo(s, i):
        return s.y + i * s.sh

    def ponto(s, i):
        """onde a bolinha fica em cima do degrau i (i pode ser fracionário)"""
        k = min(max(i, 0), s.n - 1)
        return s.cx(k), s.y + k * s.sh - 34

    def degraus(s, c, t, td, tl=None, a=1.0, acesos=(), ta=None, escuro=False, nomes=True):
        """td = instante de entrada de cada degrau (lista) ou do primeiro (número: entram em fila).
        tl = instante do rótulo de cada degrau (lista; padrão = o do degrau). acesos = degraus do caminho, em tom claro, a partir de ta."""
        if a <= 0:
            return
        for i in range(s.n):
            ti = td[i] if isinstance(td, (list, tuple)) else td + 0.09 * i
            q = ep(t, ti, 0.45)
            if q <= 0:
                continue
            top, x0 = s.topo(i), s.x + i * s.sw
            hh = (s.base - top) * ease_io(prog(t, ti, 0.45))
            meio = i == s.meio
            if s.un[i] == "":  # degrau sem nome: só o contorno tracejado
                r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + 4, s.base - hh, s.sw - 8, hh), 12, 12)
                pt = M.paint(CLARO if escuro else TINTA2, 0.55 * q * a, stroke=3)
                pt.setPathEffect(skia.DashPathEffect.Make([12, 10], 0))
                c.drawRRect(r, pt)
                continue
            if escuro:
                fundo, borda, tinta = (E.COR, CLARO, BR) if meio else ("#FFFFFF", CLARO, BR)
                alfa = 1.0 if meio else 0.07
            else:
                fundo, borda, tinta = (E.COR, E.COR, E.SOBRE) if meio else ("#FFFFFF", TINTA2, TINTA)
                alfa = 1.0
            acende = ep(t, ta, 0.4) if (i in acesos and ta is not None and not meio) else 0.0
            M.rrect(c, x0 + 4, s.base - hh, s.sw - 8, hh, 12, fundo, alfa * q * a)
            if acende > 0:
                M.rrect(c, x0 + 4, s.base - hh, s.sw - 8, hh, 12, E.COR, (0.32 if escuro else 0.16) * acende * q * a)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + 4, s.base - hh, s.sw - 8, hh), 12, 12), M.paint(borda, q * a, stroke=3))
            tli = tl[i] if tl else ti + 0.2
            E.foco(c, t, tli, 0.45, lambda b, i=i, top=top, tinta=tinta: centro(c, s.un[i], s.cx(i), top + s.size * 1.12, s.size, "g", tinta, b * a))
            if nomes:
                cor_n = (BR if meio else CLARO) if escuro else (E.SOBRE if meio else TINTA2)
                E.foco(c, t, tli + 0.1, 0.45, lambda b, i=i, top=top, cor_n=cor_n: centro(c, s.nomes[i], s.cx(i), top + s.size * 1.12 + 50, 40, "i", cor_n, b * a))

    def pulos(s, c, t, i0, hops, t0, a=1.0, cor=None, dur=0.7, rastro=True, escuro=False):
        """bolinha que aparece no degrau i0 em t0 e pula: hops = [(instante, degrau de destino), ...].
        Cada pulo deixa um arco com o número dele (1, 2, 3...): é a contagem de degraus = casas da vírgula."""
        if a <= 0 or t < t0:
            return
        cor = cor or E.COR
        atual, pulo = float(i0), 0.0
        de = i0
        for k, (th, j) in enumerate(hops):
            q = prog(t, th, dur)
            if q <= 0:
                break
            if rastro:
                s._arco(c, de, j, min(1.0, q * 1.25), k + 1, cor, a, escuro)
            if q < 1:
                e = ease_io(q)
                atual, pulo = lerp(de, j, e), math.sin(math.pi * q) * 70
                break
            atual, de = float(j), j
        x0, y0 = s.ponto(math.floor(atual))
        x1, y1 = s.ponto(math.ceil(atual))
        f = atual - math.floor(atual)
        E.bola(c, lerp(x0, x1, f), lerp(y0, y1, f) - pulo, 30 * ease_back(prog(t, t0, 0.5)), cor, a)

    def _arco(s, c, i, j, p, k, cor, a, escuro):
        (xa, ya), (xb, yb) = s.ponto(i), s.ponto(j)
        ya, yb = ya - 36, yb - 36
        alto = 64
        mx, my = (xa + xb) / 2, min(ya, yb) - alto
        pts = [(lerp(lerp(xa, mx, u), lerp(mx, xb, u), u), lerp(lerp(ya, my, u), lerp(my, yb, u), u)) for u in [p * n / 24 for n in range(25)]]
        path = skia.Path()
        path.moveTo(*pts[0])
        for x_, y_ in pts[1:]:
            path.lineTo(x_, y_)
        tinta = CLARO if escuro else cor
        c.drawPath(path, M.paint(tinta, 0.75 * a, stroke=5, cap_round=True))
        if p >= 1:
            (xp, yp), (xe, ye) = pts[-2], pts[-1]
            ang = math.atan2(ye - yp, xe - xp)
            h = skia.Path()
            h.moveTo(xe + math.cos(ang) * 3, ye + math.sin(ang) * 3)
            h.lineTo(xe - 18 * math.cos(ang - 0.5), ye - 18 * math.sin(ang - 0.5))
            h.lineTo(xe - 18 * math.cos(ang + 0.5), ye - 18 * math.sin(ang + 0.5))
            h.close()
            c.drawPath(h, M.paint(tinta, 0.75 * a))
            xm, ym = pts[12]
            c.drawCircle(xm, ym - 4, 24, M.paint(tinta, a))
            centro(c, str(k), xm, ym + 11, 32, "g", "#07070F" if escuro else E.SOBRE, a)


def posicao(t, pos, saltos, dur=0.7):
    """posição da vírgula no instante t (a mesma conta de E.anda)"""
    atual, fim = float(pos), pos
    for t0, novo in saltos:
        q = ease_io(prog(t, t0, dur))
        if q <= 0:
            break
        if q >= 1:
            atual, fim = float(novo), novo
            continue
        return lerp(fim, novo, q)
    return atual


def num_un(c, t, dig, pos, saltos, x, y, size, unidades, cor=None, tv=None, some=False, t0=None, cor_un=None, zero_esq=False):
    """número com a vírgula que anda (E.anda) e a unidade logo depois dele, que troca a cada salto.
    unidades = [(instante, "km"), ...]; a primeira entra em t0. Devolve px (centro de cada casa).
    zero_esq = o 0 antes da vírgula de "0,3" (dig "3", pos 0), que some quando a vírgula começa a andar."""
    if t0 is not None and t < t0:
        return None
    a0 = ep(t, t0, 0.5) if t0 is not None else 1.0
    c.saveLayer(None, M.paint("#000000", a0)) if a0 < 1 else None
    px = E.anda(c, t, dig, pos, saltos, x, y, size, cor=cor, tv=tv, some=some)
    cl = E.casa(size)
    if zero_esq:
        z = 1 - ep(t, saltos[0][0], 0.3) if saltos else 1.0
        if z > 0:
            E.centro(c, "0", px(-1), y, size, "g", cor or TINTA, z)
    ncas = max(len(dig), math.ceil(posicao(t, pos, saltos) - 1e-6))
    xu = x + ncas * cl + size * 0.3
    for k, (tu, u) in enumerate(unidades):
        prox = unidades[k + 1][0] if k + 1 < len(unidades) else None
        if t < tu:
            break
        if prox is not None and t >= prox + 0.35:
            continue
        sai = 1 - ep(t, prox, 0.35) if prox is not None else 1.0
        E.foco(c, t, tu, 0.4, lambda b, u=u: E.escreve(c, u, xu, y, size * 0.72, "g", cor_un or COR, b * sai))
    if a0 < 1:
        c.restore()
    return px




# ---------------- peças desta aula ----------------
def garrafa(c, cx, base, h, nivel, a=1.0, cor=None, rotulo=None, size=44):
    """garrafa de pé com a base em (cx, base): corpo, ombro, gargalo e tampa; nivel 0..1 = quanto do corpo está cheio"""
    if a <= 0:
        return
    w, hc = h * 0.36, h * 0.66
    gw = w * 0.38
    p = skia.Path()
    p.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, base - hc, w, hc), w * 0.18, w * 0.18))
    om = skia.Path()
    om.moveTo(cx - w / 2 + w * 0.06, base - hc + w * 0.1)
    om.cubicTo(cx - w / 2, base - hc - h * 0.12, cx - gw / 2, base - hc - h * 0.1, cx - gw / 2, base - h * 0.86)
    om.lineTo(cx + gw / 2, base - h * 0.86)
    om.cubicTo(cx + gw / 2, base - hc - h * 0.1, cx + w / 2, base - hc - h * 0.12, cx + w / 2 - w * 0.06, base - hc + w * 0.1)
    om.close()
    corpo = skia.Op(p, om, skia.PathOp.kUnion_PathOp) or p
    c.drawPath(corpo, M.paint("#FFFFFF", a))
    if nivel > 0:
        c.save(); c.clipPath(corpo, doAntiAlias=True)
        c.drawRect(skia.Rect.MakeXYWH(cx - w, base - hc * nivel, 2 * w, hc * nivel), M.paint(cor or E.COR, 0.85 * a))
        c.restore()
    c.drawPath(corpo, M.paint(TINTA, a, stroke=4))
    M.rrect(c, cx - gw / 2 - 4, base - h, gw + 8, h * 0.14, 6, TINTA, a)
    if rotulo:
        centro(c, rotulo, cx, base + size + 14, size, "g", TINTA, a)




def seringa(c, x, y, w, h, nivel, a=1.0):
    """seringa deitada: corpo com marcas, líquido até `nivel`, êmbolo à esquerda e agulha à direita. (x, y) = canto de cima do corpo"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 10, "#FFFFFF", a)
    c.drawRect(skia.Rect.MakeXYWH(x + w * (1 - nivel), y + 6, w * nivel - 6, h - 12), M.paint(E.COR, 0.8 * a))
    for k in range(1, 10):
        M.line(c, x + w * k / 10, y, x + w * k / 10, y + h * (0.4 if k % 5 else 0.6), TINTA2, a, 3)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 10, 10), M.paint(TINTA, a, stroke=4))
    M.line(c, x - 120, y + h / 2, x, y + h / 2, TINTA, a, 12)
    M.rrect(c, x - 140, y - 10, 20, h + 20, 6, TINTA, a)
    M.line(c, x + w, y + h / 2, x + w + 120, y + h / 2, TINTA2, a, 4)


# ---------------- cubinhos ----------------
KX, KY = 0.394, -0.308  # a profundidade na perspectiva cavaleira (a mesma de E.paralelepipedo)


def cubinho(c, x, y, s, a=1.0, cor=None):
    """cubinho cheio de aresta s: (x, y) = canto de baixo à esquerda da face da frente"""
    if a <= 0:
        return
    cor = cor or E.COR
    dx, dy = KX * s, KY * s
    br = M.paint("#FFFFFF", 0.9 * a, stroke=2)

    def poli(pts, tinta):
        p = skia.Path(); p.moveTo(*pts[0])
        for q in pts[1:]:
            p.lineTo(*q)
        p.close()
        c.drawPath(p, M.paint(tinta, a)); c.drawPath(p, br)
    poli([(x, y - s), (x + s, y - s), (x + s + dx, y - s + dy), (x + dx, y - s + dy)], E.mix(cor, "#FFFFFF", 0.35))
    poli([(x + s, y), (x + s + dx, y + dy), (x + s + dx, y - s + dy), (x + s, y - s)], E.mix(cor, "#000000", 0.25))
    poli([(x, y), (x + s, y), (x + s, y - s), (x, y - s)], cor)


def caixa(c, t, cols, fil, cam, x, y, s, tf, a=1.0, cor=None):
    """cubinhos de aresta s enchendo uma caixa de cols x fil x cam: tf(camada, fileira) = instante em que a fileira entra.
    (x, y) = canto de baixo à esquerda da frente. A fileira 0 é a de trás"""
    if a <= 0:
        return
    for k in range(cam):
        for j in range(fil):  # de trás para a frente
            t0 = tf(k, j)
            if t0 is None:
                continue
            for i in range(cols):
                q = ep(t, t0 + 0.1 * i, 0.35)
                if q <= 0:
                    continue
                prof = fil - 1 - j
                cx = x + i * s + KX * s * prof
                cy = y - k * s + KY * s * prof - (1 - ease_io(q)) * 40
                cubinho(c, cx, cy, s, a * q, cor)


def arame(c, x, y, w, d, h, a=1.0, cor=None):
    """contorno de uma caixa w x d x h (px) na mesma perspectiva, com as arestas de trás tracejadas"""
    if a <= 0:
        return
    dx, dy = KX * d, KY * d
    pt = M.paint(cor or TINTA, a, stroke=4)
    tr = M.paint(cor or TINTA2, 0.7 * a, stroke=3)
    tr.setPathEffect(skia.DashPathEffect.Make([12, 10], 0))
    c.drawLine(x, y, x + dx, y + dy, tr); c.drawLine(x + dx, y + dy, x + w + dx, y + dy, tr); c.drawLine(x + dx, y + dy, x + dx, y + dy - h, tr)
    for (x0, y0, x1, y1) in ((x, y, x + w, y), (x + w, y, x + w, y - h), (x + w, y - h, x, y - h), (x, y - h, x, y),
                             (x, y - h, x + dx, y - h + dy), (x + w, y - h, x + w + dx, y - h + dy), (x + w, y, x + w + dx, y + dy),
                             (x + dx, y - h + dy, x + w + dx, y - h + dy), (x + w + dx, y - h + dy, x + w + dx, y + dy)):
        c.drawLine(x0, y0, x1, y1, pt)


def cubo_grade(c, x, y, L, n=10, a=1.0, faces=(1.0, 1.0, 1.0)):
    """cubo de aresta L com a grade de n x n em cada face visível (frente, topo, lado); faces = opacidade da grade em cada uma"""
    if a <= 0:
        return
    cubinho(c, x, y, L, a, E.mix(E.COR, "#FFFFFF", 0.55))
    dx, dy = KX * L, KY * L
    for k in range(1, n):
        f = k / n
        if faces[0] > 0:
            M.line(c, x + L * f, y, x + L * f, y - L, "#FFFFFF", a * faces[0], 2)
            M.line(c, x, y - L * f, x + L, y - L * f, "#FFFFFF", a * faces[0], 2)
        if faces[1] > 0:
            M.line(c, x + L * f, y - L, x + L * f + dx, y - L + dy, "#FFFFFF", a * faces[1], 2)
            M.line(c, x + dx * f, y - L + dy * f, x + L + dx * f, y - L + dy * f, "#FFFFFF", a * faces[1], 2)
        if faces[2] > 0:
            M.line(c, x + L + dx * f, y + dy * f, x + L + dx * f, y - L + dy * f, "#FFFFFF", a * faces[2], 2)
            M.line(c, x + L, y - L * f, x + L + dx, y - L * f + dy, "#FFFFFF", a * faces[2], 2)


ESC_V = Escada(x=110, y=380, sw=290, sh=150, base=950, un=("m³", "dm³", "cm³"), nomes=("", "", ""), meio=0, size=80)


def litros_na_escada(c, t, t1, t2):
    """embaixo do dm³ e do cm³: o litro e o mililitro"""
    for i, s, t0 in ((1, "= 1 L", t1), (2, "= 1 mL", t2)):
        E.foco(c, t, t0, 0.5, lambda a, i=i, s=s: centro(c, s, ESC_V.cx(i), ESC_V.topo(i) + 160, 50, "g", COR, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    tq = PW("s01", "Quantos")

    def um():
        E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "2 m³ =", 160, 300, 150, "g", TINTA, a))
        if t < kb:
            E.foco(c, t, tq, 0.5, lambda a: E.escreve(c, "? L", 690, 300, 150, "g", CINZA, a))
        elif t < kd:
            E.foco(c, t, kb, 0.4, lambda a: E.escreve(c, "2 L", 690, 300, 150, "g", ERRADO, a))
        else:
            E.foco(c, t, kd, 0.4, lambda a: E.escreve(c, "2.000 L", 690, 300, 150, "g", COR, a))
        s = 190
        E.foco(c, t, ka + 0.3, 0.6, lambda a: caixa(c, t, 2, 1, 1, 1080, 820, s, lambda k, j: -1e9, a))
        E.frase(c, t, ka + 0.3, ps("caixa-d'água de 2 m³", "i", 54, TINTA2), 1300, 940, "center", 0.06)
        E.foco(c, t, kc, 0.5, lambda a: garrafa(c, 640, 820, 300, 0.85, a * (1 - 0.7 * ep(t, kd, 0.4)), ERRADO, "2 L?", 56))
        E.frase(c, t, PW("s01", "garrafa"), ps("do tamanho de uma garrafa", "i", 56, ERRADO), 640, 960, "center", 0.08)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 280, passo=0.12)
        E.frase(c, t, PW("s02", "entender"), ps("entender o que é", "i", 84) + [("volume", "g", 92, COR)], XE, 430, passo=0.12)
        E.frase(c, t, PW("s02", "converter"), [("converter", "g", 88, COR)] + ps("m³ em litros", "i", 84), XE, 570, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "na área, 2 direções:", "1 degrau = × 100"), ("s03.c", "capacidade:", "1 L = 1.000 mL"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(420, 700, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, PW("s03", "Se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1000, "left", 0.12)


# ---------------- o que é volume ----------------
def b_volume(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    if t < C["s05"] + 0.4:
        def um():
            E.frase(c, t, PW("s04", "área"), [("área:", "g", 66, TINTA)] + ps("cobre um piso", "i", 64), 200, 230, "left", 0.1)
            s = 110
            for j in range(2):
                for i in range(3):
                    E.foco(c, t, PW("s04", "piso.") + 0.08 * (j * 3 + i), 0.4, lambda q, i=i, j=j: chao(c, 230 + i * s + KX * s * (1 - j), 620 + KY * s * (1 - j), s, q))
            E.frase(c, t, a4, [("volume:", "g", 66, COR)] + ps("enche um espaço", "i", 64), 1020, 230, "left", 0.1)
            arame(c, 1060, 760, 3 * 130, 2 * 130, 2 * 130, ep(t, a4 + 0.3, 0.5))
            caixa(c, t, 3, 2, 2, 1060, 760, 130, lambda k, j: b4 + 0.3 + k * 0.6 + j * 0.3)
            for k, w_ in enumerate(("caixa,", "piscina,", "quarto")):
                E.foco(c, t, PW("s04", w_.strip(",")), 0.4, lambda a, k=k, w_=w_: E.escreve(c, w_, 1020 + k * 250, 330, 56, "i", TINTA2, a))
            E.frase(c, t, PW("s04", "contar"), ps("contar", "i", 64) + [("cubinhos iguais", "g", 66, COR)], 1300, 960, "center", 0.1)
        E.saida(c, t, C["s05"] - 0.1, um)
    if C["s05"] <= t < C["s06"] + 0.4:
        a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]

        def dois():
            E.cubo(c, t, a5, 220, 820, 420, "1 m", todas=True, tm=PW("s05", "comprimento,"))
            E.foco(c, t, a5 + 0.4, 0.5, lambda a: centro(c, "1 m³", 220 + 210 + 50, 680, 110, "g", COR, a))
            E.frase(c, t, a5 - 0.2, ps("o", "i", 76) + [("metro cúbico", "g", 80, COR)], 1060, 260, "left", 0.1)
            E.frase(c, t, b5, ps("comprimento, largura e altura:", "i", 56), 1060, 360, "left", 0.08)
            E.frase(c, t, b5 + 1.0, [("1 m", "g", 60)] + ps("cada", "i", 56), 1060, 440, "left", 0.08)
            E.foco(c, t, c5, 0.5, lambda a: (E.escreve(c, "m", 1060, 640, 130, "g", TINTA, a), E.escreve(c, "³", 1160, 640, 130, "g", COR, a)))
            E.frase(c, t, PW("s05", "mesmo"), ps("como em", "i", 64, TINTA2) + [("10³", "g", 60, TINTA2)], 1300, 630, "left", 0.1)
        E.saida(c, t, C["s06"] - 0.1, dois)
    if t >= C["s06"]:
        a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
        a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
        s, x, y = 160, 260, 820
        E.frase(c, t, C["s06"] + 0.3, ps("uma caixa de", "i", 70) + [("3 m × 2 m × 1 m", "g", 74, COR)], W / 2, 170, "center", 0.1)
        alto = 2 if t >= a7 else 1
        arame(c, x, y, 3 * s, 2 * s, alto * s, ep(t, a6, 0.5))
        tfil = (b6, PW("s06", "duas"))
        caixa(c, t, 3, 2, 2, x, y, s, lambda k, j: (tfil[j] if k == 0 else (b7 + 0.3 * j)))
        E.foco(c, t, a6 + 0.6, 0.4, lambda a: centro(c, "3 m", x + 1.5 * s, y + 70, 54, "g", TINTA2, a))
        E.foco(c, t, a6 + 0.9, 0.4, lambda a: E.escreve(c, "2 m", x + 3 * s + KX * s + 30, y + KY * s + 20, 54, "g", TINTA2, a))
        E.foco(c, t, a6 + 1.2, 0.4, lambda a: E.escreve(c, "1 m" if t < a7 else "2 m", x - 120, y - s / 2 * alto + 20, 54, "g", TINTA2 if t < a7 else COR, a))
        E.foco(c, t, b6 + 0.4, 0.4, lambda a: E.escreve(c, "3 por fileira, 2 fileiras", 1080, 360, 56, "i", TINTA, a))
        fcen(c, t, c6, "3 × 2 = 6", 1330, 480, 90)
        E.foco(c, t, d6, 0.4, lambda a: E.escreve(c, "1 camada só", 1080, 600, 60, "i", TINTA, a * (1 - ep(t, a7, 0.3))))
        bola_res(c, t, e6, "6 m³", 1330, 780, 120, 76) if t < a7 else None
        E.foco(c, t, b7, 0.4, lambda a: E.escreve(c, "2 camadas de 6", 1080, 600, 60, "g", COR, a))
        bola_res(c, t, c7, "12 m³", 1330, 780, 130, 76)


def chao(c, x, y, s, a):
    """um ladrilho do piso, deitado na perspectiva: (x, y) = canto da frente à esquerda"""
    if a <= 0:
        return
    dx, dy = KX * s, KY * s
    p = skia.Path(); p.moveTo(x, y); p.lineTo(x + s, y); p.lineTo(x + s + dx, y + dy); p.lineTo(x + dx, y + dy); p.close()
    c.drawPath(p, M.paint(E.mix(E.COR, "#FFFFFF", 0.35), a)); c.drawPath(p, M.paint("#FFFFFF", a, stroke=3))


# ---------------- metro cúbico em decímetro cúbico ----------------
def b_dm3(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, a8 - 0.6, ps("de", "i", 70) + [("m³", "g", 74, COR)] + ps("para", "i", 70) + [("dm³", "g", 74, COR)], 1040, 200, "left", 0.1)
        E.frase(c, t, b8 - 0.4, [("1 dm = 10 cm", "g", 66)], 1040, 300, "left", 0.08)
        E.frase(c, t, b8 - 0.2, ps("a décima parte do metro", "i", 54, TINTA2), 1040, 380, "left", 0.08)
        L, x, y = 440, 220, 860
        fx = (ep(t, c8, 0.4), ep(t, PW("s08", "largura"), 0.4), ep(t, PW("s08", "altura."), 0.4))
        E.foco(c, t, C["s08"] + 0.2, 0.5, lambda a: cubo_grade(c, x, y, L, 10, a, (max(fx[0], fx[2]), fx[1], max(fx[1], fx[2]))))
        E.foco(c, t, c8, 0.4, lambda a: centro(c, "10", x + L / 2, y + 70, 60, "g", COR, a))
        E.foco(c, t, PW("s08", "largura"), 0.4, lambda a: E.escreve(c, "10", x + L + KX * L / 2 + 20, y + KY * L / 2 + 20, 60, "g", COR, a))
        E.foco(c, t, PW("s08", "altura."), 0.4, lambda a: E.escreve(c, "10", x - 90, y - L / 2 + 20, 60, "g", COR, a))
        fcen(c, t, a9, "10 × 10 × 10 = 1.000", 1380, 480, 90)
        E.foco(c, t, b9, 0.5, lambda a: E.pilula(c, "1 m³ = 1.000 dm³", 1380, 620, 70, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, c9 - 0.3, ps("cada degrau vale", "i", 60) + [("10³ = 1.000", "g", 64, COR)], 1380, 780, "center", 0.1)
        E.foco(c, t, d9, 0.5, lambda a: E.pilula(c, "3 casas da vírgula", 1380, 900, 62, "g", fundo=TINTA, a=a, cor=BR))
    E.saida(c, t, C["s10"] - 0.1, um)
    if t < C["s10"] - 0.1:
        return
    a0, b0 = C["s10.a"], C["s10.b"]
    h = PW("s10", "três")
    ESC_V.degraus(c, t, C["s10"] - 0.1, acesos=(1,), ta=h)
    E.frase(c, t, a0, ps("2 m³ em", "i", 64) + [("dm³", "g", 66, COR)], 1100, 200, "left", 0.1)
    ESC_V.pulos(c, t, 0, [(h, 1)], a0)
    num_un(c, t, "2", 1, [(h, 4)], 1100, 430, 120, [(a0, "m³"), (h + 0.7, "dm³")], t0=a0, some=True)
    E.foco(c, t, h, 0.5, lambda a: E.pilula(c, "1 degrau = 3 casas →", 1500, 570, 56, "g", a=a, cor=E.SOBRE))
    bola_res(c, t, b0, "2.000 dm³", 1500, 800, 170, 60)


# ---------------- a ponte com o litro ----------------
def b_litro(c, t, C, b):
    a1, b1 = C["s11.a"], C["s11.b"]
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    if t < C["s13"] + 0.4:
        def ponte():
            E.frase(c, t, C["s11"] + 0.3, ps("a ponte para o", "i", 70) + [("litro", "g", 74, COR)], 200, 200, "left", 0.1)
            E.foco(c, t, a1, 0.5, lambda a: E.pilula(c, "1 dm³ = 1 L", 520, 340, 96, "g", a=a, cor=E.SOBRE))
            L, x, y = 300, 300, 880
            E.foco(c, t, b1, 0.5, lambda a: arame(c, x, y, L, L, L, a))
            nivel = ease_io(prog(t, PW("s11", "cheio"), 1.2))
            if nivel > 0:
                c.save()
                c.translate(0, 0)
                cubinho(c, x, y, L * 0.999, 0.75, E.mix(E.COR, "#FFFFFF", 0.15)) if nivel >= 1 else \
                    caixa_agua(c, x, y, L, nivel)
                c.restore()
            E.foco(c, t, b1 + 0.4, 0.4, lambda a: centro(c, "10 cm", x + L / 2, y + 70, 54, "g", TINTA2, a))
            E.foco(c, t, b1 + 0.6, 0.4, lambda a: E.escreve(c, "10 cm", x - 170, y - L / 2 + 20, 54, "g", TINTA2, a))
            E.foco(c, t, PW("s11", "guarda"), 0.4, lambda a: E.escreve(c, "1 L", x + L + 160, y - L / 2 + 30, 90, "g", COR, a))
            # s12
            fcen(c, t, a2, "1 m³ = 1.000 L", 1400, 340, 90, COR)
            fcen(c, t, b2, "2 m³ = 2.000 dm³", 1400, 500, 80)
            bola_res(c, t, c2, "2.000 L", 1400, 690, 130, 64)
            E.frase(c, t, PW("s12", "conta"), ps("conta de água:", "i", 56, TINTA2) + [("1 m³ = 1.000 L", "g", 60, TINTA2)], 1400, 920, "center", 0.08)
        E.saida(c, t, C["s13"] - 0.1, ponte)
    if t < C["s13"] - 0.1:
        return
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    ESC_V.degraus(c, t, C["s13"] - 0.1, acesos=(0, 1) if t < C["s14"] else (1, 2), ta=b3)
    litros_na_escada(c, t, C["s13"] + 0.4, PW("s14", "mililitros."))

    def volta():
        E.frase(c, t, C["s13"] + 0.2, ps("o caminho de volta:", "i", 60, TINTA2), 1100, 200, "left", 0.1)
        ESC_V.pulos(c, t, 1, [(b3, 0)], a3)
        px = num_un(c, t, "500", 3, [(b3, 0)], 1180, 430, 140, [(a3, "L"), (PW("s13", "São"), "dm³"), (b3 + 0.7, "m³")], t0=a3, tv=b3 - 0.4)
        E.foco(c, t, b3, 0.5, lambda a: E.pilula(c, "← 3 casas", 1500, 570, 56, "g", fundo=TINTA, a=a, cor=BR))
        if px and t >= c3:
            E.risco(c, px(1) - 40, 440, px(2) + 40, 330, t, c3, largura=10)
        bola_res(c, t, c3, "0,5 m³", 1500, 800, 140, 70)
    E.saida(c, t, C["s14"] - 0.1, volta)
    if t < C["s14"]:
        return
    ESC_V.pulos(c, t, 1, [(a4 + 0.2, 2)], C["s14"] + 0.2)
    E.frase(c, t, C["s14"] + 0.3, ps("descendo mais um degrau", "i", 60, TINTA2), 1100, 200, "left", 0.1)
    fcen(c, t, a4 + 0.6, "1 dm³ = 1.000 cm³", 1480, 330, 76)
    fcen(c, t, PW("s14", "litro"), "1 L = 1.000 mL", 1480, 450, 76)
    E.foco(c, t, b4, 0.5, lambda a: E.pilula(c, "1 cm³ = 1 mL", 1480, 590, 78, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, c4, 0.5, lambda a: seringa(c, 1240, 760, 420, 90, 0.5 * ep(t, c4 + 0.3, 0.8), a))
    E.frase(c, t, d4, [("5 mL = 5 cm³", "g", 64, COR)], 1480, 960, "center", 0.1)


def caixa_agua(c, x, y, L, nivel):
    """água subindo dentro do cubo de 1 dm³"""
    h = L * nivel
    dx, dy = KX * L, KY * L
    p = skia.Path(); p.moveTo(x, y); p.lineTo(x + L, y); p.lineTo(x + L + dx, y + dy); p.lineTo(x + L + dx, y + dy - h)
    p.lineTo(x + dx + L, y - h + dy); p.lineTo(x + dx, y - h + dy); p.lineTo(x, y - h); p.close()
    c.drawPath(p, M.paint(E.COR, 0.55))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    E.frase(c, t, C["s15"] + 0.3, ps("cuidado:", "i", 70) + [("a regra da área no volume", "g", 72, ERRADO)], W / 2, 180, "center", 0.1)
    E.foco(c, t, PW("s15", "anda"), 0.4, lambda a: E.pilula(c, "só 2 casas", 470, 300, 54, "g", fundo=ERRADO, a=a, cor=BR))
    E.foco(c, t, b5, 0.5, lambda a: E.escreve(c, "2 m³ = 200 dm³", 160, 450, 100, "g", ERRADO, a))
    if t >= d5:
        E.risco(c, 150, 470, 900, 350, t, d5, largura=12)
    L, x, y = 360, 1200, 800
    E.foco(c, t, c5 - 0.3, 0.5, lambda a: cubinho(c, x, y, L, a, E.mix(E.COR, "#FFFFFF", 0.55)))
    for k, (pal, x0, y0, x1, y1, tx, ty) in enumerate((("comprimento,", x, y + 50, x + L, y + 50, x + L / 2 - 120, y + 120),
                                                        ("largura", x + L + 30, y + 10, x + L + KX * L + 30, y + KY * L + 10, x + L + KX * L + 50, y + KY * L / 2 + 40),
                                                        ("altura.", x - 50, y, x - 50, y - L, x - 280, y - L / 2))):
        tk = PW("s15", pal)
        E.foco(c, t, tk, 0.4, lambda a, x0=x0, y0=y0, x1=x1, y1=y1, tx=tx, ty=ty, pal=pal: (M.arrow(c, x0, y0, x1, y1, COR, a, 6, 20),
                                                                                         E.escreve(c, pal.strip(",."), tx, ty, 50, "i", COR, a)))
    E.foco(c, t, c5, 0.5, lambda a: E.escreve(c, "3 direções", 160, 620, 80, "g", COR, a))
    E.foco(c, t, d5, 0.5, lambda a: E.pilula(c, "1 degrau = 1.000, não 100", 560, 760, 60, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, e5 - 1.6, [("200 dm³", "g", 66, ERRADO)] + ps("seriam só", "i", 60) + [("200 L", "g", 66, ERRADO)], 160, 920, "left", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]

    def um():
        E.frase(c, t, C["s16"] + 0.3, ps("agora, o atalho:", "i", 70, CLARO), W / 2, 160, "center", 0.1)
        E.frase(c, t, a6, [("m³ → litro:", "g", 110, BR)] + ps("vezes", "i", 100, CLARO) + [("mil", "g", 110, BR)], W / 2, 330, "center", 0.12)
        fcen(c, t, b6, "5 m³ = 5.000 L", W / 2, 560, 110, BR)
        fcen(c, t, c6, "0,3 m³ = 300 L", W / 2, 760, 110, CLARO)
    E.saida(c, t, C["s17"] - 0.1, um)
    if t < C["s17"]:
        return
    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]
    E.frase(c, t, a7 - 0.2, ps("funciona porque", "i", 70, CLARO), W / 2, 220, "center", 0.1)
    fcen(c, t, a7, "1 m³ = 1.000 dm³", 720, 400, 90, BR)
    fcen(c, t, PW("s17", "cada"), "= 1.000 L", 1400, 400, 90, CLARO)
    E.foco(c, t, b7, 0.5, lambda a: E.selo(c, 520, 640, 50, False, a))
    E.frase(c, t, b7 + 0.1, ps("não compensa com", "i", 72, CLARO) + [("cm³", "g", 80, BR)], 600, 665, "left", 0.1)
    E.foco(c, t, c7, 0.5, lambda a: E.pilula(c, "cm³ = mL", W / 2, 860, 96, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    E.frase(c, t, C["s18"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a8 - 0.8, ps("um reservatório de", "i", 70), XE, 350, passo=0.1)
    E.foco(c, t, a8, 0.5, lambda a: E.escreve(c, "3,5 m³", XE + 560, 350, 100, "g", COR, a))
    E.frase(c, t, b8, ps("quantos", "i", 68) + [("litros?", "g", 72, COR)], XE, 450, passo=0.1)
    E.frase(c, t, c8 - 0.6, ps("uma lata de", "i", 70), XE, 640, passo=0.1)
    E.foco(c, t, c8, 0.5, lambda a: E.escreve(c, "900 cm³", XE + 360, 640, 100, "g", COR, a))
    E.frase(c, t, d8, ps("quantos", "i", 68) + [("litros?", "g", 72, COR)], XE, 740, passo=0.1)
    E.relogio(c, t, C["s19.a"], 1560, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a0, b0 = C["s20.a"], C["s20.b"]
    a1, b1, c1 = C["s21.a"], C["s21.b"], C["s21.c"]
    ESC_V.degraus(c, t, C["s20"] - 0.1, acesos=(0, 1) if t < C["s21"] else (1, 2), ta=a0 if t < C["s21"] else b1)
    litros_na_escada(c, t, C["s20"] + 0.2, C["s20"] + 0.4)

    def um():
        E.frase(c, t, C["s20"] + 0.3, ps("reservatório:", "i", 60) + [("3,5 m³ em L", "g", 64, COR)], 1100, 200, "left", 0.1)
        ESC_V.pulos(c, t, 0, [(a0, 1)], C["s20"] + 0.5)
        num_un(c, t, "35", 1, [(a0, 4)], 1150, 430, 140, [(C["s20"] + 0.5, "m³"), (a0 + 0.7, "L")], t0=C["s20"] + 0.5, some=True)
        E.foco(c, t, a0, 0.5, lambda a: E.pilula(c, "3 casas →", 1500, 570, 56, "g", a=a, cor=E.SOBRE))
        bola_res(c, t, b0, "3.500 L", 1500, 790, 150, 66)
        E.frase(c, t, PW("s20", "São"), ps("3 caixas de mil e mais meia", "i", 52, TINTA2), 1500, 1010, "center", 0.08)
    E.saida(c, t, C["s21"] - 0.1, um)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.3, ps("lata:", "i", 60) + [("900 cm³ = 900 mL", "g", 64, COR)], 1100, 200, "left", 0.1)
    ESC_V.pulos(c, t, 2, [(b1, 1)], a1)
    px = num_un(c, t, "900", 3, [(b1, 0)], 1180, 430, 140, [(a1, "mL"), (b1 + 0.7, "L")], t0=a1, tv=b1 - 0.4)
    E.foco(c, t, b1, 0.5, lambda a: E.pilula(c, "← 3 casas", 1500, 570, 56, "g", fundo=TINTA, a=a, cor=BR))
    if px and t >= c1:
        E.risco(c, px(1) - 40, 440, px(2) + 40, 330, t, c1, largura=10)
    bola_res(c, t, c1, "0,9 L", 1500, 790, 140, 76)
    E.frase(c, t, PW("s21", "Quase"), ps("quase 1 litro: uma lata grande", "i", 52, CERTO), 1500, 1010, "center", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s22.a", "no volume,", "1 degrau = × 1.000"), ("s22.b", "e", "1 dm³ = 1 L"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 60, a=a), centro(c, str(i + 1), 300, y - 7, 68, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 88) + [(l2, "g", 92, COR)], 400, y, "left", 0.12)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a3, b3 = C["s23.a"], C["s23.b"]
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 80), XE, 240, passo=0.12)
    E.frase(c, t, a3, ps("a unidade que não anda de 10 em 10:", "i", 64) + [("o tempo", "g", 92, COR)], XE, 400, passo=0.1)
    E.frase(c, t, b3, ps("ler", "i", 72) + [("2,2 h", "g", 84, COR)] + ps("sem cair na armadilha", "i", 72), XE, 550, passo=0.1)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, volume=b_volume, dm3=b_dm3, litro=b_litro, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
