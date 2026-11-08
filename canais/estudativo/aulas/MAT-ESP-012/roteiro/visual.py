"""Visual — Estudativo · MAT-ESP-012: pirâmide, altura, apótema e área.
Mesma linguagem da trilha (MAT-ESP-001 a 011): sólidos do kit com as escondidas tracejadas, o elemento da vez na cor da matéria,
faces em par índigo/cinza, resposta na esfera.
- A pirâmide é E.piramide de base quadrada (vista (−24, 18), a mesma de MAT-ESP-011). A face da frente fica pintada em COR;
  a APÓTEMA DA PIRÂMIDE é o tracejado grosso em COR sobre ela, do vértice ao meio da aresta da frente; a ALTURA de dentro é o
  tracejado em cinza (TINTA2) até o centro da base; a APÓTEMA DA BASE é o traço preto do centro ao meio da aresta.
- O TRIÂNGULO RETÂNGULO em pé, dentro da pirâmide (vértice, centro, meio da aresta), fica pintado de leve com o quadradinho no
  centro; ao lado, ele aparece deitado e grande (E.triangulo) com os catetos e a hipotenusa.
- ÁREA = a pirâmide aberta como molde (Molde e piramide_q de MAT-ESP-002): a base em COR, os 4 triângulos em CINZA2, a área escrita
  em cada face.
- Atalho (palco escuro): os 4 triângulos lado a lado, com as bases formando o contorno da base.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-012_piramide_altura_apotema_e_area.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("apotema", "triangulo", "area", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)  # a 2ª família pintada numa face de papel
VISTA = (-24, 18)
assert 3 ** 2 + 4 ** 2 == 5 ** 2 and 9 + 16 == 25 and 6 * 5 / 2 == 15 and 4 * 15 == 60 and 6 ** 2 == 36 and 60 + 36 == 96
assert 6 * 4 / 2 == 12 and 4 * 12 == 48 and 48 + 36 == 84 and 4 * 6 == 24 and 24 * 5 == 120 and 120 / 2 == 60
assert 5 ** 2 + 12 ** 2 == 13 ** 2 and 4 * 10 == 40 and 40 * 13 == 520 and 520 / 2 == 260 and 10 ** 2 == 100 and 260 + 100 == 360
assert 40 * 12 / 2 + 100 == 340 and 360 - 340 == 20


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


# ================= Molde: a planificação que dobra (copiada de MAT-ESP-002) =================
def _rot(P, A, u, th):
    """gira P em torno do eixo que passa por A na direção u (unitária)"""
    c_, s_ = math.cos(th), math.sin(th)
    p = (P[0] - A[0], P[1] - A[1], P[2] - A[2])
    cr = (u[1] * p[2] - u[2] * p[1], u[2] * p[0] - u[0] * p[2], u[0] * p[1] - u[1] * p[0])
    d = u[0] * p[0] + u[1] * p[1] + u[2] * p[2]
    return tuple(A[k] + p[k] * c_ + cr[k] * s_ + u[k] * d * (1 - c_) for k in range(3))


def _sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def _cruz(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def _dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


LUZ = (-0.35 / 1.0, 0.85, 0.4)


def camera(k):
    """k = 0: o molde visto de cima; k = 1: de cima e de lado"""
    k = ease_io(min(1.0, max(0.0, k)))
    return E._vista_alta(lerp(0, -28, k), lerp(89.9, 34, k))


class Molde:
    def __init__(s, faces, pais):
        s.f = {n: [(u, 0.0, w) for u, w in pts] for n, pts in faces.items()}
        s.pais = pais
        s.h = {}
        for n, (pai, i, gr) in pais.items():
            P = s.f[n]
            A, B = P[i], P[(i + 1) % len(P)]
            assert any(math.dist(A, q) < 1e-6 for q in s.f[pai]) and any(math.dist(B, q) < 1e-6 for q in s.f[pai]), (n, pai)
            L = math.dist(A, B)
            u = tuple((B[k] - A[k]) / L for k in range(3))
            g = tuple(sum(q[k] for q in P) / len(P) for k in range(3))
            sg = 1 if _rot(g, A, u, 0.2)[1] > 0 else -1  # sempre dobra para cima
            s.h[n] = (A, u, sg * math.radians(gr))

    def pontos(s, n, dobra):
        P, k = s.f[n], n
        while k in s.pais:
            A, u, th = s.h[k]
            f = dobra.get(k, 0.0) if isinstance(dobra, dict) else dobra
            if f:
                P = [_rot(q, A, u, th * f) for q in P]
            k = s.pais[k][0]
        return P

    def desenha(s, c, t, dobra, cam, ox, oy, a=1.0, ta=None, cores=None, contornos=None, nums=None, tn=None, size=64, pisca=None, zoom=None):
        """ta = {face: instante em que entra}; nums = {face: texto}; tn = {face: instante do número}; pisca = {face: 0..1}.
        zoom = escala em volta de (ox, oy); sem ela, o sólido montado cresce 40% (visto de lado ele parece menor)"""
        R, U, v = camera(cam) if isinstance(cam, (int, float)) else cam
        z = zoom if zoom is not None else (1 + 0.4 * ease_io(min(1.0, max(0.0, cam))) if isinstance(cam, (int, float)) else 1.0)
        R, U = tuple(x * z for x in R), tuple(x * z for x in U)
        itens = []
        for n in s.f:
            P = s.pontos(n, dobra)
            g = tuple(sum(q[k] for q in P) / len(P) for k in range(3))
            itens.append((_dot(g, v), n, P, g))
        itens.sort()
        for _, n, P, g in itens:
            af = a * (ep(t, ta[n], 0.4) if ta and n in ta else 1.0)
            if af <= 0:
                continue
            pts = [E._proj(q, R, U, ox, oy) for q in P]
            nn = _cruz(_sub(P[1], P[0]), _sub(P[2], P[0]))
            nl = math.sqrt(_dot(nn, nn)) or 1
            nn = tuple(x / nl for x in nn)
            luz = abs(_dot(nn, LUZ)) / math.sqrt(_dot(LUZ, LUZ))
            base = (cores or {}).get(n) or E.mix(E.COR, "#FFFFFF", 0.82)
            if pisca and pisca.get(n, 0) > 0:
                base = E.mix(base, E.COR, 0.7 * pisca[n])
            fill = E.mix(base, "#000000", 0.2 * (1 - luz))
            path = skia.Path()
            path.addPoly(pts, True)
            c.drawPath(path, M.paint(fill, af))
            pt = M.paint(TINTA, af, stroke=5)
            pt.setStrokeJoin(skia.Paint.kRound_Join)
            c.drawPath(path, pt)
            if contornos and n in contornos:
                c.save(); c.clipPath(path, skia.ClipOp.kIntersect, True)
                c.drawPath(path, M.paint(contornos[n], af, stroke=22))
                c.restore()
            if nums and n in nums:
                vis = min(1.0, max(0.0, abs(_dot(nn, v)) * 3 - 0.3))
                q = af * vis * (ep(t, tn[n], 0.35) if tn and n in tn else 1.0)
                gx, gy = E._proj(g, R, U, ox, oy)
                cor_n = BR if (cores and n in cores) else (contornos[n] if contornos and n in contornos else TINTA)
                if q > 0:
                    centro(c, nums[n], gx, gy + size * 0.36, size, "g", cor_n, q)


def ret(x, w, lx, lw):
    """retângulo (u, w, largura, altura) no sentido horário"""
    return [(x, w), (x + lx, w), (x + lx, w + lw), (x, w + lw)]




# ================= peças desta aula =================
def vertice(c, t, t0, P, r=15, cor=None, a=1.0):
    """o ponto da vez: bolinha que salta (de MAT-ESP-001)"""
    k = ease_back(prog(t, t0, 0.35))
    if k > 0 and a > 0:
        c.drawCircle(P[0], P[1], r * k, M.paint(cor or E.COR, a))


def meio(P, Q):
    return (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2


class Pir:
    """a pirâmide de base quadrada de lado `lado` e altura `alt` (unidades), k px por unidade, base com centro em (cx, cy).
    Guarda os pontos na tela: v (vértice), o (centro da base), m (meio da aresta da frente), fr (as duas pontas dessa aresta)"""

    def __init__(s, cx, cy, lado, alt, k):
        s.cx, s.cy, s.r, s.h = cx, cy, lado * k / math.sqrt(2), alt * k
        R, U, _ = E._vista_alta(*VISTA)
        base = E._base_regular(4, s.r)
        s.pts = [E._proj((x, 0, z), R, U, cx, cy) for x, z in base] + [E._proj((0, s.h, 0), R, U, cx, cy)]
        i = max(range(4), key=lambda i: s.pts[i][1] + s.pts[(i + 1) % 4][1])
        s.i = i
        s.fr = (s.pts[i], s.pts[(i + 1) % 4])
        s.v, s.o, s.m = s.pts[4], (cx, cy), meio(*s.fr)

    def desenha(s, c, t, t0, **kw):
        return E.piramide(c, t, t0, s.cx, s.cy, 4, s.r, s.h, vista=VISTA, **kw)

    def face(s, c, a, cor=None, alfa_=0.4):
        face(c, s.pts, (s.i, (s.i + 1) % 4, 4), a, cor, alfa_)

    def triangulo(s, c, a, cor=None):
        """o triângulo retângulo em pé: vértice, centro da base e meio da aresta"""
        if a <= 0:
            return
        p = skia.Path(); p.addPoly([s.v, s.o, s.m], True)
        c.drawPath(p, M.paint(cor or E.COR, 0.28 * a))
        reto(c, s.o, s.m, s.v, k=24, a=a, cor=TINTA)


def apotema(c, t, t0, P, rot=None, cor=None, size=52, lado=1, d=0.5):
    """a apótema da pirâmide: tracejado grosso do vértice ao meio da aresta, com o rótulo"""
    aresta(c, t, t0, P.v, P.m, cor=cor, largura=9, tracejada=True, d=d)
    if rot:
        E.foco(c, t, t0 + 0.4, 0.4, lambda q: E._cola(c, rot, *meio(P.v, P.m), lado, 0, 16, size, "g", cor or COR, q))


def altura(c, t, t0, P, rot=None, cor=None, size=52, lado=-1):
    aresta(c, t, t0, P.v, P.o, cor=cor or TINTA2, largura=7, tracejada=True)
    if t >= t0 + 0.4:
        vertice(c, t, t0 + 0.4, P.o, r=8, cor=TINTA)
    if rot:
        E.foco(c, t, t0 + 0.4, 0.4, lambda q: E._cola(c, rot, P.o[0], lerp(P.o[1], P.v[1], 0.5), lado, 0, 16, size, "g", cor or TINTA2, q))


def ap_base(c, t, t0, P, rot=None, size=50):
    aresta(c, t, t0, P.o, P.m, cor=TINTA, largura=7)
    if rot:
        E.foco(c, t, t0 + 0.4, 0.4, lambda q: E._cola(c, rot, *meio(P.o, P.m), 0.3, 1, 12, size, "g", TINTA, q))


def piramide_q(s, hl):
    """pirâmide quadrangular aberta (de MAT-ESP-002): quadrado s x s e um triângulo de altura hl em cada lado"""
    h = s / 2
    gr = 180 - math.degrees(math.acos(h / hl))
    F = {"base": ret(-h, -h, s, s),
         "a": [(-h, -h), (h, -h), (0, -h - hl)], "b": [(h, -h), (h, h), (h + hl, 0)],
         "c": [(h, h), (-h, h), (0, h + hl)], "d": [(-h, h), (-h, -h), (-h - hl, 0)]}
    P = {k: ("base", 0, gr) for k in "abcd"}
    return Molde(F, P)


MK = 50
PIRQ = piramide_q(6 * MK, 5 * MK)
OX, OY = 470, 540


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")
    P = Pir(500, 900, 6, 4, 75)

    def um():
        P.desenha(c, t, a1)
        P.desenha(c, t, 1e9, aresta="6", tm=b1, size=56)
        if t >= b1:
            altura(c, t, b1 + 0.3, P, "4")
        P.face(c, ep(t, b1 + 1.2, 0.5))
        if t >= b1 + 1.6:
            apotema(c, t, b1 + 1.6, P, "?" if t < d1 else "5", cor=COR if t >= d1 else TINTA)
        X = 1340
        E.frase(c, t, a1 + 0.3, ps("pirâmide de base", "i", 64) + [("quadrada", "g", 68, COR)], X, 230, "center", 0.1)
        E.frase(c, t, b1, ps("lado", "i", 60) + [("6", "g", 66, COR)] + ps("e altura", "i", 60) + [("4", "g", 66, COR)], X, 330, "center", 0.1)
        E.frase(c, t, b1 + 1.6, ps("e a altura de cada", "i", 60) + [("face?", "g", 66, COR)], X, 480, "center", 0.1)
        fcen(c, t, c1, "4", X - 160, 680, 120, ERRADO)
        if t >= c1 + 0.5:
            E.risco(c, X - 220, 690, X - 100, 600, t, c1 + 0.5, largura=10)
        bola_txt(c, t, d1, "5", X + 140, 640, 100, 100)
        E.frase(c, t, d1 + 0.7, ps("e isso muda a", "i", 58) + [("área toda", "g", 62, COR)], X, 880, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.2), ps("a", "i", 90) + [("altura das faces", "g", 96, COR)], XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), ps("e a", "i", 90) + [("área total", "g", 96, COR)], XE, 590, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.7), ps("da pirâmide", "i", 90), XE, 720, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 940, 860
    itens = (("s03.b", "altura da pirâmide:", "em pé, por dentro"), ("s03.c", "Pitágoras:", "a² = b² + c²"), ("s03.d", "ternos:", "3, 4 e 5"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 58), x + 44, y + 80, "left", 0.1)
        E.frase(c, t, C[k] + 0.5, [(l2, "g", 60, COR)], x + 44, y + 162)
    alvo = [190 + i * 240 + 170 for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.72), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- a apótema e o triângulo ----------------
PA = Pir(520, 900, 6, 4, 82)


def b_apotema(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    PA.desenha(c, t, C["s04"])
    PA.face(c, ep(t, a4, 0.5))
    if t >= b4:
        apotema(c, t, b4, PA)
        xr = max(p[0] for p in PA.pts) + 24
        E.foco(c, t, b4 + 0.4, 0.4, lambda q: E.escreve(c, "apótema", xr, lerp(PA.m[1], PA.v[1], 0.5) + 18, 54, "g", COR, q))
    if t >= d4:
        vertice(c, t, d4, PA.m, r=14)
    if t >= b5:
        altura(c, t, b5, PA)
        E.foco(c, t, b5 + 0.4, 0.4, lambda q: E.escreve(c, "altura", min(p[0] for p in PA.pts) - 10, PA.v[1] + 40, 54, "g", TINTA2, q))
    X = 1330

    def nome():
        E.frase(c, t, a4, ps("a altura de uma", "i", 62) + [("face lateral", "g", 66, COR)], X, 240, "center", 0.1)
        E.frase(c, t, b4, ps("=", "i", 66) + [("apótema da pirâmide", "g", 70, COR)], X, 370, "center", 0.1)
        E.frase(c, t, c4, ps("desce", "i", 60) + [("pelo meio da face", "g", 62)], X, 520, "center", 0.1)
        E.frase(c, t, d4, ps("até o", "i", 60) + [("meio da aresta", "g", 62, COR)] + ps("da base", "i", 60), X, 630, "center", 0.1)
    fase(c, t, C["s04"], C["s05"] - 0.1, nome)
    if t < C["s05"] - 0.1:
        return
    E.frase(c, t, a5, [("duas alturas", "g", 76, COR)] + ps("diferentes", "i", 66), X, 230, "center", 0.1)
    E.frase(c, t, b5, [("altura:", "g", 60, TINTA2)] + ps("por dentro, em pé, até o centro", "i", 54), X, 380, "center", 0.1)
    E.frase(c, t, c5, [("apótema:", "g", 60, COR)] + ps("inclinada, deitada na face", "i", 54), X, 500, "center", 0.1)
    E.frase(c, t, d5, ps("por isso, a apótema é", "i", 58) + [("mais comprida", "g", 62, COR)], X, 680, "center", 0.1)


def b_triangulo(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    P = PA
    P.desenha(c, t, C["s06"] - 2)
    P.triangulo(c, ep(t, a7, 0.5))
    altura(c, t, C["s06"] - 2, P, "4" if t >= b7 else None, size=52)
    ap_base(c, t, a6, P, "3" if t >= c6 else None)
    if t >= c7:
        apotema(c, t, c7, P, "?" if t < c8 else "5", lado=1)
    else:
        apotema(c, t, C["s06"] - 2, P, None, cor=CINZA2)
    X = 1330

    def base():
        E.frase(c, t, a6, ps("do centro ao", "i", 60) + [("meio da aresta", "g", 62)], X, 240, "center", 0.1)
        E.frase(c, t, b6, ps("=", "i", 66) + [("apótema da base", "g", 70)], X, 370, "center", 0.1)
        E.frase(c, t, c6, ps("no quadrado:", "i", 60) + [("metade do lado = 3", "g", 62, COR)], X, 520, "center", 0.1)
    fase(c, t, C["s06"], C["s07"] - 0.1, base)

    def triang():
        E.frase(c, t, a7, [("triângulo retângulo", "g", 66, COR)] + ps("em pé", "i", 62), X, 240, "center", 0.1)
        E.frase(c, t, b7, [("catetos:", "g", 60)] + ps("a altura e a apótema da base", "i", 54), X, 380, "center", 0.1)
        E.frase(c, t, c7, [("hipotenusa:", "g", 60, COR)] + ps("a apótema da pirâmide", "i", 54), X, 500, "center", 0.1)
    fase(c, t, C["s07"], C["s08"] - 0.1, triang)
    if t < C["s08"] - 0.1:
        return
    # o triângulo deitado, grande
    A, B, Q = (1060, 620), (1360, 620), (1060, 220)
    E.triangulo(c, t, C["s08"], A, B, Q, vertices=None, lados=("3", "5", "4"), retos=(0,), preenche=0.2, tl=[a8, c8, a8 + 0.2], size=60)
    fcen(c, t, b8, "terno 3, 4 e 5", 1580, 420, 64, TINTA2)
    fcen(c, t, d8, "9 + 16 = 25", 1150, 820, 76)
    fcen(c, t, e8, "r{25} = 5", 1150, 960, 76, COR)
    bola_txt(c, t, e8 + 0.6, "5", 1600, 860, 100, 100)
    E.foco(c, t, c8, 0.4, lambda q: centro(c, "apótema", 1600, 1010, 50, "i", COR, q))


# ---------------- área ----------------
NUMS = {"a": "15", "b": "15", "c": "15", "d": "15", "base": "36"}


def b_area(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    abre = ease_io(prog(t, a9, 1.8))
    k = 1 - abre
    cores = {}
    if t >= b9:
        cores["base"] = E.COR
    for i, n in enumerate("cbad"):
        if t >= c9 + 0.25 * i:
            cores[n] = CINZA2
    tn = {"a": e9 + 0.5, "b": e9 + 0.65, "c": e9 + 0.8, "d": e9 + 0.95, "base": b0}
    PIRQ.desenha(c, t, 1 - abre, k, OX, lerp(OY, 700, k), ep(t, C["s09"], 0.5), cores=cores or None, nums=NUMS, tn=tn, size=50)
    h = 3 * MK
    if d9 <= t < e9 + 0.5:
        q = ep(t, d9, 0.4) * (1 - ep(t, e9 + 0.2, 0.3))
        M.line(c, OX, OY + h, OX, OY + h + 5 * MK, E.COR, q, 7, dash=E.TRACO, progress=ease_io(prog(t, d9, 0.5)))
        E.foco(c, t, d9 + 0.3, 0.4, lambda a: E.escreve(c, "5", OX + 18, OY + h + 2.5 * MK + 18, 54, "g", COR, a * q))
    if t >= d9:
        E.foco(c, t, d9, 0.4, lambda a: centro(c, "6", OX, OY + h - 18, 50, "g", E.SOBRE, a * (1 - ep(t, b0 - 0.3, 0.3))))
    X = 1340

    def face_():
        E.frase(c, t, a9, ps("abra a pirâmide:", "i", 64), X, 230, "center", 0.1)
        E.frase(c, t, b9, [("1 quadrado", "g", 66, COR)] + ps("no meio", "i", 60), X, 350, "center", 0.1)
        E.frase(c, t, c9, [("4 triângulos iguais", "g", 66, TINTA2)] + ps("em volta", "i", 60), X, 460, "center", 0.1)
        E.frase(c, t, d9, ps("base", "i", 60) + [("6", "g", 64, COR)] + ps("e altura", "i", 60) + [("5", "g", 64, COR)] + ps("(a apótema)", "i", 54, TINTA2), X, 610, "center", 0.1)
        fcen(c, t, e9, "f{6 × 5}{2} = 15", X, 780, 84)
    fase(c, t, C["s09"], C["s10"] - 0.1, face_)
    if t < C["s10"] - 0.1:
        return
    fcen(c, t, a0, "4 × 15 = 60", X, 260, 84)
    E.frase(c, t, a0 + 0.8, ps("a área lateral", "i", 54, TINTA2), X, 350, "center", 0.1)
    fcen(c, t, b0, "base: 6² = 36", X, 500, 84, COR)
    fcen(c, t, c0, "60 + 36", X - 190, 760, 84)
    bola_txt(c, t, c0 + 0.6, "96", X + 200, 740, 110, 84)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    P = PA
    P.desenha(c, t, C["s11"])
    P.face(c, ep(t, C["s11"] + 0.4, 0.5))
    altura(c, t, a1, P, "4", cor=ERRADO if t < e1 else TINTA2)
    apotema(c, t, e1 + 0.4, P, "5")
    X = 1330
    E.frase(c, t, C["s11"] + 0.2, [("erro comum:", "g", 66, ERRADO)], X, 200, "center", 0.1)
    E.frase(c, t, a1, ps("usar a", "i", 60) + [("altura da pirâmide", "g", 62, ERRADO)] + ps("na face", "i", 60), X, 300, "center", 0.1)

    def errado():
        fcen(c, t, b1, "f{6 × 4}{2} = 12", X, 460, 72, ERRADO)
        fcen(c, t, c1, "4 × 12 = 48", X, 590, 72, ERRADO)
        fcen(c, t, d1, "48 + 36 = 84", X, 710, 76, ERRADO)
        if t >= d1 + 0.7:
            E.risco(c, X - 230, 725, X + 230, 665, t, d1 + 0.7, largura=10)
    fase(c, t, b1, e1 + 1.0, errado)
    if t >= e1 + 1.0:
        E.frase(c, t, e1 + 1.0, [("altura de dentro:", "g", 60, TINTA2)] + ps("apótema e volume", "i", 58), X, 520, "center", 0.1)
        E.foco(c, t, e1 + 1.8, 0.5, lambda q: E.pilula(c, "na face: só a apótema", X, 700, 64, "g", a=q, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, C["s12"] + 0.2, ps("atalho da", "i", 70, CLARO) + [("área lateral", "g", 74, BR)], W / 2, 200, "center", 0.1)
        fcen(c, t, a2, "f{perímetro da base × apótema}{2}", W / 2, 400, 90, BR)
        fcen(c, t, b2, "4 × 6 = 24", 560, 700, 80, CLARO)
        fcen(c, t, c2, "24 × 5 = 120", 1100, 700, 80, CLARO)
        fcen(c, t, d2, "120 ÷ 2", 760, 900, 84, BR)
        bola_txt(c, t, d2 + 0.6, "60", 1200, 880, 100, 80)
    fase(c, t, C["s12"], C["s13"] - 0.1, um)
    if t < C["s13"] - 0.1:
        return
    E.frase(c, t, a3, ps("o atalho do prisma,", "i", 62, CLARO) + [("÷ 2", "g", 70, BR)] + ps("do triângulo", "i", 62, CLARO), W / 2, 200, "center", 0.1)
    # os 4 triângulos lado a lado: as bases somam o contorno
    s, hh, y0 = 60, 220, 620
    x0 = W / 2 - 12 * s
    for k in range(4):
        q = ep(t, b3 + 0.25 * k, 0.4)
        if q <= 0:
            continue
        xa = x0 + k * 6 * s
        p = skia.Path(); p.addPoly([(xa, y0), (xa + 6 * s, y0), (xa + 3 * s, y0 - hh)], True)
        c.drawPath(p, M.paint(E.COR, 0.6 * q)); c.drawPath(p, M.paint(BR, q, stroke=4))
        centro(c, "6", xa + 3 * s, y0 + 56, 48, "g", BR, q)
    if t >= b3 + 1.2:
        E.chave(c, x0, x0 + 24 * s, y0 + 90, CLARO, ep(t, b3 + 1.2, 0.5), h=22)
        E.foco(c, t, b3 + 1.4, 0.4, lambda q: centro(c, "24 = o contorno da base", W / 2, y0 + 170, 52, "g", BR, q))
    E.frase(c, t, b3 + 0.2, ps("triângulos iguais,", "i", 56, CLARO) + [("mesma altura", "g", 60, BR)], W / 2, 300, "center", 0.1)
    E.foco(c, t, c3, 0.5, lambda a: E.selo(c, 420, 920, 44, False, a))
    E.frase(c, t, c3 + 0.1, ps("faces diferentes (base retangular):", "i", 54, CLARO) + [("face por face", "g", 58, BR)], 490, 940, "left", 0.1)
    E.frase(c, t, d3, ps("calcule cada uma e some", "i", 52, CLARO), W / 2, 1030, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    E.frase(c, t, C["s14"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a4, ps("enfeite de vidro:", "i", 62) + [("pirâmide de base quadrada", "g", 60, COR)], XE, 340, passo=0.1)
    E.frase(c, t, b4, ps("lado", "i", 62) + [("10 cm", "g", 64, COR)], XE, 450, passo=0.1)
    E.frase(c, t, c4, ps("altura", "i", 62) + [("12 cm", "g", 64, COR)], XE, 550, passo=0.1)
    E.frase(c, t, d4, ps("quanto", "i", 64) + [("vidro", "g", 68, COR)] + ps("ele gasta,", "i", 64), XE, 710, passo=0.1)
    E.frase(c, t, d4 + 1.0, ps("contando a base?", "i", 64), XE, 810, passo=0.1)
    P = Pir(1470, 900, 10, 12, 30)

    def peca():
        P.desenha(c, t, a4, cor=E.COR, preenche=0.2)
        P.desenha(c, t, 1e9, aresta="10 cm", tm=b4, size=48)
        if t >= c4:
            altura(c, t, c4, P, "12 cm", size=48, lado=1)
    E.saida(c, t, C["s15.a"] - 0.1, peca)
    E.relogio(c, t, C["s15.a"], 1560, 760, 150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    a8, b8 = C["s18.a"], C["s18.b"]
    P = Pir(440, 960, 10, 12, 34)
    P.desenha(c, t, C["s16"])
    P.triangulo(c, ep(t, a6, 0.5))
    altura(c, t, C["s16"] + 0.6, P, "12", size=48, lado=-1)
    ap_base(c, t, a6, P, "5", size=46)
    apotema(c, t, b6, P, "13" if t >= c6 else "?", lado=1, size=50)
    X = 1300

    def apot():
        fcen(c, t, a6, "apótema da base = f{10}{2} = 5", X, 300, 66)
        fcen(c, t, b6, "terno 5, 12 e 13", X, 460, 72, TINTA2)
        bola_txt(c, t, c6, "13", X, 680, 110, 90)
        E.foco(c, t, c6 + 0.4, 0.4, lambda q: centro(c, "apótema da pirâmide", X, 850, 50, "i", COR, q))
    fase(c, t, C["s16"], C["s17"] - 0.1, apot)

    def area():
        fcen(c, t, a7, "perímetro = 40", X, 220, 66, TINTA2)
        fcen(c, t, b7, "40 × 13 = 520", X, 340, 70)
        fcen(c, t, c7, "520 ÷ 2 = 260", X, 460, 70)
        fcen(c, t, d7, "base: 10² = 100", X, 580, 70, COR)
        fcen(c, t, e7, "260 + 100", X - 220, 800, 76)
        bola_txt(c, t, e7 + 0.6, "360 cm²", X + 210, 780, 125, 52)
    fase(c, t, C["s17"], C["s18"] - 0.1, area)
    if t < C["s18"] - 0.1:
        return
    E.frase(c, t, C["s18"] + 0.2, ps("com a altura", "i", 60) + [("12", "g", 64, ERRADO)] + ps("na face:", "i", 60), X, 300, "center", 0.1)
    fcen(c, t, a8, "340 cm²", X, 470, 96, ERRADO)
    if t >= a8 + 0.6:
        E.risco(c, X - 200, 485, X + 200, 415, t, a8 + 0.6, largura=10)
    E.frase(c, t, b8, ps("faltariam", "i", 62) + [("20 cm²", "g", 66, ERRADO)] + ps("de vidro", "i", 62), X, 650, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s19.a", [("apótema", "g", 62, COR)] + ps("= hipotenusa, com a altura e a metade do lado", "i", 56)),
                 ("s19.b", [("área total", "g", 62, COR)] + ps("= base + faces laterais", "i", 58)))
        for i, (k, l1) in enumerate(itens):
            y = 470 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 220, y - 25, 52, a=a), centro(c, str(i + 1), 220, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, l1, 310, y, "left", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0, e0, f0 = (C[f"s20.{k}"] for k in "abcdef")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula, o mesmo triângulo", "i", 66), XE, 250, passo=0.1)
    E.frase(c, t, a0, ps("no", "i", 90) + [("cone", "g", 130, COR)], XE, 410)
    E.frase(c, t, b0, ps("raio", "i", 60) + [("3", "g", 64, COR)] + ps("e altura", "i", 60) + [("4", "g", 64, COR)], XE, 530, passo=0.1)
    E.frase(c, t, c0, ps("geratriz", "i", 60) + [("5", "g", 64, COR)], XE, 630, passo=0.1)
    E.frase(c, t, d0, ps("volume e área lateral do cone", "i", 58), XE, 730, passo=0.1)
    E.cone(c, t, a0, 1520, 880, 150, 200)
    E.cone(c, t, 1e9, 1520, 880, 150, 200, "3", "4", None, size=48, tm=b0)
    E.cone(c, t, 1e9, 1520, 880, 150, 200, None, None, "5", size=52, tm=c0)
    E.foco(c, t, e0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, e0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, e0 + 0.2, 0.4))
    E.frase(c, t, f0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], 900, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, apotema=b_apotema, triangulo=b_triangulo, area=b_area, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
