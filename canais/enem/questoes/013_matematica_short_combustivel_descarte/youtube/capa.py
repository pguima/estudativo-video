"""Capas do Short 013 (ENEM 2025, questão 138) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_quanto.jpg, capa_B_pegadinha.jpg, capa_C_qual.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 138", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":
        V.big(c, "QUANTO", 500, 1, V.WHITE, 150)
        V.big(c, "ENVIAR?", 660, 1, V.WHITE, 150, hl="ENVIAR?", hl_col=V.CYA)
        V.caminhao(c, V.TX, 1180, 1.45, 1, 0.34, 0.0, txt="10.200")
        V.descarte(c, V.TX, 1180, 1.45, 1, 0.5, 0.0, "?")
        V.stamp(c, "CHEGARAM SÓ 9.900", V.CX, 1440, V.AMB, 1, 54, rot=-4)
    elif qual == "b":
        V.big(c, "O DESCARTE", 500, 1, V.WHITE, 130)
        V.big(c, "DOBRA?", 660, 1, V.WHITE, 150, hl="DOBRA?", hl_col=V.RED)
        V.caminhao(c, V.TX, 1180, 1.45, 1, 0.68, 0.0, txt="×2")
        V.descarte(c, V.TX, 1180, 1.45, 1, 0.5, 0.0)
        V.stamp(c, "PEGADINHA DO ENEM", V.CX, 1440, V.RED, 1, 62, rot=-4)
    else:
        V.big(c, "20.400", 500, 1, V.RED, 150)
        V.big(c, "OU 20.300?", 660, 1, V.WHITE, 140, hl="20.300?", hl_col=V.MNT)
        V.caminhao(c, V.TX, 1180, 1.45, 1, 0.68, 0.0)
        V.glow_text(c, "?", V.TX - 85 * 1.45, 1180 - 120 * 1.45, 170, "black", V.BG0, 1, glow=0.05)
        V.big(c, "QUANTO MANDAR?", 1450, 1, V.CYA, 84)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("abc", ("capa_A_quanto.jpg", "capa_B_pegadinha.jpg", "capa_C_qual.jpg")):
        capa(V, qual, pasta / nome)
