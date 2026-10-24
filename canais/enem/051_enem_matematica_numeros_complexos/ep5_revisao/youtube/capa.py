"""Capas — Números Complexos, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos (sem repetir as revisões anteriores nem as capas dos eps. 1–4): A = "VOCÊ CAI NESTAS?" com três pegadinhas
em cartões inclinados, cada uma com "?"; B = o índice da revisão: os 4 ícones dos episódios em grade 2 × 2 em volta do
"i", "COMPLEXOS EM 1 REVISÃO"; C = fundo escuro, "(1 − i)⁴ = ?" gigante com três palpites sem marcar o certo.
Nenhuma mostra gabarito.
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
    s = "MATEMÁTICA ENEM · NÚMEROS COMPLEXOS · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, cor, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, cor, size=34, anchor="center", bounds=(0, 1920))


def capa_pegadinhas(c):
    background(c)
    selo_topo(c, W / 2)
    s = "VOCÊ CAI NESTAS?"
    text(c, s, W / 2, 300, fit(s, 170, 1700), "black", INK)
    for k, (afirm, ang, col) in enumerate((("i² = 1", -4, AMBER), ("|3 + 4i| = 7", 3, RED), ("Δ < 0: sem raízes", -2, PURPLE))):
        x = 110 + k * 590
        c.save(); c.translate(x + 270, 690); c.rotate(ang)
        shadow_rrect(c, -270, -230, 540, 460, 40, 1, 1.4)
        rrect(c, -270, -230, 540, 460, 40, "#FFFFFF")
        rrect(c, -270, -230, 540, 26, 13, col)
        text(c, afirm, 0, 10, fit(afirm, 92, 470), "black", INK)
        c.drawCircle(0, 130, 64, paint(col, 1))
        text_mid(c, "?", 0, 130, 100, "black", "#FFFFFF")
        c.restore()


def capa_indice(c):
    background(c)
    selo_topo(c)
    for k, s in enumerate(("COMPLEXOS", "EM 1", "REVISÃO")):
        text(c, s, 84, 360 + k * 170, fit("COMPLEXOS", 160, 820), "black", INK if k != 2 else PURPLE, align="left")
    text(c, "potências · divisão · giros · De Moivre", 84, 900, 46, "bold", INK2, align="left")
    cx, cy = 1400, 600
    for k, (dx, dy) in enumerate(((-230, -230), (230, -230), (-230, 230), (230, 230))):
        shadow_rrect(c, cx + dx - 200, cy + dy - 200, 400, 400, 50, 1, 1.2)
        rrect(c, cx + dx - 200, cy + dy - 200, 400, 400, 50, "#FFFFFF")
        V.icone(c, k, cx + dx, cy + dy, 1.0, 1.0)
    c.drawCircle(cx, cy, 120, paint(PURPLE, 1))
    text_mid(c, "i", cx, cy, 170, "black", "#FFFFFF")


def capa_potencia(c):
    c.drawRect(skia.Rect.MakeWH(W, H), paint(INK, 1))
    selo_topo(c, W / 2, AMBER)
    s = "(1 − i)⁴ = ?"
    text(c, s, W / 2, 520, fit(s, 300, 1700), "black", "#FFFFFF")
    text(c, "sem calculadora", W / 2, 680, 64, "bold", mix("#FFFFFF", INK, 0.35))
    for k, (v, col) in enumerate((("4", BLUE), ("−4", PURPLE), ("16", GREEN))):
        x = W / 2 + (k - 1) * 420
        rrect(c, x - 170, 780, 340, 180, 40, mix(INK, col, 0.45))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 170, 780, 340, 180), 40, 40), paint(col, 1, stroke=8))
        text_mid(c, v + " ?", x, 870, 100, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_voce_cai_nestas", capa_pegadinhas), ("capa_B_complexos_em_1_revisao", capa_indice),
                     ("capa_C_um_menos_i_a_quarta", capa_potencia)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
