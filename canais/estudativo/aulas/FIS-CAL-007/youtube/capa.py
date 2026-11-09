"""Capas do FIS-CAL-007 (1280x720). Uso: python capa.py"""
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
CLARO = E.mix(COR, BR, 0.82)
E.usar("Física")


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: a mesma água ferve a 70 °C ou a 120 °C
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a mesma água", 84, 360, 120, "i", BR)
    E.escreve(c, "ferve a", 84, 500, 120, "i", BR)
    F.medida(c, 70, "°C", 84, 720, 200, BR, cor_u=BR)
    E.escreve(c, "ou", 640, 720, 110, "i", BR)
    F.medida(c, 120, "°C", 84, 960, 200, AMARELO, cor_u=AMARELO)
    p = skia.Path(); p.moveTo(1150, 980); p.lineTo(1420, 520); p.lineTo(1690, 980); p.close()
    c.drawPath(p, M.paint(CLARO))
    M.rrect(c, 1600, 800, 260, 170, 24, AMARELO)
    M.rrect(c, 1580, 770, 300, 40, 12, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Diagrama", "de fases", "do zero")


def d(c):  # o macete: ande pela linha da pressão
    palco_capa(c)
    E.escreve(c, "ande pela linha", 84, 340, 130, "i", BR)
    E.escreve(c, "da pressão", 84, 540, 190, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    import math
    x, y, w, h = 980, 560, 860, 460
    px = lambda u, v: (x + u * w, y + (1 - v) * h)
    sub = [px(0.02 + 0.28 * k / 40, 0.25 * (k / 40) ** 2) for k in range(41)]
    vap = [px(0.3 + 0.62 * k / 40, 0.25 + 0.65 * (k / 40) ** 1.6) for k in range(41)]
    fus = [px(0.3 - 0.06 * k / 40, 0.25 + 0.73 * k / 40) for k in range(41)]
    for pts in (sub, vap, fus):
        F.poli(c, pts, 1.0, BR, 1.0, 9)
    v = 0.45
    M.line(c, x - 40, px(0, v)[1], x + w + 20, px(0, v)[1], claro, 1.0, 8, dash=[30, 20])
    for u in (0.3 - 0.06 * (v - 0.25) / 0.73, 0.3 + 0.62 * ((v - 0.25) / 0.65) ** (1 / 1.6)):
        E.bola(c, *px(u, v), 26, COR)
    E.escreve(c, "cada curva = uma mudança", 84, 1000, 70, "g", claro)


CAPAS = (("capa_A_70_ou_120_graus", a), ("capa_B_diagrama_de_fases", b), ("capa_C_ande_pela_pressao", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
