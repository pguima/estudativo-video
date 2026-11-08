"""Capas do MAT-ARE-010 (1280x720). Uso: python capa.py"""
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
VERDE = "#7BE0A8"


def a(c):  # o gancho: lado +20%, área +44%
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    x, yb, L, d = 150, 960, 500, 100
    c.drawRect(skia.Rect.MakeXYWH(x, yb - L, L, L), M.paint(LILAS, 0.35))
    for R in ((x + L, yb - L, d, L), (x, yb - L - d, L, d)):
        c.drawRect(skia.Rect.MakeXYWH(*R), M.paint(VERDE, 0.85))
    c.drawRect(skia.Rect.MakeXYWH(x + L, yb - L - d, d, d), M.paint(AMARELO))
    c.drawRect(skia.Rect.MakeXYWH(x, yb - L - d, L + d, L + d), M.paint(BR, 1, stroke=10))
    E.escreve(c, "lado +20%", 900, 420, 120, "g", BR)
    E.escreve(c, "área +44%", 900, 640, 170, "g", AMARELO)
    E.escreve(c, "por quê?", 900, 830, 120, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Ampliou?", "Área × k²", "figuras semelhantes")


def d(c):  # o atalho: 20 + 20 + 4
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho da área", 110, 380, 120, "i", BR)
    E.formula(c, "20 + 20 + f{20 · 20}{100}", 110, 640, 150, "g", BR)
    E.escreve(c, "= 44%", 110, 930, 190, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_lado_20_area_44", a), ("capa_B_area_vezes_k2", b), ("capa_C_atalho_20_20_4", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
