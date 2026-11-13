"""Capas da QUI-ORG-023 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: mesmo óleo, sabão ou biodiesel
    claro(c)
    E.escreve(c, "óleo vira", 84, 380, 170, "g", BR)
    E.escreve(c, "sabão", 84, 580, 190, "g", AMARELO)
    E.escreve(c, "ou biodiesel", 84, 760, 140, "g", BR)
    c.save(); c.translate(1560 - 0.82 * 1050, 540 - 0.82 * 560); c.scale(0.82, 0.82)
    V.trigli(c, 0, None, 1380, 560, 0.0, escuro=True)
    c.restore()


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Saponificação", "e biodiesel", "do zero")


def d(c):  # o macete: o que entra decide
    escuro(c)
    E.escreve(c, "o que entra", 84, 340, 140, "g", BR)
    E.escreve(c, "decide o que sai", 84, 500, 120, "g", AMARELO)
    for i, s in enumerate(("base → sabão", "álcool → biodiesel", "água → ácido")):
        E.escreve(c, s, 84, 680 + i * 110, 84, "g", CLARO)


CAPAS = (("capa_A_oleo_sabao_biodiesel", a), ("capa_B_saponificacao_biodiesel", b), ("capa_C_o_que_entra_decide", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
