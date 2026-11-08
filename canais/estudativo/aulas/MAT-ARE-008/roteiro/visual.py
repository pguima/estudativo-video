"""Visual — Estudativo · MAT-ARE-008: área do círculo, da coroa e do setor (A = πr², fora menos dentro, fração da volta).
Linguagem da trilha (MAT-ARE-001) e do círculo (MAT-POL-004/005): circunferência em tinta, região da área pintada clara na cor
da matéria; o setor é a cunha na cor da matéria com os dois raios em tinta; o arco da vez é traço grosso em COR. A pizza tem a
massa em âmbar claro (como na MAT-POL-005). Regra de três: tabela de duas colunas e a cruz (diagonal 1 em COR, 2 em TINTA2).
Medidas na grotesca; resposta na esfera; vermelho é erro, verde é certo; palco escuro só no atalho.
Peça central desta aula: fatias() corta o círculo em n fatias que viajam e se encaixam alternadas numa faixa quase retangular,
altura r e base πr (as fatias de cima, com o arco em cima, em COR forte; as de baixo em COR clara).
Peças locais: pt(), cunha(), arco_cor(), pizza(), tabela() (as da MAT-POL-005), fatias(), coroa(), cota_v(), cota_h().
Todo instante vem de C[...] (marcadores do roteiro); entre() reparte o tempo entre dois marcadores."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Áreas e Perímetros")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ARE-008_area_do_circulo_coroa_e_setor.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("formula", "coroa", "setor", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
MASSA = "#F3D9A4"
GRAMA = "#CFE8C4"
assert 20 ** 2 == 400 and 10 ** 2 == 100 and 2 * 100 == 200 and 400 == 2 * 200 and 400 * 3 == 1200 and 200 * 3 == 600
assert 5 ** 2 - 3 ** 2 == 16 and (5 - 3) ** 2 == 4 and 4 ** 2 == 16 and 16 * 90 == 1440 and 1440 // 360 == 4 and 16 // 4 == 4
assert 6 ** 2 == 36 and 360 // 120 == 3 and 36 // 3 == 12 and 12 * 3 == 36 and 120 * 36 == 4320 and 4320 // 360 == 12


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


def entre(C, k1, k2, f):
    return lerp(C[k1], C[k2], f)


def pt(O, r, g):
    return O[0] + r * math.cos(math.radians(g)), O[1] - r * math.sin(math.radians(g))


def arco_cor(c, O, r, g1, g2, cor=None, larg=16, a=1.0, p=1.0):
    if a <= 0 or p <= 0:
        return
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    c.drawArc(ret, -g1, -(g2 - g1) * p, False, M.paint(cor or E.COR, a, stroke=larg, cap_round=True))


def cunha(c, O, g1, g2, r, cor=None, a=1.0, alfa=0.25, borda=5):
    if a <= 0:
        return
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    path = skia.Path(); path.moveTo(*O); path.arcTo(ret, -g1, -(g2 - g1), False); path.close()
    c.drawPath(path, M.paint(cor or E.COR, alfa * a))
    if borda:
        p = M.paint(TINTA, a, stroke=borda); p.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(path, p)


def pizza(c, O, r, a=1.0, cortes=0.0, n=8, g0=0):
    """pizza vista de cima (como na MAT-POL-005): massa, borda e os n cortes"""
    if a <= 0:
        return
    c.drawCircle(*O, r, M.paint(MASSA, a))
    for dx, dy in ((0.35, 0.2), (-0.4, 0.3), (0.1, -0.45), (-0.2, -0.1), (0.5, -0.3), (-0.1, 0.55)):
        c.drawCircle(O[0] + dx * r, O[1] + dy * r, r * 0.09, M.paint("#C8553D", 0.75 * a))
    c.drawCircle(*O, r, M.paint(AMBAR, a, stroke=max(8, r * 0.06)))
    if cortes > 0:
        for k in range(n):
            M.line(c, *O, *pt(O, r, g0 + 360 * k / n), TINTA, a, 4, progress=cortes)


def tabela(c, t, linhas, tl, x, y, dy=130, size=84, cor_l=None, cruz=None, wcol=300, a=1.0, escuro=False):
    """regra de três (a da MAT-POL-005): linhas = [(esq, dir[, cor])]; tl = instante de cada linha; cruz = instante das diagonais"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA
    t0 = tl[0]
    if t >= t0:
        M.line(c, x, y - size * 0.95, x, y + dy * (len(linhas) - 1) + size * 0.45, TINTA2, ep(t, t0, 0.4) * a, 4)
    for i, ln in enumerate(linhas):
        esq, dir_ = ln[0], ln[1]
        cd = ln[2] if len(ln) > 2 else tinta
        yy = y + dy * i
        E.foco(c, t, tl[i], 0.4, lambda f, esq=esq, yy=yy: E.formula(c, esq, x - wcol / 2, yy, size, "g", cor_l or tinta, f * a, "center"))
        E.foco(c, t, tl[i] + 0.25, 0.4, lambda f, dir_=dir_, yy=yy, cd=cd: E.formula(c, dir_, x + wcol / 2, yy, size, "g", cd, f * a, "center"))
    if cruz is not None and t >= cruz and len(linhas) >= 2:
        y1, y2 = y - size * 0.35, y + dy - size * 0.35
        x1, x2 = x - wcol / 2, x + wcol / 2
        for k, (P, Q, cor) in enumerate((((x1 + 40, y1 + 30), (x2 - 40, y2 - 40), E.COR), ((x2 - 40, y1 + 30), (x1 + 40, y2 - 40), TINTA2))):
            q = ease_io(prog(t, cruz + 0.4 * k, 0.5))
            if q > 0:
                M.line(c, *P, *Q, cor, a, 7, progress=q)


def _fatia(c, A, beta, r, th, cor, alfa, a, borda=TINTA):
    ret = skia.Rect.MakeXYWH(A[0] - r, A[1] - r, 2 * r, 2 * r)
    path = skia.Path(); path.moveTo(*A); path.arcTo(ret, -(beta - th / 2), -th, False); path.close()
    c.drawPath(path, M.paint(cor, alfa * a))
    p = M.paint(borda, a, stroke=2.5); p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, p)


def fatias(c, O, r, n, p, x0, y0, a=1.0, arcos=0.0):
    """o círculo cortado em n fatias; com p de 0 a 1 elas viajam e se encaixam numa faixa: as de baixo com a ponta para cima,
    as de cima com a ponta para baixo. Base = metade da volta = πr; altura = r. arcos acende os arcos de cima (COR)"""
    if a <= 0:
        return
    th = 360 / n
    s = 2 * math.pi * r / n
    betas = [(k + 0.5) * th for k in range(n)]
    cima = sorted([k for k in range(n) if betas[k] < 180], key=lambda k: -betas[k])
    baixo = sorted([k for k in range(n) if betas[k] > 180], key=lambda k: betas[k])
    for j in range(n):
        up = j % 2 == 0  # ponta para cima: fatia de baixo
        k = baixo[j // 2] if up else cima[j // 2]
        alvo = (x0 + s / 2 + j * s / 2, y0 if up else y0 + r)
        b_alvo = 270 if up else 90
        q = ease_io(M.clamp(p * 1.6 - 0.6 * j / n))
        d = ((b_alvo - betas[k] + 180) % 360) - 180
        A = (lerp(O[0], alvo[0], q), lerp(O[1], alvo[1], q))
        _fatia(c, A, betas[k] + d * q, r, th, E.COR, 0.18 if up else 0.42, a)
        if arcos > 0 and not up:
            ret = skia.Rect.MakeXYWH(A[0] - r, A[1] - r, 2 * r, 2 * r)
            c.drawArc(ret, -(90 - th / 2), -th, False, M.paint(E.COR, a * arcos, stroke=10))


def cota_v(c, x, y0, y1, s, cor=None, a=1.0, lado=-1, size=64):
    if a <= 0:
        return
    M.line(c, x, y0, x, y1, cor or COR, a, 5)
    for y in (y0, y1):
        M.line(c, x - 14, y, x + 14, y, cor or COR, a, 5)
    E.formula(c, s, x + lado * 26, (y0 + y1) / 2 + size * 0.36, size, "g", cor or COR, a, "right" if lado < 0 else "left")


def cota_h(c, x0, x1, y, s, cor=None, a=1.0, size=64, acima=True):
    if a <= 0:
        return
    M.line(c, x0, y, x1, y, cor or COR, a, 5)
    for x in (x0, x1):
        M.line(c, x, y - 14, x, y + 14, cor or COR, a, 5)
    E.formula(c, s, (x0 + x1) / 2, y - 28 if acima else y + 28 + size * 0.75, size, "g", cor or COR, a, "center")


def coroa(c, t, t0, O, R, r, a=1.0, cor=None, alfa=0.35, d=0.7):
    """anel entre duas circunferências de mesmo centro, pintado"""
    if t < t0 or a <= 0:
        return
    q = ep(t, t0 + d * 0.6, 0.5)
    path = skia.Path(); path.addCircle(*O, R); path.addCircle(*O, r)
    path.setFillType(skia.PathFillType.kEvenOdd)
    c.drawPath(path, M.paint(cor or E.COR, alfa * q * a))
    p = ease_io(prog(t, t0, d))
    for rr in (R, r):
        c.drawArc(skia.Rect.MakeXYWH(O[0] - rr, O[1] - rr, 2 * rr, 2 * rr), 0, -360 * p, False, M.paint(TINTA, a, stroke=6, cap_round=True))
    k = ease_back(prog(t, t0 + d * 0.5, 0.35))
    if k > 0:
        c.drawCircle(*O, 9 * k, M.paint(TINTA, a))


def raio_rot(c, t, t0, O, r, g, s, cor=None, size=56, lado=1, f=0.5):
    """raio de O até a borda no ângulo g, com o rótulo ao lado"""
    if t < t0:
        return
    P = pt(O, r, g)
    M.line(c, *O, *P, cor or E.COR, 1.0, 6, progress=ease_io(prog(t, t0, 0.5)))
    k = ease_back(prog(t, t0 + 0.4, 0.3))
    if k > 0:
        c.drawCircle(*P, 9 * k, M.paint(cor or E.COR))
    nx, ny = -math.sin(math.radians(g)) * lado, -math.cos(math.radians(g)) * lado
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: E._cola(c, s, lerp(O[0], P[0], f), lerp(O[1], P[1], f), nx, ny, 14, size, "b", cor or COR, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    OG, RG = (470, 600), 300
    OP = ((1130, 600), (1560, 600))

    def um():
        E.foco(c, t, a1, 0.6, lambda a: pizza(c, OG, RG * ease_back(prog(t, a1, 0.6)), a))
        if t >= b1:
            M.line(c, *OG, *pt(OG, RG, 0), TINTA, 1.0, 7, progress=ease_io(prog(t, b1, 0.5)))
            E.foco(c, t, b1 + 0.4, 0.4, lambda a: E.pilula(c, "20 cm", OG[0] + RG / 2, OG[1] - 50, 50, "g", a=a))
        for i, O in enumerate(OP):
            ti = c1 + 0.3 * i
            E.foco(c, t, ti, 0.6, lambda a, O=O, ti=ti: pizza(c, O, 150 * ease_back(prog(t, ti, 0.6)), a))
            if t >= c1 + 0.8:
                M.line(c, *O, *pt(O, 150, 0), TINTA, 1.0, 6, progress=ease_io(prog(t, c1 + 0.8, 0.5)))
                E.foco(c, t, c1 + 1.2, 0.4, lambda a, O=O: E.pilula(c, "10 cm", O[0] + 75, O[1] - 44, 40, "g", a=a))
        E.frase(c, t, entre(C, "s01.c", "s01.d", 0.55), ps("parece a", "i", 72) + [("mesma coisa", "g", 76)], W / 2, 200, "center", 0.12)
        if t >= d1:
            E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "a grande tem o dobro!", OG[0], 990, 64, "g", fundo=CERTO, a=a))
            E.foco(c, t, d1 + 0.3, 0.5, lambda a: centro(c, "juntas", 1345, 870, 64, "i", TINTA2, a))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1520, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 300, passo=0.14)
        E.frase(c, t, entre(C, "s02.a", "s02.b", 0.3), [("área", "g", 110, COR)] + ps("do", "i", 84), XE, 450, passo=0.14)
        E.frase(c, t, entre(C, "s02.a", "s02.b", 0.4), [("círculo,", "g", 96, COR)], XE, 580, passo=0.14)
        E.frase(c, t, entre(C, "s02.a", "s02.b", 0.6), ps("do", "i", 84) + [("anel", "g", 96, COR)] + ps("e da", "i", 84) + [("fatia", "g", 96, COR)],
                XE, 710, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1520, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1520, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "a volta da circunferência:", "C = 2πr"), ("s03.c", "o arco é a fração da volta", "que o ângulo é de 360°"),
             ("s03.d", "área do retângulo:", "base × altura"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 84)
        E.formula_em(c, t, C[k] + 0.4, l2, x + 44, y + 165, 58, "g", COR)
    alvo = [(x + w - 30, 170 + i * 240 + 170) for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, alvo[0][0], lerp(lerp(alvo[0][1], alvo[1][1], q1), alvo[2][1], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 960, "left", 0.12)


# ---------------- de onde vem a fórmula ----------------
FO, FR = (500, 560), 260      # o círculo
FX, FY = 170, 420             # a faixa: canto de cima à esquerda


def b_formula(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
    a7, b7, c7, d7, e7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"]
    X = 1440
    mais = entre(C, "s05.a", "s05.b", 0.45)  # "quanto mais fatias, mais reta ela fica"

    def figura():
        # o círculo pintado, depois cortado
        if t < c4 + 0.1:
            E.circulo(c, t, a4 - 0.6, *FO, FR, o=None, preenche=0.3, d=0.7)
        if b4 <= t < c4 + 0.1:
            k8 = ease_io(prog(t, b4, 0.6))
            k16 = ease_io(prog(t, entre(C, "s04.b", "s04.c", 0.55), 0.6))
            for k in range(16):
                if k % 2 == 0 or k16 > 0:
                    M.line(c, *FO, *pt(FO, FR, 360 * k / 16), TINTA, 1.0 if k % 2 == 0 else k16, 3, progress=k8 if k % 2 == 0 else k16)
        if t >= c4:
            p = prog(t, c4 + 0.1, 2.2)
            k32 = ep(t, mais, 0.8)
            fatias(c, FO, FR, 16, p, FX, FY, 1 - k32, ep(t, c5, 0.6))
            fatias(c, FO, FR, 32, 1.0, FX, FY, k32, ep(t, c5, 0.6))
        if t >= b5:
            cota_v(c, FX - 40, FY, FY + FR, "r", COR, ep(t, b5, 0.4))
        if t >= d5:
            cota_h(c, FX + 2 * math.pi * FR / 64, FX + 2 * math.pi * FR / 64 + math.pi * FR, FY - 40, "πr", COR, ep(t, d5, 0.4))

    E.saida(c, t, C["s07"] - 0.1, figura)

    def quatro_cinco():
        E.frase(c, t, a4, ps("área =", "i", 66) + [("a região de dentro", "g", 66, COR)], X, 300, "center", 0.12)
        E.frase(c, t, b4, ps("corte em", "i", 66) + [("fatias finas", "g", 70, COR)], X, 460, "center", 0.12)
        E.frase(c, t, c4, ps("encaixe:", "i", 62) + [("ponta para cima,", "g", 58)], X, 620, "center", 0.12)
        E.frase(c, t, c4 + 1.2, [("ponta para baixo", "g", 58)], X, 710, "center", 0.12)
    E.saida(c, t, a5 - 0.1, quatro_cinco)

    def cinco_seis():
        E.frase(c, t, a5, ps("quase um", "i", 70) + [("retângulo", "g", 76, COR)], X, 220, "center", 0.12)
        E.frase(c, t, mais, ps("mais fatias,", "i", 58, TINTA2) + ps("mais reta", "i", 58, TINTA2), X, 310, "center", 0.12)
        E.frase(c, t, b5, ps("altura =", "i", 62) + [("raio", "g", 68, COR)], X, 440, "center", 0.12)
        E.frase(c, t, c5, ps("base =", "i", 62) + [("metade da volta", "g", 64, COR)], X, 560, "center", 0.12)
        fcen(c, t, d5, "f{2πr}{2} = πr", X, 720, 84, COR)
    E.saida(c, t, a6 - 0.1, cinco_seis)

    def seis():
        E.frase(c, t, C["s06"], ps("base × altura", "i", 70), X, 220, "center", 0.12)
        fcen(c, t, a6, "πr · r", X, 360, 96)
        E.foco(c, t, b6, 0.6, lambda a: E.formula(c, "A = πr^2", X, 560, 140, "g", COR, a, "center"))
        E.frase(c, t, c6, [("A", "g", 64, COR)] + ps("é a área", "i", 60), X, 720, "center", 0.12)
        E.frase(c, t, d6, [("r", "g", 64, COR)] + ps("é o raio", "i", 60), X, 820, "center", 0.12)
        E.frase(c, t, e6, [("π ≈ 3,14", "g", 64, COR)] + ps("o mesmo da volta", "i", 56), X, 920, "center", 0.12)
    if t >= a6 - 0.1:
        E.saida(c, t, C["s07"] - 0.1, seis)

    # as pizzas, de novo, com a conta
    if t >= C["s07"] - 0.1:
        OG, RG = (420, 600), 260
        OP = ((900, 460), (900, 790))
        E.foco(c, t, C["s07"], 0.5, lambda a: pizza(c, OG, RG, a))
        for i, O in enumerate(OP):
            E.foco(c, t, C["s07"] + 0.2 + 0.2 * i, 0.5, lambda a, O=O: pizza(c, O, 130, a))
        E.foco(c, t, a7 + 0.5, 0.4, lambda a: E.pilula(c, "400π", OG[0], OG[1], 76, "g", fundo=E.COR, a=a))
        for i, O in enumerate(OP):
            E.foco(c, t, b7 + 0.5 + 0.2 * i, 0.4, lambda a, O=O: E.pilula(c, "100π", O[0], O[1], 50, "g", fundo=TINTA, a=a))
        X7 = 1480
        fcen(c, t, C["s07"] + 0.3, "A = πr^2", X7, 200, 76, COR)
        fcen(c, t, a7, "20^2 = 400  →  400π", X7, 350, 72)
        fcen(c, t, b7, "10^2 = 100  →  100π", X7, 480, 72)
        fcen(c, t, c7, "juntas: 200π", X7, 610, 72, TINTA2)
        fcen(c, t, d7, "400π = 2 · 200π", X7, 750, 80, CERTO)
        E.foco(c, t, e7, 0.5, lambda a: E.pilula(c, "o raio entra ao quadrado", X7, 900, 54, "g", fundo=AMBAR, a=a))


# ---------------- coroa ----------------
CO, CR, Cr = (540, 570), 300, 180   # 60 px por unidade: raios 5 e 3


def b_coroa(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9, e9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]
    X = 1440
    coroa(c, t, a8, CO, CR, Cr)
    if t >= b8:  # o furo
        k = ep(t, b8, 0.5)
        c.drawCircle(*CO, Cr, M.paint("#FFFFFF", 0.5 * k))
        p = M.paint(TINTA2, k, stroke=4); p.setPathEffect(skia.DashPathEffect.Make([12, 10], 0))
        c.drawCircle(*CO, Cr - 8, p)
    # destaques do cálculo: o disco de fora, depois o furo
    k_fora = ep(t, b9, 0.4) * (1 - ep(t, c9, 0.4))
    if k_fora > 0:
        c.drawCircle(*CO, CR, M.paint(E.COR, 0.25 * k_fora))
    k_furo = ep(t, c9, 0.4) * (1 - ep(t, d9, 0.4))
    if k_furo > 0:
        c.drawCircle(*CO, Cr, M.paint(AMBAR, 0.45 * k_furo))
    raio_rot(c, t, a9, CO, CR, 35, "5", COR, 60, f=0.8)
    raio_rot(c, t, a9 + 0.5, CO, Cr, 200, "3", TINTA, 60, lado=-1)

    def oito():
        E.frase(c, t, a8, [("coroa:", "g", 76, COR)] + ps("o anel", "i", 72), X, 260, "center", 0.12)
        E.frase(c, t, a8 + 0.8, ps("mesmo centro", "i", 60, TINTA2), X, 360, "center", 0.12)
        E.frase(c, t, b8, ps("um disco com um", "i", 62) + [("furo", "g", 68)], X, 510, "center", 0.12)
        E.frase(c, t, c8, ps("área =", "i", 62) + [("fora − furo", "g", 72, COR)], X, 700, "center", 0.12)
    E.saida(c, t, C["s09"] - 0.1, oito)
    if t >= C["s09"] - 0.1:
        E.frase(c, t, a9, ps("raios", "i", 66) + [("5 e 3", "g", 72, COR)], X, 220, "center", 0.12)
        fcen(c, t, b9, "fora: π · 5^2 = 25π", X, 380, 74)
        fcen(c, t, c9, "furo: π · 3^2 = 9π", X, 510, 74, AMBAR)
        fcen(c, t, d9, "25π − 9π", X, 650, 76)
        bola_txt(c, t, d9 + 0.6, "16π", X, 800, 95, 70, CERTO)
        E.foco(c, t, e9, 0.5, lambda a: E.pilula(c, "π como letra: 25x − 9x = 16x", X, 960, 46, "g", fundo=TINTA, a=a))


# ---------------- setor ----------------
SO, SR = (520, 600), 300   # raio 4: 75 px por unidade


def b_setor(c, t, C, b):
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    a11, b11, c11, d11, e11, f11 = (C[f"s11.{k}"] for k in "abcdef")
    X = 1440

    def dez():
        E.circulo(c, t, C["s10"], *SO, SR, o=None, d=0.6)
        g = lerp(45, 90, ease_io(prog(t, b10, 0.8)))
        k = ep(t, a10, 0.5)
        cunha(c, SO, 0, g, SR, E.COR, k, 0.3, 5)
        if t >= a10 + 0.3:
            arco_cor(c, SO, SR, 0, g, E.COR, 14, 1.0, ease_io(prog(t, a10 + 0.3, 0.5)))
        E.foco(c, t, b10 + 0.6, 0.4, lambda a: centro(c, "2×", *(lambda P: (P[0], P[1] + 20))(pt(SO, 130, 45)), 56, "g", COR, a))
        E.frase(c, t, a10, [("setor:", "g", 76, COR)] + ps("uma fatia", "i", 72), X, 260, "center", 0.12)
        E.frase(c, t, a10 + 1.0, ps("entre dois raios e o arco", "i", 56, TINTA2), X, 360, "center", 0.1)
        E.frase(c, t, b10, ps("ângulo", "i", 62) + [("× 2", "g", 70, COR), ("→", "g", 62, TINTA2)] + ps("área", "i", 62) + [("× 2", "g", 70, COR)], X, 520, "center", 0.12)
        E.foco(c, t, c10, 0.5, lambda a: E.pilula(c, "diretamente proporcionais", X, 700, 54, "g", a=a))
    E.saida(c, t, C["s11"] - 0.1, dez)
    if t < C["s11"] - 0.1:
        return
    t0 = C["s11"]
    E.circulo(c, t, t0, *SO, SR, o=None, d=0.6)
    k = ep(t, a11, 0.5)
    cunha(c, SO, 0, 90, SR, E.COR, k, 0.3, 5)
    E.angulo(c, t, a11 + 0.3, SO, pt(SO, SR, 0), pt(SO, SR, 90), None, r=60, reto=True, preenche=0.0)
    E.foco(c, t, a11 + 0.4, 0.4, lambda a: centro(c, "90°", *(lambda P: (P[0], P[1] + 20))(pt(SO, 140, 45)), 52, "g", COR, a))
    raio_rot(c, t, a11 + 0.5, SO, SR, 180, "4", TINTA, 60, lado=-1)
    if t >= b11:
        c.drawCircle(*SO, SR, M.paint(E.COR, 0.1 * ep(t, b11, 0.4) * (1 - ep(t, c11, 0.5))))
    fcen(c, t, b11, "círculo: π · 4^2 = 16π", X, 220, 70)

    def tab(a=1.0):
        tabela(c, t, [("360°", "16π"), ("90°", "x", COR)], [c11, d11], X, 440, 130, 84, cruz=e11, a=a)
    tab()
    fcen(c, t, e11 + 0.6, "360x = 90 · 16π = 1.440π", X, 760, 64)
    bola_txt(c, t, f11, "x = 4π", X, 910, 100, 58, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    X = 1440
    O, R, r = (420, 560), 250, 150   # 50 px por unidade
    coroa(c, t, C["s12"], O, R, r)
    E.foco(c, t, C["s12"] + 0.5, 0.4, lambda a: (centro(c, "5", O[0] + R + 40, O[1] + 20, 56, "g", COR, a),
                                                  M.line(c, *O, O[0] - r, O[1], TINTA, a, 5),
                                                  centro(c, "3", O[0] - r / 2, O[1] - 18, 56, "g", TINTA, a)))
    # a largura do anel, 2
    if t >= a12:
        k = ep(t, a12, 0.4)
        M.line(c, O[0] + r, O[1], O[0] + R, O[1], ERRADO, k, 8)
        centro(c, "2", O[0] + (R + r) / 2, O[1] - 20, 56, "g", ERRADO, k)
    # o círculo de raio 2, ao lado, bem menor que o anel
    if t >= b12:
        Q = (O[0] + 120, 930)
        E.circulo(c, t, b12 + 0.3, Q[0] - 300, Q[1] - 20, 100, o=None, cor=ERRADO, preenche=0.35, d=0.6)
        E.foco(c, t, b12 + 0.6, 0.4, lambda a: E.escreve(c, "raio 2", Q[0] - 180, Q[1], 50, "b", ERRADO, a))

    def um():
        E.frase(c, t, a12, ps("erro:", "i", 66, ERRADO) + [("subtrair os raios", "g", 66)], X, 220, "center", 0.12)
        fcen(c, t, entre(C, "s12.a", "s12.b", 0.5), "5 − 3 = 2", X, 360, 80, ERRADO)
        fcen(c, t, b12, "π · 2^2 = 4π", X, 490, 80, ERRADO)
        if t >= b12 + 0.8:
            E.risco(c, X - 230, 510, X + 230, 440, t, b12 + 0.8, largura=10)
        E.frase(c, t, c12, ps("anel de largura 2", "i", 58) + [("≠", "g", 66, ERRADO)], X, 640, "center", 0.12)
        E.frase(c, t, c12 + 0.8, ps("círculo de raio 2", "i", 58), X, 720, "center", 0.12)
        fcen(c, t, d12, "25π − 9π = 16π", X, 880, 84, CERTO)
        E.foco(c, t, entre(C, "s12.d", "s12.end", 0.6), 0.4, lambda a: E.selo(c, X + 380, 855, 44 * ease_back(prog(t, entre(C, "s12.d", "s12.end", 0.6), 0.4)), True, a))
    um()


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    X = W / 2

    def um():
        E.frase(c, t, C["s13"] + 0.2, [("atalho", "g", 90, CLARO)] + ps("para o setor", "i", 76, BR), X, 170, "center", 0.12)
        E.frase(c, t, a13, ps("ângulo", "i", 72, CLARO) + [("→", "g", 72, CLARO), ("fração da volta", "g", 80, BR)], X, 320, "center", 0.12)
        O = (520, 640)
        if t >= b13:
            k = ep(t, b13, 0.5)
            cunha(c, O, 0, 90, 180, CLARO, k, 0.6, 0)
            c.drawCircle(*O, 180, M.paint(BR, k, stroke=6))
            M.line(c, *O, *pt(O, 180, 0), BR, k, 5); M.line(c, *O, *pt(O, 180, 90), BR, k, 5)
        fcen(c, t, b13, "90° = f{1}{4} da volta", 1180, 560, 80, BR)
        fcen(c, t, c13, "f{1}{4} · 16π = 4π", 1180, 760, 90, CLARO)
        E.foco(c, t, c13 + 1.2, 0.5, lambda a: E.pilula(c, "sem cruz", 1180, 920, 60, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s14"] - 0.1, um)
    if t >= C["s14"] - 0.1:
        E.frase(c, t, a14, ps("o setor é a", "i", 70, CLARO) + [("mesma fração", "g", 80, BR)], X, 280, "center", 0.12)
        E.frase(c, t, a14 + 1.2, ps("do círculo que o ângulo é da volta", "i", 64, CLARO), X, 390, "center", 0.1)
        E.foco(c, t, b14, 0.5, lambda a: E.pilula(c, "50°? não compensa", X, 600, 70, "g", fundo=ERRADO, a=a))
        E.frase(c, t, c14, ps("aí,", "i", 72, CLARO) + [("monte a tabela", "g", 84, BR)], X, 800, "center", 0.12)


# ---------------- questão ----------------
QO, QR = (560, 860), 470   # irrigador: raio 6 m, 120° (de 30° a 150°)


def jardim(c, t, t0, molha=None, cor_m=None):
    if t < t0:
        return
    q = ep(t, t0, 0.5)
    M.rrect(c, 110, 300, 900, 640, 30, GRAMA, q)
    for k in range(40):  # tufos
        x = 150 + (k * 137) % 820
        y = 340 + (k * 89) % 560
        M.line(c, x, y, x - 8, y - 18, "#7FB069", q * 0.7, 3)
        M.line(c, x, y, x + 8, y - 18, "#7FB069", q * 0.7, 3)
    if molha is not None:
        p = ease_io(prog(t, molha, 0.9))
        if p > 0:
            ret = skia.Rect.MakeXYWH(QO[0] - QR, QO[1] - QR, 2 * QR, 2 * QR)
            path = skia.Path(); path.moveTo(*QO); path.arcTo(ret, -30, -120 * p, False); path.close()
            c.drawPath(path, M.paint(cor_m or "#3A86FF", 0.35))
            pp = M.paint(TINTA, 1.0, stroke=5); pp.setStrokeJoin(skia.Paint.kRound_Join)
            c.drawPath(path, pp)
            # gotinhas
            for k in range(12):
                g = 30 + 120 * (k + 0.5) / 12
                if g - 30 <= 120 * p:
                    for f in (0.45, 0.7, 0.92):
                        c.drawCircle(*pt(QO, QR * f, g), 6, M.paint("#3A86FF", 0.7))
    # o irrigador
    k = ease_back(prog(t, t0 + 0.3, 0.4))
    if k > 0:
        c.drawCircle(*QO, 26 * k, M.paint(TINTA))
        c.drawCircle(*QO, 10 * k, M.paint("#3A86FF"))


def b_questao(c, t, C, b):
    a15, b15, c15, d15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    X = 1500
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), X, 160, "center", 0.12)
    jardim(c, t, C["s15"] + 0.2, a15)
    E.foco(c, t, a15 + 0.6, 0.4, lambda a: centro(c, "120°", QO[0], QO[1] - 110, 56, "g", TINTA, a))
    if t >= a15 + 0.5:
        E.angulo(c, t, a15 + 0.5, QO, pt(QO, 100, 30), pt(QO, 100, 150), None, r=70, preenche=0.0)
    if t >= b15:
        M.line(c, *QO, *pt(QO, QR, 30), TINTA, 1.0, 7, progress=ease_io(prog(t, b15, 0.5)))
        E.foco(c, t, b15 + 0.4, 0.4, lambda a: E.pilula(c, "6 m", *pt(QO, QR * 0.6, 30), 48, "g", fundo=TINTA, a=a))
    linhas = [(a15, ps("gira", "i", 60) + [("120°", "g", 66)]), (b15, ps("molha até", "i", 60) + [("6 m", "g", 66)]),
              (c15, ps("área molhada", "i", 60) + [("= ?", "g", 70, COR)]), (d15, ps("use", "i", 60) + [("π = 3", "g", 66)])]
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, 770 + i * 85, "center", 0.12)
    E.relogio(c, t, C["s16.a"], X, 370, 150)


def b_resposta(c, t, C, b):
    a17, b17, c17, d17, e17 = (C[f"s17.{k}"] for k in "abcde")
    a18, b18, c18, d18 = (C[f"s18.{k}"] for k in "abcd")
    X = 1480
    t0 = C["s17"] - 1.2
    jardim(c, t, t0, t0, "#3A86FF" if t < a17 else E.COR)
    centro(c, "120°", QO[0], QO[1] - 110, 56, "g", TINTA, 1.0)
    E.angulo(c, t, t0, QO, pt(QO, 100, 30), pt(QO, 100, 150), None, r=70, preenche=0.0)
    E.pilula(c, "6 m", *pt(QO, QR * 0.6, 30), 48, "g", fundo=TINTA)
    if t >= c17:  # um terço da volta: o círculo inteiro tracejado
        k = ep(t, c17, 0.5) * (1 - ep(t, C["s18"], 0.5))
        p = M.paint(TINTA2, k, stroke=4); p.setPathEffect(skia.DashPathEffect.Make([14, 12], 0))
        c.save(); c.clipRect(skia.Rect.MakeXYWH(110, 300, 900, 640)); c.drawCircle(*QO, QR, p); c.restore()

    def um():
        E.frase(c, t, a17, [("setor", "g", 70, COR)] + ps("de raio 6", "i", 64), X, 200, "center", 0.12)
        fcen(c, t, b17, "π · 6^2 = 36π", X, 340, 76)
        fcen(c, t, c17, "120° = f{1}{3} da volta", X, 500, 72, COR)
        fcen(c, t, d17, "f{1}{3} · 36π = 12π", X, 670, 76)
        fcen(c, t, e17, "12 · 3 = 36", X, 800, 72)
        bola_txt(c, t, e17 + 0.6, "36 m²", X, 945, 100, 56, CERTO)
    E.saida(c, t, C["s18"] - 0.1, um)
    if t >= C["s18"] - 0.1:
        E.frase(c, t, C["s18"], ps("pela", "i", 66) + [("tabela", "g", 72, COR)], X, 200, "center", 0.12)
        tabela(c, t, [("360°", "36π"), ("120°", "x", COR)], [a18, b18], X, 400, 130, 84, cruz=c18)
        fcen(c, t, c18 + 0.6, "360x = 120 · 36π = 4.320π", X, 700, 60)
        fcen(c, t, d18, "x = 12π", X - 50, 850, 90, CERTO)
        E.foco(c, t, d18 + 0.8, 0.4, lambda a: E.selo(c, X + 190, 820, 44 * ease_back(prog(t, d18 + 0.8, 0.4)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", "círculo:", "A = πr^2"), ("s19.b", "coroa:", "fora − dentro"), ("s19.c", "setor:", "a fração da volta"))
        for i, (k, it, g) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(it, "i", 80)], 400, y)
            E.formula_em(c, t, C[k] + 0.5, g, 400 + E.larg(it, "i", 80) + 30, y, 80, "g", COR)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    E.frase(c, t, C["s20"] + 0.1, ps("próxima aula:", "i", 72), XE, 220, passo=0.1)
    E.frase(c, t, C["s20"] + 0.8, [("juntar e recortar", "g", 100, COR)], XE, 350)
    # retângulo com meio círculo em cima
    if t >= a20:
        x, y, w, h = 260, 620, 360, 240
        E.retangulo(c, t, a20, x, y, w, h, preenche=0.15, d=0.6)
        q = ease_io(prog(t, a20 + 0.5, 0.6))
        if q > 0:
            ret = skia.Rect.MakeXYWH(x, y - w / 2, w, w)
            path = skia.Path(); path.addArc(ret, 180, 180 * q)
            c.drawPath(path, M.paint(TINTA, 1.0, stroke=6))
            path2 = skia.Path(); path2.moveTo(x + w / 2, y); path2.arcTo(ret, 180, 180, False); path2.close()
            c.drawPath(path2, M.paint(E.COR, 0.15 * q))
    # malha quadriculada com a região sombreada
    if t >= b20:
        gx, gy, s, n = 820, 540, 64, 5
        k = ep(t, b20, 0.5)
        tri = [(gx, gy + n * s), (gx + n * s, gy + n * s), (gx + n * s, gy + s)]
        path = skia.Path(); path.addPoly(tri, True)
        c.drawPath(path, M.paint(E.COR, 0.35 * ep(t, b20 + 0.4, 0.5)))
        for i in range(n + 1):
            M.line(c, gx + i * s, gy, gx + i * s, gy + n * s, TINTA2, k * 0.8, 2)
            M.line(c, gx, gy + i * s, gx + n * s, gy + i * s, TINTA2, k * 0.8, 2)
        pp = M.paint(TINTA, ep(t, b20 + 0.4, 0.5), stroke=5); pp.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(path, pp)
    E.foco(c, t, c20, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1570, 620, 76, estilo="g", a=a))
    p = ease_io(prog(t, c20 + 0.3, 0.8))
    E.cursor(c, lerp(1850, 1700, p), lerp(900, 645, p), ep(t, c20 + 0.2, 0.4))
    E.frase(c, t, d20, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, formula=b_formula, coroa=b_coroa, setor=b_setor, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
