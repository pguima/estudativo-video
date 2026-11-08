"""Capas do MAT-TRI-002 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AM = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]
OPO = "#FFB020"


def escada(c, A, T, cor):
    ux, uy = E._uni(*A, *T); nx, ny = -uy, ux
    L = math.dist(A, T)
    for s in (-16, 16):
        M.line(c, A[0] + nx * s, A[1] + ny * s, T[0] + nx * s, T[1] + ny * s, cor, 1.0, 9)
    k = 34
    while k < L - 10:
        P = (A[0] + ux * k, A[1] + uy * k)
        M.line(c, P[0] - nx * 16, P[1] - ny * 16, P[0] + nx * 16, P[1] + ny * 16, cor, 1.0, 6)
        k += 54


def cena(c, x0, y0, k, alt="?"):
    A, R = (x0, y0), (x0 + 8 * k, y0)
    T = (R[0], y0 - 6 * k)
    M.line(c, x0 - 60, y0, R[0] + 80, y0, BR, 0.8, 6)
    M.rrect(c, R[0], T[1] - 120, 50, y0 - T[1] + 120, 4, "#0A0820", 0.8)
    M.line(c, *R, *T, OPO, 1.0, 14)
    escada(c, A, T, BR)
    c.drawArc(skia.Rect.MakeXYWH(A[0] - 130, A[1] - 130, 260, 260), -36.87, 36.87, True, M.paint(BR, 0.25))
    E.escreve(c, "37°", A[0] + 150, A[1] - 30, 60, "g", BR)
    E.escreve(c, "10 m", (A[0] + T[0]) / 2 - 170, (A[1] + T[1]) / 2 - 20, 64, "g", BR)
    E.escreve(c, alt, R[0] + 70, (R[1] + T[1]) / 2 + 30, 110, "g", OPO)


def a(c):  # o gancho: a escada
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a que altura", 84, 330, 130, "g", BR)
    E.escreve(c, "ela toca a parede?", 84, 470, 100, "i", BR)
    cena(c, 900, 960, 80)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Achar", "o lado", "com sen, cos e tg")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "sem montar equação", 84, 330, 120, "i", BR)
    E.escreve(c, "oposto", 84, 560, 130, "g", OPO)
    E.escreve(c, "= hip · sen", 84 + E.larg("oposto ", "g", 130), 560, 130, "g", BR)
    E.escreve(c, "10 · 0,6 = 6", 84, 800, 150, "g", AM)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_que_altura", a), ("capa_B_achar_o_lado", b), ("capa_C_sem_equacao", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
