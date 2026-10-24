"""Capas — Porcentagem, Episódio 5: ponto percentual × por cento e gráfico de setores (tema claro).
3 variações em 1280x720 (nenhuma mostra gabarito: a Q7 é 8% → 10% e a Q8 é o setor de 54°)."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · PORCENTAGEM · EP. 5", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_pontos(c):
    background(c); selo(c); painel(c)
    V.termometro(c, 1330, 250, 720, 5, 4, 1.0, RED, [(2, "2%", INK2), (4, "4%", RED)], "JUROS", 1, v_ini=2)
    V.ftext(c, "+2 p.p.", 1600, 360, 60, "black", BLUE)
    V.ftext(c, "= +100%", 1600, 470, 60, "black", PURPLE)
    K.selo(c, 1600, 600, 1.0, "DOBROU", GREEN, -5, 52)
    big(c, "SUBIU 2%? NÃO:", 330)
    big(c, "2 PONTOS", 470)
    boxed(c, "PERCENTUAIS", 70, 520, 140, BLUE)
    text(c, "ponto percentual × por cento, sem confusão", 90, 860, 44, "extrabold", INK2, align="left")


def capa_pizza(c):
    background(c); selo(c); painel(c)
    V.pizza_setores(c, 1470, 470, 250, V.FAMILIA, 1.0, 1.0, rotulos=False)
    V.ftext(c, "360° = 100%", 1470, 820, 56, "black", PURPLE)
    text(c, "1% = 3,6°", 1470, 900, 44, "black", INK2)
    big(c, "LEIA QUALQUER", 330)
    big(c, "GRÁFICO DE", 470)
    boxed(c, "PIZZA", 70, 520, 160, PURPLE)
    text(c, "graus em porcentagem, de cabeça", 90, 860, 44, "extrabold", INK2, align="left")


def capa_grupos(c):
    background(c); selo(c); painel(c)
    V.turma(c, 1190, 330, 20, 5, 44, 6, BLUE, 1.0, 1.0, "HOMENS")
    V.turma(c, 1450, 330, 40, 8, 40, 12, PURPLE, 1.0, 1.0, "MULHERES")
    V.ftext(c, "30% + 30% = 60%?", 1470, 760, 52, "black", RED)
    strike(c, 1240, 742, 1700, 742, 1.0, RED, 1.0)
    text(c, "por cento DE QUEM?", 1470, 870, 40, "black", GREEN)
    big(c, "30% + 30%", 330)
    big(c, "NÃO É 60%", 470)
    boxed(c, "BASES DIFERENTES", 70, 520, 140, AMBER)
    text(c, "a pegadinha das porcentagens de grupos", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_dois_pontos", capa_pontos), ("capa_B_pizza_360", capa_pizza),
                     ("capa_C_bases_diferentes", capa_grupos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
