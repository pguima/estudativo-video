"""Visual — Estudativo · QUI-ORG-012: ponto de ebulição dos orgânicos. Primeira aula do módulo Propriedades físicas e isomeria.
Segue a linguagem da Química (QUI-MIS-001), da Orgânica (QUI-ORG-001) e do módulo Funções (QUI-ORG-006).
LINGUAGEM DO MÓDULO PROPRIEDADES (QUI-ORG-012 a 014 copiam daqui):
- TERMÔMETRO [kit] termo(): reta horizontal de temperatura em °C com o zero marcado; cada substância é uma bolinha que desliza
  até o seu ponto de ebulição, com o nome acima e o valor embaixo. Mais quente à direita.
- LIGAÇÃO DE HIDROGÊNIO [kit] ponte_h(): tracejado turquesa entre o H de um OH e o O da molécula vizinha. Dipolo induzido não
  tem traço (só a proximidade); dipolo permanente = tracejado cinza.
- FORÇA EM ESCADA: ligação de hidrogênio no topo (COR_TEXTO), dipolo permanente no meio (tinta), dipolo induzido embaixo (cinza).
- Polar × apolar (QUI-ORG-013): parte polar em turquesa (halo), parte apolar em cinza-amarelado (CAUDA).
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
ARQUIVO_FINAL = "estudativo_QUI-ORG-012_ponto_ebulicao_organicos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("hidrocarboneto", "oxigenio", "galhos", "erro", "atalho", "questao", "fim"))

Z3f = [(x, -y) for x, y in Q.zigzag(3)]
BUTANO = dict(pts=Q.zigzag(4))
PROPANOL = dict(pts=Q.zigzag(4), rot={3: "OH"})
ACETICO = dict(pts=Z3f + [(Z3f[1][0], Z3f[1][1] - 1)], ligs=[(0, 1), (1, 2), (1, 3)], duplas={(1, 3)}, rot={2: "OH", 3: "O"})
PROPANONA = dict(pts=Z3f + [(Z3f[1][0], Z3f[1][1] - 1)], ligs=[(0, 1), (1, 2), (1, 3)], duplas={(1, 3)}, rot={3: "O"})
Z5 = Q.zigzag(5)
PENTANO = dict(pts=Z5)
Z4 = Q.zigzag(4)
METILBUT = dict(pts=Z4 + [(Z4[1][0], Z4[1][1] + 1)], ligs=[(0, 1), (1, 2), (2, 3), (1, 4)])
DIMETILPROP = dict(pts=[(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)], ligs=[(0, 1), (0, 2), (0, 3), (0, 4)])
BUTANOL = dict(pts=Q.zigzag(5), rot={4: "OH"})
PROPANOICO = dict(pts=Z4 + [(Z4[2][0], Z4[2][1] - 1)], ligs=[(0, 1), (1, 2), (2, 3), (2, 4)], duplas={(2, 4)}, rot={3: "OH", 4: "O"})
PE = dict(butano=-0.5, propanol=97, acetico=118, propanona=56, metano=-161, propano=-42, pentano=36, hexano=69, metilbutano=28, dimetilpropano=10,
          butanol=118, propanoico=141)
assert PE["butano"] < PE["propanona"] < PE["propanol"] < PE["acetico"]
assert PE["pentano"] > PE["metilbutano"] > PE["dimetilpropano"]
assert PE["pentano"] < PE["butanol"] < PE["propanoico"] and PE["acetico"] - PE["butano"] > 100 and PE["propanol"] - PE["butano"] > 95
assert Q.contar("C5H12") == {"C": 5, "H": 12} and Q.contar("C4H10O") == {"C": 4, "H": 10, "O": 1} and Q.contar("C3H6O2") == {"C": 3, "H": 6, "O": 2}


def termo(c, t, t0, itens, x0, x1, y, vmin, vmax, marcas=(0, 50, 100), size=46, escuro=False):
    """[kit] reta de temperatura: itens = [(nome, valor, instante, cor)]; cada bolinha desliza da esquerda até o valor"""
    tinta = BR if escuro else TINTA
    X = lambda v: x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    p = ep(t, t0, 0.6)
    if p <= 0:
        return X
    M.line(c, x0, y, x1, y, tinta, p, 6, progress=p)
    M.arrow(c, x1 - 30, y, x1 + 20, y, tinta, p, 6, 20, 1)
    for m in marcas:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a, m=m: (M.line(c, X(m), y - 14, X(m), y + 14, tinta, a, 4),
                                                   centro(c, f"{m} °C", X(m), y + 64, 36, "b", TINTA2 if not escuro else CLARO, a)))
    for k, it in enumerate(itens):
        nm, v, ti, cor = it[:4]
        txt = it[4] if len(it) > 4 else f"{round(v):d} °C"
        q = ease_io(prog(t, ti, 0.9))
        if q <= 0:
            continue
        xx = lerp(x0, X(v), q)
        alto = 70 if k % 2 == 0 else 175
        M.line(c, xx, y - 26, xx, y - alto + 40, TINTA2 if not escuro else CLARO, ep(t, ti + 0.6, 0.3) * 0.5, 3)
        E.bola(c, xx, y, 22, cor or E.COR, ep(t, ti, 0.3))
        E.foco(c, t, ti + 0.6, 0.4, lambda a, nm=nm, xx=xx, alto=alto, txt=txt: (
            centro(c, nm, xx, y - alto - 50, size, "g", tinta, a),
            centro(c, txt, xx, y - alto + 4, size * 0.85, "b", COR if not escuro else E.CLARO, a)))
    return X


def ponte_h(c, t, t0, A, B, cor=None, a_max=1.0):
    """[kit] ligação de hidrogênio: tracejado entre o H de um OH e o O vizinho"""
    p = ep(t, t0, 0.4) * a_max
    if p <= 0:
        return
    pt = M.paint(cor or E.COR, p, stroke=6)
    pt.setPathEffect(skia.DashPathEffect.Make([10, 9], 0))
    pth = skia.Path(); pth.moveTo(*A); pth.lineTo(lerp(A[0], B[0], ease_io(prog(t, t0, 0.4))), lerp(A[1], B[1], ease_io(prog(t, t0, 0.4))))
    c.drawPath(pth, pt)


def escada(c, t, tl, x, y0, dy=110, size=56, escuro=False):
    linhas = (("ligação de hidrogênio", COR if not escuro else E.CLARO, "mais forte"), ("dipolo permanente", TINTA if not escuro else BR, ""),
              ("dipolo induzido", TINTA2 if not escuro else CLARO, "mais fraca"))
    for k, ((s, cor, nota), ti) in enumerate(zip(linhas, tl)):
        y = y0 + k * dy
        E.foco(c, t, ti, 0.4, lambda a, s=s, cor=cor, y=y, k=k: (E.bola(c, x + 30, y - 18, 30, E.COR if k == 0 else CINZA, a),
                                                                 centro(c, str(k + 1), x + 30, y - 4, 38, "g", E.SOBRE, a),
                                                                 E.escreve(c, s, x + 90, y, size, "g", cor, a)))
        if nota:
            E.foco(c, t, ti + 0.3, 0.4, lambda a, nota=nota, y=y: E.escreve(c, nota, x + 760, y, 44, "i", TINTA2 if not escuro else CLARO, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for k, (M_, nm, key) in enumerate(((BUTANO, "butano", "s01.b"), (PROPANOL, "propan-1-ol", "s01.c"), (ACETICO, "ácido acético", "s01.d"))):
            cx = 420 + k * 540
            mol(c, t, C["s01.a"] + 0.3 * k, M_, cx, 300, 100, d=0.5)
            E.foco(c, t, C["s01.a"] + 0.3 * k + 0.4, 0.4, lambda a, cx=cx, nm=nm: centro(c, nm, cx, 440, 46, "g", TINTA, a))
        E.foco(c, t, C["s01.a"] + 1.2, 0.4, lambda a: centro(c, "massas quase iguais: 58 a 60 g/mol", W / 2, 530, 44, "i", TINTA2, a))
        termo(c, t, C["s01.b"] - 0.3, [("butano", PE["butano"], C["s01.b"], CINZA), ("propan-1-ol", PE["propanol"], C["s01.c"], TINTA),
                                         ("ácido", PE["acetico"], C["s01.d"], E.COR)], 260, 1700, 860, -20, 140)
        E.frase(c, t, C["s01.e"], [("quem explica é a", "i", 66), ("função", "g", 66, COR)], W / 2, 1020, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 520, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("ordenar", "g", 70), ("hidrocarboneto,", "i", 70), ("álcool e ácido", "i", 70)]),
                 (C["s02.c"], [("por que os", "i", 74), ("galhos", "g", 70, COR), ("baixam", "i", 74)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula de forças entre moléculas", "i", 66, TINTA2), XE, 180, passo=0.1)
    E.frase(c, t, C["s03.a"], [("ferver", "g", 66, COR), ("= afastar as moléculas, não quebrar", "i", 62)], XE, 300, passo=0.1)
    escada(c, t, [C["s03.b"], C["s03.c"], C["s03.d"]], XE, 470)
    E.frase(c, t, C["s03.e"], [("primeiro a", "i", 64), ("força,", "g", 62, COR), ("depois o", "i", 64), ("tamanho", "g", 62)], XE, 880, passo=0.12)


# ---------------- hidrocarboneto ----------------
def b_hidrocarboneto(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("comece pelo hidrocarboneto", "i", 70), XE, 220, passo=0.1)
        mol(c, t, C["s04.a"] + 0.3, BUTANO, 1400, 330, 130)
        E.frase(c, t, C["s04.b"], [("C e H:", "g", 60), ("eletronegatividades parecidas", "i", 60)], XE, 380, passo=0.1)
        pilula_esq(c, t, C["s04.c"], "apolar", XE, 500, 58, TINTA, "g")
        pilula_esq(c, t, C["s04.d"], "só dipolo induzido", XE + 300, 500, 58, TINTA2, "g")
        E.frase(c, t, C["s04.e"], ps("os pequenos são gases: metano, butano", "i", 58), XE, 700, passo=0.08)
        return
    E.frase(c, t, C["s05.a"], ps("molécula maior, ponto de ebulição maior", "i", 66), XE, 220, passo=0.1)
    X = termo(c, t, C["s05.a"] + 0.4, [("metano", PE["metano"], C["s05.b"], CINZA), ("propano", PE["propano"], C["s05.c"], CINZA),
                                         ("pentano", PE["pentano"], C["s05.d"], TINTA2), ("hexano", PE["hexano"], C["s05.e"], TINTA)],
              200, 1720, 640, -180, 100, marcas=(-100, 0))
    E.frase(c, t, C["s05.f"], ps("mais superfície para o dipolo induzido agir", "i", 58, TINTA2), XE, 900, passo=0.08)


# ---------------- álcool, ácido e o meio ----------------
def b_oxigenio(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], [("no álcool, o", "i", 70), ("OH", "g", 66, Q.cor_el("O")), ("muda tudo", "i", 70)], XE, 220, passo=0.12)
        P1 = mol(c, t, C["s06.a"] + 0.3, PROPANOL, 900, 520, 140)
        P2 = mol(c, t, C["s06.a"] + 0.6, dict(pts=[(x, -y) for x, y in Q.zigzag(4)], rot={3: "OH"}), 1290, 760, 140)
        ponte_h(c, t, C["s06.b"], (P1[3][0] + 20, P1[3][1] + 30), (P2[3][0] - 10, P2[3][1] - 30))
        E.frase(c, t, C["s06.b"], ps("o H do OH se liga ao O da vizinha", "i", 56), XE, 340, passo=0.08)
        pilula_esq(c, t, C["s06.b"] + 1.2, "ligação de hidrogênio", XE, 430, 50, E.COR, "g")
        E.frase(c, t, C["s06.c"], [("propan-1-ol:", "g", 60), ("97 °C", "g", 66, COR)], XE, 920, passo=0.12)
        E.frase(c, t, C["s06.d"], ps("quase 100 graus acima do butano", "i", 56, TINTA2), XE, 1010, passo=0.08)
        return
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("o ácido carboxílico vai além", "i", 70), XE, 220, passo=0.1)
        A = dict(pts=[(-1.87, -0.5), (-1.0, 0), (-0.5, -0.87), (-0.5, 0.87)], ligs=[(0, 1), (1, 2), (1, 3)], duplas={(1, 2)}, rot={2: "O", 3: "OH"})
        B = dict(pts=[(1.87, 0.5), (1.0, 0), (0.5, 0.87), (0.5, -0.87)], ligs=[(0, 1), (1, 2), (1, 3)], duplas={(1, 2)}, rot={2: "O", 3: "OH"})
        PA = mol(c, t, C["s07.a"] + 0.3, A, 1150, 560, 150)
        PB = mol(c, t, C["s07.a"] + 0.6, B, 1150, 560, 150)
        ponte_h(c, t, C["s07.b"], (PA[3][0] + 34, PA[3][1] - 10), (PB[2][0] - 20, PB[2][1] + 6))
        ponte_h(c, t, C["s07.b"] + 0.3, (PB[3][0] - 34, PB[3][1] + 10), (PA[2][0] + 20, PA[2][1] - 6))
        E.frase(c, t, C["s07.b"], ps("as carboxilas se encaixam: duas ligações", "i", 54), XE, 340, passo=0.08)
        pilula_esq(c, t, C["s07.c"], "andam aos pares", XE, 440, 50, E.COR, "g")
        E.frase(c, t, C["s07.d"], [("ácido acético:", "g", 60), ("118 °C", "g", 66, COR)], XE, 920, passo=0.12)
        return
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("e o aldeído, a cetona e o éter?", "i", 66), XE, 220, passo=0.1)
        P = mol(c, t, C["s08.a"] + 0.3, PROPANONA, 1400, 560, 150)
        halo(c, t, C["s08.b"], [P[3]], 50, CINZA)
        E.frase(c, t, C["s08.b"], [("têm O, mas", "i", 62), ("nenhum H nele", "g", 60)], XE, 360, passo=0.1)
        pilula_esq(c, t, C["s08.c"], "dipolo permanente", XE, 480, 52, TINTA, "g")
        E.frase(c, t, C["s08.d"], [("ficam no", "i", 62), ("meio", "g", 62, COR)], XE, 620, passo=0.12)
        E.frase(c, t, C["s08.e"], [("propanona:", "g", 60), ("56 °C", "g", 66, COR)], XE, 760, passo=0.12)
        return
    E.frase(c, t, C["s09.a"], ps("com massas parecidas, a ordem:", "i", 66), XE, 200, passo=0.1)
    itens = (("s09.e", "ácido carboxílico", "duas ligações de H", COR), ("s09.d", "álcool", "ligação de H", COR),
             ("s09.c", "aldeído, cetona, éter", "dipolo permanente", TINTA), ("s09.b", "hidrocarboneto", "dipolo induzido", TINTA2))
    for k, (key, s, f, cor) in enumerate(itens):
        y = 340 + k * 165
        w = 1300 - k * 260
        q = ep(t, C[key], 0.5)
        if q > 0:
            M.rrect(c, XE, y - 60, w * ease_io(q), 110, 24, E.COR if k < 2 else (TINTA if k == 2 else CINZA), 0.18 + 0.1 * (k < 2), shadow=False)
        E.foco(c, t, C[key] + 0.2, 0.4, lambda a, s=s, y=y, cor=cor: E.escreve(c, s, XE + 30, y + 16, 60, "g", cor, a))
        E.foco(c, t, C[key] + 0.4, 0.4, lambda a, f=f, y=y, w=w: E.escreve(c, f, XE + 30 + w - 10, y + 12, 42, "i", TINTA2, a))
    E.foco(c, t, C["s09.e"] + 0.6, 0.4, lambda a: (M.arrow(c, 1800, 900, 1800, 300, COR, a, 6, 22, 1), centro(c, "ferve mais", 1800, 960, 44, "i", COR, a)))


# ---------------- galhos ----------------
def b_galhos(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], [("e os galhos?", "i", 70), ("mesma fórmula:", "i", 60, TINTA2)], XE, 200, passo=0.12)
        Q.formula_em(c, t, C["s10.a"] + 1.0, "C5H12", XE + 820, 200, 76)
        for k, (M_, key, nm, v, esc) in enumerate(((PENTANO, "s10.b", "pentano", 36, 110), (METILBUT, "s10.c", "com um galho", 28, 110),
                                                    (DIMETILPROP, "s10.d", "com dois galhos", 10, 100))):
            cx = 400 + k * 560
            mol(c, t, C[key], M_, cx, 470, esc, d=0.5)
            E.foco(c, t, C[key] + 0.3, 0.4, lambda a, cx=cx, nm=nm: centro(c, nm, cx, 660, 50, "g", TINTA, a))
            E.foco(c, t, C[key] + 0.5, 0.4, lambda a, cx=cx, v=v: centro(c, f"{v} °C", cx, 760, 76, "g", COR, a))
        E.foco(c, t, C["s10.c"] + 0.8, 0.4, lambda a: centro(c, "metilbutano", 960, 830, 40, "i", TINTA2, a))
        E.foco(c, t, C["s10.d"] + 0.8, 0.4, lambda a: centro(c, "dimetilpropano", 1520, 830, 40, "i", TINTA2, a))
        return
    E.frase(c, t, C["s11.a"], [("a força é a mesma:", "i", 64), ("dipolo induzido", "g", 60, TINTA2)], XE, 200, passo=0.12)
    E.frase(c, t, C["s11.b"], [("muda a", "i", 64), ("forma", "g", 64, COR)], XE, 300, passo=0.12)
    # lápis no estojo: barras deitadas encostadas
    q = ep(t, C["s11.c"], 0.5)
    for k in range(4):
        if q > 0:
            M.rrect(c, 200, 480 + k * 56, 560, 44, 22, "#C9A24A", q, shadow=True)
            M.rrect(c, 200, 480 + k * 56, 60, 44, 22, "#E0B9A0", q)
    E.foco(c, t, C["s11.c"] + 0.4, 0.4, lambda a: centro(c, "comprida: encosta no corpo todo", 480, 760, 46, "i", TINTA, a))
    q2 = ep(t, C["s11.d"], 0.5)
    for k in range(5):
        if q2 > 0:
            E.bola(c, 1180 + (k % 3) * 120 + (k // 3) * 60, 520 + (k // 3) * 110, 56, "#8FA6B8", q2)
    E.foco(c, t, C["s11.d"] + 0.4, 0.4, lambda a: centro(c, "redonda: encosta pouco", 1300, 760, 46, "i", TINTA, a))
    E.frase(c, t, C["s11.e"], [("menos contato,", "i", 64), ("ponto de ebulição mais baixo", "g", 60, COR)], W / 2, 930, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("ordenar só pela massa", "i", 70), XE + 450, 190, passo=0.12)
    E.frase(c, t, C["s12.b"], [("massa:", "g", 60), ("butano 58,", "i", 62), ("ácido acético 60", "i", 62)], XE, 360, passo=0.12)
    E.foco(c, t, C["s12.b"] + 1.2, 0.4, lambda a: E.escreve(c, "quase empatam", XE + 1050, 360, 56, "g", ERRADO, a))
    termo(c, t, C["s12.c"], [("butano", PE["butano"], C["s12.c"] + 0.2, CINZA), ("ácido acético", PE["acetico"], C["s12.c"] + 0.6, E.COR)],
          260, 1700, 720, -20, 140)
    E.foco(c, t, C["s12.c"] + 1.4, 0.4, lambda a: centro(c, "mais de 100 graus de diferença", W / 2, 870, 52, "g", COR, a))
    pilula_em(c, t, C["s12.d"], "tamanhos parecidos: primeiro a força, o tamanho desempata", W / 2, 990, 44, TINTA)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], [("o atalho:", "i", 66, CLARO), ("procure o H preso a O", "g", 64, BR)], W / 2, 170, "center", 0.12)
        linhas = (("s13.c", "–COOH", "no topo", E.CLARO), ("s13.d", "–OH", "logo abaixo", E.CLARO), ("s13.e", "O sem H", "no meio", BR),
                  ("s13.f", "só C e H", "embaixo", CLARO))
        for k, (key, s, pos, cor) in enumerate(linhas):
            y = 340 + k * 160
            E.foco(c, t, C[key], 0.4, lambda a, s=s, y=y, cor=cor: Q.formula(c, s, XE + 60, y, 80, cor, a) if s.startswith("–") else E.escreve(c, s, XE + 60, y, 80, "g", cor, a))
            pilula_em(c, t, C[key] + 0.3, pos, 1200, y - 26, 56, E.COR if k < 2 else TINTA2)
        E.foco(c, t, C["s13.c"], 0.5, lambda a: M.arrow(c, 1650, 860, 1650, 300, E.CLARO, a, 6, 22, 1))
        return
    E.frase(c, t, C["s14.a"], ps("a ligação de hidrogênio precisa do H preso ao O", "i", 60, CLARO), XE, 280, passo=0.08)
    E.frase(c, t, C["s14.b"], [("não vale", "g", 64, ERRADO), ("com tamanhos muito diferentes", "i", 64, CLARO)], XE, 460, passo=0.12)
    termo(c, t, C["s14.c"], [("metanol", 65, C["s14.c"] + 0.3, E.CLARO), ("parafina", 350, C["s14.c"] + 0.8, CINZA, "acima de 300 °C")], 240, 1700, 720, 0, 400,
          marcas=(0, 100, 200, 300), escuro=True)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    for k, (M_, nm, esc) in enumerate(((PENTANO, "pentano", 100), (BUTANOL, "butan-1-ol", 100), (PROPANOICO, "ácido propanoico", 110))):
        cx = 380 + k * 580
        mol(c, t, C["s15.a"] + 0.3 * k, M_, cx, 430, esc, d=0.5)
        E.foco(c, t, C["s15.a"] + 0.3 * k + 0.4, 0.4, lambda a, cx=cx, nm=nm: centro(c, nm, cx, 620, 52, "g", TINTA, a))
    E.foco(c, t, C["s15.a"] + 1.4, 0.4, lambda a: centro(c, "72 a 74 g/mol", W / 2, 710, 44, "i", TINTA2, a))
    E.frase(c, t, C["s15.b"], ps("do menor para o maior ponto de ebulição", "i", 62), XE, 870, passo=0.08)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1650, cy=890, r=70)


def b_resposta(c, t, C, b):
    for k, (M_, nm, esc) in enumerate(((PENTANO, "pentano", 100), (BUTANOL, "butan-1-ol", 100), (PROPANOICO, "ácido propanoico", 110))):
        cx = 380 + k * 580
        P = mol(c, t, C["s17"] - 0.4, M_, cx, 330, esc, d=0.1)
        E.foco(c, t, C["s17"] - 0.4, 0.4, lambda a, cx=cx, nm=nm: centro(c, nm, cx, 500, 50, "g", TINTA, a))
        key = ("s17.a", "s17.b", "s17.c")[k]
        f = ("dipolo induzido", "ligação de H", "ligações de H aos pares")[k]
        pilula_em(c, t, C[key], f, cx, 580, 42, E.COR if k else TINTA2)
        if k:
            halo(c, t, C[key] + 0.2, [P[4] if k == 1 else P[3]], 44)
    termo(c, t, C["s17.d"] - 0.3, [("pentano", 36, C["s17.d"], CINZA), ("butan-1-ol", 118, C["s17.d"] + 0.6, TINTA), ("ácido propanoico", 141, C["s17.d"] + 1.2, E.COR)],
          260, 1700, 920, 0, 160, marcas=(0, 50, 100, 150))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s18.a"], [("primeiro a", "i", 66), ("força:", "g", 62, COR)], XE, 340, passo=0.12)
        E.foco(c, t, C["s18.a"] + 0.8, 0.4, lambda a: E.escreve(c, "ácido > álcool > polar sem H no O > hidrocarboneto", XE, 440, 52, "g", TINTA, a))
        E.frase(c, t, C["s18.b"], [("depois o", "i", 66), ("tamanho", "g", 62)], XE, 600, passo=0.12)
        E.frase(c, t, C["s18.c"], [("mais galhos", "g", 62, COR), ("= menos contato = PE mais baixo", "i", 62)], XE, 760, passo=0.1)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("etanol", "g", 80, COR), ("na água,", "i", 76), ("hexano", "g", 80), ("não", "i", 76)], XE, 400, passo=0.14)
    E.frase(c, t, C["s19.b"], [("o álcool", "i", 76), ("da gasolina", "g", 72)], XE, 520, passo=0.14)
    E.frase(c, t, C["s19.c"], [("e o", "i", 76), ("sabão", "g", 80, COR)], XE, 640, passo=0.14)
    E.foco(c, t, C["s19.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.d"] + 0.2, 0.4))
    E.frase(c, t, C["s19.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, hidrocarboneto=b_hidrocarboneto, oxigenio=b_oxigenio, galhos=b_galhos, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
