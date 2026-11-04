"""Capas do Short 029 (ENEM 2025, questão 146) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_qual_cilindro.jpg, capa_B_16_nao_basta.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 146", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":   # os cinco cilindros e a pergunta: não entrega a resposta
        V.big(c, "QUAL CILINDRO", 470, 1, V.WHITE, 104)
        V.big(c, "AGUENTA A SEMANA?", 600, 1, V.WHITE, 96, hl="AGUENTA A SEMANA?", hl_col=V.CYA)
        V.tanques(c, 1, 0, None, yb=1330)
        V.label(c, "30 km por dia · 1 m³ a cada 13 km", V.CX, 1500, 1, 46, V.AMB, "black")
    else:   # a armadilha: 16 não basta
        V.big(c, "16 NÃO BASTA!", 540, 1, V.RED, 130)
        for i in range(16):
            V.aula.cubo(c, V.CX - 300 + (i % 6) * 120, 800 + (i // 6) * 150, 92, 1, V.CYA, rot=None)
        V.aula.cubo(c, V.CX - 300 + 4 * 120, 1100, 92, 1, V.AMB, u=2 / 13, rot=None)
        V.stamp(c, "ARMADILHA DO ENEM", V.CX, 1420, V.RED, 1, 62, rot=-4)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_qual_cilindro.jpg", "capa_B_16_nao_basta.jpg")):
        capa(V, qual, pasta / nome)
