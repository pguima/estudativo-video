"""Capas da QUI-LIG-004 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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


CLARO = E.mix(COR, BR, 0.5)

def a(c):  # o gancho: sal, gelo, ferro: quem conduz?
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    for k, f in enumerate(("NaCl", "H2O", "Fe")):
        Q.formula(c, f, 120 + 560 * k, 500, 200, BR)
    E.escreve(c, "quem conduz", 84, 780, 150, "g", AMARELO)
    E.escreve(c, "sólido?", 84, 950, 150, "g", BR)


def b(c):
    E.capa_modelo(c, "Química", "Qual é a", "ligação?", "e o que explica")


def d(c):  # o macete: olhe a condução
    palco_capa(c)
    for k, (p, r) in enumerate((("conduz sólido?", "metálica"), ("só derretido?", "iônica"), ("não conduz?", "molecular"))):
        y = 380 + 240 * k
        E.escreve(c, p, 84, y, 100, "i", BR)
        E.escreve(c, r, 1000, y, 110, "g", CLARO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quem_conduz", a), ("capa_B_qual_e_a_ligacao", b), ("capa_C_pela_conducao", d)):
    c = s.getCanvas()
    c.clear(skia.ColorWHITE)
    fn(c)
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
