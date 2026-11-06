"""Capas do MAT-NUM-005 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a conta que trava
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "9 × 7", 84, 640, 440, "g", AMARELO)
    E.escreve(c, "travou?", 1170, 600, 190, "i", BR)
    E.escreve(c, "sem decorar", 84, 900, 200, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Tabuada", "macetes", "2, 5, 9 e 10")


def d(c):  # o atalho do nove
    palco(c)
    E.escreve(c, "o atalho", 84, 370, 170, "i", BR)
    E.escreve(c, "do 9", 620, 370, 190, "g", AMARELO)
    E.escreve(c, "9 × 7 =", 84, 680, 280, "g", BR)
    E.escreve(c, "63", 1120, 680, 330, "g", AMARELO)
    E.escreve(c, "em dois passos", 84, 900, 150, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_9_vezes_7", a), ("capa_B_tabuada_2_5_9_10", b), ("capa_C_atalho_do_9", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
