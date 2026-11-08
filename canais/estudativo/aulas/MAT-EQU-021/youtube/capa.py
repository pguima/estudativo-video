"""Capas do MAT-EQU-021 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o problema da padaria
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "suco + pão = R$ 9", 84, 400, 150, "g", BR)
    E.escreve(c, "2 sucos + pão = R$ 14", 84, 620, 150, "g", BR)
    E.escreve(c, "quanto custa o suco?", 84, 900, 160, "i", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "sistemas", "preços e quantidades")


def d(c):  # o macete: a diferença entre as compras
    palco(c)
    E.escreve(c, "a diferença é o suco", 84, 360, 140, "i", BR)
    E.escreve(c, "14 − 9 = 5", 84, 680, 280, "g", AMARELO)
    E.escreve(c, "sem montar nada", 84, 920, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quanto_custa_o_suco", a), ("capa_B_praticando_sistemas", b), ("capa_C_a_diferenca", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
