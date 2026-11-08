"""Capas do MAT-FIN-014 (1280x720). Uso: python capa.py"""
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



def a(c):  # o gancho: a taxa maior engana
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "qual banco escolher?", 84, 340, 100, "i", BR)
    E.escreve(c, "11% com imposto", 84, 520, 120, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "9,5% sem imposto", 84, 680, 120, "g", BR)
    E.risco(c, 70, 540, 1010, 450, 9, 0, AMARELO, 26)
    E.escreve(c, "B ganha:", 84, 900, 150, "g", AMARELO)
    E.escreve(c, "R$ 950 contra R$ 935", 760, 900, 80, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando:", "5 propostas", "taxas, inflação e juros")


def d(c):  # o macete: compare pelo valor de verdade
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "antes de escolher, compare:", 84, 320, 100, "i", BR)
    E.escreve(c, "na mesma data", 84, 500, 130, "g", BR)
    E.escreve(c, "no mesmo prazo", 84, 660, 130, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "pelo valor de verdade", 84, 820, 130, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_banco", a), ("capa_B_praticando", b), ("capa_C_compare", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
