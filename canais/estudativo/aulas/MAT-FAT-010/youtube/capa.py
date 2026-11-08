"""Capas do MAT-FAT-010 (1280x720). Uso: python capa.py"""
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


def fra(c, cima, baixo, cx, y, size, cor):
    w = max(E.formula(None, cima, 0, 0, size, a=0), E.formula(None, baixo, 0, 0, size, a=0)) + size * 0.3
    E.formula(c, cima, cx, y - size * 0.32, size, cor=cor, align="center")
    b = size * 0.07
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y - b / 2, w, b), b / 2, b / 2), M.paint(cor))
    E.formula(c, baixo, cx, y + size * 0.98, size, cor=cor, align="center")
    return w


def a(c):  # o gancho: a resposta com raiz
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "x(x − 2) = 1", 84, 470, 210, cor=BR)
    E.formula(c, "x = 1 ± r{2}", 84, 760, 190, cor=AMARELO)
    E.escreve(c, "e não tem nada de errado", 84, 990, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Raiz não", "exata", "em Bhaskara")


def d(c):  # o atalho: separe a fração em duas
    palco(c)
    E.escreve(c, "separe a fração em duas", 84, 330, 110, "i", BR)
    w = fra(c, "2 ± 2r{2}", "2", 300, 640, 120, BR)
    E.formula(c, "=", 300 + w / 2 + 30, 680, 120, cor=BR)
    x1 = 300 + w / 2 + 170
    w1 = fra(c, "2", "2", x1 + 40, 640, 120, AMARELO)
    E.formula(c, "±", x1 + 40 + w1 / 2 + 20, 680, 120, cor=BR)
    w2 = fra(c, "2r{2}", "2", x1 + 40 + w1 / 2 + 140 + 130, 640, 120, AMARELO)
    E.formula(c, "= 1 ± r{2}", 84, 990, 140, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_resposta_com_raiz", a), ("capa_B_raiz_nao_exata", b), ("capa_C_separe_a_fracao", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
