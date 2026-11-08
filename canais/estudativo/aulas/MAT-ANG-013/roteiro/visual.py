"""Visual — Estudativo · MAT-ANG-013: semelhança em problemas, sombras e triângulos encaixados (poste 2 e 3, prédio x e 30: x = 20).
Linguagem da geometria plana (MAT-ANG-001 a 020): lados em tinta; ângulos iguais com a mesma marca e a mesma cor (um arco em
COR, índigo; o ângulo comum em TINTA2); ângulo reto = quadradinho; raio de luz tracejado em âmbar; medidas na grotesca;
erro em vermelho, certo em verde; resposta na esfera; atalho no palco escuro.
Famílias de cor dos lados: o que fica em pé (altura) vai em COR, o que fica no chão (sombra) vai em AMBAR; no encaixado,
o lado de cima (AM, AB) em COR e o paralelo (MN, BC) em AMBAR.
Figuras honestas: o poste e o prédio têm o mesmo formato (2 : 3), cada um na sua escala, com os raios na mesma inclinação;
ABC com AM = 3, MB = 6, MN = 4, BC = 12 em escala; na questão, lâmpada a 4 m, pessoa de 1,6 m a 3 m, sombra de 2 m, em escala.
Peças locais (as da MAT-ANG-012): marca(), reto(), txt_lado(), lab(), triang(), brilho(), frac2(), prop(), cruz(); e ainda
sol(), raio(), poste(), predio(), arvore(), pessoa() (a da MAT-RAZ-007) e lampada().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-013_sombras_e_triangulos_encaixados.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("sombra", "encaixados", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
AMB_C = "#FFB238"
XT = 1560
assert 3 * 20 == 2 * 30 and 60 // 3 == 20
assert 3 + 6 == 9 and 3 * 12 == 9 * 4 == 36 and 36 // 3 == 12 and 3 * 8 == 6 * 4
assert 30 // 3 == 10 and 10 * 2 == 20 and 12 // 3 == 4 and 4 * 2 == 8
assert 2 + 3 == 5 and abs(1.6 * 5 - 8) < 1e-9 and 8 // 2 == 4 and abs(1.6 * 3 / 2 - 2.4) < 1e-9


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


def dirg(V, P):
    return math.degrees(math.atan2(-(P[1] - V[1]), P[0] - V[0])) % 360


def faixa_v(V, P, Q):
    a1, a2 = dirg(V, P), dirg(V, Q)
    d = (a2 - a1) % 360
    return (a1, a1 + d) if d <= 180 else (a2, a2 + (360 - d))


def rotulo(c, V, g, r, s, cor, size, a):
    if a <= 0 or not s:
        return
    w = E.formula(None, s, 0, 0, size, "b", a=0)
    ux, uy = math.cos(math.radians(g)), -math.sin(math.radians(g))
    k = r + 16 + abs(ux) * w / 2 + abs(uy) * size * 0.4
    E.formula(c, s, V[0] + ux * k, V[1] + uy * k + size * 0.36, size, "b", cor, a, "center")


def marca(c, t, t0, V, P, Q, n=1, cor=None, r=62, rot=None, size=48, a=1.0, alfa=0.22):
    """ângulo PVQ marcado com n arcos (n = 0: só a cunha) e, se rot, a medida por fora"""
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    g1, g2 = faixa_v(V, P, Q)
    q = ease_io(prog(t, t0, 0.5))
    cunha_m(c, V, g1, g1 + (g2 - g1) * q, r, cor, a, alfa=alfa, borda=5)
    if n >= 2:
        ret = skia.Rect.MakeXYWH(V[0] - r + 14, V[1] - r + 14, 2 * r - 28, 2 * r - 28)
        c.drawArc(ret, -g1, -(g2 - g1) * q, False, M.paint(cor, a, stroke=5, cap_round=True))
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda k: rotulo(c, V, (g1 + g2) / 2, r, rot, cor, size, k * a))


def reto(c, t, t0, V, P, Q, cor=TINTA2, r=40, a=1.0):
    if t < t0 or a <= 0:
        return
    k = ep(t, t0, 0.4) * a
    ux, uy = E._uni(*V, *P)
    vx, vy = E._uni(*V, *Q)
    A_ = (V[0] + ux * r, V[1] + uy * r)
    B_ = (V[0] + vx * r, V[1] + vy * r)
    Cq = (V[0] + (ux + vx) * r, V[1] + (uy + vy) * r)
    path = skia.Path(); path.addPoly([V, A_, Cq, B_], True)
    c.drawPath(path, M.paint(cor, 0.2 * k))
    M.line(c, *A_, *Cq, cor, k, 5); M.line(c, *Cq, *B_, cor, k, 5)


def txt_lado(c, P, Q, s, G, size=56, cor=None, a=1.0, gap=22):
    if a <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = meio(P, Q)
    if (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 < (mx - G[0]) ** 2 + (my - G[1]) ** 2:
        nx, ny = -nx, -ny
    E._cola(c, s, mx, my, nx, ny, gap, size, "g", cor or COR, a)


def lab(c, t, t0, P, Q, s, G, cor=None, size=56, gap=22):
    if t >= t0:
        E.foco(c, t, t0, 0.4, lambda a: txt_lado(c, P, Q, s, G, size, cor, a, gap))


def centroide(T):
    return sum(p[0] for p in T) / 3, sum(p[1] for p in T) / 3


def triang(c, t, t0, T, nomes=None, tinta=TINTA, preenche=0.05, d=0.9, a=1.0, larg=6):
    if t < t0 or a <= 0:
        return
    if preenche:
        path = skia.Path(); path.addPoly(list(T), True)
        c.drawPath(path, M.paint(E.COR, preenche * ep(t, t0 + d * 0.6, 0.5) * a))
    p = ease_io(prog(t, t0, d))
    for i in range(3):
        P, Q = T[i], T[(i + 1) % 3]
        f = M.clamp(p * 3 - i)
        if f > 0:
            M.line(c, *P, lerp(P[0], Q[0], f), lerp(P[1], Q[1], f), tinta, a, larg)
    if nomes:
        g = centroide(T)
        for i, (V, s) in enumerate(zip(T, nomes)):
            if not s.strip():
                continue
            ux, uy = V[0] - g[0], V[1] - g[1]
            n = math.hypot(ux, uy)
            E.foco(c, t, t0 + 0.3 + 0.15 * i, 0.4, lambda k, V=V, s=s, ux=ux / n, uy=uy / n: centro(c, s, V[0] + ux * 58, V[1] + uy * 58 + 22, 56, "g", tinta, k * a))


def brilho(c, P, Q, cor, k, larg=32):
    if k > 0:
        M.line(c, *P, *Q, cor, 0.28 * k, larg)


def coloca(pts, s, ox, oy):
    """pontos da conta (y para cima) para a tela: escala s, origem (ox, oy)"""
    return tuple((ox + x * s, oy - y * s) for x, y in pts)


def frac2(c, n, d, cx, cy, size, cn=TINTA, cd=TINTA, a=1.0, barra=TINTA):
    if a <= 0:
        return
    n, d = str(n), str(d)
    wn, wd = E.formula(None, n, 0, 0, size, "g", a=0), E.formula(None, d, 0, 0, size, "g", a=0)
    lw = max(wn, wd) + size * 0.2
    E.formula(c, n, cx, cy - size * 0.2, size, "g", cn, a, "center")
    E.formula(c, d, cx, cy + size * 0.9, size, "g", cd, a, "center")
    b = size * 0.085
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - lw / 2, cy - b / 2 + size * 0.03, lw, b), b / 2, b / 2), M.paint(barra, a))


def prop(c, t, t0, n1, d1, n2, d2, cx, cy, size=100, cores=(COR, COR, AMBAR, AMBAR), t1=None, dx=170, barra=TINTA, igual=TINTA):
    t1 = t0 + 0.6 if t1 is None else t1
    E.foco(c, t, t0, 0.5, lambda a: frac2(c, n1, d1, cx - dx, cy, size, cores[0], cores[1], a, barra))
    E.foco(c, t, t1, 0.5, lambda a: (centro(c, "=", cx, cy + size * 0.36, size, "g", igual, a),
                                     frac2(c, n2, d2, cx + dx, cy, size, cores[2], cores[3], a, barra)))


def cruz(c, t, t0, t1, cx, cy, size=100, dx=170, c1=TINTA2, c2=TINTA2, wa=60, wb=60):
    xa, xb = cx - dx, cx + dx
    for tt, (P, Q), cor in ((t0, ((xa + wa, cy - size * 0.7), (xb - wb, cy + size * 0.95)), c1),
                            (t1, ((xa + wa, cy + size * 0.95), (xb - wb, cy - size * 0.7)), c2)):
        p = ease_io(prog(t, tt, 0.6))
        for u0, u1 in ((0.0, 0.36), (0.64, 1.0)):
            if p > u0:
                u = min(p, u1)
                M.line(c, lerp(P[0], Q[0], u0), lerp(P[1], Q[1], u0), lerp(P[0], Q[0], u), lerp(P[1], Q[1], u), cor, 0.85, 7)


# ---------------- figuras ----------------
def cota(c, t, t0, P, Q, s, lado, cor=TINTA2, off=60, size=54, a=1.0, onde=0.5):
    """medida afastada do segmento PQ, com tracinhos nas pontas (como na MAT-ANG-010)"""
    if t < t0 or a <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy * lado, -ux * lado
    A_ = (P[0] + nx * off, P[1] + ny * off)
    B_ = (Q[0] + nx * off, Q[1] + ny * off)
    q = ease_io(prog(t, t0, 0.6))
    M.line(c, *A_, lerp(A_[0], B_[0], q), lerp(A_[1], B_[1], q), cor, a, 4)
    k = ep(t, t0, 0.3) * a
    for V in (A_, B_):
        M.line(c, V[0] - nx * 16, V[1] - ny * 16, V[0] + nx * 16, V[1] + ny * 16, cor, k, 4)
    E.foco(c, t, t0 + 0.4, 0.4, lambda f: E._cola(c, s, lerp(A_[0], B_[0], onde), lerp(A_[1], B_[1], onde), nx, ny, 14, size, "g", cor, f * a))


def sol(c, x, y, r=46, a=1.0):
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(x, y), r * 2.4, [M.hexc(AMB_C, 0.45 * a), M.hexc(AMB_C, 0.0)], [0, 1]))
    c.drawCircle(x, y, r * 2.4, p)
    c.drawCircle(x, y, r, M.paint(AMB_C, a))
    for i in range(8):
        g = math.radians(i * 45)
        M.line(c, x + math.cos(g) * r * 1.3, y + math.sin(g) * r * 1.3, x + math.cos(g) * r * 1.7, y + math.sin(g) * r * 1.7, AMB_C, a, 5)


def raio(c, t, t0, topo, ponta, extra=260, a=1.0, cor=AMBAR, larg=5, d=0.7):
    """raio de luz tracejado, que vem de cima, passa pelo topo e chega na ponta da sombra"""
    if t < t0 or a <= 0:
        return
    ux, uy = E._uni(*ponta, *topo)
    O = (topo[0] + ux * extra, topo[1] + uy * extra)
    q = ease_io(prog(t, t0, d))
    M.line(c, *O, lerp(O[0], ponta[0], q), lerp(O[1], ponta[1], q), cor, a, larg, dash=[16, 10])


def sombra(c, t, t0, base, ponta, a=1.0, d=0.6):
    if t < t0 or a <= 0:
        return
    M.line(c, *base, lerp(base[0], ponta[0], ease_io(prog(t, t0, d))), base[1], TINTA, 0.32 * a, 20)


def chao(c, x0, x1, y, a=1.0):
    if a > 0:
        M.line(c, x0, y, x1, y, TINTA2, a, 4)


def poste(c, t, t0, base, topo, a=1.0, cor=TINTA):
    if t < t0 or a <= 0:
        return
    q = ease_io(prog(t, t0, 0.5))
    M.line(c, *base, base[0], lerp(base[1], topo[1], q), cor, a, 12)


def predio(c, t, t0, xr, base, h, w=110, a=1.0):
    """prédio com a parede da direita em xr"""
    if t < t0 or a <= 0:
        return
    k = ep(t, t0, 0.5) * a
    q = ease_io(prog(t, t0, 0.6))
    hh = h * q
    c.drawRect(skia.Rect.MakeXYWH(xr - w, base - hh, w, hh), M.paint("#DAD8E6", k))
    c.drawRect(skia.Rect.MakeXYWH(xr - w, base - hh, w, hh), M.paint(TINTA, k, stroke=5))
    for i in range(int(hh // 48)):
        for j in range(2):
            c.drawRect(skia.Rect.MakeXYWH(xr - w + 20 + j * 44, base - 40 - i * 48, 26, 26), M.paint("#9C98B8", k))


def pessoa(c, cx, base, h, cor=TINTA2, a=1.0):
    """bonequinho (da MAT-RAZ-007): cabeça e corpo arredondado; o topo da cabeça fica em base − h"""
    if a <= 0:
        return
    r = h * 0.15
    c.drawCircle(cx, base - h + r, r, M.paint(cor, a))
    w = h * 0.42
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, base - h * 0.68, w, h * 0.68), w * 0.4, w * 0.4), M.paint(cor, a))


def lampada(c, base, topo, a=1.0, acesa=1.0):
    """poste com a lâmpada na ponta; devolve o ponto da lâmpada"""
    L = topo
    if a <= 0:
        return L
    M.line(c, *base, *topo, TINTA, a, 12)
    if acesa > 0:
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(*L), 90, [M.hexc(AMB_C, 0.55 * a * acesa), M.hexc(AMB_C, 0.0)], [0, 1]))
        c.drawCircle(*L, 90, p)
    c.drawCircle(*L, 16, M.paint(AMB_C, a))
    return L


# sombras: chão em GY; poste a 90 px/m, prédio a 18 px/m (mesmo formato 2 : 3)
GY = 860
P0, PT, PS = (180, GY), (180, GY - 2 * 90), (180 + 3 * 90, GY)
Q0, QT, QS = (690, GY), (690, GY - 20 * 18), (690 + 30 * 18, GY)
assert abs((PT[1] - GY) / (PS[0] - P0[0]) - (QT[1] - GY) / (QS[0] - Q0[0])) < 1e-9


def cena_sombra(c, t, tp, ts, tr, tq, tm=None, labs=None, tx=None, a=1.0):
    """poste (tp), sombra (ts), raio (tr), prédio com sombra e raio (tq). labs = instantes de (2 m, 3 m, x, 30 m)"""
    chao(c, 80, 1300, GY, ep(t, tp - 0.3, 0.4) * a)
    E.foco(c, t, tp - 0.3, 0.5, lambda f: sol(c, 120, 170, 40, f * a))
    poste(c, t, tp, P0, PT, a)
    sombra(c, t, ts, P0, PS, a)
    raio(c, t, tr, PT, PS, 200, a)
    if t >= tq:
        predio(c, t, tq, Q0[0], GY, GY - QT[1], 110, a)
        sombra(c, t, tq + 0.4, Q0, QS, a)
        raio(c, t, tq + 0.8, QT, QS, 300, a)
    if tm is not None:
        reto(c, t, tm, P0, PT, PS, TINTA2, 30, a)
        reto(c, t, tm, Q0, QT, QS, TINTA2, 40, a)
    if labs:
        l2, l3, lx, l30 = labs
        if l2 is not None:
            E.foco(c, t, l2, 0.4, lambda f: E.escreve(c, "2 m", P0[0] - 150, (P0[1] + PT[1]) / 2 + 20, 56, "g", COR, f * a))
        if l3 is not None:
            E.foco(c, t, l3, 0.4, lambda f: centro(c, "3 m", (P0[0] + PS[0]) / 2, GY + 70, 56, "g", AMBAR, f * a))
        if lx is not None:
            def lx_(s, cor, f):
                E.escreve(c, s, Q0[0] - 110 - 30 - E.larg(s, "g", 64), (Q0[1] + QT[1]) / 2 + 22, 64, "g", cor, f * a)
            if tx is None:
                E.foco(c, t, lx, 0.4, lambda f: lx_("x", COR, f))
            else:
                E.saida(c, t, tx, lambda: E.foco(c, t, lx, 0.4, lambda f: lx_("x", COR, f)))
                E.foco(c, t, tx, 0.4, lambda f: lx_("20 m", CERTO, f))
        if l30 is not None:
            E.foco(c, t, l30, 0.4, lambda f: centro(c, "30 m", (Q0[0] + QS[0]) / 2, GY + 70, 56, "g", AMBAR, f * a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        cena_sombra(c, t, ka, ka + 0.6, ka + 1.0, kb, labs=(ka + 0.8, ka + 1.6, kc - 1.4, kb + 1.2), tx=kc)
        E.frase(c, t, ka + 0.3, [("poste", "g", 70)] + ps("de", "i", 60) + [("2 m", "g", 70, COR)], XT, 280, "center", 0.12)
        E.frase(c, t, ka + 1.6, ps("sombra de", "i", 60) + [("3 m", "g", 70, AMBAR)], XT, 370, "center", 0.12)
        E.frase(c, t, kb, [("prédio:", "g", 70)], XT, 500, "center")
        E.frase(c, t, kb + 0.6, ps("sombra de", "i", 60) + [("30 m", "g", 70, AMBAR)], XT, 590, "center", 0.12)
        E.frase(c, t, lerp(kb, kc, 0.5), ps("sem subir no prédio", "i", 56), XT, 720, "center", 0.12)
        bola_txt(c, t, kc, "20 m", XT, 880, 95, 64, CERTO)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("alturas", "g", 104, COR)] + ps("pela sombra", "i", 84), XE, 450, passo=0.14)
        E.frase(c, t, tb, ps("e triângulos", "i", 84), XE, 600, passo=0.14)
        E.frase(c, t, tb + 0.6, [("encaixados", "g", 104, COR)], XE, 730, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 820
    itens = (("s03.b", "dois ângulos iguais", "triângulos semelhantes"), ("s03.c", "lado correspondente", "de frente para o mesmo ângulo"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 160)
    py = lerp(420, 700, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 920, "left", 0.12)


# ---------------- sombra ----------------
def b_sombra(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    cena_sombra(c, t, a4, b4, c4, d4, tm=a5, labs=(a6, a6 + 0.3, b6 + 1.0, a6 + 0.6), tx=d6)
    # o poste e a sombra acendem na fala
    brilho(c, P0, PT, COR, ep(t, a4, 0.3) * (1 - ep(t, b4 + 0.6, 0.4)))
    brilho(c, P0, PS, AMBAR, ep(t, b4, 0.3) * (1 - ep(t, c4 + 0.6, 0.4)))
    # raios paralelos: pulsam juntos
    k = ep(t, b5, 0.3) * (1 - ep(t, c5 + 0.5, 0.4))
    if k > 0:
        for topo, ponta, ex in ((PT, PS, 200), (QT, QS, 300)):
            ux, uy = E._uni(*ponta, *topo)
            M.line(c, topo[0] + ux * ex, topo[1] + uy * ex, *ponta, AMB_C, 0.5 * k, 16)
    marca(c, t, c5, PS, P0, PT, 1, COR, 60)
    marca(c, t, c5 + 0.3, QS, Q0, QT, 1, COR, 80)
    # o par de cada fração acende
    if t >= C["s06"]:
        k = ep(t, a6, 0.3) * (1 - ep(t, c6, 0.4))
        brilho(c, P0, PT, COR, k); brilho(c, Q0, QT, COR, k)
        brilho(c, P0, PS, AMBAR, k); brilho(c, Q0, QS, AMBAR, k)

    def quatro():
        E.frase(c, t, C["s04"] + 0.2, ps("onde estão os", "i", 54) + [("triângulos?", "g", 60, COR)], XT, 220, "center", 0.12)
        E.frase(c, t, a4, [("poste", "g", 64, COR)] + ps("em pé", "i", 58), XT, 380, "center", 0.12)
        E.frase(c, t, b4, [("sombra", "g", 64, AMBAR)] + ps("no chão", "i", 58), XT, 480, "center", 0.12)
        E.frase(c, t, c4, [("raio de sol", "g", 64, AMBAR)], XT, 580, "center")
        E.frase(c, t, c4 + 0.8, ps("liga as pontas", "i", 56), XT, 660, "center", 0.12)
        E.frase(c, t, d4, ps("com o prédio,", "i", 58) + [("igual", "g", 64)], XT, 800, "center", 0.12)
    E.saida(c, t, C["s05"] - 0.1, quatro)
    if C["s05"] - 0.1 <= t < C["s06"]:
        def cinco():
            E.frase(c, t, a5, [("ângulo reto", "g", 64, TINTA2)] + ps("no pé", "i", 58), XT, 260, "center", 0.12)
            E.frase(c, t, b5, ps("raios", "i", 58) + [("paralelos", "g", 66, AMBAR)], XT, 400, "center", 0.12)
            E.frase(c, t, c5, ps("mesma", "i", 58) + [("inclinação", "g", 66, COR)], XT, 500, "center", 0.12)
            E.foco(c, t, d5, 0.5, lambda a: E.pilula(c, "2 ângulos: semelhantes", XT, 680, 44, "g", a=a, cor=E.SOBRE))
        E.saida(c, t, C["s06"] - 0.1, cinco)
    if t >= C["s06"]:
        E.frase(c, t, a6, [("altura", "g", 64, COR)] + ps("sobre", "i", 56) + [("sombra", "g", 64, AMBAR)], XT, 220, "center", 0.12)
        prop(c, t, b6, "2", "3", "x", "30", XT, 380, 100, cores=(COR, AMBAR, COR, AMBAR), t1=b6 + 1.4)
        if t >= c6:
            cruz(c, t, c6, c6 + 0.5, XT, 380, 100, wa=50, wb=70)
        fcen(c, t, c6, "3x = 2 · 30 = 60", XT, 660, 72)
        fcen(c, t, d6, "x = 60 ÷ 3", XT - 110, 800, 70)
        bola_txt(c, t, d6 + 0.6, "20 m", XT + 170, 775, 80, 54, CERTO)


# ---------------- encaixados ----------------
EB, EC = (130, 880), (790, 880)
EA = (330, 880 - math.sqrt(495 ** 2 - 200 ** 2))
EM = (EA[0] + (EB[0] - EA[0]) / 3, EA[1] + (EB[1] - EA[1]) / 3)
EN = (EA[0] + (EC[0] - EA[0]) / 3, EA[1] + (EC[1] - EA[1]) / 3)
EG = centroide((EA, EB, EC))
assert abs(math.dist(EM, EN) - 220) < 1e-6 and abs(math.dist(EA, EB) - 495) < 1e-6
DESL = (650, -40)


def mais(P, d):
    return P[0] + d[0], P[1] + d[1]


def seta_par(c, P, Q, k=0.5, a=1.0, cor=TINTA):
    if a <= 0:
        return
    x, y = lerp(P[0], Q[0], k), lerp(P[1], Q[1], k)
    ux, uy = E._uni(*P, *Q)
    for s in (1, -1):
        M.line(c, x - ux * 20 + uy * 16 * s, y - uy * 20 - ux * 16 * s, x, y, cor, a, 5)


def fig_enc(c, t, t0, tmn=None, labs=None, angs=None, a=1.0):
    """ABC com MN paralelo a BC. labs = instantes de (AM 3, MB 6, MN 4, BC ?); angs = instante dos ângulos"""
    triang(c, t, t0, (EA, EB, EC), "ABC", a=a)
    tmn = t0 + 0.6 if tmn is None else tmn
    if t >= tmn:
        M.line(c, *EM, lerp(EM[0], EN[0], ease_io(prog(t, tmn, 0.6))), EM[1], TINTA, a, 6)
        k = ep(t, tmn + 0.4, 0.3) * a
        for P_, s, dx in ((EM, "M", -52), (EN, "N", 50)):
            c.drawCircle(*P_, 10 * k, M.paint(TINTA, k))
            centro(c, s, P_[0] + dx, P_[1] + 20, 54, "g", TINTA, k)
        seta_par(c, EM, EN, 0.55, k); seta_par(c, EB, EC, 0.55, k)
    if labs:
        l3, l6, l4, lbc = labs
        if l3 is not None:
            lab(c, t, l3, EA, EM, "3", EG, COR, 56, 18)
        if l6 is not None:
            lab(c, t, l6, EM, EB, "6", EG, TINTA2, 56, 18)
        if l4 is not None:
            E.foco(c, t, l4, 0.4, lambda f: centro(c, "4", (EM[0] + EN[0]) / 2, EM[1] - 18, 54, "g", AMBAR, f * a))
        if lbc is not None:
            if isinstance(lbc, tuple):
                t1, t2 = lbc
                E.saida(c, t, t2, lambda: lab(c, t, t1, EB, EC, "x", EG, AMBAR, 60, 20))
                lab(c, t, t2, EB, EC, "12", EG, CERTO, 60, 20)
            else:
                lab(c, t, lbc, EB, EC, "x", EG, AMBAR, 60, 20)
    if angs is not None:
        marca(c, t, angs, EA, EB, EC, 0, TINTA2, 64, alfa=0.3, a=a)
        marca(c, t, angs + 0.6, EM, EA, EN, 1, COR, 50, a=a)
        marca(c, t, angs + 0.9, EB, EA, EC, 1, COR, 60, a=a)


def b_encaixados(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8 = (C[f"s08.{k}"] for k in "abc")
    a9, b9, c9 = (C[f"s09.{k}"] for k in "abc")
    a10, b10, c10 = (C[f"s10.{k}"] for k in "abc")
    fig_enc(c, t, a7, b7, labs=(c7, c7 + 1.2, d7, (lerp(d7, C["s07.end"], 0.6), c10)), angs=a8 + 0.6 if t >= a8 else None)
    # o pequeno, AMN, se destaca e depois sai do grande
    k = ep(t, a8, 0.4) * (1 - ep(t, C["s09"], 0.4))
    if k > 0:
        path = skia.Path(); path.addPoly([EA, EM, EN], True)
        c.drawPath(path, M.paint(E.COR, 0.25 * k))
    if t >= a9:
        q = ease_io(prog(t, a9, 1.0))
        d = (DESL[0] * q, DESL[1] * q)
        A2, M2, N2 = mais(EA, d), mais(EM, d), mais(EN, d)
        path = skia.Path(); path.addPoly([A2, M2, N2], True)
        c.drawPath(path, M.paint(E.COR, 0.12))
        for P_, Q_ in ((A2, M2), (M2, N2), (N2, A2)):
            M.line(c, *P_, *Q_, TINTA, 1, 6)
        G2 = centroide((A2, M2, N2))
        for P_, s in ((A2, "A"), (M2, "M"), (N2, "N")):
            ux, uy = E._uni(*G2, *P_)
            centro(c, s, P_[0] + ux * 46, P_[1] + uy * 46 + 20, 50, "g", TINTA, ep(t, a9 + 0.8, 0.3))
        lab(c, t, b9, A2, M2, "3", G2, COR, 56, 18)
        E.foco(c, t, b9 + 1.2, 0.4, lambda f: centro(c, "4", (M2[0] + N2[0]) / 2, M2[1] + 70, 56, "g", AMBAR, f))
        brilho(c, EA, EB, COR, ep(t, c9, 0.4) * (1 - ep(t, C["s10"] + 1.0, 0.4)))

    def sete():
        E.frase(c, t, a7, ps("um", "i", 60) + [("encaixado", "g", 70, COR)] + ps("no outro", "i", 60), XT, 240, "center", 0.12)
        E.frase(c, t, b7, [("MN", "g", 66, AMBAR)] + ps("paralelo a", "i", 58) + [("BC", "g", 66, AMBAR)], XT, 360, "center", 0.12)
        E.frase(c, t, c7, [("AM = 3", "g", 60, COR), ("MB = 6", "g", 60, TINTA2)], XT, 500, "center", 0.3)
        E.frase(c, t, d7, [("MN = 4", "g", 60, AMBAR)], XT, 600, "center")
        E.frase(c, t, lerp(d7, C["s07.end"], 0.6), [("BC", "g", 76, AMBAR), ("= ?", "g", 76)], XT, 760, "center", 0.12)
    E.saida(c, t, C["s08"] - 0.1, sete)
    if C["s08"] - 0.1 <= t < C["s09"]:
        def oito():
            E.frase(c, t, a8, [("AMN", "g", 66, COR)] + ps("e", "i", 58) + [("ABC:", "g", 66)], XT, 260, "center", 0.12)
            E.frase(c, t, a8 + 1.2, ps("o mesmo", "i", 58) + [("ângulo A", "g", 64, TINTA2)], XT, 350, "center", 0.12)
            E.frase(c, t, b8, [("ângulo M = ângulo B", "g", 60, COR)], XT, 500, "center")
            E.frase(c, t, b8 + 1.2, ps("correspondentes", "i", 54, TINTA2), XT, 580, "center", 0.12)
            E.foco(c, t, c8, 0.5, lambda a: E.pilula(c, "semelhantes", XT, 740, 64, "g", a=a, cor=E.SOBRE))
        E.saida(c, t, C["s09"] - 0.1, oito)
    if C["s09"] - 0.1 <= t < C["s10"]:
        def nove():
            E.frase(c, t, a9, [("separe", "g", 72, COR)] + ps("os triângulos", "i", 56), 1500, 720, "center", 0.12)
            E.frase(c, t, c9, ps("no grande, o lado", "i", 54) + [("AB inteiro:", "g", 58, COR)], 1500, 840, "center", 0.12)
            fcen(c, t, c9 + 0.8, "3 + 6 = 9", 1500, 950, 66, COR)
        E.saida(c, t, C["s10"] - 0.1, nove)
    if t >= C["s10"]:
        X = 1600
        prop(c, t, a10, "3", "9", "4", "x", X, 220, 88, cores=(COR, COR, AMBAR, AMBAR), t1=a10 + 1.3, dx=150)
        if t >= b10:
            cruz(c, t, b10, b10 + 0.5, X, 220, 88, dx=150)
        fcen(c, t, b10, "3x = 9 · 4 = 36", 1520, 720, 64)
        fcen(c, t, c10, "x = 36 ÷ 3", 1420, 860, 64)
        bola_txt(c, t, c10 + 0.6, "12", 1730, 835, 70, 76, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12 = C["s12.a"], C["s12.b"]
    t0 = C["s11"]
    fig_enc(c, t, t0 - 0.6, t0 - 0.6, labs=(t0 - 0.4, t0 - 0.4, t0 - 0.4, t0 - 0.4))
    brilho(c, EM, EB, ERRADO, ep(t, a11 + 0.5, 0.4))
    if t >= b12:
        k = ep(t, b12, 0.4)
        for P_, Q_ in ((EA, EB), (EB, EC), (EC, EA)):
            brilho(c, P_, Q_, COR, k, 22)
        path = skia.Path(); path.addPoly([EA, EM, EN], True)
        c.drawPath(path, M.paint(E.COR, 0.3 * k))
    E.frase(c, t, t0 + 0.2, [("cuidado", "g", 84, ERRADO)], XT, 170, "center")

    def onze():
        E.frase(c, t, a11, ps("o", "i", 58) + [("pedaço", "g", 64, ERRADO)] + ps("no lugar do", "i", 56), XT, 280, "center", 0.12)
        E.frase(c, t, a11 + 1.2, [("lado inteiro", "g", 68)], XT, 370, "center")
        prop(c, t, b11, "3", "6", "4", "x", XT, 520, 96, cores=(COR, ERRADO, AMBAR, AMBAR), t1=b11 + 1.3)
        fcen(c, t, c11, "x = 8", XT - 70, 800, 84, ERRADO)
        E.foco(c, t, c11 + 0.4, 0.4, lambda a: E.selo(c, XT + 130, 772, 52, False, a))
    E.saida(c, t, C["s12"] - 0.1, onze)
    if t >= C["s12"]:
        E.frase(c, t, a12, ps("o 6 é só o", "i", 56), XT, 290, "center", 0.12)
        E.frase(c, t, a12 + 0.6, [("pedaço de baixo", "g", 62, ERRADO)], XT, 370, "center")
        E.frase(c, t, a12 + 1.6, ps("não é lado de nenhum triângulo", "i", 46, TINTA2), XT - 20, 450, "center", 0.1)
        E.frase(c, t, b12, ps("compare", "i", 58), XT, 600, "center")
        E.foco(c, t, b12 + 0.5, 0.5, lambda a: E.pilula(c, "triângulo inteiro", XT, 700, 58, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, b12 + 0.9, ps("com", "i", 58), XT, 800, "center")
        E.foco(c, t, b12 + 1.2, 0.5, lambda a: E.pilula(c, "triângulo inteiro", XT, 890, 58, "g", a=a, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
AY = 880
TRI3 = (((150, AY), 55, 2, 3), ((470, AY), 26, 8, 12), ((880, AY), 16, 20, 30))
VERDE_C = "#7EE2A0"


def tri_sombra(c, t, t0, base, esc, h, s, a=1.0):
    """objeto em pé (h metros) com sombra (s metros) na escala esc, no palco"""
    if t < t0 or a <= 0:
        return
    k = ep(t, t0, 0.5) * a
    topo = (base[0], base[1] - h * esc)
    ponta = (base[0] + s * esc, base[1])
    M.line(c, *base, *topo, BR, k, 10)
    M.line(c, *base, *ponta, "#8C8AA8", k, 14)
    M.line(c, *topo, *ponta, AMB_C, k, 5, dash=[14, 10])


def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    LIL = CLARO
    M.line(c, 80, AY, 1840, AY, "#5A5878", ep(t, C["s13"], 0.4), 4)
    for (base, esc, h, s), t0 in zip(TRI3, (b13, c13, c13 + 0.4)):
        tri_sombra(c, t, t0, base, esc, h, s)
    (b1, e1, h1, s1), (b2, e2, h2, s2), (b3, e3, h3, s3) = TRI3
    E.foco(c, t, b13 + 0.3, 0.4, lambda f: (E.escreve(c, "2 m", b1[0] - 110, b1[1] - h1 * e1 / 2 + 20, 48, "g", LIL, f),
                                            centro(c, "3 m", b1[0] + s1 * e1 / 2, AY + 60, 52, "g", AMB_C, f)))
    E.foco(c, t, b14, 0.4, lambda f: centro(c, "12 m", b2[0] + s2 * e2 / 2, AY + 60, 52, "g", AMB_C, f))
    E.foco(c, t, b14 + 2.0, 0.4, lambda f: E.escreve(c, "8 m", b2[0] - 120, b2[1] - h2 * e2 / 2 + 20, 52, "g", VERDE_C, f))
    E.foco(c, t, a14, 0.4, lambda f: centro(c, "30 m", b3[0] + s3 * e3 / 2, AY + 60, 52, "g", AMB_C, f))
    E.foco(c, t, a14 + 2.4, 0.4, lambda f: E.escreve(c, "20 m", b3[0] - 145, b3[1] - h3 * e3 / 2 + 20, 52, "g", VERDE_C, f))

    def treze_quatorze():
        E.frase(c, t, a13, ps("calcule a", "i", 66, CLARO) + [("razão da hora", "g", 74, BR)], W / 2, 170, "center", 0.12)
        E.frase(c, t, b13 + 0.6, [("altura =", "g", 60, LIL)], W / 2 - 200, 290, "center")
        E.foco(c, t, b13 + 0.9, 0.4, lambda f: E.formula(c, "f{2}{3}", W / 2 - 20, 296, 64, "g", BR, f, "center"))
        E.frase(c, t, b13 + 1.2, ps("da sombra", "i", 60, AMB_C), W / 2 + 180, 290, "center", 0.12)
        E.frase(c, t, a14, [("30 ÷ 3 = 10", "g", 54, BR), ("→", "g", 54, CLARO), ("10 · 2 = 20 m", "g", 54, VERDE_C)], W / 2 + 330, 420, "center", 0.2)
        E.frase(c, t, b14, [("12 ÷ 3 = 4", "g", 54, BR), ("→", "g", 54, CLARO), ("4 · 2 = 8 m", "g", 54, VERDE_C)], W / 2 + 330, 500, "center", 0.2)
        E.foco(c, t, c14, 0.5, lambda a: E.pilula(c, "uma razão, várias respostas", W / 2, 1000, 48, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s15"] - 0.1, treze_quatorze)
    if t < C["s15"]:
        return
    # outra hora: o sol mais baixo, a sombra do prédio cresce e a razão muda
    if t >= b15:
        k = ep(t, b15, 0.5)
        topo = (b3[0], b3[1] - h3 * e3)
        ponta = (b3[0] + s3 * e3 * 1.45, b3[1])
        M.line(c, *topo, lerp(topo[0], ponta[0], k), lerp(topo[1], ponta[1], k), "#FF6B6B", k, 5, dash=[14, 10])
        M.line(c, b3[0] + s3 * e3, AY, lerp(b3[0] + s3 * e3, ponta[0], k), AY, "#FF6B6B", k, 14)
    E.frase(c, t, a15, ps("no mesmo instante:", "i", 60, CLARO) + [("mesma inclinação", "g", 66, AMB_C)], W / 2, 200, "center", 0.12)
    E.frase(c, t, b15, ps("horas diferentes?", "i", 60, CLARO) + [("não vale", "g", 66, "#FF6B6B")], W / 2, 330, "center", 0.12)
    E.frase(c, t, c15, ps("o sol muda:", "i", 60, CLARO) + [("a razão muda", "g", 66, BR)], W / 2 + 330, 470, "center", 0.12)


# ---------------- questão ----------------
LB = (330, 880)                                   # pé do poste
LT = (330, 880 - 4 * 140)                         # a lâmpada, no alto do poste (4 m a 140 px/m)
HB = (LB[0] + 3 * 140, 880)                         # pés da pessoa (a 3 m do pé da lâmpada)
HH = 1.6 * 140
HS = (HB[0] + 2 * 140, 880)                       # ponta da sombra (2 m)


def cena_q(c, t, t0, a=1.0):
    """poste com a lâmpada (a 4 m, em cima do x = 200) e a pessoa; devolve o ponto da lâmpada"""
    chao(c, 200, 1250, 880, ep(t, t0, 0.4) * a)
    L = lampada(c, (LT[0], 880), LT, ep(t, t0, 0.5) * a)
    pessoa(c, HB[0], 880, HH, TINTA2, ep(t, t0 + 0.4, 0.5) * a)
    return L


def b_questao(c, t, C, b):
    a16, b16, c16, d16 = (C[f"s16.{k}"] for k in "abcd")
    rel = C["s17.a"]
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XT, 170, "center", 0.12)
    if t >= a16:
        cena_q(c, t, a16)
        E.foco(c, t, a16 + 1.4, 0.4, lambda f: E.escreve(c, "1,60 m", HB[0] - 230, 880 - HH / 2 + 20, 54, "g", COR, f))
    sombra(c, t, c16, HB, HS)
    cota(c, t, b16, LB, HB, "3 m", -1, TINTA2, 70, 54)
    E.foco(c, t, c16 + 0.4, 0.4, lambda f: centro(c, "2 m", (HB[0] + HS[0]) / 2, 960, 54, "g", AMBAR, f))
    E.foco(c, t, d16, 0.4, lambda f: E.escreve(c, "?", LT[0] - 90, (LB[1] + LT[1]) / 2 + 30, 96, "g", ERRADO, f))

    def lado():
        E.frase(c, t, a16, [("pessoa", "g", 62)] + ps("de", "i", 56) + [("1,60 m", "g", 62, COR)], XT, 340, "center", 0.12)
        E.frase(c, t, b16, ps("a", "i", 56) + [("3 m", "g", 62)] + ps("do poste", "i", 56), XT, 440, "center", 0.12)
        E.frase(c, t, c16, ps("sombra de", "i", 56) + [("2 m", "g", 62, AMBAR)], XT, 540, "center", 0.12)
    E.saida(c, t, rel - 0.5, lado)
    E.frase(c, t, d16, ps("a que altura está a", "i", 56), XT, 860, "center", 0.12)
    E.frase(c, t, d16 + 1.0, [("lâmpada?", "g", 70, COR)], XT, 950, "center")
    E.relogio(c, t, rel, XT, 420, 150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a18, b18, c18, d18 = (C[f"s18.{k}"] for k in "abcd")
    a19, b19 = C["s19.a"], C["s19.b"]
    a20, b20, c20, d20 = (C[f"s20.{k}"] for k in "abcd")
    t0 = C["s18"]
    L = cena_q(c, t, t0 - 0.6)
    sombra(c, t, t0 - 0.4, HB, HS)
    HT = (HB[0], 880 - HH)
    LP = (L[0], 880)                               # pé da vertical da lâmpada
    assert abs((L[1] - 880) / (L[0] - HS[0]) - (HT[1] - 880) / (HB[0] - HS[0])) < 1e-6
    # o raio sai da lâmpada, passa pela cabeça e chega na ponta da sombra
    if t >= b18:
        q = ease_io(prog(t, b18, 1.0))
        M.line(c, *L, lerp(L[0], HS[0], q), lerp(L[1], HS[1], q), AMBAR, 1, 5, dash=[16, 10])
    TP = (HS, HB, HT)
    TG = (HS, LP, L)
    if t >= c18:
        k = ep(t, c18, 0.4)
        path = skia.Path(); path.addPoly(list(TG), True)
        c.drawPath(path, M.paint(E.COR, 0.08 * k))
        path = skia.Path(); path.addPoly(list(TP), True)
        c.drawPath(path, M.paint(E.COR, 0.22 * k))
        M.line(c, *L, *LP, TINTA2, k, 4, dash=[10, 8])
        marca(c, t, c18 + 0.4, HS, HB, HT, 1, COR, 70)
    reto(c, t, d18, HB, HT, HS, TINTA2, 30)
    reto(c, t, d18 + 0.3, LP, L, HS, TINTA2, 34)
    E.foco(c, t, a19, 0.4, lambda f: E.escreve(c, "1,6", HB[0] - 150, 880 - HH / 2 + 20, 54, "g", COR, f))
    E.foco(c, t, a19 + 1.0, 0.4, lambda f: centro(c, "2", (HB[0] + HS[0]) / 2, 950, 54, "g", AMBAR, f))
    E.saida(c, t, c20, lambda: E.foco(c, t, lerp(a19, b19, 0.6), 0.4, lambda f: E.escreve(c, "x", LP[0] - 160, (LP[1] + L[1]) / 2 + 30, 76, "g", COR, f)))
    E.foco(c, t, c20, 0.4, lambda f: E.escreve(c, "4 m", LP[0] - 230, (LP[1] + L[1]) / 2 + 30, 64, "g", CERTO, f))
    cota(c, t, b19, LP, HS, "2 + 3 = 5", -1, AMBAR, 90, 54)
    if t >= d20:
        k = ep(t, d20, 0.4)
        M.line(c, LP[0] + 10, 845, HB[0] - 60, 845, ERRADO, k, 6)
        centro(c, "só 3 m?", (LP[0] + HB[0]) / 2 - 20, 825, 46, "b", ERRADO, k)

    def dezoito():
        E.frase(c, t, a18, ps("luz de", "i", 54) + [("um ponto só", "g", 60, AMBAR)], XT, 220, "center", 0.12)
        E.frase(c, t, a18 + 1.2, ps("a razão da hora", "i", 52) + [("não serve", "g", 58, ERRADO)], XT, 310, "center", 0.12)
        E.frase(c, t, b18, ps("o raio passa pela", "i", 52) + [("cabeça", "g", 58, AMBAR)], XT, 450, "center", 0.12)
        E.frase(c, t, c18, [("encaixados", "g", 70, COR)], XT, 590, "center")
        E.frase(c, t, d18, ps("ângulo comum", "i", 54), XT, 700, "center", 0.12)
        E.frase(c, t, d18 + 0.6, ps("e", "i", 54) + [("ângulo reto", "g", 58, TINTA2)], XT, 780, "center", 0.12)
        E.foco(c, t, d18 + 1.4, 0.5, lambda a: E.pilula(c, "semelhantes", XT, 900, 60, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s19"] - 0.1, dezoito)
    if C["s19"] - 0.1 <= t < C["s20"]:
        def dezenove():
            E.frase(c, t, C["s19"], [("separe", "g", 76, COR)], XT, 240, "center")
            E.frase(c, t, a19, ps("pequeno:", "i", 58) + [("1,6", "g", 64, COR), ("e", "i", 56), ("2", "g", 64, AMBAR)], XT, 400, "center", 0.12)
            E.frase(c, t, lerp(a19, b19, 0.6), ps("grande:", "i", 58) + [("x", "g", 64, COR), ("e", "i", 56), ("2 + 3 = 5", "g", 64, AMBAR)], XT, 520, "center", 0.12)
        E.saida(c, t, C["s20"] - 0.1, dezenove)
    if t >= C["s20"]:
        prop(c, t, a20, "1,6", "2", "x", "5", XT, 300, 96, cores=(COR, AMBAR, COR, AMBAR), t1=a20 + 1.5, dx=180)
        if t >= b20:
            cruz(c, t, b20, b20 + 0.5, XT, 300, 96, dx=180, wa=80, wb=50)
        fcen(c, t, b20, "2x = 1,6 · 5 = 8", XT, 560, 66)
        fcen(c, t, c20, "x = 8 ÷ 2", XT - 120, 690, 66)
        bola_txt(c, t, c20 + 0.6, "4 m", XT + 150, 665, 74, 56, CERTO)
        E.frase(c, t, d20, ps("com 3 m:", "i", 56) + [("2,40 m", "g", 64, ERRADO)], XT - 50, 860, "center", 0.12)
        E.foco(c, t, d20 + 0.8, 0.4, lambda a: E.selo(c, XT + 220, 838, 46, False, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s21.a", "em pé e sombra:", "triângulos semelhantes"), ("s21.b", "encaixados:", "separe e use o lado inteiro"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 420 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 30, 56, a=a),
                                                         centro(c, str(i + 1), 240, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "i", 64)], 340, y - 20)
            E.frase(c, t, C[k] + 0.4, [(l2, "g", 66)], 340, y + 70)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s22.a"], [("praticando", "g", 120, COR)], XE, 440)
    E.frase(c, t, C["s22.a"] + 0.6, ps("Tales e semelhança", "i", 76), XE, 560, passo=0.12)
    E.frase(c, t, C["s22.b"], ps("paralelas, bissetriz,", "i", 60), XE, 680, passo=0.1)
    E.frase(c, t, C["s22.b"] + 0.9, ps("sombras e", "i", 60) + [("encaixados", "g", 64)], XE, 770, passo=0.1)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1630, p), lerp(720, 425, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2 + 200, 950, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, sombra=b_sombra, encaixados=b_encaixados, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
