"""Capas — Divisão Proporcional, Episódio 5: Revisão geral (tema claro). 3 variações em 1280x720.
Evita os formatos já usados nas revisões 019–022 ("N PEGADINHAS: QUANTAS VOCÊ ACERTA?", "VOCÊ ESTÁ PRONTO?",
"VERDADEIRO OU FALSO? 9 PEGADINHAS", "PROPORCIONAL OU NÃO?", "5 QUESTÕES INÉDITAS"). Nenhuma entrega gabarito."""
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_pesos(c):
    background(c); selo(c); painel(c)
    casos = [("DIRETA", BLUE), ("INVERSA", PURPLE), ("COMPOSTA", GREEN), ("PARTE FIXA", AMBER)]
    for k, (s, col) in enumerate(casos):
        y = 230 + k * 180
        pill(c, s, 1200, y, col, size=44, bounds=(0, 1920))
        K.fmid(c, "?:?:?", 1785, y + 30, 50, "black", col, align="right")
    big(c, "QUAIS SÃO", 340)
    big(c, "OS PESOS?", 470)
    boxed(c, "A DECISÃO QUE VALE", 70, 520, 120, PURPLE)
    text(c, "revisão completa de divisão proporcional", 90, 860, 46, "extrabold", INK2, align="left")


def capa_virar(c):
    background(c); selo(c); painel(c)
    for j, n in enumerate((2, 3, 4)):
        V.flip(c, n, 1290 + j * 180, 330, 120, 1.0, 1)
    K.fmid(c, "✓  vire a FRAÇÃO", 1470, 470, 46, "black", GREEN)
    for j, n in enumerate((4, 3, 2)):
        K.fmid(c, str(n), 1290 + j * 180, 640, 110, "black", RED)
    line(c, 1220, 640, 1720, 640, RED, 1, 8)
    K.fmid(c, "✗  não a FILA", 1470, 790, 46, "black", RED)
    big(c, "INVERSAMENTE", 340)
    big(c, "A 2, 3 E 4", 470)
    boxed(c, "NÃO É 4, 3 E 2", 70, 520, 140, RED)
    text(c, "as pegadinhas da divisão proporcional", 90, 860, 46, "extrabold", INK2, align="left")


def capa_multiplicar(c):
    background(c); selo(c); painel(c)
    V.quadros(c, 1240, 230, 5, 2, 92, 1, GREEN)
    text(c, "5 pessoas × 2 dias", 1470, 480, 42, "black", INK)
    text(c, "5 + 2 = 7", 1470, 640, 80, "black", RED)
    V.strike(c, 1290, 615, 1650, 615, 1, RED)
    text(c, "5 × 2 = 10", 1470, 830, 90, "black", GREEN)
    big(c, "SOMAR OU", 340)
    big(c, "MULTIPLICAR?", 470)
    boxed(c, "DOIS CRITÉRIOS", 70, 520, 140, GREEN)
    text(c, "revisão com 5 questões estilo ENEM", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_quais_sao_os_pesos", capa_pesos), ("capa_B_vire_a_fracao", capa_virar),
                     ("capa_C_somar_ou_multiplicar", capa_multiplicar)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
