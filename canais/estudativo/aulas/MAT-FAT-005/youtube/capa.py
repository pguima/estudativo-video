"""Capas do MAT-FAT-005 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 1/√2 = √2/2
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    w = fra(c, "1", "r{2}", 230, 560, 200, BR)
    E.formula(c, "=", 230 + w / 2 + 30, 620, 200, cor=BR)
    fra(c, "r{2}", "2", 230 + w / 2 + 330, 560, 200, AMARELO)
    E.escreve(c, "tire a raiz de baixo", 84, 1000, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Racionalizar", "sem medo", "raiz e conjugado")


def d(c):  # o atalho: o de baixo final antes da conta
    palco(c)
    E.escreve(c, "o atalho do conjugado", 84, 330, 110, "i", BR)
    w = fra(c, "2", "r{3} − 1", 250, 620, 150, BR)
    E.formula(c, "= r{3} + 1", 250 + w / 2 + 40, 680, 170, cor=AMARELO)
    E.escreve(c, "embaixo: 3 − 1 = 2", 84, 1000, 90, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_raiz_de_baixo", a), ("capa_B_racionalizar", b), ("capa_C_conjugado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
