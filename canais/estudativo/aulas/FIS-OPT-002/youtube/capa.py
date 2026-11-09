"""Capas do FIS-OPT-002 (1280x720). Uso: python capa.py"""
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
    E.escreve(c, "metade", 84, 420, 200, "g", AMARELO)
    E.escreve(c, "da sua altura", 84, 590, 130, "g", BR)
    E.escreve(c, "basta para se ver inteiro", 84, 800, 80, "i", BR)
    x, yb, h = 1450, 980, 640
    c.drawCircle(x, yb - h + 42, 42, M.paint(BR)); M.rrect(c, x - 45, yb - h + 90, 90, 240, 30, BR)
    for dx in (-1, 1):
        M.line(c, x + dx * 20, yb - 300, x + dx * 30, yb, BR, 1.0, 26)
    M.line(c, 1780, yb - h / 2 - h * 0.47, 1780, yb - h * 0.47, AMARELO, 1.0, 18)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Espelho", "plano", "reflexão do zero")


def d(c):  # o macete
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "r = i", 84, 420, 220, "g", BR)
    E.escreve(c, "medidos da", 84, 620, 110, "i", BR)
    E.escreve(c, "normal", 84, 790, 160, "g", claro)
    M.line(c, 1150, 860, 1820, 860, BR, 1.0, 10)
    M.line(c, 1485, 860, 1485, 420, BR, 0.7, 6, dash=[20, 14])
    M.line(c, 1200, 520, 1485, 860, COR, 1.0, 12); M.line(c, 1485, 860, 1770, 520, COR, 1.0, 12)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_metade_da_altura", a), ("capa_B_espelho_plano", b), ("capa_C_r_igual_a_i", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
