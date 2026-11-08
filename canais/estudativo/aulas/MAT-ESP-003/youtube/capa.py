"""Capas do MAT-ESP-003 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
ESCURO = "#120F3A"


def sol(c, cx, cy, r):
    for i in range(10):
        a = math.radians(i * 36 + 8)
        M.line(c, cx + math.cos(a) * r * 1.3, cy + math.sin(a) * r * 1.3, cx + math.cos(a) * r * 1.8, cy + math.sin(a) * r * 1.8, AMARELO, 1, 9)
    c.drawCircle(cx, cy, r, M.paint(AMARELO))


def lata(c, x, y, L, r):
    rx = r * 0.36
    corpo = skia.Path()
    corpo.moveTo(x, y - r); corpo.lineTo(x + L, y - r)
    corpo.arcTo(skia.Rect.MakeXYWH(x + L - rx, y - r, 2 * rx, 2 * r), 270, 180, False)
    corpo.lineTo(x, y + r)
    corpo.arcTo(skia.Rect.MakeXYWH(x - rx, y - r, 2 * rx, 2 * r), 90, 180, False)
    corpo.close()
    c.drawPath(corpo, M.paint(E.mix(COR, BR, 0.8)))
    c.drawOval(skia.Rect.MakeXYWH(x + L - rx, y - r, 2 * rx, 2 * r), M.paint(E.mix(COR, BR, 0.6)))
    pt = M.paint(ESCURO, 1, stroke=8)
    c.drawPath(corpo, pt)
    c.drawOval(skia.Rect.MakeXYWH(x + L - rx, y - r, 2 * rx, 2 * r), pt)


def a(c):  # o gancho: a sombra da lata deitada
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    sol(c, 420, 300, 70)
    for x in (260, 420, 580):
        M.line(c, x, 420, x, 520, AMARELO, 0.9, 7, dash=[18, 14])
    lata(c, 170, 660, 470, 120)
    c.drawRect(skia.Rect.MakeXYWH(170, 860, 470, 130), M.paint(ESCURO, 0.85))
    E.escreve(c, "a sombra", 900, 380, 120, "i", BR)
    E.escreve(c, "é um", 900, 520, 120, "i", BR)
    E.escreve(c, "retângulo", 890, 720, 200, "g", AMARELO)
    E.escreve(c, "e não um círculo", 900, 900, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Vistas", "e sombras", "de frente e de cima")


def d(c):  # o atalho: cada vista apaga uma direção
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 110, "i", BR)
    E.escreve(c, "cada vista", 76, 540, 180, "g", BR)
    E.escreve(c, "apaga", 76, 740, 180, "g", AMARELO)
    E.escreve(c, "uma direção", 84, 900, 120, "i", BR)
    O = (1320, 860)
    claro = E.mix(COR, BR, 0.55)
    M.arrow(c, *O, O[0] + 420, O[1], claro, 1, 12, 34)
    M.arrow(c, *O, O[0], O[1] - 420, claro, 1, 12, 34)
    M.arrow(c, *O, O[0] + 260, O[1] - 205, claro, 1, 12, 34)
    mx, my = O[0] + 150, O[1] - 118
    M.line(c, mx - 55, my + 55, mx + 55, my - 55, AMARELO, 1, 16)
    M.line(c, mx - 55, my - 55, mx + 55, my + 55, AMARELO, 1, 16)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sombra_da_lata", a), ("capa_B_vistas_e_sombras", b), ("capa_C_apaga_uma_direcao", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
