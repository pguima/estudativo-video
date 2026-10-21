"""Capas — Operações e Conjuntos Numéricos, Episódio 2: Os conjuntos numéricos (tema claro). 3 variações em 1280x720."""
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


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = V.ftext_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    V.fmid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA BÁSICA · EPISÓDIO 2", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_nunca_termina(c):
    background(c)
    selo(c)
    painel(c)
    V.quadrado_diag(c, 1360, 220, 230, 1)
    V.fmid(c, "√2 =", 1470, 640, 90, "black", V.CI)
    V.fmid(c, "1,41421356…", 1470, 770, 76, "black", INK)
    pill(c, "nunca termina · nunca repete", 1470, 880, RED, size=30, anchor="center", bounds=(0, 1920))
    text(c, "O NÚMERO", 80, 340, 140, "black", INK, align="left")
    text(c, "QUE NUNCA", 80, 470, 140, "black", INK, align="left")
    boxed(c, "TERMINA", 70, 520, 160, V.CI)
    text(c, "racional ou irracional? do zero", 90, 860, 56, "extrabold", INK2, align="left")


def capa_raiz(c):
    background(c)
    selo(c)
    painel(c)
    V.fmid(c, "√9 = 3", 1470, 320, 120, "black", GREEN)
    pill(c, "RACIONAL", 1470, 440, GREEN, size=36, anchor="center", bounds=(0, 1920))
    line(c, 1200, 540, 1740, 540, LINE, 1, 4)
    V.fmid(c, "√10 = 3,162…", 1470, 660, 82, "black", RED)
    pill(c, "IRRACIONAL", 1470, 780, RED, size=36, anchor="center", bounds=(0, 1920))
    text(c, "TER RAIZ", 80, 340, 140, "black", INK, align="left")
    text(c, "NÃO É SER", 80, 470, 140, "black", INK, align="left")
    boxed(c, "IRRACIONAL", 70, 520, 150, AMBER, INK)
    text(c, "a pegadinha que cai no ENEM", 90, 860, 56, "extrabold", INK2, align="left")


def capa_bonecas(c):
    background(c)
    selo(c)
    painel(c)
    V.bonecas(c, 1e9, 1440, 640, 0.55, dict(N=0, Z=0, Q=0, I=0, R=0),
              ex=dict(Q=[(0, "1/2")], I=[(0, "√2"), (0, "π")]))
    for k, (h, col, lab) in enumerate(((230, V.CR, "ℝ"), (190, V.CQ, "ℚ"), (150, V.CZ, "ℤ"), (110, V.CN, "ℕ"))):
        V.boneca(c, 1240 + k * 150, 400, h, col, 1, lab)
    text(c, "OS NÚMEROS", 80, 340, 128, "black", INK, align="left")
    text(c, "SÃO", 80, 470, 140, "black", INK, align="left")
    boxed(c, "BONECAS RUSSAS", 70, 530, 98, V.CQ)
    text(c, "conjuntos numéricos do zero", 90, 860, 56, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_nunca_termina", capa_nunca_termina), ("capa_B_ter_raiz", capa_raiz),
                     ("capa_C_bonecas_russas", capa_bonecas)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
