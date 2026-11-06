"""Capas do MAT-NUM-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o zero que faltou
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "34 × 26 =", 84, 460, 230, "g", BR)
    E.escreve(c, "272", 1210, 460, 260, "g", BR)
    E.risco(c, 1180, 500, 1740, 240, 9, 0, AMARELO, 34)
    E.escreve(c, "884", 1210, 760, 290, "g", AMARELO)
    E.escreve(c, "faltou", 84, 680, 150, "i", BR)
    E.escreve(c, "um zero", 84, 860, 180, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Multiplicar", "por dois", "algarismos")


def d(c):  # o macete: conferir pelo tamanho
    escuro(c)
    E.escreve(c, "a conta deu certo?", 84, 350, 150, "i", BR)
    E.escreve(c, "confira pelo", 76, 545, 170, "g", BR)
    E.escreve(c, "tamanho", 76, 720, 170, "g", AMARELO)
    E.escreve(c, "30 × 30 = 900", 84, 950, 170, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_faltou_um_zero", a), ("capa_B_multiplicar_dois_algarismos", b), ("capa_C_conferir_pelo_tamanho", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
