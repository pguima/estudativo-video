"""Capas — Matéria, Substâncias e Misturas, Episódio 2: Alotropia (tema claro). Gera 3 variações em 1280x720."""
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


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "QUÍMICA DO ZERO · EPISÓDIO 2", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_mesma(c):
    background(c)
    selo(c)
    painel(c)
    V.V.diamante(c, 1300, 330, 1, 1.15)
    V.V.lapis(c, 1630, 330, 1, 0.75)
    text_mid(c, "=", 1470, 330, 110, "black", AMBER)
    V.V.peca(c, 1470, 640, 110, "C")
    text(c, "carbono puro", 1470, 850, 52, "black", INK)
    text(c, "GRAFITE E", 80, 340, 136, "black", INK, align="left")
    text(c, "DIAMANTE", 80, 480, 136, "black", INK, align="left")
    boxed(c, "SÃO A MESMA COISA?", 70, 530, 92, RED)
    text(c, "alotropia do zero", 90, 860, 56, "extrabold", INK2, align="left")


def capa_montagem(c):
    background(c)
    selo(c)
    painel(c)
    V.mini(c, "diamante", 1470, 330, 30, 1)
    V.mini(c, "grafite", 1470, 720, 30, 1)
    text(c, "duríssimo", 1470, 520, 40, "black", INK2)
    text(c, "macio", 1470, 920, 40, "black", INK2)
    text(c, "MESMAS PEÇAS,", 80, 340, 116, "black", INK, align="left")
    text(c, "OUTRA", 80, 470, 136, "black", INK, align="left")
    boxed(c, "MONTAGEM", 70, 520, 140, PURPLE)
    text(c, "a estrutura decide a propriedade", 90, 860, 52, "extrabold", INK2, align="left")


def capa_enem(c):
    background(c)
    selo(c)
    painel(c)
    for k, kd in enumerate(("grafeno", "nanotubo")):
        V.mini(c, kd, 1470, 270 + k * 260, 24, 1)
    V.V.mol(c, "O3", 1470, 800, 64)
    text(c, "GRAFENO,", 80, 340, 124, "black", INK, align="left")
    text(c, "NANOTUBO E", 80, 470, 124, "black", INK, align="left")
    boxed(c, "OZÔNIO NO ENEM", 70, 520, 104, GREEN)
    text(c, "alotropia para quem nunca estudou", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_grafite_diamante", capa_mesma), ("capa_B_mesmas_pecas", capa_montagem), ("capa_C_nano_enem", capa_enem)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
