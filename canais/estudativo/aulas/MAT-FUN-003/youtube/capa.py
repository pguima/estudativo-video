"""Capas do MAT-FUN-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: f(x) = 30 não é trocar x por 30
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "f(x) = 30", 84, 470, 230, "g", BR)
    E.escreve(c, "x = 63?", 84, 740, 200, "g", AMARELO)
    E.risco(c, 70, 700, 760, 640, 9, 0, "#FF4D55", 18)
    E.escreve(c, "a pegadinha do f(x)", 84, 950, 110, "i", BR)
    E.centro(c, "x = 13,5", 1500, 690, 150, "g", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Notação", "f(x)", "do zero")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "desfaça", 76, 450, 220, "g", BR)
    E.escreve(c, "de trás para a frente", 84, 620, 120, "i", claro)
    y = 860
    E.centro(c, "30", 220, y, 120, "g", BR)
    E.centro(c, "− 3", 520, y - 70, 70, "g", AMARELO)
    M.arrow(c, 340, y - 40, 700, y - 40, claro, 1, 8, 28)
    E.centro(c, "27", 830, y, 120, "g", BR)
    E.centro(c, "÷ 2", 1130, y - 70, 70, "g", AMARELO)
    M.arrow(c, 950, y - 40, 1310, y - 40, claro, 1, 8, 28)
    E.centro(c, "13,5", 1520, y, 120, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_pegadinha_f_de_x", a), ("capa_B_notacao_f_de_x", b), ("capa_C_desfaca_de_tras", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
