"""Capas do MAT-FUN-024 (1280x720). Uso: python capa.py"""
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


def parabola(c, x0, y0, w, h, cor, larg=12):
    """parábola de boca para baixo na caixa (x0, y0, w, h), com o vértice no alto"""
    p = skia.Path()
    for i in range(101):
        u = i / 100
        x, y = x0 + w * u, y0 + h * (1 - 4 * u * (1 - u))
        p.lineTo(x, y) if i else p.moveTo(x, y)
    c.drawPath(p, M.paint(cor, 1.0, stroke=larg, cap_round=True))


def a(c):  # o gancho: 4 situações para resolver antes da resposta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "4", 84, 560, 380, "g", BR)
    E.escreve(c, "situações:", 400, 400, 120, "i", BR)
    E.escreve(c, "você resolve?", 400, 560, 140, "g", BR)
    E.escreve(c, "função quadrática na prática", 84, 820, 92, "i", BR)
    for i in range(4):
        cx = 1180 + 170 * i
        c.drawCircle(cx, 960, 64, M.paint(BR))
        E.centro(c, str(i + 1), cx, 985, 80, "g", COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Quadrática", "na prática", "4 situações de função")


def d(c):  # o atalho: não abra os parênteses
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "não abra os", 84, 330, 130, "i", claro)
    E.escreve(c, "parênteses", 76, 540, 200, "g", BR)
    E.formula(c, "(20 + x)(200 − 5x)", 84, 760, 110, "g", BR)
    E.escreve(c, "−20 e 40 → meio: 10", 84, 930, 100, "g", AMARELO)
    x, y, w, h = 1340, 380, 460, 420
    M.line(c, x - 30, y + h, x + w + 30, y + h, BR, 1, 6)
    parabola(c, x, y, w, h, claro)
    M.line(c, x + w / 2, y + h, x + w / 2, y - 20, AMARELO, 1, 6, dash=[18, 12])
    for xx in (x, x + w):
        c.drawCircle(xx, y + h, 22, M.paint(AMARELO))
    c.drawCircle(x + w / 2, y, 26, M.paint(AMARELO))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_voce_resolve", a), ("capa_B_funcao_quadratica_na_pratica", b), ("capa_C_nao_abra_os_parenteses", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
