"""Capas do FIS-CIN-018 (1280x720). Uso: python capa.py"""
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


def helice(c, x, y, r, cor, giro=20):
    for k in range(3):
        c.save(); c.translate(x, y); c.rotate(giro + 120 * k)
        c.drawOval(skia.Rect.MakeXYWH(r * 0.12, -r * 0.2, r * 0.9, r * 0.4), M.paint(cor))
        c.restore()
    c.drawCircle(x, y, r * 0.16, M.paint("#2A1A10"))


def a(c):  # o erro: multiplicar por 60
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "1.200 rpm", 84, 380, 170, "g", BR)
    E.escreve(c, "× 60 = 72.000 Hz?", 84, 580, 110, "g", BR)
    E.risco(c, 70, 610, 1130, 480, 9, 0, AMARELO, 26)
    E.escreve(c, "o certo é ÷ 60:", 84, 790, 100, "i", AMARELO)
    E.escreve(c, "20 Hz", 84, 960, 160, "g", AMARELO)
    helice(c, 1560, 760, 260, E.mix(COR, BR, 0.75))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Período e", "frequência", "rpm em hertz")


def d(c):  # o macete
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o atalho", 84, 330, 120, "i", BR)
    E.escreve(c, "rpm ÷ 60 = Hz", 76, 540, 150, "g", BR)
    E.formula(c, "T = f{60}{rpm}", 84, 800, 150, "g", E.mix(COR, BR, 0.5))
    helice(c, 1560, 800, 220, BR, 60)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_vezes_60_nao", a), ("capa_B_periodo_e_frequencia", b), ("capa_C_rpm_dividido_por_60", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
