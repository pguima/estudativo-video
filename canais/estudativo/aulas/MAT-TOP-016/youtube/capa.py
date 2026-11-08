"""Capas do MAT-TOP-016 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
INC = 0.3


def cone(c, cx, cy, R, r, h, cor, lw=10):
    yt = cy - h
    p = skia.Path()
    p.moveTo(cx - R, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - R, cy - R * INC, 2 * R, 2 * R * INC), 180, -180, False)
    p.lineTo(cx + r, yt)
    if r > 0:
        p.arcTo(skia.Rect.MakeXYWH(cx - r, yt - r * INC, 2 * r, 2 * r * INC), 0, -180, False)
    else:
        p.lineTo(cx, yt)
    p.close()
    c.drawPath(p, M.paint(cor, 0.35))
    c.drawPath(p, M.paint(cor, 1, stroke=lw))
    if r > 0:
        c.drawOval(skia.Rect.MakeXYWH(cx - r, yt - r * INC, 2 * r, 2 * r * INC), M.paint(cor, 1, stroke=lw))


def a(c):  # o gancho: 81, corte a 1/3, ponta 3
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "cone de 81", 84, 380, 130, "i", BR)
    E.escreve(c, "a ponta: 27?", 84, 580, 150, "g", BR)
    E.risco(c, 640, 600, 980, 460, 9, 0, AMARELO, 26)
    E.escreve(c, "só 3", 84, 800, 190, "g", AMARELO)
    cx, cy, R, H_ = 1480, 960, 300, 600
    cone(c, cx, cy, R, R / 3, H_ * 2 / 3, BR)
    cone(c, cx, cy - H_ * 2 / 3 - 120, R / 3, 0, H_ / 3, AMARELO)
    E.centro(c, "78", cx, cy - 150, 130, "g", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Troncos", "de cone", "e de pirâmide")


def d(c):  # o macete: a fórmula do tronco
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "só o tronco?", 84, 380, 150, "g", BR)
    E.formula(c, "V = f{h}{3} · (B + r{B · b} + b)", 84, 700, 130, "g", "#3CC7D3")
    E.escreve(c, "sem o cone inteiro", 84, 950, 110, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_ponta_e_so_3", a), ("capa_B_troncos", b), ("capa_C_formula_do_tronco", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
