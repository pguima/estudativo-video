"""Capas do vídeo Tecnologia 004 — Claude Code (tema 'tech', futurista). Gera 3 variações em 1280x720."""
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

T = 99.0  # tempo "final" para as peças animadas aparecerem completas


def base(c):
    tech.background(c, 3.0)
    m = 34
    for x, y, dx, dy in ((m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)):
        tech._bracket(c, x, y, dx, dy, CYAN, 0.7)
    chip(c, "IA  ·  PROGRAMAÇÃO  ·  CLAUDE", 84, 110, CYAN, 1, size=34, filled=True)


def big(c, l1, l2, word, col):
    glow_text(c, l1, 80, 340, 128, "black", INK, 1, align="left", glow=0.15)
    glow_text(c, l2, 80, 480, 128, "black", INK, 1, align="left", glow=0.15)
    size = min(140, 140 * 900 / text_w(word, "black", 140))
    w = text_w(word, "black", size) + 70
    p = chamfer_path(70, 520, w, 175, 40)
    c.drawPath(p, blur_paint(col, 0.6, 26))
    c.drawPath(p, paint(col))
    text_mid(c, word, 70 + w / 2, 607, size, "black", "#03050B")


def term(c, col=CYAN):
    terminal(c, 1140, 150, 680, 800, 1, "~/projeto", col)
    rows = [("$", "claude", CYAN, "monob"), ("", "", INK, "mono"), (">", "escreva os testes", INK, "mono"),
            ("", "  do login e corrija", INK, "mono"), ("", "", INK, "mono"), ("+", "lendo login.ts", INK2, "mono"),
            ("+", "14 testes criados", INK2, "mono"), ("$", "npm test", INK2, "mono"), ("", "  2 falharam", ROSE, "mono"),
            ("+", "corrigindo...", GOLD, "mono"), ("$", "npm test", INK2, "mono"), ("", "  14 passaram", LIME, "monob")]
    for i, (sym, s, cc, peso) in enumerate(rows):
        y = 270 + i * 54
        if sym:
            text(c, sym, 1180, y, 34, "monob", LIME if sym == "$" else CYAN, 1, align="left")
        text(c, s, 1220, y, 34, peso, cc, 1, align="left")


def capa_projeto(c):
    base(c)
    big(c, "A IA QUE", "PROGRAMA NO", "SEU PROJETO", CYAN)
    text(c, "Claude Code · do zero ao uso", 90, 830, 54, "monob", INK2, align="left")
    term(c)


def capa_canal(c):
    base(c)
    big(c, "ESTE CANAL É", "FEITO COM", "CLAUDE CODE", GOLD)
    text(c, "roteiro, animações e render", 90, 830, 54, "monob", INK2, align="left")
    panel(c, 1140, 150, 680, 800, 1, GOLD, label="visual.py")
    for i, s in enumerate(("def b_hook(c, t):", "  terminal(c, ...)", "  typed(c, 'claude')", "", "def b_loop(c, t):",
                           "  node(c, 'PLANEJAR')", "  link(c, ...)", "", "render.py --final", "→ video.mp4")):
        text(c, s, 1180, 270 + i * 62, 34, "mono", CYAN if s.startswith(("def", "render")) else LIME if s.startswith("→") else INK2,
             1, align="left")


def capa_nome(c):
    base(c)
    glow_text(c, "Claude", 80, 390, 170, "black", INK, 1, align="left", glow=0.0)
    glow_text(c, "Code", 80, 560, 170, "black", CYAN, 1, align="left", glow=0.7)
    w = text_w("Code", "black", 170)
    c.drawRect(skia.Rect.MakeXYWH(80 + w + 24, 445, 34, 120), paint(CYAN, 1))
    chip(c, "GUIA COMPLETO", 90, 680, GOLD, 1, size=48, filled=True)
    text(c, "instalar · usar · permissões", 90, 830, 50, "monob", INK2, align="left")
    term(c, VIOLET)


if __name__ == "__main__":
    for nome, fn in (("capa_A_ia_no_seu_projeto", capa_projeto), ("capa_B_este_canal", capa_canal),
                     ("capa_C_claude_code", capa_nome)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
