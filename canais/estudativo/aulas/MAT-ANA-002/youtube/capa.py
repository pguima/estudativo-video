"""Capas do MAT-ANA-002 (1280x720). Uso: python capa.py"""
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
CIANO = "#3CC7D3"


def par(c, xv, yv, cx, y, size, cor_x=AMARELO, cor_y=BR, cor=BR):
    partes = (("(", cor), (xv, cor_x), (", ", cor), (yv, cor_y), (")", cor))
    w = sum(E.larg(s, "g", size) for s, _ in partes)
    x = cx - w / 2
    for s, k in partes:
        E.escreve(c, s, x, y, size, "g", k)
        x += E.larg(s, "g", size)


def a(c):  # o gancho: o meio de dois pontos, de cabeça
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    A, B = (1180, 900), (1760, 230)
    Mx, My = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    M.line(c, *A, *B, BR, 1, 16)
    for P in (A, B):
        c.drawCircle(*P, 22, M.paint(BR))
    c.drawCircle(Mx, My, 46, M.paint(AMARELO))
    par(c, "2", "4", A[0] - 40, A[1] + 120, 80)
    par(c, "6", "10", B[0] - 40, B[1] - 60, 80)
    E.escreve(c, "o meio?", 84, 470, 210, "g", BR)
    par(c, "4", "7", 420, 740, 200, AMARELO, AMARELO, AMARELO)
    E.escreve(c, "de cabeça", 84, 960, 120, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Ponto", "médio", "e baricentro")


def d(c):  # o atalho: a outra ponta
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a outra ponta:", 84, 370, 140, "i", BR)
    E.escreve(c, "dobre e tire", 76, 560, 170, "g", BR)
    y, xa, xm, xb = 760, 260, 960, 1660
    M.line(c, xa, y, xm, y, BR, 1, 10)
    M.line(c, xm, y, xb, y, CIANO, 1, 10)
    c.drawCircle(xa, y, 26, M.paint(BR)); c.drawCircle(xm, y, 36, M.paint(COR)); c.drawCircle(xm, y, 36, M.paint(BR, 1, stroke=6))
    c.drawCircle(xb, y, 30, M.paint(CIANO))
    par(c, "2", "4", xa + 40, y + 140, 84, BR)
    par(c, "4", "7", xm, y + 140, 84, BR)
    par(c, "6", "10", xb - 40, y + 140, 84, CIANO, CIANO, CIANO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_meio_de_cabeca", a), ("capa_B_ponto_medio", b), ("capa_C_a_outra_ponta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
