"""Capas do FIS-OND-012 (1280x720). Uso: python capa.py"""
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
E.usar("Física")
ARCO_IRIS = ["#E53935", "#FB8C00", "#FDD835", "#43A047", "#1E88E5", "#3949AB", "#8E24AA"]


def wifi(c, cx, cy, s, cor):
    for k in range(3):
        E.arco(c, cx, cy, s * (0.4 + 0.33 * k), -135, 90, cor, max(5, s * 0.12), 1.0)
    c.drawCircle(cx, cy, s * 0.12, M.paint(cor))


def a(c):  # o gancho: o lambda do wi-fi
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "wi-fi:", 84, 400, 150, "g", BR)
    E.formula(c, "λ = ?", 84, 600, 190, "g", AMARELO)
    E.escreve(c, "5 questões de espectro", 84, 840, 96, "i", BR)
    wifi(c, 1480, 640, 330, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Praticando", "espectro", "5 questões")


def d(c):  # o macete: divida c pelo dado
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a conta de sempre", 84, 330, 120, "i", BR)
    E.formula(c, "λ = f{c}{f}", 84, 640, 220, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "c = 3 × 10^{8} m/s", 900, 560, 100, "g", AMARELO)
    E.escreve(c, "cuidado nos expoentes", 900, 700, 80, "b", claro)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(84, 0), skia.Point(1836, 0)], [M.hexc(cc) for cc in ARCO_IRIS]))
    c.drawRect(skia.Rect.MakeXYWH(84, 900, 1752, 40), p)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_lambda_do_wifi", a), ("capa_B_praticando_espectro", b), ("capa_C_a_conta_de_sempre", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
