"""Capas da QUI-CAL-007 (1280x720). Uso: python capa.py"""
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
def a(c):  # o gancho: 200 g de calcário não dão 112 g de cal
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "200 g de calcário", 84, 360, 130, "g", BR)
    E.escreve(c, "112 g de cal?", 84, 580, 150, "g", BR)
    E.risco(c, 70, 610, 1040, 470, 9, 0, AMARELO, 30)
    E.escreve(c, "saem 89,6 g", 84, 800, 170, "g", AMARELO)
    E.escreve(c, "o que a conta esqueceu?", 84, 990, 90, "i", BR)
    E.simbolo(c, 1600, 600, 230, cor=E.mix(COR, BR, 0.82), forma="hexagono")


def b(c):
    E.capa_modelo(c, "Química", "Pureza dos", "reagentes", "estequiometria")


def d(c):  # o macete: pureza no começo ou no fim
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "pureza no começo", 84, 340, 110, "i", BR)
    E.escreve(c, "ou no fim?", 84, 470, 110, "i", BR)
    E.formula(c, "× 0,8", 84, 720, 220, "g", claro)
    E.escreve(c, "dá o mesmo resultado", 84, 960, 100, "g", BR)


CAPAS = (("capa_A_o_que_a_conta_esqueceu", a), ("capa_B_pureza", b), ("capa_C_comeco_ou_fim", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
