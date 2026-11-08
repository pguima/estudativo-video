"""Capas do MAT-EQU-016 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: empata com 70, então a resposta é 70? não
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "empatam com 70 min.", 84, 380, 120, "i", BR)
    E.escreve(c, "a partir de quantos", 84, 560, 140, "g", BR)
    E.escreve(c, "fica mais barato?", 84, 720, 140, "g", BR)
    E.escreve(c, "70", 84, 960, 200, "g", AMARELO)
    E.risco(c, 70, 980, 340, 800, 9, 0, BR, 26)
    E.escreve(c, "71!", 420, 960, 200, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Inequação", "na prática", "e a dupla")


def d(c):  # o macete: empate e depois o lado
    escuro(c)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.escreve(c, "ache o empate", 84, 580, 170, "g", BR)
    E.escreve(c, "e escolha o lado", 84, 790, 170, "g", AMARELO)
    E.escreve(c, "35 ÷ 0,5 = 70 minutos", 84, 980, 100, "i", BR)


NOMES = (("capa_A_a_partir_de_quantos", a), ("capa_B_inequacao_na_pratica", b), ("capa_C_empate_e_lado", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in NOMES:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
