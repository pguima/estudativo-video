"""Capas — Sistemas de Equações Lineares, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos: A = a frase "Ana tem o triplo de Bruno" virando DUAS traduções com "?" (qual é a certa?), com "A TRADUÇÃO
DECIDE"; B = os trilhos paralelos gigantes com "0 = 2" e "ERREI A CONTA?"; C = duas notas fiscais se juntando, com
"PEDIRAM x + y?" e "não resolva tudo". Nenhuma mostra gabarito."""
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
    s = "MATEMÁTICA ENEM · SISTEMAS · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_traducao(c):
    background(c)
    rrect(c, 0, H * 0.56, W, H * 0.44, 0, mix("#FFFFFF", PURPLE, 0.12))
    selo_topo(c)
    s = "“Ana tem o TRIPLO de Bruno”"
    text(c, s, W / 2, 330, fit(s, 104, 1700), "black", INK)
    for x, eq, col in ((560, "a = 3b", BLUE), (1360, "3a = b", AMBER)):
        arrow(c, W / 2, 390, x, 560, INK2, 1, 8, 26)
        rrect(c, x - 290, 600, 580, 230, 40, "#FFFFFF", 1, shadow=True)
        V.mx(c, eq, x - 40, 715, 130, col, 1.0, align="center")
        text_mid(c, "?", x + 210, 715, 130, "black", RED, 1)
    s = "A TRADUÇÃO DECIDE"
    text(c, s, W / 2, 1000, fit(s, 120, 1700), "black", PURPLE)


def capa_trilhos(c):
    background(c)
    rrect(c, W * 0.5, 0, W * 0.5, H, 0, mix("#FFFFFF", RED, 0.10))
    selo_topo(c)
    s1, s2 = "DEU 0 = 2.", "ERREI A CONTA?"
    text(c, s1, 500, 440, fit(s1, 170, 860), "black", RED, align="center")
    text(c, s2, 500, 620, fit(s2, 130, 860), "black", INK, align="center")
    text(c, "9 pegadinhas · 5 questões", 500, 790, 60, "black", INK2, align="center")
    c.save(); c.translate(1440, 560); c.rotate(-12); c.scale(2.0, 2.0)
    for k in range(11):
        x = -230 + k * 46
        rrect(c, x - 10, -120, 20, 240, 5, V.CERCA, 1)
    for y in (-70, 70):
        line(c, -260, y, 260, y, INK2, 1, 16)
    c.restore()


def capa_notas(c):
    background(c); selo_topo(c, W / 2)
    s = "PEDIRAM x + y?"
    text(c, s, W / 2, 300, fit(s, 150, 1700), "black", INK)
    c.save(); c.translate(W / 2, 620); c.scale(2.3, 2.3)
    V.nota_fiscal(c, -250, -110, 1, ["3 P", "1 R"], "R$ ?", BLUE)
    V.fmid(c, "+", 0, -10, 90, "black", GREEN, 1)
    V.nota_fiscal(c, 100, -110, 1, ["1 P", "3 R"], "R$ ?", PURPLE)
    c.restore()
    s = "não resolva tudo"
    pill(c, s, W / 2, 1000, GREEN, size=64, anchor="center", bounds=(0, 1920))


if __name__ == "__main__":
    for nome, fn in (("capa_A_a_traducao_decide", capa_traducao), ("capa_B_errei_a_conta", capa_trilhos),
                     ("capa_C_pediram_x_mais_y", capa_notas)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
