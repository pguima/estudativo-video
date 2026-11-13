"""Capas da QUI-CAL-006 (1280x720). Uso: python capa.py"""
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
def a(c):  # o gancho: o de menor massa não é o limitante
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "10 g", 84, 420, 200, "g", BR)
    Q.formula(c, "H2", 560, 420, 200, BR)
    E.escreve(c, "64 g", 84, 680, 200, "g", BR)
    Q.formula(c, "O2", 560, 680, 200, BR)
    E.escreve(c, "quem acaba primeiro?", 84, 960, 110, "i", AMARELO)
    E.pilula(c, "não é o menor!", 1450, 560, 70, "g", fundo=AMARELO, cor="#121214")


def b(c):
    E.capa_modelo(c, "Química", "Reagente", "limitante", "e excesso")


def d(c):  # o macete: divida pela massa da equação
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete do limitante", 84, 330, 110, "i", BR)
    E.formula(c, "10 ÷ 4 = 2,5", 84, 560, 150, "g", BR)
    E.formula(c, "64 ÷ 32 = 2", 84, 760, 150, "g", claro)
    E.escreve(c, "o menor limita", 84, 980, 100, "g", claro)


CAPAS = (("capa_A_quem_acaba_primeiro", a), ("capa_B_reagente_limitante", b), ("capa_C_o_menor_limita", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
