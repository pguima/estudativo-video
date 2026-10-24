"""Capas — Expressões Algébricas e Produtos Notáveis, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos: A = "tire o disfarce": três situações (corrida, terreno, conta) cada uma revelando a sua expressão;
B = a pegadinha gigante (a + b)² = a² + b² com o carimbo "VOCÊ CAI?" e a faixa "9 pegadinhas"; C = 302 × 298 sobre a reta
dos gêmeos, com a pergunta "de cabeça?". Nenhuma mostra gabarito."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")
K = V.K


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · ÁLGEBRA · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_disfarce(c):
    background(c); selo_topo(c, W / 2)
    s = "TIRE O DISFARCE"
    text(c, s, W / 2, 270, fit(s, 150, 1700), "black", INK)
    itens = ((0, "5+2x", BLUE), (1, "(x−6)^2", AMBER), (4, "300^2 − 2^2", GREEN))
    for k, (ic, ex, col) in enumerate(itens):
        x = 360 + k * 600
        shadow_rrect(c, x - 250, 360, 500, 600, 30, 1, 1.2)
        rrect(c, x - 250, 360, 500, 600, 30, "#FFFFFF")
        V.area_icone(c, ic, x, 540, 1.05, 1.0)
        line(c, x - 200, 700, x + 200, 700, LIGHT, 1, 4)
        sz = 110
        while K.math_w(ex, sz) > 420:
            sz -= 4
        V.mx(c, ex, x, 820, sz, col, 1.0, align="center")


def capa_pegadinha(c):
    background(c); selo_topo(c)
    K.expr(c, "(a+b)^2 = a^2 + b^2", W / 2 - 60, 460, 200, 1.0, cores={0: INK, 1: RED, 2: INK, 3: RED, 4: INK})
    selo = "VOCÊ CAI?"
    V.selo(c, 1560, 250, 1.0, selo, AMBER, -8, 80)
    rrect(c, 0, 780, W, 300, 0, AMBER)
    s = "9 PEGADINHAS · 5 QUESTÕES"
    text(c, s, W / 2, 940, fit(s, 120, 1760), "black", INK)
    text(c, "revisão de álgebra para o ENEM", W / 2, 1035, 52, "extrabold", INK)


def capa_gemeos(c):
    background(c)
    rrect(c, 0, 0, W * 0.5, H, 0, mix("#FFFFFF", GREEN, 0.14))
    selo_topo(c)
    K.expr(c, "302 · 298", W * 0.25, 470, 170, 1.0, cores={0: BLUE, 2: BLUE})
    s = "DE CABEÇA?"
    text(c, s, W * 0.25, 720, fit(s, 140, 860), "black", RED)
    c.save(); c.translate(W * 0.75, 560); c.scale(2.0, 2.0); V.gemeos(c, 1.0); c.restore()
    text(c, "sem calculadora, em 1 linha", W * 0.75, 900, 54, "black", INK2)


if __name__ == "__main__":
    for nome, fn in (("capa_A_tire_o_disfarce", capa_disfarce), ("capa_B_voce_cai", capa_pegadinha),
                     ("capa_C_de_cabeca", capa_gemeos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
