"""Capas do Short 009 (ENEM 2025, questão 137) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_metade.jpg, capa_B_pegadinha.jpg, capa_C_quanto_sai.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 137", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":
        V.big(c, "SAI METADE", 500, 1, V.WHITE, 140, hl="METADE", hl_col=V.MNT)
        V.big(c, "DO RECIPIENTE?!", 640, 1, V.WHITE, 104)
        V.recipiente(c, V.CX, 1330, 1, 0.3, 0.5, w=420, h=600, fantasma=1, marca5=1, rot="")
        V.stamp(c, "99,95% → 99,90%", V.CX, 1480, V.AMB, 1, 60, rot=-4)
    elif qual == "b":
        V.big(c, "0,005 L", 500, 1, V.RED, 150)
        V.big(c, "OU 5 L?", 660, 1, V.WHITE, 150, hl="5 L?", hl_col=V.MNT)
        V.recipiente(c, 300, 1290, 1, 0.3, 1.0, w=300, h=470, rot="")
        V.recipiente(c, 780, 1290, 1, 0.3, 0.5, w=300, h=470, fantasma=1, rot="")
        V.stamp(c, "PEGADINHA DO ENEM", V.CX, 1440, V.RED, 1, 62, rot=-4)
    else:
        V.big(c, "QUANTO SAI?", 520, 1, V.WHITE, 130, hl="SAI?", hl_col=V.CYA)
        V.recipiente(c, V.CX, 1300, 1, 0.3, 1.0, w=400, h=500, hl_s2=1, rot="")
        V.pill(c, "S1: 99,95% → 99,90%", V.CX, 680, 56, V.AMB, V.BG0, 1)
        V.big(c, "PARECE UMA GOTINHA...", 1430, 1, V.INK2, 70)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("abc", ("capa_A_metade.jpg", "capa_B_pegadinha.jpg", "capa_C_quanto_sai.jpg")):
        capa(V, qual, pasta / nome)
