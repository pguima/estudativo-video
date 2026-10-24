"""Capas — Grandezas Proporcionais, Episódio 4: várias grandezas ao mesmo tempo (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · GRANDEZAS · EP. 4", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_guia(c):
    background(c); selo(c); painel(c)
    text(c, "A FRAÇÃO-GUIA", 1470, 220, 40, "black", INK2)
    V.andares(c, 1470, 470, 1.0, cima=[("DIRETO", 1.0)], baixo=[("INVERSO", 1.0)], pre=None, w=520, size=52, lado=False)
    K.expr(c, "R = k · L/A", 1470, 780, 80, 1.0, cores={2: PURPLE})
    text(c, "o fio elétrico", 1470, 890, 34, "black", GRAY)
    big(c, "DIRETO EM CIMA,", 330)
    big(c, "INVERSO", 470)
    boxed(c, "EMBAIXO", 70, 520, 170, PURPLE)
    text(c, "monte qualquer fórmula a partir do enunciado", 90, 860, 44, "extrabold", INK2, align="left")


def capa_efeitos(c):
    background(c); selo(c); painel(c)
    K.expr(c, "y = k · a/b", 1470, 300, 100, 1.0, cores={2: PURPLE})
    K.ftext(c, "a × 2", 1300, 500, 64, "black", GREEN)
    K.ftext(c, "b × 3", 1640, 500, 64, "black", BLUE)
    K.ftext(c, "y × ?", 1470, 700, 110, "black", PURPLE)
    text(c, "multiplique, não some", 1470, 870, 38, "black", AMBER)
    big(c, "DUAS COISAS", 330)
    big(c, "MUDAM JUNTAS.", 470)
    boxed(c, "E AGORA?", 70, 520, 170, AMBER)
    text(c, "o jeito certo de juntar vários efeitos", 90, 860, 44, "extrabold", INK2, align="left")


def capa_fisica(c):
    background(c); selo(c); painel(c)
    for k, (s, txt, col) in enumerate((("v = d/t", "d direta · t inversa", GREEN), ("F = m · a", "tudo direto", GREEN),
                                       ("P · V = k", "inversas", BLUE))):
        y = 240 + k * 240
        K.expr(c, s, 1470, y, 84, 1.0, cores={i: INK for i in range(len(s.split()))})
        text(c, txt, 1470, y + 125, 34, "black", col)
    big(c, "FÓRMULA DE FÍSICA", 330)
    big(c, "SEM DECORAR:", 470)
    boxed(c, "LEIA EM VOZ ALTA", 70, 520, 140, GREEN)
    text(c, "toda fórmula é uma frase sobre proporção", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_direto_em_cima", capa_guia), ("capa_B_mudam_juntas", capa_efeitos),
                     ("capa_C_fisica_sem_decorar", capa_fisica)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
