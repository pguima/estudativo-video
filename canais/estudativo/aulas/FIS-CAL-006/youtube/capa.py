"""Capas do FIS-CAL-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: água líquida a −40 °C?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "água líquida a", 84, 360, 120, "i", BR)
    F.medida(c, "−40", "°C?", 84, 610, 250, AMARELO, cor_u=AMARELO)
    E.escreve(c, "a conta do gelo", 84, 820, 110, "i", BR)
    E.escreve(c, "que engana", 84, 960, 110, "g", BR)
    x, yb, w, h = 1500, 950, 420, 560
    M.rrect(c, x - w / 2 + 10, yb - h * 0.7, w - 20, h * 0.7 - 6, 16, "#A9D8F5")
    for dx, g in ((-0.2, 8), (0.15, -10)):
        c.save(); c.translate(x + dx * w, yb - h * 0.7 + 20); c.rotate(g)
        M.rrect(c, -60, -60, 120, 120, 14, BR)
        c.restore()
    p = skia.Path(); p.moveTo(x - w / 2, yb - h); p.lineTo(x - w / 2 + 14, yb); p.lineTo(x + w / 2 - 14, yb); p.lineTo(x + w / 2, yb - h)
    c.drawPath(p, M.paint(BR, 1.0, stroke=12))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Trocas", "com gelo", "derrete ou não?")


def d(c):  # o macete do 80
    palco_capa(c)
    E.escreve(c, "o macete do", 84, 340, 130, "i", BR)
    E.escreve(c, "80", 84, 600, 280, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "água a 80 °C derrete", 84, 830, 100, "i", claro)
    E.escreve(c, "a mesma massa de gelo", 84, 960, 100, "g", BR)


CAPAS = (("capa_A_menos_40_graus", a), ("capa_B_trocas_com_gelo", b), ("capa_C_macete_do_80", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
