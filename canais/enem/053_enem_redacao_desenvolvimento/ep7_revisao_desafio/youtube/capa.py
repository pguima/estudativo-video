"""Capas — Redação ENEM, Desenvolvimento, Episódio 7: revisão, pegadinhas e desafio (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_dev_ep7", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def big(c, s, y, maxw=1000, size=140):
    while text_w(s, "black", size) > maxw:
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34, maxw=1010):
    while text_w(s, "black", size) + pad * 2 > maxw:
        size -= 2
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "REDAÇÃO ENEM · DESENVOLVIMENTO · EP. 7", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 160, 700, 800, r=36)


def capa_pegadinhas(c):
    background(c); selo(c); painel(c)
    V.selo(c, 1470, 330, 1, "VERDADEIRO", GREEN, -6, 64)
    V.selo(c, 1470, 520, 1, "FALSO", RED, 5, 84)
    V.selo(c, 1470, 730, 1, "PEGADINHA", AMBER, -4, 74)
    text(c, "10 erros · 10 pausas", 1470, 890, 40, "black", INK2)
    big(c, "VOCÊ CAI NESSAS", 340)
    big(c, "10 PEGADINHAS?", 470)
    boxed(c, "DESENVOLVIMENTO", 70, 530, 104, AMBER)
    text(c, "o parágrafo que prova a tese da redação", 90, 860, 44, "extrabold", INK2, align="left")


def capa_desafio(c):
    background(c); selo(c); painel(c)
    rows = [("TESE", V.MOV["tese"], "posição"), ("TÓPICO 1", V.PARTE["topico"], "razão 1"),
            ("TÓPICO 2", V.PARTE["topico"], "razão 2")]
    for k, (s, col, sub) in enumerate(rows):
        y = 250 + k * 190
        rrect(c, 1170, y, 600, 150, 18, "#FFFFFF", 1, shadow=True)
        rrect(c, 1170, y, 14, 150, 7, col, 1)
        text(c, s, 1215, y + 62, 40, "black", col, align="left", tracking=2)
        text(c, sub, 1215, y + 116, 34, "bold", INK2, align="left")
        for j in range(2):
            line(c, 1520, y + 52 + j * 30, 1730 - j * 60, y + 52 + j * 30, LIGHT, 1, 10)
    V.selo(c, 1470, 860, 1, "PROJETO VISÍVEL ✓", GREEN, -4, 50)
    big(c, "3 FRASES PROVAM", 340)
    big(c, "SUA REDAÇÃO?", 470)
    boxed(c, "O TESTE FINAL", 70, 530, 120, GREEN)
    text(c, "desafio prático do desenvolvimento", 90, 860, 50, "extrabold", INK2, align="left")


def capa_revisao(c):
    background(c); selo(c); painel(c)
    for k in range(6):
        V.ep_icone(c, k, 1310 + (k % 2) * 320, 290 + (k // 2) * 240, 1, 1.3, label=True)
    big(c, "O DESENVOLVIMENTO", 340)
    big(c, "EM 1 AULA", 470)
    boxed(c, "REVISÃO COMPLETA", 70, 530, 104, PURPLE)
    text(c, "V ou F, 5 questões inéditas e desafio", 90, 860, 48, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_pegadinhas", capa_pegadinhas), ("capa_B_teste_final", capa_desafio),
                     ("capa_C_revisao_completa", capa_revisao)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
