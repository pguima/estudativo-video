"""Capas do MAT-ANA-001 (1280x720). Uso: python capa.py"""
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
DX, DY = "#3CC7D3", "#FFB833"  # corredor e elevador, claros sobre o índigo


def tri(c, x0, y0, k, lw=16):
    """triângulo 3-4-5 com o canto reto embaixo à direita; (x0, y0) = vértice de baixo à esquerda; k = px por unidade"""
    A, R, T = (x0, y0), (x0 + 3 * k, y0), (x0 + 3 * k, y0 - 4 * k)
    p = skia.Path(); p.addPoly([A, R, T], True)
    c.drawPath(p, M.paint(BR, 0.12))
    M.line(c, *A, *R, DX, 1, lw); M.line(c, *R, *T, DY, 1, lw); M.line(c, *A, *T, BR, 1, lw)
    s = 0.22 * k
    M.line(c, R[0] - s, R[1], R[0] - s, R[1] - s, BR, 1, 6); M.line(c, R[0] - s, R[1] - s, R[0], R[1] - s, BR, 1, 6)
    for P in (A, T):
        c.drawCircle(*P, lw * 1.3, M.paint(BR))
    return A, R, T


def a(c):  # o gancho: 3 + 4 não é a distância
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    A, R, T = tri(c, 1180, 900, 150)
    E.centro(c, "3", (A[0] + R[0]) / 2, R[1] + 120, 110, "g", DX)
    E.escreve(c, "4", R[0] + 40, (R[1] + T[1]) / 2 + 40, 110, "g", DY)
    E.escreve(c, "?", 1250, 620, 150, "g", BR)
    E.escreve(c, "3 + 4 = 7", 84, 520, 190, "g", BR)
    E.risco(c, 60, 560, 900, 330, 9, 0, AMARELO, 34)
    E.escreve(c, "a distância é outra", 84, 800, 110, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Distância", "no plano", "sem decorar")


def d(c):  # o atalho: conte os passos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "fuja do sinal:", 84, 380, 140, "i", BR)
    E.escreve(c, "conte os passos", 76, 570, 170, "g", BR)
    y, x0, u = 860, 260, 190
    vx = lambda v: x0 + (v + 3) * u
    M.arrow(c, x0 - 40, y, vx(5) + 60, y, BR, 1, 6, 24)
    for v in range(-3, 6):
        M.line(c, vx(v), y - 18, vx(v), y + 18, BR, 1, 5)
        E.centro(c, E._num(v), vx(v), y + 80, 54, "b", BR)
    for v0, v1, s, alto in ((-2, 0, "2", 120), (0, 4, "4", 170)):
        n = 40
        pts = [(vx(v0) + (vx(v1) - vx(v0)) * i / n, y - alto * __import__("math").sin(3.14159 * i / n)) for i in range(n + 1)]
        for p0, p1 in zip(pts, pts[1:]):
            M.line(c, *p0, *p1, DX, 1, 9)
        E.centro(c, s, (vx(v0) + vx(v1)) / 2, y - alto - 24, 70, "g", DX)
    for v in (-2, 4):
        c.drawCircle(vx(v), y, 20, M.paint(DX))
    E.escreve(c, "= 6", 1650, 770, 130, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_7", a), ("capa_B_distancia_no_plano", b), ("capa_C_conte_os_passos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
