"""Capas do FIS-EGF-005 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def tanque_capa(c, x, y, w, h):
    c.drawRect(skia.Rect.MakeXYWH(x, y + 60, w, h - 60), M.paint("#5AB4E6", 0.75))
    M.line(c, x, y + 60, x + w, y + 60, BR, 1.0, 6)
    for X in (x, x + w):
        M.line(c, X, y, X, y + h, BR, 1.0, 8)
    M.line(c, x, y + h, x + w, y + h, BR, 1.0, 8)


def a(c):  # o gancho: a 10 m, a pressão dobra
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a 10 metros", 84, 380, 120, "i", BR)
    E.escreve(c, "a pressão", 84, 570, 180, "g", BR)
    E.escreve(c, "dobra", 84, 760, 180, "g", AMARELO)
    tanque_capa(c, 1300, 160, 420, 780)
    for m, s in ((0, "1 atm"), (10, "2 atm"), (20, "3 atm")):
        y = 220 + m * 30
        M.line(c, 1270, y, 1300, y, BR, 1.0, 5)
        E.escreve(c, s, 1050, y + 18, 56, "g", BR if m != 10 else AMARELO)
    M.rrect(c, 1450, 500, 120, 44, 16, "#1B1B20")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Lei de", "Stevin", "do zero")


def d(c):  # o macete: cada 10 m de água, +1 atm
    palco_capa(c)
    E.escreve(c, "sem fazer conta:", 84, 330, 100, "i", BR)
    E.escreve(c, "cada 10 m de água", 84, 490, 120, "g", BR)
    E.escreve(c, "+1 atm", 84, 720, 210, "g", AMARELO)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "30 m  →  4 atm no total", 84, 950, 90, "g", claro)


CAPAS = (("capa_A_a_pressao_dobra", a), ("capa_B_lei_de_stevin", b), ("capa_C_cada_10_metros", d))

pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
