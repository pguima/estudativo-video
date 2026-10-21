"""Capas — Matéria, Substâncias e Misturas, Episódio 5: Curva de aquecimento (tema claro). Gera 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "QUÍMICA DO ZERO · EPISÓDIO 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_termometro(c):
    background(c)
    selo(c)
    painel(c)
    V.V.termometro(c, 1260, 260, 1, 440, 0.55, RED)
    V.grafico(c, 1360, 330, 380, 380, 1, V.PURA, 1.0, INK, (), 22, larg=8)
    text(c, "é puro?", 1550, 860, 60, "black", BLUE)
    text(c, "PURO OU NÃO?", 80, 330, 120, "black", INK, align="left")
    text(c, "SÓ COM UM", 80, 460, 120, "black", INK, align="left")
    boxed(c, "TERMÔMETRO", 70, 520, 140, RED)
    text(c, "a curva de aquecimento do zero", 90, 860, 54, "extrabold", INK2, align="left")


def capa_patamares(c):
    background(c)
    selo(c)
    painel(c)
    V.grafico(c, 1220, 230, 500, 480, 1, V.PURA, 1.0, INK, (), 24, larg=9)
    V.patamar_rotulo(c, 1220, 230, 500, 480, V.PURA, 1, "1", 1, GREEN, -44, 30)
    V.patamar_rotulo(c, 1220, 230, 500, 480, V.PURA, 3, "2", 1, GREEN, -44, 30)
    text(c, "2 patamares = PURA", 1470, 860, 46, "black", GREEN)
    text(c, "O GRÁFICO", 80, 330, 128, "black", INK, align="left")
    text(c, "QUE MAIS CAI", 80, 460, 120, "black", INK, align="left")
    boxed(c, "NO ENEM", 70, 520, 150, GREEN)
    text(c, "conte os patamares", 90, 860, 56, "extrabold", INK2, align="left")


def capa_quatro(c):
    background(c)
    selo(c)
    painel(c)
    for k, (nome, pts, sub, _) in enumerate(V.QUATRO):
        x, y = 1170 + (k % 2) * 320, 180 + (k // 2) * 380
        V.grafico(c, x + 30, y + 30, 230, 200, 1, pts, 1.0, INK, (), 14, larg=6)
        text(c, nome, x + 145, y + 300, 30 if k != 2 else 24, "black", INK)
    text(c, "EUTÉTICA OU", 80, 330, 124, "black", INK, align="left")
    text(c, "AZEOTRÓPICA?", 80, 460, 118, "black", INK, align="left")
    boxed(c, "NUNCA MAIS ERRE", 70, 520, 104, PURPLE)
    text(c, "as 4 curvas do ENEM", 90, 860, 56, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_so_termometro", capa_termometro), ("capa_B_grafico_enem", capa_patamares), ("capa_C_4_curvas", capa_quatro)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
