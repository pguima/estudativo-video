"""Capas do MAT-TOP-011 (1280x720). Uso: python capa.py"""
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


def elipse(c, cx, cy, rx, ry, cor, lw):
    c.drawOval(skia.Rect.MakeXYWH(cx - rx, cy - ry, 2 * rx, 2 * ry), M.paint(cor, 1, stroke=lw))


def a(c):  # o gancho: onde ficam os focos?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "f{x^2}{25} + f{y^2}{9} = 1", 84, 520, 170, "g", BR)
    cx, cy, rx, ry = 1450, 760, 380, 228
    elipse(c, cx, cy, rx, ry, BR, 14)
    X = (cx + rx * math.cos(1.0), cy - ry * math.sin(1.0))
    for fx in (cx - 304, cx + 304):
        M.line(c, fx, cy, *X, AMARELO, 1, 7)
        c.drawCircle(fx, cy, 22, M.paint(AMARELO))
    c.drawCircle(*X, 18, M.paint(BR))
    E.escreve(c, "?", cx - 50, cy + 70, 200, "g", AMARELO)
    E.escreve(c, "onde ficam os focos?", 84, 840, 104, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Elipse", "e focos", "em 5 segundos")


def d(c):  # o macete: c² = maior − menor
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o maior manda:", 84, 360, 140, "i", BR)
    E.formula(c, "c^2 = 25 − 9", 76, 620, 210, "g", BR)
    E.formula(c, "c = 4", 1220, 900, 190, "g", "#3CC7D3")
    E.escreve(c, "sem triângulo", 84, 900, 110, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_onde_ficam_os_focos", a), ("capa_B_elipse_e_focos", b), ("capa_C_o_maior_manda", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
