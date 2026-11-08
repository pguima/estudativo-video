"""Visual — Estudativo · MAT-TRI-004: altura da torre (30 m, 60°: h = 30√3 ≈ 52 m), inclinação da rampa (2 em 4: 30°) e largura do rio.
Linguagem da trigonometria (a mesma de MAT-TRI-001 a 003 e da geometria plana): lados em tinta; cada lado ganha a cor do seu nome
a partir do ângulo da vez — OPO (cateto oposto), ADJ (cateto adjacente), HIP (hipotenusa, índigo da matéria); ângulo da vez = arco
com cunha na cor da matéria; ângulo reto = quadradinho; medidas na grotesca; sen, cos e tg abreviados; resposta na esfera; erro em
vermelho, certo em verde; atalho no palco escuro.
A figura não mente: a torre tem 30√3 para 30 de chão (60° de verdade), a rampa 2 para 4 (30°) e o rio 10√3 para 30.
Peças locais: torre() (o prédio, que cresce do chão), cena_torre() (chão, olhar, ângulo e lados com nome), rio() (a vista de cima,
com as margens), pessoa(), grosso(), txt_lado(), lista() (linhas numeradas das três perguntas).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-004_altura_rampa_e_distancia_inacessivel.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("torre", "rampa", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
HIP, OPO, ADJ = E.COR, AMBAR, "#0E9AA7"      # cor fixa de cada lado da trigonometria
ADJ_ESC = "#3CC7D3"                         # o adjacente no palco escuro
R3 = math.sqrt(3)
assert round(30 * 1.7) == 51 and round(30 * 1.73, 2) == 51.9 and round(30 * R3) == 52
assert 2 / 4 == 0.5 and abs(math.degrees(math.asin(0.5)) - 30) < 1e-9
assert abs(30 * R3 / 2 - 15 * R3) < 1e-9 and round(15 * 1.7, 1) == 25.5
assert 180 - 90 - 60 == 30 and abs(30 * (R3 / 3) - 10 * R3) < 1e-9 and 30 // 3 == 10 and round(10 * 1.7) == 17 < 30
assert abs(30 / R3 - 10 * R3) < 1e-9


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")))


def meio(P, Q):
    return (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2


def txt_lado(c, P, Q, s, G, size=54, cor=None, a=1.0, gap=20, dentro=False):
    """rótulo ao lado do segmento PQ, do lado de fora do triângulo de centro G"""
    if a <= 0 or not s:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = meio(P, Q)
    fora = (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 > (mx - G[0]) ** 2 + (my - G[1]) ** 2
    if fora == dentro:
        nx, ny = -nx, -ny
    E._cola(c, s, mx, my, nx, ny, gap, size, "b", cor or COR, a)


def grosso(c, P, Q, cor, a, larg=12, p=1.0, dash=None):
    if a > 0 and p > 0:
        M.line(c, *P, *Q, cor, a, larg, progress=p, dash=dash)


def pinta(c, pts, cor, a, alfa=0.14):
    if a > 0:
        path = skia.Path(); path.addPoly(pts, True)
        c.drawPath(path, M.paint(cor, alfa * a))


def torre(c, B, T, p, a=1.0, larg=46):
    """o prédio da torre, à direita da linha B–T, crescendo do chão (p = 0..1)"""
    if a <= 0 or p <= 0:
        return
    y = lerp(B[1], T[1], ease_io(p))
    r = skia.Rect.MakeLTRB(B[0], y, B[0] + larg, B[1])
    c.drawRect(r, M.paint(CINZA, 0.35 * a))
    c.drawRect(r, M.paint(TINTA, a, stroke=4))
    for k in range(1, 8):  # andares
        yy = lerp(B[1], T[1], k / 8)
        if yy > y + 6:
            M.line(c, B[0] + 8, yy, B[0] + larg - 8, yy, TINTA2, 0.5 * a, 3)
    if p >= 1:
        M.line(c, B[0] + larg / 2, T[1], B[0] + larg / 2, T[1] - 40, TINTA, a, 4)
        c.drawCircle(B[0] + larg / 2, T[1] - 44, 7, M.paint(ERRADO, a))


def chao(c, x0, x1, y, a=1.0, p=1.0):
    if a > 0 and p > 0:
        M.line(c, x0, y, x1, y, TINTA2, a, 5, progress=p)
        for k in range(int((x1 - x0) / 40) + 1):  # hachura do terreno
            x = x0 + 20 + k * 40
            if x < lerp(x0, x1, p) - 10:
                M.line(c, x, y + 6, x - 16, y + 26, TINTA2, 0.35 * a, 3)


def pessoa(c, x, ypes, h, a=1.0, cor=TINTA):
    """bonequinho de altura h com os pés em (x, ypes); devolve o olho"""
    if a <= 0:
        return (x, ypes - h * 0.9)
    rc = h * 0.11
    cy = ypes - h + rc
    c.drawCircle(x, cy, rc, M.paint(cor, a, stroke=5))
    M.line(c, x, cy + rc, x, ypes - h * 0.45, cor, a, 6)
    M.line(c, x, ypes - h * 0.45, x - h * 0.16, ypes, cor, a, 6)
    M.line(c, x, ypes - h * 0.45, x + h * 0.16, ypes, cor, a, 6)
    M.line(c, x - h * 0.2, ypes - h * 0.68, x + h * 0.2, ypes - h * 0.68, cor, a, 6)
    return (x, cy)


def resp(c, t, t0, s, cx, cy, size=76):
    """resposta comprida numa pílula com volume, na cor da matéria"""
    def f(a):
        w = E.formula(c, s, 0, 0, size, a=0) + size * 1.1
        h = size * 1.75
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, E.COR, a, shadow=True)
        E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")
    E.foco(c, t, t0, 0.5, f)


def lista(c, t, itens, x, y0, dy=150, size=64):
    """linhas numeradas [(t0, partes)] com o número na esfera"""
    for i, (t0, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - size * 0.36, 40, a=a),
                                                   centro(c, str(i + 1), x + 40, y - size * 0.36 + 18, 50, "g", BR, a)))
        E.frase(c, t, t0 + 0.1, partes, x + 110, y, "left", 0.1)


def pilula(c, t, t0, s, cx, cy, size=64):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, s, cx, cy, size, "g", a=a, cor=E.SOBRE))


# ---------------- a torre: 30 m de chão, 60° (desenho: 400 px = 30 m) ----------------
TO, TB = (230, 900), (630, 900)
TT = (630, 900 - 400 * R3)
TG = ((TO[0] + TB[0] + TT[0]) / 3, (TO[1] + TB[1] + TT[1]) / 3)


def cena_torre(c, t, k, O=TO, B=TB, T=TT, chao_med="30 m"):
    """k = instantes: torre, chao, olhar, ang, rotulo60, reto, tri, adj, opo, h, hip_q (None = não aparece)"""
    G = ((O[0] + B[0] + T[0]) / 3, (O[1] + B[1] + T[1]) / 3)
    if k.get("tri") is not None:
        pinta(c, [O, B, T], E.COR, ep(t, k["tri"], 0.6))
    chao(c, O[0] - 90, B[0] + 170, O[1], 1.0, ep(t, k["torre"], 0.6))
    torre(c, B, T, prog(t, k["torre"], 1.0))
    if k.get("chao") is not None and t >= k["chao"]:
        grosso(c, O, B, ADJ if k.get("adj") is not None and t >= k["adj"] else TINTA, 1.0, 8 if k.get("adj") is None or t < k["adj"] else 12,
               ease_io(prog(t, k["chao"], 0.6)))
        c.drawCircle(*O, 11 * ease_back(prog(t, k["chao"], 0.35)), M.paint(TINTA))
        E.foco(c, t, k["chao"] + 0.4, 0.4, lambda a: txt_lado(c, O, B, chao_med, G, 64, ADJ if k.get("adj") is not None and t >= k["adj"] else TINTA, a))
    if k.get("olhar") is not None and t >= k["olhar"]:
        if k.get("hip_q") is not None and t >= k["hip_q"]:
            grosso(c, O, T, HIP, 1.0, 10, 1.0, dash=E.TRACO)
        else:
            grosso(c, O, T, TINTA2, 1.0, 5, ease_io(prog(t, k["olhar"], 0.8)), dash=E.TRACO)
    if k.get("ang") is not None:
        E.angulo(c, t, k["ang"], O, B, T, None, r=110)
        E.foco(c, t, k.get("rotulo60") or 1e9, 0.4, lambda a: E._meio(c, "60°", O[0] + 175, O[1] - 62, 56, "b", COR, a))
    if k.get("reto") is not None:
        E.angulo(c, t, k["reto"], B, O, T, r=60)
    if k.get("opo") is not None and t >= k["opo"]:
        grosso(c, B, T, OPO, 1.0, 12, ease_io(prog(t, k["opo"], 0.6)))
    if k.get("h") is not None:
        E.foco(c, t, k["h"], 0.4, lambda a: E._cola(c, k.get("h_txt", "h"), B[0] + 50, (B[1] + T[1]) / 2, 1, 0, 24, 76, "g", OPO, a))
    return G


def nome(c, t, t0, s, x, y, cor, size=52):
    """nome do lado (oposto, adjacente, hipotenusa) em itálica na cor do lado"""
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, "i", cor, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1, e1 = (C[f"s01.{k}"] for k in "abcde")
    X = 1340

    def um():
        cena_torre(c, t, dict(torre=a1, chao=b1, olhar=c1, ang=c1 + 0.4, rotulo60=c1 + 0.8, h=d1, h_txt="h = ?"))
        E.frase(c, t, a1 + 0.3, ps("uma", "i", 84) + [("torre", "g", 96, COR)], X, 250, "center", 0.12)
        E.frase(c, t, b1, ps("você a", "i", 72) + [("30 m", "g", 80, COR)] + ps("do pé", "i", 72), X, 400, "center", 0.12)
        E.frase(c, t, c1, ps("vê o topo a", "i", 72) + [("60°", "g", 80, COR)], X, 530, "center", 0.12)
        E.frase(c, t, d1, [("altura?", "g", 110, TINTA)], X, 720, "center")
        E.frase(c, t, e1 - 0.6, ps("sem subir, sem trena", "i", 60, TINTA2), X, 840, "center", 0.1)
        pilula(c, t, e1, "a tangente resolve", X, 950, 66)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 280, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), [("alturas", "g", 100, COR)] + ps("e", "i", 90) + [("distâncias", "g", 100, COR)], XE, 440, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("que não dá para alcançar", "i", 76, TINTA2), XE, 550, passo=0.1)
        E.frase(c, t, tb, ps("a", "i", 90) + [("inclinação", "g", 100, COR)] + ps("da rampa", "i", 90), XE, 720, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 545, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 630, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "as 3 perguntas", "ângulo, tenho, quero"), ("s03.c", "a tabela de", "30°, 45° e 60°"), ("s03.d", "r{3} perto de", "1,7"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        if "r{" in l1:
            E.formula_em(c, t, C[k] + 0.1, "r{3}", x + 44, y + 86, 64, "g", TINTA)
            E.frase(c, t, C[k] + 0.2, [("perto de", "i", 60)], x + 44 + E.formula(c, "r{3}", 0, 0, 64, a=0) + 22, y + 84)
        else:
            E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 64, COR)], x + 44, y + 164)
    alvo = [C[k] for k, _, _ in itens]
    q1, q2 = ease_io(prog(t, alvo[1] - 0.35, 0.5)), ease_io(prog(t, alvo[2] - 0.35, 0.5))
    py = lerp(lerp(340, 580, q1), 820, q2)
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 900, 1000, "left", 0.12)


# ---------------- torre ----------------
def b_torre(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8 = (C[f"s08.{k}"] for k in "abc")
    X = 1330

    def figura():
        cena_torre(c, t, dict(torre=C["s04"] - 0.2, chao=C["s04"], olhar=a4, ang=a4 + 0.5, rotulo60=a5, reto=d4, tri=c4,
                              adj=b5, opo=c5, h=b6))
        E.foco(c, t, b5 + 0.4, 0.4, lambda a: centro(c, "adjacente", (TO[0] + TB[0]) / 2, 1045, 50, "i", ADJ, a))
        E.foco(c, t, c5 + 0.4, 0.4, lambda a: E.escreve(c, "oposto", TB[0] + 70, TT[1] + 120, 56, "i", OPO, a))
        E.frase(c, t, b4, ps("ângulo de", "i", 56, COR) + [("elevação", "g", 60, COR)], 140, 300, "left", 0.1)
        if t >= b4:
            M.arrow(c, 300, 330, TO[0] + 90, TO[1] - 80, COR, ep(t, b4 + 0.3, 0.4), 4, 16, ep(t, b4 + 0.3, 0.5))
    E.saida(c, t, C["s08"] - 0.1, figura)

    def quatro():
        E.frase(c, t, a4, ps("entre o", "i", 64) + [("chão", "g", 70)] + ps("e o", "i", 64) + [("olhar", "g", 70)], X, 300, "center", 0.1)
        E.frase(c, t, c4, ps("torre, chão e olhar:", "i", 64), X, 500, "center", 0.1)
        E.frase(c, t, lerp(c4, d4, 0.4), [("triângulo retângulo", "g", 76, COR)], X, 600, "center", 0.1)
        E.frase(c, t, d4, ps("a torre fica", "i", 64) + [("em pé", "g", 70)] + [("→ 90°", "g", 70, COR)], X, 790, "center", 0.1)
    E.saida(c, t, C["s05"] - 0.1, quatro)

    def cinco():
        E.frase(c, t, C["s05"] + 0.1, ps("as 3 perguntas", "i", 70, COR), X, 190, "center", 0.1)
        lista(c, t, [(a5, ps("ângulo:", "i", 62) + [("60°", "g", 66, COR)]),
                     (b5, ps("tenho:", "i", 62) + [("30 m", "g", 66, ADJ)] + [("→ adjacente", "b", 58, ADJ)]),
                     (c5, ps("quero:", "i", 62) + [("altura", "g", 66, OPO)] + [("→ oposto", "b", 58, OPO)])], 930, 360, 150, 62)
        E.frase(c, t, d5, [("oposto", "g", 70, OPO)] + ps("e", "i", 66) + [("adjacente", "g", 70, ADJ)], X, 830, "center", 0.1)
        pilula(c, t, d5 + 1.0, "tangente", X, 940, 70)
    E.saida(c, t, C["s06"] - 0.1, cinco)

    def seis():
        fcen(c, t, a6, "tg 60° = r{3}", X, 250, 96)
        E.frase(c, t, b6, ps("altura =", "i", 64) + [("h", "g", 72, OPO)], X, 380, "center", 0.1)
        fcen(c, t, c6, "r{3} = f{h}{30}", X, 560, 110)
        E.frase(c, t, d6, [("× 30", "g", 60, TINTA2)] + ps("nos dois lados", "i", 58, TINTA2), X, 730, "center", 0.08)
        resp(c, t, e6, "h = 30r{3} m", X, 890, 80)
    E.saida(c, t, C["s07"] - 0.1, seis)

    def sete():
        E.frase(c, t, C["s07"] + 0.1, ps("quanto é isso?", "i", 70, COR), X, 200, "center", 0.1)
        fcen(c, t, a7, "30 × 1,7 = 51", X, 330, 90, TINTA2)
        fcen(c, t, b7, "r{3} ≈ 1,73", X, 460, 84)
        fcen(c, t, c7, "30 × 1,73 = 51,9", X, 590, 90)
        resp(c, t, c7 + 1.6, "≈ 52 m", X, 730, 76)
        E.foco(c, t, lerp(c7, d7, 0.55), 0.5, lambda a: E.formula(c, "1,7 < r{3}", X, 880, 64, "g", TINTA2, a, "center"))
        pilula(c, t, d7, "use o valor do enunciado", X, 990, 56)
    E.saida(c, t, C["s08"] - 0.1, sete)

    if t < C["s08"] - 0.1:
        return
    # s08: o olho no chão e a altura da pessoa
    O2, B2 = (300, 900), (700, 900)
    T2 = (700, 900 - 400 * R3)
    ent = C["s08"]
    cena_torre(c, t, dict(torre=ent - 0.3, chao=ent - 0.3, olhar=ent - 0.3, ang=ent - 0.3, rotulo60=ent - 0.3), O2, B2, T2)
    if t >= a8:
        k = ease_back(prog(t, a8, 0.4))
        c.drawCircle(*O2, 22 * k, M.paint(COR, 0.25))
        c.drawCircle(*O2, 11 * k, M.paint(COR))
    E.frase(c, t, a8, ps("o olho ficou", "i", 66) + [("no chão", "g", 72, COR)], X, 300, "center", 0.1)
    if t >= b8:
        q = ep(t, b8, 0.5)
        pessoa(c, O2[0], 900, 170, q)
        M.line(c, O2[0] - 90, 900, O2[0] - 90, 730, COR, q, 5)
        for yy in (900, 730):
            M.line(c, O2[0] - 104, yy, O2[0] - 76, yy, COR, q, 5)
    E.frase(c, t, b8, ps("a prova deu a", "i", 66) + [("altura da pessoa?", "g", 72, COR)], X, 480, "center", 0.1)
    E.frase(c, t, c8, [("some", "g", 80, COR)] + ps("no final", "i", 76), X, 650, "center", 0.12)
    fcen(c, t, c8 + 0.9, "torre = h + pessoa", X, 820, 76)


# ---------------- rampa: 4 m de rampa, 2 m de altura (160 px = 1 m) ----------------
RA, RB = (200, 860), (200 + 640 * R3 / 2, 860)
RT = (RB[0], 860 - 320)
RG = ((RA[0] + RB[0] + RT[0]) / 3, (RA[1] + RB[1] + RT[1]) / 3)


def b_rampa(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    X = 1360
    # a rampa (fica no bloco todo)
    chao(c, 110, 1000, 860, 1.0, ep(t, C["s09"], 0.6))
    if t >= a9:
        p = ease_io(prog(t, a9, 0.8))
        pinta(c, [RA, RB, RT], TINTA2, p, 0.18)
        grosso(c, RA, (lerp(RA[0], RT[0], p), lerp(RA[1], RT[1], p)), HIP if t >= b0 else TINTA, 1.0, 12 if t >= b0 else 8)
        E.angulo(c, t, a9 + 0.6, RA, RB, RT, None, r=120)
    E.foco(c, t, d9, 0.4, lambda a: E._meio(c, "θ = ?" if t < b1 else "θ = 30°", RA[0] + 220, RA[1] - 50, 52, "b", COR, a))
    if t >= c9:
        grosso(c, RB, RT, OPO if t >= c0 else TINTA, 1.0, 12 if t >= c0 else 7, ease_io(prog(t, c9, 0.6)))
        E.angulo(c, t, c9 + 0.5, RB, RA, RT, r=54)
    E.foco(c, t, b9, 0.4, lambda a: txt_lado(c, RA, RT, "4 m", RG, 66, HIP if t >= b0 else TINTA, a))
    E.foco(c, t, c9 + 0.4, 0.4, lambda a: txt_lado(c, RB, RT, "2 m", RG, 66, OPO if t >= c0 else TINTA, a))
    nome(c, t, b0 + 0.4, "hipotenusa", 140, 560, HIP, 52)
    E.foco(c, t, c0 + 0.4, 0.4, lambda a: E.escreve(c, "oposto", RB[0] - 60, RT[1] - 40, 52, "i", OPO, a))

    def nove():
        E.frase(c, t, a9, [("inclinação", "g", 76, COR)] + ps("=", "i", 70), X, 300, "center", 0.1)
        E.frase(c, t, a9 + 0.8, ps("ângulo com o chão", "i", 70), X, 400, "center", 0.1)
        E.frase(c, t, b9, ps("rampa de", "i", 64) + [("4 m", "g", 70, COR)], X, 560, "center", 0.1)
        E.frase(c, t, c9, ps("sobe", "i", 64) + [("2 m", "g", 70, COR)], X, 660, "center", 0.1)
        E.frase(c, t, d9, ps("qual é a", "i", 76) + [("inclinação?", "g", 80, COR)], X, 840, "center", 0.12)
    E.saida(c, t, C["s10"] - 0.1, nove)

    def dez():
        E.frase(c, t, a0, ps("falta", "i", 70) + [("o ângulo", "g", 76, COR)], X, 200, "center", 0.1)
        lista(c, t, [(b0, ps("rampa:", "i", 60) + [("hipotenusa, 4", "g", 62, HIP)]),
                     (c0, ps("altura:", "i", 60) + [("oposto, 2", "g", 62, OPO)])], 960, 360, 140, 60)
        E.frase(c, t, d0, [("oposto", "g", 66, OPO)] + ps("e", "i", 62) + [("hipotenusa:", "g", 66, HIP)] + [("sen", "g", 70, COR)], X, 650, "center", 0.1)
        fcen(c, t, e0, "sen θ = f{2}{4} = f{1}{2}", X, 860, 100)
    E.saida(c, t, C["s11"] - 0.1, dez)
    if t < C["s11"] - 0.1:
        return
    fcen(c, t, C["s11"] + 0.2, "sen θ = f{1}{2}", X, 240, 90, TINTA2)
    E.foco(c, t, a1, 0.5, lambda a: E.caixa_pontilhada(c, X - 300, 330, 600, 170, a, COR, prog_=ep(t, a1, 0.6)))
    fcen(c, t, a1 + 0.2, "sen 30° = f{1}{2}", X, 455, 90, COR)
    bola_txt(c, t, b1, "θ = 30°", X, 660, 110, 76)
    E.frase(c, t, c1, ps("de cabeça:", "i", 56, TINTA2) + [("está na tabela", "g", 58, TINTA2)], X, 860, "center", 0.1)
    E.frase(c, t, d1, ps("outro número?", "i", 56) + [("a prova dá o valor", "g", 58, COR)], X, 960, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2 = (C[f"s12.{k}"] for k in "abc")
    a3, b3, c3 = (C[f"s13.{k}"] for k in "abc")
    X = 1330
    O, B, T = TO, TB, TT
    ent = C["s12"]
    cena_torre(c, t, dict(torre=ent, chao=ent + 0.2, olhar=ent + 0.2, ang=ent + 0.4, rotulo60=ent + 0.6, reto=ent + 0.6), chao_med="")
    # 30 na hipotenusa (errado), depois no chão (certo)
    E.saida(c, t, a3, lambda: E.foco(c, t, a2, 0.4, lambda a: (grosso(c, O, T, ERRADO, a, 10), txt_lado(c, O, T, "30?", TG, 72, ERRADO, a))))
    if t >= a3:
        grosso(c, O, B, ADJ, 1.0, 12, ease_io(prog(t, a3, 0.5)))
        E.foco(c, t, a3 + 0.3, 0.4, lambda a: (txt_lado(c, O, B, "30 m", TG, 64, ADJ, a), centro(c, "adjacente", (TO[0] + TB[0]) / 2, 1045, 50, "i", ADJ, a)))
    if t >= b3:
        grosso(c, O, T, HIP, 1.0, 10, ease_io(prog(t, b3, 0.6)), dash=E.TRACO)
        E.foco(c, t, b3 + 0.4, 0.4, lambda a: txt_lado(c, O, T, "?", TG, 80, HIP, a))

    def doze():
        E.frase(c, t, a2, ps("o erro:", "i", 70) + [("30 m na hipotenusa", "g", 70, ERRADO)], X, 230, "center", 0.1)
        E.frase(c, t, b2, ps("usa o", "i", 62) + [("sen 60°", "g", 66, ERRADO)], X, 380, "center", 0.1)
        fcen(c, t, b2 + 0.6, "30 · f{r{3}}{2} = 15r{3}", X, 560, 96)
        fcen(c, t, c2, "≈ 25,5 m", X, 760, 110, ERRADO)
        E.foco(c, t, c2 + 0.5, 0.5, lambda a: E.selo(c, X + 300, 725, 50, False, a))
    E.saida(c, t, C["s13"] - 0.1, doze)
    if t < C["s13"] - 0.1:
        return
    E.frase(c, t, a3, ps("os 30 m estão", "i", 64) + [("no chão", "g", 70, ADJ)], X, 260, "center", 0.1)
    E.frase(c, t, a3 + 0.9, ps("encostados no ângulo:", "i", 60) + [("adjacente", "g", 64, ADJ)], X, 360, "center", 0.1)
    E.frase(c, t, b3, [("hipotenusa", "g", 70, HIP)] + ps("= o olhar", "i", 64), X, 540, "center", 0.1)
    E.frase(c, t, b3 + 0.8, ps("ninguém mediu", "i", 60, TINTA2), X, 630, "center", 0.1)
    E.foco(c, t, c3, 0.5, lambda a: E.caixa_pontilhada(c, X - 400, 750, 800, 200, a, COR, prog_=ep(t, c3, 0.6)))
    E.frase(c, t, c3 + 0.1, ps("antes da conta:", "i", 60), X, 830, "center", 0.1)
    E.frase(c, t, c3 + 0.6, [("dê nome aos 3 lados", "g", 68, COR)], X, 915, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    a5, b5, c5 = (C[f"s15.{k}"] for k in "abc")
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    U = 300   # px por unidade da metade do equilátero
    A, B = (230, 900), (230 + U, 900)
    T = (B[0], 900 - U * R3)
    G = ((A[0] + B[0] + T[0]) / 3, (A[1] + B[1] + T[1]) / 3)
    X = 1290

    def metade():
        E.triangulo(c, t, a4, A, B, T, vertices=None, preenche=0.12, escuro=True, retos=(1,))
        E.angulo(c, t, a4 + 0.5, A, B, T, None, r=90, cor=CLARO)
        E.foco(c, t, a4 + 0.7, 0.4, lambda a: E._meio(c, "60°", A[0] + 140, A[1] - 44, 48, "b", CLARO, a))
        E.angulo(c, t, a4 + 0.6, T, A, B, None, r=110, cor=CLARO)
        E.foco(c, t, a4 + 0.8, 0.4, lambda a: E._meio(c, "30°", T[0] + 80, T[1] + 10, 48, "b", CLARO, a))
        for P, Q, s, cor, tk in ((A, B, "1", OPO, b4), (B, T, "r{3}", ADJ_ESC, c4), (A, T, "2", CLARO, d4)):
            if t >= tk:
                grosso(c, P, Q, cor, 1.0, 12, ease_io(prog(t, tk, 0.5)))
            E.foco(c, t, a4 + 0.9, 0.4, lambda a, P=P, Q=Q, s=s: txt_lado(c, P, Q, s, G, 66, BR, a))

        def quatorze():
            E.frase(c, t, C["s14"] + 0.2, ps("o atalho do", "i", 66, CLARO) + [("30° e 60°", "g", 70, BR)], X, 200, "center", 0.1)
            E.frase(c, t, a4, ps("metade do equilátero", "i", 60, CLARO), X, 320, "center", 0.1)
            E.frase(c, t, b4, ps("frente ao 30°:", "i", 60, CLARO) + [("o menor", "g", 66, BR)], X, 500, "center", 0.1)
            E.frase(c, t, c4, ps("frente ao 60°:", "i", 60, CLARO) + [("menor × √3", "g", 66, BR)], X, 650, "center", 0.1)
            E.frase(c, t, d4, [("hipotenusa:", "i", 60, CLARO)] + [("dobro do menor", "g", 66, BR)], X, 800, "center", 0.1)
        E.saida(c, t, C["s15"] - 0.1, quatorze)
        if t >= C["s15"] - 0.1:
            # a torre na mesma forma, à direita
            k = 0.62
            A2, B2 = (1080, 860), (1080 + 400 * k, 860)
            T2 = (B2[0], 860 - 400 * k * R3)
            G2 = ((A2[0] + B2[0] + T2[0]) / 3, (A2[1] + B2[1] + T2[1]) / 3)
            E.triangulo(c, t, C["s15"], A2, B2, T2, vertices=None, preenche=0.12, escuro=True, retos=(1,))
            E.foco(c, t, C["s15"] + 0.6, 0.4, lambda a: E._meio(c, "60°", A2[0] + 110, A2[1] - 36, 44, "b", CLARO, a))
            E.angulo(c, t, a5 + 0.6, T2, A2, B2, None, r=80, cor=CLARO)
            E.foco(c, t, a5 + 0.8, 0.4, lambda a: E._meio(c, "30°", T2[0] + 70, T2[1] + 10, 44, "b", BR, a))
            fcen(c, t, a5, "180 − 90 − 60 = 30°", W / 2 + 330, 170, 70, BR)
            if t >= b5:
                grosso(c, A2, B2, OPO, 1.0, 12, ease_io(prog(t, b5, 0.5)))
            E.foco(c, t, b5 + 0.3, 0.4, lambda a: txt_lado(c, A2, B2, "30", G2, 60, BR, a))
            E.frase(c, t, b5 + 0.4, ps("= o menor", "i", 54, CLARO), 1180, 1000, "center", 0.1)
            if t >= c5:
                grosso(c, B2, T2, ADJ_ESC, 1.0, 12, ease_io(prog(t, c5, 0.5)))
            E.foco(c, t, c5 + 0.3, 0.4, lambda a: txt_lado(c, B2, T2, "30r{3}", G2, 60, BR, a))
            E.frase(c, t, c5 + 1.4, [("sem equação", "g", 66, BR)], 1650, 560, "center")
    E.saida(c, t, C["s16"] - 0.1, metade)
    if t < C["s16"] - 0.1:
        return
    # s16: semelhança — a metade pequena e a grande, mesma proporção
    for u, x0, tk, rot in ((130, 170, a6, ("1", "r{3}", "2")), (260, 480, a6 + 0.5, ("2", "2r{3}", "4"))):
        A3, B3 = (x0, 780), (x0 + u, 780)
        T3 = (B3[0], 780 - u * R3)
        G3 = ((A3[0] + B3[0] + T3[0]) / 3, (A3[1] + B3[1] + T3[1]) / 3)
        E.triangulo(c, t, tk, A3, B3, T3, vertices=None, preenche=0.12, escuro=True, retos=(1,))
        for (P, Q), s, cor in zip(((A3, B3), (B3, T3), (A3, T3)), rot, (OPO, ADJ_ESC, CLARO)):
            if t >= b6:
                grosso(c, P, Q, cor, 1.0, 10, ease_io(prog(t, b6, 0.5)))
            E.foco(c, t, tk + 0.6, 0.4, lambda a, P=P, Q=Q, s=s, G3=G3: txt_lado(c, P, Q, s, G3, 52, BR, a))
    E.frase(c, t, a6, ps("todo", "i", 64, CLARO) + [("30°, 60°, 90°", "g", 68, BR)], 1330, 240, "center", 0.1)
    E.frase(c, t, a6 + 0.8, ps("é semelhante à metade", "i", 60, CLARO), 1330, 340, "center", 0.1)
    fcen(c, t, b6, "1 : r{3} : 2", 1330, 500, 96, BR)
    E.frase(c, t, b6 + 0.6, ps("a mesma proporção", "i", 56, CLARO), 1330, 590, "center", 0.1)
    E.foco(c, t, c6, 0.5, lambda a: E.selo(c, 900, 790, 48, False, a))
    E.frase(c, t, c6, ps("37°?", "g", 70, BR) + ps("não compensa", "i", 64, CLARO), 980, 815, "left", 0.1)
    E.frase(c, t, d6, ps("use o valor que", "i", 64, CLARO) + [("a prova der", "g", 70, BR)], W / 2, 970, "center", 0.1)


# ---------------- o rio, visto de cima (700 px = 30 m) ----------------
QA, QC = (250, 820), (950, 820)
QT = (250, 820 - 700 / R3)
QG = ((QA[0] + QC[0] + QT[0]) / 3, (QA[1] + QC[1] + QT[1]) / 3)
AZUL = "#3D7FD9"


def rio(c, t, t0, k):
    """margens e água; k = instantes: arvore, voce, anda, ang, x"""
    a = ep(t, t0, 0.6)
    if a <= 0:
        return
    y1, y2 = QT[1] + 30, QA[1] - 24
    c.drawRect(skia.Rect.MakeLTRB(90, y1, 1080, y2), M.paint(AZUL, 0.16 * a))
    for yy in (y1, y2):
        M.line(c, 90, yy, 1080, yy, AZUL, a, 5)
    for i in range(5):  # ondinhas
        wx, wy = 420 + i * 130, lerp(y1, y2, 0.3 + 0.12 * (i % 3))
        c.drawArc(skia.Rect.MakeXYWH(wx, wy, 40, 22), 200, 140, False, M.paint(AZUL, 0.5 * a, stroke=3))
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, "rio", 960, y1 + 80, 52, "i", AZUL, a))
    if k.get("arvore") is not None:
        q = ease_back(prog(t, k["arvore"], 0.5))
        if q > 0:
            c.drawCircle(QT[0], QT[1] - 34, 42 * q, M.paint(CERTO, 0.85))
            c.drawCircle(*QT, 9 * q, M.paint(TINTA))
    if k.get("voce") is not None:
        q = ease_back(prog(t, k["voce"], 0.4))
        if q > 0:
            c.drawCircle(*QA, 11 * q, M.paint(TINTA))
            E.foco(c, t, k["voce"], 0.4, lambda a: E._meio(c, "você", QA[0], QA[1] + 70, 46, "i", TINTA, a))
            M.line(c, *QA, *QT, TINTA2, ep(t, k["voce"], 0.5), 4, dash=E.TRACO)
    if k.get("anda") is not None and t >= k["anda"]:
        p = ease_io(prog(t, k["anda"], 0.9))
        cor = ADJ if k.get("adj") is not None and t >= k["adj"] else TINTA
        grosso(c, QA, (lerp(QA[0], QC[0], p), QA[1]), cor, 1.0, 12 if cor == ADJ else 7)
        c.drawCircle(lerp(QA[0], QC[0], p), QA[1], 11, M.paint(TINTA))
        E.foco(c, t, k["anda"] + 0.7, 0.4, lambda a: E._meio(c, "30 m", (QA[0] + QC[0]) / 2, QA[1] + 70, 60, "b", cor, a))
    if k.get("ang") is not None and t >= k["ang"]:
        grosso(c, QC, QT, TINTA2, 1.0, 5, ease_io(prog(t, k["ang"], 0.7)), dash=E.TRACO)
        E.angulo(c, t, k["ang"] + 0.5, QC, QA, QT, None, r=130)
        E.foco(c, t, k["ang"] + 0.8, 0.4, lambda a: E._meio(c, "30°", QC[0] - 200, QC[1] - 40, 50, "b", COR, a))
    if k.get("reto") is not None:
        E.angulo(c, t, k["reto"], QA, QC, QT, r=56)
    if k.get("opo") is not None and t >= k["opo"]:
        grosso(c, QA, QT, OPO, 1.0, 12, ease_io(prog(t, k["opo"], 0.6)))
    if k.get("x") is not None:
        E.foco(c, t, k["x"], 0.4, lambda a: E._meio(c, k.get("x_txt", "x = ?"), QA[0] - 20 - 95, (QA[1] + QT[1]) / 2, 64, "g", OPO if k.get("opo") is not None and t >= k["opo"] else COR, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    X = 1450
    rio(c, t, a7, dict(arvore=b7, voce=b7 + 0.6, anda=c7, ang=d7, x=e7))
    E.frase(c, t, b7 - 0.2, ps("árvore", "i", 46, CERTO), QT[0] + 60, QT[1] - 40, "left", 0.1)

    def texto():
        E.frase(c, t, C["s17"] + 0.2, ps("hora de testar", "i", 70, COR), X, 190, "center", 0.12)
        E.frase(c, t, a7, ps("a", "i", 66) + [("largura do rio", "g", 70, COR)], X, 310, "center", 0.1)
        E.frase(c, t, a7 + 1.0, ps("sem atravessar", "i", 60, TINTA2), X, 400, "center", 0.1)
        E.frase(c, t, b7, ps("você,", "i", 60) + [("em frente à árvore", "g", 62)], X, 520, "center", 0.1)
        E.frase(c, t, c7, ps("anda", "i", 60) + [("30 m", "g", 66, COR)] + ps("pela margem", "i", 60), X, 640, "center", 0.1)
        E.frase(c, t, d7, ps("vê a árvore a", "i", 60) + [("30°", "g", 66, COR)], X, 760, "center", 0.1)
        E.frase(c, t, e7, ps("qual a", "i", 76) + [("largura?", "g", 80, COR)], X, 900, "center", 0.1)
    E.saida(c, t, C["s18.a"] - 0.2, texto)
    E.foco(c, t, e7 + 1.6, 0.5, lambda a: E.formula(c, "r{3} ≈ 1,7", 1080, 1000, 64, "g", TINTA2, a, "right"))
    E.relogio(c, t, C["s18.a"], 1500, 420, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")
    ent = C["s19"]
    rio(c, t, ent - 0.4, dict(arvore=ent - 0.4, voce=ent - 0.4, anda=ent - 0.4, ang=ent - 0.4, reto=a9, adj=b9, opo=c9, x=ent - 0.2,
                              x_txt="x"))
    E.foco(c, t, b9 + 0.3, 0.4, lambda a: E.escreve(c, "adjacente", 470, 1000, 52, "i", ADJ, a))
    E.foco(c, t, c9 + 0.3, 0.4, lambda a: E.escreve(c, "oposto", 290, (QA[1] + QT[1]) / 2 + 80, 50, "i", OPO, a))
    X = 1470

    def dezenove():
        E.frase(c, t, ent + 0.1, ps("vamos lá", "i", 70, COR), X, 220, "center", 0.1)
        lista(c, t, [(a9, ps("90°:", "i", 60) + [("em frente à árvore", "g", 56)]),
                     (b9, [("30 m", "g", 60, ADJ), ("→ adjacente", "b", 58, ADJ)]),
                     (c9, ps("largura", "i", 60) + [("→ oposto", "g", 60, OPO)])], 1100, 380, 140, 58)
        pilula(c, t, d9, "tangente", X, 860, 70)
    E.saida(c, t, C["s20"] - 0.1, dezenove)

    def vinte():
        fcen(c, t, a0, "tg 30° = f{r{3}}{3}", X, 230, 84)
        fcen(c, t, b0, "f{r{3}}{3} = f{x}{30}", X, 420, 96)
        fcen(c, t, c0, "x = f{30r{3}}{3}", X, 620, 96)
        fcen(c, t, d0, "x = 10r{3}", X, 790, 100, COR)
        fcen(c, t, e0, "10 × 1,7 = 17", X - 140, 960, 84)
        bola_txt(c, t, e0 + 1.4, "17 m", X + 270, 930, 95, 66)
    E.saida(c, t, C["s21"] - 0.1, vinte)
    if t < C["s21"] - 0.1:
        return
    E.frase(c, t, a1, ps("frente ao 30°:", "i", 60) + [("o menor", "g", 64, COR)], X, 200, "center", 0.1)
    fcen(c, t, b1, "17 < 30", X - 50, 320, 84, CERTO)
    E.foco(c, t, b1 + 0.6, 0.5, lambda a: E.selo(c, X + 180, 292, 40, True, a))
    E.frase(c, t, c1 - 0.6, ps("pelo atalho", "i", 60, COR), X, 460, "center", 0.1)
    fcen(c, t, c1, "30 = x · r{3}", X, 580, 90)
    fcen(c, t, d1, "x = f{30}{r{3}}", X, 760, 96)
    fcen(c, t, e1, "= 10r{3}", X, 950, 100, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s22.a", "desenhe o", "triângulo retângulo"), ("s22.b", "dê nome aos lados", "a partir do ângulo"),
                 ("s22.c", "use a razão que liga", "o que tem ao que quer"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 68) + [(l2, "g", 70, COR)], 320, y, "left", 0.1)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a3, b3, c3 = C["s23.a"], C["s23.b"], C["s23.c"]
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 84), XE, 220, passo=0.14)
    E.frase(c, t, a3, ps("a altura de um", "i", 80) + [("morro", "g", 86, COR)], XE, 360, passo=0.11)
    E.frase(c, t, b3, ps("visto a", "i", 72) + [("30° e 60°,", "g", 78, COR)] + ps("a 100 m", "i", 72), XE, 480, passo=0.1)
    E.frase(c, t, c3, ps("com um", "i", 72) + [("sistema", "g", 78, COR)], XE, 600, passo=0.1)
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s23.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1000, 785, p), ep(t, C["s23.d"] + 0.2, 0.4))
    E.frase(c, t, C["s23.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, torre=b_torre, rampa=b_rampa, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
