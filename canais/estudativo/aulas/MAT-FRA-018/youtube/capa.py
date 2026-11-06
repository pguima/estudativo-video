"""Capas do MAT-FRA-018 (1280x720). Uso: python capa.py"""
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



def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: dividiu e cresceu
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "1,5 ÷ 0,25", 84, 470, 230, "g", BR)
    E.escreve(c, "= 6", 1290, 470, 230, "g", AMARELO)
    E.escreve(c, "dividiu", 84, 720, 200, "i", BR)
    E.escreve(c, "e cresceu?", 720, 720, 200, "g", AMARELO)
    E.escreve(c, "sem medo da vírgula", 84, 950, 130, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Dividir por", "decimal", "sem medo da vírgula")


def d(c):  # o macete: dividir por 0,25 é multiplicar por 4
    palco(c)
    E.escreve(c, "÷ 0,25", 84, 450, 250, "g", BR)
    E.escreve(c, "é", 930, 450, 200, "i", BR)
    E.escreve(c, "× 4", 1110, 450, 250, "g", AMARELO)
    E.escreve(c, "÷ 0,5", 84, 720, 200, "g", BR)
    E.escreve(c, "é", 780, 720, 170, "i", BR)
    E.escreve(c, "× 2", 950, 720, 200, "g", AMARELO)
    E.escreve(c, "o atalho de prova", 84, 930, 150, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dividiu_e_cresceu", a), ("capa_B_dividir_por_decimal", b), ("capa_C_atalho_vezes_quatro", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
