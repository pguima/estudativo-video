"""Capas do MAT-NUM-001 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: quanto vale o 3?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3", 90, 680, 620, "g", AMARELO)
    E.escreve(c, "52", 520, 680, 620, "g", BR)
    E.escreve(c, "quanto vale o 3?", 84, 930, 176, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Valor", "posicional", "do zero")


def d(c):  # o atalho: conte as casas à direita
    palco(c)
    E.escreve(c, "conte as casas", 84, 370, 170, "g", BR)
    E.escreve(c, "à direita", 84, 540, 170, "i", BR)
    E.escreve(c, "352", 84, 880, 260, "g", BR)
    E.escreve(c, "3", 84, 880, 260, "g", AMARELO)
    M.arrow(c, 660, 790, 960, 790, BR, 1, 12, 44, 1)
    E.escreve(c, "300", 1030, 880, 260, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quanto_vale_o_3", a), ("capa_B_valor_posicional", b), ("capa_C_conte_as_casas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
