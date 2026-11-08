"""Capas do MAT-EQU-006 (1280x720). Uso: python capa.py"""
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
    E.capa_rotulo(c, "Matemática", COR)




def a(c):  # o gancho: a sala de lado 3x
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "área da sala?", 84, 380, 170, "g", BR)
    x0, y0, l = 1400, 250, 400
    M.rrect(c, x0, y0, l, l, 12, M.mix(COR, BR, 0.25), 1)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y0, l, l), 12, 12), M.paint(BR, 1, stroke=8))
    E.formula(c, "3x", x0 + l / 2, y0 - 30, 90, cor=BR, align="center")
    E.formula(c, "3x", x0 - 30, y0 + l / 2 + 30, 90, cor=BR, align="right")
    for x, s in ((84, "6x"), (440, "9x")):
        E.formula(c, s, x, 680, 170, cor=BR)
        E.risco(c, x - 20, 700, x + 260, 560, 9, 0, BR, 20)
    E.formula(c, "9x^2", 790, 690, 200, cor=AMARELO)
    E.escreve(c, "5 situações para praticar", 84, 950, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "expressões", "5 situações com letra")


def d(c):  # o atalho: o teste do zero
    palco(c)
    E.escreve(c, "o atalho", 84, 330, 150, "i", BR)
    E.escreve(c, "teste do zero", 76, 560, 200, "g", BR)
    E.formula(c, "x = 0 → sobra o número solto", 84, 820, 100, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_area_da_sala", a), ("capa_B_praticando_expressoes", b), ("capa_C_teste_do_zero", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
