"""Capas — Sistemas de Equações Lineares, Episódio 1 (tema claro). 3 variações em 1280x720.
Formatos: A = o sítio cercado ocupando a metade de baixo, com o enigma "10 CABEÇAS · 28 PATAS" no alto e "QUANTAS GALINHAS?";
B = duas fichas inclinadas "2P = J ?" e "P = 2J ?" em cores neutras (sem dizer qual é a certa) sob "O DOBRO DE QUEM?";
C = fundo escuro com a peça "(30 − c)" encaixando em "4c + 2 ▢ = 100" e "SUBSTITUIU? PONHA PARÊNTESES"."""
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
SELO = "MATEMÁTICA ENEM · SISTEMAS · EP. 1"


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def capa_sitio(c):
    background(c)
    pill(c, SELO, W / 2, 80, BLUE, size=34, anchor="center", bounds=(0, 1920))
    V.linha(c, [("10 CABEÇAS", INK), (" · ", GRAY), ("28 PATAS", BLUE)], W / 2, 250, 130, 1.0)
    V.cercado(c, 210, 420, 1500, 420, 1.0, g=None, s=116)
    for k, (cx, cy) in enumerate(((360, 554.4), (1560, 730.8))):
        c.drawCircle(cx, cy, 70, paint(V.GRAMA, 1.0))
        (V.galinha if k == 0 else V.coelho)(c, cx, cy, 120, 1.0)
    s = "QUANTAS GALINHAS?"
    rrect(c, W / 2 - 560, 905, 1120, 120, 30, AMBER)
    text(c, s, W / 2, 994, fit(s, 92, 1060), "black", "#FFFFFF")


def capa_dobro(c):
    background(c)
    pill(c, SELO, 84, 90, BLUE, size=34, bounds=(0, 1920))
    s = "O DOBRO DE QUEM?"
    text(c, s, 84, 300, fit(s, 170, 1750), "black", INK, align="left")
    rrect(c, 84, 380, 1100, 100, 24, "#FFFFFF", shadow=True)
    text(c, "“Pedro tem o dobro das moedas de Júlia”", 634, 448, 46, "black", INK2)
    for k, (s2, rot) in enumerate((("2P = J ?", -5), ("P = 2J ?", 4))):
        cx = 560 + k * 800
        c.save(); c.translate(cx, 760); c.rotate(rot)
        shadow_rrect(c, -330, -170, 660, 340, 44, 1, 1.2)
        rrect(c, -330, -170, 660, 340, 44, "#FFFFFF")
        rrect(c, -330, -170, 660, 22, 11, PURPLE)
        V.linha(c, [(s2, INK)], 0, 10, 150, 1.0)
        c.restore()
    text(c, "metade erra esta tradução", W - 84, 1030, 46, "extrabold", RED, align="right")


def capa_parenteses(c):
    rrect(c, 0, 0, W, H, 0, INK)
    pill(c, SELO, W / 2, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))
    size = 150
    pre, body, pos = "4c + 2", "(30 − c)", " = 100"
    wpre, wb, wpos = (V.ftext_w(x, "black", size) for x in (pre, body, pos))
    x0 = W / 2 - (wpre + wb + wpos) / 2
    V.fmid(c, pre, x0, 470, size, "black", "#FFFFFF", 1.0, align="left")
    rrect(c, x0 + wpre - 14, 470 - size * 0.7, wb + 28, size * 1.4, 26, mix(INK, GREEN, 0.35))
    V.fmid(c, body, x0 + wpre, 470, size, "black", GREEN, 1.0, align="left")
    V.fmid(c, pos, x0 + wpre + wb, 470, size, "black", "#FFFFFF", 1.0, align="left")
    arrow(c, x0 + wpre + wb / 2, 180, x0 + wpre + wb / 2, 300, AMBER, 1.0, 10, 30)
    s = "SUBSTITUIU?"
    text(c, s, W / 2, 790, fit(s, 160, 1700), "black", "#FFFFFF")
    s = "PONHA PARÊNTESES"
    text(c, s, W / 2, 960, fit(s, 140, 1700), "black", AMBER)


if __name__ == "__main__":
    for nome, fn in (("capa_A_10_cabecas_28_patas", capa_sitio), ("capa_B_dobro_de_quem", capa_dobro),
                     ("capa_C_ponha_parenteses", capa_parenteses)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
