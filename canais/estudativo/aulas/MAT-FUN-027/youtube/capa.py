"""Capas do MAT-FUN-027 (1280x720). Uso: python capa.py"""
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
ERRO = "#FF5A5A"


def tabela(c, x, y, linhas, wc=170, hl=104, size=72):
    """tabela x | y | x · y em branco, com o último produto destacado"""
    for j, s in enumerate(("x", "y", "x · y")):
        E.centro(c, s, x + wc * j + wc / 2, y - 26, 56, "g", BR)
    M.line(c, x, y, x + 3 * wc, y, BR, 1, 5)
    for j in (1, 2):
        M.line(c, x + wc * j, y, x + wc * j, y + hl * len(linhas) + 10, BR, 1, 5)
    for i, (a, b, p, cor) in enumerate(linhas):
        ry = y + 10 + hl * i + hl / 2 + size * 0.36
        E.centro(c, a, x + wc / 2, ry, size, "g", BR)
        E.centro(c, b, x + wc * 1.5, ry, size, "g", BR)
        E.centro(c, p, x + wc * 2.5, ry, size, "g", cor)


def a(c):  # o gancho: só a última linha denuncia
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "é do tipo k/x?", 84, 360, 120, "i", BR)
    E.escreve(c, "confira", 76, 560, 190, "g", BR)
    E.escreve(c, "todas as linhas", 84, 760, 120, "g", AMARELO)
    tabela(c, 1250, 330, (("1", "30", "30", BR), ("2", "15", "30", BR), ("3", "10", "30", BR), ("4", "6", "24", ERRO)))
    c.drawCircle(1250 + 170 * 2.5, 330 + 10 + 104 * 3 + 52, 70, M.paint(ERRO, 1, stroke=8))


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Função k/x", "na prática", "4 situações")


def d(c):  # o atalho: a hipérbole nunca toca os eixos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "tocou o eixo?", 84, 400, 130, "i", claro)
    E.escreve(c, "não é k/x", 76, 620, 190, "g", BR)
    E.escreve(c, "sem conta", 84, 820, 120, "g", AMARELO)
    x, y, w, h = 1300, 300, 500, 560
    M.arrow(c, x, y + h, x + w + 30, y + h, BR, 1, 7, 26)
    M.arrow(c, x, y + h, x, y - 30, BR, 1, 7, 26)
    p = skia.Path()
    for i in range(201):
        u = 0.07 + 0.93 * i / 200
        X, Y = x + u * w, y + h - (0.08 / u) * h
        p.lineTo(X, Y) if i else p.moveTo(X, Y)
    c.drawPath(p, M.paint(claro, 1.0, stroke=12, cap_round=True))
    M.line(c, x, y + 60, x + w * 0.9, y + h, ERRO, 1, 9)
    for X, Y in ((x, y + 60), (x + w * 0.9, y + h)):
        c.drawCircle(X, Y, 26, M.paint(ERRO, 1, stroke=7))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_confira_todas_as_linhas", a), ("capa_B_funcao_k_sobre_x_na_pratica", b), ("capa_C_tocou_o_eixo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
