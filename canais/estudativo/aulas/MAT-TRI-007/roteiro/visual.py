"""Visual — Estudativo · MAT-TRI-007: radianos (60° = π/3 rad; π rad = 180°) e o ciclo trigonométrico (390° cai no ponto do 30°).
Linguagem da trigonometria (MAT-TRI-001): figuras em tinta; o ângulo da vez é o arco na cor da matéria; resposta na esfera ou na pílula;
erro em vermelho, certo em verde; atalho no palco escuro. No ciclo: eixos com seta, o ponto de partida à direita, o sentido
anti-horário com uma seta curva, e o arco que anda na cor da matéria, com a ponta de seta onde para.
A figura não mente: 1 rad é o arco do tamanho do raio (o raio se dobra sobre a circunferência), cabem 6 e pouco numa volta,
e os arcos de mais de uma volta saem em espiral, uma volta por fora da outra, até parar no ponto certo.
Peças locais: ciclo() (eixos, circunferência, quadrantes), arco() (arco com seta, de a0 até a1, em graus), espiral() (mais de uma
volta), marca() (ponto no ciclo com rótulo), raio_dobra() (o raio que vira arco), regra3() (a regra de três em duas linhas), resp().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-007_radianos_e_ciclo_trigonometrico.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("radiano", "converter", "ciclo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
assert 390 - 360 == 30 and 750 - 360 == 390 and 480 - 360 == 120 and 90 < 120 < 180
assert 180 * 1 / 3 == 60 and 60 / 180 == 1 / 3 and 3 * 180 == 540 and 540 / 4 == 135 and 180 / 60 == 3 and 180 / 45 == 4
assert abs(120 / 180 - 2 / 3) < 1e-12 and 2 * 180 / 3 == 120 and 57 < 180 / math.pi < 58 and 6 < 2 * math.pi < 7


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def resp(c, t, t0, s, cx, cy, size=76, alto=1.75, cor=None):
    def f(a):
        w = E.formula(c, s, 0, 0, size, a=0) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")
    E.foco(c, t, t0, 0.5, f)


def pilula(c, t, t0, s, cx, cy, size=64):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, s, cx, cy, size, "g", a=a, cor=E.SOBRE))


def pt(cx, cy, r, ang):
    """ponto do ciclo no ângulo ang (graus, anti-horário a partir da direita)"""
    return cx + r * math.cos(math.radians(ang)), cy - r * math.sin(math.radians(ang))


def ciclo(c, t, t0, cx, cy, r, tq=None, escuro=False, rotulos=True, a=1.0):
    """eixos com seta, circunferência que se fecha e, em tq, os quatro quadrantes"""
    if t < t0 or a <= 0:
        return
    tinta = BR if escuro else TINTA
    q = ep(t, t0, 0.6) * a
    M.arrow(c, cx - r - 70, cy, cx + r + 90, cy, tinta, q, 4, 20, q)
    M.arrow(c, cx, cy + r + 70, cx, cy - r - 90, tinta, q, 4, 20, q)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -360 * ease_io(prog(t, t0 + 0.2, 0.9)), False,
              M.paint(tinta, a, stroke=5))
    if rotulos:
        E.foco(c, t, t0 + 0.6, 0.4, lambda b: (E.escreve(c, "x", cx + r + 70, cy + 56, 50, "i", TINTA2 if not escuro else CLARO, b * a),
                                               E.escreve(c, "y", cx + 22, cy - r - 66, 50, "i", TINTA2 if not escuro else CLARO, b * a)))
    if tq is not None:
        for i, ang in enumerate((45, 135, 225, 315)):
            X, Y = pt(cx, cy, r * 0.62, ang)
            E.foco(c, t, tq + 0.15 * i, 0.4, lambda b, i=i, X=X, Y=Y: centro(c, f"{i + 1}º", X, Y + 22, 60, "g", CINZA if not escuro else CLARO, b * a))


def ponta(c, x, y, dx, dy, cor, a, tam=26):
    """ponta de seta em (x, y) apontando para (dx, dy)"""
    n = math.hypot(dx, dy) or 1
    dx, dy = dx / n, dy / n
    p = skia.Path()
    p.moveTo(x + dx * tam * 0.6, y + dy * tam * 0.6)
    p.lineTo(x - dx * tam * 0.6 - dy * tam * 0.55, y - dy * tam * 0.6 + dx * tam * 0.55)
    p.lineTo(x - dx * tam * 0.6 + dy * tam * 0.55, y - dy * tam * 0.6 - dx * tam * 0.55)
    p.close()
    c.drawPath(p, M.paint(cor, a))


def arco(c, cx, cy, r, a0, a1, cor=None, larg=12, p=1.0, a=1.0, seta=True):
    """arco de a0 a a1 (graus; a1 < a0 gira no sentido do relógio), desenhado até a fração p"""
    if p <= 0 or a <= 0 or abs(a1 - a0) < 0.5:
        return
    cor = cor or E.COR
    fim = lerp(a0, a1, p)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -a0, -(fim - a0), False, M.paint(cor, a, stroke=larg, cap_round=True))
    if seta:
        X, Y = pt(cx, cy, r, fim)
        s = 1 if a1 > a0 else -1
        th = math.radians(fim)
        ponta(c, X, Y, -math.sin(th) * s, -math.cos(th) * s, cor, a, larg * 2.6)


def espiral(c, cx, cy, r, total, cor=None, larg=10, p=1.0, a=1.0, passo=34):
    """arco de 0 até total graus (pode passar de 360): cada volta um pouco mais longe do centro"""
    if p <= 0 or a <= 0:
        return
    cor = cor or E.COR
    fim = total * p
    path = skia.Path()
    n = max(2, int(fim / 2))
    for i in range(n + 1):
        ang = fim * i / n
        rr = r + passo * ang / 360
        X, Y = pt(cx, cy, rr, ang)
        (path.moveTo if i == 0 else path.lineTo)(X, Y)
    pp = M.paint(cor, a, stroke=larg, cap_round=True); pp.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pp)
    rr = r + passo * fim / 360
    X, Y = pt(cx, cy, rr, fim)
    th = math.radians(fim)
    ponta(c, X, Y, -math.sin(th), -math.cos(th), cor, a, larg * 2.6)


def marca(c, t, t0, cx, cy, r, ang, rot=None, cor=None, size=50, fora=60, rcor=None):
    """ponto no ciclo, com o rótulo por fora"""
    k = ease_back(prog(t, t0, 0.4))
    if k <= 0:
        return
    cor = cor or E.COR
    X, Y = pt(cx, cy, r, ang)
    c.drawCircle(X, Y, 15 * k, M.paint(cor))
    c.drawCircle(X, Y, 15 * k, M.paint(BR, 1.0, stroke=3))
    if rot:
        Xr, Yr = pt(cx, cy, r + fora, ang)
        E.foco(c, t, t0 + 0.1, 0.4, lambda a: E.formula(c, rot, Xr, Yr + size * 0.36, size, "g", rcor or cor, a, "center"))


def raio_dobra(c, cx, cy, r, p, cor, a=1.0, larg=12):
    """um segmento do tamanho do raio, de pé na ponta direita, que se dobra sobre a circunferência (p = 0..1)"""
    if a <= 0:
        return
    path = skia.Path()
    n = 40
    for i in range(n + 1):
        s = i / n
        P0 = (cx + r, cy - s * r)
        P1 = pt(cx, cy, r, math.degrees(s))
        X, Y = lerp(P0[0], P1[0], p), lerp(P0[1], P1[1], p)
        (path.moveTo if i == 0 else path.lineTo)(X, Y)
    pp = M.paint(cor, a, stroke=larg, cap_round=True); pp.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pp)


def regra3(c, t, cx, y, linhas, tl, size=84, cab=("graus", "radianos"), tcab=None, dy=150, cor2=None):
    """regra de três: [(esquerda, direita)] em duas colunas com seta; tl = instante de cada linha"""
    xl, xr = cx - 220, cx + 220
    if tcab is not None:
        E.foco(c, t, tcab, 0.4, lambda a: (centro(c, cab[0], xl, y - size * 1.1, 46, "i", TINTA2, a),
                                           centro(c, cab[1], xr, y - size * 1.1, 46, "i", TINTA2, a)))
    for i, ((s1, s2), t0) in enumerate(zip(linhas, tl)):
        yy = y + i * dy
        E.foco(c, t, t0, 0.5, lambda a, s1=s1, s2=s2, yy=yy: (
            E.formula(c, s1, xl, yy, size, "g", TINTA, a, "center"),
            M.arrow(c, xl + 110, yy - size * 0.3, xr - 110, yy - size * 0.3, TINTA2, a, 4, 16, 1.0),
            E.formula(c, s2, xr, yy, size, "g", cor2 or COR, a, "center")))


# ---------------- gancho ----------------
GX, GY_, GR = 1360, 560, 270


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.foco(c, t, a1, 0.5, lambda a: E.escreve(c, "390°", XE, 470, 230, "g", COR, a))
        E.frase(c, t, a1 + 1.4, ps("mais que", "i", 66) + [("uma volta", "g", 70)], XE, 590, "left", 0.1)
        ciclo(c, t, a1 + 0.2, GX, GY_, GR, rotulos=False)
        espiral(c, GX, GY_, GR - 40, 390, p=ease_io(prog(t, a1 + 1.4, max(1.0, b1 - a1 - 1.4))), passo=60)
        marca(c, t, b1, GX, GY_, GR, 30, "30°", fora=80)
        E.frase(c, t, b1 + 0.3, ps("cai no", "i", 66) + [("mesmo ponto", "g", 70, COR)] + ps("do 30°", "i", 66), XE, 720, "left", 0.1)
        E.foco(c, t, c1, 0.5, lambda a: (E.escreve(c, "e a prova escreve", XE, 880, 60, "i", TINTA2, a),
                                         E.formula(c, "f{π}{3}", XE + 520, 890, 100, "g", COR, a)))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 280, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), [("graus", "g", 100, COR)] + ps("e", "i", 90) + [("radianos", "g", 100, COR)], XE, 440, passo=0.14)
        E.frase(c, t, tb, ps("qualquer arco no", "i", 80) + [("ciclo", "g", 96, COR)], XE, 600, passo=0.12)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 545, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 630, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "plano cartesiano", "x, y e 4 quadrantes"), ("s03.c", "arco e volta", "volta = 2πr"), ("s03.d", "a regra de", "três"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, l2=l2, y=y: E.formula(c, l2, x + 44, y + 164, 64, "g", COR, a))
    alvo = [C[k] for k, _, _ in itens]
    q1, q2 = ease_io(prog(t, alvo[1] - 0.35, 0.5)), ease_io(prog(t, alvo[2] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(340, 580, q1), 820, q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 900, 1000, "left", 0.12)


# ---------------- radiano ----------------
RX, RY, RR = 560, 560, 300


def b_radiano(c, t, C, b):
    a4, b4, c4 = (C[f"s04.{k}"] for k in "abc")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    X = 1400
    ent = C["s04"]
    # a circunferência e o raio
    q = ep(t, ent + 0.2, 0.6)
    if q > 0:
        c.drawArc(skia.Rect.MakeXYWH(RX - RR, RY - RR, 2 * RR, 2 * RR), 0, -360 * ease_io(prog(t, ent + 0.2, 0.9)), False, M.paint(TINTA, 1.0, stroke=5))
        c.drawCircle(RX, RY, 9, M.paint(TINTA, q))
    if t >= b4:
        M.line(c, RX, RY, RX + RR, RY, TINTA, 1.0, 6, progress=ease_io(prog(t, b4, 0.5)))
        E.foco(c, t, b4 + 0.3, 0.4, lambda a: centro(c, "r", RX + RR / 2, RY + 60, 60, "i", TINTA, a))
        # o raio copiado se dobra sobre a circunferência
        k = ep(t, b4 + 0.6, 0.3) * (1 - ep(t, C["s06"] - 0.4, 0.4))
        raio_dobra(c, RX, RY, RR, ease_io(prog(t, b4 + 1.0, 1.4)), AMBAR, k)
        E.foco(c, t, b4 + 2.4, 0.4, lambda a: E.escreve(c, "arco = r", RX + RR + 40, RY - 160, 54, "b", AMBAR,
                                                         a * (1 - ep(t, C["s05"] - 0.3, 0.3))))
    if t >= c4:  # o ângulo de 1 rad
        k = 1 - ep(t, C["s06"] - 0.4, 0.4)
        ra = 110
        path = skia.Path(); path.moveTo(RX, RY); path.arcTo(skia.Rect.MakeXYWH(RX - ra, RY - ra, 2 * ra, 2 * ra), 0, -math.degrees(1) * ep(t, c4, 0.5), False); path.close()
        c.drawPath(path, M.paint(E.COR, 0.22 * k))
        M.line(c, RX, RY, *pt(RX, RY, RR, math.degrees(1)), TINTA, k, 6, progress=ep(t, c4, 0.5))
        E.foco(c, t, c4 + 0.4, 0.4, lambda a: E._meio(c, "1 rad", *pt(RX, RY, 160, 28), 50, "b", COR, a * k))
    if t >= b5:  # os radianos em volta da circunferência
        k = 1 - ep(t, C["s06"] - 0.4, 0.4)
        for i in range(1, 7):
            if t >= b5 + 0.25 * i:
                ang = math.degrees(i)
                P1, P2 = pt(RX, RY, RR - 24, ang), pt(RX, RY, RR + 24, ang)
                M.line(c, *P1, *P2, AMBAR, k * ep(t, b5 + 0.25 * i, 0.3), 6)
                E.foco(c, t, b5 + 0.25 * i, 0.3, lambda a, i=i, ang=ang: centro(c, str(i), *(lambda P: (P[0], P[1] + 18))(pt(RX, RY, RR + 62, ang)), 46, "b", AMBAR, a * k))
        arco(c, RX, RY, RR, 0, 360, AMBAR, 8, ease_io(prog(t, b5, 1.6)), k * 0.6, seta=False)

    def quatro_cinco():
        E.frase(c, t, a4, ps("outro jeito:", "i", 64) + [("pelo arco", "g", 70, COR)], X, 220, "center", 0.1)
        E.frase(c, t, b4, ps("arco do tamanho", "i", 58) + [("do raio", "g", 62, AMBAR)], X, 360, "center", 0.1)
        resp(c, t, c4, "ângulo = 1 rad", X, 520, 64)
    E.saida(c, t, C["s05"] - 0.1, quatro_cinco)
    if C["s05"] - 0.1 <= t:
        def cinco():
            E.frase(c, t, C["s05"] + 0.1, ps("quantos cabem", "i", 62) + [("numa volta?", "g", 66, COR)], X, 200, "center", 0.1)
            fcen(c, t, a5, "volta = 2πr", X, 350, 84)
            E.frase(c, t, b5, ps("cada radiano:", "i", 58) + [("arco r", "g", 62, AMBAR)], X, 490, "center", 0.1)
            fcen(c, t, c5, "f{2πr}{r} = 2π", X, 680, 96)
            resp(c, t, d5, "volta = 2π rad", X, 880, 68)
        E.saida(c, t, C["s06"] - 0.1, cinco)
    if t < C["s06"] - 0.1:
        return
    # s06: volta e meia volta
    arco(c, RX, RY, RR, 0, 360, E.COR, 10, ease_io(prog(t, a6, 1.0)), 1 - 0.75 * ep(t, b6, 0.4), seta=False)
    arco(c, RX, RY, RR + 30, 0, 180, AMBAR, 12, ease_io(prog(t, b6, 0.8)))
    E.foco(c, t, b6 + 0.6, 0.4, lambda a: (M.line(c, RX - RR, RY, RX + RR, RY, TINTA, a, 5), c.drawCircle(RX, RY, 9, M.paint(TINTA, a))))
    fcen(c, t, a6, "360° = 2π rad", X, 230, 80)
    fcen(c, t, b6, "180° = π rad", X, 380, 80, AMBAR)
    E.foco(c, t, c6, 0.5, lambda a: E.caixa_pontilhada(c, X - 330, 500, 660, 200, a, COR, prog_=ep(t, c6, 0.6)))
    fcen(c, t, c6 + 0.1, "π rad = 180°", X, 640, 104, COR)
    E.frase(c, t, d6, [("1 rad", "g", 62)] + ps("≈", "b", 62) + [("57°", "g", 62, COR)], X, 860, "center", 0.1)
    E.frase(c, t, d6 + 0.6, ps("pouco mais de 57°", "i", 50, TINTA2), X, 950, "center", 0.1)


# ---------------- converter ----------------
def b_converter(c, t, C, b):
    a7, b7, c7 = (C[f"s07.{k}"] for k in "abc")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    cx = 620
    E.frase(c, t, a7, ps("para converter,", "i", 66) + [("regra de três", "g", 70, COR)], cx, 170, "center", 0.1)
    regra3(c, t, cx, 420, [("180°", "π"), ("60°", "x")], [b7, c7], 96, tcab=b7)
    if t >= a8:  # a cruz
        q = ep(t, a8, 0.5)
        M.line(c, cx - 220 + 70, 410 - 40, cx + 220 - 50, 560 - 40, CERTO, q, 5, progress=q)
        M.line(c, cx - 220 + 70, 560 - 40, cx + 220 - 50, 410 - 40, CERTO, q, 5, progress=q)
    X = 1440
    fcen(c, t, a8, "180 · x = 60 · π", X, 300, 84)
    fcen(c, t, b8, "x = f{60π}{180}", X, 480, 96)
    fcen(c, t, c8, "f{60}{180} = f{1}{3}", X, 680, 84, TINTA2)
    resp(c, t, d8, "60° = f{π}{3} rad", 960, 920, 70, 2.5)


# ---------------- ciclo ----------------
CX, CY, CR = 600, 560, 310


def b_ciclo(c, t, C, b):
    a9, b9 = C["s09.a"], C["s09.b"]
    a0, b0 = C["s10.a"], C["s10.b"]
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    X = 1420
    ciclo(c, t, a9, CX, CY, CR, tq=b9)
    E.foco(c, t, a9 + 0.8, 0.4, lambda a: (c.drawCircle(CX, CY, 9, M.paint(TINTA, a)), E.escreve(c, "O", CX - 50, CY + 50, 48, "g", TINTA, a),
                                           E.escreve(c, "1", CX + CR + 12, CY + 52, 46, "b", TINTA, a), E.escreve(c, "−1", CX - CR - 70, CY + 52, 46, "b", TINTA, a),
                                           E.escreve(c, "1", CX - 40, CY - CR - 10, 46, "b", TINTA, a), E.escreve(c, "−1", CX - 70, CY + CR + 50, 46, "b", TINTA, a)))
    # partida e sentido
    if t >= a0:
        k = ease_back(prog(t, a0, 0.5))
        c.drawCircle(CX + CR, CY, 22 * k, M.paint(CERTO, 0.3))
        c.drawCircle(CX + CR, CY, 12 * k, M.paint(CERTO))
    sent_a = 1 - ep(t, a1 - 0.3, 0.4)
    arco(c, CX, CY, CR + 50, 10, 70, TINTA2, 7, ease_io(prog(t, b0, 0.8)), sent_a)
    # os arcos marcados
    if t >= a1:
        fim = 60 if t < b1 else 90 if t < c1 else 180 if t < d1 else 270
        ini = {60: (0, a1), 90: (60, b1), 180: (90, c1), 270: (180, d1)}[fim]
        arco(c, CX, CY, CR, 0, ini[0], E.COR, 12, 1.0, 1.0, seta=False)
        arco(c, CX, CY, CR, ini[0], fim, E.COR, 12, ease_io(prog(t, ini[1], 0.6)))
    marca(c, t, a1 + 0.6, CX, CY, CR, 60, "60°", fora=64)
    # graus em índigo e radianos em âmbar, cada par de um lado do ponto
    lug = {90: ((470, 215), (700, 195)), 180: ((205, 505), (205, 680)), 270: ((700, 945), (470, 930))}
    for ang, rot, tk, rr in ((90, "90°", b1, "f{π}{2}"), (180, "180°", c1, "π"), (270, "270°", d1, "f{3π}{2}")):
        marca(c, t, tk + 0.4, CX, CY, CR, ang, None)
        (Xr, Yr), (Xr2, Yr2) = lug[ang]
        E.foco(c, t, tk + 0.5, 0.4, lambda a, Xr=Xr, Yr=Yr, rot=rot: E.formula(c, rot, Xr, Yr, 50, "g", COR, a, "center"))
        E.foco(c, t, e1 + 0.5 * [90, 180, 270].index(ang), 0.4, lambda a, Xr2=Xr2, Yr2=Yr2, s=rr: E.formula(c, s, Xr2, Yr2, 50, "g", AMBAR, a, "center"))

    def nove_dez():
        E.frase(c, t, C["s09"] + 0.2, ps("o", "i", 70) + [("ciclo", "g", 80, COR)] + ps("trigonométrico", "i", 70), X, 220, "center", 0.1)
        E.frase(c, t, a9, ps("raio", "i", 60) + [("1", "g", 66, COR)] + ps("e centro", "i", 60) + [("na origem", "g", 62)], X, 360, "center", 0.1)
        E.frase(c, t, b9, [("4 quadrantes", "g", 64, COR)], X, 480, "center", 0.1)
        E.frase(c, t, a0, ps("começa", "i", 60) + [("à direita", "g", 64, CERTO)], X, 640, "center", 0.1)
        E.frase(c, t, b0, ps("gira no", "i", 60) + [("anti-horário", "g", 64, COR)], X, 760, "center", 0.1)
        E.frase(c, t, b0 + 1.2, ps("o contrário do relógio, subindo", "i", 50, TINTA2), X, 850, "center", 0.08)
    E.saida(c, t, a1 - 0.2, nove_dez)
    if t >= a1 - 0.2:
        E.frase(c, t, a1, ps("marque", "i", 62) + [("60°", "g", 70, COR)], X, 220, "center", 0.1)
        E.frase(c, t, a1 + 1.0, ps("2/3 do caminho até o topo", "i", 52, TINTA2), X, 310, "center", 0.08)
        E.frase(c, t, b1, [("90°", "g", 64, COR)] + ps("o topo", "i", 58), X, 450, "center", 0.1)
        E.frase(c, t, c1, [("180°", "g", 64, COR)] + ps("a esquerda", "i", 58), X, 560, "center", 0.1)
        E.frase(c, t, d1, [("270°", "g", 64, COR)] + ps("embaixo", "i", 58), X, 670, "center", 0.1)
        E.frase(c, t, e1, ps("em radianos:", "i", 56, AMBAR), X, 800, "center", 0.1)
        E.foco(c, t, e1 + 0.4, 0.5, lambda a: E.formula(c, "f{π}{2},  π,  f{3π}{2}", X, 930, 72, "g", AMBAR, a, "center"))


# ---------------- mais de uma volta ----------------
def b_voltas(c, t, C, b):
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    a3, b3, c3 = (C[f"s13.{k}"] for k in "abc")
    X = 1420
    ciclo(c, t, C["s12"] - 0.3, CX, CY, CR - 40, tq=None)

    def doze():
        espiral(c, CX, CY, CR - 90, 360, E.COR, 10, ease_io(prog(t, a2, 1.2)), 1 - ep(t, c2 - 0.3, 0.3), passo=0)
        espiral(c, CX, CY, CR - 90, 390, E.COR, 10, ease_io(prog(t, c2, 2.0)), 1.0, passo=70)
        marca(c, t, d2, CX, CY, CR - 40, 30, "30°", fora=90)
        E.frase(c, t, a2, ps("uma volta =", "i", 62) + [("360°", "g", 68, COR)], X, 260, "center", 0.1)
        fcen(c, t, b2, "390 − 360 = 30", X, 430, 90)
        E.frase(c, t, c2, ps("1 volta completa", "i", 58) + [("+ 30°", "g", 62, COR)], X, 600, "center", 0.1)
        resp(c, t, d2, "390° → ponto do 30°", X, 780, 60)
    E.saida(c, t, C["s13"] - 0.1, doze)
    if t < C["s13"] - 0.1:
        return
    espiral(c, CX, CY, CR - 120, 750, E.COR, 9, ease_io(prog(t, b3, max(1.5, c3 - b3))), 1.0, passo=55)
    marca(c, t, c3 + 0.4, CX, CY, CR - 40, 30, "30°", fora=90)
    E.frase(c, t, a3, ps("maior que uma volta:", "i", 56), X, 240, "center", 0.1)
    E.frase(c, t, a3 + 1.0, [("tire 360°", "g", 66, COR)], X, 330, "center", 0.1)
    E.frase(c, t, a3 + 1.6, ps("até ficar abaixo de 360°", "i", 52, TINTA2), X, 410, "center", 0.08)
    fcen(c, t, b3, "750 − 360 = 390", X, 580, 84)
    fcen(c, t, c3, "390 − 360 = 30", X, 740, 84, COR)
    E.frase(c, t, c3 + 1.2, [("mesmo ponto", "g", 62, CERTO)], X, 880, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    X = 1420
    ciclo(c, t, C["s14"] - 0.3, CX, CY, CR, tq=C["s14"])
    arco(c, CX, CY, CR, 0, -30, ERRADO, 12, ease_io(prog(t, a4, 0.8)))
    marca(c, t, b4, CX, CY, CR, -30, "30°?" if t < d4 else "−30°", ERRADO, fora=80)
    arco(c, CX, CY, CR, 0, 30, CERTO, 12, ease_io(prog(t, c4, 0.8)))
    marca(c, t, c4 + 0.6, CX, CY, CR, 30, "30°", CERTO, fora=80)
    E.frase(c, t, a4, ps("o erro:", "i", 62) + [("girar no sentido do relógio", "g", 56, ERRADO)], X, 230, "center", 0.1)
    E.frase(c, t, b4, ps("30° embaixo, no", "i", 56, ERRADO) + [("4º quadrante", "g", 58, ERRADO)], X, 360, "center", 0.1)

    E.frase(c, t, c4, ps("o certo:", "i", 60) + [("subir", "g", 66, CERTO)], X, 520, "center", 0.1)
    E.frase(c, t, c4 + 0.9, [("30°", "g", 60, CERTO)] + ps("no 1º quadrante", "i", 56), X, 610, "center", 0.1)
    E.frase(c, t, d4 - 2.2, ps("no sentido do relógio,", "i", 54, TINTA2), X, 770, "center", 0.08)
    E.frase(c, t, d4 - 1.4, ps("o ângulo ganha sinal", "i", 54, TINTA2), X, 840, "center", 0.08)
    resp(c, t, d4, "aquele ponto = −30°", X, 960, 54, cor=ERRADO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a5, b5, c5 = (C[f"s15.{k}"] for k in "abc")
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    a7, b7, c7 = (C[f"s17.{k}"] for k in "abc")

    def quinze():
        E.frase(c, t, C["s15"] + 0.1, ps("agora o atalho", "i", 60, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a5, [("rad", "i", 66, CLARO), ("→", "b", 60, CLARO), ("grau:", "i", 66, CLARO)] + ps("troque", "i", 66, CLARO) + [("π por 180°", "g", 76, BR)], W / 2, 320, "center", 0.12)
        fcen(c, t, b5, "f{π}{3} → f{180°}{3} = 60°", W / 2, 540, 96, BR)
        fcen(c, t, c5, "f{3π}{4} → f{3 · 180°}{4} = f{540°}{4} = 135°", W / 2, 820, 84, BR)
    E.saida(c, t, C["s16"] - 0.1, quinze)

    def dezesseis():
        E.frase(c, t, C["s16"] + 0.1, [("grau", "i", 66, CLARO), ("→", "b", 60, CLARO), ("rad:", "i", 66, CLARO)], W / 2, 180, "center", 0.1)
        E.frase(c, t, a6, ps("quantas vezes cabe em", "i", 66, CLARO) + [("180°?", "g", 76, BR)], W / 2, 300, "center", 0.12)
        fcen(c, t, b6, "180 ÷ 60 = 3  →  f{π}{3}", W / 2, 480, 84, BR)
        fcen(c, t, c6, "180 ÷ 45 = 4  →  f{π}{4}", W / 2, 680, 84, BR)
        E.foco(c, t, d6, 0.5, lambda a: E.selo(c, 470, 860, 42, False, a))
        E.frase(c, t, d6, [("120°?", "g", 70, BR)] + ps("não cabe inteiro:", "i", 60, CLARO) + [("regra de três", "g", 64, BR)], 540, 885, "left", 0.1)
    if t >= C["s16"] - 0.1:
        E.saida(c, t, C["s17"] - 0.1, dezesseis)
    if t < C["s17"] - 0.1:
        return
    E.frase(c, t, a7, ps("funciona porque", "i", 62, CLARO), W / 2, 220, "center", 0.1)
    fcen(c, t, a7 + 0.8, "π rad = 180°", W / 2, 390, 110, BR)
    E.frase(c, t, b7, ps("só quando o", "i", 60, CLARO) + [("π", "b", 58, BR)] + ps("é um", "i", 60, CLARO) + [("ângulo", "g", 66, BR)], W / 2, 560, "center", 0.1)
    E.foco(c, t, c7, 0.5, lambda a: E.formula(c, "volta = 2πr", W / 2 - 250, 760, 80, "g", CLARO, a, "center"))
    E.foco(c, t, c7 + 0.8, 0.5, lambda a: E.formula(c, "π ≈ 3,14", W / 2 + 300, 760, 80, "g", AMBAR, a, "center"))
    E.frase(c, t, c7 + 1.4, ps("aqui o", "i", 56, CLARO) + [("π", "b", 54, AMBAR)] + ps("é um número,", "i", 56, CLARO) + [("não 180", "g", 60, BR)], W / 2, 900, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a8, b8 = C["s18.a"], C["s18.b"]
    E.frase(c, t, C["s18"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.foco(c, t, a8, 0.5, lambda a: (centro(c, "1", XE + 40, 380, 60, "g", COR, a)))
    E.frase(c, t, a8, ps("120° em", "i", 74) + [("radianos", "g", 80, COR)], XE + 110, 380, "left", 0.1)
    E.foco(c, t, b8, 0.5, lambda a: (centro(c, "2", XE + 40, 560, 60, "g", COR, a)))
    E.frase(c, t, b8, ps("480°: que", "i", 74) + [("quadrante?", "g", 80, COR)], XE + 110, 560, "left", 0.1)
    E.relogio(c, t, C["s19.a"], 1520, 440, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    a1, b1, c1, d1 = (C[f"s21.{k}"] for k in "abcd")

    def vinte():
        E.frase(c, t, C["s20"] + 0.1, ps("vamos lá", "i", 64, COR), 620, 160, "center", 0.1)
        regra3(c, t, 620, 400, [("180°", "π"), ("120°", "x")], [a0, a0 + 1.2], 90, tcab=a0)
        X = 1420
        fcen(c, t, b0, "x = f{120π}{180}", X, 320, 90)
        fcen(c, t, c0, "f{120}{180} = f{2}{3}", X, 540, 84, TINTA2)
        E.frase(c, t, c0 - 0.8, ps("÷ 60 em cima e embaixo", "i", 46, TINTA2), X, 420, "center", 0.08)
        resp(c, t, d0, "120° = f{2π}{3} rad", 960, 850, 68, 2.5)
    E.saida(c, t, C["s21"] - 0.1, vinte)
    if t < C["s21"] - 0.1:
        return
    X = 1440
    fcen(c, t, a1, "f{2 · 180°}{3} = f{360°}{3} = 120°", X, 250, 72, CERTO)
    E.foco(c, t, a1 + 2.6, 0.5, lambda a: E.selo(c, X + 380, 230, 34, True, a))
    ciclo(c, t, C["s21"], CX, CY + 40, CR - 30, tq=c1)
    fcen(c, t, b1, "480 − 360 = 120", X, 470, 84)
    if t >= b1:
        arco(c, CX, CY + 40, CR - 30, 0, 120, E.COR, 12, ease_io(prog(t, b1 + 0.6, 0.9)))
        marca(c, t, b1 + 1.5, CX, CY + 40, CR - 30, 120, "120°", fora=80)
    if t >= c1:  # o 2º quadrante aceso
        k = ep(t, c1, 0.5)
        r = CR - 30
        path = skia.Path(); path.moveTo(CX, CY + 40); path.arcTo(skia.Rect.MakeXYWH(CX - r, CY + 40 - r, 2 * r, 2 * r), -90, -90, False); path.close()
        c.drawPath(path, M.paint(E.COR, 0.12 * k))
    E.frase(c, t, c1, ps("entre", "i", 58) + [("90° e 180°", "g", 64, COR)], X, 640, "center", 0.1)
    resp(c, t, d1, "2º quadrante", X, 820, 70)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s22.a", "π rad =", "180°"), ("s22.b", "no ciclo: à direita,", "anti-horário"), ("s22.c", "a cada volta inteira,", "o mesmo ponto"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 68) + [(l2, "g", 70, COR)], 320, y, "left", 0.1)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a3, b3, c3 = C["s23.a"], C["s23.b"], C["s23.c"]
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula, o ciclo ganha", "i", 70), XE, 200, passo=0.1)
    E.frase(c, t, C["s23"] + 1.4, [("seno e cosseno", "g", 80, COR)], XE, 310, passo=0.1)
    E.frase(c, t, a3, ps("sen no eixo", "i", 60) + [("vertical,", "g", 64)] + ps("cos no", "i", 60) + [("horizontal", "g", 64)], XE, 440, passo=0.1)
    E.foco(c, t, b3, 0.5, lambda a: E.formula(c, "sen 90° = 1      cos 180° = −1", XE, 570, 66, "g", COR, a))
    E.frase(c, t, c3, ps("e o", "i", 60) + [("sinal", "g", 66, COR)] + ps("em cada quadrante", "i", 60), XE, 690, passo=0.1)
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s23.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1030, 815, p), ep(t, C["s23.d"] + 0.2, 0.4))
    E.frase(c, t, C["s23.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, radiano=b_radiano, converter=b_converter, ciclo=b_ciclo, voltas=b_voltas,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
