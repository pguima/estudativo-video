"""Capas do vídeo Tecnologia 001 — REA (tema 'tech', futurista). Gera 3 variações em 1280x720."""
import math, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import tech
from motor import *  # noqa
from tech import *  # noqa

HEXL = ["8B 45 FC 0F AF 45 F8 89", "C7 45 F4 00 00 80 3F F3", "0F 10 45 F4 F3 0F 59 C1", "E8 2A 01 00 00 48 8B 4D",
        "F0 31 C0 85 C9 74 0B 83", "F9 5B 74 1E 83 F9 5C 74"]


def base(c):
    tech.background(c, 3.0)
    m = 34
    for x, y, dx, dy in ((m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)):
        tech._bracket(c, x, y, dx, dy, CYAN, 0.7)
    chip(c, "IA  ·  ENGENHARIA REVERSA", 84, 110, CYAN, 1, size=34, filled=True)


def big(c, l1, l2, word, col):
    glow_text(c, l1, 80, 340, 128, "black", INK, 1, align="left", glow=0.15)
    glow_text(c, l2, 80, 480, 128, "black", INK, 1, align="left", glow=0.15)
    size = min(140, 140 * 900 / text_w(word, "black", 140))
    w = text_w(word, "black", size) + 70
    p = chamfer_path(70, 520, w, 175, 40)
    c.drawPath(p, blur_paint(col, 0.6, 26))
    c.drawPath(p, paint(col))
    text_mid(c, word, 70 + w / 2, 607, size, "black", "#03050B")


def capa_por_dentro(c):
    base(c)
    big(c, "A IA ABRE", "QUALQUER", "PROGRAMA", CYAN)
    text(c, "REA · open source · github", 90, 830, 54, "monob", INK2, align="left")
    panel(c, 1140, 150, 680, 800, 1, CYAN, label="app.exe")
    for i, h in enumerate(HEXL):
        text(c, h, 1190, 260 + i * 58, 36, "mono", INK2 if i != 3 else CYAN, align="left")
    c.drawRect(skia.Rect.MakeXYWH(1160, 222 + 3 * 58, 640, 52), blur_paint(CYAN, 0.35, 10))
    node(c, 1480, 760, 120, None, None, MAGENTA, 1, 0, glyph="AI", gsize=86)


def capa_porcentagem(c):
    base(c)
    big(c, "A IA LEU O", "BINÁRIO DA", "CALCULADORA", MAGENTA)
    text(c, "e achou 2 regras escondidas no %", 90, 830, 50, "monob", INK2, align="left")
    panel(c, 1140, 150, 680, 800, 1, MAGENTA, label="Calculator x64")
    glow_text(c, "200 + 10%", 1480, 330, 84, "black", INK, 1, glow=0.1)
    glow_text(c, "= 220", 1480, 440, 100, "black", LIME, 1, glow=0.5)
    line(c, 1220, 500, 1740, 500, LIGHT, 1, 3)
    glow_text(c, "200 × 10%", 1480, 640, 84, "black", INK, 1, glow=0.1)
    glow_text(c, "= 20", 1480, 750, 100, "black", MAGENTA, 1, glow=0.5)
    chip(c, "MESMA TECLA", 1480, 860, GOLD, 1, anchor="center", size=40, filled=True)


def capa_rea(c):
    base(c)
    glow_text(c, "REA", 80, 520, 330, "black", CYAN, 0.55, align="left", glow=0.9)
    glow_text(c, "REA", 80, 520, 330, "black", INK, 1, align="left", glow=0.0)
    text(c, "Reverse Engineer Anything", 90, 640, 64, "black", VIOLET, align="left")
    text(c, "agentes de IA + engenharia reversa", 90, 830, 50, "monob", INK2, align="left")
    panel(c, 1140, 150, 680, 800, 1, VIOLET, label="MCP")
    node(c, 1480, 420, 150, None, None, CYAN, 1, 0, glyph="MCP", gsize=72)
    for k, s in enumerate(("Claude Code", "Codex", "Cursor")):
        chip(c, s, 1480, 680 + k * 85, VIOLET, 1, anchor="center", size=38)


if __name__ == "__main__":
    for nome, fn in (("capa_A_ia_abre_programa", capa_por_dentro), ("capa_B_calculadora", capa_porcentagem),
                     ("capa_C_rea", capa_rea)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
