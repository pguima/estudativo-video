"""Capas da QUI-ORG-017 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: remédio e alimento com isomeria
    claro(c)
    E.escreve(c, "azeite ou", 84, 380, 170, "g", BR)
    E.escreve(c, "gordura trans?", 84, 570, 150, "g", AMARELO)
    E.escreve(c, "5 questões de isomeria", 84, 780, 100, "i", BR)
    V.graxo(c, 0, None, 1580, 330, 62, True, n=5, escuro=True, cor_dupla=AMARELO)
    V.graxo(c, 0, None, 1580, 800, 62, False, n=5, escuro=True, cor_dupla=AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Isomeria", "praticando", "5 situações")


def d(c):  # o macete: 3 perguntas
    escuro(c)
    E.escreve(c, "isomeria em", 84, 330, 110, "i", BR)
    E.escreve(c, "3 perguntas", 84, 520, 190, "g", AMARELO)
    for i, s in enumerate(("mesma fórmula?", "ordem diferente?", "só no espaço?")):
        E.escreve(c, f"{i + 1}  {s}", 84, 700 + i * 110, 80, "g", CLARO)
    V.alceno(c, 0, None, 1500, 700, ("H3C", "H", "CH3", "H"), 150, 84, escuro=True)


CAPAS = (("capa_A_azeite_gordura_trans", a), ("capa_B_isomeria_praticando", b), ("capa_C_tres_perguntas", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
