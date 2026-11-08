"""Capas do MAT-FAT-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o caminho de volta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "6x^2 + 9x", 84, 420, 200, cor=BR)
    E.escreve(c, "o caminho de volta", 84, 600, 100, "i", BR)
    E.formula(c, "= 3x(2x + 3)", 84, 880, 200, cor=AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Fator", "comum", "e agrupamento")


def d(c):  # o atalho: tire o menos junto
    palco(c)
    E.escreve(c, "o atalho do menos", 84, 330, 130, "i", BR)
    E.formula(c, "x(x + 5) − 2(x + 5)", 84, 590, 150, cor=BR)
    E.formula(c, "= (x + 5)(x − 2)", 84, 850, 170, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_caminho_de_volta", a), ("capa_B_fator_comum", b), ("capa_C_atalho_do_menos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
