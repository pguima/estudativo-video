"""Capas do MAT-DIV-002 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: 4.572 se divide por 9?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "4.572", 110, 500, 340, "g", BR)
    E.escreve(c, "se divide por", 116, 690, 150, "i", BR)
    E.escreve(c, "9?", 860, 730, 260, "g", "#FFD500")
    E.escreve(c, "sem armar a conta", 116, 900, 130, "g", BR)


def b(c):  # o assunto
    E.capa_modelo(c, "Matemática", "Testes de", "divisibilidade", "sem dividir")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 116, 370, 150, "i", BR)
    E.escreve(c, "noves fora", 110, 640, 280, "g", BR)
    E.escreve(c, "4 + 5 = 9", 116, 860, 170, "g", E.mix(COR, BR, 0.5))
    E.escreve(c, "risca e pronto", 1000, 850, 100, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_4572_por_9", a), ("capa_B_regras_divisibilidade", b), ("capa_C_atalho", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
