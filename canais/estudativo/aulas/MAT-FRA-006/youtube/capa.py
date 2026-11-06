"""Capas do MAT-FRA-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a pegadinha da menor entrada
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.fracao(c, 2, 5, 400, 490, 270, BR)
    E.escreve(c, "ou", 680, 580, 170, "i", BR)
    E.fracao(c, 3, 8, 1060, 490, 270, AMARELO)
    E.escreve(c, "?", 1260, 610, 300, "g", BR)
    E.escreve(c, "qual entrada é menor?", 84, 980, 150, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "frações", "no dia a dia")


def d(c):  # o atalho: tire o pedaço que falta
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "tire o pedaço", 84, 370, 170, "i", BR)
    E.escreve(c, "que falta", 84, 565, 170, "g", BR)
    x, y, w, h = 84, 630, 1560, 140
    E.barra_fatias(c, x, y, w, h, 6, 5, E.mix(COR, BR, 0.5))
    E.escreve(c, "240 − 40 =", 84, 950, 170, "g", BR)
    E.escreve(c, "200", 1030, 955, 200, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_menor_entrada", a), ("capa_B_praticando_fracoes", b), ("capa_C_pedaco_que_falta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
