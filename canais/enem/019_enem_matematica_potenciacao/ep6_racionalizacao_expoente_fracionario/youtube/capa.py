"""Capas — Potenciação e Radiciação, Episódio 6: racionalização e expoente fracionário (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 6", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_mesmo(c):
    background(c); selo(c); painel(c)
    K.expr(c, "1/√{2}", 1470, 310, 115, 1)
    K.fmid(c, "=", 1470, 520, 110, "black", GREEN)
    K.expr(c, "√{2}/2", 1470, 730, 115, 1, cores={0: GREEN})
    V.mascara(c, 1470, 890, 130, 1)
    big(c, "1/√2 OU √2/2?", 340)
    big(c, "VOCÊ NÃO ERROU:", 470)
    boxed(c, "É O MESMO NÚMERO", 70, 520, 120, GREEN)
    text(c, "racionalização do zero, com o 1 disfarçado", 90, 860, 40, "extrabold", INK2, align="left")


def capa_maior(c):
    background(c); selo(c); painel(c)
    for k, (s, r) in enumerate((("√{2}", "√[6]{8}"), ("√[3]{3}", "√[6]{9}"), ("√[6]{10}", "√[6]{10}"))):
        y = 290 + k * 230
        K.expr(c, s, 1340, y, 110, 1)
        K.fmid(c, "→", 1510, y, 60, "black", GRAY)
        K.expr(c, r, 1660, y, 90, 1, cores={0: GREEN})
    K.fmid(c, "8 < 9 < 10", 1470, 900, 56, "black", GREEN)
    big(c, "QUAL É MAIOR?", 340)
    big(c, "√2, ³√3 OU ⁶√10", 470)
    boxed(c, "A RESPOSTA SURPREENDE", 70, 520, 110, AMBER)
    text(c, "compare raízes de índices diferentes", 90, 860, 40, "extrabold", INK2, align="left")


def capa_tradutor(c):
    background(c); selo(c); painel(c)
    V.tradutor_icone(c, 1470, 270, 170, 1)
    V.tradutor(c, 1270, 1630, 560, 130, "8", "2", "3", 1, 1.0, 1.0)
    K.fmid(c, "=", 1420, 560, 90, "black", INK)
    K.fmid(c, "= 4", 1470, 800, 120, "black", GREEN)
    big(c, "RAIZ VIRA", 340)
    big(c, "POTÊNCIA", 470)
    boxed(c, "EMBAIXO VIRA ÍNDICE", 70, 520, 120, PURPLE)
    text(c, "o tradutor que multiplica e compara raízes", 90, 860, 40, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_mesmo_numero", capa_mesmo), ("capa_B_qual_e_maior", capa_maior),
                     ("capa_C_raiz_vira_potencia", capa_tradutor)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
