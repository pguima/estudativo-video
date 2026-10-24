"""Capas — Progressão Aritmética, Episódio 3: a soma de Gauss (tema claro). 3 variações em 1280x720.
A = os pares 1…100 ligados por arcos e "1 + 2 + … + 100 EM 5 SEGUNDOS?"; B = as duas escadas encaixadas num retângulo com
"POR QUE ÷ 2?"; C = duelo de cartões "NO 12º DIA" × "AO TODO EM 12 DIAS" com "TERMO OU SOMA?".
Nenhuma mostra gabarito (5 050, 1 100, 57 e 500 não aparecem)."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · PROGRESSÃO ARITMÉTICA · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_pares(c):
    background(c); selo_topo(c, W / 2)
    s = "1 + 2 + … + 100"
    text(c, s, W / 2, 300, fit(s, 170, 1700), "black", INK)
    V.pares(c, 99.0, 0.0, 1.0, x0=300, x1=1620, y=900)
    s2 = "EM 5 SEGUNDOS?"
    sz = fit(s2, 120, 1000)
    w = text_w(s2, "black", sz) + 80
    shadow_rrect(c, W / 2 - w / 2, 360, w, 170, 30, 1, 1.4)
    rrect(c, W / 2 - w / 2, 360, w, 170, 30, RED)
    text_mid(c, s2, W / 2, 445, sz, "black", "#FFFFFF")
    rrect(c, 0, 990, W, 90, 0, PURPLE)
    text_mid(c, "o truque de Gauss", W / 2, 1035, 54, "black", "#FFFFFF")


def capa_escadas(c):
    background(c); selo_topo(c)
    V.escadas(c, 150, 960, 1.0, 1.0, 110, 6)
    s1, s2 = "DUAS ESCADAS", "= 1 RETÂNGULO"
    text(c, s1, 1370, 380, fit(s1, 130, 1000), "black", INK)
    text(c, s2, 1370, 520, fit(s2, 120, 1000), "black", PURPLE)
    V.selo(c, 1370, 720, 1.0, "POR QUE ÷ 2?", AMBER, -5, 80)


def capa_termo_soma(c):
    background(c); selo_topo(c, W / 2)
    s = "TERMO OU SOMA?"
    text(c, s, W / 2, 300, fit(s, 160, 1780), "black", INK)
    for k, (tit, sub, col) in enumerate((("NO 12º DIA", "quanto correu?", BLUE), ("AO TODO", "em 12 dias?", PURPLE))):
        x = 520 + k * 880
        shadow_rrect(c, x - 360, 400, 720, 460, 40, 1, 1.4)
        rrect(c, x - 360, 400, 720, 460, 40, "#FFFFFF")
        text_mid(c, tit, x, 560, fit(tit, 110, 640), "black", col)
        text(c, sub, x, 690, 64, "extrabold", INK2)
        text_mid(c, "?", x, 790, 90, "black", AMBER)
    text_mid(c, "≠", W / 2, 630, 120, "black", RED)
    rrect(c, 0, 960, W, 120, 0, AMBER)
    text_mid(c, "uma palavra muda a resposta", W / 2, 1020, 60, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_cem_em_segundos", capa_pares), ("capa_B_duas_escadas", capa_escadas),
                     ("capa_C_termo_ou_soma", capa_termo_soma)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
