"""Capas do Short 041 (ENEM 2025, questão 152) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_quantos_tijolos.jpg, capa_B_1200_nao_e.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 152", V.CX, 250, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":   # a grade e a pergunta: não entrega a resposta
        V.big(c, "QUANTOS TIJOLOS", 400, 1, V.WHITE, 96)
        V.big(c, "POR DIA?", 520, 1, V.WHITE, 110, hl="POR DIA?", hl_col=V.MNT)
        V.grade(c, V.CX, 960, 5, 9, 96, 1, cor=V.AMB, cor_novo=V.CYA, base=(3, 6))
        V.label(c, "3 × 6 h = 720  ·  5 × 9 h = ?", V.CX, 1330, 1, 54, V.AMB, "black")
    else:   # a armadilha
        V.big(c, "1 200 NÃO É", 400, 1, V.RED, 110)
        V.big(c, "A RESPOSTA!", 520, 1, V.WHITE, 104)
        V.grade(c, V.CX, 960, 5, 6, 110, 1, cor=V.RED)
        V.stamp(c, "ARMADILHA DO ENEM", V.CX, 1420, V.RED, 1, 62, rot=-4)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_quantos_tijolos.jpg", "capa_B_1200_nao_e.jpg")):
        capa(V, qual, pasta / nome)
