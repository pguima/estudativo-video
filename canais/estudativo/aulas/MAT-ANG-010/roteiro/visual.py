"""Visual — Estudativo · MAT-ANG-010: Teorema de Tales no feixe de paralelas (3 e 6 numa transversal, 4 e x na outra: x = 8).
Linguagem da geometria plana (MAT-ANG-001 a 020): retas e lados em tinta; o pedaço da vez em cor forte por cima da reta;
pedaços que se correspondem têm a mesma cor (o de cima em COR, índigo; o de baixo em AMBAR); medidas na grotesca;
lados iguais com tracinhos (E.marcas_iguais); erro em vermelho, certo em verde; resposta na esfera; atalho no palco escuro.
O feixe de três paralelas com duas transversais é montado aqui (E.paralelas só faz duas paralelas e uma transversal).
As paralelas ficam em distâncias na razão certa (1 : 2 no feixe, 2 : 3 no mapa da questão) e as duas transversais têm
inclinações escolhidas para que 3 : 4 também valha no desenho: a figura não mente.
Peças locais: feixe() (três paralelas, duas transversais, setinhas de paralela), mapa() (as ruas e avenidas), pedaco(),
rot() (medida do pedaço, por fora da transversal), cota() (o trecho inteiro), frac2() (fração com o de cima e o de baixo em
cores diferentes), cruz() (como na MAT-RAZ-007), regua() (a régua do caderno), seta_curva() (o fator do atalho), vista().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-010_teorema_de_tales_feixe_de_paralelas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("feixe", "regra", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
assert 3 * 8 == 6 * 4 and 24 // 3 == 8 and 6 == 2 * 3 and 8 == 2 * 4
assert 3 * 8 == 4 * 6 and 3 + 6 == 9 and 4 + 8 == 12 and 3 * 12 == 9 * 4
assert 6 * 2 == 3 * 4 and 4 * 15 == 6 * 10 and 60 // 4 == 15
assert 60 + 90 == 150 and 60 * 200 == 12000 and 12000 // 150 == 80 and 200 - 80 == 120
assert 80 // 40 == 2 and 120 // 40 == 3 and 60 // 30 == 2 and 90 // 30 == 3 and 60 * 120 == 90 * 80


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


def meio(P, Q):
    return (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2


# geometria do feixe (coordenadas da figura, antes de vista())
YS = (250, 430, 790)          # paralelas: distâncias 180 e 360 (1 : 2, como 3 e 6)
YQ = (250, 466, 790)          # mapa da questão: 216 e 324 (2 : 3, como 60 e 90)
KL = -0.15                    # inclinação da transversal da esquerda (dx por dy)
KR = math.sqrt((4 / 3) ** 2 * (1 + KL ** 2) - 1)   # a da direita: cada pedaço dela é 4/3 do da esquerda (3 → 4)
XL0, XR0 = 470, 660
X0P, X1P = 140, 1260
VK, VOX, VOY = 0.86, 10, 40   # a figura encolhe um pouco para deixar a coluna da direita livre
XT = 1520                     # centro da coluna de texto


def pl(y):
    return XL0 + (y - YS[0]) * KL, y


def pr(y):
    return XR0 + (y - YS[0]) * KR, y


def tela(P):
    """ponto da figura em pixels da tela"""
    return VOX + VK * P[0], VOY + VK * P[1]


def vista(c, fn, k=VK, ox=VOX, oy=VOY):
    c.save(); c.translate(ox, oy); c.scale(k, k)
    fn()
    c.restore()


def seta_par(c, x, y, a=1.0, cor=TINTA):
    if a > 0:
        M.line(c, x - 14, y - 16, x + 6, y, cor, a, 5)
        M.line(c, x - 14, y + 16, x + 6, y, cor, a, 5)


def feixe(c, t, t0, ys=YS, tl=None, tr=None, tinta=TINTA, a=1.0, setas=True):
    """três paralelas (em t0) e as duas transversais (esquerda em tl, direita em tr)"""
    if a <= 0 or t < t0:
        return
    tl = t0 + 0.5 if tl is None else tl
    tr = tl + 0.3 if tr is None else tr
    for i, y in enumerate(ys):
        M.line(c, X0P, y, X1P, y, tinta, a, 6, progress=ease_io(prog(t, t0 + 0.12 * i, 0.7)))
        if setas:
            seta_par(c, 230, y, ep(t, t0 + 0.7, 0.4) * a, tinta)
    y0, y1 = ys[0] - 80, ys[-1] + 80
    if t >= tl:
        M.line(c, *pl(y0), *pl(y1), tinta, a, 6, progress=ease_io(prog(t, tl, 0.7)))
    if t >= tr:
        M.line(c, *pr(y0), *pr(y1), tinta, a, 6, progress=ease_io(prog(t, tr, 0.7)))


def mapa(c, t, t0, ys=YS, a=1.0, ruas=True):
    """o feixe como mapa: quadro claro, ruas (paralelas) e avenidas (transversais) largas"""
    if a <= 0 or t < t0:
        return
    k = ep(t, t0, 0.5) * a
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.16 * k))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(98, 152, 1220, 800), 24, 24), s)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(90, 140, 1220, 800), 24, 24), M.paint("#FBFAF6", k))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(90, 140, 1220, 800), 24, 24), M.paint(CINZA, k, stroke=3))
    for i, y in enumerate(ys):
        p = ease_io(prog(t, t0 + 0.2 + 0.12 * i, 0.7))
        M.line(c, 90, y, lerp(90, 1310, p), y, "#D6D2C6", k, 36)
        M.line(c, 100, y, lerp(100, 1300, p), y, BR, k, 3, dash=[18, 14])
    for j, f in enumerate((pl, pr)):
        p = ease_io(prog(t, t0 + 0.6 + 0.2 * j, 0.7))
        A, B = f(150), f(930)
        M.line(c, *A, lerp(A[0], B[0], p), lerp(A[1], B[1], p), "#C9C4B6", k, 44)
        M.line(c, *A, lerp(A[0], B[0], p), lerp(A[1], B[1], p), BR, k, 3, dash=[18, 14])
    q = ep(t, t0 + 1.0, 0.4) * a
    for y in ys:
        E.escreve(c, "rua", 118, y - 28, 40, "i", TINTA2, q if ruas else 0)
    E.escreve(c, "avenida", 335, 912, 42, "i", TINTA2, q)
    w = E.larg("avenida", "i", 42)
    E.escreve(c, "avenida", 1175 - w, 912, 42, "i", TINTA2, q)


def pedaco(c, t, t0, P, Q, cor=None, a=1.0, larg=14, d=0.5):
    """o pedaço da vez: traço grosso colorido por cima da reta, crescendo de P até Q"""
    if a <= 0 or t < t0:
        return
    M.line(c, *P, *Q, cor or E.COR, a, larg, progress=ease_io(prog(t, t0, d)))


def rot(c, t, t0, P, Q, s, lado, cor=None, size=60, gap=34, d=0.4, onde=0.5):
    """medida do pedaço PQ, por fora da transversal (lado = 1 ou −1); onde = ponto do pedaço (0 a 1)"""
    if t < t0:
        return
    ux, uy = E._uni(*P, *Q)
    M_ = (lerp(P[0], Q[0], onde), lerp(P[1], Q[1], onde))
    E.foco(c, t, t0, d, lambda a: E._cola(c, s, *M_, uy * lado, -ux * lado, gap, size, "g", cor or COR, a))


def rot_troca(c, t, t0, t1, P, Q, s0, s1, lado, cor0, cor1, size=60, gap=34, onde=0.5):
    """a medida s0 some em t1 e s1 entra no lugar (x vira 8)"""
    E.saida(c, t, t1, lambda: rot(c, t, t0, P, Q, s0, lado, cor0, size, gap, onde=onde))
    rot(c, t, t1, P, Q, s1, lado, cor1, size, gap, onde=onde)


def cota(c, t, t0, P, Q, s, lado, cor=TINTA2, off=120, size=60, a=1.0, onde=0.5):
    """o trecho inteiro: linha afastada da transversal, com tracinhos nas pontas e a medida"""
    if t < t0 or a <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy * lado, -ux * lado
    A = (P[0] + nx * off, P[1] + ny * off)
    B = (Q[0] + nx * off, Q[1] + ny * off)
    q = ease_io(prog(t, t0, 0.6))
    M.line(c, *A, lerp(A[0], B[0], q), lerp(A[1], B[1], q), cor, a, 5)
    k = ep(t, t0, 0.3) * a
    for V in (A, B):
        M.line(c, V[0] - nx * 18, V[1] - ny * 18, V[0] + nx * 18, V[1] + ny * 18, cor, k, 5)
    E.foco(c, t, t0 + 0.4, 0.4, lambda f: E._cola(c, s, lerp(A[0], B[0], onde), lerp(A[1], B[1], onde), nx, ny, 16, size, "g", cor, f * a))


def frac2(c, n, d, cx, cy, size, cn=TINTA, cd=TINTA, a=1.0, barra=TINTA):
    """fração empilhada com o de cima e o de baixo em cores próprias (como E.fracao)"""
    if a <= 0:
        return
    n, d = str(n), str(d)
    lw = max(E.larg(n, "g", size), E.larg(d, "g", size)) + size * 0.2
    E.escreve(c, n, cx - E.larg(n, "g", size) / 2, cy - size * 0.2, size, "g", cn, a)
    E.escreve(c, d, cx - E.larg(d, "g", size) / 2, cy + size * 0.9, size, "g", cd, a)
    b = size * 0.085
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - lw / 2, cy - b / 2 + size * 0.03, lw, b), b / 2, b / 2), M.paint(barra, a))


def prop(c, t, t0, n1, d1, n2, d2, cx, cy, size=110, cores=(COR, AMBAR, COR, AMBAR), t1=None, dx=170, barra=TINTA, igual=TINTA):
    """proporção n1/d1 = n2/d2: a primeira fração entra em t0, o = e a segunda em t1"""
    t1 = t0 + 0.6 if t1 is None else t1
    E.foco(c, t, t0, 0.5, lambda a: frac2(c, n1, d1, cx - dx, cy, size, cores[0], cores[1], a, barra))
    E.foco(c, t, t1, 0.5, lambda a: (centro(c, "=", cx, cy + size * 0.36, size, "g", igual, a),
                                     frac2(c, n2, d2, cx + dx, cy, size, cores[2], cores[3], a, barra)))


def cruz(c, t, t0, t1, cx, cy, size=110, dx=170, c1=None, c2=AMBAR, fundo=None, wa=50, wb=60):
    """produto cruzado: a diagonal do de cima à esquerda com o de baixo à direita em t0, a outra em t1"""
    xa, xb = cx - dx, cx + dx
    for tt, (P, Q), cor in ((t0, ((xa + wa, cy - size * 0.7), (xb - wb, cy + size * 0.95)), c1 or E.COR),
                            (t1, ((xa + wa, cy + size * 0.95), (xb - wb, cy - size * 0.7)), c2)):
        p = ease_io(prog(t, tt, 0.6))
        if p > 0:  # a diagonal pula o "=" do meio
            for u0, u1 in ((0.0, 0.36), (0.64, 1.0)):
                if p > u0:
                    u = min(p, u1)
                    M.line(c, lerp(P[0], Q[0], u0), lerp(P[1], Q[1], u0), lerp(P[0], Q[0], u), lerp(P[1], Q[1], u), cor, 0.85, 7)


def regua(c, P, Q, lado, a=1.0):
    """régua com a borda de medir em PQ; o corpo fica do lado `lado`"""
    if a <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy * lado, -ux * lado
    L = math.hypot(Q[0] - P[0], Q[1] - P[1])
    pts = [P, Q, (Q[0] + nx * 70, Q[1] + ny * 70), (P[0] + nx * 70, P[1] + ny * 70)]
    path = skia.Path(); path.addPoly(pts, True)
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.14 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
    c.save(); c.translate(6, 10); c.drawPath(path, s); c.restore()
    c.drawPath(path, M.paint("#F2D79B", 0.78 * a))
    c.drawPath(path, M.paint("#A9844A", a, stroke=3))
    i = 1
    while i * 22 < L - 6:
        d = i * 22
        x, y = P[0] + ux * d, P[1] + uy * d
        h = 26 if i % 5 == 0 else 14
        M.line(c, x, y, x + nx * h, y + ny * h, "#7A5A28", a, 2)
        i += 1


def seta_curva(c, P, Q, bojo, cor, a=1.0, p=1.0, larg=6):
    """seta curva de P até Q, abaulada para o lado de `bojo` (vetor)"""
    if a <= 0 or p <= 0:
        return
    K = (meio(P, Q)[0] + bojo[0], meio(P, Q)[1] + bojo[1])
    n = 40
    pts = []
    for i in range(int(n * p) + 1):
        u = i / n
        pts.append(((1 - u) ** 2 * P[0] + 2 * u * (1 - u) * K[0] + u * u * Q[0], (1 - u) ** 2 * P[1] + 2 * u * (1 - u) * K[1] + u * u * Q[1]))
    path = skia.Path(); path.addPoly(pts, False)
    c.drawPath(path, M.paint(cor, a, stroke=larg, cap_round=True))
    if p >= 0.98 and len(pts) > 2:
        (x0, y0), (x1, y1) = pts[-3], pts[-1]
        M.arrow(c, x0, y0, x1, y1, cor, a, larg, 22, 1.0)


# pontos dos cruzamentos
def cruz_pts(ys):
    return [pl(y) for y in ys], [pr(y) for y in ys]


def figura(c, t, t0, labs, ys=YS, tinta=TINTA, cor_cima=COR, cor_baixo=AMBAR, tp=None, a=1.0, size=60):
    """o feixe com os quatro pedaços pintados e as medidas. labs = (esq cima, esq baixo, dir cima, dir baixo);
    cada item é um texto ou (texto, instante) ou (texto, instante, troca, novo, cor_novo)"""
    L, R = cruz_pts(ys)
    feixe(c, t, t0, ys, tinta=tinta, a=a)
    tp = tp or [t0 + 0.9] * 4
    pecas = ((L[0], L[1], cor_cima, -1), (L[1], L[2], cor_baixo, -1), (R[0], R[1], cor_cima, 1), (R[1], R[2], cor_baixo, 1))
    for (P, Q, cor, lado), tt, lab in zip(pecas, tp, labs):
        if tt is None:
            continue
        pedaco(c, t, tt, P, Q, cor, a)
        if lab is None:
            continue
        if isinstance(lab, str):
            lab = (lab, tt + 0.2)
        if len(lab) == 2:
            rot(c, t, lab[1], P, Q, lab[0], lado, cor, size)
        else:
            rot_troca(c, t, lab[1], lab[2], P, Q, lab[0], lab[3], lado, cor, lab[4], size)
    return L, R


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    tq = lerp(kc, kd, 0.35)
    L, R = cruz_pts(YS)

    def um():
        def fig():
            mapa(c, t, ka, YS)
            pedaco(c, t, kb, L[0], L[1], COR, larg=16)
            rot(c, t, kb + 0.2, L[0], L[1], "3 cm", -1, COR, 62, 44)
            pedaco(c, t, kb + 0.8, L[1], L[2], AMBAR, larg=16)
            rot(c, t, kb + 1.0, L[1], L[2], "6 cm", -1, AMBAR, 62, 44)
            pedaco(c, t, kc, R[0], R[1], COR, larg=16)
            rot(c, t, kc + 0.2, R[0], R[1], "4 cm", 1, COR, 62, 44)
            pedaco(c, t, tq, R[1], R[2], AMBAR, larg=16)
            rot_troca(c, t, tq + 0.2, kd, R[1], R[2], "?", "8 cm", 1, ERRADO, CERTO, 72, 44)
        vista(c, fig)
        E.frase(c, t, ka + 0.3, [("3", "g", 110, COR), ("ruas", "g", 96)], XT, 290, "center", 0.15)
        E.frase(c, t, ka + 0.9, ps("paralelas", "i", 84), XT, 390, "center")
        E.frase(c, t, ka + 1.8, ps("e", "i", 76) + [("2", "g", 90, COR), ("avenidas", "g", 80)], XT, 500, "center", 0.12)
        E.frase(c, t, tq, ps("e o segundo?", "i", 76), XT, 650, "center", 0.12)
        E.frase(c, t, lerp(kc, kd, 0.65), [("sem", "i", 70), ("régua", "g", 76, COR)], XT, 760, "center", 0.12)
        bola_txt(c, t, kd, "8 cm", XT, 900, 100, 66, CERTO)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("achar o x", "g", 110, COR)], XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.55), ps("em qualquer", "i", 90), XE, 590, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.7), [("feixe de paralelas", "g", 84)], XE, 710, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 820
    itens = (("s03.b", "retas paralelas", "e transversal"), ("s03.c", "proporção e a cruz", "x/6 = 4/3 → x = 8"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
    py = lerp(420, 700, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 920, "left", 0.12)


# ---------------- o feixe ----------------
def b_feixe(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    tp = [c4 + 0.3, c4 + 0.7, c4 + 1.3, c4 + 1.7]
    L, R = cruz_pts(YS)

    def fig():
        feixe(c, t, a4, YS, tl=b4, tr=c4)
        for (P, Q), cor, tt in zip(((L[0], L[1]), (L[1], L[2]), (R[0], R[1]), (R[1], R[2])), (COR, AMBAR, COR, AMBAR), tp):
            pedaco(c, t, tt, P, Q, cor)
    vista(c, fig)
    E.frase(c, t, a4 + 0.3, [("feixe", "g", 110, COR)], XT, 280, "center")
    E.frase(c, t, a4 + 0.8, ps("de paralelas", "i", 84), XT, 380, "center", 0.12)
    E.frase(c, t, b4, [("transversal:", "g", 76)], XT, 540, "center")
    E.frase(c, t, b4 + 0.6, ps("corta todas", "i", 70), XT, 630, "center", 0.12)
    E.frase(c, t, c4, ps("dividida em", "i", 70) + [("pedaços", "g", 76, COR)], XT, 790, "center", 0.12)
    E.frase(c, t, c4 + 1.2, ps("de uma paralela à seguinte", "i", 52, TINTA2), XT, 880, "center", 0.1)


# ---------------- o caderno ----------------
LC = [230 + 115 * i for i in range(7)]          # linhas do caderno
R1 = ((420, 180), (560, 1000))                   # borda da régua 1
R2 = ((680, 180), (1080, 1000))                  # borda da régua 2, mais inclinada


def na_regua(R, y):
    (x0, y0), (x1, y1) = R
    return x0 + (y - y0) * (x1 - x0) / (y1 - y0), y


def b_caderno(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    E.frase(c, t, C["s05"], ps("por que", "i", 60) + [("combinam?", "g", 66, COR)], XT + 40, 150, "center", 0.12)

    def folha(a):
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.16 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 12))
        c.drawRect(skia.Rect.MakeXYWH(108, 182, 1060, 830), s)
        c.drawRect(skia.Rect.MakeXYWH(100, 170, 1060, 830), M.paint("#FFFFFF", a))
        c.drawRect(skia.Rect.MakeXYWH(100, 170, 1060, 830), M.paint(CINZA, a, stroke=2))
    E.foco(c, t, a5, 0.5, folha)
    for i, y in enumerate(LC):
        M.line(c, 130, y, lerp(130, 1130, ease_io(prog(t, a5 + 0.2 + 0.08 * i, 0.6))), y, TINTA2, 1.0 if t >= a5 else 0, 4)
    # régua 1 e os pedaços iguais
    E.foco(c, t, b5, 0.5, lambda a: regua(c, *R1, -1, a))
    E.foco(c, t, a6, 0.5, lambda a: regua(c, *R2, 1, a))
    dim = 1 - 0.65 * ep(t, c6, 0.4)
    for i in range(6):
        P, Q = na_regua(R1, LC[i]), na_regua(R1, LC[i + 1])
        ti = c5 + 0.25 * i
        pedaco(c, t, ti, P, Q, COR if i % 2 == 0 else E.mix(COR, BR, 0.45), dim, 10, 0.3)
        E.marcas_iguais(c, P, Q, 1, COR, ep(t, ti + 0.2, 0.3) * dim)
        P, Q = na_regua(R2, LC[i]), na_regua(R2, LC[i + 1])
        ti = b6 + 0.25 * i
        pedaco(c, t, ti, P, Q, AMBAR if i % 2 == 0 else E.mix(AMBAR, BR, 0.45), dim, 10, 0.3)
        E.marcas_iguais(c, P, Q, 2, AMBAR, ep(t, ti + 0.2, 0.3) * dim)
    # o dobro de linhas: 1 espaço (linhas 0 a 1) e 2 espaços (linhas 2 a 4)
    for R, tt in ((R1, c6), (R2, d6)):
        pedaco(c, t, tt, na_regua(R, LC[0]), na_regua(R, LC[1]), COR, 1.0, 16)
        pedaco(c, t, tt + 0.6, na_regua(R, LC[2]), na_regua(R, LC[4]), CERTO, 1.0, 16)
    E.foco(c, t, c6 + 0.2, 0.4, lambda a: (E.escreve(c, "1 espaço", 130, (LC[0] + LC[1]) / 2 + 16, 44, "b", COR, a),
                                           E.escreve(c, "2 espaços", 130, LC[3] + 16, 44, "b", CERTO, a)))
    E.foco(c, t, d6 + 0.6, 0.4, lambda a: (E._cola(c, "×2", *na_regua(R2, LC[3]), 1, -0.3, 110, 64, "g", CERTO, a)))

    def cinco():
        E.frase(c, t, a5, ps("linhas do", "i", 70) + [("caderno", "g", 76)], XT, 320, "center", 0.12)
        E.frase(c, t, a5 + 1.2, ps("sempre à mesma distância", "i", 52, TINTA2), XT, 400, "center", 0.1)
        E.frase(c, t, b5, ps("uma", "i", 70) + [("régua", "g", 76)] + ps("inclinada", "i", 70), XT, 560, "center", 0.12)
        E.frase(c, t, c5, ps("marca sempre o", "i", 64), XT, 720, "center", 0.12)
        E.frase(c, t, c5 + 0.8, [("mesmo tamanho", "g", 80, COR)], XT, 820, "center")
    E.saida(c, t, a6 - 0.1, cinco)
    if t >= a6:
        E.frase(c, t, a6, [("outra régua", "g", 76, AMBAR)], XT, 320, "center")
        E.frase(c, t, a6 + 0.9, ps("o pedaço muda", "i", 64), XT, 410, "center", 0.12)
        E.frase(c, t, b6, ps("mas é", "i", 64) + [("igual", "g", 72, AMBAR)], XT, 540, "center", 0.12)
        E.frase(c, t, b6 + 0.6, ps("entre linhas vizinhas", "i", 56), XT, 620, "center", 0.12)
        E.frase(c, t, c6, [("dobro", "g", 72, CERTO)] + ps("de linhas", "i", 62), XT + 30, 780, "center", 0.12)
        E.frase(c, t, d6, [("dobro", "g", 72, CERTO)] + ps("na outra régua", "i", 58), XT + 30, 900, "center", 0.12)


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    t0 = C["s07"] + 0.2
    L, R = cruz_pts(YS)

    def fig():
        figura(c, t, t0, ("3", "6", "4", ("x", b7 + 0.9, d9, "8", CERTO)), tp=[b7 + 0.3, b7 + 0.5, b7 + 0.7, b7 + 0.9])
        # distâncias diferentes entre as paralelas
        q = ep(t, t0 + 1.0, 0.4) * (1 - ep(t, a8, 0.4))
        for y0, y1 in ((YS[0], YS[1]), (YS[1], YS[2])):
            if q > 0:
                M.arrow(c, 200, (y0 + y1) / 2, 200, y0 + 14, TINTA2, q, 4, 16, 1.0)
                M.arrow(c, 200, (y0 + y1) / 2, 200, y1 - 14, TINTA2, q, 4, 16, 1.0)
        # na fala de cada fração, o pedaço de cima e o de baixo piscam
        for tt, (P, Q) in ((a8, (L[0], L[2])), (b8, (R[0], R[2]))):
            k = ep(t, tt, 0.3) * (1 - ep(t, tt + 1.6, 0.4))
            if k > 0:
                M.line(c, *P, *Q, TINTA, 0.25 * k, 40)
    vista(c, fig)

    def sete():
        E.frase(c, t, C["s07"] + 0.5, ps("distâncias diferentes?", "i", 56, TINTA2), XT, 170, "center", 0.1)
        E.frase(c, t, a7, ps("teorema de", "i", 76), XT, 300, "center", 0.12)
        E.frase(c, t, a7 + 0.5, [("Tales", "g", 130, COR)], XT, 430, "center")
        E.frase(c, t, b7, ps("paralelas cortam em", "i", 58), XT, 560, "center", 0.1)
        E.frase(c, t, b7 + 1.0, [("pedaços", "g", 76)], XT, 650, "center")
        E.frase(c, t, b7 + 1.3, [("proporcionais", "g", 76, COR)], XT, 740, "center")
        E.foco(c, t, c7, 0.5, lambda a: E.pilula(c, "na mesma razão", XT, 900, 64, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s08"] - 0.1, sete)
    if t < C["s08"]:
        return
    cx, cy = XT, 330
    E.frase(c, t, C["s08"] + 0.2, ps("cima sobre baixo", "i", 56, TINTA2), cx, 170, "center", 0.1)
    prop(c, t, a8, "3", "6", "4", "x", cx, cy, 120, t1=b8)
    if t >= a9:
        cruz(c, t, a9, b9, cx, cy, 120)

    def oito():
        E.frase(c, t, c8, [("3", "g", 64, COR)] + ps("está para", "i", 58) + [("6", "g", 64, AMBAR)], cx, 640, "center", 0.12)
        E.frase(c, t, c8 + 1.2, ps("assim como", "i", 58), cx, 730, "center", 0.12)
        E.frase(c, t, c8 + 1.8, [("4", "g", 64, COR)] + ps("está para", "i", 58) + [("x", "g", 64, AMBAR)], cx, 820, "center", 0.12)
    E.saida(c, t, C["s09"] - 0.1, oito)
    if t < C["s09"]:
        return
    w1 = E.formula(None, "3 · x ", 0, 0, 76, "g", a=0)
    x0 = cx - (w1 + E.formula(None, "= 6 · 4 = 24", 0, 0, 76, "g", a=0)) / 2
    E.formula_em(c, t, a9, "3 · x ", x0, 620, 76, "g", COR)
    E.formula_em(c, t, b9, "= 6 · 4 = 24", x0 + w1, 620, 76, "g", AMBAR)
    fcen(c, t, c9, "3x = 24", cx, 770, 90)
    fcen(c, t, d9, "x = 24 ÷ 3", cx - 90, 920, 80)
    bola_txt(c, t, d9 + 0.6, "8", cx + 230, 895, 80, 100, CERTO)


# ---------------- outras montagens ----------------
def b_montagens(c, t, C, b):
    a, b_, c_, d, e, f = (C[f"s10.{k}"] for k in "abcdef")
    t0 = C["s10"]
    L, R = cruz_pts(YS)

    def fig():
        figura(c, t, t0 - 0.6, ("3", "6", "4", ("x", t0 - 0.4, d, "8", AMBAR)), tp=[t0 - 0.4] * 4)
        k = ep(t, a, 0.3) * (1 - ep(t, c_, 0.4))
        if k > 0:
            M.line(c, *L[0], *L[1], COR, 0.3 * k, 44)
            M.line(c, *R[0], *R[1], COR, 0.3 * k, 44)
        cota(c, t, d, L[0], L[2], "9", -1, TINTA2, 130)
        cota(c, t, d + 0.4, R[0], R[2], "12", 1, TINTA2, 130, onde=0.3)
    vista(c, fig)
    cx = XT
    E.frase(c, t, a, ps("de uma transversal", "i", 58), cx, 160, "center", 0.1)
    E.frase(c, t, a + 0.8, ps("para a outra", "i", 58), cx, 235, "center", 0.1)
    prop(c, t, b_, "3", "4", "6", "x", cx, 345, 100, cores=(COR, COR, AMBAR, AMBAR), t1=b_ + 1.2)
    fcen(c, t, c_, "3x = 24", cx - 90, 555, 72)
    E.foco(c, t, c_ + 0.6, 0.4, lambda a_: E.escreve(c, "o mesmo", cx + 90, 550, 52, "i", CERTO, a_))
    E.frase(c, t, d, ps("o trecho inteiro", "i", 58, TINTA2), cx, 650, "center", 0.1)
    prop(c, t, e, "3", "9", "4", "12", cx, 800, 100, cores=(COR, TINTA2, COR, TINTA2), t1=e + 1.2)
    E.foco(c, t, f, 0.5, lambda a_: E.pilula(c, "a questão dá o total", cx, 1000, 54, "g", a=a_, cor=E.SOBRE))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    t0 = C["s11"]
    L, R = cruz_pts(YS)

    def fig():
        figura(c, t, t0 - 0.6, ("3", "6", "4", "x"), tp=[t0 - 0.4] * 4)
        k = ep(t, a12, 0.3)
        if k > 0:
            M.line(c, *L[1], *L[2], AMBAR, 0.3 * k, 44)
            M.line(c, *R[1], *R[2], AMBAR, 0.3 * k, 44)
        # x = 2 seria menor que o 4 de cima: o pedaço de baixo da direita é bem maior
        k = ep(t, b12, 0.3)
        if k > 0:
            M.line(c, *R[0], *R[1], COR, 0.3 * k, 44)
    vista(c, fig)
    cx = XT
    E.frase(c, t, t0 + 0.2, [("cuidado", "g", 84, ERRADO)], cx, 170, "center")

    def onze():
        E.frase(c, t, a11, ps("trocar a ordem", "i", 64), cx, 270, "center", 0.12)
        E.frase(c, t, a11 + 0.8, [("de um lado só", "g", 68, ERRADO)], cx, 350, "center")
    E.saida(c, t, C["s12"] - 0.1, onze)
    errada = lambda: (prop(c, t, b11, "3", "6", "x", "4", cx, 500, 110, cores=(COR, AMBAR, ERRADO, ERRADO), t1=b11 + 1.2),
                      fcen(c, t, c11, "6x = 12", cx, 700, 84, ERRADO),
                      fcen(c, t, d11, "x = 2", cx - 60, 850, 84, ERRADO),
                      E.foco(c, t, d11 + 0.4, 0.4, lambda a: E.selo(c, cx + 140, 822, 52, False, a)),
                      E.risco(c, cx - 150, 822, cx + 30, 822, t, b12 + 0.4, ERRADO, 10) if t >= b12 else None)
    E.saida(c, t, c12 - 0.1, errada)
    if t >= C["s12"]:
        E.saida(c, t, c12 - 0.1, lambda: (
            E.frase(c, t, a12, [("x", "g", 64, AMBAR)] + ps("e", "i", 58) + [("6:", "g", 64, AMBAR)] + ps("mesmas paralelas", "i", 58), cx, 290, "center", 0.12),
            E.frase(c, t, b12, [("x", "g", 64, AMBAR)] + ps("maior que", "i", 58) + [("4", "g", 64, COR)], cx, 380, "center", 0.12)))
    if t >= c12:
        E.frase(c, t, c12, [("regra de ouro", "g", 64, CERTO)], cx, 300, "center")
        prop(c, t, c12 + 0.3, "3", "6", "4", "x", cx, 520, 110, cores=(COR, AMBAR, COR, AMBAR), t1=c12 + 0.5)
        E.frase(c, t, c12 + 0.9, ps("cima", "i", 54, COR) + ps("sobre", "i", 54) + ps("baixo", "i", 54, AMBAR) + ps("nas duas", "i", 54), cx, 780, "center", 0.1)
        E.foco(c, t, c12 + 1.6, 0.4, lambda a: E.selo(c, cx, 920, 60, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    t0 = C["s13"]
    L, R = cruz_pts(YS)
    LIL, AMB_C = CLARO, "#FFB238"

    def treze():
        def fig():
            figura(c, t, t0, ("3", "6", "4", ("x", t0 + 0.9, c13 + 0.6, "8", BR)), tinta=BR, cor_cima=LIL, cor_baixo=AMB_C)
            ux, uy = E._uni(*L[0], *L[2])
            off = (-uy * -1 * 150, ux * -1 * 150)
            P, Q = meio(L[0], L[1]), meio(L[1], L[2])
            seta_curva(c, (P[0] - 120, P[1]), (Q[0] - 150, Q[1]), (-120, 0), BR, ep(t, b13, 0.3), ease_io(prog(t, b13, 0.7)))
            E.foco(c, t, b13 + 0.5, 0.4, lambda a: E.escreve(c, "×2", 60, (P[1] + Q[1]) / 2 + 30, 70, "g", BR, a))
            P, Q = meio(R[0], R[1]), meio(R[1], R[2])
            seta_curva(c, (P[0] + 130, P[1] - 20), (Q[0] + 140, Q[1] - 40), (150, -40), BR, ep(t, c13, 0.3), ease_io(prog(t, c13, 0.7)))
            E.foco(c, t, c13 + 0.5, 0.4, lambda a: E.escreve(c, "×2", (P[0] + Q[0]) / 2 + 300, (P[1] + Q[1]) / 2 + 60, 70, "g", BR, a))
        vista(c, fig)
        E.frase(c, t, a13, ps("procure o", "i", 70, CLARO) + [("fator", "g", 84, BR)], XT, 260, "center", 0.12)
        E.frase(c, t, a13 + 1.0, ps("na mesma transversal", "i", 56, CLARO), XT, 350, "center", 0.1)
        fcen(c, t, b13, "6 = 2 · 3", XT, 520, 90, BR)
        fcen(c, t, c13, "x = 2 · 4 = 8", XT, 680, 90, BR)
        E.frase(c, t, c13 + 1.6, ps("sem montar conta", "i", 64, CLARO), XT, 850, "center", 0.12)
    E.saida(c, t, C["s14"] - 0.1, treze)
    if t < C["s14"]:
        return
    # proporção = fração equivalente
    x1 = 520
    E.frase(c, t, a14, ps("proporção =", "i", 64, CLARO), x1, 220, "center", 0.12)
    E.frase(c, t, a14 + 0.8, [("fração equivalente", "g", 66, BR)], x1, 310, "center")
    E.foco(c, t, a14 + 0.4, 0.5, lambda a: (frac2(c, "3", "6", x1 - 150, 520, 120, LIL, AMB_C, a, BR),
                                            centro(c, "=", x1, 520 + 43, 120, "g", BR, a),
                                            frac2(c, "4", "8", x1 + 150, 520, 120, LIL, AMB_C, a, BR)))
    for xx, sg in ((x1 - 150, -1), (x1 + 150, 1)):
        seta_curva(c, (xx + sg * 50, 470), (xx + sg * 50, 600), (sg * 70, 0), CLARO, ep(t, a14 + 1.4, 0.3), ease_io(prog(t, a14 + 1.4, 0.6)), 5)
        E.foco(c, t, a14 + 1.9, 0.4, lambda a, xx=xx, sg=sg: E.escreve(c, "×2", xx + sg * 100 - (70 if sg < 0 else 0), 560, 48, "g", CLARO, a))
    E.frase(c, t, a14 + 2.2, ps("multiplica nas duas", "i", 54, CLARO), x1, 780, "center", 0.1)
    # fator que não é inteiro: vá de cruz
    x2, y2 = 1420, 420
    E.frase(c, t, b14, ps("fator", "i", 64, CLARO) + [("não inteiro?", "g", 70, AMB_C)], x2, 200, "center", 0.12)
    prop(c, t, c14, "4", "6", "10", "x", x2, y2, 110, cores=(LIL, AMB_C, LIL, AMB_C), t1=c14 + 1.2, barra=BR, igual=BR, dx=190)
    E.foco(c, t, c14 + 1.8, 0.4, lambda a: E.pilula(c, "6 ÷ 4 = 1,5", x2, 630, 50, "g", fundo="#2A2840", cor=AMB_C, a=a))
    E.foco(c, t, lerp(c14, d14, 0.75), 0.4, lambda a: E.pilula(c, "vá de cruz", x2, 735, 50, "g", a=a, cor=E.SOBRE))
    if t >= d14:
        cruz(c, t, d14, d14 + 0.3, x2, y2, 110, dx=190, c1=LIL, c2=AMB_C)
    fcen(c, t, d14, "4x = 60", x2 - 120, 920, 84, BR)
    bola_txt(c, t, d14 + 0.8, "15", x2 + 200, 895, 80, 84, CERTO)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a15, b15, c15, d15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    rel = C["s16.a"]
    L, R = cruz_pts(YQ)

    def fig():
        mapa(c, t, a15, YQ)
        pedaco(c, t, b15, L[0], L[1], COR, larg=16)
        rot(c, t, b15 + 0.2, L[0], L[1], "60 m", -1, COR, 60, 44)
        pedaco(c, t, b15 + 0.8, L[1], L[2], AMBAR, larg=16)
        rot(c, t, b15 + 1.0, L[1], L[2], "90 m", -1, AMBAR, 60, 44)
        cota(c, t, c15, R[0], R[2], "200 m", 1, TINTA2, 70, 60)
        rot(c, t, d15, R[0], R[1], "?", -1, COR, 72, 44)
        rot(c, t, d15 + 0.3, R[1], R[2], "?", -1, AMBAR, 72, 44)
    vista(c, fig)
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XT, 170, "center", 0.12)

    def lado():
        E.frase(c, t, a15, [("3", "g", 80, COR)] + ps("ruas paralelas", "i", 64), XT, 330, "center", 0.12)
        E.frase(c, t, a15 + 1.2, [("2", "g", 80, COR)] + ps("avenidas", "i", 64), XT, 430, "center", 0.12)
    E.saida(c, t, rel - 0.5, lado)
    E.frase(c, t, b15, ps("avenida 1:", "i", 56) + [("60 e 90 m", "g", 60)], XT, 800, "center", 0.12)
    E.frase(c, t, c15, ps("avenida 2:", "i", 56) + [("200 m", "g", 60)] + ps("no total", "i", 56), XT, 890, "center", 0.12)
    E.frase(c, t, d15, ps("cada", "i", 56) + [("quarteirão?", "g", 62, COR)], XT, 980, "center", 0.12)
    E.relogio(c, t, rel, XT, 420, 150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a17, b17, a18, b18, c18, a19, b19 = (C[k] for k in ("s17.a", "s17.b", "s18.a", "s18.b", "s18.c", "s19.a", "s19.b"))
    t0 = C["s17"]
    L, R = cruz_pts(YQ)

    def fig():
        mapa(c, t, t0 - 0.6, YQ, ruas=t < a17 + 0.2)
        pedaco(c, t, t0 - 0.4, L[0], L[1], COR, larg=16)
        rot(c, t, t0 - 0.4, L[0], L[1], "60 m", 1, COR, 56, 40, onde=0.35)
        pedaco(c, t, t0 - 0.4, L[1], L[2], AMBAR, larg=16)
        rot(c, t, t0 - 0.4, L[1], L[2], "90 m", 1, AMBAR, 56, 44)
        cota(c, t, t0 - 0.4, R[0], R[2], "200 m", 1, TINTA2, 70, 56)
        cota(c, t, a17 + 0.4, L[0], L[2], "150 m", -1, TINTA2, 70, 54, onde=0.78)
        # o primeiro quarteirão de cada avenida contra o trecho inteiro
        pedaco(c, t, b17, R[0], R[1], COR, larg=16)
        rot_troca(c, t, t0 - 0.4, b18 + 0.6, R[0], R[1], "?", "80 m", -1, COR, CERTO, 60, 40, onde=0.55)
        pedaco(c, t, c18, R[1], R[2], AMBAR, larg=16)
        rot_troca(c, t, t0 - 0.4, c18 + 0.6, R[1], R[2], "?", "120 m", -1, AMBAR, CERTO, 60, 44)
    vista(c, fig)
    cx = XT

    def conta():
        fcen(c, t, a17, "60 + 90 = 150", cx, 200, 72)
        prop(c, t, b17, "60", "150", "x", "200", cx, 360, 92, cores=(COR, TINTA2, COR, TINTA2), dx=230, t1=b17 + 1.6)
        if t >= a18:
            cruz(c, t, a18, a18 + 0.6, cx, 360, 92, dx=230, c2=TINTA2, wa=90, wb=95)
        E.saida(c, t, a18 + 2.2, lambda: fcen(c, t, a18, "150x = 60 · 200", cx, 600, 66))
        fcen(c, t, a18 + 2.3, "150x = 12.000", cx, 600, 66)
        fcen(c, t, b18, "x = 12.000 ÷ 150", cx, 720, 62)
        fcen(c, t, b18 + 1.0, "x = 80 m", cx, 840, 72, CERTO)
        fcen(c, t, c18, "200 − 80 = 120 m", cx, 960, 62, CERTO)
    E.saida(c, t, C["s19"] - 0.1, conta)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("conferindo", "g", 72, COR)], cx, 200, "center")
    fcen(c, t, a19, "f{80}{120} = f{2}{3}", cx, 420, 90)
    E.foco(c, t, a19 + 1.2, 0.4, lambda a: E.escreve(c, "÷ 40", cx + 230, 400, 48, "b", TINTA2, a))
    fcen(c, t, b19, "f{60}{90} = f{2}{3}", cx, 680, 90)
    E.foco(c, t, b19 + 1.0, 0.4, lambda a: E.escreve(c, "÷ 30", cx + 230, 660, 48, "b", TINTA2, a))
    E.foco(c, t, b19 + 2.0, 0.5, lambda a: E.selo(c, cx, 890, 80 * ease_back(prog(t, b19 + 2.0, 0.5)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s20.a", "paralelas cortam em pedaços proporcionais"), ("s20.b", "frações sempre na mesma ordem"))
        for i, (k, s) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         centro(c, str(i + 1), 260, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 70)], 360, y)
        E.foco(c, t, C["s20.b"] + 0.8, 0.5, lambda a: (frac2(c, "3", "6", 860, 820, 90, COR, AMBAR, a),
                                                      centro(c, "=", 980, 820 + 32, 90, "g", TINTA, a),
                                                      frac2(c, "4", "x", 1100, 820, 90, COR, AMBAR, a)))
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.2, ps("próxima aula", "i", 84), XE, 280)
    E.frase(c, t, C["s21.a"], [("Tales no", "g", 120, COR)], XE, 420)
    E.frase(c, t, C["s21.a"] + 0.3, [("triângulo", "g", 120, COR)], XE, 550)
    E.frase(c, t, C["s21.b"], ps("e onde a", "i", 70) + [("bissetriz", "g", 74)] + ps("corta", "i", 70), XE, 690, passo=0.12)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1630, p), lerp(720, 425, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, feixe=b_feixe, caderno=b_caderno, regra=b_regra, montagens=b_montagens,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
