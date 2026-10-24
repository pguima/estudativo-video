"""Capas — Função Composta e Inversa, Episódio 1: composição, máquinas em fila (tema claro). 3 variações em 1280x720.
A = o caixa: etiqueta R$ 150,00, os dois carimbos e "CUPOM ANTES OU DEPOIS?" (sem dizer qual ordem ganha);
B = as duas máquinas gigantes g → f com o 2 entrando e "?" saindo; C = f(g(x)) ≠ g(f(x)) tipográfico com "A ORDEM IMPORTA"."""
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
    s = "MATEMÁTICA ENEM · FUNÇÃO COMPOSTA · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_caixa(c):
    background(c); selo_topo(c)
    V.etiqueta(c, 470, 420, "R$ 150,00", 1.0, 700, 260)
    V.carimbo(c, 330, 730, "CUPOM −R$ 20", RED, 1.0, 68)
    V.carimbo(c, 880, 730, "−10%", RED, 1.0, 68)
    s1, s2 = "CUPOM ANTES", "OU DEPOIS?"
    text(c, s1, 1420, 440, fit(s1, 140, 860), "black", INK)
    sz = fit(s2, 140, 820)
    w = text_w(s2, "black", sz) + 70
    shadow_rrect(c, 1420 - w / 2, 500, w, 180, 28, 1, 1.4)
    rrect(c, 1420 - w / 2, 500, w, 180, 28, AMBER)
    text_mid(c, s2, 1420, 590, sz, "black", "#FFFFFF")
    text(c, "a ordem muda o preço", 1420, 800, 60, "extrabold", PURPLE)


def capa_maquinas(c):
    background(c); selo_topo(c, W / 2)
    s = "f(g(2)) = ?"
    text(c, s, W / 2, 330, fit(s, 190, 1700), "black", INK)
    V.esteira(c, 120, 1800, 820, 1.0)
    V.maquina(c, 720, 640, "g", "2x + 1", V.COL_G, 1.0, 0.3, 420, 300)
    V.maquina(c, 1320, 640, "f", "x^2 - 1", V.COL_F, 1.0, 0.3, 420, 300)
    V.bola(c, 280, 640, "2", INK, 1.0, 80)
    V.bola(c, 1680, 640, "?", AMBER, 1.0, 90)


def capa_ordem(c):
    background(c); selo_topo(c, W / 2)
    V.linha(c, [("f", V.COL_F), ("(", INK), ("g", V.COL_G), ("(x))", INK)], 500, 520, 190, 1.0)
    text_mid(c, "≠", W / 2, 520, 200, "black", RED)
    V.linha(c, [("g", V.COL_G), ("(", INK), ("f", V.COL_F), ("(x))", INK)], 1420, 520, 190, 1.0)
    rrect(c, 0, 800, W, 280, 0, PURPLE)
    s = "A ORDEM IMPORTA"
    text(c, s, W / 2, 985, fit(s, 170, 1780), "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_cupom_antes_ou_depois", capa_caixa), ("capa_B_maquinas_em_fila", capa_maquinas),
                     ("capa_C_a_ordem_importa", capa_ordem)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
