"""Capas do FIS-DIN-011 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def fsub(c, base, sb, x, y, size, cor):
    """letra com subscrito (F com R embaixo); devolve a largura"""
    E.escreve(c, base, x, y, size, "g", cor)
    w = E.larg(base, "g", size)
    E.escreve(c, sb, x + w + size * 0.02, y + size * 0.2, size * 0.6, "g", cor)
    return w + E.larg(sb, "g", size * 0.6) + size * 0.06


def carro_capa(c, cx, yb, w, cor):
    h = w * 0.62
    for dx in (-0.36, 0.36):
        M.rrect(c, cx + dx * w - w * 0.09, yb - w * 0.2, w * 0.18, w * 0.2, 10, "#1B1B20")
    M.rrect(c, cx - w / 2, yb - h * 0.75, w, h * 0.55, w * 0.06, cor)
    p = skia.Path()
    p.moveTo(cx - w * 0.36, yb - h * 0.74); p.lineTo(cx - w * 0.26, yb - h); p.lineTo(cx + w * 0.26, yb - h); p.lineTo(cx + w * 0.36, yb - h * 0.74); p.close()
    c.drawPath(p, M.paint(cor))


def a(c):  # o gancho: 72 no seco, 36 na chuva
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Seco: 72", 84, 400, 180, "g", BR)
    E.escreve(c, "Chuva: 36", 84, 600, 180, "g", AMARELO)
    E.escreve(c, "a mesma curva, em km/h", 84, 780, 90, "i", BR)
    E.escreve(c, "a velocidade máxima na curva", 84, 930, 84, "i", BR)
    carro_capa(c, 1530, 760, 520, BR)
    M.line(c, 1200, 760, 1860, 760, BR, 1.0, 12)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Carro", "na curva", "plana e inclinada")


def d(c):  # o macete: v = √(μgR)
    palco(c)
    E.escreve(c, "a velocidade máxima da curva", 84, 330, 100, "i", BR)
    E.formula(c, "v = r{μ·g·R}", 84, 620, 220, "g", BR)
    E.escreve(c, "a massa nem entra", 84, 840, 110, "i", E.mix(COR, BR, 0.5))


CAPAS = (("capa_A_seco_72_chuva_36", a), ("capa_B_carro_na_curva", b), ("capa_C_raiz_de_mi_g_r", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
