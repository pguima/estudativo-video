"""Capas do MAT-FRA-012 (1280x720). Uso: python capa.py"""
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
CLARO = E.mix(COR, BR, 0.5)


def a(c):  # o gancho: dá 7/8? não, dá 1
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    y, s = 500, 240
    E.fracao(c, 1, 2, 210, y, s, BR)
    E.escreve(c, "+", 340, y + 70, 190, "g", BR)
    E.fracao(c, 2, 3, 610, y, s, BR)
    E.escreve(c, "×", 740, y + 70, 190, "g", BR)
    E.fracao(c, 3, 4, 1010, y, s, BR)
    E.escreve(c, "=", 1140, y + 70, 190, "g", BR)
    E.escreve(c, "1", 1340, y + 120, 340, "g", AMARELO)
    E.escreve(c, "?", 1560, y + 110, 320, "g", BR)
    E.escreve(c, "não dá 7/8", 84, 985, 170, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Expressões", "com frações", "negativas e mistos")


def d(c):  # o atalho: separe em blocos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "separe em", 84, 360, 170, "i", BR)
    E.escreve(c, "blocos", 680, 360, 190, "g", AMARELO)
    y, s = 720, 220
    p = M.paint(AMARELO, 1, stroke=8)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(120, y - 235, 300, 470), 28, 28), p)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(620, y - 235, 790, 470), 28, 28), p)
    E.fracao(c, 7, 8, 270, y, s, BR)
    E.escreve(c, "−", 465, y + 60, 170, "g", BR)
    E.fracao(c, 1, 4, 770, y, s, BR)
    E.escreve(c, "÷", 925, y + 60, 170, "g", BR)
    E.fracao(c, 2, 3, 1230, y, s, BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_da_sete_oitavos", a), ("capa_B_expressoes_com_fracoes", b), ("capa_C_blocos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
