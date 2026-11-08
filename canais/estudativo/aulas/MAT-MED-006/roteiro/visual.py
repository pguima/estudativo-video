"""Visual — Estudativo · MAT-MED-006: converter tempo e hora decimal.
Mesma linguagem da trilha (peças locais Escada e num_un, iguais às de MAT-MED-001): aqui a escada do TEMPO tem três degraus
(h, min, s) e cada degrau vale × 60, não × 10, por isso a vírgula não anda sozinha.
Peças locais novas: mostrador() (uma hora como relógio: o setor pintado é o pedaço de hora, com as 10 fatias de 6 minutos
quando o assunto são os décimos), horas() (uma fila de relógios: as horas inteiras cheias e o pedaço no último) e
barra_min() (uma faixa de minutos cortada em blocos de 60). Instantes: cues C[...] e a palavra falada (PW)."""
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
ARQUIVO_FINAL = "estudativo_MAT-MED-006_converter_tempo_e_hora_decimal.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("sessenta", "minutos", "decimal", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 0.2 * 60 == 12 and 20 - 12 == 8 and 2 * 60 + 15 == 135 and 60 / 4 == 15 and 150 - 2 * 60 == 30
assert 60 * 60 == 3600 and Fr(45, 60) == Fr(3, 4) and 3 / 4 == 0.75 and 60 / 10 == 6 and 6 * 2 == 12
assert 0.5 * 60 == 30 and [k * 6 for k in (1, 2, 5, 8)] == [6, 12, 30, 48] and Fr(25, 100) == Fr(1, 4)
assert 4 * 6 == 24 and 60 + 50 == 110 and 3 * 60 + 50 + 2 * 60 + 25 == 6 * 60 + 15

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


def horas(c, t, n, frac, x0, cy, r, gap, t0, passo=0.25, cor=None, decimos=0.0, tf=None, escuro=False):
    """n relógios cheios (horas inteiras) e, se frac, mais um com o pedaço; entram um a um a partir de t0 (o último em tf)"""
    for k in range(n + (1 if frac else 0)):
        ti = t0 + passo * k if (k < n or tf is None) else tf
        f = 1.0 if k < n else frac * ease_io(prog(t, ti, 0.8))
        E.foco(c, t, ti, 0.45, lambda a, k=k, f=f: mostrador(c, x0 + k * (2 * r + gap), cy, r, f, a, cor, decimos if k >= n else 0, escuro))


def fatias_rot(c, cx, cy, r, a=1.0, cor=None):
    """o número 6 em cada fatia de um décimo, por fora do relógio"""
    for k in range(10):
        ang = math.radians(-90 + 18 + k * 36)
        centro(c, "6", cx + math.cos(ang) * (r + 44), cy + math.sin(ang) * (r + 44) + 16, 42, "g", cor or TINTA2, a)


def barra_min(c, t, x, y, w, h, total, blocos, tb, a=1.0, rot=True):
    """faixa de `total` minutos: blocos = [(minutos, cor, rótulo)] que aparecem nos instantes tb"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 12, "#FFFFFF", a, stroke=3, stroke_color=TINTA)
    xx = x
    for (m, cor, r_), t0 in zip(blocos, tb):
        ww = w * m / total
        q = ep(t, t0, 0.5) * a
        if q > 0:
            M.rrect(c, xx + 4, y + 4, (ww - 8) * ease_io(prog(t, t0, 0.5)), h - 8, 10, cor, q)
            if rot:
                centro(c, r_, xx + ww / 2, y + h / 2 + 22, 60, "g", BR, q)
        xx += ww


ESC_T = Escada(x=140, y=380, sw=300, sh=150, base=960, un=("h", "min", "s"), nomes=("hora", "minuto", "segundo"), meio=0, size=90)


def vezes60(c, t, t0, i, cor=None, txt="× 60", a=1.0):
    """pílula do × 60 no espelho entre o degrau i e o i+1"""
    E.foco(c, t, t0, 0.45, lambda q: E.pilula(c, txt, ESC_T.x + (i + 1) * ESC_T.sw, ESC_T.topo(i + 1) - 120, 50, "g", fundo=cor or E.COR, a=q * a, cor=BR))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, PW("s01", "aplicativo"), ps("o aplicativo diz:", "i", 60, TINTA2), 160, 200, "left", 0.1)
        E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "2,2 h", 160, 380, 170, "g", TINTA, a))
        E.foco(c, t, kb, 0.5, lambda a: E.escreve(c, "= 2 h 20 min?", 160, 560, 110, "g", ERRADO, a))
        r = 120
        horas(c, t, 2, 0.2, 1060, 380, r, 40, ka + 0.3, tf=ka + 1.0)
        if t >= kb:
            E.foco(c, t, kb + 0.4, 0.4, lambda a: mostrador(c, 1060 + 2 * (2 * r + 40), 380, r, 0.2, a, marca=1 / 3))
        E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "8 min de diferença", 1420, 610, 54, "g", fundo=ERRADO, a=a, cor=BR))
        E.frase(c, t, kc, ps("vai chegar", "i", 76) + [("8 minutos antes", "g", 80, ERRADO)], W / 2, 880, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 280, passo=0.12)
        E.frase(c, t, PW("s02", "converter"), [("converter", "g", 88, COR)] + ps("horas em minutos", "i", 84), XE, 430, passo=0.12)
        E.frase(c, t, PW("s02", "ler"), ps("ler", "i", 84) + [("hora com vírgula", "g", 88, COR)], XE, 570, passo=0.12)
        E.frase(c, t, PW("s02", "sem"), ps("sem errar", "i", 84), XE, 700, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "fração de uma quantidade", "3/4 de 20 = 15"), ("s03.c", "decimal em fração", "0,2 = 2/10"), ("s03.d", "multiplicar", "decimais"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, l2=l2, y=y: E.formula(c, l2.replace("3/4", "f{3}{4}").replace("2/10", "f{2}{10}"), x + 44, y + 160, 60, "g", COR, a))
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(340, 580, q1), 820, q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, PW("s03", "Se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1010, "left", 0.12)


# ---------------- o tempo anda de 60 em 60 ----------------
def b_sessenta(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    E.frase(c, t, PW("s04", "Metro,"), [("m, g, L:", "g", 64)] + ps("de", "i", 60) + [("10 em 10", "g", 64, TINTA2)], 1060, 200, "left", 0.1)
    E.frase(c, t, PW("s04", "tempo,"), ps("o tempo,", "i", 64) + [("não", "g", 66, ERRADO)], 1060, 290, "left", 0.1)
    ESC_T.degraus(c, t, [b4 - 0.3, b4 - 0.1, c4 - 0.1], [b4, b4 + 0.4, c4 + 0.4])
    vezes60(c, t, PW("s04", "sessenta"), 0)
    vezes60(c, t, PW("s04", "sessenta", 2), 1)
    fcen(c, t, b4 + 0.3, "1 h = 60 min", 1460, 440, 76)
    fcen(c, t, c4 + 0.3, "1 min = 60 s", 1460, 550, 76)
    E.foco(c, t, d4, 0.5, lambda a: E.pilula(c, "de 60 em 60", 1460, 660, 64, "g", a=a, cor=E.SOBRE))
    if t >= C["s05"]:
        E.foco(c, t, a5, 0.4, lambda a: E.selo(c, 1110, 790, 40, False, a))
        E.frase(c, t, a5 + 0.1, ps("não basta andar", "i", 54) + ps("com a vírgula", "i", 54), 1170, 812, "left", 0.08)
        ESC_T.pulos(c, t, 0, [(b5, 1), (c5, 0)], C["s05"] + 0.3, rastro=False)
        E.foco(c, t, b5, 0.4, lambda a: E.escreve(c, "h → min: × 60", 1060, 920, 64, "g", COR, a))
        E.foco(c, t, c5, 0.4, lambda a: E.escreve(c, "min → h: ÷ 60", 1060, 1010, 64, "g", TINTA, a))


# ---------------- horas e minutos ----------------
def b_minutos(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    r = 150
    E.frase(c, t, C["s06"] + 0.3, ps("um filme de", "i", 70) + [("2 h 15 min", "g", 76, COR)], W / 2, 180, "center", 0.1)
    horas(c, t, 2, 0.25, 230, 430, r, 40, a6, tf=PW("s06", "quinze"))
    E.foco(c, t, b6, 0.4, lambda a: (centro(c, "60", 230, 650, 64, "g", COR, a), centro(c, "60", 230 + 2 * r + 40, 650, 64, "g", COR, a)))
    E.foco(c, t, c6, 0.4, lambda a: centro(c, "15", 230 + 2 * (2 * r + 40), 650, 64, "g", COR, a))

    def conta():
        fcen(c, t, b6 + 0.6, "2 × 60 = 120", 1500, 380, 84)
        fcen(c, t, c6, "120 + 15 = 135", 1500, 500, 84)
        bola_res(c, t, PW("s06", "cento", 2), "135 min", 1500, 720, 130, 60)
    E.saida(c, t, C["s07"] - 0.1, conta)
    if t >= C["s07"]:
        fcen(c, t, a7, "15 min = f{1}{4} h", 1500, 400, 90)
        fcen(c, t, PW("s07", "sessenta"), "60 ÷ 4 = 15", 1500, 540, 76, TINTA2)
        E.frase(c, t, b7, ps("o filme dura", "i", 60), 1500, 680, "center", 0.1)
        fcen(c, t, b7 + 0.6, "2 f{1}{4} h", 1500, 860, 140, COR)
        E.frase(c, t, c7, ps("número misto:", "i", 54, TINTA2) + ps("2 inteiros e 1/4", "i", 54, TINTA2), 1500, 1000, "center", 0.08)


def b_horas(c, t, C, b):
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    if t < C["s10"] + 0.4:
        def um():
            E.frase(c, t, C["s08"] + 0.3, ps("o caminho de volta:", "i", 66, TINTA2), W / 2, 180, "center", 0.1)
            E.foco(c, t, a8, 0.5, lambda a: centro(c, "150 min", W / 2, 340, 120, "g", TINTA, a))
            tq = PW("s08", "Quantas")
            barra_min(c, t, 260, 420, 1400, 150, 150, [(60, E.COR, "60"), (60, E.COR, "60"), (30, TINTA2, "30")], [b8 - 0.2, b8 + 0.3, c8],
                      ep(t, tq - 0.4, 0.4))
            E.frase(c, t, tq, ps("quantas vezes o", "i", 56) + [("60", "g", 60, COR)] + ps("cabe?", "i", 56), W / 2, 650, "center", 0.08)
            E.foco(c, t, b8, 0.4, lambda a: E.escreve(c, "2 × 60 = 120", 260, 780, 76, "g", TINTA, a))
            E.foco(c, t, c8, 0.4, lambda a: E.escreve(c, "sobram 30", 260, 900, 76, "g", TINTA2, a))
            bola_res(c, t, d8, "2 h 30 min", 1450, 830, 150, 56)
            E.foco(c, t, PW("s09", "meia"), 0.4, lambda a: E.pilula(c, "30 min = meia hora", 1450, 650, 54, "g", fundo=TINTA, a=a, cor=BR))
            fcen(c, t, a9, "= 2,5 h", 1450, 1040, 76, COR)
        E.saida(c, t, PW("s09", "segundos") - 0.3, um)
    if PW("s09", "segundos") - 0.3 <= t < C["s10"] + 0.4:
        def seg():
            E.frase(c, t, PW("s09", "segundos") - 0.2, ps("com", "i", 76) + [("segundos", "g", 80, COR)] + ps("é igual", "i", 76), W / 2, 260, "center", 0.12)
            fcen(c, t, b9, "1 h = 60 × 60 s", W / 2, 520, 120)
            bola_res(c, t, c9, "3.600 s", W / 2, 800, 170, 76)
        E.saida(c, t, C["s10"] - 0.1, seg)
    if t >= C["s10"]:
        a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
        E.frase(c, t, C["s10"] + 0.3, ps("menos de uma hora:", "i", 66, TINTA2), W / 2, 180, "center", 0.1)
        E.foco(c, t, a0, 0.5, lambda a: mostrador(c, 480, 560, 260, 0.75 * ep(t, a0 + 0.2, 1.0), a))
        E.foco(c, t, a0 + 0.3, 0.4, lambda a: centro(c, "45 min", 480, 900, 72, "g", COR, a))
        fcen(c, t, PW("s10", "São"), "f{45}{60}", 1100, 520, 120)
        E.foco(c, t, PW("s10", "Dividindo"), 0.4, lambda a: E.pilula(c, "÷ 15 em cima e embaixo", 1100, 680, 46, "g", fundo=TINTA, a=a, cor=BR))
        fcen(c, t, b0, "= f{3}{4} h", 1430, 520, 120, COR)
        bola_res(c, t, c0, "0,75 h", 1430, 840, 130, 70)


# ---------------- hora com vírgula ----------------
def b_decimal(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    a3, b3 = C["s13.a"], C["s13.b"]
    r = 130
    if t < C["s13"] + 0.4:
        def um():
            sz, x0 = 200, 200
            w2, w22 = E.larg("2", "g", sz), E.larg("2,2", "g", sz)
            E.foco(c, t, a1, 0.5, lambda a: E.escreve(c, "2,2 h", x0, 330, sz, "g", TINTA, a))
            if t >= b1:
                p = ep(t, b1, 0.4)
                E.caixa_pontilhada(c, x0 - 16, 160, w2 + 26, 210, p, prog_=p)
                E.foco(c, t, b1, 0.4, lambda a: centro(c, "2 h inteiras", x0 + w2 / 2, 440, 50, "i", TINTA2, a))
            if t >= c1:
                p = ep(t, c1, 0.4)
                E.caixa_pontilhada(c, x0 + w2 + 14, 160, w22 - w2 + 6, 210, p, COR, prog_=p)
                E.foco(c, t, c1 + 0.1, 0.4, lambda a: centro(c, "pedaço de hora", x0 + w2 + 120, 510, 50, "i", COR, a))
            horas(c, t, 2, 0.2, 1020, 290, 120, 40, b1, tf=c1, decimos=1.0)
            fcen(c, t, d1, "0,2 h = f{2}{10} de hora", 1100, 620, 76, COR)
            E.frase(c, t, PW("s11", "não"), ps("e", "i", 60) + [("não", "g", 64, ERRADO)] + ps("20 minutos", "i", 60, ERRADO), 1100, 740, "center", 0.1)
        E.saida(c, t, C["s12"] - 0.1, um)
    if C["s12"] <= t < C["s13"] + 0.4:
        def dois():
            cx, cy, R = 470, 560, 260
            E.foco(c, t, C["s12"], 0.5, lambda a: mostrador(c, cx, cy, R, 0.2 * ep(t, C["s12"] + 0.3, 0.8), a, decimos=1.0))
            E.foco(c, t, a2 + 0.6, 0.5, lambda a: fatias_rot(c, cx, cy, R, a, COR))
            fcen(c, t, PW("s12", "Dois"), "f{2}{10} de 60 min", 1350, 260, 80)
            E.frase(c, t, PW("s12", "divide"), ps("divide pelo de baixo:", "i", 56, TINTA2), 1350, 400, "center", 0.08)
            fcen(c, t, a2, "60 ÷ 10 = 6", 1350, 500, 84)
            E.frase(c, t, PW("s12", "Multiplica"), ps("multiplica pelo de cima:", "i", 56, TINTA2), 1350, 620, "center", 0.08)
            fcen(c, t, b2, "6 × 2 = 12", 1350, 720, 84)
            bola_res(c, t, c2, "2 h 12 min", 1350, 900, 140, 52)
        E.saida(c, t, C["s13"] - 0.1, dois)
    if t >= C["s13"]:
        E.frase(c, t, C["s13"] + 0.3, ps("a mesma conta,", "i", 70) + [("multiplicando o decimal", "g", 74, COR)], W / 2, 220, "center", 0.1)
        fcen(c, t, a3, "0,2 × 60", W / 2, 420, 130)
        fcen(c, t, PW("s13", "Sem"), "2 × 60 = 120", W / 2, 600, 96, TINTA2)
        tc = PW("s13", "Uma")
        E.foco(c, t, tc, 0.4, lambda a: E.pilula(c, "1 casa: 120 → 12,0", W / 2, 730, 60, "g", fundo=TINTA, a=a, cor=BR))
        bola_res(c, t, b3, "12 min", W / 2, 900, 120, 64)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, C["s14"] + 0.3, ps("o erro:", "i", 72) + [("ler os décimos como minutos", "g", 72, ERRADO)], W / 2, 180, "center", 0.1)
    E.foco(c, t, a4 + 0.4, 0.4, lambda a: E.escreve(c, "2,2 h ≠ 2 h 20 min", 200, 370, 84, "g", ERRADO, a))
    E.frase(c, t, b4, ps("só se a hora tivesse", "i", 60) + [("100 min", "g", 64, ERRADO)], 200, 500, "left", 0.1)
    E.frase(c, t, PW("s14", "Ela"), ps("ela tem", "i", 60) + [("60", "g", 66, COR)], 200, 600, "left", 0.1)
    E.foco(c, t, c4, 0.5, lambda a: mostrador(c, 1420, 560, 270, 0.5 * ep(t, c4 + 0.2, 0.8), a, marca=5 / 6 if t >= PW("s14", "cinquenta") else None))
    fcen(c, t, c4, "0,5 h = meia hora", 600, 780, 84, COR)
    E.frase(c, t, PW("s14", "trinta"), [("= 30 min", "g", 84, CERTO)] + ps("e não", "i", 70) + [("50", "g", 84, ERRADO)], 200, 920, "left", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a5, b5, c5, d5, e5, f5 = (C[f"s15.{k}"] for k in "abcdef")

    def um():
        E.frase(c, t, C["s15"] + 0.3, ps("agora, o atalho:", "i", 70, CLARO), W / 2, 150, "center", 0.1)
        E.frase(c, t, a5, ps("cada", "i", 88, CLARO) + [("décimo de hora", "g", 92, BR)] + ps("=", "i", 88, CLARO) + [("6 min", "g", 92, BR)], W / 2, 280, "center", 0.12)
        linhas = ((b5, "0,1", "6", 0.1), (c5, "0,2", "12", 0.2), (d5, "0,5", "30", 0.5), (e5, "0,8", "48", 0.8))
        atual = 0.0
        for i, (k, h, m, f) in enumerate(linhas):
            y = 430 + i * 125
            E.foco(c, t, k, 0.4, lambda a, h=h, y=y: E.escreve(c, f"{h} h", 220, y, 84, "g", BR, a))
            E.foco(c, t, k + 0.4, 0.4, lambda a, m=m, y=y: E.escreve(c, f"→ {m} min", 520, y, 84, "g", CLARO, a))
            if t >= k:
                atual = f
        E.foco(c, t, b5 - 0.3, 0.5, lambda a: mostrador(c, 1480, 640, 270, atual, a, decimos=1.0, escuro=True))
        E.foco(c, t, f5, 0.5, lambda a: E.pilula(c, "algarismo dos décimos × 6", 700, 960, 62, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s16"] - 0.1, um)
    if t < C["s16"]:
        return
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, C["s16"] + 0.2, ps("funciona porque", "i", 70, CLARO), W / 2, 220, "center", 0.1)
    fcen(c, t, a6, "60 ÷ 10 = 6", W / 2, 380, 110, BR)
    E.foco(c, t, b6, 0.5, lambda a: E.selo(c, 420, 590, 50, False, a))
    E.frase(c, t, b6 + 0.1, ps("não compensa com 2 casas:", "i", 70, CLARO) + [("0,25", "g", 80, BR)], 500, 615, "left", 0.1)
    E.frase(c, t, PW("s16", "troque"), ps("troque por", "i", 70, CLARO) + [("fração", "g", 76, BR)], W / 2, 760, "center", 0.1)
    fcen(c, t, c6, "0,25 = f{25}{100} = f{1}{4} h = 15 min", W / 2, 930, 80, CLARO)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    E.frase(c, t, C["s17"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a7 - 0.8, ps("uma entrega leva", "i", 70), XE, 350, passo=0.1)
    E.foco(c, t, a7, 0.5, lambda a: E.escreve(c, "3,4 h", XE + 520, 350, 100, "g", COR, a))
    E.frase(c, t, b7, ps("em", "i", 68) + [("horas e minutos?", "g", 72, COR)], XE, 450, passo=0.1)
    E.frase(c, t, c7 - 0.6, ps("um treino de", "i", 70), XE, 640, passo=0.1)
    E.foco(c, t, c7, 0.5, lambda a: E.escreve(c, "1 h 50 min", XE + 390, 640, 100, "g", COR, a))
    E.frase(c, t, d7, ps("quantos", "i", 68) + [("minutos?", "g", 72, COR)], XE, 740, passo=0.1)
    E.relogio(c, t, C["s18.a"], 1560, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    r = 110

    def um():
        E.foco(c, t, C["s19"] + 0.3, 0.5, lambda a: E.escreve(c, "3,4 h", 200, 260, 130, "g", TINTA, a))
        horas(c, t, 3, 0.4, 260, 480, r, 40, a9, tf=b9, decimos=1.0)
        E.foco(c, t, a9 + 0.2, 0.4, lambda a: centro(c, "3 h inteiras", 260 + (2 * r + 40), 650, 52, "i", TINTA2, a))
        fcen(c, t, b9, "0,4 → 4 × 6 = 24 min", 1400, 300, 76, COR)
        bola_res(c, t, c9, "3 h 24 min", 1400, 520, 150, 56)
        E.foco(c, t, PW("s19", "não"), 0.4, lambda a: E.escreve(c, "3 h 40 min", 1220, 790, 70, "g", ERRADO, a))
        if t >= PW("s19", "não") + 0.5:
            E.risco(c, 1210, 800, 1600, 740, t, PW("s19", "não") + 0.5, largura=10)
        E.frase(c, t, d9, [("0,4 < 0,5", "g", 60)] + ps("e", "i", 56) + [("24 < 30", "g", 60, CERTO)], 260, 860, "left", 0.1)
        E.frase(c, t, d9 + 0.8, ps("menos que meia hora", "i", 54, TINTA2), 260, 950, "left", 0.08)
    E.saida(c, t, C["s20"] - 0.1, um)
    if t < C["s20"]:
        return
    a0, b0, c0 = C["s20.a"], C["s20.b"], C["s20.c"]
    E.frase(c, t, C["s20"] + 0.3, ps("treino:", "i", 70) + [("1 h 50 min", "g", 76, COR)], W / 2, 200, "center", 0.1)
    barra_min(c, t, 360, 330, 1200, 140, 120, [(60, E.COR, "60"), (50, TINTA2, "50")], [a0, PW("s20", "cinquenta:")], ep(t, C["s20"] + 0.3, 0.4))
    fcen(c, t, b0, "60 + 50 = 110", 760, 680, 96)
    bola_res(c, t, PW("s20", "cento"), "110 min", 1420, 680, 140, 66)
    E.frase(c, t, c0 - 1.4, ps("um pouco menos que", "i", 60) + [("2 h = 120 min", "g", 64, COR)], W / 2, 920, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s21.a", "o tempo anda", "de 60 em 60"), ("s21.b", "cada décimo de hora =", "6 min"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 58, a=a), centro(c, str(i + 1), 260, y - 7, 66, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 86) + [(l2, "g", 90, COR)], 360, y, "left", 0.12)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a2, b2, c2 = C["s22.a"], C["s22.b"], C["s22.c"]
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 80), XE, 240, passo=0.12)
    E.frase(c, t, a2, [("somar", "g", 110, COR)] + ps("e", "i", 100) + [("subtrair", "g", 110, COR)] + ps("horas", "i", 100), XE, 400, passo=0.12)
    E.frase(c, t, b2, [("3 h 50 min + 2 h 25 min", "g", 72)], XE, 530, passo=0.1)
    E.frase(c, t, c2, ps("trocando", "i", 66) + [("60 min por 1 h", "g", 70, COR)], XE, 640, passo=0.1)
    E.foco(c, t, C["s22.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s22.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1010, 815, p), ep(t, C["s22.d"] + 0.2, 0.4))
    E.frase(c, t, C["s22.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, sessenta=b_sessenta, minutos=b_minutos, horas=b_horas, decimal=b_decimal,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
