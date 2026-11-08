"""Capas do MAT-CNT-008 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]
CORES = {"A": "#E08A3C", "B": "#8E5BD9", "C": "#5B8DB8"}


def ficha(c, cx, cy, s, ch, a=1.0):
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.2, s * 0.2)
    c.drawRRect(r, M.paint(CORES[ch], a))
    E.centro(c, ch, cx, cy + s * 0.22, s * 0.6, "g", BR, a)


def a(c):  # o gancho: comissão de 3 entre 8 não é 336, é 56
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "comissão de 3 entre 8", 84, 330, 84, "i", BR)
    E.escreve(c, "336", 84, 560, 200, "g", BR)
    E.risco(c, 60, 490, 520, 480, 9, 0, AMARELO, 30)
    E.escreve(c, "são só", 84, 820, 130, "i", BR)
    E.bola(c, 640, 780, 170, "#FFFFFF")
    E.centro(c, "56", 640, 780 + 62, 180, "g", COR)
    for i, ordem in enumerate(("ABC", "ACB", "BCA", "CBA")):
        for j, ch in enumerate(ordem):
            ficha(c, 1260 + j * 140, 330 + i * 150, 120, ch, 1.0 if i == 0 else 0.45)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1170, 250, 450, 160), 30, 30)
    c.drawRRect(r, M.paint(AMARELO, 1, stroke=10))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Combinação", "simples", "a ordem não importa")


def d(c):  # o macete: arranjo dividido pelo fatorial dos escolhidos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a ordem não importa?", 84, 360, 120, "i", BR)
    E.formula(c, "f{8 × 7 × 6}{3!}", 84, 640, 200, "g", BR)
    E.escreve(c, "= 56", 1080, 690, 200, "g", AMARELO)
    E.escreve(c, "divida pelas ordens", 84, 960, 120, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sao_so_56", a), ("capa_B_combinacao", b), ("capa_C_divida_pelas_ordens", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
