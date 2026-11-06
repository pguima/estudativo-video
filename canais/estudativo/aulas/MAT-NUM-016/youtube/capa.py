"""Capas do MAT-NUM-016 (1280x720). Uso: python capa.py"""
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
CLARO = E.mix(COR, BR, 0.5)


def fundo_escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: a armadilha
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 − (−5)", 84, 500, 330, "g", BR)
    E.escreve(c, "= ?", 1340, 500, 330, "g", AMARELO)
    E.escreve(c, "não é −2", 84, 860, 300, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Somar e", "subtrair", "inteiros")


def d(c):  # o atalho: entradas e saídas
    fundo_escuro(c)
    E.escreve(c, "o atalho", 84, 340, 150, "i", BR)
    E.escreve(c, "entradas", 80, 570, 240, "g", BR)
    E.escreve(c, "e saídas", 84, 780, 240, "g", BR)
    E.escreve(c, "5 − 8 + 3 − 2 = −2", 84, 975, 130, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_tres_menos_menos_cinco", a), ("capa_B_somar_subtrair_inteiros", b), ("capa_C_entradas_saidas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
