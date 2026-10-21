"""Capas do vídeo Tecnologia 006 — Claude Docs, Slides e Design (tema 'tech'). Gera 3 variações em 1280x720."""
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


def base(c, col=VIOLET):
    tech.background(c, 3.0)
    m = 34
    for x, y, dx, dy in ((m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)):
        tech._bracket(c, x, y, dx, dy, col, 0.7)
    chip(c, "IA  ·  PRODUTIVIDADE  ·  CLAUDE", 84, 110, col, 1, size=34, filled=True)


def big(c, l1, l2, word, col):
    glow_text(c, l1, 80, 340, 128, "black", INK, 1, align="left", glow=0.15)
    glow_text(c, l2, 80, 480, 128, "black", INK, 1, align="left", glow=0.15)
    size = min(140, 140 * 900 / text_w(word, "black", 140))
    w = text_w(word, "black", size) + 70
    p = chamfer_path(70, 520, w, 175, 40)
    c.drawPath(p, blur_paint(col, 0.6, 26))
    c.drawPath(p, paint(col))
    text_mid(c, word, 70 + w / 2, 607, size, "black", "#03050B")


def trio(c):
    """os três artifacts empilhados à direita"""
    for k, (lab, col) in enumerate((("Docs", V.DOC), ("Slides", V.SLD), ("Design", V.DSG))):
        y = 150 + k * 275
        panel(c, 1140, y, 680, 245, 1, col, label=lab)
        if k == 0:
            V.doc_mock(c, 1180, y + 30, 600, 190, 1, lines=3, title="Relatório semanal")
        elif k == 1:
            V.slide_mock(c, 1180, y + 25, 340, 1)
            text(c, "Vendas", 1560, y + 110, 44, "black", INK, 1, align="left")
            text(c, "+18%", 1560, y + 170, 52, "black", V.SLD, 1, align="left")
        else:
            V.design_mock(c, 1180, y + 30, 600, 190, 1, 0.0)


def capa_um_chat(c):
    base(c)
    big(c, "DOC, SLIDES", "E DESIGN EM", "UM CHAT SÓ", VIOLET)
    text(c, "Claude Docs · Slides · Design", 90, 830, 52, "monob", INK2, align="left")
    trio(c)


def capa_gratis(c):
    base(c, LIME)
    big(c, "AGORA EM", "TODOS OS", "PLANOS", LIME)
    text(c, "inclusive no gratuito", 90, 830, 56, "monob", INK2, align="left")
    trio(c)


def capa_nomes(c):
    base(c)
    text(c, "Claude", 90, 250, 60, "black", INK2, 1, align="left")
    for k, (s, col) in enumerate((("Docs", V.DOC), ("Slides", V.SLD), ("Design", V.DSG))):
        glow_text(c, s, 80, 400 + k * 150, 150, "black", col, 1, align="left", glow=0.6)
    text(c, "guia completo", 90, 880, 50, "monob", INK2, align="left")
    trio(c)


if __name__ == "__main__":
    for nome, fn in (("capa_A_tudo_num_chat", capa_um_chat), ("capa_B_todos_os_planos", capa_gratis),
                     ("capa_C_docs_slides_design", capa_nomes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
