"""Visual — Estudativo · MAT-ARE-009: figuras compostas, somar e subtrair áreas (portão, malha quadriculada e piscina).
Linguagem da trilha (MAT-ARE-001): figuras em tinta preta com o miolo claro da cor da matéria; PERÍMETRO = a borda traçada grossa
na cor da matéria, andando em volta (traca()); a linha de corte, que fica DENTRO da figura, é tracejada em TINTA2 (e vermelha no
erro, quando alguém a põe no contorno). Na malha, a figura sombreada em COR, o retângulo em volta em tinta grossa e os cantos que
saem em âmbar, com os lados do ângulo reto contados em quadradinhos. Medidas na grotesca; resposta na esfera; atalho no palco.
Peças locais: traca() (contorno que anda, por PathMeasure), portao() (retângulo 4 × 3 + meio círculo de diâmetro 4), malha()
(quadradinhos de 1 cm, 6 × 4, com o quadrilátero de vértices (2,0), (6,3), (4,4), (0,1)), canto(), piscina() (10 × 6 + meios círculos).
Todo instante vem de C[...] (marcadores do roteiro); entre() reparte o tempo entre dois marcadores."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Áreas e Perímetros")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ARE-009_figuras_compostas_somar_e_subtrair_areas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "contorno", "malha", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
AGUA = "#9FD3F0"
assert 4 * 3 == 12 and 4 // 2 == 2 and 2 ** 2 == 4 and 4 / 2 == 2 and 12 + 2 * 3 == 18 and 2 * 2 == 4
assert 4 + 3 + 3 + 6 == 16 and 4 + 3 + 4 + 3 == 14 and 14 + 6 == 20 and 20 - 16 == 4
assert 6 * 4 == 24 and 2 * 1 / 2 == 1 and 4 * 3 / 2 == 6 and 1 + 6 + 1 + 6 == 14 and 24 - 14 == 10
assert 10 * 6 == 60 and 6 // 2 == 3 and 3 ** 2 == 9 and 9 * 3 == 27 and 60 + 27 == 87 and 10 + 10 == 20 and 2 * 3 * 3 == 18 and 20 + 18 == 38
# o quadrilátero da malha confere pela fórmula do cadarço
_Q = [(2, 0), (6, 3), (4, 4), (0, 1)]
assert abs(sum(_Q[i][0] * _Q[(i + 1) % 4][1] - _Q[(i + 1) % 4][0] * _Q[i][1] for i in range(4))) / 2 == 10


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


def traca(c, path, p, cor=None, larg=12, a=1.0, dash=None):
    """desenha o caminho até a fração p do comprimento: o contorno que anda"""
    if p <= 0 or a <= 0:
        return
    pm = skia.PathMeasure(path, False)
    L = pm.getLength()
    seg = skia.Path()
    pm.getSegment(0, L * min(p, 1.0), seg, True)
    pt_ = M.paint(cor or E.COR, a, stroke=larg, cap_round=True)
    pt_.setStrokeJoin(skia.Paint.kRound_Join)
    if dash:
        pt_.setPathEffect(skia.DashPathEffect.Make(dash, 0))
    c.drawPath(seg, pt_)


def tracejada(c, P, Q, cor=TINTA2, a=1.0, larg=5, p=1.0):
    if a > 0 and p > 0:
        M.line(c, *P, *Q, cor, a, larg, dash=E.TRACO, progress=p)


# ---------------- o portão: retângulo 4 × 3 + meio círculo de diâmetro 4 (100 px por metro) ----------------
U = 100
PX, PY = 300, 540           # canto de cima à esquerda do retângulo
PW, PH = 4 * U, 3 * U
PC = (PX + PW / 2, PY)      # centro do meio círculo
PR = 2 * U


def _semi(path, mover=True):
    ret = skia.Rect.MakeXYWH(PC[0] - PR, PC[1] - PR, 2 * PR, 2 * PR)
    path.arcTo(ret, 0, -180, mover)


def borda_portao():
    """a borda de fora: embaixo, lado direito, o arco, lado esquerdo"""
    p = skia.Path()
    p.moveTo(PX, PY + PH); p.lineTo(PX + PW, PY + PH); p.lineTo(PX + PW, PY)
    _semi(p, False)
    p.lineTo(PX, PY + PH)
    return p


def regiao_semi():
    p = skia.Path(); p.moveTo(PX + PW, PY); _semi(p, False); p.close()
    return p


def portao(c, t, t0, tl=None, tarco=None, corte=None, area_r=None, area_s=None, a=1.0):
    if t < t0 or a <= 0:
        return
    q = ease_io(prog(t, t0, 0.7))
    c.drawRect(skia.Rect.MakeXYWH(PX, PY, PW, PH), M.paint(E.COR, 0.1 * q * a))
    E._contorno(c, [(PX, PY), (PX, PY + PH), (PX + PW, PY + PH), (PX + PW, PY)], q, TINTA, 6, fecha=False)
    kc = ease_io(prog(t, corte, 0.5)) if corte is not None else 0.0
    if q > 0 and kc < 1:  # a linha entre o retângulo e o arco: inteira até virar corte
        M.line(c, PX, PY, PX + PW, PY, TINTA, (1 - kc) * a, 6, progress=q)
    if kc > 0:
        tracejada(c, (PX, PY), (PX + PW, PY), TINTA2, a, 6, kc)
    if area_r is not None:
        c.drawRect(skia.Rect.MakeXYWH(PX, PY, PW, PH), M.paint(E.COR, 0.25 * ep(t, area_r, 0.5) * a))
    ta = tarco if tarco is not None else t0
    if t >= ta:
        k = ease_io(prog(t, ta, 0.7))
        c.drawPath(regiao_semi(), M.paint(E.COR, 0.1 * k * a))
        ret = skia.Rect.MakeXYWH(PC[0] - PR, PC[1] - PR, 2 * PR, 2 * PR)
        c.drawArc(ret, 0, -180 * k, False, M.paint(TINTA, a, stroke=6, cap_round=True))
        if area_s is not None:
            c.drawPath(regiao_semi(), M.paint(E.COR, 0.3 * ep(t, area_s, 0.5) * a))
    if tl is not None:
        E.foco(c, t, tl, 0.4, lambda f: (centro(c, "4 m", PX + PW / 2, PY + PH + 76, 60, "b", TINTA, f * a),
                                         E.formula(c, "3 m", PX - 28, PY + PH / 2 + 22, 60, "b", TINTA, f * a, "right")))


# ---------------- a malha: quadradinhos de 1 cm, 6 × 4 ----------------
GX, GY, GS = 200, 300, 110


def gp(i, j):
    """ponto (i, j) da malha, j de baixo para cima"""
    return GX + i * GS, GY + (4 - j) * GS


CANTOS = (  # (vértices do triângulo do canto, lados do ângulo reto, área)
    ([(0, 0), (2, 0), (0, 1)], ("2", "1"), "1"),
    ([(6, 0), (6, 3), (2, 0)], ("4", "3"), "6"),
    ([(6, 4), (4, 4), (6, 3)], ("2", "1"), "1"),
    ([(0, 4), (0, 1), (4, 4)], ("4", "3"), "6"),
)


def malha(c, t, t0, tq=None, tret=None, a=1.0, tinta=TINTA, fio=None, escuro=False):
    if t < t0 or a <= 0:
        return
    k = ep(t, t0, 0.6) * a
    for i in range(7):
        M.line(c, GX + i * GS, GY, GX + i * GS, GY + 4 * GS, fio or TINTA2, 0.55 * k, 2)
    for j in range(5):
        M.line(c, GX, GY + j * GS, GX + 6 * GS, GY + j * GS, fio or TINTA2, 0.55 * k, 2)
    if tq is not None and t >= tq:
        q = ease_io(prog(t, tq, 0.8))
        path = skia.Path(); path.addPoly([gp(*v) for v in _Q], True)
        c.drawPath(path, M.paint(E.COR if not escuro else CLARO, 0.45 * ep(t, tq + 0.4, 0.5) * a))
        E._contorno(c, [gp(*v) for v in _Q], q, tinta, 6)
    if tret is not None and t >= tret:
        E._contorno(c, [gp(0, 0), gp(6, 0), gp(6, 4), gp(0, 4)], ease_io(prog(t, tret, 0.8)), tinta, 8)


def canto(c, t, t0, n, tl=None, tv=None, a=1.0, cor=AMBAR, size=54):
    """o triângulo do canto n, pintado; tl = lados contados; tv = a área dele escrita no meio"""
    if t < t0 or a <= 0:
        return
    vs, _, ar = CANTOS[n]
    pts = [gp(*v) for v in vs]
    k = ep(t, t0, 0.4) * a
    path = skia.Path(); path.addPoly(pts, True)
    c.drawPath(path, M.paint(cor, 0.4 * k))
    if tl is not None and t >= tl:
        q = ep(t, tl, 0.4) * a
        V, A_, B_ = pts  # V = o canto do ângulo reto; A_ e B_ nas pontas dos lados
        for P in (A_, B_):
            s_ = str(round(math.dist(V, P) / GS))  # o lado contado em quadradinhos
            M.line(c, *V, *P, cor, q, 10)
            mx, my = (V[0] + P[0]) / 2, (V[1] + P[1]) / 2
            dx, dy = (mx - (GX + 3 * GS)), (my - (GY + 2 * GS))
            n_ = math.hypot(dx, dy) or 1
            # o número por fora do retângulo
            if abs(V[1] - P[1]) < 1:   # lado deitado: número acima ou abaixo
                E.foco(c, t, tl, 0.4, lambda f, mx=mx, my=my, s_=s_: centro(c, s_, mx, my + (62 if my > GY + 2 * GS else -22), size, "g", cor, f * a))
            else:                      # lado em pé: número à esquerda ou à direita
                E.foco(c, t, tl, 0.4, lambda f, mx=mx, my=my, s_=s_: centro(c, s_, mx + (-40 if mx < GX + 3 * GS else 40), my + size * 0.36, size, "g", cor, f * a))
    if tv is not None:
        g = ((pts[0][0] * 2 + pts[1][0] + pts[2][0]) / 4, (pts[0][1] * 2 + pts[1][1] + pts[2][1]) / 4)
        E.foco(c, t, tv, 0.4, lambda f: centro(c, ar, g[0], g[1] + 22, 60, "g", TINTA, f * a))


# ---------------- a piscina: retângulo 10 × 6 + meio círculo em cada ponta (50 px por metro) ----------------
V = 50
QX, QY, QW, QH = 310, 400, 10 * V, 6 * V
QR = 3 * V
QE, QD = (QX, QY + QH / 2), (QX + QW, QY + QH / 2)   # centros dos meios círculos


def piscina(c, t, t0, tl=None, a=1.0, bordas=None):
    if t < t0 or a <= 0:
        return
    q = ease_io(prog(t, t0, 0.7))
    path = skia.Path()
    path.moveTo(QX, QY); path.lineTo(QX + QW, QY)
    path.arcTo(skia.Rect.MakeXYWH(QD[0] - QR, QD[1] - QR, 2 * QR, 2 * QR), -90, 180, False)
    path.lineTo(QX, QY + QH)
    path.arcTo(skia.Rect.MakeXYWH(QE[0] - QR, QE[1] - QR, 2 * QR, 2 * QR), 90, 180, False)
    path.close()
    c.drawPath(path, M.paint(AGUA, 0.85 * q * a))
    for k in range(5):  # reflexos
        y = QY + 50 + k * 50
        M.line(c, QX + 40 + (k % 2) * 80, y, QX + 200 + (k % 2) * 80, y, BR, 0.5 * q * a, 4)
    traca(c, path, q, TINTA, 6, a)
    tracejada(c, (QX, QY), (QX, QY + QH), TINTA2, 0.8 * q * a, 4)
    tracejada(c, (QX + QW, QY), (QX + QW, QY + QH), TINTA2, 0.8 * q * a, 4)
    if tl is not None:
        E.foco(c, t, tl, 0.4, lambda f: (centro(c, "10 m", QX + QW / 2, QY - 24, 56, "b", TINTA, f * a),
                                         E.formula(c, "6 m", QX + 24, QY + QH / 2 + 20, 52, "b", TINTA, f * a, "left")))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1, e1 = (C[f"s01.{k}"] for k in "abcde")
    X = 1440

    def um():
        portao(c, t, a1, tl=b1, tarco=c1)
        if t >= d1:  # a fita errada: os quatro lados e o arco
            p = skia.Path(); p.addRect(skia.Rect.MakeXYWH(PX, PY, PW, PH))
            traca(c, p, ease_io(prog(t, d1, 1.4)), ERRADO, 10, 0.9)
            pa = skia.Path(); pa.moveTo(PX + PW, PY); _semi(pa, False)
            traca(c, pa, ease_io(prog(t, d1 + 1.4, 0.7)), ERRADO, 10, 0.9)
        if t >= e1:
            k = ep(t, e1, 0.4)
            M.line(c, PX, PY, PX + PW, PY, ERRADO, k, 16)
            E.foco(c, t, e1 + 0.3, 0.4, lambda a: E.pilula(c, "não é borda!", PC[0], PY + 120, 52, "g", fundo=ERRADO, a=a))
        E.frase(c, t, a1, ps("portão:", "i", 64) + [("retângulo", "g", 70)], X, 260, "center", 0.12)
        E.frase(c, t, c1, ps("+", "g", 64, COR) + [("meio círculo", "g", 70, COR)], X, 360, "center", 0.12)
        E.frase(c, t, entre(C, "s01.c", "s01.d", 0.6), ps("fita de luz em volta:", "i", 60), X, 540, "center", 0.12)
        E.frase(c, t, d1, [("4 lados", "g", 66, ERRADO)] + ps("+", "g", 60, ERRADO) + [("o arco", "g", 66, ERRADO)], X, 650, "center", 0.12)
        E.frase(c, t, e1 + 0.6, ps("um lado", "i", 64) + [("nem fica na borda", "g", 64, ERRADO)], X, 820, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1520, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 300, passo=0.14)
        E.frase(c, t, entre(C, "s02.a", "s02.b", 0.25), [("área", "g", 110, COR)] + ps("e", "i", 90) + [("contorno", "g", 110, COR)], XE, 460, passo=0.14)
        E.frase(c, t, entre(C, "s02.a", "s02.b", 0.55), ps("de figuras montadas", "i", 84), XE, 600, passo=0.14)
        E.frase(c, t, entre(C, "s02.a", "s02.b", 0.75), ps("com pedaços", "i", 84), XE, 710, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1520, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de malha", 1520, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "áreas: retângulo, triângulo e", "círculo: A = πr^2"), ("s03.c", "a volta da circunferência:", "C = 2πr"),
             ("s03.d", "perímetro:", "a borda, a volta inteira"))
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


# ---------------- os dois caminhos ----------------
def b_ideia(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    E.frase(c, t, C["s04"] + 0.1, ps("figura composta:", "i", 72), W / 2, 200, "center", 0.12)
    E.frase(c, t, a4, ps("feita de", "i", 72) + [("pedaços conhecidos", "g", 76, COR)], W / 2, 310, "center", 0.12)
    E.foco(c, t, b4, 0.4, lambda a: E.pilula(c, "2 caminhos", W / 2, 430, 50, "g", fundo=TINTA, a=a))
    # 1) cortar e somar: retângulo + meio círculo separados
    if t >= c4:
        k = ep(t, c4, 0.5)
        sep = 40 * ease_io(prog(t, c4 + 0.4, 0.6))
        x, y, w, h = 330, 700, 260, 190
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(E.COR, 0.25 * k))
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, k, stroke=5))
        ret = skia.Rect.MakeXYWH(x, y - w / 2 - sep, w, w)
        path = skia.Path(); path.moveTo(x + w, y - sep); path.arcTo(ret, 0, -180, False); path.close()
        c.drawPath(path, M.paint(AMBAR, 0.35 * k))
        c.drawPath(path, M.paint(TINTA, k, stroke=5))
        E.foco(c, t, c4 + 0.6, 0.4, lambda a: centro(c, "+", x + w + 60, y + 20, 90, "g", COR, a))
        E.foco(c, t, c4 + 0.3, 0.4, lambda a: centro(c, "cortar e somar", x + w / 2 + 40, 980, 60, "g", COR, a))
    # 2) completar e tirar: a malha pequena com os cantos
    if t >= d4:
        k = ep(t, d4, 0.5)
        s, x0, y0 = 50, 1180, 640
        P = lambda i, j: (x0 + i * s, y0 + (4 - j) * s)
        for i in range(7):
            M.line(c, x0 + i * s, y0, x0 + i * s, y0 + 4 * s, TINTA2, 0.4 * k, 2)
        for j in range(5):
            M.line(c, x0, y0 + j * s, x0 + 6 * s, y0 + j * s, TINTA2, 0.4 * k, 2)
        c.drawRect(skia.Rect.MakeXYWH(x0, y0, 6 * s, 4 * s), M.paint(TINTA, k, stroke=5))
        for vs, _, _ in CANTOS:
            path = skia.Path(); path.addPoly([P(*v) for v in vs], True)
            c.drawPath(path, M.paint(AMBAR, 0.45 * ep(t, d4 + 0.5, 0.4)))
        path = skia.Path(); path.addPoly([P(*v) for v in _Q], True)
        c.drawPath(path, M.paint(E.COR, 0.35 * k))
        E.foco(c, t, d4 + 0.6, 0.4, lambda a: centro(c, "−", x0 + 6 * s + 60, y0 + 2 * s + 30, 90, "g", AMBAR, a))
        E.foco(c, t, d4 + 0.3, 0.4, lambda a: centro(c, "completar e tirar", x0 + 3 * s + 40, 980, 60, "g", COR, a))


# ---------------- portão: área ----------------
def b_portao(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    X = 1440
    t0 = C["s05"] - 1.2
    portao(c, t, t0, tl=t0, tarco=t0, corte=a5, area_r=b5, area_s=c5)
    if t >= c5:  # diâmetro 4 e raio 2
        k = ep(t, c5, 0.4)
        M.line(c, PX, PY - 14, PX + PW, PY - 14, AMBAR, k, 6)
        E.foco(c, t, c5 + 0.5, 0.4, lambda a: (M.line(c, *PC, PC[0] + PR * 0.6, PC[1] - PR * 0.8, TINTA, a, 5),
                                               E.formula(c, "r = 2", PC[0] + 40, PC[1] - 30, 46, "b", TINTA, a, "left")))
    E.foco(c, t, b5 + 0.3, 0.4, lambda a: centro(c, "12", PX + PW / 2, PY + PH / 2 + 30, 84, "g", COR, a))
    E.foco(c, t, e5 + 0.3, 0.4, lambda a: centro(c, "2π", PC[0] - 90, PC[1] - 50, 60, "g", COR, a))

    def um():
        E.frase(c, t, a5, ps("corte entre o", "i", 60) + [("retângulo e o arco", "g", 62)], X, 220, "center", 0.12)
        fcen(c, t, b5, "retângulo: 4 · 3 = 12 m²", X, 370, 68)
        E.frase(c, t, c5, ps("diâmetro 4", "i", 60) + [("→", "g", 60, TINTA2), ("raio 2", "g", 66, AMBAR)], X, 510, "center", 0.12)
        fcen(c, t, d5, "π · 2^2 = 4π", X, 650, 76)
        fcen(c, t, e5, "metade: 2π", X, 790, 76, COR)
    E.saida(c, t, C["s06"] - 0.1, um)
    if t >= C["s06"] - 0.1:
        fcen(c, t, a6, "A = 12 + 2π m²", X, 260, 84, COR)
        E.frase(c, t, b6, ps("com", "i", 60) + [("π = 3:", "g", 64)], X, 420, "center", 0.12)
        fcen(c, t, entre(C, "s06.b", "s06.c", 0.35), "2π = 2 · 3 = 6", X, 540, 76)
        fcen(c, t, entre(C, "s06.b", "s06.c", 0.7), "12 + 6", X, 680, 76)
        bola_txt(c, t, c6, "18 m²", X, 860, 110, 62, CERTO)


# ---------------- portão: contorno ----------------
def b_contorno(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    X = 1440
    t0 = C["s07"]
    portao(c, t, t0, tl=t0, tarco=t0, corte=t0)
    # a borda andando: embaixo (a), laterais (b), arco (c)
    if t >= a7:
        traca(c, _linha((PX, PY + PH), (PX + PW, PY + PH)), ease_io(prog(t, a7, 0.6)), E.COR, 14)
    if t >= b7:
        traca(c, _linha((PX + PW, PY + PH), (PX + PW, PY)), ease_io(prog(t, b7, 0.5)), E.COR, 14)
        traca(c, _linha((PX, PY + PH), (PX, PY)), ease_io(prog(t, b7 + 0.4, 0.5)), E.COR, 14)
    if t >= c7:
        pa = skia.Path(); pa.moveTo(PX + PW, PY); _semi(pa, False)
        traca(c, pa, ease_io(prog(t, c7, 0.8)), E.COR, 14)
    if t >= d7:  # a volta inteira, fantasma
        k = ep(t, d7, 0.5) * (1 - ep(t, C["s08"], 0.5))
        p = M.paint(TINTA2, k, stroke=4); p.setPathEffect(skia.DashPathEffect.Make([14, 12], 0))
        c.drawCircle(*PC, PR, p)
    if t >= b8:
        k = ep(t, b8, 0.4)
        M.line(c, PX + 30, PY, PX + PW - 30, PY, TINTA2, k, 10, dash=[14, 12])
        E.foco(c, t, c8, 0.4, lambda a: E.pilula(c, "dentro", PC[0], PY + 90, 50, "g", fundo=TINTA2, a=a))

    def sete():
        E.frase(c, t, C["s07"] + 0.2, ps("ande pela", "i", 66) + [("borda", "g", 72, COR)], X, 200, "center", 0.12)
        fcen(c, t, a7, "embaixo: 4", X, 330, 68)
        fcen(c, t, b7, "laterais: 3 e 3", X, 440, 68)
        E.frase(c, t, c7, ps("o arco:", "i", 62) + [("meia volta", "g", 68, COR)], X, 560, "center", 0.12)
        fcen(c, t, d7, "volta: 2 · π · 2 = 4π", X, 690, 70)
        fcen(c, t, e7, "meia: 2π = 6 m", X, 820, 76, COR)
    E.saida(c, t, C["s08"] - 0.1, sete)
    if t >= C["s08"] - 0.1:
        fcen(c, t, a8, "4 + 3 + 3 + 6", X, 250, 84)
        bola_txt(c, t, a8 + 0.8, "16 m", X, 450, 110, 70, CERTO)
        E.frase(c, t, b8, ps("a linha do corte", "i", 62) + [("não entra", "g", 70, TINTA2)], X, 700, "center", 0.12)
        E.frase(c, t, c8, ps("fica", "i", 62) + [("dentro do portão", "g", 66)], X, 820, "center", 0.12)


def _linha(P, Q):
    p = skia.Path(); p.moveTo(*P); p.lineTo(*Q)
    return p


# ---------------- malha ----------------
def b_malha(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    a11, b11, c11, d11, e11 = (C[f"s11.{k}"] for k in "abcde")
    a12, b12 = C["s12.a"], C["s12.b"]
    X = 1480
    malha(c, t, a9, tq=b9, tret=c9)
    if t >= a9 + 0.5:  # um quadradinho de 1 cm em destaque
        k = ep(t, a9 + 0.5, 0.4) * (1 - ep(t, b9, 0.4))
        c.drawRect(skia.Rect.MakeXYWH(GX + 5 * GS, GY, GS, GS), M.paint(AMBAR, 0.5 * k))
        centro(c, "1 cm", GX + 5.5 * GS, GY - 20, 46, "b", AMBAR, k)
    E.foco(c, t, c9 + 0.5, 0.4, lambda a: (centro(c, "6", GX + 3 * GS, GY + 4 * GS + 70, 60, "g", TINTA, a * (1 - ep(t, b11, 0.3))),
                                           E.formula(c, "4", GX - 30, GY + 2 * GS + 22, 60, "g", TINTA, a * (1 - ep(t, b11, 0.3)), "right")))
    # os cantos que saem
    if t >= c10:
        for n in range(4):
            tl = {0: b11, 1: c11, 2: d11, 3: d11 + 0.6}[n]
            canto(c, t, c10 + 0.25 * n, n, tl=tl, tv=tl + 0.6)

    def nove_dez():
        E.frase(c, t, a9, ps("malha de", "i", 62) + [("1 cm", "g", 68, AMBAR)], X, 220, "center", 0.12)
        E.frase(c, t, b9, ps("um", "i", 62) + [("quadrilátero torto", "g", 64, COR)], X, 340, "center", 0.12)
        E.frase(c, t, c9, ps("dentro de um", "i", 60) + [("6 × 4", "g", 66)], X, 460, "center", 0.12)
        E.frase(c, t, a10, ps("complete o", "i", 62) + [("retângulo", "g", 66)], X, 620, "center", 0.12)
        fcen(c, t, b10, "6 · 4 = 24 cm²", X, 740, 76)
        E.frase(c, t, c10, ps("fora:", "i", 62) + [("4 cantos", "g", 68, AMBAR)], X, 880, "center", 0.12)
    E.saida(c, t, C["s11"] - 0.1, nove_dez)
    if C["s11"] - 0.1 <= t:
        def onze():
            E.frase(c, t, a11, ps("os lados", "i", 60) + [("se contam", "g", 66, AMBAR)], X, 220, "center", 0.12)
            fcen(c, t, b11, "f{2 · 1}{2} = 1", X, 400, 76)
            fcen(c, t, c11, "f{4 · 3}{2} = 6", X, 590, 76)
            fcen(c, t, d11, "+ 1 + 6", X, 740, 76)
            fcen(c, t, e11, "1 + 6 + 1 + 6 = 14", X, 880, 72, AMBAR)
        E.saida(c, t, C["s12"] - 0.1, onze)
    if t >= C["s12"] - 0.1:
        fcen(c, t, a12, "24 − 14 = 10", X, 360, 92)
        bola_txt(c, t, b12, "10 cm²", X, 600, 120, 62, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a13, b13, c13, d13 = (C[f"s13.{k}"] for k in "abcd")
    X = 1440
    t0 = C["s13"]
    portao(c, t, t0, tl=t0, tarco=t0)
    if t >= a13:  # a fita errada, com a linha de dentro
        p = skia.Path(); p.addRect(skia.Rect.MakeXYWH(PX, PY, PW, PH))
        k_fora = 1 - ep(t, d13, 0.5)
        traca(c, p, ease_io(prog(t, a13, 1.2)), ERRADO, 10, 0.9 * k_fora)
        M.line(c, PX, PY, PX + PW, PY, ERRADO, ep(t, a13 + 0.6, 0.4) * k_fora, 16)
        pa = skia.Path(); pa.moveTo(PX + PW, PY); _semi(pa, False)
        traca(c, pa, ease_io(prog(t, c13, 0.7)), ERRADO, 10, 0.9 * k_fora)
    if t >= d13:
        traca(c, borda_portao(), ease_io(prog(t, d13 + 0.3, 1.4)), CERTO, 12)

    def um():
        E.frase(c, t, a13, ps("erro:", "i", 64, ERRADO) + [("a linha de dentro", "g", 64)], X, 220, "center", 0.12)
        fcen(c, t, b13, "4 + 3 + 4 + 3 = 14", X, 370, 74, ERRADO)
        fcen(c, t, c13, "14 + 6 = 20 m", X, 500, 80, ERRADO)
        if t >= c13 + 0.8:
            E.risco(c, X - 240, 520, X + 240, 450, t, c13 + 0.8, largura=10)
        E.foco(c, t, entre(C, "s13.c", "s13.d", 0.45), 0.5, lambda a: E.pilula(c, "sobram 4 m de fita", X, 630, 54, "g", fundo=ERRADO, a=a))
        E.frase(c, t, entre(C, "s13.c", "s13.d", 0.75), ps("na área, o corte", "i", 58) + [("não muda nada", "g", 60)], X, 760, "center", 0.12)
        E.frase(c, t, d13, ps("contorno:", "i", 60) + [("só o lado de fora", "g", 64, CERTO)], X, 880, "center", 0.12)
        fcen(c, t, d13 + 1.6, "16 m", X, 990, 72, CERTO)
    um()


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    a15, b15 = C["s15.a"], C["s15.b"]
    X = 1480

    def um():
        E.frase(c, t, C["s14"] + 0.2, [("atalho", "g", 90, CLARO)] + ps("para malha", "i", 76, BR), W / 2, 160, "center", 0.12)
        malha(c, t, C["s14"] + 0.3, tq=C["s14"] + 0.3, tret=a14, tinta=BR, fio=CLARO, escuro=True)
        for n in range(4):
            canto(c, t, a14 + 0.5 + 0.2 * n, n, tl=c14 if n in (0, 1) else None, cor=AMBAR)
        E.frase(c, t, a14, [("retângulo em volta", "g", 64, BR)], X, 330, "center", 0.12)
        E.frase(c, t, a14 + 0.8, [("− os cantos", "g", 72, AMBAR)], X, 430, "center", 0.12)
        E.frase(c, t, b14, ps("cantos com", "i", 60, CLARO) + [("ângulo reto", "g", 64, BR)], X, 590, "center", 0.12)
        E.frase(c, t, b14 + 1.0, ps("na própria malha", "i", 58, CLARO), X, 680, "center", 0.12)
        E.frase(c, t, c14, ps("conte os", "i", 60, CLARO) + [("quadradinhos", "g", 64, BR)], X, 830, "center", 0.12)
        E.frase(c, t, c14 + 0.8, ps("sem régua", "i", 60, CLARO), X, 920, "center", 0.12)
    E.saida(c, t, C["s15"] - 0.1, um)
    if t >= C["s15"] - 0.1:
        E.foco(c, t, a15, 0.5, lambda a: E.pilula(c, "não compensa", W / 2, 300, 70, "g", fundo=ERRADO, a=a))
        E.frase(c, t, a15 + 0.6, ps("figura de", "i", 66, CLARO) + [("quadradinhos inteiros", "g", 70, BR)] + ps("ou", "i", 66, CLARO)
                + [("retângulos", "g", 70, BR)], W / 2, 480, "center", 0.12)
        E.frase(c, t, b15, ps("aí,", "i", 76, CLARO) + [("conte ou some direto", "g", 84, BR)], W / 2, 700, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a16, b16, c16, d16, e16 = (C[f"s16.{k}"] for k in "abcde")
    X = 1500
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), X, 160, "center", 0.12)
    piscina(c, t, a16 - 0.3, tl=a16 + 0.2)
    linhas = [(a16, [("10 m × 6 m", "g", 60)]), (b16, ps("+", "g", 56, COR) + [("meio círculo", "g", 58, COR)] + ps("nas pontas", "i", 54)),
              (c16, ps("área da água", "i", 56) + [("= ?", "g", 62, COR)]), (d16, ps("borda de pedra", "i", 56) + [("= ?", "g", 62, COR)]),
              (e16, ps("use", "i", 56) + [("π = 3", "g", 60)])]
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, 740 + i * 78, "center", 0.12)
    E.relogio(c, t, C["s17.a"], X, 370, 150)


def b_resposta(c, t, C, b):
    a18, b18, c18, d18, e18 = (C[f"s18.{k}"] for k in "abcde")
    a19, b19, c19, d19, e19, f19 = (C[f"s19.{k}"] for k in "abcdef")
    X = 1480
    t0 = C["s18"] - 1.2
    piscina(c, t, t0, tl=t0)
    E.foco(c, t, a18 + 0.3, 0.4, lambda a: centro(c, "60", QX + QW / 2, QY + QH / 2 + 30, 84, "g", COR, a * (1 - ep(t, C["s19"], 0.4))))
    if t >= b18:  # raio 3 nas duas pontas
        k = ep(t, b18, 0.4) * (1 - ep(t, C["s19"], 0.4))
        for O, s_ in ((QE, -1), (QD, 1)):
            M.line(c, *O, O[0] + s_ * QR, O[1], AMBAR, k, 6)
        centro(c, "3", QD[0] + QR / 2, QD[1] - 16, 50, "g", AMBAR, k)
    if t >= c18:  # as duas metades voam e formam um círculo inteiro
        q = ease_io(prog(t, c18, 1.0))
        k = 1 - ep(t, C["s19"], 0.4)
        alvo = (QX + QW / 2, 900)
        for O, a1 in ((QE, 90), (QD, -90)):  # a metade da esquerda e a da direita
            cx, cy = lerp(O[0], alvo[0], q), lerp(O[1], alvo[1], q)
            ret = skia.Rect.MakeXYWH(cx - QR, cy - QR, 2 * QR, 2 * QR)
            path = skia.Path(); path.moveTo(cx, cy); path.arcTo(ret, a1, 180, False); path.close()
            c.drawPath(path, M.paint(AMBAR, 0.45 * k))
            c.drawPath(path, M.paint(TINTA, k, stroke=4))
        E.foco(c, t, d18 + 0.3, 0.4, lambda a: centro(c, "9π", alvo[0], alvo[1] + 24, 70, "g", TINTA, a * k))
    # a borda: os lados de 6 ficam dentro (b), os compridos (c) e os arcos (d)
    if t >= b19:
        k = ep(t, b19, 0.4)
        for x_ in (QX, QX + QW):
            M.line(c, x_, QY, x_, QY + QH, ERRADO, k, 8, dash=[14, 12])
    if t >= c19:
        traca(c, _linha((QX, QY), (QX + QW, QY)), ease_io(prog(t, c19, 0.6)), E.COR, 14)
        traca(c, _linha((QX, QY + QH), (QX + QW, QY + QH)), ease_io(prog(t, c19 + 0.3, 0.6)), E.COR, 14)
    if t >= d19:
        for O, a0 in ((QD, -90), (QE, 90)):
            p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(O[0] - QR, O[1] - QR, 2 * QR, 2 * QR), a0, 180)
            traca(c, p, ease_io(prog(t, d19, 0.8)), AMBAR, 14)

    def um():
        fcen(c, t, a18, "10 · 6 = 60", X, 220, 76)
        E.frase(c, t, b18, ps("diâmetro 6", "i", 60) + [("→", "g", 60, TINTA2), ("raio 3", "g", 66, AMBAR)], X, 360, "center", 0.12)
        E.frase(c, t, c18, ps("2 metades =", "i", 60) + [("1 círculo", "g", 66, AMBAR)], X, 500, "center", 0.12)
        fcen(c, t, d18, "π · 3^2 = 9π", X, 650, 76)
        fcen(c, t, e18, "9 · 3 = 27", X, 790, 76, AMBAR)
    E.saida(c, t, C["s19"] - 0.1, um)
    if t >= C["s19"] - 0.1:
        fcen(c, t, a19, "60 + 27 = 87 m²", X, 200, 74, CERTO)
        E.frase(c, t, b19, ps("lados de 6:", "i", 58) + [("não entram", "g", 62, ERRADO)], X, 330, "center", 0.12)
        fcen(c, t, c19, "10 + 10 = 20", X, 460, 70, COR)
        E.frase(c, t, d19, ps("arcos:", "i", 58) + [("1 volta inteira", "g", 62, AMBAR)], X, 590, "center", 0.12)
        fcen(c, t, e19, "2 · 3 · 3 = 18", X, 720, 70, AMBAR)
        bola_txt(c, t, f19, "38 m", X, 900, 110, 70, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", "corte em pedaços", "e some"), ("s20.b", "ou complete", "e tire o que sobra"), ("s20.c", "no contorno,", "só a borda de fora"))
        for i, (k, it, g) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(it, "i", 76), (g, "g", 76, COR)], 400, y, passo=0.25)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a21, b21, c21, d21 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
    E.frase(c, t, C["s21"] + 0.1, ps("próxima aula:", "i", 72), XE, 220, passo=0.1)
    E.frase(c, t, C["s21"] + 0.8, [("ampliar figuras", "g", 100, COR)], XE, 350)
    y0 = 790
    E.foco(c, t, a21, 0.5, lambda a: (c.drawRect(skia.Rect.MakeXYWH(220, y0 - 250, 250, 250), M.paint(E.COR, 0.2 * a)),
                                      c.drawRect(skia.Rect.MakeXYWH(220, y0 - 250, 250, 250), M.paint(TINTA, a, stroke=5))))
    E.foco(c, t, a21 + 0.4, 0.5, lambda a: (c.drawRect(skia.Rect.MakeXYWH(560, y0 - 300, 300, 300), M.paint(E.COR, 0.35 * a)),
                                            c.drawRect(skia.Rect.MakeXYWH(560, y0 - 300, 300, 300), M.paint(TINTA, a, stroke=5)),
                                            centro(c, "lados + 20%", 710, y0 + 62, 48, "g", TINTA, a)))
    E.foco(c, t, b21, 0.5, lambda a: E.pilula(c, "área + 44%", 1100, y0 - 150, 64, "g", fundo=AMBAR, a=a))
    E.foco(c, t, c21, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1540, 520, 76, estilo="g", a=a))
    p = ease_io(prog(t, c21 + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1660, p), lerp(800, 545, p), ep(t, c21 + 0.2, 0.4))
    E.frase(c, t, d21, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 1010, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, portao=b_portao, contorno=b_contorno, malha=b_malha,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
