"""Capas do MAT-EST-019 (1280x720). Uso: python capa.py"""
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


def anuncio(c, x, y, w, h):
    """as colunas de 50 e 55 com o eixo começando em 45: B parece o dobro"""
    vy = lambda v: y + h - (v - 45) / 10 * h
    M.line(c, x, y + h, x, y - 20, BR, 1, 6)
    M.line(c, x - 10, y + h, x + w, y + h, BR, 1, 6)
    for v in (45, 50, 55):
        E.escreve(c, str(v), x - 30 - E.larg(str(v), "b", 56), vy(v) + 20, 56, "b", BR)
    for i, (rot, v, cor) in enumerate((("A", 50, E.mix(BR, COR, 0.3)), ("B", 55, AMARELO))):
        cx = x + w * (i + 0.5) / 2
        M.rrect(c, cx - 90, vy(v), 180, y + h - vy(v), 12, cor, 1.0)
        E.centro(c, rot, cx, y + h + 80, 64, "g", BR)
        E.centro(c, str(v), cx, vy(v) - 24, 70, "g", cor)
    E.arco(c, x - 60, y + h - 4, 56, -90, 360, VERMELHO, 8)


def a(c):  # o gancho: parece o dobro, é 10%
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "parece o dobro", 84, 340, 100, "i", BR)
    E.escreve(c, "é só", 84, 560, 150, "g", BR)
    E.escreve(c, "10%", 84, 790, 230, "g", AMARELO)
    anuncio(c, 1160, 260, 600, 600)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Gráficos", "que enganam", "3 truques para pegar")


def d(c):  # o atalho: 3 olhares
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 olhares", 84, 360, 150, "g", AMARELO)
    E.escreve(c, "antes de acreditar", 860, 360, 90, "i", BR)
    for i, s in enumerate(("eixo começa no zero?", "mesmo espaço, mesmo passo?", "figura cresceu num sentido só?")):
        y = 560 + i * 160
        E.bola(c, 150, y - 34, 52, COR)
        E.centro(c, str(i + 1), 150, y - 12, 64, "g", BR)
        E.escreve(c, s, 240, y, 92, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_parece_o_dobro", a), ("capa_B_graficos_que_enganam", b), ("capa_C_tres_olhares", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
