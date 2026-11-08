"""Capas do MAT-RAZ-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: x/6 = 4/3, quanto vale x?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.fracao(c, "x", 6, 300, 520, 260, AMARELO)
    E.escreve(c, "=", 470, 620, 230, "g", BR)
    E.fracao(c, 4, 3, 820, 520, 260, BR)
    E.escreve(c, "x = ?", 1100, 620, 200, "g", AMARELO)
    E.escreve(c, "sai em 1 multiplicação", 84, 1000, 110, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Proporção:", "ache o x", "do zero")


def d(c):  # o atalho: procure o fator
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho:", 84, 340, 140, "i", BR)
    E.escreve(c, "procure o fator", 76, 540, 180, "g", BR)
    cl = E.mix(COR, BR, 0.55)
    E.fracao(c, 8, 6, 330, 790, 170, BR)
    E.escreve(c, "=", 470, 860, 150, "g", BR)
    E.fracao(c, 4, 3, 760, 790, 170, BR)
    E.pilula(c, "× 2", 1180, 820, 110, "g", fundo=cl, cor="#07070F")
    E.escreve(c, "sem equação", 1360, 860, 90, "i", cl)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quanto_vale_x", a), ("capa_B_proporcao_ache_o_x", b), ("capa_C_procure_o_fator", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
