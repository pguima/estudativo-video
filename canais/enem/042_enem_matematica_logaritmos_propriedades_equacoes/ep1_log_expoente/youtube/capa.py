"""Capas — Logaritmos, Episódio 1: logaritmo é um expoente (tema claro). 3 variações em 1280x720.
A = 2¹⁰⁰ gigante e uma fileira de caixinhas "?" que somem para a direita, com "QUANTOS ALGARISMOS?" e o chip log 2 ≈ 0,301;
B = log₂ 32 com o balão de pergunta "2 elevado a quanto dá 32?" (formato de conversa), "LOG É UMA PERGUNTA";
C = "log 0 = ?" em fundo âmbar, com o selo "EXISTE?".
Nenhuma mostra gabarito (os 31 algarismos da Q4 não aparecem)."""
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


def selo_topo(c, cx=None, col=None):
    s = "MATEMÁTICA ENEM · LOGARITMOS · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, col or BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, col or BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_algarismos(c):
    background(c); selo_topo(c)
    V.mx(c, "2^{100}", 470, 420, 300, 1.0, PURPLE)
    s = "QUANTOS ALGARISMOS?"
    text(c, s, 1360, 330, fit(s, 96, 1000), "black", INK)
    for k in range(12):
        a = 1.0 - 0.07 * k
        x = 900 + (k % 6) * 160
        y = 420 + (k // 6) * 170
        rrect(c, x, y, 140, 150, 18, mix("#FFFFFF", AMBER, 0.18), a, shadow=True)
        text_mid(c, "?", x + 70, y + 75, 96, "black", AMBER, a)
    rrect(c, 140, 820, 820, 170, 34, mix("#FFFFFF", GREEN, 0.14), 1.0, shadow=True)
    V.lrow(c, [("log", "", GREEN), ("m", "2 ≈ 0,301", GREEN)], 550, 905, 100, 1.0)
    V.selo(c, 1420, 900, 1.0, "EM 10 SEGUNDOS", GREEN, -4, 60)


def capa_pergunta(c):
    background(c); selo_topo(c, W / 2)
    V.lrow(c, [("log", "2", INK, BLUE), ("m", "32", GREEN)], 560, 600, 250, 1.0)
    V.balao(c, "2 elevado a quanto dá 32?", 1360, 400, 1.0, 64, BLUE)
    s = "LOG É UMA PERGUNTA"
    text(c, s, W / 2, 920, fit(s, 130, 1780), "black", PURPLE)


def capa_log0(c):
    background(c)
    c.drawRect(skia.Rect.MakeXYWH(0, 0, W, H), paint(mix("#FFFFFF", AMBER, 0.22)))
    selo_topo(c, col=AMBER)
    V.lrow(c, [("log", "", INK), ("m", "0 = ?", RED)], W / 2 - 60, 520, 300, 1.0)
    V.selo(c, 1520, 300, 1.0, "EXISTE?", RED, 8, 80)
    s = "O LOG QUE NINGUÉM DEVIA ESCREVER"
    text(c, s, W / 2, 900, fit(s, 96, 1760), "black", INK)


if __name__ == "__main__":
    for nome, fn in (("capa_A_quantos_algarismos", capa_algarismos), ("capa_B_log_e_pergunta", capa_pergunta),
                     ("capa_C_log_de_zero", capa_log0)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
