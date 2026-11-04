"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 014 (ENEM 2025, questão 139), com o visual da aula.
python capa.py    -> youtube/capa_A_mediana.jpg, capa_B_pegadinha.jpg"""
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
        V.coluna(c, 1, 1, lambda i, k: dict(borda=V.CYA, glow=1.0, cor_v=V.CYA) if k in (4, 5) else None, x=470, y0=230, passo=72)
        V.glow_text(c, "QUAL É A", 1350, 330, 130, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "MEDIANA?", 1350, 490, 150, "black", V.CYA, 1, glow=0.18)
        V.glow_text(c, "10 velocidades de internet", 1350, 650, 56, "black", V.AMB, 1, glow=0.12)
        V.pill(c, "QUESTÃO 139", 1350, 830, 50, V.MNT, V.BG0, 1)
    else:
        V.coluna(c, 1, 0, lambda i, k: dict(borda=V.RED, glow=1.0, cor_v=V.RED) if i in (4, 5) else None, x=470, y0=230, passo=72)
        V.glow_text(c, "ESQUECEU DE", 1330, 300, 100, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "ORDENAR?", 1330, 430, 130, "black", V.RED, 1, glow=0.16)
        pos = V.eq(c, [("(340 + 380) ÷ 2", V.AMB), (" = ", V.WHITE), ("360", V.RED)], 600, 1, 78, cx=1330, maxw=820)
        V.strike(c, pos[0][0], pos[-1][1], 600, 1, 1)
        V.pill(c, "A PEGADINHA DO ENEM", 1330, 760, 52, V.RED, V.BG0, 1)
        V.glow_text(c, "média, moda ou mediana?", 1330, 900, 62, "black", V.CYA, 1, glow=0.16)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_mediana.jpg", "capa_B_pegadinha.jpg")):
        capa(V, qual, pasta / nome)
