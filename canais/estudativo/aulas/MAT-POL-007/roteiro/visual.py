"""Visual — Estudativo · MAT-POL-007: tangente, corda e posições relativas (raio 13, corda a 5 do centro: 24).
Linguagem da geometria plana (MAT-ANG-001 a 020, MAT-POL-001): lados e retas em tinta; o segmento da vez em cor forte por cima
(a hipotenusa em COR, índigo; os catetos em TINTA2); distância do centro até a reta = tracejado com o quadradinho do ângulo reto;
lados iguais com tracinhos (E.marcas_iguais); medidas na grotesca; resposta na esfera; erro em vermelho, certo em verde;
atalho no palco escuro. As figuras respeitam as medidas (24 px por cm na corda, 38 px nas três retas): a figura não mente.
Posições relativas: três painéis lado a lado, a mesma circunferência de raio 5 e a reta a 7, 5 e 3 do centro.
Tangente: uma roda parada no chão (roda()); o raio até o ponto de contato fica em pé.
Peças locais: ps(), fcen(), bola_txt(), dist() (tracejado do centro até a reta com o quadradinho), rot() (rótulo que troca),
lin(), tri_cheio(), roda().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polígonos e Círculo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POL-007_tangente_corda_posicoes_relativas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("posicoes", "tangente", "corda", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 13 ** 2 - 5 ** 2 == 144 == 12 ** 2 and 2 * 12 == 24
assert 10 ** 2 - 6 ** 2 == 64 == 8 ** 2
assert (13 + 5) * (13 - 5) == 144 and (10 + 8) * (10 - 8) == 36 == 6 ** 2 and 6 ** 2 + 8 ** 2 == 100 and 16 // 2 == 8


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


def lin(c, t, t0, P, Q, cor=TINTA, larg=6, d=0.6, a=1.0, dash=None):
    if t >= t0 and a > 0:
        M.line(c, *P, *Q, cor, a, larg, dash=dash, progress=ease_io(prog(t, t0, d)))


def tri_cheio(c, pts, cor, a=1.0, alfa=0.2):
    if a <= 0:
        return
    path = skia.Path(); path.addPoly([tuple(p) for p in pts], True)
    c.drawPath(path, M.paint(cor, alfa * a))


def dist(c, t, t0, O, F, rotulo=None, lado=1, cor=TINTA2, size=54, viz=None, r=34):
    """distância do centro O até a reta, no pé F: tracejado com o quadradinho do ângulo reto (viz = um ponto da reta)"""
    E.segmento(c, t, t0, O, F, rotulo, cor=cor, tracejado=True, pontas=False, lado=lado, size=size, largura=5)
    if viz is not None:
        E.angulo(c, t, t0 + 0.4, F, O, viz, r=r, reto=True, cor=cor if cor != TINTA2 else E.COR, preenche=0.15)


def rot(c, t, t0, s, P, Q, lado=1, cor=None, size=56, gap=18):
    """rótulo ao lado do segmento PQ (lado = 1 ou −1), entrando com foco"""
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy * lado, -ux * lado
    mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, s, mx, my, nx, ny, gap, size, "b", cor or COR, a))


def ponto(c, t, t0, P, cor=TINTA, r=12, pulsa=False):
    k = ease_back(prog(t, t0, 0.35))
    if k <= 0:
        return
    if pulsa:
        k *= 1 + 0.45 * math.sin(math.pi * M.clamp(prog(t, t0 + 0.2, 0.8)))
    c.drawCircle(*P, r * k, M.paint(cor))


def roda(c, cx, cy, r, a=1.0):
    """roda de bicicleta vista de lado: pneu grosso, aro, raios e cubo"""
    if a <= 0:
        return
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.14 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawCircle(cx + 6, cy + 10, r, s)
    c.drawCircle(cx, cy, r - 14, M.paint("#2A2A33", a, stroke=28))
    c.drawCircle(cx, cy, r - 34, M.paint("#9A9AA6", a, stroke=6))
    for k in range(12):
        g = math.radians(k * 30 + 15)
        M.line(c, cx + 22 * math.cos(g), cy + 22 * math.sin(g), cx + (r - 36) * math.cos(g), cy + (r - 36) * math.sin(g), "#B4B4BE", a, 3)
    c.drawCircle(cx, cy, 24, M.paint("#5A5A66", a))


def nome_o(c, t, t0, O):
    """o centro com o nome O em cima, à esquerda (embaixo ficam a distância e o pé)"""
    k = ease_back(prog(t, t0, 0.35))
    if k > 0:
        c.drawCircle(*O, 10 * k, M.paint(TINTA))
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, "O", *O, -1, -0.8, 14, 56, "g", TINTA, a))


def no_c(O, r, g):
    return O[0] + r * math.cos(math.radians(g)), O[1] - r * math.sin(math.radians(g))


# ---------------- gancho ----------------
GO, GK = (560, 560), 24          # raio 13 → 312 px; corda a 5 → 120 px; metade 12 → 288 px
GA, GB, GM = (GO[0] - 12 * GK, GO[1] + 5 * GK), (GO[0] + 12 * GK, GO[1] + 5 * GK), (GO[0], GO[1] + 5 * GK)


def b_gancho(c, t, C, b):
    ka, kb, kc, kd, ke = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"], C["s01.e"]
    X = 1130

    def um():
        E.circulo(c, t, ka, *GO, 13 * GK, raio=(130, "13"), te={"raio": ka + 0.8}, size=60)
        E.segmento(c, t, kb, GA, GB, None, cor=TINTA, largura=8)
        dist(c, t, kb + 0.5, GO, GM, "5", 1, viz=GB, size=60)
        E.foco(c, t, kc, 0.4, lambda a: centro(c, "?", GO[0], GM[1] + 110, 100, "g", COR, a))
        if t >= ke:
            M.line(c, *GA, *GB, CERTO, ep(t, ke, 0.4), 12)
        E.frase(c, t, ka, ps("raio", "i", 80) + [("13 cm", "g", 84, COR)], X, 260, passo=0.14)
        E.frase(c, t, kb, ps("corda a", "i", 76) + [("5 cm", "g", 80, COR)] + ps("do centro", "i", 76), X, 380, passo=0.12)
        E.frase(c, t, kc, ps("quanto mede", "i", 84) + [("a corda?", "g", 84, COR)], X, 520, passo=0.12)
        E.frase(c, t, kd - 0.6, ps("muita gente:", "i", 70, TINTA2), X, 700, passo=0.12)
        E.foco(c, t, kd, 0.4, lambda a: E.escreve(c, "12", X + 440, 712, 120, "g", ERRADO, a))
        if t >= lerp(kd, ke, 0.7):
            E.risco(c, X + 420, 720, X + 600, 610, t, lerp(kd, ke, 0.7), largura=14)
        E.frase(c, t, ke, ps("certo:", "i", 76, CERTO), X, 900)
        bola_txt(c, t, ke + 0.2, "24", X + 400, 875, 100, 104, CERTO)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1530, 560, 240 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 280, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), [("externa,", "g", 90, COR), ("tangente", "g", 90, COR)], XE, 420, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.55), ps("ou", "i", 86) + [("secante", "g", 90, COR)], XE, 540, passo=0.14)
        E.frase(c, t, tb, ps("tangentes e cordas", "i", 76), XE, 700, passo=0.14)
        E.frase(c, t, tb + 0.6, ps("com", "i", 84) + [("Pitágoras", "g", 90)], XE, 810, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1530, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1530, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "o raio vai do centro", "até a circunferência"), ("s03.c", "isósceles: a altura do topo", "corta a base ao meio"),
             ("s03.d", "o teorema de", "Pitágoras"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.4, [(l2, "g", 60, COR)], x + 44, y + 160)
    alvo = [x + w - 30, [170 + i * 240 + 170 for i in range(3)]]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, alvo[0], lerp(lerp(alvo[1][0], alvo[1][1], q1), alvo[1][2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 960, "left", 0.12)


# ---------------- posições relativas ----------------
PO, PR = (600, 600), 230
PF = (PO[0] + 330, PO[1])        # pé da distância numa reta em pé, à direita
PX = [330, 960, 1590]            # os três painéis
PCY, PK = 370, 38                # raio 5 → 190 px


def b_posicoes(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    X = 1440

    def demo():
        E.frase(c, t, C["s04"] + 0.2, ps("a reta e a circunferência:", "i", 72) + [("3 jeitos", "g", 80, COR)], W / 2, 170, "center", 0.12)
        E.circulo(c, t, a4, *PO, PR, o="O", size=56)
        lin(c, t, b4, (PF[0], 250), (PF[0], 980), TINTA, 6, 0.7)
        if t >= c4:
            for yy in (330, 900):
                M.line(c, *PO, PF[0], yy, TINTA2, 0.55 * ep(t, c4, 0.3), 4, dash=E.TRACO, progress=ease_io(prog(t, c4, 0.6)))
                ponto(c, t, c4 + 0.5, (PF[0], yy), TINTA2, 10)
        dist(c, t, b4 + 0.4, PO, PF, None, 1, cor=COR if t >= c4 else TINTA2, viz=(PF[0], PF[1] - 100), r=44)
        ponto(c, t, b4 + 0.9, PF, E.COR, 12, pulsa=True)
        E.frase(c, t, b4, ps("quem decide:", "i", 66), X, 340, "center", 0.12)
        E.frase(c, t, b4 + 0.6, [("a distância", "g", 84, COR)], X, 450, "center")
        E.frase(c, t, b4 + 1.2, ps("do centro até a reta", "i", 60, TINTA2), X, 540, "center", 0.1)
        E.frase(c, t, c4, ps("o caminho", "i", 66) + [("mais curto", "g", 72, COR)], X, 700, "center", 0.12)
        E.frase(c, t, d4, ps("chega em", "i", 66) + [("ângulo reto", "g", 72)], X, 830, "center", 0.12)
    E.saida(c, t, C["s05"] - 0.1, demo)
    if t < C["s05"] - 0.1:
        return

    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6, e6, f6 = (C["s06." + k] for k in "abcdef")
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    R = 5 * PK
    paineis = ((PX[0], 7, a5, b5, c5, "externa", "não toca", "d > r", a7),
               (PX[1], 5, a6, a6 + 0.6, c6, "tangente", "1 ponto", "d = r", b7),
               (PX[2], 3, d6, d6 + 0.6, f6, "secante", "2 pontos", "d < r", c7))
    for cx, d, tc, tl, tn, nome, sub, regra, tr in paineis:
        y = PCY + d * PK
        E.circulo(c, t, tc, cx, PCY, R, o=None, raio=(150, "5"), te={"raio": tc + 0.6}, size=52)
        lin(c, t, tl, (cx - 280, y), (cx + 280, y), TINTA, 6, 0.6)
        dist(c, t, tl + 0.3, (cx, PCY), (cx, y), str(d), 1, viz=(cx + 60, y), size=54, r=30)
        E.frase(c, t, tn, [(nome, "g", 76, COR)], cx, 790, "center")
        E.frase(c, t, tn + 0.4, ps(sub, "i", 56, TINTA2), cx, 870, "center", 0.12)
        E.foco(c, t, tr, 0.5, lambda a, cx=cx, regra=regra: E.pilula(c, regra, cx, 975, 62, "g", a=a, cor=E.SOBRE))
    # o ponto de contato e os dois pontos da secante
    ponto(c, t, b6, (PX[1], PCY + R), E.COR, 14, pulsa=True)
    k3 = math.sqrt(5 ** 2 - 3 ** 2) * PK
    if t >= e6:
        M.line(c, PX[2] - k3, PCY + 3 * PK, PX[2] + k3, PCY + 3 * PK, E.COR, ep(t, e6, 0.4), 10)
    ponto(c, t, e6, (PX[2] - k3, PCY + 3 * PK), E.COR, 14, pulsa=True)
    ponto(c, t, e6 + 0.15, (PX[2] + k3, PCY + 3 * PK), E.COR, 14, pulsa=True)
    E.foco(c, t, C["s07"], 0.5, lambda a: centro(c, "d = distância      r = raio", W / 2, 112, 54, "b", TINTA2, a))


# ---------------- tangente ----------------
RO, RR = (720, 520), 280
RT = (RO[0], RO[1] + RR)         # ponto de contato com o chão
TO, TK = (470, 650), 45          # raio 6 → 270 px; OP = 10 → 450 px
TP = (TO[0] + 10 * TK, TO[1])
TT = no_c(TO, 6 * TK, math.degrees(math.acos(6 / 10)))


def b_tangente(c, t, C, b):
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    X = 1530

    def chao():
        q = ease_io(prog(t, a8, 0.6))
        M.line(c, 160, RT[1], lerp(160, 1280, q), RT[1], TINTA, 1.0, 6)
        for i in range(17):
            x = 180 + i * 64
            M.line(c, x, RT[1] + 10, x - 22, RT[1] + 40, TINTA2, q * 0.6, 3)
        if t >= b8:
            M.line(c, 160, RT[1], 1280, RT[1], E.COR, ep(t, b8, 0.4), 10)
            E.foco(c, t, b8 + 0.2, 0.4, lambda a: E.escreve(c, "tangente", 1040, RT[1] + 100, 56, "b", COR, a))
        E.foco(c, t, a8, 0.6, lambda a: roda(c, *RO, RR, a))
        if t >= a9:  # outros caminhos até o chão: mais longos e passam por fora
            for xx in (RT[0] - 420, RT[0] + 420):
                M.line(c, *RO, xx, RT[1], TINTA2, 0.7, 4, dash=E.TRACO, progress=ease_io(prog(t, a9, 0.6)))
                ponto(c, t, a9 + 0.5, (xx, RT[1]), TINTA2, 10)
        if t >= c8:
            M.line(c, *RO, *RT, E.COR, 1.0, 9, progress=ease_io(prog(t, c8, 0.6)))
            E.foco(c, t, c8 + 0.4, 0.4, lambda a: E.escreve(c, "raio", RO[0] + 22, RO[1] + 150, 54, "b", COR, a))
        E.angulo(c, t, d8, RT, RO, (RT[0] + 80, RT[1]), r=64, reto=True)
        if t >= b9:
            pulsa = 1 + 0.25 * math.sin(math.pi * M.clamp(prog(t, b9, 0.8)))
            E.angulo(c, t, b9, RT, RO, (RT[0] + 80, RT[1]), r=64 * pulsa, reto=True, preenche=0.4)
        ponto(c, t, b8 + 0.4, RT, TINTA, 13)
        ponto(c, t, a9, RT, E.COR, 15, pulsa=True)
        c.drawCircle(*RO, 9, M.paint(TINTA, ep(t, a8, 0.4)))

    E.saida(c, t, C["s10"] - 0.1, chao)

    def txt8():
        E.frase(c, t, a8, ps("roda parada", "i", 74), X, 300, "center", 0.12)
        E.frase(c, t, a8 + 0.5, ps("no chão", "i", 74), X, 390, "center", 0.12)
        E.frase(c, t, b8, ps("chão =", "i", 70) + [("tangente", "g", 76, COR)], X, 520, "center", 0.12)
        E.frase(c, t, c8, ps("o raio fica", "i", 66) + [("em pé", "g", 72)], X, 660, "center", 0.12)
        E.foco(c, t, d8, 0.5, lambda a: E.escreve(c, "90°", X - E.larg("90°", "g", 170) / 2, 880, 170, "g", COR, a))
    E.saida(c, t, C["s09"] - 0.1, txt8)

    def txt9():
        E.frase(c, t, C["s09"], ps("por quê?", "i", 80, COR), X, 220, "center")
        E.frase(c, t, a9, ps("o contato é o ponto", "i", 60), X, 350, "center", 0.1)
        E.frase(c, t, a9 + 0.6, [("mais perto", "g", 76, COR)] + ps("do centro", "i", 60), X, 440, "center", 0.12)
        E.frase(c, t, b9, ps("o mais curto chega em", "i", 60), X, 580, "center", 0.1)
        E.frase(c, t, b9 + 0.6, [("ângulo reto", "g", 76)], X, 670, "center")
        E.foco(c, t, c9, 0.5, lambda a: E.pilula(c, "tangente e raio: 90°", X, 830, 62, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, c9 + 0.6, ps("no ponto de contato", "i", 54, TINTA2), X, 940, "center", 0.1)
    if t >= C["s09"]:
        E.saida(c, t, C["s10"] - 0.1, txt9)
    if t < C["s10"] - 0.1:
        return

    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    tri_cheio(c, [TO, TT, TP], E.COR, ep(t, d10, 0.5), 0.12)
    E.circulo(c, t, C["s10"], *TO, 6 * TK, o="O", size=56)
    # OP: hipotenusa
    E.segmento(c, t, b10, TO, TP, None, cor=TINTA2, pontas=False, largura=6)
    if t >= d10:
        M.line(c, *TO, *TP, E.COR, ep(t, d10, 0.4), 10)
    ponto(c, t, b10 + 0.5, TP, TINTA, 13)
    E.foco(c, t, b10 + 0.6, 0.4, lambda a: E._cola(c, "P", *TP, 1, 0, 18, 64, "g", TINTA, a))
    rot(c, t, b10 + 0.7, "10", TO, TP, -1, COR, 60)
    # raio e tangente: catetos
    E.segmento(c, t, c10, TO, TT, None, cor=TINTA, pontas=False, largura=7)
    rot(c, t, c10 + 0.5, "6", TO, TT, 1, TINTA2, 60)
    lin(c, t, c10 + 0.5, TP, TT, TINTA, 7, 0.7)
    ponto(c, t, c10 + 0.4, TT, TINTA, 12)
    E.angulo(c, t, c10 + 1.1, TT, TO, TP, r=44, reto=True)
    E.saida(c, t, d11, lambda: rot(c, t, c10 + 1.0, "?", TP, TT, -1, COR, 66))
    rot(c, t, d11 + 0.1, "8", TP, TT, -1, CERTO, 70)

    def txt10():
        E.frase(c, t, a10, ps("o ângulo reto cria", "i", 64), X, 260, "center", 0.12)
        E.frase(c, t, a10 + 0.6, [("triângulos retângulos", "g", 66, COR)], X, 350, "center")
        E.frase(c, t, b10, ps("P a", "i", 66) + [("10 cm", "g", 72, COR)] + ps("do centro", "i", 66), X, 500, "center", 0.12)
        E.frase(c, t, c10, ps("raio", "i", 66) + [("6 cm", "g", 72)], X, 620, "center", 0.12)
        E.frase(c, t, c10 + 1.0, ps("catetos:", "i", 58, TINTA2) + ps("raio e tangente", "i", 58), X, 760, "center", 0.12)
        E.frase(c, t, d10, ps("hipotenusa:", "i", 64) + [("OP", "g", 72, COR)], X, 880, "center", 0.12)
    E.saida(c, t, C["s11"] - 0.1, txt10)
    if t >= C["s11"]:
        fcen(c, t, a11, "10^2 = 100", X, 290, 88)
        fcen(c, t, b11, "6^2 = 36", X, 420, 88, TINTA2)
        fcen(c, t, c11, "100 − 36 = 64", X, 570, 88)
        E.formula_em(c, t, d11, "r{64} =", X + 40, 760, 88, "g", None, "right")
        bola_txt(c, t, d11 + 0.2, "8", X + 160, 730, 82, 96)
        E.frase(c, t, d11 + 0.6, ps("a tangente mede", "i", 58) + [("8 cm", "g", 64, CERTO)], X, 930, "center", 0.12)


# ---------------- corda ----------------
CO, CK = (560, 520), 24          # raio 13 → 312 px; corda a 5 → 120 px; metade 12 → 288 px
CRr = 13 * CK
CA, CB, CM = (CO[0] - 12 * CK, CO[1] + 5 * CK), (CO[0] + 12 * CK, CO[1] + 5 * CK), (CO[0], CO[1] + 5 * CK)


def b_corda(c, t, C, b):
    a12, b12 = C["s12.a"], C["s12.b"]
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    a15, b15, c15, d15, e15 = (C["s15." + k] for k in "abcde")
    X = 1420
    meio13 = lerp(b13, c13, 0.25)
    # o triângulo OAB (isósceles) e depois OMB (retângulo)
    tri_cheio(c, [CO, CA, CB], E.COR, ep(t, b13, 0.5) * (1 - ep(t, b14, 0.5)), 0.14)
    tri_cheio(c, [CO, CM, CB], E.COR, ep(t, b14, 0.5), 0.16)
    E.circulo(c, t, C["s12"], *CO, CRr, o=None, size=56)
    nome_o(c, t, C["s12"] + 0.4, CO)
    # a reta secante e a corda
    if t >= a12:
        M.line(c, CA[0] - 150, CA[1], CB[0] + 150, CB[1], TINTA, 1 - 0.6 * ep(t, a12 + 0.8, 0.4), 4, progress=ease_io(prog(t, a12, 0.6)))
    E.segmento(c, t, a12 + 0.6, CA, CB, None, cor=TINTA, largura=8)
    if t >= e15:
        M.line(c, *CA, *CB, CERTO, ep(t, e15, 0.4), 12)
    E.foco(c, t, a12 + 0.9, 0.4, lambda a: (E._cola(c, "A", *CA, -1, 0.3, 16, 60, "g", TINTA, a), E._cola(c, "B", *CB, 1, 0.3, 16, 60, "g", TINTA, a)))
    # o diâmetro, a maior corda
    E.saida(c, t, C["s13"], lambda: (E.segmento(c, t, b12, (CO[0] - CRr, CO[1]), (CO[0] + CRr, CO[1]), None, cor=COR, largura=7),
                                     E.foco(c, t, b12 + 0.5, 0.4, lambda a: E.escreve(c, "diâmetro", CO[0] + 40, CO[1] - 26, 52, "b", COR, a))))
    # dois raios iguais
    lin(c, t, a13, CO, CA, TINTA, 6, 0.6)
    lin(c, t, a13 + 0.3, CO, CB, TINTA, 6, 0.6)
    q = ep(t, a13 + 0.8, 0.4) * (1 - ep(t, a14, 0.4))
    E.marcas_iguais(c, CO, CA, 1, TINTA, q); E.marcas_iguais(c, CO, CB, 1, TINTA, q)
    # a altura do topo: corta a corda ao meio
    dist(c, t, c13, CO, CM, None, 1, cor=TINTA2, viz=CB, r=36)
    q2 = ep(t, c13 + 0.8, 0.4)
    E.marcas_iguais(c, CA, CM, 2, COR, q2); E.marcas_iguais(c, CM, CB, 2, COR, q2)
    ponto(c, t, c13 + 0.6, CM, TINTA, 10)
    E.foco(c, t, c13 + 0.6, 0.4, lambda a: E._cola(c, "M", *CM, 0.25, 1, 18, 56, "g", TINTA, a))
    # Pitágoras no OMB
    if t >= b14:
        M.line(c, *CO, *CB, E.COR, ep(t, b14, 0.4), 10)
    rot(c, t, b14 + 0.3, "13", CO, CB, 1, COR, 62)
    rot(c, t, c14, "5", CO, CM, -1, TINTA2, 62)
    E.saida(c, t, d15, lambda: rot(c, t, d14, "?", CM, CB, -1, COR, 66))
    rot(c, t, d15 + 0.1, "12", CM, CB, -1, COR, 62)
    if t >= e15:
        E.foco(c, t, e15 + 0.4, 0.4, lambda a: E._cola(c, "24", CM[0], CM[1] + 90, 0, 1, 20, 76, "g", CERTO, a))

    def txt12():
        E.frase(c, t, a12, [("corda:", "g", 84, COR)], X, 300, "center")
        E.frase(c, t, a12 + 0.6, ps("liga dois pontos", "i", 64), X, 400, "center", 0.12)
        E.frase(c, t, a12 + 1.2, ps("da circunferência", "i", 64), X, 490, "center", 0.12)
        E.frase(c, t, b12, ps("a maior corda:", "i", 64), X, 680, "center", 0.12)
        E.frase(c, t, b12 + 0.6, [("o diâmetro", "g", 80, COR)], X, 790, "center")
    E.saida(c, t, C["s13"] - 0.1, txt12)

    def txt13():
        E.frase(c, t, a13, ps("dois raios:", "i", 64) + [("iguais", "g", 70, COR)], X, 260, "center", 0.12)
        E.frase(c, t, b13, ps("triângulo", "i", 66) + [("isósceles", "g", 72, COR)], X, 400, "center", 0.12)
        E.frase(c, t, b13 + 0.8, ps("topo no centro, base = corda", "i", 52, TINTA2), X, 480, "center", 0.1)
        E.frase(c, t, meio13, ps("a altura do topo", "i", 60), X, 630, "center", 0.12)
        E.frase(c, t, c13, ps("corta a corda", "i", 66), X, 750, "center", 0.12)
        E.frase(c, t, c13 + 0.6, [("ao meio", "g", 90, COR)], X, 870, "center")
    if t >= C["s13"] - 0.1:
        E.saida(c, t, C["s14"] - 0.1, txt13)

    def txt14():
        E.frase(c, t, a14, ps("raio", "i", 64) + [("13", "g", 72, COR)] + ps("· corda a", "i", 64) + [("5", "g", 72, COR)], X, 260, "center", 0.12)
        E.frase(c, t, b14, ps("hipotenusa:", "i", 62) + ps("o raio", "g", 66, COR), X, 420, "center", 0.12)
        E.frase(c, t, c14, ps("catetos:", "i", 62) + [("5", "g", 70, TINTA2)], X, 560, "center", 0.12)
        E.frase(c, t, d14, ps("e", "i", 62) + [("a metade", "g", 70, COR)] + ps("da corda", "i", 62), X, 680, "center", 0.12)
    if t >= C["s14"] - 0.1:
        E.saida(c, t, C["s15"] - 0.1, txt14)
    if t >= C["s15"]:
        fcen(c, t, a15, "13^2 = 169", X, 240, 84, COR)
        fcen(c, t, b15, "5^2 = 25", X, 360, 84, TINTA2)
        fcen(c, t, c15, "169 − 25 = 144", X, 500, 84)
        E.formula_em(c, t, d15, "r{144} =", X + 40, 680, 84, "g", None, "right")
        bola_txt(c, t, d15 + 0.2, "12", X + 170, 652, 82, 84)
        E.frase(c, t, d15 + 0.7, ps("é a", "i", 56) + [("metade", "g", 60, COR)], X, 790, "center", 0.12)
        E.frase(c, t, e15, ps("corda =", "i", 66) + [("2 × 12 = 24", "g", 72, CERTO)], X, 930, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a16, b16, c16, d16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    X = 1420
    t0 = C["s16"] - 3
    tri_cheio(c, [CO, CM, CB], E.COR, 1.0, 0.16)
    E.circulo(c, t, t0, *CO, CRr, o=None, size=56)
    nome_o(c, t, t0, CO)
    E.segmento(c, t, t0, CA, CB, None, cor=TINTA, largura=8)
    dist(c, t, t0, CO, CM, None, 1, viz=CB, r=36)
    M.line(c, *CO, *CB, E.COR, 1.0, 8)
    rot(c, t, t0, "13", CO, CB, 1, COR, 62)
    rot(c, t, t0, "5", CO, CM, -1, TINTA2, 62)
    E.saida(c, t, d16 + 0.3, lambda: rot(c, t, t0, "12", CM, CB, -1, COR, 62))
    def meio16():
        pulsa = 1 + 0.4 * math.sin(math.pi * M.clamp(prog(t, b16, 0.9)))
        M.line(c, *CM, *CB, E.COR, ep(t, b16, 0.3), 12 * pulsa)
        E.chave(c, CM[0], CB[0], CB[1] + 30, COR, ep(t, b16 + 0.3, 0.5), 26)
        E.foco(c, t, b16 + 0.6, 0.4, lambda a: centro(c, "só até o meio", (CM[0] + CB[0]) / 2, CB[1] + 120, 50, "b", COR, a))
    if t >= b16:
        E.saida(c, t, d16, meio16)
    if t >= d16:
        M.line(c, *CA, *CB, CERTO, ep(t, d16 + 0.3, 0.4), 12)
        E.foco(c, t, d16 + 0.5, 0.4, lambda a: E._cola(c, "24", CM[0], CM[1] + 90, 0, 1, 20, 76, "g", CERTO, a))
    E.frase(c, t, C["s16"] + 0.2, ps("o erro", "i", 72, ERRADO) + ps("mais comum", "i", 72), X, 220, "center", 0.12)
    E.frase(c, t, a16, ps("parar no", "i", 70) + [("12", "g", 90, ERRADO)], X, 360, "center", 0.12)
    E.foco(c, t, a16 + 0.6, 0.5, lambda a: E.selo(c, X + 260, 330, 46 * ease_back(prog(t, a16 + 0.6, 0.5)), False, a))
    E.frase(c, t, c16, ps("Pitágoras dá", "i", 66), X, 520, "center", 0.12)
    E.frase(c, t, c16 + 0.6, [("a metade", "g", 90, COR)], X, 630, "center")
    E.foco(c, t, d16, 0.5, lambda a: E.pilula(c, "antes de responder, dobre", X, 790, 56, "g", a=a, cor=E.SOBRE))
    fcen(c, t, d16 + 0.6, "12 × 2 = 24", X, 950, 90, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a17, b17, c17, d17, e17, f17 = (C["s17." + k] for k in "abcdef")
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    X = W / 2

    def um():
        E.frase(c, t, C["s17"] + 0.2, [("atalho", "g", 90, CLARO)] + ps("da corda", "i", 80, BR), X, 170, "center", 0.12)
        E.frase(c, t, a17, [("soma", "g", 84, BR)] + ps("vezes", "i", 76, CLARO) + [("diferença", "g", 84, BR)], X, 320, "center", 0.12)
        fcen(c, t, b17, "13 + 5 = 18", 560, 500, 100, BR)
        fcen(c, t, c17, "13 − 5 = 8", 1360, 500, 100, BR)
        fcen(c, t, d17, "18 × 8 = 144", X, 680, 110, CLARO)
        E.formula_em(c, t, e17, "r{144} =", 620, 900, 90, "g", BR, "right")
        bola_txt(c, t, e17 + 0.2, "12", 750, 868, 86, 90)
        E.frase(c, t, f17, [("corda", "i", 80, CLARO), ("=", "g", 76, CLARO)], 1290, 900, "right", 0.12)
        bola_txt(c, t, f17 + 0.3, "24", 1420, 868, 96, 96, CERTO)
    E.saida(c, t, C["s18"] - 0.1, um)
    if t < C["s18"] - 0.1:
        return
    E.frase(c, t, C["s18"], ps("por que funciona?", "i", 70, CLARO), X, 160, "center", 0.12)
    fcen(c, t, a18, "13^2 − 5^2", 520, 330, 100, BR)
    E.frase(c, t, a18 + 0.8, ps("diferença de dois quadrados", "i", 52, CLARO), 520, 440, "center", 0.1)
    fcen(c, t, b18, "= (13 + 5) · (13 − 5)", 1300, 330, 90, CLARO)
    E.frase(c, t, b18 + 0.6, ps("soma vezes diferença", "i", 52, CLARO), 1300, 440, "center", 0.1)
    E.foco(c, t, c18, 0.5, lambda a: E.pilula(c, "não serve quando falta o raio", X, 620, 60, "g", fundo=ERRADO, a=a))
    E.frase(c, t, lerp(c18, d18, 0.55), ps("o raio é a hipotenusa:", "i", 60, CLARO), X, 790, "center", 0.1)
    fcen(c, t, d18, "13^2 = 5^2 + 12^2", X, 920, 90, BR)
    E.frase(c, t, d18 + 0.4, ps("os quadrados se", "i", 52, CLARO) + [("somam", "g", 56, BR)], X, 1020, "center", 0.1)


# ---------------- questão ----------------
QO, QK = (450, 450), 24          # raio 10 → 240 px; corda 16: metade 8 → 192 px; distância 6 → 144 px
QA, QB, QM = (QO[0] - 8 * QK, QO[1] + 6 * QK), (QO[0] + 8 * QK, QO[1] + 6 * QK), (QO[0], QO[1] + 6 * QK)


def figura_q(c, t, t0, traco_raio, t_corda, t_dist, raio_lado=True):
    nome_o(c, t, t0 + 0.4, QO)
    E.circulo(c, t, t0, *QO, 10 * QK, o=None, raio=(45, "10") if raio_lado else None, te={"raio": traco_raio}, size=56)
    E.segmento(c, t, t_corda, QA, QB, None, cor=TINTA, largura=8)
    dist(c, t, t_dist, QO, QM, None, 1, viz=QB, r=32)


def b_questao(c, t, C, b):
    a19, b19, c19, d19 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 130, passo=0.12)
    figura_q(c, t, a19, a19 + 0.6, b19, c19)
    rot(c, t, b19 + 0.5, "16", QA, QB, -1, COR, 60)
    E.foco(c, t, c19 + 0.5, 0.4, lambda a: E._cola(c, "?", QO[0], (QO[1] + QM[1]) / 2, -1, 0, 18, 72, "g", COR, a))
    E.frase(c, t, c19, ps("a que", "i", 64) + [("distância", "g", 68, COR)] + ps("do centro?", "i", 64), QO[0], 830, "center", 0.12)
    E.frase(c, t, d19, ps("e uma reta a", "i", 60) + [("12 cm", "g", 64, COR)] + ps("do centro:", "i", 60)
            + [("externa, tangente ou secante?", "g", 60)], W / 2, 990, "center", 0.1)
    E.relogio(c, t, C["s20.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a21, b21, c21, d21, e21 = (C["s21." + k] for k in "abcde")
    a22, b22, c22 = C["s22.a"], C["s22.b"], C["s22.c"]
    X = 1350
    t0 = C["s21"]
    tri_cheio(c, [QO, QM, QB], E.COR, ep(t, t0 + 0.6, 0.5), 0.15)
    figura_q(c, t, t0 - 1.5, t0, t0 - 1.5, t0 - 1.5, raio_lado=False)
    lin(c, t, t0 + 0.6, QO, QB, E.COR, 9, 0.5)
    rot(c, t, t0 + 0.9, "10", QO, QB, 1, COR, 60)
    rot(c, t, a21, "8", QM, QB, -1, TINTA2, 60)
    E.saida(c, t, e21, lambda: E.foco(c, t, t0, 0.4, lambda a: E._cola(c, "?", QO[0], (QO[1] + QM[1]) / 2, -1, 0, 18, 66, "g", COR, a)))
    E.foco(c, t, e21 + 0.2, 0.4, lambda a: E._cola(c, "6", QO[0], (QO[1] + QM[1]) / 2, -1, 0, 18, 66, "g", CERTO, a))
    # a reta a 12: externa
    F = (QO[0] - 12 * QK, QO[1])
    lin(c, t, b22, (F[0], 170), (F[0], 730), TINTA, 6, 0.6)
    if t >= b22:
        dist(c, t, b22 + 0.4, QO, F, None, 1, viz=(F[0], F[1] - 60), r=30)
        rot(c, t, b22 + 0.8, "12", QO, F, -1, COR, 56, gap=12)

    def conta():
        E.frase(c, t, t0 + 0.4, ps("o raio é a", "i", 60) + [("hipotenusa", "g", 64, COR)], X, 200, "center", 0.12)
        fcen(c, t, a21, "metade: 16 ÷ 2 = 8", X, 330, 72, TINTA2)
        fcen(c, t, b21, "10 + 8 = 18", X, 460, 84)
        fcen(c, t, c21, "10 − 8 = 2", X, 580, 84)
        fcen(c, t, d21, "18 × 2 = 36", X, 710, 84)
        E.formula_em(c, t, e21, "r{36} =", X + 10, 890, 84, "g", None, "right")
        bola_txt(c, t, e21 + 0.2, "6 cm", X + 170, 862, 100, 66, CERTO)
    E.saida(c, t, C["s22"] - 0.1, conta)
    if t >= C["s22"]:
        E.frase(c, t, C["s22"], ps("conferindo", "i", 76, COR), X, 220, "center")
        fcen(c, t, a22, "6^2 + 8^2 = 100 = 10^2", X, 360, 76)
        E.foco(c, t, a22 + 1.2, 0.5, lambda a: E.selo(c, X, 480, 46 * ease_back(prog(t, a22 + 1.2, 0.5)), True, a))
        fcen(c, t, b22, "12 > 10", X, 680, 96)
        E.frase(c, t, b22 + 0.6, ps("passa longe", "i", 58, TINTA2), X, 770, "center", 0.12)
        E.foco(c, t, c22, 0.5, lambda a: E.pilula(c, "externa", X, 900, 80, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s23.a", "distância × raio:", "externa, tangente, secante"), ("s23.b", "tangente:", "90° com o raio"),
                 ("s23.c", "corda:", "Pitágoras dá a metade"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 52, a=a), centro(c, str(i + 1), 240, y - 5, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 64, COR), (l2, "i", 66)], 330, y, "left", 0.2)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s24.a"], [("Cordas que", "g", 130, COR)], XE, 440)
    E.frase(c, t, C["s24.a"] + 0.4, [("se cruzam", "g", 130, COR)], XE, 570)
    E.frase(c, t, C["s24.b"], ps("pedaços", "i", 84) + [("×", "g", 84)] + ps("pedaços", "i", 84), XE, 700, passo=0.12)
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, posicoes=b_posicoes, tangente=b_tangente, corda=b_corda, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
