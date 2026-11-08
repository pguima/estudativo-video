"""Visual — Estudativo · MAT-TRI-003: ângulos notáveis 30°, 45° e 60° (do quadrado de lado 1 e do equilátero de lado 2) e o macete da
tabela (seno = √1, √2, √3 sobre 2; cosseno ao contrário; tangente = seno ÷ cosseno).
Linguagem da Trigonometria (MAT-TRI-001): lados em tinta; cada lado ganha a cor fixa do seu nome a partir do ângulo da vez —
OPO âmbar (cateto oposto), ADJ petróleo (cateto adjacente), HIP índigo (hipotenusa); ângulo da vez = arco com cunha na cor da
matéria; ângulo reto = quadradinho; sen, cos e tg abreviados; resposta na esfera; erro em vermelho, certo em verde; atalho no palco.
A figura não mente: o quadrado é quadrado, o equilátero tem altura √3 de verdade e a metade tem 30° no topo.
Peças locais: as da MAT-TRI-001 (grosso, rot, tri, fra, bola_txt) e fl(), linha(), tabela() (a tabela 3 × 3 dos notáveis).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-003_angulos_notaveis_30_45_60.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("quadrado", "equilatero", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
HIP, OPO, ADJ = E.COR, AMBAR, "#0E9AA7"      # cor fixa de cada lado da trigonometria (MAT-TRI-001)
ADJ_ESC = "#3CC7D3"                         # o adjacente no palco escuro
R2, R3 = math.sqrt(2), math.sqrt(3)
assert abs(1 / R2 - R2 / 2) < 1e-12 and 2 ** 2 - 1 ** 2 == 3 and 180 - 90 - 60 == 30 and abs(1 / R3 - R3 / 3) < 1e-12
assert abs(R3 / 3 - 0.577) < 0.001 and round(1.7 / 3, 2) == 0.57
assert abs((R2 / 2) ** 2 + (R3 / 3) * R3 - 1.5) < 1e-12


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trigonometria ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def grosso(c, P, Q, cor, a, larg=12, p=1.0, dash=None):
    """o lado com nome: traço grosso na cor fixa, por cima do contorno preto"""
    if a > 0 and p > 0:
        M.line(c, *P, *Q, cor, a, larg, progress=p, dash=dash)


def rot(c, P, Q, s, G, size=60, cor=None, a=1.0, gap=20, est="b"):
    """rótulo ao lado do segmento PQ, do lado de fora do triângulo de centro G"""
    if a <= 0 or not s:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
    if (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 < (mx - G[0]) ** 2 + (my - G[1]) ** 2:
        nx, ny = -nx, -ny
    E._cola(c, s, mx, my, nx, ny, gap, size, est, cor or TINTA, a)


def tri(c, t, t0, A, R, T, med=("4", "3", "5"), tm=None, cores=None, nomes=None, tn=None, alfa=None, aceso=None, size=64, escuro=False,
        d=0.9, tri_t0=True):
    """triângulo retângulo: A = vértice do ângulo da vez, R = ângulo reto, T = o outro vértice.
    Lados: "adj" = A–R, "opo" = R–T, "hip" = A–T. med = medidas (adj, opo, hip); tm = {lado: instante da medida};
    cores = {lado: (instante, cor)} pinta o lado com o nome; nomes = {lado: texto}, tn = {lado: instante};
    alfa = (instante, rótulo, vértice, vizinho1, vizinho2) ou None; aceso = conjunto de lados acesos (os outros afinam)"""
    G = ((A[0] + R[0] + T[0]) / 3, (A[1] + R[1] + T[1]) / 3)
    E.triangulo(c, t, t0, A, R, T, vertices=None, retos=(1,), preenche=0.07, d=d, escuro=escuro)
    seg = {"adj": (A, R), "opo": (R, T), "hip": (A, T)}
    idx = {"adj": 0, "opo": 1, "hip": 2}
    cores = cores or {}
    tm = tm or {}
    for k, (P, Q) in seg.items():
        cor_k = None
        if k in cores and t >= cores[k][0]:
            cor_k = cores[k][1]
            vis = 1.0 if aceso is None or k in aceso else 0.25
            grosso(c, P, Q, cor_k, vis, 12, ease_io(prog(t, cores[k][0], 0.5)))
        if k in tm and med[idx[k]]:
            cor_t = cor_k or ("#FFFFFF" if escuro else TINTA)
            E.foco(c, t, tm[k], 0.4, lambda a, P=P, Q=Q, s=med[idx[k]], cor_t=cor_t: rot(c, P, Q, s, G, size, cor_t, a))
        if nomes and k in nomes and tn and k in tn:
            cor_n = cor_k or ("#FFFFFF" if escuro else TINTA)
            wnum = E.formula(None, med[idx[k]] or "", 0, 0, size, "b", a=0)
            dx, dy = abs(Q[0] - P[0]), abs(Q[1] - P[1])
            gap = 30 + (wnum if dy > 2 * dx else size * 0.8 if dx > 2 * dy else max(wnum * 0.7, size * 0.8))
            E.foco(c, t, tn[k], 0.4, lambda a, P=P, Q=Q, s=nomes[k], cor_n=cor_n, gap=gap: rot(c, P, Q, s, G, size * 0.8, cor_n, a, gap, "i"))
    if alfa:
        ta, rotulo, V, V1, V2 = alfa
        E.angulo(c, t, ta, V, V1, V2, rotulo, r=95, size=54)
    return G


def _w(s, size, est="g"):
    return E.formula(None, s, 0, 0, size, est, a=0)


def fra(c, cima, baixo, x, y, size, a=1.0, cc=TINTA, cb=TINTA, est="g", barra=TINTA):
    """fração empilhada com cima e baixo em cores próprias; y = linha de base da conta. Devolve a largura"""
    s_ = size * 0.78
    wc, wb = _w(cima, s_, est), _w(baixo, s_, est)
    w = max(wc, wb) + size * 0.16
    if a > 0:
        E.formula(c, cima, x + (w - wc) / 2, y - size * 0.46, s_, est, cc, a)
        E.formula(c, baixo, x + (w - wb) / 2, y + size * 0.46, s_, est, cb, a)
        b = max(4, size * 0.07)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - size * 0.3 - b / 2, w, b), b / 2, b / 2), M.paint(barra, a))
    return w


def razao(c, nome, cima, cc, baixo, cb, x, y, size, a=1.0, tinta=TINTA, palavra="i"):
    """sen α = cima/baixo, com as palavras coloridas. Devolve o x do fim"""
    w0 = E.formula(c, f"{nome} α = ", x, y, size, "g", tinta, a)
    w1 = fra(c, cima, baixo, x + w0, y, size, a, cc, cb, "g", tinta)
    return x + w0 + w1


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")))


def fl(c, t, t0, s, x, y, size, cor=TINTA, align="left", d=0.5):
    """fórmula que entra com foco; devolve a largura"""
    E.foco(c, t, t0, d, lambda a: E.formula(c, s, x, y, size, "g", cor, a, align))
    return _w(s, size)


def linha_ok(c, partes, x, y, size, a):
    xx = x
    for s, cor in partes:
        xx += E.formula(c, s, xx, y, size, "g", cor, a)
    return xx - x


def linha(c, t, t0, partes, x, y, size, d=0.5):
    E.foco(c, t, t0, d, lambda a: linha_ok(c, partes, x, y, size, a))
    return sum(_w(s, size) for s, _ in partes)


VAL = {("sen", 30): "f{1}{2}", ("sen", 45): "f{r{2}}{2}", ("sen", 60): "f{r{3}}{2}",
       ("cos", 30): "f{r{3}}{2}", ("cos", 45): "f{r{2}}{2}", ("cos", 60): "f{1}{2}",
       ("tg", 30): "f{r{3}}{3}", ("tg", 45): "1", ("tg", 60): "r{3}"}


def tabela(c, t, x0, y0, cw, rh, th, tl, cel, size=72, escuro=False, rotulo=72):
    """tabela 3 × 3: th = instante do cabeçalho; tl = {linha: instante do nome}; cel = {(linha, ângulo): (instante, texto, cor)}"""
    tinta = BR if escuro else TINTA
    a = ep(t, th, 0.5)
    if a > 0:
        for j in range(4):
            M.line(c, x0 + j * cw, y0 - 70, x0 + j * cw, y0 + 40 + 3 * rh, CLARO if escuro else FIO, a, 2)
        for i in range(3):
            M.line(c, x0 - 160, y0 + 40 + i * rh, x0 + 3 * cw, y0 + 40 + i * rh, CLARO if escuro else FIO, a, 2)
    for j, g in enumerate((30, 45, 60)):
        E.foco(c, t, th + 0.15 * j, 0.4, lambda a, j=j, g=g: E.formula(c, f"{g}°", x0 + cw * (j + 0.5), y0, 64, "g", CLARO if escuro else COR, a, "center"))
    for i, nome in enumerate(("sen", "cos", "tg")):
        if nome in tl:
            E.foco(c, t, tl[nome], 0.4, lambda a, i=i, nome=nome: E.escreve(c, nome, x0 - 150, y0 + 40 + (i + 0.5) * rh + rotulo * 0.36, rotulo, "g", tinta, a))
    for (nome, g), (t0, s, cor) in cel.items():
        i, j = ("sen", "cos", "tg").index(nome), (30, 45, 60).index(g)
        E.foco(c, t, t0, 0.4, lambda a, i=i, j=j, s=s, cor=cor: E.formula(c, s, x0 + cw * (j + 0.5), y0 + 40 + (i + 0.5) * rh + size * (0.3 if "f{" in s else 0.36), size, "g", cor or tinta, a, "center"))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def s01():
        for k, (nome, g), y in (("s01.a", ("sen", 30), 300), ("s01.b", ("cos", 45), 520), ("s01.c", ("tg", 60), 740)):
            E.foco(c, t, C[k], 0.5, lambda a, nome=nome, g=g, y=y: linha_ok(c, [(f"{nome} {g}° = ", TINTA), (VAL[(nome, g)], COR)], XE, y, 100, a))
        if t >= C["s01.d"]:
            cel = {}
            for i, nome in enumerate(("sen", "cos", "tg")):
                for j, g in enumerate((30, 45, 60)):
                    cel[(nome, g)] = (C["s01.d"] + 0.3 + 0.12 * (3 * i + j), VAL[(nome, g)], COR if (nome, g) in (("sen", 30), ("cos", 45), ("tg", 60)) else None)
            tabela(c, t, 1100, 340, 230, 190, C["s01.d"], {n: C["s01.d"] + 0.2 for n in ("sen", "cos", "tg")}, cel, 60, rotulo=56)
            E.frase(c, t, C["s01.d"] + 1.8, [("de", "i", 64), ("cabeça", "g", 60, COR)], 1430, 1000, "center")
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 80), XE, 220)
    itens = ((C["s02.a"] + 1.4, [("a tabela com um ", TINTA), ("macete", COR)]), (C["s02.b"], [("de onde vem ", TINTA), ("cada número", COR)]))
    for i, (t0, partes) in enumerate(itens):
        y = 420 + i * 180
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 48, a=a), centro(c, str(i + 1), XE + 40, y - 6, 56, "g", BR, a)))
        linha(c, t, t0 + 0.1, partes, XE + 130, y, 90)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só precisa de", "i", 84), XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "seno, cosseno e tangente", [("sen, cos, tg", COR)]),
             ("s03.c", "quadrado e equilátero", [("diagonal = lado · r{2}", COR)]),
             ("s03.d", "tirar a raiz de baixo", [("f{1}{r{2}} = f{r{2}}{2}", COR)]))
    for i, (k, l1, l2) in enumerate(itens):
        y = 140 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 74)
        linha(c, t, C[k] + 0.3, l2, x + 44, y + 175, 50 if k == "s03.c" else 64)
    E.foco(c, t, C["s03.c"] + 1.2, 0.5, lambda a: E.formula(c, "altura = f{lado · r{3}}{2}", x + 520, 140 + 280 + 175, 50, "g", COR, a))
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(140 + 200, 420 + 200, q1), 700 + 200, q2), ep(t, C["s03.b"], 0.4))


# ---------------- 45°: o quadrado ----------------
QX, QY, QL = 200, 300, 440
QBL, QBR, QTL, QTR = (QX, QY + QL), (QX + QL, QY + QL), (QX, QY), (QX + QL, QY)


def b_quadrado(c, t, C, b):
    a4 = C["s04.a"]
    E.quadrado(c, t, a4, QX, QY, QL, None, preenche=0.0, d=0.8)
    E.foco(c, t, a4 + 0.8, 0.4, lambda a: (E._cola(c, "1", (QBL[0] + QBR[0]) / 2, QBL[1], 0, 1, 18, 64, "g", TINTA, a),
                                           E._cola(c, "1", QBL[0], (QBL[1] + QTL[1]) / 2, -1, 0, 18, 64, "g", TINTA, a)))
    if t >= C["s04.b"]:
        M.line(c, *QTL, *QBR, TINTA, 1.0, 6, progress=ease_io(prog(t, C["s04.b"], 0.6)))
    s05 = t >= C["s05"]
    if not s05:
        E.foco(c, t, C["s04.b"] + 0.5, 0.4, lambda a: E._cola(c, "r{2}", (QTL[0] + QBR[0]) / 2, (QTL[1] + QBR[1]) / 2, 1, -1, 16, 64, "g", COR, a))
    # os dois triângulos
    k = ep(t, C["s04.c"], 0.5)
    if k > 0:
        for pts, al in (([QTL, QBL, QBR], 0.16), ([QTL, QTR, QBR], 0.06)):
            path = skia.Path(); path.addPoly(pts, True)
            c.drawPath(path, M.paint(COR, al * k))
    if s05:
        tri(c, t, C["s05"], QBR, QBL, QTL, ("1", "1", "r{2}"), tm={k_: C["s05"] for k_ in ("adj", "opo", "hip")},
            cores={"opo": (C["s05.a"], OPO), "adj": (C["s05.a"] + 0.3, ADJ), "hip": (C["s05.a"] + 0.6, HIP)}, size=64)
    # os ângulos de 45°
    E.angulo(c, t, C["s04.d"], QBR, QBL, QTL, "45°" if t >= C["s04.e"] else None, r=110, size=50)
    E.angulo(c, t, C["s04.d"] + 0.3, QTL, QBR, QBL, "45°" if t >= C["s04.e"] else None, r=110, size=50)
    X = 860

    def s04():
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.escreve(c, "2 triângulos retângulos", X, 300, 60, "g", TINTA, a))
        E.foco(c, t, C["s04.d"], 0.5, lambda a: E.escreve(c, "catetos iguais, ângulos iguais", X, 430, 54, "i", TINTA, a))
        E.foco(c, t, C["s04.d"] + 2.4, 0.5, lambda a: E.formula(c, "agudos: 180° − 90° = 90°", X, 560, 60, "g", TINTA2, a))
        fl(c, t, C["s04.e"], "90° ÷ 2 = 45°", X, 720, 110, COR)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if not s05:
        return
    E.foco(c, t, C["s05.a"], 0.5, lambda a: linha_ok(c, [("oposto 1", OPO), ("  adjacente 1", ADJ), ("  hipotenusa r{2}", HIP)], X, 240, 52, a))
    fl(c, t, C["s05.b"], "sen 45° = f{1}{r{2}}", X, 420, 84)
    E.foco(c, t, C["s05.c"], 0.5, lambda a: E.formula(c, " = f{r{2}}{2}", X + _w("sen 45° = f{1}{r{2}}", 84), 420, 84, "g", COR, a))
    fl(c, t, C["s05.d"], "cos 45° = f{r{2}}{2}", X, 620, 84)
    E.foco(c, t, C["s05.d"] + 0.4, 0.4, lambda a: E.escreve(c, "catetos iguais", X + 600, 620, 46, "i", TINTA2, a))
    fl(c, t, C["s05.e"], "tg 45° = f{1}{1} = 1", X, 820, 84)


# ---------------- 30° e 60°: o equilátero ----------------
KQ = 260
EB, EC = (180, 900), (180 + 2 * KQ, 900)
EA = (180 + KQ, 900 - KQ * math.sqrt(3))
EM = (180 + KQ, 900)


def b_equilatero(c, t, C, b):
    a6 = C["s06.a"]
    fim60 = t >= C["s10.a"]
    E.triangulo(c, t, a6, EB, EC, EA, vertices=None, angulos=("60°", "60°", "60°"), ta=(a6 + 0.9, a6 + 1.0, a6 + 1.1),
                preenche=0.04, d=0.9, size=46, r_ang=70) if t < C["s07"] else E.triangulo(c, t, a6, EB, EC, EA, vertices=None, preenche=0.04, d=0.9)
    E.foco(c, t, a6 + 0.8, 0.4, lambda a: E._cola(c, "2", (EC[0] + EA[0]) / 2, (EC[1] + EA[1]) / 2, 1, -0.5, 16, 56, "g", TINTA2, a))
    if t >= C["s06.b"]:
        M.line(c, *EA, *EM, TINTA, 1.0, 5, dash=E.TRACO, progress=ease_io(prog(t, C["s06.b"], 0.6)))
        E.angulo(c, t, C["s06.b"] + 0.6, EM, EC, EA, r=40)
    # a metade da esquerda: hipotenusa A–B (2), base B–M (1), altura M–A (√3)
    k = ep(t, C["s06.c"], 0.5)
    if k > 0:
        path = skia.Path(); path.addPoly([EA, EB, EM], True)
        c.drawPath(path, M.paint(COR, 0.14 * k))
    G = ((EA[0] + EB[0] + EM[0]) / 3, (EA[1] + EB[1] + EM[1]) / 3)
    # cores: para 30° (no topo) o 1 é o oposto; para 60° (embaixo) o √3 é o oposto
    if C["s07.c"] <= t < C["s10.a"]:
        grosso(c, EB, EM, OPO, 1.0, 12, ease_io(prog(t, C["s07.c"], 0.5)))
        grosso(c, EM, EA, ADJ, 1.0, 12, ease_io(prog(t, C["s08.b"], 0.5)))
    if fim60:
        grosso(c, EM, EA, OPO, 1.0, 12, ease_io(prog(t, C["s10.a"], 0.5)))
        grosso(c, EB, EM, ADJ, 1.0, 12, ease_io(prog(t, C["s10.a"] + 0.3, 0.5)))
    if t >= C["s08.a"]:
        grosso(c, EB, EA, HIP, 1.0, 12, ease_io(prog(t, C["s08.a"], 0.5)))
    cor1 = ADJ if fim60 else OPO if t >= C["s07.c"] else TINTA
    cor3 = OPO if fim60 else ADJ if t >= C["s08.b"] else TINTA
    E.foco(c, t, C["s06.c"], 0.4, lambda a: rot(c, EB, EA, "2", G, 64, HIP if t >= C["s08.a"] else TINTA, a))
    E.foco(c, t, C["s06.d"], 0.4, lambda a: E._cola(c, "1", (EB[0] + EM[0]) / 2, EB[1], 0, 1, 16, 64, "g", cor1, a))
    E.foco(c, t, C["s06.e"], 0.4, lambda a: E._cola(c, "r{3}", EM[0] + 6, (EM[1] + EA[1]) / 2 + 40, 1, 0, 14, 60, "g", cor3, a))
    # ângulos da metade
    E.angulo(c, t, C["s07.a"], EB, EM, EA, "60°", r=90, size=50)
    E.angulo(c, t, C["s07.b"], EA, EB, EM, "30°", r=110, size=50)
    X = 860

    def s06_07():
        fl(c, t, C["s06.e"] + 0.5, "2² − 1² = 3", X, 300, 76)
        fl(c, t, C["s06.e"] + 2.4, "altura = r{3}", X, 420, 76, COR)
        fl(c, t, C["s07.b"], "180° − 90° − 60° = 30°", X, 600, 70)
        E.foco(c, t, C["s07.c"], 0.5, lambda a: linha_ok(c, [("30°", COR), (" de frente para o ", TINTA2), ("1", OPO)], X, 760, 64, a))
        E.foco(c, t, C["s07.d"], 0.5, lambda a: linha_ok(c, [("60°", COR), (" de frente para ", TINTA2), ("r{3}", TINTA)], X, 880, 64, a))
    E.saida(c, t, C["s08"] - 0.1, s06_07)
    if t < C["s08"]:
        return

    def s08_09():
        s = 76
        fl(c, t, C["s08.a"], "sen 30° = f{1}{2}", X, 230, s)
        fl(c, t, C["s08.b"], "cos 30° = f{r{3}}{2}", X, 400, s)
        fl(c, t, C["s08.c"], "tg 30° = f{1}{r{3}}", X, 570, s)
        x2 = X + _w("tg 30° = f{1}{r{3}}", s)
        E.foco(c, t, C["s09.d"], 0.5, lambda a: E.formula(c, " = f{r{3}}{3}", x2, 570, s, "g", COR, a))
        fl(c, t, C["s09.a"], "f{1}{r{3}} · f{r{3}}{r{3}}", X, 780, 72, TINTA2)
        x3 = X + _w("f{1}{r{3}} · f{r{3}}{r{3}}", 72)
        E.foco(c, t, C["s09.b"], 0.4, lambda a: E.formula(c, "em cima: r{3}", X, 920, 50, "b", TINTA2, a))
        E.foco(c, t, C["s09.c"], 0.4, lambda a: (E.formula(c, " = f{r{3}}{3}", x3, 780, 72, "g", TINTA, a),
                                                 E.formula(c, "embaixo: r{3} · r{3} = 3", X + 420, 920, 50, "b", TINTA2, a)))
        E.foco(c, t, C["s09.e"], 0.5, lambda a: E.pilula(c, "≈ 0,57", x2 + 330, 560, 50, "g", a=a))
    E.saida(c, t, C["s10"] - 0.1, s08_09)
    if t < C["s10"]:
        return
    E.foco(c, t, C["s10.a"], 0.5, lambda a: E.escreve(c, "60°: os catetos trocam de papel", X, 230, 54, "i", TINTA, a))
    fl(c, t, C["s10.b"], "sen 60° = f{r{3}}{2}", X, 420, 80)
    fl(c, t, C["s10.c"], "cos 60° = f{1}{2}", X, 600, 80)
    fl(c, t, C["s10.d"], "tg 60° = f{r{3}}{1} = r{3}", X, 780, 80)


# ---------------- erro ----------------
KE3 = 300
FB, FM = (240, 900), (240 + KE3, 900)
FA = (FM[0], 900 - KE3 * math.sqrt(3))


def b_erro(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("trocar", "i", 72), ("o", "i", 72), ("30°", "g", 68, ERRADO), ("com", "i", 72), ("o", "i", 72), ("60°", "g", 68, ERRADO)], XE, 150)
    certo = t >= C["s11.d"]
    tri(c, t, C["s11"], FA, FM, FB, ("r{3}", "1", "2"), tm={k: C["s11"] + 0.5 for k in ("adj", "opo", "hip")}, size=64)
    if not certo:
        E.angulo(c, t, C["s11.a"] + 0.6, FB, FM, FA, "30°?", r=100, size=50, cor=ERRADO)
    else:
        E.angulo(c, t, C["s11.d"], FB, FM, FA, "60°", r=100, size=50)
        E.angulo(c, t, C["s11.d"] + 0.3, FA, FB, FM, "30°", r=120, size=50)
        grosso(c, FM, FB, OPO, 1.0, 12, ease_io(prog(t, C["s11.d"] + 0.3, 0.5)))
    X = 860

    def errado():
        E.foco(c, t, C["s11.b"], 0.5, lambda a: (E.formula(c, "sen 30° = f{r{3}}{2}", X, 400, 84, "g", ERRADO, a),
                                                 E.selo(c, X + _w("sen 30° = f{r{3}}{2}", 84) + 70, 370, 40, False, a)))
    E.saida(c, t, C["s11.d"] - 0.1, errado)
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.pilula(c, "menor ângulo ↔ menor lado", X + 380, 620, 54, "g", a=a))
    E.foco(c, t, C["s11.d"], 0.5, lambda a: (E.formula(c, "sen 30° = f{1}{2}", X, 400, 84, "g", CERTO, a),
                                             E.selo(c, X + _w("sen 30° = f{1}{2}", 84) + 70, 370, 40, True, a)))
    E.foco(c, t, C["s11.d"] + 0.6, 0.5, lambda a: linha_ok(c, [("30°", COR), (" de frente para o ", TINTA2), ("1", OPO)], X, 820, 64, a))


# ---------------- atalho (palco escuro): o macete da tabela ----------------
TX0, TY0, TCW, TRH = 620, 250, 330, 200


def b_atalho(c, t, C, b):
    palco(c, t)
    b12, c12 = C["s12.b"], C["s12.c"]
    ts = (b12, lerp(b12, c12, 0.3), lerp(b12, c12, 0.6))
    cel = {}
    for j, g in enumerate((30, 45, 60)):
        s = f"f{{r{{{j + 1}}}}}{{2}}"
        if j == 0 and t >= c12:
            s = "f{1}{2}"
        cel[("sen", g)] = (ts[j], s, BR)
    for j, g in enumerate((30, 45, 60)):
        cel[("cos", g)] = (C["s13.a"] + 0.3 * j, VAL[("cos", g)], BR)
    tg = C["s13.c"]
    cel[("tg", 30)] = (tg, VAL[("tg", 30)], CLARO)
    cel[("tg", 45)] = (lerp(C["s13.c"], C["s14"], 0.45), "1", CLARO)
    cel[("tg", 60)] = (lerp(C["s13.c"], C["s14"], 0.75), "r{3}", CLARO)

    def tab():
        E.frase(c, t, C["s12"], [("o", "i", 64, CLARO), ("macete", "g", 64, BR), ("da", "i", 64, CLARO), ("tabela", "g", 64, BR)], W / 2, 110, "center")
        tabela(c, t, TX0, TY0, TCW, TRH, C["s12.a"], {"sen": b12 - 0.3, "cos": C["s13.a"], "tg": C["s13.b"]}, cel, 76, escuro=True)
        if C["s12.c"] - 0.3 <= t < C["s12.c"] + 1.6:  # o √1 vira 1
            k = ep(t, C["s12.c"] - 0.3, 0.3) * (1 - ep(t, C["s12.c"] + 1.2, 0.4))
            E.caixa_pontilhada(c, TX0 + 40, TY0 + TRH - 70, TCW - 80, 170, k, CLARO, k)
        if t >= C["s13.a"]:  # a seta que espelha a linha
            p = ep(t, C["s13.a"], 0.6)
            y = TY0 + 40 + 2 * TRH - 22
            M.arrow(c, TX0 + 3 * TCW - 40, y, TX0 + 40, y, CLARO, p, 4, 16, p)
        E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "= f{sen}{cos}", TX0 + 3 * TCW + 24, TY0 + 40 + 2.5 * TRH + 18, 60, "g", CLARO, a))
    E.saida(c, t, C["s14"] - 0.1, tab)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"], ps("por que funciona", "i", 72, CLARO), W / 2, 170, "center")
    E.foco(c, t, C["s14.a"], 0.5, lambda a: E.formula(c, "30° + 60° = 90°", W / 2, 380, 110, "g", BR, a, "center"))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "cos = o seno ao contrário", W / 2, 560, 76, "g", CLARO, a, "center"))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.pilula(c, "só para 30°, 45° e 60°", W / 2, 760, 56, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.formula(c, "37°? a prova dá o valor", W / 2, 940, 64, "g", BR, a, "center"))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s15.a"], ps("sem olhar a tabela", "i", 72), XE, 320)
    fl(c, t, C["s15.b"], "sen 45° · cos 45°", XE, 560, 110)
    fl(c, t, C["s15.c"], "+ tg 30° · tg 60°", XE + 80, 740, 110)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], 1520, 560, 150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x0 = XE

    def s17():
        fl(c, t, C["s17"], "sen 45° · cos 45°", x0, 200, 72, TINTA2)
        fl(c, t, C["s17.a"], "f{r{2}}{2} · f{r{2}}{2}", x0, 420, 96)
        x1 = x0 + _w("f{r{2}}{2} · f{r{2}}{2}", 96)
        E.foco(c, t, C["s17.b"], 0.4, lambda a: E.formula(c, "r{2} · r{2} = 2", x0, 620, 56, "b", TINTA2, a))
        E.foco(c, t, C["s17.c"], 0.4, lambda a: E.formula(c, "2 · 2 = 4", x0 + 420, 620, 56, "b", TINTA2, a))
        fl(c, t, C["s17.b"] + 0.3, " = f{2}{4}" if t < C["s17.d"] else " = f{2}{4} = f{1}{2}", x1, 420, 96)
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.foco(c, t, C["s18"], 0.4, lambda a: linha_ok(c, [("sen 45° · cos 45° = ", TINTA2), ("f{1}{2}", COR)], x0, 200, 64, a))
    fl(c, t, C["s18.a"] - 0.3, "tg 30° · tg 60°", x0, 360, 64, TINTA2)
    fl(c, t, C["s18.a"], "f{r{3}}{3} · r{3}", x0, 560, 96)
    x1 = x0 + _w("f{r{3}}{3} · r{3}", 96)
    E.foco(c, t, C["s18.b"], 0.4, lambda a: E.formula(c, "r{3} · r{3} = 3", x0, 740, 56, "b", TINTA2, a))
    fl(c, t, C["s18.c"], " = f{3}{3} = 1", x1, 560, 96)
    fl(c, t, C["s18.d"], "f{1}{2} + 1 = ", x0, 920, 96)
    bola_txt(c, t, C["s18.d"] + 0.4, "1,5", x0 + _w("f{1}{2} + 1 = ", 96) + 120, 885, 100, 70, CERTO)
    E.foco(c, t, C["s18.d"] + 1.0, 0.4, lambda a: E.escreve(c, "um e meio", x0 + _w("f{1}{2} + 1 = ", 96) + 260, 905, 56, "i", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 160, "center")
        cel = {}
        for j, g in enumerate((30, 45, 60)):
            cel[("sen", g)] = (C["s19.a"] + 0.3 * j, f"f{{r{{{j + 1}}}}}{{2}}", None)
            cel[("cos", g)] = (C["s19.b"] + 0.3 * (2 - j), VAL[("cos", g)], None)
            cel[("tg", g)] = (C["s19.c"] + 0.3 * j, VAL[("tg", g)], COR)
        tabela(c, t, 640, 330, 300, 190, C["s19"], {"sen": C["s19.a"], "cos": C["s19.b"], "tg": C["s19.c"]}, cel, 68)
        E.foco(c, t, C["s19.c"] + 0.2, 0.4, lambda a: E.formula(c, "= f{sen}{cos}", 640 + 3 * 300 + 24, 330 + 40 + 2.5 * 190 + 18, 60, "g", TINTA2, a))
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], ps("próxima aula", "i", 80), XE, 230)
    E.frase(c, t, C["s20"] + 0.6, [("a", "i", 120), ("tabela", "g", 130, COR)], XE, 390)
    E.frase(c, t, C["s20"] + 1.0, [("na", "i", 120), ("rua", "g", 130, COR)], XE, 530)
    E.frase(c, t, C["s20.a"], [("altura", "g", 60), ("da", "i", 64), ("torre", "i", 64)], XE, 670)
    E.frase(c, t, C["s20.b"], [("inclinação", "g", 60), ("da", "i", 64), ("rampa", "i", 64)], XE + 520, 670)
    A, R = (1400, 720), (1400 + 240, 720)
    T = (R[0], R[1] - 240 * math.sqrt(3))
    tri(c, t, C["s20.a"], A, R, T, ("30 m", "h", None), tm={"adj": C["s20.a"] + 0.4, "opo": C["s20.a"] + 0.4},
        cores={"opo": (C["s20.a"] + 0.4, OPO)}, alfa=(C["s20.a"] + 0.4, "60°", A, R, T), size=52)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 560, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(900, 700, p), lerp(1000, 845, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], 1300, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, quadrado=b_quadrado, equilatero=b_equilatero, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
