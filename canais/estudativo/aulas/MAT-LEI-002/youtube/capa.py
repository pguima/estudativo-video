"""Capas do MAT-LEI-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: "3 a mais que x" não é 3x
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 a mais que x", 84, 400, 170, "g", BR)
    E.escreve(c, "3x", 84, 680, 220, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 700, 420, 500, 9, 0, AMARELO, 30)
    E.escreve(c, "x + 3", 560, 680, 220, "g", AMARELO)
    E.escreve(c, "uma palavra muda a conta", 84, 900, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Palavras", "que mudam", "a conta")


def d(c):  # o atalho: troque a letra por 10
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "na dúvida, troque", 84, 350, 130, "i", BR)
    E.escreve(c, "x por 10", 76, 600, 230, "g", BR)
    E.escreve(c, "10 + 3 = 13", 84, 850, 130, "g", AMARELO)
    E.escreve(c, "3 × 10 = 30", 1000, 850, 130, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 985, 840, 1660, 780, 9, 0, "#E5484D", 22)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_3_a_mais_nao_e_3x", a), ("capa_B_palavras_que_mudam", b), ("capa_C_troque_por_10", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
