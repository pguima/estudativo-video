"""Capas do FIS-OPT-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o lápis", 84, 400, 170, "g", BR)
    E.escreve(c, "não quebrou", 84, 580, 150, "g", AMARELO)
    E.escreve(c, "foi a luz que entortou", 84, 780, 84, "i", BR)
    c.drawRect(skia.Rect.MakeLTRB(1300, 560, 1700, 900), M.paint("#FFFFFF", 0.3))
    for x0, y0, x1, y1 in ((1300, 260, 1300, 900), (1700, 260, 1700, 900), (1300, 900, 1700, 900)):
        M.line(c, x0, y0, x1, y1, BR, 1.0, 10)
    M.line(c, 1380, 220, 1520, 560, AMARELO, 1.0, 26); M.line(c, 1520, 560, 1580, 820, AMARELO, 1.0, 26)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Snell", "e índice", "refração do zero")


def d(c):  # o macete
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "maior índice,", 84, 400, 140, "g", BR)
    E.escreve(c, "menor ângulo", 84, 570, 140, "g", claro)
    E.formula(c, "n₁ · sen i = n₂ · sen r", 84, 800, 96, "g", BR)
    E.orbita(c, 1640, 300, 170, E.mix(COR, BR, 0.82))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_lapis_nao_quebrou", a), ("capa_B_lei_de_snell", b), ("capa_C_maior_indice_menor_angulo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
