"""Capas do FIS-MAG-002 (1280x720). Uso: python capa.py"""
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


def bussola(c, cx, cy, r, ang):
    c.drawCircle(cx, cy, r, M.paint(BR))
    c.drawCircle(cx, cy, r, M.paint("#1B1B22", 1, stroke=r * 0.08))
    ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
    nx, ny = -uy, ux
    for s, cor in ((1, COR), (-1, F.NEG)):
        p = skia.Path(); p.moveTo(cx + ux * r * 0.8 * s, cy + uy * r * 0.8 * s); p.lineTo(cx + nx * r * 0.22, cy + ny * r * 0.22)
        p.lineTo(cx - nx * r * 0.22, cy - ny * r * 0.22); p.close()
        c.drawPath(p, M.paint(cor))
    c.drawCircle(cx, cy, r * 0.1, M.paint("#1B1B22"))


def a(c):  # o gancho: a corrente gira a bússola
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a corrente", 84, 380, 150, "i", BR)
    E.escreve(c, "gira a", 84, 590, 200, "g", BR)
    E.escreve(c, "bússola", 84, 790, 200, "g", AMARELO)
    bussola(c, 1480, 560, 250, 180)
    M.line(c, 1480, 150, 1480, 980, "#1B1B22", 1, 16)
    for y in (260, 860):
        F._cabeca(c, 1480, y, 0, -1, 60, AMARELO, 1)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Campo da", "corrente", "do zero")


def d(c):  # o macete: μ₀/2π = 2·10⁻⁷
    palco_capa(c)
    E.escreve(c, "o atalho do fio", 84, 330, 120, "i", BR)
    E.formula(c, "B = 2 · 10^{−7} · f{i}{d}", 84, 640, 210, "g", BR)
    E.escreve(c, "sem pi na conta", 84, 900, 110, "i", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_corrente_gira_a_bussola", a), ("capa_B_campo_da_corrente", b), ("capa_C_atalho_do_fio", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
