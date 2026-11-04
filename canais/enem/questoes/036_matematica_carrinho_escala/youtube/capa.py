"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 036 (ENEM 2025, questão 150), com o visual da aula.
python capa.py    -> youtube/capa_A_qual_andou_mais.jpg, capa_B_o_desenho_engana.jpg"""
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
    if qual == "a":   # as cinco telas e a pergunta: não entrega a resposta
        V.glow_text(c, "QUAL ANDOU", 960, 270, 130, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "MAIS?", 960, 420, 130, "black", V.MNT, 1, glow=0.18)
        V.linha_telas(c, 1, 0, y=560, w=330, x0=91, gap=22)
        V.pill(c, "cada tela, uma escala", 960, 1000, 44, V.AMB, V.BG0, 1)
    else:   # a armadilha: o maior desenho é só 9 m
        V.tela(c, 0, 120, 240, 780, 1, foco=0)
        V.glow_text(c, "O MAIOR", 1430, 330, 120, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "DESENHO", 1430, 470, 120, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "NÃO GANHA!", 1430, 620, 110, "black", V.RED, 1, glow=0.16)
        V.pill(c, "9 cm no desenho = só 9 m", 1430, 800, 44, V.AMB, V.BG0, 1)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_qual_andou_mais.jpg", "capa_B_o_desenho_engana.jpg")):
        capa(V, qual, pasta / nome)
