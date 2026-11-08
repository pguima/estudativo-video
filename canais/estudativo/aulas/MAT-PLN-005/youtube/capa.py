"""Capas do MAT-PLN-005 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)



def curva(c, x0, y0, w, h, cor, largura=12):
    """y = (x − 1)²(x + 2) de −2,5 a 2,2 na caixa; devolve a função valor → pixel"""
    f = lambda x: (x - 1) ** 2 * (x + 2)
    px = lambda x: x0 + (x + 3) / 5.5 * w
    py = lambda y: y0 + h / 2 - y / 14 * h
    M.line(c, x0, y0 + h / 2, x0 + w, y0 + h / 2, BR, 0.85, 6)
    M.line(c, px(0), y0, px(0), y0 + h, BR, 0.85, 6)
    p = skia.Path()
    xs = [-2.5 + i * 4.7 / 200 for i in range(201)]
    p.moveTo(px(xs[0]), py(f(xs[0])))
    for x in xs[1:]:
        p.lineTo(px(x), py(f(x)))
    c.drawPath(p, M.paint(cor, 1, stroke=largura, cap_round=True))
    return px, py


def a(c):  # o gancho: corta em −2, encosta em 1
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    px, py = curva(c, 900, 150, 900, 860, AMARELO)
    for x, rot in ((-2, "corta"), (1, "toca")):
        c.drawCircle(px(x), py(0), 26, M.paint(BR))
        E.centro(c, rot, px(x), py(0) + 110, 80, "g", BR)
    E.escreve(c, "corta ou", 84, 420, 150, "i", BR)
    E.escreve(c, "só toca?", 84, 580, 150, "g", BR)
    E.formula(c, "(x − 1)^2(x + 2)", 84, 840, 110, cor=AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Raiz", "dupla", "gráfico e sinal")


def d(c):  # o atalho: ímpar troca, par mantém
    palco(c)
    E.escreve(c, "o atalho do sinal", 84, 330, 120, "i", BR)
    E.escreve(c, "ímpar: troca", 84, 560, 150, "g", AMARELO)
    E.escreve(c, "par: mantém", 84, 760, 150, "g", BR)
    for k, (s_, cor) in enumerate((("−", "#5A5A70"), ("+", COR), ("+", COR))):
        E.bola(c, 1300 + 200 * k, 900, 70, cor)
        E.centro(c, s_, 1300 + 200 * k, 930, 90, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_corta_ou_toca", a), ("capa_B_raiz_dupla", b), ("capa_C_atalho_sinal", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
