"""Capas do MAT-EQU-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: x = 4 resolve 2x + 1 = 9?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "2x + 1 = 9", 84, 470, 240, "g", BR)
    E.escreve(c, "x = 4?", 84, 760, 230, "g", AMARELO)
    E.escreve(c, "confira em 5 segundos", 84, 960, 110, "i", BR)
    E.bola(c, 1600, 600, 190, AMARELO); E.centro(c, "?", 1600, 690, 260, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Equação", "é balança", "nos dois lados")


def d(c):  # o atalho: teste as alternativas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 360, 150, "i", BR)
    E.escreve(c, "teste as", 76, 560, 200, "g", BR)
    E.escreve(c, "alternativas", 76, 760, 200, "g", BR)
    for i, (s, ok) in enumerate((("A) 3", False), ("B) 4", True), ("C) 5", False))):
        x = 330 + i * 420
        E.pilula(c, s, x, 930, 90, "g", fundo=E.CERTO if ok else E.mix(COR, BR, 0.25), cor=BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_x_vale_4", a), ("capa_B_equacao_balanca", b), ("capa_C_teste_alternativas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
