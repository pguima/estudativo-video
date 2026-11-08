"""Capas do MAT-MTZ-009 (1280x720). Uso: python capa.py"""
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


def a(c):  # o desafio: 5 questões
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5", 70, 700, 560, "g", AMARELO)
    E.escreve(c, "questões", 470, 470, 170, "g", BR)
    E.escreve(c, "de sistemas", 480, 640, 120, "i", BR)
    for i, l in enumerate(("x + y + z = 9", "x − y + z = 3", "2x + y − z = 3")):
        E.escreve(c, l, 1290, 330 + i * 110, 74, "g", BR)
    E.escreve(c, "(?, ?, ?)", 1330, 760, 110, "g", AMARELO)
    E.escreve(c, "você resolve antes de mim?", 84, 990, 90, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Sistemas", "na prática", "5 questões")


def d(c):  # o atalho: equações quase iguais
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "uma subtração só:", 84, 380, 130, "i", BR)
    E.escreve(c, "quase iguais", 76, 590, 200, "g", BR)
    E.escreve(c, "x + y + z = 9", 120, 790, 100, "g", BR)
    E.escreve(c, "x − y + z = 3", 120, 920, 100, "g", BR)
    E.escreve(c, "→ 2y = 6", 1000, 860, 140, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_5_questoes", a), ("capa_B_sistemas_na_pratica", b), ("capa_C_quase_iguais", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
