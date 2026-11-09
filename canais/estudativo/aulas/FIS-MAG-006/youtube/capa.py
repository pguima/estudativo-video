"""Capas do FIS-MAG-006 (1280x720). Uso: python capa.py"""
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
COBRE = "#C27A44"
E.usar("Física")


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: o ímã que cai devagar no cano de cobre
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o ímã que", 84, 380, 140, "i", BR)
    E.escreve(c, "cai devagar", 84, 600, 190, "g", BR)
    E.escreve(c, "no cobre", 84, 790, 150, "g", AMARELO)
    cx = 1560
    M.rrect(c, cx - 150, 90, 300, 900, 30, E.mix(COBRE, BR, 0.5))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 150, 90, 300, 900), 30, 30), M.paint("#7A4520", 1, stroke=12))
    M.rrect(c, cx - 60, 390, 120, 120, 12, F.NEG)
    M.rrect(c, cx - 60, 510, 120, 120, 12, COR)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 60, 390, 120, 240), 12, 12), M.paint(BR, 1, stroke=6))
    E._meio(c, "S", cx, 450, 70, "g", BR); E._meio(c, "N", cx, 570, 70, "g", BR)
    for k in (-1, 1):
        F.seta(c, cx + k * 100, 720, cx + k * 100, 560, BR, 1, 14)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Lei de", "Lenz", "do zero")


def d(c):  # o macete
    palco_capa(c)
    E.escreve(c, "chegou,", 84, 400, 170, "g", BR)
    E.escreve(c, "repele", 790, 400, 170, "g", E.mix(COR, BR, 0.5))
    E.escreve(c, "saiu,", 84, 620, 170, "g", BR)
    E.escreve(c, "atrai", 520, 620, 170, "g", E.mix(COR, BR, 0.5))
    E.escreve(c, "face norte = anti-horário", 84, 850, 90, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_ima_no_cano_de_cobre", a), ("capa_B_lei_de_lenz", b), ("capa_C_chegou_repele_saiu_atrai", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
