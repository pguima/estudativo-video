"""Capas do vídeo Tecnologia 002 — Claude Dashboards (tema 'tech', futurista). Gera 3 variações em 1280x720."""
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
        tech._bracket(c, x, y, dx, dy, CYAN, 0.7)
    chip(c, "IA  ·  DADOS  ·  CLAUDE", 84, 110, CYAN, 1, size=34, filled=True)


def big(c, l1, l2, word, col):
    glow_text(c, l1, 80, 340, 128, "black", INK, 1, align="left", glow=0.15)
    glow_text(c, l2, 80, 480, 128, "black", INK, 1, align="left", glow=0.15)
    size = min(140, 140 * 900 / text_w(word, "black", 140))
    w = text_w(word, "black", size) + 70
    p = chamfer_path(70, 520, w, 175, 40)
    c.drawPath(p, blur_paint(col, 0.6, 26))
    c.drawPath(p, paint(col))
    text_mid(c, word, 70 + w / 2, 607, size, "black", "#03050B")


def capa_pergunte(c):
    base(c)
    big(c, "PERGUNTE E", "GANHE UM", "DASHBOARD", CYAN)
    text(c, "Claude Dashboards · novo · beta", 90, 830, 54, "monob", INK2, align="left")
    panel(c, 1140, 150, 680, 800, 1, CYAN, label="dashboard")
    V.live_dot(c, 1600, 210, 0.3, 1)
    V.kpi(c, 1180, 250, 600, 170, "CADASTROS / SEMANA", "4.812", "+38%", CYAN, 1)
    V.bars(c, 1200, 470, 560, 260, [0.4, 0.55, 0.48, 0.62, 0.95], CYAN, 1, 1.0, hi=LIME)
    V.sql(c, ["SELECT week, COUNT(*)", "FROM signups"], 1190, 820, 32, 9, 0, 1)


def capa_sql(c):
    base(c)
    big(c, "O CLAUDE", "ESCREVE O", "SQL POR VOCÊ", MAGENTA)
    text(c, "e mostra a consulta de cada gráfico", 90, 830, 50, "monob", INK2, align="left")
    panel(c, 1140, 150, 680, 800, 1, MAGENTA, label="consulta")
    V.bubble(c, 1180, 230, 600, 170, 1, VIOLET)
    text(c, "Quantos cadastros", 1220, 310, 42, "black", INK, 1, align="left")
    text(c, "esta semana?", 1220, 365, 42, "black", INK, 1, align="left")
    arrow(c, 1480, 420, 1480, 500, MAGENTA, 1, 5, 20)
    V.sql(c, ["SELECT week,", "  COUNT(*)", "FROM signups", "GROUP BY week"], 1200, 580, 44, 9, 0, 1, step=0.1)
    chip(c, "+38%", 1480, 880, LIME, 1, anchor="center", size=48, filled=True)


def capa_nome(c):
    base(c)
    glow_text(c, "Claude", 80, 390, 165, "black", INK, 1, align="left", glow=0.0)
    glow_text(c, "Dashboards", 80, 560, 165, "black", CYAN, 0.6, align="left", glow=0.9)
    glow_text(c, "Dashboards", 80, 560, 165, "black", CYAN, 1, align="left", glow=0.0)
    chip(c, "NOVO · BETA", 90, 680, GOLD, 1, size=48, filled=True)
    text(c, "painéis ao vivo em linguagem natural", 90, 830, 50, "monob", INK2, align="left")
    V.mini_dash(c, 1140, 150, 680, 800, 0.3, 1, VIOLET, "dashboard", grow=1.0)


if __name__ == "__main__":
    for nome, fn in (("capa_A_pergunte_dashboard", capa_pergunte), ("capa_B_sql_por_voce", capa_sql),
                     ("capa_C_claude_dashboards", capa_nome)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
