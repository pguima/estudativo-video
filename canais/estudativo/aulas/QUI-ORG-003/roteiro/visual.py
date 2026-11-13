"""Visual — Estudativo · QUI-ORG-003: nome dos hidrocarbonetos (prefixo, infixo e sufixo).
Segue a linguagem da Química (QUI-MIS-001) e da Orgânica (QUI-ORG-001). Nesta aula estreia o nome() da trilha: as peças do
nome lado a lado, prefixo em COR_TEXTO, infixo em tinta, sufixo e números em cinza, cada um com a legenda pequena embaixo.
A tabela de prefixos fica em duas colunas: os quatro para decorar na cor da matéria, os de figura em tinta.
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
ARQUIVO_FINAL = "estudativo_QUI-ORG-003_nome_hidrocarbonetos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("hidrocarboneto", "infixo", "posicao", "aneis", "atalho", "questao", "fim"))

Z5 = Q.zigzag(5)
PENT2 = dict(pts=Z5, duplas={(1, 2)})
PENT2R = dict(pts=Z5[::-1], duplas={(2, 3)})
_I = [(-1.9, -0.25), (-1.03, 0.25), (-0.03, 0.25), (0.97, 0.25), (1.97, 0.25)]
PINO = dict(pts=_I, triplas={(2, 3)})
PINOR = dict(pts=_I[::-1], triplas={(1, 2)})
HEX = anel(6)
PREF = ("met", "et", "prop", "but", "pent", "hex", "hept", "oct", "non", "dec")
assert Q.contar("C6H6") == {"C": 6, "H": 6} and 2 * 6 + 2 - 2 - 6 == 6


def nome_eno(c, t, t0, x, y, size=120, num="2", inf="en", passo=0.35, align="left"):
    return nome(c, t, t0, [("pent-", COR, "5 C"), (num + "-", TINTA2, "posição"), (inf, TINTA, "dupla" if inf == "en" else "tripla"),
                           ("o", TINTA2, "hidrocarb.")], x, y, size, passo, align)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for k, s in enumerate(PREF[:4]):
            ti = C["s01.a"] + 0.55 * k
            E.foco(c, t, ti, 0.4, lambda a, s=s, k=k: (E.escreve(c, s, XE, 280 + k * 150, 120, "g", COR, a),
                                                      E.escreve(c, "ano", XE + E.larg(s, "g", 120), 280 + k * 150, 120, "g", TINTA2, a)))
            if k:
                Q.bastao(c, t, ti, Q.zigzag(k + 1), 1150, 240 + k * 150, 90, d=0.3)
            else:
                Q.formula_em(c, t, ti, "CH4", 1150, 280, 70, align="center")
        E.frase(c, t, C["s01.b"], ps("o nome é um", "i", 70) + [("código", "g", 66, COR)], 1300, 900, "left", 0.12)
        nome(c, t, C["s01.b"] + 0.8, [("prop", COR, "prefixo"), ("an", TINTA, "infixo"), ("o", TINTA2, "sufixo")], 1300, 760, 110, 0.3)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 520, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("alcano,", "g", 70), ("alceno", "g", 70), ("ou", "i", 74), ("alcino", "g", 70, COR)]),
                 (C["s02.c"], [("dar nome ao", "i", 74), ("pent-2-eno", "g", 70, COR)]),
                 (C["s02.d"], [("ciclo-hexano", "g", 70), ("e", "i", 74), ("benzeno", "g", 70, COR)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula passada", "i", 76, TINTA2), XE, 200, passo=0.12)
    linhas = (("s03.a", dict(pts=Q.zigzag(4)), "saturada", "sem dupla nem tripla"), ("s03.b", dict(pts=Q.zigzag(4), duplas={(1, 2)}), "insaturada", "com dupla ou tripla"),
              ("s03.c", dict(pts=HEX, ligs=ligs_anel(0, 6), duplas={(0, 1), (2, 3), (4, 5)}), "aromática", "anel de 6 com duplas alternadas"))
    for k, (key, M_, r, nota) in enumerate(linhas):
        y = 380 + k * 240
        mol(c, t, C[key], M_, 1450, y, 100 if k < 2 else 85, d=0.5)
        pilula_esq(c, t, C[key] + 0.2, r, XE, y - 20, 60, E.COR if k == 1 else TINTA, "g")
        E.foco(c, t, C[key] + 0.4, 0.4, lambda a, nota=nota, y=y: E.escreve(c, nota, XE + 20, y + 60, 46, "i", TINTA2, a))


# ---------------- hidrocarboneto ----------------
def b_hidrocarboneto(c, t, C, b):
    def topo():
        E.frase(c, t, C["s04.a"], [("hidrocarboneto", "g", 96, COR)], XE, 250)
        E.frase(c, t, C["s04.a"] + 1.0, [("=", "g", 70, TINTA2), ("só", "i", 76), ("carbono", "g", 70), ("e", "i", 76), ("hidrogênio", "g", 70)], XE, 370, passo=0.12)
        for k, el in enumerate(("C", "H")):
            Q.atomo_em(c, t, C["s04.a"] + 1.5 + 0.3 * k, 1500 + 160 * k, 300, 60, el)
        for k, s in enumerate(("gás de cozinha", "parafina da vela", "gasolina")):
            pilula_esq(c, t, C["s04.b"] + 0.4 * k, s, XE + [0, 420, 830][k], 500, 52, TINTA, "i")
    E.saida(c, t, C["s04.c"] - 0.1, topo)
    if t < C["s04.c"]:
        return
    E.frase(c, t, C["s04.c"], ps("o nome tem três partes", "i", 76), W / 2, 260, "center", 0.12)
    for k, (key, s, cor, q) in enumerate((("s04.d", "prefixo", COR, "quantos carbonos"), ("s04.e", "infixo", TINTA, "que ligação"), ("s04.f", "sufixo", TINTA2, "que função"))):
        cx = 420 + k * 540
        E.foco(c, t, C[key], 0.5, lambda a, cx=cx, s=s, cor=cor, q=q: (M.rrect(c, cx - 230, 420, 460, 280, 30, cor, a),
                                                                        centro(c, s, cx, 600, 80, "g", BR, a),
                                                                        centro(c, q, cx, 790, 50, "i", TINTA2, a)))


# ---------------- prefixo ----------------
def b_prefixo(c, t, C, b):
    E.frase(c, t, C["s05.a"], [("prefixo", "g", 80, COR), ("=", "g", 76, TINTA2), ("quantos carbonos", "i", 80)], XE, 200, passo=0.12)
    cues = ["s05.b", "s05.c", "s05.d", "s05.e", "s06.b", "s06.c", "s06.d", "s06.e", "s06.f", "s06.g"]
    for k, (s, key) in enumerate(zip(PREF, cues)):
        col, lin = (0, k) if k < 4 else (1, k - 4)
        x, y = (XE + 60, 380 + lin * 150) if col == 0 else (1000 + (lin // 3) * 420, 380 + (lin % 3) * 150)
        cor = COR if col == 0 else TINTA
        E.foco(c, t, C[key], 0.4, lambda a, s=s, k=k, x=x, y=y, cor=cor: (E.escreve(c, str(k + 1), x, y, 84, "g", TINTA2, a),
                                                                         E.escreve(c, s, x + 110, y, 84, "g", cor, a)))
    if t >= C["s05.e"] + 0.5:
        q = ep(t, C["s05.e"] + 0.5, 0.4)
        E.caixa_pontilhada(c, XE + 30, 300, 470, 590, q, E.COR, prog_=q)
        E.foco(c, t, C["s05.e"] + 0.8, 0.4, lambda a: centro(c, "decore", XE + 265, 950, 50, "i", COR, a))
    if t >= C["s06.a"]:
        E.frase(c, t, C["s06.a"], ps("do 5 em diante: números das figuras", "i", 54, TINTA2), 1000, 300, passo=0.08)


# ---------------- infixo e sufixo ----------------
def b_infixo(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], [("infixo", "g", 80), ("=", "g", 76, TINTA2), ("a ligação entre carbonos", "i", 76)], XE, 200, passo=0.12)
        for k, (key, s, o, ex) in enumerate((("s07.b", "an", 1, "propano"), ("s07.c", "en", 2, "propeno"), ("s07.d", "in", 3, "propino"))):
            y = 430 + k * 200
            E.foco(c, t, C[key], 0.4, lambda a, s=s, y=y: E.escreve(c, s, XE + 40, y + 40, 130, "g", TINTA, a))
            Q.lewis(c, t, C[key] + 0.2, [("C", 0, 0), ("C", 1.6, 0)], [(0, 1, o)], 760, y, escala=150, size=96)
            E.foco(c, t, C[key] + 0.5, 0.4, lambda a, ex=ex, y=y, s=s: (E.escreve(c, ex, 1300, y + 26, 70, "i", TINTA2, a)))
        return
    if t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08.a"], [("sufixo", "g", 80, TINTA2), ("=", "g", 76, TINTA2), ("a função", "i", 76)], XE, 200, passo=0.12)
            E.frase(c, t, C["s08.b"], [("hidrocarboneto:", "i", 70), ("o", "g", 90, COR)], XE, 320, passo=0.12)
            exs = (("s08.c", [("prop", COR, "3 C"), ("an", TINTA, "simples"), ("o", TINTA2, None)], dict(pts=Q.zigzag(3))),
                   ("s08.d", [("et", COR, "2 C"), ("en", TINTA, "dupla"), ("o", TINTA2, None)], dict(pts=[(-0.5, 0), (0.5, 0)], duplas={(0, 1)})),
                   ("s08.e", [("et", COR, "2 C"), ("in", TINTA, "tripla"), ("o", TINTA2, None)], dict(pts=[(-0.5, 0), (0.5, 0)], triplas={(0, 1)})))
            for k, (key, pecas, M_) in enumerate(exs):
                y = 500 + k * 215
                nome(c, t, C[key], pecas, XE, y, 100, 0.3)
                if k == 0:
                    mol(c, t, C[key] + 0.5, M_, 1350, y - 40, 120, d=0.4)
                else:
                    Q.lewis(c, t, C[key] + 0.5, [("C", 0, 0), ("C", 1.6, 0)], [(0, 1, k + 1)], 1230, y - 40, escala=150, size=90)
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    E.frase(c, t, C["s09.a"], ps("o infixo dá o nome da família", "i", 74), XE, 220, passo=0.12)
    for k, (key, inf, fam, o) in enumerate((("s09.b", "an", "alcano", 1), ("s09.c", "en", "alceno", 2), ("s09.d", "in", "alcino", 3))):
        cx = 420 + k * 540
        E.foco(c, t, C[key], 0.4, lambda a, cx=cx, inf=inf: centro(c, inf, cx, 500, 140, "g", TINTA, a))
        E.foco(c, t, C[key] + 0.3, 0.4, lambda a, cx=cx, fam=fam: E.pilula(c, fam, cx, 640, 64, "g", fundo=E.COR, a=a))
        Q.lewis(c, t, C[key] + 0.5, [("C", 0, 0), ("C", 1.4, 0)], [(0, 1, o)], cx - 105, 820, escala=150, size=80)


# ---------------- posição da dupla ----------------
PX, PY, PE = 1300, 520, 170


def b_posicao(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10"], ps("com 4 carbonos ou mais", "i", 66, TINTA2), XE, 200, passo=0.1)
        E.frase(c, t, C["s10.a"], ps("o nome diz onde está a dupla", "i", 70), XE, 300, passo=0.1)
        E.frase(c, t, C["s10.b"], [("1", "g", 60, COR)] + ps("numere pela ponta mais perto", "i", 60), XE, 760, passo=0.1)
        E.frase(c, t, C["s10.c"], [("2", "g", 60, COR)] + ps("o número é o do 1º carbono da dupla", "i", 60), XE, 870, passo=0.1)
        Q.bastao(c, t, C["s10"] + 0.3, Z5, PX, PY, PE, duplas={(1, 2)}, d=0.6)
        Q.bastao(c, t, C["s10.b"] + 0.3, Z5, PX, PY, PE, duplas={(1, 2)}, d=0.01, numeros=C["s10.b"] + 0.3, passo_n=0.2)
        P = pts_tela(Z5, PX, PY, PE)
        realce(c, t, C["s10.c"] + 0.3, P[1], P[2], largura=34)
        return
    if t < C["s12"]:
        P = mol(c, t, C["s11"] - 0.3, PENT2, PX, PY - 60, PE, numeros=C["s11.a"] + 0.4)
        E.frase(c, t, C["s11.a"], ps("a dupla está mais perto da esquerda", "i", 60), XE, 200, passo=0.1)
        realce(c, t, C["s11.b"], P[1], P[2], largura=34)
        E.foco(c, t, C["s11.b"] + 0.4, 0.4, lambda a: centro(c, "entre o 2 e o 3", (P[1][0] + P[2][0]) / 2, P[1][1] + 140, 50, "i", COR, a))
        nome_eno(c, t, C["s11.c"], XE + 300, 880, 130, passo=(C["s11.f"] - C["s11.c"]) / 3.2)
        return
    # s12: a grafia antiga
    nome_eno(c, t, C["s12"] - 0.5, W / 2, 420, 150, passo=0.0, align="center")
    E.frase(c, t, C["s12.a"], ps("em provas antigas:", "i", 66, TINTA2), W / 2, 640, "center", 0.1)
    E.foco(c, t, C["s12.a"] + 1.0, 0.5, lambda a: centro(c, "2-penteno", W / 2, 820, 130, "g", TINTA2, a))
    E.foco(c, t, C["s12.a"] + 1.8, 0.4, lambda a: centro(c, "a mesma molécula", W / 2, 940, 54, "i", COR, a))


# ---------------- anéis ----------------
def b_aneis(c, t, C, b):
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], [("cadeia fechada:", "i", 76), ("ciclo", "g", 80, COR), ("na frente", "i", 76)], XE, 220, passo=0.12)
        mol(c, t, C["s13.b"], dict(pts=HEX, ligs=ligs_anel(0, 6)), 1400, 580, 170)
        E.frase(c, t, C["s13.b"], ps("6 carbonos, só simples", "i", 64, TINTA2), XE, 420, passo=0.1)
        nome(c, t, C["s13.c"], [("ciclo-", COR, "anel"), ("hex", COR, "6 C"), ("an", TINTA, "simples"), ("o", TINTA2, None)], XE, 700, 120, 0.3)
        pilula_em(c, t, C["s13.c"] + 1.4, "um solvente", XE + 330, 900, 46, TINTA, "i")
        return
    P = mol(c, t, C["s14"], dict(pts=HEX, ligs=ligs_anel(0, 6), duplas={(0, 1), (2, 3), (4, 5)}), 1400, 580, 170)
    E.frase(c, t, C["s14.a"], ps("o anel aromático tem nome próprio", "i", 66), XE, 220, passo=0.1)
    E.frase(c, t, C["s14.b"], [("benzeno", "g", 120, COR)], XE, 420)
    Q.formula_em(c, t, C["s14.b"] + 0.8, "C6H6", XE, 580, 110)
    for k, (i, j) in enumerate(((0, 1), (2, 3), (4, 5))):
        realce(c, t, C["s14.c"] + 0.2 * k, P[i], P[j], largura=30)
    E.frase(c, t, C["s14.c"], ps("3 duplas, mas sem en no nome", "i", 60, TINTA2), XE, 760, passo=0.1)
    E.frase(c, t, C["s14.d"], [("é", "i", 70), ("benzeno,", "g", 70, COR), ("e pronto", "i", 70)], XE, 880, passo=0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s15.a"], ps("numerar pela ponta errada", "i", 70), XE + 450, 190, passo=0.12)
    P = pts_tela(Z5, PX, 470, 160)
    Q.bastao(c, t, C["s15"], Z5, PX, 470, 160, duplas={(1, 2)}, d=0.5)

    def errado():
        for k in range(5):
            i = 4 - k
            E.foco(c, t, C["s15.b"] + 0.15 * k, 0.3, lambda a, i=i, k=k: (E.bola(c, P[i][0], P[i][1], 30, ERRADO, a),
                                                                           centro(c, str(k + 1), P[i][0], P[i][1] + 14, 38, "g", BR, a)))
        E.foco(c, t, C["s15.c"], 0.4, lambda a: E.escreve(c, "pent-3-eno", XE, 760, 110, "g", ERRADO, a))
        if t >= C["s15.c"] + 0.8:
            E.risco(c, XE - 10, 780, XE + 640, 700, t, C["s15.c"] + 0.8, largura=10)
    E.saida(c, t, C["s15.d"] + 0.6, errado)
    if t >= C["s15.d"]:
        Q.bastao(c, t, C["s15.d"], Z5, PX, 470, 160, duplas={(1, 2)}, d=0.01, numeros=C["s15.d"] + 0.4, passo_n=0.15)
        E.frase(c, t, C["s15.d"], ps("o menor número para a dupla", "i", 60, TINTA2), XE, 900, passo=0.1)
        nome_eno(c, t, C["s15.e"], 1100, 780, 110, passo=0.15)
        E.foco(c, t, C["s15.e"] + 0.8, 0.4, lambda a: E.selo(c, 1800, 740, 50, True, a))


# ---------------- atalho (palco) ----------------
def poligono(c, cx, cy, n, r, a=1.0, cor=None):
    pts = anel(n, r, 90, cx, cy)
    for k in range(n):
        A, B = pts[k], pts[(k + 1) % n]
        M.line(c, A[0], A[1], B[0], B[1], cor or BR, a, 6)


def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s17"]:
        def s16():
            E.frase(c, t, C["s16.a"], ps("o atalho do infixo", "i", 70, CLARO), W / 2, 170, "center", 0.12)
            E.frase(c, t, C["s16.b"], [("a,", "g", 110, BR), ("e,", "g", 110, BR), ("i", "g", 110, BR)], W / 2, 400, "center", 0.3)
            for k, (key, s, o) in enumerate((("s16.c", "an", 1), ("s16.d", "en", 2), ("s16.e", "in", 3))):
                cx = 420 + k * 540
                E.foco(c, t, C[key], 0.4, lambda a, cx=cx, s=s: centro(c, s, cx, 640, 110, "g", E.CLARO, a))
                E.foco(c, t, C[key] + 0.2, 0.4, lambda a, cx=cx, o=o: [M.line(c, cx - 110, 780 + (j - (o - 1) / 2) * 30, cx + 110, 780 + (j - (o - 1) / 2) * 30, BR, a, 9) for j in range(o)])
                E.foco(c, t, C[key] + 0.3, 0.4, lambda a, cx=cx, o=o: centro(c, f"{o}ª vogal = {o} traço" + ("s" if o > 1 else ""), cx, 920, 46, "i", CLARO, a))
        E.saida(c, t, C["s17"] - 0.1, s16)
        return
    E.frase(c, t, C["s17.a"], [("decore só:", "i", 66, CLARO), ("met, et, prop, but", "g", 66, BR)], XE, 200, passo=0.12)
    for k, (s, n) in enumerate((("pentágono", 5), ("hexágono", 6), ("octógono", 8))):
        cx = 400 + k * 420
        E.foco(c, t, C["s17.b"] + 0.4 * k, 0.5, lambda a, cx=cx, n=n: poligono(c, cx, 440, n, 100, a, E.CLARO))
        E.foco(c, t, C["s17.b"] + 0.4 * k + 0.2, 0.4, lambda a, cx=cx, s=s, n=n: (centro(c, str(n), cx, 465, 70, "g", BR, a), centro(c, s, cx, 620, 50, "i", CLARO, a)))
    E.frase(c, t, C["s17.c"], ps("9 e 10:", "i", 66, CLARO), XE, 790, passo=0.1)
    E.frase(c, t, C["s17.d"], [("novembro", "g", 70, BR), ("=", "g", 66, CLARO), ("non,", "g", 70, E.CLARO), ("dezembro", "g", 70, BR), ("=", "g", 66, CLARO),
                               ("dec", "g", 70, E.CLARO)], XE, 920, passo=0.14)


# ---------------- questão ----------------
QX, QY, QE = 1300, 560, 160


def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 180)
    mol(c, t, C["s18.a"] - 0.3, PINO, QX, QY, QE)
    E.frase(c, t, C["s18.a"], [("1", "g", 56, COR)] + ps("dê o nome", "i", 64), XE, 360, passo=0.1)
    E.frase(c, t, C["s18.b"], [("2", "g", 56, COR)] + ps("alcano, alceno ou alcino?", "i", 64), XE, 470, passo=0.1)
    if t >= C["s19"]:
        E.relogio(c, t, C["s19.a"], cx=XE + 280, cy=760, r=100)


def b_resposta(c, t, C, b):
    P = mol(c, t, C["s20"] - 0.5, PINO, QX, QY - 80, QE)
    E.frase(c, t, C["s20.a"], ps("a tripla está mais perto da direita", "i", 60), XE, 180, passo=0.1)
    realce(c, t, C["s20.a"] + 0.4, P[2], P[3], largura=36)
    if t >= C["s20.b"]:
        Q.bastao(c, t, C["s20.b"], PINOR["pts"], QX, QY - 80, QE, triplas=PINOR["triplas"], d=0.01, numeros=C["s20.b"], passo_n=0.15)
    nome(c, t, C["s20.c"], [("pent-", COR, "5 C"), ("2-", TINTA2, "posição"), ("in", TINTA, "tripla"), ("o", TINTA2, "hidrocarb.")], XE + 200, 820, 130,
         (C["s20.f"] - C["s20.c"]) / 3.2)
    pilula_em(c, t, C["s20.g"], "alcino", 1500, 800, 66, E.COR)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        nome(c, t, C["s21.a"], [("prefixo", COR, "carbonos")], XE, 420, 90)
        nome(c, t, C["s21.b"], [("infixo", TINTA, "ligação")], XE + 520, 420, 90)
        nome(c, t, C["s21.c"], [("sufixo", TINTA2, "função")], XE + 1000, 420, 90)
        E.frase(c, t, C["s21.d"], ps("numere pela ponta mais perto da", "i", 66) + [("dupla", "g", 62, COR), ("ou", "i", 66), ("tripla", "g", 62, COR)], XE, 720, passo=0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.a"], [("cadeias com", "i", 90), ("galhos", "g", 96, COR)], XE, 400, passo=0.14)
    Z4 = Q.zigzag(4)
    mol(c, t, C["s22.b"], dict(pts=Z4 + [(Z4[1][0], Z4[1][1] + 1), (Z4[2][0], Z4[2][1] - 1)], ligs=[(0, 1), (1, 2), (2, 3), (1, 4), (2, 5)]), 600, 700, 110)
    E.foco(c, t, C["s22.b"] + 0.6, 0.4, lambda a: E.escreve(c, "2,3-dimetilbutano", XE, 950, 66, "g", COR, a))
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, hidrocarboneto=b_hidrocarboneto, prefixo=b_prefixo, infixo=b_infixo, posicao=b_posicao,
              aneis=b_aneis, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
