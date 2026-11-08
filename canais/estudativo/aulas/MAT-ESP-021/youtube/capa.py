"""Capas do MAT-ESP-021 (1280x720). Uso: python capa.py"""
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
SEN = math.sin(math.radians(22))


def lata(c, cx, cy, r, n, lw=8, fundo=None):
    """corte da lata justa: retângulo com n círculos; o vazio em amarelo"""
    rect = skia.Rect.MakeXYWH(cx - r, cy - 2 * n * r, 2 * r, 2 * n * r)
    c.drawRect(rect, M.paint(AMARELO, 0.95))
    for i in range(n):
        c.drawCircle(cx, cy - r - 2 * r * i, r, M.paint(fundo or COR))
        c.drawCircle(cx, cy - r - 2 * r * i, r, M.paint(BR, 1, stroke=lw))
    c.drawRect(rect, M.paint(BR, 1, stroke=lw))


def a(c):  # o gancho: as quatro situações
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "você resolve", 84, 330, 120, "i", BR)
    E.escreve(c, "as 4?", 84, 560, 240, "g", AMARELO)
    E.escreve(c, "silo, aquário, bolas", 84, 760, 84, "i", BR)
    E.escreve(c, "e embalagem", 84, 860, 84, "i", BR)
    lata(c, 1500, 980, 120, 3)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "volumes", "4 situações")


def d(c):  # o atalho: bola em lata justa
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "bola em lata justa", 84, 340, 110, "i", BR)
    E.escreve(c, "ocupa", 84, 620, 150, "g", BR)
    E.formula(c, "f{2}{3}", 620, 700, 260, "g", AMARELO)
    lata(c, 1460, 900, 230, 1, 10, "#0B0820")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_voce_resolve_as_4", a), ("capa_B_praticando_volumes", b), ("capa_C_bola_na_lata", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
