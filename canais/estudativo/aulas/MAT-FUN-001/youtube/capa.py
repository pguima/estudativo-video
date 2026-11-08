"""Capas do MAT-FUN-001 (1280x720). Uso: python capa.py"""
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


def par(c, xv, yv, cx, y, size, cor_x, cor_y=BR):
    partes = (("(", BR), (xv, cor_x), (", ", BR), (yv, cor_y), (")", BR))
    w = sum(E.larg(s, "g", size) for s, _ in partes)
    x = cx - w / 2
    for s, cor in partes:
        E.escreve(c, s, x, y, size, "g", cor)
        x += E.larg(s, "g", size)


def a(c):  # o gancho: os mesmos números em lugares diferentes
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    par(c, "3", "−2", 470, 560, 200, AMARELO)
    E.centro(c, "≠", 960, 545, 180, "g", BR)
    par(c, "−2", "3", 1450, 560, 200, AMARELO)
    E.escreve(c, "a ordem muda o lugar", 84, 860, 130, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Plano", "cartesiano", "do zero")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o quadrante", 84, 400, 140, "i", BR)
    E.escreve(c, "pelos sinais", 76, 600, 170, "g", BR)
    cx, cy = 1450, 600
    M.line(c, cx - 360, cy, cx + 360, cy, claro, 1, 7)
    M.line(c, cx, cy - 330, cx, cy + 330, claro, 1, 7)
    for (dx, dy), (sx, sy) in (((1, -1), ("+", "+")), ((-1, -1), ("−", "+")), ((-1, 1), ("−", "−")), ((1, 1), ("+", "−"))):
        par(c, sx, sy, cx + dx * 185, cy + dy * 160 + 40, 96, claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_ordem_muda", a), ("capa_B_plano_cartesiano", b), ("capa_C_quadrante_pelos_sinais", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
