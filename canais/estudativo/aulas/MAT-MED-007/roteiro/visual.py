"""Visual — Estudativo · MAT-MED-007: somar e subtrair horas.
Mesma família visual da trilha Medidas e Unidades (tipografia, pílulas de "× 60", bola do resultado). Peças locais novas:
hm() (horas e minutos em duas colunas fixas, h e min, com o cabeçalho; a conta armada de horas é feita com elas, uma linha
por parcela, e a troca de 60 aparece como seta do minuto para a hora ou como número riscado e reescrito, igual a E.corta),
linha() (a linha do tempo de um horário a outro, com os saltos de E.salto, para o atalho de contar para a frente) e
ovos() (doze ovos que viram uma dúzia). Instantes: cues C[...] e a palavra falada (PW)."""
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
ARQUIVO_FINAL = "estudativo_MAT-MED-007_somar_e_subtrair_horas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("somar", "subtrair", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

m_ = lambda h, m: 60 * h + m
assert m_(3, 50) + m_(2, 25) == m_(6, 15) == 375 and m_(3, 50) == 230 and m_(2, 25) == 145 and divmod(375, 60) == (6, 15)
assert (m_(22, 30) + m_(3, 0)) - 24 * 60 == m_(1, 30) and m_(5, 10) - m_(2, 40) == m_(2, 30) and m_(4, 70) == m_(5, 10)
assert (m_(4, 110) - m_(2, 40)) == m_(2, 70) == m_(3, 10) and m_(3, 10) - m_(2, 30) == 40
assert m_(18, 25) - m_(13, 50) == m_(4, 35) == m_(17, 85) - m_(13, 50) and 10 + 25 == 35

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


def cabeca(c, t, t0, xh, xm, y, escuro=False):
    """cabeçalho das duas colunas: horas e minutos"""
    tinta = CLARO if escuro else TINTA2
    E.foco(c, t, t0, 0.45, lambda a: (centro(c, "horas", xh - SZ * 0.45, y, 46, "i", tinta, a), centro(c, "minutos", xm - SZ * 0.45, y, 46, "i", tinta, a),
                                       M.line(c, xh - SZ * 1.2, y + 24, xm + 100, y + 24, FIO if not escuro else CLARO, a * (1 if not escuro else 0.4), 3)))


def traco(c, t, t0, x0, x1, y, escuro=False):
    p = ep(t, t0, 0.5)
    if p > 0:
        M.line(c, x0, y, lerp(x0, x1, p), y, BR if escuro else TINTA, 1.0, 6)


def risca_troca(c, t, t0, xr, y, novo, size=SZ, cor=None, tn=None, s_len=2):
    """risca o número que termina em xr e escreve o novo em cima (a troca da hora)"""
    w = E.larg("0" * s_len, "g", size)
    E.risco(c, xr - w - 6, y + 8, xr + 6, y - size * 0.75, t, t0, cor or ERRADO, 9)
    s = str(novo)
    E.foco(c, t, tn if tn is not None else t0 + 0.3, 0.4, lambda a: E.escreve(c, s, xr - E.larg(s, "g", size * 0.6), y - size * 0.95, size * 0.6, "g", cor or CERTO, a), sobe=8)


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


def hhmm(v):
    h, m = divmod(v, 60)
    return f"{h % 24}:{m:02d}"


def linha(c, t, t0, x0, x1, y, marcas, xs, tm, escuro=False, size=46):
    """linha do tempo de x0 a x1; marcas = horários (em minutos) com traço e "hh:mm", cada um no x de xs (a linha não é em escala:
    os trechos curtos ganham espaço para o rótulo); tm = instante de cada marca. Devolve valor -> x"""
    tinta = BR if escuro else TINTA
    pos = dict(zip(marcas, xs))
    vx = lambda v: pos[v]
    if t >= t0:
        M.arrow(c, x0 - 40, y, x1 + 60, y, tinta, ep(t, t0, 0.6), 5, 18, ep(t, t0, 0.6))
    for v, ti in zip(marcas, tm):
        E.foco(c, t, ti, 0.4, lambda a, v=v: (M.line(c, vx(v), y - 20, vx(v), y + 20, tinta, a, 5),
                                              centro(c, hhmm(v), vx(v), y + 80, size, "b", tinta, a)), sobe=6)
    return vx


def ovos(c, t, t0, x, y, junta, a=1.0):
    """doze ovos em 2 fileiras de 6; com junta = 1 eles entram numa caixa de uma dúzia"""
    if a <= 0:
        return
    q = ease_io(junta)
    if q > 0:
        M.rrect(c, x - 30, y - 70, 6 * 90 + 40, 2 * 110 + 40, 26, E.mix(E.COR, "#FFFFFF", 0.8), q * a, stroke=4, stroke_color=E.COR)
    for k in range(12):
        i, j = k % 6, k // 6
        ti = t0 + 0.06 * k
        e = ep(t, ti, 0.3) * a
        if e <= 0:
            continue
        ox, oy = x + i * 90 + 25, y + j * 110 + 20
        sx = lerp(ox + (i - 2.5) * 40, ox, q)
        c.drawOval(skia.Rect.MakeXYWH(sx - 32, oy - 42, 64, 84), M.paint("#F4EAD8", e))
        c.drawOval(skia.Rect.MakeXYWH(sx - 32, oy - 42, 64, 84), M.paint(TINTA2, e, stroke=3))


# ---------------- gancho ----------------
XH, XM = 820, 1180


def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        y0 = 300
        hm(c, t, ka, 3, 50, XH, XM, y0)
        E.foco(c, t, kb, 0.4, lambda a: E.escreve(c, "+", XH - 330, y0 + DY, SZ, "g", TINTA, a))
        hm(c, t, kb, 2, 25, XH, XM, y0 + DY)
        traco(c, t, kc - 0.3, XH - 360, XM + 140, y0 + DY + 50)
        hm(c, t, kc, 5, 75, XH, XM, y0 + 2 * DY + 30, cor=ERRADO)
        tr = PW("s01", "relógio")
        E.foco(c, t, tr, 0.5, lambda a: (M.rrect(c, 1480, 640, 330, 160, 24, TINTA, a), centro(c, "5:75", 1645, 760, 110, "g", ERRADO, a)))
        E.foco(c, t, tr + 0.5, 0.4, lambda a: E.selo(c, 1810, 640, 44, False, a))
        E.frase(c, t, tr, ps("relógio nenhum mostra", "i", 62) + [("75 min", "g", 66, ERRADO)], W / 2, 960, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 300, passo=0.12)
        E.frase(c, t, PW("s02", "soma"), [("somar", "g", 100, COR)] + ps("e", "i", 90) + [("subtrair", "g", 100, COR)], XE, 470, passo=0.12)
        E.frase(c, t, PW("s02", "horas"), ps("horas sem tropeçar", "i", 84), XE, 610, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 190, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, 200, w, 196, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("uma hora tem", "i", 62)], x + 44, 284)
    E.frase(c, t, C["s03.b"] + 0.3, [("60 minutos", "g", 62, COR)], x + 44, 360)
    E.foco(c, t, C["s03.c"], 0.5, lambda a: E.escreve(c, "2 h 15 min", x + 40, 560, 80, "g", TINTA, a))
    E.foco(c, t, PW("s03", "cento"), 0.5, lambda a: E.escreve(c, "= 135 min", x + 40, 680, 80, "g", COR, a))
    E.frase(c, t, PW("s03", "Se"), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1000, "left", 0.12)


# ---------------- somar ----------------
def b_somar(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    if t < C["s05"] + 0.4:
        def porque():
            E.frase(c, t, PW("s04", "Por"), ps("por que a soma direta", "i", 70) + [("não fecha?", "g", 74, ERRADO)], W / 2, 190, "center", 0.1)
            E.frase(c, t, a4, ps("minuto", "i", 70) + [("não vai até 100", "g", 74, COR)], W / 2, 320, "center", 0.1)
            from_ = b4
            for k in range(6):  # 60 minutos em seis blocos de 10 que viram uma hora
                E.foco(c, t, from_ + 0.08 * k, 0.3, lambda a, k=k: M.rrect(c, 300 + k * 110 * (1 - 0.0 * ep(t, c4, 0.6)), 430, 100, 120, 14, E.COR, a * (1 - ep(t, c4, 0.5))))
            E.foco(c, t, b4 + 0.2, 0.4, lambda a: centro(c, "60 min", 625, 620, 60, "g", COR, a * (1 - ep(t, c4, 0.5))))
            E.foco(c, t, c4, 0.5, lambda a: (E.bola(c, 625, 490, 110, a=a), centro(c, "1 h", 625, 525, 90, "g", E.SOBRE, a)))
            tv = PW("s04", "ovos")
            ovos(c, t, tv - 0.3, 1140, 460, ep(t, PW("s04", "dúzia") - 0.2, 0.7))
            E.foco(c, t, PW("s04", "dúzia"), 0.4, lambda a: centro(c, "1 dúzia", 1390, 790, 70, "g", COR, a))
            E.foco(c, t, tv - 0.2, 0.4, lambda a: centro(c, "12 ovos", 1390, 400, 56, "i", TINTA2, a * (1 - ep(t, PW("s04", "dúzia"), 0.4))))
        E.saida(c, t, C["s05"] - 0.1, porque)
    if t < C["s05"]:
        return
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    xh, xm, y0 = 430, 780, 420

    def conta():
        E.frase(c, t, a5 - 0.6, ps("o método tem", "i", 62) + [("2 passos", "g", 66, COR)], 120, 160, "left", 0.1)
        cabeca(c, t, b5, xh, xm, y0 - 170)
        hm(c, t, b5 + 0.2, 3, 50, xh, xm, y0)
        E.foco(c, t, b5 + 0.4, 0.4, lambda a: E.escreve(c, "+", xh - 300, y0 + DY, SZ, "g", TINTA, a))
        hm(c, t, b5 + 0.4, 2, 25, xh, xm, y0 + DY)
        traco(c, t, c5 - 0.4, xh - 330, xm + 140, y0 + DY + 50)
        cel(c, t, c5, "5", xh, y0 + 2 * DY + 30, SZ, COR)
        E.foco(c, t, c5, 0.45, lambda a: E.escreve(c, "h", xh + 12, y0 + 2 * DY + 30, SZ * 0.55, "g", COR, a))
        mint = d5 if t < c6 else 1e9
        cel(c, t, d5, "75", xm, y0 + 2 * DY + 30, SZ, ERRADO if t >= a6 else COR)
        E.foco(c, t, d5, 0.45, lambda a: E.escreve(c, "min", xm + 12, y0 + 2 * DY + 30, SZ * 0.55, "g", ERRADO if t >= a6 else COR, a))
        E.foco(c, t, b5, 0.4, lambda a: E.pilula(c, "1. horas com horas, minutos com minutos", 1450, 300, 42, "g", a=a, cor=E.SOBRE))
        E.foco(c, t, a6, 0.4, lambda a: E.pilula(c, "2. passou de 60? troque 60 min por 1 h", 1450, 400, 42, "g", fundo=TINTA, a=a, cor=BR))
        fcen(c, t, b6, "75 = 60 + 15", 1450, 580, 90)
        seta_troca(c, t, c6, xm - 60, xh - 40, y0 + 2 * DY + 70, "60 min = 1 h", alto=-110)
        bola_res(c, t, d6, "6 h 15 min", 1450, 820, 160, 60)
    E.saida(c, t, C["s07"] - 0.1, conta)
    if t < C["s07"]:
        return
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    E.frase(c, t, C["s07"] + 0.3, ps("conferindo:", "i", 70, COR) + ps("tudo em minutos", "i", 70), W / 2, 200, "center", 0.1)
    fcen(c, t, a7, "230 + 145", 620, 420, 100)
    E.frase(c, t, a7, ps("(3 h 50 min)", "i", 46, TINTA2) + ps("(2 h 25 min)", "i", 46, TINTA2), 620, 500, "center", 0.1)
    fcen(c, t, b7, "= 375 min", 1240, 420, 100, COR)
    fcen(c, t, PW("s07", "Dividido"), "375 ÷ 60 = 6, resto 15", W / 2, 660, 90)
    bola_res(c, t, d7, "6 h 15 min", W / 2, 860, 150, 60)


def b_meianoite(c, t, C, b):
    a8, b8, c8, d8, e8, f8 = (C[f"s08.{k}"] for k in "abcdef")
    E.frase(c, t, C["s08"] + 0.3, ps("e se passar de", "i", 70) + [("24 h?", "g", 76, COR)], W / 2, 180, "center", 0.1)
    E.frase(c, t, b8 - 0.6, ps("um plantão começa às", "i", 60), 200, 330, "left", 0.1)
    E.foco(c, t, b8, 0.4, lambda a: E.escreve(c, "22 h 30 min", 840, 330, 80, "g", TINTA, a))
    E.frase(c, t, c8 - 0.4, ps("e dura", "i", 60), 200, 440, "left", 0.1)
    E.foco(c, t, c8, 0.4, lambda a: E.escreve(c, "3 h", 420, 440, 80, "g", TINTA, a))
    fcen(c, t, d8, "22 h 30 + 3 h = 25 h 30", W / 2, 580, 80, ERRADO if t >= e8 else TINTA)
    E.frase(c, t, PW("s08", "dia"), ps("o dia tem", "i", 56, TINTA2) + [("24 h", "g", 60, TINTA2)], W / 2, 670, "center", 0.1)
    vx = linha(c, t, b8, 260, 1660, 900, [22 * 60 + 30, 24 * 60, 25 * 60 + 30], [420, 950, 1500], [b8, PW("s08", "dia") - 0.2, d8 + 0.6])
    E.foco(c, t, PW("s08", "dia"), 0.4, lambda a: centro(c, "meia-noite", vx(24 * 60), 1040, 44, "i", COR, a))
    E.salto(c, t, c8 + 0.2, vx(22 * 60 + 30), vx(25 * 60 + 30), 880, 100, E.COR, "+ 3 h", size=46)
    E.foco(c, t, e8, 0.4, lambda a: E.pilula(c, "− 24 h", 1560, 330, 56, "g", fundo=TINTA, a=a, cor=BR))
    E.foco(c, t, f8, 0.4, lambda a: E.pilula(c, "1 h 30 min do dia seguinte", 1460, 440, 54, "g", fundo=CERTO, a=a, cor=BR))


# ---------------- subtrair ----------------
def b_subtrair(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]

    def pergunta():
        E.frase(c, t, C["s09"] + 0.3, ps("na subtração,", "i", 70) + [("a troca é ao contrário", "g", 74, COR)], W / 2, 190, "center", 0.1)
        E.frase(c, t, a9 - 0.8, ps("entrou às", "i", 62), 300, 380, "left", 0.1)
        E.foco(c, t, a9, 0.4, lambda a: E.escreve(c, "2 h 40 min", 640, 380, 90, "g", TINTA, a))
        E.frase(c, t, PW("s09", "tarde"), ps("da tarde", "i", 54, TINTA2), 1180, 380, "left", 0.1)
        E.frase(c, t, b9 - 0.4, ps("saiu às", "i", 62), 300, 510, "left", 0.1)
        E.foco(c, t, b9, 0.4, lambda a: E.escreve(c, "5 h 10 min", 640, 510, 90, "g", TINTA, a))
        vx = linha(c, t, a9, 300, 1600, 760, [14 * 60 + 40, 17 * 60 + 10], [360, 1540], [a9, b9])
        E.salto(c, t, c9, vx(14 * 60 + 40), vx(17 * 60 + 10), 740, 110, E.COR, "?")
    E.saida(c, t, C["s10"] - 0.1, pergunta)
    if t < C["s10"]:
        return
    xh, xm, y0 = 560, 920, 400
    cabeca(c, t, C["s10"], xh, xm, y0 - 230)
    troca = t >= b0
    hm(c, t, a0, 5, 10, xh, xm, y0, cor_h=TINTA2 if troca else None, cor_m=TINTA2 if troca else None)
    E.foco(c, t, PW("s10", "menos"), 0.4, lambda a: E.escreve(c, "−", xh - 300, y0 + DY, SZ, "g", TINTA, a))
    hm(c, t, PW("s10", "menos"), 2, 40, xh, xm, y0 + DY)
    traco(c, t, PW("s10", "Dez") - 0.2, xh - 330, xm + 140, y0 + DY + 50)
    E.foco(c, t, PW("s10", "Dez"), 0.4, lambda a: E.pilula(c, "10 − 40 não dá", 1420, 330, 54, "g", fundo=ERRADO, a=a, cor=BR))
    if troca:
        risca_troca(c, t, b0 + 0.6, xh, y0, 4, tn=c0, s_len=1)
        risca_troca(c, t, b0 + 0.6, xm, y0, 70, tn=c0 + 0.6)
    E.foco(c, t, b0, 0.4, lambda a: E.pilula(c, "desmanche 1 h = 60 min", 1420, 440, 54, "g", a=a, cor=E.SOBRE))
    fcen(c, t, c0 + 0.8, "10 + 60 = 70", 1420, 580, 80, TINTA2)
    yr = y0 + 2 * DY + 30
    cel(c, t, b1, "2", xh, yr, SZ, COR)
    E.foco(c, t, b1, 0.45, lambda a: E.escreve(c, "h", xh + 12, yr, SZ * 0.55, "g", COR, a))
    cel(c, t, a1, "30", xm, yr, SZ, COR)
    E.foco(c, t, a1, 0.45, lambda a: E.escreve(c, "min", xm + 12, yr, SZ * 0.55, "g", COR, a))
    fcen(c, t, a1, "70 − 40 = 30", 1420, 700, 76)
    fcen(c, t, b1, "4 − 2 = 2", 1420, 800, 76)
    bola_res(c, t, c1, "2 h 30 min", 1420, 940, 125, 44)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    a3, b3 = C["s13.a"], C["s13.b"]
    xh, xm, y0 = 560, 920, 400
    E.frase(c, t, C["s12"] + 0.3, ps("o erro:", "i", 70) + [("conta como número com vírgula", "g", 70, ERRADO)], W / 2, 180, "center", 0.1)
    hm(c, t, a2, 5, 10, xh, xm, y0, cor_h=TINTA2 if t >= b2 else None, cor_m=TINTA2 if t >= b2 else None)
    E.foco(c, t, a2 + 0.2, 0.4, lambda a: E.escreve(c, "−", xh - 300, y0 + DY, SZ, "g", TINTA, a))
    hm(c, t, a2 + 0.2, 2, 40, xh, xm, y0 + DY)
    traco(c, t, a2 + 0.5, xh - 330, xm + 140, y0 + DY + 50)
    if t >= b2:
        risca_troca(c, t, b2, xh, y0, 4, cor=ERRADO, tn=b2 + 0.4, s_len=1)
        risca_troca(c, t, b2, xm, y0, 110, cor=ERRADO, tn=c2)
    E.foco(c, t, b2, 0.4, lambda a: E.pilula(c, "empresta 100?", 1400, 330, 56, "g", fundo=ERRADO, a=a, cor=BR))
    yr = y0 + 2 * DY + 30
    E.foco(c, t, d2, 0.45, lambda a: (E.escreve(c, "2", xh - E.larg("2", "g", SZ), yr, SZ, "g", ERRADO, a), E.escreve(c, "h", xh + 12, yr, SZ * 0.55, "g", ERRADO, a),
                                       E.escreve(c, "70", xm - E.larg("70", "g", SZ), yr, SZ, "g", ERRADO, a), E.escreve(c, "min", xm + 12, yr, SZ * 0.55, "g", ERRADO, a)))
    E.frase(c, t, PW("s13", "Isso"), ps("isso daria", "i", 56) + [("3 h 10 min", "g", 62, ERRADO)], 1400, 480, "center", 0.1)
    E.frase(c, t, a3, [("40 min a mais", "g", 66, ERRADO)] + ps("que o certo", "i", 60), 1400, 590, "center", 0.1)
    E.foco(c, t, a3 + 0.8, 0.4, lambda a: E.escreve(c, "(2 h 30 min)", 1240, 670, 50, "i", CERTO, a))
    E.foco(c, t, b3, 0.5, lambda a: E.pilula(c, "1 h empresta 60, nunca 100", W / 2, 960, 66, "g", fundo=CERTO, a=a, cor=BR))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")

    def soma():
        E.frase(c, t, C["s14"] + 0.3, ps("agora, o atalho:", "i", 70, CLARO), W / 2, 160, "center", 0.1)
        E.frase(c, t, a4, ps("complete a", "i", 92, CLARO) + [("hora cheia", "g", 96, BR)], W / 2, 290, "center", 0.12)
        E.foco(c, t, PW("s14", "soma,"), 0.4, lambda a: E.escreve(c, "3 h 50 + 2 h 25", 200, 460, 80, "g", BR, a))
        E.foco(c, t, b4, 0.4, lambda a: E.escreve(c, "3 h 50 + 10 min = 4 h", 200, 600, 80, "g", CLARO, a))
        E.foco(c, t, PW("s14", "Tire"), 0.4, lambda a: E.escreve(c, "2 h 25 − 10 min = 2 h 15", 200, 720, 80, "g", CLARO, a))
        fcen(c, t, d4, "4 h + 2 h 15 = 6 h 15", W / 2, 900, 96, BR)
    E.saida(c, t, C["s15"] - 0.1, soma)
    if C["s15"] <= t < C["s16"] + 0.4:
        a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")

        def frente():
            E.frase(c, t, a5, ps("na subtração,", "i", 70, CLARO) + [("conte para a frente", "g", 76, BR)], W / 2, 200, "center", 0.1)
            E.frase(c, t, PW("s15", "como"), ps("como o troco no caixa", "i", 56, CLARO), W / 2, 290, "center", 0.08)
            v0 = 14 * 60 + 40
            vx = linha(c, t, PW("s15", "De"), 260, 1660, 700, [v0, 15 * 60, 17 * 60, 17 * 60 + 10], [320, 640, 1280, 1600],
                       [PW("s15", "De"), PW("s15", "três"), PW("s15", "cinco"), PW("s15", "dez")], escuro=True)
            E.salto(c, t, b5, vx(v0), vx(15 * 60), 680, 90, CLARO, "20 min", size=46)
            E.salto(c, t, c5, vx(15 * 60), vx(17 * 60), 680, 150, CLARO, "2 h", size=56)
            E.salto(c, t, d5, vx(17 * 60), vx(17 * 60 + 10), 680, 90, CLARO, "10 min", size=46)
            E.foco(c, t, e5, 0.5, lambda a: E.pilula(c, "20 min + 2 h + 10 min = 2 h 30 min", W / 2, 930, 60, "g", a=a, cor=E.SOBRE))
        E.saida(c, t, C["s16"] - 0.1, frente)
    if t >= C["s16"]:
        a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
        E.frase(c, t, a6, ps("na hora cheia,", "i", 80, CLARO) + [("não há troca", "g", 84, BR)], W / 2, 320, "center", 0.12)
        E.foco(c, t, b6, 0.5, lambda a: E.selo(c, 400, 560, 50, False, a))
        E.frase(c, t, b6 + 0.1, ps("não compensa com", "i", 72, CLARO) + [("muitas parcelas", "g", 78, BR)], 480, 585, "left", 0.1)
        E.frase(c, t, c6, ps("some tudo e", "i", 76, CLARO) + [("troque os 60 no final", "g", 80, BR)], W / 2, 820, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]
    E.frase(c, t, C["s17"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a7 - 0.6, ps("o ônibus saiu às", "i", 70), XE, 380, passo=0.1)
    E.foco(c, t, a7, 0.5, lambda a: E.escreve(c, "13 h 50 min", XE, 510, 110, "g", COR, a))
    E.frase(c, t, b7 - 0.4, ps("e chegou às", "i", 70), XE, 640, passo=0.1)
    E.foco(c, t, b7, 0.5, lambda a: E.escreve(c, "18 h 25 min", XE, 770, 110, "g", COR, a))
    E.frase(c, t, c7, ps("quanto tempo", "i", 80) + [("durou?", "g", 86, COR)], XE, 920, passo=0.12)
    E.relogio(c, t, C["s18.a"], 1560, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    xh, xm, y0 = 600, 960, 400

    def conta():
        E.frase(c, t, C["s19"] + 0.3, ps("pela conta", "i", 64, COR), 1440, 200, "center", 0.1)
        cabeca(c, t, C["s19"] + 0.3, xh, xm, y0 - 230)
        troca = t >= a9
        hm(c, t, C["s19"] + 0.4, 18, 25, xh, xm, y0, cor_h=TINTA2 if troca else None, cor_m=TINTA2 if troca else None)
        E.foco(c, t, C["s19"] + 0.6, 0.4, lambda a: E.escreve(c, "−", xh - 330, y0 + DY, SZ, "g", TINTA, a))
        hm(c, t, C["s19"] + 0.6, 13, 50, xh, xm, y0 + DY)
        traco(c, t, C["s19"] + 0.9, xh - 360, xm + 140, y0 + DY + 50)
        E.foco(c, t, PW("s19", "Vinte"), 0.4, lambda a: E.pilula(c, "25 − 50 não dá", 1440, 330, 54, "g", fundo=ERRADO, a=a, cor=BR))
        if troca:
            risca_troca(c, t, a9 + 0.3, xh, y0, 17, tn=PW("s19", "dezessete"))
            risca_troca(c, t, a9 + 0.3, xm, y0, 85, tn=PW("s19", "oitenta"))
        yr = y0 + 2 * DY + 30
        cel(c, t, c9 + 0.6, "4", xh, yr, SZ, COR)
        E.foco(c, t, c9 + 0.6, 0.45, lambda a: E.escreve(c, "h", xh + 12, yr, SZ * 0.55, "g", COR, a))
        cel(c, t, b9 + 1.0, "35", xm, yr, SZ, COR)
        E.foco(c, t, b9 + 1.0, 0.45, lambda a: E.escreve(c, "min", xm + 12, yr, SZ * 0.55, "g", COR, a))
        fcen(c, t, b9, "85 − 50 = 35", 1440, 520, 76)
        fcen(c, t, c9, "17 − 13 = 4", 1440, 640, 76)
        bola_res(c, t, d9, "4 h 35 min", 1440, 850, 150, 56)
    E.saida(c, t, C["s20"] - 0.1, conta)
    if t < C["s20"]:
        return
    a0, b0, c0, d0 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    E.frase(c, t, C["s20"] + 0.2, ps("pelo atalho", "i", 70, COR), W / 2, 200, "center", 0.1)
    v0 = 13 * 60 + 50
    vx = linha(c, t, C["s20"] + 0.3, 260, 1660, 620, [v0, 14 * 60, 18 * 60, 18 * 60 + 25], [320, 640, 1280, 1600], [C["s20"] + 0.3, a0, b0, c0])
    E.salto(c, t, a0, vx(v0), vx(14 * 60), 600, 80, E.COR, "10 min", size=44)
    E.salto(c, t, b0, vx(14 * 60), vx(18 * 60), 600, 150, E.COR, "4 h", size=56)
    E.salto(c, t, c0, vx(18 * 60), vx(18 * 60 + 25), 600, 80, E.COR, "25 min", size=44)
    fcen(c, t, PW("s20", "Dez"), "10 + 25 = 35 min", 700, 880, 80)
    bola_res(c, t, d0, "4 h 35 min", 1420, 870, 140, 52, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s21.a", "horas com horas,", "minutos com minutos"), ("s21.b", "a troca é sempre", "de 60"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 80) + [(l2, "g", 84, COR)], 320, y, "left", 0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a2, b2 = C["s22.a"], C["s22.b"]
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 80), XE, 240, passo=0.12)
    E.frase(c, t, a2, ps("pratique", "i", 90) + [("todas as medidas", "g", 100, COR)], XE, 400, passo=0.12)
    E.frase(c, t, b2, ps("comprimento, massa, área, volume e tempo", "i", 62), XE, 520, passo=0.08)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, somar=b_somar, meianoite=b_meianoite, subtrair=b_subtrair, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
