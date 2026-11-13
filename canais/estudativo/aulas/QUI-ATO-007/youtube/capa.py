"""Capas da QUI-ATO-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o íon misterioso
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "16 prótons", 84, 380, 110, "g", BR)
    E.escreve(c, "18 elétrons", 84, 520, 110, "g", BR)
    E.escreve(c, "qual a carga?", 84, 720, 150, "g", AMARELO)
    E.escreve(c, "4 questões resolvidas", 84, 900, 80, "i", BR)
    Q.formula(c, "S^?", 1300, 640, 360, BR)


def b(c):
    E.capa_modelo(c, "Química", "Praticando:", "o átomo", "4 questões")


def d(c):  # o macete: carga = prótons − elétrons
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "carga =", 84, 400, 140, "g", BR)
    E.escreve(c, "prótons − elétrons", 84, 580, 130, "g", claro)
    E.formula(c, "16 − 18 = −2", 84, 820, 150, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_a_carga", a), ("capa_B_praticando_o_atomo", b), ("capa_C_carga_protons_menos_eletrons", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
