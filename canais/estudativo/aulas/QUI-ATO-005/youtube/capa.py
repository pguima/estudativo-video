"""Capas da QUI-ATO-005 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 4s antes do 3d
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "por que o", 84, 360, 120, "i", BR)
    E.formula(c, "4s", 84, 600, 260, "g", AMARELO)
    E.escreve(c, "vem antes do", 470, 560, 90, "i", BR)
    E.formula(c, "3d?", 960, 600, 260, "g", BR)
    E.formula(c, "1s^2 2s^2 2p^6 3s^2 3p^6 4s^2 3d^6", 84, 900, 88, "g", BR)


def b(c):
    E.capa_modelo(c, "Química", "Diagrama", "de Pauling", "do zero")


def d(c):  # o macete: siga as diagonais e some os expoentes
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "siga as", 84, 400, 120, "i", BR)
    E.escreve(c, "diagonais", 84, 580, 170, "g", BR)
    E.escreve(c, "ferro em 1 minuto", 84, 760, 90, "g", claro)
    Q.pauling(c, 99, 0, 1180, 220, 70, Z=26, escuro=True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_4s_antes_do_3d", a), ("capa_B_diagrama_de_pauling", b), ("capa_C_siga_as_diagonais", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
