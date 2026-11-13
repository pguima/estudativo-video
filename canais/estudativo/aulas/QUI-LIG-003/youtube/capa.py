"""Capas da QUI-LIG-003 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


CLARO = E.mix(COR, BR, 0.5)

def metal(c, x, y, cols, rows, p, r, el="Cu"):
    for i in range(rows):
        for j in range(cols):
            Q.atomo(c, x + j * p, y + i * p, r, el, rotulo=False)
            E.centro(c, "+", x + j * p, y + i * p + r * 0.36, r, "g", BR)
    for k in range(int(cols * rows * 0.9)):
        u, v = (math.sin(k * 12.9898) * 43758.5) % 1, (math.sin(k * 78.233) * 43758.5) % 1
        E.bola(c, x - p / 2 + u * cols * p, y - p / 2 + v * rows * p, 11, Q.ELETRON)


def a(c):  # o gancho: dobra e conduz
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "dobra", 84, 430, 170, "g", BR)
    E.escreve(c, "e conduz.", 84, 610, 170, "g", AMARELO)
    E.escreve(c, "por quê?", 84, 800, 130, "i", BR)
    metal(c, 1180, 300, 5, 5, 130, 44)


def b(c):
    E.capa_modelo(c, "Química", "Ligação", "metálica", "e ligas")


def d(c):  # o macete: do que são feitas as ligas
    palco_capa(c)
    E.escreve(c, "bronze", 84, 400, 160, "g", BR)
    Q.formula(c, "Cu + Sn", 900, 400, 150, CLARO, escuro=True)
    E.escreve(c, "aço", 84, 680, 160, "g", BR)
    Q.formula(c, "Fe + C", 900, 680, 150, CLARO, escuro=True)
    E.escreve(c, "liga é mistura, não elemento novo", 84, 930, 80, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dobra_e_conduz", a), ("capa_B_ligacao_metalica", b), ("capa_C_bronze_e_aco", d)):
    c = s.getCanvas()
    c.clear(skia.ColorWHITE)
    fn(c)
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
