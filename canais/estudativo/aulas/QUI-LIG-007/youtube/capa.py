"""Capas da QUI-LIG-007 (1280x720). Uso: python capa.py"""
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

def a(c):  # o gancho: ligações polares, molécula apolar
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.molecula_desenho(c, "CO2", 1360, 330, 200)
    Q.molecula_desenho(c, "H2O", 1360, 760, 200)
    E.escreve(c, "apolar", 84, 400, 150, "g", BR)
    E.escreve(c, "polar", 84, 820, 150, "g", AMARELO)
    E.escreve(c, "mesmas ligações polares", 84, 560, 80, "i", BR)
    E.escreve(c, "por quê?", 84, 990, 110, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Polaridade", "molecular", "sem decorar")


def d(c):  # o macete: regra dos pares livres
    palco_capa(c)
    E.escreve(c, "par livre no central?", 84, 380, 110, "i", BR)
    E.escreve(c, "polar", 84, 560, 170, "g", CLARO)
    E.escreve(c, "sem par e ligantes iguais?", 84, 760, 100, "i", BR)
    E.escreve(c, "apolar", 84, 930, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_polar_ou_apolar", a), ("capa_B_polaridade", b), ("capa_C_regra_dos_pares", d)):
    c = s.getCanvas()
    c.clear(skia.ColorWHITE)
    fn(c)
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
