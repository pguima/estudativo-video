"""Capas do MAT-ANG-017 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF6B6B"


def a(c):  # o gancho: lado 5, diagonal não é 10
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    x, y, l = 170, 300, 520
    c.drawRect(skia.Rect.MakeXYWH(x, y, l, l), M.paint(BR, 1, stroke=14))
    M.line(c, x, y + l, x + l, y, AMARELO, 1, 16)
    E.escreve(c, "5", x + l / 2 - 30, y + l + 120, 110, "g", BR)
    E.formula(c, "5r{2}", x + 120, y + l / 2 - 10, 110, "g", AMARELO)
    E.escreve(c, "10?", 1000, 430, 150, "g", LILAS)
    M.line(c, 980, 390, 1280, 330, VERMELHO, 1, 16)
    E.escreve(c, "a diagonal", 1000, 640, 120, "i", BR)
    E.formula(c, "≈ 7", 1000, 870, 220, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Diagonal", "e altura", "quadrado e equilátero")


def d(c):  # o atalho: √2 no quadrado, √3 no triângulo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    c.drawRect(skia.Rect.MakeXYWH(220, 320, 380, 380), M.paint(BR, 1, stroke=12))
    M.line(c, 220, 700, 600, 320, claro, 1, 12)
    B1, B2 = (1100, 700), (1540, 700)
    T = (1320, 700 - 440 * math.sqrt(3) / 2)
    for P, Q in ((B1, B2), (B2, T), (T, B1)):
        M.line(c, *P, *Q, BR, 1, 12)
    M.line(c, *T, 1320, 700, claro, 1, 10)
    E.formula(c, "ℓr{2}", 410, 930, 170, "g", AMARELO, 1, "center")
    E.formula(c, "f{ℓr{3}}{2}", 1320, 920, 140, "g", AMARELO, 1, "center")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_10", a), ("capa_B_diagonal_e_altura", b), ("capa_C_raiz_2_e_raiz_3", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
