"""Capas — Divisibilidade, Primos, MMC e MDC, Episódio 6: MMC ou MDC? (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep6", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def big(c, s, y, maxw=1000, size=140):
    while text_w(s, "black", size) > maxw:
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 6", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_repete(c):
    background(c); selo(c)
    V.lado_repete(c, 1130, 150, 680, 380, 1, 1.2)
    V.lado_reparte(c, 1130, 560, 680, 380, 1, 1.2)
    big(c, "MMC OU MDC?", 340)
    big(c, "DECIDA EM", 470)
    boxed(c, "10 SEGUNDOS", 70, 520, 120, PURPLE)
    text(c, "repete ou reparte: a pergunta que decide", 90, 860, 46, "extrabold", INK2, align="left")


def capa_escolha(c):
    background(c); selo(c); painel(c)
    rrect(c, 1180, 220, 580, 260, 24, mix("#FFFFFF", GREEN, 0.10))
    text(c, "CONTA", 1470, 290, 40, "black", GREEN)
    check_icon(c, 1470, 400, 56, 1, GREEN)
    rrect(c, 1180, 560, 580, 260, 24, mix("#FFFFFF", RED, 0.10))
    text(c, "ESCOLHA", 1470, 630, 40, "black", RED)
    check_icon(c, 1470, 740, 56, 1, RED, "x")
    big(c, "A CONTA ESTAVA", 340)
    big(c, "CERTA. E VOCÊ", 470)
    boxed(c, "ERROU", 70, 520, 150, RED)
    text(c, "o erro que derruba quem sabe MMC e MDC", 90, 860, 46, "extrabold", INK2, align="left")


def capa_cerca(c):
    background(c); selo(c); painel(c)
    V.cerca(c, 1190, 330, 560, 1.0, 14, cotas=True, cont=False)
    text(c, "84 m?", 1290, 680, 64, "black", RED)
    check_icon(c, 1430, 660, 28, 1, RED, "x")
    text(c, "168 m", 1630, 680, 64, "black", GREEN)
    text(c, "14 estacas", 1470, 820, 56, "black", V.PAR)
    big(c, "QUANTAS", 340)
    big(c, "ESTACAS NA", 470)
    boxed(c, "CERCA?", 70, 520, 150, AMBER)
    text(c, "a pegadinha do perímetro no ENEM", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_repete_ou_reparte", capa_repete), ("capa_B_conta_certa", capa_escolha),
                     ("capa_C_estacas", capa_cerca)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
