"""Capas da QUI-ORG-024 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: fábrica e corpo humano
    claro(c)
    E.escreve(c, "5 reações", 84, 400, 180, "g", BR)
    E.escreve(c, "da fábrica", 84, 590, 150, "g", AMARELO)
    E.escreve(c, "e do seu corpo", 84, 770, 120, "i", BR)
    V.figado(c, 1520, 420, 200)
    V.benzeno_sub(c, 0, None, 1420, 800, 110, 1.0, escuro=True)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Reações", "praticando", "5 situações")


def d(c):  # o macete: compare antes e depois
    escuro(c)
    E.escreve(c, "compare o antes", 84, 340, 120, "g", BR)
    E.escreve(c, "e o depois", 84, 500, 140, "g", AMARELO)
    for i, s in enumerate(("sumiu dupla → adição", "apareceu dupla → eliminação", "trocou H → substituição")):
        E.escreve(c, s, 84, 680 + i * 110, 76, "g", CLARO)


CAPAS = (("capa_A_fabrica_e_corpo", a), ("capa_B_reacoes_praticando", b), ("capa_C_antes_e_depois", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
