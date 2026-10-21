"""Capas — Operações e Conjuntos Numéricos, Episódio 1: Ordem das operações e regra de sinais (tema claro). 3 variações em 1280x720."""
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


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = V.ftext_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    V.fmid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA BÁSICA · EPISÓDIO 1", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def resposta(c, s, y):
    rrect(c, 1180, y - 110, 580, 220, 28, BLUE, 0.10)
    V.fmid(c, s, 1420, y, 150, "black", BLUE)
    V.fmid(c, "?", 1680, y, 110, "black", AMBER)


def capa_14_ou_20(c):
    background(c)
    selo(c)
    painel(c)
    V.fmid(c, "2 + 3 × 4", 1470, 250, 96, "black", INK)
    resposta(c, "14", 480)
    resposta(c, "20", 760)
    text(c, "QUANTO DÁ", 80, 340, 128, "black", INK, align="left")
    text(c, "ISSO?", 80, 470, 140, "black", INK, align="left")
    boxed(c, "14 ou 20", 70, 520, 160, AMBER, INK)
    text(c, "ordem das operações do zero", 90, 860, 56, "extrabold", INK2, align="left")


def capa_erro_caro(c):
    background(c)
    selo(c)
    painel(c)
    V.fmid(c, "−3^2 = −9", 1470, 340, 120, "black", RED)
    text(c, "sem parênteses", 1470, 450, 40, "black", INK2)
    line(c, 1200, 540, 1740, 540, LINE, 1, 4)
    V.fmid(c, "(−3)^2 = 9", 1470, 680, 120, "black", GREEN)
    text(c, "com parênteses", 1470, 790, 40, "black", INK2)
    text(c, "O ERRO", 80, 340, 140, "black", INK, align="left")
    text(c, "MAIS CARO", 80, 470, 140, "black", INK, align="left")
    boxed(c, "DA PROVA", 70, 520, 160, RED)
    text(c, "regra de sinais no ENEM", 90, 860, 56, "extrabold", INK2, align="left")


def capa_menos_com_menos(c):
    background(c)
    selo(c)
    painel(c)
    V.extrato(c, 1e9, 1170, 180, 600, [(0, "Dívida", -7), (0, "Entrou", 3)], 0, -4)
    V.fmid(c, "−(−12) = +12", 1470, 760, 84, "black", GREEN)
    text(c, "cancelar dívida = ganhar", 1470, 860, 36, "black", INK2)
    text(c, "MENOS COM", 80, 340, 140, "black", INK, align="left")
    text(c, "MENOS", 80, 470, 140, "black", INK, align="left")
    boxed(c, "DÁ MAIS?", 70, 520, 160, PURPLE)
    text(c, "sinais explicados com dinheiro", 90, 860, 56, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_14_ou_20", capa_14_ou_20), ("capa_B_erro_mais_caro", capa_erro_caro),
                     ("capa_C_menos_com_menos", capa_menos_com_menos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
