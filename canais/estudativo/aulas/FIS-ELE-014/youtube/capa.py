"""Capas do FIS-ELE-014 (1280x720). Uso: python capa.py"""
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
AZUL = "#0E9AA7"
E.usar("Física")


def passaro(c, x, y, s):
    for dx in (-0.15, 0.15):
        M.line(c, x + dx * s, y, x + dx * s, y - s * 0.3, BR, 1.0, 6)
    c.drawOval(skia.Rect.MakeXYWH(x - s * 0.5, y - s * 0.85, s, s * 0.6), M.paint(AZUL))
    c.drawCircle(x + s * 0.42, y - s * 0.85, s * 0.22, M.paint(AZUL))
    c.drawCircle(x + s * 0.48, y - s * 0.9, s * 0.05, M.paint(BR))
    bico = skia.Path(); bico.moveTo(x + s * 0.62, y - s * 0.9); bico.lineTo(x + s * 0.8, y - s * 0.84); bico.lineTo(x + s * 0.62, y - s * 0.78); bico.close()
    c.drawPath(bico, M.paint(AMARELO))


def zigue(c, A, B, cor, w=9, k=30):
    (x0, y0), (x1, y1) = A, B
    L = abs(x1 - x0) + abs(y1 - y0)
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    pts = [A, (x0 + ux * L * 0.25, y0 + uy * L * 0.25)]
    for j in range(1, 8):
        f, s = 0.25 + 0.5 * j / 8, (k if j % 2 else -k)
        pts.append((x0 + ux * L * f - uy * s, y0 + uy * L * f + ux * s))
    pts += [(x0 + ux * L * 0.75, y0 + uy * L * 0.75), B]
    for P, Q in zip(pts, pts[1:]):
        M.line(c, *P, *Q, cor, 1.0, w)


def a(c):  # o gancho: por que o passarinho não leva choque?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "por que ele", 84, 330, 120, "i", BR)
    E.escreve(c, "não leva", 84, 510, 170, "g", BR)
    E.escreve(c, "choque?", 84, 680, 170, "g", BR)
    M.line(c, 1000, 640, 1900, 640, BR, 1.0, 10)
    passaro(c, 1450, 640, 300)
    E.escreve(c, "as duas patas no mesmo fio", 84, 960, 76, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Curto-circuito", "e choque", "do zero")


def d(c):  # o macete: fio sem resistor, o que ele liga sai do circuito
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "achou o curto?", 84, 330, 120, "i", BR)
    E.escreve(c, "apague o resistor", 84, 510, 150, "g", BR)
    y = 760
    M.line(c, 200, y, 600, y, BR, 1.0, 9); zigue(c, (600, y), (1100, y), E.mix(BR, "#000000", 0.5)); M.line(c, 1100, y, 1500, y, BR, 1.0, 9)
    M.line(c, 600, y, 600, y + 170, "#FF4D4D", 1.0, 12); M.line(c, 600, y + 170, 1100, y + 170, "#FF4D4D", 1.0, 12); M.line(c, 1100, y + 170, 1100, y, "#FF4D4D", 1.0, 12)
    M.line(c, 650, y + 80, 1050, y - 80, AMARELO, 1.0, 14)
    for x in (600, 1100):
        E.bola(c, x, y - 90, 50, COR)
        E.centro(c, "A", x, y - 68, 60, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_passarinho_sem_choque", a), ("capa_B_curto_e_choque", b), ("capa_C_apague_o_resistor", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
