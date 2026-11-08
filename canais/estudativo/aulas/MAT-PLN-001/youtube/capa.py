"""Capas do MAT-PLN-001 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: o grau não é 2 nem 5
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "5x^2 + x^3", 84, 470, 230, cor=BR)
    E.escreve(c, "grau?", 84, 700, 150, "i", BR)
    E.formula(c, "2", 520, 700, 150, cor=BR)
    E.risco(c, 490, 720, 640, 560, 9, 0, AMARELO, 22)
    E.formula(c, "5", 720, 700, 150, cor=BR)
    E.risco(c, 690, 720, 840, 560, 9, 0, AMARELO, 22)
    E.bola(c, 1520, 600, 260, AMARELO)
    E.formula(c, "3", 1520, 700, 300, cor=COR, align="center")
    E.escreve(c, "o que é polinômio", 84, 980, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "O que é", "polinômio", "grau e valor")


def d(c):  # o atalho: P(1) é a soma dos coeficientes
    palco(c)
    E.escreve(c, "o atalho", 84, 330, 130, "i", BR)
    E.formula(c, "P(1)", 84, 600, 260, cor=AMARELO)
    E.escreve(c, "= soma dos", 680, 560, 120, "i", BR)
    E.escreve(c, "coeficientes", 680, 680, 120, "g", BR)
    E.formula(c, "2x^3 − x + 5  →  2 − 1 + 5 = 6", 84, 930, 110, cor="#C9C3FF")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_grau", a), ("capa_B_polinomio", b), ("capa_C_soma_coeficientes", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
