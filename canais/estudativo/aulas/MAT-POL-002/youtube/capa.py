"""Capas do MAT-POL-002 (1280x720). Uso: python capa.py"""
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


def reg(n, cx, cy, r):
    ini = 90 - 180 / n
    return [(cx + r * math.cos(math.radians(ini + k * 360 / n)), cy + r * math.sin(math.radians(ini + k * 360 / n))) for k in range(n)]


def contorno(c, pts, cor, larg=12, alfa_f=0.0):
    p = skia.Path(); p.addPoly(pts, True)
    if alfa_f:
        c.drawPath(p, M.paint(cor, alfa_f))
    pa = M.paint(cor, 1, stroke=larg); pa.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pa)


def a(c):  # o gancho: 18 ou 9 diagonais?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    P = reg(6, 470, 600, 330)
    contorno(c, P, BR, 12, 0.1)
    for i in range(6):
        for j in range(i + 2, 6):
            if (i, j) != (0, 5):
                M.line(c, *P[i], *P[j], AMARELO, 1, 7)
    for V in P:
        c.drawCircle(*V, 14, M.paint(BR))
    E.escreve(c, "quantas", 920, 360, 130, "i", BR)
    E.escreve(c, "diagonais?", 900, 560, 170, "g", BR)
    E.escreve(c, "18", 920, 860, 220, "g", "#FF8A8A")
    M.line(c, 900, 820, 1190, 700, "#FF8A8A", 1, 22)
    E.escreve(c, "9!", 1280, 860, 240, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Soma dos", "ângulos", "e diagonais")


def d(c):  # o atalho: + 180° por lado
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho", 90, 340, 130, "i", BR)
    E.escreve(c, "+ 180° por lado", 90, 540, 170, "g", BR)
    for i, (n, s) in enumerate(((3, "180°"), (4, "360°"), (5, "540°"), (6, "720°"))):
        cx = 260 + i * 470
        contorno(c, reg(n, cx, 760, 105), claro, 9)
        E.centro(c, s, cx, 990, 110, "g", AMARELO if n == 6 else BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quantas_diagonais", a), ("capa_B_soma_e_diagonais", b), ("capa_C_mais_180", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
