"""Visual — Estudativo · QUI-ORG-007: aldeído e cetona.
Segue a linguagem da Química (QUI-MIS-001), da Orgânica (QUI-ORG-001) e do módulo Funções (QUI-ORG-006): a CARBONILA ganha o
halo() que cobre o carbono e o oxigênio juntos; os vizinhos do carbono da carbonila ganham anelc(), e é isso que separa
aldeído (vizinho H, na ponta) de cetona (carbono dos dois lados).
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
ARQUIVO_FINAL = "estudativo_QUI-ORG-007_aldeido_cetona.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("carbonila", "cetona", "erro", "atalho", "questao", "fim"))


def zz(n, vira=False):
    return [(x, -y) for x, y in Q.zigzag(n)] if vira else Q.zigzag(n)


def cetona_m(n, i):
    """cadeia de n carbonos com a carbonila no vértice i (para cima)"""
    Z = zz(n, vira=(i % 2 == 1))
    return dict(pts=Z + [(Z[i][0], Z[i][1] - 1.0)], ligs=[(k, k + 1) for k in range(n - 1)] + [(i, n)], duplas={(i, n)}, rot={n: "O"})


def aldeido_m(n):
    Z = zz(n + 1)
    return dict(pts=Z, rot={n: "O"}, duplas={(n - 1, n)})


ETANAL, PROPANAL, BUTANAL = aldeido_m(2), aldeido_m(3), aldeido_m(4)
PROPANONA, BUTANONA = cetona_m(3, 1), cetona_m(4, 1)
P2ONA, P3ONA = cetona_m(5, 1), cetona_m(5, 2)
assert Q.contar("CH3CH2CHO") == Q.contar("CH3COCH3") == {"C": 3, "H": 6, "O": 1}
assert Q.contar("CH3CH2CH2CHO") == Q.contar("CH3COCH2CH3") == {"C": 4, "H": 8, "O": 1}


def carbonila(c, t, t0, P, ic, io, r=58, t1=None, cor=None):
    halo(c, t, t0, [P[ic], P[io], ((P[ic][0] + P[io][0]) / 2, (P[ic][1] + P[io][1]) / 2)], r, cor, t1=t1)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        pilula_em(c, t, C["s01.a"], "formol: conserva peças", 560, 280, 48, TINTA, "i")
        Q.lewis(c, t, C["s01.a"] + 0.3, [("C", 0, 0), ("O", 1.2, 0), ("H", -0.8, -0.6), ("H", -0.8, 0.6)], [(0, 1, 2), (0, 2, 1), (0, 3, 1)], 500, 560, escala=140, size=96)
        pilula_em(c, t, C["s01.b"], "acetona: tira esmalte", 1400, 280, 48, TINTA, "i")
        P = mol(c, t, C["s01.b"] + 0.3, PROPANONA, 1400, 620, 150)
        halo(c, t, C["s01.c"], [(500, 560), (668, 560), (584, 560)], 60)
        carbonila(c, t, C["s01.c"] + 0.3, P, 1, 3)
        E.frase(c, t, C["s01.c"] + 0.4, [("C=O", "g", 70, COR)] + ps("o mesmo pedaço", "i", 70), W / 2, 880, "center", 0.12)
        E.frase(c, t, C["s01.d"], ps("só muda onde ele está", "i", 70, TINTA2), W / 2, 990, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 520, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("aldeído", "g", 70, COR), ("ou", "i", 74), ("cetona?", "g", 70, COR)]),
                 (C["s02.c"], [("dar nome ao", "i", 74), ("etanal", "g", 70)]),
                 (C["s02.d"], [("e à", "i", 74), ("propanona", "g", 70)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula passada", "i", 76, TINTA2), XE, 200, passo=0.12)
    for k, (fn, M_, io) in enumerate((("álcool", dict(pts=Q.zigzag(3), rot={2: "OH"}), 2), ("éter", dict(pts=Q.zigzag(4), rot={1: "O"}), 1))):
        cx = 600 + k * 700
        P = mol(c, t, C["s03.a"] + 0.3 * k, M_, cx, 470, 130, d=0.5)
        halo(c, t, C["s03.a"] + 0.5 + 0.3 * k, [P[io]], 50, CINZA)
        pilula_em(c, t, C["s03.a"] + 0.6 + 0.3 * k, fn, cx, 640, 50, TINTA, "g")
    E.frase(c, t, C["s03.b"], [("álcool:", "i", 66), ("ol", "g", 70, COR)], XE, 800, passo=0.12)
    E.frase(c, t, C["s03.c"], [("hoje: o oxigênio numa", "i", 66), ("dupla", "g", 66, COR)], XE, 920, passo=0.12)


# ---------------- carbonila ----------------
def b_carbonila(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("C=O", "g", 90, COR), ("=", "g", 80, TINTA2), ("carbonila", "g", 90, COR)], XE, 260, passo=0.14)
        pts = Q.lewis(c, t, C["s04.a"] + 0.4, [("C", 0, 0), ("O", 1.3, 0, [60, -60])], [(0, 1, 2)], 900, 620, escala=150, size=130)
        halo(c, t, C["s04.b"], [pts[1]], 80)
        E.frase(c, t, C["s04.b"], ps("o O gasta as 2 ligações na dupla", "i", 60), XE, 420, passo=0.1)
        for k, g in enumerate((150, 210)):
            ux, uy = math.cos(math.radians(g)), -math.sin(math.radians(g))
            E.foco(c, t, C["s04.c"] + 0.2 * k, 0.4, lambda a, ux=ux, uy=uy: M.line(c, 900 + ux * 80, 620 + uy * 80, 900 + ux * 180, 620 + uy * 180, E.COR, a, 8))
        E.frase(c, t, C["s04.c"], [("o C fica com", "i", 60), ("2 ligações livres", "g", 58, COR)], XE, 900, passo=0.1)
        return
    # s05/s06: aldeído
    def s05():
        E.frase(c, t, C["s05.a"], ps("carbonila na ponta da cadeia", "i", 66), XE, 220, passo=0.1)
        P = mol(c, t, C["s05.a"] + 0.3, ETANAL, 1400, 470, 170)
        carbonila(c, t, C["s05.a"] + 0.8, P, 1, 2)
        E.foco(c, t, C["s05.b"], 0.4, lambda a: (M.line(c, P[1][0], P[1][1], P[1][0], P[1][1] + 110, E.COR, a, 7), centro(c, "H", P[1][0], P[1][1] + 175, 70, "g", E.COR_TEXTO, a)))
        E.frase(c, t, C["s05.b"], [("uma ligação livre vai para um", "i", 60), ("H", "g", 60, COR)], XE, 330, passo=0.1)
        E.frase(c, t, C["s05.c"], [("aldeído", "g", 120, COR)], XE, 540)
        cond(c, t, C["s05.d"], ["CH3", "CHO"], XE, 720, 110, cores={1: E.COR})
    if t < C["s06"]:
        s05()
        return
    E.frase(c, t, C["s06.a"], [("o", "g", 70, TINTA2), ("do fim vira", "i", 66), ("al", "g", 76, COR)], XE, 220, passo=0.12)
    nome(c, t, C["s06.b"], [("et", TINTA, "2 C"), ("an", TINTA, None), ("al", COR, "aldeído")], XE, 420, 120, 0.3)
    cond(c, t, C["s06.b"] + 0.6, ["CH3", "CHO"], XE + 700, 420, 90, cores={1: E.COR})
    nome(c, t, C["s06.c"], [("met", TINTA, "1 C"), ("an", TINTA, None), ("al", COR, None)], XE, 650, 120, 0.3)
    Q.formula_em(c, t, C["s06.c"] + 0.6, "HCHO", XE + 700, 650, 90)
    pilula_em(c, t, C["s06.d"], "formol = metanal em água", XE + 1250, 625, 44, TINTA, "b")
    E.frase(c, t, C["s06.e"], [("sem número:", "g", 60), ("a carbonila do aldeído está sempre no carbono 1", "i", 56)], XE, 900, passo=0.08)


# ---------------- cetona ----------------
def b_cetona(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("carbonila no meio, entre dois carbonos", "i", 62), XE, 220, passo=0.1)
        P = mol(c, t, C["s07.a"] + 0.3, PROPANONA, 1400, 560, 170)
        carbonila(c, t, C["s07.a"] + 0.8, P, 1, 3)
        anelc(c, t, C["s07.a"] + 1.2, P, 0, 30); anelc(c, t, C["s07.a"] + 1.4, P, 2, 30)
        E.frase(c, t, C["s07.a"] + 1.0, [("cetona", "g", 110, COR)], XE, 400)
        E.frase(c, t, C["s07.b"], [("final", "i", 64), ("ona", "g", 70, COR)], XE, 520, passo=0.12)
        nome(c, t, C["s07.c"], [("prop", TINTA, "3 C"), ("an", TINTA, None), ("ona", COR, "cetona")], XE, 700, 110, 0.3)
        cond(c, t, C["s07.d"], ["CH3", "CO", "CH3"], XE, 880, 80, cores={1: E.COR})
        pilula_em(c, t, C["s07.e"], "a acetona", XE + 720, 855, 46, TINTA, "b")
        if t >= C["s07.f"]:
            def compara():
                Pp = mol(c, t, C["s07.f"], PROPANAL, 1400, 920, 90, d=0.5)
                carbonila(c, t, C["s07.f"] + 0.3, Pp, 2, 3, 40)
                E.foco(c, t, C["s07.f"] + 0.3, 0.4, lambda a: E.escreve(c, "propanal: na ponta", 1580, 960, 44, "i", TINTA2, a))
            compara()
            E.foco(c, t, C["s07.g"], 0.4, lambda a: E.escreve(c, "a posição muda a família", XE, 1020, 48, "i", COR, a))
        return
    E.frase(c, t, C["s08.a"], ps("com 5 carbonos, a carbonila tem mais de um lugar", "i", 60), XE, 220, passo=0.08)
    P2 = mol(c, t, C["s08.b"], P2ONA, 600, 560, 130)
    carbonila(c, t, C["s08.b"] + 0.4, P2, 1, 5, 44)
    nome(c, t, C["s08.b"] + 0.4, [("pentan-", TINTA, None), ("2-", TINTA2, None), ("ona", COR, None)], 600, 820, 84, 0.2, "center")
    P3 = mol(c, t, C["s08.b"] + 1.2, P3ONA, 1350, 560, 130)
    carbonila(c, t, C["s08.b"] + 1.6, P3, 2, 5, 44)
    nome(c, t, C["s08.b"] + 1.6, [("pentan-", TINTA, None), ("3-", TINTA2, None), ("ona", COR, None)], 1350, 820, 84, 0.2, "center")
    if t >= C["s08.c"]:
        Q.bastao(c, t, C["s08.c"], P2ONA["pts"][:5], 600, 560, 130, d=0.01, numeros=C["s08.c"], passo_n=0.12)
    E.frase(c, t, C["s08.c"], ps("numere pela ponta mais perto da carbonila", "i", 56, TINTA2), W / 2, 980, "center", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s09"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s09.a"], ps("CHO não é álcool", "i", 70), XE + 450, 190, passo=0.12)
    Q.formula_em(c, t, C["s09.a"], "CHO", 560, 470, 200, align="center", cores={"O": Q.cor_el("O")})

    def errado():
        E.foco(c, t, C["s09.a"] + 0.8, 0.4, lambda a: E.escreve(c, "álcool?", 300, 640, 80, "g", ERRADO, a))
        if t >= C["s09.a"] + 1.6:
            E.risco(c, 290, 660, 590, 590, t, C["s09.a"] + 1.6, largura=9)
    E.saida(c, t, C["s09.b"], errado)
    Q.lewis(c, t, C["s09.b"], [("C", 0, 0), ("O", 0.9, -0.8), ("H", 0.9, 0.8), ("C", -1.2, 0)], [(0, 1, 2), (0, 2, 1), (0, 3, 1)], 480, 800, escala=120, size=90)
    E.foco(c, t, C["s09.b"] + 0.4, 0.4, lambda a: E.escreve(c, "aldeído: H no carbono", 260, 1010, 50, "i", COR, a))
    halo(c, t, C["s09.c"], [(480 + 0.9 * 120, 800 - 0.8 * 120)], 50)
    Q.lewis(c, t, C["s09.d"], [("C", 0, 0), ("O", 1.1, 0), ("H", 2.2, 0)], [(0, 1, 1), (1, 2, 1)], 1200, 800, escala=120, size=90)
    E.foco(c, t, C["s09.d"] + 0.4, 0.4, lambda a: E.escreve(c, "álcool: H no oxigênio", 1180, 1010, 50, "i", TINTA2, a))
    Q.formula_em(c, t, C["s09.d"], "C–OH", 1330, 470, 160, align="center", cores={"O": Q.cor_el("O")})
    pilula_em(c, t, C["s09.e"], "O sem H: não é álcool", W / 2, 600, 52, E.COR)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], [("o atalho:", "i", 70, CLARO), ("conte os carbonos", "g", 70, BR)], W / 2, 180, "center", 0.12)
        E.frase(c, t, C["s10.b"], [("1 ou 2 C:", "g", 70, BR), ("só aldeído", "g", 70, E.CLARO)], XE, 340, passo=0.12)
        Q.lewis(c, t, C["s10.b"] + 0.6, [("C", 0, 0), ("O", 1.2, 0), ("H", -0.8, -0.6), ("H", -0.8, 0.6)], [(0, 1, 2), (0, 2, 1), (0, 3, 1)], 1100, 330, escala=110, size=80, escuro=True)
        mol(c, t, C["s10.b"] + 0.9, ETANAL, 1550, 320, 110, escuro=True)
        E.frase(c, t, C["s10.c"], ps("a cetona precisa de um carbono de cada lado", "i", 60, CLARO), XE, 560, passo=0.08)
        E.frase(c, t, C["s10.d"], [("a menor cetona tem", "i", 66, CLARO), ("3 C", "g", 70, BR)], XE, 700, passo=0.12)
        P = mol(c, t, C["s10.d"] + 0.4, PROPANONA, 1450, 820, 120, escuro=True)
        carbonila(c, t, C["s10.d"] + 0.8, P, 1, 3, 44)
        return
    E.frase(c, t, C["s11.a"], ps("com 2 C, um lado da carbonila fica sem carbono", "i", 60, CLARO), XE, 220, passo=0.08)
    E.frase(c, t, C["s11.b"], [("3 C ou mais?", "g", 66, BR), ("o atalho não decide", "i", 66, CLARO)], XE, 360, passo=0.12)
    E.frase(c, t, C["s11.c"], ps("olhe os vizinhos do carbono da carbonila:", "i", 60, CLARO), XE, 480, passo=0.08)
    Pa = mol(c, t, C["s11.d"], PROPANAL, 600, 720, 120, escuro=True)
    E.foco(c, t, C["s11.d"] + 0.3, 0.4, lambda a: centro(c, "vizinho H", 600, 900, 54, "g", BR, a))
    pilula_em(c, t, C["s11.d"] + 0.5, "aldeído", 600, 990, 54, E.COR)
    Pc = mol(c, t, C["s11.e"], PROPANONA, 1350, 720, 120, escuro=True)
    E.foco(c, t, C["s11.e"] + 0.3, 0.4, lambda a: centro(c, "C dos dois lados", 1350, 900, 54, "g", BR, a))
    pilula_em(c, t, C["s11.e"] + 0.5, "cetona", 1350, 990, 54, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s12"], ps("hora de testar", "i", 72, COR), XE, 180)
    for k, M_ in enumerate((BUTANAL, BUTANONA)):
        cx = 600 + k * 760
        E.foco(c, t, C["s12.a"] + 0.3 * k, 0.4, lambda a, cx=cx, k=k: (E.bola(c, cx - 300, 330, 36, a=a), centro(c, str(k + 1), cx - 300, 348, 44, "g", E.SOBRE, a)))
        mol(c, t, C["s12.a"] + 0.3 * k, M_, cx, 520, 130, d=0.6)
    Q.formula_em(c, t, C["s12.a"] + 0.6, "C4H8O", W / 2, 760, 90, align="center")
    E.frase(c, t, C["s12.b"], ps("qual é o aldeído e qual é a cetona?", "i", 60), XE, 900, passo=0.08)
    E.frase(c, t, C["s12.c"], ps("e o nome de cada uma?", "i", 60), XE, 990, passo=0.08)
    if t >= C["s13"]:
        E.relogio(c, t, C["s13.a"], cx=1650, cy=840, r=80)


def b_resposta(c, t, C, b):
    Ps = []
    for k, M_ in enumerate((BUTANAL, BUTANONA)):
        cx = 600 + k * 760
        E.foco(c, t, C["s14"] - 0.4, 0.4, lambda a, cx=cx, k=k: (E.bola(c, cx - 300, 330, 36, a=a), centro(c, str(k + 1), cx - 300, 348, 44, "g", E.SOBRE, a)))
        Ps.append(mol(c, t, C["s14"] - 0.4, M_, cx, 520, 130, d=0.1))
    carbonila(c, t, C["s14.a"], Ps[0], 3, 4, 46)
    pilula_em(c, t, C["s14.a"] + 0.4, "aldeído", 600, 740, 56, E.COR)
    nome(c, t, C["s14.b"], [("but", TINTA, "4 C"), ("an", TINTA, None), ("al", COR, None)], 600, 880, 100, 0.3, "center")
    carbonila(c, t, C["s14.d"], Ps[1], 1, 4, 46)
    anelc(c, t, C["s14.d"] + 0.3, Ps[1], 0, 26); anelc(c, t, C["s14.d"] + 0.4, Ps[1], 2, 26)
    pilula_em(c, t, C["s14.d"] + 0.4, "cetona", 1360, 740, 56, E.COR)
    nome(c, t, C["s14.e"], [("but", TINTA, "4 C"), ("an", TINTA, None), ("ona", COR, None)], 1360, 880, 100, 0.3, "center")
    if t >= C["s15"]:
        Q.bastao(c, t, C["s15.a"], BUTANONA["pts"][:4], 1360, 520, 130, d=0.01, numeros=C["s15.a"], passo_n=0.12)
        E.foco(c, t, C["s15.b"], 0.4, lambda a: centro(c, "sem número: só cabe no 2", 1360, 1010, 46, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s16.a"], [("carbonila", "g", 76, COR), ("=", "g", 70, TINTA2), ("C=O", "g", 76)], XE, 360, passo=0.12)
        E.frase(c, t, C["s16.b"], [("na ponta, com H:", "i", 70), ("aldeído", "g", 70, COR), ("(al)", "g", 66, TINTA2)], XE, 540, passo=0.12)
        E.frase(c, t, C["s16.c"], [("no meio:", "i", 70), ("cetona", "g", 70, COR), ("(ona)", "g", 66, TINTA2)], XE, 700, passo=0.12)
        mol(c, t, C["s16.b"], ETANAL, 1500, 520, 110, d=0.5)
        mol(c, t, C["s16.c"], PROPANONA, 1500, 740, 110, d=0.5)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s17.a"], [("o ácido", "g", 90, COR), ("do vinagre", "i", 90)], XE, 400, passo=0.14)
    E.frase(c, t, C["s17.b"], [("o éster", "g", 90, COR), ("das frutas", "i", 90)], XE, 530, passo=0.14)
    cond(c, t, C["s17.b"] + 0.4, ["CH3", "COOH"], XE, 720, 100, cores={1: E.COR})
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s17.c"] + 0.2, 0.4))
    E.frase(c, t, C["s17.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, carbonila=b_carbonila, aldeido=b_carbonila, cetona=b_cetona, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
