"""Capas do MAT-TOP-015 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o 5 inventado da calculadora
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "2,5 × 3,14 =", 84, 400, 150, "g", BR)
    E.escreve(c, "7,85", 84, 720, 300, "g", BR)
    x5 = 84 + E.larg("7,8", "g", 300)
    E.risco(c, x5 + 10, 740, x5 + 180, 470, 9, 0, AMARELO, 34)
    E.escreve(c, "7,9", 1180, 720, 300, "g", AMARELO)
    E.escreve(c, "o 5 é inventado", 84, 940, 110, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Algarismos", "que valem", "numa medida")


def d(c):  # o macete: notação científica
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "0,0", 84, 420, 200, "g", "#77778A")
    E.escreve(c, "420", 84 + E.larg("0,0", "g", 200), 420, 200, "g", BR)
    E.formula(c, "= 4,20 × 10^{−2}", 84, 680, 170, "g", "#3CC7D3")
    E.escreve(c, "3 significativos", 84, 930, 130, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_5_inventado", a), ("capa_B_algarismos_significativos", b), ("capa_C_notacao_cientifica", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
