"""Capas do FIS-MAG-007 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def transformador(c, cx, cy, w, h, n1, n2):
    e = 80
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 20, "#D9DDE2")
    M.rrect(c, cx - w / 2 + e, cy - h / 2 + e, w - 2 * e, h - 2 * e, 10, COR)
    for lado, n in ((-1, n1), (1, n2)):
        xl = cx + lado * (w / 2 - e / 2)
        for k in range(n):
            y = cy - h * 0.31 + h * 0.62 * (k + 0.5) / n
            M.line(c, xl - e / 2 - 16, y, xl + e / 2 + 16, y - 12, "#1B1B22", 1, 9)


def a(c):  # o gancho: por que a linha usa tensão altíssima
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "por que", 84, 380, 140, "i", BR)
    E.escreve(c, "220.000 V", 84, 600, 200, "g", BR)
    E.escreve(c, "na linha?", 84, 800, 170, "g", AMARELO)
    transformador(c, 1530, 540, 520, 560, 3, 9)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Transfor-", "madores", "e transmissão")


def d(c):  # o macete: tensão × 10, perda ÷ 100
    palco_capa(c)
    E.escreve(c, "tensão × 10", 84, 420, 170, "g", BR)
    E.escreve(c, "perda ÷ 100", 84, 640, 170, "g", E.mix(COR, BR, 0.5))
    E.escreve(c, "a perda vai com i ao quadrado", 84, 860, 100, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_por_que_tensao_alta", a), ("capa_B_transformadores_e_transmissao", b), ("capa_C_tensao_x10_perda_100", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
