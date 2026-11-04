"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 024 (ENEM 2025, questão 144), com o visual da aula.
python capa.py    -> youtube/capa_A_para_onde_vai.jpg, capa_B_as_sombras.jpg"""
import importlib.util, sys
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJ.parents[3] / "_ferramentas"))
import idioma  # noqa: E402
import skia  # noqa: E402


def visual():
    idioma.definir("pt")
    spec = importlib.util.spec_from_file_location("visual_pt", PROJ / "roteiro" / "visual.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def capa(V, qual, out):
    s = skia.Surface(V.W, V.H); c = s.getCanvas()
    c.drawImage(V.matematica._bg(), 0, 0)
    marca = "ESTUDATIVO · QUESTÃO DO ENEM 2025"
    w = V.text_w(marca, "extrabold", 30) + 36
    V.pill(c, marca, 70 + w / 2, 90, 30, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":   # o cubo no começo, com as setas: não entrega a resposta
        V.cena3d(c, 1)
        V.sombras(c, V.INI, 1, V.CYA)
        V.cubo(c, V.INI, 1, V.AMB, glow=0.6)
        x, y, z = V.INI
        V.seta3d(c, (x + 0.5, y + 1.2, z + 0.5), (x + 0.5, y + 4.0, z + 0.5), 1, V.CYA, "+5")
        V.seta3d(c, (x + 0.5, y + 0.5, z - 0.2), (x + 0.5, y + 0.5, z - 2.6), 1, V.AMB, "−4")
        V.glow_text(c, "PARA ONDE", 1390, 330, 110, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "VAI O CUBO?", 1390, 470, 110, "black", V.CYA, 1, glow=0.18)
        V.glow_text(c, "coordenadas e projeções", 1390, 630, 56, "black", V.AMB, 1, glow=0.12)
        V.pill(c, "QUESTÃO 144", 1390, 810, 50, V.MNT, V.BG0, 1)
    else:
        V.cena3d(c, 1)
        V.sombras(c, V.FIM, 1, V.MNT)
        V.cubo(c, V.FIM, 1, V.MNT, glow=0.6)
        V.glow_text(c, "AS 3 SOMBRAS", 1390, 330, 104, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "DO CUBO", 1390, 470, 110, "black", V.MNT, 1, glow=0.18)
        V.pill(c, "PROJEÇÃO ORTOGONAL", 1390, 650, 50, V.CYA, V.BG0, 1)
        V.glow_text(c, "geometria espacial no ENEM", 1390, 820, 52, "black", V.AMB, 1, glow=0.12)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_para_onde_vai.jpg", "capa_B_as_sombras.jpg")):
        capa(V, qual, pasta / nome)
