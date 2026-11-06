"""Capas do MAT-FRA-004 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
CLARO = E.mix(COR, BR, 0.5)
AMARELO = "#FFD500"


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: uma barra tem 3 pedaços. Como comer 7/3?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.fracao(c, 7, 3, 290, 540, 340, AMARELO)
    x, w, h = 680, 1100, 170
    for i in range(3):
        y = 230 + i * 215
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), M.paint(BR))
        for j in range(3):
            if i * 3 + j < 7:
                E.tablete(c, x + j * w / 3, y, w / 3, h, AMARELO)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), M.paint("#11151B", stroke=4))
    E.escreve(c, "como assim, 7/3?", 84, 1000, 130, "i", BR)


def b(c):  # o método
    E.capa_modelo(c, "Matemática", "Número", "misto", "e fração imprópria")


def d(c):  # o atalho: a tabuada do de baixo
    palco(c)
    E.escreve(c, "sem armar", 84, 350, 150, "i", BR)
    E.escreve(c, "a conta", 76, 570, 240, "g", BR)
    y = 790
    E.fracao(c, 23, 4, 300, y, 170, BR)
    E.escreve(c, "=", 480, y + 54, 150, "g", BR)
    E.escreve(c, "5", 620, y + 100, 300, "g", AMARELO)
    E.fracao(c, 3, 4, 900, y, 170, AMARELO)
    E.escreve(c, "4 × 5 = 20", 1090, y + 50, 130, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sete_tercos", a), ("capa_B_numero_misto", b), ("capa_C_tabuada_do_de_baixo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
