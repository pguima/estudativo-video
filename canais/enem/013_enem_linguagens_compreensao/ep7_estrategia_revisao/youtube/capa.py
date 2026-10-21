"""Capas — Compreensão Global e Tese, Episódio 7: Revisão, pegadinhas e treino (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep7", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "LINGUAGENS ENEM · EPISÓDIO 7", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_pegadinhas(c):
    background(c); selo(c); painel(c)
    rows = [("REDUÇÃO", AMBER), ("EXTRAPOLAÇÃO", AMBER), ("CONTRADIÇÃO", RED), ("TEMA CERTO, TESE ERRADA", AMBER),
            ("VERDADE DO MUNDO", AMBER)]
    for k, (s, col) in enumerate(rows):
        y = 220 + k * 140
        rrect(c, 1180, y, 580, 100, 18, mix("#FFFFFF", col, 0.14))
        check_icon(c, 1230, y + 50, 24, 1, RED, "x")
        text(c, s, 1280, y + 64, 36 if len(s) < 16 else 28, "black", col if col == RED else INK, 1, align="left")
    big(c, "AS 5", 340)
    big(c, "PEGADINHAS", 470)
    boxed(c, "DA TESE", 70, 520, 150, AMBER, INK)
    text(c, "e 5 questões inéditas para treinar", 90, 860, 50, "extrabold", INK2, align="left")


def capa_vf(c):
    background(c); selo(c); painel(c)
    for k, (s, ok) in enumerate((("A 1ª frase é sempre a tese.", False), ("Texto sem opinião pode ter tese.", True),
                                  ("Elogio irônico é elogio.", False))):
        y = 230 + k * 240
        V.para(c, s, 1470, y + 40, 34, "black", INK, 1, 620, 42, align="center")
        V.selo(c, 1470, y + 165, 1, "VERDADEIRO" if ok else "FALSO", GREEN if ok else RED, -6, 40)
    big(c, "VOCÊ CAI", 340)
    big(c, "NESTAS", 470)
    boxed(c, "PEGADINHAS?", 70, 520, 130, RED)
    text(c, "revisão de compreensão global e tese", 90, 860, 46, "extrabold", INK2, align="left")


def capa_revisao(c):
    background(c); selo(c); painel(c)
    for k in range(6):
        cx = 1300 + (k % 2) * 340
        cy = 260 + (k // 2) * 250
        V.icone(c, k, cx, cy, 1.5, 1)
        ep_, nome, _, col = V.EPS[k]
        text(c, nome, cx, cy + 125, 30, "black", col)
    big(c, "TESE NO ENEM", 340)
    big(c, "REVISÃO", 470)
    boxed(c, "COMPLETA", 70, 520, 150, BLUE)
    text(c, "os 6 episódios em uma aula", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_pegadinhas", capa_pegadinhas), ("capa_B_verdadeiro_falso", capa_vf),
                     ("capa_C_revisao", capa_revisao)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
