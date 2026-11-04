"""Capas do Short 025 (ENEM 2025, questão 144) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_onde_ficam_as_sombras.jpg, capa_B_armadilha.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 144", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    x, y, z = V.INI
    if qual == "a":   # o cubo no começo e as sombras: não entrega a resposta
        V.big(c, "ONDE FICAM AS", 480, 1, V.WHITE, 120)
        V.big(c, "SOMBRAS?", 630, 1, V.WHITE, 140, hl="SOMBRAS?", hl_col=V.CYA)
        with V.tela3d(c, 1.0, 1100):
            V.aula.cena3d(c, 1)
            V.aula.sombras(c, V.INI, 1, V.CYA)
            V.aula.cubo(c, V.INI, 1, V.AMB, glow=0.6)
        V.label(c, "o cubo que se move no espaço", V.CX, 1560, 1, 54, V.AMB, "black")
    else:
        V.big(c, "y? z? x?", 520, 1, V.RED, 140)
        with V.tela3d(c, 1.0, 1080):
            V.aula.cena3d(c, 1, tints={"yz": (V.CYA, 1.0, "yz")})
            V.aula.cubo(c, V.INI, 1, V.AMB)
            V.aula.seta3d(c, (x, y + 0.5, z + 0.5), (0.05, y + 0.5, z + 0.5), 1, V.CYA, "x", w=8)
        V.stamp(c, "ARMADILHA DO ENEM", V.CX, 1580, V.RED, 1, 62, rot=-4)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_onde_ficam_as_sombras.jpg", "capa_B_armadilha.jpg")):
        capa(V, qual, pasta / nome)
