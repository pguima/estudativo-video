"""Capas — Notação Científica e Ordem de Grandeza, Episódio 4: ordem de grandeza e conta de guardanapo (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 4", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_expoente(c):
    background(c); selo(c); painel(c)
    K.expr(c, "8,5·10^5", 1470, 300, 120, 1)
    K.fmid(c, "≠ 10⁵", 1470, 470, 100, "black", RED)
    text(c, "a ordem é", 1470, 600, 44, "black", INK2)
    K.expr(c, "10^6", 1470, 760, 170, 1, cores={0: GREEN})
    big(c, "ORDEM DE", 340)
    big(c, "GRANDEZA NÃO", 490)
    boxed(c, "É SÓ O EXPOENTE", 70, 540, 130, AMBER)
    text(c, "o critério certo, do zero", 90, 860, 46, "extrabold", INK2, align="left")


def capa_316(c):
    background(c); selo(c); painel(c)
    x0, x1, y = 1180, 1760, 560
    V._regua_log(c, x0, x1, y, 1)
    xm = (x0 + x1) / 2
    c.drawCircle(xm, y, 20, paint(GREEN, 1))
    V._arco(c, x0, xm, y - 30, GREEN, 1, "× 3,16", 60, 40)
    V._arco(c, xm, x1, y - 30, GREEN, 1, "× 3,16", 60, 40)
    K.expr(c, "√{10} ≈ 3,16", 1470, 760, 80, 1, cores={0: GREEN, 2: GREEN})
    big(c, "POR QUE 3,16", 340)
    big(c, "E NÃO", 495)
    boxed(c, "5?", 70, 545, 170, RED)
    text(c, "o meio do caminho multiplicando", 90, 860, 46, "extrabold", INK2, align="left")


def capa_guardanapo(c):
    background(c); selo(c); painel(c)
    V.guardanapo(c, 1470, 520, 600, 560, 1, -4)
    V.escrita(c, "4,7 → 5", 1250, 380, 56, 1)
    V.escrita(c, "8,2 → 8", 1250, 480, 56, 1)
    V.escrita(c, "≈ 4·10^9", 1470, 640, 90, 1, align="center")
    big(c, "ELIMINE", 340)
    big(c, "ALTERNATIVAS", 470)
    boxed(c, "SEM A CONTA", 70, 520, 140, GREEN)
    text(c, "a conta de guardanapo do ENEM", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_nao_e_o_expoente", capa_expoente), ("capa_B_por_que_3_16", capa_316),
                     ("capa_C_guardanapo", capa_guardanapo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
