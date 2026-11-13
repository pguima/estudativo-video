"""Capas da QUI-ORG-028 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: monômero, tipo e destino
    claro(c)
    E.escreve(c, "4 questões", 84, 380, 170, "g", BR)
    E.escreve(c, "de polímeros", 84, 570, 160, "g", AMARELO)
    E.escreve(c, "monômero, tipo e reciclagem", 84, 760, 96, "i", BR)
    V.tri_recicla(c, 1560, 520, 200, 1, 1.0, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Polímeros", "praticando", "4 situações")


def d(c):  # o macete: olhe a unidade
    escuro(c)
    E.escreve(c, "olhe a unidade", 84, 340, 130, "g", BR)
    E.escreve(c, "que se repete", 84, 510, 140, "g", AMARELO)
    E.escreve(c, "só carbono: adição", 84, 690, 80, "g", CLARO)
    E.escreve(c, "O ou N ligando: condensação", 84, 800, 80, "g", CLARO)


CAPAS = (("capa_A_quatro_questoes", a), ("capa_B_polimeros_praticando", b), ("capa_C_olhe_a_unidade", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
