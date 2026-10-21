"""Capas — Compreensão Global e Tese, Episódio 2: O resumo em uma frase (tema claro). 3 variações em 1280x720."""
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
    pill(c, "LINGUAGENS ENEM · EPISÓDIO 2", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def pecas_verticais(c, y0=190, h=130):
    for k, (lab, col) in enumerate(V.PECAS):
        V.piece(c, 1200, y0 + k * (h + 26), 540, h, col, 1, lab.replace("O QUE O TEXTO AFIRMA", "O QUE AFIRMA"), size=40)
        if k < 2:
            text(c, "+", 1470, y0 + k * (h + 26) + h + 22, 44, "black", PURPLE)


def capa_resuma(c):
    background(c); selo(c); painel(c)
    pecas_verticais(c)
    pill(c, "= 1 FRASE", 1470, 760, PURPLE, size=56, anchor="center", bounds=(0, 1920))
    text(c, "a fórmula do resumo", 1470, 880, 40, "black", INK2)
    big(c, "RESUMA", 340)
    big(c, "QUALQUER TEXTO", 470)
    boxed(c, "EM 1 FRASE", 70, 520, 150, PURPLE)
    text(c, "o teste de que você entendeu o texto", 90, 860, 50, "extrabold", INK2, align="left")


def capa_entendeu(c):
    background(c); selo(c); painel(c)
    for k in range(9):
        line(c, 1200, 200 + k * 42, 1200 + 520 - (k % 3) * 90, 200 + k * 42, LINE, 1, 16)
    arrow(c, 1470, 590, 1470, 660, PURPLE, 1, 6, 22)
    V.boxed(c, 1180, 690, 580, 120, BLUE, 1, 0.08)
    text_mid(c, "1 FRASE", 1470, 750, 60, "black", BLUE)
    check_icon(c, 1470, 890, 44, 1, GREEN)
    big(c, "SE NÃO CABE", 340)
    big(c, "EM UMA FRASE,", 470)
    boxed(c, "NÃO ENTENDEU", 70, 530, 118, RED)
    text(c, "interpretação de texto do zero", 90, 860, 50, "extrabold", INK2, align="left")


def capa_antes(c):
    background(c); selo(c); painel(c)
    V.phone(c, 1170, 160, 600, 760, 1, "Você")
    segs = [("O sono do adolescente", V.C_ASS, 1), ("não combina com a escola,", V.C_AFI, 1), ("e testaram aulas mais tarde.", V.C_POR, 1)]
    V.wa_bubble(c, segs, 1240, 300, 480, 1, 40)
    text(c, "ANTES das opções", 1470, 760, 40, "black", PURPLE)
    check_icon(c, 1470, 850, 40, 1, GREEN)
    big(c, "ACHE A CERTA", 340)
    big(c, "ANTES DE LER AS", 470)
    boxed(c, "OPÇÕES", 70, 520, 160, GREEN)
    text(c, "o resumo em uma frase no ENEM", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_resuma_em_1_frase", capa_resuma), ("capa_B_nao_cabe_nao_entendeu", capa_entendeu),
                     ("capa_C_antes_das_opcoes", capa_antes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
