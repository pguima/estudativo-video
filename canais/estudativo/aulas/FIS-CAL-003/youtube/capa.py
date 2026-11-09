"""Capas do FIS-CAL-003 (1280x720). Uso: python capa.py"""
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
CLARO = E.mix(COR, BR, 0.82)
E.usar("Física")


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: a areia queima e o mar não
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a areia", 84, 400, 190, "g", BR)
    E.escreve(c, "queima,", 84, 590, 190, "g", AMARELO)
    E.escreve(c, "o mar não", 84, 780, 150, "i", BR)
    x, y = 1150, 700
    M.rrect(c, x, y, 330, 260, 30, "#E8C77A")
    M.rrect(c, x + 360, y, 330, 260, 30, "#5BA8E0")
    c.drawCircle(x + 345, y - 260, 110, M.paint(AMARELO))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Calor", "sensível", "do zero")


def d(c):  # o macete: que macete
    palco_capa(c)
    E.escreve(c, "o macete do", 84, 340, 130, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (l, s) in enumerate((("Q", "que"), ("m", "ma"), ("c", "ce"), ("ΔT", "te"))):
        x = 260 + i * 440
        E.formula(c, l, x, 690, 220, "g", BR, 1.0, "center")
        E.centro(c, s, x, 920, 150, "g", claro)


CAPAS = (("capa_A_areia_queima", a), ("capa_B_calor_sensivel", b), ("capa_C_que_macete", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
