"""Capas da QUI-CAL-012 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import quimica as Q
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
def a(c):  # o gancho: quantos gramas no tanque?
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "41 L · 6 atm · 27 °C", 84, 360, 110, "g", BR)
    E.escreve(c, "quantos gramas", 84, 580, 160, "g", AMARELO)
    E.escreve(c, "de oxigênio?", 84, 760, 160, "g", AMARELO)
    E.escreve(c, "sem abrir o tanque", 84, 980, 90, "i", BR)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1460, 300, 240, 560), 120, 120)
    c.drawRRect(r, M.paint(BR, 0.25)); c.drawRRect(r, M.paint(BR, 1.0, stroke=10))
    M.rrect(c, 1550, 240, 60, 64, 10, BR, 1.0)


def b(c):
    E.capa_modelo(c, "Química", "PV = nRT", "Clapeyron", "do zero")


def d(c):  # o macete: o 24,6
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a 27 °C, guarde:", 84, 330, 110, "i", BR)
    E.escreve(c, "RT = 24,6", 84, 600, 220, "g", claro)
    E.escreve(c, "n = PV ÷ 24,6", 84, 820, 130, "g", BR)
    E.escreve(c, "mols de gás de cabeça", 84, 990, 90, "i", BR)


CAPAS = (("capa_A_quantos_gramas", a), ("capa_B_clapeyron", b), ("capa_C_24_6", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
