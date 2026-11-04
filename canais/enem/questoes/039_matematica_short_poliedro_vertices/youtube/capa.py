"""Capas do Short 039 (ENEM 2025, questão 151) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_quantos_vertices.jpg, capa_B_110_nao_e.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 151", V.CX, 250, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":   # o sólido e a pergunta: não entrega a resposta
        V.big(c, "QUANTOS", 400, 1, V.WHITE, 110)
        V.big(c, "VÉRTICES?", 520, 1, V.WHITE, 114, hl="VÉRTICES?", hl_col=V.MNT)
        V.solido(c, 2.2, 1, cy=1000, escala=245)
    else:   # a armadilha
        V.big(c, "110 NÃO É", 400, 1, V.RED, 110)
        V.big(c, "A RESPOSTA!", 520, 1, V.WHITE, 104)
        V.solido(c, 2.2, 1, cy=1000, escala=245, modo="vidro", k_ar=1.0, cor_ar=V.RED)
        V.stamp(c, "ARMADILHA DO ENEM", V.CX, 1500, V.RED, 1, 62, rot=-4)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_quantos_vertices.jpg", "capa_B_110_nao_e.jpg")):
        capa(V, qual, pasta / nome)
