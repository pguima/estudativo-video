"""Visual — Estudativo · MAT-TRA-006: equações e inequações trigonométricas (sen x = 1/2 → π/6 e 5π/6; cos x = √2/2 → π/4 e
7π/4; sen x > 1/2 → ]π/6, 5π/6[; 2 sen² x − 3 sen x + 1 = 0 → π/2, π/6, 5π/6; questão 2 cos x − 1 = 0 → π/3 e 5π/3).
Linguagem do ciclo (MAT-TRI-007, 008 e 009): eixos com seta, seno na altura em âmbar (OPO), cosseno na horizontal em petróleo (ADJ).
A equação é uma LINHA no ciclo: horizontal tracejada na altura do seno, vertical na horizontal do cosseno; as soluções são os
pontos onde ela corta. A inequação é o ARCO verde grosso acima (ou abaixo) da linha, com bolinha aberta nas pontas que não entram
e cheia nas que entram, como na reta da MAT-CON-007. O espelho do parceiro é o eixo tracejado na cor da matéria.
A figura não mente: os pontos estão nos ângulos de verdade e as linhas na altura certa.
Peças locais: ps(), cf(), cf_em(), resp(), lista(), pt(), ciclo(), ponto(), linha_h(), linha_v(), arco_sol(), aberta().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
from fractions import Fraction as F
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria Avançada")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRA-006_equacoes_e_inequacoes_trigonometricas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("equacao", "inequacao", "segundo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OPO, ADJ, TG = "#D98A00", "#0E9AA7", "#C0187C"
OPO_ESC, ADJ_ESC, TG_ESC = "#F2B33D", "#3CC7D3", "#F062B5"
S = lambda g: math.sin(math.radians(g))
Cs = lambda g: math.cos(math.radians(g))
assert abs(S(30) - 0.5) < 1e-12 and abs(S(150) - 0.5) < 1e-12 and 180 - 30 == 150 == 5 * 30
assert abs(Cs(45) - math.sqrt(2) / 2) < 1e-12 and abs(Cs(315) - math.sqrt(2) / 2) < 1e-12 and 360 - 45 == 315 == 7 * 45
assert all(S(g) > 0.5 for g in range(31, 150)) and S(29) < 0.5 and S(151) < 0.5
assert 9 - 8 == 1 and F(3 + 1, 4) == 1 and F(3 - 1, 4) == F(1, 2) and all(abs(2 * S(g) ** 2 - 3 * S(g) + 1) < 1e-12 for g in (90, 30, 150))
assert abs(Cs(60) - 0.5) < 1e-12 and abs(Cs(300) - 0.5) < 1e-12 and 360 - 60 == 300 == 5 * 60


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def cf(c, partes, x, y, size, a=1.0, align="left", est="g"):
    ws = [E.formula(None, s, 0, 0, size, est, a=0) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    if c is not None and a > 0:
        for (s, cor), wi in zip(partes, ws):
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += wi
    return sum(ws)


def cf_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: cf(c, partes, x, y, size, a, align))


def resp(c, t, t0, partes, cx, cy, size=64, alto=1.75, cor=None):
    if isinstance(partes, str):
        partes = [(partes, BR)]

    def f(a):
        w = cf(None, partes, 0, 0, size) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        cf(c, partes, cx, cy + size * 0.36, size, a, "center")
    E.foco(c, t, t0, 0.5, f)


def lista(c, t, itens, x, y0, dy=150, size=60):
    for i, (t0, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - size * 0.36, 40, a=a),
                                                   centro(c, str(i + 1), x + 40, y - size * 0.36 + 18, 50, "g", BR, a)))
        E.frase(c, t, t0 + 0.1, partes, x + 110, y, "left", 0.1)


# ---------------- o ciclo (como na MAT-TRI-009) ----------------
def pt(cx, cy, r, ang):
    return cx + r * Cs(ang), cy - r * S(ang)


def ciclo(c, t, t0, cx, cy, r, escuro=False):
    if t < t0:
        return
    tinta = BR if escuro else TINTA
    q = ep(t, t0, 0.6)
    M.arrow(c, cx - r - 70, cy, cx + r + 90, cy, tinta, q, 4, 20, q)
    M.arrow(c, cx, cy + r + 70, cx, cy - r - 90, tinta, q, 4, 20, q)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -360 * ease_io(prog(t, t0 + 0.2, 0.9)), False, M.paint(tinta, 1.0, stroke=5))
    sec = CLARO if escuro else TINTA2
    E.foco(c, t, t0 + 0.6, 0.4, lambda a: (E.escreve(c, "cos", cx + r + 60, cy + 56, 44, "i", sec, a),
                                           E.escreve(c, "sen", cx + 22, cy - r - 66, 44, "i", sec, a)))


def ponto(c, t, t0, cx, cy, r, ang, rot=None, cor=None, escuro=False, fora=78, size=50, arco=False):
    k = ease_back(prog(t, t0, 0.4))
    if k <= 0:
        return
    cor = cor or (E.COR if not escuro else CLARO)
    if arco:
        c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -ang * ease_io(prog(t, t0, 0.7)), False, M.paint(cor, 0.85, stroke=8, cap_round=True))
    X, Y = pt(cx, cy, r, ang)
    c.drawCircle(X, Y, 16 * k, M.paint(cor))
    c.drawCircle(X, Y, 16 * k, M.paint(BR if not escuro else "#07070F", 1.0, stroke=3))
    if rot:
        Xr, Yr = pt(cx, cy, r + fora, ang)
        E.foco(c, t, t0 + 0.1, 0.4, lambda a: E.formula(c, rot, Xr, Yr + size * 0.36, size, "g", cor, a, "center"))


def linha_h(c, t, t0, cx, cy, r, v, cor=OPO, rot=None, a=1.0):
    """linha horizontal na altura v (seno = v), de borda a borda do ciclo"""
    q = ep(t, t0, 0.6) * a
    if q <= 0:
        return
    y = cy - r * v
    M.line(c, cx - r - 60, y, lerp(cx - r - 60, cx + r + 60, ease_io(prog(t, t0, 0.6))), y, cor, q, 5, dash=[20, 12])
    if rot:
        E.formula(c, rot, cx - r - 80, y + 18, 48, "g", cor, q, "right")


def linha_v(c, t, t0, cx, cy, r, v, cor=ADJ, rot=None, a=1.0):
    """linha vertical na horizontal v (cosseno = v)"""
    q = ep(t, t0, 0.6) * a
    if q <= 0:
        return
    x = cx + r * v
    M.line(c, x, cy + r + 60, x, lerp(cy + r + 60, cy - r - 60, ease_io(prog(t, t0, 0.6))), cor, q, 5, dash=[20, 12])
    if rot:
        E.formula(c, rot, x, cy + r + 110, 48, "g", cor, q, "center")


def arco_sol(c, t, t0, cx, cy, r, de, ate, cor=CERTO, a=1.0, larg=16):
    """o arco-solução, de `de` até `ate` graus, grosso por cima do ciclo"""
    q = ep(t, t0, 0.8) * a
    if q <= 0:
        return
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -de, -(ate - de) * ease_io(prog(t, t0, 0.8)), False, M.paint(cor, q, stroke=larg))


def aberta(c, cx, cy, r, ang, cor, a=1.0, cheia=False):
    X, Y = pt(cx, cy, r, ang)
    c.drawCircle(X, Y, 17, M.paint(cor if cheia else BR, a))
    c.drawCircle(X, Y, 17, M.paint(cor, a, stroke=6))


# ---------------- gancho ----------------
GX, GY, GR = 1400, 560, 290


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        cf_em(c, t, a1, [("sen x = f{1}{2}", OPO)], XE, 360, 130)
        E.foco(c, t, b1, 0.5, lambda a: E.formula(c, "x = 30°", XE, 580, 110, "g", TINTA, a))
        E.foco(c, t, b1 + 0.8, 0.5, lambda a: E.escreve(c, "e só?", XE + 470, 580, 80, "i", ERRADO, a))
        E.frase(c, t, d1, ps("esqueceu o outro?", "i", 62) + [("metade da questão", "g", 66, ERRADO)], XE, 800, "left", 0.1)
        ciclo(c, t, a1 + 0.3, GX, GY, GR)
        linha_h(c, t, b1, GX, GY, GR, 0.5)
        ponto(c, t, b1 + 0.4, GX, GY, GR, 30, "30°")
        ponto(c, t, c1, GX, GY, GR, 150, "?", cor=ERRADO)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 260, passo=0.14)
        E.frase(c, t, ta + 1.2, [("equações", "g", 120, COR)] + ps("na volta inteira", "i", 84), XE, 440, "left", 0.12)
        E.frase(c, t, tb, [("inequações", "g", 110, COR)] + ps("no ciclo", "i", 84), XE, 620, "left", 0.12)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 545, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 630, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + E.larg("3", "g", 340) + 30, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "radianos:", "π = 180°"), ("s03.c", "o parceiro no 2º quadrante:", "180° − ângulo"),
             ("s03.d", "intervalos:", "]a, b[  aberto   [a, b]  fechado"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, l2=l2, y=y: E.formula(c, l2, x + 44, y + 166, 60, "g", COR, a))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 900, 1000, "left", 0.12)


# ---------------- a equação ----------------
CX, CY, CR = 600, 580, 310


def b_equacao(c, t, C, b):
    a4, b4, c4 = (C[f"s04.{k}"] for k in "abc")
    a5, b5, c5 = (C[f"s05.{k}"] for k in "abc")
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    X = 1420
    seno = t < b6 - 0.1
    ciclo(c, t, C["s04"] - 0.3, CX, CY, CR)

    def lado_seno():
        linha_h(c, t, b4, CX, CY, CR, 0.5, rot="f{1}{2}")
        ponto(c, t, c4, CX, CY, CR, 30, "f{π}{6}" if t >= a5 + 1 else None)
        ponto(c, t, c4 + 0.3, CX, CY, CR, 150, "f{5π}{6}" if t >= c5 else None)
        if t >= b5:  # o espelho no eixo vertical
            q = ep(t, b5, 0.5)
            M.line(c, CX, CY - CR - 40, CX, CY + CR + 40, COR, q, 6, dash=[22, 12])
        E.frase(c, t, a4, ps("onde a", "i", 60) + [("altura", "g", 66, OPO)] + ps("é", "i", 60) + [("um meio?", "g", 66, OPO)], X, 220, "center", 0.1)
        E.frase(c, t, c4, [("2 pontos", "g", 70, COR)], X, 340, "center", 0.1)
        cf_em(c, t, a5, [("30° = ", TINTA), ("f{π}{6}", COR)], X, 490, 80, "center")
        cf_em(c, t, b5, [("180° − 30° = 150°", TINTA2)], X, 630, 66, "center")
        cf_em(c, t, c5, [("150° = 5 · 30° → ", TINTA2), ("f{5π}{6}", COR)], X, 760, 66, "center")
        resp(c, t, a6, [("S = {f{π}{6}, f{5π}{6}}", BR)], X, 920, 64, 2.3, cor=OPO)
    E.saida(c, t, b6 - 0.1, lado_seno)
    if seno:
        return
    linha_v(c, t, b6, CX, CY, CR, math.sqrt(2) / 2, rot="f{r{2}}{2}")
    ponto(c, t, c6 + 0.3, CX, CY, CR, 45, "f{π}{4}" if t >= e6 else "45°", cor=ADJ)
    ponto(c, t, c6 + 0.6, CX, CY, CR, 315, "f{7π}{4}" if t >= e6 else "315°", cor=ADJ)
    E.frase(c, t, b6, ps("com cosseno, a linha é", "i", 56) + [("vertical", "g", 64, ADJ)], X, 260, "center", 0.1)
    cf_em(c, t, c6, [("cos x = f{r{2}}{2}", ADJ)], X, 430, 84, "center")
    cf_em(c, t, d6, [("45° e 315°", TINTA)], X, 600, 76, "center")
    cf_em(c, t, e6, [("315° = 7 · 45° → ", TINTA2), ("f{7π}{4}", ADJ)], X, 740, 64, "center")
    resp(c, t, e6 + 1.2, [("S = {f{π}{4}, f{7π}{4}}", BR)], X, 900, 64, 2.3, cor=ADJ)


# ---------------- a inequação ----------------
def b_inequacao(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    a8, b8, c8 = (C[f"s08.{k}"] for k in "abc")
    X = 1450
    CX, CY, CR = 500, 600, 300
    ciclo(c, t, C["s07"] - 0.3, CX, CY, CR)
    linha_h(c, t, C["s07"], CX, CY, CR, 0.5, rot="f{1}{2}")
    if t >= c7:  # a região acima da linha
        q = ep(t, c7, 0.5)
        y = CY - CR * 0.5
        c.save(); c.clipRect(skia.Rect.MakeLTRB(CX - CR - 10, CY - CR - 10, CX + CR + 10, y))
        c.drawCircle(CX, CY, CR, M.paint(CERTO, 0.12 * q)); c.restore()
    arco_sol(c, t, d7, CX, CY, CR, 30, 150)
    fecha = t >= c8
    for ang, rot in ((30, "f{π}{6}"), (150, "f{5π}{6}")):
        if t >= C["s07"] + 0.4:
            aberta(c, CX, CY, CR, ang, CERTO if t >= e7 else E.COR, ep(t, C["s07"] + 0.4, 0.4), cheia=fecha)
            Xr, Yr = pt(CX, CY, CR + 80, ang)
            E.formula(c, rot, Xr, Yr + 18, 50, "g", COR, ep(t, C["s07"] + 0.6, 0.4), "center")
    cf_em(c, t, a7, [("sen x > f{1}{2}", OPO)], X, 230, 96, "center")
    E.frase(c, t, b7, ps("onde a altura", "i", 58) + [("passa de um meio?", "g", 62, OPO)], X, 370, "center", 0.1)
    E.frase(c, t, c7, [("acima da linha", "g", 66, CERTO)], X, 480, "center", 0.1)
    E.frase(c, t, e7, ps("nas pontas, o seno é", "i", 50) + [("igual:", "g", 54)] + ps("ficam de fora", "i", 50), X, 590, "center", 0.08)
    resp(c, t, a8, [("] f{π}{6} , f{5π}{6} [", BR)], X, 760, 76, 2.2, cor=CERTO)
    cf_em(c, t, b8, [("sen x ≥ f{1}{2}", OPO)], X - 160, 940, 64, "center")
    cf_em(c, t, c8, [("→  [ f{π}{6} , f{5π}{6} ]", CERTO)], X + 160, 940, 64, "center")


# ---------------- segundo grau disfarçado ----------------
def b_segundo(c, t, C, b):
    a9, b9, c9 = (C[f"s09.{k}"] for k in "abc")
    a0, b0, c0, d0, e0, f0 = (C[f"s10.{k}"] for k in "abcdef")
    cf_em(c, t, a9, [("2 ", TINTA), ("sen^2 x", OPO), (" − 3 ", TINTA), ("sen x", OPO), (" + 1 = 0", TINTA)], W / 2, 190, 90, "center")
    E.foco(c, t, b9, 0.5, lambda a: E.pilula(c, "sen x = y", W / 2, 300, 56, "g", fundo=OPO, a=a))
    cf_em(c, t, c9, [("2y^2 − 3y + 1 = 0", TINTA)], XE, 460, 84)
    cf_em(c, t, a0, [("Δ = 9 − 8 = 1", TINTA2)], XE, 590, 72)
    cf_em(c, t, b0, [("y = f{3 ± 1}{4}", TINTA)], XE, 740, 80)
    cf_em(c, t, c0, [("y = 1  ou  y = f{1}{2}", COR)], XE, 900, 76)
    cx, cy, r = 1400, 640, 250
    ciclo(c, t, a0, cx, cy, r)
    linha_h(c, t, d0, cx, cy, r, 1.0, rot="1")
    ponto(c, t, d0 + 0.3, cx, cy, r, 90)
    E.foco(c, t, d0 + 0.4, 0.4, lambda a: E.formula(c, "f{π}{2}", cx + 90, cy - r - 30, 50, "g", COR, a, "center"))
    linha_h(c, t, e0, cx, cy, r, 0.5, rot="f{1}{2}")
    ponto(c, t, e0 + 0.3, cx, cy, r, 30, "f{π}{6}")
    ponto(c, t, e0 + 0.5, cx, cy, r, 150, "f{5π}{6}")
    E.foco(c, t, f0, 0.5, lambda a: E.pilula(c, "3 soluções", cx, cy + r + 150, 54, "g", fundo=CERTO, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    X = 1400
    ciclo(c, t, C["s11"] - 0.3, CX, CY, CR)
    linha_h(c, t, C["s11"], CX, CY, CR, 0.5)
    ponto(c, t, b1, CX, CY, CR, 30, "f{π}{6}")
    ponto(c, t, c1, CX, CY, CR, 150, "f{5π}{6}", cor=ERRADO)
    if t >= c1:
        q = ep(t, c1 + 0.2, 0.5)
        X2, Y2 = pt(CX, CY, CR, 150)
        c.drawCircle(X2, Y2, 44, M.paint(ERRADO, q, stroke=6))
    E.frase(c, t, a1, ps("o erro:", "i", 60) + [("parar no primeiro", "g", 66, ERRADO)], X, 240, "center", 0.1)
    cf_em(c, t, b1, [("tabela: só f{π}{6}", TINTA2)], X, 400, 72, "center")
    E.frase(c, t, c1, ps("a linha corta o ciclo em", "i", 56) + [("2 pontos", "g", 62, COR)], X, 560, "center", 0.1)
    E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "sempre procure o parceiro", X, 740, 56, "g", fundo=ERRADO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    a3, b3, c3 = (C[f"s13.{k}"] for k in "abc")
    cx, cy, r = 520, 600, 260

    def doze():
        E.frase(c, t, C["s12"] + 0.1, ps("agora o atalho", "i", 62, CLARO), W / 2, 160, "center", 0.1)
        ciclo(c, t, C["s12"], cx, cy, r, escuro=True)
        cf_em(c, t, a2, [("seno: ", CLARO), ("x", BR), (" e ", CLARO), ("π − x", OPO_ESC)], 1360, 340, 90, "center")
        cf_em(c, t, b2, [("cosseno: ", CLARO), ("x", BR), (" e ", CLARO), ("2π − x", ADJ_ESC)], 1360, 520, 90, "center")
        if t >= c2:
            q = ep(t, c2, 0.5)
            M.line(c, cx, cy - r - 40, cx, cy + r + 40, OPO_ESC, q, 7, dash=[22, 12])
            for ang in (30, 150):
                X, Y = pt(cx, cy, r, ang)
                c.drawCircle(X, Y, 14, M.paint(OPO_ESC, q))
            E.frase(c, t, c2, ps("espelho no eixo", "i", 56, CLARO) + [("vertical", "g", 60, OPO_ESC)], 1360, 700, "center", 0.1)
        if t >= d2:
            q = ep(t, d2, 0.5)
            M.line(c, cx - r - 40, cy, cx + r + 40, cy, ADJ_ESC, q, 7, dash=[22, 12])
            for ang in (60, 300):
                X, Y = pt(cx, cy, r, ang)
                c.drawCircle(X, Y, 14, M.paint(ADJ_ESC, q))
            E.frase(c, t, d2, ps("espelho no eixo", "i", 56, CLARO) + [("horizontal", "g", 60, ADJ_ESC)], 1360, 800, "center", 0.1)
    E.saida(c, t, C["s13"] - 0.1, doze)
    if t < C["s13"] - 0.1:
        return
    ciclo(c, t, C["s13"], cx, cy, r, escuro=True)
    E.frase(c, t, a3, ps("não vale com", "i", 62, CLARO) + [("1 ou −1", "g", 70, BR)], 1360, 340, "center", 0.1)
    linha_h(c, t, a3 + 0.4, cx, cy, r, 1.0, cor=OPO_ESC, rot="1")
    E.frase(c, t, b3, ps("a linha só encosta:", "i", 58, CLARO) + [("1 ponto", "g", 64, BR)], 1360, 500, "center", 0.1)
    ponto(c, t, c3, cx, cy, r, 90, escuro=True)
    E.foco(c, t, c3 + 0.1, 0.4, lambda a: E.formula(c, "f{π}{2}", cx + 90, cy - r - 30, 50, "g", CLARO, a, "center"))
    cf_em(c, t, c3, [("sen x = 1  →  só f{π}{2}", BR)], 1360, 680, 76, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a4, b4 = C["s14.a"], C["s14.b"]
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 170)
    cf_em(c, t, a4, [("2 ", TINTA), ("cos x", ADJ), (" − 1 = 0", TINTA)], XE, 460, 120)
    cf_em(c, t, b4, [("0 ≤ x ≤ 2π", TINTA2)], XE, 680, 90)
    E.relogio(c, t, C["s15.a"], 1500, 440, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a6, b6, c6 = (C[f"s16.{k}"] for k in "abc")
    a7, b7, c7 = (C[f"s17.{k}"] for k in "abc")
    X = 1420
    ciclo(c, t, C["s16"] - 0.3, CX, CY, CR)
    linha_v(c, t, b6, CX, CY, CR, 0.5)
    ponto(c, t, c6, CX, CY, CR, 60, "f{π}{3}", cor=ADJ)
    ponto(c, t, b7, CX, CY, CR, 300, "f{5π}{3}", cor=ADJ)
    E.frase(c, t, C["s16"] + 0.1, ps("isole o cosseno", "i", 60, COR), X, 190, "center", 0.1)
    cf_em(c, t, a6, [("2 ", TINTA), ("cos x", ADJ), (" = 1", TINTA)], X, 320, 80, "center")
    cf_em(c, t, b6, [("cos x = f{1}{2}", ADJ)], X, 460, 80, "center")
    cf_em(c, t, c6, [("60° = ", TINTA), ("f{π}{3}", ADJ)], X, 600, 76, "center")
    cf_em(c, t, a7, [("360° − 60° = 300°", TINTA2)], X, 720, 64, "center")
    cf_em(c, t, b7, [("300° = 5 · 60° → ", TINTA2), ("f{5π}{3}", ADJ)], X, 830, 64, "center")
    resp(c, t, c7, [("S = {f{π}{3}, f{5π}{3}}", BR)], X, 970, 64, 2.3, cor=ADJ)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"] + 0.1, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s18.a"], [("trace a linha", "g", 68, COR)] + ps("no ciclo", "i", 64)),
                     (C["s18.b"], ps("o ângulo da tabela e o", "i", 64) + [("parceiro", "g", 68, COR)]),
                     (C["s18.c"], ps("inequação:", "i", 64) + [("o arco acima ou abaixo", "g", 68, COR)])], 220, 400, 190, 64)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"] - 0.1:
        return
    a9, b9, c9, d9, e9 = (C[f"s19.{k}"] for k in "abcde")
    E.frase(c, t, C["s19"], ps("na próxima aula", "i", 72), XE, 210, "left", 0.1)
    E.frase(c, t, a9, [("praticando", "g", 110, COR)] + ps("a trilha", "i", 84), XE, 380, "left", 0.1)
    E.frase(c, t, b9, ps("leis dos", "i", 64) + [("senos e cossenos", "g", 68)], XE, 540, "left", 0.1)
    E.frase(c, t, c9, [("identidades", "g", 68)] + ps("e", "i", 64) + [("equações", "g", 68)], XE, 670, "left", 0.1)
    E.foco(c, t, d9, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 400, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d9 + 0.3, 0.8))
    E.cursor(c, lerp(1850, 1650, p), lerp(640, 425, p), ep(t, d9 + 0.2, 0.4))
    E.frase(c, t, e9, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, equacao=b_equacao, inequacao=b_inequacao, segundo=b_segundo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
