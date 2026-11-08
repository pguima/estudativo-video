"""Capas do MAT-PRO-006 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AM = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def arco(c, x0, x1, y, alto, cor, largura=10):
    p = skia.Path()
    for i in range(41):
        u = i / 40
        X, Y = x0 + (x1 - x0) * u, y - alto * math.sin(u * math.pi)
        p.lineTo(X, Y) if i else p.moveTo(X, Y)
    c.drawPath(p, M.paint(cor, 1, stroke=largura, cap_round=True))


def a(c):  # o gancho: 1 + 2 + … + 100 em segundos
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    s = "1 + 2 + … + 99 + 100"
    x0 = 84
    E.escreve(c, s, x0, 560, 150, "g", BR)
    w1 = E.larg("1", "g", 150)
    wall = E.larg(s, "g", 150)
    w100 = E.larg("100", "g", 150)
    arco(c, x0 + w1 / 2, x0 + wall - w100 / 2, 420, 170, AM)
    E.centro(c, "101", x0 + wall / 2, 230, 90, "g", AM)
    E.escreve(c, "em segundos:", 84, 860, 120, "i", BR)
    E.escreve(c, "5.050", 900, 880, 220, "g", AM)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Soma", "da PA", "a ideia de Gauss")


def d(c):  # o atalho: média vezes quantidade
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.escreve(c, "média ×", 76, 540, 190, "g", BR)
    E.escreve(c, "quantidade", 76, 730, 190, "g", BR)
    E.escreve(c, "34 · 30 = 1.020", 84, 940, 120, "g", AM)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_gauss_5050", a), ("capa_B_soma_da_pa", b), ("capa_C_media_vezes_quantidade", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
