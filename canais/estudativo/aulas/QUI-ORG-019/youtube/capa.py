"""Capas da QUI-ORG-019 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: sai um, entra outro
    claro(c)
    E.escreve(c, "sai o H,", 84, 400, 190, "g", BR)
    E.escreve(c, "entra o Cl", 84, 610, 190, "g", AMARELO)
    E.escreve(c, "a troca no alcano", 84, 800, 110, "i", BR)
    Q.formula(c, "CH4 + Cl2", 1440, 400, 96, BR, 1, "center", cores={"Cl": AMARELO})
    Q.formula(c, "→ CH3Cl + HCl", 1440, 580, 90, BR, 1, "center", cores={"Cl": AMARELO})


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Reações de", "substituição", "do zero")


def d(c):  # o macete: terciário > secundário > primário
    escuro(c)
    E.escreve(c, "qual H sai primeiro?", 84, 340, 110, "i", BR)
    E.escreve(c, "terciário", 84, 540, 160, "g", AMARELO)
    E.escreve(c, "> secundário > primário", 84, 700, 90, "g", CLARO)
    V.benzeno_sub(c, 0, None, 1400, 880, 120, 1.0, escuro=True)


CAPAS = (("capa_A_sai_h_entra_cl", a), ("capa_B_reacoes_de_substituicao", b), ("capa_C_terciario_primeiro", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
