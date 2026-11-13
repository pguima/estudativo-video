"""Visual — Estudativo · QUI-ORG-005: praticando cadeias e hidrocarbonetos (4 questões).
Segue a linguagem da Química (QUI-MIS-001) e da Orgânica (QUI-ORG-001). Cada questão: o número grande na cor da matéria no
alto, a molécula à direita, as perguntas à esquerda e o relógio de pausa; na resposta a molécula fica no lugar e ganha as
marcas (bolinhas numeradas, rótulos de H, P/S/T, pílulas da classificação).
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
ARQUIVO_FINAL = "estudativo_QUI-ORG-005_praticando_cadeias_hidrocarbonetos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "fim"))

Z3, Z4 = Q.zigzag(3), Q.zigzag(4)
BUT = dict(pts=Z4)
ISOB = dict(pts=Z3 + [(Z3[1][0], Z3[1][1] + 1)], ligs=[(0, 1), (1, 2), (1, 3)])
HX = anel(6)
LIM = dict(pts=HX + [(0, -2), (0, 2), (-0.87, 2.5), (0.87, 2.5)], ligs=ligs_anel(0, 6) + [(0, 6), (3, 7), (7, 8), (7, 9)], duplas={(0, 1), (7, 8)})
TOL = dict(pts=HX + [(0, -2)], ligs=ligs_anel(0, 6) + [(0, 6)], duplas={(0, 1), (2, 3), (4, 5)})
assert Q.contar("C4H10") == {"C": 4, "H": 10} and 2 * 4 + 2 == 10
assert len(LIM["pts"]) == 10 and 2 * 10 + 2 - 2 - 2 * 2 == 16
assert len(TOL["pts"]) == 7 and 5 + 3 == 8
assert Q.contar("CH3CH2OCH2CH3") == {"C": 4, "H": 10, "O": 1}


def titulo_q(c, t, t0, n, txt):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 170, 56, a=a), centro(c, str(n), XE + 50, 196, 72, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.2, [(txt, "i", 64, TINTA2)], XE + 140, 192)


def perguntas(c, t, itens, x, y0, dy=100, size=58):
    for k, (ti, txt) in enumerate(itens):
        E.frase(c, t, ti, [("•", "g", size, COR)] + ps(txt, "i", size), x, y0 + k * dy, passo=0.08)


def tipo(c, t, t0, x, y, letra, cor=None, r=28):
    E.foco(c, t, t0, 0.4, lambda a: (E.bola(c, x, y, r, cor, a), centro(c, letra, x, y + r * 0.45, r * 1.25, "g", E.SOBRE, a)))


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    for k, (key, s, M_) in enumerate((("s01.a", "isqueiro", ISOB), ("s01.b", "casca de laranja", LIM), ("s01.c", "anestesia", None), ("s01.d", "tinta", TOL))):
        cx = 300 + k * 440
        pilula_em(c, t, C[key], s, cx, 300, 50, TINTA, "i")
        if M_:
            mol(c, t, C[key] + 0.2, M_, cx, 600, 60 if M_ is not ISOB else 90, d=0.6)
        else:
            Q.formula_em(c, t, C[key] + 0.2, "C4H10O", cx, 620, 70, align="center")
    E.frase(c, t, C["s01.e"], [("4", "g", 80, COR), ("questões", "i", 84), ("de prova", "i", 84)], W / 2, 920, "center", 0.12)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 76, TINTA2), XE, 220, passo=0.12)
    lista(c, t, [(C["s02.a"], [("H escondidos", "g", 66), ("do bastão", "i", 70)]),
                 (C["s02.b"], [("4 perguntas", "g", 66, COR), ("da cadeia", "i", 70)]),
                 (C["s02.c"], [("as regras", "i", 70), ("do nome", "g", 66)])], XE, 400, 150)
    E.foco(c, t, C["s02.d"], 0.5, lambda a: E.pilula(c, "pause em cada questão", 1450, 900, 54, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s02"] + 0.6, 0.8, lambda a: E.simbolo(c, 1500, 500, 190 * a, giro=-6 * math.sin(t * 0.5)), blur=0)


# ---------------- questão 1 ----------------
def b_q1(c, t, C, b):
    titulo_q(c, t, C["s03"], 1, "o gás do isqueiro")
    mol(c, t, C["s03.b"], BUT, 1150, 480, 130)
    pilula_em(c, t, C["s03.b"] + 0.4, "butano", 1150, 640, 46, TINTA, "g")
    mol(c, t, C["s03.c"], ISOB, 1600, 450, 130)
    pilula_em(c, t, C["s03.c"] + 0.4, "ramificado", 1600, 690, 46, TINTA, "g")
    perguntas(c, t, [(C["s03.d"], "fórmula molecular de cada um?"), (C["s03.e"], "nome oficial do ramificado?")], XE, 840)
    if t >= C["s04"]:
        E.relogio(c, t, C["s04.a"], cx=XE + 200, cy=480, r=90)


def b_r1(c, t, C, b):
    titulo_q(c, t, C["s05"] - 0.3, 1, "o gás do isqueiro")
    P1 = mol(c, t, C["s05"] - 0.3, BUT, 1150, 480, 130)
    P2 = mol(c, t, C["s05"] - 0.3, ISOB, 1600, 450, 130)
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], ps("4 carbonos, só simples", "i", 58), XE, 330, passo=0.1)
        E.formula_em(c, t, C["s05.b"], "2 × 4 + 2 = 10", XE, 440, 66, "g", TINTA2)
        Q.formula_em(c, t, C["s05.c"], "C4H10", 1150, 720, 80, align="center", cores={"indice": E.COR})
        Q.formula_em(c, t, C["s05.c"] + 0.3, "C4H10", 1600, 760, 80, align="center", cores={"indice": E.COR})
        realca_fila(c, t, C["s05.d"], P2, [0, 1, 2])
        if t >= C["s05.e"]:
            numera_ = [0, 1, 2]
            for k, i in enumerate(numera_):
                tipo(c, t, C["s05.e"] + 0.15 * k, P2[i][0], P2[i][1] - 50, str(k + 1))
        nome(c, t, C["s05.f"], [("2-", TINTA2, "posição"), ("metil", COR, "galho"), ("propano", TINTA, "cadeia")], XE, 930, 100, 0.3)
        E.foco(c, t, C["s05.f"] + 2.0, 0.4, lambda a: E.escreve(c, "ou só metilpropano", XE + 900, 920, 46, "i", TINTA2, a))
        return
    Q.formula(c, "C4H10", 1150, 720, 80, align="center", cores={"indice": E.COR})
    Q.formula(c, "C4H10", 1600, 760, 80, align="center", cores={"indice": E.COR})
    E.frase(c, t, C["s06.a"], [("mesma fórmula,", "i", 70), ("desenhos diferentes", "g", 66, COR)], XE, 930, passo=0.12)
    pilula_em(c, t, C["s06.a"] + 1.6, "isso tem nome: outra aula", XE + 330, 1010, 40, TINTA2, "b")


# ---------------- questão 2 ----------------
LX, LY, LE = 1400, 470, 105


def b_q2(c, t, C, b):
    titulo_q(c, t, C["s07"], 2, "o cheiro da laranja")
    mol(c, t, C["s07.b"], LIM, LX, LY, LE)
    E.frase(c, t, C["s07.b"], [("limoneno", "g", 70, COR)], XE, 340)
    perguntas(c, t, [(C["s07.c"], "fórmula molecular?"), (C["s07.d"], "classificação da cadeia?")], XE, 480)
    if t >= C["s08"]:
        E.relogio(c, t, C["s08.a"], cx=XE + 260, cy=800, r=90)


def b_r2(c, t, C, b):
    P = mol(c, t, C["s09"] - 0.4, LIM, LX, LY, LE)
    titulo_q(c, t, C["s09"] - 0.4, 2, "limoneno")
    if t < C["s10"]:
        for k, i in enumerate(range(6)):
            anelc(c, t, C["s09.a"] + 0.08 * k, P, i, 24)
        anelc(c, t, C["s09.b"], P, 6, 24)
        for k, i in enumerate((7, 8, 9)):
            anelc(c, t, C["s09.c"] + 0.12 * k, P, i, 24)
        E.frase(c, t, C["s09.a"], [("6", "g", 66, COR), ("no anel", "i", 66)], XE, 360, passo=0.1)
        E.frase(c, t, C["s09.b"], [("+ 1", "g", 66, COR), ("em cima", "i", 66)], XE, 460, passo=0.1)
        E.frase(c, t, C["s09.c"], [("+ 3", "g", 66, COR), ("embaixo", "i", 66)], XE, 560, passo=0.1)
        bola_txt(c, t, C["s09.d"], "10", XE + 70, 700, 60, 60)
        E.foco(c, t, C["s09.d"] + 0.3, 0.4, lambda a: E.escreve(c, "carbonos", XE + 160, 720, 66, "i", TINTA, a))
        return
    if t < C["s11"]:
        def s10():
            E.formula_em(c, t, C["s10.a"], "2 × 10 + 2 = 22", XE, 340, 70, "g", TINTA)
            E.formula_em(c, t, C["s10.b"], "− 2 do anel", XE, 450, 66, "g", COR)
            E.foco(c, t, C["s10.b"] + 1.0, 0.4, lambda a: E.escreve(c, "fechar o anel: 2 pontas perdem 1 H cada", XE, 520, 42, "i", TINTA2, a))
            E.formula_em(c, t, C["s10.c"], "− 2 − 2 das duplas", XE, 630, 66, "g", COR)
            E.formula_em(c, t, C["s10.d"], "22 − 6 = 16", XE, 750, 70, "g", TINTA)
            Q.formula_em(c, t, C["s10.e"], "C10H16", XE, 900, 120, cores={"indice": E.COR})
            realce(c, t, C["s10.c"] + 0.3, P[0], P[1], largura=30)
            realce(c, t, C["s10.c"] + 0.5, P[7], P[8], largura=30)
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    resp = (("s11.a", "mista", "alguns livros: fechada"), ("s11.b", "ramificada", None), ("s11.c", "insaturada", None), ("s11.d", "homogênea", None),
            ("s11.e", "não aromática", "uma dupla só no anel"))
    for k, (key, r, nota) in enumerate(resp):
        y = 330 + k * 125
        pilula_esq(c, t, C[key], r, XE, y, 54, E.COR if k < 4 else TINTA2, "g")
        if nota:
            E.foco(c, t, C[key] + 0.6, 0.4, lambda a, y=y, nota=nota: E.escreve(c, nota, XE + 470, y + 16, 40, "i", TINTA2, a))
    Q.formula(c, "C10H16", 1400, 1000, 70, align="center", cores={"indice": E.COR})


# ---------------- questão 3 ----------------
ETER = ["CH3", "CH2", "O", "CH2", "CH3"]


def b_q3(c, t, C, b):
    titulo_q(c, t, C["s12"], 3, "um anestésico antigo")
    E.frase(c, t, C["s12.b"], [("o", "i", 66), ("éter comum", "g", 64, COR)], XE, 340, passo=0.12)
    cond(c, t, C["s12.c"], ETER, W / 2, 560, 110, align="center", cores={2: Q.cor_el("O")}, passo=0.3)
    perguntas(c, t, [(C["s12.d"], "classifique a cadeia"), (C["s12.e"], "cada carbono: primário, secundário ou terciário?")], XE, 760, 100, 54)
    if t >= C["s13"]:
        E.relogio(c, t, C["s13.a"], cx=1650, cy=800, r=80)


def b_r3(c, t, C, b):
    titulo_q(c, t, C["s14"] - 0.4, 3, "éter comum")
    cx = cond(c, t, C["s14"] - 0.4, ETER, W / 2, 460, 110, align="center", cores={2: Q.cor_el("O")}, passo=0)
    if t < C["s15"]:
        resp = (("s14.a", "aberta"), ("s14.b", "normal"), ("s14.c", "saturada"), ("s14.d", "heterogênea"))
        for k, (key, r) in enumerate(resp):
            pilula_esq(c, t, C[key], r, XE + k * 420, 700, 56, E.COR, "g")
        x0, x1 = cx[2]
        halo(c, t, C["s14.d"], [((x0 + x1) / 2, 420)], 60)
        return
    x0, x1 = cx[1]
    q = ep(t, C["s15.b"], 0.4)
    E.caixa_pontilhada(c, x0 - 10, 360, x1 - x0 + 20, 140, q, E.COR, prog_=q)
    E.frase(c, t, C["s15.a"], [("a pegadinha:", "g", 60, ERRADO)], XE, 650)
    E.frase(c, t, C["s15.b"], ps("o O não conta como vizinho", "i", 58), XE, 750, passo=0.1)
    E.frase(c, t, C["s15.c"], [("1", "g", 58, COR)] + ps("carbono vizinho:", "i", 58) + [("primário", "g", 56, COR)], XE, 850, passo=0.1)
    for k, i in enumerate((0, 1, 3, 4)):
        a0, a1 = cx[i]
        tipo(c, t, (C["s15.d"] if i == 1 else C["s15.e"]) + 0.1 * k, (a0 + a1) / 2, 560, "P")
    E.foco(c, t, C["s15.e"] + 0.6, 0.4, lambda a: E.escreve(c, "os 4 são primários", 1250, 860, 60, "g", COR, a))


# ---------------- questão 4 ----------------
TX, TY, TE = 1450, 560, 140


def b_q4(c, t, C, b):
    titulo_q(c, t, C["s16"], 4, "um solvente de tintas")
    mol(c, t, C["s16.b"], TOL, TX, TY, TE)
    E.frase(c, t, C["s16.b"], [("tolueno", "g", 70, COR)], XE, 340)
    E.frase(c, t, C["s16.b"] + 1.0, ps("benzeno + galho de 1 C", "i", 54, TINTA2), XE, 430, passo=0.1)
    perguntas(c, t, [(C["s16.c"], "nome oficial?"), (C["s16.d"], "fórmula molecular?")], XE, 600)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=XE + 260, cy=860, r=80)


def b_r4(c, t, C, b):
    P = mol(c, t, C["s18"] - 0.4, TOL, TX, TY, TE)
    titulo_q(c, t, C["s18"] - 0.4, 4, "tolueno")
    if t < C["s19"]:
        anelc(c, t, C["s18.a"], P, 6, 30)
        nome(c, t, C["s18.b"], [("metil", COR, "galho"), ("benzeno", TINTA, "anel")], XE, 520, 110, 0.4)
        E.frase(c, t, C["s18.c"], ps("um galho só: qualquer carbono do anel é o 1", "i", 52, TINTA2), XE, 720, passo=0.08)
        return
    viz = viz_de(7, TOL["ligs"])
    E.frase(c, t, C["s19.a"], [("7", "g", 66, COR), ("carbonos", "i", 66)], XE, 330, passo=0.1)
    E.frase(c, t, C["s19.b"], ps("no anel: dupla + simples = 3", "i", 56), XE, 440, passo=0.08)
    for k, i in enumerate((1, 2, 3, 4, 5)):
        hs(c, t, C["s19.b"] + 0.8 + 0.12 * k, P, i, viz[i], 1, 50, COR, dist=60)
    E.frase(c, t, C["s19.c"], ps("o que segura o galho: 0 H", "i", 56, TINTA2), XE, 540, passo=0.08)
    anelc(c, t, C["s19.c"] + 0.3, P, 0, 28, CINZA)
    hs(c, t, C["s19.e"], P, 6, viz[6], 3, 54, COR, dist=70)
    E.formula_em(c, t, C["s19.d"], "5 + 3 = 8 H", XE, 680, 66, "g", TINTA)
    Q.formula_em(c, t, C["s19.f"], "C7H8", XE, 880, 130, cores={"indice": E.COR})


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("o método", "i", 92, COR)], W / 2, 180, "center")
        lista(c, t, [(C["s20.a"], [("conte os C", "g", 62), ("de ponta e de dobra", "i", 66)]),
                     (C["s20.b"], [("confira os H", "g", 62), ("pelo atalho", "i", 66)]),
                     (C["s20.c"], [("4 perguntas", "g", 62, COR), ("da cadeia", "i", 66)]),
                     (C["s20.d"], [("o nome", "g", 62), ("pela maior fila", "i", 66)])], XE, 360, 150)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("álcool,", "g", 96, COR), ("fenol", "g", 96), ("e", "i", 96), ("éter", "g", 96, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s21.b"], ps("todos com oxigênio", "i", 70, TINTA2), XE, 520, passo=0.1)
    Q.formula_em(c, t, C["s21.b"] + 0.4, "–OH", XE + 60, 700, 110, cores={"O": Q.cor_el("O")})
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4, fim=b_fim)
