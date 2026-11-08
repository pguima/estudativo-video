"""Capas do MAT-EQU-003 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: 3x + 2 não é 5x
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3x + 2 =", 84, 560, 260, "g", BR)
    E.escreve(c, "5x?", 1240, 560, 260, "g", AMARELO)
    E.risco(c, 1220, 600, 1720, 360, 9, 0, BR, 30)
    E.escreve(c, "um número prova o erro", 84, 900, 130, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Termos", "semelhantes", "do jeito certo")


def d(c):  # o atalho: circule e sublinhe
    palco(c)
    E.escreve(c, "o atalho", 84, 330, 150, "i", BR)
    E.escreve(c, "circule e sublinhe", 76, 540, 150, "g", BR)
    L, y, s = "5x + 6 − 2x + 1", 860, 170
    E.formula(c, L, 130, y, s, cor=BR)
    for tr in ("5x", "− 2x"):
        i0 = L.find(tr)
        x0 = 130 + E.formula(None, L[:i0], 0, 0, s, a=0)
        w = E.formula(None, tr, 0, 0, s, a=0)
        c.drawOval(skia.Rect.MakeXYWH(x0 - 30, y - 170, w + 50, 210), M.paint(AMARELO, 1, stroke=9))
    for tr in ("+ 6", "+ 1"):
        i0 = L.find(tr)
        x0 = 130 + E.formula(None, L[:i0], 0, 0, s, a=0)
        w = E.formula(None, tr, 0, 0, s, a=0)
        M.line(c, x0, y + 45, x0 + w - 10, y + 45, AMARELO, 1, 12)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_3x_mais_2_nao_e_5x", a), ("capa_B_termos_semelhantes", b), ("capa_C_circule_e_sublinhe", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
