"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 022 (ENEM 2025, questão 143), com o visual da aula.
python capa.py    -> youtube/capa_A_quanto_mais_rapido.jpg, capa_B_conta_armada.jpg"""
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
    if qual == "a":   # a conta sem resultado: não entrega a resposta
        c.save(); c.translate(560, 560); c.scale(1.45, 1.45); c.translate(-560, -560)
        V.conta(c, 1, 0, 560, 400, "10,00", " 9,58", res=" ?,??", res_col=V.CYA)
        c.restore()
        V.glow_text(c, "O RECORDE", 1390, 330, 120, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "DO BOLT", 1390, 480, 120, "black", V.MNT, 1, glow=0.18)
        V.glow_text(c, "quanto mais rápido?", 1390, 640, 60, "black", V.AMB, 1, glow=0.12)
        V.pill(c, "QUESTÃO 143", 1390, 820, 50, V.CYA, V.BG0, 1)
    else:
        c.save(); c.translate(560, 560); c.scale(1.45, 1.45); c.translate(-560, -560)
        V.conta(c, 1, 0, 560, 400, "10,00", " 9,58", res=" 0,52", res_col=V.WHITE, cores_res={3: V.RED},
                novos={1: "9", 3: "10", 4: "10"}, riscos=(0, 1, 3, 4), hl=(3,), hl_col=V.RED)
        c.restore()
        V.glow_text(c, "0,52?", 1390, 330, 150, "black", V.RED, 1, glow=0.16)
        V.glow_text(c, "1,42?", 1390, 500, 150, "black", V.RED, 1, glow=0.16)
        V.pill(c, "AS ARMADILHAS DO EMPRÉSTIMO", 1390, 680, 46, V.AMB, V.BG0, 1)
        V.glow_text(c, "subtração com decimais", 1390, 840, 54, "black", V.CYA, 1, glow=0.12)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_quanto_mais_rapido.jpg", "capa_B_conta_armada.jpg")):
        capa(V, qual, pasta / nome)
