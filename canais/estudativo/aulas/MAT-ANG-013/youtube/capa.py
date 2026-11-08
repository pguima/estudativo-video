"""Capas do MAT-ANG-013 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
LILAS = "#C9C9FF"


def sol(c, x, y, r):
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(x, y), r * 2.6, [M.hexc(AMARELO, 0.5), M.hexc(AMARELO, 0.0)], [0, 1]))
    c.drawCircle(x, y, r * 2.6, p)
    c.drawCircle(x, y, r, M.paint(AMARELO))


def cena(c, chao=930):
    """poste de 2 com sombra 3 e prédio de 20 com sombra 30, raios paralelos"""
    M.line(c, 40, chao, 1200, chao, BR, 0.6, 6)
    P0, PT, PS = (110, chao), (110, chao - 160), (110 + 240, chao)
    Q0, QT, QS = (500, chao), (500, chao - 480), (500 + 720, chao)
    for B, T, S in ((P0, PT, PS), (Q0, QT, QS)):
        M.line(c, *B, *S, "#0B0B30", 0.45, 22)
        ux, uy = (T[0] - S[0]), (T[1] - S[1])
        n = math.hypot(ux, uy)
        M.line(c, T[0] + ux / n * 120, T[1] + uy / n * 120, *S, AMARELO, 1, 8, dash=[20, 14])
    M.line(c, *P0, *PT, BR, 1, 14)
    c.drawRect(skia.Rect.MakeXYWH(Q0[0] - 130, QT[1], 130, chao - QT[1]), M.paint("#DAD8F2"))
    for i in range(9):
        for j in range(2):
            c.drawRect(skia.Rect.MakeXYWH(Q0[0] - 105 + j * 55, chao - 60 - i * 50, 30, 30), M.paint(COR, 0.55))
    return P0, PT, PS, Q0, QT, QS


def a(c):  # o gancho: a altura do prédio pela sombra
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    sol(c, 640, 260, 55)
    P0, PT, PS, Q0, QT, QS = cena(c)
    E.escreve(c, "2", 20, 870, 80, "g", LILAS)
    E.escreve(c, "3", 210, 1040, 90, "g", AMARELO)
    E.escreve(c, "30 m", 760, 1040, 100, "g", AMARELO)
    E.escreve(c, "?", 290, 640, 200, "g", BR)
    E.escreve(c, "altura", 1240, 560, 140, "i", BR)
    E.escreve(c, "pela", 1240, 700, 140, "i", BR)
    E.escreve(c, "sombra", 1240, 880, 170, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Sombras e", "semelhança", "triângulos encaixados")


def d(c):  # o atalho: a razão da hora
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "razão", 110, 420, 190, "g", BR)
    E.escreve(c, "da hora", 110, 600, 170, "i", claro)
    E.formula(c, "altura = f{2}{3} da sombra", 110, 830, 100, "g", AMARELO)
    E.escreve(c, "30 → 20", 1180, 500, 150, "g", BR)
    E.escreve(c, "12 → 8", 1180, 700, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_altura_pela_sombra", a), ("capa_B_sombras_e_semelhanca", b), ("capa_C_razao_da_hora", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
