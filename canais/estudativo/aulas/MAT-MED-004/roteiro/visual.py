"""Visual — Estudativo · MAT-MED-004: converter área.
Mesma linguagem da trilha (peças locais Escada e num_un, iguais às de MAT-MED-001): aqui é a escada da ÁREA, de km² a mm²,
com o m² no meio; cada degrau vale cem, então a vírgula salta DUAS casas por degrau (arco numerado = degraus, pílula = casas).
Peças locais novas: grade_q() (quadradinhos que entram fileira a fileira) e metro_cm() (o metro quadrado com as 100 fileiras
de 100 quadradinhos de 1 cm²). Instantes: cues C[...] e a palavra falada (PW)."""
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
ARQUIVO_FINAL = "estudativo_MAT-MED-004_converter_area.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("area", "cm2", "hectare", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 100 * 100 == 10000 and 3 * 2 == 6 and 3 * 10000 == 30000 and 50000 / 10000 == 5 and 3 * 100 == 300
assert 2.5 * 10000 == 25000 and 1000 * 1000 == 1000000 and 1000000 / 10000 == 100 and 30000 / 300 == 100
assert 3.2 * 10000 == 32000 and 2500 / 10000 == 0.25 and 1000 ** 2 == 10 ** 6

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
UN_A = ("km²", "hm²", "dam²", "m²", "dm²", "cm²", "mm²")
ESC_A = Escada(un=UN_A, nomes=("", "hectare", "", "", "", "", ""))
XN, YN, SN = 1060, 420, 118


def grade_q(c, t, t0, cols, lins, x, y, s, cor=None, dur=1.2, a=1.0, ti=None):
    """quadradinhos de lado s a partir do canto (x, y), entrando fileira a fileira em `dur` segundos.
    ti = instante de entrada de cada fileira (lista), no lugar de dur"""
    if a <= 0:
        return
    for r in range(lins):
        for k in range(cols):
            i = r * cols + k
            t_ = (ti[r] + 0.12 * k) if ti else t0 + dur * i / max(1, cols * lins)
            q = ep(t, t_, 0.3) * a
            if q > 0:
                M.rrect(c, x + k * s + 3, y + r * s + 3, s - 6, s - 6, s * 0.1, cor or E.COR, q)


def cota_h(c, t, t0, txt, x0, x1, y, cor=None, size=50):
    def f(a):
        M.line(c, x0, y, x1, y, cor or TINTA2, a, 3)
        M.line(c, x0, y - 12, x0, y + 12, cor or TINTA2, a, 3)
        M.line(c, x1, y - 12, x1, y + 12, cor or TINTA2, a, 3)
        centro(c, txt, (x0 + x1) / 2, y - 22, size, "g", cor or TINTA2, a)
    E.foco(c, t, t0, 0.5, f)


def cota_v(c, t, t0, txt, x, y0, y1, cor=None, size=50):
    def f(a):
        M.line(c, x, y0, x, y1, cor or TINTA2, a, 3)
        M.line(c, x - 12, y0, x + 12, y0, cor or TINTA2, a, 3)
        M.line(c, x - 12, y1, x + 12, y1, cor or TINTA2, a, 3)
        E.escreve(c, txt, x - 24 - E.larg(txt, "g", size), (y0 + y1) / 2 + size * 0.36, size, "g", cor or TINTA2, a)
    E.foco(c, t, t0, 0.5, f)


def metro_cm(c, x, y, L, fil=0.0, linha1=0.0, cor_linha=None, a=1.0, grade=1.0):
    """o metro quadrado: quadrado de lado L com a grade de 100 x 100 quadradinhos de 1 cm².
    linha1 = 0..1, a primeira fileira de 100 se enchendo; fil = 0..100, quantas fileiras cheias (de cima para baixo)"""
    if a <= 0:
        return
    M.rrect(c, x, y, L, L, 4, "#FFFFFF", a)
    d = L / 100
    if fil > 0:
        c.drawRect(skia.Rect.MakeXYWH(x, y, L, d * fil), M.paint(E.COR, 0.85 * a))
    if linha1 > 0:
        c.drawRect(skia.Rect.MakeXYWH(x, y, L * linha1, d), M.paint(cor_linha or E.COR, a))
    if grade > 0:
        for k in range(1, 100):
            M.line(c, x + k * d, y, x + k * d, y + L, FIO, 0.55 * a * grade, 1)
            M.line(c, x, y + k * d, x + L, y + k * d, FIO, 0.55 * a * grade, 1)
    c.drawRect(skia.Rect.MakeXYWH(x, y, L, L), M.paint(TINTA, a, stroke=4))


def campo(c, x, y, w, h, a=1.0):
    """campo de futebol visto de cima"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 6, "#3FA45B", a)
    br = M.paint("#FFFFFF", a, stroke=4)
    c.drawRect(skia.Rect.MakeXYWH(x + 8, y + 8, w - 16, h - 16), br)
    c.drawLine(x + w / 2, y + 8, x + w / 2, y + h - 8, br)
    c.drawCircle(x + w / 2, y + h / 2, h * 0.16, br)
    c.drawRect(skia.Rect.MakeXYWH(x + 8, y + h * 0.3, w * 0.12, h * 0.4), br)
    c.drawRect(skia.Rect.MakeXYWH(x + w - 8 - w * 0.12, y + h * 0.3, w * 0.12, h * 0.4), br)


def casas(c, t, t0, txt, cx, cy, escuro=False, cor=None, size=52):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, txt, cx, cy, size, "g", fundo=cor or (E.COR if not escuro else E.COR), a=a, cor=BR))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "1 m² = ", 140, 330, 140, "g", TINTA, a))
        if t < kb:
            E.foco(c, t, PW("s01", "quantos"), 0.5, lambda a: E.escreve(c, "? cm²", 600, 330, 140, "g", CINZA, a))
        elif t < kc:
            E.foco(c, t, kb, 0.4, lambda a: E.escreve(c, "100 cm²", 600, 330, 140, "g", ERRADO, a))
        else:
            E.foco(c, t, kc, 0.4, lambda a: E.escreve(c, "10.000 cm²", 600, 330, 140, "g", COR, a))
        if kb <= t < kc + 0.3:
            E.risco(c, 590, 350, 1150, 230, t, PW("s01", "errou"), largura=14)
        L = 560
        q1 = ep(t, kb, 0.9)
        fil = 100 * ease_io(prog(t, kc, 1.2))
        E.foco(c, t, ka + 0.6, 0.5, lambda a: metro_cm(c, 1240, 380, L, fil, q1, ERRADO if t < kc else E.COR, a))
        E.foco(c, t, ka + 0.9, 0.5, lambda a: centro(c, "1 m", 1240 + L / 2, 360, 52, "g", TINTA2, a))
        E.foco(c, t, kb + 0.4, 0.4, lambda a: E.escreve(c, "100 = uma fileira só", 160, 560, 60, "i", ERRADO, a * (1 - ep(t, kc, 0.3))))
        E.foco(c, t, kc + 0.5, 0.4, lambda a: E.escreve(c, "100 fileiras de 100", 160, 560, 64, "g", COR, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 280, passo=0.12)
        E.frase(c, t, PW("s02", "entender"), ps("entender o que é", "i", 84) + [("área", "g", 92, COR)], XE, 430, passo=0.12)
        E.frase(c, t, PW("s02", "converter"), [("converter", "g", 88, COR)] + ps("m² e hectares", "i", 84), XE, 570, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "a escada do metro", "1 degrau = 1 casa"), ("s03.c", "o quadrado de um número", "10² = 10 × 10 = 100"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.foco(c, t, C[k] + 0.3 if i == 0 else PW("s03", "dez"), 0.5, lambda a, l2=l2, y=y: E.escreve(c, l2, x + 44, y + 160, 60, "g", COR, a))
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(420, 700, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, PW("s03", "Se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1000, "left", 0.12)


# ---------------- o que é área ----------------
def b_area(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    if t < C["s05"] + 0.4:
        def um():
            E.frase(c, t, PW("s04", "Comprimento"), [("comprimento:", "g", 66, TINTA)] + ps("uma linha", "i", 64), 200, 230, "left", 0.1)
            p = ep(t, a4, 0.7)
            if p > 0:
                M.line(c, 200, 340, lerp(200, 800, p), 340, E.COR, 1.0, 10)
            E.frase(c, t, b4, [("área:", "g", 66, COR)] + ps("uma superfície", "i", 64), 1000, 230, "left", 0.1)
            E.foco(c, t, b4 + 0.3, 0.5, lambda a: M.rrect(c, 1000, 300, 600, 400, 8, E.mix(E.COR, "#FFFFFF", 0.82), a, stroke=4, stroke_color=TINTA))
            for k, w_ in enumerate(("piso,", "parede,", "terreno")):
                E.foco(c, t, PW("s04", w_.strip(",")), 0.4, lambda a, k=k, w_=w_: E.escreve(c, w_, 200 + k * 230, 520, 60, "i", TINTA2, a))
            grade_q(c, t, c4, 6, 4, 1000, 300, 100, dur=1.6)
            E.frase(c, t, PW("s04", "contar"), ps("contar", "i", 64) + [("quadradinhos iguais", "g", 66, COR)], 1300, 820, "center", 0.1)
        E.saida(c, t, C["s05"] - 0.1, um)
    if C["s05"] <= t < C["s06"] + 0.4:
        a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]

        def dois():
            x, y, L = 220, 300, 500
            E.foco(c, t, a5, 0.5, lambda a: M.rrect(c, x, y, L, L, 8, E.COR, a))
            E.foco(c, t, a5 + 0.3, 0.5, lambda a: centro(c, "1 m²", x + L / 2, y + L / 2 + 40, 130, "g", BR, a))
            cota_h(c, t, b5 + 0.6, "1 m", x, x + L, y - 30)
            cota_v(c, t, b5 + 1.2, "1 m", x - 30, y, y + L)
            E.frase(c, t, a5 - 0.3, ps("o", "i", 76) + [("metro quadrado", "g", 80, COR)], 1000, 260, "left", 0.1)
            E.frase(c, t, b5, ps("um quadrado de", "i", 60) + [("1 m", "g", 62)] + ps("de lado", "i", 60), 1000, 360, "left", 0.1)
            E.foco(c, t, c5, 0.5, lambda a: (E.escreve(c, "m", 1000, 540, 130, "g", TINTA, a), E.escreve(c, "²", 1100, 540, 130, "g", COR, a)))
            E.frase(c, t, PW("s05", "mesmo"), ps("como em", "i", 64, TINTA2) + [("10²", "g", 60, TINTA2)], 1240, 530, "left", 0.1)
            E.foco(c, t, d5, 0.5, lambda a: M.rrect(c, 1000, 690, 60, 60, 4, E.COR, a))
            E.frase(c, t, d5, [("1 cm²:", "g", 64, COR)] + ps("centímetro quadrado", "i", 60), 1090, 745, "left", 0.1)
            E.frase(c, t, PW("s05", "unha"), ps("do tamanho de uma unha", "i", 56, TINTA2), 1090, 830, "left", 0.1)
        E.saida(c, t, C["s06"] - 0.1, dois)
    if t >= C["s06"]:
        a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
        x, y, s = 300, 360, 170
        E.frase(c, t, C["s06"] + 0.3, ps("um quarto de", "i", 70) + [("3 m por 2 m", "g", 74, COR)], W / 2, 190, "center", 0.1)
        E.foco(c, t, a6, 0.5, lambda a: M.rrect(c, x, y, 3 * s, 2 * s, 6, "#FFFFFF", a, stroke=4, stroke_color=TINTA))
        cota_h(c, t, a6 + 0.3, "3 m", x, x + 3 * s, y - 30)
        cota_v(c, t, a6 + 0.8, "2 m", x - 30, y, y + 2 * s)
        grade_q(c, t, 0, 3, 2, x, y, s, ti=[b6, c6])
        E.foco(c, t, b6 + 0.3, 0.4, lambda a: E.escreve(c, "3 em cada fileira", 960, 420, 60, "i", TINTA, a))
        E.foco(c, t, c6 + 0.3, 0.4, lambda a: E.escreve(c, "2 fileiras", 960, 520, 60, "i", TINTA, a))
        fcen(c, t, d6, "3 × 2 = 6", 1200, 690, 100)
        bola_res(c, t, e6, "6 m²", 1520, 880, 130, 80)


# ---------------- metro quadrado em centímetro quadrado ----------------
def b_cm2(c, t, C, b):
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    L, x, y = 560, 200, 330

    def quadro():
        q1 = ep(t, c7, 1.0)
        fil = 1 + 99 * ease_io(prog(t, d7, 1.4)) if t >= d7 else 0
        E.foco(c, t, a7, 0.5, lambda a: metro_cm(c, x, y, L, fil, q1, None, a, grade=ep(t, b7, 0.6)))
        cota_h(c, t, b7, "1 m = 100 cm", x, x + L, y - 30)
        E.frase(c, t, C["s07"] + 0.2, ps("e em", "i", 70) + [("cm²?", "g", 74, COR)], 1000, 230, "left", 0.1)
        E.foco(c, t, c7 + 0.3, 0.4, lambda a: E.escreve(c, "100 em cada fileira", 1000, 400, 60, "i", TINTA, a))
        E.foco(c, t, d7 + 0.3, 0.4, lambda a: E.escreve(c, "100 fileiras", 1000, 490, 60, "i", TINTA, a))
        fcen(c, t, a8, "100 × 100 = 10.000", 1340, 640, 90)
        E.foco(c, t, b8, 0.5, lambda a: E.pilula(c, "1 m² = 10.000 cm²", 1340, 770, 70, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, PW("s08", "comprimento,"), ps("comprimento:", "i", 56, TINTA2) + [("× 100", "g", 60, TINTA2)], 1000, 900, "left", 0.1)
        E.frase(c, t, PW("s08", "área,", 1), ps("área:", "i", 56) + [("× 100²", "g", 62, COR)], 1000, 990, "left", 0.1)
    E.saida(c, t, C["s09"] - 0.1, quadro)
    if t < C["s09"] - 0.1:
        return
    a9, b9 = C["s09.a"], C["s09.b"]
    a0, b0, c0, d0 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    ESC_A.degraus(c, t, C["s09"] - 0.1, acesos=(3, 4, 5), ta=b9)
    fase(c, t, C["s09"], a0 - 0.2, lambda: (
        E.frase(c, t, C["s09"] + 0.2, ps("a escada da", "i", 64) + [("área", "g", 66, COR)], 1060, 180, "left", 0.1),
        E.foco(c, t, a9, 0.5, lambda a: E.pilula(c, "1 degrau = × 100", 1420, 320, 58, "g", a=a, cor=E.SOBRE)),
        E.foco(c, t, PW("s09", "duas"), 0.5, lambda a: E.pilula(c, "= 2 casas", 1420, 420, 58, "g", a=a, cor=E.SOBRE)),
        ESC_A.pulos(c, t, 3, [(b9, 4), (b9 + 0.7, 5)], C["s09"] + 0.4),
        E.foco(c, t, PW("s09", "quatro"), 0.5, lambda a: E.pilula(c, "2 degraus = 4 casas", 1420, 540, 58, "g", fundo=TINTA, a=a, cor=BR))))
    h1 = PW("s10", "Quatro")
    fase(c, t, a0 - 0.2, c0 - 0.3, lambda: (
        E.frase(c, t, a0, ps("3 m² em", "i", 64) + [("cm²", "g", 66, COR)], 1060, 180, "left", 0.1),
        ESC_A.pulos(c, t, 3, [(h1, 4), (h1 + 0.7, 5)], a0),
        num_un(c, t, "3", 1, [(h1, 3), (h1 + 0.7, 5)], XN, YN, SN, [(a0, "m²"), (h1 + 0.7, "dm²"), (h1 + 1.4, "cm²")], t0=a0, some=True),
        casas(c, t, h1, "4 casas →", 1420, 540),
        bola_res(c, t, b0, "30.000 cm²", 1680, 800, 175, 48)))
    h2 = PW("s10", "Quatro", 2)
    if t >= c0 - 0.3:
        E.frase(c, t, c0 - 0.2, ps("o contrário:", "i", 64, TINTA2), 1060, 180, "left", 0.1)
        ESC_A.pulos(c, t, 5, [(h2, 4), (h2 + 0.7, 3)], c0)
        px = num_un(c, t, "50000", 5, [(h2, 3), (h2 + 0.7, 1)], XN, YN, SN, [(c0, "cm²"), (h2 + 0.7, "dm²"), (h2 + 1.4, "m²")], t0=c0, tv=h2 - 0.4)
        casas(c, t, h2, "← 4 casas", 1420, 540, cor=TINTA)
        if px and t >= d0:
            E.risco(c, px(1) - 40, YN + 10, px(4) + 40, YN - 100, t, d0, largura=10)
        bola_res(c, t, d0, "5 m²", 1660, 800, 140, 80)


# ---------------- hectare ----------------
def b_hectare(c, t, C, b):
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    x, y, L = 280, 330, 500

    def um():
        E.frase(c, t, PW("s11", "campo,"), ps("no campo:", "i", 70) + [("o hectare", "g", 76, COR)], 200, 200, "left", 0.1)
        E.foco(c, t, b1, 0.5, lambda a: M.rrect(c, x, y, L, L, 6, E.mix(E.COR, "#FFFFFF", 0.8), a, stroke=4, stroke_color=TINTA))
        E.foco(c, t, b1 + 0.2, 0.5, lambda a: centro(c, "1 ha", x + L / 2, y + L / 2 + 40, 120, "g", COR, a))
        cota_h(c, t, PW("s11", "cem"), "100 m", x, x + L, y - 30)
        cota_v(c, t, PW("s11", "cem") + 0.3, "100 m", x - 30, y, y + L, size=44)
        E.foco(c, t, c1, 0.5, lambda a: campo(c, 900, 420, 340, 220, a))
        E.frase(c, t, c1 + 0.2, ps("um pouco maior que", "i", 52, TINTA2), 1070, 720, "center", 0.08)
        E.frase(c, t, c1 + 0.6, ps("um campo de futebol", "i", 52, TINTA2), 1070, 790, "center", 0.08)
    E.saida(c, t, C["s12"] + 0.6, um) if t < C["s12"] + 1.0 else None
    if t >= C["s12"]:
        E.foco(c, t, C["s12"] + 0.4, 0.5, lambda a: (M.rrect(c, x, y, L, L, 6, E.mix(E.COR, "#FFFFFF", 0.8), a, stroke=4, stroke_color=TINTA)))
        grade_q(c, t, PW("s12", "cem"), 10, 10, x, y, L / 10, dur=1.5)
        E.foco(c, t, PW("s12", "cem") + 0.2, 0.4, lambda a: centro(c, "100 × 100", x + L / 2, y - 30, 56, "g", TINTA2, a))
        E.foco(c, t, a2, 0.5, lambda a: E.pilula(c, "1 ha = 10.000 m²", x + L / 2, y + L + 70, 60, "g", a=a, cor=E.SOBRE))
        if t < C["s13"] + 0.4:
            E.saida(c, t, C["s13"] - 0.1, lambda: (
                fcen(c, t, b2, "2,5 ha = 2,5 × 10.000", 1290, 300, 80),
                casas(c, t, PW("s12", "Quatro"), "4 casas →", 1290, 430),
                num_un(c, t, "25", 1, [(PW("s12", "Quatro") + 0.2, 5)], 1000, 640, 130, [(b2, "ha"), (PW("s12", "Quatro") + 0.9, "m²")], t0=b2 + 0.3, some=True),
                bola_res(c, t, c2, "25.000 m²", 1290, 850, 150, 56)))
    if t >= C["s13"]:
        a3, b3 = C["s13.a"], C["s13.b"]
        E.frase(c, t, C["s13"] + 0.2, ps("e o", "i", 64) + [("km²?", "g", 70, COR)], 1000, 250, "left", 0.1)
        E.frase(c, t, PW("s13", "quadrado", 2), ps("quadrado de", "i", 56) + [("1.000 m", "g", 60)] + ps("de lado", "i", 56), 1000, 350, "left", 0.1)
        fcen(c, t, a3, "1.000 × 1.000 = 1.000.000 m²", 1360, 520, 70)
        fcen(c, t, PW("s13", "hectares"), "1.000.000 ÷ 10.000", 1360, 680, 76, TINTA2)
        bola_res(c, t, b3, "100 ha", 1360, 860, 130, 70)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    E.frase(c, t, C["s14"] + 0.3, ps("o erro:", "i", 70) + [("a escada do comprimento na área", "g", 70, ERRADO)], W / 2, 180, "center", 0.1)
    E.foco(c, t, PW("s14", "anda"), 0.4, lambda a: E.pilula(c, "só 2 casas", 520, 300, 54, "g", fundo=ERRADO, a=a, cor=BR))
    E.foco(c, t, b4, 0.5, lambda a: E.escreve(c, "3 m² = 300 cm²", 200, 450, 100, "g", ERRADO, a))
    if t >= d4:
        E.risco(c, 190, 470, 950, 350, t, d4, largura=12)
    E.foco(c, t, c4, 0.5, lambda a: E.escreve(c, "1 m² já tem 10.000 cm²", 200, 620, 70, "g", COR, a))
    E.foco(c, t, d4, 0.5, lambda a: E.pilula(c, "100 vezes menor", 520, 740, 60, "g", fundo=ERRADO, a=a, cor=BR))
    L = 520
    q1 = ep(t, b4 + 0.4, 0.8)
    fil = 100 * ease_io(prog(t, e4, 1.4))
    E.foco(c, t, PW("s14", "pessoa"), 0.5, lambda a: metro_cm(c, 1230, 330, L, fil, q1, ERRADO, a))
    E.foco(c, t, b4 + 1.0, 0.4, lambda a: E.escreve(c, "1 fileira só", 1230, 920, 56, "i", ERRADO, a * (1 - ep(t, e4, 0.3))))
    E.foco(c, t, e4 + 0.4, 0.4, lambda a: E.escreve(c, "100 fileiras de 100", 1230, 920, 60, "g", COR, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a5, b5, c5, d5 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]

    def um():
        E.frase(c, t, C["s15"] + 0.3, ps("agora, o atalho:", "i", 70, CLARO), W / 2, 150, "center", 0.1)
        E.frase(c, t, a5, ps("eleve o fator", "i", 92, CLARO) + [("ao quadrado", "g", 96, BR)], W / 2, 290, "center", 0.12)
        linhas = ((PW("s15", "Do"), "m → cm", b5, "× 100", c5, "100² = 10.000", 470),
                  (PW("s15", "Do", 2), "km → m", PW("s15", "mil", 2), "× 1.000", d5, "1.000² = 1.000.000", 700))
        E.foco(c, t, PW("s15", "Do") - 0.2, 0.4, lambda a: (centro(c, "comprimento", 760, 400, 50, "i", CLARO, a), centro(c, "área", 1360, 400, 50, "i", CLARO, a)))
        for t1, par, t2, f1, t3, f2, y in linhas:
            E.foco(c, t, t1, 0.5, lambda a, par=par, y=y: E.escreve(c, par, 160, y, 76, "g", BR, a))
            E.foco(c, t, t2, 0.5, lambda a, f1=f1, y=y: centro(c, f1, 760, y, 76, "g", CLARO, a))
            fcen(c, t, t3, f2, 1360, y, 76, BR)
    E.saida(c, t, C["s16"] - 0.1, um)
    if t < C["s16"]:
        return
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    x, y, L = 300, 300, 420
    E.frase(c, t, C["s16"] + 0.3, ps("a área tem", "i", 76, CLARO) + [("duas direções", "g", 80, BR)], W / 2, 180, "center", 0.12)
    E.foco(c, t, a6, 0.5, lambda a: M.rrect(c, x, y, L, L, 8, E.COR, a))
    E.foco(c, t, PW("s16", "comprimento"), 0.4, lambda a: (M.arrow(c, x, y + L + 50, x + L, y + L + 50, CLARO, a, 6, 20),
                                                          centro(c, "× 100", x + L / 2, y + L + 120, 56, "g", BR, a)))
    E.foco(c, t, PW("s16", "largura,"), 0.4, lambda a: (M.arrow(c, x + L + 50, y + L, x + L + 50, y, CLARO, a, 6, 20),
                                                       E.escreve(c, "× 100", x + L + 80, y + L / 2 + 20, 56, "g", BR, a)))
    E.foco(c, t, b6, 0.5, lambda a: E.selo(c, 1010, 470, 42, False, a))
    E.frase(c, t, b6 + 0.1, ps("não compensa:", "i", 58, CLARO) + [("deram os lados", "g", 60, BR)], 1070, 492, "left", 0.1)
    E.frase(c, t, c6, ps("converta", "i", 64, CLARO) + [("os lados primeiro", "g", 66, BR)], 1060, 680, "left", 0.1)
    E.frase(c, t, PW("s16", "conte"), ps("e conte os", "i", 64, CLARO) + [("quadradinhos", "g", 66, BR)], 1060, 780, "left", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    E.frase(c, t, C["s17"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a7 - 0.6, ps("um sítio de", "i", 72), XE, 350, passo=0.1)
    E.foco(c, t, a7, 0.5, lambda a: E.escreve(c, "3,2 ha", XE + 380, 350, 100, "g", COR, a))
    E.frase(c, t, b7, ps("quantos", "i", 68) + [("m²?", "g", 72, COR)], XE, 450, passo=0.1)
    E.frase(c, t, c7 - 0.8, ps("uma lajota de", "i", 72), XE, 640, passo=0.1)
    E.foco(c, t, c7, 0.5, lambda a: E.escreve(c, "2.500 cm²", XE + 440, 640, 100, "g", COR, a))
    E.frase(c, t, d7, ps("quantos", "i", 68) + [("m²?", "g", 72, COR)], XE, 740, passo=0.1)
    E.relogio(c, t, C["s18.a"], 1560, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9 = C["s19.a"], C["s19.b"]
    a0, b0, c0 = C["s20.a"], C["s20.b"], C["s20.c"]
    ESC_A.degraus(c, t, C["s19"] - 0.1, acesos=(1, 2, 3) if t < C["s20"] else (3, 4, 5), ta=C["s19"] + 0.5)

    def um():
        E.frase(c, t, C["s19"] + 0.3, ps("sítio:", "i", 64) + [("3,2 ha em m²", "g", 66, COR)], 1060, 180, "left", 0.1)
        E.foco(c, t, PW("s19", "hectare"), 0.4, lambda a: E.pilula(c, "1 ha = 10.000 m²", 1420, 300, 52, "g", fundo=TINTA, a=a, cor=BR))
        ESC_A.pulos(c, t, 1, [(a9, 2), (a9 + 0.7, 3)], C["s19"] + 0.4)
        num_un(c, t, "32", 1, [(a9, 3), (a9 + 0.7, 5)], XN, 470, SN, [(C["s19"] + 0.4, "hm²"), (a9 + 0.7, "dam²"), (a9 + 1.4, "m²")], t0=C["s19"] + 0.4, some=True)
        casas(c, t, a9, "4 casas →", 1420, 590)
        bola_res(c, t, b9, "32.000 m²", 1680, 830, 175, 50)
    E.saida(c, t, C["s20"] - 0.1, um)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"] + 0.2, ps("lajota:", "i", 64) + [("2.500 cm² em m²", "g", 66, COR)], 1060, 180, "left", 0.1)
    E.foco(c, t, PW("s20", "maior,"), 0.4, lambda a: E.pilula(c, "unidade maior → número menor", 1440, 300, 46, "g", fundo=TINTA, a=a, cor=BR))
    ESC_A.pulos(c, t, 5, [(a0, 4), (a0 + 0.7, 3)], C["s20"] + 0.3)
    px = num_un(c, t, "2500", 4, [(a0, 2), (a0 + 0.7, 0)], XN, 470, SN, [(C["s20"] + 0.3, "cm²"), (a0 + 0.7, "dm²"), (a0 + 1.4, "m²")], t0=C["s20"] + 0.3, tv=a0 - 0.4)
    casas(c, t, a0, "← 4 casas", 1420, 590, cor=TINTA)
    if px and t >= b0:
        E.risco(c, px(2) - 40, 480, px(3) + 40, 370, t, b0, largura=10)
    bola_res(c, t, b0, "0,25 m²", 1660, 830, 150, 64)
    E.frase(c, t, PW("s20", "Menos"), ps("menos de 1 m²", "i", 56, CERTO), 1060, 1010, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s21.a", "área", "conta quadradinhos"), ("s21.b", "na escada da área,", "1 degrau = 2 casas"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 80) + [(l2, "g", 84, COR)], 320, y, "left", 0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a2, b2 = C["s22.a"], C["s22.b"]
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 80), XE, 240, passo=0.12)
    E.frase(c, t, a2 - 0.6, ps("uma caixa de", "i", 84) + [("cubinhos", "g", 110, COR)], XE, 410, passo=0.12)
    E.frase(c, t, b2, ps("quantos", "i", 72) + [("litros", "g", 84, COR)] + ps("cabem em 1 m³", "i", 72), XE, 550, passo=0.1)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, area=b_area, cm2=b_cm2, hectare=b_hectare, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
