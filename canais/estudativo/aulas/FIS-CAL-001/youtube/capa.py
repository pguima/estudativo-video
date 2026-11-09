"""Capas do FIS-CAL-001 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 104 graus e ninguém ferve
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "104 graus", 84, 420, 200, "g", BR)
    E.escreve(c, "e ninguém ferve?", 84, 600, 120, "i", BR)
    F.medida(c, 104, "°F", 84, 860, 150, AMARELO, cor_u=AMARELO)
    E.escreve(c, "=", 560, 860, 150, "g", BR)
    F.medida(c, 40, "°C", 700, 860, 150, BR, cor_u=BR)
    claro = E.mix(COR, BR, 0.82)
    # termômetro grande à direita
    cx, yb, h = 1600, 960, 760
    M.rrect(c, cx - 40, yb - h, 80, h, 40, claro)
    c.drawCircle(cx, yb, 95, M.paint(claro))
    M.rrect(c, cx - 18, yb - h * 0.62, 36, h * 0.62, 18, AMARELO)
    c.drawCircle(cx, yb, 70, M.paint(AMARELO))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "°C, °F", "e Kelvin", "do zero")


def d(c):  # o macete: conte de 5 em 5
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "conte de", 84, 340, 130, "i", BR)
    E.escreve(c, "5 em 5", 84, 540, 200, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (a_, f_) in enumerate(((0, 32), (5, 41), (10, 50))):
        x = 330 + i * 600
        E.centro(c, f"{a_} °C", x, 780, 110, "g", BR)
        E.centro(c, f"{f_} °F", x, 960, 110, "g", claro)
    for i in range(2):
        x = 330 + i * 600
        F.seta(c, x + 180, 745, x + 420, 745, claro, 1.0, 10)
        E.centro(c, "+5", x + 300, 700, 56, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_104_graus", a), ("capa_B_escalas_do_zero", b), ("capa_C_conte_de_5_em_5", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
