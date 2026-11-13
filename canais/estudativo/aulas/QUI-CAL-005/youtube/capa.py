"""Capas da QUI-CAL-005 (1280x720). Uso: python capa.py"""
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
def a(c):  # o gancho: 46 g de etanol → 88 g de CO2
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "queima 46 g", 84, 360, 150, "g", BR)
    E.escreve(c, "sai 88 g", 84, 580, 190, "g", AMARELO)
    Q.formula(c, "CO2", 900, 580, 190, AMARELO)
    E.escreve(c, "de onde veio a massa a mais?", 84, 990, 84, "i", BR)
    Q.molecula_desenho(c, "CO2", 1560, 780, 150)


def b(c):
    E.capa_modelo(c, "Química", "Estequio-", "metria", "massa a massa")


def d(c):  # o macete: massas embaixo da equação
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho das massas", 84, 330, 110, "i", BR)
    Q.formula(c, "C2H6O → 2 CO2", 84, 560, 150, BR, escuro=True, cores={"coef": claro})
    E.escreve(c, "46 g", 120, 720, 120, "g", claro)
    E.escreve(c, "88 g", 780, 720, 120, "g", claro)
    E.escreve(c, "uma regra de três e pronto", 84, 990, 84, "i", BR)


CAPAS = (("capa_A_46g_vira_88g", a), ("capa_B_massa_a_massa", b), ("capa_C_massas_embaixo", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
