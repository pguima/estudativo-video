"""Visual — Estudativo · MAT-TOP-011: elipse, equação reduzida, semieixos e focos.

Linguagem das cônicas (TOP-011, 012 e 013 copiam daqui): plano na metade direita, texto na esquerda; a curva em índigo;
focos como pontos em tinta com "F"; o barbante em cinza-escuro. Semieixos com cor fixa:
    A_ = índigo da matéria   o á (semieixo maior; na elipse, a hipotenusa)
    B_ = âmbar  #D98A00      o bê
    C_ = petróleo #0E9AA7    o cê (do centro até o foco)
Erro em vermelho, certo em verde, atalho no palco escuro. A figura não mente: escala igual nos dois eixos.
Peças locais: elipse() (curva que se fecha), barbante(), foco_pt(), seg() (lado colorido que cresce), conta() e conta_em()."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-011_elipse_equacao_reduzida.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("barbante", "equacao", "focos", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
A_, B_, C_ = E.COR, "#D98A00", "#0E9AA7"
C_ESC = "#3CC7D3"
assert 9 + 1 == 10 and math.hypot(4, 3) == 5 and 25 == 9 + 16 and 25 + 9 == 34 and math.sqrt(34) > 5
assert 25 - 16 == 9 and 225 / 9 == 25 and 225 / 25 == 9

P1 = E.Plano(960, 240, 840, 600, -7, 7, -5, 5)      # elipse deitada a = 5, b = 3 (60 px por unidade)
P2 = E.Plano(1140, 180, 660, 720, -5.5, 5.5, -6, 6)  # elipse em pé (60 px por unidade)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def plano(c, t, t0, P, mx=None, my=None, size=36):
    return E.plano(c, t, t0, *P.caixa, P.xmin, P.xmax, P.ymin, P.ymax, marcas_x=mx if mx is not None else [],
                   marcas_y=my if my is not None else [], size=size)


def elipse_px(c, cx, cy, rx, ry, p=1.0, cor=None, largura=8, a=1.0, ini=0.0):
    """elipse em pixels que se fecha de 0 até p (a partir do ângulo ini, em graus, sentido anti-horário na tela)"""
    if p <= 0 or a <= 0:
        return
    n = max(2, int(220 * p))
    path = skia.Path()
    for i in range(n + 1):
        th = math.radians(ini) + 2 * math.pi * p * i / n
        x, y = cx + rx * math.cos(th), cy - ry * math.sin(th)
        path.moveTo(x, y) if i == 0 else path.lineTo(x, y)
    c.drawPath(path, M.paint(cor or COR, a, stroke=largura, cap_round=True))


def elipse(c, t, t0, P, a, b, d=1.2, cor=None, largura=8, alfa=1.0, ini=0.0):
    p = ease_io(prog(t, t0, d))
    elipse_px(c, P.x(0), P.y(0), a * (P.x(1) - P.x(0)), b * (P.y(0) - P.y(1)), p, cor, largura, alfa, ini)


def no_elipse(P, a, b, th):
    return P(a * math.cos(th), b * math.sin(th))


def foco_pt(c, t, t0, P, x, y, nome="F", lado=(0, 1), cor=TINTA, size=44):
    E.ponto(c, t, t0, P, x, y, None, cor=cor, r=14)
    if nome:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E._cola(c, nome, *P(x, y), lado[0], lado[1], 22, size, "b", cor, a))


def barbante(c, F1, F2, X, a=1.0, cor=TINTA2, largura=4):
    if a > 0:
        M.line(c, *F1, *X, cor, a, largura)
        M.line(c, *X, *F2, cor, a, largura)


def seg(c, t, t0, A, B, cor, d=0.6, largura=9, a=1.0, tracejado=False):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *A, *B, cor, a, largura, progress=p, dash=E.TRACO if tracejado else None)


def rot(c, t, t0, s, X, Y, nx, ny, cor, size=50, gap=16):
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, s, X, Y, nx, ny, gap, size, "g", cor, a))


def conta(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """conta numa linha com partes coloridas: partes = [(escrita de fórmula, cor)]. Devolve a largura"""
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


EQ = "f{x^2}{25} + f{y^2}{9} = 1"


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        E.formula_em(c, t, C["s01.a"], EQ, W / 2, 330, 120, align="center")
        cx, cy, rx, ry = 960, 700, 300, 180
        p = ease_io(prog(t, C["s01.b"], 1.2))
        elipse_px(c, cx, cy, rx, ry, p, COR, 10)
        E.frase(c, t, C["s01.b"] + 0.4, [("um", "i", 64), ("círculo", "i", 64), ("achatado", "g", 60, COR)], W / 2, 980, "center")
        if t >= C["s01.c"]:
            q = ep(t, C["s01.c"], 0.5)
            M.arrow(c, cx - rx, cy, cx + rx, cy, B_, q, 6, 20, q)
            M.arrow(c, cx + rx, cy, cx - rx, cy, B_, q, 6, 20, q)
            E.foco(c, t, C["s01.c"] + 0.3, 0.4, lambda a: E.escreve(c, "largura", cx + rx + 30, cy + 16, 50, "i", B_, a))
            q2 = ep(t, C["s01.c"] + 0.8, 0.5)
            M.arrow(c, cx, cy + ry, cx, cy - ry, C_, q2, 6, 20, q2)
            M.arrow(c, cx, cy - ry, cx, cy + ry, C_, q2, 6, 20, q2)
            E.foco(c, t, C["s01.c"] + 1.1, 0.4, lambda a: E.escreve(c, "altura", cx + 20, cy - ry - 26, 50, "i", C_, a))
        for i, dx in enumerate((-240, 240)):
            k = ease_back(prog(t, C["s01.d"] + 0.15 * i, 0.45))
            if k > 0:
                c.drawCircle(cx + dx, cy, 16 * k, M.paint(TINTA))
        E.foco(c, t, C["s01.d"] + 0.4, 0.4, lambda a: (E.centro(c, "foco", cx - 240, cy + 70, 46, "b", TINTA, a),
                                                      E.centro(c, "foco", cx + 240, cy + 70, 46, "b", TINTA, a)))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 1.0, [("semieixos", "g", 130)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.6, [("e", "i", 110), ("focos", "g", 130, COR)], XE, 630)
        E.frase(c, t, C["s02.a"] + 2.2, [("da", "i", 96), ("elipse", "i", 96, COR)], XE, 760)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("duas", "g", 80, COR, C["s03.a"]), ("coisas", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 190, "center")
    x, w = 200, 1520
    for k, y in (("s03.b", 280), ("s03.c", 600)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 270, p, prog_=p)
    k = C["s03.b"]
    elipse_px(c, 400, 415, 100, 100, ease_io(prog(t, k + 0.3, 0.9)), COR, 8)
    E.foco(c, t, k + 0.3, 0.4, lambda a: (c.drawCircle(400, 415, 9, M.paint(TINTA, a)), M.line(c, 400, 415, 500, 415, B_, a, 6)))
    E.foco(c, t, k + 0.8, 0.4, lambda a: E.escreve(c, "5", 438, 400, 44, "g", B_, a))
    E.frase(c, t, k, [("circunferência", "g", 64, COR)], 600, 380)
    conta_em(c, t, k + 1.6, [("x^2 + y^2 = 25", TINTA)], 600, 490, 74)
    k = C["s03.c"]
    # parábola: foco e diretriz, mesma distância
    cx, cy, s = 400, 755, 22  # x² = 8y: foco (0, 2), diretriz y = −2; (cx, cy) = foco
    f = lambda u: (cx + u * s, cy + 2 * s - (u * u / 8) * s)
    if t >= k:
        pts = [f(-5.5 + 11 * i / 60) for i in range(61)]
        q = ease_io(prog(t, k + 0.2, 0.9))
        n = max(2, int(60 * q))
        path = skia.Path(); path.moveTo(*pts[0])
        for P_ in pts[1:n + 1]:
            path.lineTo(*P_)
        c.drawPath(path, M.paint(COR, 1, stroke=7, cap_round=True))
        a = ep(t, k + 0.8, 0.4)
        M.line(c, cx - 140, cy + 4 * s, cx + 140, cy + 4 * s, TINTA, a, 5)
        c.drawCircle(cx, cy, 10, M.paint(TINTA, a))
        X = f(2.8)
        q2 = ep(t, k + 1.4, 0.5)
        M.line(c, *X, cx, cy, B_, q2, 5)
        M.line(c, X[0], X[1], X[0], cy + 4 * s, B_, q2, 5, dash=E.TRACO)
    E.frase(c, t, k, [("parábola:", "g", 64, COR)], 600, 700)
    E.frase(c, t, k + 1.4, ps("mesma distância do", "i", 60) + [("foco", "g", 58)] + ps("e da", "i", 60) + [("diretriz", "g", 58)], 600, 800, passo=0.12)
    E.frase(c, t, C["s04"] - 2.4, ps("faltou alguma? procure no canal", "i", 50, TINTA2), W / 2, 975, "center", passo=0.1)


# ---------------- o barbante ----------------
F1, F2 = (-4, 0), (4, 0)


def b_barbante(c, t, C, b):
    plano(c, t, C["s04"], P1, [-5, -4, 4, 5], [-3, 3], 34)
    foco_pt(c, t, C["s04.a"], P1, *F1, None)
    foco_pt(c, t, C["s04.a"] + 0.2, P1, *F2, None)
    if t >= C["s05.a"]:
        for x_ in (-4, 4):
            E.saida(c, t, C["s06"], lambda x_=x_: E.foco(c, t, C["s05.a"], 0.4, lambda a: E._cola(c, "F", *P1(x_, 0), 0, -1, 22, 44, "b", TINTA, a)))
    # o lápis dá a volta (s04.b) e depois para nos pontos que conferem (s06)
    p = ease_io(prog(t, C["s04.b"], 3.0))
    elipse(c, t, C["s04.b"], P1, 5, 3, 3.0, ini=math.degrees(0.9))
    if t < C["s06.b"]:
        th = 0.9 + 2 * math.pi * p
        X = no_elipse(P1, 5, 3, th)
        q = ep(t, C["s04.a"] + 0.4, 0.5)
        barbante(c, P1(*F1), P1(*F2), X, q)
        if q > 0:
            c.drawCircle(*X, 13, M.paint(COR, q))
    if C["s05.b"] <= t < C["s06"]:
        X = no_elipse(P1, 5, 3, 0.9)
        seg(c, t, C["s05.b"], P1(*F1), X, B_, 0.5, 8)
        seg(c, t, C["s05.b"] + 0.6, X, P1(*F2), C_, 0.5, 8)
    # s06: os dois pontos que conferem
    def pt50():
        V = P1(5, 0)
        seg(c, t, C["s06.b"] + 0.4, P1(*F1), (V[0], V[1] - 8), B_, 0.6, 8)
        seg(c, t, C["s06.b"] + 1.0, P1(*F2), (V[0], V[1] + 8), C_, 0.4, 8)
        E.ponto(c, t, C["s06.b"], P1, 5, 0, None, cor=COR, r=14)
        rot(c, t, C["s06.b"] + 1.0, "9", *P1(0.5, 0), 0, 1, B_, 48)
        rot(c, t, C["s06.b"] + 1.4, "1", *P1(4.5, 0), 0, -1, C_, 48)
    if t >= C["s06.b"]:
        E.saida(c, t, C["s06.d"] - 0.1, pt50)
    if t >= C["s06.d"]:
        T = P1(0, 3)
        seg(c, t, C["s06.d"] + 0.3, P1(*F1), T, B_, 0.5, 8)
        seg(c, t, C["s06.d"] + 0.6, T, P1(*F2), C_, 0.5, 8)
        seg(c, t, C["s06.d"] + 0.9, T, P1(0, 0), TINTA2, 0.4, 4, tracejado=True)
        E.ponto(c, t, C["s06.d"], P1, 0, 3, None, cor=COR, r=14)
        rot(c, t, C["s06.d"] + 1.0, "3", *P1(0, 1.5), 1, 0, TINTA2, 44)
        rot(c, t, C["s06.d"] + 1.0, "4", *P1(2, 0), 0, 1, TINTA2, 44)
        rot(c, t, C["s06.e"], "5", *P1(-2, 1.5), -1, -1, B_, 52)
        rot(c, t, C["s06.e"] + 0.2, "5", *P1(2, 1.5), 1, -1, C_, 52)

    def s04():
        E.frase(c, t, C["s04.a"], [("2", "g", 90, COR), ("pregos", "i", 90)], XE, 330)
        E.frase(c, t, C["s04.a"] + 0.8, [("1", "g", 90, COR), ("barbante", "i", 90)], XE, 460)
        E.frase(c, t, C["s04.b"], ps("dê a volta", "i", 80, TINTA2), XE, 600)
        E.frase(c, t, C["s04.c"], [("uma", "i", 110), ("elipse", "g", 110, COR)], XE, 780)
    E.saida(c, t, C["s05"] - 0.1, s04)

    def s05():
        E.frase(c, t, C["s05.a"], [("pregos", "i", 80), ("=", "i", 80), ("focos", "g", 80)], XE, 300)
        E.foco(c, t, C["s05.b"], 0.5, lambda a: conta(c, [("dist. 1", B_), (" + ", TINTA), ("dist. 2", C_)], XE, 470, 70, a))
        E.frase(c, t, C["s05.c"], [("=", "g", 70), ("sempre", "i", 80), ("igual", "g", 76, COR)], XE, 580)
        E.frase(c, t, C["s05.d"] - 2.6, ps("parábola: distâncias iguais", "i", 54, TINTA2), XE, 730, passo=0.1)
        E.frase(c, t, C["s05.d"], [("elipse:", "g", 64, COR), ("soma", "g", 64), ("fixa", "i", 70)], XE, 840)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], ps("focos em −4 e 4", "i", 66), XE, 290, passo=0.12)
    E.frase(c, t, C["s06"] + 1.6, [("barbante", "i", 66), ("=", "i", 66), ("10", "g", 66, COR)], XE, 380)
    conta_em(c, t, C["s06.b"], [("(5, 0):", TINTA2)], XE, 530, 60)
    conta_em(c, t, C["s06.c"], [("9", B_), (" + ", TINTA), ("1", C_), (" = 10", TINTA)], XE + 40, 630, 84)
    conta_em(c, t, C["s06.d"], [("(0, 3):", TINTA2)], XE, 780, 60)
    conta_em(c, t, C["s06.e"] + 0.6, [("5", B_), (" + ", TINTA), ("5", C_), (" = 10", TINTA)], XE + 40, 880, 84)


# ---------------- a equação ----------------
def b_equacao(c, t, C, b):
    plano(c, t, C["s07"], P1, [], [], 34)
    elipse(c, t, C["s07"] + 0.2, P1, 5, 3, 1.0)
    seg(c, t, C["s07.c"], P1(0, 0), P1(5, 0), A_, 0.6, 10)
    rot(c, t, C["s07.c"] + 0.4, "a" if t < C["s08.a"] else "a = 5", *P1(2.5, 0), 0, -1, A_, 50)
    seg(c, t, C["s07.d"], P1(0, 0), P1(0, 3), B_, 0.6, 10)
    rot(c, t, C["s07.d"] + 0.4, "b" if t < C["s08.b"] else "b = 3", *P1(0, 1.5), -1, 0, B_, 50)
    # marcas dos cortes
    for k, vals, eixo in (("s08.c", (-5, 5), "x"), ("s08.d", (-3, 3), "y")):
        for i, v in enumerate(vals):
            X, Y = (P1.x(v), P1.oy) if eixo == "x" else (P1.ox, P1.y(v))
            k_ = ease_back(prog(t, C[k] + 0.2 * i, 0.4))
            if k_ > 0:
                c.drawCircle(X, Y, 13 * k_, M.paint(TINTA))
            nx, ny = ((0, 1) if eixo == "x" else (1, 0)) if v > 0 else ((0, 1) if eixo == "x" else (1, 0))
            if eixo == "x":
                E.foco(c, t, C[k] + 0.2 * i, 0.4, lambda a, X=X, Y=Y, v=v: E._cola(c, E._num(v), X + (22 if v > 0 else -22), Y, 0, 1, 14, 44, "b", TINTA, a))
            else:
                E.foco(c, t, C[k] + 0.2 * i, 0.4, lambda a, X=X, Y=Y, v=v: E._cola(c, E._num(v), X, Y, -1, 0, 20, 44, "b", TINTA, a))
    if t >= C["s08.e"]:
        q = ep(t, C["s08.e"], 0.5)
        y0 = P1.y(-3) + 70
        M.line(c, P1.x(-5), y0, P1.x(5), y0, COR, q, 5)
        for x_ in (-5, 5):
            M.line(c, P1.x(x_), y0 - 14, P1.x(x_), y0 + 14, COR, q, 5)
        E.foco(c, t, C["s08.e"] + 0.2, 0.4, lambda a: E.pilula(c, "10 = barbante", P1.x(0), y0 + 50, 40, "g", a=a))

    def s07():
        E.frase(c, t, C["s07"], ps("equação reduzida", "i", 66, TINTA2), XE, 250)
        E.formula_em(c, t, C["s07.a"], "f{x^2}{a^2} + f{y^2}{b^2} = 1", XE, 450, 110)
        E.frase(c, t, C["s07.b"], [("a", "g", 70, A_), ("e", "i", 70), ("b", "g", 70, B_), ("=", "i", 70), ("semieixos", "g", 70)], XE, 660)
        E.frase(c, t, C["s07.b"] + 1.2, ps("do centro até a borda", "i", 60, TINTA2), XE, 760, passo=0.12)
    E.saida(c, t, C["s08"] - 0.1, s07)

    def s08():
        E.formula_em(c, t, C["s08"], EQ, XE, 360, 110)
        conta_em(c, t, C["s08.a"], [("a^2 = 25  →  a = ", TINTA), ("5", A_)], XE, 560, 72)
        conta_em(c, t, C["s08.b"], [("b^2 = 9  →  b = ", TINTA), ("3", B_)], XE, 680, 72)
        E.frase(c, t, C["s08.e"], [("largura", "i", 64), ("10,", "g", 64, COR), ("altura", "i", 64), ("6", "g", 64, COR)], XE, 860)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"], [("por", "i", 80), ("que", "i", 80), ("5?", "g", 80, COR)], XE, 270)
    E.frase(c, t, C["s09.a"], [("no", "i", 64), ("eixo", "i", 64), ("x,", "g", 64), ("y = 0", "g", 64, COR)], XE, 400)
    conta_em(c, t, C["s09.a"] + 1.2, [("f{x^2}{25} + 0 = 1", TINTA)], XE, 560, 84)
    conta_em(c, t, C["s09.b"], [("x^2 = 25", TINTA)], XE, 720, 84)
    conta_em(c, t, C["s09.b"] + 1.4, [("x = 5  ou  x = −5", COR)], XE, 860, 76)


# ---------------- os focos ----------------
def b_focos(c, t, C, b):
    plano(c, t, C["s10"], P1, [-5, 5], [], 34)
    elipse(c, t, C["s10"] + 0.1, P1, 5, 3, 0.9)
    foco_pt(c, t, C["s10"] + 0.3, P1, *F1, "F" if t < C["s12.d"] else None, (0, 1))
    foco_pt(c, t, C["s10"] + 0.4, P1, *F2, "F" if t < C["s12.d"] else None, (0, 1))
    T = P1(0, 3)
    E.ponto(c, t, C["s10.a"], P1, 0, 3, None, cor=COR, r=14)
    a_s = 1 - ep(t, C["s11.a"], 0.4)
    seg(c, t, C["s10.b"], P1(*F1), T, TINTA2, 0.5, 6, a_s)
    seg(c, t, C["s10.b"], P1(*F2), T, TINTA2, 0.5, 6)
    E.saida(c, t, C["s11.a"], lambda: (rot(c, t, C["s10.c"] + 0.4, "5", *P1(-2, 1.5), -1, -1, TINTA2, 50),
                                       rot(c, t, C["s10.c"] + 0.4, "5", *P1(2, 1.5), 1, -1, TINTA2, 50)))
    # o triângulo: centro, (0, 3) e o foco (4, 0)
    if t >= C["s11.a"]:
        q = ep(t, C["s11.a"], 0.5)
        path = skia.Path(); path.addPoly([P1(0, 0), T, P1(4, 0)], True)
        c.drawPath(path, M.paint(COR, 0.10 * q))
        E.angulo(c, t, C["s11.a"] + 0.3, P1(0, 0), T, P1(4, 0), r=44, cor=TINTA, preenche=0.12)
    seg(c, t, C["s11.b"], P1(0, 0), T, B_, 0.6, 10)
    rot(c, t, C["s11.b"] + 0.4, "b = 3", *P1(0, 1.5), -1, 0, B_, 46)
    seg(c, t, C["s11.c"], P1(0, 0), P1(4, 0), C_, 0.6, 10)
    rot(c, t, C["s11.c"] + 0.4, "c" if t < C["s12.c"] else "c = 4", *P1(2, 0), 0, 1, C_, 48)
    seg(c, t, C["s11.d"], P1(4, 0), T, A_, 0.6, 10)
    E.foco(c, t, C["s11.d"] + 0.4, 0.4, lambda a: E._meio(c, "a = 5", *P1(3.9, 3.0), 48, "g", A_, a))
    if t >= C["s12.d"]:
        for x_, s in ((-4, "(−4, 0)"), (4, "(4, 0)")):
            E.foco(c, t, C["s12.d"], 0.4, lambda a, x_=x_, s=s: E.pilula(c, s, P1.x(x_), P1.y(-3) + 60, 40, "g", fundo=C_, a=a))

    def s10_11():
        E.frase(c, t, C["s10"], [("e", "i", 84), ("os", "i", 84), ("focos?", "g", 84, COR)], XE, 280)
        E.frase(c, t, C["s10.b"], ps("no meio entre os focos:", "i", 58, TINTA2), XE, 420, passo=0.12)
        E.frase(c, t, C["s10.c"], [("metade", "i", 68), ("de", "i", 68), ("10", "g", 68), ("=", "i", 68), ("5", "g", 68, A_)], XE, 520)
        E.frase(c, t, C["s11.a"], [("triângulo", "g", 70), ("retângulo", "i", 70)], XE, 660)
        E.frase(c, t, C["s11.b"], [("catetos:", "i", 60), ("b", "g", 64, B_), ("e", "i", 60), ("c", "g", 64, C_)], XE, 770)
        E.frase(c, t, C["s11.d"], [("hipotenusa:", "i", 60), ("a", "g", 64, A_)], XE, 870)
    E.saida(c, t, C["s12"] - 0.1, s10_11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"], [("Pitágoras", "g", 76, COR)], XE, 280)
    conta_em(c, t, C["s12.a"], [("a", A_), ("^2 = ", TINTA), ("b", B_), ("^2 + ", TINTA), ("c", C_), ("^2", TINTA)], XE, 420, 84)
    conta_em(c, t, C["s12.b"], [("25 = 9 + ", TINTA), ("c", C_), ("^2", TINTA)], XE, 550, 84)
    conta_em(c, t, C["s12.c"], [("c", C_), ("^2 = 16  →  ", TINTA), ("c = 4", C_)], XE, 680, 84)
    E.frase(c, t, C["s12.d"], [("focos:", "i", 64), ("(±4,", "g", 64, C_), ("0)", "g", 64, C_)], XE, 840)


# ---------------- elipse em pé ----------------
def b_empe(c, t, C, b):
    plano(c, t, C["s13"], P2, [-3, 3], [-5, 5], 34)
    elipse(c, t, C["s13.b"], P2, 3, 5, 1.0)
    seg(c, t, C["s13.c"], P2(0, 0), P2(0, 5), A_, 0.6, 10)
    rot(c, t, C["s13.c"] + 0.4, "a = 5", *P2(0, 2.5), 1, 0, A_, 46)
    for i, y_ in enumerate((-4, 4)):
        foco_pt(c, t, C["s13.d"] + 0.2 * i, P2, 0, y_, "F", (-1, 0))
    w = E.frase(c, t, C["s13"], ps("número maior embaixo do", "i", 62), XE, 260, passo=0.12)
    E.frase(c, t, C["s13"] + 1.6, [("y?", "g", 70, COR)], XE + w + 18, 260)
    E.formula_em(c, t, C["s13.a"], "f{x^2}{9} + f{y^2}{25} = 1", XE, 450, 100)
    if t >= C["s13.a"] + 1.2:
        q = ep(t, C["s13.a"] + 1.2, 0.4)
        wx = E.formula(None, "f{x^2}{9} + ", 0, 0, 100, a=0)
        wy = E.formula(None, "f{y^2}{25}", 0, 0, 100, a=0)
        M.rrect(c, XE + wx - 14, 300, wy + 28, 210, 24, A_, 0.12 * q)
    E.frase(c, t, C["s13.b"], [("em", "i", 90), ("pé", "g", 90, COR)], XE, 640)
    E.frase(c, t, C["s13.c"], [("a", "g", 64, A_), ("=", "i", 64), ("5,", "g", 64, A_), ("na", "i", 64), ("vertical", "g", 64)], XE, 770)
    E.frase(c, t, C["s13.d"], [("focos:", "i", 64), ("(0,", "g", 64, C_), ("±4)", "g", 64, C_)], XE, 880)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano(c, t, C["s14"], P1, [-5, 5], [], 34)
    elipse(c, t, C["s14"] + 0.1, P1, 5, 3, 0.8)
    r34 = math.sqrt(34)
    if C["s14.c"] <= t < C["s15"]:
        for x_ in (-r34, r34):
            E.ponto(c, t, C["s14.c"] + 0.3, P1, x_, 0, None, cor=ERRADO, r=14)
        E.foco(c, t, C["s14.c"] + 0.6, 0.4, lambda a: E.pilula(c, "foco fora?", P1.x(r34) - 20, P1.y(1.3), 40, "g", fundo=ERRADO, a=a))
    if t >= C["s15"]:
        for x_ in (-4, 4):
            foco_pt(c, t, C["s15.a"], P1, x_, 0, "F", (0, -1), CERTO)
        seg(c, t, C["s15.b"], P1(0, 0), P1(4, 0), C_, 0.5, 10)
        rot(c, t, C["s15.b"] + 0.3, "c = 4", *P1(2, 0), 0, -1, C_, 44)
        seg(c, t, C["s15.b"] + 0.6, P1(0, -0.7), P1(5, -0.7), A_, 0.5, 6)
        rot(c, t, C["s15.b"] + 0.9, "a = 5", *P1(2.5, -0.7), 0, 1, A_, 44)

    def s14():
        E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 260)
        E.frase(c, t, C["s14.a"], [("a", "g", 70, A_), ("como", "i", 70), ("cateto?", "g", 70, ERRADO)], XE, 400)
        conta_em(c, t, C["s14.b"], [("c^2 = 25 + 9 = 34", ERRADO)], XE, 560, 80)
        conta_em(c, t, C["s14.c"], [("r{34} ≈ 5,8 > 5", ERRADO)], XE, 700, 80)
        E.frase(c, t, C["s14.c"] + 1.0, ps("foco fora da elipse", "i", 60, TINTA2), XE, 820)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], ps("os pregos ficam", "i", 70), XE, 280)
    E.frase(c, t, C["s15.a"] + 0.8, [("dentro", "g", 80, CERTO)], XE, 390)
    conta_em(c, t, C["s15.c"], [("c", C_), (" < ", TINTA), ("a", A_)], XE, 580, 120)
    E.frase(c, t, C["s15.d"], [("hipotenusa", "i", 66), ("=", "i", 66), ("a", "g", 70, A_)], XE, 780)
    conta_em(c, t, C["s15.d"] + 1.0, [("a", A_), ("^2 = ", TINTA), ("b", B_), ("^2 + ", TINTA), ("c", C_), ("^2", TINTA)], XE, 900, 72)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s16():
        E.frase(c, t, C["s16"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 170, "center")
        E.frase(c, t, C["s16.a"], [("o", "i", 100, CLARO), ("maior", "g", 100, BR), ("número", "i", 100, CLARO), ("manda", "g", 100, BR)],
                W / 2, 320, "center", passo=0.15)
        y = 560
        w = E.formula(None, EQ, 0, 0, 120, a=0)
        x0 = W / 2 - w / 2
        E.foco(c, t, C["s16.b"], 0.5, lambda a: E.formula(c, EQ, x0, y, 120, "g", BR, a))
        if t >= C["s16.b"] + 0.4:
            q = ep(t, C["s16.b"] + 0.4, 0.4)
            wx = E.formula(None, "f{x^2}{25}", 0, 0, 120, a=0)
            M.rrect(c, x0 - 16, y - 150, wx + 32, 250, 26, CLARO, 0.22 * q)
            E.foco(c, t, C["s16.b"] + 0.4, 0.4, lambda a: E.pilula(c, "a² = 25", x0 + wx / 2, y + 150, 44, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s16.c"], 0.4, lambda a: E.pilula(c, "estica no eixo x", x0 + 560, y + 150, 44, "g", fundo="#000000", contorno=True, a=a))
        conta_em(c, t, C["s16.d"], [("c^2 = 25 − 9 = 16", BR)], W / 2, 900, 96, "center")
        E.foco(c, t, C["s16.d"] + 2.4, 0.4, lambda a: E.escreve(c, "→  c = 4", 1450, 900, 80, "g", C_ESC, a))
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return

    def s17():
        E.frase(c, t, C["s17"], [("por", "i", 70, CLARO), ("que", "i", 70, CLARO), ("funciona", "g", 70, BR)], W / 2, 190, "center")
        conta_em(c, t, C["s17.a"], [("a^2 = b^2 + c^2", BR)], W / 2, 350, 96, "center")
        conta_em(c, t, C["s17.b"], [("c^2 = a^2 − b^2", C_ESC)], W / 2, 500, 96, "center")
    E.saida(c, t, C["s17.c"] - 0.1, s17)
    if t < C["s17.c"]:
        return
    E.frase(c, t, C["s17.c"], [("não", "g", 76, ERRADO), ("compensa:", "i", 80, CLARO), ("lado", "i", 80, CLARO), ("direito", "i", 80, CLARO),
                               ("≠ 1", "g", 76, BR)], W / 2, 300, "center", passo=0.15)
    conta_em(c, t, C["s17.d"], [("9x^2 + 25y^2 = 225", BR)], W / 2, 520, 100, "center")
    E.foco(c, t, C["s17.e"], 0.5, lambda a: E.pilula(c, "÷ 225 primeiro", W / 2, 650, 52, "g", fundo=E.COR, a=a))
    conta_em(c, t, C["s17.e"] + 1.4, [(EQ, C_ESC)], W / 2, 870, 96, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 220)
    E.formula_em(c, t, C["s18.a"], "f{x^2}{16} + f{y^2}{25} = 1", XE, 450, 120)
    E.frase(c, t, C["s18.b"], [("semieixos?", "g", 80)], XE, 680)
    E.frase(c, t, C["s18.c"], [("focos?", "g", 80, COR)], XE, 820)
    if t >= C["s19"]:
        E.relogio(c, t, C["s19.a"], cx=1440, cy=480, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    plano(c, t, C["s20"], P2, [-4, 4], [-5, 5], 34)
    elipse(c, t, C["s20.a"] + 0.6, P2, 4, 5, 1.0)
    seg(c, t, C["s20.b"], P2(0, 0), P2(0, 5), A_, 0.6, 10)
    rot(c, t, C["s20.b"] + 0.4, "a = 5", *P2(0, 1.6), 1, 0, A_, 44)
    seg(c, t, C["s20.c"], P2(0, 0), P2(4, 0), B_, 0.6, 10)
    rot(c, t, C["s20.c"] + 0.4, "b = 4", *P2(2, 0), 0, 1, B_, 44)
    for i, y_ in enumerate((-3, 3)):
        foco_pt(c, t, C["s21.b"] + 0.2 * i, P2, 0, y_, "F", (-1, 0))

    def s20():
        E.formula_em(c, t, C["s20"], "f{x^2}{16} + f{y^2}{25} = 1", XE, 330, 96)
        E.frase(c, t, C["s20.a"], [("maior:", "i", 64), ("25", "g", 64, A_), ("embaixo", "i", 64), ("do", "i", 64), ("y", "g", 64)], XE, 500)
        E.frase(c, t, C["s20.a"] + 1.4, [("em", "i", 64), ("pé", "g", 64, COR)], XE, 590)
        conta_em(c, t, C["s20.b"], [("a = r{25} = ", TINTA), ("5", A_)], XE, 730, 76)
        conta_em(c, t, C["s20.c"], [("b = r{16} = ", TINTA), ("4", B_)], XE, 860, 76)
    E.saida(c, t, C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    conta_em(c, t, C["s21.a"], [("c^2 = 25 − 16 = 9", TINTA)], XE, 330, 80)
    conta_em(c, t, C["s21.a"] + 1.6, [("c = ", TINTA), ("3", C_)], XE, 450, 80)
    E.frase(c, t, C["s21.b"], [("focos:", "i", 64)], XE, 600)
    bola_txt(c, t, C["s21.b"] + 0.3, "(0, ±3)", XE + 410, 580, 120, 58)
    E.frase(c, t, C["s21.c"], [("3", "g", 66, C_), ("<", "g", 66), ("5:", "g", 66, A_), ("focos", "i", 66), ("dentro", "g", 66, CERTO)], XE, 820)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s22.a", [("denominadores", "g", 74), ("=", "i", 74), ("semieixos", "i", 74), ("ao", "i", 74), ("quadrado", "g", 74)]),
                 ("s22.b", [("o", "i", 74), ("maior", "g", 74, COR), ("diz", "i", 74), ("para", "i", 74), ("onde", "i", 74), ("estica", "i", 74)]),
                 ("s22.c", [("c²", "g", 74, C_), ("=", "i", 74), ("maior", "g", 74), ("−", "i", 74), ("menor", "g", 74)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 340, y, passo=0.12)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s23.a"], [("o", "i", 90), ("+", "g", 90, COR), ("vira", "i", 90), ("−", "g", 90, COR)], XE, 420)
    E.frase(c, t, C["s23.b"], [("Hipérbole", "g", 150, COR)], XE, 600)
    E.frase(c, t, C["s23.b"] + 1.4, ps("e qual figura cada equação desenha", "i", 54, TINTA2), XE, 700, passo=0.1)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, barbante=b_barbante, equacao=b_equacao, focos=b_focos, empe=b_empe,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
