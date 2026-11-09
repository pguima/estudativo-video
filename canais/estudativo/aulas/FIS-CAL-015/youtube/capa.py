"""Capas do FIS-CAL-015 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)




def a(c):  # o gancho: o motor de 60 % é mentira?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "motor de 60 %?", 84, 400, 170, "g", BR)
    E.escreve(c, "impossível", 84, 600, 170, "g", AMARELO)
    E.escreve(c, "entre 327 °C e 27 °C, o máximo é 50 %", 84, 820, 70, "i", BR)
    E.selo(c, 1660, 520, 170, False)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Carnot", 76, 430, 210, "g", BR)
    E.escreve(c, "o rendimento máximo", 76, 620, 130, "g", BR)
    E.escreve(c, "sempre em kelvin", 84, 840, 120, "i", BR)
    E.simbolo(c, 1640, 820, 190, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: diferença sobre a quente
    palco_capa(c)
    E.escreve(c, "a diferença", 84, 360, 150, "g", BR)
    E.escreve(c, "sobre a quente em kelvin", 84, 500, 100, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "f{327 − 27}{600} = 50 %", 84, 820, 130, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_motor_impossivel", a), ("capa_B_carnot", b), ("capa_C_diferenca_sobre_a_quente", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
