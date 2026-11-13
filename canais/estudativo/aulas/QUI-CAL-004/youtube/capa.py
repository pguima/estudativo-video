"""Capas da QUI-CAL-004 (1280x720). Uso: python capa.py"""
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
def a(c):  # o gancho: toda água pura tem a mesma receita
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "toda água pura:", 84, 330, 110, "i", BR)
    E.escreve(c, "1 g de H", 84, 540, 160, "g", BR)
    E.escreve(c, "para 8 g de O", 84, 730, 160, "g", AMARELO)
    E.escreve(c, "sempre. Por quê?", 84, 960, 100, "i", BR)
    Q.molecula_desenho(c, "H2O", 1580, 420, 200)


def b(c):
    E.capa_modelo(c, "Química", "Lei de", "Proust", "e mols")


def d(c):  # o macete: a receita 1 : 8 : 9
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a receita da água", 84, 340, 120, "i", BR)
    E.escreve(c, "1 : 8 : 9", 76, 600, 260, "g", claro)
    E.escreve(c, "40 g de O → 5 g de H", 84, 840, 100, "g", BR)
    E.escreve(c, "sem regra de três", 84, 990, 80, "i", BR)


CAPAS = (("capa_A_receita_da_agua", a), ("capa_B_lei_de_proust", b), ("capa_C_um_oito_nove", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
