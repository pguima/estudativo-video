"""Capas do MAT-PLN-004 (1280x720). Uso: python capa.py"""
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



def a(c):  # o gancho: uma raiz dá todas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "x^3 − 2x^2 − 5x + 6 = 0", 84, 380, 130, cor=BR)
    E.escreve(c, "se 1 é raiz...", 84, 580, 130, "i", BR)
    for k, s_ in enumerate(("1", "3", "−2")):
        E.bola(c, 300 + 330 * k, 800, 130, AMARELO)
        E.centro(c, s_, 300 + 330 * k, 850, 140, "g", COR)
    E.escreve(c, "todas as raízes", 1150, 830, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Raízes e", "fatoração", "baixar o grau")


def d(c):  # o atalho: divisores do termo independente
    palco(c)
    E.escreve(c, "ninguém deu a raiz?", 84, 330, 120, "i", BR)
    E.escreve(c, "procure nos divisores", 84, 520, 120, "g", AMARELO)
    E.escreve(c, "do termo independente", 84, 670, 120, "g", AMARELO)
    E.formula(c, "6:  ±1  ±2  ±3  ±6", 84, 900, 130, cor=BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_todas_as_raizes", a), ("capa_B_raizes_fatoracao", b), ("capa_C_divisores", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
