"""Capas do MAT-POR-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: R$ 30 de desconto em R$ 120 não é 30%
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "R$ 30 de desconto", 84, 380, 150, "g", BR)
    E.escreve(c, "em R$ 120", 84, 530, 150, "g", BR)
    E.escreve(c, "30%?", 84, 840, 230, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 880, 560, 640, 9, 0, AMARELO, 30)
    E.bola(c, 1420, 760, 240, AMARELO)
    E.centro(c, "25%", 1420, 815, 150, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Quantos %", "e o total", "parte ÷ total")


def d(c):  # o atalho: o total vira 100
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o total", 84, 340, 140, "i", BR)
    E.escreve(c, "vira 100", 84, 560, 210, "g", BR)
    E.fracao(c, 17, 50, 300, 800, 150, E.mix(COR, BR, 0.55))
    M.arrow(c, 470, 820, 640, 820, BR, 1, 8, 26)
    E.escreve(c, "× 2", 470, 770, 64, "g", BR)
    E.fracao(c, 34, 100, 810, 800, 150, BR)
    E.escreve(c, "= 34%", 1000, 860, 170, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_30_ou_25", a), ("capa_B_quantos_por_cento", b), ("capa_C_total_vira_100", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
