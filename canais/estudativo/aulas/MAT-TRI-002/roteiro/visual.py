"""Visual — Estudativo · MAT-TRI-002: achar um lado com seno, cosseno ou tangente (escada 10 m a 37°: altura 6, pé 8; telhado 8 m
a 37°: sobe 6; pipa a 12 m: linha 20).
Linguagem da Trigonometria (MAT-TRI-001): lados em tinta; cada lado ganha a cor fixa do seu nome a partir do ângulo da vez —
OPO âmbar (cateto oposto), ADJ petróleo (cateto adjacente), HIP índigo (hipotenusa); ângulo da vez = arco com cunha na cor da
matéria; ângulo reto = quadradinho; sen, cos e tg abreviados; resposta na esfera; erro em vermelho, certo em verde; atalho no palco.
A figura não mente: escada, telhado e pipa são triângulos 6-8-10 / 12-16-20, cujo ângulo é de verdade 36,9° (≈ 37°).
Peças locais: as da MAT-TRI-001 (grosso, rot, tri, fra, razao, bola_txt) e conta_r(), linha(), parede(), chao(), escada(),
cena_escada(), pipa(), cena_pipa().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-002_achar_um_lado_com_seno_cosseno_ou_tangente.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "tangente", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
HIP, OPO, ADJ = E.COR, AMBAR, "#0E9AA7"      # cor fixa de cada lado da trigonometria (MAT-TRI-001)
ADJ_ESC = "#3CC7D3"                         # o adjacente no palco escuro
assert round(10 * 0.6, 9) == 6 and round(10 * 0.8, 9) == 8 and 36 + 64 == 100 and round(0.75 * 8, 9) == 6
assert abs(math.degrees(math.atan2(6, 8)) - 36.87) < 0.01 and round(12 / 0.6, 9) == 20 and round(12 * 0.6, 9) == 7.2 < 12


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


def conta_r(c, nome, ang, cima, cc, baixo, cb, x, y, size, a=1.0, tinta=TINTA):
    """sen 37° = cima/baixo; devolve o x do fim"""
    w0 = E.formula(c, f"{nome} {ang} = ", x, y, size, "g", tinta, a)
    w1 = fra(c, cima, baixo, x + w0, y, size, a, cc, cb, "g", tinta)
    return x + w0 + w1


def linha(c, t, t0, partes, x, y, size, d=0.5):
    """[(texto, cor)] em fórmula, lado a lado; entra com foco. Devolve o x do fim"""
    def f(a):
        xx = x
        for s, cor in partes:
            xx += E.formula(c, s, xx, y, size, "g", cor, a)
        return xx
    E.foco(c, t, t0, d, f)
    xx = x
    for s, _ in partes:
        xx += _w(s, size)
    return xx


def parede(c, x, ytopo, yb, a=1.0, w=44):
    if a <= 0:
        return
    M.rrect(c, x, ytopo, w, yb - ytopo, 4, TINTA2, 0.85 * a)
    for k in range(int((yb - ytopo) / 46)):
        yy = yb - 30 - k * 46
        M.line(c, x + 6, yy, x + w - 6, yy - 24, "#FFFFFF", 0.45 * a, 3)


def chao(c, x0, x1, y, a=1.0, p=1.0):
    if a > 0 and p > 0:
        M.line(c, x0, y, lerp(x0, x1, p), y, TINTA2, a, 5)
        for k in range(int((x1 - x0) / 40) + 1):
            x = x0 + 20 + k * 40
            if x < lerp(x0, x1, p) - 10:
                M.line(c, x, y + 6, x - 16, y + 26, TINTA2, 0.35 * a, 3)


def escada(c, A, T, cor, a=1.0, p=1.0):
    """a escada de A (pé) até T (topo): dois trilhos e degraus"""
    if a <= 0 or p <= 0:
        return
    ux, uy = E._uni(*A, *T)
    nx, ny = -uy, ux
    L = math.dist(A, T) * p
    B = (A[0] + ux * L, A[1] + uy * L)
    for s in (-14, 14):
        M.line(c, A[0] + nx * s, A[1] + ny * s, B[0] + nx * s, B[1] + ny * s, cor, a, 7)
    k = 30
    while k < L - 10:
        P = (A[0] + ux * k, A[1] + uy * k)
        M.line(c, P[0] - nx * 14, P[1] - ny * 14, P[0] + nx * 14, P[1] + ny * 14, cor, a, 5)
        k += 46


# ---------------- a escada: 10 m a 37° (desenho 6-8-10, o ângulo é de verdade 36,9°) ----------------
KE = 68
EA, ER = (190, 920), (190 + 8 * KE, 920)
ET = (ER[0], ER[1] - 6 * KE)
EG = ((EA[0] + ER[0] + ET[0]) / 3, (EA[1] + ER[1] + ET[1]) / 3)


def cena_escada(c, t, k, rot_opo="?", rot_adj=None, opo_cor=None, adj_cor=None):
    """k = instantes: base, ang, hip (cor da escada), opo, adj (None = não aparece)"""
    a0 = ep(t, k["base"], 0.6)
    chao(c, EA[0] - 90, ER[0] + 120, EA[1], 1.0, a0)
    parede(c, ER[0], ET[1] - 140, ER[1], a0)
    hip_on = k.get("hip") is not None and t >= k["hip"]
    escada(c, EA, ET, HIP if hip_on else TINTA, 1.0, ease_io(prog(t, k["base"] + 0.3, 0.8)))
    if k.get("ang") is not None:
        E.angulo(c, t, k["ang"], EA, ER, ET, "37°", r=120, size=50)
    E.angulo(c, t, k["base"] + 0.9, ER, EA, ET, r=40)
    E.foco(c, t, k.get("hip_txt", k["base"] + 1.0), 0.4, lambda a: rot(c, EA, ET, "10 m", EG, 60, HIP if hip_on else TINTA, a, 34))
    if k.get("opo") is not None and t >= k["opo"]:
        grosso(c, ER, ET, opo_cor or OPO, 1.0, 12, ease_io(prog(t, k["opo"], 0.5)))
        E.foco(c, t, k["opo"] + 0.3, 0.4, lambda a: E._cola(c, rot_opo, ER[0] + 44, (ER[1] + ET[1]) / 2, 1, 0, 20, 64, "g", opo_cor or OPO, a))
    if k.get("adj") is not None and t >= k["adj"]:
        grosso(c, EA, ER, adj_cor or ADJ, 1.0, 12, ease_io(prog(t, k["adj"], 0.5)))
        if rot_adj:
            E.foco(c, t, k["adj"] + 0.3, 0.4, lambda a: E._cola(c, rot_adj, (EA[0] + ER[0]) / 2, EA[1] + 30, 0, 1, 14, 64, "g", adj_cor or ADJ, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def s01():
        cena_escada(c, t, dict(base=C["s01.a"], ang=C["s01.b"], opo=C["s01.c"], hip_txt=C["s01.a"] + 1.0))
        X = 1000
        E.frase(c, t, C["s01.a"] + 0.3, [("escada", "i", 84), ("de", "i", 84), ("10 m", "g", 84, COR)], X, 260)
        E.frase(c, t, C["s01.b"], [("37°", "g", 84, COR), ("com", "i", 84), ("o", "i", 84), ("chão", "i", 84)], X, 390)
        E.frase(c, t, C["s01.c"], [("a", "i", 84), ("que", "i", 84), ("altura?", "g", 80, OPO)], X, 560)
        E.foco(c, t, C["s01.d"], 0.5, lambda a: E.pilula(c, "Pitágoras não resolve: só 1 lado", X + 420, 760, 46, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 80), XE, 220)
    itens = ((C["s02.a"] + 1.4, [("escolher a ", TINTA), ("razão certa", COR)]),
             (C["s02.b"], [("ângulo + um lado  →  ", TINTA), ("o que falta", COR)]))
    for i, (t0, partes) in enumerate(itens):
        y = 420 + i * 180
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 48, a=a), centro(c, str(i + 1), XE + 40, y - 6, 56, "g", BR, a)))
        linha(c, t, t0 + 0.1, partes, XE + 130, y, 84)
    E.foco(c, t, C["s02.b"] + 2.6, 0.5, lambda a: E.pilula(c, "+ atalho de prova", 1420, 860, 60, "g", a=a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só precisa de", "i", 84), XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, 130, w, 500, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("seno, cosseno e tangente", "i", 56)], x + 44, 205)
    for i, (nome, cima, cc, baixo, cb) in enumerate((("sen", "oposto", OPO, "hipotenusa", HIP), ("cos", "adjacente", ADJ, "hipotenusa", HIP), ("tg", "oposto", OPO, "adjacente", ADJ))):
        E.foco(c, t, C["s03.b"] + 0.6 + 0.5 * i, 0.5, lambda a, i=i, nome=nome, cima=cima, cc=cc, baixo=baixo, cb=cb: (
            E.formula(c, f"{nome} = ", x + 44, 320 + i * 120, 56, "g", TINTA, a),
            fra(c, cima, baixo, x + 44 + _w("cos = ", 56), 320 + i * 120, 56, a, cc, cb)))
    p = ep(t, C["s03.c"], 0.5)
    E.caixa_pontilhada(c, x, 670, w, 270, p, prog_=p)
    E.frase(c, t, C["s03.c"] + 0.1, [("equação com decimal", "i", 56)], x + 44, 745)
    E.foco(c, t, C["s03.c"] + 0.4, 0.5, lambda a: E.formula(c, "0,6 = f{x}{10}", x + 44, 875, 84, "g", COR, a))
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(130 + 470, 670 + 240, q), ep(t, C["s03.b"], 0.4))


# ---------------- método: as três perguntas e a escada ----------------
def b_metodo(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("escolha", "i", 84), ("a", "i", 84), ("razão", "g", 80, COR), ("certa", "g", 80, COR)], XE, 220)
        for i, (k, s) in enumerate((("s04.b", "qual é o ângulo?"), ("s04.c", "que lado eu conheço?"), ("s04.d", "que lado eu quero?"))):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 52, a=a), centro(c, str(i + 1), XE + 40, y - 6, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], XE + 130, y)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    tb, a8 = C["s05"], C["s08.a"]
    alt = "6 m" if t >= C["s07.d"] else "x"
    cena_escada(c, t, dict(base=tb - 0.3, ang=C["s05.a"], hip=C["s05.b"], opo=C["s05.c"], adj=a8, hip_txt=C["s05.b"]),
                rot_opo=alt, rot_adj="8 m" if t >= C["s08.c"] else "?")
    X = 960
    # as respostas das três perguntas
    E.foco(c, t, C["s05.a"], 0.4, lambda a: (E.bola(c, X + 26, 190, 28, a=a), centro(c, "1", X + 26, 204, 36, "g", BR, a),
                                             linha_ok(c, [("ângulo: ", TINTA2), ("37°", COR)], X + 76, 210, 56, a)))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: (E.bola(c, X + 26, 290, 28, a=a), centro(c, "2", X + 26, 304, 36, "g", BR, a),
                                             linha_ok(c, [("conheço: ", TINTA2), ("hipotenusa = 10", HIP)], X + 76, 310, 56, a)))
    E.foco(c, t, C["s05.c"], 0.4, lambda a: (E.bola(c, X + 26, 390, 28, a=a), centro(c, "3", X + 26, 404, 36, "g", BR, a),
                                             linha_ok(c, [("quero: ", TINTA2), ("oposto = x", OPO)], X + 76, 410, 56, a)))

    def s06():
        E.foco(c, t, C["s06.b"], 0.5, lambda a: conta_r(c, "sen", "37°", "oposto", OPO, "hipotenusa", HIP, X, 620, 80, a))
        E.foco(c, t, C["s06.c"], 0.5, lambda a: E.pilula(c, "a prova dá o valor", X + 230, 790, 48, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s06.d"], 0.5, lambda a: E.formula(c, "sen 37° ≈ 0,6", X, 950, 84, "g", COR, a))
    E.saida(c, t, C["s07"] - 0.1, s06)

    def s07():
        E.foco(c, t, C["s07.a"], 0.5, lambda a: (E.formula(c, "0,6 = ", X, 620, 96, "g", TINTA, a), fra(c, "x", "10", X + _w("0,6 = ", 96), 620, 96, a, OPO, HIP)))
        E.foco(c, t, C["s07.b"], 0.5, lambda a: E.pilula(c, "× 10 dos dois lados", X + 700, 590, 44, "g", fundo=TINTA, a=a))
        linha(c, t, C["s07.c"], [("x", OPO), (" = 0,6 · 10 = 6", TINTA)], X, 820, 96)
        bola_txt(c, t, C["s07.d"], "6 m", 1730, 800, 95, 64, CERTO)
    if t >= C["s07"]:
        E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.foco(c, t, C["s08.a"], 0.5, lambda a: conta_r(c, "cos", "37°", "adjacente", ADJ, "hipotenusa", HIP, X, 580, 76, a))
    E.foco(c, t, C["s08.b"], 0.5, lambda a: E.formula(c, "cos 37° ≈ 0,8", X, 720, 70, "g", COR, a))
    linha(c, t, C["s08.c"], [("0,8 · 10 = ", TINTA), ("8 m", ADJ)], X, 850, 90)
    E.foco(c, t, C["s08.d"], 0.5, lambda a: E.pilula(c, "6, 8, 10 = o 3-4-5 dobrado", X + 400, 990, 50, "g", a=a))


def linha_ok(c, partes, x, y, size, a):
    xx = x
    for s, cor in partes:
        xx += E.formula(c, s, xx, y, size, "g", cor, a)


# ---------------- tangente: o telhado ----------------
KT = 55
TA, TR = (240, 760), (240 + 8 * KT, 760)
TT = (TR[0], TR[1] - 6 * KT)


def b_tangente(c, t, C, b):
    a0 = C["s09"]
    p = ep(t, a0, 0.6)
    if p > 0:  # a casa: paredes e o telhado de duas águas
        D = (TR[0] + 8 * KT, TR[1])
        M.rrect(c, TA[0] + 30, TA[1], D[0] - TA[0] - 60, 200, 4, CINZA, 0.25 * p)
        c.drawRect(skia.Rect.MakeLTRB(TA[0] + 30, TA[1], D[0] - 30, TA[1] + 200), M.paint(TINTA, p, stroke=4))
        M.line(c, TA[0] - 20, TA[1] + 200, D[0] + 20, TA[1] + 200, TINTA2, p, 5)
        M.line(c, *TA, *TT, TINTA, p, 8)
        M.line(c, *TT, *D, TINTA, p, 8)
    E.angulo(c, t, C["s09.a"], TA, TR, TT, "37°", r=120, size=50)
    if t >= C["s09.b"]:
        grosso(c, TA, TR, ADJ, 1.0, 12, ease_io(prog(t, C["s09.b"], 0.5)))
    E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: E._cola(c, "8 m", (TA[0] + TR[0]) / 2, TA[1] + 10, 0, 1, 16, 60, "g", ADJ, a))
    if t >= C["s09.c"]:
        grosso(c, TR, TT, OPO, 1.0, 12, ease_io(prog(t, C["s09.c"], 0.5)), dash=E.TRACO)
        E.angulo(c, t, C["s09.c"] + 0.3, TR, TA, TT, r=36)
    sobe = "6 m" if t >= C["s10.c"] else "x"
    E.foco(c, t, C["s09.c"] + 0.3, 0.4, lambda a: E._cola(c, sobe, TR[0] + 10, (TR[1] + TT[1]) / 2, 1, 0, 18, 64, "g", OPO, a))
    X = 1250
    E.frase(c, t, C["s09"], [("sem", "i", 72), ("hipotenusa?", "g", 68, COR)], XE, 160)
    E.foco(c, t, C["s09.d"], 0.5, lambda a: linha_ok(c, [("oposto", OPO), (" e ", TINTA2), ("adjacente", ADJ), (": tg", TINTA)], X - 80, 300, 60, a))
    E.foco(c, t, C["s10.a"], 0.5, lambda a: E.formula(c, "tg 37° ≈ 0,75", X, 450, 70, "g", COR, a))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: (E.formula(c, "0,75 = ", X, 640, 84, "g", TINTA, a), fra(c, "x", "8", X + _w("0,75 = ", 84), 640, 84, a, OPO, ADJ)))
    linha(c, t, C["s10.c"], [("x", OPO), (" = 0,75 · 8", TINTA)], X, 820, 80)
    bola_txt(c, t, C["s10.c"] + 1.2, "6 m", 1740, 940, 80, 56, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("escolher", "i", 72), ("pela", "i", 72), ("posição", "g", 68, ERRADO), ("no", "i", 72), ("desenho", "i", 72)], XE, 150)
    errado = t < C["s12.a"]
    cena_escada(c, t, dict(base=C["s11"] - 0.3, ang=C["s11"] + 0.4, hip=C["s11"] + 0.4, hip_txt=C["s11"] + 0.4,
                           opo=C["s11.d"] if errado else C["s12.c"], adj=C["s12.a"] if not errado else None),
                rot_opo="8 m?" if errado else "6 m", opo_cor=ERRADO if errado else OPO, rot_adj="8 m")
    X = 900
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.pilula(c, "ângulo embaixo → cos?", X + 300, 330, 50, "g", fundo=ERRADO, a=a))
    linha(c, t, C["s11.c"], [("0,8 · 10 = 8", TINTA)], X, 500, 84)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: (linha_ok(c, [("altura = 8 m", ERRADO)], X, 640, 84, a), E.selo(c, X + 620, 610, 40, False, a)))
    if not errado:
        E.foco(c, t, C["s12.a"], 0.5, lambda a: E.escreve(c, "8 é a distância no chão", X, 780, 56, "i", ADJ, a))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.pilula(c, "o lado de frente para o ângulo decide", X + 440, 880, 46, "g", a=a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: linha_ok(c, [("altura: ", TINTA), ("oposto", OPO), ("  →  sen", CERTO)], X, 1010, 64, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], [("o", "i", 72, CLARO), ("atalho", "g", 76, BR)], W / 2, 170, "center")
        E.foco(c, t, C["s13.a"], 0.5, lambda a: linha_ok(c, [("oposto", OPO), (" = hipotenusa · sen", BR)], 360, 400, 96, a))
        E.foco(c, t, C["s13.b"], 0.5, lambda a: linha_ok(c, [("adjacente", ADJ_ESC), (" = hipotenusa · cos", BR)], 360, 580, 96, a))
        E.foco(c, t, C["s13.c"], 0.5, lambda a: linha_ok(c, [("10 · 0,6 = ", BR), ("6", CLARO)], 360, 800, 110, a))
        E.foco(c, t, C["s13.c"] + 0.4, 0.4, lambda a: E.escreve(c, "sem montar equação", 1000, 800, 56, "i", CLARO, a))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"], ps("por que funciona", "i", 72, CLARO), W / 2, 170, "center")
    E.foco(c, t, C["s14.a"], 0.5, lambda a: (E.formula(c, "sen = ", 360, 400, 100, "g", BR, a), fra(c, "oposto", "hip", 360 + _w("sen = ", 100), 400, 100, a, OPO, BR, barra=BR)))
    E.foco(c, t, C["s14.a"] + 2.4, 0.5, lambda a: linha_ok(c, [("→  ", CLARO), ("oposto", OPO), (" = hip · sen", BR)], 1000, 400, 80, a))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.pilula(c, "não compensa: falta a hipotenusa", W / 2, 650, 52, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "aí ela fica embaixo: divida", W / 2, 840, 76, "g", CLARO, a, "center"))


# ---------------- questão: a pipa ----------------
KP = 30
PA, PR = (230, 900), (230 + 16 * KP, 900)
PT = (PR[0], PR[1] - 12 * KP)
PG = ((PA[0] + PR[0] + PT[0]) / 3, (PA[1] + PR[1] + PT[1]) / 3)


def pipa(c, X, a=1.0):
    if a <= 0:
        return
    x, y = X
    path = skia.Path()
    path.moveTo(x, y - 50); path.lineTo(x + 34, y); path.lineTo(x, y + 60); path.lineTo(x - 34, y); path.close()
    c.drawPath(path, M.paint(ERRADO, a))
    M.line(c, x, y - 50, x, y + 60, "#FFFFFF", a, 3); M.line(c, x - 34, y, x + 34, y, "#FFFFFF", a, 3)
    for k in range(3):
        M.line(c, x + 6 * k, y + 60 + 26 * k, x + 6 * (k + 1) + 10, y + 60 + 26 * (k + 1), TINTA2, a, 3)


def cena_pipa(c, t, k, hip_txt="?", alt_txt="12 m"):
    a0 = ep(t, k["base"], 0.6)
    chao(c, PA[0] - 90, PR[0] + 160, PA[1], 1.0, a0)
    E.foco(c, t, k["base"], 0.5, lambda a: pipa(c, PT, a))
    if t >= k["alt"]:
        grosso(c, PR, PT, OPO if k.get("opo") is not None and t >= k["opo"] else TINTA2, 1.0, 8, ease_io(prog(t, k["alt"], 0.5)), dash=E.TRACO)
        E.angulo(c, t, k["alt"] + 0.4, PR, PA, PT, r=34)
    E.foco(c, t, k["alt"] + 0.3, 0.4, lambda a: E._cola(c, alt_txt, PR[0] + 14, (PR[1] + PT[1]) / 2, 1, 0, 18, 64, "g",
                                                       OPO if k.get("opo") is not None and t >= k["opo"] else TINTA, a))
    if t >= k["linha"]:
        cor = HIP if k.get("hip") is not None and t >= k["hip"] else TINTA
        M.line(c, *PA, *PT, cor, 1.0, 6 if cor == TINTA else 10, progress=ease_io(prog(t, k["linha"], 0.6)))
        c.drawCircle(*PA, 10, M.paint(TINTA))
        E.angulo(c, t, k["linha"] + 0.4, PA, PR, PT, "37°", r=110, size=50)
        E.foco(c, t, k["linha"] + 0.6, 0.4, lambda a: rot(c, PA, PT, hip_txt, PG, 64, cor, a, 30))


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    def fig():
        cena_pipa(c, t, dict(base=C["s15.a"] - 0.4, alt=C["s15.a"], linha=C["s15.b"]))
    fig()
    X = 960
    E.frase(c, t, C["s15.a"], [("pipa", "i", 72), ("a", "i", 72), ("12 m", "g", 72, COR), ("de", "i", 72), ("altura", "i", 72)], X, 300)
    E.frase(c, t, C["s15.b"], [("linha", "i", 72), ("a", "i", 72), ("37°", "g", 72, COR), ("do", "i", 72), ("chão", "i", 72)], X, 410)
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.pilula(c, "sen 37° ≈ 0,6", X + 230, 510, 50, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s15.d"], [("comprimento", "i", 76), ("da", "i", 76), ("linha?", "g", 72, COR)], X, 650)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], 1450, 830, 75)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    hip = "20 m" if t >= C["s18.d"] else "x"
    cena_pipa(c, t, dict(base=C["s17"] - 0.6, alt=C["s17"] - 0.6, linha=C["s17"] - 0.6, hip=C["s17.a"], opo=C["s17.b"]), hip_txt=hip)
    X = 900

    def s17_18():
        E.foco(c, t, C["s17.a"], 0.4, lambda a: linha_ok(c, [("linha: ", TINTA2), ("hipotenusa", HIP)], X, 220, 56, a))
        E.foco(c, t, C["s17.b"], 0.4, lambda a: linha_ok(c, [("altura: ", TINTA2), ("oposto", OPO), ("  →  sen", COR)], X, 310, 56, a))
        E.foco(c, t, C["s17.d"], 0.5, lambda a: (E.formula(c, "0,6 = ", X, 480, 90, "g", TINTA, a), fra(c, "12", "x", X + _w("0,6 = ", 90), 480, 90, a, OPO, HIP)))
        linha(c, t, C["s18.a"], [("0,6", TINTA), ("x", HIP), (" = 12", TINTA)], X, 650, 80)
        linha(c, t, C["s18.b"], [("6", TINTA), ("x", HIP), (" = 120", TINTA)], X, 770, 80)
        E.foco(c, t, C["s18.b"] + 0.3, 0.4, lambda a: E.escreve(c, "× 10", X + 420, 770, 50, "i", TINTA2, a))
        linha(c, t, C["s18.c"], [("x", HIP), (" = 20", TINTA)], X, 890, 80)
        bola_txt(c, t, C["s18.d"], "20 m", 1600, 760, 110, 64, CERTO)
        E.foco(c, t, C["s18.e"], 0.5, lambda a: E.escreve(c, "hipotenusa > altura", 1400, 960, 52, "i", CERTO, a))
    E.saida(c, t, C["s19"] - 0.1, s17_18)
    if t < C["s19"]:
        return
    E.foco(c, t, C["s19.a"], 0.5, lambda a: (linha_ok(c, [("12 · 0,6 = ", TINTA), ("7,2", ERRADO)], X, 400, 90, a), E.selo(c, X + 640, 370, 44, False, a)))
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.escreve(c, "linha mais curta que a altura?", X, 560, 56, "i", ERRADO, a))
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "hipotenusa procurada: divida", X + 400, 760, 52, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        for i, (k, s) in enumerate((("s20.a", "ângulo, lado que tem, lado que quer"), ("s20.b", "os lados escolhem a razão"), ("s20.c", "monte a igualdade e resolva"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 76)], 430, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], ps("próxima aula", "i", 80), XE, 230)
    E.frase(c, t, C["s21"] + 0.6, [("ângulos", "g", 130, COR)], XE, 380)
    E.frase(c, t, C["s21"] + 1.0, [("notáveis", "g", 130, COR)], XE, 520)
    E.frase(c, t, C["s21.a"], [("30°", "g", 84), ("45°", "g", 84), ("60°", "g", 84)], XE, 670, passo=0.5)
    E.quadrado(c, t, C["s21.b"], 1080, 400, 250, None)
    E.regular(c, t, C["s21.b"] + 0.5, 3, 1600, 560, 160)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 560, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(900, 700, p), lerp(1000, 845, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], 1300, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, tangente=b_tangente, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
