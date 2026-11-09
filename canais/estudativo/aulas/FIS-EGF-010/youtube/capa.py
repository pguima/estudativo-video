"""Capas do FIS-EGF-010 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o dedo na mangueira
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "por que a água", 84, 380, 110, "i", BR)
    E.escreve(c, "acelera no", 84, 570, 170, "g", BR)
    E.escreve(c, "cano fino?", 84, 760, 170, "g", AMARELO)
    y = 760
    p = skia.Path(); p.moveTo(1150, y - 110); p.lineTo(1500, y - 110); p.lineTo(1560, y - 45); p.lineTo(1880, y - 45)
    p.lineTo(1880, y + 45); p.lineTo(1560, y + 45); p.lineTo(1500, y + 110); p.lineTo(1150, y + 110); p.close()
    c.drawPath(p, M.paint("#5AB4E6", 0.85))
    c.drawPath(p, M.paint(BR, 1.0, stroke=8))
    for x in (1210, 1330):
        F.seta(c, x, y, x + 60, y, "#1B1B20", 1.0, 10)
    for x in (1590, 1740):
        F.seta(c, x, y, x + 120, y, AMARELO, 1.0, 12)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Vazão", "Q = A · v", "e continuidade")


def d(c):  # o macete: diâmetro ÷ 2, velocidade × 4
    palco_capa(c)
    E.escreve(c, "deu o diâmetro?", 84, 330, 110, "i", BR)
    E.escreve(c, "eleve ao quadrado", 84, 490, 120, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "D ÷ 2  →  v × 4", 84, 760, 150, "g", AMARELO)
    E.formula(c, "A₁ · v₁ = A₂ · v₂", 84, 950, 100, "g", claro)


CAPAS = (("capa_A_acelera_no_cano_fino", a), ("capa_B_vazao_e_continuidade", b), ("capa_C_diametro_ao_quadrado", d))

pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
