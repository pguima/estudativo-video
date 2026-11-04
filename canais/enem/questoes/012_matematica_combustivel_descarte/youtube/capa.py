"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 012 (ENEM 2025, questão 138), com o visual da aula.
python capa.py    -> youtube/capa_A_quanto.jpg, capa_B_pegadinha.jpg"""
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
    if qual == "a":
        V.caminhao(c, 590, 760, 1.3, 1, 0.68, 0.0)
        V.glow_text(c, "?", 505, 570, 200, "black", V.CYA, 1, glow=0.14)
        V.descarte(c, 590, 760, 1.3, 1, 0.5, 0.0)
        V.glow_text(c, "QUANTO", 1380, 320, 150, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "ENVIAR?", 1380, 480, 150, "black", V.CYA, 1, glow=0.18)
        V.glow_text(c, "chegou 9.900 de 10.200", 1380, 650, 62, "black", V.AMB, 1, glow=0.12)
        V.pill(c, "QUESTÃO 138", 1380, 830, 50, V.MNT, V.BG0, 1)
    else:
        V.caminhao(c, 600, 760, 1.25, 1, 0.68, 0.0)
        V.descarte(c, 600, 760, 1.25, 1, 0.5, 0.0)
        V.glow_text(c, "O DESCARTE DOBRA?", 1330, 300, 92, "black", V.WHITE, 1, glow=0.12)
        pos = V.eq(c, [("2 × 10.200", V.AMB), (" = ", V.WHITE), ("20.400", V.RED)], 490, 1, 92, cx=1330, maxw=820)
        V.strike(c, pos[0][0], pos[-1][1], 490, 1, 1)
        V.pill(c, "A PEGADINHA DO ENEM", 1330, 680, 56, V.RED, V.BG0, 1)
        V.glow_text(c, "parte FIXA não dobra", 1330, 860, 78, "black", V.CYA, 1, glow=0.16)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_quanto.jpg", "capa_B_pegadinha.jpg")):
        capa(V, qual, pasta / nome)
