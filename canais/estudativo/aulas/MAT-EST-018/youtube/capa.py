"""Capas do MAT-EST-018 (1280x720). Uso: python capa.py"""
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


def ficha(c, s, cx, cy, size, fundo=BR, tinta=None):
    w = E.larg(s, "b", size) + size * 1.1
    h = size * 1.55
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(fundo))
    E.centro(c, s, cx, cy + size * 0.36, size, "b", tinta or COR)
    return w


def a(c):  # o gancho: média 30, mas o tempo típico é 20
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    x = 90
    for v in (10, 15, 15, 15, 20, 25, 30, 35, 105):
        s = str(v)
        w = E.larg(s, "b", 64) + 64 * 1.1
        ficha(c, s, x + w / 2, 300, 64, AMARELO if v == 20 else (VERMELHO if v == 105 else BR), COR if v != 105 else BR)
        x += w + 22
    E.escreve(c, "média 30?", 90, 560, 140, "g", BR)
    E.escreve(c, "o típico é 20", 90, 750, 140, "g", AMARELO)
    E.escreve(c, "5 situações para resolver", 90, 900, 80, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Média, mediana", "e dispersão", "praticando")


def d(c):  # o atalho: qual medida usar
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "qual medida usar?", 84, 330, 110, "i", BR)
    for i, (l, r) in enumerate((("valor extremo", "mediana"), ("mesma média", "DP"), ("médias diferentes", "DP ÷ média"))):
        y = 520 + i * 170
        E.escreve(c, l, 84, y, 96, "g", BR)
        E.escreve(c, "→ " + r, 1080, y, 96, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_tipico_e_20", a), ("capa_B_praticando_medidas", b), ("capa_C_qual_medida_usar", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
