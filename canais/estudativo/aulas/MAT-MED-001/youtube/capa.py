"""Capas do MAT-MED-001 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"


def escadinha(c, x, y, sw, sh, base, un, meio, cor_meio, bola_em=None, tinta=BR, alfa=0.14):
    """a escada da trilha, em miniatura, para a capa"""
    for i, u in enumerate(un):
        top = y + i * sh
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + i * sw + 4, top, sw - 8, base - top), 12, 12)
        c.drawRRect(r, M.paint(BR, 1.0 if i == meio else alfa))
        c.drawRRect(r, M.paint(tinta, 0.9, stroke=4))
        E.centro(c, u, x + (i + 0.5) * sw, top + 64, 50, "g", cor_meio if i == meio else BR)
    if bola_em is not None:
        E.bola(c, x + (bola_em + 0.5) * sw, y + bola_em * sh - 40, 34, AMARELO)


def a(c):  # o gancho: 2,5 km não são 250 m
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "2,5 km =", 84, 440, 190, "g", BR)
    E.escreve(c, "250 m", 1010, 440, 190, "g", BR)
    E.risco(c, 990, 480, 1560, 300, 9, 0, AMARELO, 30)
    E.escreve(c, "2.500 m", 1010, 680, 190, "g", AMARELO)
    E.escreve(c, "não encolha a corrida", 84, 960, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Converter", "medidas", "sem decorar")


def d(c):  # o atalho: a escada do metro
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a escada", 84, 330, 130, "i", BR)
    E.escreve(c, "do metro", 84, 520, 190, "g", BR)
    E.escreve(c, "1 degrau = 1 casa", 84, 700, 92, "g", AMARELO)
    escadinha(c, 980, 300, 130, 80, 1010, ("km", "hm", "dam", "m", "dm", "cm", "mm"), 3, COR, bola_em=0)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_encolha", a), ("capa_B_converter_medidas", b), ("capa_C_escada_do_metro", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
