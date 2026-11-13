"""Capas da QUI-LIG-012 (1280x720). Uso: python capa.py"""
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

def a(c):  # o gancho: 4 questões
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.bola(c, 1460, 560, 300, BR)
    E.centro(c, "4", 1460, 700, 420, "g", COR)
    E.escreve(c, "polaridade", 84, 450, 150, "g", BR)
    E.escreve(c, "e forças", 84, 620, 150, "g", AMARELO)
    E.escreve(c, "em 4 questões", 84, 800, 110, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Praticando", "forças", "4 questões")


def d(c):  # o macete: fórmula igual, procure O–H
    palco_capa(c)
    Q.formula(c, "C2H6O", 84, 380, 160, BR, escuro=True)
    E.escreve(c, "= mesma fórmula", 700, 370, 90, "i", CLARO)
    E.escreve(c, "procure", 84, 620, 130, "i", BR)
    E.formula(c, "O–H", 620, 640, 200, "g", CLARO)
    E.escreve(c, "ferve mais alto", 84, 900, 140, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quatro_questoes", a), ("capa_B_praticando_forcas", b), ("capa_C_procure_o_oh", d)):
    c = s.getCanvas()
    c.clear(skia.ColorWHITE)
    fn(c)
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
