"""Visual — Estudativo · MAT-MED-002: converter massa e capacidade.
Mesma linguagem da trilha (peças locais Escada, num_un, iguais às de MAT-MED-001): degraus da unidade maior para a menor,
a unidade principal (grama, litro) cheia da cor da matéria, bolinha que pula e deixa arcos numerados, vírgula que anda uma
casa por degrau. A tonelada entra três degraus acima do quilo, com dois degraus sem nome, tracejados.
Peça local nova: garrafa() (recipiente com o nível do líquido). Instantes: cues C[...] e a palavra falada (PW)."""
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
ARQUIVO_FINAL = "estudativo_MAT-MED-002_converter_massa_e_capacidade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("massa", "tonelada", "capacidade", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 750 / 1000 == 0.75 and 7.5 / 2 == 3.75 and 0.3 * 1000 == 300 and 500 / 1000 == 0.5
assert 1.2 * 1000 == 1200 and 800 / 1000 == 0.8 and 2 * 1000 == 2000 and 2.5 * 1000 == 2500 and 2500 * 1000 == 2500000
assert 3.5 * 1000 == 3500 and 3500 / 5 == 700 and 700 * 5 == 3500 and 3.5 / 5 == 0.7

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
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


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


UN_G = ("kg", "hg", "dag", "g", "dg", "cg", "mg")
NOMES_G = ("quilograma", "hectograma", "decagrama", "grama", "decigrama", "centigrama", "miligrama")
ESC_G = Escada(un=UN_G, nomes=NOMES_G)
ESC_T = Escada(un=("t", "", "", "kg", "hg", "dag", "g"), nomes=("tonelada", "", "", "quilograma", "hectograma", "decagrama", "grama"), meio=6)
ESC_L = Escada(x=110, y=340, sw=230, sh=110, base=950, un=("L", "dL", "cL", "mL"), nomes=("litro", "decilitro", "centilitro", "mililitro"), meio=0, size=66)
XN, YN, SN = 1080, 420, 140


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    tq = PW("s01", "Quantos")

    def um():
        E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "750 mL", 240, 300, 160, "g", TINTA, a))
        E.foco(c, t, tq, 0.5, lambda a: E.escreve(c, "=", 900, 300, 160, "g", TINTA, a))
        if t < kb:
            E.foco(c, t, tq + 0.1, 0.5, lambda a: E.escreve(c, "? L", 1060, 300, 160, "g", CINZA, a))
        else:
            E.foco(c, t, kb, 0.4, lambda a: E.escreve(c, "7,5 L", 1060, 300, 160, "g", ERRADO, a))
        E.foco(c, t, ka + 0.3, 0.5, lambda a: garrafa(c, 330, 860, 300, 0.9, a, rotulo="750 mL", size=50))
        tg = PW("s01", "quatro")
        for k in range(4):  # 7,5 L = três garrafas de 2 L cheias e uma com 3/4
            E.foco(c, t, kc + 0.25 * k, 0.4, lambda a, k=k: garrafa(c, 820 + k * 260, 860, 380, 0.9 if k < 3 else 0.9 * 0.75, a, ERRADO))
        E.foco(c, t, tg + 0.6, 0.4, lambda a: centro(c, "7,5 L = quase 4 garrafas de 2 L", 1210, 950, 54, "i", ERRADO, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 280, passo=0.12)
        E.frase(c, t, PW("s02", "converte"), [("converter", "g", 96, COR)] + ps("massa", "i", 88), XE, 430, passo=0.12)
        E.frase(c, t, PW("s02", "capacidade"), ps("e", "i", 88) + [("capacidade", "g", 96, COR)], XE, 570, passo=0.12)
        E.frase(c, t, tb, ps("com a mesma", "i", 84) + [("escada", "g", 88, COR)], XE, 710, passo=0.12)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
ESC_MINI = Escada(x=980, y=520, sw=120, sh=50, base=930, size=44)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 190, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, 140, w, 196, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("a escada", "i", 62)], x + 44, 224)
    E.frase(c, t, C["s03.b"] + 0.3, [("do metro", "g", 62, COR)], x + 44, 300)
    ESC_MINI.degraus(c, t, C["s03.b"] + 0.3, nomes=False)
    td = PW("s03", "Cada")
    ESC_MINI.pulos(c, t, 3, [(td + 0.2, 4)], td - 0.3)
    E.foco(c, t, td, 0.4, lambda a: E.pilula(c, "1 degrau = 1 casa", 1560, 420, 48, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, PW("s03", "Unidade"), 0.4, lambda a: E.pilula(c, "unidade menor → número maior", 1500, 500, 46, "g", fundo=TINTA, a=a, cor=BR))
    E.frase(c, t, PW("s03", "Se"), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54), XE, 1000, "left", 0.12)


# ---------------- massa ----------------
def b_massa(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    tl = [PW("s04", n) for n in ("quilograma", "hectograma", "decagrama")] + [a4] + [PW("s04", n) for n in ("decigrama", "centigrama", "miligrama")]
    t_esc = PW("s04", "meio") - 0.2

    def intro():
        E.frase(c, t, C["s04"] + 0.3, [("massa:", "g", 68, COR)] + ps("o que a balança mede", "i", 62), 1060, 170, "left", 0.1)
        E.frase(c, t, PW("s04", "dia"), ps("no dia a dia,", "i", 60, TINTA2) + [("peso", "g", 62, TINTA2)], 1060, 260, "left", 0.1)
        E.foco(c, t, b4, 0.5, lambda a: E.pilula(c, "os mesmos nomes do metro", 1440, 400, 50, "g", a=a, cor=E.SOBRE))
    if t < C["s05"] + 0.4:
        E.saida(c, t, C["s05"] - 0.1, intro)
    nada = lambda c_, x, y: None
    if t < t_esc + 0.4:
        E.saida(c, t, t_esc - 0.3, lambda: E.foco(c, t, PW("s04", "balança"), 0.5,
                                                  lambda a: E.balanca(c, 560, 620, nada, nada, 0.12 * math.sin(2 * t), a, larg_braco=600)))
    if t < C["s07"] + 0.4:
        E.saida(c, t, C["s07"] - 0.1, lambda: ESC_G.degraus(c, t, [t_esc + 0.12 * i for i in range(7)], tl))
    # s05: quilo e mili continuam valendo mil
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    t_um = PW("s05", "um")
    fase(c, t, a5, c5 - 0.2, lambda: (
        ESC_G.pulos(c, t, 0, [(t_um - 0.6 + 0.45 * k, k + 1) for k in range(3)], a5, dur=0.5),
        E.frase(c, t, a5, [("quilo", "g", 76, COR)] + ps("continua sendo", "i", 68) + [("mil", "g", 76, COR)], 1060, 180, "left", 0.1),
        fcen(c, t, b5, "1 kg = 1.000 g", 1440, 320, 90)))
    t_g = PW("s05", "grama")
    fase(c, t, c5, C["s06"] - 0.1, lambda: (
        ESC_G.pulos(c, t, 3, [(t_g - 0.4 + 0.45 * k, k + 4) for k in range(3)], c5, dur=0.5),
        E.frase(c, t, c5, [("mili", "g", 66, COR)] + ps("continua sendo", "i", 60) + [("milésimo", "g", 66, COR)], 1060, 180, "left", 0.1),
        fcen(c, t, d5, "1 g = 1.000 mg", 1440, 320, 90),
        E.frase(c, t, PW("s05", "doses"), ps("doses de remédio", "i", 56, TINTA2), 1440, 420, "center", 0.1)))
    # s06: queijo e comprimido
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    h1 = PW("s06", "Do")
    hq = [(h1 + 0.7 * k, k + 1) for k in range(3)]
    fase(c, t, C["s06"], c6 - 0.3, lambda: (
        E.frase(c, t, C["s06"] + 0.3, ps("na padaria:", "i", 64) + [("queijo", "g", 66, COR)], 1060, 180, "left", 0.1),
        ESC_G.pulos(c, t, 0, hq, a6, rastro=True),
        num_un(c, t, "3", 0, [(th, k + 1) for k, (th, j) in enumerate(hq)], XN + E.casa(SN), YN, SN,
               [(a6, "kg"), (hq[0][0] + 0.7, "hg"), (hq[1][0] + 0.7, "dag"), (hq[2][0] + 0.7, "g")], t0=a6, zero_esq=True),
        E.foco(c, t, PW("s06", "três"), 0.5, lambda a: E.pilula(c, "3 degraus para baixo", 1420, 540, 54, "g", a=a, cor=E.SOBRE)),
        bola_res(c, t, b6 + 0.2, "300 g", 1690, 780, 140, 76)))
    t_c = PW("s06", "Três")
    hc = [(t_c + 0.7 * k - 0.4, 5 - k) for k in range(3)]
    if t >= c6 - 0.3:
        E.saida(c, t, C["s07"] - 0.1, lambda: (
            E.frase(c, t, c6 - 0.2, ps("um", "i", 64) + [("comprimido", "g", 66, COR)], 1060, 180, "left", 0.1),
            ESC_G.pulos(c, t, 6, hc, c6),
            num_un(c, t, "500", 3, [(th, 2 - k) for k, (th, j) in enumerate(hc)], XN + E.casa(SN), YN, SN,
                   [(c6, "mg"), (hc[0][0] + 0.7, "cg"), (hc[1][0] + 0.7, "dg"), (hc[2][0] + 0.7, "g")], t0=c6),
            E.risco(c, XN + E.casa(SN) * 2.15, YN + 10, XN + E.casa(SN) * 3.85, YN - 100, t, d6, largura=10) if t >= d6 else None,
            E.foco(c, t, t_c, 0.5, lambda a: E.pilula(c, "3 degraus para cima", 1420, 540, 54, "g", fundo=TINTA, a=a, cor=BR)),
            bola_res(c, t, d6 + 0.6, "0,5 g", 1690, 780, 140, 76),
            E.frase(c, t, PW("s06", "meio"), ps("meio grama", "i", 56, TINTA2), 1690, 980, "center", 0.1)))
    if t >= C["s07"]:
        col = ((360, "mg", "remédio", C["s07.a"]), (960, "kg", "gente", C["s07.b"]), (1560, "t", "carga de caminhão", C["s07.c"]))
        E.frase(c, t, C["s07"] + 0.3, ps("pense no", "i", 76) + [("tamanho", "g", 80, COR)], W / 2, 220, "center", 0.12)
        for cx, u, ex, k in col:
            E.foco(c, t, k, 0.5, lambda a, cx=cx, ex=ex: centro(c, ex, cx, 460, 64, "i", TINTA, a))
            E.foco(c, t, k + 0.3, 0.5, lambda a, cx=cx, u=u: (E.bola(c, cx, 680, 140, a=a), centro(c, u, cx, 720, 120, "g", E.SOBRE, a)))


# ---------------- tonelada ----------------
def b_tonelada(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9, e9, f9, g9 = (C[f"s09.{k}"] for k in "abcdefg")
    t3 = PW("s08", "três")

    def esc():
        ESC_T.degraus(c, t, [C["s08"] + 0.2 + 0.12 * i for i in range(7)], [a8, a8 + 0.3, a8 + 0.4, C["s08"] + 0.6] + [C["s08"] + 0.8 + 0.1 * i for i in range(3)],
                      acesos=(0, 1, 2, 3), ta=t3)
        fase(c, t, C["s08"], c8 - 0.3, lambda: (
            E.frase(c, t, PW("s08", "cargas"), ps("cargas pesadas:", "i", 66) + [("tonelada", "g", 72, COR)], 1060, 180, "left", 0.1),
            fcen(c, t, b8, "1 t = 1.000 kg", 1440, 330, 96),
            E.foco(c, t, t3, 0.5, lambda a: E.pilula(c, "3 casas acima do kg", 1440, 470, 54, "g", a=a, cor=E.SOBRE)),
            E.foco(c, t, PW("s08", "como"), 0.5, lambda a: E.pilula(c, "kg: 3 casas acima do g", 1440, 560, 50, "g", fundo=TINTA, a=a, cor=BR))))
        hops = [(b9, 1), (c9, 2), (d9, 3)]
        if t >= c8 - 0.3:
            fase(c, t, c8 - 0.3, f9 - 0.3, lambda: (
                E.frase(c, t, c8 - 0.2, ps("carro pequeno:", "i", 64) + [("quantos kg?", "g", 66, COR)], 1060, 180, "left", 0.1),
                ESC_T.pulos(c, t, 0, hops, c8),
                num_un(c, t, "12", 1, [(b9, 2), (c9, 3), (d9, 4)], XN, YN, SN, [(c8, "t"), (d9 + 0.7, "kg")], t0=c8, some=True),
                E.foco(c, t, a9, 0.5, lambda a: E.pilula(c, "mil: 3 casas →", 1420, 540, 54, "g", a=a, cor=E.SOBRE)),
                bola_res(c, t, e9, "1.200 kg", 1690, 790, 150, 66)))
        if t >= f9 - 0.3:
            tf = PW("s09", "são")
            ESC_T.pulos(c, t, 3, [(tf - 0.3 + 0.45 * k, 2 - k) for k in range(3)], f9 - 0.2, dur=0.5)
            E.frase(c, t, f9 - 0.2, ps("o contrário", "i", 64, TINTA2), 1060, 180, "left", 0.1)
            fcen(c, t, f9, "800 kg", 1440, 360, 120)
            E.foco(c, t, tf, 0.5, lambda a: E.pilula(c, "← 3 casas", 1440, 470, 54, "g", fundo=TINTA, a=a, cor=BR))
            bola_res(c, t, g9 + 0.3, "0,8 t", 1600, 720, 150, 84)
    E.saida(c, t, C["s09.end"] - 0.3, esc)


# ---------------- capacidade ----------------
def b_capacidade(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    if t < b0 + 0.4:
        E.saida(c, t, b0 - 0.3, lambda: (
            E.frase(c, t, C["s10"] + 0.3, [("capacidade:", "g", 80, COR)], W / 2, 220, "center"),
            E.frase(c, t, a0, ps("quanto cabe dentro de um recipiente", "i", 76), W / 2, 330, "center", 0.1),
            E.foco(c, t, a0 + 0.3, 0.5, lambda a: garrafa(c, W / 2, 920, 460, 0.9 * ep(t, a0 + 0.6, 1.4), a))))
    tl = [b0, PW("s10", "decilitro"), PW("s10", "centilitro"), PW("s10", "mililitro")]
    if t >= b0 - 0.3:
        E.saida(c, t, C["s13.end"] - 0.3, lambda: ESC_L.degraus(c, t, [b0 - 0.3 + 0.15 * i for i in range(4)], tl))
    # s11: um litro, mil mililitros
    a1, b1, c1, d1 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    h2 = PW("s11", "descendo")
    hops = [(h2 - 0.3 + 0.7 * k, k + 1) for k in range(3)]
    fase(c, t, a1, C["s12"] - 0.1, lambda: (
        fcen(c, t, a1, "1 L = 1.000 mL", 1460, 230, 100, COR),
        E.frase(c, t, b1, ps("colher de chá", "i", 56) + [("≈ 5 mL", "g", 60)], 1100, 380, "left", 0.1),
        E.frase(c, t, PW("s11", "copo"), ps("copo americano", "i", 56) + [("≈ 190 mL", "g", 60)], 1100, 470, "left", 0.1),
        ESC_L.pulos(c, t, 0, hops, c1),
        num_un(c, t, "2", 1, [(th, j + 1) for th, j in hops], 1150, 720, 130, [(c1, "L")] + [(th + 0.7, ESC_L.un[j]) for th, j in hops], t0=c1, some=True),
        bola_res(c, t, d1 + 0.3, "2.000 mL", 1480, 900, 150, 54)))
    # s12 e s13: 750 mL em litros
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    a3, b3, c3, d3 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    if t >= C["s12"] - 0.1:
        tv = PW("s12", "vírgula")
        E.frase(c, t, a2, ps("750 mL em", "i", 66) + [("litros", "g", 68, COR)], 1100, 200, "left", 0.1)
        ESC_L.pulos(c, t, 3, [(a3, 2), (b3, 1), (c3, 0)], a2)
        num_un(c, t, "750", 3, [(a3, 2), (b3, 1), (c3, 0)], 1180, 430, 140, [(a2, "mL"), (a3 + 0.7, "cL"), (b3 + 0.7, "dL"), (c3 + 0.7, "L")], tv=tv, t0=a2)
        E.foco(c, t, b2, 0.5, lambda a: E.pilula(c, "3 degraus para cima", 1480, 570, 54, "g", fundo=TINTA, a=a, cor=BR))
        E.foco(c, t, c2, 0.5, lambda a: E.pilula(c, "← 3 casas", 1480, 660, 54, "g", fundo=TINTA, a=a, cor=BR))
        bola_res(c, t, d3, "0,75 L", 1480, 850, 120, 70)
        E.frase(c, t, PW("s13", "menos"), ps("menos de 1 litro", "i", 54, CERTO), 1100, 1010, "left", 0.1)


# ---------------- erro ----------------
ESC_E = Escada(x=110, y=380, sw=210, sh=100, base=950, un=("L", "dL", "cL", "mL"), nomes=("litro", "decilitro", "centilitro", "mililitro"), meio=0, size=62)


def b_erro(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    tc = PW("s14", "centímetro")
    certo = t >= d4
    E.frase(c, t, C["s14"] + 0.3, ps("o erro:", "i", 72) + [("parar no 2º degrau", "g", 72, ERRADO)], 110, 170, "left", 0.1)
    ESC_E.degraus(c, t, C["s14"] + 0.1)
    ESC_E.pulos(c, t, 3, [(b4, 2), (b4 + 0.7, 1), (d4, 0)], C["s14"] + 0.5, cor=CERTO if certo else ERRADO)
    E.foco(c, t, tc, 0.5, lambda a: E.escreve(c, "centi: 2 casas", 1050, 330, 66, "g", TINTA2, a))
    E.foco(c, t, b4 + 0.5, 0.5, lambda a: E.escreve(c, "750 mL → 7,5 L", 1050, 450, 76, "g", ERRADO, a * (1 - 0.6 * ep(t, c4, 0.4))))
    if t >= c4:
        E.risco(c, 1040, 470, 1650, 400, t, c4, largura=12)
    E.foco(c, t, c4, 0.5, lambda a: E.escreve(c, "mili = milésimo", 1050, 600, 76, "g", COR, a))
    E.foco(c, t, d4, 0.5, lambda a: E.pilula(c, "3 degraus, 3 casas", 1340, 690, 56, "g", fundo=CERTO, a=a, cor=BR))
    fcen(c, t, e4 - 1.6, "L > mL", 1240, 870, 90)
    E.foco(c, t, e4, 0.5, lambda a: (E.escreve(c, "0,75 L", 1480, 870, 96, "g", CERTO, a)))
    E.frase(c, t, e4 + 0.6, ps("o número fica bem", "i", 56) + [("menor", "g", 58, CERTO)], 1050, 990, "left", 0.1)


# ---------------- atalho (palco escuro) ----------------
def pulo_mil(c, t, t0, x0, x1, y, cor=None, rot="× 1.000", alto=110):
    """arco de x0 a x1 por cima, com a pílula da conta no alto"""
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    pts = []
    for n in range(25):
        u = p * n / 24
        pts.append((lerp(x0, x1, u), y - math.sin(math.pi * u) * alto))
    path = skia.Path(); path.moveTo(*pts[0])
    for q in pts[1:]:
        path.lineTo(*q)
    c.drawPath(path, M.paint(cor or CLARO, 1.0, stroke=6, cap_round=True))
    if p >= 1:
        M.arrow(c, pts[-3][0], pts[-3][1], x1, y, cor or CLARO, 1.0, 6, 20)
        E.pilula(c, rot, (x0 + x1) / 2, y - alto - 30, 44, "g", a=ep(t, t0 + 0.5, 0.3), cor=E.SOBRE)


def b_atalho(c, t, C, b):
    palco(c, t)
    a5, b5, c5, d5 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]

    def lista():
        E.frase(c, t, C["s15"] + 0.3, ps("agora, o atalho:", "i", 70, CLARO), W / 2, 150, "center", 0.1)
        E.frase(c, t, a5, ps("pule de", "i", 96, CLARO) + [("mil em mil", "g", 100, BR)], W / 2, 280, "center", 0.12)
        xs = (300, 760, 1220, 1680)
        tt = [PW("s15", n) for n in ("tonelada", "quilo", "grama", "miligrama")]
        for x, u, k in zip(xs, ("t", "kg", "g", "mg"), tt):
            E.foco(c, t, k, 0.5, lambda a, x=x, u=u: centro(c, u, x, 600, 130, "g", BR, a))
        for k in range(3):
            pulo_mil(c, t, d5 + 0.25 * k, xs[k] + 90, xs[k + 1] - 90, 510)
        xl = (760, 1220)
        tl = [PW("s15", "litro"), PW("s15", "mililitro")]
        for x, u, k in zip(xl, ("L", "mL"), tl):
            E.foco(c, t, k, 0.5, lambda a, x=x, u=u: centro(c, u, x, 900, 130, "g", BR, a))
        pulo_mil(c, t, d5 + 0.75, xl[0] + 90, xl[1] - 110, 810)
        E.foco(c, t, PW("s15", "três"), 0.5, lambda a: E.pilula(c, "sempre 3 casas", 1600, 870, 56, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s16"] - 0.1, lista)
    if C["s16"] <= t < C["s17"] + 0.4:
        a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]

        def conta():
            E.frase(c, t, a6, [("2,5 t", "g", 92, BR)] + ps("em gramas?", "i", 88, CLARO), W / 2, 260, "center", 0.12)
            fcen(c, t, a6 + 0.6, "2,5 t", 260, 640, 96, BR)
            tp = PW("s16", "pulos")
            pulo_mil(c, t, tp, 400, 560, 560)
            fcen(c, t, b6, "2.500 kg", 780, 640, 96, BR)
            pulo_mil(c, t, b6 + 0.5, 1020, 1170, 560)
            E.foco(c, t, c6, 0.5, lambda a: E.formula(c, "2.500.000 g", 1500, 640, 96, "g", CLARO, a, "center"))
            E.frase(c, t, tp - 0.4, ps("dois pulos de mil", "i", 70, CLARO), W / 2, 860, "center", 0.1)
        E.saida(c, t, C["s17"] - 0.1, conta)
    if t >= C["s17"]:
        a7, b7 = C["s17.a"], C["s17.b"]
        esc = Escada(x=180, y=380, sw=160, sh=50, base=800, un=UN_G, nomes=NOMES_G, size=50)
        E.frase(c, t, C["s17"] + 0.2, ps("os degraus do meio", "i", 80, CLARO) + [("quase não aparecem", "g", 84, BR)], W / 2, 220, "center", 0.12)
        esc.degraus(c, t, C["s17"] + 0.3, escuro=True, nomes=False)
        for i in (1, 2, 4, 5):  # os degraus do meio apagam
            q = ep(t, a7, 0.6)
            if q > 0:
                M.rrect(c, esc.x + i * esc.sw + 2, esc.topo(i) - 2, esc.sw - 4, esc.base - esc.topo(i) + 4, 12, "#07070F", 0.7 * q)
        E.foco(c, t, b7, 0.5, lambda a: E.selo(c, 1330, 470, 46, False, a))
        E.frase(c, t, b7 + 0.1, ps("com", "i", 64, CLARO) + [("cL", "g", 70, BR)] + ps("ou", "i", 64, CLARO) + [("dag", "g", 70, BR)], 1400, 495, "left", 0.1)
        E.frase(c, t, PW("s17", "volte"), ps("volte à escada e", "i", 72, CLARO) + [("conte os degraus", "g", 76, BR)], W / 2, 920, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s18.a"] - 1.0, ps("um caminhão leva", "i", 76), XE, 350, passo=0.1)
    E.foco(c, t, C["s18.a"], 0.5, lambda a: E.escreve(c, "3,5 t", XE, 500, 130, "g", COR, a))
    E.frase(c, t, C["s18.a"] + 1.4, ps("de arroz", "i", 72), XE + 420, 500, passo=0.1)
    E.frase(c, t, C["s18.b"] - 0.6, ps("em pacotes de", "i", 72), XE, 650, passo=0.1)
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.escreve(c, "5 kg", XE + 470, 650, 130, "g", COR, a))
    E.frase(c, t, C["s18.c"], ps("quantos", "i", 92) + [("pacotes?", "g", 96, COR)], XE, 860, passo=0.12)
    E.relogio(c, t, C["s19.a"], 1560, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    hs = [a0 - 0.1 + 0.7 * k for k in range(3)]

    def um():
        E.frase(c, t, C["s20"] + 0.8, ps("primeiro,", "i", 70) + [("a mesma unidade", "g", 74, COR)], W / 2, 170, "center", 0.12)
        num_un(c, t, "35", 1, [(h, k + 2) for k, h in enumerate(hs)], 360, 380, 130, [(a0 - 0.3, "t"), (hs[-1] + 0.7, "kg")], t0=a0 - 0.3, some=True)
        E.foco(c, t, a0, 0.4, lambda a: E.pilula(c, "t → kg: 3 casas →", 560, 500, 50, "g", a=a, cor=E.SOBRE))
        fcen(c, t, c0, "3.500 ÷ 5", 1450, 380, 110)
        bola_res(c, t, d0, "700", 1450, 610, 130, 90)
        E.foco(c, t, d0 + 0.3, 0.4, lambda a: centro(c, "pacotes", 1450, 800, 56, "i", COR, a))
        fcen(c, t, e0, "700 × 5 = 3.500 kg", W / 2, 960, 90, CERTO)
    E.saida(c, t, C["s21"] - 0.1, um)
    if t >= C["s21"]:
        a1, b1 = C["s21.a"], C["s21.b"]
        E.frase(c, t, C["s21"] + 0.3, ps("quem divide", "i", 76) + [("sem converter", "g", 80, ERRADO)], W / 2, 240, "center", 0.12)
        fcen(c, t, a1, "3,5 ÷ 5 = 0,7", W / 2, 500, 130, ERRADO)
        E.frase(c, t, a1 + 1.0, ps("pacote", "i", 70, ERRADO), W / 2 + 470, 500, "left", 0.1)
        E.frase(c, t, PW("s21", "Menos"), ps("menos de 1 pacote num caminhão?", "i", 70), W / 2, 700, "center", 0.1)
        E.foco(c, t, b1, 0.5, lambda a: E.pilula(c, "a unidade ficou para trás", W / 2, 860, 70, "g", fundo=ERRADO, a=a, cor=BR))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s22.a", "a escada", "é a mesma"), ("s22.b", "quilo e mili:", "sempre mil"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 60, a=a), centro(c, str(i + 1), 300, y - 7, 68, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 92) + [(l2, "g", 96, COR)], 400, y, "left", 0.12)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a3, b3 = C["s23.a"], C["s23.b"]
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 80), XE, 240, passo=0.12)
    E.frase(c, t, a3, ps("prefixos como", "i", 84) + [("giga", "g", 110, COR)] + ps("e", "i", 84) + [("nano", "g", 110, COR)], XE, 410, passo=0.12)
    E.frase(c, t, b3, [("polegadas", "g", 84)] + ps("e", "i", 80) + [("milhas", "g", 84)], XE, 560, passo=0.12)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, massa=b_massa, tonelada=b_tonelada, capacidade=b_capacidade, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
