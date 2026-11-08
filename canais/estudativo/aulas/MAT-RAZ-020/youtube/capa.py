"""Capas do MAT-RAZ-020 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: 3 cm no mapa valem quantos km?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 cm", 84, 440, 250, "g", BR)
    E.escreve(c, "no mapa =", 84, 620, 130, "i", BR)
    E.escreve(c, "? km", 84, 900, 250, "g", BR)
    # mapa à direita: duas cidades e a régua
    x, y, w, h = 1120, 330, 700, 460
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26)
    c.drawRRect(rr, M.paint(BR, 0.95))
    ax, bx, cy = x + 150, x + w - 150, y + 200
    for cx in (ax, bx):
        c.drawCircle(cx, cy, 26, M.paint(COR))
    M.line(c, ax, cy + 80, bx, cy + 80, E.TINTA, 1, 9)
    for xx in (ax, bx):
        M.line(c, xx, cy + 58, xx, cy + 102, E.TINTA, 1, 9)
    E.centro(c, "1 : 50.000", x + w / 2, y + h - 50, 70, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Escala", "1 : 100", "papel e real")


def d(c):  # o macete
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    cl = E.mix(COR, BR, 0.55)
    E.escreve(c, "quanto vale", 84, 360, 140, "i", BR)
    E.escreve(c, "1 cm?", 84, 600, 250, "g", BR)
    E.escreve(c, "1 : 50.000", 1060, 600, 130, "g", cl)
    E.escreve(c, "1 cm = 500 m", 84, 900, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_3cm_no_mapa", a), ("capa_B_escala", b), ("capa_C_quanto_vale_1cm", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
