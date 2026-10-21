"""Capas — Compreensão Global e Tese, Episódio 6: A tese implícita (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep6", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "LINGUAGENS ENEM · EPISÓDIO 6", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_sem_dizer(c):
    background(c); selo(c); painel(c)
    V.tv(c, 1470, 330, 520, 270, 1)
    text_mid(c, "×", 1470, 560, 90, "black", GREEN)
    V.relogio(c, 1470, 780, 120, 11, 1)
    pill(c, "6 HORAS", 1680, 680, RED, size=36, anchor="center", bounds=(0, 1920))
    big(c, "SEM DIZER", 340)
    big(c, "“EU DEFENDO”", 470)
    boxed(c, "TEM TESE", 70, 520, 150, BLUE)
    text(c, "a tese implícita no ENEM", 90, 860, 50, "extrabold", INK2, align="left")


def capa_ironia(c):
    background(c); selo(c); painel(c)
    text(c, "Admiro", 1470, 380, 120, "black", GREEN)
    strike(c, 1260, 340, 1680, 340, 1, RED)
    V.virada(c, "Admiro", "Critico", 1470, 620, 120, 1.0, 1)
    arrow(c, 1470, 440, 1470, 530, GRAY, 1, 6, 22)
    text(c, "elogia para criticar", 1470, 820, 40, "black", INK2)
    big(c, "ELOGIO", 340)
    big(c, "IRÔNICO É", 470)
    boxed(c, "CRÍTICA", 70, 520, 160, RED)
    text(c, "não leia a ironia ao pé da letra", 90, 860, 50, "extrabold", INK2, align="left")


def capa_fotografo(c):
    background(c); selo(c); painel(c)
    V.foto(c, 1200, 220, 540, 400, 1)
    V.visor(c, 1180, 200, 580, 440, 1, AMBER, 60, 9)
    V.camera(c, 1470, 790, 1.1, 1)
    big(c, "A OPINIÃO", 340)
    big(c, "ESTÁ NA", 470)
    boxed(c, "ESCOLHA", 70, 520, 160, PURPLE)
    text(c, "o autor é um fotógrafo", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_sem_dizer", capa_sem_dizer), ("capa_B_ironia", capa_ironia), ("capa_C_fotografo", capa_fotografo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
