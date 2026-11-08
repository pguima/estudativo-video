"""Capas do MAT-FUN-018 (1280x720). Uso: python capa.py"""
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


def parabola(c, x, y, w, h, fn, cor, x0=-0.6, x1=4.6, ymin=-2, ymax=5, largura=12):
    X = lambda v: x + (v - x0) / (x1 - x0) * w
    Y = lambda v: y + h - (v - ymin) / (ymax - ymin) * h
    M.arrow(c, x, Y(0), x + w + 30, Y(0), BR, 1, 6, 24)
    M.arrow(c, X(0), y + h, X(0), y - 30, BR, 1, 6, 24)
    pa = skia.Path()
    for i in range(201):
        v = x0 + (x1 - x0) * i / 200
        (pa.lineTo if i else pa.moveTo)(X(v), Y(fn(v)))
    c.save(); c.clipRect(skia.Rect.MakeXYWH(x - 10, y - 10, w + 20, h + 20))
    c.drawPath(pa, M.paint(cor, 1, stroke=largura, cap_round=True))
    c.restore()
    return X, Y


def a(c):  # o gancho: onde a parábola faz a curva
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "onde ela", 84, 420, 140, "i", BR)
    E.escreve(c, "faz a curva?", 76, 620, 180, "g", BR)
    E.escreve(c, "o vértice sem desenhar", 84, 820, 90, "i", AMARELO)
    X, Y = parabola(c, 1220, 230, 560, 640, lambda v: v * v - 4 * v + 3, BR)
    M.line(c, X(2), Y(5), X(2), Y(-2), BR, 0.7, 5, dash=[18, 12])
    c.drawCircle(X(2), Y(-1), 30, M.paint(AMARELO))
    c.drawCircle(X(2), Y(-1), 30, M.paint("#07070F", 1, stroke=5))


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Vértice da", "parábola", "x = −b/2a")


def d(c):  # o atalho: média das raízes
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o vértice no", 84, 400, 130, "i", claro)
    E.escreve(c, "meio das", 76, 600, 190, "g", BR)
    E.escreve(c, "raízes", 76, 790, 190, "g", BR)
    E.formula(c, "f{1 + 5}{2} = 3", 84, 960, 100, "g", AMARELO)
    X, Y = parabola(c, 1220, 230, 560, 640, lambda v: (v - 1) * (v - 5), claro, x0=-0.3, x1=6.3, ymin=-5, ymax=5)
    for r in (1, 5):
        c.drawCircle(X(r), Y(0), 24, M.paint(AMARELO, 1, stroke=8))
    M.line(c, X(3), Y(5), X(3), Y(-5), BR, 0.7, 5, dash=[18, 12])
    c.drawCircle(X(3), Y(-4), 26, M.paint(AMARELO))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_onde_faz_a_curva", a), ("capa_B_vertice_da_parabola", b), ("capa_C_meio_das_raizes", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
