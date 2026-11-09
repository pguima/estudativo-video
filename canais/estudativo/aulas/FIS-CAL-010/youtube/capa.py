"""Capas do FIS-CAL-010 (1280x720). Uso: python capa.py"""
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
AZUL = F.NEG
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def laco(c, cx, cy, rx, ry, quente, frio, larg=26):
    n = 90
    for i in range(n):
        g0, g1 = math.pi / 2 + 2 * math.pi * i / n, math.pi / 2 + 2 * math.pi * (i + 1) / n
        x0, y0 = cx + rx * math.cos(g0), cy + ry * math.sin(g0)
        x1, y1 = cx + rx * math.cos(g1), cy + ry * math.sin(g1)
        M.line(c, x0, y0, x1, y1, quente if x0 < cx else frio, 1.0, larg, cap_round=True)
    for f in (0.125, 0.375, 0.625, 0.875):
        g = math.pi / 2 + 2 * math.pi * f
        x, y = cx + rx * math.cos(g), cy + ry * math.sin(g)
        dx, dy = -rx * math.sin(g), ry * math.cos(g)
        L = math.hypot(dx, dy)
        F._cabeca(c, x + dx / L * 40, y + dy / L * 40, dx / L, dy / L, 80, quente if x < cx else frio, 1.0)


def a(c):  # o erro: "o calor sobe"
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "“o calor", 84, 420, 190, "g", BR)
    E.escreve(c, "sobe”?", 84, 630, 190, "g", BR)
    E.risco(c, 70, 660, 760, 470, 9, 0, AMARELO, 30)
    E.escreve(c, "quem sobe é o ar quente", 84, 900, 92, "i", BR)
    laco(c, 1500, 560, 260, 300, BR, E.mix(COR, "#000000", 0.45))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Convecção", "e irradiação", "do zero")


def d(c):  # o macete: duas perguntas
    palco_capa(c)
    E.escreve(c, "2 perguntas", 84, 380, 190, "g", BR)
    E.escreve(c, "e você acerta o processo", 84, 520, 96, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (s, r) in enumerate((("precisa de matéria?", "não → irradiação"), ("a matéria anda?", "sim → convecção"))):
        y = 720 + i * 170
        E.escreve(c, s, 84, y, 80, "g", BR)
        E.escreve(c, r, 1000, y, 80, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_calor_sobe", a), ("capa_B_conveccao_e_irradiacao", b), ("capa_C_duas_perguntas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
