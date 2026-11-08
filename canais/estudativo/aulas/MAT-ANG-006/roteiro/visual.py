"""Visual — Estudativo · MAT-ANG-006: quando três medidas formam um triângulo (desigualdade triangular).
Linguagem da geometria plana (MAT-ANG-001 a 005): lados em tinta; medidas na grotesca; resposta na esfera. Aqui os lados viram
palitos: o maior em tinta (deitado como base), os menores em COR e TINTA2, presos nas pontas da base por uma dobradiça e girando
para tentar se encontrar. A falta é marcada em vermelho tracejado; o "achatado" (soma igual) mostra os menores deitados sobre o maior.
O intervalo do terceiro lado vai na reta numérica do kit (E.reta + E.intervalo), com bolinhas abertas: as pontas não entram.
Peças locais: palito() e dobradica(). Todo instante vem de C[...]."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-006_quando_tres_medidas_formam_triangulo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("palitos", "terceiro", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 2 + 3 < 6 and 2 + 3 == 5 and 5 + 8 == 13 and 8 - 5 == 3 and 12 - 4 + 1 == 9 and 13 - 3 + 1 == 11
assert 3 + 5 == 8 and 9 - 4 == 5 and 9 + 4 == 13 and 12 - 6 + 1 == 7 and 12 - 4 + 1 == 9


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


def operacao(c, t, t0, op, x, y, escuro=False):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, op, x, y - 30, 54, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, t0 + 0.3, ps("nos dois lados", "i", 40, CLARO if escuro else TINTA2), x, y + 48, "center", 0.06)


def pt(V, L, g):
    return V[0] + L * math.cos(math.radians(g)), V[1] - L * math.sin(math.radians(g))


def palito(c, P, Q, cor, a=1.0, rot=None, lado=-1, size=50, larg=18):
    """palito de P a Q, grosso e arredondado, com a medida ao lado"""
    if a <= 0:
        return
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.18 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 6))
    p = M.paint(cor, a, stroke=larg, cap_round=True)
    c.save(); c.translate(3, 6)
    path = skia.Path(); path.moveTo(*P); path.lineTo(*Q)
    s.setStyle(skia.Paint.kStroke_Style); s.setStrokeWidth(larg); s.setStrokeCap(skia.Paint.kRound_Cap)
    c.drawPath(path, s)
    c.restore()
    c.drawPath(path, p)
    if rot:
        mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
        dx, dy = Q[0] - P[0], Q[1] - P[1]
        n = math.hypot(dx, dy) or 1
        nx, ny = dy / n * lado, -dx / n * lado
        if ny > 0.01 and lado == -1:
            nx, ny = -nx, -ny
        if lado == 0:
            nx, ny = 0, 1
        E.formula(c, rot, mx + nx * 48, my + ny * 48 + size * 0.36, size, "b", cor, a, "center")


def dobradica(c, L, R, la, lb, ga, gb, ca, cb, a=1.0, rots=(None, None), falta=0.0):
    """dois palitos presos nas pontas da base LR: o de comprimento la sai de L no ângulo ga; o de lb sai de R no ângulo 180 − gb.
    falta = opacidade do tracejado vermelho entre as pontas (o que falta para fechar)"""
    Pa = pt(L, la, ga)
    Pb = pt(R, lb, 180 - gb)
    palito(c, L, Pa, ca, a, rots[0], -1)
    palito(c, R, Pb, cb, a, rots[1], -1)
    if falta > 0 and math.dist(Pa, Pb) > 8:
        M.line(c, *Pa, *Pb, ERRADO, falta, 6, dash=[14, 10])
    for P in (L, R):
        c.drawCircle(*P, 11 * a, M.paint(TINTA, a))
    return Pa, Pb


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    u = 120
    L, R = (560, 820), (560 + 6 * u, 820)

    def um():
        # os três palitos soltos, depois montados
        monta = ease_io(prog(t, kb - 1.5, 1.2))
        soltos = 1 - monta
        if soltos > 0 and t >= ka:
            for i, (n, cor) in enumerate(((2, E.COR), (3, TINTA2), (6, TINTA))):
                y = 360 + i * 150
                E.foco(c, t, ka + 0.3 * i, 0.5, lambda a, n=n, cor=cor, y=y: palito(c, (560, y), (560 + n * u, y), cor, a * soltos, f"{n} cm", -1))
        if monta > 0:
            palito(c, L, R, TINTA, monta, "6 cm", 0)
            g = 70 * ease_io(prog(t, kb - 0.6, 1.0))
            dobradica(c, L, R, 2 * u, 3 * u, g, g, E.COR, TINTA2, monta, ("2", "3"), ep(t, kc, 0.4))
        E.foco(c, t, kb, 0.5, lambda a: E.pilula(c, "não fecha", 1600, 420, 76, "g", fundo=ERRADO, a=a))
        E.frase(c, t, kc + 0.3, ps("não se", "i", 66) + [("alcançam", "g", 66, ERRADO)], 1600, 600, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), [("saber na hora", "g", 90, COR)], XE, 440, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("se forma triângulo", "i", 76), XE, 550, passo=0.12)
        E.frase(c, t, tb, [("achar", "g", 96)] + ps("o terceiro lado", "i", 84), XE, 720, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 820
    itens = (("s03.b", "triângulo:", "3 lados que se fecham"), ("s03.c", "inequação dupla", "3 < x < 13"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 160)
    py = lerp(420, 700, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 920, "left", 0.12)


# ---------------- por que não fecha ----------------
def b_palitos(c, t, C, b):
    u = 125
    L, R = (240, 800), (240 + 6 * u, 800)
    X = 1500
    a4, b4, a5, b5, c5, d5 = C["s04.a"], C["s04.b"], C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]

    def fig():
        E.foco(c, t, a4, 0.5, lambda a: palito(c, L, R, TINTA, a, "6 cm", 0))
        # sobem, deitam sobre a base, sobem de novo
        g = 70 * ease_io(prog(t, b4, 1.0))
        g = g * (1 - ease_io(prog(t, a5, 1.0)))
        g = g + 55 * ease_io(prog(t, d5, 1.2))
        if t >= b4:
            Pa, Pb = dobradica(c, (L[0], L[1] - 18), (R[0], R[1] - 18), 2 * u, 3 * u, g, g, E.COR, TINTA2, ep(t, b4, 0.4), ("2", "3"), ep(t, b5, 0.4))
        if C["s05"] <= t < d5 + 0.3:
            q = ep(t, c5, 0.4) * (1 - ep(t, d5, 0.3))
            E.chave(c, L[0] + 2 * u, R[0] - 3 * u, L[1] + 110, ERRADO, q, 22)
            E.foco(c, t, c5 + 0.2, 0.4, lambda a: centro(c, "falta", (L[0] + 2 * u + R[0] - 3 * u) / 2, L[1] + 200, 48, "b", ERRADO, a * (1 - ep(t, d5, 0.3))))
        E.frase(c, t, b4, ps("tentam se encontrar", "i", 66), X, 260, "center", 0.12) if t < C["s05"] else None
        if t >= C["s05"]:
            E.frase(c, t, a5, ps("deitados sobre o maior:", "i", 60), X, 260, "center", 0.1)
            fcen(c, t, b5, "2 + 3 = 5", X, 410, 100)
            fcen(c, t, c5, "5 < 6", X, 560, 110, ERRADO)
            E.frase(c, t, d5, ps("levantando:", "i", 64) + [("mais longe", "g", 64, ERRADO)], X, 720, "center", 0.12)
    E.saida(c, t, C["s06"] - 0.1, fig)
    if t >= C["s06"]:
        A, B, Cc = (620, 300), (300, 820), (1060, 820)
        if t >= C["s06"]:
            p = ease_io(prog(t, C["s06"], 0.8))
            for P, Q in ((A, B), (B, Cc), (Cc, A)):
                M.line(c, *P, lerp(P[0], Q[0], p), lerp(P[1], Q[1], p), TINTA, 1.0, 6)
        if t >= b6:
            M.line(c, *B, *Cc, CERTO, ep(t, b6, 0.4), 14)
            E.foco(c, t, b6 + 0.3, 0.4, lambda a: centro(c, "direto", (B[0] + Cc[0]) / 2, B[1] + 80, 54, "g", CERTO, a))
        if t >= c6:
            q = ease_io(prog(t, c6, 1.2))
            M.line(c, *B, lerp(B[0], A[0], min(1, q * 2)), lerp(B[1], A[1], min(1, q * 2)), ERRADO, 1.0, 10, dash=[18, 12])
            if q > 0.5:
                f = (q - 0.5) * 2
                M.line(c, *A, lerp(A[0], Cc[0], f), lerp(A[1], Cc[1], f), ERRADO, 1.0, 10, dash=[18, 12])
            E.foco(c, t, c6 + 1.0, 0.4, lambda a: centro(c, "a volta", A[0], A[1] - 40, 54, "g", ERRADO, a))
        E.frase(c, t, a6, ps("cada lado", "i", 66), X, 260, "center", 0.12)
        E.frase(c, t, a6 + 0.8, [("menor que a soma", "g", 64, COR)], X, 360, "center")
        E.frase(c, t, a6 + 1.4, ps("dos outros dois", "i", 66), X, 450, "center", 0.12)
        E.frase(c, t, b6, ps("o caminho reto", "i", 66), X, 640, "center", 0.12)
        E.frase(c, t, b6 + 0.8, [("é o mais curto", "g", 66, CERTO)], X, 740, "center")


# ---------------- soma igual: achatado ----------------
def b_achatado(c, t, C, b):
    u = 125
    L, R = (240, 760), (240 + 5 * u, 760)
    X = 1450
    a7, b7, c7, d7, a8, b8 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s08.a"], C["s08.b"]
    E.frase(c, t, a7, ps("e se a soma der", "i", 66) + [("igual?", "g", 70, COR)], X, 240, "center", 0.12)
    if t >= b7:
        palito(c, L, R, TINTA, ep(t, b7, 0.4), "5 cm", 0)
        g = 60 * (1 - ease_io(prog(t, c7, 1.2)))
        dobradica(c, (L[0], L[1] - 18), (R[0], R[1] - 18), 2 * u, 3 * u, g, g, E.COR, TINTA2, ep(t, b7 + 0.3, 0.4), ("2", "3"))
    fcen(c, t, b7 + 1.6, "2 + 3 = 5", X, 400, 96)
    E.frase(c, t, c7, [("achatados", "g", 76, ERRADO)], X, 540, "center")
    E.frase(c, t, d7, ps("vira uma", "i", 66) + [("linha", "g", 70, ERRADO)], X, 660, "center", 0.12)
    if t >= C["s08"]:
        E.foco(c, t, a8, 0.5, lambda a: E.pilula(c, "soma dos menores > maior", W / 2, 920, 56, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, b8, [("igual não serve", "g", 66, ERRADO)], X, 800, "center")


# ---------------- o terceiro lado ----------------
def b_terceiro(c, t, C, b):
    X, PX = 1300, 1700
    a9, b9, a10, b10 = C["s09.a"], C["s09.b"], C["s10.a"], C["s10.b"]
    a11, b11, c11, a12, b12 = C["s11.a"], C["s11.b"], C["s11.c"], C["s12.a"], C["s12.b"]
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    B, Cc = (200, 600), (200 + 8 * 70, 600)
    A = pt(B, 5 * 70, 55)
    # o triângulo: 5 e 8 conhecidos, x é o terceiro
    E.foco(c, t, a9, 0.5, lambda a: (palito(c, B, Cc, TINTA, a, "8", 1, larg=12), palito(c, B, A, E.COR, a, "5", -1, larg=12)))
    E.foco(c, t, b9, 0.5, lambda a: palito(c, A, Cc, TINTA2, a, "x", -1, larg=12))
    E.frase(c, t, a9, ps("lados de", "i", 60) + [("5 e 8", "g", 64, COR)], 480, 180, "center", 0.12)

    def contas():
        fcen(c, t, a10, "x < 5 + 8", X, 220, 84)
        fcen(c, t, b10, "x < 13", X, 320, 84, COR)
        fcen(c, t, a11, "8 < 5 + x", X, 460, 84)
        operacao(c, t, b11, "− 5", PX, 500)
        fcen(c, t, c11, "3 < x", X, 560, 84, COR)
        E.frase(c, t, c11 + 1.5, ps("5 < 8 + x: passa sozinho", "b", 44, TINTA2), X, 650, "center", 0.06)
    E.saida(c, t, C["s12"] - 0.1, contas)
    vy = 880
    if t >= C["s12"]:
        def juntos():
            fcen(c, t, a12, "3 < x < 13", X, 300, 110, COR)
            E.frase(c, t, b12, ps("entre 3 e 13,", "i", 64) + [("sem as pontas", "g", 64, COR)], X, 440, "center", 0.12)
        E.saida(c, t, C["s13"] - 0.1, juntos)
        vx = E.reta(c, t, a12, 200, 1700, vy, 0, 15, list(range(0, 16)), size=40)
        E.intervalo(c, t, a12 + 0.6, vx, vy, 3, 13)
        # os inteiros que entram
        if t >= b13:
            for i, v in enumerate(range(4, 13)):
                k = ease_back(prog(t, b13 + 0.12 * i, 0.3))
                if k > 0:
                    c.drawCircle(vx(v), vy, 13 * k, M.paint(CERTO))
    if t >= C["s13"]:
        E.frase(c, t, a13, ps("lado", "i", 64) + [("inteiro:", "g", 66, COR)], X, 240, "center", 0.12)
        fcen(c, t, b13, "4, 5, 6, ..., 12", X, 360, 80, CERTO)
        fcen(c, t, c13, "12 − 4 + 1", X, 500, 84)
        E.frase(c, t, c13 + 1.6, ps("o 4 também entra", "i", 50, TINTA2), X, 580, "center", 0.1)
        bola_txt(c, t, d13, "9", X - 120, 700, 80, 90, CERTO)
        E.frase(c, t, d13 + 0.2, [("valores", "g", 70, CERTO)], X + 90, 725, "center")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a14, b14, c14, a15, b15, c15 = C["s14.a"], C["s14.b"], C["s14.c"], C["s15.a"], C["s15.b"], C["s15.c"]
    vy = 330
    E.frase(c, t, C["s14"], [("cuidado", "g", 90, ERRADO)] + ps("com as pontas", "i", 84), W / 2, 140, "center", 0.12)
    vx = E.reta(c, t, C["s14"] + 0.3, 200, 1700, vy, 0, 15, list(range(0, 16)), size=40)
    E.intervalo(c, t, b14, vx, vy, 3, 13, True, True, cor=ERRADO)
    E.frase(c, t, b14 + 0.6, ps("de 3 até 13", "b", 56, ERRADO), 700, 520, "center", 0.1)
    E.frase(c, t, c14, [("11 valores", "g", 64, ERRADO)], 1200, 520, "center")
    # a ponta 3: palitos de 3, 5 e 8 ficam achatados
    u = 70
    L, R = (240, 820), (240 + 8 * u, 820)
    if t >= a15:
        palito(c, L, R, TINTA, ep(t, a15, 0.4), "8", 0, larg=14)
        dobradica(c, (L[0], L[1] - 16), (R[0], R[1] - 16), 3 * u, 5 * u, 0, 0, E.COR, TINTA2, ep(t, a15 + 0.3, 0.4), ("3", "5"))
    X = 1360
    fcen(c, t, b15, "3 + 5 = 8", X, 720, 80)
    E.frase(c, t, b15 + 1.2, [("achatado", "g", 64, ERRADO)], X, 810, "center")
    fcen(c, t, c15, "5 + 8 = 13: achatado", X, 940, 64, ERRADO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a16, b16, a17 = C["s16.a"], C["s16.b"], C["s17.a"]
    a18, b18, c18, d18, e18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"], C["s18.e"]

    def parte1():
        E.frase(c, t, C["s16"] + 0.5, ps("atalho em", "i", 70, CLARO) + [("2 partes", "g", 74, BR)], W / 2, 200, "center", 0.12)
        E.frase(c, t, a16, [("1.", "g", 70, CLARO)] + ps("com 3 medidas:", "i", 70, CLARO) + [("teste só o maior", "g", 70, BR)], W / 2, 400, "center", 0.12)
        fcen(c, t, b16, "maior < soma dos outros?", W / 2, 540, 80, BR)
        E.frase(c, t, a17, ps("os menores", "i", 66, CLARO) + [("passam sozinhos", "g", 66, BR)], W / 2, 760, "center", 0.12)
    E.saida(c, t, C["s18"] - 0.1, parte1)
    if t >= C["s18"]:
        E.frase(c, t, a18, [("2.", "g", 70, CLARO)] + ps("com 2 lados:", "i", 70, CLARO), W / 2, 200, "center", 0.12)
        fcen(c, t, a18 + 1.0, "diferença < x < soma", W / 2, 330, 84, BR)
        fcen(c, t, b18, "8 − 5 = 3", 660, 490, 84, CLARO)
        fcen(c, t, c18, "8 + 5 = 13", 1260, 490, 84, CLARO)
        E.frase(c, t, d18, ps("a questão pede mais? ex.:", "i", 62, CLARO) + [("isósceles", "g", 64, BR)], W / 2, 690, "center", 0.1)
        E.frase(c, t, e18, ps("o terceiro lado", "i", 64, CLARO) + [("repete 5 ou 8", "g", 70, BR)], W / 2, 830, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a19, ps("lados de", "i", 80) + [("4 e 9 cm", "g", 84, COR)], XE, 380, passo=0.12)
    E.frase(c, t, b19, ps("o terceiro:", "i", 80) + [("inteiro", "g", 84)], XE, 540, passo=0.12)
    E.frase(c, t, c19, ps("quantos", "i", 96) + [("valores?", "g", 100, COR)], XE, 760, passo=0.14)

    def fig():
        B, Cc = (1150, 640), (1150 + 9 * 60, 640)
        A = pt(B, 4 * 60, 70)
        E.foco(c, t, a19, 0.5, lambda a: (palito(c, B, Cc, TINTA, a, "9", 1, larg=12), palito(c, B, A, E.COR, a, "4", -1, larg=12)))
        E.foco(c, t, b19, 0.5, lambda a: palito(c, A, Cc, TINTA2, a, "x", -1, larg=12))
    E.saida(c, t, C["s20.a"] - 0.1, fig)
    E.relogio(c, t, C["s20.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    X = W / 2
    a21, b21, c21, d21, a22, b22, c22 = (C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"], C["s22.a"], C["s22.b"], C["s22.c"])
    vy = 860
    fcen(c, t, a21, "9 − 4 = 5", 600, 220, 88)
    fcen(c, t, b21, "9 + 4 = 13", 1320, 220, 88)
    fcen(c, t, c21, "5 < x < 13", X, 380, 110, COR)
    vx = E.reta(c, t, c21, 200, 1700, vy, 0, 15, list(range(0, 16)), size=40)
    E.intervalo(c, t, c21 + 0.5, vx, vy, 5, 13)
    if t >= d21:
        for i, v in enumerate(range(6, 13)):
            k = ease_back(prog(t, d21 + 0.15 * i, 0.3))
            if k > 0:
                c.drawCircle(vx(v), vy, 13 * k, M.paint(CERTO))
    fcen(c, t, d21, "6, 7, ..., 12", 600, 560, 76, CERTO)
    fcen(c, t, a22, "12 − 6 + 1", 1250, 560, 80)
    bola_txt(c, t, b22, "7", 1130, 690, 70, 84, CERTO)
    E.frase(c, t, b22 + 0.2, [("valores", "g", 64, CERTO)], 1330, 712, "center")
    E.frase(c, t, c22, ps("com as pontas:", "i", 56, ERRADO) + [("9, errado", "g", 56, ERRADO)], 560, 712, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s23.a", "maior < soma dos outros"), ("s23.b", "diferença < x < soma"))
        for i, (k, s) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 420, y - 30, 56, a=a), centro(c, str(i + 1), 420, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 520, y)
        E.frase(c, t, C["s23.b"] + 2.0, ps("sem as pontas", "i", 66, COR), 520, 790)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24.a"], ps("hoje:", "i", 70) + [("o triângulo existe?", "g", 70)], XE, 230, passo=0.12)
    E.frase(c, t, C["s24.b"] - 0.8, ps("próxima aula", "i", 84), XE, 380)
    E.frase(c, t, C["s24.b"], [("Triângulos", "g", 130, COR)], XE, 520)
    E.frase(c, t, C["s24.b"] + 0.3, [("iguais", "g", 130, COR)], XE, 650)
    E.frase(c, t, C["s24.b"] + 1.5, ps("os casos de", "i", 70) + [("congruência", "g", 70)], XE, 760, passo=0.12)
    E.frase(c, t, C["s24.c"], ps("e o lado ou ângulo que falta", "i", 60, TINTA2), XE, 850, passo=0.1)
    E.foco(c, t, C["s24.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s24.d"] + 0.2, 0.4))
    E.frase(c, t, C["s24.e"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], 1450, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, palitos=b_palitos, achatado=b_achatado, terceiro=b_terceiro, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
