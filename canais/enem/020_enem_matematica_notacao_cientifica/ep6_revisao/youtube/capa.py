"""Capas — Notação Científica e Ordem de Grandeza, Episódio 6: Revisão geral (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike, check_icon  # noqa

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


def capa_pegadinhas(c):
    background(c); selo(c); painel(c)
    itens = [("25·10^3", False), ("7,2·10^5 → 10^6", True), ("1 m^2 = 100 cm^2", False)]
    for k, (s, ver) in enumerate(itens):
        y = 270 + k * 230
        sz = 84
        while K.expr_w(s, sz) > 470:
            sz -= 2
        K.expr(c, s, 1380, y, sz, 1)
        if not ver:
            w = K.expr_w(s, sz)
            strike(c, 1380 - w / 2 - 10, y + 6, 1380 + w / 2 + 10, y + 6, 1, RED, 1)
        K.chip(c, "V" if ver else "F", 1710, y, GREEN if ver else RED, 1, 70)
    big(c, "9 PEGADINHAS:", 340)
    big(c, "QUANTAS VOCÊ", 470)
    boxed(c, "ACERTA?", 70, 520, 160, AMBER)
    text(c, "revisão de notação científica para o ENEM", 90, 860, 46, "extrabold", INK2, align="left")


def capa_questoes(c):
    background(c); selo(c); painel(c)
    for k in range(5):
        x, y = (1300, 1640, 1300, 1640, 1470)[k], (280, 280, 540, 540, 790)[k]
        V.icone_area(c, k, x, y, 1.35, 1)
    big(c, "5 QUESTÕES", 340)
    big(c, "DE 5 MATÉRIAS", 470)
    boxed(c, "RESOLVIDAS", 70, 520, 150, GREEN)
    text(c, "Biologia · Física · Química · Humanas · Mat.", 90, 860, 40, "extrabold", INK2, align="left")


def capa_revisao(c):
    background(c); selo(c); painel(c)
    for k in range(5):
        x, y = (1300, 1640, 1300, 1640, 1470)[k], (260, 260, 520, 520, 780)[k]
        V.icone(c, k, x, y, 1.15, 1)
    big(c, "NOTAÇÃO", 340, maxw=980)
    big(c, "CIENTÍFICA", 470, maxw=980)
    boxed(c, "EM 1 REVISÃO", 70, 520, 150, PURPLE)
    text(c, "os 5 episódios em uma só aula", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_9_pegadinhas", capa_pegadinhas), ("capa_B_5_questoes", capa_questoes),
                     ("capa_C_revisao", capa_revisao)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
