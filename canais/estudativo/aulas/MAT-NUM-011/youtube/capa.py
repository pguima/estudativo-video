"""Capas do MAT-NUM-011 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: viu "mais" e somou
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "viu \"mais\" e somou?", 84, 390, 170, "g", BR)
    E.escreve(c, "30 + 5", 84, 660, 220, "g", BR)
    E.risco(c, 60, 700, 780, 480, 9, 0, AMARELO, 34)
    E.escreve(c, "30 − 5", 900, 660, 220, "g", AMARELO)
    E.escreve(c, "a palavra engana", 84, 900, 150, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Qual conta", "o problema", "pede?")


def d(c):  # o macete: números pequenos
    escuro(c)
    E.escreve(c, "não sabe a conta?", 84, 350, 150, "i", BR)
    E.escreve(c, "troque por", 76, 545, 170, "g", BR)
    E.escreve(c, "números pequenos", 76, 720, 150, "g", AMARELO)
    E.escreve(c, "pense em 10 ÷ 2", 84, 950, 170, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_viu_mais_e_somou", a), ("capa_B_qual_conta", b), ("capa_C_numeros_pequenos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
