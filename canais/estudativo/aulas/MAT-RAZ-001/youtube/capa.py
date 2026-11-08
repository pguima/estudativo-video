"""Capas do MAT-RAZ-001 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o erro: 50 cm ÷ 2 m = 25?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "50 cm ÷ 2 m", 84, 400, 180, "g", BR)
    w = E.larg("= 25", "g", 260)
    E.escreve(c, "= 25", 84, 700, 260, "g", BR)
    E.risco(c, 60, 730, 84 + w + 30, 500, 9, 0, "#FFD500", 36)
    E.escreve(c, "25 vezes o quê?", 84, 950, 130, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "O que é", "razão", "do zero")


def d(c):  # o atalho: corte os zeros
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho:", 84, 340, 140, "i", BR)
    E.escreve(c, "corte os zeros", 76, 540, 180, "g", BR)
    E.fracao(c, 50, 200, 330, 790, 170, BR)
    for x0, y0 in ((372, 740), (440, 920)):
        M.line(c, x0 - 40, y0 + 10, x0 + 40, y0 - 120, "#FFD500", 1, 14)
    E.escreve(c, "→", 590, 860, 170, "g", E.mix(COR, BR, 0.55))
    E.fracao(c, 5, 20, 950, 790, 170, BR)
    E.escreve(c, "= 1/4", 1170, 860, 170, "g", E.mix(COR, BR, 0.55))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_25_vezes_o_que", a), ("capa_B_o_que_e_razao", b), ("capa_C_corte_os_zeros", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
