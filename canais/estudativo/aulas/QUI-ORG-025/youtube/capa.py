"""Capas da QUI-ORG-025 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "roteiro"))
import skia
import editorial as E
import quimica as Q
import motor as M
import visual as V  # as peças de estrutura da aula, desenhadas paradas (t0 = None)
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
CLARO = E.mix(COR, BR, 0.5)


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def claro(c):
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)


def a(c):  # o gancho: a sacolinha é uma molécula
    claro(c)
    E.escreve(c, "1 fio de sacola", 84, 380, 150, "g", BR)
    E.escreve(c, "= 1 molécula", 84, 570, 170, "g", AMARELO)
    E.escreve(c, "feita de milhares de etenos", 84, 760, 96, "i", BR)
    V.polimeriza(c, 0, None, -99, 1480, 900, 3, ("H", "H", "H", "H"), 95, 52, escuro=True)
    V.sacola(c, 1560, 430, 300)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Polímeros", "de adição", "do zero")


def d(c):  # o macete: devolva a dupla
    escuro(c)
    E.escreve(c, "achou o polímero?", 84, 340, 110, "i", BR)
    E.escreve(c, "devolva a dupla", 84, 540, 160, "g", AMARELO)
    w = Q.formula(c, "[–CH2–CHCl–]", 84, 780, 100, BR, escuro=True)
    E.escreve(c, "n", 84 + w + 6, 810, 60, "g", BR)
    Q.formula(c, "→ CH2=CHCl", 84, 940, 100, AMARELO, cores={})


CAPAS = (("capa_A_sacola_uma_molecula", a), ("capa_B_polimeros_de_adicao", b), ("capa_C_devolva_a_dupla", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
