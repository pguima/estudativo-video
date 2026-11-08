"""Capas do MAT-POR-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 15% de 80 de cabeça
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "15% de 80", 84, 440, 230, "g", BR)
    E.escreve(c, "de cabeça, em segundos", 90, 600, 110, "i", BR)
    E.escreve(c, "10% = 8", 84, 820, 130, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "5% = 4", 84, 960, 130, "g", E.mix(COR, BR, 0.55))
    E.bola(c, 1480, 860, 170, AMARELO)
    E.centro(c, "12", 1480, 920, 170, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Calcular", "porcentagem", "de cabeça e na conta")


def d(c):  # o atalho: troque a ordem
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 380, 150, "i", BR)
    E.escreve(c, "8% de 50", 84, 600, 200, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "=", 84, 820, 200, "g", BR)
    E.escreve(c, "50% de 8", 300, 820, 200, "g", BR)
    E.escreve(c, "= 4", 1290, 820, 200, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_15_de_80", a), ("capa_B_calcular_porcentagem", b), ("capa_C_troque_a_ordem", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
