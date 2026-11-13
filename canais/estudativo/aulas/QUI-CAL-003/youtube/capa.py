"""Capas da QUI-CAL-003 (1280x720). Uso: python capa.py"""
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
def a(c):  # o gancho: o adubo tem 35% de nitrogênio
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "no adubo", 84, 330, 110, "i", BR)
    Q.formula(c, "NH4NO3", 84, 570, 210, BR, cores={"N": AMARELO})
    E.escreve(c, "35% é", 84, 800, 170, "g", BR)
    E.escreve(c, "nitrogênio", 84, 980, 150, "g", AMARELO)
    E.pizza(c, 99, 0, [("N", 35), ("H", 5), ("O", 60)], 1500, 560, 260, cores=[AMARELO, E.mix(COR, BR, 0.5), E.mix(COR, BR, 0.75)], rotulos=False, destaque=(0,))


def b(c):
    E.capa_modelo(c, "Química", "Fórmula", "mínima", "e porcentagem")


def d(c):  # o macete: a base de 100 g
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete dos", 84, 340, 120, "i", BR)
    E.escreve(c, "100 gramas", 76, 540, 190, "g", BR)
    E.escreve(c, "40% → 40 g", 84, 780, 150, "g", claro)
    Q.formula(c, "CH2O", 84, 1000, 150, BR, escuro=True)


CAPAS = (("capa_A_35_por_cento", a), ("capa_B_formula_minima", b), ("capa_C_base_100_gramas", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
