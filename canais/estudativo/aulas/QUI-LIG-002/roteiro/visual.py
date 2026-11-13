"""Visual — Estudativo · QUI-LIG-002: ligação covalente e estrutura de Lewis.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a da trilha (QUI-LIG-001/roteiro/visual.py).
Nesta aula: elétron de valência = ponto azul (Q.ELETRON) em volta do símbolo; par compartilhado = dois pontos entre os
símbolos, que viram um traço em tinta; par livre ganha caixa pontilhada quando é contado; a conta "4 + 4 = 8" fica embaixo,
com a esfera turquesa no resultado. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ligações Químicas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-LIG-002_ligacao_covalente_lewis.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("covalente", "agua", "dupla", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# contas da aula: valência, ligações e octeto de cada átomo
VAL = {"H": 1, "C": 4, "N": 5, "O": 6, "Cl": 7}
assert 2 * 2 + 2 * 2 == 8                      # O da água: 2 ligações (4 e) + 2 pares livres (4 e)
assert 4 * 2 == 8 and 2 * 2 + 2 * 2 == 8        # CO₂: C com 2 duplas; O com 1 dupla + 2 pares livres
assert 3 * 2 + 2 == 8                           # N₂: tripla + 1 par livre
assert 2 * 2 == 4 and 8 - 4 == 4                # erro O–C–O: C com 4 elétrons
assert VAL["H"] + VAL["C"] + VAL["N"] == 10 == 4 * 2 + 2   # HCN: 4 pares em ligações + 1 par livre
assert all(8 - VAL[e] == n for e, n in (("O", 2), ("N", 3), ("C", 4))) and 2 - VAL["H"] == 1


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def solto(c, cx, cy, s, size, pares=(), sozinhos=(), a=1.0, cor=None, escuro=False):
    """símbolo de Lewis com pares e elétrons sozinhos em ângulos escolhidos (graus, 0 = direita, 90 = cima)"""
    if a <= 0:
        return
    centro(c, s, cx, cy + size * 0.36, size, "g", cor or (BR if escuro else TINTA), a)
    w = E.larg(s, "g", size)
    for ang, n in [(g, 2) for g in pares] + [(g, 1) for g in sozinhos]:
        hor = abs(math.cos(math.radians(ang)))
        dist = lerp(size * 0.62, w / 2 + size * 0.22, hor)
        Q._par(c, cx, cy, ang, dist, size * 0.075, Q.ELETRON, a, n)


def anel(c, t, t0, cx, cy, r, cor=None, t1=None, larg=6):
    """círculo pulsante que marca um átomo ou um par"""
    if t < t0 or (t1 is not None and t >= t1):
        return
    q = ep(t, t0, 0.35)
    c.drawCircle(cx, cy, r + 4 * math.sin(t * 6), M.paint(cor or E.COR, q, stroke=larg))


def caixa(c, t, t0, x, y, w, h, cor=None, t1=None):
    if t < t0 or (t1 is not None and t >= t1):
        return
    p = ep(t, t0, 0.4)
    E.caixa_pontilhada(c, x, y, w, h, p, cor, prog_=p)


# estruturas usadas (unidades de ligação)
AGUA = [("H", -1, 0), ("O", 0, 0, [90, 0]), ("H", 0, 1)]
CO2 = [("O", -1.1, 0, [90, 270]), ("C", 0, 0), ("O", 1.1, 0, [90, 270])]
N2 = [("N", -0.6, 0, [180]), ("N", 0.6, 0, [0])]
HCN = [("H", -1.1, 0), ("C", 0, 0), ("N", 1.1, 0, [0])]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01"], ps("a maior parte do ar:", "i", 70, TINTA2), XE, 250, passo=0.12)
        E.frase(c, t, C["s01.a"], [("gás", "g", 110), ("nitrogênio", "g", 110, COR)], XE, 390, passo=0.2)
        Q.formula_em(c, t, C["s01.a"] + 0.8, "N2", XE, 600, 190)
        Q.molecula(c, t, C["s01.b"], "N2", 1420, 470, 230, passo=0.3)
        pilula_em(c, t, C["s01.b"] + 1.2, "3 ligações ao mesmo tempo", 1420, 720, 50, E.COR)
        E.frase(c, t, C["s01.c"], ps("átomos iguais: ninguém quer perder elétron", "i", 60), W / 2, 920, "center", 0.09)
        E.frase(c, t, C["s01.c"] + 1.8, [("como", "i", 70), ("se seguram?", "g", 66, COR)], W / 2, 1020, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1720, 600, 170 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("estrutura", "g", 66, COR), ("de", "i", 70), ("Lewis", "g", 66, COR)]),
                 (C["s02.c"], [("simples,", "i", 70), ("dupla", "g", 66), ("e", "i", 70), ("tripla", "g", 66)]),
                 (C["s02.d"], [("atalho:", "g", 66, COR), ("quantas", "i", 70), ("ligações?", "i", 70)])], XE, 440, 170)
    for k, f in enumerate(("H2O", "CO2", "N2")):
        Q.formula_em(c, t, C["s02.b"] + 0.9 + 0.3 * k, f, XE + 740 + 210 * k, 445, 76)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("duas ideias de antes", "i", 70, TINTA2), XE, 180, passo=0.12)
    E.frase(c, t, C["s03.a"], [("elétrons de valência", "g", 62, COR), ("=", "g", 62, TINTA2)] + ps("os da última camada", "i", 66), XE, 310, passo=0.12)
    for k, (fam, el, n) in enumerate((("família 15", "N", 5), ("família 16", "O", 6), ("família 17", "Cl", 7))):
        x = 330 + 420 * k
        ti = C["s03.b"] + 0.9 * k
        E.foco(c, t, ti, 0.5, lambda a, x=x, el=el, n=n: Q.simbolo_lewis(c, el, x, 480, 100, n, a))
        E.foco(c, t, ti + 0.2, 0.4, lambda a, x=x, fam=fam, n=n: (centro(c, fam, x, 620, 46, "i", TINTA2, a), centro(c, f"{n} elétrons", x, 680, 46, "b", TINTA, a)))
    E.frase(c, t, C["s03.c"], [("gases nobres:", "g", 60), ("8,", "g", 60, COR)] + ps("estáveis (o hélio tem 2)", "i", 62), XE, 820, passo=0.12)
    E.frase(c, t, C["s03.d"], ps("os outros tendem a chegar a 8:", "i", 62), XE, 930, passo=0.1)
    E.foco(c, t, C["s03.d"] + 1.8, 0.4, lambda a: E.pilula(c, "regra do octeto", XE + 1150, 910, 54, "g", fundo=E.COR, a=a))


# ---------------- covalente (s04–s06) ----------------
def b_covalente(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04"], ps("entre dois ametais", "i", 70, TINTA2), W / 2, 190, "center", 0.12)
            E.frase(c, t, C["s04.a"], [("ninguém", "g", 70, ERRADO)] + ps("quer perder elétron", "i", 74), W / 2, 300, "center", 0.12)
            junta = ease_io(prog(t, C["s04.b"] + 0.3, 1.2))
            xl, xr, y, sz = lerp(620, 830, junta), lerp(1300, 1090, junta), 560, 150
            E.foco(c, t, C["s04"] + 0.3, 0.5, lambda a: (solto(c, xl, y, "Cl", sz, (90, 180, 270), () if junta >= 1 else (0,), a),
                                                         solto(c, xr, y, "Cl", sz, (90, 0, 270), () if junta >= 1 else (180,), a)))
            if junta >= 1:
                Q._par(c, W / 2, y, 0, 0, sz * 0.075, Q.ELETRON, 1.0, 2)
                Q._par(c, W / 2, y, 90, 0, sz * 0.075, Q.ELETRON, 1.0, 1)
            anel(c, t, C["s04.c"], W / 2, y, 46)
            E.frase(c, t, C["s04.b"], [("a saída:", "i", 70), ("dividir", "g", 70, COR)], W / 2, 420, "center", 0.12)
            E.frase(c, t, C["s04.c"] + 0.4, ps("o par conta para os dois átomos", "i", 58, TINTA2), W / 2, 740, "center", 0.1)
            E.frase(c, t, C["s04.d"], [("par compartilhado", "g", 76), ("=", "g", 76, TINTA2), ("ligação covalente", "g", 76, COR)], W / 2, 900, "center", 0.15)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("estrutura", "g", 90), ("de", "i", 96), ("Lewis", "g", 90, COR)], XE, 230, passo=0.15)
            E.frase(c, t, C["s05.b"], ps("o símbolo com os elétrons de valência em volta", "i", 56, TINTA2), XE, 330, passo=0.08)
            for k, (cue, el, nome) in enumerate((("s05.c", "H", "hidrogênio"), ("s05.d", "C", "carbono"), ("s05.e", "N", "nitrogênio"), ("s05.f", "O", "oxigênio"))):
                x = 330 + 420 * k
                E.foco(c, t, C[cue], 0.5, lambda a, x=x, el=el: Q.simbolo_lewis(c, el, x, 620, 140, VAL[el], a))
                E.foco(c, t, C[cue] + 0.2, 0.4, lambda a, x=x, el=el, nome=nome: (centro(c, str(VAL[el]), x, 860, 90, "g", COR, a), centro(c, nome, x, 940, 50, "i", TINTA2, a)))
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    # s06: H· + ·H → H:H → H–H
    E.frase(c, t, C["s06.a"], [("gás", "i", 80), ("hidrogênio", "g", 76, COR)], XE, 220, passo=0.12)
    Q.formula_em(c, t, C["s06.a"] + 0.6, "H2", XE + 720, 222, 96)
    junta = ease_io(prog(t, C["s06.c"], 1.0))
    y, sz = 520, 150
    xl, xr = lerp(700, 860, junta), lerp(1220, 1060, junta)
    E.foco(c, t, C["s06.b"], 0.5, lambda a: (solto(c, xl, y, "H", sz, (), () if junta >= 1 else (0,), a),
                                            solto(c, xr, y, "H", sz, (), () if junta >= 1 else (180,), a)))
    if junta >= 1 and t < C["s06.d"]:
        Q._par(c, W / 2, y, 0, 0, sz * 0.075, Q.ELETRON, 1.0, 2)
        Q._par(c, W / 2, y, 90, 0, sz * 0.075, Q.ELETRON, 1.0, 1)
    if t >= C["s06.d"]:
        p = ease_out(prog(t, C["s06.d"], 0.5))
        M.line(c, W / 2 - 32, y, W / 2 + 32, y, TINTA, 1.0, 10, progress=p)
    E.frase(c, t, C["s06.c"] + 0.6, [("cada", "i", 62), ("H", "g", 60), ("fica", "i", 62), ("com", "i", 62), ("2", "g", 60, COR)] + ps("como o hélio", "i", 62), W / 2, 760, "center", 0.1)
    E.frase(c, t, C["s06.d"] + 0.3, [("1 traço", "g", 70, COR), ("=", "g", 70, TINTA2)] + ps("1 par compartilhado", "i", 74), W / 2, 920, "center", 0.12)


# ---------------- água (s07) ----------------
def b_agua(c, t, C, b):
    E.frase(c, t, C["s07"], [("na", "i", 76), ("água", "g", 76, COR)], XE, 200, passo=0.12)
    Q.formula_em(c, t, C["s07"] + 0.4, "H2O", XE + 330, 202, 96)
    cx, cy, esc, sz = 700, 560, 210, 130
    trac = t >= C["s07.f"] + 2.0
    pts = Q.lewis(c, t, C["s07.a"] - 0.2, AGUA, [(0, 1, 1), (1, 2, 1)], cx, cy, esc, sz, pontos=not trac,
                  tl=[C["s07.b"], C["s07.a"] - 0.2, C["s07.b"] + 0.3], tp=C["s07.d"] - 0.2)
    E.frase(c, t, C["s07.a"], [("O:", "g", 62), ("6", "g", 62, COR)] + ps("precisa de mais 2", "i", 64), 1100, 380, passo=0.1)
    E.frase(c, t, C["s07.b"], ps("cada H forma um par com ele", "i", 58, TINTA2), 1100, 480, passo=0.08)
    E.frase(c, t, C["s07.c"], [("2", "g", 62, COR), ("ligações", "i", 64)], 1100, 580, passo=0.1)
    caixa(c, t, C["s07.e"], cx - 70, cy - 150, 140, 70, E.COR, C["s07.f"])
    caixa(c, t, C["s07.e"] + 0.2, cx + 70, cy - 65, 80, 130, E.COR, C["s07.f"])
    E.frase(c, t, C["s07.d"], [("pares livres:", "g", 62, COR)] + ps("sem ligação", "i", 64), 1100, 680, passo=0.1)
    if t >= C["s07.f"]:
        c.drawCircle(cx + 15, cy - 15, 130, M.paint(E.COR, ep(t, C["s07.f"], 0.4), stroke=5))
    E.foco(c, t, C["s07.f"] + 0.4, 0.4, lambda a: E.formula(c, "4 + 4 =", 1300, 880, 90, "g", TINTA2, a, "right"))
    bola_txt(c, t, C["s07.f"] + 0.9, "8", 1400, 850, 64, 84)
    E.foco(c, t, C["s07.f"] + 0.6, 0.4, lambda a: E.escreve(c, "ligações + pares livres", 1100, 980, 46, "i", TINTA2, a))


# ---------------- dupla (s08–s09) ----------------
def b_dupla(c, t, C, b):
    E.frase(c, t, C["s08"], ps("e se faltar mais de um?", "i", 66, TINTA2), XE, 180, passo=0.1)
    Q.formula_em(c, t, C["s08.a"], "CO2", XE, 330, 120)
    E.frase(c, t, C["s08.b"], [("C:", "g", 56), ("4,", "g", 56, COR)] + ps("precisa de mais 4", "i", 58), XE + 380, 290, passo=0.1)
    E.frase(c, t, C["s08.c"], [("O:", "g", 56), ("6,", "g", 56, COR)] + ps("precisa de mais 2", "i", 58), XE + 380, 370, passo=0.1)
    cy, esc, sz = 600, 230, 130
    Q.lewis(c, t, C["s08.d"], CO2, [(0, 1, 2), (1, 2, 2)], W / 2, cy, esc, sz, pontos=True, tl=[C["s08.d"], C["s08.d"], C["s08.d"]])
    E.frase(c, t, C["s08.e"], [("2 pares", "g", 62), ("=", "g", 62, TINTA2), ("dupla", "g", 62, COR)] + ps("(dois traços)", "i", 60, TINTA2), W / 2, 790, "center", 0.12)
    Q.lewis(c, t, C["s08.f"], CO2, [(0, 1, 2), (1, 2, 2)], W / 2, 940, 180, 100, pontos=False, tl=[C["s08.f"]] * 3)
    # s09: conferir os oitos
    anel(c, t, C["s09.a"], W / 2, cy, 150, E.COR, C["s09.b"])
    E.foco(c, t, C["s09.a"] + 0.3, 0.4, lambda a: E.pilula(c, "C: 4 pares = 8", W / 2, cy - 150, 46, "g", fundo=E.COR, a=a) if t < C["s09.b"] else None)
    for s_ in (-1, 1):
        anel(c, t, C["s09.b"] + 0.2 * (s_ + 1), W / 2 + s_ * esc * 1.1, cy, 125, E.COR)
    E.foco(c, t, C["s09.b"] + 0.6, 0.4, lambda a: E.pilula(c, "cada O: 4 + 4 = 8", W / 2, cy - 150, 46, "g", fundo=E.COR, a=a))


# ---------------- tripla (s10) ----------------
def b_tripla(c, t, C, b):
    E.frase(c, t, C["s10"], [("o", "i", 76), ("nitrogênio", "g", 76, COR), ("do", "i", 76), ("ar", "i", 76)], XE, 190, passo=0.12)
    Q.formula_em(c, t, C["s10"] + 0.6, "N2", XE + 760, 192, 100)
    E.frase(c, t, C["s10.a"], [("N:", "g", 58), ("5,", "g", 58, COR)] + ps("precisa de mais 3", "i", 60), XE, 300, passo=0.1)
    cy = 560
    Q.lewis(c, t, C["s10.b"], N2, [(0, 1, 3)], W / 2, cy, 210, 140, pontos=True, tl=[C["s10.b"]] * 2, tp=C["s10.d"])
    E.frase(c, t, C["s10.c"], [("3 pares", "g", 62), ("=", "g", 62, TINTA2), ("tripla", "g", 62, COR)] + ps("(três traços)", "i", 60, TINTA2), W / 2, 780, "center", 0.12)
    for s_ in (-1, 1):
        caixa(c, t, C["s10.d"] + 0.2 * (s_ + 1), W / 2 + s_ * 126 * 1.0 + s_ * 120 - 40, cy - 60, 80, 120, E.COR, C["s10.e"] + 1.5)
    E.foco(c, t, C["s10.e"], 0.4, lambda a: E.formula(c, "6 + 2 =", 1300, 920, 84, "g", TINTA2, a, "right"))
    bola_txt(c, t, C["s10.e"] + 0.5, "8", 1400, 893, 60, 80)
    Q.lewis(c, t, C["s10.e"] + 1.0, N2, [(0, 1, 3)], 560, 900, 160, 100, pontos=False, tl=[C["s10.e"] + 1.0] * 2, tp=C["s10.e"] + 1.0)
    pilula_em(c, t, C["s10.f"], "tão forte que o N₂ quase não reage", W / 2, 1020, 44, TINTA2, "b")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("tudo com traço simples?", "i", 66), XE + 460, 190, passo=0.1)
    cy = 480
    Q.lewis(c, t, C["s11.b"], [("O", -1.1, 0), ("C", 0, 0), ("O", 1.1, 0)], [(0, 1, 1), (1, 2, 1)], W / 2, cy, 240, 150, tl=[C["s11.b"]] * 3,
            cores={"C": ERRADO, "O": ERRADO})
    anel(c, t, C["s11.c"], W / 2, cy, 130, ERRADO)
    E.foco(c, t, C["s11.c"] + 0.3, 0.4, lambda a: E.formula(c, "C: 2 ligações = 4 elétrons", W / 2, 720, 70, "g", TINTA, a, "center"))
    E.foco(c, t, C["s11.d"], 0.4, lambda a: E.pilula(c, "faltam 4 para o octeto", W / 2, 810, 54, "g", fundo=ERRADO, a=a))
    if t >= C["s11.d"] + 0.6:
        E.risco(c, W / 2 - 380, cy + 40, W / 2 + 380, cy - 60, t, C["s11.d"] + 0.6, largura=12)
    E.frase(c, t, C["s11.e"], [("confira:", "i", 62), ("cada átomo, menos o H,", "g", 56), ("fecha", "i", 62), ("8", "g", 60, COR)], W / 2, 960, "center", 0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        def s12():
            E.frase(c, t, C["s12"], ps("o atalho", "i", 72, CLARO), W / 2, 150, "center", 0.12)
            E.frase(c, t, C["s12.a"], [("ligações", "g", 72, BR), ("=", "g", 72, CLARO)] + ps("o que falta para 8", "i", 76, CLARO), W / 2, 270, "center", 0.12)
            for k, (cue, el, n, nota) in enumerate((("s12.b", "H", 1, "fecha com 2"), ("s12.c", "O", 2, ""), ("s12.d", "N", 3, ""), ("s12.e", "C", 4, ""))):
                x = 330 + 420 * k
                y = 520

                def peca(a, x=x, el=el, n=n, nota=nota):
                    Q.atomo(c, x, y, 70, el, a, escuro=True)
                    for j in range(n):
                        g = math.radians(90 - 360 * j / n if n > 1 else 0)
                        M.line(c, x + 82 * math.cos(g), y - 82 * math.sin(g), x + 140 * math.cos(g), y - 140 * math.sin(g), BR, a, 8)
                    centro(c, str(n), x, y + 250, 110, "g", E.CLARO, a)
                    if nota:
                        centro(c, nota, x, y + 320, 42, "i", CLARO, a)
                E.foco(c, t, C[cue], 0.5, peca)
            E.frase(c, t, C["s12.f"], [("dupla", "g", 60, BR), ("vale 2,", "i", 62, CLARO), ("tripla", "g", 60, BR), ("vale 3", "i", 62, CLARO)], W / 2, 1000, "center", 0.12)
        E.saida(c, t, C["s13"] - 0.1, s12)
        return
    E.frase(c, t, C["s13.a"], ps("funciona porque", "i", 66, CLARO), W / 2, 250, "center", 0.12)
    E.frase(c, t, C["s13.a"] + 0.9, ps("cada ligação traz um elétron do vizinho", "i", 66, BR), W / 2, 360, "center", 0.1)
    E.frase(c, t, C["s13.b"], [("não", "g", 64, ERRADO), ("vale", "i", 66, CLARO)] + ps("para quem foge do octeto:", "i", 66, CLARO), W / 2, 560, "center", 0.12)
    E.foco(c, t, C["s13.b"] + 1.4, 0.5, lambda a: Q.simbolo_lewis(c, "B", W / 2, 720, 130, 3, a, escuro=True))
    E.foco(c, t, C["s13.b"] + 1.6, 0.4, lambda a: centro(c, "boro", W / 2 + 200, 740, 56, "i", CLARO, a))
    pilula_em(c, t, C["s13.c"], "outra aula", W / 2, 900, 50, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s14.a"], ps("ácido cianídrico", "i", 62, TINTA2), XE, 290, passo=0.1)
    Q.formula_em(c, t, C["s14.a"] + 0.3, "HCN", XE, 470, 170)
    pilula_em(c, t, C["s14.a"] + 1.2, "muito tóxico", XE + 620, 420, 46, ERRADO)
    E.frase(c, t, C["s14.b"], ps("desenhe a estrutura de Lewis", "i", 62), XE, 620, passo=0.08)
    E.frase(c, t, C["s14.c"], [("1", "g", 56, COR)] + ps("que ligação entre C e N?", "i", 60), XE, 740, passo=0.08)
    E.frase(c, t, C["s14.d"], [("2", "g", 56, COR)] + ps("quantos pares livres?", "i", 60), XE, 850, passo=0.08)
    if t < C["s15"]:
        for k, el in enumerate(("H", "C", "N")):
            E.foco(c, t, C["s14.a"] + 0.8 + 0.3 * k, 0.5, lambda a, k=k, el=el: Q.simbolo_lewis(c, el, 1220 + 230 * k, 520, 120, VAL[el], a))
    else:
        E.relogio(c, t, C["s15.a"], cx=1480, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    cy, esc, sz = 380, 286, 150
    if t < C["s16.e"]:
        Q.lewis(c, t, C["s16.a"], [("H", -1.1, 0), ("C", 0, 0), ("N", 1.1, 0)], [(0, 1, 1)], W / 2, cy, esc, sz,
                tl=[C["s16.a"], C["s16.a"] + 0.3, C["s16.c"]])
        p = ease_out(prog(t, C["s16.d"], 0.6))
        if p > 0:
            for k in (-1, 0, 1):
                M.line(c, W / 2 + 85, cy + k * 26, W / 2 + esc * 1.1 - 85, cy + k * 26, TINTA, 1.0, 10, progress=p)
    else:
        Q.lewis(c, t, C["s16.e"] - 1, HCN, [(0, 1, 1), (1, 2, 3)], W / 2, cy, esc, sz, tl=[0, 0, 0], tp=C["s17.c"])
    E.frase(c, t, C["s16"], ps("com o atalho", "i", 62, TINTA2), XE, 170, passo=0.1)
    E.foco(c, t, C["s16.a"] + 0.4, 0.4, lambda a: centro(c, "H: 1, na ponta", W / 2 - esc * 1.1, cy + 190, 50, "b", TINTA, a))
    E.foco(c, t, C["s16.b"], 0.4, lambda a: centro(c, "C: faltam 3", W / 2, cy + 190, 50, "b", TINTA, a))
    E.foco(c, t, C["s16.c"], 0.4, lambda a: centro(c, "N: 3", W / 2 + esc * 1.1, cy + 190, 50, "b", TINTA, a))
    E.foco(c, t, C["s16.d"] + 0.4, 0.4, lambda a: E.pilula(c, "tripla entre C e N", W / 2 + esc * 0.55, cy - 170, 46, "g", fundo=E.COR, a=a))
    if t < C["s17"]:
        return
    E.foco(c, t, C["s17.a"], 0.4, lambda a: E.formula(c, "C: 2 + 6 = 8, nenhum livre", XE, 760, 62, "g", TINTA, a))
    E.foco(c, t, C["s17.b"], 0.4, lambda a: E.formula(c, "N: 6 da tripla", XE, 870, 62, "g", TINTA, a))
    E.foco(c, t, C["s17.c"], 0.4, lambda a: E.formula(c, "+ 1 par livre = 8", XE + 480, 870, 62, "g", COR, a))
    caixa(c, t, C["s17.c"], W / 2 + esc * 1.1 + 70, cy - 60, 80, 120, E.COR)
    E.foco(c, t, C["s17.d"], 0.5, lambda a: (E.pilula(c, "tripla e 1 par livre no N", W / 2, 1000, 60, "g", fundo=CERTO, a=a), E.selo(c, W / 2 + 470, 990, 44, True, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s18.a", [("covalente", "g", 64), ("=", "g", 64, TINTA2)] + ps("par de elétrons compartilhado", "i", 66)),
                 ("s18.b", [("cada traço", "g", 64), ("=", "g", 64, TINTA2)] + ps("um par", "i", 66)),
                 ("s18.c", [("ligações", "g", 64), ("=", "g", 64, TINTA2)] + ps("o que falta para 8", "i", 66)))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 50, a=a), centro(c, str(i + 1), 260, y - 2, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 350, y, passo=0.12)
        Q.lewis(c, t, C["s18.c"] + 0.6, AGUA, [(0, 1, 1), (1, 2, 1)], 1600, 880, 120, 80, tl=[C["s18.c"] + 0.6] * 3)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 240)
    E.frase(c, t, C["s19"] + 0.8, [("ligação", "g", 110, COR)], XE, 390)
    E.frase(c, t, C["s19"] + 1.2, [("metálica", "g", 110, COR)], XE, 510)
    E.frase(c, t, C["s19.a"], ps("por que o cobre conduz e dobra", "i", 60), XE, 640, passo=0.1)
    E.frase(c, t, C["s19.b"], [("bronze", "g", 60), ("e", "i", 62), ("aço:", "g", 60)] + ps("do que são feitos", "i", 62), XE, 740, passo=0.1)
    for k in range(4):
        Q.atomo_em(c, t, C["s19.a"] + 0.15 * k, 420 + 110 * k, 900, 46, "Cu")
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, covalente=b_covalente, agua=b_agua, dupla=b_dupla, tripla=b_tripla,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
