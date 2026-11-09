"""Capas do FIS-EGF-012 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 15.600 N numa asa
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "quanto a asa", 84, 380, 120, "i", BR)
    E.escreve(c, "levanta?", 84, 580, 190, "g", BR)
    E.escreve(c, "5 situações de fluidos", 84, 760, 80, "i", AMARELO)
    c.save(); c.translate(1480, 720); c.rotate(-6)
    p = skia.Path(); s = 330
    p.moveTo(-s, 0); p.cubicTo(-s * 0.7, -s * 0.32, s * 0.3, -s * 0.3, s, 0)
    p.cubicTo(s * 0.3, s * 0.06, -s * 0.7, s * 0.12, -s, 0); p.close()
    c.drawPath(p, M.paint("#1B1B20"))
    c.restore()
    F.seta(c, 1480, 640, 1480, 300, AMARELO, 1.0, 18)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Vazão e", "Bernoulli", "praticando")


def d(c):  # o macete: diferença de quadrados
    palco_capa(c)
    E.escreve(c, "um atalho de conta:", 84, 330, 100, "i", BR)
    E.escreve(c, "não eleve ao quadrado", 84, 490, 110, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "70^2 − 60^2 = 130 · 10", 84, 760, 130, "g", AMARELO)
    E.formula(c, "= 1.300", 84, 950, 100, "g", claro)


CAPAS = (("capa_A_quanto_a_asa_levanta", a), ("capa_B_praticando_vazao_bernoulli", b), ("capa_C_nao_eleve_ao_quadrado", d))

pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
