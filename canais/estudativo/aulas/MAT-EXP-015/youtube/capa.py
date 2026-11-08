"""Capas do MAT-EXP-015 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF4D55"


def a(c):  # o gancho: 4 situações, uma armadilha (o −5)
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "4", 70, 560, 380, "g", AMARELO)
    E.escreve(c, "situações", 330, 420, 130, "g", BR)
    E.escreve(c, "de logaritmo", 330, 540, 100, "i", BR)
    E.escreve(c, "x = 5", 84, 860, 150, "g", BR)
    E.escreve(c, "ou", 520, 860, 110, "i", BR)
    E.escreve(c, "x = −5?", 680, 860, 150, "g", VERMELHO)
    E.risco(c, 670, 880, 680 + E.larg("x = −5?", "g", 150) + 10, 760, 1, 0, AMARELO, 24)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Praticando", "logaritmos", "4 situações de ciências")


def d(c):  # o atalho: +0,30 dobra
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho:", 84, 340, 120, "i", claro)
    E.escreve(c, "+0,30", 76, 580, 200, "g", AMARELO)
    E.escreve(c, "= dobrar", 700, 580, 170, "g", BR)
    E.escreve(c, "+0,48", 76, 820, 200, "g", claro)
    E.escreve(c, "= triplicar", 700, 820, 170, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_x_menos_5", a), ("capa_B_praticando_logaritmos", b), ("capa_C_mais_030_dobra", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
