"""Capas do MAT-ANG-010 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
LILAS = "#C9C9FF"
YS = (300, 480, 840)          # distâncias 1 : 2, como 3 e 6
KL = -0.15
KR = math.sqrt((4 / 3) ** 2 * (1 + KL ** 2) - 1)


def pl(y):
    return 430 + (y - YS[0]) * KL, y


def pr(y):
    return 600 + (y - YS[0]) * KR, y


def feixe(c, cima=LILAS, baixo=AMARELO):
    for y in YS:
        M.line(c, 60, y, 1120, y, BR, 1, 9)
    for f in (pl, pr):
        M.line(c, *f(YS[0] - 90), *f(YS[-1] + 90), BR, 1, 9)
    for f in (pl, pr):
        M.line(c, *f(YS[0]), *f(YS[1]), cima, 1, 18)
        M.line(c, *f(YS[1]), *f(YS[2]), baixo, 1, 18)


def a(c):  # o gancho: o quarteirão sem régua
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    feixe(c)
    E.escreve(c, "3", 290, 420, 110, "g", LILAS)
    E.escreve(c, "6", 230, 700, 110, "g", AMARELO)
    E.escreve(c, "4", 700, 410, 110, "g", LILAS)
    E.escreve(c, "?", 960, 650, 150, "g", AMARELO)
    E.escreve(c, "sem", 1210, 420, 150, "i", BR)
    E.escreve(c, "régua", 1200, 600, 190, "g", BR)
    E.escreve(c, "x = 8", 1210, 830, 170, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Teorema", "de Tales", "feixe de paralelas")


def d(c):  # o atalho: procure o fator
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    feixe(c, claro, AMARELO)
    E.escreve(c, "3", 290, 420, 100, "g", claro)
    E.escreve(c, "6", 230, 700, 100, "g", AMARELO)
    E.escreve(c, "4", 700, 410, 100, "g", claro)
    E.escreve(c, "8", 940, 650, 120, "g", AMARELO)
    E.escreve(c, "procure o", 1180, 400, 110, "i", BR)
    E.escreve(c, "fator", 1180, 590, 200, "g", BR)
    E.escreve(c, "×2", 1180, 830, 200, "g", AMARELO)
    E.escreve(c, "sem conta", 1450, 810, 80, "i", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sem_regua", a), ("capa_B_teorema_de_tales", b), ("capa_C_procure_o_fator", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
