"""Capas do FIS-OPT-003 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def a(c):  # o gancho
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "qual espelho", 84, 400, 140, "g", BR)
    E.escreve(c, "aumenta?", 84, 560, 170, "g", AMARELO)
    E.escreve(c, "côncavo e convexo", 84, 760, 90, "i", BR)
    p = M.paint(BR, 1.0, stroke=16, cap_round=True)
    c.drawArc(skia.Rect.MakeXYWH(760, 220, 640, 640), -38, 76, False, p)
    c.drawArc(skia.Rect.MakeXYWH(1720, 220, 640, 640), 142, 76, False, p)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Espelhos", "curvos", "côncavo e convexo")


def d(c):  # o macete
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete:", 84, 330, 110, "i", BR)
    E.escreve(c, "o foco decide", 84, 500, 150, "g", BR)
    E.escreve(c, "antes dele: real e invertida", 84, 680, 76, "g", claro)
    E.escreve(c, "depois: virtual e maior", 84, 800, 76, "g", claro)
    E.orbita(c, 1600, 300, 180, E.mix(COR, BR, 0.82))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_concavo_ou_convexo", a), ("capa_B_espelhos_esfericos", b), ("capa_C_o_foco_decide", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
