"""Capas do MAT-PRO-002 (1280x720). Uso: python capa.py"""
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


def palito(c, x0, y0, x1, y1, cor, w=14, gap=12):
    if x0 == x1:
        M.line(c, x0, y0 + gap, x1, y1 - gap, cor, 1.0, w)
    else:
        M.line(c, x0 + gap, y0, x1 - gap, y1, cor, 1.0, w)


def fileira(c, x, y, n, l, cor, cor_div=None):
    palito(c, x, y, x, y + l, cor)
    for i in range(n):
        x0 = x + i * l
        palito(c, x0, y, x0 + l, y, cor)
        palito(c, x0, y + l, x0 + l, y + l, cor)
        palito(c, x0 + l, y, x0 + l, y + l, (cor_div if i < n - 1 and cor_div else cor))


def a(c):  # o gancho: 50 quadradinhos não é 200 palitos
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    fileira(c, 84, 250, 9, 150, BR, AMARELO)
    E.escreve(c, "50 quadradinhos:", 84, 620, 100, "i", BR)
    E.escreve(c, "200", 84, 900, 210, "g", VERMELHO)
    E.risco(c, 70, 920, 84 + E.larg("200", "g", 210) + 20, 780, 1, 0, AMARELO, 26)
    E.escreve(c, "151", 620, 900, 210, "g", AMARELO)
    E.escreve(c, "palitos", 1090, 890, 110, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Padrões", "em figuras", "a lei dos palitos")


def d(c):  # o atalho: o aumento vira o número do n
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho:", 84, 340, 120, "i", claro)
    E.escreve(c, "4, 7, 10, 13", 76, 570, 160, "g", BR)
    E.escreve(c, "sobe 3", 1140, 570, 150, "i", claro)
    E.escreve(c, "3n + 1", 76, 860, 230, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_151_palitos", a), ("capa_B_padroes_em_figuras", b), ("capa_C_o_aumento", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
