"""Capas da QUI-CAL-016 (1280x720). Uso: python capa.py"""
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
def a(c):  # o gancho: o anel nunca nasce no meio
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "o anel branco", 84, 360, 130, "g", BR)
    E.escreve(c, "nunca nasce", 84, 560, 170, "g", AMARELO)
    E.escreve(c, "no meio", 84, 740, 170, "g", AMARELO)
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(84, 860, 1800, 960), 50, 50)
    c.drawRRect(rr, M.paint(BR, 0.25)); c.drawRRect(rr, M.paint(BR, 1.0, stroke=8))
    x = 84 + (1800 - 84) * 0.6
    M.rrect(c, x - 26, 868, 52, 84, 14, BR, 1.0)
    Q.formula(c, "NH3", 200, 1040, 70, BR, align="center")
    Q.formula(c, "HCl", 1700, 1040, 70, BR, align="center")


def b(c):
    E.capa_modelo(c, "Química", "Lei de", "Graham", "difusão de gases")


def d(c):  # o macete: a raiz da razão
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "massa 16 vezes menor", 84, 330, 110, "i", BR)
    E.formula(c, "r{16} = 4", 84, 600, 220, "g", claro)
    E.escreve(c, "4 vezes mais rápido", 84, 820, 130, "g", BR)
    E.escreve(c, "não 16!", 84, 990, 90, "i", BR)


CAPAS = (("capa_A_anel_fora_do_meio", a), ("capa_B_lei_de_graham", b), ("capa_C_raiz_da_razao", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
