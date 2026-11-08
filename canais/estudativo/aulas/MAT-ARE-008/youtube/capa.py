"""Capas do MAT-ARE-008 (1280x720). Uso: python capa.py"""
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
MASSA = "#F3D9A4"


def pizza(c, cx, cy, r):
    c.drawCircle(cx, cy, r, M.paint(MASSA))
    for dx, dy in ((0.35, 0.2), (-0.4, 0.3), (0.1, -0.45), (-0.2, -0.1), (0.5, -0.3), (-0.1, 0.55)):
        c.drawCircle(cx + dx * r, cy + dy * r, r * 0.09, M.paint("#C8553D", 0.85))
    c.drawCircle(cx, cy, r, M.paint("#D98A00", 1, stroke=max(8, r * 0.07)))


def a(c):  # o gancho: 1 grande ou 2 pequenas?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    pizza(c, 430, 640, 300)
    E.escreve(c, "20 cm", 330, 1040, 80, "g", BR)
    pizza(c, 1000, 560, 150); pizza(c, 1000, 880, 150)
    E.escreve(c, "10 cm", 1180, 900, 70, "g", BR)
    E.escreve(c, "qual tem", 1250, 420, 110, "i", BR)
    E.escreve(c, "mais", 1250, 600, 190, "g", AMARELO)
    E.escreve(c, "pizza?", 1250, 760, 150, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Área do", "círculo", "coroa e setor")


def d(c):  # o atalho: setor = fração da volta
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    O, r = (1500, 600), 260
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    path = skia.Path(); path.moveTo(*O); path.arcTo(ret, 0, -90, False); path.close()
    c.drawPath(path, M.paint(AMARELO, 0.9))
    c.drawCircle(*O, r, M.paint(BR, 1, stroke=10))
    E.escreve(c, "setor sem", 110, 380, 130, "i", BR)
    E.escreve(c, "regra de três", 110, 560, 140, "g", BR)
    E.formula(c, "90° = f{1}{4}", 110, 790, 130, "g", AMARELO)
    E.formula(c, "f{1}{4} · 16π = 4π", 110, 1000, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_tem_mais_pizza", a), ("capa_B_area_do_circulo", b), ("capa_C_setor_sem_regra_de_tres", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
