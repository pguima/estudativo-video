"""Capas da QUI-ATO-002 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import quimica as Q
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
OURO = "#F2D06B"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")


def alfa(c, x, y, r, cor=None):
    E.bola(c, x, y, r, cor or E.mix(COR, "#000000", 0.25))
    s = r * 0.45
    M.line(c, x - s, y, x + s, y, BR, 1, max(3, r * 0.2)); M.line(c, x, y - s, x, y + s, BR, 1, max(3, r * 0.2))


def nuclear(c, cx, cy, R, tinta=BR):
    for k in range(3):
        c.save(); c.translate(cx, cy); c.rotate(k * 60)
        c.drawOval(skia.Rect.MakeXYWH(-R, -R * 0.38, 2 * R, R * 0.76), M.paint(tinta, 0.8, stroke=5))
        ang = k * 2.1
        E.bola(c, R * math.cos(ang), R * 0.38 * math.sin(ang), R * 0.07, Q.ELETRON)
        c.restore()
    E.bola(c, cx, cy, R * 0.07, AMARELO)


def a(c):  # o gancho: atirar contra uma folha e a bolinha voltar
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "e se a bala", 84, 380, 140, "i", BR)
    E.escreve(c, "voltasse?", 84, 570, 200, "g", BR)
    M.rrect(c, 1380, 180, 26, 720, 6, OURO, 1, shadow=True)
    for k, y in enumerate((260, 400, 560, 700, 840)):
        alfa(c, 1650 if k != 2 else 1000, y, 40)
    M.arrow(c, 1330, 640, 1060, 640, AMARELO, 1, 12, 40)
    E.escreve(c, "a folha de ouro", 84, 880, 100, "g", AMARELO)


def b(c):
    E.capa_modelo(c, "Química", "Rutherford", "e o núcleo", "do zero")


def d(c):  # o macete: três linhas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    for k, (o, cc) in enumerate((("atravessou", "vazio"), ("desviou", "positivo"), ("voltou", "núcleo"))):
        y = 400 + k * 200
        E.escreve(c, o, 84, y, 110, "g", BR)
        E.escreve(c, "→ " + cc, 760, y, 110, "g", claro)
    nuclear(c, 1680, 640, 210)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_bala_que_volta", a), ("capa_B_rutherford_e_o_nucleo", b), ("capa_C_tres_linhas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
