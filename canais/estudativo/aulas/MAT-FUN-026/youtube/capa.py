"""Capas do MAT-FUN-026 (1280x720). Uso: python capa.py"""
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


def grafico(c, x, y, w, h, cor, alvo=None, eixos=BR):
    """eixos, a curva 30 + 2.000/x (de 0 a 1.050 por 0 a 105) e a assíntota tracejada em 30"""
    X = lambda v: x + v * w / 1050
    Y = lambda v: y + h - v * h / 105
    M.arrow(c, x, y + h, x + w + 30, y + h, eixos, 1, 7, 26)
    M.arrow(c, x, y + h, x, y - 30, eixos, 1, 7, 26)
    p = skia.Path()
    for i in range(301):
        v = 27 + (1050 - 27) * i / 300
        p.lineTo(X(v), Y(30 + 2000 / v)) if i else p.moveTo(X(v), Y(30 + 2000 / v))
    c.drawPath(p, M.paint(cor, 1.0, stroke=12, cap_round=True))
    pt = M.paint(AMARELO, 1.0, stroke=7)
    pt.setPathEffect(skia.DashPathEffect.Make([24, 16], 0))
    c.drawLine(X(0), Y(30), X(1050), Y(30), pt)
    return X, Y


def a(c):  # o gancho: o preço que nunca chega
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "um preço que", 84, 360, 120, "i", BR)
    E.escreve(c, "nunca chega", 76, 560, 180, "g", BR)
    E.escreve(c, "R$ 2.030 → R$ 32 → ?", 84, 820, 96, "g", AMARELO)
    X, Y = grafico(c, 1300, 300, 500, 560, BR)
    E.escreve(c, "30", 1225, Y(30) + 20, 56, "g", AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Custo médio", "e assíntota", "funções racionais")


def d(c):  # o atalho do alvo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho", 84, 360, 130, "i", claro)
    E.escreve(c, "do alvo", 76, 560, 190, "g", BR)
    E.formula(c, "f{2.000}{40 − 30} = 200", 84, 830, 110, "g", AMARELO)
    X, Y = grafico(c, 1300, 300, 500, 560, claro)
    c.drawCircle(X(200), Y(40), 26, M.paint(AMARELO))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_preco_que_nunca_chega", a), ("capa_B_custo_medio", b), ("capa_C_atalho_do_alvo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
