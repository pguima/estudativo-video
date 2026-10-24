"""Capas — Frações, Decimais e Dízimas, Episódio 2: Números mistos e qual fração é maior (tema claro). 3 variações em 1280x720."""
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
K = V.K


def big(c, s, y, maxw=1000, size=140):
    while text_w(s, "black", size) > maxw:
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34, maxw=1000):
    while text_w(s, "black", size) + pad * 2 > maxw:
        size -= 4
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 2", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)



def capa_qual_maior(c):
    background(c); selo(c); painel(c)
    K.pizza(c, 1315, 360, 125, 5, 3, 1.0, pull=0.6)
    K.pizza(c, 1625, 360, 125, 7, 3, 1.0, pull=0.6)
    K.fr(c, "3", "5", 1315, 600, 80, GREEN)
    K.fr(c, "3", "7", 1625, 600, 80, INK)
    K.fmid(c, ">", 1470, 600, 100, "black", GREEN)
    text(c, "menos gente, fatia maior", 1470, 860, 36, "black", INK2)
    big(c, "3/7 OU 3/5?", 340)
    big(c, "QUAL É", 470)
    boxed(c, "MAIOR?", 70, 520, 160, AMBER)
    text(c, "não é o do número maior: veja com pizza", 90, 860, 46, "extrabold", INK2, align="left")


def capa_misto(c):
    background(c); selo(c); painel(c)
    for k, s_ in enumerate((4, 4, 3)):
        K.pizza(c, 1270 + k * 200, 330, 90, 4, s_, 1.0, gone={3} if k == 2 else None)
    K.expr(c, "2|3/4 = 11/4", 1470, 600, 100, 1.0, cores={2: PURPLE})
    text(c, "11 fatias de quarto", 1470, 830, 40, "black", INK2)
    big(c, "NÚMERO MISTO", 340)
    big(c, "SEM ERRAR", 470)
    boxed(c, "NAS CONTAS", 70, 520, 140, PURPLE)
    text(c, "converter, voltar e a regra de ouro", 90, 860, 46, "extrabold", INK2, align="left")


def capa_ordem(c):
    background(c); selo(c); painel(c)
    for k, (f, d) in enumerate((("7/11", "0,636"), ("5/8", "0,625"), ("3/5", "0,600"))):
        y = 290 + k * 200
        n_, d_ = f.split("/")
        K.fr(c, n_, d_, 1330, y, 80, INK)
        text(c, d, 1580, y + 22, 64, "black", GREEN)
    big(c, "COLOQUE FRAÇÕES", 340)
    big(c, "EM ORDEM", 470)
    boxed(c, "SEM CHUTE", 70, 520, 150, GREEN)
    text(c, "em X, em decimal e com a metade", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_qual_e_maior", capa_qual_maior), ("capa_B_numero_misto", capa_misto),
                     ("capa_C_em_ordem", capa_ordem)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
