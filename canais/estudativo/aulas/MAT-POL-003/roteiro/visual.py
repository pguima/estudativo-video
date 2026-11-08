"""Visual — Estudativo · MAT-POL-003: polígonos regulares (ângulo interno, externo) e pisos.
Linguagem da geometria plana (MAT-ANG-001 a 007, MAT-POL-001/002): lados em tinta; o ângulo INTERNO da vez em COR (índigo, arco
e cunha clara), o EXTERNO em TINTA2 (cinza escuro), com o prolongamento do lado tracejado; lados iguais com tracinhos;
medidas na grotesca; resposta na esfera; vermelho é erro (buraco, peça sobre peça), verde é certo.
Pisos: cada peça é um polígono regular que encosta um vértice no ponto do encontro; o canto de cada peça no ponto é uma cunha,
e as cunhas lado a lado mostram se a volta fecha (360°), sobra buraco ou passa da volta.
Peças locais: peca() (polígono regular com um vértice no ponto O, ocupando o canto de θ a θ + interno), canto() (cunha no ponto),
reg() (pontos do polígono regular de E.regular), favo() (hexágonos de E.regular lado a lado), caminhante() (a volta pela borda).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polígonos e Círculo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POL-003_poligonos_regulares_e_pisos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("regular", "externo", "atalho", "piso", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
assert 6 * 180 == 1080 and 1080 / 8 == 135 and 720 / 6 == 120 and 540 / 5 == 108
assert 180 - 135 == 45 and 8 * 45 == 360 and 360 / 8 == 45
assert 3 * 120 == 360 and 3 * 108 == 324 and 360 - 324 == 36 and 4 * 108 == 432
assert 360 / 60 == 6 and 360 / 90 == 4 and 360 / 120 == 3
assert 360 / 12 == 30 and 180 - 30 == 150 and 150 + 150 == 300 and 360 - 300 == 60 and 10 * 180 == 1800 and 1800 / 12 == 150


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
                                     centro(c, s, cx, cy + size * 0.36, size, "g", BR, a)))


def pt(V, L, g):
    return V[0] + L * math.cos(math.radians(g)), V[1] - L * math.sin(math.radians(g))


def reg(n, cx, cy, r, giro=0.0):
    """os mesmos pontos de E.regular: um lado deitado embaixo, em volta no sentido do relógio na tela"""
    ini = 90 - 180 / n + giro
    return [(cx + r * math.cos(math.radians(ini + k * 360 / n)), cy + r * math.sin(math.radians(ini + k * 360 / n))) for k in range(n)]


def interno(n):
    return 180 - 360 / n


def peca_pts(n, O, theta, L):
    """polígono regular de lado L com um vértice em O; o canto em O vai da direção theta até theta + interno (graus da matemática)"""
    pts, P, h = [O], O, theta
    for _ in range(n - 1):
        P = pt(P, L, h)
        pts.append(P)
        h += 360 / n
    return pts


def canto(c, O, g1, g2, r, cor, a=1.0, alfa=0.35, borda=5):
    """cunha no ponto O de g1 até g2 (graus da matemática, anti-horário)"""
    if a <= 0 or abs(g2 - g1) < 0.1:
        return
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    path = skia.Path(); path.moveTo(*O); path.arcTo(ret, -g1, -(g2 - g1), False); path.close()
    c.drawPath(path, M.paint(cor, alfa * a))
    if borda:
        c.drawArc(ret, -g1, -(g2 - g1), False, M.paint(cor, a, stroke=borda, cap_round=True))


def peca(c, t, t0, n, O, theta, L, cor=None, d=0.6, preenche=0.1, escuro=False, a=1.0):
    if t < t0 or a <= 0:
        return
    if a < 1:
        c.saveLayerAlpha(None, int(255 * a))
    E.poligono(c, t, t0, peca_pts(n, O, theta, L), None, cor=cor, preenche=preenche, d=d, escuro=escuro)
    if a < 1:
        c.restore()


def lin(c, t, t0, P, Q, cor=TINTA, larg=6, d=0.5, a=1.0, dash=None):
    if t >= t0 and a > 0:
        M.line(c, *P, *Q, cor, a, larg, dash=dash, progress=ease_io(prog(t, t0, d)))


def favo(c, t, t0, x0, y0, r, cols, lins, passo=0.08, cor=None, escuro=False, a=1.0):
    """hexágonos regulares (E.regular) lado a lado, sem buraco"""
    if a <= 0 or t < t0:
        return
    if a < 1:
        c.saveLayerAlpha(None, int(255 * a))
    k = 0
    for i in range(cols):
        for j in range(lins):
            cx = x0 + 1.5 * r * i
            cy = y0 + math.sqrt(3) * r * (j + 0.5 * (i % 2))
            E.regular(c, t, t0 + passo * k, 6, cx, cy, r, preenche=0.14, d=0.4, cor=cor, escuro=escuro, largura=5)
            k += 1
    if a < 1:
        c.restore()


def ang_int(c, t, t0, P, i, rot=None, cor=None, r=70, size=54):
    """ângulo interno do vértice i do polígono P"""
    E.angulo(c, t, t0, P[i], P[i - 1], P[(i + 1) % len(P)], rot, r=r, cor=cor, size=size)


def poli(c, t, t0, P, nomes=None, d=0.8, escuro=False, preenche=0.06, size=56, iguais=None, a=1.0):
    if a <= 0 or t < t0:
        return
    if a < 1:
        c.saveLayerAlpha(None, int(255 * a))
    E.poligono(c, t, t0, P, list(nomes) if nomes else None, preenche=preenche, d=d, escuro=escuro, size=size, iguais=iguais)
    if a < 1:
        c.restore()


def rotulo_em(c, t, t0, s, x, y, size, cor, a=1.0):
    E.foco(c, t, t0, 0.4, lambda f: E._meio(c, s, x, y, size, "b", cor, f * a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def um():
        favo(c, t, ka, 200, 360, 92, 5, 3, 0.06, cor=AMBAR)
        E.frase(c, t, ka, ps("favo de", "i", 76) + [("mel", "g", 80, AMBAR)], 520, 190, "center", 0.12)
        E.frase(c, t, kb, [("hexágonos", "g", 66, COR)] + ps("sem buracos", "i", 62), 520, 1000, "center", 0.12)
        O = (1450, 560)
        for k in range(3):
            peca(c, t, kc + 0.3 * k, 5, O, 108 * k + 90, 190, d=0.5)
        if t >= kc + 1.0:
            canto(c, O, 90 + 324, 90 + 360, 150, ERRADO, ep(t, kc + 1.0, 0.4), 0.45)
        E.frase(c, t, kc, ps("e", "i", 76) + [("pentágonos?", "g", 80, COR)], 1450, 190, "center", 0.12)
        E.foco(c, t, kd, 0.5, lambda a: E.pilula(c, "1 ângulo decide", 1450, 1000, 54, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1520, 560, 240 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 280, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), [("o ângulo", "g", 96, COR)] + ps("de qualquer", "i", 84), XE, 420, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("polígono", "i", 84) + [("regular", "g", 96, COR)], XE, 530, passo=0.14)
        E.frase(c, t, tb, ps("o piso", "i", 84) + [("sem buracos", "g", 96)], XE, 700, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1520, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1520, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    for k, l1, y in (("s03.b", "soma dos ângulos internos:", 150), ("s03.c", "ângulo externo:", 500)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 300, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 52)], x + 44, y + 80)
    E.formula_em(c, t, C["s03.b"] + 0.6, "S = (n − 2) × 180°", x + 44, 330, 70, "g", COR)
    E.frase(c, t, C["s03.c"] + 0.6, [("prolongue", "g", 60, COR)], x + 44, 680)
    E.frase(c, t, C["s03.c"] + 0.9, [("um lado", "g", 60, COR)], x + 44, 760)
    # mini figura: um canto com o lado prolongado
    V = (1500, 700)
    tc = C["s03.c"] + 0.8
    lin(c, t, tc, (1300, 700), V, TINTA, 6)
    lin(c, t, tc + 0.2, V, pt(V, 170, 60), TINTA, 6)
    lin(c, t, tc + 0.6, V, (1730, 700), TINTA2, 5, dash=E.TRACO)
    if t >= tc + 1.0:
        canto(c, V, 0, 60, 70, TINTA2, ep(t, tc + 1.0, 0.4), 0.35)
        canto(c, V, 60, 180, 50, E.COR, ep(t, tc + 1.0, 0.4), 0.25)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(150 + 270, 500 + 270, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 930, "left", 0.12)


# ---------------- regular ----------------
def b_regular(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]

    def quatro():
        E.frase(c, t, a4, [("regular:", "g", 70, COR)] + ps("lados iguais", "i", 64) + [("e", "g", 64, COR)] + ps("ângulos iguais", "i", 64),
                W / 2, 170, "center", 0.12)
        Lz = [(170, 560), (400, 660), (630, 560), (400, 460)]
        poli(c, t, b4, Lz, None, d=0.6, iguais=[1, 1, 1, 1])
        ang_int(c, t, b4 + 0.6, Lz, 0, None, None, 70)
        ang_int(c, t, b4 + 0.8, Lz, 1, None, TINTA2, 50)
        E.frase(c, t, b4 + 0.4, [("losango", "g", 60, COR)], 400, 800, "center")
        E.frase(c, t, b4 + 0.8, ps("ângulos diferentes", "i", 44, ERRADO), 400, 870, "center", 0.1)
        E.foco(c, t, b4 + 1.2, 0.4, lambda a: E.selo(c, 400, 960, 40 * ease_back(prog(t, b4 + 1.2, 0.4)), False, a))
        R = [(760, 640), (1160, 640), (1160, 480), (760, 480)]
        poli(c, t, c4, R, None, d=0.6)
        for i in range(4):
            ang_int(c, t, c4 + 0.6 + 0.1 * i, R, i, None, None, 44)
        E.frase(c, t, c4 + 0.4, [("retângulo", "g", 60, COR)], 960, 800, "center")
        E.frase(c, t, c4 + 0.8, ps("lados diferentes", "i", 44, ERRADO), 960, 870, "center", 0.1)
        E.foco(c, t, c4 + 1.2, 0.4, lambda a: E.selo(c, 960, 960, 40 * ease_back(prog(t, c4 + 1.2, 0.4)), False, a))
        Q = [(1420, 680), (1680, 680), (1680, 420), (1420, 420)]
        poli(c, t, d4, Q, None, d=0.6, iguais=[1, 1, 1, 1])
        for i in range(4):
            ang_int(c, t, d4 + 0.6 + 0.1 * i, Q, i, None, None, 44)
        E.frase(c, t, d4 + 0.4, [("quadrado", "g", 60, COR)], 1550, 800, "center")
        E.frase(c, t, d4 + 0.8, ps("quadrilátero regular", "i", 44, CERTO), 1550, 870, "center", 0.1)
        E.foco(c, t, d4 + 1.2, 0.4, lambda a: E.selo(c, 1550, 960, 40 * ease_back(prog(t, d4 + 1.2, 0.4)), True, a))
    E.saida(c, t, C["s05"] - 0.1, quatro)

    X = 1400
    if C["s05"] <= t < C["s06"] + 0.5:
        a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]

        def cinco():
            P = reg(8, 560, 580, 320)
            poli(c, t, C["s05"], P, None, d=0.8, iguais=[1] * 8)
            for i in range(8):
                ang_int(c, t, c5 + 0.6 + 0.08 * i, P, i, "135°" if i == 5 else None, None, 56, 50)
            E.frase(c, t, C["s05"] + 0.3, [("octógono", "g", 70, COR)] + ps("regular", "i", 66), X, 230, "center", 0.12)
            E.frase(c, t, a5, ps("cada ângulo =", "i", 62), X, 390, "center", 0.1)
            E.formula_em(c, t, a5 + 0.8, "f{soma}{n}", X, 520, 80, "g", COR, "center")
            fcen(c, t, b5, "6 × 180 = 1080", X, 700, 76)
            fcen(c, t, c5, "1080 ÷ 8 = 135°", X, 840, 76, COR)
        E.saida(c, t, C["s06"] - 0.1, cinco)
    if t >= C["s06"]:
        a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
        Hx = reg(6, 480, 480, 230)
        poli(c, t, C["s06"], Hx, None, d=0.7, iguais=[1] * 6)
        E.frase(c, t, C["s06"] + 0.2, [("hexágono", "g", 66, COR)], 480, 170, "center")
        for i in range(6):
            ang_int(c, t, b6 + 0.3 + 0.08 * i, Hx, i, "120°" if i == 2 else None, None, 52, 48)
        fcen(c, t, a6, "soma: 720", 480, 840, 66, TINTA2)
        fcen(c, t, b6, "720 ÷ 6 = 120°", 480, 960, 76, COR)
        Pn = reg(5, 1440, 500, 230)
        poli(c, t, c6 - 0.4, Pn, None, d=0.7, iguais=[1] * 5)
        E.frase(c, t, c6 - 0.2, [("pentágono", "g", 66, COR)], 1440, 170, "center")
        for i in range(5):
            ang_int(c, t, d6 + 0.3 + 0.08 * i, Pn, i, "108°" if i == 2 else None, None, 52, 48)
        fcen(c, t, c6, "soma: 540", 1440, 840, 66, TINTA2)
        fcen(c, t, d6, "540 ÷ 5 = 108°", 1440, 960, 76, COR)


# ---------------- externo ----------------
OCT = reg(8, 560, 560, 320)


def b_externo(c, t, C, b):
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    X = 1440
    # o lado de baixo (de OCT[1] até OCT[0], da esquerda para a direita) prolongado depois de OCT[0]
    V, Pv, Q = OCT[0], OCT[1], OCT[7]
    ext = (V[0] + 260, V[1])

    def sete():
        poli(c, t, C["s07"], OCT, None, d=0.8)
        lin(c, t, a7, V, ext, TINTA2, 5, 0.6, dash=E.TRACO)
        if t >= b7:
            canto(c, V, 0, 45, 90, TINTA2, ep(t, b7, 0.4), 0.35)
            rotulo_em(c, t, b7 + 0.3, "45°" if t >= d7 else "?", *pt(V, 150, 22), 54, TINTA2)
        ang_int(c, t, c7 - 0.3, OCT, 0, "135°", None, 70, 54)
        if t >= c7:
            M.line(c, Pv[0], Pv[1], ext[0], ext[1], E.COR, ep(t, c7, 0.4) * (1 - ep(t, C["s07.end"] - 0.3, 0.3)), 12)
        E.frase(c, t, a7, ps("prolongue", "i", 66) + [("1 lado", "g", 70, COR)], X, 260, "center", 0.12)
        E.frase(c, t, b7, [("externo", "g", 80, TINTA2)], X, 400, "center")
        E.frase(c, t, c7, ps("interno + externo =", "i", 60) + [("180°", "g", 66, COR)], X, 560, "center", 0.12)
        E.frase(c, t, c7 + 0.7, ps("(linha reta)", "i", 48, TINTA2), X, 640, "center")
        fcen(c, t, d7, "180 − 135 = 45°", X, 820, 90)
    E.saida(c, t, C["s08"] - 0.1, sete)

    if t >= C["s08"]:
        poli(c, t, C["s08"], OCT, None, d=0.6, preenche=0.04)
        # caminhando pela borda: em cada vértice, vira 45°
        u = 8 * ease_io(prog(t, a8, c8 - a8 + 0.6)) if t >= a8 else 0.0
        seq = [OCT[(1 - k) % 8] for k in range(9)]  # de OCT[1] para OCT[0], OCT[7], ... (anti-horário na tela)
        k = min(7, int(u))
        f = u - k
        P0, P1 = seq[k], seq[k + 1]
        pos = (lerp(P0[0], P1[0], f), lerp(P0[1], P1[1], f))
        for j in range(k + (1 if f > 0.98 else 0)):
            Vj = seq[j + 1]
            hj = math.degrees(math.atan2(-(seq[j + 1][1] - seq[j][1]), seq[j + 1][0] - seq[j][0]))
            if t >= b8:
                canto(c, Vj, hj, hj + 45, 46, TINTA2, ep(t, b8, 0.4), 0.45, 4)
        if a8 <= t < d8 + 1.0:
            al = 1 - ep(t, d8 + 0.6, 0.4)
            ux, uy = E._uni(*P0, *P1)
            c.drawCircle(*pos, 18, M.paint(E.COR, al))
            M.arrow(c, pos[0], pos[1], pos[0] + ux * 90, pos[1] + uy * 90, E.COR, al, 6, 18, al)
        E.frase(c, t, a8, ps("caminhe", "i", 66) + [("pela borda", "g", 70, COR)], X, 220, "center", 0.12)
        E.frase(c, t, b8, ps("em cada vértice, vira o", "i", 52) + [("externo", "g", 58, TINTA2)], X, 320, "center", 0.1)
        E.frase(c, t, c8, [("1 volta", "g", 70, COR)] + ps("completa", "i", 64), X, 430, "center", 0.12)
        # os 8 externos juntos no mesmo ponto
        Oc = (X, 700)
        for j in range(8):
            tj = c8 + 0.1 * j
            if t >= tj:
                canto(c, Oc, 45 * j, 45 * j + 45 * ease_io(prog(t, tj, 0.3)), 150, TINTA2 if j % 2 == 0 else E.COR, 1.0, 0.35, 3)
        fcen(c, t, d8, "8 × 45° = 360°", X, 940, 76, COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    X = 1400
    E.frase(c, t, C["s09"], [("cuidado", "g", 92, ERRADO)] + ps("com este erro", "i", 86), W / 2, 150, "center", 0.14)
    E.frase(c, t, a9, ps("trocar o", "i", 60) + [("externo", "g", 64, TINTA2)] + ps("pelo", "i", 60) + [("interno", "g", 64, COR)],
            W / 2, 260, "center", 0.12)
    fcen(c, t, b9, "360 ÷ 8 = 45°", X, 430, 84, ERRADO)
    E.frase(c, t, b9 + 1.2, ps("“é o ângulo do octógono”", "i", 52, ERRADO), X, 520, "center", 0.1)
    # 45° é agudo
    V = (1180, 820)
    if t >= c9:
        lin(c, t, c9, V, (V[0] + 300, V[1]), TINTA, 6)
        lin(c, t, c9 + 0.2, V, pt(V, 300, 45), TINTA, 6)
        canto(c, V, 0, 45, 120, ERRADO, ep(t, c9 + 0.4, 0.4), 0.3)
        E.frase(c, t, c9 + 0.4, [("agudo", "g", 64, ERRADO)], 1620, 800, "center")
    P = reg(8, 520, 640, 300)
    poli(c, t, C["s09"] + 0.6, P, None, d=0.8)
    if t >= d9:
        for i in range(8):
            ang_int(c, t, d9 + 0.06 * i, P, i, "135°" if i == 5 else None, None, 60, 50)
        E.frase(c, t, d9 + 0.4, ps("cantos", "i", 60) + [("obtusos", "g", 64, COR)], 520, 1020, "center", 0.12)
        E.foco(c, t, d9 + 1.4, 0.4, lambda a: E.pilula(c, "45° é o externo", 1560, 960, 46, "g", fundo=TINTA, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a10, b10, c10, d10, e10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s10.e"]
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]

    def dez():
        E.frase(c, t, a10, ps("comece pelo", "i", 84, CLARO) + [("externo", "g", 96, BR)], W / 2, 200, "center", 0.12)
        E.formula_em(c, t, b10, "externo = f{360}{n}", W / 2, 400, 90, "g", BR, "center")
        E.formula_em(c, t, c10, "interno = 180 − externo", W / 2, 560, 84, "g", CLARO, "center")
        E.frase(c, t, d10 - 0.2, [("octógono:", "i", 64, CLARO)], 420, 760, "center")
        fcen(c, t, d10, "360 ÷ 8 = 45", 1100, 760, 80, BR)
        fcen(c, t, e10, "180 − 45 = 135°", 1100, 900, 90, CLARO)
    E.saida(c, t, C["s11"] - 0.1, dez)
    if t >= C["s11"]:
        E.frase(c, t, a11, ps("a volta é sempre", "i", 72, CLARO) + [("360°", "g", 84, BR)], W / 2, 220, "center", 0.12)
        E.frase(c, t, a11 + 1.2, ps("e a conta fica menor", "i", 60, CLARO), W / 2, 320, "center", 0.12)
        E.foco(c, t, b11, 0.5, lambda a: E.pilula(c, "só para polígono regular", W / 2, 450, 56, "g", fundo=E.mix(E.COR, BR, 0.25), a=a))
        # irregular: externos diferentes, soma 360
        P = [(560, 860), (980, 900), (1120, 640), (820, 560), (500, 660)]
        poli(c, t, c11 - 0.3, P, None, d=0.6, escuro=True, preenche=0.0)
        if t >= c11:
            for i in range(5):
                Vi, Vp = P[i], P[i - 1]
                ux, uy = E._uni(*Vp, *Vi)
                lin(c, t, c11 + 0.15 * i, Vi, (Vi[0] + ux * 110, Vi[1] + uy * 110), CLARO, 4, 0.4, dash=E.TRACO)
                g1 = math.degrees(math.atan2(-uy, ux))
                Vn = P[(i + 1) % 5]
                g2 = math.degrees(math.atan2(-(Vn[1] - Vi[1]), Vn[0] - Vi[0]))
                varre = (g2 - g1 + 180) % 360 - 180
                lo, hi = (g1, g1 + varre) if varre > 0 else (g1 + varre, g1)
                canto(c, Vi, lo, hi, 50 + 8 * i, CLARO, ep(t, c11 + 0.4 + 0.15 * i, 0.3), 0.4, 3)
            E.frase(c, t, c11 + 0.5, ps("externos diferentes,", "i", 56, CLARO), 1500, 700, "center", 0.1)
            E.frase(c, t, c11 + 1.2, ps("soma", "i", 60, CLARO) + [("360°", "g", 70, BR)], 1500, 800, "center", 0.12)


# ---------------- piso ----------------
def b_piso(c, t, C, b):
    a12 = C["s12.a"]
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14, d14, e14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"]
    a15, b15, c15, d15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]

    def doze():
        E.frase(c, t, C["s12"] + 0.2, ps("cobrir o chão:", "i", 76) + [("sem buracos", "g", 76, COR)], W / 2, 170, "center", 0.12)
        E.frase(c, t, lerp(C["s12"], a12, 0.45), ps("e sem", "i", 66) + [("peça em cima de peça", "g", 66, COR)], W / 2, 270, "center", 0.12)
        k = 0
        for i in range(6):
            for j in range(3):
                x, y = 360 + 200 * i, 400 + 200 * j
                E.regular(c, t, C["s12"] + 0.5 + 0.06 * k, 4, x + 100, y + 100, 100 * math.sqrt(2), preenche=0.08, d=0.4, largura=5)
                k += 1
        O = (960, 600)
        if t >= a12:
            for j in range(4):
                canto(c, O, 90 * j, 90 * j + 90 * ease_io(prog(t, a12 + 0.15 * j, 0.4)), 80, E.COR if j % 2 == 0 else TINTA2, 1.0, 0.45, 4)
            c.drawCircle(*O, 12, M.paint(TINTA))
            E.foco(c, t, a12 + 0.8, 0.4, lambda a: E.pilula(c, "num ponto: 360°", 960, 1010, 50, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s13"] - 0.1, doze)

    O = (620, 580)
    X = 1450
    if C["s13"] <= t < C["s14"] + 0.5:
        def treze():
            for k in range(3):
                tk = a13 if k == 0 else b13 + 0.3 * (k - 1)
                peca(c, t, tk, 6, O, 120 * k - 90, 230, d=0.5, preenche=0.12)
                if t >= tk + 0.4:
                    canto(c, O, 120 * k - 90, 120 * k + 30, 70, E.COR if k % 2 == 0 else TINTA2, ep(t, tk + 0.4, 0.4), 0.45, 4)
            c.drawCircle(*O, 12, M.paint(TINTA))
            E.frase(c, t, a13, [("hexágono:", "g", 66, COR)] + ps("120°", "b", 66), X, 280, "center", 0.12)
            fcen(c, t, b13, "3 × 120 = 360", X, 480, 90)
            E.frase(c, t, c13, [("fecha", "g", 84, CERTO)] + ps("certinho", "i", 76, CERTO), X, 680, "center", 0.12)
            E.foco(c, t, c13 + 0.5, 0.5, lambda a: E.selo(c, X, 840, 70 * ease_back(prog(t, c13 + 0.5, 0.5)), True, a))
        E.saida(c, t, C["s14"] - 0.1, treze)
    if C["s14"] <= t < C["s15"] + 0.5:
        def quatorze():
            n4 = 4 if t >= d14 else 3
            for k in range(n4):
                tk = a14 if k == 0 else (b14 + 0.3 * (k - 1) if k < 3 else d14)
                cor = ERRADO if k == 3 else None
                peca(c, t, tk, 5, O, 108 * k - 90, 230, cor=cor, d=0.5, preenche=0.12 if k < 3 else 0.2)
                if t >= tk + 0.4:
                    canto(c, O, 108 * k - 90, 108 * k + 18, 70, ERRADO if k == 3 else (E.COR if k % 2 == 0 else TINTA2), ep(t, tk + 0.4, 0.4), 0.45, 4)
            if c14 <= t < d14:
                pulsa = 1 + 0.1 * math.sin(math.pi * M.clamp(prog(t, c14, 0.8)))
                canto(c, O, 324 - 90, 270, 130 * pulsa, ERRADO, ep(t, c14, 0.4), 0.5, 5)
                rotulo_em(c, t, c14 + 0.3, "36°", *pt(O, 190, 252), 54, ERRADO)
            if t >= d14:
                canto(c, O, 270, 342, 140, ERRADO, ep(t, d14 + 0.6, 0.4), 0.55, 5)  # a parte que cai em cima da 1ª peça
            c.drawCircle(*O, 12, M.paint(TINTA))
            E.frase(c, t, a14, [("pentágono:", "g", 66, COR)] + ps("108°", "b", 66), X, 230, "center", 0.12)
            fcen(c, t, b14, "3 × 108 = 324", X, 390, 80)
            E.frase(c, t, c14, ps("sobra um", "i", 60) + [("buraco de 36°", "g", 62, ERRADO)], X, 490, "center", 0.12)
            fcen(c, t, d14, "4 × 108 = 432", X, 650, 80, ERRADO)
            E.frase(c, t, d14 + 1.0, ps("passa da volta:", "i", 56) + [("peça sobre peça", "g", 58, ERRADO)], X, 750, "center", 0.1)
            E.frase(c, t, e14, ps("pentágonos", "i", 66) + [("não cobrem", "g", 70, ERRADO)], X, 920, "center", 0.12)
        E.saida(c, t, C["s15"] - 0.1, quatorze)
    if t >= C["s15"]:
        E.frase(c, t, a15, ps("cobre o piso quando o interno", "i", 60), W / 2, 180, "center", 0.1)
        E.frase(c, t, a15 + 1.5, ps("cabe um número", "i", 60) + [("exato", "g", 66, COR)] + ps("de vezes em", "i", 60) + [("360°", "g", 66, COR)],
                W / 2, 270, "center", 0.1)
        for n, cx, t0, s in ((3, 360, b15, "6 × 60 = 360"), (4, 960, c15, "4 × 90 = 360"), (6, 1560, d15, "3 × 120 = 360")):
            Oc = (cx, 600)
            L = 150 if n < 6 else 120
            for k in range(360 // int(interno(n))):
                peca(c, t, t0 + 0.12 * k, n, Oc, interno(n) * k, L, d=0.4, preenche=0.14 if k % 2 == 0 else 0.06)
            if t >= t0:
                c.drawCircle(*Oc, 10, M.paint(TINTA))
            nome = {3: "triângulo equilátero", 4: "quadrado", 6: "hexágono"}[n]
            E.frase(c, t, t0 + 0.3, [(nome, "g", 52, COR)], cx, 880, "center")
            fcen(c, t, t0 + 0.6, s, cx, 960, 50, TINTA2)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a16, b16, c16 = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    poli(c, t, a16 - 0.4, reg(12, 480, 560, 270), None, d=0.8, iguais=[1] * 12)
    E.frase(c, t, a16, [("12", "g", 70, COR)] + ps("lados, regular", "i", 64), 480, 920, "center", 0.12)
    E.frase(c, t, b16, ps("cada", "i", 60) + [("ângulo interno?", "g", 62, COR)], 900, 330, "left", 0.12)
    E.frase(c, t, c16, ps("piso: 2 desses num ponto", "i", 54), 900, 450, "left", 0.1)
    E.frase(c, t, c16 + 1.4, [("+ que polígono?", "g", 62, COR)], 900, 540, "left")
    E.relogio(c, t, C["s17.a"], 1490, 720, 150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a18, b18 = C["s18.a"], C["s18.b"]
    a19, b19, c19, d19 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    X = 1450

    def dezoito():
        E.frase(c, t, C["s18"] + 0.2, ps("pelo", "i", 76) + [("atalho", "g", 80, COR)], W / 2, 240, "center", 0.12)
        fcen(c, t, a18, "externo: 360 ÷ 12 = 30", W / 2, 450, 90, TINTA2)
        fcen(c, t, b18, "interno: 180 − 30 = 150°", W / 2, 640, 90, COR)
        bola_txt(c, t, b18 + 1.0, "150°", W / 2, 840, 110, 70)
    E.saida(c, t, C["s19"] - 0.1, dezoito)
    if t < C["s19"]:
        return
    O = (640, 600)
    L = 120
    # dois dodecágonos e o triângulo no buraco
    peca(c, t, C["s19"], 12, O, 0, L, d=0.6, preenche=0.12)
    peca(c, t, C["s19"] + 0.3, 12, O, 150, L, d=0.6, preenche=0.06)
    if t >= a19:
        canto(c, O, 0, 150, 60, E.COR, ep(t, a19, 0.4), 0.45, 4)
        canto(c, O, 150, 300, 60, TINTA2, ep(t, a19 + 0.3, 0.4), 0.45, 4)
    if b19 <= t < c19 + 0.3:
        canto(c, O, 300, 360, 150, ERRADO, ep(t, b19, 0.4) * (1 - ep(t, c19, 0.3)), 0.4, 5)
    if t >= c19:
        peca(c, t, c19, 3, O, 300, L, cor=CERTO, d=0.5, preenche=0.3)
    c.drawCircle(*O, 10, M.paint(TINTA))
    fcen(c, t, a19, "150 + 150 = 300", X, 250, 72)
    fcen(c, t, b19, "faltam 360 − 300 = 60", X, 380, 64, ERRADO if t < c19 else TINTA2)
    E.frase(c, t, c19, [("triângulo", "g", 64, CERTO), ("equilátero", "g", 64, CERTO)], X, 500, "center", 0.12)
    E.frase(c, t, d19 - 0.4, ps("conferindo pela soma:", "i", 50, TINTA2), X, 680, "center", 0.1)
    fcen(c, t, d19, "10 × 180 = 1800", X, 780, 64)
    fcen(c, t, lerp(d19, C["s19.end"], 0.4), "1800 ÷ 12 = 150", X, 880, 64)
    E.foco(c, t, lerp(d19, C["s19.end"], 0.75), 0.5, lambda a: E.selo(c, X, 990, 44 * ease_back(prog(t, lerp(d19, C["s19.end"], 0.75), 0.5)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s20.a", "regular:", "lados e ângulos iguais"), ("s20.b", "externo =", "360 ÷ n"),
                 ("s20.c", "interno =", "180 − externo"), ("s20.d", "piso:", "os cantos fecham 360°"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 350 + i * 175
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 50, a=a), centro(c, str(i + 1), 300, y - 5, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 66, COR), (l2, "i", 68)], 390, y, "left", 0.2)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s21.a"], [("A circunferência", "g", 120, COR)], XE, 450)
    E.frase(c, t, C["s21.b"], ps("raio e diâmetro", "i", 70), XE, 580, passo=0.12)
    E.frase(c, t, C["s21.c"], ps("e quanto a roda anda em 1 volta", "i", 66), XE, 680, passo=0.12)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, regular=b_regular, externo=b_externo, erro=b_erro, atalho=b_atalho,
              piso=b_piso, questao=b_questao, resposta=b_resposta, fim=b_fim)
