"""Capas do FIS-EGF-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: ferro e isopor recebem o mesmo empuxo
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "ferro e isopor:", 84, 380, 120, "i", BR)
    E.escreve(c, "o mesmo", 84, 570, 180, "g", BR)
    E.escreve(c, "empuxo?", 84, 760, 180, "g", AMARELO)
    c.drawRect(skia.Rect.MakeLTRB(1150, 360, 1850, 1000), M.paint("#5AB4E6", 0.8))
    M.line(c, 1150, 360, 1850, 360, BR, 1.0, 8)
    for cx, cor in ((1340, "#6E7380"), (1660, "#F4F4F0")):
        E.bola(c, cx, 720, 110, cor)
        F.seta(c, cx, 590, cx, 420, "#1F6FEB", 1.0, 16)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Empuxo", "do zero", "Arquimedes")


def d(c):  # o macete: 1 litro de água = 10 N de empuxo
    palco_capa(c)
    E.escreve(c, "na água,", 84, 330, 110, "i", BR)
    E.escreve(c, "cada litro dentro", 84, 490, 120, "g", BR)
    E.escreve(c, "= 10 N", 84, 720, 210, "g", AMARELO)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "3 L  →  30 N de empuxo", 84, 950, 90, "g", claro)


CAPAS = (("capa_A_ferro_e_isopor", a), ("capa_B_empuxo_arquimedes", b), ("capa_C_cada_litro_10_N", d))

pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
