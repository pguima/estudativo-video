"""Capas do MAT-TOP-003 (1280x720). Uso: python capa.py"""
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


def moeda(c, x, y, r, cara):
    if cara:
        c.drawCircle(x, y, r, M.paint(AMARELO))
        E.centro(c, "cara", x, y + r * 0.13, r * 0.36, "b", COR)
    else:
        c.drawCircle(x, y, r, M.paint(BR, 1, stroke=r * 0.08))
        E.centro(c, "coroa", x, y + r * 0.13, r * 0.32, "b", BR)


def a(c):  # o gancho: 2 caras em 5 não é 2/5
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    for i in range(5):
        moeda(c, 200 + i * 230, 360, 95, i in (0, 2))
    E.fracao(c, 2, 5, 330, 690, 170, BR)
    E.risco(c, 230, 820, 430, 560, 9, 0, AMARELO, 24)
    E.escreve(c, "a chance é", 640, 720, 100, "i", BR)
    E.formula(c, "f{5}{16}", 1220, 770, 200, "g", AMARELO)
    E.escreve(c, "exatamente 2 caras?", 84, 1010, 100, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Distribuição", "binomial", "sem decorar")


def d(c):  # o atalho: linha do triângulo sobre 2^n
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "moeda? o atalho:", 84, 360, 130, "i", BR)
    E.escreve(c, "triângulo ÷ 2ⁿ", 76, 560, 170, "g", BR)
    for i, v in enumerate([1, 5, 10, 10, 5, 1]):
        x = 200 + i * 250
        E.fracao(c, v, 32, x, 830, 120, AMARELO if v == 10 else BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_dois_quintos", a), ("capa_B_distribuicao_binomial", b), ("capa_C_triangulo_sobre_2n", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
