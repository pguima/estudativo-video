"""Capas — Equação do 2º Grau, Episódio 1 (tema claro). 3 variações em 1280x720.
Formatos: A = a conta do estudante em diagonal (3x² = 12x, ÷ x riscado) com o título "SUMIU UMA RAIZ" e a ficha "x = ?";
B = a tabelinha a | b | c gigante no centro com a equação x² − 7x + 10 numa faixa escura e "b = ?" em âmbar;
C = fundo escuro com as duas caixinhas do produto nulo e a frase "ALGUÉM AQUI É ZERO". Nenhuma mostra gabarito."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep1", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")
K = V.K
fmid = K.fmid


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


SELO = "MATEMÁTICA ENEM · EQUAÇÃO DO 2º GRAU · EP. 1"


def capa_sumiu(c):
    background(c)
    pill(c, SELO, 84, 90, BLUE, size=34, bounds=(0, 1920))
    c.save(); c.rotate(-6, 620, 520)
    rrect(c, 140, 300, 980, 420, 36, "#FFFFFF", shadow=True)
    K.expr(c, "3x^2 = 12x", 630, 430, 150, 1.0)
    pill(c, "÷ x", 1000, 600, AMBER, size=60, anchor="center")
    strike(c, 920, 600, 1080, 600, 1.0, RED)
    K.expr(c, "x = 4", 560, 610, 100, 1.0, cores={2: GREEN})
    c.restore()
    x = 1230
    for k, (s, col) in enumerate((("SUMIU", RED), ("UMA", INK), ("RAIZ", INK))):
        text(c, s, x, 360 + k * 170, fit(s, 190, 620), "black", col, align="left")
    rrect(c, 1230, 820, 520, 160, 32, mix("#FFFFFF", RED, 0.12))
    fmid(c, "x = ?", 1490, 900, 110, "black", RED)


def capa_tabela(c):
    background(c)
    rrect(c, 0, 0, W, 330, 0, INK)
    pill(c, SELO, W / 2, 70, BLUE, size=32, anchor="center", bounds=(0, 1920))
    K.expr(c, "x^2 - 7x + 10 = 0", W / 2, 215, 130, 1.0, cores={0: "#FFFFFF", 1: AMBER, 2: AMBER, 3: "#FFFFFF",
                                                                4: "#FFFFFF", 5: "#FFFFFF", 6: "#FFFFFF"})
    w = 300
    x0 = W / 2 - 1.5 * w
    rrect(c, x0, 420, 3 * w, 130, 26, mix("#FFFFFF", BLUE, 0.16))
    rrect(c, x0, 550, 3 * w, 210, 26, "#FFFFFF", shadow=True)
    for k, (L, v, col) in enumerate((("a", "1", INK), ("b", "?", AMBER), ("c", "10", INK))):
        xx = x0 + w * (k + 0.5)
        text_mid(c, L, xx, 485, 80, "black", BLUE)
        fmid(c, v, xx, 655, 120, "black", col)
    s = "O SINAL FAZ PARTE DO NÚMERO"
    text(c, s, W / 2, 940, fit(s, 120, 1760), "black", INK)


def capa_nulo(c):
    rrect(c, 0, 0, W, H, 0, INK)
    pill(c, SELO, W / 2, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))
    for k, s in enumerate(("2x", "(x-5)")):
        cx = 600 + k * 520
        rrect(c, cx - 220, 260, 440, 300, 40, mix(INK, GREEN, 0.25), stroke=8, stroke_color=GREEN)
        K.expr(c, s, cx, 410, 130, 1.0, cores={0: "#FFFFFF"})
    fmid(c, "·", 860, 410, 140, "black", "#FFFFFF")
    rrect(c, 1400, 330, 300, 160, 30, GREEN)
    fmid(c, "= 0", 1550, 410, 100, "black", INK)
    s = "ALGUÉM AQUI É ZERO"
    text(c, s, W / 2, 790, fit(s, 160, 1760), "black", "#FFFFFF")
    text(c, "equações incompletas sem fórmula", W / 2, 920, 60, "extrabold", GREEN)


if __name__ == "__main__":
    for nome, fn in (("capa_A_sumiu_uma_raiz", capa_sumiu), ("capa_B_sinal_coeficiente", capa_tabela),
                     ("capa_C_alguem_e_zero", capa_nulo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
