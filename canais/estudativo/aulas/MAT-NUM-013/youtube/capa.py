"""Capas do MAT-NUM-013 (1280x720). Uso: python capa.py"""
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


def fundo_escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: 14 ou 20?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "2 + 3 × 4", 84, 470, 270, "g", BR)
    E.escreve(c, "14", 84, 830, 300, "g", AMARELO)
    E.escreve(c, "ou", 560, 800, 170, "i", BR)
    E.escreve(c, "20?", 830, 830, 300, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Ordem das", "operações", "e parênteses")


def d(c):  # o atalho: os blocos
    fundo_escuro(c)
    E.escreve(c, "o atalho", 84, 340, 150, "i", BR)
    E.escreve(c, "dos blocos", 80, 590, 270, "g", BR)
    E.escreve(c, "6 × 5 − 8 ÷ 2 + 1", 84, 800, 130, "g", CLARO)
    E.escreve(c, "= 27", 84, 980, 170, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_14_ou_20", a), ("capa_B_ordem_operacoes", b), ("capa_C_blocos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
