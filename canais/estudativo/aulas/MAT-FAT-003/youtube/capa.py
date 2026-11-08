"""Capas do MAT-FAT-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 1.001² − 999² de cabeça
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "1.001^2 − 999^2", 84, 440, 190, cor=BR)
    E.formula(c, "= 4.000", 84, 760, 250, cor=AMARELO)
    E.escreve(c, "de cabeça", 84, 960, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Fatorar com", "notáveis", "diferença e trinômio")


def d(c):  # o atalho / a ferramenta: dois quadrados com menos
    palco(c)
    E.escreve(c, "dois quadrados com menos", 84, 330, 110, "i", BR)
    E.formula(c, "x^2 − 49", 84, 600, 190, cor=BR)
    E.formula(c, "= (x + 7)(x − 7)", 84, 860, 180, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_1001_ao_quadrado", a), ("capa_B_fatorar_com_notaveis", b), ("capa_C_diferenca_de_quadrados", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
