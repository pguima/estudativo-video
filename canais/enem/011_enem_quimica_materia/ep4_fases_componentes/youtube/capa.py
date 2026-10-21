"""Capas — Matéria, Substâncias e Misturas, Episódio 4: Fases e componentes (tema claro). Gera 3 variações em 1280x720."""
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


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "QUÍMICA DO ZERO · EPISÓDIO 4", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_gelo(c):
    background(c)
    selo(c)
    painel(c)
    cubes, liq = V.sis_gelo(c, 1260, 300, 420, 520, 1, 0.6)
    for k, (cx, cy, s) in enumerate(cubes):
        badge_num(c, k + 1, cx, cy - s * 0.85, 1, 30, bg=RED)
    text(c, "4 fases?", 1470, 900, 64, "black", RED)
    text(c, "ÁGUA COM 3", 80, 330, 128, "black", INK, align="left")
    text(c, "CUBOS DE GELO:", 80, 460, 104, "black", INK, align="left")
    boxed(c, "QUANTAS FASES?", 70, 520, 116, AMBER, INK)
    text(c, "a pegadinha preferida do ENEM", 90, 860, 54, "extrabold", INK2, align="left")


def capa_foto(c):
    background(c)
    selo(c)
    painel(c)
    for k, (s, ic, sub) in enumerate((("FOTO", V.icone_foto, "fases"), ("RECEITA", V.icone_receita, "componentes"))):
        y = 300 + k * 360
        c.save(); c.translate(1470, y); c.scale(3.4, 3.4)
        ic(c, 0, 0, 1, PURPLE)
        c.restore()
        text(c, s, 1470, y + 150, 60, "black", PURPLE)
        text(c, sub, 1470, y + 200, 34, "bold", INK2)
    text(c, "FASE É A FOTO,", 80, 340, 116, "black", INK, align="left")
    text(c, "COMPONENTE É", 80, 470, 116, "black", INK, align="left")
    boxed(c, "A RECEITA", 70, 520, 150, PURPLE)
    text(c, "conte duas vezes, sem armadilha", 90, 860, 54, "extrabold", INK2, align="left")


def capa_pote(c):
    background(c)
    selo(c)
    painel(c)
    reg = V.sis_pote(c, 1290, 220, 360, 560, 1, 0)
    for k, key in enumerate(("oleo", "gelo", "agua", "areia")):
        x, y, w, h = reg[key]
        V.fase_box(c, x, y, w, h, k + 1, 1, badge_x=1290 + 360 + 50 if key != "gelo" else x + w + 30)
    text(c, "4 fases · 3 componentes", 1470, 880, 44, "black", INK)
    text(c, "ÁGUA, ÓLEO,", 80, 330, 124, "black", INK, align="left")
    text(c, "AREIA E GELO", 80, 460, 124, "black", INK, align="left")
    boxed(c, "QUANTAS FASES?", 70, 530, 100, GREEN)
    text(c, "fases e componentes do zero", 90, 860, 54, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_gelo_quantas_fases", capa_gelo), ("capa_B_foto_receita", capa_foto), ("capa_C_pote_4_fases", capa_pote)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
