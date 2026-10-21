"""Capas do vídeo Tecnologia 005 — MCP explicado (tema 'tech', futurista). Gera 3 variações em 1280x720."""
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
        tech._bracket(c, x, y, dx, dy, LIME, 0.7)
    chip(c, "IA  ·  PROTOCOLOS  ·  AGENTES", 84, 110, LIME, 1, size=34, filled=True)


def big(c, l1, l2, word, col):
    glow_text(c, l1, 80, 340, 128, "black", INK, 1, align="left", glow=0.15)
    glow_text(c, l2, 80, 480, 128, "black", INK, 1, align="left", glow=0.15)
    size = min(140, 140 * 900 / text_w(word, "black", 140))
    w = text_w(word, "black", size) + 70
    p = chamfer_path(70, 520, w, 175, 40)
    c.drawPath(p, blur_paint(col, 0.6, 26))
    c.drawPath(p, paint(col))
    text_mid(c, word, 70 + w / 2, 607, size, "black", "#03050B")


def hub_panel(c, col=LIME):
    panel(c, 1140, 150, 680, 800, 1, col, label="MCP")
    V.usbc(c, 1480, 550, 280, 110, LIME, 1)
    text(c, "MCP", 1480, 470, 44, "black", LIME, 1)
    for k, s in enumerate(("Claude", "VS Code", "Cursor")):
        x = 1170 + k * 215
        V.box(c, x, 230, 195, 90, s, None, CYAN, 1, k=10)
        link(c, x + 97, 325, 1480, 495, CYAN, 1, 0.3 + 0.2 * k, pulses=1)
    for k, s in enumerate(("Arquivos", "Banco", "GitHub")):
        x = 1170 + k * 215
        V.box(c, x, 780, 195, 90, s, None, GOLD, 1, k=10)
        link(c, 1480, 605, x + 97, 775, GOLD, 1, 0.5 + 0.2 * k, pulses=1)


def capa_usbc(c):
    base(c)
    big(c, "O USB-C DA", "INTELIGÊNCIA", "ARTIFICIAL", LIME)
    text(c, "MCP explicado do zero", 90, 830, 56, "monob", INK2, align="left")
    hub_panel(c)


def capa_mcp_o_que(c):
    base(c)
    big(c, "AFINAL, O", "QUE É ESSE", "MCP?", CYAN)
    text(c, "host · cliente · servidor · tools", 90, 830, 50, "monob", INK2, align="left")
    panel(c, 1140, 150, 680, 800, 1, VIOLET, label="JSON-RPC")
    rows = [("→", "tools/list", CYAN), ("←", "weather_current", LIME), ("→", "tools/call", CYAN),
            ("←", "68°F, nublado", LIME)]
    for i, (a_, s, col) in enumerate(rows):
        y = 300 + i * 160
        text(c, a_, 1190, y, 64, "black", col, 1, align="left")
        text(c, s, 1270, y - 4, 40, "monob", INK, 1, align="left")


def capa_nome(c):
    base(c)
    glow_text(c, "MCP", 80, 470, 300, "black", LIME, 0.5, align="left", glow=0.9)
    glow_text(c, "MCP", 80, 470, 300, "black", INK, 1, align="left", glow=0.0)
    text(c, "Model Context Protocol", 90, 580, 62, "black", LIME, align="left")
    chip(c, "EXPLICADO", 90, 690, GOLD, 1, size=48, filled=True)
    text(c, "o padrão que conecta a IA a tudo", 90, 830, 48, "monob", INK2, align="left")
    hub_panel(c, VIOLET)


if __name__ == "__main__":
    for nome, fn in (("capa_A_usb_c_da_ia", capa_usbc), ("capa_B_o_que_e_mcp", capa_mcp_o_que),
                     ("capa_C_mcp", capa_nome)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
