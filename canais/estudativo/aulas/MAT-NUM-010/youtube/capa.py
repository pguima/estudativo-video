"""Capas do MAT-NUM-010 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: dividir sem a tabuada do 23
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "1.035 ÷ 23", 84, 460, 240, "g", BR)
    E.escreve(c, "sem decorar", 84, 680, 150, "i", BR)
    E.escreve(c, "a tabuada do 23", 84, 860, 130, "g", BR)
    E.escreve(c, "= 45", 1280, 800, 240, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Dividir", "por dois", "algarismos")


def d(c):  # o macete: o tamanho do resultado
    escuro(c)
    E.escreve(c, "antes de dividir", 84, 340, 150, "i", BR)
    E.escreve(c, "veja o tamanho", 76, 545, 170, "g", BR)
    E.escreve(c, "do resultado", 76, 720, 170, "g", AMARELO)
    E.escreve(c, "× 10 e × 100", 84, 950, 170, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_tabuada_do_23", a), ("capa_B_dividir_dois_algarismos", b), ("capa_C_tamanho_do_resultado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
