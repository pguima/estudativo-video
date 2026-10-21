"""Capas — Compreensão Global e Tese, Episódio 3: As 5 alternativas-armadilha (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep3", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)


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
    pill(c, "LINGUAGENS ENEM · EPISÓDIO 3", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_moldes(c):
    background(c); selo(c); painel(c)
    for k, (nome, roupa) in enumerate(V.TRAPS):
        y = 220 + k * 146
        badge_num(c, k + 1, 1200, y, 1, 30, bg=AMBER, fg=INK)
        size = 34 if len(nome) < 14 else 26
        text(c, nome, 1250, y + 12, size, "black", INK, align="left")
        text(c, roupa, 1250, y + 54, 24, "bold", GRAY, align="left")
    big(c, "AS ERRADAS", 340)
    big(c, "SEGUEM SÓ", 470)
    boxed(c, "5 MOLDES", 70, 520, 160, AMBER, INK)
    text(c, "as alternativas-armadilha do ENEM", 90, 860, 50, "extrabold", INK2, align="left")


def capa_passos(c):
    background(c); selo(c); painel(c)
    for k, (_, s, _) in enumerate(V.PASSOS):
        y = 220 + k * 120
        badge_num(c, k + 1, 1200, y, 1, 30, bg=PURPLE)
        size = 34
        while text_w(s, "black", size) > 470:
            size -= 2
        text(c, s, 1250, y + 12, size, "black", INK, align="left")
        check_icon(c, 1760, y, 22, 1, GREEN)
    big(c, "ELIMINE EM", 340)
    big(c, "SEGUNDOS COM", 470)
    boxed(c, "6 PASSOS", 70, 520, 160, PURPLE)
    text(c, "o método para interpretação de texto", 90, 860, 50, "extrabold", INK2, align="left")


def capa_verdade(c):
    background(c); selo(c); painel(c)
    V.guarda_roupa(c, 1180, 230, 300, 420, 1)
    V.camisa(c, 1620, 400, 110, PURPLE, 1)
    check_icon(c, 1620, 600, 40, 1, RED, "x")
    text(c, "em que linha", 1470, 790, 52, "black", PURPLE)
    text(c, "isso está?", 1470, 860, 52, "black", PURPLE)
    big(c, "É VERDADE,", 340)
    big(c, "MAS NÃO ESTÁ", 470)
    boxed(c, "NO TEXTO", 70, 520, 160, RED)
    text(c, "a armadilha mais traiçoeira do ENEM", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_5_moldes", capa_moldes), ("capa_B_6_passos", capa_passos), ("capa_C_verdade_do_mundo", capa_verdade)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
