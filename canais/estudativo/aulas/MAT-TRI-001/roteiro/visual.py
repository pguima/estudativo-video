"""Visual — Estudativo · MAT-TRI-001: seno, cosseno e tangente no triângulo retângulo. Primeira aula de Trigonometria.

LINGUAGEM VISUAL DA TRIGONOMETRIA (as próximas aulas de Trigonometria copiam daqui; segue a da geometria plana, MAT-ANG-001):
- Lados e figuras em tinta preta (TINTA); linha auxiliar tracejada em TINTA2. Ângulo reto = quadradinho (E.triangulo, retos=).
- O ângulo da vez é o arco com a cunha clara na cor da matéria (E.angulo), com o nome α (grotesca: a itálica não tem grego).
- Cada lado ganha uma COR FIXA quando recebe o nome, pintada por cima do traço preto (grosso()):
    OPO = âmbar  #D98A00  cateto oposto ao ângulo da vez
    ADJ = petróleo #0E9AA7  cateto adjacente (no palco escuro, ADJ_ESC #3CC7D3)
    HIP = índigo da matéria (E.COR)  hipotenusa
  As mesmas cores pintam os números e as palavras nas frações: sen α = oposto/hipotenusa com o "oposto" em âmbar e a
  "hipotenusa" em índigo. Lado que não entra na conta da vez fica fino, em tinta.
- sen, cos e tg sempre abreviados na tela. Medidas na grotesca. Resposta final na esfera; erro em vermelho, certo em verde;
  atalho no palco escuro.
- A figura não mente: os triângulos respeitam as medidas (3-4-5, 6-8-10, 5-12-13).
Peças locais: grosso(), rot() (rótulo de lado, por fora do triângulo), tri() (triângulo retângulo com os lados nomeados no tempo),
fra() (fração com palavras ou números coloridos) e razao() (sen α = …).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-001_seno_cosseno_e_tangente.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("nomes", "razoes", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
HIP, OPO, ADJ = E.COR, AMBAR, "#0E9AA7"      # cor fixa de cada lado da trigonometria
ADJ_ESC = "#3CC7D3"                         # o adjacente no palco escuro
assert 3 / 5 == 0.6 and 4 / 5 == 0.8 and 3 / 4 == 0.75 and 6 / 10 == 0.6 and 3 ** 2 + 4 ** 2 == 5 ** 2
assert 25 + 144 == 169 == 13 ** 2 and 12 / 5 == 2.4 and abs((3 / 5) / (4 / 5) - 0.75) < 1e-12


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


# ---------------- gancho ----------------
K1 = 70  # px por unidade
A1, R1, T1 = (200, 780), (200 + 4 * K1, 780), (200 + 4 * K1, 780 - 3 * K1)
A2, R2, T2 = (820, 860), (820 + 8 * K1, 860), (820 + 8 * K1, 860 - 6 * K1)


def semelhantes(c, t, ta, tb, tc, y_res=(430, 360)):
    tri(c, t, ta, A1, R1, T1, ("4", "3", "5"), tm={k: ta + 0.9 for k in ("adj", "opo", "hip")},
        cores={"opo": (tc, OPO), "hip": (tc, HIP)}, size=56)
    tri(c, t, tb, A2, R2, T2, ("8", "6", "10"), tm={k: tb + 0.9 for k in ("adj", "opo", "hip")},
        cores={"opo": (tc, OPO), "hip": (tc, HIP)}, size=60)
    E.foco(c, t, tc + 0.4, 0.5, lambda a: (fra(c, "3", "5", 260, y_res[0], 90, a, OPO, HIP), E.formula(c, " = 0,6", 340, y_res[0], 90, "g", TINTA, a)))
    E.foco(c, t, tc + 0.9, 0.5, lambda a: (fra(c, "6", "10", 900, y_res[1], 90, a, OPO, HIP), E.formula(c, " = 0,6", 1010, y_res[1], 90, "g", TINTA, a)))


def b_gancho(c, t, C, b):
    def s01():
        semelhantes(c, t, C["s01.a"], C["s01.b"], C["s01.c"])
        E.frase(c, t, C["s01.b"] + 0.6, [("o", "i", 64), ("dobro", "g", 60, COR)], 1480, 560)
        E.frase(c, t, C["s01.c"] + 2.4, [("não", "i", 68), ("é", "i", 68), ("coincidência", "g", 64, COR)], W / 2, 1020, "center")
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 80), XE, 220)
    itens = ((C["s02.a"] + 1.4, [("o ", "i"), ("nome", "g"), (" de cada lado", "i")]), (C["s02.b"], [("sen, cos", "g"), (" e ", "i"), ("tg", "g")]))
    for i, (t0, partes) in enumerate(itens):
        y = 420 + i * 180
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 48, a=a), centro(c, str(i + 1), XE + 40, y - 6, 56, "g", BR, a)))
        E.frase(c, t, t0 + 0.1, [(s.strip(), e, 96, COR if e == "g" else TINTA) for s, e in partes], XE + 130, y, passo=0.15)
    E.foco(c, t, C["s02.c"], 0.5, lambda a: E.pilula(c, "+ atalho de prova", 1420, 860, 60, "g", a=a))
    # o triângulo com os três lados nas cores fixas
    A, R, T = (1150, 640), (1150 + 4 * 90, 640), (1150 + 4 * 90, 640 - 3 * 90)
    tri(c, t, C["s02.a"] + 1.4, A, R, T, cores={"adj": (C["s02.a"] + 2.0, ADJ), "opo": (C["s02.a"] + 2.2, OPO), "hip": (C["s02.a"] + 2.4, HIP)},
        alfa=(C["s02.a"] + 2.6, "α", A, R, T), size=50, med=(None, None, None))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só precisa de", "i", 84), XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "Pitágoras", "catetos e hipotenusa"), ("s03.c", "semelhança", "mesmos ângulos, lados proporcionais"),
             ("s03.d", "fração em decimal", None))
    for i, (k, l1, l2) in enumerate(itens):
        y = 160 + i * 250
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 200, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 74)
        if l2:
            E.foco(c, t, C[k] + 0.3, 0.5, lambda a, l2=l2, y=y: E.escreve(c, l2, x + 44, y + 160, 54 if len(l2) > 22 else 64, "g", COR, a))
        else:
            E.foco(c, t, C[k] + 0.3, 0.5, lambda a, y=y: (fra(c, "3", "5", x + 44, y + 150, 80, a, COR, COR), E.formula(c, " = 0,6", x + 120, y + 150, 80, "g", COR, a)))
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(160 + 170, 410 + 170, q1), 660 + 170, q2), ep(t, C["s03.b"], 0.4))


# ---------------- os nomes ----------------
K = 150
NA, NR, NT = (200, 860), (200 + 4 * K, 860), (200 + 4 * K, 860 - 3 * K)


def b_nomes(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    G = tri(c, t, a4, NA, NR, NT, ("4", "3", "5"), tm={"opo": c5, "adj": d5, "hip": e5},
            cores={"hip": (c4, HIP), "opo": (a5, OPO), "adj": (b5, ADJ)},
            nomes={"hip": "hipotenusa", "opo": "oposto", "adj": "adjacente"}, tn={"hip": c4 + 0.3, "opo": a5 + 0.3, "adj": b5 + 0.3},
            alfa=(b4, "α", NA, NR, NT), size=72)
    # os dois agudos, antes de escolher
    if a4 + 1.0 <= t < b4 + 0.3:
        k = ep(t, a4 + 1.0, 0.4) * (1 - ep(t, b4 - 0.1, 0.4))
        for V, V1, V2 in ((NA, NR, NT), (NT, NA, NR)):
            a1 = math.degrees(math.atan2(V1[1] - V[1], V1[0] - V[0]))
            a2 = math.degrees(math.atan2(V2[1] - V[1], V2[0] - V[0]))
            ini, varre = a1, (a2 - a1 + 540) % 360 - 180
            E.arco(c, V[0], V[1], 80, ini, varre, COR, 7, k)
    E.foco(c, t, a4 + 1.0, 0.4, lambda a: E.escreve(c, "agudo: menor que 90°", 1100, 200, 56, "b", TINTA2, a * (1 - ep(t, b4, 0.4))))
    # quadro à direita
    x = 1220
    linhas = ((c4 + 0.3, "hipotenusa", HIP, "de frente para o reto", 330),
              (a5 + 0.3, "oposto", OPO, "de frente para α", 520),
              (b5 + 0.3, "adjacente", ADJ, "encosta em α (vizinho)", 710))
    for t0, s, cor, l2, y in linhas:
        E.foco(c, t, t0, 0.5, lambda a, s=s, cor=cor, y=y: E.escreve(c, s, x, y, 72, "g", cor, a))
        E.foco(c, t, t0 + 0.4, 0.5, lambda a, l2=l2, y=y: E.formula(c, l2, x, y + 70, 50, "b", TINTA2, a))


# ---------------- as três razões ----------------
KR = 100
RA, RR, RT = (180, 820), (180 + 4 * KR, 820), (180 + 4 * KR, 820 - 3 * KR)
RX, RS = 800, 76


def linha_razao(c, t, t0, t1, nome, cima, cc, baixo, cb, n, d, val, y):
    E.foco(c, t, t0, 0.5, lambda a: razao(c, nome, cima, cc, baixo, cb, RX, y, RS, a))
    xe = razao(None, nome, cima, cc, baixo, cb, RX, y, RS, 0)
    def num(a):
        w = E.formula(c, " = ", xe, y, RS, "g", TINTA, a)
        w += fra(c, n, d, xe + w, y, RS, a, cc, cb)
        E.formula(c, f" = {val}", xe + w, y, RS, "g", COR, a)
    E.foco(c, t, t1, 0.5, num)


def b_razoes(c, t, C, b):
    if t < C["s09.b"]:
        if t < C["s07.a"]:
            aceso = {"opo", "hip"}
        elif t < C["s08.a"]:
            aceso = {"adj", "hip"}
        elif t < C["s09"]:
            aceso = {"opo", "adj"}
        else:
            aceso = None
        def fig():
            tri(c, t, C["s06"], RA, RR, RT, ("4", "3", "5"), tm={k: C["s06"] + 0.5 for k in ("adj", "opo", "hip")},
                cores={"hip": (C["s06"], HIP), "opo": (C["s06"], OPO), "adj": (C["s06"], ADJ)}, alfa=(C["s06"] + 0.3, "α", RA, RR, RT),
                aceso=aceso, size=60)
            linha_razao(c, t, C["s06.a"], C["s06.b"], "sen", "oposto", OPO, "hipotenusa", HIP, "3", "5", "0,6", 270)
            linha_razao(c, t, C["s07.a"], C["s07.b"], "cos", "adjacente", ADJ, "hipotenusa", HIP, "4", "5", "0,8", 560)
            linha_razao(c, t, C["s08.a"], C["s08.b"], "tg", "oposto", OPO, "adjacente", ADJ, "3", "4", "0,75", 850)
            E.foco(c, t, C["s06.c"], 0.5, lambda a: (E.pilula(c, "seno → sen", 360, 200, 44, "b", fundo=TINTA, a=a),
                                                     E.pilula(c, "cosseno → cos", 360, 290, 44, "b", fundo=TINTA, a=a),
                                                     E.pilula(c, "tangente → tg", 360, 380, 44, "b", fundo=TINTA, a=a)))
        E.saida(c, t, C["s09.b"] - 0.1, fig)
        E.frase(c, t, C["s09.a"], [("o", "i", 64), ("mesmo", "i", 64), ("0,6?", "g", 64, COR)], RX, 1010)
    if t < C["s09.b"] - 0.1:
        return
    semelhantes(c, t, C["s09.b"] - 0.1, C["s09.b"] + 0.3, C["s09.c"])
    E.frase(c, t, C["s09.b"] + 0.6, [("semelhantes", "g", 64, COR)], 1660, 560, "center")
    E.frase(c, t, C["s09.b"] + 1.2, [("mesmos", "i", 64), ("ângulos", "i", 64)], 1660, 650, "center")
    E.foco(c, t, C["s09.d"], 0.5, lambda a: E.pilula(c, "depende só do ângulo", W / 2, 1010, 56, "g", a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10.a"], [("decore", "i", 72), ("a", "i", 72), ("posição,", "g", 68, CERTO), ("não", "i", 72), ("o", "i", 72), ("lado", "g", 68, ERRADO)], XE, 160)
    certo = t >= C["s11.a"]
    cores = {"hip": (C["s10"], HIP)}
    if C["s10.c"] <= t < C["s11.a"]:
        cores["opo"] = (C["s10.c"], OPO)            # o "oposto" decorado, ainda no 3
    if certo:
        cores["adj_"] = None
        cores["adj"] = (C["s11.a"], OPO)            # o 4 vira o oposto
    if t >= C["s11.b"]:
        cores["opo"] = (C["s11.b"], ADJ)            # o 3 vira o adjacente
    cores.pop("adj_", None)
    tri(c, t, C["s10"], NA, NR, NT, ("4", "3", "5"), tm={k: C["s10"] + 0.5 for k in ("adj", "opo", "hip")}, cores=cores, size=72)
    # o ângulo agora é o de cima, de frente para o 4
    E.angulo(c, t, C["s10.b"], NT, NA, NR, "β", r=95, size=54)
    if C["s10.c"] <= t < C["s11.a"]:
        E.foco(c, t, C["s10.c"], 0.4, lambda a: rot(c, NR, NT, "oposto?", (700, 700), 50, OPO, a, 90, "i"))
    if certo:
        E.foco(c, t, C["s11.a"], 0.4, lambda a: rot(c, NA, NR, "oposto", (700, 700), 56, OPO, a, 90, "i"))
    if t >= C["s11.b"]:
        E.foco(c, t, C["s11.b"], 0.4, lambda a: rot(c, NR, NT, "adjacente", (700, 700), 56, ADJ, a, 90, "i"))
    x, y = 1000, 330

    def conta(a, n, val, cor_v, ok):
        w = E.formula(c, "sen β = ", x, y, 80, "g", TINTA, a)
        w += fra(c, n, "5", x + w, y, 80, a, OPO, HIP)
        w += E.formula(c, f" = {val}", x + w, y, 80, "g", cor_v, a)
        E.selo(c, x + w + 60, y - 28, 38, ok, a)
        return w

    def errado():
        E.foco(c, t, C["s10.c"], 0.5, lambda a: conta(a, "3", "0,6", ERRADO, False))
        if t >= C["s10.c"] + 1.0:
            E.risco(c, x - 10, y + 60, x + 560, y - 90, t, C["s10.c"] + 1.0, ERRADO, 10)
    E.saida(c, t, C["s11.c"] - 0.1, errado)
    E.foco(c, t, C["s11.c"], 0.5, lambda a: conta(a, "4", "0,8", CERTO, True))
    x2 = 1250
    E.frase(c, t, C["s11.d"], [("oposto", "g", 60, OPO), ("e", "i", 64), ("adjacente", "g", 60, ADJ)], x2, 620)
    E.frase(c, t, C["s11.d"] + 1.0, ps("mudam com o ângulo", "i", 64), x2, 710)
    E.frase(c, t, C["s11.e"], [("hipotenusa:", "g", 60, HIP)], x2, 860)
    E.frase(c, t, C["s11.e"] + 0.6, ps("sempre no mesmo lugar", "i", 64), x2, 950)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], [("o", "i", 72, CLARO), ("atalho", "g", 76, BR)], W / 2, 170, "center")
        E.foco(c, t, C["s12.a"], 0.5, lambda a: (E.formula(c, "tg α = ", 620, 380, 110, "g", BR, a), fra(c, "sen α", "cos α", 990, 380, 110, a, BR, BR, barra=BR)))
        x0, y, s = 360, 700, 110
        E.foco(c, t, C["s12.b"], 0.5, lambda a: (E.formula(c, "f{3}{5} ÷ f{4}{5}", x0, y, s, "g", BR, a)))
        d1 = x0 + _w("f{3}{5}", s) / 2
        d2 = x0 + _w("f{3}{5} ÷ ", s) + _w("f{4}{5}", s) / 2
        if t >= C["s12.c"] - 0.6:
            for xx in (d1, d2):
                E.risco(c, xx - 36, y + 78, xx + 36, y + 6, t, C["s12.c"] - 0.6, ERRADO, 8)
        E.foco(c, t, C["s12.c"] - 0.4, 0.4, lambda a: E.escreve(c, "quintos com quintos", x0, y + 170, 50, "i", CLARO, a))
        x1 = x0 + _w("f{3}{5} ÷ f{4}{5}", s)
        E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, " = 3 ÷ 4", x1, y, s, "g", BR, a))
        x2 = x1 + _w(" = 3 ÷ 4", s)
        E.foco(c, t, C["s12.d"], 0.5, lambda a: E.formula(c, " = 0,75", x2, y, s, "g", CLARO, a))
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return

    def s13():
        E.frase(c, t, C["s13"], ps("por que funciona", "i", 72, CLARO), W / 2, 170, "center")
        y, s = 470, 120
        E.foco(c, t, C["s13.a"], 0.5, lambda a: (E.formula(c, "f{sen α}{cos α} = ", 360, y, s, "g", BR, a)))
        x0 = 360 + E.formula(None, "f{sen α}{cos α} = ", 0, 0, s, a=0)

        def grande(a):
            # oposto/hip sobre adjacente/hip
            wa = fra(None, "oposto", "hip", 0, 0, s * 0.7, 0)
            wb = fra(None, "adjacente", "hip", 0, 0, s * 0.7, 0)
            w = max(wa, wb) + 30
            fra(c, "oposto", "hip", x0 + (w - wa) / 2, y - s * 0.62, s * 0.7, a, OPO, CLARO, barra=BR)
            fra(c, "adjacente", "hip", x0 + (w - wb) / 2, y + s * 0.78, s * 0.7, a, ADJ_ESC, CLARO, barra=BR)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y - s * 0.3 - 5, w, 10), 5, 5), M.paint(BR, a))
            return w
        E.foco(c, t, C["s13.a"] + 0.6, 0.5, grande)
        w = grande(0) if False else max(fra(None, "oposto", "hip", 0, 0, s * 0.7, 0), fra(None, "adjacente", "hip", 0, 0, s * 0.7, 0)) + 30
        for i, yy in enumerate((y - s * 0.62 + s * 0.7 * 0.46, y + s * 0.78 + s * 0.7 * 0.46)):
            if t >= C["s13.b"] + 0.3 * i:
                xm = x0 + w / 2
                E.risco(c, xm - 70, yy + 10, xm + 70, yy - 50, t, C["s13.b"] + 0.3 * i, ERRADO, 8)
        E.foco(c, t, C["s13.c"], 0.5, lambda a: (E.formula(c, " = ", x0 + w + 10, y, s, "g", BR, a),
                                                 fra(c, "oposto", "adjacente", x0 + w + 110, y, s * 0.9, a, OPO, ADJ_ESC, barra=BR)))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: E.pilula(c, "tem os lados? divida direto", W / 2, 900, 52, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"], ps("conferência rápida", "i", 72, CLARO), W / 2, 170, "center")
    E.foco(c, t, C["s14.a"], 0.5, lambda a: E.formula(c, "sen e cos  <  1", W / 2, 400, 120, "g", BR, a, "center"))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (fra(c, "cateto", "hipotenusa", 640, 640, 100, a, CLARO, BR, barra=BR),
                                             E.escreve(c, "a de baixo é a maior", 1120, 640, 56, "i", CLARO, a)))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.pilula(c, "deu mais que 1? refaça os nomes", W / 2, 900, 54, "g", fundo=ERRADO, a=a))


# ---------------- questão ----------------
KQ = 50
QA, QR, QT = (360, 920), (360 + 5 * KQ, 920), (360 + 5 * KQ, 920 - 12 * KQ)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    tri(c, t, C["s15.a"] - 0.6, QA, QR, QT, ("5", "12", "?"), tm={"adj": C["s15.a"], "opo": C["s15.a"] + 0.4, "hip": C["s15.b"] + 0.6},
        alfa=(C["s15.b"], "α", QA, QR, QT), size=70)
    E.frase(c, t, C["s15.a"], [("catetos", "i", 76), ("5", "g", 76, COR), ("e", "i", 76), ("12", "g", 76, COR)], 900, 340)
    E.frase(c, t, C["s15.b"], [("ângulo", "i", 76), ("de", "i", 76), ("frente", "i", 76), ("para", "i", 76), ("o", "i", 76), ("12", "g", 76, COR)], 900, 470)
    E.frase(c, t, C["s15.c"], [("sen,", "g", 84, COR), ("cos", "g", 84, COR), ("e", "i", 88), ("tg?", "g", 84, COR)], 900, 620)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], 1500, 830, 95)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    hip = "13" if t >= C["s17.b"] else "?"
    tri(c, t, C["s17"] - 0.6, QA, QR, QT, ("5", "12", hip), tm={k: C["s17"] - 0.6 for k in ("adj", "opo", "hip")},
        cores={"hip": (C["s17.b"], HIP), "opo": (C["s17.c"], OPO), "adj": (C["s17.d"], ADJ)},
        nomes={"opo": "oposto", "adj": "adjacente"}, tn={"opo": C["s17.c"] + 0.3, "adj": C["s17.d"] + 0.3},
        alfa=(C["s17"] - 0.6, "α", QA, QR, QT), size=70)
    x = 900

    def s17():
        E.foco(c, t, C["s17.a"], 0.5, lambda a: E.formula(c, "25 + 144 = 169", x, 360, 84, "g", TINTA, a))
        E.foco(c, t, C["s17.b"], 0.5, lambda a: (E.formula(c, "r{169} = ", x, 520, 84, "g", TINTA, a),
                                                 E.formula(c, "13", x + E.formula(None, "r{169} = ", 0, 0, 84, a=0), 520, 84, "g", HIP, a)))
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    linhas = ((C["s18.a"], "sen", "12", OPO, "13", HIP, None, 300), (C["s18.b"], "cos", "5", ADJ, "13", HIP, None, 520),
              (C["s18.c"], "tg", "12", OPO, "5", ADJ, "2,4", 740))
    for t0, nome, n, cn, d, cd, val, y in linhas:
        def f(a, nome=nome, n=n, cn=cn, d=d, cd=cd, val=val, y=y):
            w = E.formula(c, f"{nome} α = ", x, y, 84, "g", TINTA, a)
            w += fra(c, n, d, x + w, y, 84, a, cn, cd)
            if val:
                E.formula(c, f" = {val}", x + w, y, 84, "g", COR, a)
        E.foco(c, t, t0, 0.5, f)
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.pilula(c, "tg pode passar de 1", 1360, 920, 52, "g", a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for k, nome, cima, cc, baixo, cb, y in (("s19.a", "sen", "oposto", OPO, "hipotenusa", HIP, 400),
                                                ("s19.b", "cos", "adjacente", ADJ, "hipotenusa", HIP, 650),
                                                ("s19.c", "tg", "oposto", OPO, "adjacente", ADJ, 900)):
            E.foco(c, t, C[k], 0.5, lambda a, nome=nome, cima=cima, cc=cc, baixo=baixo, cb=cb, y=y: razao(c, nome, cima, cc, baixo, cb, 560, y, 100, a))
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], ps("próxima aula", "i", 80), XE, 230)
    E.frase(c, t, C["s20"] + 0.6, [("o", "i", 120), ("caminho", "g", 130, COR)], XE, 390)
    E.frase(c, t, C["s20"] + 1.0, [("de", "i", 120), ("volta", "g", 130, COR)], XE, 530)
    E.frase(c, t, C["s20.a"], [("ângulo", "g", 56), ("+", "g", 56), ("um", "i", 60), ("lado", "i", 60)], XE, 660)
    E.frase(c, t, C["s20.b"], [("→", "g", 56, COR), ("o", "i", 60), ("lado", "i", 60), ("que", "i", 60), ("falta", "g", 56, COR)], XE + 470, 660)
    A, R, T = (1150, 640), (1150 + 8 * 55, 640), (1150 + 8 * 55, 640 - 6 * 55)
    tri(c, t, C["s20.c"], A, R, T, ("", "x", "10"), tm={"opo": C["s20.c"] + 0.4, "hip": C["s20.c"] + 0.4},
        cores={"opo": (C["s20.c"] + 0.4, OPO), "hip": (C["s20.c"] + 0.4, HIP)}, alfa=(C["s20.c"] + 0.4, "37°", A, R, T), size=56)
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 560, 800, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.d"] + 0.3, 0.8))
    E.cursor(c, lerp(900, 700, p), lerp(1000, 825, p), ep(t, C["s20.d"] + 0.2, 0.4))
    E.frase(c, t, C["s20.e"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], 1300, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nomes=b_nomes, razoes=b_razoes, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
