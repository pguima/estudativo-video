"""Capas do MAT-MED-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 2 GB em bytes, nove zeros numa linha curta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "2 GB =", 84, 400, 180, "g", BR)
    E.escreve(c, "2.000.000.000", 84, 620, 150, "g", BR)
    E.formula(c, "= 2 × 10^9", 84, 870, 190, "g", AMARELO)
    E.escreve(c, "bytes", 900, 870, 130, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Giga, nano", "e polegada", "sem decorar")


def d(c):  # o atalho: de 3 em 3 no expoente
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o expoente anda", 84, 340, 120, "i", BR)
    E.escreve(c, "de 3 em 3", 84, 540, 200, "g", BR)
    for x, pre, pot in ((260, "quilo", "10^3"), (860, "mega", "10^6"), (1460, "giga", "10^9")):
        E.centro(c, pre, x, 760, 90, "g", AMARELO)
        E.formula(c, pot, x, 930, 140, "g", BR, 1.0, "center")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nove_zeros", a), ("capa_B_giga_nano_polegada", b), ("capa_C_tres_em_tres", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
