"""Capas — Matéria, Substâncias e Misturas, Episódio 6: Revisão (tema claro). Gera 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep6", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "QUÍMICA DO ZERO · EPISÓDIO 6 · REVISÃO", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_roteiro(c):
    background(c)
    selo(c)
    painel(c)
    for k, (s, col) in enumerate((("1 substância ou mais?", PURPLE), ("1 elemento ou mais?", PURPLE), ("quantas fases?", PURPLE))):
        y = 280 + k * 230
        badge_num(c, k + 1, 1210, y, 1, 40, bg=col)
        text_mid(c, s, 1270, y, 40, "black", INK, align="left")
    text(c, "3 PERGUNTAS", 80, 340, 128, "black", INK, align="left")
    text(c, "CLASSIFICAM", 80, 470, 124, "black", INK, align="left")
    boxed(c, "QUALQUER MATERIAL", 70, 535, 84, PURPLE)
    text(c, "revisão de matéria, substâncias e misturas", 90, 860, 48, "extrabold", INK2, align="left")


def capa_pegadinhas(c):
    background(c)
    selo(c)
    painel(c)
    for k, s in enumerate(("O₂ é composta?", "ar é puro?", "3 cubos = 4 fases?", "1 patamar = puro?")):
        y = 260 + k * 170
        text(c, s, 1470, y, 42, "black", INK)
        text_mid(c, "FALSO", 1470, y + 60, 44, "black", RED)
    V.selo(c, 1470, 900, 1)
    text(c, "9 PEGADINHAS", 80, 340, 124, "black", INK, align="left")
    text(c, "DE QUÍMICA", 80, 470, 124, "black", INK, align="left")
    boxed(c, "NO ENEM", 70, 520, 160, AMBER, INK)
    text(c, "verdadeiro ou falso: pause e responda", 90, 860, 50, "extrabold", INK2, align="left")


def capa_questoes(c):
    background(c)
    selo(c)
    painel(c)
    for k in range(5):
        y = 230 + k * 150
        V.icone_ep(c, [2, 1, 3, 4, 4][k], 1240, y, 54, 1)
        text(c, f"Questão {k + 1}", 1320, y + 14, 48, "black", INK, align="left")
        check_icon(c, 1720, y, 30, 1, GREEN)
    text(c, "5 QUESTÕES", 80, 340, 136, "black", INK, align="left")
    text(c, "INÉDITAS", 80, 470, 136, "black", INK, align="left")
    boxed(c, "RESOLVIDAS", 70, 520, 140, GREEN)
    text(c, "treino de química para o ENEM", 90, 860, 52, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_3_perguntas", capa_roteiro), ("capa_B_9_pegadinhas", capa_pegadinhas), ("capa_C_5_questoes", capa_questoes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
