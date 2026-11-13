"""Capas da QUI-LIG-009 (1280x720). Uso: python capa.py"""
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

def a(c):  # o gancho: a ligação de hidrogênio não é dentro da molécula
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.molecula_desenho(c, "H2O", 1180, 520, 170, giro=270)
    Q.molecula_desenho(c, "H2O", 1620, 700, 170, giro=270)
    M.line(c, 1310, 620, 1480, 690, AMARELO, 1, 14, dash=[22, 16])
    E.escreve(c, "a ligação de", 84, 430, 120, "g", BR)
    E.escreve(c, "hidrogênio", 84, 580, 150, "g", AMARELO)
    E.escreve(c, "é entre", 84, 760, 130, "g", BR)
    E.escreve(c, "moléculas", 84, 910, 130, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Forças entre", "moléculas", "as três")


def d(c):  # o macete: FON
    palco_capa(c)
    E.escreve(c, "H ligado a", 84, 350, 120, "i", BR)
    for k, el in enumerate(("F", "O", "N")):
        Q.atomo(c, 300 + 330 * k, 600, 130, el, escuro=True)
    E.escreve(c, "FON, como fone", 84, 930, 140, "g", CLARO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_dentro", a), ("capa_B_forcas_intermoleculares", b), ("capa_C_fon_como_fone", d)):
    c = s.getCanvas()
    c.clear(skia.ColorWHITE)
    fn(c)
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
