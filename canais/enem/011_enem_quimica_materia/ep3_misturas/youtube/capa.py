"""Capas — Matéria, Substâncias e Misturas, Episódio 3: Misturas (tema claro). Gera 3 variações em 1280x720."""
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


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "QUÍMICA DO ZERO · EPISÓDIO 3", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_puros(c):
    background(c)
    selo(c)
    painel(c)
    V.gas_mix(c, 1300, 300, 260, 200, 1, 0)
    V.V2.garrafa(c, 1640, 330, 1)
    V.V2.anel(c, 1470, 720, 1)
    for x, y in ((1420, 210), (1730, 210), (1600, 620)):
        check_icon(c, x, y, 34, 1, RED, "x")
    text(c, "AR, ÁGUA MINERAL", 80, 330, 96, "black", INK, align="left")
    text(c, "E OURO 18K", 80, 460, 120, "black", INK, align="left")
    boxed(c, "SÃO PUROS?", 70, 520, 140, RED)
    text(c, "misturas do zero", 90, 860, 56, "extrabold", INK2, align="left")


def capa_salada(c):
    background(c)
    selo(c)
    painel(c)
    V.vidro(c, 1470, 480, 240, 300, 1, "acucar", 0, 1)
    text(c, "HOMOGÊNEA", 1470, 540, 40, "black", BLUE)
    V.salada(c, 1470, 760, 1, 1.2)
    text(c, "HETEROGÊNEA", 1470, 930, 40, "black", "#B07A00")
    text(c, "ÁGUA COM AÇÚCAR", 80, 330, 88, "black", INK, align="left")
    text(c, "OU SALADA", 80, 460, 120, "black", INK, align="left")
    boxed(c, "DE FRUTAS?", 70, 520, 140, PURPLE)
    text(c, "homogênea × heterogênea", 90, 860, 56, "extrabold", INK2, align="left")


def capa_leite(c):
    background(c)
    selo(c)
    painel(c)
    V.lupa(c, 1470, 470, 260, 1, "leite", 0, 1)
    text(c, "no microscópio", 1470, 860, 46, "black", INK2)
    text(c, "O LEITE É", 80, 340, 136, "black", INK, align="left")
    text(c, "HOMOGÊNEO?", 80, 480, 128, "black", INK, align="left")
    boxed(c, "NÃO!", 70, 530, 150, AMBER, INK)
    text(c, "o que é puro de verdade", 90, 860, 56, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_sao_puros", capa_puros), ("capa_B_acucar_salada", capa_salada), ("capa_C_leite", capa_leite)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
