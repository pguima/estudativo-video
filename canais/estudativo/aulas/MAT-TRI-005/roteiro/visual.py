"""Visual — Estudativo · MAT-TRI-005: dois ângulos de visão (morro visto a 30° e a 60°, 100 m entre os pontos: x = 50, h = 50√3 ≈ 85 m).
Linguagem da trigonometria (a mesma de MAT-TRI-004): lados em tinta; cada lado ganha a cor do seu nome a partir do ângulo da vez —
OPO (cateto oposto, âmbar), ADJ (cateto adjacente, turquesa), HIP (hipotenusa, índigo da matéria); ângulo da vez = arco com cunha;
ângulo reto = quadradinho; medidas na grotesca; sen, cos e tg abreviados; resposta na esfera ou na pílula; erro em vermelho, certo em
verde; atalho no palco escuro.
A figura não mente: o morro e o prédio têm x = d/2 e h = x√3 de verdade (6 px por metro no morro, 7,5 no prédio), e a encosta do
morro é mais íngreme que 60°, para nenhuma linha de visão atravessar a terra.
Peças locais: cena() (chão, morro ou prédio, pontos A e B, linhas de visão, ângulos, altura tracejada e os lados com nome),
morro(), predio(), cota() (medida com tracinhos sob o chão), resp(), lista(), grosso(), txt_lado().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-005_dois_angulos_de_visao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("desenho", "sistema", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
HIP, OPO, ADJ = E.COR, AMBAR, "#0E9AA7"     # cor fixa de cada lado da trigonometria
ADJ_ESC = "#3CC7D3"                         # o adjacente no palco escuro
TERRA = "#8C7A5B"
R3 = math.sqrt(3)
assert abs(50 * R3 / 50 - math.tan(math.radians(60))) < 1e-9 and abs(50 * R3 / 150 - math.tan(math.radians(30))) < 1e-9
assert 3 * 50 == 50 + 100 and 2 * 50 == 100 and round(50 * 1.7) == 85 and 50 * R3 > 85
assert round(100 * R3 / 3) == 58 and 100 * 1.7 / 3 > 56 and abs(100 * R3 / 2 - 50 * R3) < 1e-9 and 60 - 30 == 30
assert 3 * 40 == 40 + 80 and 2 * 40 == 80 and round(40 * 1.7) == 68 and abs(80 * R3 / 2 - 40 * R3) < 1e-9


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


def resp(c, t, t0, s, cx, cy, size=76, alto=1.75):
    """resposta comprida numa pílula com volume, na cor da matéria (alto ≈ 2.5 para fração)"""
    def f(a):
        w = E.formula(c, s, 0, 0, size, a=0) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, E.COR, a, shadow=True)
        E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")
    E.foco(c, t, t0, 0.5, f)


def pilula(c, t, t0, s, cx, cy, size=64):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, s, cx, cy, size, "g", a=a, cor=E.SOBRE))


def lista(c, t, itens, x, y0, dy=150, size=64):
    """linhas numeradas [(t0, partes)] com o número na esfera"""
    for i, (t0, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - size * 0.36, 40, a=a),
                                                   centro(c, str(i + 1), x + 40, y - size * 0.36 + 18, 50, "g", BR, a)))
        E.frase(c, t, t0 + 0.1, partes, x + 110, y, "left", 0.1)


def txt_lado(c, P, Q, s, G, size=54, cor=None, a=1.0, gap=20):
    if a <= 0 or not s:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
    if (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 < (mx - G[0]) ** 2 + (my - G[1]) ** 2:
        nx, ny = -nx, -ny
    E._cola(c, s, mx, my, nx, ny, gap, size, "b", cor or COR, a)


def grosso(c, P, Q, cor, a, larg=12, p=1.0, dash=None):
    if a > 0 and p > 0:
        M.line(c, *P, *Q, cor, a, larg, progress=p, dash=dash)


def pinta(c, pts, cor, a, alfa=0.14):
    if a > 0:
        path = skia.Path(); path.addPoly(pts, True)
        c.drawPath(path, M.paint(cor, alfa * a))


def cota(c, t, t0, P, Q, s, y, cor=TINTA, size=56, d=0.5):
    """medida entre P e Q, numa linha de cota em y (abaixo do chão)"""
    q = ep(t, t0, d)
    if q <= 0:
        return
    M.line(c, P[0], y, lerp(P[0], Q[0], ease_io(q)), y, cor, 1.0, 4)
    for X in (P[0], Q[0]):
        M.line(c, X, y - 14, X, y + 14, cor, q, 4)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, s, (P[0] + Q[0]) / 2, y + size + 6, size, "b", cor, a))


# ---------------- a figura: A e B no chão, o topo T sobre o pé F (A–F = 900 px) ----------------
GY, UM = 860, 5.2                       # chão e px por metro (morro: x = 50, d = 100)
FF = (900, GY)
FB, FA = (900 - 50 * UM, GY), (900 - 150 * UM, GY)
FT = (900, GY - 50 * R3 * UM)
KU = UM / 6                             # o desenho do morro foi feito para 6 px/m


def _m(x, y):
    """ponto do desenho original (F em 1060, 6 px/m) levado à escala atual"""
    return FF[0] + (x - 1060) * KU, GY - (GY - y) * KU


def morro(c, a):
    if a <= 0:
        return
    T = FT
    p = skia.Path()
    p.moveTo(*_m(840, GY))
    for q in ((905, GY - 170), (960, GY - 300), (1010, GY - 420)):
        p.lineTo(*_m(*q))
    p.lineTo(T[0], T[1])
    p.quadTo(*_m(1140, GY - 400), *_m(1180, GY - 290)); p.quadTo(*_m(1230, GY - 160), *_m(1320, GY))
    p.close()
    c.drawPath(p, M.paint(TERRA, 0.22 * a))
    pt = M.paint(TERRA, a, stroke=5); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)


def predio(c, a):
    if a <= 0:
        return
    r = skia.Rect.MakeLTRB(FF[0], FT[1], FF[0] + 130, GY)
    c.drawRect(r, M.paint(CINZA, 0.3 * a))
    c.drawRect(r, M.paint(TINTA, a, stroke=5))
    for i in range(1, 9):
        y = lerp(GY, FT[1], i / 9)
        for j in range(3):
            c.drawRect(skia.Rect.MakeXYWH(FF[0] + 16 + j * 38, y + 8, 22, 20), M.paint(TINTA2, 0.35 * a))


def cena(c, t, k, d="100 m", x_txt="x", escuro=False, objeto=morro):
    """k = instantes: base, alt, A, B, ang_a, ang_b, d, x, h, triB, triA, xd (x + d sob o chão), escondeF"""
    tinta = BR if escuro else TINTA
    q = ep(t, k["base"], 0.6)
    if q > 0:
        M.line(c, 50, GY, 1200, GY, TINTA2 if not escuro else CLARO, q, 5)
        objeto(c, q)
    if k.get("alt") is not None and t >= k["alt"]:
        grosso(c, FT, FF, OPO if k.get("triB") is not None and t >= k["triB"] or k.get("triA") is not None and t >= k["triA"] else tinta,
               1.0, 10 if (k.get("triB") is not None and t >= k["triB"]) else 6, ease_io(prog(t, k["alt"], 0.7)), dash=E.TRACO)
        E.angulo(c, t, k["alt"] + 0.5, FF, FB, FT, r=44, preenche=0.0)
        c.drawCircle(*FT, 10 * ease_back(prog(t, k["alt"], 0.35)), M.paint(tinta))
    for nome, P, chave, ang, kang in (("A", FA, "A", "30°", "ang_a"), ("B", FB, "B", "60°", "ang_b")):
        if k.get(chave) is not None and t >= k[chave]:
            sel = k.get("triA" if nome == "A" else "triB")
            on = sel is not None and t >= sel
            grosso(c, P, FT, HIP if on else TINTA2, 1.0, 8 if on else 4, ease_io(prog(t, k[chave], 0.7)), dash=None if on else E.TRACO)
            c.drawCircle(*P, 12 * ease_back(prog(t, k[chave], 0.35)), M.paint(tinta))
            E.foco(c, t, k[chave] + 0.2, 0.4, lambda a, nome=nome, P=P: centro(c, nome, P[0] - 46, P[1] - 22, 52, "g", tinta, a))
            E.angulo(c, t, k[chave] + 0.5, P, FF, FT, None, r=120 if nome == "A" else 80)
            dx = 175 if nome == "A" else 125
            E.foco(c, t, k[chave] + 0.7, 0.4, lambda a, P=P, ang=ang, dx=dx: E._meio(c, ang, P[0] + dx, P[1] - 36, 50, "b", COR if not escuro else CLARO, a))
    # lados com nome
    if k.get("triB") is not None and t >= k["triB"]:
        grosso(c, FB, FF, ADJ, 1.0, 12, ease_io(prog(t, k["triB"], 0.5)))
    if k.get("triA") is not None and t >= k["triA"]:
        grosso(c, FA, FF, ADJ, 1.0, 12, ease_io(prog(t, k["triA"], 0.5)))
    if k.get("d") is not None:
        cota(c, t, k["d"], FA, FB, d, GY + 45, tinta)
    if k.get("x") is not None:
        cor_x = ADJ if (k.get("triB") is not None and t >= k["triB"]) else COR
        cota(c, t, k["x"], FB, FF, x_txt, GY + 45, cor_x)
    if k.get("xd") is not None:
        yx = GY + 150
        E.foco(c, t, k["xd"], 0.4, lambda a: (M.line(c, FA[0], yx, FF[0], yx, ADJ, a, 4),
                                              M.line(c, FA[0], yx - 14, FA[0], yx + 14, ADJ, a, 4),
                                              M.line(c, FF[0], yx - 14, FF[0], yx + 14, ADJ, a, 4),
                                              E.formula(c, f"{x_txt} + {d.split()[0]}", FF[0] + 30, yx + 18, 52, "b", ADJ, a, "left")))
    if k.get("h") is not None:
        hx = FF[0] + 50 if objeto is morro else FF[0] - 50
        E.foco(c, t, k["h"], 0.4, lambda a: E._meio(c, "h", hx, (FF[1] + FT[1]) / 2, 72, "g", OPO, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1, e1 = (C[f"s01.{k}"] for k in "abcde")
    X = 1530

    def um():
        cena(c, t, dict(base=a1, alt=b1, A=c1, B=d1, d=d1 + 0.6, h=e1))
        E.foco(c, t, b1 + 0.4, 0.4, lambda a: (E.escreve(c, "?", FF[0] + 120, GY - 40, 70, "g", ERRADO, a)))
        E.frase(c, t, a1 + 0.3, ps("um", "i", 84) + [("morro", "g", 96, COR)], X, 230, "center", 0.12)
        E.frase(c, t, b1, ps("o pé da altura fica", "i", 54, TINTA2), X, 360, "center", 0.08)
        E.frase(c, t, b1 + 1.2, [("dentro do morro", "g", 60, ERRADO)], X, 440, "center", 0.1)
        E.frase(c, t, c1, ps("de A:", "i", 64) + [("30°", "g", 70, COR)], X, 580, "center", 0.1)
        E.frase(c, t, d1, ps("100 m depois:", "i", 64) + [("60°", "g", 70, COR)], X, 690, "center", 0.1)
        E.frase(c, t, e1, ps("a", "i", 76) + [("altura?", "g", 90, OPO)], X, 860, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), [("dois ângulos", "g", 100, COR)], XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("viram um", "i", 90) + [("sistema", "g", 100, COR)], XE, 610, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 545, 80, "g", E.SOBRE, a),
                                               centro(c, "sem sistema", 1500, 630, 72, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 860, 940
    kb, kc = C["s03.b"], C["s03.c"]
    # 1: altura com a tangente
    p = ep(t, kb, 0.5)
    E.caixa_pontilhada(c, x, 200, w, 300, p, prog_=p)
    E.frase(c, t, kb + 0.1, [("altura com a tangente", "i", 60)], x + 44, 290)
    E.formula_em(c, t, lerp(kb, kc, 0.35), "tg 30° = f{r{3}}{3}", x + 44, 420, 70, "g", COR)
    E.formula_em(c, t, lerp(kb, kc, 0.75), "tg 60° = r{3}", x + 520, 420, 70, "g", COR)
    # 2: substituição
    p = ep(t, kc, 0.5)
    E.caixa_pontilhada(c, x, 560, w, 260, p, prog_=p)
    E.frase(c, t, kc + 0.1, [("sistema por", "i", 60)] + [("substituição", "g", 64, COR)], x + 44, 650)
    E.frase(c, t, kc + 1.2, ps("isola uma letra e troca na outra", "i", 54, TINTA2), x + 44, 750, "left", 0.08)
    py = lerp(470, 790, ease_io(prog(t, kc - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, kb, 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- desenho ----------------
def b_desenho(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    X = 1530
    cena(c, t, dict(base=C["s04"] - 0.3, alt=a4, A=b4, B=c4, d=c4 + 0.6, h=b5, x=c5, xd=d5))
    if t >= d4:  # os dois triângulos, um de cada vez
        k1 = ep(t, d4, 0.4) * (1 - ep(t, d4 + 1.6, 0.4))
        k2 = ep(t, d4 + 1.6, 0.4) * (1 - ep(t, C["s05"], 0.4))
        pinta(c, [FA, FF, FT], E.COR, k1, 0.18)
        pinta(c, [FB, FF, FT], E.COR, k2, 0.25)

    def quatro():
        E.frase(c, t, C["s04"] + 0.1, [("desenhe", "g", 80, COR)], X, 220, "center")
        E.frase(c, t, a4, ps("do topo, a", "i", 60) + [("altura", "g", 64, OPO)], X, 360, "center", 0.1)
        E.frase(c, t, b4, ps("em A:", "i", 60) + [("30°", "g", 64, COR)], X, 480, "center", 0.1)
        E.frase(c, t, c4, ps("em B:", "i", 60) + [("60°", "g", 64, COR)], X, 590, "center", 0.1)
        E.frase(c, t, d4, [("2", "g", 70, COR)] + ps("triângulos retângulos", "i", 56), X, 740, "center", 0.1)
        E.frase(c, t, d4 + 0.8, ps("com a", "i", 56) + [("mesma altura", "g", 60, OPO)], X, 830, "center", 0.1)
    E.saida(c, t, C["s05"] - 0.1, quatro)
    if t < C["s05"] - 0.1:
        return
    E.frase(c, t, a5, ps("você não sabe", "i", 64) + [("2 coisas", "g", 68, COR)], X, 220, "center", 0.1)
    lista(c, t, [(b5, ps("a altura", "i", 58) + [("h", "g", 64, OPO)]),
                 (c5, ps("de B ao pé:", "i", 58) + [("x", "g", 64, COR)])], 1330, 370, 130, 58)
    E.frase(c, t, d5, ps("de A:", "i", 60) + [("x + 100", "g", 64, ADJ)], X, 650, "center", 0.1)
    E.frase(c, t, e5, [("2 letras", "g", 60, COR)] + [("→", "b", 56)] + [("2 equações", "g", 60, COR)], X, 820, "center", 0.1)


# ---------------- sistema ----------------
def b_sistema(c, t, C, b):
    a6, b6, c6 = (C[f"s06.{k}"] for k in "abc")
    a7, b7, c7 = (C[f"s07.{k}"] for k in "abc")
    a8, b8, c8 = (C[f"s08.{k}"] for k in "abc")
    a9, b9, c9 = (C[f"s09.{k}"] for k in "abc")
    a0, b0, c0 = (C[f"s10.{k}"] for k in "abc")
    X = 1530

    def figura():
        ent = C["s06"] - 0.4
        cena(c, t, dict(base=ent, alt=ent, A=ent, B=ent, d=ent, h=ent, x=ent, triB=a6 if t < C["s07"] else None,
                        triA=a7 if t >= C["s07"] else None, xd=a7 if t >= C["s07"] else None))

        def seis():
            E.frase(c, t, a6, ps("triângulo de", "i", 62) + [("B", "g", 66)], X, 200, "center", 0.1)
            E.frase(c, t, a6 + 0.8, [("oposto h", "g", 56, OPO)], X, 290, "center", 0.1)
            E.frase(c, t, a6 + 1.4, [("adjacente x", "g", 56, ADJ)], X, 360, "center", 0.1)
            fcen(c, t, b6, "tg 60° = r{3}", X, 490, 76)
            fcen(c, t, lerp(b6, c6, 0.5), "r{3} = f{h}{x}", X, 660, 90)
            resp(c, t, c6, "h = xr{3}", X, 820, 76)
        E.saida(c, t, C["s07"] - 0.1, seis)
        if t >= C["s07"] - 0.1:
            E.frase(c, t, a7, ps("triângulo de", "i", 62) + [("A", "g", 66)], X, 200, "center", 0.1)
            E.frase(c, t, a7 + 0.8, [("oposto h", "g", 56, OPO)], X, 290, "center", 0.1)
            E.frase(c, t, a7 + 1.4, [("adjacente x + 100", "g", 56, ADJ)], X, 360, "center", 0.1)
            fcen(c, t, b7 - 0.6, "tg 30° = f{r{3}}{3}", X, 490, 66)
            fcen(c, t, b7 + 1.0, "f{r{3}}{3} = f{h}{x + 100}", X, 670, 76)
            resp(c, t, c7, "h = f{(x + 100)r{3}}{3}", X, 880, 60, 2.6)
    E.saida(c, t, C["s08"] - 0.1, figura)
    if t < C["s08"] - 0.1:
        return
    # o sistema e a substituição, na tela toda
    E.sistema(c, t, C["s08"], ["h = xr{3}", "h = f{(x + 100)r{3}}{3}"], 200, 250, 76, dy=150)
    E.frase(c, t, C["s08"] + 0.3, ps("esse é o", "i", 52, TINTA2) + [("sistema", "g", 56, COR)], 200, 140, "left", 0.1)
    X2 = 1300

    def oito():
        fcen(c, t, a8, "xr{3} = f{(x + 100)r{3}}{3}", X2, 280, 84)
        E.frase(c, t, a8 + 0.4, ps("troque o h por", "i", 50, TINTA2) + [("x√3", "g", 54, COR)], X2, 400, "center", 0.08)
        pilula(c, t, b8, "÷ √3 nos dois lados", X2, 560, 60)
        fcen(c, t, c8, "x = f{x + 100}{3}", X2, 800, 110, COR)
    E.saida(c, t, C["s09"] - 0.1, oito)
    if t < C["s09"] - 0.1:
        return

    def nove():
        fcen(c, t, C["s09"], "x = f{x + 100}{3}", 520, 620, 90, TINTA2)
        E.foco(c, t, a9, 0.5, lambda a: E.pilula(c, "× 3", X2 - 330, 300, 56, "g", a=a, cor=E.SOBRE))
        fcen(c, t, a9 + 0.4, "3x = x + 100", X2 + 80, 320, 96)
        E.foco(c, t, b9, 0.5, lambda a: E.pilula(c, "− x", X2 - 330, 500, 56, "g", a=a, cor=E.SOBRE))
        fcen(c, t, b9 + 0.4, "2x = 100", X2 + 80, 520, 96)
        resp(c, t, c9, "x = 50 m", X2 + 80, 760, 80)
    E.saida(c, t, C["s10"] - 0.1, nove)
    if t < C["s10"] - 0.1:
        return
    E.frase(c, t, C["s10"] + 0.2, ps("volte na 1ª equação", "i", 60, TINTA2), X2, 220, "center", 0.1)
    fcen(c, t, a0, "h = 50r{3}", X2, 400, 110, OPO)
    fcen(c, t, b0, "50 × 1,7 = 85", X2, 580, 96)
    resp(c, t, c0, "h ≈ 85 m", X2, 780, 80)
    E.frase(c, t, c0 + 0.6, ps("pouco mais de 85 m", "i", 54, TINTA2), X2, 930, "center", 0.08)
    if t >= a0:  # a primeira linha do sistema acende
        M.rrect(c, 190, 165, 470, 120, 30, E.COR, 0.10 * ep(t, a0, 0.4))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1 = (C[f"s11.{k}"] for k in "abc")
    a2, b2, c2 = (C[f"s12.{k}"] for k in "abc")
    X = 1530
    ent = C["s11"]
    cena(c, t, dict(base=ent, alt=ent, A=ent + 0.2, B=ent + 0.2, x=c2 - 0.6, xd=b2))
    # os 100 m tratados como a distância até o morro (errado)
    E.saida(c, t, a2, lambda: E.foco(c, t, a1, 0.4, lambda a: (grosso(c, FA, FF, ERRADO, a, 10),
                                                               centro(c, "100 m?", (FA[0] + FF[0]) / 2, GY + 110, 60, "b", ERRADO, a))))
    if t >= a2:
        grosso(c, FA, FB, CERTO, 1.0, 12, ease_io(prog(t, a2, 0.5)))
        cota(c, t, a2 + 0.2, FA, FB, "100 m", GY + 45, CERTO)

    def onze():
        E.frase(c, t, a1, ps("o erro:", "i", 62) + [("100 m até o morro", "g", 62, ERRADO)], X, 220, "center", 0.1)
        fcen(c, t, b1, "100 · tg 30°", X, 400, 80)
        fcen(c, t, b1 + 1.6, "= f{100r{3}}{3}", X, 570, 84)
        fcen(c, t, c1, "≈ 57 m", X - 40, 760, 100, ERRADO)
        E.foco(c, t, c1 + 0.5, 0.5, lambda a: E.selo(c, X + 200, 728, 46, False, a))
    E.saida(c, t, C["s12"] - 0.1, onze)
    if t < C["s12"] - 0.1:
        return
    E.frase(c, t, a2, ps("100 m: só de", "i", 60) + [("A até B", "g", 64, CERTO)], X, 220, "center", 0.1)
    E.frase(c, t, b2, ps("de A ao pé:", "i", 60) + [("x + 100", "g", 64, ADJ)], X, 380, "center", 0.1)
    E.frase(c, t, b2 + 1.2, ps("e o x ainda é", "i", 56, TINTA2) + [("?", "g", 60, ERRADO)], X, 480, "center", 0.1)
    E.foco(c, t, c2, 0.5, lambda a: E.caixa_pontilhada(c, X - 300, 620, 600, 200, a, COR, prog_=ep(t, c2, 0.6)))
    E.frase(c, t, c2 + 0.1, ps("precisa das", "i", 60), X, 700, "center", 0.1)
    E.frase(c, t, c2 + 0.5, [("2 equações", "g", 70, COR)], X, 790, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    a5, b5, c5 = (C[f"s15.{k}"] for k in "abc")
    X = 1530
    ent = C["s13"]
    G = ((FA[0] + FB[0] + FT[0]) / 3, (FA[1] + FB[1] + FT[1]) / 3)

    def figura():
        q = ep(t, ent, 0.6)
        M.line(c, 50, GY, 1150, GY, CLARO, q, 4)
        grosso(c, FA, FT, BR, q, 5)
        grosso(c, FB, FT, BR, q, 5)
        grosso(c, FT, FF, CLARO, q, 4, dash=E.TRACO)
        for nome, P in (("A", FA), ("B", FB), ("F", FF)):
            if nome != "F":
                E.foco(c, t, ent, 0.4, lambda a, nome=nome, P=P: (c.drawCircle(*P, 11, M.paint(BR, a)),
                                                                  centro(c, nome, P[0], P[1] + 64, 56, "g", BR, a)))
        if t >= a3:
            pinta(c, [FA, FB, FT], CLARO, ep(t, a3, 0.5), 0.25)
        E.angulo(c, t, ent + 0.3, FA, FF, FT, None, r=130, cor=CLARO)
        E.foco(c, t, ent + 0.5, 0.4, lambda a: E._meio(c, "30°", FA[0] + 190, FA[1] - 36, 50, "b", CLARO, a))
        E.angulo(c, t, b3, FB, FF, FT, None, r=90, cor=CLARO)
        E.foco(c, t, b3 + 0.3, 0.4, lambda a: E._meio(c, "60°", FB[0] + 140, FB[1] - 36, 50, "b", BR, a))
        E.angulo(c, t, d3, FT, FA, FB, None, r=150, cor=OPO)
        E.foco(c, t, d3 + 0.3, 0.4, lambda a: E._meio(c, "30°", FT[0] - 240, FT[1] + 20, 50, "b", OPO, a))
        # isósceles: os dois lados iguais
        E.foco(c, t, a4, 0.4, lambda a: (E.marcas_iguais(c, FA, FB, 2, BR, a), E.marcas_iguais(c, FB, FT, 2, BR, a)))
        E.foco(c, t, b4, 0.4, lambda a: (centro(c, "100", (FA[0] + FB[0]) / 2, GY + 70, 56, "b", BR, a),
                                         txt_lado(c, FB, FT, "100", (FB[0] + 200, FB[1] - 60), 56, BR, a, gap=52)))
        if t >= c4:  # no triângulo de B: hipotenusa BT, oposto TF
            grosso(c, FB, FT, CLARO, 1.0, 12, ease_io(prog(t, c4, 0.5)))
            grosso(c, FT, FF, OPO, 1.0, 12, ease_io(prog(t, c4 + 0.6, 0.5)))
            E.foco(c, t, c4 + 0.8, 0.4, lambda a: E._meio(c, "h", FF[0] + 50, (FF[1] + FT[1]) / 2, 64, "g", OPO, a))
    E.saida(c, t, C["s15"] - 0.1, figura)

    def treze():
        E.frase(c, t, ent + 0.2, ps("o atalho do", "i", 60, CLARO) + [("30° e 60°", "g", 64, BR)], X, 200, "center", 0.1)
        E.frase(c, t, b3, ps("60° em B:", "i", 58, CLARO) + [("ângulo externo", "g", 60, BR)], X, 340, "center", 0.1)
        fcen(c, t, c3, "60° = 30° + ?", X, 500, 80, BR)
        fcen(c, t, d3, "topo = 30°", X, 660, 84, OPO)
    E.saida(c, t, C["s14"] - 0.1, treze)

    def quatorze():
        E.frase(c, t, a4, [("2 ângulos de 30°:", "g", 58, BR)], X, 200, "center", 0.1)
        E.frase(c, t, a4 + 0.8, [("isósceles", "g", 70, OPO)], X, 300, "center", 0.1)
        fcen(c, t, b4, "BT = AB = 100", X, 440, 72, BR)
        E.frase(c, t, c4, [("hipotenusa 100,", "g", 54, CLARO)] + [("oposto h", "g", 54, OPO)], X, 580, "center", 0.1)
        fcen(c, t, d4, "h = 100 · sen 60°", X, 720, 70, BR)
        fcen(c, t, d4 + 1.8, "= 100 · f{r{3}}{2} = 50r{3}", X, 880, 66, BR)
        E.frase(c, t, d4 + 3.4, [("sem sistema", "g", 56, OPO)], X, 1010, "center", 0.1)
    E.saida(c, t, C["s15"] - 0.1, quatorze)
    if t < C["s15"] - 0.1:
        return
    E.frase(c, t, a5, [("60°", "g", 96, BR)] + ps("é o dobro de", "i", 80, CLARO) + [("30°", "g", 96, BR)], W / 2, 280, "center", 0.12)
    E.frase(c, t, a5 + 1.2, ps("o topo sai igual ao ângulo em A", "i", 60, CLARO), W / 2, 400, "center", 0.1)
    E.foco(c, t, b5, 0.5, lambda a: E.selo(c, 520, 600, 50, False, a))
    E.frase(c, t, b5, [("30° e 45°?", "g", 76, BR)] + ps("não é isósceles", "i", 66, CLARO), 600, 625, "left", 0.1)
    E.frase(c, t, c5, ps("aí, o", "i", 80, CLARO) + [("sistema", "g", 90, BR)] + ps("é o caminho", "i", 80, CLARO), W / 2, 850, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a6, b6, c6, d6, e6 = (C[f"s16.{k}"] for k in "abcde")
    X = 1530
    cena(c, t, dict(base=a6, alt=a6 + 0.3, A=a6 + 0.5, B=c6, d=b6, h=d6, x=e6, x_txt="?"), d="80 m", objeto=predio)

    def texto():
        E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 70, COR), X, 190, "center", 0.12)
        E.frase(c, t, a6, ps("de A:", "i", 60) + [("30°", "g", 66, COR)], X, 320, "center", 0.1)
        E.frase(c, t, b6, ps("anda", "i", 60) + [("80 m", "g", 66, COR)] + ps("até B", "i", 60), X, 430, "center", 0.1)
        E.frase(c, t, c6, ps("de B:", "i", 60) + [("60°", "g", 66, COR)], X, 540, "center", 0.1)
        E.frase(c, t, d6, ps("a", "i", 66) + [("altura?", "g", 76, OPO)], X, 700, "center", 0.1)
        E.frase(c, t, e6, ps("e de", "i", 60) + [("B ao prédio?", "g", 66, COR)], X, 810, "center", 0.1)
        E.foco(c, t, e6 + 1.2, 0.5, lambda a: E.formula(c, "r{3} ≈ 1,7", X, 950, 60, "g", TINTA2, a, "center"))
    E.saida(c, t, C["s17.a"] - 0.2, texto)
    E.relogio(c, t, C["s17.a"], 1600, 430, 160)
    E.foco(c, t, C["s17.a"] + 0.4, 0.5, lambda a: E.formula(c, "r{3} ≈ 1,7", 1600, 1010, 56, "g", TINTA2, a, "center"))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    E.frase(c, t, C["s18"] + 0.1, ps("vamos lá", "i", 64, COR), 200, 140, "left", 0.1)
    E.sistema(c, t, a8, ["h = xr{3}", "h = f{(x + 80)r{3}}{3}"], 200, 290, 72, dy=150, tl=[a8, b8])

    E.foco(c, t, a8 + 0.3, 0.4, lambda a: E.escreve(c, "de B", 560, 290, 46, "i", TINTA2, a))
    E.foco(c, t, b8 + 0.3, 0.4, lambda a: E.escreve(c, "de A", 700, 440, 46, "i", TINTA2, a))
    X = 1320

    def dezoito():
        E.foco(c, t, c8, 0.5, lambda a: E.pilula(c, "substitui e ÷ √3", X, 230, 52, "g", a=a, cor=E.SOBRE))
        fcen(c, t, c8 + 1.6, "3x = x + 80", X, 420, 96)
        fcen(c, t, d8, "2x = 80", X, 580, 96)
        resp(c, t, d8 + 1.4, "x = 40 m", X, 800, 80)
    E.saida(c, t, C["s19"] - 0.1, dezoito)
    if t < C["s19"] - 0.1:
        return
    resp(c, t, C["s19"], "x = 40 m", 470, 570, 56)
    fcen(c, t, a9, "h = 40r{3}", 560, 720, 96, OPO)
    fcen(c, t, b9, "40 × 1,7 = 68", 560, 860, 84)
    resp(c, t, b9 + 2.0, "h ≈ 68 m", 560, 990, 60)
    E.frase(c, t, c9 - 0.6, ps("pelo atalho", "i", 64, COR), X + 100, 220, "center", 0.1)
    fcen(c, t, c9, "BT = AB = 80", X + 100, 380, 84)
    fcen(c, t, d9, "80 · f{r{3}}{2} = 40r{3}", X + 100, 580, 84)
    E.foco(c, t, d9 + 2.2, 0.5, lambda a: (E.selo(c, X + 100, 780, 56, True, a), centro(c, "bateu", X + 100, 900, 60, "i", CERTO, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", "uma letra para a altura,", "outra para a distância"), ("s20.b", "uma equação", "de cada ponto"),
                 ("s20.c", "e", "substituição"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 68) + [(l2, "g", 70, COR)], 320, y, "left", 0.1)
    t_fim = min(C["s21"] + 1.4, C["s21.a"] - 0.5)   # o 3º item é a última palavra da cena: fica um pouco mais
    E.saida(c, t, t_fim, resumo)
    if t < t_fim:
        return
    a1, b1 = C["s21.a"], C["s21.b"]
    E.frase(c, t, t_fim + 0.1, ps("na próxima aula, prática:", "i", 80), XE, 230, passo=0.12)
    E.frase(c, t, a1, [("altura, rampa", "g", 84, COR)] + ps("e", "i", 80) + [("distância", "g", 84, COR)], XE, 380, passo=0.11)
    E.frase(c, t, b1, ps("com e sem ângulo", "i", 72) + [("da tabela", "g", 78, COR)], XE, 510, passo=0.1)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1000, 785, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, desenho=b_desenho, sistema=b_sistema, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
