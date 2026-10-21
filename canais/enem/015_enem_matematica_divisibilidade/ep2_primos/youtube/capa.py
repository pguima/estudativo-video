"""Capas — Matemática ENEM, Divisibilidade, Episódio 2: números primos (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep2_primos", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 2", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def maxbox(s, x, maxw, size):
    """reduz a fonte da caixa colorida até caber antes do cartão"""
    while text_w(s, "black", size) + 68 > maxw:
        size -= 4
    return size


def capa_um(c):
    background(c); selo(c); painel(c)
    for k, n in enumerate(("1", "2")):
        y = 200 + k * 380
        text(c, n, 1330, y + 230, 260, "black", BLUE)
        text(c, "?", 1600, y + 230, 220, "black", AMBER)
    big(c, "O 1 É PRIMO?", 340)
    big(c, "E O 2?", 470)
    boxed(c, "PEGADINHA", 70, 520, maxbox("PEGADINHA", 70, 1000, 150), AMBER)
    text(c, "números primos do zero, sem decoreba", 90, 860, 50, "extrabold", INK2, align="left")


class _AllDone(dict):
    def __getitem__(self, k):
        return -100.0


def capa_crivo(c):
    background(c); selo(c); painel(c)
    V.crivo(c, 0, _AllDone(), 1160, 200, 62, 1.0, 1.0)
    text(c, "1 a 100", 1470, 880, 44, "black", GREEN)
    big(c, "OS 25 PRIMOS", 340)
    big(c, "ATÉ 100", 470)
    boxed(c, "EM 1 PENEIRA", 70, 520, maxbox("EM 1 PENEIRA", 70, 1000, 140), GREEN)
    text(c, "o crivo e o teste da raiz quadrada", 90, 860, 50, "extrabold", INK2, align="left")


def capa_tijolos(c):
    background(c); selo(c); painel(c)
    for k, n in enumerate((2, 3, 5, 7, 11, 13)):
        V.tijolo(c, 1190 + (k % 2) * 290, 220 + (k // 2) * 220, 260, 150, n, 1.0)
    big(c, "PRIMOS SÃO", 340)
    big(c, "OS TIJOLOS", 470)
    boxed(c, "DOS NÚMEROS", 70, 520, maxbox("DOS NÚMEROS", 70, 1000, 140), V.BRICK)
    text(c, "o que é primo, composto e o caso do 1", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_o_1_e_primo", capa_um), ("capa_B_25_primos", capa_crivo), ("capa_C_tijolos", capa_tijolos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
