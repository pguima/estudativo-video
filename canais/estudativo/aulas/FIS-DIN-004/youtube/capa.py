"""Capas do FIS-DIN-004 (1280x720). Uso: python capa.py"""
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


def visor(c, x, y, s):
    M.rrect(c, x, y, 520, 230, 36, "#1B1B20")
    E.escreve(c, s, x + 60, y + 170, 150, "g", "#7CFFB2")


def a(c):  # o gancho: a balança mente no elevador
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "A balança", 84, 400, 170, "g", BR)
    E.escreve(c, "mente", 84, 590, 170, "g", AMARELO)
    E.escreve(c, "no elevador", 84, 780, 150, "g", BR)
    E.escreve(c, "peso e normal", 84, 940, 100, "i", BR)
    visor(c, 1260, 360, "72 kg")
    E.escreve(c, "massa: 60 kg", 1290, 700, 90, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Peso e", "normal", "P = m·g")


def d(c):  # o macete: N = m(g ± a)
    palco(c)
    E.escreve(c, "elevador numa conta só", 84, 330, 110, "i", BR)
    E.escreve(c, "N = m(g + a)", 84, 580, 190, "g", BR)
    E.escreve(c, "aceleração para cima", 84, 760, 90, "i", E.mix(COR, BR, 0.5))
    E.escreve(c, "e m(g − a) para baixo", 84, 900, 90, "i", BR)


CAPAS = (("capa_A_a_balanca_mente_no_elevador", a), ("capa_B_peso_e_normal", b), ("capa_C_elevador_numa_conta", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
