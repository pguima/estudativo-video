"""Visual — Estudativo · QUI-ORG-002: classificar carbonos e cadeias.
Segue a linguagem visual da Química (cabeçalho da QUI-MIS-001) e a da Orgânica (cabeçalho da QUI-ORG-001): bastão em tinta,
carbono da vez na cor da matéria, realce() na ligação que conta. As peças de base (hs, realce, halo, cond, nome, mol) são as
mesmas da QUI-ORG-001, copiadas aqui porque o kit não pode ser editado neste lote.
Nesta aula: o carbono classificado ganha uma bolinha com a letra P, S, T ou Q (primário, secundário, terciário, quaternário),
e as quatro perguntas da cadeia ficam numa coluna à esquerda, com os exemplos à direita.
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
ARQUIVO_FINAL = "estudativo_QUI-ORG-002_classificar_carbonos_cadeias.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("carbonos", "cadeia", "erro", "atalho", "questao", "fim"))

Z4, Z5 = Q.zigzag(4), Q.zigzag(5)
MB = dict(pts=Z4 + [(Z4[1][0], Z4[1][1] + 1.0)], ligs=[(0, 1), (1, 2), (2, 3), (1, 4)])           # 2-metilbutano
MBE = dict(pts=Z4 + [(Z4[2][0], Z4[2][1] - 1.0)], ligs=[(0, 1), (1, 2), (2, 3), (2, 4)], duplas={(0, 1)})  # 3-metilbut-1-eno
HEX = anel(6)
MCH = dict(pts=HEX + [(0, -2.0)], ligs=ligs_anel(0, 6) + [(0, 6)])                               # metilciclo-hexano
BENZ = dict(pts=HEX, ligs=ligs_anel(0, 6), duplas={(0, 1), (2, 3), (4, 5)})


def vizinhos_c(M_):
    v = viz_de(len(M_["pts"]), M_["ligs"])
    return {i: len([j for j in v[i] if j not in (M_.get("rot") or {})]) for i in v}


assert vizinhos_c(MB) == {0: 1, 1: 3, 2: 2, 3: 1, 4: 1}
assert sorted(vizinhos_c(MCH).values()) == [1, 2, 2, 2, 2, 2, 3]
assert len([i for i, n in vizinhos_c(MBE).items() if n == 1]) == 3


def tipo(c, t, t0, P, i, letra, cor=None, r=30, dx=0, dy=-62):
    """bolinha com a classificação do carbono (P, S, T, Q), ao lado do vértice"""
    E.foco(c, t, t0, 0.4, lambda a: (E.bola(c, P[i][0] + dx, P[i][1] + dy, r, cor, a), centro(c, letra, P[i][0] + dx, P[i][1] + dy + r * 0.45, r * 1.25, "g", E.SOBRE, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for k, s in enumerate(("aberta", "ramificada", "insaturada", "heterogênea")):
            ti = C["s01.a"] + 0.5 * k
            E.foco(c, t, ti, 0.5, lambda a, s=s, k=k: E.escreve(c, s, XE + (k % 2) * 60, 260 + k * 150, 120, "g", TINTA if k % 2 else COR, a))
        mol(c, t, C["s01.a"] + 0.3, MBE, 1450, 560, 170)
        E.frase(c, t, C["s01.b"], ps("cada palavra responde a", "i", 64) + [("uma pergunta", "g", 60, COR)], W / 2, 1000, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 520, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("classificar", "g", 70), ("cada", "i", 74), ("carbono", "g", 70, COR)]),
                 (C["s02.c"], [("4 perguntas", "g", 70), ("para a", "i", 74), ("cadeia", "g", 70, COR)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("da mais cobrada", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula passada", "i", 76, TINTA2), XE, 220, passo=0.12)
    E.frase(c, t, C["s03.a"], [("ponta", "g", 70), ("e", "i", 74), ("dobra", "g", 70), ("=", "g", 70, TINTA2), ("carbono", "g", 70, COR)], XE, 380, passo=0.12)
    Q.bastao(c, t, C["s03.a"], Z5, 1300, 540, 170, d=0.8, numeros=C["s03.a"] + 0.9, passo_n=0.15)
    E.frase(c, t, C["s03.b"], [("o carbono faz", "i", 74), ("4 ligações", "g", 76, COR)], XE, 860, passo=0.12)


# ---------------- carbonos ----------------
def b_carbonos(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], [("cadeia carbônica", "g", 76, COR), ("=", "g", 76, TINTA2), ("o esqueleto", "i", 80)], XE, 230, passo=0.12)
            E.frase(c, t, C["s04.a"] + 1.4, ps("os carbonos ligados e os átomos entre eles", "i", 56, TINTA2), XE, 320, passo=0.08)
            P = mol(c, t, C["s04.a"] + 0.4, MB, 1350, 560, 170)
            E.frase(c, t, C["s04.b"], ps("para classificar um carbono,", "i", 62), XE, 520, passo=0.1)
            E.frase(c, t, C["s04.b"] + 1.0, [("conte só os", "i", 66), ("carbonos vizinhos", "g", 62, COR)], XE, 610, passo=0.1)
            anelc(c, t, C["s04.b"] + 0.6, P, 1, 40)
            for k, j in enumerate((0, 2, 4)):
                realce(c, t, C["s04.b"] + 1.2 + 0.2 * k, P[1], P[j])
            E.frase(c, t, C["s04.c"], [("H", "g", 62), ("e", "i", 66), ("O", "g", 62, Q.cor_el("O"))] + ps("não entram", "i", 66), XE, 760, passo=0.1)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            nomes = (("s05.a", "primário", "P"), ("s05.b", "secundário", "S"), ("s05.c", "terciário", "T"), ("s05.d", "quaternário", "Q"))
            for k, (key, nm, L) in enumerate(nomes):
                cx, cy = 330 + k * 420, 520
                ti = C[key]
                angs = [0, 180, 90, 270][:k + 1]
                for j, g in enumerate(angs):
                    ux, uy = math.cos(math.radians(g)), -math.sin(math.radians(g))
                    E.foco(c, t, ti + 0.1 * j, 0.3, lambda a, ux=ux, uy=uy, cx=cx, cy=cy: (M.line(c, cx + ux * 50, cy + uy * 50, cx + ux * 110, cy + uy * 110, TINTA, a, 7),
                                                                                             Q.atomo(c, cx + ux * 150, cy + uy * 150, 40, "C", a)))
                E.foco(c, t, ti, 0.4, lambda a, cx=cx, cy=cy: (E.bola(c, cx, cy, 50, a=a), centro(c, "C", cx, cy + 22, 60, "g", E.SOBRE, a)))
                E.foco(c, t, ti + 0.3, 0.4, lambda a, cx=cx, nm=nm, k=k: (E.escreve(c, str(k + 1), cx - 20, 820, 96, "g", COR, a)))
                E.foco(c, t, ti + 0.4, 0.4, lambda a, cx=cx, nm=nm: centro(c, nm, cx, 900, 54, "g", TINTA, a))
            E.frase(c, t, C["s05"], ps("quantos carbonos vizinhos?", "i", 66, TINTA2), W / 2, 190, "center", 0.1)
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    # s06: no 2-metilbutano
    P = mol(c, t, C["s06"] - 0.3, MB, W / 2 + 200, 540, 200)
    E.frase(c, t, C["s06"], ps("neste bastão", "i", 70, TINTA2), XE, 220, passo=0.12)
    for k, i in enumerate((0, 3, 4)):
        tipo(c, t, C["s06.a"] + 0.2 * k, P, i, "P", dy=(70 if i == 4 else -62), dx=(60 if i == 4 else 0))
    tipo(c, t, C["s06.b"], P, 2, "S")
    tipo(c, t, C["s06.c"] + 0.4, P, 1, "T", dx=-60, dy=40)
    E.frase(c, t, C["s06.a"], [("P", "g", 60, COR), ("primário: as 3 pontas", "i", 60)], XE, 760, passo=0.1)
    E.frase(c, t, C["s06.b"], [("S", "g", 60, COR), ("secundário: 2 vizinhos", "i", 60)], XE, 860, passo=0.1)
    E.frase(c, t, C["s06.c"], [("T", "g", 60, COR), ("terciário: de onde sai o galho", "i", 60)], XE, 960, passo=0.1)


# ---------------- a cadeia: quatro perguntas ----------------
PERG = (("s07", "tem anel?"), ("s08", "tem galhos?"), ("s09", "tem dupla ou tripla?"), ("s10", "tem heteroátomo?"))


def coluna(c, t, C, atual):
    for k, (sid, q) in enumerate(PERG):
        if t < C[sid + ".a"]:
            continue
        y = 260 + k * 130
        cor = COR if k == atual else TINTA2
        E.foco(c, t, C[sid + ".a"], 0.4, lambda a, y=y, k=k, cor=cor: (E.bola(c, XE + 36, y - 22, 36, E.COR if k == atual else CINZA, a),
                                                                        centro(c, str(k + 1), XE + 36, y - 4, 44, "g", E.SOBRE, a),
                                                                        E.escreve(c, q, XE + 100, y, 56, "g" if k == atual else "i", cor, a)))


def par(c, t, t0, t1, esq, dir_, rot_e, rot_d, ye=470, esc=120, xs=(1060, 1580)):
    """dois exemplos lado a lado com o nome da resposta embaixo"""
    out = []
    for (M_, rot, tk, x) in ((esq, rot_e, t0, xs[0]), (dir_, rot_d, t1, xs[1])):
        if t >= tk:
            out.append(mol(c, t, tk, M_, x, ye, esc, d=0.6))
            pilula_em(c, t, tk + 0.3, rot, x, ye + 260, 50, TINTA, "g")
        else:
            out.append(None)
    return out


def b_cadeia(c, t, C, b):
    atual = 0 if t < C["s08"] else 1 if t < C["s09"] else 2 if t < C["s10"] else 3 if t < C["s11"] else -1
    if t < C["s11"]:
        coluna(c, t, C, atual)
    if t < C["s08"]:
        def s07():
            par(c, t, C["s07.b"], C["s07.c"], dict(pts=Z5), dict(pts=HEX, ligs=ligs_anel(0, 6)), "aberta", "fechada", esc=110)
            if t >= C["s07.d"]:
                mol(c, t, C["s07.d"], dict(pts=anel(6, 1, 90, 0, 0.8) + [(0, -0.2), (0.87, -0.7)], ligs=ligs_anel(0, 6) + [(0, 6), (6, 7)]), 1180, 930, 65, d=0.6)
                pilula_em(c, t, C["s07.d"] + 0.3, "mista", 1450, 950, 50, E.COR)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    if t < C["s09"]:
        def s08():
            P = par(c, t, C["s08.b"], C["s08.c"], dict(pts=Z5), MB, "normal", "ramificada", esc=120)
            if P[0] and t >= C["s08.b"] + 0.5:
                for i in (0, 4):
                    anelc(c, t, C["s08.b"] + 0.5, P[0], i, 26)
            if P[1] and t >= C["s08.c"] + 0.5:
                for i in (0, 3, 4):
                    anelc(c, t, C["s08.c"] + 0.5, P[1], i, 26)
            if t >= C["s08.e"]:
                Pm = mol(c, t, C["s08.e"], MCH, 1450, 950, 55, d=0.5)
                anelc(c, t, C["s08.e"] + 0.5, Pm, 6, 22)
                E.foco(c, t, C["s08.e"] + 0.6, 0.4, lambda a: E.escreve(c, "no anel: galho", 1560, 960, 48, "i", COR, a))
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    if t < C["s10"]:
        def s09():
            P = par(c, t, C["s09.b"], C["s09.c"], dict(pts=Z4), dict(pts=Z4, duplas={(1, 2)}), "saturada", "insaturada", esc=140)
            if P[1]:
                realce(c, t, C["s09.c"] + 0.4, P[1][1], P[1][2], largura=34)
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    if t < C["s11"]:
        def s10():
            E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "heteroátomo: nem C, nem H", 960, 300, 50, "i", TINTA2, a))
            P = par(c, t, C["s10.d"], C["s10.c"], dict(pts=Z5), dict(pts=Z5, rot={2: "O"}), "homogênea", "heterogênea", esc=110)
            if P[1]:
                halo(c, t, C["s10.c"] + 0.3, [P[1][2]], 56)
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    # s11: o anel aromático
    E.frase(c, t, C["s11.a"], ps("um anel especial:", "i", 72), XE, 220, passo=0.12)
    E.frase(c, t, C["s11.a"] + 1.0, ps("6 carbonos, dupla e simples alternadas", "i", 58, TINTA2), XE, 320, passo=0.08)
    P = mol(c, t, C["s11.a"] + 0.4, BENZ, 1350, 580, 190, d=1.0)
    for k, (i, j) in enumerate(((0, 1), (2, 3), (4, 5))):
        realce(c, t, C["s11.a"] + 1.8 + 0.3 * k, P[i], P[j], largura=30)
    E.frase(c, t, C["s11.b"], [("cadeia", "i", 84), ("aromática", "g", 90, COR)], XE, 620, passo=0.12)
    pilula_em(c, t, C["s11.c"], "o nome benzeno: próxima aula", XE + 380, 820, 46, TINTA2, "b")


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    E.frase(c, t, C["s12"], ps("as 4 perguntas neste bastão", "i", 70), XE, 200, passo=0.12)
    P = mol(c, t, C["s12"] + 0.3, MBE, 1450, 560, 190)
    resp = (("s12.a", "sem anel", "aberta"), ("s12.b", "3 pontas", "ramificada"), ("s12.c", "dupla entre C", "insaturada"), ("s12.d", "só C e H", "homogênea"))
    for k, (key, por, r) in enumerate(resp):
        y = 360 + k * 150
        E.foco(c, t, C[key], 0.4, lambda a, por=por, y=y: E.escreve(c, por, XE, y, 54, "i", TINTA2, a))
        pilula_esq(c, t, C[key] + 0.3, r, XE + 420, y - 18, 56, E.COR, "g")
    for i in (0, 3, 4):
        anelc(c, t, C["s12.b"] + 0.3, P, i, 28, t1=C["s12.c"])
    realce(c, t, C["s12.c"] + 0.3, P[0], P[1], largura=34)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("na quarta pergunta", "i", 70), XE + 450, 190, passo=0.12)
    cx = cond(c, t, C["s13.b"], ["CH3", "CH2", "OH"], XE, 430, 130, passo=0.3, cores={2: Q.cor_el("O")})

    def errado():
        E.frase(c, t, C["s13.c"], [("heterogênea?", "g", 70, ERRADO)], 1200, 420)
        if t >= C["s13.c"] + 0.8:
            E.risco(c, 1180, 440, 1640, 360, t, C["s13.c"] + 0.8, largura=10)
    E.saida(c, t, C["s14.a"] + 0.5, errado)
    if t >= C["s14.a"]:
        x0, x1 = cx[2]
        E.caixa_pontilhada(c, x0 - 10, 320, x1 - x0 + 20, 150, ep(t, C["s14.a"], 0.4), E.COR, prog_=ep(t, C["s14.a"], 0.4))
        E.frase(c, t, C["s14.a"] + 0.3, ps("o O está na ponta, preso a 1 carbono", "i", 54, TINTA2), XE, 560, passo=0.08)
        pilula_esq(c, t, C["s14.b"], "homogênea", 1200, 400, 56, E.COR, "g")
        E.foco(c, t, C["s14.b"] + 0.4, 0.4, lambda a: E.selo(c, 1620, 400, 44, True, a))
    if t >= C["s14.c"]:
        cx2 = cond(c, t, C["s14.c"], ["CH3", "O", "CH3"], XE, 820, 130, passo=0.3, cores={1: Q.cor_el("O")})
        x0, x1 = cx2[1]
        halo(c, t, C["s14.c"] + 0.8, [((x0 + x1) / 2, 775)], 70)
        E.frase(c, t, C["s14.c"] + 0.8, ps("O entre dois carbonos", "i", 54, TINTA2), XE, 940, passo=0.08)
        pilula_esq(c, t, C["s14.d"], "heterogênea", 1200, 790, 56, E.COR, "g")
        E.foco(c, t, C["s14.d"] + 0.4, 0.4, lambda a: E.selo(c, 1640, 790, 44, True, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s16"]:
        def s15():
            E.frase(c, t, C["s15.a"], ps("o atalho dos galhos", "i", 72, CLARO), W / 2, 170, "center", 0.12)
            E.frase(c, t, C["s15.b"], [("procure um", "i", 70, CLARO), ("terciário", "g", 70, BR), ("ou", "i", 70, CLARO), ("quaternário", "g", 70, BR)], XE, 330, passo=0.12)
            E.frase(c, t, C["s15.c"], [("achou?", "i", 70, CLARO), ("ramificada", "g", 76, E.CLARO)], XE, 470, passo=0.12)
            E.frase(c, t, C["s15.d"], [("só P e S?", "i", 70, CLARO), ("normal", "g", 76, BR)], XE, 590, passo=0.12)
            P = mol(c, t, C["s15.a"] + 0.4, MB, 1400, 820, 150, escuro=True)
            tipo(c, t, C["s15.b"] + 1.4, P, 1, "T", dx=-56, dy=36)
        E.saida(c, t, C["s16"] - 0.1, s15)
        return
    E.frase(c, t, C["s16.a"], ps("numa fila sem galhos:", "i", 66, CLARO), XE, 200, passo=0.12)
    P = mol(c, t, C["s16.a"] + 0.3, dict(pts=Z5), 700, 420, 150, escuro=True)
    for k, j in enumerate((1, 3)):
        realce(c, t, C["s16.a"] + 1.0 + 0.2 * k, P[2], P[j], E.CLARO)
    E.foco(c, t, C["s16.a"] + 1.4, 0.4, lambda a: E.escreve(c, "no máximo 2 vizinhos", XE, 620, 60, "g", BR, a))
    E.frase(c, t, C["s16.b"], [("o 3º vizinho", "i", 66, CLARO), ("=", "g", 66, CLARO), ("galho", "g", 70, E.CLARO)], XE, 760, passo=0.12)
    if t >= C["s16.c"]:
        Pm = mol(c, t, C["s16.c"], MCH, 1450, 640, 110, escuro=True, d=0.6)
        tipo(c, t, C["s16.c"] + 0.6, Pm, 0, "T", dx=70, dy=10)
        E.foco(c, t, C["s16.c"] + 0.8, 0.4, lambda a: centro(c, "vale até no anel", 1450, 960, 56, "i", CLARO, a))


# ---------------- questão ----------------
QX, QY, QE = 1400, 620, 150


def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 180)
    mol(c, t, C["s17.a"] - 0.4, MCH, QX, QY, QE)
    E.frase(c, t, C["s17.a"], [("1", "g", 56, COR)] + ps("classifique a cadeia:", "i", 60), XE, 340, passo=0.1)
    E.frase(c, t, C["s17.a"] + 1.0, ps("anel, galho, dupla, heteroátomo", "i", 52, TINTA2), XE + 60, 420, passo=0.08)
    E.frase(c, t, C["s17.b"], [("2", "g", 56, COR)] + ps("quantos primários,", "i", 60), XE, 560, passo=0.1)
    E.frase(c, t, C["s17.b"] + 0.8, ps("secundários e terciários?", "i", 60), XE + 60, 640, passo=0.1)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=XE + 260, cy=850, r=90)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    P = mol(c, t, C["s19"] - 0.5, MCH, QX, QY, QE)
    resp = (("s19.a", "mista", "alguns livros: fechada"), ("s19.b", "ramificada", None), ("s19.c", "saturada", None),
            ("s19.d", "homogênea", None), ("s19.e", "não aromática", None))
    if t < C["s20"]:
        def lista_r():
            for k, (key, r, nota) in enumerate(resp):
                y = 230 + k * 120
                pilula_esq(c, t, C[key], r, XE, y, 54, E.COR if k < 4 else TINTA2, "g")
                if nota:
                    E.foco(c, t, C[key] + 0.6, 0.4, lambda a, y=y: E.escreve(c, nota, XE + 290, y + 16, 40, "i", TINTA2, a))
        E.saida(c, t, C["s20"] - 0.1, lista_r)
        anelc(c, t, C["s19.a"] + 0.3, P, 6, 30, t1=C["s19.b"])
        tipo(c, t, C["s19.b"] + 0.3, P, 0, "T", dx=70, dy=10)
        return
    tipo(c, t, C["s20.a"], P, 6, "P", dx=70, dy=0)
    tipo(c, t, C["s20.b"], P, 0, "T", dx=70, dy=10)
    for k, i in enumerate((1, 2, 3, 4, 5)):
        tipo(c, t, C["s20.c"] + 0.15 * k, P, i, "S", dx=(P[i][0] - QX) * 0.45, dy=(P[i][1] - QY) * 0.45)
    E.frase(c, t, C["s20.a"], [("1", "g", 70, COR), ("primário", "i", 70)], XE, 400, passo=0.1)
    E.frase(c, t, C["s20.c"], [("5", "g", 70, COR), ("secundários", "i", 70)], XE, 540, passo=0.1)
    E.frase(c, t, C["s20.b"], [("1", "g", 70, COR), ("terciário", "i", 70)], XE, 680, passo=0.1)
    E.foco(c, t, C["s20.d"] + 0.8, 0.4, lambda a: E.selo(c, XE + 600, 540, 56, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        E.frase(c, t, C["s21.a"], [("carbono:", "g", 70), ("conte os", "i", 74), ("carbonos vizinhos", "g", 70, COR)], XE, 400, passo=0.12)
        E.frase(c, t, C["s21.b"], [("cadeia:", "g", 70), ("4 perguntas", "g", 70, COR)], XE, 560, passo=0.12)
        for k, s in enumerate(("anel", "galho", "dupla", "heteroátomo")):
            pilula_esq(c, t, C["s21.b"] + 1.0 + 0.3 * k, s, XE + [0, 200, 420, 640][k], 700, 50, TINTA, "i")
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.a"], [("prefixo,", "g", 90, COR), ("infixo", "g", 90), ("e", "i", 90), ("sufixo", "g", 90, TINTA2)], XE, 400, passo=0.14)
    nome(c, t, C["s22.b"], [("pent-", COR), ("2-", TINTA2), ("en", TINTA), ("o", TINTA2)], XE, 600, 110, passo=0.25)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, carbonos=b_carbonos, cadeia=b_cadeia, exemplo=b_exemplo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
