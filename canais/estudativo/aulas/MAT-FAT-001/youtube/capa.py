"""Capas do MAT-FAT-001 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: (x + 3)² não é x² + 9
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "(x + 3)^2 =", 84, 430, 210, cor=BR)
    w = E.formula(c, "x^2 + 9", 84, 700, 190, cor=BR)
    E.risco(c, 64, 720, 84 + w + 20, 560, 9, 0, BR, 22)
    E.formula(c, "x^2 + 6x + 9", 84, 960, 220, cor=AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Quadrado", "da soma", "e da diferença")


def d(c):  # o atalho: 101² de cabeça
    palco(c)
    E.escreve(c, "de cabeça", 84, 330, 150, "i", BR)
    E.formula(c, "101^2 = 10.201", 84, 600, 200, cor=AMARELO)
    E.escreve(c, "10.000 + 200 + 1", 84, 830, 110, "g", BR)
    E.escreve(c, "sem conta armada", 84, 1000, 90, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_pedaco_que_falta", a), ("capa_B_quadrado_da_soma", b), ("capa_C_101_ao_quadrado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
