"""Capas do MAT-ARE-005 (1280x720). Uso: python capa.py"""
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


def hexa(cx, cy, r):
    return [(cx + r * math.cos(math.radians(60 + 60 * k)), cy + r * math.sin(math.radians(60 + 60 * k))) for k in range(6)]


def fatias(c, cx, cy, r, c1, c2, borda):
    V = hexa(cx, cy, r)
    for k in range(6):
        p = skia.Path(); p.addPoly([(cx, cy), V[k], V[(k + 1) % 6]], True)
        c.drawPath(p, M.paint(c1 if k % 2 == 0 else c2))
        pt = M.paint(borda, 1, stroke=6); pt.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(p, pt)


def a(c):  # o gancho: o hexágono é seis triângulos
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    fatias(c, 480, 600, 330, BR, E.mix(COR, BR, 0.55), COR)
    E.escreve(c, "6 triângulos", 940, 470, 130, "g", BR)
    E.escreve(c, "e mais nada", 950, 640, 120, "i", BR)
    E.formula(c, "A = 6r{3}", 950, 880, 150, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Área do", "hexágono", "e do equilátero")


def d(c):  # o atalho: a metade do lado
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho", 110, 360, 130, "i", BR)
    E.escreve(c, "metade do lado,", 100, 560, 140, "g", BR)
    E.escreve(c, "ao quadrado", 100, 720, 140, "g", claro)
    E.formula(c, "lado 6:  3² = 9  →  9r{3}", 110, 930, 100, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_seis_triangulos", a), ("capa_B_area_hexagono", b), ("capa_C_metade_do_lado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
