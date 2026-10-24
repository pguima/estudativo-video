"""Capas — Grandezas Proporcionais, Episódio 2: Reconhecer na tabela (tema claro). 3 variações em 1280x720."""
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
T = 1e6  # instante "depois de tudo": a tabela aparece completa e já colorida


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
    pill(c, "MATEMÁTICA ENEM · GRANDEZAS PROPORCIONAIS · EP. 2", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def aux(vals, cor, op):
    return dict(V.aux_col(vals, [0] * len(vals), [cor] * len(vals), 0), op=op)


def capa_duas_contas(c):
    background(c); selo(c); painel(c)
    V.tabela(c, T, 1180, 200, ["x", "y"], [["2", "30"], ["4", "15"], ["6", "10"]], 1.0,
             aux=[aux(["15", "3,75", "1,67"], RED, "÷"), aux(["60", "60", "60"], GREEN, "×")], w=(140, 140), wa=145, rh=90,
             size=46)
    K.chip(c, "INVERSA · k = 60", 1470, 640, GREEN, 1.0, 40)
    text(c, "÷ mudou · × não mudou", 1470, 760, 38, "black", INK2)
    text(c, "2 contas e pronto", 1470, 860, 46, "black", PURPLE)
    big(c, "DIRETA, INVERSA", 330)
    big(c, "OU NENHUMA?", 470)
    boxed(c, "2 CONTAS RESOLVEM", 70, 520, 130, PURPLE)
    text(c, "reconheça a proporção em qualquer tabela", 90, 860, 44, "extrabold", INK2, align="left")


def capa_uma_linha(c):
    background(c); selo(c); painel(c)
    V.tabela(c, T, 1230, 200, ["x", "y"], [["2", "6"], ["4", "12"], ["5", "20"]], 1.0,
             aux=[dict(V.aux_col(["3", "3", "4"], [0, 0, 0], [GREEN, GREEN, RED], 0), op="÷")], w=(160, 160), wa=170, rh=100,
             size=56)
    motor_selo = K.selo
    motor_selo(c, 1470, 700, 1.0, "PARECIA DIRETA…", RED, -5, 40)
    text(c, "a 3ª linha desmente", 1470, 830, 42, "black", INK2)
    big(c, "TESTOU SÓ", 330)
    big(c, "UMA LINHA?", 470)
    boxed(c, "ERROU", 70, 520, 170, RED)
    text(c, "o erro de tabela que o ENEM adora cobrar", 90, 860, 44, "extrabold", INK2, align="left")


def capa_detetive(c):
    background(c); selo(c); painel(c)
    V.tabela(c, T, 1200, 210, ["torneiras", "horas"], [["1", "12"], ["2", "6"], ["3", "4"], ["4", "3"]], 1.0,
             aux=[aux(["12", "12", "12", "12"], GREEN, "×")], w=(210, 160), wa=160, rh=90, size=48)
    V.lupa(c, 1765, 600, 1.0, 46)
    K.chip(c, "k = 12", 1470, 760, PURPLE, 1.0, 48)
    big(c, "O DETETIVE", 330)
    big(c, "DA TABELA", 470)
    boxed(c, "DIVIDE E MULTIPLICA", 70, 520, 120, GREEN)
    text(c, "e ainda acha o k que a questão pede", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_duas_contas", capa_duas_contas), ("capa_B_uma_linha_so", capa_uma_linha),
                     ("capa_C_detetive", capa_detetive)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
