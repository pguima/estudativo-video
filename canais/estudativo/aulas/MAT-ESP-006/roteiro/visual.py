"""Visual — Estudativo · MAT-ESP-006: cubo e bloco, área total e diagonal.
Mesma linguagem da trilha (MAT-ESP-001 a 005):
- ÁREA TOTAL = a caixa que se abre no plano (a classe Molde de MAT-ESP-002, copiada aqui). Faces gêmeas têm a mesma marca:
  chão e teto em COR, frente e fundo em CINZA2 (a 2ª família numa face opaca), os lados com contorno COR. A área de cada face
  aparece escrita nela.
- DIAGONAL = segmento grosso na cor da matéria atravessando o sólido; o triângulo retângulo que a calcula fica pintado de leve,
  com o quadradinho de ângulo reto (reto()) no pé da aresta em pé. Diagonal do chão em tinta preta.
- Contas com raiz em E.formula ("2r{2}", "r{12}"); resposta na esfera.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-006_cubo_e_bloco_area_e_diagonal.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("area", "diagonal", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)  # a 2ª família pintada numa face de papel
assert 3 * 2 == 6 and 3 * 1 == 3 and 2 * 1 == 2 and (6 + 3 + 2) * 2 == 22 and 3 * 2 * 1 == 6 and 22 / 10 == 2.2
assert 8 + 4 == 12 and 12 == 4 * 3 and abs(2 * 3 ** 0.5 - 3.46) < 0.01 and 30 * 30 == 900 and 900 * 6 == 5400
assert round(30 * 1.7) == 51 and round(30 * 1.4) == 42 and 2 * 10 == 20 and 22 - 20 == 2


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


def cruz_cubo(s):
    """o molde em cruz: faixa 1 a 4 em pé (1 em cima), aba 5 à esquerda do 2 e aba 6 à direita do 2. A face 2 é o chão"""
    h = s / 2
    F = {"1": ret(-h, -h - s, s, s), "2": ret(-h, -h, s, s), "3": ret(-h, h, s, s), "4": ret(-h, h + s, s, s),
         "5": ret(-h - s, -h, s, s), "6": ret(h, -h, s, s)}
    P = {"1": ("2", 2, 90), "3": ("2", 0, 90), "4": ("3", 0, 90), "5": ("2", 1, 90), "6": ("2", 3, 90)}
    return Molde(F, P)


def molde_questao(s):
    """o molde da questão: faixa 1 a 4 em pé, aba 5 à esquerda do 1 e aba 6 à direita do 3"""
    h = s / 2
    F = {"1": ret(-h, -h - s, s, s), "2": ret(-h, -h, s, s), "3": ret(-h, h, s, s), "4": ret(-h, h + s, s, s),
         "5": ret(-h - s, -h - s, s, s), "6": ret(h, h, s, s)}
    P = {"1": ("2", 2, 90), "3": ("2", 0, 90), "4": ("3", 0, 90), "5": ("1", 1, 90), "6": ("3", 3, 90)}
    return Molde(F, P)


def caixa_sapato(a, b, h):
    """a caixa: fundo a x b no chão; frente e trás a x h; tampa presa atrás; lados h x b"""
    F = {"fundo": ret(-a / 2, -b / 2, a, b), "frente": ret(-a / 2, b / 2, a, h), "tras": ret(-a / 2, -b / 2 - h, a, h),
         "tampa": ret(-a / 2, -b / 2 - h - b, a, b), "esq": ret(-a / 2 - h, -b / 2, h, b), "dir": ret(a / 2, -b / 2, h, b)}
    P = {"frente": ("fundo", 0, 90), "tras": ("fundo", 2, 90), "tampa": ("tras", 2, 90), "esq": ("fundo", 1, 90), "dir": ("fundo", 3, 90)}
    return Molde(F, P)


# ---------------- a caixa da aula: 3 m x 2 m x 1 m ----------------
CAIXA = caixa_sapato(330, 220, 110)   # 110 px por metro
PARES = {"fundo": E.COR, "tampa": E.COR, "frente": CINZA2, "tras": CINZA2}
CONT = {"esq": E.COR, "dir": E.COR}
AREAS = {"fundo": "6 m²", "tampa": "6 m²", "frente": "3 m²", "tras": "3 m²", "esq": "2 m²", "dir": "2 m²"}


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        pts = E.paralelepipedo(c, t, a1, 230, 820, 480, 320, 160, ("3 m", "2 m", "1 m"), size=54, tm=a1 + 1.2)
        q = ep(t, c1, 0.6)
        for k, idx in enumerate(((0, 1, 2, 3), (3, 2, 6, 7), (1, 2, 6, 5))):
            face(c, pts, idx, ep(t, c1 + 0.3 * k, 0.5), alfa_=0.55)
        E.frase(c, t, a1 + 0.2, ps("pintar a caixa", "i", 70) + [("por fora", "g", 74, COR)], 1060, 240, "left", 0.1)
        E.frase(c, t, b1, ps("volume:", "i", 64) + [("6 m³", "g", 70, ERRADO)], 1060, 400, "left", 0.1)
        if t >= b1 + 1.0:
            E.risco(c, 1050, 420, 1440, 340, t, b1 + 1.0, largura=10)
        E.frase(c, t, c1, ps("a tinta cobre a", "i", 66) + [("casca", "g", 70, COR)], 1060, 560, "left", 0.1)
        E.frase(c, t, d1, ps("o que importa:", "i", 62) + [("a área", "g", 66, COR)], 1060, 700, "left", 0.1)
        bola_txt(c, t, d1 + 0.8, "22 m²", 1400, 870, 120, 72)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("a área", "g", 104, COR)] + ps("da caixa", "i", 96), XE, 460, passo=0.14)
        E.frase(c, t, tb, [("a maior vareta", "g", 90, COR)], XE, 620, passo=0.14)
        E.frase(c, t, tb + 0.6, ps("dentro do cubo", "i", 90), XE, 740, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "planificação:", "face por face no plano"), ("s03.c", "área do retângulo:", "base × altura"), ("s03.d", "diagonal do quadrado:", None))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 60), x + 44, y + 84, "left", 0.1)
        if l2:
            E.frase(c, t, C[k] + 0.4, [(l2, "g", 58, COR)], x + 44, y + 160)
        else:
            E.formula_em(c, t, C[k] + 0.4, "lado × r{2}", x + 44, y + 165, 62, "g", COR)
    alvo = [190 + i * 240 + 170 for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.7), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- área total ----------------
OX, OY = 520, 600
X = 1340


def b_area(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s04.{k}"] for k in "abcde")
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]

    def molde():
        abre = ease_io(prog(t, a4 - 0.6, 1.6))
        k = 1 - abre
        cores, cont = {}, {}
        if t >= c4:
            cores.update({"fundo": E.COR, "tampa": E.COR})
        if t >= d4:
            cores.update({"frente": CINZA2, "tras": CINZA2})
        if t >= e4:
            cont.update(CONT)
        tn = {"fundo": a5, "tampa": a5 + 0.3, "frente": b5, "tras": b5 + 0.3, "esq": c5, "dir": c5 + 0.3}
        CAIXA.desenha(c, t, 1 - abre, k, OX, lerp(OY + 40, 760, k), ep(t, C["s04"], 0.5), cores=cores or None, contornos=cont or None,
                      nums=AREAS, tn=tn, size=40)
        E.frase(c, t, a4, ps("aberta:", "i", 66) + [("6 retângulos", "g", 70, COR)], X, 220, "center", 0.1)
        E.frase(c, t, b4, ps("em", "i", 62) + [("pares iguais", "g", 64)] + ps("de frente", "i", 62), X, 320, "center", 0.1)
        for kk, (tk, s_, cor, cont_) in enumerate(((c4, "chão e teto", E.COR, False), (d4, "frente e fundo", CINZA2, False), (e4, "os lados", E.COR, True))):
            y = 450 + 90 * kk
            E.foco(c, t, tk, 0.4, lambda q, y=y, cor=cor, cont_=cont_: (c.drawRect(skia.Rect.MakeXYWH(X - 260, y - 42, 50, 50), M.paint(cor, q, stroke=8 if cont_ else 0) if cont_ else M.paint(cor, q))))
            E.frase(c, t, tk, ps(s_, "i", 58), X - 180, y, "left", 0.1)
        # as contas: uma de cada par
        if t >= a5:
            for kk, (tk, s_) in enumerate(((a5, "3 × 2 = 6"), (b5, "3 × 1 = 3"), (c5, "2 × 1 = 2"))):
                E.formula_em(c, t, tk + 0.3, s_, X + 160, 450 + 90 * kk, 54, "g", TINTA2)
    fase(c, t, C["s04"], C["s06"] - 0.1, molde)

    def soma():
        CAIXA.desenha(c, t, 0, 0, OX, OY + 40, 1, cores={**{n: E.COR for n in ("fundo", "tampa")}, **{n: CINZA2 for n in ("frente", "tras")}},
                      contornos=CONT, nums=AREAS, size=40)
        fcen(c, t, a6, "6 + 3 + 2 = 11", X, 300, 84)
        E.frase(c, t, a6 + 0.8, ps("uma de cada par", "i", 54, TINTA2), X, 380, "center", 0.1)
        fcen(c, t, b6, "11 × 2 = 22", X, 520, 84)
        E.frase(c, t, b6 + 0.6, ps("cada uma tem uma gêmea", "i", 54, TINTA2), X, 600, "center", 0.1)
        bola_txt(c, t, b6 + 1.2, "22 m²", X, 760, 115, 66)
        E.frase(c, t, c6, [("área total:", "g", 60, COR)] + ps("a soma de todas as faces", "i", 54), X, 960, "center", 0.1)
    fase(c, t, C["s06"], C["s07"] - 0.1, soma)

    def formula():
        pts = E.paralelepipedo(c, t, C["s07"], 200, 820, 460, 300, 220, ("a", "b", "c"), size=60)
        fcen(c, t, a7, "Área total = 2 · (ab + ac + bc)", X, 300, 70, COR)
        if t >= b7:
            face(c, pts, (0, 1, 5, 4), ep(t, b7, 0.4), alfa_=0.5)
            face(c, pts, (0, 1, 2, 3), ep(t, b7 + 0.4, 0.4), CINZA2, 0.45)
            face(c, pts, (1, 2, 6, 5), ep(t, b7 + 0.8, 0.4), E.COR, 0.22)
        E.frase(c, t, b7, ps("cada produto = a área de uma face", "i", 54, TINTA2), X, 400, "center", 0.08)
        E.frase(c, t, c7, ps("o 2 conta a", "i", 54, TINTA2) + [("gêmea", "g", 56)], X, 480, "center", 0.08)
        E.cubo(c, t, d7, 1000, 900, 220, "a", size=52)
        fcen(c, t, d7 + 0.3, "cubo: 6a²", 1650, 780, 84, COR)
        E.frase(c, t, d7 + 0.8, ps("6 quadrados iguais", "i", 54, TINTA2), 1650, 870, "center", 0.08)
    fase(c, t, C["s07"], C["s08"] - 0.1, formula)
    if t < C["s08"] - 0.1:
        return
    E.frase(c, t, C["s08"] + 0.2, ps("e a", "i", 76) + [("tinta?", "g", 80, COR)], W / 2, 200, "center", 0.1)
    E.frase(c, t, a8, ps("1 lata pinta", "i", 66) + [("10 m²", "g", 70, COR)], W / 2, 330, "center", 0.1)
    fcen(c, t, b8, "22 ÷ 10 = 2,2", W / 2, 480, 96)
    E.frase(c, t, b8 + 0.8, ps("mais de 2 latas", "i", 58, TINTA2), W / 2, 570, "center", 0.1)
    for k in range(3):
        cx = 700 + k * 260
        q = ep(t, c8 + 0.25 * k, 0.4)
        if q > 0:
            E.cilindro(c, t, c8 + 0.25 * k - 0.6, cx, 900, 80, 170, preenche=0.5)
            E.foco(c, t, c8 + 0.25 * k + 0.2, 0.4, lambda q_, cx=cx, k=k: centro(c, "10 m²" if k < 2 else "2 m²", cx, 990, 44, "g", TINTA2 if k < 2 else COR, q_))
    E.foco(c, t, c8 + 0.9, 0.5, lambda q: E.pilula(c, "3 latas", 1500, 800, 72, "g", a=q, cor=E.SOBRE))


# ---------------- diagonal ----------------
CX, CY, CA = 250, 900, 400   # o cubo de aresta 2


def b_diagonal(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")

    def bloco():
        pts = E.paralelepipedo(c, t, C["s09"], 240, 860, 520, 300, 300)
        aresta(c, t, b9, pts[0], pts[6], largura=12, d=1.2)
        for P in (pts[0], pts[6]):
            k = ease_back(prog(t, a9 + 0.3, 0.4))
            if k > 0:
                c.drawCircle(*P, 14 * k, M.paint(E.COR))
        E.frase(c, t, a9, [("diagonal", "g", 80, COR)] + ps("do bloco", "i", 74), 1360, 300, "center", 0.1)
        E.frase(c, t, a9 + 0.8, ps("de um canto de baixo ao", "i", 56, TINTA2), 1360, 400, "center", 0.08)
        E.frase(c, t, a9 + 1.6, ps("canto de cima mais distante", "i", 56, TINTA2), 1360, 470, "center", 0.08)
        E.frase(c, t, b9, ps("atravessa", "i", 62) + [("por dentro", "g", 66)], 1360, 620, "center", 0.1)
        E.foco(c, t, c9, 0.5, lambda q: E.pilula(c, "a maior vareta que cabe", 1360, 790, 62, "g", a=q, cor=E.SOBRE))
    fase(c, t, C["s09"], C["s10"] - 0.1, bloco)
    if t < C["s10"] - 0.1:
        return
    pts = E.cubo(c, t, a0, CX, CY, CA)
    for i, j, n in ((0, 1, (0, 1)), (1, 5, (1, 0.3)), (5, 6, (1, 0))):
        rotulo(c, t, a0 + 0.3, "2", pts[i], pts[j], n, 60)
    # diagonal do chão
    if C["s10"] <= t:
        face(c, pts, (0, 1, 5, 4), ep(t, b0, 0.5) * (1 - ep(t, a1, 0.4)), alfa_=0.3)
        aresta(c, t, b0 + 0.3, pts[0], pts[5], TINTA, 9)
        E.foco(c, t, c0, 0.4, lambda q: E.formula(c, "2r{2}", (pts[0][0] + pts[5][0]) / 2 + 20, (pts[0][1] + pts[5][1]) / 2 - 18, 54, "g", TINTA, q, "center"))
    # o triângulo retângulo
    if t >= a1:
        q = ep(t, a1, 0.5)
        p = skia.Path(); p.addPoly([pts[0], pts[5], pts[6]], True)
        c.drawPath(p, M.paint(E.COR, 0.16 * q))
        aresta(c, t, a1 + 0.3, pts[5], pts[6], TINTA, 9)
        reto(c, pts[5], pts[0], pts[6], 36, ep(t, b1, 0.4), E.COR)
        aresta(c, t, c1, pts[0], pts[6], largura=12, d=0.8)
        E.foco(c, t, c1 + 0.6, 0.4, lambda q_: E.escreve(c, "d", (pts[0][0] + pts[6][0]) / 2 - 60, (pts[0][1] + pts[6][1]) / 2 - 10, 70, "g", COR, q_))
    X = 1330

    def texto10():
        E.frase(c, t, a0, ps("cubo de aresta", "i", 70) + [("2", "g", 76, COR)], X, 260, "center", 0.1)
        E.frase(c, t, b0, ps("diagonal do chão (quadrado):", "i", 56, TINTA2), X, 400, "center", 0.08)
        E.formula_em(c, t, c0, "2 × r{2} = 2r{2}", X, 510, 80, "g", TINTA, "center")
        E.frase(c, t, a1, ps("chão, aresta em pé e", "i", 56, TINTA2) + [("d:", "g", 58, COR)], X, 660, "center", 0.08)
        E.frase(c, t, a1 + 0.8, [("triângulo retângulo", "g", 60)], X, 740, "center", 0.08)
        E.frase(c, t, b1, ps("ângulo reto no pé da aresta em pé", "i", 50, TINTA2), X, 830, "center", 0.08)
        E.frase(c, t, c1, [("d", "g", 60, COR)] + ps("é a hipotenusa", "i", 58), X, 930, "center", 0.08)
    fase(c, t, C["s10"], C["s12"] - 0.1, texto10)

    def pitagoras():
        E.frase(c, t, C["s12"] + 0.1, [("Pitágoras", "g", 70, COR)], X, 220, "center")
        E.formula_em(c, t, a2, "(2r{2})^2 = 8", X, 330, 72, "g", TINTA, "center")
        E.formula_em(c, t, b2, "2^2 = 4", X, 430, 72, "g", TINTA, "center")
        E.formula_em(c, t, c2, "d^2 = 8 + 4 = 12", X, 540, 72, "g", TINTA, "center")
        E.formula_em(c, t, d2, "r{12} = r{4 · 3} = 2r{3}", X, 670, 72, "g", TINTA, "center")
        bola_txt(c, t, e2, "d = 2r{3}", X, 840, 130, 64)
        E.frase(c, t, e2 + 0.9, ps("um pouco menos que 3,5", "i", 50, TINTA2), X, 1020, "center", 0.08)
    fase(c, t, C["s12"], C["s13"] - 0.1, pitagoras)
    if t < C["s13"] - 0.1:
        return
    E.formula_em(c, t, a3, "8 = 2^2 + 2^2", X, 300, 76, "g", TINTA, "center")
    E.formula_em(c, t, b3, "d^2 = a^2 + b^2 + c^2", X, 450, 76, "g", TINTA, "center")
    E.formula_em(c, t, c3, "d = r{a^2 + b^2 + c^2}", X, 640, 92, "g", COR, "center")
    E.frase(c, t, d3, [("d:", "g", 56, COR)] + ps("a diagonal", "i", 54), X - 180, 820, "left", 0.08)
    E.frase(c, t, e3, [("a, b, c:", "g", 56, COR)] + ps("as arestas", "i", 54), X - 180, 900, "left", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    E.frase(c, t, C["s14"] + 0.2, [("o erro", "g", 80, ERRADO)] + ps("comum na pintura", "i", 80), W / 2, 170, "center", 0.12)
    pts = E.paralelepipedo(c, t, C["s14"], 200, 760, 480, 320, 160, ("3 m", "2 m", "1 m"), size=50)
    for k, idx in enumerate(((0, 1, 2, 3), (3, 2, 6, 7), (1, 2, 6, 5))):
        face(c, pts, idx, ep(t, a4 + 0.3 * k, 0.4) * (1 - ep(t, d4, 0.4)), ERRADO, 0.3)
    for k, idx in enumerate(((0, 1, 2, 3), (3, 2, 6, 7), (1, 2, 6, 5), (4, 5, 6, 7), (0, 1, 5, 4), (0, 3, 7, 4))):
        face(c, pts, idx, ep(t, d4 + 0.2 * k, 0.4), E.COR, 0.16)
    X = 1330
    E.frase(c, t, a4, ps("somar só", "i", 66) + [("3 faces", "g", 70, ERRADO)], X, 330, "center", 0.1)
    fcen(c, t, b4, "6 + 3 + 2 = 11 m²", X, 450, 72, ERRADO)
    E.frase(c, t, c4, ps("compra", "i", 62) + [("2 latas", "g", 66, ERRADO)], X, 550, "center", 0.1)
    E.frase(c, t, d4, ps("são", "i", 62) + [("6 faces:", "g", 66, COR)] + ps("o dobro,", "i", 62) + [("22 m²", "g", 66, COR)], X, 690, "center", 0.1)
    # a barra dos 22 m²: 20 pintados e 2 sem tinta
    x0, y0, u = 260, 900, 62
    for k in range(22):
        q = ep(t, e4 + 0.03 * k, 0.3)
        if q <= 0:
            continue
        cor = E.COR if k < 20 else ERRADO
        c.drawRect(skia.Rect.MakeXYWH(x0 + k * u, y0, u - 6, 70), M.paint(cor, q * (0.85 if k < 20 else 0.25)))
        c.drawRect(skia.Rect.MakeXYWH(x0 + k * u, y0, u - 6, 70), M.paint(cor, q, stroke=3))
    E.frase(c, t, e4 + 0.7, ps("2 latas = 20 m²", "i", 54, TINTA2), x0, 1030, "left", 0.08)
    E.frase(c, t, e4 + 1.2, [("2 m² sem tinta", "g", 54, ERRADO)], x0 + 20 * u - 140, 1030, "left", 0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    a6, b6, c6, d6, e6 = (C[f"s16.{k}"] for k in "abcde")

    def um():
        E.frase(c, t, C["s15"] + 0.2, ps("o atalho da diagonal", "i", 70, CLARO), W / 2, 170, "center", 0.1)
        # quadrado
        q = ep(t, a5, 0.5)
        if q > 0:
            x, y, l = 260, 360, 260
            c.drawRect(skia.Rect.MakeXYWH(x, y, l, l), M.paint(BR, q * 0.08))
            c.drawRect(skia.Rect.MakeXYWH(x, y, l, l), M.paint(BR, q, stroke=6))
            M.line(c, x, y + l, x + l, y, CLARO, q, 10, progress=ease_io(prog(t, a5 + 0.2, 0.6)))
            E.foco(c, t, a5 + 0.5, 0.4, lambda q_: E.formula(c, "quadrado: r{2}", x + l / 2, y + l + 100, 66, "g", BR, q_, "center"))
        pts = E.cubo(c, t, b5, 1000, 640, 260, escuro=True)
        if t >= b5 + 0.6:
            aresta(c, t, b5 + 0.6, pts[0], pts[6], CLARO, 10, d=0.6)
        E.foco(c, t, b5 + 0.9, 0.4, lambda q_: E.formula(c, "cubo: r{3}", 1180, 740, 66, "g", BR, q_, "center"))
        E.formula_em(c, t, c5, "d = a r{3}", W / 2, 900, 96, "g", BR, "center")
        E.formula_em(c, t, d5, "aresta 2:  d = 2r{3}", W / 2, 1010, 64, "g", CLARO, "center")
    fase(c, t, C["s15"], C["s16"] - 0.1, um)
    if t < C["s16"] - 0.1:
        return
    E.frase(c, t, C["s16"] + 0.2, ps("funciona porque, no cubo,", "i", 66, CLARO) + [("as 3 arestas são iguais", "g", 64, BR)], W / 2, 210, "center", 0.1)
    E.formula_em(c, t, a6, "a^2 + a^2 + a^2", W / 2, 360, 90, "g", BR, "center")
    E.formula_em(c, t, b6, "= 3a^2", W / 2, 480, 90, "g", BR, "center")
    E.formula_em(c, t, c6, "r{3a^2} = a r{3}", W / 2, 620, 90, "g", CLARO, "center")
    E.foco(c, t, d6, 0.5, lambda a: E.selo(c, 470, 800, 50, False, a))
    E.frase(c, t, d6 + 0.1, ps("bloco de arestas diferentes:", "i", 60, CLARO) + [("não serve", "g", 62, BR)], 550, 825, "left", 0.1)
    E.foco(c, t, e6, 0.5, lambda a: E.pilula(c, "some os 3 quadrados", W / 2, 960, 70, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    E.frase(c, t, C["s17"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a7, ps("caixa cúbica de", "i", 66) + [("30 cm", "g", 70, COR)] + ps("de aresta", "i", 66), XE, 340, passo=0.1)
    E.frase(c, t, b7, ps("quanto", "i", 70) + [("papel", "g", 74, COR)] + ps("cobre tudo?", "i", 70), XE, 480, passo=0.1)
    E.frase(c, t, c7, ps("uma", "i", 70) + [("vareta de 50 cm", "g", 70, COR)], XE, 620, passo=0.1)
    E.frase(c, t, c7 + 1.0, ps("cabe de canto a canto?", "i", 70), XE, 710, passo=0.1)
    E.formula_em(c, t, d7, "r{2} ≈ 1,4     r{3} ≈ 1,7", XE, 860, 64, "g", TINTA2)

    def cubo():
        pts = E.cubo(c, t, a7, 1330, 860, 330, "30 cm", size=50)
        aresta(c, t, c7, pts[0], pts[6], largura=10, d=0.8)
    E.saida(c, t, C["s18.a"] - 0.1, cubo)
    E.relogio(c, t, C["s18.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    X = 1330

    def papel():
        pts = E.cubo(c, t, C["s19"], 250, 860, 380, "30 cm", size=50)
        for k, idx in enumerate(((0, 1, 2, 3), (3, 2, 6, 7), (1, 2, 6, 5))):
            face(c, pts, idx, ep(t, a9 + 0.25 * k, 0.4), alfa_=0.3)
        E.frase(c, t, a9, [("6 faces", "g", 70, COR)] + ps("de 30 por 30", "i", 66), X, 300, "center", 0.1)
        fcen(c, t, b9, "30 × 30 = 900", X, 450, 84)
        fcen(c, t, c9, "900 × 6 = 5.400", X, 590, 84)
        bola_txt(c, t, c9 + 0.8, "5.400 cm²", X, 790, 180, 54)
    fase(c, t, C["s19"], C["s20"] - 0.1, papel)
    if t < C["s20"] - 0.1:
        return
    pts = E.cubo(c, t, C["s20"], 250, 860, 380, "30 cm", size=50)
    aresta(c, t, a0, pts[0], pts[6], largura=12, d=0.8)
    if t >= d0:
        face(c, pts, (0, 1, 5, 4), ep(t, d0, 0.4), ERRADO, 0.18)
        aresta(c, t, d0 + 0.2, pts[0], pts[5], ERRADO, 9)
    E.formula_em(c, t, a0, "d = 30r{3}", X, 280, 84, "g", COR, "center")
    fcen(c, t, b0, "30 × 1,7 = 51", X, 410, 80)
    E.frase(c, t, c0, [("51 > 50:", "g", 64, CERTO)] + ps("cabe, por pouco", "i", 62), X, 530, "center", 0.1)
    E.foco(c, t, c0 + 0.6, 0.5, lambda q: E.selo(c, X, 650, 55 * ease_back(prog(t, c0 + 0.6, 0.5)), True, q))
    E.frase(c, t, d0, ps("deitada no chão:", "i", 62) + [("não caberia", "g", 64, ERRADO)], X, 800, "center", 0.1)
    fcen(c, t, e0, "30 × 1,4 = 42", X, 920, 80, ERRADO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        E.foco(c, t, C["s21.a"], 0.5, lambda a: (E.bola(c, 300, 370, 60, a=a), centro(c, "1", 300, 393, 68, "g", E.SOBRE, a)))
        E.frase(c, t, C["s21.a"] + 0.1, ps("área total:", "i", 70) + [("as 6 faces,", "g", 70, COR)] + ps("em pares", "i", 70), 400, 400, "left", 0.12)
        E.foco(c, t, C["s21.b"], 0.5, lambda a: (E.bola(c, 300, 620, 60, a=a), centro(c, "2", 300, 643, 68, "g", E.SOBRE, a)))
        E.frase(c, t, C["s21.b"] + 0.1, ps("diagonal do cubo:", "i", 70), 400, 650, "left", 0.12)
        E.formula_em(c, t, C["s21.b"] + 0.8, "d = a r{3}", 920, 655, 84, "g", COR)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a2, b2, c2, d2, e2 = (C[f"s22.{k}"] for k in "abcde")
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, a2, [("Prisma", "g", 130, COR)], XE, 420)
    E.frase(c, t, a2 + 0.5, ps("de base triangular e hexagonal", "i", 66), XE, 530, passo=0.1)
    E.frase(c, t, b2, ps("volume:", "i", 62, TINTA2) + [("base × altura", "g", 62)], XE, 650, passo=0.1)
    E.frase(c, t, c2, ps("área total:", "i", 62, TINTA2) + [("a soma das faces", "g", 62)], XE, 740, passo=0.1)
    E.prisma(c, t, a2 + 0.3, 1450, 900, 6, 150, 250)
    E.foco(c, t, d2, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d2 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, d2 + 0.2, 0.4))
    E.frase(c, t, e2, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, area=b_area, diagonal=b_diagonal, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
