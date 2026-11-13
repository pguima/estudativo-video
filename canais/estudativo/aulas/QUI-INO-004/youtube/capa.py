"""Capas da QUI-INO-004 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)




def a(c):  # o gancho: um gás que vira ácido
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "um gás", 84, 400, 150, "g", BR)
    E.escreve(c, "que vira ácido", 84, 580, 150, "g", AMARELO)
    Q.formula(c, "CO2 + H2O -> H2CO3", 84, 860, 110, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Óxidos", "na água", "do zero")


def d(c):  # o macete: metal → base, ametal → ácido
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "olhe o outro elemento", 84, 340, 100, "i", BR)
    E.escreve(c, "metal → base", 84, 560, 150, "g", BR)
    E.escreve(c, "ametal → ácido", 84, 760, 150, "g", claro)
    Q.formula(c, "CaO   SO3   CO", 84, 980, 110, BR, escuro=True)


CAPAS = (("capa_A_gas_que_vira_acido", a), ("capa_B_oxidos", b), ("capa_C_metal_ou_ametal", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
