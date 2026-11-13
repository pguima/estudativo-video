"""Capas da QUI-CAL-010 (1280x720). Uso: python capa.py"""
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
def a(c):  # o gancho: o balão murcha no congelador
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "no congelador,", 84, 360, 120, "i", BR)
    E.escreve(c, "o balão murcha", 84, 580, 170, "g", BR)
    E.escreve(c, "e nenhum ar saiu", 84, 780, 130, "g", AMARELO)
    E.escreve(c, "por quê?", 84, 990, 100, "i", BR)
    c.drawOval(skia.Rect.MakeXYWH(1420, 300, 330, 380), M.paint(BR, 0.25))
    c.drawOval(skia.Rect.MakeXYWH(1420, 300, 330, 380), M.paint(BR, 1.0, stroke=10))


def b(c):
    E.capa_modelo(c, "Química", "Gases e", "kelvin", "do zero")


def d(c):  # o macete: some 273
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "Celsius para kelvin", 84, 330, 110, "i", BR)
    E.escreve(c, "+ 273", 84, 600, 260, "g", claro)
    E.escreve(c, "27 °C = 300 K", 84, 820, 130, "g", BR)
    E.escreve(c, "e 760 mmHg = 1 atm", 84, 990, 90, "i", BR)


CAPAS = (("capa_A_balao_no_congelador", a), ("capa_B_gases_kelvin", b), ("capa_C_mais_273", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
