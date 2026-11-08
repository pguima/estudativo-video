"""Visual — Estudativo · MAT-ESP-011: pirâmide, volume.
Mesma linguagem da trilha (MAT-ESP-001 a 010): sólidos do kit com as escondidas tracejadas, o elemento da vez na cor da matéria,
faces em par índigo/cinza, resposta na esfera.
- A CAIXA E A PIRÂMIDE de mesma base e mesma altura ficam lado a lado, na mesma vista (E.prisma e E.piramide, vista (−24, 18)).
  A AREIA (areia(), a mancha do sólido cheia até um nível) passa da pirâmide para a caixa três vezes, e a caixa sobe um terço por vez.
- O CUBO CORTADO EM 3 PIRÂMIDES (cubo3()): três pirâmides com o vértice no mesmo canto de cima, montadas com E._solido na
  perspectiva cavaleira de E.cubo; elas se afastam lado a lado. Cada uma tem a sua cor (COR, TINTA2, COR clara), a base pintada
  e a altura (uma aresta do cubo) em traço grosso.
- Altura da pirâmide = tracejado do vértice até o pé, com o quadradinho de ângulo reto; a aresta lateral inclinada, quando a fala
  diz que ela NÃO é a altura, fica em vermelho.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-011_piramide_volume.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("piramide", "terco", "quadrada", "triangular", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)  # a 2ª família pintada numa face de papel
AREIA = E.mix(E.COR, "#FFFFFF", 0.45)
VISTA = (-24, 18)
assert 6 ** 2 == 36 and 36 * 10 == 360 and 360 / 3 == 120 and 6 * 4 / 2 == 12 and 12 * 5 == 60 and 60 / 3 == 20
assert 36 / 3 == 12 and 12 * 10 == 120 and 25 * 8 == 200 and 200 % 3 != 0
assert 12 / 3 == 4 and 36 * 4 == 144 and 144 / 36 == 4 and 4 == 12 / 3


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)



# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com ² ou ³ vai na grotesca: a serifada não tem o expoente)"""
    return [(w, "g" if any(ch in w for ch in "²³√") else est, size * (0.92 if any(ch in w for ch in "²³√") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def face(c, pts, idx, a=1.0, cor=None, alfa_=0.42):
    if a <= 0:
        return
    p = skia.Path(); p.addPoly([pts[i] for i in idx], True)
    c.drawPath(p, M.paint(cor or E.COR, alfa_ * a))


def aresta(c, t, t0, P, Q, cor=None, largura=13, d=0.5, tracejada=False, a=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P, *Q, cor or E.COR, a, largura, dash=E.TRACO if tracejada else None, progress=p)


def reto(c, P, A, B, k=34, a=1.0, cor=None):
    """quadradinho de ângulo reto no vértice P, nas direções de P→A e P→B"""
    if a <= 0:
        return
    def un(Q):
        dx, dy = Q[0] - P[0], Q[1] - P[1]
        n = math.hypot(dx, dy) or 1
        return dx / n * k, dy / n * k
    u, v = un(A), un(B)
    path = skia.Path()
    path.moveTo(P[0] + u[0], P[1] + u[1]); path.lineTo(P[0] + u[0] + v[0], P[1] + u[1] + v[1]); path.lineTo(P[0] + v[0], P[1] + v[1])
    c.drawPath(path, M.paint(cor or TINTA, a, stroke=4))


def rotulo(c, t, t0, s, P, Q, n, size=56, cor=None, gap=20):
    """rótulo de um segmento PQ, afastado na direção n"""
    mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, s, mx, my, n[0], n[1], gap, size, "g", cor or COR, a))




# ================= peças desta aula =================
def alfa(c, a, fn):
    if a <= 0:
        return
    if a >= 0.999:
        fn()
        return
    p = skia.Paint(); p.setAlphaf(a)
    c.saveLayer(None, p); fn(); c.restore()


def vertice(c, t, t0, P, r=15, cor=None, a=1.0):
    """o vértice da vez: bolinha que salta (de MAT-ESP-001)"""
    k = ease_back(prog(t, t0, 0.35))
    if k > 0 and a > 0:
        c.drawCircle(P[0], P[1], r * k, M.paint(cor or E.COR, a))


def casco(pts):
    """o contorno convexo dos pontos (a silhueta de um sólido convexo na tela)"""
    P = sorted(set((round(x, 3), round(y, 3)) for x, y in pts))
    if len(P) < 3:
        return P
    cr = lambda o, a, b: (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, hi = [], []
    for p in P:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(P):
        while len(hi) >= 2 and cr(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    return lo[:-1] + hi[:-1]


def mancha(c, pts, cor, a):
    if a <= 0:
        return
    p = skia.Path(); p.addPoly(casco(pts), True)
    c.drawPath(p, M.paint(cor, a))


def areia_caixa(c, cx, cy, r, h, nivel, a=1.0):
    """a areia dentro do E.prisma de base quadrada até a fração nivel da altura (a mesma vista da pirâmide)"""
    if nivel <= 0 or a <= 0:
        return
    R, U, _ = E._vista_alta(*VISTA)
    base = E._base_regular(4, r)
    P0 = [E._proj((x, 0, z), R, U, cx, cy) for x, z in base]
    P1 = [E._proj((x, h * nivel, z), R, U, cx, cy) for x, z in base]
    mancha(c, P0 + P1, AREIA, 0.55 * a)
    p = skia.Path(); p.addPoly(P1, True)
    c.drawPath(p, M.paint(AREIA, 0.5 * a))


def areia_pir(c, pts, cheia, a=1.0):
    """a pirâmide cheia de areia (cheia = 0..1 é a força da cor)"""
    mancha(c, pts, AREIA, 0.6 * cheia * a)


def caixa_q(c, t, t0, cx, cy, r, h, **kw):
    return E.prisma(c, t, t0, cx, cy, 4, r, h, vista=VISTA, **kw)


def pir_q(c, t, t0, cx, cy, r, h, **kw):
    return E.piramide(c, t, t0, cx, cy, 4, r, h, vista=VISTA, **kw)


def altura_pir(c, t, t0, topo, pe, rot=None, cor=None, size=52, lado=1, ref=None):
    """a altura da pirâmide: tracejado do vértice até o pé, quadradinho e o rótulo"""
    aresta(c, t, t0, topo, pe, cor=cor, largura=7, tracejada=True)
    if t >= t0 + 0.4:
        reto(c, pe, ref or (pe[0] + 100, pe[1]), topo, k=26, a=ep(t, t0 + 0.4, 0.3), cor=cor or E.COR)
    if rot:
        E.foco(c, t, t0 + 0.4, 0.4, lambda q: E._cola(c, rot, pe[0], lerp(pe[1], topo[1], 0.45), lado, 0, 16, size, "g", cor or COR, q))


# o cubo cortado em 3 pirâmides com o vértice no canto de cima da frente, à esquerda (0, 1, 0)
_CUBO = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]
_PIRS = (((0, 1, 5, 4), 0), ((1, 2, 6, 5), 2), ((4, 5, 6, 7), 7))   # (base, o outro ponta da aresta que é a altura)
_CORES3 = (E.COR, TINTA2, E.mix(E.COR, "#FFFFFF", 0.5))


def cubo3(c, t, t0, x, y, a, sep=0.0, alvos=None, tb=None, th=None, rot_h=None, vis=(1, 1, 1)):
    """as 3 pirâmides do cubo de aresta a (px), (x, y) = canto de baixo à esquerda da frente. sep = 0 (juntas no cubo) a 1
    (cada uma no seu alvo, em fila). tb = instante das bases pintadas, th = das alturas. Devolve os pontos de cada uma"""
    vista = E._vista_obliqua()
    saida = []
    for k, (base, h_ponta) in enumerate(_PIRS):
        if vis[k] <= 0:
            continue
        ox, oy = (x, y) if not alvos else (lerp(x, alvos[k][0], sep), lerp(y, alvos[k][1], sep))
        V = [tuple(v * a for v in _CUBO[i]) for i in base] + [(0, a, 0)]
        F = [(0, 1, 2, 3), (0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4)]
        if vis[k] >= 0.999:
            pts = E._solido(c, t, t0, V, F, vista, ox, oy, _CORES3[k], 0.22)
        else:
            alfa(c, vis[k], lambda V=V, F=F, ox=ox, oy=oy, k=k: E._solido(c, t, t0, V, F, vista, ox, oy, _CORES3[k], 0.22))
            pts = [E._proj(v, *vista[:2], ox, oy) for v in V]
        if tb is not None:
            face(c, pts, (0, 1, 2, 3), ep(t, tb + 0.4 * k, 0.4) * vis[k], _CORES3[k], 0.55)
        if th is not None:
            Q = E._proj(tuple(v * a for v in _CUBO[h_ponta]), *vista[:2], ox, oy)
            aresta(c, t, th + 0.4 * k, pts[4], Q, cor=_CORES3[k] if k != 2 else E.COR, largura=11)
            if rot_h:
                E.foco(c, t, th + 0.4 * k + 0.3, 0.4, lambda q, P=pts[4], Q=Q, k=k: E._cola(c, rot_h, (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2, -1 if k == 0 else 0, 0 if k == 0 else -1, 16, 46, "g", COR, q))
        saida.append(pts)
    return saida


def pir_tri(c, t, t0, cx, cy, s, h, d=1.0, vista=(0, 30)):
    """pirâmide de base triangular (base 6, altura 4 do triângulo) e altura h (unidades x s px); (cx, cy) = meio da aresta da frente.
    pts: 0, 1 = aresta da frente; 2 = o canto de trás; 3 = o vértice. Devolve (pts, pé da altura do triângulo, pé da altura da pirâmide)"""
    vs = E._vista_alta(*vista)
    V = [(-3 * s, 0, 2 * s), (3 * s, 0, 2 * s), (-1.5 * s, 0, -2 * s), (-0.5 * s, h * s, 2 * s / 3)]
    F = [(0, 1, 2), (0, 1, 3), (1, 2, 3), (2, 0, 3)]
    pts = E._solido(c, t, t0, V, F, vs, cx, cy, None, 0.14, d=d)
    pe_t = E._proj((-1.5 * s, 0, 2 * s), vs[0], vs[1], cx, cy)
    pe_p = E._proj((-0.5 * s, 0, 2 * s / 3), vs[0], vs[1], cx, cy)
    return pts, pe_t, pe_p


def lateral_frente(pts, n, cy):
    return [i for i in range(n) if (pts[i][1] + pts[(i + 1) % n][1]) / 2 > cy]


# ---------------- gancho ----------------
PX, BX, GY, GR, GH = 480, 1060, 900, 190, 420   # a pirâmide e a caixa do gancho


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        caixa_q(c, t, a1 + 0.3, BX, GY, GR, GH)
        pts = pir_q(c, t, a1, PX, GY, GR, GH)
        E.foco(c, t, a1 + 0.6, 0.4, lambda q: (centro(c, "pirâmide", PX, GY + 120, 54, "g", COR, q), centro(c, "caixa", BX, GY + 120, 54, "g", TINTA, q)))
        E.frase(c, t, b1, ps("mesma", "i", 64) + [("base", "g", 68, COR)] + ps("e mesma", "i", 64) + [("altura", "g", 68, COR)], W / 2, 200, "center", 0.1)
        # a areia: 3 viagens da pirâmide para a caixa
        t_ini = b1 + 1.0
        T = max(1.5, (c1 - t_ini) / 3)
        nivel, cheia = 0.0, 0.0
        for k in range(3):
            u = prog(t, t_ini + k * T, T)
            if u <= 0:
                break
            cheia = min(1.0, u * 2.5) if u < 0.5 else 1 - ease_io((u - 0.5) * 2)
            nivel = (k + ease_io(max(0.0, (u - 0.5) * 2))) / 3
            if u >= 1:
                cheia = 0.0
        areia_pir(c, pts, cheia)
        areia_caixa(c, BX, GY, GR, GH, nivel)
        for k in range(3):
            tk = t_ini + (k + 1) * T - 0.2
            E.foco(c, t, tk, 0.3, lambda q, k=k: (E.bola(c, 1560, 420 + 130 * k, 40, a=q), centro(c, f"{k + 1}×", 1560, 440 + 130 * k, 44, "g", E.SOBRE, q)))
        E.frase(c, t, c1, [("3 vezes", "g", 80, COR)], 1560, 880, "center", 0.1)
        E.frase(c, t, c1 + 0.5, ps("certinho", "i", 60), 1560, 970, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), ps("o", "i", 100) + [("volume", "g", 110, COR)], XE, 490, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.55), ps("de qualquer", "i", 90) + [("pirâmide", "g", 100, COR)], XE, 630, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 940, 860
    itens = (("s03.b", "prisma: volume =", "área da base × altura"), ("s03.c", "quadrado: ℓ²", "triângulo: f{b · h}{2}"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 270 + i * 270
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 210, p, prog_=p)
        if i == 0:
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 58), x + 44, y + 84, "left", 0.1)
            E.frase(c, t, C[k] + 0.5, [(l2, "g", 60, COR)], x + 44, y + 166)
        else:
            E.formula_em(c, t, C[k] + 0.1, "quadrado: ℓ²", x + 44, y + 120, 60, "g", COR)
            E.formula_em(c, t, C[k] + 0.6, "triângulo: f{b · h}{2}", x + 440, y + 120, 60, "g", COR)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(440, 710, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.72), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 920, "left", 0.12)


# ---------------- o que é pirâmide ----------------
def b_piramide(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s04.{k}"] for k in "abcde")
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    cx, cy, r, h = 520, 900, 240, 480
    pts = pir_q(c, t, a4, cx, cy, r, h)
    if t >= b4:
        face(c, pts, (0, 1, 2, 3), ep(t, b4, 0.5), alfa_=0.5)
    if t >= c4:
        for k, i in enumerate(lateral_frente(pts, 4, cy)):
            face(c, pts, (i, (i + 1) % 4, 4), ep(t, c4 + 0.3 * k, 0.4), CINZA2, 0.55)
    if C["s04"] <= t < C["s05"]:
        vertice(c, t, d4, pts[4], r=18)
    if t >= a5:
        altura_pir(c, t, a5, pts[4], (cx, cy), "altura", lado=-1)
    if t >= c5:
        i = max(range(4), key=lambda i: pts[i][0])
        aresta(c, t, c5, pts[4], pts[i], cor=ERRADO, largura=10)
    X = 1080

    def que_e():
        E.frase(c, t, a4, [("pirâmide", "g", 96, COR)], X, 230, "left", 0.1)
        E.frase(c, t, b4, [("1 base só,", "g", 62, COR)] + ps("um polígono", "i", 58), X, 370, "left", 0.1)
        E.frase(c, t, c4, ps("faces laterais:", "i", 58) + [("triângulos", "g", 62, TINTA2)], X, 490, "left", 0.1)
        E.frase(c, t, d4, ps("que se encontram no", "i", 58) + [("vértice", "g", 62, COR)], X, 610, "left", 0.1)
        E.frase(c, t, e4, ps("base quadrada =", "i", 56) + [("quadrangular", "g", 60, COR)], X, 780, "left", 0.1)
    fase(c, t, C["s04"], C["s05"] - 0.1, que_e)
    if t < C["s05"] - 0.1:
        return
    E.frase(c, t, a5, [("altura", "g", 80, COR)] + ps("= do vértice até a base", "i", 60), X, 260, "left", 0.1)
    E.frase(c, t, b5, ps("em pé, por dentro,", "i", 60), X, 420, "left", 0.1)
    E.frase(c, t, b5 + 0.8, ps("em", "i", 60) + [("ângulo reto", "g", 64, COR)] + ps("com a base", "i", 60), X, 510, "left", 0.1)
    E.frase(c, t, c5, ps("não é a", "i", 62) + [("aresta inclinada", "g", 64, ERRADO)], X, 700, "left", 0.1)


# ---------------- por que um terço ----------------
ALVOS = ((200, 1000), (780, 1000), (1360, 1000))
CB = 270   # aresta do cubo (px)


def b_terco(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    a7, b7 = C["s07.a"], C["s07.b"]
    a8, b8 = C["s08.a"], C["s08.b"]
    X0, Y0 = 780, 1000

    def cubo():
        sep = ease_io(prog(t, b6 + 0.6, 1.6))
        cubo_on = 1 - ep(t, b6, 0.4)
        if cubo_on > 0:
            alfa(c, cubo_on, lambda: E.cubo(c, t, a6, X0, Y0, CB))
        vis = (ep(t, b6, 0.4),) * 3
        if t >= b6:
            cubo3(c, t, b6 - 0.9, X0, Y0, CB, sep, ALVOS, tb=c6, th=d6, rot_h="altura", vis=vis)
        A = (X0, Y0 - CB)
        if t < b6 + 0.6:
            vertice(c, t, a6 + 0.6, A, r=18)
        E.frase(c, t, a6, ps("um", "i", 62) + [("cubo", "g", 66, COR)] + ps("e um canto de cima", "i", 62), W / 2, 190, "center", 0.1)
        E.frase(c, t, b6, [("3 pirâmides iguais", "g", 66, COR)] + ps("com o vértice nesse canto", "i", 58), W / 2, 290, "center", 0.1)
        E.frase(c, t, c6, ps("bases: o chão e as duas paredes do lado oposto", "i", 52, TINTA2), W / 2, 380, "center", 0.08)
        E.frase(c, t, d6, ps("altura de cada uma:", "i", 56) + [("a aresta do cubo", "g", 58, COR)], W / 2, 470, "center", 0.1)
        E.frase(c, t, lerp(d6, C["s06.end"], 0.4), ps("são tortas: a altura cai sobre uma aresta", "i", 48, TINTA2), W / 2, 550, "center", 0.08)
    fase(c, t, C["s06"], C["s07"] - 0.1, cubo)
    if t < C["s07"] - 0.1:
        return

    def terco():
        cubo3(c, t, C["s07"] - 5, X0, Y0, CB, 1.0, ALVOS, tb=C["s07"] - 5)
        fcen(c, t, a7, "cada uma = f{1}{3} do cubo", W / 2, 300, 84, COR)
        E.frase(c, t, b7, ps("e vale para", "i", 60) + [("toda pirâmide", "g", 64, COR)], W / 2, 450, "center", 0.1)
        E.frase(c, t, b7 + 0.9, ps("um terço do prisma de mesma base e mesma altura", "i", 52, TINTA2), W / 2, 540, "center", 0.08)
    fase(c, t, C["s07"], C["s08"] - 0.1, terco)
    if t < C["s08"] - 0.1:
        return
    caixa_q(c, t, C["s08"], 1400, 930, 170, 380)
    pir_q(c, t, C["s08"] + 0.3, 1400, 930, 170, 380, cor=E.COR, preenche=0.3)
    fcen(c, t, a8, "V = f{área da base × altura}{3}", 700, 420, 84, COR)
    E.frase(c, t, b8, ps("a conta do", "i", 60) + [("prisma", "g", 64)] + ps(",", "i", 60) + [("÷ 3", "g", 70, COR)] + ps("no fim", "i", 60), 700, 650, "center", 0.1)


# ---------------- pirâmide de base quadrada ----------------
def b_quadrada(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    cx, cy, r, h = 480, 920, 200, 400
    caixa_q(c, t, d9, cx, cy, r, h)
    pts = pir_q(c, t, C["s09"], cx, cy, r, h)
    if t >= c9:
        face(c, pts, (0, 1, 2, 3), ep(t, c9, 0.5), alfa_=0.5)
    pir_q(c, t, 1e9, cx, cy, r, h, aresta="6", tm=a9, size=54)
    if t >= b9:
        altura_pir(c, t, b9, pts[4], (cx, cy), "10")
    X = 1320
    E.frase(c, t, a9, ps("base quadrada de lado", "i", 60) + [("6", "g", 64, COR)], X, 220, "center", 0.1)
    E.frase(c, t, b9, ps("altura", "i", 60) + [("10", "g", 64, COR)], X, 310, "center", 0.1)
    fcen(c, t, c9, "6² = 36", X, 460, 80)
    fcen(c, t, d9, "36 × 10 = 360", X, 600, 80, TINTA2)
    E.frase(c, t, d9 + 1.2, ps("o prisma", "i", 52, TINTA2), X, 680, "center", 0.1)
    fcen(c, t, e9, "360 ÷ 3", X - 200, 880, 80)
    bola_txt(c, t, e9 + 0.6, "120", X + 200, 860, 115, 72)


# ---------------- pirâmide de base triangular ----------------
def b_triangular(c, t, C, b):
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    s, hp = 85, 5
    cx, cy = 560, 860
    pts, pe_t, pe_p = pir_tri(c, t, C["s10"] + 0.2, cx, cy, s, hp)
    if t >= a0:
        face(c, pts, (0, 1, 2), ep(t, a0, 0.5), alfa_=0.45)
        E._medida_aresta(c, t, a0 + 0.3, pts[0], pts[1], "6", (0, 1), 54)
        dest = t >= b1 and t < C["s12"]
        aresta(c, t, a0 + 0.6, pe_t, pts[2], cor=TINTA2 if not dest else TINTA, largura=10 if dest else 6, tracejada=True)
        E.foco(c, t, a0 + 0.9, 0.4, lambda q: E._cola(c, "4", (pe_t[0] + pts[2][0]) / 2, (pe_t[1] + pts[2][1]) / 2, -1, 0, 14, 50, "g", TINTA2, q))
    if t >= c0:
        altura_pir(c, t, c0, pts[3], pe_p, "5", ref=pe_t)
    if t >= c1:
        aresta(c, t, c1, pe_p, pts[3], largura=12)
    X = 1330

    def conta():
        E.frase(c, t, C["s10"] + 0.2, ps("base", "i", 64) + [("triangular", "g", 68, COR)], X, 210, "center", 0.1)
        E.frase(c, t, a0, ps("triângulo de base", "i", 56) + [("6", "g", 60, COR)] + ps("e altura", "i", 56) + [("4", "g", 60, COR)], X, 310, "center", 0.1)
        fcen(c, t, b0, "f{6 × 4}{2} = 12", X, 450, 76)
        E.frase(c, t, c0, ps("pirâmide de altura", "i", 58) + [("5", "g", 64, COR)], X, 590, "center", 0.1)
        fcen(c, t, d0, "12 × 5 = 60", X, 710, 76, TINTA2)
        fcen(c, t, e0, "60 ÷ 3", X - 180, 900, 76)
        bola_txt(c, t, e0 + 0.6, "20", X + 200, 880, 100, 72)
    fase(c, t, C["s10"], C["s11"] - 0.1, conta)
    if t < C["s11"] - 0.1:
        return
    E.frase(c, t, a1, [("duas alturas:", "g", 74, COR)], X, 260, "center", 0.1)
    E.frase(c, t, b1, ps("a do triângulo da base,", "i", 58) + [("deitada", "g", 62)], X, 430, "center", 0.1)
    E.frase(c, t, c1, ps("a da pirâmide,", "i", 58) + [("em pé", "g", 62, COR)], X, 560, "center", 0.1)
    E.frase(c, t, lerp(c1, C["s11.end"], 0.5), ps("cada uma na sua conta", "i", 54, TINTA2), X, 700, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    cx, cy, r, h = 480, 920, 200, 400
    if t >= c2:
        caixa_q(c, t, c2, cx, cy, r, h, cor=ERRADO, preenche=0.18)
    pir_q(c, t, C["s12"], cx, cy, r, h, cor=E.COR, preenche=0.3)
    pir_q(c, t, 1e9, cx, cy, r, h, aresta="6", altura="10", tm=C["s12"] + 0.6, size=50)
    X = 1300
    E.frase(c, t, C["s12"] + 0.2, [("erro comum:", "g", 66, ERRADO)], X, 200, "center", 0.1)
    E.frase(c, t, a2, ps("esquecer o", "i", 62) + [("÷ 3", "g", 70, ERRADO)], X, 310, "center", 0.1)
    fcen(c, t, b2, "36 × 10 = 360", X, 470, 80, ERRADO)
    E.frase(c, t, c2, ps("360 é a", "i", 60) + [("caixa em volta", "g", 64, ERRADO)], X, 620, "center", 0.1)
    E.frase(c, t, d2, ps("a pirâmide cabe", "i", 60) + [("3 vezes", "g", 66, COR)] + ps("nela", "i", 60), X, 780, "center", 0.1)
    bola_txt(c, t, d2 + 0.6, "120", X, 920, 85, 60)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, C["s13"] + 0.2, ps("o", "i", 70, CLARO) + [("atalho", "g", 74, BR)], W / 2, 190, "center", 0.1)
        E.frase(c, t, a3, [("divida por 3 primeiro", "g", 76, BR)], W / 2, 310, "center", 0.1)
        fcen(c, t, a3 + 0.5, "f{36 × 10}{3}", W / 2, 560, 110, CLARO)
        if t >= b3:
            w = E.formula(None, "36", 0, 0, 110, "g", a=0)
            wt = E.formula(None, "36 × 10", 0, 0, 110, "g", a=0)
            p = ep(t, b3, 0.5)
            E.caixa_pontilhada(c, W / 2 - wt / 2 - 14, 455, w + 28, 100, p, CLARO, prog_=p)
            E.foco(c, t, b3 + 0.3, 0.4, lambda q: centro(c, "múltiplo de 3", W / 2 - wt / 2 + w / 2, 435, 40, "g", CLARO, q))
        fcen(c, t, c3, "36 ÷ 3 = 12", 640, 780, 84, BR)
        fcen(c, t, d3, "12 × 10", 1180, 780, 84, CLARO)
        bola_txt(c, t, d3 + 0.6, "120", 1560, 760, 100, 70)
        E.frase(c, t, lerp(d3, C["s13.end"], 0.55), ps("sem passar por 360", "i", 56, CLARO), W / 2, 960, "center", 0.1)
    fase(c, t, C["s13"], C["s14"] - 0.1, um)
    if t < C["s14"] - 0.1:
        return
    E.frase(c, t, C["s14"] + 0.2, ps("funciona porque", "i", 66, CLARO), W / 2, 190, "center", 0.1)
    E.frase(c, t, a4, ps("só vezes e dividido:", "i", 58, CLARO) + [("a ordem não muda", "g", 62, BR)], W / 2, 290, "center", 0.1)
    fcen(c, t, a4 + 1.2, "f{36 × 10}{3} = f{36}{3} × 10", W / 2, 450, 80, BR)
    E.foco(c, t, b4, 0.5, lambda a: E.selo(c, 360, 640, 46, False, a))
    E.frase(c, t, b4 + 0.1, ps("nenhum múltiplo de 3:", "i", 58, CLARO) + [("25 × 8", "g", 62, BR)], 430, 662, "left", 0.1)
    fcen(c, t, c4, "= f{200}{3}", 1440, 662, 76, CLARO)
    E.frase(c, t, d4, ps("deixe em fração:", "i", 58, CLARO), 720, 900, "center", 0.1)
    E.foco(c, t, d4 + 0.4, 0.5, lambda a: E.formula(c, "f{200}{3}", 1100, 920, 100, "g", BR, a, "center"))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    E.frase(c, t, C["s15"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a5, ps("vela em", "i", 62) + [("pirâmide de base quadrada", "g", 60, COR)], XE, 330, passo=0.1)
    E.frase(c, t, b5, ps("lado", "i", 62) + [("6 cm", "g", 64, COR)], XE, 440, passo=0.1)
    E.frase(c, t, c5, ps("altura", "i", 62) + [("12 cm", "g", 64, COR)], XE, 540, passo=0.1)
    E.frase(c, t, d5, ps("derretida, vira uma vela em", "i", 56) + [("caixa", "g", 60, COR)], XE, 680, passo=0.1)
    E.frase(c, t, d5 + 1.2, ps("com a mesma base", "i", 56), XE, 770, passo=0.1)
    E.frase(c, t, e5, ps("qual a", "i", 64) + [("altura da vela nova?", "g", 64, COR)], XE, 900, passo=0.1)

    def velas():
        cx, cy, r = 1430, 920, 130
        pir_q(c, t, a5, cx, cy, r, 480, cor=E.COR, preenche=0.3)
        pir_q(c, t, 1e9, cx, cy, r, 480, aresta="6 cm", tm=b5, size=48)
        pir_q(c, t, 1e9, cx, cy, r, 480, altura="12 cm", tm=c5, size=48)
        caixa_q(c, t, d5, 1750, cy, r * 0.8, 160)
        E.foco(c, t, d5 + 0.6, 0.4, lambda q: centro(c, "h = ?", 1750, cy - 260, 56, "g", COR, q))
    E.saida(c, t, C["s16.a"] - 0.1, velas)
    E.relogio(c, t, C["s16.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7 = C["s17.a"], C["s17.b"]
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    cx, cy, r, H_ = 340, 920, 150, 480
    pir_q(c, t, C["s17"], cx, cy, r, H_, cor=E.COR, preenche=0.3)
    pir_q(c, t, 1e9, cx, cy, r, H_, aresta="6", altura="12", tm=C["s17"] + 0.5, size=48)
    if t >= C["s18"]:
        caixa_q(c, t, C["s18"], 760, cy, r, H_ / 3, cor=E.COR, preenche=0.3)
        if t >= b8:
            E.foco(c, t, b8 + 0.6, 0.4, lambda q: E.escreve(c, "4", 760 + r + 20, cy - H_ / 6, 56, "g", COR, q))
        if t >= c8:
            for k in range(1, 3):
                y_ = cy - (H_ / 3) * k * 0.95
                pt = M.paint(TINTA2, ep(t, c8, 0.4), stroke=3)
                pt.setPathEffect(skia.DashPathEffect.Make([12, 10], 0))
                c.drawLine(cx - r, y_, 760 + r, y_, pt)
    X = 1380

    def volume():
        E.frase(c, t, C["s17"] + 0.2, ps("volume, pelo", "i", 62) + [("atalho", "g", 66, COR)], X, 220, "center", 0.1)
        fcen(c, t, a7, "12 ÷ 3 = 4", X, 400, 84)
        fcen(c, t, b7, "36 × 4", X - 200, 620, 84)
        bola_txt(c, t, b7 + 0.6, "144 cm³", X + 200, 600, 120, 52)
    fase(c, t, C["s17"], C["s18"] - 0.1, volume)
    if t < C["s18"] - 0.1:
        return
    E.frase(c, t, C["s18"] + 0.2, ps("a caixa tem a", "i", 62) + [("mesma cera", "g", 66, COR)], X, 220, "center", 0.1)
    fcen(c, t, a8, "36 × h = 144", X, 360, 80)
    fcen(c, t, b8, "h = 144 ÷ 36 = 4 cm", X, 500, 80, COR)
    fcen(c, t, c8, "4 = f{1}{3} de 12", X, 680, 80, TINTA2)
    E.foco(c, t, d8, 0.5, lambda q: E.pilula(c, "um terço da altura", X, 880, 62, "g", a=q, cor=E.SOBRE))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        E.foco(c, t, C["s19.a"], 0.5, lambda a: (E.bola(c, 260, 445, 52, a=a), centro(c, "1", 260, 466, 60, "g", E.SOBRE, a)))
        E.frase(c, t, C["s19.a"] + 0.1, ps("pirâmide:", "i", 66), 350, 490, "left", 0.12)
        E.formula_em(c, t, C["s19.a"] + 0.6, "V = f{área da base × altura}{3}", 680, 490, 66, "g", COR)
        E.foco(c, t, C["s19.b"], 0.5, lambda a: (E.bola(c, 260, 685, 52, a=a), centro(c, "2", 260, 706, 60, "g", E.SOBRE, a)))
        E.frase(c, t, C["s19.b"] + 0.1, [("um terço do prisma", "g", 64, COR)] + ps("de mesma base e altura", "i", 62), 350, 730, "left", 0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, a0, [("a apótema", "g", 120, COR)], XE, 410)
    E.frase(c, t, a0 + 1.0, ps("a altura de cada face, com", "i", 58) + [("Pitágoras", "g", 60, COR)], XE, 520, passo=0.1)
    E.frase(c, t, c0, ps("e a", "i", 64) + [("área total", "g", 68, COR)], XE, 640, passo=0.1)
    cx, cy, r, h = 1560, 860, 190, 250
    pts = pir_q(c, t, a0, cx, cy, r, h)
    if t >= b0:
        i = max(range(4), key=lambda i: pts[i][1] + pts[(i + 1) % 4][1])
        m = ((pts[i][0] + pts[(i + 1) % 4][0]) / 2, (pts[i][1] + pts[(i + 1) % 4][1]) / 2)
        aresta(c, t, b0, pts[4], m, largura=8, tracejada=True)
        E.foco(c, t, b0 + 0.4, 0.4, lambda q: E._cola(c, "5", (pts[4][0] + m[0]) / 2, (pts[4][1] + m[1]) / 2, 1, 0, 14, 54, "g", COR, q))
    E.foco(c, t, d0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, d0 + 0.2, 0.4))
    E.frase(c, t, e0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1010, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, piramide=b_piramide, terco=b_terco, quadrada=b_quadrada, triangular=b_triangular,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
