"""Capas — Sistemas de Equações Lineares, Episódio 4 (tema claro). 3 variações em 1280x720.
Formatos: A = as três balanças com as duplas em fila embaixo e "QUANTO PESA O BETO?" no alto, com o palpite "62,5 kg?" num
selo âmbar (sem dar a resposta); B = a escada do sistema escalonado na diagonal à esquerda, com "x = ?" e "y = ?" e
"COMECE PELO DEGRAU DE BAIXO" à direita; C = fundo escuro com as fichas A, B, C aparecendo duas vezes e "SOME TUDO" gigante."""
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

TAG = "MATEMÁTICA ENEM · SISTEMAS · EP. 4"


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def capa_balancas(c):
    background(c)
    pill(c, TAG, W / 2, 80, BLUE, size=34, anchor="center", bounds=(0, 1920))
    s = "QUANTO PESA O BETO?"
    text(c, s, W / 2, 250, fit(s, 160, 1760), "black", INK)
    for k, (nomes, v) in enumerate(V.PES):
        cx = 380 + k * 580
        V.balanca(c, cx, 900, 1.0, v, w=430)
        for j, n in enumerate(nomes):
            V.boneco(c, cx - 110 + j * 130, 898, 64, V.P_COR[n], 1.0, n[0])
    V.selo(c, W / 2, 400, 1.0, "125 ÷ 2 = 62,5 kg?", AMBER, -4, 60)


def capa_escada(c):
    background(c)
    pill(c, TAG, 84, 90, BLUE, size=34, bounds=(0, 1920))
    linhas = ["x + y + z = 6", "y + z = 5", "z = 3"]
    for k, ex in enumerate(linhas):
        x = 90 + k * 170
        y = 300 + k * 200
        rrect(c, x, y, 1000 - k * 170, 170, 26, K_DEGRAU if k < 2 else mix("#FFFFFF", GREEN, 0.3), 1.0, shadow=True)
        V.expr(c, ex, x + 50, y + 85, 84, 1.0, align="left")
    for k, s in enumerate(("x = ?", "y = ?")):
        V.chip(c, s, 930, 385 + k * 200, AMBER, 1.0, size=50)
    for k, (s, col) in enumerate((("COMECE", INK), ("PELO DEGRAU", INK), ("DE BAIXO", GREEN))):
        text(c, s, 1830, 420 + k * 160, fit(s, 130, 700), "black", col, align="right")
    text(c, "e suba substituindo", 1830, 920, 50, "extrabold", GRAY, align="right")


K_DEGRAU = "#EDEBE4"


def capa_soma(c):
    rrect(c, 0, 0, W, H, 0, "#22272E")
    pill(c, TAG, W / 2, 90, GREEN, size=34, anchor="center", bounds=(0, 1920))
    s = "SOME TUDO"
    text(c, s, W / 2, 330, fit(s, 230, 1700), "black", "#FFFFFF")
    for k, L in enumerate("ABCABC"):
        V.ficha(c, L, 360 + k * 240, 540, 1.0, 80)
    rrect(c, 410, 700, 1100, 120, 30, GREEN)
    V.fmid(c, "cada um aparece 2 vezes", W / 2, 760, 60, "black", "#FFFFFF")
    text(c, "o atalho dos sistemas com 3 incógnitas", W / 2, 960, 56, "extrabold", "#C9D1D9")


if __name__ == "__main__":
    for nome, fn in (("capa_A_quanto_pesa_o_beto", capa_balancas), ("capa_B_degrau_de_baixo", capa_escada),
                     ("capa_C_some_tudo", capa_soma)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
