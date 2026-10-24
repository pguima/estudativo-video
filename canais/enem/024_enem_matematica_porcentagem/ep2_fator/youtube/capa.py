"""Capas — Porcentagem, Episódio 2: o fator de multiplicação (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · PORCENTAGEM · EP. 2", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_triplica(c):
    background(c); selo(c); painel(c)
    text(c, "+200%", 1470, 230, 72, "black", INK)
    for k in range(3):
        rrect(c, 1180 + k * 200, 300, 180, 180, 20, V.BLOCO if k == 0 else GREEN, 1.0)
        text_mid(c, "100%", 1270 + k * 200, 390, 38, "black", "#FFFFFF")
    text(c, "o que tinha", 1270, 525, 26, "bold", V.BLOCO)
    text(c, "+ 200%", 1570, 525, 26, "bold", GREEN)
    V.maquina(c, 1470, 720, "3", 1.0, 25, PURPLE, 300, 230)
    big(c, "AUMENTAR 200%", 330)
    big(c, "É DOBRAR? NÃO:", 470)
    boxed(c, "TRIPLICA", 70, 520, 170, GREEN)
    text(c, "o fator de multiplicação, do zero", 90, 860, 44, "extrabold", INK2, align="left")


def capa_maquina(c):
    background(c); selo(c); painel(c)
    V.etiqueta(c, "R$ 60", 1470, 250, INK, 1.0, 56)
    arrow(c, 1470, 320, 1470, 410, GRAY, 1.0, 6, 22)
    V.maquina(c, 1470, 540, "1,25", 1.0, 30, PURPLE, 360, 250)
    arrow(c, 1470, 680, 1470, 770, GRAY, 1.0, 6, 22)
    V.etiqueta(c, "R$ 75", 1470, 850, GREEN, 1.0, 56)
    big(c, "AUMENTO OU", 330)
    big(c, "DESCONTO EM", 470)
    boxed(c, "UMA CONTA SÓ", 70, 520, 150, PURPLE)
    text(c, "a máquina que resolve quase tudo de porcentagem", 90, 860, 40, "extrabold", INK2, align="left")


def capa_contrario(c):
    background(c); selo(c); painel(c)
    K.ftext(c, "× 0,65", 1470, 260, 96, "black", INK)
    V.blocos(c, 1190, 360, 560, 170, 0.35, 1.0, RED, "0,65", "?", sai=True)
    text(c, "fica", 1370, 580, 30, "bold", INK2)
    text(c, "sai", 1650, 580, 30, "bold", RED)
    K.ftext(c, "desconto de 65%?", 1470, 720, 52, "black", RED)
    V.strike(c, 1240, 702, 1700, 702, 1.0, RED, 1.0)
    text(c, "leia o fator ao contrário", 1470, 860, 36, "black", GREEN)
    big(c, "0,65 É DESCONTO", 330)
    big(c, "DE QUANTO?", 470)
    boxed(c, "NÃO É 65%", 70, 520, 160, RED)
    text(c, "ler um fator ao contrário, sem decorar", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_triplica", capa_triplica), ("capa_B_maquina", capa_maquina), ("capa_C_ao_contrario", capa_contrario)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
