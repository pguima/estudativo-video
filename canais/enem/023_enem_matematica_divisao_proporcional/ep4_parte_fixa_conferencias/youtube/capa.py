"""Capas — Divisão Proporcional, Episódio 4: parte fixa e as 3 conferências (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep4", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · DIVISÃO PROPORCIONAL · EP. 4", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_fixa(c):
    background(c); selo(c); painel(c)
    text(c, "1  SEPARE O FIXO", 1470, 210, 36, "black", V.NOTA_ESC)
    for k in range(3):
        V.montinho(c, 1300 + k * 170, 320, 130, 1.0, "")
    text(c, "2  DIVIDA SÓ O RESTO", 1470, 470, 36, "black", PURPLE)
    V.pacotes(c, 0, 1300, 570, 6, 1.0, None, s=64, gap=74)
    text(c, "3  DEVOLVA O FIXO", 1470, 710, 36, "black", GREEN)
    check_icon(c, 1470, 800, 40, 1.0, GREEN)
    big(c, "PARTE FIXA?", 330)
    big(c, "SEPARE ANTES,", 470)
    boxed(c, "DIVIDA SÓ O RESTO", 70, 520, 130, NOTA)
    text(c, "quando a proporção não vale sobre o total", 90, 860, 44, "extrabold", INK2, align="left")


def capa_caixa(c):
    background(c); selo(c); painel(c)
    V.registradora(c, 1470, 520, 420, 1.0, "2 002", False, 1.0)
    text(c, "o total era 2 000", 1470, 880, 40, "black", RED)
    big(c, "CALCULOU CERTO", 330)
    big(c, "E ERROU?", 470)
    boxed(c, "FECHE O CAIXA", 70, 520, 150, GREEN)
    text(c, "some as partes antes de marcar a alternativa", 90, 860, 44, "extrabold", INK2, align="left")


def capa_tres(c):
    background(c); selo(c); painel(c)
    rows = [("1", "a soma fecha o caixa?", GREEN), ("2", "a ordem faz sentido?", PURPLE), ("3", "é a parte que pediram?", AMBER)]
    for k, (n, s, col) in enumerate(rows):
        y = 290 + k * 210
        badge_num(c, int(n), 1200, y - 14, 1.0, 44, bg=col)
        text(c, s, 1260, y, 36, "black", INK, align="left")
    big(c, "3 CONFERÊNCIAS", 330)
    big(c, "QUE PEGAM", 470)
    boxed(c, "QUASE TODO ERRO", 70, 520, 140, PURPLE)
    text(c, "chega de resposta \"quase certa\"", 90, 860, 44, "extrabold", INK2, align="left")


NOTA = V.NOTA

if __name__ == "__main__":
    for nome, fn in (("capa_A_separe_o_fixo", capa_fixa), ("capa_B_feche_o_caixa", capa_caixa),
                     ("capa_C_tres_conferencias", capa_tres)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
