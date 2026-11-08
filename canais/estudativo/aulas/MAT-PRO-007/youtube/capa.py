"""Capas do MAT-PRO-007 (1280x720). Uso: python capa.py"""
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


def tri(c, x, y, n, L, cor, novo=None, w=14):
    """n triângulos de palitos alternados; os palitos da última figura nova em `novo`"""
    h = L * math.sqrt(3) / 2
    B = lambda i: (x + i * L, y)
    T = lambda i: (x + L / 2 + i * L, y - h)
    segs = []
    for j in range(n + 1):
        segs.append((("d", j), (B(j // 2), T(j // 2)) if j % 2 == 0 else (T((j - 1) // 2), B((j + 1) // 2))))
    for k in range(n):
        segs.append((("h", k), (B(k // 2), B(k // 2 + 1)) if k % 2 == 0 else (T((k - 1) // 2), T((k + 1) // 2))))
    for k, ((x0, y0), (x1, y1)) in segs:
        cc = novo if novo and k in (("d", n), ("h", n - 1)) else cor
        d = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / d, (y1 - y0) / d
        M.line(c, x0 + ux * 12, y0 + uy * 12, x1 - ux * 12, y1 - uy * 12, cc, 1, w)


def a(c):  # o gancho: as figuras de palitos, pause e resolva
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    tri(c, 100, 470, 1, 170, BR)
    tri(c, 400, 470, 2, 170, BR, AM)
    tri(c, 790, 470, 3, 170, BR, AM)
    for cx, v in ((185, "3"), (527, "5"), (960, "7")):
        E.centro(c, v, cx, 610, 100, "g", BR)
    E.escreve(c, "e a figura 30?", 84, 860, 150, "i", BR)
    E.escreve(c, "61", 1500, 900, 300, "g", AM)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Praticando", "PA", "4 situações reais")


def d(c):  # o macete: termos = saltos + 1
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "não esqueça", 84, 340, 140, "i", BR)
    E.escreve(c, "termos =", 76, 540, 190, "g", BR)
    E.escreve(c, "saltos + 1", 76, 730, 190, "g", AM)
    y = 990
    M.line(c, 100, y, 1820, y, BR, 1, 6)
    xs = [180 + i * 190 for i in range(9)]
    for i, x in enumerate(xs):
        M.line(c, x, y, x, y - 70, BR, 1, 6)
        E.bola(c, x, y - 92, 24, COR)
        if i < 8:
            E.salto(c, 9, 0, x + 12, xs[i + 1] - 12, y - 130, 40, AM, None, largura=6)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_figura_30", a), ("capa_B_praticando_pa", b), ("capa_C_saltos_mais_um", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
