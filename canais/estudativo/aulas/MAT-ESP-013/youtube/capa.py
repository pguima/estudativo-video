"""Capas do MAT-ESP-013 (1280x720). Uso: python capa.py"""
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
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))


def lata(c, cx, cy, r, h, cor=None, nivel=0.0):
    """cilindro em traço branco; cor = água até a fração nivel"""
    ry, ct = r * SEN, cy - h * COS
    if cor and nivel > 0:
        cn = cy - h * nivel * COS
        p = skia.Path()
        p.moveTo(cx - r, cn); p.lineTo(cx - r, cy)
        p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
        p.lineTo(cx + r, cn)
        p.arcTo(skia.Rect.MakeXYWH(cx - r, cn - ry, 2 * r, 2 * ry), 0, 180, False)
        p.close()
        c.drawPath(p, M.paint(cor, 0.9))
        c.drawOval(skia.Rect.MakeXYWH(cx - r, cn - ry, 2 * r, 2 * ry), M.paint(E.mix(cor, BR, 0.35)))
    pt = M.paint(BR, 1, stroke=8)
    c.drawOval(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), pt)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 0, 180, False, pt)
    M.line(c, cx - r, cy, cx - r, ct, BR, 1, 8); M.line(c, cx + r, cy, cx + r, ct, BR, 1, 8)


def cone(c, cx, cy, r, h, cor=None, geratriz=None):
    """cone em traço branco; cor = corpo pintado; geratriz = cor da linha inclinada da direita"""
    ry, vy = r * SEN, cy - h * COS
    p = skia.Path()
    p.moveTo(cx, vy); p.lineTo(cx - r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
    p.close()
    if cor:
        c.drawPath(p, M.paint(cor, 0.9))
    pt = M.paint(BR, 1, stroke=8)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)
    if geratriz:
        M.line(c, cx, vy, cx + r, cy, geratriz, 1, 14)


def a(c):  # o gancho: 3 cones enchem 1 cilindro
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    for k in range(3):
        cone(c, 170 + k * 230, 520, 90, 260, AMARELO if k == 0 else None)
    E.escreve(c, "3 cones", 110, 740, 130, "g", AMARELO)
    E.escreve(c, "= 1 cilindro", 110, 900, 120, "g", BR)
    lata(c, 1260, 920, 200, 560, AMARELO, 1.0)
    E.escreve(c, "por quê?", 1500, 300, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Cone", "geratriz,", "área e volume")


def d(c):  # o atalho do volume com π = 3
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "volume do cone com", 84, 340, 96, "i", BR)
    E.formula(c, "π = 3", 84 + E.larg("volume do cone com", "i", 96) + 30, 340, 96, "g", BR)
    E.formula(c, "V = r² · h", 80, 600, 190, "g", AMARELO)
    E.escreve(c, "o atalho", 84, 800, 130, "g", BR)
    cone(c, 1580, 960, 200, 620, COR, AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_tres_cones", a), ("capa_B_cone_geratriz_area_volume", b), ("capa_C_pi_igual_a_tres", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
