"""Capas — Equação do 2º Grau, Episódio 5 (tema claro). 3 variações em 1280x720.
Formatos: A = a fantasia roxa de "y" gigante (com máscara) e o título "NÃO PARE NO y";
B = duelo das duas equações do gancho empilhadas, cada uma com um contador "? raízes", e o título "PARECEM IGUAIS";
C = fundo escuro com a placa vermelha "x ≠ 0" e a fração 6/x, título "O VALOR PROIBIDO". Nenhuma mostra gabarito."""
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
fmid = K.fmid


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


SELO = "MATEMÁTICA ENEM · EQUAÇÃO DO 2º GRAU · EP. 5"


def capa_fantasia(c):
    background(c)
    pill(c, SELO, 84, 90, BLUE, size=34, bounds=(0, 1920))
    V.fantasia(c, 520, 560, 300, 1.0, 1.0)
    K.expr(c, "x^2 = y", 520, 900, 90, 1.0, cores={0: BLUE, 2: PURPLE})
    x = 1020
    for k, (s, col) in enumerate((("NÃO", INK), ("PARE", INK), ("NO y", PURPLE))):
        text(c, s, x, 380 + k * 190, fit(s, 210, 820), "black", col, align="left")
    pill(c, "a fantasia tem de sair", 1020, 930, AMBER, size=44, bounds=(0, 1920))


def capa_duelo(c):
    background(c)
    pill(c, SELO, W / 2, 80, BLUE, size=32, anchor="center", bounds=(0, 1920))
    s = "PARECEM IGUAIS"
    text(c, s, W / 2, 230, fit(s, 150, 1700), "black", INK)
    for k, (ex, col) in enumerate((("x^4 - 13x^2 + 36 = 0", BLUE), ("x^4 - 5x^2 - 36 = 0", AMBER))):
        y = 470 + k * 290
        rrect(c, 110, y - 115, 1700, 230, 36, "#FFFFFF", shadow=True)
        K.expr(c, ex, 760, y, 110, 1.0)
        rrect(c, 1390, y - 85, 380, 170, 30, mix("#FFFFFF", col, 0.22))
        fmid(c, "? raízes", 1580, y, 64, "black", col)


def capa_proibido(c):
    rrect(c, 0, 0, W, H, 0, INK)
    pill(c, SELO, W / 2, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))
    K.expr(c, "6/x = x - 1", 560, 480, 170, 1.0, cores={i: "#FFFFFF" for i in range(5)})
    V.proibido(c, 1390, 480, 1.0, 110)
    s = "O VALOR PROIBIDO"
    text(c, s, W / 2, 820, fit(s, 160, 1760), "black", "#FFFFFF")
    text(c, "x no denominador: anote antes de multiplicar", W / 2, 950, 56, "extrabold", RED)


if __name__ == "__main__":
    for nome, fn in (("capa_A_nao_pare_no_y", capa_fantasia), ("capa_B_parecem_iguais", capa_duelo),
                     ("capa_C_valor_proibido", capa_proibido)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
