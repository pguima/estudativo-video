"""Capas — Cartografia, Episódio 4: Curvas de nível (tema claro). Gera 3 variações em 1280x720."""
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


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "CARTOGRAFIA · EPISÓDIO 4", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_perigo(c):
    background(c)
    selo(c)
    painel(c)
    V.mountain(c, 1470, 540, 0.95, 1, labels=True)
    hx, hy = V.u2x(-300, 1470, 0.95), 540
    rrect(c, hx - 26, hy - 20, 52, 40, 4, "#FFFFFF"); c.drawRect(skia.Rect.MakeXYWH(hx - 26, hy - 20, 52, 40), paint(INK, 1, stroke=3))
    p = skia.Path(); p.moveTo(hx - 34, hy - 20); p.lineTo(hx, hy - 50); p.lineTo(hx + 34, hy - 20); p.close(); c.drawPath(p, paint(RED))
    c.drawCircle(hx, hy - 6, 70, paint(RED, 1, stroke=7))
    text(c, "≥ 30%: risco", 1470, 880, 52, "black", RED)
    text(c, "DÁ PARA", 80, 340, 136, "black", INK, align="left")
    text(c, "CONSTRUIR", 80, 470, 136, "black", INK, align="left")
    boxed(c, "AQUI?", 70, 520, 160, RED)
    text(c, "curvas de nível no ENEM", 90, 860, 56, "extrabold", INK2, align="left")


def capa_fatias(c):
    background(c)
    selo(c)
    painel(c)
    V.mountain(c, 1480, 640, 0.9, 1, tilt=0.32, gap=28)
    for k in range(4):
        y = 640 - (70 * k + 28 * k) * 0.9 * 0.68 - 6
        text(c, f"{100 * (k + 1)} m", V.u2x(V.RINGS[k][1], 1480, 0.9) + 20, y, 30, "black", V.BROWN, align="left")
    text(c, "fatias de 100 m", 1470, 860, 46, "black", AMBER)
    text(c, "FATIE O", 80, 340, 136, "black", INK, align="left")
    text(c, "MORRO EM", 80, 470, 136, "black", INK, align="left")
    boxed(c, "CAMADAS", 70, 520, 160, GREEN)
    text(c, "entenda as curvas de nível de vez", 90, 860, 50, "extrabold", INK2, align="left")


def capa_escada(c):
    background(c)
    selo(c)
    painel(c)
    V.stairs(c, 1200, 520, 45, 70, 5, RED, 1)
    text(c, "colados = ÍNGREME", 1470, 590, 40, "black", RED)
    V.stairs(c, 1200, 860, 105, 40, 5, GREEN, 1)
    text(c, "espaçados = SUAVE", 1470, 920, 40, "black", GREEN)
    text(c, "CURVAS", 80, 340, 140, "black", INK, align="left")
    text(c, "JUNTAS =", 80, 470, 140, "black", INK, align="left")
    boxed(c, "LADEIRA", 70, 520, 160, AMBER, INK)
    text(c, "relevo e declividade no ENEM", 90, 860, 54, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_construir_aqui", capa_perigo), ("capa_B_morro_de_cima", capa_fatias), ("capa_C_curvas_juntas", capa_escada)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
