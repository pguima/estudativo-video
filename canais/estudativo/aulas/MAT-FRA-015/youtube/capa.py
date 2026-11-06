"""Capas do MAT-FRA-015 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o resultado que a vírgula enganou
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.numero(c, "2,35", 640, 400, 200, "g", BR)
    E.escreve(c, "+", 120, 600, 200, "g", BR)
    E.numero(c, "1,4", 640, 600, 200, "g", BR)
    E.numero(c, "2,49", 640, 850, 220, "g", AMARELO)
    E.risco(c, 300, 870, 1000, 680, 9, 0, BR, 30)
    E.escreve(c, "a vírgula", 1060, 480, 170, "i", BR)
    E.escreve(c, "te enganou?", 1060, 640, 130, "g", BR)
    E.escreve(c, "3,75", 1140, 860, 230, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Somar e", "subtrair", "decimais")


def d(c):  # o macete: suba do preço até a nota
    escuro(c)
    E.escreve(c, "o atalho", 84, 340, 150, "i", BR)
    E.escreve(c, "do troco", 76, 570, 240, "g", BR)
    E.escreve(c, "10 − 3,25", 84, 780, 150, "g", BR)
    E.escreve(c, "= 6,75", 860, 780, 170, "g", AMARELO)
    E.escreve(c, "suba do preço até a nota", 84, 960, 130, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_virgula_te_enganou", a), ("capa_B_somar_subtrair", b), ("capa_C_atalho_do_troco", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
