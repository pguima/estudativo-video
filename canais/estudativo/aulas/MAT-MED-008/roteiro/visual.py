"""Visual — Estudativo · MAT-MED-008: praticando medidas e unidades (5 problemas, um de cada medida).
Reaproveita as peças da trilha, iguais às das aulas anteriores: a Escada com a bolinha e a vírgula que anda (MAT-MED-001),
o pulo de mil (MAT-MED-002), a parede de azulejos em quadradinhos (MAT-MED-004), o aquário em perspectiva (E.paralelepipedo),
o relógio com as fatias de 6 minutos (MAT-MED-006) e a conta de horas em duas colunas (MAT-MED-007).
Cada problema abre com a ficha "problema n" e a bola numerada; a resposta abre com "vamos lá".
Instantes: cues C[...] e a palavra falada (PW)."""
import json
import math
import unicodedata
from fractions import Fraction as Fr
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Medidas e Unidades")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-MED-008_praticando_medidas_e_unidades.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "questao5", "fim"))
BR = "#FFFFFF"

assert 2.4 * 1000 == 2400 and 2400 / 400 == 6 and 2.4 / 400 < 1
assert 1.5 * 1000 == 1500 and 1500 / 30 == 50 and 50 * 30 == 1500
assert 2 * 1 * 100 * 100 == 20000 and 20 * 20 == 400 and 20000 / 400 == 50 and 200 < 400 and 200 // 20 * (100 // 20) == 50
assert 5 * 3 * 4 == 60 and 50 * 30 * 40 == 60000 and 60000 / 1000 == 60
assert Fr(3, 10) * 60 == 18 and 50 + 18 == 68 and 8 * 60 + 50 + 2 * 60 + 18 == 11 * 60 + 8 and (11 * 60 + 20) - (11 * 60 + 8) == 12

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


# ---------------- peças reaproveitadas das aulas anteriores da trilha ----------------
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


def mostrador(c, cx, cy, r, frac, a=1.0, cor=None, decimos=0.0, escuro=False, marca=None, cor_marca=None):
    """uma hora como relógio: setor pintado do 12 no sentido horário = frac da hora.
    decimos = 0..1, as 10 fatias de 6 minutos. marca = outra fração, só o contorno (o erro)"""
    if a <= 0:
        return
    cor = cor or E.COR
    tinta = BR if escuro else TINTA
    c.drawCircle(cx, cy, r, M.paint("#FFFFFF", (0.08 if escuro else 1.0) * a))
    rect = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
    if frac > 0:
        p = skia.Path(); p.moveTo(cx, cy)
        if frac >= 0.999:
            p.addCircle(cx, cy, r)
        else:
            p.arcTo(rect, -90, 360 * frac, False); p.close()
        c.drawPath(p, M.paint(cor, 0.9 * a))
    if marca:
        p = skia.Path(); p.moveTo(cx, cy); p.arcTo(rect, -90, 360 * marca, False); p.close()
        c.drawPath(p, M.paint(cor_marca or ERRADO, a, stroke=6))
    for k in range(60):
        ang = math.radians(-90 + k * 6)
        L = r * (0.16 if k % 5 == 0 else 0.07)
        if k % 5 and r < 110:
            continue
        M.line(c, cx + math.cos(ang) * (r - L), cy + math.sin(ang) * (r - L), cx + math.cos(ang) * r * 0.97, cy + math.sin(ang) * r * 0.97,
               tinta, a * (0.9 if k % 5 == 0 else 0.5), 4 if k % 5 == 0 else 2)
    if decimos > 0:
        for k in range(10):
            ang = math.radians(-90 + k * 36)
            M.line(c, cx, cy, cx + math.cos(ang) * r, cy + math.sin(ang) * r, BR if not escuro else CLARO, a * decimos, 3)
            M.line(c, cx, cy, cx + math.cos(ang) * r, cy + math.sin(ang) * r, tinta, a * decimos * 0.5, 1.5)
    c.drawCircle(cx, cy, r, M.paint(tinta, a, stroke=5))
    c.drawCircle(cx, cy, max(5, r * 0.05), M.paint(tinta, a))


SZ = 110          # tamanho dos números da conta de horas
DY = 150          # distância entre as linhas da conta


def cel(c, t, t0, s, xr, y, size=SZ, cor=None, est="g"):
    """texto alinhado à direita em xr, que entra com foco"""
    E.foco(c, t, t0, 0.45, lambda a: E.escreve(c, s, xr - E.larg(s, est, size), y, size, est, cor or TINTA, a))


def hm(c, t, t0, h, m, xh, xm, y, size=SZ, cor=None, tm=None, cor_h=None, cor_m=None):
    """uma linha "h  min": horas terminando em xh (com o "h" pequeno) e minutos terminando em xm; tm = instante dos minutos"""
    cel(c, t, t0, str(h), xh, y, size, cor_h or cor)
    E.foco(c, t, t0, 0.45, lambda a: E.escreve(c, "h", xh + 12, y, size * 0.55, "g", cor_h or cor or TINTA2, a))
    cel(c, t, tm if tm is not None else t0, str(m), xm, y, size, cor_m or cor)
    E.foco(c, t, tm if tm is not None else t0, 0.45, lambda a: E.escreve(c, "min", xm + 12, y, size * 0.55, "g", cor_m or cor or TINTA2, a))


def traco(c, t, t0, x0, x1, y, escuro=False):
    p = ep(t, t0, 0.5)
    if p > 0:
        M.line(c, x0, y, lerp(x0, x1, p), y, BR if escuro else TINTA, 1.0, 6)


def seta_troca(c, t, t0, x0, x1, y, rot, cor=None, alto=90):
    """seta curva que leva a troca de uma coluna para a outra, com a pílula no alto do arco (alto < 0: arco por baixo)"""
    p = ep(t, t0, 0.7)
    if p <= 0:
        return
    pts = [(lerp(x0, x1, u), y - math.sin(math.pi * u) * alto) for u in [p * k / 30 for k in range(31)]]
    path = skia.Path(); path.moveTo(*pts[0])
    for q in pts[1:]:
        path.lineTo(*q)
    c.drawPath(path, M.paint(cor or E.COR, 1.0, stroke=6, cap_round=True))
    if p >= 0.99:
        M.arrow(c, pts[-3][0], pts[-3][1], x1, y, cor or E.COR, 1.0, 6, 22)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.pilula(c, rot, (x0 + x1) / 2, y - alto - (50 if alto > 0 else -60), 48, "g", fundo=cor or E.COR, a=a, cor=BR))




# ---------------- peças desta aula ----------------
def ficha(c, t, t0, n, rotulo):
    """abertura de problema: bola com o número e a palavra "problema" + a medida"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, 240, 190, 70, a=a), centro(c, str(n), 240, 222, 90, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.1, ps("problema", "i", 70) + [(rotulo, "g", 72, COR)], 340, 215, "left", 0.1)


def azulejos(c, t, x, y, cols, lins, s, t0, dur=1.2, a=1.0, cor=None):
    """azulejos de lado s, de (x, y), entrando fileira a fileira"""
    if a <= 0:
        return
    for r in range(lins):
        for k in range(cols):
            q = ep(t, t0 + dur * (r * cols + k) / max(1, cols * lins), 0.3) * a
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


ESC_K = Escada(x=80, y=420, sw=140, sh=64, base=960, size=48)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "5", XE - 8, 470, 340, "g", COR, a))
    E.frase(c, t, ka + 0.3, ps("problemas", "i", 110), XE + 230, 450, "left", 0.1)
    E.frase(c, t, PW("s01", "criados"), ps("criados para esta aula", "i", 56, TINTA2), XE + 230, 540, "left", 0.08)
    for k, u in enumerate(("km", "t", "m²", "L", "h")):
        E.foco(c, t, ka + 0.6 + 0.2 * k, 0.4, lambda a, k=k, u=u: (E.bola(c, 1180 + k * 150, 380, 62, a=a), centro(c, u, 1180 + k * 150, 400, 52, "g", E.SOBRE, a)))
    E.frase(c, t, kb, ps("em todos, a unidade", "i", 66) + [("muda no meio do caminho", "g", 70, COR)], W / 2, 760, "center", 0.1)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "pause e resolva antes da resposta", W / 2, 900, 62, "g", fundo=TINTA, a=a, cor=BR))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    a2, b2, c2, d2, e2 = (C[f"s02.{k}"] for k in "abcde")
    E.frase(c, t, C["s02"] + 0.3, ps("você vai usar", "i", 70) + [("a escada do metro", "g", 74, COR)], 120, 190, "left", 0.1)
    esc = Escada(x=120, y=330, sw=120, sh=52, base=740, size=40)
    esc.degraus(c, t, a2, nomes=False)
    esc.pulos(c, t, 3, [(b2 + 0.3, 4)], a2 + 0.4, rastro=True)
    linhas = ((PW("s02", "comprimento,"), "comprimento, massa, capacidade:", "1 degrau = × 10 = 1 casa", b2),
              (PW("s02", "área,"), "área:", "1 degrau = × 100 = 2 casas", c2),
              (PW("s02", "volume,"), "volume:", "1 degrau = × 1.000 = 3 casas", d2),
              (PW("s02", "tempo,"), "tempo:", "a troca é de 60", e2))
    for i, (t1, l1, l2, t2) in enumerate(linhas):
        y = 330 + i * 170
        E.frase(c, t, t1, ps(l1, "i", 52, TINTA2), 1000, y, "left", 0.06)
        E.foco(c, t, t2, 0.4, lambda a, l2=l2, y=y, i=i: E.escreve(c, l2, 1000, y + 76, 62, "g", COR if i < 3 else TINTA, a))
    E.frase(c, t, PW("s02", "Se"), ps("travou?", "i", 54, COR) + ps("procure a aula no canal", "i", 54), 120, 1000, "left", 0.1)


# ---------------- problema 1: comprimento ----------------
def b_questao1(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s03.{k}"] for k in "abcd")
    ficha(c, t, a3, 1, "comprimento")
    E.frase(c, t, b3 - 1.0, ps("caminhar por dia", "i", 70), XE, 400, "left", 0.1)
    E.foco(c, t, b3, 0.5, lambda a: E.escreve(c, "2,4 km", XE + 560, 400, 110, "g", COR, a))
    E.frase(c, t, c3 - 0.6, ps("numa pista de", "i", 70), XE, 560, "left", 0.1)
    E.foco(c, t, c3, 0.5, lambda a: E.escreve(c, "400 m", XE + 460, 560, 110, "g", COR, a))
    E.frase(c, t, d3, ps("quantas", "i", 92) + [("voltas?", "g", 96, COR)], XE, 780, "left", 0.12)
    E.relogio(c, t, C["s04.a"], 1560, 440, 180)


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    hs = [b5 + 0.7 * k for k in range(3)]
    E.frase(c, t, C["s05"] + 0.3, ps("vamos lá:", "i", 62, TINTA2) + [("a mesma unidade", "g", 66, COR)], 120, 180, "left", 0.1)
    ESC_K.degraus(c, t, C["s05"] + 0.4, acesos=(0, 1, 2, 3), ta=b5, nomes=False)
    ESC_K.pulos(c, t, 0, [(h, k + 1) for k, h in enumerate(hs)], a5)
    num_un(c, t, "24", 1, [(h, k + 2) for k, h in enumerate(hs)], 1060, 330, 120, [(a5, "km"), (hs[-1] + 0.7, "m")], t0=a5, some=True)
    E.foco(c, t, b5, 0.4, lambda a: E.pilula(c, "3 degraus: × 1.000", 1450, 450, 52, "g", a=a, cor=E.SOBRE))
    fcen(c, t, d5, "2.400 ÷ 400 = 6", 1450, 620, 84)
    E.foco(c, t, PW("s05", "seis"), 0.5, lambda a: E.pilula(c, "6 voltas", 1450, 730, 70, "g", fundo=CERTO, a=a, cor=BR))
    fcen(c, t, PW("s05", "divide"), "2,4 ÷ 400 < 1", 1450, 880, 76, ERRADO)
    E.frase(c, t, e5, ps("menos de 1 volta?", "i", 54, ERRADO), 1450, 960, "center", 0.08)
    E.frase(c, t, PW("s05", "Resposta"), ps("resposta estranha =", "i", 50, TINTA2) + [("unidade trocada", "g", 52, TINTA2)], 1450, 1040, "center", 0.08)


# ---------------- problema 2: massa ----------------
def b_questao2(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    ficha(c, t, a6, 2, "massa")
    E.frase(c, t, b6 - 1.4, ps("um elevador aguenta", "i", 70), XE, 400, "left", 0.1)
    E.foco(c, t, b6, 0.5, lambda a: E.escreve(c, "1,5 t", XE + 680, 400, 110, "g", COR, a))
    E.frase(c, t, b6 + 0.4, ps("(uma tonelada e meia)", "i", 46, TINTA2), XE + 680, 470, "left", 0.06)
    E.frase(c, t, c6 - 0.6, ps("cada caixa pesa", "i", 70), XE, 600, "left", 0.1)
    E.foco(c, t, c6, 0.5, lambda a: E.escreve(c, "30 kg", XE + 520, 600, 110, "g", COR, a))
    E.frase(c, t, d6, ps("quantas", "i", 86) + [("caixas", "g", 90, COR)] + ps("no máximo?", "i", 86), XE, 800, "left", 0.12)
    E.relogio(c, t, C["s07.a"], 1560, 440, 180)


def b_resposta2(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    E.frase(c, t, C["s08"] + 0.3, ps("vamos lá", "i", 62, TINTA2), 120, 180, "left", 0.1)
    E.foco(c, t, a8, 0.5, lambda a: (centro(c, "t", 400, 420, 130, "g", TINTA, a), centro(c, "kg", 900, 420, 130, "g", TINTA, a)))
    pulo_mil(c, t, PW("s08", "pulo"), 480, 820, 330, cor=E.COR)
    E.foco(c, t, PW("s08", "três"), 0.4, lambda a: E.pilula(c, "3 casas", 650, 500, 50, "g", fundo=TINTA, a=a, cor=BR))
    fcen(c, t, b8, "1,5 t = 1.500 kg", 650, 680, 96, COR)
    fcen(c, t, c8, "1.500 ÷ 30 = 50", 1460, 420, 96)
    bola_res(c, t, PW("s08", "cinquenta"), "50 caixas", 1460, 640, 140, 56, CERTO)
    E.frase(c, t, PW("s08", "Confira"), ps("confira:", "i", 58, TINTA2), 1460, 850, "center", 0.1)
    fcen(c, t, d8, "50 × 30 = 1.500 kg", 1460, 950, 76)
    E.foco(c, t, PW("s08", "Faz"), 0.4, lambda a: E.selo(c, 1850, 925, 36, True, a))


# ---------------- problema 3: área ----------------
PX, PY, PS = 320, 400, 52  # a parede: 2 m x 1 m, azulejos de 20 cm = 52 px (1 m = 260 px)


def b_questao3(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    ficha(c, t, a9, 3, "área")
    E.foco(c, t, b9, 0.5, lambda a: M.rrect(c, PX, PY, 10 * PS, 5 * PS, 6, E.mix(E.COR, "#FFFFFF", 0.85), a, stroke=4, stroke_color=TINTA))
    cota_h(c, t, b9 + 0.2, "2 m", PX, PX + 10 * PS, PY - 30)
    cota_v(c, t, PW("s09", "um") + 0.2, "1 m", PX - 30, PY, PY + 5 * PS)
    E.frase(c, t, b9, ps("parede de", "i", 62) + [("2 m × 1 m", "g", 66, COR)], 1000, 440, "left", 0.1)
    E.foco(c, t, c9, 0.5, lambda a: M.rrect(c, 1010, 520, 120, 120, 10, E.COR, a))
    E.frase(c, t, c9 + 0.2, ps("azulejo de", "i", 58) + [("20 cm", "g", 62, COR)], 1160, 600, "left", 0.1)
    E.frase(c, t, d9, ps("quantos", "i", 86) + [("azulejos?", "g", 90, COR)], XE, 860, "left", 0.12)
    E.relogio(c, t, C["s10.a"], 1640, 740, 120)


def b_resposta3(c, t, C, b):
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    esc = Escada(x=90, y=440, sw=150, sh=64, base=960, un=("km²", "hm²", "dam²", "m²", "dm²", "cm²", "mm²"), nomes=("",) * 7, size=46)

    def certo():
        E.frase(c, t, C["s11"] + 0.3, ps("vamos lá", "i", 62, TINTA2), 120, 180, "left", 0.1)
        fcen(c, t, a1, "2 × 1 = 2 m²", 520, 330, 90)
        esc.degraus(c, t, PW("s11", "De"), acesos=(3, 4, 5), ta=PW("s11", "dois", 3), nomes=False)
        hs = [PW("s11", "dois", 3), b1]
        esc.pulos(c, t, 3, [(hs[0], 4), (hs[1], 5)], PW("s11", "De") + 0.3)
        E.foco(c, t, b1, 0.4, lambda a: E.pilula(c, "cada degrau × 100", 1400, 260, 50, "g", a=a, cor=E.SOBRE))
        fcen(c, t, c1, "2 m² = 20.000 cm²", 1400, 400, 76, COR)
        fcen(c, t, d1, "20 × 20 = 400 cm²", 1400, 560, 76)
        E.frase(c, t, d1 - 0.6, ps("cada azulejo:", "i", 50, TINTA2), 1400, 480, "center", 0.06)
        fcen(c, t, e1, "20.000 ÷ 400 = 50", 1400, 720, 80)
        bola_res(c, t, PW("s11", "cinquenta"), "50 azulejos", 1400, 900, 140, 50, CERTO)
    E.saida(c, t, C["s12"] - 0.1, certo)
    if t < C["s12"]:
        return
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    E.frase(c, t, C["s12"] + 0.3, ps("o erro clássico:", "i", 70) + [("a escada do comprimento", "g", 74, ERRADO)], W / 2, 200, "center", 0.1)
    E.foco(c, t, PW("s12", "dois"), 0.4, lambda a: E.pilula(c, "só 2 casas", 600, 360, 54, "g", fundo=ERRADO, a=a, cor=BR))
    fcen(c, t, b2, "2 m² = 200 cm²", 600, 520, 100, ERRADO)
    E.frase(c, t, c2, ps("a parede inteira:", "i", 60) + [("menos que 1 azulejo", "g", 64, ERRADO)], W / 2, 760, "center", 0.1)
    E.frase(c, t, c2 + 0.5, ps("(1 azulejo = 400 cm²)", "i", 56, TINTA2), 1180, 520, "left", 0.06)
    E.foco(c, t, PW("s12", "Resposta"), 0.5, lambda a: E.pilula(c, "resposta absurda = conversão errada", W / 2, 920, 62, "g", fundo=TINTA, a=a, cor=BR))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    x, y, s = 300, 420, 64

    def lados():
        E.frase(c, t, C["s13"] + 0.3, ps("o atalho de prova:", "i", 66, CLARO), W / 2, 160, "center", 0.1)
        E.frase(c, t, a3, ps("converta", "i", 88, CLARO) + [("os lados", "g", 92, BR)] + ps("não a área", "i", 88, CLARO), W / 2, 290, "center", 0.12)
        E.foco(c, t, b3 - 0.3, 0.5, lambda a: M.rrect(c, x, y, 10 * s, 5 * s, 6, "#FFFFFF", 0.08 * a, stroke=4, stroke_color=CLARO))
        for k in range(10):
            E.foco(c, t, b3 + 0.12 * k, 0.3, lambda a, k=k: M.rrect(c, x + k * s + 3, y + 3, s - 6, s - 6, 6, E.COR, a))
        for r in range(1, 5):
            E.foco(c, t, c3 + 0.15 * r, 0.3, lambda a, r=r: M.rrect(c, x + 3, y + r * s + 3, s - 6, s - 6, 6, E.COR, a))
        q = ep(t, d3, 1.0)
        if q > 0:
            for r in range(1, 5):
                for k in range(1, 10):
                    if (r * 9 + k) / 45 <= q:
                        M.rrect(c, x + k * s + 3, y + r * s + 3, s - 6, s - 6, 6, E.mix(E.COR, "#FFFFFF", 0.25), 1.0)
        E.foco(c, t, b3, 0.4, lambda a: centro(c, "10 na largura", x + 5 * s, y - 30, 50, "g", BR, a))
        E.foco(c, t, c3, 0.4, lambda a: E.escreve(c, "5", x - 70, y + 2.5 * s + 20, 56, "g", BR, a))
        fcen(c, t, b3, "200 cm ÷ 20 = 10", 1420, 470, 72, BR)
        fcen(c, t, c3, "100 cm ÷ 20 = 5", 1420, 600, 72, BR)
        bola_res(c, t, d3, "10 × 5 = 50", 1420, 820, 150, 54)
    E.saida(c, t, C["s14"] - 0.1, lados)
    if t < C["s14"]:
        return
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, a4, ps("lado é comprimento:", "i", 76, CLARO) + [("de 10 em 10", "g", 80, BR)], W / 2, 300, "center", 0.12)
    E.frase(c, t, PW("s14", "Você"), ps("você foge do", "i", 66, CLARO) + [("× 100", "g", 70, BR)], W / 2, 420, "center", 0.1)
    E.foco(c, t, b4, 0.5, lambda a: E.selo(c, 420, 630, 50, False, a))
    E.frase(c, t, b4 + 0.1, ps("não compensa com", "i", 70, CLARO) + [("área pronta", "g", 76, BR)] + ps("(hectares)", "i", 60, CLARO), 500, 655, "left", 0.1)
    E.foco(c, t, c4, 0.5, lambda a: E.pilula(c, "use a escada da área", W / 2, 860, 70, "g", a=a, cor=E.SOBRE))


# ---------------- problema 4: volume ----------------
def b_questao4(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    ficha(c, t, a5, 4, "volume")
    E.paralelepipedo(c, t, b5 - 0.4, 260, 840, 500, 300, 400, (None, None, None), d=0.8)
    E.foco(c, t, b5, 0.4, lambda a: centro(c, "50 cm", 510, 920, 56, "g", COR, a))
    E.foco(c, t, c5, 0.4, lambda a: E.escreve(c, "30 cm", 260 + 500 + 0.394 * 300 / 2 + 40, 840 - 0.308 * 300 / 2 + 30, 56, "g", COR, a))
    E.foco(c, t, d5, 0.4, lambda a: E.escreve(c, "40 cm", 60, 840 - 200 + 20, 56, "g", COR, a))
    E.frase(c, t, b5 - 0.8, ps("um", "i", 70) + [("aquário", "g", 74, COR)], 1060, 360, "left", 0.1)
    E.frase(c, t, e5, ps("quantos", "i", 86) + [("litros?", "g", 90, COR)], 1060, 520, "left", 0.12)
    E.relogio(c, t, C["s16.a"], 1500, 760, 140)


def b_resposta4(c, t, C, b):
    a7, b7, c7, d7, e7, f7 = (C[f"s17.{k}"] for k in "abcdef")

    def atalho():
        E.frase(c, t, C["s17"] + 0.3, ps("pelo atalho:", "i", 62, TINTA2) + [("lados em dm", "g", 66, COR)], 120, 180, "left", 0.1)
        E.foco(c, t, PW("s17", "porque"), 0.4, lambda a: E.pilula(c, "1 dm³ = 1 L", 1500, 160, 60, "g", a=a, cor=E.SOBRE))
        for k, (tk, txt) in enumerate(((b7, "50 cm = 5 dm"), (c7, "30 cm = 3 dm"), (d7, "40 cm = 4 dm"))):
            fcen(c, t, tk - 0.5, txt, 500, 380 + k * 130, 80)
        fcen(c, t, e7, "5 × 3 × 4 = 60 dm³", 1350, 450, 84)
        bola_res(c, t, f7, "60 L", 1350, 700, 140, 84, CERTO)
    E.saida(c, t, C["s18"] - 0.1, atalho)
    if t < C["s18"]:
        return
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, C["s18"] + 0.3, ps("pelo caminho longo", "i", 66, TINTA2), W / 2, 200, "center", 0.1)
    fcen(c, t, a8, "50 × 30 × 40 = 60.000 cm³", W / 2, 400, 90)
    E.foco(c, t, PW("s18", "Um"), 0.4, lambda a: E.pilula(c, "1 degrau no volume: × 1.000", W / 2, 520, 54, "g", fundo=TINTA, a=a, cor=BR))
    fcen(c, t, b8, "60.000 ÷ 1.000 = 60 dm³", W / 2, 680, 90)
    bola_res(c, t, c8, "60 L", W / 2, 880, 120, 76, CERTO)


# ---------------- problema 5: tempo ----------------
def b_questao5(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    ficha(c, t, a9, 5, "tempo")
    E.frase(c, t, b9 - 0.8, ps("começa às", "i", 70), XE, 400, "left", 0.1)
    E.foco(c, t, b9, 0.5, lambda a: E.escreve(c, "8 h 50 min", XE + 330, 400, 110, "g", COR, a))
    E.frase(c, t, c9 - 0.4, ps("e leva", "i", 70), XE, 560, "left", 0.1)
    E.foco(c, t, c9, 0.5, lambda a: E.escreve(c, "2,3 h", XE + 220, 560, 110, "g", COR, a))
    E.frase(c, t, d9, ps("a que horas", "i", 86) + [("termina?", "g", 90, COR)], XE, 780, "left", 0.12)
    E.relogio(c, t, C["s20.a"], 1560, 440, 180)


def b_resposta5(c, t, C, b):
    a1, b1, c1 = C["s21.a"], C["s21.b"], C["s21.c"]

    def decimos():
        E.frase(c, t, C["s21"] + 0.3, ps("vamos lá", "i", 62, TINTA2), 120, 180, "left", 0.1)
        E.foco(c, t, a1, 0.4, lambda a: E.escreve(c, "0,3 h ≠ 30 min", 120, 340, 84, "g", ERRADO, a))
        E.foco(c, t, b1 - 0.2, 0.5, lambda a: mostrador(c, 450, 690, 240, 0.3 * ep(t, b1, 0.8), a, decimos=1.0))
        fcen(c, t, b1, "f{3}{10} de 60 min", 1330, 300, 84)
        fcen(c, t, PW("s21", "sessenta", 2), "60 ÷ 10 = 6", 1330, 470, 84)
        fcen(c, t, PW("s21", "seis", 2), "6 × 3 = 18 min", 1330, 600, 84, COR)
        bola_res(c, t, c1, "2 h 18 min", 1330, 830, 150, 56)
    E.saida(c, t, C["s22"] - 0.1, decimos)
    if C["s22"] <= t < C["s23"] + 0.4:
        a2, b2, c2, d2 = (C[f"s22.{k}"] for k in "abcd")
        xh, xm, y0 = 520, 880, 340

        def soma():
            E.frase(c, t, C["s22"] + 0.2, ps("somando", "i", 62, TINTA2), 120, 170, "left", 0.1)
            hm(c, t, C["s22"] + 0.3, 8, 50, xh, xm, y0)
            E.foco(c, t, C["s22"] + 0.5, 0.4, lambda a: E.escreve(c, "+", xh - 300, y0 + DY, SZ, "g", TINTA, a))
            hm(c, t, C["s22"] + 0.5, 2, 18, xh, xm, y0 + DY)
            traco(c, t, a2 - 0.2, xh - 330, xm + 140, y0 + DY + 50)
            yr = y0 + 2 * DY + 30
            cel(c, t, a2, "10", xh, yr, SZ, COR)
            E.foco(c, t, a2, 0.45, lambda a: E.escreve(c, "h", xh + 12, yr, SZ * 0.55, "g", COR, a))
            cel(c, t, b2, "68", xm, yr, SZ, ERRADO if t >= c2 else COR)
            E.foco(c, t, b2, 0.45, lambda a: E.escreve(c, "min", xm + 12, yr, SZ * 0.55, "g", ERRADO if t >= c2 else COR, a))
            seta_troca(c, t, c2, xm - 60, xh - 40, yr + 70, "60 min = 1 h", alto=-110)
            fcen(c, t, c2, "68 = 60 + 8", 1450, 400, 84)
            bola_res(c, t, d2, "11 h 08 min", 1450, 680, 160, 54, CERTO)
        E.saida(c, t, C["s23"] - 0.1, soma)
    if t >= C["s23"]:
        a3, b3, c3 = C["s23.a"], C["s23.b"], C["s23.c"]
        E.frase(c, t, C["s23"] + 0.3, ps("quem lê", "i", 66) + [("2,3 h", "g", 70)] + ps("como", "i", 66) + [("2 h 30", "g", 70, ERRADO)], W / 2, 260, "center", 0.1)
        fcen(c, t, b3, "chega em 11 h 20", W / 2, 470, 100, ERRADO)
        fcen(c, t, b3 + 0.4, "o certo é 11 h 08", W / 2, 630, 100, CERTO)
        E.foco(c, t, c3, 0.5, lambda a: E.pilula(c, "12 minutos de erro por causa de uma vírgula", W / 2, 840, 64, "g", fundo=ERRADO, a=a, cor=BR))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s24.a", "antes da conta:", "tudo na mesma unidade"), ("s24.b", "no fim:", "a resposta faz sentido?"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 80) + [(l2, "g", 84, COR)], 320, y, "left", 0.1)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    a5, b5, c5 = C["s25.a"], C["s25.b"], C["s25.c"]
    E.frase(c, t, C["s25"] + 0.2, ps("fim da trilha de medidas", "i", 60, TINTA2), XE, 200, passo=0.1)
    E.frase(c, t, PW("s25", "Na"), ps("na próxima aula", "i", 76), XE, 310, passo=0.12)
    E.frase(c, t, a5, [("razão", "g", 150, COR)], XE, 480, passo=0.12)
    E.frase(c, t, b5, ps("3 meninos para 5 meninas", "i", 62), XE, 600, passo=0.08)
    E.foco(c, t, b5 + 1.4, 0.4, lambda a: E.formula(c, "= f{3}{5}", XE + 640, 615, 80, "g", COR, a))
    E.frase(c, t, c5, ps("comparar", "i", 62) + [("50 cm", "g", 66, COR)] + ps("com", "i", 62) + [("2 m", "g", 66, COR)], XE, 740, passo=0.08)
    E.foco(c, t, C["s25.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 780, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s25.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1000, 805, p), ep(t, C["s25.d"] + 0.2, 0.4))
    E.frase(c, t, C["s25.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
