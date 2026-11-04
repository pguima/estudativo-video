"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 018 (ENEM 2025, questão 141), com o visual da aula.
python capa.py    -> youtube/capa_A_quantas_cores.jpg, capa_B_hexagonos.jpg"""
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
        V.solido(c, 500, 560, 250, 0, 1, yaw=0.62, explode=0.5)   # sem pintar: não entrega a resposta
        V.glow_text(c, "QUANTAS", 1380, 330, 130, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "CORES?", 1380, 490, 150, "black", V.CYA, 1, glow=0.18)
        V.glow_text(c, "prisma + tronco de pirâmide", 1380, 650, 52, "black", V.AMB, 1, glow=0.12)
        V.pill(c, "QUESTÃO 141", 1380, 830, 50, V.MNT, V.BG0, 1)
    else:
        V.hexagono(c, 380, 560, 210, V.AMB, 0.3)
        V.hexagono(c, 380, 560, 210, V.AMB, 1, stroke=True)
        V.hexagono(c, 760, 600, 120, V.ROSA, 0.3)
        V.hexagono(c, 760, 600, 120, V.ROSA, 1, stroke=True)
        V.glow_text(c, "MESMA COR?", 1380, 330, 120, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "NÃO!", 1380, 490, 150, "black", V.RED, 1, glow=0.16)
        V.pill(c, "A PEGADINHA DO ENEM", 1380, 680, 52, V.RED, V.BG0, 1)
        V.glow_text(c, "mesma forma ≠ mesmo tamanho", 1380, 840, 54, "black", V.CYA, 1, glow=0.16)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_quantas_cores.jpg", "capa_B_hexagonos.jpg")):
        capa(V, qual, pasta / nome)
