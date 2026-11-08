"""Capas do MAT-EQU-015 (1280x720). Uso: python capa.py"""
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


def a(c):  # o erro: −2x < 6 não dá x < −3
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "−2x < 6", 84, 470, 230, "g", BR)
    E.formula(c, "x < −3", 1020, 470, 230, "g", BR)
    E.risco(c, 990, 520, 1800, 330, 9, 0, AMARELO, 30)
    E.escreve(c, "por que o sinal vira?", 84, 860, 140, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Inequação", "do 1º grau", "do zero")


def d(c):  # o macete: teste o zero
    escuro(c)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.escreve(c, "teste o", 84, 620, 220, "g", BR)
    E.escreve(c, "0", 830, 640, 300, "g", AMARELO)
    E.escreve(c, "e descubra se o sinal está certo", 84, 920, 100, "i", BR)


NOMES = (("capa_A_por_que_o_sinal_vira", a), ("capa_B_inequacao_do_zero", b), ("capa_C_teste_o_zero", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in NOMES:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
