"""Visual — Estudativo · QUI-ORG-008: ácido carboxílico e éster.
Segue a linguagem da Química (QUI-MIS-001), da Orgânica (QUI-ORG-001) e do módulo Funções (QUI-ORG-006). Nesta aula: o
grupo inteiro (carbonila + o segundo oxigênio) ganha um halo só; o "segundo oxigênio" ganha anelc() na hora em que a fala o
usa para separar ácido (com H) de éster (com C). O corte do nome do éster é um traço tracejado vertical no oxigênio simples:
o lado da carbonila em COR_TEXTO ("ato"), o outro em tinta ("ila").
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
ARQUIVO_FINAL = "estudativo_QUI-ORG-008_acido_carboxilico_ester.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("acido", "ester", "aroma", "erro", "atalho", "questao", "fim"))


def zf(n):
    return [(x, -y) for x, y in Q.zigzag(n)]


Z3f, Z4f, Z5f, Z4 = zf(3), zf(4), zf(5), Q.zigzag(4)
ETANAL = dict(pts=Z3f + [(Z3f[1][0], Z3f[1][1] - 1)], ligs=[(0, 1), (1, 3)], duplas={(1, 3)}, rot={3: "O"})
ACETICO = dict(pts=Z3f + [(Z3f[1][0], Z3f[1][1] - 1)], ligs=[(0, 1), (1, 2), (1, 3)], duplas={(1, 3)}, rot={2: "OH", 3: "O"})
ET_ET = dict(pts=Z5f + [(Z5f[1][0], Z5f[1][1] - 1)], ligs=[(0, 1), (1, 2), (2, 3), (3, 4), (1, 5)], duplas={(1, 5)}, rot={2: "O", 5: "O"})
ET_ME = dict(pts=Z4f + [(Z4f[1][0], Z4f[1][1] - 1)], ligs=[(0, 1), (1, 2), (2, 3), (1, 4)], duplas={(1, 4)}, rot={2: "O", 4: "O"})
PROPANOICO = dict(pts=Z4 + [(Z4[2][0], Z4[2][1] - 1)], ligs=[(0, 1), (1, 2), (2, 3), (2, 4)], duplas={(2, 4)}, rot={3: "OH", 4: "O"})
ETER = dict(pts=Q.zigzag(5), rot={2: "O"})
assert Q.contar("CH3COOH") == {"C": 2, "H": 4, "O": 2} and Q.contar("CH3COOCH2CH3") == {"C": 4, "H": 8, "O": 2}
assert Q.contar("CH3CH2COOH") == Q.contar("CH3COOCH3") == {"C": 3, "H": 6, "O": 2}


def grupo_c(c, t, t0, P, ic, io1, io2, r=56, cor=None, t1=None):
    halo(c, t, t0, [P[ic], P[io1], P[io2]], r, cor, t1=t1)


def corte(c, t, t0, P, i, h=150, cor=None):
    p = ep(t, t0, 0.4)
    if p > 0:
        pt = M.paint(cor or E.COR, p, stroke=5)
        pt.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
        pth = skia.Path(); pth.moveTo(P[i][0], P[i][1] - h); pth.lineTo(P[i][0], P[i][1] + h)
        c.drawPath(pth, pt)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        pilula_em(c, t, C["s01.a"], "vinagre: azedo", 560, 280, 50, TINTA, "i")
        P1 = mol(c, t, C["s01.a"] + 0.3, ACETICO, 560, 560, 150)
        pilula_em(c, t, C["s01.b"], "banana: perfume", 1400, 280, 50, TINTA, "i")
        P2 = mol(c, t, C["s01.b"] + 0.3, ET_ET, 1400, 560, 130)
        grupo_c(c, t, C["s01.c"], P1, 1, 2, 3, 46); grupo_c(c, t, C["s01.c"] + 0.3, P2, 1, 2, 5, 46)
        anelc(c, t, C["s01.d"], P1, 2, 46); anelc(c, t, C["s01.d"] + 0.3, P2, 3, 30)
        E.frase(c, t, C["s01.c"] + 0.6, ps("quase o mesmo grupo", "i", 70), W / 2, 880, "center", 0.12)
        E.frase(c, t, C["s01.d"], ps("a diferença: o que ocupa o lugar de um H", "i", 60, TINTA2), W / 2, 990, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 520, 240 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 220, passo=0.14)
    lista(c, t, [(C["s02.b"], [("o grupo do", "i", 70), ("ácido", "g", 66, COR), ("e o do", "i", 70), ("éster", "g", 66, COR)]),
                 (C["s02.d"], [("ácido etanoico", "g", 66)]),
                 (C["s02.e"], [("etanoato de etila", "g", 66)]),
                 (C["s02.f"], [("por que", "i", 70), ("o éster tem cheiro", "g", 66, COR)])], XE, 380, 150)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("das aulas passadas", "i", 76, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("carbonila", "g", 76, COR), ("=", "g", 70, TINTA2), ("C=O", "g", 76)], XE, 380, passo=0.12)
    P = mol(c, t, C["s03.b"], ETANAL, 1400, 470, 150)
    halo(c, t, C["s03.b"] + 0.4, [P[1], P[3]], 50, CINZA)
    E.frase(c, t, C["s03.b"], [("na ponta, com H:", "i", 66), ("aldeído", "g", 66, COR)], XE, 520, passo=0.12)
    mol(c, t, C["s03.c"], ETER, 1400, 820, 110)
    E.frase(c, t, C["s03.c"], [("éter:", "g", 66), ("O entre dois carbonos", "i", 66)], XE, 800, passo=0.12)


# ---------------- ácido ----------------
AX, AY, AE = 1400, 560, 180


def b_acido(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("troque o H do aldeído por", "i", 66), ("OH", "g", 66, Q.cor_el("O"))], XE, 220, passo=0.1)
        troca = ep(t, C["s04.a"] + 0.8, 0.6)
        if troca < 1:
            E.saida(c, t, C["s04.a"] + 0.8, lambda: mol(c, t, C["s04"], ETANAL, AX, AY, AE))
        if t >= C["s04.a"] + 0.8:
            P = mol(c, t, C["s04.a"] + 0.8, ACETICO, AX, AY, AE)
            grupo_c(c, t, C["s04.b"], P, 1, 2, 3, 60)
            E.frase(c, t, C["s04.b"], ps("no mesmo carbono: carbonila e OH", "i", 60), XE, 340, passo=0.1)
            E.frase(c, t, C["s04.c"], [("carboxila", "g", 100, COR)], XE, 520)
            Q.formula_em(c, t, C["s04.c"] + 0.5, "–COOH", XE, 680, 110, cores={"O": Q.cor_el("O")})
            pilula_esq(c, t, C["s04.d"], "ácido carboxílico", XE, 860, 60, E.COR, "g")
        return
    P = mol(c, t, C["s05"] - 0.5, ACETICO, AX, AY, AE)
    grupo_c(c, t, C["s05"] - 0.5, P, 1, 2, 3, 60)
    E.frase(c, t, C["s05.a"], [("ácido", "g", 70, COR), ("+ ... +", "g", 60, TINTA2), ("oico", "g", 70, COR)], XE, 230, passo=0.14)
    nome(c, t, C["s05.c"], [("ácido ", COR, None), ("et", TINTA, "2 C"), ("an", TINTA, None), ("oico", COR, "ácido")], XE, 450, 100, 0.25)
    pilula_esq(c, t, C["s05.d"], "ácido acético: o do vinagre", XE, 620, 48, TINTA, "b")
    E.frase(c, t, C["s05.e"], [("1 C:", "g", 60), ("ácido metanoico,", "g", 60, COR), ("o da formiga", "i", 62)], XE, 800, passo=0.12)
    Q.formula_em(c, t, C["s05.e"] + 0.8, "HCOOH", XE, 920, 80, cores={"O": Q.cor_el("O")})


# ---------------- éster ----------------
EX_, EY_, EE = 1350, 560, 160


def b_ester(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], [("troque o H do OH por um", "i", 66), ("carbono", "g", 66, COR)], XE, 220, passo=0.1)
        if t < C["s06.a"] + 0.8:
            E.saida(c, t, C["s06.a"] + 0.6, lambda: mol(c, t, C["s06"], ACETICO, EX_, EY_, EE))
        P = mol(c, t, C["s06.a"] + 0.8, ET_ET, EX_, EY_, EE)
        grupo_c(c, t, C["s06.b"], P, 1, 2, 5, 52)
        Q.formula_em(c, t, C["s06.b"], "–COO–", XE, 400, 110, cores={"O": Q.cor_el("O")})
        E.frase(c, t, C["s06.b"] + 0.6, ps("uma cadeia de cada lado", "i", 58, TINTA2), XE, 500, passo=0.1)
        E.frase(c, t, C["s06.c"], [("éster", "g", 120, COR)], XE, 700)
        pilula_esq(c, t, C["s06.d"], "nasce de ácido + álcool: outra aula", XE, 860, 44, TINTA2, "b")
        return
    P = mol(c, t, C["s07"] - 0.5, ET_ET, EX_, 420, EE)
    grupo_c(c, t, C["s07"] - 0.5, P, 1, 2, 5, 52)
    E.frase(c, t, C["s07.a"], ps("o nome tem duas partes", "i", 64), XE, 200, passo=0.1)
    corte(c, t, C["s07.b"], P, 2, 170)
    realca_fila(c, t, C["s07.b"] + 0.3, P, [0, 1])
    E.frase(c, t, C["s07.b"], [("lado da carbonila:", "i", 58), ("oico", "g", 58, TINTA2), ("→", "g", 58, TINTA2), ("ato", "g", 62, COR)], XE, 680, passo=0.1)
    realca_fila(c, t, C["s07.d"], P, [3, 4], TINTA2)
    E.frase(c, t, C["s07.d"], [("o outro lado:", "i", 58), ("prefixo + ila", "g", 58)], XE, 780, passo=0.1)
    nome(c, t, C["s07.f"] - 0.6, [("etan", COR, None), ("oato", COR, "do ácido"), (" de ", TINTA2, None), ("et", TINTA, None), ("ila", TINTA, "do outro lado")], XE, 950, 100, 0.2)


# ---------------- aroma ----------------
def b_aroma(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], [("etanoato de etila:", "g", 62, COR), ("cheiro de fruta", "i", 64)], XE, 220, passo=0.12)
        E.frase(c, t, C["s08.a"] + 1.2, ps("aparece no removedor de esmalte", "i", 56, TINTA2), XE, 310, passo=0.08)
        for k, (key, s) in enumerate((("s08.b", "banana"), ("s08.c", "abacaxi"), ("s08.d", "laranja"))):
            cx = 420 + k * 540
            E.foco(c, t, C[key], 0.5, lambda a, cx=cx: E.bola(c, cx, 560, 110 * a, E.COR, a))
            E.foco(c, t, C[key] + 0.1, 0.4, lambda a, cx=cx, s=s: centro(c, s, cx, 580, 54, "g", E.SOBRE, a))
            E.foco(c, t, C[key] + 0.3, 0.4, lambda a, cx=cx: centro(c, "éster", cx, 740, 50, "i", TINTA2, a))
        E.frase(c, t, C["s08.e"], ps("as frutas fabricam ésteres ao amadurecer", "i", 60), W / 2, 920, "center", 0.08)
        return
    E.frase(c, t, C["s09.a"], [("por que", "i", 74), ("têm cheiro?", "g", 70, COR)], XE, 220, passo=0.12)
    Q.bequer(c, t, C["s09"], 1350, 900, 360, 300, 0.45, Q.AGUA, graduacao=False,
             particulas=dict(n=26, estado="liquido", tipos=[(E.COR, 1.0)], r=12, semente=3))
    if t >= C["s09.b"]:
        q = ep(t, C["s09.b"], 0.6)
        Q.particulas(c, t, 1170, 300, 360, 360, 14, estado="gas", tipos=[(E.COR, 1.0)], r=12, semente=7, a=q)
        seta(c, t, C["s09.b"] + 0.3, 1600, 640, 1700, 380)
        E.foco(c, t, C["s09.b"] + 0.6, 0.4, lambda a: E.escreve(c, "até o nariz", 1630, 340, 50, "i", COR, a))
    E.frase(c, t, C["s09.b"], ps("as moléculas saem do líquido e chegam ao nariz", "i", 54), XE, 360, passo=0.08)
    E.frase(c, t, C["s09.c"], [("ésteres pequenos", "g", 60), ("evaporam fácil", "g", 60, COR)], XE, 520, passo=0.12)
    E.frase(c, t, C["s09.d"], ps("e o nariz é muito sensível a eles", "i", 58), XE, 630, passo=0.08)
    pilula_esq(c, t, C["s09.e"], "por que evaporam fácil: outra aula", XE, 800, 44, TINTA2, "b")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s10.a"], [("éster", "g", 70), ("≠", "g", 70, ERRADO), ("éter", "g", 70)], XE + 450, 190, passo=0.2)
    P1 = mol(c, t, C["s10.b"], ETER, 560, 560, 140)
    halo(c, t, C["s10.b"] + 0.4, [P1[2]], 50)
    E.frase(c, t, C["s10.b"] + 0.2, [("éter:", "g", 64, COR), ("C–O–C", "g", 64)], 300, 820, passo=0.12)
    E.foco(c, t, C["s10.b"] + 0.8, 0.4, lambda a: E.escreve(c, "1 oxigênio", 330, 920, 54, "i", TINTA2, a))
    P2 = mol(c, t, C["s10.c"], ET_ET, 1400, 560, 140)
    grupo_c(c, t, C["s10.c"] + 0.4, P2, 1, 2, 5, 46)
    E.frase(c, t, C["s10.c"] + 0.2, [("éster:", "g", 64, COR), ("C–COO–C", "g", 64)], 1130, 820, passo=0.12)
    E.foco(c, t, C["s10.c"] + 0.8, 0.4, lambda a: E.escreve(c, "2 oxigênios, um na carbonila", 1100, 920, 54, "i", TINTA2, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], [("o atalho:", "i", 66, CLARO), ("o 2º oxigênio da carbonila", "g", 62, BR)], W / 2, 170, "center", 0.12)
        P1 = mol(c, t, C["s11.a"] + 0.4, ACETICO, 560, 460, 140, escuro=True)
        anelc(c, t, C["s11.b"], P1, 2, 44, E.CLARO)
        pilula_em(c, t, C["s11.b"] + 0.3, "com H: ácido", 560, 680, 56, E.COR)
        P2 = mol(c, t, C["s11.a"] + 0.6, ET_ME, 1350, 460, 140, escuro=True)
        anelc(c, t, C["s11.c"], P2, 2, 34, E.CLARO)
        pilula_em(c, t, C["s11.c"] + 0.3, "com C: éster", 1350, 680, 56, E.COR)
        E.frase(c, t, C["s11.d"], [("nome do éster:", "i", 60, CLARO), ("corte no O simples", "g", 60, BR)], XE, 860, passo=0.12)
        corte(c, t, C["s11.d"] + 0.5, P2, 2, 130, E.CLARO)
        E.frase(c, t, C["s11.e"], [("carbonila =", "i", 60, CLARO), ("ato", "g", 64, E.CLARO)], XE, 970, passo=0.12)
        E.frase(c, t, C["s11.f"], [("outro lado =", "i", 60, CLARO), ("ila", "g", 64, BR)], XE + 620, 970, passo=0.12)
        return
    E.frase(c, t, C["s12.a"], ps("o éster é o ácido com um carbono no lugar do H", "i", 60, CLARO), XE, 240, passo=0.08)
    E.frase(c, t, C["s12.a"] + 1.8, ps("a parte do ácido guarda a carbonila", "i", 60, CLARO), XE, 340, passo=0.08)
    E.frase(c, t, C["s12.b"], [("escrito ao contrário?", "g", 64, BR)], XE, 540)
    cond(c, t, C["s12.b"] + 0.4, ["CH3", "OOC", "CH3"], XE, 720, 110, cores={0: BR, 1: E.CLARO, 2: BR})
    E.frase(c, t, C["s12.c"], [("ache a carbonila", "g", 64, E.CLARO), ("primeiro", "i", 66, CLARO)], XE, 900, passo=0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 180)
    for k, M_ in enumerate((PROPANOICO, ET_ME)):
        cx = 600 + k * 760
        E.foco(c, t, C["s13.a"] + 0.3 * k, 0.4, lambda a, cx=cx, k=k: (E.bola(c, cx - 300, 330, 36, a=a), centro(c, str(k + 1), cx - 300, 348, 44, "g", E.SOBRE, a)))
        mol(c, t, C["s13.a"] + 0.3 * k, M_, cx, 560, 140, d=0.6)
    E.frase(c, t, C["s13.a"] + 0.8, ps("ácido ou éster?", "i", 64), XE, 880, passo=0.1)
    E.frase(c, t, C["s13.b"], ps("e o nome de cada um?", "i", 64), XE, 980, passo=0.1)
    if t >= C["s14"]:
        E.relogio(c, t, C["s14.a"], cx=1650, cy=860, r=80)


def b_resposta(c, t, C, b):
    Ps = []
    for k, M_ in enumerate((PROPANOICO, ET_ME)):
        cx = 600 + k * 760
        E.foco(c, t, C["s15"] - 0.4, 0.4, lambda a, cx=cx, k=k: (E.bola(c, cx - 300, 330, 36, a=a), centro(c, str(k + 1), cx - 300, 348, 44, "g", E.SOBRE, a)))
        Ps.append(mol(c, t, C["s15"] - 0.4, M_, cx, 560, 140, d=0.1))
    grupo_c(c, t, C["s15.a"], Ps[0], 2, 3, 4, 50)
    anelc(c, t, C["s15.a"] + 0.3, Ps[0], 3, 44)
    pilula_em(c, t, C["s15.a"] + 0.4, "ácido", 600, 780, 56, E.COR)
    if t >= C["s15.b"]:
        Q.bastao(c, t, C["s15.b"], PROPANOICO["pts"][:3], 600, 560, 140, d=0.01, numeros=C["s15.b"], passo_n=0.15)
    nome(c, t, C["s15.c"], [("ácido ", COR, None), ("propan", TINTA, None), ("oico", COR, None)], 600, 900, 76, 0.25, "center")
    grupo_c(c, t, C["s16.a"], Ps[1], 1, 2, 4, 50)
    anelc(c, t, C["s16.a"] + 0.3, Ps[1], 2, 34)
    pilula_em(c, t, C["s16.a"] + 0.4, "éster", 1360, 780, 56, E.COR)
    corte(c, t, C["s16.b"], Ps[1], 2, 140)
    E.foco(c, t, C["s16.c"], 0.4, lambda a: centro(c, "2 C: etanoato", Ps[1][0][0] + 30, Ps[1][0][1] + 90, 44, "i", COR, a))
    E.foco(c, t, C["s16.d"], 0.4, lambda a: centro(c, "1 C: metila", Ps[1][3][0] + 40, Ps[1][3][1] - 70, 44, "i", TINTA, a))
    nome(c, t, C["s16.e"], [("etanoato", COR, None), (" de ", TINTA2, None), ("metila", TINTA, None)], 1360, 900, 76, 0.25, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        Q.formula_em(c, t, C["s17.a"], "–COOH", XE, 400, 100, cores={"O": Q.cor_el("O")})
        E.frase(c, t, C["s17.a"] + 0.3, [("ácido,", "g", 70, COR), ("com oico", "i", 70)], XE + 480, 400, passo=0.12)
        Q.formula_em(c, t, C["s17.b"], "–COO–C", XE, 580, 100, cores={"O": Q.cor_el("O")})
        E.frase(c, t, C["s17.b"] + 0.3, [("éster,", "g", 70, COR), ("ato de ila", "i", 70)], XE + 480, 580, passo=0.12)
        E.frase(c, t, C["s17.c"], ps("ésteres pequenos evaporam fácil: têm cheiro", "i", 60, TINTA2), XE, 780, passo=0.08)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s18.a"], [("amina,", "g", 96, COR), ("amida", "g", 96), ("e", "i", 96), ("nitrila", "g", 96, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s18.b"], [("a amida", "g", 76), ("num remédio", "i", 80)], XE, 540, passo=0.14)
    Q.atomo_em(c, t, C["s18"] + 0.5, XE + 90, 720, 70, "N")
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s18.c"] + 0.2, 0.4))
    E.frase(c, t, C["s18.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, acido=b_acido, ester=b_ester, aroma=b_aroma, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
