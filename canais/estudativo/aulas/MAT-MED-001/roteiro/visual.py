"""Visual — Estudativo · MAT-MED-001: converter comprimento, a escada do metro.
A linguagem da trilha Medidas e Unidades é a ESCADA (peças locais abaixo, iguais em toda a trilha): degraus que descem da
esquerda para a direita, da unidade maior para a menor, com a unidade principal no degrau do meio, cheio da cor da matéria.
Uma bolinha pula de degrau em degrau e deixa um arco numerado (1, 2, 3...); no mesmo instante, a vírgula do número anda
uma casa por degrau (E.anda) e a unidade ao lado do número troca. Descer = vírgula para a direita, como a escada.
Instantes: cues C[...] e, dentro da frase, a palavra falada (PW), lida de audio/tempos.json."""
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
ARQUIVO_FINAL = "estudativo_MAT-MED-001_converter_comprimento_escada_do_metro.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("unidade", "escada", "km", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 2.5 * 1000 == 2500 and 340 / 100 == 3.4 and 45 / 10 == 4.5 and 340 * 100 == 34000
assert 1.2 * 100000 == 120000 and 1.8 * 1000 == 1800 and 1800 + 950 == 2750 and abs(1.70 / 1000 - 0.0017) < 1e-12

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


def num_un(c, t, dig, pos, saltos, x, y, size, unidades, cor=None, tv=None, some=False, t0=None, cor_un=None):
    """número com a vírgula que anda (E.anda) e a unidade logo depois dele, que troca a cada salto.
    unidades = [(instante, "km"), ...]; a primeira entra em t0. Devolve px (centro de cada casa)."""
    if t0 is not None and t < t0:
        return None
    a0 = ep(t, t0, 0.5) if t0 is not None else 1.0
    c.saveLayer(None, M.paint("#000000", a0)) if a0 < 1 else None
    px = E.anda(c, t, dig, pos, saltos, x, y, size, cor=cor, tv=tv, some=some)
    cl = E.casa(size)
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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    tq = PW("s01", "Quantos")

    def um():
        E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "2,5 km", 300, 330, 170, "g", TINTA, a))
        E.foco(c, t, tq, 0.5, lambda a: E.escreve(c, "=", 900, 330, 170, "g", TINTA, a))
        if t < kb:
            E.foco(c, t, tq + 0.1, 0.5, lambda a: E.escreve(c, "? m", 1080, 330, 170, "g", CINZA, a))
        else:
            E.foco(c, t, kb, 0.4, lambda a: E.escreve(c, "250 m", 1080, 330, 170, "g", ERRADO, a))
        # a corrida: uma pista de 2,5 km; a de 250 m tem um décimo do tamanho
        x0, x1, y = 260, 1660, 560
        p = ep(t, ka + 0.4, 0.9)
        if p > 0:
            M.line(c, x0, y, lerp(x0, x1, p), y, E.COR, 1.0, 26)
            E.foco(c, t, ka + 1.0, 0.4, lambda a: (E.escreve(c, "corrida de 2,5 km", x0, y - 44, 52, "i", TINTA2, a),
                                                    M.line(c, x1, y - 60, x1, y + 60, TINTA, a, 6)))
        q = ep(t, kc, 0.8)
        if q > 0:
            y2 = 700
            M.line(c, x0, y2, x0 + (x1 - x0) / 10 * q, y2, ERRADO, 1.0, 26)
            E.foco(c, t, kc + 0.3, 0.4, lambda a: E.escreve(c, "250 m", x0 + 170, y2 + 18, 56, "g", ERRADO, a))
        E.frase(c, t, PW("s01", "dez"), ps("encolheu", "i", 84) + [("10 vezes", "g", 84, ERRADO)], W / 2, 900, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 280, passo=0.12)
        E.frase(c, t, PW("s02", "escolher"), ps("escolher a", "i", 84) + [("unidade certa", "g", 88, COR)], XE, 430, passo=0.12)
        E.frase(c, t, PW("s02", "converter"), [("converter", "g", 88, COR)] + ps("comprimentos", "i", 84), XE, 570, passo=0.12)
        E.frase(c, t, PW("s02", "sem"), ps("sem decorar tabela", "i", 84), XE, 710, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 190, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, 170, w, 196, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("andar com", "i", 62)], x + 44, 254)
    E.frase(c, t, C["s03.b"] + 0.3, [("a vírgula", "g", 62, COR)], x + 44, 330)
    tm, td = PW("s03", "Vezes"), PW("s03", "Dividido")
    hm, hd = PW("s03", "vai"), PW("s03", "dá")
    size = 160
    xn = 1360 - E.casa(size)
    if t >= tm - 0.6:
        c.saveLayer(None, M.paint("#000000", ep(t, tm - 0.6, 0.5)))
        E.anda(c, t, "37", 1, [(hm, 2), (hd, 1)], xn, 660, size)
        c.restore()
    E.foco(c, t, tm, 0.4, lambda a: E.pilula(c, "× 10", 1080, 600, 60, "g", a=a * (1 - ep(t, td, 0.3)), cor=E.SOBRE))
    E.foco(c, t, td, 0.4, lambda a: E.pilula(c, "÷ 10", 1080, 600, 60, "g", fundo=TINTA, a=a, cor=BR))
    E.saida(c, t, td, lambda: E.frase(c, t, hm, ps("1 casa para a", "i", 60) + [("direita →", "g", 60, COR)], 1360, 820, "center", 0.1))
    E.frase(c, t, hd, [("← esquerda", "g", 60, TINTA)] + ps("1 casa para a", "i", 60), 1360, 820, "center", 0.1)
    E.frase(c, t, PW("s03", "Se"), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1000, "left", 0.12)


# ---------------- escolher a unidade ----------------
def regua(c, t, x, y, cm, px_cm, tc, tmm, a=1.0):
    """régua de `cm` centímetros a partir de x: traços de cm (com número) em tc, risquinhos de mm em tmm"""
    q = ep(t, tc, 0.5) * a
    if q <= 0:
        return
    M.rrect(c, x - 30, y - 130, cm * px_cm + 60, 150, 14, "#FFFFFF", q, stroke=3, stroke_color=TINTA2)
    for k in range(cm + 1):
        xx = x + k * px_cm
        M.line(c, xx, y - 130, xx, y - 60, TINTA, q, 5)
        centro(c, str(k), xx, y - 14, 44, "b", TINTA, q)
    m = ep(t, tmm, 0.6) * a
    if m > 0:
        for k in range(cm * 10):
            if k % 10:
                xx = x + k * px_cm / 10
                M.line(c, xx, y - 130, xx, y - (90 if k % 5 == 0 else 100), COR, m, 3)


def b_unidade(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]

    def um():
        E.foco(c, t, a4, 0.5, lambda a: E.escreve(c, "2,5", 560, 520, 230, "g", TINTA, a))
        E.foco(c, t, a4 + 0.2, 0.5, lambda a: E.escreve(c, "km", 1020, 520, 230, "g", COR, a))
        tn, tu = PW("s04", "número"), PW("s04", "unidade")
        E.foco(c, t, tn, 0.4, lambda a: (E.chave(c, 560, 920, 580, TINTA2, a, 26), centro(c, "número", 740, 690, 64, "i", TINTA2, a)))
        E.foco(c, t, tu, 0.4, lambda a: (E.chave(c, 1020, 1370, 580, COR, a, 26), centro(c, "unidade", 1195, 690, 64, "i", COR, a)))
        E.frase(c, t, C["s04"] + 0.3, ps("toda medida tem", "i", 76), W / 2, 220, "center", 0.12)
    E.saida(c, t, b4 - 0.6, um)
    if b4 - 0.6 <= t < C["s05"] + 0.4:
        def metro():
            E.frase(c, t, b4 - 0.4, ps("a unidade principal:", "i", 76) + [("o metro", "g", 84, COR)], W / 2, 240, "center", 0.12)
            x0, x1, y = 560, 1360, 640
            p = ep(t, b4 + 0.3, 0.8)
            if p > 0:
                M.line(c, x0, y, lerp(x0, x1, p), y, E.COR, 1.0, 10)
                for xx in (x0, x1):
                    M.line(c, xx, y - 34, xx, y + 34, E.COR, p, 8)
            E.foco(c, t, b4 + 0.8, 0.4, lambda a: centro(c, "1 m", (x0 + x1) / 2, y - 60, 90, "g", COR, a))
            tp = PW("s04", "passo")
            for k, xx in enumerate((x0, x1)):  # duas pegadas: um passo bem largo
                E.foco(c, t, tp - 0.2 + 0.25 * k, 0.4, lambda a, xx=xx, k=k: pegada(c, xx, y + 130, a, k))
            E.frase(c, t, tp, [("≈", "g", 70, TINTA)] + ps("um", "i", 70) + [("passo bem largo", "g", 70, COR)], W / 2, 920, "center", 0.12)
        E.saida(c, t, C["s05"] - 0.1, metro)
    if C["s05"] <= t < C["s06"] + 0.4:
        def tres():
            col = ((360, "km", "quilômetro", "1 km = 1.000 m", "entre duas cidades", C["s05.a"], PW("s05", "mil"), PW("s05", "cidades")),
                   (960, "cm", "centímetro", "1 cm = f{1}{100} m", "um lápis", C["s05.b"], PW("s05", "centésima"), PW("s05", "lápis")),
                   (1560, "mm", "milímetro", "1 mm = f{1}{1.000} m", "risquinhos da régua", C["s05.c"], PW("s05", "milésima"), PW("s05", "risquinhos")))
            for cx, u, nome, rel, ex, k, tr, te in col:
                E.foco(c, t, k, 0.5, lambda a, cx=cx, u=u: centro(c, u, cx, 270, 170, "g", COR, a))
                E.foco(c, t, k + 0.2, 0.5, lambda a, cx=cx, nome=nome: centro(c, nome, cx, 350, 60, "i", TINTA, a))
                fcen(c, t, tr, rel, cx, 490, 64)
                E.foco(c, t, te - 0.2, 0.5, lambda a, cx=cx, ex=ex: centro(c, ex, cx, 620, 52, "i", TINTA2, a))
            regua(c, t, 760, 900, 3, 330, C["s05.b"] + 1.0, PW("s05", "risquinhos"))
        E.saida(c, t, C["s06"] - 0.1, tres)
    if t >= C["s06"]:
        a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
        E.frase(c, t, a6 - 0.3, ps("a unidade que deixa", "i", 76) + [("o número fácil de ler", "g", 76, COR)], W / 2, 190, "center", 0.11)
        E.frase(c, t, PW("s06", "altura"), ps("altura de uma pessoa", "i", 60, TINTA2), W / 2, 310, "center", 0.1)
        E.foco(c, t, b6, 0.5, lambda a: E.escreve(c, "1,70 m", 600, 480, 130, "g", TINTA, a))
        E.foco(c, t, b6 + 0.8, 0.4, lambda a: E.selo(c, 1300, 440, 44, True, a))
        E.foco(c, t, c6, 0.5, lambda a: E.escreve(c, "170 cm", 600, 660, 130, "g", TINTA, a))
        E.foco(c, t, c6 + 0.8, 0.4, lambda a: E.selo(c, 1300, 620, 44, True, a))
        E.foco(c, t, d6, 0.5, lambda a: E.escreve(c, "0,0017 km", 600, 860, 130, "g", ERRADO, a))
        E.foco(c, t, d6 + 1.6, 0.4, lambda a: E.selo(c, 1440, 820, 44, False, a))
        E.frase(c, t, PW("s06", "Ninguém"), ps("ninguém diz", "i", 54, ERRADO), 600, 950, "left", 0.1)


def pegada(c, x, y, a, k):
    """pegada estilizada: sola e dedos"""
    if a <= 0:
        return
    cor = E.mix(E.COR, "#FFFFFF", 0.35)
    c.save(); c.translate(x, y); c.rotate(-8 if k == 0 else 8)
    c.drawOval(skia.Rect.MakeXYWH(-26, -40, 52, 90), M.paint(cor, a))
    for i, (dx, dy, r) in enumerate(((-20, -58, 9), (-6, -66, 9), (8, -64, 8), (20, -56, 7))):
        c.drawCircle(dx, dy, r, M.paint(cor, a))
    c.restore()


# ---------------- a escada ----------------
ESC = Escada()


def b_escada(c, t, C, b):
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    tl = [PW("s07", "quilômetro"), PW("s07", "hectômetro"), PW("s07", "decâmetro"), b7, d7 + 0.8, PW("s07", "centímetro"), PW("s07", "milímetro")]
    td = [a7 + 0.25 * i for i in range(7)]

    def esc():
        E.frase(c, t, a7, ps("uma escada de", "i", 70) + [("7 degraus", "g", 74, COR)], 1060, 170, "left", 0.12)
        ESC.degraus(c, t, td, tl)
        a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
        fase(c, t, a8, c8 - 0.2, lambda: (
            E.frase(c, t, a8, ps("cada degrau vale", "i", 64) + [("10 ×", "g", 70, COR)], 1060, 300, "left", 0.1),
            E.frase(c, t, a8 + 0.9, ps("o de baixo", "i", 64), 1060, 380, "left", 0.1),
            E.foco(c, t, b8, 0.5, lambda a: E.pilula(c, "1 degrau = 1 casa", 1420, 500, 60, "g", a=a, cor=E.SOBRE))))
        if t >= c8 - 0.2:
            ESC.pulos(c, t, 3, [(c8, 4), (d8, 3)], c8 - 0.2, rastro=False)
            fase(c, t, c8, d8 - 0.1, lambda: (
                E.frase(c, t, c8, [("descendo:", "g", 70, COR)] + ps("o número cresce", "i", 66), 1060, 300, "left", 0.1),
                E.frase(c, t, PW("s08", "vírgula", 2), ps("vírgula para a", "i", 66) + [("direita →", "g", 70, COR)], 1060, 400, "left", 0.1)))
            if t >= d8 - 0.1:
                E.frase(c, t, d8, [("subindo:", "g", 70, TINTA)] + ps("o número diminui", "i", 66), 1060, 300, "left", 0.1)
                E.frase(c, t, PW("s08", "vírgula", 3), [("← esquerda", "g", 70, TINTA)] + ps("vai a vírgula", "i", 66), 1060, 400, "left", 0.1)
    E.saida(c, t, C["s09"] - 0.1, esc)
    if t >= C["s09"]:
        a9, b9 = C["s09.a"], C["s09.b"]
        E.frase(c, t, a9, ps("em", "i", 80) + [("1 metro", "g", 84, COR)] + ps("cabem", "i", 80) + [("100 centímetros", "g", 84, COR)],
                W / 2, 250, "center", 0.12)
        x0, x1, y = 260, 1660, 520
        p = ep(t, a9, 0.6)
        if p > 0:
            M.rrect(c, x0, y, (x1 - x0) * p, 110, 10, "#FFFFFF", 1.0, stroke=3, stroke_color=TINTA)
        tc = PW("s09", "cem")
        for k in range(1, 100):
            q = ep(t, tc + 1.2 * k / 100, 0.2)
            if q > 0:
                xx = x0 + (x1 - x0) * k / 100
                M.line(c, xx, y + 6, xx, y + (104 if k % 10 == 0 else 50), E.COR if k % 10 == 0 else TINTA2, q, 4 if k % 10 == 0 else 2)
        E.foco(c, t, a9 + 0.4, 0.4, lambda a: centro(c, "1 m", (x0 + x1) / 2, y - 30, 64, "g", TINTA, a))
        E.foco(c, t, tc + 1.2, 0.4, lambda a: centro(c, "100 pedacinhos de 1 cm", (x0 + x1) / 2, y + 190, 56, "i", TINTA2, a))
        E.frase(c, t, b9, ps("unidade menor,", "i", 84) + [("mais pedaços", "g", 88, COR)], W / 2, 880, "center", 0.12)


# ---------------- quilômetro para metro ----------------
XN, YN, SN = 1080, 420, 140  # onde fica o número que anda, na direita da escada


def b_km(c, t, C, b):
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    h3 = PW("s10", "quinhentos") - 0.7
    hops = [(c0, 1), (d0, 2), (h3, 3)]

    def esc():
        ESC.degraus(c, t, C["s10"], acesos=(0, 1, 2), ta=b0)
        ESC.pulos(c, t, 0, hops, a0)
        E.frase(c, t, a0, ps("2,5 km em", "i", 64) + [("metros", "g", 64, COR)], 1060, 170, "left", 0.1)
        num_un(c, t, "25", 1, [(c0, 2), (d0, 3), (h3, 4)], XN, YN, SN, [(a0, "km"), (c0 + 0.7, "hm"), (d0 + 0.7, "dam"), (h3 + 0.7, "m")], t0=a0)
        E.foco(c, t, b0, 0.5, lambda a: E.pilula(c, "3 degraus para baixo", 1420, 540, 54, "g", a=a, cor=E.SOBRE))
        tz = PW("s10", "completando")
        if t >= tz:
            cl = E.casa(SN)
            p = ep(t, tz, 0.5)
            E.caixa_pontilhada(c, XN + 2 * cl - 8, YN - SN * 0.9, 2 * cl + 16, SN * 1.15, p, prog_=p)
    E.saida(c, t, C["s11"] - 0.1, esc)
    if t >= C["s11"]:
        a1, b1 = C["s11.a"], C["s11.b"]
        fcen(c, t, a1 - 0.2, "2,5 km", 560, 330, 130)
        E.foco(c, t, a1 - 0.2, 0.4, lambda a: M.arrow(c, 820, 290, 1000, 290, TINTA, a, 6, 20))
        bola_res(c, t, a1, "2.500 m", 1330, 290, 210, 96)
        fcen(c, t, b1, "2,5 × 1.000 = 2.500", W / 2, 680, 110)
        tz = PW("s11", "mil", 2)
        if t >= tz:
            x0 = W / 2 - E.formula(None, "2,5 × 1.000 = 2.500", 0, 0, 110, a=0) / 2 + E.formula(None, "2,5 × 1", 0, 0, 110, a=0)
            w = E.formula(None, ".000", 0, 0, 110, a=0)
            M.rrect(c, x0 - 4, 580, w + 8, 130, 16, E.COR, 0.16 * ep(t, tz, 0.4))
        E.frase(c, t, tz, ps("mil tem", "i", 70) + [("3 zeros", "g", 74, COR)] + ps("=", "i", 70) + [("3 casas", "g", 74, COR)], W / 2, 880, "center", 0.12)


# ---------------- centímetro para metro ----------------
def b_cm(c, t, C, b):
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    a3, b3, c3, d3 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    tz = PW("s13", "zero")

    def tres40():
        ESC.degraus(c, t, C["s12"], acesos=(3, 4, 5), ta=b2)
        ESC.pulos(c, t, 5, [(a3, 4), (b3, 3)], a2)
        E.frase(c, t, a2, ps("340 cm em", "i", 64) + [("metros", "g", 64, COR)], 1060, 170, "left", 0.1)
        px = num_un(c, t, "340", 3, [(a3, 2), (b3, 1)], XN, YN, SN, [(a2, "cm"), (a3 + 0.7, "dm"), (b3 + 0.7, "m")], tv=c2, t0=a2)
        E.foco(c, t, b2, 0.5, lambda a: E.pilula(c, "2 degraus para cima", 1420, 540, 54, "g", fundo=TINTA, a=a, cor=BR))
        if c2 <= t < a3:
            p = ep(t, c2, 0.4)
            cl = E.casa(SN)
            E.caixa_pontilhada(c, XN + 3 * cl - 28, YN - SN * 0.9, 56, SN * 1.15, p, prog_=p)
        if px and t >= tz:
            E.risco(c, px(2) - 40, YN + 10, px(2) + 40, YN - 100, t, tz, largura=10)
        bola_res(c, t, PW("s13", "três", 2), "3,4 m", 1680, 760, 150, 84)
    E.saida(c, t, C["s14"] - 0.1, tres40)
    if C["s13.d"] <= t < C["s14"] + 0.4:
        E.saida(c, t, C["s14"] - 0.1, lambda: E.frase(c, t, d3, ps("o mesmo que", "i", 62) + [("÷ 100", "g", 66, COR)], 1060, 272, "left", 0.1))
    if t >= C["s14"]:
        a4, b4 = C["s14.a"], C["s14.b"]
        hop = PW("s14", "Um", 2)
        ESC.degraus(c, t, C["s14"] - 0.1, acesos=(5, 6), ta=hop)
        ESC.pulos(c, t, 6, [(hop, 5)], a4)
        E.frase(c, t, a4, ps("45 mm em", "i", 64) + [("centímetros", "g", 64, COR)], 1060, 170, "left", 0.1)
        num_un(c, t, "45", 2, [(hop + 0.3, 1)], XN, YN, SN, [(a4, "mm"), (hop + 1.0, "cm")], tv=a4 + 0.4, t0=a4)
        E.foco(c, t, PW("s14", "uma"), 0.5, lambda a: E.pilula(c, "1 casa para a esquerda", 1420, 540, 50, "g", fundo=TINTA, a=a, cor=BR))
        bola_res(c, t, b4, "4,5 cm", 1680, 790, 140, 76)


# ---------------- erro ----------------
def sala(c, x, y, w, h, a):
    """planta de uma sala: paredes grossas e a porta"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 6, "#FFFFFF", a, stroke=10, stroke_color=TINTA)
    M.line(c, x + w * 0.62, y + h, x + w * 0.62 + 90, y + h, "#FFFFFF", a, 14)
    M.line(c, x + w * 0.62, y + h, x + w * 0.62 + 70, y + h - 70, TINTA2, a, 4)


def b_erro(c, t, C, b):
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]

    def um():
        E.frase(c, t, a5 - 0.3, ps("o erro:", "i", 76) + [("andar para o lado errado", "g", 76, ERRADO)], W / 2, 180, "center", 0.11)
        fcen(c, t, a5 + 1.0, "340 cm", 420, 420, 120)
        E.foco(c, t, PW("s15", "multiplica"), 0.4, lambda a: (M.arrow(c, 660, 380, 860, 380, ERRADO, a, 6, 20),
                                                             E.pilula(c, "× 100", 760, 300, 50, "g", fundo=ERRADO, a=a, cor=BR)))
        fcen(c, t, PW("s15", "trinta"), "34.000 m", 1210, 420, 120, ERRADO)
        fcen(c, t, PW("s15", "quilômetros"), "= 34 km", 1210, 560, 90, ERRADO)
        E.foco(c, t, c5 - 0.4, 0.5, lambda a: sala(c, 620, 680, 520, 260, a))
        E.foco(c, t, c5 - 0.2, 0.5, lambda a: centro(c, "3,4 m", 880, 830, 70, "g", COR, a))
        E.frase(c, t, c5, ps("cabe numa", "i", 70) + [("sala!", "g", 74, COR)], 1200, 840, "left", 0.1)
    E.saida(c, t, C["s16"] - 0.1, um)
    if t >= C["s16"]:
        a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
        E.frase(c, t, a6 - 0.2, ps("pergunte:", "i", 70, TINTA2), W / 2, 170, "center")
        E.frase(c, t, PW("s16", "unidade"), ps("a unidade ficou", "i", 80) + [("maior", "g", 84, COR)] + ps("ou", "i", 80) + [("menor?", "g", 84, COR)],
                W / 2, 290, "center", 0.12)
        E.foco(c, t, b6, 0.5, lambda a: E.pilula(c, "unidade maior → número menor", W / 2, 450, 76, "g", a=a, cor=E.SOBRE))
        fcen(c, t, c6, "m > cm", 560, 700, 130)
        fcen(c, t, PW("s16", "então"), "340 → 3,4", 1300, 700, 130, CERTO)
        E.frase(c, t, PW("s16", "diminuir") - 0.3, ps("o número", "i", 70) + [("diminui", "g", 74, CERTO)], 1300, 850, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
ESC_P = Escada(x=110, y=380, sw=150, sh=62, base=930, size=52)


def b_atalho(c, t, C, b):
    palco(c, t)
    a7, b7, c7, d7 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]

    def nomes():
        E.frase(c, t, C["s17"] + 0.3, ps("agora, o atalho:", "i", 70, CLARO), W / 2, 150, "center", 0.1)
        E.frase(c, t, a7, ps("o nome já diz", "i", 92, CLARO) + [("a conta", "g", 96, BR)], W / 2, 280, "center", 0.12)
        linhas = ((b7, "quilo", "= mil", "1 km = 1.000 m", "3 casas", PW("s17", "um"), PW("s17", "três")),
                  (c7, "centi", "= centésimo", "100 cm = 1 m", "2 casas", PW("s17", "cem"), PW("s17", "duas")),
                  (d7, "mili", "= milésimo", "1.000 mm = 1 m", "3 casas", PW("s17", "mil", 3), PW("s17", "três", 2)))
        for i, (k, pre, sig, eq, cs, te, tc) in enumerate(linhas):
            y = 480 + i * 190
            E.foco(c, t, k, 0.5, lambda a, pre=pre, y=y: E.escreve(c, pre, 150, y, 96, "g", BR, a))
            E.foco(c, t, k + 0.6, 0.5, lambda a, sig=sig, y=y: E.escreve(c, sig, 470, y, 80, "i", CLARO, a))
            E.foco(c, t, te, 0.5, lambda a, eq=eq, y=y: E.escreve(c, eq, 920, y, 76, "g", BR, a))
            E.foco(c, t, tc, 0.5, lambda a, cs=cs, y=y: E.pilula(c, cs, 1640, y - 28, 58, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s18"] - 0.1, nomes)
    if t < C["s18"]:
        return
    a8, b8, c8, d8 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]

    def regra():
        E.frase(c, t, C["s18"] + 0.1, ps("o começo do nome", "i", 84, CLARO) + [("é o próprio degrau", "g", 88, BR)], W / 2, 260, "center", 0.12)
        E.foco(c, t, b8, 0.5, lambda a: E.selo(c, 420, 520, 50, False, a))
        E.frase(c, t, b8 + 0.1, ps("não compensa:", "i", 76, CLARO) + [("km → cm", "g", 84, BR)], 500, 545, "left", 0.1)
        E.frase(c, t, PW("s18", "conte"), ps("aí,", "i", 84, CLARO) + [("conte os degraus", "g", 88, BR)], W / 2, 800, "center", 0.12)
    E.saida(c, t, c8 - 0.2, regra)
    if t >= c8 - 0.2:
        h0 = PW("s18", "cinco")
        hops = [(h0 + 0.7 * k - 0.3, k + 1) for k in range(5)]
        E.frase(c, t, c8, ps("1,2 km em", "i", 72, CLARO) + [("centímetros", "g", 76, BR)], 110, 170, "left", 0.1)
        ESC_P.degraus(c, t, c8 - 0.1, acesos=(0, 1, 2, 3, 4, 5), ta=h0, escuro=True, nomes=False)
        ESC_P.pulos(c, t, 0, hops, c8, escuro=True, cor=E.COR)
        num_un(c, t, "12", 1, [(th, j + 1) for th, j in hops], 1000, 320, 104, [(c8, "km")] + [(th + 0.7, ESC_P.un[j]) for th, j in hops],
               cor=BR, t0=c8, cor_un=CLARO, some=True)
        E.foco(c, t, PW("s18", "casas"), 0.5, lambda a: E.pilula(c, "5 degraus = 5 casas", 1500, 470, 54, "g", a=a, cor=E.SOBRE))
        bola_res(c, t, d8, "120.000 cm", 1540, 760, 190, 70)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s19.a"] - 0.8, ps("caminhou", "i", 80), XE, 360, passo=0.1)
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.escreve(c, "1,8 km", XE, 500, 130, "g", COR, a))
    E.frase(c, t, C["s19.a"] + 1.4, ps("de manhã", "i", 72), XE + 580, 500, passo=0.1)
    E.frase(c, t, C["s19.b"] - 0.4, ps("e", "i", 80), XE, 660, passo=0.1)
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.escreve(c, "950 m", XE + 70, 660, 130, "g", COR, a))
    E.frase(c, t, C["s19.b"] + 1.4, ps("à tarde", "i", 72), XE + 580, 660, passo=0.1)
    E.frase(c, t, C["s19.c"], ps("quantos", "i", 92) + [("metros", "g", 96, COR)] + ps("no dia?", "i", 92), XE, 860, passo=0.12)
    E.relogio(c, t, C["s20.a"], 1560, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a1, b1, c1 = C["s21.a"], C["s21.b"], C["s21.c"]
    a2, b2, c2 = C["s22.a"], C["s22.b"], C["s22.c"]
    hs = [PW("s21", "quilômetro") + 0.6 * k for k in range(3)]

    def um():
        E.frase(c, t, a1, ps("tudo na", "i", 80) + [("mesma unidade", "g", 84, COR)], W / 2, 200, "center", 0.12)
        num_un(c, t, "18", 1, [(h, k + 2) for k, h in enumerate(hs)], 700, 520, 160, [(a1 + 0.4, "km"), (hs[-1] + 0.7, "m")], t0=a1 + 0.4, some=True)
        E.foco(c, t, b1, 0.5, lambda a: E.pilula(c, "km → m: 3 casas →", W / 2, 690, 62, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, c1, [("1,8 km", "g", 80)] + ps("vira", "i", 80) + [("1.800 m", "g", 84, COR)], W / 2, 880, "center", 0.12)
    E.saida(c, t, C["s22"] - 0.1, um)
    if t < C["s22"]:
        return
    tr = [PW("s22", "cinquenta", 2) - 0.2, PW("s22", "cinquenta", 2), PW("s22", "setecentos"), PW("s22", "dois")]
    E.armada(c, t, ["1800", "950"], "+", "2750", [a2, PW("s22", "novecentos")], sorted(tr), 820, 330, 120)
    E.foco(c, t, PW("s22", "metros"), 0.5, lambda a: centro(c, "m", 900, 620, 80, "g", COR, a))
    bola_res(c, t, PW("s22", "metros") + 0.3, "2.750 m", 1420, 440, 190, 84, CERTO)
    tc = c2
    fcen(c, t, tc, "1,8 + 950", 760, 900, 96, ERRADO)
    if t >= tc + 1.2:
        E.risco(c, 540, 920, 980, 820, t, tc + 1.2, largura=12)
    E.frase(c, t, PW("s22", "mistura"), ps("mistura", "i", 70) + [("km com m", "g", 74, ERRADO)], 1080, 900, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s23.a", "cada degrau,", "uma casa"), ("s23.b", "unidade menor,", "número maior"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 60, a=a), centro(c, str(i + 1), 300, y - 7, 68, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 92) + [(l2, "g", 96, COR)], 400, y, "left", 0.12)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    a4, b4 = C["s24.a"], C["s24.b"]
    E.frase(c, t, C["s24"] + 0.2, ps("na próxima aula, a mesma escada", "i", 76), XE, 240, passo=0.12)
    E.frase(c, t, a4, [("massa", "g", 120, COR)] + ps("e", "i", 110) + [("capacidade", "g", 120, COR)], XE, 420, passo=0.12)
    E.frase(c, t, b4, ps("tonelada em quilos,", "i", 66) + ps("mililitros em litros", "i", 66), XE, 540, passo=0.1)
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, unidade=b_unidade, escada=b_escada, km=b_km, cm=b_cm, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
