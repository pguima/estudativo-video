"""Capas — Conceito de Função, Episódio 2 (tema claro). 3 variações em 1280x720.
Formatos: A = a máquina de refrigerante à esquerda com 2 sabores ESGOTADOS e o título empilhado à direita; B = fundo escuro
com "f(2 + 3) = 11?" gigante e o selo "OU 24?" (a dúvida do gancho, sem dizer qual é a certa); C = a cadeira vazia gigante
f(▢) no centro com as fichas (−2), (3x) e (x + 1) esperando para sentar."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, col=BLUE):
    s = "MATEMÁTICA ENEM · FUNÇÕES · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, col, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, col, size=34, anchor="center", bounds=(0, 1920))


def capa_maquina(c):
    background(c)
    selo_topo(c)
    V.maquina(c, 470, 600, 1.0, 1.0, esc=1.08, moedas=False)
    x = 960
    for k, (s, col) in enumerate((("O QUE ENTRA", BLUE), ("O QUE TEM", PURPLE), ("O QUE SAI", GREEN))):
        text(c, s, x, 330 + k * 170, fit(s, 140, 900), "black", col, align="left")
    rrect(c, x, 820, 820, 130, 30, mix("#FFFFFF", AMBER, 0.18))
    text(c, "domínio · contradomínio · imagem", x + 410, 905, 46, "black", AMBER)


def capa_soma(c):
    rrect(c, 0, 0, W, H, 0, INK)
    selo_topo(c, W / 2, BLUE)
    K.expr(c, "f(x) = x^2 - 1", W / 2, 260, 80, 1.0, cores={0: "#B9A8F0", 1: "#FFFFFF", 2: "#FFFFFF", 3: "#FFFFFF",
                                                            4: "#FFFFFF"})
    K.expr(c, "f(2+3) = 11 ?", W / 2, 520, 200, 1.0, cores={0: "#FFFFFF", 1: "#FFFFFF", 2: AMBER, 3: AMBER})
    V.selo(c, 1480, 760, 1.0, "OU 24?", GREEN, -6, 90)
    s = "A CONTA QUE QUASE TODO MUNDO ERRA"
    text(c, s, W / 2, 990, fit(s, 84, 1700), "black", "#FFFFFF")


def capa_cadeira(c):
    background(c)
    selo_topo(c, W / 2, PURPLE)
    s = "A CADEIRA VAZIA"
    text(c, s, W / 2, 300, fit(s, 170, 1700), "black", INK)
    V.cadeira(c, "", W / 2, 520, 170, 1.0)
    for k, (s_, col) in enumerate((("(−2)", BLUE), ("(3x)", PURPLE), ("(x + 1)", GREEN))):
        cx = 480 + k * 480
        rrect(c, cx - 170, 720, 340, 150, 34, mix("#FFFFFF", col, 0.16), shadow=True)
        fmid_ = K.fmid
        fmid_(c, s_, cx, 795, 90, "black", col)
    text(c, "quem senta no lugar do x?", W / 2, 990, 56, "extrabold", AMBER)


if __name__ == "__main__":
    for nome, fn in (("capa_A_o_que_entra_o_que_sai", capa_maquina), ("capa_B_f_de_2_mais_3", capa_soma),
                     ("capa_C_cadeira_vazia", capa_cadeira)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
