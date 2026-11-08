"""Visual — Estudativo · MAT-TOP-012: hipérbole (focos e assíntotas) e como reconhecer cada cônica.

Segue a linguagem das cônicas do MAT-TOP-011: plano na metade direita, texto na esquerda, curva em índigo, focos em tinta
com "F". Cores fixas: A_ índigo = o á; B_ âmbar = o bê; C_ petróleo = o cê (aqui, a diagonal da caixa). A caixa de
lados 2a e 2b sai tracejada; as assíntotas, em cinza-escuro tracejado. Erro em vermelho, certo em verde, atalho no palco.
Peças locais: hiperbole() (os dois ramos crescem a partir dos vértices), elipse_px(), caixa(), assintotas(), seg(), conta()."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-012_hiperbole_e_conicas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("definicao", "equacao", "caixa", "reconhecer", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
A_, B_, C_ = E.COR, "#D98A00", "#0E9AA7"
C_ESC = "#3CC7D3"
assert 3 - (-5) == 8 and 5 - 3 == 2 and 8 - 2 == 6 == 2 * 3 and 9 + 16 == 25 and 16 - 9 == 7 and math.sqrt(7) < 3
assert 36 + 64 == 100 and math.isclose(8 / 6, 4 / 3)
_u = 1.0
_X, _Y = 3 * math.cosh(_u), 4 * math.sinh(_u)
D1, D2 = math.hypot(_X + 5, _Y), math.hypot(_X - 5, _Y)
assert abs(D1 - D2 - 6) < 1e-9 and f"{D1:.1f}" == "10.7" and f"{D2:.1f}" == "4.7"

P1 = E.Plano(960, 180, 840, 720, -7, 7, -6, 6)       # 60 px por unidade
P3 = E.Plano(960, 180, 840, 720, -14, 14, -12, 12)   # 30 px por unidade (questão)


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


def hip_px(c, cx, cy, ka, kb, xmax_px, ymax_px, p=1.0, cor=None, largura=8, a=1.0, vertical=False):
    """hipérbole em pixels: semieixos ka (no eixo dos focos) e kb, centro (cx, cy). Cada ramo cresce do vértice para as pontas"""
    if p <= 0 or a <= 0:
        return
    if not vertical:
        U = min(math.asinh(ymax_px / kb), math.acosh(max(1.0, xmax_px / ka)))
    else:
        U = min(math.asinh(xmax_px / kb), math.acosh(max(1.0, ymax_px / ka)))
    for ramo in (1, -1):
        for lado in (1, -1):
            pts = []
            n = 80
            for i in range(n + 1):
                u = lado * U * p * i / n
                X, Y = ka * math.cosh(u) * ramo, kb * math.sinh(u)
                pts.append((cx + Y, cy - X) if vertical else (cx + X, cy - Y))
            caminho(c, pts, cor or COR, largura, a)


def hiperbole(c, t, t0, P, a, b, d=1.2, cor=None, largura=8, alfa=1.0, vertical=False):
    k = P.x(1) - P.x(0)
    hip_px(c, P.x(0), P.y(0), a * k, b * k, (P.xmax) * k, (P.ymax) * k, ease_io(prog(t, t0, d)), cor, largura, alfa, vertical)


def elipse_px(c, cx, cy, rx, ry, p=1.0, cor=None, largura=8, a=1.0):
    if p <= 0 or a <= 0:
        return
    n = max(2, int(220 * p))
    caminho(c, [(cx + rx * math.cos(2 * math.pi * p * i / n), cy - ry * math.sin(2 * math.pi * p * i / n)) for i in range(n + 1)], cor or COR, largura, a)


def foco_pt(c, t, t0, P, x, y, nome="F", lado=(0, 1), cor=TINTA, size=44):
    E.ponto(c, t, t0, P, x, y, None, cor=cor, r=14)
    if nome:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E._cola(c, nome, *P(x, y), lado[0], lado[1], 22, size, "b", cor, a))


def seg(c, t, t0, A, B, cor, d=0.6, largura=9, a=1.0, tracejado=False):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *A, *B, cor, a, largura, progress=p, dash=E.TRACO if tracejado else None)


def rot(c, t, t0, s, X, Y, nx, ny, cor, size=50, gap=16):
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, s, X, Y, nx, ny, gap, size, "g", cor, a))


def caixa(c, t, t0, P, a, b, cor=TINTA2, d=0.8):
    p = ease_io(prog(t, t0, d))
    if p > 0:
        pts = [P(-a, -b), P(a, -b), P(a, b), P(-a, b), P(-a, -b)]
        q = int(4 * p)
        sub = pts[:q + 1]
        if q < 4:
            r = 4 * p - q
            sub.append((lerp(pts[q][0], pts[q + 1][0], r), lerp(pts[q][1], pts[q + 1][1], r)))
        caminho(c, sub, cor, 4, 1.0, E.TRACO)


def assintotas(c, t, t0, P, a, b, d=0.8, cor=TINTA2, alfa=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and alfa > 0:
        m = b / a
        for s in (1, -1):
            x1 = min(P.xmax, P.ymax / m)
            M.line(c, *P(0, 0), *P(x1 * p, s * m * x1 * p), cor, alfa, 4, dash=E.TRACO)
            M.line(c, *P(0, 0), *P(-x1 * p, -s * m * x1 * p), cor, alfa, 4, dash=E.TRACO)


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


EQ = "f{x^2}{9} − f{y^2}{16} = 1"


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        for k, s, cx, sinal, cor in (("s01.b", "f{x^2}{9} + f{y^2}{16} = 1", 480, "+", TINTA), ("s01.c", EQ, 1440, "−", TINTA)):
            E.formula_em(c, t, C[k] - 0.3, s, cx, 300, 92, align="center")
        q = ep(t, C["s01.a"], 0.5) * (1 - ep(t, C["s01.c"] + 2.0, 0.4))
        if q > 0:
            for cx in (480, 1440):
                if cx == 1440 and t < C["s01.c"] - 0.3:
                    continue
                c.drawCircle(cx - 4, 268, 52, M.paint(COR, 0.16 * q))
        elipse_px(c, 480, 690, 3 * 40, 4 * 40, ease_io(prog(t, C["s01.b"], 1.0)), COR, 9)
        hip_px(c, 1440, 690, 3 * 40, 4 * 40, 300, 230, ease_io(prog(t, C["s01.c"], 1.2)), COR, 9)
        E.frase(c, t, C["s01.b"] + 0.6, [("elipse", "g", 64)], 480, 960, "center")
        E.frase(c, t, C["s01.d"], [("hipérbole", "g", 72, COR)], 1440, 960, "center")
        E.frase(c, t, C["s01.c"] + 1.2, ps("dois pedaços", "i", 52, TINTA2), 1440, 470, "center")
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("focos", "g", 120), ("e", "i", 110), ("retas-guia", "g", 120)], XE, 450)
        E.frase(c, t, C["s02.a"] + 2.0, [("da", "i", 96), ("hipérbole", "g", 110, COR)], XE, 590)
        E.frase(c, t, C["s02.a"] + 3.0, ps("e qual figura cada equação desenha", "i", 58, TINTA2), XE, 720, passo=0.1)
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
    elipse_px(c, 400, 415, 140, 84, ease_io(prog(t, k + 0.3, 0.9)), COR, 8)
    E.frase(c, t, k, [("elipse:", "g", 64, COR)], 620, 380)
    conta_em(c, t, k + 1.0, [("f{x^2}{a^2} + f{y^2}{b^2} = 1", TINTA)], 880, 405, 66)
    conta_em(c, t, k + 3.2, [("a", A_), ("^2 = ", TINTA), ("b", B_), ("^2 + ", TINTA), ("c", C_), ("^2", TINTA)], 620, 500, 66)
    k = C["s03.c"]
    # escada da reta: sobe eme a cada passo
    x0, y0, u = 300, 820, 60
    if t >= k:
        q = ep(t, k + 0.2, 0.6)
        M.line(c, x0 - 40, y0 + 40 * 1.5, x0 + 4 * u, y0 - 4 * u * 0.75 + 0, COR, q, 7)
        for i in range(3):
            qq = ep(t, k + 0.8 + 0.3 * i, 0.3)
            xa, ya = x0 + i * u, y0 - i * u * 0.75 + 30
            M.line(c, xa, ya, xa + u, ya, C_, qq, 5)
            M.line(c, xa + u, ya, xa + u, ya - u * 0.75, B_, qq, 5)
    E.frase(c, t, k, [("reta", "g", 64, COR)], 620, 700)
    conta_em(c, t, k + 0.6, [("y = mx", TINTA)], 820, 700, 64)
    E.frase(c, t, k + 1.6, [("m", "g", 60, COR), ("=", "i", 62), ("quanto", "i", 62), ("sobe", "g", 60, B_), ("a", "i", 62), ("cada", "i", 62),
                            ("passo", "g", 60, C_)], 620, 800, passo=0.12)
    E.frase(c, t, C["s04"] - 2.4, ps("faltou alguma? procure no canal", "i", 50, TINTA2), W / 2, 975, "center", passo=0.1)


# ---------------- definição ----------------
def b_definicao(c, t, C, b):
    plano(c, t, C["s04"], P1, [-5, -3, 3, 5], [], 34)
    hiperbole(c, t, C["s04.b"], P1, 3, 4, 1.4)
    foco_pt(c, t, C["s04"] + 0.4, P1, -5, 0, "F", (0, -1))
    foco_pt(c, t, C["s04"] + 0.5, P1, 5, 0, "F", (0, -1))

    def ponto1():
        E.ponto(c, t, C["s05.b"], P1, 3, 0, None, cor=COR, r=14)
        seg(c, t, C["s05.c"], P1(-5, 0), P1(3, 0), B_, 0.6, 9)
        rot(c, t, C["s05.c"] + 0.4, "8", *P1(-1, 0), 0, 1, B_, 50)
        seg(c, t, C["s05.d"], P1(5, 0), P1(3, 0), C_, 0.4, 9)
        rot(c, t, C["s05.d"] + 0.3, "2", *P1(4, 0), 0, 1, C_, 50)
    E.saida(c, t, C["s05.f"], ponto1)
    if t >= C["s05.f"]:
        X = (_X, _Y)
        E.ponto(c, t, C["s05.f"], P1, *X, None, cor=COR, r=14)
        seg(c, t, C["s05.f"] + 0.2, P1(-5, 0), P1(*X), B_, 0.6, 7)
        seg(c, t, C["s05.f"] + 0.5, P1(5, 0), P1(*X), C_, 0.5, 7)
        rot(c, t, C["s05.f"] + 0.8, "10,7", *P1(-0.6, 2.6), -1, -1, B_, 44)
        rot(c, t, C["s05.f"] + 1.0, "4,7", *P1(4.8, 2.35), 1, 0, C_, 44)

    E.frase(c, t, C["s04"], [("elipse:", "i", 60, TINTA2), ("soma", "g", 56, TINTA2), ("fixa", "i", 60, TINTA2)], XE, 260)
    E.frase(c, t, C["s04.b"], [("hipérbole:", "g", 68, COR)], XE, 370)
    E.frase(c, t, C["s04.b"] + 0.8, [("diferença", "g", 68), ("fixa", "i", 74)], XE, 460)
    E.foco(c, t, C["s04.c"], 0.5, lambda a: conta(c, [("longe", B_), (" − ", TINTA), ("perto", C_)], XE, 580, 66, a))
    if t >= C["s05"]:
        conta_em(c, t, C["s05.b"], [("(3, 0):", TINTA2)], XE, 700, 56)
        conta_em(c, t, C["s05.e"], [("8", B_), (" − ", TINTA), ("2", C_), (" = 6", TINTA)], XE + 260, 700, 72)
        conta_em(c, t, C["s05.f"] + 0.8, [("10,7", B_), (" − ", TINTA), ("4,7", C_), (" = 6", TINTA)], XE, 830, 72)
        E.frase(c, t, C["s05.f"] + 1.6, ps("sempre 6", "i", 56, COR), XE + 560, 830)


# ---------------- a equação ----------------
def b_equacao(c, t, C, b):
    plano(c, t, C["s06"], P1, [], [], 34)
    hiperbole(c, t, C["s06"] + 0.2, P1, 3, 4, 1.0)
    for i, x_ in enumerate((-3, 3)):
        E.ponto(c, t, C["s07.b"] + 0.2 * i, P1, x_, 0, None, cor=TINTA, r=13)
        E.foco(c, t, C["s07.b"] + 0.2 * i, 0.4, lambda a, x_=x_: E._cola(c, E._num(x_), *P1(x_, 0), -1 if x_ < 0 else 1, 1, 12, 42, "b", TINTA, a))
    seg(c, t, C["s07.c"], P1(-3, -0.6), P1(3, -0.6), A_, 0.6, 6)
    rot(c, t, C["s07.c"] + 0.5, "6 = 2a", *P1(0, -0.6), 0, 1, A_, 46)
    if t >= C["s08.d"]:
        q = ep(t, C["s08.d"], 0.4)
        M.line(c, P1.ox, P1.caixa[1], P1.ox, P1.caixa[1] + P1.caixa[3], ERRADO, 0.35 * q, 22)
        E.foco(c, t, C["s08.d"] + 0.3, 0.4, lambda a: E.pilula(c, "não corta o eixo y", P1.x(0), P1.y(5), 40, "g", fundo=ERRADO, a=a))

    def s06():
        E.formula_em(c, t, C["s06.a"], "f{x^2}{a^2} − f{y^2}{b^2} = 1", XE, 300, 92)
        if t >= C["s06.a"] + 0.6:
            q = ep(t, C["s06.a"] + 0.6, 0.4) * (1 - ep(t, C["s06.b"], 0.4))
            wx = E.formula(None, "f{x^2}{a^2} ", 0, 0, 92, a=0)
            c.drawCircle(XE + wx + 22, 270, 44, M.paint(COR, 0.18 * q))
        E.formula_em(c, t, C["s06.b"], EQ, XE, 540, 100)
        conta_em(c, t, C["s06.c"], [("a^2 = 9  →  a = ", TINTA), ("3", A_)], XE, 730, 70)
        conta_em(c, t, C["s06.d"], [("b^2 = 16  →  b = ", TINTA), ("4", B_)], XE, 850, 70)
    E.saida(c, t, C["s07"] - 0.1, s06)

    def s07():
        E.frase(c, t, C["s07.a"], [("no", "i", 64), ("eixo", "i", 64), ("x:", "g", 64), ("y = 0", "g", 64, COR)], XE, 280)
        conta_em(c, t, C["s07.a"] + 1.0, [("x^2 = 9", TINTA)], XE, 400, 80)
        conta_em(c, t, C["s07.b"], [("x = 3  ou  x = −3", COR)], XE, 520, 72)
        E.frase(c, t, C["s07.b"] + 1.2, [("vértices:", "i", 60), ("as", "i", 60), ("pontas", "g", 60)], XE, 630)
        E.frase(c, t, C["s07.c"], [("6", "g", 66, A_), ("=", "i", 66), ("diferença", "i", 66), ("=", "i", 66), ("2a", "g", 66, A_)], XE, 770)
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08.a"], [("no", "i", 64), ("eixo", "i", 64), ("y:", "g", 64), ("x = 0", "g", 64, COR)], XE, 280)
    conta_em(c, t, C["s08.b"], [("− f{y^2}{16} = 1", TINTA)], XE, 440, 84)
    conta_em(c, t, C["s08.c"], [("y^2 = −16", ERRADO)], XE, 600, 84)
    E.frase(c, t, C["s08.c"] + 1.2, ps("quadrado negativo? não existe", "i", 54, TINTA2), XE, 700, passo=0.1)
    E.frase(c, t, C["s08.d"], [("partida", "g", 76, COR), ("em", "i", 80), ("dois", "i", 80)], XE, 850)


# ---------------- a caixa: focos e assíntotas ----------------
def b_caixa(c, t, C, b):
    plano(c, t, C["s09"], P1, [-5, -3, 3, 5], [-4, 4], 34)
    caixa(c, t, C["s09.a"], P1, 3, 4)
    seg(c, t, C["s09.b"], P1(0, 0), P1(3, 0), A_, 0.5, 10)
    rot(c, t, C["s09.b"] + 0.3, "a = 3", *P1(1.5, 0), 0, 1, A_, 44)
    seg(c, t, C["s09.c"], P1(0, 0), P1(0, 4), B_, 0.5, 10)
    rot(c, t, C["s09.c"] + 0.3, "b = 4", *P1(0, 2), -1, 0, B_, 44)
    seg(c, t, C["s10.a"], P1(0, 0), P1(3, 4), C_, 0.6, 10)
    E.foco(c, t, C["s10.b"], 0.4, lambda a: E._meio(c, "c = 5", *P1(1.95, 0.85), 42, "g", C_, a))
    # o compasso leva o cê até o eixo x
    if t >= C["s10.d"] - 0.6:
        p = ease_io(prog(t, C["s10.d"] - 0.6, 0.9))
        a0 = math.degrees(math.atan2(4, 3))
        k = P1.x(1) - P1.x(0)
        r = 5 * k
        n = 40
        pts = [(P1.x(0) + r * math.cos(math.radians(a0 * (1 - p * i / n))), P1.y(0) - r * math.sin(math.radians(a0 * (1 - p * i / n)))) for i in range(n + 1)]
        caminho(c, pts, C_, 4, 0.8, [10, 8])
    for i, x_ in enumerate((-5, 5)):
        foco_pt(c, t, C["s10.d"] + 0.3 + 0.2 * i, P1, x_, 0, "F", (0, -1))
    if t >= C["s11"]:
        assintotas(c, t, C["s11.a"], P1, 3, 4, 1.0)
        hiperbole(c, t, C["s11.b"] - 0.4, P1, 3, 4, 1.4)
    if t >= C["s12.a"]:
        q = ep(t, C["s12.a"], 0.4)
        M.line(c, *P1(0, 0), *P1(3, 0), C_, q, 5)
        M.line(c, *P1(3, 0), *P1(3, 4), B_, q, 5)


    def s09_10():
        E.frase(c, t, C["s09.a"], [("monte", "i", 80), ("a", "i", 80), ("caixa", "g", 80, COR)], XE, 280)
        E.frase(c, t, C["s09.b"], [("3", "g", 64, A_), ("para", "i", 62), ("cada", "i", 62), ("lado:", "i", 62), ("a", "g", 64, A_)], XE, 400)
        E.frase(c, t, C["s09.c"], [("4", "g", 64, B_), ("para", "i", 62), ("cima", "i", 62), ("e", "i", 62), ("baixo:", "i", 62), ("b", "g", 64, B_)], XE, 500)
        E.frase(c, t, C["s10.a"], [("diagonal", "g", 64, C_), ("=", "i", 64), ("hipotenusa", "i", 64)], XE, 640)
        conta_em(c, t, C["s10.c"], [("c", C_), ("^2 = ", TINTA), ("a", A_), ("^2 + ", TINTA), ("b", B_), ("^2", TINTA)], XE, 770, 66)
        conta_em(c, t, C["s10.c"] + 1.8, [("9 + 16 = 25  →  ", TINTA), ("c = 5", C_)], XE, 880, 60)
    E.saida(c, t, C["s11"] - 0.1, s09_10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11.a"], [("prolongue", "i", 70), ("as", "i", 70), ("diagonais", "g", 70)], XE, 280)
    E.frase(c, t, C["s11.b"], ps("chega perto, nunca encosta", "i", 54, TINTA2), XE, 370, passo=0.1)
    E.frase(c, t, C["s11.c"], [("assíntotas", "g", 80, COR)], XE, 490)
    E.frase(c, t, C["s12.a"], [("sobe", "g", 60, B_), ("4", "g", 60, B_), ("a", "i", 62), ("cada", "i", 62), ("3", "g", 60, C_), ("passos", "i", 62)], XE, 620)
    conta_em(c, t, C["s12.b"], [("m = f{4}{3}", COR)], XE, 760, 72)
    conta_em(c, t, C["s12.c"], [("y = ±f{4x}{3}", TINTA)], XE, 920, 76)


# ---------------- reconhecer ----------------
def mini_parabola(c, cx, cy, p, a=1.0):
    pts = [(cx + u * 34, cy + 80 - (u * u / 8) * 34) for u in [-5.5 + 11 * i / 60 for i in range(int(60 * p) + 1)]]
    caminho(c, pts, COR, 8, a)


def b_reconhecer(c, t, C, b):
    E.frase(c, t, C["s13.a"], [("as", "i", 76), ("três", "i", 76), ("cônicas", "g", 76, COR)], W / 2, 170, "center")
    cols = (330, 960, 1590)

    def tres():
        for i, (k, eq, nome, kn) in enumerate((("s13.b", "x^2 = 8y", "parábola", "s13.c"), ("s14.a", "f{x^2}{25} + f{y^2}{9} = 1", "elipse", "s14.b"),
                                             ("s14.d", EQ, "hipérbole", "s14.e"))):
            cx = cols[i]
            p = ep(t, C[k], 0.5)
            if p > 0:
                M.rrect(c, cx - 280, 230, 560, 720, 30, TINTA, 0.04 * p)
            E.formula_em(c, t, C[k], eq, cx, 380, 68, align="center")
            if i == 0:
                mini_parabola(c, cx, 620, ease_io(prog(t, C[k] + 0.4, 0.8)))
            elif i == 1:
                elipse_px(c, cx, 640, 200, 120, ease_io(prog(t, C[k] + 0.4, 0.8)), COR, 8)
            else:
                hip_px(c, cx, 640, 80, 107, 250, 170, ease_io(prog(t, C[k] + 0.4, 0.8)), COR, 8)
            E.frase(c, t, C[kn], [(nome, "g", 66, COR)], cx, 880, "center")
        E.foco(c, t, C["s13.b"] + 1.0, 0.4, lambda a: E.pilula(c, "só uma ao quadrado", cols[0], 480, 40, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s14.a"] + 1.0, 0.4, lambda a: E.pilula(c, "+ entre os quadrados", cols[1], 480, 40, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s14.d"] + 1.0, 0.4, lambda a: E.pilula(c, "− entre os quadrados", cols[2], 480, 40, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s14.c"], 0.4, lambda a: E.pilula(c, "denominadores iguais: circunferência", cols[1], 1005, 40, "g", fundo=C_, a=a))
    E.saida(c, t, C["s15"] - 0.1, tres)
    if t < C["s15"]:
        return
    P = E.Plano(1100, 220, 700, 760, -5.83, 5.83, -6.33, 6.33)
    plano(c, t, C["s15"], P, [], [-5, -3, 3, 5], 34)
    hiperbole(c, t, C["s15.c"], P, 3, 4, 1.2, vertical=True)
    for i, y_ in enumerate((-5, 5)):
        foco_pt(c, t, C["s15.c"] + 1.0 + 0.2 * i, P, 0, y_, "F", (1, 0))
    E.frase(c, t, C["s15.a"], ps("a letra com o sinal de", "i", 60), XE, 300, passo=0.1)
    E.frase(c, t, C["s15.a"] + 1.4, [("+", "g", 70, COR), ("diz", "i", 62), ("o", "i", 62), ("eixo", "i", 62), ("dos", "i", 62), ("focos", "g", 62)], XE, 390)
    E.formula_em(c, t, C["s15.b"], "f{y^2}{9} − f{x^2}{16} = 1", XE, 580, 92)
    if t >= C["s15.b"] + 1.0:
        q = ep(t, C["s15.b"] + 1.0, 0.4)
        wy = E.formula(None, "f{y^2}{9}", 0, 0, 92, a=0)
        M.rrect(c, XE - 14, 450, wy + 28, 190, 22, COR, 0.14 * q)
    E.frase(c, t, C["s15.c"], [("abre", "i", 66), ("para", "i", 66), ("cima", "g", 66, COR), ("e", "i", 66), ("baixo", "g", 66, COR)], XE, 780)
    E.frase(c, t, C["s15.c"] + 1.6, [("focos", "i", 60), ("no", "i", 60), ("eixo", "i", 60), ("y", "g", 60)], XE, 880)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano(c, t, C["s16"], P1, [-3, 3], [], 34)
    hiperbole(c, t, C["s16"] + 0.1, P1, 3, 4, 0.8)
    r7 = math.sqrt(7)
    if C["s16.c"] <= t < C["s17"]:
        for x_ in (-r7, r7):
            E.ponto(c, t, C["s16.c"] + 0.3, P1, x_, 0, None, cor=ERRADO, r=14)
        E.foco(c, t, C["s16.c"] + 0.6, 0.4, lambda a: E.pilula(c, "foco aqui?", P1.x(0), P1.y(1.0), 40, "g", fundo=ERRADO, a=a))
    if t >= C["s17"]:
        for x_ in (-5, 5):
            foco_pt(c, t, C["s17.a"], P1, x_, 0, "F", (0, -1), CERTO)
        seg(c, t, C["s17.b"], P1(0, -0.7), P1(5, -0.7), C_, 0.5, 7)
        rot(c, t, C["s17.b"] + 0.3, "c = 5", *P1(1.4, -0.7), 0, 1, C_, 44)

    def s16():
        E.frase(c, t, C["s16"], [("cuidado", "g", 96, ERRADO)], XE, 260)
        E.frase(c, t, C["s16.a"], ps("a conta da elipse", "i", 66), XE, 380)
        E.frase(c, t, C["s16.a"] + 1.0, [("na", "i", 66), ("hipérbole?", "g", 66, ERRADO)], XE, 470)
        conta_em(c, t, C["s16.b"], [("c^2 = 16 − 9 = 7", ERRADO)], XE, 640, 80)
        conta_em(c, t, C["s16.c"], [("c = r{7} ≈ 2,6", ERRADO)], XE, 780, 80)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17.a"], ps("o foco fica além do vértice", "i", 60), XE, 280, passo=0.1)
    conta_em(c, t, C["s17.b"], [("c", C_), (" > ", TINTA), ("3", A_)], XE, 450, 110)
    E.frase(c, t, C["s17.b"] + 3.0, [("elipse:", "g", 58), ("o", "i", 60), ("maior", "i", 60), ("é", "i", 60), ("o", "i", 60), ("a", "g", 60, A_)], XE, 620)
    E.frase(c, t, C["s17.c"], [("hipérbole:", "g", 58, COR), ("o", "i", 60), ("maior", "i", 60), ("é", "i", 60), ("o", "i", 60), ("c", "g", 60, C_)], XE, 730)
    conta_em(c, t, C["s17.c"] + 1.6, [("c", C_), ("^2 = ", TINTA), ("a", A_), ("^2 + ", TINTA), ("b", B_), ("^2", TINTA)], XE, 870, 72)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s18():
        E.frase(c, t, C["s18"], ps("agora, o atalho", "i", 76, CLARO), 600, 170, "center")
        E.frase(c, t, C["s18.a"], [("a", "i", 100, CLARO), ("caixa", "g", 100, BR), ("resolve", "i", 100, CLARO)], 600, 300, "center")
        y = 520
        w = E.formula(None, EQ, 0, 0, 104, a=0)
        x0 = 600 - w / 2
        E.foco(c, t, C["s18.a"] + 0.6, 0.5, lambda a: E.formula(c, EQ, x0, y, 104, "g", BR, a))
        wx = E.formula(None, "f{x^2}{9}", 0, 0, 104, a=0)
        wm = E.formula(None, "f{x^2}{9} − ", 0, 0, 104, a=0)
        wy = E.formula(None, "f{y^2}{16}", 0, 0, 104, a=0)
        E.foco(c, t, C["s18.b"], 0.4, lambda a: E.pilula(c, "a² = 9", x0 + wx / 2, y + 140, 42, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s18.c"], 0.4, lambda a: E.pilula(c, "b² = 16", x0 + wm + wy / 2, y + 140, 42, "g", fundo="#8A5800", a=a))
        # a caixa à direita
        cx, cy, k = 1440, 560, 60
        p = ease_io(prog(t, C["s18.c"] + 0.6, 0.8))
        if p > 0:
            pts = [(cx - 3 * k, cy - 4 * k), (cx + 3 * k, cy - 4 * k), (cx + 3 * k, cy + 4 * k), (cx - 3 * k, cy + 4 * k), (cx - 3 * k, cy - 4 * k)]
            caminho(c, pts, CLARO, 4, p, E.TRACO)
        q = ep(t, C["s18.d"], 0.5)
        if q > 0:
            M.line(c, cx, cy, cx + 3 * k, cy - 4 * k, C_ESC, q, 9)
            E.foco(c, t, C["s18.d"] + 0.3, 0.4, lambda a: E.escreve(c, "c = 5", cx - 170, cy - 2 * k - 10, 52, "g", C_ESC, a))
        q = ep(t, C["s18.e"], 0.6)
        if q > 0:
            for s in (1, -1):
                M.line(c, cx - 4.5 * k * q, cy + s * 6 * k * q, cx + 4.5 * k * q, cy - s * 6 * k * q, CLARO, 0.9, 4, dash=E.TRACO)
            hip_px(c, cx, cy, 3 * k, 4 * k, 4.4 * k, 6 * k, q, BR, 7)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("por", "i", 70, CLARO), ("que", "i", 70, CLARO), ("funciona", "g", 70, BR)], W / 2, 200, "center")
    E.frase(c, t, C["s19.a"], ps("canto da caixa: a para o lado, b para cima", "i", 60, CLARO), W / 2, 340, "center", passo=0.08)
    conta_em(c, t, C["s19.b"], [("c^2 = a^2 + b^2", C_ESC)], W / 2, 520, 100, "center")
    E.frase(c, t, C["s19.c"], [("não", "g", 72, ERRADO), ("compensa:", "i", 76, CLARO), ("só", "i", 76, CLARO), ("o", "i", 76, CLARO), ("nome", "g", 72, BR)],
            W / 2, 740, "center", passo=0.15)
    E.frase(c, t, C["s19.d"], [("olhe", "i", 76, CLARO), ("os", "i", 76, CLARO), ("sinais", "g", 76, BR)], W / 2, 870, "center")


# ---------------- questão ----------------
QS = ("f{x^2}{16} + f{y^2}{7} = 1", "y^2 = 12x", "f{y^2}{4} − f{x^2}{5} = 1")


def b_questao(c, t, C, b):
    E.frase(c, t, C["s20"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s20"] + 0.8, [("1)", "g", 60, COR)], XE, 360)
    E.formula_em(c, t, C["s20.a"], "f{x^2}{36} − f{y^2}{64} = 1", XE + 90, 360, 84)
    E.frase(c, t, C["s20.a"] + 3.0, [("focos?", "g", 60), ("assíntotas?", "g", 60)], XE + 90, 490)
    E.frase(c, t, C["s20.b"] - 0.4, [("2)", "g", 60, COR), ("qual", "i", 62), ("figura?", "g", 60)], XE, 640)
    E.formula_em(c, t, C["s20.b"], QS[0], XE + 90, 770, 76)
    E.formula_em(c, t, C["s20.b"] + 0.3, QS[1], XE + 620, 770, 76)
    E.formula_em(c, t, C["s20.b"] + 0.6, QS[2], XE + 90, 930, 76)
    if t >= C["s21"]:
        E.relogio(c, t, C["s21.a"], cx=1500, cy=430, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s22():
        plano(c, t, C["s22"], P3, [-10, -6, 6, 10], [-8, 8], 32)
        caixa(c, t, C["s22.b"] + 0.5, P3, 6, 8)
        seg(c, t, C["s22.a"], P3(0, 0), P3(6, 0), A_, 0.5, 9)
        seg(c, t, C["s22.b"], P3(0, 0), P3(0, 8), B_, 0.5, 9)
        seg(c, t, C["s22.c"], P3(0, 0), P3(6, 8), C_, 0.6, 9)
        E.foco(c, t, C["s22.c"] + 0.4, 0.4, lambda a: E._meio(c, "c = 10", *P3(3.4, 10.2), 44, "g", C_, a))
        for i, x_ in enumerate((-10, 10)):
            foco_pt(c, t, C["s22.d"] + 0.2 * i, P3, x_, 0, "F", (0, -1))
        assintotas(c, t, C["s22.e"], P3, 6, 8, 0.9)
        hiperbole(c, t, C["s22.e"] + 0.5, P3, 6, 8, 1.2)
        E.formula_em(c, t, C["s22"], "f{x^2}{36} − f{y^2}{64} = 1", XE, 250, 80)
        conta_em(c, t, C["s22.a"], [("a = r{36} = ", TINTA), ("6", A_)], XE, 390, 64)
        conta_em(c, t, C["s22.b"], [("b = r{64} = ", TINTA), ("8", B_)], XE, 490, 64)
        conta_em(c, t, C["s22.c"], [("c^2 = 36 + 64 = 100", TINTA)], XE, 590, 64)
        bola_txt(c, t, C["s22.d"], "(±10, 0)", XE + 190, 730, 100, 50)
        conta_em(c, t, C["s22.f"], [("m = f{8}{6} = f{4}{3}", COR)], XE, 920, 64)
    E.saida(c, t, C["s23"] - 0.1, s22)
    if t < C["s23"]:
        return
    nomes = (("s23.a", "elipse"), ("s23.b", "parábola"), ("s23.c", "hipérbole"))
    for i, (s, (k, nome)) in enumerate(zip(QS, nomes)):
        y = 330 + i * 230
        E.formula_em(c, t, C["s23"] + 0.2 * i, s, XE + 60, y, 80)
        E.foco(c, t, C[k], 0.5, lambda a, y=y, nome=nome: E.pilula(c, nome, 1300, y - 30, 64, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s23.c"] + 2.0, ps("aberta para cima e para baixo: o + está no y", "i", 50, TINTA2), XE + 60, 1000, passo=0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s24.a", [("hipérbole:", "g", 70), ("c²", "g", 70, C_), ("=", "i", 72), ("a²", "g", 70, A_), ("+", "i", 72), ("b²", "g", 70, B_)]),
                 ("s24.b", [("assíntotas", "g", 70, COR), ("=", "i", 72), ("diagonais", "i", 72), ("da", "i", 72), ("caixa", "i", 72)]),
                 ("s24.c", [("os", "i", 72), ("sinais", "g", 70), ("dizem", "i", 72), ("qual", "i", 72), ("cônica", "g", 70, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 340, y, passo=0.12)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s25"] + 0.8, [("Praticando", "g", 150, COR)], XE, 460)
    E.frase(c, t, C["s25.a"], ps("distâncias e circunferências", "i", 60, TINTA2), XE, 580, passo=0.1)
    E.frase(c, t, C["s25.b"], [("e", "i", 60, TINTA2), ("as", "i", 60, TINTA2), ("três", "i", 60, TINTA2), ("cônicas", "g", 60, COR)], XE, 670)
    E.foco(c, t, C["s25.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s25.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s25.c"] + 0.2, 0.4))
    E.frase(c, t, C["s25.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, definicao=b_definicao, equacao=b_equacao, caixa=b_caixa, reconhecer=b_reconhecer,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
