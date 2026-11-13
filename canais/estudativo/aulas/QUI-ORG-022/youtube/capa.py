"""Capas da QUI-ORG-022 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: abacaxi sem abacaxi
    claro(c)
    E.escreve(c, "cheiro de abacaxi", 84, 400, 140, "g", BR)
    E.escreve(c, "sem abacaxi", 84, 580, 170, "g", AMARELO)
    E.escreve(c, "ácido + álcool = éster", 84, 780, 100, "i", BR)
    V.abacaxi(c, 1560, 640, 300)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Esterificação", "e hidrólise", "do zero")


def d(c):  # o macete: nome do éster
    escuro(c)
    E.escreve(c, "o nome do éster", 84, 340, 110, "i", BR)
    E.escreve(c, "…ato de …ila", 84, 560, 180, "g", AMARELO)
    E.escreve(c, "ácido primeiro, álcool depois", 84, 740, 80, "g", CLARO)
    Q.formula(c, "CH3–COO–CH2–CH3", 84, 920, 90, BR, 1, cores={k: AMARELO for k in range(5)}, escuro=True)


CAPAS = (("capa_A_abacaxi_sem_abacaxi", a), ("capa_B_esterificacao_hidrolise", b), ("capa_C_ato_de_ila", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
