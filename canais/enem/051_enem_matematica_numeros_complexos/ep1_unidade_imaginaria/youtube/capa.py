"""Capas — Números Complexos, Episódio 1: a unidade imaginária, delta negativo e as potências de i (tema claro).
3 variações em 1280x720.
A = o relógio de quatro horas (1, i, −1, −i) com i^{2026} gigante e "= ?" e o selo "DE CABEÇA";
B = o celular com "√−36 = erro" e a pergunta "E SE NÃO FOR ERRO?";
C = a equação do gancho, x² + 2x + 5 = 0, com "Δ < 0" e "SEM RAIZ?" numa faixa escura.
Nenhuma mostra gabarito (o −1 de i^2026, o 6i e o −1 ± 2i não aparecem)."""
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
    s = "MATEMÁTICA ENEM · NÚMEROS COMPLEXOS · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_relogio(c):
    background(c); selo_topo(c)
    V.relogio(c, 1400, 600, 330, 1, 0.5, acesas=None, rot_casa=False, size=86)
    V.expr(c, "i^{2026}", 560, 470, 260, 1, cores={0: PURPLE})
    text(c, "= ?", 560, 760, 170, "black", INK)
    V.selo(c, 560, 930, 1.0, "DE CABEÇA", GREEN, -5, 64)


def capa_calc(c):
    background(c); selo_topo(c)
    V.calculadora(c, 520, 610, 1, 0.0)
    s = "E SE NÃO"
    text(c, s, 1300, 430, fit(s, 150, 980), "black", INK)
    s2 = "FOR ERRO?"
    text(c, s2, 1300, 600, fit(s2, 150, 980), "black", RED)
    pill(c, "o número que a calculadora não conhece", 1300, 730, PURPLE, size=40, anchor="center", bounds=(0, 1920))


def capa_delta(c):
    background(c); selo_topo(c, W / 2)
    V.expr(c, "x^2 + 2x + 5 = 0", W / 2, 360, 150, 1)
    V.expr(c, "Δ = −16", W / 2, 540, 100, 1, cores={2: RED})
    rrect(c, 0, 690, W, 200, 0, INK)
    s = "SEM RAIZ? OLHE DE NOVO"
    text_mid(c, s, W / 2, 790, fit(s, 120, 1760), "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_relogio_i2026", capa_relogio), ("capa_B_calculadora_erro", capa_calc),
                     ("capa_C_sem_raiz", capa_delta)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
