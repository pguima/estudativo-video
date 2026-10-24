"""Capas — Notação Científica, Episódio 3: Somar e comparar (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · NOTAÇÃO CIENTÍFICA · EP. 3", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 160, 700, 800, r=36)


def capa_soma(c):
    background(c); selo(c); painel(c)
    for k in range(3):
        V.nota(c, 1180 + k * 26, 220 + k * 30, 300, 130, "R$ 100", V.NOTA100, 1)
    for k in range(8):
        V.nota(c, 1540 + (k % 2) * 120, 220 + (k // 2) * 64, 108, 56, "10", V.NOTA10, 1)
    K.ftext(c, "300 mil + 80 mil", 1470, 580, 60, "black", INK2)
    K.expr(c, "3,8·10^5", 1470, 760, 120, 1, cores={0: GREEN})
    big(c, "3·10⁵ + 8·10⁴", 330)
    big(c, "NÃO DÁ", 470)
    boxed(c, "11·10⁵", 70, 520, 150, RED)
    text(c, "somar em notação científica sem errar", 90, 860, 46, "extrabold", INK2, align="left")


def capa_comparar(c):
    background(c); selo(c); painel(c)
    V.terra(c, 1470, 500, 250, 1)
    V.luas_na_terra(c, 1470, 500, 250, 80, 1, rl=19)
    rrect(c, 1290, 790, 360, 120, 24, "#FFFFFF", 1, shadow=True)
    text_mid(c, "80 vezes", 1470, 850, 64, "black", GREEN)
    big(c, "QUANTAS VEZES", 330)
    big(c, "OU QUANTO?", 470)
    boxed(c, "DIVIDE × SUBTRAI", 70, 520, 120, PURPLE)
    text(c, "comparar grandezas sem cair na pegadinha", 90, 860, 46, "extrabold", INK2, align="left")


def capa_nota(c):
    background(c); selo(c); painel(c)
    for k in range(8):
        V.nota(c, 1190 + (k % 4) * 140, 230 + (k // 4) * 90, 126, 78, "10", V.NOTA10, 1)
    K.fmid(c, "↓", 1470, 470, 90, "black", AMBER)
    V.nota(c, 1270, 540, 400, 170, "R$ 100", V.NOTA100, 1, fill=0.8)
    K.expr(c, "8·10^4 = 0,8·10^5", 1470, 830, 64, 1, cores={2: GREEN})
    big(c, "ANTES DE SOMAR,", 330)
    big(c, "TROQUE PELA", 470)
    boxed(c, "MESMA NOTA", 70, 520, 150, GREEN)
    text(c, "o passo que a maioria pula", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_nao_da_11", capa_soma), ("capa_B_vezes_ou_quanto", capa_comparar),
                     ("capa_C_mesma_nota", capa_nota)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
