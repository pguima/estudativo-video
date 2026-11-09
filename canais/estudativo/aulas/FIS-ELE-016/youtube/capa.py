"""Capas do FIS-ELE-016 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def zigue(c, A, B, cor, w=9, k=28):
    (x0, y0), (x1, y1) = A, B
    L = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    pts = [A, (x0 + ux * L * 0.25, y0 + uy * L * 0.25)]
    for j in range(1, 8):
        f, s = 0.25 + 0.5 * j / 8, (k if j % 2 else -k)
        pts.append((x0 + ux * L * f - uy * s, y0 + uy * L * f + ux * s))
    pts += [(x0 + ux * L * 0.75, y0 + uy * L * 0.75), B]
    for P, Q in zip(pts, pts[1:]):
        M.line(c, *P, *Q, cor, 1.0, w)


def a(c):  # o gancho: 5 questões de circuito
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "5", 84, 640, 520, "g", BR)
    E.escreve(c, "questões de", 470, 400, 110, "i", BR)
    E.escreve(c, "circuito", 470, 560, 170, "g", BR)
    y0, y1 = 720, 980
    M.line(c, 120, y0, 400, y0, BR, 1.0, 9); zigue(c, (400, y0), (700, y0), BR); M.line(c, 700, y0, 1500, y0, BR, 1.0, 9)
    M.line(c, 120, y1, 1500, y1, BR, 1.0, 9); M.line(c, 120, y0, 120, y1, BR, 1.0, 9)
    zigue(c, (1000, y0), (1000, y1), BR); zigue(c, (1500, y0), (1500, y1), BR)
    for x in (1000,):
        c.drawCircle(x, y0, 14, M.paint(BR)); c.drawCircle(x, y1, 14, M.paint(BR))
    E.bola(c, 1720, 850, 120, BR)
    E.centro(c, "?", 1720, 900, 150, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Praticando:", "circuitos", "5 questões")


def d(c):  # o macete: estime antes de calcular
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "antes da conta,", 84, 330, 120, "i", BR)
    E.escreve(c, "estime", 84, 540, 200, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "série: maior que o maior", 84, 760, 90, "g", BR)
    E.formula(c, "paralelo: menor que o menor", 84, 900, 90, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_5_questoes_de_circuito", a), ("capa_B_praticando_circuitos", b), ("capa_C_estime_antes", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
