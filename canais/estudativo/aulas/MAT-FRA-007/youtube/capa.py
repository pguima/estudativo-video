"""Capas do MAT-FRA-007 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
CLARO = E.mix(COR, BR, 0.5)


def a(c):  # o gancho: 2/7 + 3/7 não é 5/14
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.fracao(c, 2, 7, 280, 560, 290, BR)
    E.mais(c, 610, 545, 110, "#FFFFFF", sombra=False)
    E.fracao(c, 3, 7, 940, 560, 290, BR)
    E.escreve(c, "=", 1130, 640, 240, "g", BR)
    E.fracao(c, 5, 14, 1540, 560, 290, BR)
    E.risco(c, 1320, 860, 1770, 220, 9, 0, "#FFD500", 34)
    E.escreve(c, "somou os de baixo?", 84, 1010, 120, "i", BR)


def b(c):  # o método
    E.capa_modelo(c, "Matemática", "Somar", "frações", "denominador igual")


def d(c):  # o atalho: tampe o denominador
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 350, 150, "i", BR)
    E.escreve(c, "do dedo", 76, 570, 240, "g", BR)
    y, s = 790, 170
    E.fracao(c, 2, 7, 290, y, s, BR); E.fracao(c, 3, 7, 750, y, s, BR)
    E.escreve(c, "+", 480, y + 50, 150, "g", BR)
    E.escreve(c, "=", 950, y + 50, 150, "g", BR)
    E.fracao(c, 5, 7, 1240, y, s, CLARO)
    pele = E.mix(CLARO, BR, 0.45)
    for x in (290, 750):  # o dedo tampa o de baixo
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 85, y + 14, 170, 400), 78, 78), M.paint(pele))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 58, y + 31, 116, 128), 48, 48), M.paint(BR, 0.85))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_erro", a), ("capa_B_denominador_igual", b), ("capa_C_atalho_do_dedo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
