"""Capas do MAT-ESP-016 (1280x720). Uso: python capa.py"""
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


def cone(c, cx, cy, r, h, cor=None):
    """cone em traço branco; cor = corpo pintado"""
    ry, vy = r * SEN, cy - h * COS
    p = skia.Path()
    p.moveTo(cx, vy); p.lineTo(cx - r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
    p.close()
    if cor:
        c.drawPath(p, M.paint(cor, 0.9))
    pt = M.paint(BR, 1, stroke=8); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)


def piramide(c, cx, cy, s, h, cor=None):
    """pirâmide de base quadrada em traço branco (frente e lado direito)"""
    d = s * 0.35
    A, B, Cc = (cx - s / 2, cy), (cx + s / 2 - d * 0.3, cy), (cx + s / 2 + d * 0.6, cy - d * 0.55)
    V = (cx + d * 0.1, cy - h)
    pt = M.paint(BR, 1, stroke=8); pt.setStrokeJoin(skia.Paint.kRound_Join)
    p = skia.Path(); p.addPoly([A, B, Cc, V], True)
    if cor:
        c.drawPath(p, M.paint(cor, 0.9))
    c.drawPath(p, pt)
    M.line(c, *V, *B, BR, 1, 8)


def bola(c, cx, cy, r, cor=None):
    if cor:
        c.drawCircle(cx, cy, r, M.paint(cor, 0.9))
    c.drawCircle(cx, cy, r, M.paint(BR, 1, stroke=8))
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r * SEN, 2 * r, 2 * r * SEN), 0, 180, False, M.paint(BR, 1, stroke=6))


def a(c):  # o gancho: qual pacote de pipoca cabe mais?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    cone(c, 300, 900, 160, 560)
    piramide(c, 760, 900, 300, 520)
    E.escreve(c, "mesma altura", 1060, 360, 90, "i", BR)
    E.escreve(c, "qual cabe", 1060, 560, 130, "g", BR)
    E.escreve(c, "mais?", 1060, 760, 190, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "pirâmide,", "cone e esfera")


def d(c):  # o atalho do pi igual a três
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "com", 84, 330, 96, "i", BR)
    E.formula(c, "π = 3", 84 + E.larg("com", "i", 96) + 30, 330, 96, "g", BR)
    E.escreve(c, "cone:", 84, 560, 90, "i", BR)
    E.formula(c, "r² · h", 340, 560, 150, "g", AMARELO)
    E.escreve(c, "esfera:", 84, 800, 90, "i", BR)
    E.formula(c, "4r^3", 400, 800, 150, "g", AMARELO)
    cone(c, 1450, 760, 150, 480, COR)
    bola(c, 1680, 860, 120, COR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_cabe_mais", a), ("capa_B_praticando_piramide_cone_esfera", b), ("capa_C_pi_igual_a_tres", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
