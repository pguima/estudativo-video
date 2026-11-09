"""Capas do FIS-OND-011 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")
ARCO_IRIS = ["#E53935", "#FB8C00", "#FDD835", "#43A047", "#1E88E5", "#3949AB", "#8E24AA"]


def avental(c, cx, cy, s):
    p = skia.Path()
    p.moveTo(cx - s * 0.4, cy - s); p.lineTo(cx + s * 0.4, cy - s); p.lineTo(cx + s * 0.75, cy + s); p.lineTo(cx - s * 0.75, cy + s); p.close()
    c.drawPath(p, M.paint("#3A3F4B"))
    E._meio(c, "Pb", cx, cy + s * 0.1, s * 0.4, "g", BR, 1.0)


def celular(c, cx, cy, s):
    M.rrect(c, cx - s * 0.55, cy - s, s * 1.1, s * 2, s * 0.16, "#1B1B1B", 1.0)
    M.rrect(c, cx - s * 0.46, cy - s * 0.85, s * 0.92, s * 1.62, s * 0.08, E.mix(COR, BR, 0.6), 1.0)


def a(c):  # o gancho: avental de chumbo no raio X, nada no celular
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "raio X: chumbo.", 84, 420, 150, "g", BR)
    E.escreve(c, "celular: nada?", 84, 600, 150, "g", AMARELO)
    E.escreve(c, "o risco de cada onda", 84, 840, 100, "i", BR)
    avental(c, 1480, 420, 170)
    celular(c, 1480, 820, 110)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Usos do", "espectro", "e seus riscos")


def d(c):  # o macete: a luz visível no meio
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a luz no meio decide", 84, 330, 120, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    y, x0, xv0, xv1, x1 = 470, 84, 860, 1060, 1836
    c.drawRect(skia.Rect.MakeXYWH(x0, y, xv0 - x0, 120), M.paint(E.mix(COR, "#07070F", 0.5)))
    c.drawRect(skia.Rect.MakeXYWH(xv1, y, x1 - xv1, 120), M.paint(COR))
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(xv0, 0), skia.Point(xv1, 0)], [M.hexc(cc) for cc in ARCO_IRIS]))
    c.drawRect(skia.Rect.MakeXYWH(xv0, y, xv1 - xv0, 120), p)
    E.escreve(c, "aquecem", 84, 780, 110, "g", BR)
    E.escreve(c, "e comunicam", 84, 900, 80, "b", claro)
    E.formula(c, "ionizam", 1836, 780, 110, "g", AMARELO, 1.0, "right")
    E.formula(c, "e atravessam", 1836, 900, 80, "b", claro, 1.0, "right")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_chumbo_ou_nada", a), ("capa_B_usos_do_espectro", b), ("capa_C_a_luz_no_meio_decide", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
