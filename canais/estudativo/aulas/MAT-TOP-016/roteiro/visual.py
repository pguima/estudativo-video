"""Visual — Estudativo · MAT-TOP-016: troncos de pirâmide e de cone.

Linguagem: o sólido na metade direita, as contas na esquerda. O corte é um plano paralelo à base (elipse ou quadrado tracejado
em âmbar); a ponta que sai sobe e se afasta, em cinza-índigo claro, e o tronco fica embaixo, na cor da matéria. Arestas
escondidas tracejadas, como nas aulas de Geometria Espacial. Números do volume em pílulas sobre cada parte: ponta em âmbar,
tronco em índigo. Erro em vermelho, certo em verde, atalho (fórmula do tronco) no palco escuro.
Peças locais: cone_px() (cone ou tronco de cone, com a tampa de cima), pir_px() (pirâmide ou tronco de pirâmide de base
quadrada em perspectiva), corte_cone(), corte_pir() e cena_cone() (o cone que se parte em ponta e tronco)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-016_troncos_de_piramide_e_cone.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("tronco", "metodo", "piramide", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PONTA = "#D98A00"
C_ESC = "#3CC7D3"
assert 81 / 27 == 3 and 81 - 3 == 78 and 6 * 6 * 9 / 3 == 108 and 108 * 8 / 27 == 32 and 4 * 4 * 6 / 3 == 32 and 108 - 32 == 76
assert math.sqrt(36 * 16) == 24 and 3 / 3 * (36 + 24 + 16) == 76 and 81 - 81 / 3 == 54
assert 640 / 64 == 10 and 640 - 10 == 630 and math.sqrt(25 * 9) == 15 and 6 / 3 * (25 + 15 + 9) == 98


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


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


INC = 0.30  # achatamento das elipses (vista de cima)


def _arco(c, cx, cy, rx, ry, a1, varre, cor, a, largura, dash=None):
    if a <= 0 or rx <= 0:
        return
    pt = M.paint(cor, a, stroke=largura, cap_round=True)
    if dash:
        pt.setPathEffect(skia.DashPathEffect.Make(dash, 0))
    c.drawArc(skia.Rect.MakeXYWH(cx - rx, cy - ry, 2 * rx, 2 * ry), a1, varre, False, pt)


def cone_px(c, cx, cy, R, r, h, a=1.0, cor=None, largura=6):
    """tronco de cone (r > 0) ou cone (r = 0): base de raio R em (cx, cy), tampa de raio r na altura h (px)"""
    if a <= 0:
        return
    cor = cor or COR
    yt = cy - h
    corpo = skia.Path()
    corpo.moveTo(cx - R, cy)
    corpo.arcTo(skia.Rect.MakeXYWH(cx - R, cy - R * INC, 2 * R, 2 * R * INC), 180, -180, False)
    corpo.lineTo(cx + r, yt)
    if r > 0:
        corpo.arcTo(skia.Rect.MakeXYWH(cx - r, yt - r * INC, 2 * r, 2 * r * INC), 0, -180, False)
    else:
        corpo.lineTo(cx, yt)
    corpo.close()
    c.drawPath(corpo, M.paint(E.mix(cor, "#FFFFFF", 0.78), a))
    if r > 0:
        c.drawOval(skia.Rect.MakeXYWH(cx - r, yt - r * INC, 2 * r, 2 * r * INC), M.paint(E.mix(cor, "#FFFFFF", 0.62), a))
    _arco(c, cx, cy, R, R * INC, 180, 180, TINTA, 0.55 * a, largura - 2, E.TRACO)
    _arco(c, cx, cy, R, R * INC, 0, 180, TINTA, a, largura)
    if r > 0:
        _arco(c, cx, yt, r, r * INC, 0, 360, TINTA, a, largura)
    M.line(c, cx - R, cy, cx - r, yt, TINTA, a, largura)
    M.line(c, cx + R, cy, cx + r, yt, TINTA, a, largura)


def corte_cone(c, cx, cy, R, H_, f, a=1.0):
    """plano de corte (elipse tracejada em âmbar) a uma fração f da altura, a partir da ponta"""
    r = R * f
    y = cy - H_ * (1 - f)
    _arco(c, cx, y, r * 1.5, r * 1.5 * INC, 0, 360, PONTA, a, 5, [14, 10])


def cena_cone(c, t, cx, cy, R, H_, f, t0, tc, ts, cor_t=None):
    """cone que entra em t0, ganha o corte em tc e se parte em ts: a ponta sobe e o tronco fica"""
    a = ep(t, t0, 0.6)
    if a <= 0:
        return
    s = ease_io(prog(t, ts, 0.8)) if ts is not None else 0
    r = R * f
    hp = H_ * f
    if s <= 0:
        cone_px(c, cx, cy, R, 0, H_, a)
    else:
        cone_px(c, cx, cy, R, r, H_ - hp, a, cor_t or COR)
        cone_px(c, cx, cy - (H_ - hp) - 130 * s, r, 0, hp, a, PONTA)
    if tc is not None and t >= tc and s < 1:
        corte_cone(c, cx, cy, R, H_, f, ep(t, tc, 0.4) * (1 - s))


def _proj(x, y, z, cx, cy, k):
    return cx + (x + 0.45 * z) * k, cy - (y + 0.30 * z) * k


def pir_px(c, cx, cy, k, L, l, h, a=1.0, cor=None, largura=6):
    """tronco de pirâmide (l > 0) ou pirâmide (l = 0) de base quadrada: lado L embaixo, l em cima, altura h (em unidades; k px)"""
    if a <= 0:
        return
    cor = cor or COR
    P = lambda x, y, z: _proj(x, y, z, cx, cy, k)
    B = [P(-L / 2, 0, -L / 2), P(L / 2, 0, -L / 2), P(L / 2, 0, L / 2), P(-L / 2, 0, L / 2)]  # frente-esq, frente-dir, trás-dir, trás-esq
    T = [P(-l / 2, h, -l / 2), P(l / 2, h, -l / 2), P(l / 2, h, l / 2), P(-l / 2, h, l / 2)]
    # faces visíveis: frente, direita e (no tronco) a tampa
    for face, f in (((B[0], B[1], T[1], T[0]), 0.80), ((B[1], B[2], T[2], T[1]), 0.70)):
        path = skia.Path(); path.addPoly(list(face), True)
        c.drawPath(path, M.paint(E.mix(cor, "#FFFFFF", f), a))
    if l > 0:
        path = skia.Path(); path.addPoly(T, True)
        c.drawPath(path, M.paint(E.mix(cor, "#FFFFFF", 0.62), a))
    oc = M.paint(TINTA, 0.55 * a, stroke=largura - 2, cap_round=True)
    oc.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    for p_, q_ in ((B[2], B[3]), (B[3], B[0]), (B[3], T[3])):
        c.drawLine(*p_, *q_, oc)
    for p_, q_ in ((B[0], B[1]), (B[1], B[2]), (B[0], T[0]), (B[1], T[1]), (B[2], T[2])):
        M.line(c, *p_, *q_, TINTA, a, largura)
    if l > 0:
        for i in range(4):
            M.line(c, *T[i], *T[(i + 1) % 4], TINTA, a, largura)
    return B, T


def corte_pir(c, cx, cy, k, L, h_corte, l, a=1.0):
    P = lambda x, y, z: _proj(x, y, z, cx, cy, k)
    m = l / 2 + 0.6
    pts = [P(-m, h_corte, -m), P(m, h_corte, -m), P(m, h_corte, m), P(-m, h_corte, m)]
    path = skia.Path(); path.addPoly(pts, True)
    pt = M.paint(PONTA, a, stroke=5)
    pt.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
    c.drawPath(path, pt)


def pilula_em(c, t, t0, s, x, y, size, fundo):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, x, y, size, "g", fundo=fundo, a=a))


# ---------------- gancho ----------------
CX, CY, CR, CH = 1400, 880, 300, 600   # o cone grande da aula


def b_gancho(c, t, C, b):
    def cena():
        cena_cone(c, t, CX, CY, CR, CH, 1 / 3, C["s01.a"] - 0.4, C["s01.b"], C["s01.c"] - 0.3)
        pilula_em(c, t, C["s01.a"], "V = 81", CX, CY + 130, 50, TINTA)
        if t >= C["s01.b"]:
            q = ep(t, C["s01.b"] + 0.3, 0.4) * (1 - ep(t, C["s01.c"] - 0.3, 0.3))
            if q > 0:
                M.line(c, CX + 260, CY - CH, CX + 260, CY - CH * 2 / 3, PONTA, q, 6)
                E.escreve(c, "1/3", CX + 280, CY - CH * 5 / 6 + 20, 48, "g", PONTA, q)
        pilula_em(c, t, C["s01.c"] + 0.3, "3", CX, CY - CH * 2 / 3 - 200, 56, PONTA)
        pilula_em(c, t, C["s01.d"], "78", CX, CY - 160, 60, COR)
        E.frase(c, t, C["s01.a"], [("cone:", "i", 80), ("81", "g", 96, COR)], XE, 300)
        E.frase(c, t, C["s01.b"], ps("corte a 1/3 da altura,", "i", 60), XE, 430, passo=0.1)
        E.frase(c, t, C["s01.b"] + 1.2, ps("contando da ponta", "i", 60), XE, 510, passo=0.1)
        E.frase(c, t, C["s01.c"] - 2.2, [("ponta:", "i", 70), ("27?", "g", 70, ERRADO)], XE, 660)
        if t >= C["s01.c"]:
            E.risco(c, XE + 230, 680, XE + 380, 600, t, C["s01.c"], largura=10)
        E.frase(c, t, C["s01.c"], [("só", "i", 76), ("3", "g", 86, PONTA)], XE + 450, 660)
        E.frase(c, t, C["s01.d"], [("tronco:", "i", 80), ("78", "g", 96, COR)], XE, 820)
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("volume", "g", 120)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.4, [("de", "i", 100), ("troncos", "g", 120, COR)], XE, 590)
        E.frase(c, t, C["s02.a"] + 2.4, ps("de cone e de pirâmide", "i", 70, TINTA2), XE, 710, passo=0.1)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("duas", "g", 80, COR, C["s03.a"]), ("coisas", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 190, "center")
    x, w = 200, 1520
    for k, y in (("s03.b", 280), ("s03.c", 610)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 290, p, prog_=p)
    k = C["s03.b"]
    a = ep(t, k + 0.3, 0.5)
    cone_px(c, 380, 520, 110, 0, 200, a)
    pir_px(c, 640, 520, 34, 5, 0, 6, a)
    E.frase(c, t, k, [("cone", "g", 60, COR), ("e", "i", 62), ("pirâmide", "g", 60, COR)], 900, 370)
    conta_em(c, t, k + 1.2, [("V = f{área da base · altura}{3}", TINTA)], 900, 500, 62)
    k = C["s03.c"]
    E.frase(c, t, k, [("semelhantes", "g", 64, COR)], 260, 700)
    conta_em(c, t, k + 1.2, [("medidas × k  →  volume × k^3", TINTA)], 260, 820, 66)
    E.frase(c, t, C["s04"] - 2.4, ps("faltou alguma? procure no canal", "i", 50, TINTA2), W / 2, 980, "center", passo=0.1)


# ---------------- o que é o tronco ----------------
def b_tronco(c, t, C, b):
    def s04():
        cena_cone(c, t, CX, CY, CR, CH, 0.45, C["s04"], C["s04.a"], C["s04.b"])
        pilula_em(c, t, C["s04.b"] + 0.4, "cone menor", CX + 330, CY - CH * 0.55 - 200, 42, PONTA)
        pilula_em(c, t, C["s04.c"], "tronco", CX + 380, CY - 150, 46, COR)
        if t >= C["s04.d"]:
            q = ep(t, C["s04.d"], 0.5)
            _arco(c, CX, CY, CR, CR * INC, 0, 360, CERTO, q, 9)
            r = CR * 0.45
            _arco(c, CX, CY - CH * 0.55, r, r * INC, 0, 360, CERTO, q, 9)
        E.frase(c, t, C["s04.a"], ps("corte paralelo à base", "i", 64), XE, 300, passo=0.1)
        E.frase(c, t, C["s04.c"], [("tronco", "g", 100, COR), ("de", "i", 90), ("cone", "g", 100, COR)], XE, 480)
        E.frase(c, t, C["s04.d"], [("2", "g", 70, CERTO), ("bases", "i", 70), ("redondas", "i", 70)], XE, 620)
        E.frase(c, t, C["s04.e"], ps("balde, copo descartável", "i", 60, TINTA2), XE, 760, passo=0.1)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    a = ep(t, C["s05"], 0.5)
    s = ease_io(prog(t, C["s05.a"] + 0.6, 0.8))
    k, cx, cy = 62, 1330, 900
    if s <= 0:
        pir_px(c, cx, cy, k, 6, 0, 9, a)
        if t >= C["s05.a"]:
            corte_pir(c, cx, cy, k, 6, 3, 4, ep(t, C["s05.a"], 0.4))
    else:
        pir_px(c, cx, cy, k, 6, 4, 3, a)
        pir_px(c, cx, cy - 3 * k - 120 * s, k, 4, 0, 6, a, PONTA)
    if t >= C["s05.b"]:
        q = ep(t, C["s05.b"], 0.5)
        P = lambda x, y, z: _proj(x, y, z, cx, cy, k)
        for L_, y_ in ((6, 0), (4, 3)):
            pts = [P(-L_ / 2, y_, -L_ / 2), P(L_ / 2, y_, -L_ / 2), P(L_ / 2, y_, L_ / 2), P(-L_ / 2, y_, L_ / 2)]
            path = skia.Path(); path.addPoly(pts, True)
            c.drawPath(path, M.paint(CERTO, q, stroke=8))
    E.frase(c, t, C["s05"], [("pirâmide:", "g", 80, COR), ("igual", "i", 86)], XE, 340)
    E.frase(c, t, C["s05.a"], [("tronco", "g", 90, COR), ("de", "i", 80), ("pirâmide", "g", 90, COR)], XE, 520)
    E.frase(c, t, C["s05.b"], ps("2 bases do mesmo formato", "i", 60), XE, 680, passo=0.1)


# ---------------- o método ----------------
def b_metodo(c, t, C, b):
    E.frase(c, t, C["s06"], [("volume", "i", 76), ("do", "i", 76), ("tronco", "g", 76, COR)], XE, 210)
    E.foco(c, t, C["s06.a"], 0.5, lambda a: E.pilula(c, "inteiro", XE + 140, 330, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s06.b"], 0.5, lambda a: (E.escreve(c, "−", XE + 300, 350, 80, "g", TINTA, a),
                                            E.pilula(c, "ponta", XE + 480, 330, 50, "g", fundo=PONTA, a=a)))
    cena_cone(c, t, CX, CY, CR, CH, 1 / 3, C["s06"], C["s07.a"], C["s07.e"] - 0.4)
    pilula_em(c, t, C["s06"] + 0.6, "81", CX - CR - 40, CY - 300, 50, TINTA)
    pilula_em(c, t, C["s07.e"] + 0.2, "3", CX, CY - CH * 2 / 3 - 200, 56, PONTA)
    pilula_em(c, t, C["s08.b"], "78", CX, CY - 160, 60, COR)
    if t >= C["s07.a"]:
        q = ep(t, C["s07.a"], 0.4) * (1 - ep(t, C["s07.e"] - 0.4, 0.3))
        M.line(c, CX + 330, CY - CH, CX + 330, CY - CH * 2 / 3, PONTA, q, 6)
        M.line(c, CX + 330, CY - CH * 2 / 3, CX + 330, CY, TINTA2, q, 4)
        E.escreve(c, "1/3", CX + 350, CY - CH * 5 / 6 + 20, 48, "g", PONTA, q)
    E.frase(c, t, C["s07.b"], ps("ponta semelhante ao cone", "i", 56, TINTA2), XE, 480, passo=0.1)
    conta_em(c, t, C["s07.c"], [("k = f{1}{3}", PONTA)], XE, 600, 76)
    conta_em(c, t, C["s07.d"], [("(f{1}{3})^3 = f{1}{27}", TINTA)], XE + 330, 600, 76)
    conta_em(c, t, C["s07.e"], [("81 ÷ 27 = ", TINTA), ("3", PONTA)], XE, 760, 76)
    conta_em(c, t, C["s08.a"], [("81 − 3 = ", TINTA)], XE, 900, 84)
    bola_txt(c, t, C["s08.b"], "78", XE + 390, 870, 80, 76)


# ---------------- a pirâmide ----------------
def b_piramide(c, t, C, b):
    k, cx, cy = 70, 1330, 920
    a = ep(t, C["s09.a"], 0.5)
    s = ease_io(prog(t, C["s10.d"] - 0.4, 0.8))
    if s <= 0:
        pir_px(c, cx, cy, k, 6, 0, 9, a)
        if t >= C["s10.a"]:
            corte_pir(c, cx, cy, k, 6, 3, 4, ep(t, C["s10.a"], 0.4))
    else:
        pir_px(c, cx, cy, k, 6, 4, 3, a)
        pir_px(c, cx, cy - 3 * k - 110 * s, k, 4, 0, 6, a, PONTA)
    P = lambda x, y, z: _proj(x, y, z, cx, cy, k)
    E.foco(c, t, C["s09.a"] + 0.4, 0.4, lambda q: E._cola(c, "6", *lerp_p(P(-3, 0, -3), P(3, 0, -3)), 0, 1, 14, 48, "g", COR, q))
    if t >= C["s09.a"] + 0.6 and s <= 0:
        q = ep(t, C["s09.a"] + 0.6, 0.4)
        M.line(c, *P(0, 0, 0), *P(0, 9, 0), TINTA2, q, 4, dash=E.TRACO)
        E.escreve(c, "9", P(0, 4.5, 0)[0] + 14, P(0, 4.5, 0)[1], 48, "g", COR, q)
    if C["s10.a"] <= t and s <= 0:
        q = ep(t, C["s10.a"], 0.4)
        M.line(c, cx + 4.2 * k, P(0, 9, 0)[1], cx + 4.2 * k, P(0, 3, 0)[1], PONTA, q, 6)
        E.escreve(c, "6", cx + 4.4 * k, P(0, 6, 0)[1] + 16, 48, "g", PONTA, q)
    pilula_em(c, t, C["s10.d"] + 0.3, "32", P(0, 7, 0)[0], P(0, 7, 0)[1] - 110, 52, PONTA)
    pilula_em(c, t, C["s10.e"], "76", P(0, 1.5, 0)[0] + 20, P(0, 1.5, 0)[1] + 10, 56, COR)

    def s09_10():
        conta_em(c, t, C["s09.a"], [("lado 6, altura 9", TINTA2)], XE, 250, 56)
        conta_em(c, t, C["s09.b"], [("V = f{36 · 9}{3} = ", TINTA)], XE, 380, 66)
        conta_em(c, t, C["s09.c"], [("108", COR)], XE + conta(None, [("V = f{36 · 9}{3} = ", TINTA)], 0, 0, 66, 0), 380, 66)
        conta_em(c, t, C["s10.b"], [("k = f{6}{9} = f{2}{3}", PONTA)], XE, 540, 66)
        conta_em(c, t, C["s10.c"], [("(f{2}{3})^3 = f{8}{27}", TINTA)], XE, 690, 66)
        conta_em(c, t, C["s10.d"], [("108 · f{8}{27} = ", TINTA), ("32", PONTA)], XE, 840, 66)
        conta_em(c, t, C["s10.e"], [("108 − 32 = ", TINTA), ("76", COR)], XE, 970, 66)
    E.saida(c, t, C["s11"] - 0.1, s09_10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11"], ps("confira sem o k", "i", 70), XE, 300)
    conta_em(c, t, C["s11.a"], [("lado ", TINTA2), ("4", PONTA), (", altura ", TINTA2), ("6", PONTA)], XE, 460, 66)
    conta_em(c, t, C["s11.b"], [("f{16 · 6}{3} = ", TINTA), ("32", PONTA)], XE, 640, 80)
    E.foco(c, t, C["s11.b"] + 1.6, 0.4, lambda a: E.pilula(c, "bateu", XE + 520, 610, 50, "g", fundo=CERTO, a=a))


def lerp_p(A, B, u=0.5):
    return lerp(A[0], B[0], u), lerp(A[1], B[1], u)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 220)
    cena_cone(c, t, CX, CY, CR, CH, 1 / 3, C["s12"], C["s12"] + 0.4, C["s13.c"] - 0.4)
    pilula_em(c, t, C["s13.c"], "1/27 do volume", CX, CY - CH * 2 / 3 - 200, 44, PONTA)

    def s12():
        E.frase(c, t, C["s12.a"], ps("1/3 da altura = 1/3 do volume?", "i", 60), XE, 360, passo=0.1)
        conta_em(c, t, C["s12.b"], [("81 ÷ 3 = 27", ERRADO)], XE, 520, 80)
        conta_em(c, t, C["s12.c"], [("tronco: 81 − 27 = 54", ERRADO)], XE, 660, 72)
        if t >= C["s12.c"] + 1.4:
            E.risco(c, XE - 10, 680, XE + 760, 600, t, C["s12.c"] + 1.4, largura=11)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], [("encolhe", "i", 70), ("nas", "i", 70), ("3", "g", 76, COR), ("direções", "i", 70)], XE, 360)
    conta_em(c, t, C["s13.b"], [("f{1}{3} · f{1}{3} · f{1}{3} = f{1}{27}", TINTA)], XE, 540, 84)
    conta_em(c, t, C["s13.c"], [("tronco: 81 − 3 = 78", CERTO)], XE, 740, 72)


# ---------------- atalho (palco escuro) ----------------
FT = "V = f{h}{3} · (B + r{B · b} + b)"


def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho: só o tronco", "i", 72, CLARO), W / 2, 170, "center", passo=0.1)
        # o tronco de pirâmide com B, b e h
        k, cx, cy = 72, 1380, 860
        pir_px(c, cx, cy, k, 6, 4, 3, ep(t, C["s14.a"], 0.5), E.CLARO)
        P = lambda x, y, z: _proj(x, y, z, cx, cy, k)
        pilula_em(c, t, C["s14.b"], "B", *P(0, -0.2, -3.6), 46, E.COR)
        pilula_em(c, t, C["s14.c"], "b", *P(0, 3.6, 0), 46, "#8A5800")
        if t >= C["s14.d"]:
            q = ep(t, C["s14.d"], 0.4)
            M.line(c, cx + 4.6 * k, P(0, 0, 0)[1], cx + 4.6 * k, P(0, 3, 0)[1], C_ESC, q, 6)
            E.escreve(c, "h", cx + 4.8 * k, P(0, 1.5, 0)[1] + 16, 52, "g", C_ESC, q)
        E.frase(c, t, C["s14.b"], [("B:", "g", 60, BR), ("base", "i", 62, CLARO), ("grande", "i", 62, CLARO)], XE, 330)
        E.frase(c, t, C["s14.c"], [("b:", "g", 60, BR), ("base", "i", 62, CLARO), ("pequena", "i", 62, CLARO)], XE, 430)
        E.frase(c, t, C["s14.d"], [("h:", "g", 60, C_ESC), ("altura", "i", 62, CLARO), ("do", "i", 62, CLARO), ("tronco", "i", 62, CLARO)], XE, 530)
        E.foco(c, t, C["s14.e"], 0.6, lambda a: E.formula(c, FT, XE, 780, 84, "g", BR, a))
        if t >= C["s14.f"]:
            q = ep(t, C["s14.f"], 0.4)
            w0 = E.formula(None, "V = f{h}{3} · (B + ", 0, 0, 84, a=0)
            wr = E.formula(None, "r{B · b}", 0, 0, 84, a=0)
            M.rrect(c, XE + w0 - 10, 680, wr + 20, 150, 20, C_ESC, 0.25 * q)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s16"]:
        E.foco(c, t, C["s15"], 0.5, lambda a: E.formula(c, FT, W / 2, 230, 80, "g", BR, a, "center"))
        conta_em(c, t, C["s15.a"], [("B = 36,  b = 16,  h = 9 − 6 = 3", CLARO)], W / 2, 400, 64, "center")
        conta_em(c, t, C["s15.b"], [("r{36 · 16} = 6 · 4 = 24", C_ESC)], W / 2, 560, 76, "center")
        conta_em(c, t, C["s15.c"], [("f{3}{3} · (36 + 24 + 16)", BR)], W / 2, 740, 80, "center")
        E.foco(c, t, C["s15.d"], 0.5, lambda a: E.pilula(c, "= 76, de novo", W / 2, 900, 64, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s16.a"], ps("é a mesma subtração, já feita", "i", 66, CLARO), W / 2, 300, "center", passo=0.1)
    E.frase(c, t, C["s16.a"] + 2.0, ps("sem a altura do sólido inteiro", "i", 66, CLARO), W / 2, 400, "center", passo=0.1)
    E.frase(c, t, C["s16.b"], [("não", "g", 72, ERRADO), ("compensa:", "i", 76, CLARO), ("deu", "i", 76, CLARO), ("o", "i", 76, CLARO), ("sólido", "i", 76, CLARO),
                               ("inteiro", "g", 72, BR)], W / 2, 640, "center", passo=0.12)
    E.frase(c, t, C["s16.c"], [("subtraia", "g", 76, BR), ("a", "i", 76, CLARO), ("ponta", "g", 76, PONTA)], W / 2, 790, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.frase(c, t, C["s17.a"], [("1)", "g", 64, COR), ("cone", "i", 66), ("de", "i", 66), ("640", "g", 66), ("mL", "i", 66)], XE, 340)
    E.frase(c, t, C["s17.a"] + 1.4, ps("corte a 1/4 da altura, da ponta", "i", 58), XE + 80, 430, passo=0.1)
    E.frase(c, t, C["s17.a"] + 3.4, [("tronco?", "g", 66, COR)], XE + 80, 520)
    E.frase(c, t, C["s17.b"], [("2)", "g", 64, COR), ("tronco", "i", 66), ("de", "i", 66), ("pirâmide", "i", 66)], XE, 680)
    E.frase(c, t, C["s17.b"] + 1.4, [("B = 25,", "g", 64), ("b = 9,", "g", 64), ("h = 6", "g", 64)], XE + 80, 780)
    E.frase(c, t, C["s17.b"] + 3.4, [("volume?", "g", 66, COR)], XE + 80, 870)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1440, cy=470, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s19():
        cena_cone(c, t, CX, CY, CR, CH, 1 / 4, C["s19"], C["s19"] + 0.4, C["s19.b"])
        pilula_em(c, t, C["s19.b"] + 0.4, "10 mL", CX, CY - CH * 3 / 4 - 190, 48, PONTA)
        pilula_em(c, t, C["s19.c"], "630 mL", CX, CY - 200, 56, COR)
        conta_em(c, t, C["s19.a"], [("k = f{1}{4}  →  (f{1}{4})^3 = f{1}{64}", TINTA)], XE, 330, 66)
        conta_em(c, t, C["s19.b"], [("640 ÷ 64 = ", TINTA), ("10", PONTA)], XE, 520, 76)
        conta_em(c, t, C["s19.c"], [("640 − 10 = ", TINTA)], XE, 700, 80)
        bola_txt(c, t, C["s19.c"] + 0.3, "630 mL", XE + 590, 670, 120, 52, CERTO)
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.formula_em(c, t, C["s20"], "V = f{6}{3} · (25 + r{25 · 9} + 9)", XE, 290, 84)
    conta_em(c, t, C["s20.a"], [("r{25 · 9} = 5 · 3 = 15", COR)], XE, 470, 76)
    conta_em(c, t, C["s20.b"], [("f{6}{3} = 2", TINTA)], XE, 620, 76)
    conta_em(c, t, C["s20.c"], [("2 · (25 + 15 + 9) = 2 · 49", TINTA)], XE, 780, 76)
    bola_txt(c, t, C["s20.d"], "98", 1500, 760, 120, 100, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s21.a", [("tronco", "g", 70, COR), ("=", "i", 72), ("inteiro", "i", 72), ("−", "g", 70), ("ponta", "g", 70, PONTA)]),
                 ("s21.b", [("a", "i", 72), ("ponta", "g", 70, PONTA), ("encolhe", "i", 72), ("com", "i", 72), ("k³", "g", 70, COR)]),
                 ("s21.c", [("sem", "i", 72), ("o", "i", 72), ("inteiro:", "i", 72), ("fórmula", "g", 70), ("do", "i", 72), ("tronco", "g", 70, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 340, y, passo=0.12)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s22.a"], [("Homotetia", "g", 150, COR)], XE, 460)
    E.frase(c, t, C["s22.a"] + 0.6, ps("ampliar a partir de um ponto", "i", 64, TINTA2), XE, 570, passo=0.1)
    E.frase(c, t, C["s22.b"], [("× 2", "g", 80, COR), ("no", "i", 70), ("lado,", "i", 70), ("× 4", "g", 80, COR), ("na", "i", 70), ("área", "i", 70)], XE, 690)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 300, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(620, 325, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, tronco=b_tronco, metodo=b_metodo, piramide=b_piramide, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
