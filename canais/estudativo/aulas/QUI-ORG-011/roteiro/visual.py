"""Visual — Estudativo · QUI-ORG-011: praticando, achar as funções em moléculas reais (5 questões).
Segue a linguagem da Química (QUI-MIS-001), da Orgânica (QUI-ORG-001) e do módulo Funções (QUI-ORG-006): cada função achada
ganha halo() turquesa e uma pílula com o nome ao lado; as já achadas ficam com halo cinza enquanto a fala passa para a próxima.
As estruturas reais (vanilina, aspirina, adrenalina, cloranfenicol, penicilina G) estão em bastão, desenhadas aqui ponto a ponto.
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
ARQUIVO_FINAL = "estudativo_QUI-ORG-011_funcoes_moleculas_reais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "q5", "fim"))

HX = anel(6)
RD = ligs_anel(0, 6)
DUP = {(0, 1), (2, 3), (4, 5)}
VANILINA = dict(pts=HX + [(0, -2), (0.87, -2.5), (0, 2), (-1.74, 1.0), (-2.61, 0.5)], ligs=RD + [(0, 6), (6, 7), (3, 8), (2, 9), (9, 10)],
                duplas=DUP | {(6, 7)}, rot={7: "O", 8: "OH", 9: "O"})
ASPIRINA = dict(pts=HX + [(0, -2), (-0.87, -2.5), (0.87, -2.5), (-1.74, -1.0), (-2.61, -0.5), (-2.61, 0.5), (-3.48, -1.0)],
                ligs=RD + [(0, 6), (6, 7), (6, 8), (1, 9), (9, 10), (10, 11), (10, 12)], duplas=DUP | {(6, 7), (10, 11)},
                rot={7: "O", 8: "OH", 9: "O", 11: "O"})
ADRENALINA = dict(pts=HX + [(0, -2), (-0.87, -2.5), (0.87, -2.5), (1.74, -2.0), (2.61, -2.5), (0, 2), (1.74, 1.0)],
                  ligs=RD + [(0, 6), (6, 7), (6, 8), (8, 9), (9, 10), (3, 11), (4, 12)], duplas=DUP, rot={7: "OH", 9: "NH", 11: "OH", 12: "OH"})
RX = anel(6, 1, 0)
CLORAN = dict(pts=RX + [(-2, 0), (1.87, -0.5), (1.87, -1.5), (2.74, 0), (2.74, 1.0), (3.61, 1.5), (3.61, 2.5), (4.48, 1.0), (4.48, 0.0), (5.35, 1.5),
                        (3.61, -0.5), (3.61, -1.5)],
              ligs=RD + [(3, 6), (0, 7), (7, 8), (7, 9), (9, 10), (10, 11), (11, 12), (11, 13), (13, 14), (13, 15), (9, 16), (16, 17)],
              duplas=DUP | {(11, 12)}, rot={6: "O2N", 8: "OH", 10: "NH", 12: "O", 14: "Cl", 15: "Cl", 17: "OH"})
PH = anel(6, 1, 0, -4.2, 0)
PENI = dict(pts=PH + [(-2.33, -0.5), (-1.46, 0), (-1.46, 1.0), (-0.59, -0.5), (0.28, 0), (1.28, 0), (1.28, 1.0), (0.28, 1.0), (-0.45, 1.7),
                      (2.23, -0.31), (2.82, 0.5), (2.23, 1.31), (3.8, 0.75), (3.3, -0.35), (2.6, 2.25), (3.55, 2.55), (1.95, 3.0)],
            ligs=RD + [(0, 6), (6, 7), (7, 8), (7, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 10), (13, 14), (11, 15), (15, 16), (16, 17),
                       (17, 12), (16, 18), (16, 19), (17, 20), (20, 21), (20, 22)],
            duplas=DUP | {(7, 8), (13, 14), (20, 21)}, rot={8: "O", 9: "NH", 12: "N", 14: "O", 15: "S", 21: "O", 22: "OH"})


def ncarb(M_):
    return len([i for i in range(len(M_["pts"])) if i not in M_["rot"]])


assert ncarb(VANILINA) == 8 and ncarb(ASPIRINA) == 9 and ncarb(ADRENALINA) == 9 and ncarb(CLORAN) == 11 and ncarb(PENI) == 16
# vanilina C8H8O3, aspirina C9H8O4, adrenalina C9H13NO3, cloranfenicol C11H12Cl2N2O5, penicilina G C16H18N2O4S


def titulo_q(c, t, t0, n, txt):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 170, 56, a=a), centro(c, str(n), XE + 50, 196, 72, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.2, [(txt, "i", 64, TINTA2)], XE + 140, 192)


def achou(c, t, t0, P, idx, fn, dx, dy, r=46, t1=None, size=46):
    """halo no grupo e pílula da função; depois de t1 o halo fica cinza"""
    if t1 is not None and t >= t1:
        halo(c, t, t0, [P[i] for i in idx], r, CINZA)
    else:
        halo(c, t, t0, [P[i] for i in idx], r)
    cx, cy = P[idx[0]][0] + dx, P[idx[0]][1] + dy
    pilula_em(c, t, t0 + 0.3, fn, cx, cy, size, E.COR)


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    for k, (key, s, M_, esc) in enumerate((("s01.a", "comprimido para dor", ASPIRINA, 55), ("s01.b", "hormônio do susto", ADRENALINA, 55),
                                          ("s01.c", "antibiótico", PENI, 40))):
        cx = 340 + k * 620
        pilula_em(c, t, C[key], s, cx, 260, 46, TINTA, "i")
        mol(c, t, C[key] + 0.2, M_, cx + (60 if k == 2 else 0), 560, esc, d=0.7, size=esc * 0.6)
    E.frase(c, t, C["s01.d"], [("quais", "i", 80), ("funções", "g", 80, COR), ("estão aí?", "i", 80)], W / 2, 920, "center", 0.12)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("as funções das últimas cinco aulas", "i", 70, TINTA2), XE, 220, passo=0.1)
    E.frase(c, t, C["s02.a"], [("o método:", "g", 80, COR)], XE, 380)
    lista(c, t, [(C["s02.b"], [("ache cada átomo", "i", 70), ("que não é C nem H", "g", 66)]),
                 (C["s02.c"], [("olhe os", "i", 70), ("vizinhos", "g", 66, COR)])], XE, 540, 160)
    E.foco(c, t, C["s02.d"], 0.5, lambda a: E.pilula(c, "pause em cada questão", 1450, 920, 54, "g", fundo=E.COR, a=a))


# ---------------- questões ----------------
def questao(c, t, C, sid, n, txt, M_, cx, cy, esc, perg, pausa, size=None):
    titulo_q(c, t, C[sid], n, txt)
    mol(c, t, C[sid + ".b"], M_, cx, cy, esc, size=size)
    for k, (key, s) in enumerate(perg):
        E.frase(c, t, C[key], ps(s, "i", 58), XE, 820 + k * 90, passo=0.08)
    if t >= C[pausa]:
        E.relogio(c, t, C[pausa + ".a"], cx=1700, cy=880, r=70)


VX, VY, VE = 1350, 560, 100


def b_q1(c, t, C, b):
    questao(c, t, C, "s03", 1, "o sabor de baunilha", VANILINA, VX, VY, VE, [("s03.c", "três grupos com oxigênio"), ("s03.d", "quais são as funções?")], "s04")
    E.frase(c, t, C["s03.b"], [("vanilina", "g", 70, COR)], XE, 340)


def b_r1(c, t, C, b):
    P = mol(c, t, C["s05"] - 0.4, VANILINA, VX, VY, VE)
    titulo_q(c, t, C["s05"] - 0.4, 1, "vanilina")
    achou(c, t, C["s05.a"], P, (6, 7), "aldeído", 230, -10, t1=C["s05.b"])
    achou(c, t, C["s05.b"], P, (8,), "fenol", 200, 0, t1=C["s05.c"])
    achou(c, t, C["s05.c"], P, (9,), "éter", -210, 40, t1=C["s05.d"])
    for k, s in enumerate(("aldeído", "fenol", "éter")):
        pilula_esq(c, t, C["s05.d"] + 0.3 * k, s, XE, 400 + k * 130, 60, E.COR, "g")


AX, AY, AE = 1350, 520, 105


def b_q2(c, t, C, b):
    questao(c, t, C, "s06", 2, "um comprimido para dor", ASPIRINA, AX, AY, AE, [("s06.c", "quais são as duas funções com oxigênio?")], "s07")
    E.frase(c, t, C["s06.b"], [("aspirina", "g", 70, COR)], XE, 340)
    E.foco(c, t, C["s06.b"] + 0.8, 0.4, lambda a: E.escreve(c, "ácido acetilsalicílico", XE, 420, 48, "i", TINTA2, a))


def b_r2(c, t, C, b):
    P = mol(c, t, C["s08"] - 0.4, ASPIRINA, AX, AY, AE)
    titulo_q(c, t, C["s08"] - 0.4, 2, "aspirina")
    achou(c, t, C["s08.a"], P, (6, 7, 8), "ácido carboxílico", 120, -130, t1=C["s08.c"])
    achou(c, t, C["s08.c"], P, (9, 10, 11), "éster", -230, 150)
    anelc(c, t, C["s08.d"], P, 9, 40)
    if t >= C["s09"]:
        anelc(c, t, C["s09.a"], P, 1, 30, ERRADO, t1=C["s09.b"] + 1.0)
        E.frase(c, t, C["s09.a"], [("pegadinha:", "g", 60, ERRADO), ("O no anel...", "i", 60)], XE, 400, passo=0.1)
        E.frase(c, t, C["s09.b"], [("fenol precisa de", "i", 60), ("OH", "g", 58, Q.cor_el("O"))], XE, 520, passo=0.1)
        E.frase(c, t, C["s09.c"], [("aqui, o O", "i", 60), ("não tem H", "g", 58, COR)], XE, 640, passo=0.1)
        E.foco(c, t, C["s09.c"] + 0.6, 0.4, lambda a: E.selo(c, XE + 640, 620, 44, True, a))


DX, DY, DE = 1300, 560, 100


def b_q3(c, t, C, b):
    questao(c, t, C, "s10", 3, "o hormônio do susto", ADRENALINA, DX, DY, DE, [("s10.c", "três oxigênios e um nitrogênio"), ("s10.d", "marque todas as funções")], "s11")
    E.frase(c, t, C["s10.b"], [("adrenalina", "g", 70, COR)], XE, 340)


def b_r3(c, t, C, b):
    P = mol(c, t, C["s12"] - 0.4, ADRENALINA, DX, DY, DE)
    titulo_q(c, t, C["s12"] - 0.4, 3, "adrenalina")
    achou(c, t, C["s12.a"], P, (11, 12), "fenol", 260, 60, t1=C["s12.b"])
    achou(c, t, C["s12.b"], P, (7,), "álcool", -210, 0, t1=C["s12.c"])
    achou(c, t, C["s12.c"], P, (9,), "amina", 60, -110)
    for k, s in enumerate(("fenol", "álcool", "amina")):
        pilula_esq(c, t, C["s13.a"] + 0.3 * k, s, XE, 400 + k * 130, 60, E.COR, "g")
    E.frase(c, t, C["s13.b"], ps("os OH parecem iguais: o vizinho decide", "i", 54, TINTA2), XE, 900, passo=0.08)


KX, KY, KE = 1160, 560, 95


def b_q4(c, t, C, b):
    questao(c, t, C, "s14", 4, "um colírio antibiótico", CLORAN, KX, KY, KE, [("s14.c", "cloro, nitrogênio e oxigênio"), ("s14.d", "quais funções aparecem?")], "s15", size=44)
    E.frase(c, t, C["s14.b"], [("cloranfenicol", "g", 66, COR)], XE, 330)


def b_r4(c, t, C, b):
    P = mol(c, t, C["s16"] - 0.4, CLORAN, KX, KY, KE, size=44)
    titulo_q(c, t, C["s16"] - 0.4, 4, "cloranfenicol")
    achou(c, t, C["s16.a"], P, (6,), "nitrocomposto", 0, 110, t1=C["s16.b"], size=40)
    achou(c, t, C["s16.b"], P, (8, 17), "álcool", 0, -90, t1=C["s16.c"], size=40)
    achou(c, t, C["s16.c"], P, (10, 11, 12), "amida", -150, 60, t1=C["s16.d"], size=40)
    achou(c, t, C["s16.d"], P, (14, 15), "haleto", 120, -90, size=40)
    if t >= C["s17"]:
        for k, s in enumerate(("nitrocomposto", "álcool", "amida", "haleto")):
            pilula_esq(c, t, C["s17.a"] + 0.25 * k, s, XE + [0, 440, 760, 1060][k], 880, 50, E.COR, "g")
        E.frase(c, t, C["s17.b"], ps("o N aparece duas vezes, em funções diferentes", "i", 52, TINTA2), XE, 1000, passo=0.08)


NX, NY, NE = 1180, 540, 95


def b_q5(c, t, C, b):
    questao(c, t, C, "s18", 5, "a mais difícil", PENI, NX, NY, NE, [("s18.c", "oxigênio, nitrogênio e enxofre"), ("s18.d", "quais funções aparecem?")], "s19", size=44)
    E.frase(c, t, C["s18.b"], [("penicilina", "g", 70, COR)], XE, 330)
    E.foco(c, t, C["s18.b"] + 0.8, 0.4, lambda a: E.escreve(c, "descoberta em 1928", XE, 410, 46, "i", TINTA2, a))


def b_r5(c, t, C, b):
    P = mol(c, t, C["s20"] - 0.4, PENI, NX, NY, NE, size=44)
    titulo_q(c, t, C["s20"] - 0.4, 5, "penicilina")
    tf = C["s22"]
    achou(c, t, C["s20.b"], P, (9, 7, 8), "amida", -40, -110, t1=tf, size=40)
    achou(c, t, C["s20.c"], P, (12, 13, 14), "amida", -120, 140, t1=tf if t < C["s22.b"] else None, size=40)
    achou(c, t, C["s21.a"], P, (20, 21, 22), "ácido carboxílico", 300, -40, t1=tf, size=40)
    achou(c, t, C["s21.b"], P, (15,), "tioéter", 40, -100, t1=tf, size=40)
    if t >= C["s22"]:
        for k, s in enumerate(("2 amidas", "ácido carboxílico", "tioéter")):
            pilula_esq(c, t, C["s22.a"] + 0.25 * k, s, XE + [0, 320, 800][k], 900, 50, E.COR, "g")
        E.frase(c, t, C["s22.b"], ps("a amida do anel de 4 átomos ataca a parede da bactéria", "i", 50, TINTA2), XE, 1010, passo=0.07)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("o método", "i", 92, COR)], W / 2, 180, "center")
        lista(c, t, [(C["s23.a"], [("ache cada átomo", "i", 66), ("que não é C nem H", "g", 62)]),
                     (C["s23.b"], [("olhe os", "i", 66), ("vizinhos", "g", 62, COR)]),
                     (C["s23.c"], [("dê o nome", "g", 62), ("da função", "i", 66)])], XE, 360, 140)
        for k, s in enumerate(("fenol × álcool", "amida × amina", "éster × éter")):
            pilula_esq(c, t, C["s23.d"] + 0.4 * k, s, XE + k * 520, 860, 50, TINTA, "g")
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], [("próximo", "i", 80), ("módulo", "i", 80)], XE, 250)
    E.frase(c, t, C["s24.a"], [("ponto de ebulição", "g", 90, COR)], XE, 400)
    E.frase(c, t, C["s24.a"] + 0.8, ps("álcool e ácido acima do hidrocarboneto", "i", 64), XE, 510, passo=0.1)
    E.frase(c, t, C["s24.b"], ps("e por que os galhos baixam esse valor", "i", 64), XE, 620, passo=0.1)
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4, q5=b_q5, r5=b_r5,
              fim=b_fim)
