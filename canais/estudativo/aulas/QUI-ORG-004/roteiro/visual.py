"""Visual — Estudativo · QUI-ORG-004: nomear cadeias ramificadas.
Segue a linguagem da Química (QUI-MIS-001) e da Orgânica (QUI-ORG-001): a CADEIA PRINCIPAL ganha o realce turquesa (realca_fila)
e os galhos ficam em tinta; a numeração oficial é a bolinha numerada do vértice; o nome sai em peças com nome().
Leitura errada = realce vermelho + nome riscado.
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
ARQUIVO_FINAL = "estudativo_QUI-ORG-004_nomear_cadeias_ramificadas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("principal", "passos", "dimetil", "erro", "atalho", "questao", "fim"))

Z4, Z5 = Q.zigzag(4), Q.zigzag(5)
DMB = dict(pts=Z4 + [(Z4[1][0], Z4[1][1] + 1), (Z4[2][0], Z4[2][1] - 1)], ligs=[(0, 1), (1, 2), (2, 3), (1, 4), (2, 5)])
MP2 = dict(pts=Z5 + [(Z5[1][0], Z5[1][1] + 1)], ligs=[(0, 1), (1, 2), (2, 3), (3, 4), (1, 5)])
MP3 = dict(pts=Z4 + [(Z4[1][0], Z4[1][1] + 1), (Z4[1][0] + 0.87, Z4[1][1] + 1.5)], ligs=[(0, 1), (1, 2), (2, 3), (1, 4), (4, 5)])
ISO = dict(pts=Z5 + [(Z5[1][0] - 0.5, Z5[1][1] + 0.87), (Z5[1][0] + 0.5, Z5[1][1] + 0.87), (Z5[3][0], Z5[3][1] + 1)],
           ligs=[(0, 1), (1, 2), (2, 3), (3, 4), (1, 5), (1, 6), (3, 7)])
assert len(DMB["pts"]) == 6 and len(ISO["pts"]) == 8
assert sorted([2, 2, 4]) < sorted([2, 4, 4])


def numera(c, t, t0, P, fila, passo=0.15, cor=None, r=30):
    for k, i in enumerate(fila):
        E.foco(c, t, t0 + k * passo, 0.3, lambda a, i=i, k=k: (E.bola(c, P[i][0], P[i][1], r, cor, a), centro(c, str(k + 1), P[i][0], P[i][1] + r * 0.45, r * 1.25, "g", E.SOBRE, a)))


# ---------------- gancho ----------------
GX, GY, GE = 1350, 520, 180


def b_gancho(c, t, C, b):
    def um():
        P = mol(c, t, C["s01.a"], DMB, GX, GY, GE)
        Q.bastao(c, t, C["s01.a"] + 0.6, DMB["pts"], GX, GY, GE, ligacoes=DMB["ligs"], d=0.01, numeros=C["s01.a"] + 0.8, passo_n=0.15)
        E.frase(c, t, C["s01.a"], [("6", "g", 90, COR), ("carbonos", "i", 90)], XE, 260, passo=0.12)
        E.frase(c, t, C["s01.a"] + 1.6, [("mas o nome diz", "i", 70), ("butano", "g", 70), ("(4)", "g", 64, TINTA2)], XE, 380, passo=0.12)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.escreve(c, "2,3-dimetilbutano", XE, 860, 110, "g", COR, a))
        E.frase(c, t, C["s01.c"], ps("onde estão os outros carbonos?", "i", 66, TINTA2), XE, 990, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 520, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 240, passo=0.14)
    lista(c, t, [(C["s02.b"], [("achar a", "i", 74), ("cadeia principal", "g", 70, COR)]),
                 (C["s02.c"], [("numerar", "g", 70), ("do lado certo", "i", 74)]),
                 (C["s02.d"], [("montar", "g", 70), ("o nome inteiro", "i", 74)]),
                 (C["s02.e"], [("atalho", "g", 70, COR), ("da numeração", "i", 74)])], XE, 410, 160)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula passada", "i", 76, TINTA2), XE, 200, passo=0.12)
    for k, s in enumerate(("met", "et", "prop", "but", "pent", "hex")):
        E.foco(c, t, C["s03.a"] + 0.3 * k, 0.4, lambda a, s=s, k=k: (E.escreve(c, str(k + 1), XE + (k % 3) * 360, 380 + (k // 3) * 140, 76, "g", TINTA2, a),
                                                                     E.escreve(c, s, XE + 80 + (k % 3) * 360, 380 + (k // 3) * 140, 76, "g", COR, a)))
    E.frase(c, t, C["s03.b"], [("an", "g", 76), ("=", "g", 70, TINTA2), ("só simples", "i", 76)], XE, 720, passo=0.12)
    E.frase(c, t, C["s03.c"], ps("numere pela ponta mais perto", "i", 66), XE, 860, passo=0.1)


# ---------------- cadeia principal e galhos ----------------
def b_principal(c, t, C, b):
    P = mol(c, t, C["s04"], MP3, 1350, 470, 170)
    E.frase(c, t, C["s04.a"], [("o nome nasce da", "i", 70), ("cadeia principal", "g", 70, COR)], XE, 200, passo=0.12)
    if t < C["s05"]:
        E.frase(c, t, C["s04.b"], ps("a maior fila de carbonos seguidos", "i", 62), XE, 320, passo=0.1)
        realca_fila(c, t, C["s04.b"] + 0.8, P, [5, 4, 1, 2, 3], passo=0.25)
        E.frase(c, t, C["s04.c"], [("ela pode fazer", "i", 62), ("curva", "g", 60, COR)], XE, 420, passo=0.1)
        numera(c, t, C["s04.b"] + 2.2, P, [5, 4, 1, 2, 3], 0.2)
        return
    realca_fila(c, t, C["s05"] - 1, P, [5, 4, 1, 2, 3], passo=0)
    anelc(c, t, C["s05.a"], P, 0, 34, CINZA)
    E.foco(c, t, C["s05.a"] + 0.3, 0.4, lambda a: centro(c, "galho", P[0][0], P[0][1] - 60, 50, "i", TINTA, a))
    E.frase(c, t, C["s05.a"], [("o que fica de fora:", "i", 62), ("galho", "g", 62)], XE, 330, passo=0.1)
    E.frase(c, t, C["s05.a"] + 1.4, ps("(ou radical)", "i", 52, TINTA2), XE + 640, 330, passo=0.1)
    E.frase(c, t, C["s05.b"], [("prefixo", "g", 62, COR), ("+", "g", 62, TINTA2), ("il", "g", 70)], XE, 460, passo=0.12)
    for k, (key, s, n) in enumerate((("s05.c", "metil", 1), ("s05.d", "etil", 2))):
        y = 760 + k * 170
        E.foco(c, t, C[key], 0.4, lambda a, s=s, y=y: E.escreve(c, s, XE, y, 100, "g", COR, a))
        Q.bastao(c, t, C[key] + 0.2, [(0, 0), (0.87, -0.5), (1.74, 0)][:n + 1], XE + 460, y - 36, 110, d=0.4)
        E.foco(c, t, C[key] + 0.4, 0.4, lambda a, n=n, y=y: E.escreve(c, f"{n} carbono" + ("s" if n > 1 else ""), XE + 720, y - 10, 50, "i", TINTA2, a))
        E.foco(c, t, C[key] + 0.2, 0.4, lambda a, y=y: (M.line(c, XE + 400, y - 36, XE + 440, y - 36, TINTA2, a, 4), centro(c, "•", XE + 395, y - 18, 50, "g", TINTA2, a)))


# ---------------- quatro passos ----------------
PX, PY, PE = 1350, 430, 170


def b_passos(c, t, C, b):
    P = mol(c, t, C["s06"], MP2, PX, PY, PE)
    passos = (("s06.a", "maior fila: 5 C", "pent"), ("s06.b", "de fora: 1 C", "metil"), ("s07.a", "numere pelo galho", "no 2"), ("s07.c", "monte o nome", ""))
    for k, (key, s, r) in enumerate(passos):
        y = 220 + k * 120
        E.foco(c, t, C[key], 0.4, lambda a, k=k, y=y: (E.bola(c, XE + 36, y - 22, 36, a=a), centro(c, str(k + 1), XE + 36, y - 4, 44, "g", E.SOBRE, a)))
        E.frase(c, t, C[key] + 0.1, [(s, "i", 56)], XE + 100, y)
    realca_fila(c, t, C["s06.a"] + 0.6, P, [0, 1, 2, 3, 4])
    anelc(c, t, C["s06.b"] + 0.4, P, 5, 34, CINZA)
    if t >= C["s07.a"]:
        numera(c, t, C["s07.a"] + 0.4, P, [0, 1, 2, 3, 4])
    anelc(c, t, C["s07.b"], P, 1, 44)
    nome(c, t, C["s07.c"] + 0.8, [("2-", TINTA2, "posição"), ("metil", COR, "galho"), ("pentano", TINTA, "cadeia")], XE, 860, 130,
         passo=max(0.3, (C["s07.e"] - C["s07.c"] - 0.8) / 2.5))


# ---------------- o 2,3-dimetilbutano ----------------
def b_dimetil(c, t, C, b):
    if t < C["s10"]:
        P = mol(c, t, C["s08"] - 0.3, DMB, PX + 100, PY + 20, PE)
        E.frase(c, t, C["s08"], ps("de volta ao começo", "i", 64, TINTA2), XE, 200, passo=0.1)
        realca_fila(c, t, C["s08.a"], P, [0, 1, 2, 3])
        E.frase(c, t, C["s08.a"], [("maior fila:", "i", 60), ("4 C, but", "g", 58, COR)], XE, 320, passo=0.1)
        anelc(c, t, C["s08.b"], P, 4, 34, CINZA); anelc(c, t, C["s08.b"] + 0.2, P, 5, 34, CINZA)
        E.frase(c, t, C["s08.b"], [("2 galhos de 1 C:", "i", 60), ("metil", "g", 58, COR)], XE, 420, passo=0.1)
        if t >= C["s08.c"]:
            numera(c, t, C["s08.c"], P, [0, 1, 2, 3])
            E.frase(c, t, C["s08.c"] + 0.6, ps("de qualquer ponta: no 2 e no 3", "i", 56, TINTA2), XE, 520, passo=0.1)
        if t >= C["s09"]:
            E.frase(c, t, C["s09.a"], [("di", "g", 66, COR), ("= 2,", "g", 60, TINTA2), ("tri", "g", 66, COR), ("= 3", "g", 60, TINTA2)], XE, 680, passo=0.12)
            E.frase(c, t, C["s09.b"], ps("posições na frente, com vírgula", "i", 54, TINTA2), XE + 560, 680, passo=0.08)
            nome(c, t, C["s09.c"], [("2,3-", TINTA2, "posições"), ("di", COR, "dois"), ("metil", COR, "galho"), ("butano", TINTA, "cadeia")], XE, 880, 120, 0.3)
            pilula_em(c, t, C["s09.d"], "os outros 2 C estão nos galhos", 1450, 1000, 44, TINTA, "b")
        return
    E.frase(c, t, C["s10.a"], ps("e se os galhos forem diferentes?", "i", 70), XE, 220, passo=0.12)
    E.frase(c, t, C["s10.b"], [("ordem", "g", 76, COR), ("alfabética:", "i", 80)], XE, 400, passo=0.12)
    E.foco(c, t, C["s10.b"] + 1.0, 0.4, lambda a: (E.escreve(c, "e", XE, 560, 120, "g", COR, a), E.escreve(c, "til", XE + E.larg("e", "g", 120), 560, 120, "g", TINTA, a)))
    E.foco(c, t, C["s10.b"] + 1.3, 0.4, lambda a: (E.escreve(c, "antes de", XE + 330, 550, 60, "i", TINTA2, a), E.escreve(c, "m", XE + 600, 560, 120, "g", COR, a),
                                                   E.escreve(c, "etil", XE + 600 + E.larg("m", "g", 120), 560, 120, "g", TINTA, a)))
    E.foco(c, t, C["s10.b"] + 1.8, 0.4, lambda a: E.escreve(c, "3-etil-2-metilpentano", XE, 760, 76, "g", TINTA2, a))
    E.frase(c, t, C["s10.c"], [("di", "g", 64, ERRADO), ("e", "i", 66), ("tri", "g", 64, ERRADO)] + ps("não contam na ordem", "i", 66), XE, 920, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("a fila mais óbvia", "i", 70), XE + 450, 190, passo=0.12)
    P = mol(c, t, C["s11"], MP3, 1350, 480, 180)

    def errado():
        realca_fila(c, t, C["s11.b"], P, [0, 1, 2, 3], ERRADO)
        anelc(c, t, C["s11.b"] + 0.8, P, 4, 30, ERRADO); anelc(c, t, C["s11.b"] + 0.9, P, 5, 30, ERRADO)
        E.foco(c, t, C["s11.c"], 0.4, lambda a: E.escreve(c, "2-etilbutano", XE, 820, 100, "g", ERRADO, a))
        if t >= C["s11.c"] + 0.9:
            E.risco(c, XE - 10, 840, XE + 640, 760, t, C["s11.c"] + 0.9, largura=10)
    E.saida(c, t, C["s12.a"] + 0.2, errado)
    if t >= C["s12.a"]:
        realca_fila(c, t, C["s12.a"], P, [5, 4, 1, 2, 3])
        numera(c, t, C["s12.a"] + 0.6, P, [5, 4, 1, 2, 3], 0.15)
        anelc(c, t, C["s12.b"], P, 0, 34, CINZA)
        nome(c, t, C["s12.c"], [("3-", TINTA2, None), ("metil", COR, None), ("pentano", TINTA, None)], XE, 820, 110, 0.25)
        E.foco(c, t, C["s12.c"] + 0.8, 0.4, lambda a: E.selo(c, XE + 900, 780, 46, True, a))
        pilula_em(c, t, C["s12.d"], "etil no carbono 2 esconde uma cadeia maior", W / 2, 990, 46, E.COR)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        def s13():
            E.frase(c, t, C["s13.a"], ps("o atalho da numeração", "i", 70, CLARO), W / 2, 170, "center", 0.12)
            E.frase(c, t, C["s13.b"], [("ache o", "i", 66, CLARO), ("galho mais perto", "g", 66, BR), ("de uma ponta", "i", 66, CLARO)], XE, 330, passo=0.12)
            E.frase(c, t, C["s13.c"], [("essa ponta", "i", 66, CLARO), ("= carbono 1", "g", 66, E.CLARO)], XE, 440, passo=0.12)
            P = mol(c, t, C["s13.a"] + 0.4, MP2, 1500, 560, 110, escuro=True)
            numera(c, t, C["s13.c"] + 0.3, P, [0, 1, 2, 3, 4], 0.1, r=24)
            E.frase(c, t, C["s13.d"], [("empate?", "g", 66, BR), ("olhe o galho seguinte", "i", 66, CLARO)], XE, 650, passo=0.12)
            E.frase(c, t, C["s13.d"] + 1.6, ps("2 galhos no mesmo carbono contam 2 vezes", "i", 56, CLARO), XE, 750, passo=0.08)
            E.frase(c, t, C["s13.e"], [("vence quem chega", "i", 66, CLARO), ("mais cedo", "g", 66, E.CLARO)], XE, 880, passo=0.12)
        E.saida(c, t, C["s14"] - 0.1, s13)
        return
    E.frase(c, t, C["s14.a"], ps("a regra pede os menores números:", "i", 66, CLARO), XE, 260, passo=0.1)
    E.frase(c, t, C["s14.a"] + 1.4, [("decide o 1º galho", "g", 70, BR), ("em que as pontas diferem", "i", 66, CLARO)], XE, 380, passo=0.12)
    E.frase(c, t, C["s14.b"], [("não vale", "g", 64, ERRADO), ("com dupla ou tripla:", "i", 66, CLARO)], XE, 620, passo=0.12)
    E.frase(c, t, C["s14.c"], ps("a dupla tem preferência (outra aula)", "i", 62, CLARO), XE, 730, passo=0.1)


# ---------------- questão ----------------
QX, QY, QE = 1350, 520, 160


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    mol(c, t, C["s15.a"] - 0.2, ISO, QX, QY, QE)
    E.frase(c, t, C["s15.a"], [("o", "i", 64), ("iso-octano", "g", 62, COR)], XE, 340, passo=0.1)
    E.frase(c, t, C["s15.a"] + 1.2, ps("a nota 100 da octanagem", "i", 54, TINTA2), XE, 430, passo=0.08)
    E.frase(c, t, C["s15.b"], ps("qual é o", "i", 72) + [("nome oficial?", "g", 68, COR)], XE, 820, passo=0.12)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1600, cy=820, r=100)


def b_resposta(c, t, C, b):
    P = mol(c, t, C["s17"] - 0.5, ISO, QX, 440, QE)
    if t < C["s18"]:
        realca_fila(c, t, C["s17.a"], P, [0, 1, 2, 3, 4])
        E.frase(c, t, C["s17.a"], [("maior fila: 5 C,", "i", 56), ("pentano", "g", 56, COR)], XE, 200, passo=0.1)
        for k, i in enumerate((5, 6, 7)):
            anelc(c, t, C["s17.b"] + 0.15 * k, P, i, 30, CINZA)
        E.frase(c, t, C["s17.b"], [("3 galhos de 1 C:", "i", 56), ("trimetil", "g", 56, COR)], XE, 290, passo=0.1)
        E.frase(c, t, C["s17.c"], [("empate:", "g", 56), ("as duas pontas chegam a um galho no 2", "i", 52)], XE, 760, passo=0.08)
        E.frase(c, t, C["s17.d"], [("esquerda:", "g", 54, COR), ("2, 2, 4", "g", 54)], XE, 860, passo=0.1)
        E.frase(c, t, C["s17.e"], [("direita:", "g", 54, TINTA2), ("2, 4, 4", "g", 54, TINTA2)], XE + 600, 860, passo=0.1)
        if t >= C["s17.d"]:
            numera(c, t, C["s17.d"], P, [0, 1, 2, 3, 4], 0.12)
        return
    realca_fila(c, t, C["s18"] - 1, P, [0, 1, 2, 3, 4], passo=0)
    numera(c, t, C["s18"] - 1, P, [0, 1, 2, 3, 4], 0)
    nome(c, t, C["s18.a"], [("2,2,4-", TINTA2, "posições"), ("tri", COR, "três"), ("metil", COR, "galho"), ("pentano", TINTA, "cadeia")], XE, 800, 110, 0.3)
    E.frase(c, t, C["s18.b"], ps("o 2 se repete: dois galhos no mesmo carbono", "i", 50, TINTA2), XE, 960, passo=0.08)
    E.foco(c, t, C["s18.c"], 0.4, lambda a: E.formula(c, "2,4,4", 1500, 960, 60, "g", ERRADO, a))
    if t >= C["s18.d"]:
        E.risco(c, 1490, 975, 1680, 920, t, C["s18.d"], largura=8)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s19.a", "ache a maior fila"), ("s19.b", "galhos com il"), ("s19.c", "numere pelo galho mais perto"), ("s19.d", "junte tudo, a cadeia no fim"))
        lista(c, t, [(C[k], [(s, "g", 64)]) for k, s in itens], XE, 360, 150)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("prática:", "g", 96, COR)], XE, 400)
    E.frase(c, t, C["s20.a"] + 0.5, [("combustíveis", "i", 84), ("e", "i", 84), ("remédios", "i", 84)], XE, 520, passo=0.14)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.b"] + 0.2, 0.4))
    E.frase(c, t, C["s20.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, principal=b_principal, passos=b_passos, dimetil=b_dimetil, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
