"""Capas do MAT-NUM-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a conta em que todo mundo chuta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "7 × 8", 84, 640, 440, "g", AMARELO)
    E.escreve(c, "chutou?", 1170, 600, 190, "i", BR)
    E.escreve(c, "dobre 3 vezes", 84, 900, 200, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Tabuada", "macetes", "3, 4, 6, 7 e 8")


def d(c):  # o atalho do seis
    palco(c)
    E.escreve(c, "o atalho", 84, 370, 170, "i", BR)
    E.escreve(c, "do 6", 620, 370, 190, "g", AMARELO)
    E.escreve(c, "6 × 8 =", 84, 680, 280, "g", BR)
    E.escreve(c, "48", 1120, 680, 330, "g", AMARELO)
    E.escreve(c, "metade do 8, depois o 8", 84, 900, 130, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_7_vezes_8", a), ("capa_B_tabuada_3_4_6_7_8", b), ("capa_C_atalho_do_6", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
