"""Capas do MAT-NUM-012 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 11 ônibus não levam todo mundo
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "500 alunos", 84, 330, 130, "g", BR)
    E.escreve(c, "ônibus de 42 lugares", 84, 450, 100, "i", BR)
    E.escreve(c, "11 ônibus?", 84, 650, 210, "g", AMARELO)
    E.risco(c, 70, 690, 1140, 520, 9, 0, BR, 30)
    E.escreve(c, "o resto não some", 84, 900, 130, "i", BR)
    E.escreve(c, "12", 1420, 820, 380, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Exercícios", "4 operações", "pause e resolva")


def d(c):  # os atalhos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "contas de cabeça", 84, 360, 130, "i", BR)
    E.escreve(c, "99 × 7", 84, 600, 190, "g", BR)
    E.escreve(c, "= 700 − 7", 760, 600, 150, "g", AMARELO)
    E.escreve(c, "48 × 5", 84, 860, 190, "g", BR)
    E.escreve(c, "= 480 ÷ 2", 760, 860, 150, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_onze_onibus", a), ("capa_B_exercicios", b), ("capa_C_contas_de_cabeca", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
