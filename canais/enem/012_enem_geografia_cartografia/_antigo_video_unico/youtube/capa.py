"""Capas do vídeo 012 — ENEM Geografia: Cartografia (tema claro). Gera 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

# reaproveita os contornos e desenhos do visual do vídeo
_spec = importlib.util.spec_from_file_location("visual012", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "GEOGRAFIA ENEM · CARTOGRAFIA", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_mente(c):
    background(c)
    selo(c)
    painel(c)
    text(c, "no mapa", 1470, 210, 44, "black", RED)
    V.blob(c, V.GREENLAND, 1170, 240, 270, 270, V.ICE, 1, "#64748B")
    V.blob(c, V.AFRICA, 1470, 240, 290, 300, V.LAND, 1)
    line(c, 1180, 580, 1760, 580, LINE, 1, 4)
    text(c, "na real", 1470, 640, 44, "black", GREEN)
    V.blob(c, V.GREENLAND, 1220, 700, 80, 80, V.ICE, 1, "#64748B")
    V.blob(c, V.AFRICA, 1440, 670, 230, 250, V.LAND, 1)
    text(c, "14×", 1330, 900, 60, "black", RED)
    text(c, "O MAPA DA", 80, 340, 124, "black", INK, align="left")
    text(c, "ESCOLA", 80, 470, 124, "black", INK, align="left")
    boxed(c, "MENTE", 70, 520, 150, RED)
    text(c, "projeções e escala no ENEM", 90, 840, 56, "extrabold", INK2, align="left")


def capa_escala(c):
    background(c)
    selo(c)
    painel(c)
    text(c, "1 : 2 000", 1470, 220, 60, "black", GREEN)
    for i in range(4):
        for j in range(2):
            rrect(c, 1200 + i * 135, 260 + j * 100, 115, 80, 8, "#E5E7EB")
            for q in range(3):
                c.drawRect(skia.Rect.MakeXYWH(1210 + i * 135 + q * 36, 272 + j * 100, 26, 24), paint("#F59E0B", 0.8))
    line(c, 1180, 520, 1760, 520, LINE, 1, 4)
    text(c, "1 : 2 000 000", 1470, 600, 60, "black", RED)
    rrect(c, 1220, 630, 500, 280, 16, V.SEA)
    V.blob(c, V.BRASIL, 1370, 640, 230, 260, V.LAND, 1)
    text(c, "QUAL ESCALA", 80, 340, 116, "black", INK, align="left")
    text(c, "É A MAIOR?", 80, 470, 124, "black", INK, align="left")
    boxed(c, "PEGADINHA", 70, 520, 140, BLUE)
    text(c, "escala grande x pequena no ENEM", 90, 840, 54, "extrabold", INK2, align="left")


def capa_curvas(c):
    background(c)
    selo(c)
    painel(c)
    cx0, cy = 1500, 540
    for k, lv in enumerate((100, 200, 300, 400)):
        cx, rx, ry = cx0 - 34 * k, 250 - 56 * k, 270 - 62 * k
        V.oval(c, cx, cy, rx, ry, "#A16207", 1, 7, fill="#FEF3C7" if k == 0 else None)
    text_mid(c, "▲", cx0 - 102, cy, 50, "black", INK)
    rrect(c, 1220, 440, 110, 200, 20, RED, 0.15)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1220, 440, 110, 200), 20, 20), paint(RED, 1, stroke=6))
    text(c, "ÍNGREME", 1470, 880, 52, "black", RED)
    text(c, "CURVAS", 80, 340, 140, "black", INK, align="left")
    text(c, "JUNTAS?", 80, 470, 124, "black", INK, align="left")
    boxed(c, "LADEIRA!", 70, 520, 150, AMBER, INK)
    text(c, "curvas de nível no ENEM", 90, 840, 56, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_mapa_mente", capa_mente), ("capa_B_qual_escala", capa_escala), ("capa_C_curvas_juntas", capa_curvas)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
