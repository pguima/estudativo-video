"""Capas da QUI-ORG-016 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a talidomida e a gêmea do espelho
    claro(c)
    E.escreve(c, "talidomida", 84, 400, 170, "g", BR)
    E.escreve(c, "a gêmea", 84, 620, 170, "g", AMARELO)
    E.escreve(c, "do espelho", 84, 800, 140, "i", BR)
    V.tetra(c, 0, None, 1250, 720, 135, V.GENERICO)
    V.espelho(c, 1480, 470, 970)
    V.tetra(c, 0, None, 1710, 720, 135, V.GENERICO, espelha=True)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Carbono", "quiral", "do zero")


def d(c):  # o macete: 2 elevado a n
    escuro(c)
    E.escreve(c, "conte os isômeros", 84, 360, 120, "i", BR)
    E.formula(c, "2^n", 84, 700, 330, "g", AMARELO)
    E.escreve(c, "n = carbonos quirais", 84, 900, 90, "g", CLARO)
    V.tetra(c, 0, None, 1450, 620, 190, V.LATICO, escuro=True)


CAPAS = (("capa_A_talidomida_espelho", a), ("capa_B_carbono_quiral", b), ("capa_C_dois_elevado_a_n", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
