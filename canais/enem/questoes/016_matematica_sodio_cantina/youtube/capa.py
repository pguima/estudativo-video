"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 016 (ENEM 2025, questão 140), com o visual da aula.
python capa.py    -> youtube/capa_A_menos_sodio.jpg, capa_B_pegadinha.jpg"""
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
        V.coluna(c, 1, 0, lambda i: dict(borda=V.AMB, glow=0.6),
                 x=520, y0=250, passo=150)
        V.glow_text(c, "QUAL TEM", 1420, 330, 120, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "MENOS SÓDIO?", 1420, 480, 110, "black", V.CYA, 1, glow=0.18)
        V.glow_text(c, "por pacote, não por porção", 1420, 640, 52, "black", V.AMB, 1, glow=0.12)
        V.pill(c, "QUESTÃO 140", 1420, 830, 50, V.MNT, V.BG0, 1)
    else:
        V.coluna(c, 1, 0, lambda i: dict(borda=V.RED, glow=1.0, cor_s=V.RED) if i == 4 else None, x=520, y0=250, passo=150)
        V.glow_text(c, "O MENOR POR", 1420, 300, 100, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "PORÇÃO?", 1420, 430, 130, "black", V.RED, 1, glow=0.16)
        pos = V.eq(c, [("166 mg", V.AMB), (" → ", V.WHITE), ("E", V.RED)], 600, 1, 90, cx=1420, maxw=800)
        V.strike(c, pos[0][0], pos[-1][1], 600, 1, 1)
        V.pill(c, "A PEGADINHA DO ENEM", 1420, 760, 52, V.RED, V.BG0, 1)
        V.glow_text(c, "5 porções × 166 = 830 mg", 1420, 900, 56, "black", V.CYA, 1, glow=0.16)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_menos_sodio.jpg", "capa_B_pegadinha.jpg")):
        capa(V, qual, pasta / nome)
