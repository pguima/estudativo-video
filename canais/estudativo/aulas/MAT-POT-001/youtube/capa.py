"""Capas do MAT-POT-001 (1280x720). Uso: python capa.py"""
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
CLARO = E.mix(COR, BR, 0.5)


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: 2 elevado a 5 não é 10
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "2^5", 84, 640, 400, cor=BR)
    E.escreve(c, "=", 560, 590, 240, "g", BR)
    E.escreve(c, "10", 770, 640, 400, "g", AMARELO)
    E.escreve(c, "?", 1350, 640, 400, "g", BR)
    E.risco(c, 750, 660, 1310, 330, 9, 0, largura=26)
    E.escreve(c, "o erro mais comum", 84, 950, 170, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "O que é", "potência", "do zero")


def d(c):  # o macete: número terminado em 5
    escuro(c)
    E.escreve(c, "final 5?", 84, 370, 170, "i", BR)
    E.escreve(c, "de cabeça", 84, 560, 170, "g", BR)
    w = E.formula(c, "35^2 =", 84, 880, 240, cor=BR)
    E.formula(c, "1.225", 84 + w + 36, 880, 240, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_erro_mais_comum", a), ("capa_B_o_que_e_potencia", b), ("capa_C_final_cinco", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
