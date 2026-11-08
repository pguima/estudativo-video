"""Capas do MAT-ARE-011 (1280x720). Uso: python capa.py"""
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
LILAS = "#C9C9FF"


def tri(c, pts, cor, a):
    path = skia.Path(); path.addPoly(pts, True)
    c.drawPath(path, M.paint(cor, a))
    p = M.paint(BR, 1, stroke=10); p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, p)


def a(c):  # o gancho: dois pedaços diferentes, a mesma área
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    q = lambda x, y: (110 + x * 80, 960 - y * 80)
    A, B, Cc, Mm = q(10, 7), q(0, 0), q(8, 0), q(4, 0)
    tri(c, [A, B, Mm], LILAS, 0.55)
    tri(c, [A, Mm, Cc], AMARELO, 0.85)
    E.escreve(c, "mesma", 1020, 460, 190, "g", AMARELO)
    E.escreve(c, "área?", 1020, 660, 190, "g", BR)
    E.escreve(c, "a mediana explica", 1020, 830, 80, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Mesma", "altura", "a razão das bases")


def d(c):  # o atalho: compare só as bases
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    A, B, D, Cc = (1300, 360), (1080, 900), (1400, 900), (1880, 900)
    tri(c, [A, B, D], LILAS, 0.6)
    tri(c, [A, D, Cc], AMARELO, 0.8)
    E.escreve(c, "2", 1220, 1010, 100, "g", BR); E.escreve(c, "3", 1620, 1010, 100, "g", AMARELO)
    E.escreve(c, "nem procure", 110, 380, 110, "i", BR)
    E.escreve(c, "a altura", 110, 560, 150, "g", BR)
    E.escreve(c, "compare", 110, 760, 140, "g", AMARELO)
    E.escreve(c, "só as bases", 110, 920, 120, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mesma_area", a), ("capa_B_mesma_altura", b), ("capa_C_compare_as_bases", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
