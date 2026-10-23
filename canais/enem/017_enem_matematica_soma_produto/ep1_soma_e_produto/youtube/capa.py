"""Capas — Equação do 2º grau sem Bhaskara: Soma e Produto (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_017_ep1", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def big(c, s, y, maxw=1000, size=140):
    while V.ftext_w(s, "black", size) > maxw:
        size -= 4
    V.ftext(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = V.ftext_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    V.fmid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA ENEM · SOMA E PRODUTO", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def mini_tabela(c, x, y, rows, ok_row, size=46, rh=96):
    rrect(c, x, y, 600, 62, 16, INK)
    for j, (hd, cx) in enumerate((("NÚMEROS", 120), ("SOMA", 300), ("PRODUTO", 480))):
        text_mid(c, hd, x + cx, y + 31, 22, "black", "#FFFFFF", tracking=2)
    for k, r in enumerate(rows):
        yy = y + 72 + k * rh
        if k == ok_row:
            rrect(c, x - 8, yy, 616, rh - 8, 18, GREEN, 0.14)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 8, yy, 616, rh - 8), 18, 18), paint(GREEN, 1, stroke=4))
        for s, cx in zip(r, (120, 300, 480)):
            V.fmid(c, s, x + cx, yy + (rh - 8) / 2, size, "black", GREEN if k == ok_row else INK)


def capa_segundos(c):
    background(c); selo(c); painel(c)
    V.fbox(c, "x² − 5x + 6 = 0", 1470, 230, 50, 1.0, INK)
    V.V16.bhaskara_formula(c, 1450, 370, 1.0, 40, GRAY)
    line(c, 1250, 420, 1650, 320, RED, 1.0, 9)
    V.fmid(c, "soma 5 · produto 6", 1470, 560, 48, "black", BLUE)
    V.fmid(c, "↓", 1470, 655, 60, "black", GRAY)
    V.fbox(c, "x = 2  e  x = 3", 1470, 770, 60, 1.0, GREEN)
    big(c, "2º GRAU EM", 340)
    big(c, "SEGUNDOS", 470)
    boxed(c, "SEM BHASKARA", 70, 520, 112, GREEN)
    text(c, "só com soma e produto, do zero", 90, 860, 50, "extrabold", INK2, align="left")


def capa_tabela(c):
    background(c); selo(c); painel(c)
    V.fmid(c, "x² − 5x + 6 = 0", 1470, 230, 54, "black", INK)
    mini_tabela(c, 1170, 330, [("1 e 6", "7", "6"), ("2 e 3", "5", "6")], 1)
    V.fmid(c, "soma 5 ✓   produto 6 ✓", 1470, 650, 40, "black", GREEN)
    V.fbox(c, "raízes: 2 e 3", 1470, 790, 60, 1.0, GREEN)
    big(c, "SÓ OLHANDO", 340)
    big(c, "OS NÚMEROS", 470)
    boxed(c, "SOMA E PRODUTO", 70, 520, 98, BLUE)
    text(c, "equação do 2º grau sem decorar fórmula", 90, 860, 48, "extrabold", INK2, align="left")


def capa_sinal(c):
    background(c); selo(c); painel(c)
    V.fmid(c, "x² − 5x + 6 = 0", 1470, 230, 54, "black", INK)
    V.mrow(c, [("t", "soma = ", PURPLE), ("t", "−", PURPLE), ("f", "b", "a", PURPLE)], 1470, 380, 76, align="center")
    check_icon(c, 1250, 560, 34, 1.0, RED, "x")
    V.fmid(c, "soma = −5", 1300, 560, 58, "black", RED, align="left")
    line(c, 1300, 560, 1300 + V.ftext_w("soma = −5", "black", 58), 560, RED, 1.0, 6)
    check_icon(c, 1250, 690, 34, 1.0, GREEN)
    V.fmid(c, "soma = +5", 1300, 690, 58, "black", GREEN, align="left")
    V.fmid(c, "→  2 e 3", 1470, 830, 60, "black", GREEN)
    big(c, "O SINAL QUE", 340)
    big(c, "QUASE TODOS", 470)
    boxed(c, "ERRAM", 70, 520, 150, RED)
    text(c, "soma e produto (Relações de Girard)", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_raizes_em_segundos", capa_segundos), ("capa_B_tabela_soma_produto", capa_tabela),
                     ("capa_C_sinal_da_soma", capa_sinal)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
