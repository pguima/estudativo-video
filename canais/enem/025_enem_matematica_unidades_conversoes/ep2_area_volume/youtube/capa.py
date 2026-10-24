"""Capas — Unidades de Medida e Conversões, Episódio 2: área e volume, litro e metro cúbico (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · UNIDADES · EP. 2", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_mil(c):
    background(c); selo(c); painel(c)
    V.caixa_iso(c, 1470, 560, 250, 1, 1, 1, 1.0, cores=("#FFFFFF", "#F1F1EA", "#E2E2DA"), div=10, borda="#9A9A90")
    text(c, "1 m³", 1470, 230, 64, "black", INK)
    text(c, "= 1 000 caixinhas de 1 L", 1470, 900, 38, "black", GREEN)
    big(c, "1 m³ NÃO É", 330)
    big(c, "1 LITRO:", 470)
    boxed(c, "SÃO 1 000", 70, 520, 160, RED)
    text(c, "área, volume e litro sem cair na armadilha", 90, 860, 44, "extrabold", INK2, align="left")


def capa_leite(c):
    background(c); selo(c); painel(c)
    V.caixa_leite(c, 1310, 760, 160, 320, 1.0)
    V.caixa_iso(c, 1600, 640, 150, 1, 1, 1, 1.0, cores=("#FFFFFF", "#F1F1EA", "#E2E2DA"), div=0, borda="#9A9A90")
    text(c, "10 cm", 1600, 860, 34, "black", INK2)
    text(c, "1 L = 1 dm³", 1470, 250, 64, "black", PURPLE)
    big(c, "O LITRO QUE", 330)
    big(c, "VOCÊ JÁ", 470)
    boxed(c, "SEGUROU NA MÃO", 70, 520, 140, BLUE)
    text(c, "a caixa de leite explica o que é um litro", 90, 860, 44, "extrabold", INK2, align="left")


def capa_degraus(c):
    background(c); selo(c); painel(c)
    rows = [("comprimento", "× 10", INK), ("área", "× 100", BLUE), ("volume", "× 1 000", PURPLE)]
    text(c, "cada degrau da escada:", 1470, 240, 36, "black", INK2)
    for k, (s, f, col) in enumerate(rows):
        y = 370 + k * 170
        text(c, s, 1250, y, 50, "black", col, align="left")
        text(c, f, 1760, y, 64, "black", col, align="right")
    big(c, "ÁREA E VOLUME", 330)
    big(c, "SEM DECORAR:", 470)
    boxed(c, "CONTE OS DEGRAUS", 70, 520, 130, PURPLE)
    text(c, "m², hectare, m³ e litro do zero", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_nao_e_um_litro", capa_mil), ("capa_B_caixa_de_leite", capa_leite),
                     ("capa_C_conte_os_degraus", capa_degraus)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
