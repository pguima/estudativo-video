"""Capas do MAT-PLN-006 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)



def a(c):  # o gancho: soma e produto sem resolver
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "x^3 − 6x^2 + 11x − 6 = 0", 84, 380, 130, cor=BR)
    E.escreve(c, "sem resolver:", 84, 580, 120, "i", BR)
    for k, (rot, v) in enumerate((("soma", "6"), ("produto", "6"))):
        cx = 420 + 640 * k
        E.bola(c, cx, 820, 150, AMARELO)
        E.centro(c, v, cx, 875, 160, "g", COR)
        E.escreve(c, rot, cx + 180, 860, 100, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Relações", "de Girard", "soma e produto")


def d(c):  # o atalho: uma raiz + Girard
    palco(c)
    E.escreve(c, "1 raiz conhecida", 84, 330, 130, "g", AMARELO)
    E.escreve(c, "+ Girard", 84, 500, 130, "i", BR)
    E.escreve(c, "= as outras de cabeça", 84, 680, 120, "g", BR)
    E.formula(c, "soma 5, produto 6:  2 e 3", 84, 900, 110, cor="#C9C3FF")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sem_resolver", a), ("capa_B_girard", b), ("capa_C_uma_raiz", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
