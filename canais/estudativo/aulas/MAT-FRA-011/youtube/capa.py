"""Capas do MAT-FRA-011 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: dividiu e cresceu
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3", 84, 640, 300, "g", BR)
    E.escreve(c, "÷", 300, 610, 230, "g", BR)
    E.fracao(c, 1, 4, 650, 530, 270, BR)
    E.escreve(c, "=", 830, 610, 230, "g", BR)
    E.escreve(c, "12", 1050, 650, 340, "g", AMARELO)
    E.escreve(c, "?", 1560, 640, 320, "g", BR)
    E.escreve(c, "dividiu e cresceu", 84, 985, 170, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Dividir", "frações", "quantas vezes cabe")


def d(c):  # o atalho: fração com 1 em cima
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 370, 170, "i", BR)
    y = 660
    E.escreve(c, "÷", 84, y + 80, 230, "g", BR)
    E.fracao(c, 1, 4, 410, y, 270, BR)
    E.escreve(c, "é", 600, y + 70, 200, "i", BR)
    E.escreve(c, "× 4", 780, y + 100, 340, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dividiu_e_cresceu", a), ("capa_B_dividir_fracoes", b), ("capa_C_um_em_cima", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
