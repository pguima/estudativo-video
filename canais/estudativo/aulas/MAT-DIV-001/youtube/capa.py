"""Capas do MAT-DIV-001 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: os divisores do 36
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "quantos", 116, 350, 170, "i", BR)
    E.escreve(c, "divisores", 110, 610, 290, "g", BR)
    E.escreve(c, "tem o", 116, 840, 170, "i", BR)
    E.escreve(c, "36?", 560, 900, 320, "g", "#FFD500")


def b(c):  # o assunto
    E.capa_modelo(c, "Matemática", "Divisores", "e múltiplos", "sem confusão")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 116, 370, 150, "i", BR)
    E.escreve(c, "pare no 6", 110, 640, 280, "g", BR)
    E.escreve(c, "6 × 6 = 36", 116, 870, 170, "g", E.mix(COR, BR, 0.5))
    E.escreve(c, "e os pares acabam", 1010, 860, 84, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_divisores_36", a), ("capa_B_multiplos_divisores", b), ("capa_C_atalho", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
