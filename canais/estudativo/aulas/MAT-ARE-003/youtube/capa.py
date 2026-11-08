"""Capas do MAT-ARE-003 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"


def poli(c, pts, cor, alfa, borda=BR, larg=7, dash=False):
    p = skia.Path(); p.addPoly(pts, True)
    if alfa > 0:
        c.drawPath(p, M.paint(cor, alfa))
    pt = M.paint(borda, 1, stroke=larg); pt.setStrokeJoin(skia.Paint.kRound_Join)
    if dash:
        pt.setPathEffect(skia.DashPathEffect.Make([24, 18], 0))
    c.drawPath(p, pt)


def a(c):  # o gancho: base 10, altura 6, a área é 60?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    x, y, w, h = 110, 330, 760, 456
    A, B, V = (x, y + h), (x + w, y + h), (x + 300, y)
    poli(c, [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], BR, 0.0, AMARELO, 6, dash=True)
    poli(c, [A, B, V], BR, 0.9, BR, 6)
    E.escreve(c, "10 × 6 = 60?", 990, 470, 140, "g", BR)
    E.escreve(c, "a área é", 1000, 700, 110, "i", BR)
    E.escreve(c, "a metade", 990, 880, 150, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Área do", "triângulo", "e do paralelogramo")


def d(c):  # o atalho: divida por 2 antes
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho", 110, 360, 130, "i", BR)
    E.escreve(c, "divida por 2", 100, 560, 160, "g", BR)
    E.escreve(c, "antes", 100, 730, 160, "g", claro)
    E.formula(c, "f{10 × 6}{2}", 1440, 640, 150, "g", BR, 1, "center")
    E.escreve(c, "= 5 × 6 = 30", 1150, 960, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_metade", a), ("capa_B_area_triangulo", b), ("capa_C_divida_antes", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
