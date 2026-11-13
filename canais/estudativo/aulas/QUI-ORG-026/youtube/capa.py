"""Capas da QUI-ORG-026 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: PET e náilon soltam água
    claro(c)
    E.escreve(c, "PET e náilon", 84, 380, 160, "g", BR)
    E.escreve(c, "soltam água", 84, 580, 180, "g", AMARELO)
    E.escreve(c, "a cada ligação da cadeia", 84, 770, 100, "i", BR)
    V.garrafa_pet(c, 1560, 960, 640)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Poliéster", "e poliamida", "condensação do zero")


def d(c):  # o macete: procure COO ou CONH
    escuro(c)
    E.escreve(c, "achou COO ou CO–NH", 84, 360, 110, "g", BR)
    E.escreve(c, "repetido?", 84, 530, 150, "g", AMARELO)
    E.escreve(c, "condensação: saiu água", 84, 700, 90, "g", CLARO)
    w = Q.formula(c, "[–CO–(CH2)4–CO–NH–(CH2)6–NH–]", 84, 900, 70, BR, escuro=True)
    E.escreve(c, "n", 84 + w + 6, 920, 44, "g", BR)


CAPAS = (("capa_A_pet_e_nailon", a), ("capa_B_polimeros_condensacao", b), ("capa_C_coo_ou_conh", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
