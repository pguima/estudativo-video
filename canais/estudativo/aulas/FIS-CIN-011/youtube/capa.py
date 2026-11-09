"""Capas do FIS-CIN-011 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o erro: o gráfico não é o caminho
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.55)
    E.escreve(c, "a reta sobe:", 84, 400, 140, "g", BR)
    E.escreve(c, "o carro sobe?", 84, 580, 150, "g", AMARELO)
    E.escreve(c, "não: é o gráfico s × t", 84, 760, 84, "i", claro)
    ox, oy = 1150, 900
    M.arrow(c, ox, oy, 1860, oy, BR, 1.0, 8, 30, 1.0)
    M.arrow(c, ox, oy, ox, 260, BR, 1.0, 8, 30, 1.0)
    M.line(c, ox, oy, 1780, 360, AMARELO, 1.0, 16)
    E.escreve(c, "t", 1830, oy + 80, 70, "i", BR); E.escreve(c, "s", ox - 70, 300, 70, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Gráfico", "s × t", "posição por tempo")


def d(c):  # o macete: inclinação = velocidade
    palco(c)
    E.escreve(c, "mais em pé,", 84, 330, 120, "i", BR)
    E.escreve(c, "mais rápido", 76, 520, 170, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    ox, oy = 1150, 980
    M.arrow(c, ox, oy, 1860, oy, BR, 1.0, 8, 30, 1.0)
    M.arrow(c, ox, oy, ox, 300, BR, 1.0, 8, 30, 1.0)
    M.line(c, ox, oy, 1500, 380, COR, 1.0, 16)
    M.line(c, ox, oy, 1800, 760, claro, 1.0, 16)
    E.escreve(c, "inclinação = velocidade", 84, 900, 76, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_carro_sobe", a), ("capa_B_grafico_s_t", b), ("capa_C_mais_em_pe", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
