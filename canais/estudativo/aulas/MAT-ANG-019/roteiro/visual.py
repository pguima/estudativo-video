"""Visual — Estudativo · MAT-ANG-019: praticando Pitágoras e relações métricas (cinco situações). Fecha a trilha.
Aula de prática no molde da MAT-ANG-009: selo de progresso "situação n de 5", figura à esquerda, pergunta embaixo à direita e
relógio de pausa; na resposta, a mesma figura ganha as medidas e a conta aparece na coluna da direita.
Linguagem da geometria plana (MAT-ANG-001 a 020; Pitágoras nas MAT-ANG-015 a 018): lados em tinta; a hipotenusa da vez em COR
(índigo), o cateto conhecido em TINTA2 e o procurado em AMBAR; ângulo reto = quadradinho; lados iguais com tracinhos;
medidas e raízes na fonte pesada (√2 ≈ 1,4 e √3 ≈ 1,7); erro em vermelho, certo em verde; resposta na esfera; atalho no palco.
As figuras respeitam as medidas (20 x 21, 9 e 12, mesa de 80 com régua de 120, equilátero de 30, pedaços 9 e 16): a figura
não mente (a régua passa mesmo da diagonal, por pouco).
Peças locais: marca() (progresso), pergunta() (linhas da pergunta + relógio), txt_lado(), grosso(), terno(), geo()/fig()/pedacos()
(as da MAT-ANG-018), terreno(), antena(), mesa(), placa().
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-019_praticando_pitagoras_e_relacoes_metricas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
MADEIRA = "#C9A46A"
assert 20 ** 2 == 400 and 21 ** 2 == 441 and 400 + 441 == 841 == 29 ** 2 and 30 ** 2 == 900 and 20 + 21 == 41
assert 9 ** 2 + 12 ** 2 == 225 == 15 ** 2 and 81 + 144 == 225 and (9 // 3, 12 // 3) == (3, 4) and 5 * 3 == 15
assert round(80 * 1.4) == 112 and 80 * math.sqrt(2) < 120 and 6400 + 6400 == 12800 and 120 ** 2 == 14400 > 12800
assert abs(15 * 1.7 - 25.5) < 1e-9 and round(15 * math.sqrt(3)) == 26 and 30 * math.sqrt(3) > 50 > 30
assert 9 * 16 == 144 == 12 ** 2 and 9 ** 2 + 12 ** 2 == 15 ** 2 and 12 ** 2 + 16 ** 2 == 20 ** 2 and 9 + 16 == 25
assert 25 * 12 == 300 == 15 * 20 and 15 ** 2 + 20 ** 2 == 25 ** 2


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)


def selo(c, t, t0, cx, cy, r=50, ok=True):
    E.foco(c, t, t0, 0.4, lambda a: E.selo(c, cx, cy, r * ease_back(prog(t, t0, 0.4)), ok, a))


def meio(P, Q):
    return (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2


def txt_lado(c, P, Q, s, G, size=54, cor=None, a=1.0, gap=20, dentro=False):
    if a <= 0 or not s:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = meio(P, Q)
    fora = (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 > (mx - G[0]) ** 2 + (my - G[1]) ** 2
    if fora == dentro:
        nx, ny = -nx, -ny
    E._cola(c, s, mx, my, nx, ny, gap, size, "b", cor or COR, a)


def grosso(c, P, Q, cor, a, larg=12, p=1.0):
    if a > 0 and p > 0:
        M.line(c, *P, *Q, cor, a, larg, progress=p)


def terno(c, t, t0, nums, cx, y, size=96, cor_n=TINTA, cor_h=None, passo=0.2):
    partes = [(f"{n}," if i < 2 else f"{n}", "g", size, cor_n if i < 2 else (cor_h or COR)) for i, n in enumerate(nums)]
    E.frase(c, t, t0, partes, cx, y, "center", passo)


def marca(c, t, t0, n):
    """situação n de 5, com cinco pontos de progresso (como na MAT-ANG-009)"""
    s = f"situação {n} de 5"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", a=a)
        for i in range(5):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def pergunta(c, t, linhas, rel, X=1500, y0=800):
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, y0 + i * 95, "center", 0.12)
    E.relogio(c, t, rel, X, 400, 170)


# ---------------- figuras ----------------
# Q1: terreno 20 x 21, visto de cima (22 px por metro)
T1 = (330, 250, 20 * 22, 21 * 22)
TA, TB, TC, TD = (T1[0], T1[1] + T1[3]), (T1[0] + T1[2], T1[1] + T1[3]), (T1[0] + T1[2], T1[1]), (T1[0], T1[1])


def terreno(c, t, t0, tcerca, tl, cerca=lambda tt: "?", cerca_cor=lambda tt: COR):
    if t < t0:
        return
    q = ease_io(prog(t, t0, 0.6))
    x, y, w, h = T1
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint("#DDEFD5", 0.9 * q))
    E._contorno(c, [TA, TB, TC, TD], q, TINTA, 6)
    for V, P, Q in ((TA, TB, TD), (TB, TC, TA), (TC, TD, TB), (TD, TA, TC)):
        E.angulo(c, t, t0 + 0.5, V, P, Q, r=36)
    E.foco(c, t, tl, 0.4, lambda a: (centro(c, "20 m", x + w / 2, y + h + 76, 60, "b", TINTA, a),
                                     E.formula(c, "21 m", x - 36, y + h / 2 + 22, 60, "b", TINTA, a, "right")))
    if t >= tcerca:
        p = ease_io(prog(t, tcerca, 0.8))
        M.line(c, *TA, lerp(TA[0], TC[0], p), lerp(TA[1], TC[1], p), "#7A4E1E", 1.0, 9)
        for k in range(1, 8):
            f = k / 8
            if f <= p:
                P = (lerp(TA[0], TC[0], f), lerp(TA[1], TC[1], f))
                c.drawCircle(*P, 8, M.paint("#7A4E1E"))
    E.foco(c, t, tcerca + 0.6, 0.4, lambda a: E.pilula(c, cerca(t), (TA[0] + TC[0] + TD[0]) / 3, (TA[1] + TC[1] + TD[1]) / 3, 52, "g", fundo=cerca_cor(t), a=a))


# Q2: antena de 12 m, cabo até 9 m do pé (50 px por metro)
AP, AT, AC = (800, 900), (800, 900 - 12 * 50), (800 - 9 * 50, 900)
AG = ((AP[0] + AT[0] + AC[0]) / 3, (AP[1] + AT[1] + AC[1]) / 3)


def antena(c, t, t0, tr, th, tc, tm, cabo=lambda tt: "?", cabo_cor=lambda tt: COR):
    if t < t0:
        return
    q = ease_io(prog(t, t0, 0.6))
    M.line(c, 140, 900, lerp(140, 1040, q), 900, TINTA, 1.0, 6)
    for i in range(14):
        M.line(c, 160 + i * 64, 910, 138 + i * 64, 940, TINTA2, q * 0.6, 3)
    alt = ease_io(prog(t, t0 + 0.3, 0.7))
    if alt > 0:  # mastro em treliça
        ytop = lerp(AP[1], AT[1], alt)
        for dx in (-12, 12):
            M.line(c, AP[0] + dx, AP[1], AP[0] + dx * 0.4, ytop, TINTA, 1.0, 5)
        n = int((AP[1] - ytop) // 40)
        for k in range(n):
            y0 = AP[1] - k * 40
            M.line(c, AP[0] - 11, y0, AP[0] + 11, y0 - 40, TINTA2, 1.0, 3)
        if alt >= 1:
            c.drawCircle(AT[0], AT[1] - 8, 12, M.paint(ERRADO))
    E.angulo(c, t, tr, AP, AC, (AP[0], AP[1] - 100), r=60)
    E.foco(c, t, th, 0.4, lambda a: E.escreve(c, "12 m", AP[0] + 40, (AP[1] + AT[1]) / 2 + 24, 64, "b", TINTA, a))
    E.foco(c, t, tm, 0.4, lambda a: (M.line(c, AC[0], 970, AP[0], 970, TINTA2, a, 3),
                                     centro(c, "9 m", (AC[0] + AP[0]) / 2, 1040, 60, "b", TINTA, a)))
    if t >= tc:
        M.line(c, *AT, *AC, TINTA, 1.0, 5, progress=ease_io(prog(t, tc, 0.6)))
    E.foco(c, t, tc + 0.5, 0.4, lambda a: txt_lado(c, AT, AC, cabo(t), AG, 64, cabo_cor(t), a))


# Q3: mesa quadrada de 80 cm e régua de 120 cm (5 px por cm)
MX, MY, ML = 300, 330, 400
MA, MC = (MX, MY + ML), (MX + ML, MY)          # cantos da diagonal
RL = 120 * 5


def mesa(c, t, t0, td, tr, a_err=0.0):
    if t < t0:
        return
    q = ease_io(prog(t, t0, 0.6))
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.18 * q))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawRect(skia.Rect.MakeXYWH(MX + 10, MY + 16, ML, ML), s)
    c.drawRect(skia.Rect.MakeXYWH(MX, MY, ML, ML), M.paint("#E9D8B8", q))
    E._contorno(c, [(MX, MY), (MX + ML, MY), (MX + ML, MY + ML), (MX, MY + ML)], q, TINTA, 6)
    for P, Q in (((MX, MY + ML), (MX + ML, MY + ML)), ((MX + ML, MY + ML), (MX + ML, MY)), ((MX + ML, MY), (MX, MY)), ((MX, MY), (MX, MY + ML))):
        E.marcas_iguais(c, P, Q, 1, TINTA, ep(t, t0 + 0.6, 0.4))
    E.foco(c, t, t0 + 0.6, 0.4, lambda a: centro(c, "80 cm", MX + ML / 2, MY + ML + 80, 58, "b", TINTA, a))
    if t >= td:
        M.line(c, *MA, *MC, COR, 1.0, 5, dash=E.TRACO, progress=ease_io(prog(t, td, 0.6)))
    if t >= tr:  # a régua, centrada na diagonal, um pouco mais comprida
        k = ease_io(prog(t, tr, 0.7))
        ux, uy = E._uni(*MA, *MC)
        cx, cy = meio(MA, MC)
        L = RL * k
        nx, ny = uy * 12, -ux * 12
        P0 = (cx - ux * L / 2 + nx * 2.2, cy - uy * L / 2 + ny * 2.2)
        P1 = (cx + ux * L / 2 + nx * 2.2, cy + uy * L / 2 + ny * 2.2)
        path = skia.Path()
        path.addPoly([(P0[0] - nx, P0[1] - ny), (P1[0] - nx, P1[1] - ny), (P1[0] + nx, P1[1] + ny), (P0[0] + nx, P0[1] + ny)], True)
        c.drawPath(path, M.paint("#F2D04B", 0.95))
        c.drawPath(path, M.paint(TINTA, 1.0, stroke=3))
        for i in range(1, 12):
            f = i / 12
            Q = (lerp(P0[0], P1[0], f), lerp(P0[1], P1[1], f))
            M.line(c, Q[0] - nx, Q[1] - ny, Q[0] - nx * 0.2, Q[1] - ny * 0.2, TINTA, 1.0, 2)
        if a_err > 0:  # as pontas que sobram
            for P, sgn in ((P0, 1), (P1, -1)):
                c.drawCircle(*P, 26, M.paint(ERRADO, a_err, stroke=6))


# Q4: placa equilátera de 30 cm (16 px por cm)
QB1, QB2 = (260, 900), (260 + 30 * 16, 900)
QT = ((QB1[0] + QB2[0]) / 2, QB1[1] - 30 * 16 * math.sqrt(3) / 2)
QM = ((QB1[0] + QB2[0]) / 2, QB1[1])


def placa(c, t, t0, tl, th, h_txt=lambda tt: "h = ?", h_cor=lambda tt: AMBAR, partida=None):
    E.triangulo(c, t, t0, QB1, QB2, QT, vertices=None, iguais=(1, 1, 1), preenche=0.12)
    E.foco(c, t, tl, 0.4, lambda a: txt_lado(c, QT, QB1, "30 cm", ((QB1[0] + QB2[0] + QT[0]) / 3, (QB1[1] + QB2[1] + QT[1]) / 3), 58, TINTA, a))
    if t >= th:
        M.line(c, *QT, *QM, AMBAR, 1.0, 7, dash=E.TRACO, progress=ease_io(prog(t, th, 0.6)))
        E.angulo(c, t, th + 0.4, QM, QB2, QT, r=30)
    E.foco(c, t, th + 0.4, 0.4, lambda a: E.formula(c, h_txt(t), QM[0] + 20, 770, 56, "g", h_cor(t), a, "left"))
    if partida is not None:
        E.foco(c, t, partida, 0.4, lambda a: (E.marcas_iguais(c, QB1, QM, 2, TINTA, a), E.marcas_iguais(c, QM, QB2, 2, TINTA, a),
                                              centro(c, "15", (QB1[0] + QM[0]) / 2, 970, 54, "b", TINTA2, a),
                                              centro(c, "15", (QM[0] + QB2[0]) / 2, 970, 54, "b", TINTA2, a)))


# Q5: pedaços 9 e 16 (28 px por unidade)
def geo(B, u, m, n, h):
    Cc = (B[0] + (m + n) * u, B[1])
    Hh = (B[0] + m * u, B[1])
    A = (Hh[0], B[1] - h * u)
    return dict(B=B, C=Cc, H=Hh, A=A, G=((B[0] + Cc[0] + A[0]) / 3, (B[1] + Cc[1] + A[1]) / 3))


G5 = geo((140, 760), 30, 9, 16, 12)
assert abs(math.dist(G5["B"], G5["A"]) / 30 - 15) < 1e-6 and abs(math.dist(G5["A"], G5["C"]) / 30 - 20) < 1e-6


def fig5(c, t, t0, th, tp, rot=None, tl=None, size=54):
    g = G5
    B, Cc, Hh, A = g["B"], g["C"], g["H"], g["A"]
    E.triangulo(c, t, t0, B, Cc, A, vertices=None, retos=(2,), preenche=0.05)
    if t >= th:
        M.line(c, *A, *Hh, TINTA, 1.0, 5, progress=ease_io(prog(t, th, 0.6)))
        E.angulo(c, t, th + 0.5, Hh, Cc, A, r=34)
    k = ep(t, tp, 0.5)
    if k > 0:
        y = B[1] + 26
        for P, Q, s in ((B, Hh, "9"), (Hh, Cc, "16")):
            M.line(c, P[0] + 6, y, Q[0] - 6, y, TINTA2, k, 5)
            for X in (P[0] + 6, Q[0] - 6):
                M.line(c, X, y - 10, X, y + 10, TINTA2, k, 4)
            E.formula(c, s, (P[0] + Q[0]) / 2, y + 66, size, "b", TINTA2, k, "center")
    lados = dict(a=(B, Cc), b=(A, Cc), c=(B, A))
    for kk, (s, cor) in (rot or {}).items():
        ti = (tl or {}).get(kk, t0)
        if kk == "h":
            E.foco(c, t, ti, 0.4, lambda a, s=s, cor=cor: E.formula(c, s, Hh[0] + 16, (A[1] + Hh[1]) / 2 + 20, size, "b", cor, a, "left"))
        else:
            P, Q = lados[kk]
            E.foco(c, t, ti, 0.4, lambda a, P=P, Q=Q, s=s, cor=cor: txt_lado(c, P, Q, s, g["G"], size, cor, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]
    E.frase(c, t, a_ + 0.1, ps("5", "g", 240, COR) + ps("situações", "g", 170, COR), XE, 350, passo=0.25)
    E.frase(c, t, a_ + 1.0, ps("criadas para esta aula", "i", 70, TINTA2), XE, 470, passo=0.12)
    E.frase(c, t, b_, ps("primeiro:", "i", 70) + [("escolha a ferramenta", "g", 76, COR)], XE, 610, passo=0.12)
    for i, (s, cx, ti) in enumerate((("pause", 440, c_), ("resolva", 960, c_ + 0.9), ("confira", 1480, c_ + 2.0))):
        E.foco(c, t, ti, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 830, 56, 64, p),
                                                           E.escreve(c, s, cx - 110, 855, 92, "g", TINTA, p)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.1, ps("as ferramentas", "i", 84, COR), XE, 200, passo=0.12)
    itens = (("a", "Pitágoras:", "some para a hipotenusa, subtraia para o cateto"),
             ("b", "ternos:", "3, 4, 5  e  5, 12, 13"),
             ("c", "quadrado e equilátero:", "d = ℓ√2   e   h = ℓ√3 ÷ 2"),
             ("d", "relações métricas:", "a · h = b · c   e   h² = m · n"))
    for i, (k, tit, sub) in enumerate(itens):
        y = 360 + i * 160
        ti = C[f"s02.{k}"]
        E.foco(c, t, ti, 0.5, lambda p, i=i, y=y: num_bola(c, str(i + 1), XE + 46, y - 26, 44, 52, p))
        E.frase(c, t, ti + 0.1, [(tit, "g", 64)], XE + 120, y)
        E.foco(c, t, ti + 0.7, 0.4, lambda a, tit=tit, sub=sub, y=y: E.escreve(c, sub, XE + 140 + E.larg(tit, "g", 64), y, 56,
                                                                               "i" if k == "a" else "b", COR, a))
    E.frase(c, t, C["s02.end"] - 2.6, ps("travou? procure a aula no canal", "i", 60), XE, 1010, passo=0.1)


# ---------------- situação 1 ----------------
def b_questao1(c, t, C, b):
    a3, b3, c3, d3 = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.d"]
    marca(c, t, a3, 1)
    terreno(c, t, b3 - 0.3, c3, b3)
    E.saida(c, t, C["s04.a"] - 0.1, lambda: E.frase(c, t, b3, ps("terreno", "i", 64) + [("retangular", "g", 70)], 1500, 380, "center", 0.12))
    pergunta(c, t, [(b3, [("20 m × 21 m", "g", 66)]),
                    (c3, ps("cerca de canto a canto", "i", 58)),
                    (d3, ps("a cerca mede", "i", 60) + [("?", "g", 72, COR)])], C["s04.a"])


def b_resposta1(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6, e6, f6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"], C["s06.f"]
    X = 1440
    t0 = C["s05"] - 1.2
    terreno(c, t, t0, t0, t0, lambda tt: "29 m" if tt >= e6 else "?", lambda tt: CERTO if tt >= e6 else COR)
    grosso(c, TA, TC, COR, ep(t, a5, 0.4) * 0.6, 14)
    k = ep(t, a5 + 0.4, 0.4)
    grosso(c, TA, TB, TINTA2, k * (1 - ep(t, f6, 0.3)), 10)
    grosso(c, TB, TC, TINTA2, k * (1 - ep(t, f6, 0.3)), 10)
    grosso(c, TA, TD, AMBAR, ep(t, f6, 0.4), 10)
    grosso(c, TD, TC, AMBAR, ep(t, f6, 0.4), 10)

    def um():
        E.frase(c, t, a5, ps("cerca =", "i", 64) + [("hipotenusa", "g", 70, COR)], X, 250, "center", 0.12)
        E.frase(c, t, a5 + 0.8, ps("lados =", "i", 64) + [("catetos", "g", 70, TINTA2)], X, 350, "center", 0.12)
        E.foco(c, t, b5, 0.5, lambda a: E.pilula(c, "20 e 21: sem terno, vai na conta", X, 490, 48, "g", fundo=TINTA, a=a))
        fcen(c, t, c5, "x^2 = 400 + 441 = 841", X, 680, 84, COR)
    E.saida(c, t, C["s06"] - 0.1, um)
    if t >= C["s06"] - 0.1:
        fcen(c, t, C["s06"], "x^2 = 841", X, 190, 80, COR)
        fcen(c, t, a6, "20^2 = 400     30^2 = 900", X, 320, 66, TINTA2)
        E.frase(c, t, a6 + 0.4, ps("entre", "i", 56) + [("20 e 30", "g", 60)], X, 400, "center", 0.12)
        E.frase(c, t, b6, ps("termina em 1:", "i", 56) + [("…1 ou …9", "g", 62)], X, 510, "center", 0.12)
        E.frase(c, t, c6, ps("perto de 900:", "i", 56) + [("29", "g", 70, COR)], X, 610, "center", 0.12)
        fcen(c, t, d6, "29^2 = 841", X - 60, 720, 72, CERTO)
        selo(c, t, d6 + 0.6, X + 200, 700, 40)
        bola_txt(c, t, e6, "29 m", X, 860, 90, 70, CERTO)
        fcen(c, t, f6, "29 < 20 + 21 = 41", X, 1020, 60, AMBAR)


# ---------------- situação 2 ----------------
def b_questao2(c, t, C, b):
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    marca(c, t, a7, 2)
    antena(c, t, b7 - 0.4, b7 + 0.4, b7 + 0.4, c7, c7)
    E.saida(c, t, C["s08.a"] - 0.1, lambda: E.frase(c, t, b7 + 0.5, ps("antena em pé:", "i", 60) + [("90°", "g", 68, COR)], 1500, 380, "center", 0.12))
    pergunta(c, t, [(b7, ps("antena de", "i", 60) + [("12 m", "g", 66)]),
                    (c7, ps("cabo preso a", "i", 60) + [("9 m", "g", 66)] + ps("do pé", "i", 60)),
                    (d7, ps("o cabo mede", "i", 60) + [("?", "g", 72, COR)])], C["s08.a"])


def b_resposta2(c, t, C, b):
    a9, b9, c9, d9, e9, f9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"], C["s09.f"]
    X = 1440
    t0 = C["s09"] - 1.2
    antena(c, t, t0, t0, t0, t0, t0, lambda tt: "15 m" if tt >= d9 else "?", lambda tt: CERTO if tt >= d9 else COR)
    grosso(c, AT, AC, COR, ep(t, a9, 0.4) * 0.7, 12)
    E.frase(c, t, a9, ps("cabo =", "i", 64) + [("hipotenusa", "g", 70, COR)], X, 200, "center", 0.12)
    fcen(c, t, b9, "9 ÷ 3 = 3     12 ÷ 3 = 4", X, 330, 64, TINTA2)
    E.frase(c, t, c9, ps("terno", "i", 62), X - 250, 460, "center")
    terno(c, t, c9 + 0.2, (3, 4, 5), X + 60, 460, 84)
    fcen(c, t, d9, "5 × 3 = 15", X - 140, 620, 76, CERTO)
    bola_txt(c, t, d9 + 0.4, "15 m", X + 210, 600, 80, 56, CERTO)
    fcen(c, t, e9, "81 + 144 = 225", X, 800, 72)
    fcen(c, t, f9, "r{225} = 15", X - 80, 930, 72, CERTO)
    selo(c, t, f9 + 0.6, X + 170, 905, 40)


# ---------------- situação 3 ----------------
def b_questao3(c, t, C, b):
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    marca(c, t, a10, 3)
    mesa(c, t, b10 - 0.3, c10, c10 + 0.4)
    pergunta(c, t, [(b10, ps("mesa quadrada de", "i", 58) + [("80 cm", "g", 64)]),
                    (c10, ps("régua de", "i", 58) + [("120 cm", "g", 64)] + ps("de canto a canto", "i", 58)),
                    (d10, ps("a régua", "i", 60) + [("cabe?", "g", 70, COR)])], C["s11.a"])


def b_resposta3(c, t, C, b):
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    X = 1440
    t0 = C["s12"] - 1.2
    mesa(c, t, t0, t0, t0, ep(t, d12, 0.4))
    E.foco(c, t, b12, 0.4, lambda a: E.pilula(c, "80√2", MX + ML / 2 - 70, MY + ML / 2 + 40, 50, "g", a=a, cor=E.SOBRE))
    fcen(c, t, a12, "d = ℓr{2}", X, 220, 90, COR)
    fcen(c, t, b12, "d = 80r{2}", X, 360, 84)
    fcen(c, t, c12, "80 × 1,4 = 112", X, 500, 80)
    E.frase(c, t, c12 + 2.0, ps("um pouco mais de", "i", 58) + [("112 cm", "g", 64)], X, 600, "center", 0.12)
    fcen(c, t, d12, "120 > 112", X, 760, 96, ERRADO)
    E.foco(c, t, d12 + 0.8, 0.5, lambda a: E.pilula(c, "não cabe: sobra para fora", X, 900, 58, "g", fundo=ERRADO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    X = W / 2

    def um():
        E.frase(c, t, C["s13"] + 0.2, [("atalho", "g", 90, CLARO)] + ps("para decidir sem arredondar", "i", 76, BR), X, 170, "center", 0.12)
        E.frase(c, t, a13, [("compare os quadrados", "g", 84, BR)], X, 320, "center")
        fcen(c, t, b13, "d^2 = 6.400 + 6.400 = 12.800", X, 500, 84, CLARO)
        fcen(c, t, c13, "120^2 = 14.400", X, 650, 96, BR)
        fcen(c, t, d13, "14.400 > 12.800", X, 820, 96, AMBAR)
        E.frase(c, t, d13 + 0.8, ps("a régua é", "i", 66, CLARO) + [("maior", "g", 72, BR)], X, 950, "center", 0.12)
    E.saida(c, t, C["s14"] - 0.1, um)
    if t >= C["s14"] - 0.1:
        E.frase(c, t, a14, ps("medidas positivas:", "i", 70, CLARO), X, 280, "center", 0.12)
        E.frase(c, t, a14 + 1.0, ps("a maior tem o", "i", 76, BR) + [("maior quadrado", "g", 82, BR)], X, 400, "center", 0.12)
        E.foco(c, t, b14, 0.5, lambda a: E.pilula(c, "pediu o valor? não serve", X, 600, 64, "g", fundo=ERRADO, a=a))
        E.frase(c, t, c14, ps("aí,", "i", 72, CLARO) + [("aproxime a raiz", "g", 80, BR)], X, 790, "center", 0.12)


# ---------------- situação 4 ----------------
def b_questao4(c, t, C, b):
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    marca(c, t, a15, 4)
    placa(c, t, b15 - 0.2, b15 + 0.6, c15)
    pergunta(c, t, [(b15, ps("placa em", "i", 58) + [("equilátero", "g", 64)]),
                    (b15 + 1.0, ps("lado", "i", 58) + [("30 cm", "g", 64)]),
                    (c15, ps("altura", "i", 60) + [("h = ?", "g", 70, AMBAR)])], C["s16.a"])


def b_resposta4(c, t, C, b):
    a17, b17, c17, d17, e17, f17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"], C["s17.e"], C["s17.f"]
    X = 1440
    t0 = C["s17"] - 1.2
    placa(c, t, t0, t0, t0, lambda tt: "≈ 26" if tt >= d17 else "h", lambda tt: CERTO if tt >= d17 else AMBAR, partida=b17)
    if t >= e17:  # a altura errada passa do topo
        k = ease_io(prog(t, e17, 0.8))
        hE = 30 * 16 * math.sqrt(3) / 2 * 2
        y1 = QM[1] - min(hE, 820) * k
        M.line(c, QM[0] - 30, QM[1], QM[0] - 30, y1, ERRADO, 1.0, 7)
    fcen(c, t, a17, "h = f{ℓ}{2} · r{3}", X, 220, 84, COR)
    fcen(c, t, b17, "30 ÷ 2 = 15  →  h = 15r{3}", X, 380, 70)
    fcen(c, t, c17, "15 × 1,7 = 25,5", X, 520, 78)
    bola_txt(c, t, d17, "≈ 26 cm", X, 680, 125, 50, CERTO)
    fcen(c, t, e17, "sem o ÷ 2: 30r{3} > 50", X, 860, 66, ERRADO)
    E.frase(c, t, f17, ps("maior que o lado:", "i", 58) + [("impossível", "g", 64, ERRADO)], X, 970, "center", 0.12)


# ---------------- situação 5 ----------------
def b_questao5(c, t, C, b):
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]
    marca(c, t, a18, 5)
    fig5(c, t, a18 + 0.3, a18 + 0.8, b18, rot=dict(h=("h", AMBAR), b=("?", AMBAR), c=("?", AMBAR)), tl=dict(h=c18, b=c18 + 0.3, c=c18 + 0.3))
    E.saida(c, t, C["s19.a"] - 0.1, lambda: E.frase(c, t, a18 + 0.4, ps("junta", "i", 62) + [("tudo", "g", 70, COR)], 1500, 380, "center", 0.12))
    pergunta(c, t, [(b18, ps("pedaços", "i", 60) + [("9 e 16", "g", 66)]),
                    (c18, ps("altura e catetos", "i", 60) + [("= ?", "g", 70, AMBAR)])], C["s19.a"], y0=860)


def b_resposta5(c, t, C, b):
    a20, b20, c20 = C["s20.a"], C["s20.b"], C["s20.c"]
    a21, b21, c21, d21, e21 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"], C["s21.e"]
    a22, b22, c22 = C["s22.a"], C["s22.b"], C["s22.c"]
    X = 1440
    g = G5
    B, Cc, Hh, A = g["B"], g["C"], g["H"], g["A"]
    t0 = C["s20"] - 1.2
    fig5(c, t, t0, t0, t0, rot=dict(h=((lambda: "12" if t >= c20 else "h")(), CERTO if t >= c20 else AMBAR),
                                     c=((lambda: "15" if t >= c21 else "")(), CERTO),
                                     b=((lambda: "20" if t >= e21 else "")(), CERTO),
                                     a=("", COR)),
         tl=dict(h=t0, c=c21, b=e21, a=a22))
    # os pequenos: o da esquerda (9, 12, c) e o da direita (12, 16, b)
    for pts, ti, tf, cor in (([B, Hh, A], a21, d21, TINTA2), ([Hh, Cc, A], d21, a22, AMBAR)):
        k = ep(t, ti, 0.4) * (1 - ep(t, tf, 0.4))
        if k > 0:
            path = skia.Path(); path.addPoly(pts, True)
            c.drawPath(path, M.paint(cor, 0.28 * k))
    E.foco(c, t, a22, 0.4, lambda a: E.formula(c, "a = 25", (B[0] + Cc[0]) / 2, B[1] + 190, 60, "b", COR, a, "center"))
    grosso(c, B, A, COR, ep(t, a21, 0.4) * (1 - ep(t, d21, 0.4)), 10)
    grosso(c, A, Cc, COR, ep(t, d21, 0.4) * (1 - ep(t, a22, 0.4)), 10)

    def vinte():
        fcen(c, t, a20, "h^2 = m · n", X, 240, 84, COR)
        fcen(c, t, b20, "h^2 = 9 · 16 = 144", X, 400, 80)
        bola_txt(c, t, c20, "h = 12", X, 610, 110, 70, CERTO)
    E.saida(c, t, C["s21"] - 0.1, vinte)

    def vinte1():
        E.frase(c, t, a21, ps("cateto do grande =", "i", 58), X, 170, "center", 0.1)
        E.frase(c, t, a21 + 0.8, [("hipotenusa do pequeno", "g", 60, COR)], X, 250, "center")
        fcen(c, t, b21, "9, 12 = 3, 4 (× 3)", X, 360, 72, TINTA2)
        fcen(c, t, c21, "c = 5 × 3 = 15", X, 470, 76, CERTO)
        fcen(c, t, d21, "12, 16 = 3, 4 (× 4)", X, 640, 72, TINTA2)
        fcen(c, t, e21, "b = 5 × 4 = 20", X, 750, 76, CERTO)
    if t >= C["s21"] - 0.1:
        E.saida(c, t, C["s22"] - 0.1, vinte1)
    if t >= C["s22"] - 0.1:
        E.frase(c, t, C["s22"], ps("conferindo:", "i", 62, COR) + [("a · h = b · c", "g", 66, COR)], X, 220, "center", 0.12)
        fcen(c, t, a22, "a = 9 + 16 = 25", X, 380, 76)
        fcen(c, t, b22, "25 · 12 = 300", X, 520, 80)
        fcen(c, t, c22, "15 · 20 = 300", X - 60, 660, 80, CERTO)
        selo(c, t, c22 + 0.6, X + 290, 635, 46)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s23.a", "ache o", "ângulo reto e a hipotenusa"), ("s23.b", "teste os", "ternos antes da conta"),
                 ("s23.c", "confira:", "hipotenusa = maior lado"))
        for i, (k, it, g) in enumerate(itens):
            y = 400 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(it, "i", 76), (g, "g", 76, COR)], 400, y, passo=0.25)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.foco(c, t, C["s24.a"], 0.5, lambda a: E.pilula(c, "trilha concluída: ângulos e triângulos", XE + 520, 180, 50, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s24.b"] - 0.6, ps("próxima trilha", "i", 80), XE, 330)
    E.frase(c, t, C["s24.b"], [("Polígonos:", "g", 120, COR)], XE, 470)
    E.frase(c, t, C["s24.b"] + 0.5, ps("os quadriláteros", "i", 90), XE, 590, passo=0.14)
    E.frase(c, t, C["s24.c"], ps("paralelogramo, retângulo, losango e trapézio", "i", 58, TINTA2), XE, 710, passo=0.08)
    E.foco(c, t, C["s24.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 360, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1630, p), lerp(680, 385, p), ep(t, C["s24.d"] + 0.2, 0.4))
    E.frase(c, t, C["s24.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4,
              resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
