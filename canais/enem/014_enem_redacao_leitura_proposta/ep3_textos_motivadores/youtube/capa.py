"""Capas — Redação ENEM, Leitura da Proposta, Episódio 3: Textos motivadores (tema claro). 3 variações em 1280x720."""
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
    pill(c, "REDAÇÃO ENEM · EPISÓDIO 3", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_fantasma(c):
    background(c); selo(c); painel(c)
    V.folha(c, 1170, 170, 600, 12, 1, 0, {2: 1, 5: 1, 6: 1}, partial=(2,), counter=(9, AMBER), lh=48)
    V.ghost_label(c, 1500, 170 + 90 + 2 * 48, 1)
    big(c, "LINHA COPIADA", 340)
    big(c, "VIRA LINHA", 470)
    boxed(c, "FANTASMA", 70, 520, 150, RED)
    text(c, "o risco da cópia na redação do ENEM", 90, 860, 50, "extrabold", INK2, align="left")


def capa_zero(c):
    background(c); selo(c); painel(c)
    V.folha(c, 1170, 170, 600, 10, 1, 0, {1: 1, 3: 1, 4: 1}, partial=(1, 4), counter=(7, RED), lh=52)
    V.selo(c, 1470, 860, 1, "TEXTO INSUFICIENTE", RED, -6, 36)
    big(c, "UMA CÓPIA", 340)
    big(c, "PODE DAR", 470)
    boxed(c, "NOTA ZERO", 70, 520, 150, RED)
    text(c, "como usar os textos motivadores sem copiar", 90, 860, 46, "extrabold", INK2, align="left")


def capa_gps(c):
    background(c); selo(c); painel(c)
    c.save(); c.translate(1290, 200); c.scale(1.0, 1.0)
    V.celular(c, 0, 0, 1, 0, 1.0)
    c.restore()
    text(c, "mostra o caminho", 1470, 870, 40, "black", GREEN)
    text(c, "a entrega é SUA", 1470, 925, 40, "black", BLUE)
    big(c, "OS TEXTOS DE", 340)
    big(c, "APOIO SÃO", 470)
    boxed(c, "GPS", 70, 520, 150, BLUE)
    text(c, "use as ideias sem copiar uma linha", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_linha_fantasma", capa_fantasma), ("capa_B_nota_zero", capa_zero), ("capa_C_gps", capa_gps)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
