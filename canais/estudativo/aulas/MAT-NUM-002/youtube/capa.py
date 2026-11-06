"""Capas do MAT-NUM-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o número que trava
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "2.048.500", 72, 560, 330, "g", AMARELO)
    E.escreve(c, "você lê", 84, 760, 170, "i", BR)
    E.escreve(c, "de primeira?", 84, 940, 180, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Números", "grandes", "ler e comparar")


def d(c):  # o atalho: conte os pontos
    palco(c)
    E.escreve(c, "conte os", 84, 370, 170, "i", BR)
    E.escreve(c, "pontos", 590, 370, 190, "g", AMARELO)
    E.escreve(c, "1.000.010", 84, 610, 230, "g", BR)
    E.escreve(c, ">", 1250, 610, 230, "g", AMARELO)
    E.escreve(c, "990.000", 84, 860, 230, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_voce_le_de_primeira", a), ("capa_B_numeros_grandes", b), ("capa_C_conte_os_pontos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
