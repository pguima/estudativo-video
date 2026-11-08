"""Capas do MAT-EST-012 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF5A5A"
NOTAS = [(4, 2), (6, 4), (7, 5), (8, 6), (9, 3)]


def tabela(c, x, y, cor=BR, destaque=None):
    """a tabela nota × alunos em branco; destaque = linha em amarelo"""
    E.centro(c, "nota", x + 90, y, 54, "i", cor, 0.85)
    E.centro(c, "alunos", x + 300, y, 54, "i", cor, 0.85)
    M.line(c, x, y + 26, x + 400, y + 26, cor, 1, 4)
    for j, (n, k) in enumerate(NOTAS):
        cc = AMARELO if j == destaque else cor
        E.centro(c, str(n), x + 90, y + 120 + 104 * j, 84, "g", cc)
        E.centro(c, str(k), x + 300, y + 120 + 104 * j, 84, "g", cc)


def a(c):  # o gancho: não escreva a lista
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "não escreva", 84, 360, 120, "i", BR)
    E.escreve(c, "a lista!", 84, 550, 180, "g", BR)
    E.escreve(c, "a tabela já", 84, 760, 110, "g", BR)
    E.escreve(c, "responde", 84, 900, 140, "g", AMARELO)
    tabela(c, 1300, 280, destaque=2)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Média, mediana", "e moda", "numa tabela")


def d(c):  # o atalho: base 7
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "média sem conta grande:", 84, 360, 100, "i", BR)
    E.escreve(c, "base 7", 84, 560, 170, "g", AMARELO)
    E.formula(c, "7 + f{2}{20} = 7,1", 84, 820, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_escreva_a_lista", a), ("capa_B_media_mediana_moda_tabela", b), ("capa_C_atalho_da_base", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
