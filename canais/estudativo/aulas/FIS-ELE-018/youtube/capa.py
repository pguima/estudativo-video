"""Capas do FIS-ELE-018 (1280x720). Uso: python capa.py"""
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
E.usar("Física")


def a(c):  # o gancho: o chuveiro pesa 4 vezes mais que a TV
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "meia hora de banho", 84, 330, 110, "i", BR)
    E.escreve(c, "4× a TV", 84, 540, 230, "g", BR)
    E.escreve(c, "ligada 5 horas", 84, 680, 100, "i", BR)
    M.rrect(c, 84, 790, 1300, 110, 20, BR)
    E.escreve(c, "chuveiro  2 kWh/dia", 120, 872, 70, "g", COR)
    M.rrect(c, 84, 930, 325, 90, 20, E.mix(COR, BR, 0.45))
    E.escreve(c, "TV  0,5", 110, 995, 60, "g", BR)
    E.bola(c, 1640, 640, 200, AMARELO)
    E.centro(c, "R$ 48", 1640, 670, 90, "g", "#14141C")
    E.centro(c, "por mês", 1640, 740, 50, "b", "#14141C")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Consumo", "em kWh", "e a conta de luz")


def d(c):  # o macete: kW × h = kWh
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a conta de luz", 84, 330, 120, "i", BR)
    E.escreve(c, "em 1 linha", 84, 520, 170, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "kW × h = kWh", 84, 780, 140, "g", claro)
    E.formula(c, "× tarifa = R$", 84, 950, 110, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_banho_4x_a_tv", a), ("capa_B_consumo_em_kwh", b), ("capa_C_conta_em_1_linha", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
