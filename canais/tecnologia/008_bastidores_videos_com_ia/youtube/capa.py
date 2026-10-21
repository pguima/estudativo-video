"""Capas do vídeo Tecnologia 008 — Bastidores: como eu faço estes vídeos com IA (tema 'tech'). Gera 3 variações em 1280x720."""
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
    chip(c, "IA  ·  BASTIDORES  ·  PYTHON", 84, 110, col, 1, size=34, filled=True)


def big(c, l1, l2, word, col):
    glow_text(c, l1, 80, 340, 120, "black", INK, 1, align="left", glow=0.15)
    glow_text(c, l2, 80, 470, 120, "black", INK, 1, align="left", glow=0.15)
    size = min(140, 140 * 900 / text_w(word, "black", 140))
    w = text_w(word, "black", size) + 70
    p = chamfer_path(70, 520, w, 175, 40)
    c.drawPath(p, blur_paint(col, 0.6, 26))
    c.drawPath(p, paint(col))
    text_mid(c, word, 70 + w / 2, 607, size, "black", "#03050B")


def lado_quadros(c):
    for k, (f, col) in enumerate((("enem.png", CYAN), ("seguridade.png", LIME), ("tecnologia.png", VIOLET))):
        V.picture(c, f, 1250, 150 + k * 290, 470, 1, col)


def lado_pipeline(c):
    panel(c, 1140, 150, 680, 810, 1, CYAN, label="pipeline")
    for k, (lab, tool, col) in enumerate(V.PIPE):
        y = 250 + k * 145
        node(c, 1260, y, 52, None, None, col, 1, 0.0, glyph=str(k + 1), gsize=38)
        text(c, lab, 1340, y - 4, 42, "black", INK, 1, align="left")
        text(c, tool, 1340, y + 40, 30, "monob", col, 1, align="left")


def capa_sem_camera(c):
    base(c)
    big(c, "SEM CÂMERA,", "SEM MICROFONE:", "SÓ IA", CYAN)
    text(c, "como eu faço estes vídeos", 90, 830, 54, "monob", INK2, align="left")
    lado_quadros(c)


def capa_53(c):
    base(c, MAGENTA)
    big(c, "53 VÍDEOS", "FEITOS COM", "CÓDIGO", MAGENTA)
    text(c, "os bastidores do pipeline", 90, 830, 54, "monob", INK2, align="left")
    lado_quadros(c)


def capa_pipeline(c):
    base(c, LIME)
    big(c, "MEU PIPELINE", "DE VÍDEO", "COM IA", LIME)
    text(c, "Claude · Gemini · Whisper · Skia · ffmpeg", 90, 830, 40, "monob", INK2, align="left")
    lado_pipeline(c)


if __name__ == "__main__":
    for nome, fn in (("capa_A_sem_camera", capa_sem_camera), ("capa_B_53_videos", capa_53), ("capa_C_pipeline", capa_pipeline)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
