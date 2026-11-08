"""Visual — Estudativo · MAT-MED-003: prefixos e unidades fora do sistema métrico.
Mesma linguagem da trilha (peças locais Escada e num_un, iguais às de MAT-MED-001): aqui a escada é a dos PREFIXOS,
de giga a nano, com a unidade no degrau do meio; cada degrau vale mil, e embaixo do prefixo vem a potência de dez.
Peças locais novas: arquivo() (folha de um arquivo), virus(), tv() (tela com a diagonal que se desenha).
Instantes: cues C[...] e a palavra falada (PW)."""
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
ARQUIVO_FINAL = "estudativo_MAT-MED-003_prefixos_e_unidades_fora_do_sistema_metrico.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("grandes", "pequenos", "fora", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 2 * 10 ** 9 == 2000000000 and str(2 * 10 ** 9).count("0") == 9 and 3 * 10 ** 6 == 3000000
assert 100 * 10 ** -9 == 10 ** -7 or abs(100 * 10 ** -9 - 10 ** -7) < 1e-20
assert abs(50 * 2.54 - 127) < 1e-9 and 254 / 2 == 127 and 19 < 50 / 2.54 < 20
assert 64 * 10 ** 9 == 6.4 * 10 ** 10 and 5 * 16 == 80 and abs(5 * 1.6 - 8) < 1e-9

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
PREF = ("G", "M", "k", "1", "m", "µ", "n")
POT = ("10^9", "10^6", "10^3", "", "10^{−3}", "10^{−6}", "10^{−9}")
ESC_P = Escada(un=PREF, nomes=("", "", "", "unidade", "", "", ""))


def potencias(c, t, tl, a=1.0):
    """a potência de dez embaixo de cada prefixo, no instante do rótulo"""
    for i, s in enumerate(POT):
        if s:
            E.foco(c, t, tl[i] + 0.15, 0.45, lambda b, i=i, s=s: E.formula(c, s, ESC_P.cx(i), ESC_P.topo(i) + 128, 44, "g", TINTA2, b * a, "center"))


def linha3(c, t, t0, y, pre, nome, pot, cor=None):
    """prefixo · nome · potência, em três colunas à direita da escada"""
    E.foco(c, t, t0, 0.5, lambda a: E.escreve(c, pre, 1070, y, 64, "g", cor or COR, a))
    E.foco(c, t, t0 + 0.4, 0.5, lambda a: E.escreve(c, nome, 1290, y, 56, "i", TINTA, a))
    E.foco(c, t, t0 + 0.9, 0.5, lambda a: E.formula(c, pot, 1660, y, 60, "g", TINTA, a))


def arquivo(c, cx, cy, h, a=1.0):
    """folha de arquivo com o canto dobrado e linhas de texto"""
    if a <= 0:
        return
    w = h * 0.76
    x, y = cx - w / 2, cy - h / 2
    p = skia.Path(); p.moveTo(x, y); p.lineTo(x + w * 0.7, y); p.lineTo(x + w, y + w * 0.3); p.lineTo(x + w, y + h); p.lineTo(x, y + h); p.close()
    c.drawPath(p, M.paint("#FFFFFF", a)); c.drawPath(p, M.paint(TINTA, a, stroke=5))
    d = skia.Path(); d.moveTo(x + w * 0.7, y); d.lineTo(x + w * 0.7, y + w * 0.3); d.lineTo(x + w, y + w * 0.3)
    c.drawPath(d, M.paint(TINTA, a, stroke=5))
    for k in range(5):
        yy = y + h * (0.38 + 0.11 * k)
        M.line(c, x + w * 0.15, yy, x + w * (0.85 if k < 4 else 0.55), yy, E.COR, a, 7)


def virus(c, cx, cy, r, a=1.0, giro=0.0):
    """vírus: esfera com espículas"""
    if a <= 0:
        return
    for k in range(14):
        ang = math.radians(giro + k * 360 / 14)
        x0, y0 = cx + math.cos(ang) * r, cy + math.sin(ang) * r
        x1, y1 = cx + math.cos(ang) * r * 1.32, cy + math.sin(ang) * r * 1.32
        M.line(c, x0, y0, x1, y1, E.COR, a, 6)
        c.drawCircle(x1, y1, r * 0.09, M.paint(E.COR, a))
    E.bola(c, cx, cy, r, a=a)


def tv(c, t, x, y, w, h, td, a=1.0, cor_d=None):
    """televisão: moldura, tela e a diagonal que se desenha a partir de td"""
    if a <= 0:
        return
    M.rrect(c, x - 18, y - 18, w + 36, h + 36, 16, TINTA, a)
    M.rrect(c, x, y, w, h, 6, "#E9E7F7", a)
    M.line(c, x + w / 2 - 70, y + h + 18, x + w / 2 - 110, y + h + 70, TINTA, a, 10)
    M.line(c, x + w / 2 + 70, y + h + 18, x + w / 2 + 110, y + h + 70, TINTA, a, 10)
    p = ep(t, td, 0.8)
    if p > 0:
        M.line(c, x + 10, y + h - 10, lerp(x + 10, x + w - 10, p), lerp(y + h - 10, y + 10, p), cor_d or E.COR, a, 9)
        c.drawCircle(x + 10, y + h - 10, 11, M.paint(cor_d or E.COR, a))
        if p >= 1:
            c.drawCircle(x + w - 10, y + 10, 11, M.paint(cor_d or E.COR, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    tq = PW("s01", "Quantos")

    def um():
        E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "2 GB", 300, 330, 170, "g", TINTA, a))
        E.foco(c, t, tq, 0.5, lambda a: E.escreve(c, "= ? bytes", 790, 330, 150, "g", CINZA, a))
        y, size = 640, 130
        s = "2.000.000.000"
        x0 = W / 2 - E.larg(s, "g", size) / 2
        E.foco(c, t, PW("s01", "Escrito"), 0.5, lambda a: E.escreve(c, "2", x0, y, size, "g", TINTA, a))
        xx, k = x0 + E.larg("2", "g", size), 0
        for ch in s[1:]:
            if ch == "0":
                E.foco(c, t, kb + 0.08 * k, 0.3, lambda a, xx=xx: E.escreve(c, "0", xx, y, size, "g", COR, a), sobe=8)
                k += 1
            else:
                E.foco(c, t, kb - 0.2, 0.3, lambda a, xx=xx: E.escreve(c, ".", xx, y, size, "g", TINTA, a))
            xx += E.larg(ch, "g", size) + E.APERTO["g"] * size
        E.foco(c, t, kb + 0.6, 0.4, lambda a: centro(c, "9 zeros", W / 2, y + 100, 60, "i", COR, a))
        E.foco(c, t, kc, 0.5, lambda a: E.formula(c, "= 2 × 10^9", W / 2, 940, 130, "g", COR, a, "center"))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 280, passo=0.12)
        E.frase(c, t, PW("s02", "prefixos"), ps("prefixos", "i", 84) + [("gigantes", "g", 92, COR)], XE, 430, passo=0.12)
        E.frase(c, t, PW("s02", "minúsculos"), ps("e", "i", 84) + [("minúsculos", "g", 92, COR)], XE, 560, passo=0.12)
        E.frase(c, t, tb, [("polegadas", "g", 88, COR)] + ps("em centímetros", "i", 80), XE, 700, passo=0.12)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "a escada das unidades", "quilo vale mil"), ("s03.c", "a notação científica", "expoente negativo"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(420, 700, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, PW("s03", "Se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1000, "left", 0.12)


# ---------------- prefixos grandes ----------------
def b_grandes(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    if t < C["s05"] + 0.4:
        def byte():
            E.frase(c, t, a4 - 0.4, ps("o que é", "i", 84) + [("byte?", "g", 96, COR)], W / 2, 230, "center", 0.12)
            E.foco(c, t, b4, 0.5, lambda a: arquivo(c, 600, 600, 340, a))
            E.frase(c, t, b4 + 0.2, ps("o tamanho de", "i", 60) + [("um arquivo", "g", 62, COR)], 600, 860, "center", 0.1)
            E.foco(c, t, PW("s04", "letra"), 0.5, lambda a: (M.rrect(c, 1180, 470, 220, 240, 20, "#FFFFFF", a, stroke=5, stroke_color=TINTA),
                                                            centro(c, "A", 1290, 660, 200, "s", TINTA, a)))
            E.foco(c, t, c4, 0.5, lambda a: E.escreve(c, "≈ 1 byte", 1450, 620, 90, "g", COR, a))
            E.frase(c, t, c4 + 0.3, ps("uma letra", "i", 56, TINTA2), 1290, 790, "center", 0.1)
        E.saida(c, t, C["s05"] - 0.1, byte)
    if t < C["s05"] - 0.1:
        return
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    tl = [c5, b5, a5, C["s05"] + 0.3, 1e9, 1e9, 1e9]
    ESC_P.degraus(c, t, [C["s05"] + 0.1 * i for i in range(7)], tl, acesos=(0,), ta=C["s06.a"])
    potencias(c, t, tl)
    linha3(c, t, a5, 200, "quilo", "mil", "10^3")
    linha3(c, t, b5, 310, "mega", "1 milhão", "10^6")
    linha3(c, t, c5, 420, "giga", "1 bilhão", "10^9")
    fase(c, t, d5, C["s06"] - 0.1, lambda: (
        fcen(c, t, d5, "3 MB = 3 × 10^6 B", 1500, 560, 72),
        E.frase(c, t, e5, [("= 3 milhões", "g", 62, COR)] + ps("de bytes", "i", 58), 1500, 670, "center", 0.1)))
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    fase(c, t, a6, C["s07"] - 0.1, lambda: (
        fcen(c, t, a6, "2 GB = 2 × 10^9 B", 1500, 560, 72, COR),
        E.frase(c, t, b6, [("= 2 bilhões", "g", 62, COR)] + ps("de bytes", "i", 58), 1500, 670, "center", 0.1),
        E.frase(c, t, c6, ps("a frente:", "i", 58, TINTA2), 1450, 1010, "right", 0.1),
        fcen(c, t, c6 + 0.3, "1 ≤ 2 < 10", 1660, 1010, 64, CERTO)))
    if t >= C["s07"] - 0.1:
        a7, b7 = C["s07.a"], C["s07.b"]
        E.saida(c, t, C["s07.end"] - 0.3, lambda: (
            E.frase(c, t, PW("s07", "informática"), ps("em informática, às vezes:", "i", 56, TINTA2), 1500, 560, "center", 0.1),
            E.frase(c, t, a7, ps("cada prefixo =", "i", 54) + [("1.024 ×", "g", 58, COR)] + ps("o anterior", "i", 54), 1460, 660, "center", 0.1),
            E.foco(c, t, b7, 0.5, lambda a: E.pilula(c, "use o valor do enunciado", 1500, 1010, 54, "g", a=a, cor=E.SOBRE))))


# ---------------- prefixos pequenos ----------------
def b_pequenos(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    tl = [C["s08"]] * 4 + [a8, b8, c8]

    def esc():
        ESC_P.degraus(c, t, C["s08"] - 0.1, tl, acesos=(6,), ta=C["s09.a"] - 1.4)
        potencias(c, t, tl)
        linha3(c, t, a8, 200, "mili", "milésimo", "10^{−3}")
        linha3(c, t, b8, 310, "micro", "milionésimo", "10^{−6}")
        linha3(c, t, c8, 420, "nano", "bilionésimo", "10^{−9}")
    E.saida(c, t, C["s09"] - 0.1, esc)
    if t < C["s09"]:
        return
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    E.foco(c, t, C["s09"] + 0.2, 0.6, lambda a: virus(c, 340, 470, 120, a, t * 12))
    E.frase(c, t, PW("s09", "vírus"), ps("vírus da gripe", "i", 60), 340, 720, "center", 0.1)
    E.foco(c, t, a9, 0.5, lambda a: centro(c, "≈ 100 nm", 340, 830, 80, "g", COR, a))
    fcen(c, t, b9, "100 nm = 100 × 10^{−9} m", 1200, 330, 84)
    fcen(c, t, PW("s09", "Cem", 2), "100 = 10^2", 1200, 500, 76, TINTA2)
    fcen(c, t, PW("s09", "Repete"), "10^2 × 10^{−9} = 10^{2 + (−9)}", 1200, 670, 76)
    bola_res(c, t, c9, "10^{−7} m", 1200, 880, 130, 70)


# ---------------- fora do sistema métrico ----------------
def b_fora(c, t, C, b):
    a0, b0, c0, d0 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]

    def fora():
        E.frase(c, t, a0 - 0.3, ps("fora do", "i", 84) + [("sistema métrico", "g", 88, COR)], W / 2, 230, "center", 0.12)
        nomes = ("polegada", "pé", "milha", "libra")
        xs = (360, 760, 1160, 1560)
        for x, n in zip(xs, nomes):
            E.foco(c, t, PW("s10", n), 0.4, lambda a, x=x, n=n: E.pilula(c, n, x, 440, 66, "g", fundo=TINTA, a=a, cor=BR))
        E.frase(c, t, c0, ps("vieram de outros países e", "i", 64) + [("não andam de 10 em 10", "g", 66, ERRADO)], W / 2, 650, "center", 0.1)
        E.foco(c, t, d0, 0.5, lambda a: E.pilula(c, "a prova dá o fator de conversão", W / 2, 840, 70, "g", fundo=CERTO, a=a, cor=BR))
    E.saida(c, t, C["s11"] - 0.1, fora)
    if t < C["s11"]:
        return
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    E.foco(c, t, C["s11"] + 0.1, 0.5, lambda a: tv(c, t, 160, 300, 680, 383, b1, a))
    E.frase(c, t, a1, ps("TV de", "i", 66) + [("50 polegadas", "g", 70, COR)], 500, 200, "center", 0.1)
    E.foco(c, t, b1 + 0.8, 0.5, lambda a: E.pilula(c, "a diagonal", 500, 490, 52, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "1 pol = 2,54 cm", 500, 860, 64, "g", fundo=TINTA, a=a, cor=BR))
    if t < C["s12"]:
        return
    a2, b2, c2, d2 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    xr = 1400
    E.frase(c, t, C["s12"] + 0.3, ps("cada polegada vira 2,54 cm:", "i", 56, TINTA2), xr, 200, "center", 0.08)
    fcen(c, t, a2, "50 × 2,54", xr, 340, 110)
    E.frase(c, t, PW("s12", "Cinquenta", 2), [("50", "g", 64, COR)] + ps("é metade de", "i", 60) + [("100", "g", 64, COR)], xr, 470, "center", 0.1)
    fcen(c, t, b2, "2,54 × 100 = 254", xr, 610, 90)
    fcen(c, t, c2, "254 ÷ 2 = 127", xr, 740, 90)
    bola_res(c, t, d2, "127 cm", 1700, 935, 135, 58)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, C["s13"] + 0.3, ps("o erro:", "i", 76) + [("dividir pelo fator", "g", 80, ERRADO)], W / 2, 200, "center", 0.11)
    fcen(c, t, PW("s13", "Cinquenta"), "50 ÷ 2,54", 620, 420, 110, ERRADO)
    E.foco(c, t, b3, 0.5, lambda a: E.escreve(c, "≈ 20 cm?", 900, 420, 110, "g", ERRADO, a))
    E.foco(c, t, PW("s13", "Uma"), 0.5, lambda a: tv(c, t, 380, 560, 140, 79, 1e9, a))
    E.frase(c, t, PW("s13", "Uma") + 0.2, ps("uma TV de 20 cm?", "i", 60, ERRADO), 600, 760, "left", 0.1)
    if t >= b3 + 0.6:
        E.risco(c, 380, 450, 1420, 330, t, c3, largura=12)
    E.foco(c, t, c3, 0.5, lambda a: E.pilula(c, "cm é menor que polegada → o número cresce", W / 2, 880, 60, "g", fundo=CERTO, a=a, cor=BR))
    fcen(c, t, PW("s13", "crescer"), "50 → 127", 1500, 700, 90, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    tm = {9: PW("s14", "Giga"), 6: PW("s14", "Mega"), 3: PW("s14", "Quilo"), 0: b4 - 0.4,
          -3: PW("s14", "Mili"), -6: PW("s14", "Micro"), -9: PW("s14", "Nano")}
    nomes = {9: "giga", 6: "mega", 3: "quilo", 0: "", -3: "mili", -6: "micro", -9: "nano"}

    def regua():
        E.frase(c, t, C["s14"] + 0.3, ps("agora, o atalho:", "i", 70, CLARO), W / 2, 150, "center", 0.1)
        E.frase(c, t, a4, ps("de", "i", 92, CLARO) + [("3 em 3", "g", 96, BR)] + ps("no expoente", "i", 92, CLARO), W / 2, 290, "center", 0.12)
        marcas = [-9, -6, -3, 0, 3, 6, 9]
        vx = E.reta(c, t, b4 - 0.6, 230, 1690, 640, -9, 9, marcas, fmt=lambda v: str(v).replace("-", "−"), escuro=True, size=56,
                    tm=[tm[v] + 0.2 for v in marcas])
        for v in marcas:
            if nomes[v]:
                E.foco(c, t, tm[v], 0.4, lambda a, v=v: centro(c, nomes[v], vx(v), 580, 54, "g", BR, a))
        for v0, v1 in ((0, 3), (3, 6), (6, 9), (0, -3), (-3, -6), (-6, -9)):
            E.salto(c, t, tm[v1] - 0.1, vx(v0), vx(v1), 500, 70, CLARO, "+3" if v1 > 0 else "−3", size=40)
    E.saida(c, t, C["s15"] - 0.1, regua)
    if t < C["s15"]:
        return
    a5, b5 = C["s15.a"], C["s15.b"]
    E.frase(c, t, a5, ps("cada prefixo vale", "i", 80, CLARO) + [("mil ×", "g", 84, BR)] + ps("o anterior", "i", 80, CLARO), W / 2, 300, "center", 0.12)
    fcen(c, t, PW("s15", "mil", 2), "1.000 = 10^3", W / 2, 470, 110, BR)
    E.foco(c, t, b5, 0.5, lambda a: E.selo(c, 520, 700, 50, False, a))
    E.frase(c, t, b5 + 0.1, ps("não compensa com", "i", 72, CLARO) + [("centi", "g", 76, BR)] + ps("e", "i", 72, CLARO) + [("deci", "g", 76, BR)], 600, 725, "left", 0.1)
    E.frase(c, t, PW("s15", "volte"), ps("para eles,", "i", 76, CLARO) + [("volte à escada", "g", 80, BR)], W / 2, 900, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a6, b6, c6, d6, e6 = (C[f"s16.{k}"] for k in "abcde")
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a6 - 0.8, ps("pendrive de", "i", 68), XE, 310, passo=0.1)
    E.foco(c, t, a6, 0.5, lambda a: E.escreve(c, "64 GB", XE + 360, 310, 96, "g", COR, a))
    E.frase(c, t, b6, ps("em bytes, na", "i", 64) + [("notação científica", "g", 66, COR)], XE, 420, passo=0.1)
    E.frase(c, t, c6 - 0.6, ps("corrida de", "i", 68), XE, 600, passo=0.1)
    E.foco(c, t, c6, 0.5, lambda a: E.escreve(c, "5 milhas", XE + 330, 600, 96, "g", COR, a))
    E.foco(c, t, d6, 0.5, lambda a: E.pilula(c, "1 milha = 1,6 km", XE + 300, 690, 56, "g", fundo=TINTA, a=a, cor=BR))
    E.frase(c, t, e6, ps("quantos", "i", 84) + [("km?", "g", 90, COR)], XE, 880, passo=0.12)
    E.relogio(c, t, C["s17.a"], 1560, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")

    def bytes_():
        E.frase(c, t, PW("s18", "Giga"), [("giga", "g", 72, COR)] + ps("=", "i", 72), 560, 200, "left", 0.1)
        E.foco(c, t, PW("s18", "dez") + 0.2, 0.4, lambda a: E.formula(c, "10^9", 800, 200, 72, "g", COR, a))
        size = 150
        if t >= a8:
            c.saveLayer(None, M.paint("#000000", ep(t, a8, 0.4)))
            E.anda(c, t, "64", 2, [(b8, 1)], 500, 520, size, tv=b8 - 0.3)
            c.restore()
        xp = 500 + 2 * E.casa(size) + 40
        E.foco(c, t, a8 + 0.4, 0.4, lambda a: E.formula(c, "× 10^9", xp, 520, 120, "g", TINTA, a * (1 - ep(t, c8, 0.3))))
        E.foco(c, t, c8, 0.4, lambda a: E.formula(c, "× 10^{10}", xp, 520, 120, "g", COR, a))
        E.foco(c, t, PW("s18", "passa"), 0.4, lambda a: E.pilula(c, "64 passa de 10", 760, 670, 52, "g", fundo=TINTA, a=a, cor=BR))
        E.foco(c, t, b8, 0.4, lambda a: E.pilula(c, "vírgula: 1 casa ←", 760, 760, 52, "g", fundo=TINTA, a=a, cor=BR))
        E.foco(c, t, c8, 0.4, lambda a: E.pilula(c, "expoente: + 1", 760, 850, 52, "g", a=a, cor=E.SOBRE))
        bola_res(c, t, d8 + 0.3, "6,4 × 10^{10}", 1500, 500, 220, 70)
        E.foco(c, t, d8 + 0.6, 0.4, lambda a: centro(c, "bytes", 1500, 790, 60, "i", COR, a))
    E.saida(c, t, C["s19"] - 0.1, bytes_)
    if t < C["s19"]:
        return
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    E.frase(c, t, C["s19"] + 0.3, ps("1 milha =", "i", 66) + [("1,6 km", "g", 70, COR)], W / 2, 200, "center", 0.1)
    fcen(c, t, a9, "5 × 1,6", 560, 420, 110)
    E.frase(c, t, PW("s19", "Sem"), ps("sem a vírgula:", "i", 56, TINTA2), 1300, 330, "center", 0.1)
    fcen(c, t, b9, "5 × 16 = 80", 1300, 440, 100)
    E.foco(c, t, PW("s19", "Uma"), 0.4, lambda a: E.pilula(c, "1 casa: 80 → 8,0", 1300, 560, 56, "g", fundo=TINTA, a=a, cor=BR))
    bola_res(c, t, c9, "8 km", 560, 700, 140, 80)
    E.frase(c, t, PW("s19", "Quilômetro"), ps("km é menor que milha:", "i", 60) + [("5 → 8", "g", 66, CERTO)], 1300, 760, "center", 0.1)
    E.frase(c, t, d9, ps("o número", "i", 60) + [("cresceu", "g", 66, CERTO)], 1300, 870, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s20.a", "prefixos:", "de 3 em 3 no expoente"), ("s20.b", "fora do métrico:", "o fator do enunciado"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 430 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 76) + [(l2, "g", 78, COR)], 320, y, "left", 0.1)
        E.frase(c, t, PW("s20", "conferindo"), ps("e confira:", "i", 60, TINTA2) + [("cresce ou diminui?", "g", 62, TINTA2)], 320, 870, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1 = C["s21.a"], C["s21.b"]
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 80), XE, 240, passo=0.12)
    E.frase(c, t, a1, ps("o", "i", 90) + [("metro quadrado", "g", 110, COR)], XE, 410, passo=0.12)
    E.frase(c, t, b1, ps("na área, cada degrau vale", "i", 72) + [("100", "g", 84, COR)], XE, 550, passo=0.1)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, grandes=b_grandes, pequenos=b_pequenos, fora=b_fora, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
