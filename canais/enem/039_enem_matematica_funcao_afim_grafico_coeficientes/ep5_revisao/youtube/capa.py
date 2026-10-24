"""Capas — Função Afim, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos: A = "f(x) = ax + b" gigante no centro com as duas perguntas apontando para o b e para o a, e "2 PERGUNTAS ·
1 LINHA DE CONTA"; B = a conta de água em duas faixas (12 m³ → R$ 84 · 24 m³ → R$ 168?) com "A REGRA DE TRÊS MENTE?";
C = o gráfico do equilíbrio à direita, com o cruzamento destacado, e "EMPATOU. JÁ LUCROU?" à esquerda.
Nenhuma mostra gabarito."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO AFIM · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_perguntas(c):
    background(c)
    selo_topo(c, W / 2)
    s = "2 PERGUNTAS · 1 LINHA"
    text(c, s, W / 2, 290, fit(s, 140, 1700), "black", INK)
    rrect(c, W / 2 - 560, 420, 1120, 260, 44, "#FFFFFF", 1, shadow=True)
    V.fmid(c, "f(x) =", W / 2 - 200, 550, 150, "black", INK, 1)
    V.fmid(c, "a", W / 2 + 90, 550, 150, "black", PURPLE, 1)
    V.fmid(c, "x +", W / 2 + 250, 550, 150, "black", INK, 1)
    V.fmid(c, "b", W / 2 + 440, 550, 150, "black", BLUE, 1)
    for (x, col, s_) in ((W / 2 + 90, PURPLE, "quanto muda por unidade?"), (W / 2 + 440, BLUE, "quanto vale no início?")):
        arrow(c, x, 830, x, 700, col, 1, 10, 30)
    pill(c, "quanto muda por unidade?", 560, 900, PURPLE, size=50, anchor="center", bounds=(0, 1920))
    pill(c, "quanto vale no início?", 1430, 900, BLUE, size=50, anchor="center", bounds=(0, 1920))


def capa_regra3(c):
    background(c)
    rrect(c, 0, 0, W * 0.47, H, 0, mix("#FFFFFF", AMBER, 0.14))
    selo_topo(c)
    for j, (s, col, sz) in enumerate((("A REGRA", INK, 130), ("DE TRÊS", INK, 130), ("MENTE?", RED, 170))):
        text(c, s, 84, 340 + j * 175, fit(s, sz, 800), "black", col, align="left")
    c.save(); c.translate(1100, 300); c.scale(0.9, 0.9)
    V.torneira(c, 1)
    c.restore()
    for j, (esq, dir_, col) in enumerate((("12 m³", "R$ 84", INK), ("24 m³", "R$ 168?", RED))):
        y = 560 + j * 210
        rrect(c, 980, y - 85, 860, 170, 30, "#FFFFFF" if j == 0 else mix("#FFFFFF", AMBER, 0.28), 1, shadow=True)
        V.fmid(c, V.nb(esq), 1170, y, 80, "black", BLUE, 1)
        arrow(c, 1320, y, 1460, y, INK2, 1, 8, 24)
        V.fmid(c, V.nb(dir_), 1650, y, 80, "black", col, 1)
    pill(c, "+ TAXA FIXA DE R$ 30", 1410, 960, AMBER, size=44, anchor="center", bounds=(0, 1920))


def capa_equilibrio(c):
    background(c)
    selo_topo(c)
    text(c, "EMPATOU.", 84, 360, fit("EMPATOU.", 170, 820), "black", INK, align="left")
    text(c, "JÁ LUCROU?", 84, 540, fit("JÁ LUCROU?", 170, 820), "black", GREEN, align="left")
    text(c, "custo · receita · lucro", 84, 660, 60, "black", AMBER, align="left")
    pill(c, "9 pegadinhas + 5 questões", 84, 900, BLUE, size=48, bounds=(0, 1920))
    c.save(); c.translate(1420, 560); c.scale(2.1, 2.1)
    V.equilibrio(c, 1)
    c.restore()
    xc, yc = 1420 + 2.1 * (-160 + 330 * 90 / 130), 560 + 2.1 * (40 - 150 * 90 / 130)
    c.drawCircle(xc, yc, 52, paint(AMBER, 1, stroke=8))
    text(c, "receita", 1760, 200, 44, "black", GREEN, align="right")
    text(c, "custo", 1900, 300, 44, "black", RED, align="right")


if __name__ == "__main__":
    for nome, fn in (("capa_A_duas_perguntas", capa_perguntas), ("capa_B_regra_de_tres_mente", capa_regra3),
                     ("capa_C_empatou_ja_lucrou", capa_equilibrio)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
