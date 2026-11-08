"""Capas do MAT-TOP-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: abrir sem multiplicar parênteses
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "(x + 2)^4", 84, 470, 260, "g", BR)
    E.escreve(c, "sem multiplicar", 1150, 330, 90, "i", BR)
    E.escreve(c, "parênteses", 1150, 430, 90, "i", BR)
    E.pilula(c, "1   4   6   4   1", 1460, 560, 80, "g", fundo=AMARELO, cor=COR)
    E.formula(c, "x^4 + 8x^3 + 24x^2 + 32x + 16", 84, 900, 130, "g", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Binômio", "de Newton", "sem decorar")


def d(c):  # o atalho: troque x por 1
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "confira em 1 segundo:", 84, 360, 120, "i", BR)
    E.escreve(c, "troque x por 1", 76, 570, 180, "g", BR)
    E.formula(c, "(1 + 2)^4 = ", 90, 860, 150, "g", BR)
    E.escreve(c, "81", 760, 870, 190, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sem_multiplicar", a), ("capa_B_binomio_de_newton", b), ("capa_C_troque_x_por_1", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
