"""Capas — Redação ENEM, Introdução, Episódio 2: quatro caminhos para contextualizar (tema claro). 3 variações em 1280x720."""
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


def big(c, s, y, maxw=1000, size=140):
    while text_w(s, "black", size) > maxw:
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "REDAÇÃO ENEM · INTRODUÇÃO · EP. 2", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_primordios(c):
    background(c); selo(c); painel(c)
    V.paper(c, 1160, 170, 620, 300, 1, lh=60, top=220)
    V.hand(c, "Desde os primórdios…", 1240, 330, 44, V.PEN, 1)
    V.strike(c, 1230, 312, 1240 + V.hand_w("Desde os primórdios…", 44) + 10, 312, 1, RED, 1)
    for k in range(4):
        V.porta(c, 1230 + k * 160, 800, k, 1, 0.5, label=False)
    big(c, "PARE DE COMEÇAR", 340)
    big(c, "A REDAÇÃO COM", 470)
    boxed(c, "“DESDE OS PRIMÓRDIOS”", 70, 520, 68, RED)
    text(c, "4 começos que dizem alguma coisa", 90, 860, 50, "extrabold", INK2, align="left")


def capa_portas(c):
    background(c); selo(c); painel(c)
    for k in range(4):
        V.porta(c, 1300 + (k % 2) * 340, 470 + (k // 2) * 380, k, 1, 0.7, label=True)
    big(c, "4 JEITOS DE", 340)
    big(c, "COMEÇAR A", 470)
    boxed(c, "INTRODUÇÃO", 70, 520, 118, BLUE)
    text(c, "lei · história · dado · conceito", 90, 860, 50, "extrabold", INK2, align="left")


def capa_dado(c):
    background(c); selo(c); painel(c)
    rrect(c, 1170, 230, 600, 200, 20, mix("#FFFFFF", AMBER, 0.12))
    text_mid(c, "“Pesquisas mostram", 1470, 300, 46, "black", INK2)
    text_mid(c, "que 90%…”", 1470, 360, 46, "black", INK2)
    V.selo(c, 1470, 520, 1, "QUE PESQUISAS?", RED, -5, 56)
    V.porta(c, 1470, 860, 2, 1, 0.6, label=False, solto=1.0)
    big(c, "ESSE DADO", 340)
    big(c, "PODE CUSTAR", 470)
    boxed(c, "PONTOS", 70, 520, 140, RED)
    text(c, "os 4 caminhos e o risco de cada um", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_desde_os_primordios", capa_primordios), ("capa_B_quatro_portas", capa_portas),
                     ("capa_C_dado_sem_fonte", capa_dado)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
