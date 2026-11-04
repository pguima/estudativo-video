"""Capas do Short 011 (ENEM 2025, questão 136) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_quantos.jpg, capa_B_pegadinha.jpg, capa_C_buraco.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 136", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":
        V.big(c, "QUANTOS", 500, 1, V.WHITE, 140)
        V.big(c, "POLICIAIS?", 660, 1, V.WHITE, 140, hl="POLICIAIS?", hl_col=V.CYA)
        V.lagoa(c, V.CX, 1080, 280, 1, 0.3)
        V.anel(c, V.CX, 1080, 280, 1, 99, -1, 15, 0, s=26)
        V.glow_text(c, "?", V.CX, 1150, 220, "black", V.WHITE, 1, glow=0.14)
        V.stamp(c, "LAGOA DE RAIO 1 km", V.CX, 1450, V.AMB, 1, 54, rot=-4)
    elif qual == "b":
        V.big(c, "200 m", 500, 1, V.RED, 150)
        V.big(c, "OU 400 m?", 660, 1, V.WHITE, 150, hl="400 m?", hl_col=V.MNT)
        V.lagoa(c, V.CX, 1060, 270, 1, 0.3)
        V.um_policial(c, V.CX, 1060, 270, V.P90, 1, 99, 0)
        V.stamp(c, "PEGADINHA DO ENEM", V.CX, 1440, V.RED, 1, 62, rot=-4)
    else:
        V.big(c, "COM 14,", 500, 1, V.WHITE, 140)
        V.big(c, "SOBRA UM BURACO", 650, 1, V.WHITE, 100, hl="BURACO", hl_col=V.RED)
        g0 = 168 * V.GRAU
        V.lagoa(c, V.CX, 1060, 270, 1, 0.3)
        V.anel(c, V.CX, 1060, 270, 1, 99, -1, 14, 0, s=24, ang0=g0 + 2 * V.D12)
        V.arco(c, V.CX, 1060, 270, g0, g0 + 2 * V.D12, V.RED, 1, 30)
        V.glow_text(c, "14", V.CX, 1110, 170, "black", V.WHITE, 1, glow=0.12)
        V.big(c, "QUANTOS PRECISA?", 1470, 1, V.CYA, 80)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("abc", ("capa_A_quantos.jpg", "capa_B_pegadinha.jpg", "capa_C_buraco.jpg")):
        capa(V, qual, pasta / nome)
