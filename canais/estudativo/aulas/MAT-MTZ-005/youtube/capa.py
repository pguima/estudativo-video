"""Capas do MAT-MTZ-005 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"


def a(c):  # o desafio: 5 questões
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5", 70, 700, 560, "g", AMARELO)
    E.escreve(c, "questões", 470, 470, 170, "g", BR)
    E.escreve(c, "de matrizes", 480, 640, 120, "i", BR)
    E.matriz(c, 9, 0, [[1, 0, 2], [-1, 3, 1], [2, 1, 0]], 1620, 520, 96, cor=BR, barras=True, escuro=True)
    E.escreve(c, "= ?", 1520, 870, 150, "g", AMARELO)
    E.escreve(c, "você resolve antes de mim?", 84, 990, 90, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Matrizes", "na prática", "5 questões")


def d(c):  # o atalho: não calcule o produto inteiro
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "produto de matrizes:", 84, 380, 120, "i", BR)
    E.escreve(c, "calcule 1 só", 76, 590, 200, "g", BR)
    for n, m in enumerate(([[4, 8], [5, 4]], [[4, 8], [7, -4]])):
        G = E.matriz(c, 9, 0, m, 380 + n * 560, 850, 100, escuro=True, cor=BR, cores={(1, 0): AMARELO})
        E.matriz_marca(c, G, 1, 0, AMARELO, 1, 1, cheia=0.0)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_5_questoes", a), ("capa_B_matrizes_na_pratica", b), ("capa_C_calcule_1_so", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
