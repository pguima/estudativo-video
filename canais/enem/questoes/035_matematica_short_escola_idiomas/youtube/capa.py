"""Capas do Short 035 (ENEM 2025, questão 149) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_quantos_no_frances.jpg, capa_B_20_nao_e.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 149", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":   # os dois gráficos e a pergunta: não entrega a resposta
        V.big(c, "QUANTOS ALUNOS", 380, 1, V.WHITE, 96)
        V.big(c, "NO FRANCÊS?", 490, 1, V.WHITE, 100, hl="NO FRANCÊS?", hl_col=V.MNT)
        V.graficos(c, 1, 0)
    else:   # a armadilha
        V.big(c, "20 NÃO É A RESPOSTA!", 500, 1, V.RED, 92)
        V.graficos(c, 1, 0, foco_b=2, cores_b=(V.CYA, V.AMB, V.RED, V.INK2))
        V.stamp(c, "ARMADILHA DO ENEM", V.CX, 1560, V.RED, 1, 62, rot=-4)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_quantos_no_frances.jpg", "capa_B_20_nao_e.jpg")):
        capa(V, qual, pasta / nome)
