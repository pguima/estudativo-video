"""Capas do MAT-MTZ-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 2 ou −2?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.matriz(c, 9, 0, [[1, 2], [3, 4]], 420, 560, 210, cor=BR, barras=True, escuro=True)
    E.escreve(c, "= 2", 820, 520, 200, "g", BR)
    E.risco(c, 800, 560, 1180, 380, 9, 0, AMARELO, 30)
    E.escreve(c, "−2", 1300, 640, 300, "g", AMARELO)
    E.escreve(c, "a ordem da conta muda tudo", 84, 960, 96, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Determinante", "e Sarrus", "sem decorar")


def d(c):  # o atalho: só a diagonal
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "det em 3 segundos:", 84, 380, 130, "i", BR)
    E.escreve(c, "só a diagonal", 76, 590, 190, "g", BR)
    G = E.matriz(c, 9, 0, [[2, 5, 7], [0, 3, 1], [0, 0, 4]], 480, 880, 86, barras=True, escuro=True,
                 cores={(1, 0): AMARELO, (2, 0): AMARELO, (2, 1): AMARELO})
    E.escreve(c, "= 2·3·4 = 24", 900, 880, 140, "g", E.mix(COR, BR, 0.6))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_2_ou_menos_2", a), ("capa_B_determinante_e_sarrus", b), ("capa_C_so_a_diagonal", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
