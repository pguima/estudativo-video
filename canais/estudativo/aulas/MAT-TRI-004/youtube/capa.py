"""Capas do MAT-TRI-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a altura da torre sem subir
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    O, B = (1080, 960), (1440, 960)
    T = (1440, 960 - 360 * math.sqrt(3))
    M.line(c, 980, 960, 1700, 960, BR, 0.8, 6)
    c.drawRect(skia.Rect.MakeLTRB(B[0], T[1], B[0] + 60, B[1]), M.paint(BR, 0.25))
    c.drawRect(skia.Rect.MakeLTRB(B[0], T[1], B[0] + 60, B[1]), M.paint(BR, 1.0, stroke=5))
    M.line(c, *O, *T, BR, 0.9, 6, dash=[18, 14])
    M.line(c, *B, *T, AMARELO, 1.0, 14)
    c.drawArc(skia.Rect.MakeXYWH(O[0] - 120, O[1] - 120, 240, 240), -60, 60, False, M.paint(BR, 1.0, stroke=7))
    E.escreve(c, "60°", O[0] + 140, O[1] - 40, 70, "g", BR)
    E.escreve(c, "30 m", 1180, 1050, 70, "g", BR)
    E.escreve(c, "?", B[0] + 90, 640, 160, "g", AMARELO)
    E.escreve(c, "a altura", 84, 400, 150, "i", BR)
    E.escreve(c, "sem subir", 84, 590, 190, "g", BR)
    E.formula(c, "h = 30r{3} ≈ 52 m", 84, 860, 110, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Altura e", "rampa", "com seno e tangente")


def d(c):  # o atalho: metade do equilátero
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 360, 140, "i", BR)
    E.escreve(c, "30° e 60°", 84, 580, 200, "g", BR)
    E.formula(c, "1 : r{3} : 2", 84, 840, 150, "g", E.mix(COR, BR, 0.55))
    A, B = (1330, 960), (1580, 960)
    T = (1580, 960 - 250 * math.sqrt(3))
    path = skia.Path(); path.addPoly([A, B, T], True)
    c.drawPath(path, M.paint(COR, 0.35))
    M.line(c, *A, *B, "#D98A00", 1.0, 12); M.line(c, *B, *T, "#3CC7D3", 1.0, 12); M.line(c, *A, *T, BR, 1.0, 12)
    E.escreve(c, "1", 1440, 1050, 70, "g", BR)
    E.formula(c, "r{3}", 1610, 760, 70, "g", BR)
    E.escreve(c, "2", 1380, 720, 70, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_altura_sem_subir", a), ("capa_B_altura_e_rampa", b), ("capa_C_atalho_30_60", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
