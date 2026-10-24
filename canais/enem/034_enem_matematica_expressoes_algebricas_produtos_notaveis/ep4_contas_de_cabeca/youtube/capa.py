"""Capas — Expressões Algébricas e Produtos Notáveis, Episódio 4: contas de cabeça (tema claro).
3 variações em 1280x720. Formatos: A = a conta gigante "1 003 × 997" com o alarme verde ATALHO! e "DE CABEÇA?",
sem resultado; B = a reta dos GÊMEOS (49 · 51 em volta do 50) ocupando a faixa de baixo, título "MULTIPLIQUE GÊMEOS";
C = "87² − 13²" à esquerda e um cronômetro de 3 s à direita, com "EM 3 SEGUNDOS"."""
import importlib.util, math, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep4", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while V.ftext_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · ÁLGEBRA · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, PURPLE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, PURPLE, size=34, anchor="center", bounds=(0, 1920))


def capa_deposito(c):
    background(c); selo_topo(c, W / 2)
    s = "1 003 × 997"
    V.fmid(c, s, W / 2, 400, fit(s, 260, 1700), "black", INK)
    text(c, "DE CABEÇA?", W / 2, 700, 150, "black", GREEN)
    V.alarme(c, W / 2, 880, 1.0, 0.2, 64)


def capa_gemeos(c):
    background(c); selo_topo(c)
    text(c, "MULTIPLIQUE", 84, 330, 150, "black", INK, align="left")
    text(c, "GÊMEOS", 84, 490, 170, "black", GREEN, align="left")
    V.fmid(c, "49 · 51 = ?", 1450, 420, 120, "black", PURPLE)
    V.reta_gemeos(c, 200, 1720, 820, 50, 1, 1.0, u=1.0, escala=3, rot=("49", "50", "51"), size=64)


def capa_cronometro(c):
    background(c); selo_topo(c)
    V.fmid(c, "87² − 13²", 84, 420, 170, "black", INK, align="left")
    text(c, "EM 3 SEGUNDOS?", 84, 720, fit("EM 3 SEGUNDOS?", 130, 1100), "black", GREEN, align="left")
    cx, cy, r = 1530, 560, 230
    c.drawCircle(cx, cy, r + 26, paint(GREEN, 0.18))
    c.drawCircle(cx, cy, r, paint("#FFFFFF"))
    c.drawArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), -90, 300, False, paint(GREEN, 1.0, stroke=30, cap_round=True))
    rrect(c, cx - 40, cy - r - 70, 80, 50, 12, GREEN)
    text_mid(c, "3 s", cx, cy, 150, "black", GREEN)


if __name__ == "__main__":
    for nome, fn in (("capa_A_de_cabeca", capa_deposito), ("capa_B_multiplique_gemeos", capa_gemeos),
                     ("capa_C_tres_segundos", capa_cronometro)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
