"""Capas do MAT-TOP-014 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 1011 não é mil e onze
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "1011", 84, 560, 330, "g", BR)
    E.escreve(c, "= 11", 820, 560, 260, "g", AMARELO)
    E.escreve(c, "não é mil e onze", 84, 800, 120, "i", BR)
    E.escreve(c, "na base 2", 84, 960, 110, "g", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Base 2", "e base 60", "sem mistério")


def d(c):  # o macete: a maior casa que cabe
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "13 sem dividir:", 84, 340, 130, "i", BR)
    x, w = 130, 300
    for i, (v, d_) in enumerate(((8, "1"), (4, "1"), (2, "0"), (1, "1"))):
        cx = x + (i + 0.5) * w
        M.rrect(c, cx - 120, 420, 240, 130, 26, E.CLARO, 0.25)
        E.centro(c, str(v), cx, 520, 100, "g", BR)
        E.centro(c, d_, cx, 800, 260, "g", "#3CC7D3" if d_ == "1" else "#77778A")
    E.escreve(c, "a maior casa que cabe", 84, 990, 100, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_1011_vale_11", a), ("capa_B_base_2_e_60", b), ("capa_C_maior_casa", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
