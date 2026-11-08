"""Capas do MAT-FAV-007 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def curva(c, f, cx, cy, kx, ky, a, b, cor, lw=14):
    pts = [(cx + kx * (a + (b - a) * i / 120), cy - ky * f(a + (b - a) * i / 120)) for i in range(121)]
    p = skia.Path(); p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    c.drawPath(p, M.paint(cor, 1, stroke=lw, cap_round=True))


def eixos(c, cx, cy, w, h, cor=BR):
    M.arrow(c, cx - w / 2, cy, cx + w / 2, cy, cor, 0.6, 5, 20)
    M.arrow(c, cx, cy + h / 2, cx, cy - h / 2, cor, 0.6, 5, 20)


def a(c):  # o gancho: igual ou oposto
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "(−2)^2 = 2^2", 84, 400, 150, "g", BR)
    E.formula(c, "(−2)^3 = −2^3", 84, 620, 150, "g", AMARELO)
    E.escreve(c, "par ou ímpar?", 84, 840, 120, "i", BR)
    eixos(c, 1500, 560, 640, 760)
    curva(c, lambda x: x ** 3, 1500, 560, 120, 40, -2.3, 2.3, AMARELO)
    curva(c, lambda x: x * x, 1500, 560, 120, 40, -2.4, 2.4, BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Função par", "e ímpar", "pelo gráfico")


def d(c):  # o atalho: olhe os expoentes
    palco(c)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "olhe os", 84, 360, 120, "i", BR)
    E.escreve(c, "expoentes", 84, 550, 170, "g", BR)
    E.formula(c, "x^4 + x^2 + 5 → par", 84, 740, 90, "g", BR)
    E.formula(c, "x^3 + 2x → ímpar", 84, 880, 90, "g", AMARELO)
    eixos(c, 1550, 560, 560, 760)
    curva(c, lambda x: x ** 3, 1550, 560, 110, 40, -2.3, 2.3, AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_igual_ou_oposto", a), ("capa_B_funcao_par_e_impar", b), ("capa_C_olhe_os_expoentes", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
