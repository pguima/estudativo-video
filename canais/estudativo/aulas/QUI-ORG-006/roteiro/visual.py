"""Visual — Estudativo · QUI-ORG-006: álcool, fenol e éter. Primeira aula do módulo Funções orgânicas.
Segue a linguagem da Química (QUI-MIS-001) e da Orgânica (QUI-ORG-001).
LINGUAGEM DO MÓDULO FUNÇÕES (QUI-ORG-006 a 011 copiam daqui):
- O GRUPO FUNCIONAL é marcado com halo() turquesa atrás do heteroátomo (e do carbono da carbonila, quando houver) e a pílula
  da função ao lado, fundo E.COR. Grupo já visto e que não é o da vez: halo cinza (CINZA). Nunca pinte a função só pela cor.
- VIZINHOS DO HETEROÁTOMO: anelc() turquesa em volta de cada vizinho que decide a função, um por vez, na fala; o vizinho que
  não decide fica sem anel.
- O ATALHO de cada aula é a tabela "vizinhos → função" no palco: Q.lewis pequeno à esquerda, a função na pílula à direita.
- Nome da função no fim do nome (ol, al, ona, oico, ato) em COR_TEXTO dentro do nome(); o resto em tinta.
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
ARQUIVO_FINAL = "estudativo_QUI-ORG-006_alcool_fenol_eter.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("funcao", "fenol", "eter", "erro", "atalho", "questao", "fim"))

Z3, Z4, Z5 = Q.zigzag(3), Q.zigzag(4), Q.zigzag(5)
HX = anel(6)
DUP = {(0, 1), (2, 3), (4, 5)}
ETANOL = dict(pts=Z3, rot={2: "OH"})
P1OL = dict(pts=Z4, rot={3: "OH"})
P2OL = dict(pts=Z3 + [(Z3[1][0], Z3[1][1] + 1)], ligs=[(0, 1), (1, 2), (1, 3)], rot={3: "OH"})
FENOL = dict(pts=HX + [(0, -2)], ligs=ligs_anel(0, 6) + [(0, 6)], duplas=DUP, rot={6: "OH"})
MOXE = dict(pts=Z4, rot={1: "O"})
EOXE = dict(pts=Z5, rot={2: "O"})
BENZ_OL = dict(pts=HX + [(0, -2), (0.87, -2.5)], ligs=ligs_anel(0, 6) + [(0, 6), (6, 7)], duplas=DUP, rot={7: "OH"})
CRESOL = dict(pts=HX + [(0, -2), (0, 2)], ligs=ligs_anel(0, 6) + [(0, 6), (3, 7)], duplas=DUP, rot={6: "OH"})
MOXP = dict(pts=Z5, rot={1: "O"})
assert Q.contar("CH3OCH2CH3") == Q.contar("C3H8O") and Q.contar("CH3OCH2CH2CH3") == Q.contar("C4H10O")
assert Q.contar("C6H5OH") == {"C": 6, "H": 6, "O": 1}


def grupo(c, t, t0, P, i, nome_f, dx=0, dy=-110, cor=None, t1=None, r=64):
    halo(c, t, t0, [P[i]], r, cor, t1=t1)
    if nome_f:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.pilula(c, nome_f, P[i][0] + dx, P[i][1] + dy, 48, "g", fundo=cor or E.COR, a=a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        trio = (("s01.a", "álcool da farmácia", ETANOL, 120, 2), ("s01.b", "desinfetante antigo", FENOL, 70, 6), ("s01.c", "anestésico", EOXE, 95, 2))
        for k, (key, s, M_, esc, io) in enumerate(trio):
            cx = 360 + k * 600
            pilula_em(c, t, C[key], s, cx, 260, 48, TINTA, "i")
            P = mol(c, t, C[key] + 0.2, M_, cx, 520 if k != 1 else 560, esc, d=0.6)
            halo(c, t, C["s01.d"] + 0.3 * k, [P[io]], 60)
        E.frase(c, t, C["s01.d"], [("oxigênio", "g", 70, Q.cor_el("O")), ("só com ligações simples", "i", 70)], W / 2, 860, "center", 0.12)
        E.frase(c, t, C["s01.e"], [("muda", "i", 70), ("quem está do lado", "g", 66, COR)], W / 2, 980, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 520, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("álcool,", "g", 70, COR), ("fenol", "g", 70, COR), ("ou", "i", 74), ("éter?", "g", 70, COR)]),
                 (C["s02.c"], [("dar nome ao", "i", 74), ("etanol", "g", 70)]),
                 (C["s02.d"], [("e ao", "i", 74), ("metoxietano", "g", 70)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula passada", "i", 76, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("prefixo", "g", 90, COR), ("+", "g", 80, TINTA2), ("infixo", "g", 90), ("+", "g", 80, TINTA2), ("sufixo", "g", 90, TINTA2)], XE, 400, passo=0.2)
    nome(c, t, C["s03.b"], [("et", COR, "2 C"), ("an", TINTA, "simples"), ("o", TINTA2, None)], XE, 620, 110, 0.3)
    mol(c, t, C["s03.c"], dict(pts=HX, ligs=ligs_anel(0, 6), duplas=DUP), 1450, 560, 150)
    E.foco(c, t, C["s03.c"] + 0.4, 0.4, lambda a: centro(c, "benzeno", 1450, 840, 64, "g", COR, a))


# ---------------- função orgânica ----------------
def b_funcao(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("função orgânica", "g", 80, COR), ("=", "g", 76, TINTA2), ("uma família", "i", 80)], XE, 230, passo=0.12)
    E.frase(c, t, C["s04.b"], [("o pedaço em comum:", "i", 66), ("grupo funcional", "g", 66, COR)], XE, 360, passo=0.12)
    E.frase(c, t, C["s04.c"], ps("mesmo grupo, comportamento parecido", "i", 58, TINTA2), XE, 460, passo=0.1)
    Q.lewis(c, t, C["s04.d"], [("C", -1.0, 0.45), ("O", 0, 0, [90, 270]), ("H", 1.0, 0.45)], [(0, 1, 1), (1, 2, 1)], 1000, 720, escala=150, size=110)
    E.foco(c, t, C["s04.e"], 0.4, lambda a: E.escreve(c, "2 ligações simples", 1250, 760, 66, "g", COR, a))
    halo(c, t, C["s04.d"] + 0.4, [(1000, 720)], 80)


# ---------------- álcool ----------------
def b_alcool(c, t, C, b):
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("álcool:", "g", 80, COR), ("OH", "g", 76, Q.cor_el("O")), ("num carbono de cadeia", "i", 70)], XE, 220, passo=0.12)
        E.frase(c, t, C["s05.b"], ps("que só faz ligações simples", "i", 62, TINTA2), XE, 320, passo=0.1)
        P = mol(c, t, C["s05.a"] + 0.4, ETANOL, 1450, 560, 170)
        grupo(c, t, C["s05.a"] + 1.0, P, 2, "álcool", dy=-120)
        anelc(c, t, C["s05.b"], P, 1, 30)
        E.frase(c, t, C["s05.c"], [("o", "g", 70, TINTA2), ("do fim vira", "i", 66), ("ol", "g", 70, COR)], XE, 520, passo=0.12)
        nome(c, t, C["s05.d"], [("et", TINTA, "2 C"), ("an", TINTA, None), ("ol", COR, "álcool")], XE, 720, 130, 0.3)
        cond(c, t, C["s05.e"], ["CH3", "CH2", "OH"], XE, 940, 84, cores={2: Q.cor_el("O")})
        return
    E.frase(c, t, C["s06.a"], ps("com 3 carbonos ou mais: um número", "i", 66), XE, 220, passo=0.1)
    P1 = mol(c, t, C["s06.b"], P1OL, 600, 560, 140)
    grupo(c, t, C["s06.b"] + 0.4, P1, 3, None)
    nome(c, t, C["s06.b"] + 0.4, [("propan-", TINTA, None), ("1-", TINTA2, "na ponta"), ("ol", COR, None)], 330, 850, 90, 0.2)
    P2 = mol(c, t, C["s06.c"], P2OL, 1400, 520, 140)
    grupo(c, t, C["s06.c"] + 0.4, P2, 3, None)
    nome(c, t, C["s06.c"] + 0.4, [("propan-", TINTA, None), ("2-", TINTA2, "no meio"), ("ol", COR, None)], 1130, 850, 90, 0.2)
    pilula_em(c, t, C["s06.d"], "álcool isopropílico: limpa telas", 1400, 330, 44, TINTA, "b")


# ---------------- fenol ----------------
def b_fenol(c, t, C, b):
    E.frase(c, t, C["s07.a"], [("fenol:", "g", 80, COR), ("OH", "g", 76, Q.cor_el("O")), ("direto no anel aromático", "i", 66)], XE, 220, passo=0.12)
    P = mol(c, t, C["s07.a"] + 0.5, FENOL, 1400, 620, 150)
    grupo(c, t, C["s07.a"] + 1.4, P, 6, "fenol", dx=180, dy=0)
    anelc(c, t, C["s07.a"] + 1.8, P, 0, 30)
    E.frase(c, t, C["s07.b"], ps("o mais simples:", "i", 64), XE, 420, passo=0.1)
    E.foco(c, t, C["s07.b"] + 0.7, 0.4, lambda a: E.escreve(c, "fenol", XE, 560, 110, "g", COR, a))
    Q.formula_em(c, t, C["s07.c"], "C6H5OH", XE, 700, 90)
    pilula_em(c, t, C["s07.d"], "desinfetante antigo · tóxico", XE + 330, 860, 44, TINTA, "b")


# ---------------- éter ----------------
def b_eter(c, t, C, b):
    E.frase(c, t, C["s08.a"], [("éter:", "g", 80, COR), ("O", "g", 76, Q.cor_el("O")), ("entre dois carbonos", "i", 70)], XE, 220, passo=0.12)
    if t < C["s10"]:
        P = mol(c, t, C["s08.a"] + 0.4, MOXE, 1400, 470, 170)
        grupo(c, t, C["s08.a"] + 1.0, P, 1, "éter", dy=-110)
        anelc(c, t, C["s08.a"] + 1.4, P, 0, 30); anelc(c, t, C["s08.a"] + 1.6, P, 2, 30)
        cond(c, t, C["s08.b"], ["CH3", "O", "CH2", "CH3"], XE, 400, 76, cores={1: Q.cor_el("O")}, passo=0.2)
        E.frase(c, t, C["s08.c"], ps("separe os lados do oxigênio", "i", 60, TINTA2), XE, 520, passo=0.1)
        if t >= C["s09"]:
            realce(c, t, C["s09.a"], P[0], P[1], CINZA, alfa=0.6)
            E.foco(c, t, C["s09.b"], 0.4, lambda a: centro(c, "1 C", P[0][0], P[0][1] - 60, 50, "g", TINTA2, a))
            realca_fila(c, t, C["s09.c"], P, [1, 2, 3])
            E.foco(c, t, C["s09.d"], 0.4, lambda a: centro(c, "2 C", P[3][0], P[3][1] - 60, 50, "g", COR, a))
            E.frase(c, t, C["s09.a"], [("lado menor", "g", 60, TINTA2), ("+ óxi", "g", 60)], XE, 660, passo=0.1)
            E.frase(c, t, C["s09.c"], [("lado maior", "g", 60, COR), ("= hidrocarboneto", "i", 60)], XE, 760, passo=0.1)
            nome(c, t, C["s09.e"], [("met", TINTA2, "1 C"), ("óxi", COR, "éter"), ("etano", TINTA, "2 C")], XE, 940, 120, 0.3)
        return
    P = mol(c, t, C["s10.a"], EOXE, 1300, 520, 160)
    grupo(c, t, C["s10.a"] + 0.6, P, 2, "éter", dy=-110)
    E.frase(c, t, C["s10.a"], ps("o éter dos anestésicos", "i", 64, TINTA2), XE, 340, passo=0.1)
    nome(c, t, C["s10.b"], [("et", TINTA2, "2 C"), ("óxi", COR, None), ("etano", TINTA, "2 C")], XE, 800, 120, 0.3)
    pilula_em(c, t, C["s10.c"], "éter etílico, ou só éter", 1350, 930, 46, TINTA, "b")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("todo OH perto de anel é fenol?", "i", 66), XE + 450, 190, passo=0.1)
    P = mol(c, t, C["s11"] + 0.3, BENZ_OL, 1350, 640, 140)

    def errado():
        E.foco(c, t, C["s11.a"] + 0.8, 0.4, lambda a: E.escreve(c, "fenol?", XE, 520, 100, "g", ERRADO, a))
        if t >= C["s11.a"] + 1.6:
            E.risco(c, XE - 10, 540, XE + 330, 460, t, C["s11.a"] + 1.6, largura=10)
    E.saida(c, t, C["s11.d"], errado)
    anelc(c, t, C["s11.b"], P, 6, 30)
    E.foco(c, t, C["s11.b"] + 0.3, 0.4, lambda a: Q.formula(c, "CH2", P[6][0] - 50, P[6][1] + 18, 54, COR, a, "right"))
    anelc(c, t, C["s11.c"], P, 0, 30, CINZA)
    E.foco(c, t, C["s11.c"] + 0.3, 0.4, lambda a: E.escreve(c, "o C do OH não é do anel", XE, 700, 56, "i", TINTA2, a))
    grupo(c, t, C["s11.d"], P, 7, "álcool", dx=0, dy=-110)
    E.foco(c, t, C["s11.d"], 0.4, lambda a: E.escreve(c, "álcool", XE, 520, 100, "g", COR, a))
    E.foco(c, t, C["s11.d"] + 0.4, 0.4, lambda a: E.selo(c, XE + 420, 485, 46, True, a))
    E.frase(c, t, C["s12.a"], [("fenol:", "g", 64, COR), ("só com o OH", "i", 66), ("no próprio anel", "g", 62)], XE, 900, passo=0.12)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], [("o atalho:", "i", 70, CLARO), ("os 2 vizinhos do O", "g", 70, BR)], W / 2, 180, "center", 0.12)
        linhas = (("s13.b", [("H", 0.0, 0), ("O", 1.0, 0), ("C", 2.0, 0)], "H + C de cadeia", "álcool"),
                  ("s13.c", [("H", 0.0, 0), ("O", 1.0, 0), ("C", 2.0, 0)], "H + C do anel", "fenol"),
                  ("s13.d", [("C", 0.0, 0), ("O", 1.0, 0), ("C", 2.0, 0)], "C + C", "éter"))
        for k, (key, ats, txt, fn) in enumerate(linhas):
            y = 380 + k * 210
            Q.lewis(c, t, C[key], ats, [(0, 1, 1), (1, 2, 1)], XE + 60, y, escala=130, size=90, escuro=True, passo=0.1)
            if k == 1:
                E.foco(c, t, C[key] + 0.4, 0.4, lambda a, y=y: Q.bastao(c, 99, 0, anel(6, 0.5, 90, 0, 0), XE + 60 + 2 * 130 + 110, y, 110, ligacoes=ligs_anel(0, 6), escuro=True, largura=5))
            E.foco(c, t, C[key] + 0.5, 0.4, lambda a, txt=txt, y=y: E.escreve(c, txt, 900, y + 20, 56, "i", CLARO, a))
            pilula_em(c, t, C[key] + 0.8, fn, 1600, y, 62, E.COR, "g")
        return
    E.frase(c, t, C["s14.a"], ps("o oxigênio faz 2 ligações:", "i", 70, CLARO), XE, 300, passo=0.12)
    E.frase(c, t, C["s14.a"] + 1.4, ps("as 3 funções só mudam quem ocupa cada uma", "i", 60, CLARO), XE, 400, passo=0.08)
    E.frase(c, t, C["s14.b"], [("não vale", "g", 66, ERRADO), ("com dupla no oxigênio", "i", 66, CLARO)], XE, 620, passo=0.12)
    Q.lewis(c, t, C["s14.b"] + 0.5, [("C", 0, 0), ("O", 1.2, 0)], [(0, 1, 2)], 1400, 620, escala=150, size=110, escuro=True)
    pilula_em(c, t, C["s14.c"], "outra família: a próxima aula", W / 2, 840, 50, TINTA2)


# ---------------- questão ----------------
QY = 480


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    for k, (M_, esc) in enumerate(((P1OL, 110), (CRESOL, 80), (MOXP, 100))):
        cx = 360 + k * 600
        E.foco(c, t, C["s15.a"] + 0.3 * k, 0.4, lambda a, cx=cx, k=k: (E.bola(c, cx - 200, 300, 36, a=a), centro(c, "ABC"[k], cx - 200, 318, 44, "g", E.SOBRE, a)))
        mol(c, t, C["s15.a"] + 0.3 * k, M_, cx, QY + (40 if k == 1 else 0), esc, d=0.6)
    E.frase(c, t, C["s15.a"] + 1.0, ps("álcool, fenol ou éter?", "i", 66), XE, 840, passo=0.1)
    E.frase(c, t, C["s15.b"], ps("e o nome do éter?", "i", 66), XE, 950, passo=0.1)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1600, cy=850, r=70)


def b_resposta(c, t, C, b):
    Ps = []
    for k, (M_, esc) in enumerate(((P1OL, 110), (CRESOL, 80), (MOXP, 100))):
        cx = 360 + k * 600
        E.foco(c, t, C["s17"] - 0.4, 0.4, lambda a, cx=cx, k=k: (E.bola(c, cx - 200, 300, 36, a=a), centro(c, "ABC"[k], cx - 200, 318, 44, "g", E.SOBRE, a)))
        Ps.append(mol(c, t, C["s17"] - 0.4, M_, cx, QY + (40 if k == 1 else 0), esc, d=0.1))
    for k, (key, i, fn) in enumerate((("s17.a", 3, "álcool"), ("s17.b", 6, "fenol"), ("s17.c", 1, "éter"))):
        grupo(c, t, C[key], Ps[k], i, None, r=50)
        pilula_em(c, t, C[key] + 0.3, fn, 360 + k * 600, 760, 56, E.COR)
    E.foco(c, t, C["s17.a"] + 0.6, 0.4, lambda a: centro(c, "propan-1-ol", 360, 860, 50, "g", TINTA, a))
    if t >= C["s18"]:
        realce(c, t, C["s18.b"], Ps[2][0], Ps[2][1], CINZA, alfa=0.6)
        realca_fila(c, t, C["s18.c"], Ps[2], [1, 2, 3, 4])
        nome(c, t, C["s18.d"], [("met", TINTA2, None), ("óxi", COR, None), ("propano", TINTA, None)], 1560, 880, 76, 0.25, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo:", "i", 80, COR), ("os vizinhos do O", "g", 74)], XE, 200, passo=0.12)
        for k, (key, viz, fn, suf) in enumerate((("s19.a", "H + cadeia", "álcool", "ol"), ("s19.b", "H + anel aromático", "fenol", ""), ("s19.c", "C + C", "éter", "óxi"))):
            y = 400 + k * 180
            E.foco(c, t, C[key], 0.4, lambda a, viz=viz, y=y: E.escreve(c, viz, XE, y, 66, "g", TINTA, a))
            pilula_em(c, t, C[key] + 0.3, fn, 1100, y - 22, 60, E.COR)
            if suf:
                E.foco(c, t, C[key] + 0.5, 0.4, lambda a, suf=suf, y=y: E.escreve(c, suf, 1400, y, 66, "g", COR, a))
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("aldeído", "g", 96, COR), ("e", "i", 96), ("cetona", "g", 96, COR)], XE, 400, passo=0.14)
    Q.lewis(c, t, C["s20"] + 0.5, [("C", 0, 0), ("O", 1.2, 0)], [(0, 1, 2)], XE + 100, 600, escala=150, size=100)
    E.frase(c, t, C["s20.b"], [("etanal", "g", 76), ("e", "i", 76), ("propanona", "g", 76)], XE, 820, passo=0.14)
    E.foco(c, t, C["s20.c"] + 0.3, 0.4, lambda a: E.escreve(c, "a acetona", XE + 520, 900, 56, "i", TINTA2, a))
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.d"] + 0.2, 0.4))
    E.frase(c, t, C["s20.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, funcao=b_funcao, alcool=b_alcool, fenol=b_fenol, eter=b_eter, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
