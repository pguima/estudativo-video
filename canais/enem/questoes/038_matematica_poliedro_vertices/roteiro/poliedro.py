"""Poliedros em 3D para a questão 151 (cúpula pentagonal giralongada, J24) e para o cubo do exemplo, desenhados em skia.
Geometria exata com aresta 1: antiprisma decagonal (altura HA) + cúpula pentagonal (altura HC) colada por cima.
Anéis de vértices: 0 = pentágono de cima (5), 1 = decágono do meio (10), 2 = decágono de baixo (10) → 25 vértices.
Faces: 25 triângulos (5 da cúpula + 20 do antiprisma), 5 quadrados, 1 pentágono, 1 decágono = 32; arestas = 55.
O sólido é convexo: basta descartar as faces de costas (sem ordenar), e o modo "vidro" desenha as de costas apagadas."""
import math
from functools import lru_cache

import skia

R5 = 1 / (2 * math.sin(math.pi / 5))      # raio do pentágono de aresta 1
R10 = 1 / (2 * math.sin(math.pi / 10))    # raio do decágono de aresta 1
HC = math.sqrt(1 - 1 / (4 * math.sin(math.pi / 5) ** 2))           # altura da cúpula pentagonal ≈ 0,526
HA = math.sqrt(1 - 1 / (4 * math.cos(math.pi / 20) ** 2))          # altura do antiprisma decagonal ≈ 0,862


def _anel(r, z, n, fase):
    return [(r * math.cos(fase + 2 * math.pi * k / n), r * math.sin(fase + 2 * math.pi * k / n), z) for k in range(n)]


@lru_cache(None)
def j24():
    """(vértices, faces, anel de cada vértice); faces = (tipo, índices) com os índices no sentido anti-horário visto de fora"""
    d18 = math.radians(18)
    P = _anel(R5, HA + HC, 5, 0.0)            # 0..4
    D = _anel(R10, HA, 10, d18)               # 5..14   (ângulos 18° + 36°j)
    B = _anel(R10, 0.0, 10, 0.0)              # 15..24  (ângulos 36°j)
    V = P + D + B
    p = lambda k: k % 5
    d = lambda j: 5 + j % 10
    b = lambda j: 15 + j % 10
    F = [("pent", tuple(range(5)))]
    for k in range(5):
        F.append(("sq", (p(k), d(2 * k), d(2 * k + 1), p(k + 1))))
        F.append(("tri_c", (p(k), d(2 * k - 1), d(2 * k))))
    for j in range(10):
        F.append(("tri_a", (d(j), b(j), b(j + 1))))
        F.append(("tri_a", (d(j), b(j + 1), d(j + 1))))
    F.append(("dec", tuple(b(j) for j in range(9, -1, -1))))
    anel = [0] * 5 + [1] * 10 + [2] * 10
    return _orienta(V, F), anel


@lru_cache(None)
def cubo():
    V = [(x, y, z) for z in (-1, 1) for y in (-1, 1) for x in (-1, 1)]
    F = [("sq", f) for f in ((0, 1, 3, 2), (4, 6, 7, 5), (0, 4, 5, 1), (2, 3, 7, 6), (0, 2, 6, 4), (1, 5, 7, 3))]
    return _orienta(V, F), [0] * 8


@lru_cache(None)
def icosaedro():
    f = (1 + math.sqrt(5)) / 2
    V = []
    for a in (-1, 1):
        for b in (-f, f):
            V += [(0, a, b), (a, b, 0), (b, 0, a)]
    F = [("tri_a", (i, j, k)) for i in range(12) for j in range(i + 1, 12) for k in range(j + 1, 12)
         if all(abs(math.dist(V[x], V[y]) - 2) < 1e-6 for x, y in ((i, j), (j, k), (i, k)))]
    return _orienta(V, F), [0] * 12


def _orienta(V, F):
    """garante a ordem anti-horária vista de fora (normal apontando para longe do centro)"""
    cx, cy, cz = (sum(v[i] for v in V) / len(V) for i in range(3))
    out = []
    for tipo, f in F:
        a, b_, c = V[f[0]], V[f[1]], V[f[2]]
        u = [b_[i] - a[i] for i in range(3)]; w = [c[i] - a[i] for i in range(3)]
        n = (u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0])
        m = [sum(V[k][i] for k in f) / len(f) for i in range(3)]
        if n[0] * (m[0] - cx) + n[1] * (m[1] - cy) + n[2] * (m[2] - cz) < 0:
            f = tuple(reversed(f))
        out.append((tipo, f))
    return V, out


def arestas(F):
    s = set()
    for _, f in F:
        for i in range(len(f)):
            s.add(tuple(sorted((f[i], f[(i + 1) % len(f)]))))
    return sorted(s)


def _hex(c):
    c = c.lstrip("#")
    return [int(c[i:i + 2], 16) for i in (0, 2, 4)]


def _cor(c, k, a):
    r, g, b = (max(0, min(255, int(v * k))) for v in _hex(c))
    return skia.Color(r, g, b, max(0, min(255, int(255 * a))))


def projeta(V, rot, tilt, escala, cx, cy, zc=0.0, f=9.0):
    """gira em torno do eixo vertical (rot) e inclina para a câmera (tilt); devolve pontos de tela e profundidades"""
    cr, sr, ct, st = math.cos(rot), math.sin(rot), math.cos(tilt), math.sin(tilt)
    out = []
    for x, y, z in V:
        z -= zc
        x1, y1 = x * cr - y * sr, x * sr + y * cr           # giro no eixo z (vertical do sólido)
        y2, z2 = y1 * ct - z * st, y1 * st + z * ct          # inclinação: a câmera olha um pouco de cima
        s = f / (f + y2)                                     # y2 = profundidade (positivo = longe)
        out.append((cx + x1 * escala * s, cy - z2 * escala * s, y2))
    return out


def desenha(c, solido, cx, cy, escala, rot, tilt, a, cores, modo="solido", foco=None, k_tipo=None,
            vert=None, cor_vert="#FFFFFF", r_vert=11, linha="#0B1020", zc=None, k_ar=0.0, cor_ar="#4CC9F0"):
    """foco = tipos de face em destaque (os outros apagados); k_tipo = {tipo: 0..1} para acender por tipo;
    vert = {anel: alpha} para marcar os vértices (os de costas aparecem mais fracos); modo "vidro" mostra as de costas"""
    if a <= 0:
        return []
    (V, F), anel = solido
    if zc is None:
        zc = (max(v[2] for v in V) + min(v[2] for v in V)) / 2
    P = projeta(V, rot, tilt, escala, cx, cy, zc)
    luz = (-0.45, -0.75, 0.5)                               # de cima, da esquerda, de frente
    ln = math.sqrt(sum(v * v for v in luz)); luz = [v / ln for v in luz]
    frente, costas = [], []
    for tipo, f in F:
        pts = [P[i] for i in f]
        area = sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1] for i in range(len(pts)))
        (frente if area < 0 else costas).append((tipo, f, pts))
    vis = set()

    def face(tipo, pts, alfa, k_luz):
        kt = 1.0 if k_tipo is None else k_tipo.get(tipo, 0.0)
        dim = 1.0 if (foco is None or tipo in foco) else 0.28
        al = alfa * dim * (0.25 + 0.75 * kt)
        path = skia.Path()
        path.moveTo(pts[0][0], pts[0][1])
        for x, y, _ in pts[1:]:
            path.lineTo(x, y)
        path.close()
        p = skia.Paint(AntiAlias=True, Color=_cor(cores[tipo], k_luz * (0.35 + 0.65 * kt), al))
        c.drawPath(path, p)
        e = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=max(1.5, escala * 0.018),
                       StrokeJoin=skia.Paint.kRound_Join, Color=_cor(linha, 1.0, al))
        c.drawPath(path, e)

    if modo == "vidro":
        for tipo, f, pts in costas:
            face(tipo, pts, a * 0.22, 0.8)
    for tipo, f, pts in frente:
        # luz pela normal no espaço da câmera (aproximada pela normal 3D girada)
        n = _normal_vista([V[i] for i in f], rot, tilt)
        lam = max(0.0, sum(n[i] * luz[i] for i in range(3)))
        face(tipo, pts, a * (0.62 if modo == "vidro" else 1.0), 0.62 + 0.5 * lam)
        vis.update(f)
    if k_ar > 0:   # arestas em destaque: as da frente cheias, as de trás fracas
        lado = {}
        for tipo, f, pts in frente:
            for i in range(len(f)):
                lado[tuple(sorted((f[i], f[(i + 1) % len(f)])))] = True
        w = max(3.0, escala * 0.03)
        for i, j in arestas(F):
            al = a * k_ar * (1.0 if lado.get((i, j)) else 0.3)
            e = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=w, StrokeCap=skia.Paint.kRound_Cap,
                           Color=_cor(cor_ar, 1, al))
            c.drawLine(P[i][0], P[i][1], P[j][0], P[j][1], e)
    if vert:
        for i, (x, y, _) in enumerate(P):
            av = vert.get(anel[i], 0.0)
            if av <= 0:
                continue
            frente_v = i in vis
            al = a * av * (1.0 if frente_v else 0.45)
            c.drawCircle(x, y, r_vert + 3, skia.Paint(AntiAlias=True, Color=_cor("#0B1020", 1, al)))
            c.drawCircle(x, y, r_vert, skia.Paint(AntiAlias=True, Color=_cor(cor_vert, 1, al)))
    return P


def _normal_vista(pts, rot, tilt):
    cr, sr, ct, st = math.cos(rot), math.sin(rot), math.cos(tilt), math.sin(tilt)
    q = []
    for x, y, z in pts:
        x1, y1 = x * cr - y * sr, x * sr + y * cr
        q.append((x1, -(y1 * st + z * ct), y1 * ct - z * st))   # (tela x, tela y para baixo, profundidade)
    a, b, c = q[0], q[1], q[2]
    u = [b[i] - a[i] for i in range(3)]; w = [c[i] - a[i] for i in range(3)]
    n = (u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0])
    m = math.sqrt(sum(v * v for v in n)) or 1
    n = [v / m for v in n]
    return n if n[2] < 0 else [-v for v in n]                   # virada para a câmera


if __name__ == "__main__":
    (V, F), anel = j24()
    from collections import Counter
    print("V", len(V), "F", len(F), Counter(t for t, _ in F), "A", len(arestas(F)), "HA", round(HA, 4), "HC", round(HC, 4))
    for i, j in arestas(F):
        L = math.dist(V[i], V[j])
        assert abs(L - 1) < 1e-6, (i, j, L)
    print("todas as arestas = 1; Euler:", len(V) - len(arestas(F)) + len(F))
    (V, F), _ = icosaedro(); print("icosaedro V", len(V), "F", len(F), "A", len(arestas(F)))
