"""Capas da QUI-CAL-009 (1280x720). Uso: python capa.py"""
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
def a(c):  # o gancho: 4 questões de prova
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "estequiometria", 84, 360, 140, "g", BR)
    E.escreve(c, "4 questões", 84, 600, 220, "g", AMARELO)
    E.escreve(c, "mol · pureza · rendimento · limitante", 84, 790, 70, "g", BR)
    E.escreve(c, "você resolve antes de mim?", 84, 990, 90, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Praticando", "mol e", "estequiometria")


def d(c):  # o macete: um caminho só
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "um caminho só", 84, 330, 120, "i", BR)
    for k, s in enumerate(("1  a parte que reage", "2  massas da equação", "3  rendimento no fim")):
        E.escreve(c, s, 84, 540 + k * 170, 110, "g", claro if k == 1 else BR)


CAPAS = (("capa_A_4_questoes", a), ("capa_B_praticando", b), ("capa_C_um_caminho", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
