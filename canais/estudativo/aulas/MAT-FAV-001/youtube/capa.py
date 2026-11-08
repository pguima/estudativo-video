"""Capas do MAT-FAV-001 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def grafico(c, x, y, k, cor, lw=16):
    """o frete: pedaço 2x de 0 a 3 e a reta 9 depois; (x, y) = origem; k = px por unidade"""
    M.arrow(c, x - 20, y, x + 6.6 * k, y, cor, 0.7, 6, 24)
    M.arrow(c, x, y + 20, x, y - 10.6 * k, cor, 0.7, 6, 24)
    M.line(c, x, y, x + 3 * k, y - 6 * k, AMARELO, 1, lw)
    M.line(c, x + 3 * k, y - 9 * k, x + 6.2 * k, y - 9 * k, cor, 1, lw)
    c.drawCircle(x + 3 * k, y - 6 * k, lw * 1.4, M.paint(AMARELO))
    c.drawCircle(x + 3 * k, y - 9 * k, lw * 1.4, M.paint(COR if cor == BR else "#07070F"))
    c.drawCircle(x + 3 * k, y - 9 * k, lw * 1.4, M.paint(cor, 1, stroke=lw * 0.6))


def a(c):  # o gancho: 2 · 5 = 10 está errado
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5 kg:", 84, 390, 150, "i", BR)
    E.escreve(c, "2 · 5 = 10", 84, 600, 190, "g", BR)
    E.risco(c, 60, 640, 1000, 420, 9, 0, AMARELO, 34)
    E.escreve(c, "a regra mudou", 84, 830, 120, "i", BR)
    grafico(c, 1220, 930, 78, BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Função", "por partes", "sem confusão")


def d(c):  # o atalho: calcule as duas leis na fronteira
    palco(c)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "na fronteira,", 84, 380, 140, "i", BR)
    E.escreve(c, "duas leis", 76, 590, 200, "g", BR)
    E.escreve(c, "6 ≠ 9: salto", 84, 820, 130, "g", AMARELO)
    grafico(c, 1260, 950, 80, BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_regra_mudou", a), ("capa_B_funcao_por_partes", b), ("capa_C_duas_leis_na_fronteira", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
