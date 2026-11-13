"""Capas da QUI-LIG-011 (1280x720). Uso: python capa.py"""
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

def a(c):  # o gancho: o gelo boia, ao contrário de quase tudo
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    c.drawRect(skia.Rect.MakeLTRB(1150, 520, 1820, 980), M.paint("#BFE3F2"))
    g = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1360, 410, 250, 230), 26, 26)
    c.drawRRect(g, M.paint("#F4FBFE")); c.drawRRect(g, M.paint("#7FB8D6", 1, stroke=6))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1150, 300, 670, 680), 20, 20), M.paint(BR, 1, stroke=8))
    E.escreve(c, "por que o", 84, 450, 140, "g", BR)
    E.escreve(c, "gelo boia?", 84, 620, 170, "g", AMARELO)
    E.escreve(c, "não é o ar", 84, 820, 110, "i", BR)
    E.escreve(c, "preso dentro", 84, 950, 110, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "O gelo", "boia", "e o inseto anda")


def d(c):  # o macete: comportamento estranho da água
    palco_capa(c)
    E.escreve(c, "água esquisita?", 84, 360, 120, "i", BR)
    for k, s in enumerate(("gelo boia", "película", "sobe no tubo")):
        E.pilula(c, s, 260 + 520 * k, 560, 70, "g", fundo="#2A2C36")
    E.escreve(c, "ligação de", 84, 820, 150, "g", CLARO)
    E.escreve(c, "hidrogênio", 84, 980, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_gelo_boia", a), ("capa_B_gelo_que_boia", b), ("capa_C_ligacao_de_hidrogenio", d)):
    c = s.getCanvas()
    c.clear(skia.ColorWHITE)
    fn(c)
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
