"""Capas do MAT-FRA-009 (1280x720). Uso: python capa.py"""
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
CLARO = E.mix(COR, BR, 0.5)


def a(c):  # o gancho: multiplicou e diminuiu
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.fracao(c, 1, 2, 240, 530, 270, BR)
    E.escreve(c, "×", 410, 610, 230, "g", BR)
    E.fracao(c, 1, 4, 730, 530, 270, BR)
    E.escreve(c, "=", 900, 610, 230, "g", BR)
    E.fracao(c, 1, 8, 1240, 530, 270, AMARELO)
    E.escreve(c, "?", 1430, 640, 320, "g", BR)
    E.escreve(c, "multiplicou e diminuiu", 84, 985, 136, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Multiplicar", "frações", "de vira vezes")


def d(c):  # o atalho: cortar em cruz
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "cortar", 84, 370, 170, "g", BR)
    E.escreve(c, "em cruz", 610, 370, 190, "i", BR)
    s, xa, xb, y = 250, 300, 800, 690
    E.fracao(c, 4, 9, xa, y, s, BR); E.fracao(c, 3, 8, xb, y, s, BR)
    for x0, y0, x1, y1 in ((xa - 95, y - 40, xa + 95, y - 240), (xb - 95, y + 240, xb + 95, y + 40), (xb - 95, y - 40, xb + 95, y - 240), (xa - 95, y + 240, xa + 95, y + 40)):
        M.line(c, x0, y0, x1, y1, AMARELO, 1, 16)
    E.escreve(c, "×", 500, y + 65, 170, "g", BR)
    E.escreve(c, "= 1/6", 1090, y + 80, 230, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_multiplicou_diminuiu", a), ("capa_B_multiplicar_fracoes", b), ("capa_C_cortar_em_cruz", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
