"""Capas do FIS-EGF-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: navio boia, prego afunda
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o navio boia,", 84, 400, 130, "g", BR)
    E.escreve(c, "o prego afunda", 84, 580, 130, "g", BR)
    E.escreve(c, "por quê?", 84, 780, 170, "g", AMARELO)
    c.drawRect(skia.Rect.MakeLTRB(1120, 640, 1900, 1080), M.paint("#5AB4E6", 0.8))
    M.line(c, 1120, 640, 1900, 640, BR, 1.0, 8)
    p = skia.Path(); p.moveTo(1180, 520); p.lineTo(1640, 520); p.lineTo(1580, 720); p.lineTo(1240, 720); p.close()
    c.drawPath(p, M.paint("#2A2A30"))
    M.rrect(c, 1330, 420, 160, 100, 12, "#2A2A30")
    M.line(c, 1780, 860, 1780, 980, "#2A2A30", 1.0, 14)
    M.line(c, 1750, 860, 1810, 860, "#2A2A30", 1.0, 14)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Flutuar", "ou afundar", "do zero")


def d(c):  # o macete: a fração submersa é a densidade
    palco_capa(c)
    E.escreve(c, "quanto fica debaixo d'água?", 84, 330, 90, "i", BR)
    E.escreve(c, "a densidade diz", 84, 490, 120, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "gelo 0,9  →  9/10 dentro", 84, 740, 110, "g", AMARELO)
    E.formula(c, "madeira 0,6  →  6/10 dentro", 84, 930, 90, "g", claro)


CAPAS = (("capa_A_navio_boia_prego_afunda", a), ("capa_B_flutuar_ou_afundar", b), ("capa_C_a_densidade_diz", d))

pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
