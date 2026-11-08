"""Capas do MAT-TRA-002 (1280x720). Uso: python capa.py"""
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


def lal(c, x0, y0, base, lat, g, cor_x, txt_b, txt_l, txt_x, tinta=BR):
    """triângulo com dois lados conhecidos (base e lateral) e o ângulo g entre eles"""
    A, B = (x0, y0), (x0 + base, y0)
    Cc = (x0 + lat * math.cos(math.radians(g)), y0 - lat * math.sin(math.radians(g)))
    path = skia.Path(); path.addPoly([A, B, Cc], True)
    c.drawPath(path, M.paint(tinta, 0.12))
    M.line(c, *A, *B, tinta, 1.0, 10)
    M.line(c, *A, *Cc, tinta, 1.0, 10)
    M.line(c, *B, *Cc, cor_x, 1.0, 14)
    c.drawArc(skia.Rect.MakeXYWH(x0 - 70, y0 - 70, 140, 140), -g, g, False, M.paint(cor_x, 1.0, stroke=8))
    E.escreve(c, f"{g}°", x0 + 30, y0 - 90, 70, "g", cor_x)
    E.escreve(c, txt_b, (A[0] + B[0]) / 2 - 20, y0 + 100, 90, "g", tinta)
    E.escreve(c, txt_l, (A[0] + Cc[0]) / 2 - 100, (A[1] + Cc[1]) / 2, 90, "g", tinta)
    E.escreve(c, txt_x, (B[0] + Cc[0]) / 2 + 10, (B[1] + Cc[1]) / 2 - 40, 110, "g", cor_x)


def a(c):  # o gancho: lados 3 e 5, 120°, quanto mede?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o terceiro", 84, 400, 150, "g", BR)
    E.escreve(c, "lado", 84, 570, 150, "g", AMARELO)
    E.escreve(c, "sem ângulo reto", 84, 740, 110, "i", BR)
    lal(c, 1240, 860, 5 * 110, 3 * 110, 120, AMARELO, "5", "3", "?")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Lei dos", "cossenos", "Pitágoras + ajuste")


def d(c):  # o atalho: 60° e 120°
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 130, "i", BR)
    E.escreve(c, "60°", 84, 560, 150, "g", AMARELO)
    E.formula(c, "a^2 = b^2 + c^2 − bc", 420, 560, 130, "g", BR)
    E.escreve(c, "120°", 84, 820, 150, "g", AMARELO)
    E.formula(c, "a^2 = b^2 + c^2 + bc", 500, 820, 130, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_terceiro_lado", a), ("capa_B_lei_dos_cossenos", b), ("capa_C_atalho_60_120", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
