"""Capas do FIS-MAG-004 (1280x720). Uso: python capa.py"""
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


def simbolo(c, cx, cy, r, sai, cor):
    c.drawCircle(cx, cy, r, M.paint(BR))
    c.drawCircle(cx, cy, r, M.paint(cor, 1, stroke=r * 0.16))
    if sai:
        c.drawCircle(cx, cy, r * 0.3, M.paint(cor))
    else:
        k = r * 0.6
        M.line(c, cx - k, cy - k, cx + k, cy + k, cor, 1, r * 0.16)
        M.line(c, cx - k, cy + k, cx + k, cy - k, cor, 1, r * 0.16)


def a(c):  # o gancho: por que o motor gira
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "por que o", 84, 380, 140, "i", BR)
    E.escreve(c, "motor", 84, 610, 230, "g", BR)
    E.escreve(c, "gira?", 84, 820, 200, "g", AMARELO)
    cx, cy = 1460, 560
    M.rrect(c, 1080, 300, 140, 520, 16, "#FFFFFF"); E._meio(c, "N", 1150, 560, 80, "g", COR)
    M.rrect(c, 1700, 300, 140, 520, 16, F.NEG); E._meio(c, "S", 1770, 560, 80, "g", BR)
    M.line(c, cx - 180, cy, cx + 180, cy, "#1B1B22", 1, 10)
    simbolo(c, cx - 180, cy, 50, True, "#1B1B22"); simbolo(c, cx + 180, cy, 50, False, "#1B1B22")
    F.seta(c, cx - 180, cy - 60, cx - 180, cy - 240, AMARELO, 1, 16)
    F.seta(c, cx + 180, cy + 60, cx + 180, cy + 240, AMARELO, 1, 16)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Força no", "fio e motor", "elétrico")


def d(c):  # o macete: troque q·v por i·L
    palco_capa(c)
    E.escreve(c, "uma fórmula só", 84, 330, 120, "i", BR)
    E.formula(c, "q · v  =  i · L", 84, 600, 190, "g", BR)
    E.formula(c, "F = q·v·B  →  F = B·i·L", 84, 860, 100, "g", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_por_que_o_motor_gira", a), ("capa_B_forca_no_fio_e_motor", b), ("capa_C_uma_formula_so", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
