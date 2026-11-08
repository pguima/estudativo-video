"""Capas do MAT-ARE-004 (1280x720). Uso: python capa.py"""
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


def poli(c, pts, cor, alfa, borda=BR, larg=7):
    p = skia.Path(); p.addPoly(pts, True)
    if alfa > 0:
        c.drawPath(p, M.paint(cor, alfa))
    pt = M.paint(borda, 1, stroke=larg); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)


def a(c):  # o gancho: duas bases, qual entra na conta?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    x, y, k = 110, 380, 80
    pts = [(x, y + 4 * k), (x + 10 * k, y + 4 * k), (x + 8 * k, y), (x + 2 * k, y)]
    poli(c, pts, BR, 0.9, BR, 6)
    M.line(c, x, y + 4 * k, x + 10 * k, y + 4 * k, AMARELO, 1, 16)
    M.line(c, x + 2 * k, y, x + 8 * k, y, AMARELO, 1, 16)
    E.centro(c, "10", x + 5 * k, y + 4 * k + 120, 100, "g", BR)
    E.centro(c, "6", x + 5 * k, y - 40, 100, "g", BR)
    E.escreve(c, "qual base", 1000, 470, 130, "i", BR)
    E.escreve(c, "entra?", 1000, 640, 160, "g", BR)
    E.escreve(c, "as duas", 1000, 880, 160, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Área do", "trapézio", "e do losango")


def d(c):  # o atalho: a base do meio
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    x, y, k = 110, 460, 66
    pts = [(x, y + 4 * k), (x + 10 * k, y + 4 * k), (x + 8 * k, y), (x + 2 * k, y)]
    poli(c, pts, claro, 0.3, claro, 6)
    M.line(c, x + k, y + 2 * k, x + 9 * k, y + 2 * k, BR, 1, 12)
    E.centro(c, "8", x + 5 * k, y + 2 * k - 24, 90, "g", BR)
    E.escreve(c, "o atalho", 900, 380, 130, "i", BR)
    E.escreve(c, "a base", 890, 580, 160, "g", BR)
    E.escreve(c, "do meio", 890, 760, 160, "g", claro)
    E.escreve(c, "8 × 4 = 32", 900, 950, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_as_duas_bases", a), ("capa_B_area_trapezio", b), ("capa_C_base_do_meio", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
