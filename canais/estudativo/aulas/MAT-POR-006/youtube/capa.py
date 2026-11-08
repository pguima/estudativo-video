"""Capas do MAT-POR-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: R$ 96 com 20% de desconto não custava R$ 115,20
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "paguei R$ 96", 84, 400, 170, "g", BR)
    E.escreve(c, "com 20% de desconto", 88, 540, 110, "i", BR)
    E.escreve(c, "R$ 115,20?", 84, 790, 200, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 820, 1150, 640, 9, 0, AMARELO, 30)
    E.escreve(c, "custava quanto?", 84, 990, 120, "i", BR)
    E.centro(c, "R$ 120", 1530, 810, 150, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Preço", "de antes", "do desconto")


def d(c):  # o atalho: 20% é um quinto
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.escreve(c, "20% =", 76, 590, 210, "g", BR)
    E.fracao(c, 1, 5, 860, 520, 170, BR)
    E.escreve(c, "96 ÷ 4 × 5", 84, 870, 140, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "= 120", 760, 870, 140, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_115_ou_120", a), ("capa_B_preco_de_antes", b), ("capa_C_um_quinto", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
