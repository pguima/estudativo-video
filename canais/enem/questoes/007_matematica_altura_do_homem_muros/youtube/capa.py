"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 007, com o visual da aula (design system de matemática).
python capa.py    -> youtube/capa_A_altura_do_homem.jpg, capa_B_sem_a_distancia.jpg"""
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
    marca = "ESTUDATIVO · QUESTÃO"
    w = V.text_w(marca, "extrabold", 30) + 36
    V.pill(c, marca, 70 + w / 2, 90, 30, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":
        c.save(); c.translate(530, 620); c.scale(1.15, 1.15); c.translate(-520, -600)
        V.cena(c, 1, 0, rot_h="?", hl_homem=1, hl_muros=0.4)
        c.restore()
        V.glow_text(c, "QUAL A", 1450, 380, 140, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "ALTURA?", 1450, 560, 170, "black", V.CYA, 1, glow=0.18)
        V.pill(c, "SEM A DISTÂNCIA!", 1450, 760, 54, V.AMB, V.BG0, 1)
    else:
        V.glow_text(c, "A DISTÂNCIA", 960, 240, 150, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "NÃO IMPORTA", 960, 410, 170, "black", V.AMB, 1, glow=0.18)
        c.save(); c.translate(960, 930); c.scale(1.25, 1.25); c.translate(-520, -780)
        V.cena(c, 1, 0, d=11, U=60, rot_h="h = ?", hl_homem=1)
        c.restore()
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_altura_do_homem.jpg", "capa_B_sem_a_distancia.jpg")):
        capa(V, qual, pasta / nome)
