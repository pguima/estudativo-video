"""Capas do FIS-EGF-011 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: o telhado que voa
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "por que o vento", 84, 380, 110, "i", BR)
    E.escreve(c, "arranca o", 84, 570, 170, "g", BR)
    E.escreve(c, "telhado?", 84, 760, 170, "g", AMARELO)
    M.rrect(c, 1250, 700, 520, 300, 0, "#EDE3D6")
    p = skia.Path(); p.moveTo(1200, 640); p.lineTo(1510, 440); p.lineTo(1820, 640); p.close()
    c.save(); c.rotate(-4); c.drawPath(p, M.paint("#1B1B20")); c.restore()
    for y in (300, 360, 420):
        F.seta(c, 1150, y - 100, 1450, y - 100, BR, 1.0, 10)
    F.seta(c, 1510, 900, 1510, 660, AMARELO, 1.0, 16)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Bernoulli", "do zero", "velocidade e pressão")


def d(c):  # o macete: furo no tanque
    palco_capa(c)
    E.escreve(c, "tanque furado?", 84, 330, 110, "i", BR)
    E.escreve(c, "nem monte Bernoulli", 84, 490, 120, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "v = r{2 · g · h}", 84, 760, 160, "g", AMARELO)
    E.formula(c, "v^2 = 20 · h", 84, 950, 100, "g", claro)


CAPAS = (("capa_A_o_telhado_voa", a), ("capa_B_principio_de_bernoulli", b), ("capa_C_tanque_furado", d))

pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
