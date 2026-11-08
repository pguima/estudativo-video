"""Capas do MAT-EQU-005 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: 3x · 2x não é 5x nem 6x
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "3x × 2x =", 84, 420, 230, cor=BR)
    for x, s in ((84, "5x"), (520, "6x")):
        E.formula(c, s, x, 740, 200, cor=BR)
        E.risco(c, x - 20, 760, x + 300, 590, 9, 0, BR, 22)
    E.formula(c, "6x^2", 1000, 760, 250, cor=AMARELO)
    E.escreve(c, "quanto dá?", 84, 980, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Letra", "vezes letra", "e o chuveirinho")


def d(c):  # o atalho: (x + 2)(x + 3) direto
    palco(c)
    E.escreve(c, "o atalho", 84, 330, 150, "i", BR)
    E.formula(c, "(x + 2)(x + 3)", 84, 580, 190, cor=BR)
    E.formula(c, "= x^2 + 5x + 6", 84, 840, 190, cor=AMARELO)
    E.escreve(c, "soma no meio, multiplica no fim", 84, 1000, 80, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_3x_vezes_2x", a), ("capa_B_letra_vezes_letra", b), ("capa_C_atalho_dois_parenteses", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
