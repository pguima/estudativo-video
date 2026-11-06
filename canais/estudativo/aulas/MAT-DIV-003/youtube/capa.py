"""Capas do MAT-DIV-003 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: 91 é primo?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "91", 110, 590, 480, "g", "#FFD500")
    E.escreve(c, "é primo?", 760, 500, 230, "g", BR)
    E.escreve(c, "muita gente erra", 116, 860, 180, "i", BR)


def b(c):  # o assunto
    E.capa_modelo(c, "Matemática", "Números", "primos", "e fatoração")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "é primo? o atalho", 116, 370, 150, "i", BR)
    E.escreve(c, "pare no 11", 110, 640, 280, "g", BR)
    E.escreve(c, "97 ÷ 11 dá 8", 116, 860, 170, "g", E.mix(COR, BR, 0.5))
    E.escreve(c, "e 8 < 11", 1240, 850, 110, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_91_e_primo", a), ("capa_B_primos_fatoracao", b), ("capa_C_atalho", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
