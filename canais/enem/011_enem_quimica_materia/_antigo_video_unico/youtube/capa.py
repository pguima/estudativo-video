"""Capas do vídeo 011 — ENEM Química: Matéria, substâncias e misturas (tema claro). Gera 3 variações em 1280x720."""
import math, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

WATER = "#7DD3FC"
SKY = "#0EA5E9"


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "QUÍMICA ENEM · MATÉRIA", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_curva(c):
    background(c)
    selo(c)
    painel(c)
    x, y, w, h = 1210, 260, 520, 520
    arrow(c, x, y + h, x + w + 20, y + h, INK, 1, 6, 22)
    arrow(c, x, y + h, x, y - 30, INK, 1, 6, 22)
    text(c, "T", x - 40, y + 10, 50, "black", INK, align="right")
    pts = [(0, 0.05), (0.2, 0.36), (0.42, 0.36), (0.6, 0.72), (0.84, 0.72), (1.0, 0.97)]
    P = [(x + u * w, y + h - v * h) for u, v in pts]
    p = skia.Path(); p.moveTo(*P[0])
    for q in P[1:]:
        p.lineTo(*q)
    pp = paint(GREEN, 1, stroke=14, cap_round=True); pp.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pp)
    for i in (1, 3):
        line(c, P[i][0], P[i][1], P[i + 1][0], P[i + 1][1], AMBER, 1, 20)
    text(c, "2 patamares", 1470, 880, 52, "black", AMBER)
    text(c, "O GRÁFICO", 80, 340, 124, "black", INK, align="left")
    text(c, "QUE DIZ SE É", 80, 470, 110, "black", INK, align="left")
    boxed(c, "PURO", 70, 520, 150, GREEN)
    text(c, "curva de aquecimento no ENEM", 90, 840, 54, "extrabold", INK2, align="left")


def capa_gelo(c):
    background(c)
    selo(c)
    painel(c)
    x, y, w, h = 1240, 280, 460, 560
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), True)
    c.drawRect(skia.Rect.MakeXYWH(x, y + h * 0.28, w, h * 0.72), paint(WATER, 0.8))
    for k in range(3):
        rrect(c, x + 40 + k * 140, y + h * 0.28 - 40, 110, 100, 16, "#F8FAFC")
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 40 + k * 140, y + h * 0.28 - 40, 110, 100), 16, 16),
                    paint("#94A3B8", 1, stroke=4))
    c.restore()
    p = skia.Path()
    p.moveTo(x - 16, y); p.lineTo(x, y + 12); p.lineTo(x, y + h - 30); p.quadTo(x, y + h, x + 30, y + h)
    p.lineTo(x + w - 30, y + h); p.quadTo(x + w, y + h, x + w, y + h - 30); p.lineTo(x + w, y + 12); p.lineTo(x + w + 16, y)
    c.drawPath(p, paint(INK2, 1, stroke=9))
    text(c, "? fases", 1470, 210, 70, "black", RED)
    text(c, "ÁGUA + 3 GELOS:", 80, 340, 100, "black", INK, align="left")
    text(c, "QUANTAS", 80, 470, 124, "black", INK, align="left")
    boxed(c, "FASES?", 70, 520, 150, RED)
    text(c, "fases e componentes sem erro", 90, 840, 54, "extrabold", INK2, align="left")


def capa_carbono(c):
    background(c)
    selo(c)
    painel(c)
    text(c, "DIAMANTE", 1470, 220, 52, "black", SKY)
    nodes = [(1250 + i * 90 + (j % 2) * 45, 280 + j * 60) for i in range(5) for j in range(4)]
    for (x1, y1) in nodes:
        for (x2, y2) in nodes:
            if 0 < math.hypot(x2 - x1, y2 - y1) < 80:
                line(c, x1, y1, x2, y2, INK2, 0.8, 5)
    for q in nodes:
        c.drawCircle(*q, 13, paint(INK))
    line(c, 1180, 540, 1760, 540, LINE, 1, 4)
    text(c, "GRAFITE", 1470, 610, 52, "black", INK2)
    for k in range(3):
        y0 = 670 + k * 85
        for q in range(7):
            cx = 1240 + q * 66 + (k % 2) * 30
            pts = [(cx + 30 * math.cos(math.radians(60 * j)), y0 + 12 * math.sin(math.radians(60 * j))) for j in range(6)]
            p = skia.Path(); p.moveTo(*pts[0])
            for pt in pts[1:]:
                p.lineTo(*pt)
            p.close()
            c.drawPath(p, paint(INK2, 1, stroke=4))
    text(c, "DIAMANTE E", 80, 340, 116, "black", INK, align="left")
    text(c, "GRAFITE SÃO", 80, 470, 116, "black", INK, align="left")
    boxed(c, "SÓ CARBONO", 70, 520, 130, PURPLE)
    text(c, "alotropia no ENEM", 90, 840, 56, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_grafico_puro", capa_curva), ("capa_B_gelo_fases", capa_gelo), ("capa_C_diamante_grafite", capa_carbono)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
