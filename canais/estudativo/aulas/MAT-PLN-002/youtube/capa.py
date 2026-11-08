"""Capas do MAT-PLN-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o resto sem dividir
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "(x^2 + 3x + 5) ÷ (x − 1)", 84, 400, 150, cor=BR)
    E.escreve(c, "resto?", 84, 620, 150, "i", BR)
    E.formula(c, "P(1) = 9", 84, 850, 210, cor=AMARELO)
    E.bola(c, 1560, 640, 210, BR)
    E.centro(c, "3 s", 1560, 700, 170, "g", COR)
    E.escreve(c, "sem dividir nada", 84, 1010, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Dividir", "polinômios", "e achar o resto")


def d(c):  # o atalho: teorema do resto
    palco(c)
    E.escreve(c, "teorema do resto", 84, 330, 130, "i", BR)
    E.escreve(c, "na divisão por x − a,", 84, 520, 100, "i", "#C9C3FF")
    E.formula(c, "resto = P(a)", 84, 780, 230, cor=AMARELO)
    E.formula(c, "divisível  ↔  P(a) = 0", 84, 960, 100, cor=BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_resto_sem_dividir", a), ("capa_B_dividir_polinomios", b), ("capa_C_teorema_do_resto", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
