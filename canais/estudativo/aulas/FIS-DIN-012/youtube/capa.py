"""Capas do FIS-DIN-012 (1280x720). Uso: python capa.py"""
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


def globo_capa(c, cx, cy, R, cor):
    import math
    for k in range(7):
        c.drawOval(skia.Rect.MakeXYWH(cx - R * abs(math.cos(k * math.pi / 7)), cy - R, 2 * R * abs(math.cos(k * math.pi / 7)), 2 * R), M.paint(cor, 0.35, stroke=4))
    c.drawCircle(cx, cy, R, M.paint(cor, 1.0, stroke=14))
    E.bola(c, cx, cy - R + 50, 46, AMARELO)


def a(c):  # o gancho: por que a moto não cai?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Por que a", 84, 400, 160, "g", BR)
    E.escreve(c, "moto não", 84, 580, 170, "g", BR)
    E.escreve(c, "cai?", 84, 770, 170, "g", AMARELO)
    E.escreve(c, "o globo da morte e a lombada", 84, 930, 84, "i", BR)
    globo_capa(c, 1500, 560, 320, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Lombada", "e looping", "e pêndulo")


def d(c):  # o macete: v mínima = √(g·R)
    palco(c)
    E.escreve(c, "velocidade mínima no topo do looping", 84, 330, 96, "i", BR)
    E.formula(c, "v = r{g·R}", 84, 620, 220, "g", BR)
    E.escreve(c, "a massa nem entra", 84, 840, 110, "i", E.mix(COR, BR, 0.5))


CAPAS = (("capa_A_por_que_a_moto_nao_cai", a), ("capa_B_lombada_looping_pendulo", b), ("capa_C_v_minima_raiz_gr", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
