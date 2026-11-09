"""Capas do FIS-ELE-015 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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
AZUL = "#1F6FEB"
E.usar("Física")


def medidor(c, cx, cy, r, s, fundo=BR, letra=None):
    c.drawCircle(cx, cy, r, M.paint(fundo))
    E._meio(c, s, cx, cy, r * 1.05, "g", letra or COR, 1.0)


def zigue(c, A, B, cor, w=9, k=26):
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


def a(c):  # o gancho: ligou errado, queimou
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "ligou errado,", 84, 330, 120, "i", BR)
    E.escreve(c, "queimou", 84, 530, 200, "g", BR)
    medidor(c, 1300, 560, 210, "A")
    medidor(c, 1700, 760, 150, "V")
    for k in range(3):
        ang = -0.7 + 0.7 * k
        M.line(c, 1300 + 250 * math.sin(ang), 560 - 250 * math.cos(ang),
               1300 + 330 * math.sin(ang), 560 - 330 * math.cos(ang), AMARELO, 1.0, 16)
    E.escreve(c, "amperímetro e voltímetro", 84, 900, 80, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Medidores", "e a ponte", "de Wheatstone")


def d(c):  # o macete: produto cruzado na ponte
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "ponte em equilíbrio:", 84, 330, 110, "i", BR)
    E.escreve(c, "produto cruzado", 84, 510, 140, "g", BR)
    cx, cy, rx, ry = 1450, 760, 260, 230
    T, L, B, R = (cx, cy - ry), (cx - rx, cy), (cx, cy + ry), (cx + rx, cy)
    claro = E.mix(COR, BR, 0.35)
    zigue(c, T, L, claro); zigue(c, L, B, "#6FA8FF"); zigue(c, T, R, "#6FA8FF"); zigue(c, R, B, claro)
    M.line(c, L[0], cy, R[0], cy, BR, 1.0, 6)
    medidor(c, cx, cy, 60, "G", "#14141C", BR)
    E.formula(c, "R₁ · R₄ = R₂ · R₃", 84, 800, 110, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_ligou_errado_queimou", a), ("capa_B_medidores_e_wheatstone", b), ("capa_C_produto_cruzado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
