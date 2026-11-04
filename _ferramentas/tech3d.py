"""Peças 3D para os vídeos do canal Tecnologia (tema tech): perspectiva real com skia + numpy.
- extrude / extrude_path: texto ou caminho extrudado (face na frente, laterais escurecendo), com reflexo opcional
- star3d / star2d: estrela do GitHub extrudada girando
- cuboid + rot + project: caixas 3D com sombreamento (gráficos de barras 3D)
- spin_in: rotação de entrada que para quase de frente, com balanço lento
- icon_solid: ícone vetorial do motor como área preenchida (para extrudar)
Usar 3D só onde ele carrega informação (posição no ranking, número principal, gráfico), não como enfeite.
"""
import math
from functools import lru_cache
import numpy as np
import skia
import motor
from motor import clamp, lerp, mix, ease_out, paint, font

INK = "#EAF2FF"
CYAN = "#22D3EE"
GOLD = "#FBBF24"


def spin_in(t, t0, d=0.9, ry0=-1.35, ry1=-0.30, sway=0.05):
    u = ease_out(clamp((t - t0) / d))
    return lerp(ry0, ry1, u) + sway * math.sin((t - t0) * 0.7) * u


FOC = 1500.0


def rot(rx, ry, rz=0.0):
    cx, sx, cy, sy, cz, sz = math.cos(rx), math.sin(rx), math.cos(ry), math.sin(ry), math.cos(rz), math.sin(rz)
    Rx = np.array([[1, 0, 0], [0, cx, -sx], [0, sx, cx]])
    Ry = np.array([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]])
    Rz = np.array([[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]])
    return Ry @ Rx @ Rz


def project(P, cx, cy, foc=FOC):
    """P: (n,3) já em coordenadas de câmera (z para dentro da tela). Retorna (n,2)."""
    z = foc + P[:, 2]
    return np.stack([cx + P[:, 0] * foc / z, cy + P[:, 1] * foc / z], 1)


def _quad_matrix(src_rect, quad):
    m = skia.Matrix()
    l, t, r, b = src_rect
    src = [skia.Point(l, t), skia.Point(r, t), skia.Point(r, b), skia.Point(l, b)]
    dst = [skia.Point(float(x), float(y)) for x, y in quad]
    m.setPolyToPoly(src, dst)
    return m


@lru_cache(512)
def glyph_path(s, peso, size):
    f = font(peso, size)
    gl = f.textToGlyphs(s)
    ws = f.getWidths(gl)
    path, x = skia.Path(), 0.0
    for g, w in zip(gl, ws):
        p = f.getPath(g)
        if p is not None:
            p.offset(x, 0)
            path.addPath(p)
        x += w
    return path, x


def extrude_path(c, path, cx, cy, a=1.0, rx=0.0, ry=0.0, depth=60, face=INK, side=CYAN, layers=22, glow=0.0,
                 shine=None, blur=None):
    """Extrusão em perspectiva real de um caminho 2D (face na frente, laterais escurecendo para trás). cx, cy = centro."""
    if a <= 0:
        return
    b = path.computeTightBounds()
    l, t_, r, bt = b.left(), b.top(), b.right(), b.bottom()
    ox, oy = (l + r) / 2, (t_ + bt) / 2
    R = rot(rx, ry)
    corners = np.array([[l - ox, t_ - oy], [r - ox, t_ - oy], [r - ox, bt - oy], [l - ox, bt - oy]])

    def quad(z):
        return project(np.c_[corners, np.full(4, z)] @ R.T, cx, cy)

    src = (l, t_, r, bt)
    for i in range(layers, 0, -1):
        f = i / layers
        c.save(); c.concat(_quad_matrix(src, quad(depth * f)))
        c.drawPath(path, paint(mix(side, "#000000", 0.2 + 0.62 * f), a))
        c.restore()
    c.save(); c.concat(_quad_matrix(src, quad(0)))
    if glow > 0:
        p = paint(side, a * glow); p.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, (blur or max(b.height(), 40) * 0.08)))
        c.drawPath(path, p)
    fp = paint(face, a)
    if shine is not None and 0 < shine < 1:   # reflexo diagonal que atravessa a face
        x0 = lerp(l - 0.6 * (r - l), r + 0.6 * (r - l), shine)
        fc = skia.Color(*[int(face.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)])
        fp.setShader(skia.GradientShader.MakeLinear([skia.Point(x0 - 140, t_), skia.Point(x0 + 140, bt)],
                                                    [fc, skia.Color(255, 255, 255), fc], [0.0, 0.5, 1.0]))
    c.drawPath(path, fp)
    c.restore()


def extrude(c, s, cx, cy, size, a=1.0, rx=0.0, ry=0.0, depth=60, peso="black", **kw):
    """texto extrudado (Inter Black por padrão) centrado em (cx, cy)"""
    path, _ = glyph_path(s, peso, size)
    extrude_path(c, path, cx, cy, a, rx, ry, depth, **kw)


def _shade(col, k):
    return mix("#000000", col, clamp(k, 0.0, 1.0))


def cuboid(c, cx, cy, R, x, y, z, w, h, d, col, a=1.0, top=None, edge=None):
    """caixa 3D com a base em (x, y, z) e altura h para CIMA (y negativo). Faces com sombreamento por luz fixa."""
    V = np.array([[x, y, z], [x + w, y, z], [x + w, y, z + d], [x, y, z + d],
                  [x, y - h, z], [x + w, y - h, z], [x + w, y - h, z + d], [x, y - h, z + d]], float)
    P = V @ R.T
    Q = project(P, cx, cy)
    faces = [((4, 5, 6, 7), (0, -1, 0), top or col), ((0, 1, 5, 4), (0, 0, -1), col), ((1, 2, 6, 5), (1, 0, 0), col),
             ((3, 0, 4, 7), (-1, 0, 0), col), ((2, 3, 7, 6), (0, 0, 1), col)]
    L = np.array([-0.45, -0.8, -0.55]); L /= np.linalg.norm(L)
    out = []
    for idx, n, fc in faces:
        nn = R @ np.array(n, float)
        pts = Q[list(idx)]
        area = sum(pts[i][0] * pts[(i + 1) % 4][1] - pts[(i + 1) % 4][0] * pts[i][1] for i in range(4))
        if area >= 0:   # face de costas (ordem dos vértices + y para baixo)
            continue
        k = 0.35 + 0.65 * max(0.0, float(-(nn @ L)))
        out.append((float(P[list(idx), 2].mean()), pts, _shade(fc, k)))
    for _, pts, fc in sorted(out, key=lambda o: -o[0]):
        p = skia.Path(); p.moveTo(*pts[0])
        for q in pts[1:]:
            p.lineTo(*q)
        p.close()
        c.drawPath(p, paint(fc, a))
        if edge:
            c.drawPath(p, paint(edge, a * 0.5, stroke=1.2))
    return Q


def star_path(r, k=0.45):
    p = skia.Path()
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * k
        (p.moveTo if i == 0 else p.lineTo)(rr * math.cos(ang), rr * math.sin(ang))
    p.close()
    return p


def star3d(c, cx, cy, r, a=1.0, ry=0.0, rx=0.15, depth=None, col=GOLD, layers=16):
    """estrela do GitHub extrudada e girando"""
    if a <= 0:
        return
    path = star_path(r)
    depth = depth or r * 0.32
    R = rot(rx, ry)
    corners = np.array([[-r, -r], [r, -r], [r, r], [-r, r]], float)
    src = (-r, -r, r, r)
    front_first = (R @ np.array([0, 0, -1.0]))[2] < 0
    zs = [depth * i / layers for i in range(layers, -1, -1)]
    if not front_first:
        zs = zs[::-1]
    for i, z in enumerate(zs):
        P = np.c_[corners, np.full(4, z - depth / 2)] @ R.T
        quad = project(P, cx, cy)
        last = i == len(zs) - 1
        shade = 1.0 if last else 0.45 + 0.25 * (i / len(zs))
        c.save(); c.concat(_quad_matrix(src, quad))
        c.drawPath(path, paint(mix("#000000", col, shade), a))
        c.restore()


def star2d(c, cx, cy, r, col=GOLD, a=1.0):
    p = star_path(r); p.offset(cx, cy)
    c.drawPath(p, paint(col, a))


# ======================================================================  FUNDO


def icon_solid(glyph, size):
    """ícone vetorial do motor (contorno) convertido em área preenchida, com o lado maior = size; para extrude_path"""
    if glyph == "+":
        k = size * 0.22
        p = skia.Path()
        p.addRect(skia.Rect.MakeXYWH(-k / 2, -size / 2, k, size)); p.addRect(skia.Rect.MakeXYWH(-size / 2, -k / 2, size, k))
        p.setFillType(skia.PathFillType.kWinding)
        return p
    src = motor.icon_path(glyph)
    bb = src.computeTightBounds()
    s = size / max(bb.width(), bb.height())
    m = skia.Matrix(); m.setScale(s, s); m.preTranslate(-bb.centerX(), -bb.centerY())
    p = skia.Path(src); p.transform(m)
    st = skia.Paint(); st.setStyle(skia.Paint.kStroke_Style); st.setStrokeWidth(size * 0.075)
    st.setStrokeCap(skia.Paint.kRound_Cap); st.setStrokeJoin(skia.Paint.kRound_Join)
    out = skia.Path()
    st.getFillPath(p, out)
    return out
