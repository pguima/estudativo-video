"""Capas do Short 031 (ENEM 2025, questão 147) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_por_onde_o_heroi.jpg, capa_B_troque_o_sinal.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 147", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":   # o herói entre os vilões e a pergunta: não entrega a resposta
        V.big(c, "POR ONDE O HERÓI", 420, 1, V.WHITE, 96)
        V.big(c, "FOGE DOS VILÕES?", 540, 1, V.WHITE, 92, hl="FOGE DOS VILÕES?", hl_col=V.MNT)
        V.cena(c, 1, 0, quad=0.6)
        for q in (V.T_, V.V_):
            V.segmento(c, V.S_, q, 0.8, V.RED, 4, tracej=True)
        V.label(c, "y = ?", V.CX, 1480, 1, 70, V.AMB, "black")
    else:   # a armadilha: trocar o sinal
        V.big(c, "TROQUE O SINAL!", 540, 1, V.RED, 120)
        V.cena(c, 1, 0, s=False)
        V.segmento(c, V.T_, V.V_, 1, V.WHITE, 4)
        V.reta(c, *V.M_, -1, 3, 1, V.MNT, w=7)
        V.angulo_reto(c, V.M_, (3, 1), (-1, 3), 1, 26)
        V.stamp(c, "ARMADILHA DO ENEM", V.CX, 1470, V.RED, 1, 62, rot=-4)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_por_onde_o_heroi.jpg", "capa_B_troque_o_sinal.jpg")):
        capa(V, qual, pasta / nome)
