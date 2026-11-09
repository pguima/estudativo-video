"""Capas do FIS-DIN-007 (1280x720). Uso: python capa.py"""
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


def fsub(c, base, sb, x, y, size, cor):
    """letra com subscrito (F com R embaixo); devolve a largura"""
    E.escreve(c, base, x, y, size, "g", cor)
    w = E.larg(base, "g", size)
    E.escreve(c, sb, x + w + size * 0.02, y + size * 0.2, size * 0.6, "g", cor)
    return w + E.larg(sb, "g", size * 0.6) + size * 0.06


def a(c):  # o gancho: por que o ABS freia em menos metros
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Por que o", 84, 400, 160, "g", BR)
    E.escreve(c, "ABS freia", 84, 580, 190, "g", AMARELO)
    E.escreve(c, "em menos metros?", 84, 760, 110, "g", BR)
    E.escreve(c, "a força de atrito explica", 84, 920, 90, "i", BR)
    for i, (d, s) in enumerate(((25, "25 m"), (40, "40 m"))):
        y = 330 + i * 200
        M.line(c, 1300, y, 1300 + d * 14, y, BR, 1.0, 16)
        E.escreve(c, s, 1310, y - 40, 90, "g", AMARELO if i == 0 else BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Força de", "atrito", "e o freio ABS")


def d(c):  # o macete: a = μ·g
    palco(c)
    E.escreve(c, "freou só com o atrito?", 84, 330, 110, "i", BR)
    E.escreve(c, "a = μ·g", 84, 610, 240, "g", BR)
    E.escreve(c, "a massa nem entra", 84, 820, 110, "i", E.mix(COR, BR, 0.5))
    E.selo(c, 1650, 540, 150, True)


CAPAS = (("capa_A_por_que_o_abs_freia_antes", a), ("capa_B_forca_de_atrito", b), ("capa_C_a_igual_mi_g", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
