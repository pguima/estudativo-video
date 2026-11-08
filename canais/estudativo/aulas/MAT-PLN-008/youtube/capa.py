"""Capas do MAT-PLN-008 (1280x720). Uso: python capa.py"""
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



def a(c):  # o gancho: delta negativo tem resposta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "Δ = −36", 84, 420, 170, cor=BR)
    E.escreve(c, "e mesmo assim:", 84, 610, 120, "i", BR)
    E.formula(c, "x = 2 ± 3i", 84, 860, 220, cor=AMARELO)
    E.bola(c, 1580, 470, 200, AMARELO)
    E.centro(c, "i", 1580, 560, 260, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Delta", "negativo", "e o número i")


def d(c):  # o atalho: complexo × conjugado
    palco(c)
    E.escreve(c, "complexo × conjugado", 84, 330, 120, "i", BR)
    E.formula(c, "(a + bi)(a − bi)", 84, 560, 150, cor=BR)
    E.formula(c, "= a^2 + b^2", 84, 780, 190, cor=AMARELO)
    E.formula(c, "(2 + 3i)(2 − 3i) = 13", 84, 960, 100, cor="#C9C3FF")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_delta_negativo", a), ("capa_B_numero_i", b), ("capa_C_conjugado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
