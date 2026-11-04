"""Capas do Short 023 (ENEM 2025, questão 143) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_qual_a_diferenca.jpg, capa_B_armadilha.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 143", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":   # a conta sem resultado: não entrega a resposta
        V.big(c, "QUAL É A", 480, 1, V.WHITE, 140)
        V.big(c, "DIFERENÇA?", 640, 1, V.WHITE, 140, hl="DIFERENÇA?", hl_col=V.CYA)
        V.contaG(c, 1, 0, V.CX + 40, V.CY + 180, "10,00", " 9,58", res=" ?,??", res_col=V.CYA)
        V.label(c, "o recorde de Usain Bolt", V.CX, 1650, 1, 54, V.MNT, "black")
    else:
        V.big(c, "0,52? 1,42?", 520, 1, V.RED, 130)
        V.contaG(c, 1, 0, V.CX + 40, V.CY + 160, "10,00", " 9,58", res=" 0,52", res_col=V.WHITE, cores_res={3: V.RED},
                 novos={1: "9", 3: "10", 4: "10"}, riscos=(0, 1, 3, 4), hl=(3,), hl_col=V.RED)
        V.stamp(c, "ARMADILHA DO ENEM", V.CX, 1620, V.RED, 1, 62, rot=-4)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_qual_a_diferenca.jpg", "capa_B_armadilha.jpg")):
        capa(V, qual, pasta / nome)
