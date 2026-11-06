"""Capas do MAT-NUM-009 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o zero que some do resultado
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "612 ÷ 3 =", 84, 460, 220, "g", BR)
    E.escreve(c, "24", 1240, 460, 280, "g", BR)
    E.risco(c, 1210, 500, 1680, 240, 9, 0, AMARELO, 34)
    E.escreve(c, "204", 1190, 760, 290, "g", AMARELO)
    E.escreve(c, "não pule", 84, 680, 150, "i", BR)
    E.escreve(c, "o zero", 84, 860, 180, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Dividir", "com resto", "por um algarismo")


def d(c):  # o macete: vezes 5
    escuro(c)
    E.escreve(c, "vezes 5?", 84, 350, 170, "i", BR)
    E.escreve(c, "faça vezes 10", 76, 545, 170, "g", BR)
    E.escreve(c, "e tire a metade", 76, 720, 170, "g", AMARELO)
    E.escreve(c, "46 × 5 = 230", 84, 950, 170, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_pule_o_zero", a), ("capa_B_dividir_com_resto", b), ("capa_C_vezes_5", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
