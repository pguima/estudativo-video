"""Capas do MAT-MED-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 1 m² não são 100 cm²
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "1 m² =", 84, 420, 190, "g", BR)
    E.escreve(c, "100 cm²", 760, 420, 170, "g", BR)
    E.risco(c, 740, 460, 1420, 290, 9, 0, AMARELO, 30)
    E.escreve(c, "10.000 cm²", 760, 680, 170, "g", AMARELO)
    E.escreve(c, "errou feio?", 84, 960, 120, "i", BR)
    x, y, L = 1500, 760, 300  # o metro quadrado com a grade
    c.drawRect(skia.Rect.MakeXYWH(x, y, L, L), M.paint(AMARELO, 0.9))
    for k in range(1, 20):
        c.drawLine(x + k * L / 20, y, x + k * L / 20, y + L, M.paint(COR, 0.6, stroke=2))
        c.drawLine(x, y + k * L / 20, x + L, y + k * L / 20, M.paint(COR, 0.6, stroke=2))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Converter", "área", "e hectare")


def d(c):  # o atalho: eleve o fator ao quadrado
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "eleve o fator", 84, 340, 130, "i", BR)
    E.escreve(c, "ao quadrado", 84, 540, 200, "g", BR)
    E.formula(c, "100^2 = 10.000", 84, 820, 170, "g", AMARELO)
    E.escreve(c, "de m para cm, na área", 84, 980, 90, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_errou_feio", a), ("capa_B_converter_area", b), ("capa_C_ao_quadrado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
