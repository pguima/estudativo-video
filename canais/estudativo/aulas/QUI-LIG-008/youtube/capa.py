"""Capas da QUI-LIG-008 (1280x720). Uso: python capa.py"""
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

def copo(c, cx, yb, w, h, camadas):
    y = yb
    for hh, cor in camadas:
        c.drawRect(skia.Rect.MakeLTRB(cx - w / 2 + 6, y - hh, cx + w / 2 - 6, y - 6), M.paint(cor))
        y -= hh
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, yb - h, w, h), 20, 20), M.paint(BR, 1, stroke=8))


def a(c):  # o gancho: óleo e água não se misturam
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    copo(c, 1450, 960, 420, 640, [(330, "#BFE3F2"), (220, "#F2C14E")])
    E.escreve(c, "por que óleo", 84, 450, 140, "g", BR)
    E.escreve(c, "e água não", 84, 610, 140, "g", BR)
    E.escreve(c, "se misturam?", 84, 770, 140, "g", AMARELO)
    E.escreve(c, "a regra de três palavras", 84, 950, 90, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Semelhante", "dissolve", "semelhante")


def d(c):  # o macete: olhe a fórmula
    palco_capa(c)
    E.escreve(c, "só C e H?", 84, 380, 120, "i", BR)
    E.escreve(c, "→ gasolina", 900, 380, 120, "g", CLARO)
    E.escreve(c, "tem OH ou é iônico?", 84, 620, 110, "i", BR)
    E.escreve(c, "→ água", 1180, 620, 120, "g", CLARO)
    Q.formula(c, "C8H18     C2H5OH", 84, 900, 130, BR, escuro=True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_oleo_e_agua", a), ("capa_B_semelhante_dissolve", b), ("capa_C_pela_formula", d)):
    c = s.getCanvas()
    c.clear(skia.ColorWHITE)
    fn(c)
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
