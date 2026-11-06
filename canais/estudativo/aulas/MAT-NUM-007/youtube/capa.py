"""Capas do MAT-NUM-007 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: o vai um esquecido
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "47 × 6 =", 84, 460, 230, "g", BR)
    E.escreve(c, "242", 1090, 460, 280, "g", BR)
    E.risco(c, 1060, 500, 1680, 230, 9, 0, AMARELO, 34)
    E.escreve(c, "282", 1150, 760, 300, "g", AMARELO)
    E.escreve(c, "faltaram", 84, 680, 150, "i", BR)
    E.escreve(c, "R$ 40", 84, 860, 180, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Multiplicar", "por 10 e 100", "e por um algarismo")


def d(c):  # o macete: vezes 99
    escuro(c)
    E.escreve(c, "vezes 99?", 84, 350, 170, "i", BR)
    E.escreve(c, "faça vezes 100", 76, 545, 170, "g", BR)
    E.escreve(c, "e tire um", 76, 720, 170, "g", AMARELO)
    E.escreve(c, "99 × 6 = 594", 84, 950, 170, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_faltaram_40_reais", a), ("capa_B_multiplicar", b), ("capa_C_vezes_99", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
