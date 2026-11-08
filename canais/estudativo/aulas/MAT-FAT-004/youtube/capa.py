"""Capas do MAT-FAT-004 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def fra(c, cima, baixo, cx, y, size, cor):
    w = max(E.formula(None, cima, 0, 0, size, a=0), E.formula(None, baixo, 0, 0, size, a=0)) + size * 0.3
    E.formula(c, cima, cx, y - size * 0.32, size, cor=cor, align="center")
    b = size * 0.07
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y - b / 2, w, b), b / 2, b / 2), M.paint(cor))
    E.formula(c, baixo, cx, y + size * 0.98, size, cor=cor, align="center")
    return w


def a(c):  # o gancho: x + 3 disfarçado
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    w = fra(c, "x^2 − 9", "x − 3", 360, 560, 180, BR)
    E.formula(c, "= x + 3", 360 + w / 2 + 40, 620, 200, cor=AMARELO)
    E.escreve(c, "só disfarçado", 84, 1000, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Frações", "com letra", "simplificar sem erro")


def d(c):  # o atalho: troque o x por um número
    palco(c)
    E.escreve(c, "o atalho: troque x por 2", 84, 330, 110, "i", BR)
    w = fra(c, "x^2 − 9", "x − 3", 260, 620, 140, BR)
    E.formula(c, "→ 5", 260 + w / 2 + 40, 670, 150, cor=AMARELO)
    E.formula(c, "x + 3 → 5", 84, 990, 150, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_x_mais_3_disfarcado", a), ("capa_B_fracoes_com_letra", b), ("capa_C_troque_x_por_2", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
