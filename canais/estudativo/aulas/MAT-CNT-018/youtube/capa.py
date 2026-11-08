"""Capas do MAT-CNT-018 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
AMBAR = "#E8920C"
COR = E.MATERIAS["Matemática"]["cor"]


def gene(c, cx, cy, letra, size):
    E.pilula(c, letra, cx, cy, size, estilo="g", fundo=BR if letra == "A" else AMARELO, cor=COR)


def a(c):  # o gancho: pai Aa e mãe Aa, filho aa com chance 1/4
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "pai", 120, 330, 90, "i", BR)
    gene(c, 420, 300, "A", 84); gene(c, 600, 300, "a", 84)
    E.escreve(c, "mãe", 120, 520, 90, "i", BR)
    gene(c, 420, 490, "A", 84); gene(c, 600, 490, "a", 84)
    E.escreve(c, "filho", 120, 790, 110, "g", BR)
    gene(c, 560, 755, "a", 96); gene(c, 760, 755, "a", 96)
    E.escreve(c, "?", 870, 800, 130, "g", AMARELO)
    E.bola(c, 1380, 560, 280, "#FFFFFF")
    E.fracao(c, 1, 4, 1380, 550, 230, COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "A árvore", "das chances", "multiplique e some")


def d(c):  # o macete: ao longo multiplica, entre soma
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "ao longo do caminho:", 84, 420, 110, "i", BR)
    E.escreve(c, "×", 1180, 440, 200, "g", AMARELO)
    E.escreve(c, "entre caminhos:", 84, 760, 110, "i", BR)
    E.escreve(c, "+", 1180, 780, 200, "g", AMARELO)
    E.escreve(c, "a regra da árvore", 84, 1000, 90, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_filho_aa", a), ("capa_B_arvore_chances", b), ("capa_C_vezes_mais", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
