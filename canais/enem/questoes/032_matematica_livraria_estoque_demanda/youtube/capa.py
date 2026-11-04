"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 032 (ENEM 2025, questão 148), com o visual da aula.
python capa.py    -> youtube/capa_A_qual_livro.jpg, capa_B_some_as_barras.jpg"""
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
    if qual == "a":   # o gráfico e a pergunta: não entrega a resposta
        V.grafico(c, 1, 0)
        V.glow_text(c, "QUAL LIVRO", 1460, 300, 110, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "ESTÁ FALTANDO?", 1460, 440, 96, "black", V.CYA, 1, glow=0.18)
        V.pill(c, "estoque × demanda", 1460, 620, 50, V.AMB, V.BG0, 1)
        V.glow_text(c, "leitura de gráfico", 1460, 790, 56, "black", V.WHITE, 1, glow=0.12)
    else:   # as barras empilhadas: o truque da soma
        V.grafico(c, 1, 0, emp={i: 1.0 for i in range(4)})
        V.glow_text(c, "SOME", 1460, 320, 130, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "AS BARRAS!", 1460, 470, 120, "black", V.AMB, 1, glow=0.14)
        V.pill(c, "A PEGADINHA DO GRÁFICO", 1460, 680, 46, V.RED, V.BG0, 1)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_qual_livro.jpg", "capa_B_some_as_barras.jpg")):
        capa(V, qual, pasta / nome)
