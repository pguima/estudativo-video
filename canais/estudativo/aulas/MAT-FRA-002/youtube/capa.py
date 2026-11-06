"""Capas do MAT-FRA-002 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
CLARO = E.mix(COR, BR, 0.5)
AMARELO = "#FFD500"


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: o salário menor que a parte
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.fracao(c, 2, 5, 230, 500, 280, BR)
    E.escreve(c, "=", 430, 590, 220, "g", BR)
    E.escreve(c, "R$ 600", 620, 590, 280, "g", AMARELO)
    E.escreve(c, "qual é o salário?", 84, 1000, 170, "i", BR)
    E.escreve(c, "R$ 240", 1240, 850, 170, "g", BR)
    E.risco(c, 1220, 880, 1860, 730, 9, 0, AMARELO, 26)


def b(c):  # o método
    E.capa_modelo(c, "Matemática", "Calcular", "frações", "de um número")


def d(c):  # o atalho: tudo, menos o pedaço que falta
    palco(c)
    E.escreve(c, "tire o pedaço", 84, 350, 150, "i", BR)
    E.escreve(c, "que falta", 76, 570, 240, "g", BR)
    y = 790
    E.fracao(c, 4, 5, 230, y, 170, BR)
    E.escreve(c, "de 400 =", 340, y + 54, 130, "i", BR)
    E.escreve(c, "400 − 80", 830, y + 54, 170, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_salario", a), ("capa_B_calcular_fracao", b), ("capa_C_pedaco_que_falta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
