"""Capas — Compreensão Global e Tese, Episódio 1: Tema, assunto e tese (tema claro). 3 variações em 1280x720."""
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
    pill(c, "LINGUAGENS ENEM · EPISÓDIO 1", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_assunto(c):
    background(c); selo(c); painel(c)
    V.folder(c, 1250, 260, 440, 170, "celular na escola", 1)
    pill(c, "ASSUNTO", 1470, 500, INK2, size=40, anchor="center", bounds=(0, 1920))
    text(c, "≠", 1470, 610, 90, "black", RED)
    V.boxed(c, 1190, 650, 560, 190, BLUE, 1, 0.08)
    text(c, "“deve ser ensinado,", 1470, 730, 40, "black", BLUE)
    text(c, "não só proibido”", 1470, 785, 40, "black", BLUE)
    pill(c, "TESE", 1470, 900, BLUE, size=40, anchor="center", bounds=(0, 1920))
    big(c, "ASSUNTO", 340)
    big(c, "NÃO É", 470)
    boxed(c, "TESE", 70, 520, 160, BLUE)
    text(c, "o erro que mais derruba em Linguagens", 90, 860, 50, "extrabold", INK2, align="left")


def capa_marcar(c):
    background(c); selo(c); painel(c)
    c.save(); c.translate(1470, 250); c.scale(0.5, 0.62); c.translate(-W / 2, -230)
    V.mesa(c, W / 2, 230, 1, "TESE", 1, None, top_size=80)
    c.restore()
    text(c, "tampo = TESE", 1470, 680, 52, "black", BLUE)
    text(c, "pernas = apoio", 1470, 760, 52, "black", INK2)
    pill(c, "ache o tampo", 1470, 870, GREEN, size=40, anchor="center", bounds=(0, 1920))
    big(c, "LEU O TEXTO", 340)
    big(c, "E NÃO SABE O", 470)
    boxed(c, "QUE MARCAR?", 70, 530, 118, AMBER, INK)
    text(c, "interpretação de texto do zero", 90, 860, 50, "extrabold", INK2, align="left")


def capa_palavras(c):
    background(c); selo(c); painel(c)
    V.boxed(c, 1180, 230, 580, 330, AMBER, 1, 0.12)
    text(c, "ALTERNATIVA", 1220, 290, 26, "black", AMBER, align="left", tracking=1)
    for j, s in enumerate(("celular · escola", "aluno · proibir...")):
        text(c, s, 1220, 380 + j * 80, 52, "black", INK, align="left")
    check_icon(c, 1470, 680, 80, 1, RED, "x")
    text(c, "as palavras do texto,", 1470, 840, 40, "black", INK2)
    text(c, "a tese do outro lado", 1470, 895, 40, "black", RED)
    big(c, "AS MESMAS", 340)
    big(c, "PALAVRAS,", 470)
    boxed(c, "OUTRA TESE", 70, 520, 150, RED)
    text(c, "a armadilha das alternativas no ENEM", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_assunto_nao_e_tese", capa_assunto), ("capa_B_nao_sabe_o_que_marcar", capa_marcar),
                     ("capa_C_mesmas_palavras", capa_palavras)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
