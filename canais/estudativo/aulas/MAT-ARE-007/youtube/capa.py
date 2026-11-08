"""Capas do MAT-ARE-007 (1280x720). Uso: python capa.py"""
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
LILAS = "#C9C9FF"


def hexagono(c, cx, cy, r, tinta=BR):
    pts = [(cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a))) for a in range(0, 360, 60)]
    path = skia.Path(); path.addPoly(pts, True)
    c.drawPath(path, M.paint(LILAS, 0.35))
    for P in pts:
        M.line(c, cx, cy, *P, tinta, 0.6, 5)
    p = M.paint(tinta, 1, stroke=12); p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, p)


def a(c):  # o gancho: quantos galões?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    hexagono(c, 450, 600, 290)
    E.escreve(c, "4 m", 380, 990, 90, "g", BR)
    E.escreve(c, "2 galões", 900, 430, 150, "g", BR)
    E.escreve(c, "bastam?", 900, 610, 190, "g", AMARELO)
    E.escreve(c, "5 situações de obra", 900, 820, 90, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Área e", "perímetro", "5 situações de obra")


def d(c):  # o atalho: vezes 15
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho do preço", 110, 380, 120, "i", BR)
    E.escreve(c, "× 15 = × 10 + metade", 110, 590, 150, "g", BR)
    E.escreve(c, "130 × 15 = 1.300 + 650", 110, 800, 110, "g", AMARELO)
    E.escreve(c, "= 1.950", 110, 950, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quantos_galoes", a), ("capa_B_area_e_perimetro", b), ("capa_C_vezes_quinze", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
