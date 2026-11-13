"""Visual — Estudativo · QUI-ORG-014: isomeria plana.
Segue a linguagem da Química (QUI-MIS-001), da Orgânica (QUI-ORG-001), das Funções (QUI-ORG-006) e do módulo Propriedades
(QUI-ORG-012). Nesta aula: par() — os dois isômeros lado a lado, com a fórmula molecular comum numa pílula no meio e a pílula
do tipo de isomeria embaixo; o que muda entre eles ganha halo (grupo, heteroátomo) ou realce (cadeia, dupla). Fluxograma das
perguntas = arvore() com caixas arredondadas (fórmula → função → o que mudou).
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
ARQUIVO_FINAL = "estudativo_QUI-ORG-014_isomeria_plana.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("isomero", "funcao", "mesma", "erro", "atalho", "questao", "fim"))

Z3, Z4, Z5 = Q.zigzag(3), Q.zigzag(4), Q.zigzag(5)
Z3f = [(x, -y) for x, y in Z3]
ETANOL = dict(pts=Z3, rot={2: "OH"})
METOXIMETANO = dict(pts=Z3, rot={1: "O"})
ETENOL = dict(pts=Z3, duplas={(0, 1)}, rot={2: "OH"})
ETANAL = dict(pts=Z3, duplas={(1, 2)}, rot={2: "O"})
BUTANO = dict(pts=Z4)
METILPROP = dict(pts=Z3 + [(Z3[1][0], Z3[1][1] + 1)], ligs=[(0, 1), (1, 2), (1, 3)])
P1OL = dict(pts=Z4, rot={3: "OH"})
P2OL = dict(pts=Z3 + [(Z3[1][0], Z3[1][1] + 1)], ligs=[(0, 1), (1, 2), (1, 3)], rot={3: "OH"})
MOXP = dict(pts=Z5, rot={1: "O"})
EOXE = dict(pts=Z5, rot={2: "O"})
PROPANO = dict(pts=Z3)
PROPENO = dict(pts=Z3, duplas={(0, 1)})
PENTANO = dict(pts=Z5)
DIMETILPROP = dict(pts=[(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)], ligs=[(0, 1), (0, 2), (0, 3), (0, 4)])
PROPANAL = dict(pts=Z4, duplas={(2, 3)}, rot={3: "O"})
PROPANONA = dict(pts=Z3f + [(Z3f[1][0], Z3f[1][1] - 1)], ligs=[(0, 1), (1, 2), (1, 3)], duplas={(1, 3)}, rot={3: "O"})
BUT1 = dict(pts=Z4, duplas={(0, 1)})
BUT2 = dict(pts=Z4, duplas={(1, 2)})
assert Q.contar("CH3CH2OH") == Q.contar("CH3OCH3") == {"C": 2, "H": 6, "O": 1}
assert Q.contar("CH2CHOH") == Q.contar("CH3CHO") == {"C": 2, "H": 4, "O": 1}
assert Q.contar("CH3CH2CH2CH3") == Q.contar("CH3CH(CH3)CH3") == {"C": 4, "H": 10}
assert Q.contar("CH3OCH2CH2CH3") == Q.contar("CH3CH2OCH2CH3") == {"C": 4, "H": 10, "O": 1}
assert Q.contar("C3H8") != Q.contar("C3H6")
assert Q.contar("CH3CH2CH2CH2CH3") == Q.contar("C(CH3)4") == {"C": 5, "H": 12}
assert Q.contar("CH3CH2CHO") == Q.contar("CH3COCH3") == {"C": 3, "H": 6, "O": 1}
assert Q.contar("CH2CHCH2CH3") == Q.contar("CH3CHCHCH3") == {"C": 4, "H": 8}


def par(c, t, t0, t1, A, B, formula, tipo=None, ttipo=None, y=520, esc=130, xs=(560, 1360), tf=None, nomes=None):
    PA = mol(c, t, t0, A, xs[0], y, esc, d=0.6)
    PB = mol(c, t, t1, B, xs[1], y, esc, d=0.6)
    if nomes:
        E.foco(c, t, t0 + 0.4, 0.4, lambda a: centro(c, nomes[0], xs[0], y + 240, 50, "g", TINTA, a))
        E.foco(c, t, t1 + 0.4, 0.4, lambda a: centro(c, nomes[1], xs[1], y + 240, 50, "g", TINTA, a))
    if formula:
        tf_ = tf if tf is not None else t1 + 0.4
        E.foco(c, t, tf_, 0.4, lambda a: (M.rrect(c, (xs[0] + xs[1]) / 2 - 130, y - 50, 260, 100, 50, "#FFFFFF", a, shadow=True),
                                          Q.formula(c, formula, (xs[0] + xs[1]) / 2, y + 22, 60, TINTA, a, "center")))
    if tipo:
        pilula_em(c, t, ttipo, tipo, (xs[0] + xs[1]) / 2, y + 360, 64, E.COR)
    return PA, PB


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        PA, PB = par(c, t, C["s01"], C["s01"] + 0.4, ETANOL, METOXIMETANO, "C2H6O", tf=C["s01"] + 1.2, nomes=("etanol", "metoximetano"))
        pilula_em(c, t, C["s01.b"], "líquido", 560, 860, 50, TINTA, "i")
        pilula_em(c, t, C["s01.c"], "gás", 1360, 860, 50, TINTA, "i")
        E.frase(c, t, C["s01.d"], [("mesma fórmula,", "i", 70), ("substâncias diferentes", "g", 66, COR)], W / 2, 990, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 520, 240 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula, classifique em", "i", 70), XE, 240, passo=0.1)
    for k, (key, s) in enumerate((("s02.b", "cadeia"), ("s02.c", "posição"), ("s02.d", "função"), ("s02.e", "compensação"), ("s02.f", "tautomeria"))):
        E.foco(c, t, C[key], 0.4, lambda a, k=k, s=s: (E.bola(c, XE + 40, 360 + k * 130, 40, a=a), centro(c, str(k + 1), XE + 40, 380 + k * 130, 50, "g", E.SOBRE, a),
                                                       E.escreve(c, s, XE + 110, 386 + k * 130, 72, "g", COR if k else TINTA, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 76, TINTA2), XE, 220, passo=0.12)
    lista(c, t, [(C["s03.a"], [("cadeia principal", "g", 66), ("e galhos", "i", 70)]), (C["s03.b"], [("a numeração", "g", 66)]),
                 (C["s03.c"], [("as funções com O,", "g", 66), ("do álcool ao éster", "i", 70)])], XE, 400, 160)
    mol(c, t, C["s03.a"], METILPROP, 1500, 560, 140)


# ---------------- isômeros ----------------
def b_isomero(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("isômeros:", "g", 80, COR), ("mesma fórmula molecular,", "i", 70)], XE, 230, passo=0.12)
    E.frase(c, t, C["s04.a"] + 1.4, ps("estruturas diferentes", "i", 70), XE + 380, 330, passo=0.1)
    E.frase(c, t, C["s04.b"], ps("os mesmos átomos, montados de outro jeito", "i", 56, TINTA2), XE, 430, passo=0.08)
    par(c, t, C["s04.b"] + 0.3, C["s04.b"] + 0.7, BUTANO, METILPROP, "C4H10", y=650, esc=110)
    E.frase(c, t, C["s04.c"], [("plana:", "g", 58), ("a diferença aparece no papel", "i", 58)], XE, 900, passo=0.1)
    E.frase(c, t, C["s04.d"], [("5 tipos,", "g", 58, COR), ("2 perguntas", "g", 58)], XE, 1000, passo=0.12)


# ---------------- função e tautomeria ----------------
def b_funcao(c, t, C, b):
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("1ª pergunta:", "g", 66, COR), ("mesma função?", "i", 70)], XE, 220, passo=0.12)
        E.frase(c, t, C["s05.c"], [("não:", "g", 66), ("isomeria de função", "g", 66, COR)], XE, 330, passo=0.12)
        PA, PB = par(c, t, C["s05.d"], C["s05.d"] + 0.4, ETANOL, METOXIMETANO, "C2H6O", "isomeria de função", C["s05.e"], y=560)
        pilula_em(c, t, C["s05.d"] + 0.6, "álcool", 560, 720, 50, TINTA, "g")
        pilula_em(c, t, C["s05.d"] + 1.0, "éter", 1360, 720, 50, TINTA, "g")
        halo(c, t, C["s05.d"] + 0.6, [PA[2]], 50); halo(c, t, C["s05.d"] + 1.0, [PB[1]], 50)
        return
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], [("tautomeria:", "g", 70, COR), ("um caso especial", "i", 66)], XE, 220, passo=0.12)
        vira = ease_io(prog(t, C["s06.e"], 1.2))
        alvo = ETENOL if t < C["s06.e"] + 0.6 else ETANAL
        P = mol(c, t, C["s06.b"] if alvo is ETENOL else C["s06.e"] + 0.6, alvo, 1300, 560, 190)
        if alvo is ETENOL:
            halo(c, t, C["s06.c"], [P[2], P[1]], 60)
            pilula_em(c, t, C["s06.c"] + 0.3, "enol", 1300, 330, 56, E.COR)
            E.frase(c, t, C["s06.b"], ps("OH num carbono de dupla", "i", 60), XE, 360, passo=0.1)
            if t >= C["s06.e"]:
                hx = lerp(P[2][0] + 40, P[0][0], vira); hy = lerp(P[2][1] - 30, P[1][1] + 80, vira)
                Q.atomo(c, hx, hy, 30, "H")
        else:
            halo(c, t, C["s06.f"], [P[1], P[2]], 60)
            pilula_em(c, t, C["s06.f"] + 0.2, "aldeído", 1300, 330, 56, E.COR)
        E.frase(c, t, C["s06.d"], ps("o enol não fica parado:", "i", 60), XE, 520, passo=0.1)
        E.frase(c, t, C["s06.e"], ps("o H pula para o carbono vizinho", "i", 56, TINTA2), XE, 620, passo=0.08)
        E.frase(c, t, C["s06.e"] + 1.6, ps("e a dupla vai para o O", "i", 56, TINTA2), XE, 710, passo=0.08)
        return
    E.frase(c, t, C["s07.a"], ps("as duas formas num vaivém", "i", 66), XE, 220, passo=0.1)
    PA, PB = par(c, t, C["s07"], C["s07"] + 0.3, ETENOL, ETANAL, None, y=520, esc=150, nomes=("etenol", "etanal"))
    E.foco(c, t, C["s07"] + 0.6, 0.4, lambda a: Q.formula(c, "⇌", W / 2 - 40, 560, 120, COR, a, "center"))
    E.foco(c, t, C["s07.a"] + 1.4, 0.4, lambda a: centro(c, "quase tudo fica como aldeído", 1360, 800, 44, "i", TINTA2, a))
    pilula_em(c, t, C["s07.c"], "tautomeria", W / 2 - 40, 900, 64, E.COR)


# ---------------- mesma função ----------------
def b_mesma(c, t, C, b):
    E.frase(c, t, C["s08.a"], [("2ª pergunta:", "g", 66, COR), ("o que mudou?", "i", 70)], XE, 200, passo=0.12)
    if t < C["s09"]:
        E.frase(c, t, C["s08.c"], [("a cadeia:", "i", 62), ("isomeria de cadeia", "g", 62, COR)], XE, 300, passo=0.12)
        PA, PB = par(c, t, C["s08.d"], C["s08.d"] + 0.4, BUTANO, METILPROP, "C4H10", None, y=560, nomes=("butano", "metilpropano"))
        realca_fila(c, t, C["s08.e"], PA, [0, 1, 2, 3]); realca_fila(c, t, C["s08.e"] + 0.5, PB, [0, 1, 2])
        anelc(c, t, C["s08.e"] + 1.0, PB, 3, 30)
        pilula_em(c, t, C["s08.e"] + 1.2, "cadeia", 960, 880, 64, E.COR)
        return
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], [("um grupo mudou de carbono:", "i", 60), ("posição", "g", 62, COR)], XE, 300, passo=0.12)
        PA, PB = par(c, t, C["s09.b"], C["s09.b"] + 0.4, P1OL, P2OL, "C3H8O", None, y=560, nomes=("propan-1-ol", "propan-2-ol"))
        halo(c, t, C["s09.c"], [PA[3]], 50); halo(c, t, C["s09.c"] + 0.3, [PB[3]], 50)
        pilula_em(c, t, C["s09.c"] + 0.8, "posição", 960, 880, 64, E.COR)
        return
    E.frase(c, t, C["s10.a"], [("o heteroátomo mudou de lugar:", "i", 60), ("compensação", "g", 62, COR)], XE, 300, passo=0.12)
    E.foco(c, t, C["s10.b"] + 0.8, 0.4, lambda a: E.escreve(c, "(ou metameria)", XE + 1260, 300, 46, "i", TINTA2, a))
    PA, PB = par(c, t, C["s10.c"], C["s10.c"] + 0.4, MOXP, EOXE, "C4H10O", None, y=560, esc=110, nomes=("metoxipropano", "etoxietano"))
    halo(c, t, C["s10.d"], [PA[1]], 46)
    E.foco(c, t, C["s10.d"] + 0.3, 0.4, lambda a: centro(c, "1 C | 3 C", 560, 440, 48, "g", TINTA2, a))
    halo(c, t, C["s10.e"], [PB[2]], 46)
    E.foco(c, t, C["s10.e"] + 0.3, 0.4, lambda a: centro(c, "2 C | 2 C", 1360, 440, 48, "g", COR, a))
    pilula_em(c, t, C["s10.e"] + 0.8, "compensação", 960, 880, 64, E.COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("fórmulas diferentes não são isômeros", "i", 62), XE + 450, 190, passo=0.1)
    PA, PB = par(c, t, C["s11.b"], C["s11.b"] + 0.4, PROPANO, PROPENO, None, y=500, nomes=("propano", "propeno"))
    Q.formula_em(c, t, C["s11.c"], "C3H8", 560, 820, 90, align="center", cores={"indice": ERRADO})
    Q.formula_em(c, t, C["s11.c"] + 0.6, "C3H6", 1360, 820, 90, align="center", cores={"indice": ERRADO})
    E.foco(c, t, C["s11.c"] + 1.0, 0.4, lambda a: centro(c, "≠", 960, 830, 110, "g", ERRADO, a))
    pilula_em(c, t, C["s11.d"], "confira a fórmula antes de tudo", 960, 980, 50, TINTA)


# ---------------- atalho (palco) ----------------
def caixa(c, t, t0, s, cx, cy, w=420, h=96, cor=None, tx=BR):
    E.foco(c, t, t0, 0.4, lambda a: (M.rrect(c, cx - w / 2, cy - h / 2, w, h, 30, cor or "#22232B", a), centro(c, s, cx, cy + 16, 44, "g", tx, a)))


def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"], ps("o atalho: a ordem das perguntas", "i", 64, CLARO), W / 2, 150, "center", 0.12)
        caixa(c, t, C["s12.b"], "mesma fórmula?", 330, 300, 400)
        caixa(c, t, C["s12.b"] + 0.5, "não: pare", 330, 430, 300, 80, "#3A1F24")
        caixa(c, t, C["s12.c"], "mesma função?", 900, 300, 400)
        caixa(c, t, C["s12.c"] + 0.5, "não: função", 900, 430, 340, 80, E.COR)
        caixa(c, t, C["s12.c"] + 1.4, "enol e C=O: tautomeria", 900, 540, 470, 80, E.COR)
        seta(c, t, C["s12.c"], 540, 300, 690, 300, E.CLARO)
        caixa(c, t, C["s12.d"], "mudou o quê?", 1520, 300, 400)
        seta(c, t, C["s12.d"], 1110, 300, 1310, 300, E.CLARO)
        for k, (key, s) in enumerate((("s12.e", "a cadeia: cadeia"), ("s12.f", "um grupo: posição"), ("s12.g", "heteroátomo: compensação"))):
            caixa(c, t, C[key], s, 1520, 430 + k * 120, 600, 84, E.COR)
        return
    E.frase(c, t, C["s13.a"], ps("cada tipo responde a uma pergunta, sempre na mesma ordem", "i", 58, CLARO), XE, 260, passo=0.08)
    E.frase(c, t, C["s13.b"], [("cuidado com o", "i", 64, CLARO), ("heteroátomo", "g", 64, BR)], XE, 440, passo=0.12)
    P = mol(c, t, C["s13.c"], EOXE, 960, 680, 130, escuro=True)
    halo(c, t, C["s13.c"] + 0.4, [P[2]], 50)
    pilula_em(c, t, C["s13.c"] + 0.8, "O mudou de lugar no éter: compensação, não posição", W / 2, 900, 46, E.COR)


# ---------------- questão ----------------
QP = ((PENTANO, DIMETILPROP, "pentano", "dimetilpropano"), (PROPANAL, PROPANONA, "propanal", "propanona"), (BUT1, BUT2, "but-1-eno", "but-2-eno"))


def linha_par(c, t, t0, k, y, esc=68, nomes=True):
    A, B, na, nb = QP[k]
    E.foco(c, t, t0, 0.4, lambda a: (E.bola(c, XE + 30, y, 36, a=a), centro(c, str(k + 1), XE + 30, y + 18, 44, "g", E.SOBRE, a)))
    PA = mol(c, t, t0, A, 560, y, esc, d=0.5)
    PB = mol(c, t, t0 + 0.3, B, 1100, y, esc, d=0.5)
    if nomes:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: (centro(c, na, 560, y + 112, 40, "g", TINTA2, a), centro(c, nb, 1100, y + 112, 40, "g", TINTA2, a)))
    return PA, PB


def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar: classifique os pares", "i", 66, COR), XE, 150, passo=0.1)
    for k, key in enumerate(("s14.a", "s14.b", "s14.c")):
        linha_par(c, t, C[key], k, 310 + k * 275)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=1600, cy=560, r=90)


def b_resposta(c, t, C, b):
    E.frase(c, t, C["s16"] - 0.4, ps("os pares", "i", 66, COR), XE, 160)
    Ps = [linha_par(c, t, C["s16"] - 0.4, k, 310 + k * 275) for k in range(3)]
    respostas = (("s16.a", "C5H12", "s16.c", "cadeia"), ("s17.a", "C3H6O", "s17.c", "função"), ("s18.a", "C4H8", "s18.c", "posição"))
    for k, (kf, f, kt, tipo) in enumerate(respostas):
        y = 310 + k * 275
        Q.formula_em(c, t, C[kf], f, 1330, y + 20, 56, cores={"indice": E.COR})
        pilula_em(c, t, C[kt], tipo, 1730, y, 56, E.COR)
    halo(c, t, C["s17.b"], [Ps[1][0][3], Ps[1][1][3]], 40)
    realce(c, t, C["s18.b"], Ps[2][0][0], Ps[2][0][1], largura=30)
    realce(c, t, C["s18.b"] + 0.3, Ps[2][1][1], Ps[2][1][2], largura=30)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s19.a"], [("isômeros:", "g", 62, COR), ("mesma fórmula, estruturas diferentes", "i", 60)], XE, 340, passo=0.1)
        E.frase(c, t, C["s19.b"], [("função diferente:", "g", 60), ("função", "g", 60, COR), ("ou", "i", 62), ("tautomeria", "g", 60, COR)], XE, 500, passo=0.12)
        E.frase(c, t, C["s19.c"], [("mesma função:", "g", 60), ("cadeia,", "g", 60, COR), ("posição", "g", 60, COR), ("ou", "i", 62), ("compensação", "g", 60, COR)],
                XE, 660, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("isomeria", "g", 100, COR), ("cis", "g", 100), ("e", "i", 100), ("trans", "g", 100)], XE, 400, passo=0.14)
    E.frase(c, t, C["s20.b"], [("as duas formas do", "i", 70), ("but-2-eno", "g", 70, COR)], XE, 540, passo=0.12)
    mol(c, t, C["s20.b"] + 0.4, BUT2, 600, 740, 110)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, isomero=b_isomero, funcao=b_funcao, mesma=b_mesma, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
