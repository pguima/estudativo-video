"""Capas — Cartografia, Episódio 6: Revisão (tema claro). Gera 3 variações em 1280x720."""
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
    pill(c, "CARTOGRAFIA · EPISÓDIO 6 · REVISÃO", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_pronto(c):
    background(c)
    selo(c)
    painel(c)
    pos = [(1300, 300), (1640, 300), (1470, 540), (1300, 780), (1640, 780)]
    for k, (x, y) in enumerate(pos):
        V.icon_ep(c, k, x, y, 110, 1)
    text(c, "ESTÁ PRONTO", 80, 340, 120, "black", INK, align="left")
    text(c, "PARA O", 80, 470, 140, "black", INK, align="left")
    boxed(c, "ENEM?", 70, 520, 160, GREEN)
    text(c, "toda a cartografia em 1 revisão", 90, 860, 54, "extrabold", INK2, align="left")


def capa_pegadinhas(c):
    background(c)
    selo(c)
    painel(c)
    for k, s in enumerate(("1 : 5 000 000 é grande?", "5° N a 15° S = 10°?", "Mercator = áreas reais?", "curvas juntas = plano?")):
        y = 260 + k * 170
        text(c, s, 1470, y, 40, "black", INK)
        text_mid(c, "FALSO", 1470, y + 60, 44, "black", RED)
    V.selo(c, 1470, 900, 1)
    text(c, "9 PEGADINHAS", 80, 340, 124, "black", INK, align="left")
    text(c, "QUE DERRUBAM", 80, 470, 116, "black", INK, align="left")
    boxed(c, "NO ENEM", 70, 520, 160, AMBER, INK)
    text(c, "verdadeiro ou falso: pause e responda", 90, 860, 50, "extrabold", INK2, align="left")


def capa_questoes(c):
    background(c)
    selo(c)
    painel(c)
    for k in range(5):
        y = 230 + k * 150
        V.icon_ep(c, k, 1240, y, 54, 1)
        text(c, f"Questão {k + 1}", 1320, y + 14, 48, "black", INK, align="left")
        check_icon(c, 1720, y, 30, 1, GREEN)
    text(c, "5 QUESTÕES", 80, 340, 136, "black", INK, align="left")
    text(c, "INÉDITAS", 80, 470, 136, "black", INK, align="left")
    boxed(c, "RESOLVIDAS", 70, 520, 140, PURPLE)
    text(c, "treino de cartografia para o ENEM", 90, 860, 52, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_pronto_para_o_enem", capa_pronto), ("capa_B_9_pegadinhas", capa_pegadinhas), ("capa_C_5_questoes", capa_questoes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
