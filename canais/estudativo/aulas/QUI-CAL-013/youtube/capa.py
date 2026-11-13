"""Capas da QUI-CAL-013 (1280x720). Uso: python capa.py"""
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
def a(c):  # o gancho: três gases, o mesmo volume
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    for k, f in enumerate(("H2", "O2", "CO2")):
        x = 260 + k * 420
        c.drawOval(skia.Rect.MakeXYWH(x - 150, 230, 300, 360), M.paint(BR, 0.22))
        c.drawOval(skia.Rect.MakeXYWH(x - 150, 230, 300, 360), M.paint(BR, 1.0, stroke=9))
        Q.formula(c, f, x, 470, 110, BR, align="center")
    E.escreve(c, "o mesmo volume?", 84, 800, 150, "g", AMARELO)
    E.escreve(c, "22,4 L por mol nas CNTP", 84, 990, 90, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Volume", "molar", "22,4 L")


def d(c):  # o macete: volume segue o coeficiente
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "entre gases:", 84, 330, 110, "i", BR)
    Q.formula(c, "3 O2 → 2 CO2", 84, 580, 170, BR, escuro=True, cores={"coef": claro})
    E.escreve(c, "3 L → 2 L", 84, 800, 150, "g", claro)
    E.escreve(c, "sem o 22,4", 84, 990, 90, "i", BR)


CAPAS = (("capa_A_mesmo_volume", a), ("capa_B_volume_molar", b), ("capa_C_volume_e_coeficiente", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
