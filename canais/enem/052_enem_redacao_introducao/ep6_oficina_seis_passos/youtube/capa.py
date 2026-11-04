"""Capas — Redação ENEM, Introdução, Episódio 6: Oficina — montando uma introdução do zero (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike  # noqa

_spec = importlib.util.spec_from_file_location("visual_intro_ep6", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


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
    pill(c, "REDAÇÃO ENEM · INTRODUÇÃO · EP. 6", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_passos(c):
    background(c); selo(c); painel(c)
    V.checklist(c, 3, 1.0, feitos=3, x=1170, y=190, w=600)
    big(c, "MONTE COMIGO", 340)
    big(c, "A INTRODUÇÃO", 470)
    boxed(c, "EM 6 PASSOS", 70, 520, 140, GREEN)
    text(c, "do rascunho ao parágrafo pronto", 90, 860, 50, "extrabold", INK2, align="left")


def capa_primordios(c):
    background(c); selo(c); painel(c)
    V.paper(c, 1160, 170, 620, 740, 1.0, lh=56, top=230)
    V.hand_para(c, "Desde os primórdios, os povos indígenas...", 1250, 330, 44, V.PEN, 1.0, 500, 64)
    strike(c, 1244, 318, 1690, 318, 1.0, RED, 1.0)
    strike(c, 1244, 382, 1560, 382, 1.0, RED, 1.0)
    V.xmark(c, 1660, 470, 46, 1.0)
    V.hand_para(c, "A Constituição Federal de 1988 reconhece...", 1250, 620, 40, V.PEN, 1.0, 500, 60)
    check_icon(c, 1660, 790, 46, 1.0, GREEN)
    big(c, "“DESDE OS", 340)
    big(c, "PRIMÓRDIOS”?", 470)
    boxed(c, "RISQUE ISSO", 70, 520, 140, RED)
    text(c, "a introdução certa, ao vivo, com tema real", 90, 860, 46, "extrabold", INK2, align="left")


def capa_dez(c):
    background(c); selo(c); painel(c)
    V.clock(c, 1470, 430, 210, 1.0, 0.75, "10 min")
    for k, key in enumerate(["mapa", "rua", "tese", "lista"]):
        V.icone_peca(c, key, 1250 + k * 147, 810, 1.0, 1.0)
    big(c, "INTRODUÇÃO", 340)
    big(c, "DO ENEM EM", 470)
    boxed(c, "10 MINUTOS", 70, 520, 140, MOV_T)
    text(c, "uma ordem de trabalho para qualquer tema", 90, 860, 46, "extrabold", INK2, align="left")


MOV_T = V.MOV["tese"]

if __name__ == "__main__":
    for nome, fn in (("capa_A_seis_passos", capa_passos), ("capa_B_desde_os_primordios", capa_primordios),
                     ("capa_C_dez_minutos", capa_dez)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
