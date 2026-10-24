"""Capas — Conceito de Função, Episódio 1: a ideia de função (tema claro). 3 variações em 1280x720.
A = dois diagramas de flechas lado a lado (chegando × saindo) com "PODE?" em cada; B = a máquina gigante com o 10 entrando
e "SEMPRE 60?"; C = as bombas R$ 60 × R$ 70 com "ISSO TEM NOME". Nenhuma mostra gabarito."""
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
    s = "MATEMÁTICA ENEM · FUNÇÕES · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_flechas(c):
    background(c); selo_topo(c, W / 2)
    s = "É FUNÇÃO OU NÃO É?"
    text(c, s, W / 2, 290, fit(s, 150, 1780), "black", INK)
    for k, (setas, rot, col) in enumerate((([(0, 1), (1, 1)], "2 CHEGANDO", GREEN), ([(0, 0), (0, 1)], "2 SAINDO", RED))):
        x = 500 + k * 920
        shadow_rrect(c, x - 400, 360, 800, 600, 40, 1, 1.4)
        rrect(c, x - 400, 360, 800, 600, 40, "#FFFFFF")
        V.diagrama(c, x, 620, 1.0, setas, A=["1", "2"], B=["a", "b", "c"], h=380, gapx=380, larg=170, size=60,
                   nomes=("A", "B"), cor_seta=col)
        rrect(c, x - 230, 850, 460, 90, 45, col)
        text_mid(c, rot + "?", x, 895, 52, "black", "#FFFFFF")


def capa_maquina(c):
    background(c); selo_topo(c, 1440)
    V.maquina(c, 540, 700, 640, 1.0, "10", "60", 0.30, "FUNÇÃO")
    s1, s2 = "ENTRA 10.", "SAI SEMPRE 60?"
    text(c, s1, 1440, 470, fit(s1, 150, 820), "black", INK)
    sz = fit(s2, 120, 800)
    w = text_w(s2, "black", sz) + 70
    shadow_rrect(c, 1440 - w / 2, 540, w, 180, 28, 1, 1.4)
    rrect(c, 1440 - w / 2, 540, w, 180, 28, PURPLE)
    text_mid(c, s2, 1440, 630, sz, "black", "#FFFFFF")
    text(c, "a ideia de função do zero", 1440, 830, 50, "extrabold", BLUE)


def capa_bomba(c):
    background(c); selo_topo(c, W / 2)
    V.bomba(c, 520, 520, 700, 1.0)
    V.bomba(c, 1400, 520, 700, 1.0, valor="R$ 70,00", col_valor="#FF8A8A")
    text_mid(c, "?", W / 2 + 0, 520, 200, "black", AMBER)
    rrect(c, 0, 800, W, 280, 0, BLUE)
    s = "ISSO TEM NOME: FUNÇÃO"
    text(c, s, W / 2, 985, fit(s, 150, 1780), "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_chegando_ou_saindo", capa_flechas), ("capa_B_sempre_60", capa_maquina),
                     ("capa_C_isso_tem_nome", capa_bomba)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
