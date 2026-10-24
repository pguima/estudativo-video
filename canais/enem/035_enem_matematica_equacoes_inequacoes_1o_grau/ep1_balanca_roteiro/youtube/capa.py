"""Capas — Equações e Inequações do 1º Grau, Episódio 1 (tema claro). 3 variações em 1280x720.
Formatos: A = a balança grande à esquerda e o título empilhado à direita; B = a equação do gancho numa faixa escura no topo e
duas fichas "8?" e "20?" lado a lado (sem dizer qual é a certa); C = fundo âmbar cheio com "0x = −1" gigante."""
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
K = V.K


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, col=BLUE):
    s = "MATEMÁTICA ENEM · EQUAÇÕES · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, col, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, col, size=34, anchor="center", bounds=(0, 1920))


def capa_balanca(c):
    background(c)
    selo_topo(c)
    V.balanca(c, 600, 430, 1.0, 0, 0, "19 kg", esc=0.95)
    x = 1230
    for k, (s, col) in enumerate((("A EQUAÇÃO", INK), ("É UMA", INK), ("BALANÇA", PURPLE))):
        text(c, s, x, 330 + k * 150, fit(s, 150, 640), "black", col, align="left")
    rrect(c, x, 760, 600, 130, 30, mix("#FFFFFF", GREEN, 0.16))
    text(c, "o roteiro de 5 passos", x + 300, 845, 48, "black", GREEN)
    K.expr(c, "3x + 4 = 19", 600, 990, 96, 1.0, cores={0: RED})


def capa_sinal(c):
    background(c)
    rrect(c, 0, 0, W, 400, 0, INK)
    pill(c, "MATEMÁTICA ENEM · EQUAÇÕES · EP. 1", W / 2, 80, BLUE, size=34, anchor="center", bounds=(0, 1920))
    K.expr(c, "5(x-2) - 3(x-4) = 18", W / 2, 250, 130, 1.0, cores={0: "#FFFFFF", 1: "#FFFFFF", 2: AMBER, 3: "#FFFFFF",
                                                                   4: "#FFFFFF"})
    for k, (s, col) in enumerate((("x = 8 ?", BLUE), ("x = 20 ?", RED))):
        cx = 560 + k * 800
        shadow_rrect(c, cx - 300, 480, 600, 260, 40, 1, 1.2)
        rrect(c, cx - 300, 480, 600, 260, 40, "#FFFFFF")
        rrect(c, cx - 300, 480, 600, 18, 9, col)
        K.expr(c, s, cx, 625, 130, 1.0, cores={i: col for i in range(4)})
    s = "UM SINAL MUDA TUDO"
    text(c, s, W / 2, 960, fit(s, 140, 1760), "black", INK)


def capa_sem_solucao(c):
    rrect(c, 0, 0, W, H, 0, AMBER)
    pill(c, "MATEMÁTICA ENEM · EQUAÇÕES · EP. 1", W / 2, 90, INK, size=34, anchor="center", bounds=(0, 1920))
    K.expr(c, "0x = -1", W / 2, 470, 300, 1.0, cores={0: INK, 1: INK, 2: "#FFFFFF"})
    s = "E AGORA, QUAL É O x?"
    text(c, s, W / 2, 820, fit(s, 120, 1700), "black", INK)
    text(c, "quando a equação não tem solução (ou tem infinitas)", W / 2, 940, 52, "extrabold", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_equacao_balanca", capa_balanca), ("capa_B_um_sinal_muda_tudo", capa_sinal),
                     ("capa_C_sem_solucao", capa_sem_solucao)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
