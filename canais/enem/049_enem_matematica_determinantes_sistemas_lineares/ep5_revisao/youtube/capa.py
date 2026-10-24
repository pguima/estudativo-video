"""Capas — Determinantes e Sistemas, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos (sem repetir as revisões anteriores): A = o semáforo gigante no amarelo, com "D = 0" e as duas saídas
("gêmeas?" / "brigadas?") e o título "D = 0 É IMPOSSÍVEL?"; B = o gancho: ingresso e lanchonete ligados a um
determinante central, "O ATALHO DO ENEM"; C = fundo âmbar com o 2 × 2 do V/F 1 e duas fichas "7?" e "23?", "QUAL É O
CERTO?". Nenhuma mostra gabarito.
"""
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


def fit(s, size, maxw, peso="black"):
    while V.ftw(s, size, peso) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, cor=BLUE):
    s = "MATEMÁTICA ENEM · DETERMINANTES · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, cor, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, cor, size=34, anchor="center", bounds=(0, 1920))


def capa_semaforo(c):
    background(c)
    selo_topo(c)
    s = "D = 0 É IMPOSSÍVEL?"
    text(c, s, 84, 300, fit(s, 150, 1200), "black", INK, align="left")
    V.icone(c, 3, 1620, 560, 1.75, 1)
    shadow_rrect(c, 84, 400, 1200, 560, 44, 1, 1.4)
    rrect(c, 84, 400, 1200, 560, 44, "#FFFFFF")
    rrect(c, 140, 450, 440, 170, 30, mix("#FFFFFF", AMBER, 0.30))
    text_mid(c, "D = 0", 360, 535, 100, "black", AMBER)
    for k, (s1, col) in enumerate((("gêmeas?", BLUE), ("brigadas?", RED))):
        y = 700 + k * 130
        arrow(c, 600, 540, 760, y, INK2, 1, 8, 24)
        rrect(c, 780, y - 55, 460, 110, 55, mix("#FFFFFF", col, 0.16))
        text_mid(c, s1, 1010, y, 64, "black", col)
    V.sistema(c, ["x + y = 2", "2x + 2y = ?"], 150, 690, 56, 1)


def capa_atalho(c):
    background(c)
    selo_topo(c, W / 2)
    s = "O ATALHO DO ENEM"
    text(c, s, W / 2, 290, fit(s, 160, 1760), "black", INK)
    for k, (ic, rot, col) in enumerate(((5, "INGRESSOS", PURPLE), (4, "LANCHONETE", AMBER))):
        x = 330 + k * 1260
        shadow_rrect(c, x - 230, 420, 460, 440, 36, 1, 1.3)
        rrect(c, x - 230, 420, 460, 440, 36, mix("#FFFFFF", col, 0.14))
        V.area_icone(c, ic, x, 600, 0.8, 1)
        text_mid(c, rot, x, 800, 48, "black", col)
        arrow(c, x + (250 if k == 0 else -250), 640, x + (420 if k == 0 else -420), 640, GREEN, 1, 12, 34)
    shadow_rrect(c, 690, 400, 540, 480, 50, 1, 1.4)
    rrect(c, 690, 400, 540, 480, 50, "#FFFFFF")
    V.matriz(c, 960, 600, V.Det([["a", "b"], ["c", "d"]]), 1, 150, 120, 90)
    text_mid(c, "D = ?", 960, 810, 70, "black", GREEN)
    rrect(c, 410, 960, 1100, 80, 24, PURPLE)
    text_mid(c, "o valor pedido · e se a resposta é única", W / 2, 1000, 44, "black", "#FFFFFF")


def capa_qual(c):
    c.drawRect(skia.Rect.MakeWH(W, H), paint(mix("#FFFFFF", AMBER, 0.55), 1))
    selo_topo(c, W / 2, INK)
    s = "QUAL É O CERTO?"
    text(c, s, W / 2, 290, fit(s, 160, 1760), "black", INK)
    shadow_rrect(c, 160, 380, 860, 560, 44, 1, 1.4)
    rrect(c, 160, 380, 860, 560, 44, "#FFFFFF")
    V.matriz(c, 590, 660, V.DT("3 -2", "4 5"), 1, 220, 190, 130)
    for k, (s1, rot) in enumerate((("= 7 ?", -5), ("= 23 ?", 4))):
        y = 520 + k * 300
        c.save(); c.translate(1420, y); c.rotate(rot)
        shadow_rrect(c, -300, -110, 600, 220, 40, 1, 1.3)
        rrect(c, -300, -110, 600, 220, 40, "#FFFFFF", stroke=6, stroke_color=INK)
        text_mid(c, s1, 0, 0, 120, "black", INK)
        c.restore()


if __name__ == "__main__":
    for nome, fn in (("capa_A_d_zero_impossivel", capa_semaforo), ("capa_B_atalho_do_enem", capa_atalho),
                     ("capa_C_qual_e_o_certo", capa_qual)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
