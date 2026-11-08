"""Capas do MAT-EQU-012 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: 5 equações, você resolve?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5 equações", 84, 400, 220, "g", BR)
    E.formula(c, "f{x}{3} − 2 = f{x}{5}", 84, 720, 190, cor=AMARELO)
    E.escreve(c, "você resolve?", 84, 960, 150, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "equações", "do 1º grau")


def d(c):  # o macete: o lado com mais x
    palco(c)
    E.escreve(c, "deixe o x no lado", 84, 360, 140, "i", BR)
    E.escreve(c, "com mais x", 76, 580, 210, "g", BR)
    E.formula(c, "x + 13 = 4x − 8", 84, 820, 150, cor=BR)
    E.formula(c, "13 = 3x − 8", 84, 990, 150, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cinco_equacoes", a), ("capa_B_praticando_equacoes", b), ("capa_C_lado_com_mais_x", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
