"""Capas — Função Afim, Episódio 1: parte fixa + taxa (tema claro). 3 variações em 1280x720.
A = as duas molas (20 cm sem carga e 26 cm com 2 kg) + a terceira com 5 kg e o selo "65 cm?" da regra de três;
B = o taxímetro gigante parado em 0 km já cobrando R$ 5,00 e "O TÁXI COBRA PARADO"; C = faixa dividida "100 min · R$ 90"
contra "200 min · R$ ???" com "DOBROU O x. E O y?". Nenhuma mostra gabarito (35 cm e R$ 140 não aparecem)."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep1", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO AFIM · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_molas(c):
    background(c); selo_topo(c)
    V.mola(c, 230, 260, 1.0, 20, 18, regua=False)
    text(c, "20 cm", 230, 680, 52, "black", BLUE)
    V.mola(c, 470, 260, 1.0, 26, 18, kg="2 kg", regua=False)
    text(c, "26 cm", 470, 900, 52, "black", INK)
    V.mola(c, 710, 260, 1.0, 33, 18, kg="5 kg", regua=False, col_al=AMBER)
    V.selo(c, 960, 960, 1.0, "65 cm?", AMBER, -6, 64)
    s1, s2 = "A REGRA DE TRÊS", "MENTIU?"
    text(c, s1, 1390, 430, fit(s1, 120, 900), "black", INK)
    sz = fit(s2, 170, 820)
    w = text_w(s2, "black", sz) + 80
    shadow_rrect(c, 1390 - w / 2, 500, w, 220, 30, 1, 1.4)
    rrect(c, 1390 - w / 2, 500, w, 220, 30, RED)
    text_mid(c, s2, 1390, 610, sz, "black", "#FFFFFF")
    text(c, "parte fixa + taxa", 1390, 840, 64, "extrabold", PURPLE)


def capa_taxi(c):
    background(c); selo_topo(c, W / 2)
    V.taximetro(c, 600, 600, 900, 1.0, 0, 1.0, 0.0)
    s1, s2 = "O TÁXI", "COBRA PARADO"
    text(c, s1, 1500, 470, fit(s1, 170, 700), "black", INK)
    text(c, s2, 1500, 610, fit(s2, 110, 720), "black", BLUE)
    V.linha(c, [("f(x) = ", INK), ("a", PURPLE), ("x", INK), (" + ", INK), ("b", BLUE)], 1500, 790, 96, 1.0)


def capa_dobro(c):
    background(c); selo_topo(c, W / 2)
    s = "DOBROU O x. E O y?"
    text(c, s, W / 2, 300, fit(s, 160, 1780), "black", INK)
    for k, (mins, val, col) in enumerate((("100 min", "R$ 90", GREEN), ("200 min", "R$ ???", AMBER))):
        x = 520 + k * 880
        shadow_rrect(c, x - 340, 400, 680, 480, 40, 1, 1.4)
        rrect(c, x - 340, 400, 680, 480, 40, "#FFFFFF")
        text(c, mins, x, 540, 96, "black", INK)
        text_mid(c, val, x, 720, 150, "black", col)
    text_mid(c, "×2", W / 2, 640, 90, "black", PURPLE)
    rrect(c, 0, 960, W, 120, 0, PURPLE)
    text_mid(c, "a mensalidade NÃO dobra", W / 2, 1020, 64, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_regra_de_tres_mentiu", capa_molas), ("capa_B_taxi_cobra_parado", capa_taxi),
                     ("capa_C_dobrou_o_x", capa_dobro)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
