"""Capas do Short 037 (ENEM 2025, questão 150) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_qual_andou_mais.jpg, capa_B_o_desenho_engana.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 150", V.CX, 250, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":   # as cinco telas e a pergunta: não entrega a resposta
        V.big(c, "QUAL CARRINHO", 400, 1, V.WHITE, 100)
        V.big(c, "ANDOU MAIS?", 520, 1, V.WHITE, 104, hl="ANDOU MAIS?", hl_col=V.MNT)
        V.telas(c, 1, 0, dy=230)
    else:   # a armadilha
        V.big(c, "O MAIOR DESENHO", 400, 1, V.WHITE, 92)
        V.big(c, "NÃO GANHA!", 520, 1, V.RED, 110)
        V.telas(c, 1, 0, foco=0, dy=230)
        V.stamp(c, "ARMADILHA DO ENEM", V.CX, 1640, V.RED, 1, 62, rot=-4)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_qual_andou_mais.jpg", "capa_B_o_desenho_engana.jpg")):
        capa(V, qual, pasta / nome)
