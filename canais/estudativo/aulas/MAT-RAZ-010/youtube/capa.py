"""Capas do MAT-RAZ-010 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
CL = E.mix(COR, BR, 0.55)


def grade(c, x, y, n, s, k, c1, c2):
    for r in range(n):
        for j in range(n):
            M.rrect(c, x + j * s + 3, y + r * s + 3, s - 6, s - 6, s * 0.12, c1 if ((r // k) + (j // k)) % 2 == 0 else c2)


def a(c):  # o gancho: 18 m²? não: 36
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    grade(c, 90, 330, 3, 70, 3, BR, BR)
    E.centro(c, "3 m", 195, 620, 56, "g", BR)
    grade(c, 400, 260, 6, 70, 3, BR, CL)
    E.centro(c, "6 m", 610, 740, 56, "g", BR)
    E.escreve(c, "18 m²?", 940, 470, 150, "g", BR)
    E.risco(c, 930, 500, 1460, 360, 9, 0, "#FFD500", 26)
    E.escreve(c, "36 m²", 940, 720, 220, "g", "#FFD500")
    E.escreve(c, "dobrou o lado", 84, 970, 110, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Lado × 2,", "área × 4", "por quê?")


def d(c):  # o atalho: fator ao quadrado
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.formula(c, "lado × 3", 84, 560, 170, "g", BR)
    E.formula(c, "área × 3^2 = 9", 84, 790, 170, "g", CL)
    grade(c, 1380, 500, 6, 72, 2, BR, CL)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_18_ou_36", a), ("capa_B_lado_area", b), ("capa_C_fator_ao_quadrado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
