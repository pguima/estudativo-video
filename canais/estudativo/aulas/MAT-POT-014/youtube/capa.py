"""Capas do MAT-POT-014 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 5.000 fica mais perto de quem?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5.000", 84, 470, 290, "g", AMARELO)
    E.escreve(c, "mais perto de", 84, 640, 130, "i", BR)
    E.escreve(c, "1.000", 84, 860, 170, "g", BR)
    E.escreve(c, "ou", 640, 860, 140, "i", BR)
    E.escreve(c, "10.000?", 840, 860, 170, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Ordem de", "grandeza", "do zero")


def d(c):  # o macete: o ponto de virada
    escuro(c)
    E.escreve(c, "o ponto de virada", 84, 380, 150, "i", BR)
    E.formula(c, "r{10}", 84, 680, 240, "g", BR)
    E.formula(c, "≈ 3,16", 640, 680, 240, "g", AMARELO)
    E.escreve(c, "passou, o expoente sobe", 84, 930, 130, "g", BR)


NOMES = (("capa_A_mais_perto_de_quem", a), ("capa_B_ordem_de_grandeza", b), ("capa_C_ponto_de_virada", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in NOMES:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()

