"""Capas do MAT-EQU-013 (1280x720). Uso: python capa.py"""
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


def caixa_q(c, cx, cy, s, cor):
    p = M.paint(cor, 1, stroke=8)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), 22, 22), p)
    E.centro(c, "?", cx, cy + s * 0.22, s * 0.62, "g", cor)


def a(c):  # o gancho: ? + ? + ? = 84
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 números seguidos", 84, 360, 130, "i", BR)
    for cx in (200, 560, 920):
        caixa_q(c, cx, 590, 210, BR)
    for cx in (380, 740):
        E.centro(c, "+", cx, 640, 150, "g", BR)
    E.formula(c, "= 84", 1080, 650, 200, cor=AMARELO)
    E.escreve(c, "quais são?", 84, 960, 150, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Problema", "vira equação", "em 4 passos")


def d(c):  # o macete: soma ÷ 3 = o do meio
    palco(c)
    E.escreve(c, "o atalho", 84, 360, 150, "i", BR)
    E.formula(c, "84 ÷ 3 = 28", 84, 600, 220, cor=AMARELO)
    E.escreve(c, "o do meio", 84, 800, 170, "g", BR)
    E.escreve(c, "27, 28 e 29", 84, 980, 140, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quais_sao", a), ("capa_B_problema_vira_equacao", b), ("capa_C_o_do_meio", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
