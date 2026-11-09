"""Capas do FIS-DIN-008 (1280x720). Uso: python capa.py"""
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


def rampa_capa(c, x, y, base, ang, cor, bloco):
    import math
    h = base * math.tan(math.radians(ang))
    p = skia.Path(); p.moveTo(x, y); p.lineTo(x + base, y); p.lineTo(x + base, y - h); p.close()
    c.drawPath(p, M.paint(cor, 0.25))
    pt = M.paint(cor, 1.0, stroke=10); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)
    F.bloco(c, x + base * 0.55, y - h * 0.55 - 90, 200, 150, None, bloco, 1.0, giro=ang)


def a(c):  # o gancho: pesada e leve chegam juntas
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Pesada ou leve:", 84, 400, 140, "g", BR)
    E.escreve(c, "chegam", 84, 590, 180, "g", AMARELO)
    E.escreve(c, "juntas", 84, 770, 180, "g", AMARELO)
    E.escreve(c, "a física do plano inclinado", 84, 930, 84, "i", BR)
    rampa_capa(c, 1130, 980, 700, 30, BR, AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Plano", "inclinado", "seno e cosseno")


def d(c):  # o macete: a = g·sen θ
    palco(c)
    E.escreve(c, "rampa sem atrito?", 84, 330, 110, "i", BR)
    E.escreve(c, "a = g·sen θ", 84, 610, 210, "g", BR)
    E.escreve(c, "a massa nem entra", 84, 820, 110, "i", E.mix(COR, BR, 0.5))


CAPAS = (("capa_A_pesada_ou_leve_chegam_juntas", a), ("capa_B_plano_inclinado", b), ("capa_C_a_igual_g_sen", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
