"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 040 (ENEM 2025, questão 152), com o visual da aula.
python capa.py    -> youtube/capa_A_quantos_tijolos.jpg, capa_B_1200_nao_e.jpg"""
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
    if qual == "a":   # a grade e a pergunta: não entrega a resposta
        V.grade(c, 470, 600, 5, 9, 88, 1, cor=V.AMB, cor_novo=V.CYA, base=(3, 6))
        V.glow_text(c, "QUANTOS", 1430, 300, 120, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "TIJOLOS?", 1430, 440, 120, "black", V.MNT, 1, glow=0.18)
        V.pill(c, "3 × 6 h = 720  ·  5 × 9 h = ?", 1430, 640, 44, V.AMB, V.BG0, 1)
    else:   # a armadilha: só aumentar os funcionários
        V.grade(c, 470, 600, 5, 6, 100, 1, cor=V.RED)
        V.glow_text(c, "1 200 NÃO É", 1430, 330, 110, "black", V.RED, 1, glow=0.14)
        V.glow_text(c, "A RESPOSTA!", 1430, 470, 110, "black", V.WHITE, 1, glow=0.12)
        V.pill(c, "FUNCIONÁRIOS E HORAS JUNTOS", 1430, 660, 42, V.RED, V.BG0, 1)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_quantos_tijolos.jpg", "capa_B_1200_nao_e.jpg")):
        capa(V, qual, pasta / nome)
