"""Visual — Estudativo · QUI-ORG-013: solubilidade, sabões e detergentes.
Segue a linguagem da Química (QUI-MIS-001), da Orgânica (QUI-ORG-001) e do módulo Propriedades (QUI-ORG-012): parte polar com
halo turquesa, parte apolar com faixa cinza-amarelada (CAUDA). Peças desta aula: proveta() — proveta graduada de 100 mL com
duas camadas (gasolina amarelada em cima, água embaixo) cujo limite desliza; sabao_mol() — cauda em zigue-zague + cabeça
esférica turquesa com o sinal "−"; micela() — anel de moléculas de sabão com as cabeças para fora e a gota de gordura no meio.
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
ARQUIVO_FINAL = "estudativo_QUI-ORG-013_solubilidade_saboes_detergentes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("mistura", "gasolina", "sabao", "erro", "atalho", "questao", "fim"))
CAUDA = "#C9B26A"
GASOL = "#F2C14E"
GORD = "#E8B04A"

ETANOL = dict(pts=Q.zigzag(3), rot={2: "OH"})
HEXANO = dict(pts=Q.zigzag(6))
BUTANOL = dict(pts=Q.zigzag(5), rot={4: "OH"})
HEXANOL = dict(pts=Q.zigzag(7), rot={6: "OH"})
assert 65 - 50 == 15 and abs(15 / 50 - 0.30) < 1e-9 and 2 * 15 == 30 and 2 * 12 == 24
assert 63 - 50 == 13 and abs(13 / 50 - 0.26) < 1e-9 and 2 * 13 == 26


def cauda_halo(c, t, t0, P, idx, cor=CAUDA, largura=40):
    """faixa sob a parte apolar da cadeia"""
    for k in range(len(idx) - 1):
        realce(c, t, t0 + 0.1 * k, P[idx[k]], P[idx[k + 1]], cor, 0.3, largura, 0.45)


def proveta(c, t, t0, cx, yb, h=620, w=150, agua=50.0, a_max=1.0, rot=True):
    """proveta de 100 mL: agua = volume da camada de baixo (o resto até 100 é gasolina)"""
    a = ep(t, t0, 0.5) * a_max
    if a <= 0:
        return
    k = h / 100.0
    yv = lambda v: yb - v * k
    c.drawRect(skia.Rect.MakeLTRB(cx - w / 2, yv(agua), cx + w / 2, yb), M.paint("#BFE3F2", 0.9 * a))
    c.drawRect(skia.Rect.MakeLTRB(cx - w / 2, yv(100), cx + w / 2, yv(agua)), M.paint(GASOL, 0.75 * a))
    pt = M.paint(Q.VIDRO, a, stroke=5)
    pth = skia.Path(); pth.moveTo(cx - w / 2, yv(108)); pth.lineTo(cx - w / 2, yb); pth.lineTo(cx + w / 2, yb); pth.lineTo(cx + w / 2, yv(108))
    c.drawPath(pth, pt)
    M.rrect(c, cx - w, yb, 2 * w, 18, 8, Q.VIDRO, a)
    for v in range(10, 101, 10):
        M.line(c, cx + w / 2 - 30, yv(v), cx + w / 2, yv(v), TINTA2, a, 3)
        if rot and v % 50 == 0:
            E.escreve(c, str(v), cx + w / 2 + 14, yv(v) + 14, 36, "b", TINTA2, a)
    M.line(c, cx - w / 2 - 20, yv(agua), cx + w / 2 + 20, yv(agua), COR, a, 4)


def sabao_mol(c, cx, cy, ang, esc=1.0, a=1.0, n=6):
    """molécula de sabão: cabeça em (cx, cy), cauda para o ângulo ang (graus)"""
    ux, uy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    nx, ny = -uy, ux
    pts = []
    for i in range(n + 1):
        d = 26 * esc + i * 22 * esc
        o = (7 if i % 2 else -7) * esc
        pts.append((cx + ux * d + nx * o, cy + uy * d + ny * o))
    for i in range(n):
        M.line(c, *pts[i], *pts[i + 1], "#8A7A44", a, max(3, 5 * esc))
    E.bola(c, cx, cy, 20 * esc, E.COR, a)
    if esc > 0.8:
        centro(c, "−", cx, cy + 9 * esc, 30 * esc, "g", BR, a)


def micela(c, t, t0, cx, cy, r=180, n=14, esc=0.9):
    q = ep(t, t0, 0.6)
    if q <= 0:
        return
    E.bola(c, cx, cy, (r - 70) * ease_back(q), GORD, q)
    for k in range(n):
        g = 360 * k / n + 8 * math.sin(t + k)
        hx, hy = cx + r * math.cos(math.radians(g)), cy + r * math.sin(math.radians(g))
        sabao_mol(c, hx, hy, g + 180, esc, ep(t, t0 + 0.05 * k, 0.3))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for k, (key, ttl, cor_b, cor_t, sep) in enumerate((("s01.a", "etanol + água", "#BFE3F2", "#BFE3F2", False),
                                                           ("s01.b", "hexano + água", "#BFE3F2", GASOL, True))):
            cx = 420 + k * 520
            Q.bequer(c, t, C[key], cx, 760, 300, 340, 0.75, "#BFE3F2", graduacao=False)
            if sep:
                q = ep(t, C[key] + 0.6, 0.6)
                c.drawRect(skia.Rect.MakeLTRB(cx - 140, 760 - 0.75 * 340 + 8, cx + 140, 760 - 0.75 * 340 + 8 + 90 * q), M.paint(GASOL, 0.8 * q))
            pilula_em(c, t, C[key] + 0.3, ttl, cx, 300, 46, TINTA, "g")
            E.foco(c, t, C[key] + 0.8, 0.4, lambda a, k=k, cx=cx: E.selo(c, cx + 170, 400, 40, k == 0, a))
        micela(c, t, C["s01.c"], 1520, 560, 170)
        pilula_em(c, t, C["s01.c"] + 0.3, "sabão + gordura", 1520, 300, 46, TINTA, "g")
        E.frase(c, t, C["s01.d"], [("a mesma", "i", 70), ("explicação", "g", 66, COR)], W / 2, 960, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 520, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("etanol", "g", 70, COR), ("mistura,", "i", 74), ("hexano", "g", 70), ("não", "i", 74)]),
                 (C["s02.c"], [("medir o álcool", "g", 70), ("da gasolina", "i", 74)]),
                 (C["s02.d"], [("como o", "i", 74), ("sabão", "g", 70, COR), ("tira a gordura", "i", 74)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula de solubilidade", "i", 70, TINTA2), XE, 200, passo=0.1)
    E.frase(c, t, C["s03.a"], [("semelhante", "g", 90, COR), ("dissolve", "i", 90), ("semelhante", "g", 90, COR)], XE, 380, passo=0.15)
    E.frase(c, t, C["s03.b"], [("polar", "g", 70), ("com", "i", 70), ("polar", "g", 70)], XE, 540, passo=0.12)
    E.frase(c, t, C["s03.c"], [("apolar", "g", 70, TINTA2), ("com", "i", 70), ("apolar", "g", 70, TINTA2)], XE, 660, passo=0.12)
    E.frase(c, t, C["s03.d"], [("e o", "i", 66), ("OH", "g", 62, Q.cor_el("O")), ("faz ligação de hidrogênio", "i", 66)], XE, 840, passo=0.12)


# ---------------- etanol × hexano ----------------
def b_mistura(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("o etanol tem duas partes", "i", 70), XE, 220, passo=0.1)
        P = mol(c, t, C["s04.a"] + 0.3, ETANOL, 1350, 520, 190)
        halo(c, t, C["s04.b"], [P[2]], 70)
        E.frase(c, t, C["s04.b"], [("OH:", "g", 62, Q.cor_el("O")), ("polar, liga-se à água", "i", 62)], XE, 380, passo=0.1)
        cauda_halo(c, t, C["s04.c"], P, [0, 1])
        E.frase(c, t, C["s04.c"], [("cadeia de 2 C:", "g", 62, TINTA2), ("apolar e curta", "i", 62)], XE, 500, passo=0.1)
        E.frase(c, t, C["s04.d"], [("vence o polar:", "i", 66), ("mistura com a água", "g", 62, COR)], XE, 820, passo=0.1)
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("hexano:", "g", 70), ("todo apolar", "i", 70)], XE, 220, passo=0.12)
        P = mol(c, t, C["s05.a"] + 0.3, HEXANO, 1350, 320, 120)
        cauda_halo(c, t, C["s05.a"] + 0.6, P, list(range(6)))
        Q.bequer(c, t, C["s05.b"], 1350, 960, 380, 400, 0.8, "#BFE3F2", graduacao=False,
                 particulas=dict(n=36, estado="liquido", tipos=[("#5DADE2", 1.0)], r=10, semente=2))
        q = ep(t, C["s05.d"], 0.6)
        if q > 0:
            c.drawRect(skia.Rect.MakeLTRB(1350 - 182, 960 - 0.8 * 400 + 6, 1350 + 182, 960 - 0.8 * 400 + 6 + 100 * q), M.paint(GASOL, 0.8 * q))
            E.foco(c, t, C["s05.d"] + 0.4, 0.4, lambda a: E.escreve(c, "hexano", 1560, 690, 44, "g", TINTA, a))
        E.frase(c, t, C["s05.b"], ps("a água fica presa a si mesma", "i", 58), XE, 380, passo=0.08)
        E.frase(c, t, C["s05.c"], ps("e deixa o hexano de fora", "i", 58, TINTA2), XE, 480, passo=0.08)
        E.frase(c, t, C["s05.d"], [("camada por cima:", "i", 58), ("mais leve", "g", 56, COR)], XE, 640, passo=0.1)
        return
    E.frase(c, t, C["s06.a"], ps("cadeia maior, mistura menos", "i", 70), XE, 220, passo=0.1)
    for k, (M_, nm, key, nota) in enumerate(((ETANOL, "etanol", "s06", "mistura em tudo"), (BUTANOL, "butan-1-ol", "s06.b", "só um pouco"),
                                             (HEXANOL, "hexan-1-ol", "s06.c", "quase nada"))):
        y = 400 + k * 200
        P = mol(c, t, C[key] + (0.4 if k == 0 else 0), M_, 1150, y, 95, d=0.5)
        cauda_halo(c, t, C[key] + 0.5, P, list(range(len(M_["pts"]) - 1)), largura=28)
        halo(c, t, C[key] + 0.5, [P[-1]], 40)
        E.foco(c, t, C[key] + 0.4, 0.4, lambda a, nm=nm, y=y: E.escreve(c, nm, XE, y + 20, 56, "g", TINTA, a))
        E.foco(c, t, C[key] + 0.6, 0.4, lambda a, nota=nota, y=y, k=k: E.escreve(c, nota, 1550, y + 20, 48, "i", COR if k == 0 else TINTA2, a))
    E.frase(c, t, C["s06.d"], ps("o mesmo OH, cauda apolar comprida demais", "i", 54, TINTA2), XE, 1000, passo=0.08)


# ---------------- gasolina ----------------
PX_, PYB = 1350, 940


def b_gasolina(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("a disputa mede o álcool da gasolina", "i", 66), XE, 240, passo=0.1)
        E.frase(c, t, C["s07.b"], [("a gasolina comum", "i", 66), ("leva etanol", "g", 62, COR)], XE, 400, passo=0.12)
        E.foco(c, t, C["s07.c"], 0.5, lambda a: E.escreve(c, "30%", XE, 680, 220, "g", COR, a))
        E.foco(c, t, C["s07.c"] + 0.4, 0.4, lambda a: E.escreve(c, "de etanol, hoje", XE + 560, 650, 56, "i", TINTA2, a))
        proveta(c, t, C["s07"] + 0.4, PX_ + 100, PYB, agua=0, a_max=0.0)
        return
    agua = 50.0
    if t >= C["s09.b"]:
        agua = lerp(50, 65, ease_io(prog(t, C["s09.b"], 1.6)))
    proveta(c, t, C["s08.a"], PX_, PYB, agua=agua if t >= C["s08.c"] else 0.001, rot=True)
    if C["s08.a"] <= t < C["s08.c"]:
        pass
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], [("proveta:", "g", 62), ("tubo com marcas de volume", "i", 60)], XE, 220, passo=0.1)
        E.frase(c, t, C["s08.b"], [("50 mL", "g", 70, "#B8860B"), ("de gasolina", "i", 64)], XE, 400, passo=0.12)
        E.frase(c, t, C["s08.c"], [("+ 50 mL", "g", 70, "#2E86C1"), ("de água com sal", "i", 64)], XE, 520, passo=0.12)
        E.foco(c, t, C["s08.c"] + 1.2, 0.4, lambda a: E.escreve(c, "o sal ajuda a separar", XE, 590, 44, "i", TINTA2, a))
        E.frase(c, t, C["s08.d"], ps("agite e espere separar", "i", 60, TINTA2), XE, 760, passo=0.1)
        return
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], [("o etanol prefere a", "i", 64), ("água", "g", 62, "#2E86C1")], XE, 260, passo=0.1)
        E.frase(c, t, C["s09.b"], ps("e desce para a camada de baixo", "i", 60), XE, 360, passo=0.1)
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "50 → 65 mL", XE, 560, 90, "g", TINTA, a))
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.escreve(c, "15 mL de etanol", XE, 700, 80, "g", COR, a))
        return
    E.frase(c, t, C["s10.a"], ps("quanto é 15 de 50?", "i", 70), XE, 280, passo=0.1)
    E.formula_em(c, t, C["s10.b"], "15 ÷ 50 = 0,3", XE, 480, 96, "g", TINTA)
    bola_txt(c, t, C["s10.c"], "30%", XE + 200, 680, 100, 80)


# ---------------- sabão ----------------
def b_sabao(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], [("e o", "i", 76), ("sabão?", "g", 76, COR)], XE, 240, passo=0.12)
        E.frase(c, t, C["s11.b"], [("sal de sódio de um", "i", 62), ("ácido graxo", "g", 60, COR)], XE, 400, passo=0.1)
        E.foco(c, t, C["s11.b"] + 1.4, 0.4, lambda a: E.escreve(c, "ácido carboxílico de cadeia bem longa", XE, 480, 46, "i", TINTA2, a))
        pilula_esq(c, t, C["s11.c"], "gordura + soda cáustica: outra aula", XE, 650, 46, TINTA2, "b")
        E.foco(c, t, C["s11.b"], 0.5, lambda a: sabao_mol(c, 1000, 560, 0, 2.2, a, 12))
        return
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"], [("cauda", "g", 70, "#8A7A44"), ("e", "i", 70), ("cabeça", "g", 70, COR)], XE, 220, passo=0.12)
        E.foco(c, t, C["s12"], 0.4, lambda a: sabao_mol(c, 1500, 520, 180, 2.4, a, 14))
        q = ep(t, C["s12.b"], 0.5)
        if q > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(760, 470, 1450, 570), 50, 50), M.paint(CAUDA, 0.35 * q))
        E.frase(c, t, C["s12.b"], [("cauda: cadeia longa,", "i", 58), ("apolar", "g", 58, "#8A7A44")], XE, 720, passo=0.1)
        E.foco(c, t, C["s12.b"] + 1.0, 0.4, lambda a: E.escreve(c, "mistura com a gordura", XE, 800, 46, "i", TINTA2, a))
        halo(c, t, C["s12.c"], [(1500, 520)], 80)
        Q.formula_em(c, t, C["s12.c"] + 0.3, "–COO^- Na^+", 1440, 400, 64)
        E.frase(c, t, C["s12.c"], [("cabeça: com carga,", "i", 58), ("gosta da água", "g", 58, COR)], XE, 900, passo=0.1)
        return
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], ps("na louça: as caudas entram na gordura", "i", 60), XE, 220, passo=0.08)
        E.frase(c, t, C["s13.b"], ps("as cabeças ficam viradas para a água", "i", 60, TINTA2), XE, 310, passo=0.08)
        sai = ease_io(prog(t, C["s13.d"], 2.0))
        micela(c, t, C["s13.a"], 1250 + 300 * sai, 640, 190, 16)
        E.foco(c, t, C["s13.c"], 0.4, lambda a: E.pilula(c, "micela", 1250 + 300 * sai, 380, 56, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s13.d"], ps("a água leva a micela, e a gordura vai junto", "i", 54), XE, 980, passo=0.08)
        return
    E.frase(c, t, C["s14.a"], [("detergente:", "g", 70, COR), ("outra cabeça", "i", 66)], XE, 220, passo=0.12)
    Q.formula_em(c, t, C["s14.b"], "–SO3^-", XE, 360, 100, cores={"S": Q.cor_el("S"), "O": Q.cor_el("O")})
    E.foco(c, t, C["s14.b"] + 0.4, 0.4, lambda a: E.escreve(c, "sulfonato", XE + 380, 350, 60, "i", TINTA2, a))
    E.frase(c, t, C["s14.c"], [("funciona na", "i", 60), ("água dura", "g", 58, COR), ("(cheia de cálcio)", "i", 56, TINTA2)], XE, 540, passo=0.1)
    E.foco(c, t, C["s14.c"] + 1.6, 0.4, lambda a: E.escreve(c, "o sabão ali forma nata e perde a força", XE, 630, 46, "i", TINTA2, a))
    E.frase(c, t, C["s14.d"], [("cadeia sem galhos:", "g", 58), ("biodegradável", "g", 58, COR)], XE, 820, passo=0.1)
    E.foco(c, t, C["s14.d"] + 1.2, 0.4, lambda a: E.escreve(c, "as bactérias desmontam", XE, 900, 46, "i", TINTA2, a))
    E.foco(c, t, C["s14.a"], 0.4, lambda a: sabao_mol(c, 1700, 720, 180, 2.0, a, 12))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s15.a"], ps("o sabão dissolve a gordura?", "i", 70), XE + 450, 190, passo=0.12)
    if t < C["s15.b"] + 0.4:
        E.foco(c, t, C["s15.a"] + 1.0, 0.4, lambda a: E.escreve(c, "dissolve", XE, 420, 100, "g", ERRADO, a))
        if t >= C["s15.a"] + 1.8:
            E.risco(c, XE - 10, 440, XE + 440, 360, t, C["s15.a"] + 1.8, largura=10)
    E.frase(c, t, C["s15.b"], ps("a gordura continua inteira,", "i", 62), XE, 520, passo=0.1)
    E.frase(c, t, C["s15.c"], [("presa dentro das", "i", 62), ("micelas", "g", 60, COR)], XE, 620, passo=0.1)
    micela(c, t, C["s15.c"], 1450, 600, 180, 14)
    E.frase(c, t, C["s15.d"], [("o sabão é a", "i", 66), ("ponte", "g", 66, COR), ("entre água e gordura", "i", 66)], XE, 920, passo=0.12)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s17"]:
        E.frase(c, t, C["s16.a"], ps("o atalho do teste da gasolina", "i", 66, CLARO), W / 2, 170, "center", 0.12)
        E.frase(c, t, C["s16.b"], [("com 50 mL de gasolina:", "i", 62, CLARO)], XE, 330)
        E.foco(c, t, C["s16.b"] + 1.0, 0.5, lambda a: E.escreve(c, "% etanol = 2 × aumento", XE, 480, 96, "g", BR, a))
        E.formula_em(c, t, C["s16.c"], "subiu 15 → 30%", XE, 680, 80, "g", E.CLARO)
        E.formula_em(c, t, C["s16.d"], "subiu 12 → 24%", XE, 820, 80, "g", E.CLARO)
        return
    E.frase(c, t, C["s17.a"], [("50 é a metade de 100:", "i", 64, CLARO), ("dobrar vira %", "g", 62, BR)], XE, 280, passo=0.12)
    E.frase(c, t, C["s17.b"], [("não vale", "g", 64, ERRADO), ("com outro volume", "i", 64, CLARO)], XE, 460, passo=0.12)
    E.formula_em(c, t, C["s17.c"], "100 mL: aumento = %", XE, 620, 70, "g", BR)
    E.formula_em(c, t, C["s17.d"], "outro volume: aumento ÷ volume", XE, 760, 70, "g", BR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s18.a"], ps("50 mL de gasolina + 50 mL de água com sal", "i", 56), XE, 340, passo=0.08)
    E.frase(c, t, C["s18.b"], [("no fim, a água marcou", "i", 60), ("63 mL", "g", 64, COR)], XE, 470, passo=0.1)
    E.frase(c, t, C["s18.c"], ps("quantos por cento de etanol?", "i", 64), XE, 620, passo=0.1)
    proveta(c, t, C["s18.a"], 1450, 960, agua=63)
    if t >= C["s19"]:
        E.relogio(c, t, C["s19.a"], cx=XE + 300, cy=860, r=80)


def b_resposta(c, t, C, b):
    proveta(c, t, C["s20"] - 0.4, 1450, 960, agua=63)
    E.formula_em(c, t, C["s20.a"], "63 − 50 = 13 mL", XE, 300, 84, "g", TINTA)
    E.foco(c, t, C["s20.b"], 0.4, lambda a: E.escreve(c, "13 mL de etanol", XE, 400, 56, "i", COR, a))
    E.formula_em(c, t, C["s20.c"], "atalho: 2 × 13 = 26", XE, 560, 76, "g", TINTA)
    bola_txt(c, t, C["s20.d"], "26%", XE + 160, 740, 90, 70)
    E.formula_em(c, t, C["s20.e"], "13 ÷ 50 = 0,26", XE, 930, 64, "g", TINTA2)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s21.a"], [("cadeia curta:", "g", 62), ("vence o OH, vai para a água", "i", 62)], XE, 360, passo=0.1)
        E.frase(c, t, C["s21.b"], [("cadeia longa:", "g", 62, TINTA2), ("vence a parte apolar", "i", 62)], XE, 500, passo=0.1)
        E.frase(c, t, C["s21.c"], [("hexano:", "g", 62), ("fica de fora", "i", 62)], XE, 640, passo=0.1)
        E.frase(c, t, C["s21.d"], [("sabão:", "g", 62, COR), ("segura os dois lados", "i", 62)], XE, 780, passo=0.1)
        micela(c, t, C["s21.d"], 1550, 640, 150, 12, 0.8)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22"] + 0.6, ps("mesma fórmula, desenhos diferentes", "i", 66), XE, 380, passo=0.1)
    E.frase(c, t, C["s22.a"], [("isomeria", "g", 110, COR), ("plana", "g", 110)], XE, 540, passo=0.14)
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s22.b"] + 0.2, 0.4))
    E.frase(c, t, C["s22.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, mistura=b_mistura, gasolina=b_gasolina, sabao=b_sabao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
