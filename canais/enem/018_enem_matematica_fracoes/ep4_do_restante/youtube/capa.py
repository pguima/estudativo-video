"""Capas — Frações, Decimais e Dízimas, Episódio 4: A armadilha do "do restante" (tema claro). 3 variações em 1280x720."""
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


def capa_encolhe(c):
    background(c); selo(c); painel(c)
    pill(c, "CERTO", 1470, 190, GREEN, size=34, anchor="center", bounds=(0, 1920))
    V.encolhe(c, 0, 1200, 250, 540, 100, 1, 1, 1, ["1/3", "", ""], ["1/6", "", "", ""], 150, 36)
    pill(c, "ERRADO", 1470, 600, RED, size=34, anchor="center", bounds=(0, 1920))
    V.faixa(c, 1200, 660, 540, 100, 4, [RED], 1, ["1/4", "", "", ""], 36)
    check_icon(c, 1470, 870, 50, 1, RED, "x")
    big(c, "O ERRO QUE MAIS", 340)
    big(c, "CUSTA PONTO", 470)
    boxed(c, "EM FRAÇÕES", 70, 520, 140, AMBER)
    text(c, "a armadilha do “do restante”, do zero", 90, 860, 46, "extrabold", INK2, align="left")


def capa_reais(c):
    background(c); selo(c); painel(c)
    V.carteira(c, 1170, 200, 600, 300, 1)
    for i in range(8):
        V.nota(c, 1210 + (i % 4) * 135, 240 + (i // 4) * 85, 1)
    K.fmid(c, "1/4 de 800 = 200", 1510, 660, 58, "black", GREEN)
    check_icon(c, 1200, 660, 34, 1, GREEN)
    K.fmid(c, "1/4 de 1.200 = 300", 1510, 820, 52, "black", RED)
    V.strike(c, 1290, 820, 1730, 820, 1, RED, 1)
    check_icon(c, 1200, 820, 34, 1, RED, "x")
    big(c, "1/4 DO QUE SOBROU:", 340)
    big(c, "R$ 200 OU", 470)
    boxed(c, "R$ 300?", 70, 520, 160, RED)
    text(c, "o erro que mais custa ponto em frações", 90, 860, 46, "extrabold", INK2, align="left")


def capa_soma(c):
    background(c); selo(c); painel(c)
    K.expr(c, "1/3 + 1/4 = 7/12", 1470, 330, 76, 1.0, cores={4: RED})
    check_icon(c, 1470, 470, 46, 1, RED, "x")
    K.expr(c, "3/4 × 2/3 = 1/2", 1470, 650, 76, 1.0, cores={4: GREEN})
    pill(c, "ATALHO", 1470, 820, GREEN, size=40, anchor="center", bounds=(0, 1920))
    big(c, "1/3 E DEPOIS 1/4", 340)
    big(c, "DO RESTO NÃO É", 470)
    boxed(c, "7/12", 70, 520, 160, RED)
    text(c, "o atalho que resolve em um passo", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_erro_que_mais_custa", capa_encolhe), ("capa_B_200_ou_300", capa_reais),
                     ("capa_C_nao_e_7_12", capa_soma)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
