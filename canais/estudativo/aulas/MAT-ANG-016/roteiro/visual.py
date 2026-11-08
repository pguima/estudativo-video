"""Visual — Estudativo · MAT-ANG-016: ternos pitagóricos (3-4-5, 5-12-13 e múltiplos) e Pitágoras em problemas (escada: 4 m).
Linguagem da geometria plana (MAT-ANG-001 a 020, e a MAT-ANG-015 para Pitágoras): lados em tinta; a hipotenusa em COR (índigo),
o cateto conhecido em TINTA2 e o cateto procurado em AMBAR; ângulo reto = quadradinho; medidas na grotesca; erro em vermelho,
certo em verde; resposta na esfera; atalho no palco escuro.
Um terno aparece como três números numa pílula, com o maior (a hipotenusa) em COR. As figuras respeitam as medidas
(30-40-50, 3-4-5 da escada, 10-24-26 do terreno): a figura não mente.
Peças locais: txt_lado() e grosso() (como na MAT-ANG-015), terno() (os três números, o maior em COR), escada() (dois trilhos
e degraus), parede(), chao(), dobra() (quadrado que dobra o lado e vira quatro), terreno() e pergunta().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-016_ternos_pitagoricos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ternos", "escada", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
assert 30 ** 2 + 40 ** 2 == 50 ** 2 and 9 + 16 == 25 and 25 + 144 == 169 == 13 ** 2
assert (6, 8, 10) == tuple(2 * v for v in (3, 4, 5)) and (9, 12, 15) == tuple(3 * v for v in (3, 4, 5))
assert (30, 40, 50) == tuple(10 * v for v in (3, 4, 5)) and (10, 24, 26) == tuple(2 * v for v in (5, 12, 13))
assert 6 ** 2 == 4 * 9 and 8 ** 2 == 4 * 16 and 10 ** 2 == 4 * 25 and (15 // 5, 20 // 5, 25 // 5) == (3, 4, 5)
assert 25 - 9 == 16 == 4 ** 2 and 9 + 25 == 34 and 5 ** 2 < 34 < 6 ** 2
assert 2 * 2.5 == 5 and 2 * 1.5 == 3 and 4 / 2 == 2 and 2 ** 2 + 1.5 ** 2 == 2.5 ** 2 and 2 ** 2 + 3 ** 2 == 13
assert 10 // 2 == 5 and 26 // 2 == 13 and 12 * 2 == 24 and 26 ** 2 == 676 and 676 - 100 == 576 == 24 ** 2


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


def terno(c, t, t0, nums, cx, y, size=96, cor_n=TINTA, cor_h=None, a=1.0, passo=0.25):
    """os três números do terno separados por vírgula; o último (a hipotenusa) em COR"""
    partes = [(f"{n}," if i < 2 else f"{n}", "g", size, cor_n if i < 2 else (cor_h or COR)) for i, n in enumerate(nums)]
    E.frase(c, t, t0, partes, cx, y, "center", passo)


def parede(c, x, y0, y1, a=1.0, cor=TINTA):
    """parede vista de lado: a face em x, tijolinhos à direita"""
    if a <= 0:
        return
    M.rrect(c, x, y0, 70, y1 - y0, 0, "#E4E2DA", a)
    for i, y in enumerate(range(int(y0), int(y1), 44)):
        M.line(c, x, y, x + 70, y, CINZA, a, 2)
        xm = x + (22 if i % 2 else 48)
        M.line(c, xm, y, xm, min(y + 44, y1), CINZA, a, 2)
    M.line(c, x, y0, x, y1, cor, a, 7)


def chao(c, x0, x1, y, a=1.0, p=1.0, cor=TINTA):
    if a <= 0:
        return
    M.line(c, x0, y, lerp(x0, x1, p), y, cor, a, 6)
    for xx in range(int(x0) + 20, int(x1), 66):
        if xx < lerp(x0, x1, p):
            M.line(c, xx, y + 10, xx - 22, y + 40, TINTA2, a * 0.6, 3)


def escada(c, P, Q, a=1.0, p=1.0, cor="#6B4B2A", larg=34):
    """escada de P (pé) até Q (topo): dois trilhos e degraus; p faz crescer do pé"""
    if a <= 0 or p <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy * larg / 2, -ux * larg / 2
    L = math.dist(P, Q) * p
    Q2 = (P[0] + ux * L, P[1] + uy * L)
    n = int(L // 60)
    for k in range(1, n + 1):
        d = k * 60
        if d < L - 10:
            cx, cy = P[0] + ux * d, P[1] + uy * d
            M.line(c, cx - nx, cy - ny, cx + nx, cy + ny, cor, a, 5)
    for s in (-1, 1):
        M.line(c, P[0] + s * nx, P[1] + s * ny, Q2[0] + s * nx, Q2[1] + s * ny, cor, a, 8)


def dobra(c, t, t0, x, y, s, a=1.0):
    """quadrado de lado s que dobra para 2s: aparecem as quatro cópias"""
    if t < t0 or a <= 0:
        return
    E.foco(c, t, t0, 0.4, lambda k: (M.rrect(c, x, y - s, s, s, 0, E.CLARO, k * a), c.drawRect(skia.Rect.MakeXYWH(x, y - s, s, s), M.paint(TINTA, k * a, stroke=4))))
    for i, (dx, dy) in enumerate(((1, 0), (0, 1), (1, 1))):
        ti = t0 + 0.8 + 0.3 * i
        k = ease_back(prog(t, ti, 0.4))
        if k > 0:
            cx, cy = x + dx * s + s / 2, y - dy * s - s / 2
            h = s / 2 * k
            M.rrect(c, cx - h, cy - h, 2 * h, 2 * h, 0, "#E4E2DA", a)
            c.drawRect(skia.Rect.MakeXYWH(cx - h, cy - h, 2 * h, 2 * h), M.paint(TINTA, a, stroke=4))
    E.foco(c, t, t0 + 1.8, 0.4, lambda k: c.drawRect(skia.Rect.MakeXYWH(x, y - 2 * s, 2 * s, 2 * s), M.paint(COR, k * a, stroke=7)))


def pergunta(c, t, linhas, rel, X=1500, y0=780):
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, y0 + i * 95, "center", 0.12)
    E.relogio(c, t, rel, X, 380, 170)


# ---------------- gancho ----------------
GR, GB, GA = (240, 930), (240 + 40 * 15, 930), (240, 930 - 30 * 15)
GG = ((GR[0] + GB[0] + GA[0]) / 3, (GR[1] + GB[1] + GA[1]) / 3)


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]
    X = 1400

    def um():
        E.triangulo(c, t, a1, GA, GR, GB, vertices=None, retos=(1,), preenche=0.06)
        E.foco(c, t, a1 + 0.6, 0.4, lambda a: (txt_lado(c, GR, GA, "30 m", GG, 64, TINTA, a), txt_lado(c, GR, GB, "40 m", GG, 64, TINTA, a)))
        grosso(c, GA, GB, COR, 1.0, 12, ease_io(prog(t, b1, 0.6)))
        E.foco(c, t, b1 + 0.4, 0.4, lambda a: txt_lado(c, GA, GB, "50 m", GG, 84, COR, a))
        E.frase(c, t, a1 + 0.4, ps("catetos", "i", 76) + [("30", "g", 84), ("e", "i", 76), ("40", "g", 84)], X, 260, "center", 0.14)
        E.frase(c, t, b1, ps("hipotenusa:", "i", 76) + [("50", "g", 100, COR)], X, 400, "center", 0.14)
        E.foco(c, t, b1 + 1.0, 0.5, lambda a: E.pilula(c, "sem nenhuma conta", X, 520, 56, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, c1, ps("um", "i", 76) + [("trio", "g", 84, COR)] + ps("que se repete", "i", 76), X, 700, "center", 0.12)
        terno(c, t, c1 + 1.0, (3, 4, 5), X - 120, 860, 96)
        E.foco(c, t, c1 + 1.8, 0.4, lambda a: E.formula(c, "× 10", X + 200, 860, 80, "g", AMBAR, a, "left"))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("trios", "g", 110, COR)] + ps("de olho", "i", 100), XE, 470, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("e Pitágoras em", "i", 90), XE, 620, passo=0.14)
        E.frase(c, t, tb, [("problemas", "g", 110)], XE, 770, passo=0.14)
        E.foco(c, t, tb + 0.8, 0.5, lambda a: (centro(c, "a escada", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "na parede", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
LR_, LB_, LA_ = (1180, 820), (1180 + 4 * 130, 820), (1180, 820 - 3 * 130)
LG_ = ((LR_[0] + LB_[0] + LA_[0]) / 3, (LR_[1] + LB_[1] + LA_[1]) / 3)


def b_lembrete(c, t, C, b):
    a3, b3, c3 = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, C["s03"] + 0.2, ps("você precisa de", "i", 80, COR), XE, 190, passo=0.12)
    xg = XE + E.larg("você precisa de", "i", 80) + 30
    E.foco(c, t, a3, 0.5, lambda a: E.escreve(c, "1 coisa", xg, 190, 84, "g", COR, a))
    E.foco(c, t, b3, 0.5, lambda a: (E.bola(c, XE + 50, 372, 50, a=a), centro(c, "1", XE + 50, 394, 60, "g", BR, a)))
    E.frase(c, t, b3 + 0.1, [("teorema de Pitágoras", "g", 70)], XE + 140, 400)
    E.foco(c, t, c3 - 0.2, 0.5, lambda a: E.caixa_pontilhada(c, XE + 120, 480, 680, 170, a, COR, prog_=ep(t, c3 - 0.2, 0.6)))
    fcen(c, t, c3, "a^2 = b^2 + c^2", XE + 460, 600, 100, COR)
    E.frase(c, t, c3 + 2.5, [("a", "g", 60, COR)] + ps("= hipotenusa, de frente para o reto", "i", 56), XE + 140, 760, passo=0.08)
    E.triangulo(c, t, b3 + 0.3, LA_, LR_, LB_, vertices=None, retos=(1,), preenche=0.06)
    grosso(c, LA_, LB_, COR, 1.0, 12, ease_io(prog(t, c3 + 0.4, 0.5)))
    E.foco(c, t, c3 + 0.6, 0.4, lambda a: (txt_lado(c, LA_, LB_, "a", LG_, 80, COR, a), txt_lado(c, LR_, LA_, "b", LG_, 80, TINTA, a),
                                           txt_lado(c, LR_, LB_, "c", LG_, 80, TINTA, a)))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), XE, 990, "left", 0.12)


# ---------------- ternos ----------------
TR, TB, TA = (260, 860), (260 + 4 * 140, 860), (260, 860 - 3 * 140)
TG = ((TR[0] + TB[0] + TA[0]) / 3, (TR[1] + TB[1] + TA[1]) / 3)


def b_ternos(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    a5, b5, c5, d5, e5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]
    X = 1400

    def um():
        E.triangulo(c, t, C["s04"], TA, TR, TB, vertices=None, retos=(1,), preenche=0.06)
        E.foco(c, t, a4, 0.4, lambda a: (txt_lado(c, TR, TA, "3", TG, 80, TINTA, a), txt_lado(c, TR, TB, "4", TG, 80, TINTA, a)))
        grosso(c, TA, TB, COR, 1.0, 12, ease_io(prog(t, b4, 0.5)))
        E.foco(c, t, b4 + 0.3, 0.4, lambda a: txt_lado(c, TA, TB, "5", TG, 90, COR, a))
        E.foco(c, t, lerp(b4, c4, 0.5), 0.5, lambda a: E.pilula(c, "tudo inteiro", X, 300, 60, "g", fundo=TINTA, a=a))
        E.frase(c, t, c4, [("terno", "g", 120, COR)], X, 520, "center")
        E.frase(c, t, c4 + 0.4, [("pitagórico", "g", 120, COR)], X, 650, "center")
        E.frase(c, t, d4, ps("terno =", "i", 84) + [("trio", "g", 96)], X, 840, "center", 0.14)
    E.saida(c, t, C["s05"] - 0.1, um)
    if t < C["s05"] - 0.1:
        return
    # os dois ternos famosos
    for i, (ti, tc, nums, conta) in enumerate(((a5, b5, (3, 4, 5), "9 + 16 = 25"), (c5, d5, (5, 12, 13), "25 + 144 = 169"))):
        cx = 520 + i * 880
        E.foco(c, t, ti, 0.5, lambda a, cx=cx, ti=ti: E.caixa_pontilhada(c, cx - 380, 220, 760, 470, a, COR, prog_=ep(t, ti, 0.6)))
        E.frase(c, t, ti, ps("o", "i", 60) + [(("1º" if i == 0 else "2º"), "g", 64, COR)], cx, 310, "center", 0.12)
        terno(c, t, ti + 0.3, nums, cx, 470, 120)
        fcen(c, t, tc, conta, cx, 610, 70, TINTA2)
        # o maior: a hipotenusa
        if t >= e5:
            k = ease_io(prog(t, e5 + 0.3 * i, 0.5))
            wtot = E.larg(f"{nums[0]},", "g", 120) + E.larg(f"{nums[1]},", "g", 120) + E.larg(str(nums[2]), "g", 120) + 2 * 120 * 0.26
            wh = E.larg(str(nums[2]), "g", 120)
            hx = cx + wtot / 2 - wh / 2
            c.drawArc(skia.Rect.MakeXYWH(hx - wh / 2 - 26, 360, wh + 52, 150), -90, 360 * k, False, M.paint(COR, 1.0, stroke=6, cap_round=True))
    E.frase(c, t, e5 + 0.4, ps("o maior é a", "i", 76) + [("hipotenusa", "g", 84, COR)], W / 2, 870, "center", 0.12)


# ---------------- múltiplos ----------------
def b_multiplos(c, t, C, b):
    a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
    a7, b7, c7, d7, e7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]

    def seis():
        E.frase(c, t, a6, ps("multiplique os três pelo", "i", 70) + [("mesmo número", "g", 74, COR)], W / 2, 170, "center", 0.12)
        X1, X2 = 560, 1420
        terno(c, t, a6 + 1.5, (3, 4, 5), X1, 340, 100)
        for k, (ti, f, nums) in enumerate(((b6, "× 2", (6, 8, 10)), (c6, "× 3", (9, 12, 15)), (d6, "× 10", (30, 40, 50)))):
            y = 500 + k * 150
            E.foco(c, t, ti, 0.4, lambda a, y=y, f=f: E.formula(c, f, X1 - 330, y, 64, "g", AMBAR, a, "left"))
            terno(c, t, ti + 0.2, nums, X1 + 70, y, 90, passo=0.15)
        E.foco(c, t, d6 + 1.2, 0.5, lambda a: E.pilula(c, "o do começo", X1 + 70, 1000, 46, "g", fundo=TINTA, a=a))
        terno(c, t, e6, (5, 12, 13), X2, 340, 100)
        E.foco(c, t, e6 + 1.2, 0.4, lambda a: E.formula(c, "× 2", X2 - 330, 500, 64, "g", AMBAR, a, "left"))
        terno(c, t, e6 + 1.4, (10, 24, 26), X2 + 70, 500, 90, passo=0.15)
    E.saida(c, t, C["s07"] - 0.1, seis)
    if C["s07"] - 0.1 <= t < C["s08"]:
        def sete():
            E.frase(c, t, C["s07"], ps("por quê?", "i", 80, COR), W / 2, 170, "center")
            dobra(c, t, a7, 220, 760, 160)
            E.frase(c, t, a7 + 0.3, ps("lado", "i", 64) + [("× 2", "g", 70, AMBAR)], 380, 900, "center", 0.12)
            E.frase(c, t, a7 + 1.8, ps("quadrado", "i", 64) + [("× 4", "g", 70, COR)], 380, 990, "center", 0.12)
            X = 1220
            for k, (ti, s) in enumerate(((b7, "6^2 = 4 × 9"), (c7, "8^2 = 4 × 16"), (d7, "10^2 = 4 × 25"))):
                fcen(c, t, ti, s, X, 350 + k * 150, 96)
            fcen(c, t, e7, "4 × (9 + 16) = 4 × 25", X, 820, 76, CERTO)
            E.foco(c, t, e7 + 0.8, 0.4, lambda a: E.selo(c, X, 940, 50 * ease_back(prog(t, e7 + 0.8, 0.4)), True, a))
        E.saida(c, t, C["s08"] - 0.1, sete)
    if t >= C["s08"] - 0.1:
        E.frase(c, t, C["s08"], ps("para reconhecer:", "i", 80), W / 2, 200, "center", 0.12)
        E.frase(c, t, a8, [("divida", "g", 90, COR)] + ps("os três pelo mesmo número", "i", 76), W / 2, 330, "center", 0.12)
        terno(c, t, b8, (15, 20, 25), W / 2, 540, 120)
        E.foco(c, t, c8 - 0.6, 0.4, lambda a: E.formula(c, "÷ 5", W / 2 - 400, 720, 80, "g", AMBAR, a, "left"))
        terno(c, t, c8, (3, 4, 5), W / 2, 720, 120)
        E.foco(c, t, c8 + 1.4, 0.5, lambda a: E.pilula(c, "é terno: a conta já está feita", W / 2, 900, 60, "g", a=a, cor=E.SOBRE))


# ---------------- a escada ----------------
EP, EW, ET = (800 - 3 * 150, 900), (800, 900), (800, 900 - 4 * 150)   # pé, canto parede-chão, topo
EG = ((EP[0] + EW[0] + ET[0]) / 3, (EP[1] + EW[1] + ET[1]) / 3)


def cena_escada(c, t, t0, te, tp, th, h_txt=lambda tt: "h = ?", h_cor=lambda tt: AMBAR):
    """parede, chão e escada; te = escada (5 m), tp = pé (3 m), th = altura"""
    E.foco(c, t, t0, 0.5, lambda a: parede(c, EW[0], 180, EW[1], a))
    chao(c, 120, 1000, EW[1], 1.0, ease_io(prog(t, t0, 0.6)))
    escada(c, EP, ET, 1.0, ease_io(prog(t, te, 0.8)))
    E.foco(c, t, te + 0.6, 0.4, lambda a: txt_lado(c, EP, ET, "5 m", EG, 70, TINTA, a, gap=40))
    E.foco(c, t, tp, 0.4, lambda a: (M.line(c, EP[0], 970, EW[0], 970, TINTA2, a, 3), centro(c, "3 m", (EP[0] + EW[0]) / 2, 1040, 64, "b", TINTA, a)))
    E.foco(c, t, th, 0.4, lambda a: E.escreve(c, h_txt(t), EW[0] + 100, (EW[1] + ET[1]) / 2 + 24, 72, "g", h_cor(t), a))


def b_escada(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    a12, b12, c12, d12, e12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
    X = 1440

    def nove():
        # o triângulo escondido num retângulo (uma porta, um terreno)
        x, y, w, h = 300, 260, 640, 480
        E.foco(c, t, C["s09"], 0.5, lambda a: c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, a, stroke=6)))
        A, B, D = (x, y), (x + w, y + h), (x, y + h)
        if t >= a9:
            path = skia.Path(); path.addPoly([A, D, B], True)
            c.drawPath(path, M.paint(E.COR, 0.15 * ep(t, a9, 0.5)))
            M.line(c, *A, *B, TINTA, 1.0, 6, progress=ease_io(prog(t, a9, 0.6)))
        E.angulo(c, t, b9, D, B, A, r=70)
        grosso(c, A, B, COR, 1.0, 12, ease_io(prog(t, c9, 0.5)))
        E.frase(c, t, a9, ps("ache o", "i", 70) + [("triângulo retângulo", "g", 70, COR)], X, 300, "center", 0.12)
        E.frase(c, t, a9 + 0.8, ps("escondido", "i", 70), X, 390, "center")
        E.frase(c, t, b9, ps("procure o", "i", 70) + [("ângulo reto", "g", 74)], X, 560, "center", 0.12)
        E.frase(c, t, c9, [("hipotenusa", "g", 76, COR)] + ps("= de frente", "i", 70), X, 720, "center", 0.12)
        E.frase(c, t, c9 + 0.6, ps("para ele", "i", 70), X, 810, "center")
    E.saida(c, t, C["s10"] - 0.1, nove)
    if t < C["s10"] - 0.1:
        return
    cena_escada(c, t, C["s10"], a10, b10, c10, lambda tt: "4 m" if tt >= c12 else "h = ?", lambda tt: CERTO if tt >= c12 else AMBAR)
    E.angulo(c, t, a11, EW, ET, EP, r=70)
    if t >= b11:
        grosso(c, EP, ET, COR, 0.75 * ep(t, b11, 0.4), 12)
    grosso(c, EP, EW, TINTA2, ep(t, c11, 0.4), 12)
    grosso(c, EW, ET, AMBAR, ep(t, d11, 0.4), 12)

    def dez():
        E.frase(c, t, a10, ps("escada de", "i", 70) + [("5 m", "g", 80)], X, 300, "center", 0.12)
        E.frase(c, t, b10, ps("pé a", "i", 70) + [("3 m", "g", 80)] + ps("da parede", "i", 70), X, 430, "center", 0.12)
        E.frase(c, t, c10, ps("até que", "i", 70) + [("altura?", "g", 80, AMBAR)], X, 560, "center", 0.12)
    E.saida(c, t, C["s11"] - 0.1, dez)

    def onze():
        E.frase(c, t, a11, ps("parede e chão:", "i", 64) + [("90°", "g", 72, COR)], X, 260, "center", 0.12)
        E.frase(c, t, b11, ps("escada =", "i", 64) + [("hipotenusa 5", "g", 72, COR)], X, 400, "center", 0.12)
        E.frase(c, t, c11, ps("chão =", "i", 64) + [("cateto 3", "g", 72, TINTA2)], X, 540, "center", 0.12)
        E.frase(c, t, d11, ps("parede =", "i", 64) + [("cateto ?", "g", 72, AMBAR)], X, 680, "center", 0.12)
    if t >= C["s11"] - 0.1:
        E.saida(c, t, C["s12"] - 0.1, onze)
    if t >= C["s12"] - 0.1:
        terno(c, t, a12, (3, "?", 5), X, 260, 100, cor_n=TINTA)
        E.saida(c, t, b12, lambda: E.frase(c, t, a12 + 1.0, ps("o 5 na hipotenusa", "i", 56, TINTA2), X, 350, "center", 0.1))
        E.foco(c, t, b12, 0.5, lambda a: E.pilula(c, "terno 3, 4, 5", X, 375, 54, "g", a=a, cor=E.SOBRE))
        bola_txt(c, t, c12, "4 m", X, 530, 110, 84, CERTO)
        fcen(c, t, d12, "25 − 9 = 16", X, 770, 84)
        fcen(c, t, e12, "r{16} = 4", X - 70, 900, 84)
        E.foco(c, t, e12 + 0.8, 0.4, lambda a: E.selo(c, X + 150, 875, 46 * ease_back(prog(t, e12 + 0.8, 0.4)), True, a))


# ---------------- erro ----------------
KR, KB, KA = (300, 820), (300 + 5 * 110, 820), (300, 820 - 3 * 110)   # catetos 3 e 5
KG = ((KR[0] + KB[0] + KA[0]) / 3, (KR[1] + KB[1] + KA[1]) / 3)


def b_erro(c, t, C, b):
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    X = 1400
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)] + ps("com este erro", "i", 90), W / 2, 150, "center", 0.14)
    E.frase(c, t, a13, ps("viu", "i", 70) + [("3 e 5", "g", 76)] + ps("e completou com", "i", 70) + [("4?", "g", 76, ERRADO)], W / 2, 270, "center", 0.12)
    E.triangulo(c, t, b13 - 0.4, KA, KR, KB, vertices=None, retos=(1,), preenche=0.06)
    E.foco(c, t, b13, 0.4, lambda a: (txt_lado(c, KR, KA, "3", KG, 76, TINTA2, a), txt_lado(c, KR, KB, "5", KG, 76, TINTA2, a)))
    grosso(c, KR, KA, TINTA2, ep(t, b13, 0.4), 12)
    grosso(c, KR, KB, TINTA2, ep(t, b13, 0.4), 12)
    E.frase(c, t, b13 + 0.3, ps("3 e 5 são os", "i", 64) + [("catetos", "g", 70, TINTA2)], X, 420, "center", 0.12)
    grosso(c, KA, KB, COR, 1.0, 12, ease_io(prog(t, c13, 0.5)))
    fcen(c, t, c13, "a^2 = 9 + 25 = 34", X, 560, 90, COR)
    # o 4 riscado na hipotenusa e o √34
    E.saida(c, t, a14 + 1.2, lambda: E.foco(c, t, c13 + 0.6, 0.4, lambda a: txt_lado(c, KA, KB, "4", KG, 90, ERRADO, a)))
    if t >= a14:
        mx, my = meio(KA, KB)
        E.saida(c, t, a14 + 1.2, lambda: E.risco(c, mx - 30, my - 120, mx + 90, my - 20, t, a14, ERRADO, 10))
    E.foco(c, t, a14 + 1.2, 0.4, lambda a: txt_lado(c, KA, KB, "r{34}", KG, 84, COR, a))
    E.frase(c, t, a14, [("34", "g", 76)] + ps("não tem raiz exata", "i", 66), X, 690, "center", 0.12)
    vx = E.reta(c, t, b14 - 0.3, 1050, 1750, 820, 5, 6, (5, 6), size=56)
    if t >= b14:
        v = 5 + (34 - 25) / (36 - 25)
        k = ease_back(prog(t, b14 + 0.2, 0.4))
        c.drawCircle(vx(v), 820, 16 * k, M.paint(COR))
        E.foco(c, t, b14 + 0.3, 0.4, lambda a: E.formula(c, "r{34}", vx(v), 770, 56, "g", COR, a, "center"))
    E.frase(c, t, c14, ps("terno só com o", "i", 60) + [("maior na hipotenusa", "g", 62, COR)], W / 2, 990, "center", 0.1)
    if t >= d14:  # quem está de frente para o reto: seta do quadradinho até a hipotenusa
        k = ep(t, d14, 0.5)
        M.arrow(c, KR[0] + 60, KR[1] - 60, KG[0] + 80, KG[1] - 30, COR, k, 6, 20, k)


# ---------------- atalho (palco escuro) ----------------
def tri_px(c, t, t0, R, u, b_, h_, rot, a=1.0, d=0.6):
    """triângulo retângulo no palco: reto em R, base b_ para a esquerda, altura h_ para cima (em unidades u)"""
    P, T = (R[0] - b_ * u, R[1]), (R[0], R[1] - h_ * u)
    if t < t0:
        return P, T
    q = ease_io(prog(t, t0, d))
    path = skia.Path(); path.addPoly([P, R, T], True)
    c.drawPath(path, M.paint(CLARO, 0.12 * q * a))
    for A_, B_ in ((P, R), (R, T), (T, P)):
        M.line(c, *A_, *B_, BR, a, 6, progress=q)
    E.angulo(c, t, t0 + 0.3, R, P, T, r=40, cor=CLARO)
    G = ((P[0] + R[0] + T[0]) / 3, (P[1] + R[1] + T[1]) / 3)
    for (A_, B_), s, ti in zip(((P, T), (P, R), (R, T)), rot, (t0 + 0.4, t0 + 0.5, t0 + 0.6)):
        if s:
            s_, tt, cr = s if isinstance(s, tuple) else (s, ti, BR)
            E.foco(c, t, tt, 0.4, lambda k, A_=A_, B_=B_, s_=s_, cr=cr: txt_lado(c, A_, B_, s_, G, 56, cr, k * a))
    return P, T


def b_atalho(c, t, C, b):
    palco(c, t)
    a15, b15, c15, d15, e15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]
    a16, b16, c16, d16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]

    def um():
        E.frase(c, t, C["s15"] + 0.2, [("atalho", "g", 90, CLARO)] + ps("para medidas com vírgula", "i", 76, BR), W / 2, 150, "center", 0.12)
        u = 110
        tri_px(c, t, a15, (620, 860), u, 1.5, 2, (("2,5", a15 + 0.4, BR), ("1,5", b15, BR), ((lambda: "2" if t >= e15 + 0.6 else "?")(), b15 + 0.4, AMBAR)))
        tri_px(c, t, c15 + 0.3, (1620, 860), u, 3, 4, (("5", c15 + 0.6, BR), ("3", c15 + 0.7, BR),
                                                      ((lambda: "4" if t >= d15 else "?")(), c15 + 0.8, AMBAR)))
        E.foco(c, t, c15, 0.4, lambda a: (M.arrow(c, 760, 480, 1060, 480, CLARO, a, 6, 22, a), E.formula(c, "× 2", 910, 440, 70, "g", CLARO, a, "center")))
        if t >= e15:
            E.foco(c, t, e15, 0.4, lambda a: (M.arrow(c, 1060, 640, 760, 640, AMBAR, a, 6, 22, a), E.formula(c, "÷ 2", 910, 720, 70, "g", AMBAR, a, "center")))
        E.foco(c, t, d15, 0.4, lambda a: E.pilula(c, "terno 3, 4, 5", 1500, 300, 48, "g", fundo=E.COR, a=a))
        bola_txt(c, t, e15 + 0.6, "2 m", 910, 890, 90, 64, CERTO)
    E.saida(c, t, C["s16"] - 0.1, um)
    if t < C["s16"] - 0.1:
        return
    X = W / 2
    E.frase(c, t, C["s16"] + 0.1, ps("o mesmo motivo dos múltiplos", "i", 70, CLARO), X, 170, "center", 0.12)
    E.frase(c, t, a16, [("× ou ÷", "g", 84, BR)] + ps("os três lados pelo mesmo número", "i", 66, CLARO), X, 300, "center", 0.12)
    E.frase(c, t, a16 + 1.4, ps("Pitágoras", "i", 66, CLARO) + [("continua valendo", "g", 70, BR)], X, 400, "center", 0.12)
    E.foco(c, t, b16, 0.5, lambda a: E.pilula(c, "sem terno, não compensa", X, 540, 60, "g", fundo=ERRADO, a=a))
    tri_px(c, t, c16, (760, 960), 95, 2, 3, (("r{13}", c16 + 0.8, CLARO), ("2", c16 + 0.3, BR), ("3", c16 + 0.3, BR)))
    fcen(c, t, c16 + 0.5, "a^2 = 4 + 9 = 13", 1340, 760, 80, BR)
    E.frase(c, t, d16, ps("aí,", "i", 66, CLARO) + [("a conta", "g", 72, BR)] + ps("é o caminho", "i", 66, CLARO), 1340, 900, "center", 0.12)


# ---------------- questão ----------------
QX, QY, QU = 420, 180, 30          # terreno 10 x 24 (frente embaixo), visto de cima
QA, QB, QC, QD = (QX, QY + 24 * QU), (QX + 10 * QU, QY + 24 * QU), (QX + 10 * QU, QY), (QX, QY)   # A frente esq, B frente dir, C fundo dir, D fundo esq


def terreno(c, t, t0, tr, td, tf, tl, lado=lambda tt: "x = ?", lado_cor=lambda tt: AMBAR):
    if t < t0:
        return
    q = ease_io(prog(t, t0, 0.6))
    c.drawRect(skia.Rect.MakeXYWH(QX, QY, 10 * QU, 24 * QU), M.paint("#DDEFD5", 0.9 * q))
    E._contorno(c, [QA, QB, QC, QD], q, TINTA, 6)
    for V, P, Q in ((QA, QB, QD), (QB, QC, QA), (QC, QD, QB), (QD, QA, QC)):
        E.angulo(c, t, tr, V, P, Q, r=44)
    if t >= td:
        M.line(c, *QA, *QC, TINTA, 1.0, 6, dash=E.TRACO, progress=ease_io(prog(t, td, 0.7)))
        E.foco(c, t, td + 0.5, 0.4, lambda a: E.pilula(c, "26 m", *meio(QA, QC), 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, tf, 0.4, lambda a: centro(c, "10 m", (QA[0] + QB[0]) / 2, QA[1] + 80, 60, "b", TINTA, a))
    E.foco(c, t, tl, 0.4, lambda a: E.escreve(c, lado(t), QX - 40 - E.formula(None, lado(t), 0, 0, 64, "g", a=0), (QA[1] + QD[1]) / 2 + 22, 64, "g", lado_cor(t), a))


def b_questao(c, t, C, b):
    a17, b17, c17, d17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 120, passo=0.12)
    terreno(c, t, a17 - 0.4, a17 + 0.2, b17, c17, d17, lambda tt: "x")
    E.saida(c, t, C["s18.a"] - 0.1, lambda: (E.frase(c, t, a17 + 0.4, ps("terreno", "i", 64) + [("retangular", "g", 70)], 1500, 300, "center", 0.12),
                                             E.frase(c, t, d17 + 0.8, ps("tente", "i", 60, COR) + [("sem quadrados", "g", 64, COR)], 1500, 420, "center", 0.12)))
    pergunta(c, t, [(b17, ps("canto a canto:", "i", 62) + [("26 m", "g", 70)]),
                    (c17, ps("frente:", "i", 62) + [("10 m", "g", 70)]),
                    (d17, ps("lado", "i", 62) + [("x = ?", "g", 72, AMBAR)])], C["s18.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a19, b19, c19, d19, e19 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"], C["s19.e"]
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    X = 1400
    t0 = C["s19"] - 1.2
    terreno(c, t, t0, t0, t0, t0, t0, lambda tt: "24 m" if tt >= e19 else "x", lambda tt: CERTO if tt >= e19 else AMBAR)
    if t >= a19:  # um dos dois triângulos
        path = skia.Path(); path.addPoly([QA, QB, QC], True)
        c.drawPath(path, M.paint(E.COR, 0.18 * ep(t, a19, 0.5)))
    grosso(c, QA, QC, COR, 1.0, 12, ease_io(prog(t, b19, 0.6)))
    grosso(c, QB, QC, AMBAR, ep(t, d19, 0.4), 10)
    E.pilula(c, "26 m", *meio(QA, QC), 50, "g", fundo=TINTA)   # a medida por cima do destaque

    def um():
        E.frase(c, t, a19, [("2", "g", 76, COR)] + ps("triângulos retângulos", "i", 66), X, 230, "center", 0.12)
        E.frase(c, t, b19, ps("26 =", "i", 66) + [("hipotenusa", "g", 70, COR)], X, 340, "center", 0.12)
        fcen(c, t, c19, "10 ÷ 2 = 5", X - 230, 500, 70)
        fcen(c, t, c19 + 0.8, "26 ÷ 2 = 13", X + 230, 500, 70)
        E.frase(c, t, d19, ps("terno", "i", 66), X - 260, 650, "center")
        terno(c, t, d19 + 0.2, (5, 12, 13), X + 60, 650, 90)
        fcen(c, t, e19, "12 × 2 = 24", X, 790, 84, AMBAR)
        bola_txt(c, t, e19 + 0.8, "24 m", X, 950, 95, 66, CERTO)
    E.saida(c, t, C["s20"] - 0.1, um)
    if t >= C["s20"] - 0.1:
        E.frase(c, t, C["s20"], ps("conferindo por Pitágoras", "i", 66, COR), X, 220, "center", 0.12)
        fcen(c, t, a20, "26^2 = 676", X, 380, 84)
        fcen(c, t, b20, "10^2 = 100", X, 510, 84)
        fcen(c, t, c20, "676 − 100 = 576", X, 660, 84, AMBAR)
        fcen(c, t, d20, "24^2 = 576", X - 90, 820, 90, CERTO)
        E.foco(c, t, d20 + 0.8, 0.4, lambda a: E.selo(c, X + 220, 790, 55 * ease_back(prog(t, d20 + 0.8, 0.4)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s21.a", "decore", "3, 4, 5"), ("s21.b", "e", "5, 12, 13"), ("s21.c", "procure os", "múltiplos"),
                 ("s21.d", "o maior na", "hipotenusa"))
        for i, (k, it, g) in enumerate(itens):
            y = 360 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 420, y - 30, 52, a=a), centro(c, str(i + 1), 420, y - 8, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(it, "i", 76), (g, "g", 84, COR)], 520, y, passo=0.25)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.2, ps("próxima aula", "i", 84), XE, 260)
    E.frase(c, t, C["s22.a"], ps("Pitágoras em", "i", 84) + [("2 figuras", "g", 96, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s22.b"], [("a diagonal", "g", 100, COR)] + ps("do quadrado", "i", 84), XE, 550, passo=0.14)
    E.frase(c, t, C["s22.c"], [("a altura", "g", 100, COR)] + ps("do equilátero", "i", 84), XE, 700, passo=0.14)
    E.foco(c, t, C["s22.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1630, p), lerp(650, 355, p), ep(t, C["s22.d"] + 0.2, 0.4))
    E.frase(c, t, C["s22.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ternos=b_ternos, multiplos=b_multiplos, escada=b_escada, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
