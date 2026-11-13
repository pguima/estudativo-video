"""Capas da QUI-ATO-009 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: sódio explode, neônio nem liga
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "sódio explode,", 84, 380, 140, "g", BR)
    E.escreve(c, "neônio nem liga", 84, 560, 140, "g", AMARELO)
    E.escreve(c, "a culpa é da última camada", 84, 720, 80, "i", BR)
    Q.formula(c, "Na", 1300, 520, 260, BR)
    Q.formula(c, "Ne", 1300, 900, 260, E.mix(COR, "#FFFFFF", 0.75))


def b(c):
    E.capa_modelo(c, "Química", "Metais,", "ametais", "e famílias do zero")


def d(c):  # o macete: família − 18
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a carga do íon", 84, 380, 110, "i", BR)
    E.escreve(c, "família − 18", 84, 580, 170, "g", BR)
    E.formula(c, "17 − 18 = −1", 84, 800, 120, "g", AMARELO)
    Q.formula(c, "Cl^-", 1300, 820, 260, BR, escuro=True, cores={"carga": claro})


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sodio_explode_neonio_nem_liga", a), ("capa_B_metais_ametais_familias", b), ("capa_C_familia_menos_18", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
