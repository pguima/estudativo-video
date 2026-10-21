"""Capas — Redação ENEM, Leitura da Proposta, Episódio 4: tangenciamento e fuga ao tema (tema claro). 3 variações em 1280x720."""
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
    pill(c, "REDAÇÃO ENEM · EPISÓDIO 4", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_480(c):
    background(c); selo(c); painel(c)
    text(c, "TANGENCIOU", 1470, 250, 44, "black", AMBER)
    V.placar(c, 1180, 360, 400, 1, cap=1)
    text(c, "−480", 1470, 880, 80, "black", RED)
    big(c, "TANGENCIAR", 340)
    big(c, "CUSTA ATÉ", 470)
    boxed(c, "480 PONTOS", 70, 520, 140, AMBER)
    text(c, "o erro silencioso da redação do ENEM", 90, 860, 50, "extrabold", INK2, align="left")


def capa_bairro(c):
    background(c); selo(c); painel(c)
    V.mapa(c, 1150, 330, 0.455, 1, (1, 1, 1), bairro=1)
    for k, (nm, col) in enumerate((V.SIT["ok"], V.SIT["tg"], V.SIT["fg"])):
        pill(c, nm, 1470, 680 + k * 80, col, size=32, anchor="center", bounds=(0, 1920))
    big(c, "BAIRRO CERTO,", 340)
    big(c, "CASA ERRADA:", 470)
    boxed(c, "TANGENCIOU", 70, 520, 124, AMBER)
    text(c, "tangenciamento × fuga ao tema no ENEM", 90, 860, 50, "extrabold", INK2, align="left")


def capa_zero(c):
    background(c); selo(c); painel(c)
    text(c, "FUGA AO TEMA", 1470, 250, 44, "black", RED)
    V.placar(c, 1180, 360, 400, 1, zero=1)
    V.selo(c, 1470, 880, 1, "NOTA ZERO", RED, -6, 50)
    big(c, "FUGIR ZERA.", 340)
    big(c, "E QUANDO É SÓ", 470)
    boxed(c, "TANGENCIAR?", 70, 520, 116, AMBER)
    text(c, "as 3 entregas da redação do ENEM", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_480_pontos", capa_480), ("capa_B_bairro_certo", capa_bairro), ("capa_C_fugir_zera", capa_zero)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
