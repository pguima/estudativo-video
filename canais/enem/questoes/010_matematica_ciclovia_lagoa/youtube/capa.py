"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 010 (ENEM 2025, questão 136), com o visual da aula.
python capa.py    -> youtube/capa_A_quantos.jpg, capa_B_pegadinha.jpg"""
import importlib.util, math, sys
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


def anel(V, c, cx, cy, R, n, s, buraco=False):
    """lagoa com n policiais e seus trechos de 400 m (24°); buraco = último trecho em coral, sem policial"""
    V.lagoa(c, cx, cy, R, 1, 0.3)
    for i in range(15):
        a0 = i * 2 * V.D12
        if i < n:
            V.arco(c, cx, cy, R, a0, a0 + 2 * V.D12, V.CYA if i % 2 == 0 else V.MNT, 0.9, max(14, R * 0.08), glow=False)
        elif buraco:
            V.arco(c, cx, cy, R, a0, a0 + 2 * V.D12, V.RED, 1, max(14, R * 0.08))
    for i in range(n):
        V.policial_na_pista(c, cx, cy, R, i * 2 * V.D12 + V.D12, s, 1, V.CYA if i % 2 == 0 else V.MNT)


def capa(V, qual, out):
    s = skia.Surface(V.W, V.H); c = s.getCanvas()
    c.drawImage(V.matematica._bg(), 0, 0)
    marca = "ESTUDATIVO · QUESTÃO DO ENEM 2025"
    w = V.text_w(marca, "extrabold", 30) + 36
    V.pill(c, marca, 70 + w / 2, 90, 30, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":
        anel(V, c, 520, 600, 330, 15, 30)
        V.glow_text(c, "?", 520, 640, 260, "black", V.WHITE, 1, glow=0.14)
        V.glow_text(c, "QUANTOS", 1380, 330, 150, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "POLICIAIS?", 1380, 500, 130, "black", V.CYA, 1, glow=0.18)
        V.glow_text(c, "lagoa de raio 1 km", 1380, 660, 70, "black", V.AMB, 1, glow=0.12)
        V.pill(c, "QUESTÃO 136", 1380, 830, 50, V.MNT, V.BG0, 1)
    else:
        anel(V, c, 470, 600, 300, 14, 26, buraco=True)
        V.glow_text(c, "14", 470, 640, 180, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, "200 m ou 400 m?", 1330, 300, 110, "black", V.WHITE, 1, glow=0.12)
        pos = V.eq(c, [("6.000 ÷ 200", V.AMB), (" = ", V.WHITE), ("30", V.RED)], 500, 1, 92, cx=1330, maxw=820)
        V.strike(c, pos[0][0], pos[-1][1], 500, 1, 1)
        V.pill(c, "A PEGADINHA DO ENEM", 1330, 690, 56, V.RED, V.BG0, 1)
        V.glow_text(c, "conte os DOIS lados", 1330, 870, 78, "black", V.CYA, 1, glow=0.16)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_quantos.jpg", "capa_B_pegadinha.jpg")):
        capa(V, qual, pasta / nome)
