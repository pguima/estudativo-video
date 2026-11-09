"""Capas do FIS-CIN-005 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: km 240 ou km 260?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.55)
    E.escreve(c, "do km 20, 3 h a 80 km/h", 84, 380, 96, "g", BR)
    E.escreve(c, "km 240?", 84, 600, 200, "g", BR)
    E.risco(c, 70, 640, 800, 460, 9, 0, AMARELO, 24)
    E.escreve(c, "não: km 260", 84, 820, 130, "g", AMARELO)
    E.escreve(c, "você esqueceu de onde ele saiu", 84, 960, 70, "i", claro)
    F.carrinho(c, 1560, 760, 520, cor=BR)
    M.line(c, 1180, 760, 1900, 760, BR, 1.0, 8)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Movimento", "uniforme", "a função horária")


def d(c):  # o macete: sorvete
    palco(c)
    E.escreve(c, "a fórmula do", 84, 330, 120, "i", BR)
    E.escreve(c, "sorvete", 76, 560, 230, "g", BR)
    E.formula(c, "s = s₀ + v · t", 84, 860, 170, "g", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_km_240_ou_260", a), ("capa_B_movimento_uniforme", b), ("capa_C_sorvete", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
