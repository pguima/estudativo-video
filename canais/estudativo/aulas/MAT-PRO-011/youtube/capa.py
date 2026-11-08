"""Capas do MAT-PRO-011 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AM = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: infinitos passos, total 2
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "infinitos passos", 84, 360, 140, "g", BR)
    E.formula(c, "1 + f{1}{2} + f{1}{4} + f{1}{8} + …", 84, 640, 130, "g", E.mix(COR, BR, 0.6))
    E.escreve(c, "= 2", 84, 960, 260, "g", AM)
    x0, x1, y = 760, 1760, 930  # a barra dos passos até a parede
    pos = 0.0
    for k in range(9):
        w = (x1 - x0) / 2 * 2 ** -k
        M.rrect(c, x0 + pos, y, max(3, w - 6), 50, 6, BR if k % 2 == 0 else E.mix(COR, BR, 0.55), 1.0)
        pos += w
    M.rrect(c, x1 + 6, y - 260, 40, 310, 6, "#0A0820", 1.0)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Soma", "infinita", "da PG")


def d(c):  # o macete: a fórmula
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "soma infinita", 84, 330, 140, "i", BR)
    E.escreve(c, "numa conta", 76, 520, 190, "g", BR)
    E.formula(c, "S = f{a₁}{1 − q}", 84, 880, 170, "g", BR)
    E.escreve(c, "−1 < q < 1", 900, 860, 110, "g", AM)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_infinitos_passos", a), ("capa_B_soma_infinita", b), ("capa_C_numa_conta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
