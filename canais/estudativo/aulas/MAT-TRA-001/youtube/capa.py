"""Capas do MAT-TRA-001 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
S = lambda g: math.sin(math.radians(g))


def triangulo(c, x0, y0, base, ga, gb, cor_a, cor_b, txt_a, txt_b, tinta=BR):
    """triângulo com ângulos ga (esquerda) e gb (direita); pinta o lado de frente para cada um"""
    gc = 180 - ga - gb
    ac = base * S(gb) / S(gc)
    A, B = (x0, y0), (x0 + base, y0)
    Cc = (x0 + ac * math.cos(math.radians(ga)), y0 - ac * S(ga))
    path = skia.Path(); path.addPoly([A, B, Cc], True)
    c.drawPath(path, M.paint(tinta, 0.12))
    M.line(c, *A, *B, tinta, 1.0, 8)
    M.line(c, *B, *Cc, cor_a, 1.0, 14)
    M.line(c, *Cc, *A, cor_b, 1.0, 14)
    E.escreve(c, txt_a, (B[0] + Cc[0]) / 2 + 30, (B[1] + Cc[1]) / 2 - 10, 90, "g", cor_a)
    E.escreve(c, txt_b, (A[0] + Cc[0]) / 2 - 90, (A[1] + Cc[1]) / 2 - 20, 90, "g", cor_b)
    E.escreve(c, f"{ga}°", A[0] + 90, A[1] - 24, 64, "g", tinta)
    E.escreve(c, f"{gb}°", B[0] - 230, B[1] - 24, 64, "g", tinta)


def a(c):  # o gancho: o lado que falta, sem ângulo reto
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "sem ângulo", 84, 400, 160, "g", BR)
    E.escreve(c, "reto", 84, 580, 160, "g", AMARELO)
    E.escreve(c, "e agora?", 84, 760, 130, "i", BR)
    triangulo(c, 900, 900, 900, 30, 45, BR, AMARELO, "10", "?")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Lei dos", "senos", "sem decorar")


def d(c):  # o atalho: o número fixo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o número fixo", 84, 360, 130, "i", BR)
    E.formula(c, "f{10}{sen 30°} = 20", 84, 640, 170, "g", AMARELO)
    E.formula(c, "x = 20 · sen 45° = 10r{2}", 84, 900, 120, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sem_angulo_reto", a), ("capa_B_lei_dos_senos", b), ("capa_C_numero_fixo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
