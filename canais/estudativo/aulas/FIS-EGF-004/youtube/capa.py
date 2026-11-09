"""Capas do FIS-EGF-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: por que a faca afiada corta?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "por que a faca", 84, 380, 120, "i", BR)
    E.escreve(c, "afiada", 84, 580, 200, "g", BR)
    E.escreve(c, "corta melhor?", 84, 760, 140, "g", AMARELO)
    E.bola(c, 1500, 820, 170, "#D8342C")
    p = skia.Path(); p.moveTo(1230, 760); p.lineTo(1700, 760); p.lineTo(1700, 600); p.lineTo(1290, 600); p.close()
    c.drawPath(p, M.paint("#D9DBE0"))
    M.rrect(c, 1700, 600, 200, 90, 20, "#1B1B20")
    M.line(c, 1230, 762, 1700, 762, AMARELO, 1.0, 6)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Pressão:", "força / área", "do zero")


def d(c):  # o macete: N/cm² × 10.000 = Pa
    palco_capa(c)
    E.escreve(c, "área em", 84, 330, 110, "i", BR)
    E.escreve(c, "cm²?", 84 + E.larg("área em ", "i", 110), 330, 100, "g", BR)
    E.escreve(c, "não erre o pascal", 84, 490, 120, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "N/cm^2 × 10.000 = Pa", 84, 760, 130, "g", AMARELO)
    E.formula(c, "600 ÷ 20 = 30  →  300.000 Pa", 84, 950, 90, "g", claro)


CAPAS = (("capa_A_faca_afiada", a), ("capa_B_pressao_forca_area", b), ("capa_C_nao_erre_o_pascal", d))

pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
