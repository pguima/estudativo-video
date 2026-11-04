"""Capas do Short 017 (ENEM 2025, questão 140) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_menos_sodio.jpg, capa_B_rotulo.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 140", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":
        V.big(c, "QUAL TEM", 480, 1, V.WHITE, 140)
        V.big(c, "MENOS SÓDIO?", 640, 1, V.WHITE, 130, hl="MENOS SÓDIO?", hl_col=V.CYA)
        V.coluna(c, 1, 0, lambda i: dict(borda=V.AMB, glow=0.6), y0=820, passo=146)   # sem os totais: não entrega
    else:
        V.big(c, "O MENOR DO", 480, 1, V.WHITE, 120)
        V.big(c, "RÓTULO?", 630, 1, V.WHITE, 140, hl="RÓTULO?", hl_col=V.RED)
        V.coluna(c, 1, 0, lambda i: dict(borda=V.RED, glow=1.0, cor_s=V.RED) if i == 4 else None, y0=820, passo=146)
        V.stamp(c, "PEGADINHA DO ENEM", V.CX, 1560, V.RED, 1, 62, rot=-4)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_menos_sodio.jpg", "capa_B_rotulo.jpg")):
        capa(V, qual, pasta / nome)
