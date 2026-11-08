"""Capas do MAT-PRO-010 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AM = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: R$ 1 dobrando por 10 dias
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "R$ 1, dobrando", 84, 360, 140, "g", BR)
    E.escreve(c, "por 10 dias", 84, 510, 120, "i", BR)
    E.escreve(c, "1 + 2 + 4 + … + 512", 84, 700, 96, "b", E.mix(COR, BR, 0.6))
    E.escreve(c, "= 1.023", 84, 960, 230, "g", AM)
    for i in range(10):  # as dez colunas que dobram
        h = max(8, 2 ** i / 512 * 640)
        M.rrect(c, 1150 + i * 68, 1000 - h, 48, h, 8, BR if i == 9 else E.mix(COR, BR, 0.55), 1.0)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Soma", "da PG", "numa conta só")


def d(c):  # o atalho: próximo menos primeiro
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "somar a PG", 84, 330, 140, "i", BR)
    E.escreve(c, "sem somar", 76, 520, 190, "g", BR)
    E.formula(c, "S = f{próximo − primeiro}{q − 1}", 84, 860, 120, "g", BR)
    E.escreve(c, "atalho", 1380, 880, 120, "i", AM)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dobrando_10_dias", a), ("capa_B_soma_da_pg", b), ("capa_C_proximo_menos_primeiro", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
