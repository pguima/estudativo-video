"""Capas da QUI-ORG-020 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: plástico de cana
    claro(c)
    E.escreve(c, "plástico", 84, 400, 190, "g", BR)
    E.escreve(c, "de cana?", 84, 610, 190, "g", AMARELO)
    E.escreve(c, "o etanol perde água", 84, 800, 110, "i", BR)
    Q.formula(c, "CH3–CH2–OH", 1480, 380, 96, BR, 1, "center", cores={"O": AMARELO}, escuro=True)
    Q.formula(c, "→ CH2=CH2", 1480, 560, 96, BR, 1, "center", escuro=True)
    Q.formula(c, "+ H2O", 1480, 740, 96, AMARELO, 1, "center")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Reações de", "eliminação", "do zero")


def d(c):  # o macete: risque o OH e um H vizinho
    escuro(c)
    E.escreve(c, "risque o OH", 84, 360, 140, "g", BR)
    E.escreve(c, "e um H vizinho", 84, 540, 140, "g", AMARELO)
    E.escreve(c, "e feche a dupla", 84, 720, 100, "i", CLARO)
    Q.formula(c, "CH2=CH2 + H2O", 1440, 900, 100, BR, 1, "center", cores={"O": AMARELO}, escuro=True)


CAPAS = (("capa_A_plastico_de_cana", a), ("capa_B_reacoes_de_eliminacao", b), ("capa_C_risque_oh_e_h", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
