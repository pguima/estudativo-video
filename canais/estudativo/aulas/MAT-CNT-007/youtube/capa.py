"""Capas do MAT-CNT-007 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]
MEDALHA = {1: "#E2B33C", 2: "#C9CED6", 3: "#C27A3E"}


def podio(c, cx, base, w, h):
    for lugar, (col, k) in {2: (-1, 0.62), 1: (0, 1.0), 3: (1, 0.42)}.items():
        x, hh = cx + col * w, h * k
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w / 2 + 6, base - hh, w - 12, hh), 16, 16), M.paint(BR))
        rm = min(w * 0.22, hh * 0.3)
        c.drawCircle(x, base - hh + rm + 22, rm, M.paint(MEDALHA[lugar]))
        E.centro(c, str(lugar), x, base - hh + rm + 22 + rm * 0.42, rm * 1.15, "g", BR)


def a(c):  # o gancho: não é 8!, são 336 pódios
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "8 corredores, 3 medalhas", 84, 330, 84, "i", BR)
    E.escreve(c, "8! = 40.320", 84, 560, 170, "g", BR)
    E.risco(c, 60, 500, 1080, 490, 9, 0, AMARELO, 30)
    E.escreve(c, "são só", 84, 820, 130, "i", BR)
    E.bola(c, 640, 780, 170, "#FFFFFF")
    E.centro(c, "336", 640, 780 + 55, 150, "g", COR)
    podio(c, 1520, 1000, 210, 420)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Arranjo", "simples", "a ordem importa")


def d(c):  # o macete: desça do total, um número por lugar
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 lugares entre 8?", 84, 360, 120, "i", BR)
    x = 84
    for i, v in enumerate(("8", "7", "6")):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, 450, 250, 250), 30, 30)
        c.drawRRect(r, M.paint(BR, 0.12)); c.drawRRect(r, M.paint(BR, 1, stroke=8))
        E.centro(c, v, x + 125, 450 + 125 + 60, 170, "g", BR)
        if i < 2:
            E.centro(c, "×", x + 250 + 60, 450 + 125 + 35, 110, "g", BR)
        x += 370
    E.escreve(c, "= 336", 1200, 640, 170, "g", AMARELO)
    E.escreve(c, "um número por lugar", 84, 920, 130, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_8_fatorial", a), ("capa_B_arranjo", b), ("capa_C_desca_do_total", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
