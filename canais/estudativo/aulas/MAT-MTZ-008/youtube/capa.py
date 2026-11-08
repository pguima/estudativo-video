"""Capas do MAT-MTZ-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: só com determinantes
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "sistema só com", 84, 400, 130, "i", BR)
    E.escreve(c, "determinantes", 76, 580, 180, "g", BR)
    E.formula(c, "x = f{Dx}{D}", 84, 860, 170, "g", AMARELO)
    G = E.matriz(c, 9, 0, [[5, 1], [3, 1]], 1500, 820, 130, barras=True, escuro=True, cor=BR, cores={("c", 0): AMARELO})
    E.escreve(c, "Dx", 1440, G.y0 - 30, 80, "g", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Regra de", "Cramer", "sistema como matriz")


def d(c):  # o atalho: só uma letra
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a questão quer só o x?", 84, 380, 120, "i", BR)
    E.escreve(c, "2 contas e pronto", 76, 580, 180, "g", BR)
    E.formula(c, "x = f{Dx}{D}", 84, 880, 160, "g", AMARELO)
    E.escreve(c, "nem precisa do y", 820, 860, 90, "i", E.mix(COR, BR, 0.6))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_so_determinantes", a), ("capa_B_regra_de_cramer", b), ("capa_C_so_uma_letra", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
