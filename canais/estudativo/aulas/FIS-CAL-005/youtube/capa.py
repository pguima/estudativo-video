"""Capas do FIS-CAL-005 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a média dá 50, a mistura fica em 44
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a média dá", 84, 360, 130, "i", BR)
    F.medida(c, 50, "°C", 84, 600, 220, BR, cor_u=BR)
    E.risco(c, 70, 640, 640, 420, 9, 0, AMARELO, 30)
    E.escreve(c, "mas fica em", 84, 790, 110, "i", BR)
    F.medida(c, 44, "°C", 84, 990, 200, AMARELO, cor_u=AMARELO)
    for i, (cor, x) in enumerate(((E.mix(COR, BR, 0.45), 1180), ("#5BA8E0", 1520))):
        M.rrect(c, x, 520, 260, 340, 20, cor)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, 420, 260, 440), 20, 20), M.paint(BR, 1.0, stroke=10))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Trocas", "de calor", "no calorímetro")


def d(c):  # o macete: média ponderada
    palco_capa(c)
    E.escreve(c, "de cabeça:", 84, 340, 130, "i", BR)
    E.escreve(c, "média ponderada", 84, 540, 160, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "T = f{200 · 80 + 300 · 20}{500} = 44", 84, 860, 130, "g", claro)


CAPAS = (("capa_A_a_media_engana", a), ("capa_B_trocas_de_calor", b), ("capa_C_media_ponderada", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
