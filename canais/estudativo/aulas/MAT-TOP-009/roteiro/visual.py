"""Visual — Estudativo · MAT-TOP-009: posição entre duas circunferências.
Mesma linguagem da MAT-TOP-007 (geometria analítica: eixo x em índigo, pontos em tinta, escala igual nos dois eixos).
Cores desta aula: a circunferência maior em tinta, a menor em índigo; a distância entre os centros em âmbar tracejado.
regua(): a régua das posições, com a marca da diferença e a da soma dos raios, e o marcador âmbar da distância.
Os casos são uma animação só: a menor anda em direção à maior, e a distância passa pelas marcas da régua.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-009_posicao_entre_duas_circunferencias.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("casos", "exemplo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMB = "#D98A00"
assert 3 + 2 == 5 and abs(2 - 3) == 1
assert math.hypot(4 - 1, 6 - 2) == 5 and 4 + 2 == 6 and 4 - 2 == 2 and 2 < 5 < 6
assert 1 < 5 + 2 and 1 < 5 - 2
assert math.hypot(3, 4) == 5 and 10 + 5 == 15 and 10 - 5 == 5


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, str(s), cx, cy + size * 0.36, size, "g", BR, a, "center")))


def txt_em(c, t, t0, s, x, y, size, cor=TINTA, est="g", align="left"):
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, s, x, y, size, est, cor, a, align))


def circ(c, cx, cy, r, cor, a=1.0, p=1.0, largura=7, centro_=True):
    if a <= 0 or p <= 0:
        return
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, 360 * p, False, M.paint(cor, a, stroke=largura, cap_round=True))
    if centro_:
        c.drawCircle(cx, cy, 9, M.paint(cor, a))


def circ_em(c, t, t0, cx, cy, r, cor, d=0.8, a=1.0):
    circ(c, cx, cy, r, cor, a * ep(t, t0, 0.2), ease_io(prog(t, t0, d)))


def raio(c, t, t0, cx, cy, r, ang, s, cor, size=50):
    p = ease_io(prog(t, t0, 0.5))
    if p <= 0:
        return
    x1, y1 = cx + r * math.cos(math.radians(ang)), cy - r * math.sin(math.radians(ang))
    M.line(c, cx, cy, lerp(cx, x1, p), lerp(cy, y1, p), cor, 1, 5)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, s, (cx + x1) / 2 - 26 * math.sin(math.radians(ang)), (cy + y1) / 2 - 20, size, "g", cor, a))


def regua(c, t, t0, x0, x1, y, vmax, dif, soma, d=None, rot=True, escuro=False, size=46, td=None):
    """régua das posições de 0 a vmax: marcas na diferença e na soma; d = distância (marcador âmbar)"""
    tinta = BR if escuro else TINTA
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    X = lambda v: x0 + (x1 - x0) * v / vmax
    M.line(c, x0, y, x0 + (x1 - x0) * ease_io(prog(t, t0, 0.6)), y, tinta, q, 6)
    for v, s in ((dif, "diferença"), (soma, "soma")):
        M.line(c, X(v), y - 30, X(v), y + 30, COR if not escuro else CLARO, q, 8)
        if rot:
            centro(c, s, X(v), y + 80, size, "b", COR if not escuro else CLARO, q)
    if d is not None and (td is None or t >= td):
        qd = ep(t, td, 0.4) if td is not None else q
        M.line(c, X(d), y - 50, X(d), y, AMB, qd, 6)
        c.drawCircle(X(d), y - 60, 16, M.paint(AMB, qd))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        k, cx, cy = 90, 620, 560
        circ_em(c, t, C["s01.a"], cx, cy, 3 * k, TINTA)
        raio(c, t, C["s01.a"] + 0.6, cx, cy, 3 * k, 120, "3", TINTA)
        circ_em(c, t, C["s01.b"], cx + 5 * k, cy, 2 * k, COR)
        raio(c, t, C["s01.b"] + 0.6, cx + 5 * k, cy, 2 * k, 60, "2", COR)
        if t >= C["s01.c"]:
            p = ease_io(prog(t, C["s01.c"], 0.6))
            M.line(c, cx, cy, cx + 5 * k * p, cy, AMB, 1, 6, dash=E.TRACO)
            E.foco(c, t, C["s01.c"] + 0.4, 0.4, lambda a: centro(c, "5", cx + 2.5 * k, cy + 70, 60, "g", AMB, a))
        E.foco(c, t, C["s01.d"], 0.4, lambda a: E.escreve(c, "3 + 2 = 5", 1420, 300, 90, "g", TINTA, a))
        if t >= C["s01.e"]:
            q = ep(t, C["s01.e"], 0.5)
            c.drawCircle(cx + 3 * k, cy, 18 + 10 * (1 - q), M.paint(CERTO, q))
        E.foco(c, t, C["s01.e"], 0.5, lambda a: E.pilula(c, "encostam num ponto", 1560, 900, 60, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 560, 270 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("duas", "g", 120), ("circunferências", "g", 110, COR)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.8, [("comparando", "i", 110)], XE, 630)
        E.frase(c, t, C["s02.a"] + 2.4, [("3", "g", 120, COR), ("números", "g", 120)], XE, 780)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1300, 545, 80, "g", BR, a),
                                                      E.escreve(c, "de prova", 1320, 630, 80, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 84), XE, 190)
    E.frase(c, t, C["s03.a"], [("3", "g", 110, COR), ("coisas", "i", 100)], XE + 640, 190)
    itens = (("s03.b", "centro e raio", "(x − 2)^2 + (y + 1)^2 = 9 → (2, −1), raio 3"), ("s03.c", "distância", "pelo triângulo retângulo"),
             ("s03.d", "módulo", "|−3| = 3"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 280 + i * 245
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, XE, y, 1580, 200, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "g", 60, COR)], XE + 50, y + 125)
        txt_em(c, t, C[k] + 0.5, l2, XE + 520, y + 125, 56, TINTA, "i" if "triângulo" in l2 else "g")


# ---------------- os casos ----------------
K, CX, CY = 80, 640, 500
RX0, RX1, RY = 300, 1600, 950


def d_casos(t, C):
    """distância entre os centros ao longo dos casos (a menor anda em direção à maior)"""
    pts = [(C["s04"], 6.5), (C["s06"], 5), (C["s07"], 3), (C["s08"], 1), (C["s08.c"], 0.4), (C["s08.d"], 0)]
    d = pts[0][1]
    for t0, v in pts[1:]:
        d = lerp(d, v, ease_io(prog(t, t0, 1.0)))
    return d


def b_casos(c, t, C, b):
    d = d_casos(t, C)
    circ_em(c, t, C["s04"], CX, CY, 3 * K, TINTA)
    circ_em(c, t, C["s04"] + 0.3, CX + d * K, CY, 2 * K, COR)
    if t >= C["s04.a"]:
        q = ep(t, C["s04.a"], 0.4)
        M.line(c, CX, CY, CX + d * K, CY, AMB, q, 6, dash=E.TRACO)
    regua(c, t, C["s04.b"], RX0, RX1, RY, 7, 1, 5, d, td=C["s04.a"])
    E.foco(c, t, C["s04.b"], 0.4, lambda a: E.escreve(c, "3 + 2 = 5", RX0 + (RX1 - RX0) * 5 / 7 - 80, RY - 90, 44, "g", COR, a))
    E.foco(c, t, C["s04.c"], 0.4, lambda a: E.escreve(c, "3 − 2 = 1", RX0 + (RX1 - RX0) * 1 / 7 - 80, RY - 90, 44, "g", COR, a))
    # nome do caso, no canto
    casos = (("s05", "externas"), ("s06", "tangentes externas"), ("s07", "secantes"), ("s08", "tangentes internas"),
             ("s08.c", "uma dentro da outra"), ("s08.d", "concêntricas"))
    atual = None
    for k, s in casos:
        if t >= C[k]:
            atual = (k, s)
    if atual and t < C["s09"]:
        k, s = atual
        prox = [C[kk] for kk, _ in casos if C[kk] > C[k]]
        fim = prox[0] if prox else C["s09"]
        E.saida(c, t, fim - 0.1, lambda: E.frase(c, t, C[k] + 0.6, [(s, "g", 70, COR)], 1180, 200))
    if C["s09"] <= t < C["s10"]:
        E.saida(c, t, C["s10"] - 0.1, lambda: (
            E.foco(c, t, C["s09.a"], 0.5, lambda a: E.pilula(c, "a diferença tem que dar positiva", 1450, 180, 50, "g", fundo=TINTA, a=a)),
            E.foco(c, t, C["s09.b"], 0.5, lambda a: E.escreve(c, "|2 − 3| = 1", 1260, 330, 90, "g", COR, a))))
    if t >= C["s10"]:
        E.frase(c, t, C["s10"], ps("pontos em comum", "i", 60), 1180, 120)
        for i, (k, n, s_) in enumerate((("s10.a", "2", "secantes"), ("s10.b", "1", "tangentes"), ("s10.c", "0", "as outras"))):
            y = 230 + i * 120
            E.foco(c, t, C[k], 0.4, lambda a, y=y, n=n, s_=s_: (E.bola(c, 1240, y - 22, 44, CERTO if n != "0" else ERRADO, a),
                                                              centro(c, n, 1240, y - 2, 52, "g", BR, a), E.escreve(c, s_, 1310, y, 58, "g", TINTA, a)))


# ---------------- exemplo ----------------
PE = E.Plano(1150, 150, 660, 720, -4, 7, -3, 9)


def b_exemplo(c, t, C, b):
    E.plano(c, t, C["s11"], *PE.caixa, PE.xmin, PE.xmax, PE.ymin, PE.ymax, size=34, passo=1, marcas_x=[-2, 2, 4, 6], marcas_y=[2, 4, 6, 8])
    k = PE.x(1) - PE.x(0)
    E.foco(c, t, C["s11.a"], 0.4, lambda a: E.formula(c, "(x − 1)^2 + (y − 2)^2 = 16", XE, 260, 60, "g", TINTA, a))
    E.foco(c, t, C["s11.b"], 0.4, lambda a: E.escreve(c, "centro (1, 2), raio 4", XE + 40, 350, 50, "i", TINTA, a))
    circ_em(c, t, C["s11.b"], *PE(1, 2), 4 * k, TINTA)
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.formula(c, "(x − 4)^2 + (y − 6)^2 = 4", XE, 470, 60, "g", COR, a))
    E.foco(c, t, C["s11.d"], 0.4, lambda a: E.escreve(c, "centro (4, 6), raio 2", XE + 40, 560, 50, "i", COR, a))
    circ_em(c, t, C["s11.d"], *PE(4, 6), 2 * k, COR)
    if t >= C["s12.a"]:
        p = ease_io(prog(t, C["s12.a"], 0.6))
        (x0, y0), (x1, y1) = PE(1, 2), PE(4, 6)
        M.line(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), AMB, 1, 6, dash=E.TRACO)
        M.line(c, x0, y0, x1, y0, "#0E9AA7", p * 0.8, 4)
        M.line(c, x1, y0, x1, y1, AMB, p * 0.8, 4)
    E.foco(c, t, C["s12.a"], 0.4, lambda a: E.escreve(c, "distância: 5", XE, 690, 64, "g", AMB, a))
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.escreve(c, "soma: 6", XE, 790, 60, "g", COR, a))
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.escreve(c, "diferença: 2", XE + 330, 790, 60, "g", COR, a))
    regua(c, t, C["s12.d"], XE, 1000, 930, 7, 2, 6, 5, rot=False, size=36)
    E.foco(c, t, C["s12.e"], 0.5, lambda a: E.pilula(c, "secantes", 1480, 960, 64, "g", fundo=CERTO, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("comparar só com a soma", "i", 66, ERRADO), XE, 300)
    k, cx, cy = 70, 1360, 560
    circ_em(c, t, C["s13.c"], cx, cy, 5 * k, TINTA)
    circ_em(c, t, C["s13.c"] + 0.3, cx + 1 * k, cy, 2 * k, COR)
    E.foco(c, t, C["s13.b"], 0.4, lambda a: E.escreve(c, "distância 1", XE, 430, 64, "g", AMB, a))
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.escreve(c, "raios 5 e 2", XE + 420, 430, 64, "g", TINTA, a))
    E.foco(c, t, C["s13.d"], 0.4, lambda a: E.escreve(c, "1 < 7: secantes?", XE, 600, 80, "g", ERRADO, a))
    if t >= C["s13.e"]:
        E.risco(c, XE - 10, 620, XE + 660, 540, t, C["s13.e"], largura=10)
    E.foco(c, t, C["s13.e"], 0.4, lambda a: E.escreve(c, "1 < 3 = 5 − 2", XE, 760, 80, "g", CERTO, a))
    E.foco(c, t, C["s13.f"], 0.5, lambda a: E.pilula(c, "uma dentro da outra", 460, 900, 60, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s14"], [("atalho:", "i", 76, CLARO), ("a", "i", 76, CLARO), ("régua", "g", 72, BR), ("das", "i", 76, CLARO),
                             ("duas", "i", 76, CLARO), ("marcas", "g", 72, BR)], W / 2, 180, "center")
    x0, x1, y = 260, 1660, 560
    X = lambda v: x0 + (x1 - x0) * v / 6
    if t >= C["s14.a"]:
        q = ep(t, C["s14.a"], 0.5)
        M.line(c, x0, y, x1, y, BR, q, 6)
    for v, s, k in ((2, "diferença", "s14.b"), (4, "soma", "s14.b")):
        E.foco(c, t, C[k] + (0.3 if v == 4 else 0), 0.4, lambda a, v=v, s=s: (M.line(c, X(v), y - 34, X(v), y + 34, CLARO, a, 9),
                                                                             centro(c, s, X(v), y - 60, 46, "b", CLARO, a)))
    zonas = (("s14.c", (0, 2), "uma dentro\nda outra"), ("s14.d", (2, 2), "tangentes\ninternas"), ("s14.e", (2, 4), "secantes"),
             ("s14.f", (4, 4), "tangentes\nexternas"), ("s14.g", (4, 6), "externas"))
    for k, (a0, a1), s in zonas:
        cx = (X(a0) + X(a1)) / 2
        def f(a, cx=cx, s=s, a0=a0, a1=a1):
            if a0 != a1:
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(X(a0) + 8, y - 16, X(a1) - 8, y + 16), 10, 10), M.paint(COR, 0.8 * a))
            else:
                c.drawCircle(cx, y, 20, M.paint(AMB, a))
                M.line(c, cx, y + 30, cx, y + 190, AMB, a, 3)
            for i, ln in enumerate(s.split("\n")):
                centro(c, ln, cx, (y + 110 if a0 != a1 else y + 250) + i * 56, 46, "g", BR, a)
        E.foco(c, t, C[k], 0.4, f)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: E.escreve(c, "as marcas = os momentos em que elas se encostam", 260, 960, 44, "i", CLARO, a))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.pilula(c, "a régua diz quantos pontos, não onde", 1460, 945, 44, "g", fundo=COR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    txt_em(c, t, C["s16.a"], "x^2 + y^2 = 100", XE, 420, 100)
    txt_em(c, t, C["s16.b"], "(x − 3)^2 + (y − 4)^2 = 25", XE, 600, 100, COR)
    E.frase(c, t, C["s16.c"], [("posição", "i", 90), ("entre", "i", 90), ("elas?", "g", 90, COR)], XE, 830)
    E.relogio(c, t, C["s17.a"], 1580, 300, 160)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    k, cx, cy = 34, 1420, 560
    circ_em(c, t, C["s18.a"], cx, cy, 10 * k, TINTA)
    circ_em(c, t, C["s18.b"], cx + 3 * k, cy - 4 * k, 5 * k, COR)
    E.foco(c, t, C["s18.a"], 0.4, lambda a: E.escreve(c, "centro (0, 0), raio 10", XE, 250, 60, "g", TINTA, a))
    E.foco(c, t, C["s18.b"], 0.4, lambda a: E.escreve(c, "centro (3, 4), raio 5", XE, 360, 60, "g", COR, a))
    if t >= C["s18.c"]:
        p = ease_io(prog(t, C["s18.c"], 0.6))
        M.line(c, cx, cy, lerp(cx, cx + 3 * k, p), lerp(cy, cy - 4 * k, p), AMB, 1, 6, dash=E.TRACO)
    E.foco(c, t, C["s18.c"], 0.4, lambda a: E.escreve(c, "distância: 5", XE, 490, 64, "g", AMB, a))
    E.foco(c, t, C["s19.a"], 0.4, lambda a: E.escreve(c, "soma: 15", XE, 640, 60, "g", TINTA, a))
    E.foco(c, t, C["s19.b"], 0.4, lambda a: E.escreve(c, "diferença: 5", XE + 330, 640, 60, "g", TINTA, a))
    E.foco(c, t, C["s19.c"], 0.4, lambda a: E.escreve(c, "distância = diferença", XE, 780, 70, "g", CERTO, a))
    E.foco(c, t, C["s19.d"], 0.5, lambda a: E.pilula(c, "tangentes internas", 470, 920, 66, "g", fundo=CERTO, a=a))
    if t >= C["s19.d"]:
        q = ep(t, C["s19.d"] + 0.3, 0.4)
        c.drawCircle(cx + 6 * k, cy - 8 * k, 16, M.paint(CERTO, q))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        for i, (k, s) in enumerate((("s20.a", "distância entre os centros"), ("s20.b", "soma e diferença dos raios"), ("s20.c", "veja onde cai na régua"))):
            y = 400 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 86)], 400, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s21.a"], [("Parábola:", "g", 130, COR)], XE, 470)
    E.frase(c, t, C["s21.b"], [("foco", "g", 120), ("e", "i", 110), ("diretriz", "g", 120, COR)], XE, 620)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, casos=b_casos, exemplo=b_exemplo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
