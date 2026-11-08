"""Capas do MAT-TRI-010 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF4D5E"
VERDE = "#3BE38B"
ADJ_ESC = "#3CC7D3"
AMBAR = "#FFB020"


def a(c):  # o gancho: 1 − 3/5 = 2/5 está errado; o certo é 4/5
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "sen x = f{3}{5}", 84, 400, 150, "g", BR)
    E.formula(c, "cos x = ?", 84, 640, 150, "g", AMARELO)
    x0 = 1060
    E.formula(c, "f{2}{5}", x0, 430, 190, "g", BR)
    w = E.formula(None, "f{2}{5}", 0, 0, 190, a=0)
    M.line(c, x0 - 30, 520, x0 + w + 30, 250, VERMELHO, 1.0, 22)
    E.formula(c, "f{4}{5}", 1480, 430, 190, "g", AMARELO)
    E.selo(c, 1720, 330, 56, True)
    E.escreve(c, "o erro de quase todo mundo", 84, 900, 92, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Relação", "fundamental", "da trigonometria")


def d(c):  # o atalho: o triângulo 3-4-5
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 130, "i", BR)
    E.formula(c, "sem conta", 84, 560, 170, "g", BR)
    E.formula(c, "cos x = f{4}{5}", 84, 840, 140, "g", AMARELO)
    K = 130
    A, R, T = (1120, 900), (1120 + 4 * K, 900), (1120 + 4 * K, 900 - 3 * K)
    path = skia.Path(); path.moveTo(*A); path.lineTo(*R); path.lineTo(*T); path.close()
    c.drawPath(path, M.paint(COR, 0.35))
    M.line(c, *A, *R, ADJ_ESC, 1.0, 16)
    M.line(c, *R, *T, AMBAR, 1.0, 16)
    M.line(c, *A, *T, BR, 1.0, 16)
    E.escreve(c, "4", 1120 + 2 * K - 40, 1010, 120, "g", ADJ_ESC)
    E.escreve(c, "3", R[0] + 36, 900 - 1.5 * K + 45, 120, "g", AMBAR)
    E.escreve(c, "5", 1120 + 2 * K - 130, 900 - 1.5 * K - 40, 120, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_erro_2_quintos", a), ("capa_B_relacao_fundamental", b), ("capa_C_triangulo_3_4_5", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
