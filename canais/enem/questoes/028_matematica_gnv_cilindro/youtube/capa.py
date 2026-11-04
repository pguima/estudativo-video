"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 028 (ENEM 2025, questão 146), com o visual da aula.
python capa.py    -> youtube/capa_A_qual_cilindro.jpg, capa_B_arredonde_para_cima.jpg"""
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
    if qual == "a":   # os cinco cilindros e a pergunta: não entrega a resposta
        V.cilindros(c, 1, 0, None, yb=900, kh=26, letras=False)
        V.glow_text(c, "QUAL", 1390, 300, 120, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "CILINDRO?", 1390, 440, 120, "black", V.CYA, 1, glow=0.18)
        V.pill(c, "210 km por semana", 1390, 620, 50, V.AMB, V.BG0, 1)
        V.glow_text(c, "1 m³ a cada 13 km", 1390, 790, 60, "black", V.WHITE, 1, glow=0.12)
    else:   # os 16 cubos cheios + o que sobra
        for i in range(16):
            x, y = V.POS_CUBO[i]
            V.cubo(c, x, y + 110, 92, 1, V.CYA, rot=None)
        x, y = V.POS_CUBO[16]
        V.cubo(c, x, y + 110, 92, 1, V.AMB, u=2 / 13, rot=None)
        V.label(c, "+ 2 km", x, y + 210, 1, 40, V.AMB, "black")
        V.glow_text(c, "SOBROU?", 1390, 320, 120, "black", V.AMB, 1, glow=0.14)
        V.glow_text(c, "ARREDONDE", 1390, 480, 110, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "PARA CIMA", 1390, 610, 110, "black", V.CYA, 1, glow=0.18)
        V.pill(c, "A PEGADINHA DO GNV", 1390, 790, 48, V.RED, V.BG0, 1)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_qual_cilindro.jpg", "capa_B_arredonde_para_cima.jpg")):
        capa(V, qual, pasta / nome)
