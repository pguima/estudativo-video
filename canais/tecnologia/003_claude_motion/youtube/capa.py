"""Capas do vídeo Tecnologia 003 — Claude Motion (tema 'tech', futurista). Gera 3 variações em 1280x720."""
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


def base(c):
    tech.background(c, 3.0)
    m = 34
    for x, y, dx, dy in ((m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)):
        tech._bracket(c, x, y, dx, dy, MAGENTA, 0.7)
    chip(c, "IA  ·  ANIMAÇÃO  ·  CLAUDE", 84, 110, MAGENTA, 1, size=34, filled=True)


def big(c, l1, l2, word, col):
    glow_text(c, l1, 80, 340, 128, "black", INK, 1, align="left", glow=0.15)
    glow_text(c, l2, 80, 480, 128, "black", INK, 1, align="left", glow=0.15)
    size = min(140, 140 * 900 / text_w(word, "black", 140))
    w = text_w(word, "black", size) + 70
    p = chamfer_path(70, 520, w, 175, 40)
    c.drawPath(p, blur_paint(col, 0.6, 26))
    c.drawPath(p, paint(col))
    text_mid(c, word, 70 + w / 2, 607, size, "black", "#03050B")


def capa_anima(c):
    base(c)
    big(c, "O CLAUDE", "AGORA FAZ", "ANIMAÇÃO", MAGENTA)
    text(c, "Claude Motion · exporta em MP4", 90, 830, 52, "monob", INK2, align="left")
    V.preview(c, 1140, 150, 680, 800, 2.6, 1, MAGENTA, "animacao.mp4")
    V.play_icon(c, 1700, 280, 56, MAGENTA, 1)


def capa_codigo(c):
    base(c)
    big(c, "NÃO É VÍDEO", "DE IA. É", "CÓDIGO", CYAN)
    text(c, "sem filmagem nem pessoas geradas", 90, 830, 50, "monob", INK2, align="left")
    panel(c, 1140, 150, 680, 800, 1, VIOLET, label="animacao.js")
    V.code(c, ["scene(1, duration=3)", "  text('Receita').fade_in()", "  bar_chart(q3).grow()",
               "scene(2, duration=4)", "  image('logo').move()"], 1180, 280, 32, 9, 0, 1, step=0.1)
    V.bars(c, 1220, 620, 520, 220, [0.4, 0.6, 0.5, 0.9], CYAN, 1, 1.0, hi=LIME)


def capa_nome(c):
    base(c)
    glow_text(c, "Claude", 80, 390, 170, "black", INK, 1, align="left", glow=0.0)
    for k in range(4, 0, -1):
        glow_text(c, "Motion", 80 - k * 30, 560, 170, "black", MAGENTA, 0.10 * (5 - k), align="left", glow=0.0)
    glow_text(c, "Motion", 80, 560, 170, "black", MAGENTA, 1, align="left", glow=0.7)
    chip(c, "NOVO · BETA", 90, 680, GOLD, 1, size=48, filled=True)
    text(c, "seu conteúdo em movimento, via /motion", 90, 830, 48, "monob", INK2, align="left")
    V.preview(c, 1140, 150, 680, 800, 3.5, 1, VIOLET, "preview")


if __name__ == "__main__":
    for nome, fn in (("capa_A_claude_anima", capa_anima), ("capa_B_e_codigo", capa_codigo),
                     ("capa_C_claude_motion", capa_nome)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
