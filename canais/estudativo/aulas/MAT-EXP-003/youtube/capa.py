"""Capas do MAT-EXP-003 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF4D55"


def a(c):  # o gancho: 80 mg, 12 horas, acabou?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "80 mg, metade a cada 6 h", 84, 330, 76, "i", BR)
    E.escreve(c, "12 h:", 84, 560, 170, "g", BR)
    E.escreve(c, "0 mg?", 84 + E.larg("12 h:", "g", 170) + 50, 560, 170, "g", VERMELHO)
    E.risco(c, 84 + E.larg("12 h:", "g", 170) + 30, 520, 84 + E.larg("12 h:", "g", 170) + 50 + E.larg("0 mg?", "g", 170) + 20, 470, 1, 0,
            AMARELO, 26)
    E.escreve(c, "sobram 20 mg", 84, 820, 150, "g", AMARELO)
    for i, mg in enumerate((80, 40, 20)):
        M.rrect(c, 1250, 260 + 190 * i, mg * 7.2, 110, 24, BR if i < 2 else AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Meia-vida", "e dobras", "quanto resta?")


def d(c):  # o atalho: 10 dobras = ×1.000
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho:", 84, 360, 120, "i", claro)
    E.escreve(c, "10 dobras", 76, 580, 200, "g", BR)
    E.escreve(c, "≈ ×1.000", 76, 800, 200, "g", AMARELO)
    E.formula(c, "2^{10} = 1.024", 1180, 980, 90, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_80mg_12h", a), ("capa_B_meia_vida", b), ("capa_C_10_dobras", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
