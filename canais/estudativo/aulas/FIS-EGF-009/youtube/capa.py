"""Capas do FIS-EGF-009 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o gelo que afunda
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o gelo", 84, 400, 190, "g", BR)
    E.escreve(c, "que afunda", 84, 590, 160, "g", AMARELO)
    E.escreve(c, "5 situações de hidrostática", 84, 780, 76, "i", BR)
    p = skia.Path(); p.moveTo(1300, 250); p.lineTo(1300, 1000); p.lineTo(1760, 1000); p.lineTo(1760, 250)
    c.drawRect(skia.Rect.MakeLTRB(1300, 420, 1760, 1000), M.paint("#E9B44C", 0.9))
    c.drawPath(p, M.paint(BR, 1.0, stroke=10))
    M.rrect(c, 1450, 820, 160, 160, 22, "#EAF6FF")
    F.seta(c, 1530, 520, 1530, 760, "#1B1B20", 1.0, 16)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Praticando", "fluidos", "hidrostática")


def d(c):  # o macete: peso no ar ÷ o que sumiu = densidade
    palco_capa(c)
    E.escreve(c, "a densidade pela balança:", 84, 330, 90, "i", BR)
    E.escreve(c, "peso no ar ÷ o que sumiu", 84, 490, 104, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "50 ÷ 20 = 2,5 g/cm^3", 84, 760, 130, "g", AMARELO)
    E.formula(c, "sem calcular volume", 84, 940, 90, "g", claro)


CAPAS = (("capa_A_o_gelo_que_afunda", a), ("capa_B_praticando_hidrostatica", b), ("capa_C_densidade_pela_balanca", d))

pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
