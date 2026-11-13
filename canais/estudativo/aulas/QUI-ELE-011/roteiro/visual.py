"""Visual — Estudativo · QUI-ELE-011: emissões alfa, beta e gama. Primeira aula do módulo Radioatividade.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001) e a da trilha (QUI-ELE-001).
LINGUAGEM VISUAL DA RADIOATIVIDADE (as aulas QUI-ELE-011 a 014 copiam daqui):
- NÚCLEO = cacho de bolinhas: próton em laranja PROTON (a carga +, como na Física) e nêutron em cinza Q.NEUTRON (peça local
  nucleo(), candidata ao kit). Núcleo instável treme de leve.
- NUCLÍDEO = símbolo com a massa em cima e o número atômico embaixo, à esquerda (peça local nuc(): o Q.formula não aceita
  "^{4}_{2}α", porque só põe os números em símbolo de elemento). Equação nuclear com eq_nuc(), cada termo no seu instante.
  Massa (em cima) em TINTA, número atômico (embaixo) em turquesa: são as duas somas que fecham.
- PARTÍCULAS: alfa = pacote de 2 prótons + 2 nêutrons, rótulo α em laranja; beta = elétron azul Q.ELETRON, rótulo β; gama =
  onda violeta GAMA, rótulo γ (peças locais alfa(), beta(), gama_onda()).
- PENETRAÇÃO = três barreiras lado a lado: papel (folha clara), alumínio (placa cinza), chumbo (bloco escuro); cada emissão
  para na sua (peça local barreiras()).
- CONTAGEM de decaimentos: massa que caiu ÷ 4 = alfas; o que falta no número atômico = betas (pílulas na cor da partícula).
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
ARQUIVO_FINAL = "estudativo_QUI-ELE-011_emissoes_alfa_beta_gama.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "alfa", "penetra", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PROTON, GAMA, BETA = "#E07B39", "#8E44AD", Q.ELETRON

# contas da aula
assert (238 - 4, 92 - 2) == (234, 90) and (234, 90 + 1) == (234, 91)
assert (238 - 206) / 4 == 8 and 92 - 2 * 8 == 76 and 82 - 76 == 6
assert 238 == 206 + 8 * 4 and 92 == 82 + 8 * 2 - 6
assert (232 - 208) / 4 == 6 and 90 - 2 * 6 == 78 and 82 - 78 == 4 and 90 == 82 + 6 * 2 - 4


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def s01():
            E.foco(c, t, C["s01.a"], 0.5, lambda a: (nucleo(c, 560, 560, 26, 34, 15, a, 3, 1, t), nuc(c, 238, 92, "U", 440, 820, 110, TINTA, a)))
            if t >= C["s01.a"] + 0.6:
                M.arrow(c, 760, 560, lerp(760, 1120, ep(t, C["s01.a"] + 0.6, 0.8)), 560, TINTA2, 1, 6, 22, ep(t, C["s01.a"] + 0.6, 0.8))
            E.foco(c, t, C["s01.a"] + 1.2, 0.5, lambda a: (nucleo(c, 1360, 560, 22, 30, 15, a, 5), nuc(c, 206, 82, "Pb", 1240, 820, 110, TINTA, a)))
            E.foco(c, t, C["s01.a"] + 1.4, 0.4, lambda a: E.pilula(c, "bilhões de anos", 940, 480, 46, "g", fundo=TINTA2, a=a))
            if t >= C["s01.b"]:
                for k in range(4):
                    f = ((t - C["s01.b"]) * 0.5 + k / 4) % 1.0
                    ang = -1.2 + k * 0.8
                    x, y = 560 + 120 * math.cos(ang) + 500 * f * math.cos(ang), 560 + 120 * math.sin(ang) + 300 * f * math.sin(ang)
                    (alfa if k % 2 == 0 else beta)(c, x, y, 12, ep(t, C["s01.b"], 0.4) * (1 - f), False)
            E.frase(c, t, C["s01.c"], ps("dá para contar quantas,", "i", 64), W / 2, 960, "center", 0.1)
            E.frase(c, t, C["s01.d"], [("em trinta segundos", "g", 62, COR)], W / 2, 1050, "center")
        E.saida(c, t, C["s02"] - 0.1, s01)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1580, 560, 230 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 230, passo=0.14)
    lista(c, t, [(C["s02.b"], ps("escrever a", "i", 66) + [("equação de um decaimento", "g", 62)]),
                 (C["s02.c"], ps("comparar quanto cada uma", "i", 66) + [("atravessa", "g", 62)]),
                 (C["s02.d"], [("contar", "g", 62, COR)] + ps("as partículas do urânio ao chumbo", "i", 62)),
                 (C["s02.e"], [("atalho", "g", 62, COR), ("de", "i", 66), ("prova", "i", 66)])], XE, 390, 150, 62)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 76, TINTA2) + [("duas", "g", 70, COR), ("coisas", "i", 76, TINTA2)], XE, 190, passo=0.12)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: nucleo(c, 1450, 520, 6, 6, 26, a, 4))
    E.foco(c, t, C["s03.a"] + 0.5, 0.4, lambda a: (E.bola(c, 1300, 760, 22, PROTON, a), E.escreve(c, "próton", 1340, 775, 46, "g", TINTA, a), E.bola(c, 1530, 760, 22, Q.NEUTRON, a), E.escreve(c, "nêutron", 1570, 775, 46, "g", TINTA, a)))
    E.frase(c, t, C["s03.b"], [("número atômico", "g", 60, COR)] + ps("= prótons", "i", 64), XE, 380, passo=0.1)
    E.frase(c, t, C["s03.c"], [("número de massa", "g", 60)] + ps("= prótons + nêutrons", "i", 64), XE, 500, passo=0.1)
    E.foco(c, t, C["s03.c"] + 1.6, 0.4, lambda a: E.escreve(c, "aqui, chamado só de massa", XE, 590, 48, "i", TINTA2, a))
    E.frase(c, t, C["s03.d"], ps("e resolver uma", "i", 64) + [("equação simples", "g", 60)], XE, 760, passo=0.1)


# ---------------- radioatividade ----------------
def b_ideia(c, t, C, b):
    if t < C["s05"]:
        E.foco(c, t, C["s04"], 0.5, lambda a: nucleo(c, 600, 560, 24, 32, 16, a, 7, 1, t))
        E.frase(c, t, C["s04"], ps("núcleo", "i", 66) + [("instável", "g", 62, COR)], XE, 220, passo=0.12)
        if t >= C["s04.a"]:
            f = ((t - C["s04.a"]) * 0.5) % 1.0
            alfa(c, 760 + 600 * f, 480 - 200 * f, 16, ep(t, C["s04.a"], 0.4) * (1 - f * 0.7))
            gama_onda(c, 760, lerp(760, 1500, ep(t, C["s04.a"] + 0.5, 1.0)), 680, 18, 50, ep(t, C["s04.a"] + 0.5, 0.4))
        E.frase(c, t, C["s04.b"], [("radioatividade", "g", 76, COR)], 1000, 880)
        E.foco(c, t, C["s04.b"] + 1.2, 0.4, lambda a: E.escreve(c, "Becquerel e Marie Curie, fim do século dezenove", 1000, 950, 40, "i", TINTA2, a))
        E.foco(c, t, C["s04.c"], 0.4, lambda a: E.pilula(c, "soltou algo e virou outro: decaiu", 600, 990, 46, "g", fundo=TINTA, a=a))
        return
    E.frase(c, t, C["s05.a"], ps("o símbolo com", "i", 66) + [("dois números", "g", 62, COR)], XE, 220, passo=0.12)
    E.foco(c, t, C["s05.a"] + 0.6, 0.5, lambda a: nuc(c, 238, 92, "U", 700, 640, 300, TINTA, a))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.pilula(c, "em cima: a massa", 1560, 430, 54, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "embaixo: o número atômico", 1560, 760, 54, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s05.d"], ps("urânio 238, número atômico 92", "i", 58, TINTA2), W / 2, 950, "center", 0.1)


# ---------------- alfa ----------------
EQ_A = [(238, 92, "U"), "->", (4, 2, "α", PROTON), "+", (234, 90, "Th")]


def b_alfa(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], ps("a primeira:", "i", 70) + [("alfa", "g", 80, PROTON)], XE, 220, passo=0.12)
        E.foco(c, t, C["s06.b"], 0.5, lambda a: alfa(c, 640, 560, 60, a, False))
        E.foco(c, t, C["s06.b"] + 0.6, 0.4, lambda a: E.escreve(c, "2 prótons + 2 nêutrons", 900, 560, 64, "g", TINTA, a))
        E.foco(c, t, C["s06.c"], 0.4, lambda a: E.escreve(c, "o núcleo do hélio", 900, 660, 56, "i", TINTA2, a))
        E.foco(c, t, C["s06.d"], 0.5, lambda a: nuc(c, 4, 2, "α", 640, 900, 160, PROTON, a))
        E.foco(c, t, C["s06.d"] + 0.4, 0.4, lambda a: E.escreve(c, "massa 4, número atômico 2", 900, 880, 56, "g", TINTA, a))
        return
    cs = eq_nuc(c, t, [C["s07.a"], C["s07.a"] + 0.4, C["s07.a"] + 0.7, C["s07.b"] - 0.3, C["s07.b"]], EQ_A, W / 2, 470, 130)
    E.foco(c, t, C["s07.b"], 0.4, lambda a: E.pilula(c, "massa: 238 − 4 = 234", cs[4], 620, 46, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s07.c"], 0.4, lambda a: E.pilula(c, "número atômico: 92 − 2 = 90", cs[4], 720, 46, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s07.d"], 0.4, lambda a: E.escreve(c, "90 prótons: o tório", cs[4] - 220, 830, 50, "i", TINTA2, a))
    E.foco(c, t, C["s07.e"], 0.4, lambda a: E.formula(c, "238 = 234 + 4", 300, 960, 64, "g", TINTA, a))
    E.foco(c, t, C["s07.e"] + 1.2, 0.4, lambda a: E.formula(c, "92 = 90 + 2", 1000, 960, 64, "g", COR, a))


# ---------------- beta ----------------
EQ_B = [(234, 90, "Th"), "->", (0, -1, "β", BETA), "+", (234, 91, "Pa")]


def b_beta(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("a segunda:", "i", 70) + [("beta", "g", 80, BETA)], XE, 220, passo=0.12)
        E.foco(c, t, C["s08.b"], 0.5, lambda a: (E.bola(c, 600, 520, 50, Q.NEUTRON, a), E.escreve(c, "→", 700, 540, 80, "g", TINTA2, a), E.bola(c, 860, 520, 50, PROTON, a), E.escreve(c, "+", 940, 540, 80, "g", TINTA2, a)))
        E.foco(c, t, C["s08.b"] + 0.5, 0.4, lambda a: beta(c, 1060, 520, 30, a, False))
        if t >= C["s08.c"]:
            f = ease_out(prog(t, C["s08.c"], 1.2))
            beta(c, lerp(1060, 1600, f), lerp(520, 380, f), 30, 1, False)
            E.foco(c, t, C["s08.c"] + 0.4, 0.4, lambda a: E.pilula(c, "o elétron é atirado para fora", 1300, 640, 44, "g", fundo=BETA, a=a))
        E.foco(c, t, C["s08.d"], 0.5, lambda a: nuc(c, 0, -1, "β", 640, 900, 160, BETA, a))
        E.foco(c, t, C["s08.d"] + 0.4, 0.4, lambda a: E.escreve(c, "massa 0, carga −1", 900, 880, 56, "g", TINTA, a))
        return
    cs = eq_nuc(c, t, [C["s09.a"], C["s09.a"] + 0.4, C["s09.a"] + 0.7, C["s09.b"] - 0.3, C["s09.b"]], EQ_B, W / 2, 470, 130)
    E.foco(c, t, C["s09.b"], 0.4, lambda a: E.pilula(c, "massa igual: 234", cs[4], 620, 46, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "número atômico: 90 + 1 = 91", cs[4], 720, 46, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s09.d"], 0.4, lambda a: E.escreve(c, "virou o protactínio", cs[4] - 220, 830, 50, "i", TINTA2, a))


# ---------------- gama ----------------
def b_gama(c, t, C, b):
    E.frase(c, t, C["s10.a"], ps("a terceira:", "i", 70) + [("gama", "g", 80, GAMA)], XE, 220, passo=0.12)
    gama_onda(c, XE, lerp(XE, 1700, ep(t, C["s10.b"], 1.2)), 470, 40, 120, ep(t, C["s10.b"], 0.4), rotulo=False)
    E.foco(c, t, C["s10.b"] + 0.6, 0.4, lambda a: E.escreve(c, "uma onda, como a luz, com muito mais energia", XE, 610, 52, "i", TINTA, a))
    E.foco(c, t, C["s10.c"], 0.5, lambda a: nuc(c, 0, 0, "γ", 640, 820, 160, GAMA, a))
    E.foco(c, t, C["s10.d"], 0.4, lambda a: E.escreve(c, "não muda nem a massa nem o número atômico", 840, 800, 44, "g", TINTA, a))
    E.foco(c, t, C["s10.e"], 0.4, lambda a: E.pilula(c, "costuma sair junto com uma alfa ou uma beta", W / 2, 980, 44, "g", fundo=GAMA, a=a))


# ---------------- penetração ----------------
def b_penetra(c, t, C, b):
    E.frase(c, t, C["s11"], ps("qual atravessa mais?", "i", 66, TINTA2), XE, 180, passo=0.12)
    bx = barreiras(c, t, C["s11"] + 0.3, 620, 560, 560)
    xp, xal, xpb = bx[0][0], bx[1][0], bx[2][0]
    y1, y2, y3 = 400, 560, 720
    # alfa para no papel
    if t >= C["s11.a"]:
        f = ease_out(prog(t, C["s11.a"], 1.0))
        alfa(c, lerp(260, xp - 30, f), y1, 18, 1, True)
        E.foco(c, t, C["s11.b"], 0.4, lambda a: E.pilula(c, "alfa: para no papel", 330, y1 - 80, 40, "g", fundo=PROTON, a=a))
    if t >= C["s11.c"]:
        f = ease_out(prog(t, C["s11.c"], 1.2))
        beta(c, lerp(260, xal - 30, f), y2, 18, 1, True)
        E.foco(c, t, C["s11.d"], 0.4, lambda a: E.pilula(c, "beta: para no alumínio", 330, y2 - 80, 40, "g", fundo=BETA, a=a))
    if t >= C["s11.e"]:
        f = ease_out(prog(t, C["s11.e"], 1.4))
        x1 = lerp(220, xpb + 60, f)
        gama_onda(c, 220, x1, y3, 16, 50, 1, rotulo=False)
        if f > 0.9:
            gama_onda(c, xpb + 110, xpb + 260, y3, 6, 50, 0.5, rotulo=False)
        E.foco(c, t, C["s11.f"], 0.4, lambda a: E.pilula(c, "gama: só chumbo grosso ou concreto", 470, y3 + 90, 40, "g", fundo=GAMA, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("a beta diminui o número atômico?", "i", 62), XE + 450, 190, passo=0.1)
    if t < C["s12.c"]:
        E.foco(c, t, C["s12.a"] + 0.8, 0.4, lambda a: E.formula(c, "90 − 1 = 89", W / 2, 480, 110, "g", ERRADO, a, "center"))
        if t >= C["s12.b"]:
            E.risco(c, W / 2 - 330, 500, W / 2 + 330, 400, t, C["s12.b"], largura=12)
        return
    E.foco(c, t, C["s12.c"], 0.5, lambda a: (E.bola(c, 600, 480, 50, Q.NEUTRON, a), E.escreve(c, "→", 700, 500, 80, "g", TINTA2, a), E.bola(c, 860, 480, 50, PROTON, a), E.escreve(c, "+", 940, 500, 80, "g", TINTA2, a), beta(c, 1060, 480, 30, a, False)))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.pilula(c, "um próton a mais", 860, 620, 54, "g", fundo=PROTON, a=a))
    E.foco(c, t, C["s12.e"], 0.4, lambda a: E.formula(c, "90 + 1 = 91", W / 2, 840, 110, "g", COR, a, "center"))
    E.foco(c, t, C["s12.e"] + 0.5, 0.4, lambda a: E.selo(c, W / 2 + 380, 810, 48, True, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.foco(c, t, C["s13"], 0.4, lambda a: (nuc(c, 238, 92, "U", 300, 300, 140, BR, a, BR, E.CLARO), E.escreve(c, "→", 620, 290, 110, "g", CLARO, a), nuc(c, 206, 82, "Pb", 820, 300, 140, BR, a, BR, E.CLARO)))
    if t < C["s14"]:
        E.frase(c, t, C["s13.b"], ps("conte as alfas", "i", 64, CLARO) + [("pela massa", "g", 60, BR)], XE, 520, passo=0.1)
        E.foco(c, t, C["s13.c"], 0.4, lambda a: E.formula(c, "238 − 206 = 32", XE, 660, 90, "g", BR, a))
        E.foco(c, t, C["s13.d"], 0.4, lambda a: E.formula(c, "32 ÷ 4", XE, 800, 90, "g", BR, a))
        E.foco(c, t, C["s13.e"], 0.4, lambda a: E.pilula(c, "8 alfas", XE + 560, 770, 64, "g", fundo=PROTON, a=a))
        return
    E.foco(c, t, -10, 0.4, lambda a: E.pilula(c, "8 alfas", 1500, 280, 60, "g", fundo=PROTON, a=a))
    if t < C["s15"]:
        E.foco(c, t, C["s14.a"], 0.4, lambda a: E.formula(c, "8 × 2 = 16 prótons a menos", XE, 520, 76, "g", BR, a))
        E.foco(c, t, C["s14.b"], 0.4, lambda a: E.formula(c, "92 − 16 = 76", XE, 650, 90, "g", BR, a))
        E.foco(c, t, C["s14.c"], 0.4, lambda a: E.formula(c, "chumbo: 82", XE + 800, 650, 90, "g", E.CLARO, a))
        E.foco(c, t, C["s14.d"], 0.4, lambda a: E.formula(c, "82 − 76 = 6", XE, 800, 90, "g", BR, a))
        E.foco(c, t, C["s14.e"], 0.4, lambda a: E.pilula(c, "6 betas", XE + 680, 770, 64, "g", fundo=BETA, a=a))
        return
    E.foco(c, t, -10, 0.4, lambda a: E.pilula(c, "6 betas", 1500, 380, 60, "g", fundo=BETA, a=a))
    E.frase(c, t, C["s15.a"], ps("a beta não mexe na massa: a massa conta", "i", 60, CLARO) + [("só as alfas", "g", 56, BR)], W / 2, 580, "center", 0.08)
    E.frase(c, t, C["s15.b"], [("não", "g", 58, ERRADO), ("compensa", "i", 60, CLARO)] + ps("com outra partícula:", "i", 60, CLARO), W / 2, 740, "center", 0.1)
    pilula_em(c, t, C["s15.c"], "monte as duas somas, a de cima e a de baixo", W / 2, 870, 46, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: nuc(c, 232, 90, "Th", XE, 480, 160, TINTA, a))
    E.foco(c, t, C["s16.b"], 0.4, lambda a: (E.escreve(c, "→", XE + 420, 460, 120, "g", TINTA2, a), nuc(c, 208, 82, "Pb", XE + 600, 480, 160, TINTA, a)))
    E.frase(c, t, C["s16.c"], ps("quantas", "i", 66) + [("alfas", "g", 62, PROTON)] + ps("e quantas", "i", 66) + [("betas", "g", 62, BETA)] + ps("saem?", "i", 66), XE, 720, passo=0.1)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1560, cy=520, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.foco(c, t, C["s18"], 0.4, lambda a: (nuc(c, 232, 90, "Th", 300, 260, 120, TINTA, a), E.escreve(c, "→", 600, 250, 90, "g", TINTA2, a), nuc(c, 208, 82, "Pb", 760, 260, 120, TINTA, a)))
    E.foco(c, t, C["s18.a"], 0.4, lambda a: E.formula(c, "232 − 208 = 24", XE, 450, 84, "g", TINTA, a))
    E.foco(c, t, C["s18.b"], 0.4, lambda a: E.formula(c, "24 ÷ 4 = 6", XE, 570, 84, "g", TINTA, a))
    E.foco(c, t, C["s18.b"] + 0.6, 0.4, lambda a: E.pilula(c, "6 alfas", 1050, 540, 64, "g", fundo=PROTON, a=a))
    E.foco(c, t, C["s18.c"], 0.4, lambda a: E.formula(c, "90 − 12 = 78", XE, 720, 84, "g", TINTA, a))
    E.foco(c, t, C["s18.d"], 0.4, lambda a: E.formula(c, "82 − 78 = 4", XE, 840, 84, "g", TINTA, a))
    E.foco(c, t, C["s18.e"], 0.4, lambda a: E.pilula(c, "4 betas", 1050, 810, 64, "g", fundo=BETA, a=a))
    E.foco(c, t, C["s18.e"] + 0.6, 0.4, lambda a: E.selo(c, 1300, 680, 56, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s19.a"], [("alfa", "g", 62, PROTON)] + ps("tira 4 da massa e 2 do número atômico", "i", 62)),
                     (C["s19.b"], [("beta", "g", 62, BETA)] + ps("sobe o número atômico em 1", "i", 62)),
                     (C["s19.c"], [("gama", "g", 62, GAMA)] + ps("não muda nada e é a que mais atravessa", "i", 62))], 200, 390, 190, 62, 46)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("meia-vida", "g", 100, COR)], XE, 420)
    E.frase(c, t, C["s20.b"], ps("e a idade de um", "i", 80) + [("fóssil", "g", 76)], XE, 570, passo=0.12)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, alfa=b_alfa, beta=b_beta, gama=b_gama, penetra=b_penetra,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
