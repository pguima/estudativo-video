"""Capas do MAT-MED-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 750 mL não são 7,5 L
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "750 mL =", 84, 440, 190, "g", BR)
    E.escreve(c, "7,5 L", 1020, 440, 190, "g", BR)
    E.risco(c, 1000, 480, 1520, 300, 9, 0, AMARELO, 30)
    E.escreve(c, "0,75 L", 1020, 680, 190, "g", AMARELO)
    E.escreve(c, "a garrafa não cresce", 84, 960, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Massa e", "capacidade", "a mesma escada")


def d(c):  # o atalho: pule de mil em mil
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "pule de", 84, 340, 140, "i", BR)
    E.escreve(c, "mil em mil", 84, 540, 200, "g", BR)
    xs = (200, 640, 1080, 1520)
    for x, u in zip(xs, ("t", "kg", "g", "mg")):
        E.centro(c, u, x, 900, 150, "g", BR)
    for k in range(3):
        x0, x1 = xs[k] + 100, xs[k + 1] - 110
        path = skia.Path(); path.moveTo(x0, 800); path.quadTo((x0 + x1) / 2, 660, x1, 800)
        c.drawPath(path, M.paint(AMARELO, 1.0, stroke=10, cap_round=True))
        E.pilula(c, "× 1.000", (x0 + x1) / 2, 700, 46, "g", fundo=AMARELO, cor="#07070F")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_garrafa_nao_cresce", a), ("capa_B_massa_e_capacidade", b), ("capa_C_mil_em_mil", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
