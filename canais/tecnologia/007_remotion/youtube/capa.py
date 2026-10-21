"""Capas do vídeo Tecnologia 007 — Remotion (tema 'tech'). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
sys.path.insert(0, str(HERE.parent / "roteiro"))
import skia
import tech
from motor import *  # noqa
from tech import *  # noqa
import visual as V


def base(c, col=CYAN):
    tech.background(c, 3.0)
    m = 34
    for x, y, dx, dy in ((m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)):
        tech._bracket(c, x, y, dx, dy, col, 0.7)
    chip(c, "IA  ·  VÍDEO  ·  REACT", 84, 110, col, 1, size=34, filled=True)


def big(c, l1, l2, word, col):
    glow_text(c, l1, 80, 340, 128, "black", INK, 1, align="left", glow=0.15)
    glow_text(c, l2, 80, 480, 128, "black", INK, 1, align="left", glow=0.15)
    size = min(140, 140 * 900 / text_w(word, "black", 140))
    w = text_w(word, "black", size) + 70
    p = chamfer_path(70, 520, w, 175, 40)
    c.drawPath(p, blur_paint(col, 0.6, 26))
    c.drawPath(p, paint(col))
    text_mid(c, word, 70 + w / 2, 607, size, "black", "#03050B")


def lado_codigo(c):
    """código React em cima, vídeo resultante embaixo"""
    panel(c, 1140, 150, 680, 380, 1, VIOLET, label="Video.tsx")
    lines = [[("const ", V.KW), ("frame", V.NM), (" =", INK)],
             [("  useCurrentFrame", CYAN), ("();", INK)],
             [],
             [("<", INK), ("h1 ", V.NM), ("style", VIOLET), ("={{", INK)],
             [("  opacity", VIOLET), (": frame/", INK), ("30", GOLD)],
             [("}}>", INK), ("Olá!", LIME), ("</h1>", INK)]]
    code_lines(c, lines, 1180, 230, 36, 99, 0, a=1)
    arrow(c, 1480, 548, 1480, 615, CYAN, 1, 5, 18)
    panel(c, 1140, 630, 680, 330, 1, CYAN, label="video.mp4")
    V.canvas_frame(c, 1190, 670, 580, 90, 1, CYAN)


def lado_mil(c):
    panel(c, 1140, 150, 680, 810, 1, MAGENTA, label="1.000 renders")
    for i in range(24):
        V.thumb(c, 1175 + (i % 3) * 210, 200 + (i // 3) * 92, 195, 1, (CYAN, VIOLET, MAGENTA)[i % 3],
                V.NOMES[i % 12], f"R$ {1000 + 137 * i:,}".replace(",", "."), i)


def capa_codigo(c):
    base(c)
    big(c, "VÍDEO FEITO", "COM", "CÓDIGO", CYAN)
    text(c, "Remotion · React · agentes de IA", 90, 830, 50, "monob", INK2, align="left")
    lado_codigo(c)


def capa_mil(c):
    base(c, MAGENTA)
    big(c, "1 MODELO", "VIRA", "MIL VÍDEOS", MAGENTA)
    text(c, "vídeos a partir de dados", 90, 830, 54, "monob", INK2, align="left")
    lado_mil(c)


def capa_nome(c):
    base(c, VIOLET)
    glow_text(c, "Remotion", 80, 420, 190, "black", INK, 1, align="left", glow=0.3)
    text(c, "faça vídeos com React", 90, 520, 60, "black", CYAN, align="left")
    chip(c, "npx create-video@latest", 90, 640, LIME, 1, size=40, filled=True)
    text(c, "guia completo", 90, 830, 50, "monob", INK2, align="left")
    lado_codigo(c)


if __name__ == "__main__":
    for nome, fn in (("capa_A_video_com_codigo", capa_codigo), ("capa_B_mil_videos", capa_mil),
                     ("capa_C_remotion", capa_nome)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
