"""Visual — Estudativo · MAT-POL-006: ângulo central e ângulo inscrito (o inscrito vale a metade; na semicircunferência, é reto).
Linguagem da geometria plana (MAT-ANG-001 a 007, MAT-POL-001 a 005): circunferência em tinta (E.circulo); o ARCO aberto pelos
ângulos é o traço grosso na cor da matéria; o ângulo CENTRAL é da 1ª família (COR) e o INSCRITO da 2ª (TINTA2); raios e cordas
em tinta; lados iguais com tracinhos; medidas na grotesca; resposta na esfera; vermelho é erro, verde é certo.
"O central é a soma dos dois x": as duas cunhas x do triângulo isósceles voam (voa(), da MAT-ANG-002) e assentam lado a lado
no centro, preenchendo o ângulo central. Ângulo reto = quadradinho (E.angulo reconhece sozinho).
Peças locais: pt() (ponto da circunferência pelo ângulo da matemática), arco_cor(), seg(), dirg(), cunha_m(), voa(), meia_pizza().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polígonos e Círculo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POL-006_angulo_central_e_inscrito.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("central", "prova", "semi", "atalho", "questao", "fim"))
BR = "#FFFFFF"
MASSA = "#F3D9A4"
AMBAR = "#D98A00"
assert 100 // 2 == 50 and 180 // 2 == 90 and 2 * 35 == 70 and 35 / 2 == 17.5
assert 90 - 25 == 65 and 2 * 25 == 50 and 25 + 65 == 90


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


def pt(O, r, g):
    return O[0] + r * math.cos(math.radians(g)), O[1] - r * math.sin(math.radians(g))


def dirg(V, P):
    return math.degrees(math.atan2(-(P[1] - V[1]), P[0] - V[0]))


def arco_cor(c, O, r, g1, g2, cor=None, larg=16, a=1.0, p=1.0):
    if a <= 0 or p <= 0:
        return
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    c.drawArc(ret, -g1, -(g2 - g1) * p, False, M.paint(cor or E.COR, a, stroke=larg, cap_round=True))


def seg(c, t, t0, P, Q, cor=TINTA, larg=6, d=0.5, a=1.0, dash=None):
    if t >= t0 and a > 0:
        M.line(c, *P, *Q, cor, a, larg, dash=dash, progress=ease_io(prog(t, t0, d)))


def ponto(c, t, t0, P, nome=None, lado=(0, -1), cor=TINTA, size=56, a=1.0):
    k = ease_back(prog(t, t0, 0.35))
    if k > 0 and a > 0:
        c.drawCircle(*P, 11 * k, M.paint(cor, a))
    if nome:
        E.foco(c, t, t0, 0.4, lambda f: E._cola(c, nome, P[0], P[1], lado[0], lado[1], 16, size, "g", cor, f * a))


def cunha_m(c, V, g1, g2, r, cor, a=1.0, alfa=0.3, borda=6):
    if a <= 0:
        return
    ret = skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r)
    path = skia.Path()
    path.moveTo(*V); path.arcTo(ret, -g1, -(g2 - g1), False); path.close()
    c.drawPath(path, M.paint(cor, alfa * a))
    if borda:
        p = M.paint(cor, a, stroke=borda, cap_round=True)
        p.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(path, p)


def voa(c, t, t0, d, V0, g1, g2, r, cor=None, V1=None, giro=0.0, fica=0.8):
    """o ângulo se move (ver MAT-ANG-002): a cunha sai de V0, gira e viaja até V1, deixando o contorno tracejado na origem"""
    if t < t0 or t > t0 + d + fica + 0.4:
        return
    cor = cor or E.COR
    V1 = V1 or V0
    p = ease_io(prog(t, t0, d))
    a = 1 - ep(t, t0 + d + fica, 0.4)
    ret = skia.Rect.MakeXYWH(V0[0] - r, V0[1] - r, 2 * r, 2 * r)
    tr = M.paint(cor, 0.8 * a, stroke=3)
    tr.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
    path = skia.Path(); path.moveTo(*V0); path.arcTo(ret, -g1, -(g2 - g1), False); path.close()
    c.drawPath(path, tr)
    lift = 1 + 0.08 * math.sin(math.pi * p)
    c.save()
    c.translate(lerp(V0[0], V1[0], p), lerp(V0[1], V1[1], p))
    c.rotate(-giro * p)
    c.scale(lift, lift)
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.25 * a * math.sin(math.pi * p)))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
    path2 = skia.Path(); path2.moveTo(0, 0); path2.arcTo(skia.Rect.MakeXYWH(-r, -r, 2 * r, 2 * r), -g1, -(g2 - g1), False); path2.close()
    c.save(); c.translate(6, 12); c.drawPath(path2, s); c.restore()
    cunha_m(c, (0, 0), g1, g2, r, cor, a, alfa=0.55)
    c.restore()


def meia_pizza(c, O, r, a=1.0):
    """meia pizza: o corte reto embaixo (diâmetro deitado) e a borda curva em cima"""
    if a <= 0:
        return
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    path = skia.Path(); path.moveTo(O[0] - r, O[1]); path.arcTo(ret, 180, 180, False); path.close()
    c.drawPath(path, M.paint(MASSA, a))
    for dx, dy in ((-0.5, -0.3), (0.1, -0.6), (0.45, -0.25), (-0.15, -0.2)):
        c.drawCircle(O[0] + dx * r, O[1] + dy * r, r * 0.08, M.paint("#C8553D", 0.7 * a))
    c.drawArc(ret, 180, 180, False, M.paint(AMBAR, a, stroke=max(8, r * 0.05)))
    M.line(c, O[0] - r, O[1], O[0] + r, O[1], TINTA, a, 6)


def figura(c, t, t0, O, r, A, B, P, centro_=True, inscrito=True, tcen=None, tins=None, rot_c=None, rot_i=None,
           r_c=90, r_i=80, tarco=None, nomes=True):
    """central AOB (COR) e inscrito APB (TINTA2) sobre o mesmo arco de A até B (sentido anti-horário)"""
    E.circulo(c, t, t0, *O, r, o="O" if nomes else None, d=0.6)
    PA, PB, PP = pt(O, r, A), pt(O, r, B), pt(O, r, P)
    if tarco is not None:
        arco_cor(c, O, r, A, B, E.COR, 16, 1.0, ease_io(prog(t, tarco, 0.6)))
    if centro_ and tcen is not None:
        seg(c, t, tcen, O, PA); seg(c, t, tcen + 0.2, O, PB)
        E.angulo(c, t, tcen + 0.5, O, PA, PB, rot_c, r=r_c, cor=E.COR, size=56)
    if inscrito and tins is not None:
        seg(c, t, tins, PP, PA); seg(c, t, tins + 0.2, PP, PB)
        E.angulo(c, t, tins + 0.5, PP, PA, PB, rot_i, r=r_i, cor=TINTA2, size=56)
    return PA, PB, PP


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    O, r = (600, 760), 400
    X = 1450

    def um():
        meia_pizza(c, O, r, ep(t, ka, 0.5))
        A, B = (O[0] - r, O[1]), (O[0] + r, O[1])
        if t >= kb:
            # o ponto passeia pela borda: 120° → 60° → 150°
            g = 120
            if t >= kd:
                g = lerp(120, 45, ease_io(prog(t, kd, 0.9)))
                g = lerp(g, 155, ease_io(prog(t, kd + 1.1, 0.9))) if t >= kd + 1.1 else g
            P = pt(O, r, g)
            al = ep(t, kb, 0.4)
            M.line(c, *P, *A, TINTA, al, 6)
            M.line(c, *P, *B, TINTA, al, 6)
            c.drawCircle(*P, 13, M.paint(E.COR, al))
            if t >= kc:
                E.angulo(c, t, kc, P, A, B, None, r=70, cor=E.COR)
        E.frase(c, t, ka, [("meia", "g", 80, COR)] + ps("pizza", "i", 76), X, 260, "center", 0.12)
        E.frase(c, t, kb, ps("qualquer ponto", "i", 66) + [("da borda", "g", 70, COR)], X, 400, "center", 0.12)
        E.frase(c, t, kc, ps("o ângulo é", "i", 70) + [("reto", "g", 80, COR)], X, 580, "center", 0.12)
        E.frase(c, t, kd, ps("ponto aqui, ponto ali:", "i", 58), X, 740, "center", 0.12)
        E.frase(c, t, kd + 0.9, [("90°", "g", 110, COR)], X, 880, "center")
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1520, 560, 240 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 280, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), [("por que", "g", 110, COR)] + ps("isso acontece", "i", 84), XE, 430, passo=0.14)
        E.frase(c, t, tb, ps("ângulos", "i", 84) + [("dentro", "g", 100, COR)], XE, 600, passo=0.14)
        E.frase(c, t, tb + 0.6, ps("da circunferência", "i", 84), XE, 720, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1520, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1520, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "externo do triângulo =", "soma dos internos de longe"), ("s03.c", "no isósceles:", "ângulos da base iguais"),
             ("s03.d", "ângulo central:", "vértice no centro"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.4, [(l2, "g", 54, COR)], x + 44, y + 160)
    alvo = [(x + w - 30, 170 + i * 240 + 170) for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, alvo[0][0], lerp(lerp(alvo[0][1], alvo[1][1], q1), alvo[2][1], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 960, "left", 0.12)


# ---------------- central ----------------
O1, R1 = (600, 560), 330
GA, GB, GP = -20, 80, 230  # arco de A até B = 100°; P do outro lado


def b_central(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    X = 1450
    PA, PB, _ = figura(c, t, C["s04"], O1, R1, GA, GB, GP, inscrito=False, tcen=a4, tarco=b4, rot_c="100°" if t >= d4 else None, r_c=90)
    ponto(c, t, a4 + 0.4, PA, "A", (1, 0.3)); ponto(c, t, a4 + 0.6, PB, "B", (0.3, -1))
    E.foco(c, t, c4, 0.4, lambda a: centro(c, "100°", *pt(O1, R1 + 80, 30), 60, "g", COR, a))
    E.frase(c, t, a4, [("central:", "g", 72, COR)] + ps("os lados são raios", "i", 60), X, 280, "center", 0.12)
    E.frase(c, t, b4, ps("abre um", "i", 66) + [("arco", "g", 72, COR)], X, 430, "center", 0.12)
    E.frase(c, t, c4, ps("o arco também tem", "i", 60) + [("graus", "g", 66, COR)], X, 600, "center", 0.12)
    E.foco(c, t, d4, 0.5, lambda a: E.pilula(c, "arco = seu ângulo central", X, 780, 50, "g", a=a, cor=E.SOBRE))


# ---------------- inscrito ----------------
def b_inscrito(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    X = 1450
    PA, PB, PP = figura(c, t, C["s05"], O1, R1, GA, GB, GP, centro_=t >= a6, tcen=a6, tins=b5, tarco=c5,
                        rot_c="100°" if t >= c6 else None, rot_i="50°" if t >= d6 else None, r_c=90, r_i=110)
    ponto(c, t, C["s05"] + 0.4, PA, "A", (1, 0.3)); ponto(c, t, C["s05"] + 0.5, PB, "B", (0.3, -1))
    if t >= a5:
        pulsa = 1 + 0.5 * math.sin(math.pi * M.clamp(prog(t, a5, 0.8)))
        c.drawCircle(*PP, 13 * pulsa, M.paint(TINTA2))
        E.foco(c, t, a5, 0.4, lambda f: E._cola(c, "P", PP[0], PP[1], -0.7, 0.7, 16, 56, "g", TINTA, f))

    def cinco():
        E.frase(c, t, a5, [("inscrito:", "g", 72, TINTA2)] + ps("vértice na borda", "i", 60), X, 280, "center", 0.12)
        E.frase(c, t, b5, ps("os lados são", "i", 60) + [("cordas", "g", 66, TINTA2)], X, 420, "center", 0.12)
        E.frase(c, t, b5 + 1.0, ps("(ligam 2 pontos da borda)", "i", 48, TINTA2), X, 500, "center", 0.1)
        E.frase(c, t, c5, ps("abre o", "i", 60) + [("arco", "g", 66, COR)] + ps("do outro lado", "i", 60), X, 650, "center", 0.12)
    E.saida(c, t, C["s06"] - 0.1, cinco)
    if t >= C["s06"]:
        E.frase(c, t, a6, [("o mesmo arco", "g", 70, COR)], X, 270, "center")
        E.frase(c, t, b6, [("inscrito", "g", 70, TINTA2)] + ps("= metade do", "i", 64) + [("central", "g", 70, COR)], X, 420, "center", 0.12)
        fcen(c, t, c6, "central: 100°", X, 600, 76, COR)
        fcen(c, t, d6, "inscrito: 50°", X, 740, 76, TINTA2)
        E.formula_em(c, t, d6 + 0.8, "50 = f{100}{2}", X, 900, 70, "g", None, "center")


# ---------------- por que a metade ----------------
GA2, GB2 = 20, 120
GP2 = GA2 + 180  # P do lado oposto de A: o lado PA passa pelo centro


def b_prova(c, t, C, b):
    a7, b7, c7, d7, e7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9, e9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]
    O, r = (600, 560), 330
    X = 1450
    E.circulo(c, t, C["s07"], *O, r, o=None, d=0.6)
    PA, PB, PP = pt(O, r, GA2), pt(O, r, GB2), pt(O, r, GP2)
    # o lado PA passa por O
    seg(c, t, a7, PP, PA, TINTA, 6, 0.7)
    ponto(c, t, a7 + 0.4, O, "O", (0.3, 1))
    ponto(c, t, b7, PP, "P", (-1, 0.3))
    ponto(c, t, b7 + 0.3, PA, "A", (1, -0.2)); ponto(c, t, b7 + 0.5, PB, "B", (-0.3, -1))
    seg(c, t, b7 + 0.6, PP, PB, TINTA, 6, 0.5)
    arco_cor(c, O, r, GA2, GB2, E.COR, 16, 1.0, ease_io(prog(t, b7 + 0.8, 0.6)))
    seg(c, t, c7, O, PB, TINTA, 6, 0.5)
    if t >= d7:
        path = skia.Path(); path.addPoly([O, PP, PB], True)
        c.drawPath(path, M.paint(AMBAR, 0.18 * ep(t, d7, 0.5)))
    E.marcas_iguais(c, O, PP, 1, TINTA, ep(t, e7, 0.4))
    E.marcas_iguais(c, O, PB, 1, TINTA, ep(t, e7 + 0.2, 0.4))
    # os dois x do isósceles (2ª família)
    gP1, gP2 = dirg(PP, PA), dirg(PP, PB)
    gB1, gB2 = dirg(PB, PP), dirg(PB, O)
    xP = "x" if t >= c8 else None
    E.angulo(c, t, a8, PP, PA, PB, xP, r=110, cor=TINTA2, size=60)
    E.angulo(c, t, b8, PB, PP, O, xP, r=90, cor=TINTA2, size=60)
    # o central AOB, fora do triângulo
    if t >= a9:
        E.angulo(c, t, b9, O, PA, PB, "2x" if t >= d9 + 2.6 else None, r=90, cor=E.COR, size=60)
    if t >= d9:
        voa(c, t, d9, 1.2, PP, gP1, gP2, 90, TINTA2, V1=O, giro=0.0, fica=1.2)
        voa(c, t, d9 + 0.6, 1.2, PB, gB1, gB2, 90, TINTA2, V1=O, giro=(GA2 + 50) - gB1, fica=1.2)

    def sete():
        E.frase(c, t, a7, ps("um lado passa pelo", "i", 58) + [("centro O", "g", 64, COR)], X, 260, "center", 0.12)
        E.frase(c, t, b7, ps("vértice", "i", 58) + [("P;", "g", 64), ("arco", "i", 58), ("de A até B", "g", 64, COR)], X, 380, "center", 0.12)
        E.frase(c, t, c7, ps("ligue", "i", 58) + [("O a B", "g", 64)], X, 500, "center", 0.12)
        E.frase(c, t, d7, ps("triângulo", "i", 58) + [("OPB", "g", 64, AMBAR)], X, 620, "center", 0.12)
        E.frase(c, t, e7, ps("OP e OB são raios:", "i", 54), X, 760, "center", 0.1)
        E.frase(c, t, e7 + 0.6, [("isósceles", "g", 70, AMBAR)], X, 860, "center")
    E.saida(c, t, C["s08"] - 0.1, sete)

    def oito():
        E.frase(c, t, a8, ps("ângulos da base", "i", 60) + [("iguais", "g", 66, TINTA2)], X, 300, "center", 0.12)
        E.frase(c, t, b8, ps("em P (o inscrito)", "i", 58) + [("= em B", "g", 62, TINTA2)], X, 440, "center", 0.12)
        E.frase(c, t, c8, ps("cada um:", "i", 60) + [("x", "g", 80, TINTA2)], X, 600, "center", 0.12)
    if t >= C["s08"]:
        E.saida(c, t, C["s09"] - 0.1, oito)

    if t >= C["s09"]:
        E.frase(c, t, a9, ps("o central fica", "i", 58) + [("de fora", "g", 64, COR)], X, 220, "center", 0.12)
        E.frase(c, t, b9, ps("é um", "i", 60) + [("ângulo externo", "g", 64, COR)], X, 340, "center", 0.12)
        E.frase(c, t, c9, ps("= soma dos internos de longe", "i", 52), X, 450, "center", 0.1)
        fcen(c, t, d9, "x + x = 2x", X, 600, 96, COR)
        E.foco(c, t, e9, 0.5, lambda a: E.pilula(c, "central = 2 × inscrito", X, 760, 54, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, lerp(e9, C["s09.end"], 0.4), ps("com o centro em outro lugar,", "i", 46, TINTA2), X, 900, "center", 0.08)
        E.frase(c, t, lerp(e9, C["s09.end"], 0.5), ps("a regra continua valendo", "i", 46, TINTA2), X, 970, "center", 0.08)


# ---------------- semicircunferência ----------------
def b_semi(c, t, C, b):
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    a11, b11 = C["s11.a"], C["s11.b"]
    O, r = (600, 620), 360
    X = 1450
    E.circulo(c, t, C["s10"], *O, r, o="O", d=0.6)
    A, B = pt(O, r, 180), pt(O, r, 0)
    seg(c, t, a10, A, B, TINTA, 7, 0.6)
    ponto(c, t, a10 + 0.3, A, "A", (-1, 0)); ponto(c, t, a10 + 0.4, B, "B", (1, 0))
    arco_cor(c, O, r, 0, 180, E.COR, 16, 1.0, ease_io(prog(t, b10, 0.8)))
    if t >= c10:
        E.angulo(c, t, c10, O, B, A, "180°" if t < C["s11"] else None, r=70, cor=E.COR, size=56)
    if t >= C["s11"]:
        g = 115
        if t >= b11:
            g = lerp(115, 50, ease_io(prog(t, b11, 1.0)))
            g = lerp(g, 150, ease_io(prog(t, b11 + 1.4, 1.0))) if t >= b11 + 1.4 else g
        P = pt(O, r, g)
        al = ep(t, C["s11"], 0.4)
        M.line(c, *P, *A, TINTA2, al, 6); M.line(c, *P, *B, TINTA2, al, 6)
        c.drawCircle(*P, 13, M.paint(TINTA2, al))
        E.angulo(c, t, a11, P, A, B, None, r=64, cor=TINTA2)

    def dez():
        E.frase(c, t, a10, ps("o corte reto:", "i", 60) + [("diâmetro", "g", 66, COR)], X, 280, "center", 0.12)
        E.frase(c, t, b10, [("semicircunferência", "g", 62, COR)], X, 420, "center")
        E.frase(c, t, b10 + 0.8, ps("meia volta", "i", 58), X, 500, "center")
        E.frase(c, t, c10, ps("central = linha reta:", "i", 56) + [("180°", "g", 66, COR)], X, 660, "center", 0.12)
    E.saida(c, t, C["s11"] - 0.1, dez)
    if t >= C["s11"]:
        fcen(c, t, a11, "180 ÷ 2 = 90°", X, 360, 96, TINTA2)
        E.frase(c, t, b11, ps("todo inscrito na", "i", 60), X, 560, "center", 0.12)
        E.frase(c, t, b11 + 0.6, [("semicircunferência", "g", 62, COR)], X, 660, "center")
        E.frase(c, t, b11 + 1.0, ps("é", "i", 60) + [("reto", "g", 80, COR)], X, 790, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a12, b12, c12, d12, e12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
    O, r = (560, 620), 300
    X = 1380
    E.frase(c, t, C["s12"], [("cuidado", "g", 92, ERRADO)] + ps("com este erro", "i", 86), W / 2, 150, "center", 0.14)
    E.frase(c, t, a12, [("dividir", "g", 66, ERRADO)] + ps("quando devia", "i", 62) + [("multiplicar", "g", 66, CERTO)], W / 2, 260, "center", 0.12)
    figura(c, t, b12 - 0.4, O, r, -35, 35, 180, centro_=t >= d12, tcen=d12, tins=b12, tarco=b12 + 0.4,
           rot_c="70°" if t >= e12 else "?", rot_i="35°", r_c=80, r_i=110, nomes=False)
    fcen(c, t, c12, "35 ÷ 2 = 17,5°", X, 440, 80, ERRADO)
    if t >= d12:
        E.risco(c, X - 300, 460, X + 300, 400, t, d12, largura=12)
    E.frase(c, t, d12, ps("o central é", "i", 60) + [("sempre o maior", "g", 66, COR)], X, 590, "center", 0.12)
    fcen(c, t, e12, "2 × 35 = 70°", X, 760, 96, CERTO)
    E.foco(c, t, e12 + 0.8, 0.5, lambda a: E.selo(c, X, 900, 55 * ease_back(prog(t, e12 + 0.8, 0.5)), True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    O, r = (560, 600), 320
    X = 1400

    def treze():
        if t >= C["s13"]:
            c.drawCircle(*O, r, M.paint(BR, ep(t, C["s13"], 0.4), stroke=6))
            c.drawCircle(*O, 9, M.paint(BR, ep(t, C["s13"], 0.4)))
        A, B, P = pt(O, r, 180), pt(O, r, 0), pt(O, r, 125)
        if t >= a13:
            E.poligono(c, t, a13, [A, B, P], None, preenche=0.0, d=0.7, escuro=True)
            M.line(c, *A, *B, CLARO, ep(t, a13 + 0.6, 0.4), 12)
        E.angulo(c, t, b13, P, A, B, "90°", r=60, cor=CLARO, size=54)
        E.angulo(c, t, c13, A, B, P, None, r=90, cor=BR)
        E.angulo(c, t, c13 + 0.3, B, P, A, None, r=80, cor=BR)
        E.frase(c, t, a13, ps("um lado no", "i", 64, CLARO) + [("diâmetro,", "g", 70, BR)], X, 260, "center", 0.12)
        E.frase(c, t, a13 + 1.0, ps("o vértice na borda", "i", 64, CLARO), X, 360, "center", 0.12)
        E.frase(c, t, b13, [("reto,", "g", 90, BR)] + ps("sem conta", "i", 76, CLARO), X, 540, "center", 0.12)
        E.frase(c, t, c13, ps("os outros dois", "i", 60, CLARO), X, 720, "center", 0.12)
        E.frase(c, t, c13 + 0.6, [("somam 90°", "g", 80, BR)], X, 830, "center")
    E.saida(c, t, C["s14"] - 0.1, treze)
    if t >= C["s14"]:
        fcen(c, t, a14, "180 ÷ 2 = 90", X, 260, 90, BR)
        E.frase(c, t, a14 + 1.0, ps("o diâmetro abre meia volta", "i", 56, CLARO), X, 360, "center", 0.1)
        if t >= b14:
            c.drawCircle(*O, r, M.paint(BR, ep(t, b14, 0.4), stroke=6))
            c.drawCircle(*O, 9, M.paint(BR, ep(t, b14, 0.4)))
            A, B, P = pt(O, r, 200), pt(O, r, -20), pt(O, r, 110)
            E.poligono(c, t, b14, [A, B, P], None, preenche=0.0, d=0.7, escuro=True)
            E.angulo(c, t, b14 + 0.8, P, A, B, None, r=60, cor=ERRADO)
            E.frase(c, t, b14, ps("corda qualquer:", "i", 60, CLARO) + [("não vale", "g", 70, ERRADO)], X, 560, "center", 0.12)
        E.foco(c, t, c14, 0.5, lambda a: E.pilula(c, "volte para a metade do central", X, 760, 50, "g", fundo=E.mix(E.COR, BR, 0.25), a=a))


# ---------------- questão ----------------
OQ, RQ = (560, 600), 320


def fig_q(c, t, t0, rC=None, rB=None, rcen=None, tC=None, tB=None, tcen=None, tarco=None, tA=None):
    E.circulo(c, t, t0, *OQ, RQ, o="O", d=0.6)
    A, B, Cc = pt(OQ, RQ, 180), pt(OQ, RQ, 0), pt(OQ, RQ, 50)
    seg(c, t, t0 + 0.4, A, B, TINTA, 6, 0.6)
    ponto(c, t, t0 + 0.6, A, "A", (-1, 0)); ponto(c, t, t0 + 0.7, B, "B", (1, 0))
    if tC is not None and t >= tC - 0.6:
        ponto(c, t, tC - 0.6, Cc, "C", (0.5, -1))
        seg(c, t, tC - 0.4, A, Cc, TINTA, 6, 0.5); seg(c, t, tC - 0.2, B, Cc, TINTA, 6, 0.4)
    if tarco is not None:
        arco_cor(c, OQ, RQ, 0, 50, E.COR, 16, 1.0, ease_io(prog(t, tarco, 0.6)))
    if tA is not None:
        E.angulo(c, t, tA, A, B, Cc, "25°", r=120, cor=TINTA2, size=52)
    if rC is not None:
        E.angulo(c, t, rC[1], Cc, A, B, rC[0], r=60, cor=E.COR if rC[0] != "?" else TINTA2, size=54)
    if rB is not None:
        E.angulo(c, t, rB[1], B, Cc, A, rB[0], r=70, cor=TINTA2, size=54)
    if tcen is not None and t >= tcen:
        seg(c, t, tcen, OQ, Cc, E.COR, 6, 0.4)
        E.angulo(c, t, tcen + 0.3, OQ, B, Cc, rcen, r=48, cor=E.COR, size=50)
    return A, B, Cc


def b_questao(c, t, C, b):
    a15, b15, c15, d15, e15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    fig_q(c, t, a15 - 0.6, rC=("?", d15), rB=("?", d15 + 0.2), rcen="?", tC=b15, tcen=e15, tA=c15)
    X = 1060
    E.frase(c, t, a15, [("AB", "g", 60), ("diâmetro,", "i", 58)], X, 320, "left", 0.12)
    E.frase(c, t, b15, [("C", "g", 60), ("na circunferência", "i", 58)], X, 410, "left", 0.12)
    E.frase(c, t, c15, ps("ângulo em", "i", 58) + [("A = 25°", "g", 60, TINTA2)], X, 500, "left", 0.12)
    E.frase(c, t, d15, ps("em", "i", 58) + [("C", "g", 60), ("e em", "i", 58), ("B?", "g", 60, COR)], X, 620, "left", 0.12)
    E.frase(c, t, e15, ps("e o central", "i", 58) + [("BOC?", "g", 60, COR)], X, 710, "left", 0.12)
    E.relogio(c, t, C["s16.a"], 1500, 830, 110)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a17, b17 = C["s17.a"], C["s17.b"]
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]
    X = 1400
    A, B, Cc = fig_q(c, t, C["s17"], rC=("90°", a17), rB=(None, b17 + 0.4), rcen="50°" if t >= c18 else None, tC=C["s17"] + 0.9,
                     tcen=b18 if t >= b18 else None, tarco=a18, tA=C["s17"] + 0.8)
    # o rótulo 65° sai quando o central entra, para não encostar no 50°
    E.saida(c, t, C["s18"], lambda: E.angulo(c, t, b17 + 0.4, B, Cc, A, "65°", r=70, cor=TINTA2, size=54))

    def dezessete():
        E.frase(c, t, C["s17"] + 0.3, ps("lado no diâmetro, vértice na borda", "i", 50), X, 240, "center", 0.1)
        E.frase(c, t, a17, ps("em C:", "i", 64) + [("90°", "g", 80, COR)], X, 400, "center", 0.12)
        fcen(c, t, b17, "em B: 90 − 25 = 65°", X, 560, 76, TINTA2)
    E.saida(c, t, C["s18"] - 0.1, dezessete)
    if t >= C["s18"]:
        E.frase(c, t, a18, ps("o inscrito em A abre o", "i", 54) + [("arco BC", "g", 60, COR)], X, 260, "center", 0.1)
        E.frase(c, t, b18, ps("o central", "i", 58) + [("BOC", "g", 62, COR)] + ps("abre o mesmo", "i", 58), X, 400, "center", 0.12)
        fcen(c, t, c18, "2 × 25 = 50°", X, 580, 96, COR)
        bola_txt(c, t, c18 + 0.9, "50°", X, 780, 100, 72)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s19.a", "inscrito = metade", "do central do mesmo arco"), ("s19.b", "na semicircunferência,", "o inscrito é reto"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 460 + i * 230
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 28, 54, a=a), centro(c, str(i + 1), 260, y - 6, 62, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 70, COR), (l2, "i", 70)], 360, y, "left", 0.2)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s20"] + 0.8, [("Reta e", "g", 130, COR)], XE, 440)
    E.frase(c, t, C["s20"] + 1.1, [("circunferência", "g", 130, COR)], XE, 570)
    E.frase(c, t, C["s20.a"], ps("longe, encosta ou corta", "i", 66), XE, 690, passo=0.12)
    E.frase(c, t, C["s20.b"], ps("a que encosta:", "i", 66) + [("reta com o raio", "g", 66)], XE, 790, passo=0.12)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, central=b_central, inscrito=b_inscrito, prova=b_prova, semi=b_semi,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
