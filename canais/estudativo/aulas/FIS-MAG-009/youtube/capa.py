"""Capas do FIS-MAG-009 (1280x720). Uso: python capa.py"""
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


def turbina(c, cx, cy, r, cor):
    for k in range(8):
        g = math.radians(45 * k + 10)
        x1, y1 = cx + r * math.cos(g), cy + r * math.sin(g)
        M.line(c, cx, cy, x1, y1, cor, 1, 16)
        M.line(c, x1, y1, x1 + r * 0.3 * math.cos(g + 1.3), y1 + r * 0.3 * math.sin(g + 1.3), cor, 1, 16)
    c.drawCircle(cx, cy, r * 0.2, M.paint(AMARELO))


def a(c):  # o gancho: toda usina termina igual
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "água, vapor", 84, 380, 130, "i", BR)
    E.escreve(c, "ou átomo:", 84, 520, 130, "i", BR)
    E.escreve(c, "tudo gira", 84, 720, 190, "g", AMARELO)
    E.escreve(c, "uma turbina", 84, 880, 120, "g", BR)
    turbina(c, 1480, 540, 300, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Como a usina", "gera energia", "do zero")


def d(c):  # o macete: P = 10.000 · Z · h
    palco_capa(c)
    E.escreve(c, "potência da queda d'água", 84, 330, 100, "i", BR)
    E.formula(c, "P = 10.000 · Z · h", 84, 600, 190, "g", BR)
    E.escreve(c, "em watt, sem conta longa", 84, 840, 100, "i", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_tudo_gira_uma_turbina", a), ("capa_B_como_a_usina_gera_energia", b), ("capa_C_potencia_da_queda", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
