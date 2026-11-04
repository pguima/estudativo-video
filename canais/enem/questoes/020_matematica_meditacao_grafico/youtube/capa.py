"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 020 (ENEM 2025, questão 142), com o visual da aula.
python capa.py    -> youtube/capa_A_o_que_acontece.jpg, capa_B_diminui_ou_constante.jpg"""
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
    g = (170, 900, 660, 560)
    if qual == "a":   # o gráfico sem pintar os trechos: não entrega a resposta
        V.grafico(c, 1, 0, 1.0, cores={"antes": (V.WHITE, 1, 0), "desce": (V.WHITE, 1, 0.3), "deitada": (V.WHITE, 1, 0)}, g=g)
        V.glow_text(c, "RESPIRAR", 1390, 330, 120, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "MEDITANDO", 1390, 480, 120, "black", V.CYA, 1, glow=0.18)
        V.glow_text(c, "o que o gráfico diz?", 1390, 640, 60, "black", V.AMB, 1, glow=0.12)
        V.pill(c, "QUESTÃO 142", 1390, 820, 50, V.MNT, V.BG0, 1)
    else:
        V.grafico(c, 1, 0, 1.0, cores={"antes": (V.INK2, 0.5, 0), "desce": (V.CYA, 1, 1), "deitada": (V.MNT, 1, 1)}, g=g)
        V.glow_text(c, "DIMINUI?", 1390, 330, 120, "black", V.CYA, 1, glow=0.16)
        V.glow_text(c, "CONSTANTE?", 1390, 480, 120, "black", V.MNT, 1, glow=0.16)
        V.pill(c, "OU PROPORCIONAL?", 1390, 650, 54, V.RED, V.BG0, 1)
        V.glow_text(c, "leitura de gráfico no ENEM", 1390, 820, 54, "black", V.AMB, 1, glow=0.12)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_o_que_acontece.jpg", "capa_B_diminui_ou_constante.jpg")):
        capa(V, qual, pasta / nome)
