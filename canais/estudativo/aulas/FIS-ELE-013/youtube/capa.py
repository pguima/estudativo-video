"""Capas do FIS-ELE-013 (1280x720). Uso: python capa.py"""
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


def zigue(c, A, B, cor, w=9, k=30):
    """resistor em zigue-zague de A a B (horizontal ou vertical)"""
    (x0, y0), (x1, y1) = A, B
    L = abs(x1 - x0) + abs(y1 - y0)
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    nx, ny = -uy, ux
    pts = [A, (x0 + ux * L * 0.25, y0 + uy * L * 0.25)]
    for j in range(1, 8):
        f = 0.25 + 0.5 * j / 8
        s = k if j % 2 else -k
        pts.append((x0 + ux * L * f + nx * s, y0 + uy * L * f + ny * s))
    pts += [(x0 + ux * L * 0.75, y0 + uy * L * 0.75), B]
    for P, Q in zip(pts, pts[1:]):
        M.line(c, *P, *Q, cor, 1.0, w)


def a(c):  # o gancho: o labirinto vira um resistor só
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "circuito labirinto?", 84, 330, 110, "i", BR)
    E.escreve(c, "reduza", 84, 530, 190, "g", BR)
    y0, y1 = 620, 960
    for P, Q in (((80, y0), (160, y0)), ((420, y0), (560, y0)), ((560, y0), (900, y0)), ((80, y1), (900, y1)), ((80, y0), (80, y1))):
        M.line(c, *P, *Q, BR, 1.0, 9)
    zigue(c, (160, y0), (420, y0), BR)
    zigue(c, (560, y0), (560, y1), BR)
    zigue(c, (900, y0), (900, y1), BR)
    F.seta(c, 1000, 790, 1200, 790, BR, 1.0, 16)
    E.bola(c, 1520, 790, 230, BR)
    E.centro(c, "6 Ω", 1520, 840, 150, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Associação", "mista", "do zero")


def d(c):  # o macete: uma letra em cada nó
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o macete das", 84, 330, 120, "i", BR)
    E.escreve(c, "letras nos nós", 84, 520, 160, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    y0, y1 = 720, 960
    M.line(c, 200, y0, 520, y0, BR, 1.0, 9); zigue(c, (520, y0), (900, y0), BR); M.line(c, 900, y0, 1200, y0, BR, 1.0, 9)
    M.line(c, 360, y0, 360, y1, claro, 1.0, 9); M.line(c, 1060, y0, 1060, y1, claro, 1.0, 9)
    M.line(c, 360, y1, 520, y1, claro, 1.0, 9); zigue(c, (520, y1), (900, y1), BR); M.line(c, 900, y1, 1060, y1, claro, 1.0, 9)
    for (x, y), s in (((360, y0), "A"), ((1060, y0), "B"), ((360, y1), "A"), ((1060, y1), "B")):
        E.bola(c, x, y, 52, COR)
        E.centro(c, s, x, y + 22, 64, "g", BR)
    E.escreve(c, "A–B e A–B:", 1300, 800, 90, "g", BR)
    E.escreve(c, "paralelo", 1300, 920, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_reduza_o_labirinto", a), ("capa_B_associacao_mista", b), ("capa_C_letras_nos_nos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
