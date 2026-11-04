"""Capas do Short 021 (ENEM 2025, questão 142) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_o_que_acontece.jpg, capa_B_pegadinha_inversa.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 142", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    g = (210, 1420, 720, 560)
    if qual == "a":   # o gráfico sem pintar: não entrega a resposta
        V.big(c, "O QUE", 480, 1, V.WHITE, 140)
        V.big(c, "ACONTECE?", 640, 1, V.WHITE, 140, hl="ACONTECE?", hl_col=V.CYA)
        V.grafico(c, 1, 0, 1.0, cores={"antes": (V.WHITE, 1, 0), "desce": (V.WHITE, 1, 0.3), "deitada": (V.WHITE, 1, 0)}, g=g)
        V.label(c, "respiração × tempo, meditando", V.CX, 760, 1, 46, V.AMB, "black")
    else:
        V.big(c, "INVERSAMENTE", 480, 1, V.WHITE, 120)
        V.big(c, "PROPORCIONAL?", 630, 1, V.WHITE, 120, hl="PROPORCIONAL?", hl_col=V.RED)
        V.grafico(c, 1, 0, 1.0, cores={"antes": (V.INK2, 0.5, 0), "desce": (V.WHITE, 1, 0), "deitada": (V.MNT, 1, 0.6)}, g=g)
        V._curva(c, 0.19, 1.0, g, V.RED, 1, w=8, fn=lambda u: min(1.05, 0.2 / max(u, 0.01)), glow=0.3)
        V.stamp(c, "PEGADINHA DO ENEM", V.CX, 1620, V.RED, 1, 62, rot=-4)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_o_que_acontece.jpg", "capa_B_pegadinha_inversa.jpg")):
        capa(V, qual, pasta / nome)
