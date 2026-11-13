"""Visual — Estudativo · QUI-ORG-009: amina, amida e nitrila.
Segue a linguagem da Química (QUI-MIS-001), da Orgânica (QUI-ORG-001) e do módulo Funções (QUI-ORG-006). Nesta aula: o
nitrogênio sai azul (CPK) e o PAR LIVRE em azul Q.ELETRON (Q.lewis com ângulo do par); o H⁺ que a base captura é uma bolinha
branca com "+" que voa até o par. Amida = halo que cobre N e carbonila juntos; amina = halo só no N.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (linguagem da Orgânica, QUI-ORG-001; [kit] = candidatas a quimica.py) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def pilula_esq(c, t, t0, s, x, cy, size, fundo=None, est="i", cor=BR):
    """pílula alinhada pela esquerda em x"""
    w = E.larg(s, est, size) + size * 1.1
    pilula_em(c, t, t0, s, x + w / 2, cy, size, fundo, est, cor)
    return w


def lista(c, t, itens, x, y0, dy):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, y=y, i=i: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def pts_tela(pts, cx, cy, esc):
    return [(cx + x * esc, cy + y * esc) for x, y in pts]


def anel(n=6, r=1.0, rot=90, cx=0.0, cy=0.0):
    """vértices de um anel regular em unidades de ligação (lado = 1 quando r = 1 e n = 6)"""
    return [(cx + r * math.cos(math.radians(rot + 360 * k / n)), cy - r * math.sin(math.radians(rot + 360 * k / n))) for k in range(n)]


def ligs_anel(i0, n):
    return [(i0 + k, i0 + (k + 1) % n) for k in range(n)]


def viz_de(n, ligs=None):
    ligs = ligs or [(i, i + 1) for i in range(n - 1)]
    v = {i: [] for i in range(n)}
    for i, j in ligs:
        v[i].append(j); v[j].append(i)
    return v


def hs(c, t, t0, P, i, viz, n, size=50, cor=TINTA2, dist=None, a_max=1.0):
    """[kit] hidrogênios escondidos do vértice i: rótulo H₃/H₂/H por fora, do lado oposto aos vizinhos"""
    if n <= 0 or t < t0:
        return
    ux = uy = 0.0
    for j in viz:
        dx, dy = P[j][0] - P[i][0], P[j][1] - P[i][1]
        L = math.hypot(dx, dy) or 1
        ux, uy = ux + dx / L, uy + dy / L
    L = math.hypot(ux, uy)
    ux, uy = (-ux / L, -uy / L) if L > 0.2 else (0, -1)
    dist = dist or size * 1.15
    x, y = P[i][0] + ux * dist, P[i][1] + uy * dist
    s = "H" if n == 1 else f"H{n}"
    E.foco(c, t, t0, 0.4, lambda a: Q.formula(c, s, x, y + size * 0.36, size, cor, a * a_max, "center"), sobe=8)


def realce(c, t, t0, A, B, cor=None, d=0.4, largura=22, alfa=0.45, t1=None):
    """[kit] faixa clara por cima de uma ligação do bastão (a ligação que conta, a cadeia principal)"""
    p = ease_io(prog(t, t0, d))
    if t1 is not None:
        p *= 1 - ep(t, t1, 0.3)
    if p > 0:
        M.line(c, A[0], A[1], B[0], B[1], cor or E.COR, alfa, largura, progress=p)


def realca_fila(c, t, t0, P, fila, cor=None, passo=0.15, largura=22, alfa=0.45, t1=None):
    for k in range(len(fila) - 1):
        realce(c, t, t0 + k * passo, P[fila[k]], P[fila[k + 1]], cor, 0.3, largura, alfa, t1)


def halo(c, t, t0, pts, r=70, cor=None, alfa=0.25, t1=None):
    """[kit] mancha translúcida atrás de um grupo funcional"""
    a = ep(t, t0, 0.5) * alfa
    if t1 is not None:
        a *= 1 - ep(t, t1, 0.4)
    if a <= 0:
        return
    lay = skia.Paint()
    lay.setAlphaf(a)
    lay.setImageFilter(skia.ImageFilters.Blur(r * 0.18, r * 0.18))
    c.saveLayer(None, lay)
    k = ease_back(prog(t, t0, 0.5))
    for x, y in pts:
        c.drawCircle(x, y, r * k, M.paint(cor or E.COR))
    c.restore()


def anelc(c, t, t0, P, i, r=34, cor=None, t1=None, largura=6):
    """anel de destaque em volta de um átomo ou vértice"""
    q = ep(t, t0, 0.3)
    if t1 is not None:
        q *= 1 - ep(t, t1, 0.3)
    if q > 0:
        c.drawCircle(P[i][0], P[i][1], r, M.paint(cor or E.COR, q, stroke=largura))


def cond(c, t, t0, partes, x, y, size, cores=None, passo=0.25, align="left", traco="–"):
    """[kit] fórmula condensada em fila: partes = ["CH3", "CH2", "OH"], com o traço entre os grupos. Devolve as caixas (x0, x1)"""
    cores = cores or {}
    ws = [Q.formula(None, p, 0, 0, size) for p in partes]
    wt = Q.formula(None, traco, 0, 0, size)
    tot = sum(ws) + wt * (len(partes) - 1)
    xx = x - tot / 2 if align == "center" else x
    caixas = []
    for k, (p, w) in enumerate(zip(partes, ws)):
        cor = cores.get(k)
        E.foco(c, t, t0 + k * passo, 0.4, lambda a, p=p, xx=xx, cor=cor: Q.formula(c, p, xx, y, size, cor, a))
        caixas.append((xx, xx + w))
        xx += w
        if k < len(partes) - 1:
            E.foco(c, t, t0 + k * passo + 0.15, 0.4, lambda a, xx=xx: Q.formula(c, traco, xx, y, size, TINTA2, a))
            xx += wt
    return caixas


def nome(c, t, t0, pecas, x, y, size=110, passo=0.4, align="left", leg=40):
    """[kit] nome oficial por peças: pecas = [(texto, cor, legenda ou None)]; legenda pequena embaixo. Devolve os centros"""
    ws = [E.larg(p[0], "g", size) for p in pecas]
    tot = sum(ws)
    xx = x - tot / 2 if align == "center" else x
    cs = []
    for k, (p, w) in enumerate(zip(pecas, ws)):
        s, cor = p[0], p[1]
        lg = p[2] if len(p) > 2 else None
        tk = t0 + k * passo
        E.foco(c, t, tk, 0.4, lambda a, s=s, xx=xx, cor=cor: E.escreve(c, s, xx, y, size, "g", cor, a))
        if lg:
            E.foco(c, t, tk + 0.2, 0.4, lambda a, lg=lg, cx=xx + w / 2, k=k: centro(c, lg, cx, y + leg * (1.6 + 1.15 * (k % 2)), leg, "i", TINTA2, a))
        cs.append(xx + w / 2)
        xx += w
    return cs


def seta(c, t, t0, x0, y0, x1, y1, cor=None, d=0.5, largura=6):
    p = ep(t, t0, d)
    if p > 0:
        M.arrow(c, x0, y0, x1, y1, cor or E.COR, p, largura, 22, ease_io(prog(t, t0, d)))


def mol(c, t, t0, M_, cx, cy, esc, d=1.0, numeros=None, escuro=False, largura=7, size=None):
    """bastão de uma molécula descrita em dict(pts, ligs, duplas, triplas, rot). Devolve os pontos na tela"""
    Q.bastao(c, t, t0, M_["pts"], cx, cy, esc, duplas=M_.get("duplas", ()), triplas=M_.get("triplas", ()), rotulos=M_.get("rot"),
             d=d, numeros=numeros, escuro=escuro, ligacoes=M_.get("ligs"), largura=largura, size=size)
    return pts_tela(M_["pts"], cx, cy, esc)
E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-009_amina_amida_nitrila.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("amina", "amida", "remedio", "erro", "atalho", "questao", "fim"))

Z3f = [(x, -y) for x, y in Q.zigzag(3)]
HX = anel(6)
DUP = {(0, 1), (2, 3), (4, 5)}
METILAMINA = dict(pts=[(-0.45, 0.25), (0.45, -0.25)], rot={1: "NH2"})
TRIMETIL = dict(pts=[(0, 0), (0, -1), (-0.87, 0.5), (0.87, 0.5)], ligs=[(0, 1), (0, 2), (0, 3)], rot={0: "N"})
ETANAMIDA = dict(pts=Z3f + [(Z3f[1][0], Z3f[1][1] - 1)], ligs=[(0, 1), (1, 2), (1, 3)], duplas={(1, 3)}, rot={2: "NH2", 3: "O"})
ACETICO = dict(pts=Z3f + [(Z3f[1][0], Z3f[1][1] - 1)], ligs=[(0, 1), (1, 2), (1, 3)], duplas={(1, 3)}, rot={2: "OH", 3: "O"})
NITRILA = dict(pts=[(-1, 0), (0, 0), (1, 0)], triplas={(1, 2)}, rot={2: "N"})
PARA = dict(pts=HX + [(0, -2), (0, 2), (0.87, 2.5), (0.87, 3.5), (1.74, 2.0)],
            ligs=ligs_anel(0, 6) + [(0, 6), (3, 7), (7, 8), (8, 9), (8, 10)], duplas=DUP | {(8, 9)}, rot={6: "OH", 7: "NH", 9: "O"})
RX = anel(6, 1, 0)
LIDO = dict(pts=RX + [(1, -1.73), (1, 1.73), (2, 0), (2.87, -0.5), (2.87, -1.5), (3.74, 0), (4.61, -0.5), (4.61, -1.5), (5.48, -2.0), (5.48, 0), (6.35, -0.5)],
            ligs=ligs_anel(0, 6) + [(1, 6), (5, 7), (0, 8), (8, 9), (9, 10), (9, 11), (11, 12), (12, 13), (13, 14), (12, 15), (15, 16)],
            duplas=DUP | {(9, 10)}, rot={8: "NH", 10: "O", 12: "N"})
assert Q.contar("C8H9NO2") == {"C": 8, "H": 9, "N": 1, "O": 2} and len(PARA["pts"]) == 11
assert len([i for i in range(len(LIDO["pts"])) if i not in LIDO["rot"]]) == 14  # C14H22N2O


def amida_halo(c, t, t0, P, iN, iC, iO, r=50, t1=None):
    halo(c, t, t0, [P[iN], P[iC], P[iO]], r, t1=t1)


def hmais(c, t, t0, x0, y0, x1, y1, d=1.0, r=30):
    """o H⁺ voando até o par livre"""
    if t < t0:
        return
    p = ease_io(prog(t, t0, d))
    x, y = lerp(x0, x1, p), lerp(y0, y1, p)
    a = ep(t, t0, 0.3)
    Q.atomo(c, x, y, r, "H", a)
    E.foco(c, t, t0, 0.3, lambda a: E.escreve(c, "+", x + r * 0.7, y - r * 0.5, r * 1.2, "g", COR, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        pilula_em(c, t, C["s01.a"], "cheiro de peixe", 560, 280, 50, TINTA, "i")
        P = mol(c, t, C["s01.a"] + 0.3, TRIMETIL, 560, 560, 150)
        halo(c, t, C["s01.c"], [P[0]], 60)
        pilula_em(c, t, C["s01.b"], "limão: ácido", 1400, 280, 50, TINTA, "i")
        E.foco(c, t, C["s01.b"] + 0.3, 0.5, lambda a: (E.bola(c, 1400, 560, 140 * a, "#E9D84A", a), Q.formula(c, "H^+", 1400, 590, 80, TINTA, a, "center")))
        seta(c, t, C["s01.b"] + 0.8, 1240, 560, 760, 560, TINTA2)
        E.frase(c, t, C["s01.c"], [("tudo por causa de um", "i", 70), ("nitrogênio", "g", 70, Q.cor_el("N"))], W / 2, 900, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 520, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("amina,", "g", 70, COR), ("amida", "g", 70, COR), ("e", "i", 74), ("nitrila", "g", 70, COR)]),
                 (C["s02.c"], [("por que a amina é", "i", 74), ("base", "g", 70)]),
                 (C["s02.d"], [("a amida", "g", 70), ("num remédio", "i", 74)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("das aulas passadas", "i", 76, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("carbonila", "g", 70, COR), ("C=O", "g", 70)], XE, 360, passo=0.12)
    P = mol(c, t, C["s03.b"], ACETICO, 700, 640, 140)
    halo(c, t, C["s03.b"] + 0.4, [P[1], P[2], P[3]], 46, CINZA)
    E.foco(c, t, C["s03.b"] + 0.6, 0.4, lambda a: centro(c, "ácido carboxílico", 700, 880, 50, "i", TINTA2, a))
    E.frase(c, t, C["s03.c"], [("Lewis:", "i", 66), ("N faz 3 ligações", "g", 62)], 1150, 360, passo=0.12)
    Q.lewis(c, t, C["s03.c"] + 0.3, [("N", 0, 0, [90]), ("H", -1, 0.5), ("H", 1, 0.5), ("H", 0, 1.1)], [(0, 1, 1), (0, 2, 1), (0, 3, 1)], 1450, 600, escala=130, size=100,
            tp=C["s03.d"])
    E.frase(c, t, C["s03.d"], [("e fica com um", "i", 60), ("par livre", "g", 60, Q.ELETRON)], 1150, 960, passo=0.12)


# ---------------- amina ----------------
def b_amina(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("amônia,", "i", 70)], XE, 220, passo=0.12)
        Q.formula_em(c, t, C["s04.a"] + 0.3, "NH3", XE + 290, 220, 76)
        Q.lewis(c, t, C["s04.a"] + 0.3, [("N", 0, 0, [90]), ("H", -1, 0.5), ("H", 1, 0.5), ("H", 0, 1.1)], [(0, 1, 1), (0, 2, 1), (0, 3, 1)], 600, 520, escala=130, size=90)
        seta(c, t, C["s04.b"], 860, 560, 1080, 560)
        E.foco(c, t, C["s04.b"], 0.4, lambda a: centro(c, "troque um H por C", 970, 500, 44, "i", TINTA2, a))
        Q.lewis(c, t, C["s04.b"] + 0.5, [("N", 0, 0, [90]), ("C", -1.1, 0.5), ("H", 1, 0.5), ("H", 0, 1.1)], [(0, 1, 1), (0, 2, 1), (0, 3, 1)], 1450, 520, escala=130, size=90)
        halo(c, t, C["s04.c"], [(1450, 520)], 60)
        pilula_em(c, t, C["s04.c"] + 0.3, "amina", 1450, 330, 60, E.COR)
        Q.formula_em(c, t, C["s04.d"], "CH3–NH2", XE, 840, 100, cores={"N": Q.cor_el("N")})
        nome(c, t, C["s04.e"], [("met", TINTA, "1 C"), ("il", TINTA, None), ("amina", COR, "função")], XE + 600, 840, 100, 0.3)
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], ps("dá para trocar mais de um H", "i", 66), XE, 220, passo=0.1)
        P = mol(c, t, C["s05.b"], TRIMETIL, 1350, 560, 160)
        halo(c, t, C["s05.b"] + 0.4, [P[0]], 60)
        for k, i in enumerate((1, 2, 3)):
            anelc(c, t, C["s05.b"] + 0.6 + 0.15 * k, P, i, 30)
        E.frase(c, t, C["s05.b"], [("3 grupos CH3", "g", 62), ("no N: nenhum H", "i", 62)], XE, 400, passo=0.12)
        nome(c, t, C["s05.c"], [("tri", TINTA2, "três"), ("metil", TINTA, None), ("amina", COR, None)], XE, 640, 110, 0.3)
        pilula_esq(c, t, C["s05.c"] + 1.2, "o cheiro de peixe", XE, 840, 50, TINTA, "b")
        return
    # s06: por que é base
    E.frase(c, t, C["s06.a"], [("por que a amina é", "i", 70), ("base?", "g", 70, COR)], XE, 220, passo=0.12)
    E.frase(c, t, C["s06.b"], [("base:", "g", 62), ("captura o", "i", 64)], XE, 360, passo=0.12)
    Q.formula_em(c, t, C["s06.b"] + 0.5, "H^+", XE + 440, 360, 70, cores={"H": E.COR})
    E.foco(c, t, C["s06.b"] + 1.0, 0.4, lambda a: E.escreve(c, "o cátion hidrogênio", XE, 440, 48, "i", TINTA2, a))
    Q.lewis(c, t, C["s06"], [("N", 0, 0, [90]), ("C", -1.1, 0.5), ("C", 1.1, 0.5), ("C", 0, 1.2)], [(0, 1, 1), (0, 2, 1), (0, 3, 1)], 1350, 640, escala=130, size=100)
    E.foco(c, t, C["s06.c"], 0.4, lambda a: c.drawCircle(1350, 560, 48, M.paint(Q.ELETRON, a, stroke=5)))
    hmais(c, t, C["s06.c"] + 0.3, 1700, 260, 1350, 470, 1.4)
    E.frase(c, t, C["s06.c"], [("o", "i", 64), ("par livre", "g", 62, Q.ELETRON), ("agarra o cátion", "i", 64)], XE, 600, passo=0.12)
    E.frase(c, t, C["s06.d"], ps("é assim que reage com o ácido do limão", "i", 56, TINTA2), XE, 760, passo=0.08)
    pilula_esq(c, t, C["s06.e"], "ácidos e bases: aula própria", XE, 900, 46, TINTA2, "b")


# ---------------- amida e nitrila ----------------
def b_amida(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], [("no ácido, troque o", "i", 66), ("OH", "g", 62, Q.cor_el("O")), ("por", "i", 66)], XE, 220, passo=0.1)
        Q.formula_em(c, t, C["s07.a"] + 1.2, "NH2", XE + 660, 220, 66, cores={"N": Q.cor_el("N")})
        if t < C["s07.a"] + 1.0:
            mol(c, t, C["s07"], ACETICO, 1400, 560, 170)
        else:
            P = mol(c, t, C["s07.a"] + 1.0, ETANAMIDA, 1400, 560, 170)
            amida_halo(c, t, C["s07.b"], P, 2, 1, 3, 56)
        E.frase(c, t, C["s07.b"], ps("o N colado na carbonila", "i", 62), XE, 360, passo=0.1)
        E.frase(c, t, C["s07.c"], [("amida", "g", 120, COR)], XE, 560)
        cond(c, t, C["s07.d"], ["CH3", "CO", "NH2"], XE, 760, 90, cores={2: Q.cor_el("N")})
        nome(c, t, C["s07.d"] + 0.6, [("etan", TINTA, None), ("amida", COR, None)], XE, 920, 90, 0.3)
        return
    E.frase(c, t, C["s08.a"], [("nitrila:", "g", 80, COR), ("na ponta da cadeia", "i", 70)], XE, 220, passo=0.12)
    P = mol(c, t, C["s08.a"] + 0.3, NITRILA, 1200, 520, 200)
    halo(c, t, C["s08.a"] + 0.8, [P[1], P[2]], 60)
    E.frase(c, t, C["s08.a"] + 0.5, ps("carbono em tripla com o nitrogênio", "i", 60), XE, 340, passo=0.1)
    nome(c, t, C["s08.b"], [("etano", TINTA, None), ("nitrila", COR, None)], XE, 800, 110, 0.3)
    pilula_esq(c, t, C["s08.b"] + 1.0, "um solvente de laboratório", XE, 950, 46, TINTA, "b")


# ---------------- o remédio ----------------
PX_, PY_, PE_ = 1400, 500, 95


def b_remedio(c, t, C, b):
    P = mol(c, t, C["s09.b"], PARA, PX_, PY_, PE_)
    E.frase(c, t, C["s09.a"], ps("a amida aparece em muito remédio", "i", 66), XE, 220, passo=0.1)
    E.frase(c, t, C["s09.b"], [("paracetamol", "g", 80, COR)], XE, 360)
    E.foco(c, t, C["s09.b"] + 0.8, 0.4, lambda a: E.escreve(c, "para dor e febre", XE, 440, 50, "i", TINTA2, a))
    anelc(c, t, C["s09.c"], P, 7, 44, Q.cor_el("N"))
    E.frase(c, t, C["s09.c"], ps("procure o nitrogênio", "i", 60), XE, 560, passo=0.1)
    anelc(c, t, C["s09.d"], P, 8, 26)
    E.frase(c, t, C["s09.d"], ps("colado num C com dupla com O", "i", 56), XE, 650, passo=0.08)
    amida_halo(c, t, C["s09.e"], P, 7, 8, 9, 46)
    pilula_em(c, t, C["s09.e"] + 0.3, "amida", PX_ + 300, PY_ + 2.9 * PE_, 54, E.COR)
    halo(c, t, C["s09.f"], [P[6]], 46, CINZA)
    pilula_em(c, t, C["s09.f"] + 0.3, "fenol", PX_ + 200, PY_ - 2.0 * PE_, 50, TINTA2)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s10.a"], ps("todo N é amina?", "i", 70), XE + 450, 190, passo=0.12)
    P = mol(c, t, C["s10"], PARA, PX_, PY_, PE_)

    def errado():
        halo(c, t, C["s10.a"] + 0.4, [P[7]], 50, ERRADO)
        E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "amina?", XE, 460, 100, "g", ERRADO, a))
        if t >= C["s10.b"] + 1.4:
            E.risco(c, XE - 10, 480, XE + 360, 400, t, C["s10.b"] + 1.4, largura=10)
    E.saida(c, t, C["s10.c"] + 0.3, errado)
    E.frase(c, t, C["s10.b"], ps("N com um H e um C do anel...", "i", 56, TINTA2), XE, 600, passo=0.08)
    anelc(c, t, C["s10.c"], P, 8, 26)
    halo(c, t, C["s10.c"] + 0.2, [P[8], P[9]], 44)
    E.frase(c, t, C["s10.c"], ps("...mas o outro vizinho é a carbonila", "i", 56), XE, 700, passo=0.08)
    E.frase(c, t, C["s10.d"], [("N + carbonila", "g", 66), ("=", "g", 66, TINTA2), ("amida", "g", 70, COR)], XE, 880, passo=0.12)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], [("o atalho:", "i", 70, CLARO), ("os carbonos vizinhos do N", "g", 66, BR)], W / 2, 180, "center", 0.12)
        linhas = (("s11.b", ETANAMIDA, (2, 1, 3), "amida", "tem dupla com O?"), ("s11.c", NITRILA, (2, 1), "nitrila", "tripla com o N?"),
                  ("s11.d", METILAMINA, (1,), "amina", "só simples, sem carbonila?"))
        for k, (key, M_, ih, fn, perg) in enumerate(linhas):
            y = 400 + k * 230
            Pk = mol(c, t, C[key], M_, 420, y, 90 if k == 0 else 100, escuro=True, d=0.5)
            halo(c, t, C[key] + 0.3, [Pk[i] for i in ih], 40)
            E.foco(c, t, C[key] + 0.2, 0.4, lambda a, perg=perg, y=y: E.escreve(c, perg, 760, y + 20, 56, "i", CLARO, a))
            pilula_em(c, t, C[key] + 0.6, fn, 1650, y, 60, E.COR)
        return
    E.frase(c, t, C["s12.a"], ps("as três funções só mudam o que está preso ao N", "i", 60, CLARO), XE, 300, passo=0.08)
    E.frase(c, t, C["s12.b"], [("cai em prova:", "g", 66, BR), ("a amida quase não é base", "i", 66, CLARO)], XE, 520, passo=0.12)
    pilula_em(c, t, C["s12.c"], "por quê: outra aula", W / 2, 720, 50, TINTA2)


# ---------------- questão ----------------
LX, LY, LE = 760, 560, 105


def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 180)
    mol(c, t, C["s13.a"] - 0.3, LIDO, LX, LY, LE)
    E.frase(c, t, C["s13.a"], [("lidocaína,", "g", 62, COR), ("anestésico usado pelo dentista", "i", 56)], XE, 300, passo=0.1)
    E.frase(c, t, C["s13.b"], ps("dois nitrogênios:", "i", 62), XE, 880, passo=0.1)
    E.frase(c, t, C["s13.c"], ps("qual é amina e qual é amida?", "i", 62), XE, 980, passo=0.1)
    if t >= C["s14"]:
        E.relogio(c, t, C["s14.a"], cx=1650, cy=830, r=80)


def b_resposta(c, t, C, b):
    P = mol(c, t, C["s15"] - 0.4, LIDO, LX, LY, LE)
    E.frase(c, t, C["s15"] - 0.4, [("lidocaína", "g", 62, COR)], XE, 300)
    anelc(c, t, C["s15.a"], P, 9, 26)
    amida_halo(c, t, C["s15.a"] + 0.3, P, 8, 9, 10, 44)
    pilula_em(c, t, C["s15.b"], "amida", P[8][0], P[8][1] + 110, 54, E.COR)
    for k, i in enumerate((11, 13, 15)):
        anelc(c, t, C["s15.c"] + 0.15 * k, P, i, 24)
    halo(c, t, C["s15.c"] + 0.5, [P[12]], 46)
    pilula_em(c, t, C["s15.d"], "amina", P[12][0] + 40, P[12][1] + 170, 54, E.COR)
    E.frase(c, t, C["s15.c"], ps("só simples, 3 carbonos, sem carbonila", "i", 54, TINTA2), XE, 900, passo=0.08)
    E.foco(c, t, C["s15.d"] + 0.6, 0.4, lambda a: E.escreve(c, "como a do peixe: nenhum H no N", XE, 990, 50, "i", COR, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s16.a"], [("N só com simples, sem carbonila:", "i", 62), ("amina", "g", 66, COR), ("(base)", "g", 58, TINTA2)], XE, 380, passo=0.1)
        E.frase(c, t, C["s16.b"], [("N colado na carbonila:", "i", 62), ("amida", "g", 66, COR)], XE, 540, passo=0.1)
        E.frase(c, t, C["s16.c"], [("C em tripla com N:", "i", 62), ("nitrila", "g", 66, COR)], XE, 700, passo=0.1)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s17.a"], [("haletos:", "g", 96, COR), ("cloro e flúor", "i", 90)], XE, 400, passo=0.14)
    E.frase(c, t, C["s17.b"], [("CFC", "g", 80), ("e a camada de ozônio", "i", 76)], XE, 540, passo=0.12)
    E.frase(c, t, C["s17.c"], [("DDT", "g", 80), ("que se acumula", "i", 76)], XE, 670, passo=0.12)
    E.foco(c, t, C["s17.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s17.d"] + 0.2, 0.4))
    E.frase(c, t, C["s17.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, amina=b_amina, amida=b_amida, remedio=b_remedio, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
