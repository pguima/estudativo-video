"""Capas do Short 019 (ENEM 2025, questão 141) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_quantas_cores.jpg, capa_B_hexagonos.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 141", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":
        V.big(c, "QUANTAS", 480, 1, V.WHITE, 140)
        V.big(c, "CORES?", 640, 1, V.WHITE, 150, hl="CORES?", hl_col=V.CYA)
        V.solido(c, V.CX, 1200, 300, 0, 1, yaw=0.62, explode=0.45)   # sem pintar: não entrega a resposta
    else:
        V.big(c, "MESMA", 480, 1, V.WHITE, 140)
        V.big(c, "COR?", 640, 1, V.WHITE, 150, hl="COR?", hl_col=V.RED)
        V.hexagono(c, V.CX - 150, 1050, 260, V.AMB, 0.3)
        V.hexagono(c, V.CX - 150, 1050, 260, V.AMB, 1, stroke=True)
        V.hexagono(c, V.CX + 260, 1100, 140, V.ROSA, 0.35)
        V.hexagono(c, V.CX + 260, 1100, 140, V.ROSA, 1, stroke=True)
        V.stamp(c, "PEGADINHA DO ENEM", V.CX, 1500, V.RED, 1, 62, rot=-4)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_quantas_cores.jpg", "capa_B_hexagonos.jpg")):
        capa(V, qual, pasta / nome)
