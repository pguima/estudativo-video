"""Visual — Estudativo · MAT-TOP-013: praticando distâncias, circunferências e cônicas (aula de prática, cinco situações).

Segue a linguagem das cônicas do MAT-TOP-011 e 012: plano na metade direita, texto na esquerda, curva em índigo, focos em
tinta com "F"; A_ índigo = o á, B_ âmbar = o bê, C_ petróleo = o cê. Cada situação: enunciado com o desenho, relógio de
pausa, resposta passo a passo com o desenho completo. No Sarrus, as diagonais que descem em índigo e as que sobem em âmbar.
Atalho (inclinação) no palco escuro."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-013_praticando_distancias_e_conicas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "atalho", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
A_, B_, C_ = E.COR, "#D98A00", "#0E9AA7"
C_ESC = "#3CC7D3"
# conferência das contas
assert abs(4 * 2 + 3 * 3 + 3) == 20 and math.hypot(4, 3) == 5 and 20 / 5 == 4
PE = (2 - 4 * 4 / 5, 3 - 3 * 4 / 5)  # pé da perpendicular
assert abs(4 * PE[0] + 3 * PE[1] + 3) < 1e-9
MZ = ((1, 1, 1), (3, 5, 1), (4, 8, 1))
_d = MZ[0][0] * MZ[1][1] * MZ[2][2] + MZ[0][1] * MZ[1][2] * MZ[2][0] + MZ[0][2] * MZ[1][0] * MZ[2][1]
_s = MZ[0][2] * MZ[1][1] * MZ[2][0] + MZ[0][0] * MZ[1][2] * MZ[2][1] + MZ[0][1] * MZ[1][0] * MZ[2][2]
assert (_d, _s, _d - _s) == (33, 31, 2) and (5 - 1) / (3 - 1) == 2 and (8 - 5) / (4 - 3) == 3
assert math.hypot(7 - 1, 10 - 2) == 10 == 2 + 8
assert 100 - 36 == 64 and 2 * 10 == 20 and 12 / 4 == 3 and 9 + 16 == 25

PA = E.Plano(1100, 200, 720, 720, -4, 5, -4, 5)        # situação 1: 80 px por unidade
PC = E.Plano(1170, 170, 630, 700, -2, 16, -1, 19)      # situação 3: 35 px por unidade
PE4 = E.Plano(960, 260, 840, 560, -12, 12, -8, 8)      # situação 4: 35 px por unidade


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def plano(c, t, t0, P, mx=None, my=None, size=34, escuro=False):
    return E.plano(c, t, t0, *P.caixa, P.xmin, P.xmax, P.ymin, P.ymax, marcas_x=mx if mx is not None else [],
                   marcas_y=my if my is not None else [], size=size, escuro=escuro)


def caminho(c, pts, cor, largura, a=1.0, dash=None):
    if len(pts) < 2 or a <= 0:
        return
    path = skia.Path(); path.moveTo(*pts[0])
    for p_ in pts[1:]:
        path.lineTo(*p_)
    pt = M.paint(cor, a, stroke=largura, cap_round=True)
    if dash:
        pt.setPathEffect(skia.DashPathEffect.Make(dash, 0))
    c.drawPath(path, pt)


def elipse_px(c, cx, cy, rx, ry, p=1.0, cor=None, largura=8, a=1.0, ini=0.0):
    if p <= 0 or a <= 0:
        return
    n = max(2, int(220 * p))
    th0 = math.radians(ini)
    caminho(c, [(cx + rx * math.cos(th0 + 2 * math.pi * p * i / n), cy - ry * math.sin(th0 + 2 * math.pi * p * i / n)) for i in range(n + 1)],
            cor or COR, largura, a)


def elipse(c, t, t0, P, cx, cy, a, b, d=1.0, cor=None, largura=7, ini=0.0):
    k = P.x(1) - P.x(0)
    elipse_px(c, P.x(cx), P.y(cy), a * k, b * k, ease_io(prog(t, t0, d)), cor, largura, 1.0, ini)


def hip_px(c, cx, cy, ka, kb, xmax_px, ymax_px, p=1.0, cor=None, largura=8, a=1.0, vertical=False):
    if p <= 0 or a <= 0:
        return
    if not vertical:
        U = min(math.asinh(ymax_px / kb), math.acosh(max(1.0, xmax_px / ka)))
    else:
        U = min(math.asinh(xmax_px / kb), math.acosh(max(1.0, ymax_px / ka)))
    for ramo in (1, -1):
        for lado in (1, -1):
            pts = []
            for i in range(81):
                u = lado * U * p * i / 80
                X, Y = ka * math.cosh(u) * ramo, kb * math.sinh(u)
                pts.append((cx + Y, cy - X) if vertical else (cx + X, cy - Y))
            caminho(c, pts, cor or COR, largura, a)


def foco_pt(c, t, t0, P, x, y, nome="F", lado=(0, 1), cor=TINTA, size=42):
    E.ponto(c, t, t0, P, x, y, None, cor=cor, r=13)
    if nome:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E._cola(c, nome, *P(x, y), lado[0], lado[1], 20, size, "b", cor, a))


def seg(c, t, t0, A, B, cor, d=0.6, largura=9, a=1.0, tracejado=False):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *A, *B, cor, a, largura, progress=p, dash=E.TRACO if tracejado else None)


def conta(c, partes, x, y, size, a=1.0, align="left", est="g"):
    ws = [E.formula(None, s, 0, 0, size, est, a=0) for s, _ in partes]
    w = sum(ws)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    if a > 0:
        for (s, cor), wi in zip(partes, ws):
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += wi
    return w


def conta_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: conta(c, partes, x, y, size, a, align))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")))


def titulo(c, t, t0, n):
    E.frase(c, t, t0, [("situação", "i", 66, COR), (str(n), "g", 66, COR)], XE, 190)


def pausa(c, t, t0, cx=1460, cy=470, r=190):
    E.relogio(c, t, t0, cx=cx, cy=cy, r=r)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 200, COR), ("situações", "i", 150)], XE, 330)
    itens = (("s01.b", "distâncias"), ("s01.b", "pontos alinhados"), ("s01.b", "circunferências"), ("s01.c", "cônicas"))
    for i, (k, s) in enumerate(itens):
        x = XE + (i % 2) * 760
        y = 520 + (i // 2) * 140
        E.foco(c, t, C[k] + 0.5 * i if k == "s01.b" else C[k], 0.5, lambda a, x=x, y=y, i=i: (
            E.bola(c, x + 34, y - 26, 34, a=a), E.escreve(c, str(i + 1), x + 34 - E.larg(str(i + 1), "g", 40) / 2, y - 12, 40, "g", BR, a)))
        E.frase(c, t, (C[k] + 0.5 * i if k == "s01.b" else C[k]) + 0.1, [(s, "g", 70)], x + 100, y)
    E.foco(c, t, C["s01.d"], 0.5, lambda a: E.pilula(c, "pause e resolva", W / 2, 930, 60, "g", a=a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02.a"], [("as", "i", 80), ("ferramentas", "g", 80, COR)], W / 2, 170, "center")
    itens = (("s02.b", "distância ponto–reta:", "d = f{|ax₀ + by₀ + c|}{r{a^2 + b^2}}"),
             ("s02.c", "alinhados:", "det = 0"),
             ("s02.d", "circunferências:", "centros × raios"),
             ("s02.e", "cônicas:", "sinais e a conta do c"))
    for i, (k, l1, f) in enumerate(itens):
        y = 330 + i * 170
        E.frase(c, t, C[k], [(l1, "i", 62)], XE + 40, y)
        E.foco(c, t, C[k] + 0.4, 0.5, lambda a, f=f, y=y, i=i: E.formula(c, f, 900, y + (10 if i == 0 else 0), 64 if i == 0 else 66, "g", COR, a))
    E.frase(c, t, C["s03"] - 2.4, ps("travou? procure a aula no canal", "i", 50, TINTA2), W / 2, 1010, "center", passo=0.1)


# ---------------- situação 1: distância de ponto a reta ----------------
def reta1(c, t, t0, P, d=0.8):
    f = lambda x: (-4 * x - 3) / 3
    p = ease_io(prog(t, t0, d))
    if p > 0:
        x0, x1 = -4, 2.25
        M.line(c, *P(x0, f(x0)), *P(lerp(x0, x1, p), f(lerp(x0, x1, p))), TINTA, 1.0, 7)


def desenho1(c, t, t0, tp=None, tr=None):
    plano(c, t, t0, PA, [-2, 2, 4], [-2, 2, 4], 34)
    reta1(c, t, t0 + 0.4, PA)
    E.foco(c, t, t0 + 1.0, 0.4, lambda a: E.pilula(c, "estrada", *PA(-3.1, 4.3), 38, "g", fundo=TINTA, a=a))
    E.ponto(c, t, t0 + 0.6, PA, 2, 3, None, cor=COR, r=16)
    E.foco(c, t, t0 + 0.8, 0.4, lambda a: E._cola(c, "torre (2, 3)", *PA(2, 3), 1, -1, 18, 42, "b", COR, a))
    if tp is not None and t >= tp:
        seg(c, t, tp, PA(2, 3), PA(*PE), COR, 0.7, 6, tracejado=True)
        E.angulo(c, t, tp + 0.6, PA(*PE), PA(2, 3), PA(PE[0] - 0.6, -(4 * (PE[0] - 0.6) + 3) / 3), r=34, cor=TINTA, preenche=0.1)
    if tr is not None:
        E.foco(c, t, tr, 0.4, lambda a: E.pilula(c, "4 km", *PA(1.3, 1.2), 46, "g", fundo=CERTO, a=a))


def b_questao1(c, t, C, b):
    desenho1(c, t, C["s03.a"], C["s03.c"])
    titulo(c, t, C["s03"], 1)
    E.frase(c, t, C["s03.a"], [("torre", "i", 66)], XE, 340)
    conta_em(c, t, C["s03.a"] + 0.3, [("(2, 3)", COR)], XE + 200, 340, 66)
    E.frase(c, t, C["s03.b"], [("estrada:", "i", 66)], XE, 460)
    conta_em(c, t, C["s03.b"] + 0.4, [("4x + 3y + 3 = 0", TINTA)], XE, 570, 70)
    E.frase(c, t, C["s03.b"] + 2.0, ps("em quilômetros", "i", 50, TINTA2), XE, 650)
    E.frase(c, t, C["s03.c"], [("menor", "g", 70, COR), ("distância?", "i", 74)], XE, 790)
    if t >= C["s04"]:
        pausa(c, t, C["s04.a"], 880, 790, 70)


def b_resposta1(c, t, C, b):
    desenho1(c, t, C["s05"] - 3, C["s06.d"], C["s06.c"])
    E.formula_em(c, t, C["s05"], "d = f{|4 · 2 + 3 · 3 + 3|}{r{4^2 + 3^2}}", XE, 330, 72)
    conta_em(c, t, C["s05.b"], [("4 · 2 = 8", TINTA)], XE, 520, 60)
    conta_em(c, t, C["s05.c"], [("3 · 3 = 9", TINTA)], XE + 330, 520, 60)
    conta_em(c, t, C["s05.d"], [("|8 + 9 + 3| = ", TINTA), ("20", COR)], XE, 630, 66)
    conta_em(c, t, C["s06.a"], [("r{16 + 9} = r{25} = ", TINTA), ("5", COR)], XE, 760, 66)
    conta_em(c, t, C["s06.c"], [("d = f{20}{5} = ", TINTA)], XE, 920, 72)
    bola_txt(c, t, C["s06.c"] + 0.3, "4 km", XE + 420, 895, 85, 52, CERTO)


# ---------------- situação 2: alinhamento ----------------
PTS2 = ((1, 1), (3, 5), (4, 8))


def b_questao2(c, t, C, b):
    titulo(c, t, C["s07"], 2)
    for i, (k, (x, y)) in enumerate(zip(("s07.a", "s07.b", "s07.c"), PTS2)):
        conta_em(c, t, C[k], [(f"({x}, {y})", COR)], XE + i * 330, 380, 80)
    E.frase(c, t, C["s07.c"] + 0.8, [("estão", "i", 90), ("alinhados?", "g", 90, COR)], XE, 560)
    P = E.Plano(1260, 200, 440, 700, 0, 5.5, 0, 8.75)
    plano(c, t, C["s07"], P, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8], 28)
    for k, (x, y) in zip(("s07.a", "s07.b", "s07.c"), PTS2):
        E.ponto(c, t, C[k] + 0.2, P, x, y, None, cor=COR, r=13)
    if t >= C["s08"]:
        pausa(c, t, C["s08.a"], 560, 790, 80)


def b_resposta2(c, t, C, b):
    titulo(c, t, C["s09"], 2)
    x0, y0, dx, dy, s = 380, 380, 150, 140, 80
    # matriz com a coluna de uns, e as duas colunas copiadas
    for i, linha in enumerate(MZ):
        for j, v in enumerate(linha):
            tt = C["s09.a"] + 0.25 * i + (0.6 if j == 2 else 0)
            E.foco(c, t, tt, 0.4, lambda a, i=i, j=j, v=v: E.centro(c, str(v), x0 + j * dx, y0 + i * dy, s, "g", A_ if j == 2 else TINTA, a))
        for j in range(2):
            E.foco(c, t, C["s09.b"] + 0.2 * i, 0.4, lambda a, i=i, j=j: E.centro(c, str(MZ[i][j]), x0 + (3 + j) * dx, y0 + i * dy, s, "g", CINZA, a))
    q = ep(t, C["s09.a"], 0.4)
    if q > 0:
        for xb in (x0 - 75, x0 + 2 * dx + 75):
            M.line(c, xb, y0 - 90, xb, y0 + 2 * dy + 30, TINTA, q, 6)
    # diagonais
    for j in range(3):
        p = ep(t, C["s10.a"] + 0.3 * j, 0.5)
        if p > 0:
            M.line(c, x0 + j * dx - 40, y0 - 70, x0 + (j + 2) * dx + 40, y0 + 2 * dy + 10, A_, 0.55 * p, 9, progress=p)
        p = ep(t, C["s10.b"] + 0.3 * j, 0.5)
        if p > 0:
            M.line(c, x0 + j * dx - 40, y0 + 2 * dy + 10, x0 + (j + 2) * dx + 40, y0 - 70, B_, 0.55 * p, 9, progress=p)
    conta_em(c, t, C["s10.a"] + 1.0, [("5 + 4 + 24 = ", TINTA), ("33", A_)], 1250, 400, 70)
    conta_em(c, t, C["s10.b"] + 1.0, [("20 + 8 + 3 = ", TINTA), ("31", B_)], 1250, 530, 70)
    conta_em(c, t, C["s10.c"], [("33 − 31 = 2", TINTA)], 1250, 680, 76)
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "≠ 0: não alinhados", 1440, 800, 54, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s10.a"], [("descendo", "i", 54, A_)], 380, 860)
    E.frase(c, t, C["s10.b"], [("menos", "i", 54), ("subindo", "i", 54, B_)], 680, 860)


# ---------------- atalho: inclinação (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    P = E.Plano(1180, 170, 480, 760, 0, 6, 0, 9.5)
    plano(c, t, C["s11"], P, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9], 30, escuro=True)
    for i, (x, y) in enumerate(PTS2):
        E.ponto(c, t, C["s11"] + 0.3 + 0.2 * i, P, x, y, None, cor=BR, r=13)
    if t >= C["s11.b"]:
        q = ep(t, C["s11.b"], 0.5)
        M.line(c, *P(1, 1), *P(3, 1), C_ESC, q, 7)
        M.line(c, *P(3, 1), *P(3, 5), "#FFB833", q, 7)
        M.line(c, *P(1, 1), *P(3, 5), BR, q * 0.8, 5)
        E.foco(c, t, C["s11.b"] + 0.4, 0.4, lambda a: (E._cola(c, "2", *P(2, 1), 0, 1, 10, 40, "g", C_ESC, a),
                                                      E._cola(c, "4", *P(3, 3), 1, 0, 10, 40, "g", "#FFB833", a)))
    if t >= C["s11.c"]:
        q = ep(t, C["s11.c"], 0.5)
        M.line(c, *P(3, 5), *P(4, 5), C_ESC, q, 7)
        M.line(c, *P(4, 5), *P(4, 8), "#FFB833", q, 7)
        M.line(c, *P(3, 5), *P(4, 8), BR, q * 0.8, 5)
        E.foco(c, t, C["s11.c"] + 0.4, 0.4, lambda a: (E._cola(c, "1", *P(3.5, 5), 0, 1, 10, 40, "g", C_ESC, a),
                                                      E._cola(c, "3", *P(4, 6.5), 1, 0, 10, 40, "g", "#FFB833", a)))

    def s11():
        E.frase(c, t, C["s11"], ps("sem determinante:", "i", 66, CLARO), XE, 220)
        E.frase(c, t, C["s11.a"], [("compare", "i", 80, CLARO), ("a", "i", 80, CLARO), ("inclinação", "g", 76, BR)], XE, 330)
        conta_em(c, t, C["s11.b"], [("f{4}{2} = 2", BR)], XE, 500, 88)
        conta_em(c, t, C["s11.c"], [("f{3}{1} = 3", BR)], XE + 400, 500, 88)
        E.frase(c, t, C["s11.d"], [("2", "g", 76, BR), ("≠", "g", 76, ERRADO), ("3:", "g", 76, BR), ("faz", "i", 80, CLARO), ("curva", "g", 76, BR)], XE, 700)
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.a"], ps("numa reta, a inclinação", "i", 64, CLARO), XE, 300, passo=0.1)
    E.frase(c, t, C["s12.a"] + 1.2, [("é", "i", 64, CLARO), ("a", "i", 64, CLARO), ("mesma", "g", 64, BR), ("em", "i", 64, CLARO), ("todo", "i", 64, CLARO),
                                    ("trecho", "i", 64, CLARO)], XE, 390, passo=0.1)
    E.frase(c, t, C["s12.b"], [("não", "g", 64, ERRADO), ("compensa:", "i", 64, CLARO)], XE, 580)
    E.frase(c, t, C["s12.b"] + 0.8, ps("pediu o determinante", "i", 60, CLARO), XE, 680, passo=0.1)
    E.frase(c, t, C["s12.b"] + 2.6, ps("ou tem letra no meio", "i", 60, CLARO), XE, 780, passo=0.1)


# ---------------- situação 3: duas circunferências ----------------
def desenho3(c, t, t0, tr=None):
    plano(c, t, t0, PC, [5, 10, 15], [5, 10, 15], 32)
    elipse(c, t, t0 + 0.4, PC, 1, 2, 2, 2, 0.8)
    elipse(c, t, t0 + 0.8, PC, 7, 10, 8, 8, 1.0, cor=TINTA)
    E.ponto(c, t, t0 + 0.6, PC, 1, 2, None, cor=COR, r=10)
    E.ponto(c, t, t0 + 1.0, PC, 7, 10, None, cor=TINTA, r=10)
    if tr is not None and t >= tr:
        seg(c, t, tr, PC(1, 2), PC(7, 10), C_, 0.7, 6)
        E.foco(c, t, tr + 0.5, 0.4, lambda a: E._meio(c, "10", *PC(5.6, 5.4), 44, "g", C_, a))


def b_questao3(c, t, C, b):
    desenho3(c, t, C["s13.a"])
    titulo(c, t, C["s13"], 3)
    E.formula_em(c, t, C["s13.a"], "(x − 1)^2 + (y − 2)^2 = 4", XE, 360, 64)
    E.formula_em(c, t, C["s13.b"], "(x − 7)^2 + (y − 10)^2 = 64", XE, 500, 64)
    E.frase(c, t, C["s13.c"], [("qual", "i", 74), ("a", "i", 74), ("posição?", "g", 74, COR)], XE, 680)
    if t >= C["s14"]:
        pausa(c, t, C["s14.a"], 560, 850, 70)


def b_resposta3(c, t, C, b):
    desenho3(c, t, C["s15"] - 3, C["s16.b"])
    if t >= C["s16.d"]:
        tp = PC(1 + 0.6 * 2, 2 + 0.8 * 2)
        E.foco(c, t, C["s16.d"], 0.4, lambda a: c.drawCircle(*tp, 16, M.paint(CERTO, a)))
    titulo(c, t, C["s15"], 3)
    conta_em(c, t, C["s15.a"], [("centros: ", TINTA), ("(1, 2)", COR)], XE, 330, 60)
    conta_em(c, t, C["s15.b"], [("e ", TINTA), ("(7, 10)", TINTA)], XE + 480, 330, 60)
    conta_em(c, t, C["s15.c"], [("raios: ", TINTA), ("2", COR), (" e 8", TINTA)], XE, 440, 60)
    conta_em(c, t, C["s16.a"], [("dist.: r{6^2 + 8^2} = ", TINTA)], XE, 590, 60)
    conta_em(c, t, C["s16.b"], [("10", C_)], XE + conta(None, [("dist.: r{6^2 + 8^2} = ", TINTA)], 0, 0, 60, 0) + 10, 590, 66)
    conta_em(c, t, C["s16.c"], [("2 + 8 = 10", TINTA)], XE, 720, 66)
    E.foco(c, t, C["s16.d"], 0.5, lambda a: E.pilula(c, "tangentes externas", XE + 330, 860, 54, "g", fundo=CERTO, a=a))


# ---------------- situação 4: elipse ----------------
def desenho4(c, t, t0, focos=None, soma=None):
    plano(c, t, t0, PE4, [-10, 10], [-6, 6], 32)
    elipse(c, t, t0 + 0.3, PE4, 0, 0, 10, 6, 1.0)
    if focos is not None:
        for i, x_ in enumerate((-8, 8)):
            foco_pt(c, t, focos + 0.2 * i, PE4, x_, 0, "F", (0, -1))
    if soma is not None and t >= soma:
        th = 1.1
        X = PE4(10 * math.cos(th), 6 * math.sin(th))
        seg(c, t, soma, PE4(-8, 0), X, B_, 0.5, 6)
        seg(c, t, soma + 0.3, PE4(8, 0), X, C_, 0.5, 6)


def b_questao4(c, t, C, b):
    desenho4(c, t, C["s17.a"])
    titulo(c, t, C["s17"], 4)
    E.formula_em(c, t, C["s17.a"], "f{x^2}{100} + f{y^2}{36} = 1", XE, 360, 84)
    E.frase(c, t, C["s17.b"], [("focos?", "g", 70, COR)], XE, 540)
    E.frase(c, t, C["s17.c"], [("soma", "g", 70), ("das", "i", 74), ("distâncias?", "i", 74)], XE, 660)
    if t >= C["s18"]:
        pausa(c, t, C["s18.a"], 430, 830, 70)


def b_resposta4(c, t, C, b):
    desenho4(c, t, C["s19"] - 3, C["s19.d"], C["s20.a"])
    seg(c, t, C["s19.a"], PE4(0, 0), PE4(10, 0), A_, 0.5, 8)
    seg(c, t, C["s19.b"], PE4(0, 0), PE4(0, 6), B_, 0.5, 8)
    titulo(c, t, C["s19"], 4)

    def s19():
        conta_em(c, t, C["s19.a"], [("a = ", TINTA), ("10", A_)], XE, 330, 70)
        conta_em(c, t, C["s19.b"], [("b = ", TINTA), ("6", B_)], XE, 450, 70)
        conta_em(c, t, C["s19.c"], [("c^2 = 100 − 36 = 64", TINTA)], XE, 570, 66)
        conta_em(c, t, C["s19.d"], [("focos: ", TINTA), ("(±8, 0)", C_)], XE, 690, 66)
    s19()
    E.foco(c, t, C["s20.b"], 0.4, lambda a: E.formula(c, "soma = 2a = 2 · 10", XE, 860, 62, "g", TINTA, a))
    bola_txt(c, t, C["s20.c"], "20", XE + 640, 835, 70, 64)


# ---------------- situação 5: parábola e hipérbole ----------------
PP = E.Plano(170, 470, 680, 530, -7, 7, -4, 6.9)       # parábola x² = 12y (48,6 px por unidade)
PH = E.Plano(1110, 470, 700, 530, -7.2, 7.2, -5.45, 5.45)  # hipérbole y²/9 − x²/16 = 1 (48,6 px por unidade)


def parabola(c, t, t0, P, d=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0:
        xs = [-7 + 14 * i / 120 for i in range(121)]
        pts = [P(x, x * x / 12) for x in xs if x * x / 12 <= P.ymax]
        n = max(2, int(len(pts) * p))
        meio = len(pts) // 2
        lo, hi = max(0, meio - n // 2), min(len(pts), meio + n // 2 + 1)
        caminho(c, pts[lo:hi], COR, 7)


def b_questao5(c, t, C, b):
    E.frase(c, t, C["s21"], [("última", "i", 66, COR), ("situação", "i", 66, COR)], XE, 190)
    E.frase(c, t, C["s21"] + 0.8, [("que", "i", 66), ("cônica?", "g", 66), ("e", "i", 66), ("o", "i", 66), ("foco?", "g", 66, COR)], XE, 300)
    E.formula_em(c, t, C["s21.a"], "x^2 = 12y", 510, 560, 96, align="center")
    E.formula_em(c, t, C["s21.b"], "f{y^2}{9} − f{x^2}{16} = 1", 1460, 560, 96, align="center")
    if t >= C["s22"]:
        pausa(c, t, C["s22.a"], W / 2, 800, 110)


def b_resposta5(c, t, C, b):
    E.formula_em(c, t, C["s23"], "x^2 = 12y", 510, 200, 76, align="center")
    E.formula_em(c, t, C["s23"], "f{y^2}{9} − f{x^2}{16} = 1", 1460, 200, 76, align="center")
    plano(c, t, C["s23"], PP, [], [3], 30)
    parabola(c, t, C["s23.a"], PP)
    E.foco(c, t, C["s23.a"], 0.4, lambda a: E.pilula(c, "parábola", 510, 300, 48, "g", fundo=CERTO, a=a))
    conta_em(c, t, C["s23.b"], [("f{8}{4} = 2   →   ", TINTA2)], 220, 420, 50)
    conta_em(c, t, C["s23.c"], [("f{12}{4} = 3", COR)], 220 + conta(None, [("f{8}{4} = 2   →   ", TINTA2)], 0, 0, 50, 0), 420, 50)
    foco_pt(c, t, C["s23.d"], PP, 0, 3, "F (0, 3)", (1, 0))
    if t >= C["s23.e"]:
        q = ep(t, C["s23.e"], 0.5)
        M.line(c, PP.x(-7), PP.y(-3), PP.x(-7) + 760 * q, PP.y(-3), TINTA, 1.0, 5, dash=E.TRACO)
        E.foco(c, t, C["s23.e"] + 0.3, 0.4, lambda a: E.escreve(c, "y = −3", PP.x(3.2), PP.y(-3) - 16, 44, "g", TINTA, a))
    if t >= C["s24"]:
        plano(c, t, C["s24"], PH, [], [-5, 5], 30)
        k = PH.x(1) - PH.x(0)
        hip_px(c, PH.x(0), PH.y(0), 3 * k, 4 * k, 7.2 * k, 5.45 * k, ease_io(prog(t, C["s24.b"], 1.0)), COR, 7, vertical=True)
        E.foco(c, t, C["s24.a"], 0.4, lambda a: E.pilula(c, "hipérbole", 1460, 300, 48, "g", fundo=CERTO, a=a))
        conta_em(c, t, C["s24.c"], [("c^2 = 9 + 16 = 25", TINTA)], 1460, 420, 50, "center")
        for i, y_ in enumerate((-5, 5)):
            foco_pt(c, t, C["s24.d"] + 0.2 * i, PH, 0, y_, "F", (1, 0))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s25"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s25.a", [("distâncias:", "g", 66), ("Pitágoras", "i", 70), ("e", "i", 70), ("ponto–reta", "i", 70)]),
                 ("s25.b", [("circunferências:", "g", 66), ("centros", "i", 70), ("e", "i", 70), ("raios", "i", 70)]),
                 ("s25.c", [("cônicas:", "g", 66, COR), ("sinais", "i", 70), ("e", "i", 70), ("a", "i", 70), ("conta", "i", 70), ("do", "i", 70), ("c", "g", 66, C_)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 340, y, passo=0.12)
    E.saida(c, t, C["s26"] - 0.1, resumo)
    if t < C["s26"]:
        return
    E.frase(c, t, C["s26"], ps("próxima aula: assunto novo", "i", 72), XE, 290, passo=0.12)
    E.frase(c, t, C["s26.a"], [("Bases", "g", 150, COR), ("de", "i", 130), ("contagem", "g", 150, COR)], XE, 470)
    E.frase(c, t, C["s26.b"], [("binária", "g", 80), ("e", "i", 80), ("sexagesimal", "g", 80)], XE, 600)
    E.foco(c, t, C["s26.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 760, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s26.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(960, 785, p), ep(t, C["s26.c"] + 0.2, 0.4))
    E.frase(c, t, C["s26.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920 + 40, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              atalho=b_atalho, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
