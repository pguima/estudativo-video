"""Capas do Short 033 (ENEM 2025, questão 148) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_qual_livro.jpg, capa_B_some_as_barras.jpg
Texto importante no miolo (y 400–1500): a grade do canal e o feed cortam as bordas."""
import importlib.util, os, sys
from pathlib import Path
os.environ.setdefault("VIDEO_FORMATO", "vertical")  # antes do import motor
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
    V.pill(c, "ENEM 2025 · QUESTÃO 148", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":   # o gráfico e a pergunta: não entrega a resposta
        V.big(c, "QUAL LIVRO", 420, 1, V.WHITE, 104)
        V.big(c, "ESTÁ FALTANDO?", 540, 1, V.WHITE, 96, hl="ESTÁ FALTANDO?", hl_col=V.CYA)
        V.grafico(c, 1, 0)
        V.label(c, "estoque × demanda", V.CX, 1480, 1, 60, V.AMB, "black")
    else:   # a armadilha: somar as barras
        V.big(c, "SOME AS BARRAS!", 500, 1, V.AMB, 110)
        V.grafico(c, 1, 0, emp={i: 1.0 for i in range(4)})
        V.stamp(c, "ARMADILHA DO ENEM", V.CX, 1480, V.RED, 1, 62, rot=-4)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_qual_livro.jpg", "capa_B_some_as_barras.jpg")):
        capa(V, qual, pasta / nome)
