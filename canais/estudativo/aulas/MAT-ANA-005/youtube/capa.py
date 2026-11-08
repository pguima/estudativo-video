"""Capas do MAT-ANA-005 (1280x720). Uso: python capa.py"""
import math
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"


def cruz(c, cx, cy, m1, m2, L, cor1, cor2, larg=16, q=60):
    """duas retas pelo ponto (cx, cy) com inclinações m1 e m2 (em pixel, y para cima) e o quadradinho do ângulo reto"""
    for m, cor in ((m1, cor1), (m2, cor2)):
        u = (1 / math.hypot(1, m), -m / math.hypot(1, m))
        M.line(c, cx - u[0] * L, cy - u[1] * L, cx + u[0] * L, cy + u[1] * L, cor, 1, larg)
    u1 = (1 / math.hypot(1, m1), -m1 / math.hypot(1, m1))
    u2 = (-1 / math.hypot(1, m2), m2 / math.hypot(1, m2))
    a, b = (cx + u1[0] * q, cy + u1[1] * q), (cx + u2[0] * q, cy + u2[1] * q)
    d = (a[0] + u2[0] * q, a[1] + u2[1] * q)
    M.line(c, *a, *d, BR, 1, 7); M.line(c, *d, *b, BR, 1, 7)


def a(c):  # o gancho: o ângulo reto sem desenhar
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    cruz(c, 1480, 560, 2, -0.5, 470, BR, AMARELO)
    E.escreve(c, "ângulo reto", 84, 400, 150, "i", BR)
    E.escreve(c, "só pelo m", 76, 600, 190, "g", BR)
    E.formula(c, "2 · (−f{1}{2}) = −1", 84, 900, 130, "g", AMARELO)


def b(c):  # o modelo
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)  # o modelo, com a 2ª linha menor: a palavra é longa
    E.escreve(c, "Paralelas e", 76, 450, 210, "g", BR)
    E.escreve(c, "perpendiculares", 76, 640, 160, "g", BR)
    E.escreve(c, "pelo m", 84, 860, 170, "i", BR)
    E.mais(c, 1640, 800, 170, E.mix(COR, BR, 0.82), 1.0)


def d(c):  # o atalho: inverte e troca o sinal
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "inverte e", 84, 380, 150, "i", BR)
    E.escreve(c, "troca o sinal", 76, 580, 180, "g", BR)
    E.formula(c, "2", 120, 880, 190, "g", BR)
    E.formula(c, "→", 330, 880, 170, "g", E.mix(COR, BR, 0.5))
    E.formula(c, "−f{1}{2}", 560, 880, 190, "g", "#FFB833")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_angulo_reto_pelo_m", a), ("capa_B_paralelas_perpendiculares", b), ("capa_C_inverte_e_troca", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
