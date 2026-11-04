"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 026 (ENEM 2025, questão 145), com o visual da aula.
python capa.py    -> youtube/capa_A_nao_e_40.jpg, capa_B_100_internautas.jpg"""
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
    if qual == "a":   # os 100 internautas ainda sem cor e a pergunta: não entrega a resposta
        V.cem(c, 1, 0, t_ac=-99, cy=580)
        V.glow_text(c, "90% ACESSAM", 1390, 300, 96, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "60% MULHERES", 1390, 430, 96, "black", V.AMB, 1, glow=0.14)
        V.glow_text(c, "HOMENS: 40%?", 1390, 600, 110, "black", V.CYA, 1, glow=0.18)
        V.pill(c, "NÃO É 40%!", 1390, 780, 56, V.RED, V.BG0, 1)
    else:
        V.cem(c, 1, 0, t_ac=-99, t_gen=-99, t_hom=-99, foco="H", foco_a=1.0, cy=580)
        V.glow_text(c, "IMAGINE", 1390, 300, 110, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "100 PESSOAS", 1390, 440, 110, "black", V.CYA, 1, glow=0.18)
        V.pill(c, "PROBABILIDADE", 1390, 620, 50, V.AMB, V.BG0, 1)
        V.glow_text(c, "porcentagem de porcentagem", 1390, 790, 52, "black", V.MNT, 1, glow=0.12)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_nao_e_40.jpg", "capa_B_100_internautas.jpg")):
        capa(V, qual, pasta / nome)
