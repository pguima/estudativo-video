"""Capas do MAT-FAT-015 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 101 × 99 de cabeça
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "101 × 99 =", 84, 440, 220, cor=BR)
    E.formula(c, "9.999", 84, 760, 260, cor=AMARELO)
    E.escreve(c, "de cabeça, em segundos", 84, 960, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Soma vezes", "diferença", "e o cubo da soma")


def d(c):  # o atalho: 52 × 48 pela distância ao 50
    palco(c)
    E.escreve(c, "o atalho", 84, 330, 150, "i", BR)
    E.formula(c, "52 × 48 = 2.496", 84, 600, 190, cor=AMARELO)
    E.formula(c, "50^2 − 2^2 = 2.500 − 4", 84, 850, 130, cor=BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_101_vezes_99", a), ("capa_B_soma_vezes_diferenca", b), ("capa_C_52_vezes_48", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
