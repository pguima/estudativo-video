"""Capas do MAT-RAZ-013 (1280x720). Uso: python capa.py"""
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


def pilha(c, cx, base, n, rotulo):
    for i in range(n):
        y = base - i * 74
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 150, y - 62, 300, 62), 31, 31)
        c.drawRRect(r, M.paint(BR))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 140, y - 54, 280, 46), 23, 23), M.paint(COR, 0.35, stroke=3))
        E.centro(c, "1.000", cx, y - 16, 40, "b", COR)
    E.centro(c, rotulo, cx, base + 110, 92, "g", BR)


def a(c):  # o gancho: metade para cada? não
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "lucro de R$ 1.200", 84, 380, 110, "i", BR)
    E.escreve(c, "600 e 600?", 76, 630, 190, "g", BR)
    E.risco(c, 60, 680, 1060, 470, 9, 0, AMARELO, 30)
    E.escreve(c, "quem pôs mais leva mais", 84, 900, 100, "i", BR)
    pilha(c, 1440, 760, 3, "3")
    pilha(c, 1750, 760, 5, "5")


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Repartir", "o lucro", "na proporção certa")


def d(c):  # o atalho: quanto a mais
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho do", 84, 360, 150, "i", BR)
    E.escreve(c, "quanto a mais?", 76, 590, 220, "g", BR)
    E.formula(c, "(5 − 4) × 700 = 700", 84, 860, 150, "g", E.mix(COR, BR, 0.6))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_metade_nao", a), ("capa_B_repartir_lucro", b), ("capa_C_quanto_a_mais", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
