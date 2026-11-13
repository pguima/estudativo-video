"""Capas da QUI-ORG-018 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: óleo vira margarina
    claro(c)
    E.escreve(c, "óleo vira", 84, 400, 180, "g", BR)
    E.escreve(c, "margarina", 84, 610, 200, "g", AMARELO)
    E.escreve(c, "com hidrogênio", 84, 800, 120, "i", BR)
    V.adicao(c, 99, 0, 0, 0, 1500, 640, 135, 76, ("H", "H", "H", "H"), ("H", "H"), escuro=True, cores={6: AMARELO, 7: AMARELO})


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Reações", "de adição", "do zero")


def d(c):  # o macete: quem tem mais H ganha mais H
    escuro(c)
    E.escreve(c, "quem tem mais H", 84, 360, 130, "g", BR)
    E.escreve(c, "ganha mais H", 84, 540, 150, "g", AMARELO)
    E.escreve(c, "Markovnikov sem decorar", 84, 720, 90, "i", CLARO)
    V.adicao(c, 99, 0, 0, 0, 1520, 700, 125, 70, V.PROP, ("H", "Br"), escuro=True, dx={3: 0.25}, cores={6: AMARELO, 7: AMARELO})


CAPAS = (("capa_A_oleo_vira_margarina", a), ("capa_B_reacoes_de_adicao", b), ("capa_C_quem_tem_mais_h", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
