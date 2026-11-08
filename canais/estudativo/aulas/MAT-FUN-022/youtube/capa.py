"""Capas do MAT-FUN-022 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF4D55"
VERDE = "#2BD487"


def bolinha(c, cx, cy, s, cor, r=46):
    c.drawCircle(cx, cy, r, M.paint(cor))
    E.centro(c, s, cx, cy + 26, 80, "g", BR)


def a(c):  # o gancho: 2 e 3 não é a resposta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "x^2 − 5x + 6 < 0", 84, 390, 120, "g", BR)
    E.escreve(c, "2 e 3", 84, 620, 150, "g", VERMELHO)
    M.line(c, 70, 640, 520, 500, VERMELHO, 1, 14)
    E.escreve(c, "]2, 3[", 640, 620, 150, "g", AMARELO)
    y, x0, x1 = 860, 200, 1700
    M.arrow(c, x0, y, x1, y, BR, 1, 6, 22)
    X = lambda v: x0 + (v - 0) / 5 * (x1 - x0 - 60)
    for v in range(0, 6):
        M.line(c, X(v), y - 18, X(v), y + 18, BR, 1, 5)
    M.line(c, X(2), y, X(3), y, AMARELO, 1, 16)
    for v in (2, 3):
        c.drawCircle(X(v), y, 20, M.paint(COR)); c.drawCircle(X(v), y, 20, M.paint(AMARELO, 1, stroke=7))
    E.centro(c, "um pedaço da reta", (X(2) + X(3)) / 2, y - 60, 64, "i", AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Inequação", "do 2º grau", "pelo desenho")


def d(c):  # o atalho: fora, sinal do a; entre, o contrário
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "fora: o sinal do a", 84, 400, 110, "g", BR)
    E.escreve(c, "entre: o contrário", 84, 560, 110, "g", AMARELO)
    E.escreve(c, "sem desenhar a parábola", 84, 690, 64, "i", claro)
    y, x0, x1 = 900, 160, 1760
    M.arrow(c, x0, y, x1, y, BR, 1, 6, 22)
    xs = (x0 + (x1 - x0) * 0.38, x0 + (x1 - x0) * 0.62)
    for xv in xs:
        M.line(c, xv, y - 22, xv, y + 22, BR, 1, 6)
    for cx, s, cor in (((x0 + xs[0]) / 2, "+", VERDE), (sum(xs) / 2, "−", VERMELHO), ((xs[1] + x1) / 2, "+", VERDE)):
        bolinha(c, cx, y - 90, s, cor)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_2_e_3_nao_e_a_resposta", a), ("capa_B_inequacao_do_2o_grau", b), ("capa_C_fora_e_entre", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
