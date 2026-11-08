"""Capas do MAT-POT-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: uma raiz que parece de calculadora
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "r{1.764}", 84, 560, 300, cor=BR)
    E.escreve(c, "= ?", 1090, 545, 300, "g", AMARELO)
    E.escreve(c, "sem calculadora", 84, 920, 190, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Raiz", "quadrada", "exata e aproximada")


def d(c):  # o atalho: cerque com dezenas e olhe o final
    palco(c)
    E.escreve(c, "cerque e olhe o final", 84, 340, 170, "i", BR)
    E.formula(c, "r{1.764}", 84, 660, 240, cor=BR)
    E.escreve(c, "= 42", 900, 650, 240, "g", AMARELO)
    E.escreve(c, "o atalho", 84, 930, 170, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sem_calculadora", a), ("capa_B_raiz_quadrada", b), ("capa_C_atalho", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
