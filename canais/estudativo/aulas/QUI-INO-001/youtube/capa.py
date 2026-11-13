"""Capas da QUI-INO-001 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: o ácido só vira íons na água
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "na água,", 84, 380, 120, "i", BR)
    Q.formula(c, "HCl -> H^+ + Cl^-", 84, 600, 170, BR)
    E.escreve(c, "o ácido se parte", 84, 860, 120, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Ácidos", "na água", "do zero")


def d(c):  # o macete: O − H
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "forte ou fraco?", 84, 360, 120, "i", BR)
    E.escreve(c, "O − H", 84, 580, 200, "g", claro)
    Q.formula(c, "H2SO4", 84, 830, 160, BR, escuro=True)
    E.formula(c, "4 − 2 = 2: forte", 84, 1000, 100, "g", BR)


CAPAS = (("capa_A_acido_na_agua", a), ("capa_B_acidos", b), ("capa_C_oxigenio_menos_hidrogenio", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
