"""Capas do MAT-FRA-017 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: colar o resto depois da vírgula
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "7 ÷ 4 =", 84, 480, 240, "g", BR)
    E.escreve(c, "1,3", 1000, 480, 280, "g", BR)
    E.risco(c, 970, 520, 1530, 230, 9, 0, AMARELO, 34)
    E.escreve(c, "1,75", 1200, 760, 280, "g", AMARELO)
    E.escreve(c, "o resto ainda", 84, 710, 130, "i", BR)
    E.escreve(c, "precisa dividir", 84, 850, 104, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Dividir", "decimais", "até o resto acabar")


def d(c):  # o macete: metade da metade
    escuro(c)
    E.escreve(c, "dividir por 4?", 84, 340, 150, "i", BR)
    E.escreve(c, "metade da", 76, 540, 190, "g", BR)
    E.escreve(c, "metade", 76, 720, 190, "g", BR)
    E.escreve(c, "7", 84, 950, 170, "g", BR)
    E.escreve(c, "3,50", 370, 950, 170, "g", BR)
    E.escreve(c, "1,75", 960, 950, 170, "g", AMARELO)
    for x in (225, 815):
        M.arrow(c, x, 890, x + 100, 890, BR, 1.0, 8, 26)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_resto_nao_fica", a), ("capa_B_dividir_decimais", b), ("capa_C_metade_da_metade", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
