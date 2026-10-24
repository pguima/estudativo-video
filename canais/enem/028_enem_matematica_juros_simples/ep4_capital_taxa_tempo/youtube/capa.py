"""Capas — Juros Simples, Episódio 4: descobrindo capital, taxa ou tempo (tema claro). 3 variações em 1280x720.
Formatos: A = as três pilhas do triplo ocupando a metade de baixo, pergunta no alto e o palpite errado riscado;
B = a mesa de quatro pernas com a perna que falta tracejada, título à esquerda; C = etiqueta de preço da geladeira
(à vista × a prazo) com a pergunta da taxa escondida."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · JUROS SIMPLES · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_triplo(c):
    background(c); selo_topo(c, W / 2)
    s = "TRIPLICA EM QUANTO TEMPO?"
    text(c, s, W / 2, 260, fit(s, 130, 1780), "black", INK)
    V.linha(c, [("a 2% ao mês", PURPLE), ("  ·  juros simples", INK2)], W / 2, 360, 64, 1.0)
    rrect(c, 0, 520, W, 560, 0, "#EAF4EC")
    for k in range(3):
        x = 330 + k * 420
        if k == 0:
            V.pilha(c, x, 950, 1.0, 9, 300, 80, col="#8FB4E8", col2="#4F7FC4")
            text(c, "CAPITAL", x, 1020, 52, "black", BLUE)
        else:
            V.pilha(c, x, 950, 1.0, 9, 300, 80)
            text(c, "JUROS", x, 1020, 52, "black", GREEN)
    rrect(c, 1420, 560, 440, 240, 30, "#FFFFFF", shadow=True)
    text(c, "12,5 anos?", 1640, 700, 70, "black", RED)
    V.strike(c, 1450, 720, 1830, 650, 1.0, RED)
    V.selo(c, 1640, 840, 1.0, "ERRADO!", RED, -8, 54)


def capa_mesa(c):
    background(c); selo_topo(c)
    text(c, "A LETRA", 84, 320, 140, "black", INK, align="left")
    text(c, "QUE FALTA", 84, 470, 140, "black", PURPLE, align="left")
    V.linha(c, [("J = C · i · t", PURPLE)], 84, 620, 80, 1.0, align="left")
    text(c, "capital, taxa ou tempo:", 84, 760, 54, "extrabold", INK2, align="left")
    text(c, "ache qualquer um", 84, 840, 54, "extrabold", GREEN, align="left")
    V.mesa(c, 1430, 430, 1.0, falta="i", prog=0.0, w=700, h=470, size=96)


def capa_geladeira(c):
    background(c); selo_topo(c, W / 2)
    s = "QUAL É A TAXA ESCONDIDA?"
    text(c, s, W / 2, 260, fit(s, 130, 1780), "black", INK)
    for k, (tit, l1, l2, col) in enumerate((("À VISTA", "R$ 1.000", "", BLUE),
                                            ("A PRAZO", "R$ 400", "+ R$ 660 em 2 meses", AMBER))):
        x = 180 + k * 820
        shadow_rrect(c, x, 360, 740, 520, 40, 1, 1.4)
        rrect(c, x, 360, 740, 520, 40, "#FFFFFF")
        rrect(c, x, 360, 740, 120, 40, col, 0.16)
        text(c, tit, x + 370, 445, 66, "black", col)
        text_mid(c, l1, x + 370, 640 if l2 else 660, 140, "black", INK)
        if l2:
            text(c, l2, x + 370, 800, 52, "extrabold", INK2)
    text_mid(c, "OU", W / 2, 620, 80, "black", GRAY)
    text(c, "a entrada NÃO é empréstimo", W / 2, 990, 60, "black", GREEN)


if __name__ == "__main__":
    for nome, fn in (("capa_A_triplica_em_quanto_tempo", capa_triplo), ("capa_B_a_letra_que_falta", capa_mesa),
                     ("capa_C_taxa_escondida", capa_geladeira)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
