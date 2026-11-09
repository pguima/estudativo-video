"""Capas do FIS-EGF-013 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a estação espacial cai o tempo todo
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a estação espacial", 84, 380, 100, "i", BR)
    E.escreve(c, "está caindo", 84, 570, 180, "g", BR)
    E.escreve(c, "o tempo todo", 84, 760, 150, "g", AMARELO)
    E.bola(c, 1680, 1450, 700, "#2F6FB0")
    pt = M.paint(BR, 0.8, stroke=6); pt.setPathEffect(skia.DashPathEffect.Make([22, 16], 0))
    c.drawCircle(1680, 1450, 860, pt)
    x, y = 1680 - 860 * math.sin(0.3), 1450 - 860 * math.cos(0.3)
    M.rrect(c, x - 70, y - 22, 140, 44, 8, "#2F5DA8")
    M.rrect(c, x - 22, y - 30, 44, 60, 8, "#D9D9DE")
    F.seta(c, x + 40, y + 60, x + 120, y + 230, AMARELO, 1.0, 16)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Satélites", "e marés", "do zero")


def d(c):  # o macete: v = √(g·R)
    palco_capa(c)
    E.escreve(c, "a velocidade de um satélite", 84, 330, 90, "i", BR)
    E.escreve(c, "numa raiz", 84, 490, 130, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "v = r{g · R}", 84, 760, 170, "g", AMARELO)
    E.formula(c, "= 8 km/s", 84, 960, 130, "g", claro)
    E.bola(c, 1600, 700, 170, "#2F6FB0")


CAPAS = (("capa_A_esta_caindo", a), ("capa_B_satelites_e_mares", b), ("capa_C_numa_raiz", d))

pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
