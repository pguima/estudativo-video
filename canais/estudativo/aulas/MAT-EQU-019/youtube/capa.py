"""Capas do MAT-EQU-019 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: some as equações e o y desaparece
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    x, s = 260, 170
    E.formula(c, "3x + 2y = 16", x, 380, s, cor=BR)
    E.formula(c, "5x − 2y = 16", x, 600, s, cor=BR)
    E.escreve(c, "+", 110, 600, s, "g", AMARELO)
    w = E.formula(c, "3x + ", 0, 0, s, a=0)
    w2 = E.formula(c, "2y", 0, 0, s, a=0)
    for y in (380, 600):
        M.line(c, x + w + 5, y - 30, x + w + w2 + 25, y - 110, AMARELO, 1, 22)
    M.line(c, 90, 660, 1360, 660, BR, 1, 10)
    E.formula(c, "8x = 32", x, 870, s, cor=AMARELO)
    E.escreve(c, "o y sumiu", 1380, 860, 120, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Sistemas", "pela adição", "sem errar")


def d(c):  # o atalho: x + y sem achar x e y
    palco(c)
    E.escreve(c, "o atalho", 84, 360, 150, "i", BR)
    E.formula(c, "x + y = 5", 84, 640, 260, cor=AMARELO)
    E.escreve(c, "sem achar x e y", 84, 900, 160, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_y_sumiu", a), ("capa_B_sistemas_adicao", b), ("capa_C_atalho_x_mais_y", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
