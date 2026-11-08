"""Capas do MAT-ESP-018 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
KX, KY = 0.394, -0.308
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))
_PEDRA = [(1.0, 0.0), (0.78, 0.55), (0.25, 0.82), (-0.42, 0.7), (-0.95, 0.28), (-0.88, -0.35), (-0.4, -0.75), (0.3, -0.68), (0.82, -0.42)]


def pedra(c, cx, cy, s, cor):
    pts = [(cx + s * u, cy + s * v * 0.72) for u, v in _PEDRA]
    n = len(pts)
    m = [((pts[i][0] + pts[(i + 1) % n][0]) / 2, (pts[i][1] + pts[(i + 1) % n][1]) / 2) for i in range(n)]
    p = skia.Path(); p.moveTo(*m[-1])
    for i in range(n):
        p.quadTo(pts[i][0], pts[i][1], m[i][0], m[i][1])
    p.close()
    c.drawPath(p, M.paint(cor, 0.95))
    pt = M.paint(BR, 1, stroke=7); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)


def aquario(c, x, y, w, d, h, n0, n1):
    """caixa em traço branco com água até n0 e a camada que subiu (n0 a n1) em amarelo"""
    dx, dy = KX * d, KY * d
    for (a, b), cor, al in (((0, n0), BR, 0.35), ((n0, n1), AMARELO, 0.95)):
        h0, hh = h * a, h * b
        for pts in ([(x + w, y - h0), (x + w + dx, y + dy - h0), (x + w + dx, y + dy - hh), (x + w, y - hh)],
                    [(x, y - hh), (x + w, y - hh), (x + w + dx, y - hh + dy), (x + dx, y - hh + dy)],
                    [(x, y - h0), (x + w, y - h0), (x + w, y - hh), (x, y - hh)]):
            p = skia.Path(); p.addPoly(pts, True)
            c.drawPath(p, M.paint(cor, al * 0.8))
    pt = M.paint(BR, 1, stroke=7)
    for (x0, y0, x1, y1) in ((x, y, x + w, y), (x + w, y, x + w, y - h), (x + w, y - h, x, y - h), (x, y - h, x, y),
                             (x, y - h, x + dx, y - h + dy), (x + w, y - h, x + w + dx, y - h + dy), (x + w, y, x + w + dx, y + dy),
                             (x + dx, y - h + dy, x + w + dx, y - h + dy), (x + w + dx, y - h + dy, x + w + dx, y + dy)):
        c.drawLine(x0, y0, x1, y1, pt)


def a(c):  # o gancho: a pedra torta e a água que sobe
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    aquario(c, 110, 960, 640, 380, 560, 0.5, 0.64)
    pedra(c, 110 + 320 + 75, 960 - 60, 90, E.mix(COR, "#000000", 0.35))
    E.escreve(c, "volume de", 1000, 380, 110, "i", BR)
    E.escreve(c, "uma pedra", 1000, 520, 120, "g", BR)
    E.escreve(c, "torta?", 1000, 720, 190, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Volume", "pelo nível", "da água")


def d(c):  # o atalho: transborda? compare com o espaço vazio
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "transborda?", 84, 340, 110, "i", BR)
    E.escreve(c, "compare com o", 84, 560, 110, "g", BR)
    E.escreve(c, "espaço vazio", 84, 740, 150, "g", AMARELO)
    cx, cy, r, h = 1560, 980, 170, 640
    ry, ct = r * SEN, cy - h * COS
    nv = cy - h * 0.8 * COS
    p = skia.Path()
    p.moveTo(cx - r, nv); p.lineTo(cx - r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
    p.lineTo(cx + r, nv); p.arcTo(skia.Rect.MakeXYWH(cx - r, nv - ry, 2 * r, 2 * ry), 0, 180, False); p.close()
    c.drawPath(p, M.paint(COR, 0.9))
    c.drawRect(skia.Rect.MakeLTRB(cx - r, ct, cx + r, nv), M.paint(AMARELO, 0.85))
    c.drawOval(skia.Rect.MakeXYWH(cx - r, nv - ry, 2 * r, 2 * ry), M.paint(E.mix(COR, BR, 0.3)))
    pt = M.paint(BR, 1, stroke=8)
    c.drawOval(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), pt)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 0, 180, False, pt)
    M.line(c, cx - r, cy, cx - r, ct, BR, 1, 8); M.line(c, cx + r, cy, cx + r, ct, BR, 1, 8)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_pedra_torta", a), ("capa_B_volume_pelo_nivel_da_agua", b), ("capa_C_espaco_vazio", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
