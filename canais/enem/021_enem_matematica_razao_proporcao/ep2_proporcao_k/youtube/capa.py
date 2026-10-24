"""Capas — Razão, Proporção e Regra de Três, Episódio 2: Proporção e o truque do k (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 2", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_k(c):
    background(c); selo(c); painel(c)
    text(c, "R$ 10 000 na razão 2 : 3", 1470, 220, 40, "black", INK)
    for i in range(2):
        V.pacote(c, 1230 + i * 120, 400, 100, V.CAIXA, 1, 1, "2 000", 34)
    for i in range(3):
        V.pacote(c, 1230 + i * 120, 620, 100, V.mix(V.CAIXA, PURPLE, 0.25), 1, 1, "2 000", 34)
    text(c, "4 000", 1780, 420, 46, "black", GREEN, align="right")
    text(c, "6 000", 1780, 640, 46, "black", GREEN, align="right")
    V.linha(c, [("k = ", INK), ("2 000", GREEN)], 1470, 815, 80, 1)
    big(c, "DIVIDA NUMA", 340)
    big(c, "RAZÃO EM", 470)
    boxed(c, "1 LINHA", 70, 520, 160, GREEN)
    text(c, "o truque do k, com pacotinhos", 90, 860, 46, "extrabold", INK2, align="left")


def capa_por_que(c):
    background(c); selo(c); painel(c)
    V.proporcao_x(c, 0, 1, ("2", "3"), ("x", "12"), 1470, 380, 120, ap=1, am=1, cores={"c": RED})
    K.expr(c, "3x = 24", 1470, 680, 90, 1)
    K.expr(c, "x = 8", 1470, 820, 100, 1, cores={2: GREEN})
    big(c, "POR QUE A", 340)
    big(c, "REGRA DE TRÊS", 470)
    boxed(c, "FUNCIONA?", 70, 520, 150, PURPLE)
    text(c, "uma propriedade explica tudo", 90, 860, 46, "extrabold", INK2, align="left")


def capa_pontas(c):
    background(c); selo(c); painel(c)
    xs = [1200 + k * 90 for k in range(7)]
    for k, (s, col) in enumerate([("a", AMBER), (":", INK), ("b", BLUE), ("=", INK), ("c", BLUE), (":", INK), ("d", AMBER)]):
        if col != INK:
            rrect(c, xs[k] - 40, 310, 80, 110, 18, col, 0.16)
        K.fmid(c, s, xs[k], 365, 90, "black", col)
    text(c, "PONTAS", 1470, 520, 50, "black", AMBER)
    text(c, "MIOLO", 1470, 600, 50, "black", BLUE)
    K.expr(c, "a · d = b · c", 1470, 760, 80, 1, cores={0: AMBER, 2: AMBER, 4: BLUE, 6: BLUE})
    big(c, "PONTAS × PONTAS", 340)
    big(c, "= MIOLO × MIOLO", 470)
    boxed(c, "PROPORÇÃO", 70, 520, 150, BLUE)
    text(c, "a propriedade fundamental, do zero", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_divida_numa_razao", capa_k), ("capa_B_por_que_funciona", capa_por_que),
                     ("capa_C_pontas_e_miolo", capa_pontas)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
