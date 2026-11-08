"""Capas do MAT-CNT-004 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: 8!/6! de cabeça
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "f{8!}{6!}", 360, 640, 330, "g", BR, align="center")
    E.escreve(c, "=", 650, 700, 220, "g", BR)
    E.bola(c, 1080, 620, 230, "#FFFFFF")
    E.centro(c, "56", 1080, 620 + 76, 210, "g", COR)
    E.escreve(c, "de cabeça", 1360, 560, 130, "i", AMARELO)
    E.escreve(c, "em 1 linha", 1360, 720, 130, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Fatorial", "sem medo", "e a conta que corta")


def d(c):  # o atalho: a diferença diz quantos sobram
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "f{10!}{7!}", 330, 600, 260, "g", BR, align="center")
    E.escreve(c, "= 10 × 9 × 8", 560, 650, 170, "g", BR)
    E.escreve(c, "a diferença diz quantos sobram", 84, 960, 100, "i", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_de_cabeca", a), ("capa_B_fatorial", b), ("capa_C_diferenca", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
