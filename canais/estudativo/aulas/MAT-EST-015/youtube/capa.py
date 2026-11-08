"""Capas do MAT-EST-015 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF5A5A"


def boxplot(c, x0, x1, y, cinco, vmax=10, h=120, cor=BR, fundo=None):
    """caixa e bigodes em branco, na escala de x0 a x1"""
    vx = lambda v: x0 + v / vmax * (x1 - x0)
    mn, q1, q2, q3, mx = cinco
    M.line(c, vx(mn), y, vx(q1), y, cor, 1, 8)
    M.line(c, vx(q3), y, vx(mx), y, cor, 1, 8)
    for v in (mn, mx):
        M.line(c, vx(v), y - h * 0.3, vx(v), y + h * 0.3, cor, 1, 8)
    r = skia.Rect.MakeXYWH(vx(q1), y - h / 2, vx(q3) - vx(q1), h)
    c.drawRect(r, M.paint(fundo or E.mix(COR, "#FFFFFF", 0.35)))
    c.drawRect(r, M.paint(cor, 1, stroke=8))
    M.line(c, vx(q2), y - h / 2, vx(q2), y + h / 2, AMARELO, 1, 12)


def a(c):  # o gancho: a mesma mediana, turmas diferentes
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a mesma mediana", 84, 340, 100, "i", BR)
    E.escreve(c, "e turmas", 84, 520, 150, "g", BR)
    E.escreve(c, "diferentes", 84, 680, 150, "g", AMARELO)
    boxplot(c, 1000, 1840, 470, (4, 5, 6, 7, 8))
    boxplot(c, 1000, 1840, 720, (1, 4, 6, 8, 10))
    E.escreve(c, "manhã", 830, 490, 60, "i", BR)
    E.escreve(c, "noite", 860, 740, 60, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Boxplot e", "amplitude", "de uma olhada")


def d(c):  # o atalho: conte os pedaços
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "sem conta:", 84, 360, 110, "i", BR)
    E.escreve(c, "cada pedaço", 84, 540, 140, "g", BR)
    E.escreve(c, "= 25%", 84, 720, 170, "g", AMARELO)
    x0, x1 = 900, 1840
    boxplot(c, x0, x1, 860, (2, 4, 6, 8, 10), fundo="#2A2A6A")
    for k in range(4):
        cx = x0 + (2 + 2 * k + 1) / 10 * (x1 - x0)
        E.centro(c, "25%", cx, 760, 52, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mesma_mediana_turmas_diferentes", a), ("capa_B_boxplot_e_amplitude", b), ("capa_C_cada_pedaco_25", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
