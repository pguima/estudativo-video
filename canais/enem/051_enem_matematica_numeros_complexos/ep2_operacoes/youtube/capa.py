"""Capas — Números Complexos, Episódio 2: as operações (tema claro). 3 variações em 1280x720.
Formatos: A = o produto gigante com "= ?" e a cabine do pedágio "i² = −1" numa faixa roxa; B = o espelho: 3 + 4i em cima,
a linha tracejada e o reflexo com o sinal em "?", título à esquerda; C = fundo escuro com a fração (3 + i)/(1 − i) gigante e
"= ?". Nenhuma mostra gabarito."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep2", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")
RE, IM = V.RE, V.IM


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, col=BLUE):
    s = "MATEMÁTICA ENEM · NÚMEROS COMPLEXOS · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, col, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, col, size=34, anchor="center", bounds=(0, 1920))


def capa_pedagio(c):
    background(c); selo_topo(c, W / 2)
    V.linha(c, V.cx_("2", "+ 3i", True) + [(" · ", INK)] + V.cx_("1", "− i", True) + [("  = ?", INK)], W / 2, 300, 140,
            1.0)
    shadow_rrect(c, 200, 480, 1520, 330, 40, 1, 1.4)
    rrect(c, 200, 480, 1520, 330, 40, PURPLE)
    V.cancela(c, 380, 690, 1.0, 0.0, 1.6)
    s = "O PEDÁGIO DO i²"
    text_mid(c, s, 1150, 600, fit(s, 120, 900), "black", "#FFFFFF")
    text_mid(c, "todo i² vira −1", 1150, 720, 70, "extrabold", "#FFFFFF")
    V.selo(c, 1600, 920, 1.0, "VOCÊ ESQUECE?", AMBER, -6, 54)


def capa_espelho(c):
    background(c); selo_topo(c)
    s = "O ESPELHO"
    text(c, s, 84, 330, fit(s, 170, 900), "black", INK, align="left")
    text(c, "do número complexo", 90, 420, 60, "extrabold", BLUE, align="left")
    text(c, "conjugado · z barra", 90, 500, 50, "bold", INK2, align="left")
    cx = 1420
    V.linha(c, V.cx_("3", "+ 4i"), cx, 330, 150, 1.0)
    line(c, cx - 400, 530, cx + 400, 530, "#9FC6E8", 1, 10, dash=[30, 18])
    V.linha(c, [("3", RE), (" ? 4i", IM)], cx, 730, 150, 1.0)
    rrect(c, 120, 760, 820, 150, 36, mix("#FFFFFF", GREEN, 0.18))
    text_mid(c, "troca o quê?", 530, 835, 80, "black", GREEN)


def capa_andar(c):
    c.drawRect(skia.Rect.MakeWH(W, H), paint("#1B1A2E"))
    selo_topo(c, W / 2, PURPLE)
    s = "DIVIDIR COM i EMBAIXO?"
    text(c, s, W / 2, 290, fit(s, 120, 1700), "black", "#FFFFFF")
    V.linha(c, [("3", "#6FA8FF"), (" + i", "#B79CFF")], 820, 520, 150, 1.0)
    rrect(c, 520, 610, 600, 16, 8, "#FFFFFF")
    V.linha(c, [("1", "#6FA8FF"), (" − i", "#B79CFF")], 820, 760, 150, 1.0)
    text_mid(c, "= ?", 1360, 680, 170, "black", AMBER)
    text(c, "limpe o andar de baixo", W / 2, 990, 64, "extrabold", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_pedagio", capa_pedagio), ("capa_B_espelho", capa_espelho),
                     ("capa_C_andar_de_baixo", capa_andar)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
