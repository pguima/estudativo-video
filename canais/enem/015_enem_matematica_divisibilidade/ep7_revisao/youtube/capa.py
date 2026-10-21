"""Capas — Divisibilidade, Primos, MMC e MDC, Episódio 7: revisão (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep7_revisao", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 7", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)

def capa_pegadinhas(c):
    background(c); selo(c); painel(c)
    V.selo(c, 1470, 300, 1, "VERDADEIRO", GREEN, -6, 62)
    V.selo(c, 1470, 500, 1, "FALSO", RED, 5, 80)
    V.selo(c, 1470, 720, 1, "PEGADINHA", AMBER, -4, 64)
    big(c, "VOCÊ CAI", 340)
    big(c, "NESSAS", 470)
    boxed(c, "9 PEGADINHAS?", 70, 520, 104, AMBER)
    text(c, "MMC, MDC, primos e divisores no ENEM", 90, 860, 48, "extrabold", INK2, align="left")


def capa_repete(c):
    background(c); selo(c); painel(c)
    for k, (nm, sub, ic, col) in enumerate((("REPETE", "MMC", 3, V.ORANGE), ("REPARTE", "MDC", 4, GREEN))):
        y = 300 + k * 330
        rrect(c, 1170, y - 120, 600, 250, 26, mix("#FFFFFF", col, 0.12))
        V.icone(c, ic, 1290, y, 1, 1.4, label=False)
        text(c, nm, 1570, y, 60, "black", col)
        text(c, sub, 1570, y + 70, 44, "black", INK2)
    big(c, "MMC OU MDC?", 340)
    big(c, "5 QUESTÕES", 470)
    boxed(c, "INÉDITAS", 70, 520, 150, BLUE)
    text(c, "treino com as pegadinhas que mais caem", 90, 860, 48, "extrabold", INK2, align="left")


def capa_serie(c):
    background(c); selo(c); painel(c)
    for k in range(6):
        V.icone(c, k, 1310 + (k % 2) * 320, 260 + (k // 2) * 260, 1, 1.5, label=True)
    big(c, "TUDO DE MMC,", 340)
    big(c, "MDC E PRIMOS", 470)
    boxed(c, "REVISÃO", 70, 520, 150, PURPLE)
    text(c, "os 6 episódios em uma aula", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_pegadinhas", capa_pegadinhas), ("capa_B_questoes_ineditas", capa_repete), ("capa_C_revisao_serie", capa_serie)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
