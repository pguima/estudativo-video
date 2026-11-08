"""Capas do MAT-PRO-005 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a armadilha do +1
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "múltiplos de 7", 84, 380, 150, "g", BR)
    E.escreve(c, "com 3 algarismos?", 84, 540, 120, "i", BR)
    E.escreve(c, "127", 120, 880, 230, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 110, 900, 560, 690, 9, 0, AM, 30)
    E.escreve(c, "128", 760, 880, 260, "g", AM)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Atalhos", "da PA", "meio e contagem")


def d(c):  # o atalho: a frase de contar termos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "contar termos", 84, 330, 140, "i", BR)
    E.escreve(c, "sem listar", 76, 520, 190, "g", BR)
    E.formula(c, "f{último − primeiro}{razão}", 84, 840, 120, "g", BR)
    E.escreve(c, "+ 1", 900, 860, 170, "g", AM)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_armadilha_do_mais_um", a), ("capa_B_atalhos_da_pa", b), ("capa_C_contar_termos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
