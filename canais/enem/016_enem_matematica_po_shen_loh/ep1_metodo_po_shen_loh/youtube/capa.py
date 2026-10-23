"""Capas — Equação do 2º grau, Episódio 1: o método de Po-Shen Loh (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_016_ep1", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def big(c, s, y, maxw=1000, size=140):
    while V.ftext_w(s, "black", size) > maxw:
        size -= 4
    V.ftext(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = V.ftext_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    V.fmid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA ENEM · PO-SHEN LOH", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_sem_bhaskara(c):
    background(c); selo(c); painel(c)
    V.fbox(c, "x² − 8x + 12 = 0", 1470, 230, 48, 1.0, INK)
    V.bhaskara_formula(c, 1450, 360, 1.0, 40, GRAY)
    line(c, 1250, 410, 1650, 310, RED, 1.0, 9)
    X = V.reta(c, 1200, 1740, 760, 0, 8, 1.0)
    V.gangorra(c, X, 760, 4, 2, 1.0, show_val=1.0, col_ok=GREEN, h=150, s=1.5)
    big(c, "2º GRAU EM", 340)
    big(c, "3 PASSOS", 470)
    boxed(c, "SEM BHASKARA", 70, 520, 130, GREEN)
    text(c, "o método de Po-Shen Loh, do zero", 90, 860, 50, "extrabold", INK2, align="left")


def capa_gangorra(c):
    background(c); selo(c); painel(c)
    text(c, "raízes = média ± u", 1470, 240, 46, "black", PURPLE)
    X = V.reta(c, 1200, 1740, 640, 0, 8, 1.0)
    V.gangorra(c, X, 640, 4, 2, 1.0, show_u=1.0, show_val=1.0, h=210, s=1.7, labels=["m − u", "m + u"])
    V.fbox(c, "2 e 6", 1470, 860, 60, 1.0, GREEN)
    big(c, "AS RAÍZES", 340)
    big(c, "NUMA", 470)
    boxed(c, "GANGORRA", 70, 520, 150, BLUE)
    text(c, "equação do 2º grau sem decorar fórmula", 90, 860, 48, "extrabold", INK2, align="left")


def capa_receita(c):
    background(c); selo(c); painel(c)
    text(c, "x² + bx + c = 0", 1470, 230, 46, "black", INK)
    rows = [("1", "m = −b/2", PURPLE), ("2", "u² = m² − c", PURPLE), ("3", "m − u  e  m + u", GREEN)]
    for k, (n, s, col) in enumerate(rows):
        y = 370 + k * 190
        rrect(c, 1170, y - 70, 600, 140, 26, mix("#FFFFFF", col, 0.10))
        badge_num(c, n, 1240, y, 1, 38, bg=col)
        V.fmid(c, s, 1300, y, 58, "black", col, align="left")
    V.fmid(c, "x² − 8x + 12 = 0  →  4 ± 2", 1470, 870, 38, "black", INK2)
    big(c, "O MÉTODO DE", 340)
    big(c, "PO-SHEN LOH", 470)
    boxed(c, "MÉDIA ± u", 70, 520, 150, PURPLE)
    text(c, "as raízes em 3 passos, sem Bhaskara", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_sem_bhaskara", capa_sem_bhaskara), ("capa_B_gangorra", capa_gangorra),
                     ("capa_C_media_mais_menos_u", capa_receita)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
