"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 034 (ENEM 2025, questão 149), com o visual da aula.
python capa.py    -> youtube/capa_A_quantos_no_frances.jpg, capa_B_20_nao_e.jpg"""
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
    if qual == "a":   # os dois gráficos e a pergunta: não entrega a resposta
        V.pizza(c, 290, 600, 190, 1, title="2023")
        V.barras(c, 520, 860, 1, kh=1.5, w=60, gap=108, title="2024", lab=21)
        V.glow_text(c, "QUANTOS", 1460, 300, 120, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "NO FRANCÊS?", 1460, 440, 110, "black", V.MNT, 1, glow=0.18)
        V.pill(c, "% de 2023 · total de 2024", 1460, 620, 46, V.AMB, V.BG0, 1)
    else:   # a armadilha: o 20 da barra é de 2024
        V.barras(c, 160, 820, 1, kh=1.8, w=90, gap=170, title="2024", foco=2, cores=(V.CYA, V.AMB, V.RED, V.INK2))
        V.glow_text(c, "20 NÃO É", 1460, 320, 120, "black", V.RED, 1, glow=0.14)
        V.glow_text(c, "A RESPOSTA!", 1460, 470, 110, "black", V.WHITE, 1, glow=0.12)
        V.pill(c, "A PEGADINHA DOS 2 GRÁFICOS", 1460, 680, 44, V.RED, V.BG0, 1)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_quantos_no_frances.jpg", "capa_B_20_nao_e.jpg")):
        capa(V, qual, pasta / nome)
