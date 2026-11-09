"""Capas do FIS-CAL-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: mais fogo e a água não esquenta
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "mais fogo", 84, 400, 190, "g", BR)
    E.escreve(c, "e a água fica", 84, 580, 120, "i", BR)
    F.medida(c, 100, "°C", 84, 820, 220, AMARELO, cor_u=AMARELO)
    cx, yb, h = 1600, 960, 760
    M.rrect(c, cx - 40, yb - h, 80, h, 40, CLARO)
    c.drawCircle(cx, yb, 95, M.paint(CLARO))
    M.rrect(c, cx - 18, yb - h * 0.8, 36, h * 0.8, 18, AMARELO)
    c.drawCircle(cx, yb, 70, M.paint(AMARELO))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Calor", "latente", "do zero")


def d(c):  # o macete: rampa e patamar
    palco_capa(c)
    E.escreve(c, "a curva em", 84, 340, 130, "i", BR)
    E.escreve(c, "2 contas", 84, 540, 190, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    pts = [(120, 1000), (420, 820), (820, 820), (1120, 640), (1800, 640)]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        M.line(c, x0, y0, x1, y1, claro if y0 == y1 else BR, 1.0, 16)
    E.formula(c, "m · c · ΔT", 300, 1010, 80, "g", BR, 1.0, "left")
    E.formula(c, "m · L", 620, 790, 90, "g", claro, 1.0, "center")
    E.formula(c, "m · L", 1460, 610, 90, "g", claro, 1.0, "center")


CAPAS = (("capa_A_mais_fogo_100_graus", a), ("capa_B_calor_latente", b), ("capa_C_rampa_e_patamar", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
