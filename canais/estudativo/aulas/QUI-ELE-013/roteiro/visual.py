"""Visual — Estudativo · QUI-ELE-013: fissão e fusão nuclear.
Linguagem visual: a da Química (QUI-MIS-001), a da trilha (QUI-ELE-001) e a da Radioatividade (cabeçalho da QUI-ELE-011): núcleo
em cacho (prótons laranja, nêutrons cinza), nuclídeo com nuc(), equação nuclear com eq_nuc(). Fissão = núcleo grande que treme
e se parte em dois com nêutrons e um clarão (fissao_anim); fusão = dois leves que se juntam (fusao_anim); usina em blocos
reator → água → turbina → gerador (usina()). Fissão em turquesa, fusão em âmbar. Peças locais candidatas ao kit.
Todo instante vem de C[...]."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-013_fissao_e_fusao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("fissao", "usina", "fusao", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PROTON, GAMA, BETA = "#E07B39", "#8E44AD", Q.ELETRON

def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """palavras de uma frase; sinais (=, −, +, ×, →) vão na grotesca, porque a serifada itálica não tem esses glifos"""
    return [((w, "g", size * 0.9, cor) if w in ("=", "−", "+", "×", "→", "≠") else (w, "b", size * 0.9, cor) if ("-" in w and est == "i") else (w, est, size, cor)) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=66, r=40):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + r, y - size * 0.38, r, a=a), centro(c, str(i + 1), x + r, y - size * 0.38 + r * 0.42, r * 1.2, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + r * 2 + 40, y, passo=0.1)


def nuc(c, A, Z, s, x, y, size, cor=None, a=1.0, cor_a=None, cor_z=None):
    """nuclídeo: massa em cima e número atômico embaixo, à esquerda do símbolo. Devolve a largura."""
    cor = cor or TINTA
    sn = size * 0.5
    ta, tz = str(A), str(Z)
    wn = max(E.larg(ta, "g", sn), E.larg(tz, "g", sn))
    if c is not None and a > 0:
        E.escreve(c, ta, x + wn - E.larg(ta, "g", sn), y - size * 0.46, sn, "g", cor_a or TINTA, a)
        E.escreve(c, tz, x + wn - E.larg(tz, "g", sn), y + size * 0.2, sn, "g", cor_z or COR, a)
        E.escreve(c, s, x + wn + size * 0.06, y, size, "g", cor, a)
    return wn + size * 0.06 + E.larg(s, "g", size)


def eq_nuc(c, t, tl, itens, x, y, size, align="center"):
    """itens = [(A, Z, símbolo, cor) | "+" | "->"]; tl = instante de cada item. Devolve o centro x de cada item."""
    gap = size * 0.35
    ws = []
    for it in itens:
        if it == "+":
            ws.append(E.larg("+", "g", size * 0.8))
        elif it == "->":
            ws.append(size * 1.4)
        elif isinstance(it, str):
            ws.append(E.larg(it, "g", size))
        else:
            ws.append(nuc(None, it[0], it[1], it[2], 0, 0, size))
    tot = sum(ws) + gap * (len(ws) - 1)
    xx = x - tot / 2 if align == "center" else x
    cs = []
    for k, (it, w) in enumerate(zip(itens, ws)):
        tk = tl[k] if tl else -10
        q = ep(t, tk, 0.4)
        if q > 0:
            if it == "+":
                E.escreve(c, "+", xx, y - size * 0.05, size * 0.8, "g", TINTA2, q)
            elif isinstance(it, str) and it != "->":
                E.foco(c, t, tk, 0.4, lambda aa, it=it, xx=xx: E.escreve(c, it, xx, y, size, "g", E.COR, aa))
            elif it == "->":
                M.arrow(c, xx, y - size * 0.32, xx + w * ease_io(prog(t, tk, 0.5)), y - size * 0.32, E.COR, q, 6, 22, ease_io(prog(t, tk, 0.5)))
            else:
                E.foco(c, t, tk, 0.4, lambda aa, it=it, xx=xx: nuc(c, it[0], it[1], it[2], xx, y, size, it[3] if len(it) > 3 else None, aa))
        cs.append(xx + w / 2)
        xx += w + gap
    return cs


def nucleo(c, cx, cy, Zv, Nv, r=14, a=1.0, semente=2, treme=0.0, t=0.0):
    """cacho de prótons (laranja) e nêutrons (cinza); Zv e Nv = quantas bolinhas de cada"""
    if a <= 0:
        return
    rnd = random.Random(semente)
    n = Zv + Nv
    tipos = [PROTON] * Zv + [Q.NEUTRON] * Nv
    rnd.shuffle(tipos)
    pts = []
    for k in range(n):
        ang = k * 2.399963
        rr = r * 1.05 * math.sqrt(k + 0.5)
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    dx = treme * math.sin(t * 40) * 2
    for (x, y), cor in sorted(zip(pts, tipos), key=lambda p: -math.dist(p[0], (cx, cy))):
        E.bola(c, x + dx, y, r, cor, a)


def alfa(c, x, y, r=16, a=1.0, rotulo=True):
    for k, (ox, oy, cor) in enumerate(((-1, -1, PROTON), (1, -1, Q.NEUTRON), (-1, 1, Q.NEUTRON), (1, 1, PROTON))):
        E.bola(c, x + ox * r * 0.75, y + oy * r * 0.75, r, cor, a)
    if rotulo:
        E.escreve(c, "α", x + r * 2, y - r * 1.2, r * 2.4, "g", PROTON, a)


def beta(c, x, y, r=16, a=1.0, rotulo=True):
    E.bola(c, x, y, r, BETA, a)
    M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, a, max(2.5, r * 0.16))
    if rotulo:
        E.escreve(c, "β", x + r * 1.4, y - r * 1.2, r * 2.4, "g", BETA, a)


def gama_onda(c, x0, x1, y, amp=20, lam=60, a=1.0, cor=None, rotulo=True):
    if a <= 0 or x1 <= x0:
        return
    p = skia.Path()
    p.moveTo(x0, y)
    x = x0
    while x < x1:
        x += 4
        p.lineTo(x, y + amp * math.sin((x - x0) / lam * 2 * math.pi))
    c.drawPath(p, M.paint(cor or GAMA, a, stroke=6))
    if rotulo:
        E.escreve(c, "γ", x0, y - amp - 20, 60, "g", cor or GAMA, a)


def barreiras(c, t, t0, x, y, h, a=1.0):
    nomes = (("papel", "#EFEAD8", 18), ("alumínio", "#B9C0CC", 40), ("chumbo", "#3A3D45", 110))
    xs = []
    for k, (nome, cor, w) in enumerate(nomes):
        xx = x + k * 360
        q = ep(t, t0 + 0.3 * k, 0.4) * a
        if q > 0:
            M.rrect(c, xx, y - h / 2, w, h, 6, cor, q)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx, y - h / 2, w, h), 6, 6), M.paint(TINTA2, 0.5 * q, stroke=2))
            centro(c, nome, xx + w / 2, y + h / 2 + 60, 44, "g", TINTA, q)
        xs.append((xx, w))
    return xs



NEU = Q.NEUTRON
OXI = "#E08A00"
assert 235 + 1 == 141 + 92 + 3 and 92 == 56 + 36
assert 2 + 3 == 4 + 1 and 1 + 1 == 2 + 0
assert 235 + 1 - (140 + 94) == 2 and 92 == 54 + 38

EQ_F = [(235, 92, "U"), "+", (1, 0, "n", NEU), "->", (141, 56, "Ba"), "+", (92, 36, "Kr"), "+", "3", (1, 0, "n", NEU)]
EQ_U = [(2, 1, "H"), "+", (3, 1, "H"), "->", (4, 2, "He"), "+", (1, 0, "n", NEU)]


def neutron(c, x, y, r=16, a=1.0):
    E.bola(c, x, y, r, NEU, a)


def fissao_anim(c, t, t0, cx, cy, escala=1.0, nn=3, ciclo=None):
    """um nêutron chega, o núcleo grande treme e se parte em dois médios, soltando nn nêutrons"""
    if t < t0:
        return
    u = t - t0
    if ciclo:
        u = u % ciclo
    r = 13 * escala
    if u < 1.0:
        f = ease_io(u / 1.0)
        neutron(c, lerp(cx - 420 * escala, cx - 120 * escala, f), cy, r)
        nucleo(c, cx, cy, 28, 36, r, 1, 11)
    elif u < 1.5:
        nucleo(c, cx, cy, 28, 36, r, 1, 11, 1, t)
    else:
        f = ease_out(min(1, (u - 1.5) / 1.2))
        nucleo(c, cx - 40 * escala - 170 * escala * f, cy - 120 * escala * f, 14, 18, r, 1, 12)
        nucleo(c, cx + 40 * escala + 170 * escala * f, cy + 120 * escala * f, 12, 16, r, 1, 13)
        for k in range(nn):
            ang = -0.6 + k * 0.6
            neutron(c, cx + 380 * escala * f * math.cos(ang), cy + 380 * escala * f * math.sin(ang) * 0.6, r)
        if f < 1:
            g = skia.Paint(AntiAlias=True)
            g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), 260 * escala, [M.hexc("#FFD54A", 0.7 * (1 - f)), M.hexc("#FFD54A", 0)], [0, 1]))
            c.drawCircle(cx, cy, 260 * escala, g)


def fusao_anim(c, t, t0, cx, cy, escala=1.0, ciclo=None):
    if t < t0:
        return
    u = t - t0
    if ciclo:
        u = u % ciclo
    r = 22 * escala
    if u < 1.2:
        f = ease_io(u / 1.2)
        nucleo(c, lerp(cx - 400 * escala, cx - 40 * escala, f), cy, 1, 1, r, 1, 21)
        nucleo(c, lerp(cx + 400 * escala, cx + 40 * escala, f), cy, 1, 2, r, 1, 22)
    else:
        f = ease_out(min(1, (u - 1.2) / 1.0))
        nucleo(c, cx, cy, 2, 2, r, 1, 23)
        neutron(c, cx + 60 * escala + 400 * escala * f, cy - 200 * escala * f, r)
        if f < 1:
            g = skia.Paint(AntiAlias=True)
            g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), 240 * escala, [M.hexc("#FFD54A", 0.8 * (1 - f)), M.hexc("#FFD54A", 0)], [0, 1]))
            c.drawCircle(cx, cy, 240 * escala, g)


def usina(c, t, t0, x, y, a=1.0, tq=None, tv=None, tt=None):
    """reator → água fervendo → turbina → gerador, em blocos"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    M.rrect(c, x, y, 300, 380, 40, "#3D4350", q)
    centro(c, "reator", x + 150, y + 430, 42, "g", TINTA, q)
    for k in range(4):
        M.rrect(c, x + 50 + 60 * k, y + 40, 24, 240, 6, "#8A8D96" if k % 2 else "#E07B39", q)
    if tq is not None:
        M.rrect(c, x + 400, y + 120, 260, 260, 30, "#9CCBE8", q * ep(t, tq, 0.4))
        centro(c, "água ferve", x + 530, y + 430, 42, "g", TINTA, q * ep(t, tq, 0.4))
        for k in range(5):
            f = ((t - tq) * 0.6 + k / 5) % 1
            c.drawCircle(x + 460 + 35 * k, y + 360 - 220 * f, 10, M.paint(BR, q * ep(t, tq, 0.4) * (1 - f)))
    if tv is not None:
        q2 = q * ep(t, tv, 0.4)
        cxx, cyy = x + 860, y + 240
        for k in range(6):
            ang = (t - tv) * 4 + k * math.pi / 3
            M.line(c, cxx, cyy, cxx + 90 * math.cos(ang), cyy + 90 * math.sin(ang), "#5B6470", q2, 14)
        centro(c, "turbina", cxx, y + 430, 42, "g", TINTA, q2)
    if tt is not None:
        q3 = q * ep(t, tt, 0.4)
        M.rrect(c, x + 1020, y + 160, 200, 160, 20, E.COR, q3)
        centro(c, "gerador", x + 1120, y + 430, 42, "g", TINTA, q3)
        centro(c, "eletricidade", x + 1120, y + 250, 30, "g", BR, q3)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def s01():
            E.foco(c, t, C["s01.a"], 0.5, lambda a: (E.bola(c, 500, 480, 160, "#FFC24A", a), centro(c, "estrela", 500, 700, 50, "g", TINTA, a)))
            E.frase(c, t, C["s01.a"], ps("o carbono do seu corpo nasceu numa", "i", 56) + [("estrela", "g", 52, OXI)], XE, 200, passo=0.08)
            E.frase(c, t, C["s01.b"], ps("parte da luz do Rio vem de", "i", 56) + [("urânio se partindo", "g", 52, COR)], XE, 860, passo=0.08)
            fissao_anim(c, t, C["s01.b"] + 0.3, 1400, 520, 0.8, ciclo=4.0)
            E.foco(c, t, C["s01.c"], 0.4, lambda a: E.pilula(c, "núcleos que se juntam, núcleos que se partem", W / 2, 990, 46, "g", fundo=TINTA, a=a))
        E.saida(c, t, C["s02"] - 0.1, s01)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1580, 560, 230 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 230, passo=0.14)
    lista(c, t, [(C["s02.b"], [("fissão", "g", 62, COR), ("x", "i", 66), ("fusão", "g", 62, OXI)]),
                 (C["s02.c"], ps("a", "i", 66) + [("usina nuclear", "g", 62)] + ps("e o lixo dela", "i", 66)),
                 (C["s02.d"], ps("como as estrelas fazem", "i", 66) + [("elementos", "g", 62)]),
                 (C["s02.e"], [("atalho", "g", 62, COR), ("de", "i", 66), ("prova", "i", 66)])], XE, 390, 150, 62)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de uma coisa", "i", 76, TINTA2), XE, 200, passo=0.12)
    cs = eq_nuc(c, t, [C["s03"] + 0.5 + 0.2 * k for k in range(5)], [(238, 92, "U"), "->", (4, 2, "α", PROTON), "+", (234, 90, "Th")], W / 2, 520, 120)
    E.foco(c, t, C["s03.a"], 0.4, lambda a: E.formula(c, "em cima: 238 = 4 + 234", W / 2, 720, 64, "g", TINTA, a, "center"))
    E.foco(c, t, C["s03.b"], 0.4, lambda a: E.formula(c, "embaixo: 92 = 2 + 90", W / 2, 830, 64, "g", COR, a, "center"))
    E.foco(c, t, C["s03.c"], 0.4, lambda a: E.pilula(c, "as somas fecham dos dois lados", W / 2, 960, 50, "g", fundo=E.COR, a=a))


# ---------------- fissão ----------------
def b_fissao(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("fissão", "g", 80, COR)] + ps("= partir, como numa fissura", "i", 64), XE, 220, passo=0.12)
        fissao_anim(c, t, C["s04.b"], W / 2, 580, 1.0)
        E.foco(c, t, C["s04.b"] + 0.3, 0.4, lambda a: E.pilula(c, "nêutron, sem carga", W / 2 - 420, 480, 42, "g", fundo="#6E7280", a=a))
        E.foco(c, t, C["s04.b"] + 0.8, 0.4, lambda a: E.pilula(c, "urânio 235", W / 2, 360, 46, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s04.d"], 0.4, lambda a: E.pilula(c, "dois núcleos médios", W / 2 - 300, 900, 46, "g", fundo=PROTON, a=a))
        E.foco(c, t, C["s04.e"], 0.4, lambda a: E.pilula(c, "2 ou 3 nêutrons e muita energia", W / 2 + 330, 900, 46, "g", fundo=OXI, a=a))
        return
    if t < C["s06"]:
        cs = eq_nuc(c, t, [C["s05.b"], C["s05.b"] + 0.3, C["s05.b"] + 0.6, C["s05.c"] - 0.3, C["s05.c"], C["s05.c"] + 0.2, C["s05.c"] + 0.4, C["s05.c"] + 0.6, C["s05.c"] + 0.8, C["s05.c"] + 0.8], EQ_F, W / 2, 470, 100)
        E.foco(c, t, C["s05.b"] + 0.4, 0.4, lambda a: E.formula(c, "235 + 1 = 236", 480, 680, 70, "g", TINTA, a, "center"))
        E.foco(c, t, C["s05.d"], 0.4, lambda a: E.formula(c, "141 + 92 + 3", 1380, 680, 70, "g", TINTA, a, "center"))
        E.foco(c, t, C["s05.e"], 0.4, lambda a: (E.formula(c, "= 236", 1380, 790, 80, "g", COR, a, "center"), E.selo(c, 1620, 765, 40, True, a)))
        return
    E.frase(c, t, C["s06.a"], ps("de onde vem a", "i", 70) + [("energia?", "g", 66, OXI)], XE, 240, passo=0.12)
    E.frase(c, t, C["s06.b"], ps("os números de cima fecham, mas numa", "i", 58) + [("balança de precisão", "g", 54)], XE, 380, passo=0.08)
    E.foco(c, t, C["s06.b"] + 2.0, 0.4, lambda a: E.formula(c, "pedaços < começo", XE, 520, 90, "g", TINTA, a))
    E.frase(c, t, C["s06.c"], ps("a massa que some", "i", 64) + [("vira energia", "g", 60, OXI)], XE, 700, passo=0.1)
    pilula_em(c, t, C["s06.d"], "a conta disso: outra aula, na Física", 760, 850, 46, TINTA2)


# ---------------- reação em cadeia ----------------
def b_cadeia(c, t, C, b):
    E.frase(c, t, C["s07.a"], ps("os nêutrons novos batem em", "i", 60) + [("outros núcleos", "g", 56)], XE, 200, passo=0.08)
    niveis = [(C["s07.a"] + 0.4, [(400, 560)]), (C["s07.b"], [(800, 420), (800, 700)]), (C["s07.b"] + 1.2, [(1200, 330), (1200, 530), (1200, 730), (1200, 930)])]
    for k, (tk, pts) in enumerate(niveis):
        for (x, y) in pts:
            E.foco(c, t, tk, 0.4, lambda a, x=x, y=y: nucleo(c, x, y, 10, 12, 12, a, 30 + x // 10))
            if k > 0:
                for (px, py) in niveis[k - 1][1]:
                    if abs(py - y) < 300:
                        p = ep(t, tk - 0.3, 0.4)
                        if p > 0:
                            M.arrow(c, px + 60, py, lerp(px + 60, x - 60, p), lerp(py, y, p), "#8A8D96", 1, 4, 14, p)
    E.foco(c, t, C["s07.c"], 0.4, lambda a: E.pilula(c, "reação em cadeia", 1600, 420, 56, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s07.d"], 0.4, lambda a: E.escreve(c, "solta, cresce em frações de segundo", 1360, 600, 44, "i", TINTA, a))
    E.foco(c, t, C["s07.e"], 0.4, lambda a: E.pilula(c, "a bomba atômica", 1600, 720, 56, "g", fundo=ERRADO, a=a))


# ---------------- usina ----------------
def b_usina(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("na usina, a cadeia é", "i", 64) + [("controlada", "g", 60, COR)], XE, 200, passo=0.1)
        E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "barras de controle engolem nêutrons", 640, 320, 44, "g", fundo="#3D4350", a=a))
        E.foco(c, t, C["s08.c"], 0.4, lambda a: E.escreve(c, "cada fissão provoca, em média, só mais uma", 1100, 320, 42, "i", TINTA2, a))
        usina(c, t, C["s08.b"], 260, 440, 1, C["s08.d"], C["s08.e"], C["s08.f"])
        return
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], [("vantagem:", "g", 64, CERTO)] + ps("não solta gás carbônico ao gerar", "i", 64), XE, 260, passo=0.1)
        E.frase(c, t, C["s09.b"], [("problema:", "g", 64, ERRADO)] + ps("o lixo", "i", 64), XE, 420, passo=0.1)
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "radioativo por milhares de anos", 700, 560, 56, "g", fundo=OXI, a=a))
        E.foco(c, t, C["s09.d"], 0.4, lambda a: (M.rrect(c, 1200, 600, 520, 300, 30, "#9CCBE8", a), centro(c, "piscinas e depósitos blindados", 1460, 960, 40, "g", TINTA, a)))
        return
    E.frase(c, t, C["s10.a"], ps("acidentes:", "i", 64), XE, 260, passo=0.1)
    E.foco(c, t, C["s10.a"] + 0.6, 0.4, lambda a: (E.pilula(c, "Chernobyl, 1986", 500, 380, 54, "g", fundo=TINTA, a=a), E.pilula(c, "Fukushima, 2011", 1000, 380, 54, "g", fundo=TINTA, a=a)))
    E.frase(c, t, C["s10.b"], ps("no Brasil, o maior", "i", 62) + [("não foi numa usina:", "g", 58)], XE, 600, passo=0.1)
    E.foco(c, t, C["s10.c"], 0.4, lambda a: E.pilula(c, "Goiânia, 1987: césio de um aparelho médico abandonado", W / 2, 760, 46, "g", fundo=OXI, a=a))


# ---------------- fusão ----------------
def b_fusao(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], [("fusão", "g", 80, OXI)] + ps("= juntar", "i", 66), XE, 220, passo=0.12)
        fusao_anim(c, t, C["s11.b"], W / 2, 470, 1.0, ciclo=3.5)
        cs = eq_nuc(c, t, [C["s11.c"], C["s11.c"] + 0.3, C["s11.c"] + 0.6, C["s11.d"] - 0.3, C["s11.d"], C["s11.e"] - 0.2, C["s11.e"]], EQ_U, W / 2, 820, 100)
        E.foco(c, t, C["s11.c"] + 0.5, 0.4, lambda a: E.escreve(c, "dois isótopos do hidrogênio", 240, 680, 44, "i", TINTA2, a))
        E.foco(c, t, C["s11.f"], 0.4, lambda a: E.formula(c, "2 + 3 = 4 + 1", W / 2, 990, 64, "g", TINTA, a, "center"))
        return
    E.frase(c, t, C["s12.a"], ps("os núcleos são positivos:", "i", 62) + [("se empurram", "g", 58, ERRADO)], XE, 240, passo=0.1)
    E.frase(c, t, C["s12.b"], ps("para vencer, precisam de", "i", 62) + [("milhões de graus", "g", 58, OXI)], XE, 380, passo=0.1)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: (E.bola(c, 1400, 700, 230, "#FFC24A", a), centro(c, "Sol", 1400, 700, 70, "g", TINTA, a), centro(c, "15 milhões de °C", 1400, 780, 44, "g", TINTA, a)))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.formula(c, "H → He", 300, 680, 110, "g", OXI, a))
    E.foco(c, t, C["s12.d"] + 0.8, 0.4, lambda a: E.escreve(c, "o tempo todo: daí vem a luz", 300, 790, 50, "i", TINTA, a))


# ---------------- estrelas ----------------
def b_estrelas(c, t, C, b):
    E.frase(c, t, C["s13.a"], ps("nas estrelas maiores, a fusão", "i", 62) + [("continua", "g", 58, OXI)], XE, 220, passo=0.1)
    cadeia = (("He", C["s13.a"] + 0.8), ("C", C["s13.b"]), ("O", C["s13.c"]), ("Fe", C["s13.d"]))
    for k, (el, tk) in enumerate(cadeia):
        x = 330 + 380 * k
        Q.atomo_em(c, t, tk, x, 470, 80, el)
        if k > 0:
            p = ep(t, tk - 0.2, 0.3)
            if p > 0:
                M.arrow(c, x - 290, 470, lerp(x - 290, x - 100, p), 470, OXI, 1, 6, 20, p)
    E.foco(c, t, C["s13.b"] + 0.4, 0.4, lambda a: E.pilula(c, "o carbono do seu corpo nasceu assim", 710, 640, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s13.d"] + 0.4, 0.4, lambda a: E.pilula(c, "até o ferro", 1470, 600, 46, "g", fundo="#D9732A", a=a))
    E.frase(c, t, C["s13.e"], ps("mais pesados que o ferro, como o", "i", 58) + [("ouro", "g", 54, "#B8860B")], XE, 820, passo=0.08)
    E.frase(c, t, C["s13.f"], ps("nascem quando estrelas", "i", 58) + [("explodem ou se chocam", "g", 54, ERRADO)], XE, 920, passo=0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s14.a"], ps("usina nuclear funciona por fusão?", "i", 62), XE + 450, 190, passo=0.1)
    E.foco(c, t, C["s14.a"] + 1.0, 0.4, lambda a: E.pilula(c, "usina = fusão", 600, 420, 70, "g", fundo=ERRADO, a=a))
    if t >= C["s14.b"]:
        E.risco(c, 360, 450, 840, 390, t, C["s14.b"], largura=12)
    E.foco(c, t, C["s14.b"], 0.4, lambda a: E.pilula(c, "todas as usinas de hoje: fissão", 1300, 420, 54, "g", fundo=CERTO, a=a))
    fissao_anim(c, t, C["s14.b"] + 0.3, 1300, 700, 0.6, ciclo=4.0)
    E.foco(c, t, C["s14.c"], 0.4, lambda a: E.escreve(c, "a fusão para gerar energia ainda está em teste", XE, 960, 52, "i", TINTA2, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s16"]:
        E.frase(c, t, C["s15"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        E.frase(c, t, C["s15.a"], ps("olhe os núcleos que", "i", 62, CLARO) + [("entram", "g", 58, BR)], W / 2, 290, "center", 0.1)
        E.foco(c, t, C["s15.b"], 0.4, lambda a: (E.escreve(c, "um pesado → médios", 300, 450, 70, "g", BR, a), E.pilula(c, "fissão", 1300, 425, 60, "g", fundo=E.COR, a=a)))
        E.foco(c, t, C["s15.c"], 0.4, lambda a: (E.escreve(c, "leves → um maior", 300, 580, 70, "g", BR, a), E.pilula(c, "fusão", 1300, 555, 60, "g", fundo=OXI, a=a)))
        E.frase(c, t, C["s15.d"], ps("quantos nêutrons? feche a", "i", 60, CLARO) + [("soma de cima", "g", 56, BR)], W / 2, 760, "center", 0.1)
        E.foco(c, t, C["s15.e"], 0.4, lambda a: E.pilula(c, "o que falta são nêutrons, de massa 1", W / 2, 880, 48, "g", fundo="#3A3B46", a=a))
        return
    E.foco(c, t, C["s16.a"], 0.4, lambda a: nuc(c, 1, 0, "n", 860, 400, 200, BR, a, BR, E.CLARO))
    E.frase(c, t, C["s16.a"] + 0.4, ps("massa 1, número atômico 0:", "i", 60, CLARO), W / 2, 560, "center", 0.1)
    E.frase(c, t, C["s16.b"], ps("só aparece na", "i", 60, CLARO) + [("soma de cima", "g", 56, BR)], W / 2, 650, "center", 0.1)
    E.frase(c, t, C["s16.c"], [("não", "g", 58, ERRADO), ("compensa", "i", 60, CLARO)] + ps("se faltar um núcleo com prótons:", "i", 60, CLARO), W / 2, 800, "center", 0.08)
    pilula_em(c, t, C["s16.d"], "feche também a soma de baixo", W / 2, 920, 48, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 180)
    itens = [(235, 92, "U"), "+", (1, 0, "n", NEU), "->", (140, 54, "Xe"), "+", (94, 38, "Sr"), "+", "x", (1, 0, "n", NEU)]
    eq_nuc(c, t, [C["s17.a"], C["s17.a"] + 0.3, C["s17.a"] + 0.6, C["s17.b"] - 0.2, C["s17.b"], C["s17.c"] - 0.2, C["s17.c"], C["s17.d"] - 0.2, C["s17.d"], C["s17.d"]], itens, W / 2 - 100, 470, 100)
    E.frase(c, t, C["s17.e"], [("1", "g", 56, COR)] + ps("quantos nêutrons saem?", "i", 60), XE, 700, passo=0.08)
    E.frase(c, t, C["s17.f"], [("2", "g", 56, COR)] + ps("é fissão ou fusão?", "i", 60), XE, 810, passo=0.08)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1600, cy=760, r=150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    itens = [(235, 92, "U"), "+", (1, 0, "n", NEU), "->", (140, 54, "Xe"), "+", (94, 38, "Sr"), "+", "x", (1, 0, "n", NEU)]
    eq_nuc(c, t, [C["s19"]] * 10, itens, W / 2, 330, 96)
    E.foco(c, t, C["s19.a"], 0.4, lambda a: E.formula(c, "em cima: 235 + 1 = 236", W / 2, 520, 64, "g", TINTA, a, "center"))
    E.foco(c, t, C["s19.b"], 0.4, lambda a: E.formula(c, "140 + 94 = 234", W / 2, 620, 64, "g", TINTA, a, "center"))
    E.foco(c, t, C["s19.c"], 0.4, lambda a: E.pilula(c, "faltam 2: dois nêutrons", W / 2, 730, 56, "g", fundo="#6E7280", a=a))
    E.foco(c, t, C["s19.d"], 0.4, lambda a: (E.formula(c, "embaixo: 54 + 38 = 92", W / 2, 850, 64, "g", COR, a, "center"), E.selo(c, W / 2 + 420, 828, 36, True, a)))
    E.foco(c, t, C["s19.e"], 0.4, lambda a: E.pilula(c, "um pesado se partiu: fissão", W / 2, 970, 56, "g", fundo=E.COR, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s20.a"], [("fissão", "g", 62, COR)] + ps("parte um pesado e move as usinas", "i", 64)),
                     (C["s20.b"], [("fusão", "g", 62, OXI)] + ps("junta leves e acende as estrelas", "i", 64)),
                     (C["s20.c"], ps("as somas de cima e de baixo", "i", 64) + [("sempre fecham", "g", 60)])], 220, 390, 190, 64, 46)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("praticando", "g", 100, COR)], XE, 420)
    E.frase(c, t, C["s21.b"], [("Faraday,", "g", 70), ("decaimento", "g", 70), ("e", "i", 74), ("meia-vida", "g", 70)], XE, 570, passo=0.12)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, fissao=b_fissao, cadeia=b_cadeia, usina=b_usina, fusao=b_fusao, estrelas=b_estrelas,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
