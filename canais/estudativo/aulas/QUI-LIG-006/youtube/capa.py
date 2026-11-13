"""Capas da QUI-LIG-006 (1280x720). Uso: python capa.py"""
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

def a(c):  # o gancho: H₂O dobrada × CO₂ reta
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.molecula_desenho(c, "H2O", 480, 470, 230)
    Q.molecula_desenho(c, "CO2", 1380, 500, 220)
    Q.formula(c, "H2O", 330, 760, 140, BR)
    Q.formula(c, "CO2", 1230, 760, 140, BR)
    E.escreve(c, "dobrada", 84, 960, 130, "g", AMARELO)
    E.escreve(c, "× reta", 760, 960, 130, "g", BR)


def b(c):
    E.capa_modelo(c, "Química", "Geometria", "molecular", "do zero")


def d(c):  # o macete: ligantes e pares livres
    palco_capa(c)
    E.escreve(c, "conte no átomo central", 84, 310, 100, "i", BR)
    linhas = (("2 + 0 pares", "linear"), ("2 + par livre", "angular"), ("3 + 1 par", "piramidal"), ("4 ligantes", "tetraédrica"))
    for k, (p, r) in enumerate(linhas):
        y = 470 + 160 * k
        E.escreve(c, p, 84, y, 90, "b", BR)
        E.escreve(c, r, 900, y, 100, "g", CLARO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dobrada_ou_reta", a), ("capa_B_geometria_molecular", b), ("capa_C_conte_os_pares", d)):
    c = s.getCanvas()
    c.clear(skia.ColorWHITE)
    fn(c)
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
