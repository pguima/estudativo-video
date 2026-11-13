"""Visual — Estudativo · QUI-ORG-010: haletos e outras funções (CFC, DDT, nitrocomposto, tiol).
Segue a linguagem da Química (QUI-MIS-001), da Orgânica (QUI-ORG-001) e do módulo Funções (QUI-ORG-006): halogênios em CPK
(F e Cl verdes, Br vinho, I roxo), S amarelo-escuro. Peças desta aula: camada() — a faixa de ozônio com moléculas de O₃, o
Sol no alto e as setas de luz ultravioleta; cadeia_alimentar() — três caixas (peixe pequeno, peixe grande, ave) com bolinhas de
DDT que se acumulam da esquerda para a direita.
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
ARQUIVO_FINAL = "estudativo_QUI-ORG-010_haletos_outras_funcoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("haleto", "cfc", "ddt", "outras", "erro", "atalho", "questao", "fim"))
CL, FL, SC = Q.cor_el("Cl"), Q.cor_el("F"), Q.cor_el("S")
CORES_X = {"Cl": CL, "F": FL, "S": SC, "N": Q.cor_el("N"), "O": Q.cor_el("O")}


def anel_em(cx, cy, rot):
    return [(cx + math.cos(math.radians(rot + 60 * k)), cy - math.sin(math.radians(rot + 60 * k))) for k in range(6)]


_L, _R = anel_em(-1.74, 1.0, 30), anel_em(1.74, 1.0, 150)
DDT = dict(pts=[(0, 0), (0, -1), (-0.87, -1.5), (0.87, -1.5), (0, -2)] + _L + _R + [(-3.48, 2.0), (3.48, 2.0)],
           ligs=[(0, 1), (1, 2), (1, 3), (1, 4), (0, 5), (0, 11)] + ligs_anel(5, 6) + ligs_anel(11, 6) + [(8, 17), (14, 18)],
           duplas={(5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16)}, rot={2: "Cl", 3: "Cl", 4: "Cl", 17: "Cl", 18: "Cl"})
HX = anel(6)
TNT = dict(pts=HX + [(0, -2), (-1.74, 1.0), (1.74, 1.0), (0, 2)], ligs=ligs_anel(0, 6) + [(0, 6), (2, 7), (4, 8), (3, 9)],
           duplas={(0, 1), (2, 3), (4, 5)}, rot={7: "O2N", 8: "NO2", 9: "NO2"})
ETANOTIOL = dict(pts=Q.zigzag(3), rot={2: "SH"})
ETANOL = dict(pts=Q.zigzag(3), rot={2: "OH"})
CFC_AT = [("C", 0, 0), ("Cl", -1.2, 0), ("Cl", 1.2, 0), ("F", 0, -1.1), ("F", 0, 1.1)]
CFC_LG = [(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1)]
assert len([i for i in range(len(DDT["pts"])) if i not in DDT["rot"]]) == 14 and len(DDT["rot"]) == 5  # C14H9Cl5
assert Q.contar("CCl2F2") == {"C": 1, "Cl": 2, "F": 2}


def camada(c, t, t0, y=300, a_max=1.0, sep=None):
    """faixa de ozônio no alto, com o Sol e a Terra embaixo"""
    a = ep(t, t0, 0.6) * a_max
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeLTRB(900, y - 70, W, y + 70), M.paint(E.COR, 0.12 * a))
    for k in range(6):
        sk = sep[k] if sep else 0.0
        Q.molecula_desenho(c, "O3", 1000 + k * 150, y, 38, a * (1 - 0.6 * sk), separa=sk)
    E.bola(c, 1780, 110, 60, "#FFC93C", a)
    E.foco(c, t, t0, 0.4, lambda q: E.escreve(c, "camada de ozônio", 930, y + 120, 42, "i", TINTA2, q * a_max))


def cadeia_alimentar(c, t, t0, x0, y, passo=0.8):
    itens = (("peixe pequeno", 3), ("peixe grande", 10), ("ave", 28))
    for k, (s, n) in enumerate(itens):
        tk = t0 + k * passo
        x = x0 + k * 520
        q = ep(t, tk, 0.4)
        if q <= 0:
            continue
        M.rrect(c, x, y, 420, 260, 30, "#FFFFFF", q, shadow=True)
        centro(c, s, x + 210, y + 320, 48, "g", TINTA, q)
        for j in range(n):
            qj = ep(t, tk + 0.2 + 0.03 * j, 0.25)
            if qj > 0:
                E.bola(c, x + 40 + (j % 7) * 56, y + 40 + (j // 7) * 56, 18, CL, qj)
        if k:
            seta(c, t, tk - 0.2, x - 90, y + 130, x - 15, y + 130, TINTA2)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        pilula_em(c, t, C["s01.a"], "gás de geladeira antiga", 520, 280, 46, TINTA, "i")
        Q.lewis(c, t, C["s01.a"] + 0.3, CFC_AT, CFC_LG, 520, 560, escala=130, size=84, cores=CORES_X)
        pilula_em(c, t, C["s01.b"], "inseticida proibido", 1400, 280, 46, TINTA, "i")
        P = mol(c, t, C["s01.b"] + 0.3, DDT, 1400, 560, 80, size=38)
        halo(c, t, C["s01.c"], [(520 - 156, 560), (520 + 156, 560)], 50, CL)
        halo(c, t, C["s01.c"] + 0.3, [P[i] for i in (2, 3, 4, 17, 18)], 32, CL)
        E.frase(c, t, C["s01.c"], [("cloro", "g", 70, CL), ("preso a carbono", "i", 70)], W / 2, 920, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 520, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("haleto,", "g", 70, COR), ("nitro", "g", 70, COR), ("e", "i", 74), ("tiol", "g", 70, COR)]),
                 (C["s02.c"], [("o estrago do", "i", 74), ("CFC", "g", 70)]),
                 (C["s02.d"], [("o acúmulo do", "i", 74), ("DDT", "g", 70)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("das últimas aulas", "i", 76, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], ps("cada função muda o grupo preso à cadeia", "i", 62), XE, 330, passo=0.1)
    P = mol(c, t, C["s03.b"], ETANOL, 600, 620, 150)
    halo(c, t, C["s03.b"] + 0.3, [P[2]], 50, CINZA)
    pilula_em(c, t, C["s03.b"] + 0.4, "álcool: ol", 600, 820, 50, TINTA, "g")
    P2 = mol(c, t, C["s03.c"], dict(pts=[(-0.45, 0.25), (0.45, -0.25)], rot={1: "NH2"}), 1350, 620, 150)
    halo(c, t, C["s03.c"] + 0.3, [P2[1]], 50, CINZA)
    pilula_em(c, t, C["s03.c"] + 0.4, "amina: N sem carbonila", 1350, 820, 50, TINTA, "g")


# ---------------- haleto ----------------
def b_haleto(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("halogênios:", "i", 70)], XE, 220)
    for k, s in enumerate(("F", "Cl", "Br", "I")):
        Q.atomo_em(c, t, C["s04.a"] + 0.4 + 0.2 * k, XE + 460 + k * 150, 196, 56, s)
    E.frase(c, t, C["s04.b"], [("cada um faz", "i", 64), ("1 ligação,", "g", 62, COR), ("como o H", "i", 64)], XE, 360, passo=0.12)
    Q.lewis(c, t, C["s04.c"], [("C", 0, 0), ("H", -1.1, 0), ("H", 0, -1.0), ("H", 0, 1.0), ("Cl", 1.25, 0)], [(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1)],
            1350, 640, escala=150, size=96, cores=CORES_X)
    halo(c, t, C["s04.d"], [(1350 + 1.25 * 150, 640)], 60, CL)
    pilula_em(c, t, C["s04.d"] + 0.3, "haleto orgânico", 1350, 900, 56, E.COR)
    E.frase(c, t, C["s04.e"], ps("o nome: o halogênio na frente", "i", 60), XE, 560, passo=0.1)
    nome(c, t, C["s04.f"], [("cloro", CL, "halogênio"), ("metano", TINTA, "a cadeia")], XE, 760, 110, 0.3)


# ---------------- CFC ----------------
def b_cfc(c, t, C, b):
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("CFC", "g", 90, COR), ("=", "g", 80, TINTA2), ("clorofluorcarbono", "i", 74)], XE, 230, passo=0.12)
        Q.lewis(c, t, C["s05.a"] + 0.5, CFC_AT, CFC_LG, 1350, 580, escala=150, size=100, cores=CORES_X)
        E.frase(c, t, C["s05.a"] + 1.2, ps("carbono só com cloro e flúor", "i", 60, TINTA2), XE, 340, passo=0.1)
        E.frase(c, t, C["s05.b"], [("não pega fogo,", "g", 62), ("quase não reage", "g", 62, COR)], XE, 520, passo=0.12)
        for k, s in enumerate(("geladeiras", "sprays")):
            pilula_esq(c, t, C["s05.c"] + 0.3 * k, s, XE + k * 330, 680, 52, TINTA, "i")
        return
    if t < C["s07"]:
        camada(c, t, C["s06.a"], 300)
        E.frase(c, t, C["s06.a"], ps("dura décadas e sobe", "i", 62), XE, 220, passo=0.1)
        sobe = ease_io(prog(t, C["s06.a"] + 0.2, 2.0))
        cx_, cy_ = 1300, lerp(900, 470, sobe)
        quebra = ep(t, C["s06.c"], 0.6)
        Q.lewis(c, 99, 0, CFC_AT[:1] + CFC_AT[2:], [(0, 1, 1), (0, 2, 1), (0, 3, 1)], cx_, cy_, escala=70, size=48, cores=CORES_X)
        clx = lerp(cx_ - 84, cx_ - 260, quebra)
        Q.atomo(c, clx, cy_, 30, "Cl")
        if quebra < 0.2:
            M.line(c, cx_ - 30, cy_, clx + 28, cy_, TINTA, 1, 5)
        E.frase(c, t, C["s06.b"], [("o escudo contra a luz", "i", 60), ("ultravioleta", "g", 58, COR)], XE, 330, passo=0.1)
        for k in range(3):
            seta(c, t, C["s06.c"] - 0.6 + 0.15 * k, 1700 - k * 40, 170, 1380 + k * 30, 430 + k * 10, "#9B5DE5")
        E.frase(c, t, C["s06.c"], ps("a luz ultravioleta quebra a ligação C–Cl", "i", 56), XE, 560, passo=0.08)
        E.frase(c, t, C["s06.d"], [("e solta um", "i", 60), ("átomo de cloro", "g", 58, CL)], XE, 660, passo=0.1)
        return
    camada(c, t, C["s07"] - 1, 300, sep=[ep(t, C["s07.a"] + 0.9 * k, 0.5) for k in range(6)])
    E.frase(c, t, C["s07.a"], ps("um cloro destrói um ozônio", "i", 62), XE, 220, passo=0.1)
    # o cloro passeia pela faixa e cada ozônio que ele toca se desfaz
    ciclo = (t - C["s07.a"]) / 0.9
    if t >= C["s07.a"]:
        k = min(5.0, max(0.0, ciclo))
        Q.atomo(c, 1000 + k * 150 - 40, 380, 26, "Cl")
    E.frase(c, t, C["s07.b"], ps("e sai livre para destruir outro", "i", 58, TINTA2), XE, 330, passo=0.1)
    E.frase(c, t, C["s07.c"], [("1 cloro", "g", 70, CL), ("→", "g", 70, TINTA2), ("milhares de ozônios", "g", 66, COR)], XE, 560, passo=0.12)
    pilula_esq(c, t, C["s07.d"], "Protocolo de Montreal, 1987: o CFC foi sendo proibido", XE, 760, 44, TINTA, "b")


# ---------------- DDT ----------------
def b_ddt(c, t, C, b):
    if t < C["s09"]:
        P = mol(c, t, C["s08.a"], DDT, 1300, 560, 100, size=46)
        E.frase(c, t, C["s08.a"], [("DDT:", "g", 76, COR), ("inseticida", "i", 70)], XE, 220, passo=0.12)
        halo(c, t, C["s08.a"] + 0.6, [P[i] for i in (2, 3, 4, 17, 18)], 36, CL)
        E.frase(c, t, C["s08.a"] + 0.8, [("5", "g", 62, CL), ("cloros", "i", 64)], XE, 320, passo=0.1)
        E.frase(c, t, C["s08.b"], ps("dois anéis e um carbono", "i", 58, TINTA2), XE, 410, passo=0.1)
        E.frase(c, t, C["s08.c"], [("não se dissolve na água,", "i", 56), ("dissolve na gordura", "g", 54, COR)], XE, 880, passo=0.08)
        E.frase(c, t, C["s08.d"], ps("e o corpo quase não desmonta a molécula", "i", 56, TINTA2), XE, 980, passo=0.08)
        return
    E.frase(c, t, C["s09.a"], ps("cada animal guarda o DDT que comeu", "i", 64), XE, 220, passo=0.1)
    cadeia_alimentar(c, t, C["s09.b"], 220, 400, passo=(C["s09.d"] - C["s09.b"]) / 2)
    E.frase(c, t, C["s09.e"], [("a cada passo,", "i", 64), ("a dose fica maior", "g", 64, COR)], W / 2, 1010, "center", 0.12)


# ---------------- nitro e tiol ----------------
def b_outras(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("mais duas funções", "i", 66, TINTA2), XE, 220, passo=0.1)
        E.frase(c, t, C["s10.b"], [("nitrocomposto:", "g", 70, COR)], XE, 360)
        Q.formula_em(c, t, C["s10.b"] + 0.5, "–NO2", XE + 600, 360, 90, cores={"N": Q.cor_el("N"), "O": Q.cor_el("O")})
        E.foco(c, t, C["s10.b"] + 0.8, 0.4, lambda a: E.escreve(c, "preso a um carbono", XE, 440, 50, "i", TINTA2, a))
        P = mol(c, t, C["s10.c"], TNT, 1400, 640, 110, size=56)
        for k, i in enumerate((7, 8, 9)):
            halo(c, t, C["s10.c"] + 0.5 + 0.2 * k, [P[i]], 46)
        E.frase(c, t, C["s10.c"], [("3 no tolueno:", "i", 60), ("TNT", "g", 66, COR)], XE, 640, passo=0.12)
        E.foco(c, t, C["s10.c"] + 1.2, 0.4, lambda a: E.escreve(c, "um explosivo", XE, 730, 54, "i", TINTA2, a))
        return
    E.frase(c, t, C["s11.a"], [("tiol:", "g", 76, COR), ("o álcool com", "i", 66), ("S", "g", 66, SC), ("no lugar do", "i", 66), ("O", "g", 66, Q.cor_el("O"))], XE, 220, passo=0.12)
    P1 = mol(c, t, C["s11.a"] + 0.4, ETANOL, 560, 520, 150)
    seta(c, t, C["s11.b"], 830, 520, 1080, 520)
    P2 = mol(c, t, C["s11.b"] + 0.3, ETANOTIOL, 1350, 520, 150)
    halo(c, t, C["s11.b"] + 0.6, [P2[2]], 54, SC)
    pilula_em(c, t, C["s11.b"] + 0.6, "–SH", 1450, 380, 54, TINTA, "g")
    nome(c, t, C["s11.c"], [("etano", TINTA, "hidrocarboneto"), ("tiol", COR, "função")], 1150, 760, 100, 0.3)
    E.frase(c, t, C["s11.d"], [("cheiro", "i", 64), ("forte", "g", 62, COR)], XE, 760, passo=0.12)
    pilula_esq(c, t, C["s11.e"], "vai no gás de cozinha: para você sentir o vazamento", XE, 930, 44, TINTA, "b")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("todo N é amina?", "i", 70), XE + 450, 190, passo=0.12)
    Q.formula_em(c, t, C["s12.a"] + 0.5, "CH3–NO2", 560, 480, 130, align="center", cores={"N": Q.cor_el("N"), "O": Q.cor_el("O")})

    def errado():
        E.foco(c, t, C["s12.a"] + 1.2, 0.4, lambda a: E.escreve(c, "amina?", 380, 640, 80, "g", ERRADO, a))
        if t >= C["s12.a"] + 2.0:
            E.risco(c, 370, 660, 640, 590, t, C["s12.a"] + 2.0, largura=9)
    E.saida(c, t, C["s12.b"] + 0.4, errado)
    E.frase(c, t, C["s12.b"], ps("N preso a dois O, sem H", "i", 56), 300, 760, passo=0.08)
    pilula_em(c, t, C["s12.d"], "nitrocomposto", 560, 880, 56, E.COR)
    Q.formula_em(c, t, C["s12.c"], "CH3–NH2", 1360, 480, 130, align="center", cores={"N": Q.cor_el("N")})
    E.frase(c, t, C["s12.c"], ps("N só com C e H, sem carbonila", "i", 56, TINTA2), 1080, 760, passo=0.08)
    pilula_em(c, t, C["s12.c"] + 0.6, "amina", 1360, 880, 56, TINTA2)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], ps("o atalho do enxofre", "i", 70, CLARO), W / 2, 170, "center", 0.12)
        Q.atomo_em(c, t, C["s13.b"], 820, 330, 54, "O", escuro=True)
        Q.atomo_em(c, t, C["s13.b"] + 0.2, 1100, 330, 60, "S", escuro=True)
        E.foco(c, t, C["s13.b"] + 0.4, 0.4, lambda a: centro(c, "mesma família, 2 ligações", 960, 440, 50, "i", CLARO, a))
        E.frase(c, t, C["s13.c"], [("troque O por S:", "i", 64, CLARO), ("+ tio", "g", 70, E.CLARO)], XE, 580, passo=0.12)
        linhas = (("s13.d", [("C", 0, 0), ("O", 1, 0), ("H", 2, 0)], [("C", 0, 0), ("S", 1, 0), ("H", 2, 0)], "álcool → tiol"),
                  ("s13.e", [("C", 0, 0), ("O", 1, 0), ("C", 2, 0)], [("C", 0, 0), ("S", 1, 0), ("C", 2, 0)], "éter → tioéter"))
        for k, (key, a1, a2, rot_) in enumerate(linhas):
            y = 730 + k * 170
            Q.lewis(c, t, C[key], a1, [(0, 1, 1), (1, 2, 1)], XE + 40, y, escala=110, size=76, escuro=True, cores={"O": Q.cor_el("O")})
            seta(c, t, C[key] + 0.3, XE + 340, y, XE + 460, y, E.CLARO)
            Q.lewis(c, t, C[key] + 0.4, a2, [(0, 1, 1), (1, 2, 1)], XE + 540, y, escala=110, size=76, escuro=True, cores={"S": SC})
            pilula_em(c, t, C[key] + 0.6, rot_, 1450, y - 10, 56, E.COR)
        return
    E.frase(c, t, C["s14.a"], ps("o S ocupa o mesmo lugar do O na molécula", "i", 62, CLARO), XE, 300, passo=0.08)
    E.frase(c, t, C["s14.b"], [("mas não espere", "i", 66, CLARO), ("as mesmas propriedades", "g", 62, BR)], XE, 480, passo=0.12)
    E.frase(c, t, C["s14.c"], [("etanol:", "g", 62, BR), ("cheiro suave", "i", 64, CLARO), ("·", "g", 62, CLARO), ("etanotiol:", "g", 62, BR), ("fede", "g", 64, ERRADO)],
            XE, 660, passo=0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s15.a"], ps("qual é a função de cada uma?", "i", 64), XE, 300, passo=0.1)
    itens = (("s15.b", "geladeira antiga"), ("s15.c", "aeromodelo"), ("s15.d", "cheiro de gás"))
    for k, (key, s) in enumerate(itens):
        cx = 360 + k * 600
        E.foco(c, t, C[key], 0.4, lambda a, cx=cx, k=k: (E.bola(c, cx - 190, 440, 36, a=a), centro(c, str(k + 1), cx - 190, 458, 44, "g", E.SOBRE, a)))
        pilula_em(c, t, C[key] + 0.2, s, cx + 40, 440, 42, TINTA, "i")
    Q.lewis(c, t, C["s15.b"] + 0.3, CFC_AT, CFC_LG, 360, 680, escala=110, size=70, cores=CORES_X)
    Q.formula_em(c, t, C["s15.c"] + 0.3, "CH3–NO2", 960, 700, 90, align="center", cores={"N": Q.cor_el("N"), "O": Q.cor_el("O")})
    Q.formula_em(c, t, C["s15.d"] + 0.3, "CH3–CH2–SH", 1560, 700, 80, align="center", cores={"S": SC})
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=960, cy=900, r=60)


def b_resposta(c, t, C, b):
    for k in range(3):
        cx = 360 + k * 600
        E.foco(c, t, C["s17"] - 0.4, 0.4, lambda a, cx=cx, k=k: (E.bola(c, cx - 190, 440, 36, a=a), centro(c, str(k + 1), cx - 190, 458, 44, "g", E.SOBRE, a)))
    Q.lewis(c, t, C["s17"] - 0.4, CFC_AT, CFC_LG, 360, 680, escala=110, size=70, cores=CORES_X)
    Q.formula_em(c, t, C["s17"] - 0.4, "CH3–NO2", 960, 700, 90, align="center", cores={"N": Q.cor_el("N"), "O": Q.cor_el("O")})
    Q.formula_em(c, t, C["s17"] - 0.4, "CH3–CH2–SH", 1560, 700, 80, align="center", cores={"S": SC})
    for k, (key, fn, nm) in enumerate((("s17.a", "haleto", "um CFC"), ("s17.b", "nitrocomposto", "nitrometano"), ("s17.c", "tiol", "etanotiol"))):
        cx = 360 + k * 600
        pilula_em(c, t, C[key], fn, cx, 900, 56, E.COR)
        E.foco(c, t, C[key] + 0.5, 0.4, lambda a, cx=cx, nm=nm: centro(c, nm, cx, 1010, 50, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for k, (key, a_, b_) in enumerate((("s18.a", "halogênio no C", "haleto"), ("s18.b", "–NO2", "nitrocomposto"), ("s18.c", "–SH", "tiol"))):
            y = 330 + k * 120
            E.foco(c, t, C[key], 0.4, lambda a, a_=a_, y=y: Q.formula(c, a_, XE, y, 60, TINTA, a, cores=CORES_X) if a_.startswith("–") else E.escreve(c, a_, XE, y, 60, "g", TINTA, a))
            pilula_em(c, t, C[key] + 0.3, b_, 900, y - 20, 54, E.COR)
        E.frase(c, t, C["s18.d"], [("CFC:", "g", 60), ("solta cloro, que destrói o ozônio", "i", 60)], XE, 760, passo=0.08)
        E.frase(c, t, C["s18.e"], [("DDT:", "g", 60), ("se acumula na gordura, de bicho em bicho", "i", 60)], XE, 870, passo=0.08)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("prática:", "g", 90, COR), ("as funções", "i", 84)], XE, 400, passo=0.14)
    E.frase(c, t, C["s19.a"] + 0.6, ps("em moléculas reais", "i", 84), XE, 510, passo=0.12)
    for k, (key, s) in enumerate((("s19.b", "aspirina"), ("s19.c", "adrenalina"), ("s19.d", "penicilina"))):
        pilula_esq(c, t, C[key], s, XE + [0, 260, 610][k], 680, 52, TINTA, "g")
    E.foco(c, t, C["s19.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.e"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.e"] + 0.2, 0.4))
    E.frase(c, t, C["s19.f"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, haleto=b_haleto, cfc=b_cfc, ddt=b_ddt, outras=b_outras, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
