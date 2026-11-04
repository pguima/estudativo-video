"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 008 (ENEM 2025, questão 137), com o visual da aula.
python capa.py    -> youtube/capa_A_metade.jpg, capa_B_pegadinha.jpg"""
import importlib.util, sys
from pathlib import Path

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
    marca = "ESTUDATIVO · QUESTÃO DO ENEM 2025"
    w = V.text_w(marca, "extrabold", 30) + 36
    V.pill(c, marca, 70 + w / 2, 90, 30, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":
        c.save(); c.translate(400, 560); c.scale(1.3, 1.3); c.translate(-470, -560)
        V.recipiente(c, 470, 840, 1, 0.3, 0.5, w=300, h=480, fantasma=1, marca5=1, rot="")
        c.restore()
        V.glow_text(c, "99,95% → 99,90%", 1330, 330, 92, "black", V.AMB, 1, glow=0.14)
        V.glow_text(c, "SAI METADE", 1330, 540, 140, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "DO RECIPIENTE?!", 1330, 700, 100, "black", V.CYA, 1, glow=0.18)
        V.pill(c, "QUESTÃO 137", 1330, 860, 50, V.MNT, V.BG0, 1)
    else:
        V.glow_text(c, "0,005 L ou 5 L?", 960, 260, 150, "black", V.WHITE, 1, glow=0.12)
        V.eq(c, [("99,95% − 99,90%", V.AMB), (" = ", V.WHITE), ("0,05%", V.RED)], 470, 1, 100, cx=960, maxw=1500)
        V.strike(c, 360, 1560, 470, 1, 1)
        V.pill(c, "A PEGADINHA DO ENEM", 960, 660, 64, V.RED, V.BG0, 1)
        V.glow_text(c, "olhe para o que NÃO MUDA", 960, 860, 84, "black", V.CYA, 1, glow=0.16)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_metade.jpg", "capa_B_pegadinha.jpg")):
        capa(V, qual, pasta / nome)
