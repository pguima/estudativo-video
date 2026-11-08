"""Capas do MAT-FUN-015 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 4 situações para resolver antes da resposta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "4", 84, 560, 380, "g", BR)
    E.escreve(c, "situações:", 400, 400, 120, "i", BR)
    E.escreve(c, "você resolve?", 400, 560, 140, "g", BR)
    E.escreve(c, "função afim na prática", 84, 820, 100, "i", BR)
    for i in range(4):
        cx = 1180 + 170 * i
        c.drawCircle(cx, 900 - 20, 64, M.paint(BR))
        E.centro(c, str(i + 1), cx, 905, 80, "g", COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Função afim", "na prática", "4 situações")


def d(c):  # o atalho: ande para trás até o x = 0
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "ache o b", 84, 420, 150, "i", claro)
    E.escreve(c, "andando", 76, 640, 210, "g", BR)
    E.escreve(c, "para trás", 84, 850, 170, "i", BR)
    x, y, w, h = 1240, 200, 560, 660
    M.arrow(c, x, y + h, x + w + 30, y + h, BR, 1, 7, 26)
    M.arrow(c, x, y + h, x, y - 30, BR, 1, 7, 26)
    X = lambda v: x + v * w / 5
    Y = lambda v: y + h - v * h / 18
    M.line(c, X(0), Y(1), X(5), Y(16), claro, 1, 12)
    for k in range(2):
        x0, x1 = 2 - k, 1 - k
        M.line(c, X(x0), Y(3 * x0 + 1), X(x1), Y(3 * x0 + 1), AMARELO, 1, 9)
        M.line(c, X(x1), Y(3 * x0 + 1), X(x1), Y(3 * x1 + 1), AMARELO, 1, 9)
    c.drawCircle(X(2), Y(7), 22, M.paint(BR))
    c.drawCircle(X(0), Y(1), 26, M.paint(AMARELO))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_voce_resolve", a), ("capa_B_funcao_afim_na_pratica", b), ("capa_C_ache_o_b_para_tras", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
