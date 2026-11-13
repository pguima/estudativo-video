"""Capas da QUI-ELE-009 (1280x720). Uso: python capa.py"""
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


def base(c):
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)


def salvar(capas):
    pasta = Path(__file__).parent
    s = skia.Surface(E.W, E.H)
    for nome, fn in capas:
        fn(s.getCanvas())
        tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
        tmp.unlink()


def a(c):  # o gancho: sal na água não dá sódio
    base(c)
    Q.formula(c, "NaCl(aq)", 84, 420, 170, BR)
    E.escreve(c, "não dá sódio.", 84, 640, 150, "g", AMARELO)
    E.escreve(c, "dá hidrogênio.", 84, 810, 150, "g", BR)
    E.escreve(c, "eletrólise aquosa", 84, 980, 80, "i", BR)
    for k in range(9):
        c.drawCircle(1500 + 60 * math.sin(k * 1.7), 900 - 80 * k, 26 + 6 * (k % 3), M.paint(BR, 0.85))


def b(c):
    E.capa_modelo(c, "Química", "Eletrólise", "aquosa", "do zero")


def d(c):  # o macete: família 1, 2 e Al dão H2
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho dos polos", 84, 300, 110, "i", BR)
    E.escreve(c, "família 1, 2 e Al", 84, 500, 120, "g", BR)
    Q.formula(c, "-> H2", 1160, 500, 120, AMARELO, escuro=True)
    E.escreve(c, "ânion com O", 84, 720, 120, "g", BR)
    Q.formula(c, "-> O2", 1160, 720, 120, AMARELO, escuro=True)
    E.escreve(c, "senão, sai o próprio íon", 84, 920, 80, "i", claro)


salvar((("capa_A_nao_da_sodio", a), ("capa_B_eletrolise_aquosa", b), ("capa_C_familia_1_2_e_al", d)))
