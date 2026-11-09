"""Capas do FIS-EGF-001 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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


def gangorra(c, cx, cy, L, ang, cor_tab="#FFFFFF", cor_ap="#FFFFFF"):
    p = skia.Path(); p.moveTo(cx, cy); p.lineTo(cx - 70, cy + 110); p.lineTo(cx + 70, cy + 110); p.close()
    c.drawPath(p, M.paint(cor_ap))
    c.save(); c.translate(cx, cy - 14); c.rotate(ang)
    M.rrect(c, -L / 2, -16, L, 32, 10, cor_tab)
    c.restore()


def a(c):  # o gancho: quem pesa o dobro senta onde?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o dobro", 84, 400, 190, "g", BR)
    E.escreve(c, "do peso,", 84, 590, 190, "g", BR)
    E.escreve(c, "senta onde?", 84, 790, 120, "i", BR)
    claro = E.mix(COR, BR, 0.82)
    gangorra(c, 1500, 740, 760, 0, claro, claro)
    F.bloco(c, 1210, 640, 140, 120, "30 kg", cor="#1B1B20", size=40)
    F.bloco(c, 1650, 630, 170, 140, "60 kg", cor="#1B1B20", size=44)
    E.escreve(c, "?", 1620, 520, 150, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Torque", "e alavancas", "do zero")


def d(c):  # o macete: corte o 10
    palco_capa(c)
    E.escreve(c, "gangorra:", 84, 330, 120, "i", BR)
    E.escreve(c, "nem calcule o peso", 84, 500, 120, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "30 · 10 · 2 = 60 · 10 · d", 84, 760, 130, "g", BR)
    w0 = E.formula(None, "30 · ", 0, 0, 130, a=0)
    w1 = E.formula(None, "30 · 10 · 2 = 60 · ", 0, 0, 130, a=0)
    wd = E.formula(None, "10", 0, 0, 130, a=0)
    for x in (84 + w0, 84 + w1):
        M.line(c, x - 10, 780, x + wd + 10, 660, AMARELO, 1.0, 14)
    E.formula(c, "d = 1 m", 84, 960, 130, "g", claro)
    E.selo(c, 760, 915, 70, True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dobro_do_peso", a), ("capa_B_torque_e_alavancas", b), ("capa_C_nem_calcule_o_peso", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
