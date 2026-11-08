"""Capas do MAT-ESP-020 (1280x720). Uso: python capa.py"""
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
SEN = math.sin(math.radians(22))


def taca(c, cx, ty, r, h, f):
    """a taça de ponta para baixo em traço branco, com o suco amarelo até a fração f da altura"""
    ay = ty + h
    yl, rl = ay - f * h, r * f
    suco = skia.Path(); suco.moveTo(cx - rl, yl); suco.lineTo(cx, ay); suco.lineTo(cx + rl, yl); suco.close()
    c.drawPath(suco, M.paint(AMARELO, 0.95))
    c.drawOval(skia.Rect.MakeXYWH(cx - rl, yl - rl * SEN, 2 * rl, 2 * rl * SEN), M.paint("#FFE866", 1))
    c.drawOval(skia.Rect.MakeXYWH(cx - r, ty - r * SEN, 2 * r, 2 * r * SEN), M.paint(BR, 1, stroke=8))
    M.line(c, cx - r, ty, cx, ay, BR, 1, 8); M.line(c, cx + r, ty, cx, ay, BR, 1, 8)
    M.line(c, cx, ay, cx, ay + 0.22 * h, BR, 1, 10)
    c.drawOval(skia.Rect.MakeXYWH(cx - 0.45 * r, ay + 0.22 * h - 0.45 * r * SEN, 0.9 * r, 0.9 * r * SEN), M.paint(BR, 1, stroke=8))


def a(c):  # o gancho: metade da altura, só 1/8
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    taca(c, 470, 300, 300, 560, 0.5)
    E.escreve(c, "suco até a", 1000, 330, 100, "i", BR)
    E.escreve(c, "metade?", 1000, 480, 150, "g", BR)
    E.escreve(c, "só", 1000, 760, 120, "i", BR)
    E.formula(c, "f{1}{8}", 1180, 800, 220, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Dobrou?", "Volume × 8", "sólidos semelhantes")


def d(c):  # o atalho: os cubos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "decore os", 84, 340, 120, "i", BR)
    E.escreve(c, "cubos", 84, 560, 230, "g", BR)
    for i, n in enumerate((1, 8, 27, 64, 125)):
        E.escreve(c, str(n), 84 + i * 340, 900, 170, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_so_um_oitavo", a), ("capa_B_volume_vezes_oito", b), ("capa_C_decore_os_cubos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
