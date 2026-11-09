"""Capas do FIS-ELE-012 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def zigue(c, x, y0, y1, cor, w=10):
    """resistor vertical em zigue-zague de y0 a y1"""
    h = y1 - y0
    pts = [(x, y0), (x, y0 + h * 0.25)] + [(x + (34 if k % 2 else -34), y0 + h * (0.25 + 0.5 * k / 8)) for k in range(1, 8)] + [(x, y0 + h * 0.75), (x, y1)]
    for A, B in zip(pts, pts[1:]):
        M.line(c, *A, *B, cor, 1.0, w)


def a(c):  # o gancho: mais um resistor, menos resistência
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "mais um resistor,", 84, 330, 120, "i", BR)
    E.escreve(c, "MENOS", 84, 530, 200, "g", BR)
    E.escreve(c, "resistência", 84, 680, 130, "g", BR)
    y0, y1 = 300, 800
    M.line(c, 1180, y0, 1780, y0, BR, 1.0, 10)
    M.line(c, 1180, y1, 1780, y1, BR, 1.0, 10)
    for x in (1300, 1660):
        zigue(c, x, y0, y1, BR)
        c.drawCircle(x, y0, 16, M.paint(BR)); c.drawCircle(x, y1, 16, M.paint(BR))
    for x in (1300, 1660):
        E.centro(c, "6 Ω", x - 110, 580, 64, "g", BR)
    E.bola(c, 1480, 960, 95, BR)
    E.centro(c, "3 Ω", 1480, 990, 72, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Resistores", "em paralelo", "do zero")


def d(c):  # o macete: produto pela soma
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "paralelo em 1 linha:", 84, 330, 120, "i", BR)
    E.escreve(c, "produto pela soma", 84, 520, 150, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "f{3 × 6}{3 + 6} = f{18}{9} = 2 Ω", 84, 830, 150, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mais_resistor_menos_resistencia", a), ("capa_B_resistores_em_paralelo", b), ("capa_C_produto_pela_soma", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
