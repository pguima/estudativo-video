"""Capas — Potenciação e Radiciação, Episódio 2: As sete propriedades (tema claro). 3 variações em 1280x720."""
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


def capa_sete(c):
    background(c); selo(c); painel(c)
    for k in range(7):
        x = 1230 + (k % 4) * 160 + (80 if k >= 4 else 0)
        y = 200 + (k // 4) * 160
        rrect(c, x - 62, y - 62, 124, 124, 22, "#F7F7F5", 1)
        badge_num(c, k + 1, x, y, 1, 46, bg=PURPLE)
    K.expr(c, "2^3 · 2^4 = 2^7", 1470, 620, 90, 1, cores={4: GREEN})
    K.expr(c, "(2^3)^2 = 2^6", 1470, 800, 90, 1, cores={2: GREEN})
    big(c, "7 REGRAS DE", 340)
    big(c, "POTÊNCIA SEM", 470)
    boxed(c, "DECORAR", 70, 520, 160, PURPLE)
    text(c, "cada propriedade aberta, uma por uma", 90, 860, 46, "extrabold", INK2, align="left")


def capa_falsa(c):
    background(c); selo(c); painel(c)
    K.expr(c, "2^2 + 2^3 = 12", 1470, 300, 90, 1, cores={4: GREEN})
    K.fmid(c, "≠", 1470, 470, 130, "black", RED)
    K.expr(c, "2^5 = 32", 1470, 640, 100, 1, cores={2: RED})
    K.selo_teste(c, 1470, 830, 1)
    big(c, "2² + 2³ = 2⁵?", 340)
    big(c, "ESSA REGRA", 470)
    boxed(c, "NÃO EXISTE", 70, 520, 150, RED)
    text(c, "teste com 2 e 3 e nunca mais caia", 90, 860, 46, "extrabold", INK2, align="left")


def capa_base(c):
    background(c); selo(c); painel(c)
    K.expr(c, "{2^5·4^3}/8^2", 1470, 330, 110, 1)
    K.expr(c, "4 = 2^2", 1470, 530, 64, 1, cores={2: GREEN})
    K.expr(c, "8 = 2^3", 1470, 630, 64, 1, cores={2: GREEN})
    K.expr(c, "= 2^5 = 32", 1470, 800, 100, 1, cores={3: GREEN})
    big(c, "PRIMEIRO,", 340)
    big(c, "TUDO NA", 470)
    boxed(c, "MESMA BASE", 70, 520, 150, GREEN)
    text(c, "o movimento que destrava a expressão", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_sete_sem_decorar", capa_sete), ("capa_B_regra_que_nao_existe", capa_falsa),
                     ("capa_C_mesma_base", capa_base)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
